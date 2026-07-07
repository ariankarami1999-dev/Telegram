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
<img src="https://cdn4.telesco.pe/file/osdWt1GLC7NyW_x5VFgBwooyo6rUnF4bJBGE1lSt8yaqkk6BKtJolol1lI9i1kG7WeTmX8XWljmYa-KpL3jSyaNLhhuh5CmDIFMJwOHf-gD_A2r0ZprT7MEiRCGtX6KVubnCivqRF4xpLOI0nFBtVVu5F7_1NYAf36t1E14Xed-7-uyyTD9CLVtFjwHYMnOMgU3vqi3nPutrGcxPpcoKAffnIzn2Lu93C_kyJiu6ro5bNQm6J0n1rCF9guBQOQrHYE1XHxWJI4UdMCnm2jLnP8-X2b_vEORvuaVG06XtwoOPWdYW10UAXRf923PCYBK6M-EftC36TwPbqKerLh7Rjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 21:55:52</div>
<hr>

<div class="tg-post" id="msg-16673">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">داریم به این لحظه نزدیک میشیم. گفتم از الان داشته باشین، سیو کنین، چون اون موقع ممکنه اینترنتتون قطع باشه و نفهمین چی شده.
@withyashar</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/withyashar/16673" target="_blank">📅 21:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16672">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آرژانتین ۳-۲ زد جلو</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/16672" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16671">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کامبک سنگین آرژانتیتثن ۲-۲</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/withyashar/16671" target="_blank">📅 21:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16670">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مصر دوباره گل زد ( این دیگه درسته ) ۲ بر هیچ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/16670" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16669">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یک مسئول ترکیه‌ای به شبکه الجزیره گفت: رئیس‌جمهور ترکیه، اردوغان و ترامپ، مسائل مربوط به إيران را مورد بحث قرار دادند و بر لزوم یافتن یک راه حل قابل قبول برای جنگ و باز شدن تنگه هرمز تاکید کردند.
@withyashar</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/withyashar/16669" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16668">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مصر‌ ۱ هیچ جلو هست مسی هم همین الان پنالتی رو خراب کرد ! شخمی‌ترین جام جهانی تاریخه !</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/withyashar/16668" target="_blank">📅 21:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16667">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مصر گل دوم رو هم زد</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/withyashar/16667" target="_blank">📅 20:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16666">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مصر‌ ۱ هیچ جلو هست مسی هم همین الان پنالتی رو خراب کرد ! شخمی‌ترین جام جهانی تاریخه !</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/withyashar/16666" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16665">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نتانیاهو درباره ایران: توافقی بشه چه نشه  من هیچ‌وقت اجازه نمی‌دم ایران به سلاح هسته‌ای برسه، این دقیقاً همون موضع ترامپه
نتانیاهو : اردوغان فقط مشکلش با اسرائیل نیست , حتی یونان (که عضو ناتوه) رو هم تهدید کرده به نابودی
@withyashar</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/withyashar/16665" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16664">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو به سی‌ان‌ان: به رئیس جمهور ترامپ توضیح دادم که فروش جنگنده‌های اف ۳۵ به ترکیه توازن قوا در خاورمیانه را برهم می‌زند.
ترکیه جاه‌طلبی‌های متجاوزانه‌ای دارد و نیرویی حامی صلح و ثبات نیست.
اگر ترکیه هواپیماهای اف ۳۵ را دریافت کند، اقدامات متخاصمانه‌ای صورت خواهد گرفت
نتانیاهو : هنوز خیلی زود است در مورد آینده ایران صحبت کنم.
@withyashar</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/withyashar/16664" target="_blank">📅 20:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16663">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv81Dnl8cWvqGZzZPGBS60zl2HNX2Z3dQh8HToE5LikyYaAebAlXI5eqhyRu_xFrFA2eWlhWXBxdacHpdpA5wA69lBitf-As_lqjT_VF1iKf-RrS0KFQd9qs18Q8dz9AldFYIB2DHyh0EgtXJlmWAph9kBKc1nLnqMevF26WV3_p7u9xQjNDvAOLJL7SYJQQiwn8LdkzXbUWre-jyiGcdRCih2wQ5AQ7i3DNNboK8tW3gwx2oWfwN2cSp5kGc2fXIotrc6QFOydm_IGpK1KjgseY9MLPWRql5PZVtwq93unCMkyS_ySohanCq69zmpNkDAgamNPY9_xAteP0sd0BKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : هواپیمای بوینگ ۷۷۷ ماهان حامل جنازه خامنه ای تا دقایقی دیگر وارد نجف می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/withyashar/16663" target="_blank">📅 20:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16662">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hcip43WDUljTPrqaIlt1t8cC5dz9xiMJR-UOJKb2ZSpy4_sq87_FyQZYA_AH4I_xoCsgz3bbAN96Olf-JHmphS1lbZ1ArbUKg4itOQfyfzL_gzqxXJ4YchB7psXjpaMl0e1xawAbgT8_GoGTaWG_3oQrMPklbZo0mN67d559E2IuQjDdSD3XCSZeLNqy4W8oCS5Tfnx-dg5xfvb-xPGa0LZByCPLOZZajXV_NGG0kPvdIPYi_R64ya-_nwwzbcuUi5FrbIWDY2EH_E1SxEHYzI0ATDQW1dcAo4dDbblg4HdOOIzdBJNYCrS6mYxeu0CsqxvaYQR6HlgjmedmSP5tAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه گروه تندرو ناشناس برگه‌ای روی ماشین و خانه قائم پناه، معاون پزشکیان چسبوندن و به حذف فیزیکی تهدید کردن
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/16662" target="_blank">📅 20:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16661">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مصر‌ ۱ هیچ جلو هست مسی هم همین الان پنالتی رو خراب کرد ! شخمی‌ترین جام جهانی تاریخه !</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/16661" target="_blank">📅 19:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16660">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بلومبرگ:ایران به سازمان بین‌المللی دریانوردی اطلاع داده است که بر تنگه هرمز تسلط دارد.
@withyashar</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/withyashar/16660" target="_blank">📅 19:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16659">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مقام ارشد آمریکایی:ایران با شلیک موشک ها به سمت تنگه هرمز،یادداشت تفاهم نامه با آمریکا را نقض کرده است. @withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/16659" target="_blank">📅 19:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16658">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مقام ارشد آمریکایی:ایران با شلیک موشک ها به سمت تنگه هرمز،یادداشت تفاهم نامه با آمریکا را نقض کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/16658" target="_blank">📅 19:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16657">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ecd9127e.mp4?token=LU_ZUJJU-29oDej8uoegnaC_Yrn07PgHm3NQJub9qOzEMqhqu9_so6tO43qVBxx4czxTgDK97jCu_aGpOVDtAOjDWNSkJKXZLhKRKhmnvN10uJvXbQLKKyViL3gsFgQAu9-fYli8XippnLOvX_MT0s_himJGqfsM8cu0j50vbmesEsNym370AGr9_PpLHruGTCDNU4nbjjf957HcNrMfyi3EkKb6PoZEgtGfn4jkr-F5o0lmH-n1hp4jNQd4V5rZNh3ra-lIXQ9g6kvHObKwXSDIb7namalfYbzqAex-jeNKlLKEbfrUnmIXUL0H4zThijYFs4Zu1rgzLLnvaI2nzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ecd9127e.mp4?token=LU_ZUJJU-29oDej8uoegnaC_Yrn07PgHm3NQJub9qOzEMqhqu9_so6tO43qVBxx4czxTgDK97jCu_aGpOVDtAOjDWNSkJKXZLhKRKhmnvN10uJvXbQLKKyViL3gsFgQAu9-fYli8XippnLOvX_MT0s_himJGqfsM8cu0j50vbmesEsNym370AGr9_PpLHruGTCDNU4nbjjf957HcNrMfyi3EkKb6PoZEgtGfn4jkr-F5o0lmH-n1hp4jNQd4V5rZNh3ra-lIXQ9g6kvHObKwXSDIb7namalfYbzqAex-jeNKlLKEbfrUnmIXUL0H4zThijYFs4Zu1rgzLLnvaI2nzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکل زبون وا کرد
😩
@withyashar</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/16657" target="_blank">📅 19:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16655">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b528ebf23a.mp4?token=ksnFPAuyXHnoRgyk0mjU3FKqG8WSbB8Oi4LwkG_Hzceq5pBo373NupCL_YTTZH2Jwt_qb0N2tDpGdsfmYfFmYWPY4gPvM0xFNiPcUZ6uORwBPYLtX2GTTr1X4Utveh48qIzzhpVIhptEKz-dOrVtvNsFpWk0rnaxf974KCAick07RfKWpzCbfmXUCCRrBZFGmCe1Mn0oh584jSQ9pjA2Q5EAJAdvnZxbsl-1Vu0XKgPUf3lX_lp5WQrZKdbHuxZtYV_xAYTvSnWR7frN5I_W3vYh_ntBOWUr3Wn41K2pgXMAFOLJUat_tfEgpwkD49FnWgSHm-4CX9Xg-BhL7EO3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b528ebf23a.mp4?token=ksnFPAuyXHnoRgyk0mjU3FKqG8WSbB8Oi4LwkG_Hzceq5pBo373NupCL_YTTZH2Jwt_qb0N2tDpGdsfmYfFmYWPY4gPvM0xFNiPcUZ6uORwBPYLtX2GTTr1X4Utveh48qIzzhpVIhptEKz-dOrVtvNsFpWk0rnaxf974KCAick07RfKWpzCbfmXUCCRrBZFGmCe1Mn0oh584jSQ9pjA2Q5EAJAdvnZxbsl-1Vu0XKgPUf3lX_lp5WQrZKdbHuxZtYV_xAYTvSnWR7frN5I_W3vYh_ntBOWUr3Wn41K2pgXMAFOLJUat_tfEgpwkD49FnWgSHm-4CX9Xg-BhL7EO3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جایزه موش طلایی سیرک هم به این تاپاله میرسه
@withyashar</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/16655" target="_blank">📅 19:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16654">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شبکه ان‌بی‌سی به نقل از یک مسئول آمریکایی: ایران شب گذشته دو کشتی را با دو موشک که مسافتی کوتاه را با سرعت بالا طی کردند، مورد حمله قرار داد.
@withyashar
اتاق جنگ با یاشار : دو تا هم  الان زد ، پس امشب دکل سیریک و برای بار ۴۸ ام میزنند
🤒
🚨
@withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/16654" target="_blank">📅 19:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16653">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl-2ZtBDHaVPPZJDMrB-F9rINXPNFY0EgQ3X_3VIC3aln78inpYtCB-_5iJcMOuYRThfwFWM8-lfu1qMyIuoZM78tSKnWTuNFRLa6GksLbuaMKOgHVQ8hPErhaxXxV4sL7X04D0NHlAmQXG5x-gUmR30O01nXWhlS69Njxp-A7sfrAu8CLnTb5DoBSkrsxMrOswm3oU_uFl0xO3Ky6NbaIs4QxiHkOhQdBy8cGv8z-YeWauor067IBsAyHDcrHhrUDIapXGmBxod-3KZBY-ASkO5ESsZwUGa7Vs6zX_Tn0hFEb80Bq9L9sKHvvVHWQlbDkVGQraOO2qdgpRhZzQ9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اینم یکی از کشتیایی که دیشب بهش حمله شده، به وضوح نشتی سوختش مشخصه، قبلا خیلی گفتم ۳پا میخواد بخش جنوبی هرمز(مسیر عمان) رو باطل کنه و به طبع تمام ترافیک رو بکشه بخش شمالی برای ایران، اینجوری نبض هرمز هم دستشه
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/16653" target="_blank">📅 18:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16652">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk2Gu3R9KGfh8rO9qFTBYQHLoPDfi-qFoV8OMu5GugNEjyZsGOENb9I2KZh5kBLA6SoWvgxEP5okXzQuQ2vo3-Xor0-EKhlfXNiBHE3PEYZPgcZ2LbadQPdDfE32em-oPjzUCcDkISMW5CRbVxJ416-eGJvVg2c4haI4To9doUYjjEaHxefINHR1gzDWVxniuRwL6Qw7bPytjkCfUqnjnWSiZ8vieD2Tg0KOQ8ip4d-hAyVgV6GgvslWkIPXHj81Kd2R6e5kntYsNYoFfrB2TszZhxmWIXCdjzG2xEFNleghJ4sPt25ibDcA3DPCAny8rM9kbv9Y0LilRgS5rzkmpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حمله دیگر به یک نفتکش در تنگه
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از اصابت یک پهپاد ناشناس به یک نفتکش خبر داد.
این نفتکش هدف حمله یک پهپاد با هویت نامشخص قرار گرفته که منجر به ایجاد خسارات  در بدنه کشتی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/16652" target="_blank">📅 17:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16651">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک مقام ناتو به الجزیره گفت: رهبران این ائتلاف، در نشست خود که فردا چهارشنبه برگزار می‌شود، به موضوع تنگه هرمز و آزادی کشتیرانی خواهند پرداخت.
@withyashar</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/16651" target="_blank">📅 17:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16650">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گروه فرانسوی "مهاجرین" که از جولانی حمایت می‌کند، مسئولیت انفجارات در نزدیکی کاروان مکرون در دمشق را بر عهده گرفت
@withyashar</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/16650" target="_blank">📅 17:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16649">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">درگیری مرزی طالبان و ارتش پاکستان
منابع محلی در ولایت ننگرهار اعلام کردند میان نیروهای طالبان و ارتش پاکستان در نقاط مرزی شهرستان دوربابا تبادل آتش صورت گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/16649" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16648">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqqvLLdlNLXU0r-rhyruydF3Ri8e39Q7k6rp9JRbHWoxmJTfhkB8Lq-QcKKfQJMBAk_X2JKtXddUXzrwQBfa5F6CKxX8_bG81ZO94QkarLu4CLF52x84_SXjXTiYURKIhohqK-o6EaKQCSlbFPGewsvK49TP5TvL75iDPGTC7qfZrs1w-o1jzSHFI5Q1DaqLMw8WdCUcoBsF-frH9caVNJgeDze5niSUDbhw9zcIvzi-Q2yWCGSb2V4m9g9iBnLnssN4w_nKvpxMjDtONjgQXZPQCnPS0Hj6rLJPMfaNMp4Jio_mvnnq69qs6K6OnLi6rgYQ7vKEXMrMf7TmHMtTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات دریایی تجارت بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفت‌کش در حال عبور از تنگه هرمز دریافت کرده است.
این نفت‌کش مورد اصابت یک پرتابه ناشناس قرار گرفته و به نظر می‌رسد آسیب‌های ساختاری به آن وارد شده باشد.
@withyashar</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/16648" target="_blank">📅 17:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16647">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هم اکنون از سیریک صدای دعوا در تنگه شنیده شد @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/16647" target="_blank">📅 17:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16646">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دبیرکل ناتو: بدون اروپا، آمریکا نمی‌توانست به ایران حمله کند
رومانی بزرگترین فرودگاه‌های تجاری خود را بست تا به هواپیما‌های آمریکایی اجازه برخاست و فرود دهد
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/16646" target="_blank">📅 16:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ: ترکیه به خاطر من درگیر جنگ با ایران نشد و نمی‌خواهد شاهد دستیابی ایران به سلاح هسته‌ای باشد
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/16645" target="_blank">📅 16:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بدل موشتبی خامنه ای خودش دهن باز‌ کرد !
این ویدیو رو پرت کنین تو صورت عرزشی ها !
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/16644" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ به ناتو : کاری که تو ایران انجام دادیم، اصلاً به کمک هیچ‌کس احتیاج نداشت
حتی خودم هم کمکی نمی‌خواستم. البته قبل از اینکه برم، گفتن کنارمون هستن
ما هم تریلیون‌ها دلار خرج ناتو کردیم؛ برای چی
@withyashar</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/16643" target="_blank">📅 16:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16642">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور، آیا قصد دارید جنگنده‌های اف-۳۵ را به ترکیه بفروشید و محدودیت‌های قانونی آن چه می‌شود؟
ترامپ: ما قرار است تصمیمی بگیریم. فکر می‌کنم خیلی‌ها - می‌توانم بگویم، خیلی از افرادی که همین جا نشسته‌اند - بگویند چرا این کار را نکنیم؟
ما رابطه بهتری با ترکیه داریم و ترکیه از بسیاری جهات بسیار وفادارتر از سایر کشورهایی بوده است که فکر می‌کنیم وفادار خواهند بود.
و مطمئناً چیزی است که ما در نظر خواهیم گرفت - بله
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/16642" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16641">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">قطر: ایران مسئول حمله به نفتکش ماست
ما ایران را مسئول قانونی این تجاوز و خسارات احتمالی ناشی از آن می‌دانیم.
هدف قرار دادن نفت‌کش قطری هنگام عبور از تنگه هرمز، تجاوزی مردود به امنیت کشتیرانی است.
ما از ایران می‌خواهیم اقدامات‌هایی را که به امنیت منطقه آسیب می‌زند یا کشتیرانی را تهدید می‌کند، فوراً متوقف کند.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/16641" target="_blank">📅 16:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16640">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رویترز: نفتکش حامل گاز قطر که در تنگه هرمز هدف قرار گرفته، به دلیل آتش‌سوزی در اتاق موتور، در معرض انفجار است
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/16640" target="_blank">📅 16:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16639">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOf3-V2lCIBsOCBUZH-jHIZ5wa-CR_gWAHcXKxiE1utrbTsl1TiBw7hqaAEIMH35WK-Qiy78K9nAq_oosX9GLZpbttZkQ6n6MdX4SLXpOBbZvnKoPK01Zv7Nt-IIbgMV_ay5mhXsrUHa3GXg5aKwJmSVRcJX0NJSeX8EVwoxS-RaD83x2rqFNVTq7Wxf5peY-_Ch72rcw_UReYkYpWic0YTpWPPS4LeohgIXbbHmBmbD2OZFJIJt__CP_eRnJOnHX06jyLmJzNALOt8J7lf1xZYVhTO5npXz8YSikLHmXG1sQNvq9gtnuIyvFUnmGEffZULAAYxiSrD63BFoOO9ozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : کارخانه تویوتا از مکزیک به ایالات متحده (تگزاس!) منتقل می‌شود. یک معامله بسیار بزرگ. تعرفه‌ها در حال اجرا هستند!
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/16639" target="_blank">📅 16:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16638">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ارتش اسرائیل و شاباک : ارتش دیروز در شمال نوار غزه به دو پایگاه تروریستی حمله کرد ابتدا، احمد یحیی ابراهیم بتش، فرمانده یک گروه نفوذی در سازمان تروریستی حماس و در یک عملیات دیگر  جنوب نوار غزه، حمواده ابودقه، فرمانده یک واحد اطلاعاتی نظامی در این سازمان را به هلاکت رساند.
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/16638" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16637">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هم اکنون از سیریک صدای دعوا در تنگه شنیده شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/16637" target="_blank">📅 16:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16636">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bfc7d0dc6.mp4?token=V6TOHo6EsB8NX33aCZgJpwpgPq0oX4AmELLGcXPAEPrT4FsSELrd6lagX0ZWSv2gY7MOYAOGvPqDi3s5_IA_LP6GOpC7G5kTDFlo9C5giCm_7x3CjycTBX4F6wdc_e4Qw2nFiBOGhYv-9149i5k4-eg0pjh1VjcllMd36Q69aUtMINbPsyzO7G9I_L1ipOC4-VXsefWVzekqfqJ1l5SdEVtUFXz_TAaAunMtbXDVZwCL8i3gv5H39txGTLcWHyWg0MoACwQ4RM2B1ysiEvdhjPimerKDXPKEwGLM3BYM-YnHFgT9Y9hz_x9yMoAQNKebopqrmz4XLavbN9bizWl06Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bfc7d0dc6.mp4?token=V6TOHo6EsB8NX33aCZgJpwpgPq0oX4AmELLGcXPAEPrT4FsSELrd6lagX0ZWSv2gY7MOYAOGvPqDi3s5_IA_LP6GOpC7G5kTDFlo9C5giCm_7x3CjycTBX4F6wdc_e4Qw2nFiBOGhYv-9149i5k4-eg0pjh1VjcllMd36Q69aUtMINbPsyzO7G9I_L1ipOC4-VXsefWVzekqfqJ1l5SdEVtUFXz_TAaAunMtbXDVZwCL8i3gv5H39txGTLcWHyWg0MoACwQ4RM2B1ysiEvdhjPimerKDXPKEwGLM3BYM-YnHFgT9Y9hz_x9yMoAQNKebopqrmz4XLavbN9bizWl06Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب سنگ به سوی وزیر امورخارجه ، عراقچی که با چند متر اختلاف به ماشین کنار وی میخوره
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/16636" target="_blank">📅 15:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16635">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f08747f0.mp4?token=i9lo8TUrUTxeJ7589qXVr3J7Rr6nDF2EehHIQu55-Ee1w-y8CSGDFrP8UW2arQeTkF-m-YK9WktSgljEeeL3i1J19XA1h1_mPSvvmNZYFl8Sci1BXT8flZklfau54KbJ--XC88Uzzj4N89VcYKXKrjdiETYmkicHYqUea7Ogr8MYfrNb580vg7egpj3AwAVXNYGfgY1rSXoWA1hnhKAO6c4VRyG7Pz4CQIQNmrBv-PqQDnfpe59uer3BUumsOuOTYPZHnP7FRWCR-55cUe54rIRa9sOjV2GNFAS1erSGHT5HAmm5cGYa9W7zyEOgMFy80R0yTuxp0PGpu6VgDcQa3TqRQsJ6DiVnUozoiNM0oDvyLlKgXORiu9TnF8Y_e0nF0bmuVd-1Rsh_8AFe3tCxbAYcHhUspz8qtM6YvT4UNjGi82qjc7rY9V2LwHydrMslh16qjuPgjGaHzFN5BzGIw1TD931W_-IYng5Xfif9AlfcbW79vuwZmKNqjQmFvI7ZaeAAlpJVB25lb8pPY--UWgSaOiOfblFMyHCZTdYzlRpKiKdj2XjFWDRaMmv5Rv4vJkoJLjT0VJP1Y1vkozMQGpSd4MfnGivSTs_KcoeWBrcLjTRaIxJ_mhgsUCtGpsW_X5cECNVwV-XfMtCevkiKDqqW9D4ghwF7KPEiAbqj87o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f08747f0.mp4?token=i9lo8TUrUTxeJ7589qXVr3J7Rr6nDF2EehHIQu55-Ee1w-y8CSGDFrP8UW2arQeTkF-m-YK9WktSgljEeeL3i1J19XA1h1_mPSvvmNZYFl8Sci1BXT8flZklfau54KbJ--XC88Uzzj4N89VcYKXKrjdiETYmkicHYqUea7Ogr8MYfrNb580vg7egpj3AwAVXNYGfgY1rSXoWA1hnhKAO6c4VRyG7Pz4CQIQNmrBv-PqQDnfpe59uer3BUumsOuOTYPZHnP7FRWCR-55cUe54rIRa9sOjV2GNFAS1erSGHT5HAmm5cGYa9W7zyEOgMFy80R0yTuxp0PGpu6VgDcQa3TqRQsJ6DiVnUozoiNM0oDvyLlKgXORiu9TnF8Y_e0nF0bmuVd-1Rsh_8AFe3tCxbAYcHhUspz8qtM6YvT4UNjGi82qjc7rY9V2LwHydrMslh16qjuPgjGaHzFN5BzGIw1TD931W_-IYng5Xfif9AlfcbW79vuwZmKNqjQmFvI7ZaeAAlpJVB25lb8pPY--UWgSaOiOfblFMyHCZTdYzlRpKiKdj2XjFWDRaMmv5Rv4vJkoJLjT0VJP1Y1vkozMQGpSd4MfnGivSTs_KcoeWBrcLjTRaIxJ_mhgsUCtGpsW_X5cECNVwV-XfMtCevkiKDqqW9D4ghwF7KPEiAbqj87o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال اردوغان از ترامپ در فرودگاه آنکارا، همینطور حضور سربازان ناتو با یونیفرم جنگ جهانی دوم.
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/16635" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16634">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">علیرضا فغانی کاندید قضاوت فینال جام جهانی 2026 شد.
@withyashar
🏆
😍
💥</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/16634" target="_blank">📅 15:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16633">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedf1332c.mp4?token=Y0lJ5K3F7T9LChcfpAhwOaeedV3KCGxRGjAvtslSj5vI9cAXYBEcmWHjlDgAk4Zp_uUAbxf1N4cI21ezN6w-JA99M3BQIyBr_aEggVmGwUmWFRysWyDOkoOJSlZyOYdc7w1Og0OC6Z7I9aAcjZe6HZ1sEvoSWT5bR1uk5ccrrK6v_2g0xmH0x8IRhx_uYeqfNoK3sz7iOSBQOE2f_Bo_FB79ld0M-GYR0yiiwrrP23cDmMs__yVW28YDkZgNQmL7Vfh6NYBl6S8SVkZLASSuWDMUxiak7I6BMsKIMUup787fskyEvIbYHVLFG_5XQchGo--iJ2tbn8KRxwy_RPaREg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedf1332c.mp4?token=Y0lJ5K3F7T9LChcfpAhwOaeedV3KCGxRGjAvtslSj5vI9cAXYBEcmWHjlDgAk4Zp_uUAbxf1N4cI21ezN6w-JA99M3BQIyBr_aEggVmGwUmWFRysWyDOkoOJSlZyOYdc7w1Og0OC6Z7I9aAcjZe6HZ1sEvoSWT5bR1uk5ccrrK6v_2g0xmH0x8IRhx_uYeqfNoK3sz7iOSBQOE2f_Bo_FB79ld0M-GYR0yiiwrrP23cDmMs__yVW28YDkZgNQmL7Vfh6NYBl6S8SVkZLASSuWDMUxiak7I6BMsKIMUup787fskyEvIbYHVLFG_5XQchGo--iJ2tbn8KRxwy_RPaREg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان در فرودگاه از ترامپ استقبال کرد
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/16633" target="_blank">📅 14:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16632">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">در سال ۱۹۷۵، زمانی که رضاشاه به همراه همسرش به ترکیه آمد، همسر فاروق کوروتورک، رئیس‌جمهور وقت ترکیه، سرویس کامل اتاق خواب خانه شخصی خود را به کاخ چانکایا برای ایشان منتقل کرد، چون در آنجا امکانات مناسبی وجود نداشتیم.  اما امروز، خوشبختانه، با همه امکانات موجود،…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/16632" target="_blank">📅 14:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16631">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a9d31515.mp4?token=VzfvcFOQsT4nN308uZ_NhZ0aLSFvucOgknHr71lDWqdflluxaRfu5SMYjjpVgmMx0bzF-KUOJsh9t7i8sOUbba2SqVBbmQ2qPEtc9Yadi3cw4S3PLZ7dOjj9irx6lgFq6rlhyFP7voOolM5kh8DtEyXYGaBg2RaasFsBkdmcB3gjNk-Q7XNEhkrw8koDR43uptX9-y8ZUjurKfn2MUvkDjSjPEb_zDhU4H5Hpdv_B_oIy6e3PIE-A87-3ErWloxprDV6jWkhwPdllba8vhVrUElZSYZ26AIEApvrnyefXWO0czt3d8KbnDPAQjAXggof0k-KJ3S-QfQKG8xISbHP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a9d31515.mp4?token=VzfvcFOQsT4nN308uZ_NhZ0aLSFvucOgknHr71lDWqdflluxaRfu5SMYjjpVgmMx0bzF-KUOJsh9t7i8sOUbba2SqVBbmQ2qPEtc9Yadi3cw4S3PLZ7dOjj9irx6lgFq6rlhyFP7voOolM5kh8DtEyXYGaBg2RaasFsBkdmcB3gjNk-Q7XNEhkrw8koDR43uptX9-y8ZUjurKfn2MUvkDjSjPEb_zDhU4H5Hpdv_B_oIy6e3PIE-A87-3ErWloxprDV6jWkhwPdllba8vhVrUElZSYZ26AIEApvrnyefXWO0czt3d8KbnDPAQjAXggof0k-KJ3S-QfQKG8xISbHP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سال ۱۹۷۵، زمانی که رضاشاه به همراه همسرش به ترکیه آمد، همسر فاروق کوروتورک، رئیس‌جمهور وقت ترکیه، سرویس کامل اتاق خواب خانه شخصی خود را به کاخ چانکایا برای ایشان منتقل کرد، چون در آنجا امکانات مناسبی وجود نداشتیم.
اما امروز، خوشبختانه، با همه امکانات موجود، از تمام رؤسای کشورها به بهترین و امن‌ترین شکل ممکن پذیرایی می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/16631" target="_blank">📅 14:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16630">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/16630" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16629">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=jKn1qspfKlQV9SPg6HabDCepb2lnBJPyiYA6W9fQ_cvOwC5U25vi99pB2yDxNKcgSmASYq2uPlLKMzJMZtphCba3NO_UaUAfysiomBbfn5cEl32CFyxfI68N04ZnlayQo-RHP6Maxt9uXpFBgta4hHqx_cdC-KT2NnaTxKbwahnK_V3JR6azXF3Vc1pYSWf72Cmd3u95B8fCCBSYMvGfzy83XBTqrLiDntrWxZY4-EQ7WjARB_6XbH1Iv6ZGClRjvcFjzagT3FlujPTqSSHiTsPyIy7lbtX7xnt8S_0cn6lguWt1bK-VLuf-NOZN0Fg17w1YOxDOFTUzGR27iHIafRirPbCVKW3R0Dg3EuoIpaXLIRBKWP3rOw1c1q8yOe2LO9eZ_KMmxumBkRbIXaEOnxSQesHNZ2MKN8z5dqFH69_tE21Uzr-Mn1KBxBnWHFDhRXNia8pg9_nJOcvTiDeyJQEvb_aASzkeoN5bx-ZD0D-NAT3cZgM3IoC3JU90VzLATvRvnFutaa2mCNOj1FM1DGvzWjqFNBwHMxSyfSH6apR8aC1-QqQo-hFTj9GOI2blu3eG_pI5y8BmwRIIVeQDSSdk0R50kwt8Vvv5yy9pPHGzLA3xQ9yye9qzg5eLTGgTStGQ-JXMln5hc7xlrBN9SfHVQqwcV8zakcH_kfB3OTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=jKn1qspfKlQV9SPg6HabDCepb2lnBJPyiYA6W9fQ_cvOwC5U25vi99pB2yDxNKcgSmASYq2uPlLKMzJMZtphCba3NO_UaUAfysiomBbfn5cEl32CFyxfI68N04ZnlayQo-RHP6Maxt9uXpFBgta4hHqx_cdC-KT2NnaTxKbwahnK_V3JR6azXF3Vc1pYSWf72Cmd3u95B8fCCBSYMvGfzy83XBTqrLiDntrWxZY4-EQ7WjARB_6XbH1Iv6ZGClRjvcFjzagT3FlujPTqSSHiTsPyIy7lbtX7xnt8S_0cn6lguWt1bK-VLuf-NOZN0Fg17w1YOxDOFTUzGR27iHIafRirPbCVKW3R0Dg3EuoIpaXLIRBKWP3rOw1c1q8yOe2LO9eZ_KMmxumBkRbIXaEOnxSQesHNZ2MKN8z5dqFH69_tE21Uzr-Mn1KBxBnWHFDhRXNia8pg9_nJOcvTiDeyJQEvb_aASzkeoN5bx-ZD0D-NAT3cZgM3IoC3JU90VzLATvRvnFutaa2mCNOj1FM1DGvzWjqFNBwHMxSyfSH6apR8aC1-QqQo-hFTj9GOI2blu3eG_pI5y8BmwRIIVeQDSSdk0R50kwt8Vvv5yy9pPHGzLA3xQ9yye9qzg5eLTGgTStGQ-JXMln5hc7xlrBN9SfHVQqwcV8zakcH_kfB3OTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ همکنون در آنکارا به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/16629" target="_blank">📅 14:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16628">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رئیس‌جمهور آمریکا برای شرکت در اجلاس سران ناتو، وارد پایتخت ترکیه آنکارا شد
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/16628" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16627">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ7ifgJwnfVggHDzuGrwCtfTBIRHRseHYALbntKxnGDxdjfpti0YqA6ZH6gMzteZjls7haUnJ___PKyglNM3Z9kug88f1bWP21LA8O6CXifaeTA7nxK1u5bF3En6sjrETOBuGXNaQydouTaz-zxQHVJAPlybol6HJKcFAYmaEf9E67Gnsbt4Jyo8oj_dhZRTq6OjxpuZbVKq4CahdE4zlX2y58fIIyTVmKwMMMK6T6ZwWor-TJyM_e5oCZNjjk0V7lDbuvmlTTQw0YfIgXVzrsYWxyhyd6d7OnRChLl_9zoEPGskgpRqjWDziU3S3X_LHULPRFfIyleyD_oEVXAkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با هواپیمای ایرفورس وان جدید هم اکنون در حال ورود به آسمان استانبول است و حدود چهل دقیقه دیگر در فرودگاه آنکارا به زمین مینشیند.
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/16627" target="_blank">📅 13:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16626">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">منابع امنیت دریایی: یک نفتکش نفت خام با پرچم عربستان سعودی در نزدیکی تنگه هرمز در نزدیکی عمان آسیب دید، پس از آنکه یک نفتکش LNG در همان منطقه مورد اصابت قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/16626" target="_blank">📅 13:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16625">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfVLnW7NAwiGyT79VHbsUTxo_iUfVUG-T19k13EW6Iz4U0eBY2aIM9n-cKOCf6cMESGRY3f7aKE_F-BQAzi7jUfzmEjwhRyQUCNNB_vr0XqezeRLefX9LXAB8i3JtwzmkKe49xL30B-NVA31p04QRPbkXd_MEs3q6qmNuZq6ROQlD1upzDkM8SzohFHxRDegENXQ4SVjLQ4R4kNiOeHsqLt38qbySIbiyQeQKrLICGvMWobUsC56pP-SqPJzBUzYN6k5S-532Fv-La5yYkdd2n_p7E0YoocEFz55aDHkJ62Z9wP6CQXq5M_RBE5izYrm0m3BBkX6pRaR6wOveOZqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا هر وقت این کامیون عجیب و ماجرای تابوتهای یخچالدار را میبینیم ، یاد فیلم «سرباز جهانی» محصول سال ۱۹۹۲ می افتم که داستان دو سرباز آمریکایی را روایت می‌کند که در جنگ ویتنام کشته می‌شوند، اما اجسادشان در قالب یک پروژه فوق‌محرمانه ارتش بازسازی شده و به سربازانی با توانایی‌های فرا انسانی تبدیل می‌شوند. این نیروها با یک کامیون بسیار پیشرفته و مجهز جابه‌جا می‌شوند که درون آن محفظه‌های سرمایشی یخی ویژه قرار دارد و سربازان هنگام نداشتن مأموریت در آن‌ها به حالت ریکاوری نگهداری می‌شوند چون گرما ضعف این پروژه بود.
امیدوارم موشتبی خامنه ای‌ رو هیچوقت نبینیم و زنده نشه
😂
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/16625" target="_blank">📅 13:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16623">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7801177f00.mp4?token=o2Mm8k3tbLEtRW2wsM0bnQihkectOsfUhrUuC2TOjBe6QiGzlhbglgi0SYbDmX70Wc0AL_veIKqlnSQLWq_cSIZzzm61m_y_xNlaXWZ9lfa_3oiA-e8dT-OVa7wNbLQg5siqI86IQxxX8e2QSDcZGNNk4nlw7jA5gCp7y-GZkpTKO6sAI843ppuFpEmN_2-Uz4bMn108jVU0TZqIP7EJ1TTM2Y21CgNhZZXNM9a3K08RMNP__oWt8AyCkq5OkUMAK9_2Hb0R21A2I_I98UoKuPa-5-5D4pSLd4fTZsNBYrALeMP5kGqdJhnSNzyZm5ZA7I2Tpq2RTGbPTFarsAgUpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7801177f00.mp4?token=o2Mm8k3tbLEtRW2wsM0bnQihkectOsfUhrUuC2TOjBe6QiGzlhbglgi0SYbDmX70Wc0AL_veIKqlnSQLWq_cSIZzzm61m_y_xNlaXWZ9lfa_3oiA-e8dT-OVa7wNbLQg5siqI86IQxxX8e2QSDcZGNNk4nlw7jA5gCp7y-GZkpTKO6sAI843ppuFpEmN_2-Uz4bMn108jVU0TZqIP7EJ1TTM2Y21CgNhZZXNM9a3K08RMNP__oWt8AyCkq5OkUMAK9_2Hb0R21A2I_I98UoKuPa-5-5D4pSLd4fTZsNBYrALeMP5kGqdJhnSNzyZm5ZA7I2Tpq2RTGbPTFarsAgUpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات بالاخره تپه علی الطاهر در جنوب لبنان توسط ارتش اسرائیل فتح شد
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/16623" target="_blank">📅 12:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16622">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0122a2f81d.mp4?token=NHeMmQ9Ytv5kKTYRdRQ_OLvPLNhJlfI_3lYUypLGsR0UUL-ntkklOTy5yFSdOkhL_HVt_69DheuVxJwt9cLzPxJz70EYxAt0vwueTC6t30MhZjm3Gqsfp7QtKRKAKlMwlGltsplHPV8Tw0OQFPT90FWt9CFEIowM87QZ65zNv56eGFnAigElbSkJyymGJtQQIR27Nik-HXgDvgJogeXfslhbs-uipJJ0b6TO26mMqx_S2RPuaIhN5EM0Vi6TXefRxNWQyrxZQCDaJgSrnkndVf5zCSTklxyklsVo6NspAzgwSKIbWo_av7gLKgyJL5et74PA0m9-HcFthunK5KhquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0122a2f81d.mp4?token=NHeMmQ9Ytv5kKTYRdRQ_OLvPLNhJlfI_3lYUypLGsR0UUL-ntkklOTy5yFSdOkhL_HVt_69DheuVxJwt9cLzPxJz70EYxAt0vwueTC6t30MhZjm3Gqsfp7QtKRKAKlMwlGltsplHPV8Tw0OQFPT90FWt9CFEIowM87QZ65zNv56eGFnAigElbSkJyymGJtQQIR27Nik-HXgDvgJogeXfslhbs-uipJJ0b6TO26mMqx_S2RPuaIhN5EM0Vi6TXefRxNWQyrxZQCDaJgSrnkndVf5zCSTklxyklsVo6NspAzgwSKIbWo_av7gLKgyJL5et74PA0m9-HcFthunK5KhquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم مثل تهران دیدن جمعیت کمه
در مسیر فیلم خورش خوب نیست کامیون ضریحی جنازه ها رو از وسط راه اصلی خارج کردن و از یه مسیر فرعی بردن
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/16622" target="_blank">📅 12:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16621">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مقام ارشد آمریکایی به آکسیوس:
ایالات متحده با حملاتی علیه اهداف ایرانی،انتقام حمله به نفتکش ها در تنگه هرمز را خواهد گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/16621" target="_blank">📅 12:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16620">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a7de57d9.mp4?token=A9gtdLoR6h9-sf5Am3ZTcYO9Yh6hDoyDosrIU0FtWSi25aRTy3TZ9i1XZcjX93FoMW1z9g9s8ECevP9OOeUduDiXx7-NKvDGaYvW3cztjuWfNW8hN0AuMrW7vAh7hUZz3sjSY6VQj_MsZo3EwspCv4TJLrxMxq8y8-inTz7ZhqmXw_6HHPcS3cOLaTZ_ExJQhsKv1N3NIVSpXj4O6nkPUlB3mbwgFh8PYquJYtbB_E3QQ6Ro58orTsONvwoDIm3asNBAU7RfVdM9wyz33s7cdwcPBMCPqzDdRvnQgWiufaZvZcQNzpCbL-BIdLP--7o3AFcPvc-tApUJ1qABciOKSocVYm4qna24nhP7Z7BToPwdWMadNMfphyTI08FU2LtezkgX350U2wHIIiXqyOl7H8Is-85IeudcGmJ9VkAz5KPXwQ2X1HI9i2IAGjewYBVr9erNb6ZXU-NUe8Nr4O4Dpl8aE1_gaByaXpgoP55LloAwRJimLcecNN6qU4n5Cu1tkuO0apTElBHuBEo7Bt3jjb-8Rhe7TK2KP9w7vmOYzv4bAUHfH6epbnexQtJi8zSfEo3oa3VItwSgyXLcwfmJW3sWqgQd4fQ9pPPKMS6sCfWtvKYn6Ypcr_NwrA3RLkuQMI-hesG3hr6UGpT-lygNIluNAP-fIZOsBOz4rY6CcBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a7de57d9.mp4?token=A9gtdLoR6h9-sf5Am3ZTcYO9Yh6hDoyDosrIU0FtWSi25aRTy3TZ9i1XZcjX93FoMW1z9g9s8ECevP9OOeUduDiXx7-NKvDGaYvW3cztjuWfNW8hN0AuMrW7vAh7hUZz3sjSY6VQj_MsZo3EwspCv4TJLrxMxq8y8-inTz7ZhqmXw_6HHPcS3cOLaTZ_ExJQhsKv1N3NIVSpXj4O6nkPUlB3mbwgFh8PYquJYtbB_E3QQ6Ro58orTsONvwoDIm3asNBAU7RfVdM9wyz33s7cdwcPBMCPqzDdRvnQgWiufaZvZcQNzpCbL-BIdLP--7o3AFcPvc-tApUJ1qABciOKSocVYm4qna24nhP7Z7BToPwdWMadNMfphyTI08FU2LtezkgX350U2wHIIiXqyOl7H8Is-85IeudcGmJ9VkAz5KPXwQ2X1HI9i2IAGjewYBVr9erNb6ZXU-NUe8Nr4O4Dpl8aE1_gaByaXpgoP55LloAwRJimLcecNN6qU4n5Cu1tkuO0apTElBHuBEo7Bt3jjb-8Rhe7TK2KP9w7vmOYzv4bAUHfH6epbnexQtJi8zSfEo3oa3VItwSgyXLcwfmJW3sWqgQd4fQ9pPPKMS6sCfWtvKYn6Ypcr_NwrA3RLkuQMI-hesG3hr6UGpT-lygNIluNAP-fIZOsBOz4rY6CcBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس شبکه ۱۴ اسرائیل، درباره مجتبی خامنه‌ای : اون هنوز زنده‌ست
- از مخفیگاهش بیرون نمیاد و می‌ترسه، اما تو دورِ بعدی درگیری‌، یه بمب اسرائیلی به سراغش میاد
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/16620" target="_blank">📅 12:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16619">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید @withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/16619" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16618">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">به ادعای رسانه ها دولت مصر با یک تصمیم سیاسی، تمام برنامه‌های سالگرد درگذشت محمدرضا شاه پهلوی شاهنشاه فقید ایران را که همه ساله در مسجد الرفاعی برگزار می‌شد لغو کرده است.
‏همچنین گزارش شد که از سوی مقام‌های مصری به وزارت خارجه این کشور ابلاغ شده اجازه ورود چهره سرشناس مخالف حکومت ایران به قاهره داده نشود.
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/16618" target="_blank">📅 11:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16617">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ: کنگره باید بودجه ۳۵۰ میلیارد دلاری دفاعی را تصویب کند
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/16617" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16616">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شبکه الخدث عربستان سعودی گزارش می‌دهد که رئیس‌جمهور ماکرون، ربع ساعت قبل از وقوع انفجار، هتلی را که در دمشق اقامت داشت، ترک کرده است.
در سوریه‌ نیز گزارش شده است که رئیس‌جمهور احمد الشرع، دقایقی پیش از رئیس‌جمهور ماکرون در کاخ ریاست‌جمهوری در دمشق استقبال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/16616" target="_blank">📅 11:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16615">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=cY5HfH24JfM9wAX2nvGq6bot12e4eYCK9ZmISYxBov9EOPBJFJ5-OrjXoGTX9PDhNBy-76vZOOI5h5D2LlM_LbjHnzTT0HgU-dKSQRsD8EntCNmuHGSIFEUCPRCXckYHy-LRzIZS3Jxpz34Dm9JLeBhNPzTBWICrsixOugTRIk-qKnxYlMnWY8045ragoVvGq27nSJkWlX6GjTdBHuIhfHpvAd0CMHj6bTvL8832ukgNLx8UHqdl2E4ZurP-Nlmm5HUDcBAgvMvrFYPJDtHAJB1YtSm-Pq1ZoOMOoUPW01_e6CkoGT7kzeL49TlrGPuTwIo6oLrgwCFOLQwAxiJ15Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=cY5HfH24JfM9wAX2nvGq6bot12e4eYCK9ZmISYxBov9EOPBJFJ5-OrjXoGTX9PDhNBy-76vZOOI5h5D2LlM_LbjHnzTT0HgU-dKSQRsD8EntCNmuHGSIFEUCPRCXckYHy-LRzIZS3Jxpz34Dm9JLeBhNPzTBWICrsixOugTRIk-qKnxYlMnWY8045ragoVvGq27nSJkWlX6GjTdBHuIhfHpvAd0CMHj6bTvL8832ukgNLx8UHqdl2E4ZurP-Nlmm5HUDcBAgvMvrFYPJDtHAJB1YtSm-Pq1ZoOMOoUPW01_e6CkoGT7kzeL49TlrGPuTwIo6oLrgwCFOLQwAxiJ15Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تصاویر ماهواره‌ای رویترز از تهران در بهترین ارزیابی حدود چند صد هزار نفر را نشان میدهد
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/16615" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16614">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=VrLE1HOGvxh5_IvBgqoY6n8omcEXP9wA-qsxd2SdUopEqS9MhbTyLF4C_BZZKA8EbVY4PZufUm7Qr46HxrrgpcWxNwP8IjWXaXS7NQMHkrIa_NCIa3TdNxHFlfYtVIzr-MQpnkuguQ3en7J1A05J2Ac9d8RQp658Lsge19rDW8J8JqGPFTHRnwbb44f1gXPXn3on7eISERX3ecE9ak1yXAB-5LcGIsfwDukG65zAyJBxGECPDs9xul_NeTtPekU6iPqcJw0GU6BhoCoRC3qi9abByC5XRivWoq_nkiJhzyE-_b48Vbw_BXWmUxFrSAkBeUdnz11nyWlLlEzLd_KAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=VrLE1HOGvxh5_IvBgqoY6n8omcEXP9wA-qsxd2SdUopEqS9MhbTyLF4C_BZZKA8EbVY4PZufUm7Qr46HxrrgpcWxNwP8IjWXaXS7NQMHkrIa_NCIa3TdNxHFlfYtVIzr-MQpnkuguQ3en7J1A05J2Ac9d8RQp658Lsge19rDW8J8JqGPFTHRnwbb44f1gXPXn3on7eISERX3ecE9ak1yXAB-5LcGIsfwDukG65zAyJBxGECPDs9xul_NeTtPekU6iPqcJw0GU6BhoCoRC3qi9abByC5XRivWoq_nkiJhzyE-_b48Vbw_BXWmUxFrSAkBeUdnz11nyWlLlEzLd_KAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند انفجار در دمشق، در نزدیکی هتلی که رئیس‌جمهور فرانسه، ماکرون، در آن اقامت دارد.
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16614" target="_blank">📅 11:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16613">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک منبع امنیتی ارشد لبنانی امروز به روزنامه "ال-جوماهوریه" لبنان گفت:
"ما در صحنه، هیچ اقدامی از سوی اسرائیل ندیدیم که نشان‌دهنده عقب‌نشینی از مناطق مشخص شده در توافق‌نامه باشد. برعکس، شاهد تشدید عمدی تنش‌ها هستیم."
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/16613" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16612">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رویترز به نقل از یک منبع امنیتی: انفجاری با استفاده از تعدادی مواد منفجره در نزدیکی هتلی که ماکرون در آن اقامت دارد، در دمشق رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/16612" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16611">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">صداوسیما : نفتکش هدف‌گرفته‌شده در تنگه هرمز پس از نادیده گرفتن هشدارهای مکرر مورد اصابت قرار گرفته است
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/16611" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16610">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=El57ZDPh10Eu5p1nqwkeHhK4FJ9aXn8qcNX0p7xOyOb9OZfUmh74FSQIl5vriO4lKS6xRdVuOgi85rIdR0uYvf1mM8cC1G07XRKhZ_-LAvuBXUYrcPSKGV2OXQg8WWO4t3eG4nrtfDbsHdon6uYZNuICiqe7uJZcsFfnGv6wBI8GyLnqcwJJpMHVwczfZymmAGQbkRALSuqYQz1O7rMX6Hpkes4oRxoTncivtcKKJFLqkRrybabYZBoUNDnDTerBokNhGaYM-w6NAqFyL3N_6r_sVqtVqx3NbeU-Rf2ckDHDPAIruszqrdDWqu8pZGu1_WkzKRChb7VqnH9RwC-eCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=El57ZDPh10Eu5p1nqwkeHhK4FJ9aXn8qcNX0p7xOyOb9OZfUmh74FSQIl5vriO4lKS6xRdVuOgi85rIdR0uYvf1mM8cC1G07XRKhZ_-LAvuBXUYrcPSKGV2OXQg8WWO4t3eG4nrtfDbsHdon6uYZNuICiqe7uJZcsFfnGv6wBI8GyLnqcwJJpMHVwczfZymmAGQbkRALSuqYQz1O7rMX6Hpkes4oRxoTncivtcKKJFLqkRrybabYZBoUNDnDTerBokNhGaYM-w6NAqFyL3N_6r_sVqtVqx3NbeU-Rf2ckDHDPAIruszqrdDWqu8pZGu1_WkzKRChb7VqnH9RwC-eCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره ای از ۶ ژوئیه دیروز ، چند هزار نفر را نشان می‌دهد که در نزدیکی برج آزادی در تهران، ایران، برای مراسم تشییع، جمع شده‌اند که کاملا برخلاف ادعا های میلیونی رژیم است
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/16610" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16609">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZAu2_j9HHMGGzyCiTWEjCtnEoK_r2Vhwk-enERDWd6GWKn-zh8Brz4bXYNMkdvVMgFdMilPiGj4ow5xNSuD9RwqH1jwctdBULEyKP-bfv3xKomfBl3Xm6lzrY4QkeKYA0zBl8Q2l8pX6EpLa_aNEGzC2AGYEpuh26zLFGbuzJRzJPH2GvWmcb4R0-a1iv-eEJGrmbUHqjVUiHd4sqxkWwwspEjIP_SmFqeTWUY_ay2wppN9BtgOdsuaKr65YJpZ6Ffv_VoAAROYUperGs2q6bss0dUxihCGrS88ppRsKv1PEZbjytqrR_HbQ5AMqTf1LcDJK4pf-Q3pn-KTBspEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدل ایست نیوز : تصاویر ماهواره‌ای نشان می‌دهد ناو هواپیمابر امریکایی «آبراهام لینکلن» از دریای عمان خارج شده و در دریای عرب مستقر شده است
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/16609" target="_blank">📅 10:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16608">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyUt5BQcjrUkyQWpKUyRfpurPj0sNYB-WB6sOn5KaFE-kUWfqqmI5CBwgz_bNbot4qrA-3-N2b2uuoonQoldJTaYBQ2aVis4UJdfYI8m7ta9ggktXv4ZTk7DI2TA31ATNTtbYI9AdT3rqJHJnYxjD0CwdjxIu4yHRMedsaR09l-wweLurvNzr_trN6waajurty455HOnqOokqs9xvMz2IS9bB6Ey9gMzSRBZtSYP6Ud27F4XbYlLRSMEFkaw_tZ6Oq9UUi07gn9Jje6T1wk7p7WVNG2QfZRv8DI3j3l58dhtIe3m5o3KEY9D3Dryl7Zw1N9Q_0zpE1MHi6QkvQ7kzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: انتظار می‌رود ترامپ به اردوغان اطلاع دهد که مایل به فروش جنگنده‌های اف-۳۵ به ترکیه است، اگرچه هنوز مشخص نیست چنین معامله‌ای چه زمانی یا چگونه انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/16608" target="_blank">📅 10:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16607">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عراقچی به ترامپ: به امضای خود پایبند باشید
تا زمانی که تهدید‌ها علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/16607" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16606">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یک منبع امنیتی اسرائیلی به وب‌سایت والا گفت:
حماس هیچ قصدی برای خلع سلاح شدن، تسلیم کردن سلاح‌های خود، یا تخریب تونل‌ها ندارد.
استعفای دولت حماس یک اقدام نمادین است که با هدف نشان دادن تغییر به واشنگتن و شورای صلح انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16606" target="_blank">📅 09:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16605">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی: سپاه پاسداران دست‌کم دو موشک به سمت کشتی‌های تجاری که در حال عبور از تنگه هرمز بودند، شلیک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/16605" target="_blank">📅 09:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16604">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6NnynToEjbKxHHGAsjBpkeR49pkg5E2qITfCsQllYuauCFHOZv4RLnM_olMY_n1bkXPX6lYRpjyKXRbT3IKUzPu7-qjY1sIs8TOHMrY0HTdOKxMNwJMvGlNxAEZAMLYD00vg6LU6qo3lp8Xaz5idTgz40B9O_iW5NQMd1RdztM7WN8L6_592243ZSF3IJALoqknQitcjE6p7ghyaKxkn8-ZqF6LL7UqpGWmGeDuW5ThBtzZbBinyriSkva1btG_v3ICCGHYCEOlrJ-OSCoF_ghQFapqVTFAodtRoUUK69MC1KIkQML3bbOxNgBFt2p9DigF25tyVMv0fMlKTudEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
گفته شده نفتکش مذکور حامل گاز صادراتی قطر بوده است
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/16604" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16603">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=f5In7O7945pX7nmEuaoVOGIvJ29GX7VAB72qZz5PG2urUbf1C_s09V6n3jgG3W0TdKeeocwuyIKeQtjVTW70tbAp9NKBNohLfLWl6unp6xsEAZV99N-KI-DeTy9p2VHEYs8F173hBsA9W_Xfft7QVIZvoT5w2WYX9vFlu2DJusSejbfp-DaeszZX_preb6ZSoySX6rJtSNbFWY8eP7NkHxSnn1CtoH6M5VuXjuHiK6NEB2oFP1oshfjwEkexw9baq_otwKtdSd6TaZ9wdbYXzRnk1FBJygjhhFocaFG8AYs3VGk-7GUEtJg7-ADcFWnOBxBbMbFix1-3VXaayJoRXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=f5In7O7945pX7nmEuaoVOGIvJ29GX7VAB72qZz5PG2urUbf1C_s09V6n3jgG3W0TdKeeocwuyIKeQtjVTW70tbAp9NKBNohLfLWl6unp6xsEAZV99N-KI-DeTy9p2VHEYs8F173hBsA9W_Xfft7QVIZvoT5w2WYX9vFlu2DJusSejbfp-DaeszZX_preb6ZSoySX6rJtSNbFWY8eP7NkHxSnn1CtoH6M5VuXjuHiK6NEB2oFP1oshfjwEkexw9baq_otwKtdSd6TaZ9wdbYXzRnk1FBJygjhhFocaFG8AYs3VGk-7GUEtJg7-ADcFWnOBxBbMbFix1-3VXaayJoRXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوایی که ما تنفس میکنیم سیاسی هستش !
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16603" target="_blank">📅 02:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16602">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=PHTcbTRjaJaKzLzQfelXaiaxcvuJmWiXXd1vgHyzMw3bXxiFHZQUsF-IrDmH0-aGFZCJ46_lFK4MX38tRCUvDZFfNxervfk8IgfCfp-5HaD12eZAQpjIIVvnaXYo4QRvxbI02_JGKWQZL92kl9pf8CfqiOCuC6b51EMaftYesuvuGA6Ahj3ggfgNcS2E1dAhGZhrPf6uoGT-YK2l-ZTqVK4V2y55SmegxQiyoGl62bcDofIeWb23Dpzznp17GrCE6kYWr9VRzZ9SpiEo0eMfehmUHYYbdUvpn82sDZkw-CVjnHmH-AdGMj2wUI2i0mcXwLeocpw67kgU_Onu6QVs-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=PHTcbTRjaJaKzLzQfelXaiaxcvuJmWiXXd1vgHyzMw3bXxiFHZQUsF-IrDmH0-aGFZCJ46_lFK4MX38tRCUvDZFfNxervfk8IgfCfp-5HaD12eZAQpjIIVvnaXYo4QRvxbI02_JGKWQZL92kl9pf8CfqiOCuC6b51EMaftYesuvuGA6Ahj3ggfgNcS2E1dAhGZhrPf6uoGT-YK2l-ZTqVK4V2y55SmegxQiyoGl62bcDofIeWb23Dpzznp17GrCE6kYWr9VRzZ9SpiEo0eMfehmUHYYbdUvpn82sDZkw-CVjnHmH-AdGMj2wUI2i0mcXwLeocpw67kgU_Onu6QVs-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک پمپئو، وزیر خارجه آمریکا در دوره اول ترامپ: حکومت ایران عمداً چهارم جولای (روز استقلال آمریکا) را برای مراسم تشییع جنازه انتخاب کرد تا نفرت خود را از هر آنچه آمریکا نماینده آن است نشان دهد.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16602" target="_blank">📅 01:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16601">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr05N_O9ZxZjhi9pZDsTCcYmBpNQflKVYvqjMavEioH7uLsXqXkP-DEN40zWtna8gQXnx0u0z6BgcfFZCLrX_9LQSleh98I0mlmDBRWw9OUbZYnuTfyco0MhktXXFd6S-b8DyG7Ejq4HIVK_JBYiH1eFLA8-uKZAsGsFsq8XAExEYhgeNWUzoyrILBLSNAj_pruMBS6RLsCSCI3SBLjz3v7U1vDx1pctmV4qhwAQH3RfEuaRAtEoZHaFCBo5Uq2rwRUPIJMro-kuFam75R_37Y3nU_IhtZ47nn9ILv-d0GSD2vcSskW2Yj12Mf8hgKPaTZ38DRHvpAWWcRCJz5N4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر هوایی از گشت زنی امروز گروهی از قایق های تندروی نیروی دریایی سپاه در تنگه هرمز
این شناورها در دو گروه مجزا به حرکت درآمده‌اند؛ اقدامی که توجه و دقت برخی رسانه های خارجی را به خود جلب کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16601" target="_blank">📅 01:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16600">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزیر امور خارجه آلمان:
ایران باید تمام هزینه عملیات‌های بین‌المللی برای پاک‌سازی تنگه‌هرمز از مین‌های دریایی را پرداخت کند
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16600" target="_blank">📅 01:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16599">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Q7JU5b23MEU3MVt0jq0_wHMdivP0ekfvd4oBHgRCKSytSJSYe2YVfTja9KlYqGlFDCgiIA0D-Y2SkOv_b8AccKPNDaLgGshv8SY3EKQcvmlo8rr_D3dSDrGxevCJUFhc7qQDOqoFk3qGMtgc8dHqb3czc1mh65mF8v1i4ktnnTwXv0lkv7dvzAbkN_GUVN1ypsw2DkS2InOe8qb0r7i5bpLUc7nOi4iDx7w4bmEbiVj4Ah3qvZshYo7b93m9dVJD1055dkAy7HH9PnbLD1zhdTnVtwXu6JT3qOy1YT-HxfQLTiiGeE_A-nbeD9pbrPkolkBxFOCwe7JBilvkpdImSm6eAjIUf7BMhXmvViXrhBXYYiRZpjjbitysvfiM4EDqgZ_Jatb1pPg2OwIyl-yUHojn5Sj1BzMt0VEsQ1_G3HFyUPToQz23TVv8XCLKrEUF1sKguoNwvIjNpvPWh8Pez9HQpJsQF9tFRDj-mdWVAcScJdOWUtc1QTf-N43fj9Du6aGirj-znH0wfFamTO9Ko0jrZWulhzouz9lWpxZACsPcqxkbxYF2FuSSHPRo5Kp-KSBYd2Q_1xZyRpOoBatAG5d3i9i2Ln5JOjyiPOssTQYmccMIvG2lYO97gsAOgquA2RELtj-RF8fqSWCxijD2mhwbYVfXaCJPwLFZAbMkmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Q7JU5b23MEU3MVt0jq0_wHMdivP0ekfvd4oBHgRCKSytSJSYe2YVfTja9KlYqGlFDCgiIA0D-Y2SkOv_b8AccKPNDaLgGshv8SY3EKQcvmlo8rr_D3dSDrGxevCJUFhc7qQDOqoFk3qGMtgc8dHqb3czc1mh65mF8v1i4ktnnTwXv0lkv7dvzAbkN_GUVN1ypsw2DkS2InOe8qb0r7i5bpLUc7nOi4iDx7w4bmEbiVj4Ah3qvZshYo7b93m9dVJD1055dkAy7HH9PnbLD1zhdTnVtwXu6JT3qOy1YT-HxfQLTiiGeE_A-nbeD9pbrPkolkBxFOCwe7JBilvkpdImSm6eAjIUf7BMhXmvViXrhBXYYiRZpjjbitysvfiM4EDqgZ_Jatb1pPg2OwIyl-yUHojn5Sj1BzMt0VEsQ1_G3HFyUPToQz23TVv8XCLKrEUF1sKguoNwvIjNpvPWh8Pez9HQpJsQF9tFRDj-mdWVAcScJdOWUtc1QTf-N43fj9Du6aGirj-znH0wfFamTO9Ko0jrZWulhzouz9lWpxZACsPcqxkbxYF2FuSSHPRo5Kp-KSBYd2Q_1xZyRpOoBatAG5d3i9i2Ln5JOjyiPOssTQYmccMIvG2lYO97gsAOgquA2RELtj-RF8fqSWCxijD2mhwbYVfXaCJPwLFZAbMkmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو لوئیز نازاریو دلیما</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/16599" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16598">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16598" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16597">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from~‌🇭🇦‌‌🇦🇳‌~,</strong></div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/16597" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16596">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی : کیپ‌ورد آرژانتین رو حذف میکنه، من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود! @withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/16596" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16595">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig9xExPJWDOY8JCQdhm1t9vOyEs5uXr4JMlNuMoGSdDqixmXBMPJqcWV3_DSCQu3TpKK75xjEn8jd59MCLZl9-DTAkkxCxrj_HwdtAdl2i-fpnrbfBa1CeszaHOJj0NnGnvfwSYZx28yF5KWHXi7gcJLzHAZQBp9DQD9u0rzWJ0NQEk_i8wViqe8LFtZoe5no8BS7FgVKsgW2eox5USxkUIRSgt2q1zpvoGqImIYhNkJCFia7rClGV9_asvO5SRxrrsTygwk03BPRZnMl8wjxyXVMFmvAaoKYTWc93jchoFMShxV7QNWtO6TqS1Dq0GoluxzBUmJxFNsW9s3zpz8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرهنگ پاسدار صفدر سلطانی جانشین سپاه پاوه در مسیر بازگشت از مراسم تشییع توسط یک خودروی ناشناس منحرف و دچار سانحه تصادف گردید و کشته شد
@withyashar
🚨
🚨
🚨
🚨
سربازان گمنام حضرت موسی بد فرمون دادن</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16595" target="_blank">📅 00:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16594">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آکسیوس : نتانیاهو در تماس تلفنی با ترامپ؛
- خواسته که به اردوغان «تذکر جدی بده» یا «جلوی رفتارش رو بگیره»
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16594" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16593">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است. @withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/16593" target="_blank">📅 00:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16592">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">استان هایی که تاکنون سه شنبه ١۶ تیر را تعطیل اعلام کرده‌اند:
استان تهران
استان قم
استان سمنان
استان خوزستان
استان مازندران
استان اصفهان(شهرستان های آران و بیدگل و کاشان)
استان یزد
استان مرکزی
استان بوشهر
استان لرستان
استان هرمزگان
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/16592" target="_blank">📅 23:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16590">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دیوید کیس مشاور نتانیاهو:
بمباران مراسم ؟
شوخی میکنید؟
صدها مامور موساد توی اون مراسمه!
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16590" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16589">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=Wzo0EcNe8L2dSQMLqxoILE9fyY73--1kYJqIi7FPggy3J3jOgtYPZvrrrmcmK78I_JoT-m7w0SmiHTzC979Rzm95KgQfGX6NknOec_2yRdKP2rEsd1SLp48WHtbMk2jJAAOkxMrxZQvQKblpCiRWMlN2dM24G1Wem0SfK881dZiDt1MqaCuAfFZy398GtvZg8u7x9Z9OncwSZYydqGhp3HG2en_tTGvPwArKH-XtcaDP92EMMXbYpsfoAZVCAIw7yCe4QNJsjTT0t3s_q9KAJtf59ZL55QoLt6XAh6qbdxOcVUT8aXa7jXmfNcv5zx7_D64wLqAni7dDjODgG9ohwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=Wzo0EcNe8L2dSQMLqxoILE9fyY73--1kYJqIi7FPggy3J3jOgtYPZvrrrmcmK78I_JoT-m7w0SmiHTzC979Rzm95KgQfGX6NknOec_2yRdKP2rEsd1SLp48WHtbMk2jJAAOkxMrxZQvQKblpCiRWMlN2dM24G1Wem0SfK881dZiDt1MqaCuAfFZy398GtvZg8u7x9Z9OncwSZYydqGhp3HG2en_tTGvPwArKH-XtcaDP92EMMXbYpsfoAZVCAIw7yCe4QNJsjTT0t3s_q9KAJtf59ZL55QoLt6XAh6qbdxOcVUT8aXa7jXmfNcv5zx7_D64wLqAni7dDjODgG9ohwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/16589" target="_blank">📅 22:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16588">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم. @withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/16588" target="_blank">📅 21:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16587">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=f0mxl0zMrDzxXFK9MfmB2rmntRHHI7GqclEjzChj_fvH1MfCAACVGDxi-Cu_KbPRZLmIANlAxMbngsjvFUDDU6_xlgQwDGGmAIlZ-wu6eLmGK-ltOxbtqa_HV6Pjln4-WG6hnASYi8OBjm7uIRxp5jCGGQdiK501A6Y0wswAanJUaEAS6QGykt-rEcfKWiOecnUoUELSE68QnNSR0n-ImGkkg3Bsav83Vyc5E1abT5AVThgrlaBCAm0ENs_1riutOsoTPJR2B6VCy57EHeuSTY97xSVj3NrlkljauKvZibgBq7Mzve3pCcLMVftmw46o7PVtQjx__H0Uq_sdblIL8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=f0mxl0zMrDzxXFK9MfmB2rmntRHHI7GqclEjzChj_fvH1MfCAACVGDxi-Cu_KbPRZLmIANlAxMbngsjvFUDDU6_xlgQwDGGmAIlZ-wu6eLmGK-ltOxbtqa_HV6Pjln4-WG6hnASYi8OBjm7uIRxp5jCGGQdiK501A6Y0wswAanJUaEAS6QGykt-rEcfKWiOecnUoUELSE68QnNSR0n-ImGkkg3Bsav83Vyc5E1abT5AVThgrlaBCAm0ENs_1riutOsoTPJR2B6VCy57EHeuSTY97xSVj3NrlkljauKvZibgBq7Mzve3pCcLMVftmw46o7PVtQjx__H0Uq_sdblIL8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون با عینک آفتابی معروفش که ترامپ مسخرش میکنه وارد سوریه شد
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/16587" target="_blank">📅 21:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16586">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رئیس‌جمهور فرانسه پس از ۱۸ سال وارد سوریه شد
یک منبع ریاست‌جمهوری فرانسه اعلام کرد که سفر رئیس‌جمهور این کشور به دمشق با هدف از سرگیری همکاری‌های اقتصادی و تجاری با سوریه انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16586" target="_blank">📅 20:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16585">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=hUe5B5PyPEW1rEkCmMpK9RbMNM1407GguDSXE6w_UrsP6D3MmedE6C4SMJaarYOd2tKV588ot8Buvhp7csZBk2jCHTirVJmHzpvQZ1yZmiMU-SfNb9A4NJbSq3pA3Ze345ADJyQ3cJ3dlHYzMNqxxz-_91qAaHMmJ8Su_ZymbbUiyd_UdYCUlIXBtpwBmjbjxMdeHrAxdhSl0C6OAiQ6kvxZ0t7CTfG0dszqBTJisz-q_YUphGfMMftkm1SiT29poOBXZ73TXYyuvIqn-zWb1eYjwjU94nCWZlvxfkrQkDv7qO2ITpyQcS9YimeA_BhQrOt5kUF_PNyUQN7u917c5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=hUe5B5PyPEW1rEkCmMpK9RbMNM1407GguDSXE6w_UrsP6D3MmedE6C4SMJaarYOd2tKV588ot8Buvhp7csZBk2jCHTirVJmHzpvQZ1yZmiMU-SfNb9A4NJbSq3pA3Ze345ADJyQ3cJ3dlHYzMNqxxz-_91qAaHMmJ8Su_ZymbbUiyd_UdYCUlIXBtpwBmjbjxMdeHrAxdhSl0C6OAiQ6kvxZ0t7CTfG0dszqBTJisz-q_YUphGfMMftkm1SiT29poOBXZ73TXYyuvIqn-zWb1eYjwjU94nCWZlvxfkrQkDv7qO2ITpyQcS9YimeA_BhQrOt5kUF_PNyUQN7u917c5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16585" target="_blank">📅 20:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16584">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=SW7HU1iUuNIJcdaF3XT_l-ROchSn6ZPctkm1epRkZRY46eUIpuBErcdsCTOXJsvQ4P2vAQ0iirsTy4symVn5B2La-RznULsT1zsU7M-wzO4uZHpYX7Q6Cu09jDvebY3ll9NRFmC4D44DgGc7ViHQvGrt-GYklraDur9-cuA2g5Sb_XdbHTf4bWm5ZLIxk4Jg3wkh7_8pX3LQ7shHg-CYhOclII4HkD1FRP36AhSLV9TLCACkSAYhHfrb-UtVzYrQOoFFpg1LsRugiWLHaq6568L7rlMQ0L88F0GB6c4PBaaDLNChohBTBn7XWj6DrnR0Oi8qPZ6HooY1EKwMoaPbqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=SW7HU1iUuNIJcdaF3XT_l-ROchSn6ZPctkm1epRkZRY46eUIpuBErcdsCTOXJsvQ4P2vAQ0iirsTy4symVn5B2La-RznULsT1zsU7M-wzO4uZHpYX7Q6Cu09jDvebY3ll9NRFmC4D44DgGc7ViHQvGrt-GYklraDur9-cuA2g5Sb_XdbHTf4bWm5ZLIxk4Jg3wkh7_8pX3LQ7shHg-CYhOclII4HkD1FRP36AhSLV9TLCACkSAYhHfrb-UtVzYrQOoFFpg1LsRugiWLHaq6568L7rlMQ0L88F0GB6c4PBaaDLNChohBTBn7XWj6DrnR0Oi8qPZ6HooY1EKwMoaPbqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این نسل چی میخواد از جون ما ؟
اومده تخم مرغ آبپزشو بگیره…
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16584" target="_blank">📅 20:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16583">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qtsmgRAO9keymBnLixu1mOcvrFIaYfLC_RJ4OFAeZ1Ax79RSVDwBCPqo07LNhzcFh3m2Tp9BpM2BuSxY-qdz0_Wtv-G4DhVIItceHw6xeRFZDOP6oTmgWiVsH-eWVsFbStRcPNl3kHtxQl55cslrpx39GDtwGOrnfDQOUWJ0nbFFwJNLs7YmFB6w3Cczi5KEl0D1wRoipV65B9WCQ3N5nZaFmBo1HFLu23bNpRliWjlY9aYOrpnElzzPXDFP5BuVbPxu7sKHRS_kK0Sz1SK4cUbJBl3r3FFr_sdtSAPReOVLBWKhazSw6Dny8h3VnxC5InNf9DQ0SC8wCeekqWY89g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qtsmgRAO9keymBnLixu1mOcvrFIaYfLC_RJ4OFAeZ1Ax79RSVDwBCPqo07LNhzcFh3m2Tp9BpM2BuSxY-qdz0_Wtv-G4DhVIItceHw6xeRFZDOP6oTmgWiVsH-eWVsFbStRcPNl3kHtxQl55cslrpx39GDtwGOrnfDQOUWJ0nbFFwJNLs7YmFB6w3Cczi5KEl0D1wRoipV65B9WCQ3N5nZaFmBo1HFLu23bNpRliWjlY9aYOrpnElzzPXDFP5BuVbPxu7sKHRS_kK0Sz1SK4cUbJBl3r3FFr_sdtSAPReOVLBWKhazSw6Dny8h3VnxC5InNf9DQ0SC8wCeekqWY89g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/16583" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16582">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5PVr5QkNU49r-qaoIEYttRjFj6Ak--Jb2dGZxRg2yRCHlQDuz0UHqNnj6rAWFblWG3-PPER-cYVLKw9rSo3RshS0G4lF-EnAtSEvJiTO-0ToQHRKkQ6iEVWz5EUUgiGC9vduBrABarfNUGGaCgHWDuy_nrZjQh6ekJCIwHs8uQbBax2QIE4SMsjvqpWiHuuu9pcUTM32vuXPpD1BZVdYVJhfuJvuLCT4WkE48EaEfIgzx12hGb7k5tg4xK7OHqL4DrBhk9FhTukBOK8SmA7OZBVYSRbPEXy4EZnTIfA4BXCSjbnmUBr5je4VlhtYa_LBUzPC5IcAOjWyMu_05JMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهام شرکت دل پس از اظهارنظر دونالد ترامپ مبنی بر اینکه «بروید و یک کامپیوتر دل بخرید» ۸.۳ درصد افزایش یافت
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16582" target="_blank">📅 19:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16581">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ : ما از ایران امتیازاتی گرفتیم و آنها باید به آنها پایبند باشند و ما همچنین اورانیوم غنی‌شده با خلوص بالای ایران را دریافت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16581" target="_blank">📅 18:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16580">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=H-pPVEySuC_FxOIluZ9FnAlRJIAZXIhSNh1_kZWetamDkZjxDUyoud7vtsfpPEa-1gkUVI_TQC93TE8Fp27QknPkx8Vs4vQJ1QwFYH1FenZr99cupIp65-RQB80uijfGBnyxSebeFC84-u1sDWoGn7nkQ6WTve7RTRVIfCr40P83mseRIkH1m0ioa_-7N8k5x9i00c6Y9QrbhAEIFN3CqJ8t7H5Ox-9iXSwoM4VJrhV_z5wi5DclNfA5O6h8QDriz9eh1zr0TCrnSkC-ZQAhN3yxuc_St49o9gAtxSQuqKVJkJMLsO8OF4fOWBcswsQeRK5pZWpxFqFCIdBnvMXcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=H-pPVEySuC_FxOIluZ9FnAlRJIAZXIhSNh1_kZWetamDkZjxDUyoud7vtsfpPEa-1gkUVI_TQC93TE8Fp27QknPkx8Vs4vQJ1QwFYH1FenZr99cupIp65-RQB80uijfGBnyxSebeFC84-u1sDWoGn7nkQ6WTve7RTRVIfCr40P83mseRIkH1m0ioa_-7N8k5x9i00c6Y9QrbhAEIFN3CqJ8t7H5Ox-9iXSwoM4VJrhV_z5wi5DclNfA5O6h8QDriz9eh1zr0TCrnSkC-ZQAhN3yxuc_St49o9gAtxSQuqKVJkJMLsO8OF4fOWBcswsQeRK5pZWpxFqFCIdBnvMXcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بررسی ترافیک کشتی‌های تجاری از طریق تنگه هرمز طی ۲۴ ساعت گذشته که از طریق مرین ترافیک قابل مشاهده است، نشان می‌دهد که اکثریت قریب به اتفاق کشتی‌ها همچنان از طریق طرح جداسازی ترافیک (شمالی) ایران عبور می‌کنند و تنها تعداد کمی از آنها کریدور جنوبی تحت حمایت ایالات متحده از طریق آب‌های عمان را انتخاب می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/16580" target="_blank">📅 18:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16579">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=oDfVTG4MH27IdLfhug_8hYHj0kaz7pjnP7Q3o3Q8Q_xovzmrO2BJE3hPdXe8kaoOS_z6OvOVydbCCXc-EPwBwdV8UdkEhgRvUvq64cru0X8ouVzQejwMa02WkDeTysKlRjnkpKc8eaANCYy1Cac1PsqeDKMVUq0W0Uwl3DQsl1VhgD6m6aBYhsRXTXfoZ8zAnhx6ZcmdsPSlPDROjtfOnRy3kZV9OLjnw-o_U8UTotexDskCAze6E8Rb-2v7NkxQBW-RbcLaj0quqZK15YsME5zeHBOHQJPjrM75JlDn6oJMDIWJQPA1iBS8gtc9vena4sYonM5PqK6h_v3ybptbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=oDfVTG4MH27IdLfhug_8hYHj0kaz7pjnP7Q3o3Q8Q_xovzmrO2BJE3hPdXe8kaoOS_z6OvOVydbCCXc-EPwBwdV8UdkEhgRvUvq64cru0X8ouVzQejwMa02WkDeTysKlRjnkpKc8eaANCYy1Cac1PsqeDKMVUq0W0Uwl3DQsl1VhgD6m6aBYhsRXTXfoZ8zAnhx6ZcmdsPSlPDROjtfOnRy3kZV9OLjnw-o_U8UTotexDskCAze6E8Rb-2v7NkxQBW-RbcLaj0quqZK15YsME5zeHBOHQJPjrM75JlDn6oJMDIWJQPA1iBS8gtc9vena4sYonM5PqK6h_v3ybptbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد جنگهای پهپادی: چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند.
شگفت‌انگیز است.
شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد.
و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16579" target="_blank">📅 18:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16578">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: نیروی دریایی ایالات متحده بزرگترین محاصره‌ای را که جهان تاکنون دیده است، علیه ایران اعمال کرد و حتی یک کشتی هم نتوانست از آن عبور کند.
هیچ پولی به ایران نمی‌دهیم
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/16578" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16577">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=arMptQwIjg6kw_mRZAos-F9gRD6nMQFHSMn72G4g5qYuxLb77jUD8ocZYaD52gq_R-HHSHMFDIDTLUh18wwqwjr1KjIrUNnotuANLBFlKukYUaeTd1iLTYv7nCrZ2Zk65j-6foqI3ZX6mZrax6G3bUt5eZN-ogvw4cAxwfGR_PEA8Mx9PRuemy4RRB7HKNW_mkszVDWFFwFU7rXnD25nGAYwyW8CzENdkscRnYV3h2fuzzNJsgwBc005XKt0vHlrNjKCvMSETJ7PdocFWUfQ95ipwOSyEw9RJmxrVFb7CCJLw8qUf7B-5B-xwew_QvLWFQlYXJ92tMxc01S94Yo6iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=arMptQwIjg6kw_mRZAos-F9gRD6nMQFHSMn72G4g5qYuxLb77jUD8ocZYaD52gq_R-HHSHMFDIDTLUh18wwqwjr1KjIrUNnotuANLBFlKukYUaeTd1iLTYv7nCrZ2Zk65j-6foqI3ZX6mZrax6G3bUt5eZN-ogvw4cAxwfGR_PEA8Mx9PRuemy4RRB7HKNW_mkszVDWFFwFU7rXnD25nGAYwyW8CzENdkscRnYV3h2fuzzNJsgwBc005XKt0vHlrNjKCvMSETJ7PdocFWUfQ95ipwOSyEw9RJmxrVFb7CCJLw8qUf7B-5B-xwew_QvLWFQlYXJ92tMxc01S94Yo6iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره اورانیوم غنی شده در ایران:
ما قرار است چیزی را که من به آن گرد و غبار می‌گویم، یعنی مواد غنی‌شده، به دست آوریم. من به آن گرد و غبار هسته‌ای می‌گویم.
من به یک دلیل بسیار قوی وارد عمل شدم و آن این است که ایران نباید سلاح هسته‌ای داشته باشد. من به دنبال تغییر رژیم نیستم، هرچند این همان تغییر رژیم است.
رژیم اول رفته است. رژیم دوم رفته است. و من فکر می‌کنم رژیم سوم منطقی‌تر است، اما خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16577" target="_blank">📅 18:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16576">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6831709af6.mp4?token=iTcn8Gq6MTWipzuEnpIU4XEQKY3jWJfxPVeD-0f5B6BpLkthCeaI24iaFNiFOBDpsk8HmqCn5ZX7fU8JoMRwDf5uDfaO4GGbK8V8OGZcqkt3Sru86nv2Ojf7ZYd8VCtDalY21GCY0LLTi55kkNwIPsHRTWNAEMRHSltuyeW5gv-MmCMEmieim0tzssziCGwvwFzlWDetlPv8Zr_aoJOewvsHTI2H4RS-z0S5yQSRwsoWRQ856cWJE_HublC97G_5JGp5X7VDdf6O6tyfAdoMhfpCzT58OnyjX1fKJBKhBvRIxtT7s3ow0ZaO8L2usT1L_ZLmQbIOxKS_PWCwouJa0n3qCD7KgXVCl6K-HU0T7OI-TvRdLX7jpwOhLFONbGYast0O16UbxiX5N6JYMwuBVGaM0fN6XvL0mMt1q6lyE2cvTlYkNFEi0Ju2dELtdAv3KFlWExKND4FQEG5YLtXhXh4t1BG7lH1EqZnySYdJwBiJXU8Vu-ul6vvP4B7PNvJE95SOT-EBad_aqoirljhI-hLJW2YW7y7dniVh4gqRqvyQro80nFDFGcbZG6TFT0Lsli1K6RnKBXyECJaFBw6-SqyO7C-yWd53zP1h81vepqOWLtWxeG4f8DO33mFZQpIzm1Klq-yJDtLPDxRRn-yAu2NG7BD5Z_f5pbNmFYDhbdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6831709af6.mp4?token=iTcn8Gq6MTWipzuEnpIU4XEQKY3jWJfxPVeD-0f5B6BpLkthCeaI24iaFNiFOBDpsk8HmqCn5ZX7fU8JoMRwDf5uDfaO4GGbK8V8OGZcqkt3Sru86nv2Ojf7ZYd8VCtDalY21GCY0LLTi55kkNwIPsHRTWNAEMRHSltuyeW5gv-MmCMEmieim0tzssziCGwvwFzlWDetlPv8Zr_aoJOewvsHTI2H4RS-z0S5yQSRwsoWRQ856cWJE_HublC97G_5JGp5X7VDdf6O6tyfAdoMhfpCzT58OnyjX1fKJBKhBvRIxtT7s3ow0ZaO8L2usT1L_ZLmQbIOxKS_PWCwouJa0n3qCD7KgXVCl6K-HU0T7OI-TvRdLX7jpwOhLFONbGYast0O16UbxiX5N6JYMwuBVGaM0fN6XvL0mMt1q6lyE2cvTlYkNFEi0Ju2dELtdAv3KFlWExKND4FQEG5YLtXhXh4t1BG7lH1EqZnySYdJwBiJXU8Vu-ul6vvP4B7PNvJE95SOT-EBad_aqoirljhI-hLJW2YW7y7dniVh4gqRqvyQro80nFDFGcbZG6TFT0Lsli1K6RnKBXyECJaFBw6-SqyO7C-yWd53zP1h81vepqOWLtWxeG4f8DO33mFZQpIzm1Klq-yJDtLPDxRRn-yAu2NG7BD5Z_f5pbNmFYDhbdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : یا توافق میکنیم یا کار رو تموم می‌کنیم، تمام کردن کار سخت نخواهد بود.
من ترجیح می‌دهم توافق کنیم چون نمی‌خوام به ۹۱ میلیون نفر آسیب بزنم. می‌تونیم پل‌هایشان رو در یک ساعت خراب کنیم.
می‌تونیم تأمین انرژی‌شان رو قطع کنیم، تمام کارخانه‌های بزرگ که ساختن، کارخانه‌های بزرگ، زیبا و مدرنی که پول زیادی هزینه شده بود. حالا دیگر پولی هم ندارن. ما پولی به آن‌ها نداده‌ایم.
می‌توانیم برق و نیروگاه‌های تولید انرژی‌شان رو، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر نیروگاهی از بین خواهد رفت و آن‌ها این رو می‌دانند.
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16576" target="_blank">📅 18:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16575">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ:من به دنبال تغییر رژیم در ایران نیستم و ترجیح می‌دهم به توافق برسیم زیرا نمی‌خواهم به ۹۱ میلیون نفر آسیبی برسد.
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/16575" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16574">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کانال ۱۴اسرائیل: مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از افراد حاضر در جمعیت، تلاش کرد از ردیابی بگریزد.
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/16574" target="_blank">📅 17:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16573">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXC8oAXvelj0soVWaFbxmf7LQVkRivU5Qv5zkhbRdBurefzJAfgn5I7_Nv0-zgSNYV7Gs0jmSgXJJ5i98T2c4Ko6mEzwgWiU-ewIjt76me2Bf_CI_Tij9ioLSA2S16G1VXyK-QlTs3sSXE3U3nLFkHcwLPe5QxFZPkzqLHE_4QFd68xZ-vEmvMM5DR14Ze7Vgbcg1H4mnUst7kbJpLMXbatAdEdVDLyYkN7uljlBqm_B5k4C4UtP0TEFgMxNvvUN-L7OPvsOZ1ZD3HDfGyVs0nVahldz76x6ME4tTlFFMqDRQ_RNed4Rvsf4FXKTCu1dWuM6k9Awpg26aLUuwwYqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن چاه وشی این استوری حقیرانه را منتشر کرد …
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/16573" target="_blank">📅 16:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16572">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مجری فاکس
:
چرا این حکومت هنوز توی ایران سرِ پاست؟
نتانیاهو : چون چند صد هزار نفر نیروی سرکوب داره که وسط روز آدم می‌کشن و شب هم مردم خودشون رو به قتل می‌رسونن
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16572" target="_blank">📅 16:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16571">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=JLu_POY9PXGy-vYtRKaAq8h3n1KuYMRdS1PvI_a1RLrAT73DKoh7mV3HMu4_DovLscoC8QNJd_E0DbJI_gXbEAojd484qSP3xGmi3K0i7iY9iN1sLfmq0mK_Pn8a0LcDQCptoUzEgZIryzfICEOwJw759EL0en_0q_oHhmthddmUn_HjLZQykJmHQJwG3f0JZSzJkM2qGtUXYMYMBUhPiDXselg-_q5zhZ8a3n2tKFnvPUpYPm5k18da70n0e4NSbJfW4SVMTNa9gqZIJeD6GGR8u0JNEXDucDWTVSgENY1yu7ORXi2GC7fuMToD8y39Cnv55n00521TucBjKizdQGxKCjTmpe4mhm5ol7LLknT-wBRiJpWSMQH7jZWiKrrfgLae_eOJz4XMktjgFESoTiCmlJ0wuHpoWX14aXukuvdO4CHljn433jAE_ZrlDKZoQxL1OTT8M1BuGv_3dnI6LyoDvFdU03PgAZ4t4iquHdLLg-JFjJyy1xnQt0c42igrcOZCRcQrpCpotiiW_lElvlmaevuo93SgP-1ctXzeLoZU2tHzVNI-B5kLQp7zgo6Ich90lEdQBnGAbdYLJFQAZZfkBH1zSWvCAX5Qg6mubb-XORI1gkPjnB9V5RaiOaONwoNRw417fkMVdjTwQ7PgyaGsp9OpgRd4PYqk-KFZ-7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=JLu_POY9PXGy-vYtRKaAq8h3n1KuYMRdS1PvI_a1RLrAT73DKoh7mV3HMu4_DovLscoC8QNJd_E0DbJI_gXbEAojd484qSP3xGmi3K0i7iY9iN1sLfmq0mK_Pn8a0LcDQCptoUzEgZIryzfICEOwJw759EL0en_0q_oHhmthddmUn_HjLZQykJmHQJwG3f0JZSzJkM2qGtUXYMYMBUhPiDXselg-_q5zhZ8a3n2tKFnvPUpYPm5k18da70n0e4NSbJfW4SVMTNa9gqZIJeD6GGR8u0JNEXDucDWTVSgENY1yu7ORXi2GC7fuMToD8y39Cnv55n00521TucBjKizdQGxKCjTmpe4mhm5ol7LLknT-wBRiJpWSMQH7jZWiKrrfgLae_eOJz4XMktjgFESoTiCmlJ0wuHpoWX14aXukuvdO4CHljn433jAE_ZrlDKZoQxL1OTT8M1BuGv_3dnI6LyoDvFdU03PgAZ4t4iquHdLLg-JFjJyy1xnQt0c42igrcOZCRcQrpCpotiiW_lElvlmaevuo93SgP-1ctXzeLoZU2tHzVNI-B5kLQp7zgo6Ich90lEdQBnGAbdYLJFQAZZfkBH1zSWvCAX5Qg6mubb-XORI1gkPjnB9V5RaiOaONwoNRw417fkMVdjTwQ7PgyaGsp9OpgRd4PYqk-KFZ-7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎نتانیاهو به فاکس : ایران حدود ۹۰ میلیون جمعیت داره
- به نظر من حدود ۸۰ درصد مردم از این حکومت خوششون نمیاد و مخالفشن
- ولی بازم چند میلیون نفر هستن که حکومت می‌تونه بیاره تو خیابون
- اون‌ها هم شعار "مرگ بر ترامپ" و البته "مرگ بر من" سر می‌دن
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16571" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
