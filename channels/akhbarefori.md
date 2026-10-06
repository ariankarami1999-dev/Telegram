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
<img src="https://cdn4.telesco.pe/file/WOpU48kJUupeyagb48xAeWQUlPMAhfJoWdL2Ax123CicIAlY9Jk70_rtsiusbwOxum5AdnXA3lpy09V40k9F1SP2qTdHwJtCLhW2nsjuDRttj2C3gj7IFGYvllsWVc5Xr0ptpN-EkiEip1OLSn-fsHlqYDNjj3AGFQ_VdKejzdZTBIUoZxzAxV9AvVv2ept5xYHreR7zGC2Ob9DoADmMdO0Dt0DhDFDC6E4vLJAlGDISBqFbMRmJQrLuqjNqiuC-2MM54EVR8Vmzn75npO18DY3_XrGJey8SWVgmlROuXh8ojLwIzQHPN6KybhecD9Jt7M_1x22ZLrvElEGpOrHdOg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-696015">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
مجلس مجازات ارائه دهندگان اطلاعات به بیگانگان را مشخص کرد
🔹
هر کس اطلاعات، گزارش‌ها و داده‌ها با آمار رسمی منتشر نشده کشور را در اختیار بیگانه قرار دهد به حبس درجه چهار و محرومیت دائم از تصدی شغلی که به اعتبار آن به اطلاعات دسترسی داشته یا از طریق آن اطلاعات را ارائه نموده است؛ محکوم می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/akhbarefori/696015" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696014">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
استخدام سرباز فراری ممنوع است
رئیس سازمان وظیفه عمومی فراجا:
🔹
با کسانی که سرباز فراری را استخدام کنند برخورد می‌شود، حتی اگر بخش خصوصی باشد.
🔹
خرید خدمت نداریم، اما معافیت ۳ و ۴ فرزندی همچنان پا برجاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/696014" target="_blank">📅 10:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZUko-4g4skppD21Ter9wRO4eabgzxH7s0H6xKNJCZ6aAPLV2Hmdm9cJTThYxrf5fWoAIm4SL_w-a93WsRtdf80dxH0wHKsKAm2nCeqd6FmJ9wG-4WsHupvc6BR9ogFS2qLeYQxKVZwYwMqehlEHEWW4Y96MiQ88LOcOB0umnLO0fhXh3_oRJ3mCW0zdQ68oMjj1BClONM3kueS8bBZkc36fgtlqdUWsz-8LJ2ojA3Q36JrylNj8nygCIWOAgdvGpPwcTl0FxlE7mc-WYpAiOmCyGA2FxwoLCHp2J1dRdQvTb8Fta4T-rgp3LoOlPL4znkHeplr63yT2E9pFAQdc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت آموزش و پرورش ترکیه در جلد کتاب درسی جدید خود، تمام مناطق شمالی و شمال‌غربی ایران را جزو نقشه‌ "دنیای ترک" قرار داده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/696013" target="_blank">📅 10:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ایلان ماسک بار دیگر تریلیونر شد
🔹
بر اساس شاخص میلیاردرهای بلومبرگ، ثروت ایلان ماسک، ثروتمندترین فرد جهان، دوشنبه پنجم اکتبر، ۶۵ میلیارد دلار افزایش یافت و به ۱.۰۴ تریلیون دلار رسید که ناشی از افزایش ارزش سهام او در شرکت‌های اسپیس‌ایکس و تسلا بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/696012" target="_blank">📅 10:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696011">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b49274fd.mp4?token=ba0jOQ_lN0GA9sFMg79qYAeCUGHtbGraWxBVyk0inxZ2h9F4WT23EVCHO6rdSrnuwR8jtgLilJKjz8Ik2ysNqfqS0uJVCquxKMLvB8uK_CeNa6f3aN7RGSAUcL0fr_NZRQDZ4VTqIpMqqD_IWBuBJziDwSwwxMCqYW99xS-lmhZlSsDX69_8kgdrhrJfK_vteM6vGyIoS3ke5Xl_cbjOmtgnMR2dL5vTmuq7tvj9oiOtIeSEpB61qSw6Emqhy9KzTWmT89lyzn5Dss_NamVkZWHVbSBa7hVZRkI8mcfUYI6UnGaYiY_dW6EfuxLxhas9Q0sE1m17nB9xGSYnOKuhrQWRO78l80D6jZJILzPffkxoKTvJ44P0bHVXTtjrAA4ed6tDca1xiIcw8nbzohzp1_Bf-YZlyc5KE0ugclZLXDmy2BTtyKxlvtJXdqLU_mEgxWzxbkh5t98khV1RPjk1CAe4VI9fRxcsdYY1-_cnpaaGcNsWoAsEG_3iT5067PMh1rRP2_d-7KcwoziyJkPHX-z7yR47gFEkXVKSNO5_QfKwVDrjUJtbkwP6PnCMNkRZQh56cFXfK1d_aO8dF6-lJimBfcgovstQdb9xxLuQ9nSEOV7KLh3JFwLW6_cwlDlFeCg-I4O-8crQ-Ah8PTDIE0RwIVYZnQRfzkXLLBGNP10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b49274fd.mp4?token=ba0jOQ_lN0GA9sFMg79qYAeCUGHtbGraWxBVyk0inxZ2h9F4WT23EVCHO6rdSrnuwR8jtgLilJKjz8Ik2ysNqfqS0uJVCquxKMLvB8uK_CeNa6f3aN7RGSAUcL0fr_NZRQDZ4VTqIpMqqD_IWBuBJziDwSwwxMCqYW99xS-lmhZlSsDX69_8kgdrhrJfK_vteM6vGyIoS3ke5Xl_cbjOmtgnMR2dL5vTmuq7tvj9oiOtIeSEpB61qSw6Emqhy9KzTWmT89lyzn5Dss_NamVkZWHVbSBa7hVZRkI8mcfUYI6UnGaYiY_dW6EfuxLxhas9Q0sE1m17nB9xGSYnOKuhrQWRO78l80D6jZJILzPffkxoKTvJ44P0bHVXTtjrAA4ed6tDca1xiIcw8nbzohzp1_Bf-YZlyc5KE0ugclZLXDmy2BTtyKxlvtJXdqLU_mEgxWzxbkh5t98khV1RPjk1CAe4VI9fRxcsdYY1-_cnpaaGcNsWoAsEG_3iT5067PMh1rRP2_d-7KcwoziyJkPHX-z7yR47gFEkXVKSNO5_QfKwVDrjUJtbkwP6PnCMNkRZQh56cFXfK1d_aO8dF6-lJimBfcgovstQdb9xxLuQ9nSEOV7KLh3JFwLW6_cwlDlFeCg-I4O-8crQ-Ah8PTDIE0RwIVYZnQRfzkXLLBGNP10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این پنکیک‌های هتلی، صبحانه‌ سالمیه که بد غذاترین بچه‌ها هم عاشقش‌اند
🥞
مواد اولیه با محاسبه یک تخم مرغ:
🔹
تخم مرغ یک عدد
🔹
ارد یک پیمانه (پیمانه قنادی یا لیوان فرانسوی)
🔹
وانیل ۱/۲ ق چ، اگر نداشتی پوست پرتقال بزن
🔹
به ازای هر تخم مرغ سه قاشق غذاخوری شکر و سه…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/696011" target="_blank">📅 10:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696009">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KxDm1Ees2reQV_ANJ5QWFcWQFMOG1XvcV7r-2V1lPDm5dRGVCNonoOBvdji_3wE7ZioTgl82wQQ9Oo5lwlQWUjJWvxTguQODC71FOesrv5V1DCIN3UBx1ac9IqM5M5xcO66Z-VZwK3P9XWhtIN5mvHMW_aYHFApg0OsHMz7aI_o1oXWs54Gfv4CR1SYM-VJwvuS37aM0Xel9N8hzTWjrC9FNDOv3jZNiMNpxjV4K4YfkcYbpdqiMnS7GLppGhhfGHek1FPufQWr33x2RdKqmYisY3w_r9oGwx0U7l2CJdhLs7SekeSjFtjEx-YDFTqzs5ti-MQgNaDDxJ6l-mtVUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYK3-kdgh1ovR16j0lOe6sfpNxFq3pAvgZX3p05rFR2OMFKwY1QEgWMwhAmQ8Maxzbe_rIoYedV8LVm1ey78diPzF6y-bJozUVG2PgY1BbOE21oRIL2M1Ga9dSheZNQ5vhvCT8y0XbhLNSs3k3nGLazux-svyQOTz2n8yxWbPKKETkB595Y3IZbc4Dk9H6QoX3q2q7AifIJX-bcY3px5UAcY4mc2JXQq1WnWMzKnQCTLwNsGWmLLdwEAUWMCfMVY6RAdwAn1SmLX0O_voi7yry9Vz3mmf1ZcG50-Ia3oRAjrHp9i5-e8HRW_cxWSURLsJHklC3vrvycAntLZlU87Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دو قاب جالب از آموزش های نظامی جانفدا که در تهران جریان دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/696009" target="_blank">📅 10:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696008">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه شانزدهم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/696008" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه شانزدهم؛ شکوه حق
🔹
در فضل الهی، بخشش خداوند از راه می‌رسد و خیر و نیکی بر انسان‌ها و سرزمین‌ها جاری می‌شود.
🔹
وقتی انسان‌ها در میدان آزمون درستکاری قرار می‌گیرند، لازم است در همدلی باشند و با روان محکم، یکدیگر را حمایت عاطفی کنند.
🔹
تحلیل‌های بی‌مورد و پیش‌گوییِ رویدادها و همچنین گرفتار شدن در ترس و اضطراب، مانع دریافت فیض الهی می‌شود.
🔹
در سخت‌ترین شرایط، سالک باید مثل یک اقیانوس عمیق، آرام و مانند یک کوه، استوار باشد.
🔹
در نور قادر مقتدر پروردگار، انسان باور دارد که هیچ‌کس به جز خداوند نمی‌تواند سرنوشت را رقم بزند و این مسیر، سعادت دنیا و آخرت را به ارمغان می آورد.
🔹
پروردگار در نور مبارک قادر مقتدر، هرکمیت، اندازه‌گیری و کیفیت را با تسلط کامل رقم می‌زند‌.
🔹
نور مبارک قادر مقتدر، از قلب انسان‌های سالک، بر سرزمین‌ها تابش می‌کند و تقدیری نیکو را در عزت، قدرت و بزرگی با فضل الهی رقم می‌زند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/696008" target="_blank">📅 09:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696007">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
پژو ۲۰۷ از مرز ۴ میلیارد تومان عبور کرد
🔹
قیمت پژو ۲۰۷ اتوماتیک سقف شیشه‌ای امروز در بازار آزاد با افزایش ۲۰۰ میلیون تومانی به ۴ میلیارد و ۵۰ میلیون تومان رسید؛ جهشی که همزمان با افزایش قیمت‌ها و نوسانات شدید در بازار خودرو رخ داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/696007" target="_blank">📅 09:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696006">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db884db9f9.mp4?token=PVGHSqMIY6wNvp4jHb5q4Zi4ZbG0S7EXssKgPXIBWYiQyP4QJ1hhN5ANNj5ItfCr5pg8dOKPrvin6zssb9vsT9xOsXZj7v-cNgxUL6ZgdNFuIVDzkRzi5iHXtHWH6uI7cN8Lphxo1qHWL3GyJvDdqkliY66TQbLKTSHeOo4k-c05tdNPVUb7RYz_bI71tb4-5SX0xFDyp_vj8d8Uuy_2JOsV8CnS8jcij6401Q7LoI9JWL0fj6pmvwfHU4Zrb6qxCFPcSwDlaMVWhG2X0oJpxwKF_wVo2ndyr12lysNevGtHxqm6ShtXkJbWXErJOYDT98qLLVvEl2tDx1ZCN4rDEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db884db9f9.mp4?token=PVGHSqMIY6wNvp4jHb5q4Zi4ZbG0S7EXssKgPXIBWYiQyP4QJ1hhN5ANNj5ItfCr5pg8dOKPrvin6zssb9vsT9xOsXZj7v-cNgxUL6ZgdNFuIVDzkRzi5iHXtHWH6uI7cN8Lphxo1qHWL3GyJvDdqkliY66TQbLKTSHeOo4k-c05tdNPVUb7RYz_bI71tb4-5SX0xFDyp_vj8d8Uuy_2JOsV8CnS8jcij6401Q7LoI9JWL0fj6pmvwfHU4Zrb6qxCFPcSwDlaMVWhG2X0oJpxwKF_wVo2ndyr12lysNevGtHxqm6ShtXkJbWXErJOYDT98qLLVvEl2tDx1ZCN4rDEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چهار کار پرتکرار ما که به مرور زمان باعث آسیب جدی به گوش میشود
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/696006" target="_blank">📅 09:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696004">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وزارت بهداشت از ادامه افزایش موارد ابتلا به کرونا و عبور شاخص آن از آستانه هشدار بالا خبر داد و بر رعایت موازین بهداشتی تأکید کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/696004" target="_blank">📅 09:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696003">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ماشین دست ساز وایرال شده در مشهد که شباهت زیادی به سایبرتراک تسلا دارد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/696003" target="_blank">📅 09:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696001">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyisnCU_2D5QqOC1_fJeFO-yh_8jXcdnn_kK10lXTfUFBQ8IdoNV2tReasl9Hjn-44NOGpr1ODs8mUJAHqhpsai07YaLjXnNStYUlQiFPrnQrUtZjsvK3QVUt_myCf6eCND9g-eG-h4Ob-s-rYavjDhkeHzR9mTVytvSeDmyiL5K9qC4nEkNTLS1qRplM4Vug-cUBCWa4KDuNJh_2yQHyL_C1xdiJKUrih2YhsCo7nEuwZ4WBCy0_ycmoXD5WIfj_s6wrRwH41yjZBSypAbKpHirP0k3U3ZNIjpa7x73VomAJ6-S7XD4L2aTSfjvhnRHFGffRCtsXIQckHLKDWf0UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماریو نوفل: عجیبه که همه چطور پرونده‌های اپستین رو کلاً فراموش کردند و هیچ‌کس هم بابتش مجازات نشد؛ لعنت به این دنیا!
#جاسوس_موساد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/696001" target="_blank">📅 09:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696000">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lx4qRthX_zfaj1V9rRD5FdMPawKDknzauYdpClWWGwVE1SiAwVmF48bZhiDgWRGZyUjofsdRktvlsreno-0hqWBhl5TKJVoas3JWV6PVrEDT04wNUBk6q13_4OYCcMvIj9GtionSYo9N363pSvChgvIi0nTFr3CJIpx2ySou0TB7e38n2xqNGMAVb7yGRpe5b3xXFwPUwCdpgGMrkdmT-wqCitHkj5Rs_hN-cdGW2SlmzFDmPqbu_iyfiqpksAN7hJ59yZ0gJOnf6bY_Hs_9xTO2g1ge7SJ0lKNfwaZa4mjzboOBToE6vJtsYGw-PXMKn2_6j5VBNluDGPVruStOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت شهر تعز، دومین شهر مهم کشور یمن
🔹
نیروهای انصار الله به رنگ سبز، نیروهای وابسته به عربستان به رنگ قرمز می باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/696000" target="_blank">📅 09:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695999">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
قتل ۴ عضو یک خانواده به دست داماد بر سر ارثیه
🔹
داماد یک خانواده در روستای ملایوسف مرند که بر سر ارثیه با برادرزنش اختلاف داشت، با شلیک گلوله برادرزن، همسر و ۲ فرزند او را به قتل رساند و حدود ۲۴ ساعت بعد با شلیک گلوله به زندگی خود پایان داد؛ تحقیقات درباره این پرونده ادامه دارد.
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/695999" target="_blank">📅 09:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695997">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
خبرنگار: دولت ایالات متحده در مورد خطر شیوع طاعون از روسیه چه اقدامی انجام خواهد داد؟  ترامپ:
🔹
ما این موضوع را به دقت بررسی می‌کنیم. میکروب‌ها و عوامل بیماری‌زا قوی‌تر شده‌اند. ما به آن‌ها کمک خواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/695997" target="_blank">📅 09:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695996">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e919cc080.mp4?token=bVQc0R0F9w5QilSHERn_XP10MzOVTUdjy5OkAdVytTnx9bbfTHJcBoYjhzWYIc9iurMem_cpmNTTUYOrZY5pQyouaEYH-ILCHU9tm8EaPBrdL9waIuAtgF8r06quS-RCD6wVlGMwuThkLOv6NR540FgP1mPSnjsqyq7OxNsa38qiQZwPDgoE4qw-s-qSrKGem5drAQ6uq27xi4RHQxWKi2AbJlBTrEK3rHW3rkE_LBSOCluPjtlng3jEdv2ns0ZeYYIHsEKSXaCn-fHFPVQPOqkEfheHu7VDyX2-5Uo2CM2-57foYrhWwTi-L4pXYJeOle8KWy-tqU8L5gQUI5t6OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e919cc080.mp4?token=bVQc0R0F9w5QilSHERn_XP10MzOVTUdjy5OkAdVytTnx9bbfTHJcBoYjhzWYIc9iurMem_cpmNTTUYOrZY5pQyouaEYH-ILCHU9tm8EaPBrdL9waIuAtgF8r06quS-RCD6wVlGMwuThkLOv6NR540FgP1mPSnjsqyq7OxNsa38qiQZwPDgoE4qw-s-qSrKGem5drAQ6uq27xi4RHQxWKi2AbJlBTrEK3rHW3rkE_LBSOCluPjtlng3jEdv2ns0ZeYYIHsEKSXaCn-fHFPVQPOqkEfheHu7VDyX2-5Uo2CM2-57foYrhWwTi-L4pXYJeOle8KWy-tqU8L5gQUI5t6OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنگین‌ترین پرونده مهریه ایران؛ آقای جراح ۶۳۶۰ سکه مهر خانمش کرده بود و الانم در زندان
است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/695996" target="_blank">📅 09:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695995">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b2adc887.mp4?token=Zgj3amt8UdcYSWdHHA8zOWZ4uRxV6ZC49LOuue6eW9OQyeeJd2w7oRoxxe-ETuCYRVj0nwBRLIXAHfBiL2tQdSjkN_XrILit4uA7v5ZJdcPvL-XWFVb3z3HUPS0pQzBr_8_4xhJEdn7XmVJg74cd4KDUrsO9WxSqkRF5kLOYG8YBoBOAG8nvAvHH4tG8GM-_hZgqZATVEYxV3QoKhh-XB4pM0acN0BDeQkM-OhfnkUGE_VUyM7OUnuoX5o4JauM58OSc-9P6NlXZeqSVb5YM5LMopqgD0nIRQm-1Bz29lTKWi5f6iOuDr5oprFUH0oQQKoSbw7xypwPaIdS59GXTv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b2adc887.mp4?token=Zgj3amt8UdcYSWdHHA8zOWZ4uRxV6ZC49LOuue6eW9OQyeeJd2w7oRoxxe-ETuCYRVj0nwBRLIXAHfBiL2tQdSjkN_XrILit4uA7v5ZJdcPvL-XWFVb3z3HUPS0pQzBr_8_4xhJEdn7XmVJg74cd4KDUrsO9WxSqkRF5kLOYG8YBoBOAG8nvAvHH4tG8GM-_hZgqZATVEYxV3QoKhh-XB4pM0acN0BDeQkM-OhfnkUGE_VUyM7OUnuoX5o4JauM58OSc-9P6NlXZeqSVb5YM5LMopqgD0nIRQm-1Bz29lTKWi5f6iOuDr5oprFUH0oQQKoSbw7xypwPaIdS59GXTv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا توانِ فنی ساخت بمب اتمی را داریم؟
کوروش احمدی، دیپلمات سابق:
🔹
از لحظه تصمیم‌گیری تا رسیدن به بمب هسته‌ای حداقل یک تا دو سال زمان لازم است و در طول این مدت، کشور با بیشترین تهدیدات امنیتی مواجه خواهد شد./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/GbSIAN0lpkI
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/695995" target="_blank">📅 09:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695994">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
فرمانده انتظامی سیستان و بلوچستان از کشف و جمع‌آوری بیش از ۲۵۰۰ قبضه سلاح غیرمجاز خبر داد؛ در یکی از عملیات‌ها نیز ۲ عضو یک گروهک کشته شدند/ تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/695994" target="_blank">📅 08:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695993">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eblXYBLkE_bFXAs8HeWf2aw2ZGL84NCNQpx6FeIjO4cOwpkBfJe7ht80LJnV_cN8zyKeQnXhK29EsEW-_TppI3n9_9kI0K2rnzvdvuc_0PsdYcxHX2tBgKcGdL2CruiYiY4sEhqbhI0eknZHp_PtTzadrlxBCJkk2CUTzMrGedi2-m_qIScY6MdrBxgw7Jsu44rcjN0Pos13vfh9zygqzd3nkoxFGOHA7MeSBdQXZiAmjV9tMAgfkhfYRjzKb6bARri42WbhPaacpmo8p2iFcsp8qe7x0L_kyHTy_VGPU8kTmGqRXWDTLu7dul6UDiitgMSvm6Hf1tVMEz7OIqwIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرزند رهبر معظم انقلاب سید محمدباقر حسینی خامنه‌ای رتبه ۱۰۶ کنکور انسانی ۱۴۰۵ را کسب کرد/ صبح صادق
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/695993" target="_blank">📅 08:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695992">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0429ed04.mp4?token=BK6RtyxhRfDqX_0cZpQtZQUE63nqB5VQB_M5GA5mV9qyQK-C4GVJHapFnlP49ZiZHVKXz8OXo-8qYHUzSU3LtXcibYj7Hs9fzgHq50iwaZk-D1ZBn9mHK_bDHC_qWJHO_EY6XHXWNKPPf9n-wTu-YYWm4w0NnXDReu-uAwwVxsSx3IpRzAM5741Pzh7fy_7IIVECLqHDFwgNx-Nv9FFUe65PayKFKiplm4RbGw5WuJiaeUrbVC6AZ2HQ_oqlIiieD_qfOR-bUehRzXSnOxhm35ONCMa86PYWpvI5odQRYgrFj9jWKSjs0ejWGkr3EWcIj3H2m_LdcS8tTADNB96LTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0429ed04.mp4?token=BK6RtyxhRfDqX_0cZpQtZQUE63nqB5VQB_M5GA5mV9qyQK-C4GVJHapFnlP49ZiZHVKXz8OXo-8qYHUzSU3LtXcibYj7Hs9fzgHq50iwaZk-D1ZBn9mHK_bDHC_qWJHO_EY6XHXWNKPPf9n-wTu-YYWm4w0NnXDReu-uAwwVxsSx3IpRzAM5741Pzh7fy_7IIVECLqHDFwgNx-Nv9FFUe65PayKFKiplm4RbGw5WuJiaeUrbVC6AZ2HQ_oqlIiieD_qfOR-bUehRzXSnOxhm35ONCMa86PYWpvI5odQRYgrFj9jWKSjs0ejWGkr3EWcIj3H2m_LdcS8tTADNB96LTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاروان‌های نیروهای وابسته به عربستان در میان آتش شدید نیروهای انصارالله از منطقه میسراخ در استان تعز عقب‌نشینی کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/695992" target="_blank">📅 08:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695989">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lhhbdm-YvRIyypXxSpCyIeBC84ZZcvl-gE69Aa6Gv6nW9ApKLDMg2K7i8cfL7xo_sqXQ9cHA3Lw8xBdxZfpLdt9Y7YEEngbuEf38tjFuaoj1A01nNCMKrBJj_ifDsFEMqZ8fnM1gVnGJYSJBn_AISJS-JNwrCojEF0sdWKpIPQatYcIcBXo6ipRlNhTWv17fNd2yX6Ku2EkDhrxQH5A1B9FHq6apCgbKe2etHOwbEkggbF8RdBVk6YyToXWdi_xfAUpMOxDab9NIiKZRs9xAGuaF8ZdvOEV7ggEP3reT_JGV8sJkxGQ57NBDNATwtx53MF7vKdPIicX2IuDosz3cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرزند رهبر معظم انقلاب سید محمدباقر حسینی خامنه‌ای رتبه ۱۰۶ کنکور انسانی ۱۴۰۵ را کسب کرد/ صبح صادق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/695989" target="_blank">📅 08:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695988">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a9f3906fa.mp4?token=SEEQb-pU9qKsicn0nCKlXuKmjrRdXoCpla3zDcc_RNtV_v-wojjFEAdJmQr0WRFXVicD7fFCA-bzfTFelq7MPa03KaXIGeVu6K2i1Hr_DVsiKrK2aZWtDb-ZI1B21ZUmWm5Xgq0nGRdeyf1YbFqiEJ8X1MVZM24ZapIqag3hOuVc9XeWdTmJHJeQljRFFxMxwYVuR9WXE0TbhQRHz6AGuF2rxEJB0WNtfGbszfFA2YGdOKBzTdbolMfdr0d09n-XrmYV-2yM5aGqFhRa33AkbKaOfG-5z1N3orRRHbAL2dbzHCGkMi-M-IFKQ6UtoBEntXuG7YEETe0IiZc45eqiYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a9f3906fa.mp4?token=SEEQb-pU9qKsicn0nCKlXuKmjrRdXoCpla3zDcc_RNtV_v-wojjFEAdJmQr0WRFXVicD7fFCA-bzfTFelq7MPa03KaXIGeVu6K2i1Hr_DVsiKrK2aZWtDb-ZI1B21ZUmWm5Xgq0nGRdeyf1YbFqiEJ8X1MVZM24ZapIqag3hOuVc9XeWdTmJHJeQljRFFxMxwYVuR9WXE0TbhQRHz6AGuF2rxEJB0WNtfGbszfFA2YGdOKBzTdbolMfdr0d09n-XrmYV-2yM5aGqFhRa33AkbKaOfG-5z1N3orRRHbAL2dbzHCGkMi-M-IFKQ6UtoBEntXuG7YEETe0IiZc45eqiYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین حرکات برای سرد کردن و گرم کردن قبل از جلسه تمرینات ورزشی که مانع از گرفتگی عضلانی می‌شه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/695988" target="_blank">📅 08:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695987">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWqVvCb01OPFSTj3Uz7Cg_M7Ho5erE8YmcvuoxMuhnZ9Fb1ZD7j3P3e0e1rch1U1n6_nEaMDq7a1otUYSmpusAfHsFXGhlNmld_iwc5JNssFWpgoUwPFY6XeN6WwVwkAZJU6PLOHajYMnovRVR0RwV9MtoU9fqg7TnHUDPvDkdvadRQtYitThlETUTkSd_UM-4WD_-oBilg1qql0EccOka8yutvw3BkfT0oGAVkOJZvZkePkhisnpUgEzP8ku8ymT2gwN3ugQ0wSmO66kSo6YhL-F4fjdAk_f7OFeMixPsXgriaFUwR0AKHCr593kWUrOPahdLEMmeAKwBvLpj0NdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ حکم اعدام یک نظامی آمریکایی را از طریق تیرباران امضا کرد
🔹
نضال حسن در ۵ نوامبر ۲۰۰۹ در پایگاه فورت هود تگزاس به سمت نظامیان آمریکایی تیراندازی کرد و ۱۳ نظامی را کشت و ۳۲ نفر را زخمی کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/695987" target="_blank">📅 08:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695986">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
بنا بر زمان‌بندی اعلام شده از سوی وزارت رفاه فردا چهارشنبه کالابرگ گروه اول مشمولان طرح شارژ می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/695986" target="_blank">📅 08:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695985">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ترامپ اعتراف کرد: با پایان جنگ ایران، قیمت بنزین و نفت به‌سرعت کاهش خواهد یافت
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/695985" target="_blank">📅 08:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695984">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
قلیان و موسیقی زنده در کافه‌ها ممنوع است
رئیس پلیس اماکن تهران بزرگ:
🔹
ارائه قلیان، اجرای موسیقی زنده و استفاده از دی‌جی در کافه‌ها ممنوع است؛ کافه‌ها همچنین نباید در فاصله یک کیلومتری مراکز آموزشی فعالیت کنند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/695984" target="_blank">📅 08:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695983">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIQB5Zlappz0aUm9KM-OJvO-xZU4SivYbtGPbrRgFPpNwyl5AuHN1833HvuqNS-nS-nFu_5zKFp-HZmP3-EXzfL7YTfsIcU5nMkyqQzc-_K6xiPvQ_99gTdrze5GzOFzT61pPs8K2RGLMQHLKKskNxI8PYMrDbF_34eti9jgDvc0yuaFqJglIDo2wuxaxEZlZSt-BXUvip-KX8rzDzVd6DCX1KcjYc6U7MSK6uO6IXvUSrtlSxqOqMaNE4tHFmkkfLJRWNJ6X4fGgmAYWFD0mcYzT5oDB0eej1cN6tzULjdQTvfKBNCncGnGLG4Fx4qCOVveTliULfQQd2jMyIMY0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط بالگرد آمریکایی در دریای سرخ
🔹
یک بالگرد MH-60R آمریکا نزدیک ینبع پیام اضطراری ارسال کرد و داده‌های راداری ارتفاع آن را صفر نشان می‌دهد؛ سقوط هنوز رسماً تأیید نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/695983" target="_blank">📅 08:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695981">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
صدور هشدار نارنجی برای شمال غرب کشور
🔹
سازمان هواشناسی برای امروز در شمال‌غرب و برخی مناطق غرب، مرکز و دامنه‌های جنوبی البرز رگبار، رعدوبرق و وزش باد شدید پیش‌بینی و برای شمال‌غرب هشدار نارنجی صادر کرد.
🔹
در شرق اردبیل، گیلان، بخش‌هایی از مازندران و گلستان نیز بارش پیش‌بینی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/695981" target="_blank">📅 08:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695980">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8nG8qRakF5KRo5E_7H6UssqeikkVdB0U8awAow_Ks7K2REQLp8sGzj8nqdbBCjeSsDgXP2HY1CzrnpTfwbYhYBLzvDkMNBHpZ7CLoWyMVrC_-4DKBAgPPr3--pv74vVgpRRpl9SkQKuz3Mky9MTtXfoolqqvu5l02dZ52ScXJoXyfWjQ-TyirN09_7a8UBVdMl8h5P3A3R52fTQTAcJQcU-jywgI3xMyWh18XSZ77FEQUeBSf_SjsDGSGL-UriaYvd0b_DAvr5U2xOmn7P6DK1HpDfx_qZ9NoygEaOkVKTYZ4c_s9hIzl3F962wAjVVB6kzjWNBKKe4QzGMYxl8Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۱۴ مهر ماه
۲۴ ربیع‌الثانی ‌۱۴۴۸
۶ اکتبر ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/695980" target="_blank">📅 08:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695979">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuVNhzCDIjtrBfBJZ2FBxyYIKJXy7L1QpePX5ZJYkSINOEA69tXFlvr-gnuD1AQqVwmuhkNvOGufkErZCgRWppeAZ9WO10J9iJ2mCftlvpY3UifsLijBi43oDVNXDPWrKwtgZV7kuSfH3B_lcJaCKRlcsvd3TtNEPcFNWh0jBUXGWLbndFKeIcjtENAa3OJ36MLPUC0rxKiyt936nVOgTvTFBeYEFNGre7EoImO6ujhjZNGGlMQYW-9f7ZqqsWH1rcgJfN8CMrovuWQjsIy3p7c0noYSX9xvzRKsW-krRJncSIDmScK-WrN3mmvP6FAa5HZv6pUY0NU9X_uB8aXiMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تک رقمی‌های کنکور ۱۴۰۵
موسسه عارف
🫡
💡
فقط درصدت مهم نیست
💡
جایگاهت مهمه !
🎯
هم مسیر رتبه‌های برتر
🎯
از همین امروز شروع کن
💪
موسسه کنکور عارف
🫡
| موسسه رتبه ساز | کل کشور
کنکوری داری؟
پس این لینک رو براش بفرست:
📱
https://t.me/+xVKhaZN3zi41OWZk</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/695979" target="_blank">📅 00:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695978">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGK79e_BaDxYuYhzpDnD4WiydSxq9iJafQDtB9mKhbcUWi7vD3_iSCRyY7LBc5AtjMAvJe4tdzJrvxWzm5kY1v3a1R0Ko-tHSm_MVKqSFx36t386Hb5iYI3rXUtPniCdqK6m7vGxeSIT0HIugfWgtX5ghd8h8WECpo6Sg90WU7ErtiQgnyAN1CGyF_TF1VLY82_aSDuRxbfG6dc2sfVbd-oqemRXo8e5dIejtzwEYGRIQ5d4gbmXvJarXUELlelIifKCsX-ckZcXqZfdnMlD3aAfO0lhB4uBDA0flMlWAZua8KzD0NyreaR_QDRjR5UNByXZfKEkUMkr6wI7YJ4mCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«الان بخر، بعداً پرداخت کن!»
📱
🔋
دنبال یه گوشی دوم مطمئن، خوش‌دست و جون‌سخت هستی
🔹
گوشی نوکیا ۱۰۶ (مدل ۲۰۲۳) – Nokia 106
▫️
طراحی جمع‌وجور، سبک و مقاوم در برابر ضربه
▫️
باتری بادوام با نگهداری شارژ طولانی‌مدت
▫️
آنتن‌دهی قوی حتی در نقاط کم‌پوشش
💳
شرایط خرید ویژه و آسان:
•
قیمت نقدی:
۲,۹۸۰,۰۰۰ تومان (
پرداخت درب منزل
)
•
خرید اقساطی:
۴ قسط ۸۰۰ هزار تومانی
📥
برای ثبت سفارش و کسب اطلاعات بیشتر کلیک کنید.
https://memarket24.ir/product/fast/63669/180124/
خرید قسطی
👇
https://memarket24.ir/product/brief/63669/180124/</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/695978" target="_blank">📅 00:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695977">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB308u1x1zskteLC7Jsk0dfAARl99G88mu0I1fFge2oLLO8zjqf6K-tboqrixqSOBu5GhizQ8wdtBWOdV-nVLVSD1pHH9mDv0E0a2dUMtvGxO_hHz7V05mWYesOAOrk2RiVbuSiBkL5KGT2QCKLlCYu6kIPDQSq6XvEp87acKfg5mPlTb0uzxIUbZQJKlnDfQb4DYTg3fcNLGhqVopjlxY8K5SnXbdohUBzCx1ZBfM_fgPPsNs4tn-ZBhphk8VbCOZ8bQImC6MXS-3MVz7OQNBhCm7gl4ADi96JMi_RS18r_3Co9XnWo0aiaLOnEKE65YqhQAortS_mChIJuQ3qFQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅️
سلام رفقا، برای شناخت میزان آشنایی جامعه ایرانی از سوپرمارکت‌ها نیاز به تعدادی پاسخنامه داریم
پر کردن این پرسشنامه کمتر از ۲ دقیقه از وقت شما رو میگیره و هیچ اطلاعات شخصی از شما گرفته نمی‌شه؛ در پایان هم به قید قرعه به تعدادی از نفرات
جوایزی اهدا میشه
🙏
لینک پرسشنامه
لینک پرسشنامه
ممنون از کمک بزرگی که به ما می‌کنید
🌸</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/695977" target="_blank">📅 00:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695976">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650f6da1ad.mp4?token=lLSDUkpr_AgobrkEQWUJZ3MZva8VSt2OlcwndIWItZJBtl0CyyU3jvOVW699vQZAZezNiq9loUIgLjKXUlRYIvELGckVema34JMEZjIQZtk8vgMu0BDqjF5thYwX9DV0nsh1ZdWTRsDa6YErTNbBre2HUYpACSvEyVJRiJfBJD6fIdQqMwYOQuUKRj3Ew7Qx7P2soo1QV68AaMbwKHTMEvoWd1uhuWri3bpbYHkWWrZaWs6uRap-BvRZAMxgAZeJyikTlZb4-pcNK7zvoxPUh2jlLQZEnyKko8uNJXU2WfO7TnWY8HFv4w_5ImYuLQcvdXtF0ON_WcBhIxz5uIZ6Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650f6da1ad.mp4?token=lLSDUkpr_AgobrkEQWUJZ3MZva8VSt2OlcwndIWItZJBtl0CyyU3jvOVW699vQZAZezNiq9loUIgLjKXUlRYIvELGckVema34JMEZjIQZtk8vgMu0BDqjF5thYwX9DV0nsh1ZdWTRsDa6YErTNbBre2HUYpACSvEyVJRiJfBJD6fIdQqMwYOQuUKRj3Ew7Qx7P2soo1QV68AaMbwKHTMEvoWd1uhuWri3bpbYHkWWrZaWs6uRap-BvRZAMxgAZeJyikTlZb4-pcNK7zvoxPUh2jlLQZEnyKko8uNJXU2WfO7TnWY8HFv4w_5ImYuLQcvdXtF0ON_WcBhIxz5uIZ6Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال شده از روتین غذایی یک خروس در فضای مجازی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/695976" target="_blank">📅 00:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695975">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada5338a9d.mp4?token=hw6wHFRY5o6SWO4067rXf9H445pILWhWvM3B3BicTVoKbogyz--ag0TX59obXDS0_KWz3ZBNAKIldNturfHfL6N9kBr8WXAS6HJOeYFil4ipzy2xkqLeAzsHxnKwk7R3_p7KeVRVuQuWZP3FW5lMloFS0dovuz-INMBY8pC_rDFN--WfNrb666KBfHFz96UE1qja0Na11BtNBd4YJbUkAdD7HgYW_JMgKJsaD-Ru5mPQtN9f9B0UwDQDPKQJvOwcTJUvKEcgv94MKYJqfipkLGLh0eaZH_Ux_Yy5t09vlRXE3YRt-vJHnAXEY29jCP_f4vC1eqfZc4sQjuRX9b8w2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada5338a9d.mp4?token=hw6wHFRY5o6SWO4067rXf9H445pILWhWvM3B3BicTVoKbogyz--ag0TX59obXDS0_KWz3ZBNAKIldNturfHfL6N9kBr8WXAS6HJOeYFil4ipzy2xkqLeAzsHxnKwk7R3_p7KeVRVuQuWZP3FW5lMloFS0dovuz-INMBY8pC_rDFN--WfNrb666KBfHFz96UE1qja0Na11BtNBd4YJbUkAdD7HgYW_JMgKJsaD-Ru5mPQtN9f9B0UwDQDPKQJvOwcTJUvKEcgv94MKYJqfipkLGLh0eaZH_Ux_Yy5t09vlRXE3YRt-vJHnAXEY29jCP_f4vC1eqfZc4sQjuRX9b8w2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگین‌کمانی که از دل گدازه‌های آتشفشانی بیرون آمده است
🔹
ابسیدین یا شیشه آتشفشانی زمانی شکل می‌گیرد که گدازه با سرعت زیادی سرد شود. در بعضی نمونه‌ها، آرایش لایه‌ها و بلورهای بسیار ریز درون سنگ باعث ایجاد درخشش‌ها و رنگ‌های رنگین‌کمانی می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/695975" target="_blank">📅 00:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695974">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
خبرنگار العربیه: وزارت خارجه آمریکا فروش بیش از ۲ میلیارد دلار تسلیحات به خاورمیانه را تأیید کرد
🔹
امارات متحده عربی: ۱۰ هزار بخش هدایت‌کننده سامانه مهمات دقیق‌الاصابت پیشرفته APKWS-II به ارزش ۱.۰۴ میلیارد دلار
🔹
کویت: خدمات تعمیر و بازگرداندن موشک‌های سامانه پاتریوت به ارزش ۴۰۰ میلیون دلار
🔹
مصر: سامانه‌های موشکی جاولین به ارزش ۸۳۲ میلیون دلار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/695974" target="_blank">📅 00:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695973">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
یک منبع آگاه آمریکایی: پهپادها احتمالاً از قبل در داخل خاک بریتانیا مستقر بوده‌اند
🔹
ایالات متحده نگران بود که ایران بتواند با الگوبرداری از عملیات اسپایدر وب اوکراین (عملیات تار عنکبوت)، حمله‌ای پهپادی به پایگاه نیروی هوایی سلطنتی فیرفورد انجام دهد.
🔹
بنا…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/695973" target="_blank">📅 00:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695970">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: ادعای درخواست پناهندگی عراقچی دروغ است
🔹
روبیو به عراقچی نگفت آمریکا را ترک کن. ما در زمینه وظایف نمایندگی، آزاد هستیم
🔹
برای نمایندگان تهران هیچ مشکلی وجود ندارد و پرونده ای نیز تشکیل نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/695970" target="_blank">📅 00:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695969">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQgRjdLSJm-450UoIQk3qA13hdQb8YagXyMk0mZCfD4xSnVSqlWuKzqeKwP0C-9Yl-eMqDNdv90GA1oZnr3FamxPSA9Nld80JA20ZdXG69Ssp_b6qk68SiecJuuqx8OO9c7mh9qYP1sX-knEP4O5JkJqj1DXHLl0wCSvwI68OYtqy8XeglMllPeWGQfhxYoh7t--4Ma5IqJfVOSBsjk01vCG-1TH2hIC-iOYrW-kY0N-1QYngOBqIF0nkF4BgfAzEZWPAl_nmEZQB0GN4tc3Ye5SzcGPPnqwcrP6HJimtOETryGEYamdd2CjcUxMT6h4whErdsvtwx9scT8Lv6Io4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باید دوباره دنیا را وارد قرنطینه کنیم تا تقاضا برای نفت را نابود کنیم
🔹
اقتصاددان و استراتژیست حوزه اقتصاد کلان و ژئوپلیتیک: این تنها گزینه‌ای است که برای پایین آوردن قیمت نفت باقی مانده
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/695969" target="_blank">📅 00:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695968">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdsEhAqgcQJbkUlMIzB_lRq41B6g2-L5TJy-jp97e_DURfi1ySQaX2xF-pD30E9PeChNccrMSaNKp68gwOlPhTkpbd8BU-45jizT5CiNgunMM2cUpWIrQN5IDVYU3OO6pHdxjNGZi5SKK1iNXOoIdo95cgTii2Cyv7Zhu20HjXg4Ygg69XAOs67oTNOlnAoMGVNQeomP5zs08meLCDb3MkSs3zrcxuCQ8AJSjrQ61h6Vs_hWLf-6Y0Fh9k_SdBkqSmE_IJQMu5dz2d8qcZ7HUtN31Hzb7GwLY8t9kFGB_qxBNGRRrskkhmQzvV3qyWXPLj4NHQJP3NM-ogVjwI-T2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/695968" target="_blank">📅 00:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695967">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
یک منبع آگاه آمریکایی: پهپادها احتمالاً از قبل در داخل خاک بریتانیا مستقر بوده‌اند
🔹
ایالات متحده نگران بود که ایران بتواند با الگوبرداری از عملیات اسپایدر وب اوکراین (عملیات تار عنکبوت)، حمله‌ای پهپادی به پایگاه نیروی هوایی سلطنتی فیرفورد انجام دهد.
🔹
بنا به گزارش‌ها، این نگرانی باعث خروج ناگهانی بمب‌افکن‌های B-1 شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/695967" target="_blank">📅 23:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695966">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7faea8050b.mp4?token=pcPx7vua104QLhmUFkQzczt5PoScO16oXmuh4ZM9CkX8384WmGn5lHbNURY0d2gz1h93DQROCYCF19OX4_7kFt8qURLqy92pPHcJ4DkYDYWO5F2Uo2OmOkG456zDdBprJY3i-JTX3E2bhh-yLNWww2zhJSP2WdOnrT0zgupynhot3Rk2kPCen5nV8CuNYtNMSR1Qb0RCZWWm80ML5rnst95ZyxBj6WJKTxCElwjMtJzhqY568SIwmLrtGbxHHy0yRs4JEIsn4NC97FkED3-0zmvlrBMwfOy0cjtlCsYwm0R5NV0gaf5Njb2rcjciGvVZ-67ieHzAzYg7lcm_emwVD3jmDsxhBE0V4uBAoSx1VSy72-SDEByKgsX5XrAPfzAhx9elslyQma8zmPCWIqIFQzwlNWe2AEAunsipLQFuVm_opyTs6JVxwzTGVEgrjN9C6GxxMiglHXPjmeryc3U3urWqhMDQQECQDSRG4QwDaiSRPCJiaesOYSdqO4p2czFi1A6_h0udhFJhZsuw03ngkvHXgqyJYBIvy_pJFZu48zumgYBLZMNPHcYWxCOzMGG_sXxxRUBfKpXq3bu7FZCxKgb8W-rKR6C7yFgsV53jCDvC81mpu31QSFlLXZW9MwOxoam1-FLh0qicrnJb7dxkJRVc_sue3qC-MwhrYhHgI1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7faea8050b.mp4?token=pcPx7vua104QLhmUFkQzczt5PoScO16oXmuh4ZM9CkX8384WmGn5lHbNURY0d2gz1h93DQROCYCF19OX4_7kFt8qURLqy92pPHcJ4DkYDYWO5F2Uo2OmOkG456zDdBprJY3i-JTX3E2bhh-yLNWww2zhJSP2WdOnrT0zgupynhot3Rk2kPCen5nV8CuNYtNMSR1Qb0RCZWWm80ML5rnst95ZyxBj6WJKTxCElwjMtJzhqY568SIwmLrtGbxHHy0yRs4JEIsn4NC97FkED3-0zmvlrBMwfOy0cjtlCsYwm0R5NV0gaf5Njb2rcjciGvVZ-67ieHzAzYg7lcm_emwVD3jmDsxhBE0V4uBAoSx1VSy72-SDEByKgsX5XrAPfzAhx9elslyQma8zmPCWIqIFQzwlNWe2AEAunsipLQFuVm_opyTs6JVxwzTGVEgrjN9C6GxxMiglHXPjmeryc3U3urWqhMDQQECQDSRG4QwDaiSRPCJiaesOYSdqO4p2czFi1A6_h0udhFJhZsuw03ngkvHXgqyJYBIvy_pJFZu48zumgYBLZMNPHcYWxCOzMGG_sXxxRUBfKpXq3bu7FZCxKgb8W-rKR6C7yFgsV53jCDvC81mpu31QSFlLXZW9MwOxoam1-FLh0qicrnJb7dxkJRVc_sue3qC-MwhrYhHgI1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: دولت ایالات متحده در مورد خطر شیوع طاعون از روسیه چه اقدامی انجام خواهد داد؟
ترامپ:
🔹
ما این موضوع را به دقت بررسی می‌کنیم. میکروب‌ها و عوامل بیماری‌زا قوی‌تر شده‌اند. ما به آن‌ها کمک خواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/695966" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695965">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
اگر فرصت دنبال کردن همه خبرهای امروز را نداشته‌اید، پربازدیدترین‌ها اینجا در دسترس شماست
🔹
🔹
نشانه مهم از تغییر آرایش نظامی آمریکا | از ۲۳۲ تانکر سوخت‌رسان تا ۱۶۵ فروند جنگنده | چرا احتمال جنگ کاهش یافت؟
👇
khabarfoori.com/fa/tiny/news-3250072
🔹
ترمز قیمت‌ها کشیده نشد؛ بازار طلا با فشار دلار صعودی شد
👇
khabarfoori.com/fa/tiny/news-3250124
🔹
حملات سنگین به یمن | پای آمریکا و پاکستان به جنگ باز شد | یمن تهدیدش را عملی می‌کند؟ | نشست محرمانه تیم امنیتی ترامپ درباره ایران و یمن
👇
khabarfoori.com/fa/tiny/news-3250188
🔹
آزار جنسی بازیکن مشهور فوتبال توسط مجری بی‌بی‌سی! |+ عکس
👇
khabarfoori.com/fa/tiny/news-3249918
🔹
طاعون از آزمایشگاه روسیه خارج شد؟ | آمریکا به حالت آماده‌باش درآمد | واقعا چه اتفاقی افتاده است؟
👇
khabarfoori.com/fa/tiny/news-3250121
🔹
خبرهای جنجالی را در وبسایت خبرفوری کلیک‌کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/695965" target="_blank">📅 23:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695964">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: سه عملیات منحصر به فرد علیه دشمن را با تعداد زیادی موشک بالستیک، بالدار و پهپاد انجام دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/695964" target="_blank">📅 23:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695963">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
آزادی بیان به سبک آمریکا؛ دولت ترامپ حضور خبرنگار خبرگزاری پولتیکو در هواپیمای ریاست‌جمهوری را ممنوع کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/695963" target="_blank">📅 23:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695962">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b31a9d3c.mp4?token=UpGrVXmXC0sA8KZEbzvV4sb22AsFWwwc1NuOssTjLgQsm5XDFZduDH0Oz6_JHL2w8jeudmvbmMoPF2yNdmSA3L4Q2O39oqgnQqa-uZbmbt1gTz-yz0gy4LsSAqonu73LVGXWLuKiofdAzB0CDurwuMZdTA0V_4YEAGsCOJ0ZvY-n8TyBh4KnfLbnhqEdq_dtbGAeOVP9S-lfPtfYAYemvyKjuMiWZElu5ESG6HpX_yMobvKWUGmZqjNcdOdm3deRCEI9QeumDOsC-2NWCJaPb7AIitzMR0FWwrKm-y9iHH-5WzCrv0KrMLGRnHBPHoypd_0SREU1-M82AIujmml_xUcIX_0mU85-x589RzLvLylWMZ5h0IiS_vtGIr78q5P9ZxtsV-Impozt6NZcOsWckrFOogGlSbwlK233OFhJJfjPZusl5lP3ICBSrHjjS7qsHY5-V2FgIDV0CPzica68EhmG1HgmxYOHc6kt5vuFM-v0nQaqwWRtJ2hh8OH-Lte8AwISoZnn3oDO7Kbd3QaVGvKzF01Iqb5DQQFqrCUfiFt3340Ca-y13BWh4Nlpuwx4fZDnHgkijy_BOAaOX4yYoML90IwWaasCoKLLTBISbwQwdeXKviQzRpiLnn-hYnIQ-Rs38bi_uRtkNIIfvtixa-TRrmzWESj46T_xOP5mjNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b31a9d3c.mp4?token=UpGrVXmXC0sA8KZEbzvV4sb22AsFWwwc1NuOssTjLgQsm5XDFZduDH0Oz6_JHL2w8jeudmvbmMoPF2yNdmSA3L4Q2O39oqgnQqa-uZbmbt1gTz-yz0gy4LsSAqonu73LVGXWLuKiofdAzB0CDurwuMZdTA0V_4YEAGsCOJ0ZvY-n8TyBh4KnfLbnhqEdq_dtbGAeOVP9S-lfPtfYAYemvyKjuMiWZElu5ESG6HpX_yMobvKWUGmZqjNcdOdm3deRCEI9QeumDOsC-2NWCJaPb7AIitzMR0FWwrKm-y9iHH-5WzCrv0KrMLGRnHBPHoypd_0SREU1-M82AIujmml_xUcIX_0mU85-x589RzLvLylWMZ5h0IiS_vtGIr78q5P9ZxtsV-Impozt6NZcOsWckrFOogGlSbwlK233OFhJJfjPZusl5lP3ICBSrHjjS7qsHY5-V2FgIDV0CPzica68EhmG1HgmxYOHc6kt5vuFM-v0nQaqwWRtJ2hh8OH-Lte8AwISoZnn3oDO7Kbd3QaVGvKzF01Iqb5DQQFqrCUfiFt3340Ca-y13BWh4Nlpuwx4fZDnHgkijy_BOAaOX4yYoML90IwWaasCoKLLTBISbwQwdeXKviQzRpiLnn-hYnIQ-Rs38bi_uRtkNIIfvtixa-TRrmzWESj46T_xOP5mjNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سبزی خوردن فقط دورچین نیست؛ یک بخش مهم از سفره سالم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/695962" target="_blank">📅 23:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695961">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: سه عملیات منحصر به فرد علیه دشمن را با تعداد زیادی موشک بالستیک، بالدار و پهپاد انجام دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/695961" target="_blank">📅 23:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695960">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
منابع خبری از توقف موقت کلیه پروازها در فرودگاه «شانلی‌اورفا» در جنوب ترکیه پس از هشدار وقوع بمب‌گذاری در یک فروند هواپیما خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/695960" target="_blank">📅 23:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695959">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4V9A3dTDM-dZAH31koANb4cGvsr_edtZC5QlgmNugmKomESR98s68gvpRhTzAb5nCPr8UGfP-ftyvv_BcRTLY0OwsQSUhA0PAIMfm_0iB4oFIUf9tlSoNMXGItSOMJnb06oywTarfyjpkPSuTRggHHabxNCQa_TVlHxsPktSQ2iOjdKG_vQPQBzBz7Egqpj1OztOLWgSbHRobwmE9mN_PPNWhjNPhAa26Y0Wb7dScYTTV2UurxiBoTt7MSPgmi41Ogiv4QFWGLhcEH7q-EHo1QX6VTttb6mUJx8sksQSU13-2RXKtuDkrl65puDE3XZEMsOurWJDTGNLv-PXbOkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از صاعقه در گیلانغرب/ امشب
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/695959" target="_blank">📅 23:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695958">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ug2usIj7XR70PLMZR3C-6j6w64bdleUm55pvgkVS6mCObkkiG2j7ciBv8-QZE_-5rPa9_3y3a6k7sqHnJMWCWB3iYHBzUHFkBCW0SF0ziq6SJ0iMGJa3qFtSczE7-p-tMWhdr4W98uKyrulBxe9yOOwCN_4luzECGY0oHp17bdOwUBP8QHJT8eWs4S1AHzRNgOKDZ1wXVP024HYUEY90LUCg62lfEj0ZpoLVsdCrKbp7N4kNb5yaJzyxMSJu2y3nJs1JmMQlTqadn3N4mOEe75n460KptzBKbL-WS8zy2qK37818l3NkKnGJjgLqIss-rCTF0iPE2C1Pzo2C6-JkJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرور وحشتناک‌ترین اپیدمی تاریخ با ۷۰ میلیون مرگ / یک خبر نگران‌گننده: طاعون مجددا عالم‌گیر شده؟
🔹
مورخان تخمین می‌زنند که جمعیت اروپا پیش از طاعون حدود ۷۵ میلیون نفر بود. تا پایان سال ۱۳۵۱ میلادی این جمعیت به ۵۰ میلیون سقوط کرد. در برخی مناطق، مرگ و میر به دوسوم جمعیت رسید.
گزارش تاریخی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3250225</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/695958" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695957">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
شلنگ باغچه‌ سوراخ شده؟
قبل از خرید شلنگ جدید، این ترفند ساده برای تعمیرش رو ببین!
🔧
🌱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/695957" target="_blank">📅 23:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695956">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون انرژی: استعفای وزیر نفت به دلیل مسائل پتروشیمی خلیج فارس و تراستی‌ها نبود
فرهاد شهرکی، عضو کمیسیون انرژی مجلس در
#گفتگو
با خبرفوری:
🔹
استعفای وزیر نفت به اصرار خودشان و به دلیل مشکلات شخصی که داشتند، بود که بعد از دو الی سه ماه پذیرفته شد.
🔹
مسئله تراستی‌ها و پتروشیمی خلیج فارس در مجلس و کمیسیون انرژی مطرح نشده است.
🔹
هر مسئولی اگر در زمان مسئولیتش اتفاقی بیفتد، حتی اگر استعفا هم بدهد، فردا روزی باید پاسخگو باشد و اگر تخلفی باشد، به تخلفش رسیدگی می‌شود، اما این مسائل برای وزیر نفت مطرح نبوده و استعفا به اصرار خودشان بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/695956" target="_blank">📅 23:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695955">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOAcbWmNwbCo-WPbv-qcQCZ-zqzygKZz0vPP28_qYKCJ1qxgmz3hy9yPLtzyfpisEkMlMHRXqx6bDtW-cjWk5dgh9156ZM-7xsY2gelktFvNWJVOO9GTRpcE6aYR4hQlv2mmDO3lvg2Cje1E7aJCC6lHGfJDC2OD-I1xReaN7_FgNV9wjXvAue_Nv7nyaXhs3TFzMGb0xfwXo3x5mrgmjA6DCJrr9yx9FNgJKGMTbRQPUI87seTa3Y8jzv18TQCymd39bWAx7q91XwAwfFAofYTlagdc2cYJzpK1aYKGvXIYQ2ShJa6Jku52tjgzeaizaJQAOvWJ0wXBoG4eKC-ykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی ایلان ماسک هم در پاسخ به یک اکانت توییتری اسرائیلی، از کار افتادن استارلینک توسط ایران را تایید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/695955" target="_blank">📅 23:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695954">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای ترامپ: من معتقدم ایران مسئول حادثه هواپیمای فلای‌دبی است
🔹
ترامپ: عقب‌نشینی بمب‌افکن‌های آمریکایی از بریتانیا، در پی یک تهدید صورت گرفت و ما می‌دانیم چه کسی پشت این تهدید قرار دارد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/695954" target="_blank">📅 23:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695953">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtyWRzmS32DQ8a96lRhUy8F1OfeJbyHELAY02ZGs-AFwYTXFp9LcZLpdFEjzy3dKEUMD9JMKsk751k2ydVem2k8e--NKJQhQeEyzB_lY_VnUorDVNU0Cw2AUbM_2IJXLyQQTuqiATGfFeItZUMvTSgUQHjdtSgf8etZ0fis6cI2k14YYVxKNKXTBgRhAlr4rnqMIt6efyxy0h5r0sJyWMvrVal_4g34_eeAlCoQcYnNw5xR7TakYMgc8iVwTzBMKkDepKL5lB6ikgK8ofpOmrqyN3mS32aFlvrqaq3vuq2XMFOuQSgds6c4m2SMm0neImaG9x9i-eqJ6WaRQQ6OGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسوشیتدپرس تصویر دیگری از حمله پهپادی ایران به پایگاه محل استقرار نیروهای ارتش تروریستی آمریکا در کویت را منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/695953" target="_blank">📅 23:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695952">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ادعای واهی ترامپ جنایتکار: همیشه آماده گفت‌وگوهای مستقیم هستم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/695952" target="_blank">📅 23:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695951">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668e7e80f8.mp4?token=nRL_HxUbTDohrT5N83ETkAL0dd-VOKJSEDvOU3zqlP3pjSVIllG1PVGwknJoPrnon1Yi4lkWJBJw7oQ35cpiTRX3LSXmrOY9PHU1xZnJ8YuB5rcAMbNWRoPxjzwp557IdNN6bAqK4pRPU0bbcztJ26TVVq-JVH-6qtXR3yKRbhAuSLOmUmwAkz9D1wpWcHTFwD7Cp9fv_jHDJ8L5Xs0jcfOq6tGgsdLcwuS4JFnRR7vLjKLOUVWrm7q0C8akTjJt-C65x6F1-TmlqjQgBRVh9mfHeoNHFkDCT2eN7Fswac1OUESigEtj05Aya3AHp3QhNWJoxM_t-hIQojGpa7jrq41wWrhG_95cqg4t-FiHb2HNVxIe5SBTPonzz_ZOhh4ixqmyyi1B_T6NGd6IfFApKYN9_1m_5s5jd9BY3cBsjysedEhFq8SI1SJ7DqlHjYH6S9Rv9qqD9NoJhFh9SwOHxRdBwp4ZG6OeH2ueraWNytcrmD5NDLfhBpw8ScIdWJGWHPrw6E03ppqJxFqMbIzGe2iGwM_aTUFRi3vmDMbPyGs8-Jw6iiGkdB7OD_NrdJSJcRfVubLDnC8Xmm5g4q56seRj04VmTPqZKnU687AmV_LoINvKEuyDyt9NUAjkjhD4yEdj3wfZXd3jvWUbMUBHSGySPLhZUFhAv-xkRnDNtso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668e7e80f8.mp4?token=nRL_HxUbTDohrT5N83ETkAL0dd-VOKJSEDvOU3zqlP3pjSVIllG1PVGwknJoPrnon1Yi4lkWJBJw7oQ35cpiTRX3LSXmrOY9PHU1xZnJ8YuB5rcAMbNWRoPxjzwp557IdNN6bAqK4pRPU0bbcztJ26TVVq-JVH-6qtXR3yKRbhAuSLOmUmwAkz9D1wpWcHTFwD7Cp9fv_jHDJ8L5Xs0jcfOq6tGgsdLcwuS4JFnRR7vLjKLOUVWrm7q0C8akTjJt-C65x6F1-TmlqjQgBRVh9mfHeoNHFkDCT2eN7Fswac1OUESigEtj05Aya3AHp3QhNWJoxM_t-hIQojGpa7jrq41wWrhG_95cqg4t-FiHb2HNVxIe5SBTPonzz_ZOhh4ixqmyyi1B_T6NGd6IfFApKYN9_1m_5s5jd9BY3cBsjysedEhFq8SI1SJ7DqlHjYH6S9Rv9qqD9NoJhFh9SwOHxRdBwp4ZG6OeH2ueraWNytcrmD5NDLfhBpw8ScIdWJGWHPrw6E03ppqJxFqMbIzGe2iGwM_aTUFRi3vmDMbPyGs8-Jw6iiGkdB7OD_NrdJSJcRfVubLDnC8Xmm5g4q56seRj04VmTPqZKnU687AmV_LoINvKEuyDyt9NUAjkjhD4yEdj3wfZXd3jvWUbMUBHSGySPLhZUFhAv-xkRnDNtso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی یکی از گوش‌های ایرپاد صدا نمی‌ده، چطور درستش کنیم؟
🔹
راهکار ساده‌اش رو در این ویدئو ببینید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/695951" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695950">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 7- میدان هفتم، صبر</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/695950" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صدمیدان خواجه عبدالله انصاری
🔹
میدان هفتم، صبر
🔹
آن زمان که قصد الهی خود را مشخص شده یافتید و به درک آن رسیدید، می‌بایست در مسیر تعالی استوار و مقاوم باقی بمانید
🔹
صبر توانایی تبدیل آزار به لذت به کمک نور و حکمت‌ الهی می‌باشد
🔹
هرگاه در هنگام دشواری صبر را پیشه کرديد تغییرات مثبت بسیاری در زندگی خود مشاهده خواهید کرد
صبر سه قسم می‌باشد:
🔹
صبر بر بلا (به دوست‌داری توان): یکتایی دل_علم باریک_نور فراست
🔹
صبر بر معصيت (به ترس توان): الهام دلها_قبول دعا_نور عصمت
🔹
صبر بر طاعت (به امید توان): بازداشت بلاها_روزی نابیوسیده_گراییدن با نیکان
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/695950" target="_blank">📅 23:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695949">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
اظهارات مضحک و تکراری ترامپ: مقدار زیادی نفت از تنگه هرمز عبور می کند!/ شرایط در تنگه هرمز نرمال است! #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/695949" target="_blank">📅 22:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695948">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
اظهارات مضحک و تکراری ترامپ: مقدار زیادی نفت از تنگه هرمز عبور می کند!/ شرایط در تنگه هرمز نرمال است!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/695948" target="_blank">📅 22:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695947">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a7fba16c.mp4?token=SIurKgnIxQScsx5mp2mh9WIvPpA6UNnfP0gyR4pS_jzyJbfZ81cCBzpI04wxjGoIMzzkRooNI0BiEJyV81gj58gOqyvRW0M_NyO05V1QvN57wwHQKFNjjiteBz5CWoamMBBl57HGml50xngUSSa_gz120O6XeLOwLl9xOFgqu2pvjiawk6QUlR8nI65NeN9DAEXEjo7PwybyBaAG0Lqx1QclsdnARBzWnUNHen1JZ-jwypBwnM7OVyLCRKF3UGmJUbPNsXTOOp83jXcXj0a5X2p5xv1rC5SUiPdnT0_hNkHjoMIKtltrSAuGiCRK5Xw0zsoxuhduunEAJPTxxA58LHXaPId_GzkS641rD3Qqc0DnxrLZ4DrO7Hf2qzUCwcnrQ5w4FjeIJzZOhRZe44FDMc7tDBa5Nz9lNieeOQRFi0RtKg-H_CzRWE3mMy8YjRbumRT-XD86bJo36bXe3HgaWxkaGE9C17Pq061cv5EDph1_3idJOYRV2fNnZ-AYHNcQIm3dEwSuKhHmkm3SCketbEqn0nTbKDd5V0sIwjwgYiVqOIoo3gJIQcEXcGnu5hLZZtAuFmIT5vY18A2vYY4GuJm-uOdDh8H-bva1DqobUEKYEtS3xhdi2KhkydtYFm3lcGPOpK-EkcToqD_QqSRxiWAid6mGnXeM6hHCqesujgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a7fba16c.mp4?token=SIurKgnIxQScsx5mp2mh9WIvPpA6UNnfP0gyR4pS_jzyJbfZ81cCBzpI04wxjGoIMzzkRooNI0BiEJyV81gj58gOqyvRW0M_NyO05V1QvN57wwHQKFNjjiteBz5CWoamMBBl57HGml50xngUSSa_gz120O6XeLOwLl9xOFgqu2pvjiawk6QUlR8nI65NeN9DAEXEjo7PwybyBaAG0Lqx1QclsdnARBzWnUNHen1JZ-jwypBwnM7OVyLCRKF3UGmJUbPNsXTOOp83jXcXj0a5X2p5xv1rC5SUiPdnT0_hNkHjoMIKtltrSAuGiCRK5Xw0zsoxuhduunEAJPTxxA58LHXaPId_GzkS641rD3Qqc0DnxrLZ4DrO7Hf2qzUCwcnrQ5w4FjeIJzZOhRZe44FDMc7tDBa5Nz9lNieeOQRFi0RtKg-H_CzRWE3mMy8YjRbumRT-XD86bJo36bXe3HgaWxkaGE9C17Pq061cv5EDph1_3idJOYRV2fNnZ-AYHNcQIm3dEwSuKhHmkm3SCketbEqn0nTbKDd5V0sIwjwgYiVqOIoo3gJIQcEXcGnu5hLZZtAuFmIT5vY18A2vYY4GuJm-uOdDh8H-bva1DqobUEKYEtS3xhdi2KhkydtYFm3lcGPOpK-EkcToqD_QqSRxiWAid6mGnXeM6hHCqesujgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی پول‌های کوچک مردم کنار هم قرار می‌گیرن، می‌تونن کارهای بزرگی رو رقم بزنن
@Tv_Fori</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/695947" target="_blank">📅 22:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695946">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
عربستان اعلام کرد که ائتلاف مکه توافق کرده تا در واکنش به حملات حوثی‌ها به خاک عربستان اقدامات بازدارنده جمعی را به اجرا درآورد
🔹
این تصمیم پس از برگزاری نشست اضطراری «کمیته راهبردی سیاسی و دفاعی» این ائتلاف در ریاض اتخاذ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/695946" target="_blank">📅 22:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe3z60IRrmTZkZvwBvxXwfgp3wX2mkHehlCOW3cHTOvoCkRNgCJ7K9pDuH_lVuLCqCZHN1nGUACJEvU1P8n2DdVGctciJTbrpW0pzjkg2DhKoQWN8Y6jQhcPRZ7_bQapWXPF77jQR4JQ4ExKpk5FOZE0WcSugTN4utF8bY4kTVmrGa60qTXwx_agtcsKKZKD6vDK4cNtSKJWVMG2SxYRfK80qEjXi-L8NLc6_h0Mn-UnlDxAjH1bslWo2UH2ES3SvftJ9-WOSCkMMlY6Z4OuQditPHmCXWe_yiGfC6_RttkmlbCShIRh-rm-D6DhInGdCKgdO0o2Z51yWlkAzF5DNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPJyEIsGausOMmRCNsj62Jc2yAtEk-NFPK4tgs_IadlWw7i5izyZ56ws40Pim1Pv7TVM6cV7p0jIH8FFhDcV7z4JlOfFD_7-MVPo9WFCoXOdfne2EibYHz17EhyE1nsQHUvyIAVOuOASdiNAhD5gyb3zQk-mqN-tmgzuRiaB2T-AySJ657yiL6Vbx3yHVHlESDaGX9UmH4zmV4QbCJ0AWgZzPrgXahwGVuysLDDg8wB3YO5WWArJ40XRyBoXx1prqujEAkKQUUGXPu6pHqCONFTzrca7S5hntZ_2Yk4R2flHhuFKJpIaeC_MQyKsDxpQhtwDhFMaYWjOOuIBqoemdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWrDwQ8Wsfg-b35co3fml7Yubkw8wbKCexsZW7S5XIxluzNh5Zy_x_7ClOI2ZGuN-th-dYXAWmt-RHi-2Wr7m3nRRc7o65C3dg9vlUSn-Rmc5_r1vvMiSxAt8OenIAWpu6uSNf6VJJDeD9NMHMr1DxM8YiKVG2f0yLXerxGjeEHRNhzB-RG1kByK6cAcoWRu322jOXt4er3ioUIPpbho7NG3lPZgdIbMAUP20HVE5G58wUhD_0u1EOJFRonROffRDaCothPPMNHzp07sEZVrBco47efmzeXbR7Y8iLLq-JOE7zXhWSkOfA6rB910NJK3z9hN6qt0YvZPDADovPTgiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWOcKoIkDUTC-1NRwmG23QfzF_Sdh2uZTJb-HXCt1_gkhOrT0yoIoVbNlshQ5IhsgU8FVXNwPS6mNTz4FUzEpiMTrHyZQPxqJrQy6X8L71wr90nEa3KVpEhpxtUYt63WzwkS50uIUg0JAEg151gzlPzvJqDkYTEFaZ4ppGe6bPFGqeuDG8NmWfHcXFaf9WLB-YCP6uLSOxNRCKpB5q447lw1aGC6N1vu5NQHqYhs7gFsJND4Q1UbgFg58t75SfxKwL2Z4caercq9g_WQKyzGvE2p5En4n15tLhKWV83Ufx1zDJBkYW917al22Mkms7E3Xv-tYVrgvZVCi3gntGte6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRihr1H33WTagxG90Z68a8O1Zk4qXK_zVolJlRwwbmBd25ZLHTmQB07MY-j9OB7Lpl5FGS95c031XmvmsW5VH2iz7TrwR52DIwT6Eetuaw0JgCgKBkhOvgFt_Gwc-1Zs_5WJJB-abFw4mo0kkDiR5jBGmx_qosDX6buV8zMYVkmPJG0BwVqrcprhOLVsi7daw4Fcc7Y3K7YY0_qCCBLZZUmorsCpRz22R8p1IaSJBeVkx1uTKgv4YF0jSE3mkkXE6q0gDonYB20D4CsKZjXGsY3NE4zRhHJM9o27iQTPEwFR93UiqJEYXryQXEOOZd_YdHEDHS-D7fY2OyS9rAvOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auka1K_J0FSn8gnDVpBg--03TxNFBBEOvvqUmcJkP8p4_OEw8zarReERnKQgpKkYmzT6bUvpcUMaHBlFehFb7BQvF9-3qywhvylR2_JW3hPlMCs-tg4BMIMD-fIJF4ZkjWad8Yo7ZRk1pG2mn0Zcwi5kL4f_oyLDWefAw4E7KukJmXzmn3nGZ0OnFVFySQlSlVipORTwFBf_povhZGHksfVtrOrrWyo4cJ-i3bHF3QJZBNblZwLSUsGhQAOvjSJu67-YCu3o8qgdEjIbfI6orC9jNdyjl5hcAqmkV2nsJO3cX39siBbCA134vYYMC5VCXRUmAGUL2gPF-iEKYFP6Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چیزهایی که هر روز می‌بینیم، اما اسمشان را نمی‌دانستیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/695940" target="_blank">📅 22:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd281cff39.mp4?token=UQiTIWGychDXI1BEuVS7kwmSdnp0hkh90-utfDLufQ9fjjZB4Myca3iuPK5fR677PJjqHwWzwQlPgi9EUXZtKsQ_ACoGq4RVwb490fGapgGMM02L-Lh-AbyTXK8Y-UiLo-75lZ4xKwVqADh9lZuACDhPC6vDKbSgp3w98EQmsWsLlOHZMVieZtFU-Qgkb1mK_-3AemHIaNjOAYI3fOdIK2VcEYgWIF-lkCS57t73G8YcPYodTSQlfuvWeBYbFFCUZeZIRwklgulmzQrBjh1lIMJi8N-3ledte6RD6Q_ryCZoWfqu0OJGP7pY6b8FlIclFpTwMx93inLI28KXDbxVjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd281cff39.mp4?token=UQiTIWGychDXI1BEuVS7kwmSdnp0hkh90-utfDLufQ9fjjZB4Myca3iuPK5fR677PJjqHwWzwQlPgi9EUXZtKsQ_ACoGq4RVwb490fGapgGMM02L-Lh-AbyTXK8Y-UiLo-75lZ4xKwVqADh9lZuACDhPC6vDKbSgp3w98EQmsWsLlOHZMVieZtFU-Qgkb1mK_-3AemHIaNjOAYI3fOdIK2VcEYgWIF-lkCS57t73G8YcPYodTSQlfuvWeBYbFFCUZeZIRwklgulmzQrBjh1lIMJi8N-3ledte6RD6Q_ryCZoWfqu0OJGP7pY6b8FlIclFpTwMx93inLI28KXDbxVjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عاقبت یک نفتکش در تنگه هرمز پس‌ از تخلف
🔹
تصاویر جدیدی از برخورد با یک نفتکش متخلف در تنگه هرمز منتشر شده؛ این نفتکش به‌ دلیل نقض مقررات و هشدارهای دریایی، متوقف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/695939" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMPKi31KGzITB7wUf1t9lcxfxx13KebRj07M-A18XsBV-yAOQ_V3uH0hqEfLJlYxZ39gkBjnFVyGJRiaC0B4Px5LHsO0u1sawLwbZ-crYCvWH2-d46lNlvseDHXNuPLBY19FR0TDvvETF0Qdq75mtzaE5JjRSvBBucwqtQokKlMCvH6Y9TZSv7oaoTip0vMBmgJHbZwuqZzCygkXymZLa90jUdukLRZZsDtNlXYVIEpMdtLCpeG2yNXoWGUP2g17kUkSSEBktvEPPOZcSkRN6Ki8KmZ3cacCyJqIOboCS9ziiSTjr9lPTUSilO5G_bQEVThF-ygl6EPgI_HnF4jIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ نشانه مهم از تغییر آرایش نظامی آمریکا | از ۲۳۲ تانکر سوخت‌رسان تا ۱۶۵ فروند جنگنده | چرا احتمال جنگ کاهش یافت؟
🔹
در شرایطی که احتمال ازسرگیری حملات آمریکا علیه ایران همچنان یکی از پرسش‌های اصلی در محافل سیاسی و نظامی است، برخی نشانه‌های میدانی از کاهش تدریجی آرایش تهاجمی نیروهای آمریکایی در منطقه حکایت دارد؛ روندی که البته به معنای منتفی شدن حمله در آینده نیست.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3250072</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/695938" target="_blank">📅 22:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnBN1c-p1VtnpeAJkwESWb3vUDnAPsMg_bXP-UJz75UR-DCktYijbKkLcpTbKjiIDEEKLSFg8KUI0g1b7xczwdsJRhEbShA5a88bSZuZGL7Vic2HYcD0tlNkdXJp5rYHucw9WoutE13ZUe1Goeg1Ht-_Bgy_udvS93tBg1ZuD66QWRoNDnEFm-pVodCyJfA2wDloMI337F0qcjjte6tZ0y3y4NxMUgkIEtR_kQnGsC6kMzn2k7Dj_SD7mBv0n_FlsIeRKdTng_w1DyrB0xcqcpvAAoA7rIQ9c6ac4VYIOp8MaWioqCasIJTyZM-B7QjGlR3imLboYXwbf3q6pQj7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیستی از ۱۰۰ قرص پرمصرف همراه با کارایی هر کدام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/695937" target="_blank">📅 22:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تامین مالی از بازار سرمایه، راهکار مدرن بقا و رشد شرکت‌ها</div>
  <div class="tg-doc-extra">گروه فیروزه</div>
