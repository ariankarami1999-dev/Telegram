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
<img src="https://cdn4.telesco.pe/file/AISTfjBj_wPqBOHU0SBZqdOVDami_CwZ3xI_njsOFyyzxr_Y1SmbENZ8jRcnadOBhR_PN4SHZLb2oVdOlEAs1oqlos-FkDk94Ilx1oOG2g7HnhpbRIfyuhSDUVWTkxm-p8Oz9BwP5oSG14NlDWRiEwMwCWAoBFfiwJJ4ByNHhmRJDZWRMNgDsDKpiw7jV0TigOVapRJYPAXds6nUQ_5iEiLyUDnetGQRT3ZnkxmmenOe0whvL37POgd2QiWJYBmezwoaqLanmG1SoG4LeWlfhnoBxMYPsrA4_0NMXW1jHD4DnOk2PS4Xe8yN8V3pjBZOrSctAl3Os2-x2KWKCq_0eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 17:44:11</div>
<hr>

<div class="tg-post" id="msg-680029">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
جهش ۸ درصدی قیمت گاز در اروپا
🔹
قیمت گاز در بازارهای اروپایی با افزایشی ۸ درصدی روبرو شد که ناشی از ابهام در سرنوشت مذاکرات پیرامون بازگشایی و امنیت تردد در تنگه هرمز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19 · <a href="https://t.me/akhbarefori/680029" target="_blank">📅 17:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680026">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28de48ce92.mp4?token=J4KaeBzxRTOdBrtxnkWdGpX0bE3c51FewYR2mmJKu59X0ST0xTNgSNY2COIrSXE7MmJcvIqlo31Gy7ANV31cjKhrhLu7p4IO5bFuqAtzrwRI8thDH7bwe5QnEfl59eTJSQXM0geuKwegIJBnF0tNLDlOoq5df94G6TPKQK7hU4uhGh9dcdFO6UnkHWUTRYpH3ZNLA8qdoYrl5VZw8-lVs_7cB4NjnDY-hxMnsSY3IHLQzhLCd5lwMupolAPB6h5B4xRU_mfl7kQK2dJb66-ixmFtLsNw9R3IY8FZ7FHwhm22hufjuDm70KwWWbYkyr1yAgmlWdMUKL6OLBF4FdK7hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28de48ce92.mp4?token=J4KaeBzxRTOdBrtxnkWdGpX0bE3c51FewYR2mmJKu59X0ST0xTNgSNY2COIrSXE7MmJcvIqlo31Gy7ANV31cjKhrhLu7p4IO5bFuqAtzrwRI8thDH7bwe5QnEfl59eTJSQXM0geuKwegIJBnF0tNLDlOoq5df94G6TPKQK7hU4uhGh9dcdFO6UnkHWUTRYpH3ZNLA8qdoYrl5VZw8-lVs_7cB4NjnDY-hxMnsSY3IHLQzhLCd5lwMupolAPB6h5B4xRU_mfl7kQK2dJb66-ixmFtLsNw9R3IY8FZ7FHwhm22hufjuDm70KwWWbYkyr1yAgmlWdMUKL6OLBF4FdK7hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات اولیه زلزله ۷.۴ ریشتری کلمبیا
🔹
سازمان زمین‌شناسی آمریکا از وقوع زمین‌لرزه‌ای به بزرگی ۷.۴ ریشتر در کلمبیا خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/680026" target="_blank">📅 17:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680025">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
حمید رسایی: مگر منصوب رئیس جمهور می‌تواند مجلس را تعطیل کند؟! جایگاه حقوقی دبیر شورای عالی امنیت ملی در جایگاهی نیست که بتواند مجلس را تعطیل کند
نایب رئیس مجلس:
🔹
مصوبات شعام پیش از ابلاغ به استحضار رهبر انقلاب می‌رسد اما در نهایت با امضای دبیر شعام ابلاغ می‌شود
🔹
ما سر هر موضوع و مصوبه‌ای نمی‌پرسیم آیا به استحضار رهبر انقلاب رسیده است یا خیر؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/680025" target="_blank">📅 17:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680024">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904a9af188.mp4?token=cU3Z3wDWl9rGL477vlQzM_NEbJpe1xi_KRqa99NLFLHlDeSjSf5yIeKKDg1IEHQgzMhCqic8hKFGuTiAB9Zn3EwOFaZf_e5R2OW08GaZh7LQ3YXc7iqCgl8Dg4axWrb5znzKB-gdMtr69qTcq2tc1TmA4MviMMrOQfTWb2pVCJ1o0xDNvE86rbPYdBnW7gWTUmGcVLrJe63MFR9NMQLof7q56VQBK2-bFfg3pnTV-vGIOFgcZfb10IvATU04wleNKv5gjeVm1Mo9vrbhs5zsDowZsZD-__Qs83nQJGMNQLIAajVrEaoK_31qGckIrdQfwgdxWLUdnEjCySXVy5h8GxKZxR2CMghLTHOvqWUU6fal3_XqwIrA3UrxCxW4N5ag1mHHfV3FBIa0YQu4ynECCgt4BUIobm0rklQOV9U_j6RsMsL5eKlctVCY3A1LkNmvqmD9Q4YMd3foCBjDzY_e8U6PQdo3YMpRzzMTBX7rBJqXBvJORYCTG5JaWHNHjle7VcurnmVsAHDXrJx5sZi5YleFNp4XLTIX4R4JvSYFi8CPR97prt45I4v4faj3LoO30kqV7t0enhAeT7r9rD1ipBAMEQs9dLFX4_jS1xyRAm8EKVc5ES6qAKnkUDwkhZp9C_Dejb2D0B_XJHnTA60qT-7x2cbiSKgmeVOgIDhpYto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904a9af188.mp4?token=cU3Z3wDWl9rGL477vlQzM_NEbJpe1xi_KRqa99NLFLHlDeSjSf5yIeKKDg1IEHQgzMhCqic8hKFGuTiAB9Zn3EwOFaZf_e5R2OW08GaZh7LQ3YXc7iqCgl8Dg4axWrb5znzKB-gdMtr69qTcq2tc1TmA4MviMMrOQfTWb2pVCJ1o0xDNvE86rbPYdBnW7gWTUmGcVLrJe63MFR9NMQLof7q56VQBK2-bFfg3pnTV-vGIOFgcZfb10IvATU04wleNKv5gjeVm1Mo9vrbhs5zsDowZsZD-__Qs83nQJGMNQLIAajVrEaoK_31qGckIrdQfwgdxWLUdnEjCySXVy5h8GxKZxR2CMghLTHOvqWUU6fal3_XqwIrA3UrxCxW4N5ag1mHHfV3FBIa0YQu4ynECCgt4BUIobm0rklQOV9U_j6RsMsL5eKlctVCY3A1LkNmvqmD9Q4YMd3foCBjDzY_e8U6PQdo3YMpRzzMTBX7rBJqXBvJORYCTG5JaWHNHjle7VcurnmVsAHDXrJx5sZi5YleFNp4XLTIX4R4JvSYFi8CPR97prt45I4v4faj3LoO30kqV7t0enhAeT7r9rD1ipBAMEQs9dLFX4_jS1xyRAm8EKVc5ES6qAKnkUDwkhZp9C_Dejb2D0B_XJHnTA60qT-7x2cbiSKgmeVOgIDhpYto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله آمریکا به اداره پست آذرشهر در ۱۹ اسفند
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/680024" target="_blank">📅 17:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680023">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111e8c1034.mp4?token=L5Ky80QaJumaRXMM7Pg_4lex_tY1Fbz2U1p8mJmhQdOLh7v4DfE05H_cXFx974F-vigWyo-gTY-XAa570RIRwFvQeBmzzAUizdMejrIr-KqjrVVIyodZ-xlipJxZCTq2aQ1tG5kA50boI7dhzo1yS4b9dWpOp8ntUEIHsdCzUk87w3pO3WMeNfXUdyWOGm5tUQflbB3Y5tOpZJgoKm0Iu1EsHJvAOcBW7Y5vI5Y5nT36gwJ3C11oujUPZ3CnNYTedhUE72hc7LCdbTj4k_Try-lw_OfKafY-RVNTdPJvvpuKl0gsItYkfjc_6QdSzjdKBgqrYiWMfsChyKboToQC4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111e8c1034.mp4?token=L5Ky80QaJumaRXMM7Pg_4lex_tY1Fbz2U1p8mJmhQdOLh7v4DfE05H_cXFx974F-vigWyo-gTY-XAa570RIRwFvQeBmzzAUizdMejrIr-KqjrVVIyodZ-xlipJxZCTq2aQ1tG5kA50boI7dhzo1yS4b9dWpOp8ntUEIHsdCzUk87w3pO3WMeNfXUdyWOGm5tUQflbB3Y5tOpZJgoKm0Iu1EsHJvAOcBW7Y5vI5Y5nT36gwJ3C11oujUPZ3CnNYTedhUE72hc7LCdbTj4k_Try-lw_OfKafY-RVNTdPJvvpuKl0gsItYkfjc_6QdSzjdKBgqrYiWMfsChyKboToQC4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدادعادل: کسانی‌که هنوز در رویای دوران انتخابات هستند اشتباه می‌کنند؛ وقتی که کشور در معرض خطر است چه اصولگرا و چه اصلاح‌طلب باید به دولت کمک کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/680023" target="_blank">📅 17:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680022">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
رئیس پژوهشگاه رویان: اروپایی‌ها ایران را برای درمان ناباروری انتخاب می‌کنند
شاهوردی، رئیس پژوهشگاه رویان:
🔹
پیش از چالش‌های یک سال تا یک سال و نیم اخیر، سالانه بیش از ۵۰۰ زوج نابارور خارجی در پژوهشگاه رویان پذیرش می‌شدند.
🔹
بیماران مسلمان از کشورهای اروپایی، از جمله انگلیس، برای درمان ناباروری به ایران مراجعه کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/680022" target="_blank">📅 17:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680021">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/680021" target="_blank">📅 17:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680020">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cad9612af.mp4?token=Yt31narOd5Fu9sftic5W6gmJno7EoKfYSuSfI7H0BDYaHTdNw8qCbRJFOUZrct0oBp20RyV2lyTNQppgVvBVKbjM2LOQ6DDapmDdLNKSGJcgb1b0yNhvgOoVXHL31-zt5DWoYBHoTs_4ME5kPVGpuzSpFh6j9kLUwoT55xQQ6-ZifR2lXX4RhqOQQhtzFJideIpXDjAOfB3q6_JzOqULxuSWqiMLv60W-PRG3ooCYN5WbTrcijoumQLbfJ9fdNo4JdN4gF3rMqaJp5DT3RI6EeWv7ZbDvXxj2UpRv6BledUbIyzihorOBivr7TgXRYeH4sGFa6Cvd9HhKYNWG9RynjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cad9612af.mp4?token=Yt31narOd5Fu9sftic5W6gmJno7EoKfYSuSfI7H0BDYaHTdNw8qCbRJFOUZrct0oBp20RyV2lyTNQppgVvBVKbjM2LOQ6DDapmDdLNKSGJcgb1b0yNhvgOoVXHL31-zt5DWoYBHoTs_4ME5kPVGpuzSpFh6j9kLUwoT55xQQ6-ZifR2lXX4RhqOQQhtzFJideIpXDjAOfB3q6_JzOqULxuSWqiMLv60W-PRG3ooCYN5WbTrcijoumQLbfJ9fdNo4JdN4gF3rMqaJp5DT3RI6EeWv7ZbDvXxj2UpRv6BledUbIyzihorOBivr7TgXRYeH4sGFa6Cvd9HhKYNWG9RynjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: خدمت رهبر انقلاب رسیدیم و از هر دری گفتیم
🔹
ایشان از لحاظ جسمی  در صحت و سلامت کامل بودند؛ ایشان رهنمودهای خود را ارائه فرمودند و  دغدغه‌ها و مشکلات را گفتم و به راحتی سخنانم را گوش دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/680020" target="_blank">📅 17:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680019">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/680019" target="_blank">📅 17:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680018">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpSOiM6Ru61MPJX13MCxSeEO3ZtG8GL4UOaIG4k9JlXpub92QA14L3U9XsrTm2aFqW9JP4P29BBfp6nUYtKbAYwZAaDy65gBP9Poj9c0V8xQsbxEYNDhgDMnihgqlVGfr1Ke1QNO2zaYZJChWizXmIvqdejs04ySkJRkxi_1_IH5_bcpfcJA5pRl9yS9MWRu0KknWO1lnyfCn1skyw53iy2jReTZW5HZ4_4wpeaSRCaSMDl6Vo6NOagJs_OOJPTfCiAlWFYnYw65nDCiGOe6sDQW-0lZKQ_8aDZSu85CiiFyiRnO-3JHXny7Ks7TsyqjhGn_z_SCn9KL17xKuFzI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۴
🔹
عبور سهم از بازار بانک کشاورزی از مرز ۷ درصد پس از ۲۰ سال
🔻
سهم بانک کشاورزی از کل سپرده‌های شبکه بانکی برای نخستین بار طی ۲۰ سال گذشته، در تیرماه ۱۴۰۵ از مرز ۷ درصد عبور کرد.
🔻
سهم از بازار این بانک پس از یک دوره تثبیت در بازه زمانی ۱۴۰۰ تا ۱۴۰۲، روند صعودی به خود گرفته و از ۴.۳۶ درصد در ابتدای سال ۱۴۰۳ به ۴.۵۱ درصد در فروردین ۱۴۰۴ رسید و سپس با عبور از کانال ۶ درصد در پایان سال ۱۴۰۴، در تیرماه ۱۴۰۵ به ۷.۱۷ درصد رسید.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/680018" target="_blank">📅 17:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680017">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f2576f565.mp4?token=YPxQdIA5H7-2R2thSDfajxooIZcyF4_qiA6ZTRQ7TnmvVTduZL6dZ20I4kmaOqKGjDBRvApHbzEknaxdLWZ0Uhek6e2RJ67h0ye9FfrJsvsdHcwfK4cr3SB9NLIJVC99lToc3HgnHI_xhQt797ZcMKRdWOTbHFg-PXAFMYn4GDIDx4eCgXEo5L0FXSzz4y1jQDd3_kUISM3__FPMYLjd1eijaSvDb2OLo6e7HxDMrP4oGSQKeGBgCN7XCAM47f1XXH6i05QP0mIK7F34xQ__kJTdwooitQZccz7M0i5seeQ2gDjyEDdtLQ9-Dme8MnxUsWl58hnbxo8w0yUbSwCBrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f2576f565.mp4?token=YPxQdIA5H7-2R2thSDfajxooIZcyF4_qiA6ZTRQ7TnmvVTduZL6dZ20I4kmaOqKGjDBRvApHbzEknaxdLWZ0Uhek6e2RJ67h0ye9FfrJsvsdHcwfK4cr3SB9NLIJVC99lToc3HgnHI_xhQt797ZcMKRdWOTbHFg-PXAFMYn4GDIDx4eCgXEo5L0FXSzz4y1jQDd3_kUISM3__FPMYLjd1eijaSvDb2OLo6e7HxDMrP4oGSQKeGBgCN7XCAM47f1XXH6i05QP0mIK7F34xQ__kJTdwooitQZccz7M0i5seeQ2gDjyEDdtLQ9-Dme8MnxUsWl58hnbxo8w0yUbSwCBrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات اولیه زلزله ۷.۴ ریشتری کلمبیا
🔹
سازمان زمین‌شناسی آمریکا از وقوع زمین‌لرزه‌ای به بزرگی ۷.۴ ریشتر در کلمبیا خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680017" target="_blank">📅 16:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680016">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15e2b081d.mp4?token=j6_nKPqtPAqPd4qWHygxFSSVzpCSoel66Az-qrCNxD8qp_scdsOYJS8OQifoS2-pqxHtcR5fZgm2V7xcmcOkTWTeN1p2oqj2lhdn5KDpAtaDtctlR1VWzjZGyTKcK5K8YT2GLlT79DrbxgVZNLk5WPwgV8f9s9gixh5F8g5p8pkQqbh4H9qznsC9FuyQ2ZNckJTjP71RIgXqCxH_HU0z_KD_F4clH_7AjA4JT-18aJ5yNIJRPCEG9Mj4FfK52XFu0LNGqau8t7m0WOjF5RrYhqf2fk6vYCSDMbzHDOWvDFrUJYzht6-siHt35qc8Nv40xy2UV_HQumSOXJ8XhIdLvQrmUoRZcLCR1m8Yu2Bvg_pPtomq-grRsDJNE5NCNvTXfbIzFiURofc9Is3yxRkXmG7K5_EnmiKvmfvs7rSucf9mIQDbJcGUC8pnddmnfjiI0eJ7rByYxDeOukQWmkZoum4lCip1gBYM71L4njyQfZSZBIcGNQPGt4usT6NkedtyTExzt7eE13k9iTBWFfAmLmJiqkaSqUy955oESBWQwgy8S8p3jBZZvn3yhOYaj7KmNP-U-j6PQj9E2CYPuWvNoNnktbF5iAaXoZUt-0fZCEhin-MQj6gF0mzgZBztbU5L_Lq4AuWK74sN18WnR5NdRiJaBiayFwjF07rrbj8Fus8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15e2b081d.mp4?token=j6_nKPqtPAqPd4qWHygxFSSVzpCSoel66Az-qrCNxD8qp_scdsOYJS8OQifoS2-pqxHtcR5fZgm2V7xcmcOkTWTeN1p2oqj2lhdn5KDpAtaDtctlR1VWzjZGyTKcK5K8YT2GLlT79DrbxgVZNLk5WPwgV8f9s9gixh5F8g5p8pkQqbh4H9qznsC9FuyQ2ZNckJTjP71RIgXqCxH_HU0z_KD_F4clH_7AjA4JT-18aJ5yNIJRPCEG9Mj4FfK52XFu0LNGqau8t7m0WOjF5RrYhqf2fk6vYCSDMbzHDOWvDFrUJYzht6-siHt35qc8Nv40xy2UV_HQumSOXJ8XhIdLvQrmUoRZcLCR1m8Yu2Bvg_pPtomq-grRsDJNE5NCNvTXfbIzFiURofc9Is3yxRkXmG7K5_EnmiKvmfvs7rSucf9mIQDbJcGUC8pnddmnfjiI0eJ7rByYxDeOukQWmkZoum4lCip1gBYM71L4njyQfZSZBIcGNQPGt4usT6NkedtyTExzt7eE13k9iTBWFfAmLmJiqkaSqUy955oESBWQwgy8S8p3jBZZvn3yhOYaj7KmNP-U-j6PQj9E2CYPuWvNoNnktbF5iAaXoZUt-0fZCEhin-MQj6gF0mzgZBztbU5L_Lq4AuWK74sN18WnR5NdRiJaBiayFwjF07rrbj8Fus8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رئیس‌جمهور از دیدار ۷ ساعته خود با رهبر معظم انقلاب و تاکید ایشان بر حفظ وحدت و انسجام ملی و توجه به معیشت مردم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/680016" target="_blank">📅 16:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680015">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO2WlF3RIFQbgLD2sw_mCxMIGSWKxMfPUeg4PIXwQYU46dWPHxrpDsDjv9bvof_8vzNW77gn9gr3l_7jQ3WliUplQQ3uvluv8tHHHYdFNXefz2Bsoj7M8hIon4QybeKoI00m-ZL7QYkUbpFmJnzlzIrJO3HccieREc8FkUTC7Q9ANMUyWR8tNxm0J-9zcP9bSyizvV_SWV-BqNoe8FKsFXqyIONVezCsKo1EkgGHA70AdJcXMsYkjAX2Bes5pkdxcUhA06C3U2mtWSbsIVzJqJWyXHZsAUQKMYzxp9QTQWMQ3J5tmqmIq5XNvgd25vpy1VLbzIpHp-tiBDBENILcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: ایران در چارچوب توافقی برای بازگشایی تنگه هرمز، متعهد شده مانع عبور ناوهای جنگی آمریکا از این آبراه شود؛ اقدامی با هدف محدود کردن حضور نظامی آمریکا در خلیج فارس/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/680015" target="_blank">📅 16:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680014">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxKJibBbD21UNk5G60ZPYse05Ru35Cbe9CZhPmL8IIS5yomfA1cYtYRDD0SNMHdXoGgchaRPDfTLFMnW_fOydCPKyO_1q0vEELxoLp-NFoxCJmYWu2WnQ9wDYxJkmSkQ9Zleu_6269T-K19HsNc6zsEJVh9KHzN0kKvLQe6ruu1nZ76YShF1-6a8V1mI7TMSkOVRznVRR_OYhuoj6XsiB1KmS9Mwk0gUfzRV7D8PpJ77pAAbP-wdAfFcFLN4I-SN-SsMoELMeY8u1WsDC_vaGWZm-hcAYi5RO7dypaVDXq-44qARTWRWkM1vmo7ZWexf6cf4rE4fRrEnp0eJS7vg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت سالروز شهادت امام رضا (ع)؛ حاجت روا
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و از حاجت شیرینی که با عنایت و لطف امام رضا (ع) برآورده شده است، برایمان بگویید.
🔹
در ابتدای ویس، نام و شهر خود را بگویید و روایتگر کرامت و نگاه ویژه ضامن آهو در زندگی‌تان باشید.
🔸
صدای شما می‌تواند امیدبخش دل‌های بی‌قراری باشد که این روزها به سوی خراسان پر کشیده‌اند
👇
#حاجت_روا
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/680014" target="_blank">📅 16:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680013">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b1219c01.mp4?token=pd72VzqxZXAcP79Qk1_vv1KwvvVDWsXo83YqrAyGp5a6OtUhZw4DfUrbxgtmXGuM7zXWTkNSnvs7dP8yHbZlWlZDCWvXO7Hln3SGpPNB5-wbqbAUbc7Dbjqmxig6-dQP3YoZucEyMonVUHkQ3BAsa7KFF4vXKW4CoMTdhRNYJx0KozG4MArSp4wujo-FURqh8LJ_D-hgnQorVjfPzPlXQ59ADmXWPmWQiEEyuFrix9WRLhcUgD2G3VDP1cy8k5aa02bkAX0UnqoLBEaLwCNFyisGsMfr51cZL0o8PLWrX_bHHxzSVnIEaVgiqPiJoXX2wp2El0X6EQii93X6JdAV3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b1219c01.mp4?token=pd72VzqxZXAcP79Qk1_vv1KwvvVDWsXo83YqrAyGp5a6OtUhZw4DfUrbxgtmXGuM7zXWTkNSnvs7dP8yHbZlWlZDCWvXO7Hln3SGpPNB5-wbqbAUbc7Dbjqmxig6-dQP3YoZucEyMonVUHkQ3BAsa7KFF4vXKW4CoMTdhRNYJx0KozG4MArSp4wujo-FURqh8LJ_D-hgnQorVjfPzPlXQ59ADmXWPmWQiEEyuFrix9WRLhcUgD2G3VDP1cy8k5aa02bkAX0UnqoLBEaLwCNFyisGsMfr51cZL0o8PLWrX_bHHxzSVnIEaVgiqPiJoXX2wp2El0X6EQii93X6JdAV3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی عجیب از خانومی که بخاطر عمل زیبایی ماشین خودش رو زیر قیمت بازار فروخته!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/680013" target="_blank">📅 16:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680012">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loe2sDMMo8JdHjMlZxZiMX_qfnNllP4UlpbupWgxiN1jnVak3y_OKGp-BwyNb0jAc2WhfI05VhFEaP-Nk6SEV0IheEmD0TuujZGwvzfCc-ER4lvt6a_zxDubsekIo9Ak5t0-lxL_IHXYv8Fo_icmvizWV6EyFzBH2Ah9Cd0tMGn2mdlnwcZQFlDVWc9GRVYzOzBg4Ck3c7reQPpcnxlvPu7l18HLf50GH83sm8oMqt2EDteYqnPPsNkNcj1uUTH5civ1nRnaFN1SyM-DGFkBQCR0ppk5YsD00D53jIirR_s6Sf6g5AM7NcZsUIcWvqSB_qjX7NkLL0PRVd2s6pZN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهانبخش به اکسلسیور هلند پیوست
🔹
علیرضا جهانبخش کاپیتان تیم ملی فوتبال ایران، با عقد قراردادی به اکسلسیور هلند پیوست و بار دیگر به فوتبال هلند بازگشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/680012" target="_blank">📅 16:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680011">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156dbace98.mp4?token=txic4fgf0JGklJyq40DpDHlRuPVlN4Hw_paQ3p7744sKJpacPf5L5RWceQW03wWHn7dNo_x_LDlbU51t71CePEk78l3u1BpTDMrBwmlO0rtFb58zVV3nQYU1pIJXyCl3QMR83IZ3JMIrFe_6XXsu1pd5N2o-91M5X5QHRS8G4DPpHX1su2dRHQBMEkwTMCxdHdWgV_VoMcSxbEKAMSgyNuoKNqQJUOH2wTFqktXV3El7kYMekunXDKOvlbe_72dGMNrTsmv1hpgrOTDq8EAHUf9j6oS-fwhI3k7dZY5z-_gSuWBMNL-RC7sFUmYLeaHNf6wzz68kO8hDRceSiZZnJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156dbace98.mp4?token=txic4fgf0JGklJyq40DpDHlRuPVlN4Hw_paQ3p7744sKJpacPf5L5RWceQW03wWHn7dNo_x_LDlbU51t71CePEk78l3u1BpTDMrBwmlO0rtFb58zVV3nQYU1pIJXyCl3QMR83IZ3JMIrFe_6XXsu1pd5N2o-91M5X5QHRS8G4DPpHX1su2dRHQBMEkwTMCxdHdWgV_VoMcSxbEKAMSgyNuoKNqQJUOH2wTFqktXV3El7kYMekunXDKOvlbe_72dGMNrTsmv1hpgrOTDq8EAHUf9j6oS-fwhI3k7dZY5z-_gSuWBMNL-RC7sFUmYLeaHNf6wzz68kO8hDRceSiZZnJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایده جالب برای بسته‌بندی محصولات کوچک
🎁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/680011" target="_blank">📅 16:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680009">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
الجزیره: ترامپ لحنی آرام‌تر نسبت به تهدیدات قبلی خود در قبال ایران در پیش گرفته است
«نورالدین بوزیان»، خبرنگار الجزیره در واشنگتن:
🔹
از یک نقطه عطف در موضع آمریکا نسبت به تهران خبر داد، جایی که دونالد ترامپ، رئیس‌جمهور آمریکا، لحنی آرامتر و کمتر تند نسبت به تهدیدات قبلی خود در پیش گرفته و بر گزینه فشار اقتصادی و محاصره دریایی به جای تشدید نظامی مستقیم شرط‌بندی کرده است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/680009" target="_blank">📅 16:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680008">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7557a5a45e.mp4?token=W6CsG-FlFumz2e9H8lPmfbq--1TnBe-JLp6BYr3qmoeMYLBWkfqrB8rDTFUL8hq4iuKZHrHtLOt9gXuzR54iwQog-SG1BJRr1I6ge487LU_Nww_Ja7uF1jbgVfkGSvXlUBGluIsFKMt_beqd5egKOAzwN1G1ASI3DPlUMSJ7NHTRaWd31fMhQU3rBoQBpSR0R9iiHMpJ0NHntryLdYoFZ2gYjzJagfSmHtGVd1UNoYVX8x5ggCgznVzxzq8rSeqKkTaCohVjoXOCTiP51r83TY0Dj1g_Rns998bE4a-iXGqgKWDmeJ1gdRniHBG_l0w2NfowrTc0OnIUzH8wjW5Kzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7557a5a45e.mp4?token=W6CsG-FlFumz2e9H8lPmfbq--1TnBe-JLp6BYr3qmoeMYLBWkfqrB8rDTFUL8hq4iuKZHrHtLOt9gXuzR54iwQog-SG1BJRr1I6ge487LU_Nww_Ja7uF1jbgVfkGSvXlUBGluIsFKMt_beqd5egKOAzwN1G1ASI3DPlUMSJ7NHTRaWd31fMhQU3rBoQBpSR0R9iiHMpJ0NHntryLdYoFZ2gYjzJagfSmHtGVd1UNoYVX8x5ggCgznVzxzq8rSeqKkTaCohVjoXOCTiP51r83TY0Dj1g_Rns998bE4a-iXGqgKWDmeJ1gdRniHBG_l0w2NfowrTc0OnIUzH8wjW5Kzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش عجیب از «مستراح سنتی» در تلویزیون ملی بریتانیا
🔹
در اقدامی که برای بسیاری از بینندگان غیرمنتظره بود، تلویزیون ملی بریتانیا در گزارشی به شیوه استفاده از مستراح سنتی پرداخت!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/680008" target="_blank">📅 16:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680007">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ibe1oxfyBXTy_rrOH6TI3roDs95GtxKHK5G3o3iFs9koBVlgLpEO66gDbgCvIMOcxijMa3AwPNyzAcej-z8XNHP-rnR_gCWIQ3HfiklwtgCUUya_PBm-uDTCFlyBOJ29sBr5tWdAfh6J3G-aKM4fmRkTJWtSf5M6hmKJvQ8PlY-N4ur9xAOFORKEWlhXQtuff3h1iRmvTadX29mr2gACccwmHyGk-FnZeVvCCWXD2QDuNXNxXS-A0IcLchQon4kIWCX_76OdUvIkbrqEwg4DQl7X_WpxnP_HUf5LXoyNkWm1bKqrMvnaWir7SwI8qMgoY-RZRM4Kqe-Et1LXh4XQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آیا می‌توان با ۱۰۰ هزار تومان طلا خرید؟
صندوق‌های طلا با پشتوانه فیزیکی سکه و شمش و امکان خرید از ۱۰۰ هزار تومان را دارد که امکان پس‌انداز تدریجی طلا را فراهم می‌کند.
رشد قیمت صندوق‌ها مانند طلا است، مثلا صندوق «رز ترنج» بازدهی ۱۲۶ درصدی داشته، اما چگونه می‌توان صندوق طلا خرید
👇
👇
👇
📌
آموزش نحوه خرید صندوق طلا را اینجا ببینید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/680007" target="_blank">📅 16:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680006">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785faa238a.mp4?token=qBnzchO4JPMrp-QjYnDlGDSVZIHFet0QTvJzQBD2cZY0B4-D5AEiWpFJQv6lAk8_J1yYpAPGNl79trnbQp7RZG3s-TWYycBh3oNyvJxa8wTgeRb7xaRPjFEr8jNQ4Rrfx3D2VBe5sdjk8V1WdgYgqnDj_8ZbulPBfQ6paAhniH1tHW37iW8krYGCI0iAVp8YlcIrU7l2h946KD_4v4Jjlxdl6Xxcl6-gdHOnS59mI6Z38iZTRldbzErpusO4NuIPP-M_Dk4oZ8U97AI3iYJ3gMOwvAwaCaJi4C22NXYQ9bV0XmEGBUltVhgBrKjLOgtehL8FJd_QmmzToiJpjcX-jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785faa238a.mp4?token=qBnzchO4JPMrp-QjYnDlGDSVZIHFet0QTvJzQBD2cZY0B4-D5AEiWpFJQv6lAk8_J1yYpAPGNl79trnbQp7RZG3s-TWYycBh3oNyvJxa8wTgeRb7xaRPjFEr8jNQ4Rrfx3D2VBe5sdjk8V1WdgYgqnDj_8ZbulPBfQ6paAhniH1tHW37iW8krYGCI0iAVp8YlcIrU7l2h946KD_4v4Jjlxdl6Xxcl6-gdHOnS59mI6Z38iZTRldbzErpusO4NuIPP-M_Dk4oZ8U97AI3iYJ3gMOwvAwaCaJi4C22NXYQ9bV0XmEGBUltVhgBrKjLOgtehL8FJd_QmmzToiJpjcX-jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با سرمایه کم، یاد بگیریم دارایی‌مون رو زیاد کنیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/680006" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680005">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر کار: پرداخت معوقات بازنشستگان احتمالا از دهم شهریور آغاز خواهد شد
🔹
نتایج آزمون ورودی پایه دهم مدارس نمونه دولتی و تکمیل ظرفیت سمپاد اعلام شد
🔹
سخنگوی دولت عراق: هیچ اطلاع قبلی از حمله سعودی آمریکایی به مواضع حشد الشعبی نداشتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/680005" target="_blank">📅 16:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680004">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7a5d5e08.mp4?token=viluDPE6xkKOS41ahDCfMrQepV_NE7QjVCq44jd1NtsGXi29A1Xxsi11eyGexz8wEr6Zlb-_zF-j9wL7RL3xgHtWnenmfO4uLsITmPtzoWffTObprri0ge1Y60Y3PSidW_vNkSLfhCb2eZ8fQCF-rndHqlwS_Svhfr-NhecVFexaFsGafopuV1ch3dZfY8Sppk2J6k7gZc_wOx6odohI214M-dIjo_klk3-rDwcCN6GI-iu5JyOiB-_cValwvDRUZtxXff13jChCG2c-6pV3a88V-CF-O_vbS6UIwDxJp4FHZ8AtVtl8wmIsV2bbNxCEIJ-Q7fDIgBQ-UFgUfkzncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7a5d5e08.mp4?token=viluDPE6xkKOS41ahDCfMrQepV_NE7QjVCq44jd1NtsGXi29A1Xxsi11eyGexz8wEr6Zlb-_zF-j9wL7RL3xgHtWnenmfO4uLsITmPtzoWffTObprri0ge1Y60Y3PSidW_vNkSLfhCb2eZ8fQCF-rndHqlwS_Svhfr-NhecVFexaFsGafopuV1ch3dZfY8Sppk2J6k7gZc_wOx6odohI214M-dIjo_klk3-rDwcCN6GI-iu5JyOiB-_cValwvDRUZtxXff13jChCG2c-6pV3a88V-CF-O_vbS6UIwDxJp4FHZ8AtVtl8wmIsV2bbNxCEIJ-Q7fDIgBQ-UFgUfkzncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله توپخانه رژیم صهیونیستی به منطقه «بنی‌حیان» در جنوب لبنان
🔹
منابع خبری با انتشار ویدیویی از حمله توپخانه نظامیان رژیم صهیونیستی به منطقه «بنی‌حیان» در جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/680004" target="_blank">📅 15:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680003">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428feada65.mp4?token=GJ3v-Q5zTkmoLR7A2NJTKTuApTE8rte3hB3vj192bdTFEHRhYl1FSRRqVjJKOOPxxWG4paQuEZGeRrmM_a9AWON0wABeTMfC2PtBvXH_u1yKAOxAKJtYt_j_kmTVMLhbIODG5FjJCAAMR-EiJE84NRQcqAHjBMKagE4_DbOk2gf4pzSLZRGz7qEYDQLNYslHMGkQxjC2_dThCqv-p2zp8Jij7UXV8LO9bnTOhk1zA6DZn5WpoMMb-WlNyecPnbZjq67fVF-sM70qc8Sk6_HWQvHnUO0pdBMdqT0qa_3tWS0xodw1uJH0RwDYQ4WHME0ZHSowWcArgMnfIhZbgli6MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428feada65.mp4?token=GJ3v-Q5zTkmoLR7A2NJTKTuApTE8rte3hB3vj192bdTFEHRhYl1FSRRqVjJKOOPxxWG4paQuEZGeRrmM_a9AWON0wABeTMfC2PtBvXH_u1yKAOxAKJtYt_j_kmTVMLhbIODG5FjJCAAMR-EiJE84NRQcqAHjBMKagE4_DbOk2gf4pzSLZRGz7qEYDQLNYslHMGkQxjC2_dThCqv-p2zp8Jij7UXV8LO9bnTOhk1zA6DZn5WpoMMb-WlNyecPnbZjq67fVF-sM70qc8Sk6_HWQvHnUO0pdBMdqT0qa_3tWS0xodw1uJH0RwDYQ4WHME0ZHSowWcArgMnfIhZbgli6MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دارو چطور در بدن پخش می‌شود؟
🔹
این همان چیزی است که وقتی تزریق می کنید داخل بدن‌تون اتفاق می‌افتد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/680003" target="_blank">📅 15:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680002">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پدر مبینا زارع: متهم مبینا را در کارگاه کوره‌ آلومینیوم‌پزی پدرش سوزاند | قبلا هم مبینا را با اسید تهدید کرده بود
khabarfoori.com/fa/tiny/news-3176216</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/680002" target="_blank">📅 15:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680001">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d8e98d63.mp4?token=THh5CgTCBvfTMBRgzCK7UgSVtB9OzwjTU457gaAOaE_VOzXhQvk9_eStj1KfvGBYE6uP7jkpmjSHaP3Ebdm93Vc9a-x40WziJRMaDaMSjkcL_TVMysADjb5Hkwby5jq8xWCq0YS6PDIJsBbtI2SOtdL0aNddgAMbeKSKzzWRpm68N1ugGBj3hyN9eS-_i9hJ9QnZ7T0z40BSLzOfeRnyGEq0Ai5y-YiXOxjveTl6q0mqgbuFgsly49tpKdzFjt4A1Ip3Y1iwV1Du6LHjubA5FbmmVtWVPX8ItUuuBlzm_fzLj4YKKLIg9vicNVni0Y8cbS-UKXnlkd6v1kYkELxHAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d8e98d63.mp4?token=THh5CgTCBvfTMBRgzCK7UgSVtB9OzwjTU457gaAOaE_VOzXhQvk9_eStj1KfvGBYE6uP7jkpmjSHaP3Ebdm93Vc9a-x40WziJRMaDaMSjkcL_TVMysADjb5Hkwby5jq8xWCq0YS6PDIJsBbtI2SOtdL0aNddgAMbeKSKzzWRpm68N1ugGBj3hyN9eS-_i9hJ9QnZ7T0z40BSLzOfeRnyGEq0Ai5y-YiXOxjveTl6q0mqgbuFgsly49tpKdzFjt4A1Ip3Y1iwV1Du6LHjubA5FbmmVtWVPX8ItUuuBlzm_fzLj4YKKLIg9vicNVni0Y8cbS-UKXnlkd6v1kYkELxHAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین ترکیب طبیعت: پلاتیپوس؛ هم تخم‌گذار، هم شیرده، هم سمی!
🔹
این پستاندار آبزی استرالیایی هم تخم می‌گذارد، هم به بچه‌اش شیر می‌دهد، منقاری مانند اردک، پاهای پرده‌دار و دمی مثل سگ‌آبی دارد. جالب‌تر اینکه نرها روی پاهای عقبشان خار سمی دارند! انگار طبیعت چند حیوان را در یک قالب خلق کرده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/680001" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680000">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syH2BngPmcSpMXUY8CaTQ4maEUQov1P-unXrRywmMp-ARVgeh2dXZXuUbP0NyrubtN_hPKknZrrwa6IumHWUlO2Ey97jsDp6Afupp_abJFP2K_bakgY9yKL8Wu_6-IhIswCHhzkr9GuSMZkuI7Iq5zCbVoA-pI2ciRrgJgO5jk14GgfG_aXJhc1MK5Z6yNL0ObJdeGJ5qEOQpFdGm7Goqe9neZ9PWKnw1WPHgzIOLt647kc-FR_3xz2LvGK13HfoAK_u4Sj3avOxqaKMGVopTaGX_D5Mt3EiVhJnFsV4twGG4IotNmoxWI1UgXPTQA45ay5OtZ4Lei3ZWV30NXxfuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: هیچ قدرتی نمی‌تواند مردم ما را وادار به تسلیم کند
🔹
مردم با حضور در میدان، تهدیدها را به فرصت تبدیل کردند و همۀ معادلات دشمن را با وحدت و همدلی شکست دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/680000" target="_blank">📅 15:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679998">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران، راهبری مسئولیت اجتماعی برای آینده پایدار اقتصاد
🔺
واحد مسئولیت اجتماعی اتاق تهران با ترویج پایداری و اجرای برنامه‌های اجتماعی، نقش بخش خصوصی را در توسعه پایدار اقتصاد تقویت می‌کند. برای کسب اطلاعات بیشتر اینجا
کلیک
کنید با شماره (داخلی۱۶۵۱)۰۲۱۸۸۷۱۹۰۱۱ تماس بگیرید.
https://t.me/TehranChamber</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/679998" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679994">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSQznovN28jPGzFqUJdUZMItTdWaNNliV18QGvlGDJ4tgf_RZJJMcSjSY5OoSRn7SD5BYp5eG5W4MN4wBQWMZ7APlwU8D5YI3nbDEzM5ObKuSmnXlXHzWS9tT79eDxTUb8LZN7hj31cEtf5sbesSWi5mGgwynrpWYpsWwLv3bXMZ6OllC7b9eYxLOhCVD6md75SwVd7JksoLxd4dh0Cil1r4llHXhogqnYSwJTQA6edb7XcAqrvVoZFGziRbQVQ4z2kELf7sFdn2ASRc8imyQnUuEO_3oVzcCQ2a4S8eniCFHQ7iQK0oIpVGy6_D37SXQjDAqDV4jtF7AKYn5GRXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qq8Qq_SxPT3gUFk3N39Z-pd1SAPhcadOQyvsdKF_XH4aY53sXhllQRtip2dA21akspm_z-EW01SrPGm7WMxav6f9pT5yt-kSlVCV_C3xRC5Xx8Ni6PVWe1RmapnHbGVkM6pdt_BTwGmKNBKSyk47zq6rSW_60UiBcd0Ze-3VdWogRIiO2hopTDNXOQ-90UJV7E67uxoN4r8h80bkI_y9w1ATdrmRyzkJn2lJC8D00WXGAKZTKHtqddJzlrhi6mKmeyUzZSYSTgKIu12WOAJZXYdD8YVzwpQOoK2rYVLkKH5J5tocrnSu27ZgWryknr_PW8GdvNxbUYIWRg-62HRiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fY7zukPvwrEuhIY2nGFtE0q_h2KHcbWkgaElAJXHlEpA-F8vyTuwoI2AqHgr0iDNkAs_Ug5uhTQDBNHNgeTqe-ggifc3bj3a96q794xZ7EXm-DeTYJd9_vN-uMxxdtKMiLFfvgBO9Ps2aUSIxcX3THnAwIpF0kjcmnStbp2Z_q1E_vWmb_pzaeegXl1l9SZiGqWIKrZWSe_9QLW34tVoOJfgyV9FWBNgxMrf9L-l639i1Hsbz9sIZMSNkB8iv4f2xEWP02uUz-o1lAKsRLkgdGER9exF7SAQCXgKSsVwPPajOuoEpu5K3r2H7aZZOJM4hSqIM3HFcH75m9pymVM99A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cee229a5.mp4?token=HilZV0DvcRQMw_UdJZ-vd8LwjdpsyslWPJX_C43whIyO74IucomRKolD42v6mOeYzhOjCxhwGzuxYKDhi80RfZyp6_xAoBPxqugYXcuNA0epFcxkFGy6pwowDA0lQNwbhRskevL0r0aZQ-idYtS9OH5Y8J0fFBIhSp8sL23yps9PTU7BrP7Dm6q5D-D21n4FwIj5D389GDAAClqSEjr6aBU6uZu7e822iqKaI-erpuITPqX7-s7HnbE-49bBlCusxPIVONOUekn8OxDTcFdjrkWH9PQ45k52Q3Ex_DmhZowg4uKgEM5s0pY6-0x_B4vlR_vdhb9aaIZIBaxoohaTrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cee229a5.mp4?token=HilZV0DvcRQMw_UdJZ-vd8LwjdpsyslWPJX_C43whIyO74IucomRKolD42v6mOeYzhOjCxhwGzuxYKDhi80RfZyp6_xAoBPxqugYXcuNA0epFcxkFGy6pwowDA0lQNwbhRskevL0r0aZQ-idYtS9OH5Y8J0fFBIhSp8sL23yps9PTU7BrP7Dm6q5D-D21n4FwIj5D389GDAAClqSEjr6aBU6uZu7e822iqKaI-erpuITPqX7-s7HnbE-49bBlCusxPIVONOUekn8OxDTcFdjrkWH9PQ45k52Q3Ex_DmhZowg4uKgEM5s0pY6-0x_B4vlR_vdhb9aaIZIBaxoohaTrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام ایستگاه پمپاژ شرکت STAR ENERGY زیر مجموعه شرکت ADVARIO در بندر جبل علی امارات متحده عربی در جریان جنگ رمضان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/679994" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679993">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d332845585.mp4?token=fwei3MYjSJKXpdF7Ycs3UfBFKl1k1C61rj8j59XtykLhXEtvnaWyPd5k6nXUDpkOG7oGIy5vYMzkbF1TALRfZLyoBXIs4ecII2n5GDnAlPysaEZUZ0XzWht-eaXb11vVskYbozTErmU9rnmi2odlY66upkFd6tYilIFEbyFuZnkIapF6T2G0cRy3VQxRCctIP1MRs9Sa18XlGxTX3_Q6XwXkL0S_Q0G7PE6B8bR6UenT6PjKCv-P0eBkECeFp__yXzJZFh_pOkvKYirsiPy-Kn6MZLItJom8Po7DcYx_pJdNdWJXVsoIy8Oehi0oTk1U7npqQqWpt1BHxsxnihxG1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d332845585.mp4?token=fwei3MYjSJKXpdF7Ycs3UfBFKl1k1C61rj8j59XtykLhXEtvnaWyPd5k6nXUDpkOG7oGIy5vYMzkbF1TALRfZLyoBXIs4ecII2n5GDnAlPysaEZUZ0XzWht-eaXb11vVskYbozTErmU9rnmi2odlY66upkFd6tYilIFEbyFuZnkIapF6T2G0cRy3VQxRCctIP1MRs9Sa18XlGxTX3_Q6XwXkL0S_Q0G7PE6B8bR6UenT6PjKCv-P0eBkECeFp__yXzJZFh_pOkvKYirsiPy-Kn6MZLItJom8Po7DcYx_pJdNdWJXVsoIy8Oehi0oTk1U7npqQqWpt1BHxsxnihxG1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشای چهره وحشی آمریکایی‌ها؛ از ویتنام تا امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/679993" target="_blank">📅 15:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679992">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba76786ce.mp4?token=hePW2MvCASeSWcXt-JLcvd4Z5QmftboDAkfhdQ8HH7Xxv1ibnovOar7T2OLLPgGlvl_nQqR-bST8P2liegIZrgGFAPZcXRlSEkF2kCGtBjYDsfrfYxOIHbyJ5BRJF7q8J2fA2jxhjN8wFj3sCdFD9uMl4Ajd-RR6xpHl1YNbn9A9yL-Ff5XGINzhXjnqqzrmLM_XDjw5gv6kJo-9jxR8zxgVl9UFKf-wlXr5ns-AEhtoksJ1C3XvO9YYlRV8Rv0xuIMvrnn1LIWkb7ULOu56jVG1vEPLjabZJm0_Lbi_K6J7b_FXcAt9dKdSwTYgWuyLKBYIOp0kXWKPY6Qb3cBoEBVQGBUIsbScqxQsFOshCjshzXILmENEFjL-LambBDDQYFBybkN1Pu5RQmbhU4jxL-tXS2FSHvQah0l_YWlxxvcppOaVY71Kzn9mospM8zScypH0o0bQ643aCOfZEZ6IPEcgzgPFyxGiFidaLUurZwC3nusSz5cH7PawM8urkaJ5HQkjQWJvxYQbBuiCdz9p2mxy1wS7-62RcWVSt1zy1RDjnBaMT6XPHnyr0dxiqA8WDWnJlXCXbbGYAfaav8nY29rINo3Tkc-eRQ5z-OKYDSQ3t-APcfiAv3hSmBmsV_46gECEjU-WWbSv8wqcl-oWJfrGRbhCk15IfsDvv6Zz4vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba76786ce.mp4?token=hePW2MvCASeSWcXt-JLcvd4Z5QmftboDAkfhdQ8HH7Xxv1ibnovOar7T2OLLPgGlvl_nQqR-bST8P2liegIZrgGFAPZcXRlSEkF2kCGtBjYDsfrfYxOIHbyJ5BRJF7q8J2fA2jxhjN8wFj3sCdFD9uMl4Ajd-RR6xpHl1YNbn9A9yL-Ff5XGINzhXjnqqzrmLM_XDjw5gv6kJo-9jxR8zxgVl9UFKf-wlXr5ns-AEhtoksJ1C3XvO9YYlRV8Rv0xuIMvrnn1LIWkb7ULOu56jVG1vEPLjabZJm0_Lbi_K6J7b_FXcAt9dKdSwTYgWuyLKBYIOp0kXWKPY6Qb3cBoEBVQGBUIsbScqxQsFOshCjshzXILmENEFjL-LambBDDQYFBybkN1Pu5RQmbhU4jxL-tXS2FSHvQah0l_YWlxxvcppOaVY71Kzn9mospM8zScypH0o0bQ643aCOfZEZ6IPEcgzgPFyxGiFidaLUurZwC3nusSz5cH7PawM8urkaJ5HQkjQWJvxYQbBuiCdz9p2mxy1wS7-62RcWVSt1zy1RDjnBaMT6XPHnyr0dxiqA8WDWnJlXCXbbGYAfaav8nY29rINo3Tkc-eRQ5z-OKYDSQ3t-APcfiAv3hSmBmsV_46gECEjU-WWbSv8wqcl-oWJfrGRbhCk15IfsDvv6Zz4vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رئیس‌جمهور از دیدار ۷ ساعته خود با رهبر معظم انقلاب و تاکید ایشان بر حفظ وحدت و انسجام ملی و توجه به معیشت مردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/679992" target="_blank">📅 15:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679991">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TckD2PwykbqhqkoBttDMUKbb6pNGjRdjT_ydVN6wnfdoBpfbjQAn23wo3PapO_WFBDFnDG1HUrk7kjyO7rO-mCmPdSHce3yBVvtjEh5fpa39e4_1gKAPLNnKPFQVRcfOs9P8FTZlxZECdxSasrJe-GMidwrwzO5IGn7uBjqPfz-eydZo3Z_sr2OQnl9WjGr7ZtEzDaxdaySR0idy5sEV-Tgu4lX4KwkeGlgG7-BOCqKnaFBWO1wNhSvGfZF7LF-B7NeZ7Yy1wGEqvVrttQ5B12gl35_Xky-rOJ0Oer62Endy7RbchJZx3OwvfyYvcESxezqe70_pD6ggWcIvth1_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ فایتر ایرانی در مسکو برای کمربند قهرمانی
🔹
امیر علی‌اکبری، قهرمان اسبق کشتی فرنگی جهان، شنبه ۲۴ مرداد ۱۴۰۵ در مسکو برای کمربند سنگین‌وزن سازمان ACA با علیخان واخائف (قهرمان فعلی) مبارزه می‌کند. این دیدار اصلی رویداد ACA 206 خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/679991" target="_blank">📅 15:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679990">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
دادسرای جنایی: جنازه حمیدرضا رجب‌زاده اطراف تهران کشف شد
🔹
ساعتی پیش جنازه حمیدرضا رجب‌زاده در اطراف تهران کشف و به پزشکی قانونی منتقل شد.
🔹
در پی قتل فجیع حمیدرضا رجب‌زاده و در دسترس نبودن پیکر وی، سرانجام با دستور قضایی و اقدامات جنایی پیکر وی ساعتی پیش…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/679990" target="_blank">📅 15:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679989">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b60ca78f.mp4?token=SII8Ij8RQS5j5MrQXVpZlDkC2J6cGho3lQbYnS3t_tAWzXcwQj_NqKB2wIEvtsr6wyqT_9lGb2uPudLnIvH4RATQFgEXTYfvk6L1XpLR3q-avDkVBNO1KM0rugt5hoCFPRleonBFDPR3OeDNZlqWALfTGhtsiJoqo6ea4qczfAVNCF7zHkeKageEXo0cQnic0B8Png4XouoRAtxf6Wol7_SpQwpa4h8olxQ5iZd-XqdQnkDNml72GnahxG-JW5Xw-40QZka7XcfbRFTo9J_QXdpROAzDi-6C09ZGB8csl8vAuOYbR8-IOxPT1BUoyWtr9jMiVIJ7xp37aj4f6JF5Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b60ca78f.mp4?token=SII8Ij8RQS5j5MrQXVpZlDkC2J6cGho3lQbYnS3t_tAWzXcwQj_NqKB2wIEvtsr6wyqT_9lGb2uPudLnIvH4RATQFgEXTYfvk6L1XpLR3q-avDkVBNO1KM0rugt5hoCFPRleonBFDPR3OeDNZlqWALfTGhtsiJoqo6ea4qczfAVNCF7zHkeKageEXo0cQnic0B8Png4XouoRAtxf6Wol7_SpQwpa4h8olxQ5iZd-XqdQnkDNml72GnahxG-JW5Xw-40QZka7XcfbRFTo9J_QXdpROAzDi-6C09ZGB8csl8vAuOYbR8-IOxPT1BUoyWtr9jMiVIJ7xp37aj4f6JF5Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنالیز بی‌بی‌سی از ادعاهای ترامپ: جنگ روانی برای پوشش بن‌بست‌های آمریکا
کارشناس روابط بین‌الملل در بی‌بی‌سی:
🔹
ترامپ ۶ ماه است که مدعی است تمام مشکلات ایران حل شده، ما آن‌ها را شکست دادیم و تنگه هرمز در حال باز شدن است؛ در حالی که حتی مسئله هسته‌ای نیز برخلاف ادعاهای او حل نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/679989" target="_blank">📅 15:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679988">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سخنگوی سپاه: موشک‌های ایران قابلیت‌ تغییر مسیر دارند
🔹
موشک‌های ما قابلیت هدایت دارند و حتی برخی موشک‌ها می‌توانند در برابر سامانه‌های پدافندی دشمن تغییر مسیر دهند
🔹
حتی اگر برای موشکی یک هدف مشخص شده باشد، می‌توانیم آن هدف را در میانۀ مسیر تغییر دهیم و هدف ثانویه‌ای برای آن تعیین کنیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/679988" target="_blank">📅 15:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679987">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c92dd8ed3.mp4?token=Trr084xFkgaLrtwmSH7Ki-52Hn6VDfpMWOJSX3hsFOrGDwxW1iBu93-6REIwg5ewerEL7i1sGoXnxM_yE98ohbwtcA557K3fJe5sM6t0FmL-SDcbZHioC2Z7fY_FoFUGKlZ8gdPziMKXGNVR_NfuIkgq6PvpwZQeRfI1nTYteJEbx5iPFghXB4KmGHQhebIQJrqCER-S216WfSZCixVDhODi5LgNyV015E0dqLfomyl4s1Ls8mUTCqkNxPf74gVQMaF9W6CL6YM81GaJPIX6U8PS5-VkMnYu_XmjxRSSP2vsf0UCAOiK87_Oq-GBI1CpzSoHzaNK2Nvo898fVAb7_VwZnBGG2I7HWasCcgUcV6ybqis0ZEnmhOHXz9QLvJZ5_00Bn2bQjsaxxX0ze_TOREo5ANadhNKrh0e5dYlGsF8GcgvfGqgRl0GjHyjNQr145P4P1Q8ljprhZjTOMk2VkGZYNPWq4Hob5DmOm262dJ9XadR1lvc7Vxa18yxaXX_zxl6Qzjn1CsXe1C9_qF2LJlFE3OSJqjrEDnfb4KsIpPzJ9atBqDu9MsaWJ8LqGF3ohw_iK1ZHjWhoexItoQnmvek37Brpbmg8IlDZCyuDPUzIiuWxNiESh8haqjjGSPwTupOSoPf_T6WvbV1NwrQi-di5xQrwlJsc-whr8t0q7CI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c92dd8ed3.mp4?token=Trr084xFkgaLrtwmSH7Ki-52Hn6VDfpMWOJSX3hsFOrGDwxW1iBu93-6REIwg5ewerEL7i1sGoXnxM_yE98ohbwtcA557K3fJe5sM6t0FmL-SDcbZHioC2Z7fY_FoFUGKlZ8gdPziMKXGNVR_NfuIkgq6PvpwZQeRfI1nTYteJEbx5iPFghXB4KmGHQhebIQJrqCER-S216WfSZCixVDhODi5LgNyV015E0dqLfomyl4s1Ls8mUTCqkNxPf74gVQMaF9W6CL6YM81GaJPIX6U8PS5-VkMnYu_XmjxRSSP2vsf0UCAOiK87_Oq-GBI1CpzSoHzaNK2Nvo898fVAb7_VwZnBGG2I7HWasCcgUcV6ybqis0ZEnmhOHXz9QLvJZ5_00Bn2bQjsaxxX0ze_TOREo5ANadhNKrh0e5dYlGsF8GcgvfGqgRl0GjHyjNQr145P4P1Q8ljprhZjTOMk2VkGZYNPWq4Hob5DmOm262dJ9XadR1lvc7Vxa18yxaXX_zxl6Qzjn1CsXe1C9_qF2LJlFE3OSJqjrEDnfb4KsIpPzJ9atBqDu9MsaWJ8LqGF3ohw_iK1ZHjWhoexItoQnmvek37Brpbmg8IlDZCyuDPUzIiuWxNiESh8haqjjGSPwTupOSoPf_T6WvbV1NwrQi-di5xQrwlJsc-whr8t0q7CI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری رییس کمیسیون عمران مجلس
:
خیلی از پروژه‌ها را در کشور که اولویت نداشتند، به دلیل فشار و لابی شروع شده است
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
خیلی از پروژه ها در کشور در اولویت نبودند یا نیاز کشور نبودند، اما با فشار افراد مختلف این پروژه ها را در کشور داریم؛ از جمله فرودگاه‌ها ، سدها و غیره.
🔹
از سال گذشته دولت سختگیری می‌کند که پروژه جدیدی شروع نشود مگر اینکه پروژه قبل تمام شود‌.
🔹
دولت هم نباید از زیر بار نیاز یک منطقه به یک پروژه عمرانی به این بهانه فرار کند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/679987" target="_blank">📅 15:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679985">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دادستان کل کشور: قرار نهایی پرونده مدرسه شجره طیبه میناب به زودی صادر می‌شود
🔹
انفجار کنترل‌شده مهمات عمل‌نکرده در بندرکوهستک سیریک امروز انجام می‌شود.
🔹
خودکشی نظامی صهیونیست؛ هاآرتص: آمار در ارتش اسرائیل نگران‌کننده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/679985" target="_blank">📅 15:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
وال استریت ژورنال فاش کرد: ۴۲ هواپیمای آمریکایی در حملات ایران منهدم شدند یا آسیب دیدند
وال‌استریت ژورنال:
🔹
حملات ایران (بیش از ۲۰۰۰ حمله در منطقه) به ۲۰ سایت آمریکایی در ۸ کشور آسیب زده، ۴۲ هواپیمای نظامی آمریکا را منهدم یا آسیب‌رسانده و ۱۳ میلیارد دلار خسارت تجهیزاتی و تأسیساتی به آمریکا تحمیل کرده؛ درحالی‌که پنتاگون برای دفاع از پایگاه‌هایش آمادگی کافی ندارد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/679984" target="_blank">📅 15:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c9a00d27b.mp4?token=nRoX3rDaTJHtUTEBNwwxwG_QyoxLO1okg5jTbr_xGEBo7NumpwhMA3Ayw8_Oy-kGRgFxCO_4eLphobU2k12SQRoah-RNKQQ8Xkwlw99qMe5P-x29r0RFn3pNlLs29cY1x0uPbKsE_pl6kEfbDw788fyM0blw6ZGKnngTFIKsyRoJ3-n01Rxk80iN4z8ra5rNNO4-M3gPQR7Ur-MiUWdD7CTTVHsclPQcJxQfeUrHdJ0zozMJpCTNOjPFmT_tHYvOzycKFf7f9tbZZ4bT91gTxBRNbjwOuJHDCP9e6ricEuuKQ33SZLtGBxe_h0QGdAYM_s16N-GfiM_xNa3dEKK-yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c9a00d27b.mp4?token=nRoX3rDaTJHtUTEBNwwxwG_QyoxLO1okg5jTbr_xGEBo7NumpwhMA3Ayw8_Oy-kGRgFxCO_4eLphobU2k12SQRoah-RNKQQ8Xkwlw99qMe5P-x29r0RFn3pNlLs29cY1x0uPbKsE_pl6kEfbDw788fyM0blw6ZGKnngTFIKsyRoJ3-n01Rxk80iN4z8ra5rNNO4-M3gPQR7Ur-MiUWdD7CTTVHsclPQcJxQfeUrHdJ0zozMJpCTNOjPFmT_tHYvOzycKFf7f9tbZZ4bT91gTxBRNbjwOuJHDCP9e6ricEuuKQ33SZLtGBxe_h0QGdAYM_s16N-GfiM_xNa3dEKK-yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی هیئت رئیسه مجلس شورای اسلامی: معاهده کنوانسیون خزر یک معاهده پرچالش است که باید در مجلس تصمیم‌گیری شود/ فعلا لایحه‌ای رسما ارسال نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/679983" target="_blank">📅 15:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679982">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_9VXOTJSbpQpE_G8n5hWWdd2nAwsozJOC7TM1QQ-6R12rafDzTAOtqRp_34qYAs2RnYnivjriNpuXNlviPZboIMTFfcYchgAwtfUgJmlZVbjmb-vYz9DqBG-cQ9c2FxeaW04nMDwL9hVMeQMNlIK0PjNzlbX_EEplMXeMxhPrabvpwTuEYYqQ8UcNj9DPj_ARx35CMkoezSkn44ToRoGDXtNspEH7Jcy_lo6k5cmL8M6Ex-ZcYzdqaS-2In315Km5rEmx8OHjwe7pMxAZXycnrat5i09-onwxSu5tH-FBRfkCeILbQCjnIEDR2fAOWQApY0_9_3W_zJszRUOSr7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ۱،۰۰۰،۰۰۰ تومان تخفیف، خودروتان را برای سفر آماده کنید
💯
🔸
تعویض انواع لاستیک دولتی
🔸
تعویض روغن موتور با قیمت مصوب
🔸
خرید و تعویض لنت و سایر لوازم خودرو
تمام این خدمات با تضمین کمترین قیمت و یک تومان تخفیف در اختیار شما قرار دارد.
کد تخفیف: RWELXT
مهلت استفاده: ۲۳ مرداد
حداقل خرید: ۳ میلیون تومان
همین حالا وارد سایت تپسی‌گاراژ شوید، نزدیک‌ترین مرکز خدماتی را انتخاب کنید و سفارش خود را نهایی کنید.
👇
https://tapsi.link/mrip0</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/679982" target="_blank">📅 15:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679981">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
چرا نباید ایران از تنگه دست بردارد؟
🔹
دست‌کشیدن از تنگه هرمز یعنی ازدست‌رفتن اهرم بازدارندگی ایران؛ چون قطر، عراق، کویت، امارات و عربستان ۷۸ تا ۱۰۰٪ صادرات نفتشان را از این مسیر انجام می‌دهند و مدیریت تنگه، کنترل اقتصاد و تورم کشورهای نفتی منطقه را در اختیار ایران می‌گذارد./ فرهیختگان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/679981" target="_blank">📅 15:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679980">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec49f80d3b.mp4?token=qzV-7a6_d8LgCnWfsU8nTFw7uqgP5ICjPQT5gzp5zDtfmM1QRjgEb54AeTD2NPYUJV06wjtuTVyKvABjgpOgZou8TTp1eLQboea8_rfgu5hCAQ-2Dp8zFJFfuYdaWOWQ67kg7N1UQFaJr2TCgXlox4ZsYePam9jy7CRQ28U_MWPFwyshwOTuOaPFs56uLbRXH79OY592P7Jqroqjqj8ZxQ55VMkJo4BYNtEKWnVJ9hL8V1u3rRhM9qE9dRRyLCpIXxxtuUczHX1bgu_jwkss43bYfYMe7Vi_gTOUP5cWieMLz0wrmrzTVGy_WqLDRWkvL6yKI9OyIFHeSbrzVvZZ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec49f80d3b.mp4?token=qzV-7a6_d8LgCnWfsU8nTFw7uqgP5ICjPQT5gzp5zDtfmM1QRjgEb54AeTD2NPYUJV06wjtuTVyKvABjgpOgZou8TTp1eLQboea8_rfgu5hCAQ-2Dp8zFJFfuYdaWOWQ67kg7N1UQFaJr2TCgXlox4ZsYePam9jy7CRQ28U_MWPFwyshwOTuOaPFs56uLbRXH79OY592P7Jqroqjqj8ZxQ55VMkJo4BYNtEKWnVJ9hL8V1u3rRhM9qE9dRRyLCpIXxxtuUczHX1bgu_jwkss43bYfYMe7Vi_gTOUP5cWieMLz0wrmrzTVGy_WqLDRWkvL6yKI9OyIFHeSbrzVvZZ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری پزشک قلابی عمل‌های زیبایی در شهریار تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/679980" target="_blank">📅 14:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679979">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688432cc6d.mp4?token=J0-jVCoYPPhpAOPg2Njpe3nnaMlj3n2FvSt9qdUB-PlbNsBK2sJzS8jaV028P_-Slp5XIQm6fw2CdPP1zafrqARUqrvwWWoYqyEKTfil1639pw_3WLS1hdAbHBrTUrzsi2h3PiKgFw6G3nGKEzPyxVSmslpWjkuGLK-6fdvxRePy-uUWmmDJQeyDUhlf-8UqsJuGivFNjQin8KPQQ4OAdCrEbIW6u5swmZK3Idc9WqQhmCHX0GFNwzS1PQGaJ3JpdU3RkBYuH1gcZTPAX14O2BwvHSBTirE4L-2ORHeOfEP6YuA84BdF8YmXiwq_Dm14DM09QTII2QxqSFuW3LagCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688432cc6d.mp4?token=J0-jVCoYPPhpAOPg2Njpe3nnaMlj3n2FvSt9qdUB-PlbNsBK2sJzS8jaV028P_-Slp5XIQm6fw2CdPP1zafrqARUqrvwWWoYqyEKTfil1639pw_3WLS1hdAbHBrTUrzsi2h3PiKgFw6G3nGKEzPyxVSmslpWjkuGLK-6fdvxRePy-uUWmmDJQeyDUhlf-8UqsJuGivFNjQin8KPQQ4OAdCrEbIW6u5swmZK3Idc9WqQhmCHX0GFNwzS1PQGaJ3JpdU3RkBYuH1gcZTPAX14O2BwvHSBTirE4L-2ORHeOfEP6YuA84BdF8YmXiwq_Dm14DM09QTII2QxqSFuW3LagCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید سپهبد موسوی: هرچی تنبیهی من خوردم، بخاطر خنده‌هام بود
🔹
۱۹ مرداد ماه، سالروز ولادت فرمانده شهید نیروهای مسلح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/679979" target="_blank">📅 14:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679978">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrJz9kaDJZ7on2Dle_OGbwV6HufVwVnExr-0j5kneIHxaNvNByQVYqb3G9nBtzw5N-dpIA7BLlpraxJyiefHokHRHbJdHQr5tZx6d3siBbYDaicA6tFhMk6G5uaotkKpno2HbGFBkUks3cldkBacVz5JU19h6ABP-o2md7RVptD8J6HLbps_R6tjgzCiAb6EygOWgpgfFJIwHd9QPNKQXvt6F4NjAuOs7oBuP1iY__HCjDbwMUiGAE6MmAZ9aaBmRGZY1vuNv5jIxjvHwXruwxl7WRH-feOqmOGiIwMofqLtpNSogoYNNKzmZ0NEqpITok6WSi2lfyehHXw4s8dOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات سایبری؛ عامل بیش از ۶ درصد ترافیک اینترنت کشور
🔹️
بیش از ۶ درصد ترافیک در سطح کشور بدلیل "دیداس" و حملات سایبری است که عدد بسیار بزرگی است.
🔹
حملهٔ دیداس نوعی حملهٔ سایبری است که در آن، مهاجم با ارسال حجم زیادی از درخواست‌ها به یک وب‌سایت یا سرور، باعث ازدسترس خارج شدن آن سرویس می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/679978" target="_blank">📅 14:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679975">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7607a3ad.mp4?token=g2_-BUEH5wvHpIaNWHI12HnGpunQ4d0d8YgvXc0xnZFORaZtF45IIgQLYGtfJlCkLfnKawz0M26lKGkW1NqpUHhL2ABSqSSgvXwgmfm6iK-ZXEOC93Ex-57Udwg39R6Zpuum5guYrB4-oq3d78bZ2Glk9GRO0L-OdHI1bUKVWiVESf-m8k1Hd7y19eWSOMjSPv0PzK7A6QaUG6sWvTzQAmP7X6bH8VMloq0NcHBn2BIRafvGe2joGDtHTNJpoSJPfmnkcYpLpf-IhWXTpywL5-wU6zcAavJeIzFLVR8LcdVUr4iYrBpv4b84uDTore3qGQCXzMYw8tiYhtigO_OR-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7607a3ad.mp4?token=g2_-BUEH5wvHpIaNWHI12HnGpunQ4d0d8YgvXc0xnZFORaZtF45IIgQLYGtfJlCkLfnKawz0M26lKGkW1NqpUHhL2ABSqSSgvXwgmfm6iK-ZXEOC93Ex-57Udwg39R6Zpuum5guYrB4-oq3d78bZ2Glk9GRO0L-OdHI1bUKVWiVESf-m8k1Hd7y19eWSOMjSPv0PzK7A6QaUG6sWvTzQAmP7X6bH8VMloq0NcHBn2BIRafvGe2joGDtHTNJpoSJPfmnkcYpLpf-IhWXTpywL5-wU6zcAavJeIzFLVR8LcdVUr4iYrBpv4b84uDTore3qGQCXzMYw8tiYhtigO_OR-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی کمتر دیده شده از سینه زنی رهبر انقلاب در مراسم تشییع فرزند مرحوم آیت‌الله استادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/679975" target="_blank">📅 14:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679974">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45066d47b4.mp4?token=HGF-NR9UCAu2fVnSWKEHvEr2ndmArRO3CoP7mZTG7hdky6dNFX4Vt1vi_9_jiAW1jyoFBwr2uz_GUn3GUz3uraGrSzNQ02k5xoRMB4CtY6C7OHlNz-C7bh8zD5ZQjLcT57Cxi-tJP86MwNMIP4YiCweVPZKv34LwwGmch9GkV0ZE80zd6WYWKpWMiSFqs1qKHkCCMX3zWMoAzkYPWyom4x8AvNmPfC9pFsfAhtii4uDRuyJ3GmSKw1VRI9SH2iZa5Pd8uJ-iIKJ8Y9VMzwa0O4A56qibi05es7NXlUmReMuIqCC5wDwmK_7hN3TcdYabnJIn5coBtEMIve9nVigifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45066d47b4.mp4?token=HGF-NR9UCAu2fVnSWKEHvEr2ndmArRO3CoP7mZTG7hdky6dNFX4Vt1vi_9_jiAW1jyoFBwr2uz_GUn3GUz3uraGrSzNQ02k5xoRMB4CtY6C7OHlNz-C7bh8zD5ZQjLcT57Cxi-tJP86MwNMIP4YiCweVPZKv34LwwGmch9GkV0ZE80zd6WYWKpWMiSFqs1qKHkCCMX3zWMoAzkYPWyom4x8AvNmPfC9pFsfAhtii4uDRuyJ3GmSKw1VRI9SH2iZa5Pd8uJ-iIKJ8Y9VMzwa0O4A56qibi05es7NXlUmReMuIqCC5wDwmK_7hN3TcdYabnJIn5coBtEMIve9nVigifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه رشد لاله مردابی
🔹
یکی از اشتباهات رایج، یکی دانستن لاله مردابی با نیلوفر آبی مصری است؛ با توجه به مرکز گل می‌توان تفاوت این دو گیاه را تشخیص داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/679974" target="_blank">📅 14:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679973">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa2d0a474.mp4?token=PnNWIRituQlHOGWforseksjVOCgOmrcFhXrc-zi1R1xkt-VGh9CJJBBGIb3BwTFRUJE1cCFGQ_za5lZprdBpM7hILIwuypXg4NjhNQgmqoMt0NYGJP3DX7gXGETGVt5Jfb6uJ_A0zkwhEyLWwViC8tPyc1vjMRp2p68ryPthnXvEbTiLowIpV1tB1_mrPlviswPLzL8fGKtVtzrPOhEX3fbcgsyQDXsUXRrDMoc-jsExbaH_JmWrW6UI0CC08WBF9A9GWZPRQGXVJZ1O8nwHmMoBAE7rAvJzDQH9C5wEKkdEAflTYS3w4DFhq4C9RxG3V5PBA7gxrGEfdvR_acuPCJxk2zh8ypU0EJ7O9Q7IKuCx6nU3GJ63X2Ihn_t_lRQk8FJOYJ3tYVGMpqUs1WvO6uTUF4HEetd8OkU6RY3GM5N54ZGhKI756fPa2N_E8UAAkA9lc3PWzZ94fv3Niuqki7SXHGm1cTIiGTzlQx_XNFfN92ZesrM_q1bqLQncqqaOAS_eNubF2B4nxlR8XhTBV0dI-rP6sPoEefHpUTZkdcYRLPaOT777NcAfKREbHH2qASGoKvjXs1pw_4DWUbwZM0mEKS6sjRLrVtvZdUKRoLnuUKEFL5rhjmexU1_cjyuoOpUb74apEAAfeNkKb87aLBj2DSefPMWdtew7ItuGnIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa2d0a474.mp4?token=PnNWIRituQlHOGWforseksjVOCgOmrcFhXrc-zi1R1xkt-VGh9CJJBBGIb3BwTFRUJE1cCFGQ_za5lZprdBpM7hILIwuypXg4NjhNQgmqoMt0NYGJP3DX7gXGETGVt5Jfb6uJ_A0zkwhEyLWwViC8tPyc1vjMRp2p68ryPthnXvEbTiLowIpV1tB1_mrPlviswPLzL8fGKtVtzrPOhEX3fbcgsyQDXsUXRrDMoc-jsExbaH_JmWrW6UI0CC08WBF9A9GWZPRQGXVJZ1O8nwHmMoBAE7rAvJzDQH9C5wEKkdEAflTYS3w4DFhq4C9RxG3V5PBA7gxrGEfdvR_acuPCJxk2zh8ypU0EJ7O9Q7IKuCx6nU3GJ63X2Ihn_t_lRQk8FJOYJ3tYVGMpqUs1WvO6uTUF4HEetd8OkU6RY3GM5N54ZGhKI756fPa2N_E8UAAkA9lc3PWzZ94fv3Niuqki7SXHGm1cTIiGTzlQx_XNFfN92ZesrM_q1bqLQncqqaOAS_eNubF2B4nxlR8XhTBV0dI-rP6sPoEefHpUTZkdcYRLPaOT777NcAfKREbHH2qASGoKvjXs1pw_4DWUbwZM0mEKS6sjRLrVtvZdUKRoLnuUKEFL5rhjmexU1_cjyuoOpUb74apEAAfeNkKb87aLBj2DSefPMWdtew7ItuGnIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین‌پاک، کارشناس جبهه مقاومت: رژیم صهیونیستی ۷۰ درصد غزه را اشغال کرده است/ اگر دوباره خطای حمله به ایران را تکرار کند، با ضربات متفاوت و تسلیحات پیشرفته‌تر ایران روبه‌رو خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/679973" target="_blank">📅 14:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679972">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
فیلتر پلتفرم‌ها بدون تایید رییس جمهور ممنوع شد
؛
دولت اختیار محدودسازی کسب‌وکارهای دیجیتال را مشروط به تأیید رئیس‌جمهور کرد
🔹
بر اساس این مصوبه، دستگاه‌های اجرایی دیگر نمی‌توانند به‌صورت مستقل درباره محدودکردن فعالیت پلتفرم‌ها تصمیم بگیرند و هرگونه اقدام در این زمینه باید ابتدا در «ستاد راهبری و ساماندهی فضای مجازی» بررسی و در نهایت به تأیید رئیس‌جمهور برسد.
🔹
اهمیت این مصوبه فقط به تعیین یک مسیر اداری جدید محدود نمی‌شود؛ دولت برای تصمیم‌هایی که خارج از این چارچوب اتخاذ شوند نیز اعتبار قانونی قائل نشده است. بر اساس ابلاغیه هیئت دولت، هر تصمیم یا اقدامی که بدون طی این فرایند برای انسداد، تعلیق، تحدید یا ممنوعیت فعالیت سکوها و کسب‌وکارهای فضای مجازی انجام شود، «فاقد اعتبار» خواهد بود.
🔹
فرد ذی‌ربط در صورت واردشدن خسارت، مطابق قوانین و مقررات مسئول جبران آن خواهد بود./ شرق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/679972" target="_blank">📅 14:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679971">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f43b18398.mp4?token=qFFGxLOl4ctt-HNgVLJv_FgB4tw8Ph4a1i_JMeYWhtwoEOuVcmcGzqDv86fOvE5V4JdeEcSSLz8mDmiou4_dB0Nk38cldwhtTmAP5QGADW8TBeDH4mjtkNuRhtk4XjDZPf84h2V0O5crYk214NVDW-G66I6zfef71SqMoZfD2M7PaQaL6srTwklReWnbfnseQ1tpN98MYR7tGUYKfd6fXXVdVFQ2YP0xKRvqh1FaG9cXFdtx4KhAXdE8NMgJhxfdwtB8b0-RjIaJz6gPrk1-ocadHBPh2ngNi-PRqhw2YpaedmDEVArdmY6x0Ccmp55qfUo8T_n_B0s3uOR1wgE5HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f43b18398.mp4?token=qFFGxLOl4ctt-HNgVLJv_FgB4tw8Ph4a1i_JMeYWhtwoEOuVcmcGzqDv86fOvE5V4JdeEcSSLz8mDmiou4_dB0Nk38cldwhtTmAP5QGADW8TBeDH4mjtkNuRhtk4XjDZPf84h2V0O5crYk214NVDW-G66I6zfef71SqMoZfD2M7PaQaL6srTwklReWnbfnseQ1tpN98MYR7tGUYKfd6fXXVdVFQ2YP0xKRvqh1FaG9cXFdtx4KhAXdE8NMgJhxfdwtB8b0-RjIaJz6gPrk1-ocadHBPh2ngNi-PRqhw2YpaedmDEVArdmY6x0Ccmp55qfUo8T_n_B0s3uOR1wgE5HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: هیچ قدرتی نمی‌تواند مردم ما را وادار به تسلیم کند
🔹
مردم با حضور در میدان، تهدیدها را به فرصت تبدیل کردند و همۀ معادلات دشمن را با وحدت و همدلی شکست دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/679971" target="_blank">📅 14:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679970">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وهفتم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سید امید متقی که بخاطر خواب آلودگی در حین رانندگی دچار سانحه تصادف و ضربه مغزی شده و یک‌ ماه در کما به سر می‌برد و با رؤیت جد بزرگوارشان امام موسی‌بن‌جعفر، شکستگی‌های داخلی در بدن که بیمارستان متوجه آن نشده بود، شفا می‌یابد و به او سفارش رعایت حق‌الناس و طلب حلالیت از انسان.ها در دنیا می‌شود، را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید امید متقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/679970" target="_blank">📅 14:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679969">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3Vy33Wz8HUQLG08nKaGUQ9O960dqmxQNyAifja3yMQrnOiu0EHFTc_2Djs5Dw2-FdcsJXPvtuIPZg06MYzyk7ZcoS-TnHNVcMVzuA0FsNlxL05tV6VjfAJxS95ata-cI5nechwxzhwU2fD5Ipa5DtMhxzyytquSSqdzTCfNRNTVx1dkQhKSB77rrgPUcjEMFZv1wBqCud0WKMSFdJf40FyoTmkJuX7-ZHD4yrwdacG_zrUF5eMVKbmaeOu3KfmdeX2B_WzeiuNZTONA6cdqXTNkQMc_g9-l7d0aJg9yYiFdXFZtJB6XDT0Uq6iVaYa6GEQUPYDkrBQHLdGX5HnMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر کتونی مناسب چه مدل شلواریه؟
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/679969" target="_blank">📅 14:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679968">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
افزایش شهدای حشدالشعبی به ۲۰ نفر
🔹
حشد الشعبی در بیانیه‌ای اعلام کرد که در پی حملات آمریکا و عربستان تاکنون ۲۰ نفر شهید و ۳۲ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/679968" target="_blank">📅 14:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679967">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e7d6feab.mp4?token=ko4kCBwsVYLiNSS6HL4EiGJi10ZArdaLAagwz0sNvqb5kDy3_A07DvKbRa5kv8evwOpc-osBOGSJx0FWWu332XjaO0U4AgqIEX1XBdIcprJ_BYOGn5q0U9x9wN26_UDdQPWZ2i_vm7w2Q8f-bv0UoYwFAg4B1HswVV6cJu09xBEt2ZRQMKlyw5-S3-WkaaMkg6egjh_WTfQMYNVDOj2UEiLDfaHrrKScvIo-p1gf_yyCfRH0kWtYdACC0v77CEDSWWcGTVn8Wel6hiX-ZKxVn2c3AJkq4By4sDMDig9YmCxEc0zgNajmMMSMslZwiIiQwxXXk4WOuJ9WNqGQrDsc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e7d6feab.mp4?token=ko4kCBwsVYLiNSS6HL4EiGJi10ZArdaLAagwz0sNvqb5kDy3_A07DvKbRa5kv8evwOpc-osBOGSJx0FWWu332XjaO0U4AgqIEX1XBdIcprJ_BYOGn5q0U9x9wN26_UDdQPWZ2i_vm7w2Q8f-bv0UoYwFAg4B1HswVV6cJu09xBEt2ZRQMKlyw5-S3-WkaaMkg6egjh_WTfQMYNVDOj2UEiLDfaHrrKScvIo-p1gf_yyCfRH0kWtYdACC0v77CEDSWWcGTVn8Wel6hiX-ZKxVn2c3AJkq4By4sDMDig9YmCxEc0zgNajmMMSMslZwiIiQwxXXk4WOuJ9WNqGQrDsc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باید برخاست؛ برای ایران، با هم و کنار هم
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/679967" target="_blank">📅 14:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679966">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d4c320e7.mp4?token=mCOY_lMdF9HfBE58zscZGtXDQ4hoZ7u-UMsDgJkSC7jibZAk7u7dsXJtQAv-JVWdPn9QpsIOcIGL0lkRHbwM4lUbo_xw8YmNfdE75fEyl03VH_2IVLgBXkkKUtCHvyVo1DbtZ3aFDFBBqouwp3S_AV0vsmRBGRhkD1qqXJxk7oMJ496omNP0GHEOR9zptaF-SBcme2K4ZE8sBodFdA7XIqsr5KSNv2PYTHlXuRx7kALj91PL--krXjSxrYxR5amsxi3ir0rHik7cd9cQQiSDmGwqUhjDSse0aJ1OHPwrLr3XkMhlKMFgPZ7eTMotozwKpY7CSZqf0ea6LrqVI2yjf10YB9hCYGIbxuSH7O-vVMOdt370Y00f_1dA-FL_9DAZ9Kk0v6z1rzY0cbSx842fp1JPGdCO1QOOVp1lpyfwhsBK59hWMRGpQnNC62DJaajUHhmdyH3-EFS7c_Q5cKqqyyJRFfj6nB5-tQJB90hVZHGGAHUiQHtEvDgg6fqgypztdNXFoXFMtVbLCBVwiPzmNHC4JtUGiSQI9fuQy-1xweTC6vOxvRhEJwY3AS_CxUE2TZ-0MlpG8mYbU-pchzjMmDXiD2F052RIHbU0lB0qe_4zoalJCzoKlkunoR_7c9pHFdNvf6gFW5d-PlRwciogWWzIexr1xHsAG-q8SQ0ie5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d4c320e7.mp4?token=mCOY_lMdF9HfBE58zscZGtXDQ4hoZ7u-UMsDgJkSC7jibZAk7u7dsXJtQAv-JVWdPn9QpsIOcIGL0lkRHbwM4lUbo_xw8YmNfdE75fEyl03VH_2IVLgBXkkKUtCHvyVo1DbtZ3aFDFBBqouwp3S_AV0vsmRBGRhkD1qqXJxk7oMJ496omNP0GHEOR9zptaF-SBcme2K4ZE8sBodFdA7XIqsr5KSNv2PYTHlXuRx7kALj91PL--krXjSxrYxR5amsxi3ir0rHik7cd9cQQiSDmGwqUhjDSse0aJ1OHPwrLr3XkMhlKMFgPZ7eTMotozwKpY7CSZqf0ea6LrqVI2yjf10YB9hCYGIbxuSH7O-vVMOdt370Y00f_1dA-FL_9DAZ9Kk0v6z1rzY0cbSx842fp1JPGdCO1QOOVp1lpyfwhsBK59hWMRGpQnNC62DJaajUHhmdyH3-EFS7c_Q5cKqqyyJRFfj6nB5-tQJB90hVZHGGAHUiQHtEvDgg6fqgypztdNXFoXFMtVbLCBVwiPzmNHC4JtUGiSQI9fuQy-1xweTC6vOxvRhEJwY3AS_CxUE2TZ-0MlpG8mYbU-pchzjMmDXiD2F052RIHbU0lB0qe_4zoalJCzoKlkunoR_7c9pHFdNvf6gFW5d-PlRwciogWWzIexr1xHsAG-q8SQ0ie5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: هیچ دولتی در حوزه مسکن خوب عمل نکرده است
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
متاسفانه در کشور برای حوزه عمرانی جایی برای بخش خصوصی پیش بینی نکردیم.
منابعی که در بودجه سالانه برای حوزه عمرانی پیش بینی می کنیم یک پنجاهم چیزی است که نیاز داریم.
🔹
باید قبول کنیم خیلی از پروژه های عمرانی را در کشور کلنگ زدیم؛ حتی درصدی پیشرفت فیزیکی دارد، اما نیاز کشور نیست.
🔹
در حوزه عمرانی کشور را گران اداره می کنیم.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/679966" target="_blank">📅 13:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679963">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
کشف جسد «دنیل سیاد» از مرتبطان پرونده اپستین در پاریس
🔹
جسد دنیل سیاد، از چهره‌های کلیدی در پرونده جفری اپستین که متهم به تأمین دختران جوان برای او بود و قرار بود بازجویی شود، در پاریس پیدا شد.
🔹
وی دومین فرد مرتبط با این پرونده است که در فرانسه جان باخته…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/679963" target="_blank">📅 13:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679958">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdXl3g_1M0wd-2ImhkTUk14b3sf-ZkeyEODaoJELJkEP7RWpFeQY5A9_nWCGxTlAaH_0nYODDLaUTepx46DPbBuqDicwxOTAb9AJjL4n6qw7w5Nttoih9WBL_ahtuH9tDwaDwU2WaVGs5nD5YS54wRHk3j-gbJ9bpW5T3yM-3MeNCyRE8G8onqWmTPgxcTzvEiIc5f3NX-zvLNHb54K7ZC1Xiru2XcLbUztdDg_mKRIFdrsG3J_McyVlXLJEwxKUbWZFiBEDWyvTCs3q5hFA-U3tyHzqcEO4tmnUtXEeZ4odyZjEsZqLRPXvU3krAegkdAAAmSkVa5banOtlUbkkmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYEaIj56K5X8Axmi7TB5ivsNFzVrLTyu37YwbwK_vX5qEILMoQ2yluxeagizZjqZDpRKA4YEX7ro7VEEzbtQB8YlSHbv63xXg0yuQUgcKGARubKmtjIkso47-A5AiM3DeJm_S0DolIdwrnpWisF_ajCoIE5BmehXUE06pC-bx0STk7jf2QDh1UHdOLMfavSh98hx42khQCSSdSOd-WlFUtNYFPLjjHqx_Gl1oJZtrObnJWN5NCEuGD-ySElJaBfa-Q7ouz8jKob8-Pbe7mjcUr4olVwLCpC_pOB_mki-diWwGxCzbeMZyJxhY-OdzG2vo3c5m2qTD0F75RoKVp0JXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQGvrwost6tTf2ahK0_xtKD4ik2k71TL3dpmuw5tGCA58NP485tLzMRYwWhpcc1yHN1SCc7CkNNjgRFNXPcVzvXkT_FUYnPea09NH1n5269Bs8NtIEhA63MCXXPZ52_COaE01oTyZhFl6HMNs3r7_unw_34pNPm8Mem6NqTbFb8Ku4EZsSl7492kUVjwWKdS3DgfGmNFM_m6AmqAcpuLkedz5pspghNHY6n2mNIngNtlZ-xEZ652_4uiiyc7KJSfvv2Eg3Jzsc2MAZtBWMU8tQKe4ncudBsyDsYxyK_fB4mT3grc7IYysuYUMFWXAugeQd_-RjUO6E32W23B1e4TIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شمشیر کوتاه هخامنشی
🗡
🔹
اکینکه‌ی زرین یا شمشیر کوتاه هخامنشی، متعلق به سده‌های پنجم تا چهارم پیش از میلاد است که در اکباتان (همدان امروزی) کشف شده و اکنون در موزه ملی ایران نگهداری می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/679958" target="_blank">📅 13:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679956">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdd3a47ed.mp4?token=LirSty3wpxhEcTI8aD5wmn-jqDusLStM_wFxAJJotIfnUMSByQWdttuI3um5yPwbCprcYRNpyGkmFzahTOMqLaLhx5J-CwgwJn1UO2txV6G802f2fQRQTBpd_frw2C0f8Z11aGSsAo-KJJnZrqeIBeaYOQdzPxhbeMkMyCEnuNM7RCG_xeLQ5pRiL8fUibpE7CtlpGNXjhLLDHEWWgGaQyvfPl5-ESWapxNn6-4ewi2ldII0kWgdprirW_B0i3zYlCXhchgjSL_ZwhyNMmJDV4EDn48lW_E0EbF-8_BFesshmGkkKZs79v8G0Y7obN_Uk_WlW5Xn3dLbjFKwAv-Q0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdd3a47ed.mp4?token=LirSty3wpxhEcTI8aD5wmn-jqDusLStM_wFxAJJotIfnUMSByQWdttuI3um5yPwbCprcYRNpyGkmFzahTOMqLaLhx5J-CwgwJn1UO2txV6G802f2fQRQTBpd_frw2C0f8Z11aGSsAo-KJJnZrqeIBeaYOQdzPxhbeMkMyCEnuNM7RCG_xeLQ5pRiL8fUibpE7CtlpGNXjhLLDHEWWgGaQyvfPl5-ESWapxNn6-4ewi2ldII0kWgdprirW_B0i3zYlCXhchgjSL_ZwhyNMmJDV4EDn48lW_E0EbF-8_BFesshmGkkKZs79v8G0Y7obN_Uk_WlW5Xn3dLbjFKwAv-Q0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبلیغ متفاوت نتفلیکس برای فیلم «آخرین خانه»
🔹
نتفلیکس برای تبلیغ فیلم «آخرین خانه»، مردی را سه روز داخل اتاقی ساخته‌شده درون یک بیلبورد در لس‌آنجلس مستقر کرده است؛ اتاق به کتابخانه، کارت بازی، دوربین دوچشمی و تخته سفید برای ارتباط با رهگذران مجهز شده و با فضای داستان فیلم هماهنگ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/679956" target="_blank">📅 13:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679955">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWwVh9A33FG-OcqAAdjgXmzNPQRSL2NwhhiY0BW9GIzuCmSLDRQQr9cegwB4RVn7PU8t_jFqz4793Ec0Xt-N9QRtvEqFYy6OZQ7uGQ1fUSBZToqucSpgT0OrkF_7uIXo_UESR_vWeGbTMMaRqTa2TEcuQOlhKfSHM5YDc5D14xVmOYIeMaKY7mduI3VpZ7EeiOPmv6RTusOkTebsRB4xjsmw4ui7iO6-pqzbIvE2u37VJq3zGbWAmRIAEY0v1IA2-_gWXTH7XDuqWBZd4U9NjO4B2AxfsJnjcj1XFE15gj1WYC8dOU6RsSlcrg3xOqQ3UK3UgLZ1yfGikXXR3skaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۹ مرداد ۱۴۰۵؛ ساعت ۱۳:۰۰
🔹
دلار در معاملات امروز با افت هزار تومانی نسبت به نرخ پایانی دیروز، به کانال ۱۸۵ هزار تومان عقب‌نشینی کرد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/679955" target="_blank">📅 13:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679954">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efnoHij_6gXvG4AhievbY0utBDmNqWWchqcIyCuhRdCxjKXs1yaJH-cEqC5JrA5-5pcMC4lzMhwWE8iq09XLnDh1oOywCo7ck8i2iCddc3TfkGHGGHWDQsgJ75_-liN0Hj3MsjvH4-VZFg1MATTQh6MRfHDRq17ZP5A7_V6DW4AaGicxLWFV0UIdE1SBlaHq28eI21zl4E0_uhdMBifqREfBXx9dGEJHq3HnAXtRYQBh8t9IHG5aPhMoIZj0pGei5rtfXGSLXjNB6Z3sRvqL1XkjXZWBcm45TJQ9rSiMB8KZ9lRQNyVdAv5Y3So6AGuUmfIsdJtvkBzTwbsuwsDtEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصمیم‌های بزرگ نوری برای آینده سهامداران؛ از افزایش سرمایه و تقسیم سود تا تثبیت سرمایه‌گذاری‌های راهبردی شرکت
🔹
تصویب افزایش سرمایه به ۹۶ هزار میلیارد ریال و تقسیم ۳۸۵۰ ریال سود به ازای هر سهم
🔹
مجامع عمومی فوق‌العاده و مجمع عمومی عادی به‌طور فوق‌العاده شرکت پتروشیمی نوری، امروز یکشنبه ۱۸ مردادماه با حضور سهامداران در سالن همایش ضرغام تهران برگزار شد و تصمیم‌های مهمی درباره آینده مالی، سرمایه‌گذاری و توسعه‌ای شرکت اتخاذ شد.
در این مجامع، افزایش سرمایه پتروشیمی نوری از ۶۰ هزار میلیارد ریال به ۹۶ هزار میلیارد ریال به تصویب رسید و در مجمع عمومی عادی به‌طور فوق‌العاده نیز با تصویب سهامداران، ۳۸۵۰ ریال سود به ازای هر سهم تقسیم شد.
بررسی و تصویب صورت‌های مالی سال ۱۴۰۴، گزارش عملکرد سالانه، اصلاح اساسنامه و انتخاب حسابرسان از دیگر محورهای این مجامع بود.
*سودآوری در کنار سرمایه‌گذاری؛ تصویری از منابع و تعهدات نوری*
در جریان ارائه گزارش عملکرد مجمع، دکتر غلامرضا جمشیدی، مدیرعامل موفق پتروشیمی نوری، با تشریح وضعیت مالی شرکت تأکید کرد: ارزیابی عملکرد نوری تنها با تمرکز بر سودآوری و توجه به جنبه های تک بعدی امکان‌پذیر نیست، بلکه باید همزمان میزان به مقولات متعددی همچون سرمایه‌گذاری‌های کارشناسی شده سودآور ، تعریف پروژه های نوین، مدیریت هدفمند هزینه ها،  تخفیفات خوراک، بدهی‌ها و نیازهای نقدینگی شرکت مورد توجه قرار گیرد.
*«هنگام» از سرمایه‌گذاری تا تولید؛ حفظ دارایی‌های ارزشمند برای سهامداران*
یکی از مهم‌ترین محورهای گزارش مدیرعامل بزرگترین شرکت آروماتیکی ایران، به ثمر رسیدن سرمایه‌گذاری در پتروشیمی هنگام بود؛ پروژه‌ای که در شرایط فشار نقدینگی و وجود بدهی خوراک، با تأمین منابع مورد نیاز به مرحله تولید رسید.
دکتر جمشیدی با اشاره به اهمیت این سرمایه‌گذاری اعلام کرد: آثار سودآوری پتروشیمی هنگام می‌تواند از سال ۱۴۰۵ در پرتفوی نوری نمایان شود و در بودجه سال جاری نیز حدود ۶.۸ همت سود برای این شرکت پیش‌بینی شده است.
مدیرعامل نوری همچنین تأکید کرد مدیریت برای تأمین نقدینگی می‌توانست نسبت به واگذاری بخشی از سهام هنگام یا سایر دارایی‌های شرکت اقدام کند، اما با استفاده از ابزارهای تأمین مالی، اعتبار و ال‌سی، از فروش این دارایی‌ها جلوگیری شد تا سرمایه‌گذاری‌های سودآور و بلندمدت برای سهامداران حفظ شود.
*از یورو ۶ تا عبور از بحران؛ بازگشت مقتدرانه نوری به مدار تولید*
پروژه تولید محصول با استاندارد یورو ۶  به عنوان محصولی ارزشمند و راهبردی نیز از دیگر طرح‌های مهم مورد اشاره مدیرعامل نوری در مجمع بود.
این پروژه مهم که به مراحل پایانی رسیده، اکنون کاتالیست آن بارگذاری شده و آماده افتتاح رسمی است.
دکتر جمشیدی خاطرنشان کرد : این پروژه با ظرفیت فعلی حدود ۱۳۰ هزار تن، از منظر توسعه بازارهای صادراتی و ایجاد فرصت‌های جدید در حوزه بانکرینگ دارای اهمیت ویژه‌ای است که ظرفیت افزایش تولید نیز برای آن وجود دارد.
مدیرعامل نوری در بخش دیگری از گزارش خود به آسیب‌های عملیاتی ناشی از جنگ اشاره کرد و گفت کارکنان پتروشیمی نوری طی ۶۷ روز تلاش شبانه‌روزی، بازسازی ۱۸ خط و حدود ۵ کیلومتر خطوط انتقال را انجام دادند و در مجموع حدود ۹۶ هزار نفرساعت برای بازگرداندن واحدهای آسیب‌دیده به مدار تولید صرف شد؛ تلاشی که در نهایت به بازگشت شرکت به چرخه تولید انجامید.
در کنار این اقدامات، نوری در سال ۱۴۰۴ موفق به ثبت رشد حدود ۵۰ درصدی فروش داخلی و ۵۱ درصدی صادرات شده است  که توانسته جایگاه این شرکت را در بازارهای داخلی و جهانی به طور ویژه تقویت کرده و ارتقا دهد.
*خلق ارزش ؛ از رشد عملکرد تا رضایت بینظیر سهامداران*
گفتنی است پس از ارائه گزارش عملکرد شرکت توسط دکتر غلامرضا جمشیدی، مدیرعامل پتروشیمی نوری، این گزارش با استقبال بینظیر و تشویق پرشور سهامداران حاضر در مجمع مواجه شد؛ واکنشی که با توجه به عملکرد درخشان نوری، رضایت صد درصدی سهامداران و تشویق های مکرر آنها در حین ارائه عملکرد شرکت، نشان دهنده این بود که مجموعه پتروشیمی نوری در سال ۱۴۰۴ توانسته است رضایت سهامداران خود را به بهترین شکل ممکن فراهم کند که می توان آن را دستاوردی بینظیر در صنعت پتروشیمی کشور دانست .
این استقبال به‌ویژه در زمان تشریح رکورد تولید ۱۱۲ درصدی، عملکرد فروش و صادرات، حفظ دارایی‌های ارزشمند و اقدامات انجام‌شده برای عبور از چالش‌های نقدینگی و تأمین خوراک، جلوه بیشتری یافت.
مجموعه تصمیم‌های اتخاذشده در این مجامع، از افزایش سرمایه و تقسیم سود تا حفظ و به ثمر رساندن سرمایه‌گذاری‌های راهبردی، توسعه پروژه‌های جدید، تصویری روشن از رویکرد پتروشیمی نوری برای تقویت بنیان‌های مالی، حفظ ارزش دارایی‌ها، توسعه پایدار و خلق ارزش بلندمدت برای سهامداران ارائه کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/679954" target="_blank">📅 13:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679943">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ad7XoWYT3WvXEEA0fO1Kg8S_Fa9GuLrAuq56leOcBjXuTW75g8PZubX20IHfWwsa1e3ev3ZgAn7Um0z-HSlgwP119BJIOvImIoopydMv25ag6toGAhFO4HMfS8HpOnqkAzzoA13ZXmy6RoGpellyxhRcbVBFp9K-C5f7k835SbnlGirVT5Naj4qU_tHoZCQ1BGHug32jQuFJBgFpvlbBHSyCZvJrACZ4gny4Ghi_YnMIhbvnWpAL_5p8k9edm6sECjsVbNrqTi3VHLHTavjJtiDLttwv_wP83lgIxD6E4hJbc7ic7UMzK9OTIBrFwIudhTdSoTJZ0qbtXKqSr8R7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCjofCTTj4PF8szqiFkdUy5VUqOi7BrUP2xrdWBbrm1XNEcjhU1OtevdzsiYwQz7zho0NnVrrKKoOcSJ8yTGeXEyEcy9z_sEvUwmaKC0CQDPqiSNlyncgKzzODjJyMSMkXzI8_q7dWF4kbOcgfneV3ngmT2SNKEqh8nVXk3HC1uaM721KNQB8WockWe-frpDX08uuYHtT3AdeZ6w3_PGVpTiDY8id042QGU4qHTXwG4B317ESu3AikUM0ezfEn1dcYQOXZbm8EdqG-kxl3G2w7lOO5eQ126WNJbHqoO_C4Nk0_0_a7cDcuLgfehVLcE3q74da-1Mf1HeLLhuKEXwsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMqaJV4gTNq-ywEDOMhZl-Iu3yDF3ojciEml9etrhnI95BW_ea40RXKIAgnFXm3Zx9CBglLzMg0_FXfMWRWbqtb_LZWeNeGwi5PKT9JlWrox7nGiatPo5wMFhBjyax7f_8ikCGxcxBQR6TuD9R3F853QgYztP96q7G9Kap22mkwZAEGyzBKRn-zhzxWwpx-PJb6ggll90zACOPluCFB5IdbEsnzw6YnD9RJtctbqHYSCnq7DYBMi0ENxdvYpjUnJYbOYWehUFcSmV2YSNbh0CObxsSlEWtsPGSWsx-TZZY0IXG-XyWh_0dsUni3iPK8MbE4PHGlzXHKoPmVvcS3C8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wu2CJceHM3fs_5IAGgbXkjqCe9jfegsrRDljmryUIM-bTYdBptTr9b7Wuo_BiGDWYSyzmMiDq3ij5jCxnmEfNAmxf_6Oba9RGbx7usevpmaPckcumV2HMl2KdGl8sMHm9YFQoyw3UqyocN12eRl4M5zFPIK4vm0KfvGZmUQ4BoFV-qpHY9kdalifmCSqDPiMWkf4lDPM1v4DcTLUqPYvdhuanRPtMQ3F4JQ_qG6OB5TBkHxjN18Zww_icPjEGdbaPQ-HVa26x4LZuP4VvA5BR_zhwTqRWr1dqBcakqhZHVFaZ1_Tty_ELdPQJCfR46SPfMkv9u6vdy2wBvFsFmGSNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qi7wNIIdjVgFELQDVYoBUfo7OTbqwrrUgc9vXFwGqn6RxzZoHhpT-0qoMRJlQ16tfasWFPm21AfdoQS4MPpFBuX-7XWTVQsFfCFt3qpFa-M8keCsNiwoBMzFZE-AlLGCeV59xmFQ-RvPOXKgR1uVZ1Y64z0kGJGvUX_ATkKipw6xVK4EFtUZT2H83oDkMgepNBizE4J7tMoilFnLZ32J8LMN1ooxtjScWsqYcaUb43K33kbHAuHJEjNfo-eJOU1iTBtxmscJnRUr3SxmZi9mC83kAlUCADdPbNhVDWWj0_Vv34uUIfyc239y60mRd0EG-IpYBhFq_7tbz2IxqcCuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZNloHJ5WtFUrUZR38cybRTgNpytyVgAdyTubQv3_5As22IOUGt4zTw5sEw-r_Gz6TOuEGz3k5X_s0rnUMr0hhsyizJKl261drbPyq2wP9r9G8Efg8j_Beq3KFYTJKPfyMo2MHUPNb628N5po1tOWhWFGmyLrskE4OWe-9qINjCb2aRfR2FcQPSvOpfq_4bc8yXPuLy8SKJlmScjKqxv_dd_TdYh2VZW0cuvJNkP6hKfEExtsnaO-bCDVcQ_FY6pXv2ABjocWnpJ0RP0LBNucj_uVm2M1LtQ2ouA7LciEmum0FO2S5dds9WdVXHd01wuaCi2Dq8yBiXZ3jLGk-aJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlQoEZDenYKmshT-QQ-DJVyGdEAu-mWWTBSgPSOBV_2ZmS6Xq14vsDfI27utCEWmcysEa7dKpB0u3o3Do1xKKC2l8upBZgZN34pv7dMmgbghzgFYr7x5JKUbVT6IFCUDr1wc_Nw-RunOJbt5XEFxt2jGZnqnEJz8nNVBApesNyDoC6SWae1ui-6OqS2ui3KumzHX9LbSRgEewyRL8ykS0nZFOgisTZpqOnzB0Zo1cbSE_NdHktZZhCp3vrc3XDPvdjUOo7b5IDe2yJiEkotulQpaBzVwJklPSGa8E70Aw9Gl5yzPjU4FGfZ1ZOCDAkN6wH9vx7SqVICJUL6xhPEUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faxtueQRpBaVsIKeDC2nPp0yutN7CLFjAgXyihI0_wnrHO9P9qgn8kvc1hM9iZ6wRqRyfvk5R6QyFcTNExSIj_4t5kQ5m10VkGyZqXqKUkpqlSRjOXV6_CLw8TdMY8SlQbDceuHDc4v4gO-bA1Cmn7ECwTaOBdKTO_fUCz-wN0s7hGo49Zrkl2dlQfwmh87gA7gyUIIh7Rpdl60W5HjRB-BLrRAr8YsM674A7LQhiOOyiCD963s5UgKd9Mj2VgW_hGhy3-Ig1_UrvPiRvccXgdtnsqi-TgDm04R7HXBHpLwmKucxHr4btWZ3TTdl5HW0iybYHS6u8anpNo2ZSjQopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsz2YUc0qpnN5CPBJ2h_Q7KPY4t3YQkqdonO9uEEKDVDnSL4C1Wpw7D5zN10Wz5G9nPUjraclUXAx8aHfSu-pUdUWQeV8QCEL7HVd3MELVwsSojA9uwEcbEzMD7vbYPius0mPW2NySGuSrOmQAe4e96PQXPcedfalvz9s9YXnYwc-SmtA4I_8FhF55qQnkzzqIF4tlC3tfET6B-JabODBBCu7R7KpUW87Ca4vCAsixlgwnvI8aH0Q44MYdCQZ3DolkXx5qgAsrBM2MEEGHhvEmZo6gx7W3XoTJwv9pbZah4qn3fws0a_Jb1jVxpTUlGQDZcWWpYgK4Gd2Q1SFsFpHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حال و هوای موکب هیئت قرار در مسیر عاشقی
🔹
موکب هیئت قرار در محل تپه سلام مسیر ورودی به مشهد مقدس درحال خدمات به زائران پیاده امام مهربانی است، چندین هزار زائر پیاده از روزهای گذشته به سمت مشهد در حال حرکت هستند
🔹
هیئت قرار با همت کارکنان هلدینگ تبلیغاتی و رسانه‌ای خبرفوری راه‌اندازی شده است
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/679943" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679942">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXwjBIlfysuwK0JWYup7OiaFazlaY_AtvQCS2zstFHtAMPxMwJVLRKHnYmjaqGwTlPCbYsvuMg9eWkaVQ__aXOm1ftrTXv0daAShSEakFoIBLWX5ZavKxlEbNsPi2BRg6YjM5dfP5jlcGDKJb00elgckVjRqHRX3mPPkGiozKpVG2vAsAd0i3cwiV6f4mQ92N2kX9F9xDVMSqys648D9nzKi0hK6Qp_rOSisI8tKubVzgk92tdkVIboD_FMERQw97j-eeR2WR8_O-iw-SGi_KvasIwhAYgzwHSr9kvN-rnozbVi47h6IS08bgF_jZJ-t_gAwhiwg69Pmo2TvedOL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس جمهور: با حکم ریاست جمهوری اسلامی ایران دکتر مسعود پزشکیان، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/679942" target="_blank">📅 12:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3ROz5xpb5mf4mhojeuzFZ9Fgjy4gDBLzSrdY0ida8pSt9Sg3Ly6jzLjZOGnhVtRKIgYudATjuzNtkD84NzE86qTFvNJ86J-a6ByCtnv200Va_N2W40ocIpfgi7EOJwBNL2GaRAMeTuYB7361cD4mk0vL5cqde66Rphd9R1GZSzTgyLuWiCEqtuxqiImHBzR36zgAOoNT6JFVf7rPB7AgP2Qpmv2T4kn81Oskvl5wgkLgSs4Zj2TmTSDzKeTJYxmf5ViCPproSed9cq6Kncuq58Hadkg_RKCzQ1mjSpweG4oU4_VEE5K2KqVqD5bdeKat97l_-pek_i5HSd2rSUe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679938" target="_blank">📅 12:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ba817d81.mp4?token=PG4cvn73lbWC0eFFMaMBg2J36qPWhf05CnpFjSCZ9biu8Z31445SC91VRLsXxZ7PcZtyA4VEfX-r414KlWCoAInlKntBuuSTHjIyGs48WLIXirqX0-mcnv2KWxnN3DuufkrLxIsCiF5gURDkim-JQyNW28Q0KcJKuVHcTPBopFDhZbdaQ8gfzGDNc12OilsxT7JbzyppBH3M3o28Cz4n8Zrs5ug_3iHeoDuAOfpkS1gD8HdqP3m_i0pInCNl7stHdvReZUMa44k1pUeXB2HCbYU8AiK6DThCNF9Ab63Ys0mz8InMOhHAGwIlyMMuUQspsa_Jtt0KKzaebPh3Iaf7VCDPNUVTUxwUR65ThT8Sceby7JmYXEjhaMe_aVrNJQNtxIHuH1Ma8E5f2JQ4R3fpMEa0Js7_8loh6wNzdchkVHiMrKvIw09gsM2CsuVHYlLX_0gVQynzG950CkB33jW9M5EHlXP4bdX8_jdjjSZ3dR9e__d3rhBPHhIu3MPz2B3OnfSkIGdhiGESJ2pB0o3JfLLd6GoYmerAnYx2ddHnG3JnYrcnTND1EanIAaM6En-s84kLRFxxTPf_SD4DJ1IjbUomXu4TUl4ixSMi6mCUmwzN4q1oCOXSMrO4TQ7kyJLL8QFyuL4o1vIOJxzk_Xhg23VhiBCgAWRKivnezjeLzNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ba817d81.mp4?token=PG4cvn73lbWC0eFFMaMBg2J36qPWhf05CnpFjSCZ9biu8Z31445SC91VRLsXxZ7PcZtyA4VEfX-r414KlWCoAInlKntBuuSTHjIyGs48WLIXirqX0-mcnv2KWxnN3DuufkrLxIsCiF5gURDkim-JQyNW28Q0KcJKuVHcTPBopFDhZbdaQ8gfzGDNc12OilsxT7JbzyppBH3M3o28Cz4n8Zrs5ug_3iHeoDuAOfpkS1gD8HdqP3m_i0pInCNl7stHdvReZUMa44k1pUeXB2HCbYU8AiK6DThCNF9Ab63Ys0mz8InMOhHAGwIlyMMuUQspsa_Jtt0KKzaebPh3Iaf7VCDPNUVTUxwUR65ThT8Sceby7JmYXEjhaMe_aVrNJQNtxIHuH1Ma8E5f2JQ4R3fpMEa0Js7_8loh6wNzdchkVHiMrKvIw09gsM2CsuVHYlLX_0gVQynzG950CkB33jW9M5EHlXP4bdX8_jdjjSZ3dR9e__d3rhBPHhIu3MPz2B3OnfSkIGdhiGESJ2pB0o3JfLLd6GoYmerAnYx2ddHnG3JnYrcnTND1EanIAaM6En-s84kLRFxxTPf_SD4DJ1IjbUomXu4TUl4ixSMi6mCUmwzN4q1oCOXSMrO4TQ7kyJLL8QFyuL4o1vIOJxzk_Xhg23VhiBCgAWRKivnezjeLzNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدرالحسینی، کارشناس مسائل غرب آسیا: پس‌ از ۶۰ سال تنگهٔ هرمز کاملاً ایرانی شده/ حاکمیت و مدیریت ایران بر عبور و مرور در تنگه تثبیت شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/679937" target="_blank">📅 12:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55254c2963.mp4?token=bP26LZdVMPkuWGPCw6ng32OSkTEnAgE7lfx3R0U1_x8IWOPjOZR90GIYbvOhWu1x9v9B1EH6DT_Z_XYl93jBQ3kR-O4LtrW7r7QH0ZDWWuIfKUy8E0zavUdP7_jpFwleakhX12gVM6Bf59xANVmmwgHXTtdlZWGxsbs2XUn8cNIjrlMmU_75pODiFGlF33OcRak2cSvkc__Wpo242syOB16l40noGe1CrHRJrA9U2tqgCy44ZW9HlOc2bIbwXLW3YWPe-2ShpYsXQMmVcrb-viBRqOPiIep7LTLOrC-E2KpjBW402FGoyx71bEP7hypYOoN-iOyw5R9f5lCBE7BtsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55254c2963.mp4?token=bP26LZdVMPkuWGPCw6ng32OSkTEnAgE7lfx3R0U1_x8IWOPjOZR90GIYbvOhWu1x9v9B1EH6DT_Z_XYl93jBQ3kR-O4LtrW7r7QH0ZDWWuIfKUy8E0zavUdP7_jpFwleakhX12gVM6Bf59xANVmmwgHXTtdlZWGxsbs2XUn8cNIjrlMmU_75pODiFGlF33OcRak2cSvkc__Wpo242syOB16l40noGe1CrHRJrA9U2tqgCy44ZW9HlOc2bIbwXLW3YWPe-2ShpYsXQMmVcrb-viBRqOPiIep7LTLOrC-E2KpjBW402FGoyx71bEP7hypYOoN-iOyw5R9f5lCBE7BtsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان زندگی مستربین؛ خاطره‌ای برای همه‌ ما
❤️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/679936" target="_blank">📅 12:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679925">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88f47e1bd3.mp4?token=rLpvQD6xUjk_DZWCZevfrSY0R7xWk3rS6aO9OsmCHEvX56rF56qZeEsFxQIxYycnbMXZNAmVXCDPCJOSmNBREhCLg47NfEQEskLo2-VPYVVihIKDakYxmLBOA5Wfae2DmBW8Cpq4hGF7wR385P6HIxP5WfiKBRXZbhipgmLvWyI2z5Ydb13SIcfgDsNyWDRR4cAAeWLx4MHuowgVoEo84i5u0fDmWUX0IjUz7CRQILrfZ6B5qkkJvuYGPQkuvWWAo2BUhXiR0RO8aesykMtsvPShgI0fB6iSvS4iGOE8OcERMMf9C77iKed2XPOHGJ4NLY-PHy6pIGanuJWgt40vgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88f47e1bd3.mp4?token=rLpvQD6xUjk_DZWCZevfrSY0R7xWk3rS6aO9OsmCHEvX56rF56qZeEsFxQIxYycnbMXZNAmVXCDPCJOSmNBREhCLg47NfEQEskLo2-VPYVVihIKDakYxmLBOA5Wfae2DmBW8Cpq4hGF7wR385P6HIxP5WfiKBRXZbhipgmLvWyI2z5Ydb13SIcfgDsNyWDRR4cAAeWLx4MHuowgVoEo84i5u0fDmWUX0IjUz7CRQILrfZ6B5qkkJvuYGPQkuvWWAo2BUhXiR0RO8aesykMtsvPShgI0fB6iSvS4iGOE8OcERMMf9C77iKed2XPOHGJ4NLY-PHy6pIGanuJWgt40vgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قاعدتاً خدمات دریایی مابه‌ازایی دارد و باید آن را دریافت کنیم  سخنگوی وزارت امور خارجه:
🔹
همچنین حقابه ایران موضوعی حیاتی و راهبردی در مذاکرات با افغانستان است و در سال آبی اخیر پیشرفت‌های ملموسی حاصل شده؛ رایزنی‌ها برای تحقق کامل تعهدات…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/679925" target="_blank">📅 12:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679924">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d434b9cefc.mp4?token=atdtmxcHhALkxhwALd3JFn9G0t797AGPS-JJgzJdMbOex8DqY3UXvbgvq5A6ugp7eSPylUyyWs5_dyA5K36BF-UQjkgiUeEJDsx7NZYchOFd67gewh_BsQjGNtMvMgPtCWEX2nBQ0eoxze8Hq7rkMLtrkZU60Q70A9nhkFROU1pvwSkDPRMZlCnkhQ8zkfaorbuZSV-_R2HX4a7AtshsKoc0FXmAiZLqBq_fcKR8jGItszXapd0AHCPtU_yhh8VLFYuW00-UQKU_iuCAne-NpW9ioYmIBti4rdz6rNUMKl7bmNbd-o3MzgdnmppxP5Yap-d8ndZ7SspglrgiahprBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d434b9cefc.mp4?token=atdtmxcHhALkxhwALd3JFn9G0t797AGPS-JJgzJdMbOex8DqY3UXvbgvq5A6ugp7eSPylUyyWs5_dyA5K36BF-UQjkgiUeEJDsx7NZYchOFd67gewh_BsQjGNtMvMgPtCWEX2nBQ0eoxze8Hq7rkMLtrkZU60Q70A9nhkFROU1pvwSkDPRMZlCnkhQ8zkfaorbuZSV-_R2HX4a7AtshsKoc0FXmAiZLqBq_fcKR8jGItszXapd0AHCPtU_yhh8VLFYuW00-UQKU_iuCAne-NpW9ioYmIBti4rdz6rNUMKl7bmNbd-o3MzgdnmppxP5Yap-d8ndZ7SspglrgiahprBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«نترسید… پای وطن بمانید»
🇮🇷
ایران، تکه‌تکه نیست؛ یکپارچه و جاودانه است #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/679924" target="_blank">📅 12:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679923">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOJAHS2gV97tOC4WMsEV4w9-nY5J1kekDWiAnxvH_YkWEodiY2XGPaoaYa1J2v0eDqWWIEK2tf9mrI0Vd5NDj8DwSMWNFwKne9fOKQRocVv1j3ENVRAQvdG_7gYNldyx4fo643IeOe6CA7tkRiB3DnfwXpZ8hUadXEqw7R3o9XwKv9Lk6su1PHapWwUVDZjsuGuYj1JHtjVVwH6-ZlD1lH_dU6I4z7I_kAHCqFZjdR64hk2N7rVVE8gNvsP6kZ-ryRDltyzjKsS8XkhJ3dS644auOOjmKFV7KBXOisZi5MAPKKxzb2OULK-bY_3njDKcXM40Brc6KZydlSvEQ2wuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
يايان يك وابستگی راهبردى
🔹
بهره‌بردارى از نخستين و تنها توليدكننده الكترود و محصولات گرافیتی در خاورميانه با سرمايه‌گذاری فولاد مباركه
🔹
تامین ۵۰ تا ۶۰ درصدی نیاز کشور به الکترود گرافیتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/679923" target="_blank">📅 12:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679922">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02c24c2ca.mp4?token=pwANrxO2j99BZCY5v7uPabcEkRc9nJAyWKin4HRfgAcONcr_zDx2AOD9aZiixlzmzUPtjzEnHnk6k1vkZrPkeADCTRqx0asvCNbisWgS2ZGOZjVwqodH1F6sRtx3SfBm9BMydW1FGqea9ksjz8N8mCHP1ciwAzpCnZq5wiHmGh1OpCc4EF0icHb2ZP2kTODBAYWBzQaKMgTpvsMue_MhyBQ6VR44M0vkBS9CTaEAEQin7eV01_MOIgij8AgcnGwoh-rst57kkg6d-rlUzSPxjbameb5hNRezQT1mRs8Eapiat0lH1DROZ8Y2cVoHb1XUEoqOV-yM86u5BPdDyx_XrGlG-zzC1VP_PNSowZXPuN04_aClR2AKaoBd0kv_CYok9ezTIivSjG8AYpe1DtesxhMqhqg_ZnLpDbhgzOZGXjXsbHuFtxSOAlArzrFUeRfaYukMwqcojDIDRcISsQAZIoAcwvb_cvsoBXDDMnAzgKHRGb1z3BvQy_NT2qyjYxgI--YSTzw1y1t_b4obIANb7DWpC4Yp7TPNWD0Vh2Q9sy8uCk2Pxv0Ly3oUmGmdFdpXuQFAeS8nt16cLNcyXwfDaQ9SKH1XdIr3NHaiu-frvNpTS3DrlgzPvmO08wAtBy9aRN4cLusV6yEL6q95Y4794CXuV9cF-odpvZuyaZD8xmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02c24c2ca.mp4?token=pwANrxO2j99BZCY5v7uPabcEkRc9nJAyWKin4HRfgAcONcr_zDx2AOD9aZiixlzmzUPtjzEnHnk6k1vkZrPkeADCTRqx0asvCNbisWgS2ZGOZjVwqodH1F6sRtx3SfBm9BMydW1FGqea9ksjz8N8mCHP1ciwAzpCnZq5wiHmGh1OpCc4EF0icHb2ZP2kTODBAYWBzQaKMgTpvsMue_MhyBQ6VR44M0vkBS9CTaEAEQin7eV01_MOIgij8AgcnGwoh-rst57kkg6d-rlUzSPxjbameb5hNRezQT1mRs8Eapiat0lH1DROZ8Y2cVoHb1XUEoqOV-yM86u5BPdDyx_XrGlG-zzC1VP_PNSowZXPuN04_aClR2AKaoBd0kv_CYok9ezTIivSjG8AYpe1DtesxhMqhqg_ZnLpDbhgzOZGXjXsbHuFtxSOAlArzrFUeRfaYukMwqcojDIDRcISsQAZIoAcwvb_cvsoBXDDMnAzgKHRGb1z3BvQy_NT2qyjYxgI--YSTzw1y1t_b4obIANb7DWpC4Yp7TPNWD0Vh2Q9sy8uCk2Pxv0Ly3oUmGmdFdpXuQFAeS8nt16cLNcyXwfDaQ9SKH1XdIr3NHaiu-frvNpTS3DrlgzPvmO08wAtBy9aRN4cLusV6yEL6q95Y4794CXuV9cF-odpvZuyaZD8xmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در حال بد شریک‌عاطفی‌مون چه رفتاری باید داشته باشیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/679922" target="_blank">📅 12:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679920">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae87096f27.mp4?token=oAtFTRvS5HA-G9K4sMPbUZPgc_ZmaOc2axyVnGtEbhuzZTA0ENgdmkt7Yb-qmWUtBll1EydLYMWYEp0i7EDCIPtW2btPA4cG2rxq-E6dLDkKJbcT8e9qfsyp_JT0UfS11mE8Cp_vZPFIKnb2S4o0UqXYZ8BUJ-W_PiP3FK-E_BE1ildTDwmbv7oYh1mEEroaKFLZue4A1spNKSJqqRq-ZZ2Ix3jn_uoragbUGsk2xKm3EHyiWsZeSql6N0fHcyi-acdDVkr6GZ0mJ_IKR_5nG9VENXRA0xLntIu8i2YV4gupzeIJ09x9I63wTB4luR0fe_GnQQwojcWlzuC84DPHOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae87096f27.mp4?token=oAtFTRvS5HA-G9K4sMPbUZPgc_ZmaOc2axyVnGtEbhuzZTA0ENgdmkt7Yb-qmWUtBll1EydLYMWYEp0i7EDCIPtW2btPA4cG2rxq-E6dLDkKJbcT8e9qfsyp_JT0UfS11mE8Cp_vZPFIKnb2S4o0UqXYZ8BUJ-W_PiP3FK-E_BE1ildTDwmbv7oYh1mEEroaKFLZue4A1spNKSJqqRq-ZZ2Ix3jn_uoragbUGsk2xKm3EHyiWsZeSql6N0fHcyi-acdDVkr6GZ0mJ_IKR_5nG9VENXRA0xLntIu8i2YV4gupzeIJ09x9I63wTB4luR0fe_GnQQwojcWlzuC84DPHOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهکار مکانیکی از دل ضایعات!
🔹
مردی روستایی در چین یک بازوی مکانیکی غول‌پیکر را تنها با استفاده از ضایعات فولادی و کار دستی ساخته؛ بدون پرینتر سه‌بعدی یا تجهیزات پیشرفته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/679920" target="_blank">📅 12:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679917">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOzsRDLELFTHiN6Q_Sich4iJBXFLPD6H7sMEJaCzfSCQyu-Wpkd_7p1BExpG-GTfPQkD4PO245jLQbI5QN7YJwhNS4kMAC-m0ZHdhD7Ry9tMKow8L8Uit-DO47dBPQNp_HS4ZHsqkdtCiPiGHP9ip0ixZg6jFh_GZBA38ODijqGQ7eKsl2Pd1T6htwfHD8YCmYxbZqnHf_TrmsGCzJbMDcjQHhfuhCfK9G-PS38xBZyCTARDV9J3-N9yItsIeJKGtN-ODFleP1y1VQjhcdhaztQH_BZy3aryM5arKNlLm0YBzEzLZ9oIX6lo9HY28ltZHfwot3neMvaCCoaJSfCs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نیت خیر شما، لبخندی بر لبان کودکانمان خواهد شد.
امروز بیش از 14 هزار کودک، تحت حمایت محک در حال پیمودن مسیر درمان هستند.
با حمایت از کودکان مبتلا به سرطان، امید رسیدن به فردا را به آنان هدیه دهید.
روش حمایت از کودکان
#محک‌
پرداخت آنلاین:
https://mhak.ir/makakcharity1
تو می‌تونی فردا رو رقم بزنی
❤️
موسسه خیریه حمایت از کودکان مبتلا به سرطان محک</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/679917" target="_blank">📅 12:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679916">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b0b97643a.mp4?token=t-NpXnPGUF1pDpwDhbV_72x7b0vrypHqV4SUWGx0hxuRJCf-EYvxggUKLz3bg1rSvPOzNukeFqVqD6YdVtJxwv4uzwXT9KYNuzlYqGsNaQH7MH5aets8_DxPtPmUWsoTYdWj7V4jhtBiaVbNmXBa4gOwP7-loiBv7gbJJEIwbiFASKz2JMTRYQ10oSF3EM_DySlQfwNe0mw7AnIEXnbLUKq2yx0T1p13xjmFY6NDLYIdd9ja1DTZNaiuNSTCTYg-HtQNY5bpuv7fttJgYal6BYp0IWOGScPLoMJw7a4sOKvqhQcaP7nDaafkfvsRgDKMKiAoFI-hgVNfHbWSXklKtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b0b97643a.mp4?token=t-NpXnPGUF1pDpwDhbV_72x7b0vrypHqV4SUWGx0hxuRJCf-EYvxggUKLz3bg1rSvPOzNukeFqVqD6YdVtJxwv4uzwXT9KYNuzlYqGsNaQH7MH5aets8_DxPtPmUWsoTYdWj7V4jhtBiaVbNmXBa4gOwP7-loiBv7gbJJEIwbiFASKz2JMTRYQ10oSF3EM_DySlQfwNe0mw7AnIEXnbLUKq2yx0T1p13xjmFY6NDLYIdd9ja1DTZNaiuNSTCTYg-HtQNY5bpuv7fttJgYal6BYp0IWOGScPLoMJw7a4sOKvqhQcaP7nDaafkfvsRgDKMKiAoFI-hgVNfHbWSXklKtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قاعدتاً خدمات دریایی مابه‌ازایی دارد و باید آن را دریافت کنیم
سخنگوی وزارت امور خارجه:
🔹
همچنین حقابه ایران موضوعی حیاتی و راهبردی در مذاکرات با افغانستان است و در سال آبی اخیر پیشرفت‌های ملموسی حاصل شده؛ رایزنی‌ها برای تحقق کامل تعهدات ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/679916" target="_blank">📅 11:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679907">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سوال یک خبرنگار درباره نقل حکایت سخنگوی وزارت خارجه از عبید زاکانی و تهدید ترامپ: نفهمید چه موشکی شلیک کردید
بقایی:
🔹
وقتی با خوک‌ها کشتی بگیری، لاجرم گل‌آلود هم می‌شوی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/679907" target="_blank">📅 11:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679904">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwrvfrwgmTGINv65qO9Lrvh5njzU5bJSImZ1TkG6uaM_Aws1q03o7aduGG4a6RSiIc2A9y0s_1iAYhBvZrqpZRG67lclEk3T_8GH4PV1Of30oS7Nvdb9LAg8z4zj6c1Dw0VbuwV8LO1s377g_Sm9wEvIUmu8hYQqMRDuDXFRHMCCDs-HbpXN6UVrwOzLkzimUF-TBlpGs9AsrUpVefGZZdEV56U4DUm8Azx721j8N6DQAQS1LbPnh_YtpEWNpe9COGBXaRp7Huw54hTPY2Sl3PJ9HyQr8hiAvOezs52WhMtOFCHVl9z23Jlzl-xkaNDplB_sLHAGJOPCXIJsBibYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
سجاده متبرک حرم حضرت معصومه (س)
یادگاری معنادار از حرم کریمه اهل‌بیت(س)؛
انتخابی خاص برای استفاده شخصی یا یک هدیه متفاوت و ماندگار.
💰
قیمت اصلی: ۳٬۸۰۰٬۰۰۰ تومان
✨
قیمت ویژه: ۲٬۹۸۰٬۰۰۰ تومان
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
🌐
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/679904" target="_blank">📅 11:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679903">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d36785b85.mp4?token=Wl2yvwnJD25ElL1FYyQuDL12tzrVj-a_upDDnXsZ2Vx0E_R8wCe0FYvci5twl2KVyzCm2Wk7-zo9d5FD5fM1g-EYAxev38uhag00YV_KUEgcVyy2h3LENUequq-4QYBPfze1vxgCV_SIRyXQ8MrSHJnYO9_Z-5W7DsFMmcwquNvcpJUoGxOo3kxSC1SSo2oc0q_0BhGCI3lZlp_--Fag0OgMTgeA6QQv1dzsdHDZeM_-y0KiAbp6lxYbfaFe9_1VyQxqkppX98HMZ3hlvIDi7w65DMAzQJpsPvavQyYOVaE-6OfZuAQZ9W8Ki01lFAiiZrPl_aVvj6G5MDaqGyofRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d36785b85.mp4?token=Wl2yvwnJD25ElL1FYyQuDL12tzrVj-a_upDDnXsZ2Vx0E_R8wCe0FYvci5twl2KVyzCm2Wk7-zo9d5FD5fM1g-EYAxev38uhag00YV_KUEgcVyy2h3LENUequq-4QYBPfze1vxgCV_SIRyXQ8MrSHJnYO9_Z-5W7DsFMmcwquNvcpJUoGxOo3kxSC1SSo2oc0q_0BhGCI3lZlp_--Fag0OgMTgeA6QQv1dzsdHDZeM_-y0KiAbp6lxYbfaFe9_1VyQxqkppX98HMZ3hlvIDi7w65DMAzQJpsPvavQyYOVaE-6OfZuAQZ9W8Ki01lFAiiZrPl_aVvj6G5MDaqGyofRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: مدیریت و تأمین امنیت تنگه هرمز بر عهده ایران است؛ نقض عهد آمریکا در تنگه هرمز عامل اصلی بروز درگیری‌ها بود
سخنگوی وزارت خارجه:
🔹
تنگهٔ هرمز به‌خاطر اختلاف‌نظر ایران و عمان بسته نشده که با توافق ایران و عمان باز شود. بازشدن تنگهٔ هرمز منوط به تحقق شرایطی است که در پی تجاوز نظامی آمریکا و رژیم صهیونیستی به ایران تحمیل شده؛ ما هنوز در جنگ هستیم و تا وقتی که محاصرهٔ دریایی آمریکا ادامه داشته باشد و سایر نقض‌های آمریکا نسبت به تفاهم‌نامه جبران نشود، تنگه باز نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/679903" target="_blank">📅 11:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679899">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJ9AJrGkjnLFBfpFrxNdLa9z-iolP5TqB6d7d-y5rPrwU_Xeh9DWbc6zVS_3VSeFOXBNYjICFIdStX6sCoQ62al5R4Ij6UGj9ltwZ_c0nliNH_ocGx8MaZ8BN7Wm-iNtmlZB6MROIZVoErNOneHwZdTFaA6RPWcTzlZoR1-cVv_3tnTnAOu9EAKNVZ4F6F05JgZHo4hJ13cQwiW0MrKIPHUoBxMfcp_RguWmK1l_0wbPh2v6gLBKZ9j2yBdsBag9tjtfpHfZ0I1dDnNeJAd94Vb2hZgJkZF3wwgWrZGzOpu-6-VXSXrHpeQMnr8AE4isfNhIJpDF_YvpWu47mDRi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ns8esu2Jb7C7trjAgu13sJP_D_LhgbIWWx1W4lIkJ-p9OeWE6WUXSqMTepNNmWsf9paBzjOwYUMAcoSWUJAUFIancepjaWbtGLqW1VKDXja6BewXJwjv6F93fFmTn_c5l1B9xtbUb1BakNIENALeUwfwEfFSEkaoGs1RfITr_9xFqvU8rAn7DST9UKVGSCon3EKCr1Bx-fm5KE0S_z7qlYEmTOxg2-rcZ9Gh_4ErPgsewVLQnIs6ZjRlGcdOy7hODLUy9WfCX4efg51yMUAmRi7Co1XFEk6NEM8pku5VMNu4btwuYsUn2mg27RmAINJ1QO97XalAJgIoMVIcv-jCng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دو تصویر متفاوت از محسن رضایی در کنار رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/679899" target="_blank">📅 11:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69fb622a4.mp4?token=jXdGTEPBu4bfYwixgCa45CFT98iHkIYwu1oHt9ARTUgvPTmJ3wFpoVMuqW7EIZhogjMSkuvosxNWUigeEPKbMfWCAELE_7Dh33HtUfwAR-HGH2xM43vpXdsKItxT0a8hlTaVNG-J4gDEvSN4zQMI0yjMvtAUd6frveXSxDY7XynJwm1QdmUyeuJRzTUxyzjS2QsIi_jvXEUhLRyxUnI-1Cg4JiKEZ7eFa4n3vhIoC6usExuqvkFbybUMYkl7Ieo0WK-b-4ePGgCbyiG7vdszn7tAPO_pbeNtde-t9bfMtWI9l7zvz8xDI4DBP9AOcqdTx9q7juKRfLLGveIZazbD5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69fb622a4.mp4?token=jXdGTEPBu4bfYwixgCa45CFT98iHkIYwu1oHt9ARTUgvPTmJ3wFpoVMuqW7EIZhogjMSkuvosxNWUigeEPKbMfWCAELE_7Dh33HtUfwAR-HGH2xM43vpXdsKItxT0a8hlTaVNG-J4gDEvSN4zQMI0yjMvtAUd6frveXSxDY7XynJwm1QdmUyeuJRzTUxyzjS2QsIi_jvXEUhLRyxUnI-1Cg4JiKEZ7eFa4n3vhIoC6usExuqvkFbybUMYkl7Ieo0WK-b-4ePGgCbyiG7vdszn7tAPO_pbeNtde-t9bfMtWI9l7zvz8xDI4DBP9AOcqdTx9q7juKRfLLGveIZazbD5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا پزشکیان به نیویورک می‌رود؟
بقائی:
🔹
تصمیم قطعی در خصوص حضور رئیس‌جمهور در مجمع عمومی سازمان ملل گرفته نشده است؛ امسال هم در نظر داریم از این فرصت استفاده کنیم
.
🔹
همچنین دعوت‌نامه‌ای برای سفر آقایان عراقچی و قالیباف برای سفر به پاکستان واصل شده و هر وقت که زمینه مناسب باشد این سفر انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/679898" target="_blank">📅 11:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679897">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig7IN9gX6df-uTfwhCEHl_Tv9GOb9h1nxuwmvkICXxCO8QDesrm-wZKn2Fgu20rEGGu0_bcQUGS3WPQJz9xq64g-yRmWDC-ap06uuq3RQjgt8MHRqPBRE-jyDlZ0CpL93NrddQ1y2okxViYdAjy7g6qcJlYFNC8szLleqJlhQzXe1FSIjMulNfIBRyLJ8L45RlGYaScD5SjFPSQpX74-srrh1DCwgb-ZGC7Xiv6Ukw3sXdgO4MA6U5fH-fSaWZTl-48sgIiDwv6pR4PdVJck2VE9HEFiGfxFzXVaGUY2uMOuMHWogU16s-6zUYQD7xh8grVEyWGsj2Lzbypm_2TKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از احمدی‌نژاد در جلسه مجمع تشخیص مصلحت نظام؛ روز گذشته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/679897" target="_blank">📅 11:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679894">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd277d9b53.mp4?token=mXLQ8NRStjDcokD8-JVKd_4S8PcYgQQOxJ8D0w_TtqQd9F-SN0-wxyCjLo9J1eCCZ4iSkYJC_G8r1CSrTPGXwdj7T7g8jppwhQtzCigOx8Sz-9qLv1J1DD7LwHQmn6kunYHfe6C_OQun8daoyv6d-jv54TY845gNlAjqjIz0cZCvBe8qqdYq8pgNxwbVRhdxP1_lJfXjWqKPxpyWS2b3b1Q994GkF3VlOnEZzjwyTuenNbqB3GfhoHp6ATV2si0L2BVNne7MA8iqTTngUWtzSyLHk5AcktPjS9txx_zmJlTPKBlACM7CEyBVm10ytYx2LesCk2eOEudm-SeqpyeHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd277d9b53.mp4?token=mXLQ8NRStjDcokD8-JVKd_4S8PcYgQQOxJ8D0w_TtqQd9F-SN0-wxyCjLo9J1eCCZ4iSkYJC_G8r1CSrTPGXwdj7T7g8jppwhQtzCigOx8Sz-9qLv1J1DD7LwHQmn6kunYHfe6C_OQun8daoyv6d-jv54TY845gNlAjqjIz0cZCvBe8qqdYq8pgNxwbVRhdxP1_lJfXjWqKPxpyWS2b3b1Q994GkF3VlOnEZzjwyTuenNbqB3GfhoHp6ATV2si0L2BVNne7MA8iqTTngUWtzSyLHk5AcktPjS9txx_zmJlTPKBlACM7CEyBVm10ytYx2LesCk2eOEudm-SeqpyeHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/679894" target="_blank">📅 10:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679891">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmUjtUOS5bN0JnBfxh_sBnEjncFG_cs7hEzch6mTG2FcvhzjGWIs3VrLY_tb4jD6_Iw3rQQp5gTg2ZBNJEtGgF6uG-_MdybZSEuB3WtuafmpZ_FitKJy_mj8GgSZ1oNLMDAnvqp4HNe_3ROgEMokLLznbqIFstZSLi-lGgv4m-xT8N9MfBmn4UR3U4AluMrqZHdkSxI-HaoQBC3jxZTNueaMEjS3eUmN2CLUJPbHF52sg2FUNSny58oQlR-LruPufA7p_6rJebM1yLnEG4NApha7A01EYLBlHZN6EP0IXO024KYHAAk57scbUXRWNujMs2ysu2DIi6BJzt_J9Y7cSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«ونوین» در بازار رکوردشکنی کرد / ارزش بازار بانک اقتصادنوین از ۱۰۰ هزار میلیارد تومان عبور کرد
🔹
در مقایسه با بانک‌های بورسی، رشد ارزش بازار «ونوین» همواره جزو بالاترین‌ها بوده است، به طوری که هم ارزش بازار و هم رشد ارزش بازار این نماد، رتبه‌های برتر را به خود اختصاص داده است.
اطلاعات بیشتر:
https://www.enbank.ir/s/mfa8Od</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/679891" target="_blank">📅 10:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679890">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a024cee033.mp4?token=S6HP6IwtNgvQhxwtixsx1b2e1ihKW-1Uug9ElVA5YBPPSG0taeGQvYY7pDleq2ZU_t6lWYxWmTHMl4GQEcMdvDdqgS26CDM8Y6anoNW9cIBvbhjSeLZBeebNW5oUrvBCM67X1EYeXMS1ErUobb9Zt2yzGBLheUSxl3lkqKNe9HETpH74TfA6TdFHu1Nh0-6Xr7LpqMIUdt2Ia2-b48iiE7ST0aQr2KLJCSxSoFPXSR1x10Qi0Qq6bgvDxl14PfIrLDT75vY8V5ZbJWJjfFt2lt-L0GlJmt0vQhTARVtjDX0Jzenwp9govFN9WFmnkhKuNzOLM0jP4HBNIYxTPsvedA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a024cee033.mp4?token=S6HP6IwtNgvQhxwtixsx1b2e1ihKW-1Uug9ElVA5YBPPSG0taeGQvYY7pDleq2ZU_t6lWYxWmTHMl4GQEcMdvDdqgS26CDM8Y6anoNW9cIBvbhjSeLZBeebNW5oUrvBCM67X1EYeXMS1ErUobb9Zt2yzGBLheUSxl3lkqKNe9HETpH74TfA6TdFHu1Nh0-6Xr7LpqMIUdt2Ia2-b48iiE7ST0aQr2KLJCSxSoFPXSR1x10Qi0Qq6bgvDxl14PfIrLDT75vY8V5ZbJWJjfFt2lt-L0GlJmt0vQhTARVtjDX0Jzenwp9govFN9WFmnkhKuNzOLM0jP4HBNIYxTPsvedA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در سفر شی جیگ پینگ، رئیس‌جمهور چین به ایران، دستشویی هتل خراب بود!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/679890" target="_blank">📅 10:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679885">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره تخصصی اتاق تهران برای توسعه تجارت در بازارهای خلیج فارس
🔺
اتاق بازرگانی تهران با ارائه مشاوره تخصصی، شرکت‌ها را برای ورود و توسعه تجارت در بازارهای کشورهای حوزه همکاری خلیج فارس همراهی کرده و مسیر صادرات را کم‌ریسک‌تر و هدفمندتر می‌کند.
👈🏻
دریافت مشاوره:
۸۸۷۲۵۲۶۹
(۰۲۱) |
۰۹۱۰۲۶۶۹۷۱۴
|
service.tccim.ir/intl</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/679885" target="_blank">📅 10:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679881">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CmXrqop1uanWMAkRw13GqhSFo4mPqrQGksmt-ll05lh1YehjiIGwSOwY9z1q84D5bDZ3--F49ugbsfnqC4ARZngDvCkz-nVa5yciKPrHAO3N8OWVArvm5otj-CtKobNl82o0etCKao86OgagZHZjbaoEihcn-Z0B_Xp8PPMmziHbyiUJ_UfnlP2DaE7Bfj5bjiYXiH_TrTIAlTllbeuom0jYHyj-L7siwmBqKjLOdoN5dltHNk73FsN79ie-dbeMDhbFy3h5kOcg0Bm75gmXyZBLBs300qyxWtuifs2oY6jF3bqwEp261RRSI1ZXYvq5u0pIMSwJgTnaWrTnR6oRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWSeHEY04ZqjLOPJJlM_qvjHCrivOrP0tI7nlUOCPmFne4UoNyQQntaoEyhu50nVPJa5dfMfIKIT-u_BVKZxDcRfsASKy3dEmMYbLAuGWNyDulm-aR_Q30rUp7Qx-kfLiUfGIe7lRWt_l2u6Yp7I_UpWyAwKxUwOC-TgudSQUaCYpLDTzW9hyq8PNijPZ1PZAQBSRbI6cDZRFtaLcOq1PWFt50f36ifz2VPqhqeiYMOuMaJs9Mh2WShkcuc0sZlcHVRsiY6qe6qHchhGhvWU0xi94ELvIW5Lt8gbfkeE0Z__oXFj1K9GrbUpyEKo1hAedIAmfiiR9yasSHzBlM7u_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b53MUZ6sfo9nG1bb_-FIhYNvoF-O1x_1kiQTFUTWUO5zlCwIJGyYU4xmhcSEKVFdb9zSr7xhYOdvDFWRzcVl5i_XyHPvfPBiYh4Ut6rQyWHrfn7N6W3lFgUB1VlWKU90CGj6zWh4bK_y84sEvNk3Jozj2eCM5Nukm3wC_T1v-MFX0HRtgu0CQ9uR8kXmfkBLeHpESxxR-1PpnUtanb4qrbSGk6SiTzWvhewYXXgMEaryJPSIm2zdW9-U7XSIpH3RAAHfRO6GTRsQVjZWapDe6RYsiTzERH4gVBwsf2A_PapLB-YW_iDI897WeGJ7NmsjX4HVcnx37g2LJjGHBfOYdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چنگیز وثوقی، بازیگر و برادر بهروز وثوقی در بیمارستان بستری شده است
فرح‌بخش کارگردان سینما:
🔹
بیش از یک هفته است که چنگیز وثوقی به دلیل بیماری‌های قلبی و کمی عفونت و همچنین مشکلات ناشی از کهولت سن در بیمارستان است و مشغول مداوا است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/679881" target="_blank">📅 10:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679880">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
اولین تصویر از کلثوم اکبری بعد از بازداشت/ زنی، اهل ساری که متهم به قتل ۱۳ مرد که همسرهای صیغه‌ای او بودند/ رکنا  #اخبار_مازندران در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/679880" target="_blank">📅 10:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679878">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da51d32c6.mp4?token=pvVS-deP6XkbfPb7pLty-qrtdSwC8VIwCpnqODhvGEUBvFb3y-WQpO4X9F4asA-Av16aMt1NecgYQQOs0rB3zVztjOCiyg5azLsGj9uiKF_jKdAnFI77qD8RGuXdP1ud61aIcMNWas1oGqpyqPHfOwiL2H7IWF21Yd9AY7EqfdA2aXb04KFBLBcQ7EGlyorJkpjNLNPOc8o_cG48cFlaS-tfT9SjCEREZS1JY0yqnn-5j9RcA3EHbSP7PWpNR7DP4VsWl_5QpfDbeBlLsH3fZaDD-hPc5-qgb1EvPOlmqs4Sc6OTOCskRJiIV_HyCD6YT1rx5DPylCIaaXU31k47ybKMQA6LuDT7q3kgjqdPKAka8PXiMqZiEPOlWhAe8RNw0k1B6N257SanrJZeLEwZXKJMOXRnn54m37PtBA8eGNi_bve8jT3ZSDTSab9vaQsDRk7DxAKPHZi_MxqP60xeFNc8vl1MIq66jOKoC8bWOMWVWOiOZdg6CWvk5flC5lbGmUljw_waJCBDt2gkEmjbMnOr5fUnNiES6RiRPb0yG222Qhw5ImZjCV7298fvjoEaH6RlJs-RHJfkRAWrEHG0QVQEm145BcGTAi0YuMjABb6BMg7A0_tFg9RX3ZBkHJHqOXgensns9_6OrKbh0YmaRyyJLQ2RxUFnKbyKi8xTFMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da51d32c6.mp4?token=pvVS-deP6XkbfPb7pLty-qrtdSwC8VIwCpnqODhvGEUBvFb3y-WQpO4X9F4asA-Av16aMt1NecgYQQOs0rB3zVztjOCiyg5azLsGj9uiKF_jKdAnFI77qD8RGuXdP1ud61aIcMNWas1oGqpyqPHfOwiL2H7IWF21Yd9AY7EqfdA2aXb04KFBLBcQ7EGlyorJkpjNLNPOc8o_cG48cFlaS-tfT9SjCEREZS1JY0yqnn-5j9RcA3EHbSP7PWpNR7DP4VsWl_5QpfDbeBlLsH3fZaDD-hPc5-qgb1EvPOlmqs4Sc6OTOCskRJiIV_HyCD6YT1rx5DPylCIaaXU31k47ybKMQA6LuDT7q3kgjqdPKAka8PXiMqZiEPOlWhAe8RNw0k1B6N257SanrJZeLEwZXKJMOXRnn54m37PtBA8eGNi_bve8jT3ZSDTSab9vaQsDRk7DxAKPHZi_MxqP60xeFNc8vl1MIq66jOKoC8bWOMWVWOiOZdg6CWvk5flC5lbGmUljw_waJCBDt2gkEmjbMnOr5fUnNiES6RiRPb0yG222Qhw5ImZjCV7298fvjoEaH6RlJs-RHJfkRAWrEHG0QVQEm145BcGTAi0YuMjABb6BMg7A0_tFg9RX3ZBkHJHqOXgensns9_6OrKbh0YmaRyyJLQ2RxUFnKbyKi8xTFMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیاین باهم یک دسر انبه یخچالی درست کنیم
🔹
یک عدد انبه بزرگ
🔹
یک بسته پودر ژلاتین
🔹
یک عدد رانی انبه
🔹
یک بسته بیسکویت پتی‌بور
🔹
نیم‌کیلو خامه قنادی #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/679878" target="_blank">📅 10:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679876">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شهید علی لاریجانی پس از شنیدن خبر رد صلاحیتش توسط شورای نگهبان: این‌ها اشتباهی هستند و این‌ها باید بروند؛ من هرگز روی صورت انقلاب، پنجه نمی‌کشم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/679876" target="_blank">📅 09:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679875">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea5aa23a3.mp4?token=Ls_dQtS7OLUcx8sKR5kdMnUHN6av3yS4PQW3rPgG6vpb34PEh-6PPnMtmMcHhbduv3IKHIvCIGtsgS3WbbUxmUDn1ezWqlHoB01F5TaMU36msyVjvalRc1tnrFNC--UjeO6DIzPjvHZ7jsZJxa6dX-YrQ0cYLKBcKLrSMU-R6CerDwHKFFH7S3s1LSzrAjguWqy1hxkVio_QjeSZFIvQKiagZT2_kN35NKtCRfpQcD9ekwTf-l6PHV5hbkCK6Ezq9eROv-7aIMaL1KTOID0efU0gnQIWhlLPKYA3bZDKgRa_7T0DYgABwaWqHfaiECRHY6YAKFKBM0Sc_pLLnaISGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea5aa23a3.mp4?token=Ls_dQtS7OLUcx8sKR5kdMnUHN6av3yS4PQW3rPgG6vpb34PEh-6PPnMtmMcHhbduv3IKHIvCIGtsgS3WbbUxmUDn1ezWqlHoB01F5TaMU36msyVjvalRc1tnrFNC--UjeO6DIzPjvHZ7jsZJxa6dX-YrQ0cYLKBcKLrSMU-R6CerDwHKFFH7S3s1LSzrAjguWqy1hxkVio_QjeSZFIvQKiagZT2_kN35NKtCRfpQcD9ekwTf-l6PHV5hbkCK6Ezq9eROv-7aIMaL1KTOID0efU0gnQIWhlLPKYA3bZDKgRa_7T0DYgABwaWqHfaiECRHY6YAKFKBM0Sc_pLLnaISGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا همسرت همیشه صورتش را می‌پوشاند؟
عثمان دمبله:
🔹
همسر من یک زن بسیار مذهبیه، پوشاندن صورت در اسلام اجباری نیست، اما اون واقعا بهش پایبنده؛ گاهی بهش میگم که حداقل صورتت رو در جمع نشون بده، اما اون همیشه به من میگه: عثمان من میخوام فقط تو صورت من رو ببینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/679875" target="_blank">📅 09:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679869">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJ8oG3YZx51UAt1sCWnvbHB_Qc2ZXsDZnlehi6J7h-ATN1mdjaGIROtrwPxfITMdNyLSWZ9_MgNI7AVbFsFMnZkGPqgimQPR6D9t8rmP8SSXpbTSVyHdtUVa0tU8I6cgnLNrTjWO0LUHEC5RpHV3t4NtVkM_Bm7gyrapMEsCRKz_RGKD9qxfSBQt8hIzn0LyNKro-I-FieWTzyxfUoTjfslYJjUGqVOyKBlWmSl4tKq6o5ShVK3CY6znpHoHBESkr9tVOV-ZBd0V5XaRnxF22V618vCGZBv23HC3EnqAnLxxlwhj6uoMRfxut6NTZgE6IzF9YbTTZ37vMnlivMPfYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gb8oStzC402R6PqtOPqWasWeXNDK72rcUzRnEmHsTcVd_PDcSW0tZvm_taiyVt3yU8CXIGvTRwRHxGRLgB2CtLXjs-GP52tL7CyBqGRPv3B24NLasiSOV2yPNYvQE7Rh1WPflGRCQ6c9ggGnclLEYotEkHqTAOFIbimHinPEoP_bRlBER8B5aF15SvIE8JzGREl-xm86795TXjsyBeuppOGyRmI58Sh9QxbyLYAx34JtfItQWmhV-0hz-N1ju73yT1-re3th9S09BgMaL-yD6OIs_JA9F6j0ZClvUZ_pp2JsAwSCGWIGDExZy1xCHu9x-wKj2mgF0y2FykE464ceoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSIqP2RRfs6F3aMjfK6BCAxJ89TOp-pmIDstxWqzkyEPez4PZoE6YkSKOGtVoQX2P_gpT7Q7j56x-LTfH1fiI_oj_AdTXrbKiKod_WLXai5CcO-5o8qHtxhWsZUh5kWgVG_Ga7WfZNyMDqUSglMswQ2vBKrcf_WZzkWRr2xCCJEOI7HOV0CrCdIv30bF17AaqUkYRYve88_JrOTYOVIuaUpQzlavEPnFzX0TcQ0VChxTFdKmgLwP6b1PnFyLPyjjXpUGGjef7InnjPwqFUio6vTqKjDOQqW2FxjPf3PDNYkjwpnUpHEdAXMNl0dqIc4pznRRpqGlfVNqi_4McOb0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeqfZ0QGvNdwxWkpMP92X645464dXmsdJEwaZsBlxvxH0P7k5y4xVq7at3GpOnqM20jC1L2CESH0yEo4-9fr_A9gqOxQeftRsu4hgvTaiZIxmDx8LxEgLtgqupCZEdMMIVAqFYOW9xCup9IYBWZu_xPVCRB5jpf6LwGYfjNtRq6fVxIsUOVGPTgP4VGLoGp_4B0GTckBwV2laxAqWu2DZeW6fdX0RDB4TYRZtAx3JzQ_gmBdp7eD9w-65vxQs2dybIkoJ0SVJDiQ-7TB3XDXci_X2hvGQCp8pxKk68EpRoxegWAIp2DGZE2DEqFbPMHaDFuQSP0mKLExynYMMb02rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3tALI-gC-rJIkE_Q-MR84Mmx6OMm6-DgZ2B2l9AeIZ728mWKVsiqOKvg3Pu0hQiiwX9Wk2IcTzFjGXImF3vKIw3OhRbm8W7MJ74GE17zpwcu0nf0EbJT9qRtxEyXzx-2YLj3AySvyLLj5zIxebvmNm8AZixp8AYVVeXbdar7YJkhPjQMQ28eEDXrsLeThKytz98KCLYHRQNow5bJ-qLw16GYg-4Oi40vc-kWCpQPrf47c0TGaFdB_WrtiL5dq-3EEijl9dLDmAqXXssECw0sUhV-SyLkbiA-t-qLqeNRJMlROo2U1BKOgfpG52VLx9cCdYYXfJPZCyI6JH_1ZHLEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵
نوشیدنی ساده و خوشمزه که می‌تونن حال بدنت رو بهتر کنن
😍
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/679869" target="_blank">📅 09:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679861">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c42b704b33.mp4?token=Op5LnSYb4Ulf3hkj_fWDp32j-QiPdKqanNJrJUQDkKDjql155MC1AkmMMHaRqCzfTQRBAmuhw4hBiaw1u6zoSYlrV4-RMyLA0fsfXsxcCDoOAi1V5VHy6LvEH7oFSbQGL2YRE0tm5XIE0e4vYY2dbtGjMoi422t9p6RIZwz4lVWGrzJVBY4v8RME6xH_5BG0F09IVATWCClUwIs56JW1ZsE-oPw1e993abZSbG5FqBaIAQPNJgbtIHSUa1USf-SyVcuzwblnYNxc8CANDMPrJjZx_u-_UAV_e1aEv8p0N6i-AfpIYp-hNP1gI27zj7CEdbXZBiS3OtRNJo7di5-XvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c42b704b33.mp4?token=Op5LnSYb4Ulf3hkj_fWDp32j-QiPdKqanNJrJUQDkKDjql155MC1AkmMMHaRqCzfTQRBAmuhw4hBiaw1u6zoSYlrV4-RMyLA0fsfXsxcCDoOAi1V5VHy6LvEH7oFSbQGL2YRE0tm5XIE0e4vYY2dbtGjMoi422t9p6RIZwz4lVWGrzJVBY4v8RME6xH_5BG0F09IVATWCClUwIs56JW1ZsE-oPw1e993abZSbG5FqBaIAQPNJgbtIHSUa1USf-SyVcuzwblnYNxc8CANDMPrJjZx_u-_UAV_e1aEv8p0N6i-AfpIYp-hNP1gI27zj7CEdbXZBiS3OtRNJo7di5-XvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کادوپیچی تیشرت با یک کاغذ؛ ایده‌ای ساده اما متفاوت و تماشایی
🎁
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/679861" target="_blank">📅 08:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679859">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
خورشیدگرفتگی کامل در راه است/ روز در کدام نقاط زمین شب می‌شود؟
🔹
چهارشنبه این هفته، برای اولین بار در دو سال اخیر، خورشید گرفتگی کامل در بخش‌هایی از گرینلند، ایسلند، شمال اسپانیا و شمال شرقی پرتغال قابل رویت است و برای دقایقی، با ناپدید شدن کامل خورشید، آسمان برای لحظاتی تاریک می‌شود.
🔹
این خورشیدگرفتگی در بخش‌هایی از اروپا، آفریقا و آمریکای شمالی، به صورت جزئی دیده خواهد شد و در آن تنها بخشی از نور خورشید از دید پنهان می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/679859" target="_blank">📅 08:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679857">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682e4ae741.mp4?token=E0teNFPDEr6rrHiPYrKxXeEYJOvVfUXsIOfsG_vvXeKkFRUwfFOquXbaR91Gq-UmDN0TwwTCkA1XuIjJ6XwAtNvJOq4QPOV5KO2lrKJgvfwcUT7hOHmRYBPa8v19AAxfA9KBE7-RP1YlJg1OcPff0XQmf0thwcfqIA0L0wGp-9t74_YViXAJC2QJszrZx3yqxMfnK1QOcgxxjGITYuDNvE-KktK9hyuKQf-NItLGFZVAdlha7QsDsrUjA8x6MXxfVoqirloX1eOmLY26enSbPavX-OfIacfhXD0msCl26cRi2ISpDooCi9RxGRpb2haLwUbmZBkRKhTAPklxRwGGCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682e4ae741.mp4?token=E0teNFPDEr6rrHiPYrKxXeEYJOvVfUXsIOfsG_vvXeKkFRUwfFOquXbaR91Gq-UmDN0TwwTCkA1XuIjJ6XwAtNvJOq4QPOV5KO2lrKJgvfwcUT7hOHmRYBPa8v19AAxfA9KBE7-RP1YlJg1OcPff0XQmf0thwcfqIA0L0wGp-9t74_YViXAJC2QJszrZx3yqxMfnK1QOcgxxjGITYuDNvE-KktK9hyuKQf-NItLGFZVAdlha7QsDsrUjA8x6MXxfVoqirloX1eOmLY26enSbPavX-OfIacfhXD0msCl26cRi2ISpDooCi9RxGRpb2haLwUbmZBkRKhTAPklxRwGGCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاس گل عجیب بازیکن ایرانی در روسیه چشم‌ها را خیره کرد
🔹
رسانۀ انگلیسی one football با انتشار ویدئوی پاس گل نادر محمدی نوشته: «عجب پشتکی!»؛ محمدی در تیم اسپارتاک کوستروما در دستۀ دوم روسیه بازی می‌کند.
🔹
رسانۀ انگلیسی که در اینستاگرام بیش از ۱۰ میلیون دنبال‌کننده دارد، به تمجید از این حرکت پرداخته و با تعجب نوشته: «او به معنای واقعی کلمه توپ را با یک چرخش از جلو به داخل محوطه جریمه پرتاب می‌کند».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/679857" target="_blank">📅 08:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679856">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90d15cee9.mp4?token=SV5Pgh0Zu-39faHZ4v-aAxmDQ3ulE085P1GfOIL1sVjWlDK5bon1jmdFZWFDrajMKBzGyEVJGjD-QdD8s8AQPHVRurXb4kakofZd76eXBMESvC-VKKCHRhb6UFh-R3KVDNE7prE7FnwncilGQWl6Wc5-jRM8xTgF5LGFDO8bhszapVFbLwMqRH-AKaFCQ0diXizS2R2MsLqYvL3DMZVAMDCFCau7yOuBJD7IaEcwRSnc7buPNVByrW0K7yg6FfbkScZJ5yDhn2xca8XvzvK5T1BB7xRMsC7TfF9oGw3jxiDSQrcqlcu7bsiEcisha-ESEwPOr_fXwdfWE8tYQtPvtR4T2DHlkmeW9d1mfDziMJZp0fBFVkZ6GVdKykwVnMg68_2eF_9lKXsWAf0OvS_Pj-ha5LutKZic9VWK4y9hP21FMpNRfJW1FEz4UAAmBOiNgkc7mEdRw2HDz4aFI1JqwFpi-XAvocTSNfONFx7om_CEYYmFjkVgapAM8vM8ChbLN3rG2AI_U7v5SqQhLNdQEosXIm88xNyow548_UN_bJBM8CFhwEatqcdm6kEf-Q2SBT9czTXFvwpydZV4euF_E_RCZVtqev_ZFK6aQJAehfmzv4SzV-m40RgtjVmA58ttlKRZeEKFJXa1hEk_23mVBlKgwc4gzAMWJekzfySj8RU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90d15cee9.mp4?token=SV5Pgh0Zu-39faHZ4v-aAxmDQ3ulE085P1GfOIL1sVjWlDK5bon1jmdFZWFDrajMKBzGyEVJGjD-QdD8s8AQPHVRurXb4kakofZd76eXBMESvC-VKKCHRhb6UFh-R3KVDNE7prE7FnwncilGQWl6Wc5-jRM8xTgF5LGFDO8bhszapVFbLwMqRH-AKaFCQ0diXizS2R2MsLqYvL3DMZVAMDCFCau7yOuBJD7IaEcwRSnc7buPNVByrW0K7yg6FfbkScZJ5yDhn2xca8XvzvK5T1BB7xRMsC7TfF9oGw3jxiDSQrcqlcu7bsiEcisha-ESEwPOr_fXwdfWE8tYQtPvtR4T2DHlkmeW9d1mfDziMJZp0fBFVkZ6GVdKykwVnMg68_2eF_9lKXsWAf0OvS_Pj-ha5LutKZic9VWK4y9hP21FMpNRfJW1FEz4UAAmBOiNgkc7mEdRw2HDz4aFI1JqwFpi-XAvocTSNfONFx7om_CEYYmFjkVgapAM8vM8ChbLN3rG2AI_U7v5SqQhLNdQEosXIm88xNyow548_UN_bJBM8CFhwEatqcdm6kEf-Q2SBT9czTXFvwpydZV4euF_E_RCZVtqev_ZFK6aQJAehfmzv4SzV-m40RgtjVmA58ttlKRZeEKFJXa1hEk_23mVBlKgwc4gzAMWJekzfySj8RU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ دقیقه تمرینات عضلات پا بدون تجهیزات در خانه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/679856" target="_blank">📅 08:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679852">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i93s7XiZ-PglaExZlzCJDlv8HoNRZ8o10E_QraSesWh5tgFmcPMENKNgFSJPkP67wGfgH-g0ln6MdCIYPPvXWw03EZUrOGmpgO7EuzhZkCktO9E3DPuVx9kzxBA-uMooOJkQPQ-QE_Y-vgTTNk6fDoKWqJ24Q3T6oOeSW58nWRay-ebKPAZeZvhkF7BlxS7aZlCekjNPhsvp_bY2OM6SE1FFOlMz9feY8lVJ_yWBC69clSOULhsXSxHjLcZ7FBv42pXpVYJgbudRLvm4nJKbMCxWbHebNpblGBBBqsk70dWxL1bmz7DrtZLYkedPbS4igdCEckxM7xwzepQGvljcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGkj9agRqoNXf6qWC6ZP1FC-gA-jGiVQP1qaQScEr7cq2zTmfKaRZu9pyw_efl4MzCAalkkcBo_5k9LppuvGesvp6xcoCV1XUWHKY2XfgGGUDHeaF0nzaIOIIV847Z5Msx9ZFJT25vSCJTMjgQ9Gqfkib6gzhqn47kuusi6UzsiRjLQVEdklL_aX7lVZc_De0ZStE1JRrUgv2mIsjbCWLIpxVb4yMAyY8BJoJgUwiBzNay8cosvFdvhtWS6btD3M1jS9by2IyGgHXutYpcZ93E9F2EYtjZvMbolc5_1Xa-Kc0uRDhFfuuhb4bGOrfkUQJiu6QanDDKbADRO-eYjDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcMunhkPZhHQIxlx5j8Aket_Re2VKcv_yIJZLVveU8w94WrYmLwtG7T07fk-BSv0RFxiw8It2pKJLRGDoGOF6H58nATO-mIXU8Iy5ygHQCZtJC--W42ipM-IbccBAfAh2dIm8BGMHVcbNOQ9aTVgofd6TtjcU5Brq693QE4SzW2k2yK-3z9XQ_fECaA99MQBvWXUYsGmYiGJyRn2rW3VsJfGBTAkC-Scmzto-082ibc2CnnKh5uvg4Sub1or5i-hJQJZ8KKqptjo-8lz1TrKM4wDJD42RfGUtiVnXoUy7zf_IBbdob-jiyCcF2EW0RHiUhf6SzYMtfUUl6raslLdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4UIUTGw9Idp6NPXcvRpNcBZkvriXXKa-309yDc4mFvn3kjf084au_d3D10Ey2XpZV3iNNbSrTXw0HUYjtCpGDXqi86yfPkTRqxLog8HdDFWbkbW0uVk2GuLcIUvmijDFkRula_6QWi9CQVrO-fzWU5wrlhHlFf6R4iN4I-BwnNEd3M_HM9IzCI50sG7UGoTYqdLEAgknDIhudUgialuuhcMsyqnkWmrOmFk10KGo_zUW7j1qKkWGfzlJbF8vgySQ_WeaNDlHWTp7Cdp6nWRIBAP9vmFxL4sSpCevgowWNkzbq2GxbscECwsgZc0epMm4D0GEyskE7pSOFjjRHF-EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بلیت پرواز تهران - مشهد از ۱۰ تا ۱۹ میلیون تومان
🔹
قیمت بلیت پروازهای تهران - مشهد در روزهای دوشنبه و سه‌شنبه به صورت یکطرفه در بازه ۱۰ میلیون تومان است و از روز چهارشنبه قیمت‌ها نزولی می‌شود و به پنج میلیون تومان به صورت یکطرفه می‌رسد.
🔹
همچنین قیمت بلیت این مسیر برای پروازهای کلاس پریمیوم اکونومی و  بیزینس نیز از حدود ۱۲ میلیون تومان آغاز شده و تا حدود ۱۹ میلیون تومان نیز ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/679852" target="_blank">📅 07:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679850">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
چین یکی از گسترده‌ترین اقدامات تلافی‌جویانه تجاری علیه آمریکا را آغاز کرد
خبرگزاری CNBC:
🔹
این اقدامات شامل ممنوعیت معامله شرکت‌های چینی با هفت نهاد آمریکایی، تشدید کنترل صادرات پهپادها و فناوری‌های مرتبط به آمریکا، و ممنوعیت همکاری با نهادهای انطباق و گواهی‌دهی آمریکایی است.
🔹
چین همچنین نخستین تحقیق امنیت ملی خود در حوزه تجارت خارجی را علیه تجهیزات چاپ و کپی وارداتی با نرم‌افزار خارجی آغاز کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/679850" target="_blank">📅 07:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679849">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8MKHdg0x4pSCqVXX06S2xkNxbqkMVAaoGnoHP-2_voZkWTldh4tPcRnbAJrygBnQCSUWmn_yllzm90WT95dufIxNIEW80BrmMlm0sJo7r8kifn2y1HJWb9HWSkmFZIp1X-eR3AU4WvO_wxaSkOqkGNBF-JefyydAW7vz5Urc9vgCAhn_aJ41wcEXKegfh6szkdUYjwojbw3zYg_wB2qmUwoNkZ9tyzQbzdeG_WfXaTJ0HbeKbnrZ7TgaURnbm8_0A3YpzaKth4QHIm9jZ3OYGIx5uz1bDRn3zji2_qfpHL6DpZBaNQP4SABBovqNyv36H2kbBArNiTTLRzWW_I0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۱۹ مرداد ماه
۲۶ صفر ‌‌۱۴۴۸
۱۰ آگوست ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/679849" target="_blank">📅 07:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679848">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b634713d8b.mp4?token=ASh81L-mZV7F1y8vLGS42lDvZrqVxO-p1j5Vth5K8FWcR_HRcyoNq2QJBZY4-6YncBuzc9iaf071zZTXRPvUtmSFuxvXx1HrXVawfAVVUnajCJj3_Hw8ztYSBMt3pHq8qtiUKTYrXLmdDLh2pY9Ci6eCDaQG6t2k1vxXoZzDa8FuzgWCSrNiFXT79mjDYxH4dfzlFKvU-b0Rr7N8lt7YQ26NHTR20AGzSvU4wAyP1fsb5bJwLQ6Y1mxrwUy1C4HY-5CgdAvTWQC5_xVhnKyaBV9VPrSkU8KVI_kLVQuWXORyNxBBaaEexv-BWrhO-n3P4WYrPFz6kgnsLOCOrXOMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b634713d8b.mp4?token=ASh81L-mZV7F1y8vLGS42lDvZrqVxO-p1j5Vth5K8FWcR_HRcyoNq2QJBZY4-6YncBuzc9iaf071zZTXRPvUtmSFuxvXx1HrXVawfAVVUnajCJj3_Hw8ztYSBMt3pHq8qtiUKTYrXLmdDLh2pY9Ci6eCDaQG6t2k1vxXoZzDa8FuzgWCSrNiFXT79mjDYxH4dfzlFKvU-b0Rr7N8lt7YQ26NHTR20AGzSvU4wAyP1fsb5bJwLQ6Y1mxrwUy1C4HY-5CgdAvTWQC5_xVhnKyaBV9VPrSkU8KVI_kLVQuWXORyNxBBaaEexv-BWrhO-n3P4WYrPFz6kgnsLOCOrXOMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهپیمایی بزرگی در مونترال کانادا در اعلام همبستگی با غزه و مردم فلسطین در حال برگزاری است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/679848" target="_blank">📅 04:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679846">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a71c940c21.mp4?token=LcXKanvBrI_5deC2oQBVa_LBrC8i5ETu-XAesq2gqfy1BbyY8y980RORXbtfdIcfXFHtLWItKkSLqq-jxtX8EXA9s-xPDv2DIIMEB5dTpez0CAhtfKoeDpYLf50Uzde24nmCQiymhvAa5ugIAjuwLmtrbAMf4QY40AsNkT9B3hn4ZKBtAQxn0OtFh0bXz581Qcn17SE97NrhWNAspIiq2GnGkbrGOqvhcZeqo-Z2RY4vmPeZ0Hibz5AmLkFkZM90Q3kl753x72u4UsZE-l44R5gPRTeCTHkDsMeolBEVcTa7TeVGbO2WcATciAiM7W7nlGg_fplBxm7Nzt5VBBm5f2QN2L9pe8yqNktxJ7L8yx1g-8ZgJ5mu2_j-qptZeT4HOgOl2V95UGnF1UiIlQZXcupIatsDXRsZmubU_ZdFxXIdPi6g8VmbWSsbIB7I6yixuDHdkXsGBGerGngmJpUVbdeHtpzSQPdWrOE4udLutLPyKSifw4iyG3sOJa-exbL5dQqK12jrq-CiwpO-1teOtRrgh_Uxf6trNQocLPhR_6BoWIwv0vR5ndhZSN_wZq-vN6iyHuKR1LmjSNTEDK0Mzj-MzebS_aXu3vYDjd9PXjV9_clhcI9y_gRyKX_VDY2QGVtsiCWZehqdMWo8i-LBIvjw7mh0lrcT0gC9u-QBz18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a71c940c21.mp4?token=LcXKanvBrI_5deC2oQBVa_LBrC8i5ETu-XAesq2gqfy1BbyY8y980RORXbtfdIcfXFHtLWItKkSLqq-jxtX8EXA9s-xPDv2DIIMEB5dTpez0CAhtfKoeDpYLf50Uzde24nmCQiymhvAa5ugIAjuwLmtrbAMf4QY40AsNkT9B3hn4ZKBtAQxn0OtFh0bXz581Qcn17SE97NrhWNAspIiq2GnGkbrGOqvhcZeqo-Z2RY4vmPeZ0Hibz5AmLkFkZM90Q3kl753x72u4UsZE-l44R5gPRTeCTHkDsMeolBEVcTa7TeVGbO2WcATciAiM7W7nlGg_fplBxm7Nzt5VBBm5f2QN2L9pe8yqNktxJ7L8yx1g-8ZgJ5mu2_j-qptZeT4HOgOl2V95UGnF1UiIlQZXcupIatsDXRsZmubU_ZdFxXIdPi6g8VmbWSsbIB7I6yixuDHdkXsGBGerGngmJpUVbdeHtpzSQPdWrOE4udLutLPyKSifw4iyG3sOJa-exbL5dQqK12jrq-CiwpO-1teOtRrgh_Uxf6trNQocLPhR_6BoWIwv0vR5ndhZSN_wZq-vN6iyHuKR1LmjSNTEDK0Mzj-MzebS_aXu3vYDjd9PXjV9_clhcI9y_gRyKX_VDY2QGVtsiCWZehqdMWo8i-LBIvjw7mh0lrcT0gC9u-QBz18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات گسترده در سئوتا؛ معترضان در اعتراض به مدیریت دولت در بحران مهاجرتی اخیر، خواستار استعفای دولت مادرید شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/679846" target="_blank">📅 03:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679845">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: از آغاز عملیات «خشم حماسی»، ایران بیش از ۲هزار حمله هوایی، موشکی و پهپادی به پایگاه‌های آمریکا انجام داده و به ۲۰ سایت در ۸ کشور آسیب زده
🔹
خسارت وارده به تجهیزات و تأسیسات آمریکا ۱۳ میلیارد دلار و ۴۲ هواپیما منهدم یا آسیب دیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/679845" target="_blank">📅 03:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679843">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqOwy7XGurEy1ZQhHv9QrFaxxSyAgu5M3VsRQq4FVLn8bS-YQEYvebIYAL-M25Mdrc-O4Yn1q1NuaWlxtCESfvWVJ9E-_EBIpDIVI50LwmJ3y06BOdvWx-LhGRHoXqairvC9pYjif6WwTu2yk7RgHqRfwxIDLhKkTY2980Y52ymnvrPracLMjkbKia9jz51ddpx1Bioq5JZT8eGSTN3SgvImcINncXsKqpZKzFkjY3-a9r4BT4jjmiiUoRiGyJ2Bc0xi2tTe-dyRjBiiRMcC3s-pvR-WKO7cjOBxdhxmjxOafMopmbsd00VhQLFMOjJj94GaXO8Mtpe8dYLAKbp2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای یمنی:
امیدوارم توافق دفاعی مشترک، شامل کمک به سعودی برای خاموش کردن آتش‌سوزی‌ها هم باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/679843" target="_blank">📅 02:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679841">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
برای آزمایش بمب جان ۱۵۰ هزار نفر [توسط آمریکا] در وهله‌ی اول از بین میره...
🔹
به مناسبت جنایت آمریکا در هیروشیما و ناگازاکی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/679841" target="_blank">📅 02:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679839">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
افزایش قیمت نفت: ۸۴.۸۳ دلار/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/679839" target="_blank">📅 02:00 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
