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
<img src="https://cdn4.telesco.pe/file/sF2V53ozbzXl-taL4NuNsMvbPCuqRq4e8CHmZc1gn630fchu5wAyP6kpHjmyTL03rQdEIw7gXzuohdG8fPsDjLP9ytys8hBzI5eodnmLXChIlwongGojXctFNGAHRNWiXMH2qLXlU2sGudtY6xOKRHAC9TF1-08WYwd_hJXwTVIzV3-TqM4rhs162bL3u5NKg46c52s2rj_H9d-fXQ6Qhn-MqoYz9PP80pzVyxVIQP91NnXhE3m9tTIGEk8oCSTtCWYRNbrd-toI_nzhGrzWvh5Oggorovcbr1CMuUAU6UBR_ibrHRE3TMDvAMuvbZlm48YAAsZ6eVxds-WrfMPJ0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 237K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 17:28:34</div>
<hr>

<div class="tg-post" id="msg-23274">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhHo0b7_cHIAtD_Umetj8xWIr0knyH7oe9SVXvWiOg56LPAzs5KDAmu1OO3Qrkr8_q1PP8AytsWbdo3-zmRwPEckpOrHFNwXWOLx9TqGlg1VqfUHnHa6vFfKPaJyavWnOClsUJHmAFbSM-pQ9kUyzWSLrBCZd90oxyx28Ve2BPIQdFXWEokmg8EVvAUiLMJi00x3UMEFa3A5itXkiMNCyN9guGXoBXWYC1-_LL1CyCWyoZQBavrlzC-6HsAJlXt-xlAQWXvFc9FeUUCvS5qnathqJCbi-6OWM3Gs0UURyuEP01C0bjELjGN_YGcpceEf3BVDeCmXtkLhzpOlDRoAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/persiana_Soccer/23274" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23273">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=SO7UFVJQk1I3MLm8DGlnj2L8gmihE3VkYmg_m91q86Onh4Q6tiktZkir3OeZJAkUEf3zhN_rbOqCH8FVbFBzMIf4eSfqFN_8ysnh609ZN5ACjW7XzJ2IaFoWSnfDVUqfowHtN19BdRF1W5humVtfczx_KfdeYCIqRi-Weq1UKuARPCXayOEuDnOjKf5DZFbK4YzZ3WgikEVflpIp2ViCpLZnqN-fcPfovRnv0r-QkkB57fNMALRpu0dUDT27yw0wMGAUXmHmDGFkkKb4s63VKtyZU8MIwqvrLxB0D6llItK0Y5MxxgZHrvhjOeSflhkSXqVP1GgYqD9BTNlIgZxUuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=SO7UFVJQk1I3MLm8DGlnj2L8gmihE3VkYmg_m91q86Onh4Q6tiktZkir3OeZJAkUEf3zhN_rbOqCH8FVbFBzMIf4eSfqFN_8ysnh609ZN5ACjW7XzJ2IaFoWSnfDVUqfowHtN19BdRF1W5humVtfczx_KfdeYCIqRi-Weq1UKuARPCXayOEuDnOjKf5DZFbK4YzZ3WgikEVflpIp2ViCpLZnqN-fcPfovRnv0r-QkkB57fNMALRpu0dUDT27yw0wMGAUXmHmDGFkkKb4s63VKtyZU8MIwqvrLxB0D6llItK0Y5MxxgZHrvhjOeSflhkSXqVP1GgYqD9BTNlIgZxUuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/persiana_Soccer/23273" target="_blank">📅 17:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23272">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRCWQpX8swPcRA6b0Rk_aPao99_63RIpZUOQAZmeevY9i3cm_xX1sHApj8vBb_ReCgOeMYt6R4m_e9asYI4qJSItga2m4GQBBOZHoj5AGvzRVc-4VhyttRceTPUHZG2HvqDMpcBpV0y6WC7hd5ppaKw5g9m9Xv6DPhHagD3v3Hnsrn9o6lA__A_McnHUrXivtxn5kmnLLgtemKRWq5POFs6TVj5y0ouI2sJXGSqUhf6WtMXuCdnMFYU5zuC-fPDGT-kpoUoQWciHUOgXhzlf8Cr0GeW8JYBHjhJJeOzUDTXBkgAEgRLP6P2-PU-tUq6m_9IkQ4OGa00T6DaTG21tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/23272" target="_blank">📅 16:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23270">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1a4HIan_gDMgdX7WkaTGsNjaHSMG41x-rmRwvLZrGsWpqg8ETj1vVWsXMx4NWCcg4pIUNUk2xt7xVKYvjxY0m5iog1eO8oVmq6NbIn6GlNZgO5IgYaFoIL_r-GcG7d6GJ_LxO-pdH1gteV_QkcWeog0ZaASMwIKoDoZofdnaR32JqLVMJ4lRp3Y_TyHmNgLni19j4l4HU5aEPdodR9Qc0uEkiJlskN5uh8bhohm5M-GBMA1wDWRjcFQZujjd7UTvuYlm1RUh2tKeux-8LenCmL4IRlFWD1SWWj19uV2z3QPztjR7sUpSzZZYcyVOgMVuCr1fmg8IymG9rD87h0oxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFgadsdJcA_ZgNlm-ChFftKMcRAs8soA7tsZlx-Up4qnKNIsI0YODrxHohfAkSOSdMeF4UXtEbNpHp-KRvOdGf-pap6hjGyHRonqYg3DPWXKJzRMw3PfN2PmR41E7tWFBaTSvjv8UBq5WkxFI-ebTAuLsmDeM0BByzezNzDNKEmVQIrLYjPS6rW-suZiK3_fjfhI-Re7EzJ-0nqcBqXRp6JKPmPS8698t9MNDqvW-9e26doW1-T9l8D-6iiSm34TlSeU1xlhgoYOofjL8m2rxLNoCV8CKa-DJGXRTs7i5Pa2AOAj1cI5jj-9-KQx_s3IHwNNP49ZcRBAF31szi-6zA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/23270" target="_blank">📅 16:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23269">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=KAvXF5DPYjAZz4I534w6chM9iXs2Kj3babngCjLWCxt7qNlPKro0rEq4qTtMSeyei7i6pT5aqqEZ7fHrAaEu4uECesyazpVbVUpJAl0zWVXdEzBP5O_SkfscyKIWZwxwJwgWnUEhzUcX2tvwLB40ut9hANUCWBKJdPP7Aw0-QpqLSx4bL4-O-kYBMkOkQZn0KVaMkulYdrfZWlQ65Oj4PyBCsouW6bknxNZLvI51DassXa__P3OYXaE_XTVPwbaTbn3siFkCi0i-RAYmNOEudHrxaieO24GQ6_zuNN9NfHkTINqf7T8HeugwunfGOyJsFHLVE33E8zecVRuYiZnzZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=KAvXF5DPYjAZz4I534w6chM9iXs2Kj3babngCjLWCxt7qNlPKro0rEq4qTtMSeyei7i6pT5aqqEZ7fHrAaEu4uECesyazpVbVUpJAl0zWVXdEzBP5O_SkfscyKIWZwxwJwgWnUEhzUcX2tvwLB40ut9hANUCWBKJdPP7Aw0-QpqLSx4bL4-O-kYBMkOkQZn0KVaMkulYdrfZWlQ65Oj4PyBCsouW6bknxNZLvI51DassXa__P3OYXaE_XTVPwbaTbn3siFkCi0i-RAYmNOEudHrxaieO24GQ6_zuNN9NfHkTINqf7T8HeugwunfGOyJsFHLVE33E8zecVRuYiZnzZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم بهتره برادر بعد از این حرکتی که زد کلا از فوتبال خداحافظی کنه و پشت سرشم نگاه نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23269" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23268">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uziv-EEEJt6JT2xHd63Z7DzhHkqZIx8GgQUdWfNwh7_xR0TfkyDpkKy-sU3SGHN48d59OTo24zqsJVeeVv77JPdhzY-laahp6hj8EwFA5DI9giGo7U06GrPk1rZOADxDQKkRvaIQ_ByrOVYzhm8H567wFbwjPaKZPvF5udiIzZXCRsoLDXWQ46sYJENzyGM0wo8nlFNVNhCfS82S74pl2jXW0sNB2WHF3Qamz71bVLGjrRKbzen8CtETwpgpMRD2RTDnqWNAhInQZd_ZZ4_dAU7gyRcoB4dc_rUHEo2MTS13JtyQMEWuW1u-Mw81ve_pzJFZLDXc1VSKJ1VuV8FAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/23268" target="_blank">📅 15:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23267">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRsZIc4AxI_O0IAJo8YQbsuTUFlFCNlBMQuDuayX3noRYfoZZ60LmGgifwJHfIknmYz2m8TMOM2WbQmcY2GBSrEkU-9cds5gOQK1AtoQEX5eYCmlyFiFBKLZhMPgOwkcFlNf2sqTafJdDTaBx8wN_I74vfxOe_51mO0q6AK--_kjQyxs81FQU2ETG5FCPmzPqrRE1Lge4Wv-q_lIc4r0Z9hxpufVTjoQWk7XbjNV_scT-ryDeX83vU0Mf20UsbT-piQgOkRTIwzuN2Hoeb0NjKhnDjtLystwc0z9lpJfVheTEIeghP1QAm1W-DkSCYx8UkzDY3LrWH7KGtxkfjj3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛براساس‌رسانه‌های‌نزدیک‌به‌دولت ترتیب رفع فیلترشدن پلتفرم‌های‌ فضای‌مجازی به اینصورت: واتساپ، یوتیوب، توییتر، تلگرام و اینستاگرام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/23267" target="_blank">📅 15:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23266">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=da6DttT9SZrSiz0tEBw62gIB7DYpZbhVCpSEK56JJlYa-VeFlHBvM3AgIgveFuzNe2B8bzwQRBr_TDCZ-dVqtMrPeG3JiAmGfilCBvn6nQrmAtq7h8sEOen0NJZevT3d_BN_WYn91l-FTTAgVAldKC-jU_l_AWtTYmeguHIW0_sIAzX0xk_Ca4uBUDF0fNtXflpbcbV5ZEWIqjsjWwbkJzXuM-UThjRUWX7iQsecG5xaJ5SBiDbeKih2FTbI-SNhL3XhRoCpM60o2qtkKUf8bIgC_kw5x2gEKfs5T-n_S0cO4RMGH3aXk3yhozhs0cNeVHTHEiAXVSjca21ueGcHvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=da6DttT9SZrSiz0tEBw62gIB7DYpZbhVCpSEK56JJlYa-VeFlHBvM3AgIgveFuzNe2B8bzwQRBr_TDCZ-dVqtMrPeG3JiAmGfilCBvn6nQrmAtq7h8sEOen0NJZevT3d_BN_WYn91l-FTTAgVAldKC-jU_l_AWtTYmeguHIW0_sIAzX0xk_Ca4uBUDF0fNtXflpbcbV5ZEWIqjsjWwbkJzXuM-UThjRUWX7iQsecG5xaJ5SBiDbeKih2FTbI-SNhL3XhRoCpM60o2qtkKUf8bIgC_kw5x2gEKfs5T-n_S0cO4RMGH3aXk3yhozhs0cNeVHTHEiAXVSjca21ueGcHvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درسال‌های‌اخیر؛
گولر، اندریک، دانز دامفریس و حالا هم برناردو سیلوا تا آستانه عقد قرارداد با بارسا پیش رفتند اما در نهایت سر از باشگاه رئال مادرید دراوردند و راهی سانتیاگو برنابئو شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/23266" target="_blank">📅 15:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23265">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffdXWvwH1lkSKA-u_scJV8w_ptj-8dmEJjk0WbQg5LZD5gJ3b0okuTDzLpCSBHBL-Ycxjj6e9iFt8lUUX-TJuTFAv1nR_l4kFMBs-OcD_f2wseP7HMwuvKWEVxTLFDpJJ8nc48y-qrAjXQZZVJ5gn3pqF413GY4EjVVCAUr_zeflrKQvP7dPdMzqCp8ih27H4WUoSptowWiPwbLIAVF4RWhHPsmmV-a0QJDpGwPs_WtYs39SGYgUjYUbRa2PYSOVYGAaWn_y-9xc2CBAgV1iYp3b2mAEx675fDGr0A_gl99ACU2ImuTEe6e1Mn246Vg9id0WmIvgnv20mVMeBZ1akg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/23265" target="_blank">📅 15:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23264">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=nz_ebix55wfwqOb3UiYo74mHSIeCBV4ilqICkT_K-cFDTAlHr9qbr_BEgU_k9tU20tQUn7DZR5tdLFzgnqIzcqj7W09S7-eE_8ckd_zir7NSNEaYTekNd5SN_53Do2h-YmU7mXqATpoZN5YdvI7yFMm288xfHOqTZjZdzrb1JrBGi7nzkAYmkDWqnDapRrsyRL2UX38L1PE2iuPIo168Q2D5Pi2iJmKJ5Z3jMx1cDQp_x9m-txHE5frK5FOaNyvX9xA5DWrNZvURSt6XUnZxVpV4Lm6dGrr0P1P35_m8lyP4dUHEt-FC0t22z2pa43xRHTQgC-lIQOkxY6sc1FmSuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=nz_ebix55wfwqOb3UiYo74mHSIeCBV4ilqICkT_K-cFDTAlHr9qbr_BEgU_k9tU20tQUn7DZR5tdLFzgnqIzcqj7W09S7-eE_8ckd_zir7NSNEaYTekNd5SN_53Do2h-YmU7mXqATpoZN5YdvI7yFMm288xfHOqTZjZdzrb1JrBGi7nzkAYmkDWqnDapRrsyRL2UX38L1PE2iuPIo168Q2D5Pi2iJmKJ5Z3jMx1cDQp_x9m-txHE5frK5FOaNyvX9xA5DWrNZvURSt6XUnZxVpV4Lm6dGrr0P1P35_m8lyP4dUHEt-FC0t22z2pa43xRHTQgC-lIQOkxY6sc1FmSuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
ویدیویی‌باحال‌از مسی‌ودریبل خاصش؛ همه میدونن‌میخواد چیکارکنه ولی بازم دریبل میخورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23264" target="_blank">📅 14:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23262">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNP4912OK_Xu6EtYzYMlX2XUGPOKw33ZL6Heslm_fR7g3OVDLv5bwxltQE6glEgokERSkdfg5VzoiQ9Sl0Gy8asDOTZ5mpjLpltSqqU7Mo8XCwBH4LXJ9TAtBLiLeRF_NrQVScvk-EBqHRU9K34j0HlPWRJmYkAQ64lobl2cHmHL5EGqyi17Z_Qk5QJUGTbZhDrK4217uXvwzU42fNdvCbJNvjTlZeM_BqKzs0msSG22_hOH6yddVuzmhsv1488VeMgTK02f4YD_XDl4az353DvWz_b93LCSS2thJJZLCWo4rMaK29iiYfKJCUJz6h2isi74CeHe5BvSQ2_8v9H18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/23262" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23261">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=sbiruecc8Qs8MCKvu-6_REFLks0ZfqNUVFSOv8SVX62Elo602kK_CpWIf4MSS4Yvqo7SPIiQsx00-9U0Qp0yNk-7ZRWZBwk94RX7pOKBswUvZEDoeNGSbUyDkFzacSskdipF2QD3GzjUcZkNs-mhfA7Thl-OjG8--eCYwBL35AumXJLrmrFSXwoj0lxDM-wGJvNL_Pukl4gomMqq-7sJcquHNdyERjZ4ALNSa7UVjL_GZcxFqkA-lnVIUVcfJ6pn5nHZzhd_B_d7zNzoDy2jcpHc-G6OkOX6UOYrNVUtWOsVDOjQ26NLUsTnSh6xSBV2oeoRHqZc1yG2RisBSZzn_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=sbiruecc8Qs8MCKvu-6_REFLks0ZfqNUVFSOv8SVX62Elo602kK_CpWIf4MSS4Yvqo7SPIiQsx00-9U0Qp0yNk-7ZRWZBwk94RX7pOKBswUvZEDoeNGSbUyDkFzacSskdipF2QD3GzjUcZkNs-mhfA7Thl-OjG8--eCYwBL35AumXJLrmrFSXwoj0lxDM-wGJvNL_Pukl4gomMqq-7sJcquHNdyERjZ4ALNSa7UVjL_GZcxFqkA-lnVIUVcfJ6pn5nHZzhd_B_d7zNzoDy2jcpHc-G6OkOX6UOYrNVUtWOsVDOjQ26NLUsTnSh6xSBV2oeoRHqZc1yG2RisBSZzn_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/23261" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23260">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4jIDnm40vzGUk8aN00Izam61O9raEybSocUTX6rO59SXc_x5wDDrQGJ2qx4soi84NuEJWFaJfAxgneILhkQuArTEfxQOrSVSfVrCHOqQafXePBXK61vQ-bNwwBxhbIoUy5ewWLRxIWwFUdZYTNLMwfCYsfCSdNNPHOd7Y9zVQ1QGA0T7iCPXqSkWNjmb1ueM4N3-p6KskGyo01eJjrwkv93xDsy5JV5YfsNn-iLhd7j4uGdFfAsYhuRj9VcMbeA92oKt9yFHtYHsyfqjvCrAIBFdUWS-40tmRnEoi25QshdCzmJPdsWzfAcIb03v-DLBHTgn273P6ag22SZZSaigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دوستان‌عزیز لیست نقل و انتقالاتی باشگاه استقلال کاملاآماده‌کرده‌ایم و قرار شد امشب بزاریم که‌به‌احترام‌مدیربرنامه نزدیک به این باشگاه و طبق‌درخواستی‌که از ما داشتن فرداشب لیست کامل روبا جزئیات میزاریم. امشب باسه‌بازیکن مدنظر تیم جلسه داشتن که فردا…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/23260" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23259">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7927d57219.mp4?token=iFSCQ59aV34n2iZcT1Bkg-HvlsjjHfvuTwCl7Jf22IqIo82j0iDA59e_aZEOAWc-l1cERUyQWktvYNvsnGIWGtCIKbugHW1PAkuI9yCrkPA9vs3hDI7V2I8EUtOvZwQ2MWFFaoZ60CpC9Yz1BXzCAqQx4pVXgW6fe5xdBcSTOntZ0zfnq9eD0DnYZ58IHGjbBwlSxeLCCOGo91k2zPhDgEd5DOTSjjlTdGqHMMP3hQ1vXjNq-XuYbbP06owKHYSCiW0eTS2_VdhFVD_oPQTDZ8Z4iYe_iWhkocO8MjoSvOb6v2i2uqeBEyhXSIaHnpt2qTINDxM3oXbQwSTYhKFO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7927d57219.mp4?token=iFSCQ59aV34n2iZcT1Bkg-HvlsjjHfvuTwCl7Jf22IqIo82j0iDA59e_aZEOAWc-l1cERUyQWktvYNvsnGIWGtCIKbugHW1PAkuI9yCrkPA9vs3hDI7V2I8EUtOvZwQ2MWFFaoZ60CpC9Yz1BXzCAqQx4pVXgW6fe5xdBcSTOntZ0zfnq9eD0DnYZ58IHGjbBwlSxeLCCOGo91k2zPhDgEd5DOTSjjlTdGqHMMP3hQ1vXjNq-XuYbbP06owKHYSCiW0eTS2_VdhFVD_oPQTDZ8Z4iYe_iWhkocO8MjoSvOb6v2i2uqeBEyhXSIaHnpt2qTINDxM3oXbQwSTYhKFO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/23259" target="_blank">📅 13:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23257">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjBzULUFQQVWI6ciIWrCx3ZZA17Xzx1NmCzb65tKfh24-ymSDyRX7KiA1YtNh9J2401psaxqlvmZ6hoTQi26__vv6iCHRYUQso26tEREDUW21pAvplhZ2517x4ktar3hCW6xiIBPnEAceUenOhBoM4r1DHPIP0IgeuncFt9EBKrm4wOsLfL9sWarvjSmcs3Q6LnkdNSv2BioKkU6R5bG45yYIeS2ca7MZ0DofG2mnhcLT4xtjXTs4_XGONlWja8XMVUZQn62FdgZHq1b9B7KLuy6sAQr_-CFWhzuh-SK6uZmgikqXxqeudH4c4yBC6ne2WkzFltbLVsfpt3feL_auA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-pg1wK5YY32ILGFhDrRDPKoXZLPRz6mVFFZHR_2XkxxameXzILm-bo6zBdKl9TEj3u3KPHKfIOuNUasdM43ZQir-OEvFK0n1vtZfGEkRWwTMDwj5OuMppTWORpun9YUFKC91k25B6hYZDY1qzB2swaT0lcIklzKUunfhGRqHBsVtVULM91FwqGK-tUOyE2Fu8FBobdCW_lcRqobXCT7TOQdKJbqqFRWx6CVwNxCu52-PMao5xi4iYjgZZKAZaozAYHx6SAlET5BBumgLCyzkT--VHNtI_bEjyBnp0CKmmFfMALKYmpGEM__JP7BFEdGXqFkq5LLHZ0o25pSTlzCQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به احتمال فراوان طی روز های آینده؛
پائولو مالدینی، لوئیز فیگو و رونالدو نازاریو نیزمهمون ویژه برنامه عادل خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23257" target="_blank">📅 13:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23256">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎙
استعداد ناب گزارشگری روببینید فقط؛
با این سنش چه صدااای خوبی داره چه قدرت بیانی داره. رفقامون تو شبکه پرشیانا اسپورت تو کانالن باهاش تماس بگیرند که گزارش بازیارو بهش بسپارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/23256" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23255">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4ueYb-rjSchGzMSzErhpen9ClbFUbC_VNoouwFhEQsvJBiliS3-CCyvwqOhkv9IvW66yctTzhcuLQnn7WG63X0FlDmeD8jfLKdhDZb_L-49dw2zZqMi2d1xLUGY7cNZA9ngITBKaJJObM-gelFkjy0DvkjYbnHtLwCIUxR3Cu4ZvKRTvLfpFtl8ApkEtWSfoHYj6X5oAzAVGCCGB6cm6u_kbKvUApd07940lt-Oaj8eyuojpOyV9TNVVM2zfMUEV78Qar329lsubxaN1012jINK8aavgyRea5S8AT94CyNT5E2zkCCGXHGNNK3ew7y37MMle5h6BNCNdPNnCaxaLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23255" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23254">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N87rOJcDp-EuuU3y1AR8KjTJf25R8TH7yysKbE34OqDlph9LZXLCmzqMGNgop4poIk4pB81pctBuANpEZWJaCxZeTP8lfypEyXT3YZbzXgaoEfkrGay-dv0hSrhxWmiWvmf_e41etzF1A08iO8beDTJobvclSIBUF8blcouIvbFMgyIR-nAu-pW5dlYgQLGgssPJpTUM1ndzN0ftICuxVmMXSmzrHCc_m7Q4scjx_e9tHdCgLYGNuawXBNdnZDWhpifdFE-0w8IBaPfYGPYoWzZUkqZe1rgrfCE-cQitvlc6930bZ65NZlw7WXsIrn51dtiJcwp9WFnNTauapOkPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23254" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23253">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg2oDffGcLDWoVysbIaMiG9OrmC4vhdYTFZFk5EbZ_yNmmab8BMyN8P4B88k4XHYcESVofyqtGh1BRvmVGler2R2jJ7s0lQdJDhGny5xebjnZC8n73AlelEcq5XZYHYKSQzE1nvVzzHgqn42EHzXAyrAwsFq6OMKs6j-qWSy8McsIY7HaFlUwPkdf-6US0r2yRbldpt3O2-0zyaeJ_viWiMWVaz2sObu_P0mRYNYrksq0Gi8f7v4IrH7mRpv6pknoDXXZYZeQ866X3zkPDEgu951wO-Immgi9pRCKiHtrLQGXY7fFgM9AU-tmudFJazdM4X3VfCuVrHszWa_rizRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/23253" target="_blank">📅 12:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23252">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=kws5EdyoJuwu06j-2xUZzUJW0YCYMzfeD67B2cnSMIwpTMLMr2ObwA7V8uDg2oa4BlmFYXTviLj2QkT9FGxKweCR8haN8kPQGTvzERNSssneFinDXyZyxu84KUAH3_Nu5HhFaJBOuste6IRgxauFDCQITVZpU4RAZiv1lgyuYBadNsVUhpECvw7oWm_JStQqqVTJvV-OcmfI-n_4-WM0IkiHad1QpToNwxQcXu-lgcBGCsyZsX3gTpq9ePMkhey5qwC8TBYMegR6luO_GKfI4sWmbeRGy9dlXx2KrtuFJeu2cqdM-hHNojAxpfZaJjOLkmQHrf4HGigked5YwP5WJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=kws5EdyoJuwu06j-2xUZzUJW0YCYMzfeD67B2cnSMIwpTMLMr2ObwA7V8uDg2oa4BlmFYXTviLj2QkT9FGxKweCR8haN8kPQGTvzERNSssneFinDXyZyxu84KUAH3_Nu5HhFaJBOuste6IRgxauFDCQITVZpU4RAZiv1lgyuYBadNsVUhpECvw7oWm_JStQqqVTJvV-OcmfI-n_4-WM0IkiHad1QpToNwxQcXu-lgcBGCsyZsX3gTpq9ePMkhey5qwC8TBYMegR6luO_GKfI4sWmbeRGy9dlXx2KrtuFJeu2cqdM-hHNojAxpfZaJjOLkmQHrf4HGigked5YwP5WJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|
هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23252" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23251">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OftcdZupUKOZpQddyQT7GhNLmTwTIO63fqKywbxUsNtLw6kXdaOJ553hvWDqsUQci8je6Uo-j7Qp657O-XycCAsd5zM6xvgONjmljALMTHasSylk6nishnezMaiWo1byvQrk6aHkZrSqrIciSVDc14K3pL1PFreT73vymS7JIj5L5mSgb7LlQOfGPvMWZTbU8Zke1lopTvF4FEyngm-u1Ggh4oe-mYJOe1rBeqoYJl4kKTucLf7BEJrXCrQsEqwG6l5yfUc7wOJC0oH_hUH92CEgQNNrWMWelPaGkCK6QO5NZu2Nhs2_KGD3JvyQKHDA_VKZe-2FTdpoNh5EzDVR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
خوزه‌فلیکس‌دیاز: یوشکو گواردیول امروز در تماس بامدیران‌منچسترسیتی اعلام کرده که از باشگاه رئال مادرید آفر دریافت کرده و قصد داره بعد از جام جهانی به جمع شاگردان خوزه مورینیو اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23251" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23250">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXNeuV1LqJGxwcW1WHx-8PBnqAEeX8TbaliuM1MBRoHwCZ2WHr9eGLnZFC_ZaaDoz0ykE-bflPIELChhKdZBXwCqieth3X9fdawgf3_mq38AbHn9YMmO_DgIA8mpOBCor_05f5_yxeFY8wNEg4qrWV5oDB7H2azWvXvk3snC-VZ0JZKs9O7UVFfNDovNK6cYVWLzV1InsPRTKA0XD9sTqUoDXuGoGCWHwZ0Bg7SCfYZb2m_DcUCkdPpVGw_Vpajn-8r8PalR0oo1gyKsCakkUFoeq3XGsmY0GnWX_h--P7krFZXjGmK2HkGlHf0NNHGMzi_4qctI4044Y1FfowjehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23250" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23249">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKmK993hS42quTpqzkOVKbHYEy-hnYvE8waNL9MgtIDdLwc-ixIEgPfuOMoRxz4BtWXGRV1P_dV-jNATnx-OP3A6OWNhMV8ERDLdA0E-so9Jh7UKoPv1YcLSAeATzyvNe1l0mbqagspD8ooG6S4W4E3gR1FXVizrgoPihwxYDweDLg7BTl3sWo21ySpL60wJhClf5LZBrbuqtnNO__1WKXQ5qm4N2VyDkD5ldWPr2J21i4e8cHDTSe74CMYqkj2BfcEnTFpK0Uu0Le9OydCrBC629bM2JgkDrOcyxiBqi8q1SjNJf3kFEvVKksgtuF5IWtG3G6niV8Ivjo0--u8n_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23249" target="_blank">📅 11:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23248">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733942b449.mp4?token=iUBw5XRn58wDFHJiD9MOlqHWT6VtVceHk2dikPpPhJpjLcENWDitO1rvW91SkBsPKC0FjOWwmcvqcrtAtaA8xTMavskiA2NJ0l1y5Gb34jzbxp2gCAe1vZSf_KssBQKPTioSAVi12LTteeyrrb7iYdT0bLLFW78OV_m1TRJsNBg9cheurWzNaV4_cCpg3u6qXYx_i6-2BBZDfPUF4J5CpwwFY6HFyrwqfHZoYmbiHZpOekXP1CH94Pya2rWCfjDmt0cVHOFvKc4BkAIwZ0m-gyy8QW9DXHeks0FhTLGu4f3WpqEYqaiNpNySxq--5n98E0XLrEpuodzdRnPJLUnicQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733942b449.mp4?token=iUBw5XRn58wDFHJiD9MOlqHWT6VtVceHk2dikPpPhJpjLcENWDitO1rvW91SkBsPKC0FjOWwmcvqcrtAtaA8xTMavskiA2NJ0l1y5Gb34jzbxp2gCAe1vZSf_KssBQKPTioSAVi12LTteeyrrb7iYdT0bLLFW78OV_m1TRJsNBg9cheurWzNaV4_cCpg3u6qXYx_i6-2BBZDfPUF4J5CpwwFY6HFyrwqfHZoYmbiHZpOekXP1CH94Pya2rWCfjDmt0cVHOFvKc4BkAIwZ0m-gyy8QW9DXHeks0FhTLGu4f3WpqEYqaiNpNySxq--5n98E0XLrEpuodzdRnPJLUnicQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23248" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23247">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=oc9OMGkcXF3sx_0hWANCj73opWdEUiO8qYr33jW4o2ISQwSWKhTd44GKDZg7h9VjsoSeuYsk9g91lE1ekoJmkDWinoSzsWeqohWL1ArtHHo8q_ePf4ytuaIu6ENwT6gs1hBLKyueryVRByCIeAPusw_remQ-qcBsRiUKthlaUt0FhzdRAJn74_PsaJVfU59sj6MME2ZE8ULwZBCsbgOPkaum0CrP_zs8CD0TOkAc9nz2Qbm5tt1uRawPiiNI3mvhzNqLig-vKFrJHuNqdMVOjlMEDeRHbhk3xGPBoT-u1SakdvaNAI7S_OY9-Q2AYA5pFf9uKVN_Imo4lzZX44Fjeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=oc9OMGkcXF3sx_0hWANCj73opWdEUiO8qYr33jW4o2ISQwSWKhTd44GKDZg7h9VjsoSeuYsk9g91lE1ekoJmkDWinoSzsWeqohWL1ArtHHo8q_ePf4ytuaIu6ENwT6gs1hBLKyueryVRByCIeAPusw_remQ-qcBsRiUKthlaUt0FhzdRAJn74_PsaJVfU59sj6MME2ZE8ULwZBCsbgOPkaum0CrP_zs8CD0TOkAc9nz2Qbm5tt1uRawPiiNI3mvhzNqLig-vKFrJHuNqdMVOjlMEDeRHbhk3xGPBoT-u1SakdvaNAI7S_OY9-Q2AYA5pFf9uKVN_Imo4lzZX44Fjeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23247" target="_blank">📅 10:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23246">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=ZDuVBi4k52CG_2GhX7U-Zr9Gsr3pgRtKh1pToxBzLBwjgyouEG0_gwi_vdl4mmZlc3xA86z_qY5Jo5AVLAfcKP2_WKzvpQO7H4bHLlkE8kNejBVeExQQpwGOmxnjQHTvoZ8BVLrk9F7jRN4odJZqYmp1-6CdYtD6E-IGmFWAsmSYG8DI9VwDg3UnXHv1uHwZntoAbqVfAToKK_TBoKJuUxDl23DQYSoVlnWuv7DFUmXrZ5ImIHrSDipLZ7dfkSqw6WsVwMcA5lqXzOfuzDxTReIQV3-sptJgX9WLPxTqlFiZ3XkvaInBFu5cuZxM-Oj3rOh-q92iJ25a29G8NhNMyI9dFjBsCTAxP4Z1F6P4iYpopzN7JVGBe2Ul7BBaSwccSNzc2EXU_RTm-8zU3e8jcHEhUu5Cbe5mA7dpSUBpUhH9c2xLWkHUdioE8Gv6g0kfVin6qhj_b4XSXA5ZFbXpJl14j0_Jg77JoBTxPMnhTlzrGf0sxeVjSMxR5DytlDrv4Fw7LghFRFa96DOrhaV_aEeq75rtNDudk2ofmqVmVJO6vIV9TrWsz4HIEKMqDVSIvkxxTED0RE9B-obrG_uHnPJlXFf-hOChWSAMC_FT1mW26iqMtxRnClR2PjfhZ5NKBOuUz-Q8CiecJiv8DCpBGlDpENPSCH25MYCxde4kPE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=ZDuVBi4k52CG_2GhX7U-Zr9Gsr3pgRtKh1pToxBzLBwjgyouEG0_gwi_vdl4mmZlc3xA86z_qY5Jo5AVLAfcKP2_WKzvpQO7H4bHLlkE8kNejBVeExQQpwGOmxnjQHTvoZ8BVLrk9F7jRN4odJZqYmp1-6CdYtD6E-IGmFWAsmSYG8DI9VwDg3UnXHv1uHwZntoAbqVfAToKK_TBoKJuUxDl23DQYSoVlnWuv7DFUmXrZ5ImIHrSDipLZ7dfkSqw6WsVwMcA5lqXzOfuzDxTReIQV3-sptJgX9WLPxTqlFiZ3XkvaInBFu5cuZxM-Oj3rOh-q92iJ25a29G8NhNMyI9dFjBsCTAxP4Z1F6P4iYpopzN7JVGBe2Ul7BBaSwccSNzc2EXU_RTm-8zU3e8jcHEhUu5Cbe5mA7dpSUBpUhH9c2xLWkHUdioE8Gv6g0kfVin6qhj_b4XSXA5ZFbXpJl14j0_Jg77JoBTxPMnhTlzrGf0sxeVjSMxR5DytlDrv4Fw7LghFRFa96DOrhaV_aEeq75rtNDudk2ofmqVmVJO6vIV9TrWsz4HIEKMqDVSIvkxxTED0RE9B-obrG_uHnPJlXFf-hOChWSAMC_FT1mW26iqMtxRnClR2PjfhZ5NKBOuUz-Q8CiecJiv8DCpBGlDpENPSCH25MYCxde4kPE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مصاحبه‌جالب‌ابوطالب‌حسینی‌باهوادار معروف و روشن دل باشگاه پرسپولیس که اون جمله معروف و تاریخی رو خطاب به علی پروین به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23246" target="_blank">📅 10:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23245">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd_AVGE7sGQJmVEkwavqQ2FbmmmqlTxmbuJ2HK8bANE86dd7Ln34GRZV_nksebsWMXE3PqukwXN3xVlC7m7Vyre5XeO9ACf8BukfBFkw2hkcXGJBzt1khURrNczZ9zoZMR3mHr5SPsJiE2ooZff3QbAS3KwMAyrg0YPExhVIGtHATBQMUUW1yQMSJ9cjhgissCkIskSStA3mRzhGvZD4iJz72Q-TmZzPx-z-EIIooLFCj3kG_EDDpyrIMybwUhCA9Uv_0Go8KDGST-ZLakPoDivahHmeDVih6wewqOBwt65oEmBNlRgtXBN7tkCacEty96TTU5qjJRKXQySu5D2IFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23245" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23244">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5655edf133.mp4?token=b0JTzK4fhZa6cFqVwZqg1_MpiLBEOzP6AxLcLFIhacW1CdW6xl0GR92Go6-D0R9jaLgcxDkHZHzr-esKzc6j_HxAM8xlUYUiDEQKD9AwxB-edknfthb1lf6aIoeZ6s16eZpibXTUp-bPPmN3C42Hr0qk02T_NGakoBy-StBBY3Ng1p_J5k7RdlcnU2IjtEV0PxikjzDvAQFroJAdwoHOvVTzcqN3ge_fjusRH2NABaOoiHwGhUCnhb-kiQIu8tPRP9NWGbsBFDhBxIq3Kg52Nq77gYUBmCjhV2wULuDt9M9511M7g3D5AlEn3YmHaY7d7f20fARVGS3sHQGCjuZ6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5655edf133.mp4?token=b0JTzK4fhZa6cFqVwZqg1_MpiLBEOzP6AxLcLFIhacW1CdW6xl0GR92Go6-D0R9jaLgcxDkHZHzr-esKzc6j_HxAM8xlUYUiDEQKD9AwxB-edknfthb1lf6aIoeZ6s16eZpibXTUp-bPPmN3C42Hr0qk02T_NGakoBy-StBBY3Ng1p_J5k7RdlcnU2IjtEV0PxikjzDvAQFroJAdwoHOvVTzcqN3ge_fjusRH2NABaOoiHwGhUCnhb-kiQIu8tPRP9NWGbsBFDhBxIq3Kg52Nq77gYUBmCjhV2wULuDt9M9511M7g3D5AlEn3YmHaY7d7f20fARVGS3sHQGCjuZ6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
زلاتان:
«مسی یا رونالدو؟ مسی بعد از بردن جام جهانی حجت رو تموم کرد.»مسی یا رونالدو؟ زلاتان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23244" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23243">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJPiSBX7eV9rauRj7hL9h2iKgpjzJENPzOUGrLMYiBN-I0WP3m9eOAmcwNiBwNmq2CPHy1YpWdr8CeCwBNU7owgho5I-GbuIrPvuVJElytWbngQ-thq8bW_iYeaRf10gc0ADhQUgz_wWvkQr_ZoBNo16yAkGiHKDVBKc6M4NhS_eVMyCUrn3HdIIXewQmmweuPPG7I5rqAXlu2XuKvdgu-YZ6329LpalA718AzZEd7m2fgfIoz6s093XIEVSYKocLT0XJ8QTiyTsHg8Kkk_ht4FjpulpSc-9OaPWE92qTc2e8xs0AloAY7pV_vRvI2Grjlc7YzvcYDWzZJhomBIdXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23243" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23242">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=MGGQVpO-1UQ4XjCz-YMb-G6ijdSBr1TrnA2CUlAByDw1UZ9nX_nqi0ZBsNbP9lYPoqSsA4QkoNw1Re1no3IZhnEo2P3mtzcW19HNSVfPwjsahkpK3JqZKfsxaEdB8OkxMHQz3SAZZ4bJQnB1lOBSzb3-K96FcRUt_Z7V_KLGR7HmbvRYLe2u7RFrJjXrh-3ukX8zvhyAZoBoVsA8eEY3lDBcmsw1qXHmvjFktp7tw1mtZWoUQdsp8pFz4OAyLg17zZ9a6l1ha_do1ODWL6rOcgCq3MMEcFUhKkGj8djgb5vfUjO0nzQLcTAnfh1r58V1-j7O_bNAAil7V0_OZQKQti1BwxLq0s1cwBSxtJ5HMskNgw3YJY4zRy-hYp8miYimqtPUtpwqltRvuYtrKVORZkgBUaikw92xOMnOrCN6mYPZy0B32p1oAGuo3YBdT3JL58pzxycmQUg9fUVuu5DtgF9fIf7WyNg2qMmkaAGpgK5mfAblwRiKxHKaTF-Bx-LqM44ISZt-4fXJmrlbMwyAWeKpII5SP1zME-g28foMH7RoiU7Gfp8Zh0zNFOWGVFB2mB0d_f0ZxzVooquXjebf8hmILjjBI9t1Bn9NJJ8VOnAMTaIZ5fMH7YJvW-iYp8rJdpQsseGALaoZa1gVokFgi6fYS5UGt93O9ZKEwxa6pOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=MGGQVpO-1UQ4XjCz-YMb-G6ijdSBr1TrnA2CUlAByDw1UZ9nX_nqi0ZBsNbP9lYPoqSsA4QkoNw1Re1no3IZhnEo2P3mtzcW19HNSVfPwjsahkpK3JqZKfsxaEdB8OkxMHQz3SAZZ4bJQnB1lOBSzb3-K96FcRUt_Z7V_KLGR7HmbvRYLe2u7RFrJjXrh-3ukX8zvhyAZoBoVsA8eEY3lDBcmsw1qXHmvjFktp7tw1mtZWoUQdsp8pFz4OAyLg17zZ9a6l1ha_do1ODWL6rOcgCq3MMEcFUhKkGj8djgb5vfUjO0nzQLcTAnfh1r58V1-j7O_bNAAil7V0_OZQKQti1BwxLq0s1cwBSxtJ5HMskNgw3YJY4zRy-hYp8miYimqtPUtpwqltRvuYtrKVORZkgBUaikw92xOMnOrCN6mYPZy0B32p1oAGuo3YBdT3JL58pzxycmQUg9fUVuu5DtgF9fIf7WyNg2qMmkaAGpgK5mfAblwRiKxHKaTF-Bx-LqM44ISZt-4fXJmrlbMwyAWeKpII5SP1zME-g28foMH7RoiU7Gfp8Zh0zNFOWGVFB2mB0d_f0ZxzVooquXjebf8hmILjjBI9t1Bn9NJJ8VOnAMTaIZ5fMH7YJvW-iYp8rJdpQsseGALaoZa1gVokFgi6fYS5UGt93O9ZKEwxa6pOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌جالب‌از برخی‌بازی‌هایی‌که تیم‌های بزرگ تحقیر شدن و شکست سنگینی رو متحمل شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23242" target="_blank">📅 09:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23241">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=rZ5EqFW4WcTQ1NflKpCL81p_a-hNEJ0XHE3vg4k1tp-IuPbegghE9Pr6lwPRShhQSQQzbvqgr1SaeHpRhYiNBIWiawW-7ltWX3RfKW7uNhki6Ti0g-HaO1HRLPjYZWvHKthPMVCGO-K69M3CfH9UYwWzHSH_fJS85Zb9bK6ZQACvEZGSp07wLjL8qqtfanfTSuOZz-o9oykqeIYmB22-IyeJM9fIfpd8p7bfjiIyFD5bBpHKsXXvHBPLj5u_NxyArAHmCoa4ApgieokGOTXW0hf8nJXbHnJSppAO_NYUR30IbklrelmmhB40nVRxY1Zs8hHHBA4o5Y3rId0gt8cZ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=rZ5EqFW4WcTQ1NflKpCL81p_a-hNEJ0XHE3vg4k1tp-IuPbegghE9Pr6lwPRShhQSQQzbvqgr1SaeHpRhYiNBIWiawW-7ltWX3RfKW7uNhki6Ti0g-HaO1HRLPjYZWvHKthPMVCGO-K69M3CfH9UYwWzHSH_fJS85Zb9bK6ZQACvEZGSp07wLjL8qqtfanfTSuOZz-o9oykqeIYmB22-IyeJM9fIfpd8p7bfjiIyFD5bBpHKsXXvHBPLj5u_NxyArAHmCoa4ApgieokGOTXW0hf8nJXbHnJSppAO_NYUR30IbklrelmmhB40nVRxY1Zs8hHHBA4o5Y3rId0gt8cZ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مدعیان‌اصلی قهرمانی در رقابت‌های جام جهانی از نگاه کاوه رضایی و جواد نکونام؛ چقدر قدرت بیان کاوه خوبه. چقدر خوب و سنجیده حرف میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23241" target="_blank">📅 09:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23240">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqURB5HH3K9SxmghYupFibTjkRY-9M3rkFDOl-ROYOOsXY18OQNjV4p3eh2he1GqPJGXfmRiRsgr0YfO5uk4RRWS6OWX-NIf4xTBr9Y9fNgWzxdoJMT6Fp1AD1z3-k65jYnTgdWMi1ZBPX1iJ4fdXG1Wn3kmjbaHUPcnKEKPBNWTLiR4qUTvMwkEq5ieLPSWrQVCa2gbZz3GFjNsJ85u6mPgNZle2gX-Ukyemn1RUwin1oyBpe9t_TfjsXnd04l70IvT5Z9VAvE2alkOmY-UNDRokQtWw7aSNxgWbvveHMJXrLFzzeRIUKhyYY4csrvYNskyPSKLgdjTL87o4eei7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: باشگاه مطالبات یاسر آسانی رو فراهم کرده و بزودی به او پرداخت خواهیم کرد. اجازه جدایی به همچین بازیکن‌‌ارزشمندی رونخواهیم‌داد. یاسر آسانی و منیر الحدادی فصل بعد نیز در تیم استقلال خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23240" target="_blank">📅 09:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23238">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=aULsoA56L5gGQUAfSITaA3kchPnPWkOQLKC_zWTi5k0F1opWjABVY_I1AmK064RtORkG_ni2Mqd5TcXipBPzZayLQ5DncZuRQKse8TW27kGQoP1hr1DlgV7gNP-g5-aDkQ4nSasZbLeUruc_vv4QoQrhTV3b_qWPBJ2OP5eZaKJDPug4unb3T8IA040zmHXtSFrEf8jy0lPdx834y7HySI4OjAdG5651WTZiFlAfMyeRvDTF1tX-XyeiDnBmG5VJMXAFqMgsQFBILoWzpHZuIqPOxr85ftvlqVkRcVpB1I06IsMgSzF-StSWo-2XKafo_7xoSkHwE4i5QS2DicnPQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=aULsoA56L5gGQUAfSITaA3kchPnPWkOQLKC_zWTi5k0F1opWjABVY_I1AmK064RtORkG_ni2Mqd5TcXipBPzZayLQ5DncZuRQKse8TW27kGQoP1hr1DlgV7gNP-g5-aDkQ4nSasZbLeUruc_vv4QoQrhTV3b_qWPBJ2OP5eZaKJDPug4unb3T8IA040zmHXtSFrEf8jy0lPdx834y7HySI4OjAdG5651WTZiFlAfMyeRvDTF1tX-XyeiDnBmG5VJMXAFqMgsQFBILoWzpHZuIqPOxr85ftvlqVkRcVpB1I06IsMgSzF-StSWo-2XKafo_7xoSkHwE4i5QS2DicnPQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هنگ کردن عادل از مصاحبه اخیر امیر قلعه نویی سرمربی ایران ازسخت‌تربودن جام جهانی 48 تیمی نسبت به 32 تیمی: واقعا نمیفهممش. یا من خنگم که نمیفهمم اون چی میگه یا قلعه نویی تعطیله و ندونسته که چی داره میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23238" target="_blank">📅 08:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23237">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-ijUul-KojqE1YcADHYbyeSwXHpKigeUt0UvlcJJcKA1AqiE5fEft7dB9O9Tks1a38joM_bauzwqMyLddMPh_w0krE7vXicS-GKKywMJeAX84BygpKy64AcsmXtfiRwgmLlT43uFZlZVSLQdFkuuVK-6ray0T8eotl5iZ4Ba2Do0ywMI1uYmWSgNQ2n0qhCwlmzplHLEKi0aKe-Bw0l5luh2Z4oJamlTbiU5w2q0GuO2F6n6OX7Y-gjZEB4i1SP0zPDMrvuzY8wsCYXS-jV-pe9tIlwUGLNsBdXY1LEzOGnwj_ciuUz-xBUIHygCKdfgZqdbAnSuE_DRbvPNBj_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23237" target="_blank">📅 08:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23236">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23236" target="_blank">📅 08:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23235">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qillcs-VbEhxeqRPG8OFbQwNcteLeF_j_gyMrxv5DTRW2oGESxfGNO834dXad47q3mN-S3CpYM9X91qou2r25bmo1-fW8S7227tRxyRUPzzkUlFgny42ICmo0UF3Ddq2NrS2VDkQZFGAn-q8eLoj4Uvg-xLuQEfBivZs_TX_xX4drmFaBOd1LrvgcQU1TduZx0MtmRc4CJu3OUAhX4Ywd4hi0ouikSl076T6NAYJmM9dzVKDEhLCXvT3qinuMgsHUlJXqvdGFlFfpjuR4IUdMQusajJd5QYkeCVJZZ8lDb4nfoUmnXlNVaRVMwaFMY3mcmFjn3Ma9rg-h2cD8aZkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23235" target="_blank">📅 07:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23234">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fh0BoYezsTkon8r1QHlXADVa0PNmzQ5Z1jfJn6vHX7BhC1xmYGoWH7b2THgx2f86kPat9-OEHzCzitQDmNVNgRZ_OxKjOqF9YegF5tmqNMhhyEEoEJxNR1aIZ4BTz9Mb-1Y6Wsy4V06yjlkzA9_1SZ-tcMVqOZu525yzr_PxpQve72fZuBIwKDCaaJyeMM_teg_bby2dsXlFci16kNJ9Z-Z7J1qhD-Cw2AUiUTmBiPmItUlibqmBSaoqxv31h0fZGT_zwML2lmXlwdJ7W53yPiiFCtelPcUxjXRoW0H_u6gpRxL22Jk-sJn2fVJWFV47WN7zLlqwDGmlKZuBrUd8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23234" target="_blank">📅 07:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23233">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=ik7M8aMupMS8SW8tQ06fZc1h-UGQZMARXhqUX1bHYZbhWESHS1LNMqne8W6H2YALSR6kStti6cbkRZGrh8aKCbEGve3RPGOS3EyfEFNf7TpUFa2elLMAd9yEAv48fj8IynP8ehQqHdoYArwUBEeRZXte6U66hI2lG8OeiAO-Ex3o6W5M39ib5UeuGjrYiABBYnWan4UoBjMQhPcyOkabCMZS3jaOvbLgCUuL_SSIPBosi9x60widL-2Bmryl0jSDnDkfCzq6I6QFQc6Ng1-_xduS1nCY_A1OXytOduvskzy3x0MSrz_OWBPTEl9UcYWtIefYCuDlEY-1CRUoTBaC8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=ik7M8aMupMS8SW8tQ06fZc1h-UGQZMARXhqUX1bHYZbhWESHS1LNMqne8W6H2YALSR6kStti6cbkRZGrh8aKCbEGve3RPGOS3EyfEFNf7TpUFa2elLMAd9yEAv48fj8IynP8ehQqHdoYArwUBEeRZXte6U66hI2lG8OeiAO-Ex3o6W5M39ib5UeuGjrYiABBYnWan4UoBjMQhPcyOkabCMZS3jaOvbLgCUuL_SSIPBosi9x60widL-2Bmryl0jSDnDkfCzq6I6QFQc6Ng1-_xduS1nCY_A1OXytOduvskzy3x0MSrz_OWBPTEl9UcYWtIefYCuDlEY-1CRUoTBaC8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های والیبال؛ دومین شکست تلخ شاگردان روبرتو پیاتزا مقابل بلغارستانی‌ها
🏐
ایران
0️⃣
-
3️⃣
بلغارستان
🇧🇬
25|25|25
🇮🇷
23|19|21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23233" target="_blank">📅 01:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23232">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚽️
👤
ویدیوکامل قسمت‌اول ویژه برنامه عادل برای جام جهانی باحضور پائولو دیبالا، جواد نکونام و کاوه رضایی برای‌دوستانیکه‌نرسیدند کامل ببینن برنامه رو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23232" target="_blank">📅 01:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23231">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=qWw51er4aEMqKjyEKdyiNqxqpCrBIHdJrD6_qHISu1d8vcno723jaBxvoagFd88YEQDUOfUrnehX5A3auT4scXZj8CSaJmutNAJEZZQeh9-hgRTak-NNSRqf4GyPuzIiOKHHERrmp9NVErfy8NgPWq8J-liDbpiTyv4_HoFhrqLL50uV4N3JowzfQCMdpkt7BPSUn-aIDj7ZcD2ItrAnEaMIEfe0paxTb3dmr6wC8Lkz4VIU8oEIKLMA62eGntvlaAwgQXqbwLQ9itmb41J3NdqoPGWLffmdnaWgWCSrKJJvFNQYPKr0B0izFr1vILcjp_yNHwPrh5yGNvoFyq9rZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=qWw51er4aEMqKjyEKdyiNqxqpCrBIHdJrD6_qHISu1d8vcno723jaBxvoagFd88YEQDUOfUrnehX5A3auT4scXZj8CSaJmutNAJEZZQeh9-hgRTak-NNSRqf4GyPuzIiOKHHERrmp9NVErfy8NgPWq8J-liDbpiTyv4_HoFhrqLL50uV4N3JowzfQCMdpkt7BPSUn-aIDj7ZcD2ItrAnEaMIEfe0paxTb3dmr6wC8Lkz4VIU8oEIKLMA62eGntvlaAwgQXqbwLQ9itmb41J3NdqoPGWLffmdnaWgWCSrKJJvFNQYPKr0B0izFr1vILcjp_yNHwPrh5yGNvoFyq9rZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل‌فردوسی‌پورخطاب به دیبالا: تو ۲۵ـ۳۰ سالی که کار رسانه می کنم تا الان با ادم خوشتیپ و خوش رویی مثل تو مصاحبه نکردم! خیلی خوشکلییی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23231" target="_blank">📅 01:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23229">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ55NsOTs35s_uSEfS6mHvMH1FkmKQifcMIIV8Z7I12iExCjV9SUAodfUIoDhmLg9rnm0E5KxwzjyBlBLWSVeZ5YmXJglT5p1B-osaSkPKAxEOlj1odiUxzObaNT-2gwTJ0yUwiulvOXw3Pft_7lTBLUZcD4DCsRH2dl4gkb55AHVQh-QJ3lctVa3lnXH1g-9NZQoMHzkkwIca72m05NqhbXmaAJA7qRO6chTIYscUUBXQ3ecMCRRxBb1H9iBPZZqeXzrXSOrx1RmvaIyV8TzzrJIdZFDAiDixlkqc6zfvyqNDxF_nSLQrwWFjDbgBVCGxZ8iFRiM7Ve5zdKrceWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛اسپورت: تماس‌فوری‌خولیان آلوارز باسران‌تیم اتلتیکو: بندفسخ‌ قراردادم رو برای باشگاه بارسلونا فعال کنید. فصل بعد در اتلتیکو نمیمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23229" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23228">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4_0TkJGEOxUKTjzWMUzcu-5a5E3Wo5egsQkgcrLJFgMkGovvhhdjHWasfATOjoIShpXdrjm7Q6Xz2CwJkzS1He24DPYT9voWNW03iLPuhzTwV061OCWFg2Qx4RX2K8du3qNEouXspEeRh2k3UXoWwO0PJ6syszW78aCJKOhhMS5HK7JUAvCiU52ix161oKQJcE6aoOG2kWoPWFkQNl0lSmcNKENMl214flbbqLl0gCgB3hBxGagKFnpzEqe10OpvdWRC4iNtd6lilHe11VivDeNV7oB47MfxaGhoPtU-M0HpoFefs-CDEb2USmksuF2Eo0AkBsIhBZp_vQ8W53TKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23228" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23227">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gySTPeqFNulQx5vlfV-jSleXdIna5qM6lbasp_1mGrqTICNZ-gILUGE_3XX7K4vFRf6aA3d2hiMHmZlTwXFK-8tS4qk2jBltbHyLLq0ZvrSHrHlDFiio6365cHt8OPH4svlC9R2VmeQHK0Z-6Yh2TFGE0IFeBOHC9_i2rEvWHU00TsspY99MTCZt2kpduk4zqBe05Qjio_7nrbLvplfIpkVgXF-ZWYRQ5DQT7HSil0G8QZleQ-xRS0U4jTKrpHPr0KTmcH6r1tls52-xJ4a59iNk2ZGc_lSGgRIF6megAMN0whggZ00ZurN6IWYv0ko-72RDkOPOOJRQRX6QoILkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدارمهم ‌‌دیروز؛
استارت قوی مکزیکِ میزبان با غلبه بر آفریقای جنوبی در دیدار جنجالی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23227" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23225">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23225" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23224">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz46dud0HJQnDhwdhkES0dLol4qF4cUBcbzb6tv8Fl0CJxhv5vzu1DK2fei_WjClMlso4NyZy0QVmo7eDLLjDEJfZFN983TRD52cwd4BlGsGzpZsaYVU8q6DY4yENTDfIuW2j5t9Z4aYeXGHhWu2D2qkEATLSP4_fz_xmb1lZGxvp_S2cCaWtCnSGoh2Vz1JxbYJ21hVe_ajQIT-6wqac8nL__ygNIsROhjUf9W-yJwjdzWPW4QQW5tKwG3zC_hxvJj-NLwvyfkt8-CH4hkkVU736rScPd-I5SvpbN_PKmOmNjCRcl9crYREH05go4MtyV6BXVZpad2uVddNJedsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ با وعلام رومانو؛ برناردو سیلوا ستاره سابق منچستر سیتی با عقد قراردادی تا سال 2028 رسما به رئال مادرید پیوست و شاگرد مورینیو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23224" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23222">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WSKKCcn1AZ7lHECvd7FvvIbvZdqIipivKjGgbkaFmZVhqURabOtT9BiJAYa9Yabg0pDm10eKg9kxDuehaNpj81TgVMN8MAjReNer1AfX9PVz_cVLz8UteD40d0Fg9hrqs8b100wz70lE43gVBWewcFvPumBYHg2QMouL8rxONICUWPiD2I03BSQWI_rMZ_BeR36zAcK_rEHSydo9rjRK8E30TW9KHntOtg3WCL93Kqx7iu5fHSASI-iSw4qFzlNfGggtLf-patEI6Sm9_5URYd8aVgv9LNo0cMB_KFTByp3P06S7SZ3LX0v2qyzG66Y4Ff_gLJIevZPalb9NVOdqBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tg5YDs1fsz3tRCWGmTfndFXf8JGuq3NoykUSQHNiGTkZxXKVScbyDAzGa9v7bY_gaqTo0I05rRIiHywV-5Im0k08m_co8JICXaHUMXjbo_pnNiUanXYxEm6jmVC6r_DZll9SGPMzsHra5WFzTHm1bpDbXSWhDwFNeBdp9C2SwLT0rOI6VSEMUGvDU1TFLUBWb7IBRcgVDrxbXWNns9nQA8QtP5-D2bLFRVfNtpxtKtKPBKzAEvuWHlJUNWB0UL_nE3p5F-YZ4IVklvDz_QIcITR8U2cHAeNp1tGD2jGRL_Xesetb4-sD75wF8sBHft8tiK_5mUnwamSGhNnZv_SOsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23222" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23221">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdUraStrqmxIpbyn-P5KFkLoGxSJ8WJ9cK1pFpDyk9P428_JebrOetgiZT38sB9dJiBGLfwFydazPhqu_YZ7yl18PUjPzFvbk2nrzzUn3UKBYZTCOnL73C8JGq2s70KO50cbYiO9xf1TowF4FZ6rtcuzyW5gSJ1GQySK3RMggcyycBa2Tx4V-bt-wpxyZOfI9OnQ3Clwr-ne9ZbJtIO2VRClhuxwelDtexzz4QbCatis9GhT9Bk7c9QEe8PmIMPUkA6cMDl2EmH9PF6iT9Yx97L5RRnGYgNqlTvS6PItTAf4lG5bVOzuRCBnoC3sdIvXR9wFdqC_n6rr25P-Lrk21A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حیف‌از این‌رالی‌دیدنی‌بازی‌بامداد ایران
🆚
برزیل؛ شاگردان روبرتو پیاتزا در نخستین گام لیگ ملت های والیبال بازی رو سه بر یک به برزیل واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23221" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23220">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq8SMvAs2t0WPBAO4neunU1e9Lbyr1Q9v3HpB0V_nXimH-bB7u0b_pUdw4_TcF8GjuHsEKND48e91eq12_EnRQuBZ9-x-z7tmdsmNoifEeCGqsEQTXNWpE7oDO-zr9qC_9G_tT756eZL4lM5U-dQh9XN4rcuz4RwS4i-lJZ09JMDUi4EzdPIAFBqWQk9C_pDAO08uqprCUHE5169OZuIeagY-X-UlfVe9gbuLpVUhCz4hemlnJF0GET6-rh6g7w42bEU_s9ZVFljEPfV9R8mILudFHm5HPEMMqVMmwQl7RPbSJ59Rakc4YD6b4kv6ow3esCdM4ykh-qPsnLHjLbWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مربی‌بدنسازباشگاه پرسپولیس ساعتی‌قبل به تهران رسید و از فردا در تمرینات سرخ پوشان شرکت خواهدکرد. اوسمار ویرا و کادرفنی‌اش نیز احتمال زیاد پنجشنبه وارد تهران خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23220" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23219">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnvVoUPa8GTrQreewiVuzv2UX3mOdOKTqTsWWeqEiNrLyJaMu_IZHNQPELEOIi3Gps-_HPF7jDkgj87dJPc74-W8xD9SK0XOExN6jyqWCRVsH9Xs80-UflhZzreI6rl4hEXclQXuAzsYpfOk_8HRmdKW3huUvXpS8qkBogvY2NXeuAU4BwN7n2sfqRgaFoR4wM8aVJaHdZrgWzYTHr1pksbk8rTG5TFO_dus7DqeeOsO_uozYtw8psv_nmaojiibB-mN5FHdxvR15oozYxLMTBEOpN0g5gpkSOS7jQsOyaQB6zjW_xZQUKdJ5lGnjpXEqARIs7k0gx5QKaSgqaKWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23219" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23218">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mckb1RchfhWAYF-KZnwqOWKu3uuvSsU_XtbzTZI7bk0a-5K-SJS5X0HmbMyqFFHt85R4tGRbOojiW0CkpLXbOSHW-no8uPF_z6NYUs88s3kmI2VNEGfzj3thCvi1HNEChIfZU0qV2kQ8nhC9WStMv3m6SCyMf8Zi7PCj76BJHUvznk0I9asOyjGKUMsLSM8TX6LCY2sFi6EMOSROssvYTv6NrOBO_0aAbS3JpuVeXzpaJk-zJX6-qHIRUKN1WXc45dvvX3bKPBtHqqdZ8eYFc8dG9IlPG2n_5CTIEDeP0RemQUC2gTKO2qgtA4xFzyp0GsHx7YUunzg4KKimlJ4_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23218" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23216">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EiMeAzlCFWKHh6cK6UZs2F4jO1SvTz5AsPW2w8ijX2vdfQB0EHGVSDJ0iQA7IvGq4GA6wlBlBI-BzKhQLTSa3wnSY9T8QWqSGzj10N84RJ2dlI7R0jyDK3Y2ceOFxHVRnJ27p-GIuPpTKWvSiidiHD4X8syZPA9BLRYEqOcEgRB_FvEpLFJuDrDlTi6VGl-p9KIcgK1F9N-9t56aBmByN6Fft2krDKPAb2V7C78rJcKPMOtyyY-HGjMtfzixMSePQN7itVN9YzcReab5IMrxj9X6UoOCa-E_TlEMx7OTcThynYEFlBfEQqjaFbbOm7P8uhEOijhzy3XGvo5ih2DYIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sy9ASiJJWIZANJxDpxTUF53UjY90ptaWmYRPHieFIyakmRV_a5wKvdUxCyo9HlryInedNfre3f_0YaiJH9eow_Zidse5749nsIeBMb6cVKeasGzFGHGUgdmL_5TbKmgOP5zN_ujpZUsTGLhWXNn8sg_41PtziUp1UdUXrzGaW93aDfLdy215GjMSZz8uOKtu1dBDMovdgRwW-fWwwBq5IZPJi43jP0MHONFhUKzD_gZGumOyXbAhD1VDdv83LczDKj6oAj34jubjBl177Rf9Go59mylSeSabNTfICXGbqQFDGxYE80p8rYaHab8GEzAsMrWTKdkpQgV54MoL5oYNUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23216" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23215">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ariYMseFxVa0GSjiKiFb7rDBMnfrMyAdj-9nVBTbxOuyk4NOx7drIw1kDnXbkKTblxioRdcDZkuolCSTzGAxjGYxzvFiemY9gMCsvYYQx95Z0E-WdNrSxMKxpAC_yZGad1tzF4LiMy1iheZ4DAEzeIptFzR-wbgVVBVTeok54GDJ-t_Lvwhngc05a0_GpELod-e4Z-thAr9UGxVGD7v90dYcwmiHLC4_GWYX_BJF2ITE7EYTEFGFYMKgght8qyErKDkQAR-df4pCaNPD2mSkJb1EYUEXwP_OvzvatqASBTcPOEGl6MAKDLlRO2DyMX297-3oYQdBUjEZorzUNuOuog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
#فوری؛‌ خوزه‌فلیکس‌دیاز: برناردو سیلوا ستاره 31 ساله تیم ملی پرتغال برای عقد قراردادی 3 ساله با تیم رئال مادرید با پرز به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23215" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23214">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=dDNDKas5RSRP8II1iJktsCF6JR7_3SH_bI9OYTyQdbTefUh8KdpACX-YCQITDLLx4Ip3LcGJiyhZMnJcAeju1LnyRRQy79-HompGRzzUuxFPP-6tFdBQkpuY60QNeMjyr8aFu3geb7FNaZlYSsHdd7uLY7lReZNxFsCfI7UR7wqOOFdXJ4MAhEjsxrr2Stwnnq6pGq8_eelhsvTdlXFZkuMXAoQwT3aPuLxWtx-IHTo8s3XMvPqddam7raTD88txHhQEiSyhTw1OInlxe_Y5a52siRVSCDmVUfKlKzCnYnufCGRKbmi01P4mLnQNxfaZJouiR3Bcot-IpktMD3c61g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=dDNDKas5RSRP8II1iJktsCF6JR7_3SH_bI9OYTyQdbTefUh8KdpACX-YCQITDLLx4Ip3LcGJiyhZMnJcAeju1LnyRRQy79-HompGRzzUuxFPP-6tFdBQkpuY60QNeMjyr8aFu3geb7FNaZlYSsHdd7uLY7lReZNxFsCfI7UR7wqOOFdXJ4MAhEjsxrr2Stwnnq6pGq8_eelhsvTdlXFZkuMXAoQwT3aPuLxWtx-IHTo8s3XMvPqddam7raTD88txHhQEiSyhTw1OInlxe_Y5a52siRVSCDmVUfKlKzCnYnufCGRKbmi01P4mLnQNxfaZJouiR3Bcot-IpktMD3c61g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد نکونام در برنامه زنده خطاب به عادل: پائولو دیبالا لامصب چقدر خوشکلهه این پسر
🗿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23214" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23213" target="_blank">📅 21:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23212">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHQjZ8T_85NvbGtajegSgirSza6FPCUSzBrkw7gvGLtD6ePjRHYXy3ZR0bL6AuNeoDWC3fT2fmcg09LKagptJuNHNQYZlx11PWuxz_HMLCEnT-0HkAMM33rNqGNy46HMWkOujdyyaFvYz2ah9CzGu09BSG04y77PAYFKmm6Y2qFi4Ft31hk7ElT-FMX0l_IRVsAizYZ-ueHZZoY37wXCKuCaOJR6g0XqihukGqIOts5PRFGAU0uWe_AyczNZ7Of5UFo5WPKS_4jhamZt7fhC7IOI-LvyimUcI1czZ5QKYWtM1CdiHVWa34zRs-5lULZzTL2YBUE3x3LNNLHecdZwbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🇦🇷
صحبت‌های جالب پائولو دیبالا ستاره تیم ملی آرژانتین در گفتگو با عادل؛ برگای جواد نکونام و کاوه رضایی از این مهمون برنامه عادل ریخت قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23212" target="_blank">📅 21:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23211">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUolcgK5EOKcAWya8tNYalCjYMpJ_4LgYsh9jBue8EQXeZb3bykmgNI3tRDcsEa_viEgetBslDSBhn6uWlIvGtM035OHA2ivJwfMfeHtFMWP2gf-NGtcjzZWojvkXuVhIQXrrH7WOJZnC4lWyGnQvP2qxPmQ_W5z-fx_G5aPXDYThntGfNSQvnZWYTWTAcspOiERzoCeL43f9uvzx6pyzbPaU1PpNiGIMkYJewQuhiFm2AYS_7GvaqtTOPD7gryqbMmTr9Ism4ENgzIdymt6ZnuDloAsBoAdzPh7IL29ktWPeAGvDT1yAR86uQz1WKbfh017YsVI9wy3rn1xPfQVGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ باشگاه رئال‌مادرید تا ساعات آینده خبر عقد قرارداد سه ساله با ژوزه مورینیو رو منتشر خواهد کرد و رسما اعلام خواهدکرد که این سرمربی پرتغالی بار دیگر به جمع کهکشانی ها پیوسته است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23211" target="_blank">📅 21:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23210">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRw4NnDrnjWUBbxHlfSSxu3eRIY5Tv_YzushwGUS6ZkfQh-z3UieRl3yUAdLTJQASjBhd6hQZ15SS8h0XbhrLPMxqEdosoDqmh6b3FnDaNimRsqv6MqwrBDAvf8dOvk_qujJc-zuONkfLx2ugDkjKoTMDr1H7khHnHT-OSIm7mV9gpk-ZK7e3ljfv-FU2PB44WpLvGWnJoDLTwznZ4pUJCAW7Y7yxEqzNa3ByGfvoYtsD14-KyryZLPFJ33idr5Ue0hfe-2qVPl5WcjfXy7PSpueMRMkVt3tkEk7VZKZQIUFUf8okg7_gQgEVMIh1st6oNhQeT-1EpPLOURIjyCbCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23210" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23209">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=dRvmE8Gg-F14ywZWT6VgXAC7W6cFy_zFpm89Utg8uYrAopByJkZgDzo5E_4OOU7u8vGipoTDkhViT01KuPHgJ-jonUGefid4eLg-0zJA8hoBKexlS6t0ePbbgmkMTEWkPbwkU-MOnvjgDAAc7vqLNuZYG_s3gzM7VVg6Z5D3I2jWigO1e1M5EM2qB2D3Va9tr7Us9DCK66DALyERgbsKo5eXjWBJAU1iZPvcjx0aqVUb-nIOWRrKFTRmlb0kLOJIUhIJzzuZyCw0EQdfrasklyrTezYXb-HHVTmAKWBecpc1JPxVBNSbEMvu0mAzbSyvjRtoT1N8PGGUVJ2_vDklQmJGkk2wWmNdIe7ELvLtfauU_N563I0FzEX4jMd55LQjVhcBch8iAjcpPx_Ke-Bedc2wrcNa9MFTkofoD6zYzjRRaX4T0LKxg1_JOPGBn7bQ299_OCV7xQC78SwG2rpmihKPxl-0V8cZvhox3IH3m5dJNXdFyH6fxR3FZbwnXMNgMqpzbuIBsLKxAZ6tylgsBVwifDnOaffCvdKqnRwkkB-y_obFEQ5EPb3tRPt4047GIN-Xvx1EJ4yAxJxSTGWC4N1xEa5P5XpSV-7W5rgQE_jElrLQZ-Xn2tKoSzP_g0_D9c3abnCKJ8P3ANA1n8kjcwTmrKc2AUkEsEwIaV4ubQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=dRvmE8Gg-F14ywZWT6VgXAC7W6cFy_zFpm89Utg8uYrAopByJkZgDzo5E_4OOU7u8vGipoTDkhViT01KuPHgJ-jonUGefid4eLg-0zJA8hoBKexlS6t0ePbbgmkMTEWkPbwkU-MOnvjgDAAc7vqLNuZYG_s3gzM7VVg6Z5D3I2jWigO1e1M5EM2qB2D3Va9tr7Us9DCK66DALyERgbsKo5eXjWBJAU1iZPvcjx0aqVUb-nIOWRrKFTRmlb0kLOJIUhIJzzuZyCw0EQdfrasklyrTezYXb-HHVTmAKWBecpc1JPxVBNSbEMvu0mAzbSyvjRtoT1N8PGGUVJ2_vDklQmJGkk2wWmNdIe7ELvLtfauU_N563I0FzEX4jMd55LQjVhcBch8iAjcpPx_Ke-Bedc2wrcNa9MFTkofoD6zYzjRRaX4T0LKxg1_JOPGBn7bQ299_OCV7xQC78SwG2rpmihKPxl-0V8cZvhox3IH3m5dJNXdFyH6fxR3FZbwnXMNgMqpzbuIBsLKxAZ6tylgsBVwifDnOaffCvdKqnRwkkB-y_obFEQ5EPb3tRPt4047GIN-Xvx1EJ4yAxJxSTGWC4N1xEa5P5XpSV-7W5rgQE_jElrLQZ-Xn2tKoSzP_g0_D9c3abnCKJ8P3ANA1n8kjcwTmrKc2AUkEsEwIaV4ubQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23209" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23208">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709c123d60.mp4?token=M4u8mmh6HyaJrIJ9Ivs67ZR3ZHY0gJU0ROSfzt3FuNwvyKdbp7WmJVBGJNc5716IDXVRk-3_StIvObQ3y201k-2EfKWjMgwaZRnEsZ7zaM91XXo6vE6iyVPc_nUWyFWcdC07fYNB5WDFiN3V7lv8ZLE67UZcmG8kpdtujS2ctvTNOdSeuhsJyo9pkqMDc_LtBRlAs84nT5sRUdVvfIcm6YupT1R2GIRKNlLQvHmc63REt7V7ZxvDYGv4AmAJo2luX6MohK8wCRBAhL44AyE6f3-sWisvr_QdS1k6Y58hYti80SYe_08mCaB9wjhdGoM-NGx2CDtMSiW-dNJPalRerQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709c123d60.mp4?token=M4u8mmh6HyaJrIJ9Ivs67ZR3ZHY0gJU0ROSfzt3FuNwvyKdbp7WmJVBGJNc5716IDXVRk-3_StIvObQ3y201k-2EfKWjMgwaZRnEsZ7zaM91XXo6vE6iyVPc_nUWyFWcdC07fYNB5WDFiN3V7lv8ZLE67UZcmG8kpdtujS2ctvTNOdSeuhsJyo9pkqMDc_LtBRlAs84nT5sRUdVvfIcm6YupT1R2GIRKNlLQvHmc63REt7V7ZxvDYGv4AmAJo2luX6MohK8wCRBAhL44AyE6f3-sWisvr_QdS1k6Y58hYti80SYe_08mCaB9wjhdGoM-NGx2CDtMSiW-dNJPalRerQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور تو ویژه برنامه امشب پائولو دیبالا ستاره سابق‌تیم‌ملی آرژانتین و سابق یوونتوس رو بالا اورده و داره باهاش حرف میزنه؛ صداوسیما هم داره با خداداد عزیزی حرفای کارشناسانه میزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23208" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23206">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ft5IcIZa34KJF9jA-_1PMmsUnRKCw0SqgXnFD5VfgLlugCCaAcE_mSa0BpFEaIMF_QU0yJUpq_qzAOELnG0BZ8XrjXGlGugi8DPafRXCV567mvzUBtRqwLemcvl0mH4SzWoiKQXS7IcHTYVnF7aGfVK0GyxhU2Ix6KyMSim6b5VlN42uY1lXL_MZLoCmBI02D3kuA-eYZbOs9XptA8pQR8Ny2R5MV63hC-8HH9HBMmXiUIBEGZclaUQG33swch0bvjmZ7hpJyGes1uLvpbUI0luBoiFrPykbwNJQF-yMHllvqqHfv42zWaPJ0_tQclmT8xeDpCz77bdP6zqofSFvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23206" target="_blank">📅 21:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23205">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgpkRprdMI-9VM8BuzTMTxQhTtPmwnrWHKJZcBITnUIAwlwX8_y5dd8a8A48_7U0vpD3crdzTn08UZX4WB5GO9gjLKYik3oP9rIqt1rv7o7P-Q_RUQOIW40XsPlnPcObzglBwioBKZ3DVg1ueoYPbCZnT7yjpY91DC4MYyoDZDvZuqH6nPbfO9FoY7ItPtd5MfQRWoCFP6WE-L21HA8XNhSPBY37cCqIKs1--bHlvn54NX-e7t3qOeoZY52g4Uf0yyuUgLwkt4l_jMHYUpDxUIy6j14GIP8v5fGGJTheOdx_e_EWNgd8YrYwsSAgtz1pmYajT3WEXAtVcR_5Ry7i0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو: باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23205" target="_blank">📅 21:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23204">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlhTuSm0sz77XEfvPoDSm11Zj9EuNCsj5jfs0Frb8gV_nj7Q_J2j2bUnAaXd84RpJFUPaQcHIJUtaUJuzYbZgxqDutcfsSdMHWAI-G5hoOKJwYVwUG6v99pPI0czAmcXojceQCzm9YN0tD95pgakEUEnKRiKq3NsdEZg_wodooevHJ0ATKHK6uip_azhSEfTpaGfBfteq_4zzBt4z1VFkZoQbfAIcb6hnz4n3yUP9P8znAsFTv2bKvsnv807i1t_TADean1JkyUXhKRG3SFxtswMw2TeF-nS3P4W5BqTZxjBsqVQYSU5djUcUJYWneZYjnego1QcC0eHXpETUZBgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23204" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23203">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgWN2qz_a9RopIWbQKVEa-Jy-haQD5m4XbZ0yf6OGAeRoatz27lICo3o3rkN_M88HR1a3vqDLGsuTsEw8PZiF9VWynhVYRYkwRIwpYqQ4ItSHwWaDA2KVXCsPBltTETM5rcZsDKepBlBN-q4JBOl0hy2Uu2CHalmri63QSRByIe-djXEuw5ZJCZD0rgt51UwB3QKwQROwIB9W9AMRazcFqXijV8AH8KcMmiVM4LQHgN9wcAFqKsZMTNtkGwnsAbScZIw5ATSgF8ld6EI4NGgmmKIKLhcotYa5gzNZUARv7LBJjNoqUnJWjESHz2bWp3KR_QDXl0sm8VBFlrHS3nTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23203" target="_blank">📅 20:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23202">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3b5cySAf6ghMs40fjrKv0GiRYG7eI1YRogBuZvWJwgCZw8wn7OI68KiIdOI7Z5AGuwxYosTYmJCcepE56XcwtCFjai1Z1ce42HLNfT_Fooqep7kYq973XGIiysAGQ7K_Ob2nuVyqMG_ApHc5wR-k8jZfVLDY9Gy2t2JnGFe8U2KyOMcwvqun0lrdLBWmRbLP2-TtO8xX3JhHxdog3njNUhFudowuOcYYMiinm9VQ-XbeFESCkufT1y6T8iagU49I6z0ctQkjasMbVNG9feiUL1sSjki14xpBDUoLbx6RMViR2kM-m_OCKkHq8vR6JkRxbThreVAiWPsH6C5miPmEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23202" target="_blank">📅 20:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23201">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKkWLth1JdVy-cHz9JqHpguYVhrlajYgtb0sEBDvKkkYPnNsZ9QWeunbDi3DepIQbsWG01GsuBSOzdT8ezbjqN1G8giFm3tZe9wOSr7NhlZqEtjLNGF0LmczbLDn7DR1OB0VdW-fp4ddIzxvFhx1rUkbUWM7y8Ub16Xv8H4GuE0l-xqOxsK61a-Et5KGYcbF-LfriFrFJ4PJqa_GNgcHYHbZLE6ylcor06fv-Ht6eiUE7lKsefA_JyACaPbuBdhVLaOCo4_FPHtyl05fUhGEDON9pCbH2DEZv4K0Qw3gdp0gj7rFXr2Y7Uugf-asCpZQDRbvLzr73hgKhJg7oAl_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو:
باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23201" target="_blank">📅 20:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23200">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtPOTdav0TXGcKKXkPBi35UTeuZBVQFvcEWnqw2XzsCSyxqDpqjVYgE7L6yApAL88SKjIz7oq5AogFXWHmoBEZXVl_EGVgLp0-kpz0CKQzTjwWA7hHEguJURYMFdWpEPzNF3eiyvGkGDgruwE3KVuSuZ3fULiUVPfoXHgTzPvvP_-ljhDtNR-_rTwPrGqxaD6L13K99_XeEM8D_hJYhCCMJOr-z8IcbMuDYR6C1OVEzH4UnW_94w_X3fcOQ81DkdT5N3T0FlgV-0ss3qbn3sOwFy__XV5D341zLMk3DdBZ5Bdv7OKVw9TdBjh1s8mh-_aJXH8Wq5RTskZa6BADwSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقا از طریق‌کانالای‌بالامیتونید مراسم افتتاحیه جام جهانی رو بدون سانسور ببینید. خودمونم سعی میکنیم در پایان مراسم ویدیو کاملش رو در کانال قراربدیم برای دوستانیکه نتونستن مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23200" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23199">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myZKUbJviZKhwS4C3HNXxj5XLSkKPzUL4ENX3PT_hjaeRLoG7b_pskJd0TBGb2etE4_uQ8J50ERTU6cieh8thhsNPoyGWa0whv5Hcriu0snUWdkzqsreXY3NcrAseKq-BT_3OUwuDzCayJz19DugP3eGhKh6f3cHIAwz5tmrEqv5BPLrAIzuRhERc7cyfMFgeDxDPgNAivdvZBQTqgXInkjxu9c8cdkLlJS9LsYC9UDiqM_Zfw-9L4f2VKyxpvze9abtOU7DlSvHalWDTsmN8X4emzlDt4eLCdkDlodrgqIrIhjMuhx8X4sPYV8DkLbzwDfpuYfnlfAY75mx3r4mRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان: بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23199" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23198">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTBelUld8zPNfpQYqHsiBekcRZmRJp8UNjSazfnowuD69FCxjfjTk79PyHFHnecMSLvTqlo4PBM4N88xgZgGEs15yNGAGusJi7UPIP1GZPdkyCL7jveRO2pevFYya_gJ3XccJ2lHZIvAdIR0k-l_g7i1BTpSNT1sZP2J7qh89vTRAhTspD20WO14KM5IaIdP8qwL2TV2So10OTHrzCmtapSlR4fAwL6s2yIgQptFFByhsB7HLlxuPZ5WH04hs9jA0CnqfHCiDkRHlgAKS_7IkgjBgjYe8Mx6bRb37mX8m6WXZXZBFIiBa2Kbwu9ruJAPKCfZ5zhMC6vhObwFuJzP1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23198" target="_blank">📅 19:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23197">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgcKJXJX5zdHbn1mMqtlwqVeXuYz-u6J50XDRyAz779BNQR1CmLtjQFCzRJFOwLKn0Lk2Me8ZZJL3AMC_dHS0TgbwFVuCIDalrH6PtlRHRh-EvOQ4tUeUAj9RAn2dTFOR0rG-TJ10Uhuts048XyMvLHdqY0gWlJbGaj5CXor0p82wHcfIxVR6eUJIaPt13t0tYVZRRyvbmnKiDpEspAU4Zt16eLxmWRFnCf3mafQulWgQGaIGQZ1zYWLGvtLO41sTqysGElPrw3g5D1Jp-D-ExpCk6U1mh9jkkklPe2P-lK-p1zeMrRjowDM0sM5PPbWVxeKW1L1wUlem0t6xjxYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23197" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23196">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jz9UR5DnZbzsGN44i4oVIMLOQXRIb9hP_qYYczTjyz8kTjJXo3bMNKZlM_WTLYVC-dqigo-OgMp8ozuuoyWc1IEUcildXE3Ua_y0k4ayuvhjY3v3nAS50cN-ikguamDQ-cBWKRA-F1j0zs5-zAFeDhJpQUumuKjn40HwGHrMMWUqeucUjxIfAMe8S6vGq8rKRwLWtwpiz-I3wZHBiQmbt92sL4hAEs-ufYJiOfv5NYZvBw1MOq3IsT4ts4BdBkDfkwTZxyAlC5RQ0l0suTxI0Qmgr3SApwfskIL5_WxLAvq5rGZ-kCWfZURRaaMY67QAJBhyjqFIoimcIP3uzazKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌افتتاحیه‌رقابت‌های جام جهانی ۲۰۲۶
🔴
برنامه افتتاحیه در مکزیک
؛ پنج‌شنبه ۲۱ خرداد پیش از بازی مکزیک و آفریقای جنوبی؛ ساعت ۲۰:۳۰: آغاز مراسم افتتاحیه؛ساعت ۲۱:۴۰: گرم‌کردن تیم‌ها؛ ساعت۲۲:۳۰:آغاز بازی مکزیک-آفریقای جنوبی شکیرا، برنا، آلخاندرو فرناندز، بلیندا، دنی اوشن، جی بالوین.
🔴
برنامه‌افتتاحیه‌درکانادا
؛جمعه ۲۲ خرداد؛ پیش از بازی کانادا-بوسنی؛ساعت۲۱:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۲۲:۳۰:آغازبازی کانادا-بوسنی؛ آلنيس موریست، آلسیا کارا، الیانا، جسی ریز، مایکل بوبله، نورا فتحی، سانجوی، وگدریم و ویلیام پرینس
🔴
برنامه‌روزافتتاحیه‌در‌آمریکا؛بامدادشنبه۲۳ خرداد؛ پیش از بازی آمریکا-پاراگوئه؛ساعت ۳:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۴:۳۰: آغاز دیدار آمریکا و پاراگوئه؛ کیتی پری، فیوچر، آنیتا، لیسا، رما و تایلا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23196" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23194">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syBgvAVERUstqx7eS8_m2PMH8RJMl74ZJnB4hbTHKeAFZxVpYr2BEueKK_QK8TcJxbHMmILlCgXgZXI7IZhS3qHEAPyNoZ2y0VRrA5utw3-C8Nubjx4W-4kFE4J-KYuRzPIPKjCI4EBUTqGl8Zoahu7H_HtQ20k6VTFUjtLqik4C4i4QdGlQwPm_BW64OkB3ate-uqMSUl44kdtVjxjP59JXUF4zV7pi13am5MqWdbFct1QKON603gyUw-UZoTRVUvT4lqs4koc89qW7TKfYQWNKpTblFXULX2i0HiQxyENGLrDNUfelqrxkdzNej22LCJ_4t85bJErTOR0PjTDLKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23194" target="_blank">📅 19:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23193">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL5YjM2-292FghAq1973_R9cMJWniDTgY00TVESEQwI8NcOjEI6LWJR4x5NUQzfLLVkvuxi5ZsWMCQkhWIj_-Mkf6hRuIgmwjzuY85IKjdkaDDkMLNkcWISW79QIb-Cfp5vPTadims-cNacm5jOt_hNV8qk4bWLfagzrR9-oOge4PQktSiHp5_QFqijZ_QtauiWYvhmfibXYdcp1A96DlGpCNl6n7CwpmLcQtq50XS_ZBoROIjpGGbyrSKYX6i3UQ-4UvgZA7rSMsAIXy7h65k6s7OybgmUKsLcm9TZD90-F3EDk5fM6JKXF0t5GSV2SB14fisAdIQeHOprSPebUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23193" target="_blank">📅 18:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23192">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=uirP2PdGnDGYZnPB_7oiYCfRVKszDOSxpLwLnnS1PSZ_9-tAZFagnTubSPIpWK21uw6AmMXJIR28VUxZZ3eXzHZyIlHXQVVIetxLuVXj8yLuletCPcBk-EVj6P6Z-saSn0NZDiwvAzhwSMyPYgaGp0xnoncSSOb3jmjoEb1RrKbiBk0U-yWaDEOTMfXYNtL8mZrp1LsPS9Np9xl9cINQ1icgwyiR2697kY01xsjzFUfqWMi9ouZYbvwgBEtGkfPDwrBh2Oz4SnS_4jbGjwVxaWL1wKNfnT5n8KvGDLGBe9CFO-T48kJYWC2fG4H72PicABquW0cl5NDntP-LerTtFVYkGWV09cc5bCYIAD65v-4aoZKpuFy8WsHG4LDnUXn1MrYVxr3Omgbn0Bdh_FkTKyYPKPpgeHlRhBtpGTw_beRoPQACcXL9tbq4uQ1k3TRacbTQE8B0FcjE27cnWsHidxWeX2vfJ4tEc0kiPx2-zEzgTWVLnivMOh7lWOGazfobOkuSqw3VcIgJioFZkg0aMGjC_UK6z27jyLzyKdepYmSpTJoGdw_jnXIhb9Mb666VvIRErPXJppQlvMHlcrxzBMCgCB2-T-_Gw7TOvruo0yDCHxaXT5Tz4C6cLT0RBQvo_JfQBE_W2EHqG8CjPItZv_kGK7dxU2whYyfqutgLMoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=uirP2PdGnDGYZnPB_7oiYCfRVKszDOSxpLwLnnS1PSZ_9-tAZFagnTubSPIpWK21uw6AmMXJIR28VUxZZ3eXzHZyIlHXQVVIetxLuVXj8yLuletCPcBk-EVj6P6Z-saSn0NZDiwvAzhwSMyPYgaGp0xnoncSSOb3jmjoEb1RrKbiBk0U-yWaDEOTMfXYNtL8mZrp1LsPS9Np9xl9cINQ1icgwyiR2697kY01xsjzFUfqWMi9ouZYbvwgBEtGkfPDwrBh2Oz4SnS_4jbGjwVxaWL1wKNfnT5n8KvGDLGBe9CFO-T48kJYWC2fG4H72PicABquW0cl5NDntP-LerTtFVYkGWV09cc5bCYIAD65v-4aoZKpuFy8WsHG4LDnUXn1MrYVxr3Omgbn0Bdh_FkTKyYPKPpgeHlRhBtpGTw_beRoPQACcXL9tbq4uQ1k3TRacbTQE8B0FcjE27cnWsHidxWeX2vfJ4tEc0kiPx2-zEzgTWVLnivMOh7lWOGazfobOkuSqw3VcIgJioFZkg0aMGjC_UK6z27jyLzyKdepYmSpTJoGdw_jnXIhb9Mb666VvIRErPXJppQlvMHlcrxzBMCgCB2-T-_Gw7TOvruo0yDCHxaXT5Tz4C6cLT0RBQvo_JfQBE_W2EHqG8CjPItZv_kGK7dxU2whYyfqutgLMoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23192" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23191">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1dedLp0CPvTAf0tCAOi48Jj-x7sfLMI6Z93wHcvqh_8xYVNB5-K5d6gKatluaFn7Niwwdy-bbKqDG0nUFojbHkU41NZMtO5QPtWnCyl3jaIzRCxia-J6FKY7fnkRhJGGO0m-LSPaJkZ5CbT8zApR5Ri215VRN-ZIbvYrK1OaBjpjZI9pGgPGeHDKxrXYxWLn3AeZ0bGTsaadKzcK1q4TYTHVE5E_Ba3GkCWC73yXKomOKhTm6Gm78AQxJgi27OZnkV9r9UWkhzmYafgnqqaFUfNi4Rl1zc6sBTgUpy8XeBQuzBRqIUR4EBFeXuGerLfyPgpoz45aOHcdqtF9M08LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23191" target="_blank">📅 17:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23190">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsifE5wbiQ030tOz3BxOpb9XSkg5GGf8O9FcrxMq-UwumbBxJriuvkMu1il-YT6naMDk27iv-o-sZ_YOycPJ27LBVD8DFCg9sKBBGlmQnsNg4Gqw1uBC-QDhwkO2f1Fe6QBYGYlqFTXTObsLOW5MOdpIXyT3MemaKyiIKmzTjpXarf-_9hTBfld9cx6GetFEC0NTH22V0uicUMnXYJ77KPhQ-MQ7YP3a7oKmcvjWHNSjf-2wwI3w_gH_sF37yCDgyKXJE3xg24otyAeeYW56dNC9_g2N59u6QKyCHcETtDRhAbmyxRxHLCtMTJexksZyY7n_OvNf-UZQmKp26auEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23190" target="_blank">📅 17:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23189">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdEU1IlvSTK757NE_KQQR44gedaqtxScxe-uw3qaEkt6VwSqghCXrAsCjnKPLlnb84NZ-m7S8Nm-L1aV5-CgxpmEHVJ9oyN40LrixVGBVa9OWwg1zSivDmzCjB7ZyTETZPNUeq8GH-9H6kTKcWCuYllriSXi0mO5bVYtJ5Jqyah0eD8DkctQyPmovZFrrgC22w4bZMrKgRMreK8PMHtF_qBxcKZMhnA7gQyUVSIUWINhBy7DMDyXpjmnub9eYsRQ8sBOWv_0--n73yjDUE6w8U_JonTzOfXw22VqVngHSzbn9Y2hr7UDL2meKTN64fyRJKP21OwTmJJOMqg1_0ZEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیستی‌از اموال‌برخی از افراد معروف کشورمون که درماه‌های اخیر توسط قوه قضائیه مصادره شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23189" target="_blank">📅 17:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23188">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgE674_ero5Lv1CIS1WJHv7LfZ6KyS-vT205N2avINBocVPvlXoUSXMar7xp2ecaujp8GkEkbpyvqvCJbkHdOyAxGWUwyNaQIl3g-irktUMCDpa7vnapESnSxl070Cw2mZcNwkvv3fHj_Vuif7_o8lv-JaSaAyB_ydcthH8ojjFtEZdy5Ara0sRy00QGhlDG3oAZMy20NgJ-TxEozZI35xDCUMM3gea72Apv0p7G9kw5gRKSd2KXhIQP8d7JZpJvgQ00aHJcIsvEcFoUzBM4oPpxzg-b3jyplHryFWy4Bw3JoP7hZ_8yXzuUsfHrJufrW7smsFvMTeYyGbA_890SSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23188" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23187">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFklrJ1N3Uimt5WANVPZLN04ZRbcgjOiu0xeMYpIn7roPRycC25i_ke5cPSAeFDy6WJIXMAUNz9xrSmhQ3h_sta4TAzWha2wN6B6sVYH_pKnMUipxHxBhe1zmk9H2HvkF0F5C_KRS_O1GzBwrmC-S6Qh9wZ_PrbY5miYgAI1bcZEDB5beoHgNa9Nma--wJcLP-oESuseHDjAZ_Bw-GrKPzQG_YwZblELY68j_I-K-qdvt_MhkfMxrR_hSLeaBfhmjR6EyZxBGBDKhXlSUhUAUWIlpTWkJJH4jcpYbEbTPFO2wZXmb2IXGxfsGwfr0Ov9a7ZqIYA0UcKvrQVRnzKm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23187" target="_blank">📅 16:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23186">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b33c6zEIFcUbuIoDjCuGKIfycclFcuibJ5XoMYeL2V4D3KcSAFTLKVNcT13ti2lOHEiA3pjMofxQgPjS8Athh1KCT_RY9uF-HOxvQtqvWdn_CFWkbNllcy0J6mwDRvWXMy4O9ccqUmWQxU8fzzSMdssimO1O6_Zh1PvrSBssh-qJ3gzD7MFYIN4wCY05GkPAlroIKE7toIdqBvpII1J3Fo2ZvNYkiOP29x4STBjYZvyMvp1jEypCtGFRenfiNohzyFjYUp0MIbeqarrnnmi2D310f67cUzBDSj_cIfXbmkA8LlffVkLYUoXp7Hbl9_RiDMR7tcP5wsSZIkYte0BTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌مرحله‌گروهی رقابت‌های جام جهانی 2026 در یک نگاه؛ این پست رو که کامل و جامعه هست ذخیره کن و برای دوستات هم بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23186" target="_blank">📅 16:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23183">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIP3oWS5YgqYfrXmoVmEKh7cE_5EeEX4NOOFrBiRc0seSV2DTNVt4rnff-m3NR248pIMmWTOv7zh1rw9WDVnduKfmlKcXz7zf4CbnyOBUgsEGQC0mbJBwL0wkqoIvS5YUmGzF9w10UnwUtuLV8QGzXdAd0HUlxS-Isd-0EXM8QZQ5xVSdr8Hv4mevF-Nq3mNP8eiB9sN6sKN3Fbki4cJYeshy6N7A8SfYiDeAZD6DIWNScE8VMX5_N85o_bkQ7k_uAf9-y4_fLCmKkyRvnR22MHpabsRtPB4-VUsGK08WPCD8c06I-_IzUJY8RXtFUWiUwvPwOPkfw_H9i0SookhLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=SUUSm4HuHhsQr1wGYlX1C-QQGJpCiHELexocLCARobjXpwpAaP6DW7DuraGGbfG91qAO270ox67o3RKH-sKLeD7khHF_G3Xp-lCVISGnB5KbXGZXZuL6UeA98aq65M-FFI1fjFGWlwu9FjB3a5qFJbOUQUyOMHQ3QVow01z__t07zrdbBAAnaanLexg9cTzZeOThO8xn7QT5kDCFgyiau8Vy8R3iIz1RvFngIqXiPTby6LfEbLxuHg73J9cphn1G6Y2z1WzDt1VLliRX4M6m0kAqhI35qBdke39q-ISOr7ku6N7wPsEsr_v2oIl0-xqLvhG6PmaMIsf2qM5ZHjHHFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=SUUSm4HuHhsQr1wGYlX1C-QQGJpCiHELexocLCARobjXpwpAaP6DW7DuraGGbfG91qAO270ox67o3RKH-sKLeD7khHF_G3Xp-lCVISGnB5KbXGZXZuL6UeA98aq65M-FFI1fjFGWlwu9FjB3a5qFJbOUQUyOMHQ3QVow01z__t07zrdbBAAnaanLexg9cTzZeOThO8xn7QT5kDCFgyiau8Vy8R3iIz1RvFngIqXiPTby6LfEbLxuHg73J9cphn1G6Y2z1WzDt1VLliRX4M6m0kAqhI35qBdke39q-ISOr7ku6N7wPsEsr_v2oIl0-xqLvhG6PmaMIsf2qM5ZHjHHFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23183" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23182">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nON83XDWSFd-EpyUEc-6h67EFA-Fn6QRZMZk-m-wXu6Tr1CjzQzhuGlxSSX0hgd4V72RHOiantUxVd51-ONzBLDPudNzJSnFlvVhXKlw2F1-PH0ijPMDr-KWGqulr_B8tMd9TuRRGNqTKeYqgb8OC5PSzFKufgN00fBEnQEErz_k4uayUUz0DfiHpXyT20mcZRdyZtwPFpcR6d1ln3_Xr3GxfeeSE9MhJS32bRvg145PPiGHCPmy1S5hYB2FDAsvbJtagXyvC2GjE17-bKoLwexoHYnF67z58rCONrR9JyKnhYXLhsXZI4qyzcbAsHVHbv7DYcUzfkpXsZY2w_L8HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه بندی تیم‌های ملی حاضر در رقابت‌های جام جهانی 2026؛ یاران لیونل مسی در رتبه اول جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23182" target="_blank">📅 15:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23181">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAgS4F1gnafmwKSfogF1rW1t7_JVMwIkpMgfHOR8FmEFQpXWwdA-cKBXXZKE3buWfI5S0ZIIEW5QFhouL1QwGLXBKpcMKSgsZknzNanDBvEELehCNixM1eI18NPqtpk1lYCF1aycaS7T8Rnf7493uN42GiofiW_n66p9V38Z_LNTaHfQnA6DdtkOzK2S-CrWT_3WMIYDVdsvzLSd0bq2oE8uQhR_X9Ik195eYUWP4Cw_XxYnuWpo-1rx1dhjaXOXcS-rNBFdKc9wevmS2Z6eBDSIJfFGxqy7kdQ2fyk_CokqCV4vRM6EFqNIQGlsou2EF1rAkokiEKarKNBLtIPxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23181" target="_blank">📅 15:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23180">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=JXPMq_36Z8PGBTmFTDk1QhO3Pi37MhIn1hvNo30bEgdujM-tS4kb1FiUp02zKDZ9suf0oQJaFN6uhPQUhJSeZ2qCwGyGZwgaQ7dXyD0x04PtYyTNHB9_FlDy7TdWoVu87jGoNB4uw87kyYRJ-qRC49DFiZgkiC7GLhuDWf9igc4RQNV_PjvWkw-2a3zfklpC8tW7zo-IwBYJvIiJx6ajLkDn1vw_Bw3VfTmKVE0eJyk4JOzGpByBe8TbwbmaZjEz8-JqnPX8McGrnWV3XEQ1SHQ44KWt0tgwpbn1CfpuoI5cxJIsjhh1ta9OUTvkkq984SBnn0CCAOlYxe9bdiQ9rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=JXPMq_36Z8PGBTmFTDk1QhO3Pi37MhIn1hvNo30bEgdujM-tS4kb1FiUp02zKDZ9suf0oQJaFN6uhPQUhJSeZ2qCwGyGZwgaQ7dXyD0x04PtYyTNHB9_FlDy7TdWoVu87jGoNB4uw87kyYRJ-qRC49DFiZgkiC7GLhuDWf9igc4RQNV_PjvWkw-2a3zfklpC8tW7zo-IwBYJvIiJx6ajLkDn1vw_Bw3VfTmKVE0eJyk4JOzGpByBe8TbwbmaZjEz8-JqnPX8McGrnWV3XEQ1SHQ44KWt0tgwpbn1CfpuoI5cxJIsjhh1ta9OUTvkkq984SBnn0CCAOlYxe9bdiQ9rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
جوادخیابانی:
سردارجان تو الان تیم ملی نیستی ولی هستی، بعضیا وقتی نیستن نیستن؛ بعضیا وقتی هستن نیستن؛ بعضیا وقتی نیستن هستند.
👤
سردارآزمون:
آقاجواد حقیقتش اصالتا ترکمنمی هستم فهمیدن اینجور مسائل یه مقدار برام سخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23180" target="_blank">📅 15:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23179">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=ZC7pbytxzU2IvByVx_k0XfkrpywD1jLLdk3GduFx-Mp4WMed5ub1FfHjEwSAvhmnSGRPbAcBveTNIxEkJKpRcRmlrh6zajscJwGJGfWsCsoKVO_z92rld-uXrUP56JSiQAOkiTOqx_UdObdCSn2L04z2YPtd8G9_RRaOiZnpx2Qn3rdMwv6nmKbUxAXsHyXkWXPnqEQP_kBERTdLmXj8qd7Xiw_AgorOJOyCbwY36TxQ91vaTL4-EC6Hob7A5R3Y0saWCAftTAJTIO33pV3wz_ILbHXEzZmzK7Uw8pzKNn2IbqaEdXcYq-zL_puFU5GS69VEx-amGcZ-m73jM2W9pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=ZC7pbytxzU2IvByVx_k0XfkrpywD1jLLdk3GduFx-Mp4WMed5ub1FfHjEwSAvhmnSGRPbAcBveTNIxEkJKpRcRmlrh6zajscJwGJGfWsCsoKVO_z92rld-uXrUP56JSiQAOkiTOqx_UdObdCSn2L04z2YPtd8G9_RRaOiZnpx2Qn3rdMwv6nmKbUxAXsHyXkWXPnqEQP_kBERTdLmXj8qd7Xiw_AgorOJOyCbwY36TxQ91vaTL4-EC6Hob7A5R3Y0saWCAftTAJTIO33pV3wz_ILbHXEzZmzK7Uw8pzKNn2IbqaEdXcYq-zL_puFU5GS69VEx-amGcZ-m73jM2W9pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#تقویم
؛
خیلی‌جالب‌شد؛
دقیقا 16 سال پیش در چنین روزی؛ آفریقای‌جنوبی‌میزبان جام جهانی 2010 دربازی افتتاحیه به مصاف مکزیک رفت که با این گل دیدنی اون‌بازی رو برد.حالا بعداز 16 سال امشب این دوتیم دوباره افتتاحیه جام جهانی رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23179" target="_blank">📅 14:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23178">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tssll9DCLnNT2Z_ZMIEb5BPoEv2wuURbhFTnVYQ_T5k5WHW3e0hVHvd8jBtUJz9UQAepYEjr6QqUBLUO3cAco_zBd2DCU8FjWEKmJmgr1x9jOXzfQTvtDclDj9I7TbjH3fOZfTnwEXbr7-U76n5bKZ7pQISZrDS26ZsA9VyJC_zWuJN5pEZ_RVAy5e3bUIduZ8ONxdsqkqS7uNtAZOdBRMoP_oSihPEI8zMK1rQr0zDa5grLobpJIg7K5OYBq2nm6kTETngFBTJZnrKMKotD8gWAiSGmOoAPDD_VJlp1ACZrEBD1CfomYi1uJY7hFvQgN9uLHHmLHqtSkYDjVHELYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23178" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23177">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzpwZpzk8iFdexSvZb05HYb3oaA601fG98B315vL-w5hrKOi-tqTEPoUJiYa1XIr3jKqFdibrMkK4Vm1lbVkVQIOmkL5sBYBKRm3T1GN7r5OfI2SPAAtTh8uvoVaOOuDnul_lufOGTrPks1Q0d3W4Zcq5Fb_cROwzRlm3ZmdTVBAlfLO0qIbLnX7732OWJVOalVYuHDjinxILNQDm9Z7U36a4MyF6XgJDp9MsrP9FLxQsHntPB92GH0vJW1v8vg-WVnJx3_VXVmGVqxOL9J-X0y5D_vD0lXoq0D-MFUIb_4KMOUGMjh1UJKZcgtbDEvsH9k5TsL-Xxh1ihHEd40c0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا از باشگاه استقلال؛ علی تاجرنیا برای تمدید قرارداد محمدحسین اسلامی بمدت 3فصل‌دیگر با ایجنت او به توافق کامل رسیده و این بازیکن 25 ساله به زودی با حضور در باشگاه استقلال قراردادش رو رسما تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23177" target="_blank">📅 14:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23176">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=qn8oYY6DypTCSOKEFkp1u_Zrx8EsQ604bQo88qJpuF9qIbgiizlOr9dJPbQeJ3Nyql1QHJiIVbTqNHpVs2FDnuYjUJNNBdf5l7_-AO-itAMTFXev9o0s12vBqjRXLXAiOc21XfV1GKgODo6oWE163aNMkWSUh8EBDNoXDSh5D8j2SeuB5j2Y1z8zWtXJCHcSTIuQZg1-WNk1TYxbgoHWodV9WLBG1psAJiE71kn9TvI5QTQrgJl8L3gYSri1yqy63E2gTiNYQ-9wxp4bN88SOIqrsvXHlqzwLu54rdgPUxBGQUdz5R_YGmvoLkPgM56LJPDKLLMtSNdvypuVg6SPDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=qn8oYY6DypTCSOKEFkp1u_Zrx8EsQ604bQo88qJpuF9qIbgiizlOr9dJPbQeJ3Nyql1QHJiIVbTqNHpVs2FDnuYjUJNNBdf5l7_-AO-itAMTFXev9o0s12vBqjRXLXAiOc21XfV1GKgODo6oWE163aNMkWSUh8EBDNoXDSh5D8j2SeuB5j2Y1z8zWtXJCHcSTIuQZg1-WNk1TYxbgoHWodV9WLBG1psAJiE71kn9TvI5QTQrgJl8L3gYSri1yqy63E2gTiNYQ-9wxp4bN88SOIqrsvXHlqzwLu54rdgPUxBGQUdz5R_YGmvoLkPgM56LJPDKLLMtSNdvypuVg6SPDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 تااز بهترین‌پاس‌‌گل‌های دیدنی در تاریخ رقابت های باشگاهی؛ کدومشون رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23176" target="_blank">📅 13:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23175">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sd2d7xnbfqc8SFI1nf2tZnRJ83MPynxR2kmOAbxCFhr8Brtdv70wtgPjGF7ToPAQt037_UHI66UEIY08_NFsvfWw1OeFH-cYpsPihonA-s6qtGB0IQURs7pEpxTobBLmE9bmNl2lsUneSMnSsSNW08VjeEW34cCH9DmUvRK4WayOMPrKCaXL5vPC7JHlUXQFomfJgkJCck02zXTrdmyzhvgz1zdPTNTopD36x_vifQiD8qAVPln2TWLFFBheodN0pU9eBlURiidacW-ITh5OqAvUJ4HeBvZ9yFl5JDbH5T5d3gdiDnEhXp2_KdmB3uT5s7mWxTmjLUsrJZPyLPYXOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
🔴
#اختصاصی_پرشیانا #فوری؛برای اولین بار اعلام میکنیم که اگه شرایط کشور برای فصل بعد مساعد شود نظمی گریپشی فوق‌ستاره‌البانبایی روبین کازان به لیگ‌برتر خواهد امد. هر سه باشگاه استقلال، پرسپولیس و تراکتور بدنبال‌جذب این بازیکن هستند. باایجنت ایرانی نزدیک به…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23175" target="_blank">📅 12:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23174">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRinMpSYodLZumMqexmKbKBJeR_obwzjbnwo2rLDRyhQyhOK_WJcaPdP6wGXSl-fa7Kl1evZ2WPKZjudRlaRZ7qWfP2_QieKY4JXdnUnm9wLWAH96PGdOkuE4x2yvSP9VrXIQ0jYNlD4TD9inBuXhX3toutzVM5MXbqBGoAsMaDjMKNjMmBgSWA1IKhFEgEJcadaxS6XBqE46ztlH74qarQyC1kCeO1seu75Ye_Nc85J9Jt-9Uq8cMc7-ZLiR5ftCJA8hwU1PMuaXnGo-sXQ0HuGF1F2nblOWsy0CSh6Kp0H3-AfSSEY_4jrhOAtKV4j0nRYomP1w4tgXV66zR3IGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23174" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23173">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rylLHMZgBgrqIGp7UIM-JwukOwyHrtPm4Lr4-0DGMF9g4O9YxDzGRtk6Gwf1Jo-5c3edhIaSUuuxUwqyBKEgjzbkMekcb66aclgAzKr57MNBDzAc6Z6R6f0c8EInN9myk55pOmVzxgcwH8gAjrQC9cIIB0fkLiGPg5VtX6aGr9ZG2_GVMeodJdoTH0uxlPj_W1PNDd7jqk-PfV4hlyzPto9TyqK78jXh_FxMwGbdwiHP4VbNN_1j_NoQ1I3NyPVuAAAR78r7OWUZPVG21WDcboXLvvernfdiAo-ChhLqN6zHdURGCVyGZigHw8gwpEXY6sgPjIJSxYloy15Wd1F2gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده شش ستاره فوتبال اروپا در فصلی که گذشت؛ جای ستاره‌گرجی در WC خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23173" target="_blank">📅 12:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23172">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=saJ_0xzGCgTJjqDk3-ZNA5--VLS82nvA_9Z7FJYNMxOkztjIWCtmuYIL4p7ncAi1s4mnHfOWRntp0zGQnBdALyEpWAksvsP16f3lM28V9OWUvqhQXYy7xY-zkLfAWTkWpjJ2sU4WCpiatkQ9526do84tcQHginJiufQRyz_fJGzOxGiJLoEseJxPvvX8pX8yjo0IS1T_-ZnfFWds0bYB5BwMK2srNo45Fslhp10wo1_kXYCA8P_3XP_C_ZeREZzTa718jEBc5Zh2sBernc90GNeyaaWFugoV8XRP95PxE2qi75n-tk_xsMvqsgtOSO9FLH8n0CQBr3g7on0Gc7gcLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=saJ_0xzGCgTJjqDk3-ZNA5--VLS82nvA_9Z7FJYNMxOkztjIWCtmuYIL4p7ncAi1s4mnHfOWRntp0zGQnBdALyEpWAksvsP16f3lM28V9OWUvqhQXYy7xY-zkLfAWTkWpjJ2sU4WCpiatkQ9526do84tcQHginJiufQRyz_fJGzOxGiJLoEseJxPvvX8pX8yjo0IS1T_-ZnfFWds0bYB5BwMK2srNo45Fslhp10wo1_kXYCA8P_3XP_C_ZeREZzTa718jEBc5Zh2sBernc90GNeyaaWFugoV8XRP95PxE2qi75n-tk_xsMvqsgtOSO9FLH8n0CQBr3g7on0Gc7gcLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ نوستالژی‌وخاطره‌انگیز از اوج هماهنگی فوق العاده لیونل مسی و اندرس اینیستا در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23172" target="_blank">📅 11:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23171">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZERWv-LsoOM1ZdzQeFVPJtZwD6lh6wsSUSDTaP5DWAg5BXipbLGbqZzapLGlj76-6l_Zq7uXYqvIDcnBZM3IqhWADogAbCBP9Hc81T-lrZs2XSye-zsQelWAjC5gp0dYNAMzs1Eicroepd09qnDdRVEOZL0Rs57mAdnloYdqv5Xfvr7iYrisDjThQsAEDRIVHOlZYoG4uq3ewMBnBICSr5tTnkWNHp6QMVqxcSd7fSJlb_fDTa0grtCBivU_u_hgaDa7CvEDUjv-z24Qz2eej0ggTA9MGEPS3Adryw7Eev8tnolgqYHOog5_Piw1FE_0EHKMAx-yG2G36ld6LeAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23171" target="_blank">📅 11:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23169">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4D34HGFgu5S8DSoiKQmAKecOY1rhmsPZGg8t9LnovvH4iWY5Qfd8WZTkvxt_bIcOSqHKAFVpG8vh_O3y1oJvHwh0ybWOwY1OB4dIV5BakxDeQkxAZTliD-AhhJ0e48F3oZTxetkaoRj2CLja9R7Ovjm7Q0q9ddMFlaM5Es6qsQHY2hICRruKDYlp5PS9NRkr7TBlJAoVmDGfMoJHx_KjnJdccOQL8d4SE4bcVXUvtH68lbfCjzwEvIwpwECR-4-eo_RcJX8IHWiL3UUyjrS716YI3-2p5wse3SByngsZC2lfptnCvN2e-lVvnqTL-tTm3bEgBGoADw_eT3ElhauuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJeekVB-FKSluqzv6DOQho8m1y2yZMA4W8BYm-9kjxOEjdvOdNEctdA--25Lk_2wcXqf8gv7w_F7j6S6xTYu0LZCZ8zbqhg0OoSDSqonz49scKP8jTgGHPIFFYXxphRfmW4ctCyWDjJmmVAYwJAt7SVB6CsrLi7swt0fr1jSSmXkm6_zNsxO89jmSceYGHD6poa_C7VhXgYK7KryolW2rLfryVkq02EZ4Ugv7qSkjfRthntq1zCPOZqulqCj8f6WVRcs_r9eRaEHvEYDlukL398T6HiOTIa8KnnKsvpyLyEYPD8QfvxBMkfkeUzooc6dO5tHvxN9upW-d5Hmw1EBcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک تموم بازی‌هارو سعی میکنیم پیدا کنیم بزاریم. اپ آپارات اسپرت هم که چندروزپیش تو کانال گذاشتیم دانلود کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23169" target="_blank">📅 11:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23168">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnRlEYdkUS_Thox_wJCfbl3mYKmdHXAbBX8ZbZLIpwOpY3ht14reddnyzW5b05EKdLTdPPqSocc8XG_oH5vgaLsROifO1XBEZh4YemaW1FltLGH_jSju8itcNEmdG2zTG77GE6xHQK_CrU1csuPMvkAe-HJ0klqzDsQPNWiJqXGnyNMZ9ErGQhOmcNlec-sqfNma7BOHNxnhx7iTHjVa9XsL1uBeWQOH2BKLmsWGhBLq-NYb7v8ga9mpFJJ_lfwxWcRnPut_pplpxK0FfTskrmrtRtZECXfNJNta-PWEpR9G5z89_mpHoziTh0H_COVYwj3H3OTsMDrUNsiYimP9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛شهریار مغانلو مهاجم‌ملی‌پوش‌باشگاه اتحاد کلبا نیز از دو باشگاه تراکتور تبریز و پرسپولیس آفر هایی دریافت‌کرده و درپایان رقابت های جام جهانی پاسخ نهایی خود را به پیشنهادات خود خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23168" target="_blank">📅 10:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23167">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=EWMfBQpd4bjWE4SsRQWmLXUQThw8rmQmKs___sfFDy_BLo2L07FltMZfdYOFoRTVe7rZbscIUx8Gt1qRE5D2KKz8x8yQ472tvxOaQHDGhNaHl-CRQ9w9o_TCSO65WwdPN3BXicrOxEeoLL797GsbubKOkdAqoGYF_v0GY7fPD2vRjsIek6gP_ux5mkNXTIrwyH5ScXbgFDGhi_K6WYP3crjlIbFDYsszfK5tUBr3Ibktwpz8aZpANR09NV4cbJXy9miNeeIOTaSr1og07IAo90gGIVg3iDjh8XqmcWbnufxBMMcPJ6bwhJ29OVu_lOvmlBnn-MT_W1ilLqbqxI8j8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=EWMfBQpd4bjWE4SsRQWmLXUQThw8rmQmKs___sfFDy_BLo2L07FltMZfdYOFoRTVe7rZbscIUx8Gt1qRE5D2KKz8x8yQ472tvxOaQHDGhNaHl-CRQ9w9o_TCSO65WwdPN3BXicrOxEeoLL797GsbubKOkdAqoGYF_v0GY7fPD2vRjsIek6gP_ux5mkNXTIrwyH5ScXbgFDGhi_K6WYP3crjlIbFDYsszfK5tUBr3Ibktwpz8aZpANR09NV4cbJXy9miNeeIOTaSr1og07IAo90gGIVg3iDjh8XqmcWbnufxBMMcPJ6bwhJ29OVu_lOvmlBnn-MT_W1ilLqbqxI8j8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23167" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23166">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tirWAVRrZaw5-ZovqHYgiYSe5UES_8FUE826CUjCckz0E220S0dAG-tmJestbPzamTKrnUtmXg7e-eRa-8So8U4s_FimLU3hdq2ZFLzSna0baqNJ6PNIAGnmCxQIzuM8m0hbLLW6zQYLDjY8eXokVozUMr2nfuv_ZORUjlUWy1pzS50PWrqJJ_z0iFxUgEK3DFGPF-G6DiViIzT7qUwQGwaI7BY54nMMTefaSUF5xxNqj2dVgOft9coZhDUe6ZqetJbKmldVipzl2o-CjAu4URc-wVsF9VW-xQM-HaZ-pwcRlPnkaxa2K7OgqkDTObGoES1Ue7WuC8oG8t97cvA07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23166" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23164">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKEUGnlmg8hya7OrHuAR86rBhTY7hsZlmrwLMFEJRcTJw-dBVelpRxLaD3WE6xSCpZFHCFhpji-LUjoe2Z8HJk8WRggfbm1toktm_4SuFnVmjhuqrDo7lfExaU2pDtQT-BCa6y7EyZGDYTkON04JQukv_0x70JpShLa2PjnPudqeFKX0CcfA1onqf3zxrZaJCF6LpA5EgNdRALuyLME80veeVXhCA7liC8cKK-sKKhQjp2oyykgDPHTuCFWGU3jqq6Jj7H7VtzclhuGo4W8cHbCZLpXP8026EfHPlRoCpgffXE8YcK-5ibt-Pd4t5OmIMp6ygwpPCwQ0iCAzISr3Nrfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKEUGnlmg8hya7OrHuAR86rBhTY7hsZlmrwLMFEJRcTJw-dBVelpRxLaD3WE6xSCpZFHCFhpji-LUjoe2Z8HJk8WRggfbm1toktm_4SuFnVmjhuqrDo7lfExaU2pDtQT-BCa6y7EyZGDYTkON04JQukv_0x70JpShLa2PjnPudqeFKX0CcfA1onqf3zxrZaJCF6LpA5EgNdRALuyLME80veeVXhCA7liC8cKK-sKKhQjp2oyykgDPHTuCFWGU3jqq6Jj7H7VtzclhuGo4W8cHbCZLpXP8026EfHPlRoCpgffXE8YcK-5ibt-Pd4t5OmIMp6ygwpPCwQ0iCAzISr3Nrfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجموعه‌ای از بهترین آهنگ‌های ادوار جام‌ جهانی از سال 1998 تا 2022؛ کدومشو دوست داشتید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23164" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23163">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1y93jSHNrIhdLovGS0ppaeG58KRFA_teW3tUlyQktcxVcnf6rBt5FFhBQtcU7KD9j4U-ge2MOc48G7cGp-UESU51yI1bS96D4lU6KySdRL0WssQPJ60oZ_SHwBHEKcrvAgVQYCDcQRNH-RaOippgMkX5kQdGGaK-IiJHhuIWiboa3gBG7jUb48bb9K7H7EbQn_mGEOVEW92eyoFHGrG03yWALEkkvzj209qanTiAQloEe9zvCYV0wVhpn-uhenINhp2pOZVgameryF_bcd1x1zLHMgdVhWUTeVMJ3AxCTSTRLUuMs_0mMXChIIrwSfaEkn2XoyZCMd6idaj61M2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23163" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23162">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK1jme-inhN8A1rmaRoihYgZm8uS_bPjBg-hL829K1kBrRxKQqPJVzb83a8te0cd0sYVaqtTK6RH_HDhUO_Ff6f2Sr51MyxraJQOndT-m5RMC5hsEqf68_E4RvwG34K3BmkXk-IULTHZpsobotTLZr7BjXfGmY5bJcNfldwqPV3NoxEFJOw72bKB1io3ugp9SEteBZYavyclSgfJwEQbeyz4BmI6O9ZEmX0DCPKMlcQ-voEdp7FAezZLdtQnLKQF7MxXUDyrU2vuEo4NMrj5jzqtDhuYcXrTWh9YWir2tvFFj5bNIc4FT-YJrHKslm2qA6Q6ShG6hPiwcXieQNikkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23162" target="_blank">📅 09:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23161">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=lYppkOf8LIbLZoK5M3MJJK-S3QJd4tBRgApaSk_v9tL8k1J7HcEqxO3xnLcSpHzqPb18o6rBZ4d6Gc7doV3l9hj5EQkiMv7ZAbsnQhUwPCJjsjXc12ddrDjZhqTeh-Kv0RVnX4-QOvWSKcYKpGogM6r22iKXRy1-Gws2Gt3nfGL0hNjFJwrpYiYokJusF1yH_tpf-xPbNayI1MgH-oQvTy9R5AcjPA7lL7J4SfZGXrYFck2EIA_sp1MgFonNzg8i6EPKL-_EFS6l-ZHZfPyMuD1Zv47HeRrYMkd9mhLi8piHzTNPa4g9KJnywJoZcHIt_JkYPHAPrEPzgDrcy9FWUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=lYppkOf8LIbLZoK5M3MJJK-S3QJd4tBRgApaSk_v9tL8k1J7HcEqxO3xnLcSpHzqPb18o6rBZ4d6Gc7doV3l9hj5EQkiMv7ZAbsnQhUwPCJjsjXc12ddrDjZhqTeh-Kv0RVnX4-QOvWSKcYKpGogM6r22iKXRy1-Gws2Gt3nfGL0hNjFJwrpYiYokJusF1yH_tpf-xPbNayI1MgH-oQvTy9R5AcjPA7lL7J4SfZGXrYFck2EIA_sp1MgFonNzg8i6EPKL-_EFS6l-ZHZfPyMuD1Zv47HeRrYMkd9mhLi8piHzTNPa4g9KJnywJoZcHIt_JkYPHAPrEPzgDrcy9FWUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇺🇾
جالبه بدونید
؛ مینا بونینو، مجری سرشناس آرژانتینی، تنهااز‌طریق‌چت‌اینستاگرام با فده والورده ستاره رئال مادرید در ارتباط بود و قصد صمیمی‌ تر شدن نداشت؛ اما شنیدن یک پیام صوتی از فده همه‌ چیز را تغییر داد و او در جا عاشق لحن والورده شد.
‼️
درادامه مینا دراقدامی‌جنون‌آمیز و ریسکی شغل موفقش درتلویزیون را رهاکرد و بایک بلیط یک‌طرفه راهی مادریدشد تابرای‌اولین بار او را از نزدیک ببیند؛ تصمیمی بزرگ که‌سرآغاز یکی از وفادارترین و پایدار ترین زوج‌های حال حاضر دنیای فوتبال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23161" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