</div>
<a href="https://t.me/akhbarefori/695936" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔵
تامین مالی از بازار سرمایه، راهکار مدرن بقا و رشد شرکت‌ها
گاهی اوقات سفارش هست، بازار هست، خط تولید هم آماده است؛ اما اگر پولِ خرید مواد اولیه و هزینه‌های جاری سرِ وقت نرسد، چرخ تولید کند می‌شود. برای بسیاری از شرکت‌های تولیدی، گره اصلی دقیقاً همین‌جاست: تأمین مالی.
در این فایل صوتی با پرستو ابوالقاسمی، مدیرعامل شرکت مشاور سرمایه‌گذاری دانش فیروزه درباره تامین مالی بنگاه‌ها، شرکت‌ها، سازمان‌ها و واحدهای تولیدی از بازار سرمایه گفت‌وگو کردیم.
🔙
مشاوره تخصصی و رایگان سرمایه‌گذاری
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/695936" target="_blank">📅 22:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
یک کارواش در آمریکا با کارکنانش تم هالووین زدن و اینطوری مشتری‌ها رو میترسونه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/695935" target="_blank">📅 22:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای
اسرائیل هیوم: اسرائیل در حال تدارک گزینه‌هایی برای حمله‌ای دیگر به ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/695934" target="_blank">📅 22:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMTHhMtvjhx6JFhmhd_QIEUvOkFz18hnOXT0Tlcn5kHxYIegnAv4w8pmc_usqLOCu8pDLW-vzlE1VS5TNbk6jkwhY-7Gv5V1HHEeJYwMpldEDw6p7ZK73wxvPLFuuUOfMz05Xzbk8WAzqO-c3j6kz7ObuOqyD1B5_Av60KpOM1HKzMPTqK1KyjARl9wx_oVMVqJPemh1AVmxUDxodvfvjYp2AiNe8FM_mmRdYrsWWPWBnmlCjwL4wRSvwj50KxDXpz9fELCF-LQODM98bhamId1qETygk8h9vruFqXUZIhBjVM0wXPSE-hCXIKNnz2pkq95UfIBrkT7saHW_9wUMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشت عفونت ناشناخته از آزمایشگاه طاعون روسیه/ ۲۰۰ نفر قرنطینه شدند
🔹
یک کارمند ۲۸ ساله آزمایشگاه ضدطاعون روسیه پس از شکستن تصادفی لوله آزمایش حاوی نمونه زیستی، به ذات‌الریه ناشناخته مبتلا شده و جان باخته است. حدود ۲۰۰ نفر قرنطینه شده‌اند و احتمال طاعون ریوی…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/695933" target="_blank">📅 22:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbcd65b81.mp4?token=PzLdiORBqdsqCpdEkFIcOLAHEbnBHvZbUzAaQDvhN0BprZrrKjsFWMTkmwpdec01NB58TTsQw5Un-E8H6ry5haY3a-UxdcV8X7i17hB3jzOhZQTPsKi7byrDQkA869-SPD9yBAZmUEGarnaSmS4fzeK2PfBI7PgYiXlaN8UkY_dSMniJp3Fck5f3RoeghFEG0aUJdlpPj3YXqbw0my_m6xb5Ugu9CN0iHOE8XqmBSkq2x-VA3CRydsbXGjVfquSE50n308dy9LYK2f1DHk0qNWOfnFSqj_P14sAaAbSWMH7Stlb0qvo-ggtMgpbY7l6a3IBaa48qvHM1oMCUrzcYuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbcd65b81.mp4?token=PzLdiORBqdsqCpdEkFIcOLAHEbnBHvZbUzAaQDvhN0BprZrrKjsFWMTkmwpdec01NB58TTsQw5Un-E8H6ry5haY3a-UxdcV8X7i17hB3jzOhZQTPsKi7byrDQkA869-SPD9yBAZmUEGarnaSmS4fzeK2PfBI7PgYiXlaN8UkY_dSMniJp3Fck5f3RoeghFEG0aUJdlpPj3YXqbw0my_m6xb5Ugu9CN0iHOE8XqmBSkq2x-VA3CRydsbXGjVfquSE50n308dy9LYK2f1DHk0qNWOfnFSqj_P14sAaAbSWMH7Stlb0qvo-ggtMgpbY7l6a3IBaa48qvHM1oMCUrzcYuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله تروریستی به خودروی شهروندان در پل جکیگور راسک
🔹
بر اساس اطلاعات اولیه، این حمله توسط عناصر گروهک تروریستی جیش‌الظلم انجام شده و شهروندان عادی هدف این اقدام تروریستی قرار گرفته‌اند.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/695932" target="_blank">📅 22:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1QAQB3qb8biszRevLW8535CWG6IC7hHNM1QUa-DTMPkNsndiQ1I1ev3-r7uE7jCu3jlHTcd3SUD0VWDWcle-gXzj0P1IliUosiqqHhuM15OCm9zvNTptrvd5XRQwsS9YSkN-y6JqsIoFjL4juwPTKqN2WOqB5yfC-VmLbsju8x3bTGYb0QjwthiG1r3G2GfmHxzZmaLbQjFfuFo7sZiRX35USKe0XRAgLeXu9QB5LEgCIH8XDpOvW-wpVy0SE9T8mBB00XtVL8ey49A-1VXVpvP6y8AW7G__2cIGaKT6255z0gyPpah8-QXhJcDCtQlYQiJqiNFrmRR5GgfoIda0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
علوم پزشکی وارستگان (اولین و تنها مرکز آموزش عالی علوم پزشکی غیر انتفاعی کشور) فقط از طریق کنکور سراسری در رشته‌های زیر دانشجو می‌پذیرد:
🔬
علوم آزمایشگاهی (کد مهر:37358)
🔬
علوم آزمایشگاهی (کد بهمن:37359)
🥗
علوم تغذیه (کد مهر:37360)
🥗
علوم تغذیه  (کد بهمن:37361)
💻
فناوری اطلاعات سلامت (کد مهر:37364)
💻
فناوری اطلاعات سلامت  (کد بهمن:37365)
🏥
مدیریت خدمات بهداشتی و درمانی (کد مهر:37368)
🍏
علوم و صنایع غذایی (گرایش کنترل کیفی و بهداشتی) (کد مهر:37362)
🍏
علوم و صنایع غذایی (گرایش کنترل کیفی و بهداشتی)  (کد بهمن:37363)
👩‍⚕️
پرستاری (کد مهر:37356)
🚑
فوریت‌های پزشکی پیش‌بیمارستانی (کد بهمن:37367)
📞
05131771
🌐
www.varastegan.ac.ir</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/695931" target="_blank">📅 22:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91ec4c629.mp4?token=kSOJvTNmL9eK_L7rW5vxdfT79sGcul0dEzD9Ln9i3n96Dl5O4EsbZj61aqnsRmD7PETHzzQ7DYT0F7bAyXRkkmk6pY7WjFpSIL86BcfBLaCci1aB9hAZ2N3_ehxy9wDZ36a1tCXRdxpCa2YGmcLvSdrLacgkIInuHkzT7pvwKCEsbqUJKDuzpolK5_L_beO9i9e9W4gZn4LGStR_tq4-86wkHAV07kE4J5-LYgeWqo77AoIh1NdS0yacM4JuxEI3iR7EmXnX7OZYdd4pLYq8YDbjqhDigs5kuCTircg9YWXrYLGW7PjbU6MANHgAsLQbAYtqvsEqrrZp7mtsiNdIGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91ec4c629.mp4?token=kSOJvTNmL9eK_L7rW5vxdfT79sGcul0dEzD9Ln9i3n96Dl5O4EsbZj61aqnsRmD7PETHzzQ7DYT0F7bAyXRkkmk6pY7WjFpSIL86BcfBLaCci1aB9hAZ2N3_ehxy9wDZ36a1tCXRdxpCa2YGmcLvSdrLacgkIInuHkzT7pvwKCEsbqUJKDuzpolK5_L_beO9i9e9W4gZn4LGStR_tq4-86wkHAV07kE4J5-LYgeWqo77AoIh1NdS0yacM4JuxEI3iR7EmXnX7OZYdd4pLYq8YDbjqhDigs5kuCTircg9YWXrYLGW7PjbU6MANHgAsLQbAYtqvsEqrrZp7mtsiNdIGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرود افغانستانی خوندن پیمان طالبی مجری برنامه سرآشپز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/695930" target="_blank">📅 22:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
امروز سیزدهم مهرماه، سالروز برگزاری نماز جمعه تاریخی نصر در مهرماه سال ۱۴۰۳ به امامت رهبر شهید است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/695929" target="_blank">📅 22:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
افشای طرح محرمانه عربستان برای حمله پهپادی به کعبه
🔹
منابع منطقه‌ای از طرح تیم امنیتی سلطنتی عربستان برای پرتاب پهپادهای «لوکاس» ساخت آمریکا به سمت مکه و هدف قرار دادن کعبه و مناطق مسکونی اطراف مسجدالحرام خبر دادند. در این طرح هدف قرار دادن چند هتل نزدیک مسجدالحرام، از جمله هتل انجم مکه و پولمن زمزم، و همچنین مناطقی در اطراف مسجدالحرام پیش‌بینی شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/695928" target="_blank">📅 22:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a0c44aaa4.mp4?token=QhbjLBjr1BHHzS3uOIoB3mUSwlAYZ66PfT2vISJXBX3OKnVeg9QF3QwPsY46qVw9MCg5RXwa7KtHw6KX9Zwakf5aw4yGmnJ5ubGfuPf51DnAodWd2CWOtfayeDc6IUdXi7_24JTAnGjG7EztHGi8I7pOydBuiGN7Kleu87DR3a9N0QX-cy2v1QYaXA_YWpwG3jVgK7qh9qTBKWJ45aPoPrWGrvILW9cTNfod29douekpzPscn2XSG86PWXQtIeFCdA-RHPsVYVaz4KUThrWxiKxkdx3-8SfcKQFoEG7sSl1n0LKg2PCxOX-8dLVVG6mhxMy4JK1gN1Yj8xx5_dGjQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a0c44aaa4.mp4?token=QhbjLBjr1BHHzS3uOIoB3mUSwlAYZ66PfT2vISJXBX3OKnVeg9QF3QwPsY46qVw9MCg5RXwa7KtHw6KX9Zwakf5aw4yGmnJ5ubGfuPf51DnAodWd2CWOtfayeDc6IUdXi7_24JTAnGjG7EztHGi8I7pOydBuiGN7Kleu87DR3a9N0QX-cy2v1QYaXA_YWpwG3jVgK7qh9qTBKWJ45aPoPrWGrvILW9cTNfod29douekpzPscn2XSG86PWXQtIeFCdA-RHPsVYVaz4KUThrWxiKxkdx3-8SfcKQFoEG7sSl1n0LKg2PCxOX-8dLVVG6mhxMy4JK1gN1Yj8xx5_dGjQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفع دردهای مختلف از زبون خودشون
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/695927" target="_blank">📅 22:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a037aa0fa.mp4?token=eQOKRnHprxpeMuyhj5xm5E8RreRbOQHgRqKCMuPKmX4ZCXHYGTN4VerXzpKIzHcaQjNaeTGFII2AfHm0bhGVBcpLJatQ9ivkCdqaJoTouOyOu-IFcyz_rangHLBnfyEHimJ2NRoYFCvwW_PjTt3aNgeEzvmjBu-ZSjn_Vt6XwCKAXDxOJZ0-RqqXbeWv9YN7dnscm_n4fGaPDvPsvis2rETSfTdxchQiaJiVRkj6XFndP1qh9gjCg9gKPQzQYjj2xBibWcai41WLJHzos5Rh-YevdTdFzzUXp79oiyBCgfhcABVw5P4x4YPrxBKm5LTE5sd1gZAzdSQ5uSHdbSyr-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a037aa0fa.mp4?token=eQOKRnHprxpeMuyhj5xm5E8RreRbOQHgRqKCMuPKmX4ZCXHYGTN4VerXzpKIzHcaQjNaeTGFII2AfHm0bhGVBcpLJatQ9ivkCdqaJoTouOyOu-IFcyz_rangHLBnfyEHimJ2NRoYFCvwW_PjTt3aNgeEzvmjBu-ZSjn_Vt6XwCKAXDxOJZ0-RqqXbeWv9YN7dnscm_n4fGaPDvPsvis2rETSfTdxchQiaJiVRkj6XFndP1qh9gjCg9gKPQzQYjj2xBibWcai41WLJHzos5Rh-YevdTdFzzUXp79oiyBCgfhcABVw5P4x4YPrxBKm5LTE5sd1gZAzdSQ5uSHdbSyr-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین ویدئو از شهر طاعون‌زده‌ شلخوف در سیبری که مردانی را در سطح شهر با لباس‌های مخصوص محافظ سفید نشان می‌دهد
🔹
هم‌زمان گزارش‌هایی هم درباره قرنطینه شدن بیمارستان شهر و کمبود آنتی‌بیوتیک در داروخانه‌ها منتشر شده!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/695926" target="_blank">📅 21:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX0HZOctQuTi186tnvhSYM6hIR33HrY0vGGfQwF6DVgykyHuoGwiO_3tBm0jBWxdnvwMNo5MhgIEPZHOL4XXL_wT0x4dRf9X-S-FwOTOxRZdsUh_ED3kN8s_xEdGfeKK5vtX5Dv7iJAhuni8xTAiuDr9XQtAIt4KLvUjmi5BVVw49SXcHLNSebOrM-mJrwurG3IkxARiUDbeRiBmOcLblnsHRqSQtMwAXwi9v-SnCAf5ci50Zete3XXLrh0BTk-U0qePP_Fc_GZU86K061ju5xxb7XT_3KUOka8cu2GKad2Aw3mjJ53__znKe2slhcURXFCVw9xFsGVKOz6M86976Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریشه‌های شوک ارزی در شرایط جنگ و محاصره
🔹
پویا جبل‌عاملی ریشه اصلی شوک ارزی را کاهش شدید تجارت خارجی و درآمدهای ارزی در شرایط محاصره و جنگ می‌داند؛ وضعیتی که به گفته او، صادرات کشور را به حدود یک‌پنجم گذشته رسانده و بازار ارز را با عدم تعادل روبه‌رو کرده است.
🔹
او تأکید می‌کند نااطمینانی درباره درآمدهای آینده دولت نیز از مسیر انتظارات، فشار تورمی ایجاد می‌کند. به گفته جبل‌عاملی، تا زمانی که یک چشم‌انداز اطمینان‌بخش در محیط بین‌الملل ایجاد نشود، ابزارهای اقتصادی به‌تنهایی نمی‌توانند بازار ارز را آرام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/695925" target="_blank">📅 21:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
عربستان اعلام کرد که ائتلاف مکه توافق کرده تا در واکنش به حملات حوثی‌ها به خاک عربستان اقدامات بازدارنده جمعی را به اجرا درآورد
🔹
این تصمیم پس از برگزاری نشست اضطراری «کمیته راهبردی سیاسی و دفاعی» این ائتلاف در ریاض اتخاذ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/695924" target="_blank">📅 21:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR3AcaK2VXT-j21_pujrVXehOv4DRCPCH1GEUVaQS3RdSLogySTit3PVjIymTqjhQLMjgGBILd9E1Kz3eBekBVXcqbkAxyTeO1Uhc3iulSwET1-Uz4rptin5um5DhSIe8POE5kaHlAk0wGgb-ne6-9La3gVexzutiCKWvfGfytnSUsd-YGAjg1Yk2yVQ1ql5_CiiT5DGAU9sM-GJId-oEsUwjM71vB4K-dHlqvYgtgZeWR1eI8w5cRgfu2YjL0X8-MqlZ0Y5ZwYSj-aWjE1CaBfIzgRA9qC44lyCtpIahJV3vXBmm7c9892HK6ou3fv0dAVWhryoue0mylFp7hRQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صورت‌حساب سنگین ۲۳ ساله آمریکا در عراق
🔹
از هزینه‌های تریلیون‌دلاری تا آوارگی، ویرانی زیرساخت‌ها و پیامدهای امنیتی، مروری بر میراث حضور آمریکا در عراق.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/695923" target="_blank">📅 21:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
آمریکا با فروش تسلیحات یک میلیارد دلاری به امارات موافقت کرد
🔹
این قرارداد شامل فروش سامانه‌های تسلیحاتی دقیق و تجهیزات وابسته به امارات است که توان عملیاتی این کشور را افزایش می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/695922" target="_blank">📅 21:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS_Z2uqJD3Hobew9w9hNoS5NicTIM3nNnShS7iF-I60ZMkknk7xbGiERBnrKQjMlPVu7vTQNABxqFBWP-Sq_4MftiHTQMpqUn0QsTr6trmQM0yx9LRnNlUwZkF6uppOl6jGqV03y8EnggCAVgmlOeZQ-DA2yyUyLxSp4WZmSkHgn3sHCXsjl9FJN9-EKyUILpuyETimKyLXWfzzW9UzxZJa4T0buyk7QAhzKo-PFxpLA1MjaindXXJRMbg4lI8lmXZfwXRxa8CYhzmwnX34yCLs8tc4omrVSyuze4Pcc7FvYCvyu02NToa8hfT5_kxppJCCC69HI_Z7bOng0zS9zng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دعای خاص استاد شفیعی کدکنی برای ایران: ان‌شاءالله ایران سربلند و مستقل باشد؛ صددرصد به ایران امید دارم
🔹
استاد شفیعی سرش را جلو می‌آورد تا صدایم را بشنود. «شما برای بچه‌های ادبیات با کلاس‌هایتان همیشه پناه بودید. آینده ادبیات ایران را با نسل جدید و این‌همه تغییر چطور می‌بینید؟» می‌خندد و جواب می‌دهد: «والا غیر از خدا هیچ‌کس نمی‌تواند پیش‌بینی کند ما دعا می‌کنیم که ان‌شاءالله ایران سربلند و  مستقل باشه.»
🔹
یکی از همراهان می‌آید کنارش و می‌گوید: «یعنی امید دارید به آینده‌ این...» شفیعی‌کدکنی سرش پایین است و اجازه نمی‌دهد جمله تمام شود و می‌گوید: «بله. صددرصد»./ فرهیختگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/695921" target="_blank">📅 21:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
حمله تروریستی به خودروی شهروندان در پل جکیگور راسک
🔹
بر اساس اطلاعات اولیه، این حمله توسط عناصر گروهک تروریستی جیش‌الظلم انجام شده و شهروندان عادی هدف این اقدام تروریستی قرار گرفته‌اند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/695920" target="_blank">📅 21:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiWaP9hTEYE66h9EOT2XAm0MuRwGouZ4YdHdqu0sePFvtiKgue2uBAAdKMHQA7uf-0AMLli-oQDjl98XPQ5TKZY5srRH96nITHWyseR71FLteci3o5afTwczzOPuTwwGNbFf1vOYevpd_snSPVWo7IR5sUuiVRTgKHYfPDKAfGZw8DpebyXzd0VW9BUiRTnC4LQGyEeHTM0xKFRsuMzPRPFkxiQ_Sz9kEcvZlOShhxbSUrPozneNoxiT-orgZ7U_QrRPtEp87k7oMB5hT_pfsWbRbOHKnp8n9ddcLBiceJVilIY28lWJo0WMfJEpwNUKQMfC_RwXddbbvX9N4pp9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تجربه فرهنگی با اعتبار دیجی‌پی؛ کنسرت همایون شجریان در شیراز
🔹
کنسرت همایون شجریان به‌زودی در شیراز برگزار می‌شود و فروش بلیت این رویداد از طریق
فیدیبوآرت
انجام خواهد شد. دیجی‌پی نیز به‌عنوان حامی مالی این کنسرت، در کنار فیدیبو و دیجی‌کالا حضور دارد.
🔹
در این همکاری، کاربران می‌توانند با استفاده از
اعتبار و کیف پول دیجی‌پی
هزینه بلیت را پرداخت کنند و در صورت استفاده از کیف پول، بدون نیاز به ورود اطلاعات کارت بانکی در لحظه خرید، فرآیند پرداخت را سریع‌تر انجام دهند.
🔹
حمیدرضا سعادتی، معاون سوپراپلیکیشن و مارکتینگ دیجی‌پی، این همکاری را بخشی از توسعه کاربرد خدمات مالی دیجیتال در حوزه فرهنگ و سرگرمی دانست و امیر بهدانی، مدیرعامل فیدیبو، نیز از آن به‌عنوان بخشی از مسیر توسعه فعالیت‌های فیدیبوآرت در حوزه موسیقی، تئاتر و سینما یاد کرد.
🔹
این همکاری با هدف ساده‌تر شدن دسترسی مخاطبان به تجربه‌های فرهنگی و ایجاد زمینه برای همکاری‌های بیشتر فیدیبو و دیجی‌پی در حوزه هنر شکل گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/695919" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695917">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47e78e0ce2.mp4?token=ds_Tv2p26b3pR8lSpJwjcDvH1JjO0udE4koO5wbpJOPlYvnE93Sdjqzr9WsNHaAvaqZSHuOThui6Y3OI6e0D0o2xPeL63xE7tOf2MYEPU-ED0tjNK4Snl_1WrIND3eGEbDYmoHFqXOjZoVL2pwey9OfYnSk1UqyML2p7cxYbpVK4izjPBXPH9JwgcfHdyFhCdIx7VqmhmkV3DGHcqpJMU-IIM90hhp9zDCJ12OB8KLe9uI4dC1LH0f1jJNfG0vNnhcOwv7C1SFVtW9SmNTXIYW8QHAgr8l4ZeYuEbbXBssYp7bcnWoAef9IPPpnq-Qm2WBYmKO0M0HLa0qZWGiVWJIVCSxKdH1qXZItNkXF6jFf6vFOVLpRyMBdADpi5e5-SOxMLVob6Ms3fgIzURMhZBfp_ceWsjhRqI4W5nt_mTdM57KQWSfKbAE-IzAxCadVSKeawjmm-kyJg1yew-o7FwNe2tLpx7V-BwzdS-ANKhtq3ZyLBB-EpY4-2sK-4utHFuZvaR3O70unS95fVh9uuHxDdrdUunE-adFHgaROHrt8u84AR6s_nJwAJr8MORoiGPRRl56yoETHje3DjDxUJuJ2EPAamMVbS4xnaoLfuCqAoui1rOeM7wwF-nSxT_qhJL0Nh1edmYfRrMSPr5n_0PLeVAkoDymcSGnZHkVizrV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47e78e0ce2.mp4?token=ds_Tv2p26b3pR8lSpJwjcDvH1JjO0udE4koO5wbpJOPlYvnE93Sdjqzr9WsNHaAvaqZSHuOThui6Y3OI6e0D0o2xPeL63xE7tOf2MYEPU-ED0tjNK4Snl_1WrIND3eGEbDYmoHFqXOjZoVL2pwey9OfYnSk1UqyML2p7cxYbpVK4izjPBXPH9JwgcfHdyFhCdIx7VqmhmkV3DGHcqpJMU-IIM90hhp9zDCJ12OB8KLe9uI4dC1LH0f1jJNfG0vNnhcOwv7C1SFVtW9SmNTXIYW8QHAgr8l4ZeYuEbbXBssYp7bcnWoAef9IPPpnq-Qm2WBYmKO0M0HLa0qZWGiVWJIVCSxKdH1qXZItNkXF6jFf6vFOVLpRyMBdADpi5e5-SOxMLVob6Ms3fgIzURMhZBfp_ceWsjhRqI4W5nt_mTdM57KQWSfKbAE-IzAxCadVSKeawjmm-kyJg1yew-o7FwNe2tLpx7V-BwzdS-ANKhtq3ZyLBB-EpY4-2sK-4utHFuZvaR3O70unS95fVh9uuHxDdrdUunE-adFHgaROHrt8u84AR6s_nJwAJr8MORoiGPRRl56yoETHje3DjDxUJuJ2EPAamMVbS4xnaoLfuCqAoui1rOeM7wwF-nSxT_qhJL0Nh1edmYfRrMSPr5n_0PLeVAkoDymcSGnZHkVizrV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطارهای معلق ووهان چین؛ واگن‌هایی که از زیر ریل آویزان‌اند و کف شیشه‌ای‌شان منظره شهر را زیر پای مسافران نشان می‌دهد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/695917" target="_blank">📅 21:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695915">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ اسرائیل: کمک‌ خلبان فلای‌ دبی قصد داشت آن را به فرودگاه بن‌‌گوریون بکوبد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/695915" target="_blank">📅 21:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695914">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
یکی از فرماندهان پدافند هوایی خاتم‌الانبیا: ادواتی از دشمن به غنیمت گرفته‌ایم که در آینده نزدیک، به لطف الهی علیه خودشان استفاده خواهیم کرد
/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/695914" target="_blank">📅 21:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695913">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا حسین زاده؛ یادداشت ها، صحبت ها و سخنرانی ها</strong></div>
<div class="tg-text">#یادداشت
📊
داده ها؛ سرمایه های جدید صنعت بانکداری
🔸
در گذشته، سرمایه اصلی بانک‌ها را شعب، ساختمان‌ها و منابع مالی تشکیل می‌داد؛ اما در عصر تحول دیجیتال، داده به یکی از ارزشمندترین دارایی‌های بانک‌ها تبدیل شده است.
🔸
هر تراکنش، جست‌وجو و تعامل مشتری، اطلاعاتی تولید می‌کند که می‌تواند تصویری دقیق‌تر از نیازها، رفتارها و ترجیحات او در اختیار بانک قرار دهد. تحلیل هوشمند این داده‌ها به بانک کمک می‌کند نه‌تنها بفهمد مشتری چه می‌خواهد، بلکه بداند چه زمانی و با چه خدمتی می‌تواند ارزش بیشتری برای او خلق کند.
🔸
با این حال، داده به‌تنهایی ارزش‌آفرین نیست. ارزش واقعی زمانی شکل می‌گیرد که داده به بینش، بینش به تصمیم و تصمیم به اقدام مؤثر تبدیل شود. از این منظر، رقابت در بانکداری مدرن دیگر صرفاً بر سر جذب مشتری نیست؛ بلکه بر سر شناخت عمیق‌تر مشتری و ارائه تجربه و ارزش متناسب با نیاز اوست.
🔸
در کنار همه اینها، یک اصل اساسی وجود دارد: اعتماد مشتری. داده‌های بانکی بخشی از حساس‌ترین اطلاعات زندگی مالی افراد است و استفاده از آن باید همراه با امنیت، حفظ حریم خصوصی، شفافیت و مسئولیت‌پذیری باشد. بانکی که بتواند داده را هوشمندانه، امن و مسئولانه به کار گیرد، نه‌تنها خدمات شخصی‌سازی‌شده‌تری به مشتریان خود ارائه می کند، بلکه می‌تواند از داده ها یک مزیت رقابتی پایدار بسازد.
داده ها، سرمایه های جدید صنعت بانکداری هستند، اما اعتماد، ابزار مهم حفظ این سرمایه است که نباید به هیچ عنوان آن را از دست داد.
@Mohammadrezahoseinzadehh</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/695913" target="_blank">📅 21:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695912">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9eb85747.mp4?token=JUIxMvOyqNRrjiOg3fsUm1xuTYH5-ZYOJ9JCS98p6z2rsrYEC9cf1qvXJ_XVqNzHE7dB3uQ6S5ZnKqM2EFPTGU9Y6pzU4F-XrNtIDqmx7qZdlkNQivScNh8wnlVjiC-B8EiHFZYjClWxrBwKPjOBGmHQ4Qk5n9Qf6FtlPQ33-Kay3jP1DJle1mfhwjUOmE0-Xjf5hw0loOyRqjfMcSNLxP4G-gw8N8DOLAGqVWY1I4konK0_yykJ8pNNWD1J5lrqG4EuZDrGWDhkPES-P6j8oJMi2wQLh9VjfnsDR3MpeNdC964WlKvzqzEAlByIb98Jw6PjB90RPKf32MdN0v9YcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9eb85747.mp4?token=JUIxMvOyqNRrjiOg3fsUm1xuTYH5-ZYOJ9JCS98p6z2rsrYEC9cf1qvXJ_XVqNzHE7dB3uQ6S5ZnKqM2EFPTGU9Y6pzU4F-XrNtIDqmx7qZdlkNQivScNh8wnlVjiC-B8EiHFZYjClWxrBwKPjOBGmHQ4Qk5n9Qf6FtlPQ33-Kay3jP1DJle1mfhwjUOmE0-Xjf5hw0loOyRqjfMcSNLxP4G-gw8N8DOLAGqVWY1I4konK0_yykJ8pNNWD1J5lrqG4EuZDrGWDhkPES-P6j8oJMi2wQLh9VjfnsDR3MpeNdC964WlKvzqzEAlByIb98Jw6PjB90RPKf32MdN0v9YcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های یک دکتر: حالا که هوا سرد شده به‌خاطر یک سرماخوردگی بلافاصله آنتی بیوتیک نخورید؛ بدنتون به آنتی بیوتیک مقاوم میشه
🔹
یک پسر ۳۲ ساله و یک دختر ۱۹ ساله به خاطر یک عفونت ساده فوت کردن. چون از بچگی به خاطر سرماخوردگی آنتی بیوتیک میخوردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/695912" target="_blank">📅 21:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695911">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
اداره ارشاد خراسان رضوی، با لغو کنسرت علیرضا قربانی در مشهد، اعلام کرد: با توجه به «برخی ملاحظات» کنسرت به وقت مناسب دیگری موکول شد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/695911" target="_blank">📅 21:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695910">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9xHr1nMFZzCF8dBVkKNITfI1Kccz9Dg8GyBjxVGDkj5-kcknp7Cd_zU4qW3Q_Ywv6FEIAqi0lyqFImMf7NM-ngghHvWMFaZ2aMO1hUFg-h4QRQ1J6Yd5VV6J7pmwjZaA8v8cqXmGrcYKf8wHQyejLnpXg6C1mtznzZIyux8gQRjQn_dFZIPRKBbeN3uiGJ-gVsepvAS8aQJi5owR6GEYCpYB7Y187KTzwC5ElHRW6YqmJLXaJq2NHe-9aIEMz1Un0F-Z0P_Rszr9WVBJbZM9pFUNLF1eMukn3ltbaBomwqQWIzN7a-VuqYYXczDdMCyhzGltpsucvqB2dM4_zz8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای هر کاری، سراغ کدوم هوش مصنوعی بریم؟
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/695910" target="_blank">📅 21:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695909">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efda9da751.mp4?token=td8jXMe0fnD6lxo4uPAwutkffOobiVcWtA0fD6T12E7c4cv5wdQd4GbkENaOYoTOATKE04K0TWsGHstN39uF3H3aanrWXqcNtzDdX59ml9Ldd5BgL4oH-IX-3V3Bw9jE7aBvy0qy4bKMJUHfdqsqPpeq0rkMQQY5zoexYrdVlAd_Q1qvcEM9GlKvC_hmBypM2gpn_BeJk4VO1zysXCRSrF4rBQNgVrmvFVIJm9vGpDQS8xWlMJkJfcL3qDI8hmuG8nHpj4CFAxYKEb8XABD8m6grPj7XtSQlxYK_MxzZoyVfm0x876WqrsRFYlOjW_007_DpeAjjWEvP_ny6CsYKoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efda9da751.mp4?token=td8jXMe0fnD6lxo4uPAwutkffOobiVcWtA0fD6T12E7c4cv5wdQd4GbkENaOYoTOATKE04K0TWsGHstN39uF3H3aanrWXqcNtzDdX59ml9Ldd5BgL4oH-IX-3V3Bw9jE7aBvy0qy4bKMJUHfdqsqPpeq0rkMQQY5zoexYrdVlAd_Q1qvcEM9GlKvC_hmBypM2gpn_BeJk4VO1zysXCRSrF4rBQNgVrmvFVIJm9vGpDQS8xWlMJkJfcL3qDI8hmuG8nHpj4CFAxYKEb8XABD8m6grPj7XtSQlxYK_MxzZoyVfm0x876WqrsRFYlOjW_007_DpeAjjWEvP_ny6CsYKoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این اشتباهات پولت رو قفل می‌کنه!
🔹
یک اشتباه توی سرمایه‌گذاری هست که ممکنه باعث بشه پولت رو، روی یک دارایی نگه داری که دیگه ارزش نگه‌داشتن نداره،
اما نکته ترسناک اینجاست که ممکنه اصلاً متوجه این اشتباه نشی، چون این بار مشکل بازار نیست، بلکه احساس خودته!
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/695909" target="_blank">📅 21:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695908">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سفارت آمریکا در عربستان هشدار امنیتی برای آمریکایی‌ها صادر کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/695908" target="_blank">📅 21:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695907">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtMs3_qIy5BYpPrk5deIk4NvPetiJLhcPjTZ6esFVcRvCy9BwLBNswD_Xt5LbPycIrthDfaQDjGyzXoRv-F_2gLCyahOib71M84evqQhQ4TGawXazljnv7qNn5cBwCkcrYc_PgOBB8p3otB-5ayqe4NOlvfI6KQVKfSKlPvAybDfyXu47PsaaxXcgjlgssK-xi9k3hFpWfrR-PZsSsne9JZ2hH1Fp7v6BF5aByCfSh8r0wdEBtbqm-VjPSSPjWDlnarDvmHx0bCusEKEjex_FC2OpeTLTfcg0okAZRWS0fjmeWnsuk6hpMEBAjDAHiA8ZYHE_jQOfs4Gaw_NfYwybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جشنواره هدایای رویایی اسنوا
🎉
با خرید و نصب محصولات منتخب
🎉
—— بدون قرعه‌کشی هدیه دریافت کنید ——
با خرید از اسنوا، علاوه بر دریافت هدیه از تخفیف حین خرید هم استفاده کنید
💰
⏳
فرصت، فقط تا 15 مهر
❗️
🔥
برای اطلاعات بیشتر وارد لینک زیر بشید
:
👇
👇
👇
https://lnk.snowa.ir/snowa-telegram
.</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/695907" target="_blank">📅 21:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695906">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک گردشگری | TOURISM BANK</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyzpjQAezmA0-vr0HN3XkuPXm56rF5IkawCe83D5f2ovb2Pfr_vsMwSdkZEuZlM4_aE5uS2FMeFtn63XLyg1mAcxUC65QOSPxJwBCUe-jOliUUA7OzrQR2u9Tt_DbnPKDwZbhDfy1A6QTCVDdIBry_BM8hb3ardSyOsy4rpEmmBAUc2nhoJ1sl8OIJU-bhHSCqqE0a45QGO15mHk6lN8aInduV-ugXpEfyiZQN8I3GPgpuUXYCKVimCr59MlD6v9tCVORVlOIiRduZ7CttC4YLQ12nRcQm_AA0YXM5rYdLCF1wLVgxzIqIAthJsJJzenkXsa_qNz8546leMXrQtxcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
تمدید شد!
قرعه‌کشی حساب‌های قرض‌الحسنه پس‌انداز بانک گردشگری تا۱۵مهرماه تمدید شد
دارندگان حساب قرض الحسنه پس انداز با حفظ یا افزایش موجودی می‌توانند در قرعه‌کشی شرکت کنند.
🚀
هر ۱۰۰ هزار تومان در هر روز = یک امتیاز
🎁
جوایز: ۲۰۰ جایزه ۲۵۰ میلیون تومانی، ۳۰۰ جایزه ۱۰۰ میلیون تومانی، ۴۰۰ جایزه ۵۰ میلیون تومانی، ۵۰۰ جایزه ۱۰ میلیون تومانی و بیش ۱۰ هزار جایزه نقدی دیگر.
📅
دوره محاسبه امتیازات: ۱ آبان ۱۴۰۴ تا ۱۵مهر ۱۴۰۵
🎯
قرعه‌کشی: ۲۶ مهر ۱۴۰۵
💳
حداقل موجودی برای شرکت در قرعه کشی= ۲۰۰ هزار تومان
افتتاح حساب و افزایش موجودی:
🔸
مراجعه به شعب سراسر کشور
🔹
آنلاین از طریق اپلیکیشن توبانک:
tobank.ir
کسب اطلاعات بیشتر:
📞
۰۲۱۲۳۹۵۰
__
🔴
بانک گردشگری؛ فراتر از مرزها...
@iran_tourismbank</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/695906" target="_blank">📅 21:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695901">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSfMj4vMdIT3dlfHhTFWceXPQhtPNkjuQXzNt7hlMbl9jkzY8Yw7uVP1ztypHyPJTfS6ahjzJd10Y7YXgCO0_whZ_KK1TFm_Msr_2RCTBw6mIkcQ_BA0QBT2Fap9if2tySJgrCSqtKGnRnihpeFl4vXzzVqL3vAWseJMprCo8VslAx7jFJ98-E-wY-frhDCwx6AG7CtZxwnmvaHnwjjZNHtEpVqpJzZxENikiR4CD7R0nlurSO1wnvc42ykCF_Qdg3mERKFeHzz7PXrBZ_VxbsWSNTo-r1KceWuk9dwaGxgxfqaVnF2Gy8jNUUJRv20JmbFYUzDinvFYKn_S7MQzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRvb5kSS6z67vdOxwwgF_1dRQlhd417owVis4ILMMpu7CMS7nGA2gbqQY6l8Ia_VrVX0612YpN1fPxtxlTwTdC6cEKO1V7jY-3DCG_Hda6bZtIlWvVQ1UF2F3Iba_Zf6WOQHW3YboAlQh_-qxpd2L-3CpI4IH__7jIlCsD_WsU0jkJJnpc5ydg5YG2zQt3x1mARgzHAxj504eWL1am53AYGreb5hPMGFYE3FVffT7YntYUpFAj5OEOgGlmvgp1Pa205gbFuaEnEnAOCuvwGQc6RLdPPEgercG4tSyWHC3miJ8hSPAQT-iSF_dR9CiO2wIENP3su_4PWB0NeolBr5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIF8p6BK4f2U7CpUTR8wxUOUOcZfaJBX83zGxJJXOhEzqaJT152NJgHs-DiPJ0l197g9SDRqvnAcikaFyYUloAuuL8PCf9UNvBNrfQkPh_0JwyiLy0fHu2tPSfPFWK4cdpEE6DbeCXbMDX_V1M1i2kw2mLB_LZ4KdZz5B8og1hV84uRrCS_GRsjs4O9F2vKU_T3y3X5zb0KQ6LAM009s86f1YaoxOgEmhJe0wTSEwZdkhcMn3BBO4jJ97E3JS-oRZVZL4hnTOgpHa9SjCe4a8XTA840nMjPzyEKRB6YBFZxR9gYBwacNbqN51gHwvY2Wu08IlE15QdLVKHk1xqAwvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgC3NW7TqU-dgZ3eKrekhZ6MUc_qb8aUurqU4LLjjw4dFksdfz3nF8xdtqQeDuLz369CvVxnUpTCf1Hoxf4r1Vv371bkPiDfWtPZ1bZ1tVBMZM2N8cJkgjnML8eLXynFeM2DGtmUWclRXL2aRUTuYnWCkMwdrxNRDgz7jYXr54XcG4qOvoPPM3JCyOEymUt2rR0oMHRSeNtB-EpDwMDBUiRXX1IlKJ1rXD0yUeRztpFT1aUyLiBkI_msOSeDduwyM_NJxAjcci1HD0E_ZZDkkFlqHilehd92JaB5qIbQoGargiciK6HUJuXaMeXluZDhtwlbE_8rvu2InFsAA2fjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eB9U03riCS9I9JH9NPqamhUYg_GR6d8Uvh6u14TgT7vxmlPEoDpxF1HB-AqAlV0QQLFA2Hfk-vMfXUnQeV-UlTdHO7HrQIJAYoH7l6gHLv_Y0-21jOl-lotH-MqBvoKRHODOowMhXCCPUMQy26dMQaWAiOJreCyBNiv2Ca8_WQBGXlaH4b0Y1erc20d8kj295oXzvhWc5fC8bLxocxY3d5bgj5exhsG63SR_CnSNxcEuvNgMMnmNDaZ1C3lmMeWHLOF4oOazAPVum0sMGQQ3m-WrI1-_7f9bjdQDWka9568U_3vzUmnI5KL_b86NOWnuznulhNDFwas8LjABw1cM6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جزیره بان‌وول در کره جنوبی؛ جزیره‌ای که در آن همه چیز بنفش است: ماشین‌ها، خانه‌ها و گل‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/695901" target="_blank">📅 20:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695899">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGdITTRXQVW_qjCJ5U6VBClibYc03BM1pqtAVMbgVx38g45OPMnermXITzorv_4tgWXBrzc_JYHmc2k98H0YNVClR5QDEmNz1kI4fpjjNXXx56xqbtTOqDy8LM7o9ZCNujUJQXfWH_Fj_alJ-yt4L2O28E0q4foGhB5BRwJZrESZsvJnUTeYvmEKAhGpgPkPXr2qDpamh5rEnJxVMgdJd78ppu_4fjx_ogqD45hE_JFlNNRsMesLdcuVrOUpLj5QTDblP0OO1Oon-mvxXRhPwZKPNRpO8gTVLoUJflgRlRznUgfaDJqmWjgOfmfqriz5NLQx2K2xm_lhUl6OIXCiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وعده‌های نافرجام رفع فیلترینگ
🔹
در این اینفوگرافی، مروری بر وعده‌ها و اظهارنظرهای مسئولان درباره رفع فیلترینگ داشتیم و سوال اینجاست،
بالاخره چه زمانی رفع فیلتر صورت می‌گیرد؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/695899" target="_blank">📅 20:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695897">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VC_doKI7lbAue1gfUhUlRTRBxNCTqOl-lkw6NHAm92Yaj-68yUFEnnnJqgmrFYz1I-G8WIXP6XVLl6oL0G8HFBxQpkkgrm35MiV8l4zO_5MdTVFZp-TTo0HX1jyX87SHivS__b7p5M-2KXdtZcExqPa4EXUJ-oykPmtSh-dc7DogGmt0xofR5fSsA63SPps6PiXe6_29LWjSe8Ox_B-ke2KGk6JseYLGvDJtlpk2X7pfSLOI_m6glnar_iOZ0sfQfM88QQCyRPs6u4_szMz8zVNX6U_QSv0HvMqpYCIK0XQbDZZuihw_kNVtenHlgSuuSyQqrwtU_Me45DC4ysHzRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JB5EIToT8dIjIlh0Bk6k3rXZdpRBJyUpq4QFCGucpQT-LRW6MIhcrTHlUy2UXZuLJ9SZ0ex2tPSdgCQu041J2-cDR3xn-2OW-VnOQSBXS0z8Ax7bAZpXNH4uSrD2sUGgBZp7T7YD08QjDeC9K4I-MFbQFp9ACf9Cfq4AK5Af_sImXZ_DQ5k3QoDQNR90dhRGAP1M1FzS3GflfSF_B_YilvHcDcT7E0TaD9y-uiqlOZMtUYLAGj_FAhtLe3Sq82nlpvSl9Dbyc8hmZw8ZsU4O1-zV3Hw3ZFg9uv_08J_PnW9xPQzmOmXqNnW2dzkjD_buCXP6l6Z6jq2djfmPG1Mk7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع خبری از اصابت مستقیم یک فروند موشک به فرودگاه ریاض خبر دادند
🔹
در پی این حمله سنگین، دست‌کم ۱۰ هواپیمای مسافربری از فرود فرودگاه ریاض منصرف شده و مجبور به تغییر مسیر اضطراری شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/695897" target="_blank">📅 20:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695896">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
پزشکیان: آمریکایی‌ها تاکنون ۳ بار پس از گفتگو به ما حمله کرده‌اند و این نشان می‌دهد که آن‌ها به دنبال گفتگو نیستند، بلکه هدفشان ساقط کردن نظام جمهوری اسلامی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/695896" target="_blank">📅 20:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695895">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">طلا و تترم رو نگه دارم یا بفروشم؟
از موج صعودی اخیر جاموندم؛ کی طلا و تتر بخرم؟
همین الان کدوم بازارها هنوز نقطه ورود جذاب دارن؟
نرم افزار مشاور سرمایه گذاری اکوتراست
👇
برای دریافت نرم‌افزار کلیک کنید
برای دریافت نرم‌افزار کلیک کنید
برای دریافت نرم‌افزار کلیک کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/695895" target="_blank">📅 20:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695894">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okVdHwMNDQNFsb0EZ5J7WKE8wmyLvSlVnly5W3V3B1wEPt-eEvtqrmYKrfE_CByRKgUb7CGpzULxI7RosXQNSiEL-p1qNmZCJI1CHqeJuvqJo892s2l5zyev753BEzZYL7-PGUoGHEL5O4zwEWN9Kq4L_WDZKlctopOGWITQh63UomRAi1QccUSD2SDSORmb445PA0jZnqK8u8d60YbZnAZAovcAgKqrTLvtUzMgDkWFsAhZBUfHoAxzPJaezKsc9dOoOdKmeV6zLm2nkQJDpIsap0FiourEo_Ypd_tImG6XTS2k60CukBX-dwro88wDzNAOT7_Lw79-ril2lhkQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتر بعد از موج شهریور، فقط ۱۴ روز استراحت کرد و دوباره وارد موج صعودی شد
🔹
ویس زیر رو بادقت گوش کنید
👇
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/695894" target="_blank">📅 20:38 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
