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
<img src="https://cdn4.telesco.pe/file/t_r6O36fvFxyDz1cSWQQxM_R963RZymQu0Y3nFYBC1MGGWfwTroQzz9pkWk54W8-us6MEe7uNk_jdvNKj9sbMlswZYFQk6McxvosjumEPRuXpL2y7_awoYQGVfzkGxolqzCqHwPcLFMhsZGtH8Erh8jW0Ji3wx2bCFlk8_BhEnaondz4Aqfa3tsZlkhwslWzCq-HUX0RjTjV0wOidraFWH1DvfzsInd9KBvxK9P9DUJFG908oSlXjTL7phDeJ4uJT0TjRDnIn12qWX-ZG09JA95LwQRjC9gtlxfcNxp_6Shm2RyLh3zCIA_JIV-k_RNk3B9C3s6zHY7pfFe0l3clnQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 14:39:06</div>
<hr>

<div class="tg-post" id="msg-663881">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
واکنش اروپا به تهدید تعرفه‌ای ترامپ: سریع و قاطع پاسخ می‌دهیم
🔹
اتحادیه اروپا در واکنش به تهدید رئیس‌جمهور آمریکا، درباره اعمال تعرفه ۱۰۰ درصدی بر کالاهای کشورهایی که مالیات بر خدمات دیجیتال وضع کنند، اعلام کرد در صورت اجرای این اقدام، «سریع و با قاطعیت» واکنش نشان خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17 · <a href="https://t.me/akhbarefori/663881" target="_blank">📅 14:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663880">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd931c0cd6.mp4?token=ogu6XBTaPQ4UGXUJkhuf_jZe9SQvSPD1iVaksynNVoBwDPyVBVVzeeUnvAEwj6PCj9hoex53T28VPftJjx76udkFQAsBDEbyr2gwjLldMpitpD9rJLfiUctu0FDXawFw9Wr3VrraZQBjVHhh5d0xNKNNMVYS2e1QDEZSFQGNEUlF-s7zvnDcIqewxTJDEBzflAiXkMlN1kjiKUveBSqZFnWQzF5n_uUa_1YLT_4c0C83KrvXbKqbQ3Z1rrWF6vnB0GHWKkPOA798oo9G1W6Qwz_Vy7yEdxx2bldwtvFkGItiZpenCJgLDKleRuOGZIw-RezzsGyQoTvrcCNllV0fPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd931c0cd6.mp4?token=ogu6XBTaPQ4UGXUJkhuf_jZe9SQvSPD1iVaksynNVoBwDPyVBVVzeeUnvAEwj6PCj9hoex53T28VPftJjx76udkFQAsBDEbyr2gwjLldMpitpD9rJLfiUctu0FDXawFw9Wr3VrraZQBjVHhh5d0xNKNNMVYS2e1QDEZSFQGNEUlF-s7zvnDcIqewxTJDEBzflAiXkMlN1kjiKUveBSqZFnWQzF5n_uUa_1YLT_4c0C83KrvXbKqbQ3Z1rrWF6vnB0GHWKkPOA798oo9G1W6Qwz_Vy7yEdxx2bldwtvFkGItiZpenCJgLDKleRuOGZIw-RezzsGyQoTvrcCNllV0fPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت طنز از وضعیت قلعه‌نویی بعد از بازی ایران و مصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/663880" target="_blank">📅 14:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663879">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyZS3xftZ4SDt0d_NJRDFnz-OsibO1BeHeFdqjKtVkPMXLChsDR31nDq1LadFE7RQ1iCrsbI0ZVWUojODG10njxftfZkO0ERx2uUAojYd_DGtSB8Ddx8kweRjWmik4du_sHbePtkUGnzYrDgJoMBwjrdYee2JFm9WdfW8MEf4KjF_2FUED-f51xRto6K9xKGbxnRDTHDHCiFuc9pWLV-a75QDDNK4D22qvkIN3kALxr8ByfRyntMfUItMYJHdz4fCTN0r0kEtHNl-mcA6ReozeXwEvyhtNLtFG_M-u_Anhzwoe2yJ-LBDOkAPpLB2zuEnGq3Vk6E3GBF8yB-gufyag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیرِ برقِ خانه را ببندیم!
⚡️
🔹
آیا می‌دانستید وسایل برقیِ در حالت آماده‌باش (Standby)، سالانه میلیاردها تومان برق هدر می‌دهند؟
🔹
این فقط یک جریانِ ساده نیست، یک نشتی بزرگ است. همین امروز برای کاهش مصرف قدم برداریم.
#مدیریت_مصرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/663879" target="_blank">📅 14:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663878">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ncm7oesZPrzRFWzam3PRvW7nClKkc4uWj2kV4-yqMwx1c5ElXyD_uLF3QR2Ik7TLgTWqkyJfP_tHEJzOowTYZPci-YWbsANyEhniEbA96XuxPxPXrVBc76q9YK1fWrUzL2Vqb9IHKhDBItegQobaB_Ol9d-MrjoVQjnaPT6WZlevcfIma_XL5qspZaefI6UTz_-mZFpuKI-UPspWvmiGdku80FBlmqGsTh7gvWGAKSezYDGkNZhj92B-87L-86ZwU2V88VBdxCVTIfbwfOx-e16_eMyGRgFUWrodUkenlA2E-RllKoqbdMbPf-ebhNrlHIGewZxLgwV8qCqPv8zL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیر صعودی تعداد بازی‌ها در ادوار مختلف جام جهانی؛ از ۱۹۳۰ تا امروز
🔹
جام جهانی ۲۰۲۶ با برگزاری ۱۰۴ مسابقه به میزبانی مشترک سه کشور، شلوغ‌ترین و بزرگ‌ترین دوره در تاریخ فیفا محسوب می‌شود.
🔹
تعداد بازی‌ها از نخستین دوره در سال ۱۹۳۰ با تنها ۱۸ مسابقه، روندی صعودی داشته و در دوره‌های طولانی (از ۱۹۹۸ تا ۲۰۲۲) روی عدد ۶۴ مسابقه ثابت مانده بود.
🔹
حجم کل مسابقات برگزار شده در جام جهانی ۲۰۲۶، بیش از ۵.۷ برابر نخستین دوره این رقابت‌ها در اروگوئه است.
@amarfact</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/663878" target="_blank">📅 14:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663877">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjupfmiCjRbNwKMNzXsb0wJ2ZYR3tGQkElXiAvYKPqoGc_uA7qyEl8akIA-mM70rHTIiNryVdy3hyBNkEAqTfdDY9YX8zzVh5d3OMxa0Gm8p52JceUrlQJdetCIy65P3ne9p1-5Eo63vJ_hbHyjncidS9XOU2ehM-5m7yN-5rb0KQZeH7WRJ6ufDZtjqMMoBlE3-X0EkeHUvm1TOkU74aJoABH8AIVNgFxTJPhdk9XZRK8IOsHavDdZyp5zNQK00zw6E80-HeCqsTmr4w1uXIyFf7NENneeakjymO6jYQNinaeHo3Yug-d6pa1Q-62hgrBSlysZXzUGPx3Krd1K-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این روزها هیچ‌کس حریف اسپانیا نمی‌شود؛ آن‌ها با ثبت ۳۳ بازی پیاپی بدون شکست، به درخشش خود ادامه می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/663877" target="_blank">📅 14:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663876">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
بسته شدن کامل تمامی ورودی‌های تهران از روز جمعه
رئیس پلیس راهور منطقه ۱۲ تهران:
🔹
با اعلام آماده‌باش صددرصدی از بامداد جمعه تا صبح سه‌شنبه، از بسته شدن کامل تمامی ورودی‌های تهران از روز جمعه خبر داد و گفت: با پیش‌بینی حضور ۱۵ تا ۲۰ میلیون نفری، هیچ خودرویی از شهرستان‌ها اجازه ورود به پایتخت را نخواهد داشت و زائران فقط با مترو وارد شهر می‌شوند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/663876" target="_blank">📅 14:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663875">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1911760c6b.mp4?token=HeHJdKji_uQx9LzH7dRW_oF8diBmwnaVuFsnhtwaezRPnxEjR38kGpqQN-TkI-uqZZUlTEPEdAxb108w4540CRM-AW4tYueI-UutIuBoeQuch8lcnHDzTlt-_vOl87QycIPi4h4WU-GTlvgCOvWFW8vRZlmzi87fY5yA6J5IW2o4jn5NQmxX-yK7f3gQnOHHI8Hnbw8HHSYyUNiWfswevik_48SwaLq0i-64yfsnGq-108QdI20s52C3iRmPvs7C6fiGhSPXCPkbwxs53Cum9rMS7BFuPc_xnQRA2lLhYmPtc55J9k5Du9kWiScQ0GxM7r5qK_5V7h9djVwKXpIvYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1911760c6b.mp4?token=HeHJdKji_uQx9LzH7dRW_oF8diBmwnaVuFsnhtwaezRPnxEjR38kGpqQN-TkI-uqZZUlTEPEdAxb108w4540CRM-AW4tYueI-UutIuBoeQuch8lcnHDzTlt-_vOl87QycIPi4h4WU-GTlvgCOvWFW8vRZlmzi87fY5yA6J5IW2o4jn5NQmxX-yK7f3gQnOHHI8Hnbw8HHSYyUNiWfswevik_48SwaLq0i-64yfsnGq-108QdI20s52C3iRmPvs7C6fiGhSPXCPkbwxs53Cum9rMS7BFuPc_xnQRA2lLhYmPtc55J9k5Du9kWiScQ0GxM7r5qK_5V7h9djVwKXpIvYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با هم بریم به مخفیگاه هیتلر در جنگ‌جهانی دوم!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/663875" target="_blank">📅 14:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663874">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای الحدث: وزیر خارجهٔ ایران فردا به بغداد سفر می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/663874" target="_blank">📅 14:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663873">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وسوم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای حسن‌رضا هادی‌زاده که در کسری از ثانیه متوجه تغییر رنگ در آسمان شده و ندایی که پیام فرارسیدن مرگ به ایشان را می‌دهد را می‌شنود و سپس به آسمان هفتم دعوت شده و تا آسمان پنجم گذر می‌کند که در این میان به خاطر دعای برادر به درگاه خداوند و متوسل شدن به حضرت ابالفضل به این دنیا بازگردانیده می‌شوند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حسن‌رضا هادی‌زاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/663873" target="_blank">📅 14:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663872">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔹
آخرین وضعیت شبکه بانکی: خدمات کارت‌به‌کارت پایدار شد، اختلال خدمات آنلاین برخی بانک‌ها ادامه دارد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/663872" target="_blank">📅 14:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663871">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ3ZdC_SyaA2ir3GoTVR98ynLOBYCUysWbRiiGeaeEUjaZqp-i1m3RUtspIAEuA6SmE7XfbC2qAKpSyfOlmf0RHurtVZckuXHfd-0YVkqiu4RZ-NII83gjEXzYWygM_OByDNb58H4CtOjgUZfqe0DNp8dX4nZl1WQlj5z3wfg9KDud0oOUyJUJ_VklgBr4DDLARtFLCLAE1KVnGoTV2vhA9h3UlZ10iY8JrjDIC9m1yZPKTaPqSiHMGIrLbfl0cRYTQ_8OcFr_Llqdb3G6lZKY05z1RKs4GSHqJj9--S9uvs5bk0K5SGgalFzJxHrF-xiqNz9TmeuTJlK79XO1JFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز یک واژه، برای فهم بهتر خبرها امروز نوبت اصطلاح «حق‌وتو» است؛ می‌دانستی یعنی چه؟
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/663871" target="_blank">📅 14:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663870">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
خلاصه بازی ایران-مصر/ طوفان پسران ایران به پیروزی منجر نشد!
⬛️
🇮🇷
1️⃣
🏆
1️⃣
🇪🇬
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/663870" target="_blank">📅 14:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663869">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس دادگستری استان تهران: حکم ضبط اموال ۲۰۰ همتی برای مؤسسهٔ مولی‌الموحدین صادر شد.
🔹
رسانه پاکستانی: شهباز شریف در مراسم رهبر شهید ایران شرکت می‌کند.
🔹
روبیو: واشنگتن در حال برنامه‌ریزی برای سفر ترامپ به هند است.
🔹
آزمون‌های امروز و فردا دانشگاه علمی کاربردی لغو شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/663869" target="_blank">📅 13:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663868">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_X3T09X9KOfDMTV2F24nOFiNe49LdXaJ8i9pXdXdGNfQdKXUkccSu0WlJmTX16S3xAZmiqGh4-OCbY12konL5b0Wyv1Vhb_lnuwOBwqDVnXkq7nOnbAoBiPj2EVe10ikWqMwNs7BdckxDESl-TxtudgP-225GVKvoxcFyatiI3q2OOhhoE8VKAuVp0_6GPL0dVqy3DkNsMzUYKk5ciaOC7gVzRSyNVByADe_XXejumm7hFWjGttoQiqu7cmdzq39QaFIf_yA0YAC3QoxqsJAM9wTlcpamRLEcpByKNb3HjbVdvNLqSIlsM3IxMygLMKdiIlWsbUV7ulzXxZ7A3p3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: پاسخ نقض هر بند از تفاهم‌نامه، سریع و کوبنده خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/663868" target="_blank">📅 13:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663867">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔹
گل ایران به مصر  آفساید اعلام شد
⬛️
🇮🇷
1️⃣
🏆
1️⃣
🇪🇬
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/663867" target="_blank">📅 13:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663866">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujKtg0YscaZu1pyklJqv3GdftxgPs-DmetefVKULQB8xWAB6xXpEm7apdWBWiJZM_Q2EQIw7uHy-uecYM1QVviOlZSLubPjTgpM9QxR9qT05IaUQwF_7evgB2yGzC72gcHFf-ZdgRGexjhQ4MNPjiAFnA5jQMwvifFsgRkiOoJXxMmYS6XmPmRy3lhdEe0Ql6JmcL5gdMS9ccydxpc7W9g-Xx9dwJFtYQPdY60C39IR2G9cmH1aMrA6YwROeozh_vz8wxyyM9eOkOGhGB-hBALEwaqnnKKA3uEe0bgo4so-RnyIybAHV3y0W2U2-pklNhrEcjF85lEpaCqeeRDKI-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار سازمان غذا و دارو درباره مصرف مکمل ورزشی ON
سازمان غذا و دارو:
🔹
سازمان غذا و دارو اعلام کرد مکمل ورزشی ON (Optimum Nutrition Whey Protein) مجوز رسمی این سازمان را ندارد و از مسیرهای غیرمجاز عرضه شده است.
🔹
شهروندان مکمل‌های ورزشی را فقط از داروخانه‌ها و مراکز مجاز تهیه کرده و اصالت آن‌ها را از طریق سامانه تی‌تک استعلام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/663866" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663858">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kW3dsOeGVn697pDKkX3_Vz_5PIrr4YUO-Xn1h2cE5JTGfWP_fHedLlB5YAulcx-7P3vQ8LRhaasm_MxMQhidVDMuh78EauCGTJ34sBjKguNsSZjI8Fo5PrwrTdv76VhCaw08eHS-uA1ZbfHUzkIqTSoNCa6igsZAxXvtMtRWwZQ_ZwWFp28UN5s1pFKGY7MIKBj7--9rLLVvBiAUK5ZXGioeJAltGISq9HA1n1dn86RJu0lNSBj1COuFwvl_UmA_Oqywnp76XdLFeDU72PL4yOArbyJMzvapdf8a9Tvdp5U1GDKnMDPbZ7Ypg_rprqWalBeEvC-ucfPyRfUPFeAiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHMJWF8xeK7eEFw_MvKMxeFFl3Xb4Y0G9KZyFaiNDhBr_iUAgpEGwYycUYZziSj5n6w_SPylbrl5_6Cihn96gSwmEuTJJkCgoUj042MaaWY-xcYav26S2JIyZnPjdYgQCkufDcZaQ27CXxFX2a11d4CV7w5TPzXYo_AQUvCh_9iSWzk7n4GaZv7x1Rxhrlle6bS5xJC-ANpX9T_FccJ_HanrfgYln5gF0ciHEok9_6kCvj9PInqapDJ9tc2QeyyxtEc-MiYLMGu4--SSVM4hnediLyAZV25r-WUcQvHdQ5PgHFQeQj_wd8tNqqsx1vc1PzCFJqNV4cJ-8deZmDeiXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oa_BKsNPk8TUUXZz7ZFwQUit2Z_YUVFiBZgYVE0rxdeVs-wXkrWym_bwL45lnCIUEnMFjrRpZtVqaWXtPIxPCtcqis04a8Y9fGrcDlyH1TbPUtpFkiDnut_uN32u9bgjLaGv-_Y3fbWddzNz5I16G8RfRNccz_4PbFHrI8My9GYt-6hGguW00zm67QujxlatNwzzGCGyzH5vKc-gvnNr6om5IsNmRidS6ggKdlTlJVj41Taahw0kGgYSyPW6jOELPVoG4heVw14yLQBcLXf4vMxxiiZwZTM1zyQedOe5039VSBwSTsHkg5YleYasXyhT0CcB3JXGsTcrINM54XvJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E05LUbLRCb5FB_YdHeXwsp4G-W3RTV5TVKfEr1cdDNk4pKHzshWVUqWT3bduScrJ_CPed-i8O7SNh5D4_jRUtt6FL0ypWodJnT6ZxMWJDpXphu78CYgFqeTIVI9aZ2zjE40nlOm4fUmtGuFPSULXyUHIhsiMlrChWUUSPlJWuVTS2BEzk_Gfoyb1wQA9DSf2NSAirHQ0KEOaMviQaWigv7Z_3J5Q2CzWqstnRX5swFltoWSsI-f-gYiQk8aENO8OsbjOet2K_S16WVgzV7t9dYdk4ffZQEGD_y0kvKceMNPLllsZiCcdZwbjeoU8YA9V3xBQWK9wTDyN4b8vGkMqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvUhw6rvLcXFTl_JB18RtyEGDTEDMVsr7JpbAiZ8kmHd62Nk7mVBJRGDKkgYVgCIK-IfkvQM7kttS17xPUylJ9uVYP1WNUwmsOj83ftudF4wFTmtFhWSGUCguSz2XUV5Z_vDpQVTWWR8pA_uZRUMlBIJFM5Y_Run_hzA3kgoQMWynCbl2Ptf9QxbcJmtSy8ExwHO62kUp3EYNYcalX9Wf_1eUKDeueLzgz27Ucaw9qlAhbkO8x2NS4m5qYNMdq5mbeM8Asj13pJ7ktX4aVBtfy7kOryf8l5gqwQQfLpxlZZSOwI6a1b-25MhAiD7R6ZFmW1cvQ5F7DzmTS8BNfcxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giDib88EzDAmQIiG9XfNCDpfIrtwTEkknv5ey9EH5XwHx--0DkzaqiL7SZ9g7Yofk4VMUXR8s0WOgYJa1kZ6WnxVWlRndm2A8R6nbVcvHysCIJpByYuHvXpnK8v_wUXfK8KS4K5bCZ_Ibcj2iMEyznQQb2I72YFRD41LKCXMOgYGRz883zmbZ1seMpTeSzoqGsxUOtnghdZsQhoB979h7UNZ2S7fdwkHmq5dm2vJKKnGtzhCWPOWnPxPp4u8XXPvvnLdBSTqA_n96b87urvwW2ADj1EW_CxLBrHUqYYt_z_gqlDQbTkyDfwQYxLAc0pKY14-mD0CHnV0l22oSfdiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJQP2kYgXkel8XKdOs56fMhEGQB_-BHuhySsQGMD5Y-2Ow-YBDOU6D4FRxIJ333xe0JkNVU4OoY4AUdMK1z-84zytPQAkLGDbvz0ox57qaE4JoPxlJ0xr5Quf3x9ZfVG2bPteaemw8xwUCOQL63rG-WOo1TdJaK4mJFgeYzaFHsDlTZ8vpML4e_04gv3eQS7tAY0ZdzxbmlYx6pllVXy-59pfGgGFMyrR357TrSawnR8b5b-iBUTMdiYlvtmD3yNSSR7WdbIc9tb_tpfv2qvcn5HpdepVA7oK5G_KWTBzzPdlW6rGhgWPLlkLnXuHiv__fsEQUrml6h6Lw1r-wURiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrwszNrlMopGOVwPiVxIzUL7omO_9jmWofELh12EabMADPeYjgk_OGlf6MHiQPkcOp9PurAA3jcTShjq2QFqgwihYe2Fnecu_v17xhvKDoxnWHpinKNbO_EEKDJfotFcarrG2Df5vREGf5o8XKka-txO8-O_-tGKgh1uCn4yDKEQJKiE5LouQdxNOKD3UtlD3vSsx6NGI3oE0wemqPnchuVc7ZZsjGXrsxb9jWYR3xKmexEi30rSKn-yglkOVpUe363DL-Pv3se4lQo1UiqWe9HFRJI5OSjloVLl90zB2LintUfymKyeUtLZOoiNseOW_zqWgOXnunTddef6gYIpwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان حسینی
🔹
هر کوچه و هر خانه‌ای که با پرچم‌های عزای حسینی مزین شده، نشانی از عشق به سیدالشهدا (ع) است.
🔸
تصاویر خود را برای انتشار ارسال کنید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/663858" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663857">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6338b65760.mp4?token=Puhn4SzStUjK6MCrk6ghraXIZdJKnkElIXDJCXBmDjoAXf5Dz8036sZ8nlwd8-89Y8TtQcBxysUpJC9NZM92FKzOWfTisJQh0eMYMHVE8Wl39cMQsdZjSJUxiI3zyyzF2GasQAHsm52Lb77P6SibYfgJFj0IdujkBY6QVZAxlhMEInCQCB4Xmns9gGtfrwUyG1O1GrXybjLb2bDCZN7dCY800bJ69kt0YFttujlBYDcnfH0lUXMZaeGL0PWrkrpZWFZ3UKmR9whOl8NMqs8OiFi02hmOkME1qJ7E8UjPYEZSdRLcOiwvmeE5o7J1hrv9r3vBD90PnfX1fM_wr64-uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6338b65760.mp4?token=Puhn4SzStUjK6MCrk6ghraXIZdJKnkElIXDJCXBmDjoAXf5Dz8036sZ8nlwd8-89Y8TtQcBxysUpJC9NZM92FKzOWfTisJQh0eMYMHVE8Wl39cMQsdZjSJUxiI3zyyzF2GasQAHsm52Lb77P6SibYfgJFj0IdujkBY6QVZAxlhMEInCQCB4Xmns9gGtfrwUyG1O1GrXybjLb2bDCZN7dCY800bJ69kt0YFttujlBYDcnfH0lUXMZaeGL0PWrkrpZWFZ3UKmR9whOl8NMqs8OiFi02hmOkME1qJ7E8UjPYEZSdRLcOiwvmeE5o7J1hrv9r3vBD90PnfX1fM_wr64-uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شادی محمد صلاح بعد از صعود مصر به مرحله حذفی جام جهانی برای اولین بار
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/663857" target="_blank">📅 13:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663856">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
اعلام زمان بازگشایی مصلی تهران برای وداع با رهبر شهید
🔹
ستاد برگزاری مراسم وداع: درهای مصلی تهران از ساعت ۶ صبح روز شنبه ۱۳تیرماه برای حضور مردم در مراسم وداع با رهبر شهید بازگشایی خواهد شد.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/663856" target="_blank">📅 13:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663855">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77881dbba4.mp4?token=EzLBf4jtsjp4pg-vOQE_Bt2FbArYa-C7jjTcfGI62zPW8PYQkT35Mid9vvCQY6PwfTDTeUqJas0s19btLQgD9-96960VI7ajw-R29erAMBNOIauKztO0mhWbMJbkxh5J0h8TSoTmJ1xRUPkTFkvXCPsikUa3y9Uf3-SfVWnTdASqTuCekKhk2ZjNXp37OGS3F-VSqCqQUJJv96idf7QQiL-1g94E80Bz8ZwUKgDcr6DqeXaZnlT6D_ILX8gfm4LgwVRnY2jXUq9VkMRe5yXsiqhhFwsdF6s1H6QOd-X4Y1pya6HSUzB7RSK6GBvheAv0IdyG1HkPsFFscvOSFIBW4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77881dbba4.mp4?token=EzLBf4jtsjp4pg-vOQE_Bt2FbArYa-C7jjTcfGI62zPW8PYQkT35Mid9vvCQY6PwfTDTeUqJas0s19btLQgD9-96960VI7ajw-R29erAMBNOIauKztO0mhWbMJbkxh5J0h8TSoTmJ1xRUPkTFkvXCPsikUa3y9Uf3-SfVWnTdASqTuCekKhk2ZjNXp37OGS3F-VSqCqQUJJv96idf7QQiL-1g94E80Bz8ZwUKgDcr6DqeXaZnlT6D_ILX8gfm4LgwVRnY2jXUq9VkMRe5yXsiqhhFwsdF6s1H6QOd-X4Y1pya6HSUzB7RSK6GBvheAv0IdyG1HkPsFFscvOSFIBW4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفت!
🔹
شهید سید کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/663855" target="_blank">📅 13:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663854">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
بلژیک نیوزلند را گلباران کرد
/
دی‌بروینه و یاران هم صعود خود را قطعی کردند
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/663854" target="_blank">📅 13:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663852">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سازمان دریایی بریتانیا: یک نفتکش گزارش داده است که در تنگه هرمز با یک پرتابه ناشناس مورد حمله قرار گرفته است. خدمهٔ نفتکشِ در سلامت هستند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/663852" target="_blank">📅 13:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663851">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
خبرهایی درباره حمله به یک کشتی در سواحل عمان
🔹
منابع خبری گزارش دادند در پی این حملات، صدای چند انفجار شنیده شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/663851" target="_blank">📅 13:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663850">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW16IK5Un3fLOxj--_v66C53W6LwwbWs9XhBhCvmrY8Y4rC9_D19fsPKcOUtF6WL8Nt9lNRps0P-DUrkW5JbjR7gAZPaF1Y6HAdIWHd7fTeHaEUeaAcD7iBsZUgWwD9fLMKhfensNqVoTyPqwVpgLUlCQiTUfwuJ0X_hvCvFeKLAqO_W9Qlh7DdHMUL9VX47qJdqqaPw7raEpJ39DFMHZg0syjAYL3bvhDTLrvS6Q9XJfmmDmLqbUkGaThyL3j5eP0sd-yShruN6Nw7Z56XNWhytAD152zChUsd_owaN9ZfLI03PQuPGRh3u_RkGJr2NmHNx9E_-27d0GtVAFWOf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرهایی درباره حمله به یک کشتی در سواحل عمان
🔹
منابع خبری گزارش دادند در پی این حملات، صدای چند انفجار شنیده شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/663850" target="_blank">📅 13:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663849">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ارزش سرانه معلولان کمتر از ۳ تخم‌مرغ در روز است
علی همت محمود‌نژاد، مدیرعامل انجمن دفاع از حقوق معلولان در
#گفتگو
با خبرفوری:
🔹
در کشور بیش از یک میلیون و ۷۰۰ هزار نفر معلول به‌طور رسمی در سازمان بهزیستی کشور ثبت‌نام شده‌اند که ماهانه به ازای هر نفر تنها ۲ میلیون تومان مستمری می‌گیرند که کمتر از سرانه ۳ تخم‌مرغ در روز دریافت می‌کنند.
🔹
از وزیر رفاه می‌خواهیم به جای سرازیر کردن مشارکت‌های اجتماعی به شرکت‌های بزرگ و سایر ارگان‌های وزارت رفاه، مشارکت‌ها به سمت معلولین سرازیر گردد. وضعیت معلولان از زمان تصدی وزارت میدری روز به روز بدتر شده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/663849" target="_blank">📅 13:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663848">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD4mLxgzFB1aKJtC2WHBeNzN2R0sci7vmLRbCVwLlPlzjV8YlytonXFTTw8mMnqSV1ryQ2tg5CaLG33wKt7c8-N6hDMp-BwkZPBJpDxvxsiuAyMiah-xPgPuyw9xeoZ_EhG2eKhsq63V2ZiUGtrOX4GfkvElPePgowy3-WGWNidtaRwaQTsyjyhi9_twuxrWdn7NoETUQcOtZ_uT9EtIcNEXYr0I3-YEiZNfp5Rw3SYci5tejomiczvHbgaZKslmMj3zE0ppWg6Rj8f1TzClyDA-4NBSkY6xpJN3uqeWrLZWHHCEtqNzCyjVh_n1iyDsDmzC7FBHaVe0CauRxzzl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرمازدگی؛ از علائم اولیه تا اقدامات نجات‌بخش در یک نگاه
☀️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/663848" target="_blank">📅 13:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663847">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره مالی اتاق تهران؛ همراه کسب‌وکارها در بحران
🔺
مشاوره مالی در شرایط بحران؛ راهکاری برای حفظ نقدینگی و تداوم کسب‌وکار. اتاق بازرگانی تهران با ارائه مشاوره تخصصی در حوزه ابزارهای تأمین مالی و مدیریت زنجیره تأمین، همراه فعالان اقتصادی برای عبور از چالش‌های مالی است.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/663847" target="_blank">📅 13:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663845">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d4a20ece.mp4?token=FbghbSeO-Gk7vLprRJLaZp0GWuDOOa3z0GCqemVij1Mt4rrhvz34a8OwYb_CGsVNWaiFveSnQgsrfzjxXSWWdprWDon2X7XZtK-Bktltqn7XONEIfZsTGC7wxzgVHoVK49UOwUOTWF0-bAEuXpdkYx6T8pKeflicYIH0IcPu40KifOIZ9ivcUeDw1SQDMINLWEPuj3VaN826By7ISSPCPa-wrlLGEK_qbMQZcagBnUCimMy12QP_aTPH7EHdZJgniUJRbYU3hzHVE8IN3oSQ80UZEOvoBDF14YELQiHpkxZI2Wv9seUwTPUBNdxl5CojTeYU_S0jMTm_9AuwhU76yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d4a20ece.mp4?token=FbghbSeO-Gk7vLprRJLaZp0GWuDOOa3z0GCqemVij1Mt4rrhvz34a8OwYb_CGsVNWaiFveSnQgsrfzjxXSWWdprWDon2X7XZtK-Bktltqn7XONEIfZsTGC7wxzgVHoVK49UOwUOTWF0-bAEuXpdkYx6T8pKeflicYIH0IcPu40KifOIZ9ivcUeDw1SQDMINLWEPuj3VaN826By7ISSPCPa-wrlLGEK_qbMQZcagBnUCimMy12QP_aTPH7EHdZJgniUJRbYU3hzHVE8IN3oSQ80UZEOvoBDF14YELQiHpkxZI2Wv9seUwTPUBNdxl5CojTeYU_S0jMTm_9AuwhU76yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طارمی از خجالت فیفا در آمد
!
مهدی طارمی:
🔹
این دیگر چه قانونی است، چرا ما باید پس از پایان هر بازی به مکزیک سفر کنیم؟ چرا تیم تدارکاتی ما هنوز ویزا ندارد؟ این یک فاجعه برای فیفاست!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/663845" target="_blank">📅 13:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663844">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8ca5c1e5f.mp4?token=qiFyg77u2my0jjULaPkKDhQ_4eBjfpS4wEPaeHve2PwrxvMfRwZnN8HKeyyiqstviBQst-EloYhCPwRZL9RnFegWvuGoCxPpP5JsiUspm5XovDCp_1JwwwsxXrYru2CJWGbSMW-umlnGnM7RLu7kqC_H8Zpf8y-td5su_TzrxJ-e5Ng51YJt3aS-ikr0bUbUBegL87ZlQ7Dp58zww-01kQazRVhKqXcaguhsLiC5uWYkvD8UFeBvuvafmRcfiDikmPTDklfM6fIBCdj5NNgFaUl0rciy8lhpSs9flVppPfBjtUP2LVqm0h0hZsSf2hNKkZvCeES_ZaK303jNSPCHaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8ca5c1e5f.mp4?token=qiFyg77u2my0jjULaPkKDhQ_4eBjfpS4wEPaeHve2PwrxvMfRwZnN8HKeyyiqstviBQst-EloYhCPwRZL9RnFegWvuGoCxPpP5JsiUspm5XovDCp_1JwwwsxXrYru2CJWGbSMW-umlnGnM7RLu7kqC_H8Zpf8y-td5su_TzrxJ-e5Ng51YJt3aS-ikr0bUbUBegL87ZlQ7Dp58zww-01kQazRVhKqXcaguhsLiC5uWYkvD8UFeBvuvafmRcfiDikmPTDklfM6fIBCdj5NNgFaUl0rciy8lhpSs9flVppPfBjtUP2LVqm0h0hZsSf2hNKkZvCeES_ZaK303jNSPCHaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آب‌دوغ‌خیار اصیل ایرانی؛ ساده، سریع و فوق‌العاده خوش‌طعم
😋
مواد لازم:
🔹
نون خشک
🔹
خیار ۳ عدد
🔹
خامه ۱ ق غ
🔹
ماست ۲ ق غ
🔹
کشمش ۵۰ گرم
🔹
دوغ گاز دار ۲ عدد
🔹
سبزی خرد شده ۱ پیاله
🔹
نمک و فلفل ۱ ق چ
🔹
دوغ محلی ۱ لیتر
🔹
گردو ۱۰۰ گرم
🔹
پیاز ۱ عدد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/663844" target="_blank">📅 12:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663843">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSUvmSvxI4gJmR_k-3cZPpe-Qn54h70gvtuAnT34W8KIlvfkPTiAowQoBW-pFxEXuEdxQUT9jM5OAD4qeU2v_YePneUtsJ5-08ZQRFRkpGUwaXRhNLHtpIy1S3J0Lvxp7x7AapOhv_2ZQYUT49n1JoJj--Z1EbZu__ktgP7fTqjcGbUQjZ7ijLUVCWXjB12h7-mFt76Tb2iuQNBGpv5LVEI5oxjAj6Sr-tzhj-3hvES_OEzmU5Zva8VqMQpzMitspS0rm0c1U7oqFqXOhPIYCMKrSUqas0IKltxF3t29WB4T4Pz99kx5Hy1zv94hEVS8CsmazyUprkNLk58lHEJyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلفیق فوتبال و اسطوره؛ شماره‌های تیم ملی نروژ با فونت باستانی نوردیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/663843" target="_blank">📅 12:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663842">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
نوازندگی کارلوس کی‌روش همراه با جشن بازیکنان غنا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/663842" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663841">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
المانیتور: عصبانیت در اسرائیل بر سر رویکرد ونس در مذاکرات با ایران
منبع نزدیک به نتانیاهو:
🔹
ونس به آرامی دارد ما را به کیسه بوکس خود تبدیل می‌کند؛ آنچه اینجا اتفاق می‌افتد، پیروزی ونس بر چهره‌های طرفدار اسرائیل مانند مارکو روبیو است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/663841" target="_blank">📅 12:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663840">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دومین مسابقه مرحله پلی‌آف آسیا بین چادرملو و گل‌گهر، روز دوشنبه ۸ تیر برگزار می‌شود.
🔹
دبیرکل شورای همکاری خلیج فارس: آمریکا به ما توضیحی درباره صندوق ۳۰۰ میلیارد دلاری نداده
🔹
شاخص کل بورس با رشد ۱۵ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۱۷۶ هزار واحد رسید.
🔹
شهباز شریف: آزادی دریانوردی یک کالای لوکس نیست بلکه ضرورتی مطلق برای کل جهان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/663840" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663839">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
آخرین بازی دانش آموزان مدرسه شجره طیبه میناب؛ روز حادثه (۹ اسفند ۱۴۰۴)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/663839" target="_blank">📅 12:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663838">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔹
نیروی دریایی سپاه به تجاوز و عهدشکنی آمریکا پاسخ داد  روابط عمومی سپاه پاسداران انقلاب اسلامی: بسم الله قاصم الجبارین  فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ ۚ
🔹
به دنبال نقض آتش‌بس رژیم صهیونیستی در جنوب لبنان،…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/663838" target="_blank">📅 12:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663837">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P26xGBWf7PBEhJQGLY9KTa_m1-Vm0vzAD0TM6FYBr6vrKR72yw66IuefuGvXYcgdScs2xdylVDQJ1xDgHSkIN395Ig8e_IbHsPJFK3PnFZL6VxSzi7MU0T4VKA0y-eYpQUQIdCfO0Vbw4aOsTfKSGY3lCMoPIaf6pSI2h4zAFlzm-zOfxFj4iU92TlqCCKYoCbtp-le7u-nP4LC50ljrNbEnvCcoRY2A9kjDvPGGIxGHwzG8JEN_3xQMpWcKxwQrJ4qeVKfjAZ4OWJi5a2C6TahJD-3SbO_KYp6X7R9XqfkzcjHpiL7njRAIOeWHDfy5tPGTn6PTKbuPZffgAf0NDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاد هیکی درباره بازی امروز: انگار همان داستان جنگ است؛ هرچه دشمن بیشتر به روش‌های ناپسند متوسل می‌شود، ایران سربلندتر و استوارتر می‌ایستد
فعال حقوق بشر ایرلندی:
🔹
دومین گل مردود واقعا افتضاح بود و به‌ هیچ‌ وجه قابل قبول نیست. با تیم ایران طوری رفتار می‌شود که انگار مجرم هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/663837" target="_blank">📅 12:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663835">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XARTQ-INzjIqMW-d_Y61IVgVj682ILCd7Ry-yNcxTwrQSRb6fskcSfHI6xos_BKSrrkzk9Aer2GbyliD81vGxG68w9Dpn4bFMvHbHo3bsd_eIPk-vcU88tMCcqotdxROng-aDa2ZiHLblqYGKZ-BZoiLf9oKgNch6ZqEbcy-JHU9Brvv0lmbhI1SQ5vG8XeMh5OhXmqiD5zr1agtazkj5RdvN_zKRD48ksDoXvuWg9mluH9hHKwa0ljIi1kbjSPpjqTyF935aNEF36tUYAmoyRM8VSmintcXWK0NOrWragxlxuXwpIe9CxRI876gESMrMjKn1_atHGgHVG-Sl1JuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kMxk-Gfm2jyUu-e0zcsANddOwA_BxHXZZEQq4vSvnLWACUNfMCngVPgHT-HAW-0cnzo-GSSvJe0iEm05Qh9E1hahChTH8SqbtXSBEaLhvFSheVb7rkzgtQ4vqb0sfjO0yapMYgtDn6s58r-b9AOMXooGBFbLFBlrdEPUVhO5WyXgqPaVxRAOPn8q0fajYHDPegKPMWkK4jgsCvEkzEu3GH4hkTKT_9VHoXUJUpzizmMFuSKlShOYT-SOeyAqkcT87X-ZsCfDIhSyqB-6RpPNZyLb8jySorTIC4i_g9FowziLqQDcd0Lm9SzM8QTW9P9EdneOav4mLRN9AyDb52YWfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گل دوم تیم ملی چگونه آفساید شد؟
🔹
دروازه‌بان مصر از دروازه خارج شده و‌ جلوتر از شجاع خلیل‌زاده قرار دارد که در چنین شرایطی، مدافع آخر، به عنوان دروازه‌بان در نظر گرفته می‌شود.
🔹
خلیل‌زاده در زمان ضربه چند سانتی‌متر از دیگر مدافع مصر جلوتر است و همین باعث شد گل او آفساید اعلام شود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/663835" target="_blank">📅 12:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663834">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgSa_Qqmx3al7PL36vKXkqYpxMLhtKuFM0YcSdyqwhe2PiWfKTNCvshjV_kpJNuYl_10-9i0fG4Htk4BqXB2a6eijt-EU2mPwh7inrt196-Q_xRtY_L2gxRIrYPOar8azwb5lfuEB3P--jr3pInqy7PhrRlA3r3boK1f69d6Djoh-5O335JUUsTUGfGJGOObaTCnByp8HhUAMgsrsqSRTZiDluDM8RgjHNTTQzrKBw5zMij9DhFAMot9fY3FePg3amQgZIGm0bpcPivo2z2LEv1INtnR2UiYYka5DxdhuIwTp3fbF2k71T_uHzqk1cqVA54JT3JwzURRpNtj0lOkbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور در کمتر از ۶۰ ثانیه فریب می‌خوریم؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/663834" target="_blank">📅 12:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663833">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd53596d48.mp4?token=aupJlPMlNuLgRJRsH767sVwrb4p3nY7eAJGY-PJ4rni1RSKhWRZ3PoNu61aT3nTYY5gTHrbaUdERaS7uKfAXvMOVw64iwLoUkJlZZiatTzmViUlXSrN3CxQqz8oaYEJ6TNoRgsa5J49VzSBuurNclnCXRfrWk6iuD36-1dBARIptgEjV5j7QHFT0aK5CSOdcU6LENxxwMxwxuGP6a_fCkpuq9oGUkdB1F9Mpfp21ndJt57DE9YmKp71NBKYUFhtLg0ZlsvuxWN0r2nOrp4axIEdy6aAnGvn4OiR10wIEDgSfMtQaeVAlAOUdM8pz80FcQoYhxYZ9ZdbereQZWcu7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd53596d48.mp4?token=aupJlPMlNuLgRJRsH767sVwrb4p3nY7eAJGY-PJ4rni1RSKhWRZ3PoNu61aT3nTYY5gTHrbaUdERaS7uKfAXvMOVw64iwLoUkJlZZiatTzmViUlXSrN3CxQqz8oaYEJ6TNoRgsa5J49VzSBuurNclnCXRfrWk6iuD36-1dBARIptgEjV5j7QHFT0aK5CSOdcU6LENxxwMxwxuGP6a_fCkpuq9oGUkdB1F9Mpfp21ndJt57DE9YmKp71NBKYUFhtLg0ZlsvuxWN0r2nOrp4axIEdy6aAnGvn4OiR10wIEDgSfMtQaeVAlAOUdM8pz80FcQoYhxYZ9ZdbereQZWcu7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💡
روشنایی زیباترین بافته ماست که از خانه‌ای به خانه‌ای دیگر جاریست
⭐️
در مدار این همدلی، فرصت درخشش برای همه فراهم می‌شود؛ از اروند تا خزر این جاده نور پیوسته باقی می‌ماند.
🤝
تار و پود این عظمت به دست ماست، برای تداوم تپش زندگی، ۲۵ درجه قرار همدلی ماست
✅️
همیار ما باشید
ba25.ir
#پویش_۲۵درجه_قرار_همدلی
#هفته_مدیریت_مصرف_برق
|
#شرکت_توانیر
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/663833" target="_blank">📅 12:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663832">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/663832" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663831">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb908d1e4.mp4?token=bOmlk21x12UDdXeEHfnEkEvu63VEk_YmPDLViZRiBf8G3WraFIiezixmvrpMLlMIUStpSf0LkgRfreMHkcVVzy7HEN_E-T8iz42s-u3ySVi3-byDKCtGCXpgN7-dKWcq7cdqANsW3uW8g6XoTlS2OgMDkR-V_YgxJnsuOjTi0vKBoGXjOGqZ84_YXtlfv8vRBVcLD2ckMY5QNAidEsUvFHXHEMcpeAe00doeQxGG-Yqa0jDNIAsiS1RJTsA6U0k_3rlm-z6MNyla8nobLcneP4OwfvgL9fYXPBBMCFD2uXwnVKP9wz-DFH_azoCcR337E0M0iUgCoembLUn84kdYtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb908d1e4.mp4?token=bOmlk21x12UDdXeEHfnEkEvu63VEk_YmPDLViZRiBf8G3WraFIiezixmvrpMLlMIUStpSf0LkgRfreMHkcVVzy7HEN_E-T8iz42s-u3ySVi3-byDKCtGCXpgN7-dKWcq7cdqANsW3uW8g6XoTlS2OgMDkR-V_YgxJnsuOjTi0vKBoGXjOGqZ84_YXtlfv8vRBVcLD2ckMY5QNAidEsUvFHXHEMcpeAe00doeQxGG-Yqa0jDNIAsiS1RJTsA6U0k_3rlm-z6MNyla8nobLcneP4OwfvgL9fYXPBBMCFD2uXwnVKP9wz-DFH_azoCcR337E0M0iUgCoembLUn84kdYtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبر خوب برای دانشجویان، هوش مصنوعی به دنیای خودکارها رسید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/663831" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663830">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
خبرگزاری رویترز: کمپ مخالفان کرد ضد ایران در شرق اربیل، مرکز اقلیم کردستان عراق، هدف حمله پهپادی قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/663830" target="_blank">📅 12:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663829">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a430385722.mp4?token=o0cuf-8uG5Pjc10mlL7RX3PKoX_K7VXJjuIbBXuR0I6djPE5JgvlhBC_UDV4KLsB2tLfnDZB4ZdFUA9_us2MGEGy6bBVuKDGlx2defnJXTi4kSSk3B32N16Ve4ARQj4usBkdPLBRBX6AsoThx-l2sFXcQLOju08Zztx7CygVO_WT7LXxd-bD6r_EAPffwaoSl5OYP7j3pFnxFnzhw4LDoKKeIHws1hmUnTvHS4PDeWCvZZXs0KPuMbKOCEwi9cSmm_vpQHEqLQHMrspYXwySggZBpish6Q4UnV2qGb1rxPRjuG58QffxzYs6ksPdxHgCvO3zjvLlxxch-18OQQdAXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a430385722.mp4?token=o0cuf-8uG5Pjc10mlL7RX3PKoX_K7VXJjuIbBXuR0I6djPE5JgvlhBC_UDV4KLsB2tLfnDZB4ZdFUA9_us2MGEGy6bBVuKDGlx2defnJXTi4kSSk3B32N16Ve4ARQj4usBkdPLBRBX6AsoThx-l2sFXcQLOju08Zztx7CygVO_WT7LXxd-bD6r_EAPffwaoSl5OYP7j3pFnxFnzhw4LDoKKeIHws1hmUnTvHS4PDeWCvZZXs0KPuMbKOCEwi9cSmm_vpQHEqLQHMrspYXwySggZBpish6Q4UnV2qGb1rxPRjuG58QffxzYs6ksPdxHgCvO3zjvLlxxch-18OQQdAXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویرسازی لحظه گل آفساید ایران در لحظات پایانی برای علیرضا باباجانی‌پور هوادار روشن‌دل تیم ملی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/663829" target="_blank">📅 12:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663828">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
حکم بدوی اخراج دانشجوی دانشگاه امیرکبیر به‌دلیل اهانت به پرچم ایران صادر شد
🔹
در پی بررسی پرونده دانشجویان متخلف در تجمعات غیرقانونی دانشگاه امیرکبیر، کمیتهٔ انضباطی این دانشگاه در حکمی بدوی حکم اخراج یکی از دانشجویان را به‌دلیل اهانت به پرچم جمهوری اسلامی ایران از دانشگاه صادر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/663828" target="_blank">📅 12:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663827">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ7jYOiIsRWyeuYy-uRtGcTNPyuaMPK82IHQiabpkLFgKpS9Fpq1lSNtOrbvX4iJYzXYJPfOzB0imzwmPwVpWLYaFu1cksjJRv8bowDMv_btwJBlTNnO2GE_v-_X1DPXXi8prYVgVL6b4uA3Gk8OKJhDEYL-Il3VnQ4ifWC58Hs_8TCI3GEYnc0JRVJ5kQwCQeke-wAoNv5MWQaqKBNiz7Vru_qrhA5Gn4J858XUScbTV6A3BZ0xJKvf82bAeI5WCUb-tpg7l4F8taQQVrANQz1TdVK_raUcSZ9ZvjuduCKIZqdkx1bMf1N0h-n-Bp1q1fX45ZWnkZqLKHV1SwlWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیشرت جالب هوادار ایرانی
🔹
این هوادار ایرانی در آمریکا با تیشرتی که پیام«طرف درست تاریخ رو انتخاب کن» و هشتگ ۱۶۸ روی آن نقش بسته بود، سوژه شد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/663827" target="_blank">📅 11:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663826">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGVCMxxDcxw7bsQ5qiF98_kXxT36QD5XAr50_xDnbJA0WiC33-1vJ2UtuuvIHXsLGxz2eSiJlRFKX21iN7GBVo6xZGXe4lvDx4BJo07TX3A3O7BN1tOCkYvXt3ektJIy-XN2rBS5MONt6ZpWsIpzEf1s57FPAKKlAzFlnkPELnIdTdJm4jpXT_WwHZmTNoBaQsilQPNR11gFO074bKthn8URuyF-8hk4Net0D6X0F6P0aiymG21qIKWheOymlgFLtqDPpXNxFiM4IcYqQyowiVdQn3QKHdXyDUuQdPVBfvVAYaPIGXsJgKHBqOuVdKdLEYy7YsmFvtQDWgemBhpqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلید صعود ایران در دستان این مرد است | آیا کی‌روش دوباره قهرمان ایران می‌شود؟
🔹
فوتبال دنیای غریبی است، حالا با توجه به نتایج به دست آمده و رده بندی تیم‌های سوم یکی از کلیدهای صعود تیم ملی فوتبال ایران برای اولین بار به مرحله حذفی در دستان مردی است که سالها سرمربی تیم ملی فوتبال ایران بود؛ کارلوس کی‌روش.
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3225973</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/663826" target="_blank">📅 11:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663825">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سفر آیفون از ۲۰۰۷ تا ۲۰۲۶؛ داستان انقلابی که هنوز ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/663825" target="_blank">📅 11:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91ee4ddf11.mp4?token=FgjcqB4DyDBXEZYyiVimIPZG8XnQieorUP5-7Xtd7hxfY9hQQw9MB95y2tPzmWh7iNeHjfksENdPHQmPUFSya1Enyd2hmBWXJGa9H6Zg_A2iIBZzSmymEfUszhUAKtayryOZO1q1Vt2SoAmYBSZ4fnrLhqR079sHkvlwQBMtGNZMMfJMSRybop3PlVwnfn4trHR5GGelEUG7z0AY3Ayl0dWPvq9TOiI3IvTMtq9lqphvGnxn6MKa5C1i7muU12KZxNb7AtesvbTOO-UixvPteDWM_E6pT_ySRnv_OrTw1cIvFBv5Lt7qIb6oi_gztjppcP1-f6jTXHlLkK_VR48lZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91ee4ddf11.mp4?token=FgjcqB4DyDBXEZYyiVimIPZG8XnQieorUP5-7Xtd7hxfY9hQQw9MB95y2tPzmWh7iNeHjfksENdPHQmPUFSya1Enyd2hmBWXJGa9H6Zg_A2iIBZzSmymEfUszhUAKtayryOZO1q1Vt2SoAmYBSZ4fnrLhqR079sHkvlwQBMtGNZMMfJMSRybop3PlVwnfn4trHR5GGelEUG7z0AY3Ayl0dWPvq9TOiI3IvTMtq9lqphvGnxn6MKa5C1i7muU12KZxNb7AtesvbTOO-UixvPteDWM_E6pT_ySRnv_OrTw1cIvFBv5Lt7qIb6oi_gztjppcP1-f6jTXHlLkK_VR48lZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی که مادر شهید ماکان نصیری برای بازیکنان تیم ملی ارسال کرد
🔹
ماکان من برای مدرسه از خانه رفت اما هیچ وقت برنگشت.
🔹
دعا می‌کنم شما با عزت و سربلندی برای ایران بازی کنید و موفق باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663824" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c42893670.mp4?token=umqv8CvjVIA_TvhIve9pXNN0KGiDapzBrqvRGWKUNUGW5jW7_6ux3-kEKE-0fpAtM-BpPJZKG9rf0oMK6RclH1tmitR6Hv4kTtploLXGMyOcCAGghglRZZ_hZGP1QLpzbSK0r_CvNHggS-C1cFevSSrtj_1i6S5kZuLzrs24XW6j6aFMsf-ZNM3BATzFP_1Ryjg4uFACy-_M2CezHdss63tM1iNwBLwd5MWWNB4L8XlINJK-c4HU975KDU1MCGqYjIaxPAOVrXgVeHTmrVDIsmm60-lM79d3Spm8rtm34kSfCe4D8MEG7Jk9LPLGyegXpJk1ZkfmZpK_yrxjRIDiJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c42893670.mp4?token=umqv8CvjVIA_TvhIve9pXNN0KGiDapzBrqvRGWKUNUGW5jW7_6ux3-kEKE-0fpAtM-BpPJZKG9rf0oMK6RclH1tmitR6Hv4kTtploLXGMyOcCAGghglRZZ_hZGP1QLpzbSK0r_CvNHggS-C1cFevSSrtj_1i6S5kZuLzrs24XW6j6aFMsf-ZNM3BATzFP_1Ryjg4uFACy-_M2CezHdss63tM1iNwBLwd5MWWNB4L8XlINJK-c4HU975KDU1MCGqYjIaxPAOVrXgVeHTmrVDIsmm60-lM79d3Spm8rtm34kSfCe4D8MEG7Jk9LPLGyegXpJk1ZkfmZpK_yrxjRIDiJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جورج فلویدِ جدید؟ مرگ زندانی سیاه‌پوست در زندان کانتیکت
🔹
تصاویر تازه منتشر شده نشان می‌دهد «جی‌الِن جونز» در جریان مهار خشن مأموران زندان کانتیکت جان باخته است؛ حادثه‌ای که بسیاری آن را با مرگ جورج فلوید مقایسه می‌کنند که جریانی عظیم را با عنوان جان سیاهان مهم است در جهان برانگیخت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663823" target="_blank">📅 11:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
صحن علنی مجلس، هفته پس از تشییع پیکر مطهر رهبر شهید انقلاب برگزار می‌شود
گودرزی، سخنگوی هیأت رئیسه مجلس:
🔹
در جلسه صبح امروز هیأت رئیسه مجلس با حضور رئیس و سایر اعضا مقرر شد هفته پس از تشییع پیکر مطهر رهبر شهید انقلاب، مجلس شورای اسلامی ان‌شاءالله رسماً تشکیل جلسه بدهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663822" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIrv0XLV7VAZNw1UqZ7ou5qKT8Nn4ulKdkOzBX29VJdxdXaS9P0QlWz3tsH_LB2Gx_2YH1tmwBzo51EXMpBMZC1zSv2UlAt0btzFb0BtRApwP1yggJakQX94rXGIHxWVMWxYbVvyC_k8BkdWlEnT-HCtcG5tyEE8L1aoNTK3m4vmhFFJi-op5oZ2VwCYrEGlTt8Q4t6AhHqpa3oplMnRYjn4DXeKksBUupCIzP0FjzjKXuC87jmTrjzulVb7vCSEEFJqdq6QyQv0Q96cA5oCM5U7dJo-awPhe_8knBdScxlIuxIvpoa-QvaKIX9TdOpuJBKTLWm0or2MgPw02gQ0Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست جدید شجاع خلیل زاده: «شاید خیر باشد و تو ندانی به حکمتش دل بسپار...»
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/663821" target="_blank">📅 11:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
صادقی، معاون قوه قضائیه: در حقوق عمومی و از نظر شرعی، منعی وجود ندارد که زنان موتورسواری کنند
🔹
دغدغه خدشه‌دار شدن حجاب هم صرفاً به موتورسواری مربوط نمی‌شود و در هر جایی ممکن‌است که رخ دهد. اگر مجلس قانون گواهینامه موتور را برای بانوان تصویب کند، قوه قضائیه هم موافق‌ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/663820" target="_blank">📅 11:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_bXCXeXXUqfuQ1ozVmvr7kHB-DrRs1J3KcJBcLc_xh_wBWfZzxVg5iP0SCfhhkJDuw-aLkpmYnLJS8y44IA4ZbqC46oB8vfOMhRyXikaYqR_29SiNIVFerZNxrXjUyaat-bWYl0hSZ00uR0joJqiCgYx41fRacNBzK4RpGTiAoPOuASmTIJIgRoyMSiF28twdLoQTu8WSPORLPHVN8a4Qk2nnXlTQWolWOGTaKG4bsOFYSkyMDbZ5QUBeUFty8HxdJu43JXLVSMPSaCzYCRGPKiHvCcbc-PqZRX-_Oze4qA0W2H34VjJ2WUJfmnnLn4ON-SOmrZNTibfU5OHDjqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف بولتون ترامپ را شاکی کرد؛ او بسیار احمق، نامتعادل و دیوانه است
ترامپ:
🔹
جان بولتون، نماینده سابق بسیار احمق، نامتعادل و بی‌مهارت ایالات متحده آمریکا، به تازگی به گناهکاری اعتراف کرده است!
🔹
اودیوانه‌ای است که فقط می‌خواست دردسر و جنگ به راه بیندازد و باید با او برخورد شود.
🔹
بولتون اقرار کرده بود که از اسناد محرمانه نگهداری غیرقانونی می‌کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/663819" target="_blank">📅 11:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663818">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
۸ کشته بر اثر عملیات ارتش پاکستان علیه افراد مسلح در بلوچستان
🔹
بر اساس بیانیه این ارتش، عملیات نخست در خاران و در پی شناسایی یک گروه مسلح انجام شد که طی آن سه فرد مسلح از پا درآمدند.
🔹
عملیات دوم نیز در مستونگ و با هدف مقابله با یک حمله انتحاری احتمالی انجام شد که در جریان آن پنج فرد مسلح، از جمله یک مهاجم انتحاری، کشته شدند.
🔹
در این بیانیه همچنین از کشف سلاح، مهمات و مواد انفجاری خبر داده شده و تأکید شده است عملیات پاک‌سازی در مناطق یادشده ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/663818" target="_blank">📅 11:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEOxww9zQxg7uTxOmnc54qVU81NGCd91ktGLsyiCMZ5oER-4uHeUI1w1jIpgEVO60GyNfKl52QXDyVtMqwuqbjpPfGiAYGQD8OPSOQhLlvj1jDjpP5qVTxUXhM_IhNXvn7PZHUdz3t3K4x8w0IOheombYYMrDq1bmzhoZNmfbSE91Iz2EIDdt4mXPD-TLMFsTIFT6NHmaYqTQKzlWtxv_x3iNaiTN5rjAW5M3B26lqpKKJuyQu2GS-2FXBnL-JjsmdbOJs0sMICJHX5b4E1SjVwww6xuEIuBbtWdCa9TrE8GziVDZMlQjgSo5EwY9ygGxJnoRULYLPJ4cHaWLTg4AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام تیم ایران از رختکن سیاتل به دنیای فوتبال برای اجرای FAIR PLAY
🔹
از ایران آمده‌ایم… از سرزمینی که هزاران سال، شرافت را بالاتر از پیروزی دانسته است. برای ما، فوتبال فقط رقابت برای نتیجه نیست؛ آزمونی است برای شخصیت.
🔹
شاید بتوان با هر راهی امتیاز گرفت، اما احترام را نه. شاید بتوان از یک گروه صعود کرد، اما از قضاوت تاریخ، تنها با جوانمردی می‌توان سربلند عبور کرد.Fair Play یک بند از قوانین فوتبال نیست؛ روح فوتبال است.
🔹
سپاس، سیاتل… برای مهمان‌نوازی‌ات و سپاس از همه ایرانیان… که قلب، صدا و تمام وجودشان را برای ایران به میدان آوردند.
ایران، همیشه سربلند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/663817" target="_blank">📅 11:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxvqVigDgv9XFRDvV_2Cf5_2lp-dLN1LBK6AKoMcvB6r-oXggqpNJsh0plzGXSoYh6MbKoiB8RVk_micFz19apyPe5UBGJ1eZrI2ndYZIYhHbER3hTWMsoP0s9Rs6lwLXBnPnGNyo6wfnDYodCbPDNlsUX2GB4R3lOln5k-128EqJuSvxKJPBKlN0WeiV2uyP7BvXIlNUtNyQtNpyADRCIdw3CHDjAJKhIpmsptnrpuIvm-tyI_0Dv5FLsW3oEy7FcDdkKKXEx5z8mdZdRrRExbaTceNb7--W_yTIwjNONRK0QcqTNAy9GHrDtrKRx-oF5e7SXbzJLwfw1FqOU8OrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نبویان: بعد از حمله دیشب، هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/663816" target="_blank">📅 11:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663815">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فراجا: آخرین فرصت بهره‌مندی از معافیت سه فرزندی و بیشتر تا پایان شهریور
🔹
آبونمان ماهانه تلفن ثابت ۴۵ درصد افزایش یافت
🔹
تمام خدمات حمل‌ونقل عمومی تهران در مراسم تشییع رایگان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/663815" target="_blank">📅 11:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663812">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtqn1oUTjX2wIt6a7LbM-Yzcdd49YOq5xKxspuYThq3Q5u0QwDzeoThAVfjr9rqPL6X9AimnonXRX_NlF78doFRcVTIWA8sqnE7DNakZrY3ToedY1Nui4isg0uonik-LZ7nlvaA1XQCxbxuZzXbM8EMEntSkGtwqYxY6nJmH7WzZNE09HwqfrLDrhOdkx4NViE6_GR1PR82EjQSZf5IMx1OKlaDOeag0HLZVq5CJ9-WNn0xzo4FrdyUGxGYON8WItZqE_5pJBssOt3UyXkUdxiuIqzNKMCEJD5cP8wvxLDKUcY13dQFEU-3UFcdbOH_OH9GJe0B6KMcWf0v0nW5sjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از قاب تلویزیون تا جام جهانی ۲۰۲۶؛ نبردی که واقعی شد
🔹
سال‌ها پیش، در انیمیشن «فوتبالیست‌ها»، تقابل ژاپن و برزیل فقط یک کارتون بود؛ جایی که سوباسا و یارانش مقابل غول‌های فوتبال جهان می‌ایستادند و میلیون‌ها نفر با هیجان آن را تماشا می‌کردند. حالا در جام جهانی ۲۰۲۶، این رؤیا روی چمن واقعی جان می‌گیرد؛ نوستالژی و واقعیت، در یک مسابقه به هم می‌رسند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/663812" target="_blank">📅 11:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663811">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeUBfSi1Xd4Bx3pcJm0MboJUzWBR6nQkBJ6igRmRW6vH6dbsddXEKTUEXA5-NR-711WZBT73PcwyGIZ9TPaPp_1Hi_b1WadjfdvZ0IgpHmkAbDGjPVnsZjB6KolbajkV-oB2fhhnrG_SkhOuDUdAJK4xOVw3xMD3TWyh4sBM8LxbYAletHMxC7uTTK7yzNKUJhjzBIP5bAkz6TueFVoP_EFtXyegoK-rR_pW7mDBNBuYHzG4L1q93acBf5AGIFEmwFWplO4BUqRlKK0ScLAhhCNEsbqTd_nLynwvZS1InXoyTrGp_5pP_txDnm3810VM2sGzYgC0PMf8Z0DUv76DZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکن رکورد دار رکود در ۱۴۰۴ شد
🔹
تازه‌ترین آمارهای بانک مرکزی از رشد اقتصادی بخش‌های مختلف اقتصاد در سال ۱۴۰۴ نشان می‌دهد بخش ساختمان با ثبت رشد منفی ۱۵.۸ درصدی، بیشترین افت تولید را در میان تمامی فعالیت‌های اقتصادی به خود اختصاص داده و رکورددار رکود در اقتصاد کشور شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/663811" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663810">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c64b94b7bd.mp4?token=KSphOchZSHg9sk2PneQUfZmaspUZv-wbRV8HBiKStFoasFHZ9VqF0PglUGUX50rc9e1ZFRb70pzL2KMeUG9CH9hfMDwt2Ksen0bZCZ1eVCUo4vLWvGHjmRkZBxPvvSzepqxQN_kTg5Fltvgu42S8Qu1RXiCNkHbQ_dwouTwdFtdcAS91t-wYhqwrvSXFDMrMPEE1QlVivHYWs-PhhgLTuDrb4u3Y3-tCDM7H97vf0Krz7sqpdlr8Fa38bOfYqn7vkiUkOPN1UqzmzCkrV10td8Oyp0oJ4FNw1gSYCGj6h8vetMUoAhZSwz3JOnmWI68qeKWXYrAaihxoU1--60X31g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c64b94b7bd.mp4?token=KSphOchZSHg9sk2PneQUfZmaspUZv-wbRV8HBiKStFoasFHZ9VqF0PglUGUX50rc9e1ZFRb70pzL2KMeUG9CH9hfMDwt2Ksen0bZCZ1eVCUo4vLWvGHjmRkZBxPvvSzepqxQN_kTg5Fltvgu42S8Qu1RXiCNkHbQ_dwouTwdFtdcAS91t-wYhqwrvSXFDMrMPEE1QlVivHYWs-PhhgLTuDrb4u3Y3-tCDM7H97vf0Krz7sqpdlr8Fa38bOfYqn7vkiUkOPN1UqzmzCkrV10td8Oyp0oJ4FNw1gSYCGj6h8vetMUoAhZSwz3JOnmWI68qeKWXYrAaihxoU1--60X31g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من شاهد نسل‌کشی فلسطینی‌ها بودم
🔹
هوادار تیم اسکاتلند در حاشیه بازی این کشور با برزیل در آمریکا خطاب به کسانی که پرچم رژیم صهیونیستی را در دست داشتند شعار داد: فلسطین را آزاد کنید. من در غزه پرستار بودم. من داوطلبانه در غزه کار کردم. من دیده‌ام چه اتفاقی می‌افتد. نسل‌کشی در جریان است. فلسطین را آزاد کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/663810" target="_blank">📅 10:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663809">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a0434cfe9.mp4?token=U-8NR3jumzBZ5yHnq37H98_nNqGylMLglS0zffJIETerry8Vh9UJXKYwfCJr4ueYmXg-HrOX9CkR_fr-4eJThktPaL3DEUxwwdSMCKAy7P3qNoZF5LdWOTQwjFk8CK2lhpQWC3HDtJNfSb8XY7lptQddPKfBUYf-Dho2hgZJ2MDvuT8_Aa0DzBfTvsyO-UXSFliCGZfKvHeR-8wg5ZkKkej3kJOrt2Ygujsj_PJiM4RhV2OqChzJy8aJIzTpzasW9f4C_3iDb0YXcu_e2H8IRpeZ5R05eZ7zTVYVLs3N7m8CzhoIrhf7KBdmQorgC7Z6sFykjtYdDEvCg7PkTpWAXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a0434cfe9.mp4?token=U-8NR3jumzBZ5yHnq37H98_nNqGylMLglS0zffJIETerry8Vh9UJXKYwfCJr4ueYmXg-HrOX9CkR_fr-4eJThktPaL3DEUxwwdSMCKAy7P3qNoZF5LdWOTQwjFk8CK2lhpQWC3HDtJNfSb8XY7lptQddPKfBUYf-Dho2hgZJ2MDvuT8_Aa0DzBfTvsyO-UXSFliCGZfKvHeR-8wg5ZkKkej3kJOrt2Ygujsj_PJiM4RhV2OqChzJy8aJIzTpzasW9f4C_3iDb0YXcu_e2H8IRpeZ5R05eZ7zTVYVLs3N7m8CzhoIrhf7KBdmQorgC7Z6sFykjtYdDEvCg7PkTpWAXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
آتش بس نقض شد  به گزارش خبرنگار صداوسیما در سیریک:
🔹
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
🔹
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
🔹
حدود ۵ ساعت پیش چند شلیک اخطار از…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/663809" target="_blank">📅 10:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663808">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl20oCTfjyekFLUv8DHSkRt8qIxqjJ4n8n_gSRR6wcsD730HnxplnQA8FNxlBeqMHiMUfF_b3_aESV5tGGbyapTnv6wB9FKg7AAP-JOXNkHJ8zcEGcn9y3cpfxmF9J3WrPg2nVUD9caarACEYj3JuyxGm7pL9KaHEMizO_UqGFJnj7utpvnLEE8gcpLDTlTPxiE1ClBHeQO1afEHqM4Wog16l2uA2w0ef-RasVrjumHMbjtj-TVXEWVPcWXkj6n4MfDLi1EIyyBTVPa3z4SHwcih_lL0r7Yt1uo7SqYB4jSe0BLq0tOp4rEQIQ8htRg7FmLZj_Zyf33xdVym5CD7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریباً از هر ده نفر در جهان، یک نفر هنوز در فقر شدید زندگی می‌کند
🔹
آمار کل جمعیت تحت فقر مطلق در جهان روندی نزولی داشته و در سال ۲۰۲۴ به حدود ۸۴۷ میلیون نفر رسیده است.
🔹
منطقه آفریقای زیرصحرا با ۵۸۲ میلیون نفر، نزدیک به ۶۸ درصد از کل فقرای دنیا در سال ۲۰۲۴ را به خود اختصاص داده است.
🔹
مناطق جنوب و شرق آسیا و اقیانوسیه، نسبت به سال‌های ۱۹۹۰ و ۲۰۰۰ کاهش چشمگیر و موفقی را در کاهش جمعیت فقیر خود ثبت کرده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663808" target="_blank">📅 10:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663807">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_5ayUZ59tGbiiVbMV06EpdqJ1tt77lX6BcNTV0CHnyY0AodnAz71LZJn5J_MYECzP-DL54PyD3KMZfyKTt962zQGMoKiKkL-Xx3bt0ZaXmEarbHfLdq2j37-9G3BvUDhxsB62Bb3bVTFrc1ft2atmPzaLOTnKF0okoSGnMosBpDujNIHjMC1em7SyBy9JpohUcSaiA8H0X30i6AWVUrGGhIjEmp0cFJGZzoWdX-PfrQOa-saArXLgLQ_OOBRwrqrBidvnAwKyk4hDRTtSUYqSwZVK7tvg4u4I_NBVsQWmSj2lVcZKLGzLvnPi5LRd6AWaoJEXO11c1EuLiP6I-uuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این ۵ علامت را نادیده نگیر؛ شاید فقط چند دقیقه برای نجات جانت فرصت داشته باشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/663807" target="_blank">📅 10:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHzLjdH6bVzUxY8zMoVorhvWLLZ-pjw4411m7d8ibAul4OWTuaF6qfp5pLHGL4MJiCu7ywM7GKob-Aw0Js4Rx66g4nY8jTjLYsvxNV_-rbxLEmDgboefzAgyptftz8TLUjbBNQP5ep0IKjyvENMjo59tnTiIjqG9bXJJRRYDWas3Ox_beMlpgCoUVM4qE8WrA3NoJnrH6P_lhfrUjtd5CJO4sy2xUUqTq7iLjw-mvvFeBMTuAsSeZqo21ZeQOkV9k4Mdd-mWcsxweEGkKcv4Fi3FfzQkAJGuy9waJTw1MnmX6jc-x62M6XhiMxFSW46DFSMJfBcwsvTvU-EIGG8VUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره نقض آشکار یادداشت تفاهم خاتمه جنگ توسط آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/663805" target="_blank">📅 10:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a464775ad3.mp4?token=LjZ4uqLd7TcHzuTlk7IMCgXL2LuUCHMfeWRf-4t8L_-dt9QbubkxE0A2MyW9ZURSNJIU6YKvY6zbCXvnNwBywcGnZZjYHR7XOH9aRyTFjapyFofUy-iGkNVWvzEtANBlvA-MNdzzaEO5EwT0WwDUu-R1Uxp8PevVUFPZdaEuvXbBwCWZDuQ5qxEULkbbmzbp3feISvbNbrXYX0ilgYvA01nmMc3ZG0R-RIkyF6Yldf7gD1hHlocQizK3eGIiTv2IhCYefkVT2lIE8QG0YCpc2Tsg3HzAZXNhhsyNQc2Y6a-8tEEymze-TVZerII1emzQIv9Uv6nwt4mJMoadqAji1ZmOZq_PDGB-9xvjTICi1uWOhrY07-3sEurmFUu3GEZ8LyZH6ByikpkMmq5QtH4BFeJ9E-feY-hX7Y3acs39_10gnh6mvtUNVTg3jfBW0vMmGkdQWdfZ_sLeuE_PA9noeqduEdVqqr61UF6VK3ybx5-EWmZYWoV8aE7R4BaHMitaTgLxhSSGJtsJAgX7w4cNy-EKEWYWAWzKaAfSrB6g0Hd2jBdCF8DJQ4quLzplN_AVJLYlPI9iXUx_4AcTLssiJG9-yr5QwZUVGe7UctISXwvrhee0YSIZkB4P_6Ayj3od6_6jTdUHfEhNuxH6Jv8NVZl-3Tb1dFX72v4bXS07xMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a464775ad3.mp4?token=LjZ4uqLd7TcHzuTlk7IMCgXL2LuUCHMfeWRf-4t8L_-dt9QbubkxE0A2MyW9ZURSNJIU6YKvY6zbCXvnNwBywcGnZZjYHR7XOH9aRyTFjapyFofUy-iGkNVWvzEtANBlvA-MNdzzaEO5EwT0WwDUu-R1Uxp8PevVUFPZdaEuvXbBwCWZDuQ5qxEULkbbmzbp3feISvbNbrXYX0ilgYvA01nmMc3ZG0R-RIkyF6Yldf7gD1hHlocQizK3eGIiTv2IhCYefkVT2lIE8QG0YCpc2Tsg3HzAZXNhhsyNQc2Y6a-8tEEymze-TVZerII1emzQIv9Uv6nwt4mJMoadqAji1ZmOZq_PDGB-9xvjTICi1uWOhrY07-3sEurmFUu3GEZ8LyZH6ByikpkMmq5QtH4BFeJ9E-feY-hX7Y3acs39_10gnh6mvtUNVTg3jfBW0vMmGkdQWdfZ_sLeuE_PA9noeqduEdVqqr61UF6VK3ybx5-EWmZYWoV8aE7R4BaHMitaTgLxhSSGJtsJAgX7w4cNy-EKEWYWAWzKaAfSrB6g0Hd2jBdCF8DJQ4quLzplN_AVJLYlPI9iXUx_4AcTLssiJG9-yr5QwZUVGe7UctISXwvrhee0YSIZkB4P_6Ayj3od6_6jTdUHfEhNuxH6Jv8NVZl-3Tb1dFX72v4bXS07xMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت هفتم مستند احیاء و حقیقت | این‌جا زمزم ۳ ایران است
🔹
بزرگ‌ترین مگامدول تولید آهن اسفنجی خاورمیانه
✔️
جایی که روز افتتاحش، یک جمله بیش از هر چیز شنیده می‌شد: ما توانستیم!
✔️
اما امروز، وقتی ردِ تخریب بر پیکر این دستاورد بزرگ ملی نشسته است، یک سؤال پیش…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/663804" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663801">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZE-NvQpfkvVma1KDCTipVdP1fgvApUXTHZUku6N1UPYl6n9XXEuedEljpa65dWAzNhQsedyij8YmcyHxGL-q2aZyYWg6HXYh71ukHNLvSLBsrBexNda-XlafEux-SO-EvCPjRDjEFNADQT58m6-9W5tenbMDgRqFX-kYIh_IDFg6y0DfRkViacKFusirsfFuapPu_bfZjkEXU7k1bj9EKC74ZbOKsCp4UzagJ6_Gcc6sQJ93lMxRWGIdGItYHU-7DewmYKALJ3H4E1xoD8jLUHSRPHxdubp58Zm4trOo9O16y7qHx9_-oVrtTd_TtB2HkAYCsTAtEglPVpBjkXzilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOHTFR0xsj5ICseczTLdtsBToPqcAy1b7CV8DtLs9v7W8DZ4Bzo9RnxdKsiFvRG8V7UUiT9HY3F9Z30neacpdj6e3SKs-I59Xy6oSsb_YPXb_1RJqOIKyyFVJaR63yjlfmAmm8MlRL-LgnzEGaWuJErR8re2iPQbXtVpgVXS8koRneyg1WxW5SB4TG9dasl4HfnNHviCC9TMIDLNPyPH7TM9HGPZoYtAI0J3h_MMXQtu5ZI2U4GWEei8TbRi-pR612c6GjrZZVo69Nlqk1Q3YhJEb5SpPlUm4RlRFRgWyhud-vrajXsXQJb1Il69zq1Gtw4ITPh9KNJ1ErAex4b30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nk_T5GStV6TQ1foc-D9jeG4J_ZibDi56qorkXg45iz-1jSxKXO2hYCcKLx3tjQlWm7IaMFFpC-APNvZ7THRtZNzH0ZH5IBkZQuDU9bsoJpojHVppSMrCNWdcV4Sur-IRbvdm0ST8CUJiqOnZA-ySkmbuZFh7bLOgviuKHsN3VMyYfE2_eozV8v6B7OnzS5eMWKEXamw3ohfER0UM4tGF7QQF3GecwW1OYicpjPTMbwS7ANqA9-DZDomJcZds6mJvZYTfyAUxOYQpmfrtgMDCLWNn1gpqS5o-KO7A8VRUvSd9VEpvD1rPqoHfLbrVggyIjYfMQt6zMfzrEkR_PfTUJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصاویر قبل و بعد از حجم تخریب زلزله مرگبار ونزوئلا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/663801" target="_blank">📅 10:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
شایعه سود بانکی ۴۰ درصدی تکذیب شد
🔹
پیگیری‌ها از بانک مرکزی حاکیست، هیچ تصمیمی برای تغییر نرخ سود بانکی گرفته نشده و این موضوع فعلاً تنها در مرحله مطالعاتی در بانک مرکزی قرار دارد؛ بنابراین گزارش‌های منتشرشده فاقد هرگونه پایه و اساس است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/663799" target="_blank">📅 10:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYASwrIP4N8-fUtlM21-WOVJ-KSQBjIiZvmn2nFVPmvg2_gc34HU2aqEjmwuYYcCBAz9nszaafzgZ4z5YoJd2eA8jmZUVXk3RydI7WOvINXttoB_A8R_gBm1CknaOUDgDBBEeVCViuP0UGL5FllWf_lPWQFYBoWB3EZ10-8Iiy9YmWK7Nw0YDUkvfv7X_dpbF7y2TD9NPceADaV36cXDWxAXGc1ZOheuWDH-29g_ww_7-4TGXFm9BYPKOjJ7zZQ3L04t994omtbKEpPdHXd1mdt42g81YK9qhfxOiyrpRF0NPGYSDa1iAYqfcK3xxnuypxGm1Vqi_NoWzSiqcqOraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اشک‌های رامین رضاییان و حسرت از نتیجه بازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/663798" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663797">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
مقامات امارات مدعی صدور هشدار در شهر دوبی امارات در پی احتمال حمله موشکی شدند و در ادامه توجیه کردند نقص فنی در سامانه‌های هشدار اولیه منجر به ارسال پیام‌های نادرست شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/663797" target="_blank">📅 10:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663796">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxR4fgQNxBJlucAt2yxbLHDzOTAtPvkHAr9a5OXMpVVeXjMe46mgPyXAHLCIZM-vf92iGTiD1t7lzdJIckB7OZj-A6w3ZS-q1n1yQzuT_o2pC00qchTcPGPg92hGStnkFbCcvs0KAVgmD31ysaBTUlDKTh5xVAmVkNWwAAMBFGTm_shqveysdiBJEylAZ3edVetRdLu02jYPAEX1Ze8KrJnk-QDj7Sp548jEkHZqD0XuyB0sY6JczYGf9i1KELKsMrNaSZlIVvVrfWZAQFhzYOfBoSLWITqzqcvPdnziuJvwwxa2XdvvNQUjr6XwefOGlW1O-FbKx7-uFp5PkEhreg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرکز آمار:‌ تورم نقطه به نقطه خرداد ماه به ۸۸.۶ درصد رسید
🔹
تورم مناطق روستایی در خرداد ماه نیز به ۱۰۸ درصد رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/663796" target="_blank">📅 10:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663795">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc9103364e.mp4?token=SWAfg168zeCD0d5YDCPDKqar344LaVPN0H5ixB1NUP7EyqvVzWdvKRYOwKnLpeYksz-7Wk8pNGtx2Hd5lCf2UMxmAiB3OGBsdPzcV1mCarnIJIeJqZdh7W3TddinmvO6_n3gMWejqieBRfKd1ZzEty64kZJFuwwtrtbtOXHVcQ84XpSGmGcm0N2pVzOTGpS5Kq6JV0iFJ3YC8gmx-yWJRxxYoHTGA5eFU3GZ4nNcz95EcgrukMBnkOkHXrg4C8mcf5d9sJvuMcpUjU8VY3AUq6xlPpVw2XIjSkVLCSpgp98GilP2R13IAr1xJ3Hb6B8SpqViVeYqdm6rRg5IlhVigw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc9103364e.mp4?token=SWAfg168zeCD0d5YDCPDKqar344LaVPN0H5ixB1NUP7EyqvVzWdvKRYOwKnLpeYksz-7Wk8pNGtx2Hd5lCf2UMxmAiB3OGBsdPzcV1mCarnIJIeJqZdh7W3TddinmvO6_n3gMWejqieBRfKd1ZzEty64kZJFuwwtrtbtOXHVcQ84XpSGmGcm0N2pVzOTGpS5Kq6JV0iFJ3YC8gmx-yWJRxxYoHTGA5eFU3GZ4nNcz95EcgrukMBnkOkHXrg4C8mcf5d9sJvuMcpUjU8VY3AUq6xlPpVw2XIjSkVLCSpgp98GilP2R13IAr1xJ3Hb6B8SpqViVeYqdm6rRg5IlhVigw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاق جالب بازی الجزایر و اردن؛ شو نوری با موبایل‌ها
🔹
در بازی الجزایر و اردن، هواداران با اسکن یک QR کد روی نمایشگر ورزشگاه، بدون نصب اپلیکیشن، فلش و صفحه گوشی‌هایشان را با یک سیستم مرکزی هماهنگ کردند و یک نمایش نوری جذاب روی سکوها شکل گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/663795" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663794">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poglgd8uaUUsqktJdzhPJwoX_CanJ-N9JkbzzA2wHQHfmlmVmbsZk9g8vH3uwVUj2hgNAQPbqTZvvlEd9fWpIOSYvKId6vY2E7PJ_Cwf-nFBKOBW6NOr4PIaNlDEiP0RNEk7J1Co2wMLn1GNoH4HfzYtVG8kjdbwpIbBGfBsG5eMwgVI7FO2nSQpjFVm-qkdg2GTuC9eUodGofjnSzo9s5Bz4bCDYV1c6FMkbYqs3ZsZjNTJQDnLZH1gCMSu45wIPHuv1e0gpTypvrXFokrprlMkhX3PqwXN0zLg1ONLVx7JAeTCEX3hepZMybXyKBEKx7AIaex1k5QSKYlNl3ugmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا بعضی‌ها خونه‌ موندن و دیدن سریال‌های تکراری رو‌ به مهمونی ترجیح می‌دن‌؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/663794" target="_blank">📅 10:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663792">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lanIxM79pQxIazgOG1kj1u9JP49hb1OVxjIuqguXUiXBP5e8aQsr_W49yJIf2VVv_MtKi3f3sBhMTSyej-mRN5wKJU9SlZOdXz_UtZml2xikP4LQskU8pK6dNMG5U2Nr-ZOzEkaJuX6-PdkOXkODw69MQiTOLW9xmjHZPW6PaREPMaA2iCK4ZQeMuIFuiFNdW0i4zksBd1Uc_oriIht-sJCD_7oib98GnywR9zY8C_5XfLc-n2MdmGvaSaW9PskNvXCOKVJaU4neUj8MxG0u71tFz_ZEI3xrX5DmBdKLLCLv_K0oXpZXz7lj1M0mjM4BTlkYm0aNEx6T7mFqTOIwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
🟥
🟥
🟥
🟥
🟥
🟥
⭕️
شعبه مجازی کافی نت مرکزی افتتاح شد
🟥
یک راه حل ساده برای کارهای شما
✅
فقط یه پیام از خانه یا محل کار، بقیش رو بسپار به ما
✅
⭕️
انجام کلیه امور به صورت غیرحضوری
⭕️
✅
انجام کلیه امور نقل و انتقال خودرو (تعویض پلاک)
✅
درخواست صدور کارت سوخت
✅
وام ازدواج و فرزندآوری
✅
وام ودیعه و کد رهگیری مسکن
✅
انجام کلیه امور مالیاتی
✅
پاسپورت زیارتی
⭕️
ابلاغیه شما رایگان دریافت میشود
🆓
👨‍💻
کافی‌نت مرکزی؛ جایی که کارهای اینترنتی شما در کمترین زمان انجام می‌شود .
🟠
🟠
🟠
🟠
👇
👇
👇
ارسال پیام آسان در تمامی پیام رسان ها
📱
@Cafinet_markazii
📱
تماس:
09388780700
📶
09216800950
📶
🌟
«یک بار مراجعه، یک عمر اعتماد»
🌟</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/663792" target="_blank">📅 10:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663791">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcPS1yfMPhPxQnBOOksG7xqbZW9XyfHjy6jgCPeFAjYJfBNtL7ANMefiQtK6Szg7FsTsPOTQI8lhfUBIlnF40_C320eoi9OnqGmMAkmm86k5O1ChEtXe-k7jcDoZxpbSccXv3ocJ0vLdCo9qOygZnRIhmLk-X26hb1JEnIgadXIQW8ISmasBTv5NTRoXchCy-npnwe1YnX32grSVRAVZxXN3SD3ELK3goNpdPh-V_Ap70PCmrdw247ecSvLLTZbvta-EbrQCsrq0ZWFHIGbiAXVWDcaa_H8Lp6TFQtspyozs-B4vBVHNuhqmb2f8AvKJ6R_MtHWqv9yamZDbHGy4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا گل ایران توسط وار رد شد؟ + عکس
🔹
از همان دقیقه رد شدن گل ایران به دلیل آفساید، کاربران بسیاری این تصمیم را نادرست خواندند و معتقدند که گل وقت‌های تلف شده ایران درست بوده است. اما واقعا گل ایران سوخته و داوری به اشتباه آن را مردود کرده است؟
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3225956</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/663791" target="_blank">📅 09:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663790">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fcfaf70cd.mp4?token=ORSaDUxJNbfVgKhxHGaw3gcsPHvN-8JO9YiQ3BXJbuRcuVqfj6oKVHAjeZ6Q8FYiI7kVMzwwymtAkd0HJZl0BBXkn79grchdbfLikTnymzORx_6G7FvZLRO0UbY2i3JRfOIwJ0-W89-94ILUEAEYZGIA2eM_fL3UkfSKOf-5YZtkCDP6AJl9Hg3f3gbBoE3AvQRhjFNuBvHZ_WQfSPq1XU7STwMfDDpLHOz3spv0pZlKe2QSg8WZxDiqQesaZP_IjWa08TV1sx1AiDXEJ3GMmbmw8s7KraG888nTZTX3nnUm9lYjkab61IKhtF9ASMuJS9wsH87xyB5tusyu1z0lhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fcfaf70cd.mp4?token=ORSaDUxJNbfVgKhxHGaw3gcsPHvN-8JO9YiQ3BXJbuRcuVqfj6oKVHAjeZ6Q8FYiI7kVMzwwymtAkd0HJZl0BBXkn79grchdbfLikTnymzORx_6G7FvZLRO0UbY2i3JRfOIwJ0-W89-94ILUEAEYZGIA2eM_fL3UkfSKOf-5YZtkCDP6AJl9Hg3f3gbBoE3AvQRhjFNuBvHZ_WQfSPq1XU7STwMfDDpLHOz3spv0pZlKe2QSg8WZxDiqQesaZP_IjWa08TV1sx1AiDXEJ3GMmbmw8s7KraG888nTZTX3nnUm9lYjkab61IKhtF9ASMuJS9wsH87xyB5tusyu1z0lhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رامین رضاییان با بغض و گریه: می‌خواستیم مردم کشور رو شاد کنیم ولی بدشانس بودیم/ مردم ایران ما دوست‌تان داریم و فقط می توانم بگویم ببخشید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/663790" target="_blank">📅 09:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663789">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a952300921.mp4?token=iPmY7semxR7cMaaf91mfDhLsrwU5wbzgvvg0uULwm_L442S4fEWc7IlKXWlkLNfcJvgJO4tzc_WzlBMK5BD7TLw_u-lvSDbSapBd6IFFseqbAEr4YgGqodCaOJTGZdjGzKQ43rPeAathSFRUbbcuDWNMx_42N2VPiXIMGmOPghLFPmWwevgmQ_Ij30asPBuujFaycBGnbc9oYEJG8CaoPPvMpNCCTIz8cDEcnf82lo55cahXRK45dLvVAjHGzrMEBdLQOrZKL9Av-sc1wI7C_e8vYI5bYJ1YGc8l8S1IK0BuCL1oOg1DfjP8_2fSlhpQn-Vw0_sAhwImqLPKNKYaUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a952300921.mp4?token=iPmY7semxR7cMaaf91mfDhLsrwU5wbzgvvg0uULwm_L442S4fEWc7IlKXWlkLNfcJvgJO4tzc_WzlBMK5BD7TLw_u-lvSDbSapBd6IFFseqbAEr4YgGqodCaOJTGZdjGzKQ43rPeAathSFRUbbcuDWNMx_42N2VPiXIMGmOPghLFPmWwevgmQ_Ij30asPBuujFaycBGnbc9oYEJG8CaoPPvMpNCCTIz8cDEcnf82lo55cahXRK45dLvVAjHGzrMEBdLQOrZKL9Av-sc1wI7C_e8vYI5bYJ1YGc8l8S1IK0BuCL1oOg1DfjP8_2fSlhpQn-Vw0_sAhwImqLPKNKYaUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به اروگوئه توسط بائنا
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/663789" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663787">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BW1090oJEs26AQ7b8V2-Vb6PDX7FZNa4CC-dQm_yM80D9Jhr44n6ggjVrsV98ax5IlRTgwM4RBccfTG9R2514SwVGl_KTcMuKr_0ltmQJ33u6Ph1h7WHHJJvbS2nkeR4sTDGId_1DPRUDwK1kAFWZ5mA9yGKPk0mefxWm0lBi4kvxG68ze-NTIqHHETtjk-MTeW6vLg4XBcFtpv-VTEz8TYk15llEQL3R8ZlckRflxyHIyrf0uowRspN3TmJlCkNaDbJOrGIq2iDwWRHaCL-1lL_rQCw-sl_adr1f2P_1NGNNRr3h0Re16QkdVVjz8Sf31UdhXiOa5el1b41eqcBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در صورت قطعی شدن صعود ایران به عنوان تیم سوم، ملی‌پوشان ایران در مرحله یک سی‌ودوم، جمعه ساعت ۶:۳۰ صبح به مصاف سوئیس خواهند رفت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/663787" target="_blank">📅 09:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663786">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/69803c621e.mp4?token=n9oT7gomkmCXYJ4BswhnBQcHzCQxAFI6sVZPxsZZjThu3G9Uqh5H0RBix4wcL-o5sNV0nK8aSgHsx4dRf77cM8h5rEp17T3LoBp2UvocGL_R1c9tdMBbM1SgqEbcSUDpltoaoHlEOUul5GUlv3eI1wZP6XZjG3wuZlp8m8k4uSFhmdo3FccgV9wcXhyPbuUN-62XbRQcnrMUPu8qwtp0CLUjUquVsvRUHiCjoSzjdRFJryh3spZ4CIuHe607Je3bY8KkvzpJwCsqrLXnnDbZWmCawZdUHyx4W-csXmCIgGFtEvR6_pbGEdhqdwyzZDtm2v8prP8MMZat01uWsruL8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/69803c621e.mp4?token=n9oT7gomkmCXYJ4BswhnBQcHzCQxAFI6sVZPxsZZjThu3G9Uqh5H0RBix4wcL-o5sNV0nK8aSgHsx4dRf77cM8h5rEp17T3LoBp2UvocGL_R1c9tdMBbM1SgqEbcSUDpltoaoHlEOUul5GUlv3eI1wZP6XZjG3wuZlp8m8k4uSFhmdo3FccgV9wcXhyPbuUN-62XbRQcnrMUPu8qwtp0CLUjUquVsvRUHiCjoSzjdRFJryh3spZ4CIuHe607Je3bY8KkvzpJwCsqrLXnnDbZWmCawZdUHyx4W-csXmCIgGFtEvR6_pbGEdhqdwyzZDtm2v8prP8MMZat01uWsruL8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج جرم از تاج خورشیدی/ ویدیوی منتشرشده توسط ناسا خروج جرم از تاج خورشیدی را به نمایش می‌گذارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/663786" target="_blank">📅 09:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663785">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyPU4P6oMUJN_nFGh3bfJ5a4ozt1IOLCA0DEQ_rUDIBKGGugBlBL-Ky604Vgf7R-WK5nVB9wD8ESaGhXt4fwMzx_1VF5it1_4IzOYGE1FmXQ6WWzhWDezLgLHBuR_wM30DfqgrNGd74yNchTPPWl-ETBISio3-stLMWWInlmSpF47QP4hEaF-eORuMrQ-eo8lc7e-maOzYf1kWDGnyhK67CRhUQNgj6olBOi8oaLLpwB0h9zvlqBDqmy25nkeiG4emuqnuE3tFPbuhYhMmTWa6yY99g46PoYIcodd5jXO9c9KRIpA9IdjRj8Bqo06W3P7FRENZmttwNgyNw7zOOfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شانس ۹۲ درصدی ایران برای صعود/ برآورد سایت اتلتیک از احتمال صعود ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/663785" target="_blank">📅 09:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663778">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7tIvhiIJCBvdlqE7oDA5NH0ayBkSt31LBoncD7dIyPdq0bEnfSnWWcAk15b1uL-W8xFDHUwwFGGOVZECFSS0uJMNSmL9_Lyizs3_MdHhwLKYfIN2u-QXJhJea18C7ANvbDGdUsnkPUpe7lWtOk72L28BHUYyEw0xONUFexMKY09K_8GlGZnwvzwBhrTHOAZsBEexVPom1XkBxM6eKbqG_QiGSEU9jtF57GLx7kN-M3ggkj-7m3nJ8NvPb9gqJVpySDMXTGlUWSvkiSWhg7in6akQvtvZVIsW6T1XloY0XOTBbFgJwcdzR4I1aPJ0QBmRxXeRbgRfFHFC82LjHMtAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVh1_jhohFA1wOtqCVphjV4qlcKxppOJDyyAfkuS1sl3qI3f4rGulEsiZiuOdhjB1OtsO5REf3x1QqpfGo3JgWDCT2mAZ7gEe33Rtsnp8w5ITq9i_qh5uJnk_nwOaWAOdGxC210QgKQZsT81lIV_w5eMcyTqliPTawixDx44wbtolF9X9g923HsorfXIZmat8dPHmQ5KpRJV9daEb2gCEngABIzM4eKyqgZP3Ll0-Hsro1TjaKcA7yGf4YDdudG3ZO7QvOw9-jXsg4kQDGXaAwFXJ8aDFe7uCPzlLWmbq4gcnNrVBAS-vUXo5_y56iPxgXqD2PFnB0Vts4MLDY8QtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A10G0uVKzib0Q7fDODKYshmOAgcogMYXE6Olt8DxU6zrL5eselKsu7R7jAcPIkernNbk_vsKh1id2R65j_i1v5un-ZElK0H2jBQrNX3qwAn7e1bDh1SysAyg__wKdt2OWrjyjcQoKjPjWPNnTzIqwJchaaM2Ff7Q0Vtg9amB__kVg0Ph6Vs9mrZSIGhKtxGKWUKNzMjEA2kE-TqHPkS58oOICFJ6tq0LqYMQl8_7vaU2tB7j7yG8QHwOzSZyLffd15dJhTGGDdbHIW3GlM2ha73IyhUY8ayIYaOCssBdTmlGJJVYZMDqnDMFeASdyKC79he2nhf4crJs7yhV8zZWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hp5WDAo6AzpsbqSvbCQsBD4lSaunu9SR9UsXhbDsfCPVAQnQMoP37JBB-aYuo5o8YCGvmkV-1LloqOdP7tC3LCAPO5oD4kLjzwLa_DYZvtf0C5DH6lSjTIKVoaJXUieK2mnjiwmdfshHQXDqkkiS6hNKrj2xJHzHOHAOKxt12yyptI6irDdRnMZKd8ZRjCPEEmUBxp0oIMcapXgeZxUq7hVgAtHxyjoU166Tz-1tbX7PMPKvb3wYGyfI41_5lOOUbF4QrJFYci7NdNgHO3E_RFSLg4E_warcNn5qPOnjNa24WLE6qJQF6LJ_NAgz9LkwfOtj-oZrAwTfGtAkInXLSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfIy8GwGq-In3DosbnjdJr0vN15eoxCdrLy7brTQmK-4XzdWG46GS32CtF-TlWj_Dg14Fj4yE7ajO8qZ4EXBd58jDMZSb8ZSqJWS6Yy-QxezXGjZTpEMA8EfgVbirYq_kJ3YaDFBlGMh2pOLYuwvVH1lMApCYRrGVe-JNHbMg_jnfNhFM6_OnCHm1WlccJgJR3HV3LbvUoyf8zDEO7qcfY5Oa-1W24KeKb2L-30hHNT_UEezy2K7wlp2Z3VrGlT1CmGy0y4FQRbFf3EWbxmWw25YExRkDbVa6wzz3Vne7cANTHnAoHhFy1dCwj4FvHBpLfJJlR4uWcB6BmsItup-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wlze_yR-56jeRbFvEb0t7EMragVF0ajZOVWgFRj0MVUfak3Fph38dOl3mCpx1UC6obiWDL9V4mjLChc0HlnBiJjQTTQKjpG0JQHQo05MfAK6l3tpYLQVJIQ3RLN5_uEArEFZoqAVOgoZFq2oumaQa746sa0aA88cUqf4ShT9tWQNZQTFQxQ3xltgDO9DR41dHoFsukUSkLp3tBDDgqDZutzKP_-zzkwJ5A4LseU104rX5a6R38aRU5t4db95Jd_LUe8gB_tc5nMtS1CdT_-H8tq6cEjy1cKc6jafVnTu12DVn-jJOPBpiRTcT-MG8KFEQKbms5JPMr9HsOX-WdfLfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فقط یک فنجان می‌تونه عنوان «نوشیدنی ویژه کافه» رو بگیره... انتخاب تو کدومه؟
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/663778" target="_blank">📅 09:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663777">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUJBR1HToaQVpL0cydA-1Xz4iY44HYrA5uXKeAVh7Vrb2x7Sa56NFH18uzLEfRYL0cOWTFGIC2UYHJaIwivCMLSKb-2EieHiKF1cO_Mj3DTuyoW92cWWqhmFBXXnFVs65fr7PpIb22Nam0yjiXvJudH5q2WEzbMkJjmHfCZmcz8dbt5msByUb_dTT9zTfs9jkr0pskV-OvMt4yWan3OFlfyK2bMnQjQMlcSJKKUasBytdhoQp2oiXO1BEqz5W8LuUTNp7KFrXbDzYr8tVHG6hvNORLfMAAeiuEUHXSinZDl9WmzxzxpYERsmWCGns9u3c0weV7q8rAy78ot4oBY1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای قطعی شدن صعود تیم ایران باید ١ اتفاق از ٣ اتفاق زیر رخ بدهد:
1️⃣
. غنا موفق شود کرواسی را شکست دهد
2️⃣
. ازبکستان موفق شود از کنگو امتیاز بگیرد
3️⃣
. دیدار الجزایر - اتریش مساوی نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/663777" target="_blank">📅 09:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663776">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3b09b240.mp4?token=ZbdKETOdnu-gXgAx3wUPnkRN9TZDvFW77uQsb3bkGzwP-IncRN4kGZxHuMLEAZzLyDdfZ_P8Xw86tWuIqQ10bGRiptHK2FehIXYEybgdDXAfCh6e7vNgn9RLt3BVarfQrwNVytqimIdAACn2Emg-oaaOcvEEEn__AT_o6KgiFWHZwbwJ3Z_-EDK5KkNMWk82U7RK0cQs61ePdP3DD1qdOMPz7YVFNTvT0HKyldKCioDClZIpONo9py_rGyHfl0lR4nP7aO-GueIRuo3OIE5sBUh_a4c4-KRg9VDm9PwtjdDyWsWYC2I9vObTXaeaIKYEDqFlX_Ox1LH1kJWkoldgVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3b09b240.mp4?token=ZbdKETOdnu-gXgAx3wUPnkRN9TZDvFW77uQsb3bkGzwP-IncRN4kGZxHuMLEAZzLyDdfZ_P8Xw86tWuIqQ10bGRiptHK2FehIXYEybgdDXAfCh6e7vNgn9RLt3BVarfQrwNVytqimIdAACn2Emg-oaaOcvEEEn__AT_o6KgiFWHZwbwJ3Z_-EDK5KkNMWk82U7RK0cQs61ePdP3DD1qdOMPz7YVFNTvT0HKyldKCioDClZIpONo9py_rGyHfl0lR4nP7aO-GueIRuo3OIE5sBUh_a4c4-KRg9VDm9PwtjdDyWsWYC2I9vObTXaeaIKYEDqFlX_Ox1LH1kJWkoldgVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین سیکس‌پک؛ قابل اجرا در منزل و باشگاه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/663776" target="_blank">📅 09:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663775">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYMEd1D0f_UkS3WKAMznkkK2827Wtk5ev7UcBu5XK7h_0YLYR0w8nx4hQgYSnkoF9JR6KqYBn0tj6U-yZHSvTnMQRHTf4ph8Bgcm_LlMsRjDZ2CG01rEQPnQJEczSgD-yM7_O5VCqZaH5Jt9bjrYAgMTCbT80RZqfml7NctRtiug5_-xCv5WBTfQ8dxWbCc3xcQ5XFt4jCC3EYwN8O5Qb7iIigyQikRDXL2y3RyBUMvZWpNsV8kfCQO5kLtth81XwE5KiIfK86HFOL-TFS_bcHZqEhcYBstnKIxwRggzbSHGa4dHdBQS9oybw7SruYAzqKSANWnVX65nLMIT_iqIUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۰
💻
آموزش سواد رسانه
|
#آگاهی_رسانه‌ای
| ساعت ۱۲
🥛
معرفی اصطلاحات مختلف
|
#واژه_کاوی
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها
|
#فوری_کتاب
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/663775" target="_blank">📅 09:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663774">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570e6447c3.mp4?token=cmO71BnYmBesiYL4SnyXxZdyQ6uE2yzUm_inB9kAGvHbxIAlGWf4KKU8QVnxiC7VuEctF6BZljYCGq5hYt2TuLXBWvk-a7zT2KgHhhwtvo62-HrpV5Qj1mwGDmunDo8FJ9l7UB4ba-RKRqVbPpD64c_RHdVzgoYsLAosOTGDT4_siEY8fg2TZDhpHIdAj1g0vf2qli6bLBt6BqEM--oRiBS1ZrxufWklVx9IlshwHH8J9R-Diu7UR-21xaAPxW66GxcQEWHgry2fGnYWji3xpwCFYJLwjC6mNDsZx_XYa4o0LL2f7h6GGdZulGElNg9o-h6J5Z7d0-hF45FTKiuj4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570e6447c3.mp4?token=cmO71BnYmBesiYL4SnyXxZdyQ6uE2yzUm_inB9kAGvHbxIAlGWf4KKU8QVnxiC7VuEctF6BZljYCGq5hYt2TuLXBWvk-a7zT2KgHhhwtvo62-HrpV5Qj1mwGDmunDo8FJ9l7UB4ba-RKRqVbPpD64c_RHdVzgoYsLAosOTGDT4_siEY8fg2TZDhpHIdAj1g0vf2qli6bLBt6BqEM--oRiBS1ZrxufWklVx9IlshwHH8J9R-Diu7UR-21xaAPxW66GxcQEWHgry2fGnYWji3xpwCFYJLwjC6mNDsZx_XYa4o0LL2f7h6GGdZulGElNg9o-h6J5Z7d0-hF45FTKiuj4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد تماشاچیان هنگام خروج از ورزشگاه: فلسطین را آزاد کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/663774" target="_blank">📅 09:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663771">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In-z9_XCTE2sw3yQntpBIUqHLxwqhquU3Epk9DucNUCFGA6L9LsY_yU1RieV3FMA48Wk_90d5WIP3p7rlKbkFWMonVBDkJrNljxmgvxL4vhSUChHLwW9Kc3MV00NsI-9imXgdbGcPB_7r6OOYD7ZZKk8Zk0PZT3sfTCR-_upXCxtOtnBCIxRPcWSAZzSISigRxRF5MlPuFOWVB7V0n7LS4LanGfuI3Csb9bu_Lyc5vQbNtDLXCpaEWbrKZDFrtozJtB3zlAJL76HaFGMOOow7LE4WzVh4X3O9kYmQbffGC8bi4djSBUipv-IYrgY8LkaFrjs8fgeYbSTiofQXCbbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">《 اقامت۲۴؛ باتجربه در سفر 》
✈️
🏖
تجربه‌ای از دل سال‌ها همراهی
🏕
بیش از 20 سال تجربه
بیش از یک میلیون نظر مسافران
و پشتیبانی ۲۴ ساعته
پشتوانه سفرهای شماست
رزرو آنلاین هتل، تور و پرواز
همین حالا مقصدت رو انتخاب کن:
👇
www.eghamat24.com
www.eghamat24.com</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/663771" target="_blank">📅 09:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663770">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21bc126cd.mp4?token=Cj_Pw9Pw-4ypi6iLZ0PXjHguuPjqdAcMN8O-SnvtD1TYvytRmmq95yK_noGDozwuwBR6Pch9U2etAKkY5OWayNQI6VB5hsVulsNJMi5OltY9n963ZFxGScfgzEiwLBVCXqLzxPCG5SEbm-hMLrGD9c314bMlvBDicRbpoctut12i0o_zUp-8nWZoj6VeAnhOZRuuK5EHvy8a9TXdMjTrJbG2psi-mTLqgmPO76NIi7U1m88_NRWfsYhbFr9hHmHhIKvrcVKHruvsNLYHq8t3-9AapZpnji_W2t4Ad1E2MYHZANokmOvz0ai2Hzj9iLw3y-kkLtJn71YZ1j2IFYEJdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21bc126cd.mp4?token=Cj_Pw9Pw-4ypi6iLZ0PXjHguuPjqdAcMN8O-SnvtD1TYvytRmmq95yK_noGDozwuwBR6Pch9U2etAKkY5OWayNQI6VB5hsVulsNJMi5OltY9n963ZFxGScfgzEiwLBVCXqLzxPCG5SEbm-hMLrGD9c314bMlvBDicRbpoctut12i0o_zUp-8nWZoj6VeAnhOZRuuK5EHvy8a9TXdMjTrJbG2psi-mTLqgmPO76NIi7U1m88_NRWfsYhbFr9hHmHhIKvrcVKHruvsNLYHq8t3-9AapZpnji_W2t4Ad1E2MYHZANokmOvz0ai2Hzj9iLw3y-kkLtJn71YZ1j2IFYEJdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل ایران به مصر  آفساید اعلام شد
⬛️
🇮🇷
1️⃣
🏆
1️⃣
🇪🇬
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/663770" target="_blank">📅 09:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663769">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdTgMouohv5cw9N1yoGiOexaP4-Y9KFwFhdCxdOVY_oXvw5sxd5MVOkQf-aEaUhu8_UMi3sY5zaKyQBeHxe_vCWBGeVjkgAWeJK7GQnazSX4smGMhAAUAK4S6t4WLqcc65ppIfRtgB3NPScJ2yEfo6-C69HLY9WKQMTxNfkLKpCfPrKEoQMYiCF8ynSiNws4JHOvkKFsm3MC9k3fJwtZ7cq1QxOnFymQ3Bxz75JcxCw92xmuCvhp8H8DKx18KUomjVZ6FHMZeLCyOFwPn7qELBQ_HycLDhOze4bvQVYkDSKA-tEZLHB9GA63wfo1Jiwy5KuD3cIf4z1ocHXArTi3gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش مهدی حسن، مجری معروف بریتانیایی-آمریکایی به بمباران ایران توسط آمریکا و میزبانی در جام جهانی
🔹
آیا تا به حال جام جهانی ای برگزار شده که تیمی در کشور میزبان بازی کند، درست در همان روزی که کشور میزبان، کشور آن تیم را بمباران می‌کند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/663769" target="_blank">📅 08:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663768">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639ab0958c.mp4?token=Lc1TcJf-bSHi8AsJ5dw8IAhiM_5XqqH3Ey2dwiyns4c84dTM8VvpmcJBTSSoActB1GqkVZqPtc74Pv8Q50_gByWNA9AJ7zK5udwf_O1q75E8zRxyj0v0MWODDJPW-gl9RpCcEVWJz5t1ZlHyOeAJFATsLf-_tbdmQS6RW92iB9eB3DiexcDT2tVJDAElqEBb6THpmOtDtSl5Wwew2mKxqeNNic1iTWebKh2pMasIt7TDVA5Rx-grCPvIQR4h4qskGzc8kN7zY1VyB-P93CrRlBeWmANHJxcQHtlD4ow5krWAm4xP2F_qzzs5PWJ2I8Uiqxpi9IzFkORtpeQyw1GpIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639ab0958c.mp4?token=Lc1TcJf-bSHi8AsJ5dw8IAhiM_5XqqH3Ey2dwiyns4c84dTM8VvpmcJBTSSoActB1GqkVZqPtc74Pv8Q50_gByWNA9AJ7zK5udwf_O1q75E8zRxyj0v0MWODDJPW-gl9RpCcEVWJz5t1ZlHyOeAJFATsLf-_tbdmQS6RW92iB9eB3DiexcDT2tVJDAElqEBb6THpmOtDtSl5Wwew2mKxqeNNic1iTWebKh2pMasIt7TDVA5Rx-grCPvIQR4h4qskGzc8kN7zY1VyB-P93CrRlBeWmANHJxcQHtlD4ow5krWAm4xP2F_qzzs5PWJ2I8Uiqxpi9IzFkORtpeQyw1GpIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رامین رضاییان با بغض و گریه: می‌خواستیم مردم کشور رو شاد کنیم ولی بدشانس بودیم/ مردم ایران ما دوست‌تان داریم و فقط می توانم بگویم ببخشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/663768" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663767">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtP4OMFdnjPnBOoycUzYHBPR01NqhAliQx-whnG87lZvs0xyQfLliGH557qB3T6fSELZpM4cUllvzSfB9iiBpS4KB_u8tvu22Dnazk_JEigfqebhpmnPWkomEruIGZ8o2-bb7LJF3VHBHm5RPa4Ults7Mdq2vpaJPhbUWmS-CNAEbv3-_dIkoTbp6jGIOEsT-3vNI9q8h3egPZmAFuZ07yWfSLwyyeDwYCv0t1OarMpei7VOtVd70DySDVl9fPPCo7SUdIeZpOQasPXvC9655TGYt6myI3X94bpUpsX_LfRcnLYStdff65hUOyUj3LBG5LyZ4liimN9-LpYBXxGSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شوخی کاربران فضای مجازی: خلاصه بازی واسه کسایی که ندیدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/663767" target="_blank">📅 08:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663766">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ee7eabed3.mp4?token=Nw2sGw3nf9j_002AmR--w8Nt5Vr4lnDYi4ahJ6SftUCacnt4anJqZm_82crsTtTs7rVMis-8y4Ke_XQH5u36_4cm2syccn7356UmFqxXxUuMvuw5Y1UXNVqPFA1Jjv6K1IwqQdKig9wMsuwWd2xtyo16UuNUGwNGPZ_AsoLC8vAqNGQKZDzxJumC2leu3h4PgBk_q_yrTy2lX_7eeQ4b2e57lsRZijRrFamjtBOV78UgQxL86jeAvjUJZHO9L4qgNQopyzYZEC_0E0-Ot8-vk0TEYlQg34Y9IJqIBDJbKQ4QrsffRtSp8AsE1H6_bpIlUvnLyFvftcVnyXcgVZ3Vng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ee7eabed3.mp4?token=Nw2sGw3nf9j_002AmR--w8Nt5Vr4lnDYi4ahJ6SftUCacnt4anJqZm_82crsTtTs7rVMis-8y4Ke_XQH5u36_4cm2syccn7356UmFqxXxUuMvuw5Y1UXNVqPFA1Jjv6K1IwqQdKig9wMsuwWd2xtyo16UuNUGwNGPZ_AsoLC8vAqNGQKZDzxJumC2leu3h4PgBk_q_yrTy2lX_7eeQ4b2e57lsRZijRrFamjtBOV78UgQxL86jeAvjUJZHO9L4qgNQopyzYZEC_0E0-Ot8-vk0TEYlQg34Y9IJqIBDJbKQ4QrsffRtSp8AsE1H6_bpIlUvnLyFvftcVnyXcgVZ3Vng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قلعه‌نویی: همه لذت بردیم؛ حالا نمی‌دونم خدا هم با ما سر ناسازگاری داره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/663766" target="_blank">📅 08:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663765">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJ-9CJAyGua6P7IJpaeglr7c63Qyt_wguGly0sQyeBksQAkW_FVeU8Z_irkkc0Zv5cmVw8PQ6o8xK-gQJhy7xhZcZpfdltIzy6sls6xRYtEtxcqc-vUk-QcNdpvXaf0VN_PY4geVGD-iWhmpnQErrLGT9VueHkPfg2fBtianq6JUPWEedFWJOflZyleAhqM1POwO1SFxsKDWmK5ETP2aUinMv1k-_35TtHgGjiQ8D9BdF7H-1s-I8mMkSX1xbY3miIUwdyEbgeHGWZ_j3p1vLeMiGivP-CJTp4dscG7K-tHhUUXE2INFmkxl2jUOUzk9zp4XuJGYIlGc8vkjd32JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری سردار آزمون پس از تساوی ایران و مصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/663765" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663764">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NrM3e34sFzLeaiK11ky7WIcw9MMmreUfyNTZFSbXZzD199LM4nu24a9wKhG5ANM8hFCwlZ3T4qmn_2SBZ_GRgbLWt8lVx0DvmBJneeVwtrc4JkLR2Ej8xg6XpHaZtPbDw6yFe6CEwoAxcVW6s71hMLM38HywF48-ZOFq29e6AtmEqNZ7mFiwVl3aq3b_-U5ly8ctVl39qKtZ3KLT_An9VE4BdWfi2Tor3SIPbKkGa67m2E0Th8QA0o4KQHIgoXBT_lqVY8D_p8rv9Kj-tqJQ5BGXF6U2k2d4ek_R1czuKJMUyltpv299X2ze1N1W1ObTuEF7hce3BHtBMfxfUMa4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی ۲۰۲۶ تا به اینجای مسابقات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/663764" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663763">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq_hpj6FxZYsAp-BTxwlETN-9iQKC8_nBBbJTySORaRXnC1tgGzbfmXIjIcRxL51JNMy0r3jK_JTUS7xmYfzpRxucG3LFzq5LZztN3VpsB6kXPelcRMxYVSvKhgD3VzMzUqHP2pVhTOHsB_NsFI-MomXNuEEUiO3QE0T4xTYEz-3FxB2UfSnNswmWmhne-OAs5SbKCLTAtdrccXblZdAslUVnBKgGqYKFg5ljxedkRb6cwWnMN2IT-UPtUpS-6teW7tK0mccXW0XwbEh-z0bFc5mu2GsXoldE6dQduBQx3t4EmpDac8m5GodhVtcWo6n7s2TNxpAlSI6VFke6tAuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
آتش بس نقض شد  به گزارش خبرنگار صداوسیما در سیریک:
🔹
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
🔹
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
🔹
حدود ۵ ساعت پیش چند شلیک اخطار از…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/663763" target="_blank">📅 08:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663762">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwmv9inYih1t8Vefjc2bxPK70dM6Ii9tqBRX6FfdLEW3FrUzJk8OYL3WiWW6-l38HchFqYpPIrKTN1X2adpg8Q_SQMMMIArmpdJfnpGsBcoru9G_nMxUbqtgbuHAo9gtEgZAxCj9V0YWdyJHfTgbOCzB0-bn6PDvc1mC0bPlQ-fDw3s-IcyuUl4uyt-y-hUJUx4aBdp-8mgi7r1oFXeqG30TjEYF6JTM1A8DKVScmUSWtstXtbSQ5haaC4oCKPgEhWTorY08VTHaOWmJC8LgblCEw0cx-cafxi8jgg-7Y08G8p8_hGUPbq7R0P20bCYemeLmxekT1EH75Vg29fp5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول نهایی گروه G جام‌جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/663762" target="_blank">📅 08:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663761">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=n5qHtEK4thDVFegX8eqNT_7kGxjU5ZNWUyVLsYV8bEbPkDvumsXV6wz-Ufqnf1wCAo8uxG-hxOrSOkvYPKVvha3VkI7cFFuagubLSEsWFDVdmivWR3msp0Ua44URpvQubrCbCQuC8ZoSD83MY9SD1A4JnZBE7ia7VLi0onysnzRgwLumN8ujPf1AfF3KQASx4nL3CMVevAwMogE211kIg1CG0WT8G5d1lRcnb0NYtil3xqcIJu1p3LbmpfxIje6t3LYE2k7a3JVrbaB9cXfL_EbOYYoQNfR_EpWXls2157hC_6qsHNj2qyDP4KDxACmCbBrKLFq-fEexMf79L8hfYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=n5qHtEK4thDVFegX8eqNT_7kGxjU5ZNWUyVLsYV8bEbPkDvumsXV6wz-Ufqnf1wCAo8uxG-hxOrSOkvYPKVvha3VkI7cFFuagubLSEsWFDVdmivWR3msp0Ua44URpvQubrCbCQuC8ZoSD83MY9SD1A4JnZBE7ia7VLi0onysnzRgwLumN8ujPf1AfF3KQASx4nL3CMVevAwMogE211kIg1CG0WT8G5d1lRcnb0NYtil3xqcIJu1p3LbmpfxIje6t3LYE2k7a3JVrbaB9cXfL_EbOYYoQNfR_EpWXls2157hC_6qsHNj2qyDP4KDxACmCbBrKLFq-fEexMf79L8hfYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افسوس قلعه‌نویی و بازیکنان تیم ملی بعد از پایان بازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/663761" target="_blank">📅 08:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663760">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c672ce05.mp4?token=DL0VDhGaV4N8CnBD6rDS85DvQ0QLwl0yqj--CPSzrg8AlaCj5lOYxoYuHaZczLxESIT56lrVVAVpNNvFH-qY1Dg36X2n_2YvpAHm7Mss5AzM8uPVsoIaMNC1GASsrMTNFd9CkpjBPbcL33x8XbdHmqC_5xP7FuZzup5aKqucrrSsh9cFzAq1M0RTLxs-cawjkOJ7ETB1wjYrTEhiRHqBw5ZLG7SXS7So41SbQZ8Kq8o6p0R4I6rCx4VD1wWz_YlQ1TmbcXDmb_x_ruZ20FMmxi1JVPCH22uvm0vnTHWxhkh00oSSw1HhYy1AQNsMw7DA--hk4aTHWpe6T6I4bykh8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c672ce05.mp4?token=DL0VDhGaV4N8CnBD6rDS85DvQ0QLwl0yqj--CPSzrg8AlaCj5lOYxoYuHaZczLxESIT56lrVVAVpNNvFH-qY1Dg36X2n_2YvpAHm7Mss5AzM8uPVsoIaMNC1GASsrMTNFd9CkpjBPbcL33x8XbdHmqC_5xP7FuZzup5aKqucrrSsh9cFzAq1M0RTLxs-cawjkOJ7ETB1wjYrTEhiRHqBw5ZLG7SXS7So41SbQZ8Kq8o6p0R4I6rCx4VD1wWz_YlQ1TmbcXDmb_x_ruZ20FMmxi1JVPCH22uvm0vnTHWxhkh00oSSw1HhYy1AQNsMw7DA--hk4aTHWpe6T6I4bykh8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های رامین رضاییان و حسرت از نتیجه بازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/663760" target="_blank">📅 08:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663759">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
برای قطعی شدن صعود تیم ایران باید ١ اتفاق از ٣ اتفاق زیر رخ بدهد:
1️⃣
. غنا موفق شود کرواسی را شکست دهد
2️⃣
. ازبکستان موفق شود از کنگو امتیاز بگیرد
3️⃣
. دیدار الجزایر - اتریش مساوی نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/663759" target="_blank">📅 08:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663758">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6055a2907.mp4?token=adYzsQyKPYz_Cy3_kB6cM-Is8UQDGKrVWCThCZAuYYgxRI6Ap2Kl7bigJZlmR8IykFmWQXJEUzGqIL-Y97dYJw0Tf4ituA-W-cYX8GcB3IdT5eECNwNbis6kUgfzJZrMi6YM4XAayCQQlb0EalWQOcNTwLaVwzMDe2A21GdEURMoMlJxRngOXSDsJy02qdRPq7YtCLJC0MdzDiQw3EzqY21S7O0upKK6OkYkk8b1DuRRzKnAUmNkNGifhjzxEr6YZtC1z84MK7wj3eCa53ssfGB-2aJtOrX7WaTPd5-ffT4pQs7sXb8JlTzhmS7sng2724jyXDK3OC9zUonstdPeIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6055a2907.mp4?token=adYzsQyKPYz_Cy3_kB6cM-Is8UQDGKrVWCThCZAuYYgxRI6Ap2Kl7bigJZlmR8IykFmWQXJEUzGqIL-Y97dYJw0Tf4ituA-W-cYX8GcB3IdT5eECNwNbis6kUgfzJZrMi6YM4XAayCQQlb0EalWQOcNTwLaVwzMDe2A21GdEURMoMlJxRngOXSDsJy02qdRPq7YtCLJC0MdzDiQw3EzqY21S7O0upKK6OkYkk8b1DuRRzKnAUmNkNGifhjzxEr6YZtC1z84MK7wj3eCa53ssfGB-2aJtOrX7WaTPd5-ffT4pQs7sXb8JlTzhmS7sng2724jyXDK3OC9zUonstdPeIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل ایران به مصر  آفساید اعلام شد
⬛️
🇮🇷
1️⃣
🏆
1️⃣
🇪🇬
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/663758" target="_blank">📅 08:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663751">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fff729c34.mp4?token=AgviIZ3mPeDq137Uj_fn7v22GNVXgRntp2N0_ViJbXXM1bXLFFwCyaUyEfaSdoPL8mJoTJ9dS68nEaITO4MS--zf5Ln5-MPPxTt69R6KNJuJsSm9239p__sHEG6Zt0uqW6QgzyUjD0VgSqe0IPJzYRToKjktFldzMDppCRHNWlpIQsR_e0-PrKuP2jq3d_29ChWNlQhq_hv2X9x2g727yTgrR4aipqR7q-N3DbEK752DlNtgbeZ72CPQEMTt7D_Ekgfy5X2apO3gIklubT0v-PPTQY4Q1biRD6fuq2Bzz2VTVrUfUdWxx3EDxMGl02M9e8M3BaZrAboeiFWNuHtLUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fff729c34.mp4?token=AgviIZ3mPeDq137Uj_fn7v22GNVXgRntp2N0_ViJbXXM1bXLFFwCyaUyEfaSdoPL8mJoTJ9dS68nEaITO4MS--zf5Ln5-MPPxTt69R6KNJuJsSm9239p__sHEG6Zt0uqW6QgzyUjD0VgSqe0IPJzYRToKjktFldzMDppCRHNWlpIQsR_e0-PrKuP2jq3d_29ChWNlQhq_hv2X9x2g727yTgrR4aipqR7q-N3DbEK752DlNtgbeZ72CPQEMTt7D_Ekgfy5X2apO3gIklubT0v-PPTQY4Q1biRD6fuq2Bzz2VTVrUfUdWxx3EDxMGl02M9e8M3BaZrAboeiFWNuHtLUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه سر طارمی با بدشانسی به تیر دروازه خورد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/663751" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663747">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY54s8g5ZzN9aU5LSp6Dyj4UxpuSkUTT8LFyTslxVpUX9nQn9qu9vyhkkGaMadmsoVRjZ5QwNNThT_VeuuBE3cKIRGWOI0JW21fV0KbXA9NAdqmadp5WIsqF6jkdSyaZr_32icjQyO194kZLtZQ92LByNoLp9THGy5p_RrnpM_GGf2sblpPSMRv18fzy8BiLLwYhihgMk6muE0arOBeOghYlXbieu5QgpDKSi-LQXVO-GYJAczcimyh2uhAwHP8AZdJprClopId91TgCI9uqYYmcoIbpQB2ihNqya36bm1VHqiDoz2tF-2q8tNbMR_EzPobklaK9xtK7jRQlEEG0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ملاقات مهدوی‌کیا و اینفانتینو در حاشیه بازی ایران - مصر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/663747" target="_blank">📅 08:20 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
