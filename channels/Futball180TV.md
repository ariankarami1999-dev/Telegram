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
<img src="https://cdn4.telesco.pe/file/LOsRygUJlbLivrv3n3aoa_zQEtyOIE3s_V2VI3l_RzrzyIBurKEdAfMBuqWJX4Yn4NcK5z_dj9vU0kGTiXGaj7-AW2b_XAZ72cICuA4lbHErtuhkh9ziuqXo9nqEoC61RANiziW5vf7icjsarkIcK2W0Cgg9ptll_4FGft16PtKBFhHB6fc8DMwg4vMqFFcDpK-nLLm60V90vnK4-yZQHAxkGx8wZqFy_k69J3Kovv70hitc9P-DVTdNcDQG_jsqPrbRWDFBRNeX1h087ZGZTgBkeRMg_guMfk3Smr4StnsYeEf7mtDoyeGzGhsgGHxcxtSz5geY6L8faFAJ7Wk7wA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 134K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 20:18:30</div>
<hr>

<div class="tg-post" id="msg-90004">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-hqUbXGPof2S7Q50un5zJzzvs0MrXnRb5oc41kxlzvT50qlfqXZBpuwrUFIrXPEjyuBykXa__eCtgd5kDRH_WbSV0-7jdluZILFz8xz_ELxzIDkMNiOYnZM1QP9pECARo1Ke3T5Yx-Wq1P_AnAy9clxYPh7YsFjt5VYzIrTMY_BAu7ek6dWnPLTBtzA24RMEmRYbl2swwp-xeHahvCCdT04hB8whOi3XenHHYFuRg6TPSYs3sCSyQXgS5jr1hNGFJqVv0wH_8u5u4JkjMbQyoYNEC-Ozx8aadyWegGn7mMkmvthQt8b5HZbVLHBudpjPIkQ-Aygb-gbjs5RUZgaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 363 · <a href="https://t.me/Futball180TV/90004" target="_blank">📅 20:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPnkNvY0Rz-85-r3M2dPFkVulUKBeUy8HOayQ-mCjTX_MpcusW3pAEBF8aficUyIudEzuH3bcxdrWI9eEZoTkTPqa7QhCD8h2au_gaFm0iz0rfp49rxZsVubbJgaY_G32n8NUEvmtwGzJkSOVQf4H1_lM7j6_WZFtb11cTURUsNFInjYga5-PNUh8XXE2jtZGYpJSK5aGfJa59OEov0Rho485u0kzZrxim8TEZy6T2JH468g7H3QARR3l65uqxr-XcKcpv4tUHIogbqZfdPT-2K75hN_K4Vr6-JDWVxnpHjob_lyXU-gWSnthEc0Uur8HtokTPD1J4usPjBCPMCxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پپ‌گواردیولا طی ۱۹ سال ۴۱ جام کسب کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 598 · <a href="https://t.me/Futball180TV/90003" target="_blank">📅 19:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt4bDx4sQJLVOxqqEjMK-Fq7EqwLtVyXomvLVO4NSmeF1EY3kn0XK0ffZuiltg1_sXVXVScyow3_sD3n7bXSCfR5N_B3jsJy3_UrlfNpFxtPoA7ShtFPlL9ofF8NVDDSEhixXXSmXKZJmqm6bQinMLUSGb0Y85k7R9lag-lXx3WA6fk6dNR8JMXA1lAObU4nxZoLVwezGRV8nPuxpwWhFsuy9Obxp78713eCu7yk0FKhZVIL5HO2wGd2iacQUcQfJgo8VKgHU9WyQk9jJ5noiEO2uR_j1ncJ9H-5W2gUaXoM60Za5vSAw5PXgds7haVo4rJUpsXvPF5XnkYpoKf1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منچسترسیتی با برتری مقابل چلسی قهرمان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 647 · <a href="https://t.me/Futball180TV/90002" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90001" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 617 · <a href="https://t.me/Futball180TV/90001" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJeyFon773X9La_rUxvMhn1XmDvRGp1tf0kX-dgNRclvAGVy5h9gv0e7HKcUprYfAbMSm2VAZAUMf1yYKhdC_tWyoOHPJ7nc_1cRQgf8_amTa4WI8TPk0rk7BWKvqq5lzYDuErV7kSJwPh5OM6-GCxEyhJuPlsqURCCydwEUYKR5Jn-hGXYte3bi1V5Mys82ZarXUv5PAxIhUdWu_uZtODTZV9uWkwQkqA-cUfBZhZeBRYVoQ_P1G1oNjB0acLhsOkaEDACec-kYhl9aV2XFiiIUaRHB5Bq1UAAV1Ft3HhC3lth2FrhcyOPINj-Zl1t5b5ooMMpGbjbL-iYFAdjwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازی جذاب
🔵
پاریس سن ژرمن vs پاریس
🔴
را در 1XBET پیش‌بینی کنید
⚽️
فکر می‌کنید کدام تیم برنده می‌شود؟
👀
یا چند گول در بازی زده خواهد شد؟
💥
🔺
ضریب‌های بسیار بالا در میان سایت‌های معتبر بین‌المللی
📱
امکان تماشای زنده مسابقات مهم ورزشی در اپلیکیشن
⚽️
اسپانسر رسمی باشگاه‌های پاریس سن ژرمن و بارسلونا
اگر پیش‌بینی‌تان درست باشد، شانس برد بیشتر دارید
💰
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
<div class="tg-footer">👁️ 617 · <a href="https://t.me/Futball180TV/90000" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1wb5winNnpUCNnYLhlM5JzazznQXW6kx6Pk-Vxp3zjd-VSV-xJGT7zL4kL3OvTHIDYTb1GarXJLehamooZ-0zfpMi12puCKofn22hyk4vgL2ms93_O32Zyfo-OtO64UZa2LrKLlbfxGkXwWpnXH850XlXpHUw87I3CqYBOayQx7hpY86s3rJEsd_XwxU0WkgWdKs7I4uJ8fqqKxLqNKYoFtsvrUweP08c_xUsVBk1HRpefp-D6cDo_kBKNKlJz3I7dTYZ6wSbeqM65G41QvIssKb1c6noDeSZNmuL8Z_Ti-Fbq3-XcRxp4-mlglOvL92njn8tKLRg8DCJPREV5oiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام‌حذفی انگلیس؛ ترکیب سیتی و چلسی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/Futball180TV/89999" target="_blank">📅 16:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXYpTEto6bplrpiu1aN0s5Ct5TQhoQwlwJffPT5IulXRixUOd6edR46xWR5cCro4wu8KPH6mg4AUj6HmO1nVQwfB0f-byvucAKBA1CINK9HvzxgzLqQ2xjF847uXOs4MpRTpy3kVydEh_X6ZEyOZvzgHOLqFZfDh00ZfBtpvu3Yu1772PrOYcwrHZu6qTgWHygNKDFMEq7fakVBbnVHUvffADwiWeV2Xpdhjzhvd-HlQ7FnDoVFe_WjtTyEgJdH5-gu2uOb8e-mET_Fuenu6g2z4_gqfhk1P38CxL5RtjPPlMztFe6FEw8gg5sm-hRxHjc19amWmPnstvQYb9mzLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
فهرست نهایی تیم‌ملی کنگو برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/Futball180TV/89998" target="_blank">📅 16:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKhinXGdDyLQ0stlqhalEWTVWcARKeSlauJNTYM7rBFYCIYFyT4cDQSPmSGptKljsE8SHmrJqpjQW_37vaysksEQ8LSxKGU2BV4pRVuCUYn4aNtL_G0aLKhHs2yJG9kt6P674A_wJvcbHTiU9-DfQfA-632Y0q3dVE9uW6FWfEXgxAwQUPVq-VXMg504rwhdtUr3eUSA88Bc-1tLqIX8cqAZqLgiJZUCTvsktR4jQmApbUSaw99H3jHHaQEQ7Tef72a3tF94JQ9BYUCv249zZseDEAC6hyE4qKTSJZHQpNqabfK65LxWABCU9p0EgCJZk3LyDcWLp6ZBIqA-jDetCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پپ‌گواردیولا: فصل بعد نیز سرمربی سیتی هستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/89997" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=Crd_Vm82h_0PrzD2WbI94peoYAYGR2qz3e_Z6d8zgHjTRb8jWPzGYmhbooCrRFsUpxq25wG20pmhcqxp5sBxvlTG42ZefrQWCOg3Cmrz5UeaaKkX5X55AwO4LJXZppMRZGbD5eqU_oEB3ZnwJdG9l63W7NoK_qHQr-zn-C-THaoHubcr_tE-os7HFPYoQQPos3RXD3TsYjW3tqGp_azfMVzfVxjx5Vwnrf-N-RpEK9zbe_6TjcX1rOX7e8LPzcprn5FqtsCyZsTdTOljDe3Xq-R7di9t0xsXY36kX8n90NmqkhbbZ7MAigagiS6aO_57f9swsyh0upJaTd5pletdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=Crd_Vm82h_0PrzD2WbI94peoYAYGR2qz3e_Z6d8zgHjTRb8jWPzGYmhbooCrRFsUpxq25wG20pmhcqxp5sBxvlTG42ZefrQWCOg3Cmrz5UeaaKkX5X55AwO4LJXZppMRZGbD5eqU_oEB3ZnwJdG9l63W7NoK_qHQr-zn-C-THaoHubcr_tE-os7HFPYoQQPos3RXD3TsYjW3tqGp_azfMVzfVxjx5Vwnrf-N-RpEK9zbe_6TjcX1rOX7e8LPzcprn5FqtsCyZsTdTOljDe3Xq-R7di9t0xsXY36kX8n90NmqkhbbZ7MAigagiS6aO_57f9swsyh0upJaTd5pletdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📲
پست جدید لواندوفسکی:
بعد از چهار سال چالش‌برانگیز و سخت، وقت رفتنه. من با این احساس اینجا را ترک می‌کنم که ماموریتم کامل شده. چهار فصل و سه عنوان قهرمانی!
هرگز عشقی را که از همان روزهای اول از هواداران دریافت کردم فراموش نخواهم کرد. کاتالونیا خانه من است.
از همه کسانی که در این چهار سال فوق‌العاده ملاقات کردم متشکرم. یک تشکر ویژه از رئیس لاپورتا برای اینکه به من فرصت تجربه باورنکردنی‌ترین فصل دوران حرفه‌ای‌ام را داد.
بارسلونا به جایی که به آن تعلق دارد، برگشته است. ویسکا بارسا. ویسکا کاتالونیا
💙
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/Futball180TV/89996" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLkmosTUKxWvrnImQI3VxBagV1C6EJ-jlW5eU09PqBYtsBjMzVBO0s87OShRlwzvOLY-bDI8LxR3H2Nq7yKWLfZ3k3xElL_VOkFz9zA050oEkhAyVQJWFiHgQLWDo35Z2TjABOOsuz74Qd_uy-cnDSojhb2ffsT_uCyilD-sdmM8UXo1Hzm47Z4VqESMO_9qHZ1-M0CXumX4ckosRDOs2doVXvSnBb5P6eSdLLD6FEdAtcS9f3pFHLlrhtqjTN3y6z6OErkqY8NlPxDnJZ4M_ulAnzg5lRRxLsdj97CZhhKShU71DXjAVqQiOdaJVbRkovMyDuUBDvL0nWhsbPTd8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نت‌بلاکس اعلام کرد خاموشی دیجیتال در ایران وارد دوازدهمین هفته خود شده و اکنون به هفتاد و هشتمین روز رسیده است که در سطح جهانی بی‌سابقه به حساب می‌آید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/Futball180TV/89995" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89994" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/Futball180TV/89994" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFxZP6VSaiaLPDiB4vjDC-NhFV1yUXgLmG0O92l369odfcPEfKligWAVXuZHjrlZsnrEzBHKY1qT0ZD7mOU7_Q8od5FU4AdDcRBXspi2-TgZza-mvb4jKqqAqeVl-DFdzwnPCe5U_DmV0FHivGcGCuxh4-uaSSiLljeGVOH5Wf2Kpozq5747cfI9ZvZwUfwz6CXrAngZ8IrczcPUW1vKJ49xWwCMRc6r7-0O_oEmeOLlKXfNGuxLXOWS-WNPlAyv0TUqF93fPgSM7UjURAzFzgeiIYgw-D5PELQOZkWRy77-c2BHcdtBcAXNFU3iyFkvPzQTaeAQe7xkcQn9TWVJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/Futball180TV/89993" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQkRIahVd0jZkuoPbMujLCIyFgTbSBuY2kej97fKeQP0f5UY78WmYvM-ik4owvLnMcuLv6UPGI9KWltDx5D65Iff5tTMFHBsjGJV7AWP2E2ebHZSB9s8bTlZIJqM7Lo95Eoow8fJQvyLu6h8SnWkzzgQDRKRaCs8yD-KwHeR_-DbCCfXvXCMaugG-0Uw4gfEVBaso5T_lZMKna5rtjrR2f-t0GWdFSEChpnsNnHKZn4Un7JEwcHhy-WWqGvN0yXi2NT8zX3zDIql-mo6rz-5hXPpuv8F8mmt7o8CGul0Sk-eQHJIH5NuFHqJm05gAV1PGz6djkYNpKZF-Q8jHaKbKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
تا اواسط هفته‌جاری انتقال ژوزه مورینیو به رئال‌مادرید رسمی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/Futball180TV/89992" target="_blank">📅 12:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89991">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=mrDhI7Py51WhHxO4rOZg8L-ZhnVWnl8zIhbfGr6FdIUqnVjZgVJvYGed0bqHSbG6HAJVj16V10rlo2P-lerWAIGMSCiIEzL-jYL_DoAMqQgQp6x-LwE4CmXWHn6IiLSDJGnBYKc_v2gxmkhPh0OVxpBl_Xr1Ivq1l7KwVmMW2Q2xagDHhNc7jCGndwO90ZLTLTMQbBH9uZQZXRqb3GwbZtnCbYQ6tj-PxJYdBTlPMpXyBHZRW1oGbw2RJsDcVEupcnzVnn2hYH5ILory0ylMkWtRgbSttvJ7C9d14ff5rprw4MC6rrBvDJ6LbAYimAGy7o2VIvDosyS9NQJZbliUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=mrDhI7Py51WhHxO4rOZg8L-ZhnVWnl8zIhbfGr6FdIUqnVjZgVJvYGed0bqHSbG6HAJVj16V10rlo2P-lerWAIGMSCiIEzL-jYL_DoAMqQgQp6x-LwE4CmXWHn6IiLSDJGnBYKc_v2gxmkhPh0OVxpBl_Xr1Ivq1l7KwVmMW2Q2xagDHhNc7jCGndwO90ZLTLTMQbBH9uZQZXRqb3GwbZtnCbYQ6tj-PxJYdBTlPMpXyBHZRW1oGbw2RJsDcVEupcnzVnn2hYH5ILory0ylMkWtRgbSttvJ7C9d14ff5rprw4MC6rrBvDJ6LbAYimAGy7o2VIvDosyS9NQJZbliUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آموزش‌مسلح کردن اسلحه و شلیک در آنتن‌زنده!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/Futball180TV/89991" target="_blank">📅 12:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89990">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoJlwSaaNXm21Z0EbVXdA3djg-BUG_qo9s19nK69mlh6G-o-1GbY1MoqCLkyeed_PtXkfFEFgPNjAHJkyiHYYGjHlVHH9kwbZyUSRukUTpgybAxu9PaaMMA52WFBXHMSRgDIU7iN2adI1xE8xAPFhX95EGjrR88pGrsgWhKzPprJgai8Psrkx9uUFeRn0owN0vJSdsEI-MGx4OEOB6pNSpl3NGEJ_8qfX6EssDJDQgFNZigyewI7F1MC4V7izKtJMdTjmZd9uPl1uBSuKazCSa2ppasG6H5wPdELdn0UvJdfktFW9u-g59vtNgm2BK17umnqOWx-YwEeWNeWU--Q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هانسی‌فلیک با ماندن رشفورد موافقت کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/Futball180TV/89990" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89989">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhPVvKm4F0BDeC3PYw4X1RhKJ1Md2l09t439Bw3qbrefmcuJgF6L-TkL9Wf4-Oy-DbCT-PqIvzvWl5x6cTyxHCFVdoWGpltPSngaZXhIoozUM3v0MDVRFa5syz8E33w2RqhlXjnbVQjsB1XwymbagOPdywSIT0HTCuD3zRBRFl8JeU-8enUa_5IWXUt9dPqe4ng_VyFnzX8a_T9me90DvLeONpthFVY5C0r79VRVkXIR3N6wA7iOxEvzLSnXBS1pgWPWMyOAKxZBJa6uAuL6bD2hcWxCooaVPdLXKe6d5gCUEw4qGQn70_mduBkczSoFO_bHffd1sFTISZPHqcgL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
لیست کره‌جنوبی برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/Futball180TV/89989" target="_blank">📅 11:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89988">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-_t0iZwJQrw1l8xTwApiS91ljc-EgiMpKf14iCjF9nKV8wbzy6dTSqTSrJiOaZr-eVmqB_3RTDxHi5Fej3ZbM7MYmYw3q564hYhZXyyAk1feuRjerchOvKBzIWhiXYuNA6oonxbM0jL82WdZg4HMDhllSto0m9F3sKVXN5PgNswtRdtW-d2awOsAReHE6iniT2-1itZOXK7mV_6EQ50P5zP_aA5RlQF_dZGEIMLjTpPRMTEfJIltlpXKRJiwVhmFLHkHkAkR71HO827rgl80FVR8928y8ad5XQmaG6whM9lUvcOhsKzwc_OujDf82pnz5s5Vj3vsYk7BSMAzI0Nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه آمریکا: ونزوئلا 7340 کیلوگرم اورانیوم غنی‌شدهش رو به آمریکا منتقل کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/89988" target="_blank">📅 10:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فوت پدرم باعث شد از آلمان برگردم/ کخ سخت‌ترین دوره فوتبالم را رقم زد
مهدی پاشازاده، پیشکسوت باشگاه استقلال: در اوج بودم اما به دلیل مصدومیت‌های پیاپی‌ای که داشتم، وقتی خواستم به استقلال برگردم، آقای کُخ گفت که باید تست بدهی و این برایم خیلی سخت بود.
به ترکیب استقلال برگشتم اما دوباره با دو بار پارگی رباط صلیبی لژیونر شدم.
کخ مربی بادانشی بود اما اطرافیانش خوب چیده نشده بودند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/Futball180TV/89987" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89986">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromADS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMDPP9Hy37ypglCxUriouskcNthGeVLM0F05acV5kWPZjXUmki9AKM-wGt1mrSQAZG9ywYW_BuuSIYbRqxyEOBlm1c0ZbtcHYo2eRh0DxJ7A6ZxzgYAjvF6gzQTyx73fMFJ9Rno-FMQJgs0Qiz0Cx8M2q20fpPgOXp3ym93slTsMrbQ134ReUpvwVCIwyQ90ri_XR4QusZOJEuXyMAOVVZplVrN_Gk9o_QwffkHCg5cTf7VVWKbFSnvzODcIOsf0IkMVWxuzEq8HaoTlgdnyJJesJ33Z18puOKE0g7u5QRddiLiCtqmxBJsaGQjHFQcVfd3cdPzM1p4Db_GCzPemoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
بونوس ویژه ثبت‌نام – ۵۰۰٬۰۰۰ تومان رایگان
💥
با ثبت‌نام در سایت، ۵۰۰٬۰۰۰ تومان بونوس رایگان دریافت کنید و شانس خود را امتحان کنید.
🔥
چگونه کار می‌کند؟
⬅️
ثبت‌نام کنید
⬅️
بونوس ۵۰۰٬۰۰۰ تومانی دریافت کنید
⬅️
شرط‌بندی کنید و بونوس را به موجودی واقعی تبدیل کنید
🔥
وقتشه بازی رو یه جور دیگه ببینی
⚽️
پوشش کامل مسابقات ورزشی
📊
پیش‌بینی با بهترین ضرایب
⚡️
تجربه سریع و حرفه‌ای
😀
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
A24
😀
کانال تلگرام:
🔴
@winro_io
😀
هدیه خود را با ثبت نام در سایت دریافت کنید:
🔴
Winro.io
سایت اصلی در روزهای آینده بازگشایی خواهد شد
✅</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/Futball180TV/89986" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89985">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIRYHHIe45nhJi0u67jalMAEWgLf1y8jeP3TBoYq7TsFadKjWdoj-mLQkq-rU26JNG7kujcgYVgJH_S2tusMMCmVtHRZNt4KI6hjDmLal-7qUxQI--_qxhq0wCDOPn5Y6Oooil4MJaPDyyd-xuXXU97CH4Dp1s3BShW3XkVoQZxqn7aOLadRqaEM2yNZt5d6kepZFYEvO3NFMpszurp3CFojO9j63vro896UUfDioZhEvslNOROpAOzily3bDhzge8ryzefd0D27bE46RJ45bo0t4Umb2BC4p6JbziYX42lppW6ConM9xCkZAvyRBQmytNteM2Ot4vQB2OSyHciSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژوزه‌مورینیو اعلام کرده که پس از پایان دوران حضور در رئال از سرمربیگری خداحافظی می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/Futball180TV/89985" target="_blank">📅 09:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89984">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">💥
🇹🇷
جشن‌ویژه باشگاه گالاتاسرای برای ایکاردی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/Futball180TV/89984" target="_blank">📅 09:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89983">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1mvNgCnIcY1yZMNF_sRDiW1iRXZaoP5MHMq7FsIrH9xG0wyyjZnWyDU2zGG34_SGEBAveXR76YYTJigW1C51YGLGWEa04iQZlrbrcQPWzq1fk3xbUmupEnauAFepprWGkjLcQ8yGN_q96CdopgeXveqyJJwtYw1a9Kb5CK0Z94o8wuhTvVrY7a_LmU7F1UI8Pqh26iWRmyR4MKmDhrls-XrxkCjPx5PjTvvIjwy1REUS-_zkIt20dSFgrozW-ouN_JaxCtVlOAlNJ-rvZKeiJ26yzM_CFcjBnRa0QgaeVa1dXlbM0fvwq3NwE3wbwLfA6ltMYHPKu1iL2bht20FhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک سرمربی فصل‌آینده تیم فوتبال منچستریونایتد خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/89983" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89982">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/89982" target="_blank">📅 00:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3rbPzTCLWuNUS6LAa50nXk33XBRkmJBjyYhN-ejDODo3f3QdPNl9cgkfXq9tbi3Bjesi21NOq5lmKxJz7dPrzQ3YT9vFQMDuzN6lPaQGYKMwgDpN4AUV5WCPsBtOkHs5n0-W2gU-nptN1offsIB_llYwgQy30yC2Z3LYxPzkIFR-N1bxodE6lS39GTwVQwaztjDEK4blqjc1DMRTBZVhw2RH5MGrN7aPspEWw-XuIRJWjQwMyPtZqJ3069jxbygo3MHrs1fFPeEMEKdW1UNf73-k3Rlky_WNUS4pSjauE5m5xODUISGttL5uuGkMH6I2-Q0gnj78XEn6kHJyZ1aRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/89981" target="_blank">📅 00:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0zvE3MvuzDzsSiwUr1nDq8qowH6cPNBVkkUMX2sZPZofaycf4U9muLhPOZxrpgKT7sI07wtIBiUe2uA8DI6z3tco7SOJ2HifQv4ejSn-Ni3gEktydOYqSIa9KdpenoUa1A0oLPgSRnlMGgEI-jIIEJCWw2ToV8pULh7IvoB5Czj5zbOsGwC5nj9xDiKDPJiLAdWHTj41dNeQRCUBXIqsIl3sRs4-nSnlCyj382xLHURGSU_42oYy38fIXTRO7X4CwX8qvbYfEF9F-W4VUxOwprsawpHCDUOxt7Q1mzuvg3DIP3KTU_wYtETmb1nu27i49QpT1CrUBv7gT6ZzEIBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل لیورپول سهمیه لیگ‌قهرمانان اروپا را کسب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/Futball180TV/89980" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nD1psfZJwQN6R4bhhgGuBX0Aa1kVUFfsAlh1sGQsXwwj7fY4Ycj6Ry_2a1ThM7YXwLdaJp5h2JGkUUHhkkxm8mTmA6Dgt71Ef-fl4Bbbehr53V4Xnu7oV9VJ8gdtBOPPpUfGBVLIv4TA7zX-sA_AxSUHJit-f4vyTY2zCL0o7XW9m6IU1v9eZdnUnTqk5rw083g-Xnn3cLiIVB-QhxwTy0C9F2xvBxEBqTlAx_IZXnRIJ9HnvWgRoIDFX1CS5cz8C6egE_AdreCy2iLAngotmaktd-OYa7hTONp2PxkydOtUbBTQCD2hnVkKVU5kQFwVr2pxADClidTtNvR9cI95tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/89979" target="_blank">📅 00:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
‼️
سازمان برنامه‌بودجه به دولت جمهوری اسلامی اعلام کرده که با وجود تورم شدید اخیر، منابع لازم برای افزایش رقم کالابرگ را ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/89978" target="_blank">📅 00:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erBzVlPbHs3LY4dAlNcZc2rGmjrBNcInyWVNzrGnvMl_aXAFD4Xq-mMx5-RTjpCJ-wKBXUdGluJjBFlvOy8kQJY8d0WFY6yzEcktndR0r9x0f5w1hm1e6A6PaeAAUaKEvJMKkLFBSw1GCvk1s_MdWKoGKEzyD-wu6f3EBXgH_G546sv2c7vq1JvTVFleSne9xfZo6maeDa9R3J9qN0EQyfD1nrVQ0EbhK0hLxvGghL2nZWP99_4N4Lkmo4fQtGkanKkmkF2iwcoIb9M1KgotnehZDggwwLWIAQhpEU29YB-ojd-gitgn-oELHJuFD-3XXD0aAnkZb-yz6IWJBUoecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇱
تیم‌ملی لهستان از برگزاری دیدار تدارکاتی با تیم فوتبال جمهوری اسلامی انصراف داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89977" target="_blank">📅 00:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCfZL5RvoOnEmJSjSopohNhbG8Mj-J_QoS0hm5YFjlOXJ3lLSMd1LeRKra7Roi-bD3muVqYTbT20ERBkAN3QRa_CHyQYWyX_cAYjTsoFJbkcZTSq2IDv_7VNpgrldsAOJ5p_oUTeWbBtVKy4QXKQAhzdqqQhJTbchS7t5nQGeQtsme3bVaBtAroJUeFT2cOUO_rlbHYJ1T8UeULJfI51iSmNdD71Mr-AuRIRAV6KesHdm6O-OXavkuoU88bZtG5dRrPOisaOgtl6sy-1tg1LC4i3PWOQ1fKrXl2-0KNS8ZdUnA16H_kdh9bV4OEOCM6Ajt1_pDmeMcLDDF6Y-rjBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇹
لیست‌تیم‌ملی هائیتی برای جام‌جهانی با حضور داکنز نازون مهاجم تیم‌فوتبال استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/89976" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89975">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-yWAdpZ6amBgh0_Z-Dp5UBcCGNm77SG-8OKdOBfUUc7nPwo9bFA_1GQTacZBBWXcuog2WzjWP9xLQnxSqhmSfrwTz40YYdkE3tcnEbydRsT7Wop3UrL3dI6gBUMnTeJ4hEKa0mYwPgIdyqLeUEgAoOAt-r8OSNgyqWxdeMRC75BeBWDGgyISW_ovdG4tex48QcSJPuvt3dvlbvjp6iJZ6hGb7Pubg7og0-ruR_hQv56uaD4ZuX4APfrZOVchoIJdp_iyaeu6uTyhtKYb2R8HSTZRxdK7cl5Rkkcdmbx74CzLBHV-qUrOLYHEjnHRam78tkRdSP3tsCh-IRnnLZU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/Futball180TV/89975" target="_blank">📅 19:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89974" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/89974" target="_blank">📅 19:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89973">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0v9eZS2NO7UMnSH5s24jYwIeCYoPu0fLL5Qjj10rdjqcgUIt_2CdXhLD3K--UPr_T1BgElu_fq_l1Vi_jUcBe-WxBpUkUyzZUnikcdYwFicuqv5jRRjszdi2Qnl9pErhzP7aeMXVm6KegjfE0fM0z_S5GqAFF7HaP-eVmjHBQl-azS4ok-tCixmVkjtriQ_-ySeLfCAOpxolp_yMyHzZAHH4e_sGlbTPJp8ktPtaLhguTG7yTCHRUT0ChIrQYhRAcNvKn1yuH8j-k7UnWHVR_r9b0PLE-2dV8mOVblQco6z0TnTyhQFVPxJ2uzq6diBHomNe7ZIrezt70MfTSFg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی بدون ریسک بر مبارزه
Verhoeven
🥊
Usyk
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
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
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89973" target="_blank">📅 19:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89972">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzA3ayv1ApXiRbNIw8rG_QQlLm6Be5GVqJB8tfA2A8vI1liq9aGuutS9ixppsmpjIUXtV--TkbIiLIOj2oC1ZxDPWBS5PhorePq6_WSOSOFgS2fIzvbKv4soJJLcQZUIMvQPC3e7XrBkemfkhON0WgszUaYNdqhQhwsiUVL7mCEoNB7YatgMXFPygJg8Gu_BainhQWgBA7u6b_mXKTL4Qkmzsm8gHCcdo_rXM_3qCKKBtvYf57gWDX0rXXf0N3JtuORqz-Ac0zhz02kSlM59-rgO8aQF1arCMs62DaahSZ6inBbMb_j0UzsE-uMwEx_PVh8aaBqs-O4WcP5F7BBOBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
لیست‌تیم‌ملی ساحل‌عاج برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/89972" target="_blank">📅 17:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89971">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnCHj5TrJu-PbGTGLP2jGa4o-BE9OPXRJHl542qBYaZ6-any0jhYF5Xl6oxsQx31l0vFjz4z1NZ4xBMfSmpES7qZ0SBGf2LDba74Zm2le_STl9oSb5WFMpzGcOZynP-mBaA17f4UxIjMHIPF1HsRvVo8bQe18zwq_cnSZqH0DJEOC3Lxtkf2fnHsw0JpbmPXC7x0-QjlPiYRC15lMSNk8cvOtuogAfJbBml0IZ_Mry8Na1a_KDwzHU1fAxYtjd18Jta7LKVT4ttyKC_wkry3q4RggDNftFkKWH8ejoVVM5JqLP9JW94D4ctxXiRdNh3ero-EpS-8vkcrZF5po1tqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
اعلام‌ لیست نهایی بلژیک در جام‌جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/Futball180TV/89971" target="_blank">📅 16:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89970">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇺🇸
فوری/ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/89970" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89969">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSK-XUihj6AebmasESYuUMoKk0foSj06YIQc_5zysdI8OZPhw1ZHGL-BHyvGjmho8xPygxcvA9Fr58gy3QTJwu-yPoRo0F1JoUMeGgGya57cbrtTNNkPH0Q3QpA2dAY8AVHDwe5lWy15kCdrUTw9gU_o4eBN5-fVQHLV6ZzIvNZY2cZW25TheR6nMTW-8OzL4oVY56ZuphZAHe3ATK40vjYbCzc_2TXGHbVffT7rxNWRzHnAH4AhcBdSjmOZJWN-022HHpkgg0u6cCNupjlaMgCMjg12l5vERb8ayJUMU-sqnEDB5KWCKkAjoz4wf9wQSwTlOi6XQEkeBY5UE4jU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای بهترین سرمربی فصل پرمیر لیگ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/89969" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89968">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/89968" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89967">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff-sro6mVqWK8SvYHg8CvC8jiHf1PPurY2Ply6hJOhYzQ94zVH8wjPphxDaRe8yB83QIN4u_JbzPXSEBFcRMVKKsqYMw4VBg4tpzPWlJ2bwT4Xg08BslbOFA8oSUwjvqt_NOeIq20zybqQ9swwvWlrpOKOyK5Lj10Yo9KguQeZtQzFx9qQzZ7-9DXQGceGqcRMnEcdZZBjFCo13IYZRfiSo31ZxSsuAFscouS-0hoF7hEeZC7LvnEUK4NgZoikErFlYGR0IGM2clzH6OGHe3grOJbG4Z5IZIMjJGE_kOpEeJevNEnpdAEGqhoRg5O0QR7Ll-BrSGl9VIJsnOnTYcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/89967" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89966">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy9UvT_STFJO1mpW7FWI-yI82CIk3o4gpsDujoOR4DpzFtltYKWPcUwcILBzcfR_c4mUowePURtk30PBGnhQIkFKLoBxgcFsfsdEuqUz7-M_ILNbPT8CB9dZgH7Zvu920p2j_Rd9bXMvVTF0wMnPPzwxj61KRfzM-edSsK9e4FrRIshomt8zJlBNabitZNslKzZOHprZay3ZXCGm4vG118JIunDll4dQbYW6Z0Lm___5oB4DEdEStH0Vi-SwoafdTHOxwtNlwo0r0y60sOJeG2E81gCCB1NbiHdcKkavS9nbuRkaCVK3kf3lCZ_Xhb_UEAvr_OS8pI356GiPM6tlCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇺
کوبا اعلام کرد رئیس سازمان سیا به این کشور سفر کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/89966" target="_blank">📅 12:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89965">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeFVCFgv5yZ6LbcN9n9lABtrpsuExDH0Sj2P-VvpMaE4oNlB_7NWi-ZLkXaf2OGrBmyrZNoBzU5TZ_ecapggkfSoMrLOK1iAVndbMH15lmUrOsFk2Oyg0o6Vh1OWOQQIcvsWdA84RHhjz-ibVI4ddiwWPqVgIUYc7jBI9_OYr64J1c9kxD84HSiu8SEdBDQPFbE2wkzXowS-LKPL0AWNIREeN9BHGvjbxOb0mkm7sEeuI2Jyo5VmD_pzb7WfhPSRi52LFzf8nopjhRy0FErOPgyouDyhIA9DwsLWY3B67gHQZA9NY-JWyzPQYlIuSH8DwUTAFa-YA4EH0KjTDlfa-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
فهرست تیم‌ملی ژاپن برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/89965" target="_blank">📅 11:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89964">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D91uyzfazfoVYRoAcV1zNkxVCJOFZLufvNVppDQETo3VVe-SVPfppMklg3pCIQODVoJYC3Mp4aHXB1JnIlkFGq768uwuKGadMgkuG1gRApwY1wAaaSDB5q0K_fx40ZVmjhft9p_Bs8Hiia9TYbsMiua4O3OgfI-yzechnFoPSPXoh9_ynFE1ciaaSq_QnKGe9I7J-Sx_dPmOnEjRBjybuGJhaqNVRNqbI74KCF3TGxWcHcZmQS6OkdSCNddCVybYH4TkYwIdzdZYYfO9u7LX-7lqN1VnGnesVTqjgrqYF0yAHj2veAnP24YqEYh0wi1vbbCi6ZI2qs5gMJTnEBpOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
امباپه: سوت‌های اعتراضی علیه بازیکن مشهوری مثل‌من عادیه. آربلوآ بهم گفته که مهاجم چهارم تیمم هستی درحالی که همیشه آماده بازی کردن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/Futball180TV/89964" target="_blank">📅 09:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89963">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
وزارت آموزش‌وپرورش: امتحانات پایه‌های هفتم تا دهم با نظر استانداران با توجه به شرایط هر استان به صورت حضوری یا مجازی برگزار خواهد شد
امتحانات پایه‌یازدهم و دوازدهم تا تیرماه برگزار نخواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/Futball180TV/89963" target="_blank">📅 09:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89962">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWhVjFFM9I_erzZSVVkjZFL8B4O-_e02FidC_kLq9h7mKbyVsE1DS7cRK1rxNGG3FGjRoX0yCcOuGLT8l-nWV8Dq2sIBjWID0YxFvpuO1jAtJUkve1PPQyg_SEI3GgsRWFgMoe3EJvcPFPnmjNUcPAY0bXffyzjsZyGaZogC9C9L-qocZHBAnGjTO6wvfOUyIO_01auGFHYGtsXAAuF-UmI3xpli1zg4ELAjDUf0O4mpNWfSsotFmkh379qkYfHM0Q-jhqA4wsrgnilbn4Gb4_K2uE9cb_wAJ799axH0aWXcZsXppHeci9YSH16YTQ2QaM_Br7pbDLMn2FVz-7tTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که بیشترین قهرمانی در رقابت‌های لیگ در ۵ لیگ برتر اروپایی را بدست آورده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/89962" target="_blank">📅 09:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇨🇺
دولت‌کوبا با هشدار تمام شدن مخازن سوختی خود اعلام کرد که برق در سراسر این کشور تا مدتی نامشخص قطع خواهد بود و مردم این کشور در آستانه شورش قرار دارند
+کوبا کشوری‌ست که اخیرا ترامپ اعلام کرده بود سقوط سیستم حاکمیت‌ش بزودی رخ خواهد داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/89958" target="_blank">📅 23:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=ZXUMr5Uxm8nGgt2yiC0G1KH3i5zUj3CRVe5vf80a5vW5zFaNUi-3sKC6M_9Ylx0BtAu1p5z8pYzzERIYUKJfKOsWaXpZ6wr2gc4fCP6o0wWs1jUA-RTbW-oYhLLCRKnxNK13qfH2FZ6aY30WZ07gwwHpKbBc4CiQqi5byM4fjuXAbrC1iXw0i7UsFherndMknENmvPylcL4acEfmPQJURCSrxHuMtN3BY4VCkdIOwoG9J302OaxHh9iVZwVSUb2LuHK_MD4v7eecRYrdJXC9Q-5ly67Pps1FCWF-eElCGjl1jOvT0FZ5fU_JxUuvpk1-f2u8Nyk5ugGix8e-nzvikSHUgUcb6C7ehJrmkhuapdCmO4T9k3iipCwWQD8HaxIkceVwaiwSh4M5kDiONMG-Is8c4t798L40wdZQZbPKPSUxsqPdKvgoCvmCneXAeusvUboAEdbtPiBMT97bE8GEmPzeGziDOn8cyl2hD9eMt4IQiF2KqO4NCSJHNkmB7qZJKQyiQhHbAJbzJ9cvckLXnNS4cgkn3DVpZe4eFsRMTgJcts3fK8UHLn3u9iwzdPIQSirgRS7JaYi8Akue4qqBAsBQEEthSRhSU4m9L7KyTs8CdY4SV-31cG_OF5RZxzBwo2-7aMc3H71aZKeig8tZWHmGVzm5Jz5Wg-xcKLEkBx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=ZXUMr5Uxm8nGgt2yiC0G1KH3i5zUj3CRVe5vf80a5vW5zFaNUi-3sKC6M_9Ylx0BtAu1p5z8pYzzERIYUKJfKOsWaXpZ6wr2gc4fCP6o0wWs1jUA-RTbW-oYhLLCRKnxNK13qfH2FZ6aY30WZ07gwwHpKbBc4CiQqi5byM4fjuXAbrC1iXw0i7UsFherndMknENmvPylcL4acEfmPQJURCSrxHuMtN3BY4VCkdIOwoG9J302OaxHh9iVZwVSUb2LuHK_MD4v7eecRYrdJXC9Q-5ly67Pps1FCWF-eElCGjl1jOvT0FZ5fU_JxUuvpk1-f2u8Nyk5ugGix8e-nzvikSHUgUcb6C7ehJrmkhuapdCmO4T9k3iipCwWQD8HaxIkceVwaiwSh4M5kDiONMG-Is8c4t798L40wdZQZbPKPSUxsqPdKvgoCvmCneXAeusvUboAEdbtPiBMT97bE8GEmPzeGziDOn8cyl2hD9eMt4IQiF2KqO4NCSJHNkmB7qZJKQyiQhHbAJbzJ9cvckLXnNS4cgkn3DVpZe4eFsRMTgJcts3fK8UHLn3u9iwzdPIQSirgRS7JaYi8Akue4qqBAsBQEEthSRhSU4m9L7KyTs8CdY4SV-31cG_OF5RZxzBwo2-7aMc3H71aZKeig8tZWHmGVzm5Jz5Wg-xcKLEkBx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت تلخ یک تولیدکننده در نشست ستاد تسهیل منطقه کاشان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/89957" target="_blank">📅 23:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsfO765LAYheDpaVz25NK7c6UN-EBFuwfm6fEkzglRn4vzMtsi9mUh_0LL4rfqMvKLYHjYoyYO-AyOMBR_aAsW5IYGPPqOUFlWYWWPGS2z_hwVHTAcgv-fWPVudIzXgrgHtkg-aS0oL1cs9c1U0cfiNasBHe7FTR3JnStmSheWXtmm49Wquq8ar97Eah7RF1KlL4N0_p9fw7ZplhbqgAm_MHGKCdCyTbzh99fBfAfkNdBP2FY_TtmGCqhZzIG2q_Si7bQjNLndD8Q3EP5s3pht7m496yucoticfSq2B0cThHW895d3bQM72ZN-laoLoM-sqFhYqqvKcoWMSzOhE7Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇪
فهرست تیم‌ملی سوئد برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/89956" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOq4_JwenglHigV1vNMDF4fVAqWW7GsSHFnkeaBJm1vi_d9P93BGzEGdncUvXdONVkRNOzLOjOQwzMY89pn2DnZ4VnxfhhT6JWixDRE20-qZVqMECL-zA5rUa733hIGgkJjqqKXi_TPQ3wfirygbDe-RCQ5pREbo7JXGBphxQYZRrMObWGBOqETbedFfBLTj2hGC0lfZPYFDCoUkuBrFoKFKsAlWBjabHM-DULAcJKNz87HSaREkCxurEIVbxoknmUYGQm3OgRQEeck8y-jQPCjwsMzk1LIAoQ2Bv9W5IsfKdh5_FK40oDL0gSMCMEL3h9DxFtrI4U5mupTgGeqsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست فرانسه برای جام جهانی بدون حضور کاماوینگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/89955" target="_blank">📅 23:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89954">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=H8ua6ghxsMXgqZZa_6UjwPp2IqLF35m2O7ASR5io2eXyQf5_tHrI19i1CArBy80Mzsqxp9TzXXA_goC-Q_z-fPKpdfB2T8vGRJsFiAzmIX7Hb3H1mjO4a8IVJEcUh-2NhCWgKlhl6HATw3oVhIJ0GP42yEanYxsN2RVnU0rTnoxmwwwl-yYM1jjet2MMtbQZXfIPc_512Tq0HOzNCd6Z0Q7GrmtS5XIn2BpSUnTlZnU1LVB-VMRwsLqnkKJgFclsTeqLYBeblxuk0CeXulgXmkjAzl79_qMV83lRyRd0x1oWGC1Fi5BUjJXvgsrcT-DzNs-FTFeo7Znmp34I6RTg2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=H8ua6ghxsMXgqZZa_6UjwPp2IqLF35m2O7ASR5io2eXyQf5_tHrI19i1CArBy80Mzsqxp9TzXXA_goC-Q_z-fPKpdfB2T8vGRJsFiAzmIX7Hb3H1mjO4a8IVJEcUh-2NhCWgKlhl6HATw3oVhIJ0GP42yEanYxsN2RVnU0rTnoxmwwwl-yYM1jjet2MMtbQZXfIPc_512Tq0HOzNCd6Z0Q7GrmtS5XIn2BpSUnTlZnU1LVB-VMRwsLqnkKJgFclsTeqLYBeblxuk0CeXulgXmkjAzl79_qMV83lRyRd0x1oWGC1Fi5BUjJXvgsrcT-DzNs-FTFeo7Znmp34I6RTg2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاتس وزیر دفاع اسرائیل  :
ماموریت ما کامل نشده است.
ما برای احتمال اینکه ممکن است مجبور به اقدام دوباره شویم - شاید حتی به زودی - آماده‌ایم.
اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89954" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHVO1bp63eCKqtZ4pRG8MQeQj6X-O4WypZuH1I30XjXTd4bOtWglqvnOXtBN11kJSIkuz00fVRS5RC1wBcvJCiQFbhVqhG0zcaO5cgLw3dRViI704z9VIh7jFdihqxPu7K1dhKDPI2ArTYPHpRIQ1cHtORdZGO5BlZmpfgU1bWPkUxjsMOWXjbtPGlStX4Ly6HxIu-cpJDt7mbhEPpqK0vKVUHYHL0n-lxn6QrtdsBcb7BDZZm9xFS_WflUaQOXs6HivUju_6RHE36JIFLANkxHk-HaRDF1IT75_sE37q0Zh0kycH_VvF2vzJ_JtLKbNn00L3wATptFfoXFVKvSlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
قرارداد آنجلوتی با برزیل تا 2030 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/Futball180TV/89951" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsWgZofeIfQMxv3ewmXLfpN0Osd-w0Ecs6OaJ1LWYXAyeHr_H4H9ukGq70psPjDUiQJ785wg3RvWS5hTcfacdSEX3Hyi_u8mwtgfqSaBLFKhCHiO_xAz24AQqtAAPmBFrtD61MMaPVoWn8XrM24ibkT5RF0sHZf-O1d8tPoKkRPd-kcGpzUKHxmmlI6mWxVvZ2RtUUvKQNnoatoS_vfxmoHjMARVAIKb3pCPsRiN7YJ6f6F8DVdoDa1DQ4GPLS9F5I5hwVagw0ofWr5nf-s8nxPA1RmlJ-G90jhi0-Y14kXLsC0dcWpz0gqnSXgYkoJucV6hUEaJvt96e5X0I59_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
فهرست‌ابتدایی کلمبیا برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/89950" target="_blank">📅 19:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89949">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🔵
یاسر‌آسانی در گفتگو با مدیران استقلال اعلام کرده که بلافاصله پس از پایان جنگ به ایران برمی‌گردد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/89949" target="_blank">📅 19:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89948">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc_ZPyDfr-p45vlFYSfq8KT3eiNsjPqBFAnM8MSRSrbKRs_Bw6q9C_8SbYZr5rrO0SAgkvNwgkb_-9DvroZGkxtYD1gVd0fo98gFpvzSowuQjKXMsTlqKqCXnHLwEBtNIvN2fo4_t2wguZFfv2EM40zdoVhOY2DbnjnlxpcHBpsLGn-sFBJd03boGbxKZDijjaiXdaQIOGXVGTy3gCFBR23qrq7k2Mw1bYfshwfq1mqqCjPRQGDW0KD2S_CvzABLKnoqGRiaMU3azXAT-fq4jqDTeyfnHbqFoip7G2wJNvL1POoJ-uQ6nYqQTbCC0M1ctGbJy2j3BkmkQ4PwxLS3zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژائو پدرو ستاره تیم فوتبال چلسی هدف‌بعدی نقل‌وانتقالات بارسلونا در صورت عدم جذب آلوارز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/89948" target="_blank">📅 19:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89947">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrn6KRY7atXQ8x46I93LhOTPuWTWQhzJL6srZJwB4mbK0A9X2kSjJdDeALvD9-_IdgslJcBRA7OMgtu9QOkgzuDtT8Apr5SwAAZDph4sOkPNxlgdiMsNSkRZfSwIN_rM-bozWWb8hWw9Pq0FO7UtKVATuubgnS5H9v4YwILeNhJf3SZgsxVPoz3maHLpw6XmPLHJevRY_0sBsJtK-WQXuSyw8gZY-lrYNq42eD3PoP_bKZfvaAGzL3f1d10aXAWNOuApetW8Dz_82ScULw-BRMpcjKrJ2EK0UqOqdBGu1wOvoKeEHgRAVMpSEiFjOW6RNGqd6AyHmr15ier0ajGTAtOzs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrn6KRY7atXQ8x46I93LhOTPuWTWQhzJL6srZJwB4mbK0A9X2kSjJdDeALvD9-_IdgslJcBRA7OMgtu9QOkgzuDtT8Apr5SwAAZDph4sOkPNxlgdiMsNSkRZfSwIN_rM-bozWWb8hWw9Pq0FO7UtKVATuubgnS5H9v4YwILeNhJf3SZgsxVPoz3maHLpw6XmPLHJevRY_0sBsJtK-WQXuSyw8gZY-lrYNq42eD3PoP_bKZfvaAGzL3f1d10aXAWNOuApetW8Dz_82ScULw-BRMpcjKrJ2EK0UqOqdBGu1wOvoKeEHgRAVMpSEiFjOW6RNGqd6AyHmr15ier0ajGTAtOzs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ستاره روی لوگو فقط برای قهرمانی آسیاست؛
تاجرنیا: لیگ برگزار نشود، قهرمانی حق استقلال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/89947" target="_blank">📅 17:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89946">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z69oiBRUje33Lm39-HT4pzdUhaRrRUq3Os8RwJjFQo8gzU0Mp4HzeZ9xGQylOTyjSZUdTXJ9ZgZoRqn7MNcVOnZa3UggQk2Mg4NQq1R0uvkR4sv7R5kCnClB5VhvPPvT9wxblsSq8T3Q75zt6f3vQ2NaphYYlVjPilx25hjfwqffMfmp4ACkAS8P8hgMWCrEIryDntZnuIlnqz3JWx_BMmMZcdJ6wowWH0-G-nwF1-VQpP_Jgdqd5gDSI4P8KBUxRyfDgC-_ClhbXbmHhq2BH4hIkhhQqVyjIFpTqV0Toa4NA1m8TWqV3tkAtIEoZlqDu2u3hoaNk9gKlY4o7RZImg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای کسب‌عنوان بهترین بازیکن فصل لیگ‌برتر انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/89946" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89943">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=vknner-KNwnkPDoKRL6lAOplvZZCHLS94OQilAoU1vyADPLDKvxJ_NW_4JUcic9y15pDv_icNokGSVNe96aY_2-_B7-luChT7Zygs7kst7Fl7NxN7pSGuCt2DpOmrzKfON9pd1frgjfBNdcWXyIC5dJkpmbuuBrCm6xEF_G87mDH8V3O_uRwvfacysc7jOi-FfVIoz5IvNHEMUNB_fEcGkZldgrwimMwyFu6SWy-BFzcNuea3cGSX-kI_Gs2qY4mo7Bnw1qjSnoIEcWv9tN_09LG3cf1crxQzq9d9ooGYK0I_fDHgJxmq5mSc_6UmMz8NPDvIoZSXw1lTWKgtDd8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=vknner-KNwnkPDoKRL6lAOplvZZCHLS94OQilAoU1vyADPLDKvxJ_NW_4JUcic9y15pDv_icNokGSVNe96aY_2-_B7-luChT7Zygs7kst7Fl7NxN7pSGuCt2DpOmrzKfON9pd1frgjfBNdcWXyIC5dJkpmbuuBrCm6xEF_G87mDH8V3O_uRwvfacysc7jOi-FfVIoz5IvNHEMUNB_fEcGkZldgrwimMwyFu6SWy-BFzcNuea3cGSX-kI_Gs2qY4mo7Bnw1qjSnoIEcWv9tN_09LG3cf1crxQzq9d9ooGYK0I_fDHgJxmq5mSc_6UmMz8NPDvIoZSXw1lTWKgtDd8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/89943" target="_blank">📅 12:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89942">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVyXiev-9vwIBPU73vnxwPslgZzuFeHKPGUKb2Oeb-FrPUKWf-5fSkA5HH7qVgOAcYKA62fkddhj5FsSh1uxdyRca180G0L7v1qvnJg-SVXeMHro8D6w2yF2uEalOw_4F6HL26yFjQleKaOR5S-E85b5l08fztSlJLPom2U91EMQVKXZ--FTKs8VGT_Qw_v9QlZgEKtnfEZqqk6CHKuBqsFhGr4Fv9F56I3LeByp0wWLK9NRxVlYU1MVwUJoIbtMT_EJxtriLAT09mnPIsQWjHPzICwyklQf66IuCXfv9CHaG5a6ZQna-J14tqNsobfFRcJCwvwq7sXPApKab7HDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژابی‌آلونسو به چلسی
🔜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/89942" target="_blank">📅 12:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89941">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTDWHDeSf9ujmbAZFDr7Z8Rl7Qll1VmfwR_hd3ylKB8Fc2D5I1C1IdMavx8Q2WDOzDgwnYd2LwqSXuLgzjqaZFb8hnyrT5LwTJGqhQp0vZdMOxSvJjiS4g8_7td1OvCzX7xiF1Y7QNG5Zad6X2X3Zs8nnxz9D8XURnkRfJO3jhE6__-nGhQjy-kMae_Z-3lM_Vi-KLHzi4D0ijWRK08SmjCuAke-gtXp_ouZelAjfV--4Q7IU9ww4LQmIUBV2my3tTfK4oujbiMI5Vv1xIsNBhwcb7-dG2KtWPbR3bM8z3AlOUnIrr3Ageeu-S5Ry8gciLl_u-_iRAetB3JdaHrM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی از کیت اول فصل‌آینده منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/89941" target="_blank">📅 12:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89940">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoVYqkxoLjZq5xFzIo3D5GeGWocxAkZAVKLSnsVRfFlM7COzv72cBzveV9JgVkonuPh4NAXIg5Wn2HZ5P8KIEVmO5zsNyCFTXC2dEWl_4EAYOJMs5tLCcgZfPUREO-c-QP4ORw_jZLWwiKkn_XaLU11BLXc9jWuLmUWBQTnBO4qGy34L_H1M1uHhAVfQzFXgB7UPXFz6ZTJiK0E6HQacWwg0GAcqJTSg0gH_FCIEgEhtaZeMvNp13BP3O8h3-6r0fFUnwr_1mJPDufSS6O5p7EpXCUlHSNXIwrbN0I_L1-2V07FE-4_5yvG-5kixiDRg7l7oxLuhDx5tjXr9Ticrbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام فیفا، در بین نیمه بازی فینال جام‌جهانی، شکیرا، مادونا و گروه BTS اجرا خواهند کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/89940" target="_blank">📅 11:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89939">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHT4A0CIomfriO9wxRV8DKTie4ZzpIL1wPlPysL0y966SMUzFIDbRMAlaNUKgOvWWxnyJti5sKfp4Wvv1XI-lfsIdyO7LBwQBDeBlUL8ZHA4WUWKg_kUAMV2ia8DWHMQkCD8aLOnMqtgFC8hehsFEzo8MmCTIyfq8_3DdpGm3__g_bAQF8nn71Y3a4D2T9ylnAv6Dz0ervCAvb1CoRVqUCBAAAFPqdhe-QrPqH4u1v3qpY2BPO6fyBVOKAGP7GZK0T_JyF8PPq-hP2vKbnAiTeI2v6BvmzXcQcgleY8lj1wHYuuD6QBSyBojf63CL3eqaL1wVq5CNAyXfHPnEG8QGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام لیست نهایی بازیکنان تیم ملی نیوزیلند، یکی از رقبای ایران برای جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/Futball180TV/89939" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89938">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fs5oqtX6yE_5e2K-tRFMXWpyIUhISh5byYQJYyx0RnfkFn_JvcBSUdwMgeelvuMuDxJBS_TxiaYO8449sMUhK-27qzAhuB_s7OBphsFRs_H8BtYefuf5yJO5xvGNUt3ErCjPrD8Q2vi5aY4T6tvBvoG-GVxdo3m0JYWD78IkKNslgMEzbE5VpnLPX9cdriOxJmw5PyylmDstQKAPTgBCnY0hppTOBreUL9iHm8KWVIDLjtfWVATGpuMIhPYUn5XpHJhrTTl3whORTRuCMhRy0L2v1d1qahBEpYeATiGhVEVYtjSlCNAeoLb3h7Ym8oqaK4bolGniyMFfvyT-RJ51oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نصرالله معین خبر خواندن سرود برای تیم جمهوری اسلامی را تکذیب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/89938" target="_blank">📅 08:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89935">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMKXlScPIQL5Bb6k1q1dlMh0Al3G2YVfAUvClTt9ySzgtJ-Jy8O7yrY5ETOiF6KfUoBfX9l_js6MYzadNeF2UVs2mJ64pR2yfAfWSD4eGxNwgyzL9OygRFaR3kYsJYe4fjtpd-tUTZAUePJqrK2szj7TrjAq44Gw-8AhUXQUm37Nbmtp4VJ-HKInoUn_fHaf6Qlhe6N1bIcyZX8_4-5jK4PWKu5qVbGWLbJUUg2dTgOgbsXQi632he8g2oGEyg0jhkI8sRw4YDL33u_qG1rLApV2Wwcp9WEkaR1ycbfZedPZGTXrWRKvapV07_KLIVGHPgnXWBRCV9ra-lryq9H-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇫🇷
پاری‌سن‌ژرمن قهرمان لیگ‌فرانسه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/89935" target="_blank">📅 00:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89934">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olEyXpojBB25ou-zKuWHpDKEVfn9gbKGjCc3sMlQ9mfgS73ir0b_etDt-YeR0hlFdt1OgnLMkXCCTiQTOnBNJkB7uWmWRwGzUBto_rPyfjjxyNlGrdMZ-ADoRHNren2yCK5PEhW5AIVNXYWilsV0hZ1k_soermZHo40lYjbp2o8QkadlesPxBpPEeUKgU5K0J7j6dCSyUBXwk7tuzltj0uxZ203wlt0voDqpkukcX0e9gZa2ZxExeWatDTMrf0jNWe9XRhxf6OtJDTZrTQVrjr-gGkfXI99NJX2s48k6_fbtUBHgXfmNOdZsiw2mwmF3iYdKYorxgrZL6giWCyTzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
اینتر با برتری دو بر صفر مقابل لاتزیو قهرمان کوپا ایتالیا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/89934" target="_blank">📅 00:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89933">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQZeHcCaBCArBh2HQNe0dy4H8VKpMFI7YPC_pL1Mlc8UqU3LOKxHtRXmHF65hlo9z1FKFIdVsWsglGLSgovFHbtG1-x2Nxxl2qPdN47inMQxr0mrYgQjziSg2W7icMGJyoqNk7uxSJWo-nNde_gD4InZLjKwSGlyVB6G66GNQ5RJ0TYaIbxCJPoqeH3ZDWN2S8pZwZIcQYvzGis4rTWIbhrKILfrrB7exCUPp4Jwk3RHsscH-tr7myViK0mPVCH5WL6_eb5KUY8rQkZEH2ZI3fLEPkyb86BGk3QJeA_H0ohDGRuR86_tk5FHW-XeDvBxSwc4d5NWxSezEkqRjyjftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مایکل اولیسه به نخستین بازیکن بوندسلیگا از زمان جیدون سانچو تبدیل شد که در یک فصل بیش از ۱۵ گل و پاس گل به ثبت رسانده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/89933" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89932">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CauOXVif7nwTtMpDhum-bWdVCm2FHTTG7fYvXkNKQnGWV2daVAL-EhrQS1xObNqHBqC29wuKyWgugLgDCfVM_GFusN_n1tUK3d4MxOyZeAkKV_bJbmBPdq6YBRfyudcKWMrVWbq_XG_KCx1_BQrXKctDqyJrAFqgBPvLKVJVPTXLZDUmY4FmExh3kcKEMpdVa3XPsul_z_xusXhFRdakFUg9_4NK4vfnHH4_CB6Fni0zE-zQ66DjeNWmocrDjwpugYsqoXaRe_3aNFVdK1S-B7ol4LI5gTMmLdhqR4eN0Jsfvl1Cx1ROVGUiHnuwrXIvCpgZNdqvGfgoIOI3YtrYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار و عملکرد مارکوس رشفورد در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/89932" target="_blank">📅 20:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89929">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
باشگاه سلانگور قهرمان فوتبال مالزی با ارائه پیشنهادی خواستار جذب یاسر‌آسانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/89929" target="_blank">📅 17:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHO-Y7_zBSP4i5eI8ZNf8m2FpmmY35S5PNEq2kzWBQFgr4ZxTnUZNUObbcnizUzOwz2anNg-6j6HCUhvn5aPrBvrPEwU_WPSyyQqcHhVKOVUayNVPhPQuaxMsX5_VP1t7WV19hQSkssmrHFLNu3_Q4LfGQm8UY-rXzDYvFUTeLJ_STI087w1UDv_M8Xs-H8JMzKHa9Ga16DgrB7bqYuU6g22F5jWSWIGNbK4EIouWBBOii-IyrLmuXqciFNbqYEKstKVtRa4HenWj0c9krqFe66p9lJyU6xvzr74XEv64tXwXY7IWV-Lb6wFM4KXyiOmalN_ayu0xA0P7jIt4BKsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
اتلتیکومادرید پیشنهاد تمدید قرارداد با افزایش دستمزد به آلوارز ارائه داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/89928" target="_blank">📅 15:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mom_5r8JMW4zFVnGl10blREkcjNt9S0OZLU3vFR22LqvN3BZF0-jFjgVtzG9qfNJg7O8GChwl6q12klm3aZnnAZ2LO3uyykvYWLNINOZSOARWTuysP_DYHjzon882zBMzW7SKrbrMiWwA5xOaSxcMjVPjqgDq08w71OgmeXOocSfb7ZkbfcOJVOZ9mrO9RUeOxu68DKIXtPVVvjsffgeIeu0K3TyAIZUH9kC1bsB3gFOaGByRt7ztbwh5buKPNtibZXR0fh5nTdBYp9bNhbwvpI3o2OF-f8LWLcVpKztM1xN8oH4sFHvZruOY7cMNCtUqL7bfzIMixPU7qhGvuU9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
باشگاه بایرن‌مونیخ درحال تکمیل قرارداد با آنتونی گوردون ستاره نیوکاسل برای فصل بعد است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/89927" target="_blank">📅 13:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=LhmMRNPfsjtWvyUav5TexuRaCs7Tk0zYZiE878eC5RB2xkco6_67tod0BjzQwt3V93ZvQdrAj_fYceSjWKjWSw6WfugVCekGeoisKYUlj6Sy8Mcj_nMEgai4mxkoywrDYzF1BMtuG3VRRiLHICbKiXsk_X2b6C1jT5b9N7OTAfPZHjGdQsQDFu5giB3mLLpgx6HkAgsQuuvV9_SZrIAsQ1CNZ8ECL7id2sMMOG1r7SgvxJkzfDulpjeMmJVHexzOKnHS29jltJ3lCSF8gl4YezTaaWbpf6VxQSJuT4cMqd-2mGDlZUV0YW4msJ_Dse1r6AjsZ2truldrGv9S-CMfOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=LhmMRNPfsjtWvyUav5TexuRaCs7Tk0zYZiE878eC5RB2xkco6_67tod0BjzQwt3V93ZvQdrAj_fYceSjWKjWSw6WfugVCekGeoisKYUlj6Sy8Mcj_nMEgai4mxkoywrDYzF1BMtuG3VRRiLHICbKiXsk_X2b6C1jT5b9N7OTAfPZHjGdQsQDFu5giB3mLLpgx6HkAgsQuuvV9_SZrIAsQ1CNZ8ECL7id2sMMOG1r7SgvxJkzfDulpjeMmJVHexzOKnHS29jltJ3lCSF8gl4YezTaaWbpf6VxQSJuT4cMqd-2mGDlZUV0YW4msJ_Dse1r6AjsZ2truldrGv9S-CMfOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در ایام‌آتش‌بس درحال بازی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/Futball180TV/89926" target="_blank">📅 13:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89925">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9hhjMEZDN3vml78Py72wATSa18OvQ4ppTA6MZSW70I0bAUnCLqT22S94TM2YL4hGLfGsRqLs4WmEMZ3JEH2DeUcc_z4KVr_3c4nQaBrH_9hDejOwqRNPzPCMV2yAkxx8upzidmzcfwXjEU9LL483Pdpy5AF5v13eSC5EVHo7yuhVwl27DxtIbJ8IYkf-577QphagsDJounjVRi6D0JL0Urcmay_OmLms23iI_Qa8RDXZIYbuA7k4vR62OE6bkK56xx2gnRJiSbkjFlJzp9mf8uzZzvNuoc81_zNIhsnMc-mj1yWFJvIF90AMHQnww9Jb8Qt11Gvq5_2Fgv3df7vDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
برخلاف اخبار منتشر شده، رئال تا این لحظه اقدامی برای جذب رودری نداشته و این بازیکن بزودی قراردادش با منچسترسیتی تمدید می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/89925" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89924">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO_eIMIFeTS1KbCF6tAHl5dIgCEvCjf5Vf2sGouS3cX8zTeGR0lVdj32e5KjD3SjOIfupfcEJkuawNc1kSRrySvGJVMdlQKHBiV1ZcXO4Ka-3yJM8VSA5qzNUJzkQKRmYMN3aC1nDuotpieoZtKoLtZjFVbnma0BiBab4JIyJNEhOc0KJh1wyZMljRDEZ_HIIYT00K--tbebBpSUdk1haMy3iV59443bdjJG1XdBIbEpELkV0dzeHSXDVDI-f5CRXkLHeNTwhJQp97GfQz4NmZMOy8kNEvyNeiv2Rx2LsbWhrDoJF_UG574L2QHWdvUo2Np7Zbq7W_SP4zSgmsUloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
یک خبرنگار مطرح لهستانی در خبری فوری اعلام کرد رابرت لواندوفسکی پایان فصل از بارسا رفتنی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/Futball180TV/89924" target="_blank">📅 12:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89923">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-ikDwPG2DYta4zO3ZseBf5GpeYlb1uUfnVknZcQfdkAtl9SUpGmhxCYuu-uIFYR9bGkAqo1q24fIs91h0Cz0YojhJuS7mNanzyZvVcH40xruRpiFJ27Tt6vS9hAlxf35IDuhEA4JY9BTznLIZxAi03bzJwqql2D-iGAgBgqjfqoYiy5WBcErhz8O4BNblPHxar5j6dwmc2o1MvizMVb3I9eoqL-TRDlAMOMpoaE5_-0FK7wEOHAV4GGWqFhRX-I1QJKDnxeWtvPS3m3SEerDWxVSPv2ieF37ot2mUuJ7e5w1ibTqIV_5rJZWIh63mJt7T1hNCmEst59IjC3rgmarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: قرارداد مانوئل نویر با بایرن‌مونیخ تا ژوئن سال 2027 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/89923" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89922">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyRkq7rk8_6srQ3TCR-xzTiSnnGt__s_7rk7cksyGJhJ1DEWLIAncqRAuvaibZ_gtMiONjQBvsr4tyWqX5SKC2ZrJb01WWF9c__1eDmkJyTYrQVY-bOD4wW0cOvJnSD3kv7pJTxJqV3XwCAJpKPTLreMwvurjreNbwLIICm884_Bb_IrbQ1hLKPZ3daswQx23FVHBWx9VODeKwR6nlgUHHt-VcZOMr1fpftji4IFvfp1YovvbMulTS8Yxo-px2MOXgYKakS0X12nCFmsq_vBfs5hV0dt5hrJF3SK33Os0TDVEOOZREJBKS6X1S08NrIEW62meacPvjodtgRHG4jL5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قصد دارد برای جذب فده والورده از رئال‌مادرید اقدام کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/Futball180TV/89922" target="_blank">📅 12:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89921">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjIYqhGJlz6pw5HcHNeiQMTNkBn_HfdxX7CMIwf8g3m6CXgneQrtXCetPjCdDTBXVnyKWlLYoQM4Jy914_xQ8VQAssp1j1OwhmQK0ePmxbTECzmMxRpBC3spk4r39FBp2WrOQnt82Hf8r9X0UZG7LIxc660bBHW9at8epHxkwdd19PMlfT5OCA3iCyAkHQUKYOe3lElHEyQ5RnyKE4Br7OVVXv_k-rZ22FKQU7_as6-guEPz988PZDBzf57MG54QFHb2bIVD8dXBpiJF2R8lrY4OGsGfiZwHm9mm6HYQ9D9j9gTPv84u4HH60JJXeKCFR4MT4wYWF_-ZZKGVXI7vBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
فهرست اولیه تیم ملی بلژیک برای جام جهانی ٢٠٢۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/Futball180TV/89921" target="_blank">📅 12:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89920">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjQoId9LHEvMsuBWJC3307OniKewWmZtSA3OR5CQ9-iDp1cpto-YRtuXX2s36d_xc9OnMhLa_by6IFlgBMYUhiePFAbs6L6_5ZakLMJL55wn31uUhjXFzsQ466MtbLPXOo0pbHSXr8sApvMxxMKAy1QNdlXFb8yALM73i0_emugt4mmtDipxAi1hrmchEwi8G7pr7UrJpIDvoYhB7JYiNQgpJtUrP1VPPhL4NdMc7Aa6mDWCx1QtDIluxrRfWgy8B8cGvgVGaJekb5Br8Mgk7nlRwPwqJb53LGA1i4w3M_PUHhlkyUKpogYxHFa5_yYlGX-_ogrZJD6u9xYRyNiT7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پی اس جی مذاکره با اتلتیکو برای جذب آلوارز رو شروع کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/Futball180TV/89920" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89919">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89919" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/Futball180TV/89919" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89918">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN38bDy9wQePchybNDNz-EAwccoskBzkvjsAPs0wz6QGGHKvzs7l0G7uM6RqRqxtQjomUgh8QlCVC1K8wg4biRauu_O3k4z2e7IvSYnUahc4eaBOxSBGck-k_DMhoMT5Umim9-nFXlhY1N21-eLHfVTH3KNciweV87sqbFCzLW5TNp0rQdANVXIbzK3S0sdhTJUSxm8QlnUBNPgan6ILkagyfRDX_XKkDxSXPvIPqbT9ILjCElAwb0wwibc4aHJbZHkSpn8azIwJWrnfm3QCD_MWEzCCcrpS3B3JYMCbWwYj4fuammo2RT9jmxAReeMIndPIz_-NMG_ZiSAVYuNlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/89918" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89917">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇶
آمریکا برای جام جهانی به پنج بازیکن تیم ملی عراق ویزا نداده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/89917" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89916">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=atEt7_fayADyO_Xw53kKl56dnBXk6b9dsiTGmujB092YZyDT59lVrMuGJI4xL83NkjnJxMuTUA5xtE0dag8AwEEOjtfGxODm0lvxly0DduZ142LYkT7q2Vgu8WK7EoQkRg8Hn8hwn4uj2LjAUeS5LjBh_AjRmmtbLipOEfNufwO-4tSf8qGoi90QJyU31qT0eLCr7JIveD1_WldRqoMcbya_PPw0iTxQ8H80jdifPbmdxkAo5-pYk52vJjTAWny02WWyIBF7Kk1lqp-DFGN2kh6_2zLtcej-MXG2FkIvCdnbAMk9TH_hPbOxTZ6NiPt-_B8eAnDCz08g58d7QS2Ftg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=atEt7_fayADyO_Xw53kKl56dnBXk6b9dsiTGmujB092YZyDT59lVrMuGJI4xL83NkjnJxMuTUA5xtE0dag8AwEEOjtfGxODm0lvxly0DduZ142LYkT7q2Vgu8WK7EoQkRg8Hn8hwn4uj2LjAUeS5LjBh_AjRmmtbLipOEfNufwO-4tSf8qGoi90QJyU31qT0eLCr7JIveD1_WldRqoMcbya_PPw0iTxQ8H80jdifPbmdxkAo5-pYk52vJjTAWny02WWyIBF7Kk1lqp-DFGN2kh6_2zLtcej-MXG2FkIvCdnbAMk9TH_hPbOxTZ6NiPt-_B8eAnDCz08g58d7QS2Ftg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درگیری هواداران الهلال روی سکوها در دیدار شب گذشته الهلال مقابل النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/89916" target="_blank">📅 11:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89915">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zfnp6Jy59_uciKI5GfRKYwEUcp5vbRYO6g1vL1vIbiwMjnJoDxLNK-rythD3gMu_-qX8gU3pf41Jk_flGrGLsSU-nNeaobZsiItlL8YtHFJlkBS2l4x0J8Qocpck0c_PbK99hUOrvkd6QFdbDjLE9iDhEw-bDJECXHIU38tImjtN9Huj3KcqMLB7a3Rukz_VulI0yHXbCLZ7e46i_TUZu7S9yXVVoX9ovUxnF_eoO5pXi1cDzPAAq2tKOpZkVA9JtVWF8hjTu_sb_dss2-x8NVqAtWSMR8tmm9DK0uAwgIUsooivfTstfGqGKEODOn7pwlpxsLPOO3FJ3IDDjKMiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با برد ۲-۱ مقابل الچه، رئال بتیس موفق شد بعد از حدود ۲۰ سال غیبت، جواز حضور در لیگ قهرمانان اروپا فصل بعد را بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/89915" target="_blank">📅 09:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89912">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حمله پرز به بارسا:
پرونده نیگررا بدترین رسوایی در تاریخ فوتبال است. باورم نمی‌شود که هنوز حل نشده است. داوران همان دوره نیگررا هنوز قضاوت می‌کنند. آنها هنوز بازی‌ها را مدیریت می‌کنند. این غیرقابل باور است. بارسلونا برای خدمات نیگررا به مدت دو دهه پول پرداخت کرده است و این داوران هنوز در دهه سوم قضاوت می‌کنند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/89912" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89911">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
پرز: رئال‌مادرید مشهورترین باشگاه دنیا است و سایر مسائل خنده داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/89911" target="_blank">📅 19:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89910">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
پرز: با هیئت‌مدیره فعلی در انتخابات شرکت میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/89910" target="_blank">📅 19:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89909">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
پرز: دوران ریاست من بجز امسال با کسب ۷۶ جام همراه بوده. هرگز فراموش نکنید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/89909" target="_blank">📅 19:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89908">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
پرز: مثل سگ صبح تا شب کار میکنم(جدی)
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/89908" target="_blank">📅 19:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89907">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
پرز درخواست برگزاری انتخابات رئال مادريد رو سه سال زودتر اعلام کرد
دوره فعلی حضور پرز تا ۲۰۲۹ هست ولی او برای نشون دادن اقتدار خودش امسال انتخابات برگزار میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/Futball180TV/89907" target="_blank">📅 19:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89906">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
پرز: متاسفانه استعفا نخواهم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/89906" target="_blank">📅 19:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89905">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/89905" target="_blank">📅 19:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89904">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqLQo3hl_6LL4LnL86Pl8pZh2kaMXTS7tTOhBlIuVOxM1xWVku9fX3IqeWnkjV0lnwCE5hCf8UpKf96n1Hlaw9DsAzjC2kJULMNIQNEmuX3p8EgwFNsJ-dqb4QpFQQ7lMmy6Z6mIvSCTEkRPfeJ4aQNZSGCEKu2z85KYcliWm5wTbYgvW9oMFYI0pV4VucJFGoNErmKICLQUyR_MpmLSeM447EXoYh4Cso805tWY5XYsU99l56oVVe-T47Kb6WUdXG9Ikdb9JPW1X2qsMj2ypmGgtzV0CDwjH0T9PGeA8NuK1nOD-2RBJxE8P3d6PDEA51GqIIje4RqdHaYdon8MhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/89904" target="_blank">📅 19:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89903">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kv4reUyaexqli8zv4p2VVT6hUYHYuH2KQ8tl8EcFsgnPr6wq29lYo3dNEVO8pfiTXjtQOr41YirAcpkpMKW-cxBvHqnGv5KlAgsyeRa2En8T5rsOvYmIwLabitqwq1weYZQyx3WmLYRKRR2IT5ZEEUBualry8OU810z5z2MGoYjkaVgEfNG1e5ukftSFu5emsiZxYu68MxFsbBNxiDkCjyZMbyzDQGTDDoAc22i4g52pnL3qKAyGE-sNG7n2ajnfeFyoeobR3SfIdrMeuPlJmNMUgx4NviMh1P-spJi7J8vQnJoaSYK9cFJhQCqCQefb0L_tC7t77uK-E7-SRjbYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو راموس باشگاه سویا را خرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/89903" target="_blank">📅 14:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89902">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHMZOooVgiucjusVhCguYGNiLA0F1iNehALy01ArHjCQVNCBXOGA-ONc0VQIQXFk1mPpSH5sWBmtLMqIgG0o5j1P_5D28k1U9617LyPrDqi0VxaEmZcZVJunIKpG9FBLozAp44qtEz7B2kYjXStRDJH1rNgdJJlgD55_zKaJFG99-6dGKUl3bKT8u4w6A_coCMYXGJU_CFaqc-bxd5crmqtBdy5JbFcuaneS-0JYVUqiyjUUlhwMkUIaOVg8XiBnWiZaw6F4wjVEvRUCX6bB3clhYXxB77Rw4fGmjAngYJ6WokAovRLHhobS5jx_ftL1FoPbkMvfm4BBDhkJEw98Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
لیست اولیه قطر برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/89902" target="_blank">📅 13:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89901">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddXnhLVm6YN5gxMuczGEVbeAYpIOCGiwKq5X31tozVfmoIDRQDNfsn14c6D3S-jGCLIvsSR_rLYMfVLetYYuu-KPwN810a4dbKRZT9B-zJPSXFOygzVd84rcRr53mO1gw4Id4ewCXfyIhYvfdQM6ZqswRWm3oGqKOpljEt_igBXfpu8UwKlEkAj9XnFHBK91hlld2IE0LuYV2WO6W-d342Jy9el7vkJPHCdMSRb9Az5smOer4hCAFVcAHNjKS2OPnpyd_OBUJhzajb44mG3xTHx3CuwkmyOgaD8UO1rdi72uIT97_NswJbQU7m5YV0UvUg0rPbKLpF-h3kmFsUkmLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
پیراهن اول یوونتوس در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/89901" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89900">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEEKtcTpKOSgiEjQaCG1YrOdbXl_Yotp5B6aQ0LhTE3gf7o05r8eFOk0KAjQdKuehHpj66Y1Cx35qmfNu1SMFGGy8kvTnp0QWDT4CIOpRv1nUaKG-EhYe3AUpn-LF9MwRhJ_X1PigwYvkoUHgQRCedPaU9fR-AXAiey5NKUh2IO-r8k9W2OvDq1YSAKh6JeQc474mTaSGL4CwsFsPs6A5x_CMZV6fF1qgWyLx1_Sm9iM7DvpJ4i_Jmf2kQSorKKqJ1G0pMd9rXJ2kSImf3BAJHPDdejF7saPErjj_0xTYKt9gvkvzuOFTbOag1gJl7kJJN9QKCafMNXp2nmIVcC_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/89900" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89897">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-1TR6O3lTHM-tU6UGVnjHV5eZnEp9QH8QAz9qMc-mD6kuLhoDmDlppD2zA2akVM9ocFzJpbICuTgydSIc60e82TIqO3270mhaZpD4r8AI8JhvoUxUwCWIQnfFPiQ5Qt51016_iOnXUcvi5j4mMm4Tlo-u5DN5ZPS8pCbWychi1nBj3rREo_Tmf3BlT_9V2f1WlG9RqDFSx76Ql-4rbDP3EY9md0oq1CJ7dT4eyWjNNqObtuV0DyU6TfFtTc7YmQxQhEPaL9hxJX0eKk5NUet4sCW7GFfvruuuN2cIZ0mu713I4Ry9dU53ohczba4TrK02kPBW1wsOaiXNb-3jKtug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/89897" target="_blank">📅 11:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89896">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQvGUO_7nRnr6pxmZdJ9ZIrKhXmzgfladyFkS45cgb4QCyEPPFHxYUkPgJD1Eeqr15UkyjCnlMfCYi43gOQ3TZSOY_aYDkdzG7rZE1_QusYlLwr6H9SYarqLYM2jzhPuqsmMND-S_AIvXaoOkuO1-ltwC8SCW8Te-3dRaeS6zyZp8uLZS1PtfgcBT5CdYTB0Bo7qi_UD0su250CGaTNc8JTt3S0bKVm9KtlYD3l9AbkHgp2sPXXGA1MARFP7kCBDZjUBKOVOvfqjHxbq3-Pi0xYSL39GK3NgMqBoRV3p-bSHVxJx9dIkH1rnL8osVAf9p7IkDHJydQWb21i2ODSh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسانه‌های اسپانیا: امباپه خواستار فروش والورده توسط رئال‌مادرید شده است هرچند وینیسیوس و بلینگهام شدیدا مخالفت کرده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/89896" target="_blank">📅 11:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0WEsOJiuLPLk2FIVO3VJwfAedQQ-8gQgq4U2xfH8hbikb67RGSyQ166brvUgFGAkmv5OjmLi0-l-2AorsFbl58UajdgomtWsJb_9YFdr4po5N4sooFCk0yuRO8CVsTVhg4LQu17I4NC7dKEAfnqjBdQ612gy0KFgjaQ6JZEp58Yg507D3dtDY_dAzBg3ER5tCdFaOd6tZIC9nYUCMFxUNHDA6SvSnM5-yL3K2yiitd6_uGMiUqc3jmxKm0yUuxmharBCRIaufEzyPPNNJ8DgoqypGL7rpNY__zoFOslaYmUAFkJHepkRGiLF3PSA5tIflD_MlwTV49uWL4Ggs0B3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نبرد حساس قهرمانی لیگ‌عربستان
🔵
الهلال - النصر
🟡
🔥
امشب ساعت ۲۱:۳۰
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/89895" target="_blank">📅 09:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89894">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=CEhKhOb2uH5s2yZAY9_GfK_Sv4V5cz2gl8m32cTAKpHWlU3EYFzSJXimcJScFLvZUfiqZC2sea4DObxiM1M1CWSdkQuuTJ74AaJiq8ewwh4NYKDM5YBaMD6tRcNc3mrjWB7w67jtSzNW5M4HhsWhmofukNSSl8NnUWkiy33pZ9Ic60bR7WDnuDmnysmFREOdyM-BDVUeY_OKCOlFP7cGN_M-7VpvuXYcXVmQRZm94CssHuKCBfqOzRekUF6Ldhi17Vx4eBIKkb1jv-tgVM1GgDfI0pROSmUKCEk8OpmD1G-DzCNBItDZ8p2kBdWTLNhsMUq5QY8apb2aqi_Ar5_EoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=CEhKhOb2uH5s2yZAY9_GfK_Sv4V5cz2gl8m32cTAKpHWlU3EYFzSJXimcJScFLvZUfiqZC2sea4DObxiM1M1CWSdkQuuTJ74AaJiq8ewwh4NYKDM5YBaMD6tRcNc3mrjWB7w67jtSzNW5M4HhsWhmofukNSSl8NnUWkiy33pZ9Ic60bR7WDnuDmnysmFREOdyM-BDVUeY_OKCOlFP7cGN_M-7VpvuXYcXVmQRZm94CssHuKCBfqOzRekUF6Ldhi17Vx4eBIKkb1jv-tgVM1GgDfI0pROSmUKCEk8OpmD1G-DzCNBItDZ8p2kBdWTLNhsMUq5QY8apb2aqi_Ar5_EoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی محمد قربانی برای الوحده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/89894" target="_blank">📅 09:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89890">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=p6SZ65AAV8ktLJawzSQI4nbziYtrkubANZUAodMXHZU3VxObHu0QO9KzJ7l-coxS0iC8llGDrSHUs1eTxHp3KGMPbvTYXinEFsGw3acSwWBcROdp-RV1S1zrhIbfcZTjiGqGbXb45Z5HBaWVWs9zAJhyklV3YXTt_NsKbexjkbExwWLg2R21hTVFAYXhTrxPDo4-UnNKKszNgagElUIgwxK2QmGsXEk-52F2nJlXGFpQu4BPyuKisEihGFGWg0u81w2UH6R_SZchVU98n0JG5JwmJTrlRLNgksglLm4uAAhGCxn56l567yZuquJB_NishZoYKcB2Du3KrHGG8PVpFLzbSOZ9yiZkNtO1PPPlKPAeLIInfEUhZW_dwJHymSkO4zW5CU9TqQq6t60vzTcN9nth8y9_SmoCdC0lK0SG7HmtLQ2mXwGLGvZk-h41pIAnMGl94PnA10Bt6nBQ8A01QyNixGkCFG8EEddTgt8HzVSGbvW7Lin0qP3zTiKk7LcL8ogw4xQ7Eeq5iI0fhq6ed5lkmze1fs62iXrwN3ecwan5DbE03hylthSW-Y26dMzqrOWpwf4ZMLFy9xYVtlB8Ual4jQDv16XIE0pA6e2LBRKEp5oIQQw8Y9B7WhtzR80OI5qmHHdI7YXUF-1y0ZWAx6e6Rf4xXpVf0md5n4PURs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=p6SZ65AAV8ktLJawzSQI4nbziYtrkubANZUAodMXHZU3VxObHu0QO9KzJ7l-coxS0iC8llGDrSHUs1eTxHp3KGMPbvTYXinEFsGw3acSwWBcROdp-RV1S1zrhIbfcZTjiGqGbXb45Z5HBaWVWs9zAJhyklV3YXTt_NsKbexjkbExwWLg2R21hTVFAYXhTrxPDo4-UnNKKszNgagElUIgwxK2QmGsXEk-52F2nJlXGFpQu4BPyuKisEihGFGWg0u81w2UH6R_SZchVU98n0JG5JwmJTrlRLNgksglLm4uAAhGCxn56l567yZuquJB_NishZoYKcB2Du3KrHGG8PVpFLzbSOZ9yiZkNtO1PPPlKPAeLIInfEUhZW_dwJHymSkO4zW5CU9TqQq6t60vzTcN9nth8y9_SmoCdC0lK0SG7HmtLQ2mXwGLGvZk-h41pIAnMGl94PnA10Bt6nBQ8A01QyNixGkCFG8EEddTgt8HzVSGbvW7Lin0qP3zTiKk7LcL8ogw4xQ7Eeq5iI0fhq6ed5lkmze1fs62iXrwN3ecwan5DbE03hylthSW-Y26dMzqrOWpwf4ZMLFy9xYVtlB8Ual4jQDv16XIE0pA6e2LBRKEp5oIQQw8Y9B7WhtzR80OI5qmHHdI7YXUF-1y0ZWAx6e6Rf4xXpVf0md5n4PURs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درخواست صالح حردانی از مسئولان برای معافیت خدمت سربازی ملی پوشان فوتبال ایران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89890" target="_blank">📅 00:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89889">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=f8Uuf1loeKiWJnhrj6y0YBfuyEiFzQ8ci793Qp1AQeyv_LAHYv9yRrbKy2yKgmgsrfW3ZZQmHkNj_lzx8XBGGg81vbeJYFlDiMwPPbeiTO32L4NhIgI2wwODMvu5RmCOz7ADaHX9mAaRnhC7-Rm-f0SJKp-g2MRd5kFVFv4Hki4A20nEgiir4KL7eBetd7Nlk5mfth1SniXiyBZgKgT-agPYix-m-Ue7wX8tvZWL6BTOwPKz1DKJkx64caR7uU-eH6gUlNaoKCRJLZaN627QNBDskDxVQH7kT8gRqsUxu8HWhex8DPIatm4ki3cx-PnBipE1PugbfEjVVJnZ-1hTWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=f8Uuf1loeKiWJnhrj6y0YBfuyEiFzQ8ci793Qp1AQeyv_LAHYv9yRrbKy2yKgmgsrfW3ZZQmHkNj_lzx8XBGGg81vbeJYFlDiMwPPbeiTO32L4NhIgI2wwODMvu5RmCOz7ADaHX9mAaRnhC7-Rm-f0SJKp-g2MRd5kFVFv4Hki4A20nEgiir4KL7eBetd7Nlk5mfth1SniXiyBZgKgT-agPYix-m-Ue7wX8tvZWL6BTOwPKz1DKJkx64caR7uU-eH6gUlNaoKCRJLZaN627QNBDskDxVQH7kT8gRqsUxu8HWhex8DPIatm4ki3cx-PnBipE1PugbfEjVVJnZ-1hTWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین یامال در جریان جشن قهرمانی بارسا در لالیگای اسپانیا، با در دست داشتن پرچم فلسطین حضور یافت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/89889" target="_blank">📅 22:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89887">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksL6mqcRLUkdTBEwtCyQr4HPb7wLCgX7cBHLtAmWGP4a2rUEe3iAPSwjzbbyxHqhDrx-ZYYDjzmSeixT3hV13OUfi51z3f14mskZRqTBnNL3zHRp3LDsIXwMD4wH5YZrj-Lh8Z9aSJq7X2XDstFxCo-gmFZJt76E3mN5iCKV7Lo538M5IQNUOT7BlroZNQyNlF8anUP9WmIjIYza6Y0Ej2BIiawg6_se-RuuUJfmgda6u5bxKh5qTj01zLnfzYBVyoldUmlMpeLjUJT93y8lHTt7ApdXX1kLGkBoa7F9qQR0FKbxqaS0q_ExPJUJ5nQoS4UBBY5_nlUHjmtGcWUqPsUc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksL6mqcRLUkdTBEwtCyQr4HPb7wLCgX7cBHLtAmWGP4a2rUEe3iAPSwjzbbyxHqhDrx-ZYYDjzmSeixT3hV13OUfi51z3f14mskZRqTBnNL3zHRp3LDsIXwMD4wH5YZrj-Lh8Z9aSJq7X2XDstFxCo-gmFZJt76E3mN5iCKV7Lo538M5IQNUOT7BlroZNQyNlF8anUP9WmIjIYza6Y0Ej2BIiawg6_se-RuuUJfmgda6u5bxKh5qTj01zLnfzYBVyoldUmlMpeLjUJT93y8lHTt7ApdXX1kLGkBoa7F9qQR0FKbxqaS0q_ExPJUJ5nQoS4UBBY5_nlUHjmtGcWUqPsUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: من از کردهایی که به آنها سلاح دادیم تا آن را در داخل ایران تحویل دهند اما آن را نگه داشتند، بسیار ناامید شده‌ام.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/89887" target="_blank">📅 19:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89886">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=ZyfE-fQ8xPRRW1CQMkYN2GezY5aSrX06rsSBQWJf8Ag2swwuGJTXzEnlO46wM-GczC4QTJ1UmAmwWxHAvtRlK1xfmvWWlpNBfQOSdKIuomFA33Tza9c-ESEVmYuAGwCe1B7WHHnRXDXBbUHL7ARf13XYKdCFrexgQWWiN8IM7h9sRj69PfTQ-wZxHpsVWkGHExvIRShSMi4vBRgMjLcwkoiubdnDSk6N0MsiBKVNQnhVHoWmKyNX3XiVP1OPrnJtHtDRwCu5pn9DDyQkl932f7oj5X8H51lS3_S-UsMvfAvU_zS6f3-heXcl8hlfdvPsko_XFx9iT7W4k7ZvSQhxRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=ZyfE-fQ8xPRRW1CQMkYN2GezY5aSrX06rsSBQWJf8Ag2swwuGJTXzEnlO46wM-GczC4QTJ1UmAmwWxHAvtRlK1xfmvWWlpNBfQOSdKIuomFA33Tza9c-ESEVmYuAGwCe1B7WHHnRXDXBbUHL7ARf13XYKdCFrexgQWWiN8IM7h9sRj69PfTQ-wZxHpsVWkGHExvIRShSMi4vBRgMjLcwkoiubdnDSk6N0MsiBKVNQnhVHoWmKyNX3XiVP1OPrnJtHtDRwCu5pn9DDyQkl932f7oj5X8H51lS3_S-UsMvfAvU_zS6f3-heXcl8hlfdvPsko_XFx9iT7W4k7ZvSQhxRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😄
🚬
شزنی‌همین الان وسط جشن قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/89886" target="_blank">📅 19:13 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
