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
<img src="https://cdn4.telesco.pe/file/O4yXg3uUySvxP0Mg4CCsMoQgBR1_meuFPrzg50ntr43055xuUILcM-Wgtz5lFgDbJpjoBD3qlvIbHFkaM7GDawEGodiFnY7eYSW-nDuoBPzNwvYakulSZEgGHzTWRSHZf12gqP9HT3KaGWFSHeD1ATnx5Wp5G7EKw4X7lrQPmXztgKBIQdZpEH6i-69jynifp8qHEq3y8JrtDoU64_hSnDT923GidIxU427yFePV91x78zII6PnpSMEY7xUihmngaHez6Vkjbg0AkBSuNn4t_uzqIcFfyWjD4A8kN3mDsw9ca_Vr7tiiU_jOPryuUAy3ZwABzz1sA6ctA_IFJqlkYg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 126K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 11:07:02</div>
<hr>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=Bk7B8vUKe8Q3I09Mb5gBrCIrwQPREZZuJJbBdRjTKYDrg_-_fAKLnCE7_5kar_8thc5836K2jnzopSShyaGsoPuBZklcgS-UPqD2512EmRATj0bXK1H5jG9p1_lkQ3svc-COho-wIrpcg5gmXbc3gfNn3MMKLCFOdNUfR6__EFJQztTbtiZWaY6HldWx1sOkoLGfxl7MIlwSE48SuBgKOXPVTPhaR9unyylvrUi7w-cj1TJys8YHp7Fpj-0CYvGtHooNZ1166HFwcTm63ChGXAgCxY-zlQJoQQUYu-xnxJyerFntYnTD3aIUk4MAZvu26CeTSQRDLefb7XDR3FXN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=Bk7B8vUKe8Q3I09Mb5gBrCIrwQPREZZuJJbBdRjTKYDrg_-_fAKLnCE7_5kar_8thc5836K2jnzopSShyaGsoPuBZklcgS-UPqD2512EmRATj0bXK1H5jG9p1_lkQ3svc-COho-wIrpcg5gmXbc3gfNn3MMKLCFOdNUfR6__EFJQztTbtiZWaY6HldWx1sOkoLGfxl7MIlwSE48SuBgKOXPVTPhaR9unyylvrUi7w-cj1TJys8YHp7Fpj-0CYvGtHooNZ1166HFwcTm63ChGXAgCxY-zlQJoQQUYu-xnxJyerFntYnTD3aIUk4MAZvu26CeTSQRDLefb7XDR3FXN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنت بین الملل چه زمانی وصل می‌شود؟
🔘
سخنگوی دولت: امیدواریم با ابلاغ رئیس جمهور ظرف روزهای آتی اینترنت بین الملل بازگشایی شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 92 · <a href="https://t.me/Futball180TV/90226" target="_blank">📅 11:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UncP7O5Oi1Z0MEbXTPUOtEOyV58pgfotvQPcrjv-6f8tfm1RBoRRl_ufPGKtKWQp8EMdCKOaYb0XYI8hlhfsB4e9NyBOVvLoatxMnDnvRb_bkDygFUMnZU66dI9M_4k0g-ZPLV6HB9Lb7Wc1_kxHhIkrh_oAXLmmpSY3hr9AvBJutUmAA1aSmS1RdM6A504mtnDIsTsY-vLYmEdn1Kq9sDWjjwKkudBeH34hDH-dwzTSKlnujRbDgl8pFw2rUiIPQqDCuw7WzXkkUu8VG_1fuAb3hh-2uNLmNOnq-tjibkKsp9YuS6b7ShKfjvdGiyz5DCjZfLmoa7IB9HlOEnzMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C قرار داشتند. برزیل مهمترین تیم گروه C در جام‌جهانی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 216 · <a href="https://t.me/Futball180TV/90225" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dt4bEe5TI7h2DkyizJaPUaiLjfT0MWx26QkotumHjZt4Ihb5f4FYw2hwVFbnWmNhZxk9Y5jZ_GhBVCTUrvqRMEURkBAzSIb_drlbUWXW_lzbk8FGi11zsRCYagGtPwH5HmyVevVLOPgdafeHDFy3vNvL-DVZLL3-SjCladgfUrlA4w1J3A20GpK60FrggF0-5DH3gmF7VESnERx2_UThk_coYreHGxv2ztzuC4M6Ny419OnIOrldsJVTQwbOHX0PVC-PgnRkCH20Gku6mkAl7RFQ-EszUb4O5F1FtBy7OM-dCUSr9dNRZ0eAliQL6LeHeUuM1LFU860Sfdmh57bE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با آغاز اتصال احتمالی اینترنت بین‌الملل؛
ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/Futball180TV/90224" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=Ur-HgUaksCTe7AUQQzQCnBcSvDI1ckprNSb5qpErE_oUj7JFJBZq_2Ud_5k-ddnr-jMhyFLqLotrCS7a4VrDCBVAoATnAubfKmv0HswHOBlb2u3RuvozOErMdB-iciG3UWbA1Db-ZhxYc9bBcZXsOYlR5rqZrPv2AMTA8iUYC--OF3oRSqYJyc46UHA3E0ftwkt4A6jmgBkSUnniqeCKizVyM-FN4ojknpcqWGblh0kCaK9JhjhWTNVL0B3rCV9GJ-Fyn9LUI5P-cMHReTXbDch8mUnj5c9RPzY7gg05FR-4a6SgVgL5da9WVeO2tInDMJpd0LI1RP6LjlUzOYZJ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=Ur-HgUaksCTe7AUQQzQCnBcSvDI1ckprNSb5qpErE_oUj7JFJBZq_2Ud_5k-ddnr-jMhyFLqLotrCS7a4VrDCBVAoATnAubfKmv0HswHOBlb2u3RuvozOErMdB-iciG3UWbA1Db-ZhxYc9bBcZXsOYlR5rqZrPv2AMTA8iUYC--OF3oRSqYJyc46UHA3E0ftwkt4A6jmgBkSUnniqeCKizVyM-FN4ojknpcqWGblh0kCaK9JhjhWTNVL0B3rCV9GJ-Fyn9LUI5P-cMHReTXbDch8mUnj5c9RPzY7gg05FR-4a6SgVgL5da9WVeO2tInDMJpd0LI1RP6LjlUzOYZJ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران ترکیه در آستانه جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/Futball180TV/90223" target="_blank">📅 10:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90222">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=jjQPaoQlw57IVT4nSqE4NLxD7s9ku3CjMMyb5UgydGC0OeDIO5J2KDMso2Syc2E3mGL3LDztfqCQ7m2NP6rizs4LHUeE3UgNPsLL4F8NDQjlEFxfZLiU-LhTHg5i7LAOBvy292FkZryjp-4TaxFx_daTpglCITFV0WuOUKj0_6EqdpbN2RMol0AFbxOFdY8ZwRmzrvQJ-Yp5kNNdfN2lZF36M6oUhz_-YAlFiYpGaqGGocmcrpRQHAAl2JCs-htlhRdyDWxN_N2xpOTiL2cWQrzlwm0RQEB9atLABU9aBnPy8DVkgRMH1U6uSjMpZP6GztsrBNWSQwdSRjRVr0Qkdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=jjQPaoQlw57IVT4nSqE4NLxD7s9ku3CjMMyb5UgydGC0OeDIO5J2KDMso2Syc2E3mGL3LDztfqCQ7m2NP6rizs4LHUeE3UgNPsLL4F8NDQjlEFxfZLiU-LhTHg5i7LAOBvy292FkZryjp-4TaxFx_daTpglCITFV0WuOUKj0_6EqdpbN2RMol0AFbxOFdY8ZwRmzrvQJ-Yp5kNNdfN2lZF36M6oUhz_-YAlFiYpGaqGGocmcrpRQHAAl2JCs-htlhRdyDWxN_N2xpOTiL2cWQrzlwm0RQEB9atLABU9aBnPy8DVkgRMH1U6uSjMpZP6GztsrBNWSQwdSRjRVr0Qkdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سیاوش اکبرپور: جرمی دوکو رو می‌شه مهار کرد!
😁
محسن مسلمان: ولی نمی‌شه؛ فکر نکنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/Futball180TV/90222" target="_blank">📅 08:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90221">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/Futball180TV/90221" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idxc_ejw8dwFLmFVPOkxKZRLxfgpNtAKbtPsLHRmlzOU5ImokpEPGcgohxcGVzbxlppZuumRJCWat8qlmI9foIruMxsqBg4bBL95veiNsl-UnBlAlEPqzZgZz_532IcXbbpEb4nVNyVH__pb-9z5lV4Cmab6Ve01BTNUKjpiz5WCxhF-z2bU1Y7LjvoaRs2R-CH7MT-8vg6-_V7Grxx0OQVbulERaMgEEZYhwd9hvYrcJ6wwCRv3Ui9KUlcJl_NOp-emvF5yVIJJquCymHQy6xRwv5xhyR2X6D3a5X6VI6CQLz98T73qrtRbf_W-d6vk8sOEzKXOrx1gnNXAQNRXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/Futball180TV/90220" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL_nUgdpOmViHaBQnEtibc_toeL2jvnS4fXiMk_qhHdKvjz3W9yD4FCD3vNoOYSYqlXKMVJwFSnWTQq-L0ST-YmPr9kl_nLPHMi1fjKMjDdfsiwXgnQMxfOev2sFU8d6HUfbiCwjqaLvnxtCnImEQ-XL4R3tbWuN7gTDy1aBhQnKayYC26SF-cDIpUX4BiPDo4R3a-zkatdWbjjtySUPWKlYjPJxB7e2tU-L95we1mpUPKdgzC0t0J8bp-I8ls9Mgzxtm2NxE2th0V1gfiUB4K7r1XRDU6wFUpqVshoppz-3To2FwC84zU6nFTDlqGzN87q5uEBY-pmh3d42dw5Xhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
لیست تیم ملی کلمبیا برای
#جام_جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/Futball180TV/90219" target="_blank">📅 23:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6XxRBo8USJiw5wZeR-XB9Rb3cpLaUQXsO-Gy3-CpKhUsVnKvljmwchMz_YOeqqsPMlVsGYkSqxNWe-74MR8GNwjZl9Uzy57BzbxnvOcSZBeWAbeYJUTrJlFkKorX4a8HrnUcIvZVWFa-aOeQJByMxHlAzZpDRo20dWRIElHcL8hwHqQm1NI4qBT_5_wtvxoqSIu6bV8NfcOQr0eYbbL9PnE4LO9rV5-04Yl-4b7_XQCBqtqCw2T50OIm6tfjunsyyH94xZYDbLp0l0p3_w0yLJmEIjYA02uAxJg-tB1uDa2AmEEa_9pkiRVYetoQq1mwA-T4X-UQFwADzYnIy9Phw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکس آلگری از هدایت میلان برکنار شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/90218" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=Asbf4GVzwv10xa3l8PuiEYk4KUvhmH-2So2IbSI3HHX-x_Jr9ioOJaC_n5u3vmqgSkXdZcg2PccAv6Ha15NqAq99f90W-av7JzJ7OGvUK_bTMGvtAmLj4T1FPgr0vDq11ODrLBKIIIBr2w-URz_xS77kNV3x_NVg50PcRndf9hs-1gFlRFS5EOnoJERBvcW-PsTXqZcNznrZDFw0_rm3D6UTNYirTVLmPNAvt3YruRNm6R-9HzOOhbP71xcDLgjxhfPZbR-OaKIRNhamng7wPMLt8vFYk3WNu-6KcklHiiByUSaPv8tZRxdhJYPfgQIr8GD1o2H_qJDWqn6WlRjiT7nT12PkGzl9iC1_GmS3Z7yg6MJMELuztVU9v9aPCDkDN0FB2RBb8Do5XdMmE5E4ZvUOJwLdcDaOpvC5PTCsWYzUCWcAh4nz7oKzH_Xk8Ls-BORDAqQTtbNod4i6rPchLAk0PRmGDuSdko4cEfotjBPa-40pOWO3AoO6giNbvrq7G7Ggf_zSOWhF-FrmMvjRTp6-ywwrzc3WvA-CyRB1-bfvRl0JGf6DviMQ4LDTL5pZ2keA1bH4pIy_BgpnBfcJzEer-hdgtUFQcOosPuzpONRfJCIepVKJisjqBhBndaSgv6Liq2Uq3zZ_AclqSeN5Q07fAjrDaflCwkGGFQEKBYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=Asbf4GVzwv10xa3l8PuiEYk4KUvhmH-2So2IbSI3HHX-x_Jr9ioOJaC_n5u3vmqgSkXdZcg2PccAv6Ha15NqAq99f90W-av7JzJ7OGvUK_bTMGvtAmLj4T1FPgr0vDq11ODrLBKIIIBr2w-URz_xS77kNV3x_NVg50PcRndf9hs-1gFlRFS5EOnoJERBvcW-PsTXqZcNznrZDFw0_rm3D6UTNYirTVLmPNAvt3YruRNm6R-9HzOOhbP71xcDLgjxhfPZbR-OaKIRNhamng7wPMLt8vFYk3WNu-6KcklHiiByUSaPv8tZRxdhJYPfgQIr8GD1o2H_qJDWqn6WlRjiT7nT12PkGzl9iC1_GmS3Z7yg6MJMELuztVU9v9aPCDkDN0FB2RBb8Do5XdMmE5E4ZvUOJwLdcDaOpvC5PTCsWYzUCWcAh4nz7oKzH_Xk8Ls-BORDAqQTtbNod4i6rPchLAk0PRmGDuSdko4cEfotjBPa-40pOWO3AoO6giNbvrq7G7Ggf_zSOWhF-FrmMvjRTp6-ywwrzc3WvA-CyRB1-bfvRl0JGf6DviMQ4LDTL5pZ2keA1bH4pIy_BgpnBfcJzEer-hdgtUFQcOosPuzpONRfJCIepVKJisjqBhBndaSgv6Liq2Uq3zZ_AclqSeN5Q07fAjrDaflCwkGGFQEKBYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۱۳ نظامی در عملیات خشم حماسی از دست دادیم تا مطمئن شویم ایران به سلاح اتمی دست پیدا نمی‌کند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/90217" target="_blank">📅 21:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90216">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQuOf9zKMtDanEhDpsQz_IxGPuPaK2sUv-2rNWvvUrdXO-M6KMsY5In0I95a-9zB490m7QPfke_2DStvYOFG6uk9fm0sgPwfuHZ5xhFF7c-E8k-TimNkcRMeHsAzdNg6j73dGcyQUkVxKBJ1-9zA22Rsui6knNAAvhnTEax4Xk0YVUx_pcy52iGnnxbp3rshlo_Ukjxj36psT3uxScuVjpmPrGdM59TCtVSZqE1ztWNo1Pabo_vY05yRRu8WvJ2Rnj7Nce49hL1q3eQcNxdv6RS49ysWRvk8MWdtcY0NlDO0bcfpEsqCd0R9wBcGI5eXQd4Hj12L9NiKsySUyMT0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سن-اتین - نیس
🏆
پلی‌آف لیگ ۱ فرانسه
🇫🇷
⏰
سه‌شنبه ساعت ۲۲:۱۵
🏟
ورزشگاه جفری-گیشارد
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
سن-اتین در
۱۰
دیدار اخیر خود، چهار برد و سه تساوی کسب کرده و در سه بازی شکست خورده است.
✅
نیس در
۱۰
دیدار اخیر خود،
پنج
تساوی کسب کرده و در
چهار
بازی شکست خورده و تنها در
یک
بازی پیروز شده است.
📈
میانگین گل در
۱۰
دیدار اخیر سن-اتین
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیس
۲.۳
گل در هر بازی بوده است.
🧠
اطمینان صددرصدی نشانه خطای شناختی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/90216" target="_blank">📅 21:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90215">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=I8KaePELBoj-ZQeB6JxvMqdDA258fdRnHeRqnVMlhUMNxgvjYnaXjaXrp2O6dXxTbNQj70THBHp_0KnxyJqy_isysYONy-ZpynEbcrEK6wRRLZB_SUguas58KUwpCqGVPg80vsle7m-i4Q3YtmLF21tk-kT4zOAl4SbeaBgW90JVa-VhtHtJfKBF_oolQc2Hr64DAUC5o6AMa74FCEYt_VvKGSBbNJSmO6TUcf-WSY2zRCqlwSVq4dApvMMPg5x3p-LNm7y01FKtgQi9LjSgw_XRIUpu1_EbKyRX6qCWjRX4WABH_q2nuMeu4erTUKofjZKRWWqUaAgV7vLl-9YLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=I8KaePELBoj-ZQeB6JxvMqdDA258fdRnHeRqnVMlhUMNxgvjYnaXjaXrp2O6dXxTbNQj70THBHp_0KnxyJqy_isysYONy-ZpynEbcrEK6wRRLZB_SUguas58KUwpCqGVPg80vsle7m-i4Q3YtmLF21tk-kT4zOAl4SbeaBgW90JVa-VhtHtJfKBF_oolQc2Hr64DAUC5o6AMa74FCEYt_VvKGSBbNJSmO6TUcf-WSY2zRCqlwSVq4dApvMMPg5x3p-LNm7y01FKtgQi9LjSgw_XRIUpu1_EbKyRX6qCWjRX4WABH_q2nuMeu4erTUKofjZKRWWqUaAgV7vLl-9YLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن‌روشن: فيتيله ترامپ رو بكشيد پايين وگرنه با "اسلحه ژ ٣ "ميريم آمريكا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/Futball180TV/90215" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90214">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/90214" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90213">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bAHjgC1rI3Klg6_5JYdbsGSuO1SIx5WZSDA8muxaknH4BO9x1D7QnoCHRtrD1nFQu2ry4SFLl60WSK97CYczmW4cB8PdYmuPQ5qhuq2nUnPodjtndwyM4Dqre9YccFzzdo2rxz54861NfHcn3M6WO8ul8c2Gd_iD2LLQ2lZVULgj4-ec9xavw84fAlxoIk2NoLsAIQNujLRWMvIsyKk-4rTGKz532EM6GS4JCll4g_nFDflPJ803U1Tz-OpEMIdKBxmXXOt_iWXet7_cz6RNckhxkrKCThfzw7lSyX3nIBFMHaaWFm8Rl_jP7-6iN871aOooud8mxef79ELrZcskwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/90213" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90212">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🔷
جواد نکونام سرمربی سابق استقلال از طریق ارتباطات خود با افشین عبداللهیان مجری سابق شبکه ورزش که نفوذ گسترده‌ای در هلدینگ‌خلیج‌فارس دارد، خود را برای سرمربیگری فصل‌آینده استقلال معرفی کرده هرچند که در این میان تاجرنیا قصد دارد با سهراب بختیاری‌زاده در فصل‌آینده ادامه دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/90212" target="_blank">📅 16:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90211">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkpK8U4X9BoBkLi2XIrWPfegBUU-iGkTpsXSQVrZdHkziwRir_Tw7GiVTSjIj6Jg1cKs67VYpL4K3lLdJZSVpQ5TstoMnUtT2na0TGJrdx2EAK7tsp_IcR7C0l5GabSb_aaBWuGfPFxKk8fJ9cHdE3aB1jto3An3QNirF9-JsviIBObwLJBg4d7qks9cWC8I1s0xy8btocpkKjgF71lD8uPxv6ID8nmeZSol7XGj_BvlAq0V0UHztEtNO53Rpo-74z_WLsHQ1NvTIlDs-7Rm2lkEq3FRiOLYi1rV2xzV65yD7nQcsqTfPp8upJOn2wtPau5sM8QKK1RRB1TYSeWgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست تیم‌ ملی اسپانیا برای جام جهانی 2026؛ بدون حضور حتی یک بازیکن از رئال مادرید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/90211" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90210">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90210" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90209">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
ستاد راهبردی فضای مجازی صبح امروز موضوع اتصال اینترنت بین‌الملل را مشابه دی‌ماه سال ۱۴۰۴ مصوب و به رئیس جمهور ابلاغ کرد تا در صورت تایید نهایی،‌ وزارت ارتباطات موضوع اتصال اینترنت را اجرایی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90209" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90208">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=KrWyggHqbh3sZudn6KW_6MghLx0euA9lM8kBFF47NkQH7U9C_mz-oMZfwPqdssQq61zjAYY8_nU8cy-hDYqIBFIV66UulfQrvWuPC0Z8zi3-uILhFSKN0-IRuD5UnK2pbX1g9UY5nUIXRKlrdjyzXpDfgYbth6S8UnbU9f3YZvT0Ax0P2Zwjmrbru3s1I9R2gKkY8ZGNTm5j68KGRqh-Y5ZEFgWyKw4LNldKsPeXgaytfu7oCsU5MyJXE3Je5Kkg8qN1oG-LwU-VkedjS544mQ4xQ1yp3J02KUkWfz77_MytFNJe6CKG6ydVLTh4_s81Lcyt2Hug7O7CLrYxei4UsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=KrWyggHqbh3sZudn6KW_6MghLx0euA9lM8kBFF47NkQH7U9C_mz-oMZfwPqdssQq61zjAYY8_nU8cy-hDYqIBFIV66UulfQrvWuPC0Z8zi3-uILhFSKN0-IRuD5UnK2pbX1g9UY5nUIXRKlrdjyzXpDfgYbth6S8UnbU9f3YZvT0Ax0P2Zwjmrbru3s1I9R2gKkY8ZGNTm5j68KGRqh-Y5ZEFgWyKw4LNldKsPeXgaytfu7oCsU5MyJXE3Je5Kkg8qN1oG-LwU-VkedjS544mQ4xQ1yp3J02KUkWfz77_MytFNJe6CKG6ydVLTh4_s81Lcyt2Hug7O7CLrYxei4UsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین ریکشن‌های پپ‌گواردیولا در منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90208" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90207">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90207" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/90207" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90206">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJPnqqHmVgE2u0BwdTtDIkHWcJP8MunfKYk_nsCoxOw89p652xdJ7IZw-rM_nlpUvfOtcxPzoUJMgUKqvPU8XFbzkWdSIDTdHpQcprIxVyyCXbQ38jPIhpPhTqqR1g41ylOev1qf2tYcqYcBqU1rPWlGl_et69lW_0tEFq3JP2SKBJWaMhpt-rD4ERsOoim1JbbZ04eB1gkYleAl_yUUmPtgTtC70meNfSBUcEPgvVwWED6UyXV9q_OwZDZNE0qgO5xiXkbwZBQQtbgkyoTf3qAIm0A-x5AfBOpQ4dikOnUKa1n7Xkiurtu99YZDzZDZ3dgcUODqmhtqyLfMKL_Cxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/90206" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90205">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940870b589.mp4?token=LGu_yvtfb3jfgQHzZXCU10sSXY4HKXb9vvhI329_b_Wf5J4U-8KNWwiTUeIqq_ywpwGer8MVQEiTJmqnZZ6rFSqGQoD-I79mFjdUhWaiEdEtfMYrQ3DLKimK6-22Ivb_KthgS0fqA-IRIGUbKBCAITZq0YL909pxFuDeaxqLwhvosgh-k-D7wEKVLlpnz1pQgKBUiD_h14XYMHaLsBnN_KV-Q9y4qy8aicBexb-CyYp8dVZoe7Z8BcHnLjUctCDQKhWWPIiAHQNeDyGS66NjXv61oBKrbQEyQQdZcfQVdbzg4zLTaOo0Tsx7ueEzw3Sk89YnPTUVDXP_awMf-z6NsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940870b589.mp4?token=LGu_yvtfb3jfgQHzZXCU10sSXY4HKXb9vvhI329_b_Wf5J4U-8KNWwiTUeIqq_ywpwGer8MVQEiTJmqnZZ6rFSqGQoD-I79mFjdUhWaiEdEtfMYrQ3DLKimK6-22Ivb_KthgS0fqA-IRIGUbKBCAITZq0YL909pxFuDeaxqLwhvosgh-k-D7wEKVLlpnz1pQgKBUiD_h14XYMHaLsBnN_KV-Q9y4qy8aicBexb-CyYp8dVZoe7Z8BcHnLjUctCDQKhWWPIiAHQNeDyGS66NjXv61oBKrbQEyQQdZcfQVdbzg4zLTaOo0Tsx7ueEzw3Sk89YnPTUVDXP_awMf-z6NsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیگه محمد صلاح تنها قدم خواهد زد.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/90205" target="_blank">📅 11:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90204">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=RJoDOXIwNsWz8jl8dT0lVut-sj1pDOAc_1ocMyM8mQe6oUa-ZgzrUV5essnfvhkZo2zBAZ4jQijPqUreK5GdUydLfnRNDRL6QkQuFnI-SiJ3TOznQSWyBAgIl9VQkHb6VAi-WFSVolsOxXPZD9BIZwnVU6b5i6KrgWgTtxLCmLgjd-ENClV2xZ7Agf-e_sQ1LTJHw48Ue9uOYVAs4LxHlxQ6sbIFRDn6uIkE_pr6hSqR3VG3NK2F9-jAbj_2CIjMqx-R7STBg0EhmowPKgSQ3TbkcSdXQ-L9csZSGAJ5tNkJUrZ3PlRMAib5llnwczFH8wnhcMdMrAZwLWrwN0AfwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=RJoDOXIwNsWz8jl8dT0lVut-sj1pDOAc_1ocMyM8mQe6oUa-ZgzrUV5essnfvhkZo2zBAZ4jQijPqUreK5GdUydLfnRNDRL6QkQuFnI-SiJ3TOznQSWyBAgIl9VQkHb6VAi-WFSVolsOxXPZD9BIZwnVU6b5i6KrgWgTtxLCmLgjd-ENClV2xZ7Agf-e_sQ1LTJHw48Ue9uOYVAs4LxHlxQ6sbIFRDn6uIkE_pr6hSqR3VG3NK2F9-jAbj_2CIjMqx-R7STBg0EhmowPKgSQ3TbkcSdXQ-L9csZSGAJ5tNkJUrZ3PlRMAib5llnwczFH8wnhcMdMrAZwLWrwN0AfwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت لیونل‌مسی در فاصله ۱۷ روز تا جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/90204" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90203">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76980eb486.mp4?token=QHKNopueYM_m7Sl_iVNrRgO1FJRIRhfJFAkPvlr-6g7JaoM0D52dj5lTeYLVXqAYc4-iQ8mTD51iw1ggz7sHrT_08A9kChU8t885B2NE-END6U5ubuLTwFnSgUrR6Wk4BG_uERGqz9IiY-g7qJ8pii7FEV7GBEMN7Uge5oM2bHnX8VjCYBpiM7a_Nzkb4lhjSMaOWRHx00aztk5sTACaJ7GAcwUgpJLEQ36ns43OaJcpx9hMTRxLr1lHRHdHxS1_mYeDCHRJ-NDhnp16p9RSfMWCSwoYyCG7qNr1a_JiPRZG0zTJiLIs28_V7EdAh_ObXjb8qLVABdIpqMECBH5PJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76980eb486.mp4?token=QHKNopueYM_m7Sl_iVNrRgO1FJRIRhfJFAkPvlr-6g7JaoM0D52dj5lTeYLVXqAYc4-iQ8mTD51iw1ggz7sHrT_08A9kChU8t885B2NE-END6U5ubuLTwFnSgUrR6Wk4BG_uERGqz9IiY-g7qJ8pii7FEV7GBEMN7Uge5oM2bHnX8VjCYBpiM7a_Nzkb4lhjSMaOWRHx00aztk5sTACaJ7GAcwUgpJLEQ36ns43OaJcpx9hMTRxLr1lHRHdHxS1_mYeDCHRJ-NDhnp16p9RSfMWCSwoYyCG7qNr1a_JiPRZG0zTJiLIs28_V7EdAh_ObXjb8qLVABdIpqMECBH5PJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ در گفتگو با بهاره افشاری: امیر قلعه‌نویی واقعا غیرت و معرفت دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/90203" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90200">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4l_MlOE7F7Q4CfCv2fSIFnVnyrgVgv5e9BKf1UQ2-rnU0D2y3g3iQP7VrG-6h3RmDxqWHPUqwuhlYi8IH0hL9B8dSPCNHP8vfZiJxx931FVTMzaE8S34lBNqQCh4xu_9HxoOj4sSYoSu-DHUANOXAtYD-4NrFYORfwtRnwNp98oaBRV1v6pWw5V0hQkE11b0zB7x-IS1-uJPHlDLMJl7ihxh84K2nzm139M_ih-4D90Ea3kNEzX7avnR_JoM84BPzwKZzBzD9iwP4Cwx1_NgzJwIARvxQyFetD1wPXZNvigzrlO9Ht4sAo9U4xG1oj-cMf0szhZ26_W9rh42nTyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخشش کومان ستاره النصر در دوران باشگاهی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/90200" target="_blank">📅 00:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90199">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=U1gMvqtUuCpam39mRVG94NE1C5scI7KkXKE0JkWETjgdN_aSL8RJiFACAL4Zr_69lCI_LyDPNvDtmtCgbuQBY7GHhbpDP_-zsEzX0iOGuxky1Am4kK5EwJJ0o0cB_-ch3GVPa_Y3CGlf4Cy6MHTKgBkTs8BPkhw2ZFG1KBLl7KqqtcWRxeHNcuKpIMO5Qeh84M5VuaSNwrcBwrt5qiADRadyRRG1Dr0jRlHvw-SyscsJwWeFe9MpnbvozQ5oK3WxcyOymXMV8gCHuyWZfdmjmMIoQmACtk8lynJ_LyDla9wafi4VP_44Aa7Bxe2EOUlyTH5nmXyhJCmQOfAeZGz7jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=U1gMvqtUuCpam39mRVG94NE1C5scI7KkXKE0JkWETjgdN_aSL8RJiFACAL4Zr_69lCI_LyDPNvDtmtCgbuQBY7GHhbpDP_-zsEzX0iOGuxky1Am4kK5EwJJ0o0cB_-ch3GVPa_Y3CGlf4Cy6MHTKgBkTs8BPkhw2ZFG1KBLl7KqqtcWRxeHNcuKpIMO5Qeh84M5VuaSNwrcBwrt5qiADRadyRRG1Dr0jRlHvw-SyscsJwWeFe9MpnbvozQ5oK3WxcyOymXMV8gCHuyWZfdmjmMIoQmACtk8lynJ_LyDla9wafi4VP_44Aa7Bxe2EOUlyTH5nmXyhJCmQOfAeZGz7jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
بازیکن تیم‌ملی والیبال ترکیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/Futball180TV/90199" target="_blank">📅 21:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90197">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028fa17067.mp4?token=f9Cee1MSf1891WRmPzUtKl2yDOM8oPqgSaFDvMZkhyiIbMmZW3JF2nsFUDNiWFEdr2DFzYw8d61e7lEsOEkd7uHOWhEvcOtPiVhYmj5_6qTxztko8jgH8-RW2zuKEGV4Ftv9tiiiYSse6Wsoj7iiA2P8YHbp31NIwxvjm7uTw1pPPGzL-7gn3fQjr6bm9oP6Kpil1Z1LA6-2quE74YHP7haoMn59oT5Eslt2E_kzyWr5N9jluziAaB-19MUScxJFXh5w1hxVaMJaSDPszKOFRiy-xaP6WTQsL3sQKUQ16oKi4z523eg_1Eq3fy0vcjFsWiVBEs8BrC0AyUNDu14dFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028fa17067.mp4?token=f9Cee1MSf1891WRmPzUtKl2yDOM8oPqgSaFDvMZkhyiIbMmZW3JF2nsFUDNiWFEdr2DFzYw8d61e7lEsOEkd7uHOWhEvcOtPiVhYmj5_6qTxztko8jgH8-RW2zuKEGV4Ftv9tiiiYSse6Wsoj7iiA2P8YHbp31NIwxvjm7uTw1pPPGzL-7gn3fQjr6bm9oP6Kpil1Z1LA6-2quE74YHP7haoMn59oT5Eslt2E_kzyWr5N9jluziAaB-19MUScxJFXh5w1hxVaMJaSDPszKOFRiy-xaP6WTQsL3sQKUQ16oKi4z523eg_1Eq3fy0vcjFsWiVBEs8BrC0AyUNDu14dFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیشب آخرین بازیِ دنی کارواخال با پیراهن رئال مادرید بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/90197" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90194">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=j3fTroUwLSWg9uUWcJ4GBqOBoTHrSTzs0IqbgwLPlsZkk8uCyuuMVvrZMqGICSEMBzFqGIzFDNokCsM2vYUfWF2Rm3WELZtCCbcIaKK07weltyzYD25oICtqCC-iGCxGYt0rMWDMZVguJzZ209l21A7nbkaZccp7aMB-6m8PvlQVstA7XFqx0xzzeRSmnQKO5rMWMtz75n1TFkroawoFORS1lascFQEovvhkGFCew6fhM45UCx---Q0ITvH_B-14kRf-9CffKpCAvbRGYWQUWzcqzfze_rYdCsoTP0ZQiqXz_Bx8UvL4jpsk9xtpSdqsUW0QGKxAKw5m5tFmIJOm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=j3fTroUwLSWg9uUWcJ4GBqOBoTHrSTzs0IqbgwLPlsZkk8uCyuuMVvrZMqGICSEMBzFqGIzFDNokCsM2vYUfWF2Rm3WELZtCCbcIaKK07weltyzYD25oICtqCC-iGCxGYt0rMWDMZVguJzZ209l21A7nbkaZccp7aMB-6m8PvlQVstA7XFqx0xzzeRSmnQKO5rMWMtz75n1TFkroawoFORS1lascFQEovvhkGFCew6fhM45UCx---Q0ITvH_B-14kRf-9CffKpCAvbRGYWQUWzcqzfze_rYdCsoTP0ZQiqXz_Bx8UvL4jpsk9xtpSdqsUW0QGKxAKw5m5tFmIJOm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهناز شفیعی :«می‌گفتم ناصرخان یک کم کلاس بگذار و با زنگ اول تلفن را جواب نده اما ناصر قبول نمی‌کرد!»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/90194" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90193">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
آکسیوس: تفاهم‌نامه ایالات متحده و ایران:
🔴
- تمدید آتش‌بس به مدت ۶۰ روز.
🔴
- هیچ عوارضی از سوی ایران بر تنگه هرمز دریافت نخواهد شد.
🔴
- ایران ابتدا تمام مین‌ها را پاکسازی کرده و محاصره خود را برمی‌دارد. ایالات متحده محاصره خود را تنها پس از برآورده شدن این خواسته‌ها توسط ایران به پایان خواهد رساند.
🔴
- ایالات متحده برخی معافیت‌های تحریمی مرتبط با صنعت نفت ایران را صادر خواهد کرد.
🔴
- تعهد ایران به اینکه هرگز به دنبال سلاح هسته‌ای نخواهد بود.
🔴
- ایران متعهد می‌شود که در مورد تعلیق کامل برنامه غنی‌سازی اورانیوم و حذف ذخایر اورانیوم غنی‌شده خود مذاکره کند.
🔴
- ایالات متحده متعهد می‌شود که در مورد تدریجی برداشتن تحریم‌ها از ایران و بحث درباره دارایی‌های مسدود شده ایران مذاکره کند.
🔴
- ایالات متحده هیچ نیرویی را از اطراف ایران پس نخواهد کشید. خروج نیروها تنها پس از رسیدن به یک توافق نهایی در پایان ۶۰ روز رخ خواهد داد.
🔴
- جنگ بین حزب‌الله و اسرائیل به پایان می‌رسد – به اسرائیل اجازه داده می‌شود اقدامات پیش‌دستانه‌ای برای جلوگیری از بازسازی سلاح‌های حزب‌الله انجام دهد؛ این شامل حملات هوایی و پهپادی به لبنان خواهد بود. «اگر حزب‌الله رفتار مناسبی داشته باشد، اسرائیل نیز همین‌طور خواهد کرد.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/90193" target="_blank">📅 17:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90192">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqcDN4dl8Jy5JgGMB4VJE4vdUhXzzgNO9mnd1NKUwWeHFj83emNd7ijSHiUxi_b4fSBws1DtmWIPO4of4yV6ElgSAd4_4CmjJGOBIj1sHvKYYoH0DELDX5R5W1nTGhZE20-Q53GE5R_D9fjRNWfornWOvqULD508W-rQSgkm10nquPYyKQPQ6o6CZ-0zjQzEVbFhvhSqx17xWEj0qEeyztaDiN0FZrZgPCzKB-wE5Xim0f_nRfGmRRVKtpQpIaSf15lVCyaUQnNKfOGWrXNcyN6_Knfhf_A662r8baSb-pHAVP7NyOzWSRMAOAgE3XRVEaqk1C7Za40rVgiBuEyw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب مشترک داکنز نازون مهاجم استقلال و روماریو اسطوره فوتبال برزیل در پاریس؛ هائیتی و برزیل در یک گروه جام جهانی 2026 حضور دارند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90192" target="_blank">📅 17:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90191">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihJY9QJ3v2XgziaMOIYlrqkrAmkCVPKyXyqTXQ4a5xuPB2SJTYH-4HCw2mbQHR8E4bbuxYQmm0116veLwrPHWFnQg_2u8uF7xOICyseysJifcUTCc1pEg5e6xvF9w0BpIzrTyXj6kzP9YhkzRJZgeTREmldzqNu8QTURNl3_-2rpwNxwcnicry9mcdsFIqkZ7Zvsb7N4nWV2ZiAVxeY2QdVt_rOa4NWzk8FVXhTHJAKwxDso3rrT-QOR4ohyhyBYN0bt5N5k7Kbly84yELDC-b-X3X9zhmZTBwKMijXnL_7w4nIyLfslNxo86omgVjUCWaKJM8qeYOzq3O1BuSuc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: خدانگهدار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/90191" target="_blank">📅 16:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90190">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67618efab5.mp4?token=f5Tqk_Kt9WYKvx-BtnPLsarDjvFkM2rATWUdiXs_lTSI7e-UOGJk-VabsnnQdWzT-3NHb7X0HI74znO8OUzwXXma-_bCWT2r2PQJxFyjtH107ljL4RF7LTS4jbb4i82015dhUYnwfB9NlMxs3rkwgIdCwxxvK4FsyfHZoT-IyuzunLBU68sOSuZcEWkUOxht15pYo2qthn86Gu39ZYPhb15PHZI7Rxh7gt78dY1eEtcXO9pdN3LaW-UMVH81uvYqv8fii2VNfrXUiXyAakE_xS8fw_9Kb2myIc3k9hdTfpGSskumZWk0sAGTudvIxay5bdnFhthKgNK_iSVVs3hb-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67618efab5.mp4?token=f5Tqk_Kt9WYKvx-BtnPLsarDjvFkM2rATWUdiXs_lTSI7e-UOGJk-VabsnnQdWzT-3NHb7X0HI74znO8OUzwXXma-_bCWT2r2PQJxFyjtH107ljL4RF7LTS4jbb4i82015dhUYnwfB9NlMxs3rkwgIdCwxxvK4FsyfHZoT-IyuzunLBU68sOSuZcEWkUOxht15pYo2qthn86Gu39ZYPhb15PHZI7Rxh7gt78dY1eEtcXO9pdN3LaW-UMVH81uvYqv8fii2VNfrXUiXyAakE_xS8fw_9Kb2myIc3k9hdTfpGSskumZWk0sAGTudvIxay5bdnFhthKgNK_iSVVs3hb-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر حجازی: دامادم گل زد، تیم ناصر سقوط کرد، دخترم گفت طلاق می گیرم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/90190" target="_blank">📅 13:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90187">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=gsW4AuhjN2pGabPVrE8CeG_ZntAjPXFtsndQnI_Xcc_wAl561PemUkuHJcOkV-1eBMDYTSVm8F3p-C-GbNGu4bdKGqflwCwTdPy2sOG5ZnAElf5K9dvsiMkQ1jZqjPPTS1XMOvBTDd_ZRrmVxhDTsbG2OMXs2yGExggsGXZ99WdHKXhGy3mWaAaKoN7K1lN9H6LsJ30F3R8X8Q1iugN0Q6zQC3blIQc-L66X6L0gDyawE135hYW5JUH0dB9M8Xf6Y8aC6iaEVFG_rvzwKxhSu3rdqV1ZutSGIFRFZ33QQnJ6fR8coUPw2pNr61t7CZOMF-oRCnJeRc6MKWA2jjIlQIV9a3lZrkwFCi3L8cjSgBiQlBzPn6mipIZAP_f_RC3m0YCVTMeorByI3csmZXF37Iw7zcm72k3UDZ1fC2AgpB3nrUEagizJh-fHR0Ot7ckj-BkCFWJC42UoGaPQlWl8IE2lQyC86BfAncaIt_Xzcqfpn7Mftc1ElKf3r5n-5cnG8qfhS78xyIiSKl3qx_tiLx-xSrCUw8d9oVAUVteC8aWt91lyOTFEfQCLDo7UjEN8KVYl5_moJZtuLblTsNtaMLb5PgyMX8ic9eUja2awAdaqr4U2mPtNzjnLim57V8xgVW5IbGvPOiDyGZ7QJXout-YVbd0X-U5RykXaDKksOSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=gsW4AuhjN2pGabPVrE8CeG_ZntAjPXFtsndQnI_Xcc_wAl561PemUkuHJcOkV-1eBMDYTSVm8F3p-C-GbNGu4bdKGqflwCwTdPy2sOG5ZnAElf5K9dvsiMkQ1jZqjPPTS1XMOvBTDd_ZRrmVxhDTsbG2OMXs2yGExggsGXZ99WdHKXhGy3mWaAaKoN7K1lN9H6LsJ30F3R8X8Q1iugN0Q6zQC3blIQc-L66X6L0gDyawE135hYW5JUH0dB9M8Xf6Y8aC6iaEVFG_rvzwKxhSu3rdqV1ZutSGIFRFZ33QQnJ6fR8coUPw2pNr61t7CZOMF-oRCnJeRc6MKWA2jjIlQIV9a3lZrkwFCi3L8cjSgBiQlBzPn6mipIZAP_f_RC3m0YCVTMeorByI3csmZXF37Iw7zcm72k3UDZ1fC2AgpB3nrUEagizJh-fHR0Ot7ckj-BkCFWJC42UoGaPQlWl8IE2lQyC86BfAncaIt_Xzcqfpn7Mftc1ElKf3r5n-5cnG8qfhS78xyIiSKl3qx_tiLx-xSrCUw8d9oVAUVteC8aWt91lyOTFEfQCLDo7UjEN8KVYl5_moJZtuLblTsNtaMLb5PgyMX8ic9eUja2awAdaqr4U2mPtNzjnLim57V8xgVW5IbGvPOiDyGZ7QJXout-YVbd0X-U5RykXaDKksOSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت همسر ناصر حجازی از روزی که شُهره به همسرش پیشنهاد شام مشترک داد
همسر حجازی: هم خودم را باور داشتم، هم به ناصر مطمئن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/90187" target="_blank">📅 10:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90186">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
روزبه‌چشمی بدلیل مصدومیت از اردوی تیم‌ملی جدا شد و به دبی رفت تا مراحل درمانی خود را طی کند. احتمال خط خوردن این بازیکن از لیست تیم‌ملی برای جام‌جهانی وجود دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90186" target="_blank">📅 10:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90185">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hffZsjOMD7_AU5Hp73yeXH0JQccurXljMtwgnDa4AP2ZmQW_Zv-N6XBiWZph4B9I73ONsNEnjhT5Rcy5tOkGx6KeMvyuk8kEgX_4pY6-oEHw-CNHhe-irHsTfz2sFisRx55ldeZHe2-04kC3E0rYaBzQ6V8eZvxeWqLOfkbYUAiyc8JZUXy5KNEOi1j3ewt4euIDrIjxwVgUqSgWjmc4O8ZJU3u0Vi1y5PtpEaNFlnyE9COgyNXnshHzzqDKdkPnE2SApxAq692vqrBQPuD2nySJjnQElm8vCjClBVzdLEhzu2se3ICpANw8dSIIRS0GGy3b5ZSmcq7aw-_Bz8hQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس ایران پس از شایعات توافق:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/90185" target="_blank">📅 09:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90184">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=LYkgn1E2HHr5n5NSOxAcT1AC47CxWR-nYJpGHKOudDIZnrIj01wkPDhLNRHESSbdQJ3NZ1PUX2mOLG-uw4KTwyUQAGGEh-ksW8qsD2jwdZbM_GHkqu7Rw1wocCqPVA7fOOgC0tcwbPD3lMnqEFMJpm-B8Pq73GeEwZ-QHJWRZEMnqlZetYzM5839ELf878Ap-iYQo4hkUdIJMahH988uU4fyNDFjT2jpqRjnnKYlSbh_eUtZECfhbLq3douYtpZtiO8X5eesGOpC0i2MtYWT2trAQXNxuQ0LKIG3v-ARhEQAngf0W_xGKHMOrAo-6pLN4rui6QwoQ2kOqQZYwTOMaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=LYkgn1E2HHr5n5NSOxAcT1AC47CxWR-nYJpGHKOudDIZnrIj01wkPDhLNRHESSbdQJ3NZ1PUX2mOLG-uw4KTwyUQAGGEh-ksW8qsD2jwdZbM_GHkqu7Rw1wocCqPVA7fOOgC0tcwbPD3lMnqEFMJpm-B8Pq73GeEwZ-QHJWRZEMnqlZetYzM5839ELf878Ap-iYQo4hkUdIJMahH988uU4fyNDFjT2jpqRjnnKYlSbh_eUtZECfhbLq3douYtpZtiO8X5eesGOpC0i2MtYWT2trAQXNxuQ0LKIG3v-ARhEQAngf0W_xGKHMOrAo-6pLN4rui6QwoQ2kOqQZYwTOMaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی باشکوه کارواخال از رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/90184" target="_blank">📅 09:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90181">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX-iMyp1EYD12bOvKe8wGZGeueAbgV8OiRZdEnK6b3P3NREmBTXTx29ajd12LH33bnVD4AcWjxWUvHkrtoO4rOFON8_qZY3l-xQplJsiYxaWKAO2WYuRI-J8WG1ygMoOVN3HqNNMMgLGIDcp4xXesllOga7vJQzgJ4bG1TsFSq6JnvTa31lpN5LvH4cvw_rRcfscbhJSQ956eVzD5wI6dogcaPBfD8uzP84ugS3CQqKatj0zXQewHocNglU9JDDxtV2B-0DQpEWpBu7gb6kcqFaRrruCeSZyl8-fEZnCZvV1gQjyMlSnya2k99o9jAMRFHGHLbS8wCUup3QekK8PKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
ترامپ: یادداشت تفاهم با ایران تا حد زیادی مورد مذاکره قرار گرفته و در حال نهایی شدن است و به زودی اعلام خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/Futball180TV/90181" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90180">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCymOeL17FfkxPMQa6ey9ebRvWuxbHOOMfFStZckTpQWBmXLAUniz2FWCuxIRogYm_6mf-r5JC__3W9HcrOY-UpsHRA1TnoMNHpQvyt420JHuOpCrMB7dhpTihBpTLa4SOSY1nNyy1oVIS_Rrkmej4Tj311gsmXKN7AuY9eomwqNtr_fqn-Sx39obf4YkJfVkj9xf0MfrDGW0TNIK_Q6us9J5a5q-pklZL9fHxwd7kdwsruD-GgLwKlxUfwl5v-pDsXpg8s_RFz9V0cjyQjDOoSCx-xjYr81ZHpadlR6vPNqolifyMB9jAgrQoE8JzFq5cl5hfzJn3A3CRWFYghtPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تیم‌فوتبال زنان بارسلونا با برتری قاطع مقابل لیون قهرمان لیگ‌قهرمانان اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/90180" target="_blank">📅 23:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90179">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWFhAlqO7Cf5iZ89dA6vQ6JXkSmvjlSgOL9ZUJPwh5rbUfeXkcSDhALuLV97LKc9Fh4FiDGrw5zR0f2TbulN4qw5HEWqFaeA0FmXCHXER2gFWpZg7EGbGRQDa2XfJiKY4nSBruZxu7T2YfCLrX2Gc00CSWK-F_hQ3LZyj72fIzmGaMdoxwsXmgXvXp0QhCzYaDTnQ3kOJs-lO3L2ahFWmZH4vVj4ZyaPcXICGGIwhfTHgkXeOSUcCzLxdHXbZT_LYZLUXSj5rIic7g_ZhIzxbqrmnDtAtlX85t6nwwacyi8gPE3hpp7yjPSbSCRCUbaTIF3Ljdnmj-4r5A_yPZkIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون درگذشت پرویز قلیچ‌خانی را تسلیت گفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90179" target="_blank">📅 22:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90177">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=nN7VFDKn1cNjEVRi4b4Umq19-FVma24Mmse54MUjLlVxsXaOpspuILt7clIbBiNSLVBtCl5gw3Z75U4UrrA_kA5JmXaEqEezroVxDUKrH6FBT7-dJRr64Kc4l6P7JnZIZ6frQ-zRTefAGccaHomLy4mMKZY9MnmaA17j0PEUPw_kkYiTDMez8BCUdMIrehOZM6rnlWpBgqZpih9zv0t3zGcc8ag_iZ6TyXxcfcxr1A-6FcrSsxMe39RuzxyHwfcVgGEARMhdMe_uPZuIXuaQInCMWWXI4OlYjZqA_2ScYMuYGEvF8_6lvIy39aTWB4scwoWJeSlsFFete2xQxJ98LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=nN7VFDKn1cNjEVRi4b4Umq19-FVma24Mmse54MUjLlVxsXaOpspuILt7clIbBiNSLVBtCl5gw3Z75U4UrrA_kA5JmXaEqEezroVxDUKrH6FBT7-dJRr64Kc4l6P7JnZIZ6frQ-zRTefAGccaHomLy4mMKZY9MnmaA17j0PEUPw_kkYiTDMez8BCUdMIrehOZM6rnlWpBgqZpih9zv0t3zGcc8ag_iZ6TyXxcfcxr1A-6FcrSsxMe39RuzxyHwfcVgGEARMhdMe_uPZuIXuaQInCMWWXI4OlYjZqA_2ScYMuYGEvF8_6lvIy39aTWB4scwoWJeSlsFFete2xQxJ98LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
افشاگری همسر ناصر حجازی؛ علی دایی تمام هزینه‌های درمان را پرداخت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90177" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90176">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hn2SJlMcownk96N2XdFL66bReDMUmNep5n8cpFgExx98pJzvDQV4Qlt84MP2x-IcUATxXTWFTWcHtw-bM7xYndHepCK0Gu4ybsL9gYAemT6wmaIGrTcknzn0-k_KkyxNQA_nb7gTh8TRVOE_JYQZmPT1c20_BJb8i19R5YejyQGuo6JWjD3-V3e9_uh_Ll_DJrdeLXALwBd3bopU-dqqmNiD6kA6w4myFkn7wuD72b0iJLMUU894el3Vy41SAsCvYNG9dobqSycbmz6YuhL2ertcb7VwhLx3PRHMXE7qGglUS7zPYx40Lxd3vWPqz-GOSF2SWP4tZr8zPQq7CTR_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مائوریتسیو ساری با جدایی از تیم فوتبال لاتزیو سرمربی آتالانتا در فصل‌آینده شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/90176" target="_blank">📅 20:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90175">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=q9QiGsrfP_GfZu7xiwSXdFmmaqNwY9KukWuOQLfAdSWDhYvPGe54eKb9rGbOzZA-CDjWfQXsdVQf-lgDJeW1-TA6v_WLPEdvdzkhVPnaXUu9msLktfaiYp8dL65C_MA36Yij9I5xZXUBN0SdIf8Xd2FFs3fJK_USqjZSJrws28cN3bNljKyFLAKA7Ah0niGfw247rA_FLfEeWB7GYLuLypQQHLNJmogsznVgsqeVGq5tkPNKXHhI8Q1DhLD3mCj-lgUXSrc8KF-uhuJgjlvXSImEWyDkGvAgsN6_UYSE4l1Huj8xv0d3xh3anBY9PbyIxEz2z4QenboIgp7jysT-nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=q9QiGsrfP_GfZu7xiwSXdFmmaqNwY9KukWuOQLfAdSWDhYvPGe54eKb9rGbOzZA-CDjWfQXsdVQf-lgDJeW1-TA6v_WLPEdvdzkhVPnaXUu9msLktfaiYp8dL65C_MA36Yij9I5xZXUBN0SdIf8Xd2FFs3fJK_USqjZSJrws28cN3bNljKyFLAKA7Ah0niGfw247rA_FLfEeWB7GYLuLypQQHLNJmogsznVgsqeVGq5tkPNKXHhI8Q1DhLD3mCj-lgUXSrc8KF-uhuJgjlvXSImEWyDkGvAgsN6_UYSE4l1Huj8xv0d3xh3anBY9PbyIxEz2z4QenboIgp7jysT-nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهناز شفیعی، همسر اسطوره فوتبال ایران ناصر حجازی، گفت حقوق بازنشستگی او ۲ میلیون تومان است.
او در ادامه با انتقاد از وضعیت مالی در فوتبال ایران گفت چرا باید کارلوس کی‌روش با پول این مردم به سطحی از درآمد برسد که بتواند برای خود در پرتغال جزیره‌ای بخرد، در حالی که ناصر حجازی در آن زمان حقوقی بسیار پایین دریافت می‌کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90175" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90172">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=T-MIFTWOONz9XPwW9be0t8MHQ98wBbTUxRhhItfZIihQvdFLERP05HDTNPKcl_Qbwu7vAvtq795LMmSmY0SnzvN4VPCw_Es5vFCnU-215IeVSRisKog0_fEnKx3CzwW9kfjv9iYRwWJeiQLTJ-Y_f8_8_B5yzMM8-NklC-nY2xHfl5DozjMkLzrLh0bAJhH4tyE5MXa-RcPfn-W_RNR0hu1DlsS3RPjyDWPod8lbW1hq3rAcL4hPZbCmcA9aEWsWLhtsjTjxuDxiTqdPnodhf9yLtK3QnLSruWxWuuD6hN5qE9KpUIUUDGb9eFtVMTBogZGHY2K4FC9MF3vaNW7faw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=T-MIFTWOONz9XPwW9be0t8MHQ98wBbTUxRhhItfZIihQvdFLERP05HDTNPKcl_Qbwu7vAvtq795LMmSmY0SnzvN4VPCw_Es5vFCnU-215IeVSRisKog0_fEnKx3CzwW9kfjv9iYRwWJeiQLTJ-Y_f8_8_B5yzMM8-NklC-nY2xHfl5DozjMkLzrLh0bAJhH4tyE5MXa-RcPfn-W_RNR0hu1DlsS3RPjyDWPod8lbW1hq3rAcL4hPZbCmcA9aEWsWLhtsjTjxuDxiTqdPnodhf9yLtK3QnLSruWxWuuD6hN5qE9KpUIUUDGb9eFtVMTBogZGHY2K4FC9MF3vaNW7faw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دوم خرداد، سالگرد زنده‌یاد ناصر حجازی، اسطوره باشگاه استقلال و فوتبال ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/90172" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90171">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxR4DxZCzjs00SiSKhrNxP_-qdT5tWu2huZ4AqF7vuS_1r2Ff6VJ0MBAx5O7x0u5tZQcbCiMXVkieOwMrZgnMzq5RhrJVWIfxmLWHV0t4kic7qqQDCOJSR1qGhsCifbePiUfACsnEuSGJKb7fF8CVPBOhaaizcs_SGXpSL_w3EHQBs0CpMRHjqSgvE2cY00FcMxdSF29QHB9m6fOGl2gxhimeW1xxk4WLhpA6UqgcnTLQj1vR0L6FuXxS8KvIOR3IL7fy1aS6SzLQJsk6i-BWNxJ_3Pjxn34kAnUfSPDB7OfBlVc8B0CAN4lMfWKH7qgJ0jv27pzufx9QheD4ZuBpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
تلخ و ناگوار؛ درگذشت چهره افسانه‌ای فوتبال ایران
پرویز قلیچ‌خانی، چهره تاریخی فوتبال ایران و یکی از بزرگ‌ترین تاریخ این رشته ورزشی ساعاتی قبل در حومه پاریس جان به جان آفرین تسلیم کرد. قلیچ‌خانی متولد ۱۳۲۴ و در 81 سالگی پس از ماه‌ها تحمل بیماری از دنیا رفت. او تنها بازیکن تاریخ فوتبال ایران است که سه بار به صورت متوالی قهرمان جام ملت‌های آسیا شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/90171" target="_blank">📅 18:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90170">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLU-W_HLNHKHABoutm2HUCkw7hT3kXUbPahSXWDBLGXyaZk6vzRKQeUdZ8XcuuFY6Yja3SSq7CznALs-IVRP9mMfM8FxujsL245yMMkZX6IgDbK1ACMun2-hnL8gS8ppTGAfGLvKXwTJN6gLK1f_gpr0NYTkWfenIPBoYVF1XacaDFvZ8i5pNCaL-UdZD1ijW_McO45F9iBOhg6tCJGTqIFfpRsMNhAWBJgPHoWb4yPtGVEh4NS_bAQUAQjhqev6E_t47BQekL6up9LAFuEeJTKm4z_d3CK4BWXhG-wJSibuwqFKovTDzMIvvkBacAaFUdQXx-EAZ_x8hVOF2wa-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
عکس جدیدی که ترامپ منتشر کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90170" target="_blank">📅 17:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=fpqXxubn4UVC70vHy7BupMa1_3Bt-AG_Ad9Fp4-LeOtAMPVCwCixn46K1BFR3YVlXgkybhat4dnechEayJnoRpgSmNmVwtYT7c6eROjfND4dqjf5aAI7WCr1PUXTwPBUe5Ij7Nha5n3gYnAJqAFEgmya13IS3rxMm6MO5joweWOQihrL9VlfHIq3Z-bKl0nrqtx5yXi42w2NzQyP0ACWLZI1rmwXGgNfHLdWJbEUJMzuDQwhweKnsjIL6Ih9oKzm8A5Ce6ZiF-71k6TSOinp05vwExn7b7c9yDX23kcfwdQ3oT96QAH-CrL2duMob0TuQu6emS7SVXVfTU4CVpNDew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=fpqXxubn4UVC70vHy7BupMa1_3Bt-AG_Ad9Fp4-LeOtAMPVCwCixn46K1BFR3YVlXgkybhat4dnechEayJnoRpgSmNmVwtYT7c6eROjfND4dqjf5aAI7WCr1PUXTwPBUe5Ij7Nha5n3gYnAJqAFEgmya13IS3rxMm6MO5joweWOQihrL9VlfHIq3Z-bKl0nrqtx5yXi42w2NzQyP0ACWLZI1rmwXGgNfHLdWJbEUJMzuDQwhweKnsjIL6Ih9oKzm8A5Ce6ZiF-71k6TSOinp05vwExn7b7c9yDX23kcfwdQ3oT96QAH-CrL2duMob0TuQu6emS7SVXVfTU4CVpNDew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پادرمیانی همسر ناصر حجازی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/Futball180TV/90169" target="_blank">📅 14:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDinbxyr4yraYmomu0eJKBpR7CsX8N8unQK1A6doKjsJ0egcKTXh_v7gRz-DaRt-mF_3EFJCh5818uuiar9EvhsrrMRdzsX9_N9P6wA6jy90fycjw_t1sf2mALbnjwbaH6M6cRwNn0-CNv_-UAK_pMPcKygS_C3E15i5gz4amlfefNlOfuvcHyQejpjs1pIzi512yhKoMbph0kOBN-6Zj3EmEc4AG2XzPZymgjPCW85JIStl6b4QRhRu_YY6iqocl98LXjvk3U8uMdr90BGrI8RlE4XL0E68UuVmNsw_ROCtHNW0qxJPE97lmFGgHL4kHy3i9WrWQEg0gcXINPwYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو فرناندز به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ پرمیرلیگ انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/90168" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0ve_x5whulE_UnEluNLSG8AT5qWAp0cODIq0xtpZW623OE0e8lPLSG0NnXGivXkATkczlimiNuQTD9uwWWEGYgHXocWeL_7yurZ-8Szgqf9x13fGdQeWODPKUlETDcMbo28vLf6hB00JEcAiQp8wXOUzs_Ip9T_Q2uTY6uMOga_uW-R265IA4qHLYyEMFym4iFH7kaxagm6gmR2HiuCIxNv4Volivc7SPr4QzGrcsKFx7Nh8tPfBQwXZYQ4N-FpS6YKbdt5jD8kHYm9HaP_aKWW44MZMWfam8WwUk620MY0TiycIT6MS9_0DPwrMIPMeQTBEoXXl00wHPdjEKL3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گستون ایدول (روزنامه‌نگار آرژانتینی):
🔻
فکر می‌کنم ۲۰٪ احتمال داره بره آرسنال، ۳۵٪ پاری‌سن‌ژرمن، و ۴۵٪ بارسلونا.
🔻
اگه بارسلونا واقعاً می‌خوادش، باید این رو با یه پیشنهاد قوی ثابت کنه. تنها تیمی که واقعاً قدم برداشته پاری‌سن‌ژرمنه. بهش قول یه حقوق خوب دادن و پول کافی برای مذاکره با اتلتیکو مادرید رو هم دارن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/90167" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90164">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=W1jbb2ZRS4CQ4eWuhGb8JAgNu7VtWuq0VQLR3UKHl4EaD5IIHGHDfflvv0uajnmkIaUC3P67u0ETNdTvmFy1fvWcNV9LGdRy3eA02z5JPQVQfsPDH1XlHtABacvykHDyOf4drn_7ge6CKs4IbfEJhIcVUycFgoOJ2v3cUp6eYSj1BR2W4AlI9aFdRy-tA_TsMlDhInouj8Vx7ZpVoVxakYqEIbMP-LzYeyanlTw76QipDkPaP9SAfD2y-NMG0CHZTY2YpDnFVAKX8de5V0TdG7MYn1MPl4EQmdtK6bGVGdJw-CPrqMilaJZ04OeDwGTz0tKUrgYznd6aQl8aua3NnQueqqbem4vJSBBSmnufJFbZq6dX-n09JeIgkOkgGYJbmZn64V_wpLZDVd580p-WCUwsuXG8gzuvzmU4hA1IcsSHIbEmQcao2Igod5UpMRrAJhwKySSdwS3IqSSWhuxoWlnyc1t86xgmAG7y_0U4LPGioL6YtoCdUHv5kw2xdvDOmuN-_5G8CD9Q0_huldAc4ztocJ8FuyX1rWTIBVasrxFf2WOhYFLjZmHp5eoYkgZo1WlIerNWaSQtiE5z0A25v8MDVWi4hNhjHQz_0ZvR3L3ACP2HKd5gyd_RGFQ9Zg2p5frbQo9mGz8sAITwLeX97h_xTBHzx-oWJtUTZ7YMDm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=W1jbb2ZRS4CQ4eWuhGb8JAgNu7VtWuq0VQLR3UKHl4EaD5IIHGHDfflvv0uajnmkIaUC3P67u0ETNdTvmFy1fvWcNV9LGdRy3eA02z5JPQVQfsPDH1XlHtABacvykHDyOf4drn_7ge6CKs4IbfEJhIcVUycFgoOJ2v3cUp6eYSj1BR2W4AlI9aFdRy-tA_TsMlDhInouj8Vx7ZpVoVxakYqEIbMP-LzYeyanlTw76QipDkPaP9SAfD2y-NMG0CHZTY2YpDnFVAKX8de5V0TdG7MYn1MPl4EQmdtK6bGVGdJw-CPrqMilaJZ04OeDwGTz0tKUrgYznd6aQl8aua3NnQueqqbem4vJSBBSmnufJFbZq6dX-n09JeIgkOkgGYJbmZn64V_wpLZDVd580p-WCUwsuXG8gzuvzmU4hA1IcsSHIbEmQcao2Igod5UpMRrAJhwKySSdwS3IqSSWhuxoWlnyc1t86xgmAG7y_0U4LPGioL6YtoCdUHv5kw2xdvDOmuN-_5G8CD9Q0_huldAc4ztocJ8FuyX1rWTIBVasrxFf2WOhYFLjZmHp5eoYkgZo1WlIerNWaSQtiE5z0A25v8MDVWi4hNhjHQz_0ZvR3L3ACP2HKd5gyd_RGFQ9Zg2p5frbQo9mGz8sAITwLeX97h_xTBHzx-oWJtUTZ7YMDm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
یکی از جذابیت‌های فصل آینده لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/90164" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90163">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
⭕️
شنیده می‌شود کشور آمریکا ویزای مهدی طارمی، احسان حاج‌صفی و شجاع خلیل‌زاده را بدلیل گذراندن خدمت سربازی خود در سپاه صادر نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/Futball180TV/90163" target="_blank">📅 11:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90162">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbhZecxMy1Spq5Vi03Imc1DIKZeq9-Ih1FvxuUBLaYKJcgAFTL7Wi8-dJqKCTrgbgfxzolROBkpoALqgYQ92m7LeuDyOwKRv5s_GqRkzTQgVikrZboV29oXCZcWzsDC1bu3ngQDhGUnOg69QAQiKOYcb9wrFWzRUfxnmFmZCTWIxpf1-SlELt1TMOmugacBertv6e6fRtLn9atlt82eHFUeMMlGEC3qQ9AWXDu6p6PCtJesCUboPuIBVtKiIuUKO3KTFwW26uY1IvzYFIsGuIQOanQ0xoJZvdoxN3Sumhmskcq8S4oIrT8Oh49ffDadVv3NCrXZ4BCXXemZAgM8adg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توخل: این فقط یک مسئله ساختاری برای ایجاد تیمی متوازن است تا پنج بازیکن در پست شماره 10 نداشته باشیم. حتی اگر این تصمیم دردناک باشد، معتقدم که برای تیم ملی انگلیس تصمیم درستی بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/90162" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90159">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=gt4WxqUvv4Rc2pQAnzaWqSXbUcvIZN4AM5uMNozYgU0tWnNZIOEgAq9C-G3EKcMgcitq_Zfam1JKPyKEdqYicKE-nGr-MsFDO6peanGJV0TOFOsCHmT_qs3RoZB4SR-aUXstCQ2YBTK9LqDtNovR9FwTuzfgfM9Ni2MtocsgFB4wxYiyqgeJJcWMqMOuqeIeKsk1I3cPC96W3WUI44k00JvRUJEeyoqa3a5MITY-U7pfodKxbOYthRNceQhGsZF8sLH-f9QdCgf8QSumSIZ2rExzSAmDJ4r71BHhCVPn8VCI9oRPt0bVWJBJdS24onxIME1o8NBCRXmKuZXXzei1qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=gt4WxqUvv4Rc2pQAnzaWqSXbUcvIZN4AM5uMNozYgU0tWnNZIOEgAq9C-G3EKcMgcitq_Zfam1JKPyKEdqYicKE-nGr-MsFDO6peanGJV0TOFOsCHmT_qs3RoZB4SR-aUXstCQ2YBTK9LqDtNovR9FwTuzfgfM9Ni2MtocsgFB4wxYiyqgeJJcWMqMOuqeIeKsk1I3cPC96W3WUI44k00JvRUJEeyoqa3a5MITY-U7pfodKxbOYthRNceQhGsZF8sLH-f9QdCgf8QSumSIZ2rExzSAmDJ4r71BHhCVPn8VCI9oRPt0bVWJBJdS24onxIME1o8NBCRXmKuZXXzei1qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ترامپ در سخرانی امشبش:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/Futball180TV/90159" target="_blank">📅 00:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90158">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKqU_colNKU1bIo28g0azvWZNzGjE-gt9dhJD5e0BmB2S2nOhETX40ktbdRPGoNd1N45wdFHKD1mW16FKMnr2fZq9ifS6eDnj8K0pfiTjMtlZWKM0B6giHeAQ9ht3w7AwzkYoqgl1qAt_SFj7sOT9DTZBIaCEcBOjdUpZgzVc4aY1Uix3GB0VdsIQvKhCyVcudcd58x3ly9AX84RFck_zk-xjVVYMGlIgh_f4fZpZhavOEUOY1FcYhYTkGPq4Jy8J4WnVG-bqqEw1PIRbHLXIMzVhmslfqGRlsZqnZDBuPR8WR_bA1yrHmPXMeM01DjdfZEFpED7FSX0vmUZB-iOjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کریمی خطاب به شاهین نجفی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90158" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90154">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YrGccBHbp2Hh-33YAaiabK5p-aalrRZo6ovN-exGC_l1NCtR0xs0EOKAGv9UvP5phoRpceZCJIidqb4yUgsn8eiyr7xi-SE3RKfXIJPA-77NMBLrtHhUQUTYUfywwSlOmRMcKu91smSyInhP5ye51ZMuQuZ27P4yc7pCml9zg3239OIg756q0vdj-R-YC1V5cvpiqDaZzW-yMt10zOIVDeigLnMv-DM3tzhxBut0Vrt4-G18i2CDhs71FOP9B2AsjfHSB-wzPe_8I6DkCFrX0I8ZM_jn3UGCnCh004igUufDKl9Z2ZbQHtFgL9Vp_rgClNTRAHgaakqad8CRkBcSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5qHOmjbuQ6f2vqZ0P4i8nb8d6hOoWH3Wp2bi5e_5jxze-w7N6ThheVvEOUwnCNgcJb90tbfUGCromWlDnm00P-ry83vtcdSAafrljlrttCYE3UZiAtm6jhhA8_HfTiTreYj6-Rg1i3VU6WI8xWQwPaQA8Gch4bkq52w63Bn4p7PDzJzetmJz0VrB69c2s5upD8xd7kndD4cIeurO7Mdnyi7M8cV-dmq_rHphQ_-rISbaKxCF2wywSI84q-T37QceQlom50YTmlQDR2rcLRMZut_8bpqgPI0FDvsDwDN7qSPZZJGMy4ONlrA1HEiqyjSFkMOt0kTxu4tJWkIOb8dgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EgnXDSgvUSfokz68fWxbB3FEQcOAEhnM2_Hm04UIHZMWxuedWVPMD-qFGiormIcU_hNXvLEDk8rjflCfQAFasRoODpcc522L2YXjFHtiqTKfS6Ugc4vx9TSer0ZLr9ALVzPca53nmeQh6F8gJxiDfKraJuBf2yEub0pygywwoL9gC8Dvadqsd6DOhWtdVE_tqMYm3H5qJDOZbK3bOwfJSQr51UfZl3NKlrrDcptwI8eZH0O-6pAmzEhTU8MHFdoBNAjb8HS6XGaFE1zPs4roXF_q_UvuX8JQOWKW57_EXcnoRwNXghanDisBUFUELbkJ2Yc9lz_4k88iDfdsSyldXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عناوین برتر سری آ تو فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/90154" target="_blank">📅 20:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90151">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
العربی الجدید به نقل از منبعی در وزارت خارجه پاکستان: واشنگتن و تهران انعطاف کافی در پرونده‌های اصلی از خود نشان نمی‌دهند/ سفر فرمانده ارتش (پاکستان) به تهران ممکن است آخرین تلاش برای جلوگیری از بازگشت منطقه به جنگ باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90151" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90150">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPqqmUjXUxd_Cecajy25Ub24hbOzPvV2D5a820FFnyrYMjKa1yVpPidboUA7TQ48R0rLk6eO49e37weR6kPEiplNXEZhwOHbaqLSFv5j2QEw-xNIdDEcqHW4qzP2AuryUpnzEI5ZJQAAaVRmNfm382EOxkiOwsspKo5VtgtGCep-X5QcIt418F2dNxPIFShfirSkE0W1vv5tLRhalTQdEWVlVzhDiBq8NyyLbxWkTH_AGYaVckDNCt3wimiyXRn-Ah30LTVsX7qpGg_OKQL68eTmPXDUVHop-VNwXjS-nwYG88MJSjriq2xlBpRArq_gGvZZAs4PUSMA6y5FwGZe5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ کیت اصلی بارسلونا برای فصل آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/90150" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🔵
باشگاه استقلال مذاکرات مثبتی با آلومینیوم اراک برای جذب محمد خلیفه سنگربان جوان این تیم انجام داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/90148" target="_blank">📅 17:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oC7_fjJ5eOVn3s-lpZsILIGt3AVCzWooGrUvVDJFSUqhDzJZNWtj6_NQQElXGICb1oHbz_yPJ6Xj_c1RP_9zViWSBNm25VayM-zcpjZFhsGlcK0J6BW92A1tt8iJzL_Dn7pzMHHFqNZRzAge36ktPFw1rmv7H4vMIORoPrLobOKH5LgfpiKCTWaa_hbHyY063MoRSv6Krn_II-uOy9V2ka1PCgRAfFLaE7MSIyWPCmXE7Li9RnjctbqRGOMqy2oBCUXzWiEdyNck983OdOk-Up3i86i0Pb74usU30iSpOrIrSmIa_urlYzGtk4nqiOT3j98fm8jnyEK_vhkWXxjbBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب‌منتخب بازیکنان خط‌خورده انگلیس از فهرست توخل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/Futball180TV/90147" target="_blank">📅 14:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90146">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6PiBbuERCK3ekf0Nm5f9B-Zju7LMJEP22NqILsUjTHCq7HVK5npNJq-m9bc-fbCDWmQSVMIcfDBJOelMfahgJkf9t-cmoK0RjuJNI1CbiSEcRTMUbjBEyP4WIfxIX0hLqX5UwQG_usPTOTw61o4o3iIONHn8MN8mMGFeYtUy3YhGh_JUj0XCXeFChuOr_jVCNwBwCO28Y6t6dt9hY75S-u05mthmiw970MCtSxxhhWwhmr08o-FukyxDOFJhj_jPolTbrfDrvR0bN0ERDtPbUzNO4G5dbemm0SwTFY9-ttS3ystBDEtexbtYgDlaCy3nale23hbI8Y-j133g2xWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی دوساله رسما سرمربی دائم منچستریونایتد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/90146" target="_blank">📅 14:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AibFSr2LWnnBoHIweE1OMBWuATn-n92m3sNA88HiseelS6EqKbF-YK9hCHYQvNNnEe7H-qK3VqAX2Nm0YKAuwf44Dj-QDBG2EGW9-cWGO0cfnApNDuFkm4qH3g-PSRrFC2_koSCpliztnq8A-4e9YyqfpPxWXBVJlNPpJf5WLY5tb41R35OgTaCl86wfp9EtfMw3ARVMtoZdqWKeaZtsFn7Gm9gKp5AEgjImd4Gg8IhiuzEK_xts2AyWVQrqDvgntB-tQUsxW5FD0a0dPA906RVZzcrAjpRXoFawkM7SpEGapQMFa0PtWJecl4EdH8M2E6k_rCY6RTGr_SvEQonHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ پپ‌گواردیولا از سیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/90145" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90142" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFwyhrfefDyzLAYXDmUHjujuKySlPEuAqV1yb-laMhVhtutZoiH5XMfSqejNjWlZtpm0_UqZJLGupyhMHD6eKT19ie2LMfR2uhFMj4WVXzFuJbxjxosYeD0nDBYUHLRbApH5jt30GMycCUp4SsUm1_pGA5XKzaQjKh0bHF45-COWQ5f3oI3FtfutwktqFW2l7MecqqTvKYr-dVR0FMhV5OEvut69VI_0nB7N2qYSk9TfuaMrWZ4JoxYCPZ_ullEXQsVHSPywqIQuHDZCrqT9jZ00VeDIoUa8n4-f_56jHwzl_darVoPZPn3S9cMMeshX-aJMQ7uogyLBkPcokVADcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/Futball180TV/90141" target="_blank">📅 12:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90140">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇪🇸
آربلوا: با عشق و احترام فراوان،‌ فرداشب پس از بازی رئال‌مادرید را ترک‌ خواهم کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/90140" target="_blank">📅 12:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🟡
باشگاه سپاهان با انتشار اطلاعیه‌ای با کنایه فراوان به سایر تیم‌ها، عدم صدور مجوز حرفه‌ای خود را تایید کرد و بدین‌ترتیب باید شاهد تیم جایگزین برای طلایی‌پوشان در آسیا باشیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90139" target="_blank">📅 12:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/90138" target="_blank">📅 12:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90137">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAG2FqJ79sivJT3_OwTpUDlPzWJ7Q2pS0os6FPPIvXTgW4nLXE4PvsFsrh3JuF7Ip_p5wAzB91z_Tmj2bavJ41KcDK7RbZCeUPUpZKFjj_VI3vzKDim6IEWh30yMrg3po7w49j3GbhcuqoJsGETHS66IK6Mqej1VbPg_T_A_bgJGOMs1znFTCxzQrUZChFURfHBFuswD_z-SVzvILsXFqy037oGzmIupJutgzOUR6urztqJ_h2KAkt2_crvTzFfN0bDWwg0KvL8fOK2b_uP3_mbnq0aeITgTzaYuICduUciGdtMu96N2dlOF5tffgvBtYO8-HR6iMlkFVC6wmlkNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کیت‌اول تیم‌فوتبال میلان برای فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90137" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90136">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/90136" target="_blank">📅 11:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90135">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyy_-eMs_uOqpf6lybYDhFwr3Aq0pSn1sI5FOMKr7yVYIazLEDuk-wJLnNcu7i4IDRxnFSCfCuXIeFtFCN65m0ju6Jmg4NLvtY_NMNoYuECUAVAbWniybFWmDSGBUvFbp-57JMP29WFzgHzdCnpi6qidI5a0MHmLmT3eNGRQxxEb9ARW2DZ7SGFvVx7WFJzVdVJMNsWBWEiSj9Oo77Qsope0IFEW00GZKiDlkR0DLm6JkCLnIJ6Jz5gcyldoU7z_BMYQGEPUY84yAguE8y6kP0iWehkRZNY4gxjiQGuifoZgLDIhLLsTTvFuidM-hKBVXcVK5NQ6UWA_tdVhBYtFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آرنولد ستاره خط دفاعی رئال‌مادرید از لیست انگلیس برای جام‌جهانی خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/Futball180TV/90135" target="_blank">📅 10:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90134">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3IuGI94s3OaS6pvWDUVmoiJl0W8GUfnWzabDYjlsqpQUW9DzDicscrCR28crNKZk_3iIbYp0v7SYXZ3NHRDac-89vsa2pcAKaeTfc8ViNUm2gv3pJVv8VL-A5K286SmE1w2t9yDil1DxPSNn6Gebxg5pnRcYGd7f1coYZ7KliSSIT1UO1eqMrQ5_sRcSRllcF3bHUVHsyyl3Cv03XI1uFHVCFH700KBjIfDzIN44IW2Txs7a8xCxDEpcc3r_zNIx1rWenkgIYW7JIQWPHYuqChkT2cmhpk8rn-5F9xjWE5m2uDGoRuuht4K9xZk5X9NzVf2n1AidyHWnFiRKyU4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه بازارهای کشور در اردیبهشت ماه:
دلار ۱۸%+
💵
طلا ۱۱%+
🥇
بورس ۱.۷%+
📊
مسکن ۱۷%+
🏠
خودروی داخلی ۴۵%+
🚗
خودروی خارجی ۲۲%+
🚘
بیت کوین ۱%+ دلاری
🪙
اوراق بدهی ۳.۳%+
📜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/90134" target="_blank">📅 10:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90130">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=B6ocDl4dOdj6zw9Ey4TL6c1Jv7d3ourKx30ludhCn0wSSn9nO318OGHb7KUjETP1np6In2GvVR04u4uW4dbefhm4A_eShXZy7pNG5H2qb35eZ87XYF0BrLaE89FvYgedXCk4SXeGHOwoL7DQuYSYmJhYsu5xNaZ-q9j-F56vgzkBzpNrhIFmda_sVcgGj0tjAzJG_YMwp001Xd3ISDB5mG80Rl4eiDLwDzfPd-B3LRbOdR6gleQPYMtsz-_W1eYUKcfxYDGZRIbx3pW_oWcZRX1LhDcwstiy1i-GRZz8jVM1l_pK7PpfQsPXXgI3NSTaGXQOKJFV--01W90XR31tmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=B6ocDl4dOdj6zw9Ey4TL6c1Jv7d3ourKx30ludhCn0wSSn9nO318OGHb7KUjETP1np6In2GvVR04u4uW4dbefhm4A_eShXZy7pNG5H2qb35eZ87XYF0BrLaE89FvYgedXCk4SXeGHOwoL7DQuYSYmJhYsu5xNaZ-q9j-F56vgzkBzpNrhIFmda_sVcgGj0tjAzJG_YMwp001Xd3ISDB5mG80Rl4eiDLwDzfPd-B3LRbOdR6gleQPYMtsz-_W1eYUKcfxYDGZRIbx3pW_oWcZRX1LhDcwstiy1i-GRZz8jVM1l_pK7PpfQsPXXgI3NSTaGXQOKJFV--01W90XR31tmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فوق‌العاده رونالدو پس از قهرمانی در عربستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/90130" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqvehliXk_bKghOivjnzevT070x6DB4ZsRKE2DQBODT_JHFcJyfNnD3fuqQN7elO5prpUUvTDUhJ3v9nTfYTHk4VPeFifa6SG38lb-Og3aUOuY81GWcYtyP9t6stNAow1hFxlGzRN7aMwNxxTvqRMdEB_KC2p9-SSvbXDb0Qg66eVpVMgtWwVT-gQ35Y_ykj-u_JvsMyikN89ovQA_YpB4zTibek0KoTn_Qm8urFp-nKEypKRdsud3uothFNQE07QWIwkxRAD6fT-9o2i_pW01deeGxrrkQfvca4cLuXx-fKnYUEjbEydl_gcMFWPSe3zhfOr75n1OJr6Uh9dDpMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
النصر قهرمان لیگ‌عربستان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/Futball180TV/90129" target="_blank">📅 23:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90128">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIbDcO7tm7oFJzElywOCQfGmLtc5bLR7ISmi9z3f_guSuGWnIl-lu1vGHSaG1bEafNiW0YWYbZSNY_XQvjuU6eA6-w2EinwPzHOpbOVuCxk75lm9uOL97mdqjZqq-hzjLKtYB8svSYkkshGG_Tf_L2GVcC4UhbsMBe9iWJUYS5Waxo0cuknTE2GGit0l79fEyN3DoSNLPIKZktaKrl3ANfg0N5SrfS12gDobBJqdT8PrEm-g1SBWczMrDChmQe8V3N3TR2xzQC1r7FAfw1W8jdp8DGNYF6cbvnS6dZR0w-FTg-Ft3l3dJpjCzR1TQOwEpX5e-FbQ8D9Scv2pRtp0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیم گل کریس‌رونالدو به جورجینا همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/Futball180TV/90128" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90127">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=Y8xsAy4WHfBmjTG-KteYP8Qsn2rBaSrqtT0loJIwyC1csoNuudbXjCcFiOscsb25CrE2AGedFVBqGAzWEOHSlBhaH4dBB1vhlbiWgJKbOc2Vk4oj6VN3M9Krt0ZuwBMcRqBeet3iNsG-1sYfwSYm3foBDpaIZjl7QVILujXtJn1wAGKlF4oJOEmCWA5A8CLkEiHe4uamO-JQCZ5C7KNRBgl2B2cdqsy1bNZ_Kdi_ALIfHBmfqhI9Fzn4uOGWFj20wd30sZSypYH1LgMi_YPwElHiSO4pjwWF_5bQDsCDmghgu4YryPibY4CeMMre1AseMTHj1-CtosTaVR-84XFNep0U3tNjElcXXvJZJGxGMY4G1POz1gT5qF6Wnl2JQ1s-zq4gENbc0Uxw02q61VMhvJy-m-OH3E-fJOTWzEBHyjZIkO3otqLBADZQwUJuSu9nZMxBe9KEktjiLlUmR2oLasEsWhyRpze2rsiZyyzOn5isVkelTz56vb_Tvgs6_GPzeRBfmJE_R6o1A8NR4RI6kJTa36VS4ki2NOS0VpQ9n52nriOA8PB06m77U_N1BvDlaWVUY0X9a1UROmgzK9jBf5xkEsytOA4mkcm3ab6g1O5og1QrRBOdTDuuLUZSZ1q-8BIrEtxOq9QrPbX9Xmn1SzJH9s79lSnWH6D5m-YPxlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=Y8xsAy4WHfBmjTG-KteYP8Qsn2rBaSrqtT0loJIwyC1csoNuudbXjCcFiOscsb25CrE2AGedFVBqGAzWEOHSlBhaH4dBB1vhlbiWgJKbOc2Vk4oj6VN3M9Krt0ZuwBMcRqBeet3iNsG-1sYfwSYm3foBDpaIZjl7QVILujXtJn1wAGKlF4oJOEmCWA5A8CLkEiHe4uamO-JQCZ5C7KNRBgl2B2cdqsy1bNZ_Kdi_ALIfHBmfqhI9Fzn4uOGWFj20wd30sZSypYH1LgMi_YPwElHiSO4pjwWF_5bQDsCDmghgu4YryPibY4CeMMre1AseMTHj1-CtosTaVR-84XFNep0U3tNjElcXXvJZJGxGMY4G1POz1gT5qF6Wnl2JQ1s-zq4gENbc0Uxw02q61VMhvJy-m-OH3E-fJOTWzEBHyjZIkO3otqLBADZQwUJuSu9nZMxBe9KEktjiLlUmR2oLasEsWhyRpze2rsiZyyzOn5isVkelTz56vb_Tvgs6_GPzeRBfmJE_R6o1A8NR4RI6kJTa36VS4ki2NOS0VpQ9n52nriOA8PB06m77U_N1BvDlaWVUY0X9a1UROmgzK9jBf5xkEsytOA4mkcm3ab6g1O5og1QrRBOdTDuuLUZSZ1q-8BIrEtxOq9QrPbX9Xmn1SzJH9s79lSnWH6D5m-YPxlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل رونالدو در دیدار امشب النصر مقابل ضمک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/90127" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90126">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=e6MY2vMo9ujfmvEJRUg25AqjSIDAIQGmbU6Ygd2sosTpdI2wA4kDb6zKJ1eQK7yo8uIc_SjiM42Qb_9NEtNbnE6wgMCmc9IWyiZyxai_6E9K-lzI7MjhTswDxM54DE0vpWgn24pjULy7Zx0EljEXKv6MnRqvqdXklowqffL4CiQYOL_tNqzD1qSwXUtrZmT-NyrpBoamfmJQRjMsXpuBGbSuQlvH69sTjuJ59nCGgKRdMTkQs9eQuAps4-hV38OqeQ-6-W5o41kA2KtEfkOKTsgUVvIiPl6zpFpvHkBDOucYZL4gNQ-DEdBA5qf1-BYeHzMiFC_IVYE8Iq_fNNep6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=e6MY2vMo9ujfmvEJRUg25AqjSIDAIQGmbU6Ygd2sosTpdI2wA4kDb6zKJ1eQK7yo8uIc_SjiM42Qb_9NEtNbnE6wgMCmc9IWyiZyxai_6E9K-lzI7MjhTswDxM54DE0vpWgn24pjULy7Zx0EljEXKv6MnRqvqdXklowqffL4CiQYOL_tNqzD1qSwXUtrZmT-NyrpBoamfmJQRjMsXpuBGbSuQlvH69sTjuJ59nCGgKRdMTkQs9eQuAps4-hV38OqeQ-6-W5o41kA2KtEfkOKTsgUVvIiPl6zpFpvHkBDOucYZL4gNQ-DEdBA5qf1-BYeHzMiFC_IVYE8Iq_fNNep6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرگل کریس‌رونالدو برای النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/Futball180TV/90126" target="_blank">📅 22:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90125">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnAlu6Kz1OZWSCHdY0WvaBWbYAX_whb7CfmS2I3dzDBk6kFgdFcfAfBoiuCKK-SExNA41pmXorgJ6C2oEbAhj4zRJdoy_GqpYYtvq-BEQxPfNvGJvglMZmxMD17udJDY3EA5JnqUGxx4PUOkLZRksqiKm61pENteddLgaEXjJII-WyRESvqfysw6suJSsQxsJlAiQO0aKMc7Fj-eQ6k2gy0BCIRdS3BgZzrtWEuWx3E7tla8t7PWVt2ve_aqx1lZhquI-F8Xc79pghrjnBbtSU-VoPgcS6mfDxi8K7b6ZqGrrnNrqfvoqYaii9pTRzT8s8bbfzgb3dAoxGusnzAmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
فیفا قصد داره جام جهانی ۲۰۳۰ را با ۶۶ کشور برگزار بکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/90125" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90124">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsPxHoZHNz1F0buPgQbRV-zVB1g9bSTR-HmkJQLpV6fwDUu_RP1-TGnp-YL1HvktV_DeWjHj5RnHfB7R2lzqi5lJctzOYsG6K0ImuUWPPU86jmxHPqoM_HmkofOx83H1IeL98jt9FeP8Zl60JGHIb_DaJ_g7gKGVtfTzJ0wzc1TJnyjsKOPO4TEx0IInSWvropCUHW_bzx2pZuugPhm-UotdBVlYrGwZQ-J_Spa3SYzw3E4dWFrmmn4zA0zxywzyJTlxn10XYpOGZaslmQvAoMJJMjSrTMfruHYk6C6A6l9gWFQEoNXn93q3JnDaGezeOrLCVZLt2ANCCMAxoCch5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوس‌دخترهای لامین‌یامال در سه سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/Futball180TV/90124" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90121">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFkPzTQfz6frV4qm2RcqGRQA5vwES2BGD4nM8UVnn9VI-aCtBN2vaqudxigkVguI4gg2U5diaFFAlKdPKBVFHi4p4hLEpf6n5hBo_an8Df_gp5EbgE7UomlXZ_lSk4LWUJGKQLqaNurYeG-f7kCPYRFQ1WX3yp7p9TcfrvO_qrfG-ZDu_FO3jqyInPc2akmnozAbcN4ebAS5XEUHieTsQAtvWu7jG6OUumX48HO7qYcPGeSZtgwRffO11hqwy02V8nwFhzjDx0G9fCI8C3MsIWh79NbNphVgz-Z36KNyCTWBGPImTLBO5FxMffSt38LJ94wwf90mj9PL6-UMjCCh_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
لیست آلمان برای جام‌جهانی اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/90121" target="_blank">📅 18:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90120">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvKZR67ENSgCyq8UPTE3N-iMOakAQXZ6X1cMNanBFJ-6pPsd6ITKZ6lFYaKDrez1E7p1OIa1xVKXfKflmB4CD1mHMvTH7wgHWi7wU07hviMKLF-WSB5xv39pO1JKUY7347xalbbCmFcVhUEnKJO-wbqGMzacc-lq0BdvduuUy64SdwYRZVP3wntif0OQCJrXr9IftL6x5J-xKrIf0dWJoxRqJKJ_fXC0v-raevCoA6bgK4H2ZcB-M1JFbBY9TmjoQD9nmh9p5luELlcWe2yticzZOWZSXSoK2N7Arv4_ibaQFNfqjkLV-6V8Ookyvpi3DOZ_3GudTd_8Fkcq4R4pCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آرتتا به مانند آرسن‌ونگر‌ پس از سه فصل نایب قهرمانی، بالاخره موفق به فتح پریمیرلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/90120" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90119">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNIOBLwL10YFzyLJY5xHySRzMHFhXrPQtar_5-N_U3pVPQ0YxbLpxLc9CPhj0VgT4PbjpkDjOsPu46EiIfh2y58cwFkJcKi-rpiBxFf0d6ka2O3vjtZZUpuLcJDboJO3bY99IdmkTPqII_1kRw1EKZEjGmXtGaWLWNZRg82IdE3vV2Cp3tI-X9-aq0-a3sh-m2FoA5gJ2S3-s1b8TNa7iV3mfgwgXHauCg0y1WwGZwJtYEZqZWM1OB_tc0Cj-_T7Nleo4g3OqdDoZ9JzETpKSYr0IF-15PLwGX0KSsbk1LMLfOhIckmnPDd2bSJ2Y76E84d_IHmh39D7uhZJsshJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی جمهوری چک برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/90119" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90118">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90118" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/90118" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90117">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INYXR8komlbLPWh2kaxkeyNJVUPAuJVkl9otj5AeJxwAG2lvLuuDqwQgeLhS6fDMmlNORYijLy0cqrUQhBorltBV-r056GCsMs8lRFY9fOmMkIPnJ1PGuUhTDEP3mRan6LEQlIhnVlQa6mN7ym2Qij3VNSlVc-A2_Hv0AbCKJ2OnmSSADlYueLH8YPMhNKv7MrpP_EVeIfJJiJuwQltCmK6tQCbglf8TQIa206TpWc8t1XrahsOZ9M0K091c7i0o_uiDzO8ZXgDVni3eHQSbAYImJC1reO3kLuKnJP1fP9skZZclWV-CRbbyApjDy9vCL_l66pOngpZhHMMYNnMnWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/Futball180TV/90117" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90116">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
فرمانده ارتش پاکستان، عاصم منیر دقایقی پیش وارد تهران شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/Futball180TV/90116" target="_blank">📅 12:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90115">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfrcZDh8LEgBYy1svwSczWqEg-syGwLanSZsI0XTTmsrFM7xQT3ahQK5RbXPkqZJe-32GSy_w1ukI0x115VGxz04Id5hR-dj_lgacWoiQm4lY_6xKukEb_83CTlZA_SnkcTF-SXAp9uWw6cHRFkTPQ8dx3DdXBBk-89-KhNY-HChaBa0Q-_jd8mNWg1rzTxVB8ax25NffacxbpH4D8CnUlLHAXoufOmp2kg89zZdMM4PDYbuqiS-i3Q1zwumt0zs1ojVrLRXSoLDu8hcIyGI1GlWSnNu5Ks8CDnL0XfIqBpaeCgevrAC2n3z5duERwvYKeJUO4Ja8G8A7vFBXXyulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه کریر فوتبالی لیونل‌مسی و رونالدو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/90115" target="_blank">📅 08:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90112">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUzpjR_dZL1vwQVclFWrZejpwUuzp845aDHMHb65HKvtUbB9fKZuwtvNRlDhnlVmlP5Y_Luvh5RkvuAEPtPhrT03lxQkGwo3forGgb2sBQFutNcgLkSlFHYyiAmFFOVbMIGmhjUZw60-DxnCHjQeUjI0wqEjBRiQXWsRVtJiyU_9odQ8K3PIaTB7PtWwhUfq0jzB-ygzsZSCk_a6FlPCBw3et46hk-9YFJfqgbR1-O0FpFg0M3ZSzIvpnBSKQ0lN0DccyCtFQrCQqNgrgrYWQPL6pL7OY1RcxOZUmjehoaZR5Q3Ih2wQhHPpBWiqjR7zDSZ5EbpOIVabExfjdV7hzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل فرایبورگ قهرمانی لیگ‌اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/Futball180TV/90112" target="_blank">📅 00:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90111">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
👤
برخلاف اخبار منتشر شده، سردار آزمون بزودی قراردادش با شباب الاهلی تمدید می‌شود و‌ این بازیکن قصدی برای حضور در ایران ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/Futball180TV/90111" target="_blank">📅 00:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90110">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
ترامپ: منتظر پاسخ مناسبی از ایران هستیم تا از تشدید بیشتر جلوگیری کنیم.
چند روزی منتظر پاسخ ایران خواهیم ماند.
تا زمانی که به توافق نرسیم، هیچ تحریمی را از ایران برنمی‌دارم.
در ایران افراد باهوش و بااستعدادی وجود دارند و امیدواریم معامله‌ای خوب برای هر دو طرف انجام دهند.
اگر پاسخ‌های ۱۰۰٪ صحیح از ایران دریافت کنیم، زمان، تلاش و جان‌های زیادی را صرفه‌جویی خواهیم کرد.
امور ممکن است خیلی سریع پیش برود یا چند روز طول بکشد، اما ممکن است خیلی سریع هم به پایان برسد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/Futball180TV/90110" target="_blank">📅 22:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90109">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqwYvRllk22j8uWVLMsD4X6rnDqCQo9T5R5CwQce_AZ_UtS8KglkR3KgXnwtvV6MDfDl_4nJuS_G6YIpxxaQnh5X-PrsJ-GTOiUxqNq3XplGQ9kxJpY48NQBjAF5x3eP3LSYojHvlMHyol7WJFWFkIRuuU7sNy0ZmfS2ivB0LHfugqAzmUfWc1JgToDLAVBOoOSTDki61Q9IVEE9ZUPX2-WrcmvVnuf3-s1FxBbGOtu-j4P9hjUWaLNU3lSYtE-PdS3c8Q87q3HmIx0f6WltWL9ABW5PPShYDoX5ILdQBpM8toEufoDw_3LHYo8w-LNQ41AJavZ51PIP-2uphEySOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون: ایران هویت، قلب و افتخار من است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/Futball180TV/90109" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90108">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🔵
مجوز حرفه‌ای باشگاه استقلال برای حضور در لیگ‌نخبگان آسیا صادر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/Futball180TV/90108" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90107">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZaLCLv5TdQa4MTioRZy2Doows-ErJZWoHLTtZMTIU5ObA10Dmc1gbILdsVV2OC--42oLXwvM3-k3BKrpKWEEyg899DurIho-9T-lNZOt-kKfC5dh8FWvLNYXAzoRoSjilaDlQ_ogHzaNdeM-3ZccgIFeiiLRpO8W6q-JSDQCyWQ7jzDfB7u8WkmmM2Nn3EZd__LWk2hXz904MOWgMNM01kSg4FjUk1PZn9628ra1Exe9a_kYxatVlcEu87mVgQPpgUw7bHDp0cNpQIIZAGnRQxqjxg6JB4vuTTpkuDJYA7c5MLtnoiY7Zr9dszGeQ0HHiSHsauIp4gk9sqIq6gLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید کریستیانو کریستیانو؛
همان شور و افتخار همیشگی؛ بیایید همه چیز را برای پرتغال ارائه دهیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/90107" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90104">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=NFjDGBpQilTZTK9eVhcV7uLKRg8NmfkkoQWz-o7Gpfunud3GTPS-X_yipRzXWiL8gMJoEXXsNxw4xYdNzmB8oKjkZ7qF-8neZrf-KBrIMBCZW3KdJfPHhLXbFiwYnouGIVOt_TuiDAosU9yz8nG4QWe8Tle1GlyPGB6eXFqMDX1JYaXOUEthAiWs2x7_wp99CKW56MpCxHxpeTVc7Q75TUVbJTKVSUcBoo4KZPjoV2IuQ6tNouJT4fgBKowxSU_Im6q8r4fHYDuWwrkD8hM5H02kFlTapz19Vy-Suc0TNfTopqflCft_HH_OrkY8rDFvdJpoA00DfWveauPNNiqWxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=NFjDGBpQilTZTK9eVhcV7uLKRg8NmfkkoQWz-o7Gpfunud3GTPS-X_yipRzXWiL8gMJoEXXsNxw4xYdNzmB8oKjkZ7qF-8neZrf-KBrIMBCZW3KdJfPHhLXbFiwYnouGIVOt_TuiDAosU9yz8nG4QWe8Tle1GlyPGB6eXFqMDX1JYaXOUEthAiWs2x7_wp99CKW56MpCxHxpeTVc7Q75TUVbJTKVSUcBoo4KZPjoV2IuQ6tNouJT4fgBKowxSU_Im6q8r4fHYDuWwrkD8hM5H02kFlTapz19Vy-Suc0TNfTopqflCft_HH_OrkY8rDFvdJpoA00DfWveauPNNiqWxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
ترامپ : الان تو اسرائیل ۹۹٪ طرفدار دارم. می‌تونم برای نخست‌وزیری کاندید شم، شاید بعد این ماجرا برم اسرائیل واسه نخست‌وزیری
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/90104" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90103">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=KvqZxmL3EZz-6Q4H83o6VZGrJt3wtL8QCET_8e0M1AXZOWo2Q2sM5HCDWzLk_vl-TDqRT3gPzEDFTR0sbmnCWsaFQ6R083YuA-627270RL_ZHWHslcFeL0q9OflxsCVIVTmIBmj-bIg0nyVAZzhdDv5UZzK4DBDX9WPKQ9meqqtqbaalCj9SAxoDSskh7iZq9rvpFRGG0w5MCL3Y406dWfhMmpxNYAP32GzgDv2SQBgBnrIUhCDS6cv1F0f5jvXyD12a0eHkRTQApqx1kljUXH8T9YAEKpiqr1r_GQnu_MDC9iySvaA0qMmE0uY0YcEyGK3V4balVX0xgTAmI80_OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=KvqZxmL3EZz-6Q4H83o6VZGrJt3wtL8QCET_8e0M1AXZOWo2Q2sM5HCDWzLk_vl-TDqRT3gPzEDFTR0sbmnCWsaFQ6R083YuA-627270RL_ZHWHslcFeL0q9OflxsCVIVTmIBmj-bIg0nyVAZzhdDv5UZzK4DBDX9WPKQ9meqqtqbaalCj9SAxoDSskh7iZq9rvpFRGG0w5MCL3Y406dWfhMmpxNYAP32GzgDv2SQBgBnrIUhCDS6cv1F0f5jvXyD12a0eHkRTQApqx1kljUXH8T9YAEKpiqr1r_GQnu_MDC9iySvaA0qMmE0uY0YcEyGK3V4balVX0xgTAmI80_OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدایی رسمی برناردو سیلوا از منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/90103" target="_blank">📅 17:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90102">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/252c545abf.mp4?token=SESllf9JNKbAfv_KkBKO279cR4-101mnAaY1jUGWZQqZd57mjGjZuAOwgkQQ4242ZAXecnjaXtfby0pYSiygQ-Zy6HoZlsCQ2OQXiDQE-YfuIz5vAYU03aJ0OkqhyUsRLa0L7C1YgYKxeZ65hITTu-WxHdLSyhvgW0ucBchtsAso18ldf-uvExhKzXh4A8EtcrjdQI-O7ksIyiOg3_I5-xrFRVE8Atzf1y4WMvWERdS_1_oPp08XwaK9Wvm9MieAjBhOPaL013lGXGvkqRnn4-KWF4NMM4VOnsjbcCp3ey3i3LKOnaouDn8LqJKKfGiW4EuaB43N_LMOQEF8n3TUcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/252c545abf.mp4?token=SESllf9JNKbAfv_KkBKO279cR4-101mnAaY1jUGWZQqZd57mjGjZuAOwgkQQ4242ZAXecnjaXtfby0pYSiygQ-Zy6HoZlsCQ2OQXiDQE-YfuIz5vAYU03aJ0OkqhyUsRLa0L7C1YgYKxeZ65hITTu-WxHdLSyhvgW0ucBchtsAso18ldf-uvExhKzXh4A8EtcrjdQI-O7ksIyiOg3_I5-xrFRVE8Atzf1y4WMvWERdS_1_oPp08XwaK9Wvm9MieAjBhOPaL013lGXGvkqRnn4-KWF4NMM4VOnsjbcCp3ey3i3LKOnaouDn8LqJKKfGiW4EuaB43N_LMOQEF8n3TUcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا شبکه‌اجتماعی غیر معتبر روسی با این ویدیو مدعی زنده بودن علی خامنه‌ای شدند و گفتند که به این کشور پناهنده شده :)
❌
سطح اعتبار این ویدیو : 0
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/Futball180TV/90102" target="_blank">📅 17:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90101">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
⭕️
⭕️
🇪🇺
تمام باشگاه‌های لیگ‌برتر ایران بجز پرسپولیس و گل‌گهر سیرجان با ارسال نامه‌ای به مراجع مرتبط خواستار لغو ادامه مسابقات لیگ‌برتر و مشخص شدن تکلیف نهایی تیم قهرمان و سهمیه‌های احتمالی شدند
🔵
این تیم‌ها با عنوان کردن مشکلات مالی و ...، موافقت خود را با قهرمانی این‌فصل استقلال اعلام کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/90101" target="_blank">📅 16:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuL3fBeUrGVQWbNaTWaUw0KRTZp1YX72SRXpBdUzP0fcay7p4ApdYKWJgnVGf2SAiUY3HB4PpP6mjjCz_FrfxTb1Sc4SKURC4LKi7FJpFVy0VtgLJLNKlCi6Oh0ioFRG5K43dyfY5rcoPtXht4ka0xZn-mc_24H70ahAlKY03Esnb7rzqEqQGnK6NWq4qCprfNA8H2Ae1hgljmkW4A0LXcNeJ81upCZqMFbagn0BIJbmvCmM-BeFZlIhgW7b0pJZ4mDZVyt5eqNxg51O1m8si57pylaN8WYVs91tztMu87eqWm4JXTCijdIBLAWojmdoSpmpcy-dITy1sZ2G0BKeyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6pLXQkLGgFdi_X2r50oEACIESFtmVEJ3qgoOOJRbWhhMGBJkxqotEIgID2dPCaN0BLsA7isNdYpT72bM5HaTmJ_qhmLWGS32gpXDbF6CATNyGmhwBdgzpCxxuB4jse4iyiJUuA9z8AtK765f3qtUM-qaaejwHede7tj_JK387ENhlRIo3fg58dNwiJXZcL44DQwGKHodSV5LI8JgLcJgTv-NQX-r7XI2TymZY0IuTVWl5ae7xEUjTh0xkJt9BV1jP8qZCTAvuLgmaMQr4WP4eauA3DGVgprW-xCDM4p6lffp3YWY8p6vrCISo0ItlD9R3TLHw8lebuJYZmZexSNEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینس گارسیا بلاگر ۲۱ ساله اسپانیایی و دوست دختر جدید لامین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/Futball180TV/90099" target="_blank">📅 14:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
⭕️
رشید مظاهری سنگربان شریف سابق فوتبال ایران در حین خروج از کشور در فرودگاه بازداشت شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/90098" target="_blank">📅 14:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=j8waNVK-wjf598DQ_GLmkXBiV-S4RSCiAF7JQ2yAJz49hOyr_tt4A1bMcl3fBGENIrAuCv7PuvDMZTz-tW2fyRV83SyOT5_1CUzYlIkFxnogxgco4WOobfCe8FGML-QiXM1U4ypSQDQbz1BSB4y-FAh-HLYct5E9bDppaWeTJcgwTV6ZfxpJZ7tzWNul9-dLHrSW1de3qFPX8QnX7TWk6d030EZK2ZYliOL1eSgZ7ljqDDuSmRKRHfi0tec6x_f5saBYrCIpHX3wUB-D1z9bgln32uNTeDyaiNrUY0PwOFnEWHWRpDrXBX3YyKDYoKigEKzJgm0Fc1XQCRpKzMa2qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=j8waNVK-wjf598DQ_GLmkXBiV-S4RSCiAF7JQ2yAJz49hOyr_tt4A1bMcl3fBGENIrAuCv7PuvDMZTz-tW2fyRV83SyOT5_1CUzYlIkFxnogxgco4WOobfCe8FGML-QiXM1U4ypSQDQbz1BSB4y-FAh-HLYct5E9bDppaWeTJcgwTV6ZfxpJZ7tzWNul9-dLHrSW1de3qFPX8QnX7TWk6d030EZK2ZYliOL1eSgZ7ljqDDuSmRKRHfi0tec6x_f5saBYrCIpHX3wUB-D1z9bgln32uNTeDyaiNrUY0PwOFnEWHWRpDrXBX3YyKDYoKigEKzJgm0Fc1XQCRpKzMa2qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شادی گابریل مدافع آرسنال با خانواده‌ش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/90097" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90094">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3tVHbxwuPfz5AvPKmZCzNLdUOrCvIqBB2Ph_tG1TE2cDO0CL_k-5qhHkOgA6SLicnV_JenVk7xMaVWALXSYQpbO_xS1bnsXEuwjl5DVSwnNznLDt0eG3C5P9UBgqgdguj9L9aTBhAs_GvVqXBACIiDOHiIzddqkJihbSlXOGPKlnLC_Ey0W0ffFs3F9HY9WreuAIW3WpGcdH63IfGUaLHZtV5h3x1VDExcq6B1s7Ba-6-JbuupgEEm-m4yqZ9QOB8qu8z8CHmmVcMGbKoaboEiLcH5pmW8H4MR7eCK-T6Impg6_IthvBeqBvybUq0X7GB6qvDDMtmLWJp90UfOGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
توییت تاجرنیا در واکنش به شائبه‌ دخالت غیر فوتبالی در تعیین تیم‌های آسیایی: ‌عدالت یعنی سطح دسترسی به قدرت سیاسی، تعیین‌کننده نباشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/90094" target="_blank">📅 12:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90093">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56d546629.mp4?token=SxciveHKHMfYc7sXEYOQllun3864G5xOC1VIUUOkznw59XzYRGb_LgXkRRg3h3pgaDJJJwt1QNcpFcD5qRdJFFzs4Rc0--hiRTehf_9noDBgqjdLDKlFhYvwxw1OoVr_Skhm-DXySRdhP49YBcwLwUjlGy7BrKTo6n1VrzZz0Ipde1C0N_eCg9lgCW9fknyxReRnuFVPoqpQFRUq0-W_TVgU6spm4iTcIxCXDNX2Llmk-3QtZyMcdMhuwni8ZkxSj2WAbwlXUg13ums6wvDO6EGGJuHE99VitBU4iL61nXxxTS6tWApbKnUA5VuH4lGqRIug-Bz1F7HxOe-m69ahpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56d546629.mp4?token=SxciveHKHMfYc7sXEYOQllun3864G5xOC1VIUUOkznw59XzYRGb_LgXkRRg3h3pgaDJJJwt1QNcpFcD5qRdJFFzs4Rc0--hiRTehf_9noDBgqjdLDKlFhYvwxw1OoVr_Skhm-DXySRdhP49YBcwLwUjlGy7BrKTo6n1VrzZz0Ipde1C0N_eCg9lgCW9fknyxReRnuFVPoqpQFRUq0-W_TVgU6spm4iTcIxCXDNX2Llmk-3QtZyMcdMhuwni8ZkxSj2WAbwlXUg13ums6wvDO6EGGJuHE99VitBU4iL61nXxxTS6tWApbKnUA5VuH4lGqRIug-Bz1F7HxOe-m69ahpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما: هر کی جنگ نمی‌خواد، جمع کنه بره‌‌‌‌...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/90093" target="_blank">📅 11:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90092">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🟢
باشگاه آلومینیوم اراک بدلیل مشکلات مالی در آستانه ورشکستگی و انحلال قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90092" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90091">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=BjmwJlew_DSFEVzGz5aA86velRm0BKwZREv1kibQ7LthThYxXmfzIOb49Lz7TxQUs9oNxyKaZWnBWOn-C1_FK-nF634IWqzymMgstVKwB9xRUYiVByzOEYWEIuJRFS8TAYZnJvcL7ywulSDc4432fQfAVVGZ87tiN4bJLAuHPTvLzB2YeI5XPXvr7LD8LvwlMJZ-NPqm_opNjFZAAi7GHmjiSQsPzo0OeTdqY22GF92rKAL406nZPyq5a_TMra1HMCZP0PAmS_Y4eq7Gnkuc9WJiEDGPKtqmsMxmsFBLCKd1UZgLFIKuZKkMbqvhbGqt347-fNygiO3fA8iDqx_FpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=BjmwJlew_DSFEVzGz5aA86velRm0BKwZREv1kibQ7LthThYxXmfzIOb49Lz7TxQUs9oNxyKaZWnBWOn-C1_FK-nF634IWqzymMgstVKwB9xRUYiVByzOEYWEIuJRFS8TAYZnJvcL7ywulSDc4432fQfAVVGZ87tiN4bJLAuHPTvLzB2YeI5XPXvr7LD8LvwlMJZ-NPqm_opNjFZAAi7GHmjiSQsPzo0OeTdqY22GF92rKAL406nZPyq5a_TMra1HMCZP0PAmS_Y4eq7Gnkuc9WJiEDGPKtqmsMxmsFBLCKd1UZgLFIKuZKkMbqvhbGqt347-fNygiO3fA8iDqx_FpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
واکنش تند مامک جمشیدی، خواهر پژمان جمشیدی به خبر منتشر شده درباره صدور حکم پرونده برادرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/90091" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
