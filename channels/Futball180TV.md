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
<img src="https://cdn5.telesco.pe/file/DXS4la6HD-4NjPxFR3uS_9x919RdS_T4AckDu0wBxXbpWodE89S1KxVBemTkNMEkXcea2iYxycwHiMQte_BKdUCzbae-qZnWvpF8aU_i2GMubgOudoorEX525is7kGc86tPJJC8jfO2VgY-hDA5Le2x5GYP8itWgQ24WNcjMFaQ_7fEe2U-sDNQZGEzP3po1m0cZQVDU1vRXFnv4fCdkvYhKyC_-VZ08eOZXbV7KLBBcYscDSctEgo-0UNpMkEN5slVt-v4YIM9Up7L6YtXkbCIWHaOU1xZkXIiItTZTXkKN6ZvIPp9bqY_hd9YEfu42-kRr7n3ttar3w5Yr1gqWNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 190K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 15:12:48</div>
<hr>

<div class="tg-post" id="msg-91030">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fb78b5f3.mp4?token=IqMOkFjcRIVy55i34nbXsvdjNPa6PJCHYs-MnvFUCjgMoSDajqBAzb5O0DRJ8eC0GPtIdH7uCBpTYOdZUr1s-zDVpoVUgTCayh0PKI33FnxfjxAuHZGVF5qQZh9JosP1rCVmVchcZUqU6P4RBPnd4CAX9kNFBFjxPDefhUiAzSd6ZCQJKnb8xTTibz3PQaomoAQRbbl_7IoayvqEnK-6OL6X9ZBE-v8RRiv2hC_PnZf9xNzjuYwWQdK4zpbeKOyDuSA3-wWE_fartUt9MqXk1GqUs4f67ba_PA4kKWv-1-7rfmgIG-x7pDV03hfFW70_ImXN2biHoMe3v62RDBfyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fb78b5f3.mp4?token=IqMOkFjcRIVy55i34nbXsvdjNPa6PJCHYs-MnvFUCjgMoSDajqBAzb5O0DRJ8eC0GPtIdH7uCBpTYOdZUr1s-zDVpoVUgTCayh0PKI33FnxfjxAuHZGVF5qQZh9JosP1rCVmVchcZUqU6P4RBPnd4CAX9kNFBFjxPDefhUiAzSd6ZCQJKnb8xTTibz3PQaomoAQRbbl_7IoayvqEnK-6OL6X9ZBE-v8RRiv2hC_PnZf9xNzjuYwWQdK4zpbeKOyDuSA3-wWE_fartUt9MqXk1GqUs4f67ba_PA4kKWv-1-7rfmgIG-x7pDV03hfFW70_ImXN2biHoMe3v62RDBfyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ از یه عروسی توی کرمان وایرال شده، مثکه رسمه فامیلای عروس اینجوری فامیلای داماد رو میارن وسط و با چوب میوفتن به جونشون
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/91030" target="_blank">📅 15:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91028">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MM6eKXM_mT4N1JwDhws7HWaw3cKcxaT5Rbo2WYSzPy-i3KhWUUqmj0idDzJG1IyGzElqRmnYTVrTALgRQ_I1klnxNqZrIrpWeci3HHEvxVHVYuYTLohL0HFk4CfafeVEU6PoSaYq_s-2d3nfRFa7IgL1ftBELbO_avOma1t0T5F24gorXI9O-4jXqtDtBwBTwblNjSfvgKZHZSjUwjRlV6PKsD_iQ2sxjuL2UXIBfOMLgTz1gHuImXMJz8jXkwsoFFGufFC50bwQRCRtaqBaLFpG73tA_mo70m7MX2ypX4L4dqL_7-5OCm4HDjDqJ6uKb7Cnu43jhEnNCw4hhdpUdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9IOryRMBNo7HvRs75SjICZNHYN9vaqLZ5Q37OXnEMpSyXmKoIru4D4OXXYLmsugN_9mmgmaaOG68_n6-xNtpox6uAB2S3Td-7mNWvq5i9z5glugI5k71JEHBIMxUdllkdDqFx1jXsJ6DJwJaDOo_D1YgCSLuX58EYUREuUnvX0Pn3FwEzBRUv0HD6Hwivd-VeNRkLlT2cS4q4VLQosPCJDbdZhE8hDjp77ja8WZ0eq4rBIp9BQyEtF8xAirZDnmEukBRC1D_BVyDe1DFem3wUjhthoLDGtw4Ej3MP7VtAmu2LwBKsLQQW_44nxc0wnEf6uDrh65Q5RNxFIbw6zTyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🎙
🇧🇷
جسیکا توگا، دوست‌دختر سابق وینیسیوس جونیور: «بازیکنان سیاه‌پوست همیشه از نژادپرستی شکایت می‌کنند؛ اما همیشه زنان سفیدپوست و بلوند را ترجیح می‌دهند. هرگز با زنان سیاه‌پوست رابطه ندارند. چرا اینطور است؟»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/91028" target="_blank">📅 14:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91027">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=PFd8VIvGMYfKSj0uK6AzFORK13wL8P4KBI-4RK-O3JoQUQIWRDWsMCjSLb0FEjOqkS0tMuQtOl7YE9HUnyanxPk5aicGFtlGpR1hHSRdSDimIYtkMbp0Z_RxFhIOD-f6Uq7DyJdQLB8nYre3wDtOlqHCon6ul7fy4JEaCZaJKHZsslprYmnqBM9Fx0v8c_53ry5MvBbzC7qyzRC6uWeY1STOnhWygrLy8vt-D4QExUCdV_oWaxL5NI_tFOem0Ib3b0zvUUkkPQ8FJM6T4lH_2fRh1ESSMePV1If93oLRt6zPKCtcqhl9ErZ38hUu9h7pbU_Cy7NAjb_rf-6UnkbX-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=PFd8VIvGMYfKSj0uK6AzFORK13wL8P4KBI-4RK-O3JoQUQIWRDWsMCjSLb0FEjOqkS0tMuQtOl7YE9HUnyanxPk5aicGFtlGpR1hHSRdSDimIYtkMbp0Z_RxFhIOD-f6Uq7DyJdQLB8nYre3wDtOlqHCon6ul7fy4JEaCZaJKHZsslprYmnqBM9Fx0v8c_53ry5MvBbzC7qyzRC6uWeY1STOnhWygrLy8vt-D4QExUCdV_oWaxL5NI_tFOem0Ib3b0zvUUkkPQ8FJM6T4lH_2fRh1ESSMePV1If93oLRt6zPKCtcqhl9ErZ38hUu9h7pbU_Cy7NAjb_rf-6UnkbX-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
امیرحسین ثابتی نماینده مجلس: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد و ایران را تبدیل به غزه دوم می‌کنند.
❗️
اگر دوباره سایه جنگ بصورت جدی روی کشور آمد باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/91027" target="_blank">📅 14:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91026">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7143a2f59a.mp4?token=nFFREtfQEfbtrX7-K1JolHESDnwngz5ocobTbtw611Dnbc_qJMRZnP-05BRNxjVs8wnZ_NP_yy5EFa-qYwU2JDv2vjuUTCLPkCGMVGwi5ZuqigA5V-KhAZ1vfnzXVAoi9UWZgbwEQBoQexyrr8-EhKkc3-9R9TPHPuPxM2_5L_Bk6ArmcIzxizB5Z2mlgffk6pLRH2Hv1t01phqyuW6DMsAoF0lN77jiBFCZXOIrgvx5UvOza5sI5ipqVrSUr-5fsgMXYl-g99XM509CMSHZWuEAiG1Q-DHkjnw-d7ycOVmnIKohUhTquIaPJ2JRInwJON30WycEtzY4EDOGWUJ0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7143a2f59a.mp4?token=nFFREtfQEfbtrX7-K1JolHESDnwngz5ocobTbtw611Dnbc_qJMRZnP-05BRNxjVs8wnZ_NP_yy5EFa-qYwU2JDv2vjuUTCLPkCGMVGwi5ZuqigA5V-KhAZ1vfnzXVAoi9UWZgbwEQBoQexyrr8-EhKkc3-9R9TPHPuPxM2_5L_Bk6ArmcIzxizB5Z2mlgffk6pLRH2Hv1t01phqyuW6DMsAoF0lN77jiBFCZXOIrgvx5UvOza5sI5ipqVrSUr-5fsgMXYl-g99XM509CMSHZWuEAiG1Q-DHkjnw-d7ycOVmnIKohUhTquIaPJ2JRInwJON30WycEtzY4EDOGWUJ0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امباپه در ترکیب فصل‌بعدی رئال
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/91026" target="_blank">📅 14:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91025">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKEafMEN09GeMpLdPEZ3Z9r1SZOnUqsbvzdb9Do0JU42z4ZSWSqXMwXcwpjn4ep3sD9aPf-2UGMkS7pK8U4_DQP5r8Kd1HHyWAfYWATxrn159FW52DnNM-fU6A_ZpnTfJwC6vQdLXp6RKWu6PvEIF7IL_I6VqXKO4IpnLtKONawMhscc6B_A2gCUasgYzUCyHYc8gyc9yTI4Y-YwdRbImlcVyNPzR9CB_TNX7tY8FvLJ4JJ_V3NAqHcOLBkJxpRgmk5SC71tPZGsSQprIiuQZf9XECV2xIatEvH2NAASsaOo6P9-684kkp_f7sb7QuvqarCer1Vkji8FzNggvwEv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تلگراف: با وجود تکذیب‌ها، فلورنتینو پرز برای جذب ستاره بایرن‌مونیخ رقمی بیش از ۱۵۰ میلیون یورو پرداخت میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/Futball180TV/91025" target="_blank">📅 14:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91024">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ روزنامه تلگراف: هدف فلورنتینو پرز جذب مایکل اولیسه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/91024" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91023">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFonJw0zwgzaCxfZ1EEsK8EiLxuViwWEQxZq0VfI_wdtC2mM6_6p4cfeeqc37q26_ajJcuXok1Hdk829VsSdeYaeUCV6OICJx0SN1qO3PH4xrB2eOE6MisETbmbZMso9tYAi6UVOvBrsOGxoljqBCi2vwqLaVtrV8pxzKoM76W7DMeSKzwqzKrry0FTBSRS4_WqgZJ3SwlIyLxm5cIQelXh5GEu2eRAl063sVCstrKr8mXLThtsLPNBARIb4d0okrw_rAZpt2Un1VhQAflNcaFx-1KxH3ddTAxeA9xEVb9cYvPLtPT7rgcMWIm36AfLE-qjaAp0RwQfw_uU5Y7lmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ روزنامه تلگراف: هدف فلورنتینو پرز جذب مایکل اولیسه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/Futball180TV/91023" target="_blank">📅 14:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91022">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJHp7oNEVB_bKcOZ0KdPZcrCF4_ZLC_KSM4TbF47G1fNA9UnB4dwmtvg6QTZchtV_EgXx2BNv1nBkytDjsYdKizyA-QvPoCKve_89MEy-pEyirIrHkPH6RQ_xZqZFxBRAr3gcUdyvYG_lPqbjabgpPoai0_tphsyRwnPoUg7G6ys5HOz6psk2qtK1ssPRO1Bvb0-KvTCSyA4l9vF87AjbZPwHHpF-Gn8u4T1kO8tJDfXgY4JkbbKT0sCM--YkChz68Pxvc0FW5NTmDwWwZzEmy-28ggbxiLx9qXGzHaxgxSLzC-WvdhE6lk5zUTWZbiji-Mzk4qXXx157_d8JQqqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان هر چند وقت یه بار هوس فحش میکنه یه استوری میزاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/91022" target="_blank">📅 14:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91021">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e1282030.mp4?token=N42aJ1nT5-cba5sk91TxOKYXujixYDLkLyc5VNQVL8LibCSTDx1WEWbagPto4bsv-mZ3EbWML2gbTdI5purcX2-oonT5BsLk-MROEDodwq0JyVnlj8cuSl-eit0sozi-iPJcXTWKY3oNExZXUagKq0Wd-W-H0W8S_snbR4ICCwEIWbkWk_cC9OfIepioT1aWtXDA3f_8EWuNvfW5L03NftMJGKefRBqYcaRaXOb_qor9-XyWzhyJwr5RUgIYmbIhVl_G7gRImqXaJBO7k3PVDlP6rcuumCcbybKxRQE2leqLZBGrexavJUToK6hVuPjBUU95IoUuJR8Xbc8kob6zlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e1282030.mp4?token=N42aJ1nT5-cba5sk91TxOKYXujixYDLkLyc5VNQVL8LibCSTDx1WEWbagPto4bsv-mZ3EbWML2gbTdI5purcX2-oonT5BsLk-MROEDodwq0JyVnlj8cuSl-eit0sozi-iPJcXTWKY3oNExZXUagKq0Wd-W-H0W8S_snbR4ICCwEIWbkWk_cC9OfIepioT1aWtXDA3f_8EWuNvfW5L03NftMJGKefRBqYcaRaXOb_qor9-XyWzhyJwr5RUgIYmbIhVl_G7gRImqXaJBO7k3PVDlP6rcuumCcbybKxRQE2leqLZBGrexavJUToK6hVuPjBUU95IoUuJR8Xbc8kob6zlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شهریار مغانلو:
میخوایم با ۳ برد به عنوان صدرنشین صعود کنیم!🫪🫪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/91021" target="_blank">📅 14:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91020">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cf842d659.mp4?token=Y5-T3U_koupFs_2cEcgyfV8Ii_pItugMU31PccRXGi9I7ORcjKBzSpDbuIXYzUA84UMB7Lr3PtdtgYnejijoaX2mJt6A8aAzJuOxVEuS-22_4rbtQW0ncXtQMIxnb9dEhRT7RTH55VcijfQL4m7wXJDO0LzRaXfamiEn0HB9xhafeoWWWsY7N-etjCgU_W5uFGXnogM6yFhIS67wKXWIdWhPHA0y6opxa9MCUhYZqQWV8lse3ZY5cme2YDV8waMXxXsq7_p2jT5ufjLppYl9DSMrFicD5N4ZnyZqqJ2LB2S5pKZgGc5JR90o7odVabiEszxN-lHasjfGhzs423jsEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cf842d659.mp4?token=Y5-T3U_koupFs_2cEcgyfV8Ii_pItugMU31PccRXGi9I7ORcjKBzSpDbuIXYzUA84UMB7Lr3PtdtgYnejijoaX2mJt6A8aAzJuOxVEuS-22_4rbtQW0ncXtQMIxnb9dEhRT7RTH55VcijfQL4m7wXJDO0LzRaXfamiEn0HB9xhafeoWWWsY7N-etjCgU_W5uFGXnogM6yFhIS67wKXWIdWhPHA0y6opxa9MCUhYZqQWV8lse3ZY5cme2YDV8waMXxXsq7_p2jT5ufjLppYl9DSMrFicD5N4ZnyZqqJ2LB2S5pKZgGc5JR90o7odVabiEszxN-lHasjfGhzs423jsEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇯🇵
ویدیو منتشر شده از زمین تمرین کمپ تیم‌ ژاپن در مکزیک که کیفیت خوبی نداره و باعث‌اعتراض شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/91020" target="_blank">📅 14:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91015">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jb_zhLThUCgLUcLSt66kU8WnJ3pBcR9l8eliSR4_DDxX4wz0L412zlG4LiX5gLPVjmD6NOopu-cgAJrjjCoFcsTWLf6l-5H809p095pBfwGnlNp3hyhvO6OZOWKKozG1NeoyCLA0qR4MAqMWwnD9x0-eQM8PMy2xT5KjuVzmcfcw2Z0OaR3HnyUUTtYXwf4ROZSb4gJiHn3CbpJPRbtOh9kCTI2ewYXFyw7V5g_NMSxigiiCEJESjS2-MZl0JIBos8-efEeDu0kEkfvpizmnMQ_WfEUpC5s7PnUB3CyolwICSXjcKYqqeLci1-wrjW1KRnyfogysPrtct2yob3FLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMSatLVANNzK2GSOQpXe4EVirt7yL6ZUAKSZtY7LLGVQOEXeM0sWvMK-ZX_VNRCcH3QqqOzfch31Esgwgm8WyoJOKK3N2l5Qr0yLWeVq6b7TqKJ-gzt3ZPqPFUtxVKTQutA2g__6Ah2tx3sgXCDGPcegd9pcgu_iqyp1djbsa8XIKJibJIgGyZ82iUlhw94t6lVaEeVgD6Ly5vHrkX83XWMcM82yAw6i6gew7hdLjk6cSMTlmRZm9NhfBnWwJQ1oNRXlI0RDi5FnXmsxwBrJgkoCbybRu9VJinYZvnqiwQuyHbu3itVnv3sbT3Sxjn2BO04CaLXn4QXs1207Gms5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSBJlfh3AqvVA3DhNKEbk4WuxCFJnjM1IBt-tubP9uBhxqOLttqCkzPZi1jFDZWKH6heJVuZcblnp5AvvxpM1Uu3McQsoAK3nUj_gZKmVMvX-C46h7Lc7-LpmtPIZOaDxnE4YDR-56GEWpoQySnvutZ52lyKqHYu4DL7szwbtrCS8V22Vs-iNtm1MTZP30rmW0QRDNrfjLH9IvFB4YRM2a9b9FYOvvUiu_btkmH_V0r9QZm3vBdK9gefojGyMgsqUoH2c7NcMGoARDlbR9KNkfRag-WqxVMndXNiuCjmmprWdtU3IDNQf0xyyRmo77Vn_WzK5mzmRncVgGjOhn_CjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEHuTFB9WKJpapjbj99me5W6PKj3CE6eetE1RSBtk8q0wtOESsh6HWQRegRwCO0SX5j7-CLZF_G9o3pTw4kR1fUX8NrhjG8xR52A4gOY1B7SLkqQj0ru8loAz_n1_4UbUrGmqkI5mFJ6vzqYvfGj2KO-pZEUzGFOx0llTbwNeDqc9-n7dFiZ10eyP0PlwvrnpPpZCUzfNn6jEsjNboqu-LBzQibx-ddEy78zb3v4hmQ0NhC4D3hULvVujzMQhaLPswcOVDSrvHF1k9LqnMAt41J9YVlyx5t_OpbWksas3wBEqui9sHZviy1u9cSmrXrq5D8-1lBqhUFVXL4YPvCL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4sSgxOGmyC5aJCMt0twiQoL-en6-IrjGOuupRaFLJd5cQzefX_ZM9T8fNz7HyhbRqA8Ra6JF_E-yaRlWhb3ko4HhzNQdpercAqSoo_1RaVFwUJ15U0bms6DsWYdRdGxWVP6z2fNxKXl6gIYltPNV_goMkJ0tRw5o5HfIB_jrgOG5ukKwMXnDNlnMHkloBU-U36BBbjGc6C7PhDvL_TChVLVURDM_Gfo9qWHxmmPvMHu0yscOY0vTrfMGtPm6KK3UI0t70tfceeJRJVsYrqPSGNs1lZjSFbuH_o8hVk0SAP7dtmyxspVMoJ1rtb97MgHxajnhGGICUrk8jRfW99O5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
هوادار روسیه‌ای در انتظار آغاز جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91015" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91014">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8abc04017.mp4?token=E1vrTtPUnkzryXYwROnRGhv3g2DTF0zW0DRqyKk_lk2i-VXnDs_gl4thYqWLd32Shxr7aJV0y9YzY6F9c7lu0fOM2QB9qdiB4mZRBQQ8ocI1oIIpCQT68XCDn0RpkNv48DBgB0EMRCbE4OTuYod9c-TmpU0PCd3roHObkahMaqpkCw3lb_reoxZGe7f2wg7_IIn46M_PP9tGc0aWQ545Kn9RSnlSp8lr9rrcLD76Mlf3syUXPYqNL5FsFX_jbF6w7DOHKrZdeo6GDXdtd-LaQIjQ4SoiS6CPAEKlQQOe6Bn2EpOw1_AKe_S9jmMKy8fk5jOsbb5ckiShLXRe2SsaYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8abc04017.mp4?token=E1vrTtPUnkzryXYwROnRGhv3g2DTF0zW0DRqyKk_lk2i-VXnDs_gl4thYqWLd32Shxr7aJV0y9YzY6F9c7lu0fOM2QB9qdiB4mZRBQQ8ocI1oIIpCQT68XCDn0RpkNv48DBgB0EMRCbE4OTuYod9c-TmpU0PCd3roHObkahMaqpkCw3lb_reoxZGe7f2wg7_IIn46M_PP9tGc0aWQ545Kn9RSnlSp8lr9rrcLD76Mlf3syUXPYqNL5FsFX_jbF6w7DOHKrZdeo6GDXdtd-LaQIjQ4SoiS6CPAEKlQQOe6Bn2EpOw1_AKe_S9jmMKy8fk5jOsbb5ckiShLXRe2SsaYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
بانوان جذاب اونور آبی موقع استادیوم رفتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91014" target="_blank">📅 13:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91013">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b018b6c88.mp4?token=LjSlfg2GdrkwLBJzPB3Hnlv0laDkYPSPffEFeApJ6jEwvOMkqs0SzuABhkbKX-c7bG0We06fS_Ea5LbjHlLW-lJZ7h2RRpZkpNutghdhr__iYq4LOi48qkCee3evk-_t5E1Atzrl4JBUTEyXtC8ICQIILK83gTG2CvBcG2BBP7uzxkNJFuXVxgXdArsoP3D3lxRG3ghgo0LRPN5OdxLoHAW5BK59D0FcNlW_fNFImHabanq5bxa9ylatVZrAq2ffIQy1uXUEXPmkH1X5MDDRLVOj0HCm8qhhpEWQxnQFnR7al3870skyfNv3qyhWxrm-T0JA_VjZtQnXrI7F1izWJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b018b6c88.mp4?token=LjSlfg2GdrkwLBJzPB3Hnlv0laDkYPSPffEFeApJ6jEwvOMkqs0SzuABhkbKX-c7bG0We06fS_Ea5LbjHlLW-lJZ7h2RRpZkpNutghdhr__iYq4LOi48qkCee3evk-_t5E1Atzrl4JBUTEyXtC8ICQIILK83gTG2CvBcG2BBP7uzxkNJFuXVxgXdArsoP3D3lxRG3ghgo0LRPN5OdxLoHAW5BK59D0FcNlW_fNFImHabanq5bxa9ylatVZrAq2ffIQy1uXUEXPmkH1X5MDDRLVOj0HCm8qhhpEWQxnQFnR7al3870skyfNv3qyhWxrm-T0JA_VjZtQnXrI7F1izWJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای‌کاش اینترنت وصل نمیشد اینارو نمیدیدیم
🙁
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91013" target="_blank">📅 13:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91012">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Otjabr5Xj31yPBzOKNgW4k7camrX4qfERW_Sa2hsRQj4QQiVIoDXPAhdwN8M4imW5aT3ftNhRy6APDjiZhM6j-bMFO9Kf7-gjNCT7poKpVPw5arqoaatkG6H2d7APEUUzWb0qcOfyE1MNGTx76Rx3IbehrtqGgjFPzS2NkjzYyigkbZU14o_-YbxbnWqZz_wb2amsE8wEkJwyRyhEPXkLXzpagp_ssJxf8-Dfm6tVNrtDL543iCZ6hDIEKeWn9Vjk0T-8_KaFmQfLF4ak9C6BVOatIJ0VjRnpMEbcHx3446fci5H4tqtFTu2Ao5NvUlakfMxO_bCeX7PFH2WcGTcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇪🇸
#نقل‌وانتقالات
|یوونتوس درحال مذاکره پیشرفته با اتلتیکومادرید برای جذب سورلوث است. در صورت خروج این بازیکن، احتمالا ولاهوویچ که قراردادش با بانوی پیر به پایان رسیده، راهی مادرید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91012" target="_blank">📅 12:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91011">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
‼️
🎙
افشاگری نیکبخت‌واحدی از پشت پرده بازداشت مجاهد خذیراوی در پارتی شبانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91011" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91010">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137c5fb470.mp4?token=ka3mUfwqwMZEfNfRrDHEFPg7w7pcQuD3THtgxmLo0d6XOAObulBF0WNOZaN8uGeiXjH0C7mXAgsP884OkNTIzAXDrHb59N6Nv5xbcvuQ_jvbLcR6879ygM4rCHUchOVnMGOawefDMDdbx3l8lHC1EyYCeRHoSpfJ93VnGmebp9gpj1LaI8TLDlCPXf18e35ckDtgtzSEtvJ2MK1cTvLuhGPO41dC474ga44UDEJtak69WqwkW-AvABzZGWnIQh60eFKv8Z5RCVu2dfGTGEORJo-i8jDn6WELcpGfsc8RhwilamHxPhkyu9cYMSLest3Rv-3uz1VCmaQ5qQs-CX5eZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137c5fb470.mp4?token=ka3mUfwqwMZEfNfRrDHEFPg7w7pcQuD3THtgxmLo0d6XOAObulBF0WNOZaN8uGeiXjH0C7mXAgsP884OkNTIzAXDrHb59N6Nv5xbcvuQ_jvbLcR6879ygM4rCHUchOVnMGOawefDMDdbx3l8lHC1EyYCeRHoSpfJ93VnGmebp9gpj1LaI8TLDlCPXf18e35ckDtgtzSEtvJ2MK1cTvLuhGPO41dC474ga44UDEJtak69WqwkW-AvABzZGWnIQh60eFKv8Z5RCVu2dfGTGEORJo-i8jDn6WELcpGfsc8RhwilamHxPhkyu9cYMSLest3Rv-3uz1VCmaQ5qQs-CX5eZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیدا مقصودلو شیطون شده و میخواد با پولای ددی مورایس موزیک ویدیو جام‌جهانی منتشر کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91010" target="_blank">📅 12:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91009">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWrXjTWKerXSsbmPd3iu3b3VSDodJTJcZ2AF58kC5-Hum6fK-f6-_VV63B32KDQCqsCueStZ4fTpCZxC9xm7YaDMqFOogORkWMPI7m9mR-e_CBM7PVlIHFHydzrDRbCNhV1aAAlN8BkwvMXarxTxp9LgjvPgvh-sly7TlUQ8gSSqLbNP5p1NlPJhORz2pyEzRNcUUK0T0hJgdIuUtE6x919HMYXx32BXhp1nnWOQejfoTOCYY44jxiLJPN1aEMJfKnIanAo-n8HYnxpgoKM_z-eSXoI7ayYe4WnRI-kOet0sOky8chWd1xt9oyy4ZRoNQ-EeoFmPxFok-MRD-N6G8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇫🇷
#فوووووووری
؛ روزنامه الکاس‌قطر به نقل از ناصر خلاف: ویتینیا و نوس به هیچ‌وجه فروشی نیستند و رئال‌مادرید باید قید این بازیکنان رو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91009" target="_blank">📅 12:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91008">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c4d39e7f.mp4?token=XoSPNyFasWfnZQHtAPhI1olOKM_Grm_Sd1p0nV-1ar_pmagJJet0dAO8se_8BODiZYoTeghBQbIbSwiuwfhJd6VlIQSCX9VNViM7jlKnPdqTn6g4twcumZrpiPAozIdiGtm-FblMLgFuod21olS3LEj6CRfnuw8Df82WGqVOfMCGHk3LnLvEW4HRx5joAG3jbRr25Enk-HHX7GGnLS_QcJXzP2s8Kqg6yY_X4ZyblR_aWzQ5O0xr4WU35aLd0r5QZDzOjoUtnmYyfeDcraGpYJcOSxQY8_kG55RJ7-AzhIDv0CWoIMm0pucMtAa_zWWp_bGmuMzjXRPa9L05TMzDfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c4d39e7f.mp4?token=XoSPNyFasWfnZQHtAPhI1olOKM_Grm_Sd1p0nV-1ar_pmagJJet0dAO8se_8BODiZYoTeghBQbIbSwiuwfhJd6VlIQSCX9VNViM7jlKnPdqTn6g4twcumZrpiPAozIdiGtm-FblMLgFuod21olS3LEj6CRfnuw8Df82WGqVOfMCGHk3LnLvEW4HRx5joAG3jbRr25Enk-HHX7GGnLS_QcJXzP2s8Kqg6yY_X4ZyblR_aWzQ5O0xr4WU35aLd0r5QZDzOjoUtnmYyfeDcraGpYJcOSxQY8_kG55RJ7-AzhIDv0CWoIMm0pucMtAa_zWWp_bGmuMzjXRPa9L05TMzDfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
صف کشیدن بازیکنای عراق بعد بازی دیشب برای گرفتن عکس با لامینه یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91008" target="_blank">📅 12:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91007">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0U_owUHpRy_syQJp6zcssb-qh-2H6RKK0Qs2QNF8mCevCN7PXrDOuK_2PHABCo65hUsyun8xbSRDnLXp7A8vU4vs6r6S-1RJH0SlIGpDG32ixZLGZzu9d40J6b_OcEQQ3kgiSBwzyEhSQnalv8fDaV-DS4lo_doT4ZXyHPW0Z4OvIaepFxWK-to32yVZEqVrOubGAUouqsigIsCqGpv3D40xxTrfrbibxyDsOyMlTy9Tjom4W5kMx81apBbqMqj-3A5m-zM2ezNUGwCKtmJgPGMaHNxKWEpgSQ8Idq6AP8zLjW1jRoL_WnvBJ7zvnd9IPXh_mRedapsyM5sQaoWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظر آموزش های آشپزی هستیم دوست عزیز
☺️
🙏
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91007" target="_blank">📅 12:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91006">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b863e17f0.mp4?token=X0w_LGpsx20dVYMzCGu5xQrlhMcSdYN3Vbn62tvKE_g0jTIK2kcDcBN5XYTA-SfVxHv8SkkSnZgxzAit5nNH06CY0aNzLwnPAyCo5C4gsb2gU5j-tZubfCMvGD9xefA_VXUg_J0FDs8ZFP83bkfogeAk5mTLCa-8O8yvySzsjriuLFs6RBHjktpI7vQuFF_GPqIXSRtnD0aTeW7n3syKmcJr6IBENNMWYUnEJr8GHZ7if11ltkhTUktekh5dh4rwjNbWZ6o5ZRkiXOoIkf5DXdhTDXXSj7dyukKvKaUDQ-lPwfwo7lx4O91CQ3_x4xm7Wi0KmiiFVBltHZutY3ZpMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b863e17f0.mp4?token=X0w_LGpsx20dVYMzCGu5xQrlhMcSdYN3Vbn62tvKE_g0jTIK2kcDcBN5XYTA-SfVxHv8SkkSnZgxzAit5nNH06CY0aNzLwnPAyCo5C4gsb2gU5j-tZubfCMvGD9xefA_VXUg_J0FDs8ZFP83bkfogeAk5mTLCa-8O8yvySzsjriuLFs6RBHjktpI7vQuFF_GPqIXSRtnD0aTeW7n3syKmcJr6IBENNMWYUnEJr8GHZ7if11ltkhTUktekh5dh4rwjNbWZ6o5ZRkiXOoIkf5DXdhTDXXSj7dyukKvKaUDQ-lPwfwo7lx4O91CQ3_x4xm7Wi0KmiiFVBltHZutY3ZpMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور مکزیک در کنفرانس مطبوعاتی یه توپیو انداخت وسط خبرنگارا و یه خانومی انقدر ذوق توپ داشت که با کله رفت تو کف سالن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91006" target="_blank">📅 11:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91005">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8de806e44.mp4?token=Ded-9umeAAI1VelVTgxtfHbgAF5oEjc6jSXXitoCsm6hwr-XQ4YD_Afbbcr3KD0xSUpUDUNG9xMTfidJrrSrtuV1_Qog3-AeT7JxVR2kXIMB8IQi1FeomjlwtQmHqAOVOlYLs69FCPuIy2n8ZEBLUXj5JoUW8X5FXDGlO6wA-CGYQEy6hR-DLrB7tmZbAz9wqDJwNBqwxIwyUJDU5XMW3hd6ZbSYX0yMGPySdkkRl-s0uxY5lvkeV9mDF1eEs8etdiLI35weVPxo-TjXIx3KQ6FMbNgqje2QWfgV15W8yjEn9FMiqE2CQjrfqmUbW2MjD5hUfGeGAIMSu-AsVItEjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8de806e44.mp4?token=Ded-9umeAAI1VelVTgxtfHbgAF5oEjc6jSXXitoCsm6hwr-XQ4YD_Afbbcr3KD0xSUpUDUNG9xMTfidJrrSrtuV1_Qog3-AeT7JxVR2kXIMB8IQi1FeomjlwtQmHqAOVOlYLs69FCPuIy2n8ZEBLUXj5JoUW8X5FXDGlO6wA-CGYQEy6hR-DLrB7tmZbAz9wqDJwNBqwxIwyUJDU5XMW3hd6ZbSYX0yMGPySdkkRl-s0uxY5lvkeV9mDF1eEs8etdiLI35weVPxo-TjXIx3KQ6FMbNgqje2QWfgV15W8yjEn9FMiqE2CQjrfqmUbW2MjD5hUfGeGAIMSu-AsVItEjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور با انتشار این ویدیو نوشت: و شما ادامه خواهید داشت...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91005" target="_blank">📅 11:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91004">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czWrgvN644A9BsDJMnPVLW0RAjITVu8wern0C3-Uao3Lcl_pWHc6LHP5NeokxivFe3qB9uLIXI3xTeO52rPrpJVuDgZ2PfQVxzOCaiuxorKJSaqfWnwAUGaJ1CLRWsrc-iaEeRWTKL716OcmujP1Z0_WF4aHUXVOok2ft0zSWOhBaq-x_RM8WhHC4fwLzmucbVw7_d0WOzdVdM8qeSI7LHeG3zKuGmNvjl0jd_em5lxeJpSZqORim7Gvdf_5ygsqSuU8Bz2gU3KddA6I7nRee4Jqvnpvgo8eeC-IWqh9cOBtWC9joodVnhgW9ZgYwtCw0x0iNoIiFy2fv1HvrRGZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇳🇴
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91004" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91003">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae875521b.mp4?token=FQMYXBpCuVqxZygEu7oihCtqrzxSXVQYMu-sjutHz8ME4AY1HJ_tBKZ2m3NqD9V5SBKv9U9IJ-LNEE39xCu2Acs4eB7P-JI56c8zTsMVOFOLZSpnlVr_27JpYs8lkG1ll55huUL3S8B5mtpjER1emFjH6dznpBJit1N5nOhAx_sFcEC124xxDQIcUkjudytJtp5nUHWpjH2l546BMK8qv2aOWkJnNaNL035wOqcwAkUh8el765risIIZ0agw-dxAClDN7zqqY8xki1N_rfLoxFbMd5YEJld9fUGve3YskDisfTuCOkC4JmgnpttZZMgFsN9AbiGeNh4XVLHPz6gUsFa7z8B-E0jp6U1Hjv0F0K72wIV1zCp53xU3AKaYQLmpu08bdM1NjFodN52lC5IB57NZGKOYm5-o3N9o2Kj3fx81YrY0-UwMJ54QoYP1w4rWw7sLIzC6KXzK4jGB-B9OXdRoM4tvO80rPuFQkJekl_OFZZuoXXwr6ISJl5pon6ovpv8Fwdmu0wiECLd1_KvMOYYqXkwTqtgclQ2JynAysKe7064W470JjyO1rH-9VBZlwANIrMSfmA-Fvxy1PK1ddWWchi2RTPJIVj7BogQPaTe9m_ywI_yZ7puSU25p4bmh6KZlheLZZ-xJ9YXUC_JIKdv-ytbWmMI5gXNHdV4HCvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae875521b.mp4?token=FQMYXBpCuVqxZygEu7oihCtqrzxSXVQYMu-sjutHz8ME4AY1HJ_tBKZ2m3NqD9V5SBKv9U9IJ-LNEE39xCu2Acs4eB7P-JI56c8zTsMVOFOLZSpnlVr_27JpYs8lkG1ll55huUL3S8B5mtpjER1emFjH6dznpBJit1N5nOhAx_sFcEC124xxDQIcUkjudytJtp5nUHWpjH2l546BMK8qv2aOWkJnNaNL035wOqcwAkUh8el765risIIZ0agw-dxAClDN7zqqY8xki1N_rfLoxFbMd5YEJld9fUGve3YskDisfTuCOkC4JmgnpttZZMgFsN9AbiGeNh4XVLHPz6gUsFa7z8B-E0jp6U1Hjv0F0K72wIV1zCp53xU3AKaYQLmpu08bdM1NjFodN52lC5IB57NZGKOYm5-o3N9o2Kj3fx81YrY0-UwMJ54QoYP1w4rWw7sLIzC6KXzK4jGB-B9OXdRoM4tvO80rPuFQkJekl_OFZZuoXXwr6ISJl5pon6ovpv8Fwdmu0wiECLd1_KvMOYYqXkwTqtgclQ2JynAysKe7064W470JjyO1rH-9VBZlwANIrMSfmA-Fvxy1PK1ddWWchi2RTPJIVj7BogQPaTe9m_ywI_yZ7puSU25p4bmh6KZlheLZZ-xJ9YXUC_JIKdv-ytbWmMI5gXNHdV4HCvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شکیرا از ارتباط عمیقش با جام‌جهانی میگه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/91003" target="_blank">📅 11:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91002">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwdzxk20RPi296LZwGHw55A17Jxse7cBJf5z5ALL8yaetht-f0oAMeaaOOB3X27qECn4vCnoXqlaJNjAevquABwQ0ch47HrzyzzS8IsCEbS0p1VCI0ABTvl4jvCEoWxfQXWPHi4KWjvUKsdq0KqURazA3y95J0f5zGPtvWMCW0-OMkAFyRmFGTwZDxn47NU2V6sV8cPr_TYyNFm15nJsBsatD2dCcwWCUJXl8cXvaYhiz7Kwujhe6LDI8C7ODZNTwZixyctUMEoZ2nLnqgUXZeGKGjS7WxEfN6gCjdymR2aZghOz9Kkq0OI-aHpMrK5ywA1ElaPNam1BuliL0Vpvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇲🇦
پشماممممممم؛ رسانه‌های مراکشی میگن که یاسین بونو گلرشون در آستانه جام‌جهانی با نورا فاتحی بازیگر هندی ریخته رو هم و به زنش خیانت کرده که شدیدا در کشورش جنجال آفرین شدههههع
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/91002" target="_blank">📅 11:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91001">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1356d4c5.mp4?token=MJLeOtFVKib8GPuhEttxy6h7lNgN8s42dhLLvsRCldUJTxc8BdoV_0DuMYVrJuabGtERfxEYVM0rRKm_jeWKdcRb6iS4ckNWbSI_I18T8aUgovI_h4HNWeMD5qIBlIqR3rcjR5s62nG-ujKibXmQvoMi7Hi1hiny1_T9tjGBQ7rhZknSlKwCzdCRYiMtMKE_C-CdrxggLHG8NQd5KP9daM6s0_oq0-TZ_lCBGNj80xQSNvT4e1_hdUlFbZ3ZbS-tStlImGEgohnB03biRwaAadUO8Fbz2Zj6Z6J8H9NQuLppU9GjDFtqi7hSG_L5LM6hYscioRWNm1SfpR0Zy_34Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1356d4c5.mp4?token=MJLeOtFVKib8GPuhEttxy6h7lNgN8s42dhLLvsRCldUJTxc8BdoV_0DuMYVrJuabGtERfxEYVM0rRKm_jeWKdcRb6iS4ckNWbSI_I18T8aUgovI_h4HNWeMD5qIBlIqR3rcjR5s62nG-ujKibXmQvoMi7Hi1hiny1_T9tjGBQ7rhZknSlKwCzdCRYiMtMKE_C-CdrxggLHG8NQd5KP9daM6s0_oq0-TZ_lCBGNj80xQSNvT4e1_hdUlFbZ3ZbS-tStlImGEgohnB03biRwaAadUO8Fbz2Zj6Z6J8H9NQuLppU9GjDFtqi7hSG_L5LM6hYscioRWNm1SfpR0Zy_34Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تو مراسم اجرای حرکات نمایشی ربات کنگ‌فو کار در شانگهای، ربات کسخل مسخلش در میره و با لگد محکم به شکم یه بچه میزنه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/91001" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91000">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiijI7RlfLrSm6zfiLhBhDX4INEihmJvL1-_mqIhM1MBorqpdG-R7-I7uCwWA19RDANK9kOHLtG-Oz3IvlNsbAiUcCXiy_zjtkh5JQrVClwgW8WpXgVzPMnGqaDDzkN9pFjnypPtAhNJvo2ttwwN9q1YqAimqFKTYluGmQtOIlmdkXDg8VRPbIWFRStiVjOyMtmygkTQOZYuDO-oYDu5ZuokkWsyWFD9w5h-yZbdAnd5NVSSewT_fNb0WHwmF5arKpxgkaMA8KYI9B3SCPhveJOr2dQV7MxUzzRGB9OjY_qUHZCVxvW05A3WhRpwuOv5kw7rkyKaK2zhAgPMzUZQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو دنیای امروز به بالایی میگن آفریقایی به پایینی میگن اروپایی
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91000" target="_blank">📅 10:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90999">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1b7afdc1.mp4?token=cIieW2VRm7w9Sxg2fn2kPS-_eB8oDYEENDwT20_yj7c9Jyj6o7VgewVWSVNGj7dP9S8X_mTxUNEhIoK24ElQIiHc0cxEWr0wwMbO-5uU4H-MpJU_263cDpgZQ8tL7kDh0yBeseYhlu2grWf7o_edmRBx8ggtORqhy0LKeHZKoZJaPo0XIMEEqfuS66Uu4nWTcmZucle_3rPXjmBn0GVUD2Am2mcOBw4QaDnf20ZOzhYgCb7BiDi_PFQyJuZ1ylyrJO1-gNsGrgHTPnTdxDQuS-iq1lyAuNYH2mUpN9CU--sQIroALcTCC1lzLRIqfK0o-FKQABwuAjSqO76lBEjBdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1b7afdc1.mp4?token=cIieW2VRm7w9Sxg2fn2kPS-_eB8oDYEENDwT20_yj7c9Jyj6o7VgewVWSVNGj7dP9S8X_mTxUNEhIoK24ElQIiHc0cxEWr0wwMbO-5uU4H-MpJU_263cDpgZQ8tL7kDh0yBeseYhlu2grWf7o_edmRBx8ggtORqhy0LKeHZKoZJaPo0XIMEEqfuS66Uu4nWTcmZucle_3rPXjmBn0GVUD2Am2mcOBw4QaDnf20ZOzhYgCb7BiDi_PFQyJuZ1ylyrJO1-gNsGrgHTPnTdxDQuS-iq1lyAuNYH2mUpN9CU--sQIroALcTCC1lzLRIqfK0o-FKQABwuAjSqO76lBEjBdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇿
عملکرد دیدنی پسر زیدان در چارچوب خط دروازه الجزایر در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/90999" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90998">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwtaxoUyjQqq0fBrUXgA-1rBMsgxuTh0XzzntJEKcTq5Fs9LvLEkmL-SVFfktHuVk_s4wTRVk48EC_Az1ZRmAmWvDkxq8RBGXyV_YPMnHZoBpeePm-aBls49Yu0DfRpNcDrJlse7pZOaicau-HwWfiBLcnjr7Ob0FJqkWl0-J8920zrWZJwbJAlmrTT6-RFMZ9E4JUpaCsUV4REo3u0gNRulqNWOqi2BUvge5irDzMoIBE4ZogOXvnxqQkYlyKySDCCcLqfFTlZE9aNF4yPlMYfvS3vfxZsGwtUoAq5PXzDry2e2B5UsZrVRfpCcqpXNd1xWJ_PGL6e9mj4bu3eeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنا د آرماس با کیت رئال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/90998" target="_blank">📅 09:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90997">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDA-Mt459xfaLhuh4IM708L3PZoY34QC51MgWhQZRp5dup6mCWR305rnxNxeiulvg5iXC5YgY64ODJxJOLxpakbCbHzFbhiG2q6dSzldRNjKq9i-SeKpEUinJgzopcEc9gotkXH5Ve9luYcoM8BrnwzCZ66ujXm22jcFnkB3M0UDhKqh0y8qGBh4Q62ehUFJi5DoiNBWe_UhmuQRwlkm-62RBsOY1EEBvnCXXPl2Ob3ajUD9MYycqTJa8YZgeqeftJFVig-ULCPJLYi8fZkTYhGr49HGFkeUOjouut7PHAr2uBiLkG_vcrvEpdf8RaofFhYPl7QP8YikM9u2Kxt-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇳🇴
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/90997" target="_blank">📅 09:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90996">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcd2dc7981.mp4?token=K1DQ4MgVPGKHtoBhcFsYpTxgTD33Q-vANRjN7jysrfM5TYPFI0JngPniVtouRtKsZQawGwkqDNR3r965xJG5SmEJhufL3uBtNdhtFh14xKl7fhGm6rkeiBZzDOQQhdUufvkAmtrYCUpsbkXMcwF9N9htTMY8KhKkDnmS1smp07bSJY0F2xyVi1LsiNRxoEZylqTcfK_eUxv-Lhx4wXbRF_rsJDWzjamethm20wie1u7XXeu-1UxMB-FfQvlgBqDzSkILPQ4NlTtdKrSF_xTml7mSwYYYjPYuh5h4wP1OawtCgMn9HHezMQGkjQ59LtlHUhQMszGl5m0X-E2Eov4fzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcd2dc7981.mp4?token=K1DQ4MgVPGKHtoBhcFsYpTxgTD33Q-vANRjN7jysrfM5TYPFI0JngPniVtouRtKsZQawGwkqDNR3r965xJG5SmEJhufL3uBtNdhtFh14xKl7fhGm6rkeiBZzDOQQhdUufvkAmtrYCUpsbkXMcwF9N9htTMY8KhKkDnmS1smp07bSJY0F2xyVi1LsiNRxoEZylqTcfK_eUxv-Lhx4wXbRF_rsJDWzjamethm20wie1u7XXeu-1UxMB-FfQvlgBqDzSkILPQ4NlTtdKrSF_xTml7mSwYYYjPYuh5h4wP1OawtCgMn9HHezMQGkjQ59LtlHUhQMszGl5m0X-E2Eov4fzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وضعیت مردم ایران در شب‌های جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/90996" target="_blank">📅 09:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90995">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">▶️
🏆
گل‌های برتر جام‌جهانی 1998 فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/90995" target="_blank">📅 09:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90994">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65885deac.mp4?token=pIH_5IRWHBA4VWdZRwHtWUTwRRhsmEyaTtycABCRMehoRzLhnlr_Eq-dkb6Rrq7P9MV5bFE8NgCc0qtw6HsVLEgtSUAayT-tBNnZG4u95OK6LC82bXCCbYkpCN8YTnXfW72WIEBSyEsiEO68pC0I65oq-Ir09FR5l4Wkgp5QwNBLX9aWRzemsVBqNZmVtlcqT7m5k4f6iYjPKXl4UJ7zUjMY6ZI0JRIQo_Uzq1BMX-UYqIDTv2WfnSk5CBF5BSQBeXsqOL9k2tcXswIIU6lOyMJSXnkO83hbKdZZRLMvlTcPLMisl63avuz5YAY5I-shWjs5GZvw9zGExVnpUMaLEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65885deac.mp4?token=pIH_5IRWHBA4VWdZRwHtWUTwRRhsmEyaTtycABCRMehoRzLhnlr_Eq-dkb6Rrq7P9MV5bFE8NgCc0qtw6HsVLEgtSUAayT-tBNnZG4u95OK6LC82bXCCbYkpCN8YTnXfW72WIEBSyEsiEO68pC0I65oq-Ir09FR5l4Wkgp5QwNBLX9aWRzemsVBqNZmVtlcqT7m5k4f6iYjPKXl4UJ7zUjMY6ZI0JRIQo_Uzq1BMX-UYqIDTv2WfnSk5CBF5BSQBeXsqOL9k2tcXswIIU6lOyMJSXnkO83hbKdZZRLMvlTcPLMisl63avuz5YAY5I-shWjs5GZvw9zGExVnpUMaLEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چون از پست قبلی ورزش تو خونه استفاده کردید، این ورژن‌هم ببینید خیلی خوبه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/90994" target="_blank">📅 09:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90993">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzusmD8_YMox6onh8HdYTWevGnKqJmlqoFp6hDkYQ_CBUxQnbt10srKSnlKXcGngVNv9t9Xo-B7sgGMCBLvt8PAaFkgIt50tSHs82CgRuKFwZvYqI3HucOa_3xOqBPRgCgOAPy8SBEiNe0IMYstU3fKHdCNryp0bLhc7DJN6KopdXSgGfqSuFxBdq39y4CL0TSLkVS5rXY-si6iBt5-8pgjb4s-8H1JC8ZCF1bkIrAdOJ_N4hDmKGi7EgVf02zSTy9p0E_PNOuI7GlfDTdAmvM724auQDzGLcKUEchTNH7E_5EhVXYevXmympoU57YNxiiGfrMLTC4vaZIAX06jSbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بهتون با قلب رنگی‌رنگی شب‌بخیر میگه
😎
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/90993" target="_blank">📅 02:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90992">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خوب بسه بریم بخوابیم</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/90992" target="_blank">📅 02:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90991">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
خلاصه اخبار امشب اینکه الکی گولتون نزنن. خرید احتمالی پرز یکی از بین نوس و ویتینیا هست. گزینه‌های دیگه بنظر بازی رسانه‌ای جهت وایرال شدنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/90991" target="_blank">📅 02:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90990">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cci-p--vrmyXnzoBgWuYeXM7CSaJDNbVyzM5Gut4kkiJ8V1PiGGC5moAeh1__cvSt4DhGoT8ifRf1dy7882FSb9rV0_KFUy6_ivEb6jmxg4luU8fMM0n5rSDn692KVe7cVSwU8Xnk686l-Q4wYLr_fbIUH-Xj0VZQrwBVS1hw4EQE6Mb-p3M1kgDRkBzzqJhrmvBQM6bt6rsNAvU5w7CNT1XrPi1-ewQY4fHiZTqOkQFo0IUhXU_mFT3ETxYpfIDFAeZsc0f-LzGBsLpYWbPZkJSemGbyqLBNyTeP2r50NBMMhMwcHpPIz98zPPFfOGRgkZC8Kq1S-Bauw0TWyQujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سالگرد ازدواج آنتونیو آدان و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/90990" target="_blank">📅 02:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90989">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/90989" target="_blank">📅 02:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90988">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
مارکا در سال 2021 :
🔵
⚪️
دو باشگاه بارسلونا و رئال مادرید پیمان بستند که از یکدیگر بازیکن جذب نکنند، پیمانی نانوشته ولی محکم بین پرز و لاپورتا که بر این اساس هیچ‌یک از این دو باشگاه برای جذب بازیکنان تحت قرارداد، اقدامی نخواهند کرد، البته این توافق شامل حال بازیکنانی که قراردادشان در پایان فصل به اتمام می‌رسد، نمی‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/90988" target="_blank">📅 02:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90987">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua6RUSG9wVEoPjBzcI8JCf0BBWsPKdZqLEtAoXvn4vEz8s2xlczX-VfoqmlNA0n1mpwbP86f1fITuBEGOA_DP_XsE7X0umFroHSHLj7t3WZSdXakmPDTf1IkBzitN47I-iZbQZNzTNV3mH-CeJ4Gf6VepMvKV7VALTSdv2pZH1cY9O70QLXSHRm23oonRwrDcaACDI7b6wQRD-IKU8YergkTanYwneMvqDS9IvozkCUHTkVyp0viCvZ3jawEmImy7a2sWlZUniVIO2cHLJ4B3uwIqUxxKb6oIRgkOdcQtoMJ2FfTehwIqumy0fE331eshNJzNWurDVcn1q7D7tVnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
#رسمیییی
؛ فیفا رسماً اقدام جدیدی را قبل از بازی در جام جهانی اعلام کرد. بازیکنان اصلی و ذخیره در هنگام سرود ملی در دایره مرکزی خواهند ماند، هر تیم در نیمه زمین خود [مانند تصویر]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90987" target="_blank">📅 02:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90986">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfeO-Yzv5foe7FZYMuggyIpNMUQKMOS2gHlfbMOd2xLoN8AZX0xM38dAVLUgh__nqSk0hL9jRH4KcRVfmC022YIam-KbZ1oHRU6bo_gPzoHlE0B510lTpYa2ccugIco4DedRAP4oVoudQmBWbaaBwNCkTcVGxfVbrXcxNw1kSvcXEETGnmOWvoQOgEZjJCj23dRgNU75SAiBhy1ez2t889KWWnPOifJSzcgL2OAC4t0zHMhk_YxunXXXtbQv_bYCe9f-HViunqHlLGtCWHPfMyqyl6hHCI2JB46CwcKttjJlQd90U5oA98_dLoIXMAa_f-rXDbxLzS6DT8b42exUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😴
😴
محتوای خواب امشب رئالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90986" target="_blank">📅 02:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90985">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyK79gGNxad1VpLOTxZ9qJbProzL9kFxwkwJwipchOR2cfY0wME8LOGUm708bKkpnyeYWxswGW87W8DI8GyiHOlNtAlUzYdriNvsE1aDCHdc4HdD_n6zDR90rpKxd78xuJ-BodVUG3pzMRnnh-CG8m5WW4pT5tvbDIeLHBv3GzSgiL1Vk0WeV8AxDSlyxIqONcuwoyM4YbY0_6ZgNfxa85PsczZIu9LWiBbSjM8b20f7OxFb5lUYexylyIGRiVAzthfwU2ura-dN6JcZygh_adhScH_rRwCR0Gv50M6itTCS0Z2UzH8qRdE9QEJxijhOj92C6ZU3IHfIZzmiU8NO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90985" target="_blank">📅 02:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90984">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/90984" target="_blank">📅 02:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90983">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فووووووری
؛ رومانو: پس از جذب کوناته، رئال‌مادرید شدیدا بدنبال جذب یک مدافع دیگه رفته و حاضره رقمی نجومی پرداخت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90983" target="_blank">📅 02:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90982">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90982" target="_blank">📅 02:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90981">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXRAtXE26aUlymYS2nD570mDgZrRSxhzD9_-NaddAHMWPAkN5GQV_rFIfhyHqISCd48PRTQ0hlHchN7o_41BGVHAAkBz0NNFsP8pZIaRhafExqGb9D7pfqd9oS1b6sUkQWe9fpY8-H3UIkuhCXkINLEmcHS37pfTLqDM5c87oQiegrqRteOIB3MbNc0nuwj2MJ36-RTLhqvx1bvrQ65IOYKNyOPLgzNTfTf-7eN-Bnxwt-vxLnvdP6Lqh9mf5es0ILfSb61u5XA4Zda_Lx9mU7c34JcNM9T7yoIEJH1vNPpVi3DuCm-_3vsySJqZa9jvKCRVLbFaM5lYSXxfOi-J_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری
از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/90981" target="_blank">📅 02:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90980">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
فوری: خوزه فلیکس دیاز گفته گزینه‌های مدنظر پرز، اولیسه و نوس و ویتینیا ان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90980" target="_blank">📅 02:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90979">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
وعده های انریکه ریکلمه قسمت n ام  : اگه رئیس بشم دلبوسکه یه پست مهم تو رئال‌مادرید خواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/90979" target="_blank">📅 01:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90978">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ولی بهترین بازیکنای تموم اروپارو هم بیارن هنوز خیلی کار دارن به این ترکیب یک دست برسن
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/90978" target="_blank">📅 01:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90977">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تمام رئالی ها منتظرن رومانو زودتر از سه‌شنبه بازیکن مدنظر پرز رو معرفی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/90977" target="_blank">📅 01:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90976">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E_uHZ9-lv2tx9CzoMJVECYsj1PgSd4fofzZgAMoyx8niUvULtYQwqA8B8cOjIweP9lTX8f95xETq5hRrirRDmTfvO4-Qkg9I7lVbFGuPWNeibgq3xnpGXnWvcvmTYEUuVElLhu8RTOBNf7D66wfvtMkc6K3rwzMgSOmrir1QCQbf-hgj5r9LubwJ4SCxHl_mShHEsEjPDgDXqF1o2D7FT3nh3HHfUf1LRaTYjX-JXjIINWKk65z7gQLhnJTY6bbHffcI-y8GocIWT24LAN7Zt864JGGFYEWqrRQIVzEhonl0VZfzwhKpKFKqmhCfakG5X00UzHu44_etfTV3l-bLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی بهترین بازیکنای تموم اروپارو هم بیارن هنوز خیلی کار دارن به این ترکیب یک دست برسن
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/90976" target="_blank">📅 01:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90975">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
⚪️
کوپه : این 150 میلیون یورویی که پرز اعلام کرده پیشنهاد اولیه اس و در صورت رد شدن قیمت بالاتری اعلام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90975" target="_blank">📅 01:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90974">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjTaQgy_BFzfRt_5kGw01-Aa7HL7VE6pFPez_iaXDGKdSsS9I0Nf-P2lgyz-XotQlrvgp7ibUIRUqbC5ZX8o18pQcMtuldt_9PBApKEqP-1Efv7IBpcsW643wmd5iTFuNHvTRFfHkjDlFeuThOt3dTm2zgZDaRZCfG0cz7q0qdRHK1UZGc34fNKvqmWZ6QKsA5oSEjNIpSpnZV_NikiY4yl15oWyi22TI3iDlfH6B7UaWoBAmhPwbxZPJRsohBlVZ9NNEJG7jpSlBS1VNG-SHkd7OO8PfjFtFVWCZhLBFpp5jrBKA5S6lpiIkTcnfC80X8sDba_zx16Wok_VPg6bFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/90974" target="_blank">📅 01:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90973">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5cGEVfmInDKckqmQAyOusBxkNpY0qvlmPZeG9eJm6YZeU51fcgCT6WkCWEQ5A-IEJ6arffdRSKaGn1_Q7hrJPb3KZzUqM6UBttOKCXNoVrQDKZWZSGZAdI48VZWCukf1agwPOoe-jK0AOYA3U7zFlIVDSbZXZ4PaAHXMIe4T88NFeSc0NOXNLsX6S27lLCm8XsIjx8GwTigGMHcD05_II6_NfFhCWa9sW9UuvL6oLEUGfKsgp3sO5uYtAHP3zJ9El79hxaEcs-mJBpYtxLzrnJyYb98tyFLHkgAK4RKIVpVds8wh9DJ7MA1uQLUS9Ti9tGgNePQq-zegnwqWoN38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توییت جدید اتاق جنگ اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/90973" target="_blank">📅 01:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90972">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WrQDzxMLhCBDcW011VDAHZCtR2LpXNZAi6Ywe3Xp960qUbTnmY1DP21869ZUaP0hbWzpvUJIi0ZsP_6DkR3DGBYXKB4IsfuLOfjbIH9hsFrngyzHuvIdAOS-4Pmf8zjDAPuc6GVlLmUEw6eZAT3y_FCXslCU1zIeubAAzv4AhDU5RsKN4HRudJDAAx7Hnisw4K2glNBB8J3PqbEKUpDy8pnIy1TyxOduB6tswxeqTxlSjA9NvmHMdwYz90DWBIGPXFe8jz2rHVl5jeFTnYexbMPnDN0KunonioNI1JlIPsH2wHVSn4vJpDGLy5EkF9PPp2z7YkLIoc93gX-WAKmrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از فابریتزیو رومانو | نیکولاس جکسون به رئال مادرید
✅
Here We Goooooo!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90972" target="_blank">📅 01:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90971">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu6vQgti-kN1nQXnH6o3MtydlokW3y6YOB8Zq7WdILs0ug-2mz3FUUFkvgKzqCu0UC6MHCtqV7jvtm_tcoWX46AgLnY8IZ3M1eBz9icMZ8tc4usPZhtIkBhIi6RTcEuJmo8ip4np2NAhYYTzX4nm60omUaSUD3_VfUpzNv5AhOrrsmcO0Zj406rf1rsd6YC6hRucVvvyAftOz4aiW-3pdrHRKaT7KeEg4WpREXgHzAp5TTLwMAakjMNSAchKzkiEKKfvCaZduLu7xZnW73_Ny1ynNmmaiStwcLMZpEuGJV1XVjLvKIrXLXsMBx8UWK6rYUvFnQQXmNs01rJzFAcWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
پرز نسل جدید کهکشانی‌هارو استارت زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90971" target="_blank">📅 01:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90970">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ولی خودمونیم ها   پزشکیان هم موقع انتخابات ازین حرفا زیاد زده بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90970" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90969">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90969" target="_blank">📅 01:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90968">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwT7Qsa5OmYiUnix7HPBG9NS4K5mEy5Ufwi9-n3T666TmQMVLeLoO_5TMY2j_zmjsmaxEfB70bbCA2PiQhrf0K5QYnTl15q9VvQi6DLaswJOoF4FA4Rx4eKtBlUAlRTupGNW542Ro1wD-5Pq8Pz4dVCptgsxXt3hqPf3W0sDM8JbVqMMMCJqUIiFRCq2h2iUEK-83SuQNQT_1Yjdr6CWLNtoetTTdkY2evN1zl2CkujSpgdDJI2O4qjB60DHITA1U2ku2Rv5mtCwT8XeetBlG_PXtY2i9QESI7kc5sxvaeKJ_pkuKdX5EvvAgfNHQZUYdPmB2bT_eQkN68qma3AFtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90968" target="_blank">📅 01:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90967">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لاشی دنبال پدری نباشه یوقت
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90967" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90966">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووووری پرز؛ هیچکس باور نمی‌کرد بتونم با فیگو و زیدان قرارداد ببندم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90966" target="_blank">📅 00:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90965">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووووری
پرز؛ هیچکس باور نمی‌کرد بتونم با فیگو و زیدان قرارداد ببندم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90965" target="_blank">📅 00:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90964">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IMCLKyAH00VramnZH2lOUMTVKW9RyPR0ZFiZuLVO9d5yeZlahtPzamQ0N_kpIuCrNpw1gf2GYn8a6meIzBmFCjQbq85fL0D8-_yvK7KoKEim1fUaLRP9DPZuCYiEwZkyy8pY46LMk2Zro-S4mvlZlBZqZXgKodok4FIxAw-2uW6Ha2ZuI53tr7RS4g4KBkKZof8zBclvVecQCer-wspjLBdmfY9TOKZsbELSbuVnyM13QZH2CNDWUk-00MtoE3OjUQEVr8w-MNUn43jPvArNJ98zP_tNoaT9-lSCafZqcMkCvRNa0NoHbk06JN5q9nQbJk2zquvc8ufgFkk6FY4mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فووووورییییییی
بمب پرز لو رفت !!!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90964" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90963">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ6FCNa6gO46kg3LTuHxzM16uPY_Kj5jZqMWHjHX1sczOx7yOPNZTXxJTjhRFXxGm--luOS5On6cn6iIUA9H3y3nzLXIsesiNmofSBCgv7_Pi56FKvBzXXcIep4-LiQnxfjDvTzBBROo4c7B0L840pRU316HRAK99gOkb84UL0es1XXRG5R0t7SJsbM-A6aT-hDdL0871wQQVNTUlneJEmS3fd4RfNsqiTO2hTJV1-rRZR2sgEQHFk5iyWwYlwt2-jUni2dhSX18fzcY42az2ngaN7c671e9sX3pC87QrZ_Y1TRmeOwly5FR_jI0ZuKxN6Nh18_OwVjtUQJZMJAPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90963" target="_blank">📅 00:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90962">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90962" target="_blank">📅 00:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90961">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
پرز تایید کرد که بازیکن مدنظرش هافبکه   نوس، ویتینیا یا رودری!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90961" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90960">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
پرز تایید کرد که بازیکن مدنظرش هافبکه   نوس، ویتینیا یا رودری!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90960" target="_blank">📅 00:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90959">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90959" target="_blank">📅 00:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90958">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90958" target="_blank">📅 00:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90957">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🇪🇸
فلورنتینو پرز: اسم آوردن از هالند یه حقه انتخاباتی هست. مورینیو حتی اگه ستاره‌هارو روی نیمکت بذاره کاملا تحت حمایته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/90957" target="_blank">📅 00:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90956">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
‼️
پرز: این فصل هیچ درگیری بین بازیکنان شکل نگرفته و هرکی هرچی گفته زر زده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90956" target="_blank">📅 00:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90955">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUq-aMNAYU64ON6DkE-WE9rUQIUm8025E_Z9WGItlWoUrsB8zQwh6EcTGop0FsSb-mSYieBLwRgAt64XjOXtUtq9gG2FArcJmwbLGWVSOgHZzffZa2xJ2tVTbfLaaEf5Qs1xYFVMLa_jm1-UHRiCPE9OBDN2TQacgsS7HX8d4OaBiRs39h2S83aVzKLUFklkIAuCLnCf9oFtjovMAHMs0NdEtBHSnl0DS8VjBCLN5rvIxSYl4SHE92mXSDRuUzJbynV7K3eC5aO70X2ABnulgijkgtCPQixgqG_mixsl7TXSNmgcYaMkKt1SOK4VbIIcXqJdcTqo533XWvLMQ_aYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه به ساحل‌عاج 2-1 باخت.
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90955" target="_blank">📅 00:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90954">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">▶️
🇪🇸
🇮🇶
خلاصه بازی امشب اسپانیا و‌ عراق با گزارش فارسی خدمت شما عزیزان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90954" target="_blank">📅 00:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90953">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
پرز: همه ستارگان مطرح دنیا آرزوی پوشیدن پیراهن رئال‌مادرید رو دارند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90953" target="_blank">📅 00:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90952">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff5287c9d.mp4?token=ZrfzuXUAGsZkMhL19rpx8IP3eELN3cNttLr5z0chjIo4563WrrQPltWRH_1Rn_31wvhOIPFpfnx2QHLqQ1f1CgjH2CH9kd3U06w6iuUMqeibBvFCe0j2hidb49eXxVK4H9MN6J54fmnyyzFpjO4blutUlBXTPSWbcCLScDPSxDjp8hgHdIbzHhcjwKzR2c4BFSO0ZwGSn0KjEhDsugZd9ww5XTEIXHYqj1A34P-e_xr2HjPrh0nO9s8BJ3WnqhqV4BXTSxF8tBP2aq1CIRw1dVY_Y6Ijba4jWZdhoPFY-rJkkXiwbRUBforGqfb6zR6TsZPlI3Wu_qqujvI_xqdnRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff5287c9d.mp4?token=ZrfzuXUAGsZkMhL19rpx8IP3eELN3cNttLr5z0chjIo4563WrrQPltWRH_1Rn_31wvhOIPFpfnx2QHLqQ1f1CgjH2CH9kd3U06w6iuUMqeibBvFCe0j2hidb49eXxVK4H9MN6J54fmnyyzFpjO4blutUlBXTPSWbcCLScDPSxDjp8hgHdIbzHhcjwKzR2c4BFSO0ZwGSn0KjEhDsugZd9ww5XTEIXHYqj1A34P-e_xr2HjPrh0nO9s8BJ3WnqhqV4BXTSxF8tBP2aq1CIRw1dVY_Y6Ijba4jWZdhoPFY-rJkkXiwbRUBforGqfb6zR6TsZPlI3Wu_qqujvI_xqdnRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇮
🇫🇷
گل‌دوم ساحل‌عاج به فرانسه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90952" target="_blank">📅 00:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90951">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
پرز: ژوزه مورینیو از اومدن به رئال داره ارضا میشه و بزودی میبینیمش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90951" target="_blank">📅 00:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90950">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6vslloLSemADOvKAEbFHRF_RbmiL64dDIimw4teAiQA2Rwyz5g2lTye-x_ADR6gaFxD4lUB_JJTNd6lddQcWsyTzmmS-YNIz2lzMnqbg2yf36iUhNTSbF1VEs3fAxDZY-KuslloBwAVpAti51m5Umc5TCYE9LWi8zvBPz1riNya7bU5RE9xPou1JJfL2y6bXxDM70wTSRpmvb1nwDGty3hvKL8UPuiTGhJxSfkLwNk_8tjAbSGb9M7pX2VonIRwi2w0T2L9D-ZWLCrQIkQWpB2jdA9RGBVjmJVjhZ2_E70fPPeSpKsg_rhEv3M2fi5BUMDuBwk2Dqk51h0oDtdOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
پرز: ژوزه مورینیو از اومدن به رئال داره ارضا میشه و بزودی میبینیمش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90950" target="_blank">📅 00:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90949">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
فلورنتینو پرز: مردم می‌گویند من ۸۰ ساله هستم و باید به جای رفتن به انتخابات استراحت کنم؟ پدرم رئال مادرید را در وجودم کاشت وقتی که پسر کوچکی بودم، و احساس می‌کنم باید به این باشگاه کمک کنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90949" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90948">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd6vieg2fi5x_5Qa6xQ_zbOR2wikLbH_kXstMRvYaZ5oiZVfan7RQdyqyzaLNC5-rsX2mdU34Jp45WX_InqXmxn6G3rH8rsINA8CCH6PzvDkb5Zb29zAKo2o7NxJIhWL0tl3sM_ybmwpm3hB1PX__TrgxL26SE7OROltzK73IxO70EHXHL8duA284DE5vVOYQ_ambDGwkM-t4OyasJU2311eypEZ-7yAqZ4tzCGxvagX040Jd_XMKYd45IP9bvL1va3S5VrTe858TIbIMBvTXdh_i5ZwCyo5e2vj-qCYSWRAEPpUbeqQPsMiNRZC-T4mGtAXa7XoG8ez7J4q8Gw0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فلورنتینو پرز: مردم می‌گویند من ۸۰ ساله هستم و باید به جای رفتن به انتخابات استراحت کنم؟ پدرم رئال مادرید را در وجودم کاشت وقتی که پسر کوچکی بودم، و احساس می‌کنم باید به این باشگاه کمک کنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90948" target="_blank">📅 00:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90947">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju4vC68pFKobNleQX8ZAug6yM6LZXMU2wtmqRa_RnZcKhHa9_dm3CVsSKtcBwukaCidnMlbju1O3EudCszSFPD86xY-0y254DsUi5olbmDEraxcZkRmW6NlvqpTxh1zdrxzUAblj-zpvRKBwyGtqGr_evSVDLm9s4_FOKvcxJ8YOw4NouinwkyAZZpqyIq06nCc7e1D_a7k8cK4LhCiyZoEV47K3atPayDSXYrgv6RrQnd6fIagnta8vnKG5RagVgzQ0x4GvQ90K23p7g3Kr09Eri2nh9wSf9s9QLca7Dn2_jNz0c4q4nJxBgP2CwKwT8IbbXL5dAJk0DSb6AgBZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پرز اومده مصاحبه انتخاباتی؛ صحبت‌های مهمش پوشش میدیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90947" target="_blank">📅 00:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90946">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3vf-gPizOfunznfqMKe6qi2Fn_YFAtwyRHc69VsshY7PHDuaEinB3_VM8Q25XqDGvH7gAui0ZNOJSUP4-D6pOEr4Ipgf236zN7utaxbXvaBU660BmstyNVZhphZLORIrMeditGJsTuxoa8YYBBtT01ndwUR59H2EsXDYtIMA0GwqWvmwkLm-p7m0il4IbQVUa_SDjch9b3yTipVzfYZW74Cil7rCqf3WbUWA6QjAvHMDSecnswyLVbMjuhoB4t45EpEm7gUKFXWWLrLqOiH4q6TPjSBQoZeN69mqDsqAdRle0r37BcgZ2pgCKFIzHOeHGf5TPEBXkJMX3CccOwsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇶
🇪🇸
تیم‌ملی عراق در بازی امشب مقابل اسپانیا به تساوی رسید! اسپانیا قرار بود با ایران بازی کنه اما بخاطر تحریم کشورهای مختلف، عراق رو جایگزین کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90946" target="_blank">📅 00:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90945">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
ایجنت منیر الحدادی:
ما هیچ نوتیسی به استقلال ندادیم. مونیر به قراردادش پایبنده و هیچ گونه مشکلی برای ادامه‌ همکاری دو طرفه وجود ندارد‌.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90945" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90944">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
😐
قیصر خواننده قدیمی آمریکایی‌نشین که امروز پس از چند دهه به ایران برگشته، در تجمعات بسیجی‌ها کنسرت گذاشته🫪🫪🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90944" target="_blank">📅 00:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90943">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c7dad01d.mp4?token=mX6Pclm252OGpJF58gutaeyiCcCJZ_Ehy3-sbCFlAFZ6g4aRdcWp1bxtCW4hbYpSZhv0z17SQWZYjIVmdBdufyBiVcum1KwWGn578jO4iBvekO2_yCZ3YwW3yWtHpx61bOevHwMIIl-33032nPMWLQ9SeSb2lqwd-OarWZ1O5BBMcGnWdch1aikXEvPGJ9u08-lUmMP7PaF3Aj5bcsujh7Y05A-s7S4BSns0CfK7WmRfHYMwAR9cm6bThK1YYm-4HJQM3fnTVnNZ9cl20VTG7RIKU0eI6yIywGE3ybN1VrGg90XcWFhmNvDCcgGtt2h7HQCYsy929HPQ1m0Xj8MQvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c7dad01d.mp4?token=mX6Pclm252OGpJF58gutaeyiCcCJZ_Ehy3-sbCFlAFZ6g4aRdcWp1bxtCW4hbYpSZhv0z17SQWZYjIVmdBdufyBiVcum1KwWGn578jO4iBvekO2_yCZ3YwW3yWtHpx61bOevHwMIIl-33032nPMWLQ9SeSb2lqwd-OarWZ1O5BBMcGnWdch1aikXEvPGJ9u08-lUmMP7PaF3Aj5bcsujh7Y05A-s7S4BSns0CfK7WmRfHYMwAR9cm6bThK1YYm-4HJQM3fnTVnNZ9cl20VTG7RIKU0eI6yIywGE3ybN1VrGg90XcWFhmNvDCcgGtt2h7HQCYsy929HPQ1m0Xj8MQvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇮
گل‌تساوی ساحل‌عاج به فرانسه توسط دوئه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90943" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90942">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🙂
👀
#فکت
اگه ایران تو گروهش دوم بشه و آمریکا سوم تو یک شونزدهم میخورن بهم🫪🫪
☠
☠
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90942" target="_blank">📅 23:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90941">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de9f07d6e.mp4?token=hlJdyP72kVWLV07vxEnEtZGU1oBc52GkXVA1z0mzKmNjb-rFJ9kXDeDfPWN2orlbv91agMUlBFzIpd9aE2J35XLwYfToFOKOMTmVit1uf9iBuBfuVZsQ30XKI3kW2XtBr6WPK71tA7yibykopWzdnOWRM0xHA1UTnBE9KMS0SorZNS5zN9NK_WHg7OA0aydoffpwQLcpebweNcP2DJmxjdb0ycjo1eLvlUfjNQUbm4B8BG6nY-siKCK8N6HIlUHTYyqOeIiae3aBYsjXbN0ExhKV_gCcW4aJy4fPrF3yeWo-RP3UGR8M57-CuHJiAEgDA_Fayx0naOB75Z7ZfNNcUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de9f07d6e.mp4?token=hlJdyP72kVWLV07vxEnEtZGU1oBc52GkXVA1z0mzKmNjb-rFJ9kXDeDfPWN2orlbv91agMUlBFzIpd9aE2J35XLwYfToFOKOMTmVit1uf9iBuBfuVZsQ30XKI3kW2XtBr6WPK71tA7yibykopWzdnOWRM0xHA1UTnBE9KMS0SorZNS5zN9NK_WHg7OA0aydoffpwQLcpebweNcP2DJmxjdb0ycjo1eLvlUfjNQUbm4B8BG6nY-siKCK8N6HIlUHTYyqOeIiae3aBYsjXbN0ExhKV_gCcW4aJy4fPrF3yeWo-RP3UGR8M57-CuHJiAEgDA_Fayx0naOB75Z7ZfNNcUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
میکاپ جالب آرایشگر خانم خلاق ایرانی با تم جام‌جهانی ۲۰۲۶؛ حتما ببینید جالبههههه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90941" target="_blank">📅 23:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c687b5ca.mp4?token=Ui8vNPnlH6I3ut0t71TZVuA0wM00uT8U0vhcG4jMs2sljNuPv-9gpdXb4hKg_MTLPlu3t6DSaD3OrxRDQMxI40KAIk7PaJSxftpTUzjQCPiMBzzpl6KhqGJRFFghBraJR_eSp-kj0ozPtiMlGtF5W5BRS19Vp8szCx92c9b6B9daGbGYWHKI28-IUd9hZ9WofyxnwS33H_631e5BNOSKcBDOtxorGh8_hFvSfcXpYgurMMNkvT9aV-faVHZ83FQXY2_BYz9Rh5O_w2Ts_Jd-gwJ5NSCbC0aJpzs7BxHIT_Molz05srWBeCPGuLu6YA-gJt6l_70-47WKb183fUOrvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c687b5ca.mp4?token=Ui8vNPnlH6I3ut0t71TZVuA0wM00uT8U0vhcG4jMs2sljNuPv-9gpdXb4hKg_MTLPlu3t6DSaD3OrxRDQMxI40KAIk7PaJSxftpTUzjQCPiMBzzpl6KhqGJRFFghBraJR_eSp-kj0ozPtiMlGtF5W5BRS19Vp8szCx92c9b6B9daGbGYWHKI28-IUd9hZ9WofyxnwS33H_631e5BNOSKcBDOtxorGh8_hFvSfcXpYgurMMNkvT9aV-faVHZ83FQXY2_BYz9Rh5O_w2Ts_Jd-gwJ5NSCbC0aJpzs7BxHIT_Molz05srWBeCPGuLu6YA-gJt6l_70-47WKb183fUOrvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پشمامممممم از بازی امشب فرانسه؛ تنه عجیب فرانک کسیه به داور بازی باعث سرنگونی و مصدومیت قاضی این دیدار شد.
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/90940" target="_blank">📅 23:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90939">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cff28a7c0.mp4?token=Aizl2lwJOp3Ggp8HjlNMqdMpFU6k8xxZbaF47jZ8Mriq36k90oOz_9EggYbfSd13kRS2JPKF02IIFD5W47oRSmMAHIHFOUTTiK_mh7piIL85B_7XFg_hB6A0CspzTgwpOlVRDGBTREyLSAp6CckBlSEdiau9lSlgwCLVbX20fGyCyaKQFtnF5NE5EiJ0WRmX15kXtP2OPAyM_rw0d9d1pj5oFB2Z9c0eX9jLzmYwn5_OCnGC9lcABMV3_hD2XcjWwnVpzRd7ybJRv6FmfH3pkHXpmCBGM3TEVgiIRVD1IcDSW73tnhP6BU2l4FuKm0e8RJEhgn8HGvJGMqWlYebLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cff28a7c0.mp4?token=Aizl2lwJOp3Ggp8HjlNMqdMpFU6k8xxZbaF47jZ8Mriq36k90oOz_9EggYbfSd13kRS2JPKF02IIFD5W47oRSmMAHIHFOUTTiK_mh7piIL85B_7XFg_hB6A0CspzTgwpOlVRDGBTREyLSAp6CckBlSEdiau9lSlgwCLVbX20fGyCyaKQFtnF5NE5EiJ0WRmX15kXtP2OPAyM_rw0d9d1pj5oFB2Z9c0eX9jLzmYwn5_OCnGC9lcABMV3_hD2XcjWwnVpzRd7ybJRv6FmfH3pkHXpmCBGM3TEVgiIRVD1IcDSW73tnhP6BU2l4FuKm0e8RJEhgn8HGvJGMqWlYebLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به ساحل‌عاج توسط چرکی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/90939" target="_blank">📅 23:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrq9KnsEeguQnYtOXLDWJXgvOwLTHLDr4sMq7r4HE0XX7WnkPZnFF-hdHUv6frAWb0EDQtQ2MhEUT5zlKRfgBxCBPW7gr3V89rRArMgD9cc1W8UVKcusUfyHso4rF51RtaB_eXthI-7w6IDDy-5uWy0Ruj-OnOoK9TLxSMH6VGJw2ce5UgCxhrD3xhPfgbjGgZgtAXq6O1dkIRDiNFoGh4gAYKy6a8GB6K0P_TANPBEJP3NQr1fYf6ppf4Pv1xlL3bc0vl6_3kFlr2VspyX62k5_zBvQ3RWb8qShCrSeydzUOgO_54T1FPAYeCgurPA5cwdSPxNFe3FcaAanzrURmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#
فوووری
از ESPN: خولیان آلوارز شدیدا از رفتارهای اتلتیکومادرید در ایام اخیر عصبانی شده و برای خروج از این تیم دست به هرکاری میزنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/90938" target="_blank">📅 23:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90937">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHydJxpl2Sv-Rv-cNqGMfXMrL-Fg-HmgUBwTldNnufGbNP63TU5EBqSnhi2yHVV_VuBydRUJWT-6O_YRbx1E22JkUAzntymGtY7c8DHKmbM1sziVJ33VUYOeJc59VLI5gUxOYEKtDLp5RoyGFqtw-si7gN1eyfJUQ25Wlj0-cyMBC1GoBC9rN-TTBzUHmM9nJaf7tDWw5-C-E3E7rrXXkSdErcD31nCda8zLhaoClwgUiQFkTDhmoWQ1L6nOm2nCCKq40vaCTmrPUsmx8MGw6BBnYFAnDtQ9v2ug-V6L87JpHzhiPbPiCL_m7vmBy5zRn6sXXd_vI148GZtZjFIiug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/90937" target="_blank">📅 23:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90936">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db661e26bc.mp4?token=SBBAMKeKEctmt55xZNTBjUzzkoOXTRek3K_eHr9UsOpUbaKI4URWBm1CCfM3GPui9BjOsDP9Ji8ivIY-iSYZYJcRwU9Y3mvFRG89VIR1J08OtYq-RHZc8NKCZDFH5xOJ1jrs9TOn6qt9xxaQbSyxovQPCtLx8GlWAWoRvpqPESJ4tByGcANvE7f4fqFK-H7ZlGCDV5IOPDbNUjSGNgahK7tdrly-GQnvnk1zPTHHe7AOcnL9SwYBmV1PDywdgsA2qJ9tXdYFHRCo5Gtr8DiFq968EfT8JRMqPI_cxjWYqZ_ur5mtlf5dZwUn5qiK7TvockYGwFmJgg1CEyur1ogJow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db661e26bc.mp4?token=SBBAMKeKEctmt55xZNTBjUzzkoOXTRek3K_eHr9UsOpUbaKI4URWBm1CCfM3GPui9BjOsDP9Ji8ivIY-iSYZYJcRwU9Y3mvFRG89VIR1J08OtYq-RHZc8NKCZDFH5xOJ1jrs9TOn6qt9xxaQbSyxovQPCtLx8GlWAWoRvpqPESJ4tByGcANvE7f4fqFK-H7ZlGCDV5IOPDbNUjSGNgahK7tdrly-GQnvnk1zPTHHe7AOcnL9SwYBmV1PDywdgsA2qJ9tXdYFHRCo5Gtr8DiFq968EfT8JRMqPI_cxjWYqZ_ur5mtlf5dZwUn5qiK7TvockYGwFmJgg1CEyur1ogJow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل تیم ملی عراق به اسپانیا
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/90936" target="_blank">📅 23:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90935">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
فوری و رسمی |گل‌گهر با رأی انضباطی مقابل چادرملو برنده شد
🔹
کمیته‌ انضباطی فدراسیون فوتبال رای خود را در خصوص شکایت گل‌گهر سیرجان از چادرملو اردکان در خصوص استفاده از مائورو آندرس کابایرو آگوییلرا، مهاجم پاراگوئه‌ای چادرملو، صادر کرد و براساس این رای گل گهر سیرجان در این مسابقه ۳ بر صفر برنده اعلام شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/90935" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تاجرنیا:
فصل پیش هرچی اتفاق افتاد مقصرش ساپینتو بود نه رامین رضاییان و غیره
من میخواستم ساپینتو رو قبل از بازی با الحسین اخراج کنم میدونستم اگه بمونه حذف میشیم ولی تو جلسه ۳_۲ به نفع ساپینتو شد و موندگار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/90934" target="_blank">📅 22:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90933">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLOTznFslKVUJn0S8oHrSw82aPaKULbC1ns6C5n5Gw4hozE6F-LTXd3YxWJkaT3uiiK0r8pZn0nzG1seZeadyiqtT_Hn8LtVj3Y3ICR7PXHI0TZMPsi8A6j30WhSFEXiTBHPaKimYOjzH42Y1YjoSCJutnDwqSSJ58i5py8avI_C6n_HcSgx4N6PRtN30NbyVWhkmwFcnTh-yChFUjLkn_MxunosgV8kqn8Yr_-8jN3Tmsmjcs_YvWAs0ZWaO7_xlwkf3zAfyTo8bd_BshqQPtDI4FDltzeQ66GEi_yHoKvikE76myVrV7q6OaEzYTCBseRzeN67KXGwmBKa5nhm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییی و رسمییی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آندونی ایرائولا سرمربی فصل گذشته بورنموث به عنوان سرمربی لیورپول انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/90933" target="_blank">📅 22:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90932">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNiv4-03PENSdTZceJy3bADUCfXABQxS0jMHmJ_kKPK6NZep3DeTVv5eQ28RYVYN_26guhbbWbBD0TNL9iaDOz630QsiMXczfYluqYiaHmYIYaleKs49rnyPH-ouPM32afRPNOjrLT-6LWU6luvCyZjXOUluQmMlDkneId7OzUonsdFrklWd9eOm6pgZqs2bCDniXprHb_FQ0WxycjtWN-kBlH0Epc4JBg0OUuQOnQSUeaBuGMOHm4UDcbLLN5K-PFM-asMmiaqvPpXkVsBA7p2odPn_57tYLFUaF3kySFl33qD4xxinfie45YI9nvIQbUtuzs4a_mXeqOxylcxXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با پیروزی ۲ بر صفر مقابل مالی آماده جام جهانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/90932" target="_blank">📅 21:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90931">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncewUgSfh2LkWtRoKz_wAt2Jnnw4HI_-hzgpV26_sR6ZqD9zd4vxyRB00i2FxQXnMU-Pw2VWNuZtxqx-5VvYEL_pBbBqBHv8W3O7CvH9TfGEHSHyMx8GLvKpaDff6F19l8OKZuyQ9-DSQLp8U4aMGSX1Y3CWa9FDufFrxn2lZb1_pX0-0-GjzyK6mRYsf6R5zgYuLzqRzxmCZf3WO9lHT_zQsvPRRzMuwSHb0kSStpw69c_7IecA_osxB7zpJThTQJfOdWQ7rk7UnUkZVIWaKcJrJn2E9uef4CflGiTwpu8WqmJG3GvW5coPasc6AICBMQLJKc_BUlkXSRQoxFJdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب پرستاره فرانسه در بازی امشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/90931" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90930">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2312570c50.mp4?token=QXVgMvA0YrVNOk9kfnWHE2Ke2YF4pV0xvQHB7Ll6iflDBLsEo_W2XD76IhcVTweqGgF-i87Fa1xO5vL9ft_eGCI3dEMrqyEM_ZLEq7rZZ_yLTy1ViHfvX3RtLzm61quVigCEEWUNbU-k75bmj_DtBpiVnjc7kfmnEk_Jm1TMAW5xDubV-kP8OBjvciIGb__EG1cE8a4N4nybRxiCTTEE6zZb_g2r78oEIpXzLWFWkPfH60kHb9D1n5rQhwXl_34rH_807h-W2H7PEkeD2M6drGVM80wrT0e-SDsHrjm1HAfURnXNFdFoMOJAx3pBFOyoiJyEvmTRpG1GPfzYpQ8MxmiNmkIqLWZDBtCkefcXYLabDxjmIdfIDGxb71Z3le6a4CzfEQ0CjFgVjXtfeDuvC27vzn5j1qLgGXqyuqHAbaIZEVCW4T1luQ_bVVa0qoETFVUBGInp6HQpCfTp8-mu8emtoPSp_ePqgF14NcLsgvd4yLZGF8Vrx5MzP0bZgO1U_g1pDrBJNuMs_opebPBol0r0lcco-xKLFJdSukNPCkkAYxQvxh8tMvlLoIJOT5uOy8svVC1_MsLsJ6KIeFxMa-dmr3CuuTvxsc-lCLaXbp0NhmmRdYGp3ypcuOaz0DfUVeQOR5jn1VmUnpbvzygW-NGB0hWzn61t8m_nJegBpfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2312570c50.mp4?token=QXVgMvA0YrVNOk9kfnWHE2Ke2YF4pV0xvQHB7Ll6iflDBLsEo_W2XD76IhcVTweqGgF-i87Fa1xO5vL9ft_eGCI3dEMrqyEM_ZLEq7rZZ_yLTy1ViHfvX3RtLzm61quVigCEEWUNbU-k75bmj_DtBpiVnjc7kfmnEk_Jm1TMAW5xDubV-kP8OBjvciIGb__EG1cE8a4N4nybRxiCTTEE6zZb_g2r78oEIpXzLWFWkPfH60kHb9D1n5rQhwXl_34rH_807h-W2H7PEkeD2M6drGVM80wrT0e-SDsHrjm1HAfURnXNFdFoMOJAx3pBFOyoiJyEvmTRpG1GPfzYpQ8MxmiNmkIqLWZDBtCkefcXYLabDxjmIdfIDGxb71Z3le6a4CzfEQ0CjFgVjXtfeDuvC27vzn5j1qLgGXqyuqHAbaIZEVCW4T1luQ_bVVa0qoETFVUBGInp6HQpCfTp8-mu8emtoPSp_ePqgF14NcLsgvd4yLZGF8Vrx5MzP0bZgO1U_g1pDrBJNuMs_opebPBol0r0lcco-xKLFJdSukNPCkkAYxQvxh8tMvlLoIJOT5uOy8svVC1_MsLsJ6KIeFxMa-dmr3CuuTvxsc-lCLaXbp0NhmmRdYGp3ypcuOaz0DfUVeQOR5jn1VmUnpbvzygW-NGB0hWzn61t8m_nJegBpfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا حتی دهات رفتنشونم با ما فرق داره ناموسا
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/90930" target="_blank">📅 21:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90929">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYHP0uyVEjWbaqhrFRxGCfcsNQWBi642ui5TL1lX_TaBCczbnHyXA7ZGe1Y4fNWxik4MK9VIAEoWXDir1Y5kZIsVTo7SIwh7GZCwRDVPCCdW0MANfWF_cK7WTMBqsKU_dqVUyfU8HC82oP8K6OAPElQFwZvfDK-NqYy5VDZLGrZP97fhAIm5tOwmaTDqOliMPG35Nch24Je2vMnPDiATK8qP7YuUZo8rsZYloilbWSFy6ncwz0UQPx5OyW_oWHj4wBia1Xjt_t_FD-D9rmxBR4VXKwXKVgWn-TYm90m8RSZAN3tZsci4AGSBgOHugFo3H0AubtZy8-AbgQ4f34aP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از فابریتزیو رومانو | نیکولاس جکسون به رئال مادرید
✅
Here We Goooooo!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/90929" target="_blank">📅 21:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90928">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/707e563eeb.mp4?token=W_3JIqFCYFg6PO5b3JPetq85As3NeyFQSaxZ4rVGhWIxfGPqcSV0JmMpotGN120kKxPPPjmpn7-mcBujRuiCLx_HJ4jDLR1PhEu0jV3DWyIMRj0HqrXraVWBVI0uIa2y0bXFhq7RAPYydk1pNiuRMz6uUpdf5aCHG3ik-P9CuuuqfD7RLOrC60cRTAYsNyvF2k4O12WvIF0mlFSXNWqMdYd6Fe-JMdxXB7bbEwqJ99Ic_XuV12vZ87Rlw1R3fu6hwlwdXyoAk4llInYnnB99YhJeHVsaufGR3BoEmalVw-GHBcQZA7TuPmd9doq7fsc3xGD0CiTsajlTpUxtLqg6qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/707e563eeb.mp4?token=W_3JIqFCYFg6PO5b3JPetq85As3NeyFQSaxZ4rVGhWIxfGPqcSV0JmMpotGN120kKxPPPjmpn7-mcBujRuiCLx_HJ4jDLR1PhEu0jV3DWyIMRj0HqrXraVWBVI0uIa2y0bXFhq7RAPYydk1pNiuRMz6uUpdf5aCHG3ik-P9CuuuqfD7RLOrC60cRTAYsNyvF2k4O12WvIF0mlFSXNWqMdYd6Fe-JMdxXB7bbEwqJ99Ic_XuV12vZ87Rlw1R3fu6hwlwdXyoAk4llInYnnB99YhJeHVsaufGR3BoEmalVw-GHBcQZA7TuPmd9doq7fsc3xGD0CiTsajlTpUxtLqg6qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فووووووری
؛ علیرضا نورمحمدی دستیار مهدی تارتار اعلام کرد که سرمربی فعلی گل‌گهر به احتمال فراوان فصل‌آینده جانشین اوسمار در پرسپولیس میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/90928" target="_blank">📅 21:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90927">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0759f4cb2e.mp4?token=dn5fZwig_azm1ABbiulCAk50wGiYH5D_ETOD_ptC_jbE4uHtMFk7As3qOt56ZPl8pKS3ZiOTGLCEN4QZZbDMIpXrguKAidS14aiX7q4zAuWiK_yydVgTQAyc-L7ijupysNtrHWg7AWzEJY98WyKxYuR1kvnfhnjKe8Fsw0kWSSCw3ZN_DRWCf5O0j7C6CrGQ5vszNsutLHFP3CnQFEJkfPy6SMKehvHuf-unHLxyoHHLlItl2rXObt3l_k4xwdnHVonLN_cEYTk7nztbRr2L2VyOu9QRP8JVjgL6T80FOMG_D5XVkKf063fQwPN6ZsYEStGtWpub-GVBaSXTiO09sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0759f4cb2e.mp4?token=dn5fZwig_azm1ABbiulCAk50wGiYH5D_ETOD_ptC_jbE4uHtMFk7As3qOt56ZPl8pKS3ZiOTGLCEN4QZZbDMIpXrguKAidS14aiX7q4zAuWiK_yydVgTQAyc-L7ijupysNtrHWg7AWzEJY98WyKxYuR1kvnfhnjKe8Fsw0kWSSCw3ZN_DRWCf5O0j7C6CrGQ5vszNsutLHFP3CnQFEJkfPy6SMKehvHuf-unHLxyoHHLlItl2rXObt3l_k4xwdnHVonLN_cEYTk7nztbRr2L2VyOu9QRP8JVjgL6T80FOMG_D5XVkKf063fQwPN6ZsYEStGtWpub-GVBaSXTiO09sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال چالش رفته بعد پشماش ریخته که اسم خودشو نمیتونه درست بگه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/90927" target="_blank">📅 21:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90926">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlfcV0emfomfAbMZzYZY_I0qWUCkWQbew6CT-FEfns0zA5SzQWI1U8G4eOVzrQH4G7WK30sFppCovz01LMEiG5M6HmZ2Q3GkpwiEX8TcYkUiuf9yki97qUdS4FFQ69TE5kgXPI_hcUT00-ZXd42kiHbnLi4QbMuz2h293mWi676FMtkNJNLGmvbHcqpp1spmNpqCS689F1cfweWt-Ph110kD_FzcvQpUWQmczUFa8P5ElKVpDlG4RL8Ow48SGivoUaKX2LMCoNzWHf1vqnzMyhBf_b-G0F6Fe4G3thPms_Ck-SdQt3Id1mAXb8ZKKA4rvriEB-UcoRHx4eTwHx3bSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب اسپانیا در بازی امشب مقابل عراق
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/90926" target="_blank">📅 20:52 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
