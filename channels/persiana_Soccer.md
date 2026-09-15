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
<img src="https://cdn4.telesco.pe/file/pMrgRbT3mgH68o5QK7N0rlCkGX5a4mxeDZgpZSTs5zhOn-cUoLRMrvPpUd9tNWuu6r_LgEF7J0yYGPo_8LZb7jbn9RztzGPE9P3LCFPzVzgHkIwxbxe3Dv5xlnHjT1p0gGWcoSPO-MaFd1KH4FqeM6j9usksFrIAKCn56KIBdMQTJAhJ-ddmfH78cBlrbjJSsbNVPBTZIo3UhRk5GUol17a9uI-NTX3-Ooi9UOZf2MZPPAeDm-4eyEJi-KVEhtOfrF2VoKqvvFsWgtW5grP26lwakyuRO5QD3D4Yi3HV_VOL4kYA2qWsdq_AbV5CPoPlsXSlaJ1MpvpI7rhj1pUsNQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 508K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 23:14:42</div>
<hr>

<div class="tg-post" id="msg-29835">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=GEYd0SI8k6nUlVwbAExMV5taZN8TLnmbuuqkp3B5KbmQsmcYVMqwXnRs_9OvriciEYGY-hMn_XE1ZLVdm86Yp1sECRswYLxO7s0fCeMeDodM0CgC0zEYwlN8aS00dLmEoaHqR7R3nAFC-3tdQxYS2SKCWb_AGYlRqK868qoGtiAx7BFY4w4A6q49EktWStfGjPPR2PUusQcYGmp3Flxm-e5muhfgkOj-tBbnJw_J_99xBYJhzsfw55n75C06cXsHIxql1Aj7GkMBkhe3El9Uz_Cqqwjr_c1EyCEwAqfSnq0fzRgdgHbWiZNWvbiB4_rfrsv9OZB1WFT45zhfWLOo56j6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=GEYd0SI8k6nUlVwbAExMV5taZN8TLnmbuuqkp3B5KbmQsmcYVMqwXnRs_9OvriciEYGY-hMn_XE1ZLVdm86Yp1sECRswYLxO7s0fCeMeDodM0CgC0zEYwlN8aS00dLmEoaHqR7R3nAFC-3tdQxYS2SKCWb_AGYlRqK868qoGtiAx7BFY4w4A6q49EktWStfGjPPR2PUusQcYGmp3Flxm-e5muhfgkOj-tBbnJw_J_99xBYJhzsfw55n75C06cXsHIxql1Aj7GkMBkhe3El9Uz_Cqqwjr_c1EyCEwAqfSnq0fzRgdgHbWiZNWvbiB4_rfrsv9OZB1WFT45zhfWLOo56j6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
توضیحات‌مهدی‌زارع ستاره‌جوان پرسپولیس درباره مصدومیت‌عجیبش؛ دیروز  پزشک پرسپولیس خبر داد پای مهدی زارع در تمرین ریکاوری امروز طی برخورد با یک جسم تیز پاره شد که بخیه زدیم. زارع امروز خودش در استروی نوشته پای چپش به شیار تخلیه آب گیر کرده و اصلا هم جدی نیست.…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/29835" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29834">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=VGZooCC4DyoOHstc-kG5QWDZGLTEOJFgZ_xUXjodeTA_NSasdhzGu8d9CBHSxyldWHCTeAoWuV6qI1-iyPXb8sSK3BPL9mvvoYPFYyKFpyC5sz5DovUjORtcG8BP1VQTJuyagfy3gwbEniqWc_5RrUdz-hrf9T4hpp1fNm2i_S5lWMkimCr0xwbX7HqBMTykv2kZtxGJSA_Av2qVyMsJ66fVEWn65KliRjNZLjErLv___hehLwHBL0PRXNALS35ZKoYDlbPRhmB74JytVC9aaM51coAx_to_GqSlkVyHtyl-_35HMux5RUMry-A18eivfO04p6LsbF-AKUx5Q0fUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=VGZooCC4DyoOHstc-kG5QWDZGLTEOJFgZ_xUXjodeTA_NSasdhzGu8d9CBHSxyldWHCTeAoWuV6qI1-iyPXb8sSK3BPL9mvvoYPFYyKFpyC5sz5DovUjORtcG8BP1VQTJuyagfy3gwbEniqWc_5RrUdz-hrf9T4hpp1fNm2i_S5lWMkimCr0xwbX7HqBMTykv2kZtxGJSA_Av2qVyMsJ66fVEWn65KliRjNZLjErLv___hehLwHBL0PRXNALS35ZKoYDlbPRhmB74JytVC9aaM51coAx_to_GqSlkVyHtyl-_35HMux5RUMry-A18eivfO04p6LsbF-AKUx5Q0fUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/persiana_Soccer/29834" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29833">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=PGCTHdkU6apsmgyX18_5WTqOBUpDBa4hos5w-8bho6XF1DyOGvHHxQj0XsPdfpVq0zQ7wiOcxqEJX1P7A0XnI3G0_74XsbRER9DPq6OXce6wZBxokZKt41BRDiUTNGWbLTqW_RUOToWfWPd80XTm_6y6RyVD4y-V6FpHl7Pb6X4lAW3wV3cSlZh0foT6tOivn6udrqp8kyjnZVLhK00yeNnpOn1AbiKsyp_5q3iaybtDUMEAdBV-cwNz7mgYuwmA7s7b2KXjJ7H3K9iXNDduFxssk9x1o7D4H0BwfuZhtcLO-8RiaUju8qZ5X3Ch7zPC1JwxqToPU5-Kgx_PlLqVuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=PGCTHdkU6apsmgyX18_5WTqOBUpDBa4hos5w-8bho6XF1DyOGvHHxQj0XsPdfpVq0zQ7wiOcxqEJX1P7A0XnI3G0_74XsbRER9DPq6OXce6wZBxokZKt41BRDiUTNGWbLTqW_RUOToWfWPd80XTm_6y6RyVD4y-V6FpHl7Pb6X4lAW3wV3cSlZh0foT6tOivn6udrqp8kyjnZVLhK00yeNnpOn1AbiKsyp_5q3iaybtDUMEAdBV-cwNz7mgYuwmA7s7b2KXjJ7H3K9iXNDduFxssk9x1o7D4H0BwfuZhtcLO-8RiaUju8qZ5X3Ch7zPC1JwxqToPU5-Kgx_PlLqVuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
درهفته‌اول‌لیگ‌نخبگان‌آسیا؛ العینی‌ها بادرخشش خیره کننده برادران رحیمی توانستند با نتیجه پر گل چهار برصفر یاران کریس رونالدو رو شکست بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/29833" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29832">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRbDTt8IuJ_so9vT1xj1_uSTsxyoE6JNX0CU0EffJvhacqnddblClaiUW2z71tJGPoHZZjgH4zczCWCdvXszVul6QfNtXUesz5woESnOaZHN7zs10PfCOj6C_7nHML_RyEqtK9buvGkaxQg0jPCMWUluYnD_ul00S3euZ-sEgxz4ss6j47xHwcQ8h7wmAOxNCLNVT8chb3HX4YP9SX68A5JQqZImEt5e5eJBLHWc8egkfnh7DbVLUqTKj3YXuzWvbON1unMQrigZT71kB1i7BFZNgsPxhR-R53Ilydxh6CRPpWV62LGSUlWCSwEFIVAP3IQQ7aRQinpCgS0894djOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/29832" target="_blank">📅 22:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29831">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3q3t5gFp1i0N_TONPZ19BQh3NRPrQfeV_SRCnzFzzOjxOvlhRswHApMbNWW3UzkeDmQ-8Tg354aBOOZ-Mja3PFO-NT0aBb21FExO36ZQ6AI5CzlI9J6n5t5wvSv6LzqLGR_Eawht_zyC6YD3DuZerbM-ga_e5vxyNvi-WhEIM93WFg_UdcrnkRyKidNtE53y9VZt1AgaKal44g09RV_UZe4nMMo5NhEOdFFkDnDnjKq3j3uqdDLkZY0W4RAAvJAroyXp0HtaGA4w6_F87NnUyEdK9o2mQ-5O7fBkfD1XDId691psEWgNthHAvZAde7DMNKkEHZzERoWm56NkSOljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/29831" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29830">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-ZvH2PgOfeJnYJiQZUmYgHhxkwQFpQhQiruTRpd62xs8ZYPVUavdlz0CuDwd-InyetJiKwG1WWwXLYlr5qIbDJb5uTPMEIwnIijUY_LwLK-8D_X4P9gNQ6iV0iCy2w5XwMspYwAkBGpGgkMHWkbStCW30dbwe86_KK6Bb89wTiEjGEa_PUdPjq64r51JA8W_RDM8VcoCYm-cQcJ_XZ-fa9FLwxsHv8xWLyoPlArmsV2IOAR0CZtT35H3W0oTdX2mxiY40q3QGgZqq2CRF-7vGIxdzXpYFVXV1Ed3Bb2Ih7ZCb2rVJUL8yQ2RSArj41Rb8p11HqGS2GcHyZyJ2RTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛
شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام
در سایت میتونید مسابقه بازی
رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/29830" target="_blank">📅 21:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29829">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvroLRreFCTf6QJvevhvMU8jOr1gwBddhpi-ZsDL3Wee_dR4Ri2QtpFXFf8U-aBMyFjddk0ItDDl6aa9tUvZkGEI_k5FZ8krs2lvFEa8JMxkj6xFxf6m3TY-horxc5OGOS-3zq42IItMMGq0KR2CL9A1U2AhZTMlUOIIhp96--1brp9RSRBR_HhIdFy8oUuIEsU_2Vo8Qyvyqi9eHy2VVRaru5dml9SuL59MyJpBwg86qtD75tB2OFTNJpXARcDiYygtHD_3ly1FUKbn5zzrdp32kH1tWuj3LaILiU3QQC1bHMFAGqFxgFPGCMVLh380bcIuhCAkxypim0EXB8yk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇨🇴
#تقویم؛دقیقا 11 سال‌پیش درچنین روزی؛ خامس رودریگز فوق‌ستاره‌کلمبیا این گل فوق العاده تماشایی رو در جام جهانی 2014 به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/29829" target="_blank">📅 21:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29828">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/29828" target="_blank">📅 21:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29827">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=ImuTia9bklseH29ptesWo2QeJpfQU9lLMTB8ITAYuK8rTcEuhmMdTDQd4-z2UEwp4-T-RjlYWdOcx8c0I_vjeiWT03EJUlLg2z5vqObWLNSXDpOhfWDnBrVD5Saqn8-uSNiFuBQhx3gNMmg4umRwOBYWg9wOPUd9OeGQqjGjm245b_1e3cKV4P1bmbGtU6UOEN11J6u4GQRlTrsVTeTxqrTVuua-mS7EjgqJrmfU8xLbN2OxVHT5liuEKX0dGGcIxVeeyRV2iyyBwa7_1-PTOyvlI1c7pgl6PQ5S4XWYL3WSoLJ5nFukiC--geppjf9UFOc9bpnpEL1WJ_PmjUCiXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=ImuTia9bklseH29ptesWo2QeJpfQU9lLMTB8ITAYuK8rTcEuhmMdTDQd4-z2UEwp4-T-RjlYWdOcx8c0I_vjeiWT03EJUlLg2z5vqObWLNSXDpOhfWDnBrVD5Saqn8-uSNiFuBQhx3gNMmg4umRwOBYWg9wOPUd9OeGQqjGjm245b_1e3cKV4P1bmbGtU6UOEN11J6u4GQRlTrsVTeTxqrTVuua-mS7EjgqJrmfU8xLbN2OxVHT5liuEKX0dGGcIxVeeyRV2iyyBwa7_1-PTOyvlI1c7pgl6PQ5S4XWYL3WSoLJ5nFukiC--geppjf9UFOc9bpnpEL1WJ_PmjUCiXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای‌ایلان‌ماسک:
گوشی‌های هوشمند امروزی تا پنج الی شش سال دیگر کانل ناپدید میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/29827" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29826">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_jViPPuef1s9R7j2Ez4xKpgU76kJxhMgflfqDI_sYdjNJXe-99XQxyOmdZH1Tw_Mh8C2pfnad0LMN8xhb_s6GUZ25RnwnwxuUUiFCroMb3ByXO0kCyLgcgLAgP7YLhSFiHFUYSh6q1jEkGt3Rss93gYn_DDZ2F2JEu7ywFaH3KlYx37arBebAvko4FiddtK41Ri8YbHyMRB-YITpQFKOy7gnFIHPN3Auccrim6SFmKSywO72MUXYitwfp6XfyxMh2VU65cqenMAjYh4235LEx6mNR5O1xz3knxRO6u7dWP9EiBfeuu9wO_lpEo13wjlEEQvp37jkq1Ts9BsYe333w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29826" target="_blank">📅 20:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29825">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXbX8auptH-YVzH_hlZzAFQqRDxoQmqTQpjMpOYKpJaw-goU7cW5Oz0tyHh9P5UNGKfKc1Rq_PGTLHxv_lhkVlWr5OZIqdX_sIe7-XWStjHbVTkYh7FmDtk7rjRYdyPvpIOjmJoq_3Bq9HSQDFaGwVyUwF7kfbYTWkVJppJ03wKrWAqfJKuE2RWnmwyEbABQymo6y8f-VL9f0BidN3xVRKVU6U6uohTfX4MCCJCB8UYnaLYVllaGEEseVnPgT8OwAOEI73yt9tECBoXkR0IIm_LqHH1Tlogdtp4_Iee9mRvgy7khHur1etEvx7_SoVrbCCNEb380SGh4FtpGyXZ2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇪🇸
رودری ستاره30ساله‌جدید بارسلونا:
رد کردن پیشنهادباشگاه‌رئال‌مادرید اصلا برام آسان نبود. بله‌ابتدا درآستانه‌پیوستن به رئال مادرید قرار داشتم اما بعدِصحبت‌هایی‌که با دکو و هانسی فلیک داشتم تصمیم گرفتم به پیشنهاد رئال مادرید پاسخ منفی بدهد و با باشگاه بارسلونا قرارداد امضا کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/29825" target="_blank">📅 20:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29824">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de2283857.mp4?token=L8tU3y7aq9enCunRpJWj24Bgk5n7Kx88xSILYhYlDk1ox2JEwuH0Ry7OGJBXU4CAdSxG4iN5nk6OqpowR69mGKWvfOTPT-AvHQah_myXKsVHnryfXRoijeS3WQshx1qKcjDPSMwDpMq8c6ipkimBNtmncm5CGKnbo49VRLACZ62bavc0GLH6OF9SQXiLFJ2NlS_kCSpz7VAVnoFkRhAIhs5tvErEqPBTopLwHAlYBcu4tCJYBahAprBTMZIA0ON-gi7XuXfgh7_9aKbEUQ2cYbA6LV_lFRZqMJ4nhbMqo3as6nkjvboA8Y4gmYi8JXZ65rxNFi5xWfRUPV1CdkimbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de2283857.mp4?token=L8tU3y7aq9enCunRpJWj24Bgk5n7Kx88xSILYhYlDk1ox2JEwuH0Ry7OGJBXU4CAdSxG4iN5nk6OqpowR69mGKWvfOTPT-AvHQah_myXKsVHnryfXRoijeS3WQshx1qKcjDPSMwDpMq8c6ipkimBNtmncm5CGKnbo49VRLACZ62bavc0GLH6OF9SQXiLFJ2NlS_kCSpz7VAVnoFkRhAIhs5tvErEqPBTopLwHAlYBcu4tCJYBahAprBTMZIA0ON-gi7XuXfgh7_9aKbEUQ2cYbA6LV_lFRZqMJ4nhbMqo3as6nkjvboA8Y4gmYi8JXZ65rxNFi5xWfRUPV1CdkimbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایتی‌از عملکرد خیره کننده جیجی گابریل ستاره 15 ساله تیم منچستریونایتد در فصل گذشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/29824" target="_blank">📅 20:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29823">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLg4Sx2WuGVPDL4ZhAACjCcs985un_6A0NkjfLpOtH5GmyTJJBU8bqI3dSpr0-1z3iC5i4tgSWWhg9JdpEr2M7hhxH9ZYPl__BAaiwp11R_oHf04inX1EEWv5XWPo7ZafH2Fpc2CfX9dlNaYw62idkKSM-sgFP5Byupruh5p5KajegVSbDorKg8PX7-BGwbQBXeMl-gSY8qpa3iHR9m5J_77-b3PH_TPiNj_0EZZFQCrxxBRLU16kP7vN3txrvO14fcG-Dgwv58t3wpp0f02wC2aze8KluMQi8Xl2ihmyg584vmNKot5XRMjYGwoWPRSKWwSjTEHJdJ4_MH1oamcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق به ثبت 27 گل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/29823" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29822">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGs9GBOy-UFEPuScC5Ks8KpGAL2yBay44i4zTj-JFrBhI9OnusGVBpK2mRURuZU6TuRec-255X607tYKVAOVEklqHO707fHbpfUT01NYaKJ-iVBp7wfVFwbCG82BoqvqghDIs_jXoQPEs-mLexIwd-EEmUpYZxTCMy5238qvHB7jJ8jAuNr4dJXGEpQU_K4-nKAReVileHw-IIErHl2YffVp3wAb6_GXe93Wij-nRsj5_Pe8FCNRQT-6SX_-FGbDBBWdRCtL4iUEsDYZ6S-tr6nYfXLGynjEzeuOfZ3AOiFUY10DGZ6hT3A6K0aBimie0fsaSCi0bEJfmJha9U41Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/29822" target="_blank">📅 19:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29821">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8dtSNYSh4IsRQdhLQ111RnFYyg9GhaZYvNo3AVgKmWiE5tQfLnepltQ0IwiTJqs5Ku9VWBh_uEEWtBCay4f5xeScPyTD5CYJM4UOEtLcFKZQeIzp0tMT30qbS9HUnIPgvuEaB7WjlBJuvMBiB4fxOvF8dcIl9C_AlB-zB8c3nBUMMHfvCQRF4GIrPbSwzWxwPd7G4vkKj3NKUm7xdBRzNTvU0RqHwbKKJEqptq8y0txPIWmXd9hJO8WQS4PQqnDJCV9q8t_GByEUiM27MaoHy5QtyiIzdIcnf2r2kOPKBh2qMXUJClg25ImYS62ykVYHRPvYQ1B9nPG0gLj_m7UKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/29821" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29820">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/29820" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29819">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_YagaCaOk3TeDMQHCNLxw7eTQyZJboSICWZ-eOTmxhvZ-LkedkmuWposG3BXqpjovC4XJlARqc148pGk6bdSdHD12e-3i9vQ0uwNPOzj4uwftdJ7SeyklEQ1J9qbyL2qgc8biUg-bgksQ3HJCI0gKlWO3ivKMox4r4Qe3gqRhP5OY2tO42gh3sHRCiVm6TtrhqB8JmbnbF2nm13qsGWLFIwolJs7emN8UN-F48txzpE-YA4wkjFPdzOM7BnK7HmyEUvqRtYkvd3GnCEIb93PiqVoWYoiHJi9NLYOHx4850qYRq49Mg05UPGEk0tlEuJOfVn9H3YrOgMFfBsECyXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لالیگا اسپانیا
⚽️
رئال مادرید
🆚
الچه
⚽️
💥
باپین باهیس؛ برای تو، پیروزی یک سرنوشته
🌐
سایت پین باهیس بابیش از400اپشن برای پیش بینی
🛍
پیش بینی باضرایب بالا
💎
🤩
🤩
🤩
🤩
بونوس خوشامدگویی
💎
🤩
🤩
🤩
فریبت ارزی ودلاری
💎
🤩
🤩
🤩
کش بک روزانه
💎
🤩
🤩
🤩
فریبت درگاه های ریالی
🤖
دانلود اپلکیشن حرفه ای
💵
درپین باهیس دلار با آربیتاژ 30 هزارتومن بیشتر ازقیمت بازارمحاسبه میشود
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g24
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/29819" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29818">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3gZbnWyDOvmF2hW86_9cw3Zbs4ztmafpYnQwPUfKSauOWk50Q6_yh_rjPAfqGeSaJq3cGpjvOjp0UAMGBiVjx1X53fbskpNdpXtbTorTD3pwd7jP0s7-9grvMiimQGlwHdl2U21JAWWjm1SPLUDBT-5_G-4fIRF-OQKdB83f-b0wq3166POdlp3nCZNJju8CEpr6AlnxPVb4haqSa8fvpHrp0jQlhVcJOLF6FhaqT1HnnRlkLWbBoJj0rD5AtUTVsOzl2s7rjrUImLLaaai31uUuKnkrkoPUMopVy7qiZDPcvTiSpY8BFG3_xwsjYE0wFRRRiSfLHx5AnM2JFAb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/29818" target="_blank">📅 19:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29817">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmFIWl8Q27AlHsjJmSPy2KSN-R-4CpFA8sM5PtZD6gGd1xRUN_t98LIS_wctd67mw96VCHEYS9_nDKCttsSSeZgmt2-sTpXxEgky3avE-RhHbAcw5WpgZAQ47-6fMxzh8H4e8ETX9173QQXE59RQ7blaETqwX_VX8qu1D0MvKk10eVA-1mb5C6AzwywOJYyQ_km6_P_xlP9SdBhue2aArgXWV38610T9I8giW8JCT0jJ2iErJ0ctYvIaClmUbKHfIyrS0v_onPgR0b6-0fH_5OPM4blGm3IlLwmYGVodFEodGOXPBxK44TPBOWnmjPmihjvb1MSCphS5qoqIx2AE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/29817" target="_blank">📅 19:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29816">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf-egeZeABpSkupE6yRcV0ZiIwJZEssD4ovQxPEW1_0Oj0J2TNUHw_vHhHcbHPkBbG-DlUs85SpwZ2zpr4QtlugDRd7Cg8_vJqO5FeY8D4HyhTCXjCK-7rjSgnict9jInVC9Bw7modJyvCMx5svlMXtRYlQrsUmIvEoCjIGOScciUYmrUEC7sZF0iX2ab3sXfZ1CQQhjRvpwYI1UPlUhC_oS8_zyIWByWvJ9UqS72xFnKHZha6kNA88N-47OXYc_n7GZ0PAcv8_Awzfn9Q9AgG17KquUa6qZdDJYiZ_3FE0xSlKni_e3US3RkezdFWvKmQq8avtefnF5Nf8_b8s6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/29816" target="_blank">📅 18:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29815">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9Nn8IB3Uj1FoghQFPJlLhNiqaBoAuWjKKBL4k_EcheMywyAGMRH6GuBLxfoAX9776-MaZyY8nlT8ZN2MdSLv0m6JE0FRN0onUC2R5UCQ6amYbigxuuiYfbaeQ3pqOZwitf25n629Oth8K5S-WLkyXOxHr7MFfI2HsofZWJ_rv7dcYdCFxnaZxSKdAAB8yZj2kcMhJwqciOb1PymlKcWOXsxcBAZXjuVmgmXbIHlcQqxr0XBy7O0L4zOm9_A2h0arCxEKBKLWA1kn9UQanyAkehYV0mXOsBFrP1TKxm7QLSKQId054P8yC5754zyf1k29rAxx0IOOieUlAihwGo5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/29815" target="_blank">📅 17:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29814">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlMzHRvFCmKN-HaQcw52B5JXFUBheHk77rhCYxnoDJusxp3HU7ol-q67CiHkI36CBgc7FZMdcXLt-mXX1JCojy6mw9FcieicBXSHsedMwpepGutYQK--tns3FbpUl6x3yRsdChCUBV0UxNfEfcnKfdP4QS7EoHoMe6EhUnnDa6DOcjnY_obkatvEKZ8FIe2RSeCN7wVfrKBWg2F4kbc4wyQWYjKoIHP9s8S73yCEyYYtncQZNzj8fcss_0OgW-A-0WnFAWFyqd80CYAaLT_4EUBZeSfqW4IijuXjTO6ZJe0eNOXkUipcTs6H1lT36yfWIdxaSBVt75MA25EsEwt4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29814" target="_blank">📅 17:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29813">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okyr2B6VBTDObiVBxbI9sbf57YVWJJGeYTCj1KqcYXTnJc0Vay9vZPggXVxv8EVLqZJ5gh6x4Aj7dKVsnm3xdRp7sjPjMzoSmNwSe-EF17fQUjDZ_Xfx_L92v7vNXUtTCSTRD46pX6vOuhx0JbMAV27RV8zX3kidpUzdJP4HlXPrLk1Zxdi4bxKDVMaGWOI7ByYAVj7pXhkre2ifWneY9FD2CyZLRzwAD6SLA4FZh1ZTXNtDcUxceygUgOWjl39lme88xh9GLKs4CpyNh8lF5RYyOxfmZFjChPeMKVkLdY5HOwKL2fVcU6EINrlt5d4Mrptm_sUhvHt5zAQiBQh5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمپین تبلیغاتی جدید سیدنی سوئینی برای پلتفرم Novig هیت زیادی ازسمت ورزشکارهای زن گرفته اونا میگن این کارهای بانو ورزش زنان رو جنسیتی میکنه و اینجور به نظر میاد که تنها استفاده زنا از ورزش این حرکتای سکسیه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29813" target="_blank">📅 17:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29812">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djYmHS87O8eQmpyt4Bnb38aVDeicOVcX53hgaOWY7n7QcBCi1-s_xTElybShbVNkxMI75fTX0oPBbZ2cx4yQd_9jo7cDUTAS004mOxvIFyAcIOJVX3NZVxDe6BmRwRQjU6Mttl_9kraz8AHf33QZogpki4h5YZbGk-HdbSV-IplzJJR_QhrW-yH8qdChHPuvHw3-ublqHfYxUiOi89WRcu5nTJLVNB7JE0UFDs9c_rN0fILHnfqG_WvQCUAEPg5Hic3eCqsb60gGf7KfxML8jCPNVah8W2pZ9K2H7zONjb-7e7Oa57PWs7CMsja5sdU38Z0j2wI6zUEFJS5asTusvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای تیم امید ایران در مرحله گروهی بازی‌های آسیایی ناگویا 2026؛ فردا اولین بازیمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29812" target="_blank">📅 17:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29811">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsTvD1_JavbiI3vMnnSO3VK1l2Ib9fbJk40AinlmC23jIeJC7pXhKPE1vxDwYRR-Dl-oWCwik1xGlGeuijDcoCe-JBtpxdMk9EcYwn_EiDskAnYkD_K76AF5D7CtZBpOSiOq0xnuHwN9sftG8aHCNdMGzNu82QEfZgOj_i--zwP5KgIspYQXhDnLDgLU1nSvPFiaXMRzgVTbzoMksjLB-Oky4-UOsJP4SbysbBdbsEzU5Na9Ap9wM6O20c69ptFJqLkB2Zn3EI-WzAgU3rT_RIWPRQdZriYPAUWdZVSLroEONk73ao2ZYOhgqjmB25MqZ92YLiezd-sZBmByWlCNGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ویدیویی‌زیبابه‌بهانه خداحافظی مانوئل نویر 40 ساله از بازی‌های ملی. نویر گفته دو سال دیگه کلا از دنیای مستطیل سبز برای همیشه خداحافظی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/29811" target="_blank">📅 17:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29810">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQFxB-RwN4sqe7BRpyYp_QXsk4M-uCwbWmQO8nhD0FDvBPsXX53E5Sju2k5FCxQiZtwSOUWOj-3gEynnCGBwNldjQ4RDiMsoyIUHnG0iiz5qINYHcuq1u0SySv_nblbqY2_rHm0XA-NZb-phog9X3pbUTebeXDvD4WRpT6ZYmmzVVRUj1DMaFKJ3zS8eX66Mj5DGxe7moZDoJyIQG_zTcs6CDFt4dHgUKGaAUXI1fD42i0VZJaEkIpVbPJojxrLTc1MLaWTv-wP_51xJ6UmttOauv1KDBfAqpzJrzG5fOq6onoNojG3w568ojvvTOY633UBzV2lBVJ39rv98RKHqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29810" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29809">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJJfE-C0qsRKaH9CpqyiSJ2eykZRV76-rfL4Qc028DgUdNfGVhHMrzg_cxDOJyhmiRjo4zKqBpivnWP6CgI9gfklpsemusFnIHRzOHc6tUoSMhQv--Q0UdCUOfPG9S5EYykdWVO0FylGQASEAZs2Yk2GcTSZXUBzOPSd-j_idUmJduXpyoo2TjvAmTwVWBlOqSJC96Cr2fqpYRAf3Q8y9jzH-92MRc_4JBJ1MRVaThVqAXYSIUSVU1drDH7ZtY3ZINN8bNVMVVBeEsh6BSvamHjYZQxgh2RhdPHNgrtDpE7s0yg1jTL5Vuu2AVC3Fs9I0_KsiK2VOZnJgjEWg4HfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29809" target="_blank">📅 16:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29808">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep-dV8se2CvvubQQhQ9ub_2-8-43sleOJVvqgPc5Dow9AyCxC4RcndWkIiQavTz2V65UgnvEPm1iWtDzD6tuf5B4rKsFow76CzoBFu_GtQMGNTOngx8oHlDjhfLQJ0hjmjjcrCmeBn0Vyv2JA6NfFnUCKBV767ldAPecxBwBTy3DgRgE5MVStrPqIxfEKWsVKvne8W1Ke2vml2j4NKlEI7bNiSUD6sBbv_XLrqzTeSjAR0UCMZ5W1fUkvxic-YuvPgfxLPttZygIH8u_88kzJOdPzXoU6zag5wVb3aBdF0RuGcfdpTqFPakThQgmIEVN9u28vJsMFioJCSzb3zlvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ در قرارداد شهاب زاهدی با باشگاه جوهور دارالتعظیم بند فسخ 150 هزار دلاری گنجانده شده است. هر باشگاه لیگ برتری که شهاب زاهدی رو برای نیم فصل بخواهند باید 150 هزار به باشگاه مالزیایی پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29808" target="_blank">📅 15:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29807">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrUDIQUyXDRK3yVLrW73iIp0zjA_BAWQ1BFeCkRft2_viZHhf7Y4h1wm2YyMvWyM-GuUsRCMujZgbBaZZihTVDFi8OBI4ugGTHDc9kI7eHqDZR9AkjuGO7V_ogSngPP_RJMjAFnKI0pic6gCLa3qv4jA1gJiyl3s9tLL8ADKLA4Zl29Yl4BDMvzpkgTPCRai_wudYg9tdc-Ny0liylt9By5jTQTjH__JF0KhyuB6dwOXqhO97QX8hcJ_pwQ-FVJKwerskNREqm1TX9-R3QoZ1-cEPgvxbtcsXgUqyNFY2-u9xsCbdlQRm_TXWQ9Z5hlfPspyNMhvC6-gRAzvNzPM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابل‌توجه‌مفت خورایی که با گذشت حدود چهار سال هنوز نتونستن‌آزادی روبازسازی‌کنند؛ ورزشگاهی که دیشب‌استقلال دربصره‌عراق از السد میزبانی کرد ۶۵ هزارگنجایش‌داشت و ساخته‌شرکت‌های آمریکایی بین‌سال‌های۲۰۰۹ تا ۲۰۱۳ بوده. هزینه‌ساخت مجموعه به همراه استادیوم ۵۵۰ میلیون دلار گزارش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29807" target="_blank">📅 15:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29806">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAZUuudk51XK-HZlQRPedNCk6zRDZItPQlAHrvIj02C9uv_eGG9lwb8ide3o1hijov556zIYQ4wIrnFw77M6BldG48tBBklEMRru1LDBAeVa2psFGQPehmY9IxGMzqT-68v7w0EFmx-utn6rEH9yh0PuRQhi4fkvF3LYtEGrjwvuwJDy9LhpvZ4lgFbQPJfiq0K87aby09eiIVpCi7jwePO7j-9hq0_Rr4qhFlKMPrW40VXmC3S4fOWN7kOREXDOXAiBGJu8Njclk-cAcaZv6pQ9OywklAvYMgIUaCqXwQbL1icT6YQPlEiUQalli-QqFpAjHQG9f6yrCxfJwZ2Aiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29806" target="_blank">📅 14:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29805">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdv7NG0fsc_QnztDr4SZkqPO9vW7cjBdFDYdN5T5-z5U_4C5oYQDAcwkJ8qbtyXto4EfVaqdKyqCj3beLB-WartrHygEryO2f8Yo-m7F8qcrnYCg7U4MiKAiNNhqfH2WKlNVHOlBprb4PhoHc2-F9JRwodtbJocqCYVx3HY_ciPj9bJ20U2w0loif32h7REl3eOGBt5a6pWrHdfwIbN6w2ux7iY4Xi9o4wLlykWazE9P8ZuKX7lMMZHeHK6q64WYha0xFiQL7VWu5XZt_tOy2fo2OBqt9g7DKn-GtuebQ63AfJQKpNFMQKDwR7tlkPPt8hcos6h553nqvUT-cB1MYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امیرنوری‌بازیگرسینماچندروزپیش در مصاحبه‌‌ای گفته بود که خیلی پولدارم از هفت سالگی فیلم بازی کردم و اولین خونه ام رو تو پانزده سالگی خریدم.
‼️
خلاصه‌کلی از اتفاقات مثبت زندگیش گفت. بنده خدا فکر کنم چشم‌ خورد دیشب‌ تصادف شدید کرده الان بستریه. زندگی‌خودتون رو رسانه ای نکنید لطفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29805" target="_blank">📅 14:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29804">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-Yd84dbHesu2I6mzpFGOzq8w_f_VKC_h1QuX9GOMsOLOVoqt5nemaElvhDO22Psjb3f05cmsmJwKKE9dAjyauQIg8timxbF4NX9DfhSFSVYGmGvN8oedlV64EuTcJ01ZsG8RVZY5fSU_0yrFq36YgmDnsTJfxKN_TTuf_VNO1LmBLfWuOnU0fAi6dbwayonUa6k9ZSV_A63UDVvCk_QX4pRcK10cQgBrZLf8tFINNFwPBadt_gBiEMeQA6Ss5K3kLwYnb7voQZoPMUKkY9w7mH42mPEJzzRsMWaSvhPb9BxXmX4I-Lffm_Tl9SkgfMSfR_Ym7CqxEFgBMwx4y-8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سسک‌فابرگاس سرمربی‌جوان‌وموفق کومو در گفتگو با گاتزتا گفته در وهله اول اولویت فابرگاس موفقیت کومو دراین‌ فصله اما اگه درپایان فصل رئال مادرید به او پیشنهاد بدهد باعث افتخار ماست که با باشگاه رئال مادرید کار کنیم و سسک به اونجا برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29804" target="_blank">📅 13:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29803">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9Q93cZKcJPg3x9cRijGHsdiD9HdSWJMOnElM8iLqW40RqNQbkbqOIkHhS6nmW11G-Mg0TSfEzhYuR55ZmT4Qg9tE5qMVStow8uZOR13PPUGHSUxgYTjc7FRIhChyjFtWr7WlESVMgbHxcqK4Pq91qsyykrXRG5Tzbrmz4UNAUoG-xoDqbCGNtpyZgTmz_pL6Yvc-yfNj_qi2ZbuY1EVRguOMonK8LKVX38epJ2n92KNSeSAqK4-u2131egrDchQdSbRpoL15TAZeaXYVqsae0LaABDWaG0LUFdqN-XvPDE--2WqKc-vMGhjd_bCAgd1MmXjnslt6qfbHxLgZYdF0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29803" target="_blank">📅 13:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29802">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzUe_SaQdWSH2cWrW9HvWl62BnyF3Y07NpQNSaY4dg63Nfg1VU_m4NFqTRVqyFvjcEP-PipZmX6ErAc7Myo8bANBJY8fMUTwglZZ8bQMHfxxoJkgmczkmdKIVHOr911BYYLuz5WRRnrKUCto2s9rWRQtQEIUFZjrSOej7rRugY-of4G3iDXDtfqCAgLKVu92EroIKsPx6k6PmZGPmF2K1QzGrv8ruvThy5QxEAt1N1dqlq3jtMwOr29tUOUZPHevBjPZLeqjTh6naFiSX0pr5OzmgFCLsKIi__74Th4MV_TxFUKI9qzrtql0PFicYZLMcsKuUxUevTTVC8aL83Igow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دراتفاقی‌جالب‌وبی‌نظیر؛
در هفته چهارم رقابت های لیگ جزیره؛ لیدز یونایتد تنها تیم میزبان بود که موفق به کسب سه امتیاز شیرین مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29802" target="_blank">📅 13:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29801">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecWs-CQvvDIdBwU47UpCBXi8VGy3u-0Z3RWJk2c0lFGw3_zWllQ9NNdm_UozBgvcsli47McUZOc7dMfnm_iA-uC22CvZxMTjKuSfiUN-ZKw3WVuY-NFmN8Pd89s2UIcNS-6kBsg_OWu5ZQ7lXDGS6lqMTvl8q6yrfS89WlCcSTzCdEzwqXV2Ga8d0bSBOoOOC13W6-KTElKu_yAfzebV9Wb8wMczcpZGM2Hi2wJwLfoRVb7ygAf6AS8ANvURCrfhBARkoeOgRN1IrVYBSEKOrvLoAmAxFVIH5K-7AEKgwyG-zs5vIXv9ePEMvyNABfCAy2rRUbpuTbLf2cIlcABAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29801" target="_blank">📅 13:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29800">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdYXPqOTu6AtI30H3ADGFmaK_qU5mdSka2txBGlMJYcVAbmztaRfH9DkmQI9Kl3GNRnATMGmbL4Z3Q92MPXzDMtRrbOnwF3Gp9eETkDx158zGK2B5hFG15PAE-laRvAaRcvs-cxQaSBr-8XBMSz02v0uzLHnIOhEKdbkQty6_KkSsvbkZz7W_PvPzzBfV02Q1oP-lHDVrPdLfg06VTPGB0M-beeZeAT7g1tEQuRuS1LjwM1meAQR13IUz-jg5IOJwNpwMW0VnIixrOju--Jq1ARbdL8enFqsibjVWcz7fnHfO4MNvaVPPtT6DNmNEngI37MexaHTSAxxExINB2U70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های علی قلی‌زاده امشب به محسن خلیلی گفته درنیم فصل با پرداخت 700 هزار دلار به لخ‌پوزنان میتونه موافقت مدیریت این باشگاه رو برای صادر کردن رضایت‌نامه علی قلی زاده بگیرد. خلیلی قراره با حدادی و بانک شهر در میان بگذارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29800" target="_blank">📅 12:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYCCaViVBIKPEPOW2W9GrCsB5aSwy2QQigpdsvKeca5g95JVnQEuyteuOv7lTkKdPk2psAxNSG8H_E2uqOhpM7b3nCZ-ATrJPKhjMfSmMhAPPOD1WOh_S-2wbqdAYiex0qiaDtixdL-44iYWgMq-1YTn1UYQf7vzc5cRtvmoFWyYNi6hMF5sORs9TwReZj4UU-LlH0uRapCQKzJcgNKiLSLcVNfLnJ5a7GOqjRPZj6D75y8j_pgMS9CohHcNEQfeDJDJd3754xrNwPpr382kQ6CBsGxxJwutokqG5b1MeOoeOWr_IhULStgNoqHchx1h3Thc3NQgasjE1FvFtHYZRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درخواست‌عجیب‌وغریب علیرضا بیرانوند از سازمان نظام‌وظیفه: مریض هستم یه ماه سربازی ام رو بندازین عقب که بتونم برای تراکتور بازی کنم!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29799" target="_blank">📅 12:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29798">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZRQUi-htMzmbghZt5lViinWnq2nunpJUEFQZJbMEXnNfjkF9-Au_YoqnANq6Xywm_XdbND4qhb3NOZmMfYO9NHgEyF9VGGjI1tdlFkm8397G_IKCqwaD0LkmlL7ySO1zJKubaY5ObE5x10TKLSvk1I99GsRBqewqDH-7nbBhJ09GjY68rmZRt1dPfK-nZxE6D7tA9WgYjD-VDcKtYONWmvmTpq2BhJpb5aQqNbPBNUWYP2RaD7Gr8R90gTD0IWZcqE50riEneWW0cJv7CLmJTuW6UNWRRpNlAu2IMO6fggT4EqYAn8ZQsZfM9Op6HvDvmMEWDjHvH_ZsF2iLNrO7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29798" target="_blank">📅 12:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29796">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vE5P8hWoGMM6pdQLiv8ntdhqsNyDpCxn5tD_ocIJjbBWZdO-977H9iUxNaFj-_wtaDQ3f0cs6fMMjEuslzCDs6KdS31uGd8r7YeQHv-tcLuAY96Jzr_qKJepiEIfuMtmj6jOx3UvLQXNbdN_NVTueV1Ju5eCBXROIL1PJHyaut1juQFaYYg29cpWUYP93-L8QeDjCe6jteLejO-NOmOtx87COqDHfIDT67EjLAEua_fdrDK4MkZ-CgEXDocMhKYhcWbG02bGtNvY0K6gS8rgUktaYJe_zQvMEzLtNpTWNFRRsiGaeKa4P4QB9CDQtzqi8d0ZB35DaVgGOhge81XjsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfG4FnSPRTtSw9-TXq_lSPnaRorfh5-0TL3eXkzk-K6BI6Ai1dNdTyt3guCKpQ89H-Uv0U3ZoyB-HtzfZichitdEvNDFUH2dZoNzxZa_YsvhPSwfgh6t8o7HCf1PcIl-tB_4pE0cvq8KBOpLisQWpBdEujPqAin7BmZms1covfJMn676n5EnHBJW2PIuxmQxlio2RFEFMel8aWxRPk-z5y_e0t-JAwPjY7c5dSaN9DYP_5qAQ4X7fD5GFSGcZyiGLkxCU3gdQBsYRsWAqjgsxuwGuRzMv8JjEtK_WjJZhajPOn8L07sTXOkPEhzWy_pESgB9_vocVKu5YedgSTJu7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
تمام قهرمانان رقابت‌ های لیگ قهرمانان آسیا از ابتدا تاکنون؛ الهلال‌پرافتخارترین تیم قاره کهن. نکته جالب این که تیم الاهلی تا همین دو سال پیش هیچ افتخاری نداشت اما درست هزینه کرد و عین باقلوا دوتا قهرمانی شیرین در این مسابقات بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29796" target="_blank">📅 11:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29795">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPYWIzRZ0Qhckvu4yC9C6Ib3Yj87MjQ7jb4NoDC4Hjr7yw97a2fOoZg65y9N6lA580epZ414VFjue8zpEx4jI3zSQBTJlYSXuEQ4K9Wo6wAOs6UKnX5GH80yNRXrqUyJD_eAnmCUicDvK4_XHr7uvDjYPPt2ENKsX9Bz6biVwg_J0PdJPfckcsIQYFr5OYq-mi-5ggSrTd2sVyQDTazUhdfWoPepg4eNLrg_5_uk5P0dzTYvCLgTaSFHXogFZaGm9HKhH41KoVjy-0q5wrH2JoVfrxnCCPGPYBSh28nB_8H7dOsZz5Isyrf3wY78L5n4bhVWXw1rJtb_hXwRfoQtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابیو آبرئو تا پایان نیمه اول بازی امروز بیجینگ گوان درسوپرلیگ‌چین؛ موفق به به ثبت سه گل شده که‌یکی‌ش داور بازی مردود اعلام کرد. نمره آبرئو در این بازی تا پایان نیمه اول 9.1 ثبت شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29795" target="_blank">📅 11:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29794">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj6IDE-6MiBUggWk4RWlR7GVTcrquHUKtmgfO_nJ--GsMaWDR2wtrtrjtmjZniiki86fcy2DncJHJdXZFM3McgOEPQyJS0gOea3gQrGun8rmngQlDuYfbfbo2nAuVbDpQrLB0A_xoNSbXtClpVqcRagOYUpXkE2FTGqWDgJUxJdQyVthJBJcufjM8YsJD8hJeU66wdGznZf7lANUxsasMicxZ5TePaPGBJT8cWKk4_gZ2FQmjzlguBoOmpVOxGn1w5PlYlxGclpQl7aGE3VMNnu1Q3i9PueFmw7FG9bRhOVpajjRzPucC7WldkPGJvHpYbKFJgja0LWcgZqKw6mEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ایجنت‌ایرانی‌نزدیک‌به مدیریت تیم استقلال به فابیو آبرئو اعلام‌کرده درصورتیکه باشگاه چینی بیجینگ گوان به او پیشنهاد تمدید قرارداد داد این پیشنهاد رو رد کنه. مشاور نقل‌وانتقالاتی تاجرنیا به‌آبرئو اعلام کرده که هیچ مشکلی در ایران برای او رخ‌نخواهد داد…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29794" target="_blank">📅 11:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29793">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dal86uCYI8nr1-M4Bn96tJaaH6RuqSjaruyLuP1Mtmy8ju6Gz13pfvUQRftVpXLA-GzVpprP5eLINj4MUOFvcIcu2Kdw-6hfKWg97Xmt6stBTtJ58inLBJ5_FAa5pAFA7IWXeFaITkTSJ7PTkjOcz8rFhKqVAz30H-n7qGbJE_KfBp4LmdRTDrWPDLbv2wL1BL9QEMsdsRr37Lw08x2Cyxikxorvkkat-6i2S_NHchgBdX4zv0KC7YDq9aXFX6nSv0Ovu4WNUNwOxvB6dqioupLHJqoYsh25Kn1kqs0_u9wiXM3h9HP4fbojPywAvStWtVTeCMQcR4VVgAS4n4dgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29793" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29792">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29792" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc2q9K62souzViM5k9s4qGUJ3_oyUP6HzNQdzL3RqwNk6-6Bt5c0POb1EgP9LudRAo6W47FeUaaAc4OBZrW_U2Divg9hhmaamdG9WTaekXhS_osg_DrOl4flZ8BTq3WITP251sN7o17L4nWUzP2u38PDwn9WCaKPE3Ngs5jAFnae0UNXdNqtkehJ-DR_A1iymYRGOMDX87VwdXq_AbJyzQAWAKVZpusuOgwNxkzYRNFkka_G8at0ZfQfTMDn8ZDgCe0auNrYF7pImUSxA2y78PLrp9wWheENkQ_BLWFCTx4nFwCJXaC_hcwViGWja5J2dPuuElDmIeVAYRubnKkC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29790" target="_blank">📅 10:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxKBzthMNjB4Qi9LC1aSasnjarcnDREB9b8hlllcFO2B3qJBt7UOK1IAD1MIGQwjUhP4UO0KcP59E-sReGEtyzpYtceMv96NgUMEpRrkJ1bH7zGqzLOaqfE9pxqHSkPBpxJTK9LCDOVZlItbbgVPDl1tMa0oFYvNpp5feXNKLfSfQESdVxLy5XooBIUXW2NALUTgTipkuVuZgPOp8xq1e7HHajf4JBNqBVzqiwXuMXhCpyuV_GsJiOYX9tBPIq6yp9G93FAQ3OwKNNtuJJhQ3leEYjAiHsk8jTphfnmCeSmPtsbp8-uQLgT4dsxZGazGtJ7SgDGBoWrcW41e5y5KEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌کادرپزشکی‌تیم استقلال؛ مصدومیت یاسر آسانی جزئی بوده و او مشکلی‌برای همراهی‌آبی‌ها در بازی روز دوشنبه مقابل السد قطر نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29789" target="_blank">📅 10:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltEmSh2G30Mu49W2eG4BzhgnPRtlJ4bmKRvNnh7i5hEcjaR8GhRM0KmRZmlcblQE0jy3M0VHQrQg8OYws5KxHGfeP8MtOhCCPxd2BMonVFrRWk6aNJtZYC8JijWjR5VUddR8CRMJ08GSE31oH547qNGNRav6JJz8IrRGlfHVB-pj5WfrpjHB1r9COy7gulxS45fEo9gb_TdSzJMSpjsW3ZgRMo8aAOf3mge6J6Dn3PeIHmRo8ZVqkPBxhJaWtrAXmAbxzB-11dWQDyCUuy5S60aMkeqIxRlFue0HKGO47LIaH8mD9tn4rwOqoMURmg9Hmqoh1pskdnKRE4cMVnMgWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودیگو گومز ستاره پرتغالی ولورهمپتون در کنار دوس‌دخترش؛ پارتنرش‌به‌حدی گومز رو دوست داره که تموم بازی‌ها برای حمایت از استادیوم میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29788" target="_blank">📅 10:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=KmCZLPWqRSSVxMFiy_7-CdwL9AK7eAa9ZLkbY4Vofb6Ie7NJmuG4A4wYqHasDhwz-24Ya5ZJ42WmH2frSdAgEpnQMo_bTDoM7Pc0H2WYvE1IO5K8Nv7DEnzd8EKlvXXlGRiZYAiQbvNotduMmp5D3ujN6thcZzyr0kOvJKstRz57-6z0nRS-d4FBiW-YEusKVmUKH18Q555KJXFpGV78fzRxZtZnX13MyALHq6n3N_VNNJxNhqp8SzbOPfny37SUO1y1QJQzTOu1l2Gq4cClMlg2naTMaNT_eGf6O4Rzk62_K71vduEZ83JGRH0sUB7EenXcrvFOdpZV4hTP_NZY4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=KmCZLPWqRSSVxMFiy_7-CdwL9AK7eAa9ZLkbY4Vofb6Ie7NJmuG4A4wYqHasDhwz-24Ya5ZJ42WmH2frSdAgEpnQMo_bTDoM7Pc0H2WYvE1IO5K8Nv7DEnzd8EKlvXXlGRiZYAiQbvNotduMmp5D3ujN6thcZzyr0kOvJKstRz57-6z0nRS-d4FBiW-YEusKVmUKH18Q555KJXFpGV78fzRxZtZnX13MyALHq6n3N_VNNJxNhqp8SzbOPfny37SUO1y1QJQzTOu1l2Gq4cClMlg2naTMaNT_eGf6O4Rzk62_K71vduEZ83JGRH0sUB7EenXcrvFOdpZV4hTP_NZY4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/29787" target="_blank">📅 10:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5bokmgI__iqMBKYdBlm3y1AkqW4mxoIRZaSdfYkOLWTZ35E7u6m886Dt8acP2djH_vtx2ay0vHuifBWUvelYnDI4f7rBj1728POjHVwEgOAyG2B-efMHPVbRI0gBPNLRsiSxYIuzaqgn6vA_e1oybX-WzCs28FiPldplwnRv5zjefYqxzhSTApISkos5etk-_Ve4_aTPGytToS2byAV7495k0WAnK5LSBYCq5eOw9YxLMIxPCNhjD1-yH27duXZ0G0Ie7aMCgDTpHh71opFN4dF6tAIPhbjgzeFhrQE9KL8dj6IUT8X8WutnAUL1MQRIbC9Cx0yBCQOCKt_042HPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/persiana_Soccer/29786" target="_blank">📅 02:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29784">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilR88zVHFYDzTyL_Yzf10PlBUQ-I-mnw-yX2UKsl3X3WrZKm7Y55DNNqRyOybfP9zbmo8YcCnEICVHpeRZvSvKvXERdNCApxcK-LOoytvdc1iLN_haYWONaBGZqXWX50MMjY_B626GykldfKTtkJvFBT5hHgRFxPNUfoynTcD7s4RILI7A1pQHjNymoWkTNrVWPJQxiMFoNebtavvHYAP8TXtDMlNglGHXGAwaT6rFR1h4sGE6xnxmykrpyQ-Twy4tdc5GxV-di7Bj5RqkkzzJryCIKzFddQe-s5Yzo7U9zb3VeT09CojPhSgt3PLm-T5oQJJvg9HSMq6xAp2figXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/persiana_Soccer/29784" target="_blank">📅 01:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29783">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp31UKBFribHQa78XP1MM_TC1AQUq-C7QzRHKcM2EzBNwWbcbZsWEnpLq4akiT0oltXwJONR1imMLNUZ3TrbDeIcQiYugllss_OoAc2fF5VjECx5CSjd72OH2-RlHYnjPiRx-raL-_r6fV7tLAk14X2fns2FVxQwlqMrbIPVGBYqKN80vAh-gmTnrMVPHnMSnKVaOj0k8Tcf5JrEI2Iw36U_C2ox90XaDIXYSnmtV2OWxXdFKcAkvK2tpXozYBTZ653JLtv3mIs29H-LWQv6XvZtnsjMTtUZOSYAuEP0LOUK2LPrQOJJ6fzMrEsuGXEs_J0TTUjOqaqKvLniCFdMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/29783" target="_blank">📅 01:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29782">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWyzWAngF4E3VRAPqk1PmkDL_7Zcs5ve8b48G7XgBejcL2UzTMqmH6SGEiWIZmemn2vU8NUPpCMGBKh8jEBshp-uqnTB3hJCZhCXvFfHMbO-kWrPqRwYMMGcM4SAqt9Rd8rhuxgh5ad8VfbMry1j2Pp7ffQCVIA9maXRmpeC4HIVXQvdC28eEdVzZHKd79p5KDKUNkseoxZDXXI6glWGuJ_ZIKcUs59zZGbTzgfohLuGPJ_59O4rPF9jgBGlY4-kfITWyEGiwahch1dKNj46RMGS3Ufv1CoL1yzac_gB_Ir2Qykv16HBxmMCjQU3tFK4Xr3Y5uFc4uCUXb9kJEz7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ تقابل‌لیورپولیها با شاگردان دی‌زربی در کارابائوکاپ و مصاف رئال مادرید با الچه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/29782" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29781">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP1vvnH3kssCyKtUKvzhLg8lQ02wFXhMA-cM1SDYxD7uSirWXm2PZ-NFJiBaILHTOhnJBfCly4ISvJuUUwnhOZpI3JuCGRGcm88WejYmeAJhyXdJbs7jXih3-giHVLr-kiErokxToLBcmpux9vJYLAxeWgZoGYW3eNwAbvC9te9kHbUJTM6DmcSBBc4PYg74UqNJbODm--p99E7O0nTjDv3DKrQxYsn3gB3jzz-XqSOuPjD092rLHYrfuI0kt3I95TE1cUWlWTMy1XPvmDHZQM2wo0tjI-vF5OO-HrvjQ9lMGvYGM3g4bXLi8jy3M9s8IbSsFAiQomIPUZNUttPimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرد شاهکار استقلال برابر قهرمان قطر تاصدرنشینی‌یاران دیبالا در سری‌آ ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/29781" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29779">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyET6BxKQmOgaDQJ-Gc_XXaQl4q91dsEYmQpixkaujOBF4NvP_Hp9T4SxGbjEpQmk8xlJCzjdvq2fz6DiHhxilNzgYimuJ-CX70Nv65KGLBUfyf6Q72OKdmXocFCrsRPKRmIiSKZtXeQEtTsXSm1REVB96Ud8C47Um7QcanKq_dUQDPmyvCqlS6FktdBq8vjCHis7IEFqcAhTH5pSt5-7Gc6yZ2h2v5R4d0ykfN_l5VGy08uyNv2PN183tKPBDC1CbsmdyoUEUG0GZ_0omftOkMpJPOgA76kCo02pvf1BJpCXsvJqujh8kyPgwL5ZkkfZWzscGpiJGDsPZSHu-cU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیربرنامه‌های علی قلی زاده که رفاقت نزدیکی که با محسن خلیلی داره با توجه به چراغ سبز علی قلی زاده به پیوستن به پرسپولیس قصد داره این بازیکن رو در نیم فصل به پرسپولیس بیاره و صحبت‌های اولیه شروع شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/persiana_Soccer/29779" target="_blank">📅 01:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29778">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCY8LkflslenX4thrWy6Ff49T8sIcrUw1A2_K6Qrym1lo1SLVNnMh8GsG87pWXs3p-7SvqDOuO0uVA-a3du6cmCwk3F_gleYRNP8ryIspTFNwEdFLQ4168gJ3gWTZkjExrVIb_vwV3Ulai4fdsNvqC_9gJfF19AOfnlVvlq6MmohVDlXCO8YMjoXoIpRdu6kNsrnC5dMVBFTFrhblSz4ZxKtd_P177cl7AYcldLjAB4aJyMOS2wNIKlNbKzrYAY-62Rxif6_I-b9ey9zzi5C3Hneu9jyjL8YVeOxiOXZHGyhZbKt9avsRn3pGuwvih5YRlzKboL8R05AbXZMSRMSmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/persiana_Soccer/29778" target="_blank">📅 01:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29777">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx-MFbQWZ8F9KTQ0m1-eD2l3Ps6oV3rNz6Zxld3HyfXqiQaq3UJ0Qb4COfQZwMoaPr_LVNdi690Vp9x7AlDMCXTm-IZrR9vjwFl4V9oi4pGoEXqvyj1413guQ2oCpRoDNKPqsG0N86sC22sfhYtsJMg9Dej7EzWijGn2gOBeeWXm51Az_41S7txh4CRfpeSuMjo6mhPdNup-M_T24cBE2suBlfMcbByFjN5gL0Bb2jk7LnYZ0u4Fg2AEM6AUE5nGoNZHClUjf7BXhMqI5_aBeupxwXJ2a_1pkyIQwjUF0j3123AgsLXQX-Q1Slg5boFCu_PlDuBa07BPYc-4_lpR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/persiana_Soccer/29777" target="_blank">📅 00:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29776">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0PrEanUuEInfkQs2xYqbBO-R9kU2HkUGgpY4C1-Wg6wPgHctd7wJrM8Zs4cKoGyQSNjFMVOQ9YujZ4YpCzhwCkd4i2P0EXX9Ivd0qEROXmIbHhpa3Qg1nctiOVIUrR_pZWm14D7YApoz7C9xRUwZb4OONP7Vq9fBF4h1IMC-GklEORquT7IQScKxnzSKT6wPnzNDz24-x4ONTZxei2M0rrrHFYL4642gQWMJZw0YES9tT9fJMhs-zS88jQTFL6lBTIGrMbMX_DK1y9KBDQ1F6AQZFyjF5iBEsv5reyzHGvBzrYJHuvoOHU48uPHylKYBksrk_os3C_mNl8fRDwU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال‌ میخواد درروزهای آتی با پرداخت 800هزاردلار به‌فابیو کاریله پرونده او ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/persiana_Soccer/29776" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29775">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niqFGeMUv21OPxDXLjNCaGRl99VbhbN4eDAxxrzF36jLMdInqJwZgCsuTZuQJE82HO_KgwRW9AiQuRN3gsPVwbgE9RcNbidNYmph134ZeeeZvAORu_SGNdvcwKXHL5IsUcDYtrat_T6PgBrVyDeLRzN3tv_3HcPWlBgWZVGzbEdJjwtaOTvIQ-auwStDbRM_v-ywa1pnHaD28uouaWt81NEN04crUKHdvOXMSJDSPMUTnubbG4qsmQWay5odTKn5OdErj0rv3CfAHewF1viSEB7Oj074qNvU19vlM-CdMMIOiaDfOMxeNtB7l-QqNVnyN5YRbj2Yc7kjQcc3nPS0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم سری‌آ؛ آاس رم گاسپرینی با دو گل سه‌امتیازارزشمند رو از تورینوگرفت‌و با چهار پیروزی پیاپی درصدرجدول ایستاد. شاگردان سسک فابرگاس هم دو بر یک ازسد پارماگذشت و با10 امتیاز در رتبه دوم جدول رده بندی سری‌آ ایتالیا قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/29775" target="_blank">📅 00:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29774">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la-M6RZQvgSKJo3euvwrWynCwcQkzrtdiK13eBTu05a2rKHK9gX__GN5MGnm4kA6oG2cE9OAbiqizAM9TG0NOrjDUvcqxKooZcDmd01ZUNhYNSfpYNXX-FUV3j8IpEgbfWr2Nm5AN7e4hDu24GqBqnnhWGiwQoLtoulJhNlEWG4FqUsvjh3y9CS-19dBOjKYINRcTwXrJBTnZuUE2J96NT54hu8rbJzKiXYkWHjrVa1PIQp6VTxtFNl5GTSYlJnbK-PJ6rAkaNWrGovpPrrQlmjP1dZWeMiw5FaIySY_jTrlyX7fcsnGcVZQ0HRy7AWeg5lopDw1-JqRfbj49nUmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/29774" target="_blank">📅 00:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29773">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTmIqO9Wavu2uiWFZHmDRKR_OCJSojlGJkvhpHWvVReVaFMUuyBxJkJqhHnvlbB3fS3NWiIoOKh68qKdTWYuxk6MhHfBE67fo3cvG8m3ZgJVtNVX6EW4LXNxW9ehuM_khsOVPpiMIH4_vbV5Fq_rAnncGA6wXMhbFsnhbwOVh4F0wE2lF8XdGqoYQRP7EisQiFpypeA1ALb-jHkYBxVnqUV-AUxLELAQdh12249On4isW6y_yLU261TFwLEQJNDvwVkToJAATiTg3-PQejzbz5N_YaXdZXeUPmXS6k5WuHPy-KmbSM4QiWCHJZ84Cj7BE3gpO8rKnAaSL0HIYGCbOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/29773" target="_blank">📅 23:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29772">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp_HPv6lAjwj__DawcfcqzE7yNfcvk3w_tdXwZtnZxCGSGSyKWYHZXnY495JQiMJ1prlPtg5ObiZmXI2nK3XII5Kx9vB-sF4SjzI0DvOVvz3yq0_Ipzqn1p8PttP42GkNR6GVox5ZLkYDvBYPyYnd9xaoWOgmH8XpXTjZo1aS3sr80ZQczU897QG2QU4c-BCK_MTkg4WEtOszel7UP8zFtqCZKQGo3G1zfgMY0jlk5ZKxaMka7gdwwKfbg2G5Wr2Bp20imeYAH5ERrErac0fkDa8vkp5qJhfutT6WJwY-wkCUx_ydRrlVJbLUAZ20R1vHNoRWL3xsbFd9aXdiUWFbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/29772" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29771">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLKML1cpqzy2zFAtaCeF1VKy9KhWzs1hJU1EZv6RH2Kzkfvp2j7bj6qlOJWgq-HSIqaiZ67_ZZ2anelGxXwoams0hc2u1dQgDkqzmDjNW3ZNvQHI3qmkeZv9Z8Ig8f7sOsXjk4LbAk24wIMYM0nPGrCTnwJ5UmDxNuez7GoWDu-VliwznbrJ9B3VNABfnz2n7eEVy8MqjTHufeI88XAO9uPI1ozM_rS_fn1ZAo8BGcypFqyfVfSHH5aRYm7oW2tbpxp7zxk8f6tCQOs4x-v-CD9LJ5AFkEwMO3ee-xyDhMDUfPDDx4bdGbA1e3_jSfyESxPz9x7PxzGaOWGDyBEtHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/29771" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29770">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=CjKTEz1k2jaSvbO_Ck_2D17zApOTL1wIr77ti6HGkXrkv--CnSFao9YFEbPr8ApyL4SvVDZDFEh6sIqZh7gGpffGxsayeRlrIbc6xO5xVJmFvwdg_J7q-FexeM_E_1uX-ZH9efbey4ozW6eWkDDhVkHVjpqMY_JfwOHAidU2qSRp_xgjQOEmRMgXrfKeVRBBq8v0JceV7q3DXb7TNLcwZzaACvugGTLVkb4YPOZV_KiVPgq-5SKbzXLpBRTYMvNLH3KcWBusvLCUYyvBkMrbhb52mPj58DDEd0Zs_LHGK_2ytH3-DHxz7KU5oo4K-hQs9jswLGjml9NgrMROBNyAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=CjKTEz1k2jaSvbO_Ck_2D17zApOTL1wIr77ti6HGkXrkv--CnSFao9YFEbPr8ApyL4SvVDZDFEh6sIqZh7gGpffGxsayeRlrIbc6xO5xVJmFvwdg_J7q-FexeM_E_1uX-ZH9efbey4ozW6eWkDDhVkHVjpqMY_JfwOHAidU2qSRp_xgjQOEmRMgXrfKeVRBBq8v0JceV7q3DXb7TNLcwZzaACvugGTLVkb4YPOZV_KiVPgq-5SKbzXLpBRTYMvNLH3KcWBusvLCUYyvBkMrbhb52mPj58DDEd0Zs_LHGK_2ytH3-DHxz7KU5oo4K-hQs9jswLGjml9NgrMROBNyAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/29770" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29769">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0Z_ZxzMstolFMbiXAMBWuzbsPNC5HQYVYV4_RJ-Jvu8jPTZD6w4jsnQPAbz2i2bulf3lqMZky5OjDd9GmjeTLzAOm_6HBjFq9-EhqDWP5cKJOMgF7A0lrkuuDVy9nDYpf8JfyNVQm1TR_XaUDlmehhRS1CzZ4opSEETmvg1ERzUJAna2EMhSA_qC1wvWRWV-2OUKLcIOqC0EmK_JoIP3rnkdvuNc2sM4Ss9AsThCTktq6rePd9W5todv6kxdPPJACIB4d0_0ymHJdKeRoSc2dRti-4_Fg-4iRrb-khstr1juNePY2Hl6DlYBAf353ijlRpOXfogQcnJNCsTVdDzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
اظهارات‌ جالب لامین یامال ستاره بارسلونا درباره توپ طلا: "فکر می‌کنم امسال من لیاقتش رو داشته باشم، بخاطر چیزهایی که بردم. چون از نظر من، من و امباپه دو تا از بهترین‌های دنیا هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/29769" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29768">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=YfDXwdqsLUAyuTalforhJxBByROx5B2BbUvqBXX-3wm5DKV99Z-sfL0t1Yd5Ir36HOCsP9_TxcovyHL5YttrlV5z1taGsL2e4vDyrzL_L3WDr131VHeeFNFvZz7sxT_b7hUIgo_EV2INj432rjl3obTi1O0TGBV_aMLyoI5NHcbY4mL1wrwkmaYDaBQ5nldqeflSh6mcyWib_AWL7ejBQWskCJ0s8REuw6_qKAPUe0k38g1DH4aPUNcrkd3xJ1RnuWzL6IGADRIzSnb2css_8praeb2uSekaIYPxdBpKmw6iE9ZB331d8GIYj_Yl9U7yLHxbFx-as2cbnbFlvPqiFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=YfDXwdqsLUAyuTalforhJxBByROx5B2BbUvqBXX-3wm5DKV99Z-sfL0t1Yd5Ir36HOCsP9_TxcovyHL5YttrlV5z1taGsL2e4vDyrzL_L3WDr131VHeeFNFvZz7sxT_b7hUIgo_EV2INj432rjl3obTi1O0TGBV_aMLyoI5NHcbY4mL1wrwkmaYDaBQ5nldqeflSh6mcyWib_AWL7ejBQWskCJ0s8REuw6_qKAPUe0k38g1DH4aPUNcrkd3xJ1RnuWzL6IGADRIzSnb2css_8praeb2uSekaIYPxdBpKmw6iE9ZB331d8GIYj_Yl9U7yLHxbFx-as2cbnbFlvPqiFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
روی‌سماجت‌کاپیتان‌‌آبی‌ها؛گل‌دوم استقلال به السد توسط سحر خیزان روی پاس آسانی دقیقه 47
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/29768" target="_blank">📅 23:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29767">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=dhxGtTQlTZ31PZWA6CDM2zZrHgtlm5umDgZfCK1eHT1o7nVNyvy4ELURLUV0NnY975qGIVl52sQXIKqV-iNvS7UbIJkDAlZ15tywFi-Iqr4a1YKLB73ycENXROKNV-u6t91XVPdQ1T3M94J98aaA0fFfYZ8djI2x5piB_WcJvHgRKA5tDM1u02CeLVi1rY799UfjMw-ckGpBvsWFBG1jcBQE-mFP6Hl7i54PgRXk0eyh5cGmiauJWLr4qSisUfWx0-nltBsMbMxzeCDeHOkP5hLmVAfaEBlPsQsXDyL0PFokRjGymPCIL2Zha8ipdLr8uule-gDRoDuVdJAHAYRmOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=dhxGtTQlTZ31PZWA6CDM2zZrHgtlm5umDgZfCK1eHT1o7nVNyvy4ELURLUV0NnY975qGIVl52sQXIKqV-iNvS7UbIJkDAlZ15tywFi-Iqr4a1YKLB73ycENXROKNV-u6t91XVPdQ1T3M94J98aaA0fFfYZ8djI2x5piB_WcJvHgRKA5tDM1u02CeLVi1rY799UfjMw-ckGpBvsWFBG1jcBQE-mFP6Hl7i54PgRXk0eyh5cGmiauJWLr4qSisUfWx0-nltBsMbMxzeCDeHOkP5hLmVAfaEBlPsQsXDyL0PFokRjGymPCIL2Zha8ipdLr8uule-gDRoDuVdJAHAYRmOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/29767" target="_blank">📅 22:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29766">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDkDlsy0SmQweMB5dDhvAKj021CqJebVE45IQko8dQSbKJsNbc2WFHjikqGt-y33p6G6F1btnSguRHRCBwChtQ8mH4NACgBGsf7LJMRCTfV6L7jTDiBmD8yq40Ra3jm6xjFU7W255A6lESWSwPN_wX7jc3hA5Dp2dHXdrW3kwt4sY8y7k8OyzD_PajJ2aYHQG22mCK21vj0OZpKJA24p0lGPAeYGNeft4gVIQSv2ajT6r9yuYyBhDYUOD2gTn1gAKGn-JxOu5B9vm6zSzSfZwF9IcSrCAU08tme5aVlVl4EslkycBKrhHAyJuOcATZh0DLWt0LGPYiIQCnAgHkij6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/29766" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29765">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxnjAM9XL7YKuCE6Mqh5Y6QNs-T94asgs3iJhRooeqT_mLvyyONoTIv3gwJrTBBO3jU1conTNscMnaJ3BHX1DhS6aoLm33nIprFOHikbI2F_WyRWAIQ-s4cp9xrdWQlgV5vPHiYVSlhH-eGgbv0UUuXPHS5djZZuREOOHYhV9UtES4ExqSLw_YTKzGekzmAmzUCuRGZ2Jlw5xnxk4ZlC555Jf0j1UqI1pQL715sX4dBkpqDHWqnJ_B43MM5SRxZobDo2yMSvi588-fBM98BQ2pJlxRtBof2GVjev_FMVSWCQ-UfqSTtEEJDvlkVxzj1n6e3SRL1EKh68HpRZ-m4muQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/29765" target="_blank">📅 22:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29764">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=Mvu0JwXsQrtK2V88uRDd-nKvnpeuPyyoXHcGsTW88aZwYZlGIJacC1zWDbt5xTyOL0m7bOQPFWs6yu_9MTpfOyCUg8jTuds7eXEplXh_i2Tq1qUWBZ2Sj3EATXVm6HbiUO9iX4AV7G7URxxzTJi-9SxoJgdu6BBvUm7Jm2o7_U255EeXrlnC1gek5ACwqWhC2tBK-qZTo938XSDPLLIrKMVgBR-xOvaEKOtqGrMs3pFvw9gmLpeP1eutiK9PXiHqqZFp9KqEDDjhFoNgj82bab_VDs1KZfg7QiyafUdnWx3Dx3IZJs5VVI6ITX7vRykhOCz-Y3Ce31d-XAtjzmzytQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=Mvu0JwXsQrtK2V88uRDd-nKvnpeuPyyoXHcGsTW88aZwYZlGIJacC1zWDbt5xTyOL0m7bOQPFWs6yu_9MTpfOyCUg8jTuds7eXEplXh_i2Tq1qUWBZ2Sj3EATXVm6HbiUO9iX4AV7G7URxxzTJi-9SxoJgdu6BBvUm7Jm2o7_U255EeXrlnC1gek5ACwqWhC2tBK-qZTo938XSDPLLIrKMVgBR-xOvaEKOtqGrMs3pFvw9gmLpeP1eutiK9PXiHqqZFp9KqEDDjhFoNgj82bab_VDs1KZfg7QiyafUdnWx3Dx3IZJs5VVI6ITX7vRykhOCz-Y3Ce31d-XAtjzmzytQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امشب مقابل تیم السد قطر در هفته اول لیگ نخبگان اسیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29764" target="_blank">📅 21:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29763">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoXnOkkmn5G0cJynbVVYuJQaPb2_GYp0woa-GbIO2isreOGTA0VqeLlY93tY1rXVGAuX3qPRFAhanAV64hFv_Fe58XlakjIfkoMqBPrfu0M96EzueXJ69mlzIUWZwKv_RBLfi-kjo_Yj82dCZ4ZlpX2Q1KK1Qu5jyrMtKBXWyFU5Do8zi1bp3X-BEjqXv_AJmFVS2FEBve4XBk9gLXY3xNcxLFqGkp0I8GwXGkVRBhovu2ijQ4GWBoztsGulz6TPDmMaJNpnJCxekkRI5NfdVAp9GOdyxjtAHJvBoFiKtW0JRdPpAxyp6hIudQXK-fwswVpQeDC1To0_lrdlIrHltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل اول شباب الاهلی به تراکتور توسط یوری سزار در دقیقه 22 روی پاس زیرکانه سردار آزمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29763" target="_blank">📅 21:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29762">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=g3b7yyx_2fZ8DJ6C3KIXII2lUc89BFkVXYcdCrRuzqsLciChmGNGl72PKAg5RjgITZ3o_6AJLojjR8-BxPQXsDti-urACfZjMqIcjZ4cu5zqTykKVCXsw3bUTKfS4JFVaJTBgj7y6ZBeTWvsVaJ3MqYyOOYN54BCF7cHYF-oCZZF9NFbc1K6fSInbCCMopGpg9z4f93uHZJU8KWiql1NKjEc-FEFAO_7T-8pPJvDQ-OQDWlxbrrB7uTyHb7AqNNtwdzXael6RwhRGNJ2H-woP-3byEEMpdWjrnRNv6NDIFLAYd4QKpwflA-KSEUFDYPZqTZeFxlVN99vZZ-JfoyZYhT5wofnAfQXaIQ76wLXpk20CakcJfKC5_C38Ut1ENwBXQjXIjITQxkWInjKtdYzAIjnLcS61J7KalhzO-Lp6i_1UeZsfLEQdLa8prV9rbTvUiJ7XmfxkJjw8Rs_A1uZDJ0-wm-kUmpm7aM2tpiyMD4OLVGMWSTfwqhBothHE62D_jflOBrpruD3KiV4ILn-JOFH0nplf99o5nWyChj7w6pnYC-SN7dx3JHk11akAXbuSBaGSesw22vW6UHQNFPaxcePCykTRgxEF_Fh2QxHthdLfBszcys1X_z6D4YJzjFNrdMTK36DXDr_YJdjREqKOjvkW0GIAouLcIWZTUeaRA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=g3b7yyx_2fZ8DJ6C3KIXII2lUc89BFkVXYcdCrRuzqsLciChmGNGl72PKAg5RjgITZ3o_6AJLojjR8-BxPQXsDti-urACfZjMqIcjZ4cu5zqTykKVCXsw3bUTKfS4JFVaJTBgj7y6ZBeTWvsVaJ3MqYyOOYN54BCF7cHYF-oCZZF9NFbc1K6fSInbCCMopGpg9z4f93uHZJU8KWiql1NKjEc-FEFAO_7T-8pPJvDQ-OQDWlxbrrB7uTyHb7AqNNtwdzXael6RwhRGNJ2H-woP-3byEEMpdWjrnRNv6NDIFLAYd4QKpwflA-KSEUFDYPZqTZeFxlVN99vZZ-JfoyZYhT5wofnAfQXaIQ76wLXpk20CakcJfKC5_C38Ut1ENwBXQjXIjITQxkWInjKtdYzAIjnLcS61J7KalhzO-Lp6i_1UeZsfLEQdLa8prV9rbTvUiJ7XmfxkJjw8Rs_A1uZDJ0-wm-kUmpm7aM2tpiyMD4OLVGMWSTfwqhBothHE62D_jflOBrpruD3KiV4ILn-JOFH0nplf99o5nWyChj7w6pnYC-SN7dx3JHk11akAXbuSBaGSesw22vW6UHQNFPaxcePCykTRgxEF_Fh2QxHthdLfBszcys1X_z6D4YJzjFNrdMTK36DXDr_YJdjREqKOjvkW0GIAouLcIWZTUeaRA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه دورتموند با انتشار سوپرگل دیدنی و فوق العاده فیلکس کلو اِنمکا در بازی این هفته با پادربورن مدعی شده باید جایزه پوشکاش 2026 به او برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29762" target="_blank">📅 21:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29761">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usxtkU008a8QHywotfCVxkXjbrT1zZuNIqKfui5f6IyFrKLGyDUKwvv__Eynq_I6QXcWH-Rw7ctzxV16BSGjfEYKPGPX0k-AeBEdDTGam5Qf4-UYZkKlL0RT8_n5ucbZYzg2oceChEIFUKfTjbHVrASWEr0-4Ycr9CWaK3JrrP0np1Zr3GyYtclCZa56hdD0g1I6Ftb4AuRBP3sHyIOM4-8l42bFubCgpqqK5HVJteVD3XnXMXAfLU5Ca8pIan17CB7RVxbz6kQ-0lHgqQ2vOuRbiFUSUoMkIWrFtT04v9v4WI-JKojzsZq1YAXXBBQvDg9Pz9oF-XU_lZg-gHWeYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29761" target="_blank">📅 20:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29760">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjB638nJMe3CWdPcxSnFuN4tKF_xvOeBXKCtr3G15Ptssi76zwvuEug4dUmK0nICrn4bmdOqK-UjEkn4ozcpCuoEe90w4tdDOw2zHjZD9lOhqocSxKoExJmbJTCI--E42HMw5pbsG3-oF4aoHYNfC0PUPRYFw74xUy1cMCElOFwZPISRq0df5abDE3aUapuVw7To9bgPfK9gNcByc7IH4XkxdgbT2BdtyhdM8-0oMpeMBhJL8qcLTCR7_PwFmlPWvnrZLk2CApxxaTuVcYp2nC0HUOt6oWXnYwBuqkvEuHADIGvxzP_mEQNNocKvWVCTL0UwBCCfZqDijIwdWj73Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29760" target="_blank">📅 20:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29759">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODGTmKB3hQ4pqArRwlfUE6d29U7CDDQNZc4CZ_uArWUMXQgu_rIGlYgZK-1yZAWItSFuUcdxuDKym71rebDc-CPajYNHZZ_rhk5gulPwOtwKs-Uf-FrHrFE1-OjoDJeTcJm7ChFAiM3qbToqXzqiRJY8w2JbDjSRwR7N6gJGeG83CA5LuPi21vwdnlNCqrpfsjhNMIwjWL_QB7Y0t2UopyTpfsYMz-NDSt-9fWroh5P9yIy3GRQJy1sNQdoxR-NX4VUy6efziYgrvhr0ASKTMgdnaj-3byZB3jAYTVu54XlbAzTjopZDr4Ev-zpJffkqm6Ey3JE-mJbJP9vBHAkB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔵
شماتیک ترکیب احتمالی استقلال برای دیدار امروز مقابل السد قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29759" target="_blank">📅 20:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29758">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8__q9j_DFIRyfy5ARCc107iSzBOE7wFv7-M2svKqzu1FRWYH9o2ZUUseKYOu6qYzC5LBAmGIbNRef8_E09WFo3hpPzqQFMBpiDshTzdq7MAm2ucHZZT22tVgofp4cSpK8jnCOVYy_LvnEGte2xxNTvY34tJGvUt44wGRMTj8_7Dxa0oVNPUWGZcNpoakuX5cvzghDysHVvGKmQhhg-K4bWsZ1T3TPFa16MNs18XoRDryEVjE9FM-ivwW1_d7wgfQj-aXOBZPZZXsBTAMYl6xlKKLgYjmFZOB8_E2aXzSeoCc2MeNAfkbVBWoL_TcEcxR0HEJQgR0ZuZFo0wImfVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سوال خبرنگار از بلینگهام:
هنوز هم گواهینامه رانندگی نداری‌نه؟ جود بلینگهام: نه ولی به کسی نگی ها. من هنوز راننده‌شخصی میگیرم، الانم کسیو ندارم باید ببینم همیلتون بعد فرمول یک چیکارست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29758" target="_blank">📅 20:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29757">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=axejkdwk7dWY4s6I5M_CCyQ2MCMPaOL9YLv6tXLQ9PVa5AqOcz9YI0mI5w0DOoPn88owBb2jAaSDSzkW0OtQW6CigUJY67auch4q1dcCh2tbb9-xAM8YnlgQPUvkmLiPHnLGbVwdpz4XplKrSlOUxA6LWD2jgJytUisKLPzasPO9JfHcxHYffxfOPUUaZhYLbs_mSfHQXwBbFEzY47zO78uiI5FBf1W15-K7ROC94YVEJpdXVL6awExiniXJHJE0VDzcEarQ4tigs6fKjvw7kM2KSxTrq6zuIJUdPe404m-j1AnWJk9yuRTdH0f3KrwJqbyB2TSrErEkYFT50EGZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=axejkdwk7dWY4s6I5M_CCyQ2MCMPaOL9YLv6tXLQ9PVa5AqOcz9YI0mI5w0DOoPn88owBb2jAaSDSzkW0OtQW6CigUJY67auch4q1dcCh2tbb9-xAM8YnlgQPUvkmLiPHnLGbVwdpz4XplKrSlOUxA6LWD2jgJytUisKLPzasPO9JfHcxHYffxfOPUUaZhYLbs_mSfHQXwBbFEzY47zO78uiI5FBf1W15-K7ROC94YVEJpdXVL6awExiniXJHJE0VDzcEarQ4tigs6fKjvw7kM2KSxTrq6zuIJUdPe404m-j1AnWJk9yuRTdH0f3KrwJqbyB2TSrErEkYFT50EGZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ضربه‌سرمحکم‌سردار آزمون‌در دقیقه 7 مسابقه که وارد دروازه تراکتورشد اماآفساید بدرستی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29757" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29756">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90deefc883.mp4?token=ELBTYqMfid_AkzJnJshS1WVITOQZMwzPb7L4Qnfq1QQN0xfhcOqhbu2-z4sKxX-FvfB1QTsOj7RYeEFERdF88HnfQOs0dj71o73QQMjW8i_qx61CKYK_qVIMnEVmPCw2p_Fz1YdQwpoWoZ97Ma2fEYeRJgczxvqV9PIVsh08uLZsJM3VtEeRNi40zKmRPbkTmPs3EgGNAF2A3i6GJLZtOYQKq9NgWdezdLWOsLFKLHd-Ypi78p25cui2AU0z5Ij0uDnrP7EctogkF_XKyrDBWDRCEpWBkQYY_t7AwuyTAMQVmr-YAsPwivZdiauXGYn8epc4EWPjYVtnSttb3lBxdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90deefc883.mp4?token=ELBTYqMfid_AkzJnJshS1WVITOQZMwzPb7L4Qnfq1QQN0xfhcOqhbu2-z4sKxX-FvfB1QTsOj7RYeEFERdF88HnfQOs0dj71o73QQMjW8i_qx61CKYK_qVIMnEVmPCw2p_Fz1YdQwpoWoZ97Ma2fEYeRJgczxvqV9PIVsh08uLZsJM3VtEeRNi40zKmRPbkTmPs3EgGNAF2A3i6GJLZtOYQKq9NgWdezdLWOsLFKLHd-Ypi78p25cui2AU0z5Ij0uDnrP7EctogkF_XKyrDBWDRCEpWBkQYY_t7AwuyTAMQVmr-YAsPwivZdiauXGYn8epc4EWPjYVtnSttb3lBxdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ایشون خبرنگار باشگاه شباب‌الاهلی هستن که پیش از مسابقه امروز با سردار مصاحبه کرده و بهش گفته مطمئن هستم امشب دو گل به تراکتور میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29756" target="_blank">📅 19:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29755">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oo9oTJShv2fl7rL1Qbn177qREdaqLFpBW0Hpeb6xisPMWtQEAhxmL3pBZ7QSCf2TdsBOtF7i5EJU8vta-xlnLQgn8_31Iyom378n9e8s6iHwa0ZzfggmdO2tqnkONzEHLRvmti-G0ExSoi_lxejJ4HgM43jY92Gm64zWiADM6bS2KaGOt54U7whxfcHWXPOGiANJ80MAxGIhnZjeeEVlYbcxXzleWSYDDlJnrPfa71Si4zasan41gFlEz4fjzbh7NmW1Vm5KnwYrpZZLNxRYSoYBZ06f8HwmNAbKmddnuZhzt5cAowh-_ovqU87Y-7gDCFkmM3__TjzM44pc3y9Iog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29755" target="_blank">📅 19:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29754">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHkOAEvGto1Qqlvp1STjpmoSpABrT83Uyyx45NxYw8iXpN24AbgLqcdq2k36GOvzzeQOJzFW9oEhTWBavLjtE8jVVzdUDqKJMRhrQ-jl0YHfQhS6vvkuVkgk0c31chGDuaexwCKqoxp-B3zguq7698ssEOoCOFYnu7SY0xBcq6nS1YYzDCSFqeOSF1PSr2X3PsJDMI0X8TfSBPY7bvpxibBVg0AJ5LM8w5EffqAGnU5uXHobniHbUhQQYjeSG4T_cqp88YicrZdLCgGIUO_P_AgKWU4MSdABr5oZ2ssiRW-cqywCKFW_p1bOMZof0uZxX1ojdelt5VXaI4Ggd-1vdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فلیپ کوتینیو فوق‌ستاره‌برزیلی سابق لیورپول و بارسا با عقد قراردادی دو ساله به سانتوس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29754" target="_blank">📅 19:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29753">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9Rn8lBVZwkIvquW_XoloshV3lUScAB3MxT0Pe3hlOSdjsey060x7jfEyvygr97t9Qb5LPlCi-9KTDlMB_upPE2kzaVlvC6DG3BFMpmkSvvrE8wsPwv1BPMq89p_-7IUxCfNJgERcZWdplFBt82--3nx-6BXfXw7NAcqBt6Sd5qK87eDhIPAymkC9BqilFEcHpiWNtNLvcsvz2yv6S5V763hQ6gaNjeq1_A3-De8auOejEkKDVnRHfUkML4vcGV1-V7EkSuiLQKmBz0OsHp5uautgi2P6N4-3psh-kmv2S23bnwpgizXVz3KASaUwhoQHa3G3IORMH4nND8E_tQIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛
مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29753" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29752">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZr3JmcVUQXU0Vi67EJWim5z8FWZjwl-XMNI_Zx7cJO1OFvqRWehdOcQD69o3vcCInuiKT1MxEGNyV9uvz9AQBfVC_pXtTSZtcplkMOIUpvN1o35OifTKc8ox966OScB96GywQHvqpITPKlEjrd-4XxpjoH2_i-S6NGRQxRmBG0TQRPciOKcL996av0yPFaOrkgDmF798I4X_-1O1FaPJYOBabhaDX7anJRQyKWdyr5Cz9X7Pqt6iXB9cRiVHvskZxEkcBwVBYZgXZUoebrBu5Wgg9OerLPbq-RXY2tu9A4uayZ1N9GV45iKMowfpDDhYReelhNeNFN9wAfk8RHQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29752" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29751">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPGHqzfD52boH6NYh5VK7UWROMKVjMuRGMOsh90CLCC8gV-OpyI4rx47xh51XmmkDhYbxv4s5aCAKS4zw7_qKwCYDs-pyeMZST5hf2sNJm9pMlNQICHZDcu8DnmZxDBiVJQLmR1vjtWiogfvKRWNlDYhlPwdhuvzcmG-ODW0oKOIfZjHxjsVzkThjptHY3O8SaMsqcb1QgjVZHAgT4539-j6yy3fecQ2riAqmH4fycHZzdxuV1JMBEZ0STFqTrV4Y52Wz8c_dckp5KAXdkHVUjm_SZ96UVDWKFWXaWrXVOoR-xrLefvx3xLATBBQ1Zvg9twS8ulORLWQePbBq5onBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤝
دوستان خود را به پین باهیس دعوت کنید و
🤩
🤩
🤩
واریزی دوست دعوت شده پاداش بکیرید
🤩
برای دعوت دوستان خود در پین باهیس بعد از واریزی دوست دعوت شده به پشتیبانی وصل شوید و همزمان با دوست دعوت شده و برای  واریزی شخص دعوت شده پاداش  بکیرید
🤩
برای آزاد سازی فری بت دریافتی میباست یک بار فری بت را با ضریب 2 به بالا کردش دربیاورید و سود حاصل از فری بت را برداشت نمایید
💬
برای اطلاعات بیشتر با پشتیبانی زنده سایت در ارتباط باشید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g23
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29751" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29750">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPyIuMCAN924c9OSetKeeu3TemPdjMkqFIMys75BwhhBdf2LNRrCGMARVPqiKJquVyiaVlDODnsH8REWZCQ6yYUme2JU8NOEPUMuwUOO5TKqXJNP1j89tjgVvjOlIuF_GKi7DAEISkI5awXXeCYAdtGetbtbl_4L3FeHrxZ0c3X3N4ChECtrNS2k1tNwTv6KCHpu94C-vV8PsNHtItu9DJIBE5Ah8xjq-frZoIZ-PrtXINpKnX0wjISGzLPKsI3PODFCimkEYFfyfAKQKn7BZDcHohrHSEi4oxWJTV7Au1ixmwrIsL-smorpe4zBEMS6qBRHcXNpF3VJdJsvND9IXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29750" target="_blank">📅 18:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29748">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHYU-eRuw1QIkRJmpXqkm1BZN6L6sQRemIpF4R8Ap4MzuY0GcpvN5baLNXcNnTqpGS6PC6sOpdeMCwHx2xDAar07SPOLJ3cZ8lT-LfxhALICrWnkOkwO7Vh7ofy0scT00u99U_OmwEznAE7NZNYamAPdWeQcJDSVDdUbnXSB3KG6Wn0lQU8foPJJIB8LL63z0bjrhC5qHqAWq_IMTa0DGZe7wzVTG_81iGlsU6AdNB53j5VZ5oUdWImwZpVr2Q4hENfi3qujv67T5N9POUKi-eDKpTUcbdy5cpWfAbm0VuUOLlJTop4m0qCnAvH8Ixf3BmF19jIy41MAWh1V8HNz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhep4fS_Jze8bIjXB5YEnI48in2wUt_uk8NDREncWMJSrVcqFO50Zh37AWVZQLfl1Gg0hEQd-tIsEDut8FQRQclOO_bYdYmkTN1wHQYh0RN1UarMbz0utAyTMnZglkReeHp7dRENMfsGY4xMfS3MB1rGkpDnoDDanTk3FOBU9P-H3xRGidc0H2uN8U5RcqcwENfnoh5dndxgUhWE6Ti3S94HFci8hOQoWZrXFHpbnkI4A_sO6xde-RVho1ngYVTLZ4AECMvJ9vUuydeEVeFvf080JJdPVd9i-Sdrd_vrkBFqcMA0hv1tPODi7PBWR68HLi2z_lQeclEcxsk8E-AncA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا
؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29748" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29747">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxaRsnCyU17PkSkDNKPWVnuXzZKpaS1EtsiynHQbNAMy73B5VSAVL6Ldd0JKQmLQ4alsUHgRK0ts1BTOTb92OyuDJHFhhyFUJD55gFP1T43n9gHBTA4D0ZG1VyNk82nHHzcJIbZ2hJda52xryUDRF-9ZxjrNyd4TiB15MdYrA7UYZUGl-ep41v5YnWTIio8ZXLOJQs8lzBld_HXNc8FqGhcL9CjDOnalks2X4pdDKD-iUyH7SskFtWm5U_QFXEl6paK1WmnscZq5nas9tInTSzhpsQmRroeSxYUlw4ctInql0d91aOwheIeDhSq8wJsjYxAJS4KQ0JknzW7JHMiqjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از زمانیکه
؛نامزد ویکتور بونیفیس قبل از مراسم عروسی‌وقتی‌‌فهمیدبازیکن تمام اموالش را به نام مادرش‌زده سریعا تصمیم به جدایی از بازیکن گرفت. دختره این امید رو داشت که بعداز ازدواج و باطلاق از او ۵۰ درصد از دارایی او رو صاحب شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29747" target="_blank">📅 18:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29745">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adae707100.mp4?token=SoH79qbFZWJ_XuLbGtAfDT_gg943jG3giJaCMr7V1ni9n7ztjNO3t2LhdD4sfDscqgvue0te9ki9Gs90YENooSK28TR_nIMxRw4sxLiUGHEkVbbBM0Ykrz2hYCLDNkcE6DasQ0Pp-Uw0FeBmFUBo3fKb3i_dCC_SIX_4ylwljSwMf53-wpz9VS7D1Goufd8BtbcsacFXCKF3K3bqpf0wUwiBfT8BlHkW5PkAT5Wi54TrDehpROg4JK6UyzrMcqabBbth6aQsCvwmqAZ1ssaNjn8Af4bLlcGcWHjOai595fjpaLYH35xBKZPveg6ivePToq0QSUFSMdSFoEag7EoAAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adae707100.mp4?token=SoH79qbFZWJ_XuLbGtAfDT_gg943jG3giJaCMr7V1ni9n7ztjNO3t2LhdD4sfDscqgvue0te9ki9Gs90YENooSK28TR_nIMxRw4sxLiUGHEkVbbBM0Ykrz2hYCLDNkcE6DasQ0Pp-Uw0FeBmFUBo3fKb3i_dCC_SIX_4ylwljSwMf53-wpz9VS7D1Goufd8BtbcsacFXCKF3K3bqpf0wUwiBfT8BlHkW5PkAT5Wi54TrDehpROg4JK6UyzrMcqabBbth6aQsCvwmqAZ1ssaNjn8Af4bLlcGcWHjOai595fjpaLYH35xBKZPveg6ivePToq0QSUFSMdSFoEag7EoAAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله‌ تند و عجیب یک‌آخوند روی آنتن زنده صدا و سیمای‌ جمهوری‌ اسلامی خطاب به لاله مرزبان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29745" target="_blank">📅 17:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29744">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNyuQ8NpGZR3XCrjpZ6gwC-Xbrdc4RiQAOyv62NAmQQjBh2YJ-9maOqGuoVfiv9pz6GLdVpYAcutqr4uc8dQ0IaY3iJI8jcNPPqh-24rqKPTvG0e1iXf2z8a-zztI2WB60C0vMaKi6Ib8hCKEEqRJK-YbvcJERcNzxTsXPp75sjNQnyKV__gyqawRJQ-1SFeljTRir3Di8v4wCeT4JDdOC2S2XBAtGM2hkNXZFAPO-2C1ABKDs2vB27Q6JNkoAmqLOCuZJvdD-57M_trohiQePL23_D7nVhAXaIQcNk_LZcpoxix1KZKqvaBirFxIiORxB7N90RNsJu7M1Zm1dVYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29744" target="_blank">📅 17:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29742">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY5NjfPt6Y3UI-AvU_YS5cq7RtQIaxYS8r67wVw0Ylnhbw7aav7FeRIKBUthfZdcyWPhqXugOu-dbR5cwryUKVLn5aqpSbRMFx-RUAVGKN29dwDLnfK9iQoRomP9UqV_KKTQHDzug3UlZCzLy7EDh4rFsO-XTDcvDUgLQWobXaRTG1PQdBgTDhUDF98lc105cGXJAuo2UguhFWXt9P9L-cKm2wlYOIArwIDdKt98JupNxSc8VUWppRsX45T39WeP1NnsOabNSRqLokQ3ZFU_1Iagz1PLMl0SYURbrdoBDzGSm0Ft9VIl19Uj73dE9N50v4wfHGLRJuF5-aXQxxLK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگارباشگاه فنرباغچه هستن که معتقده کارتال باید درفنرباغچه‌بمونه و باید به او فرصت داد. باشگاه اون‌فردیکه بطری زده بود تو سر کارتال شناسایی کرد و از حضور در استادیوم در فصل جاری محروم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29742" target="_blank">📅 17:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29741">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAEnFwzIs03miRMdTNiBQxSUqy7Z4sZTRaCIFwl82oWQ7I6b77DN424VjZfwMpgdFs7EEPdfjYPi0oC9qhLnRGOEfvdvzsRpdp_QbRqDuqlLjQ5MZX_gi3m0SWQP6--2Gv3-sZ6sX6AenX9BvkjlItb9IJh3bQBHNcq8giiQjJtVwhnKdeanfh6yvvvnt02ZXBWaCOSvaAdNWLgoZdax4K-JZV9laSbtkzLoaLwzjYfR5kSzDjuT0YjFvrzK0_-mI4eD_P50ygEp7j1VzbmK-KYKSSePUPAd0u8cN0vooUVDuHeigzEu_WTozyFHQsNucs0X5AtKifbAFwfaAjjmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29741" target="_blank">📅 16:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29740">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JixGL7-uuqm7chEH4pq7neh-67QcH37-bjwUwtsMxnzbIIWtZ3_NxeQGMxsy_tybnMn6fi8aExrXS1qT0UGKwCznAzs_7T6heHMac7uKGTXpglffG6Vc4tPYx1Y5sqmOURZOreaSxWdBJ3K67VtvmGNHylnrqaZyYHH6ezE9-sB9_Z9RvDaKO-3_lpuMeTvkJNX6orXqLr_wNMP-sc82tFWQTHZ-5hlVEfeo63KCFuaK6kTVa_zPTEvVqnxQEZfKIx9PqR0akRJoFv8D8-3h0WLNRLNeLE25w1c6MOai0yOvJ9ixeZcRSbtFGcv2pgzTwBbTmjBcy00PeSCbk1xklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29740" target="_blank">📅 16:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29739">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfcI2H0uS91e5ez-liQsHDSn8FVkFFieb__VpioOaKHoghoezCpfub8OiuoNiVaHfGZBt28AJKggBEviARtwxYac44P65KXQ95qxjDDrasNi3BnWZ9OAItl-wu6bcWiP7MN9-anNjRat54tddB9Rqe9Ft9wbwwb42IlcfJy57XcptIQA1dNq87UvLU2MT_-e9l86UrGbMFQY1u_BMNSOKn-Jn3SvKYaJSt-Q-6jhm-VxHce6c5mIpru36GSMb5nkT1QPXjC0KPWCr-ZAUI1Z9RIA2YjL6IRR2xruUxTjEe6bwBNP8qFZdsMiNulgALLNmdBaslgBbuPnQQfMgBqURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29739" target="_blank">📅 16:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29738">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_by2lJHiO65HPMvvegiRdVFeSofmRthZ0kBi7aCQm-v7dmINqXbePN41gXkU0B7vnPknhBkFyCMYCZZS2fd7b8-AToeMljI5vxmIt1-TuI-WDZhu--FioSIOqIUZLBmFFMZRz6VVdGBvXu5WFdjR-3inK4et0I-tnrtlfIxq1cN5Eyy41j7FcTMn4JImhB9fY05AVTEbbaqJCC7BHuguSaUrJf7yKWaqnn443sZ5n-4_JNabRVT6IB5VGAlWE5UEgGHdxuFmEc7eqxcyTTImCzkXqzAk3fNV4c0G_RGI4jBneKDScQ03gxjaV2P-HzJo5QVgNb61R1vHHAF18xaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردلامین‌یامال و رافینیادیاز باعملکرد کیلیان امباپه و وینیسوس جونیور در فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29738" target="_blank">📅 15:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29737">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=vpcq1A9JWwV_mvn0s00RIVnYCCbmLgxs-vrNGfR8zQpe1owIebXduoy5cDNOpDJftVKM7WfCamCA5ChXMdLz4TWri68wGbovBNDdx9ejU_Ryqt5HBqL-gMew25EoLqJJLAkOV-yy8RwVyfYoQ2MDTdCYz-KjIxg0kuOUwLimmokkNwIV27utLFi1WDH2BRXjz1y3DvcmRD-knZl9MtGz2DweisuX7-uAiKBRK1njLwh3alYBJBfUzuAYW7Zvl1YJLc8AY1hc17qZOHUrEByqUs8srCJ9x_Mam1dK9VJFPEz7dj8Gq7yijvgMCyiFbULoEAtGul6bx0hadc3i6DzYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=vpcq1A9JWwV_mvn0s00RIVnYCCbmLgxs-vrNGfR8zQpe1owIebXduoy5cDNOpDJftVKM7WfCamCA5ChXMdLz4TWri68wGbovBNDdx9ejU_Ryqt5HBqL-gMew25EoLqJJLAkOV-yy8RwVyfYoQ2MDTdCYz-KjIxg0kuOUwLimmokkNwIV27utLFi1WDH2BRXjz1y3DvcmRD-knZl9MtGz2DweisuX7-uAiKBRK1njLwh3alYBJBfUzuAYW7Zvl1YJLc8AY1hc17qZOHUrEByqUs8srCJ9x_Mam1dK9VJFPEz7dj8Gq7yijvgMCyiFbULoEAtGul6bx0hadc3i6DzYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛ تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29737" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29736">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpJBQFjG5W8-wKaOF8MyVx-weszXu6Qzd2fsK9A7NFkCbnrsj2lALnxonsYrI-_AilzBwsNQT6f3ovL_96RXSpV0ipyqs6-xdaWH_CRj0HDzK02nO-f9OoqyS5TsduFumcSokBivZODBxHmit62nYzbAI_JGr7ioE59bbNRat_al75vByIlibclsfYFdhUP3FfbbzNwn3mLbpDwTCzRXsG6Al_CqBDf8ya8_46FbnPYeBL9FXkYpepRtx_ljr40p5DWEPOeWUzCX4_X61LeKcIj7bkYbllZuTz5zUHpUtjtty0huez7Q2ecJ8u3XrjQlcTJ-3AbFfvcvGxEW-hP7Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان نیم فصل و قهرمانان فصل لیگ برتر خلیج‌فارس در 10 دوره گذشته این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29736" target="_blank">📅 14:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29735">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXotaOW9391CBQPDtS7MAT3AUUbJRM5fFOdRDg_72dcGxzIcyyYre6pnrwHUGG_T8UR4A5UCxjRHBq-rw1Hiqun2TFMo9C5u5t31VEtfYamQZ_UPcTOeugVT03xG6Y6pdOqiR4Ju4eyDqpCQNRuD9Q07Ggb3NUavJnPaBj1PEt31zNgde8NZe7o3lQp_-h8CkYXIfBMQ8oQOWju3UZT8b5mM3NxBn0enFUbXcJtxkMLWZTf5b4sSJ2GHQoRWHEoptnoxG8_uDRTIPoXMtNw0gtzY5aGeGdk_dwIhiBmbCSCuMxksUu3g_MTg3pLFf5H-8uH5cHvW556UpMKuUIuDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29735" target="_blank">📅 14:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29734">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=aBPTyaK8CjZ5-zE-WjV5ma4DLoKAK-y8ycAuSFCt9DRRFbRP5roXl4Cw8p9abL0EpBb43Oamo-ucQK0z3WN0yOHlq7y41MaPkw4KBv2Bmz9L0yeKvtm0fW-eJSuZB1NSQuwHGL4CaLXzq4cnjBLxVIjYO4MXyhs709FSWgvVV-P3G3y8_0D44dD51St5QZo6B_RszzwjwILbuRlyHA5nI0A83E8Fh2-3YAGlOQR8iEiGHJuV5eEC9DQdDcZXPxezCiZKADWvkXdCEofOSYDKJNnuXru5TvCxUEPAZLetf8FuQib1ikHNq4ROlav39INokoojZkMDBs7zyz-6is2b2QZfZjkwjEEMFnzLoaX3Wq7tez19wEHyCtTjypd4je0l_0YMe9-jnUrIHOqVgKQYPPiCSevojVa2L-Q7MpKy6TjLRkiyZpq97ia3okOXg5aGQzIrXFVDakLfmVP6xY_yunS8kblA0eS-riIFDxg10zqTzZkYlxp0LH8Kf4DPoB9PBCdVi0cB_Q605qNvqF_bQKRByHMgAVOPi2M06senE5ZhOGYXahz-R2oh_VCkf3vnL_cgGfwS_FYpiHKEBhGQtoK-_gLD_MBhhg-BDZFwuV-9mNt2DjHr1F_SXlESaWlzIPUiFHXvQNouyRYGqr4yJO9spI-w-3ZhvHupVE9dJf8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=aBPTyaK8CjZ5-zE-WjV5ma4DLoKAK-y8ycAuSFCt9DRRFbRP5roXl4Cw8p9abL0EpBb43Oamo-ucQK0z3WN0yOHlq7y41MaPkw4KBv2Bmz9L0yeKvtm0fW-eJSuZB1NSQuwHGL4CaLXzq4cnjBLxVIjYO4MXyhs709FSWgvVV-P3G3y8_0D44dD51St5QZo6B_RszzwjwILbuRlyHA5nI0A83E8Fh2-3YAGlOQR8iEiGHJuV5eEC9DQdDcZXPxezCiZKADWvkXdCEofOSYDKJNnuXru5TvCxUEPAZLetf8FuQib1ikHNq4ROlav39INokoojZkMDBs7zyz-6is2b2QZfZjkwjEEMFnzLoaX3Wq7tez19wEHyCtTjypd4je0l_0YMe9-jnUrIHOqVgKQYPPiCSevojVa2L-Q7MpKy6TjLRkiyZpq97ia3okOXg5aGQzIrXFVDakLfmVP6xY_yunS8kblA0eS-riIFDxg10zqTzZkYlxp0LH8Kf4DPoB9PBCdVi0cB_Q605qNvqF_bQKRByHMgAVOPi2M06senE5ZhOGYXahz-R2oh_VCkf3vnL_cgGfwS_FYpiHKEBhGQtoK-_gLD_MBhhg-BDZFwuV-9mNt2DjHr1F_SXlESaWlzIPUiFHXvQNouyRYGqr4yJO9spI-w-3ZhvHupVE9dJf8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایوان تونی مهاجم انگلیسی الاهلی عربستان:
من‌ عاشق این هستم که موقع پنالتی زدن دروازه‌بان حریف رو تحقیر کنم برای همینه اکثرا چیپ میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29734" target="_blank">📅 13:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29733">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIs7LnmuyfqduS9_2vjquBTWsYYONCFtnz1TXjqOfv59-T3boV4BDldXbtVmneqJEgL2vXDxPRnYYJRIwmvA-PCVnCPQCijCtY4vK0YsOyNoLI6YcwHPJljLgXZnkZXt6DoklxVMCr-wKhpkIU3ZtX02rWBXSbDPPqxaxw0vJKMZ8yDFtnsGzbz6EfjZN3cNUqBiBoIuobpEPETVEiVPJ-SUZkTB3pp0f6F8OUGcCkT5Sy7LNWaEFPwkbPOqW0qAuI_dcSeIg5Aatk7R7JdCNBvCp64s7DYUmlPGmJcBy7KFnjBBKT5W2rMTRI92IjDCcXl50Vgt9_B-pwWJjkUBzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خوزه مورینیو خطاب به‌خبرنگاران در نشست خبری پیش‌از دیدار فرداشب با الچه: در فاصله 3 روز من باید 6  بار بیام جلوی شما بشینم، خدایی خودتون خسته‌نشدین؟ اصلا سوالی مونده ازم بپرسین؟ واقعا خسته‌کننده‌ست. بلند شیم همگی بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29733" target="_blank">📅 13:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29732">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5pAq9VYwAe6OB78kGERNUvLPSDrTB_NkUt-vPkxYpNTm3cLUvn94DkbOLC0-PgM5hQpmJQXGgWDqlgN6WaE43Xa2fC5Ep2YnSYZo3lLGaeq7rLmXtyk7bbR5mPhPBFwe2XAeJm4FlzkyNKu-Mx4nDoogzYCOYgtrSKQlwB_IzBT76le0k6PvpIPVloGLeirJSZpSEBnf9uTYI3LoVkEZY2ahi4q73vIqPNIgYlerdK6Ps6WuTtA1bWVzwyQaUtkQC2CEgWhsuocYEL-gqqbDKvh84UGH5otdHE1jYP4iUaSgWVWE8KWpYbZDXLtgcIXDmTE5zOT2Vd1Ct_PSncuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیره‌کننده رافینیا و لامین یامال زیر نظر هانسی فلیک دربارسا؛ یادتون باشه قبل اومدن فلیک سران‌بارساداشتن‌رافینیا رو میفروختن‌که فلیک اومد و با رفتن رافینیا مخالفت‌کرد و گفت احیاش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29732" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29731">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=TQczqVwCQBzsN_wBWMBoXCuP8R2rJDdpwECbcpUsh8OY6uZypnT2piAWHOlIGvqxeUqVzVY1PrLY8fX2_wcHBso77sAYhJqNmpccEVH2gbkdYUnZYmbPjYYsZvST5zwnFHLSPLX1OAuOlPC67OJf1JhlLPLoqVIsD_wn2BsJYlf0Ek1vls6LL_JYsEreM85T-UrXHVe4IIPgBZroLzDrMGatPjDvYVwEm1FYXQJeerZBiDQf6oYX7-O6WrBxcfXTn9xIV219TB8SJx2zVC5cK3Q0Ea6fp7XtOrRrXZashxghfSk6zDJT28vYPJyfOm3snz9nrNBl1n55jgmUsud2sFPIde0o9caInyO7ysjLdHYz4vFLCVtPjchAc-uRQBGEmyo735KgwfLllS9TlI03n1zf_pErriPRD0dpTuajNRnDd2i1pVJpiV2lynnnLbshUewl5oXarFqcVgqB2MzmFs_6XmnF-Hg2zVe7EgvYgIv1Po0TNMq2bexQFyzBCBpiw18ij1p9XextXH4q4mPGUgLNS0A-MkZpk-hsvzRF_7HTCcSOlijn8EkUhCbZaIH_HhDdsA2361WH7KUQMVDoNQBGO3SSDJBEFRjm79Daoa_nbbAtCTtb5-PU3x6dXdthENRM-6E89tzpMMvVTPO8iijSqVVfui811qHvAj9qXHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=TQczqVwCQBzsN_wBWMBoXCuP8R2rJDdpwECbcpUsh8OY6uZypnT2piAWHOlIGvqxeUqVzVY1PrLY8fX2_wcHBso77sAYhJqNmpccEVH2gbkdYUnZYmbPjYYsZvST5zwnFHLSPLX1OAuOlPC67OJf1JhlLPLoqVIsD_wn2BsJYlf0Ek1vls6LL_JYsEreM85T-UrXHVe4IIPgBZroLzDrMGatPjDvYVwEm1FYXQJeerZBiDQf6oYX7-O6WrBxcfXTn9xIV219TB8SJx2zVC5cK3Q0Ea6fp7XtOrRrXZashxghfSk6zDJT28vYPJyfOm3snz9nrNBl1n55jgmUsud2sFPIde0o9caInyO7ysjLdHYz4vFLCVtPjchAc-uRQBGEmyo735KgwfLllS9TlI03n1zf_pErriPRD0dpTuajNRnDd2i1pVJpiV2lynnnLbshUewl5oXarFqcVgqB2MzmFs_6XmnF-Hg2zVe7EgvYgIv1Po0TNMq2bexQFyzBCBpiw18ij1p9XextXH4q4mPGUgLNS0A-MkZpk-hsvzRF_7HTCcSOlijn8EkUhCbZaIH_HhDdsA2361WH7KUQMVDoNQBGO3SSDJBEFRjm79Daoa_nbbAtCTtb5-PU3x6dXdthENRM-6E89tzpMMvVTPO8iijSqVVfui811qHvAj9qXHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ بااعلام‌مدیرعامل‌فجرسپاسی؛ علیرضا بیرانوند دروازه‌‌بان‌تراکتور درنیم‌فصل‌با عقد قراردادی تاپایان‌خدمت‌سربازی به این‌تیم خواهد پیوست. بدین ترتیب بیرو تا نیم‌فصل بدون تیم خواهندماند و راهی لیگ آزادگان نخواهدشد. بااین‌شرایط باید ببینیم بیرو درجام ملت…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29731" target="_blank">📅 12:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29730">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va_7l5ZGCeWzjbqSOzGvoL8Qg4Ix0UjJxS6abgF2Qu0LPhRWDZGxgx4hVSDNTCE2oIucEuRk7IIrWvDn39qGVOEbgOfrbwU3LyEDArnRHKWC_lAotC73W-CcwfBp3N09vUqqh5IEKaHng6D_AXYlKJM3dHV887BzwHI8IysVs3X9LglIosJjTj_FWQLZ8v_UQxM7Wic3AJL13tX7aHrIga63xv9dVPz48bIJxsjIlMZr7a-sK8Vl_M36oHyQPAiGG9O2Kr0DvA-9dQrZJQkXZdQuEMgv7rRFzzFri-IlFyTUl6IPY9G_HCDwJSNxEmBRU0mcVwOp5ht5NZ0z3TgKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده یاسر آسانی ستاره آلبانیایی استقلال در لیگ‌قهرمانان آسیا: 10 مسابقه، 9 گل زده، 1 پاس گل، کسب میانگین نمره 9.1 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29730" target="_blank">📅 12:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29729">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=MhoKHX32J1Ap5M5SnIVWSlkCMr6mcF2fqqjnk27L6ebxu0IdtxBuGo_dsyVoaSMZjfS97HWlnVj7UWYsRV8olBJlCoVvs0GplAJ2DeIHmkUrLY9Ix37K9N-_L_5KZRNkp20cPe_cC3-7e_VG5SK_NXyX1Awhc11SKz5yl6RgE0L7Hy5j96BYGfTetnD0E9kvkP7T52SO2huQ35yfkTg5o1pOJwA5zET9KiTVKyiazIyXi0-hssbK7jGuVvbqRGMCYVrM-iiN4XM_ZW4vo_cSqhYknfwOVbP-f_zTsB24d9RPpExccv3Su4LSU0dp082dPp7S-ys4g7O6i878xnZIeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=MhoKHX32J1Ap5M5SnIVWSlkCMr6mcF2fqqjnk27L6ebxu0IdtxBuGo_dsyVoaSMZjfS97HWlnVj7UWYsRV8olBJlCoVvs0GplAJ2DeIHmkUrLY9Ix37K9N-_L_5KZRNkp20cPe_cC3-7e_VG5SK_NXyX1Awhc11SKz5yl6RgE0L7Hy5j96BYGfTetnD0E9kvkP7T52SO2huQ35yfkTg5o1pOJwA5zET9KiTVKyiazIyXi0-hssbK7jGuVvbqRGMCYVrM-iiN4XM_ZW4vo_cSqhYknfwOVbP-f_zTsB24d9RPpExccv3Su4LSU0dp082dPp7S-ys4g7O6i878xnZIeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛
تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29729" target="_blank">📅 12:03 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
