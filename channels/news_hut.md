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
<img src="https://cdn4.telesco.pe/file/qv0zHbFY8WTyRl5HgTZnlUKwbG-AfVRELkqLCWAB3zXRVAUCgw81BUV1NhqjpcKdxfK7g3RFj3IGQm9CLEe4io5rvN9KI3kRF0IEonhUtDiN1V63P6PxnBCVvDoyvnWe_3Q8hKkdP06mTszOxfa84PBN5FgIk7B9cRq3JgCj3cLNI-cK0MKqQPoe-Qrd5capcZBMHutNnIgFK3Bop36PLZdls-Mte7CUhzuEbA0dU7qE5Y2hRXe5LhgR1kz6S3LFASkrpJAndUobZzZ6rKraxKKLrWjMeyxwpcGx2KG_XYyz_b9cQBfowkT50Umxp6kI-j5_ayVTAe4FqnokEWrEfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 21:56:54</div>
<hr>

<div class="tg-post" id="msg-71206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=DGVfqA9P-2l6Ft0TS6-hx9ZUs1MvB2KfAQuCuNF81DfssG-ycGa9J84tGHuxH0Qd1FjdVPUANdOYzP_eGipHjTyAh-2SpooYUkFzHwflvY9JAQiUzMP0Wkshqtw3pggX7IBXd_JhSkvtDKb9oS9aQ18GwTin5FwhImVXowCIMbiFdj3vJf_UaQRpTsxGhB0vC1k2CWEgpqbcvU-ucYmuYLXlEwUsP_-67BJs9BaKhZfgE3IBEgvBcKkdJQBD3MveW4zgjOlGMnPSdO_ztiZyvYLLRzblOqg7LPZ3-ZDv6yQAlYN8stKOCQZbTb1kHTtz7fxsuOudmR9TMbXLNxSXGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=DGVfqA9P-2l6Ft0TS6-hx9ZUs1MvB2KfAQuCuNF81DfssG-ycGa9J84tGHuxH0Qd1FjdVPUANdOYzP_eGipHjTyAh-2SpooYUkFzHwflvY9JAQiUzMP0Wkshqtw3pggX7IBXd_JhSkvtDKb9oS9aQ18GwTin5FwhImVXowCIMbiFdj3vJf_UaQRpTsxGhB0vC1k2CWEgpqbcvU-ucYmuYLXlEwUsP_-67BJs9BaKhZfgE3IBEgvBcKkdJQBD3MveW4zgjOlGMnPSdO_ztiZyvYLLRzblOqg7LPZ3-ZDv6yQAlYN8stKOCQZbTb1kHTtz7fxsuOudmR9TMbXLNxSXGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مجری لبنانی:
مجتبی خامنه‌ای، رهبر عالی و ولی‌فقیه، اگر به بیروت بیاید باید بداند که هویت ما عربی است، نه فارسی.
بگذارید این را به روشنی دریابد: اینجا بیروت است، نه تهران؛
اینجا پایتختی عربی و آزاد است و هرگز به پایتختی فارسی بدل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/news_hut/71206" target="_blank">📅 21:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
⭕️
#فوری
؛ نرخ سوم بنزین تغییر کرد
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد سه‌شنبه به ۱۰ هزار تومان افزایش خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/news_hut/71205" target="_blank">📅 21:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71201">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2YseL0kAXk99M1o8Q1fEwWA2Xc8nwLzVsnBqsveJoqjbcXdo1N_FtzepdsYiGfumcrho2R1WvLyVdx_fL9K0vC_ljznLnTV1ANDvMFao7TcUM3J04Hwo1uaaHPJcfXJP27RwY2VZK5ztRz38VmUNL2ICUgGTd-cqmvDkInBR-WqOn8gQnj9oJDprGRy80nRgLKNA-Ec8ROoU9_x62LTfHFLhFbQ0rL5s8Oo1DvbcRMyvw7YieRz2KOvJGiR7Ak8W4TxslQZW9v4QOHD3rkit6vozZwW__TTA2p5uQCV30WQJO-RjLnlJ9_CPrMlg9MHnKOJqPLByy2Njjayuq3NJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzjJAxlueh9m-oIY44YGDioqrRjhtco0Tfb8qSJKIiafryf_RbwLGVBvYx_M_CJ3CotMJSP_iCPXzjQzerrY7mJl82RfFn7J7sYnQlsXo8F5sj0hBy5vxHjcPFk9MPErGOwjQF6aD7vlAQ6dnc0SsFW5BKIcPU5MBI10pE95UVoalZm2SVPYl3uUzBGwXZX5H6GCx0iCE22L0o6je-vRQzIQM8VsLXserz8sBQ-G4Z55mDEjCYj4Y4TECrDqymqcw-eTfKfVLfGBv6QJ2SbsLjlrVLUHIKEZlG8b-2GhxOQ3EkqXhtLfoBZtJ5Ek0dkGtVumW0cFTn9hhNd1KcG8GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=cY36qWDIkcS3UIl-PyA-j91I7H_HKAE8u_TOz3iQL1mUs0lhCdC1GQlL84QmKCMIr1rJvHPgayKtt4mB9nkhSmK6vOF-UBXWPscxLus9uiwV2EGejicoSZrauEuQr_k8LXYKa4fG4u-GElw7kwaL77eyoy_AV0boJ3GDt9jQWTNg6FpnXNdpLkSrJBvWjnOMENjoUDte_rPm84L27aLtW-I6IOt-5VTPKywgPn6qXDjvQBN1BasmQ_pG1Wz3HLVOSN3b_yq2QVe41nHP-y-JHrvrdMU0XfntanvqcfOvstm0QnortDpHekDb-TfjHq7p-_d6YwJMGxWRTTgFLo1qTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=cY36qWDIkcS3UIl-PyA-j91I7H_HKAE8u_TOz3iQL1mUs0lhCdC1GQlL84QmKCMIr1rJvHPgayKtt4mB9nkhSmK6vOF-UBXWPscxLus9uiwV2EGejicoSZrauEuQr_k8LXYKa4fG4u-GElw7kwaL77eyoy_AV0boJ3GDt9jQWTNg6FpnXNdpLkSrJBvWjnOMENjoUDte_rPm84L27aLtW-I6IOt-5VTPKywgPn6qXDjvQBN1BasmQ_pG1Wz3HLVOSN3b_yq2QVe41nHP-y-JHrvrdMU0XfntanvqcfOvstm0QnortDpHekDb-TfjHq7p-_d6YwJMGxWRTTgFLo1qTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
حملات شبانه جنگنده های اسرائیلی به ارتفاعات علی الطاهر و نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/news_hut/71201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71200">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a237cee509.mp4?token=VvhekB5CYjsJHaIzsInK7WoTiGtIRTnNlNoH3f9L-A2WTAzlq8bblpodTd2iq4tb_UZssGoaH0WxYNYcVY29uBQKIz3wvlfmVBRc1RIepXBagrq_xsFOjRn-bmokZdmkX9-ZuWTpGcL-46bODnvWJI4BNz2jT6vY8bbzMOzUT6r8msaqc-bL62ahcX-Aswf6Y9hEB55IjOpECXDmAB4_5opSTll0RDmCY5nzmaRPxtJ0ljamw-SW8M4hBz2LzfKrfi9sCTxaW31xp-ciRW_bk91U1z6-lr8f3vftT5LNGRJZeUE7DstS8NfF2yUlnVotw4ZoaAWNpy0JwTscNQuakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a237cee509.mp4?token=VvhekB5CYjsJHaIzsInK7WoTiGtIRTnNlNoH3f9L-A2WTAzlq8bblpodTd2iq4tb_UZssGoaH0WxYNYcVY29uBQKIz3wvlfmVBRc1RIepXBagrq_xsFOjRn-bmokZdmkX9-ZuWTpGcL-46bODnvWJI4BNz2jT6vY8bbzMOzUT6r8msaqc-bL62ahcX-Aswf6Y9hEB55IjOpECXDmAB4_5opSTll0RDmCY5nzmaRPxtJ0ljamw-SW8M4hBz2LzfKrfi9sCTxaW31xp-ciRW_bk91U1z6-lr8f3vftT5LNGRJZeUE7DstS8NfF2yUlnVotw4ZoaAWNpy0JwTscNQuakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زاکانی:از وصیت‌نامه علی خامنه‌ای خبری نیست، احتمالا در بمباران از بین رفته.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/71200" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71199">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90305378ee.mp4?token=FUzlLnKc86Yn730gVui_s_g3clg_jiW_35ML7UH7nqvgYDQ--ta-uKIFUvHV1dB8UJplGrak82iOEpCFZRsLib7mvLm6IBI6gy6b_s6eX0M39EawizpUZPKEYiXpBwfroie9tIbkdBayqKuGHkrZbHbJeiL0OzzsE-i2ELiotAwrganey2qokIyvbPE3CRM5Zrat55kqAvEqSt0Xh3jyHrkdrc_UJa9XNNubMyMBNirVKkjBQFJBeKTpf3Oi2WQxqoNLA1Sa5SLyjfWWEhxZ2oMdGrWYumJ4T5NZNX50sxl3cMQdOj1OgS6r7MeP6o6LAKTqPNKuMaL6YdoYVdomtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90305378ee.mp4?token=FUzlLnKc86Yn730gVui_s_g3clg_jiW_35ML7UH7nqvgYDQ--ta-uKIFUvHV1dB8UJplGrak82iOEpCFZRsLib7mvLm6IBI6gy6b_s6eX0M39EawizpUZPKEYiXpBwfroie9tIbkdBayqKuGHkrZbHbJeiL0OzzsE-i2ELiotAwrganey2qokIyvbPE3CRM5Zrat55kqAvEqSt0Xh3jyHrkdrc_UJa9XNNubMyMBNirVKkjBQFJBeKTpf3Oi2WQxqoNLA1Sa5SLyjfWWEhxZ2oMdGrWYumJ4T5NZNX50sxl3cMQdOj1OgS6r7MeP6o6LAKTqPNKuMaL6YdoYVdomtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇵🇰
بلاتکلیفی بیش از یک‌هفته‌ای صدها راننده ترانزیت ایرانی در نقطه صفر مرزی پاکستان
این سنگین‌سواران ١۴ شهریور در ویدیویی گفتند که بی آب، غذا و امکانات بهداشتی به حال خود رها شده‌اند. با اتمام سوخت یخچال‌ها، بارهای فاسدشدنی در آستانه نابودی است و گمرک هیچ‌یک از دو کشور پاسخگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/71199" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71198">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بیناموسا مگه نگفتین از امروز برق نمی‌ره؟ رفت که
#hjAly‌</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/71198" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71197">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=R32tAAZRpyoBYDUbqMVi7gNTcD245QLMIo4edxsH48cNcWbAlKoDOg-6G69L_EQxbJ85PoHjut7YjdAbUtU6pWBqx8VBjj9XKyRQCTqnILXoH34a2G4mu9oq6BT9LwFHu9Xp5pz3b1T3MBBXBy_HX3sJJcfAL2ZooTKpH9COmF63yD1E8b4103mID3HfqcOiQQ7Nqlfp_0DyVdTI9aRB9PP8XzqNDK6RFnSdoiQRxS2KeQlePVX0QCPE2tYnCfX_GCqds0FUjrROZXsePlQer2WwxmIah6sXgq26jom4p6uOPzBsPHSQjwxF6IzdPo8OJtmfbDXQm1wjMgaZjBuk9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=R32tAAZRpyoBYDUbqMVi7gNTcD245QLMIo4edxsH48cNcWbAlKoDOg-6G69L_EQxbJ85PoHjut7YjdAbUtU6pWBqx8VBjj9XKyRQCTqnILXoH34a2G4mu9oq6BT9LwFHu9Xp5pz3b1T3MBBXBy_HX3sJJcfAL2ZooTKpH9COmF63yD1E8b4103mID3HfqcOiQQ7Nqlfp_0DyVdTI9aRB9PP8XzqNDK6RFnSdoiQRxS2KeQlePVX0QCPE2tYnCfX_GCqds0FUjrROZXsePlQer2WwxmIah6sXgq26jom4p6uOPzBsPHSQjwxF6IzdPo8OJtmfbDXQm1wjMgaZjBuk9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
پایان این رژیم در ایران نزدیک است.
این رژیم ضعیف است، برای بقای خود می‌جنگد، متزلزل شده است و هنوز مأموریتی ناتمام باقی مانده که ما مصمم به انجام آن هستیم.
این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/71197" target="_blank">📅 19:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71196">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djTvA5MEvOW-qWoGwfTs9MZHjV4Fch2b9wnA1X3kRPUaxUvLkBiFqF-95hUpBrqsWPg_LO4onSbZ7RWi6xNLHvMNPJBE3ia63DzWYn7-xR-dxTolLRysrLFbaHmrv8b4d_4POlqtbLDURexDrxTa-HNMuwWh3zbnqJ5LIpjGFDZsMsvdWTCSL3Wfjm7xCnRzdh3FGpB2s4xpDRN5ZJydpHDYqABAyQTMCetWHhKhZ-VYpgqq9TRQGHqPkVs3RO2jAGZGt9CpRdMUGjEMwKUclL3FLX3egzo566mlQSgPJ1VJOcTkEmkJWXQPQY3ZxPYRGIX3PWCK9P1KV1FuiSE04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیس قالیباف به بسنت:
چرخ‌ها آماده. گرم کردن قبل از پرتاب:
دیزل ATH: فروش فوری
بزرگترین طلبکار شما: موفق باشید با Yentervention++
80میلیارد دلار کاهش می‌دهد: نام نروژ را به Americaway تغییر دهید
استخدام کم: بدهی به خدمات با DO[Israel's]W، طبق گفته عروسک‌گردان‌های شما
اوه. طرح نقطه‌ای فدرال رزرو قرمز چشمک می‌زند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/71196" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71195">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeAiQ91AkS-kG5UIlzucjcy-xadSCd4Bt97hods_8JivyUdsWx7t_okrKn_PFOiUMtxvU3OMBOr0xeoWE7KrkzT4ylH-paSvUwKiC9oeYblW-gSFyZgR1a8WFQoL6bT6jmkkshb4nis3tewriuLP3iFDPFs4PW4YMTZSc4LkOkcPuu5GTUoUupDMDkRlOo6_ISqolGTqUJBqTgZ2z2A2m-H7NJN1Wk6WA-h-dXIuBJj1ELqbDWKpnu35pvmpPPt7h7QgEwhiNUqkwjnV31NFzoh8G7KeOaSgp8hbLGMXLce4_iMcaEIN7In0KcScEw2wuvQkbgbMBqaLRr55WpAgNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
گویا املاکی موهاشو رنگ کرده
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71195" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71193">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbDx5bgKnUZ3ub3MqzE7Py9q2pRAKpkJu5usPjHdqz8jrcsylTfB_zMvuOnZ6pxeuExtz9ZyZ9CdNluW8Z4YeCZ_MlUXYXKET7vs_M-JJ_MGV8YHQXZ2TN2XjUKSpxdjbi_dVkPLbu7bB-LMlv5yHsGVZSCsNAzdHHlXnbrNRVIwH5tzCtdwwUs9pxcBIQKZvWGvuTGa0jtOp4oQJsM118cOlPI_UtKYwuf_6r81GCwzzi5L_1qSM7xgvSISERiOdoMwPgva4VnoD2zHutw-1f1THtNuc4Q7kuklh8Hn8bfih2sF_QNc9FgpQX6HbaAiCYvtrR_uWxlPRmK_PguG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=v-IyJHVCQD-XDOBcYutAPCC6m5R1CNeaQowWz8HnfbzDnJCFSU8ptHpaX9yAMhqf3VHJTSmITdH_sgCfybWI5m5B-WD0z6GITvHntXqwGO8dQ2VCen-7OkzAmxZD87zyt127p7NT56ygouEo2uCJbktrnsByu2AZKnNR2i4aoeR1KPZKqE9fvG2YH3Q_FobJejE4IsNBiDW0eQhgTeKXxbYnklKUBAbeGhSA9U31yYVihu3GI7TlQ9_d7wfuAdky5j6SYI8l0DuBGzu8_HSdVX87M8EpXa2p_0rLxB7cQL776cwxC5823sSv5KMW4_F0m7t18PRGPDjgQD9KfGJaKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=v-IyJHVCQD-XDOBcYutAPCC6m5R1CNeaQowWz8HnfbzDnJCFSU8ptHpaX9yAMhqf3VHJTSmITdH_sgCfybWI5m5B-WD0z6GITvHntXqwGO8dQ2VCen-7OkzAmxZD87zyt127p7NT56ygouEo2uCJbktrnsByu2AZKnNR2i4aoeR1KPZKqE9fvG2YH3Q_FobJejE4IsNBiDW0eQhgTeKXxbYnklKUBAbeGhSA9U31yYVihu3GI7TlQ9_d7wfuAdky5j6SYI8l0DuBGzu8_HSdVX87M8EpXa2p_0rLxB7cQL776cwxC5823sSv5KMW4_F0m7t18PRGPDjgQD9KfGJaKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
تو همه جای جهان هوش مصنوعی داره جای آدما رو میگیره ولی تو ایران برعکسه
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71193" target="_blank">📅 18:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71192">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=Z2u-76JdrCUDSpBAXxFuU1f5DYpY47JxNNGcWWeuGaWGXNqP62rEA6jBBRx8V2U959pHYcyIzIFPk2Ea3etdaKe_3GtZXHSXzmcBSMc_WW6lGKWrVbDuHsibRtOgv2NWUXLYOEXebtLer7xLpnM241MonXnVP4KewdAPBbAgmzTqXlA0F-tJiktjVT4d6L0bMHZISlpX4n-a1fAtjrhbalq2ieOTWWYaVKL21TzXIZyUvxZVIqTxcEMKK_mpgBxKsKWxCoLZvm7T8eJYuRb5JKn8VgjsYuq8WWLyVcdwqyHjsVa24pVJzEscUtsUSStzZtQ1ZG5ABW9sy9fSfmOQkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=Z2u-76JdrCUDSpBAXxFuU1f5DYpY47JxNNGcWWeuGaWGXNqP62rEA6jBBRx8V2U959pHYcyIzIFPk2Ea3etdaKe_3GtZXHSXzmcBSMc_WW6lGKWrVbDuHsibRtOgv2NWUXLYOEXebtLer7xLpnM241MonXnVP4KewdAPBbAgmzTqXlA0F-tJiktjVT4d6L0bMHZISlpX4n-a1fAtjrhbalq2ieOTWWYaVKL21TzXIZyUvxZVIqTxcEMKK_mpgBxKsKWxCoLZvm7T8eJYuRb5JKn8VgjsYuq8WWLyVcdwqyHjsVa24pVJzEscUtsUSStzZtQ1ZG5ABW9sy9fSfmOQkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای دو تا ترنس تو پارک لاله تهران!
فقط آخرش
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71192" target="_blank">📅 17:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71191">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=OyW40qeJseGlmc8KGz8kuwUjtrK9sMZ-H1vX9CcRTt_RKVMozqhlhnokdRG2vI_7skmVDLpHlgYEfcjIm_CjjC-2supoEQxJfu5-ejAgqVoEWFoEW0TgZEANs7niMRDi--MGQNWdSbQJ27_BDLeAw7OIYpZnZjnv40IDilb4OtSGfB7dGufcZXPiNQV8kXw42_O5oOILDsxHaOAgUOxWIuVMXsw0XXBLxWXAE_I-4mBdvyWRZU299G9o30u3eIIUxLLTKzVlXVt-hnzeLrHt0IzZBkwP4x8jmqUB9vIGaxAK0Cop9RWnX9wOK0Ta5YHRma2SKc1DLt5UUfQcA1glDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=OyW40qeJseGlmc8KGz8kuwUjtrK9sMZ-H1vX9CcRTt_RKVMozqhlhnokdRG2vI_7skmVDLpHlgYEfcjIm_CjjC-2supoEQxJfu5-ejAgqVoEWFoEW0TgZEANs7niMRDi--MGQNWdSbQJ27_BDLeAw7OIYpZnZjnv40IDilb4OtSGfB7dGufcZXPiNQV8kXw42_O5oOILDsxHaOAgUOxWIuVMXsw0XXBLxWXAE_I-4mBdvyWRZU299G9o30u3eIIUxLLTKzVlXVt-hnzeLrHt0IzZBkwP4x8jmqUB9vIGaxAK0Cop9RWnX9wOK0Ta5YHRma2SKc1DLt5UUfQcA1glDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71191" target="_blank">📅 17:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71190">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45226525f2.mp4?token=VbyOKZkCccXj8XbZfctwryXesKEecflc07isw7ggjd01BBmCw_rDL7STwu8Da1Bhip6xkDvDgxnp3mgqO3apNZeF9VVtNvARv0HcpndBJJsMWuDXAkwExQwoZN3n2j_wLljSDv30xXNecsqGq8X0_vU_QaWU32InynRH1uqbSOXCsVu4_Gay3AUMhK6B1nKlcjaubobLCZgmji6xqv3zKSeePoq8kc_hwU2D2B_0nIJM9r_GGB_HAaPP5XrYrtcZkwEotQvGbZ2ObrOh6AGuJJbjWU0CafNw-iB-1A3zbYcuGFZTZtflQstUgpZz0RoLqCdQ0k1Ih_EKugRlGETHsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45226525f2.mp4?token=VbyOKZkCccXj8XbZfctwryXesKEecflc07isw7ggjd01BBmCw_rDL7STwu8Da1Bhip6xkDvDgxnp3mgqO3apNZeF9VVtNvARv0HcpndBJJsMWuDXAkwExQwoZN3n2j_wLljSDv30xXNecsqGq8X0_vU_QaWU32InynRH1uqbSOXCsVu4_Gay3AUMhK6B1nKlcjaubobLCZgmji6xqv3zKSeePoq8kc_hwU2D2B_0nIJM9r_GGB_HAaPP5XrYrtcZkwEotQvGbZ2ObrOh6AGuJJbjWU0CafNw-iB-1A3zbYcuGFZTZtflQstUgpZz0RoLqCdQ0k1Ih_EKugRlGETHsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
راننده ای که چند شب پیش در مشهد طرفداران حکومت رو زیر گرفت:
عمدی نبود تعادل نداشتم به یکی برخورد کردم تشنج کردم جای ترمز گاز دادم و یهویی زیر گرفتم
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71190" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71189">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71189" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71189" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71188">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPpaHh-lGkKx_zEWCUxr_Ieyl5hdSICpZbmw0Ok5VGSClkGo5FZVfnV5wOWLot09gkn1cX2jkN2lgZcW7w59nx89DyYawunnrTvhx17mw1mHNQQRmj134Ngg2itG_TI6vqMfM6fwrz6PWFWWfn2tWyDv8NY2KDtATuPvqrwqTg-6ARccp32U7-XXcaWnkj-KhRI-06i1P7HA4_Tgz0Ec_FdoSkdnscOIUSOiiDBokSA-3Ogh0ueIy3pIP3zFeESKvZgwVzO8Gc9pYXcLZJylzUxCWkyCT3QZgvXR7Z0hlVW2R3dYmAEnPjC6kqDMTeIo2oJupQ0V0flzjuzSle-ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
چلسی
🆚
آرسنال
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم:
چلسی: ۲ بازی ۲ برد و ۷ گل زده
آرسنال: ۲ بازی ۲ برد و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71188" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71187">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU27KpZqhBXcA3sYj5wOJR7M2d39C5vA-lQfPmUc3zOiTuOC9huC9uLx5Pujnb68aTMiuyCDkMBbWbgigtm6j9KQ0S592UiY8gkf1M_3V8JQLGn21to4rSfTNneUovGz_8vs4D7hJgEFevAikO4aDDCVp0pBqSoX_g9YecqxRXhZOmeah4nYvpP1bQKbtyUax2jLRDdW9KapSTMGYS15PUhyGZjZUF_q4fiYUTIw1yHKwWzGUCeQWGCYfiEtWP60HbDDzLnVemxGjnTnN62PfQBkxQ_NT7sFhY9KBJdC9uEpG4uloCTlpMnIe7Azo2hJ71wWhKjhZiHG95PzkAcMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇰
🇵🇰
پارلمان پاکستان برای نخستین بار در تاریخ این کشور، فرماندهی قانونی هر سه شاخه نیروهای مسلح — شامل نیروی زمینی، نیروی دریایی و نیروی هوایی — را به «عاصم منیر»، فرمانده ارتش، واگذار کرده است.
او می‌تواند بدون نیاز به تصویب کابینه، کارکنان این نیروها را بازنشسته یا اخراج کند و یا در خدمت نگه دارد.
دوره پنج‌ساله مسئولیت او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت.
او با دریافت درجه «فیلد مارشال»، این درجه و مصونیت قانونی را مادام‌العمر حفظ خواهد کرد و برکناری‌اش مستلزم کسب رأی دو‌سوم نمایندگان پارلمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71187" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71186">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22246726de.mp4?token=pl96_1ClUtH0GVZDLdPNKbUfEhYFqhy1d5toMKMxlEhqMXZtibzMloN12qAgwp61tZyWjmbyTpH5ibzUOiTJkXSPqkHf25BZCU38izfmTGKFqHqNOMoI6gcF_K7FzQDD27f3QTdqrqcjT21rxnom0YXRhCI3REvG74HZbxwC4uf1G-Yj2LEvm366FwzGwRBjX0pImQlb34JNLHZdwAQvwrc1_IAQTl3-OU2xqgfdYKsVT3nld4PyIt9SVOEhk8dlnD3ppJQgBSmnyp0wUAHvUfMVmgUNNdADJMvLhy9lkoRyeWCNo-w-WAocyAVRxkj6-FkgHUq538RnQt8U2R1rBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22246726de.mp4?token=pl96_1ClUtH0GVZDLdPNKbUfEhYFqhy1d5toMKMxlEhqMXZtibzMloN12qAgwp61tZyWjmbyTpH5ibzUOiTJkXSPqkHf25BZCU38izfmTGKFqHqNOMoI6gcF_K7FzQDD27f3QTdqrqcjT21rxnom0YXRhCI3REvG74HZbxwC4uf1G-Yj2LEvm366FwzGwRBjX0pImQlb34JNLHZdwAQvwrc1_IAQTl3-OU2xqgfdYKsVT3nld4PyIt9SVOEhk8dlnD3ppJQgBSmnyp0wUAHvUfMVmgUNNdADJMvLhy9lkoRyeWCNo-w-WAocyAVRxkj6-FkgHUq538RnQt8U2R1rBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از ی دختر ایرانی که با یه پسر مکزیکی با هم وارد رابطه میشن و بعد از ۴ سال بالاخره به هم میرسن و باهم ازدواج میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71186" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71185">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWt1__7W_WkU62DTYn28DTMFhp6qCrU4_HG_aS4YpI87FriX7_VQq3UAF4OtjsngdbuRcIYusvsSViPuQ-wPSjC43KBCbel2pqyyzUFpp61lruQ2MX1vlfikpONkvvF2K4rVI10ApXnXwcdZgrrUlthNCZCxD9sAW6WP790uDXcErUi-Djco6hDlywkMeuRk2WltyBqSawdc-sVGlDrerl2FHrVRyXqQ6JqBv21Q5p_PgnWBYGJsmxrZHj0Cbdj0mBauusxJxVULVIRTUoqD_Azh_I202Wrd4GkLhy-15dsVRbrJa1vo-NKHgmKW0WnvfnhiXQ7IfvNxuyxzRqisSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیده شده در تجمعات شبانه:
قالیباف
:
علی الاصول یادت رفت
علی الطاهر هوا رفت
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71185" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71184">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=tPG1rWT3OEY1Zq_kN7pIjt7FNY4w98i0Ih0UQPCDUhw7q1OrxUq3NyUjxyJPFAvCbvFKtMIal8TSfaFb_2vKGXHqM4tyzsAkOe8O4FEeUBIKaPGKfvOsMcdzuINyhcVOW_EvxpuiI71v7846ETuoc65vOQp27XOqz67iJ2x17qbHgDbAGxA7PJZ0HT3wHr4xlLFzFAlJC4nVgkcQaybiWjD80PqECxzm5OnJmpLejHC63R_lRVO-sE9NxFfjYrJ6HSni9YfUtXyc8EuFYOYmafaoLTlswf2l0i3k5cUgB4HJuRIjaiiNMYG0dnqGPdwWfdIUqqaXnh8qWjDV8Ex4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=tPG1rWT3OEY1Zq_kN7pIjt7FNY4w98i0Ih0UQPCDUhw7q1OrxUq3NyUjxyJPFAvCbvFKtMIal8TSfaFb_2vKGXHqM4tyzsAkOe8O4FEeUBIKaPGKfvOsMcdzuINyhcVOW_EvxpuiI71v7846ETuoc65vOQp27XOqz67iJ2x17qbHgDbAGxA7PJZ0HT3wHr4xlLFzFAlJC4nVgkcQaybiWjD80PqECxzm5OnJmpLejHC63R_lRVO-sE9NxFfjYrJ6HSni9YfUtXyc8EuFYOYmafaoLTlswf2l0i3k5cUgB4HJuRIjaiiNMYG0dnqGPdwWfdIUqqaXnh8qWjDV8Ex4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو درباره یکی از جنبه‌های سختی مرد بودن در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71184" target="_blank">📅 15:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71183">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=HGAUK3LKt60jgRqwW199bt0bN4n8GiGqAX0XBCbn1rzpSY-XhZRfHhXyzGhwScgJYcuaz9vVvbd3KPjONMtsx2yUvKENaFq9WunoVih7JkpmtLFGMk9zhCg5R_plIWKXL2sPTqxxNiqbwTdaXr_xsp5LMRarf1T4Yu60peTR6uxebTUsGPygn7qJOm0vfKIC-2fnh5kJvX27TA3OyYnLey4E2u0WlkY3Hw_S2xsd_nGs8R5J4iRLk67jq6FRaeYFW93lkpkdaEEDx-pEQCTNyXhmHBuIbt030MiMdJpKn12OUnRe9b_R-4kzZdJo-iSH1Z9AG4Z4-SXpj8T9N9z1PIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=HGAUK3LKt60jgRqwW199bt0bN4n8GiGqAX0XBCbn1rzpSY-XhZRfHhXyzGhwScgJYcuaz9vVvbd3KPjONMtsx2yUvKENaFq9WunoVih7JkpmtLFGMk9zhCg5R_plIWKXL2sPTqxxNiqbwTdaXr_xsp5LMRarf1T4Yu60peTR6uxebTUsGPygn7qJOm0vfKIC-2fnh5kJvX27TA3OyYnLey4E2u0WlkY3Hw_S2xsd_nGs8R5J4iRLk67jq6FRaeYFW93lkpkdaEEDx-pEQCTNyXhmHBuIbt030MiMdJpKn12OUnRe9b_R-4kzZdJo-iSH1Z9AG4Z4-SXpj8T9N9z1PIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مراد ویسی درباره مسعود پزشکیان:
حساب اینو نکنید این متخصص قلبه. از نظر سواد اجتماعی یه آدم به شدت پرتیه پزشکیان.
گفته کارمند‌های دولتو داریم صحبت می‌کنیم در سراسر شهرها، نیان تو شهرها. مثلاً اگر کارمند بانک‌اند اولین بانکی که اونجا هستن برن تو بانک بشینن کار کنن. اگر کارمند تامین اجتماعی‌اند اولین شعبه تامین اجتماعی که هست برن اونجا کار کنن
😟
گفته دو میلیون خودرو میاد کارمند ما اگر یه میلیون از این کارمندها رو بگیم روزانه نیان سر کار تعطیل کنیم اداره رو یا بگیم اولین اداره‌ای که می‌بینن برن اونجا بشینن کار کنن.
گفته یه میلیون خودرو هرکدوم روزی بیست لیتر مصرف می‌کنن یه میلیون ضربدر بیست لیتر می‌شه بیست میلیون لیتر مسئله بنزین حل می‌شه
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71183" target="_blank">📅 14:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71181">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=A85KxOo6R-xC4QJZJxkWQgIMBtFpCy7Bhd9VdBLlaERcBcDCzUpwIdO05_K20LxJmR42Po9juNKMkS4A6EYf5wu_AbnhLLXCq7wUgiPopi4rfnINl6QMQtRJvu3Xocimiq-NJhnBxOKVgBMP4x74aUM37r0C9bA8Za1gjOFVU9sOXg9U8kxwZE2t14UzhhaPkJudzTnXrKzdl-FBx4IlOgKhBUA8XAoZnPBKeqE2Jl4oKpUwGFrEj4-Xoff-BiIbRcQw9NuvwQlDw0hClT9CvgPJbgcC11w3vUOJpk8CqdN-Lbp04AePM_4km-hnyGuyN5fXUjblgiovO67htug8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=A85KxOo6R-xC4QJZJxkWQgIMBtFpCy7Bhd9VdBLlaERcBcDCzUpwIdO05_K20LxJmR42Po9juNKMkS4A6EYf5wu_AbnhLLXCq7wUgiPopi4rfnINl6QMQtRJvu3Xocimiq-NJhnBxOKVgBMP4x74aUM37r0C9bA8Za1gjOFVU9sOXg9U8kxwZE2t14UzhhaPkJudzTnXrKzdl-FBx4IlOgKhBUA8XAoZnPBKeqE2Jl4oKpUwGFrEj4-Xoff-BiIbRcQw9NuvwQlDw0hClT9CvgPJbgcC11w3vUOJpk8CqdN-Lbp04AePM_4km-hnyGuyN5fXUjblgiovO67htug8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
〰️
ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» (CVN-72) اسکله C-0 در بندر «لائم چابانگ» واقع در استان چونبوری تایلند را ترک کرد و مسیر خود را در عرض اقیانوس آرام به سوی پایگاه اصلی‌اش در سن‌دیگو در پیش گرفت.
خروج این ناو در صبح روز ۶ سپتامبر، به توقفِ حدوداً چهارروزه‌ای که از ۲ سپتامبر آغاز شده بود پایان داد و مرحله بعدیِ مسیر بازگشت آن به ایالات متحده را رقم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71181" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71180">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003437fd92.mp4?token=ooCAVwne7Qd5Km6TmeSO7BF8cD0Kp3f_hNAvFmAXSi4pou-xPHkPK7k2sj2HzhX3iiXdNlsfRgvLWAyDc0-qPlDbz5Wy_9WIkzKhrvargjLjJWO2htjV4sjKn8LdMm6SSBeyOidEFjAvRdaNzLn4v4lhBF-_SHms966rV5SyijpQhDG4cvusqy3Dv2jszbUjvMNz_t_8HSS6evcUUPyOayKWe7un8_ESTQTNqeH27VgBlTLXfeAi3PEzDUHXZJ-RbHMRAvtjMz98W3ibcCKbG_Q2g2GyBJbDvIg0K1rrpFicFtWu1WsL4-8bKchr4rDBIXYy5AGkF8TyRXWX1ak24Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003437fd92.mp4?token=ooCAVwne7Qd5Km6TmeSO7BF8cD0Kp3f_hNAvFmAXSi4pou-xPHkPK7k2sj2HzhX3iiXdNlsfRgvLWAyDc0-qPlDbz5Wy_9WIkzKhrvargjLjJWO2htjV4sjKn8LdMm6SSBeyOidEFjAvRdaNzLn4v4lhBF-_SHms966rV5SyijpQhDG4cvusqy3Dv2jszbUjvMNz_t_8HSS6evcUUPyOayKWe7un8_ESTQTNqeH27VgBlTLXfeAi3PEzDUHXZJ-RbHMRAvtjMz98W3ibcCKbG_Q2g2GyBJbDvIg0K1rrpFicFtWu1WsL4-8bKchr4rDBIXYy5AGkF8TyRXWX1ak24Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی ایتا و روبیکا، ناو جرالد فورد رو بمبارون و غرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71180" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71179">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71179" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71178">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekpZnXO9BBpWJ-spqLoixB2JhPrs2I7Zxh-YD5egen6BPr2ssXo4EOUSLL_2nGbUSi9Ex9psSukD8uxlXHT_AUl5yAaTycZm1zMAFTAI7gwzist9JmPA5KqDYAB-2NiWQYk2_FeUwkjLyL3pvbvq9mC028qymnXIrwW3q853fSeCisj6zF3JYzyOIc5G4hs_OlN9QvKK6UXv2C5lgINw00MiiTC_8QytBbJPrTxmxuNOxjppaVPw4GRz84QsLcs_xpAQkxGtpivkTlj7ksHtbIbv6vMY3PEw_TFZAt2nLref7dXK4JlD-pZpqoJZag9BoMrQbKmyIyUzbD1uZl8T5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71178" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71177">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=sXyiLkwBqBmvsW6rJgjkC0gKLcz4k1TDprXoUEyTeh3O5TubNyU-11kmjoy4ITvTsLMwoBDlrfSRAZCezADYYSqjuYGrgRgAePdQJpfUvX8J8CXEHau2aMtrNKoWB4jIJAULfpRcpRhoJv9w4By50BBd_KEO3yTkwAa3AtLl9kMcdSC8AtPkUOoZOLiQvPNv9q2_ygwzbRyAZvRWs0s6SiupXsxi7fJG3TpTIvk4sEw25lAVfsFsD9-BkgyMBCtF7oDQu6hhKoOkM589VgnIeu7_Ty9nJIvdLbZ6pW8waqtB93gMbv_dXP40o3OmaWFwtQ-hDVofWB_pv5LWXQBy5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=sXyiLkwBqBmvsW6rJgjkC0gKLcz4k1TDprXoUEyTeh3O5TubNyU-11kmjoy4ITvTsLMwoBDlrfSRAZCezADYYSqjuYGrgRgAePdQJpfUvX8J8CXEHau2aMtrNKoWB4jIJAULfpRcpRhoJv9w4By50BBd_KEO3yTkwAa3AtLl9kMcdSC8AtPkUOoZOLiQvPNv9q2_ygwzbRyAZvRWs0s6SiupXsxi7fJG3TpTIvk4sEw25lAVfsFsD9-BkgyMBCtF7oDQu6hhKoOkM589VgnIeu7_Ty9nJIvdLbZ6pW8waqtB93gMbv_dXP40o3OmaWFwtQ-hDVofWB_pv5LWXQBy5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام ویدئو غرق شدن نفتکش ایرانی در دریای عمان را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71177" target="_blank">📅 13:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71176">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
آمریکایی‌ها باید دریافته باشند که دوران «پاسخ‌های متناسب» به سر آمده است.
حملات ما به پایگاه‌های متجاوزان تنها یک آغاز بود.
قواعد بازی تغییر کرده است.
از این پس، هرگونه تجاوز به منافع ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر در پی خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71176" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71175">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=eT6yE4cJ5VlK7nZ2EykSbgum-cplWZzQ_74IrD52rNAxVp2EYfOy9X-GcLh83k1rz0Eiktg7OAQ7PixXBL_SbjM7F0MfZnM_qZ1xqK_LluFDDhlMXnV6N0tlZrI2qwJh91KBG5y2JIHCJz7VxW8THI5zVTkts5NjYkHvYIMpbQ8Re5Fe5iNg4AKVpctKiFptxreOuv4VpzZUT5k-zPZx9FC2-qYEUT52cHNkckz7SPIUJE48Fo7i2Da4YRdAIXdazH2jXa-skbSxGAcm4wpp_VUGN2ykvhzX-fsu3ctPtoA-0FfM3jPxq4cYhULeHBPHkALjgVGda2e5FBJn7kvkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=eT6yE4cJ5VlK7nZ2EykSbgum-cplWZzQ_74IrD52rNAxVp2EYfOy9X-GcLh83k1rz0Eiktg7OAQ7PixXBL_SbjM7F0MfZnM_qZ1xqK_LluFDDhlMXnV6N0tlZrI2qwJh91KBG5y2JIHCJz7VxW8THI5zVTkts5NjYkHvYIMpbQ8Re5Fe5iNg4AKVpctKiFptxreOuv4VpzZUT5k-zPZx9FC2-qYEUT52cHNkckz7SPIUJE48Fo7i2Da4YRdAIXdazH2jXa-skbSxGAcm4wpp_VUGN2ykvhzX-fsu3ctPtoA-0FfM3jPxq4cYhULeHBPHkALjgVGda2e5FBJn7kvkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:بستن تنگه هرمز به ضرر ایران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71175" target="_blank">📅 12:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71174">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=D2stdFqt5EY9jjv2pdf6YSpCG5cQntnKkz894o1Q3A6wGyzRf1zsOVxDwvkGAAxo8mrpDxmJLOnE94Qe2-TQkdS-iq30IBAKsWWTQZk3JKbhH7p_YKzLTCR49gQaWSLFQfYcpFGRzx6t3KiMAr1NbzMuwGfftpCHBd26wv8GBD2wqc84jm_xwVmhmMkxYFZx6AJLnpMeq02EugVBT4bAV3KwX1tml79AQzPv6oYktGvbu6V4sgwEgslxacs1WQGj0FV6yOHnb9tm_B-RewIR4cYz-Qd7TkDiSXihmZk0jFdvoMd_w9yFNSPVDfmeshIazHDc779JsXTjT3mw5URJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=D2stdFqt5EY9jjv2pdf6YSpCG5cQntnKkz894o1Q3A6wGyzRf1zsOVxDwvkGAAxo8mrpDxmJLOnE94Qe2-TQkdS-iq30IBAKsWWTQZk3JKbhH7p_YKzLTCR49gQaWSLFQfYcpFGRzx6t3KiMAr1NbzMuwGfftpCHBd26wv8GBD2wqc84jm_xwVmhmMkxYFZx6AJLnpMeq02EugVBT4bAV3KwX1tml79AQzPv6oYktGvbu6V4sgwEgslxacs1WQGj0FV6yOHnb9tm_B-RewIR4cYz-Qd7TkDiSXihmZk0jFdvoMd_w9yFNSPVDfmeshIazHDc779JsXTjT3mw5URJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
ویدیویی که در توییتر فارسی به شدت در حال وایرال شدنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71174" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71173">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=RhTIA-A14TnlaCzcRSmSXrxY52Zfut7uVz7Q3cjDheU_G6x7EpOp2H23wk0bvyvtRiipmHnOp__NFd_HVBTjue7nkZRxc5Rvco1TPEp5Avgk1Mia9JcdQnsp6TGrPPXU0zOKRqyR3vfnB7TcWgp8ykv17NTkl5XFqfZYLkRDy6pYhpvvEca-zBLxeUtQz1oxgRI6sPlgy3QhXIyxM8Fw1M4wBHDqGF7-pQFLfBzF0tBdoolinPESbTRoM6nZY8gXIDaloNC_dVWoKxiVqxZwdt35VY2PkgoHe0zkUvJGjnlgTZ7TOOhdRf2VMoCb1SBumwys-swvPWHYA11iG9MA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=RhTIA-A14TnlaCzcRSmSXrxY52Zfut7uVz7Q3cjDheU_G6x7EpOp2H23wk0bvyvtRiipmHnOp__NFd_HVBTjue7nkZRxc5Rvco1TPEp5Avgk1Mia9JcdQnsp6TGrPPXU0zOKRqyR3vfnB7TcWgp8ykv17NTkl5XFqfZYLkRDy6pYhpvvEca-zBLxeUtQz1oxgRI6sPlgy3QhXIyxM8Fw1M4wBHDqGF7-pQFLfBzF0tBdoolinPESbTRoM6nZY8gXIDaloNC_dVWoKxiVqxZwdt35VY2PkgoHe0zkUvJGjnlgTZ7TOOhdRf2VMoCb1SBumwys-swvPWHYA11iG9MA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به گفته آقای دکتر اگه می‌خوای سرطان پروستات نگیری، باید ماهی ۲۱ بار سکس کنی...!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71173" target="_blank">📅 11:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71172">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b321711db4.mp4?token=lYL7NmekmMv3egqBvxMNmjNkXQueyHGnk-YhVMgCneT7DDeVWiC6CELP5BavZXXMepOWEwKlOGvkjyc8R_-yfnn_kXHTcWjZs942cP3B-DcU6h8-LPkTTOPS0CkrFhQMsMuAnEbHuuWaVETo9n6qPsTAdoudUWcmfafj4zllfYpBb7cUlQ0u-dOl0cNfy5Hq84lfb0dpLQd3iWJY_IsTdw2Cy9M42VQIm8LWjhuNip7YSIy73f5CD3fNWxHEw8MLF9So61ipXG9wiwP71EMEOeHCQ3MAGexloFOY82w5yTSnQCD6cNlU_3hwI7AxZW4QypnGOhMEjUW4hfRAr3__dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b321711db4.mp4?token=lYL7NmekmMv3egqBvxMNmjNkXQueyHGnk-YhVMgCneT7DDeVWiC6CELP5BavZXXMepOWEwKlOGvkjyc8R_-yfnn_kXHTcWjZs942cP3B-DcU6h8-LPkTTOPS0CkrFhQMsMuAnEbHuuWaVETo9n6qPsTAdoudUWcmfafj4zllfYpBb7cUlQ0u-dOl0cNfy5Hq84lfb0dpLQd3iWJY_IsTdw2Cy9M42VQIm8LWjhuNip7YSIy73f5CD3fNWxHEw8MLF9So61ipXG9wiwP71EMEOeHCQ3MAGexloFOY82w5yTSnQCD6cNlU_3hwI7AxZW4QypnGOhMEjUW4hfRAr3__dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇹🇷
این پسر بچه ارومیه ای که چند وقت پیش با ویدیوش که در حال آهنگ خوندن بود توی اینستاگرام به شدت وایرال شد حالا یه کمپانی بزرگ از ترکیه اومده و باهاش قرارداد همکاری بسته؛
فعلا این قرارداد واسه اجرای کنسرت های مختلف تو ترکیه‌ست
رئیس کمپانی میگه که این تازه اول راهه و قراره بزودی تو سراسر جهان کنسرت برگزار کنیم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71172" target="_blank">📅 10:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71171">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e529d142.mp4?token=W7XMBJaLaTZJEKZKAYD6LZNPNVYBbbZT80-19KM6_ZHN-Gsh6z7Ij7brd5JORFFr_vr8WNuZ3kvmgxs9T-yNeRjOXHavyxi0qPSTncsNCAHiiYNqIThNUyInAkPcStQSzXk7SVTbKg5Rl6G5lFa3xdKsQVxOxaR6Ru-ZqbJLDdgZz2kjryi7ECwdCKGgB6ke8DjDM_p4yFPLkl5BfwLYftvh5FNYGsOk5ho40ItbfjqdYXjqxTIBb_HQhrirUcQPo3m99kf-UV_qsBV7wvDX8EEaQFctR4EUX9vu_BN6D1eXwgI8XqSgAH3fpSIvR35_pE43qwtpeVQuXBX9jUuLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e529d142.mp4?token=W7XMBJaLaTZJEKZKAYD6LZNPNVYBbbZT80-19KM6_ZHN-Gsh6z7Ij7brd5JORFFr_vr8WNuZ3kvmgxs9T-yNeRjOXHavyxi0qPSTncsNCAHiiYNqIThNUyInAkPcStQSzXk7SVTbKg5Rl6G5lFa3xdKsQVxOxaR6Ru-ZqbJLDdgZz2kjryi7ECwdCKGgB6ke8DjDM_p4yFPLkl5BfwLYftvh5FNYGsOk5ho40ItbfjqdYXjqxTIBb_HQhrirUcQPo3m99kf-UV_qsBV7wvDX8EEaQFctR4EUX9vu_BN6D1eXwgI8XqSgAH3fpSIvR35_pE43qwtpeVQuXBX9jUuLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
خبرنگار جمهوری اسلامی در لبنان:
اعضای سپاه پاسداران در تپه‌های علی‌الطاهر، به دلیل محاصره اسرائیل، در شرایط عاشورایی قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71171" target="_blank">📅 10:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71170">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a662811c73.mp4?token=u_SEuAqj2bv_p1PnKNGtfhfTQEkViy0Qdzf-rX_HaMNEwdpfsH58c6bCkijab7ZNn8wFRLsu3-iIcx3Ji7S_R7PLyDkSpuJ4EfDN3qs1qF-QgmCQFiRmhK8mkzBawHyDfqpMqB-4tVMDZMtrI6keXGdz-yrJhAnNbL8p7WUyANBCpwXAKAJb9Qx9_vIh9OCCWoSjBjrxQdXFpsdIZESKaimJCbV0xT8maSgdmwltaNT3gEtLWxHpGuugIjBWjR21YNe4JoO1MoOVzmbnh1jP-yLcvhqQQ1cBA0ckd9CQz1IUo9MZAgTYsYbVjvb8jPEGNdfmtfkDD7uAWLLAG2lBWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a662811c73.mp4?token=u_SEuAqj2bv_p1PnKNGtfhfTQEkViy0Qdzf-rX_HaMNEwdpfsH58c6bCkijab7ZNn8wFRLsu3-iIcx3Ji7S_R7PLyDkSpuJ4EfDN3qs1qF-QgmCQFiRmhK8mkzBawHyDfqpMqB-4tVMDZMtrI6keXGdz-yrJhAnNbL8p7WUyANBCpwXAKAJb9Qx9_vIh9OCCWoSjBjrxQdXFpsdIZESKaimJCbV0xT8maSgdmwltaNT3gEtLWxHpGuugIjBWjR21YNe4JoO1MoOVzmbnh1jP-yLcvhqQQ1cBA0ckd9CQz1IUo9MZAgTYsYbVjvb8jPEGNdfmtfkDD7uAWLLAG2lBWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شاهین نجفی:
هرکسی رضا پهلوی رو مورد انتقادهای عجیب غریب قرار میده و میزنتش یه سرش وصل میشه به جمهوری اسلامی
اینا جوگیر شدن چهارتا شعار دادن و حرف زدن بعد دیدن اینجا خبری از سهم دهی به کسی نیست مسیرشون رو عوض کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71170" target="_blank">📅 09:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71169">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=fxVr0Hbvj-8kV7NBzmnnNc3TnFi0-bM91kVbMf6UX3GfxSMg53zRTV9OBW4EUcSOSq_QQ4UBXuPeYUzY9Uip8kDiJaT6glMCSREcg8PGTQfWFSeyDqEQYD_Vb5iWsoeS9RI-UHwrW9uj5KVKQJmtI4b92VT_yky4KkYPjRzZxHes7uQ_bLZj8jBsuDAPRJwmlh7WB9JPI-u_NYYksOpZiAYRIZoI3mdcnoRVF58DMWDybqqFd94OFTh8flDSfA78Zg-vBwn_7Koa-543kmSb_dY2syiRmH4lknQTQiTwUGCGIYv_wMnM3ZUG4ICcCYmr_dr6D2sbYXWz52wmVFBRTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=fxVr0Hbvj-8kV7NBzmnnNc3TnFi0-bM91kVbMf6UX3GfxSMg53zRTV9OBW4EUcSOSq_QQ4UBXuPeYUzY9Uip8kDiJaT6glMCSREcg8PGTQfWFSeyDqEQYD_Vb5iWsoeS9RI-UHwrW9uj5KVKQJmtI4b92VT_yky4KkYPjRzZxHes7uQ_bLZj8jBsuDAPRJwmlh7WB9JPI-u_NYYksOpZiAYRIZoI3mdcnoRVF58DMWDybqqFd94OFTh8flDSfA78Zg-vBwn_7Koa-543kmSb_dY2syiRmH4lknQTQiTwUGCGIYv_wMnM3ZUG4ICcCYmr_dr6D2sbYXWz52wmVFBRTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما آمار رسمی کشته شدگان اسرائیل تو سه روز اول جنگ رو منتشر کرد:
۶عدد ژنرال ارشد اسرائیلی
۳۲ نفر مامور موساد و ۷۸ نفر مامور شین بت
یازده دانشمند هسته‌ای
۱۹۸ نفر افسر نیروی هوایی
۴۶۲ سرباز و ۴۲۳ نیروی ذخیره ارتش اسرائیل کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71169" target="_blank">📅 09:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71168">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
سپاه پاسداران انقلاب اسلامی ساعاتی قبل در بیانیه ای مدعی حمله به یک ناو هواپیمابر و یک ناوشکن آمریکایی شد و اعلام کرد که پس از این حمله اونا خسارت دیدن، ترسیدن و از منطقه فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71168" target="_blank">📅 08:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71167">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71167" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71167" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71166">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McAvCe5vp92xSPV0Q7c5PfCL94ITqzN1Wjp5XPFoUvGvjNUZIKlTWYOA_eF4P3K0cGp6UAIP3fEXYMObxx2a6jVHM1umQ45ZtSnu411JhC3-qIK0UeyplVxXBHy_yJJCUb2PHncVNhOibkjYiy_JNzA36r7c4y16sCi81nhJbEQtIaT6jMMonQzybt-IIoyTQd8hmeolZUHaXK5rUTKM5O0_0ljRBk7cw89cwsu9c65QrGmrqdASPvzq1PDyv6-pk4cV3Esh4eCRUf_bh-dEWsTc6Em9d2qNaFawUU3P4ciYHvinF84lVGu7-CJV5FChJl14hc6T03tuZGfkAlTFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
تنیس US Open داغ‌تر از همیشه دنبال میشه!
🦖
مسابقات جذاب
US Open
رو در
TrexBet
پیش‌بینی کنید، هیجان رقابت‌ها رو بیشتر کنید و برای جوایز جذاب وارد رقابت بشید!
🦖
فرصت هیجان
US Open
رو از دست ندید!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71166" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71165">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/news_hut/71165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71165" target="_blank">📅 01:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71163">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=mkBJlPM0qCOWSbc-b5BKGWZMXhYn7BUimgeJTpT0XT194YSVnOTaXuhvDONBDiPMQU3vJ9a4EgfgaaZCOHdA4SSEmgTAgGaUlq26R9hE1z4XVx42bYeVmVim1F7WrFrh9zt-1sVRd8xt8qoexVzvvccgUtYYvhwYmPjptVBtnLFB8gGnfmsRCSsu5EzzaDtracJtUKqZ-g-5srBWs_KacENmaP3UxEmDxWDDe-g6PsV_VPpNIZuRU0wXC5p59pVnI3ias-UuvcK-IisIM1itUzvVqy0pJJA367O0SMt4GDzDrhPvf__AZGKROHTeeL6TKcDq2vWw-_w4ujuNRrXq_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=mkBJlPM0qCOWSbc-b5BKGWZMXhYn7BUimgeJTpT0XT194YSVnOTaXuhvDONBDiPMQU3vJ9a4EgfgaaZCOHdA4SSEmgTAgGaUlq26R9hE1z4XVx42bYeVmVim1F7WrFrh9zt-1sVRd8xt8qoexVzvvccgUtYYvhwYmPjptVBtnLFB8gGnfmsRCSsu5EzzaDtracJtUKqZ-g-5srBWs_KacENmaP3UxEmDxWDDe-g6PsV_VPpNIZuRU0wXC5p59pVnI3ias-UuvcK-IisIM1itUzvVqy0pJJA367O0SMt4GDzDrhPvf__AZGKROHTeeL6TKcDq2vWw-_w4ujuNRrXq_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سپاه پاسداران تصاویری از «رصد و رهگیری شناورهای متخلف» در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71163" target="_blank">📅 00:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71162">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=uzDQmsYqcoSXzE-jqGoYEEuF_RMoIgxQked9VDCvOSsV-6fteA3UYX17VZuoir__gGz09BbeXS5YqIAQK9Dv1HM_q5U0qpMKFZ7QQv8a8sR2MJgH1dpkLpbLqpmQrHX0sr3n5XkJIcZ6TsujZjoj4Y96PUnqZrBZ8fZshodgEyxxotPlgMudwH0aozPlBdhmc4Gp7GcKjQskFXXCPCSmKVIQPoZGg-Jn4qTbP-txk2D0j0KelnRy1XVjKS6U8_AvSeXfCpzoIaFghIOdJqsGlq_YtuvgvRQJxInnjwGtk2vQAPgOjUIXXMCV0u6HHRskGZw0JNejVn5YQvY8VNbqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=uzDQmsYqcoSXzE-jqGoYEEuF_RMoIgxQked9VDCvOSsV-6fteA3UYX17VZuoir__gGz09BbeXS5YqIAQK9Dv1HM_q5U0qpMKFZ7QQv8a8sR2MJgH1dpkLpbLqpmQrHX0sr3n5XkJIcZ6TsujZjoj4Y96PUnqZrBZ8fZshodgEyxxotPlgMudwH0aozPlBdhmc4Gp7GcKjQskFXXCPCSmKVIQPoZGg-Jn4qTbP-txk2D0j0KelnRy1XVjKS6U8_AvSeXfCpzoIaFghIOdJqsGlq_YtuvgvRQJxInnjwGtk2vQAPgOjUIXXMCV0u6HHRskGZw0JNejVn5YQvY8VNbqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
یک فروند جنگنده F-4 فانتوم نیروی هوایی یونان در جریان رویداد «هفته پرواز آتن» در پایگاه هوایی تاناگرا سقوط کرد و دو خلبان این جنگنده کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71162" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71161">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=rzySHiLVFOzhBOVotvagucwYDyJJEF_fVyYDLM9DFW-pxGoUapf69JOWF4vqRXLOVYksp9HZWimOyB7zdqBrcbi1v4Y31iUOIuR642a3qxG2r5tDtAWhJSudqBMBPPKUEW-Zh3RCLTJnrjjMkmXy-Tm0FOo19anqfLnYvEMYLUYkTa7aSJ4v7tBYGg9pQTJWo__ncpa2QSxgGDc7DwC5LFf8DRr9G5hdiN-0uyE24l0WdFeFTEf0XWatI8UNulzMw3YXmZVySIh4XiTHQi2MmBx47aQL3e15wfgE2KgIqLatPdX6zEYuj0zTvkAN7UzHy6EPIhWTO4-ZGS2skcClOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=rzySHiLVFOzhBOVotvagucwYDyJJEF_fVyYDLM9DFW-pxGoUapf69JOWF4vqRXLOVYksp9HZWimOyB7zdqBrcbi1v4Y31iUOIuR642a3qxG2r5tDtAWhJSudqBMBPPKUEW-Zh3RCLTJnrjjMkmXy-Tm0FOo19anqfLnYvEMYLUYkTa7aSJ4v7tBYGg9pQTJWo__ncpa2QSxgGDc7DwC5LFf8DRr9G5hdiN-0uyE24l0WdFeFTEf0XWatI8UNulzMw3YXmZVySIh4XiTHQi2MmBx47aQL3e15wfgE2KgIqLatPdX6zEYuj0zTvkAN7UzHy6EPIhWTO4-ZGS2skcClOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه خانم درباره اقتصاد:
چرا مردم هر چی گرون میشه از زاویه ی آدمای متوسط بهش نگاه می‌کنن؟
خونه از ۵ میلیارد شده ۵۰ میلیارد.
گوشت از ۵۰۰ تومن شده ۴ میلیون.
سود شما چند برابر شده.
مردم از گرونیا دارن سود میکنن، مردم باید دیدگاهشون از آدمای متوسط جامعه تغییر بدن و بگن هر چی گرون میشه خب ما هم سودمونو داریم میبریم
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71161" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71160">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=hZICHMrk03UVV1DT1E4-6N0MXC1v8LS1WxWiGm9buyZghFu22yDpiK-VWBuMLlBsqIfsAVOQGH_bUsfHUSS_MGouWV4bR0GlCi-etDKp8jzOzSdWaYDgROwL1R0ojssJJvu04tZjWxLl-NORhZNIEddV0Vbhk7Ae4nHLPt96rKrLo61XC0Ln1-D_r82mwEEc5Boj_YQfouiWTGpUeus7Em2cn4UJqmcU2ii9KS5KS7WCj8JQvg8M_Vw7dKZYacsHXhA2_p9jkJ3Zoc-XfUHbAklrcUHk6qpoZtyH_u1QFxUjym2MxnnBQWIDdsmIMXspGoQJ0Ddazpy9xa-MhD74AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=hZICHMrk03UVV1DT1E4-6N0MXC1v8LS1WxWiGm9buyZghFu22yDpiK-VWBuMLlBsqIfsAVOQGH_bUsfHUSS_MGouWV4bR0GlCi-etDKp8jzOzSdWaYDgROwL1R0ojssJJvu04tZjWxLl-NORhZNIEddV0Vbhk7Ae4nHLPt96rKrLo61XC0Ln1-D_r82mwEEc5Boj_YQfouiWTGpUeus7Em2cn4UJqmcU2ii9KS5KS7WCj8JQvg8M_Vw7dKZYacsHXhA2_p9jkJ3Zoc-XfUHbAklrcUHk6qpoZtyH_u1QFxUjym2MxnnBQWIDdsmIMXspGoQJ0Ddazpy9xa-MhD74AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جانفدای رندوم و حرکات جالبش
😃
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71160" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71159">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=QHIkNvOAfZpomKAawnYWhcv1l_PlNLhPQvEEEYMCLTVAFZ07yC62aZHlLeJ7Ojj3Ztk8LtVUXscsOa1AKwVfn4pRYMDYpUeg5UNinctzx0JBb-C42fksak6UHwyGn7oOb3ke77R2ypKpQn0uX3_4WIuYz5k7Kzh5A4-ZhdANDUov0uMJnnROFxZAHCqN6gbBclVQWJnXIz0oS-dZM07IeRR1S-MPbIfaroQHPaWwh773txBttARFLU-LC_mUTU3tVgISr3snY_ekJOd67Mz8wv9FxUfqpdUfIpj47zbFHlQ1cOoRsA2OdHhfvlyt9n3DKGjeuvqykuL-ElJazrcpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=QHIkNvOAfZpomKAawnYWhcv1l_PlNLhPQvEEEYMCLTVAFZ07yC62aZHlLeJ7Ojj3Ztk8LtVUXscsOa1AKwVfn4pRYMDYpUeg5UNinctzx0JBb-C42fksak6UHwyGn7oOb3ke77R2ypKpQn0uX3_4WIuYz5k7Kzh5A4-ZhdANDUov0uMJnnROFxZAHCqN6gbBclVQWJnXIz0oS-dZM07IeRR1S-MPbIfaroQHPaWwh773txBttARFLU-LC_mUTU3tVgISr3snY_ekJOd67Mz8wv9FxUfqpdUfIpj47zbFHlQ1cOoRsA2OdHhfvlyt9n3DKGjeuvqykuL-ElJazrcpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7  جونشون رو از دست دادن...
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71159" target="_blank">📅 22:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71158">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=m5YqA6g14CrPObNJUXWwrnS9mU1CxfvTb_V9StTcVHO4RPnPCByCXsZI8_Wm1OkQaiTR29a8tA8jo8XlRI-XlQ36gz3MefOwG3X7HmiMdv6aO2HUTPqNhofOwbz4kxIcXUfJj29hAm1uba93Bu3OqmySQmvLkhkFvD6afWK3jSHZxiUZrShYg8G0stwcn13Mutsqk9E_MVNOS9hIu33JWMvuDyx7jnn6vD5Id6Ie0x0IrU3tWMvUjSW6P6qJeZpWsyjMJaMlcTKCv0leOfLaUXInRC00OlL8xDcJd-yJV71QY_XgXyxZ0AXcxP3axIQIvZNVIMHfsxiIU5r-vfmc_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=m5YqA6g14CrPObNJUXWwrnS9mU1CxfvTb_V9StTcVHO4RPnPCByCXsZI8_Wm1OkQaiTR29a8tA8jo8XlRI-XlQ36gz3MefOwG3X7HmiMdv6aO2HUTPqNhofOwbz4kxIcXUfJj29hAm1uba93Bu3OqmySQmvLkhkFvD6afWK3jSHZxiUZrShYg8G0stwcn13Mutsqk9E_MVNOS9hIu33JWMvuDyx7jnn6vD5Id6Ie0x0IrU3tWMvUjSW6P6qJeZpWsyjMJaMlcTKCv0leOfLaUXInRC00OlL8xDcJd-yJV71QY_XgXyxZ0AXcxP3axIQIvZNVIMHfsxiIU5r-vfmc_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر نیرو:
دیگر قطعی برق برنامه‌ریزی‌شده نداریم
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71158" target="_blank">📅 21:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71157">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=RqrS1-dl23k_7JQoCvHUpjEcjC0_FDxNZn-MHyMhAvhyJFws2LBAaFP76rFlezy6fFld6ofX_0oB5siB5nOFFzIq71HtyMjvRVIUrk0wbr-Nu4fWZd3beg7EmqQCdXhKaskYI25emaAa8ScfoP-ddUPu8IRxF_Io9zXsQO6y0p71oYboAlWM6YYAIMtgSf-5nlOEL43MnAhw_OmLsWO2kbsqSkj4TdznO-dTuHXsU7hWz_q8yTy9X2Y8Y6oxAo5WUtdxkRp2oSbxbs4HmziWwJzC0KlskTdcJsgJpQ0Jp8GSJLAy5endyGmI5d54uOhHrcFKNI-fVVMLSJL2s12D-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=RqrS1-dl23k_7JQoCvHUpjEcjC0_FDxNZn-MHyMhAvhyJFws2LBAaFP76rFlezy6fFld6ofX_0oB5siB5nOFFzIq71HtyMjvRVIUrk0wbr-Nu4fWZd3beg7EmqQCdXhKaskYI25emaAa8ScfoP-ddUPu8IRxF_Io9zXsQO6y0p71oYboAlWM6YYAIMtgSf-5nlOEL43MnAhw_OmLsWO2kbsqSkj4TdznO-dTuHXsU7hWz_q8yTy9X2Y8Y6oxAo5WUtdxkRp2oSbxbs4HmziWwJzC0KlskTdcJsgJpQ0Jp8GSJLAy5endyGmI5d54uOhHrcFKNI-fVVMLSJL2s12D-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
جان بولتون دیپلمات آمریکایی درباره ایران:
من معتقدم — و دهه‌هاست که چنین نظری دارم — که تنها راه دستیابی به صلح و امنیت واقعی و پایدار در خاورمیانه، خلاص شدن از شر رژیم تهران است.
به گمانم حملات آمریکا و اسرائیل آسیب قابل‌توجهی به این رژیم وارد کرد.
بی‌شک ما اشتباهات زیادی مرتکب شدیم.
اما اگر اراده کنیم که درباره چگونگی انجام آن به‌درستی بیندیشیم، این هدف همچنان قابل‌تحقق است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71157" target="_blank">📅 21:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71156">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
صداوسیما:
صدای انفجار هایی که در جزیره قشم شنیده شده مربوط به شلیک موشک ها به سمت شناور های متخلف در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71156" target="_blank">📅 21:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71155">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=s7toTg_DsWHTG-_0-muFN1eH0cm58aYZ_A2KX-cBhBVZFyty3kNpvgb9fGW_B9ufIfdgeqAyQQCabR3dD8ZQPPOfWkpfVaHIZnYx_bIc7hWtatvEqHgQjXLOxoWgiAWsX7dcHU6wLDWttN2_sFnfK40SxKF8qIIoGv2SbKdgB0n4yvtsOLzAhMvDQgidtcBaa3dJ7FlTxwDwGOGS3Tv9Da_H49dNrRhzF5_VMNJ_w4VIsFMTog6Ae72eTa6hKyUbBPB9Nc6UQgEbgPHwISPD7FqnYgTjkS7ywygs-4vUP7zoOPO8masnrziJ8B9vfzTvDQswO2WUG-Gsb_Q3jortsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=s7toTg_DsWHTG-_0-muFN1eH0cm58aYZ_A2KX-cBhBVZFyty3kNpvgb9fGW_B9ufIfdgeqAyQQCabR3dD8ZQPPOfWkpfVaHIZnYx_bIc7hWtatvEqHgQjXLOxoWgiAWsX7dcHU6wLDWttN2_sFnfK40SxKF8qIIoGv2SbKdgB0n4yvtsOLzAhMvDQgidtcBaa3dJ7FlTxwDwGOGS3Tv9Da_H49dNrRhzF5_VMNJ_w4VIsFMTog6Ae72eTa6hKyUbBPB9Nc6UQgEbgPHwISPD7FqnYgTjkS7ywygs-4vUP7zoOPO8masnrziJ8B9vfzTvDQswO2WUG-Gsb_Q3jortsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تصاویر منتشرشده نشان می‌دهد یک کشتی کانتینربر در اسکله بوشهر تقریبا به‌طور کامل نابود شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71155" target="_blank">📅 20:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71154">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
گزارش‌ هایی مبنی بر وقوع حوادث برای چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71154" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71153">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=klLms4N-i6NXyhVT3T0oxPE26jMJBhL330MYH6uIinkzEeKYEc5N7_dJqhGGcIBGhQtMdHmlKs2FcuPv8HRIRb0KFAjtRxMimYxZFeSKjLtFYXyJpaTMKHvGcF7VYXW0iMk5yADvsfyORBfg9oQi3RVHENxdrFx7yVqLy0ws44w9doB76xyVQqOSrv2gGMJ-e6s0aVLIEabuv2l4nx0IVxQorXxh3U1zHT18o0m0U7MxB2vDA3UH0v8ysrwcW5QeD_bRyGpp4v-MocYri_DlfPD020ANoSlXvHICIg-6GpgDkJ7gbeEtUMJjSikoRhR2LAAMhfsyCTQoZS1VgUb6rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=klLms4N-i6NXyhVT3T0oxPE26jMJBhL330MYH6uIinkzEeKYEc5N7_dJqhGGcIBGhQtMdHmlKs2FcuPv8HRIRb0KFAjtRxMimYxZFeSKjLtFYXyJpaTMKHvGcF7VYXW0iMk5yADvsfyORBfg9oQi3RVHENxdrFx7yVqLy0ws44w9doB76xyVQqOSrv2gGMJ-e6s0aVLIEabuv2l4nx0IVxQorXxh3U1zHT18o0m0U7MxB2vDA3UH0v8ysrwcW5QeD_bRyGpp4v-MocYri_DlfPD020ANoSlXvHICIg-6GpgDkJ7gbeEtUMJjSikoRhR2LAAMhfsyCTQoZS1VgUb6rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
✈️
ویدیویی تایید نشده از پرواز تانکر سوخت‌رسان آمریکایی به همراه دو جنگنده در آسمان جزیره کیش استان هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71153" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71152">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71152" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71151">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6tf94m1ybLtlKkL7pFcq35Tri-a8WpkDDepVswZms32Yl9IeYa9cHDmh_gGZSSV9bLT1SI0huZybW8HI0t6qePc1AlwMqds0eJ3c4KX3Z0u_Qrr8GZXaaLhBVrVNwZmXgxLibwn1wwY-nTkB6AgwVPQ266y9NlWa-chLz8f2xuJ9GxsNaQiKYQ618FR9UIvOhtDqUxNOWI2LAXufbBXJhetQl_OAtsZW_D_zJ9FSSDCL2Sx0tX2nnKofi4c9MYGJpfmj8Qm7DDdA2dIFcZGX2hlaG8vGFSdC4jhyqLXQ_jEU3YAW3x2FtVUW7cpLmg2NrZPxCeymLF-iS9tw1KqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71151" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71150">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=ruUvKS-e6vN0LEFQDdw1cvBQLZPMUnJULzByZORkMVtpkkY3-oQoHdWDeukpmbda1n0ZCc6E2ScZDANIGKF58MqPaXwNgiT9JAC4lEH-BQjyRW8mzarBqM5N5VkwwULw9-OdMgRy_j9Lq64Jb8WN-ClpzqDFPz0MSw2G0tHuAAhIaflexyb20WWA9QUauLOFFibZQ7GbinonertnKDXwlE0WIXNUbR1ssNq8fjs81vPZ-MwwxOm8ig_sGzxNOLOXJUsoHSManh0_LinCi1py4c3Qyoz0JAWRcmbvfma47b9J217yp1SxeVUsAUt8TlqFpB62xlfR8QlZyyLJwC2HjAxECLOaxtwmEH4UYdUN8d2qvrZfkBOfvXvcf-K56Yu_hP0waRN-nMbOrdgHucS37DLb6MS75uZ0IMyt7-6IOALt2O0Rp8Go0ccJDqw2pz4YmO4H9UOUzq_ntcTWntYo_cR3CW5JFY58M-2FzYFIoyq8FTaAQNPxYaclZMWcM0-aZPTZO1lcBmq5mlhbAedkyKl_p_K-cuSfyD0FkZJATFmH4-rSTb75vjy3hzaecYKRW9O4Gta1yXBlPi_Cvm7o1tVOw2qv5TvvbpR1MWAC6LNE146FEeZgZxkcAB9_ZbNCPyQlAlzkANwFRtOiHoOnDEhfBTByl15uLaysCVts2_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=ruUvKS-e6vN0LEFQDdw1cvBQLZPMUnJULzByZORkMVtpkkY3-oQoHdWDeukpmbda1n0ZCc6E2ScZDANIGKF58MqPaXwNgiT9JAC4lEH-BQjyRW8mzarBqM5N5VkwwULw9-OdMgRy_j9Lq64Jb8WN-ClpzqDFPz0MSw2G0tHuAAhIaflexyb20WWA9QUauLOFFibZQ7GbinonertnKDXwlE0WIXNUbR1ssNq8fjs81vPZ-MwwxOm8ig_sGzxNOLOXJUsoHSManh0_LinCi1py4c3Qyoz0JAWRcmbvfma47b9J217yp1SxeVUsAUt8TlqFpB62xlfR8QlZyyLJwC2HjAxECLOaxtwmEH4UYdUN8d2qvrZfkBOfvXvcf-K56Yu_hP0waRN-nMbOrdgHucS37DLb6MS75uZ0IMyt7-6IOALt2O0Rp8Go0ccJDqw2pz4YmO4H9UOUzq_ntcTWntYo_cR3CW5JFY58M-2FzYFIoyq8FTaAQNPxYaclZMWcM0-aZPTZO1lcBmq5mlhbAedkyKl_p_K-cuSfyD0FkZJATFmH4-rSTb75vjy3hzaecYKRW9O4Gta1yXBlPi_Cvm7o1tVOw2qv5TvvbpR1MWAC6LNE146FEeZgZxkcAB9_ZbNCPyQlAlzkANwFRtOiHoOnDEhfBTByl15uLaysCVts2_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
لحظه تهدید تخلیه خدمه نفتکش های جمهوری اسلامی توسط خلبان جنگنده ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71150" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71149">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛  پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند. دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71149" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71148">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI0QmXmC1piC2VCNVyRURVaZbwk0jnO_B_YTFWgVH2dpT9L4d7w-0tegUHSy1puCHbtSw8-fWRctG3UUIxGNgthPS56BOfG7TOMqRjmTwM5xo9YfsBi8H76O9dbwXCz10rRVaqD3Mssi-z1QIbzA-FPR3RGFiuSQNMeMRy-VOiRr4LOUp_XiNtUbyAP1cbptXP430KzDsojq8nJQFjyMWe9iZArrnzbzHqf7HA76t51FaXOFRr91kD6d7lF79aNTVR5HlMEiyxs3_DYiBkbBwWvnFRkab2nklCGJSqddrwBiq1Wo-d0Z6JhdkT5gtOUoowYNYQsUIrc5Ez84UYDcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
🇧🇭
سفارت ایالات متحده در بحرین:
با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره اوضاع وجود دارد.
سفارت ایالات متحده به شهروندان آمریکایی یادآوری می‌کند که ایران پیش‌تر زیرساخت‌های غیرنظامی در بحرین، از جمله هتل‌های منامه، را هدف قرار داده است.
آمریکایی‌هایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری خود را افزایش دهند و نسبت به احتمال لغو پروازها، بسته شدن حریم هوایی و اختلال در سفرها آگاه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71148" target="_blank">📅 18:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71147">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=n3knvJPhQhCrt232wh6h6kfi6fzrRo5qNUlwukavKbID7_9AyLt0wI_MHGR1mTGR39Yt2B5E9kK7nYvEerjnrBmfTK0nz1oV-hZ-xmsv_taTVAW9iAZhD6lCv8-COLsEbow2xoECAC61YocoiIj_7k84krnBzqVd2_40Ac69GesmfXd_HmCEcYUufqS2I0DUAuuxSVSg3OwMMMbP5-du31KrEssGG0ehE6_6DLuxtT9BFQLSzgkL2nlAXuH6KFki1EZpWMssbLEE71BxSI_DrzvBrlrQDgkRT1HQRD68azFMdsI4PW2q8nC1amzv8soUZ9YBAQ4Gtp1AsZ0FaOLhlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=n3knvJPhQhCrt232wh6h6kfi6fzrRo5qNUlwukavKbID7_9AyLt0wI_MHGR1mTGR39Yt2B5E9kK7nYvEerjnrBmfTK0nz1oV-hZ-xmsv_taTVAW9iAZhD6lCv8-COLsEbow2xoECAC61YocoiIj_7k84krnBzqVd2_40Ac69GesmfXd_HmCEcYUufqS2I0DUAuuxSVSg3OwMMMbP5-du31KrEssGG0ehE6_6DLuxtT9BFQLSzgkL2nlAXuH6KFki1EZpWMssbLEE71BxSI_DrzvBrlrQDgkRT1HQRD68azFMdsI4PW2q8nC1amzv8soUZ9YBAQ4Gtp1AsZ0FaOLhlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71147" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71146">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=ZWwtJ6FIfWgbE2LIwlNTLdSwCTfd-spfP0WySdjFzB-8nm5zJxFbVUjW5xExpPviNhK1Dyjl6ivWQAvdGTo9jW_JdW7Ph197aQfl8ThN1AQnGExuXf-t2q08twmpnA8DMjUuWb4tRfPUMZuwLAf52im7QQqCzui3bBwcQwODcJuejGksBcYHxavSNLyEIkgGyIs82L6exGDAMwHgUIvQYyp2pS_50qoEe4LwPd_ms3KT8W5D9DL0erqVneaD46LGmdDLOGv9IQdi-dSaPG-njBbnM0NuSZuOWA9_gAqX6fWmfMcI8EpvbqR0ubJlkqjuMxSCYyFSY8ZgyGwMWGmX2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=ZWwtJ6FIfWgbE2LIwlNTLdSwCTfd-spfP0WySdjFzB-8nm5zJxFbVUjW5xExpPviNhK1Dyjl6ivWQAvdGTo9jW_JdW7Ph197aQfl8ThN1AQnGExuXf-t2q08twmpnA8DMjUuWb4tRfPUMZuwLAf52im7QQqCzui3bBwcQwODcJuejGksBcYHxavSNLyEIkgGyIs82L6exGDAMwHgUIvQYyp2pS_50qoEe4LwPd_ms3KT8W5D9DL0erqVneaD46LGmdDLOGv9IQdi-dSaPG-njBbnM0NuSZuOWA9_gAqX6fWmfMcI8EpvbqR0ubJlkqjuMxSCYyFSY8ZgyGwMWGmX2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی:
به مردم بگیم قرار ما اینه که با قدرت‌های بزرگ تا بیست سال دیگه بجنگیم.
اگه مردم قبول کردن عالیه بریم ادامه بدیم.
ولی اگه مردم نپذیرفتن و راه دیگه‌ای نشون دادن حق نداریم نادیده‌شون بگیریم.
حتی پیغمبر هم با مردم خودش مشورت می‌کرد.
تو این کشور هیچکی از جانب خدا حاکم نیست‌؛ همه به لطف رای مردم اومدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71146" target="_blank">📅 17:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71145">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100451e13a.mp4?token=MCGvgKXbEJTZhM6QZ6VFc_Ybwx_JF-DIPgdmjgWDWVPG09ouqShkE8Mh3iG2hi5kAaPnIaVmF7yoTvCD2TgU6B9x614XFc6yujXlw40CY-tavjsEkJGDvR8vg3cNXNQMGvKbx43eUgkmvNFsNQOAUSnUAIx8detZ7OnlvuQqMy_x9UlECdWynL9-7fPIqIxIE1K0GWXcuJuIBQHrkGP5vg---wPnZGZIm97GWeDob0bXaNndW0CxEp-n1MzrOy5NeoakANo4otckhYyr9Jr9kzHLtN4GdvrKNk4s0GDO1lkXhHb6HipddTRNHW2IveOvIKTvI-N29t_ktDROWJkhsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100451e13a.mp4?token=MCGvgKXbEJTZhM6QZ6VFc_Ybwx_JF-DIPgdmjgWDWVPG09ouqShkE8Mh3iG2hi5kAaPnIaVmF7yoTvCD2TgU6B9x614XFc6yujXlw40CY-tavjsEkJGDvR8vg3cNXNQMGvKbx43eUgkmvNFsNQOAUSnUAIx8detZ7OnlvuQqMy_x9UlECdWynL9-7fPIqIxIE1K0GWXcuJuIBQHrkGP5vg---wPnZGZIm97GWeDob0bXaNndW0CxEp-n1MzrOy5NeoakANo4otckhYyr9Jr9kzHLtN4GdvrKNk4s0GDO1lkXhHb6HipddTRNHW2IveOvIKTvI-N29t_ktDROWJkhsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی: سایپا را ۱ میلیارد دلار می‌فروختند، ۲ میلیارد پیشنهاد دادم، نفروختند
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71145" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71144">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=qdoh3qrdiYsJwRHvkLLFV7023r33b0uqPK-zo8BtkLdY7cNlDDkrntfadmGxS7VRFeMc3VB7xU_tYf7zeQs-zN4ELQu35iN6vnBIMSHkUVH_7BwTye5VHB8ojfA_kOWhdigH1jujIpw6WgEtgvTeq-Nx4ujxkWtFGbx5ZdnTqXhFZzY_pXC7o-v8WZXwgb1Zaygz2EhljBW8q3yjaRV8hmPHhimOiXIxidJ4IXVmiEi9eUxHAoXclTLrdiWdJVSmRURBO6EgNtycZhClpW3pTNWL8qhzVmG5r3mQ0XNypUb4g4H-bGXhgo-13Z4Hvh-kK-Z_IPl_zAOyoZd3QDUQDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=qdoh3qrdiYsJwRHvkLLFV7023r33b0uqPK-zo8BtkLdY7cNlDDkrntfadmGxS7VRFeMc3VB7xU_tYf7zeQs-zN4ELQu35iN6vnBIMSHkUVH_7BwTye5VHB8ojfA_kOWhdigH1jujIpw6WgEtgvTeq-Nx4ujxkWtFGbx5ZdnTqXhFZzY_pXC7o-v8WZXwgb1Zaygz2EhljBW8q3yjaRV8hmPHhimOiXIxidJ4IXVmiEi9eUxHAoXclTLrdiWdJVSmRURBO6EgNtycZhClpW3pTNWL8qhzVmG5r3mQ0XNypUb4g4H-bGXhgo-13Z4Hvh-kK-Z_IPl_zAOyoZd3QDUQDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری ایرانیا هم انگار توی یه ایران دیگن و رفتن توی جنگلای شمال پستونک پارتی گرفتن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71144" target="_blank">📅 16:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=gGmxgPX0oR1IGh_Io_wriJ6xGp9xlDJVcX76HZtTQoOHLQSfROrve3Mb5XOPjeAtF3GV9x4EhvT3FC94bJ7FvkeWg4EjdUcg8pEFuco1TIatn2CmQFmKWpQXVhWyJMCvwDvuCIWB9G7TWcpOK0ZcFgYqfnx1WhEG_xJ_i_XctO_dlHX39K0R0BumOmLXLnEVIGsYUCONWm-F4jRmEuEqfzP5oXOp7n5YhhQqZp--gbly3EFlcrQf4Ogg-J1Lxt5f8S5fkbJBpQ8znJGJj6EtFCQgKblY2y0OfIO0HQ8Av4W8jH0qkGW9732_Ys9BwUCozKf6nBRlInFcha9HPjQqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=gGmxgPX0oR1IGh_Io_wriJ6xGp9xlDJVcX76HZtTQoOHLQSfROrve3Mb5XOPjeAtF3GV9x4EhvT3FC94bJ7FvkeWg4EjdUcg8pEFuco1TIatn2CmQFmKWpQXVhWyJMCvwDvuCIWB9G7TWcpOK0ZcFgYqfnx1WhEG_xJ_i_XctO_dlHX39K0R0BumOmLXLnEVIGsYUCONWm-F4jRmEuEqfzP5oXOp7n5YhhQqZp--gbly3EFlcrQf4Ogg-J1Lxt5f8S5fkbJBpQ8znJGJj6EtFCQgKblY2y0OfIO0HQ8Av4W8jH0qkGW9732_Ys9BwUCozKf6nBRlInFcha9HPjQqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تو چین یه نفر بعد ورود به مغازه‌ش که به علت نشتی پر از گاز بوده، کلید برق رو میزنه و کل مغازه میترکه ولی خوشبختانه زنده میمونه و بعد از اینکه به بیرون پرت میشه کون لختی فرار میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71143" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71142">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=jjmEGggyUYJA0zd13NxS0HJcSr8gtz3umMPVtcu31KOX54IF9yAdWW9_6PP5Zp4PhqYBd9Gw_czheS6mmi6D5_qvo6iW-MUGUaQUZIJNF8Lket2o1WB1eZYAbJJKeEN4HC8Uj4ygww4dDWjA19ggpC6Z3p7RuoXZJ1_BY1PZqA0rjRmZFzWibBqrneqW2IE-whSiG-MERmHonjgIlpkey-N5TzEmxwi813t3ZoRFozb47GED7eAhuz4N-t7kmdYNATVxSUUgD1RD2WKjRbDlB8eV8JtNjFJjsZyFZbcamFjhKzwghO_P1BqXbI4K_maLa0iAjtibWwK9yeL3bk144TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=jjmEGggyUYJA0zd13NxS0HJcSr8gtz3umMPVtcu31KOX54IF9yAdWW9_6PP5Zp4PhqYBd9Gw_czheS6mmi6D5_qvo6iW-MUGUaQUZIJNF8Lket2o1WB1eZYAbJJKeEN4HC8Uj4ygww4dDWjA19ggpC6Z3p7RuoXZJ1_BY1PZqA0rjRmZFzWibBqrneqW2IE-whSiG-MERmHonjgIlpkey-N5TzEmxwi813t3ZoRFozb47GED7eAhuz4N-t7kmdYNATVxSUUgD1RD2WKjRbDlB8eV8JtNjFJjsZyFZbcamFjhKzwghO_P1BqXbI4K_maLa0iAjtibWwK9yeL3bk144TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇺🇦
🇷🇺
یک مزدور برزیلی که در درگیری‌های روسیه و اوکراین می‌جنگید، لحظه حیرت‌انگیز عبور یک تانک از روی خود را — در حالی که میان علف‌ها پنهان شده بود — ضبط و در حساب اینستاگرامش منتشر کرد
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71142" target="_blank">📅 15:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71141">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=EEVqXxjE9PY2KD4OfNyc0nWz5qu4VOfVZ15oHt_by8U-_nBkGeJu49jqmNLZQZa5gfTqn-YT74WIRsItGDnVuXkM1RtYRtdyouFKi1iCYFpz1YV1YGu9xnVszhCLomwA1tBXKSOXtiK9XUI2VWkzumEerxu5GMKdMHKCcy_e-wgkGJadWvIa8FajJxWgZQwSb9UV4c1xG22PH0J-XDZXytu6_yoasLk5Jq7X1AtK-x4bCeq8zfUr9x9wiqsp_iARr_2Fxc7mQkqs-VOA4etxT7RLWOnQ-uV1enPVTTZX1vRrAvcxDkw8syu-pJ_eVx6cW1Li-gRZhBrhqh9Izr9BEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=EEVqXxjE9PY2KD4OfNyc0nWz5qu4VOfVZ15oHt_by8U-_nBkGeJu49jqmNLZQZa5gfTqn-YT74WIRsItGDnVuXkM1RtYRtdyouFKi1iCYFpz1YV1YGu9xnVszhCLomwA1tBXKSOXtiK9XUI2VWkzumEerxu5GMKdMHKCcy_e-wgkGJadWvIa8FajJxWgZQwSb9UV4c1xG22PH0J-XDZXytu6_yoasLk5Jq7X1AtK-x4bCeq8zfUr9x9wiqsp_iARr_2Fxc7mQkqs-VOA4etxT7RLWOnQ-uV1enPVTTZX1vRrAvcxDkw8syu-pJ_eVx6cW1Li-gRZhBrhqh9Izr9BEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه آخوند درباره شعار«تا آخوند کفن نشود این وطن وطن نشود»
؛
همونطور که رهبرمون رو شهید کردن یه آخوند دیگه جاشو گرفت
به ترامپ و نتانیاهو و منافقین داخلی میگم این حرفمو
تا آخوند شماهارو کفن نکنه ول نخواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71141" target="_blank">📅 15:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71140">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⛔️
این قبیله ای که میبینید اسمشون موکو موکو هست
؛
این قبلیه در افریقا که مثل سرخپوست ها هستن برای اینکه زنان قبیله خودشون دعوت کنن به سبک رقص های به خصوص خودشون انجام میدن
هر زنی در قبیله شون مجذوب رقص مردی بشه میره بهش میده و اصلا اینطوری نیست که کسی حتما باید زن شخص خاصی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71140" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=kI5HNjbGtUeF_vRazf5AAoWJzMbNiZ2GYvKmD5MjBl3nMnNx-izIZ8AP-dEUUsUim-fvdC1THyH-eFzQNFzvQaVK5QMi38ZVxqQ500QBgbigTIicWHZxscX2Zf0-fS2y86oEmLZftljE6wwQ9GpRsbuPoLGI03Djn7VmwetT1Zh6158FdBvwhx9CO3H2gd2wE2AOuvWGHPKGQBOZXCIcMZW2kPOaoBI7c86NjSP1LcwUNRlHVu2cZ4AEprhtq1me6UiMu7SusfjAdlXkNkDbCyvIMM_WpLOGaaREQSq8qI7-Ml9huy0fUA7ilZp-o33ijHzWYHGkUEvMGI9bOI40ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=kI5HNjbGtUeF_vRazf5AAoWJzMbNiZ2GYvKmD5MjBl3nMnNx-izIZ8AP-dEUUsUim-fvdC1THyH-eFzQNFzvQaVK5QMi38ZVxqQ500QBgbigTIicWHZxscX2Zf0-fS2y86oEmLZftljE6wwQ9GpRsbuPoLGI03Djn7VmwetT1Zh6158FdBvwhx9CO3H2gd2wE2AOuvWGHPKGQBOZXCIcMZW2kPOaoBI7c86NjSP1LcwUNRlHVu2cZ4AEprhtq1me6UiMu7SusfjAdlXkNkDbCyvIMM_WpLOGaaREQSq8qI7-Ml9huy0fUA7ilZp-o33ijHzWYHGkUEvMGI9bOI40ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
تصاویری از تورنتو کانادا بعد از بارش باران و طوفان
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71137" target="_blank">📅 13:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=ha9OEbZMjuiWjTOR7VOqCPV1Wb5BgrfxSJOj5AvmmNfgrRospIQaiRJVkNqCvxg2n5X2u5d-CSWHSKm2UapMYEbVZJk2CYb7x8z0MTDJdwg5FZA0JIuACwOrOPIIVCDcFIp12ZYih1h_R3lEFV3FKjE5b8tcn7fp5dVV2CJb8zBzuqzJrii48ViGTYPkezl--O_5AJq1AQK1f3KEKGhesf3EyCKbyJFC1CtTS8sytj29GZknGQqamCY-LlzHBo3Hkid8QA_EP-PQoz5rXwlf7RtvnTi39dzoqatY_N0QDqnl93nN1C0A5a6FBcDiZgYy8xY_owEEewJZ3mJeqol9xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=ha9OEbZMjuiWjTOR7VOqCPV1Wb5BgrfxSJOj5AvmmNfgrRospIQaiRJVkNqCvxg2n5X2u5d-CSWHSKm2UapMYEbVZJk2CYb7x8z0MTDJdwg5FZA0JIuACwOrOPIIVCDcFIp12ZYih1h_R3lEFV3FKjE5b8tcn7fp5dVV2CJb8zBzuqzJrii48ViGTYPkezl--O_5AJq1AQK1f3KEKGhesf3EyCKbyJFC1CtTS8sytj29GZknGQqamCY-LlzHBo3Hkid8QA_EP-PQoz5rXwlf7RtvnTi39dzoqatY_N0QDqnl93nN1C0A5a6FBcDiZgYy8xY_owEEewJZ3mJeqol9xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیرزن طرفدار حکومت که میگه:
نه پول میخایم نه چیزی دیگه گرونی هم تحمل میکنیم مسئله حجاب رو حل بکنید خیلی مسئله مهم تر و واجبی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71136" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71135">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=qHVt6AV_ovd5Aqa52WZkWDDgVVa9QUVRUlc7_PD7TVOoB42KUQ16jNw5wSkFkCGtPfNzLpHgJE5L513jbGefUR8Ef00u_QEuiYWglzt-4M1TQ-c3dXeSIKms8FhFu88Q_G-krDZUvocTPnpid57Sn-OXBhyGl-xTmI8hAcfZIX5gs34ZQrT6L6gFtn9URueT-7oKADTK5fZ9idkuBifD8ELNkQYp0amZi3nsDzW99Z1Sl_yhd0Zy6I3hH5WgOEKQ8Qyt5S73GZR-YOfD7sR7J1hx0g0qxbRb-2eehY01hjvDbCUh9SSjUQxz2YnluGnbKhQKVm4qmELDesc37BLb6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=qHVt6AV_ovd5Aqa52WZkWDDgVVa9QUVRUlc7_PD7TVOoB42KUQ16jNw5wSkFkCGtPfNzLpHgJE5L513jbGefUR8Ef00u_QEuiYWglzt-4M1TQ-c3dXeSIKms8FhFu88Q_G-krDZUvocTPnpid57Sn-OXBhyGl-xTmI8hAcfZIX5gs34ZQrT6L6gFtn9URueT-7oKADTK5fZ9idkuBifD8ELNkQYp0amZi3nsDzW99Z1Sl_yhd0Zy6I3hH5WgOEKQ8Qyt5S73GZR-YOfD7sR7J1hx0g0qxbRb-2eehY01hjvDbCUh9SSjUQxz2YnluGnbKhQKVm4qmELDesc37BLb6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
تصاویری از نفتکش ایرانی که چند ساعت قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71135" target="_blank">📅 12:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71131">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=cTNMIyCmD7n87h77sw2f_PsLuEbjVX1lnP5FUjWsbK1HVNI483clGh8WT8WD4nyONewfI04BUquuhArxbSVqryLqXo-JmRf7Lx0fIZi2pdt5p_u6ezf2FORr_2n-xpehDYuQNw2RJsyYKy7zmLVbHtFwXnmLBAWG6m604Hc4t749L9D6O-kNmrx9t2gJ9g1hIs46k1ykF2V4v9VZjuUjox40i-8ru-G9xgEa2X-FEDwvc2TfpUsM7bDth43CGt0I7-fM-x-O0S1y2qjtVuvv_fSRzxKxT208z37DNB-YqaSc-qViLyge9MbyTbiOjpFIytjommycSKMTMSnVBTp_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=cTNMIyCmD7n87h77sw2f_PsLuEbjVX1lnP5FUjWsbK1HVNI483clGh8WT8WD4nyONewfI04BUquuhArxbSVqryLqXo-JmRf7Lx0fIZi2pdt5p_u6ezf2FORr_2n-xpehDYuQNw2RJsyYKy7zmLVbHtFwXnmLBAWG6m604Hc4t749L9D6O-kNmrx9t2gJ9g1hIs46k1ykF2V4v9VZjuUjox40i-8ru-G9xgEa2X-FEDwvc2TfpUsM7bDth43CGt0I7-fM-x-O0S1y2qjtVuvv_fSRzxKxT208z37DNB-YqaSc-qViLyge9MbyTbiOjpFIytjommycSKMTMSnVBTp_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇱🇧
خبرنگار اعزامی صداوسیما به لبنان سقوط تپه علی الطاهر در جنوب لبنان رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71131" target="_blank">📅 12:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71130">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد  خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود. تاکنون اطلاعات رسمی و دقیقی درباره…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71130" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n97-1n3baaU6Q3LvebutqVHCnTvRduu89zgeIAsEcrBJ6qBt9OOG8kybqcvBzIsiy6EyJ22MtOVzokxXTORNnAUDd5xfeZ3qOPx4ri-hqPjLEyYbPchDpWPW_4WCGPohBptydtydye58tYTIIxKlcqQkUi6iwjutcI3AehIvTW2ip1un6fGjLrhk7hPLqmdza4AAnW7smgwNfns7dfCvO9lPYdCOsOQKZbf2yUikdn1tLdtueynHhJ-T0D_uf6AREhcX80KNm6U_YNRN7DM9wankMi9nWP7Qc9mvGwsM75w__kitwE7ZEKOPND-BpyMgsuLBGml2-i6OMWfkiPtiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=e72-PWyHzw3yaSchIBLrvGblfPg1p28psqsQI3dyfpxXEAIn8RjOxC4ypFM3UVtSKzemNPK9Sf3-fAWHhXEYia-DlhLS2emYT0dXp2GZcmb_rk0qH5IlYZm4r81BNdVkCPHdDc6VqalwL5m4BAtmJmBTcGYahELBQz6HusZFQN6h7LqlWhgcDIFMDwM63LfB5GUmhs-ZzPA33phlANueivjXYlThyPV2n336Q2bLiMKAphf2Je0RvPJAoWAwSPJa8tYhIa9hSDLh2H7Tt9CXbMge6BLgwUvjLTtOJQgDObOADU1fNj8xyDCjt7-C9HwztU6ln0UTXs6dgFlWw7DoLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=e72-PWyHzw3yaSchIBLrvGblfPg1p28psqsQI3dyfpxXEAIn8RjOxC4ypFM3UVtSKzemNPK9Sf3-fAWHhXEYia-DlhLS2emYT0dXp2GZcmb_rk0qH5IlYZm4r81BNdVkCPHdDc6VqalwL5m4BAtmJmBTcGYahELBQz6HusZFQN6h7LqlWhgcDIFMDwM63LfB5GUmhs-ZzPA33phlANueivjXYlThyPV2n336Q2bLiMKAphf2Je0RvPJAoWAwSPJa8tYhIa9hSDLh2H7Tt9CXbMge6BLgwUvjLTtOJQgDObOADU1fNj8xyDCjt7-C9HwztU6ln0UTXs6dgFlWw7DoLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه پسر بدبخت پست گذاشته که اگه این پست ۵ هزار تا لایک بخوره، صاحبکارم منو میکنه! تورو خدا لایکش نکنین.
و حالا واکنش مردم دلسوز ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71128" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.
تاکنون اطلاعات رسمی و دقیقی درباره علت و منشأ این صداها منتشر نشده و جزئیات تکمیلی متعاقباً اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71127" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71126" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71126" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71125">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxZRpLoSPDdl5uZzK7hP9ZgmvwULYSe9pXNIGTHWwJkmVpU7a5uldNAyzv7KTdil3VOOcSxdnFlQGTfTbs08Ivx9uH3xDHfwR7v3iMtMYpX7tdhqbsyjSgRnJrMcrryRGfAgxn_KDUREMaTFfujcBFmznuwkwGCdyElusAQ0-J9UzNxYI-uqnt9F9ulkPSXg9-HpgmxZTfa7k42ka_UO1XV761wTOmOfzvpqM4BLRp5Q1ZHEsXmB0tKJjZGL2zyxgmcYrYmk_K5HPVpJ0_Ua0NLwSvC1iFQOgWreWcWnaE7BhjXA2iTDZXdxpcne2krd4gKwYXH_tni19WavSbJJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71125" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71124">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=a3gmA0QeR7iNw3sUqfRXiRsluM-qjzO4DF-X4U-Gfj4t7rvDJ-HsaL2-3VOa6gilF5wwkR7S0_uZbVgkuZicN--O713sSqyNTICD4DbjORffPjEVmkrgxl6JYAlD_2IZ0__svuwowAgc9f1YMnjfGq0_Lqcc61eMXJky7FE9WV8n1Gfl55t-R8EIvt_3FWcI7cwo8vfIdfRv4UZKJy8e9M-HZA-izx7r2HCKJWmfvSW_0RR5XsXufI4dPiQOGn8Z-OT7X4zpPKrDtY0-S8j9uOSmQ1PLGuVkXX99TbFYG2yEWP0L1-HUJP9i2UR2llxuHfrgIhs0-DHkl7s5bX39kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=a3gmA0QeR7iNw3sUqfRXiRsluM-qjzO4DF-X4U-Gfj4t7rvDJ-HsaL2-3VOa6gilF5wwkR7S0_uZbVgkuZicN--O713sSqyNTICD4DbjORffPjEVmkrgxl6JYAlD_2IZ0__svuwowAgc9f1YMnjfGq0_Lqcc61eMXJky7FE9WV8n1Gfl55t-R8EIvt_3FWcI7cwo8vfIdfRv4UZKJy8e9M-HZA-izx7r2HCKJWmfvSW_0RR5XsXufI4dPiQOGn8Z-OT7X4zpPKrDtY0-S8j9uOSmQ1PLGuVkXX99TbFYG2yEWP0L1-HUJP9i2UR2llxuHfrgIhs0-DHkl7s5bX39kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
معرفی لاکچری‌ترین مدارس ایران !
برای اینکه به علم برسی هم باید اول ثروت داشته باشی!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71124" target="_blank">📅 11:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71123">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=IU1oWpFOlC-o8aTSw8J7JAxm58HvuN7mwG0w7MdZ3HVD51nE2jhk0qTom4pbIw_gwvc_dOLS1oxbc5AqqMAL3M_8V7ylwHuUsT7l8D6AMzpcgFKrE4yjB7V1qOVC4LDrqEMSrYDITs_S6-Yi4rWnSWlgFQySDKFo-AzKt7WxmMCrgQ5XV4Oo91cvohlO082bED_r0A79Jq-CZGGXakbspNUHPykWKigk1TWfBW-QT2Rar_FgTZ9UYiMlS316hKkPZ0zXiLieOsj9nJg1U_b2oPE8Op-WyJjmrFer0hcKQ1eCmhRGHL1ST-g5aXi_u16-bAT9Q38XoMz_A8bSPGo2VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=IU1oWpFOlC-o8aTSw8J7JAxm58HvuN7mwG0w7MdZ3HVD51nE2jhk0qTom4pbIw_gwvc_dOLS1oxbc5AqqMAL3M_8V7ylwHuUsT7l8D6AMzpcgFKrE4yjB7V1qOVC4LDrqEMSrYDITs_S6-Yi4rWnSWlgFQySDKFo-AzKt7WxmMCrgQ5XV4Oo91cvohlO082bED_r0A79Jq-CZGGXakbspNUHPykWKigk1TWfBW-QT2Rar_FgTZ9UYiMlS316hKkPZ0zXiLieOsj9nJg1U_b2oPE8Op-WyJjmrFer0hcKQ1eCmhRGHL1ST-g5aXi_u16-bAT9Q38XoMz_A8bSPGo2VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسلا، سفر با تاکسی‌های خودران Cybercab رو تو تگزاس آغاز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71123" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71122">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=V3yV-WTaMGb8-SXZbX1jX6FPmi2ish_o_t-uWjRtaZIynqSR3FlOxMt2sKgxruCDF7oES9RP7BLQRANUX7u9dSw16QHe7OV4xYj2qPevUW1IH81KUY7we4A6L0oJYWmH8PX2695a_E9yc2yFqGK22h7KRFgAHH8cKIstn3cpzbgVyz3J-1lGbXhKyknyzodEIANEfzvlHzkBfkdUEZRipX-DoLOwvup_yKY33Ku0AmNKqTK7mgnmsfOg6dUD_BdIabsdEJnE43OmhQn07EO1NBOURB9oQXSHlwou_v_1lx6qX3ge7kO4zG8F_ocv0NTRMri9aFiiCCcc2UV_LHfyDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=V3yV-WTaMGb8-SXZbX1jX6FPmi2ish_o_t-uWjRtaZIynqSR3FlOxMt2sKgxruCDF7oES9RP7BLQRANUX7u9dSw16QHe7OV4xYj2qPevUW1IH81KUY7we4A6L0oJYWmH8PX2695a_E9yc2yFqGK22h7KRFgAHH8cKIstn3cpzbgVyz3J-1lGbXhKyknyzodEIANEfzvlHzkBfkdUEZRipX-DoLOwvup_yKY33Ku0AmNKqTK7mgnmsfOg6dUD_BdIabsdEJnE43OmhQn07EO1NBOURB9oQXSHlwou_v_1lx6qX3ge7kO4zG8F_ocv0NTRMri9aFiiCCcc2UV_LHfyDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
🇹🇭
کامیون‌های سوخت‌رسان مشغول انتقال سوخت هواپیما به ناو هواپیمابری «یو‌اس‌اس آبراهام لینکلن» (CVN-72) در بندر «لائم چابانگ» تایلند هستند؛ به‌طوری که از زمان پهلو گرفتن این ناو، روزانه ورود و خروج ۲۰ تا ۳۰ دستگاه کامیون مشاهده شده است.
این سوخت برای تأمین نیازهای «بال هوایی نهم ناو» (CVW-9) در داخل ناو ذخیره می‌شود؛
یگانی شامل جنگنده‌های رادارگریز F-35C Lightning II، جنگنده‌های تهاجمی F/A-18E/F Super Hornet، جت‌های جنگ الکترونیک EA-18G Growler، هواپیماهای هشدار زودهنگام E-2D Advanced Hawkeye و بالگردهای MH-60 Seahawk.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71122" target="_blank">📅 10:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71121">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deba41468f.mp4?token=ZXS5KnOQ_i6-dKs1MzzqWs2F-rG51zRhNhWRbTRE0Dj68PXiqso-CuEXra-39N7csqFyy7QdYGEIr8SenxIOFmKR4zuHTNe0A89RVd5DQNxXgnnjaAFK082LZQMa7UbnugHSrys76_vEHZGhaTCc1Ln-TxnHM2zopHCIqgxq1j7sF0PSoTzEXj6cpCwd4QWicPmNzYzQ4vYultRJ07nyLKNOmULXzt495xSpQxiOauDTHsnd10Cz6J59wW3PtvI6C7yg_vqRxj0HsDD8FMYUYOmfb-dwYvV_t5rllrwvnlqt_YMXIZLzVbDmYkp5hG0juS77SwMrHK1EXLJsEArfFxXAd6KOQRzOZVOzVUffp5pei2uUX6qdXHxgMhCnlIPLXwPglvenlIYroohqo8cG17N5UKnxryy5YyhH3fmWylrln7Ufn99vIIHuxhFSJcq8NbmHk5OT42-ZMXGLMekpX2GZBcKvBtt81n_xgr43_daFKi4N1zx3onj48azr2wsD7DkCvyDvlZTSNTyfzDyOliG8esnpw7hmR9e5sTDkRaE2UWWsLQueVqniyXFRfduJ6bvRt2N3CT0gMDHd4fQYoe6U98pDThSFjBbNDqjV8yk0M-o9R7gZvrhloADgatW1LYuYv14zj33oqJr2GSsimK4qfguBh5ikNmZK0ZUrYjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deba41468f.mp4?token=ZXS5KnOQ_i6-dKs1MzzqWs2F-rG51zRhNhWRbTRE0Dj68PXiqso-CuEXra-39N7csqFyy7QdYGEIr8SenxIOFmKR4zuHTNe0A89RVd5DQNxXgnnjaAFK082LZQMa7UbnugHSrys76_vEHZGhaTCc1Ln-TxnHM2zopHCIqgxq1j7sF0PSoTzEXj6cpCwd4QWicPmNzYzQ4vYultRJ07nyLKNOmULXzt495xSpQxiOauDTHsnd10Cz6J59wW3PtvI6C7yg_vqRxj0HsDD8FMYUYOmfb-dwYvV_t5rllrwvnlqt_YMXIZLzVbDmYkp5hG0juS77SwMrHK1EXLJsEArfFxXAd6KOQRzOZVOzVUffp5pei2uUX6qdXHxgMhCnlIPLXwPglvenlIYroohqo8cG17N5UKnxryy5YyhH3fmWylrln7Ufn99vIIHuxhFSJcq8NbmHk5OT42-ZMXGLMekpX2GZBcKvBtt81n_xgr43_daFKi4N1zx3onj48azr2wsD7DkCvyDvlZTSNTyfzDyOliG8esnpw7hmR9e5sTDkRaE2UWWsLQueVqniyXFRfduJ6bvRt2N3CT0gMDHd4fQYoe6U98pDThSFjBbNDqjV8yk0M-o9R7gZvrhloADgatW1LYuYv14zj33oqJr2GSsimK4qfguBh5ikNmZK0ZUrYjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی:
الان کافه‌های مردم را می‌بندید بعد شب آدم می‌فرستید که بیاید تعامل کند.
می‌خواهم فیلم و مستند درباره این موضوع تهیه کنم... آن شخص هم فکر می‌کند که با ۱۰، ۲۰ سکه زندگی‌اش را گذرانده
بیکار کردن ۸۰ نفر در منِ بابک زنجانی چه اثری دارد؟! اصلاً فردا بیایید آتشَش بزنید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71121" target="_blank">📅 09:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71120">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po6yNKzH3J1q0SpZH_UDG02HekmLfLy_w1hvmLFHeivcdiX-iQJphTdcs7CTUfffFFPwB0By3GneUKse6hl8DC95B6dqIvdYKzLN0Sat1wo0NdisC0txzXPP0KhoH9_bFGligoi4bRKRVH6hdYZrFQEF-M27yASt_uEe7H-vJ763xyz8YCNE8B9w7S7rObKZewdLL-_ZNCu50zOXGbrfPRbiIhzD5_ClnohSWKRXM7HZOaxGYRpq92COz1ngg-wII1U4CcIEr_wBQH4DCCiXYHejy5KA6a4LO0qvfqg3SXNhUDSEtQd50VYSiqCIrLVr3RgSWu-Zm_MrxZhIgLyTZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇴🇲
نیویورک پست:عمان بی‌سروصدا پیشنهاد ایران برای دریافت مشترک عوارض از کشتی‌های عبوری از تنگه هرمز — حتی به‌صورت داوطلبانه — را رد کرده است.
این اقدام، ادعای هفته گذشته سپاه پاسداران مبنی بر توافق دو کشور بر سر تقسیم درآمدهای این آبراه را تضعیف می‌کند.
عمان معتقد است که دریافت عوارض از کشتی‌های عبوری ناقض قوانین بین‌المللی است و تحت فشار آمریکا و کشورهای حوزه خلیج فارس، از این طرح عقب‌نشینی کرده است.
ترامپ دو بار تهدید کرده است که در صورت موافقت عمان با دریافت عوارض، این کشور را بمباران خواهد کرد.
ایران در دوران جنگ، نهادی برای مدیریت تنگه ایجاد کرده بود و از هر نفتکش مبلغی بین ۱ تا ۲ میلیون دلار عوارض می‌گرفت؛ اما بدون همکاری عمان، هرگونه سازوکار دریافت عوارض در دوران پس از جنگ، فاقد وجاهت قانونی خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71120" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71119">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71119" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71119" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71118">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1xi9NT2lCusxtMgrN5hivz-rxU2OVP8O2RIyG9eTvXJE0httlZN7Pnb-1jRahGOjDo5VhnKRHqhbAUJy9ybcXUAg-dSE_nh2hhDSWIlKfEAn5cjxz4ITyXHUduq9BmizERhvhhXiNkGCU7LEWsFpFNdANcxKSqaLLPBsvSjNpW15Gt5-4oCudbMxjwovd9eR4cnBIjFl6-SEhoZuliZc8y2KHDe_B1NmD5XyQXThPSTl9WJ3Ch_XA5dNBpqrEO9eO-Yuvku9pNIucitg6KzjNZuUf0EsDunndZ76VAiKO3td9AwZQcbCiyU_mt9NgZqvsd86osyvC7l3AbxhZldrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71118" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71117">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=FZbSX-YoJroXb2J7hi_y4DGClTS2029quel6RUcNzKqbH5oTUPxbhCUZTjVXfPuywmjsiedX3dAaLCu98U3RF8ruW6iIvbptRV8WjyeyilApVsGzEgL5p71xTX2xjkxoyjNb3VxS2VuKEKOiwCDi6U57LvuoaaJH4BqhTrOyP6WRhh6uvx7q_h6xgC8Xny_YE2NSdfmV8y93ef0ltUYHz2aH0vtcGxIhf3iVlQXuiIXC2dKLoOqhKMLSmQjMQ1pJS5Z3IMrqKl3yAB3Pads0ol0BQzzBfz6VJqCPpXUn5UVeVLXHmDQzhuRzToA7TNd1IS_HoWil8Irbh4YUMJUUaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=FZbSX-YoJroXb2J7hi_y4DGClTS2029quel6RUcNzKqbH5oTUPxbhCUZTjVXfPuywmjsiedX3dAaLCu98U3RF8ruW6iIvbptRV8WjyeyilApVsGzEgL5p71xTX2xjkxoyjNb3VxS2VuKEKOiwCDi6U57LvuoaaJH4BqhTrOyP6WRhh6uvx7q_h6xgC8Xny_YE2NSdfmV8y93ef0ltUYHz2aH0vtcGxIhf3iVlQXuiIXC2dKLoOqhKMLSmQjMQ1pJS5Z3IMrqKl3yAB3Pads0ol0BQzzBfz6VJqCPpXUn5UVeVLXHmDQzhuRzToA7TNd1IS_HoWil8Irbh4YUMJUUaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
مردم آمریکا چه زمانی باید انتظار تعیین تکلیف (resolution) در مورد ایران را داشته باشند؟
🇺🇸
ترامپ:
انقلاب(Revolution)؟
🎙
خبرنگار:
تعیین تکلیف(Resolution).
🇺🇸
ترامپ:
تفاوت بزرگی است. فکر کردم انقلاب(Revolution) جالب‌تر بود.
⭕️
🗒️
به دلیل تلفظ نزدیک دو کلمه راه حل/تعیین‌وتکلیف(Resolution) و انقلاب(Revolution) ممکنه ترامپ اینجا به عمد کلمه انقلاب رو انتخاب کرده باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71117" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71116">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=L-1PLZepMYSJ3rxob8YhJoIyw9mGzgewgM8jDO9A_tmCHMFJSFDXN1roCFT9OlvUn48oC1HyORtvcGYY469OP2ztq4Fe1inLopDrhIqDlflT5cPLGNkc6qiIr4OgHakbuvJ4YiCy6X-uc9lEgbMMbg_0VUu5QFLHTy1EQwRYwGwWmxgi9Ob2zRhaYSXoGOZrT7wy65jKrUZFc23_Aurvmbpfq6MaJ27kWq7H2A6ocLEk8k_fR44LrRM1vcLhCrbvhV3WQ3koauWXZ6qgI_jwwY16ajMTC45BXfAusyMd_ptNz7CsMUzY9i4uKFGfmO_ToaQPTC5pubNHJB0vlc-G5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=L-1PLZepMYSJ3rxob8YhJoIyw9mGzgewgM8jDO9A_tmCHMFJSFDXN1roCFT9OlvUn48oC1HyORtvcGYY469OP2ztq4Fe1inLopDrhIqDlflT5cPLGNkc6qiIr4OgHakbuvJ4YiCy6X-uc9lEgbMMbg_0VUu5QFLHTy1EQwRYwGwWmxgi9Ob2zRhaYSXoGOZrT7wy65jKrUZFc23_Aurvmbpfq6MaJ27kWq7H2A6ocLEk8k_fR44LrRM1vcLhCrbvhV3WQ3koauWXZ6qgI_jwwY16ajMTC45BXfAusyMd_ptNz7CsMUzY9i4uKFGfmO_ToaQPTC5pubNHJB0vlc-G5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ایتا و روبیکا از یچیزی رونمایی کردن که حتی خودشون هم نمیدونن چیه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71116" target="_blank">📅 23:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71115">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=NGAxHqCiNf8kWaj37NhJHpFsooGsgjLnpXAaFijLuQEWZvqTcL0MK4tOnVUbov_JO45umgPorwbGLeaFJKO2itJ-PgoU8nEFHP8AdyWERMJepptoApSYbuC5L8evkQm_fZoKBpxLu6BmKnMaHegPpukD1Gz8nhJw0tI0gqwSnPUWdebF3pbXnGfgb0k8bxTFf55xvOrFIN9rcOCg7VVd6McHsNAtV1m2BllKkge8juSNiROCYd49DGjPZL-FuydGMT_qD-TuibG4Ofg9yKxrrxA1_r0TR0rcBIEMTeJctGOdHWi2rh1A0C3w9RXWvujM51xqMQFdQAUDHAi6VXrOeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=NGAxHqCiNf8kWaj37NhJHpFsooGsgjLnpXAaFijLuQEWZvqTcL0MK4tOnVUbov_JO45umgPorwbGLeaFJKO2itJ-PgoU8nEFHP8AdyWERMJepptoApSYbuC5L8evkQm_fZoKBpxLu6BmKnMaHegPpukD1Gz8nhJw0tI0gqwSnPUWdebF3pbXnGfgb0k8bxTFf55xvOrFIN9rcOCg7VVd6McHsNAtV1m2BllKkge8juSNiROCYd49DGjPZL-FuydGMT_qD-TuibG4Ofg9yKxrrxA1_r0TR0rcBIEMTeJctGOdHWi2rh1A0C3w9RXWvujM51xqMQFdQAUDHAi6VXrOeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
طرف اندازه یه گاری پول جمع کرده و الان آورده تبدیل به دلارش کنه، کل این همه پول نقد شد فقط ۳۰۰ دلار
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71115" target="_blank">📅 22:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71114">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=YwPtBMKJ1VND2eC8rWhlLUndEcR6MZPQNw3wc7d_66uVPdiHXY3f9lz-xdjOpLpmvgJQnrQGSapbcALaTv4J_Dl5JiAAIFgIF_etPePw6MW31tES-dlLCW0E8C4Z4_f8vt4oiGeus1uvKWQfsFV09L9JXEIUFxkiuCrmHjJgpgdyrO7vjWi3kbLoTYTD5tuy4tgRtgimtkFT0JTTe3INEyRQwwF3yZjl-s41S6HvZitV322fWrWoXcRHbsk3_RhHvTPpdSnDw7Uoqq-g7PVadLjF1wGDfWk9L9VCioUuw1alOoyhkI23FKdhog5aZOnD4d5eLWW_UCee_BIThIu6qlNe9sViECsiNlqOnYr8iKpDzvWQkPAW4K2pmLKKubpDy-5LQw2JnQd9w6tOBkK3KxuSTs26O0uAw3uErWS9vlW7sdSQu8bt2hcCg_Y9E4tGhAraWehPgCFnmqAAn6aRKhFsDHMiIeW2KHaHU1_Pkv8jxTNnJRpqVl85eWJClwnB33v7ZYvYepHoF2eo9pX9Vd_oxoc_1lUltEJlhPTG1ztJ5q6_77Zgn5EBZQ5_fOJBOnSBHiIc-rPivHETTrwFkMS1YoQUYLI5v9c9LxDAQzLKoUWevJqGzMNlp_u43XSs2HezLBj4MATiyAbwbdngtebS_GLx7OH8SzMTDh5BNNM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=YwPtBMKJ1VND2eC8rWhlLUndEcR6MZPQNw3wc7d_66uVPdiHXY3f9lz-xdjOpLpmvgJQnrQGSapbcALaTv4J_Dl5JiAAIFgIF_etPePw6MW31tES-dlLCW0E8C4Z4_f8vt4oiGeus1uvKWQfsFV09L9JXEIUFxkiuCrmHjJgpgdyrO7vjWi3kbLoTYTD5tuy4tgRtgimtkFT0JTTe3INEyRQwwF3yZjl-s41S6HvZitV322fWrWoXcRHbsk3_RhHvTPpdSnDw7Uoqq-g7PVadLjF1wGDfWk9L9VCioUuw1alOoyhkI23FKdhog5aZOnD4d5eLWW_UCee_BIThIu6qlNe9sViECsiNlqOnYr8iKpDzvWQkPAW4K2pmLKKubpDy-5LQw2JnQd9w6tOBkK3KxuSTs26O0uAw3uErWS9vlW7sdSQu8bt2hcCg_Y9E4tGhAraWehPgCFnmqAAn6aRKhFsDHMiIeW2KHaHU1_Pkv8jxTNnJRpqVl85eWJClwnB33v7ZYvYepHoF2eo9pX9Vd_oxoc_1lUltEJlhPTG1ztJ5q6_77Zgn5EBZQ5_fOJBOnSBHiIc-rPivHETTrwFkMS1YoQUYLI5v9c9LxDAQzLKoUWevJqGzMNlp_u43XSs2HezLBj4MATiyAbwbdngtebS_GLx7OH8SzMTDh5BNNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
یه بلاگر ایرانی رفته چین و ربات انسان نمای چینی رو به مبارزه طلبیده؛
حرکات ربات به قدری تمیزه که انسان واقعا از آینده جهان خایه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71114" target="_blank">📅 22:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71113">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=sXy9VV6EsfiNZTzZ-Dv9se1Q0NIy5cFpHze-Y57QKtGQsn1ydGep6Uxif-V90TkdPPcFbp5FSoUzmJ9i4I48o9VWwHhUFQawQ9AkHoHc_ohe1IegwZ9MxigeCaGWpu4FHzI-XMZfQiILz_SN7Qhz8OEGV8x0vBxGK5kQnX-os3X6wTo9Xj-VC0mOhzv8E59WFBJpTIj6Qch8KnN5mxWj3H_-TF1jAekruUTg8VqrUoQ_7_yvsH2IPwlSZCRyXKI_FeaNe2as0ydwL11P6WsSqVhEIP8GP1bQfdjGG8RVy2tWwPup--brhmMb1R6MoBkUANhcPw8I6BBXji6dRv6Twg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=sXy9VV6EsfiNZTzZ-Dv9se1Q0NIy5cFpHze-Y57QKtGQsn1ydGep6Uxif-V90TkdPPcFbp5FSoUzmJ9i4I48o9VWwHhUFQawQ9AkHoHc_ohe1IegwZ9MxigeCaGWpu4FHzI-XMZfQiILz_SN7Qhz8OEGV8x0vBxGK5kQnX-os3X6wTo9Xj-VC0mOhzv8E59WFBJpTIj6Qch8KnN5mxWj3H_-TF1jAekruUTg8VqrUoQ_7_yvsH2IPwlSZCRyXKI_FeaNe2as0ydwL11P6WsSqVhEIP8GP1bQfdjGG8RVy2tWwPup--brhmMb1R6MoBkUANhcPw8I6BBXji6dRv6Twg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا بعضی دخترا طی یه حرکت فوق‌العاده و زیبا، دارن هرچی ژل و بوتاکس تو صورتشون بوده رو خارج میکنن تا نچرال به نظر بیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71113" target="_blank">📅 21:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71112">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTvIo8mQd848MIQK4bJFkCkfsxIibFuKsfPr_aZ30hHsCn3j6NFrUqM9IV8PFdVUQtI2AOWWX6G2pVd-Q5Sgn6Z1Jd5RWutD8pbSr9OOEteM8bAk5kAvjwm7v5aFgyFOWM9jyfmM6aXOU-h3ZLGsB2J0x2ipPAGyW1oNBfReVvDf0En45YoG0TizHNHOgKM1KRqk-6avQZZR3uMp4pbrbhBkiYqlwY6_zhDYFUbLYUYLdCdmCAJxS2wYCUEClsRirKbRbMmtWt7xAT4P8eeaITKa5V80QvIs9kfFS5poRpFiF4vQ1ueZYII3_T_GzNEUmQu328ew_Ds5j0IgvToApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👎
قرارگاه خاتم الانبیا: حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
❌
خبر بالا که بطور گسترده در حال انتشار در رسانه هاست فیک و نادرسته، همونطور که می‌بینید سپاه پاسداران و قرارگاه خاتم‌الانبیا هیچ اطلاعیه‌ای مبنی بر حملات پیش‌دستانه منتشر نکرده
@HutNewsPlus</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71112" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71111">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTMeVaZUeiYrRZOAW0OCkd8ZxRgbz6eoKHGduchib76AsMzYCMVeoGI5IdtB7VisH0xY-HKKcxzLxDdqF1r6KkkUXNbK7Gk7cE4H0mB9hmVyouqQjSm741OKTZXmsIUfoj73dSuL5KCawndp8iHYHLaLQoz4AtVmg5Ip6XB08l4M68l_sFaVmuMgluuKUF4w8GV5AR_iFrFXY3D6FZhCR3cRYK0UAnS2tf3JO_bsfz-G46Wv_D-u1k3PQZ5Y7ueOd54jlR0ULosWuqY3KVAWitH_GbG-OslB7MQ11SfNKCPihqm7ADwkX6C_ExcobY_7dlJdBDsn2sofz_cWPwmamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد آمریکایی به کانال 12: در حال حاضر هیچ اطلاعی از وقوع آتش‌سوزی در پایگاه‌های آمریکا در اردن وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71111" target="_blank">📅 21:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71110">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=Ri58pbIDbznI0k9vW_z0CptJaSm-o7PVo-DBEc6R3YjfI84bjAtqObHfw9Oc-puykTvOzPoCM06-Yo0jXN7HPmckivgFSjp1neRCKdJ5W9P7S_GluebB_o4yHJo-c6T0qp8uzYF6raouMrbSw1Vxkm0-i7POX7RnTADnuW52pKruYASkueOSjrDetHE0Ik9iDrxeZywNjvorblSDPHAEzpnVW2Nv7uwkVOboCMCO-lq-vtJUpljJQ6TNj2nrNnKEMiGXw-gy5VGGRYUv5eA61LJol7rlU0vLkfnDCE7puUiLFaCzBHIJP7yFNLKwGH5lLWA9J4cK36W75GtOLzG48A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=Ri58pbIDbznI0k9vW_z0CptJaSm-o7PVo-DBEc6R3YjfI84bjAtqObHfw9Oc-puykTvOzPoCM06-Yo0jXN7HPmckivgFSjp1neRCKdJ5W9P7S_GluebB_o4yHJo-c6T0qp8uzYF6raouMrbSw1Vxkm0-i7POX7RnTADnuW52pKruYASkueOSjrDetHE0Ik9iDrxeZywNjvorblSDPHAEzpnVW2Nv7uwkVOboCMCO-lq-vtJUpljJQ6TNj2nrNnKEMiGXw-gy5VGGRYUv5eA61LJol7rlU0vLkfnDCE7puUiLFaCzBHIJP7yFNLKwGH5lLWA9J4cK36W75GtOLzG48A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک ها از ایران به سمت اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71110" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71109">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در اردن رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71109" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71108">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=VFhiWtnutyMRcZHAwdjFn_d2RnLyijRcJjM4DbOeRfLCjmUd-huOOcOd2Uvto6dkKmd4vj1qtMn7rKTa_N6XABgvmdoWmpWagCyarSz47HwoAfwjVLBMjxQXNsjJv_zVKifMvmHazpeyr1Ln4ZNxsN3AM0RFBqeYmcogAqvyyBSSuC2d-zdZfFw9f_TZ7YGDj5wO6rChi32sWcvUjqAwg-I1Vy6QFp7gjn4oS074iUx8CSfD8IMek2Lz8_JKezSFSn8SFmpIbthHV_k9YcNkxfxtP1in_a0kSyznhqvILOBARrenvTjr3Um7LBkzn14xKw_-IxDNT03K55wSCq5oJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=VFhiWtnutyMRcZHAwdjFn_d2RnLyijRcJjM4DbOeRfLCjmUd-huOOcOd2Uvto6dkKmd4vj1qtMn7rKTa_N6XABgvmdoWmpWagCyarSz47HwoAfwjVLBMjxQXNsjJv_zVKifMvmHazpeyr1Ln4ZNxsN3AM0RFBqeYmcogAqvyyBSSuC2d-zdZfFw9f_TZ7YGDj5wO6rChi32sWcvUjqAwg-I1Vy6QFp7gjn4oS074iUx8CSfD8IMek2Lz8_JKezSFSn8SFmpIbthHV_k9YcNkxfxtP1in_a0kSyznhqvILOBARrenvTjr3Um7LBkzn14xKw_-IxDNT03K55wSCq5oJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇨🇳
بِسِنت درباره ایران:
آن‌ها محموله‌های نفت را به سمت چین روانه کردند. منتظر اقدامات مربوط به این موضوع در روز سه‌شنبه باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71108" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71105">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=EWrxGh8mz3ErpG_nXLoMKh1PfJqRY-GmPNlXKFOQDi49JOKcGJibkXi6sAlpPrGebj021p-FpXje198gVok8KACNdJHZuqykTMmyyzXTlaZalQOHBdf9NpD5SUnrF2n1GOgd6EAksJp7tno1UmPwwUtCyIwI_GfehDbhunGqZvcESFcvRec-LGo0KpXQeRHau4XBK342hFWQfNj1fobAlURiO6uFaj2VBxhmxSGWJJn-5zWD2-IKpFlwSyPPeGKFHEfwRWNrfR1g1tehpqOAUxcIkDz2jQF-TUWUbrNwh3R_i4gTy81gPbeGR5LWciombMwblqEyIed3SWuhmXcGYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=EWrxGh8mz3ErpG_nXLoMKh1PfJqRY-GmPNlXKFOQDi49JOKcGJibkXi6sAlpPrGebj021p-FpXje198gVok8KACNdJHZuqykTMmyyzXTlaZalQOHBdf9NpD5SUnrF2n1GOgd6EAksJp7tno1UmPwwUtCyIwI_GfehDbhunGqZvcESFcvRec-LGo0KpXQeRHau4XBK342hFWQfNj1fobAlURiO6uFaj2VBxhmxSGWJJn-5zWD2-IKpFlwSyPPeGKFHEfwRWNrfR1g1tehpqOAUxcIkDz2jQF-TUWUbrNwh3R_i4gTy81gPbeGR5LWciombMwblqEyIed3SWuhmXcGYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بابک زنجانی: دلار رو بدید دست من تا یک سال رو همین قیمت نگهش میدارم وگرنه با همین فرمون کشور تا یک سال دیگه نابود میشه.
من رو ۷ سال بدون بدهی انداختن زندان و همشم تو انفرادی بودم. همه اموالمم ازم گرفتن. وقتی آزاد شدم حتی ۱ دلار نداشتم.
با چند تا تلفن ۱ میلیارد دلار پول جور کردم و چندتا شرکت تاسیس کردم.
من میخواستم سایپا رو به قیمت ۲ میلیارد دلار بخرم که نشد ولی خودم میخوام کارخونه تولید خودرو تاسیس کنم
من توی خارج کشور بانک داشتم پولای وزارت نفت تو اون حساب بود. اونا تحریم شدن پولاشون اونجا گیر کرد گفتن تقصیر توعه و حکم اعـدام بهم دادن
تمام بانکای ایران بیان جلوی من بشینن ببینیم من بیشتر میتونم سرمایه جذب کنم یا اونا. فقط با چندتا تلفن. تا معلوم بشه کی اعتبار داره
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71105" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71104">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=RdsYsKUk7X2znxV_zYCgfWK10FS6hlKviPRoWp_nndiXoas2SWyOTlzvpvLI2fnLAb6XNBq-VrdZv9WTFfDLoeuA6r6tRdb7zOrokkbyf9XnOgo_KgkAtg2zGfOPEqISlfH_F2bOzsWRHoaQPXg9o7TjhKGXkiYfPnbvBrw0dAmjq6laPB8pm1V9VYaLKyd84uGcGzIUrYNWERGY5VMfAzGdGSQreGzkhLaZ-945yd8riOEXkcf3f1E-zIDEQVb1dL-pMI_km3fRx3-rzVYDQ7yxrJQQiFIMjDX1FyABVANPoSiWr0EocT3fmOBcyWbY5IybaDUs74dHhW5lCoMSVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=RdsYsKUk7X2znxV_zYCgfWK10FS6hlKviPRoWp_nndiXoas2SWyOTlzvpvLI2fnLAb6XNBq-VrdZv9WTFfDLoeuA6r6tRdb7zOrokkbyf9XnOgo_KgkAtg2zGfOPEqISlfH_F2bOzsWRHoaQPXg9o7TjhKGXkiYfPnbvBrw0dAmjq6laPB8pm1V9VYaLKyd84uGcGzIUrYNWERGY5VMfAzGdGSQreGzkhLaZ-945yd8riOEXkcf3f1E-zIDEQVb1dL-pMI_km3fRx3-rzVYDQ7yxrJQQiFIMjDX1FyABVANPoSiWr0EocT3fmOBcyWbY5IybaDUs74dHhW5lCoMSVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت درباره ایران:
متحدان ما در امارات متحده عربی در خصوص این بانک مستقر در دبی همکاری بسیار مؤثری داشتند. اکنون ما برای متوقف کردن تمامی این جریان‌های مالی غیرقانونی، با آن‌ها وارد همکاری شده‌ایم.
ما برای رفع این مشکل با آن‌ها همکاری خواهیم کرد، چرا که بانک‌های متعددی در سیستم مالی آن‌ها فعالیت می‌کنند.
ما نمی‌خواهیم این بانک‌ها را نابود کنیم — هرچند اگر لازم باشد چنین خواهیم کرد — اما اکنون همه کشورها در این مسیر با ما همراه شده‌اند.
این پایان کار برای این رژیم است؛ آن‌ها یا باید [رفتار خود را] عادی‌سازی کنند و یا با عواقب آن روبرو شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71104" target="_blank">📅 18:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71103">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=EYNkVcC_rOhfBibpVqOGGql92wJyWYOQbgaajHRaRzRib9e3jLDocODvp1jIQLcCaEJ8zbvLSc04tWikgMGtrRpTnfokPiKr8b_GvpI6S3N_VyXUTXbJgU8sqRJsFvo5-7YSCN_xcFm6Ma2MRvH8lU9TiCYs_Lk-X5zdQVNmCTLC5DC_lzlTyE5_98QPWZmYrMvTPR8zpbZmAS3wXk3B2eOUU0cMf7bTQAsMkNOBr1sj0k0D5bH975Hz3w4r0Ae6ujkuPoXz1wNSGgNQJjGWfpwT0VFs-KdMVZAQdTYB6f_ebkKmF6Lfas6YbwZFZqo2k6jgInUU7r-gCZ_3sY_BXz3zqTCABwVdhcMh-UowZUymlAIjjdUEo0EKFpSqQj8d_k3TxpkIsoiuEzZVqCt_Z2cX0M_YLqT3TSZVBSv8VbYt6n6joWrfiMAFyZ-ZQ0OP7q0vpfWSWEMGhupK8bUc58KeVMezFBEsRbG4eQS_6Jj0A7wIptqva6-WoD6Kwnl8dMxRVOm_hNDS0WXf1NALMYeyGZO93yOK-thXXT2d8wm2LEwRhXocaz8YNpF6vvEHeTdywl1MKJAqy0xYx-9Qt3zXCw65FlUAOJq7soBPImiwV2VTDIA4Rt_Jw6mQE3SxyFHxJ5qRvjP-ff6nhAxOkm981HdoRi-gfa6KsoWiM_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=EYNkVcC_rOhfBibpVqOGGql92wJyWYOQbgaajHRaRzRib9e3jLDocODvp1jIQLcCaEJ8zbvLSc04tWikgMGtrRpTnfokPiKr8b_GvpI6S3N_VyXUTXbJgU8sqRJsFvo5-7YSCN_xcFm6Ma2MRvH8lU9TiCYs_Lk-X5zdQVNmCTLC5DC_lzlTyE5_98QPWZmYrMvTPR8zpbZmAS3wXk3B2eOUU0cMf7bTQAsMkNOBr1sj0k0D5bH975Hz3w4r0Ae6ujkuPoXz1wNSGgNQJjGWfpwT0VFs-KdMVZAQdTYB6f_ebkKmF6Lfas6YbwZFZqo2k6jgInUU7r-gCZ_3sY_BXz3zqTCABwVdhcMh-UowZUymlAIjjdUEo0EKFpSqQj8d_k3TxpkIsoiuEzZVqCt_Z2cX0M_YLqT3TSZVBSv8VbYt6n6joWrfiMAFyZ-ZQ0OP7q0vpfWSWEMGhupK8bUc58KeVMezFBEsRbG4eQS_6Jj0A7wIptqva6-WoD6Kwnl8dMxRVOm_hNDS0WXf1NALMYeyGZO93yOK-thXXT2d8wm2LEwRhXocaz8YNpF6vvEHeTdywl1MKJAqy0xYx-9Qt3zXCw65FlUAOJq7soBPImiwV2VTDIA4Rt_Jw6mQE3SxyFHxJ5qRvjP-ff6nhAxOkm981HdoRi-gfa6KsoWiM_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
همه خواهان پایان یافتن این وضعیت هستند. ۴۷ سال از عمر این رژیم شرور می‌گذرد و دنیا دیگر از دست آن‌ها به ستوه آمده است.
مردم ایران مردمی عالی هستند؛ اما رژیمی سرکوبگر بر آن‌ها حاکم است.
یا رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، و یا باید دید چه پیش می‌آید.
ما آن‌ها را از نظر اقتصادی خفه خواهیم کرد. آن‌ها در وضعیتی قرار دارند که من آن را «آرواره‌های مرگ اقتصادی» می‌نامم.
ارزش پول ملی‌شان در حال فروپاشی است و صادرات نفت آن‌ها به صفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71103" target="_blank">📅 18:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71102">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=X_6img29dm8Z8nUdsPaSUOXHVmaD4WJcQaNIOdIElLGC2cwowdyfJw-90j0O1wEqjVDITkHaur8zYgQoyc_VWAJZbedL-G3u0lURhtNh39HhnhZCD0JZm68PSAafRfzFcN973IheMg52yGZlb9rOpbB9JkDk2MmYCGjCslpiL3YRxKot4jlcKT1Xbr9j3pv1ztu84blC7uqEtcTbT9bXky1RsLaUjpVquv1OMYQShZoz0uhFMCMhaqfJSlFUVHpE7B5RUd-pYklF5qHp5NdwlsP-BBEKll5kY46yKFBUkJwlO7pwt8gRX-fqmyAvsn5rmaZEWyWzzIfZ7T-IG2xdiTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=X_6img29dm8Z8nUdsPaSUOXHVmaD4WJcQaNIOdIElLGC2cwowdyfJw-90j0O1wEqjVDITkHaur8zYgQoyc_VWAJZbedL-G3u0lURhtNh39HhnhZCD0JZm68PSAafRfzFcN973IheMg52yGZlb9rOpbB9JkDk2MmYCGjCslpiL3YRxKot4jlcKT1Xbr9j3pv1ztu84blC7uqEtcTbT9bXky1RsLaUjpVquv1OMYQShZoz0uhFMCMhaqfJSlFUVHpE7B5RUd-pYklF5qHp5NdwlsP-BBEKll5kY46yKFBUkJwlO7pwt8gRX-fqmyAvsn5rmaZEWyWzzIfZ7T-IG2xdiTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ما بانک دیگری را که با ایران مرتبط است، تحریم کردیم. هفته گذشته، یک بانک مصری را که پنج شعبه در دبی داشت و ۱.۸ میلیارد دلار در اختیار این رژیم قرار داده بود، تحریم کردیم.
امروز بانک دیگری را تحریم خواهیم کرد و احتمالاً هفته آینده نیز بانک دیگری را تحریم می‌کنیم.
ما به سیستم مالی می‌گوییم:
ای عوامل مخرب، ما می‌دانیم شما چه کسانی هستید. خودتان هم می‌دانید چه کسانی هستید. کارتان تمام است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71102" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:  Golden Global Portföy Yönetimi Golden Global Varlık Kiralama Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71101" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:
Golden Global Portföy Yönetimi
Golden Global Varlık Kiralama
Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن معاملات (wind-down) با این نهادها صادر شده است
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71100" target="_blank">📅 18:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuKaln2rqBti8i7nQFTK9YaGygEJvVMjN3MgY4DX_AsW4OCs1QzFIKiBUZgFanf0zPxm9xqUML8RYLqU7AUfQxCaT4Ey14BovTanZXCwwDBNPgWVGmkKEeWY8d4YPSN8MmQgzH86QddbhLapmGFdEXB2qYACGW4zZUbxr4m6b55YkYtLDNdQSb72MUgRV_ccaHsxQ399ZZ7Q1k2MdbusAn_eoovQvlArLXJnhKsp1R9bdyN62W7vnmvLCx03LjtrDjz1zjD_bNW7V45xsbPrJSVcXBe86UKs5nfUGoxxh212wHy0thlsRGixmV9NnBoeeqhwQl7VNnlDL0Rvtb_u33W4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuKaln2rqBti8i7nQFTK9YaGygEJvVMjN3MgY4DX_AsW4OCs1QzFIKiBUZgFanf0zPxm9xqUML8RYLqU7AUfQxCaT4Ey14BovTanZXCwwDBNPgWVGmkKEeWY8d4YPSN8MmQgzH86QddbhLapmGFdEXB2qYACGW4zZUbxr4m6b55YkYtLDNdQSb72MUgRV_ccaHsxQ399ZZ7Q1k2MdbusAn_eoovQvlArLXJnhKsp1R9bdyN62W7vnmvLCx03LjtrDjz1zjD_bNW7V45xsbPrJSVcXBe86UKs5nfUGoxxh212wHy0thlsRGixmV9NnBoeeqhwQl7VNnlDL0Rvtb_u33W4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیزر دوم فصل اول سریال هری پاتر که از کریسمس 2027 قراره پخش بشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71099" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71098" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71098" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sX8l4o2FlE3gnZhAeKL70HD83om4oDM_gN-W1tn7w_1d1h4YcDk_SC63fN9X_MmbvCAOnAA5buVgx2_95mRldPdIzW68x2PFwXtFDPQr65fIeKl6EadRxVg0i80-h459SjmbpModF_9w-GQKmAh1c5IU5erNS_kE-UEoyy6mWDtqAE9fjfM5QYMst6jgKtEkwFpVxVtcLNBazrCEC8KtNdxcF72GJuNe9uiHF6_vjT8SS7uROghsR5m1olOUxKbnnAu14vNKX7Z9Twy3TUqF1ymocMdbPGA1y_ewr0lVlP4r06nooAMkD3_dp2D85ov9AsIag6uYraAXtxS9jA6zzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71097" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71096">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">〰️
سنت‌کام:
بیش از ۲۶۰۰ تفنگدار دریایی و سرباز نیروی دریایی آمریکا، بر روی ناو جنگی USS Boxer (LHD 4) مستقر هستند و این ناو جنگی در حال حاضر در خاورمیانه در حال انجام ماموریت است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71096" target="_blank">📅 17:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=CSJ7a6NQ5jh3WkXy7N0-C7D138qiR5fFirAR-mY80x3ve0maRkrvDzXs63kqGNRgri_DOBLDSlFqKGoWYMpDD4jZY27feCTE4mLnzChHIQItShrk5ynbR0dz588DZcQh2hVHJ-5chMe-69HWguxN7nrt6wjZdWnrUwsfbv4tffYoLiZbs2ToR23tVDKrIjvJkCwm76IKg3b1egaGiztJ6odjiDffiinUieA4MA3UxlP7HA0yijkMROD3c7sBN4YinwTITRSK2JZcyQKKk9ysHWB-Wu1OxpnwZCLEroD4sIuwHY-l_fpSUE5eJXuNEmQTvD_oG_B-ucUR3GCJyhU0Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=CSJ7a6NQ5jh3WkXy7N0-C7D138qiR5fFirAR-mY80x3ve0maRkrvDzXs63kqGNRgri_DOBLDSlFqKGoWYMpDD4jZY27feCTE4mLnzChHIQItShrk5ynbR0dz588DZcQh2hVHJ-5chMe-69HWguxN7nrt6wjZdWnrUwsfbv4tffYoLiZbs2ToR23tVDKrIjvJkCwm76IKg3b1egaGiztJ6odjiDffiinUieA4MA3UxlP7HA0yijkMROD3c7sBN4YinwTITRSK2JZcyQKKk9ysHWB-Wu1OxpnwZCLEroD4sIuwHY-l_fpSUE5eJXuNEmQTvD_oG_B-ucUR3GCJyhU0Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ببینید از خانمی که داره از تجربیات رفتن خودش به تور کویر میگه...
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71095" target="_blank">📅 17:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=PlAg6TOduSY6yckTFxwYPmUxr_m97YB4GO1o6Eo7c7eIiFtYT4G-hnUZMbJLt7QpThTVku6Q0SKpa0NU3gvkp-y46rN7YC631urzJRor2uoQskzJms0gM1pocMgTSkxeL73ETmqsHXBlthkinD6ujYGCvypjFs8oaIH1-0NM5QQNsEWa1BT0dvK676259HHqLX1TbwwjJezacILo1CQXhgb2zZ_E9yoj3yzqUQZmICla0VHh3lISElifN_oXRkpzCMbr10cxXbU-OJ6Jbbb3ZKWgvlxIKBJNlo9zJvVgaK_-QViW7ShI3rqcyoZ_CNy7SQNI0g_Pus4ZMRZRFJ0KcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=PlAg6TOduSY6yckTFxwYPmUxr_m97YB4GO1o6Eo7c7eIiFtYT4G-hnUZMbJLt7QpThTVku6Q0SKpa0NU3gvkp-y46rN7YC631urzJRor2uoQskzJms0gM1pocMgTSkxeL73ETmqsHXBlthkinD6ujYGCvypjFs8oaIH1-0NM5QQNsEWa1BT0dvK676259HHqLX1TbwwjJezacILo1CQXhgb2zZ_E9yoj3yzqUQZmICla0VHh3lISElifN_oXRkpzCMbr10cxXbU-OJ6Jbbb3ZKWgvlxIKBJNlo9zJvVgaK_-QViW7ShI3rqcyoZ_CNy7SQNI0g_Pus4ZMRZRFJ0KcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سامسونگ A17 که یکی از ضعیف‌ترین و تخمی‌ترین‌ گوشی‌های بازار به حساب میاد، قیمتش به 100 میلیون تومن رسیده.
البته این قیمت واسه دیروزه و امروز احتمالا گرونتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71094" target="_blank">📅 16:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71093">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=LFhmXaq3Q_fGbPx2xK9peJ3LVbGH-D-Qv9zJwL_iGKVJOOQrGX3eLvUHJHFybgN-CSsrQ93RhhqdnV9xpVLxsljNyUSgH3REInfPbiifU38-gGxDL9gxspfKhtw2vDNN7xAge5ZXxaCxtRgjN41YHXiacbunDeV8P_8HnlyNgF8KjAjn_Vq7Tob_fW-i7mvqUgI6wLHIAw7HLQqndIIHSlxToBkgFNlEfsz_uFQrzwGWuWqAaY-A5i73XkOjz6roaNv9dLTH4FnQOxJFGvAWEX9RVy2XTvqbiMBjuv5qjHX_HNbioztOJv7C75ROaxeUl9lBoWRXm0Typ39Z-9xXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=LFhmXaq3Q_fGbPx2xK9peJ3LVbGH-D-Qv9zJwL_iGKVJOOQrGX3eLvUHJHFybgN-CSsrQ93RhhqdnV9xpVLxsljNyUSgH3REInfPbiifU38-gGxDL9gxspfKhtw2vDNN7xAge5ZXxaCxtRgjN41YHXiacbunDeV8P_8HnlyNgF8KjAjn_Vq7Tob_fW-i7mvqUgI6wLHIAw7HLQqndIIHSlxToBkgFNlEfsz_uFQrzwGWuWqAaY-A5i73XkOjz6roaNv9dLTH4FnQOxJFGvAWEX9RVy2XTvqbiMBjuv5qjHX_HNbioztOJv7C75ROaxeUl9lBoWRXm0Typ39Z-9xXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک راننده کامیون:
الان کنار مرز پاکستان هستیم میخوایم رد بشیم اجازه نمیدن.
رفتیم پیش رئیس گمرک میگه طرف پاکستانی اجازه ورود نمیده.
پاکستان گفته به ازای هر ماشین باید دو میلیارد تعرفه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71093" target="_blank">📅 16:02 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
