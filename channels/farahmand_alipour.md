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
<img src="https://cdn4.telesco.pe/file/cbU3eORFKmYNVSaWUlIQMdEaNUhjNftOgBwQ1h5nHZ397Szdl2nKaEWa2E3WS0-f5klnTNxrnEtX6ckcMQJ_mlvM5exD7qdh9ILCj8PgAZD8xcT3e2a4BewtfomKlz9maQQ8N5hsJ67-cOHiMZkEw_-1f12kU4f8OllskMgvBPTouWNppR1eDfpIuOG1jr3yYpSqBjySfmHIhdUOjZ5M-k08rUcUq6GHZ2UFgrbnplzhFKqyNkCbj-PEDdbAjH__6FZfCWZGoM1GW5hxcatieEb-AAHpFq6mIYMVoyZptkXZlPY3AjvTVZ-LvjSeAD4U86Unv89fLJ1N6Kf9m9nQAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 22:20:19</div>
<hr>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9LuuOXkJJJ11GtRZ9pNp1zF4kdbQHHlGLDop6TDMS7y97g8_HSOOhVpyy1MsmJKocbNFTnDDXn7f5imiuMb4MoFiCm9Ei2UBSB_mkQLJNhf_f1d6eaA9K54shcZwqCCGjhyzl-4PASTS43QNJ1sUFZWe5GOKi3k1j2pDkJdRzzpgogM6eXbhla0b7rBsovEBbA0qS-FVF3rQw4Hjlb8iB075ez5448hzCZwDLqdYPFL3ubjs4UfA3PhOqxQCK8ImOjwEaraC3a7d-CXgRZU35UWxotshIt3xFvFatUgDx3U9nl8iwFMmkFvMem_3GJGR3Toetms_y7fB_m113PvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY3Q2AHJn5uDtLFColFfCMpe3qaje_eKXc-uoay-xKRgSlvSPnLo3DzewH-Qi0uNscdQCjItqVXI-684BCOb4I-e24tBKcdReWDUq80BHwGZg0aPvccBWw3CeCgxgWNxOzj3mdfQpkiSw3hqc3H6neo8X0ndmmXh-eBpUaDoj_LikZK-K4sX__WYPrAaZn-V5Z4-WE1wnDDuUsM9wZxu_0_ggPxb85S1sdYb9WqrS3n_pzr1MzZvD-ZEgX3QFHXWRXoIIJ82sHmlaVxDvnycXvlsUm2TxuGni_2g80uDbUL5aw0sxX-ZWkhIoM4TooJUdT5yBJXm4koYE7gXp6KlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJxuu2KHZHunrWNUVKXExmubGffLYqOPo0x23EvsKZ64JI7B5hjYft7tmODY6Y5GZQi0zl6U-FYGOyaU-E-4Mir-98vHsgumWlwmro3OlBd32SuBefwaQvBsv_lvceI43gqXoXcssxN_mheIj0ln6y73edEPWGpolcIj8EMdxVm7hYt8ckJjnZz1bQr7-psk3f51xGte6zNQLL6f4MobiN9dx2i2Y9KRVULsXuVicsjkdr792kc6oZQGR7jj47XlgK2-M5Pmh40yZDJE0wB6DdlMcwHQtY-kcLsn2lDNCHzbFIvrmyLF2UO-tjhfmf9NIROwY90z4spgbc0Ytwm1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjmUzi9johmzWQWPuTw11kOZKyWRKZE6Rq4YsD-fC-AOJBezxFPt7NthaHW52aQmB4njlxuSuayXzefi1ocVOFcSfRW2vukC5tY3NMDNNYIA0ZDGKM2k1FGiP9snPbUkywkhXau0AlEjyomIk3z2tvODd2SMM_2TcviHl0IeMWRLOxlteICESGIK9erT5m5Fx2N7HgKhsGjQmM49knQeffVHfmTk62Q0NdMUZWXIh4Jm-CWb0llYdR1K4uB8RmuhSgiHd4wwfquEMCZBkk5RiedxUKNo1fPi0jsLkKKhPTAHkqb8i2pogu60qQuo6h4nXlGrDGvK9VDou57v5AlDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxEBTaWPYFYgBoVjH8ycpvW7Ua9nXYqGenHF4kmK2m1AWxh_9EwC07szc_QqWWZCgY6SgzCzjfx7XFjgGE1s7XFA1TAJ_kL62Up8UuHb67pnqdZdFlcg_ivTvhMbHpq9TXPqgtXkK1q5pLiPzVBfmiZZp-2RCul2bpMiz7jylxPxc8MFTuSQa5RSrpQlgiOoeG0f2zyfdrAzYVCZhx7jMulFQxSWs3vFDCxlwJn4_-i-4jiQmNe1gtSl4DhaibvLakRbvGCSU4QlhYX_DtImhB-gJDy3QpcnFwqXhZMZM7Aff4ZoQ-hRPkynDrR1VjRj5ARtUhT5Yn_-JNe62s_Ihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDpU9RJwLRRIjiRFMe0sGJ3NrwrmFdf2PfehFhmkdXqUh-dZJS_E229LfzdyMaOgy__n2N-JtFFAEKxiJHxU07MjYQL-ujO_Om42sPD9XMZXePkqNIMnH_x1YeKoHKrYmxRoNWawoVOUQSOqfzO7JiMF5l5im618mLB3u8laqzuY4FIRiFJx36XnU-NvlIf1ylK1qUwWf3mPplnauoYo6UMMY5MW0w9QRy3yZ0cleH9azRFQvZ82H4EIsU4fhxoNf2H0l8M43rAUmmTPqhhaFYMEdqrCHRYDbIa62iV1JaZj81A9S_BT_Ab6SNGVI8lX6NxdkbSBAEtWJ2vTXGJcAZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDpU9RJwLRRIjiRFMe0sGJ3NrwrmFdf2PfehFhmkdXqUh-dZJS_E229LfzdyMaOgy__n2N-JtFFAEKxiJHxU07MjYQL-ujO_Om42sPD9XMZXePkqNIMnH_x1YeKoHKrYmxRoNWawoVOUQSOqfzO7JiMF5l5im618mLB3u8laqzuY4FIRiFJx36XnU-NvlIf1ylK1qUwWf3mPplnauoYo6UMMY5MW0w9QRy3yZ0cleH9azRFQvZ82H4EIsU4fhxoNf2H0l8M43rAUmmTPqhhaFYMEdqrCHRYDbIa62iV1JaZj81A9S_BT_Ab6SNGVI8lX6NxdkbSBAEtWJ2vTXGJcAZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SA-ntt700ZS27ZCnM1PiNsSePDF1axiFbA03JQFfuaOFqWbyyduRyJTtvqya6-H_Z2K7Oamjar4eZklB1QYQc1pvzsTYdRRn02OXfu8lGftKP99uxl26qkvGdX4ytjBpPklrMa3iy070vdyymHFQ2XG2_bGxhp2uSOXrdJmxMh-eLRD79ygeqrL4Me-9IXcWlaflbsFKgCxCKD_I1lBAnngVC616ufdZKt10cqluQBVDfTuzWhIyqV6Y1CMcy8rTJ4QmwlXFeD8GzdMs9LqfboKXAGxYXkORzO84M8JnySM7m_xJ_lyOTyfWJNVUd_pdyAOVagjTyOKiLqEBtsRlfnTUMe4EHaZZg0CqEXQQfyLuCO5IBoC4m4wdRp6uvEe-1-NbXyXAEWB9YIr45kM2ghDUvDRsYoeVom8_QfmwwnVsNdWRAB2lDx06huN7TkB_fhs7ajraVrqpKbat8Ii8SFryd6scxlZ9IT3mxPvGERisSB4OBx_sMey9D-STkndV1oetOIxpvdEWcj_R6a16uT4rHf31HvNV1_Lx0mpk23laoPUho1MIy7AxkokUxN_dJ4BOB3BWkNPOcCQH7m-d5JB4h0_RqzT-BExyeWPDqFH6Tp45ZI_nA_xTLUvRCw2kZ6ErDvT4e87g1ilxRoGxbkkEXelBAR07n0ynm7z5d4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SA-ntt700ZS27ZCnM1PiNsSePDF1axiFbA03JQFfuaOFqWbyyduRyJTtvqya6-H_Z2K7Oamjar4eZklB1QYQc1pvzsTYdRRn02OXfu8lGftKP99uxl26qkvGdX4ytjBpPklrMa3iy070vdyymHFQ2XG2_bGxhp2uSOXrdJmxMh-eLRD79ygeqrL4Me-9IXcWlaflbsFKgCxCKD_I1lBAnngVC616ufdZKt10cqluQBVDfTuzWhIyqV6Y1CMcy8rTJ4QmwlXFeD8GzdMs9LqfboKXAGxYXkORzO84M8JnySM7m_xJ_lyOTyfWJNVUd_pdyAOVagjTyOKiLqEBtsRlfnTUMe4EHaZZg0CqEXQQfyLuCO5IBoC4m4wdRp6uvEe-1-NbXyXAEWB9YIr45kM2ghDUvDRsYoeVom8_QfmwwnVsNdWRAB2lDx06huN7TkB_fhs7ajraVrqpKbat8Ii8SFryd6scxlZ9IT3mxPvGERisSB4OBx_sMey9D-STkndV1oetOIxpvdEWcj_R6a16uT4rHf31HvNV1_Lx0mpk23laoPUho1MIy7AxkokUxN_dJ4BOB3BWkNPOcCQH7m-d5JB4h0_RqzT-BExyeWPDqFH6Tp45ZI_nA_xTLUvRCw2kZ6ErDvT4e87g1ilxRoGxbkkEXelBAR07n0ynm7z5d4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fztRn2exidVShVS38-afA4hxkjC4LotutVqLbGDBvFUvD-29nZBP9JFyCL7UCGcECfGprImzN33WwgCoIPaSW2FuWVHFTWO2fKfDxp9AVxzBIzCt500bsZJTSCHWpOZGfxkCGA0ik7Jwq6bibYBtJX2872sSZ-qaWjTfiEts0Mrx1c8KG4JWUTrF7uuHiuQJKCz0DKYc2o9vRNnFAir2jPixfsvHsoZ2N8574OPlUdxL1cYWz-NNBQrElRsrczAoImUHWhG1c0Aj9WSDexb8ANzEOrVbmXwEnKgwwH6mhXcSmGjO5uIv_xJbfqaoxZ_6VWVsl5a-JveZLMFsYCaGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XuUOyura1PqFICYpN--FoDRvfugu2kZEVs2wn6ENQM2A_6TI2ExhizW7T2CiUht3FwzNzB82imwOhFOZUHd-55Jgbb5a6SMeV_PZUyMd2p55j1Px8FmxT_miJfNfetEJcvW6h7YpwMYuZ8Ia-czCSjQWZHSQ7OrjQIJ4U-ecQwCl-YTabn5IAusER03XdhzQQi6oryj0eY129E0IjLjDX5IT4pK1F4n85LTpcNSNEuauyLstLZVpo8AAHrvpTPYsynfFl7nIuCxH7FrjKHXTnj-uCceCIjzAMhkLSZ10JeKfnn_hRfJ0I2EKFQApnCwPe0osm-5aQNayy31ysY1eSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XuUOyura1PqFICYpN--FoDRvfugu2kZEVs2wn6ENQM2A_6TI2ExhizW7T2CiUht3FwzNzB82imwOhFOZUHd-55Jgbb5a6SMeV_PZUyMd2p55j1Px8FmxT_miJfNfetEJcvW6h7YpwMYuZ8Ia-czCSjQWZHSQ7OrjQIJ4U-ecQwCl-YTabn5IAusER03XdhzQQi6oryj0eY129E0IjLjDX5IT4pK1F4n85LTpcNSNEuauyLstLZVpo8AAHrvpTPYsynfFl7nIuCxH7FrjKHXTnj-uCceCIjzAMhkLSZ10JeKfnn_hRfJ0I2EKFQApnCwPe0osm-5aQNayy31ysY1eSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=EQDqqUnmmainNW4tviUqMqoTQmCtCnAcytNt7YAFLSWRrA1ORHLYBc1GNW9hBgsIyYLMTR5IBxu6PXQciTqnEBnx147Lce8ij6qdUPeM9sOWsPJO-p4bYpFIRZDirBGhlXUVwU5CuxNkLWPVcaPFCB46Bc4evjZtNBH-OLdEk_nm_MxYANz3pkxKur017LU_7r8Lv3vIuS3tGrg0sLGq2zfrqQFh1FLI7LQ1p1nEeRSTYyjGMGatLTIhjn-05X7a9XC4vQGszGAzH6Q8R09tuFBnT5BWVY8TBvVRaHitBP6Py9AkDQ3lbek3qXjPuCTR7jwKl6vovs6XVlzNEI2rYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7U6VgsmWc6M0-vWa9P2SnAMmQ9Gp16g3XE_5UurUNL4IlTlKSRx-pA0V2WLJXDvF1OQQbYl0Fv6lL6vOjD_knC2Qm8xTG7d4EK2qW9viZqtLaUEsk-a3hRKaHsOoGZaiNt-sq2QeEwGRYlUGzG2JVLb9e_0ITB_ZUsBUDyfcOujpvBUAeOAwDAXKbaN-_0Khaqt-tzTRyevu3MxYUL79MaOA3o5d5tJGRGpeg5vSv_T1tZW2EYVVpUTpWzPcMtVrZqMIlODJNbm4A0EBvxRHor3Xrbhn4wpJnO6EARVCApNvIoR3cn0NDKeNBRQtHx-iRTESFnpMVSQBxVvTtBmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwIKd6DytcskgrREZ8hwA8c0pD0sZgM_-vgLSFSuppsLWvo4lKHUdnYamvU6KTJ0ZIwie4YA-P8WvlGHSSsdL1Tqj1EqYmTBJtXSZZJjRFO3ivP5mNbMPqYPVtPXuQk9OJ3aio7IybF7LKje0fKB21QUwTvctk4viQjjQTVEGzMXgeQYKOZ-JI-ojiPVYjQYGeBhs_G-zPRglqIgT0eNEBsIyy61lsLPDIe3zNaTwlZG02u33BI7OSk33P83sDXz49KXOUPsyBV0Igb4hJ2yXW5ne1QUNBSUjH4NSib_WEtNlf3eOJo1lKyP202mi84jZO9uilhtDq90cEmta9cboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=kFuWpp96iOhuXyaOmZ2SyrC_B44rMOv7IdXvBY_8nW6uYsyct77qvYZqNjLdEiS3-wUruZw_zuespSmh5gw06_ut9IIs8uhKzUloBHwVowjjd00qB7sGFR7pn2tk8N1I6iupx3HWPqafYieLgvVh20HocW_msFWqN2azMResOAZNllJrlnVK1tFF9xlD50RFSkvfzp902tvS3L17jQIdB2V-KUIJNj0MM3FBLi34scIQcOoDfVW1_ScipVw66EFS0KclJvONHTAAfXvcsydY5ztDvsIx358CWmfTG_sHFlaGjzymCJVqv53P8NvutLTH712F87XVHOzgGgoZHo3ySF6fefClmLBZA2B7rqWo9wZT_7EEOcEy6ognI8TYe3qJXhjbi4QftULJqPottSlmxzDYbwkX6RBchbvsqO31GLfsmar3qPSq-p5cWnglQZu-eZ6zJIdh390XslKAXF-uwjZGElxvKDdPh7PtzHsL0YkTI-jh8IOdxZGNGuoOOcXZ-tZ_Zvfff32ITaPUW5kwQgUIECdNM57hZPIOxhraWSK3CJ3DMe4N6Tr9hNdRV7CyzH2AWD3JdxHAPtrEtI3SYapalFSc6Xc7YpXVeX-IczzpdcmmEJY3j-yyLPTQ0yvvtgM4bpDeOYop3pTNAfK--L8_0oEQLc8qJ9uIS01z6gM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=kFuWpp96iOhuXyaOmZ2SyrC_B44rMOv7IdXvBY_8nW6uYsyct77qvYZqNjLdEiS3-wUruZw_zuespSmh5gw06_ut9IIs8uhKzUloBHwVowjjd00qB7sGFR7pn2tk8N1I6iupx3HWPqafYieLgvVh20HocW_msFWqN2azMResOAZNllJrlnVK1tFF9xlD50RFSkvfzp902tvS3L17jQIdB2V-KUIJNj0MM3FBLi34scIQcOoDfVW1_ScipVw66EFS0KclJvONHTAAfXvcsydY5ztDvsIx358CWmfTG_sHFlaGjzymCJVqv53P8NvutLTH712F87XVHOzgGgoZHo3ySF6fefClmLBZA2B7rqWo9wZT_7EEOcEy6ognI8TYe3qJXhjbi4QftULJqPottSlmxzDYbwkX6RBchbvsqO31GLfsmar3qPSq-p5cWnglQZu-eZ6zJIdh390XslKAXF-uwjZGElxvKDdPh7PtzHsL0YkTI-jh8IOdxZGNGuoOOcXZ-tZ_Zvfff32ITaPUW5kwQgUIECdNM57hZPIOxhraWSK3CJ3DMe4N6Tr9hNdRV7CyzH2AWD3JdxHAPtrEtI3SYapalFSc6Xc7YpXVeX-IczzpdcmmEJY3j-yyLPTQ0yvvtgM4bpDeOYop3pTNAfK--L8_0oEQLc8qJ9uIS01z6gM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=vCtBmwEIObiyZJhUNi6r2dauU_yXE1eEzDvj6RvCPTrF178HKPVmz4tbbzLBDOW-rBFUIaQ3XJVtEWM03Q6rg-YAN9o00QA2vsSnxWJeXIj9Uz5dR_PdmfTvs99IxwepNiaXAUupb-RHTJlCgDWmXH4TdkTbU6l3jBQwqpqtGn3qrux3cL12CFUsQHQ3KqNsCP006uXDo-DhqH3cNEKM6cTSAA0lpRCYKdhnxXgmJuRzuqRIcPiFs2Ba-9YStrf9yFwlUimH0-36sW3YX3d582Eud40M_blwK8W0r7HvYQUE-KFsnEXqiOn5afShShSD-BVpEeNDXv0Wc3oAgi8h1RZOkFmRU8Ttr6OvlFD8bMx3HlbdLPqpjpxAJtZpDXHKwqdYGbNtDM4COgUrDCnR_a3cNCoGS_wasbLcPlLhArVEOrT3gOycoG8eoAF_E0NSYeDPM3X-F80L_K1YYgPVIh1bsZmwxnbdO-pwqyVtwGQq33wy_K_emsdlhkZrj2WDdjMAP2LerDQO_6fG-L7NbGcjmFWVmsQf6ndK6zc0HpkhWr7iUpMDX9wugfLcEOrPwlhiibujxLDY7-Rfu6Y-oHGFhqlatdNs1J9W1mO9w5x5n_r6Y2jrbVb4CZnSaoqS4XHJPxHsioGDvIIVMxboMLbXcAG8WmqnydZMqZCHNDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=vCtBmwEIObiyZJhUNi6r2dauU_yXE1eEzDvj6RvCPTrF178HKPVmz4tbbzLBDOW-rBFUIaQ3XJVtEWM03Q6rg-YAN9o00QA2vsSnxWJeXIj9Uz5dR_PdmfTvs99IxwepNiaXAUupb-RHTJlCgDWmXH4TdkTbU6l3jBQwqpqtGn3qrux3cL12CFUsQHQ3KqNsCP006uXDo-DhqH3cNEKM6cTSAA0lpRCYKdhnxXgmJuRzuqRIcPiFs2Ba-9YStrf9yFwlUimH0-36sW3YX3d582Eud40M_blwK8W0r7HvYQUE-KFsnEXqiOn5afShShSD-BVpEeNDXv0Wc3oAgi8h1RZOkFmRU8Ttr6OvlFD8bMx3HlbdLPqpjpxAJtZpDXHKwqdYGbNtDM4COgUrDCnR_a3cNCoGS_wasbLcPlLhArVEOrT3gOycoG8eoAF_E0NSYeDPM3X-F80L_K1YYgPVIh1bsZmwxnbdO-pwqyVtwGQq33wy_K_emsdlhkZrj2WDdjMAP2LerDQO_6fG-L7NbGcjmFWVmsQf6ndK6zc0HpkhWr7iUpMDX9wugfLcEOrPwlhiibujxLDY7-Rfu6Y-oHGFhqlatdNs1J9W1mO9w5x5n_r6Y2jrbVb4CZnSaoqS4XHJPxHsioGDvIIVMxboMLbXcAG8WmqnydZMqZCHNDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=UlNu53HFmrcY1HfU2wpYSppljSkodqFsXOSdT661w8CkfA5SmRU1c11racj4SpSEvWA8BcnpivlW937T0De_1kqixH0GAWtUtFnsYiupj8E6-UUzJWpPESadZVpWamLGh7prEwR6yGgWfBRsMH3OwEwfXAC_rG68AmuEsKbF8N8rMrpjBloO9Htj3dOHK0FfZYEl294k9aTpY7_nD_PcrSa4t9xrh6tnDmHnBs7l0muuBGI890c7XCT7aSVnEEFxFfWoJpw-SiygoJA6UvKMdsvBbuEZaSS2KglUnL3e4EV3LiD1THZU9YOpcItrc7W1yLScJ9w-L9oc2iLHgrZPFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=UlNu53HFmrcY1HfU2wpYSppljSkodqFsXOSdT661w8CkfA5SmRU1c11racj4SpSEvWA8BcnpivlW937T0De_1kqixH0GAWtUtFnsYiupj8E6-UUzJWpPESadZVpWamLGh7prEwR6yGgWfBRsMH3OwEwfXAC_rG68AmuEsKbF8N8rMrpjBloO9Htj3dOHK0FfZYEl294k9aTpY7_nD_PcrSa4t9xrh6tnDmHnBs7l0muuBGI890c7XCT7aSVnEEFxFfWoJpw-SiygoJA6UvKMdsvBbuEZaSS2KglUnL3e4EV3LiD1THZU9YOpcItrc7W1yLScJ9w-L9oc2iLHgrZPFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2fE2-tr1Yd47CNar9JQ9K-EBH8livxnN9Ob7kJGmaAGexJ-QDJnhf11um-xyAHRuxs3kW_FhRwBJd4qKyzIE8FVuo7ZvMjKkTFjtlYd34cCA0zNvic9PyUWfOC2jqdgndPxNuAXf8waA3Nt3OUMFCmBoCl7JF1weeK65wvJJaaKjWB60vS9p87C2zlt4YXCKAE05zWI1Znc4B1OK3itBO2rNqgEaExa_JJgSNe8zvTAMKjIThl60DBog_yyFrpVJfm7ayq2ICLy21G-tXoSxJ3Cg-K0wAzRWvWOhXZeELlDkBXILZ6CrwZFxQb9xAU6AFxxEGNssYLZiazyo51Thg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=KvexchOmTtXQgN_VUv9ca8aP9TpRH6hhPfllGupwZbpd2PXG05q7YM79ajVFnFH9AjF5phU9YpMquLmqbVjLirgtBcdywEwp3JbdlT-kw1zciLn5l-SDfHu2U2fIlr_JCyDIL1JQeBi3oJz_TnnThg1WOyeoF8Jvj7BOrQoemnnmzVyXK4FsaszxHvo2LnisXkaSNBhrhab7UTN0WqGai2ZMZqa4Mhnvna0hR2Y8sOqa0ieQUL_qBTDZimQbtJ-xVeLp4O-FceAusHp9Zd1bBZxlutcJzuzOxzxaVLUbXrXxJHL0SxLq4a_-fv1kGPjr08sEQWtEm5jVKFh0ZTu8iG2Hf-QUmILs7SAaDb3KGpaQpKDDrMgB2l6gf0vsSiFUuS-YwWEW51vFIMgTDfq5PSggnBm3R0OB11bU_f_yaune1kgmXpgmfVvn6AZahSdDsKL-783utn_nkAxCL_9h38ujJNw-yWew6iUDzG5g-hSfWZDKOe3g7hX3BBv6uv7vGBA3BMmhuK5FEl3_UTtmmLkRuLGe2i6wxpmlpVku6jMx0m6z2hEFNdOI0l6D15jHm--F-NsByXTGscddC3xVtPsS_wBbSZ0XqlIofLK3HffOfOFwSdOfwD0AWy8PTl8Afw9EAS81acal_8G_sBosV6kOA2HGbo1nreWzafn8qyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=KvexchOmTtXQgN_VUv9ca8aP9TpRH6hhPfllGupwZbpd2PXG05q7YM79ajVFnFH9AjF5phU9YpMquLmqbVjLirgtBcdywEwp3JbdlT-kw1zciLn5l-SDfHu2U2fIlr_JCyDIL1JQeBi3oJz_TnnThg1WOyeoF8Jvj7BOrQoemnnmzVyXK4FsaszxHvo2LnisXkaSNBhrhab7UTN0WqGai2ZMZqa4Mhnvna0hR2Y8sOqa0ieQUL_qBTDZimQbtJ-xVeLp4O-FceAusHp9Zd1bBZxlutcJzuzOxzxaVLUbXrXxJHL0SxLq4a_-fv1kGPjr08sEQWtEm5jVKFh0ZTu8iG2Hf-QUmILs7SAaDb3KGpaQpKDDrMgB2l6gf0vsSiFUuS-YwWEW51vFIMgTDfq5PSggnBm3R0OB11bU_f_yaune1kgmXpgmfVvn6AZahSdDsKL-783utn_nkAxCL_9h38ujJNw-yWew6iUDzG5g-hSfWZDKOe3g7hX3BBv6uv7vGBA3BMmhuK5FEl3_UTtmmLkRuLGe2i6wxpmlpVku6jMx0m6z2hEFNdOI0l6D15jHm--F-NsByXTGscddC3xVtPsS_wBbSZ0XqlIofLK3HffOfOFwSdOfwD0AWy8PTl8Afw9EAS81acal_8G_sBosV6kOA2HGbo1nreWzafn8qyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=Hn5f084bR8z2OTdSJOzlKOOyBcxKtppvcogjRqCcROu9bidNLd1aRBssT5Ee4FwdctOGhG0hoN918DingywpZSE7J4XlxjI_Onsa9W6yRzDO2OoxcxqEdOgM6SAnhoFxyYwv5uHlLYlfyZqu2LPSfu1wFUTTKVAjiYAJGrbsWAGk9H_tiI2tZ0e0LsB_8QMzT1rOSJYviDSbIPCuZTsXxD13SzTpekib81vuvJoo_Hzan4-y0j1OxwtfDMb77_WxwA1bdazuCpm1wh2OuCteMIu8TJl3okDd0J_gU_ac3k-sV1ne1p065crJKOHcYdKaOyePsdh5ys2MKPIb2rqUWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=Hn5f084bR8z2OTdSJOzlKOOyBcxKtppvcogjRqCcROu9bidNLd1aRBssT5Ee4FwdctOGhG0hoN918DingywpZSE7J4XlxjI_Onsa9W6yRzDO2OoxcxqEdOgM6SAnhoFxyYwv5uHlLYlfyZqu2LPSfu1wFUTTKVAjiYAJGrbsWAGk9H_tiI2tZ0e0LsB_8QMzT1rOSJYviDSbIPCuZTsXxD13SzTpekib81vuvJoo_Hzan4-y0j1OxwtfDMb77_WxwA1bdazuCpm1wh2OuCteMIu8TJl3okDd0J_gU_ac3k-sV1ne1p065crJKOHcYdKaOyePsdh5ys2MKPIb2rqUWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBwc_DUlGtp_Z672ncNU-1JYJRKYA24bmxwd7QpFtDXcxBy9K-8I103lerjVfbkukd8O-awrGspPtmAerUBNMY6Joi2waaYY6wFyfJpBNdTGzGvn8fpC7GyEynclJyTKLZfjYvZp3whp4CsaBMbYBcTI0nv1hXRlasYEtJiTLRKAByxy6yfNQ93W1KD49yLWU-T8poLCvs01zuFWxN4JrkzgyYXtRQ7y4dad-M6EkNSi20TmlEfRV7_PJh7R9chNSnNyBVQeb42LETc4eRMsN69l5fqUGASLmMtU-uUXra5CRMjCVqoR0fwYKa8CndQCGNSgAasqzTTRnzge9mBOGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/couw9tpHoNO2EdNZLbRJCn5aQrQMNUUvn36kRoAPYyS7CdVSdiKKiwmtIj6-xtnCF-X1b4ULLDRYrEkoRf6TDOMSsRJXOD2B27GzckvDrEZP7VPAi3t9jQPwzVL21t6vijjSS3ufitywiWFw8tvGwEUOlh1WG2MbezXPgGJnEmFrd09ThSRNzOtzNB419roThR930-Dk80YIIJfHy_eFX8WVP2AGWUNyLiXBO2HAtXDkUq8mqVp5OEm07wTiMH26MCQn30JeIyLyNi1z4wmfvyp5oX8LtLcXY-vNk3g1R0iYryE0mGMBBPWlwmzgfo8MOoI8OdvBDIg9Tcm3SoCnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQctvpa-XhCzC95Gx2fklgRFigxdtUH5VNGWOAE25W57FNnShcLihjFTFgzFWoQQWdQNVvtJPZRQFEtrMtzDXQy3g4e87CMhT5Qogz4NVi82ig_V49s7p9fHDjtMpTsjOVP16FSvRwZISpEpquXPVXzOfJGZzmqEVSN81OWRGLIIrqhxRJjCOxKHckOgwVdW-GxGZ2jpr6BeTe6p6GdcVRMYb7QW4sF3gazvGcIn9ZrMo83Z9TxZLDWxRh6vpelEoB2fNQEK3ImxaLgd9yuK4RY2FK1W8Sdq29tf5Lnoqa1pRhrqPpQR0_ig82zg2-yjLI6OLf52UvpGBIY3Y713aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7Jpl_Esf2-FABbs1k1XdfasH-bS4qCUKyb6omfYIolNOSZAoSmawXjL2LraBDraknFvoijZjVxqz1ifxr_Zmc1B9UXv2dHpH2zD_yqfZfUgXnZSozVPBht1-Go_tqJEES5PxgjWuSi-sNj7xroNP8Eg5LkqmmGusdJCM5RvP5YK3SpZZAccjM0FzQAR2w8pjD988puhSeJv4fMe-3yYpxLgEBIjOXxqP2zjGxhQWQY6kt5HOYEjSVuINWhAcWcQnBU6kCGfucw_gOxBVryN6DyEp1nDNrWoq_1_QiBOq2zZFkn8L3BZMeWz8kp5AnPViFnv90G2CIHIpHzEeD4KpGKq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7Jpl_Esf2-FABbs1k1XdfasH-bS4qCUKyb6omfYIolNOSZAoSmawXjL2LraBDraknFvoijZjVxqz1ifxr_Zmc1B9UXv2dHpH2zD_yqfZfUgXnZSozVPBht1-Go_tqJEES5PxgjWuSi-sNj7xroNP8Eg5LkqmmGusdJCM5RvP5YK3SpZZAccjM0FzQAR2w8pjD988puhSeJv4fMe-3yYpxLgEBIjOXxqP2zjGxhQWQY6kt5HOYEjSVuINWhAcWcQnBU6kCGfucw_gOxBVryN6DyEp1nDNrWoq_1_QiBOq2zZFkn8L3BZMeWz8kp5AnPViFnv90G2CIHIpHzEeD4KpGKq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5eAdLdIOK_9VlCFFX08MlEVLAMj0N3oFt0Cul2UwB6Nqof6jLP2CsNREcvoDQcUF7GTr30hUtyQRsIS4ZM5YoCTrWQv8cZPARPcGQyofZ_NHKFUSDyfHRvHewSEw_OE8x_pyu5xA8dU6-A-1ZuFqKgzyDf4t4govkawizmgCGx8G4Q5_TNb4l5OgDMlZc3jVYq_M2mY80mURyiAKRkcR5mL4k56lXRpBbLU8vTotoIzgaKf9iW1qGY5GF6U7Dpna2Zo-mWpbaZ_HqXuWBKHCRRvfxnoeGQpwZ7lroQTZCP2kkwv_biWUJErtoMevVa9cCVxCGrHf6UEPPfYdCuFug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=NQkVc5Wuo-AZ2dFBdHU0Y0e4odEYVjoTBKH56eeeTw9bz0aR0Mn2yEfWOyZd4nHtYGq-nFQhGpOQB-50vQz2kL4VB7v2Png4FLnng5fiwuHQLbtgedZlruk1q7zsfHkb2cK3AsDT_jPm7SD0f3r6wzTAZJXsQQypAASWA2UezP3gdd7nEqoCPspALiJYdmjSc8Iu2mmqDnVELw0AqiHemQRVAkOmPtl66vUXF7_0G0xLiUMefzVMQ5egfnb9i3tarLBAEPD4C7e2wqyw4LS6LNwwBEmSGbf-NiaEG32WaVMxr7g8iNjdfk82BWwDk1N5VSRnczsk2oFb_s61Fuvi4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=NQkVc5Wuo-AZ2dFBdHU0Y0e4odEYVjoTBKH56eeeTw9bz0aR0Mn2yEfWOyZd4nHtYGq-nFQhGpOQB-50vQz2kL4VB7v2Png4FLnng5fiwuHQLbtgedZlruk1q7zsfHkb2cK3AsDT_jPm7SD0f3r6wzTAZJXsQQypAASWA2UezP3gdd7nEqoCPspALiJYdmjSc8Iu2mmqDnVELw0AqiHemQRVAkOmPtl66vUXF7_0G0xLiUMefzVMQ5egfnb9i3tarLBAEPD4C7e2wqyw4LS6LNwwBEmSGbf-NiaEG32WaVMxr7g8iNjdfk82BWwDk1N5VSRnczsk2oFb_s61Fuvi4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=ruYhiVX1fNXaJW_nWNS4CLDxjDBD_BMP6llcYNENCQXXjMhp2QT0I8G82yRLtlIxZ2T6Vt3Eosy0dgCm_UDox7YTx0ENOk62CCdQNC2ZHkdaPa10i6kGbO2Z4kD6MjCVzJXs1ro40Se4v3RxUsUTisgr6FUsyWDuhgmH54fKQdZN2kOSayRY0jS1hsq9JJ-udjxjUQaIVlK5YGqk1vVGeyst8QOJVIw6WTlX-6pG_0_rE0Eq2LrUDvJ7zoJbn7BKz5Gj7uCUPcpA8rxm7uLssLNaHTL0tadmGwP9jYdig_XtK5qMtUQ5Oq-0kpEeX3aEeFx_48RwzNZiooEUI7OxGR3P54u0Z5aC9PvFwc0WU_I9453YLodeGn1ZV18Nd2gTOrHAZ0lqGsdXyBspDPUzctK3dJqfOFy2Y87We0hK2uEgXKIGA0XB22_yWO4dkBdiY2VJws9q7t0LdnRMhseeEea6aSpNJEqAPUIskgamnO592tikVblyp8WbuXTs1w3B48vBmo7AGcV0VBmCiJlBFV2iPGJlox9J0BiFI_cRsuzCELCUBhaziqI6QhTkdkEQfk4CT0-7xW9ba1GyUTIANwLiaHW-_8f4icmtVEakNYz5JFCm2G7QVddOioo5NI3HVebWCZYgfZr1pUUhu-IMNK5b80kR0yf8jHNpJVsPWjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=ruYhiVX1fNXaJW_nWNS4CLDxjDBD_BMP6llcYNENCQXXjMhp2QT0I8G82yRLtlIxZ2T6Vt3Eosy0dgCm_UDox7YTx0ENOk62CCdQNC2ZHkdaPa10i6kGbO2Z4kD6MjCVzJXs1ro40Se4v3RxUsUTisgr6FUsyWDuhgmH54fKQdZN2kOSayRY0jS1hsq9JJ-udjxjUQaIVlK5YGqk1vVGeyst8QOJVIw6WTlX-6pG_0_rE0Eq2LrUDvJ7zoJbn7BKz5Gj7uCUPcpA8rxm7uLssLNaHTL0tadmGwP9jYdig_XtK5qMtUQ5Oq-0kpEeX3aEeFx_48RwzNZiooEUI7OxGR3P54u0Z5aC9PvFwc0WU_I9453YLodeGn1ZV18Nd2gTOrHAZ0lqGsdXyBspDPUzctK3dJqfOFy2Y87We0hK2uEgXKIGA0XB22_yWO4dkBdiY2VJws9q7t0LdnRMhseeEea6aSpNJEqAPUIskgamnO592tikVblyp8WbuXTs1w3B48vBmo7AGcV0VBmCiJlBFV2iPGJlox9J0BiFI_cRsuzCELCUBhaziqI6QhTkdkEQfk4CT0-7xW9ba1GyUTIANwLiaHW-_8f4icmtVEakNYz5JFCm2G7QVddOioo5NI3HVebWCZYgfZr1pUUhu-IMNK5b80kR0yf8jHNpJVsPWjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=iBMg9Q_j9ZVdqra5KXQHuuQEs4wjodoAGhh1yAkpzguuVQp9NcBIK8-PtoS4zOqqP-uEaSFTIH3H1A-2ZKK6ALLcDTKIwrwNEWH4MLfAxBVYxUjAfYIYCbRTHa9i5NvOGWZLtzmX8Xk2cGn3UQErZra-Nr0i4HqELESZRiLFqOPt2oVJFkEilKFjOwLv8pYEdyxyzLrUN-6H_iP99ZvHZoae3rrjpCYe1rwOssyDfxdj0CQfKkRK-_v3fBeK9X2WH4GYjkQTZUF0_jmw9ezhefukA42pl9D3jTni7P7muC2uLAJd1TGlEF4H86Sbrur9p3yHA8NLK6zGIsMgEoB5gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=iBMg9Q_j9ZVdqra5KXQHuuQEs4wjodoAGhh1yAkpzguuVQp9NcBIK8-PtoS4zOqqP-uEaSFTIH3H1A-2ZKK6ALLcDTKIwrwNEWH4MLfAxBVYxUjAfYIYCbRTHa9i5NvOGWZLtzmX8Xk2cGn3UQErZra-Nr0i4HqELESZRiLFqOPt2oVJFkEilKFjOwLv8pYEdyxyzLrUN-6H_iP99ZvHZoae3rrjpCYe1rwOssyDfxdj0CQfKkRK-_v3fBeK9X2WH4GYjkQTZUF0_jmw9ezhefukA42pl9D3jTni7P7muC2uLAJd1TGlEF4H86Sbrur9p3yHA8NLK6zGIsMgEoB5gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMzZ06kfei87xcYD5Z3cRhIapbGTozbrgANXGYNuhVjcsXpVPqpjSFWWsxW12_4ATjci-8kAmVrNGb92nDy0F_VlzDEoo-2290hwdcEJBCf0KCAgA2m0_YZ_7lgbRKDPTkp_AI0R32be43QEi_s4_bETbKumWwt6VP3mE-dF2iO0YVc9zI-4bAHXuHjeDXC7yCbQjdjRszVKrL0zcygNSEz0OzOy8a2CNT78narD9y1Rg56_jvrq_c2cfaYK4LHYqimcM5uNloAPY_elS-KP9ziEyDhMh2BEiaSup2dicPOhzNJoZzJXkxGLtyUc1CV3anaASK3myUVgnmV_iKVjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=gtMRQNzYR1ITF0znX4dsw1wQRC_W05lDMjlXkbwPi1ajW95daQfdpteHF3WoOGDu6dYHm3mvLjK919-WPqlOzd6pfBDKdGQsYeo0M4xyKdgkw15T56Gti3UDdy2EzmqBFmSNhouOEu7lMRuM2n57-QlTyCoV7fsQB4_-74nexawXrRYQbeX68vybKIFsoFBGa6VRUAJZ8qzbMeiY9h5GMWBwra--6PYArBS3FpP6R3Z3ANvClIOf8GppANa2VfbsggctLpR-RgQPM7DgJCk5z8SrfTfBiHjYG0d7o7eaByPxJnG7KQTD5rBioIypZuqaJHiIiYPypmyf5LAvP6NVliVFP8quiGyCYZIsptjb4aDdhyGmRDCjDiCNAmzrpEzNBXApbjJMvBt9re5nUBTI4wPGJyzJVHsJsetz9x5HkWvL7XTZ3F3W2OGmPtvHbyLMWMFeq8XwOta_lTT5oI9xVvX3qbXyLvRFseXzE_8o8OpiAvjUu8BbOOmDIDkQACgDiWjODmYJk9D2Sg2_uGwlVf-5C25d8VaEF4xd-Wr1IjGTz7Fvx55H4fhw3cgJdfePZFtlI2Szr65-L3W3Q6t_M6mZIKQMS7JhfmMC3dra94c1267WOpAYpQl3RZ2RevN-Ql4UoQYfNZkqkK7UjipYYHHgkqpf2bdT5BXekNx-u5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=gtMRQNzYR1ITF0znX4dsw1wQRC_W05lDMjlXkbwPi1ajW95daQfdpteHF3WoOGDu6dYHm3mvLjK919-WPqlOzd6pfBDKdGQsYeo0M4xyKdgkw15T56Gti3UDdy2EzmqBFmSNhouOEu7lMRuM2n57-QlTyCoV7fsQB4_-74nexawXrRYQbeX68vybKIFsoFBGa6VRUAJZ8qzbMeiY9h5GMWBwra--6PYArBS3FpP6R3Z3ANvClIOf8GppANa2VfbsggctLpR-RgQPM7DgJCk5z8SrfTfBiHjYG0d7o7eaByPxJnG7KQTD5rBioIypZuqaJHiIiYPypmyf5LAvP6NVliVFP8quiGyCYZIsptjb4aDdhyGmRDCjDiCNAmzrpEzNBXApbjJMvBt9re5nUBTI4wPGJyzJVHsJsetz9x5HkWvL7XTZ3F3W2OGmPtvHbyLMWMFeq8XwOta_lTT5oI9xVvX3qbXyLvRFseXzE_8o8OpiAvjUu8BbOOmDIDkQACgDiWjODmYJk9D2Sg2_uGwlVf-5C25d8VaEF4xd-Wr1IjGTz7Fvx55H4fhw3cgJdfePZFtlI2Szr65-L3W3Q6t_M6mZIKQMS7JhfmMC3dra94c1267WOpAYpQl3RZ2RevN-Ql4UoQYfNZkqkK7UjipYYHHgkqpf2bdT5BXekNx-u5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=OGmZmGpPG0_aAmY1i9iKKknJW728hIgvpzaNMSPcHTkdr1JS1DzZZI7WWjiofHrtsZaODlBJ0pwYnlKpdhGqBHQ8SAyEItYQ9Kh79dZuWZ6C6aAfmmnjLWIvvVSPbqnr11l5ANFW8gexF12kgvLc9K_8XIZbDGAdYTbjCfMc3H9tMgbLepwkbggxJ6qicZdfhwrIWtbXT9fmtEPrHIWti4BsCQVG0M9Eu6tzIjEXu0sPNJJ0ky-snSjcf95vqwZXyjdXbRHrk2zr-ZL47-QBaPBWPyfW9zbbQrPpwyZ8OqtqZ1_wNTpjuC9cZ8an1GD5RXrzWd76AxrERSxpaacJmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=OGmZmGpPG0_aAmY1i9iKKknJW728hIgvpzaNMSPcHTkdr1JS1DzZZI7WWjiofHrtsZaODlBJ0pwYnlKpdhGqBHQ8SAyEItYQ9Kh79dZuWZ6C6aAfmmnjLWIvvVSPbqnr11l5ANFW8gexF12kgvLc9K_8XIZbDGAdYTbjCfMc3H9tMgbLepwkbggxJ6qicZdfhwrIWtbXT9fmtEPrHIWti4BsCQVG0M9Eu6tzIjEXu0sPNJJ0ky-snSjcf95vqwZXyjdXbRHrk2zr-ZL47-QBaPBWPyfW9zbbQrPpwyZ8OqtqZ1_wNTpjuC9cZ8an1GD5RXrzWd76AxrERSxpaacJmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=rdcKFuO90HPZSPDhE2R6_VOWE1QrFFqfH0hjNx8m1qFR8c67WdEHEBv5BdOBPdSL7OfSexRhyKw6UK50ncdHH51UkzWLLkVagVQDdbgYgG-QULE555xoiEgBG420Uuay-9B6dGV_2OJSCdukCDJdG6LHkbL4i0UhrvwA__ks5xLthLae0KuUnuZij_OWRzvjGH2gDh8GYGdsXZjS4lakXePCtwSHuZlUn0r2tMdtysu9nb-ZtOUiwOkW-9CQVgNCQcZjGAgtP99i1RIFzRRjRb-9qw4rtMQe1dpy665fsUiy29JohXp0pSVX-CyhKX9w6iGQF_RtYaghViEMns5A8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=rdcKFuO90HPZSPDhE2R6_VOWE1QrFFqfH0hjNx8m1qFR8c67WdEHEBv5BdOBPdSL7OfSexRhyKw6UK50ncdHH51UkzWLLkVagVQDdbgYgG-QULE555xoiEgBG420Uuay-9B6dGV_2OJSCdukCDJdG6LHkbL4i0UhrvwA__ks5xLthLae0KuUnuZij_OWRzvjGH2gDh8GYGdsXZjS4lakXePCtwSHuZlUn0r2tMdtysu9nb-ZtOUiwOkW-9CQVgNCQcZjGAgtP99i1RIFzRRjRb-9qw4rtMQe1dpy665fsUiy29JohXp0pSVX-CyhKX9w6iGQF_RtYaghViEMns5A8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly-Xa_Y5UR94a6XQc89_rJUwvOKhPNmSeZLgfiQ9dIRuI4vQo_F8Nx-xy-OT_zziG4wEHjtL1M7BuzMQ3lRf_UFpg_P-_ehL5E44d_HEgNebdTICk7gwjOmy6VNUgJxmSYZI1MjuKatoxdUHFIiTGXdcdMCy4luT56adHL7tL8BAtgh8FAhxEVhjMLNyjDKQiLD4u4dLUphm_IMu_7ujQjxvdbpg8Mr7l0rA9HdbPENguUdfrEeNXdcfZu21TAndjqwOik15uk3-E9wrEl6O34AX2P8AGmyp6p-tTsVzEHi1f2Qmc7lW7vB02n5A5uQ37q3WqLeXi7GpPYyCfs-eoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=AmzwbMhjq7MowUPQ10llKSBUngwbZV0Qatv1dDeOCSRXkK3yHAD_uIjTQxSIC-G7vWztVAPU-agz7k1ZeHppMbyInlj-JUAR6JiOiSkBk6rH_KVf0qH39BmRSGNX5Potd61yOXRj8AepJ19973cc6axGlvLSoPy8CP4Bv7AhjUbQox2oiCEEHwo-eo8aSVSngD3VyrTQWJ7dWYqmGLEDDJznGqBaFVVYjocmBKp2UG2Z5UjwO_R3h96BwFHBMqEHHxmuQcUK7MXt5E6xSomMjLdIiXnM6L7w9YO1_KEJF6lj38d3x_38dWrBdA3H2RFRQ_JsIejyqAMi69AwxeH6Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=AmzwbMhjq7MowUPQ10llKSBUngwbZV0Qatv1dDeOCSRXkK3yHAD_uIjTQxSIC-G7vWztVAPU-agz7k1ZeHppMbyInlj-JUAR6JiOiSkBk6rH_KVf0qH39BmRSGNX5Potd61yOXRj8AepJ19973cc6axGlvLSoPy8CP4Bv7AhjUbQox2oiCEEHwo-eo8aSVSngD3VyrTQWJ7dWYqmGLEDDJznGqBaFVVYjocmBKp2UG2Z5UjwO_R3h96BwFHBMqEHHxmuQcUK7MXt5E6xSomMjLdIiXnM6L7w9YO1_KEJF6lj38d3x_38dWrBdA3H2RFRQ_JsIejyqAMi69AwxeH6Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlVg3OY0PpRQLHPVkjLksSrff2uuZtBrczb66sq08vVr6eq4jx1bZdCNMP9jOR7hBoBSF9b3uHyeBY-YrA40QvvtE2ob98nTeolrzCnMwZOfmRyNMs88uL9Wy8lEGuk9DITQvVDv3xq3qFvwSX4qsx_qp6xYcWnIkjzA648wB7Km58NoABw42T3o2gnBO0HJJYZtQdcaETgCoJbk-q0Atdd31hGJ_svkSJF6ScxZR76Ha7TcdPahndX5L7Y0rmNL0qbIGIC0NuyNkbplkkl55NR2T00Jr7yfY5b2vw6-rOjjiyqqgabCpnp1gEXtOj1AzIGjh6GUUL2uIF-nep-MQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=Sf3BSp2XgUJrarh_FJePomHLDwUYEQM2ceTlXLM9Qj56s7abk0WE3GT9Ee93lHI77K9yjp1G5JshKkMbE2peXQjBk3jmrJYsylMPuhmcguKAyfWF9OMY2rH8d-e3h9JKwnhsjYkq5GS9z2b4VHvxHQVw0Mu2K-lgyvbqtI_hR3yewlMnRqej71B2yLp-yRQJU8iYasPFkvV4AqeKXuxKU9h8GaV5mFd0HVpna4rZZxnf5_6eZBGUmOkEuJAT5kFFJdX9R-c3aA7emj4UckYZEpX-9A26m6Uy4SKhy2AxkKqaKAv9lMb1ToRY0mXGQAsDdmWbvtVAWxyHmdpph3PwRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=Sf3BSp2XgUJrarh_FJePomHLDwUYEQM2ceTlXLM9Qj56s7abk0WE3GT9Ee93lHI77K9yjp1G5JshKkMbE2peXQjBk3jmrJYsylMPuhmcguKAyfWF9OMY2rH8d-e3h9JKwnhsjYkq5GS9z2b4VHvxHQVw0Mu2K-lgyvbqtI_hR3yewlMnRqej71B2yLp-yRQJU8iYasPFkvV4AqeKXuxKU9h8GaV5mFd0HVpna4rZZxnf5_6eZBGUmOkEuJAT5kFFJdX9R-c3aA7emj4UckYZEpX-9A26m6Uy4SKhy2AxkKqaKAv9lMb1ToRY0mXGQAsDdmWbvtVAWxyHmdpph3PwRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDwr81IDiMS6cJunKfc0fL5jRJgF3AVusqih_p84CxCG5Qg_pfy7l_J6ubPXeHvL6zE7IsysgkIF9KqzMJm-G53bWe2eNg-W6s1UokOYo1IevFdrd1miBZjAwyPgHwX447BcwZ2YS9UcqJglwAauFaJOZYQj4oqWee1tyBJFa80rvMy3nyjOiLvWymPJ_cQZBpEDyJAmAv2ZFqvHWW4MGiR78fFf6VBeYcejyNhlUlM2EqLpIAWCC0ZdM4F5qk0yqmriixrlTugCnzBfW68k5XfTgQnUs4e5-wPijnqJxB-8_T-cFTF_w3BSe9fbcRSTC4SiX5j_j-2OOIKtn23-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=AkFsdhmMAwsISQ_zDHORi825yBuODfIXNSThQK1GRHoAftzDZA83CIt0AVe7w74ulaDosBcWgfTMEy55uaMQpZFnWXj7Z0WtChGYExa_PEaB1LZZPZaJFucI9XRst_xcsXWBGsR_nXUy-RBY-oSecRSFIqUZibriDSQJvRsjUWCHF40MHFR-9tEBkH9bllfex-dMrd4juivouDt2rpRKBbJJ4HSzqIoPQflSWN5fDiW6SiTbFokYuME1AriFsBWHaDU2tfS6zdbxgBduFtiFcUxW3TE2l-RL4fJokJ1nyjqwE_KRKHgjm1x8et34qfaeR9EdD1_mK0AF_SeH7AKP_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=AkFsdhmMAwsISQ_zDHORi825yBuODfIXNSThQK1GRHoAftzDZA83CIt0AVe7w74ulaDosBcWgfTMEy55uaMQpZFnWXj7Z0WtChGYExa_PEaB1LZZPZaJFucI9XRst_xcsXWBGsR_nXUy-RBY-oSecRSFIqUZibriDSQJvRsjUWCHF40MHFR-9tEBkH9bllfex-dMrd4juivouDt2rpRKBbJJ4HSzqIoPQflSWN5fDiW6SiTbFokYuME1AriFsBWHaDU2tfS6zdbxgBduFtiFcUxW3TE2l-RL4fJokJ1nyjqwE_KRKHgjm1x8et34qfaeR9EdD1_mK0AF_SeH7AKP_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=QWdp2_iYke28m9OCt8lfVQRn0011LVJPPUqTN-aUVg-n_Sok4DifSn5Xucu-XxoJnn_q4MXg6_RUNfA0m80aJwAR8yUCzHJrkCpgabXtIPzbv6J5jTk6728ay8UEyJ9OM42N7cmPVjFPE8-ysopxOGix15kqfWGJxI5tb2ygL-jBhzB6ksuOb-HGNmQfdsEq0stDDSTmGgDtbr9emN6k_es6kcM7FPWnX46qQR0ITZjyGR0_Ns3VpQUkdYmZ-wP2NI-Rh9y2QtVIUCilWWfyWZiFCPvgR4-N_NURxkwU49gN2LrDFXTV9JC_pxkApriXJaOZ0HmtHDB4kwGbVdBI_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=QWdp2_iYke28m9OCt8lfVQRn0011LVJPPUqTN-aUVg-n_Sok4DifSn5Xucu-XxoJnn_q4MXg6_RUNfA0m80aJwAR8yUCzHJrkCpgabXtIPzbv6J5jTk6728ay8UEyJ9OM42N7cmPVjFPE8-ysopxOGix15kqfWGJxI5tb2ygL-jBhzB6ksuOb-HGNmQfdsEq0stDDSTmGgDtbr9emN6k_es6kcM7FPWnX46qQR0ITZjyGR0_Ns3VpQUkdYmZ-wP2NI-Rh9y2QtVIUCilWWfyWZiFCPvgR4-N_NURxkwU49gN2LrDFXTV9JC_pxkApriXJaOZ0HmtHDB4kwGbVdBI_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U260wXeawImJXNdKPU93k2WBobkSCfVsT132AfSF1RbO4k0qJ8wNmhD8s0HtBSDZa9IQkxMO-Rw4Lea-DDV0YzOna2FI6ssQiyvWSOBdAqjGTXb0Zde_99hW6KSN8ggHjI96RfO6HjiDHAYqNRQxATF-Z8PAL-M2s8-yG-vwchqplmS3zaVObp1AWjLxijMgafi-n1IufhAxHQSnhsm5uY6UCxmp7-fgPTSdSRpQfdCdLJenJZ1NGoolWWYTMYothLT6_BJJiFpNqr8EnS6rYpjT_8M-OLbnLPg8zzOjM4pttO-PkU8qlT--JkUf8Vu-t_u94bGoMKFPPNGlQ49Dxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oay2qq4MTaNRFoJYkly-qlSgbyN-pHRLYPKOfHExb3OoxE7x8XltApLxUKspqQ5HK1tEyzZV-qsWNCwB0bR-YpDJ69h-9f1wMc1dsK1PyURzxu5fjSgzxqiJ9XZ1-Y0HTNGUHhdg3w-nJIx3AEAR_at9wx4_gxh_2GUOmQZhBwe_E6QHuQdiM9YcMGcVZFzraLorc_j2-kPJ1aaIJxt6VvV_Oa352-6Urvd9JzznMRxDYP5OlLr4s6B5c1Kxg9ethxjqn7gq17CXifoLDVfx7OAYEUJXZd-v35ypgM-HZKN11QbQqKVApvXyrUneSKf5uhcYXUvua8Q8iUHpqJk825eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oay2qq4MTaNRFoJYkly-qlSgbyN-pHRLYPKOfHExb3OoxE7x8XltApLxUKspqQ5HK1tEyzZV-qsWNCwB0bR-YpDJ69h-9f1wMc1dsK1PyURzxu5fjSgzxqiJ9XZ1-Y0HTNGUHhdg3w-nJIx3AEAR_at9wx4_gxh_2GUOmQZhBwe_E6QHuQdiM9YcMGcVZFzraLorc_j2-kPJ1aaIJxt6VvV_Oa352-6Urvd9JzznMRxDYP5OlLr4s6B5c1Kxg9ethxjqn7gq17CXifoLDVfx7OAYEUJXZd-v35ypgM-HZKN11QbQqKVApvXyrUneSKf5uhcYXUvua8Q8iUHpqJk825eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=PoSfdsmLqp4SHRQeW7s-DOZnO87iAsQszHKsslIKx50Ipoa14apVU_Ki5E8i3WlLFKo743_IOexOczuHGvj9yQ61gDNbFABEQvtNCEfCRtClTUiov628y0zkxTmjXjEPsavoDdkU_aumNKVDzw3ts8HgSZrPiNZBRlGVPEN0KmlS51690JZgbUki6Ivuk80Uza9ZDrLHpqGgMtgxz3bacWGa6f1TJIj4R49Dj4tB5htqH0z-Dpg_bf5dAR7OqS8NK_h2QE_ZmGR8_20fAcjfTw5wUXT9buNDmCa0Vb1DBvZoj__A-YfQishaas43siDDFAkXIXne8Uce9oloDpv7hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=PoSfdsmLqp4SHRQeW7s-DOZnO87iAsQszHKsslIKx50Ipoa14apVU_Ki5E8i3WlLFKo743_IOexOczuHGvj9yQ61gDNbFABEQvtNCEfCRtClTUiov628y0zkxTmjXjEPsavoDdkU_aumNKVDzw3ts8HgSZrPiNZBRlGVPEN0KmlS51690JZgbUki6Ivuk80Uza9ZDrLHpqGgMtgxz3bacWGa6f1TJIj4R49Dj4tB5htqH0z-Dpg_bf5dAR7OqS8NK_h2QE_ZmGR8_20fAcjfTw5wUXT9buNDmCa0Vb1DBvZoj__A-YfQishaas43siDDFAkXIXne8Uce9oloDpv7hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=BKnmeChbvX4CGjODVdYkrBRuHIdSiSBQuJ2h4rygvfybxx16M1cKR6sYRVzpI3QE92vpCkGL6K4ojSGpAT_JoxlpuHjZqzhBroZrq7rfAqMGVfCSyV0Q0k7XkCnuNaH-YsIfjVtmM7wPTxq-yqY0VVHL5JDC_dtfmWaOCubSFyrVFcXkQAFCxV4Or229PRb767y0EAb0n63N9pzjca2r_f6XV2Nsz_Um9o8TiGAB-6Ri5aXNm8vt65KeXDq6LSUo-Latu0sce8dQ_MEq5FKvz0P2ZkpBO6xor4WLZNWhxT-OXzmW-XTPQ4m9g_th1gr77OHlafHz48FKmFUe7flu4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=BKnmeChbvX4CGjODVdYkrBRuHIdSiSBQuJ2h4rygvfybxx16M1cKR6sYRVzpI3QE92vpCkGL6K4ojSGpAT_JoxlpuHjZqzhBroZrq7rfAqMGVfCSyV0Q0k7XkCnuNaH-YsIfjVtmM7wPTxq-yqY0VVHL5JDC_dtfmWaOCubSFyrVFcXkQAFCxV4Or229PRb767y0EAb0n63N9pzjca2r_f6XV2Nsz_Um9o8TiGAB-6Ri5aXNm8vt65KeXDq6LSUo-Latu0sce8dQ_MEq5FKvz0P2ZkpBO6xor4WLZNWhxT-OXzmW-XTPQ4m9g_th1gr77OHlafHz48FKmFUe7flu4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJYwShR2RZ9aLPUpMOLr9sfgZUJV_UXpPqUWzyfJbHzWBcIalcVbYqHePmqvauqvi-uusCOWWk7lCGzPDqZYGmMOIm1h77HplZPMBOhwFR6OWWzbI9oedEqhmL-4DJUklYsFLCw8gveUYZnxdLVcOW7yi1RkF1BX5tQXPKdTED6VH8xTD8POmcT02bAKL2diHb47jsAmcd9rXodYfdt4qGxMs7LDymlVuP8s1Hdfc5JDgGyP6vIfE_cdRzpF0sr2Db-lWiiGG9sst-GgotPipLhWJLnuU0y9bfxU9CSfYfdRRK0fMKD9VNAlBCDvKYtjncPPYKyQ9iFzrLtS2Nth8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=LrH_bYiHt5Isd_od1GV_1va3xEyS5mNrExP1nLmU1k0CuYLLC5jLsQag4PQNaGMHSNMB4T4ibnyJFnDD8-4Ym887szruSGL7OIBxPDx6Da4d7UAQY9ru1WbfiUQ1gjTPLtu0-quBjMbDuHXszUX1t8tmk57Vck1UDUHLPlmPAaYAgn9Vdw-rIYku4nu7wiPyxIelI0erIX4ZcKD7QX5rA2rrD90OuCg8p2VlRiiAAanKAErAtMdzBRQRYIVtXxhPjxKblyMN6P7sbkyYDEoe6X_j1CmFA8humj5tA20TqvExgxfghCDGnOHB5CStuWpihwN34dwAaQtTdI7CVT8E7iEoVWlkLWU9Lyslt7UkHUbYXNSYWGTn2htfsUqOLEhP7ec-c5xg3KF3MNv8FU-wjDt_8RXmU8MpSH6LLdrLEoqYL7qRGY-Z8PAQK52RVIbajqlQKLtwCuHMGMUqBMqOWajU9Aj9_CjjJODEY8EezpE9QUS0x83Vfj-eyc4rP7LxwbyYt-erp9TBcF3_xjyJqNJLxOM55hg_Zq7ovTwDAf5l6wL566r24gWou0iER5s_Z9Di7ijkBuNuS648zAfKC7EzCs5CNeDu6mGkBLDpWT0Pu9AOpmic5GDwfXupzQLqao3nZUlmG9Ar3CPBvgNPsIEXfEpVFEFpalE8nIIFCpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=LrH_bYiHt5Isd_od1GV_1va3xEyS5mNrExP1nLmU1k0CuYLLC5jLsQag4PQNaGMHSNMB4T4ibnyJFnDD8-4Ym887szruSGL7OIBxPDx6Da4d7UAQY9ru1WbfiUQ1gjTPLtu0-quBjMbDuHXszUX1t8tmk57Vck1UDUHLPlmPAaYAgn9Vdw-rIYku4nu7wiPyxIelI0erIX4ZcKD7QX5rA2rrD90OuCg8p2VlRiiAAanKAErAtMdzBRQRYIVtXxhPjxKblyMN6P7sbkyYDEoe6X_j1CmFA8humj5tA20TqvExgxfghCDGnOHB5CStuWpihwN34dwAaQtTdI7CVT8E7iEoVWlkLWU9Lyslt7UkHUbYXNSYWGTn2htfsUqOLEhP7ec-c5xg3KF3MNv8FU-wjDt_8RXmU8MpSH6LLdrLEoqYL7qRGY-Z8PAQK52RVIbajqlQKLtwCuHMGMUqBMqOWajU9Aj9_CjjJODEY8EezpE9QUS0x83Vfj-eyc4rP7LxwbyYt-erp9TBcF3_xjyJqNJLxOM55hg_Zq7ovTwDAf5l6wL566r24gWou0iER5s_Z9Di7ijkBuNuS648zAfKC7EzCs5CNeDu6mGkBLDpWT0Pu9AOpmic5GDwfXupzQLqao3nZUlmG9Ar3CPBvgNPsIEXfEpVFEFpalE8nIIFCpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWYxCmbMsIOLrMRa8oCVhsOjejh6fvAoxdP4js5MXJ07tR0DWz99e3CbEBIx02DJyapzGf0zoHFJRQ6qdVyUWd_up-t77vp3OSujWaspfQjlOP2n0xSu-hLfF4EahoVwW-NgSPHo2pb3E6QHHXMzu2YUKze_zpgGVOEJRsQbrGSYtG_G2CQ-ITQ0E9Q8Ok1RMM_bdQcL1Kcwkb7Vb0TjL48T6xE_Mqs1ZGBelBCt3AyMfvAtzUGVe4OsiPNconph5xJgZ4hz6gWNtuiMZZLN8Afrm3yDNQEUREXK2Kb3M1JmTftVvVcgE4G7xpsB86LY6KXetH3Gq0LX2trwDL397w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=AbRR4wuTiQSnfAjL0uPJWxENKG4pWgTD199ru7GYVwaV051XDWjQ-wVHiHshINqJpNuE4cBlKyEbu0DZ1AZ4zNYV98dsLtr27HFAktzyUPg2LrqsKNzCTttlns91J7sOl9EKRYU4zNDz2CrKNuRSWinZWuSlabXepAWMKPlhA3NykkswsCLSdN6EiIb65C0fnTzaQD1DH5M4_rlL5crcGn7fVqf9Fh8LcsuBO5WEPYFkb6hbopfa4m4Lk3Ctpv6Ru_ahiD0rgL27M5Lf8P1t6YKYhrZ55l_UUo3aiyl48DurwgjeaNHpOeSMWHzmjc1mP2RdTQDc_gmYlJlOXuGDug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=AbRR4wuTiQSnfAjL0uPJWxENKG4pWgTD199ru7GYVwaV051XDWjQ-wVHiHshINqJpNuE4cBlKyEbu0DZ1AZ4zNYV98dsLtr27HFAktzyUPg2LrqsKNzCTttlns91J7sOl9EKRYU4zNDz2CrKNuRSWinZWuSlabXepAWMKPlhA3NykkswsCLSdN6EiIb65C0fnTzaQD1DH5M4_rlL5crcGn7fVqf9Fh8LcsuBO5WEPYFkb6hbopfa4m4Lk3Ctpv6Ru_ahiD0rgL27M5Lf8P1t6YKYhrZ55l_UUo3aiyl48DurwgjeaNHpOeSMWHzmjc1mP2RdTQDc_gmYlJlOXuGDug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVgKTj3wmecsxS6m8Rv74uBe-HVArPAu9K1D15rfCHWSAA2cKcq2Jv7bBQ-OtBzC_bkvFDSQ9sLognwCnTGpfW0Cc6KNp4TpsZuuAN6rvGvlhHOnqppb-X8P4-GLofBowuwTwSY-HYIbrlQj6WMalTogmrv8LsCh81uLTwQwK71hm5b1z8OzvEDLwOHTpblYyNoNA02ker2MxceIxxCdVSJSDIrI7l272QPfPHoPWTcpK381jqU9jAhDCyDNCvW8Ow4kRKhEM4mEgjy8maadAWeyuOMLFxhGUITgPuiuywDzzMfp2Khzdq7HO5j92oOTm6C1UGFCcc1LkNvudi2uxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sADhxmTAUpLkZwh1taqYkZ3TyInt2-gfH2eVKJvjPQYpqruFJ9nJC6bFVkQQvYdlsPh1gK296bJgfZEQKS6KMYjY-NAsgo_2D7F8ZhmfVzigU1gI6BqQfeuCs7Q9Pcs6VoNW5ahk5EMB8HZLn4vU6kQgQ7zCteyOIA9_16eq6htifWOhgwroUTf8aKu2R4lxlitxIC6udceauCtmABkAt4hxScN_LDVYnjJZ5QLrVajGcH3Fj9YhTkMZyex5z1ZPw5PjGGopGU1TG4uXtRe-v1qFfHFzjuG_k6KQLlzbXEhYhBB_RvNf3fwzhSD_1KXNYEWQrTKXIUfjChHEZMUGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAJXUgcQXJhSxG0_cfIuLnqcpRacIblv4IRdWAiewi6bFjRpA-8n6dgPbeJA6ZKf8PLmzyifRhSXhlaGczxwfh8bsdlBmJj7Zq6eKPAKMFldPgLcKgVGnNiEyCj6o5rsk40hXCOMZXX8Lsdc9iSxInbwFXmR7CicJavxX1stTYlpcBresKGERI7OzNeENE3lk-A2BbWTil7oaEpN8u00v2gjgr4ACFm7ht-UcNpCSMcHBBf-2vX3ORp5Ogl4LATEaBJiTadsLX9fV32EWO3Ujylv-XGow0piNHzCU3KPkSK3Yv7feYKBEEuDtcml_9Q2Plp4UXAzkgXDvaCjxn9qlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=BKFIsEFMVmKOfDG_NmS5ZWB0ZUxyfGmo7u7HfUkxHDZrN0kAByOuPccwiSXtBAGHa3jtk1csHI9wriM3dlf3Ukv48505QyRQrry_jaWV1JoOmuwAiAr9oFdVnlHzjeECitP6e_vsp1Ay9ehhmQOdfEnu36m8XFgNVZlFxCAb-dA1GTRuIR4Qgf6Wra8WkA7OknuAl9LMzYA_Ne0x-OcYmVBLsY-lmD-QKcBtJp4stdNzzVHpZI4TM1XozZ4yAQv3BD1jZrBZnRK2TQhPwK0x93SZjuDFaITP-Ee6ks9M9y-q371sTLBDreZ-2t1Bdmw-4i18RwWQ5KGcNxBkyNZsRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=BKFIsEFMVmKOfDG_NmS5ZWB0ZUxyfGmo7u7HfUkxHDZrN0kAByOuPccwiSXtBAGHa3jtk1csHI9wriM3dlf3Ukv48505QyRQrry_jaWV1JoOmuwAiAr9oFdVnlHzjeECitP6e_vsp1Ay9ehhmQOdfEnu36m8XFgNVZlFxCAb-dA1GTRuIR4Qgf6Wra8WkA7OknuAl9LMzYA_Ne0x-OcYmVBLsY-lmD-QKcBtJp4stdNzzVHpZI4TM1XozZ4yAQv3BD1jZrBZnRK2TQhPwK0x93SZjuDFaITP-Ee6ks9M9y-q371sTLBDreZ-2t1Bdmw-4i18RwWQ5KGcNxBkyNZsRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=X3uw1rVW6g6aCV9SeOvlF1xBFhTGl6TiykdxwHw77eIDcF8hw3RKttU2zLpiGdedmPPOak-F2NeB7UvqYBpMpdum6OED9FlI4Iiu2fJmYdRrQoOxrvtXHTyWbvS7-8tx1NLbyH9EKxzsnsHyZIVFGatI0P2MZBRwoezcwU69GPzX203CSnBm5AYG9ohAHcgEqbGleEEjdinOlwCNQ16So4piQo7C3ErtCDWFf8mP4YUcH6Ega19u4SkFuefqaDBJmnwmr9Nrs3qHTc3sxZaaIX-x9y4Vc4S__2pI2oWrcazAqStN6x-lb0L5ZqpXYaTmrX3R4vBjYIqOND178ZAkAjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=X3uw1rVW6g6aCV9SeOvlF1xBFhTGl6TiykdxwHw77eIDcF8hw3RKttU2zLpiGdedmPPOak-F2NeB7UvqYBpMpdum6OED9FlI4Iiu2fJmYdRrQoOxrvtXHTyWbvS7-8tx1NLbyH9EKxzsnsHyZIVFGatI0P2MZBRwoezcwU69GPzX203CSnBm5AYG9ohAHcgEqbGleEEjdinOlwCNQ16So4piQo7C3ErtCDWFf8mP4YUcH6Ega19u4SkFuefqaDBJmnwmr9Nrs3qHTc3sxZaaIX-x9y4Vc4S__2pI2oWrcazAqStN6x-lb0L5ZqpXYaTmrX3R4vBjYIqOND178ZAkAjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV7C2TjUUCk3FDGoX-OgDzVmU4TrbM4JqiZuL17I7OVr6AgkQBJ17WY8zWsWbWN91XrN_-S5T0MO6Ff6yJxtfhpxFACnNY4EwpPOe3KUAlihyICu-USoB4bULjs2S8Kf6yDYCykh6ws55Jgx8-5PbnkiMizu2PJ6luBHrZyAfVkRn4pRZMomyJlufzUOaIPG9gT1g4GpykwsORIkY6zWPLAJYyxQdY9YtURswg0oVpfmsFqDDSSKNr74pHmmP1QE_Qfch5uYFGEEgmZBi6rnzTVloIPBWVdZVJQNbNcV_kAvi2_SwCey8gC3WVf6f1-MP0IB44Xh7sm6kzX6HWNUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr7crBqHwXcWuzIifYhJfWftQizR3Q-9gbW_cdMKasoT5gJfdoHxuc1jisatWxqa8rsSodbZWGrO6Bx2hWfWwFQI-XLngKFgvpo2vZx-QsoJQ3Ib2ZP3Jn2YdYvag-fUSThT-IQ2QXxj_ke2KTMg0ZVx5LyG8zOQNivn7ONEP9pN3zqyIjYfU_5MvK-UBlVzwKfbNX3INEOva6gPrY17GaM-MAr5U5y7uiaMNEQ5prIW6WF2Icqjo_px_oFQARhDf-NyGnHWBhJHxzeVyxR88-3YBA3sB1wBi8Y3O_ma80fGds60Bvcs6eejQax7Db5z4ThblQ5rbtFGeYU_gdvgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=tQKhw-4LLW4DI7xOMwuK1ZLSNP_BrlqZ_DHckGxWDY99ewhDsEXpFA_TaY7iHJO_aO_n6kmdU7rc1NVNi5-MMjVBFHX0gXONHhCy1djRBo2IDFILQY8lCXTlkUE32R-O73Ql9kvbAzKuG3CLqLqNIeSZbt--zDL-ah7GnQ4nBTq5vRRltxPJxU6n1T4so7168unhWfa51rry7askS_sXYUQw5CfxdRi6V-BawYl6ktTgxhZopKeyFFjJ9uM_fjZ2SCJCC5dvxj8GLhUZ8JxD0AyaEX-tXvdETnoX_ZDit40vYmVdBZ_KutTRxx-3CZb9E9jln6s9IhG3KuQavj_AszNZZM7pV_B9UgaO-aaYOTlXekU7peEXmA7yrdGlzCl-AZtKtpOXymDoc_9HanyGeux3AClsaeCc9tMEWyrBEcctH1PeZ0SdBan-WvyIQqn8e_moDaAStDUD0jywjWAAAtUdLwE5PzvMlCIdfFgLKaptw_gmofWesRQ6ocD7fRzsz_avNr9OqxaXbrOFySjC2IWvCkE0wUba5QtGx3gaYzGziBiVP4paf5ibn8ZXLGcf4_BLeZXWpZo2LkmNa_Ou42IwB-7RneTuV0C4OM8AuvV-ABDX_Qaunl--LY-8AeZJvQPrRKk_jXS0H3y8cTkEKX508s6Y0Sq9gnOGWtvByJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=tQKhw-4LLW4DI7xOMwuK1ZLSNP_BrlqZ_DHckGxWDY99ewhDsEXpFA_TaY7iHJO_aO_n6kmdU7rc1NVNi5-MMjVBFHX0gXONHhCy1djRBo2IDFILQY8lCXTlkUE32R-O73Ql9kvbAzKuG3CLqLqNIeSZbt--zDL-ah7GnQ4nBTq5vRRltxPJxU6n1T4so7168unhWfa51rry7askS_sXYUQw5CfxdRi6V-BawYl6ktTgxhZopKeyFFjJ9uM_fjZ2SCJCC5dvxj8GLhUZ8JxD0AyaEX-tXvdETnoX_ZDit40vYmVdBZ_KutTRxx-3CZb9E9jln6s9IhG3KuQavj_AszNZZM7pV_B9UgaO-aaYOTlXekU7peEXmA7yrdGlzCl-AZtKtpOXymDoc_9HanyGeux3AClsaeCc9tMEWyrBEcctH1PeZ0SdBan-WvyIQqn8e_moDaAStDUD0jywjWAAAtUdLwE5PzvMlCIdfFgLKaptw_gmofWesRQ6ocD7fRzsz_avNr9OqxaXbrOFySjC2IWvCkE0wUba5QtGx3gaYzGziBiVP4paf5ibn8ZXLGcf4_BLeZXWpZo2LkmNa_Ou42IwB-7RneTuV0C4OM8AuvV-ABDX_Qaunl--LY-8AeZJvQPrRKk_jXS0H3y8cTkEKX508s6Y0Sq9gnOGWtvByJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
