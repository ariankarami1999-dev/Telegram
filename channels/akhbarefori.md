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
<img src="https://cdn4.telesco.pe/file/WaIisjjQRvtJP1DajXDstszTfTRPLKR4X8fQf9fJ5EnPMvBY97-C01z0C0_7slXrTk5fAmPmlzff651eV_Rqikq0CPN4umyDoRlxKU0mujeJrTN16nisPHESGFUIWArJzqtoMhDaUpvL8iIxxxmIcIVjwj6jKDHsBHgug0rD8-C90saEmHAEVoRNVrLrlhRISXPwoxR6CcnujSdQcGf6sMkNcZSJdqXm-fGCHB2VMANqHb8wdnlXg6MLJXGSiuZdtoMoA1T3jf20-4SFa7rj9LGKXH4Py9A-os4xiJPr92bSm2izwv4l6-u-jcYj8z2ue8JJjNBwDXnJxEF5v0-Eyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.6M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 06:07:11</div>
<hr>

<div class="tg-post" id="msg-657891">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">در پی سومین موج حملات ایران به پایگاه‌های آمریکا در کوبت، ستاد کل ارتش این کشور از تلاش سامانه‌های پدافندی برای مقابله با موشک‌ها و پهپادهای ایرانی خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/akhbarefori/657891" target="_blank">📅 06:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657890">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هشدار عراقچی به آمریکا: منطقه را ترک کنید تا در امان بمانید
🔹
وزیر خارجه ایران در واکنش به نقض آتش‌بس از سوی آمریکا که با پاسخ قاطع ایران مواجه شد، به واشنگتن هشدار داد که اگر می‌خواهد در امان باشد، منطقه را ترک کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/akhbarefori/657890" target="_blank">📅 06:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657889">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ادعای ستاد کل ارتش کویت: سامانه‌های پدافند هوایی کویت در حال حاضر در حال درگیری با اهداف هوایی متخاصم هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/akhbarefori/657889" target="_blank">📅 05:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657888">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcc150c12.mp4?token=jUf7-kj5QF6eRm7jdo9RdBKn26ZOvFKQ31gSn98R630R14pBFsp4SaCmWegvKluiwuRzpF-_nWBHrKjYSW9WVJS4ZR3A_q7k87nxiKsOtuMhaWYhlBno8sSnsDOV6QqVpaXmHGHt7jY28XYgqp20FhsyEsNFzACvAJa-JgMXpGrkdJFMN3K3YpMDFBa7izKgQgHCNi2VVyFibm97xka81VCoG-kH_LkUcBb068OWNMZsgPOUXsA2qX2HYS7yKIqN5cVnRLGV0QzWbqWUJhIqgf4xl2Hl-VAo6c2LkjlgVNrVWoVVLZQcgRGceYVEYDX3iz7mBPba4N2yh03f6qk5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcc150c12.mp4?token=jUf7-kj5QF6eRm7jdo9RdBKn26ZOvFKQ31gSn98R630R14pBFsp4SaCmWegvKluiwuRzpF-_nWBHrKjYSW9WVJS4ZR3A_q7k87nxiKsOtuMhaWYhlBno8sSnsDOV6QqVpaXmHGHt7jY28XYgqp20FhsyEsNFzACvAJa-JgMXpGrkdJFMN3K3YpMDFBa7izKgQgHCNi2VVyFibm97xka81VCoG-kH_LkUcBb068OWNMZsgPOUXsA2qX2HYS7yKIqN5cVnRLGV0QzWbqWUJhIqgf4xl2Hl-VAo6c2LkjlgVNrVWoVVLZQcgRGceYVEYDX3iz7mBPba4N2yh03f6qk5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رد موشک‌های ایران در آسمان اَمّان، پایتخت اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/akhbarefori/657888" target="_blank">📅 05:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657887">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">موج جدید انفجارها در کویت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/akhbarefori/657887" target="_blank">📅 05:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657886">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک‌ منبع آگاه نظامی: ایران با استفاده از موشک‌های دوربرد سوخت جامد خیبرشکن، آشیانۀ جنگنده‌های اف۳۵ آمریکا در اردن را هدف قرار داده است/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/akhbarefori/657886" target="_blank">📅 05:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657885">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بسم الله قاصم الجبارین قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ  سپاه پاسداران انقلاب اسلامی:
🔹
رژیم جنگ افروز آمریکا در اوایل بامداد امروز با بهانه های واهی چند نقطه در جاسک،…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/657885" target="_blank">📅 05:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657884">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تلاش سامانه‌های پدافندی آمریکایی در پایگاه الازرق اردن برای مقابله با موشک‌های ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/akhbarefori/657884" target="_blank">📅 05:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657882">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ثبت لحظه انفجار و اصابت موشک به محل استقرار ناوگان پنجم نیروی دریایی آمریکا در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/akhbarefori/657882" target="_blank">📅 05:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657881">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آژیر هشدار در پایگاه آمریکایی‌ها در اردن
🔹
رسانه‌های عربی می‌گویند که موشک‌های شلیک‌شده توسط ایران، پایگاه «الازرق» محل استقرار نظامیان آمریکا در اردن را هدف قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/akhbarefori/657881" target="_blank">📅 05:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657880">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4aee3aed.mp4?token=PIJLSet3qAiXeYS2LuX1vkJT2wQaHJdgJ-JwMr8whP6GsN12UEGISZSyrELXiacNKFE6xZEas2CNuSHd1AeBadBusUAUhdmaGlEJ6eOpw-Mu0QesgoUYp32e7ns9GSeYE59aivooL1wiUbvB5RpiHbB3TVnQZ4w7qb6-p-la9V5kO_XqRcsIO6oA6slFT7OeMyrimDlUTfN4_ECSDPX6PPUD0yFfkODjFKcCWqbC01RrdFbiYJx1mOrFNoSKrutS9yZtzBk6P0GmLxWT5i9Sglcxjkd_tk6fWc2yOiwIV6WopSGEnBTaosO5FAn4u9p8OOmBqQgeZhM4iiad0t7wxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4aee3aed.mp4?token=PIJLSet3qAiXeYS2LuX1vkJT2wQaHJdgJ-JwMr8whP6GsN12UEGISZSyrELXiacNKFE6xZEas2CNuSHd1AeBadBusUAUhdmaGlEJ6eOpw-Mu0QesgoUYp32e7ns9GSeYE59aivooL1wiUbvB5RpiHbB3TVnQZ4w7qb6-p-la9V5kO_XqRcsIO6oA6slFT7OeMyrimDlUTfN4_ECSDPX6PPUD0yFfkODjFKcCWqbC01RrdFbiYJx1mOrFNoSKrutS9yZtzBk6P0GmLxWT5i9Sglcxjkd_tk6fWc2yOiwIV6WopSGEnBTaosO5FAn4u9p8OOmBqQgeZhM4iiad0t7wxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاربران شبکه‌های اجتماعی تصاویری منتسب به اصابت موشک‌های ایرانی به مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین منتشر کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/akhbarefori/657880" target="_blank">📅 05:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657879">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
سپاه پاسداران دقایقی قبل پایگاه آمریکایی الازرق در اردن را هدف حملۀ موشکی قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/akhbarefori/657879" target="_blank">📅 05:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657878">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
وزارت کشور بحرین: در پی به‌صدا درآمدن آژیر خطر، مردم فورا به نزدیکترین مکان امن بروند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/akhbarefori/657878" target="_blank">📅 05:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657877">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6EGfMIz50pxFW6uVC8MqqijovPIWnYyxzbTGstFdBlF_aXHPYw3URPVXSTKMuQg6VtuPKGKXEn3E4BsL4nAPMTqmf_FawDPpRfzfb6KhiiuO9ZCSVHQfGz0lR9okpmjh3oqW0aM3J4nfp4hRyyBTifbwbolJaF2ZdhCSJelG5CXVxr2Mek_m5kC5B8u4HjFEeKOQO712b5ADwY5mFiaCn0l3AtQmkIbN8wCtD2klE0f7zA-Ji4GedOtcZmhIbf4rQJDk7689efmnjwaMyXdGfGDm3KrEC2sgqy10jKEFBtTXuQH0N8U91Onu5xaG0ITQKTWQXsZ2Zh_XgFzRatRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاهده چندین ابر دود در آسمان بحرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/akhbarefori/657877" target="_blank">📅 05:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657876">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
صدای انفجار در کویت
🔹
منابع خبری از شنیده شدن صدای انفجار در کویت و به صدا در آمدن آژیرهای هشدار خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/657876" target="_blank">📅 05:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657875">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
انفجارها در بحرین قطع نمی‌شود
🔹
منابع محلی در بحرین می‌گویند تاکنون صدای ۱۶ انفجار را شنیده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/akhbarefori/657875" target="_blank">📅 05:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657874">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تکمیلی/ انفجارهای متعدد در کویت و بحرین
🔹
منابع محلی می‌گویند که انفجارهایی کویت را لرزاند اما آژیرهای هشدار فعال نشدند.
🔹
گزارش‌ها همچنین حاکی از آن است که انفجارهای متعدد در بحرین همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/akhbarefori/657874" target="_blank">📅 05:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657873">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
صدای انفجار در کویت
🔹
منابع خبری از شنیده شدن صدای انفجار در کویت و به صدا در آمدن آژیرهای هشدار خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/657873" target="_blank">📅 05:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657872">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
آژیرهای هشدار در بحرین به صدا در آمد
🔹
منابع عربی از شنیده شدن صدای چندین انفجار شدید در بحرین در پی حمله موشکی ایران خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/657872" target="_blank">📅 05:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657871">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای سنتکام: حملات ما به پایان رسید
🔹
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در واکنش به سرنگونی هلیکوپتر آپاچی ارتش ایالات متحده در روز 9 ژوئن، حملات دفاعی خود علیه ایران را به دستور فرمانده کل ارتش تکمیل کردند.
🔹
نیروهای سنتکام با مهمات دقیق نیروی…</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/akhbarefori/657871" target="_blank">📅 04:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657870">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بسم الله قاصم الجبارین قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ  سپاه پاسداران انقلاب اسلامی:
🔹
رژیم جنگ افروز آمریکا در اوایل بامداد امروز با بهانه های واهی چند نقطه در جاسک،…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/657870" target="_blank">📅 04:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657869">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
صدای انفجار از شمال غرب اهواز شنیده شد/
صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/657869" target="_blank">📅 04:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657868">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای سنتکام: حملات ما به پایان رسید
🔹
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در واکنش به سرنگونی هلیکوپتر آپاچی ارتش ایالات متحده در روز 9 ژوئن، حملات دفاعی خود علیه ایران را به دستور فرمانده کل ارتش تکمیل کردند.
🔹
نیروهای سنتکام با مهمات دقیق نیروی هوایی و جت های جنگنده نیروی دریایی ایالات متحده، پدافند هوایی، ایستگاه های کنترل زمینی و سایت های رادار نظارتی در نزدیکی تنگه هرمز را مورد حمله قرار دادند. این عملیات پاسخی متناسب به حملات اخیر به نیروهای آمریکایی و کشتی‌های تجاری بین‌المللی بود که از آب‌های منطقه عبور می‌کردند.
🔹
نیروهای آمریکایی هوشیار و آماده دفاع در برابر تهاجم غیرموجه ایران هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/657868" target="_blank">📅 04:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657867">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
یک فروند پهپاد MQ9 رهگیری و منهدم شد
روابط عمومی سپاه:
🔹
در جریان درگیری های هوایی جاری در تنگه هرمز یک فروند پهباد MQ9 که از آسمان شمال خلیج فارس قصد نزدیک شدن و مداخله در صحنه نبرد را داشت، در آسمان شهرستان جم استان بوشهر مورد اصابت آتش  رزمندگان قهرمان پدافند هوایی نوین سپاه قرار گرفت و منهدم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/657867" target="_blank">📅 04:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657866">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
صداوسیما با تایید ۲ انفجار در بندر عباس: هنوز دربارهٔ محل دقیق انفجارها و جزئیات اصابت‌های احتمالی، اطلاعات دقیقی در دسترس نیست و بررسی‌های مسئولان مربوطه ادامه دارد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/657866" target="_blank">📅 04:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657865">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
سپاه پاسداران انقلاب اسلامی:
🔹
رژیم جنگ افروز آمریکا در اوایل بامداد امروز با بهانه های واهی چند نقطه در جاسک، سیریک و قشم را مورد حمله قرار داد که به یک دکل مخابراتی در سیریک خساراتی وارد آمد و دو مخزن آب بخش بمانی این شهرستان  منهدم شد.
🔹
در پاسخ به این حرکت شرارت آمیز دشمن، رزمندگان نیروی دریایی سپاه ساعت ۲.۳۰ دقیقه بامداد
ناوگان پنجم دریایی بحرین را مورد حمله پهپادی
قرار دادند.
🔹
درگیری‌ها ادامه دارد و پاسداران غیور ملت ایران در حال پاسخگویی به تجاوزهای دشمن هستند و در صورت ادامه شرارت، پاسخ‌های سنگین‌تری در راه است
و ماالنصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/657865" target="_blank">📅 04:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657864">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
صدای انفجار در اهواز شنیده شد
🔹
منابع محلی از شنیده شدن صدائی شبیه به انفجار در اهواز خبر می‌دهند.
🔹
هنوز جزییاتی از علت و مکان دقیق این حادثه یا احتمال تلفات جانی منتشر نشده است و پیگیری‌ها برای روشن شدن ابعاد ماجرا ادامه دارد./ مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/657864" target="_blank">📅 04:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657863">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در قشم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/657863" target="_blank">📅 04:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657862">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
المیادین حمله آمریکا به ایران را بی دلیل و غیرموجه خواند
المیادین انگلیسی:
🔹
ایران ادعاها مبنی بر اینکه نیروهایش یک بالگرد آپاچی آمریکایی را سرنگون کرده‌اند رد کرد؛ این در حالی است که فرماندهی مرکزی آمریکا (سنتکام) اعلام کرده بود پس از آنکه جمهوری اسلامی ظاهراً یکی از هواگردهایش را سرنگون کرده، در حال انجام حملات هوایی علیه ایران است.
🔹
ایران اعلام کرد در ۲۴ ساعت گذشته هیچ عملیاتی در تنگه هرمز انجام نداده است؛ موضوعی که نشان می‌دهد حمله آمریکا بار دیگر بی‌دلیل و غیرموجه بوده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/657862" target="_blank">📅 04:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657861">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
کانون صداهایی که حدود نیم ساعت پیش در بندرعباس شنیده شد، غرب این شهر بود اما هنوز دربارهٔ محل دقیق انفجارها و جزئیات اصابت‌های احتمالی، اطلاعات دقیقی در دسترس نیست و بررسی‌های مسئولان مربوطه ادامه دارد/ صداوسیما
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/657861" target="_blank">📅 04:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657860">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c08e8a50.mp4?token=MeMD667Cc890v2tQdGS5kpYffMN4XBhyNmemSN9leyAK4iHpCHM3i7vXvRNVXHZ0veQ6NsNhiy7A2CzccRsH9J72FUYd5IMJg8skoPlKcqeDXw1rM7IekK31VO_5MYVgrmQPTLhF7_kQoq0JPO8EsRKVfaD77bM8Sn--2u1gkgcGpkU5YjPLJr71kxkjECHuJtX_4_YF0R732I-ZoGpF5-YcyNtQC9zCAImUfGE0IJ2FikuZ8yAahf7KnD33XYWFhtfqgg4r-R8f8j6l3cNKsK3fBFM2Ncbm-FQlv_KJ3wVX2jfI1llmbOFlGj4xw27ojcqW-V2iy4xGwqbJFW9x-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c08e8a50.mp4?token=MeMD667Cc890v2tQdGS5kpYffMN4XBhyNmemSN9leyAK4iHpCHM3i7vXvRNVXHZ0veQ6NsNhiy7A2CzccRsH9J72FUYd5IMJg8skoPlKcqeDXw1rM7IekK31VO_5MYVgrmQPTLhF7_kQoq0JPO8EsRKVfaD77bM8Sn--2u1gkgcGpkU5YjPLJr71kxkjECHuJtX_4_YF0R732I-ZoGpF5-YcyNtQC9zCAImUfGE0IJ2FikuZ8yAahf7KnD33XYWFhtfqgg4r-R8f8j6l3cNKsK3fBFM2Ncbm-FQlv_KJ3wVX2jfI1llmbOFlGj4xw27ojcqW-V2iy4xGwqbJFW9x-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشات اولیه از انهدام یک شیء بر فراز آسمان بوشهر  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/657860" target="_blank">📅 03:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657859">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
صدای انفجار در قشم شنیده شد
🔹
این صدای انفجار برای چندمین بار است، که در جزیره قشم شنیده می شود. پیش از این نیز صدای انفجار در بندرعباس، سیریک و جاسک شنیده شده بود
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/657859" target="_blank">📅 03:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657858">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
جزئیات حمله آمریکا به زیرساخت‌های آبی سیریک
حمزه پور مدیرعامل شرکت آبفا هرمزگان:
🔹
نیروهای آمریکایی به زیرساخت‌های حیاتی توزیع آب در شهرستان سیریک حمله کردند.
🔹
در پی این حمله موشکی که ساعاتی پیش به وقوع پیوست، دو مخزن استراتژیک آب در بخش بمانی هدف قرار گرفته و به طور کامل تخریب شدند.
🔹
این مخازن شامل یک مخزن ۵۰۰ متر مکعبی و یک مخزن ۲ هزار متر مکعبی بوده‌اند که نقش کلیدی در تأمین آب شرب بخش بمانی و شهر کوهستک ایفا می‌کردند.
🔹
در حال حاضر روند توزیع آب در تمامی روستاهای بخش بمانی و شهر کوهستک متوقف شده است و تیم‌های عملیاتی و مدیریت بحران آبفا در تلاش هستند تا اقدامات جایگزین برای تامین آب پایدار انجام شود./مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/657858" target="_blank">📅 03:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657857">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
گزارشات اولیه از انهدام یک شیء بر فراز آسمان بوشهر
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/657857" target="_blank">📅 03:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657856">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از مقام آمریکایی: دور سوم حمله آمریکا به ایران درحال انجام است/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/657856" target="_blank">📅 03:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657855">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شنیده شدن مجدد صدای انفجار در سیریک
‌
🔹
دقایقی پیش صدای انفجاری مجدد در محدوده شهرستان سیریک  از سوی منابع محلی و ساکنان روستاهای اطراف گزارش شده است.
🔹
بررسی‌ها نشان می‌دهد، این حمله مربوط به نوار ساحلی این شهرستان بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/657855" target="_blank">📅 03:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657854">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
صدای انفجار در بندرعباس و قشم شنیده شد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/657854" target="_blank">📅 03:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657853">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
صدای چندین انفجار در بندرعباس شنیده شده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/657853" target="_blank">📅 03:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657852">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
گشت دریایی P-8A آمریکا که از بحرین برخاسته، همچنان در جریان حملات به ایران بر فراز عربستان در حال عملیات است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/657852" target="_blank">📅 03:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657851">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
منابع خبری عراقی: مشاهده جنگنده های آمریکایی در تعداد بالا درحال پرواز در آسمان عراق در نزدیک خط مرزی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/657851" target="_blank">📅 03:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657850">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
گزارش ها از ادامه انفجار ها در بندرعباس خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/657850" target="_blank">📅 03:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657849">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
فاکس نیوز به نقل از یک مقام آمریکایی مدعی ادامه حملات آمریکا به برخی مناطق جنوبی ایران شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/657849" target="_blank">📅 03:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657846">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b372cea86a.mp4?token=r94pPkQJsGYe4WbYyKWs7Tmr-9PA4plIqpCS-8iYdXvNgHOU2x8HxAI9ghGwvxa4EHj0vF53L_Vl1a1mVwFa87X9USyl3W2gey5iUbxtSd8V82CXO9QcIxDrdMb58ZEDk0CaWbGvuha3RxbZGWxHdvVjzthLtCyx3Mzepmi9QnyVYAe_a8cKkdSYXyW-EpK1rgkneeLjzvLIUNOnkOvARuJCx7i-X5CMPqB9Et1fdrAdCcx-rd6cQmPD0DS_pp6W5jQrYcLNaXZCmI0xJGTr60NUN6brgiPgCrzawP9J6O0Waju552MVgXuJY1PsUNSWqVICzCO0yRI_a9hZLc_XwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b372cea86a.mp4?token=r94pPkQJsGYe4WbYyKWs7Tmr-9PA4plIqpCS-8iYdXvNgHOU2x8HxAI9ghGwvxa4EHj0vF53L_Vl1a1mVwFa87X9USyl3W2gey5iUbxtSd8V82CXO9QcIxDrdMb58ZEDk0CaWbGvuha3RxbZGWxHdvVjzthLtCyx3Mzepmi9QnyVYAe_a8cKkdSYXyW-EpK1rgkneeLjzvLIUNOnkOvARuJCx7i-X5CMPqB9Et1fdrAdCcx-rd6cQmPD0DS_pp6W5jQrYcLNaXZCmI0xJGTr60NUN6brgiPgCrzawP9J6O0Waju552MVgXuJY1PsUNSWqVICzCO0yRI_a9hZLc_XwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ، عصر دیروز، درباره هو شدنش توسط هزاران آمریکایی در محل برگزاری فینال لیگ بسکتبال، گفته بود «فکر می‌کنم بیشتر تشویقم کردند» اما این ویدیوها چیز دیگری نشان می‌دهد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/657846" target="_blank">📅 03:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657845">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای اکسیوس: یک مقام آمریکایی می‌گوید دور دوم حملات در ایران در حال انجام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/657845" target="_blank">📅 02:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657844">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای اکسیوس: یک مقام آمریکایی می‌گوید دور دوم حملات در ایران در حال انجام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/657844" target="_blank">📅 02:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657843">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
شنیده شدن مجدد صدای انفجار در شهرستان جاسک
🔹
دقایقی پیش، صدای انفجارهایی مجدد در محدوده شهرستان جاسک از سوی منابع محلی و ساکنان و روستاهای اطراف گزارش شده است.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/657843" target="_blank">📅 02:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657842">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
شنیده شدن مجدد صدای انفجار در شهرستان جاسک
🔹
دقایقی پیش، صدای انفجارهایی مجدد در محدوده شهرستان جاسک از سوی منابع محلی و ساکنان و روستاهای اطراف گزارش شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/657842" target="_blank">📅 02:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657841">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f35de44f.mp4?token=CY9y_GJwQ9FSab952NV9dwoMANmgdXKl1aWB2woGu4k4yc8VMAwxF4O4NZFUj5FmGdHmAuEedENw4erJl4sfjjoo1VtFqiu9DDF53hD_eByBzVHeoVSamRZEU34PQoTlu_EX1Uzy4YWzuTKvYm6J3t3cAXYtserGrlC5LS4hCiH-su6l-p1L69e9lPWLNJdsEV6fRXugV6LX1QIxl5_jsfLSsOWsR37dnRm-9EBYRlFYh8i5memwk7MgVh9bDGPRfATU-j_paSmdKgtGlIa_hJYctvN6qaIFUfmxCXuhfb6OOwcnOGsRKzLslZyIIrxrHhrew-9zosRL7CbjMgKN_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f35de44f.mp4?token=CY9y_GJwQ9FSab952NV9dwoMANmgdXKl1aWB2woGu4k4yc8VMAwxF4O4NZFUj5FmGdHmAuEedENw4erJl4sfjjoo1VtFqiu9DDF53hD_eByBzVHeoVSamRZEU34PQoTlu_EX1Uzy4YWzuTKvYm6J3t3cAXYtserGrlC5LS4hCiH-su6l-p1L69e9lPWLNJdsEV6fRXugV6LX1QIxl5_jsfLSsOWsR37dnRm-9EBYRlFYh8i5memwk7MgVh9bDGPRfATU-j_paSmdKgtGlIa_hJYctvN6qaIFUfmxCXuhfb6OOwcnOGsRKzLslZyIIrxrHhrew-9zosRL7CbjMgKN_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع سه انفجار در خط لوله گاز در منطقه داغستان روسیه
🔹
وزارت امور اضطراری منطقه‌ای روسیه گزارش داد که سه انفجار در یک خط لوله گاز در شهر کیزیلیورت در منطقه داغستان روسیه در قفقاز شمالی رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/657841" target="_blank">📅 02:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657840">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
نماینده پاکستان: شکست دیپلماسی، مأموریت حیاتی راستی‌آزمایی آژانس بین‌المللی انرژی اتمی در پرونده هسته‌ای ایران را مختل ساخته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/657840" target="_blank">📅 02:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657839">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
گروه هکری حنظله: مختصات تمام نیروهای نظامی تروریستی آمریکا در کشورهای خلیج‌فارس به سپاه پاسداران انقلاب اسلامی منتقل شد
🔹
به‌زودی به پهپادهای شاهد-۱۳۶ «خوش‌آمد» خواهید گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/657839" target="_blank">📅 02:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657838">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
آماج‌نیوز افغانستان: لحظات پیش جنگنده‌های پاکستانی اهدافی را در ولایت‌های خوست، پکتیکا و کنر بمباران کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/657838" target="_blank">📅 02:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657837">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df42fc015a.mp4?token=Sx3x6WQtwWQHVLpxbYUu5roLcm_hPPD2_7GFzg0DJ3T0wftl5wSJnqckZ9ulGCiFzd8RiLaFZNNnOwlRpVr5MO45Hejn8E4V34YFQ3TsxnzrLZBNUmbo2HMqQgUstt4WnQWYbMLp-zJi88Ua-UJGQtopTh0AN5I12vD7NMu5A3kyFV8emre1ij3HSpcqcRim1eoDdOHssspzZkKPGra0ZTCqDwdEf8RpaE8I0vhB-iu9kqIeD9ePFONFipz83VcixXETON0MNXo-A5XJzrZ3jGtxG_roE-xXauEq0wuDneTUfmYIIy5qwKwiAO8tMxfUcVQj8E6AZprXilThf2M7vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df42fc015a.mp4?token=Sx3x6WQtwWQHVLpxbYUu5roLcm_hPPD2_7GFzg0DJ3T0wftl5wSJnqckZ9ulGCiFzd8RiLaFZNNnOwlRpVr5MO45Hejn8E4V34YFQ3TsxnzrLZBNUmbo2HMqQgUstt4WnQWYbMLp-zJi88Ua-UJGQtopTh0AN5I12vD7NMu5A3kyFV8emre1ij3HSpcqcRim1eoDdOHssspzZkKPGra0ZTCqDwdEf8RpaE8I0vhB-iu9kqIeD9ePFONFipz83VcixXETON0MNXo-A5XJzrZ3jGtxG_roE-xXauEq0wuDneTUfmYIIy5qwKwiAO8tMxfUcVQj8E6AZprXilThf2M7vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش تحلیلگر فاکس‌نیوز به ادعای تکراری ترامپ مبنی بر «نزدیک شدن به توافق» با ایران، همزمان با ادامه تجاوزات آمریکا: اگر فردا بشنویم که به توافق با ایران نزدیک‌تر شده‌ایم و تقریباً به آن رسیده‌ایم، فکر می‌کنم کمی پذیرفتنش سخت باشد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/657837" target="_blank">📅 02:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657834">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
حمله تروریستی آمریکا به  دو مخزن آب در سیریک
‌
🔹
در پی حمله امشب دشمن آمریکایی به سیریک، ۲ مخزن آب بخش بمانی مورد اصابت قرار گرفته و آب آشامیدنی این بخش قطع شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/657834" target="_blank">📅 02:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657833">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
هیچ بندر تجاری در جزیره قشم هدف پرتابه های دشمن قرار نگرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/657833" target="_blank">📅 02:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657832">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPnSv5ULXpCexjwndxBmH8UmspxWk9tWfcjeI9vEcDAOf_FX-eWoLb6Y4WXkaX9_BO9NTflf3nZ21NYx_4wEuCJBybT7fWb1rD3Lf4hw4sCc-tvZcl7DiBYWbPmxDn2tBVTlP0RHfPLkCtm5tKIfk_Qeue1XNFjm3nFUBa7oI8wKn3G95VchlD04-iBrGydF6pQTFc1NFP6ugkoUPFMbMtWLHAAnpZJWZJ9205UnrltBLWyt3q80VYZbXgijZRoqCV8CJ5zexhVRxkXhi00jw5vevBrdpJa4F7jo4lIm2z8XoCLawdVGzNx0danqnLGv63hbZOthnGwI_iUWkM_V7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: آمریکا با وجود شکست‌هایش در میدان نبرد، تصمیم گرفت اراده ما را بیازماید
🔹
نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نخواهند گذاشت.
🔹
اگر خواهان امنیت هستید، منطقه ما را ترک کنید.
🔹
تاریخ خلیج فارس فصل‌های زیادی درباره سرنوشت شوم بیگانگان…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/657832" target="_blank">📅 02:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657831">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
عراقچی: آمریکا با وجود شکست‌هایش در میدان نبرد، تصمیم گرفت اراده ما را بیازماید
🔹
نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نخواهند گذاشت.
🔹
اگر خواهان امنیت هستید، منطقه ما را ترک کنید.
🔹
تاریخ خلیج فارس فصل‌های زیادی درباره سرنوشت شوم بیگانگان متجاوز دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/657831" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657830">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
پولیتیکو: یک مقام ارشد کاخ سفید ادعا کرد که دونالد ترامپ همچنان معتقد است توافق صلح با ایران نزدیک است، حتی در حالی که ایالات متحده امشب حملات تلافی‌جویانه‌ای علیه ایران انجام داد
🔹
هیچ چیز وضعیت کنونی توافق را تغییر نمی‌دهد.
🔹
این مقام تأکید کرد که توافق با تهران «هنوز نزدیک است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/657830" target="_blank">📅 01:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657829">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMZmPGuDpUTVUoO4DjYSO_DlIcRnGBKyhY7ruUnvSM2FyLzVJwBHkmeW_D6-yb-2kkR9zYSbkIZsD-QZ5q8-wadMfMEVZAfKrUlg_DJwkzFf5KEabU_E-sPmLwmfQthPX3nC_DHqtAdD6re2vcHibG58Ekq9qF-qOqvFE-2n6EDnWB45SnSNjwutU_fWTMEPpfY3NgKTTRS2M4FyvlfP8yT0M-5U2gEjhOQt9bW0pjzPguX_SQLiVmkZp2qZF0a25EL1lMEMe3mQLXEeLhCvuhJCn1I0aTr9k43FTSLT6WGQE9_3a2oWPs8aFrwk8OU2yckpTXNjQGWRXs2OzRz48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم اکنون، آسمان منطقه و وضعیت پروازها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/657829" target="_blank">📅 01:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657828">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
موج حملات آمریکایی ها در جنوب فروکش کرده است و بعد از اقدامات خصمانه در قشم، سیریک و جاسک و کوه مبارکه جاسک، هم اکنون وضعیت آرام گزارش می شود/مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/657828" target="_blank">📅 01:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657827">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
نامۀ عراقچی به شورای حکام درباره پیش‌نویس قطعنامۀ ضد ایرانی
🔹
وزیر امور خارجۀ ایران در نامه‌ای به اعضای شورای حکام، پیش‌نویس قطعنامۀ ارائه‌ شده از سوی آمریکا و ۳ کشور اروپایی را اقدامی سیاسی و از روی بدنیتی خواند و از اعضا خواست اجازه ندهند آژانس بار دیگر به ابزار سیاسی آمریکا تبدیل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/657827" target="_blank">📅 01:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657826">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960b224ee4.mp4?token=MK8sFAuDINroiIbsiYScW9pSLvUycU0q0wWIRH3uesxCRwyWYTSNSjgFOnkEZebNC9l9HyyhLmm4qhL7Ikjr0h5B6Wv7hTNaubk2yZmiusbUn8CO6OFEjU9gUNJCh3qe1tgC08YWE1j2bOO0mStqpUABtkmCM2cqETvxdPrtRa9nkzqH0LVH754B8DbqpyT-Jy6dRe2ylL70J0c0PHZ7Ij0Lw_y5n_vFbUAANB2PYr9q9ZNgqWQ0KjTGqJk8mHBuF7VUnPU9ikD6pASAvKkDJdNOlC8NZz4WnJrNrSwGLAXEjORM9JeJhKaMXjxqy_lUiUWxYNFme-W-1vg1-iCTfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960b224ee4.mp4?token=MK8sFAuDINroiIbsiYScW9pSLvUycU0q0wWIRH3uesxCRwyWYTSNSjgFOnkEZebNC9l9HyyhLmm4qhL7Ikjr0h5B6Wv7hTNaubk2yZmiusbUn8CO6OFEjU9gUNJCh3qe1tgC08YWE1j2bOO0mStqpUABtkmCM2cqETvxdPrtRa9nkzqH0LVH754B8DbqpyT-Jy6dRe2ylL70J0c0PHZ7Ij0Lw_y5n_vFbUAANB2PYr9q9ZNgqWQ0KjTGqJk8mHBuF7VUnPU9ikD6pASAvKkDJdNOlC8NZz4WnJrNrSwGLAXEjORM9JeJhKaMXjxqy_lUiUWxYNFme-W-1vg1-iCTfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عراقی تصاویری از یک پرواز شاهد در آسمان این کشور منتشر کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/657826" target="_blank">📅 01:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657825">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
خبرنگار اکسیوس به نقل از مقام آمریکایی: نیروهای آمریکا به چندین سامانه پدافند هوایی و سامانه‌های راداری ایران در اطراف تنگه هرمز حمله کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/657825" target="_blank">📅 01:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657824">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
سامانه‌های پدافندی در کویت و بحرین فعال شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/657824" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657823">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
مقام آمریکایی: هدف از حملات آمریکا ارسال پیام هشدار به ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/657823" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657822">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDIC7iDAbaEBcnGlk8_ZXh4iv2_z74P5bTw7vuY9OolrL94ZGHiU9ZdXhn0c4X7FEBDGVYqwfJ8A2e1QhH0aQLFELPopjVcvT82xYAQMtQEcCSGOF7aIJPTZSS78WHdK1ywiMElwzr2phjgmwFR9NLvQH8fQoTOPA3ie2VxDtWJTc-bObNqx61k7_W9rL8F34wSeiDVx6bwI6HqDfz3BQI1UpCTS4POCjR_BDQmSFQl01jEoidhUtylKBNbkFLxKoc0WBLuVjzRehbQPa8cmeMuHncAM_t-woL8Wr43i-k7PzSxyqFfdR4GlWBUmbqzwPlZSq-9Ja21BTpPfQl1LTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سید مجید موسوی: ‏و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/657822" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657821">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
فایننشال تایمز: قیمت نفت پس از حمله آمریکا به ایران اندکی افزایش یافت و به ۹۲.۳۰ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/657821" target="_blank">📅 01:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657820">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
حریم هوایی قطر بسته شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/657820" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657819">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
گزارش های غیر رسمی از پرتاب موشک و پهپادهای ایران به سمت اهداف آمریکایی در منطقه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/657819" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657817">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی: حملات علیه ایران همچنان ادامه دارد
🔹
یک مقام آمریکایی در گفتگو با الجزیره ادعا کرد که نیروهای آمریکایی به انجام حملاتی علیه ایران برای دفاع از خود ادامه می‌دهند و عملیات هنوز در جریان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/657817" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657816">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/657816" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657815">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ایران به تجاوز آمریکا پاسخ خواهد داد
‌
🔹
ایران همچنانکه ساعاتی پیش نیز هشدار داده، پاسخ قطعی به تجاوز آمریکا که به بهانه سقوط هلیکوپتر آپاچی انجام می‌شود، خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/657815" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657814">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
اصابت پرتابه در قشم، صداهایی شبیه هواپیما شنیده شد
🔹
در قشم صداهایی شبیه صدای هواپیما و اصابت چند پرتابه گزارش شده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/657814" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657813">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
منابع عربی: بالاترین سطح هشدار در پایگاه‌های آمریکا در کویت، بحرین، امارات و قطر صادر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/657813" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657812">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
صدای انفجار در اطراف بندرعباس نیز شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/657812" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657811">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ترامپ: باید پاسخ انهدام بالگرد را می‌دادیم
🔹
رئیس‌جمهور جنایتکار آمریکا به خبرنگار ای بی سی نیوز گفت: باید انهدام بالگرد آپاچی را پاسخ می‌دادیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/657811" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657810">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
تمام کشور های عربی حاشیه خلیج فارس از بیم حملات ایران  در حالت آماده باش کامل درآمدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/657810" target="_blank">📅 01:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657809">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
به گزارش خبرنگار صداو سیما در قشم دقایقی پیش یک مکان در قشم مورد حمله قرار گرفته است
‌
🔹
به گفته یک منبع آگاه ۶ صدای انفجار در قشم شنیده شده که بر اثر پرتابه های دشمن بوده است.
‌
🔹
ظاهراً این پرتابه ها از جنگنده شیلک شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/657809" target="_blank">📅 01:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657808">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
سیریک اصابت یک پرتابه تایید شده اما مکان و نحوه اصابت مشخص نشده است
‌
🔹
برخی منابع از شنیده شدن صدای انفجار و فعالیت پدافند در بندرعباس، قشم و سیریک خبر می دهند.
‌
🔹
خبرهای تکمیلی متعاقبا اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/657808" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657807">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در مناطقی از هرمزگان
‌
🔹
دقایقی پیش صدای چند انفجار در مناطق شرقی هرمزگان از جمله در کوهستک و سیریک و میناب شنیده شد.
🔹
هنوز منشأ و محل دقیق این انفجارها مشخص نیست اما منابع محلی از فعالیت پدافند در برخی نقاط استان نیز خبر می‌دهند./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/657807" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657806">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سنتکام: حملات نظامی علیه ایران با دستور مستقیم پرزیدنت ترامپ انجام شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657806" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657805">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
صدای انفجار و فعالیت پدافند در قشم و بندرعبا
س
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657805" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657804">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
برخی منابع خبری مدعی شدند حداقل شش انفجار از موقعیت نیروی دریایی در سیریک گزارش شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/657804" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657803">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tke4B5EPfqfqdUhEQvxAxz9ShNxcg-ky3r90_3FVYU_62QWw6P99HE5JslItthrlH4EW004GA_SQz-TKzvFXlcc7Vl7GeJOMpKSdy-V-GXagu9Z2x_I_LWIlB7sgxtaMVFn0BOEtZmz9vOGovc4LtyndcRAV_XxwV8YPaxr89ruYzg3YizMnF-Yzi00yLM3keZhOkzJpkloKey9s4GCqTQXJmTAbnC9cnsmmCj3jSqCTrk8XZHeh6igoJkon48jq8KqQhi45YPws21ONyawIgae68cFsc1CzGsbf2UqtcnRXNNVZDjAAsonNvTm9aeWADErte2HyRbghGrUyS-rSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام اعلام کرد که در واکنش به سرنگونی یک بالگرد آمریکایی، حملات تجاوزکارانه‌ای را به چند نقطه در جنوب ایران انجام داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/657803" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657802">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای فرماندهی مرکزی ایالات متحده (سنتکام): نیروهای سنتکام، به دستور فرمانده کل قوا، حملات دفاعی خود را علیه ایران از ساعت ۵ بعدازظهر به وقت شرقی امروز، در پاسخ به سرنگونی یک بالگرد ارتش آمریکا از نوع آپاچی در دیروز، آغاز کردند
🔹
این عملیات، پاسخی متناسب با اقدام غیرموجه ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/657802" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657801">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در محدوده بندر سیریک
🔹
ساکنان محلی بندرسیریک از شنیده شدن صدای انفجار‌هایی در محدوده این شهرستان خبر دادند.
شامگاه سه شنبه، صدای انفجار‌هایی در محدوده شهرستان سیریک از سوی منابع محلی و ساکنان بندر سیریک و روستاهای اطراف  گزارش شده است./مهر
گزارش لحظه به لحظه حمله آمریکا
👇
khabarfoori.com/fa/tiny/news-3221874</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/657801" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657800">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
خبرنگار کانال ۱۴ رژیم صهیونیستی: ترامپ تلافی می‌کند هرچند کوچک
خبرنگار:
🔹
پیش‌بینی‌ من این است هرچند صمیمانه امیدوارم اشتباه کنم؛ ترامپ در پاسخ به سرنگونی بالگرد آمریکایی، یک حمله‌ی جزئی و نمادین انجام خواهد داد، مثبت یک ایستگاه راداری و چند سکوی پرتاب ضدموشکی در منطقهٔ تنگه‌ی هرمز، یا چیزی مشابه
🔹
یعنی حملاتی از جنس همان حملاتی که قبلاً هم بیش از یک بار در جریان آتش‌بس دیده‌ایم، نه چیزی که جنگی را شعله‌ور کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/657800" target="_blank">📅 00:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657799">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
الحدث: نتانیاهو و ترامپ امشب درباره ایران و لبنان تلفنی گفت‌وگو کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/657799" target="_blank">📅 00:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657798">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-qns_WZxVGDz4fyjUCmYXGfzYah4jhzK0uyZ4Awylk6IGQ0cvIzaqL1eenhh4QySXWQZbEstQy-pDCwlfFWZNrdJSu4md9GmJ7YJYidz2Em_VuyiGTWRd3MxTzhrrhz6FxQX5u6II6mSfJlnjyZWpklwg1DFYGBF0Rl91k9Ft7853tCA-F3tzYQOw1ztHBX3IphkZlwZl-CEvUGAmJYCerZNBqAJnqYYYYzxGiEgpkkqFJwyiLu9nvdUgrsxidmHFkpruhemwjHD3iU869EB9Mulqgmt0e4LEEDbXEPyhdFdYdoTLRc_uMRumexa5p_I_OYBkY5kS5YpFnDQNVQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب عالی برای درست کردن شربت بهارنارج که برای هوای گرم خیلی مفید و دلچسب هست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/657798" target="_blank">📅 00:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657797">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83de2e39f8.mp4?token=tnicuHkgkII6Gz_V8yPL8_uF6Wkb3W1OHXQXtRAkeRfz8YY9luafFtAUVrEUoX5pVyAXcrfNnssLyN_y-abFV3aRIFgqm3DpljKtBjOX7HmbrgRDuRzgTi99qwrWGoD80emKeR63jNMB6KdX2i6rhsjXGQCBNp5GI9zorIMWNzzOjDbHm42pNcjsPLLEOTugAPAux5-3F-Cqge6UXasy5DiFjVT8tMboeQl9DGgQjgzldRJUyGvK5LCrRuwdikSP8jECrWcDdWchzm_mwum5g2XaHS05-AP0o36aXbH5Nc9tv2eW3F-oL7kA0S4fPPyrF3fOhHJOE8P-NILWbU0cFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83de2e39f8.mp4?token=tnicuHkgkII6Gz_V8yPL8_uF6Wkb3W1OHXQXtRAkeRfz8YY9luafFtAUVrEUoX5pVyAXcrfNnssLyN_y-abFV3aRIFgqm3DpljKtBjOX7HmbrgRDuRzgTi99qwrWGoD80emKeR63jNMB6KdX2i6rhsjXGQCBNp5GI9zorIMWNzzOjDbHm42pNcjsPLLEOTugAPAux5-3F-Cqge6UXasy5DiFjVT8tMboeQl9DGgQjgzldRJUyGvK5LCrRuwdikSP8jECrWcDdWchzm_mwum5g2XaHS05-AP0o36aXbH5Nc9tv2eW3F-oL7kA0S4fPPyrF3fOhHJOE8P-NILWbU0cFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🏆
سوت شروع «جام وینگری‌ها» زده شد!
اگه فوتبال رو دوست داری، جام وینگری‌ها همون جاییه که نباید از دستش بدی.
😎
⚡
چالش‌های جذاب
🔥
رقابت‌های هیجان‌انگیز
🎁
کلی هدیه خفن در انتظارته
منتظر باش؛ این تازه شروع بازیه!
جزئیات و نحوه شرکت رو توی سایت وینگری‌ها ببین:
🔗
wingeriha.ir
⚠️
هیچ خبر و جایزه‌ای رو از دست نده!
همین حالا عضو کانال شو و ما رو دنبال کن:
🆔
@en_bank_ir
#وینگر
#وین_کاپ
#جام_جهانی
#وینگری_ها
#بانک_اقتصادنوین
🔗
www.enbank.ir
▫️
02162740</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/657797" target="_blank">📅 00:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657796">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dj2qJvM07apHrnUWJXSH9PIpYyPxUFQP57HvIQkg1nm0gG19Jqdv1vUv90Bqa4oaQpXMTBqvI6kq1Q-6166_CpZX_X0orROfuRh-4SqZs1gSc9QYFzx78hHMo-fZnVcGCaYDab0Fh0ehdwP68v1OrbDphU2Ru95r1kojzjFihq1o3cSVT5mHY88tChWrcQgmLgqf0FFRsrLJunri7afV-VhGTi58ryK0DzrygC3vZwUQCW9dCc7nci7FRe6PoKtkyKBgqXAEOBPV9sDDI-2zczL4q9WK7AJX7q8gJWtKgSwTOaWFjhKSMyPPsVU9kAHfrsF961OPcFpxLgl4gIBqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرژانتین تنها تیم جام جهانی است که تا به امروز تمام بلیت‌های بازی‌های مرحله گروهی‌اش به فروش رفته است
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/657796" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657795">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
معاون وزیر امور خارجه ایران در مصاحبه با الجزیره: هیچ هدف‌گیری عمدی از سوی ایران برای بالگرد آمریکایی بر فراز تنگه هرمز صورت نگرفته است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/657795" target="_blank">📅 00:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657794">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صحبت‌های جنجالی مشاور اسبق هاشمی رفسنجانی: پیامبر چطور با پادشاه حبشه صلح کرد، ما هم همان کار را بکنیم
!
محمدصادق مشایخ، مشاور اسبق رفسنجانی و رئیس کمیسیون اقتصادی بیان امید ایرانیان در
#گفتگو
با خبرفوری:
🔹
سال ۱۴۰۳ گفتیم اگر سفارت آمریکا باز شود، مشکلات حل می‌شود ولی انگار می‌ترسند این کار را بکنند، به هرحال ما داریم ضرر می‌دهیم. ما یک اشتباهی کردیم که سفارت آمریکا را گرفتیم، الان هم ۴۸ سال است که داریم تاوانش را پس می‌دهیم.
🔹
باید آمریکا را همان چیزی که هست ببینیم و باید دید پیامبرمان با پادشاه حبشه و دشمن چیکار کردند و چطور توانستند مکه را با صلح فتح کنند تا ما هم همان کار را بکنیم. بارها این روایت را آقای هاشمی‌ رفسنجانی مطرح کرده‌ بودند که ما بیایم و با آمریکا بسازیم و از این وخامت اوضاع جلوگیری بکنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/657794" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657793">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QawPMYGzyIwj9rDIxTPtZmTQr31TRruukEt8VTzl-VsTD1ZkdOdeote9AaAD2vyZSYjZNYjckZX9bP3RJ9y-mebGrtIk2UFCS1wnkmQTDdsp57NY7fdaXFzyKAkSNRff9LN7X2PmhojbkRM7njGXCFHpYyWuUjIJOPEeR2fQ6I9UpuixDr64RfbpY9nBvNnvnhiolAvwGh7QrN4VQO2AFoCWBtxoc805YVbfB1CFlR7BnF2NN5gYo9bYGwUsfwg6g5mP-N7oflzTpiicvRx8q8EN8UKhTjP8nM6dAWiXi7f7isQiyfVlEWoXP3CovXSaIuB4PrEvVGLVtADx-4Q2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به مقر کمله‌های تجزیه طلب مخالف ایران در اربیل
‌
🔹
مواضع کمله‌های تجزیه طلب مخالف جمهوری اسلامی ایران در اربیل در شمال عراق هدف حمله قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/657793" target="_blank">📅 00:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657791">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA8_O9sUpNCOuPJxVdZcySwmlfp3exUwD7vnVl0iRC9UwDARqGAifGkepLHFo87T71DpYRwjt2nINvFCw2fu5zBbQ--BaHJZ9kcxcfnpFbvb5mj8a7-rGOcrr4_Wnht2Wpn99Idao3JdogvwFmuOQNIZpTomDCgF4yedtnyLNJoFRJrFij5T01NWwWxWlozqCyoSqt3N2K7VklSaO0Bkxuc9yyfoBF4t86_PksShZCxum3gc-H9gAQo6Wlb1zhJtetJWfE1iHSOpEwOBE60T87n6upb_aO74il8DgeCXih8ewTE3-zaoqALzQJP5GGqHvNAE-uw7dBss7NC2zEnSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/657791" target="_blank">📅 00:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657790">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ونس: ایران برای ما یک باتلاق طولانی نخواهد بود  جی‌دی‌ونس، معاون ترامپ در گفتگو با یو‌اس‌ای تودی:
🔹
مطمئنم که دخالت آمریکا در جنگ ایران ظرف یک سال پایان خواهد یافت و به یک باتلاق طولانی تبدیل نخواهد شد. آمریکا یک سال دیگر درباره جنگ ایران صحبت نخواهد کرد.…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/657790" target="_blank">📅 23:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657789">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ایران: قطعنامه ۲۲۳۱ شورای امنیت سازمان ملل در ۱۸ اکتبر ۲۰۲۵ منقضی شده است
نمایندگی ایران در سازمان ملل متحد:
🔹
باز هم نمایش دیگری از ریاکاری و استانداردهای دوگانه در جلسه و بررسی شورای امنیت سازمان ملل.
🔹
تعدادی از اعضا، به دستور ایالات متحده، ادعاهای بی‌اساس علیه برنامه هسته‌ای صلح‌آمیز ایران را تکرار کردند و کمپین دروغ‌پراکنی ایالات متحده و رژیم اسرائیل را طوطی‌وار تکرار کردند.
🔹
قطعنامه ۲۲۳۱ شورای امنیت سازمان ملل در ۱۸ اکتبر ۲۰۲۵ منقضی شد و تمام مفاد و وظایف مربوطه را به پایان رساند.
🔹
هیچ مبنای قانونی برای کمیته موسوم به ۱۷۳۷ وجود ندارد، هیچ قطعنامه تحریمی شورای امنیت علیه ایران باقی نمانده است و هیچ توجیهی برای تشکیل جلسات تحت دستور کار «عدم اشاعه» وجود ندارد.
🔹
این سوءاستفاده آشکار از اختیارات شورای امنیت و تلاشی عمدی برای گمراه کردن جامعه بین‌المللی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/657789" target="_blank">📅 23:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
نروژ با «آشپزخانه کامل» راهی جام جهانی ۲۰۲۶ می‌شود
‌
🔹
تیم ملی نروژ تصمیم گرفته برای حفظ آمادگی بازیکنان، بخش بزرگی از غذاهای سنتی خود را به همراه کاروان این تیم به آمریکا منتقل کند.
‌#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/657788" target="_blank">📅 23:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
نماینده مجلس: زمان پرداخت پاداش نیروهای مسلح مشخص نیست
موحد، عضو کمیسیون اصل نود مجلس شورای اسلامی:
🔹
موضوع پرداخت پاداش و حمایت از نیروهای مسلح به عنوان یک دغدغه جدی در میان نمایندگان مجلس مطرح است و ضرورت پیگیری آن مورد تأکید قرار دارد.
🔹
در حال حاضر زمان مشخصی برای پرداخت این پاداش‌ها اعلام نشده، اما تلاش بر این است که راهکارهای لازم برای رسیدگی به مطالبات نیروهای مسلح در اسرع وقت دنبال شود./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/657787" target="_blank">📅 23:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
ترامپ تهدید به حمله کرد؛ ایرانی ها بالگرد پیشرفته ما را سرنگون کردند، ناچاریم پاسخ بدهیم
👇
khabarfoori.com/fa/tiny/news-3221841
🔹
اسرائیل دوباره آتش‌بس لبنان را نقض کرد
👇
khabarfoori.com/fa/tiny/news-3221698
🔹
مرگ تلخ اینفلوئنسر ۲۷ ساله پس از سال‌ها میوه‌خواری
👇
khabarfoori.com/fa/tiny/news-3221683
🔹
سقف تراکنش بانکی اعلام شد
👇
khabarfoori.com/fa/tiny/news-3221829
🔹
عکس گوگوش با تیم ملی فوتبال ایران | خواننده زن چرا حجاب دارد؟
👇
khabarfoori.com/fa/tiny/news-3221720
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/657786" target="_blank">📅 23:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657785">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhhC8yFNdiAIuLkXa8JC3MWdJEvRhyI1buKPoi6rNVO6P5RABAhKPEekhGK6yULqjjlTYC9udL6mfE910R4pfygbQanxlKmrXptCTDflg3lrhEz6WGyDVSRwpn_QW4q7Bef3Yv7bSDCkJAbunS4mjlLetdLWdEPm9Lq1mAjDfKN7dU1iMXfTntNmVyOAdvnSTZdrXGWNWkeB-MGz8jzmQ9vMsuwInu8VqigGVBzezscxQx88m0E4fzwvbl-ARptisrVdEj8eCq64qocAQR4LxewpqW1Joob09E3E4c-DqVl1po4pQD6bzOHObsbpSx1SvJGnScvGpdqhY9j9yXAtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
You will be drowned in blood
در خون غرق خواهی شد
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/657785" target="_blank">📅 23:32 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
