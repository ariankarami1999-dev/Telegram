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
<img src="https://cdn4.telesco.pe/file/PkmP68KdnmaAU9ui13KRvbPDQoDFM0aD0XtqFXj3i64roOfD25hlbu1CcZGSqU8Mixrq2L9cdPYZvZjT4YqA0zLsUEXsvAVBt1rt4XRaoCGew3nrrbhoo_1NsznAUxFQ7DC8sbZ1JzNErlDIucui04Z_pOtDeOfCXfKW1ebt2_pDa9F8G6fWS_VHkiMQ00p2sh3TugDg5wbXmKUuSbnpHUfcSz_osA_kjWf6uofe0bvkfdlPqmGmncUAYCi1HiiJZZiENJUiWrC3WLXJ4d9NzL3pHxRXvL3-K_qwSrqt0U4QC7qoZrwR4ZZaifhJJL_D8COgNy5C_hzPkQBtDniBaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 940K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 14:19:15</div>
<hr>

<div class="tg-post" id="msg-122000">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
امتحانات دانش‌آموزان کهگیلویه و بویراحمدی غیرحضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/alonews/122000" target="_blank">📅 14:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121999">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnPnTElHgwK3m7jcRGpEuP_w3h5EpgNxE03yVcIqPHAaV5fY5xgPhUI8z8Caurli-KBzIyoLGAeuOXwMMQHAY6FFIf5LjOoxhU48CtsyTQfpdwOgn-eZkGOcECOvfNBKUZiEDdu8x0K5ZTH-WddAK7H7H9gOa45lIlrHQP2yyDorh01O0YeCWJtSuzPKFkI9U6YsUmOflmV4JEh6AUiP8Gu9YMHYvgvy8RCQy5x3TalMxrcwo_gCO4Q8WGy2QvJ4QMYfNczGmeIQtNzCo8lt7JtdIw5xh9XHC8dbAgfCYjRg3ALGcyAKrOkPECZ4lrIoIOQNXrC34V48eGCzfXtGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏روزنامه نیویورک تایمز به نقل از دو مقام نظامی اسرائیلی
:
تل‌آویو در جریان گفت‌وگوهای اخیر میان واشنگتن و تهران عمدتا از مسیرهای غیرمستقیم از روند تحولات مطلع می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/alonews/121999" target="_blank">📅 14:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121998">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
قطر: بستن تنگه هرمز تنها منجر به عمیق‌تر شدن بحران می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/alonews/121998" target="_blank">📅 14:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121997">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_G5A3dpa2IeHd0ulWPqA6Ec2xZmgeQWmugp3Mle_PyYb6ZsMBdT7yYxYK7iieyoV0cd3ofB3g_rtXbSx1cvhws5OufL6QpM8hRswRMbn4B63Aa6T1U49ZTnbkD1z6uWLW5NmbskyfcMw3WULkGNST0M8GoESQiOnizuF_8ey0MCy2YLxM0DJnLUj6E3GkJoqwQl32oZOHTOmH1lk4mxSZdzQPi3KQ0au6XOs4gn4yMoW14o9m7Ab8RsRM0XVJ5vo1qLo09RZr3VUVQ5vS91yC8qC75mjJNkU99Q24BpfcBrrGBL8wB843USx3Wfddx2MnGmGFplYnDV2UnV6HgSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع الحدث : آمریکا به تهران پیام داده اگه توافقو رد کنه، عواقب بدی در انتظارشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/alonews/121997" target="_blank">📅 14:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121996">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سازمان ملل خواستار توقف اخراج افغان‌ها از کشورهای میزبان آنها شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/alonews/121996" target="_blank">📅 14:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121995">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
دیدار مجدد عاصم منیر با عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/alonews/121995" target="_blank">📅 14:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121994">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeklJiDkD0uvc9ibc7z3egSjbArg3ETDwGBVytaDBm2BpN-Pl2HWOqM2p_jfwCv9V6G6I0DLLkptIqpeW940JZ21lf8khduYiOlJ4fUKBx_pWFW1jJcKVbE4f7Ruzwul74-Z4EzcCfSN2mYWa790kwwSkspbVhqAjbIm6ZR2i2o-_XKQbpfZ20xfp5Xhym48XKxFN7Uj-YfSaLkfTp6qzM80nZwC0HrmZNsh4kgxFKlbPrm5pHaTKPkpOVtUiZq4LSPPdx2WxUmRGAtum_mnreno457jo3HJh3HIZki7G2XhTYi6pH7u70E4buljD5tIIJ58weyChDwsUYbDdpXEzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان با پزشکیان دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/alonews/121994" target="_blank">📅 13:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121993">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان با  قالیباف، رئیس مجلس دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/alonews/121993" target="_blank">📅 13:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121992">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
منابع خبری از حمله هوایی اسرائیل به شهرک «مجدل سلم» در شهرستان «بنت جبیل» در جنوب لبنان خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/121992" target="_blank">📅 13:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121991">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: وساطت‌ها بین تهران و واشنگتن به مرحله‌ای رسیده که یکی از سران منطقه‌ای به طور مستقیم برای پر کردن شکاف‌ها وارد عمل شده.
🔴
ظهور قطر در این لحظه حساس به طور مستقیم و بر اساس اطلاعات و منابع موجود، نه صرفاً به عنوان نقش کمکی برای پاکستان، بلکه به عنوان نقش محوری است.
🔴
منبعی می‌گوید که احتمال دارد یکی از میانجی‌ها به واشنگتن سفر کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/121991" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121990">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
فروش متری خانه در تهران آغاز شد
🔴
مدیرعامل سازمان سرمایه‌گذاری شهر تهران: عرضهٔ آزمایشی خانه‌ریز در تهران آغاز شده و از این ماه کار به‌صورت گسترده از طریق سامانۀ شهرزاد شروع می‌شود.
🔴
قیمت خانه‌ریز معادل میانگین کل آن ملک است و افراد می‌توانند از چند متر تا کل واحد را خریداری کنند.
🔴
قیمت‌گذاری برای این املاک توسط کارشناس رسمی و در روز تحویل ملک انجام شده و به مزایده گذاشته می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/121990" target="_blank">📅 13:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121989">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
فروش کانفیگ استارلینک و VIP با سرعت بالا و اتصال پایدار
💎
پلن‌های VIP
📍
1 گیگ — 200 هزار تومان
📍
3 گیگ — 600 هزار تومان
⭐️
پلن‌های Starlink
🔸
5 گیگ — 1.500 میلیون تومان
🔸
10 گیگ — 2.900 میلیون تومان
✅️
آی‌پی ثابت
✅️
پشتیبانی ۲۴ ساعته
✅️
کیفیت تضمینی…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121989" target="_blank">📅 13:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121988">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRYTqffSa01I7n11ZZRvyncuLTYO3-LlK6pwFaas9pdkaot4jZBzYv_0bf5QAXGxoKYF2rKWnStdXXQQARqwhiPk6Bxre-K5_1uL6rlgbGgyouw_hm6anOiivts1t4OTZRvstWGQ-ij25tjkJyMWiAiA7dA-Vyn00MOdN61yGE-ujl2NDVylPFZiqRtgCx7U51G_tZHXFigS7g6uYnpiflZYaHGlsHBgJZ48AZ7PANBhFa14-sgpctgvAwhWfaLGbzGlcxRSMvSWg58U7LO8ZmAPwFoUrmUuHFEo4XEYIiHOClnmsDO_9ft0ByMeYRa1fVhaHtigbetxBzucO8xS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فروش کانفیگ استارلینک و VIP با سرعت بالا و اتصال پایدار
💎
پلن‌های VIP
📍
1 گیگ — 200 هزار تومان
📍
3 گیگ — 600 هزار تومان
⭐️
پلن‌های Starlink
🔸
5 گیگ — 1.500 میلیون تومان
🔸
10 گیگ — 2.900 میلیون تومان
✅️
آی‌پی ثابت
✅️
پشتیبانی ۲۴ ساعته
✅️
کیفیت تضمینی
✅️
دارای ساب باقیمانده لحظه ای
✅️
متصل در تمامی دستگاه ها و اپراتور ها
🛫
خرید و پشتیبانی:
🏠
@expressuport
🤖
ربات خرید:
💻
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/121988" target="_blank">📅 13:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121987">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ادعای العربیه: یک هیئت فنی و حقوقی پاکستانی عازم تهران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/121987" target="_blank">📅 13:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121986">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ادعای الحدث: پیام‌های آمریکا که به تهران منتقل شده، حاکی از آن است که اگر ایران با توافق موافقت کند، حل باقی مسائل به زمان بعد موکول خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/121986" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121985">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزارت بهداشت: مورد مثبتی از ویروس‌های جدید در ایران گزارش نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/121985" target="_blank">📅 13:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121984">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
خنثی‌سازی مهمات اسرائیلی ـ آمریکایی در خرم‌آباد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/121984" target="_blank">📅 13:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121983">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_tUJcjxwSyGwZzh1AON910gdylGbbj7jYqJJ6fkZkx7Kt5AwEHmARteDy6ixfatYG2cfeOuJLeJt3dVG4Vrqf-RycFVB8w5HnUVqMS6LohHs3JXGrGCXE6ooURgDIoEuAh6KXgKkBJP8Y_fcOsCIjbj-u3nDLRGBZ2E7x9UW7TMfXA7VHFevKO_mu19D_ax7y0vTciSJCRjFY4jUKnIrXnLsRbTxfmoplHJNSqCM9hegZ0dAbahzhB4IUxnY9-5xS4U5aO8R193R0-3NddSBhrosgQbb1296PRaHswdC5PbNb8ecW8X6gPOOxJhkzYbc4ZCVKvf7PIPWBii7ZQuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ترامپ با دموکرات‌ها در تروث سوشال
اگر ایران تسلیم شود و بپذیرد که نیروی دریایی‌اش رفته و در قعر دریا آرمیده است و نیروی هوایی‌اش دیگر با ما نیست و اگر تمام ارتشش از تهران خارج شود و سلاح‌هایش را زمین بگذارد و دست‌هایش را بالا بگیرد و هر کدام فریاد بزند «تسلیم می‌شویم» در حالی که پرچم سفید نماینده‌اش را تکان می‌دهد، و اگر تمام رهبران باقی‌مانده‌اش تمام «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه بپذیرند،
نیویورک تایمزِ شکست‌خورده، چاینا استریت ژورنال (کنایه از وال استریت ژورنال)، سی‌ان‌انِ فاسد و تمام اعضای دیگر رسانه‌های خبریِ جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است.
دموکرات‌ها و رسانه‌هایشان کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121983" target="_blank">📅 13:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121982">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
الحدث به نقل از منبع ایرانی: آنچه تهران می‌خواهد، توافق بر سر چارچوب است که مشخص کند جنگ چگونه پایان خواهد یافت.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/121982" target="_blank">📅 13:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121981">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
الحدث به نقل از منبع ایرانی: آنچه تهران می‌خواهد، توافق بر سر چارچوب است که مشخص کند جنگ چگونه پایان خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/121981" target="_blank">📅 13:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121980">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df35f5dfa.mp4?token=N5GoB83MpXb7tAGWIKIVyG2pNvR6Hg7mwUASH3VKmFG-pazz8GSYxEUFWRZnzjbVyU7wTVZZdkvyo9MPRdy4_--yXXowPdXNJ81-al26PnPMJs6JZeBoAvvi4xqX5MzGgpHz4iHu2h2a9KTY-CrU13cwNa6GXJBKidUCjKSXuxptviuqB3cTfi-522vKv8G0Ukf-AZrXak7BxjBuZZdYIe9RCmV6rpQI3hQNylH4kkQevRoVNU9ZxCYJkk_iS3yFyQZaFmIYiQOZixWYpANtaiPoSC0PWg2OmaEOq0X69qn1Hk9vULaPB5mJw9Or9xXS7Ib9AbaQzfDDqvHzhqpqbIIP7B6NjGml8oLX_i5WX-3VrGtjpA6MA8-pkHGFNpIhnjLJmtkcwYPEqu6TCLIw6AeGBfHaYVSZLG5eHS4peDFC0giQJTOGnDgZ-lW6GWESSr2lTIKvnfPPouwGccNaG8VB2grHrtaiYyz7xzvte5mANRhrRloPjyiHa8tnr0gjh6-DpWPxT_ny_FPMA57IcCOc2vVXMIf83FU5QZGd3_0ufo7aGVqAq-V_AFq6zaYN9sNigtHscMPqkpcIet--A5chgqDPLTnETtCe-HPevLSbALcAw4h4sj83xN0hq3NRzK2HiXMxHXm21ExPX6RR-KfsyVW5Y_Wsj0tNnZ6Rrs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df35f5dfa.mp4?token=N5GoB83MpXb7tAGWIKIVyG2pNvR6Hg7mwUASH3VKmFG-pazz8GSYxEUFWRZnzjbVyU7wTVZZdkvyo9MPRdy4_--yXXowPdXNJ81-al26PnPMJs6JZeBoAvvi4xqX5MzGgpHz4iHu2h2a9KTY-CrU13cwNa6GXJBKidUCjKSXuxptviuqB3cTfi-522vKv8G0Ukf-AZrXak7BxjBuZZdYIe9RCmV6rpQI3hQNylH4kkQevRoVNU9ZxCYJkk_iS3yFyQZaFmIYiQOZixWYpANtaiPoSC0PWg2OmaEOq0X69qn1Hk9vULaPB5mJw9Or9xXS7Ib9AbaQzfDDqvHzhqpqbIIP7B6NjGml8oLX_i5WX-3VrGtjpA6MA8-pkHGFNpIhnjLJmtkcwYPEqu6TCLIw6AeGBfHaYVSZLG5eHS4peDFC0giQJTOGnDgZ-lW6GWESSr2lTIKvnfPPouwGccNaG8VB2grHrtaiYyz7xzvte5mANRhrRloPjyiHa8tnr0gjh6-DpWPxT_ny_FPMA57IcCOc2vVXMIf83FU5QZGd3_0ufo7aGVqAq-V_AFq6zaYN9sNigtHscMPqkpcIet--A5chgqDPLTnETtCe-HPevLSbALcAw4h4sj83xN0hq3NRzK2HiXMxHXm21ExPX6RR-KfsyVW5Y_Wsj0tNnZ6Rrs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رضا تقی‌پور، نماینده مجلس:
شبکه حیاتی کابل‌های فیبر نوری جهان از تنگه هرمز و باب‌المندب عبور می‌کند و ایران می‌تواند این کابل‌ها را قطع کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/121980" target="_blank">📅 12:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121979">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
شهباز شریف نخست وزیر پاکستان امروز شنبه وارد شهر هانگ‌جو واقع در شرق چین شد و دیدار رسمی چهار روزه خود از چین را آغاز کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/121979" target="_blank">📅 12:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121978">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9l53y5PPVRF7RJn5EsEUYNSim5xBV6sR2PdqrIGB09_aoaoGKeL2Sb31IE-G5nZGJA4oAPi5VY9_aXwKIBi6e-p_KMk9pEa2gp-cGapyQrwaobgXv9PwU5ED_REYylSwq55N3EXwNmDjUOO4Tp9chH9Y2D-5kNNPpTRqSHUDHDDeqzMIiCnOEooda0XDwWWuBR3zStwRKqx4dKNJzG3EqVUzOJKixkv0k0eDHRW65lo-Wb3y7UXQt9c1GMnVphNXFf6uOmgNSqXEqgwmbrMVsDFJYfPDoKOSDDizvtqjk2ctFKsMT_RQtpKt_jkVkNJh_7uzRB-2bwzCjedKesBMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۳.۵۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/121978" target="_blank">📅 12:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121977">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نیروی دریایی سپاه اعلام کرد در شبانه‌روز گذشته ۲۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/121977" target="_blank">📅 12:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121976">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
تایوان : چین بیش از ۱۰۰ کشتی جنگی رو تو آب‌های سرزمینی مستقر کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/121976" target="_blank">📅 12:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121975">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dde66f77e.mp4?token=BjDziGdd54aNsB1etnn-38S0MBzzr_4tl72LUpNR0PMLMsSHyPiN6kfuoU9XmIMPFYpFdeS88r_pqGFOZCU28YFQBHKK2OYbfrMOFFZcwQXHv-vSHcb9Nm2v_Uq3_V96Oqpr4hUbWmPSXuEsQLbJtQxEoaadc4ThjeR1BHEhuV_wUjCqeqOMiTG9yOrkZ3IpsQsP6Bo1c2Im3Op1W5cX40_ZNWO0BKzizSUofPXss8g_F-lgUdQrz3QklAzklKfh0wsJNeF0eZ4LYiYEj8vSwC8py4sykFE57WfMEsndpVtlJLUlNWFgJCmlo5k7fCwh3TtdL3LcvaZ1Wn3wIsuZiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dde66f77e.mp4?token=BjDziGdd54aNsB1etnn-38S0MBzzr_4tl72LUpNR0PMLMsSHyPiN6kfuoU9XmIMPFYpFdeS88r_pqGFOZCU28YFQBHKK2OYbfrMOFFZcwQXHv-vSHcb9Nm2v_Uq3_V96Oqpr4hUbWmPSXuEsQLbJtQxEoaadc4ThjeR1BHEhuV_wUjCqeqOMiTG9yOrkZ3IpsQsP6Bo1c2Im3Op1W5cX40_ZNWO0BKzizSUofPXss8g_F-lgUdQrz3QklAzklKfh0wsJNeF0eZ4LYiYEj8vSwC8py4sykFE57WfMEsndpVtlJLUlNWFgJCmlo5k7fCwh3TtdL3LcvaZ1Wn3wIsuZiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش
تند وزیر ارتباطات به مخالفین اتصال مجدد اینترنت: این نگاه قیم معابانه به مردم چیست؟ کی گفته اینترنت را باید خلاصه در دو پیام‌رسان بدانیم؟
🔴
ستار هاشمی وزیر ارتباطات: صحبت هایی که در رابطه با نقد دسترسی مردم به اینترنت آزاد می شود، نگاه قوه عاقله کشور نیست.
🔴
ان‌شالله اینترنت برای آحاد مردم و به صورت عادلانه برقرار می شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/121975" target="_blank">📅 12:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121973">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjpJGxu5W2HDQOiDx9O5qrhQRRtlGmM-18fEZZN6mwekMlDG3ZLurJn87DvW_dpAFWBAuEpn-M61oNfvy4nhqFOTKlzjmqCShkyxOis9mDIT7sXV_e_yt0tsJwnjUkG0kl_Oi5VrSdfjX7n9qlEWtD7JLmqDC_71uGOpL_QcbULv_Wpel7T6nYav_PI9Faf9O2-_IIPyUFg0NEer4mHMVJ5BshnGQZTpKf-etNckCo-1ANxVYZDV693f1r8rEZFG5jklysSKj_dAbI_g1_Y6XlRhUbXjSnhPtLu050135c0gUFloIVtQZut7PWtdxY37BHw29frcALiGh-PeMlrrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efeb4d8934.mp4?token=Jf8Je0e8IZHlubAi1vkkD4QXUK3I8m9wY5AK57GHgRPF22QPhb5sterwS5ylyrXLxO1MaApuyFCTFqSuKXw4POOXy_21OXxAWgjdT2z7TKuA7aaCNf2S_x5Mj69lVhbThpcvkdHomlGENJynyHv2Y85iDzyaXPcgU2lHZC7Du2A6YPkfHVvzDUhiWHV_Zbj1s4i3imovWH9vbzK38-rrVUEFUNXgp6DHDtXbpKeOlVtmQHwGaJoxY5T2d8ftnZNttmYu4gbh_6dmPVhm0dRvMf3UuQsSNbVI8WbmUoroayAoB1MppoiKLfwKJoCZ1I8LNE5uxYGxPF61Q4zCKV_Ehw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efeb4d8934.mp4?token=Jf8Je0e8IZHlubAi1vkkD4QXUK3I8m9wY5AK57GHgRPF22QPhb5sterwS5ylyrXLxO1MaApuyFCTFqSuKXw4POOXy_21OXxAWgjdT2z7TKuA7aaCNf2S_x5Mj69lVhbThpcvkdHomlGENJynyHv2Y85iDzyaXPcgU2lHZC7Du2A6YPkfHVvzDUhiWHV_Zbj1s4i3imovWH9vbzK38-rrVUEFUNXgp6DHDtXbpKeOlVtmQHwGaJoxY5T2d8ftnZNttmYu4gbh_6dmPVhm0dRvMf3UuQsSNbVI8WbmUoroayAoB1MppoiKLfwKJoCZ1I8LNE5uxYGxPF61Q4zCKV_Ehw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز جنوب لبنانِ تحت حمله‌ شدید اسرائیل بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/121973" target="_blank">📅 12:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121972">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
بلومبرگ: هند برای سومین بار در هشت روز، قیمت گازوئیل و بنزین را افزایش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/121972" target="_blank">📅 12:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121971">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
بلومبرگ: وقتی کانال سوئز در سال ۱۹۶۷، پس از آغاز جنگ میان مصر و اسرائیل، بسته شد، ۱۵ کشتی در داخل این آبراه گرفتار شدند. آن‌ها لنگر انداختند تا منتظر پایان درگیری‌ها بمانند. جنگ خیلی زود تمام شد. نام آن، به‌درستی، «جنگ شش‌روزه» بود؛ اما کانال به مدت هشت سال بسته ماند. زمانی که سرانجام در سال ۱۹۷۵ اجازه خروج به کشتی‌ها داده شد، فقط دو فروند هنوز قابلیت دریانوردی داشتند. بقیه آن‌قدر زنگ زده بودند که به «ناوگان زرد» معروف شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/121971" target="_blank">📅 12:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121970">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
هزینه دریافت گواهینامه رانندگی با ۵۶ درصد افزایش به ۱۵ میلیون تومان رسید
...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/121970" target="_blank">📅 12:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121969">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f5a8b8d1.mp4?token=FoyuOdUe6Bnsc2rBD6E_dt4PoX00URZTw8w0xtBAXmrzXALPrdkPMQ7dDMRrcaUTe3tq6_znG_nCSdbkxkhcD6lhxAJow-Rzx1KR0n0h3QJwPpMvWz0z7AssFYqaqTCF88rVc0-oVDumpjAIxDDSMBlhgWqqms-UJBEZA90jZnXhW_ZteChBi0QWbcq1-E34rRoD7FakAOxBGlF13uo-VtSPpq3STHs4h60sFBLgLHk93-yHwMOIB8XXO0vyudPwbNABdZfhliBoJBK3y-IJ9Nqzf3XVimBBh6HNDPvOPqth-IYRN8ZwcPC1sAJbb0JGsOB0vtbgzYgst8Wo9T-rlbBIjdB-voJVtr62oXBqHQWkJyX_UapqdDQElDBZKvcQqYMbKA4BBk6HWD3-KINImbhSHBCm3LPoOFTpVi3hnqBo4Irj0bUyX_6EI2p2hPKmTz6ZPj4RxFFtXyG3-_VxiVbaCJ1t37IlNYdlmkmHtMhTRfZDXw3JfKzcQZltBMCYIfZ_6KQH2W-g0IAdkCw0xcAblJ4xHYlOXB-VVxga__K0MIYVi-XmmFRYdxGcjr_6Z1rcx6asGbKJtQjXIgIAcxraVy6x4FhC74o_ZL9eR-PODIluQ6ag5l0fbleR6bs2rJd_ppbeLKKmh9rQZf5MMdt9NANjiXI2k4x05qLrIzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f5a8b8d1.mp4?token=FoyuOdUe6Bnsc2rBD6E_dt4PoX00URZTw8w0xtBAXmrzXALPrdkPMQ7dDMRrcaUTe3tq6_znG_nCSdbkxkhcD6lhxAJow-Rzx1KR0n0h3QJwPpMvWz0z7AssFYqaqTCF88rVc0-oVDumpjAIxDDSMBlhgWqqms-UJBEZA90jZnXhW_ZteChBi0QWbcq1-E34rRoD7FakAOxBGlF13uo-VtSPpq3STHs4h60sFBLgLHk93-yHwMOIB8XXO0vyudPwbNABdZfhliBoJBK3y-IJ9Nqzf3XVimBBh6HNDPvOPqth-IYRN8ZwcPC1sAJbb0JGsOB0vtbgzYgst8Wo9T-rlbBIjdB-voJVtr62oXBqHQWkJyX_UapqdDQElDBZKvcQqYMbKA4BBk6HWD3-KINImbhSHBCm3LPoOFTpVi3hnqBo4Irj0bUyX_6EI2p2hPKmTz6ZPj4RxFFtXyG3-_VxiVbaCJ1t37IlNYdlmkmHtMhTRfZDXw3JfKzcQZltBMCYIfZ_6KQH2W-g0IAdkCw0xcAblJ4xHYlOXB-VVxga__K0MIYVi-XmmFRYdxGcjr_6Z1rcx6asGbKJtQjXIgIAcxraVy6x4FhC74o_ZL9eR-PODIluQ6ag5l0fbleR6bs2rJd_ppbeLKKmh9rQZf5MMdt9NANjiXI2k4x05qLrIzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله ویدیو منتشر کرده که توش یه نفربر زرهی نامر اسرائیل رو تو جنوب لبنان با پهپاد FPV زده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/121969" target="_blank">📅 12:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121968">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر خارجه قطر در تماس با عراقچی:
ما از تلاش‌ها برای رسیدن به توافقی جامع که بحران را پایان دهد حمایت می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/121968" target="_blank">📅 12:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121967">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVUd3xEIuqDe_n8JVeF3x-bhghjJo3LIRvO1aDbyyvHu_OqwNbpXHbfq2chGY_ZadJ7-Dknj3R0fc8NZd0wHOBpsPA5d3aIXW-zMKMOkP0UigdmuuVApzuDWHoSUbx6t3QgkyfH75DOHMwcn1zdNuG_0pcCZLgHhwOF6iCsKOIVVc5G9XqfHQayh9IA0UKBb1M8paWXNRwQ4-7YQ-FYkRyS8n3JyFTcCZddGV2WoLiIWW7H7-iBQoi1662RojRsUm0vh7WuDAJkcz6zHSuFc-IMRmlw1giViOU1xO39L38i-v6bubhmhuQYF-_srfxASxmnE2Ug7rnJ3die1xB9t0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
منابع به اسکای نیوز عربی گفتند که میانجی پاکستانی موفق شد بر مانع پرونده هسته‌ای ایران غلبه کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/121967" target="_blank">📅 12:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121966">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی سازمان هواپیمایی: سازمان هواپیمایی نوتام جدیدی صادر نکرده است.
🔴
نوتامی که اخیرا در فضای مجازی منتشر شده، تکذیب می‌شود.
🔴
شرایط آسمان کشور همچنان مانند روال گذشته است و پروازها طبق برنامه انجام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/121966" target="_blank">📅 12:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121965">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ اسرائیل را آن‌چنان از روند‌ها کنار گذاشته که رهبران این کشور تقریباً به‌طور کامل از مذاکرات آتش‌بس میان ایالات متحده و ایران بی‌اطلاع ماندند
🔴
اسرائیلی‌ها که از دریافت اطلاعات از نزدیک‌ترین متحد خود محروم شده‌اند، مجبور شدند اطلاعات رفت‌وآمدهای دیپلماتیک میان واشنگتن و تهران را از طریق ارتباطاتشان با رهبران و دیپلمات‌های منطقه به دست آورند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/121965" target="_blank">📅 12:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121964">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f2d8f3736.mp4?token=kdWx6ilIgi6T7zBL3i9jeHGTFTyOF9kPamdEAzIBuNRReMSzkqcPuFCIZNwiQGbl4LYTX9KFLk036sMqeIpkg5CVVOsCvmwcrAVtoVLd4lFuxu54H24MqFtEMDn8Lx0odywcsy9p5cEBgDDtUNnm_M9ML5gNRcex78o8CngtpGBV2OQM-8ZLhQ78YIvsSocBEQ4h_eRIlU6Xsx2WhRUhCbze1vOq_m6RhnmHNJMnq0_j95iYViNX3RsewzwTtS-vAAitj4waCc2vR8bJG-22lHvv9q9nTFFJo0D6fIVBS3xHAUFGDZHYzlSULAPoq3_r3eJB4_Vo0KlGbBTYNyEZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f2d8f3736.mp4?token=kdWx6ilIgi6T7zBL3i9jeHGTFTyOF9kPamdEAzIBuNRReMSzkqcPuFCIZNwiQGbl4LYTX9KFLk036sMqeIpkg5CVVOsCvmwcrAVtoVLd4lFuxu54H24MqFtEMDn8Lx0odywcsy9p5cEBgDDtUNnm_M9ML5gNRcex78o8CngtpGBV2OQM-8ZLhQ78YIvsSocBEQ4h_eRIlU6Xsx2WhRUhCbze1vOq_m6RhnmHNJMnq0_j95iYViNX3RsewzwTtS-vAAitj4waCc2vR8bJG-22lHvv9q9nTFFJo0D6fIVBS3xHAUFGDZHYzlSULAPoq3_r3eJB4_Vo0KlGbBTYNyEZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیراندازی عروس جان فدا با کلاشینکف در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/121964" target="_blank">📅 12:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121963">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49046a9f4e.mp4?token=Rtf6LysbJvUmntmc528xNzWptY1Daxzqb7SnUledcx7KaIyO9IVG2SAmyXhdU0svP_ad-LsBcluaruuDqIXNjJKehdFvxkbn4bDiaUDGWo17VR12xjuV-EQdZgn117UDlO77N-NXQVJ_5a-DBeLpyMgL7HAPcpSGf9j_NQAxgK4_pqjtRrcZs6A06Y_gZeNMkVutz8NDUScFSNJxgVh8lsYSabBKadzTPLtaKGDUcnoyW7ZsvXI2gWnPboNBOE1AxwCHSrAacvIiOOYWWEXtJu_7rP9iY8T9ZandfP6CcGM9u1KamwKPOVDOXrfZnC9eUNwHa_s-hHhVMD8hOfPIuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49046a9f4e.mp4?token=Rtf6LysbJvUmntmc528xNzWptY1Daxzqb7SnUledcx7KaIyO9IVG2SAmyXhdU0svP_ad-LsBcluaruuDqIXNjJKehdFvxkbn4bDiaUDGWo17VR12xjuV-EQdZgn117UDlO77N-NXQVJ_5a-DBeLpyMgL7HAPcpSGf9j_NQAxgK4_pqjtRrcZs6A06Y_gZeNMkVutz8NDUScFSNJxgVh8lsYSabBKadzTPLtaKGDUcnoyW7ZsvXI2gWnPboNBOE1AxwCHSrAacvIiOOYWWEXtJu_7rP9iY8T9ZandfP6CcGM9u1KamwKPOVDOXrfZnC9eUNwHa_s-hHhVMD8hOfPIuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ توی توییتر که با هوش مصنوعی یه مجری که مخالفش هستو میندازه توی سطل آشغال :))
🔴
تو ۸ ساعت بیش از ۵۰ میلیون ویو خورده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/121963" target="_blank">📅 12:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121962">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نیویورک تایمز: تنزل جایگاه نتانیاهو، از حضور در کابین خلبان، به نشستن به عنوان مسافر، می‌تواند پیامدهای مهمی برای اسرائیل و به‌ویژه برای نخست‌وزیر آن داشته باشد؛ کسی که امسال با نبردی دشوار برای انتخاب مجدد روبه‌رو است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/121962" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121961">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9eqnPbhlZPiTQiodE0jie0SfKbNIo_SHsWG3ejh2FwNfOi4NQ_bu2oPcyCb6uRBPL7C_KwM4qFRNQCHlqn1yz6Xu351jiMUpWbi_8nCBoeIK75j0SPcwp0uArFDc1p4dNrLCq9pfZxt6e5k3sstVzXOY49hxasZcHJHju5d_nD71yO5ckGOwVzNrvoh_mmVl1CqPxXP98eguOng714eLJ--FNTXYrWRDCEopN_RR-cU4wfb3eTj3YkAlMal3k6jMQyUiSEzxpLenuMw2qCEGN6UFmuVZ2XivFVfPhNd5b3w_EyRc2Xj-Mkif4VLzOoY-_nppa1vTQRgPTvheO_6gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: سه ماه پس از جنگی که قرار بود در شش هفته با پیروزی قاطع به پایان برسد، ترامپ در باتلاق ایران گیر کرده است و قادر به یافتن راه خروجی برای حفظ آبرو یا گسترش حملات نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121961" target="_blank">📅 11:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121960">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رسانه‌های دولتی چین خبر دادند که در نتیجه انفجار در معدن زغال سنگ شهرستان «چینیوان»، حداقل ۸۲ نفر جان باختند.
🔴
به گفته مقامات چین، با توجه به شدت بالای انفجار در این معدن زغال سنگ، احتمال افزایش تلفات وجود دارد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/121960" target="_blank">📅 11:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121959">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654f03f44d.mp4?token=q4xs6wkFNCLCUjNaqY5Zo73mAv9FGUkij90ID4Ap25bxbygx8Vs62t2O1Gycm9-mekDXDu0Lsfl_76EWb4HHfB1YD2aBciQgu8hwTLIMhZQT9t-nJP2BsVd80BGI2frfh-kB8vV3WdBFB9MRTGV1TOgiwJuXRzf9LlIBDqv4Y9S1LlV0zDXyD4DaW0chkiQQdRAiJffqCbTtP182h8DgqfhEl0FRMBQByj1ltz4Y39d4spl7IG42gcIfoDtLi7ScZTrM6PiwP2nYmGJAyVVuFi_UJn-p5V9pcUZUkQ1ZG5BGHjS7R-RZ9HrasOspG-UHqgMaM6MnPsFbXzAGa6AzDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654f03f44d.mp4?token=q4xs6wkFNCLCUjNaqY5Zo73mAv9FGUkij90ID4Ap25bxbygx8Vs62t2O1Gycm9-mekDXDu0Lsfl_76EWb4HHfB1YD2aBciQgu8hwTLIMhZQT9t-nJP2BsVd80BGI2frfh-kB8vV3WdBFB9MRTGV1TOgiwJuXRzf9LlIBDqv4Y9S1LlV0zDXyD4DaW0chkiQQdRAiJffqCbTtP182h8DgqfhEl0FRMBQByj1ltz4Y39d4spl7IG42gcIfoDtLi7ScZTrM6PiwP2nYmGJAyVVuFi_UJn-p5V9pcUZUkQ1ZG5BGHjS7R-RZ9HrasOspG-UHqgMaM6MnPsFbXzAGa6AzDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌های دولتی چین خبر دادند که در نتیجه انفجار در معدن زغال سنگ شهرستان «چینیوان»، حداقل ۸۲ نفر جان باختند.
🔴
به گفته مقامات چین، با توجه به شدت بالای انفجار در این معدن زغال سنگ، احتمال افزایش تلفات وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/121959" target="_blank">📅 11:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d430a4d80.mp4?token=jZZlaQGZqPfvht-9939nYgKcV1QyMaZlgaB16edkwgTkR6P0iMAH1pTr0C4DnTBr2fy0jLjCIqlEidNusxFtOz5vu_2XUT-ewhpSfO2aXiMrwYBKikYx9mPUyh1_vOEhh0I-pua1jj6TO_-vgoxXN7X98sfJ7dXKWWUbWpgubeR8jV9dzK5913TqbJ35jCrNyAAAl0G-XJmXSssygzEWp68oToSWcUsdwBCQJhvuK8sc43JfABNeXpgtdM1JgimqYKrRwFnPydypUg3FcttRsA-CzKR-gsXY2rRFR27KS5LS6m6SWtdOy-SZkUQNX0vetf8D5pSZCoFdhUo-3q0hXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d430a4d80.mp4?token=jZZlaQGZqPfvht-9939nYgKcV1QyMaZlgaB16edkwgTkR6P0iMAH1pTr0C4DnTBr2fy0jLjCIqlEidNusxFtOz5vu_2XUT-ewhpSfO2aXiMrwYBKikYx9mPUyh1_vOEhh0I-pua1jj6TO_-vgoxXN7X98sfJ7dXKWWUbWpgubeR8jV9dzK5913TqbJ35jCrNyAAAl0G-XJmXSssygzEWp68oToSWcUsdwBCQJhvuK8sc43JfABNeXpgtdM1JgimqYKrRwFnPydypUg3FcttRsA-CzKR-gsXY2rRFR27KS5LS6m6SWtdOy-SZkUQNX0vetf8D5pSZCoFdhUo-3q0hXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سیلوستر استوانه در تجمعات شبانه رونمایی شد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/121958" target="_blank">📅 11:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121957">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">برخی شایعات حاکی از آن است که سفارت آمریکا درخواست ویزای شجاع خلیل‌زاده، مهدی طارمی و احسان حاج‌صفی را رد کرده است  @AloSport</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/alonews/121957" target="_blank">📅 11:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121956">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ادعای کانال ۱۳ عبری به نقل از نیویورک‌تایمز: ترامپ اسرائیل را از مذاکرات با ایران کنار گذاشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/121956" target="_blank">📅 11:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121955">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hy8MqmoHaA5K3sU5Ci9yPFYncgR37ch497gBiR8S2EjwYaV4uqwuWXLC4KfZ8ro1lcMBruk6CPZxwhgkulU_hXm8b0AGs7RJsNe_4HVRyLaMsWXTZ7RnLBxwu0mqnAnkqf-h_BeZiinuQI5hiT0Ta4hIJqDpdhWXFqvZKC17tRFeSQOUjXdCq5I1vII4eHmDkoZjZL7mJpkl--dN4Hd94CLiHFIOPnZpjvJqVccIES1T-XSK2RPX7LmjMEVY4WzlVDbzFyInCFtxkVxZMisellpHCbp753DjJW9yZojoF4z2iFBzIfcdOlGd0du5wn18N5QChhpBAx9z8uo5hyMkeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه ماه پس از جنگی که قرار بود در شش هفته با پیروزی قاطع به پایان برسد، ترامپ در باتلاق ایران گیر کرده است و به گفته رویترز، قادر به یافتن راه خروجی حفظ آبرو یا گسترش حملات نیست.
🔴
با وجود حملات نظامی آمریکا، ایران فرو نپاشیده است؛ کنترل مداوم آن بر تنگه هرمز — که یک پنجم نفت جهان از آن عبور می‌کند — همچنان اهرم اصلی آن است.
🔴
تحلیلگران می‌گویند رئیس‌جمهوری که به پیروزی‌های خود می‌بالد اکنون با چالشی روبرو است که می‌تواند جایگاه جهانی آمریکا را بیشتر از هر درگیری در دهه‌های اخیر تضعیف کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/121955" target="_blank">📅 11:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121954">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
مگه سال ۸۸ پهلوی فراخوان داده بود؟
🔴
مگه آبان ۹۸ با فراخوان پهلوی بود؟
🔴
مگه ۱۴۰۱ را پهلوی شروع کرد؟
🔴
هر بار مردم به خیابان آمدند، جمهوری اسلامی کشت، سرکوب کرد، زندان کرد و اعدام کرد. حالا یک نفر اولین فراخوان جدی عمرش را داده و حکومت از ترس سقوط مردم را قتل عام کرده؛ بعد عده ای که بی شک از طرفدارن حکومت هستند می‌خواهند بار خون مردم را از دوش قاتل بردارند و گردن پهلوی بیندازند!
🔴
این دقیقاً همان چیزی است که جمهوری اسلامی می‌خواهد: قاتل فراموش شود، اپوزیسیون متهم شود.
🔴
آبان ۹۸، جنبش سبز، زن‌زندگی‌آزادی، کوی دانشگاه، اعدام‌های هر روزه؛ همه این‌ها هم تقصیر پهلوی بود؟
🤔
قاتل جمهوری اسلامی است. مسئول خون مردم جمهوری اسلامی است. این حکومت چهل‌وچند سال است با گلوله و اعدام زنده مانده.
⭕️
هدف و اتحاد مردم برای عبور از این قاتلان کاملا مشخص است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/121954" target="_blank">📅 11:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121953">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMB13YfXs5yfxQYZ4eKhKJOXTPuyhxeWyg_GeGi9ZsW7DPEi1WCvG-KszjXMIOyr-qD0I92GbZm_9yPax1iXRfceVpfZjtBPmHQ2Dw35r7a6jL4SasVYm8rqkE9TuvEXOCUbrkh_Wx6pOjKUCfW71Lh2iqA0PdaZV-HlQcwghyUQXC5hGxYaNtBk15T2QjzV9Cdv1uy3mXI58i_pcYp1DKrnkqTmpYgnApanf2otTxJH3Ewu1D-bxF4OmZCwMokeFo9fg30LNL25Yq2BWP5yPQct2TZPgDV0ZPoD2xcK5KgADASlG0v7z65sl27mlGiMpsH-r8FanS8f6ChP3PdYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از یک هفته هوای خنک، از امروز روند افزایش دما آغاز می‌شود و در پایان هفته ها، شرایطی کاملاً تابستانی حاکم خواهد شد. به‌عنوان نمونه، پیش‌بینی می‌شود دمای هوای تهران در روز جمعه هفته آینده حدود ۱۲ درجه سانتی‌گراد بالاتر از میانگین نرمال این بازه زمانی باشد
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/121953" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121952">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سازمان عملیات دریایی انگلیس (UKMTO) از دومین حادثه امنیتی امروز در ۲۰۰ مایلی غرب جزیره سقطری یمن خبر داده است. طبق گزارش دریافتی، ناخدای یک کشتی باری اعلام کرده که یک قایق کوچک حامل ۵ سرنشین به آن نزدیک شده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/121952" target="_blank">📅 11:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121950">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2vFDQDEZEdOwrQL85fDJc0cJfA4SFsL006p_tDZ0OEmUH-_LWjVI_axG6a5i6Ct6lD2UFL7V-SAfFXr_Ixso9c2zGX93H5gbZLiUQZAe84826RGyilWEsOmdwrz3J28j_hDdgNKf6iki6t-vH6EjJ_QXlQsiidwdNM6quWMJX30Iep3Zat-Pj8cBBkL_UdSaSMBtAvD7743J406KsUBk8bm-QkH3apB2qWV9cuIczT3HLeaGJEVDFC1zD6McDJiZA4YeNCBcXxHi818vwEMx-8ngunBLg58fqSt1gMGhr815eX7qKNkeRQ2j-3xi4GFZ3W_QFJlPfS8Fy6wdbMWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/admjFmsviJ90YJrSlyYR4_iNldxm9FiCXBxWb2hjJiL5oEK78i5WnMU2NtRokYZOJqzCmz92Bd23iSKOYcrrCHrZqMCczsXNjO5ZOwjx8FLFvtT7h6V7qfHL4t9e4xU4M-abA3O6DclkKTM_oHL3xtb7I_aN5zZVPs5_MNh_dPKShUFcJ1v58ZzW8FengdZBh4yRrVxCA9VBlU1vvhctmI8sGktrPJ_LGyJ4xxVfmka13GXQAFfnG_NW6xHqQyX1fOl7a9lgDW03zu1lursv8_2kAlF3WRiRb5NcdiYNlorHMha4g3gUdpxlGin8HB3Yz6GToZarO-O81HkX9JPCLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
فوری /  پهپادهای شناسایی قطر و امارات در حال انجام پروازهای مداوم (اطلاعات، نظارت و شناسایی) در سراسر خلیج فارس هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/121950" target="_blank">📅 11:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121949">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
آسوشیتدپرس: کنفرانس بازنگری پیمان منع گسترش سلاح‌های هسته‌ای شکست خورد
🔴
کنفرانس سازمان ملل متحد برای بررسی پیمان منع گسترش سلاح‌های هسته‌ای بدون دستیابی به توافقی پایان یافت.
🔴
هیئت نمایندگی ایران در سازمان ملل: اقدامات کارشکنانه واشنگتن و متحدانش دلیل شکست کنفرانس بود.
🔴
خبرگزاری آسوشیتدپرس به نقل از رئیس کنفرانس: دلیل اصلی شکست، بندی در پیش‌نویس بود که بیان می‌کرد ایران نمی‌تواند به سلاح هسته‌ای دست یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/121949" target="_blank">📅 11:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121948">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3ZPP-DpK0QUO1Jvgbk_8C1EpzkQIfFOydYMH32BpFHCg_8TO7aZd-qrsFdawOU5NxT8cwkzxkBfWjoygo3Z7tDdhJTHovCZAaFe1mcHLxmB0fjLmZYzpp5pfhLyjIQEIc_urZAVsVksNfBoEzi-RGCsoXVAnJJhgbasWrkq2csoYxe0MnuSCtyTrHkIfEtsZnoKu-TItCP08qIwpXQHdsbM6lw_vGHBXyHqGZmV22bGYw2ME6msnfX1OimpDoi3A0JDynpQqxh9EfWy_oXaS7tI1D46goMDhPxAuCD8ddyJcuNIq7W2FjBphXXdy-csnjysYhXE7yf7acV00AS3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل: دولت‌های خلیج فارس موظف به جبران کامل خسارات علیه ایران هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/121948" target="_blank">📅 11:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121947">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت خارجه اردن: وزیر خارجه اردن در تماس تلفنی با وزیر خارجه قطر درباره تحولات اوضاع و میانجیگری پاکستان گفتگو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/121947" target="_blank">📅 11:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121946">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ورود هر خبرنگاری امشب به کاخ سفید لغو شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/121946" target="_blank">📅 11:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121945">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTdz0aC529Ib1Ub1YwlOAyQ1633U7d4Hzh5FIEKZg2vFTJdxsi3quxYV_diNsN3aWmmis3g7am5QIhk9JAeCO8L5fQiu5rUDXImofoT8khLqO9iZ_EZKgdLRIgIwBiijgEszH-ledWeycGiBbTU0ZwKAByO_J_1yTKQDQTw95KB9pgx1tTVlALxYjAaoOmeyKLSkPmw7y2JJQSrLxtjR3tdt47Rhk5K3xXEEWTjJz_z3Pnfk1RTsN7y0L-1qXyW5sBOKC1PEX_FP75nTuDb6fand_DlfGhS1ju9g6ECrHpvDDevoS3QloZ45f8XthHCfgpDs1COHzDYeZFWQmQLR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های کره جنوبی از سقوط یک فروند هواپیمای سبک در منطقه مسکونی «هاینم» خبر دادند
🔴
تاکنون جزئیات بیشتری از علت سقوط هواپیما یا آسیب احتمالی به مناطق مسکونی منتشر نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121945" target="_blank">📅 11:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121944">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
مقام آمریکایی به رویترز: ترامپ به‌زودی درباره فروش تسلیحات به تایوان تصمیم خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/121944" target="_blank">📅 11:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121943">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGzXL4jdXEITkWvt9JxjGLCNNhpByyKLtjG8ID_SVXrMaDWVXAuc-vrt2gTwRe1BEVyDzjPrrD1fOpj1T8qSzfFnNmJlOPlkvfB6EmlnpivUH-DtsCuNrWq0HFd29knz9BGJsVF2i5zppGwwLUJXH_vFLLQnuTNnmvtAB4seFBtPqBwRpD-r2KDdedf_1FbOwwox8Z6_WGCwGkTqBzt3Em4Zp7V4pspMpE7wlOnMVims1ltGQG1BW2suaV10e3g5IV5W7hYztTpzVuyv3BODPKbvny1lxbKTQU3SozRo7FFfcu767WZpHl6rSybcPg9XX__eePLY5yKtlVeDf4eYhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهاجری خطاب به رسایی نماینده مجلس: تصمیم‌ جنگ یا صلح ربطی به نمایندگان کم سواد ندارد!
🔴
محمد مهاجری: تصمیم گیری درباره جنگ و صلح و نیاز سیاست های کلی کشور در حوزه دیپلماسی و مذاکره، از اختیارات رهبری است و هیچ ربطی به مجلس و بخصوص نمایندگان کم سواد و تندرو آن ندارد.
🔴
به همین دلیل، اظهارنظرهای شتابزده و متوهمانه آنها در این زمینه به اندازه یک پول سیاه هم نمی‌ارزد.
🔴
رسایی پیشتر گفته بود: مذاکره زمانی معنا دارد که در چارچوب مشخص و با حفظ منافع ملت انجام شود، نه خارج از آن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121943" target="_blank">📅 11:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121942">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل: چندین دولت واقع در سواحل جنوبی خلیج فارس در جریان جنگ علیه ایران، «عملاً شانه‌ به شانه آمریکا» عمل کرده‌اند
🔴
آن‌ها موظف به جبران کامل خسارات علیه ایران هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/121942" target="_blank">📅 11:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121941">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
آکسیوس: هیچ نشانه‌ای از تصمیم ترامپ برای از سرگیری جنگ با ایران وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121941" target="_blank">📅 11:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121940">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">برخی شایعات حاکی از آن است که سفارت آمریکا درخواست ویزای شجاع خلیل‌زاده، مهدی طارمی و احسان حاج‌صفی را رد کرده است
@AloSport</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/121940" target="_blank">📅 10:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121939">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
چهار عضو کابینه ترامپ که در سه ماه گذشته از سمت خود کناره‌گیری کرده‌اند، همگی زن هستند:
🔴
تولسی گابارد، مدیر اطلاعات ملی آمریکا
🔴
کریستی نوم، وزیر امنیت داخلی
🔴
پم باندی، وزیر دادگستری
🔴
لوری چاوز-درمر، وزیر کار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121939" target="_blank">📅 10:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121938">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uiW6EUezuY7CnMG80PP6HOHCQh_bij4RtLtYCLS7rw2WrGAaV5mlFtZBajXop28YiqshuwoHZUXDEMZ8Xw7LQCM5yFbJibbmzjpyA2KR9WKRudtcw2cTY-vdKu8j5Y9r2Su0Rrv35Ghm71xD19WejGdcw-sNlY4dLb2NyK0ofVNnFRgJV2zOuRyZJHv4HZdzuVinTbsQHEXqvYAppK60RD4Mx8S8Zn6dWzLRafCw413VWYJ_coePNE4NeRQgfiBOkzEIn9zyuZJfYlnYChLUMzPVKFJlzE3jFMzby6m_dFixW7KjD_-XaWCxpykxlm5-The0c8QInTyVSx9Pn1sezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121938" target="_blank">📅 10:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121937">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سردار طلایی‌نیک: تنها راه خروج از جنگ، تأمین مطالبات ایران است و تمکین نکردن، شکست‌های بیشتری برای آمریکا رقم می‌زند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121937" target="_blank">📅 10:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121936">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwcEFLbmwcLvDFf8gJRiezajco9MP6QByav1gTCs9xhqh5Guktm9C3R5-ohrLJcB82AQ2CilWeLg_M4iRGLx_8wnny4Nqhb1xrjikPpvOQdrZr1dxy__lS8HgQ1eXJiJNrjFTUVCv_b-cx-TS4oQF_xGFY0gcYdsvsqgMWCN7Hw1bdT4FTeZSMJvrYZY8swT7pwWZdvMM18vrrnIXieo6-y79poK4MOiP5pheQD0YZ3pvHV3IZhDlmteSsSbQoKcSAUC6-H_BAu_6Qo8_J1iDRBx9-rCPjoVfkxpjM0aL1xrdyv4oEM4Mqu3EMwMMGICNhCTxOrN6mGxF5_h53TQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت سنگال منحل شد
🔴
رئیس جمهور سنگال در شرایط پرتنش این کشور و در پی بالا گرفتن اختلافات با دولت، نخست وزیر متحد و حامی سابق خود را برکنار و دولت را منحل کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/121936" target="_blank">📅 10:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121935">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: درنهایت برآورد اسرائیل اینه که هیچ توافقی انجام نخواهد شد و ارتش دفاعی اسرائیل برای شروع موج جدیدی از حملات به ایران طی روزای آینده آماده می‌شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121935" target="_blank">📅 10:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121934">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
الجزیره: اولین نفتکش تحت مدیریت ژاپن که از تنگه هرمز عبور کرده، به‌ زودی در این کشور پهلو می‌گیرد
🔴
این نفتکش با پرچم پاناما به نام «ایدهمیتسو مارو» قرار است روز دوشنبه به یک پالایشگاه در استان آیچی ژاپن برسد. به گزارش اناچکی، این کشتی حامل حدود دو میلیون بشکه نفت خام عربستان سعودی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121934" target="_blank">📅 10:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121933">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
گزارش الجزیره از معادله جدید در تنگه هرمز
🔴
عبور کشتی‌ها منوط به هماهنگی با تهران؛ بهای خدمات به بیت‌کوین!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121933" target="_blank">📅 10:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121932">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
معاریو:‌ حزب‌الله در حال تکرار تاکتیک‌های قدیمی است؛ نیرویی از دو واحد ویژه این هفته در نزدیکی رودخانه لیتانی عملیات انجام داد.
🔴
آنها با نیروهای ما جنگیدند، آنها را زیر نظر داشتند، مسیر حرکت آنها را به درستی تحلیل کردند و یک وسیله انفجاری را جاسازی و هنگام مشاهده نیروها آن را منفجر کردند. چهار سرباز زخمی شدند.
🔴
کپی برابر اصل از جنگ چریکی که حزب‌الله علیه ارتش اسرائیل در جنوب لبنان در دوره منطقه امنیتی ۱۹۸۵ - ۲۰۰۰، انجام داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121932" target="_blank">📅 10:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121929">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKKcJPYnKZsGAIfkYMx7yrW9wn384XEYoi6Bv7mG21Iqumw7dTjuOx_VmyNy6MaTGM01akY9k3-880KV6rLSBcQIEzTPXj7CfuF5B4jpb6S1LIffuUnWDa7SYxWLRmAOR3QiyvpQ0CWA5S0oSG7eLCP6dXDCsyc6duEfYplNxa5BnMC_w1ak49fDZgApyhqW2d8Oz2qM0pIBn-1N6KbFVJkEvAJR0XMIiw3F3bKNVNeKI-alQuVgF4gJ9A-kOpH_-pgWP7OrtV4F1wB-Z4AKkAen_sm7aYHpOXzcZYraD6a0g-HDn26Y1ovpJa4GUtFsoVye4LALiw3dl-cM9bCahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLkDG2j_LDaw4JRLfaortQ3-nnGkxrlvAo8m4pXSwMDEc1GoSlgb1L-Jq3vPt1zmCU9GHIDmKomSIhB7ramLjuOAUQx15yQHezt6EdWNTaAnqI5IwtJ9YjWzJNffduBCKO7cpegm-255gmNzBtuRjiE4MUWCWsWvPz5y3ToKg_p5h0WrC9TtX23ZF-tHT9_Fp_Jw1ZQPKNAdUtWrXjW7X_cKHmlwik606mJmJedcvPWOdCJoca5iwI92wxsuw5svxwSiW_RbmkJQEEp2wVjbzk9q-rv4bzJ6SZW3hrqDLNJxrdOaQe7K_9i54fwctgRjQouD_wce1-edxO3PaBB26w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qeXJOkdEdSwhwll_URWZerIPelP7XVirfMmmyI8qdlFpiCUYhR87rC6y72_Y_TY5UYUs-9ro5bg0haUISWPDgoeYaYLXlwG9SRl23PtsQvPCu5_IEKiQt5KXxhZEvTelicrvqZf230Ppkdqz-W0fu0BKA9TQSOl4r0KVuMQNsZD0Jl_MumcjfJOna5CR0RGueY9fSAFci9eEMqCg0JLnLvmMAw4XMMXvhT_NuqrIK3rs9RrsSonUQ_fSInnQEaMjyld9FI74WGXWwrzbKKoj0A1nyih4iMFFhiKNx9VfidNH_Yz_CiEDysQX3JLdNxl0Q2R7dJK-ZLLETuYFcLhA7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک هلیکوپتر مدل MH-60S نیروی دریایی آمریکا با فراخوان RESCU11 بر فراز خلیج عمان مشاهده شد. ‏ممکن است ماموریت نجات باشد. (این هلیکوپتر متعلق به یکی از کشتی‌های جنگی مستقر در دریای عمان است)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121929" target="_blank">📅 10:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121928">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
تماس تلفنی وزرای خارجه ایران  و عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121928" target="_blank">📅 10:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121927">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4901ad7b09.mp4?token=M5j-Yf7C__P50cd9E3bIS7xHfyo0Nb2JVl_Movpd8Ictiiz4dQXKGonTsfWndWWWL7jhrMy2i8yLI9DTCVMDCl6HKnvIa4s-ooAjVaWP8d2F-Z-6dZQnbEiHREwbrHya9mmvmVRUVC7mrSG4yzeW9rF_nmXJ1TzWwbydlvjIiMQMO8ro5Nt7nsAYVx-mKqBvx4QiY8EKQRvA-Bp9X0uRUowB4Sp5VaEo_GZZbqspH0yoxhIx0hochVK38EEBZRjOdI7Ex-Bsw4S0Go2ahkCgz9DqbePNNum4UE3388eFHnFuKtDeerEGZ-sUvWOvAcPDwoPN3acaiEn60z4dMMJhfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4901ad7b09.mp4?token=M5j-Yf7C__P50cd9E3bIS7xHfyo0Nb2JVl_Movpd8Ictiiz4dQXKGonTsfWndWWWL7jhrMy2i8yLI9DTCVMDCl6HKnvIa4s-ooAjVaWP8d2F-Z-6dZQnbEiHREwbrHya9mmvmVRUVC7mrSG4yzeW9rF_nmXJ1TzWwbydlvjIiMQMO8ro5Nt7nsAYVx-mKqBvx4QiY8EKQRvA-Bp9X0uRUowB4Sp5VaEo_GZZbqspH0yoxhIx0hochVK38EEBZRjOdI7Ex-Bsw4S0Go2ahkCgz9DqbePNNum4UE3388eFHnFuKtDeerEGZ-sUvWOvAcPDwoPN3acaiEn60z4dMMJhfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه CBS به نقل از چند منبع آگاه از برنامه‌ریزی‌های نظامی اعلام کرد که دولت ترامپ در حال آماده شدن برای دور جدیدی از حملات علیه ایران است، هرچند هنوز به تصمیم نهایی نرسیده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121927" target="_blank">📅 09:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121926">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
دیوید تیلور، نماینده پارلمان بریتانیا با اشاره به تأثیرگذاری شبکه پرس‌تی‌وی در بریتانیا، خواستار اعمال تحریم‌های مالی علیه شبکه‎‌های پرس‌تی‌‌وی و هیسپن‌تی‌وی شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121926" target="_blank">📅 09:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121925">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
یزدی خواه، نماینده مجلس اعلام کرده که فعلاً اینترنت بازگشایی نمی‌شود و بیش از ۹۰ درصد نیازهای مردم در فضای فعلی برآورده می‌شود؛ دسترسی به اینترنت بین‌الملل فقط برای گروه‌های خاص مانند شرکت‌های صادراتی، موسسات علمی و پژوهشی باز شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121925" target="_blank">📅 09:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37645353b1.mp4?token=l4644w9eQQxhcEE1sMExbeltf2xaUvSo_gjEvpUFHzBvhVdGoW4GD2LsBCMGx1O29jS4JXGhtuvxSk8J9Q85R-XyP9D3BMewAv13VMIXwfFR3ZIjgVuBBsFTrfkokOkQAH0tzCurtTb-RQISSc7lir8xryccVqDWOn4ek8Kv5ADMG0vappfnm2T9fYUw9tu9dWYEFKLrJtVE9WE9T4DoTP8BtSqALf33mp-pZyRdoTb-brVq46FGrFCGe9LZNaSUwIXeejoFfknbVW1OF9G7HbAod-yLSMUOE-JD27-RbVvAn33XVuk4XHxue3O9BE9LgCklEgjJL1-snskGgqWpSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37645353b1.mp4?token=l4644w9eQQxhcEE1sMExbeltf2xaUvSo_gjEvpUFHzBvhVdGoW4GD2LsBCMGx1O29jS4JXGhtuvxSk8J9Q85R-XyP9D3BMewAv13VMIXwfFR3ZIjgVuBBsFTrfkokOkQAH0tzCurtTb-RQISSc7lir8xryccVqDWOn4ek8Kv5ADMG0vappfnm2T9fYUw9tu9dWYEFKLrJtVE9WE9T4DoTP8BtSqALf33mp-pZyRdoTb-brVq46FGrFCGe9LZNaSUwIXeejoFfknbVW1OF9G7HbAod-yLSMUOE-JD27-RbVvAn33XVuk4XHxue3O9BE9LgCklEgjJL1-snskGgqWpSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس دفتر کاخ سفید و دستیار ترامپ، دن اسکاوینو، ویدیویی از بمب‌افکن‌های مخفی‌کار B-2 را بدون هیچ زمینه‌ای منتشر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/121924" target="_blank">📅 09:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فعال شدن آژیرها در کریات شمونا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121923" target="_blank">📅 09:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPB8j_P7E1FA7rdYw5esbhwuPgN05-P1LdgexTz3Ui7IauKYZBh9pnLakym5ZPX1TstWmpa_e47nggAIcF6YuevwfqmnTxQ5PGmbCBxY-KY2M4eWU6ngxNwOHp3zVux44Ektgt0JIgaMuWj1KWwG53-Et88CnudcH4KBVuToBD3bakP0mUz_1reDwfVguRPr5ru5GYh8EkqSXsnlveQLD-GKZXp3gHUBGCcHuxI59hw8AAp9k8IJTuwCfOEhRQ__qMi4FfySXmU1nYazwbQL1hJz2EpJqJxGA7bLMudPpGh6RRPP6XmPLFBKKBXv27ix3GgdAh5IPc5412yG-wUQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روبیو وارد هند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/121922" target="_blank">📅 09:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121920">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GIAAmS6bCDtCFFBg5A25bxNYcFcioXUk0FrLkvHDgyap8RE-d8S8-8_0JBiUQHzsRZqbeEbOrUjktysdPbTXLw7LzDoW94Z34KJInO8kS3a0g4un5Fsf_rXG9FzL1_i3PQMUC_5XD62-1lWLwvKh3DdbYHFoM9S1If8pLIYEFJqDwHCH79dihNQ1aC1HzDwdpHhrL5KsK-3Dujc6rXVYp-I_UGS7IDDxgzbrxdl5wg7yogH5X74tDYmeTe8KjMlmMNC-q_Gu1hlGpUk5fW2eguip9lIwm9QBV9RaH4gt91fTm44uejkpbLpWOzu03tjnM7NfF6JLTQbYHbb-JDjsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gDF2ibetkw30ttbVnOjIIv3m3drRluBJ3g2dqGvTR8x8jy1JqA63Rp6lMmT8N0tG6SsbpWrL1LnRBN-3y4oyf5i1sWe0LeHckOm5sEZFmJxVaZaCaujQ_a02f5eq0QZMrDeJfZ46rDDWVOFOMKSd1hYoRQO7jINhMOCE5Lt5O_v_5DDUAazM9nWU2Xx-NpcZ8XX8810iLKIxZU0u5fyJBKOu0a--y9HAnIWtg2GXOzNtxXpO-voC7-XU5hlr_R2cSyVpyZ-arCQcfv6e12l0_sn9apKEkD_L6dbk757s64e9h2CQM59dptCBF853Kq2mILfmpwRIEEZRNR9Udjsz4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
محمدباقر السعدی، فرمانده ارشد گردان‌های حزب‌الله عراق، قصد داشت به ایوانکا ترامپ، دختر رئیس‌جمهور آمریکا برای انتقام ترور قاسم سلیمانی حمله کند. او نقشه خانه ایوانکا در فلوریدا را در اختیار داشت. السعدی اخیراً در ترکیه بازداشت شده و در آمریکا علیه او کیفرخواست صادر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/121920" target="_blank">📅 09:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121919">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI7NXwFTuEFmpmbVzy1vX-BnWHwsog03xV-PTAx8ButHfx3qfvGEAcODU46Md0NgBrTWs3qOS_L4ghHNdjQ9GEMbOXJH8Xwh8XXWET2FhiSRtudIMBUOMfWHDlJhKMNtBFZitzgwNyPXGHHOjatB7ZyWUgxXidjgnF4pC8I5tW-ZuziijY8JSXlzhyAqSZQzSqvsplTUm9Mrqq9KArgrgtJwhlkRGIRkpEblIHZiUBU_i8GX-uPNm7H0JXm6VSAKDBOqfoUQjfFCI0QKasrSf-FGX7DghPI-Z5Vv2s6i5jczFh7wwCP1UgCQS3ZwA0pO23J6y3Tl3m6ILTu_juTzSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121919" target="_blank">📅 09:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121918">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soT9HqtMWcICUF0sNfptPG9v0NfbyLx36e9BFFp48z_pPumS3mFv4bh06gtwvz3TO4RrY25IidRSxgcynILUhyWfTz6zdvvkoyEm4vqOcz3eYS4ODHQiamBcmz5RP017OmZbWhMkhwRfeRNiU5PPuxSsPGbhMR1R66nQI3W2nqNJqyYJrqC8uC6L69oxGTJfQWc8uyG-OZvS2xkrjQbt1w8XfunddQkBLjeN6_qPagk2JkVPxmSj1lBYtQRJVdTR-SwJeF_Y6yqYlO9SruMN0A6RSCYCtJNkB2rOyZyDvg62HH-CrQ9vbDOUDGeVk12qNkU4BNkm7_nRuhHxAeEK1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گفت وگوی تلفنی عراقچی با وزیران خارجه ترکیه، قطر و عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121918" target="_blank">📅 09:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121917">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سازمان ملل خواستار پاسخگویی درباره رفتار تحقیرآمیز با فعالان کاروان غزه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121917" target="_blank">📅 08:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121916">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYioxifEhIcUFYJq93PXGH9iEb7A35MYeptYklIzii7Gdj96KY4lVFfwQFM7OJFnU2qmwzHD5AlJC1wPmC4CMOWmLIvzRUY3T6h_YH_dC2zVL570Ib-JGML_7D8IGl1UrAGf8hwgyAaQLv9ePn9YaUIOIzcDyakRd5x_kGznxWgHXjahVrv3brXMcjbbQGf0T05rnZgVmhh1ToaUxMYav048QXla4r6v4wpwvbDUgkVao1bMJ00lyoi4pYm6c97_Biryk63vkunyn_HZ9MvdZyVFIubKiX44X13ayrDrph6rel-tQn-dfPESV8f3KhMfZya-Qfq18STZLySRJTl6sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی و فرمانده ارتش پاکستان با هم تو تهران دیدار کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/121916" target="_blank">📅 08:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121915">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا: گزارشی از یک حادثه در فاصله ۲۰۰ مایل دریایی (۳۷۰ کیلومتر) غرب جزیره سقطری یمن دریافت کردیم
🔴
یک تانکر حامل فرآورده‌های نفتی گفته است یک شناور کوچک با پنج سرنشین به آن نزدیک شده است.
🔴
این شناور تا فاصله ۱۰۰ متری (۳۲۸ فوت) تانکر نزدیک شده بوده، اما پس از استقرار تیم امنیتی مسلح تانکر، مسیر خود را تغییر داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/121915" target="_blank">📅 08:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121914">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وال‌استریت ژورنال: ترامپ در جلسه روز جمعه به دستیارانش گفته که می‌خواهد به دیپلماسی زمان بیشتری بدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/121914" target="_blank">📅 08:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121913">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8W_tjfLDS-6zYjR2QmzsE08CTrR4lDlnXjY5dGEQBd5OSaYxBjGCU0WqboUbdAKCr7fQgpxR7UEOzM9QxRMCFC3sae1fGEqzaphvDANFs0ZUfvHseGt_MjUTj_O1TzwrAmGKpppZoKVXEyDwgGwDM59wFFJ_sNr0aw0y4XdBQN1BtU4UOYh82FU3SJbAlOiJ7ALWn4-oLw8udkU1wtlXcUJZfDd8YUhC4qN5cH_dbaeMWNnR2KWAXrAn6kz3hkrxx_vxWCAfVRj2-_G7S5ssJ_muZ5etYmwdJusa2jHznxR4IqjCbuPpylhvqMnlpF2OUXD4IGvaLcg6JHjIPuNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیرس مورگان: جای تعجب نیست که اعتبار اسرائیل در سراسر جهان در حال سقوط است
🔴
پیرس مورگان، مجری انگلیسی خطاب به بن‌گویر نوشت: تو یک بیمار روانی هستی. با وجود افرادی مثل تو در دولت اسرائیل، جای تعجب نیست که اعتبار آن‌ها در سراسر جهان در حال سقوط است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/121913" target="_blank">📅 08:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121912">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
یک منبع عالی‌رتبه به العربیه گفت: فضای مذاکرات مثبت است و پیش‌نویس توافق آماده، ولی توافق نهایی حاصل نشده؛ تهران خواستار تضمین روشن برای آزادی دارایی‌های مسدودشده و رفع تحریم‌های نفتی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/121912" target="_blank">📅 08:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121911">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meRttmvweNsqGrZh9Dl8qYiZLlqGDQkJBYPFB96WyguMvJ-n_clbmdLALmfldrgOvfvi-kuzdjR5zlH5mUmF36qmc9cOJDpEU2aWFT2E5QWx8MmlOKQWlyI8uZ2-pBKgmsEn6DHTu8R1j7wjMmc0gGsyqt36I2HIoVuV3OwzisODbfK0olm1xAsz-_K07kaRLsmwhq_sZtOyPYTbJ6koRJqfU6T0YvtwIv2IW1rAS6C7Kn8nNquv51Yq6OUhxq_1Uh9I0mukCayVMXaV0Z9if1_iyN2oileQH31jsdri4RqCSuXm-1njp7AyAexIJ96OwQdgc_uUiVDRxAnqZrHDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به ساختمانی در صور در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/121911" target="_blank">📅 01:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121910">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
عراقچی هم اکنون:
زیاده‌خواهی آمریکا مانع اصلی در روند گفتگوها است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/alonews/121910" target="_blank">📅 01:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121909">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5302f20640.mp4?token=qcp9gFDhj0qtYWyN05ul19LzZ0Ijeg7HvxHxmwtWe_dGLKv46yIKEo6wN_q0WaRhpg65-RzejhDij_H1VsN2Y7-y22lVrXxunBdKJOJSkUd54oxBbBg7MQXt66SdBD9E5_E9aIADA9aDsvgR0UJvUZn-48VSlgHa6sop3amXFlRrdsVgdOWJm4-GZWH6amzjnqRmsyO6M9D5w8cQVn-r-QYPIhornGYPr9-5VfPKfGAsMMXccWSUP4bEmTlG7b1rp8MJY_u7XIlHd08rRxYLf9A_d6QrBT3D5UAv1Jk98GKUGw14zsHJDlg4QLiYTM28Lc0Y9LrqZGU-9JnXv4j-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5302f20640.mp4?token=qcp9gFDhj0qtYWyN05ul19LzZ0Ijeg7HvxHxmwtWe_dGLKv46yIKEo6wN_q0WaRhpg65-RzejhDij_H1VsN2Y7-y22lVrXxunBdKJOJSkUd54oxBbBg7MQXt66SdBD9E5_E9aIADA9aDsvgR0UJvUZn-48VSlgHa6sop3amXFlRrdsVgdOWJm4-GZWH6amzjnqRmsyO6M9D5w8cQVn-r-QYPIhornGYPr9-5VfPKfGAsMMXccWSUP4bEmTlG7b1rp8MJY_u7XIlHd08rRxYLf9A_d6QrBT3D5UAv1Jk98GKUGw14zsHJDlg4QLiYTM28Lc0Y9LrqZGU-9JnXv4j-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به سمت کاخ سفید رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/alonews/121909" target="_blank">📅 01:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121908">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgRgN_Facv400vjkapgWmDj52Tb3wzECcTwf2qK8XCjl7wMJudyz9C4YmVR-KUyO2SkuUz-gpZ2z41dCy9ePvKfTwoLeS_xsqx0Yy36cDNS9Qutn3-kj-NufCFZ3ZCq-Vdh85-DSEdV5zqeXxe6euMDwr-LZJliorrWaqZnXoLI0Y9TPRbf9iRG6TzusFUMzuij-vL183bEf-Nfdxx0hQNdHzZhEIFqua5wwlWs9VW-wOAyP6Tou2iBMViX7GnD4Yhf8o1cKUKpTsha5SFriNkURjk17y6HFrS_oZXrnIZBeRhAvuReUU0oO2I64PfrLHph0uXVZX_w8kuUdxhYMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فضای هوایی غرب ایران طبق یک NOTAM جدید تا صبح روز دوشنبه بسته شده است، به‌جز پروازهای روزانه (در ساعات روشنایی روز).
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/121908" target="_blank">📅 01:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121907">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
دقایقی پیش بازار بورس آمریکا برای حدود ۹۰ ساعت آینده بسته شد.
اگر قرار است ترامپ فرمانی صادر کند امشب یا فرداشب صادر میشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/alonews/121907" target="_blank">📅 01:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121906">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
منبعی عالی‌رتبه به العربیه: فضای مذاکرات مثبت است، اما تاکنون به توافق نهایی نرسیده‌اند.
🔴
«پیش‌نویس توافق آماده است که نیاز به موافقت تهران و واشنگتن دارد.»
🔴
«تهران خواستار تضمین‌های روشن در مورد آزادی دارایی‌های مسدودشده و تحریم‌های نفتی است.»
🔴
کار برای کاهش فاصله بین خواسته‌های مشروع ما و خواسته‌های واشنگتن در جریان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/121906" target="_blank">📅 00:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121905">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76666c05ca.mp4?token=eux0agEN-JUwOQE9W4FAn8wQK2Z8YnMorAe3yEOX9MYSzCw_IRrlekAPUOsfmaqfvPQlWv75qxiNJCuzDrOSZedhN7FPtJUd-o1e8nVLfhOO8BD8_A026zsq_8YMCEKUvhhfirT1HInix1yuBpJ6T8UUO_T1RHvXVl8eZ77aHhxGGrf3pIPHAQ7fXCKYmHVvmmIlvPnqnfn_yyPJY7aXpd7HYd-uogEwKCaILPfYnIJvRaJBESs1w-qpn53t-cGV241H4Pkm2QMTsW9bUQcVUNnxSVoTUMDSnKZfgH_4b9wH-Zt_uZFOctLZmOEXuB5SyIuq7Rq_FxUyxLdyRSuaFojlhy3NfLM7v2tzk3-Vun6rSR_NsGtIgifTIIFtNERCBGtcx6XFMRoTWAD1a2M9gcBDBrgFG0VD8kYL_YhQ3UkCISgNAMpTsRdwGoM7hX8kAWn8rA4u_8kYlGL3lnXpRiILKbMr6nMIwdmFMNCaznTSvhOCmxur8Q6qCZ-85qXYs6kt1wAe1Vfl3xT6sSK93ZvMsFRegA3nMVWRgBwth4TDVV6jTLt7AUliWioJ-Uq_V1KyHb3t3eH8l-HNj9-V12zNIuyf1XUcU5fY18EwjkeJ9D0YAbYLnf2tyALlwsMJwdVxH7wQSut7ZbTylEX6NfJ5dHhESq4n4ndtzB1Ryhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76666c05ca.mp4?token=eux0agEN-JUwOQE9W4FAn8wQK2Z8YnMorAe3yEOX9MYSzCw_IRrlekAPUOsfmaqfvPQlWv75qxiNJCuzDrOSZedhN7FPtJUd-o1e8nVLfhOO8BD8_A026zsq_8YMCEKUvhhfirT1HInix1yuBpJ6T8UUO_T1RHvXVl8eZ77aHhxGGrf3pIPHAQ7fXCKYmHVvmmIlvPnqnfn_yyPJY7aXpd7HYd-uogEwKCaILPfYnIJvRaJBESs1w-qpn53t-cGV241H4Pkm2QMTsW9bUQcVUNnxSVoTUMDSnKZfgH_4b9wH-Zt_uZFOctLZmOEXuB5SyIuq7Rq_FxUyxLdyRSuaFojlhy3NfLM7v2tzk3-Vun6rSR_NsGtIgifTIIFtNERCBGtcx6XFMRoTWAD1a2M9gcBDBrgFG0VD8kYL_YhQ3UkCISgNAMpTsRdwGoM7hX8kAWn8rA4u_8kYlGL3lnXpRiILKbMr6nMIwdmFMNCaznTSvhOCmxur8Q6qCZ-85qXYs6kt1wAe1Vfl3xT6sSK93ZvMsFRegA3nMVWRgBwth4TDVV6jTLt7AUliWioJ-Uq_V1KyHb3t3eH8l-HNj9-V12zNIuyf1XUcU5fY18EwjkeJ9D0YAbYLnf2tyALlwsMJwdVxH7wQSut7ZbTylEX6NfJ5dHhESq4n4ndtzB1Ryhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کسشرهای ترامپ تموم؛ آخرش هم یه رقص معروفشو زد قمار باز
‎
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/alonews/121905" target="_blank">📅 00:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121904">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: «مسئله‌ی ایران خیلی زود تمام می‌شود و همه‌چیز به‌‌ سرعت به حالت عادی بازمی‌گردد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/121904" target="_blank">📅 00:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121903">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یک مقام ایرانی به المانیتور گفت که «برخی ایده‌ها و متون جدید بین دو طرف مبادله شده است.»
🔴
این مقام افزود: «این فقط می‌تواند مبنایی برای گفتگو بین ایران و ایالات متحده باشد. به معنای توافقی نیست که بتوان آن را اعلام کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/121903" target="_blank">📅 00:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121902">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / اکسیوس: ترامپ امروز با افسران ارشد جلسه داشت به شدت درحال بررسی بازگشت به جنگه!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/alonews/121902" target="_blank">📅 00:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121901">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
اکسیوس:برخی منابع نزدیک به مذاکرات همچنان بر این باورند که طی ۲۴ ساعت آینده فرصتی برای نوعی پیشرفت وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/alonews/121901" target="_blank">📅 00:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121900">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری / اکسیوس: ترامپ امروز با افسران ارشد جلسه داشت به شدت درحال بررسی بازگشت به جنگه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/alonews/121900" target="_blank">📅 00:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121899">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0a0b67a23.mp4?token=FV1XvE-7Z_1QVm4LUVYhTqgnSVYp-WsSdbC34CctaXurpf6XWctecAjQ6j6MC2FdS6AicULnzc0EwLgPX2iD4yhF0NlA0fCqCCEJ0tsRzcAtcaDr2EE-G_6eGLFGVg1qw6wPzA-G4BHeqeDu9wPF0XvUlcDHYL-i-93w4NabW0UiPZ12xov9yU_gBJRUfKCa694h8rU9RxeuWFzqeSAbmvr2pUSr9iiJMegs3KLjtaSqFgsciT7OLvEInVnz1wTK3Cuwo4wZdZB4eyNPRabY8qxEYsGnHnr8FxNBmiFTR3rOC0X0WsySA99mW4Cr1KEgNNfGg_zjYbX5ILLyD8ijtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0a0b67a23.mp4?token=FV1XvE-7Z_1QVm4LUVYhTqgnSVYp-WsSdbC34CctaXurpf6XWctecAjQ6j6MC2FdS6AicULnzc0EwLgPX2iD4yhF0NlA0fCqCCEJ0tsRzcAtcaDr2EE-G_6eGLFGVg1qw6wPzA-G4BHeqeDu9wPF0XvUlcDHYL-i-93w4NabW0UiPZ12xov9yU_gBJRUfKCa694h8rU9RxeuWFzqeSAbmvr2pUSr9iiJMegs3KLjtaSqFgsciT7OLvEInVnz1wTK3Cuwo4wZdZB4eyNPRabY8qxEYsGnHnr8FxNBmiFTR3rOC0X0WsySA99mW4Cr1KEgNNfGg_zjYbX5ILLyD8ijtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما جلوی ایران رو گرفتیم اونها هرگز نباید سلاح هسته ای داشته باشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/121899" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121898">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11fa26796b.mp4?token=Rfn3eRu39faRB2Xb8XAPOZpMDXLCDZMaXfRlA1ghnSTmTaEft-pv82OkeV0tCRKu4o-Xe6fe0iC7Wya5JgMORaKlMIFrpr4bVu7x6KX_dOHRz6e7td84VOSQIZvtqHNlWW-YfIYq01ca7symNrDJWHlTcAmT2F99SZyI75OlO0POJwU-y03U58dmbG0U_mkSvxYomNkM8I9HEFZDf2WkJKSHf-RMl5FA968N6lGxhdeTffllgW6Ey9UlN9viRYYqMNEUgWPuainOyyylP6JuDWpeNqFPXoia5Yv9OqRCKbe1octPANKKZoPFW7L5rPkAsFjl7_UInXGNFb91do3gtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11fa26796b.mp4?token=Rfn3eRu39faRB2Xb8XAPOZpMDXLCDZMaXfRlA1ghnSTmTaEft-pv82OkeV0tCRKu4o-Xe6fe0iC7Wya5JgMORaKlMIFrpr4bVu7x6KX_dOHRz6e7td84VOSQIZvtqHNlWW-YfIYq01ca7symNrDJWHlTcAmT2F99SZyI75OlO0POJwU-y03U58dmbG0U_mkSvxYomNkM8I9HEFZDf2WkJKSHf-RMl5FA968N6lGxhdeTffllgW6Ey9UlN9viRYYqMNEUgWPuainOyyylP6JuDWpeNqFPXoia5Yv9OqRCKbe1octPANKKZoPFW7L5rPkAsFjl7_UInXGNFb91do3gtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ می‌گوید این محاسبه را درست انجام داده است:(203 × 9 ÷ 2 + 1324 − 1292) × 19
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/121898" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121897">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af1fc50695.mp4?token=PEETLUd8xUk78YqrpbpvfmpkwhGX37LTyWmAauWt46wNVx_etnG1edV2wB_RYz0AQn5513hSGzZ-raI9skhFnpqBZjgtBIxp2f56BpiCIiy2RDPMtlDwTmi3Jbmk5IjI57sZoDl_REwqWPAyCqfPXxyUX-O8bd4-kndIAqRtkjl-fn56CzqxkdwI4dLp3SiwLQerLnoasm_oRMqmCcpERWSKnGaYWtGX8hqXCwrIYIY_aURUPIVP2_E96ReaJLmQEmMPBP7sHLxTjq867Ya-L8c1MloWqIRNKgSlWy4OlrmpOmDQZ6DnQiz7rgRtqSuhslgnYEGRvDI7g2V2J4FcrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af1fc50695.mp4?token=PEETLUd8xUk78YqrpbpvfmpkwhGX37LTyWmAauWt46wNVx_etnG1edV2wB_RYz0AQn5513hSGzZ-raI9skhFnpqBZjgtBIxp2f56BpiCIiy2RDPMtlDwTmi3Jbmk5IjI57sZoDl_REwqWPAyCqfPXxyUX-O8bd4-kndIAqRtkjl-fn56CzqxkdwI4dLp3SiwLQerLnoasm_oRMqmCcpERWSKnGaYWtGX8hqXCwrIYIY_aURUPIVP2_E96ReaJLmQEmMPBP7sHLxTjq867Ya-L8c1MloWqIRNKgSlWy4OlrmpOmDQZ6DnQiz7rgRtqSuhslgnYEGRvDI7g2V2J4FcrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره تست شناختی : بایدن حتی سوال اول رو هم نمی‌تونست جواب بده
🔴
فکر نمی‌کنم بتونه بگیره اینا رو کدوم خرسه کدوم اسبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/121897" target="_blank">📅 00:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121896">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: «از ناهار خوردن با کسی که واقعاً، واقعاً موفق است متنفرم، چون او مدام درباره‌ی عالی بودن خودش لاف میزند و این مانع از این می‌شود که من درباره‌ی این حرف بزنم که رئیس‌جمهور شدم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/121896" target="_blank">📅 00:05 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
