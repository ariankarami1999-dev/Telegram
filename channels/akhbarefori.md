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
<img src="https://cdn4.telesco.pe/file/uhDvF0Gd3UEBtEBFl4Yp7Sh3i_muUp38zvdlXLEKhGwsCO4Ia8JfvG34n7f23tFfktpfRgkygpIhV9EDe_JocDXI037w3kc47LmuKryf5dRDQh6pRb7vApZMvyt9YWo7sTaQ3B4Le138NoBtqwFFM04DJ0-y_wx8KK71UMidxZ38dfLtUAVygO2-GAfzrMxg-IJEWKMp4Bv-o03ShPmVM3v-U9REKx8EBRwDZJcHkXLRwoDflmxT852VRvjgKHrAONAnk_15mMLOvMtILUjhDlz8jxqEL_2-er1RINOdbdc8KpLlMrtAjQEgKg0kCvB4lUzADkKyMbtWlCgTZyXukQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 03:13:32</div>
<hr>

<div class="tg-post" id="msg-672371">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
وقوع چند انفجار در بحرین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/672371" target="_blank">📅 03:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672370">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8c5a8ae3b.mp4?token=rO_ZU6xJ0U1gtpq41Tk4Sx_zUKd8YqIq4qEBzyIBttHCoBxiwZdDUkgNbnrpGL9-DTUANri3zhrt-ASGqoWq_xESagUj0vVizNZ0rwB2X2X0ke-7yPNoS-C4XZuZSj7yiJUFdQtEP5j046SKwp16Wqc17vpY4cnuzPruhod1tcegXIYR7_WM4RsaDt8oLFYu1MgaWgGFmSqW-ZnDJDwYoiVd5oyA5NlW6SzE0mCXh_dxsJ8FLc91pobhU2RYTaTdju-W8g2XyaoSwlYIbI0dUnT5N_XY-5LSZ6y9QPKiwyQYXaT_amxe_SnsAo6TkCVvl4MOLzOAvvK368WLPaxywn-8mkdftc1K7-DxdbM29MaYE_fRvt8REzE4U8DdipgFMlgxY1hl9WEJ0fusPdNujkLEX7zEg2NpAV2lqlNRYaXIoNYbGx3nHKjd4xhNPIXDNiYRH3cYOteDmWD8CrOUIXWrCHOrUGVsIfYu9V1HCTCAQxqV6FG96OShJyEfBtvVPJBHj7jGEudxuD66-SE2U0xDkMpJ5J_4Ak0S91WiWm5bGq1umdTmLHNHA9pU2S7FpTaOtljsFm2KD3CysGLstHM229SL1q04LAuwZdT75fZ6X31fcJvxmZyATbSjJOaLc98K9IpD_WMIWGzoPoBaifDIfHOVqRTmXymKDSf7ieY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8c5a8ae3b.mp4?token=rO_ZU6xJ0U1gtpq41Tk4Sx_zUKd8YqIq4qEBzyIBttHCoBxiwZdDUkgNbnrpGL9-DTUANri3zhrt-ASGqoWq_xESagUj0vVizNZ0rwB2X2X0ke-7yPNoS-C4XZuZSj7yiJUFdQtEP5j046SKwp16Wqc17vpY4cnuzPruhod1tcegXIYR7_WM4RsaDt8oLFYu1MgaWgGFmSqW-ZnDJDwYoiVd5oyA5NlW6SzE0mCXh_dxsJ8FLc91pobhU2RYTaTdju-W8g2XyaoSwlYIbI0dUnT5N_XY-5LSZ6y9QPKiwyQYXaT_amxe_SnsAo6TkCVvl4MOLzOAvvK368WLPaxywn-8mkdftc1K7-DxdbM29MaYE_fRvt8REzE4U8DdipgFMlgxY1hl9WEJ0fusPdNujkLEX7zEg2NpAV2lqlNRYaXIoNYbGx3nHKjd4xhNPIXDNiYRH3cYOteDmWD8CrOUIXWrCHOrUGVsIfYu9V1HCTCAQxqV6FG96OShJyEfBtvVPJBHj7jGEudxuD66-SE2U0xDkMpJ5J_4Ak0S91WiWm5bGq1umdTmLHNHA9pU2S7FpTaOtljsFm2KD3CysGLstHM229SL1q04LAuwZdT75fZ6X31fcJvxmZyATbSjJOaLc98K9IpD_WMIWGzoPoBaifDIfHOVqRTmXymKDSf7ieY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایرانی بر فراز پایگاه موفق السلطی اردن محل استقرار ارتش تروریست آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/672370" target="_blank">📅 03:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672369">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049b5524e5.mp4?token=jj41LPdDCAr8ZdjxxHux1F18DiDZKjz4bXvbnc9B4nohiPGnlpv61jzJZQTaiyE5B4rhBqhrZifmtkAJREk4bEcCecijy7Ni6GlJKIMDqDlz8dM-0UbpjDTcsZjK_LVtuN5lK9QHQrhVHBzotYxf6P1WMGb73YQlET0X-0qmKUF_dcBiyJmLOM4XEHeFGxwIh3qECCbJ0XmWOmZ8UIAn_drIu6h0aEFIkBOiF69xjqYe5_wBeTv08kFi1drXes2seD1F4j_uaMCpRyVl3cLlnIlIrSghAEgpFulmtPt7h9hRZy449Q2PRrrHT2NW-h9z91W-7GWAcBh29qF0qsQgdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049b5524e5.mp4?token=jj41LPdDCAr8ZdjxxHux1F18DiDZKjz4bXvbnc9B4nohiPGnlpv61jzJZQTaiyE5B4rhBqhrZifmtkAJREk4bEcCecijy7Ni6GlJKIMDqDlz8dM-0UbpjDTcsZjK_LVtuN5lK9QHQrhVHBzotYxf6P1WMGb73YQlET0X-0qmKUF_dcBiyJmLOM4XEHeFGxwIh3qECCbJ0XmWOmZ8UIAn_drIu6h0aEFIkBOiF69xjqYe5_wBeTv08kFi1drXes2seD1F4j_uaMCpRyVl3cLlnIlIrSghAEgpFulmtPt7h9hRZy449Q2PRrrHT2NW-h9z91W-7GWAcBh29qF0qsQgdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان الزرقاء، اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/akhbarefori/672369" target="_blank">📅 03:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672368">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
انفجار در کویت
🔹
منابع عربی از چند انفجار شدید در پی اصابت پرتابه‌هایی از سمت ایران خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/672368" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672367">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fed2838.mp4?token=Akrs0FTVt7MmRELHbvxLoY1f0N4JAqeuDq5xW8w4jO2cAYuPLCbkLJUCA3rHbJZ8etWAssZRCfVb3Cd1rCfuL1_80Wg5ata0dBNem_8A3KM_E8dw8bTs3kOXfTRdx_qdVhygA2vflF3Ryi4JfWIvjoYbx_ulz6jStj17BD6dPLMzDWwO6YyStMFfiKPjiMYDe2KeHgADO_d9_uyNOCfOlm42llfpkeWcvRKCuEAfJsFhuFjfA2IDi6jcnx1hCuSlY_LwJuBB3k7W6SRNMJLqhJgBQwjCFUPDraPHE72To1uYJt2I4cJVljY2OdBYp2hfRQ-g6HQwK5Q01ouxdjUyQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fed2838.mp4?token=Akrs0FTVt7MmRELHbvxLoY1f0N4JAqeuDq5xW8w4jO2cAYuPLCbkLJUCA3rHbJZ8etWAssZRCfVb3Cd1rCfuL1_80Wg5ata0dBNem_8A3KM_E8dw8bTs3kOXfTRdx_qdVhygA2vflF3Ryi4JfWIvjoYbx_ulz6jStj17BD6dPLMzDWwO6YyStMFfiKPjiMYDe2KeHgADO_d9_uyNOCfOlm42llfpkeWcvRKCuEAfJsFhuFjfA2IDi6jcnx1hCuSlY_LwJuBB3k7W6SRNMJLqhJgBQwjCFUPDraPHE72To1uYJt2I4cJVljY2OdBYp2hfRQ-g6HQwK5Q01ouxdjUyQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجارها در پایگاه‌های آمریکایی اردن به حدی بود که در مناطق اشغالی شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/672367" target="_blank">📅 02:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672366">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxFE3iMV16qo3smsgSpliPICwnf3DHgzFaxhpL6aA4lHtvU87XzgkTaV8mbsQbSRQSmCTKO4ZBNVydOSDW87SAf691Zzc96Uz1G45XQ0QWt1_HGd5ikeAKcKjipC6SfZROC7ZaH8hJZE72n5halfOWKlXBVfKev8v5wbkq4P4Xw-zfkYDJeA36NPhG4l4DRy2je2fSHqKCRTP-FAlrDNdNM9_2fH-gMXKEMrWHuzHZNcO5T5iQh8tRevv8CqxmQT1nR9nVWxfOvY4Kgd9kQ5fsrw1sdkoz1_T9fxJisivsmGpMxRqxQ4PqJpyaFy8iU26VxCLCT6K-85h-ZhScxD2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از مقام آمریکایی: ایران یک موشک بالستیک به سوی یک پایگاه آمریکایی در عربستان سعودی شلیک کرد
🔹
این نخستین حمله ایران به عربستان است پس از ۴ ماه.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/akhbarefori/672366" target="_blank">📅 02:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672365">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بر اساس گزارش‌ها، آژیرهای هشدار در شهرهای الخرج و ینبع پس از رصد شلیک موشک از ایران به صدا درآمده‌اند/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/akhbarefori/672365" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672364">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در اردن به گوش می‌رسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/akhbarefori/672364" target="_blank">📅 02:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672363">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
فرماندار بوشهر: لحظاتی قبل یک نقطه اطراف شهر چغادک از توابع این شهرستان مورد اصابت تهاجم دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/akhbarefori/672363" target="_blank">📅 02:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672362">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
انفجار در کویت
🔹
منابع عربی از چند انفجار شدید در پی اصابت پرتابه‌هایی از سمت ایران خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/672362" target="_blank">📅 02:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672361">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
معاون استاندار هرمزگان: در پی حملات دشمن به برخی نقاط استان هرمزگان سه نفر شهید و ۸ نفر مصدوم شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/672361" target="_blank">📅 02:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672360">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
صداهای شنیده شده در لرستان مربوط به شلیک موشک های رزمندگان اسلام است
🔹
مردم عزیزمان نگران نباشند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/672360" target="_blank">📅 02:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672359">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌‌
♦️
منابع عربی: پایگاه‌های نظامی آمریکا در عربستان سعودی، هدف حملۀ موشکی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/672359" target="_blank">📅 02:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672358">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
فارس: دقایقی پیش اهالی امیدیه خوزستان از شنیده‌شدن صدای انفجار خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/672358" target="_blank">📅 02:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672357">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
رسانه‌های عربی از وقوع چندین انفجار در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/672357" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672356">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
رسانه‌های عربی از وقوع چندین انفجار در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/672356" target="_blank">📅 02:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672355">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ایروانی: آمریکا مسئول کامل تلفات و خسارات حملات علیه ایران است
🔹
سفیر و نماینده دائم ایران در سازمان ملل متحد در نامه‌ای به دبیرکل سازمان ملل و شورای امنیت، آمریکا را مسئول کامل تلفات جانی و خسارات ناشی از حملات اخیر علیه ایران دانست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/672355" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672354">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در اردن به گوش می‌رسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/672354" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672353">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPuovJgSDNyP5FFRZA9jx1lNplBv69UR8ODmDBRLlr9KzS9n3eFG0J2WEa1fQNq4sziGgMttsbi1RCz8RFYBuzcpzi6-cbEB4tOIDQ4QUM1y_uzQWICXtZLsicn5rLWfWHmfRdi_rWlb0AoocJfm00CFPhpJ1bUsWlf1CwmCxuLeoITqtM-dtEkT0C3XmyHwq1ZtmzSsAetN6uRozwtX7HvBn8OmbZd4YBR0nkHA0U_Ord3d4sk014RDiNplQIyIKeFZWAxLP1e-cxL2iaOJuD_XRyQ4pk_aWmOg7Geyqne-b2eKO2Hy-pGslVUcubkpn86SOQdZNBiBtfXUWB3diQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروی دریایی سپاه: در ساعات گذشته ۴ کشتی متخلف متوقف شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/672353" target="_blank">📅 02:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672352">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
حمله پهپادی مجدد به اربیل و انفجارها در پایگاه‌های اشغالگران و تروریست‌های تجزیه طلب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/672352" target="_blank">📅 02:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672351">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تایید مسئولیت آمریکا در کشتار مدرسه میناب
🔹
تحقیقات مشترک «اسکای‌نیوز» و آژانس «معماری قانونی» با استناد به تحلیل‌های فنی، بررسی‌های منبع‌باز و شهادت بازماندگان، مسئولیت مستقیم ارتش آمریکا در حمله به یک مدرسه در شهر میناب را تایید کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/672351" target="_blank">📅 02:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672350">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سی‌بی‌اس نیوز به نقل از مقامات آمریکایی: در جریان حملات هفته جاری به دو پایگاه در اردن، شماری از نظامیان آمریکایی مجروح شده‌اند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/672350" target="_blank">📅 02:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672349">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
انسداد محورهای مواصلاتی هرمزگان در پی حملات دشمن
🔹
در پی حملات به زیرساخت‌های جاده‌ای هرمزگان، تونل «شهید میرزایی» (محور بندرعباس-حاجی‌آباد) به طور کامل مسدود شد.
🔹
همچنین پل «شور» و پل محور سه‌راهی میناب به رودان نیز مورد حمله قرار گرفتند. از شهروندان خواسته شده است تا اطلاع ثانوی از ترددهای غیرضروری در این مسیرها خودداری کنند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672349" target="_blank">📅 01:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672348">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
افزایش سطح آماده‌باش سنتکام در پایگاه‌های منطقه
🔹
فرماندهی مرکزی آمریکا (سنتکام) با استناد به ارزیابی‌های اطلاعاتی درباره احتمال حملات تلافی‌جویانه، سطح آماده‌باش نظامی در تمامی پایگاه‌های ایالات متحده در منطقه را افزایش داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/672348" target="_blank">📅 01:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672347">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
حملات دشمن آمریکایی به اهواز، لار، یزد و چند شهر ایران
🔹
ارتش تروریستی آمریکا در ادامه حملات نامشروع امشب به خاک وطن، برای چند بار متعدد مناطقی در شهرهای اهواز، بندرعباس، قشم، لار، داراب و یزد را هدف موشک‌های خود قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/672347" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672346">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در قشم؛ مشاهده نور انفجار در بندرعباس
🇮🇷
✊
@AkhbareFori.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/672346" target="_blank">📅 01:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672345">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
۵ انفجار در حومه یزد؛ آسمان امن گزارش شد
معاون سیاسی و امنیتی استانداری یزد ضمن تأیید شلیک ۵ پرتابه دشمن در خارج از محدوده این شهر:
🔹
این حادثه خسارت جانی در پی نداشته و در حال حاضر با برقراری آرامش، امنیت کامل بر آسمان یزد حاکم است./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/672345" target="_blank">📅 01:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672344">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
پدافند هوایی آمریکا ۸ مجروح برجای گذاشت  رسانه‌های عراقی:
🔹
در ‌پی اصابت گلوله‌های پدافند هوایی آمریکا به یک زمین بازی در استان سلیمانیه، ۸ نفر مجروح شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/672344" target="_blank">📅 01:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672343">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در قشم؛ مشاهده نور انفجار در بندرعباس
🇮🇷
✊
@AkhbareFori
.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/672343" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672342">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۶/دو فروند کشتی نفتکش با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند
سپاه پاسداران:
🔹
ملت قهرمان و بصیر ایران اسلامی؛
حضور شما در صحنه و حماسه آفرینی خیابانی شما، همانگونه که قائد شهید امت فرمودند سوخت موشک‌های رزمندگان اسلام و دعای شما تضمین پیروزی‌های درخشان آنهاست.
🔹
ساعتی پیش دو فروند کشتی نفتکش که با فریب سازمان‌های جاسوسی آمریکا قصد عبور از مسیر مین گذاری شده جنوب تنگه هرمز را داشتند، منفجر شده دچار حریق گسترده شدند.
🔹
نیروی دریایی سپاه با قاطعیت اعلام می‌دارد تنگه هرمز به خاطر شرارت‌های ارتش کودککش آمریکا به شدت ناامن و به طور کامل بسته است و تا زمانی که تجاوزات آمریکای جنایتکار پایان نیابد، امکان صدور کود شیمیایی و حتی یک قطره نفت و گاز از این منطقه وجود ندارد.
🔹
شناورها برای حفظ سرمایه و مهمتر از آن جان خود فریب نخورند و وارد مسیر مین‌گذاری شده نشوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/672342" target="_blank">📅 01:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672341">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
صدای انفجار و پرواز هواگرد در بندرعباس
🔹
صدای چندین انفجار و پرواز هواگرد در بندرعباس و اطراف آن گزارش شده است.
🔹
خبرنگار مهر شنیده شدن ۲ انفجار را تایید می کند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/672341" target="_blank">📅 01:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672340">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4cca69fa3.mp4?token=OOqHvmNe2o8myaQJO1DWBRkFvacbnv6M2krZEAlhduI7f__h0tz0WINBqNSkqXyBXVxOsLX4LIlxEZEM4dBiWJbVobbG-evBoi-Dt-FHBIkA2s8R35ShMqliu_nFVgp4n3y7VxUXctVQyVt78GlqZe-UoJGc-QyZwaxVlYV-lV2WEB-TBg1CumyOtAQiDjT1PbPajSxXqUhcmsnxnzTdelvmOutJQWjyFHknN0d56rhVABpGsqbXE3IaXfwgHlsq3pC-CYT2ehhUTwKETWKSnr212MI7JsEos_S3yOW1vwCvR_Zn3ezx4ACvTSnsbzlXh--tpAB_sCZIxIUwCY2NYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4cca69fa3.mp4?token=OOqHvmNe2o8myaQJO1DWBRkFvacbnv6M2krZEAlhduI7f__h0tz0WINBqNSkqXyBXVxOsLX4LIlxEZEM4dBiWJbVobbG-evBoi-Dt-FHBIkA2s8R35ShMqliu_nFVgp4n3y7VxUXctVQyVt78GlqZe-UoJGc-QyZwaxVlYV-lV2WEB-TBg1CumyOtAQiDjT1PbPajSxXqUhcmsnxnzTdelvmOutJQWjyFHknN0d56rhVABpGsqbXE3IaXfwgHlsq3pC-CYT2ehhUTwKETWKSnr212MI7JsEos_S3yOW1vwCvR_Zn3ezx4ACvTSnsbzlXh--tpAB_sCZIxIUwCY2NYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینفانتینو: فدراسیون بین‌المللی فوتبال (فیفا) منبع اصلی شادی برای بشریت است/ ترامپ: مگر اینکه تیم شما شکست بخورد!
رئیس فدراسیون جهانی فوتبال:
🔹
شما نیازی به افرادی ندارید که شما را تحسین کنند، اما این جام جهانی بدون شما، به این میزان موفقیت چشمگیر را به دست نمی‌آورد.
🔹
جام جهانی ۲۰۲۶ بزرگترین رویداد اجتماعی و فرهنگی انسانی است که بشر تا به حال شاهد آن بوده است. از شما سپاسگزارم، آقای ترامپ.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/672340" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672339">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
♦️
منابع عراقی: دو انفجار مجدد پایگاه آمریکایی در اربیل، شمال عراق را لرزاند
🔹
پدافند هوایی آمریکا در تلاش است تا با پهپادها در آسمان اربیل مقابله کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672339" target="_blank">📅 01:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672338">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
صدای انفجار در حاشیه جنوبی لار
🔹
منابع محلی اعلام کردند که لحظاتی پیش صدای یک برخورد در حاشیه جنوبی این شهر شنیده شده است./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/672338" target="_blank">📅 01:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672337">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد MQ9 در آسمان بوشهر
🔹
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانۀ نوین پدافند پیشرفتۀ نیروی دریایی سپاه در آسمان بوشهر رهگیری و منهدم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/672337" target="_blank">📅 01:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672336">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
♦️
منابع عراقی: دو انفجار مجدد پایگاه آمریکایی در اربیل، شمال عراق را لرزاند
🔹
پدافند هوایی آمریکا در تلاش است تا با پهپادها در آسمان اربیل مقابله کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/672336" target="_blank">📅 01:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672335">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
معاون استاندار اصفهان: هرگونه فعالیت پدافندی در شهرستان نجف‌آباد تکذیب می شود
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/672335" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672334">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
وقوع هرگونه برخورد یا انفجار در لار استان فارس تکذیب شد/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672334" target="_blank">📅 00:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672333">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حملۀ موشکی به نقاطی از اطراف شهر اهواز توسط دشمن آمریکایی
معاون استانداری خوزستان:
🔹
دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
🔹
اخبار تکمیلی متعاقبا اعلام می‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/672333" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672332">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e35cd90c5.mp4?token=cb18mW1vY-EX_ZeBZLZ3JyTRRwIzJ2gIGBFct2O5k7ac8jkEHkT3vaDusObSe7GwhRWN9JdvLMb13oAy0yXWaGi8uFjhzbgsx2-6w2uzjFjnwA0AFbuiXILo9fxcv6YhuMlSAGXd0BTxUEPHK-3FN5oa9ZIdBzT4HYkb3Ukgc5W90mArKdgDgtw-rNxAnITHsfNHsmnbIoiu6YBV-palnInB8TCNppe-gy-5Xnx_e8MWmBXBqm3cobwkeZ1rHWnc3bVx-8DfLS0aFspXy2c_y7rmTpXtWDfnc8UG4li1NLLBXF-1yx15pjkQtbHUu0SUuV3bInYMaCdpWE-sfp_M7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e35cd90c5.mp4?token=cb18mW1vY-EX_ZeBZLZ3JyTRRwIzJ2gIGBFct2O5k7ac8jkEHkT3vaDusObSe7GwhRWN9JdvLMb13oAy0yXWaGi8uFjhzbgsx2-6w2uzjFjnwA0AFbuiXILo9fxcv6YhuMlSAGXd0BTxUEPHK-3FN5oa9ZIdBzT4HYkb3Ukgc5W90mArKdgDgtw-rNxAnITHsfNHsmnbIoiu6YBV-palnInB8TCNppe-gy-5Xnx_e8MWmBXBqm3cobwkeZ1rHWnc3bVx-8DfLS0aFspXy2c_y7rmTpXtWDfnc8UG4li1NLLBXF-1yx15pjkQtbHUu0SUuV3bInYMaCdpWE-sfp_M7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع محلی در سلیمانیه عراق می‌گویند شدت انفجارهای امشب به حدی است که برخی گمان کرده‌اند زلزله رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/672332" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672331">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
هم‌اکنون شنیده شدن صدای ۵ انفجار در یزد/ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/672331" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672330">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
وقوع هرگونه برخورد یا انفجار در لار استان فارس
تکذیب شد
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/672330" target="_blank">📅 00:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
استانداری هرمزگان: تا این لحظه اصابتی به بندرعباس گزارش نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/672329" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672328">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqzv-Msvh4eoiuDd2zPR5cI--CPtUlPQlomtWOqb_QLQDGUUnH3o7VPFAxC2H1cA92EH-M-JgFOX7157xolUafTZsXPixzRRhO4wNQgvRhTupYfOknjuUFYlbtqNm-56eodgtc0phaXI5xONmFvvOD_sRRoDP4AJqR2v5h68M_fjhdtlQo52XV4GOhRE97BYGdG1WnU5-adN4lzbyQZdvUMH1pOdVEXJ_7vA4HoWPBtvoBAPR96sieoMgtfSCxF9xKiO9fbHM2kesJ3djPuv4zu29TKf3T2iaNukGFqUP_c1OgyYOCgRO_kS4S-J7NGWfOhqAzg3qcZVh_YyirP7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ملت ایران امروز بیش از هر زمانی متحد و مصمم است که قاطعانه دشمنان وحشی را از تجاوز نظامی جنایتکارانه علیه میهن عزیزمان، پشیمان کند
🔹
آمریکا می‌خواهد با حمله به زیرساخت‌های غیرنظامی و کشتار بی‌گناهان، به اصطلاح «قدرت» خود را به رخ بکشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/672328" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672327">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
فرماندار بوشهر: تاکنون هیچ گزارشی از اصابت در بوشهر دریافت نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/672327" target="_blank">📅 00:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672326">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
داستان جنایت آمریکا؛ از ۶۶ کودک شهید پرواز مسافربری تا ۱۶۸ کودک شهید میناب
گزارش متفاوت اژدهایی، خبرنگار صداوسیما در بیمارستان بندرعباس:
🔹
من روزی با موی سیاه بر لب ساحل ایستادم و پیکر ۶۶ کودک شهید پرواز ۶۵۵ مسافربری را دیدم، حالا با موهای سفید دوباره روایتگر جنایت آمریکا هستم.
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/672326" target="_blank">📅 00:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672325">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff2416c74.mp4?token=vUR7t7fJDCUV7GY5USQrT-vlyFmgQdx9hhD8fPGi3GYiQjuYfAJbHH5WzdjUeOt09-6VB1UxVytgoPm_z-_5tNA0Ne1x6DJCx72B4SR6f07g48AqX0SXd5pi25ahh4qOaZF2ATLhSzCPqwB5mZ42--DaE7QXsdSUbzlpLHq6TwTvodlYCGbWi9pFVkQ3aRDwevWV0stvfLi9IVPvuVofWNWVfr0ckcUsyMOWcseb5YlKkvbxBXmqswqV-aaeDhp1c6g5E6rZNe0bEJH04CimY9Xl3UFrQQHu45RleIaf817AUMjhJlrruIEY7GFFW9kVEHqGMjshQb6ux8_HTPglJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff2416c74.mp4?token=vUR7t7fJDCUV7GY5USQrT-vlyFmgQdx9hhD8fPGi3GYiQjuYfAJbHH5WzdjUeOt09-6VB1UxVytgoPm_z-_5tNA0Ne1x6DJCx72B4SR6f07g48AqX0SXd5pi25ahh4qOaZF2ATLhSzCPqwB5mZ42--DaE7QXsdSUbzlpLHq6TwTvodlYCGbWi9pFVkQ3aRDwevWV0stvfLi9IVPvuVofWNWVfr0ckcUsyMOWcseb5YlKkvbxBXmqswqV-aaeDhp1c6g5E6rZNe0bEJH04CimY9Xl3UFrQQHu45RleIaf817AUMjhJlrruIEY7GFFW9kVEHqGMjshQb6ux8_HTPglJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع محلی در سلیمانیه عراق می‌گویند شدت انفجارهای امشب به حدی است که برخی گمان کرده‌اند زلزله رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/672325" target="_blank">📅 00:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672324">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
گزارش شنیده شدن صدای ۴ انفجار در سیریک
🔹
خبر اولیه از شهرستان سیریک در استان هرمزگان حاکی از شنیده شدن صدای چهار انفجار متوالی است.
🔹
جزئیات بیشتر در خصوص علت و منبع این صداها هنوز در دست بررسی است و اخبار تکمیلی متعاقبا اعلام خواهد شد/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/672324" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672323">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJVWI9C3TMaqJU4MaFk9qCldUc3imu_ee-dPEgzrhncaKKVAdvRH20QKKt6yMjgIAFDlY_nxjVETFLnkpXj41edFaaPDvv9ktjLegbS1_5jyhiuR676cF8rldBxyU5J02zis9nH86ZCgyCb98JRWBB6b4jE6GipbrbtW1R6vocQDvotwu3TWuk-kr18lM_NaKkr0kvrWGq2yNv5HSK9n7QvYFpnfToqzipzmmtJOh4A5r4mU1GtObDsWspV0Ois9jMotJJwEBuGXyd5Cz_y8-QhNT3oG3EPN2ErH2V1XA4MB_aP_tcwlBMQlpgdi4P6OXg_Rdi4eMVj_YxWyB9Z7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/672323" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672322">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
لغو تمامی پروازها در فرودگاه اربیل
🔹
در پی حملات پهپادی به مقر ارتش تروریستی آمریکا در پایگاه حریر واقع در مجاورت فرودگاه اربیل،  تمامی پروازهای این فرودگاه لغو شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/672322" target="_blank">📅 00:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672321">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۵/
دپوی شهپاد های آمریکایی (شناورهای بدون سرنشین) در بحرین در هم کوبیده شد
🔹
مرکز اصلی هوش مصنوعی بحرین که در هدف‌یابی دشمن مورد استفاده شیطان بزرگ قرار می‌گرفت با چندین موشک بالستیک و بیش از ده‌ها فروند پهپاد به طور کامل تخریب شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/672321" target="_blank">📅 00:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672319">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سخنگوی دولت: دولت چهاردهم تا پای جان کنار مردم ایستاده است
فاطمه مهاجرانی:
🔹
در نشست روز چهارشنبه هیات دولت مقرر شد با توجه به حملات دشمن، به‌ویژه در استان خوزستان، برنامه‌ریزی لازم برای حضور در این استان انجام شود.
🔹
مردم جنوب، جان ایران هستند. همه مردم ایران قدردان رنج‌ها، ایستادگی، صبوری و فداکاری‌های شما هستند و به لطف خدا، با همدلی و همراهی، از این شرایط و گردنه دشوار نیز عبور خواهیم کرد.
🔹
این دولت تا پای جان پای کار مردم ایستاده است و اجازه نخواهد داد خللی در ارائه خدمات به مردم ایجاد شود./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/672319" target="_blank">📅 00:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672318">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
وزارت دفاع کویت: چند مرکز و پادگان متعلق به ارتش کویت هدف حملات پهپادی قرار گرفته‌ است
🔹
در این حملات تعدادی از نظامیان مجروح شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/672318" target="_blank">📅 00:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672317">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvG6H2KmICNpbskwf7CPvRh4fmK5ijii5AJOBJmiH_LSB4P5PGZFzef9Z3rJLbIVKfBtWXgJPeUEQtn3Ky7kepTQMEvjje_AUEpfmJWkexxZsQRg_ZfXym6uV-E5VqXLH7WCbiaj68fxisHlMkY4FFsiROzS88MBxAGnpswnoZ1SAyenRjQZBYofOpmKEUgh9QzJBgJS01vO2iZppUutNRzuWk-7Yjj-d9jVT0DOW7twJIs73Me1wXnaBgIv9BYmJFXBC2kftwq2SbQRdGBJS7kxjAeU_szB539FxG-yo5EFpJ-X8FpktI-HFGngRIcQB7XAKb9NXE6sSKyL1DHbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/672317" target="_blank">📅 00:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672316">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
استانداری هرمزگان: فردا شنبه ادارات و بانک‌های استان با حضور ۵۰ درصدی کارکنان فعالیت خواهند کرد
🇮🇷
✊
@AkhbareFor</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/672316" target="_blank">📅 23:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672315">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
صدای ۳ انفجار در بخش بمانی سیریک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/672315" target="_blank">📅 23:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672314">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
انفجار در اهواز تا این لحظه مورد تایید نیست و هیچ گزارشی در این خصوص وجود ندارد./مهر
اخبار لحظه‌ای حملات امشب
👇
khabarfoori.com/fa/tiny/news-3231107</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/672314" target="_blank">📅 23:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672313">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuRqPjHhZBQWdJ0BHcFzjb18QJMWBo_0FRw_TI8dC1SaGRPmcV6VK_ptq682PI7nm5kqXJxYbiOepPktMIEz98l7lglLhmqRuxABc1zjkubpZ8zXrNhmaN6n8OIKhUS5uJZsUvuk00V144DZiRICA4C5Dg75XmKVUvTBx-9rBaRuKFsoqX_daiAjAf-zHsS-E27GbfcblEglbtxXKPwt0wWA2pBzhxuHMkNO39BLKMbdo7VXtNDmQqL12OCiO6KFtQax4lj9k2_YRzQY83Hoeo_XukZKXzwOFQ4HfgkHSNgZv3FvH8g1otgOSeFKT0oMl1_ynnexrUd38MDm1A7qoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت و آتش در پایگاه الحریر امریکا، شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/672313" target="_blank">📅 23:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
رژیم صهیونیستی با نقض مجدد آتش‌بس، روستای حداثا در جنوب لبنان را مورد تجاوز قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/672312" target="_blank">📅 23:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672311">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
وزیر دفاع یمن: آماده‌ایم از دستورات آیت الله سیدمجتبی خامنه‌ای پیروی کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/672311" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672310">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
صدای ۳ انفجار در بخش بمانی سیریک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/672310" target="_blank">📅 23:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672309">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
دولت عراق رسما مجوز فعالیت شرکت استارلینک در عراق را امضا کرد/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/672309" target="_blank">📅 23:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672307">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
سه پلن احتمالی ترامپ برای ادامه جنگ با ایران/ از حمله زمینی به خارک تا جنگ پل ها
👇
khabarfoori.com/fa/tiny/news-3231099
🔹
پاداش کشتن ترامپ اعلام شد
👇
khabarfoori.com/fa/tiny/news-3230933
🔹
حملات گسترده ایران به پایگاه‌های منطقه‌ای آمریکا در منطقه
👇
khabarfoori.com/fa/tiny/news-3230968
🔹
هشدار پاکستان به ایران درباره خط قرمزش در خاورمیانه
👇
khabarfoori.com/fa/tiny/news-3231059
🔹
خواننده مشهور بازداشت شد
👇
khabarfoori.com/fa/tiny/news-3230930
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/672307" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672306">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAeSmdtkDIwPniPQjYO28_sLL3sYl_BC_D_fRMcMM9lCevf_YeAOJtX4WLqE_w00yETU7A_DwXcokQNBQCggxYWZkVg67bUZkTHALmTTvisFUvGZ3g0esxYEf8akcOrZS3ny5OdHsWTbdMfGTI5jE_y3ZiBYsVVsSmwoaYppBf5dKh9hVzQLv940HYXmXl-k154uzH7oPCnXF1bpoUBA-qZok2ODaddbzbX-OQSIxrBZMhEqcqF6gIa18He73tdWHpQzVPizukmuhyX4I1UibSmyVd7QdB7ZnxY6tc1oFtueQ3rZeHmyf6w8qSqApIQ7a1F8bia_sVf8y_XAyJjypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندهی مرکزی آمریکا: فرماندهی مرکزی آمریکا برای هفتمین شب متوالی در ساعت ۳ بعدازظهر امروز به شرق ایران دور حملات خود را علیه ایران آغاز کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/672306" target="_blank">📅 23:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672304">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در قشم و سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/672304" target="_blank">📅 23:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672302">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQtj-XjCPmln_Qs9wEemBFAP1RWL4NnvLYQb6Mfv8v-qgHdyyvrxLNWYSBpwyzWo0oReJEgi6ZCz9yO8I6dCfVwVU9xvlsAbm8NWeq7wf99G9I4y4afIGRSNefYZme0_6_J640uu3mK7i5Q3pvkAIRj29blStagOHnaTtmuXwdFj_N8vCynYaQY6tdPMT9MEZRBpPIFmQnRMrpkDGFWCcASc0Pi5EyjqavlZgHH-5xqICzhHqv1EzM52_q83e414i_DSzz-HNcyyJ3LpTVmwTWyku1YTC1r9OV-EQ--Zk3fOr3AcK2onPS5b8stNc74wJMvODz8nwt21zkZCcPAdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4082b86485.mp4?token=kmYjViSgEqz2EV2pWZApQ_Ye8FcUUOT-aFQYUhAN50HUGIo1t5yYtCE7goIyuFBq32cSbwyH77PXLgRwXrqFkSs0wGqx-hBmWx4dhtg6rA-6DMT_N3Zjh0DKmHyxGwLVigLEy_8eUbKHjTGJflB5UdIxY642RCmTyRadaQK774nSekVBLGaxi8a_LhUiTfBMXeIzDdcVB-5mP6OYfpbMAdgLrrdvM8rz4QK-h6XDdBitAOswu9crZAoiOhGCdN-s-JUIrTFyqwDrHwfQUNYelOZNXdSRLQbid4jftZI4YCGsd6XUaOzNlATE4e0fF4jsBwKeo187Dt-VVVAz5BuoMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4082b86485.mp4?token=kmYjViSgEqz2EV2pWZApQ_Ye8FcUUOT-aFQYUhAN50HUGIo1t5yYtCE7goIyuFBq32cSbwyH77PXLgRwXrqFkSs0wGqx-hBmWx4dhtg6rA-6DMT_N3Zjh0DKmHyxGwLVigLEy_8eUbKHjTGJflB5UdIxY642RCmTyRadaQK774nSekVBLGaxi8a_LhUiTfBMXeIzDdcVB-5mP6OYfpbMAdgLrrdvM8rz4QK-h6XDdBitAOswu9crZAoiOhGCdN-s-JUIrTFyqwDrHwfQUNYelOZNXdSRLQbid4jftZI4YCGsd6XUaOzNlATE4e0fF4jsBwKeo187Dt-VVVAz5BuoMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش از مقر گروهک‌های تجزیه‌طلب در سلیمانیه همچنان زبانه می کشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/672302" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672301">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
تحقیقات رسانه انگلیسی، آمریکا را عامل جنایت مدرسه میناب معرفی کرد
🔹
شبکه انگلیسی اسکای‌نیوز با استناد به نظر هفت کارشناس مستقل و بررسی تصاویر ماهواره‌ای، بقایای مهمات و الگوی تخریب، آمریکا را عامل حمله به مدرسه شجره طیبه میناب و به شهادت رسیدن کودکان این مدرسه معرفی کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/672301" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672300">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی سنتکام: امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی، برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم
🔹
حملات با هدف تضعیف قابلیت‌های نظامی ایران، به دستور ترامپ، طراحی شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/672300" target="_blank">📅 23:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672299">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
پاسخ یمن به حمله به فرودگاه صنعا؛ فرودگاه «ابها» عربستان هدف قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672299" target="_blank">📅 23:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672298">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
تصاویری از لحظه برخورد پهپاد انتحار به پایگاه آمریکایی الحریر در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/672298" target="_blank">📅 23:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672297">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAooAkTjS3ox1ZY3VNH2gALAnCyEuoWSs2CSKOX1rMZ8rmFAlYi-6WomSwII53QDepgWo546RvgH6KNeZD_OLfxVWFKXEBRrtsUYMKto5IwIAgmoGMhgGA_M8cxVjK47RGq2M07Vek0h30iqv9nIRBfBas4pI1tI5c22I1bplOkvqcpLFnfklu7_8P4-nkfJpV2Plp5yocwlsWWJ-Bjn2IgKr3G-2e7zfs8KMbWu7MmtBnnRfMHdmWdqt3B2Xjscf7KtxH1Q_SU40IiOPFJdlTcx_qqeMxmQDZVtoQZQNRN7-TNNTIpOCKrY-WjUaeoUtgAxfg-rEvTZSE1GiC8Vig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
احتمال به تعویق افتادن فینال جام جهانی به دلیل آتش‌سوزی‌های جنگلی در کانادا
🔹
دود غلیظ ناشی از آتش‌سوزی‌های جنگلی در کانادا، ایالات متحده را نیز فرا گرفته است.
🔹
به گزارش خبرگزاری Ole، احتمال به تعویق افتادن فینال جام جهانی در حال حاضر کم است، اما فیفا این…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/672297" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672296">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
هدف‌گیری تاسیسات در کویت
ارتش کویت:
🔹
حمله ایران منجر به هدف قرار دادن تعدادی از تأسیسات و اردوگاه‌های ارتش کویت با پهپادهای دشمن و مجروح شدن تعدادی از نیروهای زمینی کویت در حین انجام وظیفه شد.
🔹
همچنین تعدادی از تاسیسات حیاتی و عمرانی از جمله ایستگاه تقطیر برق و آب مورد هدف قرار گرفت که منجر به آتش‌سوزی و خسارت به تعدادی از تاسیسات ایستگاه‌ها و واحدهای تولید برق و همچنین سقوط ترکش در تعدادی از نقاط کشور شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/672296" target="_blank">📅 23:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672295">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd672daa05.mp4?token=WfvNaC5aG5h4TYAeVGSNKuggTb78MPUrAvOP8e3w4hppyB56jLsz5PCaHjKtXJyT8iS6ey2V_-nO_rXzXE5tWzr5vxEdIzwQQ7xANgcDqOPgAgBEu3K1lgw72m8fLx5py8ddRQuxszb7NJxRe-YJG04sczYQIhgAs8S9-L9R5_WAR0IR7ZYVW9bc7VKpliWG4OB723-f0iw4jg6LG1VTZpOQstG-aMLlGEuGPi3WjVoKE3lb86wLSvxYMV3u1NLYnDqJbg-ENSWLywcR4mAltaqL5tKNAgIftkFg6vriYFHDPkgWBWbromlrHczyuPJ3gR7PtOvZAZGjSCGlwE19FWTMZ5ayVjhvu5-ApIK3ostHx4CCWElNLKCVL0RRpDFdajSWu7bKCrR8H-SYMa963l8GQnFEVRH6sBe5UW7tiEh8VhuB8WbliqJX70MXojwM1PmNhnTVjAU2N0dbOuAoYHs9yfygBh-bPEPIM53eGe0hAYda6uRsFH4tShXMjfOKuL4DGmr2c5a6P4jscqYQ8Ulbo83h5sXyqB7BcMN_Y6JtU2y6Vc9L1XVYUhHV4OasP1xDJ2JWgh2DxLZ5zjpkPofe3S-v1gy6t8CcPNnrbO35mvsQxTpZw5mr9LPuWkdAGUouYCeYwgZKE8MGOTxEnUd9o6OMpV_gmsfzZmd9FrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd672daa05.mp4?token=WfvNaC5aG5h4TYAeVGSNKuggTb78MPUrAvOP8e3w4hppyB56jLsz5PCaHjKtXJyT8iS6ey2V_-nO_rXzXE5tWzr5vxEdIzwQQ7xANgcDqOPgAgBEu3K1lgw72m8fLx5py8ddRQuxszb7NJxRe-YJG04sczYQIhgAs8S9-L9R5_WAR0IR7ZYVW9bc7VKpliWG4OB723-f0iw4jg6LG1VTZpOQstG-aMLlGEuGPi3WjVoKE3lb86wLSvxYMV3u1NLYnDqJbg-ENSWLywcR4mAltaqL5tKNAgIftkFg6vriYFHDPkgWBWbromlrHczyuPJ3gR7PtOvZAZGjSCGlwE19FWTMZ5ayVjhvu5-ApIK3ostHx4CCWElNLKCVL0RRpDFdajSWu7bKCrR8H-SYMa963l8GQnFEVRH6sBe5UW7tiEh8VhuB8WbliqJX70MXojwM1PmNhnTVjAU2N0dbOuAoYHs9yfygBh-bPEPIM53eGe0hAYda6uRsFH4tShXMjfOKuL4DGmr2c5a6P4jscqYQ8Ulbo83h5sXyqB7BcMN_Y6JtU2y6Vc9L1XVYUhHV4OasP1xDJ2JWgh2DxLZ5zjpkPofe3S-v1gy6t8CcPNnrbO35mvsQxTpZw5mr9LPuWkdAGUouYCeYwgZKE8MGOTxEnUd9o6OMpV_gmsfzZmd9FrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد انتقام خواهی مردم بندرعباس در حضور پیکر مطهر دو تن از شهدای حملات جنایتکارانه دیشب آمریکا در هرمزگان
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/672295" target="_blank">📅 23:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672294">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818b30dc1e.mp4?token=YLllOwCNSgEwAWVe8tI9XlTKmqrPuRzi7i1N1JomyJAZAUNIkfGM3BELMVSgmLpbGLJbbavIQr9DU4yaXddxw4tcPLKe9f1qGbuJrhR9xBEj3-xHguywoIeAeCbgZiDAnXTdM0J2woC_e5yTAJvhxOGXkJ0S4z265p0DXXj-OA68ZhQfYGqWRh9MA-qkUtNyF8z3uDdxRfnEfsBvHRHPrVweJnXsbUc-QoBw91trx0ix0DhWjVdbZVlVrlhJ5imkSppSycr3lLI8ap9wC7vsPKTf4J7O_7t2kVdrGgzkyvYld6RmFDs-kqaliLj_PKmUNdgyE3JrikIHgMvR9IpdMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818b30dc1e.mp4?token=YLllOwCNSgEwAWVe8tI9XlTKmqrPuRzi7i1N1JomyJAZAUNIkfGM3BELMVSgmLpbGLJbbavIQr9DU4yaXddxw4tcPLKe9f1qGbuJrhR9xBEj3-xHguywoIeAeCbgZiDAnXTdM0J2woC_e5yTAJvhxOGXkJ0S4z265p0DXXj-OA68ZhQfYGqWRh9MA-qkUtNyF8z3uDdxRfnEfsBvHRHPrVweJnXsbUc-QoBw91trx0ix0DhWjVdbZVlVrlhJ5imkSppSycr3lLI8ap9wC7vsPKTf4J7O_7t2kVdrGgzkyvYld6RmFDs-kqaliLj_PKmUNdgyE3JrikIHgMvR9IpdMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله سیزدهم عملیات صاعقه ارتش؛ شلیک موشک کروز به سمت شناور دشمن متجاوز آمریکایی
روابط عمومی ارتش:
🔹
ساعاتی پیش و در مرحله سیزدهم عملیات صاعقه،  سامانه موشکی  نیروی دریایی ارتش، با موشک کروز ساحل به دریا، شناور متخاصم دشمن متجاوز را در شمال اقیانوس هند، هدف قرار داد.
🔹
شلیک موشک کروز توسط نیروی دریایی ارتش موجب ایجاد رعب و وحشت دشمن و دور شدن شناور متخاصم از تیررس رزمندگان دلیر این نیرو شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/672294" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672293">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
والیبال لیگ ملت‌ها | ایران به اسلوونی باخت
🔹
ایران ۰ - ۳ اسلوونی
🇮🇷
۲۵ | ۱۹ | ۲۴
🇸🇮
۲۷ | ۲۵ | ۲۶
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/672293" target="_blank">📅 23:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672292">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4576e8e153.mp4?token=OrBHShKfvjH6ZqQ9iolysgds-dDvGRT1_6OaAuXaavvtOycST956SrVmb6gr1Bv9bjVzMMG3AHoYnqUwXksOjcj0-TW9dfqa3drfwe3hNbFMmpBYgo8LhPO4BLxfWXcnjRcFLKAMtwrdKUwRftN0fNoLx13O-Esm6GgA3c9ICQPSGz2UvSqMQyWNLhzFjgzy1sQsct80boUGK7Ty2LvLq1ZcQ7u0BYDgCXNh_sPN4lDmr746wOmACtKEnUW7keU_VAd14UrWBJIoxsv4ACNRYGhHmiX6IpDD8OAcoSlrkVdLRldht480Ih1_kqqlnPrjNumBP8sqstFeA45wY-x-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4576e8e153.mp4?token=OrBHShKfvjH6ZqQ9iolysgds-dDvGRT1_6OaAuXaavvtOycST956SrVmb6gr1Bv9bjVzMMG3AHoYnqUwXksOjcj0-TW9dfqa3drfwe3hNbFMmpBYgo8LhPO4BLxfWXcnjRcFLKAMtwrdKUwRftN0fNoLx13O-Esm6GgA3c9ICQPSGz2UvSqMQyWNLhzFjgzy1sQsct80boUGK7Ty2LvLq1ZcQ7u0BYDgCXNh_sPN4lDmr746wOmACtKEnUW7keU_VAd14UrWBJIoxsv4ACNRYGhHmiX6IpDD8OAcoSlrkVdLRldht480Ih1_kqqlnPrjNumBP8sqstFeA45wY-x-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از لحظه برخورد پهپاد انتحار به پایگاه آمریکایی الحریر در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/672292" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672290">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddad2c1542.mp4?token=mvvYlJ7Jbm4IG3pZiGAFVICNhTKw52LSJA6tDyiaZfr2xxHd8eSG-pRZDsUAc7N2DjYA1HGwiDHZhT8PhzRGTvizqjCH8Q1lQenpBUZpwqNeErUngaqFCrXJuqBTIOdjLAsWS-QsHJLqm361VwKq3KWCJ5AIOY3JTUzdGVxe0gBXXst7g6pTz0_mSrTjg6E0znAKwIrUZOJ0NM_rZaQz15p-a-_P6PbCf0UpJEQ7yvry-fsK-pdV6JbvdLMtiNvnWpIdBHJUTd8ALJt7FVnhtOUZyF36UxK7Vn-ZLBDCc5T3gTXD59UiwyW2fAbkyOtuwifjd5QhOdV9IqfuPe396Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddad2c1542.mp4?token=mvvYlJ7Jbm4IG3pZiGAFVICNhTKw52LSJA6tDyiaZfr2xxHd8eSG-pRZDsUAc7N2DjYA1HGwiDHZhT8PhzRGTvizqjCH8Q1lQenpBUZpwqNeErUngaqFCrXJuqBTIOdjLAsWS-QsHJLqm361VwKq3KWCJ5AIOY3JTUzdGVxe0gBXXst7g6pTz0_mSrTjg6E0znAKwIrUZOJ0NM_rZaQz15p-a-_P6PbCf0UpJEQ7yvry-fsK-pdV6JbvdLMtiNvnWpIdBHJUTd8ALJt7FVnhtOUZyF36UxK7Vn-ZLBDCc5T3gTXD59UiwyW2fAbkyOtuwifjd5QhOdV9IqfuPe396Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای انفجار اربیل را به لرزه انداخت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/672290" target="_blank">📅 23:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672286">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9ZiDaOYklRoOsA4j7eUL8tUiF2gBPCwxTgR3M8iNuADWHqV3Hs3HXMX1O2p04UwIEvuGAvTnLcXxAWDX30EAAAxOap_LnfdqTqVFgAu5g6ozKrHTvz06517c3kbTi54QultYovweci6WC6QujLrQvrHHP944AHK5GzEiNmGDV6EAmNEL1tsUltYqO3MmYc07X5pJZYA2hnUQ1HSkiqCqbiEZ-y4mh9JGpWUHEtDevpkfxAfW4yHzkhPzviekfgyRVBqAskzJGwiQC2oFLFS-mu9HHH0IfROuOC4cLOmzB8hkJUxh8W0I5gkoyEOOgqRvBkkrAbQVQj3_amuYSdezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IQAUS2mg15fpZLs3DGKSajXuzfkxIfuYFSC4lOudD27rLYGSJwik_ecNRzPvMynCbnUIG74vC6w26RsUKk0XO0uPsUxGhauwHpM1sh6F8egkl5j2YZ_6Tg9JPqXh7fHhKmoYUBj6DUtTa3FDBUSg3H3A9SeITdr-7kVXJq1hJ4EcXzSgsSVx6-104xDcQFvEThfe3TcdWwml6NM3TnAvxSBl779oC2lmMFjAr-06_WfmeYkRJLVI1ys_g6yzhqLz19sGxyh3nMobAZvH0qXJkL03cYqXvcdqwmSlL6CESr6zBH8wHFKElts5KGFi-cXNB7TL42QqxCwnSHHMdWGxlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی: تعداد زیادی از آمبولانس‌ها به مقر تروریست‌های تجزیه‌طلب در سلیمانیه عراق روانه شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/672286" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672284">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb16946e3.mp4?token=frG_CeHUbBp63lG8u_F1hSFJ2tPb_zic6AYwDJv2gCmNhG8QJA9XTgRVSvoThwuBPy4awfuad6o4ABJhw45LDhlLMEouXEl5bFu4zrNrpnRZutc4W3TkMIDLQnwYAFu1rlK6BiE8ZTG48DIJGMnx70DDz7O5C5nTShXqjet73c50MYDIlwyvy3XH6spxfbb2WaAdYuqW-PHiD41OGm9v8Ll7_IzfPKGk3u_aNdLGJLiPEo_pfH9gaW27_gUHDAK0Lg9tcaZAK5N9w6uP4K4dWiPOnTFRSHqRCdzsWZJFVHMkRiUJvea-gW7GRB8yADlaG6ueYEjg6b-tEgYptgAwww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb16946e3.mp4?token=frG_CeHUbBp63lG8u_F1hSFJ2tPb_zic6AYwDJv2gCmNhG8QJA9XTgRVSvoThwuBPy4awfuad6o4ABJhw45LDhlLMEouXEl5bFu4zrNrpnRZutc4W3TkMIDLQnwYAFu1rlK6BiE8ZTG48DIJGMnx70DDz7O5C5nTShXqjet73c50MYDIlwyvy3XH6spxfbb2WaAdYuqW-PHiD41OGm9v8Ll7_IzfPKGk3u_aNdLGJLiPEo_pfH9gaW27_gUHDAK0Lg9tcaZAK5N9w6uP4K4dWiPOnTFRSHqRCdzsWZJFVHMkRiUJvea-gW7GRB8yADlaG6ueYEjg6b-tEgYptgAwww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادهای انتحاری به پایگاه تروریستی آمریکا در شمال عراق
🔹
خبرها از حمله پهپادهای انتحاری به پایگاه نظامیان تروریست آمریکا در اربیل، در شمال عراق حکایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/672284" target="_blank">📅 22:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672283">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deafedf62.mp4?token=sKvRgibUgbqIoGSQnwAuybkCRp2QO4jp7DBynEc8JVy0QEYKYIIhF07MwxH54nuFWBXsoqNgiOHiaNcWine3D4kYL8FroiHtTEHwqMQs8TQCGsw2RDFZYLfEg8WtsLFXfH1JeMy-dE5-wYpO-B28sycNuBJ-KtmtVziNO_hMOpNwaaorT4eZaJ0_RSgpW8OG1Kv54XPyBNRsqS8FK4-Dk1Qzauj8fT2vAVx71nTrht_aOVdVQBSGxf0zCs1S1ItKh16KrzZMjADfOMp0zs7Fxo_Z7p9FAR5_JPA7ZQm3I20t1ICvkr9BZTWYLu7njdnwktvSb4v9rxf-BOZ75tuMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deafedf62.mp4?token=sKvRgibUgbqIoGSQnwAuybkCRp2QO4jp7DBynEc8JVy0QEYKYIIhF07MwxH54nuFWBXsoqNgiOHiaNcWine3D4kYL8FroiHtTEHwqMQs8TQCGsw2RDFZYLfEg8WtsLFXfH1JeMy-dE5-wYpO-B28sycNuBJ-KtmtVziNO_hMOpNwaaorT4eZaJ0_RSgpW8OG1Kv54XPyBNRsqS8FK4-Dk1Qzauj8fT2vAVx71nTrht_aOVdVQBSGxf0zCs1S1ItKh16KrzZMjADfOMp0zs7Fxo_Z7p9FAR5_JPA7ZQm3I20t1ICvkr9BZTWYLu7njdnwktvSb4v9rxf-BOZ75tuMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: به هیچ عنوان از انتقام خون قائد شهید نخواهیم گذشت
🔹
امنیت و آرامش آینده ایران در گرو تحقق انتقام خون رهبر مجاهد شهید و شهدای مظلوم جنگ‌های تحمیلی است. #تقاص_خواهید_داد  #WillPayThePrice #خونخواهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/672283" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672281">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OaEhcT3yD3yXdofGtWiIFO9TYv5RONJepzN-bbn9RegD28zUN6T7bmI-qEk0IlD7GHvtsZyFexSsaACWma3B1T01rT6hSOIPJvPcVQxKbqpqiVjHB33t9aqgK6oWh5R3-ecKnjr0TOXjFXNhN0P6QrWICSov-5B2xh9ocrnlVdS4DyG8B8dEYChHu56CiJeHnWONCEsaz9-V9cuGeva2CEtxVzKzH1ToUJNV2xuGIhlwPoq7tjzNy7q433GOFKbn5q_7vxyFrIkTuIOm2FhjaFiDFsv5Z-_x7nTh8K7vlsuLPW61CFfGT8QVtk6r7xEfQ_lv3HynXIMxRFgJVfzhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCC1FLVHa6MrQkc6Ed8zT8Kw8EvLHBFgLf_GCRr8axQ0dLp-PUn5jR4ES_77W-HPT_T6nA9ACxbCJwy6PRY95PCcNW_7NvyiicYWNgerkORJP3L2a4TiFnsVlmppvExN-3mDrpbjuHZ9TY7CqwkMPYQ0H9FTvt4-o2APLz1l_DQnPicU9Hq4hhlyKncCDkqQfpFMp2XBmsGXxJ6crD4jFtkvSK5SaL-YxsI-M15H4npGWqRO9eu3L7az85onDXPxyaLF9rAhMK0OP61vKMKqAOI8NPBNWcJW-fc3WmVrh0SNyzQJwMISLoCOWZr-Fd-mmi6j9rTHC9K-mOwYlLlIpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
استوری بیرانوند در واکنش به صحبت‌های علی دایی نسبت به تیم‌‌ملی
فوتبال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/672281" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672280">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: به هیچ عنوان از انتقام خون قائد شهید نخواهیم گذشت
🔹
امنیت و آرامش آینده ایران در گرو تحقق انتقام خون رهبر مجاهد شهید و شهدای مظلوم جنگ‌های تحمیلی است.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/672280" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672279">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
حمله پهپادهای انتحاری به پایگاه تروریستی آمریکا در شمال عراق
🔹
خبرها از حمله پهپادهای انتحاری به پایگاه نظامیان تروریست آمریکا در اربیل، در شمال عراق حکایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/672279" target="_blank">📅 22:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672278">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تصویر ۳ تن از شهدای حمله آمریکا به پل بندر خمیر
🔹
این ۳ شهید اهل روستای نیمه‌کار بودند که درحال رفتن به منزل خویش روی پل به شهادت رسیدند.
🔹
در جریان این حملات ۸ نفر شهید و ۱۹ نفر مجروح شدند. #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/672278" target="_blank">📅 22:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672274">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
سرلشکر رضایی: سیاست هم مذاکره هم جنگ تمام شد؛ اگر آمریکا طی ۲-۳ روز آینده آمریکا جنگ را ادامه دهد وارد مرحلهٔ «تهاجم و انهدام کامل» خواهیم شد
؛
به طوری که پایگاه‌ها و سربازان آمریکایی در فراتر از مرزهای سیاسی هدف تعقیب و تهاجم مستقیم قرار خواهند گرفت
🔹
رضایی ضمن رد هرگونه مدیریت مشترک تنگه هرمز، تأکید کرد کنترل ایران بر این آب‌راه برای امنیت ملی و جلوگیری از سلطه آمریکا بر بازار جهانی انرژی ضروری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/672274" target="_blank">📅 22:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672272">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
محسن رضایی: آمریکا با نقض تفاهم‌نامه و حملات نظامی، از فرصت آتش‌بس برای بازسازی تسلیحاتی خود بهره برد
محسن رضایی:
🔹
ترامپ پیش از خروج رسمی، با نقض بندهای توافق و حملات نظامی، تفاهم‌نامه را از بین برده بود
🔹
آمریکا با محاصره دریایی و اقدامات نظامی، به دنبال شکست مقاومت و تحمیل مذاکرات است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/672272" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672271">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84851cccf2.mp4?token=EoKWhwdjIfxYMwUAdZq1oun1JKtV8miPVlX0WCSuirxwx1wdEnULi95iZj14x3bIl9h9aHlrunEHdkQRLbYATLWqszw19ujpEHhMxr7r8EQ_9EsQaCsq6lYRu8CnmWMsfa0Q8DJ9GXY6lwZswqZtmdqKkHyKuLQ6KR7Ei59uRCIm7tbMWwrpWwCGdJK6_EAymeaGhzPqz7J1P0MoGYOfOEWD76w9OA7rmwkD-CTsdgydRwWXPPp64R7WZnte6MhKcMVyfYvaxxUhFA2NjdzPqYm-TMc-DDrB6ETZHrhNDcq2HDtujDtZPVqtClQKNHZuchQBBXPkMCbiePG1DzBG4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84851cccf2.mp4?token=EoKWhwdjIfxYMwUAdZq1oun1JKtV8miPVlX0WCSuirxwx1wdEnULi95iZj14x3bIl9h9aHlrunEHdkQRLbYATLWqszw19ujpEHhMxr7r8EQ_9EsQaCsq6lYRu8CnmWMsfa0Q8DJ9GXY6lwZswqZtmdqKkHyKuLQ6KR7Ei59uRCIm7tbMWwrpWwCGdJK6_EAymeaGhzPqz7J1P0MoGYOfOEWD76w9OA7rmwkD-CTsdgydRwWXPPp64R7WZnte6MhKcMVyfYvaxxUhFA2NjdzPqYm-TMc-DDrB6ETZHrhNDcq2HDtujDtZPVqtClQKNHZuchQBBXPkMCbiePG1DzBG4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه تروریست‌های تجزیه طلب هنوز در آتش می‌سوزد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/672271" target="_blank">📅 22:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672270">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEzdvcRDzzC6bdRGC8ei9b91Tz14SJYmtmd3bG5veQ1Vmolkx0hqkl3RyKO0nhLLhQ2yaqpa3irnXd6Wivp9tQQs0BhL1hEo3-v4Ddak-4Y0OExonzVd_xLVkN5yRnOK8xbiOUGeHW8OazeNn4YIzhJXWLpYy5CxWM_S09IRLZm2csrTY8OEGGJk9FZgaYpW345EoU8DT_TehX3e9-YcrE4_BT5XmrEsMeJWXASLI3YpvT-t2DeahtAkpFIXi7JomTtYhEp9o2WbHX9FhPDPEfKjYPRgZQQkulYK_4je-KrgwkSQ2CIzSyAaKT8E0WsvEaBenAVhqY4TwdeEYRmlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای همدلی با مردم شریف و مقاوم جنوب؛ ایران وطنم
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و با لهجه شهر خودتان، یک جمله همدلانه و امیدبخش خطاب به مردم شریف و مقاوم جنوب کشورمان بگویید.
🔹
در ابتدای ویس، نام و شهر خود را بگویید و با صدای واضح و رسا، پیام حمایت و همراهی خود را به گوش مردم جنوب ایران برسانید.
🔸
صدای شما می‌تواند روایتگر همبستگی، غیرت ملی و ایستادگی مردم ایران در کنار جنوبی‌های عزیز باشد
👇
#ایران_وطنم
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/672270" target="_blank">📅 22:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672269">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پرس تی‌وی: هیچ پرتاپه‌ای به محوطه نیروگاه هسته‌ای بوشهر برخورد نکرده است
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/672269" target="_blank">📅 22:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672268">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
اعتراف کویت به اصابت موشک‌های ایران
🔹
کویت به اصابت موشکهای تلافی جویانه ایران به دو موضع در خاک کویت و به آتش کشیده شدن آن اعتراف کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/672268" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672266">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC_JddAQkDjl6ryra3S_QKQsyiGMjWcQdWgtxDTQrOnXbJgFJd7Ya0MuWWqfMcgKiq_cx5aci8qRVoFlnqhI4g9wU3Brh6E11KEH3N_wiHKqcbbnfwlXYFTiUmCySUSVAa1789L3uP9A0PmwzFaDIBVNLi9CLwVaC-mJ-GM5wXpsYxim4xHB0SxfE20DA-tfqs4SLBTfWiGyUAPHurICrPgAeWshTmrvJrGjThK2LnyA6hza4uctpM35-hHlTLCJRNV3JFGtmc19viYm_dfRqFGufDAkO9Og-DlxQsaCbEMEtZsWtFFD8a3PmMl5aW6Y98LZeymonujuMAaQ6ItTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر ۳ تن از شهدای حمله آمریکا به پل بندر خمیر
🔹
این ۳ شهید اهل روستای نیمه‌کار بودند که درحال رفتن به منزل خویش روی پل به شهادت رسیدند.
🔹
در جریان این حملات ۸ نفر شهید و ۱۹ نفر مجروح شدند. #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/672266" target="_blank">📅 21:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672265">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqJzU9-S5lOjo-svVK4pQUsmRZEvqrh5xeopDykpjZjcjW1nUXC6kGu59ZdMDWz_bn0AzaNqZ5zo-FQeZZxGgILDOPzpCFwHg1IKHuzCZNyKhpgTnXG_ZoGd6yF9JEkbn09Pix35JnrMLtDigUTEGWMTz2MGf-uURBlEbQPC63tADcAE5LYmW9eUaRyB8bEa0rSbOjgtUurMahTHiXa6e6KwK_bXr0_BzwIh1rFbRYxarBPP6qGUt_hJGepAkC6AZpCRLyBj2F_sR9elDtyAQJuynSMnjUwKQBuKIAJIGMKtqd4G5TR4lremw9nI8W0NawaaC54aQ6_ZZdg5Kpl45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت بورس امریکا در لحظات آخر این هفته معاملاتی
🔹
ریزش سنگین بدلیل درگیری‌های تنگه هرمز.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/672265" target="_blank">📅 21:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c71764ae7.mp4?token=Y9AumAVJQWJzyENLnUBqwVKKKDxv5HZuBcJXIE_sScyuS2jFxx8CwavF1koRjwSr9hFM5CkQK30zdBpK_VHIlPOMNX9H6b_-ObVT7Q7SGnBKZuESD447Nx9XerJ99h71fk1n7BVPZPwwTMPVshk5DlmN3iRB1ZB7Su3V73dkTlx5U7frp7oPfhF0E2dIoM_TxPvnWt_Ani7t7hQBpl0qUlgThaeA5EVzK6qWoJrpDvXiG8QlmbB0er2TSnnbfGFetJ5UQrbGgaY3-jMphh0QIBPMOP6dS--LVCE2AznbOesowCcnrBO4D2OJwoUn8c2ba7XbxaonxHPrdvBNuNrJo4Y4_2I81-Vi8bj_ZDcc8UfuovCJkQGg-rKVzrZEO7bY1b6C4ouQlTdBHsgl2vwb6r3fRLneSuXFo0oEfvfmvH0TDBpuzcHq_AsL-LqkYrw4gPFRSs7GD_PJpS9IDeXs7S1UyW4XKybyXQQyh8wDzPyxNm7MQuD5-1CukgKKXHbqDlL0TZsZhQwVkAObdYucys_FXcVgnYOJm2OAU80nhoTjA6LnhrAsmqgkBgsOkaqBO-Md_o6TGqcUq3Oj_JNY3SXbSj8GBes6vbzE66oghokMgaMhTJK3r9gjEi6JW5o44jvbT2U0i6_73vEYZwGmV9c_P_4GUgaHbIECJdlPr_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c71764ae7.mp4?token=Y9AumAVJQWJzyENLnUBqwVKKKDxv5HZuBcJXIE_sScyuS2jFxx8CwavF1koRjwSr9hFM5CkQK30zdBpK_VHIlPOMNX9H6b_-ObVT7Q7SGnBKZuESD447Nx9XerJ99h71fk1n7BVPZPwwTMPVshk5DlmN3iRB1ZB7Su3V73dkTlx5U7frp7oPfhF0E2dIoM_TxPvnWt_Ani7t7hQBpl0qUlgThaeA5EVzK6qWoJrpDvXiG8QlmbB0er2TSnnbfGFetJ5UQrbGgaY3-jMphh0QIBPMOP6dS--LVCE2AznbOesowCcnrBO4D2OJwoUn8c2ba7XbxaonxHPrdvBNuNrJo4Y4_2I81-Vi8bj_ZDcc8UfuovCJkQGg-rKVzrZEO7bY1b6C4ouQlTdBHsgl2vwb6r3fRLneSuXFo0oEfvfmvH0TDBpuzcHq_AsL-LqkYrw4gPFRSs7GD_PJpS9IDeXs7S1UyW4XKybyXQQyh8wDzPyxNm7MQuD5-1CukgKKXHbqDlL0TZsZhQwVkAObdYucys_FXcVgnYOJm2OAU80nhoTjA6LnhrAsmqgkBgsOkaqBO-Md_o6TGqcUq3Oj_JNY3SXbSj8GBes6vbzE66oghokMgaMhTJK3r9gjEi6JW5o44jvbT2U0i6_73vEYZwGmV9c_P_4GUgaHbIECJdlPr_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع پیکر ۲ شهید حمله آمریکا به بندرخمیر در اجتماع شبانه
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/672264" target="_blank">📅 21:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672263">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f219ddcb5.mp4?token=gKQId9XydBoAE1tYCSNLt1twd9HgsJ1ndfqES7i5jiZFIewhJ_7TnPfReQcOxLnmJY4oL1B99DquszvN74ZFmu3i0k4_ttk58piBMfWUA38gLLUEk1BbydS1dEeH5LUtYNGEBIehRZqtm_dQnq_uQ8PVOy6FjDLA41nSJuUj079cwPwzom5SDClA4zzhUWawG1mc2C4c8p5isVbzVHzr5KmP9u0qlwmbMF9gXIMIRPV0Mtpwc88loybv5_oaLHN4DL_7IWHBYpuQIviQjlAHF9Szi0sGnPB-j26TNa_hnfPUPVUmmFirYexTSH4JPWgMzonYXuCdhcLU7lPNN6mKAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f219ddcb5.mp4?token=gKQId9XydBoAE1tYCSNLt1twd9HgsJ1ndfqES7i5jiZFIewhJ_7TnPfReQcOxLnmJY4oL1B99DquszvN74ZFmu3i0k4_ttk58piBMfWUA38gLLUEk1BbydS1dEeH5LUtYNGEBIehRZqtm_dQnq_uQ8PVOy6FjDLA41nSJuUj079cwPwzom5SDClA4zzhUWawG1mc2C4c8p5isVbzVHzr5KmP9u0qlwmbMF9gXIMIRPV0Mtpwc88loybv5_oaLHN4DL_7IWHBYpuQIviQjlAHF9Szi0sGnPB-j26TNa_hnfPUPVUmmFirYexTSH4JPWgMzonYXuCdhcLU7lPNN6mKAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهادت یک مادر و قطع دست کودک یک‌ساله در حمله آمریکا به بندرعباس
🔹
در پی حمله آمریکا به محله «تپه الله‌اکبر» بندرعباس، یک مادر به شهادت رسید و ۸ تن مجروح شدند. دست کودک یک‌ساله این بانو در جریان انفجار قطع و وضعیت وی وخیم گزارش شده است.  #اخبار_هرمزگان در…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/672263" target="_blank">📅 21:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672262">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72169cd2e.mp4?token=OvSM-L9sd6lmE4ICsmdiP9g4G0F0ZJuyUb3nHwcRYZBSHJLzidLyV643WCnVZwwD15kPyDAwyDnUUwOzfRQa1LJs3-fjWDm3UGyHia2HsbJ_FGJ-Y4COYWhTrRU2ci-wy--Xw0EmdZpoVvtdJyT1OlscTHYQeOVTsHnhaKzV1YvpQGgbLS8Sg6rc5LU3hZRJvD_53vW0lUMMiiC5zN0JkGThiNC5DaY5Ex3etKGwvtGIa3Qjeabl4mfNOgc3i-bQkmz5hXmGzr5ABzMMQyWk1LjlxkI1H7KJGz7obJJoZ46tnDS1mxaTOM_Ez1CT0JOxRRefWEMgZv-Y6eJMuZX57g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72169cd2e.mp4?token=OvSM-L9sd6lmE4ICsmdiP9g4G0F0ZJuyUb3nHwcRYZBSHJLzidLyV643WCnVZwwD15kPyDAwyDnUUwOzfRQa1LJs3-fjWDm3UGyHia2HsbJ_FGJ-Y4COYWhTrRU2ci-wy--Xw0EmdZpoVvtdJyT1OlscTHYQeOVTsHnhaKzV1YvpQGgbLS8Sg6rc5LU3hZRJvD_53vW0lUMMiiC5zN0JkGThiNC5DaY5Ex3etKGwvtGIa3Qjeabl4mfNOgc3i-bQkmz5hXmGzr5ABzMMQyWk1LjlxkI1H7KJGz7obJJoZ46tnDS1mxaTOM_Ez1CT0JOxRRefWEMgZv-Y6eJMuZX57g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه تروریست‌های تجزیه طلب هنوز در آتش می‌سوزد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/672262" target="_blank">📅 21:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672261">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ0IhmcK3z82EF_otNNqBxCCJRjSekXz87GyBKYdDhShYpcVOdDuzNzr0xo-ZOiUK5ePdXd73GnUGB-KM5FpkXJ9bVTitQZVd7yS4oaSK-kfDyeRM2XBdt_hrDbyK7-ugQ31uB-v-akQOX1u7Q1q5rcHzRAibKir33KKCvEZk2PqyNYfFe7DIGzXWO4ZLtZkn3p5tg3VwcW1u2dYD-6XKxizgypsjNpOAobqt8AFVmH3D5tcAb4Gh1-SG6rtuu4WTgXMCGXEFIFvVf3YVVYOIUMMnXMDgIRKrqrICTxrB1oLJZeLoMy4CdsanJkHquyrTDmjWaST9FkyL3GiT-ckMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت جهانی نفت به ۸۸ دلار رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/672261" target="_blank">📅 21:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672260">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf1d7b71d.mp4?token=YimTECpT8u094D7CnD0Mrlc4Uig8a4M3wgHgklzbmhugRNW93mG_NAbX17VrJKDt9kV3d8X8dW7rPLIBytwyH3lrgR7F5IWIgRa5qN8Vj2pcJ_n221NQ3mOOxiM9uXud3p_XkSHB9nZylqVg1_v8X4Ip8uRTfaK4xA0D74kE2h7nMduWiQY3Bky7L67XBzMCOswuOU-JxIF3M0GVYgKqJdElAi3szUL_j2uOoXG4x2MciMxDW-8CZBt8ozfRLLoJarxgbCQgAZLNMOle5YCH35_J2E4gCdr1RO0v78c-NnSIfTNRB8RAoTPcYUqaQo8b7iGJOM2Y1BGjhpEk55JT352OR99zOJnNGWnOosOuEiu4FAnXxfrJUW4natQYvNzLAyrr8YeOdrcjc2HuNhx-d8hjzjxiWRyBoX7QCEmfn8VYDiDBUrZIhbjJtNft52XZa402I8sqglzjFo9PtcDU9TRvMTbg-rDXV4s43Wsu31Oc04ciY5hlJ2TbfELre3oRu4y8wS5cH-mEIx66RnBe50cszNeUTJoaRrtlU2RDUEKFFoiAFGu4qKam6oMfbdQ0Nh065WChtZRz0p-dtFlFDcfUFpc_-j74R4vaE5EWOCB7chB45bgkI3_SNI8CUfRvVZmaTCxPTkawrq9B7E7RMOmT074Iga-5TUM5hu9WQz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf1d7b71d.mp4?token=YimTECpT8u094D7CnD0Mrlc4Uig8a4M3wgHgklzbmhugRNW93mG_NAbX17VrJKDt9kV3d8X8dW7rPLIBytwyH3lrgR7F5IWIgRa5qN8Vj2pcJ_n221NQ3mOOxiM9uXud3p_XkSHB9nZylqVg1_v8X4Ip8uRTfaK4xA0D74kE2h7nMduWiQY3Bky7L67XBzMCOswuOU-JxIF3M0GVYgKqJdElAi3szUL_j2uOoXG4x2MciMxDW-8CZBt8ozfRLLoJarxgbCQgAZLNMOle5YCH35_J2E4gCdr1RO0v78c-NnSIfTNRB8RAoTPcYUqaQo8b7iGJOM2Y1BGjhpEk55JT352OR99zOJnNGWnOosOuEiu4FAnXxfrJUW4natQYvNzLAyrr8YeOdrcjc2HuNhx-d8hjzjxiWRyBoX7QCEmfn8VYDiDBUrZIhbjJtNft52XZa402I8sqglzjFo9PtcDU9TRvMTbg-rDXV4s43Wsu31Oc04ciY5hlJ2TbfELre3oRu4y8wS5cH-mEIx66RnBe50cszNeUTJoaRrtlU2RDUEKFFoiAFGu4qKam6oMfbdQ0Nh065WChtZRz0p-dtFlFDcfUFpc_-j74R4vaE5EWOCB7chB45bgkI3_SNI8CUfRvVZmaTCxPTkawrq9B7E7RMOmT074Iga-5TUM5hu9WQz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اصابت دقیق پهپاد تهاجمی نیروی دریایی سپاه به یک فروند نفتکش متخلف در تنگه هرمز
نیروی دریایی سپاه:
🔹
تا پایان شرارت‌های ارتش تروریست آمریکا در منطقه، تنگه هرمز بسته خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/672260" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672258">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27926a0c3a.mp4?token=v6_atXnq_OEMpGfQY2tmKWIYcd-1pQz4E0AHpNIjSuO5B4Ol-GP_GS0r8cJThJoh0-cwbS4eQ-1xOO6GWh4GmWUP8bmMpiqj2dWnX4oHTJrs6Vu73qqHGabCO9VJRAgx0RRntY8C_9n82UBrtYdw4tNHGCGEQOOAuwNfcfecyIa0AcHqQ1DtKnGjOC99Oq5YBDhxcvsm0cpL550L9F52LSHW2Zf4cYHBo2sqzIOzzetRwE3fmaGaPXGdRHxUlEpdqrTzBrT1KrEPobSh0HemIzKE8kC9s337nYGmYEMSqj5xe5uD4C3Lm9I9e4d594hTeBZHE2TGKjuiUjd0ZNZrig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27926a0c3a.mp4?token=v6_atXnq_OEMpGfQY2tmKWIYcd-1pQz4E0AHpNIjSuO5B4Ol-GP_GS0r8cJThJoh0-cwbS4eQ-1xOO6GWh4GmWUP8bmMpiqj2dWnX4oHTJrs6Vu73qqHGabCO9VJRAgx0RRntY8C_9n82UBrtYdw4tNHGCGEQOOAuwNfcfecyIa0AcHqQ1DtKnGjOC99Oq5YBDhxcvsm0cpL550L9F52LSHW2Zf4cYHBo2sqzIOzzetRwE3fmaGaPXGdRHxUlEpdqrTzBrT1KrEPobSh0HemIzKE8kC9s337nYGmYEMSqj5xe5uD4C3Lm9I9e4d594hTeBZHE2TGKjuiUjd0ZNZrig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محل انبار مهمات تروریست‌ها/ الان سلیمانیه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/672258" target="_blank">📅 21:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672257">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c411da7d.mp4?token=Z3uMU5PcKGbk8v_o5U0IoG7EqsCPaF67sCfhMP5PkqmtscEViu8bSnnicpfqBYT6w4CDKioTCEJYtrOM8rCEn5dWIa1Md6vjJIojywCulv01ipNLd7A4nGB6OLDCqpKuSZnfrP8dZqJ2RBHvvmDlSmJ9TJ1fLfEZMZsL43N-tvWBn2nAtYZK_VgA0yPm9xWU3C-tbsXJ3EkZkHtJnkeUKvKjpLEErCz3dOp6rRxiX5r2IbaC3paL3gz0AbHE0vUQGf7E7koAmKyKzjZC5w5JXvhDaj-RsZmMf9yC3ALB16CXZuytIoU3RpILNOsCC4Ipt3hNpLMFpkO-ZeqKjvHnAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c411da7d.mp4?token=Z3uMU5PcKGbk8v_o5U0IoG7EqsCPaF67sCfhMP5PkqmtscEViu8bSnnicpfqBYT6w4CDKioTCEJYtrOM8rCEn5dWIa1Md6vjJIojywCulv01ipNLd7A4nGB6OLDCqpKuSZnfrP8dZqJ2RBHvvmDlSmJ9TJ1fLfEZMZsL43N-tvWBn2nAtYZK_VgA0yPm9xWU3C-tbsXJ3EkZkHtJnkeUKvKjpLEErCz3dOp6rRxiX5r2IbaC3paL3gz0AbHE0vUQGf7E7koAmKyKzjZC5w5JXvhDaj-RsZmMf9yC3ALB16CXZuytIoU3RpILNOsCC4Ipt3hNpLMFpkO-ZeqKjvHnAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار رونالدو با نسخه کودکی خودش در فضای مجازی احساسات میلیون‌ها نفر را درگیر کرد
🔹
این شاهکار که توسط هوش مصنوعی ساخته شده در فضای مجازی نزدیک ۲۰۰ میلیون ویو خورده و خود رونالدو هم لایکش کرده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/672257" target="_blank">📅 21:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672254">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5aeae1ea.mp4?token=pK00EMYcq30s9WehEYco21wBRhBWhsu3wIMGSpyo8XhxGy15OQHkjgPQ5UFVMviOlyqRo2zEBt291bEkZKJ9UeSFORDHc68X6gSe_v5dJpTZH_25X10r4vWcenlTPfb2oeo5sP3zQBj2MdDbG2xMBw7klU7A9BOO_tQ65WM6c8Kmw7j39PvlXpB9NY3slQgVpAJow_gIHYlAmcUSd6Jm3hiIeAPYBUxiGi8myLTeDqQPN6StDhtVGbeNodcOEAVn14kZdMM9eHdsklyPS-qXxcaqSbY_KD0z6cGZ4YPVLOT05STX7N4ZEaI515zMM5bE69PvDg-0Re7PCI0dqTQ4-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5aeae1ea.mp4?token=pK00EMYcq30s9WehEYco21wBRhBWhsu3wIMGSpyo8XhxGy15OQHkjgPQ5UFVMviOlyqRo2zEBt291bEkZKJ9UeSFORDHc68X6gSe_v5dJpTZH_25X10r4vWcenlTPfb2oeo5sP3zQBj2MdDbG2xMBw7klU7A9BOO_tQ65WM6c8Kmw7j39PvlXpB9NY3slQgVpAJow_gIHYlAmcUSd6Jm3hiIeAPYBUxiGi8myLTeDqQPN6StDhtVGbeNodcOEAVn14kZdMM9eHdsklyPS-qXxcaqSbY_KD0z6cGZ4YPVLOT05STX7N4ZEaI515zMM5bE69PvDg-0Re7PCI0dqTQ4-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خانواده‌ها در منطقه تسلوجه سلیمانیه خانه‌های خود را در نتیجه انفجار انبارهای اسلحه ترک کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/672254" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
