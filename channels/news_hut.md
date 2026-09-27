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
<img src="https://cdn4.telesco.pe/file/S3wgdqW2d8hdyUXkpgTgwpjZP-vOfDuEbH7fOvdFntQX8FpAuMSmJZrQFlg-ndwR4JBpYUqQhRy8s4gE7oymxDbxBsaqeEx3a8k4bNen0v4oXqCrxSTnmqkxL8-ntpQZD-ROeSoPwB5zIoj2fTVwXFP_HEvTbtlD4oosneOI15pOJC0CJDRmX3_Xy523C1aguJRYUcaTUrwOxDCPWtHzKQDsKH37ktyTxzeqRrYc1mZpeydvDZUUvNSbKpdZwJk98ZmEkGAjIgJDgwGLMCSobLUCsDzUWvGbM8260WME-4bcpA9tcSK6wptfafPGyKz3aYVmZtgCc-pa63PVE5B8Rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-72364">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=Cvf6KCMbBP0s-Bt91NXwxcWncjR1-h001jid-R1R0W81Fc2C53hJLdAxnVkjVHr5n-9_1ATdITyzTmn_YDDKb8jEXbbWpkOSOGh0ufbZx6VK77hRmA3hZ0poga9B6-7uJkxtK-G1hpdziHq8M7Fjyzbmi9Y-fVCFEbT0gKlhKkF6bwbOt10oSKtILF9s7HhpeTe7_XMg_6BoAC4I4RFtW9K200Z8PGsmy3jtuJOa55yOiH5qX0REfwpIZVN1kdQV-H7b-8ne3CU1UKM2qophs2y2RmnnHUwFPxxHVHBmlt1eNLwGIqeQdbMZXyyocWw4v7l89k9EHRDuWibPkm74403KBjMf2Fx0ed9AZskI5HtqB3bhuIIPwwJJSmRNNnbBEDeCmXu2sGsq3To271iAO2qxOd0_2TmpL_LElZnI8L8XfU7JlXkmpQ_VCUZpFX7ss5OfSdPJtgwzCj209-OnsILtfwDVCGOt-7BU-voyAmgB8uVew_Bc_4XJtZBaYSCuKZHnetL5Hmt0CUjewWgzc7fhYoheyK0xd3FO33NBzcZX-JOy6k8zMW1HeTBANy17bVrTzxCNv5uuHX09gG8EncInSABqwbumxIe0MFuESo48HrbYcD_3poD-fgbOWyD54be0QuriCLVe49hPYRdAFAKb3Za37fQXpLDgMecXbPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=Cvf6KCMbBP0s-Bt91NXwxcWncjR1-h001jid-R1R0W81Fc2C53hJLdAxnVkjVHr5n-9_1ATdITyzTmn_YDDKb8jEXbbWpkOSOGh0ufbZx6VK77hRmA3hZ0poga9B6-7uJkxtK-G1hpdziHq8M7Fjyzbmi9Y-fVCFEbT0gKlhKkF6bwbOt10oSKtILF9s7HhpeTe7_XMg_6BoAC4I4RFtW9K200Z8PGsmy3jtuJOa55yOiH5qX0REfwpIZVN1kdQV-H7b-8ne3CU1UKM2qophs2y2RmnnHUwFPxxHVHBmlt1eNLwGIqeQdbMZXyyocWw4v7l89k9EHRDuWibPkm74403KBjMf2Fx0ed9AZskI5HtqB3bhuIIPwwJJSmRNNnbBEDeCmXu2sGsq3To271iAO2qxOd0_2TmpL_LElZnI8L8XfU7JlXkmpQ_VCUZpFX7ss5OfSdPJtgwzCj209-OnsILtfwDVCGOt-7BU-voyAmgB8uVew_Bc_4XJtZBaYSCuKZHnetL5Hmt0CUjewWgzc7fhYoheyK0xd3FO33NBzcZX-JOy6k8zMW1HeTBANy17bVrTzxCNv5uuHX09gG8EncInSABqwbumxIe0MFuESo48HrbYcD_3poD-fgbOWyD54be0QuriCLVe49hPYRdAFAKb3Za37fQXpLDgMecXbPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بالگرد رسانه‌ای تصاویری از بمب‌افکن‌های B-1B نیروی هوایی ایالات متحده ثبت کرده است که در محوطه‌های پارکینگ شرقی پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) مستقر شده‌اند؛ این در حالی است که یگان‌های خنثی‌سازی بمب همچنان مشغول عملیات پاکسازی مهمات منفجرنشده در منطقه «وِل‌فورد» (Whelford) در مجاورت این پایگاه هوایی هستند.
این پایگاه برای ایالات متحده در جریان جنگ علیه ایران، نقشی حیاتی داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/news_hut/72364" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72362">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUrP3xXxwNJ8NVejr-_uQUV7YA_wOcmAQjwoZqTTY8Ru2zQ6ruD2UU7OQhiAc-iGV1A_QgLeg5h2n4RzGHAlErT_FHWWGP3a9c-uIOcO2MlQUrzkRoeU8YJss8n3Eq2rxKSklbnzlbmkBj3hXXFpmr_3b6AfDEprjn7aIvZT-JTMC1yAeXZGBKmXSPBY-XOx9-cY_C9Uh6SsTXMMrKSED6EH6DbJASIq6W49pBnCDd8qFxNussjrZwRrlK5JKYgnGxIUspsa9FE4NodjrpOfXumQMD99juQAiIKV3d-hksTtQuZiFLQ0KzrrgsOHCo5IR8eS7iQESpTUFHNtmE8xMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=UJhe5a0dFTgW5JSy_0_JdFhw4Wm1UkWh9k549Z0QHtFuPop1cafzdmzPwr3KrR3MoAJlbH91orenaZvRYJOFchELhOZoLHsD5oaILRpdvMl-gI2675EZNetfxDLuM4Sc9giT2clGdqFpmAyxxXW_sNJ-2Wd9Bl8xJ-RDL3HtJE2RnfaE0Nwp2QZapPi-x6xbB4vf4ctnG2Ieqli4Obh68UZvjnwy9pwJrMbjRzAibpqWfjy8FpJLleq5r1PZAHfSYSGEOZLSw_o7tZri8AfXX11XAobGC3i3dSEycZooet0hBRiWT8dHaozX8Evu0EyR2YyYzpQJ49clpeJ0FMaNVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=UJhe5a0dFTgW5JSy_0_JdFhw4Wm1UkWh9k549Z0QHtFuPop1cafzdmzPwr3KrR3MoAJlbH91orenaZvRYJOFchELhOZoLHsD5oaILRpdvMl-gI2675EZNetfxDLuM4Sc9giT2clGdqFpmAyxxXW_sNJ-2Wd9Bl8xJ-RDL3HtJE2RnfaE0Nwp2QZapPi-x6xbB4vf4ctnG2Ieqli4Obh68UZvjnwy9pwJrMbjRzAibpqWfjy8FpJLleq5r1PZAHfSYSGEOZLSw_o7tZri8AfXX11XAobGC3i3dSEycZooet0hBRiWT8dHaozX8Evu0EyR2YyYzpQJ49clpeJ0FMaNVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی ارتش اسرائیل لحظاتی پیش منطقه «حداثا» در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/news_hut/72362" target="_blank">📅 15:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72361">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=Gdkznlma7VIAgM-0R-UXK0B4pokgwxSF8CqVkSKpvVbjx0c6UW8gyUxNNUKYfOkfbloJb0ZdBxY8nSa34ZLAmzpKrV78WHtIoWuc23b0QRwd_fmI73G3tBT6bF8frYs92Vz4dfZ-wO2KZFYv6MlgKgi1sgG7vBTaYlSclioXOqDmbR_cGT6VcKIP1CmCIQWyVo3TLgsqlObWQ9jz5MGyaw5DwguzRz25aIQ4SfaHVYOt5rObNablzsqzCPbkzHkTV2pldlkyqIk5b53Pq6Ixv3hXkwsyNDpzvl6k1LjDq8gvw3ybqLoaQni6a-vgGWcnfOjb9021sLRl4WzL6t4E2ztN9JxZh0BMVrRaV-ySct7GIWB3tR25EIEvFyr4iqJ8BMfYVAuweEs0sPmhwwsrqLKT4xNtQ4wKt54DCsgyKbTSIsI42J5zFJTzw7wewDHUgrDxvG-zKxgqXGPi7-BE-Irq_Hgu05xbgRvmLO3uuaqA8HA115j2syM18zW18p8mzRJ6D3f-3FzKzqTVFoaOBqTf_ClQMVkRFQkPe_UNdSdeYYrTh4Y7xQCH3PcwiBonPLb7Doge-1viZu6wrQLNqubh39-o_Cw63XjLdrCzuXerQa8jdl7dHtDgNVTX0wbrxAm-rKSKXXycQygCyqJa-fejNCeeZW5iDrDi9smQIRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=Gdkznlma7VIAgM-0R-UXK0B4pokgwxSF8CqVkSKpvVbjx0c6UW8gyUxNNUKYfOkfbloJb0ZdBxY8nSa34ZLAmzpKrV78WHtIoWuc23b0QRwd_fmI73G3tBT6bF8frYs92Vz4dfZ-wO2KZFYv6MlgKgi1sgG7vBTaYlSclioXOqDmbR_cGT6VcKIP1CmCIQWyVo3TLgsqlObWQ9jz5MGyaw5DwguzRz25aIQ4SfaHVYOt5rObNablzsqzCPbkzHkTV2pldlkyqIk5b53Pq6Ixv3hXkwsyNDpzvl6k1LjDq8gvw3ybqLoaQni6a-vgGWcnfOjb9021sLRl4WzL6t4E2ztN9JxZh0BMVrRaV-ySct7GIWB3tR25EIEvFyr4iqJ8BMfYVAuweEs0sPmhwwsrqLKT4xNtQ4wKt54DCsgyKbTSIsI42J5zFJTzw7wewDHUgrDxvG-zKxgqXGPi7-BE-Irq_Hgu05xbgRvmLO3uuaqA8HA115j2syM18zW18p8mzRJ6D3f-3FzKzqTVFoaOBqTf_ClQMVkRFQkPe_UNdSdeYYrTh4Y7xQCH3PcwiBonPLb7Doge-1viZu6wrQLNqubh39-o_Cw63XjLdrCzuXerQa8jdl7dHtDgNVTX0wbrxAm-rKSKXXycQygCyqJa-fejNCeeZW5iDrDi9smQIRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های یک خانم به خاطر شرایط اضطراری که واسش به وجود اومده و عدم وجود سرویس بهداشتی در مترو.
@News_Hut</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/news_hut/72361" target="_blank">📅 15:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72360">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تمسخر پزشکیان در شبکه فاکس‌نیوز؛
در مصاحبه ای که با رئیس جمهور ایران پژاکیان(پزشکیان) کردیم همش جوابای مبهم و بی معنی میداد.
اصلا اون به هیچ سوالی جواب نداد.
حتی نتونست بگه رهبر رو دیده یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/news_hut/72360" target="_blank">📅 14:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72358">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5drwvHb96D1QM08kgRJv1vrkvClFawy08Wm_7Q0Sqn85ycJrWmAv2w6hrVkE92ShWvODx3E5L5gAFgNWi_6b2dnxxRhOiv6unY0aSAdAH6KtQyDyyvh_asJqLI0mlaXqJl3SUoykx5LIRMdrH3HBpafZTrPU8SEbvZzCOp3Hw_YO2ZamxHNeYWItvQFr9tSihlbtRgQf6iiNhJOOBujhynELOp9smo2nX7jeU18lfoubpJZ9WqV2V8VuaYh87XQwPQHD5V6DKXgu-h1ly4DWkvuEkCE1LC57MJgrWXfhcGdPw2TOnE8Zq_0g-v_L6LGhpleokr8YSPBfhvmwThmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=QH80-oaVdweEKZgkjms7r1v19SB_ojDeYtQZaora9PJiDy0GgP4egXpsElXlOtbv1V4y6z-v_i5Vfs9vSzeYCxHXqkmmleOLp34rn-NGV1HjKL8c-VUajp4qCacXjGUWYIhDwWvKIhxMwDLVkmy_iH2g7wKPLalF1pMzGFKRgy8wvHg19hf_jWhHC7EZpjCJqS8DW4x0HQS_sLJrgJzFv3PlBsVN03fktxhqtAjNAHnhD5XmN4NobttmoLZVfdLuyCNFTd9zNGs0yzhQjMt8LxdsSMzp37kaqMtDdohqLjw_-UGn2mSlbq0Ncrgn4q2dYPEuEmnDffoK1muR4D8jgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=QH80-oaVdweEKZgkjms7r1v19SB_ojDeYtQZaora9PJiDy0GgP4egXpsElXlOtbv1V4y6z-v_i5Vfs9vSzeYCxHXqkmmleOLp34rn-NGV1HjKL8c-VUajp4qCacXjGUWYIhDwWvKIhxMwDLVkmy_iH2g7wKPLalF1pMzGFKRgy8wvHg19hf_jWhHC7EZpjCJqS8DW4x0HQS_sLJrgJzFv3PlBsVN03fktxhqtAjNAHnhD5XmN4NobttmoLZVfdLuyCNFTd9zNGs0yzhQjMt8LxdsSMzp37kaqMtDdohqLjw_-UGn2mSlbq0Ncrgn4q2dYPEuEmnDffoK1muR4D8jgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی
سپاه پاسداران:دومین زهپاد(زیرسطحی )ارتش آمریکا در تنگه هرمز شکار شد.
شناور توقیف‌شده از نوع پیشرفته «Remus 600» است که به گفته سپاه، متعلق به «ارتش آمریکا» بوده و با اهداف جاسوسی فعالیت می‌کرده است.
این شناور طی یک عملیات هماهنگ و با بهره‌گیری از قابلیت‌های اطلاعاتی و جنگ الکترونیک توقیف شد و هم‌اکنون برای استخراج اطلاعات در اختیار کارشناسان سپاه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/72358" target="_blank">📅 14:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4389424237.mp4?token=rHTBi-9mW_w9_au3Dv5aHDg7z8pGRjEfKwTwHjS8q2Cuprw9IduvFYfu9RzSz-rv3X_JYTNqeF9zBiqHIwE8rLaeJAaiaC2I7jk4Lciw4GxoPTCqoQikB87fFdfs8_-2hQ8sXdRy58VRb671TqOrLvagOOCRbz_95BJ-96O6tzarGd_BK3odX50-rU2zjKEJtoDZLBt_0LnM_peMg8KQ__BtCgvyn7tXzoxrFDyeZBbOk-NccUwCXv0ttTP3XcJxMI21Rxq1fNo0WG6Lzs333pWNjIWPG21kCRe6E8IJE647m_2bzp2t-1S5AyKvwcYsPRFoE8S9yOw-fNEDGX9RSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4389424237.mp4?token=rHTBi-9mW_w9_au3Dv5aHDg7z8pGRjEfKwTwHjS8q2Cuprw9IduvFYfu9RzSz-rv3X_JYTNqeF9zBiqHIwE8rLaeJAaiaC2I7jk4Lciw4GxoPTCqoQikB87fFdfs8_-2hQ8sXdRy58VRb671TqOrLvagOOCRbz_95BJ-96O6tzarGd_BK3odX50-rU2zjKEJtoDZLBt_0LnM_peMg8KQ__BtCgvyn7tXzoxrFDyeZBbOk-NccUwCXv0ttTP3XcJxMI21Rxq1fNo0WG6Lzs333pWNjIWPG21kCRe6E8IJE647m_2bzp2t-1S5AyKvwcYsPRFoE8S9yOw-fNEDGX9RSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش در چنین روزی سید حسن نصرالله به همراه چند فرمانده ارشد حزب‌الله و سپاه پاسداران در حمله نیروی هوایی اسرائیل کشته شدند.
در آن عملیات ۸۳ بمب سنگرشکن ۲۰۰۰ پوندی به مقر فرماندهی زیرزمینی حزب‌الله در زیر یک شهرک ضاحیه بیروت اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/72356" target="_blank">📅 13:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=WEJ6kLNT4GsM4nJRUAQkIZlAqEeK3ZyHO1qHjmYB4AHXU7lX8gTxGP2mGhpkkOlRdGOxydfRMwqPBLeWCA0KGHvzM__yr4yb4Smt-ET4qiU1KStJvHhsME8K-Cub7z4Zoq2OguDL1Pji4xFM9DMDk_Wo9br-90Cx96GXnXSvDhJ5ph7l0rMZAn4Wdvyr2zEPZkUBuJmvdAQH1XgEuPtMd54CrTWmLNisH0WMggq4RwkFGzDEk9RbDZDGJdNnUHllE-bnuyue9DImVgtdQAAMo1kMwmZAgqTXGxlTrDiwBA7o89J5D-urM5vO85GAKRqEegW0kkqPvuHgQnuxhJABWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=WEJ6kLNT4GsM4nJRUAQkIZlAqEeK3ZyHO1qHjmYB4AHXU7lX8gTxGP2mGhpkkOlRdGOxydfRMwqPBLeWCA0KGHvzM__yr4yb4Smt-ET4qiU1KStJvHhsME8K-Cub7z4Zoq2OguDL1Pji4xFM9DMDk_Wo9br-90Cx96GXnXSvDhJ5ph7l0rMZAn4Wdvyr2zEPZkUBuJmvdAQH1XgEuPtMd54CrTWmLNisH0WMggq4RwkFGzDEk9RbDZDGJdNnUHllE-bnuyue9DImVgtdQAAMo1kMwmZAgqTXGxlTrDiwBA7o89J5D-urM5vO85GAKRqEegW0kkqPvuHgQnuxhJABWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابطحی میگه: سال ۸۸ توی زندان گفتند اعتراف کن که خاتمی به اسرائیل سفر کرده
گفتم خب سفر نکرده
گفتند اگر بگویی که به اسرائیل سفر کرده، آینده دینی ایران را ایمن نگه می‌داریم...!
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/72355" target="_blank">📅 13:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72354">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0MVEqbsQHYwUh8feNtqvnpctw4HEmkhmObseyhu4PbTUAV536J_cu5S5Iic-E0e-wIcmzNfK8NGv6zaNXD8eR5QY1ITv3H8KmJ_I5BcJeAOFanPONoWLAavoH6at2zpJqAeyczjpyVw9DAoxt2zWzfIgckT6gV4CcVCdighesgvbQAcIs7nJcmPB_5ktNfy7R-Z56ynJieHwWaJVc3bjK5wUa-fr_-dPmQ8L-lCqt42XGxAQRqTTlmMDUTzkFT3AGip3UC4Lcm2nT_l9k0bPdTEi3N_BedGaIzi6ViXNojvg5eG6VNdTB72t11yAIRlspvknP5ZAGrV4a7IvKnEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا:
در پی آغاز «عملیات طرد اقتصادی» (Operation Economic Outcast)، وزارت خزانه‌داری ایالات متحده اقدامات مالی هدفمندی را علیه بانک‌ها و شرکت‌های ارائه‌دهنده خدمات هوانوردی اعمال کرد. به دستور من، تیم‌هایی به سراسر جهان اعزام شدند تا با کشورها رایزنی کرده و خواستار اقدام علیه رژیم ایران شوند.
این تلاش‌ها در حال به ثمر نشستن است. ترکیه و عمان از توقف پروازهای «هواپیمایی ماهان» به کشورهای خود خبر دادند. امارات متحده عربی نیز تمامی پروازهای شرکت‌های هواپیمایی ایرانی را متوقف کرده و بانک‌های تجاری بزرگ در امارات و ترکیه، انجام هرگونه تراکنش مالی با ایران را متوقف ساخته‌اند.
حتی رهبران ایران نیز به پیامدهای اقتصادی این وضعیت اذعان کرده‌اند، چرا که ارزش ریال به پایین‌ترین حد تاریخی خود سقوط کرده است.
من از دولت‌های بریتانیا، ترکیه، عمان و امارات متحده عربی قدردانی می‌کنم. ما به همکاری‌های خود ادامه خواهیم داد، زیرا برای جلوگیری از پیشبرد دستورکار تروریستی تهران، هنوز کارهای بیشتری باید انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72354" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/72353" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU0VZm32LytR-9VdbnVfjOQag9y37IDTkq8b0yQ1jJVpVWP_1Zi8_S7ISuO8ZD81DjF_1Y9d8aLJZPI_OREfdqS2FXGdmWf131gpy-Cu7z9H_-mBrDYxmOtOCmkWa9f5BbsZCZSWSNN7kjIoYf5tTWEMHTJeNk4hn6Sym8kNmAi4PVpRct0VR8zyNZJd4xOGmvjFqz7WLhPMNyDci0tmASpenRYza8tfoaAzeE38MFHKyXU9V4zGDzGDr-fkizZ0Rm44ifX1RPIjT68lV2R5bK2Bv0r3xer95v69EOaLPl3i6dY9W3NoNb97pHuszIHsbAo-YDsFAVIyhCHV1ThKhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
پرتغال
🆚
نروژ
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۸ گل زده
نروژ: ۳ برد، ۲ شکست و ۹ کل زده
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/72352" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مدارس ریاض به دستور مقامات سعودی و بدون اعلام دلیل رسمی، به مدت یک هفته به آموزش از راه دور روی آورده‌اند.
این تصمیم یک روز پس از آن اتخاذ شد که پدافند هوایی عربستان دو پهپاد حوثی را که ریاض را هدف قرار داده بودند، رهگیری و منهدم کرد؛ اقدامی که در بحبوحه تشدید حملات حوثی‌ها به این پادشاهی صورت گرفت.
در دو پیام جداگانه که خبرگزاری فرانسه (AFP) آن‌ها را مشاهده کرده، آمده است: «به‌تازگی از سوی مقامات سعودی مطلع شدیم که مدارس باید در تمام طول هفته تعطیل بمانند.»
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72351" target="_blank">📅 11:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72348">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZrtOzKYm_4K7WQq62q51cFnoJLNt5DS074Dl56AkjF9JWjxDfAUSFvDoP9b56N9dsPgolnr0_ZG_A5McrEMssk1KXdsSXRGk5ab3lpulnS0CmtPwE3xhKSo_VKd0udgfp63gL1Uymxv4m7FiD222EKE_ih5QYfD15pCO6yctJTWYpJzA_-M9p2R3Dtcy369V9XDFI4pbB2TN6wu0F7UFZorDAQDZgeFAj4KFpoVCYX93g9C-zb7JHCUM8_5Ywp5VO1lbol7ZbnxbZ7mCs8lZIIWXJSUlgmZoF8xGmHXkqHGwVLqzTm73Zeq3__d1Xu2i5Pm29UeH18k-1fqitcO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGSFprswkExyMNB-6HDws1EYiBrFQ_76nTiUHzvzbRUuHU2ByRMpqN4nQDdsduc5e_YdXvNLdJ0Dok7RRRINXoVxqb0qIpt3VEHv8ccgf8viH3EliC6Lh3oBgWtIPdKXNOHETo46IHYZFGJ7gtRvDG_X7wD9sV_RYp7VetLXk5tCf1vwzCMvR5YVey5hTHKelJlc1OCuJG9uP83BtDO6v0ePkgYrOfe4f1dFp8IZ1vAp9GBYE9IekC72cSfazLxK8SMcWxSt_R412JzZ9fLfi5JxsjBbEd5fPmbNsnxb_U3yrbMcwU-BJhBrdWWoRW5CLY_BKCHkA__uAHEn7ndo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rILzzjUkYxdodvTn0-dSJ0IsbOnFSiqQRRiLAC91U7WcWqA36sPiggIzkrXiLufLBBq_8RDSIjfqTs0T4LNeaSIjT4__ew1E6i0FSQY_QVh879mWYy0fqwauw4nr0Ox0v09S-DJ_AP5oMnp-a21dleHQmLlQ46xInmbjZ5x9mt7e_lYi9GyP-KAO5PJmIpCCOnS-cUifOP6Ic7hURDNitcCWKBh4IDz-NFFKfcVuRpAZcLIvUDM-1ToA5N8KenbKv8B2smxlaRN6aazVE6i6AMPPwhnHWh2X2cCJgPRa5sfxI6kklp6mF3BHGyeVnR8Bu309tIgeQ6MzrVElY3csOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رژیم جمهوری اسلامی که خودش فرودگاه نجف را ساخته بود و هزینه‌ی آن را تقبل کرده بود، از استفاده از این فرودگاه محروم شد!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72348" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72347">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=nCuRLGRKlQ5OFkA2ayNaEw9VBak4qoB5cJvafw8y5JU-tJoxqfO3Yx8kt-9x7K3DjuPqe5g4C_IZSMUa8Q0uwXfHuWdhyZOgVg8P-4wOWEYHP7_WaCLEq0cFf-gqm2W1Joo3uuoy7SpMcvv9Jvduq8NA_LKlXgUd3VLcC1E3KRO5-2AZa55WQ1CUfu87N9wG5bElSmJGVmnUGm43atLf7WyzW8YUvB7iY3511rGffolIJJQM4l37GiQeHXjjOvFfKLHHCEBYjVy4M8xTt3kP9IyHvc8kj57QH-BTMqddlgrpFMw9EWVf_PetR8FuX1sHTq1mHy3SclQAgZP9iCTCTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=nCuRLGRKlQ5OFkA2ayNaEw9VBak4qoB5cJvafw8y5JU-tJoxqfO3Yx8kt-9x7K3DjuPqe5g4C_IZSMUa8Q0uwXfHuWdhyZOgVg8P-4wOWEYHP7_WaCLEq0cFf-gqm2W1Joo3uuoy7SpMcvv9Jvduq8NA_LKlXgUd3VLcC1E3KRO5-2AZa55WQ1CUfu87N9wG5bElSmJGVmnUGm43atLf7WyzW8YUvB7iY3511rGffolIJJQM4l37GiQeHXjjOvFfKLHHCEBYjVy4M8xTt3kP9IyHvc8kj57QH-BTMqddlgrpFMw9EWVf_PetR8FuX1sHTq1mHy3SclQAgZP9iCTCTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌سخنگوی ارشد نیروهای مسلح ج ا :
آمریکایی‌ها باید خواب این را ببینند که در مدیریت تنگهٔ هرمز دخالت کنند و در صورت دخالت سیلی از نیروهای مسلح ایران خواهند خورد؛ آن‌ها باید از منطقهٔ ما بروند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72347" target="_blank">📅 11:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72346">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=TFAQ5-qjul784a7IK3utRH2ie51u6m6giZGDF0j8XbrNgoh1pPz2xgZdkqb3q-aSqrGuMgnmW6b37MtyULVTHrk8Nov-nMX1rz_RSLPJl9Q-Svaer6BxY5JRh7WT399-nbSZEPivAc7sg8qVjJVcdFLI5irWJJSnoScdK9e8NlSEdN7hyuKa9foMQ9220EuRzpOWKh5DPIx3IaP5lnOxuo4WDT3lv1JuI8cpZiUxIzp69-YaBzMOHezHlaYPbZNwSSWAjY2_SKa_yY6FeyPfprio1_0_ySdAlQpHyIbSwvJBzy5jm-6pqfFIcdYVoMHC_OlL6fAZtj7Nf7kjol-nWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=TFAQ5-qjul784a7IK3utRH2ie51u6m6giZGDF0j8XbrNgoh1pPz2xgZdkqb3q-aSqrGuMgnmW6b37MtyULVTHrk8Nov-nMX1rz_RSLPJl9Q-Svaer6BxY5JRh7WT399-nbSZEPivAc7sg8qVjJVcdFLI5irWJJSnoScdK9e8NlSEdN7hyuKa9foMQ9220EuRzpOWKh5DPIx3IaP5lnOxuo4WDT3lv1JuI8cpZiUxIzp69-YaBzMOHezHlaYPbZNwSSWAjY2_SKa_yY6FeyPfprio1_0_ySdAlQpHyIbSwvJBzy5jm-6pqfFIcdYVoMHC_OlL6fAZtj7Nf7kjol-nWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای ایشون در مورد مظلومیت پسرا، بیشترین لایک ۲۴ ساعت اخیر رو داشته:
پسرا از یه جایی به بعد، از بس کار دارن و به فکر آینده‌ان، حتی یادشون نمیاد که کِی تولدشونه!
ولی همینکه یکی باشه و بهشون بگه تو چقدر برام مهم و با ارزشی، اندازه هزاران کادوی میلیاردی براشون ارزش داره!
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72346" target="_blank">📅 10:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72345">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2CGP0CT_ZgnJAuY68Bf6DpfJLDFyr0Hlq63FAlV8Y9YqCZXaTy313PZdOx3v7JDZurjaPi-vVqMUS3bLv22arBDOMFLxhFC3yj1l3EBAHMMH4FbJ9qFTUnKF1DdWa5n9m8GVHRqyugwZQF43m5hl_dZBy8kgWxzAkjTeEad6blQjdZsxHg3ec8m6hzQEZpap5VA0bnGbRolYX1yKCzRaW3T5yp3XkEHC36at0YHauQNmTgeCn_anfk40AGs6ho14Je_2vAH-xvnTeQqspgVNatE-pZUBgMeFJ4PPwZZxH_wtrNRvGRmzv9KVRps9o6INZM3lBnl6vtOGqrNmpMIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارشد نیروهای مسلح جمهوری اسلامی :
قدرتمندترین ارتش جهان مقابل نیروهای مسلح ایران زانو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72345" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72344">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=jJEn12rOqdLjNUceTRz7sJMA9tFQ5fs8C2AjvzMkIMPA-ix7tN5JgkgbBj20dtI5Z2rivoPtMyWnuU1kTaF3HCLDWf832O03fNYDBT_ygzapo35oKR1Y0S1-YO-Ngqll4OGzncIVUQLNx0BdPwkMdpWpaAUIaTQXSU7iiIMHLcjbE4LYQ-zAZzfknaVxhWBdB7bPDIRRMwq4_0GD0tbaTinBk3MQUwSi6fxdLvyEKT2z7HvWXUSuqjevT1XTtyP_Y31gTLC5M9LpF97eeOYanOdy-YLa04owf7exOPCGyB9bGM_PYocFJDrqUtjTHhce_FBrsQfGJM1lunaniF6ezA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=jJEn12rOqdLjNUceTRz7sJMA9tFQ5fs8C2AjvzMkIMPA-ix7tN5JgkgbBj20dtI5Z2rivoPtMyWnuU1kTaF3HCLDWf832O03fNYDBT_ygzapo35oKR1Y0S1-YO-Ngqll4OGzncIVUQLNx0BdPwkMdpWpaAUIaTQXSU7iiIMHLcjbE4LYQ-zAZzfknaVxhWBdB7bPDIRRMwq4_0GD0tbaTinBk3MQUwSi6fxdLvyEKT2z7HvWXUSuqjevT1XTtyP_Y31gTLC5M9LpF97eeOYanOdy-YLa04owf7exOPCGyB9bGM_PYocFJDrqUtjTHhce_FBrsQfGJM1lunaniF6ezA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آقای سفیر، پیام دولت آمریکا به مردم ایران چیه؟؟
سفیر آمریکا در سازمان ملل: این رژیم تروریستی باید بره راهی دیگه نیست
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72344" target="_blank">📅 09:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72343">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjjRho10B0MqJnfCEJwI9LaxBK4_7jiEWhx9hNjw2Uk80gFHNzZHq-somvoQubUtF7m58LsKmhTJcfq1m6bAUPVaMXGT88JptMwMF7H9tIVgP7gTlQRouLTEsIcFgx8-gYSbMqmTZG79MXN7MCy0epf-qBAQFcNXsbXswLEC0nvph5JDFkOCH41ZEnJheUe2cqg1mfN4Vu7euoHcQkqLl247RP-1FG_JqVFT4x2bio_rqtRd-pTSZcw6eu0F8qqSsi8rTBto7ocSKOGnBN2X37tG9_stlEW3RR6w84tpCB6IMjKQ1WGsK7mi46v6zwpsmM1vAMFvxewho87SDnekMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال‌استریت ژورنال، دولت ترامپ فشار اقتصادی خود را بر ایران افزایش داده و از کشورها در سراسر خاورمیانه و اروپا می‌خواهد تا روابط هوایی و بانکی خود را با تهران قطع کنند.
جاناتان برک، مسئول ارشد وزارت خزانه‌داری آمریکا، این ماه از چندین کشور بازدید کرد و به شرکای تجاری ایران هشدار داد که باید بین انجام تجارت با تهران یا واشنگتن یکی را انتخاب کنند.
در پی این کمپین دیپلماتیک، عمان، امارات متحده عربی و ترکیه، پروازهای ایران را محدود کردند، در حالی که مقامات امارات، تراکنش‌های مرتبط با ایران را توسط بانک ملی مسدود کردند و ترکیه، مجوز فعالیت بانک ملت را لغو کرد.
آذربایجان و گرجستان نیز پروازهای شرکت‌های هواپیمایی ایران را محدود کرده‌اند، در حالی که بریتانیا قصد دارد معافیت‌های بانکی را که به موسسات مالی ایران اجازه فعالیت در لندن را داده بود، لغو کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72343" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72342">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72342" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72342" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72341">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rj56Cw4WBmRUjaS7kYngHQHCHc-ezC2RnsdlsU3AxsMCgc40kGOjnAeNqFF5SjSfGYelIytQY-2EeCB-a5L_ts6KcWNQylABb6jjTebMF-9ifJQ7wtFcHlQPlNp0pXwBEaoY6FpjJn8AL6rkrXM2K3R1hcW3ccjzjAeznnerOAtFBsXtXzYVyP9b1dkEDl6Ie0VDF1IEbL9IC1ggI1HmM1t2yaqBRx_zwWvY7hob-hOMfLksUKe3MZt7s6SZ__80TZ5UpFsG47YDqY9EZpU_PrAEgMkIh3MWqxSBnwyf2iu8kALJzr8kyGcDuScYgB3rSYlRljn1G3Fj4HAz2cO00w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72341" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72340">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار های جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72340" target="_blank">📅 01:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72339">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سپاه پاسداران:توی جنگ بعدی ناوها و ناوشکن‌های دشمن حتی توی اقیانوس هند هم امنیت نداره و قطعا هدف قرارشون میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72339" target="_blank">📅 01:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72338">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72338" target="_blank">📅 00:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72336">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ایلیا هاشمی:
ساعت در محدوده ۰۰:۱۵ الی ۰۰:۴۰ بامداد یکشنبه، چندین انفجار مهیب همراه با لرزش در محدوده تنگه هرمز شنیده شد.
تحرکات نظامیِ سواحل جنوبی هرمزگان در کنار تعداد و شدت انفجارهای امشب، نسبت به دو ماهه اخیر بی‌سابقه است و می‌تواند گسترده‌تر شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72336" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72335">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شنیده شدن صدای چند انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72335" target="_blank">📅 00:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72334">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">عراقچی رفته نیویورک گفته اگه این هفت تا کارو بکنید تنگه رو باز می‌کنیم، اونام گفتن مرتیکه جاکش تنگه که دست خودمونه پس صیکتیر کن تا پیشنهاد بعدی
و این شد پایان این دوره از مذاکرات:
#hjAly‌</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72334" target="_blank">📅 00:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72333">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=iBP6Z7NohunVSfTHEwI0lQ1YdPpWO7-_2rCV-S40lW84MFSalr7bGwhzm-jiYMjeWXA9dRE7Cka2W48bAoI01UutBO0p_wTrC9ABJ9MlgvaZMvmJqT83h2gA9StoEJgNo53yHkR5ctVpRqo2xnpY88uYJQWSLS74vceP67wK1Lf5-SVcfBor4PFv72EBdpJ_I7maSn-Ol9YSgQBTiZdRt3mm2JSRgeQzJ_yEingFl4N2-1w0bWDfHQ8Wd_-OCBKRVQHPQjW0-91GhuV8nKSRkdcgodN1lAjcgtEmFteavCvNyP6GVPpSJfBpBXklab7pWtSeGc9b8LzGVCoTqA9hbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=iBP6Z7NohunVSfTHEwI0lQ1YdPpWO7-_2rCV-S40lW84MFSalr7bGwhzm-jiYMjeWXA9dRE7Cka2W48bAoI01UutBO0p_wTrC9ABJ9MlgvaZMvmJqT83h2gA9StoEJgNo53yHkR5ctVpRqo2xnpY88uYJQWSLS74vceP67wK1Lf5-SVcfBor4PFv72EBdpJ_I7maSn-Ol9YSgQBTiZdRt3mm2JSRgeQzJ_yEingFl4N2-1w0bWDfHQ8Wd_-OCBKRVQHPQjW0-91GhuV8nKSRkdcgodN1lAjcgtEmFteavCvNyP6GVPpSJfBpBXklab7pWtSeGc9b8LzGVCoTqA9hbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پریشب تو تهرانپارس، یه خانواده برای مریض بدحالشون با 115 تماس گرفتن تا آمبولانس بیاد و ببرتش بیمارستان؛
ولی از اونجایی که خودِ آمبولانس خراب شد، همراه‌هایِ مریض مجبور شدن تا نزدیکی‌های بیمارستان هُلش بدن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72333" target="_blank">📅 23:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72332">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=ubXIUUCubIvv5jpHDyoMBIQwbLDMgVpFLFZ42_rKRRNnYF9bYF2HDPrIuIeTH7iH2BX5Air12H2AlHM0E4tnJNd6gUVvzad5NbJ_F6dXnVbSpA-rSbXmov0TIE5YFbD_kqih3kZ4PM-j0FNgeApXFIGMs_a16ymkjouVppKBye5JF1KdsLFUVHL556JZidWUEVxya_hbekbEdjaZZvHoYmlmG4tzIUEfIJ4_WnPjdnjgznmUkA6QbQEAPmPADwyAbzE7Vt5Po6w8uugeAMFbP5WUjOn0i9K2tSrNUV_G_3ZReDdIR0W--xOIvLgVWv2mS157aQweDE5c3M_tBDIsbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=ubXIUUCubIvv5jpHDyoMBIQwbLDMgVpFLFZ42_rKRRNnYF9bYF2HDPrIuIeTH7iH2BX5Air12H2AlHM0E4tnJNd6gUVvzad5NbJ_F6dXnVbSpA-rSbXmov0TIE5YFbD_kqih3kZ4PM-j0FNgeApXFIGMs_a16ymkjouVppKBye5JF1KdsLFUVHL556JZidWUEVxya_hbekbEdjaZZvHoYmlmG4tzIUEfIJ4_WnPjdnjgznmUkA6QbQEAPmPADwyAbzE7Vt5Po6w8uugeAMFbP5WUjOn0i9K2tSrNUV_G_3ZReDdIR0W--xOIvLgVWv2mS157aQweDE5c3M_tBDIsbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز داخل تهران اولین مرکز آموزش نظامی برای جان‌فداها افتتاح شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72332" target="_blank">📅 22:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72331">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=X6doSJD68pslBZnJjRTARlCCeuVNMPW7C7mVYpeLAY52nhKymepLPzj0BP0ET0EPSBTBmph0ZbwHyCVP_K1a6PFXYsw5YJDgbxfFRWIR_2l_LNyLTiuOLHz-Xvmofkg2Yj-OreZaJwhpszUmaNUkTJbe7oaLh6hqX6GU5ytlggCSETtqko1KyLw9Ktw2J5CXw9mYKQmPyk2Wl9jIEjka5sL3oCt_GoLTIYMPdMavv-yGcP1hwNQ1Fnw3eh5RLHYYThP8v57DNmrTK-LSatZE-j4owRxPKp3bQ8lPpWIOe21xyfPkJTUz_6H0kZ8diET08I9Wz_r7bKiHlcnSqU7rgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=X6doSJD68pslBZnJjRTARlCCeuVNMPW7C7mVYpeLAY52nhKymepLPzj0BP0ET0EPSBTBmph0ZbwHyCVP_K1a6PFXYsw5YJDgbxfFRWIR_2l_LNyLTiuOLHz-Xvmofkg2Yj-OreZaJwhpszUmaNUkTJbe7oaLh6hqX6GU5ytlggCSETtqko1KyLw9Ktw2J5CXw9mYKQmPyk2Wl9jIEjka5sL3oCt_GoLTIYMPdMavv-yGcP1hwNQ1Fnw3eh5RLHYYThP8v57DNmrTK-LSatZE-j4owRxPKp3bQ8lPpWIOe21xyfPkJTUz_6H0kZ8diET08I9Wz_r7bKiHlcnSqU7rgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرازیر شدن موج جدید افغان ها از کوه‌های صعب‌العبور به سوی خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72331" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72328">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWrqRm4-b7rZgNNrC1d_TkSQagMJJ6XLxvHM7oVrzy8If9GD8LhcjLtn9g1YdKSZQoQ0fnTy-71bf6-9y3UjRwU0BaTb7bhd_IUuuQWWjQstWMZ50ozAjaw5jnjrPP1sJXfvEQz9BlKpGOhgD_9GYQ0VPWtpP_GmgzsttSfRVPXOzJe_dvL_2tsqSEHS8tjEVAKqlTTSPhntFTz6kIB5bGSodXCHO16FyjahXl-EkJ3S5_HpqQKj4iOVfyekkx5eeQ-VK54ef2q_UjeJNY3lRBTqWFSD4rmEiF03I-bQSVlVUJTNiwNzVbp636feBTOxCnK3W4gvzwFxl3BiYu59oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=UQ0vJzfNPWhoZuZdvgxfEXiSomTTXOg2meYDSTRiPb6s9m11sYLoE7OykN24qFlPmjMCoXz1RV354YQCi8L7N3xJhhPwiJ5jMUR54Q2qJG8fSppLN3OrCH9U0frq9GwR37dK3RYq755waMhLkvnii1z6nE4T7FkgVgYQkR6WFGMiBAsb-7kEmlgh8eGHxXG4dUicNsElXqZ8nrMGTRvg9yJbV_3tRHopEMmdRopz_LK-E-0hrJ-tc9Lb-ehcHasiOCgzI3xL6xbTdigaI0aNiG5CqXV36BnFQBkNtLy0kPWsqZ8YpRkWbVysaViydhLV6mN1IamsLcdl-jjn3EtBCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=UQ0vJzfNPWhoZuZdvgxfEXiSomTTXOg2meYDSTRiPb6s9m11sYLoE7OykN24qFlPmjMCoXz1RV354YQCi8L7N3xJhhPwiJ5jMUR54Q2qJG8fSppLN3OrCH9U0frq9GwR37dK3RYq755waMhLkvnii1z6nE4T7FkgVgYQkR6WFGMiBAsb-7kEmlgh8eGHxXG4dUicNsElXqZ8nrMGTRvg9yJbV_3tRHopEMmdRopz_LK-E-0hrJ-tc9Lb-ehcHasiOCgzI3xL6xbTdigaI0aNiG5CqXV36BnFQBkNtLy0kPWsqZ8YpRkWbVysaViydhLV6mN1IamsLcdl-jjn3EtBCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله یه مدت به خونه صمیمی‌ترین دوستش که مامان باباش طلاق گرفته بودن، رفت و آمد داشته.
بعد از یه مدت، دختره رو بابای دوستش که ۴۷ سالش بوده کراش میزنه و مخِ بابای صمیمی‌ترین دوستشو میزنه تا باهم ازدواج کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72328" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72327">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=DwHM7C2l0F8dcamNTPVdb6M67rLDHUlOMAh4eOZjtShQE4-HTQimBKC6tWVXthElZKR6CPI6WPgOAY3ckv3ruHynkBik2OJVPgVsLxa9J8n6poc5w2NKlx4X--3wLIObeHpiuaa2NAs_1wmDEL-RJq4qcu9F-m3yn6HLXeZU3NxUw-3AonQJEG6DRCMUQGyulg5OwY42DNBpAwfh-B_zol9Wo4VjCHo-9pxIf307g6JVfJTDuRlvYp3p6CxdRrVAOj-6DHuKQgtVJPpAdf_bZ0lp9pmS7n12oBzD1ajWL7HQTWch5_OOwJ0vRQs-6-Az54VexGvPYE6RM1CXyf6hgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=DwHM7C2l0F8dcamNTPVdb6M67rLDHUlOMAh4eOZjtShQE4-HTQimBKC6tWVXthElZKR6CPI6WPgOAY3ckv3ruHynkBik2OJVPgVsLxa9J8n6poc5w2NKlx4X--3wLIObeHpiuaa2NAs_1wmDEL-RJq4qcu9F-m3yn6HLXeZU3NxUw-3AonQJEG6DRCMUQGyulg5OwY42DNBpAwfh-B_zol9Wo4VjCHo-9pxIf307g6JVfJTDuRlvYp3p6CxdRrVAOj-6DHuKQgtVJPpAdf_bZ0lp9pmS7n12oBzD1ajWL7HQTWch5_OOwJ0vRQs-6-Az54VexGvPYE6RM1CXyf6hgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه مینی رپر کوچولو و زیبا
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72327" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72326">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72326" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72325">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIkhSQ7uQVAGNQLH92H_i1wlp7DT3iCLlkWIKrrmBqebMyJqYweJVekW07r99aQWD3qAGrCkZO77YE_80d4YwsvlpBRzkJZZqX20HmrkwOlRiRwVU6qd4EMY5jNq9neU7_g0PEe2hhzSy2nSrQqqaZgjD0ZsIaVUP2aqv3S_7Zj7MMAs82hk1zFC5WKn77RhMIwvz7FNlyhHH_vjyqQa0bWYVyxv7vzvuJ2Oq0XrEZIofhagx-9naiAbtTaYEHVtK6BtnuzN4MfxJS9ajLuMqTQS6cMxn5_y7eJ27OCtNIXOZAsebMnWLG4CLVnP6Dorcm6zWX7My73GgFaS2OV8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر!
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورود به کانال اصلی (آنالیزها و فرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه (چت و تبادل نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72325" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72324">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">طبق گزارش های تایید نشده، عباس عراقچی بازگشتش به ایران تاخیر افتاده و قراره سه‌شنبه ۷ مهر ۱۴۰۵ (۲۹ سپتامبر ۲۰۲۶) از نیویورک به تهران برگرده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72324" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72323">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9470296462.mp4?token=hIEF-9kjoJY6vwqLOpI3jgfiuGKgsvX4Mv5EHdnlLoKVT4yrltJsBHzHDOu1vlvx-QiSMJddrB9olJqroUEtmCPbgiJBOE00IPt3juCetOaja4Q0WTR5brjeNq39frCCyxNs-wADDP2_HCmIDzgs-cXUN3aeeMn_nn_WENUvXPCoaX0UrhwQ18bhP4bO3OW_vM9TVgjSIWb1r2DhayclpSlqf0V4_gkOoSvlnGRG9EBNpQKpH08BamrI-eZzM7qy5guvJB4UkdQZlfANwtkVKAFfftaMTxFMBJPyHkZB7n0tzzoofJwXDoqP1L4aSMgt76dFZdxJr7QVT8kp1fQESQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9470296462.mp4?token=hIEF-9kjoJY6vwqLOpI3jgfiuGKgsvX4Mv5EHdnlLoKVT4yrltJsBHzHDOu1vlvx-QiSMJddrB9olJqroUEtmCPbgiJBOE00IPt3juCetOaja4Q0WTR5brjeNq39frCCyxNs-wADDP2_HCmIDzgs-cXUN3aeeMn_nn_WENUvXPCoaX0UrhwQ18bhP4bO3OW_vM9TVgjSIWb1r2DhayclpSlqf0V4_gkOoSvlnGRG9EBNpQKpH08BamrI-eZzM7qy5guvJB4UkdQZlfANwtkVKAFfftaMTxFMBJPyHkZB7n0tzzoofJwXDoqP1L4aSMgt76dFZdxJr7QVT8kp1fQESQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع عده‌ای در فرودگاه مهرآباد و شعار علیه پزشکیان و عراقچی
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72323" target="_blank">📅 20:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72322">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=gsZVspe5EndsxTpJrI8-i55S4Zzz19_iMRoGs7WDCCkfP5xJ4nuCMooWIKGdGBGNLYR8Bbw7uE5kArscbv59Job1_GGWTO-PLjN7eryufY7xtYZLAkWnyLw_9fANdRfYvsjwp5kibQaRwDhUXRMXpRsYDcgB0PS5oKTdAr3LMryej38y0l_ubY3SkYfshUYjxlpPKG7jvD00DQDCe04fVjDQheg-b6B0IA-a3SLB_3cTCrXHk-VdARwbftQRtD_ZX-hdzK1oUZ7Vaf3b9Ms9BA4gxQVZVFI0JwJ1o_rsuafgjkrfD7zpUleynl1YrKnxCbcUGBTVkx6IjhxWTBvR2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=gsZVspe5EndsxTpJrI8-i55S4Zzz19_iMRoGs7WDCCkfP5xJ4nuCMooWIKGdGBGNLYR8Bbw7uE5kArscbv59Job1_GGWTO-PLjN7eryufY7xtYZLAkWnyLw_9fANdRfYvsjwp5kibQaRwDhUXRMXpRsYDcgB0PS5oKTdAr3LMryej38y0l_ubY3SkYfshUYjxlpPKG7jvD00DQDCe04fVjDQheg-b6B0IA-a3SLB_3cTCrXHk-VdARwbftQRtD_ZX-hdzK1oUZ7Vaf3b9Ms9BA4gxQVZVFI0JwJ1o_rsuafgjkrfD7zpUleynl1YrKnxCbcUGBTVkx6IjhxWTBvR2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از پاسخ دادن به سوال خبرنگار درباره زمان آغاز جنگ خودداری کرد.
خبرنگار:
آیا پس از انتخابات میان‌دوره‌ای به ایران حمله خواهید کرد؟
ترامپ:
من توافق آن‌ها را رد می‌کنم. آن‌ها می‌خواهند توافقی کنند که در آن بلافاصله تنگه را باز کنند، چون دارند به‌شدت متحمل شکست می‌شوند.
آن‌ها خواهان توافق هستند و به نظر من این اشکالی ندارد. من هم از توافق کردن استقبال می‌کنم، اما آن توافق [مدنظر آن‌ها] قابل‌قبول نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72322" target="_blank">📅 19:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72321">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1e0c-XkPse7477ILIgTQOwTA3NF6LKsbPXH8O7D3kcLkFIvGCHTNfgOUl1VeaHvnceqvzV1S449tqGj-PiAZXTjDQEUH1J5l_O0uI4PUCyacpu65LREyj4q-D1QwM5KzZScF4jBxRbEq0NGIysBhbZwFuWKC13N3tdqo1tfn5iMKh9bDdfjcYd09j0RQmbPV9GSwXmNuaxrCMzguWsv4nhfgScWIscmfZjSImtbMzfbUnRNgFgIqynHkpdCtdimPj5MrxFrkbe7BeYfFliIDeW5qzc0mbOXCJf4sntZfrxZ34HHYdzitnrf6aODqIloWVrv6fz_pantaD4yO0Ne8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای ترابری نظامی آمریکایی(C-40 Clipper) که بر پایه Boeing 737-700C ساخته شده و عمدتاً در اختیار نیروی دریایی آمریکا (US Navy) است در بحرین فرود آمد. مأموریت اصلی آن جابه‌جایی پرسنل و محموله‌های لجستیکی است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72321" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72320">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ما کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز عبور می‌کند؛ همین دیشب، ۲۹ کشتی از آنجا عبور کردند.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72320" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72319">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=mRdyusL5xwtgPK53CmkCFpB-PE7p-Wtm7npYQdJH_nYbIoFEQ4p5C0x7GBFEMRXm37qzx3Y6P_qE9vYbPptjpmJDQnv8vOF9li2eW5LDRW9aBbjQG6j9TgVRWpvNTzTvVBekZC942D6KwvhdEH_ytyw3pE2t1t_i_0LeWopTAuc-wpBx_eZRO9uFRX7XDF_agMOC_ShPgBWKPop9H_eiHI3dBDc3cWUlu7e1VWJGIy5KZ-isakyCXZS4OEpNlXGCMtewc2U_mozeumkdHGX99ncjjYCtUMe1Hm3lsUBm1nAArtkSNcGNi-ggRu0MSgLawh9X4ROjt9qat-Y9oXXl_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=mRdyusL5xwtgPK53CmkCFpB-PE7p-Wtm7npYQdJH_nYbIoFEQ4p5C0x7GBFEMRXm37qzx3Y6P_qE9vYbPptjpmJDQnv8vOF9li2eW5LDRW9aBbjQG6j9TgVRWpvNTzTvVBekZC942D6KwvhdEH_ytyw3pE2t1t_i_0LeWopTAuc-wpBx_eZRO9uFRX7XDF_agMOC_ShPgBWKPop9H_eiHI3dBDc3cWUlu7e1VWJGIy5KZ-isakyCXZS4OEpNlXGCMtewc2U_mozeumkdHGX99ncjjYCtUMe1Hm3lsUBm1nAArtkSNcGNi-ggRu0MSgLawh9X4ROjt9qat-Y9oXXl_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانوی گاثی که دریک براش هاپ هاپ کرد:
غذای مورد علاقه‌ام کباب کوبیده‌اس! بابای من ایرانیه و عاشق انواع کبابم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72319" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72318">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72318" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72318" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72317">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGloWVWGdSxmSgflBrKpShA5pOTuC-Xz9M0Y_UrMSCKa7Q1xGtGaXj18IpdYTUkiJUttzmU8BJQ1woowb-7auLBg5b0njGtEmYtpDVX4CNXGTXnbHtZ4mqHgfNJSAEBO3SNDhI6EbGI-MsI6iHGV_j4eOAbLprg5yCOLDWrulxjsin5wtBaRE0dkzCgr9sSt-Ls9fHWeB_zkRmD40qLEgDaTPZYMXt7X-0_J6NG4xDYOB41ND-Q8CKFaKVIzeevzziUavMeRruxly_eSY3ubt4UaILR-sMjMxW7yzFYRa8cjr83uninykWKPtjPhZ1LYlJ-yT97QTgxDbXSl43doxA.jpg" alt="photo" loading="lazy"/></div>
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
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72317" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72316">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=b2qWJ2u7s5EblVvQbQk1WhtUkJOSGbp6t5s7AXEglGXQZkbxrbPRM4af-Pdi_SDYPJ-uhkYFGl8em5ZKd-S6YBf2xSVoRojFllZWFHyVWQM9n9LrsCy4EQkjekSgByNk9exwuBPive5HJYAIHlKcMdsSzUjdzDDOrQrB54gs9XklVrLUazWg2XCu1uIvXByAR4EaLxK6olr_MXviJBcMCw46niu-xstTcro31gJa3_o_06WUQQ92yOHz5uqnxozz4a6G5pmHFfKsjCNO_f9KswOZ_Vog9WQYt0vWYlWF9cX_i6RwrQoKvpz4PEcQundjK8OQP-T1vDMN0jBKaxY3mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=b2qWJ2u7s5EblVvQbQk1WhtUkJOSGbp6t5s7AXEglGXQZkbxrbPRM4af-Pdi_SDYPJ-uhkYFGl8em5ZKd-S6YBf2xSVoRojFllZWFHyVWQM9n9LrsCy4EQkjekSgByNk9exwuBPive5HJYAIHlKcMdsSzUjdzDDOrQrB54gs9XklVrLUazWg2XCu1uIvXByAR4EaLxK6olr_MXviJBcMCw46niu-xstTcro31gJa3_o_06WUQQ92yOHz5uqnxozz4a6G5pmHFfKsjCNO_f9KswOZ_Vog9WQYt0vWYlWF9cX_i6RwrQoKvpz4PEcQundjK8OQP-T1vDMN0jBKaxY3mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
بعید میدونم مجتبی خامنه‌ای بیاد بیرون؛ بنظرم مجتبی خامنه‌ای تنها رهبریه که توی تونل رهبر شده،
توی تونل رهبریشو طی میکنه
و توی تونل رهبریش به پایان میرسه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72316" target="_blank">📅 18:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72315">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9475808af6.mp4?token=Kit50sOn8RK9Wqba1hFWLtuk_KZ2wMFou3rqvWPNeeTqPrE9k1V3yfTAYaf_hio6Dw0801kHFobNoIYJktg7H2Vf6p4BkROmHtDZ9ou6NWTQtefx3rS5i7qpZox_ue6Yn5nRLK6VomKJZW2MPoodlAXawvQMF-XZjOf4HefeALClBqzTn-TAoFzATMn2qjo9AtMU8tTwW_t6FpIsLONCnpTkhVbMCSAYgqKPIp-cPwUqUDsXiCl0-2y9iMA_00VTml2Xx5CfwcoIOA7lWSpiRgOu4c6EWJ44V08R-F8cWaLcl8UsPtmpV-TVH2ipHow4o0kMgoQy7BElle-u1fjjcKkMvIM1Oq1ZnGCaaOKLeKYSLGRXX2oTo1yn23fOINhnEbloNZyHIiGh42ouFs6skDlMzTc1Q2qP--76_pHlFB7OVaSOJ8scp72d-knHNzTAaV4k3BCa_Y5I4oI_vcemsiDYmzTg91KCtGFPaXDl7UG2nKuWew1bLFwgy82yKXrHUdBLwXSEnphLHB8CYQLQS6YzImFIhb9ff0XJYIqT-Coh4J4DDl58BWkr3E1rRUlPqm498vvVpcht9-8VqRH4E8ydQ1paMjGa3bA6mY0-JgpsS7m3sDAZsGCd9rBHbFOa_S0SXv3FyRpZjTPr89ffms8G7mik7IoWVVwTDE69V8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9475808af6.mp4?token=Kit50sOn8RK9Wqba1hFWLtuk_KZ2wMFou3rqvWPNeeTqPrE9k1V3yfTAYaf_hio6Dw0801kHFobNoIYJktg7H2Vf6p4BkROmHtDZ9ou6NWTQtefx3rS5i7qpZox_ue6Yn5nRLK6VomKJZW2MPoodlAXawvQMF-XZjOf4HefeALClBqzTn-TAoFzATMn2qjo9AtMU8tTwW_t6FpIsLONCnpTkhVbMCSAYgqKPIp-cPwUqUDsXiCl0-2y9iMA_00VTml2Xx5CfwcoIOA7lWSpiRgOu4c6EWJ44V08R-F8cWaLcl8UsPtmpV-TVH2ipHow4o0kMgoQy7BElle-u1fjjcKkMvIM1Oq1ZnGCaaOKLeKYSLGRXX2oTo1yn23fOINhnEbloNZyHIiGh42ouFs6skDlMzTc1Q2qP--76_pHlFB7OVaSOJ8scp72d-knHNzTAaV4k3BCa_Y5I4oI_vcemsiDYmzTg91KCtGFPaXDl7UG2nKuWew1bLFwgy82yKXrHUdBLwXSEnphLHB8CYQLQS6YzImFIhb9ff0XJYIqT-Coh4J4DDl58BWkr3E1rRUlPqm498vvVpcht9-8VqRH4E8ydQ1paMjGa3bA6mY0-JgpsS7m3sDAZsGCd9rBHbFOa_S0SXv3FyRpZjTPr89ffms8G7mik7IoWVVwTDE69V8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
کاری که آن‌ها می‌خواهند انجام دهند، باز کردن فوری تنگه هرمز است. می‌دانید چرا؟ چون دارند از پا درمی‌آیند. می‌دانید چرا دارند از پا درمی‌آیند؟ چون هیچ پولی عایدشان نمی‌شود.
آن‌ها درآمدشان را از طریق تنگه هرمز به دست می‌آورند؛ بنابراین با این کار، عملاً علیه منافع خودشان عمل کردند.
آن‌ها گفتند: «بیایید تنگه را ببندیم و برای دنیا مشکل ایجاد کنیم.» اما من وارد عمل شدم و ما بزرگ‌ترین محاصره تاریخ نظامی را برقرار کردیم؛ یک دیوار فولادی.
و حالا چه شده؟ آن‌ها دیگر پولی ندارند، چون می‌خواستند تنگه را ببندند.
و من گفتم: «بسیار خب. ما آن را به روی شما می‌بندیم، اما بقیه می‌توانند از آن استفاده کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72315" target="_blank">📅 17:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72314">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6488dcc10a.mp4?token=JpHYJS_cm0Bu4uLbi9Xb5wWm2U929-fwfkTnBMf2H9jpAyvUSCkleWh61vVg0M5JouDxTqHEBvdeQKPM0LpVFVGrMdGUPiNDcpXAW3r97Q-ySDoZ42I7xn-Krf7sjLjq6PDGSuA-i9wpFa9xnrm2gfwCtc5d3urnKSusilTOQB9Fl8dXEp3E-0zPOl-IEtYj7WR_X8RSRzqudAsJ2JgsVjBH9KF-orZ2G8hh5hWPNqOKq4m48uUQ_We8KE7cv_yGfxLxTVmCjU-w6LDIvFajklKf1s6-ntel3rI_DXa8GiaGnzkCAGBQT9AI4zRXZ5O90E6l3G9Z3fIWTIXEQ8w2ji0MhQZdJB-uz_UkShBeTZoVbtjfzU0oQXUf1iWZ6ZlZEXbi2OxVrc5_5FPM4WLJRwJehWGxYKXoBb3v9yY-ExdWZmUXCJmpYgSrwkjvlrRZljg-2eFLgNMCpFDSKH3rnX1q-Wj2RZq_HTxRJK_CeC1kI-LaQjfbYp6tG8SZYs40AD3_BZ4xJxGYb3rFc0YSwCJhcjDharCFJm9ZMPzFe7Om_Uea6IL82qy9YNUWHShg-rNHMiDONcNQV-Ff0kVf4nDkBI81SwoUOpQKNxqTphhepC26pL-CiqyAWm97HdDgvsZGk9qwU9RjplrdT8vPqBqnCa-O1PLgdaq3ahYeS6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6488dcc10a.mp4?token=JpHYJS_cm0Bu4uLbi9Xb5wWm2U929-fwfkTnBMf2H9jpAyvUSCkleWh61vVg0M5JouDxTqHEBvdeQKPM0LpVFVGrMdGUPiNDcpXAW3r97Q-ySDoZ42I7xn-Krf7sjLjq6PDGSuA-i9wpFa9xnrm2gfwCtc5d3urnKSusilTOQB9Fl8dXEp3E-0zPOl-IEtYj7WR_X8RSRzqudAsJ2JgsVjBH9KF-orZ2G8hh5hWPNqOKq4m48uUQ_We8KE7cv_yGfxLxTVmCjU-w6LDIvFajklKf1s6-ntel3rI_DXa8GiaGnzkCAGBQT9AI4zRXZ5O90E6l3G9Z3fIWTIXEQ8w2ji0MhQZdJB-uz_UkShBeTZoVbtjfzU0oQXUf1iWZ6ZlZEXbi2OxVrc5_5FPM4WLJRwJehWGxYKXoBb3v9yY-ExdWZmUXCJmpYgSrwkjvlrRZljg-2eFLgNMCpFDSKH3rnX1q-Wj2RZq_HTxRJK_CeC1kI-LaQjfbYp6tG8SZYs40AD3_BZ4xJxGYb3rFc0YSwCJhcjDharCFJm9ZMPzFe7Om_Uea6IL82qy9YNUWHShg-rNHMiDONcNQV-Ff0kVf4nDkBI81SwoUOpQKNxqTphhepC26pL-CiqyAWm97HdDgvsZGk9qwU9RjplrdT8vPqBqnCa-O1PLgdaq3ahYeS6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
من توافق آن‌ها را رد می‌کنم. آن‌ها می‌خواهند توافقی کنند که طی آن فوراً تنگه هرمز را باز کنند، چون دارند به‌شدت متحمل شکست می‌شوند.
می‌دانید، شما این موضوع را در «اخبار جعلی» نمی‌خوانید یا نمی‌بینید؛ اما ما داریم با قدرت تمام پیروز می‌شویم.
ما کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز عبور می‌کند؛ همین دیشب، ۲۹ کشتی از آنجا عبور کردند.
آن‌ها خواهان توافق هستند و به نظر من این اشکالی ندارد. من هم از توافق کردن استقبال می‌کنم، اما آن توافق [مدنظر آن‌ها] قابل‌قبول نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72314" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72313">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5297b02f7.mp4?token=HJPLuDwde0R__itbCnxK1DckdL3jrn9zaew7YsmGSPqcdhdS1XlS_0FsC1cDxODHgWKM0eRnds_p9YQ8Jm1J8GU5lNILVIAIQwtctTz67ypOsMX1egpVlFDTEvvb0HsfS7zHW9lm_7ktZJcFOzytqeV-oEW-qceyvrLYaa-6h-VZePerl6H9kMflsUx8Jvk1sTNrrmoMXP_sI3TLGh_P8PFm1xLlR46cKKWQsUrPxHxSjXFK6ASCsR8cBtapQ7gDy9eMwF0JV16D0i7f8elPDjvl4noxXFjrOq3By-_6vISFSL56AAc9fpsAP358Ize65kBZnJbO-ygMAfhW3pBozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5297b02f7.mp4?token=HJPLuDwde0R__itbCnxK1DckdL3jrn9zaew7YsmGSPqcdhdS1XlS_0FsC1cDxODHgWKM0eRnds_p9YQ8Jm1J8GU5lNILVIAIQwtctTz67ypOsMX1egpVlFDTEvvb0HsfS7zHW9lm_7ktZJcFOzytqeV-oEW-qceyvrLYaa-6h-VZePerl6H9kMflsUx8Jvk1sTNrrmoMXP_sI3TLGh_P8PFm1xLlR46cKKWQsUrPxHxSjXFK6ASCsR8cBtapQ7gDy9eMwF0JV16D0i7f8elPDjvl4noxXFjrOq3By-_6vISFSL56AAc9fpsAP358Ize65kBZnJbO-ygMAfhW3pBozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره طرح هفت ماده ای ارائه شده توسط ایران:
آن‌ها پیشنهادی ارائه کردند، اما من آن را رد کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72313" target="_blank">📅 17:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72312">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDlpGfEKIqyDCRJKU4cta6BtQwNPZACPICgoop0yQ9mYxcwcHhcXNxWm7vF3uIhOOjY6zzG1e39bQEEuwFdBqkCnXvEf-ZVxET4BMfDAWQ7YArwfTZ_1SCdKCaTTMTmBruq2h5KoZhMeyq0IP3pA1-AQq1pBI2r05zQ4vNxG89jBMoYOFcswwx-VkHP8TPncOZc3brMmJJgdk0AGNEariUGCWGqIU3ZN1owCtYGiPNyAMXWNeYI0aEVHe5Hlz827SxtwugHkYrHa6XMRHVpA5YnPhAZf6RX9cvBqVQFCDWJvwN3UociftbcfqFkr9v8UiNLxEmBDuuDckCvHrjIS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران نمی‌تواند سلاح هسته‌ای داشته باشد!!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72312" target="_blank">📅 17:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72311">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b70e110ec.mp4?token=MJ-3-OicH5WIB_ehEovHNxwvLR6ZP2NS4eqXXAgculBg4VjeVe_mn7L2b1Y4teYVt6296yyY3dHAIiB9ASDW5O-FYtLmHEgnnCaaE-ABWFhBK2HLqwbhrhtDpC4i61zZ3mE72PasTf0-NaL9fptrc4zDhIcCjWORpkX5_Y2wo6efyzb640vMANO4Obiqb6mI5cjWAjqv_60UJNvzoANrxkPOeTXITLI4DHlrlv80kF_GSB124HWommDTVOJaAFP-vXmeQykZqwmr-ebIW_LEEM7ynD2RxEQEcfsoyAeAj3a_LrxAEvY51y4SgeT-qY-boDzEJJjMr1e5AY_wJPKNCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b70e110ec.mp4?token=MJ-3-OicH5WIB_ehEovHNxwvLR6ZP2NS4eqXXAgculBg4VjeVe_mn7L2b1Y4teYVt6296yyY3dHAIiB9ASDW5O-FYtLmHEgnnCaaE-ABWFhBK2HLqwbhrhtDpC4i61zZ3mE72PasTf0-NaL9fptrc4zDhIcCjWORpkX5_Y2wo6efyzb640vMANO4Obiqb6mI5cjWAjqv_60UJNvzoANrxkPOeTXITLI4DHlrlv80kF_GSB124HWommDTVOJaAFP-vXmeQykZqwmr-ebIW_LEEM7ynD2RxEQEcfsoyAeAj3a_LrxAEvY51y4SgeT-qY-boDzEJJjMr1e5AY_wJPKNCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عرزشی داره فخر میفروشه نسبت به بنزین مفتی که میگیره در حالی که بقیه مردم ایران و دنیا باید گرون تر بخرن
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72311" target="_blank">📅 17:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72310">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204024e85e.mp4?token=ZBgH3EyIHCiHzSO5gWt_Zf8r55KN7IRomJdRBHGcy4n0rQ4vBEWzKr_t6wBkf3J4bfZMe4twi2CUp4hRBBSgMo8mxTDxBop0OOElB3_cIZcX3oI8EVBJaRSaPMlSy_mLouTa13vUqptX4nV5iQjf2QEbG3BqrQnsG-EYqecivTZOL7cEkSf2jWvx2-HwR4DCpf4oOBYSkhTjR0SzRoOV72BN7dio4qG67oe0iPROeO6IcAQg2bwu7zCQITDCfdMeI6E8j6aNIGaIDVykXGXSnuESdVSe3U9OHsiabIKFyO-C9ntYGLanO1N1qaWIuTqkPptmiO9cjceToX0ELFT-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204024e85e.mp4?token=ZBgH3EyIHCiHzSO5gWt_Zf8r55KN7IRomJdRBHGcy4n0rQ4vBEWzKr_t6wBkf3J4bfZMe4twi2CUp4hRBBSgMo8mxTDxBop0OOElB3_cIZcX3oI8EVBJaRSaPMlSy_mLouTa13vUqptX4nV5iQjf2QEbG3BqrQnsG-EYqecivTZOL7cEkSf2jWvx2-HwR4DCpf4oOBYSkhTjR0SzRoOV72BN7dio4qG67oe0iPROeO6IcAQg2bwu7zCQITDCfdMeI6E8j6aNIGaIDVykXGXSnuESdVSe3U9OHsiabIKFyO-C9ntYGLanO1N1qaWIuTqkPptmiO9cjceToX0ELFT-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه تعداد هم وطن به مناسبت شروع سال تحصیلی لوازم تحریر جدید گرفتن پخش کردن بین بچه های محلشون
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72310" target="_blank">📅 16:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72309">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11382bd536.mp4?token=pVRzbhb4y0DjQ83PYSrFyEmOSniGXWm-asvrXBoJQi3GbNN479-0t3Ik9SZYeQul2Pupd53AMsGeBekDbB8yRjr_pkg6b907I4sJoVVysO2P1ypCOjY4hoI5p60LWCIc6Jvcqj_5Bn7-Stbies6NTm2K6ed37yMRAHmHG0kuhMx44t0UH-F6BOTWiauXVI2ZxnoVAhBPvc-d4QIgo7577uEGzWey_itylj8QMPb-ny81cipU8JorV3pc4JZa4_ZHps00oAIikb8A2bPLa4LUA4GMzXzOWt_rl9mBVRjIj6ap9L3scLhRc7dNnWmPE1G5PAXZgO27HxPqX4XRjY8joFFl5rBG8cwx2ehgExVgTmJB6rTZDIx9GPg32pfqJcQJN9EvZdzt6lw2ecfCHb5n0biElKODq6iLs1aHP0oLaw1Jh_w29N2svTpCQeiO5EHfhFdRkW83JZu03-hb2zf4tD5ymDgvW_BrMUkHy9qNX1kthSbtIxmpj28_fNsaebtag0gZUIFDzgUDxOSc2WSKTE4SmIe6V_qdAdVZ_3IXDNXTHOG9TYQ4gV_f704ERtYSfisiDMDsaOC_adCk3nAwFOaw7wljATDpw5QPudOFA3BveyHkZbiJWLm2hdzfwxjLzJC9z2xbxc5If9fYw24J3xAV2XGZuRqUIyXPoEb_c60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11382bd536.mp4?token=pVRzbhb4y0DjQ83PYSrFyEmOSniGXWm-asvrXBoJQi3GbNN479-0t3Ik9SZYeQul2Pupd53AMsGeBekDbB8yRjr_pkg6b907I4sJoVVysO2P1ypCOjY4hoI5p60LWCIc6Jvcqj_5Bn7-Stbies6NTm2K6ed37yMRAHmHG0kuhMx44t0UH-F6BOTWiauXVI2ZxnoVAhBPvc-d4QIgo7577uEGzWey_itylj8QMPb-ny81cipU8JorV3pc4JZa4_ZHps00oAIikb8A2bPLa4LUA4GMzXzOWt_rl9mBVRjIj6ap9L3scLhRc7dNnWmPE1G5PAXZgO27HxPqX4XRjY8joFFl5rBG8cwx2ehgExVgTmJB6rTZDIx9GPg32pfqJcQJN9EvZdzt6lw2ecfCHb5n0biElKODq6iLs1aHP0oLaw1Jh_w29N2svTpCQeiO5EHfhFdRkW83JZu03-hb2zf4tD5ymDgvW_BrMUkHy9qNX1kthSbtIxmpj28_fNsaebtag0gZUIFDzgUDxOSc2WSKTE4SmIe6V_qdAdVZ_3IXDNXTHOG9TYQ4gV_f704ERtYSfisiDMDsaOC_adCk3nAwFOaw7wljATDpw5QPudOFA3BveyHkZbiJWLm2hdzfwxjLzJC9z2xbxc5If9fYw24J3xAV2XGZuRqUIyXPoEb_c60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقایسه ارزش برگ‌های اسکناس با یک برگ دستمال‌کاغذیِ دورانداختنی
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72309" target="_blank">📅 16:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72308">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=sYvtaRQQ6RnG7FphsGdMMyMPTo8rqdzi1rKcX2JVPcIB_105Em2pBxtWJPk6KKdHOdhtgcpyQuOw6FvNXk-GOUAcNG8V_ywFzQzuqWNdJEEu0z0rK9Es50LEnYyBSbhJ43DYqVyvu9dgceNqQwBJXjyNOyN-WQozkHDpZOqXJOKVzWDoeFO6g2hM28lJ3jDZErRWbwIPj_zGs9HyAZLhIYTnzkc-Y2L_KtI4ZoV0ivBdHXXCaiyVue3YaHk2lLnqkcDcJdOrPAjK-S6IohJL7hvx1f8TFF761HaOtC9mB47rGjmOfG6UpDhTfJTc1cPtaX5aYjLFLKR-a13mKjFRWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=sYvtaRQQ6RnG7FphsGdMMyMPTo8rqdzi1rKcX2JVPcIB_105Em2pBxtWJPk6KKdHOdhtgcpyQuOw6FvNXk-GOUAcNG8V_ywFzQzuqWNdJEEu0z0rK9Es50LEnYyBSbhJ43DYqVyvu9dgceNqQwBJXjyNOyN-WQozkHDpZOqXJOKVzWDoeFO6g2hM28lJ3jDZErRWbwIPj_zGs9HyAZLhIYTnzkc-Y2L_KtI4ZoV0ivBdHXXCaiyVue3YaHk2lLnqkcDcJdOrPAjK-S6IohJL7hvx1f8TFF761HaOtC9mB47rGjmOfG6UpDhTfJTc1cPtaX5aYjLFLKR-a13mKjFRWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضخامت رنگ کوییک اسباب بازی از تولیدی کارخونه بیشتره !
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72308" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72306">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qOlvhB5AajAGKVPyVyiC5Gf8Rftl2GslUBHMjbU7AdCoNg7thgLyJ2iF-3IPQvFmTvnlhm-5lVr3CGrce7Ws_W_nEf8BoVtMcGpyMZrK2UjNylerVmD9rWEG9NMZ_fBWZajCdw9LwUmLaPb9u9Hd4NX1x_fal4CP6qc2s-ncBfde2W0y-4urkQquFeTnDuCz_4abunujiIufynfUrRSOwf5uLCf2Ogy9aU3B7xFNY3LOq3JWqb9wzSaGbgmmZeQkHf4eeq3rwSLSOgln4Bv-u7rWMWu4GIqrhlGMAdMx25oZ3xuMzbBd8a57-qZLAOt4RGNfPGn5zZo3wxMr2A6gnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=tKuD3Ah6-CtLjG6_mKLspFkpTGrIAxujSuqk-bZde2FRzCsAB7ySvy65fFPhasIP4ArDjRieZcF_n6Iwk6phEQyCSCIbFrZwFbob8yhTy7RhZkeutt6EoOCwzmAFHbUQ21vX0_cHtzrpkjIOtv2h7jBKuhOgPjCFoxGnV7L2097pf5eGhFUAW5mNX4UKY4gEy9Fbb8FW5FuWQmHre1XlREJpQ2EUzBOZxDY8LnQo2bu3sI4r2TnZfjjM9-vp-rUF3ia5PFTrQ5_Q9iXwx8_STPK2s4Pl88GUzWQPM-hS4pBEZ8aIZ5PfMTobSrTGapIDZCTKCh1K1n3i7vkytApr-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=tKuD3Ah6-CtLjG6_mKLspFkpTGrIAxujSuqk-bZde2FRzCsAB7ySvy65fFPhasIP4ArDjRieZcF_n6Iwk6phEQyCSCIbFrZwFbob8yhTy7RhZkeutt6EoOCwzmAFHbUQ21vX0_cHtzrpkjIOtv2h7jBKuhOgPjCFoxGnV7L2097pf5eGhFUAW5mNX4UKY4gEy9Fbb8FW5FuWQmHre1XlREJpQ2EUzBOZxDY8LnQo2bu3sI4r2TnZfjjM9-vp-rUF3ia5PFTrQ5_Q9iXwx8_STPK2s4Pl88GUzWQPM-hS4pBEZ8aIZ5PfMTobSrTGapIDZCTKCh1K1n3i7vkytApr-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72306" target="_blank">📅 14:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72305">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اثر جدید ابی به یاد جان‌باختگان ۱۸ و ۱۹ دی
از او بگو به دنیا..
از او که قصه ای داشت او جشنِ زندگی بود..
سروی که قد برافراشت از اُجرتِ گلوله ..
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72305" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72304">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=aI9RYkmzgT9oSbF_5dnWo4ZCPFM7bZAGGX8bOxX69uKdIvEg4gIC854at1lAZ9ih3ZtT7GMITQC4s4WDRM2C8KbSkTLRLf9dk8j8KpEazwwlG0wvNIhn_EyWMpxfXxFVCHYXouwAAGnnuA7i1uCzrWxJVf9zjHm220QdHMx7rElKpRFryk9rlSBqVeuXbg2A-0IN8qq3zRnKmMt2CoSU4wcFVMawYXGvMkIW1-i9YVa8K-tBGgF6cJp_ZLaPXVQjRN55Sy9jzqR8HUOTc_JBh2qrjX5ha3Py3WGQb6glepayBzVW1ym4qcbC9AZsuzfmXfDmk9WIu13PIJfCzRitOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=aI9RYkmzgT9oSbF_5dnWo4ZCPFM7bZAGGX8bOxX69uKdIvEg4gIC854at1lAZ9ih3ZtT7GMITQC4s4WDRM2C8KbSkTLRLf9dk8j8KpEazwwlG0wvNIhn_EyWMpxfXxFVCHYXouwAAGnnuA7i1uCzrWxJVf9zjHm220QdHMx7rElKpRFryk9rlSBqVeuXbg2A-0IN8qq3zRnKmMt2CoSU4wcFVMawYXGvMkIW1-i9YVa8K-tBGgF6cJp_ZLaPXVQjRN55Sy9jzqR8HUOTc_JBh2qrjX5ha3Py3WGQb6glepayBzVW1ym4qcbC9AZsuzfmXfDmk9WIu13PIJfCzRitOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ در پلتفرم ایکس منتشر کرده:
در این ویدیو تصاویری از انهدام یک لانچر سپاه دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72304" target="_blank">📅 13:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72303">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش های تایید نشده از انفجار در نزدیکی جزیره خارگ/همچنین صدای انفجارهایی از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72303" target="_blank">📅 13:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72302">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc192b406.mp4?token=azsCdGjJg4oo5t9VCXegLneK4Y8sM-S0iBCfcUxG-rPXv2rkSDN1wlA2qBA38Z09T4kuBB5QoboHooIVimC1dhZVQ6WkoqdYFu0G6Vi_BcKzywj3vPW-AmDXaWpsDCJUgtXjQBgtxHb5_pkz-9BFLENR-mcsEd6GDRg5ERCbgX49HBwo2pyPzShudUHU86dtQDrOcT8OcPwNfCl9Y5Muq4UyuyLXA1HQqpGQInYzWggA-sGkxN4CK2yws9PVT9Kt-O3RePTtye9GLogrc0iuvst_K-KVC8YQSItN-pj_RKP9DG5Pq0D-MvPdwWpigv6ET_HdME6MnePlPPLnRW8s8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc192b406.mp4?token=azsCdGjJg4oo5t9VCXegLneK4Y8sM-S0iBCfcUxG-rPXv2rkSDN1wlA2qBA38Z09T4kuBB5QoboHooIVimC1dhZVQ6WkoqdYFu0G6Vi_BcKzywj3vPW-AmDXaWpsDCJUgtXjQBgtxHb5_pkz-9BFLENR-mcsEd6GDRg5ERCbgX49HBwo2pyPzShudUHU86dtQDrOcT8OcPwNfCl9Y5Muq4UyuyLXA1HQqpGQInYzWggA-sGkxN4CK2yws9PVT9Kt-O3RePTtye9GLogrc0iuvst_K-KVC8YQSItN-pj_RKP9DG5Pq0D-MvPdwWpigv6ET_HdME6MnePlPPLnRW8s8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی خراتیان کارشناس صداوسیما از نامه ای محرمانه که چند روز بعد از اعتراضات ۱۸و۱۹ دی از طرف جمهوری اسلامی برای دونالد ترامپ فرستاده شد می‌گوید :
ما از طریق سوئیسی‌ها، حدود دو سه روز بعد از حوادث ۱۸ و ۱۹ دی، نامه‌ای محرمانه برای ترامپ فرستادیم.
نامه به تقریر رهبر شهید بود و فکر می‌کنم آقای پزشکیان هم آن را امضا کرده بود.
متن نامه چند محور داشت و لحن آن بسیار جدی بود. در این نامه به ترامپ هشدار داده شده بود که اگر جنگ را آغاز کند، شرایط مثل گذشته نخواهد بود و ایران درخواست آتش‌بس را نخواهد پذیرفت.
تأکید شده بود که جنگ را به منطقه خواهیم کشاند، به پایگاه‌های آمریکا حملات بی‌سابقه خواهیم کرد، به نفت رحم نخواهیم کرد، مسیرهای انرژی را خواهیم بست و چه جنگ باشد و چه نباشد، به اسرائیل حمله خواهیم کرد.
رهبر شهید نیز در یکی از آخرین سخنرانی‌هایش تأکید کرده بود که این جنگ قطعاً به یک جنگ منطقه‌ای تبدیل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72302" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72301">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72301" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72300">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_uj4RsdfFDJhEEvAlgP1H6XVmYHRjrjwxt8FYMQ3o471lw44cO8_PEHdaMYT1c9AnAQ-G_8ImvHQByA72ib499wmQTaQOH1uETHqFNTiWs7zrPUrSW2dKI6hZ7U6j2y7hL1Sp4ND0uzvMDJdOnJ9S2fIQUhclWIc5r9srNrFpCRpeINYzlXIsf0UyobPhlGunf29cEcTsom18TVUpZu6dkDeBBE0M3Jnyjq88EXZbo-3fbloD8nhNEneL11BqxMJgrM8Rm6HxGzP2kGXF8GJcZIaATTuGRPz0S_wafUehhg5Zmi2KKrNnOUHorEunDzi741OOwJs6nzYx8xhHSLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز اسپانیا
🆚
انگلیس را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
اسپانیا: ۵ برد و ۹ گل زده
انگلیس: ۴ برد، ۱ شکست و ۱۴ گل زده
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72300" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z37wp4ovswiU_C3sPlCbUKdRN6NeY6daYvXzAE4JcmInNDIvCJvD8D-TfNJWDurH4GbQnto4asoz7IsGIGAyfECB6oFj8GsYFrWL8sYC35cmKkoejgoFerS1Io7TNgwnCji68QA1CvYUvPAVRWZMYEhIJi5kqcIywwqNxu98vyB0ZY3pLhZyBYYlFP4DVTCIIHlkOBKzCXK-7XRumo--Q0okssTE_TcVL0GmnCQ9J_RMcJKn9tt7QXxjI9ejFTtID5YLMJC382GJPY69Xvk0mhchrF52paw07EsAh4tArYJ2YhvZ5r2SHhKLgx5K6-Vabm-BIHP4GyIPSmdZ0WD99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSk8Ol3hoJ3PxaOC9dGzW8cL1a7AhKX2PinhiLWnwR1rYuPDWWFPyD7GMMBc0Gsmi_VlUEGtXGnishkUVx5xbhV2PvMUX5SHWQADTbjit8EigBTjZgJWEMFHq6yaLM33tGcmxZgYTiQZSu4vAm9DR4Bs4LClaI9CX0N0MgjVpojH1dTqWa9FmQFcQX5q1Cmbe3S_Dsy5dqdJ79um6hH-P9nUWConJ2ZBZyPtHJAZ9SxV7_QuyQYQtd53i7f1SF8Hhlf5f1RlfS4h2g8TuxkerOoQqR524EBVDPC9MjK_HisPVfV-eZ98KQhfHEJ7vewU63qnRzO3qe4xZGSW-8UcPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hP5uAaOvtpOAB4Q6h34CmR1cjygdBirD1pmXP7q-dc9W6nPeYFqY8zdxBNhPN5FxaSUcyLHYxziRJoHTZQz49qdFQQwtrdulF7s75LZhPKiOQar0Qno7aA2gQaBrcc4qiUzycXbR0nZrfu0RB8go3XwNQdw10M0h8LPPzSnjfpzOxVgYrToR0ttTeU0WTg_VjhqByhHMGuW-dsLFQWegv-Rl1ZDq09HMeMblO4JXn_u2LABJHGdbsHMzwRc2GYyQAMb5Bar8R0suxcC6acyz-i-43j2IGKW2Jux-BampNAjc5GHGj0k1PMabVLnxiFsdHngg9Fkz5KOyGGXXBmj3pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سیرک جان فدایان ادامه دارد
ترامپ توسط جان فدایان دستگیر شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72297" target="_blank">📅 12:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=kABJAEHPvLb3RrzuP6Sq4mqcETls3ibY7gUkxvcT9bCbHgtBejPcN3jT6b5b_3ju0tBerDs4JF-O31Ep_fDhiX89ctL_bbs6xETYPRGcMr12di_14A6ofjVZ0yLZUv5pSPIWd9X0hJ_jOtkWjR0pS1AZaBYrpWZdJeA9MvW4_5XSrP0m4H_1VQFBVRRMsYEa0a2k9MH4a6uaVCxvt_QfF6sezmvfV-ATgwMm8H1xQAE39Nt2rGLh_LU2YEzy3S07Cg-u-n2yTLp7K9oWwgWKpQ0JXijmxUOB_mepv6fm1G9409CDxNsuGcje21uxwfq-Df3CkBN0GyJPigr0pC3qOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=kABJAEHPvLb3RrzuP6Sq4mqcETls3ibY7gUkxvcT9bCbHgtBejPcN3jT6b5b_3ju0tBerDs4JF-O31Ep_fDhiX89ctL_bbs6xETYPRGcMr12di_14A6ofjVZ0yLZUv5pSPIWd9X0hJ_jOtkWjR0pS1AZaBYrpWZdJeA9MvW4_5XSrP0m4H_1VQFBVRRMsYEa0a2k9MH4a6uaVCxvt_QfF6sezmvfV-ATgwMm8H1xQAE39Nt2rGLh_LU2YEzy3S07Cg-u-n2yTLp7K9oWwgWKpQ0JXijmxUOB_mepv6fm1G9409CDxNsuGcje21uxwfq-Df3CkBN0GyJPigr0pC3qOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکر کارلسون گفت که پس از تلاش برای متقاعد کردن دونالد ترامپ جهت پرهیز از جنگ با ایران، او به وی چنین پاسخ داد:
«بله، حق با توست؛ اما در نهایت همه ما می‌میریم، پس [این موضوع] اهمیتی ندارد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72296" target="_blank">📅 11:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=QVJTCyiN0OEOsodD2yjgqDbzebf7ysdOjVHlmED3BDzJhsFZx8qMMAFkihwI8ux6A8gHohMZJIIXLbudItZfFmKr_h8HGJ7LDmiWh4DZ65xpxI9d9J9GYUEyD68U7LJM5XASUp8WmVj8maxYrXiNRpUc2Lwy5OQHy-PbpTPkCJbi9EOZpBgEzmdsg94-639uPAkBTumu08f0GWNAdCMQtWsrIMPd83LGuA9gvsA4E8-_u1pKrjOV1BedtPM4m4q1lHzIzZij5Dg_g2vZR2bceecNUavF2MNzQ_Ay4MStZyN8q67EEeiFgqttFhe_eqfT_nrqZG4avvf3HRsYY0r9JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=QVJTCyiN0OEOsodD2yjgqDbzebf7ysdOjVHlmED3BDzJhsFZx8qMMAFkihwI8ux6A8gHohMZJIIXLbudItZfFmKr_h8HGJ7LDmiWh4DZ65xpxI9d9J9GYUEyD68U7LJM5XASUp8WmVj8maxYrXiNRpUc2Lwy5OQHy-PbpTPkCJbi9EOZpBgEzmdsg94-639uPAkBTumu08f0GWNAdCMQtWsrIMPd83LGuA9gvsA4E8-_u1pKrjOV1BedtPM4m4q1lHzIzZij5Dg_g2vZR2bceecNUavF2MNzQ_Ay4MStZyN8q67EEeiFgqttFhe_eqfT_nrqZG4avvf3HRsYY0r9JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان درباره مجتبی خامنه‌ای:
مجتبی خامنه‌ای هیچ‌گونه مشکل یا چالش جسمانی خاص و مداومی ندارد.
در آخرین دیداری که بیش از هفت ساعت طول کشید، البته ما عادت نداشتیم که آن‌قدر طولانی‌مدت در حالت نشسته بمانیم.
ما زاویه و وضعیت نشستن خود را تغییر می‌دادیم، پاها را روی هم می‌انداختیم و کارهایی از این قبیل؛ اما قطعاً او از سلامت کافی برخوردار بود که بتواند پس از آن ساعات طولانی در آن وضعیت، بایستد.
از منظر پزشکی، او کاملاً سالم است. این را از زبان من به عنوان یک پزشک بشنوید و بپذیرید: او هیچ مشکلی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72295" target="_blank">📅 11:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=HMGzy5V-eGzR4nEde1Ln4vqCu3KHTfnY1kaA9QSu0pV9Te0kAggabdbwE2uBAHGqYxUZN7l-sh03BFKNqFnp53-bi3c5mAI_LjbD2pGpKyij31gsgz2M_cYoqq-DhQN6P1DegV79CoGsCFzXzbRhVg59h8fYp4h5VXVRj1zxtzov--xxD9Dfbn4bs9beTfq3egkyM5ybf3RVsTSnTXxL2_2UNqjHsdU0k2oBDkZkoH7WEnVwxXuKP_tBbvqdzUzgQoEVJ8AvLuMoS1u-8iGcKcnhjDSu9bns5QVnZ-D6WGM6V4GNTTKNucd9HGlHSGtO9m1MtwnS5gGILRRWRNL5sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=HMGzy5V-eGzR4nEde1Ln4vqCu3KHTfnY1kaA9QSu0pV9Te0kAggabdbwE2uBAHGqYxUZN7l-sh03BFKNqFnp53-bi3c5mAI_LjbD2pGpKyij31gsgz2M_cYoqq-DhQN6P1DegV79CoGsCFzXzbRhVg59h8fYp4h5VXVRj1zxtzov--xxD9Dfbn4bs9beTfq3egkyM5ybf3RVsTSnTXxL2_2UNqjHsdU0k2oBDkZkoH7WEnVwxXuKP_tBbvqdzUzgQoEVJ8AvLuMoS1u-8iGcKcnhjDSu9bns5QVnZ-D6WGM6V4GNTTKNucd9HGlHSGtO9m1MtwnS5gGILRRWRNL5sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا ایران بعد از امضای تفاهم‌نامه با آمریکا سه کشتی را زد و تنگه هرمز را بست؟
اینجا احمدی‌مقدم در حال توضیح دادن یکی از دلایل آن است:
نود میلیون بشکه نفت‌مان از محاصره خارج شد اما خریداری نشد.
چون ناگهان نفت زیادی عرضه شده بود، مشتری‌ها با قیمت‌های پایین می‌خواستند بخرند.
با بسته شدن تنگه، همان را با قیمت بالا فروختیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72294" target="_blank">📅 10:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aF-uTF88A8PD3d_5Yp1W--LB6keGUjBM5ix5ZFein-nbZfMrC9LgabKuMdpW5goXrbjoQI3LNHi6gSMbN6ndbjDJaJ-TzZ0nIm69U7bE8nQN6ghHoeiDN9bGTN8lOAJbv4kapB3cwVuxpFVpbdGXsYSCX_NJ41xJ3BAd2JN4ltM_Ds7s-25-VNukd1HwxTSv_mxejPZvnV4oyY4TycsL3hejaMNmQiMvi9Va1v7ZcfSPoAlPyPqPwqGYo8pWOQ7iKksFYrcrdeTy6eGefXwydcXXFbrsjgmuIGdanrJ8cb82RjY70uf3akgedHh_uSinXRu5o78vIpK_yBqKmYTg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وال‌استریت ژورنال:
به گفته مقامات آمریکایی، ترامپ پیشنهاد ایران برای برقراری آتش‌بس هفت‌روزه را رد کرده و اعلام داشته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران ایران از سر گرفته شود.
پیشنهاد ایران شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران و کاهش فشارهای اقتصادی از سوی آمریکا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72293" target="_blank">📅 10:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=ZWguwrTWz-EQvG87hr3Zh3-nnnI7SazOTkWpCS23B9_EuoRO5-gN-TcTTeyvYez6XpJgUgj1wbg69HJR06hH1Td2569MWyCrqxqWupCWXvrdJeaAWCxL8dn9JrcpXsaKsOG5H1meQL0sDwZjWC7HjfPC1sv3npSobrwx0djyOoxMPgHha4rZ4GzTMSAHpzoNPNWqKNlta85QDiO_6S3W44VblRZLd-TcJpeRUoUMmSwxzuzM7Xc1OgL9Mn_S6N3KEhZPCVTwHXGZMIKTdHkuPbWh7E-IQsS8xR6t0KrT-lynYoq20AyfHTCzMcNIfox7l37sicuNqlJgMxiDByy28A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=ZWguwrTWz-EQvG87hr3Zh3-nnnI7SazOTkWpCS23B9_EuoRO5-gN-TcTTeyvYez6XpJgUgj1wbg69HJR06hH1Td2569MWyCrqxqWupCWXvrdJeaAWCxL8dn9JrcpXsaKsOG5H1meQL0sDwZjWC7HjfPC1sv3npSobrwx0djyOoxMPgHha4rZ4GzTMSAHpzoNPNWqKNlta85QDiO_6S3W44VblRZLd-TcJpeRUoUMmSwxzuzM7Xc1OgL9Mn_S6N3KEhZPCVTwHXGZMIKTdHkuPbWh7E-IQsS8xR6t0KrT-lynYoq20AyfHTCzMcNIfox7l37sicuNqlJgMxiDByy28A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامبد جوان :
سانسورچی‌های صداوسیما واقعا مریض جنسی هستن
طوری که با سیبیل خانم تحریک میشدن. میگفتن سیبیل فلان مرد زنانه‌ست و تحریک کنندست.
یادمه توی یه سکانس یکی از بازیگرا میگفت «بیا بشین اینجا». میگفتن اگه یکی فقط صدا رو بشنوه ممکنه از «بشین اینجا» برداشت بدی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72292" target="_blank">📅 10:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=cGHa7es96RyuTeUAs_NerzaAUxqVf1C1ooAXGayjqvRWLMDFhA150AcVW3gxiSKfQrTZy_zH9A062C1ZHAOnAZY58PtFmca0wR58KGIjQjk-_ozNO-el1AAnriDMAFZH-LqS8_IPBJt-kW2AQ-3pMG14HCM_vjY31wUFP_46gto5c1NpDqlRWOSAPGjphPoQMuczp0dqCAKzokCD0UwBU_iSo-jEa3ilpjKJbYYiJ-juWCGdr0j-wtCvjqDPkLFj-rpPZRTgR9r6twD0jHF9YRklICMa0KV7jOfTRIukqQDGVREllz1BQhxMSzqcuLmXSrltML42gj2KLuRoQKOxAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=cGHa7es96RyuTeUAs_NerzaAUxqVf1C1ooAXGayjqvRWLMDFhA150AcVW3gxiSKfQrTZy_zH9A062C1ZHAOnAZY58PtFmca0wR58KGIjQjk-_ozNO-el1AAnriDMAFZH-LqS8_IPBJt-kW2AQ-3pMG14HCM_vjY31wUFP_46gto5c1NpDqlRWOSAPGjphPoQMuczp0dqCAKzokCD0UwBU_iSo-jEa3ilpjKJbYYiJ-juWCGdr0j-wtCvjqDPkLFj-rpPZRTgR9r6twD0jHF9YRklICMa0KV7jOfTRIukqQDGVREllz1BQhxMSzqcuLmXSrltML42gj2KLuRoQKOxAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:  @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72291" target="_blank">📅 09:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7db87608.mp4?token=AZy18p758lgN3KCuNcACPUIh2gAb8496K9kDHsbrzg01OkNxkTJVWcfCQ1RK9RvLTX7ISs8A2YSLiJ7Oqtr72On5D6j5_SUx84xc33wF6RtwH2ba7d-xBsw7brCMimWahduxa52p1E0cBOk7PHBKtZ8UeEzI-k81vCHfW_WsPjca6URoCMUviKtK9J7NLVut1xQjMFdw1rGcicWq7l1rx3oMVHPdfXmiAk57-yrjBt1JARlyFr6PAsVAAaag2HkNM1D4nPoQmuf7vYBt4wLcTYuJzXjk2XcSd4uBs4n2l7lX2-DUDDkfABT3qhiFdJoU28JmR26PCu-yBFNCK9AEUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7db87608.mp4?token=AZy18p758lgN3KCuNcACPUIh2gAb8496K9kDHsbrzg01OkNxkTJVWcfCQ1RK9RvLTX7ISs8A2YSLiJ7Oqtr72On5D6j5_SUx84xc33wF6RtwH2ba7d-xBsw7brCMimWahduxa52p1E0cBOk7PHBKtZ8UeEzI-k81vCHfW_WsPjca6URoCMUviKtK9J7NLVut1xQjMFdw1rGcicWq7l1rx3oMVHPdfXmiAk57-yrjBt1JARlyFr6PAsVAAaag2HkNM1D4nPoQmuf7vYBt4wLcTYuJzXjk2XcSd4uBs4n2l7lX2-DUDDkfABT3qhiFdJoU28JmR26PCu-yBFNCK9AEUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احسان کاظمیون فعال اینستاگرامی، یک هفته با یک پیج فیک دخترانه با پیمان اکبری، مجری سپاهی صداوسیما توی تله انداخته!
آخرش هم باهاش تماس تصویری می‌گیره و پیمان وقتی می‌بینه طرف پسره، خشکش می‌زنه
پیمان اکبری همون مجری حکومتی بود که بابت اعدام ها از اژه‌ای تشکر کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72290" target="_blank">📅 09:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72289" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd4aEb28tQkXZFZiMYii2eR0DYa-HWqRDWLP_6WfILLlA-6_-jW1Z_IFRzUDGtej9baoLxlCvvH6pttbZZiRG9wbXDk8KUY2ZoQsAZSH4ZgeDgtUua7hXj-jgGTSZgjmhJshcnjJOGdZx0USGkYDSRUOVv21rZWOcqnbLkAA2vVvbwYQJbI2mVBx9EXyHt437DAcSbfXqYZUTkt8Ki17oV1GIOniBan9eHPXi9pqjXleEENePHEkWrd-hCcSrBGH9vjLOXcht95rEIM6NJ-XxAQLath2wj8mQWaRoD3L-DxrQE_v3LRXl5ES_hwUuk8gf84zIcIpVX14GtMMLnbXqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72288" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72287">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CVj6nlxfBl_aGVlIcBtWIdvY1gghNKwrBn7QzsTn1KQeni54jpdB_hB4NzkpNhZUrcdh14F6cQBw7q6n6LaKM392RVeYwqwVKEfQMq6RWYT2cY27F8eXBYFzn9T8Tl4Vw3SdGd-9o7B4anChfI6hDpEj_OmRGSAQOMikjwioPf1Dug6K_NtxoquAQdXQDEBFfS0kxgcZnu85KHX5FfZCekvehWmV5fl_5PptPhS7gZUQEfJ_Z3d3yH-f6SDsepZR2iT31gA24ADUf_1gVOwons69F7DzpY29hUJIZP3qMgffxS3JyPNFlvoWbPobmO1sLo8S_yzxd3PFIqecmv_MwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه توی ریاضیات و بخش توابع مشکل داشتین؛
این عکس به بهترین شکل تابع f(f(x)) رو نشون میده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72287" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:   طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه. در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه. توپ در زمین آمریکاست.  @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72286" target="_blank">📅 00:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72285">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=vmTUsh8D0TU9Le1ZQySWpyoHgvCWKMu02icDEGv1THgPCtjxfMtIoNqV5A-CXJ7DAG7hdObcZ4JdFzpDsM54Ug-Ul6vbUuAofio7MjsWgmOWGbiu1t3DYKP4I5Ct-IivljIKLC-OWbjN8sMhXvmcXA9tU3nrikq2uHdl_fnGzZllxN-ZaBUoJm_uaBrRrEGGMxp0aEmuGSlkRZKgp3jJXzm7-xBJNSJLlu23RIpbHbbceu-ETFuv0Cv4ZMIQ16S5VPFUBaW-nwwChvZb-iqjmkZEHB0cUcLU0zuIVwuSMVUIVFci2I0R2JfAjWmmzOzoHAAcU9KdHn0kJeE622fbSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=vmTUsh8D0TU9Le1ZQySWpyoHgvCWKMu02icDEGv1THgPCtjxfMtIoNqV5A-CXJ7DAG7hdObcZ4JdFzpDsM54Ug-Ul6vbUuAofio7MjsWgmOWGbiu1t3DYKP4I5Ct-IivljIKLC-OWbjN8sMhXvmcXA9tU3nrikq2uHdl_fnGzZllxN-ZaBUoJm_uaBrRrEGGMxp0aEmuGSlkRZKgp3jJXzm7-xBJNSJLlu23RIpbHbbceu-ETFuv0Cv4ZMIQ16S5VPFUBaW-nwwChvZb-iqjmkZEHB0cUcLU0zuIVwuSMVUIVFci2I0R2JfAjWmmzOzoHAAcU9KdHn0kJeE622fbSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:
طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه.
در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه.
توپ در زمین آمریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72285" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72284">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=geP37u5XHCmjd-xuhUmHSDwsRaC9FY451WmfSzQo1Ef1lMRE_Rosx7pvQHlhgzDzdY3h1OPU30bmboWkQgeRRPoN9kQwCgh5SMNzPiD886W-cg-1PtEopO__qiKcw68Q5ZyvFdwt0hFSTXhXEB72uRtaYzi9S1g0LLJGZBfqPylDEkF-kRvFg1yR7XgO6cCvwRs0sX5hp60kW-q7mIpDVQAYGa98ugiPjxFyjVbzE9As-zbmv6wPDQvJ6LPABGm3cdVR-aiEgenvRG1a-xwG6-A1bn5FP1raYTTDqvyMl5igEGVT5sWYqOcPswtyjtrUmN2P49cdbONh6GplqZtL7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=geP37u5XHCmjd-xuhUmHSDwsRaC9FY451WmfSzQo1Ef1lMRE_Rosx7pvQHlhgzDzdY3h1OPU30bmboWkQgeRRPoN9kQwCgh5SMNzPiD886W-cg-1PtEopO__qiKcw68Q5ZyvFdwt0hFSTXhXEB72uRtaYzi9S1g0LLJGZBfqPylDEkF-kRvFg1yR7XgO6cCvwRs0sX5hp60kW-q7mIpDVQAYGa98ugiPjxFyjVbzE9As-zbmv6wPDQvJ6LPABGm3cdVR-aiEgenvRG1a-xwG6-A1bn5FP1raYTTDqvyMl5igEGVT5sWYqOcPswtyjtrUmN2P49cdbONh6GplqZtL7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب‌افکن جدید «بی-۲۱ رایدر» (B-21 Raider) ایالات متحده، پرواز آزمایشی خود را بر فراز کالیفرنیا انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72284" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72283">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرگزاری فارس به نقل از یک منبع آگاه ایرانی، گزارش‌های «اکسیوس» و «الجزیره» درباره دور جدید مذاکرات ایران و آمریکا را تکذیب کرد و مدعی شد که هدف اصلی این گزارش‌ها، تأثیرگذاری بر قیمت نفت و ایجاد ثبات در بازارهاست.
این منبع همچنین ادعای الجزیره مبنی بر اعزام کارشناسان فنی ایران به نیویورک برای شرکت در مذاکرات را رد و این گزارش‌ها را نادرست توصیف کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72283" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72282">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eda15604.mp4?token=pAQFUAncovJtR-jNVHt-RCRwV1C9xKi7_7UHYK3pbHxpcWHH1nUoQpuEyqpeNTRjw0XCcSC2YbIshY3ZOLHj2NwLPZU3urfkRlfmCfXFa_bemFsEKvYMtDt0id6au6aVCKbKI9eFK-_2L0UIJ4zswcecHAwVHA7ByhB5i7Psar92iFiOFVSepo2IJLW3RyXL_zT9KzaMKmlIzkNGfWin2O9DbH3jwCjUMgOZjy_Suat3DdLVV0RX1a4G6O2LttvN8mqD5bbz5xUDaSn3nzCZa_ZFA7FVRpx1-LZ1w8UjtZpNv-4-wmTSXHt5eftZyKq_zkgx6zWcoeNttjHk_CazUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eda15604.mp4?token=pAQFUAncovJtR-jNVHt-RCRwV1C9xKi7_7UHYK3pbHxpcWHH1nUoQpuEyqpeNTRjw0XCcSC2YbIshY3ZOLHj2NwLPZU3urfkRlfmCfXFa_bemFsEKvYMtDt0id6au6aVCKbKI9eFK-_2L0UIJ4zswcecHAwVHA7ByhB5i7Psar92iFiOFVSepo2IJLW3RyXL_zT9KzaMKmlIzkNGfWin2O9DbH3jwCjUMgOZjy_Suat3DdLVV0RX1a4G6O2LttvN8mqD5bbz5xUDaSn3nzCZa_ZFA7FVRpx1-LZ1w8UjtZpNv-4-wmTSXHt5eftZyKq_zkgx6zWcoeNttjHk_CazUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون سوال باشه چرا به یه جمع دخترونه میگن خانوادگی ولی به یه جمع پسرونه میگن مجردی:
دیروز ، رامسر به سمت جواهرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/72282" target="_blank">📅 22:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=Rd7H06TweNyx7ePXkuSEfXmtYTaz18ZkJGdERODVW7dWmdMK1Y0m08uePSmWwXs3CzqJrW36_dRNplG8TCs-dBmMo5sJLk4mxzureRnJqdNknnUVjICpdYp9i6HxME2vPZADv6MRvm9mlbzuLMLno_nFj8m21LKhw4QUKHOp0DqZwLMdbb5tyfxqLn8j27CwVgpz0BK_kuJsEUL10f-hXlwrmoJ5hDc8zZSxi5CzG_eRzCBeip82LECJV90q92w5sW3fY3ue7A599bP0FTgurJVP5t92fgaeZdvTOcKgXR3lYYQATIlbzn_j-enh0jX63MISFvNd8ouMRr5m4P6-bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=Rd7H06TweNyx7ePXkuSEfXmtYTaz18ZkJGdERODVW7dWmdMK1Y0m08uePSmWwXs3CzqJrW36_dRNplG8TCs-dBmMo5sJLk4mxzureRnJqdNknnUVjICpdYp9i6HxME2vPZADv6MRvm9mlbzuLMLno_nFj8m21LKhw4QUKHOp0DqZwLMdbb5tyfxqLn8j27CwVgpz0BK_kuJsEUL10f-hXlwrmoJ5hDc8zZSxi5CzG_eRzCBeip82LECJV90q92w5sW3fY3ue7A599bP0FTgurJVP5t92fgaeZdvTOcKgXR3lYYQATIlbzn_j-enh0jX63MISFvNd8ouMRr5m4P6-bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روسیه در حال اتخاذ تدابیری برای محافظت از پالایشگاه‌های نفت در برابر پهپادهای اوکراینی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72281" target="_blank">📅 21:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز:
ایران حتی در صورت پذیرش پیشنهاد تهران برای بازگشایی تنگه هرمز از سوی آمریکا، هیچ‌گونه امتیازی در حوزه هسته‌ای نخواهد داد.
تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته خواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72280" target="_blank">📅 20:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72279">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=kF3qg8aPjmEOk0jqp3D03PGqYgYyMXXJOD-tbDWyFekLTYyqHy3TqHTpkPu7QbBFdbqTplL9nq24hiJwBuqCGVJK3s8ly8vVO0ABGB9p5_y5Bj6CvqtJeLIcNsBBTqb-dQJIN_5pJSVcpWfpTgxZ1OkCAEagqP2WYRj7c2a1GFyMT1h4nUZUIYUY0E9dt6r5dZtCMmUnyFHm-24zULXNwMWdaLudeT_4MHv4wRiCuT-I4DWluehqPZEz2r-9imhl6e8rvZwkrt5YSq7rcPMQe63MeVPLL9aMk2XP2aCQCBySe7viH3CNhdCJY2hQebXS8KoWY7jpr82BDadkBOArMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=kF3qg8aPjmEOk0jqp3D03PGqYgYyMXXJOD-tbDWyFekLTYyqHy3TqHTpkPu7QbBFdbqTplL9nq24hiJwBuqCGVJK3s8ly8vVO0ABGB9p5_y5Bj6CvqtJeLIcNsBBTqb-dQJIN_5pJSVcpWfpTgxZ1OkCAEagqP2WYRj7c2a1GFyMT1h4nUZUIYUY0E9dt6r5dZtCMmUnyFHm-24zULXNwMWdaLudeT_4MHv4wRiCuT-I4DWluehqPZEz2r-9imhl6e8rvZwkrt5YSq7rcPMQe63MeVPLL9aMk2XP2aCQCBySe7viH3CNhdCJY2hQebXS8KoWY7jpr82BDadkBOArMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌بی نتانیاهو یه شوخی برا میلی رئیس جمهور آرژانتین کرد و اونم یهو زد زیر خنده
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72279" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72278">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=szQ0Tx7f6QIxaIuRIs5GM7l5ecWt940h9ClW0rljSUacjVrgrc-pLst0_-aECEu5okLh1wvuMQSQs__Q78s80vV_bNtHmvTR2xGTplcU9JQPlXPdo9orjhgc2uf-WXYYL_w2OdFgzX19Eo2SJ9plVqDxCLnZxjcQBY8ilzD1KZ5516fySqpD7SIX-FDzot6TfIaEKsAHDs8XGEt3zLzZx1j8zPTxfrGyQP32fnXfPDELib0BS15gKLNN8S3wIJsrLcVlw9BBAp6RBd4_956YYlodZWbZqsp1GXM0d5eJdJMrc57SwB4qCwjeirCPpu8WHPPWrAZ4gFmHR_1uTP-YPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=szQ0Tx7f6QIxaIuRIs5GM7l5ecWt940h9ClW0rljSUacjVrgrc-pLst0_-aECEu5okLh1wvuMQSQs__Q78s80vV_bNtHmvTR2xGTplcU9JQPlXPdo9orjhgc2uf-WXYYL_w2OdFgzX19Eo2SJ9plVqDxCLnZxjcQBY8ilzD1KZ5516fySqpD7SIX-FDzot6TfIaEKsAHDs8XGEt3zLzZx1j8zPTxfrGyQP32fnXfPDELib0BS15gKLNN8S3wIJsrLcVlw9BBAp6RBd4_956YYlodZWbZqsp1GXM0d5eJdJMrc57SwB4qCwjeirCPpu8WHPPWrAZ4gFmHR_1uTP-YPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای ۲۴ و ۲۵ سپتامبر (دیروز و امروز)، افزایش فعالیت‌های ترابری ایالات متحده در ارتباط با خاورمیانه مشاهده شد که شامل هواپیماهای ترابری و پشتیبانی آمریکا—مانند مدل‌های C-17، C-5M، C-130 و KC-135می‌شد...
تدارکاتی در جریان است!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/72278" target="_blank">📅 19:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=OwId23zecNF_M-QXWLtYCRSnNr4mfQgig8GE2CfSqFpVoe3-LQFEsJwjBLY3Sr83BFzpbmcwE-0dXLkEOqkAY4HrzUIYfCvb53xiXkdkn1Uee3fPnIVPC8IFFjpycACXVnxUg6C78S4BuMmN0lpV86_MqBEtH8OMsN7Lr8RV1kRM3SuPpaSzcoZP6iZ5gv5bsuR_JXqswo6S-f1wTOebC7-DU8crQNlIO0N3wDZMGCyNsINoCt4UJxXvf0XZH5Xfx12_n1Tb8Zv4DrJT_qB8MfDmzr6kJ3khzMAz5GIvUgZJzsnAv8NjYyxo9qt_OqBO4F2Ho24eKBWSssuIVPV9Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=OwId23zecNF_M-QXWLtYCRSnNr4mfQgig8GE2CfSqFpVoe3-LQFEsJwjBLY3Sr83BFzpbmcwE-0dXLkEOqkAY4HrzUIYfCvb53xiXkdkn1Uee3fPnIVPC8IFFjpycACXVnxUg6C78S4BuMmN0lpV86_MqBEtH8OMsN7Lr8RV1kRM3SuPpaSzcoZP6iZ5gv5bsuR_JXqswo6S-f1wTOebC7-DU8crQNlIO0N3wDZMGCyNsINoCt4UJxXvf0XZH5Xfx12_n1Tb8Zv4DrJT_qB8MfDmzr6kJ3khzMAz5GIvUgZJzsnAv8NjYyxo9qt_OqBO4F2Ho24eKBWSssuIVPV9Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شی رئیس جمهور چین میگه عکس روی دیوارو ببین؛
ما خیلی برات احترام قائلیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72277" target="_blank">📅 18:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72276">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=gNz82LYSWEry6uz9T8WgDVAYrr23tCQ5ZWYzkM6iwXdEt9d8kpzVmx99rb8R9G-V_2QQ9lWN1HIuLryKdFmOXaIeCXhGSBfiXD65fBfLCVjqQOtxxrC5KifPsxzEZfxJi63EVjJTO7HbNIWZ8_eTVoREUPocUNeEXBXcERX_S_HpsGGYeTbra7TvATP0AomG-7JkTh5Cwo3G_i-8QcyfpIA2D1meCTCa3MZ77GXF9WLVw0OCzMrMKxYfXau5G6DORsgnbWzpnPSpA9FSXag7ar7u3ISJqN-kdTm6B91U6y4ULYMpcJFE2H5Ly0vBaVYG_l3b5JZcVR544hiXjkx5Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=gNz82LYSWEry6uz9T8WgDVAYrr23tCQ5ZWYzkM6iwXdEt9d8kpzVmx99rb8R9G-V_2QQ9lWN1HIuLryKdFmOXaIeCXhGSBfiXD65fBfLCVjqQOtxxrC5KifPsxzEZfxJi63EVjJTO7HbNIWZ8_eTVoREUPocUNeEXBXcERX_S_HpsGGYeTbra7TvATP0AomG-7JkTh5Cwo3G_i-8QcyfpIA2D1meCTCa3MZ77GXF9WLVw0OCzMrMKxYfXau5G6DORsgnbWzpnPSpA9FSXag7ar7u3ISJqN-kdTm6B91U6y4ULYMpcJFE2H5Ly0vBaVYG_l3b5JZcVR544hiXjkx5Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده با این شرح:
مردی در مشهد با انداختن 100 میلیون از امام رضا شفای همسرش رو طلب کرد ولی همسرش شفا نگرفت و درگذشت و اونم برگشت تا 100 میلیون رو پس بگیره
😑
😑
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72276" target="_blank">📅 18:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72275">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72275" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72275" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72274">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqWUPqF_oZ0FNFyMXQUouy880dzt6OBkuKz4o-tAzAYidMVCoXFoPJbqV5jqdnTMimvnVBEgkT6XdRK0dcs1ifvO9Z6pEQHR32TZJxfa7GFBPboe0syZwjie5HE9pRT7VH0KLLGYdqp96ek4nmxx2ur_qLf_6zV9ZYhCfjXlqoAbbjk5DBIVwrNJUECzd-C08mkhdCR0mq1lvIU8csycam8iNLbx9EQEdSOMANGZiheVUKf7AxN1cC3fGWdzEDCFGvhFHGrD4CcTg5pG71grlXPyKheJMF7xKJbKg4eq-2kmV1o3bdIHjZS6modBLzaUhJ0pBvGDaEpMopW-LkA_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72274" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72273">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=sCUR62Xpkvmj_H72-Q914xfBFdaErKczaNJk9r8bt3ssan25V8clQR6qIEs1oi_t4iloe3hGegoX8ULKMqA3HX9BS3mFyoikZ-POVCv3aLQz8rr2QgJACPM-Twb81CLZIBcaaBmKP3ArhseYm74IeHu32FcOmQ1WUlseAUNLyaQTYVfMSXkrhN7MqT9DA0PCLikyh1AieIW50NuJGp2pJIWlarkuF7hUoIKuRk8ff1E4E2RwB83aaaKro1htxPpv7cPwTJugBR2d0C_-HPQycj6seL7Qpmo2tzwCo3V3ZWtux4bZg1FkEDNGKMYafPLzqhS55z-emiWFiIR7DIW6dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=sCUR62Xpkvmj_H72-Q914xfBFdaErKczaNJk9r8bt3ssan25V8clQR6qIEs1oi_t4iloe3hGegoX8ULKMqA3HX9BS3mFyoikZ-POVCv3aLQz8rr2QgJACPM-Twb81CLZIBcaaBmKP3ArhseYm74IeHu32FcOmQ1WUlseAUNLyaQTYVfMSXkrhN7MqT9DA0PCLikyh1AieIW50NuJGp2pJIWlarkuF7hUoIKuRk8ff1E4E2RwB83aaaKro1htxPpv7cPwTJugBR2d0C_-HPQycj6seL7Qpmo2tzwCo3V3ZWtux4bZg1FkEDNGKMYafPLzqhS55z-emiWFiIR7DIW6dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی گسترده در یک کشتی حامل خودرو با پرچم یونان در شمال جزیره میکونوس
این کشتی ۲۹سرنشین و نزدیک به۲۰۰دستگاه کامیون و خودرو داشت
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72273" target="_blank">📅 17:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72272">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=JQkc7_wrhulndmc-hQgRcuJYAC1ZpYkGQ3FyCkGxJ97uF8LYP1hoVBn9JDTmSfpPqL96i0F6Elzw1d67Z6wAujC-U8nUBsgAB-hP6oxaP85CTOglCjb-M8oLtJaH-84b5l003euOo-5Ha9xLOErWRsE4dCameR_FZuSwNMu0N_xHqhbu1NsppJBp0kQd8xjjUUd5B_zCuf4yks1ywRDkeYOhIv9COYdmQS20MvOL-1y-J1v5xiWlsqkETWF4K-voe2Q6VrgGNbFgWC7HHmRAUnpESx1_xfE0UgZHNOz7M1A4Hc_NRzZIth5ZUF93GJQZ3Aoqkz196-rYs7WCMKwcTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=JQkc7_wrhulndmc-hQgRcuJYAC1ZpYkGQ3FyCkGxJ97uF8LYP1hoVBn9JDTmSfpPqL96i0F6Elzw1d67Z6wAujC-U8nUBsgAB-hP6oxaP85CTOglCjb-M8oLtJaH-84b5l003euOo-5Ha9xLOErWRsE4dCameR_FZuSwNMu0N_xHqhbu1NsppJBp0kQd8xjjUUd5B_zCuf4yks1ywRDkeYOhIv9COYdmQS20MvOL-1y-J1v5xiWlsqkETWF4K-voe2Q6VrgGNbFgWC7HHmRAUnpESx1_xfE0UgZHNOz7M1A4Hc_NRzZIth5ZUF93GJQZ3Aoqkz196-rYs7WCMKwcTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت اسرائیلی در سازمان ملل اسامی کشور هایی رو که حین سخنرانی بنیامین نتانیاهو سالن رو ترک کردن یادداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72272" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72271">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=jXxWya4bNieURorJRjZWujM7dpiET_jkX98HQbz_-Qt3LwRA5MJD_g5nZyXtrnSwS6fkPXioaz4PQGGIyu5T3AKnWNy8hwV65xee-aYU2r2SJvBiMvn6LNIurlTNzNbh4kPF_9nFTc6G7p-INQc7maCXVttuAh8_6-Kpb8mpIpqXNcnLIHjcUFk58mky4RzDX_9sfNyxdVd4ijbuPpWsVEt0_C-tBspt4d3T2xDLM-gDeUw23ImWVhEmuwQQyb-U5Dt3mztrmGKOp_Gtzr_g4HLgxNdlys4JYsD3JVklyr7HdJWtsRBG0vlJBdV9owoEfk4P4dQTJ7BZQSH0H132qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=jXxWya4bNieURorJRjZWujM7dpiET_jkX98HQbz_-Qt3LwRA5MJD_g5nZyXtrnSwS6fkPXioaz4PQGGIyu5T3AKnWNy8hwV65xee-aYU2r2SJvBiMvn6LNIurlTNzNbh4kPF_9nFTc6G7p-INQc7maCXVttuAh8_6-Kpb8mpIpqXNcnLIHjcUFk58mky4RzDX_9sfNyxdVd4ijbuPpWsVEt0_C-tBspt4d3T2xDLM-gDeUw23ImWVhEmuwQQyb-U5Dt3mztrmGKOp_Gtzr_g4HLgxNdlys4JYsD3JVklyr7HdJWtsRBG0vlJBdV9owoEfk4P4dQTJ7BZQSH0H132qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پزشک کودکان : امروز تو تهران ی دختربچه ی ۴ ساله ی بسیار زیبارو آوردن پیشمون با خون ریزی شدید واژن، معاینش کردیم و کاملا مشخص بود بهش
تجاوز
شده، از پدرش پرسیدیم میگه با واژن افتاده رو جاروبرقی درصورتی که دروغ میگفت و مادر بچه وقتی رفته بود بیرون این کودکو با پدر کودک و دوست پدرکودک تنها گذاشته بود...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72271" target="_blank">📅 16:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72268">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc6xTukdl_ZYVFXqJfPWbI2TRPYBrQfqMX6ioMhCO69i73kNpbCIFcr6QUl__CUEOyGKZvKDq5kFWggoFcwfrApa--Tpmcq-KuqYWsN-i7yLBqjfGKDS25-zkbbu3jiZ-ExRvZldnnNQZtCH-_8-G2xMivi3lad9MXNWunCGzaByn5PGTMmScNE2xzax-fv87uG2j_tCjvZf9Z-SWvy72jFSQLSWM6F8Vhv5X1orEiHO6Gu3hpFBpBdY3oOSRAnDI4M5GDYZYbF7naf0C2ivya9li03Yy1vPdOCAvYJHsgbdC6aQe2N6A9myJ4VF5s9MvDVHGlAWxW5CX72qyrrhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=SUzSmnjhPsF7iJk8JKe7XOB493i_40me1P1BAJHZalU5fjlsYGTjATAEm-RR4kMxGgz16AiNy4fUPslBpowjsJqE338uN49s2W9VNXKbuLn2RemV3GaByXUte3VN8eoDNavMufw5uU2bcmelnk8-rWtaTZniQo-XcJoSVUA3qYLC74pas_X-2a7p0ogYYnaMM6EII_KItsY5OKJUl0Pl0TSymzyPfUOOqbJf2I5ZEh8YJhepVtat68VDMV1eMr1uXIiGYITaVlLRBb0NFvOFf4yXH2q5UCQ3xr8dLyF-cGDmii0d_rKOQb6RY8orWf2CwnE-H9Tso9fRfjsYB95kCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=SUzSmnjhPsF7iJk8JKe7XOB493i_40me1P1BAJHZalU5fjlsYGTjATAEm-RR4kMxGgz16AiNy4fUPslBpowjsJqE338uN49s2W9VNXKbuLn2RemV3GaByXUte3VN8eoDNavMufw5uU2bcmelnk8-rWtaTZniQo-XcJoSVUA3qYLC74pas_X-2a7p0ogYYnaMM6EII_KItsY5OKJUl0Pl0TSymzyPfUOOqbJf2I5ZEh8YJhepVtat68VDMV1eMr1uXIiGYITaVlLRBb0NFvOFf4yXH2q5UCQ3xr8dLyF-cGDmii0d_rKOQb6RY8orWf2CwnE-H9Tso9fRfjsYB95kCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای اوکراینی به چندین تأسیسات صنعتی در روسیه، از جمله پالایشگاه نفت «پرم»، کارخانه «ایسکرا» در اولیانوفسک و تأسیسات «وورونژ‌سینتزکااوچوک» در وورونژ، حمله کردند.
پالایشگاه پرم که یکی از بزرگ‌ترین پالایشگاه‌های روسیه است، در پی این حمله دچار آتش‌سوزی در واحد فرآوری «AVT-5» شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72268" target="_blank">📅 16:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72267">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که یک موشک رهگیر به سمت یک «هدف هوایی مشکوک» که بر فراز جنوب لبنان (منطقه فعالیت نیروهای اسرائیلی) شناسایی شده بود، شلیک کرده است.
ارتش در حال بررسی این حادثه است. هیچ‌گونه آژیر هشداری در شمال اسرائیل به صدا درنیامد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72267" target="_blank">📅 15:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72266">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=rpJdwMuDNxlQq1enLcvyFnqv-A0c7wtfom4wY1sc7VWqhl_iFuHlzkCAi0TkTGv7Zeu0sZyA57zNXukneI6O3im5PQZP_NrW4SNTvwWR_xRZdLTCZjJDoNV8kerZSEHf0MXHy07j7LmPCFL_xt0e8lKLbn3l5tergr_6kyWW2PYRdT7RM80ecqj6cX7bZ0vl1nyp5dOVxngWbux-FYzEn1kiOQPFaVvYA0rTsVEuD_nK1Cbx8zTtGH9fD0AGaMVLnRxoM7fGYMRp54bkHV_N3kXcWr6k6ZaVKFpSyuAbDF4Sy3TGe6HIJf6k8-Iv4_Eq0qnhbJiSXT2M5-nltxEN4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=rpJdwMuDNxlQq1enLcvyFnqv-A0c7wtfom4wY1sc7VWqhl_iFuHlzkCAi0TkTGv7Zeu0sZyA57zNXukneI6O3im5PQZP_NrW4SNTvwWR_xRZdLTCZjJDoNV8kerZSEHf0MXHy07j7LmPCFL_xt0e8lKLbn3l5tergr_6kyWW2PYRdT7RM80ecqj6cX7bZ0vl1nyp5dOVxngWbux-FYzEn1kiOQPFaVvYA0rTsVEuD_nK1Cbx8zTtGH9fD0AGaMVLnRxoM7fGYMRp54bkHV_N3kXcWr6k6ZaVKFpSyuAbDF4Sy3TGe6HIJf6k8-Iv4_Eq0qnhbJiSXT2M5-nltxEN4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از پزشکیان پرسید که میخواید بمب اتم بسازید یا نه اونم میگه نهههه نههه اصلا،
بعد بهش میگه اگه بمب اتم نمیخواید چرا اورانیوم رو بردید زیر زمین ۶۰ درصد غنی کردید؟
گفت اونو که میخوایم رقیقش کنیم! یعنی غلیظ کردید که رقیق کنید؟! بمب نمیخواید بسازید؟!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72266" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhr7noIGnClHFvbUYAMZQxt-SDQJJb1AkDMviuFHzgkCyULcDQPQNhnpFwF42mkOHGq6Qfl62s07F1sLTGVsk-wGSMv_TZnQ4fDDhLSigBVXNEey6_fWIWKvW9GhON5nuFH3Tup05V2QigUmtPED5orvWKHDFOnjH8AKAtwhZtMVjd8E9iGDPXPWa4ZW9YCBXNF-gCCkZ_MWLv0-KzTVk7T-oj9ZoqzcsZcygH-mM1kNRAqXS4wt488D3Uz4ZuzqexnSmYCLXBNCNoaDWJpW8EP2WtYIhzjzm2Cv0bwxzoGPhArB3Pqn76-Ho16PqPAPegM7GNrVO-Ssx3tX31AvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران طرح جدید ۷ روزه‌ای را برای پایان دادن به جنگ پیشنهاد می‌کند؛
به نقل از نیویورک تایمز و به واسطه وزیر امور خارجه ایران:
• توقف کامل تمامی خصومت‌ها، از جمله در لبنان
• آزادسازی بیش از ۱۲ میلیارد دلار از دارایی‌های مسدودشده ایران توسط ایالات متحده
• لغو تحریم‌های نفتی
• پایان محاصره دریایی توسط ایالات متحده
• روز هفتم: بازگشایی تنگه هرمز
• آغاز فوری مذاکرات هسته‌ای
عباس عراقچی، وزیر امور خارجه، این چارچوب را علناً تأیید کرد اما جزئیات تمام شرایط را بیان نکرد و اظهار داشت که این طرح تا حد زیادی مشابه توافق ماه ژوئن است.
نکته مهم اینکه او نگفته است که عبور از تنگه هرمز برای همیشه رایگان خواهد بود؛ در چارچوب توافق ماه ژوئن، امکان عبور رایگان برای مدت ۶۰ روز پیش‌بینی شده بود تا در این فاصله درباره نحوه مدیریت آتی آن مذاکره شود.
ایران اعلام کرده است که آمادگی دارد این طرح را حتی پیش از موافقت واشنگتن اجرایی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72265" target="_blank">📅 14:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=u25WkQeX2qwZYWONxeS8P1fYpY06nAuM36ltDqxDwJ5TO27tSlRdir06GGEOJgixYu27cWDu8a431ha9xKx0BGIz0JLGfmb8vU9-lzpkNY1aNMWHHS-pZfE2ngyp31Nv0G0aYOv6KL-OOqZmOu8K7M8bVa6fLnIfI-wIZcrGgy9WEXQgZj0y9SuXCvMyHe1VMfNSVesgLcQa070d1ZTVm-dV7k822XCxVVk3Xzfx-MLu6ArTcmJv3qnRAHEG6hRe8wJ6ZFeWCXFlOzOpx3yX6qNN-blrzcCfMmA1S7FNSPShGNieYj9AciT6q-wWH0RLRs-EsWncAf3uNsFN1ZF5Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=u25WkQeX2qwZYWONxeS8P1fYpY06nAuM36ltDqxDwJ5TO27tSlRdir06GGEOJgixYu27cWDu8a431ha9xKx0BGIz0JLGfmb8vU9-lzpkNY1aNMWHHS-pZfE2ngyp31Nv0G0aYOv6KL-OOqZmOu8K7M8bVa6fLnIfI-wIZcrGgy9WEXQgZj0y9SuXCvMyHe1VMfNSVesgLcQa070d1ZTVm-dV7k822XCxVVk3Xzfx-MLu6ArTcmJv3qnRAHEG6hRe8wJ6ZFeWCXFlOzOpx3yX6qNN-blrzcCfMmA1S7FNSPShGNieYj9AciT6q-wWH0RLRs-EsWncAf3uNsFN1ZF5Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم #hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72264" target="_blank">📅 14:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وال استریت ژورنال:کشورهای حاشیه خلیج فارس در مورد تلاش‌ها برای از سرگیری مذاکرات ایالات متحده و ایران اختلاف نظر دارند.
عربستان سعودی و امارات متحده عربی از دولت ترامپ می‌خواهند که فشار اقتصادی و تحریم‌ها علیه تهران را حفظ کند، در حالی که قطر برای مذاکره، از جمله پیشنهاد توقف هفت روزه درگیری‌ها برای بازگشایی تنگه هرمز، تلاش می‌کند.
عربستان سعودی با اشاره به حملات به کشتیرانی خلیج فارس و اقدامات حوثی‌ها در یمن، استدلال می‌کند که ایران باید قبل از هرگونه توافقی با فشار بیشتری روبرو شود.
قطر و عمان از بازگشایی مرحله‌ای تنگه هرمز و یک راه حل دیپلماتیک حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72263" target="_blank">📅 13:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BGDRy4HOJ5U4VqgR79LKgvEXpTVUZk1PGiHe9mdDDXOAGUWC2v58RR-lsQT37Wg-WlB-vllOVQ7T6CLCkZ-OWkFc0zj0f1lg1RBqq1aF5gZ2VG7C9rUpA9KqAuS-wnqTFt102cS55S7wVx6RwFYKVFi0cMf5ZvehCHvPYxHxDT_Dk0AcvvZE7j7ei9_-4vxW7Uy5oebFdnLh0yy4jmI1BzVzASOFKS1FDEtCrPX-qWQEbhYSsM41_6rjTqCRfgLJs5MUPf0YU-15IHWnBc1Ah5h8dTf0iYCvrVTsCIrp7_z-g9fQzDYfHxYUnHsZ45xLLdy_VCRa-0rrfGsVsIpShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hDyN5iWCyoXSaZcCPM_WcPGvlIkTiRj9BrBO-ACSEDILcqcm7ItSUKEdpbZIiqndiAlMuod5daqsR_GrfKT4uJh4iDlEkFp4LnawBz1-_QOO51fGZeJy4fFg8eTrDpCYcWtHx7wFJ8N_WEDsnauACQ-f4G4q9ekN5RV61tWaKoyDjvr7QWuWqD6Ys_M6vQE1x85YGLN4wt3NueTj5ELliyz0E7RKcpGiAyM47PuvNF-f1m3ZmVtMjiWAjaArIXnT9wkFPsCxhqYQ5V_uLXRgQkPY8gd-jxMzL8ud79uzy3mtewcPt4anzawmoqqjuXtfEBMJir7pufBz7lxY1poKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XgCmv0oMtbQ6wqp1r10TE55Z5cJhczX4TJsXGetQWSko5xmUNsC5ZPuCX_N0tOj6p6OdRAxLvVvffRca3G4IAw5RAjiMZ4R6wKAtUV8zkuWSP_9MtIyDm09_8U8Rbjm29YL2tz6JO06Tm12z45BEYA_5hfhoL6v_Rho_vHCdfF3t_3MI9RZRjmEMzQIvdnBHak_1Pv2oN8-q9NhECepN2iIZwciU6eViOMIZq8F7zPkEdmKESRwPj39iDkEBMSEInzq41D1EaSFb0SJRzqKnLx3RaRTay3gql9AdE7CmPtkc1EscwwCz0e7YWK5OzECNpg4Lsd7Ywaszg4qR0_LrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ag0X9UxFbqUhu5p_nzvQFWw9lrPXqFJRmu6rULvpU4xrxdQSdjrKg6I9p34xRj0IZpKMzbNNGy7x5hWDY5nZmyISOVtitl7E_OuDlkMrQ4D6jnKNOgXwGg5JOUkI0PSRhJ2F4y_g7HZEIMJEq-XhhXdJDH7ygFkdm8cukP2lioJ8iC-bImUVbgNylpGPumlW57e2jUWsVACqn-72erdaFNZ8GhKmltHhtlSXJLsQ4qQVVAmM75GdHnn1WHiAjf_NgUdkjJS5vIHk2L-MQYH_28C5YJ1rj4-PZ6DmZNelF3XsdGWPKK3fJa93-7tmv1TxBpdLVsbg1rhqh4y2h0CjyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگولی ترین دانش‌آموز امسال معرفی شد
این دختر کوچولو به اسم
گندم
لقب کوچولو و کیوت‌ترین دانش آموز امسال رو از طرف مردم کسب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72259" target="_blank">📅 12:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72258">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72258" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72258" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72257">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwuGWTdxTrsdmI4oVeM4dBtgDOpHf7RNQWfBe9wkLSa8FoEFUnNr_4Wrvw0drFmtE3TzLtiESCkmAstr6rOyoULInWVeJcLgyeGeETbSFfbtV67D8t_-cWUf2ytMZM1UVLVL116JB14W2yuXMEsjOMDzPP1g5ZuV9eYFIhelFkkUUW9GJFuVY3zKerNvSEyGiiS2eCgd0Iq9q_N9xyHiDFDhRJJ-Y-k3o0crdZM2PP_I4u_LX9SwQSIcZ6zSF4f3J_bgui89Plssi1nBlq3-AZwyNM0xsNzzpscZwhmBkB1VCmGTqRcKAzE_Ml7NIwBcqd_hvtf1p25iL6p12pQBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72257" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOCQCHwe9aVO3DrZSorWr6g1cpxcFthCrm0s2jbZvTaLVDAZDrus8Pfgg-HjpWmToly2sskjkGVkv4sdzbnYYCYoD2TxLz_WXuoCTyOO6AD8YMBeFE24K-p_bcui23egAtJs6BqKFu-oH2HyvzQLdAQ80PU9hxQiXT14-zoWVlIXqVDsUHwhblv3UwzYiPvQvHncn4pnOoKib-07d4IO2_O3ENSbIS85o6axp8redvKKw6bbcfkaNHftbGXN2jnwu9_xDEZVmF32bRo61fFyzpYjeZfAmqMl9s7W8GLWZrtyFHAvluegqJ1F4-2338667V_J6KgWU-KUsFKKfOtDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
مذاکره‌کنندگان در حال بررسی توافقی مرحله‌ای هستند که بر اساس آن، تهران در ازای کاهش محاصره اقتصادی ایران توسط واشنگتن، تنگه هرمز را بازگشایی خواهد کرد.
این مذاکرات با مانعی بزرگ روبروست، زیرا هر دو طرف خواهان حفظ اهرم فشار خود هستند: ایالات متحده کنترل فشار ناشی از تحریم‌ها را در دست دارد و ایران کنترل دسترسی به یکی از مسیرهای حیاتی انرژی جهان را.
ممکن است ایران در ازای دریافت امتیازات اقتصادی، از درخواست خود برای دریافت حق ترانزیت صرف‌نظر کند، اما همچنان خواهان حفظ کنترل اجرایی بر این تنگه است. کشورهای حوزه خلیج فارس با هرگونه ترتیبی که به ایران اجازه دهد از تنگه هرمز به عنوان اهرم فشار استفاده کند، مخالف هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72256" target="_blank">📅 12:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72254">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jONXhpK3ZYNR88BLeiD6A7yzwTd2UJ1_w8O-9tJq3b3W5ZXfu1JQupZwQkyy41TU4Uizo9UfOI-pLF9h4M8cZFg-LKpmrsCuBlb2_KQYp3KXvAb1E-kE231wymTR6Gp8J7H1V9J5nG0BUF9XK5q_SA_KVeJlN9O5xaIweTXAWYYYRqWhJhFI_1jyr9bYb_NN4CYlHN9nrjwwWBWa4NuBEcPWqS16wC5DyCHJMtIa20z8JkDkHK1v2vvW-p5ZfGHX181ou4R8JQDL0KMtBW2S8bPeV39NPZymggM129nzoOrs13EE__Nsb-X0YkCC9861Xz4azML9UImzDqyT_C-0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=YvgV3AZCYA3UcVD6a8ACe7E2TL8okMYbQ1Fl0Ct0xphGVd6wCNA4IRH9s0gArKzlHElHtPj4jhntU5QP6dimuZ2s49TxVrl31y4thfqL_LFhYalhHRkMlSUxgrGNeNaSCgUZW50WMyrRHMteEUlcutrvpTd2r94P7F3SL4oMsIQ7Kyi8LhE2ginpNc7xzmuBDshsGVpJCcg2Mq2oSQ_jL0B6n5tOdugyXaj0KHVrqT3Y6yLuF0UvcWwK49RTqMZuAUQVz83vql65h70ae0j2IHV7YYFjbn4T1T2xrP1P1Cm30zDI20p9TNaZNhZ8CGyaLX__XeA2uzv0FivDdN79YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=YvgV3AZCYA3UcVD6a8ACe7E2TL8okMYbQ1Fl0Ct0xphGVd6wCNA4IRH9s0gArKzlHElHtPj4jhntU5QP6dimuZ2s49TxVrl31y4thfqL_LFhYalhHRkMlSUxgrGNeNaSCgUZW50WMyrRHMteEUlcutrvpTd2r94P7F3SL4oMsIQ7Kyi8LhE2ginpNc7xzmuBDshsGVpJCcg2Mq2oSQ_jL0B6n5tOdugyXaj0KHVrqT3Y6yLuF0UvcWwK49RTqMZuAUQVz83vql65h70ae0j2IHV7YYFjbn4T1T2xrP1P1Cm30zDI20p9TNaZNhZ8CGyaLX__XeA2uzv0FivDdN79YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نایا:مقام‌های فرودگاه مانع سوار شدن مسافران به پرواز شرکت هواپیمایی معراج ایران از نجف به مشهد شدند. این هواپیما بدون مسافر در حال بازگشت است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72254" target="_blank">📅 11:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72253">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=guVPMTQQHDVLmNrpGNi-RfOlQHs6HBgteppkNDcyYPA4C6y401SdzZ2f7e_ofe1pzhsh2_iPFW-MY5Pc9Z1s449UUibKbnv0DXFTbPRbUpUkiN-zrf5cMMuECAzIUmo-wIMPVUBQq0VWUuKsz-IcLQbZ9DoQaoqFr2EZNCA_eX-3dTY-fbRaYSucRsiee6NsbDiqUfbQ1K5MPtd69tdUajS93JQS_9Qpkkh98GczXNubh8Q31fhe02xaso1FXVulpX1Hgf3ZMm6UxVX1DbYkB0SK15M7Ue5OTlvvcoxoFXb6MVgIMNn9wFBbSS0-kHGOa4HLcnI4vbbVotVq_YIIHBk9JYX6cH6i4gHw5LNX1YCE-HJMRpazcBIewOVXbTviGi589A3ZKhKIleBbaauNzWAJNcb6SyY4OEgfwSVjjC3JeBjeFFG6I9Pp1-tD5GpozDH0XxotY9tu9mvnR7ffGVc6YITf92D3dvDk3Rn6AUr1ek7F75vIOacXNyiYQ5eR2Uh_apz4YlYNwfcr_lHopcJYncfHWswmIc5r_Jg1JDMxG3Tw-ZHuZpzIf6Ff2HSwh8eS9FrlPhNWQEJwEuzz3gfWLlDf4vjQctruyl7A_Ec4yxfFuUmrTgZNc84yHiwF9YLremYesH0FQF1lsN_-13PL-QWBsupGdg5N3NIpzeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=guVPMTQQHDVLmNrpGNi-RfOlQHs6HBgteppkNDcyYPA4C6y401SdzZ2f7e_ofe1pzhsh2_iPFW-MY5Pc9Z1s449UUibKbnv0DXFTbPRbUpUkiN-zrf5cMMuECAzIUmo-wIMPVUBQq0VWUuKsz-IcLQbZ9DoQaoqFr2EZNCA_eX-3dTY-fbRaYSucRsiee6NsbDiqUfbQ1K5MPtd69tdUajS93JQS_9Qpkkh98GczXNubh8Q31fhe02xaso1FXVulpX1Hgf3ZMm6UxVX1DbYkB0SK15M7Ue5OTlvvcoxoFXb6MVgIMNn9wFBbSS0-kHGOa4HLcnI4vbbVotVq_YIIHBk9JYX6cH6i4gHw5LNX1YCE-HJMRpazcBIewOVXbTviGi589A3ZKhKIleBbaauNzWAJNcb6SyY4OEgfwSVjjC3JeBjeFFG6I9Pp1-tD5GpozDH0XxotY9tu9mvnR7ffGVc6YITf92D3dvDk3Rn6AUr1ek7F75vIOacXNyiYQ5eR2Uh_apz4YlYNwfcr_lHopcJYncfHWswmIc5r_Jg1JDMxG3Tw-ZHuZpzIf6Ff2HSwh8eS9FrlPhNWQEJwEuzz3gfWLlDf4vjQctruyl7A_Ec4yxfFuUmrTgZNc84yHiwF9YLremYesH0FQF1lsN_-13PL-QWBsupGdg5N3NIpzeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های یکی از خبرنگارای رسانه های فارسی خارج از کشور با معاون عراقچی، کاظم غریب آبادی:
خبرنگار:
ترامپ‌ گفته میخواد جمهوری اسلامی رو نابود کنه ولی هنوز به توافق فرصت داده، فکر میکنید چقدر فرصت دارید؟
غریب آبادی:
ما با رسانه های فارسی زبان خارج از کشور که موافق مردم کشورشون نیستن مصاحبه نمیکنیم
خبرنگار:
ولی با ⁦CNN⁩ رسانه ی آمریکایی که رهبرتونو کشته مصاحبه میکنید
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72253" target="_blank">📅 10:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72252">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=vEt622qHZULqtP9jyiQIdpzCoGjxwYzV3F_aiQZgi6qRi4xyiwMRKF9ZcYIawKaWmAf3EyPsJCG9idN_7I30Y9UkMoP42HKQPpKc8hdnTLg3giO1d9YPP8J7n77Mw9i-Fu9cxT0iCCJ1jke6Y6vqUOPI5pG52MqZDLAxCHlXQKYsHm0KPfQnEhPRvKroOWW7tbcQug8mlGlK6Ndazx1NOMteIU4t1_ixBoKbwGDtj0stm5MjdFk0wo6J47h43i5Y6OAIKittcLiSZA0dD91Bdak0gQCmXrpY2qg6at0dkI-tF8Bh1hY7DueOWDRlKZyw_K1iXIlo5voMINNobIs0yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=vEt622qHZULqtP9jyiQIdpzCoGjxwYzV3F_aiQZgi6qRi4xyiwMRKF9ZcYIawKaWmAf3EyPsJCG9idN_7I30Y9UkMoP42HKQPpKc8hdnTLg3giO1d9YPP8J7n77Mw9i-Fu9cxT0iCCJ1jke6Y6vqUOPI5pG52MqZDLAxCHlXQKYsHm0KPfQnEhPRvKroOWW7tbcQug8mlGlK6Ndazx1NOMteIU4t1_ixBoKbwGDtj0stm5MjdFk0wo6J47h43i5Y6OAIKittcLiSZA0dD91Bdak0gQCmXrpY2qg6at0dkI-tF8Bh1hY7DueOWDRlKZyw_K1iXIlo5voMINNobIs0yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس سنا با ۵۰ رأی مخالف در برابر ۴۹ رأی موافق، قطعنامه‌ای را که هدف آن محدود کردن اختیارات جنگی ترامپ در قبال ایران بود، رد کرد.
چهار جمهوری‌خواه — شامل سوزان کالینز، لیزا مورکوفسکی، رند پال و تام تیلیس — در حمایت از این قطعنامه با دموکرات‌ها همراه شدند، در حالی که جان فترمن تنها دموکراتی بود که با آن مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72252" target="_blank">📅 10:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upsLSsc5uE3Cpg3K2ip6Rd19ez14ZVoPZlVAX7dYWmjEW2-dNGjeEgZAifTmxuRCjTO2JjjzATkOA5Fy2RzBA6oev5oWczyjFeGNE0fk7xjvytxf-B1qbHFS_OL3n6Zyje5SvYfnAFoRuyUZBfXXhDGa5nZ16WnFpAVB7hx0VLLBy0F9t5hA5Xr3xO2w0rOreB74afgveV2XZ5AzLkEYPcTTRaeY7qpk6LwJlVZBwPF47ue0ms9j15Hr18EWepEERpkf1dXNwaqo2K3tHG70N_g8jbQm5oEJ7kePl65bYz_mnnEPCGlSiLfFGHarAlko5HbMEQP84LRlOeLHQNE79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی‌ نیوز:
مسعود پزشکیان، رئیس‌جمهور ایران، اظهار داشت که تهران خواهان احیای توافق آتش‌بس خود با ایالات متحده پیش از انتخابات میان‌دوره‌ای ماه نوامبر است.
پزشکیان گفت: «ما نمی‌خواهیم کار به انتخابات میان‌دوره‌ای بکشد. ما خواهان آن هستیم که آمریکایی‌ها پیش از انتخابات میان‌دوره‌ای به تفاهم‌نامه بازگردند.»
پزشکیان همچنین اعلام کرد که ایران برای بازرسی از تأسیسات هسته‌ای خود «آمادگی دارد» و هرگونه تلاش برای ترور ترامپ یا خانواده‌اش را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72251" target="_blank">📅 09:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72250" target="_blank">📅 09:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=k8Gwb2P6XMo20D0eWYeWF3gzWSli4Ug7L9nSvQl6Xsu7kQl20ykWJSim8CPqtyTfV6YpHRBRzDiplXA9SqV4IVWJuJKRsfvjA0zU3_nPRe6zMN9GII9yQdqjATJbN5FdfkPF-nfUbSQtRYytjpRAAW7cRgjzS_5vVE06r-uqr7ILYjRa23IOTXFhs0TIn_07MU-O-V_ADF1BYdBm_OFKFHVWRwMuObqzaS6UVm57luF6pu3w9cn18tCAIlR01yvJLFfUfX5gQsEhECCY-N99AyplRwK2_xBx-8AbWr_uEveGN1JWsOO6eKDTXeBCiuaIC4kwi6N0mSFO3KXl3NzKoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=k8Gwb2P6XMo20D0eWYeWF3gzWSli4Ug7L9nSvQl6Xsu7kQl20ykWJSim8CPqtyTfV6YpHRBRzDiplXA9SqV4IVWJuJKRsfvjA0zU3_nPRe6zMN9GII9yQdqjATJbN5FdfkPF-nfUbSQtRYytjpRAAW7cRgjzS_5vVE06r-uqr7ILYjRa23IOTXFhs0TIn_07MU-O-V_ADF1BYdBm_OFKFHVWRwMuObqzaS6UVm57luF6pu3w9cn18tCAIlR01yvJLFfUfX5gQsEhECCY-N99AyplRwK2_xBx-8AbWr_uEveGN1JWsOO6eKDTXeBCiuaIC4kwi6N0mSFO3KXl3NzKoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جناب نخست وزیر پیامتون برای مردم ایران چیه؟؟
بی‌بی نتانیاهو: ما با شما هستیم نا امید نشید
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72249" target="_blank">📅 08:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">با این جوابایی که پزشکیان به خبرنگار داد باید منتظر موج جدیدی از حملات طرفداران افراطی جمهوری اسلامی و تندرو ها به پزشکیان و دارو‌دستش باشیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72248" target="_blank">📅 07:52 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
