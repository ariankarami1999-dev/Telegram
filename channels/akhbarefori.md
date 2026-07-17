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
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 17:40:19</div>
<hr>

<div class="tg-post" id="msg-672190">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62390cef03.mp4?token=WZwn36Bk4XCUC9GLX76ppb0W0nZk2wIGCPAYZStlxjP5O0PokimfzPRGt9elaciq-DcHH8LNyK_yimfup09xR8WQK7BxpOJIoSrmjVfr88CeKts89fM2Tj_5DWN8dIqfesYI7bBewYX-XPjunNe0HQamij8M6Tpn0YFKRLx4x2cIhXTldtHB_bjpp5-_p56wfdFKp5K9LqX2VZ-ojDn53xQBAWi3YRB9ojOwAbXAIFFoPhZ2AuuFvet7DaY3oC6rZjtf-TZvSPdoZIt8vzMIah2azlr5dvBmv6o0xib6WfYX8GskPSTQ2WJhV2QSbJ_D4dUkSG3cOFctu_WvRq-9r3IarexCiptPD1d7kId2NraesyPAyr1a-itr_1n4T3y6D_nKQtRLTtXkdNV2uUPYQbECOLeb0JQwkGM5ulHY0VF_QEGftQSsCHAjTFLXukNDBhTo33KdqIRggT9JSV04ubYE1q-04GrxxnJFgCB5I0VnPmtPsWtzrwdUG4nP1Pt7_TvOPejOxe1pm2o2YQCzWLeVMeydvHuF7nGdLxNgjmBBS2qgImOi1pHR9B1zinNmcQLgrJMRVdlZtEKFB8i4StNhHroZFLiYPzcZnXM0pkTqvppyUIBUsddrPI7oKyTr7zRwdaOUHMo8C9vIdBPkPj4_Xx9NlBlLb056YrxsPrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62390cef03.mp4?token=WZwn36Bk4XCUC9GLX76ppb0W0nZk2wIGCPAYZStlxjP5O0PokimfzPRGt9elaciq-DcHH8LNyK_yimfup09xR8WQK7BxpOJIoSrmjVfr88CeKts89fM2Tj_5DWN8dIqfesYI7bBewYX-XPjunNe0HQamij8M6Tpn0YFKRLx4x2cIhXTldtHB_bjpp5-_p56wfdFKp5K9LqX2VZ-ojDn53xQBAWi3YRB9ojOwAbXAIFFoPhZ2AuuFvet7DaY3oC6rZjtf-TZvSPdoZIt8vzMIah2azlr5dvBmv6o0xib6WfYX8GskPSTQ2WJhV2QSbJ_D4dUkSG3cOFctu_WvRq-9r3IarexCiptPD1d7kId2NraesyPAyr1a-itr_1n4T3y6D_nKQtRLTtXkdNV2uUPYQbECOLeb0JQwkGM5ulHY0VF_QEGftQSsCHAjTFLXukNDBhTo33KdqIRggT9JSV04ubYE1q-04GrxxnJFgCB5I0VnPmtPsWtzrwdUG4nP1Pt7_TvOPejOxe1pm2o2YQCzWLeVMeydvHuF7nGdLxNgjmBBS2qgImOi1pHR9B1zinNmcQLgrJMRVdlZtEKFB8i4StNhHroZFLiYPzcZnXM0pkTqvppyUIBUsddrPI7oKyTr7zRwdaOUHMo8C9vIdBPkPj4_Xx9NlBlLb056YrxsPrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش دوخت خلاقانه کاور برای دستمال کاغذی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/672190" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672185">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037e23375e.mp4?token=FXDQoxuoebkstJIuQvJAEE9g6_cNcjfL4IdAmY0Z2yYlIqqL32NsgHfSZXldNmmINqcWF8UIC_lY1N0J7_FG4mPzBbruWZljJpu9xm3_Mv2e3fkmeDf8GSSjRB2-M1HTc75j5TIwxjh-D4-isTBNaRyIZVY5u5ZdLX5OJd6MKOwCTCbat0sL71UN4-BaXnhO3tiVn1Ym9Wnb5LRyT2NPrXgO7J3SXpRyCdSI57MO2n_PCQpDWDPDW8ilM1SbA93DNcxOC5aR2gQ9zUPchbtW33T6bhOcd-YyaES1jJTy5VhM7fSZEd9npONSKx27bx2URCK-dKchTSEoENKWgGuoNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037e23375e.mp4?token=FXDQoxuoebkstJIuQvJAEE9g6_cNcjfL4IdAmY0Z2yYlIqqL32NsgHfSZXldNmmINqcWF8UIC_lY1N0J7_FG4mPzBbruWZljJpu9xm3_Mv2e3fkmeDf8GSSjRB2-M1HTc75j5TIwxjh-D4-isTBNaRyIZVY5u5ZdLX5OJd6MKOwCTCbat0sL71UN4-BaXnhO3tiVn1Ym9Wnb5LRyT2NPrXgO7J3SXpRyCdSI57MO2n_PCQpDWDPDW8ilM1SbA93DNcxOC5aR2gQ9zUPchbtW33T6bhOcd-YyaES1jJTy5VhM7fSZEd9npONSKx27bx2URCK-dKchTSEoENKWgGuoNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باران‌های سیل‌آسا در شمال ویتنام
/
تخلیه ساختمان‌های مسکونی و تخریب جاده‌ها و زیرساخت‌ها
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/672185" target="_blank">📅 17:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672184">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: شورای نگهبان افرادی را فرستاده بود که از همسایگان من سوال بپرسند که آیا همسر من چادری است یا خیر/ شورای نگهبان کسانی را مامور می‌کند که در خانه طرف بروند که ببینند ماهواره دارد یا ندارد!
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
خیلی‌ها را به خاطر اینکه حرفشان مطابق نظر آن‌ها (شورای نگهبان) نیست، رد می‌کنند. بسیاری از این نابسمانی‌های سال‌های اخیر محصول تفسیرهای شورای نگهبان است. تفسیر کرده‌اند از راهی که دوست داشته باشیم، می‌توانیم نظارت کنیم.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/672184" target="_blank">📅 17:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672183">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458316cecf.mp4?token=nAwmeLqFSwIoxcgHKn3pP0m9RFgT77aRs5a_H1DQ0-iwPrCWfM8_QPlQ8i8oie4jt5UtkN2SuFhCnEIkI4UN2m2uQWdAzvHOXcMLGacFjukrvfQY8lRH25DsZrudB4gN9WUoUkCwS-VYVK1eScvtZ96aQATrmqGy9eApA2NRui2p0Gd0MNF8T5zvK_tQVK7kU2xxi1mgqa-Qq7rSGCaKFHlegePAyUY0xhMHM-QsFD-BqDAvR1EfVevsalkofOjCXh79fmV4Fm3-V1vhEovXP3InT2peeUsoECNBZTfAtctYWmsWGw34GTl745GWxELXfN_VI_qV225ksne48A9rHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458316cecf.mp4?token=nAwmeLqFSwIoxcgHKn3pP0m9RFgT77aRs5a_H1DQ0-iwPrCWfM8_QPlQ8i8oie4jt5UtkN2SuFhCnEIkI4UN2m2uQWdAzvHOXcMLGacFjukrvfQY8lRH25DsZrudB4gN9WUoUkCwS-VYVK1eScvtZ96aQATrmqGy9eApA2NRui2p0Gd0MNF8T5zvK_tQVK7kU2xxi1mgqa-Qq7rSGCaKFHlegePAyUY0xhMHM-QsFD-BqDAvR1EfVevsalkofOjCXh79fmV4Fm3-V1vhEovXP3InT2peeUsoECNBZTfAtctYWmsWGw34GTl745GWxELXfN_VI_qV225ksne48A9rHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارخانه‌ی شکلات سازی/عجب جای شاهکاریه
🍬
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/672183" target="_blank">📅 17:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672182">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e468509e2a.mp4?token=iIDAXW07s39X6MBXIhyVSidbtivIb9fQi6W5EuF9t88bZM3qm-6sUbYR-G3in641dS5gbmK8Ck3e0LZM_y-iUiHJ3hdp8O3VRsMFqdDNlX4H8MsbyqGCpRC3xZEE_P9CnEW-ksqhzpuwAinYl8VaQp9FEHl1_vsKeb1o76BRnEYbw_hXa4WhCbDMJ5CsWNU6dzkLGEPXyApjgkmyyRYwplDKIxd77tOMJqvwhaOSv_fmpt6WoVwf6wW81E7Adk2qU9gEqW6P8KcL33Z1PN_deXLx-o4ix1dLoiD7tcFVVJeNl_eG2_K6gd-O43DCRGuUH2XJ3Dhwvn2uZF78HsUJlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e468509e2a.mp4?token=iIDAXW07s39X6MBXIhyVSidbtivIb9fQi6W5EuF9t88bZM3qm-6sUbYR-G3in641dS5gbmK8Ck3e0LZM_y-iUiHJ3hdp8O3VRsMFqdDNlX4H8MsbyqGCpRC3xZEE_P9CnEW-ksqhzpuwAinYl8VaQp9FEHl1_vsKeb1o76BRnEYbw_hXa4WhCbDMJ5CsWNU6dzkLGEPXyApjgkmyyRYwplDKIxd77tOMJqvwhaOSv_fmpt6WoVwf6wW81E7Adk2qU9gEqW6P8KcL33Z1PN_deXLx-o4ix1dLoiD7tcFVVJeNl_eG2_K6gd-O43DCRGuUH2XJ3Dhwvn2uZF78HsUJlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه پایگاه العدید قطر؛ جنگنده‌های آمریکا به اسرائیل و عربستان منتقل شدند
🔹
تصاویر ماهواره‌ای از خروج ده‌ها فروند جنگنده و سوخت‌رسان آمریکایی از بزرگ‌ترین پایگاه هوایی آمریکا در قطر حکایت دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/672182" target="_blank">📅 17:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672181">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
روسیه: تبعات اقدام علیه ایران تا دریای سرخ کشیده خواهد شد.
🔹
منابع لبنانی از بمب‌گذاری و انفجار دو ساختمان در شهرک کفرتبنیت واقع در جنوب لبنان خبر دادند.
🔹
دستگیری ۳ تروریست خطرناک در ۳ شهر عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/672181" target="_blank">📅 17:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672172">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqqi0FmGnsInNNxSrpHjM45oZuwwY3AFxizYMXFFb0ZxLuQ4oqSsUxzEWCd5nHgLiutNKry_4Orxf4K-JaE-TjLNfScaUJR9NWhQ5hWfIWPE5GiiMcTtvM3tkMn_BWYkZHAjcGTzl3Nnmau8uNHXT7pvxRK-eS0Y18rE21SAEX_ZfoxVCO82tObneIhchZsR-Dbr98IlZpDhMCig1hmUPUi7L-Dvu3qFL0ajLqsQzssPFGjRFtWaiZjuty7QloJMekXKau1z4JVoFREXIzKxADraoZH6sPoVkqrS2TmFPWlcW_snU7QY7MFdNqas7m6-9HEFmd3HvAFL9t5D4feUVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H59_WhzC7jR-UjR3SI-gZLfamE54Jx_7FIIHZMoPffIenqBZJL75w_6Qrd5znYrvLE1x7HwYt-Qoi-E_4IPDKNINIlCYKUP_3J11S_0WbJBx4r-gN7fFIMOdhaXPyfD6vdh7L47MeEQGW-xizpfOGwM_uBiKGOATSebswbcwoK0evGGKcXou_t1I7OfRg2lBlLf56FtmMi9z2Mq9RalyvGj6ZQZ0VPpuv-xW1ckiMvHzXjTQx2lYKY4q76ZGodOmRPGEph9rs2jEgQAROZ7VHMM7pnYryDCI4bC0gp4v-Kv7iPDVB_-_6LMoHBsHnpAVecvcwjIrhHVtD4ib-ezzRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTO8W3EBkGpSE4YeVymfXIxMAjK7JSpzgPD4QdPyyB_sK5wNG25JZ_xd0JEmQEtQ5xCgKzuf8v_sTGJYP648O3mJndWO8jvYcj4-UPiG-PaW-m9woWucBtX2HSFnwm6E-xb9jKsr0nb2vIQr8KzSrD1J6RPORcTgqXGnV-_y7te5xHcqM9Exgzep6c7hAR7eO1_wu503gsD7XdDBohFbS8EIg-t0M1lvxAyYWZO2HkiN8ty2wS_uGIpNQj3ucKB5j1nNj-GeXrwEjByEFOWlcb7lGpZSQCqJN-0Ai4EEv-scYKPI40Rx_jOinNnk8PZaTnAbu_H7e5KmfkEnJooXkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jILjTZLnjdTmO6WmarGHDLB_FL4vMsw3d5wRZ24Hnh-4gJVB1nZE7e1Hl_L0mCI85Q89LekJ2CSGirACcPw_US2qAp6IUpjO7knjnFd7PMML_8--JvmgirhIZTUcBY5g7Ifp5-irpoUZBpZyxU3SyyoA2BagADk2fA9qtqe8-NPoZcCWOWShRnzngwuB-hsRlvaT6lPx1ophZ50PBpczPj3StCocOKLSE8_ObR4CfBYCXi9bLx3e0hy0zvDdJwVpAo7-l52Qi1eTk2xlK-ccnBjLsvqa980COFqDoXh_gXWDIiB3ij4-AkJcEfB21RJ1FVaf2gjWx2hf4Vtj0BNpLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ev2FrqrLMKbzMmhNTG7ITUjBpd2yLyhLmDOefoJedPwTR06czemW9hpDRknidISo19BBzKdUHIr9KkI4SyODRy94gVc3ZAikA0ERgnFcEuDmN56cK25N5TDnU5BC_wSYUzQa50gCYMuAgdMxj1QHpQrnDBf_A2nLQuNBtC6IL77onjuGRccTzCPd53lNnu28XsJ0esx6lJyI9t44x6nNn5vPWpRWZxORIu81Thh-19KAzPDh3cnB14xtAEUI3pKNYtmxcmp29aIgqJkEGDzFu9TV4U9O22RByHkvDv0PpDctYjmyCZlTiCilZHew6AAEecfzNn5fsIAyhwXWYlo_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ae6uMQm_VaqLK1H1iwKj9dYgfzKy2viK1kzdGiGKXsTCEalwAbofBFo2ocFxZG-RYBkXHOfZG_rzuhRSGm6LgMfM9XLUZ7vxqGKk4quBdNups7ISCnoYBQCqwJtMOkz1K1VMNxeKiBezknu52nzd0Z5deFXJtL1Zi3-ezlAuYr4_EbzXWfRY9vKf_7YYNIYjQOtyU38rGgqT9m47zVi63yovf3XhUkWnYPJDUe6I2BB1I7UyohFUweoE_2KjRlixxdlS4LjUYtfdMezHZAYKmn87-fjIMAdGHuBKj1GBfpprBPRUR--Nf4a6aH30X9nOZckNCVvglKoLL9htLUpoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u09AkJM2tiRFdVXGO_yzHz4KSHf1TsPDY5Hnfj9h3Ui5eVpWgC4_AvnPBblq7PQvEI1jd9oTQmA_2BG2S1AiMZxrxtD8tEa974az3whyObd-kCCnyPSr-8q_PD61IxoCLCAl9DAQNVlf27B4xWBPaRYtpW17UOZEjqPf6bb9Mkx4TUpU0IarlcR5wOpeMRA7N5LBdr9w1rsveizJVkLi3LzihF6zttycp5qjQqY0ARDzVUxCQzeQDpysChQ0Sq1NaIXBeOHwheueWN7tQg_pyTkOpIfEuJgD55ICeDbTvi1-_6-xzKB0za1X5Q3ioWWY6QrXAM6wxe4zY6PAwIksPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WM5f57qCRtIaVQjsGe1mi31xdmwoJ2HTCiFZi1QPPGplD4l81I77vCI2_FVARBPPHbJHt4CnRmHsDY7UyiFbd87Xh6tQcgcWkMMpA9Kny65IhM92tir9yMCM9-QhiTZFlZEB3Yobc61t2UIgU4pJ7P__o-kiDopZN3vXx8GL1GVWIM5SdPYxX_mrq9j2k1mpvkKo8ZZ__3r_ZKuYnGBS3-wmPL2XJst9ThL0-o7psJAyLwWAMPyNBJ1bM3xZEuo-15Mj8_yum-I828GORUyGHMOKDIBoDkXjz9PoKlDwti785gWDEU91O4jU1iQlgj5Bp7sPH--6wlRpo_sZwiuQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLXY-cGfZ233NGnpbXNNIOGX7lcJkqmeO6v4KxhA7ECrVqTdhe7W-VE2N5tNArsW7Cy7695vSR-zOmFz1Pjv1XthneKIWFEeShLIVOgbSmdidOPSAlJf8n7lHXoIAKd6aN-YupJ2KRB0PNsYd2IMhGNoU_jVn44zYGERuJCfqL4PoYG1Q7L0rNCkiG7FTWtsvZc8dTgHXPY80cmMEtbum_5vWPsEMq2x3HskXMPd25_bDCStygkoByjvadFXd7f1jh2rM7xpvF2O1olrJdx4eb9x3KNE1pFPT3qaCDisB4HBmwAmoTdfPkSdWFRw9kJK9h5wPfGz3-gMk8imasl6nA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هوایی از جنایت آمریکا‌ در حمله به پل‌های بندرخمیر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/672172" target="_blank">📅 17:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672171">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETniqasXkCe4wZa3EOG1CF_v3tVn60KwzX5BbSNtlbYBaWM8H9EeaSYrVJ4QetA9MrCemeiZSTo_RfyWnlts3GsF46gcDslUU9hZ7_ECwfln3xSyZHQG0Nx1v-zyxrRfV2CLnKrxBBcWLO5SYGVco2enPBQwZBfl0u1yHdBJVSejJcfYEiP780hAbBz9ntQgtKF-K5JoN0a55YxUuG2k5lSgPegEEszAH_03lg2X8o9Kq4_uJKdMkRGeE-xbKmY3TBk9MGi5Gz3LQ3_V3K7P4b5yrAEg2hVPOH0rCVzRsot49nUQV4j51P5cTLASd9qqa8Bg8K0UoSo2VQIW-LzvNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/672171" target="_blank">📅 17:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672170">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
حمله به یک نفتکش در دریای سیاه
شرکت CPC:
🔹
نفتکش اجاره‌ای «نوردیک زنیت» (Nordic Zenith) هنگام نزدیک شدن به پایانه CPC در دریای سیاه مورد از حمله قرار گرفت/ شفقنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/672170" target="_blank">📅 17:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672168">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
برخورد پلیس فتا با کانال‌های مدعی فروش سوالات امتحانات نهایی
رئیس پلیس فتا:
🔹
کانال‌ها و وبگاه‌های اینترنتی رصد و با گردانندگان این قبیل صفحات، بدون هیچگونه اغماضی برخورد می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/672168" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672167">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIgq7ROBc1n9jbDEEE1s9yGfrCw3mML3K93BKrcMvrNnD27DulUC5PfZrwRov650QXNhAARcgIe7rmeSDUddHk-g79RtKUSlOmFf9d9291POyHMhVpxSqyKjODNLnpRzEvEgyTg7VrF2q_GWWgFK_cysqaTKOxKEcTYZD1mwpk5u0SrNy9O4_99tQpn_mEs_UfcJ1q4caQTklpF3CqcmBe-_0L-rHh-T3vkve-QNIAqdQVqkMqMkThy2sSrmp5OD6rB9P4fZoyGArfHvc_y2hlnesFkq8DDtlwUn_4-mKr7IIEVNQD8NtAC_X4oaeT9y0vd4jHcyPYunNC_Tgmk6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانه تامین کالری در کشورها چقدر است؟
🔸
این شاخص، کالریِ در دسترس برای هر نفر در روز را نشان می‌دهد؛ نه لزوماً کالری‌ای که افراد واقعاً مصرف می‌کنند.
🔸
میانگین جهانی کالری تأمین‌شده ۳,۰۵۶ کیلوکالری است؛ آمریکا با ۳,۹۴۷ در صدر و یمن با ۱,۸۸۱ در انتهای این فهرست قرار دارند.
🔸
ایران با ۲,۸۷۵ کیلوکالری و رتبه ۱۰۷ جهان، کمی پایین‌تر از میانگین جهانی و بالاتر از کشورهایی همچون تایلند، هنگ کنگ و اوکراین قرار دارد.
@amarfact</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/672167" target="_blank">📅 16:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672166">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6b4167e81.mp4?token=rWQi4b0Qy0wcSgotzoHmnuWpT_LSXzfd1HIeRZLCveiEUBNvElwcTq_yW8ryadVzbRrNY_eOwyQImVAJhNEtT84pW8BqukVjzuzPSCJXsxXo1Gqu73a2OIuC__yjaIkQhKSCGpHBiKzoTzSYbQjfDgjOYwoeW7Gy6-5H2ffSDJMXwjQARrcjIWLGmv5kWLLkdT3uMAE3wFrxukdk-bt7vLINkA-QWZ9Rj1bhqz8DaatH-xp6YzhpQexk0xKHmQhV699lb_lIUoozEt1pxWf3T__uKl4Qxdn1QZ6bKQlQvuongNtcrtGEU7PhHfz_uLPKzfdZatZ8CD1AxdeeOlBFPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6b4167e81.mp4?token=rWQi4b0Qy0wcSgotzoHmnuWpT_LSXzfd1HIeRZLCveiEUBNvElwcTq_yW8ryadVzbRrNY_eOwyQImVAJhNEtT84pW8BqukVjzuzPSCJXsxXo1Gqu73a2OIuC__yjaIkQhKSCGpHBiKzoTzSYbQjfDgjOYwoeW7Gy6-5H2ffSDJMXwjQARrcjIWLGmv5kWLLkdT3uMAE3wFrxukdk-bt7vLINkA-QWZ9Rj1bhqz8DaatH-xp6YzhpQexk0xKHmQhV699lb_lIUoozEt1pxWf3T__uKl4Qxdn1QZ6bKQlQvuongNtcrtGEU7PhHfz_uLPKzfdZatZ8CD1AxdeeOlBFPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در عملیات ۱۱ تا ۱۵ نصر ۲ و مراحل ۱۱ و ۱۲ عملیات صاعقه چه مناطقی مورد هدف قرار گرفت؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/672166" target="_blank">📅 16:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672165">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyjTrPIwsyABCo0lzddCUjE9WSoJkTE8uOL8yuIP0Qb_DKl5SDMB5S1NGehSRjHdWSIOd0pwWXqALPK-F2PrsuwsNC94WM58vUg_agZJzHqTbbj-Y_fbypY8XpwYtCgrrfLIpGE0uxAGPn1rIl28ke7LkGR-CxLelGhTP906u1E-OeKIikuXxY9-m1AMAloKhQVZljnQqzvHR-Jr7Qa4uE9VznubdJYXdxomsjCSpEugoh3JdEknwEjSgt1MRQdEyWQWEYps1Ic9C-YF7tIRGFruz0QTFNmLPxVY71V_yb8GTEvs10kfWb9uF-dushFIsYnNEB7VhRhVTDWQ45I8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش رحمان عموزاد قهرمان کشتی جهان به تجاوز وحشیانه آمریکا به شهرهای جنوبی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/672165" target="_blank">📅 16:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672164">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
وقوع انفجارهای مجدد در اربیل
🔹
گزارشها از وقوع انفجارهای مجدد در اربیل در شمال عراق حکایت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/672164" target="_blank">📅 16:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672163">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
راه‌آهن مسیر جدید سفرها به بندرعباس را اعلام کرد
راه‌آهن جمهوری اسلامی ایران:
🔹
در پی حمله بامداد امروز به سه نقطه ریلی در محور بندرعباس، قطارهای مسافری تا ایستگاه فین تردد می‌کنند و جابه‌جایی مسافران در مسیر فین تا بندرعباس تا زمان بازسازی کامل خط، به‌صورت ترکیبی با قطار و اتوبوس انجام می‌شود.
🇮🇷
✊
@AkhbareFori
​</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/672163" target="_blank">📅 16:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672162">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a02bc8676.mp4?token=BavI1kvASiOCIYVLoF5q_KETcGLofcfkxF9SX1pMqWPHZCUwNds1pMjxvYXcNJk2PlsTd3NNyk0Ti58qz9rQ5w4J76kGFP20ySmpChhGw8Bm4RDbaP5QQ7yDJqvLfF0BDWH0hRdtzCvtp7jgQIDmq7sTwYbA8I10FCuOke8CeFiPtbzMzBADw-7IVGenwr_Gvdd5IHSjqQwzgJML5frlABBqXlmXjRy3pc83LoPqWKbMh10orJK-5kg0gG5EhfZjhsFV4pviHHXAtRztG25f2BL0vg61ga6Jc7fR3BOnqaJo9MhTtLnt-Qhq-KUidBmxSP55R8KXnMBlfZQcVXmHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a02bc8676.mp4?token=BavI1kvASiOCIYVLoF5q_KETcGLofcfkxF9SX1pMqWPHZCUwNds1pMjxvYXcNJk2PlsTd3NNyk0Ti58qz9rQ5w4J76kGFP20ySmpChhGw8Bm4RDbaP5QQ7yDJqvLfF0BDWH0hRdtzCvtp7jgQIDmq7sTwYbA8I10FCuOke8CeFiPtbzMzBADw-7IVGenwr_Gvdd5IHSjqQwzgJML5frlABBqXlmXjRy3pc83LoPqWKbMh10orJK-5kg0gG5EhfZjhsFV4pviHHXAtRztG25f2BL0vg61ga6Jc7fR3BOnqaJo9MhTtLnt-Qhq-KUidBmxSP55R8KXnMBlfZQcVXmHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
احتمال به تعویق افتادن فینال جام جهانی به دلیل آتش‌سوزی‌های جنگلی در کانادا
🔹
دود غلیظ ناشی از آتش‌سوزی‌های جنگلی در کانادا، ایالات متحده را نیز فرا گرفته است.
🔹
به گزارش خبرگزاری Ole، احتمال به تعویق افتادن فینال جام جهانی در حال حاضر کم است، اما فیفا این سناریو را منتفی نمی‌داند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/672162" target="_blank">📅 16:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672161">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بسیاری از افراد شناخت مستقیمی از رهبر جدید انقلاب ندارند/ برخی نمایندگان تلاش می‌کنند برای شورای نگهبان خودی نشان بدهند
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
شناخت مستقیمی از آیت‌الله سیدمجتبی خامنه‌ای ندارم؛ نه ملاقات حضوری با ایشان داشته‌ام و نه ارتباط تلفنی.
🔹
برخی نمایندگان به فکر دوره بعدی خودشان هستند. برخی افراد در مجلس به من حمله کردند و قصد پاره کردن نطق مرا داشتند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/672161" target="_blank">📅 16:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672160">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
انگلیس پس از پنج دهه موشک بالستیک می‌سازد
🔹
یک رسانه غربی گزارش داد که انگلیس در اقدامی جدید برای تقویت توان نظامی اوکراین، برنامه ساخت نخستین موشک بالستیک خود در بیش از پنج دهه اخیر را کلید زده و متعهد شده محموله این موشک‌ها را تا سال ۲۰۲۷ در اختیار کی‌یف قرار دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/672160" target="_blank">📅 16:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672159">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLGN7T8HzYyHfAgzjoUbjP0qcrTty4di8uGAL72OEvPE4CVnQGo3pP5dsOHWd7b5-a2VJU5tdzolGC0J3CpkMb6wqIxYOJN-oFm9-LIatyGSBlsmdbD7a-dNqSL9lADoZ4mYuYcNKd2W32TX5A05Jv3_o71y9T9677-9QLgXuGsTiHVNzlDThGq5Zac98LcIg6voOQuGY4BWX3L-aJRfcjqWkIXB9Q0KU1PORVoUmg0uFTpQ-udVNA-8vjVu-2fjfJrDluBYCtc_L7VnG8PdNOzUxSeTOV2FWfYqSDSNqKJrdhf8FfnJwmlS6fLR3c6N9Iyvm1UIQWk927v3duu2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با پیروزی ژاپن برابر بلژیک؛
بقای ایران در لیگ ملت‌های والیبال
🔹
پیروزی قاطع ژاپن برابر بلژیک، خیال تیم ملی والیبال ایران را از بابت حضور در فصل آینده لیگ ملت‌ها راحت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/672159" target="_blank">📅 16:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672157">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpnVdyHkbYAWUZ62EEr6DVbuw2oYjKClCHoNyPxevruBPZLcPexnNlmmwRYUciytfAxSjPYOwMST51-LEJnV7Rur10DmA6uHA8pokgxYIbJEk9bto8LZE4eTQkNDsn97HlC3txTqvfuW7K3npEi3Y_ACkMqgVmjXjQB-CgfIDGZCtNm4rBzpxEyaPiMgAVW8toIIdLB7s1pFE73LxulHgZ5XK50A0hefoqaSMvl0UTbc1nskg9fFwyxBP20MDNwBemkbv0tSmODAIFHJRlg2ImdVT45pCSxaAr03TS5sfEizr9_5uTR1quuepBnG8Rgg_qtUhG6ftiFZ1bvArTT3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e0ee339a.mp4?token=gU2_FjRRoFm_I88LnkOxbIRr2Gr1WbybW7R3plkkybJaUlzUPquyTb7DPCoFgb090ChcqLprA9Q_oApAA_aaCT0vKBToS0Tv7wWlgzYBlQum3RvnVq440LrN_3Ph5WvlJuKNfiFn5vncL-goPp8swZIJk4loIf-IC7PwNJIHREYlbt2K4jL8MQdB8R2fxVE_xF-D3aG52TEopKhdzZ1XzCabjjZTXuF-Y5AzPbnqdI6mcvrqoflOzCSprPf1KU6trlzOmpVkkUfiQwUgiNyWpCgaZ4keDCGM6XgyDh2S_w1SgUxzC-sFcZWxC9CrKmuC4oIhJ7kZiGAOsoFeZc_uBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e0ee339a.mp4?token=gU2_FjRRoFm_I88LnkOxbIRr2Gr1WbybW7R3plkkybJaUlzUPquyTb7DPCoFgb090ChcqLprA9Q_oApAA_aaCT0vKBToS0Tv7wWlgzYBlQum3RvnVq440LrN_3Ph5WvlJuKNfiFn5vncL-goPp8swZIJk4loIf-IC7PwNJIHREYlbt2K4jL8MQdB8R2fxVE_xF-D3aG52TEopKhdzZ1XzCabjjZTXuF-Y5AzPbnqdI6mcvrqoflOzCSprPf1KU6trlzOmpVkkUfiQwUgiNyWpCgaZ4keDCGM6XgyDh2S_w1SgUxzC-sFcZWxC9CrKmuC4oIhJ7kZiGAOsoFeZc_uBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام یک انبار لجستیکی آمریکا در کویت پس از اصابت پهپادهای ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/672157" target="_blank">📅 16:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672156">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3V79j-lon73oNDaFz94Urgd-oVMV2ffkA166x0XEF1rZV9MjAfes_wgBz5LenMOHFEvqNV5_x6KvkoqizfpPAustwI1O2RzdKozVRQZxC5g3dcuaXdywMF04ICePuDZlen9e-yj54QFPxTHFr1zLWxZqOeDq6LqD_B1UGkQdnq_RyMUNkTlC7--4ned8Pu4MoVsP7wLFY5tfstlBlExCesHhWDYiF1npgWzqSQtCDpzVMzUWw31zu0R4IIoYeg6kv6bxQmI5zrrmf08gDtY6G9g8fcUs-jB2KZMsY4u3pbQFra2oqOdj82SsjUFJuXCXtgEC351cvG2SgJ_Z7zbtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابی جدید از مزار نورانی «رهبر آزادیخواهان جهان» در رواق دارالذکر حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/672156" target="_blank">📅 16:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672153">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-text">🔹️
ویل لكل همزة لمزة
💥
نباید به یکدیگر برچسب بزنیم.
نیروی انقلابی نباید اهل «هَمْز و لَمْز» باشد.
🔰
آیت‌الله میرباقری:
1⃣
دشمن با اخبار یک‌سویه و گزارش‌های ساعت‌به‌ساعت، می‌خواهد دلهره ایجاد کند و پیروزی ملت ایران را وارونه جلوه دهد.
دشمن جنگ رسانه‌ای راه انداخته تا میان ما دعوا بیندازد. دشمن خبرسازی می‌کند و نتیجه این می‌شود که ما شروع به محکوم کردن یکدیگر می‌کنیم.
2⃣
علاوه بر این، همز و لمزهایی در کلام وجود دارد که قابل‌گفتن نیست. کجا خدا به ما اجازه داده که با هم این‌گونه برخورد کنیم؟! «سابقون» نباید اهل همز و لمز باشند؛ وظیفۀ آن‌ها این است که دستِ کسانی که پشت‌سرشان هستند را بگیرند، آن‌ها را آماده کنند و به جلو بیاورند؛ این مسیر باید مسیرِ «راه بردن» و یک مسیر تربیتی باشد.
از هر کسی باید مطابق با توان و جایگاهش انتظار داشت. ما نمی‌توانیم همه را وادار کنیم که دقیقاً با گام‌های ما حرکت کنند. «مدارا» یعنی همین؛ یعنی جبهۀ مؤمنین درجات مختلفی دارند و با هم مدارا کنند.
3⃣
وقتی ما با این حرف‌ها با هم درگیر می‌شویم، مشخص است که آن ۳۰ درصدی که به سرمایه اجتماعی ما اضافه شده بود برمی‌گردند و می‌گویند: «بگذارید این دعواهای غیرمنطقی را ادامه دهند». و دیگر در کنار ما نمی‌ایستند.
ما درست در آستانۀ یک پیروزی نشسته‌ایم، اما باز هم معلوم نیست چرا این‌گونه با هم حرف می‌زنیم.
☑️
@mirbaqeri_ir</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/672153" target="_blank">📅 16:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672152">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2871b47955.mp4?token=bmdpk7GveZ0YErrnEmE-5t-881JZnSB0SyVycli4tFjTIodSlSlW9sFNx3uThO73k-f6lMeRVIBZKJZeFis1O92SBmemVouLnU2HlA9y5Rt7t0FPb8S1sQz1SGopGeSTw-Agarlu9BXtapC1W7LKzJMObbxuoFrWYMwFop-Inw0fHf28XD9vXQebncgNj2YmS2A2Rv1tQsqukHrV9ZmyM8VxslA20gGixv91nKNmqqutc0hsgnFPnbc_U1iPcJkfsOHog5l9c4kf4FwYEjIHbqVqS3ttbY9MPX3KWLf3ieLx8D8NGe6oFcOMay6zfv_u4kN49YYt2mRXboPmmS8X9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2871b47955.mp4?token=bmdpk7GveZ0YErrnEmE-5t-881JZnSB0SyVycli4tFjTIodSlSlW9sFNx3uThO73k-f6lMeRVIBZKJZeFis1O92SBmemVouLnU2HlA9y5Rt7t0FPb8S1sQz1SGopGeSTw-Agarlu9BXtapC1W7LKzJMObbxuoFrWYMwFop-Inw0fHf28XD9vXQebncgNj2YmS2A2Rv1tQsqukHrV9ZmyM8VxslA20gGixv91nKNmqqutc0hsgnFPnbc_U1iPcJkfsOHog5l9c4kf4FwYEjIHbqVqS3ttbY9MPX3KWLf3ieLx8D8NGe6oFcOMay6zfv_u4kN49YYt2mRXboPmmS8X9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاقانه‌ترین چیزی که امروز می‌بینی: لیوانی که با عرق کردن بهت لبخند می‌زنه
:)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/672152" target="_blank">📅 16:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672151">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e876bc17ee.mp4?token=ehr4_nLfaKC_NX4DYgv46v1Ne1tSm54h4-ahOlxcIgg1js9ob8pjvfMAaiG00xE1hJPfrWML2biqofWyfHoS88KVioSBDCxv0tgh_vrq51B8jbTSsNJNngGFng8joNL4rDgebzQ9g0KVgMLp74JetbuD9eNSXFmMfO9aCyQapgYHzlSmcp3U8jNc-75o3xnytlqTbQFsu79NsamP1eqERL5djOufkO3Gmxu14FRWYhrJkYpsKBtCS4KOLUU0GDom3op-oamGA4xYfx97QDtY4k8n_16ArtZpzt4EgGrba4k7DCuCYMSHKl-3kvkRYd0XJSfm4VEZPZFv911v0AD0VgyZ8LnKzGpraqUSVquVjwmA9yBhRkctMWwL9BqpHUaYN5StMyGlNUmoShZQdYCFPzJ76-FYNG21Dh4pJFV0Rqh4afTDdchnfphr91TRp0PK0IGMv0KwRhLuRjQIzICZWTuLllbnjBnhiaJgxcboarJTbUhqPUUFnC26voB-WmSbrKNicPdAJkYMxUrEkywTgupz6FwwBKgl8b1eWI9YaCmXrpDBVL4UqKL1Wm6jPrNQhmBoNYZztTe6TkjArVwPnzfihqrf3ptA7urktRmiYpgKUgGT4vfduwtXG6j-QF3nCXA09-Az_L4yoWPiA1kWSB6GBA7gcm4Fi6XOk8aePOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e876bc17ee.mp4?token=ehr4_nLfaKC_NX4DYgv46v1Ne1tSm54h4-ahOlxcIgg1js9ob8pjvfMAaiG00xE1hJPfrWML2biqofWyfHoS88KVioSBDCxv0tgh_vrq51B8jbTSsNJNngGFng8joNL4rDgebzQ9g0KVgMLp74JetbuD9eNSXFmMfO9aCyQapgYHzlSmcp3U8jNc-75o3xnytlqTbQFsu79NsamP1eqERL5djOufkO3Gmxu14FRWYhrJkYpsKBtCS4KOLUU0GDom3op-oamGA4xYfx97QDtY4k8n_16ArtZpzt4EgGrba4k7DCuCYMSHKl-3kvkRYd0XJSfm4VEZPZFv911v0AD0VgyZ8LnKzGpraqUSVquVjwmA9yBhRkctMWwL9BqpHUaYN5StMyGlNUmoShZQdYCFPzJ76-FYNG21Dh4pJFV0Rqh4afTDdchnfphr91TRp0PK0IGMv0KwRhLuRjQIzICZWTuLllbnjBnhiaJgxcboarJTbUhqPUUFnC26voB-WmSbrKNicPdAJkYMxUrEkywTgupz6FwwBKgl8b1eWI9YaCmXrpDBVL4UqKL1Wm6jPrNQhmBoNYZztTe6TkjArVwPnzfihqrf3ptA7urktRmiYpgKUgGT4vfduwtXG6j-QF3nCXA09-Az_L4yoWPiA1kWSB6GBA7gcm4Fi6XOk8aePOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسعود اسداللهی، کارشناس غرب آسیا: هدف ترامپ از امضای تفاهم‌نامه بازگشایی مجدد تنگه‌هرمز بود/ شخصی که تفاهم‌نامه را امضا کرد باید به این تفاهم و موارد آن شک می‌کرد، این تفاهم نبود سوءتفاهم بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/672151" target="_blank">📅 16:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672150">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDJOgUlSo6AwNpSxcCf0tTpCTkwY2cbIiP8RR8KGp19MIU3Td_GB9DCnbBbua3dX5-gINhs3C4CuVtXMDlOqo7dvQVQ1e21LCTBJvgM3KktdY9f8iko7f0FgA_eh8Ix25I4RMOprtJchvjulvStjllTBhae2Esux_PWSwL9mLvoOpLvfSp7W5Ti2uQ1zXZvfkzI2lv6PX0yGTR8S0UqnomeSrjVhhJBk2ZqbcfGmLdDuu_uGVQq17axxwu4VSb2cjuXVCfHYDY6HvFwiLf_ldZkIlvBkfQ3Xz8HP1Z3uICgyHUf3_RBYa0uGb9A697XVxiGaYjC2caQyfh9SemhwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدال طلای شناگر ایران در مسابقات رده‌های سنی آسیا
🔹
«محمدمهدی غلامی» ملی‌پوش جوان شنای ایران، در دوازدهمین دوره مسابقات شنای رده‌های سنی آسیا با ثبت زمان ۵۴.۵۱ ثانیه در فینال ماده ۱۰۰ متر پروانه، به مدال طلای این رقابت‌ها دست یافت و بر سکوی نخست آسیا ایستاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/672150" target="_blank">📅 16:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672149">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
اقدام خصمانه دولت بریتانیا علیه سپاه
🔹
دولت بریتانیا رسماً سپاه پاسداران ایران را به عنوان گروهی که تهدیدی برای امنیت ملی این کشور محسوب می‌شود، معرفی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/672149" target="_blank">📅 16:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672146">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bh3DblFetmAA6js5DrfG4X1c848q-7E8JjJ_rFpkZKd01970OtSW7gd4iIcxera65uBMKlu0n0iiQnwQbbNc9rx8BKQPYor-_ne-aZJr29W8Hj6565ESeuKhXnoxJf9CTsYimGHsSULxnmRnCZpoF7TQ_-9A2HqORHOEdwj6a2Iq8RcYgDJsHJSyxV9pL7u0mi9HsZx0ENfbEBpK0kB_eZHBOxzNsRn6FZ_Z8eSsSn8JRkN9846GMqmRU-xdSSBQ8kk6Jtzv7HdOze2fSbYDhDWlOuzuNdhkQmhs68ZXjvwwZJF-hD6m3bD8bFKj4ZrPHuljZrqDW6xV4tBpYMhCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaeGcT7L0UFSLfnvNM9kXQafY9GO8r2LKDJAi8FQPdzW4kXH1_ACZ-pe3nH6xjPDqC70RoRDuw2XvJ6lyATdXM4Hf6tKeUi3N3kxG7s9Gdxc1bu3ZPgZyRr8q8QT2ZGo_A698OeC9pxoFBSVe5Z5QfvBlEj55J8z80KHlEyOaAgO2p7qi0k4rFbiR3lrohVoeQUFdaz1rbTUlw4nbM18gEZeFaClO3JzGlbDv9drFg8Lzgd1iR9GkhjNmmFb0ofuJZaGrK1XT0fkrpc_rNz2xiK-phTq4GpvKyVMhmRaid1vPJQKpt9ZTjBjchVhv9HgIVsrZMVP-vQKofqWh_fVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdSej6mET_ilvwfl5CpmNJYEWs1_iX8z4OFL2gNXJxUMo00uD9WetohHOv78db48oOSu4l1uQHL0gQtmjy6Jc3uN5Wvxpo8M6S35yUpX4JXD6Z5wH1f5yZC66YPnjuhPtPCYrV5oWclnmEtB5F8REV8Z95kB9cb3yn9wF9dvsPjX44TvwBK1BCx4jDTauCiMI_upvg67JmhIsuTP_dkzHXDASa4QPNi2nBeqdznjy7b9sAxepeswpLdRwlS1l8b1gJ5RJ61s9pkRJ6w3bQAiCaCUuX2hs6S9n_moNUb0AX01D4TsbJsElbCcQnEqmo-YzFsm1vLF_BZ7Wqjs38vM2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
محصول جدید تسلا به بازار آمد: دوچرخه تعادلی ۲۲۵ دلاری برای کودکان
🔹
تسلا دوچرخه تعادلی ۲۲۵ دلاری برای کودکان ۲ تا ۵ ساله (بدون موتور و پدال) با فریم منیزیمی و صندلی تنظیم‌شونده عرضه کرد، اما قیمت آن بسیار بالاتر از رقباست (زیر ۱۰۰ دلار).
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/672146" target="_blank">📅 16:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672145">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: برخی مخالفت‌کنندگان با مذاکرات از روی اعتقادشان چنین نظری دارند/ ممکن است برخی از صحنه‌گردان‌ها اهداف سیاسی داشته باشند و بخواهند به رقیب سیاسی خودشان آسیب وارد کنند
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
استناد می‌کنند به برخی از سخنان رهبری مبنی بر اینکه مذاکره با آمریکا جز خسارت چیزی نیست، و این را به تمام شرایط تعمیم می‌دهند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/672145" target="_blank">📅 15:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672144">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
منابع عربی از وقوع انفجارهایی در سلیمانیه و اربیل در منطقۀ کردستان عراق خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/672144" target="_blank">📅 15:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672143">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr1K1jYN8UATFqLCLHFvq4tuDFZAVYzgMzjQ5ZzP82H3OeS4hBTIRRiIP7gZoGIRyU5ipd6Vow0qT1KgG5Q3F9u4EiKwTn9RPyZS5EA5nSUeDwcjvmjlo6WqRN8f3ruId1r-VJPVfER-tuSTJ6iGhbz6yaChA9Z7ZSyDSTlsbbVjOAj3xzsvyVENZJHE9VXWKspmRDdHPgRLBHR5BZw46bJmLJaMrofbo6PFLnhG4yvu27XiV7qq9vZP26yclIUXi16pj9gCjuQ2o5qMG8WZZhdwt8ZK7MKbSkJuNMSi2VcxApT5X6V6eiDCupr7oR2wZgJX_MMWBLuyA42wyzPAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده هوافضا: شلیک‌های موثر و هدفمند ما تا برگشتن آرامش ادامه خواهد داشت
سردار سید مجید موسوی:
🔹
در نظام محاسباتی ما خاک، خاک است، تهران تا جنوب یکپارچه برای ایران هستند. شلیک‌های موثر و هدفمند ما از سراسر ایران بر سر دشمن تا برگشتن آرامش به خط ساحلی جنوب و تنگه هرمز ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/672143" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672142">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osknJBMIlTmDHBanXoZFd3id5wnIV-t9SL9EYXHgmBrWCEiF-ChJKg1I2A93HHgGGS66B5bcanWEIhlLIGAxvwDrsWlkF7v6KMlM-5Qqt_oWb-UXJk3GFEZzcKn829wSreBbN7oFwy4vfXauBX6kxyANsBf1rxCqSh03PgjVy2B3Rmwc3Q1uqppnsuyBkoBaASxcDzYq4_aytDfDF4AnJLIL4_d7zrYuaUr28AjDzreckW2wnWnVlE2R217VKK8owLdFQ6qsn6GN2YwcjJ57Dqt1REXJ-GZA4B_bVbEzvPNtjcJrPpasIkc2empZ-dqLY3PQjjFJzS03IkLxRuKukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام پایگاه های آمریکا در منطقه مورد اصابت موشک های ایران قرار گرفته‌اند؟
🔹
اطلاعات موجود نشان می‌دهد که در شبانه روز گذشته پایگاه های آمریکایی در ۷ کشور منطقه مورد هدف حملات موشکی و پهپادی نیروهای مسلح کشورمان قرار گرفته اند و خسارات زیادی به آنها وارد گشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/672142" target="_blank">📅 15:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672141">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb1219524.mp4?token=i5xvlSV7gjBNlWxbBToNwFpSEw5jvCF1uw1fh4dwcBCKeg6d9sIbpGY9tMBO-VHkaU5vQnpr7mu9JIPWLrvtuxQvCrUA9fXLnKhEfOtxC9iMpLvUmFYzmgzHXX-oeRvQ39W0Cok3OXwv2fSz67BksVjpaDvnDQHNmJY4hRV6PlCLrdH8Z-hDkoCaAm_j_Xscg5nCrxlHmCxsUoCn88tB7cIk03f6PfM2HTpQgRbuMuxaEMnZQCcUpKdu7BeFYSHIDL4pvsoUnIH8TI36O9y8K-NuZMwxziGXvETuSfCiIyFneXYrMKgo6_mx4RE90GhARVOkYAzn4qpeA40KMQpmjQ3r5pI6GHdMG1uqNINUFLNOq8WIOQ5VMgz3MKp33V8ZC3IhkiXRL_APnyii6MKCNkS7VGRvqqBt4znhVvDmKRx5X_QqId4OTkzxJ7fLHUPhAjO6oOY0oX4_seLlGKCyHYjb-nWp6kOOk7pwW_MLcRUsJXuX4c6WujSUayVSENllDEhGzKDfy93ykN1vQ5lhu-cpGvLMtRPn6oSsYxDq9vy8_zQzDVnkkXv95mKOgnIaQjDpgtPkWR6Y9kUrVsrwY5lUzRUQ-vPQzczeRD-Jc3KSJXPZHATC5wkr34MVVKAJ6t34Hbz_F0xXnDLh7fGd0l3ZSlFxTmriMLylwmCigh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb1219524.mp4?token=i5xvlSV7gjBNlWxbBToNwFpSEw5jvCF1uw1fh4dwcBCKeg6d9sIbpGY9tMBO-VHkaU5vQnpr7mu9JIPWLrvtuxQvCrUA9fXLnKhEfOtxC9iMpLvUmFYzmgzHXX-oeRvQ39W0Cok3OXwv2fSz67BksVjpaDvnDQHNmJY4hRV6PlCLrdH8Z-hDkoCaAm_j_Xscg5nCrxlHmCxsUoCn88tB7cIk03f6PfM2HTpQgRbuMuxaEMnZQCcUpKdu7BeFYSHIDL4pvsoUnIH8TI36O9y8K-NuZMwxziGXvETuSfCiIyFneXYrMKgo6_mx4RE90GhARVOkYAzn4qpeA40KMQpmjQ3r5pI6GHdMG1uqNINUFLNOq8WIOQ5VMgz3MKp33V8ZC3IhkiXRL_APnyii6MKCNkS7VGRvqqBt4znhVvDmKRx5X_QqId4OTkzxJ7fLHUPhAjO6oOY0oX4_seLlGKCyHYjb-nWp6kOOk7pwW_MLcRUsJXuX4c6WujSUayVSENllDEhGzKDfy93ykN1vQ5lhu-cpGvLMtRPn6oSsYxDq9vy8_zQzDVnkkXv95mKOgnIaQjDpgtPkWR6Y9kUrVsrwY5lUzRUQ-vPQzczeRD-Jc3KSJXPZHATC5wkr34MVVKAJ6t34Hbz_F0xXnDLh7fGd0l3ZSlFxTmriMLylwmCigh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از استقبال گرم و پرشور مردم جنوب عراق از زائران پیاده ایرانی برای شرکت در مراسم اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/672141" target="_blank">📅 15:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672140">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
منابع عربی از وقوع انفجارهایی در سلیمانیه و اربیل در منطقۀ کردستان عراق خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/672140" target="_blank">📅 15:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672139">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دو برادر معلول در حمله دشمن به پل نیمه‌کارۀ بندر خمیر شهید شدند
🔹
استاندار خوزستان: بیماران سرطانی و تالاسمی هنگام حمله آمریکا در بیمارستان حضور داشتند.
🔹
سقوط پاراگلایدر در دماوند، سلمان عبدلی، خلبان و مسئول ورزش‌های هوایی سمنان درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/672139" target="_blank">📅 15:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672138">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb3be02fd.mp4?token=nt8d0X_wmzC04_VvTRFk3-spInx9JRXkWcmvfzXqNCpNTiKDpwjoyxu6DltI_e_GlHN9_g49DpQZqmhFhs0wbHbyM3xkWL2KWrP_Y3uiHzJxHdfHqTdoya79ltvx-hYANVKuLjERo1Q2N4llgnoCXAmIje1wVJ_w4kfa-HBfapRucgSVwiciyV5k9pGtFmqT8O0pTpmMuPK-GajsqObrln9bFhjSlL69FDpIRMiJv4t0NkdqbowZ7zHHKfoefczIvIvXSF6k2GI8zBTyfJKWJxlKHp5Z2VN3I6WJUIICdZGt27HQ_xjlXwwz9afasPNGK8yu_u3CuTBtbUVrAyui3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb3be02fd.mp4?token=nt8d0X_wmzC04_VvTRFk3-spInx9JRXkWcmvfzXqNCpNTiKDpwjoyxu6DltI_e_GlHN9_g49DpQZqmhFhs0wbHbyM3xkWL2KWrP_Y3uiHzJxHdfHqTdoya79ltvx-hYANVKuLjERo1Q2N4llgnoCXAmIje1wVJ_w4kfa-HBfapRucgSVwiciyV5k9pGtFmqT8O0pTpmMuPK-GajsqObrln9bFhjSlL69FDpIRMiJv4t0NkdqbowZ7zHHKfoefczIvIvXSF6k2GI8zBTyfJKWJxlKHp5Z2VN3I6WJUIICdZGt27HQ_xjlXwwz9afasPNGK8yu_u3CuTBtbUVrAyui3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منفجر کردن مسجدی در جنوب لبنان توسط ارتش رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/672138" target="_blank">📅 15:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672137">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a81372c62.mp4?token=hUpZCG8jpdmgQ0OWzm9uY4IJOQvQC-6SNl6fzBFAz5sqw9hbYcd_b4V7-QDOIKTjHU_tCk0ziFuw4Q-8LYEXODPm0H7zCjVLaNOBO3mLlD6bs9QzdRFqnRQ1deNIY1Qdoaau0h-LkqPohYqL9hr9aqVT6rAIrI8o8BSpjKS1N6zOfB0ly3dpHUiXEd3zp1aqFZFM6_YvD_uXohpMmxbKap-gB_ex34llO254vp2RwsoEcWKN3mek_crntYyhgn_d-4W-TaI9mOn5tdirEw7OlHTWy3S9pAq75b7mfjvioX4-P8ivartme85vTnoP3GjpRv1ohn9kBqi73M4j5r0Mew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a81372c62.mp4?token=hUpZCG8jpdmgQ0OWzm9uY4IJOQvQC-6SNl6fzBFAz5sqw9hbYcd_b4V7-QDOIKTjHU_tCk0ziFuw4Q-8LYEXODPm0H7zCjVLaNOBO3mLlD6bs9QzdRFqnRQ1deNIY1Qdoaau0h-LkqPohYqL9hr9aqVT6rAIrI8o8BSpjKS1N6zOfB0ly3dpHUiXEd3zp1aqFZFM6_YvD_uXohpMmxbKap-gB_ex34llO254vp2RwsoEcWKN3mek_crntYyhgn_d-4W-TaI9mOn5tdirEw7OlHTWy3S9pAq75b7mfjvioX4-P8ivartme85vTnoP3GjpRv1ohn9kBqi73M4j5r0Mew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاوی تصاویر دلخراش
♦️
موشک‌های جدید رژیم صهیونیستی پیکر قربانیان را غیرقابل شناسایی می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/672137" target="_blank">📅 15:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672136">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed2a9082f0.mp4?token=lQy7oe0TyeuQhWmywEyOBUqbkLWenwiKsctWUyVlubvvp4-Rci9n69caN_cFcr6v8eNf4lTPYVmomsQVA3wsF-8S2LnrwMob_jEc-0VQGxv4yeEuiVD1pwm6Wu-q5g93SRZqX6g4G8HXRSjrInAEiMGTtEfy9ZoGI4MPPdV4qUWMU_CAUxd6Q0TpgKuJOtHnThkWLNeJauNFEX6N6lpWKQCZdjMoAfamZucXGczXLsHHRhiEzBHzATUSbIRLXLHu0j2MWZkz0efud5FMz04rkqyfiTvGl9Ju32vGRak4qbRmYWjqQqP_44oz_LCOW_sXQYdu5qad7swCTqjGc9lmVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed2a9082f0.mp4?token=lQy7oe0TyeuQhWmywEyOBUqbkLWenwiKsctWUyVlubvvp4-Rci9n69caN_cFcr6v8eNf4lTPYVmomsQVA3wsF-8S2LnrwMob_jEc-0VQGxv4yeEuiVD1pwm6Wu-q5g93SRZqX6g4G8HXRSjrInAEiMGTtEfy9ZoGI4MPPdV4qUWMU_CAUxd6Q0TpgKuJOtHnThkWLNeJauNFEX6N6lpWKQCZdjMoAfamZucXGczXLsHHRhiEzBHzATUSbIRLXLHu0j2MWZkz0efud5FMz04rkqyfiTvGl9Ju32vGRak4qbRmYWjqQqP_44oz_LCOW_sXQYdu5qad7swCTqjGc9lmVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاضری برای وطنت اینو بپوشی؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/672136" target="_blank">📅 15:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672135">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
آرزو داشتیم به نجف برگردی اما نه اینگونه...
🔹
قاب‌هایی اشک‌آلود از بدرقه‌ی پیکر مطهر  مرجع تقلید شیعیان جهان، حضرت آیت‌الله العظمی شهید خامنه‎‌ای توسط مردم شهر نجف عراق.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/672135" target="_blank">📅 15:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672134">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ2Z82n7Fp6hmYlmXX_gbNKyUTV6nzDSIvtbhneawjGPTh9EMAUhXeik8GGopVKGF3mP2wXrN8TJtYubGZ6PLQCklNXuGeZMf3oZlFBj0UyjcNtLNEy47Nsf16xpotWYMvMYO4PDyv__qihF2T1gTUTqxo0Ie-z8X6smifBWWpkKvXlAtHZI9Knq5K1jpzp10ghOTw9PpJibccdjrrT2IxjQoSjBBQIjyKeROQoQtmUN_s1Zglqqtp8a4RTHJzsNY2EDuHz1gNPMv3cTi_kx91BH8jWaVT6JlO9w1DwUpJqFiBAbn0kP-RcX5e0ZhGBXRcjdvdAGDS-t-_XN51PVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست وزیر جدید انگلیس معرفی شد
🔹
اندی برنهام، شهردار پیشین منچستر بزرگ، با کسب حمایت گسترده نمایندگان، اتحادیه‌های کارگری و شاخه‌های حزب کارگر، به رهبری این حزب انتخاب شد و قرار است روز دوشنبه جایگزین کی‌یر استارمر در مقام نخست‌وزیر بریتانیا شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/672134" target="_blank">📅 15:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672133">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtzJ3KietRUyMrJXn9hs3rEZHdPE_fLZLIQRq57-PHjjG-efPAzjzbUsQvz4nEJjd9nRPWIjcmwG5E4vfKMVOABwgSvPhHRdf1bKlvoa_-RdGigOagfQGb8q4g515A-MjNDIm-zYaSIs6qAYh5_AEEkbhLkRE_fuWSZkq9yUwIRRUyNBTu1k9C-5bUbU9xq0LCzTkIin9lq_xANXBiOBDch-yKagFezbplZL0xp4yyjA7ywnudCXwH66BuiUIA22UxXkyoJqrupGZrGV9bO5ur4PRMWk9UFY9peUq5bcabTHV02KsF12k24IMiMm9_e1AicIHKedtQv7ZqC7ngBrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمیته وزیران امور شین‌بت تصویب کرد: سارا و بنیامین نتانیاهو تا پایان عمر نخست‌وزیر تحت حفاظت خواهند بود
🔹
وزیران همچنین با تمدید پنج‌ساله حفاظت امنیتی از دو فرزند این زوج، یائیر نتانیاهو و آونر نتانیاهو، موافقت کردند.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/672133" target="_blank">📅 15:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672132">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش علی مطهری به گزارش نیویورک تایمز در خصوص احمدی‌نژاد: احمدی‌نژاد دیگر در جامعه ایران طرفدار زیادی ندارد
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
آقای احمدی‌نژاد چندان پایگاه اجتماعی ندارد. عده محدودی طرفدار ایشان هستند.
🔹
اگر هم بحث آلترناتیو بودن احمدی‌نژاد (به ادعای نیویورک تایمز) مطرح بوده باشد، چنین تصمیمی درست نیست.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/672132" target="_blank">📅 15:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672131">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988241fe78.mp4?token=aXNsaGbg6zA8CsVwnjeKBoeFcOO9k3g4S1hC8Ous29NI1-xyUqVI2ahqWVAYshp43IGjfGzaVKTyjnE_EygzQJkYfmlPVFN4BxilTkeOmtp2ciNvLMeQ5qyUpXBMXXVMYwpQSJdCBVXcm1zTLRDvUYqIe7JobaXMxpkRsw1VJHAOoVIsV6NvHF30AGbeH26G4zsDWWxumCPyv8DPwLbbpzCJoQLuOCq7ZUTbEHxVVlccWFQdC3cR-G3yzjuaucr4JFRpnQsti_A92PBtD2qUt8vWiy4VuQ3f3XEV9R3WeHsBFeGk3w4FwFrJ9cJkb1ncMgpBOOoSuNc2pgjYGB7-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988241fe78.mp4?token=aXNsaGbg6zA8CsVwnjeKBoeFcOO9k3g4S1hC8Ous29NI1-xyUqVI2ahqWVAYshp43IGjfGzaVKTyjnE_EygzQJkYfmlPVFN4BxilTkeOmtp2ciNvLMeQ5qyUpXBMXXVMYwpQSJdCBVXcm1zTLRDvUYqIe7JobaXMxpkRsw1VJHAOoVIsV6NvHF30AGbeH26G4zsDWWxumCPyv8DPwLbbpzCJoQLuOCq7ZUTbEHxVVlccWFQdC3cR-G3yzjuaucr4JFRpnQsti_A92PBtD2qUt8vWiy4VuQ3f3XEV9R3WeHsBFeGk3w4FwFrJ9cJkb1ncMgpBOOoSuNc2pgjYGB7-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت‌هایی که‌ آمریکایی‌ها در هرمزگان انجام دادند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/672131" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672130">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95465ecf3a.mp4?token=IjtGll8iVxgrsS-XFd2Jr_8x38gEl6NgXzvHbxj4o8am5E3vxl1sdVFCb3jBYskomkq1JwaXph7jONWYGsYNuKAMHcnBfDLIt6wGyTQw0Mop1xj3GkVQOwpwguekdravTi4Dmd8_BU4AmNIRvIm0ZFCTe9Wnc7c9CzdxD4UIodLlVc7xCl1vMPnVCfDqxtHsGWEmpAsvF082z-7KoahWfmRceg2kkZmroTNBXTH1RgztWun76y-pqgstFj5A0TBGIQfdGTt-yiydSQrjFdvYltFaxHsxHKaXi0I0yNkJLmRgTfcrEMTbn3B7mEJ_KoZ6AbSbJQazJlZ6bwj6qGP4pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95465ecf3a.mp4?token=IjtGll8iVxgrsS-XFd2Jr_8x38gEl6NgXzvHbxj4o8am5E3vxl1sdVFCb3jBYskomkq1JwaXph7jONWYGsYNuKAMHcnBfDLIt6wGyTQw0Mop1xj3GkVQOwpwguekdravTi4Dmd8_BU4AmNIRvIm0ZFCTe9Wnc7c9CzdxD4UIodLlVc7xCl1vMPnVCfDqxtHsGWEmpAsvF082z-7KoahWfmRceg2kkZmroTNBXTH1RgztWun76y-pqgstFj5A0TBGIQfdGTt-yiydSQrjFdvYltFaxHsxHKaXi0I0yNkJLmRgTfcrEMTbn3B7mEJ_KoZ6AbSbJQazJlZ6bwj6qGP4pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپاد اسقاطی لوکاس امریکا، نسخه فیک شاهد ۱۳۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/672130" target="_blank">📅 14:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672129">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViP6-rTQ5dGK-3GfmHRjzALsywu-NFKnf1V2p7V55SewdFNy_G3WJMXl4iDSc6PxwGrhI85aYA2nSBdFTN7f7sjKWSPFyAAItpfOImQG2WVtKC9xcuFhwdZqovsAqA2tilQ6IqdqPNAT-ouUM6v5ziBCxhlPca1ars8L6skUCsvesjBcQM5Xc-Wteeh_QbXiMLWyvkUbv9t8h89GvnmpPJ9J44H-dSOMOc18ABkTsCwYITWOFHJSaNw3ZLnhXkaULjWNTED_kVc3ia7jNtaqp1xj27bgwx8mUAqXOEcj5swiAGCdDt6yLztcUVXl5vbpiA2OWm-6_38ZBw8p947ZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📍
پایگاه‌های آمریکایی‌ها در منطقه باید تعطیل شوند
🗒
ما با پانزده کشور همسایگی خاکی یا آبی داریم و همیشه مایل به ارتباط گرم و سازنده با همه‌ی آنان بوده‌ایم و هستیم، لکن دشمن پایگاه‌هایی در بعضی از این کشورها احداث کرده تا تسلّط خود بر منطقه را تأمین نماید... من توصیه میکنم هر چه زودتر آن پایگاه‌ها را تعطیل کنند
✍
بخشی از اولین پیام رهبر معظّم انقلاب | ۲۱/اسفند/۱۴۰۴
🖨
نسخه کیفیت اصلی
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/672129" target="_blank">📅 14:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672128">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-text">"نه به جنگ" گفتن ساکتان جنگ رمضان  در واقع جبهه گشایی برای تجاوزات اخیر دشمن است. اینها پیاده‌نظام رسانه‌ای دشمن‌اند. دندان‌هایشان باید خُرد شود تا به‌یاد بیاورند جنگ را دشمن شروع کرده و ما در حال دفاع و مقاومتیم.
@yaminpour</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/672128" target="_blank">📅 14:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672127">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9g4SAWFnAps8gnb3cDtBblKD1WZwq5985o7-DMmtAtuGn3dy07YjOY93o7ev2NtShoJ-t6rbIyyTZAtb8FHzvROtsWyIaTaX8lgIiUUthlvLYS_OGMJCSZ5lAQLukE9-uUSL24lypRdczbkqhhItWym8EsY8CdzdjLoGTrxZF_pRswSSPTKKjF-VRvCqPnRnVg3yKl_6HzAejTwUiWvEWoag4PAzwsnPE7KHM2S7iGjvWarX0p7C9Kvc5mBJZZ-g0Y-5SJz82W0qa2aTNZ3PX2fYWbcz0d7d6hqbpfCC5y7KkXwqnGlKXMqqwrhejgsaXSU_-nt8_vFbqw-xdKYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تصویری از کاپ قهرمانی جام جهانی ۲۰۲۶ در نیویورک
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/672127" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672126">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
قیمت بنزین همچنان در حال افزایش است
انجمن اتومبیل آمریکا:
🔹
قیمت بنزین همچنان در حال افزایش است و به دلیل وضعیت تنگه هرمز، قیمت هر گالن به ۴ دلار نزدیک شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672126" target="_blank">📅 14:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672116">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-yfiMkObJUnNrxUdteAvfIWw-CTI-Ege5SEimRI9jvYicGnL1onFapaRZFAKV1RkwwSY2lUYNeJhe6hfM0chTsedKeFBXAI_RI_hC2RPf3cPm9_xnVLduBocp_cuh8yIA8TIPiqqaJC5w6X2EHAsiNZyeYxYhXPzFkaEPoZzYyArQHZmCZswtCYHAhW2oLgqpUBG_-dng9WUBEMDi7zF7Yq0Y_OIzhpn7U5fWLQwU_TOK_8L5m7LJ6haJ-IeOMFnr8bWjYz6eqbUV27_HjFX77JorAeoFbEvWGcV6NfEupwKLKA0qs7DVVHa_O4G-FTb794Yru8RPB4yXS3E-2STw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPp83XGcE-6EYGQ3iSwguFxPVnkeBoNPU-sy1-H44qr6fWy_A5VdE--oz-6ZXG2HxZW2_mo3F7ciZP4OjK5B162U5aoUvWysC8ZYYaVVRIPv49I2wehRgzn8exGrI0DLuz8wqwsrpJSLm7rAUhYai---2XI4cwtFX98fpGJhJBUKnJAykf3UzrM85yJgm0PsLon3G3IEFkS2dSldPURE6X4BXEm2a_Sryb93q3sMTG9qfptoUqQWIaqzQveCxq9jOOSMv6RCTUhp-bIinydNxyhXtcO3EW1wPOzJwjJckrRwVMZreMQF7MRKCoeKsAoX2PtyINGP8pv1MzxOKJntUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESr2OF-5swkRSZcxjyAVlNz0ViBCbP41YP54WZ1KLT32kcaHUiccRpbEUglyzQqjzK2SciDYSShL5MydCaa5b1EliyDieUzFEmtBVfDnMFuhKVoQ0agl0mMei2RmfpNAz72_6g9ccnNZBkEV8Ccle67PRtDjWITd3O5gIXVO_7w4JCDPH1XTji1UwnsBiBn0A-_d1ZJHCmk35yFJda4xK9cczvbnhEbHjD4tbAT52fr2jpLHKnFo0T5ch7MWr6DBrKJ5Ys7KmGYRVvZSjks_JAAug3w26UG0KYROp-VzO7Z5Qq1VHH-qqfrk2aK29vsBrhXqzoSew72C207DyX0KlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1e_Jf3Xr-HlTSgHyAqs4OyT_c2jFjCfamO2NybM_eecQmubR2Nnh8b-Zse4tcfow_vOOgiaxeOL6qqLgj30_GFTxAM5ai7gXfh-D6EmGtUdb5tMtGAjDC5eMYAyZJHpTC5su9-JmbItNJuK2x47usVmC735IgUyhopfbEgyB4U-ZV_q6omd7Ia2AgkJ1TqzFGzxLOYSS7f5Hglq41BMWfD08XDF1GAhtWxRgfOP5IReF1WlQGcMPNVtZGmxr-yH0W-yhaNZH6CVhZ7fN_FESJeHpKMGRquq1PM1I41kfykq7TLGWJFhssRV8Vv_lXqNWaKUfCSmzz76wbRMvc1Ihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPBJfARUyfyTDWw8Wd4mF5qi9aez0HM_SYbhBJCgTmYYpA0BDT1Bgo-pX2jeZFO1mF2VI6Fl_rxEEkJXfAUQCe3RT4qTM3bZPp0Hbdv5n52cJFdOABhG2cp96JwZF0XarmDKnWnGY-2dBgc4yM6ER1vhQb5v2ud5UD2rWp-cC8REu7odXyh1JiMh3tM33Ryzk0m4xlInL6qfn2UsTVj7O51wQjGgSuGunozR2nmpidn302irZdHrTk7xYy4Ll0LekZAQVSaDntgwMyJOVWyCLzFxQC3HdhVXjuTq-xYhrotvdlAW4fKN21Lcexxgjr5AL2PCixPq5fllVfkllpUEgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVeYAb-EI3gDJ7V9IdwaDrUUuIuAoodTw0OE0mxxz7PEhUwvM19bD82S7iaXieASWiIIfLxqL6B2ZsLEV21-RIdAA4K-T6iri-YD4KTd4ayLLFfyq7DGcOtK4LVH2EcdnZeI0rMMYP2OYfe4GDzmoorCmhYc4QXH1TDasFTnUAnOZpk4-pq3lRGXvN27hm-ykSnYtXstB6wyNCKOKJsc0lwWft2Mww44JamClO3_zvlFuOyu8LBmM99jCqpFWiLFfT2DOZLifnpPk6dftJCtMAtccBAmjixeARlY7xazWwE0Y6bISGcul_uDmNjcZfC7Ucozq-ZN4RAYCJwqP61VjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERPGWfRAGlcD0xgEKX1jd_5_I0PYE-Cg4tLcKqy6as862w44e2Kl1uVNodO_Bntyd9EGWVw9xCcH-lcJJOpk8Hn-U_s78PgX2i2oXwVTF-pklsk18PZVFPLaPVB3SV2JaiMRAT21QYocyNmEOfNXOjutneloWR5Cqpm4h-iXxIKV7rS-8yu5_LTM_DtdwbVH_DcP1jpqi0yncwN1I99GoYQxu2f1k783auN9bz2YsobxDExKkskNnnlIZ-k0oWh1pBv6J-1HcYGmPVP1EpK1Rb8ixJ8ujKs4_76Nm5wzwhGUZMXqUEYnG95eZy1wWbFrId3sJ4RC-V3pjbHyMFI-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPZHz8YkndHEtjGkuzFYTP8s6OMnr4-lYIri_wqLzn69TV8G-SF73LA1cetwH8RksOgR5NGfdxPjcn2cnbAQA0WcBbaYn95bHJHj_KTs_nEGPlDCBmWD1DsGSmA8kANja48mAT_L4aE55P6Xh_ECmEs6DSfF6WI6LzQHHbPuzgWw6PztnlWRhYmijlB8TW29y8ZR8UvJML3Ns0gEV2HGtZrdtIKXnhSHUm6ap5MMegbsqBmLpDeb5BGD-OyTzTolIZmhvAjxXoWxH6EmNB7HGhEx2MH1ynHah9aVBpjeysSmSHQyk3wRWqe5HWyS3QO8sKh_AI1e2h0jPbjKgD3J6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFIUlhgaedH9KHWV8YZ_qUF5snjE3OdpFEOFRfM9c9nFuwnpsPhti6Ii0XPc61pVt3uPlvvr-_PwOZG7ZommNS1rRXcXOeAlYwm7HU1zBMUwhWzgDhWTQ_f2y7dzlwxqhyuTHdN8UECVfKUeTh9Dx642BMy_CyhZA5eyONEdjHKrRcgWWLoCNOgZnQJjJ_ky6Qb7CNk_8Hs4DgZ2RPTGqy2xtogXpJ_Te8UTCz-gXoEPiGxjQG_kLmpXAAnpCHGFDWtfKoKTr26ygsD4Q_9Djdzg4p7sgzlJ5cmzBD426v-UcME97xtqoO_hpvwZxdnA5nLYxyaKPQIvAmse9wPVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_Wrl6VJKQxX-_mqvs7puKYbStAqhSPAiNZpDAng_T3IyjW8X6ddOJ4TdiXWGMOkPrPlCE2TyYSvnBY48pV0-4kds62jAqjvsiCe1vIg46Dc_RvH4XstqMaA6qs0IyZhLFaJaZ76ehJ228ufxqzX90x-aHF3RjEZ8w3BQtrCpK_oOV_5cmeUdexWVdID-fKMDcvlr7HnQ9uh7nP9-PeBCzTfO3KA5C4h6Wxn7H6C_7V9EjzrG6Oi6dzHyMefzVqka4N1MqzpQokgNKdw-jakA5u65XQjGiJioE_jEL8s5gDSoo1MvlS-seBA_nz1r532pCPa2JfgluKO-w4S1wCmHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت‌های ارسالی مخاطبان خبرفوری از قطعی برق خارج از زمان اعلام‌شده
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/672116" target="_blank">📅 14:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672105">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46817c70b6.mp4?token=OqEC5lJGrDnpSI47rqb5BUpRnUwXjHBVAE0Ig7rnAv80nRGF22R06Z-0LqlFMGshCUTykDy2h4OqPZW9rtMWcYkrzKRNbA3ISqSdLdQQ3104AqhXeJ1LkpqsEWpLaKJShsOOBlYXtLZ3Bt5N24t4vuTuQmoz9Ig6o5QBZqcEtUfrZRU0kh8Ybh0zH_PkicJV-0IyLoPDsE0tEYyNHVcRe7qaWmaM0DoZOG97PWLCRj9CMjUeF4DhPH3cOa9wHlTm8sBaXoojmsPZXwDEGQ6Rvp4NYrlHeqHbAkdWNP8a3tWLegZqXGDupcvtwE-nND0Uv1yIuVUecG_W8XdfG_bahQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46817c70b6.mp4?token=OqEC5lJGrDnpSI47rqb5BUpRnUwXjHBVAE0Ig7rnAv80nRGF22R06Z-0LqlFMGshCUTykDy2h4OqPZW9rtMWcYkrzKRNbA3ISqSdLdQQ3104AqhXeJ1LkpqsEWpLaKJShsOOBlYXtLZ3Bt5N24t4vuTuQmoz9Ig6o5QBZqcEtUfrZRU0kh8Ybh0zH_PkicJV-0IyLoPDsE0tEYyNHVcRe7qaWmaM0DoZOG97PWLCRj9CMjUeF4DhPH3cOa9wHlTm8sBaXoojmsPZXwDEGQ6Rvp4NYrlHeqHbAkdWNP8a3tWLegZqXGDupcvtwE-nND0Uv1yIuVUecG_W8XdfG_bahQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله مجدد جنگنده‌های آمریکایی به برج مراقبت دریایی چابهار
🔹
صبح امروز ۳ انفجار شدید باعث وحشت مردم منطقه شد، اما منطقه مورد انفجار مشخص نبود. جنگنده‌های ارتش متخاصم آمریکا ‌برای سومین بار طی روزهای اخیر، برج‌ مراقبت دریایی بندر چابهار را با شلیک سه موشک…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/672105" target="_blank">📅 14:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672104">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
سپاه: حمله به مردم و زیرساخت‌های غیرنظامی تاوان بسیار سخت و بیچاره کننده‌ای خواهد داشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/672104" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672103">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msbNhsPPQwDcx4wTKOaoHVTkyIFaQR_H-XEtQe3kS1-SclAam_qhGr8jicstccLuxq04tNxA4dy3tT6UxmZ1Z2FD63Ec7OfQyyF5LWlA_M5lTEcr-sq93jA0Z5qkryWjumHFdaiGlvhsPkORUL3iWLKqQo9cBgqhJ1WH5cl78OBLcYhAmQJ7Isw8DsRDW6NNOOMX3ouxAJFuKkXSGMjUT3_DGGGq04CYLBSEvNu3xPpj-pMj4AnwdAo14FrzI2xURTZEuSDvIdljmmQc4YlxBEdz9Zvu7k--em6aGoNBHUFC8Cd-xZt1EjU_9gIlhMbUs5qLcD5xNoPXGC_E632nyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای دروغ‌گویی اردنی‌ها در رهگیری موشک‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/672103" target="_blank">📅 14:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672102">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCzUARU6Qkqz7zg10OYGmpUjV0lX2wuJHl0mx4_LPzQFawLi9r80YPF-qQvd-wABWVEaq25bYs0L9Mc36bAI9mYb3BibuM907immUkm050FQu0fyb7ReHWpfJZ_M4g9kWZfd3Pzva9Rx2T-8N5VSwgIgTD8-zMeoRrxhZW4M28vEoOsowQOWQw2foC2ESXKyvYecy_FeEUWqKw1EFS4eVq0QSAv_F1mBjPxalm1Lb_nP3ZfmAoVKZXMqfBkvT6HMrtArRAQgMNUaU3k0zFHhI5-ssHd-HZ--UEQ5qZYFub5oF0776YYhcfdKCw9MkAJIE6YkAOwEPfi71pw_6V6CSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میثم ظهوریان، نماینده مجلس: یکی از عجیب‌ترین و غیرقابل دفاع‌ترین تصمیمات کشور بعد جنگ رمضان پذیرش قطر به عنوان میانجی مذاکرات با آمریکا بوده‌است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/672102" target="_blank">📅 14:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672101">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coMgGJFvB0cnD3HDpv-qQ4xhQ-SMFkq2-ZokuVVz9vA_JtNFBfxFKLTub7Y-xNCPxDXwxpamFjQ3QlXq2Wviw6GUixRtghzu-8o5Id2E82pp05_mM182_ZfZ_6ZGLO8rLp-EfVBSIkI9q2gHNg0kaQCgzYpiFLFlExX-v93dUy9ANw9SWdftUfjoXuYT1HBK9HhXtuXv785SV9QIrMiOYtJlidy1HSbihVd3a-O1hdTfKVr4YIQBTDiRw2MO-DzQFIiemIkg5Aunoldn4ZnTXBrG3PIrMdO7_0lq9hUuCzUhuRWopGUR1Iv_lRouQk-aVziJhs7MtxB9_mAuAbmz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثه برای یک کشتی تجاری در شرق بندر الدقم عمان
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) اعلام کرد گزارشی درباره وقوع حادثه‌ای مربوط به یک کشتی تجاری و نیروهای نظامی در فاصله حدود ۱۰۰ مایل دریایی شرق بندر الدقم عمان دریافت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/672101" target="_blank">📅 14:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672099">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF14xEPYA_gyrl3KE3Wr5X3u9Ndj-5jGkOzUD__CXTsG1F9YFDH4IO8HthJJF8UX9XjdxipAAt6AxIvvh4y8VSaobTJDMIg1aQxIm_dSZP4R2xDMAevaHCpJrADlDtNu9yiTFhlBkGlt4gce1t_LG947NhkUk5ZChQjKUfUfKvvEAgkqU8DQAvePVrTIicLbUZht0yCbGcrrimdSordrVlLlE6IbwcyCWCjFGB6X8QQVEiScv4MAvrqJxjVTNOG0mYEX45YxIdBWf1Pxps_yJrsf0rk6GqV7hEj5axk_LfACdqIMYM1Wm-h79hlCMXXFCGN7dQ5y06X1tJi6AT9_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلیمو برای استان‌های همجوار خلیج فارس رایگان شد
پلتفرم فیلیمو با انتشار اطلاعیه‌ای، تماشای محتوا برای هموطنان ساکن چهار استان جنوبی کشور را به مدت ۲هفته رایگان کرد.
در متن منتشرشده آمده است:
فیلیمو برای استان‌های هم‌جوار خلیج فارس رایگان شد
❤️
ایستادگی قهرمانانه شما، داستانِ فرزندان امروز و آینده‌ی این سرزمین است.
❤️
🫂
تماشای فیلیمو برای شما قهرمانان حقیقی ایران، هموطنان نجیب و خونگرم جنوبی، مجاوران و حافظان خلیج همیشه فارس، در استان‌های «هرمزگان، بوشهر، خورستان و سیستان و بلوچستان» به‌مدت «دو هفته» رایگان است تا شاید ساعتی را در قاب تماشا، هم‌داستان شویم!
با هم از این روزهای سخت عبور خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/672099" target="_blank">📅 14:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672098">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2492fc3624.mp4?token=bTQSML_4G8pxWV3nE0BKsNUHSc8aBcnWry0e2pDmu-sYj3r2LlnAymda0WaRIV6mJCmtqT0lRfZVWfGQtMf-V7m3sqDYXk84l5O8WpwqAzKQI4aw60j2A_Lo3iiekBNyzsnoU2-1To4SS34YfsxtLe6zdK20Baog9eIxCFtw2Cl77TcQ4uQxff2qGTmZQ70qp5H4gIWAZrwiDK1DLHmRhFLnvc8Z5-DlsvQzFtkCPQ-HYQfpm41EY5EwoeKgz7s9ER8EmXH2Fedkds8vPVwj_YN-bOPDsxvyBwvugBn0eKCpeIvmQdw7w9R7VMBMXPdmYSaD9_rE8gj6GL59eHRoKSANCTH7vCsjqbOIj3f4x5X-tpcvS5yyddK2svImcadn9Mh8bEo0xAWEWH2fnDYfhjP4F3-I_tmM1zzUcyUECERiIaaTdc-HTx9-vfpiaNEkqtCH5k6oDXApZJxh8GU7FHFly1rryilBzWbJAX9UuKWh7Uep6xnbyxxNkshzjMpZOm0BBGfEgG2vmNY2gFV_YKg1e3dSsCya-7GKStpPEglFSPFIZHQp3M6dNbBZ_c6AVJWdhRTgNfQM0q4k-eg5HJsW1RB2MG61mWkhBiSpXpGJgHHVnXGXALBkShNkRFcbudI13fv3LPmX_OgyR-SJjd4oKEm7jLUdoEumx2s6MS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2492fc3624.mp4?token=bTQSML_4G8pxWV3nE0BKsNUHSc8aBcnWry0e2pDmu-sYj3r2LlnAymda0WaRIV6mJCmtqT0lRfZVWfGQtMf-V7m3sqDYXk84l5O8WpwqAzKQI4aw60j2A_Lo3iiekBNyzsnoU2-1To4SS34YfsxtLe6zdK20Baog9eIxCFtw2Cl77TcQ4uQxff2qGTmZQ70qp5H4gIWAZrwiDK1DLHmRhFLnvc8Z5-DlsvQzFtkCPQ-HYQfpm41EY5EwoeKgz7s9ER8EmXH2Fedkds8vPVwj_YN-bOPDsxvyBwvugBn0eKCpeIvmQdw7w9R7VMBMXPdmYSaD9_rE8gj6GL59eHRoKSANCTH7vCsjqbOIj3f4x5X-tpcvS5yyddK2svImcadn9Mh8bEo0xAWEWH2fnDYfhjP4F3-I_tmM1zzUcyUECERiIaaTdc-HTx9-vfpiaNEkqtCH5k6oDXApZJxh8GU7FHFly1rryilBzWbJAX9UuKWh7Uep6xnbyxxNkshzjMpZOm0BBGfEgG2vmNY2gFV_YKg1e3dSsCya-7GKStpPEglFSPFIZHQp3M6dNbBZ_c6AVJWdhRTgNfQM0q4k-eg5HJsW1RB2MG61mWkhBiSpXpGJgHHVnXGXALBkShNkRFcbudI13fv3LPmX_OgyR-SJjd4oKEm7jLUdoEumx2s6MS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد/ دولت پزشکیان می‌توانست فیلترینگ تلگرام را رفع کند ولی متاسفانه چون پزشکیان روی وفاق تاکید داشت این اقدام را انجام نداد
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
دیدیم از طرف مقابل خیلی مقاومت شد و هنوز نتوانسته‌اند باز کنند. اگر قرار است بسته شود باید به شکل قانونی انجام شود و اینگونه نباشد که یک نهاد امنیتی یا یک نهاد قضایی اعلام کند که فلان سایت بسته شده است.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/672098" target="_blank">📅 14:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672096">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bc77fdf3c.mp4?token=eEy7Iab7UFGZVwb_t4LmkbPO9X3JcTeuAfYvQDuRsJoTcP1S0CYFVe1MXQpAZh9aRCZXX-L2ZKZjxBpTpwPUS04q7FXiMTsxWmDc5NmrNal5Up75V8iA-Uzcr2QU4uh6kdfUEEcD57jKNALARwrS4zML0sSSWUIGCTCJpR1bIgAOlwiLnN9dyV06v37Jggwu_tuPEpTnIQAuK8yuqLIoRBgu4lbt9fYKz0Q9tz2941h3YSyxyvr2oBNvFWYWC-LTRnFsxkvbeMDNYkc98KyV__e78nE7y8rPL0cvK0KBzq4ixqjTTu1cFOmD-WveP_iFWU1Es-L_0OGwSdCJcff_Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bc77fdf3c.mp4?token=eEy7Iab7UFGZVwb_t4LmkbPO9X3JcTeuAfYvQDuRsJoTcP1S0CYFVe1MXQpAZh9aRCZXX-L2ZKZjxBpTpwPUS04q7FXiMTsxWmDc5NmrNal5Up75V8iA-Uzcr2QU4uh6kdfUEEcD57jKNALARwrS4zML0sSSWUIGCTCJpR1bIgAOlwiLnN9dyV06v37Jggwu_tuPEpTnIQAuK8yuqLIoRBgu4lbt9fYKz0Q9tz2941h3YSyxyvr2oBNvFWYWC-LTRnFsxkvbeMDNYkc98KyV__e78nE7y8rPL0cvK0KBzq4ixqjTTu1cFOmD-WveP_iFWU1Es-L_0OGwSdCJcff_Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رانش زمین در جنوب ‌غربی چین
🔹
بر اثر وقوع رانش زمین در نزدیکی پل «ووجیانگ سانچیائو» در شهرستان پنشویی، واقع در کلانشهر چونگ‌چینگ واقع در جنوب غربی چین، چندین خانه مسکونی تخریب شد و تعدادی از ساکنان زیر آوار گرفتار شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/672096" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672095">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف: ایرانی میراث پرافتخار خود را به آسانی واگذار نمی‌‌کند
🔹
مدیرکل روابط عمومی وزارت نیرو: خبر افزایش صادرات برق به پاکستان جعلی و مغرضانه است
🔹
وب‌سایت کپلر: دیروز تنها ۸ کشتی عبور کردند که کمترین میزان در ۳ هفته اخیر است.
🔹
نیروهای امنیتی عراق در استان الانبار یک تروریست داعشی را به دام انداختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672095" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672094">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
تیزر قسمت چهارم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای حسین حاتمیان که به دلیل سقوط از بالای تریلی و شدت ضربه به سر، روح از جسم جدا شده و قدم به دنیایی بسیار زیبا و دلنشین می گذارد؛ منزل و باغ بزرگی که متعلق به ایشان است را رؤیت می‌کند ولی عذاب دردناکی از دوستان و نزدیکان گناهکار را نیز درک و احساس کرده و در نهایت به دلیل سلام دادن همه روزه به اهل بیت در دنیا، از آنها پاسخ سلام را در برزخ دریافت و توسط نوازش دست مبارک امام جعفر صادق(ع) به دنیا باز می‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حسین حاتمیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/672094" target="_blank">📅 14:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672093">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f48ceb9ad.mp4?token=JvJSPw9k1WGS2PkLPY4wAohTo7qNzlfHvrvWP8ewst3KuaLZ2v66ocj93nKePMZ-jMvwibFdkYNxlt_FyGYiZJGkiY5Ko9xVCMuRPew64dIwis3D_Qytr9uLj2sh4SuSwyS6tDJslece2blUKS8yYZ4Y16clycs5kHDbTbP_SVYwT0fBZ_TS0iE8BCArBRgpgKhk3DDyYxpDKRznWr8kz3j-me_S5ChB1_BCSRz_KCQe0DPs6HC5hNDrRwQ8mBHUBV7NMKzgzyR7Bt-Iw9VKjpr0Lh2Hbuy2PfpJqkJvmHrWBlvH-9gwqBPw5v685BUG6c7cci7zJFnMcsK7xv0eIDM9WyWON_u_r0_uDSA9z-aMEQmnscxRqED8Z9hruOI0xMOKr2XYrLk0Z0ScRixWIDmGRtMR41ugVJ3wYevTRA2GLFopU_m7fDw_VjNW9K-UqFFMGdXwfxeT7FzS8ixweq-jNy51nIwDIOhg8J2AGxt__5MdgmRVMnmwn6yopTkXPtPOGRCw-K2CeoMtQwaclCJ42c58DerjR1FqmGtkEPwkdBV9mbBILO9qpfBVA58gSjBhhDjdqx35oDxpghJaykfVFweG9aH6HjGlwdq837RLG8fnR_SUnrheiE8UkWgNkbgnpHn5MQHBSwmgaYKx9y9eSW7V9OKqZtIYni8IabM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f48ceb9ad.mp4?token=JvJSPw9k1WGS2PkLPY4wAohTo7qNzlfHvrvWP8ewst3KuaLZ2v66ocj93nKePMZ-jMvwibFdkYNxlt_FyGYiZJGkiY5Ko9xVCMuRPew64dIwis3D_Qytr9uLj2sh4SuSwyS6tDJslece2blUKS8yYZ4Y16clycs5kHDbTbP_SVYwT0fBZ_TS0iE8BCArBRgpgKhk3DDyYxpDKRznWr8kz3j-me_S5ChB1_BCSRz_KCQe0DPs6HC5hNDrRwQ8mBHUBV7NMKzgzyR7Bt-Iw9VKjpr0Lh2Hbuy2PfpJqkJvmHrWBlvH-9gwqBPw5v685BUG6c7cci7zJFnMcsK7xv0eIDM9WyWON_u_r0_uDSA9z-aMEQmnscxRqED8Z9hruOI0xMOKr2XYrLk0Z0ScRixWIDmGRtMR41ugVJ3wYevTRA2GLFopU_m7fDw_VjNW9K-UqFFMGdXwfxeT7FzS8ixweq-jNy51nIwDIOhg8J2AGxt__5MdgmRVMnmwn6yopTkXPtPOGRCw-K2CeoMtQwaclCJ42c58DerjR1FqmGtkEPwkdBV9mbBILO9qpfBVA58gSjBhhDjdqx35oDxpghJaykfVFweG9aH6HjGlwdq837RLG8fnR_SUnrheiE8UkWgNkbgnpHn5MQHBSwmgaYKx9y9eSW7V9OKqZtIYni8IabM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر عملیات ترکیبی موشکی و پهپادی با تاکتیک های ویژه و غافلگیر کننده علیه مواضع آمریکایی در موج‌های ۱۰ تا ۱۶ عملیات نصر۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/672093" target="_blank">📅 13:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672092">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند  استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/672092" target="_blank">📅 13:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672091">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
حمله به یک کشتی در سواحل یمن
خبرگزاری رویترز به نقل از منابع امنیتی دریایی:
🔹
افراد مسلح به نفتکش حامل محصولات شیمیایی «آسانا» در خلیج عدن در سواحل یمن حمله کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/672091" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672082">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: برخی مسئولان امنیتی با پرونده‌سازی برای افراد تلاش می‌کنند انتخابات را مهندسی کنند/ گاهی مسئولان شورای نگهبان فریب می‌خورند و به نوعی رأی می‌دهند که منجر به رد صلاحیت برخی افراد می‌شود
علی مطهری، نایب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
گاهی مواردی را که جرم محسوب نمی‌شوند، به عنوان جرم جلوه می‌دهند. دلایل رد صلاحیت آقای لاریجانی خیلی سست و سخیف بود و در دوره دوم که ایشان کاندید شدند دوباره ردصلاحیت شدند که این‌ها ناشی از مهندسی انتخابات است.
🔹
گفتند شما در نطق خود گفته‌اید نهم دی اگر باعث تفرقه شود دیگر یوم‌الله نیست، بلکه یوم‌الشیطان است.
🔹
رهبر انقلاب گفتند که اگر امام بودند (درباره موضوع حصر) خیلی سخت‌تر برخورد می‌کردند. به یکی از  اعضای شورای نگهبان گفتم متاسفم که شما با این افکار عضو شورای نگهبان هستید.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/672082" target="_blank">📅 13:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672081">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۴| روابط عمومی سپاه پاسداران انقلاب اسلامی: سامانه راداری برد بلند و چندین فروند هواپیمای راهبردی سوخت‌رسان آمریکا منهدم گردید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/672081" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672080">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7D8s4m-BiR5gKF23Iye0rGVzqjk5Mk7ogWUqzd4r7EzgyGsGvC8BWSazM_tcClOHAFq_aSBF45K9DtaJOm0cXgc3e5ioElxP7p9bJ-bBidGT5wmXmywIibAcst8xvnf6tlXhdRdp066JgispIQ8tS06uKnBwdNa2iD2VE0bQftsTWs3SyPC0QcKU8t1LgAfaGURN9BYLRlfnr-nxA-RwWFO6_HtiVgAlDCnqLdSmtE24ZHMnkmzlbCARpVsbxX6ru25VTqrFv4G29PhRDI8hmzQGxz2zLjNEJu1C9XseWZ0THJtPgZiz7v100UC3lbT1qiXgJ7h3drFj0UsG-OSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۴ خاصیت سیب که سلامتی شما را بیمه می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/672080" target="_blank">📅 13:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672079">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11f25b166.mp4?token=J2PUNRXcirImWdNgiPIH5Bqqto51bcSxi5tHO4ejDSpoO6ekUPTHqhdG0aT_huH91enqF6T4RBouJOcWjzKDnSgculPK6GEiLMBann90VOLVy2McbcA_dYQjkdwv9Zly5SxnSr6kzqkfRnOuZim13VsP4D9r7fxeqcQOkuI7s_5-3cbD2bCOWc5VloaJ4zFlB05K3Rn_HlEOhT7tDaY0_R1kMT8Y17ViXDBrweCQ1QKDS67rC8DxeWo4pnASnfpvSXOYcxcZ9_w9fTgyx4KL-4WYscXXyrcQYW_YuYC_7dwLVM8E1vIOsPzaX0MITSX7pFO1ZbsAwKbBaRKgof2kWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11f25b166.mp4?token=J2PUNRXcirImWdNgiPIH5Bqqto51bcSxi5tHO4ejDSpoO6ekUPTHqhdG0aT_huH91enqF6T4RBouJOcWjzKDnSgculPK6GEiLMBann90VOLVy2McbcA_dYQjkdwv9Zly5SxnSr6kzqkfRnOuZim13VsP4D9r7fxeqcQOkuI7s_5-3cbD2bCOWc5VloaJ4zFlB05K3Rn_HlEOhT7tDaY0_R1kMT8Y17ViXDBrweCQ1QKDS67rC8DxeWo4pnASnfpvSXOYcxcZ9_w9fTgyx4KL-4WYscXXyrcQYW_YuYC_7dwLVM8E1vIOsPzaX0MITSX7pFO1ZbsAwKbBaRKgof2kWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرائت دعای سلامتی امام زمان(عج) توسط رهبر مسلمانان جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/672079" target="_blank">📅 13:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672078">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSS4IkDqKDFdnOw_SE-Vx5jV_3S0ZhZwD7vYATOrMWFPPJ0oPZ6Zzpg0RRY6gE4w4V7vaGXSDsiaEsiGWNt7VTz6f9_TJbqINQU0P7Sz56WCPe6YeoQa_YtowEaDLBWGVzkw7xgIJIdOHhstAIMmgilv1nwg3z4NaiQbtprXRo6HyHjw3QMMcUA3KUbhp1hqlXCBYILL7lmXJxUUe0kxqUHiZMztc_REnAOOmv1JxIz0wKxaZbs__RbQuEnDKboN-2R_tNRIDx7wUlamueWKnNjaYxJjv4x8fT0JE77Nm8UlwdmyKrV249F_uXOd6091zEFljecfeGNqChP0hYX_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اشاره عراقچی به جریان نفوذ اسرائیلی در امریکا؛ همه این‌ها به‌زودی برملا خواهد شد
🔹
به آمریکایی‌ها مرتبا درباره «نفوذ خارجی» هشدار داده می‌شود؛ پس در مورد کارزار گسترده اسرائیل برای فریب دادن دولت آمریکا و کشاندن آن به یک جنگ انتخابیٍِ بی‌فرجامی که حتما پیروزی در آن نخواهد بود، چه می‌توان گفت؟
🔹
بدتر از آن، اسرائیل از پول مالیات‌دهندگان آمریکایی استفاده می‌کند تا هر صدای منتقدی را در داخل ایالات متحده خاموش کند.
🔹
اما همه این‌ها به‌زودی برملا خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/672078" target="_blank">📅 13:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672077">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
اختلال ارتباطی در ویسیان و معمولان پس از حمله آمریکا
شرکت مخابرات لرستان:
🔹
به‌دلیل اختلال فنی گسترده در زیرساخت‌های ارتباطی، تلفن ثابت و همراه در بخش ویسیان و شهرستان معمولان با قطعی مواجه شده است.
🔹
تیم‌های فنی در حال بازسازی شبکه هستند و طبق برنامه، ارتباطات ویسیان تا عصر امروز و معمولان حداکثر تا بعدازظهر فردا برقرار خواهد شد.
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/672077" target="_blank">📅 13:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672076">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا به شهروندان خود؛ به عراق سفر نکنید
🔹
سفارت ايالات متحده در عراق با صدور بیانیه‌ای سطح هشدار سفر به این کشور را به بالاترین درجه افزایش داد و از شهروندان آمریکایی خواست به عراق سفر نکنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/672076" target="_blank">📅 13:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672075">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند  استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/672075" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672074">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
تعویض گل‌های مزار مطهر رهبر‌ شهید ایران و خانواده ایشان در رواق دارالذکر در جوار حرم امام رضا(ع)
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/672074" target="_blank">📅 13:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672073">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: شهید لاریجانی ساعاتی قبل از شهادت با پزشکیان جلسه داشت/ پیکر شهید لاریجانی چندان سالم نبود
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
ایشان جای خود را در خانه آشنایان و اقوام به طور دائم عوض می‌کردند. افطار همان شب پیش آقای رئیس جمهور بودند. عوض کردن مکان‌ها به صلاحدید دکتر لاریجانی، فرزندشان و تیم حفاظت بود.
🔹
این اتفاق کار اسرائیل بود چون ترس داشتند به وسیله علی لاریجانی توافق و نزدیکی بین ایران و آمریکا اتفاق بیافتد. هروقت احساس کنند قرار است با آمریکا توافقی شکل بگیرد، کارشکنی می‌کنند. دلیل اصلی شکست خوردن برجام نتانیاهو بود.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/672073" target="_blank">📅 13:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672072">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8bc8dc64.mp4?token=Ev9Ex4jzSy0LWw_GXfAuhnlHsl7mDb2gmCvMpGsmhJOQdmtc8K_-Qe-tCWnvyWIygRqAiqDfhKimnRQ-oNXNKlcAYZze3HQRjm65BDZJO6JZOo0W3OU1HaRxPQhBYrswLseudGbjS8X0TtuAW50cAtMFLcpkbgYDAX596JajDbwqHZ1pWwH1ddrNV-O8erloF-9Qtx3Gsfkl_zJq1_jVBdl2f-58kGo4TnbavCk4u-3PmWc25CNiXcQ-tL_b8LLhfAkkccmjUx76Axr0Bo0z6QHC2V2edlWJG0Hss6PV1oiJnJHnfJrNRzRvnVvVNcnA5airDPDcHENwyErZ0_tJxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8bc8dc64.mp4?token=Ev9Ex4jzSy0LWw_GXfAuhnlHsl7mDb2gmCvMpGsmhJOQdmtc8K_-Qe-tCWnvyWIygRqAiqDfhKimnRQ-oNXNKlcAYZze3HQRjm65BDZJO6JZOo0W3OU1HaRxPQhBYrswLseudGbjS8X0TtuAW50cAtMFLcpkbgYDAX596JajDbwqHZ1pWwH1ddrNV-O8erloF-9Qtx3Gsfkl_zJq1_jVBdl2f-58kGo4TnbavCk4u-3PmWc25CNiXcQ-tL_b8LLhfAkkccmjUx76Axr0Bo0z6QHC2V2edlWJG0Hss6PV1oiJnJHnfJrNRzRvnVvVNcnA5airDPDcHENwyErZ0_tJxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم ملی والیبال نشسته ایران برای نهمین بار قهرمان جهان شد
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/672072" target="_blank">📅 12:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672071">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaQg__fJmj-1Pv-uLDWThEcx0m3K-N6JYllJhd3pLK_MBrICxwPF50k5LhCmEfkkTSzJu_o5uwie20NrtzOUmgmRG-ym6xTx3AZxRBIucuBUhg9DumGchQNewnkmiS7QRpKdZaRvCBe8pGlo4ZpV9mw2biAIDQTzs4KwlwB1JTrSXCr0BVp-n-Lc0yjL2nPC498p8rIBvgmcEP4FvSAunzqQvAPi1f0scyJDZpQ0f7QjHbp9CddSM5aoh586MtNEs8M5iGyM4EFh6-3tG5XfPs4Q7kLy3YkgMj4y_GiE_YWgMFFByzAwu3yN6NcxcFmgnNINevKQ_VOj670beEe87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام لانچرهای موشکی مستقر در اردوگاه سازمان ملل توسط ایران
🔹
ایران در یک حمله پیش‌دستانه، لانچرهای هایمارسِ مستقر در اردوگاه سازمان ملل در کویت را منهدم کرد؛ این رویداد بار دیگر نقش پوششی این نهاد در عملیات‌های نظامی (مشابه عملکرد آن در غزه و یمن) و فریب افکار عمومی درباره ماهیت سازمان ملل را آشکار کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/672071" target="_blank">📅 12:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672070">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
افسر ارتش صدام: روزی نبود که خبر ترور کسی را در خانه‎اش نشنویم؛ ایران بعد از جنگ هیچ‌کدام از فرماندهان و خلبانان بعثی زمان جنگ را رها نکرد و همه را حذف کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/672070" target="_blank">📅 12:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672069">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
گزارش وقوع حادثه نظامی برای یک نفتکش در خلیج‌فارس
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه میان یک نفتکش و نیروهای نظامی در آب‌های خلیج‌فارس خبر داد.
🔹
تحقیقات برای روشن شدن ابعاد این رویداد آغاز شده و به شناورهای عبوری هشدار امنیتی صادر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/672069" target="_blank">📅 12:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672068">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF48efWsOLelUaWj4QWQZUql0q6TNDWtbzaA9r_wqrEj-W3-VhT4aZAOig0Z9BJrOe3VazUIRF4ZkdWcVYGSw1yJtnNahO2xBNIZ2-FxbpIN93SwJ_E1D5YLZ3scb_UJ7HEOIMZlL0Lymq7pAaHtpqaS3jWK2Rj1WMsESgheTekdjpmZ9V0pzJk8yIqy2A-WGpMRU2QRs_IcvChlHvlidUCJevO_78UssHE_7G_c4KknVNm5IfWTT7E8co38F2_syAqCLkDEJcWt2Hn0z8YJD682h9uhtBWIqmhrOZt3F23SbtBpQwXNKm0C46vXk1MIW0SKSJpXAoqa8PXayY5f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد
🔹
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/672068" target="_blank">📅 12:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672067">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وقوع حادثه دریایی برای یک کشتی در جنوب یمن
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) اعلام کرد گزارشی از وقوع یک حادثه دریایی در فاصله ۶۵ مایل دریایی جنوب شهر المکلا در یمن دریافت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/672067" target="_blank">📅 12:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672061">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1DRes35gqWz5Lo81xponQv1iqmDtl_ZIULBHg3PDWlALDDtMxca4Hi1-bGeKpP6AsDKnTAzeJlepOUdkRaSBUxEvsQDlNGpWl7isTycq_SBlp2_cwGqYaaIJiN3jlwaRTuwvbpw0Js1CFM3taxK98La53HgsGdnnbDojc26GTfVmPy3uA6AzOWVCbMTmqIyILzlqOCaptNjSlpILIWwWJqQ-ffnNT85Dpbq0WVx9QYeSHqO9jTecXmUs3mC_qEviPOoAvpr5lTbEnhan--PRl0_2egaSPdHYVDrHif7xDh2FoOLNmR2lqb9-AnuQ9M49k4bUZWi5Rbmbkv_wrUphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBxFyh31G-IXcoUa0MgVxkrO6FZmlL-Ejz398Uz6jXnwEc_T4rqmJVNr8QF-aTn16AG0kVjCREuvdsn8LHhJfzsKSZ0oUh1UyEUZl8Bgaqtt25qH_Qsc4ISC7AujY6NDCejDyvY4HEO66S5gsySURKIbe7pztyTy8IhmUCk85QjhbdLV3-ad6XPTpy5bZ1pFOmimoS8rfru5QML4Inpgw4djFmHgUAKmGe9w_YfBFK7ClmGmoJT7Z64hrGVAZdALK2h-kOnwGkJ9eNWskXPhDoizH1h3vxTQcD3U0NXRPPeOHAxeiftriqARGbegvWUqbSr5AWY3SYnu3TfMBqlANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4cQjdWi-ZFv9CcgNX_a4N6Utc_0Q_gQqNATFfU3DkZLeZSzLl1bGP28fCH7Iptt3xC5Hgep5BnR4Pc0OCoPat2BoGhl3JKP_gdLLtWrz02rp4noZX1dZBB1PKwyMcUIgQ1nVe4zWLym0F24lAvGFtRdGgsigkrBiZnbTeAFtYHjtg3o8wl0LieOev4iu0VA4X-UsFFtrGe9Qx0APSlAOEMqObJQL6Tu8fjF8RXq8hpfNuuYBJsasMOKyZhxptTgWgEBn1vrcnI_xfWG4DpeKxLuGnn4mVF6xAC-tnD4ZL_OtDIf9O-5KCOdUXEu30xIXAFbQuIEU-_15B59EP2R9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8cUuZWg3AM9YUOY5FTv_MI1nEyX-zGQzKP-kTv3xRS_MVq1I4ndT6N5rSeRNnV2NqjyLZVsWQqpO2EqgYq1jD2LY-IcvTUoQgra2NZGJet6sKWgacMaiBBRNj6NBD-f6NIjAGhjqmjELMePpcxknFH6ZeoivBpkKErTqpSnc4Vfbl35bwuAwXlK3ctjQs-kfAB3u92fey46l1OPIxQ1d-nJEmjzteKKPILCzRI8bIHMAZXA0MDaqpIa6GsOiocZfpQJVN44qI1sThq8-XjAsA_UbSW3J5t2ClmoQE1j5fMtWXm0yqP1-Y5lgOErp8gbgwTzvCDjwV6UIaWhKJ__ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlX-KvBf-k9vD3QvcldF5q6zLQkEmffFgk1Mc4J7Kb02R317Q8rkdQYFvjPH7920pPwBouyQG_E5uuURe4bDkxoIzOxoozpxKA2pPg_SJT2NkhX8qI3tFnpNrDSqaz9GbPZ-QCarTM6KGgYMh_SR_89bjpf_KwoTfkPLbb_W32Bmv1_xngJS3KBp-edTlTmrbmouUXrbnimNesT9IB9uRtLx1aqWu2ZOdQC2rsxsYEbakl1jAiE2MAovxt0Vt_zeDJbIVofCMj1Oa0JdUkKww-D8Y3dTvX1gAa4vqpV3Itl7c6IWZT68wlYTZmyGqz5r17ojrzPUjJ9Gc857Xod4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uV2tFHKkbYQQA-ymqmXwipAlT4n0Nu87-ILWGRjQG9epIjBb0qiSYVh6iRTr6FtnB0OQNaYUh9cTB2TtWhEsf5IsDhIikhl_AXThHWokmW3gyMKBcL2F84hJIUmPJQdBLR017z8FByIlOBaLRW5f56SCBLg1PI945exe9aPzBENln4JvTxCMTpTJ9-rCGtmE4k2rTiXqZNz8kRlDtX1wvjRNok8ZCx-p1k4PLn_s4tX-wNGHxuJKtaTICFSJbIpe55UvQBxASBSm3NPmTo7XT0L3N6Kf82fe3T1vwYlDvO_QQTsZfLQVG9Ki69kcsx3p1Wtyn5IPb-q3RvGwyBN32g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افشای دروغ‌گویی اردنی‌ها در رهگیری موشک‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/672061" target="_blank">📅 12:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672060">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f51880bf.mp4?token=ivIqseVfjjM9eihXX555qP50Os6_cWhg4qkj3444SwfJeFAGB3FnlJ8bLyJ4ifhtRyvdrW5bT8rHVB89TduxDvjbA6vEbhJpRBqart_5Oof0nLGJs_Mtr1CJJP7oOXkyFj27xS-7QYjGOr546gypw6IQvGVEUimZFzDpEdqdyoOdi5MsUjLct4gm0Uvdgs9KV79U5OMqib-wmCPmDC7TLtl3952pf4bik362dbwrBVuQUwFvB3jORYZZVV-9cJJO-iNIhac3vNoHVSaJmVCqzJ6IUWojTcdI-RzFgZ9oYYOus4bGfDTnXttSTIV08eKJ57sRQV6t_3-a-qffPVcm5RKdhfmTz3rZN0irQv4G4uhiWCjIMuE-j8adb8WiBT32mqIPegbbU0ymVgwSuoXdemTSIKILNZLD3lCs-rxQ0XPrhuSsCntIi3llDm5USis7N8R4OCja8DDD7pQ2oKP6qUnkHSwI1twINe2IefkZObfZqKgLHzPTOWqnK0x0KGjdwbN3DTb4u2rcaLvVxSlAKyVdYilY7dGduzwttkvzpdapH2zNrCM3WSsJRRsgfs5cQhmSDMrTL9HeG7FhLWMozOXH6TEk636BZKA9Rm1284wCOc0KqxP9VRxtin1UW23wwrXbxKZvqnxV4XZ4O2-1viKbOSSlCTHptEHtgQEDyEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f51880bf.mp4?token=ivIqseVfjjM9eihXX555qP50Os6_cWhg4qkj3444SwfJeFAGB3FnlJ8bLyJ4ifhtRyvdrW5bT8rHVB89TduxDvjbA6vEbhJpRBqart_5Oof0nLGJs_Mtr1CJJP7oOXkyFj27xS-7QYjGOr546gypw6IQvGVEUimZFzDpEdqdyoOdi5MsUjLct4gm0Uvdgs9KV79U5OMqib-wmCPmDC7TLtl3952pf4bik362dbwrBVuQUwFvB3jORYZZVV-9cJJO-iNIhac3vNoHVSaJmVCqzJ6IUWojTcdI-RzFgZ9oYYOus4bGfDTnXttSTIV08eKJ57sRQV6t_3-a-qffPVcm5RKdhfmTz3rZN0irQv4G4uhiWCjIMuE-j8adb8WiBT32mqIPegbbU0ymVgwSuoXdemTSIKILNZLD3lCs-rxQ0XPrhuSsCntIi3llDm5USis7N8R4OCja8DDD7pQ2oKP6qUnkHSwI1twINe2IefkZObfZqKgLHzPTOWqnK0x0KGjdwbN3DTb4u2rcaLvVxSlAKyVdYilY7dGduzwttkvzpdapH2zNrCM3WSsJRRsgfs5cQhmSDMrTL9HeG7FhLWMozOXH6TEk636BZKA9Rm1284wCOc0KqxP9VRxtin1UW23wwrXbxKZvqnxV4XZ4O2-1viKbOSSlCTHptEHtgQEDyEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: در ماه‌های اخیر که نظارتی بر موضوع حجاب نیست با موارد ناهنجار مواجه شده‌ایم و دولت باید به این موضوع ورود پیدا کند/ ایران قرار نیست اروپا شود و نمی‌توانیم به برهنگی و بدن‌نمایی بی‌تفاوت باشیم/ قبل از سال ۱۴۰۱ حجاب در کشور وضعیت خوبی داشت
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
حجاب یک اصل اسلامی است و نمی‌توان گفت هیچ نظارتی در این زمینه نباید وجود داشته باشد.
🔹
نمی‌توان اجازه داد خانم‌ها و آقایان، هرطور که دوست دارند، لباس بپوشند.
🔹
اینکه مسئله پوشش در خانم‌ها و آقایان به تدریج به برهنگی و بد‌ن‌نمایی تبدیل شود، چیزی نیست که نسبت به آن بی‌تفاوت باشیم.
🔹
برخی اقدامات ستاد امر به معروف مانند مقایسه تصاویر افراد با کارت ملی، ارسال جریمه به در منزل و محدودیت‌هایی که برای تاکسی‌های اینترنتی ایجاد شد، ضرورتی نداشت و جامعه را تحریک کرد.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/672060" target="_blank">📅 12:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672059">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbIe5H-fG9msX32QafKFeS_hU6XqtPR6WtJqgeA6SeykKwDjdUrqIF_RMhRoEKdDy750fWY3aYDemT67RQWCaIl3yN_9JOUj4qyhnAledj_Mb_QpyaKxrGb-m5bXVq4RJ0eFSMQyxAlNF8mriwp8K3-OZD9h2hWI-j6YlgbGygTDNrYYyhHefvgFjpbGNuQMaO8un9gKuOnxnEohJFQhAfFwrBHQAqqFhM8Xj9KQA3EqCj-vDNAVGx18uuEOR3jzOVUANeENaRpNos8XN77UbnIcDA8ST6-z9odadh6DNUxdMyuJv4lVnsD1YB3MkYcSqMnEo_CDpOcsR1xVvcmhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این مطالبه‌ی جدی و قطعی مردم است! خونخواهی قائد شهید امت و مجازات عاملین جنایاتی که علیه مردم ایران به وقوع پیوست
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/672059" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672057">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd3kbcTztlDH0i3YCn2D8OiNy_Nlzbowz5qgZunoqKjG12IKEzJA-wx2KlmsTTPXFnlgHRR2xgdzQwA6GxGScXEbX7uTjaPqrAvn3oVfk8pBuat_esJklfJ1hcprs4oe4_c8uSpeZAbTOj9s2x3xdgkHb0U7Lm6yyfutcZhRM3buCB9BDEuOBc39rVUvGkQnNZrbIMbdOUCNB6C5HOGxLDfXgHPwMAdi2CGB4dvQVUtih0nJlihzcmil3Se0yxvG3hmYNL5XjLA5zfsqIkjwbsGB--X8Mi02---425Jwns3-GdwRoaXorS3w9KcXRk6tS48bJlaAgMP-GGdOrrkg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا مدعی تصرف یک نفتکش ایرانی شد  نهاد تروریستی «ستاد فرماندهی مرکزی آمریکا» (سنتکام):
🔹
این نهاد مدعی شده که نیروهایش در دریای عمان بر عرشه نفتکش ایرانی «ون یائو» فرود آمده و آن را بازرسی کرده‌اند.
🔹
به گفته سنتکام، این اقدام در چارچوب «محاصره دریایی»…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/672057" target="_blank">📅 12:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672055">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
هلاکت ۸ تروریست کومله در حمله موشکی به سلیمانیه
🔹
حمله به مقر گروهک کومله در روستای «زرگویزله» منجر به کشته‌شدن ۸ نفر و محبوس شدن تعدادی دیگر زیر آوار در مناطق کوهستانی شد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/672055" target="_blank">📅 12:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672054">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تشدید عملیات سپاه در اقلیم کردستان؛ هدف‌گیری مواضع تجزیه‌طلبان و تأسیسات گازی
المیادین:
🔹
عملیات پهپادی و موشکی سپاه علیه گروهک‌های تروریستی تجزیه‌طلب در اقلیم کردستان عراق برای سومین روز متوالی ادامه دارد.
🔹
این حملات علاوه بر مواضع تروریستی، تأسیسات گازی مهم منطقه که با پیمانکاران آمریکایی همکاری داشتند را نیز هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/672054" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672053">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcF6-lYdCN415gJfRJ_Yfxofte75fIFPJOEZ2fr8lHDun4dvHA7leYRB1pkVBJAtKouAWRPczYI44W8EJHEYtOGljOVhpYe1xIBr7detyP4g5wPxOb8VEh9ZMkR-IHtNn4W7IFtRf_DXLsBA6AcQd12UyCts7LZzwONbqhvI7gAzeBeLkUJNe2ZYHX1jvSOWfBOnzvQuiCTrYR5M8kcVk_4YIYddH8C7RsWni-_Q6BnKAURHEH9hVbNDZSzlTagZ_QG4ODg5rehj4dklA9fzpm2wNl2c3VotPwj0tC0QFDXBHG480ZlTD6Z-NxQT2RYIspwQYpoZK2m6dmlxU6p77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فصل پایانی امپراتوری آمریکا؛ ترامپ و کابوس جنگ زمینی
تحلیلگر آمریکایی:
🔹
ورود به یک جنگ زمینی فرسایشی، تیشه به ریشه هژمونی آمریکا خواهد زد و فروپاشی آن را تسریع می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/672053" target="_blank">📅 12:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672052">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
تجاوز دشمن آمریکایی در تپه الله اکبر بندرعباس/ ۷ نفر مجروح شدند
🔹
دقایقی پیش تپه الله اکبر بندرعباس مجددا مورد حمله دشمن قرار گرفت.
🔹
حجم این اتفاق به حدی بود که برق این منطقه در بندرعباس در حال حاضر قطع شده است، هدف مورد اصابت در این حمله یک دکل مخابراتی…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/672052" target="_blank">📅 12:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672048">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dr7R3WM4XGK-kq40X6KuJgy4WFISQmMck9zRp9YaOrKW1omY1TUd-ZIJG5AWCeA8gtQBCLZcMp7v2rzU9KxIjcmmWN3am_9Pnb7RbNock2Z1Gy8V3t71XQotE-LQKZiXZAjfXj3OU0TceDN22AQgMXRNi5ZEf--owQ9aU3WBi02y-km-_sHrggZdyF5KC86mBCaoYpSUtjujOypLvuOZCH7nXNxB2CQ_DuAvLB5-e08NbUb9R-bVw3RhrmCYjt6OYv9s3nC6riZmBJcjj7Nlxt_PgIuQF0UEoOyVXntg1Jb_mUcr52ww9geS0ZgpQPJukPLyxI7SgmqJL5L47RWm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYM04zD5XPSIUZGr_ZjwfzoH37bXt4ZfIksjvLYd6kTQRJ9K8A93o3N_IUhyEYwtW2kyYd9UL9ZNP5JXRzkmluj7n5npKgrHC50GbA0dNn_lrDA9bG7lp8L94z7G_1NgmoKbDMfAuKTwOHIlJ1iP701suMtRDQcSBzcO2gVChtFx3WEeeB21ESgU7gGcAVY8xvo8XBj6iDv0FsyQHPJQgI5wyg4Kf7wy1hOm7tHkNlX6EZrpUWEWI20Xt8l1bLdxqQSSdnX-B0u_5CTGALDerJ00K7imrjo6YuigxMm7TQWZuMoLFO3jYEII4omwswlMWHjXVCE7pjCvbhApzYRjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0vtZrQIkzZa9ahfCOm6_w8srsqw4LhqFdPxcJrBUxSEggAu9VK0l7a9AzzhRMOQpFiyi9oBbnCGxhq0rjSEVGqEMJWScVVS_-lZzKhZzFv1Uv13nQU1ti5QNjh7N491XUliRMHftdoUC5hdWGtpLGEcM3a4PDphKpXDQLcYvQvdfOiEX7DHv_lzx6UHl7HmPvAJFLKjUa90Cv8e0tl4-peL4H2TH8fnJHfJQS1CqJW7-2lVJU2hEKpoV7WVvRkY1qjrmYlu8NLpuxG_YkqfSvF5CUZd62GRprYjuEbd4pPECrr2y4ns4TqSEaMx1-DXSqAmjiNzLGevwOGmF8n2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjjS71GHEWN_QtI-UmE2ap_AoFtzPUYp5Aj3_w88WGRCb682T1phRVdReSbQJjfQdDP_fF3k2I55AmdQexOd8cwVqjpANCFQms7UsvzD0qBFKAy5B3gxcmi6aWVvcseX_9PMVPyWTEUNGqUSdEq3LDK6Vu1wz2CGf7v5yqaT995wC0xzf4yiPFmZ22oQ2T9WiuQFeVpeNPqCzWDuZz62pa9m7I4_fyRjsbvZRWyZr3Q-V9CH9aEvHweY07C5occOyEFjGn3u-C6HpLPDtULftjWdayQhW3KDWSWPvl8cLthe9RaCNg1PxJGEL6id723N4fR-i02yWSchfe6eXosUwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زیبایی کوههای مریخيِ چابهارِ ایران
🇮🇷
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/672048" target="_blank">📅 12:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672047">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7965901c30.mp4?token=s-nukAFs72NGnK5ob1oLj6aiDG1o6KL4_eSxueDmTRShmMMxT2AHfKo2JHqN9WwMx-MDrK19sXsuV7P_sbd59vQqZ-ELc8CVx240lEIeWvIF51spz631oho86uHqngjtTDnUCHCMKmTnfOsVE4Y8VSZkJPjkbbQ6JS1yXts1Rfe3ksFXLT1D6K8SaTD3wwg7O8Xl-ZF_MU_i86brVNOT-wgD6j2IGdEC8gC6ADm6p_7sUS_9g56Ku_62E1wXAFQbAqtDgiB1nPbqBLDS-5MiFd-rw1RJT476f-XyML18fbcGesnu9YeyambrWCD0eX-pjajHn7NS-395-LWXCZFPgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7965901c30.mp4?token=s-nukAFs72NGnK5ob1oLj6aiDG1o6KL4_eSxueDmTRShmMMxT2AHfKo2JHqN9WwMx-MDrK19sXsuV7P_sbd59vQqZ-ELc8CVx240lEIeWvIF51spz631oho86uHqngjtTDnUCHCMKmTnfOsVE4Y8VSZkJPjkbbQ6JS1yXts1Rfe3ksFXLT1D6K8SaTD3wwg7O8Xl-ZF_MU_i86brVNOT-wgD6j2IGdEC8gC6ADm6p_7sUS_9g56Ku_62E1wXAFQbAqtDgiB1nPbqBLDS-5MiFd-rw1RJT476f-XyML18fbcGesnu9YeyambrWCD0eX-pjajHn7NS-395-LWXCZFPgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امنیت خونه و محل کارت رو همیشه زیر نظر داشته باش!
🎥
💡
دوربین مداربسته لامپی V380؛ یک دوربین هوشمند در ظاهر یک لامپ معمولی!
✅
نصب آسان بدون نیاز به سیم‌کشی پیچیده
✅
اتصال به وای‌فای و مشاهده تصاویر با موبایل
✅
مناسب منزل، مغازه، دفتر کار و پارکینگ
✅
دید بهتر برای کنترل محیط در هر زمان
✅
طراحی لامپی و کم‌جا، بدون اشغال فضای اضافی
🏠
با این دوربین، هر لحظه از محیط اطرافت باخبر باش!
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۱,۷۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
همین حالا سفارش بده و امنیت محیطت رو بیشتر کن.
http://memarket24.ir/briefcart/180124/g-en50734</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/672047" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672046">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌
♦️
سپاه: سکو و موشک‌های هی‌مارس در کویت و محل استقرار نیروهای آمریکایی و ضدانقلاب درهم‌کوبیده شدند
🔹
در تداوم عملیات مقابله به مثل و پاسخ به جنایات جنگی شب گذشته، رزمندگان غیور نیروی زمینی سپاه در موج ۱۵ عملیات نصر ۲ با رمز مبارک "یامهدی ادرکنی" علاوه بر انهدام سکو و موشک‌های هی‌مارس در کویت، طی یک عملیات ضربتی پهپادی و موشکی چندین محل استقرار نیروهای آمریکایی و ضدانقلاب مزدور آمریکا و اسرائیل را درهم کوبیدند و تعداد زیادی از ضد انقلابیون و نیروهای ویژه آمریکایی را به درک واصل کردند. عملیات مقابله به مثل ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/672046" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672045">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw6Ks5DTIG3ibACpHCoertmTSyaJJj7hm_Dx0dXki9KqzBr_dxVhYycAtZXNy9HLjRZzmcFVXKgNYIAZWmZv0isr20q4MJHlXwZZD6DCvMufkOy8sTLJHQOz46P6pXt_7t5M8kwnPZjgtIoTBoyf94SCgj9lZfHcsuIwAAK_-qkBNOmycZk4UObYp956nswmGKOZ7s4_ORvR08jftAe5qv7JvWDFTYEUNsFGmlQWjjFdQKxOoJSS9Sxq8H60Weyd2ecDBSLo7XdMG1EB-0l_g6zcDzl1I_OpIWJOO0eO_FTJaghRb3J399_sprL-0ggELR9QgAvzbWWW0NZiJPfQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر توییتر: آمریکا شب گذشته وقت خود را صرف بمباران پل‌ها، بیمارستان‌ها و نیروگاه‌های برق در ایران کرد
🔹
در تهران باید این پرسش مطرح شود که چرا این پل هنوز پابرجاست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/672045" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672044">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mgfqhw1qyNVnB7_eRwJ6CqKUZ6u64-QOakqUM2FcY4BxWSpOvkzrZAHp1yDALMsBGvTVRpP74IMJywEToVyq_9kNhIxA8JkDgpWRVd0kk1HpFXnAAU58VAhz4jCJ0B5wDhVW-WhAXkPEHkkOeI9KRIM3rn7__EBh0sBuhfhNatcANKt27MhOmJWI59IV8K4WArRW6x3YOpAb_rBhjHpRPB_Trup17gGKJSKM1HjbQViGmbuJC9-SrfwKsF_gw4FETImMQy-RGqHQzwnFwW5fx9JQfpHRM705btdvuQrPt7pYlQym-mzEuNzx2eIcCefH0bWLsadqO5tnVi8k7k8p_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای: تخریب سه ساختمان در شهر نظامی زاید ابوظبی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/672044" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672043">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9321113987.mp4?token=T4rnJG_bP6Q-5wjwFxiemjSG3oTvd5pbHy3ckiH1kUGxHYjfiAXGmvaB48ZQNKpD5n1wQaCe8eiLNzDmPugkjj1aqV1yBoVs3Zs77eBvTZTH395f4n-ITwdo00ztG3s8Pb-8bHAtPg8IQHIvIeM7ED71TAZzK0OlU1IDjq3UaBxJLzsSY7HqZV9ulXCfvJZ4sgn2URsdH3ZwyWEgpuMg9Zu8RaeWd3j8BXx-7d6WvCSqpmwc7pmSbiSslr7FniR4_TmzqP0QVPLWriy_EBK4DFwju1XAPAlZWWG368FRDAcHPI2GVSJygeEOBs39ypVrHV4yoW0JvjrC0UbsMbJ82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9321113987.mp4?token=T4rnJG_bP6Q-5wjwFxiemjSG3oTvd5pbHy3ckiH1kUGxHYjfiAXGmvaB48ZQNKpD5n1wQaCe8eiLNzDmPugkjj1aqV1yBoVs3Zs77eBvTZTH395f4n-ITwdo00ztG3s8Pb-8bHAtPg8IQHIvIeM7ED71TAZzK0OlU1IDjq3UaBxJLzsSY7HqZV9ulXCfvJZ4sgn2URsdH3ZwyWEgpuMg9Zu8RaeWd3j8BXx-7d6WvCSqpmwc7pmSbiSslr7FniR4_TmzqP0QVPLWriy_EBK4DFwju1XAPAlZWWG368FRDAcHPI2GVSJygeEOBs39ypVrHV4yoW0JvjrC0UbsMbJ82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از اصابت به سامانه پاتریوت آمریکا در نزدیکی اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/672043" target="_blank">📅 11:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672042">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سپاه پاسداران: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن را هدف قرار دادیم  روابط عمومی سپاه پاسداران:
🔹
در واکنش به حمله اخیر آمریکا به زیرساخت‌های بندرعباس، در «عملیات نصر ۲»، پایگاه‌های هوایی آمریکا در اردن را با موشک‌های بالستیک و پهپاد هدف قرار داده…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/672042" target="_blank">📅 11:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672041">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سپاه پاسداران: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن را هدف قرار دادیم
روابط عمومی سپاه پاسداران:
🔹
در واکنش به حمله اخیر آمریکا به زیرساخت‌های بندرعباس، در «عملیات نصر ۲»، پایگاه‌های هوایی آمریکا در اردن را با موشک‌های بالستیک و پهپاد هدف قرار داده و چندین جنگنده و سوخت‌رسان آمریکایی را منهدم کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/672041" target="_blank">📅 11:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672038">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
قیمت بلیت اتوبوس‌های اربعین اعلام شد
مسیر تهران ـ مهران
🔹
اتوبوس ۴۴ نفره؛ ۱۲۵۰ هزارتومان
🔹
۳۲ نفره؛ ۱۷۰۰هزارتومان
🔹
۲۵ تا ۲۷ نفره؛ ۲۲۰۰ هزارتومان
مسیر تهران ـ شلمچه
🔹
اتوبوس ۴۴ نفره؛ ۱۳۵۰ هزارتومان
🔹
۳۲ نفره؛ ۱۸۵۰ هزارتومان
🔹
۲۵ تا ۲۷ نفره؛  ۲۳۵۰ هزارتومان
مسیر تهران ـ خسروی
🔹
اتوبوس ۴۴ نفره؛ ۱۱۰۰ هزارتومان
🔹
۳۲ نفره؛ ۱۵۵۰ هزارتومان
🔹
۲۵ تا ۲۷ نفره؛  ۱۹۵۰ هزارتومان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/672038" target="_blank">📅 11:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672037">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0cedef3b.mp4?token=s6RSaBDZ10LohfPjKSZBOp9FTXwxSD2LOAPxGiVFRRWts17QjXhvOodiC9WF1HpjH0Q2Tl_nRiWM5GpT-GSYG8KyXP9-b_Ve3S6DZ_3y8xp6DPMtfPBPGL7IYxkZYV-_nm0W63SYyHVHfWgkVDZx3mxTOAVHp6lb7N3VQv0gq6TXjFb4KONS7nSr8MOQryDDsJ4J98EfO1I64yYVdaD2f9ZJ92mfVZyC3C73RC5hjVrgTXG0FLgkwyF7yp9SqzFSOfZGtmEseRos7Gg88ceK4GpHtTQLp8w8P8BMSlks9aZIy1kbBPYFpgbdLHzjEuqiV9Sa2ualk7C5nF6gG9Uznig5jxop_148KIbdb68ZI27F89BHeuGKHK_CJF7ZjZuoH21lDdgVFegaLKg4unKxehJ8ofXayrnypndhJ0BJcD5nRaGHyyW7ZQbghLySJQJmhs1Jiroy_OawEBKNgRlNO1BMr8gjlCb3l4Osu_eb8DQXVGwlvqWbIBMEjMMvoOo1HQ7WVO1Tku0T62LER2UYUFo31Jmpjq8wLobBkL2N3hTKB9U77ipzqOdOzT_28vXj68rER966JAAfE92C80_Bf6Mbq5nPg7LbgtdkGb2xSm3JX6g3EBWgsDyovnCGThYIHXBBiK41sb4JlF6EXunBiNi-kVnkJgC69M3sgcByAec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0cedef3b.mp4?token=s6RSaBDZ10LohfPjKSZBOp9FTXwxSD2LOAPxGiVFRRWts17QjXhvOodiC9WF1HpjH0Q2Tl_nRiWM5GpT-GSYG8KyXP9-b_Ve3S6DZ_3y8xp6DPMtfPBPGL7IYxkZYV-_nm0W63SYyHVHfWgkVDZx3mxTOAVHp6lb7N3VQv0gq6TXjFb4KONS7nSr8MOQryDDsJ4J98EfO1I64yYVdaD2f9ZJ92mfVZyC3C73RC5hjVrgTXG0FLgkwyF7yp9SqzFSOfZGtmEseRos7Gg88ceK4GpHtTQLp8w8P8BMSlks9aZIy1kbBPYFpgbdLHzjEuqiV9Sa2ualk7C5nF6gG9Uznig5jxop_148KIbdb68ZI27F89BHeuGKHK_CJF7ZjZuoH21lDdgVFegaLKg4unKxehJ8ofXayrnypndhJ0BJcD5nRaGHyyW7ZQbghLySJQJmhs1Jiroy_OawEBKNgRlNO1BMr8gjlCb3l4Osu_eb8DQXVGwlvqWbIBMEjMMvoOo1HQ7WVO1Tku0T62LER2UYUFo31Jmpjq8wLobBkL2N3hTKB9U77ipzqOdOzT_28vXj68rER966JAAfE92C80_Bf6Mbq5nPg7LbgtdkGb2xSm3JX6g3EBWgsDyovnCGThYIHXBBiK41sb4JlF6EXunBiNi-kVnkJgC69M3sgcByAec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه فیک را از اصل تشخیص دهیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/672037" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672033">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kU66h9au4Dmq5VGpMjuqfTEzWJjj91Q9FH-s85cHAuPC5JeOFkG7sm9p0ZJksBkEW1xwGKykhU2CcsmNzRFFPs5VnXwX3CETPCG022Xtsy1u8GewmdkeWVqCAbSML13JjKZsvWmPVNGsy_de11Sl8W37wfYnK-DUpi15UWjeRvPzpZoV5ffNk4iP2Nb8IjPkxTuSzwz8Z2p29yAafN6uqhtEzhoCun8oVnK9siviu6NS-wz5WKWQE18gmkU28ax7IpHNz4iVhDA3_YWamsv4Jy_u1IuQ9r4fnV5SdIpxiJr_QUYgi40bTfAS5FpG7mdZGvFZ4_b-Q6uifyh8_I-FtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYdnfLLa9LtwFVxDMm-c5GWuEPF8oeEwKNcimv6kSXwDYlRse2hwCST0nsTHlYV4k8xVYPUZbO8rEi5fXemf2dZl_dTLgoh3lUDXxG_JyWvXMOnFGv9-f9-KWSR5X_5tt1q1EIu12fjqaMd7drKe6CFbKDfl7rFTjstTkZ-exiwW5m_W9gtkD2fMaGVKxxG8ER17b6MaLAsrD8wvptJAY3sKOP_A9_8hx0BTJIUg4Xp6pY2DsUiK0t5HZbvOe_f6xnNbMBVZ36E630EorWbqeD7vbuSftOx-fC7t_RRcFrWpfkc7vBGCda1X-xr_XcyNdnDilib_vA0-thYCh-YrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4Uvtu1E5WL-r7uUyw0G7r3WhwEw7q8Sik_Ls-7B6GstkY6J_FW_65ojy2rXWH1KfjHjlDy6O6o4HbJg67o94ROZu7qQOJKPZu1CwVvCpk5TdBfix97-KIagov2qUSVJs3CgwQbUmauJC81ZSMCY2SrEmYQfhJ6z1ChKhfo3PkYf84w8s8j80sK_tRJcFJVxSPsLPgvMoysevA92g449YSVxzD0WMFy8EYxOHXQ9iMt8t4P8aPVV5aKPlW5zidbLTaXCOjx291licDZFgSsNdwMaCbyzaawbCebX-ISDntj-D7bFoGxtZ8m8R_xMsr0jAa8fo58HvhHxiHsQF2VF1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4e6qTOoDBmegQGgYZPK9OnCIlonXdG-04xvdWshIYKODla7UIkPbEjq91VA7QnEdI23Ls8NtCfm_S7nxN9OdPWgRVNEUN2ACMmSghUbucTD_H4XCtUtw60N1mAHij03nfef-k3Gl4yn_pWiVVQIm2XCnqe54BAJIdNQzixidQuZw_hqKDKJqJpCNGaJJMbCcBPmSYeb_0RUGnOoe-3ajKCO9eVXmhqDooHHcvH_hZrBcve64ayVnKhZWieNMDMIfAb2CfgUMwjiRoXQ2kh4h-fCxEaxgs_4kmdbcfmiLzTWGH2vPhiltpjqSfIahtmPQLvDI_1ZCxJm7eOUZ1tIGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افزایش پروازهای نظامی آمریکا به
غرب آسیا
🔹
داده‌های منابع باز (OSINT) از اعزام دست‌کم ۱۰ هواپیمای ترابری C-17A از آلمان به پایگاه‌های آمریکا در خاورمیانه خبر می‌دهند؛ هواپیماهای اطلاعاتی و سوخت‌رسان نیز در حال حرکت به این منطقه‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/672033" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672030">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7GAZInypPYfZXkkC95iZVJG7GQqhjucVOuTeoCIzPA3yFvvs_O9SLwgKzYCcHOnd1cT6KvN7w_Q_MffWnsgcban-SE2I3IuJTl42Dj89oTdmfR0XYLS8qwoophgtIEHThF4FIqKPOlthDRbzIHcGLpnvAcwavObNqk_8M-21sbmgfIm6DVa3fbC4Ae9UvNIEIAhZEJhlVnIf3glcUMofgpdaGrq3cdC2aBY9u2kea-jHVPGYnqvqcL7LslMnZtfmJUIX20GgFU3YkuSGEmKN9Mr_FbiYLElK6PHH0-nTLqa6zQUMs10CbImWcMbtPKyKqco7wWX9MX36PEDCSg1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن شهید شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/672030" target="_blank">📅 10:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672025">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
حمله به نفتکش در شرق خصب؛ خسارت ساختاری به بدنه و سلامت خدمه
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از حمله به یک نفتکش در شرق بندر خصب عمان خبر داد که منجر به آسیب ساختاری شد؛ تمامی خدمه در سلامت هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/672025" target="_blank">📅 10:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672022">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaDm_XFydquA72RPeLIjzH8IlkQ-1DJ6-x_GzMr8A2g9kok-wRej0QPxH-T01oviP7C4Pw59I0tgYnIhW88UYakk1bAqPYsXpbN_-Y8t9JPhmhAv9tSvKuO-vhZSR0nKpXUp4E5iKjxB_oecpzBxxz1gac8qwoV48J5jCvfATEh55hKax-IdY4rUwLfF1f5Ft5bzLjqXZjeKcrIGMWXpGHYUnZiw6gJ2V_swKw6PTIubcCbdpbK13A-xQMEAQuZm0uTnW0GVRUQKaoVwoEH77dpEXEj4JezwZ-1RUaFCEcKP7PbrrkXocZcNvaDOG62acsLE4vWs8s6C9y_NY5nnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شب‌نشینی ماه و زهره در آسمان امشب ایران
🔹
ماه از غروب امشب در کنار پرنورترین سیارۀ آسمان یعنی زهره، مقارنه‌ای را با یکدیگر خواهند داشت که در آن تقریباً ۲.۶ درجه از هم فاصله دارند.
🔹
این مقارنه از حدود ۱۵ تا ۲۰ دقیقه پس‌ از غروب خورشید تا ساعت ۲۱ در قابل دیدن است و ستاره قلب‌الاسد را نیز می‌توان درست کمی پایین‌تر از ماه و زهره دید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/672022" target="_blank">📅 10:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672020">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufITZQWwVuQq1uTsW6dLDEB9Qya9Twm0l2VMQVWeQq-JwBV8vM2AXfAe1zvoXY2ygo2ZDD8d8gmXV7hcZNJ5YryV6YSEy-PTZC0FdzH_fREi1jkQo9LTFRlfTWCnqjLtRV_5uns6fx7UXhprm4i3iBl-w_eaIjfkoYsovus7qTKMLMESRUbw9TyW5EzYHwpRYecN3A_bm8oKbS83zhP_s-l2tyTxg0jC4XqG0wltuvWJYKj0MPsUnAFW_RwLEXLj552_RiwXvf8FgkW5uICo6VEIUpvNZnEepLxqpOuOWAZ7m_oZJtk6k7BpBrtYGpVO6BMgW0vPlLGw7X9EbuoRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما نفت کش تصرف کنید
ما جزایر قبلی مونُ رو ان شاالله</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/672020" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
