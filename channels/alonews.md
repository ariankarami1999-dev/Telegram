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
<img src="https://cdn4.telesco.pe/file/SAD2gRopAA04krslXDmRC2q2P7Njjv-B7xhn9_Gt6r8BhppH_VbnYRRMURnUWrxBzHbOlUE9Z6IX_N4VHIF8BP-ZsOh5njNZ3FlsBsjghsswC3RI_WUO4KkVYarF7-MGjx_flhitWnbeDx6993UlNojhYgh5AohVmw4EJxKlo8T8pgn2_8N2npGnIbLUhJ09IhK7vjertztabP1W7_bfYnAhl2_HoZeY2Qt7qf_Ro8hwjbQsKcmYcPn6f03dlKMn6l2EXP_3LyfbScqEWhjTtgb9csW8q3uN9JL7eB4WdwKRdmkPk7L8lU6gR9VgKf_KS9czwOEDyZHRxhnblaMHvA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 930K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 13:34:21</div>
<hr>

<div class="tg-post" id="msg-130840">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ارتش: انفجارهای کنترل شده در شیراز به دلیل خنثی‌سازی مهمات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/130840" target="_blank">📅 13:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130839">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9ce41f48.mp4?token=AxwWIy_aQiPDATkv9-xFa9RPVzhteIHPn3zZylgsj5Es06ot6jzeZ0EOWHc-wyeSi8wTLQtgyaq6uQwDIQSCUf2laWHlQ2STVepwaOIH0_R8Mg3A6HPV3I3YvpXDxp8Yn0JZfh2ZnC5PaFCw8gdbi_6kQzwwX36_0dfbcJburD1D3_5_dN8VqAlGngUi_PiG3r2ABShES7ixw5IS9m5bEMicdTZBKidFyzCOFSlY2Md34xiB774olSAEU8Xc_iaiLC7P37Rc6mSXiaaJZE744eU2Eh2Hv1SRb_FKF7IIwtKvzUG_8ZbJEhhPEKmXBjPRXx8uMaRkPuDdvTCBuqg2sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9ce41f48.mp4?token=AxwWIy_aQiPDATkv9-xFa9RPVzhteIHPn3zZylgsj5Es06ot6jzeZ0EOWHc-wyeSi8wTLQtgyaq6uQwDIQSCUf2laWHlQ2STVepwaOIH0_R8Mg3A6HPV3I3YvpXDxp8Yn0JZfh2ZnC5PaFCw8gdbi_6kQzwwX36_0dfbcJburD1D3_5_dN8VqAlGngUi_PiG3r2ABShES7ixw5IS9m5bEMicdTZBKidFyzCOFSlY2Md34xiB774olSAEU8Xc_iaiLC7P37Rc6mSXiaaJZE744eU2Eh2Hv1SRb_FKF7IIwtKvzUG_8ZbJEhhPEKmXBjPRXx8uMaRkPuDdvTCBuqg2sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش پاکستان : تو عملیات «غضب‌الحق» به اردوگاهای گروه‌‌های مسلح داخل خاک افغانستان حمله کردیم
🔴
آدم‌های داخلش کشته شدن و انبارهای اسلحه‌شون هم نابود شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/130839" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130838">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erR0f_mPbSbUgq-ZweslZKGJWE7NIAvQNtxQa0PSVrflhHrx8uYkUoettYFhKyMcEBNqpsxmMcTmibO8mJ3zAAclzKtAWjWs3945Pr13WLQ77GtoOEj7bTOyD3gxND1PsAcjq3yhH7xaCKOwk7RYbjnRcY6iS3y1RhxLcaley9s7fxA3SEY7e5o-eS376r5yZJWFxwTVO4D8XEM25NvVys3dOPwzjlLovCBK_M8m_jXdIbd4T6XK1rlU41dxJ4Z0dfsywdVwhfqwpcn9XySSTbHrTbF-NVR3Gfiufgp3V5UCI9te7T2fzA2nfMbsG0YEQ8MrTjsw93DTBLruAEr9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان حقوق بشری
هه‌نگاو
:
روز جمعه 6 تیر،
امیرمحمد کاظمی
، سرباز 19 ساله اهل نگارِ کرمان، که برای مرخصی اومده بود خونه، به همراه چندتا از دوستاش رفته بود بیرون که یه دوری بزنه؛
🔴
بعدش به خاطر اینکه صدایِ آهنگ ماشینشون تو ایام محرم زیاد بوده با نیروهای بسیج درگیر میشن و تو این درگیری به امیرمحمد شلیک میشه که گلوله دقیقاً به سرش می‌خوره و همون‌جا جونش رو از دست میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/130838" target="_blank">📅 13:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130837">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: جی دی ونس و افرادش کسانی بودند که طرح مخفی موساد برای تغییر حکومت در ایران با کمک کردها را به اردوغان، لو دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/130837" target="_blank">📅 13:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130836">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
المیادین: محل مذاکرات فنی ایران و آمریکا از سوئیس به قطر تغییر کرد و به گفته یک مقام آمریکایی، این مذاکرات همچنان طبق برنامه در روزهای آینده برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/130836" target="_blank">📅 13:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130835">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گزارش اختلال شدید در همراه اول؛ تماس‌ ها قطع می‌ شود، پیامک‌ ها با تاخیر می‌ رسد و اینترنت کند شده است
🔴
از دیشب شماری از مشترکان همراه اول از بروز اختلال گسترده در خدمات این اپراتور خبر می‌ دهند. کاربران می‌ گویند ارسال پیامک با تأخیر انجام می‌ شود، تماس‌ های تلفنی مکرراً قطع می‌ شود و سرعت اینترنت نیز به شکل محسوسی کاهش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/130835" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130834">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7rC7OwJyqBRNwTaEWumVRd6urzqdH5i610J8swD3Sf6Zw6EPEFhWzqFhs2ORgmkbYVp73P23DIpVeXtKL8WLbzQUtWiyh8BRyfP78twsfOzTAMNTMXmnSDmSHzFHJWoay-pFEqBu2EsovDub5QqO2TUivZDjZitfMUuDfycxcONpmG2m2s4ZAuCNXC8kMO4Ruwn5D3gQkgX5B0lT0c3kVnB-vg1V1XBYYWpajI_31Ib7XphpRIw03sG7A316M8cB1glVLF_OX50vnk1hH6fCKdE9qJhhJBbP67qug4ihiNe3Oa7pyGgThJpNf4zAXBPE9Z0WnvN3zLioEjobghHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با کاهش ۱۶ هزار واحدی به ۵ میلیون و ۵۹ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/130834" target="_blank">📅 12:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130833">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
آزمون وکالت ۱۴۰۵ در نیمه دوم پاییز برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/130833" target="_blank">📅 12:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130832">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
رئیس ستاد کل اسرائیل، ایال زمیر : الان جنگ به یه مرحله حساس رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130832" target="_blank">📅 12:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130831">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ایندیپندنت: تابستان امسال تو بریتانیا با یه موج گرمای بی‌سابقه آغاز شده که دمای هوا رو در سراسر این کشور به سطحی فوق‌العاده بالا رسونده و اگه وضعیت ادامه پیدا کنه کشته های زیادی میدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130831" target="_blank">📅 12:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130830">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516d2a369b.mp4?token=VYyyuhN2wcBCJKPVTP9rM8INKvseZNIN_K5TgNQxgxgyO_FS2SFnMRPy0zHjvqt2Ffn7mO9-8xyz9IWUuw3NvY6nFW9Ein0fZfPDCidZ0Jr2ZKw8xcU3k6t9wU30YfYayKk-Mwlbwe-SsnbqFiOdUpAblQhH1zLOv67aC84EVIxZWvXQ_uloi_Z3gyACokCaQASH39WuTsBj_gMhvROHXd_xJGyyuQBiKO7WZRrM4vAIvOX0fr0t0-WBxI9-HCi-6l18Qlh9GI02j-zK1Vgahs8tqA35obV4XnXGSJdoz3SUobneC4Qw0GXHaeDkjzfpYDjSHS4DuhLcZXfeJuPamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516d2a369b.mp4?token=VYyyuhN2wcBCJKPVTP9rM8INKvseZNIN_K5TgNQxgxgyO_FS2SFnMRPy0zHjvqt2Ffn7mO9-8xyz9IWUuw3NvY6nFW9Ein0fZfPDCidZ0Jr2ZKw8xcU3k6t9wU30YfYayKk-Mwlbwe-SsnbqFiOdUpAblQhH1zLOv67aC84EVIxZWvXQ_uloi_Z3gyACokCaQASH39WuTsBj_gMhvROHXd_xJGyyuQBiKO7WZRrM4vAIvOX0fr0t0-WBxI9-HCi-6l18Qlh9GI02j-zK1Vgahs8tqA35obV4XnXGSJdoz3SUobneC4Qw0GXHaeDkjzfpYDjSHS4DuhLcZXfeJuPamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سود سپرده بانکی افزایش می‌یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/130830" target="_blank">📅 12:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130829">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نبیه بری: تنها راه اخراج اسرائیل اجرای تفاهم‌نامه ایران و آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/130829" target="_blank">📅 12:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iM0MZDxlZl3_vI0gDDC08nnIYSHMche_Rsc9W4IwG7tfwuRE7Rth0EAfdPbZNCl3y3dlOYRBdIe3Y4OSqlk1cjBuMfzWiNQZFEpcj2am0YQAidx1GbFCQvepGOmZG0jyB4_SkmL67TGiOHux5g_aQvIfaF0UE_qZK1HlSD2dSYlfOFElGjMjLatmHfOld0YWlYKG71VR85Cpdvvt845ZshycFzUiYiAa04OVl4ymcUxYM1bDoTcx3F1aANq7AZSTCbCvU8JOtLX2xV5Vq7_8jdh7XJcZVEJl8fiYM9ULM0CwOkVHWY9E5VK0l61OBrs3bueIpZ9ckyAxBzbPgIeQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYWM0ZTnRSK8j3zlnAU91USETWRbu4ZRBtpPGJp7UgDKfNBcb7pt60IZzTSjjUdJ402xbQX5G7C010kntioXB4YNBN8xBxSWL6rkYPeqOccCHIl3PhPA4TbOaROpzD7qPi1SBw7LAcxDQ8gLcIL7oK-F5Csa-C_npoAmIw-H84TjsHBfXYvHboW7yL4w8kuup5Q0bNiobDE24LLh14UvwnqXw7r6HubkBRoJ1-kmqfk8EJ_0hXJABxDPM_8WMGZ5qXzBjijhEqbQdtdfVYHU016m1TuKZgU2VBHP8bHdeulGKdbAsOe_vfCmUEfjeB2C3jLUGyFZBQpJFqU9ILFSQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQzG4o6hdVAtx_Hlk5kNe2qaQxQLVSDhsIFFbJGON3nWMJR6o6L9E5-cnaq8nbxPupQEooo-TznMHD3_lFLFxlL7SI-LbX3c1FpEQWqucK1AXWoQxTfLC0FgU2fjJkQHJoZvPOk43pn0oLHJdLRAL9QfpCfxXdYw_CChbbWoPPKtKbXlHGeZTREzHRcHtO56TSq65wDN2pL0BccWNcLdE5oNFdLjy5Y0cJEM-a12qkEhF3sgoIb4KbaP763_0TbER68ueKb_ZHoLQZXpnck0vUXPm0Mk4o_9UgC5SjFP3YmnApk9FruMOBIjrHPh8af1Quhax7N9TFJY2EqVtSRBfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDVIjj_yk2pjyU8yeqTwkcr_M8cg6PbvysRYluh-ZOpKMtc2KZ8BEMc-1uooxfS8ltMoHUvH6PK6rJD9IxkEtGF_Y4VpJmjMKtXf5_HCUFx2clyKp2RtIGisLHJZEMucbk2q343u5eexwj7CisOCWbQJx6HNDRt-F-jEYrE8TFmYPMb1ny0VCDVRRPdY7ZVN_MFsAdswzrzd3ZW-eiqLIuxOOfp31MhKOvdT8dNXPCNbhzCz3052Qpdta2k6SgoveXLgD6c_-e0oPHScw-BBu87l1uXrvypzX5SEeKRbGobh3lBwTTDtZ57uheRUtbtrtXjqqQw2hC4DvVfh8nHCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgkgkWBGeyyyw-WLxUW7UACEtCMgqML2cdUN5iIYMMozix-d4m8BeW2c-VM8_8U_-TrU9i6Ejmhy6YF-YrhV4vx8yfnZs56JCMIrZIOMjCAslb7w6ZWnyWqQ_vx6GhPNMQVeBIQ4Nf5Xl0giBlQSQ2pskKxgEvSbDcz_gzJyoNQlefGxzzqd63KuOUh3B_N2cn7i-1Uc07lGVQ454m2vIbQnkEsZ3dGYYFtp6LToT8ExjgmHrelKWKOtKiyE1z-mPUoX2Bz0lZ64mOqhJYPzHJGw0psDaJ18KBZOlmr_-i9qjZLjvDV346nv7_bNZ_CEWa_6WuBZRQGuURkmMZ7BOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ui2difXNBqDItjed0NL7LvS-7ZS3E2w2PlSLZ5xT52euB5Gx0FYayUZpNng-hHn4Z9PCrKG8XVVzMT216y81ujfG2bYASDNDlxzK95jlaSh6PqRtp5v05VBHCjrlNh_xS5LZfMPld_8U0AsBBGw5ipi_NZmUZ2_c1SwTJVG51uVtDwy3gDWgV-cjAd6NcvtyqE1wLmRTFr_tV8i8hCalaBo9A26J0DOgrA1nEoDVJIvWN8fDBW_fv7l-HAFhBgr0JDR94UiMbGqjiIn1yz5tsx_EODN_utcMLxFOhAtG-4rAThAGBUimrDIlxnuz3O3LeeH8IvEvt_BjklthZTtYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-WVhrO6zLX6RZQDcJMyqzYskHh0oVzBhyIh3D8PYW9oIOul8kNug92FTLEbT2RFG0YccOmokKKChRBupArx4442GCBqmgI0niIiV3CO80sU35Ia2ILRc03ZkBAX1TBq9u_1YlTZ1qlavQsiGnl9TBEIbplQdO-Phx6V7Fxg-1JwDKBH-krGqJDAX8VhUJ8MbiK5Wreg6VJBf14Adg8gqRPedgsCMYLlddcGxVV0e_3louzk4I_y-9AfPrPcFzZb0SiJiNg82virCihq2XDEF9oL5EDXhfBskBy3PrREYqsrlyfZMw2aw2VRUTojbU1Hg5ht1aZLq9IF23Em3KnqwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر خبرگزاری فارس از تردد کاروان کشتی‌ها در تنگهٔ هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130822" target="_blank">📅 12:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سازمان جهانی بهداشت (WHO) با هشدار نسبت به پیامدهای مرگبار موج بی‌سابقه گرما در اروپا، اعلام کرد که «تنش گرمایی» به عنوان یک «قاتل خاموش» طی هفته گذشته جان بیش از یک‌هزار و ۳۰۰ نفر را گرفته و علاوه بر تلفات انسانی، زیرساخت‌های انرژی، حمل‌ونقل، بهداشت و محیط‌زیست کشورهای اروپایی را با بحران کم‌سابقه‌ای مواجه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130821" target="_blank">📅 12:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130820">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ارتش اسرائیل: در پاسخ به نقض توافق آتش‌بس توسط حزب‌الله، از طریق حملات مداوم به سربازان ارتش اسرائیل در منطقه امنیتی، ارتش به سه مرکز فرماندهی حزب‌الله در مناطق نبطیه و مفدون در جنوب لبنان حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/130820" target="_blank">📅 12:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
استاندار تهران: روزهای ۱۳ و ۱۴ تیر در تهران و ۱۵ تیر در سراسر کشور تعطیل است؛ با این حال، مراکز درمانی، بهداشتی، انتظامی و بخشی از شعب بانک‌ها برای ارائه خدمات فعال می‌مانند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/130819" target="_blank">📅 12:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2301d6d68.mp4?token=uBgYVeatdIxn3oX6AVpGc0vPTTMW6ttX5FgsN244Kap0r8QOv3jYxEvnmOFijAg4qMa_z1_3FT-6BtLi8-lo3IjEVVNmAlqoIbbo6ZfWnmj03p9KBQ5UiSBqrs0nL3TXeCInIzpURKhGkowtPWQufc8rlhCtSFF_qjE7cYFWVOgSSTyQ_8nWVMCDywWrQdOHYZRuyVAfMHeQjla8ehDnRHBuUlOyFzwMmqsLMev5QGiULaHTfLppAYIJzbNzKaXhLNN8NbzNth7LaTUtg_g3ac3QSecfhT7ZTY42EGzN8-7V0yirc6n3CRecAbX-ZuKP3cBSmPmQxchrdBnCubfX3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2301d6d68.mp4?token=uBgYVeatdIxn3oX6AVpGc0vPTTMW6ttX5FgsN244Kap0r8QOv3jYxEvnmOFijAg4qMa_z1_3FT-6BtLi8-lo3IjEVVNmAlqoIbbo6ZfWnmj03p9KBQ5UiSBqrs0nL3TXeCInIzpURKhGkowtPWQufc8rlhCtSFF_qjE7cYFWVOgSSTyQ_8nWVMCDywWrQdOHYZRuyVAfMHeQjla8ehDnRHBuUlOyFzwMmqsLMev5QGiULaHTfLppAYIJzbNzKaXhLNN8NbzNth7LaTUtg_g3ac3QSecfhT7ZTY42EGzN8-7V0yirc6n3CRecAbX-ZuKP3cBSmPmQxchrdBnCubfX3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تسلیحاتی که در این تونل زیرزمینی حزب‌الله توسط ارتش اسرائیل کشف شد ، از جمله راکت و قطعات ساخت پهپاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/130818" target="_blank">📅 12:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eeb8978e0.mp4?token=lUI-sxHkFcR71nEpKF0KFhQxH1PmjuhDYwFqUoi3JH0NuZr-MyD5ppdYSudRbEzJpSTDZoIgztYxT8SaVTbtZ9clodGctCxBiVzrN_I9Ov5TBvkThW3wz0OD-_1nZZtHauOVVlTKmG0UUyeDbV4Qttd-1Q9eY8Cph07OVQF1XjjpH0ZsrqFNJngKTlcSqSJKmmYrlmAM9jQmNAH-L7ZJbBcNtuOzIwoiNmdwL_XrPVvl0mdKuF2ARYMhgaZMSyKT3l7siS5Ua5n8VIxfZMp_92Ogc-MMjuL9iCwi2Vbh5IF0eeQBnGzNMsTmVw0oPRSnD_qDPdLi8pf_BByMAd5i8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eeb8978e0.mp4?token=lUI-sxHkFcR71nEpKF0KFhQxH1PmjuhDYwFqUoi3JH0NuZr-MyD5ppdYSudRbEzJpSTDZoIgztYxT8SaVTbtZ9clodGctCxBiVzrN_I9Ov5TBvkThW3wz0OD-_1nZZtHauOVVlTKmG0UUyeDbV4Qttd-1Q9eY8Cph07OVQF1XjjpH0ZsrqFNJngKTlcSqSJKmmYrlmAM9jQmNAH-L7ZJbBcNtuOzIwoiNmdwL_XrPVvl0mdKuF2ARYMhgaZMSyKT3l7siS5Ua5n8VIxfZMp_92Ogc-MMjuL9iCwi2Vbh5IF0eeQBnGzNMsTmVw0oPRSnD_qDPdLi8pf_BByMAd5i8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل ویدئویی منتشر کرد که دیشب تخریب یک «تونل بزرگ حزب‌الله» زیر روستای در مجدل زون در جنوب لبنان  نشان می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/130817" target="_blank">📅 12:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130816">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پزشکیان : از اون ۱۲ میلیارد دلار پول ایران که توی قطر هست
🔴
قراره ۶ میلیارد دلارش آزاد بشه و برگرده ایران
🔴
برای برگردوندن ۶ میلیارد دلار باقی‌مونده هم داریم پیگیری می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/130816" target="_blank">📅 12:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
جان حداقل ۱۴۵۰ نفر را در ونزوئلا گرفت
🔴
برخی شاهدان می‌گویند هنوز صدای افراد را از زیر آوار می‌شنوند، اما نمی‌توانند صفحه‌های سنگین بتنی را جابه‌جا کنند...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/130815" target="_blank">📅 11:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
واکنش بانک مرکزی به حواشی اختلال ۴ بانک: انتخاب شرکت‌های فناوری ارتباطی با ما ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130814" target="_blank">📅 11:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130813">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مرکز مدیریت بدهی‌های عمومی و روابط مالی دولت اعلام کرد: میزان بدهی‌های دولت ۲۴۹۷ هزار همت و مطالبات دولت ۲۰۳۳ هزار همت است.
🔴
آنگونه که مرکز مدیریت بدهی‌های وزارت اقتصاد اعلام کرده، نسبت بدهی دولت به تولید ناخالص داخلی تا پایان سال گذشته (۲۹ اسفند ۱۴۰۴) ۶ درصد بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/130813" target="_blank">📅 11:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130812">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU13iFCGULiYRxeZHdFIJDbT-jUZUR1wGfywOSW_IEbKQp1sG8onhEVEdE1GtspNzOm1dSZDcCfatYwBXQTEEWvL_YVYBDj9Ppo0aSzwIm_z_yKpvPPGbxJyRpBzqnE4uSmcbMZ0TU-lewXe9XdmiOooaWcxveg1PbiTNOZS8D4xFA3ImdrdIrr2_1d4yfkcUumQTOhBjAfoMJwgs2JZ6T7p7dz-HG7Rb82B0PpaObmy2R5ckSP4gK-u0cgOzYyxsr30uVXIQAi-jQWfyI5bAypxNwPDtA2GsEOSHEevm9mxJzrbCcoMNhmaFHl3PbtjbSiT02IGpT0NwEUAfSshaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باز شدن نفت بالای ۷۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130812" target="_blank">📅 11:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130811">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
قیمت دلار ۱۷۲ هزار و ۵۰۰ تومان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/130811" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130810">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ce213c07.mp4?token=hXwrq3K6yNmLeVXFUOJvlX04epqqLOTg6mD-q7JThrQk7ITC6ie8-hfBxS64myAf-S7S1bXeuyV7QxC9_-dqjFs8_NByyH2NWxGg3WRO0L0IUM4MJ31InHX7l8LamAHQy4LPlATUMugeQv1wg7t6AYjFSLLqYBHUkHOBQPh5Wkre3M89_19tWagUNAq2WZCVPy4vGlM3k86iAygI6FQJMqD8dywX9Ncbk2WafhEGdmedJDtGriCUWbaorFj-ZRfj6PDxeGv2NpxL46PbqI2KxLwMBTbqYWAie1UZUF1ok33WedrswzaoBEbYO4hPuH5GdTrFMmS2IZn_QA6gLqPkKhDjMjy1xmhooY5FuiwlBZAdRGSPH4dNZ9u0xpJEHki3dWFEmJl-XZhF4CoVi9TE4rFkIyQ2Qb7X71_Lh3jxHhmknmf5n4XPk3G6Hf0JBO3bbF25OKHtfGzmui0Q4i_0mumzFIFJMh6ko3alSr_TKKD59xsOOOayFUJ2WlaxcH3mTY62_TvHp-dHUMaupkRX-MKL53A64ViION2NNM4qeS2uGxqTug7JfCPra9eDDFcWm3KUvsoeL3wnmuXFGvhBHKkDXacysu-8Er58aqgQJpY8mv8io6ITb1x-OdKrwiVCbx9ye_XT90gyItY4kZ6gbJeS71w9TQC2JbaKCMYskvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ce213c07.mp4?token=hXwrq3K6yNmLeVXFUOJvlX04epqqLOTg6mD-q7JThrQk7ITC6ie8-hfBxS64myAf-S7S1bXeuyV7QxC9_-dqjFs8_NByyH2NWxGg3WRO0L0IUM4MJ31InHX7l8LamAHQy4LPlATUMugeQv1wg7t6AYjFSLLqYBHUkHOBQPh5Wkre3M89_19tWagUNAq2WZCVPy4vGlM3k86iAygI6FQJMqD8dywX9Ncbk2WafhEGdmedJDtGriCUWbaorFj-ZRfj6PDxeGv2NpxL46PbqI2KxLwMBTbqYWAie1UZUF1ok33WedrswzaoBEbYO4hPuH5GdTrFMmS2IZn_QA6gLqPkKhDjMjy1xmhooY5FuiwlBZAdRGSPH4dNZ9u0xpJEHki3dWFEmJl-XZhF4CoVi9TE4rFkIyQ2Qb7X71_Lh3jxHhmknmf5n4XPk3G6Hf0JBO3bbF25OKHtfGzmui0Q4i_0mumzFIFJMh6ko3alSr_TKKD59xsOOOayFUJ2WlaxcH3mTY62_TvHp-dHUMaupkRX-MKL53A64ViION2NNM4qeS2uGxqTug7JfCPra9eDDFcWm3KUvsoeL3wnmuXFGvhBHKkDXacysu-8Er58aqgQJpY8mv8io6ITb1x-OdKrwiVCbx9ye_XT90gyItY4kZ6gbJeS71w9TQC2JbaKCMYskvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از آخرین وضعیت میزان آب در سد کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/130810" target="_blank">📅 11:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130809">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری / پزشکیان، رئیس‌جمهور: ۶ میلیارد دلار از منابع مسدود شده ایران در قطر آزاد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130809" target="_blank">📅 11:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130808" target="_blank">📅 11:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130807">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
غریب‌آبادی: اولین نشست کمیته مشترک هرمز در عمان برگزار شد. درباره مدیریت آینده تنگه هرمز تبادل نظر کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130807" target="_blank">📅 11:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130806">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-K9IY537Ck1B-ckYH75pqEKhcwEr0h258fkH5BGnwxXoMTAphSII04AQGWNEi6U39Q5K5HCL5EeesmixQFcy22AOImO8XUwyCq3EEAsyyscpwG30yVlO0lBWgcGdtRt6qkHLYy3RgyOTsiw70Uei_ng1tv96liU6UYEmxSXKLONo4k9_5jOuvErA9GWLWkaMCondUWjoTkEKr3GRn7W_NiSqYVK-UFQUl7FNvQoCsKEi2opD39EsgpNVOSrYfIzo98AZASt8d1xThTmk2hbfFX9mFIaDMFcKQFWb8lpziI_uNDpVcjup2USU5iBU0EITAUGGVXE9WZQFLDebiCVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثروت بنیان‌گذار بایننس از بیل گیتس فراتر رفت
🔴
براساس جدیدترین فهرست میلیاردرهای فوربس، ثروت چانگ‌پنگ ژائو (CZ)، بنیان‌گذار بایننس، به ۱۰۷.۷ میلیارد دلار رسیده و از بیل گیتس با ۱۰۵.۹ میلیارد دلار عبور کرده است.
🔴
بخش عمده دارایی ژائو به سهام او در بایننس، بزرگ‌ترین صرافی رمزارز جهان، نسبت داده می‌شود. البته خود ژائو پیش‌تر اعلام کرده بود برآورد فوربس از ثروتش را دقیق نمی‌داند و معتقد است ارزش واقعی دارایی‌هایش کمتر از این رقم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130806" target="_blank">📅 11:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130805">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/giVVDF47raOxRKxhFuLk9ex8uDkJuI7FOOsejJrpUgKbqarwkGo6xde2kZC8wWG6KKb3tdASmU_XawHLQIo-UKgLkJuPDymLrGTyD1HI6T2mWonumNrgQd1VtYUkn29lmqlHpl0bjh8a01QqyPEu5DDY0IKy1n-JUcl8zijsFW2Zylfp0pLhL-RxJv7PFATd6DtnS_zAkjQIUfVaEw_9tjUwrbYebJl4YUsTPP3YF0FhzJ-C5HrQ58WKjCAzofTp2MnDLUtPGY2xJGSXRkN4EurQ5TF0MP6BkbiMWwiQYHKZL4fcIA5D7Tf_hUr245piw6XYcInn079OD8EmBbBqVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر گاز اروپا در مسیر رسیدن به پایین‌ترین سطح خود در حداقل 15 سال گذشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/130805" target="_blank">📅 11:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130804">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35ef3b087.mp4?token=i06PyPkK120EcBMWa7fZTJXtPae8sIgrJiO6USOgY26jFhZkGYKuVPYRNaad8e0Ozve1v-p0b3RRFGV9AT08EK89TyhjIFSsdT_PbWz0p0opVYDfcAxqQ6S5xu9z4wYqFmfnR-ImU5ynrIKpuUAMx48SwdNwNfwIYi5FFFvVupvCjUmbQCXhv8TR69A309QvTU8MSmlvRoZL4GfxtHhX21Wty_35XRlWkLVTeDwVrnH9hBnDwnIv6_8hg1X0STpRJzJrC-NM2fsdk2eImnht1gOPQ6LX5AQCCUsNzziXmlKRsHSpb7v6ObHYi7LPX987dQju5UhU01i3TNRPqTxbeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35ef3b087.mp4?token=i06PyPkK120EcBMWa7fZTJXtPae8sIgrJiO6USOgY26jFhZkGYKuVPYRNaad8e0Ozve1v-p0b3RRFGV9AT08EK89TyhjIFSsdT_PbWz0p0opVYDfcAxqQ6S5xu9z4wYqFmfnR-ImU5ynrIKpuUAMx48SwdNwNfwIYi5FFFvVupvCjUmbQCXhv8TR69A309QvTU8MSmlvRoZL4GfxtHhX21Wty_35XRlWkLVTeDwVrnH9hBnDwnIv6_8hg1X0STpRJzJrC-NM2fsdk2eImnht1gOPQ6LX5AQCCUsNzziXmlKRsHSpb7v6ObHYi7LPX987dQju5UhU01i3TNRPqTxbeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو نشون می‌ده آمریکا طی ۷ روز گذشته فعالیت ترابری نظامی سنگینی داشته و حجم زیادی از مهمات و تجهیزات نظامی جابه‌جا شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130804" target="_blank">📅 10:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130803">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5532f056.mp4?token=A7GHbZgVENXOs3uM1bNNNQniyj-LveCf1UlUszk4sdl6PYarnS2YPozcu7cLHWb552_A9NlJywLdz1lzNX0-gq0GMCkyXevHu4RD9rq1HmQq6UVZOadeeDPFNoRpok3Nwpm4f_fSN69SKSfPRkzAmeUa7TvTH8rcN70xFOXQFjZ8NAVC0MCMAJgGYu8YtndsCqqjb4QGO-VJ_tOPhfsDfTBRhDAfyklf0LrBk1r4GHMK-9d3fX-vdUz1fTcEqiR8tmWOyfWDdRw5MFLAkxkU4yEZLs69ZyAcdDH_rIYTjakC_3aKN2RU1TvaTA1IU0suza2migJI4O9M_foVlubBog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5532f056.mp4?token=A7GHbZgVENXOs3uM1bNNNQniyj-LveCf1UlUszk4sdl6PYarnS2YPozcu7cLHWb552_A9NlJywLdz1lzNX0-gq0GMCkyXevHu4RD9rq1HmQq6UVZOadeeDPFNoRpok3Nwpm4f_fSN69SKSfPRkzAmeUa7TvTH8rcN70xFOXQFjZ8NAVC0MCMAJgGYu8YtndsCqqjb4QGO-VJ_tOPhfsDfTBRhDAfyklf0LrBk1r4GHMK-9d3fX-vdUz1fTcEqiR8tmWOyfWDdRw5MFLAkxkU4yEZLs69ZyAcdDH_rIYTjakC_3aKN2RU1TvaTA1IU0suza2migJI4O9M_foVlubBog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جان کندی درباره ایران: ایران الان مثل یک مرد خیلی پیر است که توانایی خوب شدن از سرماخوردگی را هم ندارد. ما آنها را به شدت تضعیف کرده‌ایم، نباید تسلیم شویم.
🔴
برای من عدم توافق یا توافق بد قابل قبول نیست ، در پایان یک دوره زمانی معقول ۶۰ روز یا هر چه که باشد، فکر می‌کنم باید دوباره وارد شویم و با قدرت با آنها برخورد کنیم ،باید آنها را بخوریم و استخوان‌ های آنها را روی زمین تف کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/130803" target="_blank">📅 10:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130802">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رویترز به نقل از مقام آمریکایی: مذاکرات فنی ایران و آمریکا درباره تمامی بند‌های یادداشت تفاهم، از سر گرفته می‌شود
🔴
دو طرف حملات را متوقف و کشتی‌ها آزادانه تردد می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130802" target="_blank">📅 10:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130801">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/229c290e15.mp4?token=pUTBmLYauvGcgNLVjMB0V83G9NY9OifAZcjwftDdqaRhC94tYGoKvWO4z0DWwEXdl0H4M-F3eW5QJX08eKINYm4-uhleuqMw5QPLJ2HQ8RLlAvd5jXsQKFfe3DjONSwAz7L8Aye8HT-TsCiBJEAF_9ivp4kmhaV3GY7b6-U-Td4Oll5YB3dzI6_6VqvdKJg2eXBgUVahwAIDe91jOiqYlZePyAcYTsG6bfRRG167GgDl4pBKg15xk58FZIKYx3fXOnEP1AGAJtamR22DXGH8KjlpO_m9maFYgSjtShmTgsGNiHrng8-VloIOiQgdESUpfQaPDrOJPYSlprt4fCVAT3ocNfmjbTYd6A-FsRsVoc9vywP8R97ucvUmmbTKjAFenI2iKvnGBwCZvjZYctxOVFYUSAoLYrwgRG8M7pnvXMRQFAq0l3jHRI5jVbyiNoOdjdzNSS1bvJCH-ETteDCdkn49KBqeDmsBPcri7dw1OO29eafvNYqr-MJcxWUO7ahA0bC4nQH7FulfE7wYgZYTJtQJPAT_AcLKpHGbFyJ89Af9B5Z2vv3G68SUmFVw6A6ZekHuwQ7jsrQgc1uNRyH6EQy-cgSZ7ORrJt5WlfmlW1cMXMXbQvr-05BjVLK7IDTsKXxb-OXQJYqHhlIkuPo4xbWf3m34wZ2DuMxi8XfxWNY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/229c290e15.mp4?token=pUTBmLYauvGcgNLVjMB0V83G9NY9OifAZcjwftDdqaRhC94tYGoKvWO4z0DWwEXdl0H4M-F3eW5QJX08eKINYm4-uhleuqMw5QPLJ2HQ8RLlAvd5jXsQKFfe3DjONSwAz7L8Aye8HT-TsCiBJEAF_9ivp4kmhaV3GY7b6-U-Td4Oll5YB3dzI6_6VqvdKJg2eXBgUVahwAIDe91jOiqYlZePyAcYTsG6bfRRG167GgDl4pBKg15xk58FZIKYx3fXOnEP1AGAJtamR22DXGH8KjlpO_m9maFYgSjtShmTgsGNiHrng8-VloIOiQgdESUpfQaPDrOJPYSlprt4fCVAT3ocNfmjbTYd6A-FsRsVoc9vywP8R97ucvUmmbTKjAFenI2iKvnGBwCZvjZYctxOVFYUSAoLYrwgRG8M7pnvXMRQFAq0l3jHRI5jVbyiNoOdjdzNSS1bvJCH-ETteDCdkn49KBqeDmsBPcri7dw1OO29eafvNYqr-MJcxWUO7ahA0bC4nQH7FulfE7wYgZYTJtQJPAT_AcLKpHGbFyJ89Af9B5Z2vv3G68SUmFVw6A6ZekHuwQ7jsrQgc1uNRyH6EQy-cgSZ7ORrJt5WlfmlW1cMXMXbQvr-05BjVLK7IDTsKXxb-OXQJYqHhlIkuPo4xbWf3m34wZ2DuMxi8XfxWNY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رانش عجیب زمین در هند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130801" target="_blank">📅 10:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130800">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
تحلیل جدید خوش چشم، کارشناس صداوسیما: ترامپ تنها به دنبال باز کردن تنگه هرمز است
🔴
من ندیدم کسی به این موضوع اشاره کند؛ مذاکره‌کنندگان هم به این موضوع توجه ندارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/130800" target="_blank">📅 10:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130799">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
حسین شریعتمداری: تیم مذاکره‌کننده باید با صراحت اعلام کند که حاضر به مذاکره با قاتل رهبر فقید نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130799" target="_blank">📅 10:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130798">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
قیمت نفت در معاملات روز دوشنبه بازار جهانی، افزایش یافت.
🔴
قیمت نفت خام برنت با ۵۸ سنت معادل ۰.۸ درصد افزایش، به ۷۲ دلار و ۵۷ سنت در هر بشکه رسید، در حالی که نفت خام وست تگزاس اینترمدیت آمریکا با ۸۸ سنت معادل ۱.۳ درصد افزایش، به ۷۰ دلار و ۱۱ سنت در هر بشکه رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130798" target="_blank">📅 10:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130797">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdZSDh9mDsW04AqeSOnsLhxZkpd_vlyo6dFbBz4PzfUbeQz5xxfzB1Vk6ySseFRmMHiDUW7fmlkfVBiS8zJS96-z2JY7sE91U_hJ9mOAh7vCl84NjF5qENbiXmiasUwuaQ7bSSbbcQiyS1XZ1TPAR1QURIoJcy7flKr2qquzf1UynSeW3Emsx14n589LqLpx8yM62Uhe6bA3B3pcpHEHzpwUFt-SuAjk6CvMVklZz0kar96R1y9gMONcS3zIo1ELoTcdxC-tYw8xpB2wDha6jwAGv---LjcHeqTv7gzAr_sv-hlBGy5f35IB3H8-g58jXutZSR7VhIJu4kiWe3t3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه سوریه، تجاوزات و گلوله‌باران‌های اسرائیل در استان‌های جنوبی قنیطره و درعا را محکوم کرد و آن‌ها را «نقض حاکمیت خود، حقوق بین‌الملل، منشور سازمان ملل و توافق‌نامه آتش‌بس 1974» خواند.
🔴
این بیانیه پس از آن صادر شد که ارتش اسرائیل اعلام کرد نیروهایش 2 نفر را در جنوب سوریه کشته‌اند، پس از آنکه آن‌ها ظاهراً وارد «منطقه امنیتی» شده بودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/130797" target="_blank">📅 10:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130796">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7766251c.mp4?token=orAXahTXIBrwBULgqZo9JQxVi0caTA6TL4tpS7pcHDz8b7fDpHYyfyUtmaUlz46fP9odMHi4HWIyHlM73zF4Jl2ibMCNyZzH5EoGzowlKK32wv-TAl3rEtYl9R8mN_8kVt4NqumqyjA3kiDe5nPIirBe9vToK7d3ApsMieG2eHjcQEJxJozPDRJJ9Bz0fYAIL-Lv2k70q9I6ocoSFPBWEuRWWWtvf2NrvjtI9bqTCBxB53tm8E_rAs4adTBKaoaNkLzBQxB4Sj0O91AinZ5MJnaUxenAKZTEbrz4b4U1NJXAy83bsxAyVc5ksGXGjxvi5vY1gWKfoNXAXocz5Jt-Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7766251c.mp4?token=orAXahTXIBrwBULgqZo9JQxVi0caTA6TL4tpS7pcHDz8b7fDpHYyfyUtmaUlz46fP9odMHi4HWIyHlM73zF4Jl2ibMCNyZzH5EoGzowlKK32wv-TAl3rEtYl9R8mN_8kVt4NqumqyjA3kiDe5nPIirBe9vToK7d3ApsMieG2eHjcQEJxJozPDRJJ9Bz0fYAIL-Lv2k70q9I6ocoSFPBWEuRWWWtvf2NrvjtI9bqTCBxB53tm8E_rAs4adTBKaoaNkLzBQxB4Sj0O91AinZ5MJnaUxenAKZTEbrz4b4U1NJXAy83bsxAyVc5ksGXGjxvi5vY1gWKfoNXAXocz5Jt-Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زهران ممدانی شهردار نیویورک در رژه هم جنس گرایان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/130796" target="_blank">📅 10:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130795">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355c9f4cbe.mp4?token=jrRp8__xuAyWGYVvpr6x1m7dMlGfTNnuKI0aeni4aP9KWxTfZdTXMaSqwySURPjXDo4GGuoQ3DUnwpYkMWDhKm3zFCrd0Mls7QC0_EQ0jBoCC-uY9oEIFumZHa1vuy-pguvnk0c9Mj9bI7EcwSMHgDpcqYBd2X8iMB4hjDDQ1m74GJReAOcjUr6F53GwCQOK36k2Ry-5lUKmIcs1Ckmj5oXNf6AkhoGd6KUJqHwFVq83nN3ivcFuwbV1_uf2NBD6-SHdV-UONnvzH1Jl0fld_fjdmszu0EaTvHY1MfY96feDEohHutyfpc7jrK2e6VcqNwEK02_-NSvO3QBlxiyq3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355c9f4cbe.mp4?token=jrRp8__xuAyWGYVvpr6x1m7dMlGfTNnuKI0aeni4aP9KWxTfZdTXMaSqwySURPjXDo4GGuoQ3DUnwpYkMWDhKm3zFCrd0Mls7QC0_EQ0jBoCC-uY9oEIFumZHa1vuy-pguvnk0c9Mj9bI7EcwSMHgDpcqYBd2X8iMB4hjDDQ1m74GJReAOcjUr6F53GwCQOK36k2Ry-5lUKmIcs1Ckmj5oXNf6AkhoGd6KUJqHwFVq83nN3ivcFuwbV1_uf2NBD6-SHdV-UONnvzH1Jl0fld_fjdmszu0EaTvHY1MfY96feDEohHutyfpc7jrK2e6VcqNwEK02_-NSvO3QBlxiyq3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل، بحران زلزله در ونزوئلا را تشدید کرد
🔴
بارندگی‌های شدید فصلی و امواج گرمسیری، بحران ناشی از زلزله‌های ویرانگر اخیر در ونزوئلا را تشدید کرده و عملیات امدادرسانی و جست‌وجوی بازماندگان را با مشکلات جدی روبه‌رو ساخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/130795" target="_blank">📅 10:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130794">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
روزنامه هاآرتص به نقل از یک منبع نظامی اسرائیلی: ارتش تاکنون هیچ دستوری برای عقب‌نشینی از هیچ منطقه‌ای در لبنان دریافت نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/130794" target="_blank">📅 10:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130793">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی:
کشتی‌ها می‌توانند در طول مذاکرات فنی آزادانه در تنگه هرمز تردد کنند
✅
@Aloanews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/130793" target="_blank">📅 10:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130791">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f6d88768.mp4?token=uA_OX4sf2n00QledB2qQ9m0Aaur7Y7Gk-p09_aPeMlkcQDEaA0GmttVXwTKXSXo57TpDDFltCCBwS85aSrf4u7uXZjm4MZ5eegE8YjTxjOsE3uNhl5HOL4099gFxgjGxnWj4Et4xsSCcKlDIdivP4X67Ba7xo8MubNn5elTocsxn4S_eSL02cXOtlfwit0EA9gUH34Ti07AkrzM7kxaWRuuVpHsexxQs3G4TXkGziaaAkLmW43VJ8JsyafwQkfgaEpCbbIXxnkxWtmKGmVX6uhdemgELNINwW1mzdR4t_VBxtQaDgGSh6LeRYnM4ZZ0g1tGLbLJBSq3VdJH_sIaViw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f6d88768.mp4?token=uA_OX4sf2n00QledB2qQ9m0Aaur7Y7Gk-p09_aPeMlkcQDEaA0GmttVXwTKXSXo57TpDDFltCCBwS85aSrf4u7uXZjm4MZ5eegE8YjTxjOsE3uNhl5HOL4099gFxgjGxnWj4Et4xsSCcKlDIdivP4X67Ba7xo8MubNn5elTocsxn4S_eSL02cXOtlfwit0EA9gUH34Ti07AkrzM7kxaWRuuVpHsexxQs3G4TXkGziaaAkLmW43VJ8JsyafwQkfgaEpCbbIXxnkxWtmKGmVX6uhdemgELNINwW1mzdR4t_VBxtQaDgGSh6LeRYnM4ZZ0g1tGLbLJBSq3VdJH_sIaViw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از پایگاه علی‌السلام کویت نشان می‌دهند حداقل یک سوله در بخش پدافندی شمال پایگاه منهدم شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/130791" target="_blank">📅 09:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f16b33ff1.mp4?token=lLErcSW61buHVgZBUaLtvEf2gNNStyBRaBY73YzfSHGyvyFpRw9_7hNLVQS9OkGn68XKjf3TmOBsd2CXtUhsn2WmYnVXhcqVc2JoXgg6A0zOFQDhKHGpCCP-lZ2yf0L5foUK7dkk8L7Kx788LVdw8WKBRUWYXazdy9npmhXSglKVlzqeg1xNAiYgB5q_Xxift8KckKJWkkBIV-ro4Kqrpa7PPaGxc5TNPyBzysEYZeLhT9AQekNy7SJTZRkBFrJHSfViZ7iQzfpm3sxdmh_lWFUQhQ1MxNAatah6eFho-mbGT6IkCfZh4RuXpVf34wn8vg9OW01gHARqoC8H3S2nLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f16b33ff1.mp4?token=lLErcSW61buHVgZBUaLtvEf2gNNStyBRaBY73YzfSHGyvyFpRw9_7hNLVQS9OkGn68XKjf3TmOBsd2CXtUhsn2WmYnVXhcqVc2JoXgg6A0zOFQDhKHGpCCP-lZ2yf0L5foUK7dkk8L7Kx788LVdw8WKBRUWYXazdy9npmhXSglKVlzqeg1xNAiYgB5q_Xxift8KckKJWkkBIV-ro4Kqrpa7PPaGxc5TNPyBzysEYZeLhT9AQekNy7SJTZRkBFrJHSfViZ7iQzfpm3sxdmh_lWFUQhQ1MxNAatah6eFho-mbGT6IkCfZh4RuXpVf34wn8vg9OW01gHARqoC8H3S2nLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عالیشاه، دادستان مرکز مازندران:
به همه ضابطان قضایی دستور میدم که اگه از این به بعد هرجا با موردی از عریان‌سازی تو معابر عمومی برخورد کردید، سریع و قاطع وارد عمل بشید و طبق قانون باهاش برخورد کنید و تو این موضوع هم هیچ کوتاهی و مماشاتی قابل قبول نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/130790" target="_blank">📅 09:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b0902dd1.mp4?token=Cnv0-noj3yZuN_r1CQ3JtL5K87pdKAwzhGMfSLj57IzHbqubZ_IGHkiH3IUUkVHHNZ-E324L_oDVEH-GEZIj5NItV2Lrm8ZKnIlrkhi7HTJ4N_G7S6x30EHfr_qw00Hw1EmQxcnolfuRSIP13_A3h4kfIxMT5cNqX2DqjR3dgPUQwcZjO17aE4pUQuT8myiXbNWYQeaZo_L3UUGbl7Z0K_ED4ZzD_Jt79x7qkKQHHtUbJvt4OdMU-MRNK1tB9CRDrId59GNoTVfFOK6JTOw3XPcFvZmp7_QBTjWsBvTa5ad4nH3Q6ko2sAdEouBoiFtxS0LbPmueYx_A9Xp9Wq5KNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b0902dd1.mp4?token=Cnv0-noj3yZuN_r1CQ3JtL5K87pdKAwzhGMfSLj57IzHbqubZ_IGHkiH3IUUkVHHNZ-E324L_oDVEH-GEZIj5NItV2Lrm8ZKnIlrkhi7HTJ4N_G7S6x30EHfr_qw00Hw1EmQxcnolfuRSIP13_A3h4kfIxMT5cNqX2DqjR3dgPUQwcZjO17aE4pUQuT8myiXbNWYQeaZo_L3UUGbl7Z0K_ED4ZzD_Jt79x7qkKQHHtUbJvt4OdMU-MRNK1tB9CRDrId59GNoTVfFOK6JTOw3XPcFvZmp7_QBTjWsBvTa5ad4nH3Q6ko2sAdEouBoiFtxS0LbPmueYx_A9Xp9Wq5KNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پسر ۱۱ ساله پس از ۳ روز از زیر آوار زلزله ونزوئلا زنده بیرون آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/130789" target="_blank">📅 09:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
دادگستری تهران:  در پایتخت وضعیت کشت خشخاش در سطح ناچیز قرار دارد
🔴
گزارش‌های مربوط به کشت، عمدتاً مربوط به برخی استان‌های غربی و شمال غربی کشور است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130788" target="_blank">📅 09:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcfJfJ5mxo5XxM9Y-zCgA9fq-5kj2x_af9dyuNvTNH_pdSA9j7VS8wfvCdX0WGhSjLiU_UOgF0bIFFAqtfUwh14C-jVfu1GPcGNLfQQQJoR7fbK-dCMgUQ_dxHFESBbuQyr4rNYWSPN4myNKajSvtFu-uw91HafPV6Jd2uvrDEG1HS-EQ7WmJ9kTDpDwKHCl_OlVo4m6a917eAjrT_jclezq2j3hibsT6uMvqVmOqbP3VUBs83OSuG0BzwpmbWHtQkK8Fkcvrn3qb2gmt98YKXKaqYPGT0f44hcDPTxo0kv_UtTrkeRUDrO6s2RbhBKLXIQ-1cXZFHlQRkQbS3kqhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده ارشد دموکرات‌ها: جنگ علیه ایران برای آمریکایی‌ها یک فاجعه بود
🔴
حکیم جفریز رهبر اقلیت دموکرات‌ها در مجلس نمایندگان آمریکا جنگ علیه ایران را برای آمریکایی‌ها یک فاجعه خواند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/130787" target="_blank">📅 09:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFkiMG4kVaRBaG4yix1hMtGwCVugk72M8r64Fg5JCDGlwh69yvXPixwtPKGG7taKidRM1cmCuM28K0OX0QUggJyjyq_k-X1jNLmKUDqgMS_edui3g_ETG4s9bgqqcCDcb0r_muQBCj59E16Ye2QwtAEacQrSZEXjtu40e2ePqo0hEOCP9uHdSZqggmDv3FbLQM2ZWQrnpaT96jfFduFxcIK4MoHjWZrCZclOZfk1zsgDq2jyE0nVQvWRpg2FwT8eTc6ehgfF3SsfPyLyfOPOA3GsnrPqVnYukEnvGUjyndNVf5m-JrtIcoN_apJe3ozertpLDwoUcn8nYi7MsRgl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قطع برق باعث از کار افتادن اتصال اینترنت در استان دونتسک، در شرق اوکراین که تحت تسلط روسیه است، شده؛
🔴
این اختلال با حملات اوکراین به زیرساخت‌های انرژی هم‌زمان بوده و با آن مطابقت دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/130786" target="_blank">📅 08:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رسانه‌های افغانستان گزارش دادند پاکستان چند نقطه را در ولایت‌های کنر، پکتیا و پکتیکا هدف قرار داده است.
🔴
هم‌زمان، پاکستان اعلام کرد مواضعی را در مناطق مرزی با افغانستان هدف گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/130785" target="_blank">📅 03:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43e3853e66.mp4?token=qRsWSWwXOkt9t4m-gegzCefuPUHgZoNxFAv-srkE14vl08nNK0t_B3i9do7uh5ReKW8fqKYlmouC3KV1ZeWuIRBA8QDQcGKUijmBxMzumVI2E1UrsoTFdhqhNk6HWXyGvrPXOVd4_kcuPtb8mCxwSXzPnj1pvdNcBXduQtxRqZ3j0oOXipqBTDCES8-FEuVKr369t0Lxm_oIEepruiZgJwDvl5XLG7ZcFT7njOSCwugXn00H8V1XA7bwVf3TeZxZBjBebfyIurZPDP8s3W3-oblULrugNLUb3h_-_KiqqGTtG3qj9KrOsJLUw_YWQEmr5nF1715b6eIcTxJATLYQqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43e3853e66.mp4?token=qRsWSWwXOkt9t4m-gegzCefuPUHgZoNxFAv-srkE14vl08nNK0t_B3i9do7uh5ReKW8fqKYlmouC3KV1ZeWuIRBA8QDQcGKUijmBxMzumVI2E1UrsoTFdhqhNk6HWXyGvrPXOVd4_kcuPtb8mCxwSXzPnj1pvdNcBXduQtxRqZ3j0oOXipqBTDCES8-FEuVKr369t0Lxm_oIEepruiZgJwDvl5XLG7ZcFT7njOSCwugXn00H8V1XA7bwVf3TeZxZBjBebfyIurZPDP8s3W3-oblULrugNLUb3h_-_KiqqGTtG3qj9KrOsJLUw_YWQEmr5nF1715b6eIcTxJATLYQqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه جدید با بدل جمهوری اسلامی
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/130784" target="_blank">📅 02:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6SLHTdbOhbJC-FhdSwGPm7U6FxrtoPGiMm4Q8Gp5PdMCvMW0l394AJWiDWjpBLfJrLAjnMdNe5FTqc52uY2jTeAaT5qOZfw2QHxEtvS6DgsjvbLhNbuO-4K0mTPtgnAovSCWOBdrrhnZjie40upARtdutfsrsFgFGXqWsOS1_EHGr_ZE2PKeXFi2g0EzH1kachPNq9xf4hKmXWuYRw7B1VTAWzddRrcv649TUTLrYTTqms_qDRWXFnp0cN1iVZevKBhP7RBNpsTdNZe2DTBIDo3EGUfLaNQ-ceyceW3Wh01e5cfilulrk0SESkSwSn5Sz4ZWnIdOVY8IBl9uR7VWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های افغانستان گزارش دادند پاکستان چند نقطه را در ولایت‌های کنر، پکتیا و پکتیکا هدف قرار داده است.
🔴
هم‌زمان، پاکستان اعلام کرد مواضعی را در مناطق مرزی با افغانستان هدف گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/130783" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b399dce4b.mp4?token=s0ZLqK8qEVy9ARl25_C9os63-bRsfzZGFXR0TNzL1FBpFhiZOu_fxSn0hcJM8hVoJ_7ESjxiXrZojCb9hvHuh5ZdVjE4Xg_KVpvlSxPcP8m1tu-yeHHwxQvuiZKFb3dYxHvET4ToWr9lnPZ0HuQUPwUojVnvfWD2bFxuIlNOicFOZdCiZrArVsVCD3qWwTY5-TRr8gJcSNLJQ1WmKb-WM97nfpb5IJD24B6hDgUMIXPuDyUoDWg8lbffsLhQ4LM3n0xNRDTcutx39XYSr_mlCjGzYoVpWO-zG8iLa1grjYQTyTFfbHtrq5FxWClwCp8bRbr39C0_TPXkVuWPqg95Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b399dce4b.mp4?token=s0ZLqK8qEVy9ARl25_C9os63-bRsfzZGFXR0TNzL1FBpFhiZOu_fxSn0hcJM8hVoJ_7ESjxiXrZojCb9hvHuh5ZdVjE4Xg_KVpvlSxPcP8m1tu-yeHHwxQvuiZKFb3dYxHvET4ToWr9lnPZ0HuQUPwUojVnvfWD2bFxuIlNOicFOZdCiZrArVsVCD3qWwTY5-TRr8gJcSNLJQ1WmKb-WM97nfpb5IJD24B6hDgUMIXPuDyUoDWg8lbffsLhQ4LM3n0xNRDTcutx39XYSr_mlCjGzYoVpWO-zG8iLa1grjYQTyTFfbHtrq5FxWClwCp8bRbr39C0_TPXkVuWPqg95Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تهیه کننده برنامه مشهور تخت گاز (top gear):
ایران به طرز خیره‌کننده‌ای زیبا بود، میخواستم برنامه‌ام را در ایران بسازم اما به من اجازه ورود ندادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/130782" target="_blank">📅 01:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJxjXroshRS-Si5y3_iikrnTrAcVeNxJag_8FtFFbktxIjH0ape-NnwHo_jX95psAmO8-A_CQAXPqR7OfwRDSJ_wEKxAyNPY0gbk0y29BU-ACcZRLrWOzFtiyw52Ytb6y36zyF9r6bENhcqfuRfmnVPJgSR8kSWBTSPaMXrx0FWQn9mnF9sIkju0_bD-Gt9rO1N7raiFWTSAbLa2Y5l4T3TO0Z8WdTNiXzOncAl60ckzOPLe3kv9nMRyAoXMSM8SNO_iaxCinZvWFyF7b30-J7cfXaOEuHrvc6_BmAK81KF542jiyiHFHaeCrnniHYvByHHb1qW8NzlnGmuNoy6Jug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: کشتی‌ها می‌توانند در طول مذاکرات فنی آزادانه در تنگه هرمز تردد کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/130781" target="_blank">📅 01:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP5JVRyKsLZbg7oeAA_a_BmWTbpivNWt8YUttSiusMkbn6HPoYXhxvFoPXeO_fX8cExhWgl1pkEWDgTY65Gg1eU80ryi0PZ2J8D6_t1oDbMr_GOLoCZJd4A9Y85qAAaBu8pyiSOEGSbG6aYagwDJ_vLyTmTkvvV4Yq9ljHc-N3VIIP-x8ipQ__6tB10Pdiv-7AOrhLvN7Q4ZpyqG0GbLOsit0zvyEV6_X2tHjrRnZXp4340D92GUGxt6YLQNJzD66siintZIACtRmWlcjM2R-S85k8uXSSSDmAGaprmjHe-jf2TGJrZZ7yGfD5ITmC91v8T1xOSa4yzHIoDvUA0SKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی: استعفا نمیدم و آماده میشیم برای جام‌ملت‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/130780" target="_blank">📅 00:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOZUMJ_lyRyAFesZGqKfxN7vkQdsYPT-6GJF18G0cERKioziJSahEX2bXcbe5vKMm7h6KH9SVvNu9Sina_pQseyHF04aVDr3eBPRSSZUmq6_v3jgt04b2DT43949szYttGmHAWEGRGaXgTU8iN9Lhh51xWkg-GJk95RASrkd3H8FDh0hqRcYXrlyZG2PzGgWHrIRBEjF69ANQbhF9EMGQdhWpM8VDoV-ZPULeCWYhHCTal1v_-3e9xqfWqIT_2bgDrt_ngFBR5SQMuBjZhrrSOMYXYZjqkWvz7zMxglIGE0PJKDrjop6Hpwp3DSL6O_ZzOggjavtFsNSki_jDLEjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏این تنها بخش کوچکی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراق است.
🔴
‏اگر روزی خانه برخی مسئولان جمهوری اسلامی هم به همین شکل بازرسی شود، چه چیزهایی پیدا خواهد شد؟!
🔴
امروز در عراق بیش از ۱۲۰ نفر به اتهام فساد بازداشت شدند...
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/130779" target="_blank">📅 00:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35ef3b087.mp4?token=hZTRtTmBPcnv6_jZO8aptUQ0GQc-62kVdpJtbJCMkyIJcM1tDDxzSJqKgHQ7UM6JcDWH8bCtcRdxrA1Xy-G9w6KQzWErMFpvVL6TCTg7_mf8p7XRWGOlVkAxauRY56GBtnjxemRjoIYTkcr1QCR5CEXMhd0_jQd1qmokmmX9-cl2mN1jj2Gi0fGALePYdmxwyQKf0qAZ99PtYMbKn-EUKAaz8SMg2Y_Wp_D2C_xEuhIQGYxM_EVyRjb1PSm4l9Gj_N_S_QrlXAtA6bunRSLvhKpGP_MYHbjii3MFfx80TQePrkpkGBPa_9KpdPV8rtHVuKKkuvsPyYKd04O635EZBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35ef3b087.mp4?token=hZTRtTmBPcnv6_jZO8aptUQ0GQc-62kVdpJtbJCMkyIJcM1tDDxzSJqKgHQ7UM6JcDWH8bCtcRdxrA1Xy-G9w6KQzWErMFpvVL6TCTg7_mf8p7XRWGOlVkAxauRY56GBtnjxemRjoIYTkcr1QCR5CEXMhd0_jQd1qmokmmX9-cl2mN1jj2Gi0fGALePYdmxwyQKf0qAZ99PtYMbKn-EUKAaz8SMg2Y_Wp_D2C_xEuhIQGYxM_EVyRjb1PSm4l9Gj_N_S_QrlXAtA6bunRSLvhKpGP_MYHbjii3MFfx80TQePrkpkGBPa_9KpdPV8rtHVuKKkuvsPyYKd04O635EZBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل فراوان تجهیزات سنتکام به منطقه
این ویدیو که ۲۰ هزار برابر سریعتر شده؛ خلاصه‌ای از فعالیت سنگین ترابری هوایی آمریکا طی ۷
روز
اخیر در منطقه است که به شدت مهمات جابجا میکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/130778" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
تصاویر رهگیری موشک‌در شمال اردن
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/130777" target="_blank">📅 00:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس: مقامات آمریکایی به من گفتند که ایالات متحده و ایران توافق کردند که حملات را متوقف کرده و این هفته ملاقات کنند.
🔴
یک منبع آگاه از مذاکرات گفت که قرار بود مذاکرات سه‌شنبه در ابتدا در سوئیس برای رسیدگی به برنامه هسته‌ای ایران برگزار…</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/130776" target="_blank">📅 00:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eef835b390.mp4?token=qGrgD6x3s_WixpRv2DiIReSb-g3Fx6MrmtAFvSyI18zq95o6uQjAwPSOeeACWLlbC6U9QqtdwI-WH_7apRnc1MAMwwk1Ys4fTQxlubQuwSq8jA7vDeM0ktiZiIhteesB9V3vntVNt4Bu0--_GQI6e_ZqmtilRtnlNH4y-kYuXfwfBjTd3Vce6l_ZoCEKZrLbkc2-WxyGDCIyPxHcCo6ugOV9G09NAo6wxNpKfJ27GTEil7lRg6MlcmDm5lXx7nOVKefl8pnwaOyxmUjbOGiXKCzTkFfTITPRqdiB8CMnwSg_S-4nQoD5V5ZnePctVH2tWWCgueXZBNxmJaQkEzghbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eef835b390.mp4?token=qGrgD6x3s_WixpRv2DiIReSb-g3Fx6MrmtAFvSyI18zq95o6uQjAwPSOeeACWLlbC6U9QqtdwI-WH_7apRnc1MAMwwk1Ys4fTQxlubQuwSq8jA7vDeM0ktiZiIhteesB9V3vntVNt4Bu0--_GQI6e_ZqmtilRtnlNH4y-kYuXfwfBjTd3Vce6l_ZoCEKZrLbkc2-WxyGDCIyPxHcCo6ugOV9G09NAo6wxNpKfJ27GTEil7lRg6MlcmDm5lXx7nOVKefl8pnwaOyxmUjbOGiXKCzTkFfTITPRqdiB8CMnwSg_S-4nQoD5V5ZnePctVH2tWWCgueXZBNxmJaQkEzghbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ لبنانی‌ها تو ۲۴ساعت اخیر تو اینستاگرام عربی بالای ۱۰میلیون لایک خورده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/130775" target="_blank">📅 00:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=lIYYe6HVdZeH-gcCrUj0SDTdFKXl9kSEARz9C7Vqco8TrZEVPBwW_54zHhWSPrmGVkzJvVpk-c2MOUK05HATsHaOkFCFUvOJpEqkZ4Ysn1eMNMC_DpmVA685kQT7Gg0AUNjV8JfoUsL_6g2aoquTT_eRk0zlc2BMEBhtJmptKf6VzCpSuSvt05-HK-LmLvTO2KdwTLdx0fTaxRhiBb726GGqrMVgl2QIMujkW5TwGOmwgTgFrulrvK6X0OUDFTGMhfi2T7buQjTt111n5oyfrnugjWuEPHHA1wkz4unKFJ4vN8aR6yzaVSFNiWhmU-4tzvwq9QVPCbsP-A98lrJswg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=lIYYe6HVdZeH-gcCrUj0SDTdFKXl9kSEARz9C7Vqco8TrZEVPBwW_54zHhWSPrmGVkzJvVpk-c2MOUK05HATsHaOkFCFUvOJpEqkZ4Ysn1eMNMC_DpmVA685kQT7Gg0AUNjV8JfoUsL_6g2aoquTT_eRk0zlc2BMEBhtJmptKf6VzCpSuSvt05-HK-LmLvTO2KdwTLdx0fTaxRhiBb726GGqrMVgl2QIMujkW5TwGOmwgTgFrulrvK6X0OUDFTGMhfi2T7buQjTt111n5oyfrnugjWuEPHHA1wkz4unKFJ4vN8aR6yzaVSFNiWhmU-4tzvwq9QVPCbsP-A98lrJswg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/130774" target="_blank">📅 00:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130772">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7lWAWzUzaTmxaV6uhX1kF5ahbojgG8CtASzOUU7g5c_sfxfU19l-qsXVNNs_a_s6G0PIat-rUAoz1LbEcfr_reLFXrFIH4cr-7k6zeVHI3nOB03QUS8cvEGvcR_NyYgPHPDkuVlnSExyTsseFo1IVT79wHqtKZ4f7D9O43ISQpVx41qvXOP4Igoob_JgURzHaxQXQihlkLR71oy95aKbUl_c-OjldJkC2AVxeZ5XW9zHRrGkSvjDdrYH6YBdu7fkD75LWouDe1m38Ys6oFM7QD0NMj6mLPqZA43m24xWjiPGhZRhMXwiYFHbYnW_ViWOfWFhhhHYQiZ0-RHQyTAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس: مقامات آمریکایی به من گفتند که ایالات متحده و ایران توافق کردند که حملات را متوقف کرده و این هفته ملاقات کنند.
🔴
یک منبع آگاه از مذاکرات گفت که قرار بود مذاکرات سه‌شنبه در ابتدا در سوئیس برای رسیدگی به برنامه هسته‌ای ایران برگزار شود. تشدید تنش‌ها آنها را به مکان دیگری منتقل کرد و دوباره بر تنگه هرمز متمرکز شد.
🔴
به گفته یک مقام آمریکایی و یک منبع آگاه، انتظار می‌رود نیک استوارت، که ریاست تیم فنی ایالات متحده را بر عهده دارد، در این مذاکرات شرکت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/130772" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
اگه واسه کانالت دنبال
ممبر، سین، ری‌اکشن اتوماتیک و حتی کامنت با هوش مصنوعی
می‌گردی ارزون‌ترین ربات
کلیکو
هستش
قیمت‌ها عالیه:
سین کایی ۵۰۰
ری‌اکشن کایی ۲۵۰۰
ممبر از کایی ۵۰.۰۰۰
⚡
تحویل سریع
💰
قیمت تضمینی
🤖
ثبت سفارش خودکار
👤
پشتیبانی 24 ساعته
لینک ربات
👇
👇
✅
@ClickooBot
🤖
✅
@ClickooBot
🤖</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/130771" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130770">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ولادیمیر پوتین، رئیس‌جمهور روسیه:
روسیه منتظر ورود مذاکره‌کنندگان آمریکایی پس از اتمام «فاز داغ» رویدادهای مربوط به ایران است.
🔴
لوکاشنکو به خاطر اظهارات تند زلنسکی دچار وحشت نشده است
او با آرامش و تعادل بسیار به این موضوع نزدیک می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/130770" target="_blank">📅 23:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130769">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpNzGiZQkR1tGIsp_Y85uE_hnH4CHAgK_5kT5Zl6i8NeeMcP4ZGIS9OfIV5P1673q-oHHRBUqLtfMnEqBrPIGJuIcikdm0VDUJXEWPMrfDbAnxuXAnuVBz475Mo0TobfdOU5_3H7grsVFdoOn2fjQa3UYjqGrRcLEI8umUeJsAnZ_fzpOVjjwCnWVrkrhmOiqdsn-BxAfMaBCySlPIUIwzEElGy3SF_ftkgu9oZSxR4BWjBHptD1vDc0T4_6xGk7FG1jvE2-i7owrgvF4KSl8TaNz-q1R2YquBVLHBu0NqgANpb4_qv2-K9fmL5n6rhTWbATnP5wl5ktQTV4YTkIYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل در حال گلوله‌باران توپخانه‌ای و حملات هوایی به منطقه عابدین در جنوب سوریه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/130769" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130768">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ارتش اسرائیل امشب عملیات تخریب گسترده‌ای را علیه «زیرساخت‌های زیرزمینی حزب‌الله» در شهر مجدل زون در جنوب لبنان انجام خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/130768" target="_blank">📅 23:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130767">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLpRWNJ0RqZbx1KgXlPWxeaP4QylzaybzZhW72ix_KRgU-_y7N75lqA_NdXKtjedDbu-baHj7WQyCoXaEbBbqSXgB7ZANDPnLkFNAP1BrZWss3yOWfOufGpos2qtZ6rhH-1HTiw76qREu987KRDRr3rH2h6uP5oe4P44ERUGpnmPki5q6yeUK3RQaLj86qHfS3fQKFGUq9dUbNbHG4U_2aExUVFR-5yv9tYBRi0lEgkUiW5JKHaBUUGe8H-aKjoLRv2ShHlQzMTYxGX7Chf56YwGT_pAVTAO4s6TvxdS06WHsbYGb2VnyiwnF2Xu74HQ3uVzVo4Ll_zdJHR52x2zdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر رهگیری موشک‌در شمال اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/130767" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130766">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل امشب تخریب گسترده‌ای از «زیرساخت‌های زیرزمینی حزب‌الله» در شهر مجدل زون، جنوب لبنان، انجام خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/130766" target="_blank">📅 23:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130765">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
میساکی باز هم توهین کرد: کسایی که برای خوشحالی گل شجاع کلیپ می‌سازن همون جای خالین @AloSport</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/130765" target="_blank">📅 23:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130764">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
یک مقام ارشد آمریکایی به الجزیره:
کانال‌های رفع تنش با ایران همچنان برقرار و فعال هستند
🔴
گفت‌وگوها با ایران لغو نشده است
🔴
مذاکرات فنی برای اجرای تفاهم‌نامه با ایران همچنان طبق برنامه قرار است در روزهای آینده برگزار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/130764" target="_blank">📅 23:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130763">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803cd79e57.mp4?token=Y8h2xGHTZd8SY3REEY8hPMyjustue3gIibrtrgtfnA5HP-Lg-KGAI9YgVPNCtzbHzkQ1faPddH5QgOc9W-uxMfLizuIIz0Wgn3eRDjDPQLQ7TR79hd9jl2qNqwYVKkWe2HNdn_xP1G5IL7iSsPiWi1nSlfT4uJzddVPjCUPcQ-DKiIrSqwDs93ccHwM2nka15tDem2GOWDnxiTwbNp1kWYGwOCF046PjDi6dWJMh9ymeheICtJtySc-3RdzSlCR34CREWUpbV0_tMm5J7noKICgbJQsMU6jtytBw-6ebG54lOvWesLBTSdv-3JC7T0MWi6EnLHn3s45KoGaezlkh-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803cd79e57.mp4?token=Y8h2xGHTZd8SY3REEY8hPMyjustue3gIibrtrgtfnA5HP-Lg-KGAI9YgVPNCtzbHzkQ1faPddH5QgOc9W-uxMfLizuIIz0Wgn3eRDjDPQLQ7TR79hd9jl2qNqwYVKkWe2HNdn_xP1G5IL7iSsPiWi1nSlfT4uJzddVPjCUPcQ-DKiIrSqwDs93ccHwM2nka15tDem2GOWDnxiTwbNp1kWYGwOCF046PjDi6dWJMh9ymeheICtJtySc-3RdzSlCR34CREWUpbV0_tMm5J7noKICgbJQsMU6jtytBw-6ebG54lOvWesLBTSdv-3JC7T0MWi6EnLHn3s45KoGaezlkh-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از میفدون، جنوب لبنان، پس از یک حمله هوایی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/130763" target="_blank">📅 23:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130762">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40133fcdb1.mp4?token=enzBc4UZjjp-1FHuOKUyAHXf-eXi8WtHt5avwGId9EXmFwP_WP7U8buk3pfM3tDmD9ZVcV9QyUa-SfV4K1G-_YckFFoDsE0QDgNyIdST96Pbab2TswBqHA7rL4iX3WP1uqRH2PSZQOnW5KVDrgusNQmR5IFKL9b3RHZex62oYcoa6ls8qULAGCGu6v2Ykq2Ln0hcOHhEHKBtsEW_sHH4iqhZDQSzvKJrcSy6nWpe4H6-5gGCY819_VHrQ8QujOArs1hQRE6A-jYL9q_omh7j_k6qk9Fsu-bDusowWSk4sXdcKCBecf3Lqv8qQsGpxD9qRMx7smJt2S7QS8Ts4oglN51YcK9RHQX0BYshlOrcmV1bfXDGQhKVyOTvQ_wcxYRhRgAw7QhAj8iWrUAv6ZB8a9rFz1fV19wuHp5IA4IqW0uuLdBVfHc1MrwoA6Sd9JpEqy4mrssr5ciXxFPQ8chkBkj7pzsyCf2hLmGVXdFsUlwYhy6uC5jnqmSc45kzlerIEQCVRVZ-GVknrKczUkGpoUGh2QR62oFGIXLClR0q9BuL_QtUFp5ehFVxOajEXXr27ADrgGazkHaC6ugu2xv5_WMG54mjzF2_uUthgcMJeleKrjRn_vIVzF9PaBSrkHDS713nhuEVrbCb3DUnaSXL76zf2eoIfHIj-mzNdBIcqgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40133fcdb1.mp4?token=enzBc4UZjjp-1FHuOKUyAHXf-eXi8WtHt5avwGId9EXmFwP_WP7U8buk3pfM3tDmD9ZVcV9QyUa-SfV4K1G-_YckFFoDsE0QDgNyIdST96Pbab2TswBqHA7rL4iX3WP1uqRH2PSZQOnW5KVDrgusNQmR5IFKL9b3RHZex62oYcoa6ls8qULAGCGu6v2Ykq2Ln0hcOHhEHKBtsEW_sHH4iqhZDQSzvKJrcSy6nWpe4H6-5gGCY819_VHrQ8QujOArs1hQRE6A-jYL9q_omh7j_k6qk9Fsu-bDusowWSk4sXdcKCBecf3Lqv8qQsGpxD9qRMx7smJt2S7QS8Ts4oglN51YcK9RHQX0BYshlOrcmV1bfXDGQhKVyOTvQ_wcxYRhRgAw7QhAj8iWrUAv6ZB8a9rFz1fV19wuHp5IA4IqW0uuLdBVfHc1MrwoA6Sd9JpEqy4mrssr5ciXxFPQ8chkBkj7pzsyCf2hLmGVXdFsUlwYhy6uC5jnqmSc45kzlerIEQCVRVZ-GVknrKczUkGpoUGh2QR62oFGIXLClR0q9BuL_QtUFp5ehFVxOajEXXr27ADrgGazkHaC6ugu2xv5_WMG54mjzF2_uUthgcMJeleKrjRn_vIVzF9PaBSrkHDS713nhuEVrbCb3DUnaSXL76zf2eoIfHIj-mzNdBIcqgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین: ایده ممنوعیت کامل صادرات سوخت دیزل در حال بررسی است
🔴
اوکراین چند هفته‌ای است که به صورت سازماندهی شده به مخازن سوخت روسیه حمله می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/130762" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130761">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQI8zrdk75uHaIULFlWXXT5IpJc0-Z6GiPUWvjOOIHlXqEh3cFZ4OEIYmObk3wbN83fe5i-U0tCTDvPu_ClGOjSqYXI7wLNyeupf8Zo5LWXYQQO43xJ8kkds0kFx52VYX2RfEFuKt-SawJLjhLob6BINM68__bDS7UFnzpupAYMHnRPNUnyYCtwUjlQPtaBrrI6w7xs6_A6Dni0ipwUDV0NIx993iEyenWJ6p52twuyh_nMdcfA0Ww-TbsxnhBP-zIgq3wIcsUgyDegqMuFdfw6V1H9AsMzqmX078mm_NAAegSz8l6M6SdJ0bpNwIbMslIuBWCT7Ef2hGCdcR-A4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندی پیش حملات هوایی اسرائیل به میفادون و نبطیه الفوقه در جنوب لبنان انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/130761" target="_blank">📅 23:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130760">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
آتش زدن نمادین متن تفاهم نامه توسط یک مداح تندرو و جنگ طلب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/130760" target="_blank">📅 23:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130759">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فضائلی، عضو دفتر حفظ و نشر آثار آیت الله خامنه ای: امروز قرار بود مذاکرات فنی برگزار شود که ایران آن را لغو کرد و شرکت نکرد که دلیل این امر درگیری‌های این چند شب گذشته بود و دلیل دیگر این است که منتظر اجرای برخی شروط هستند که مثلا امکان برداشت پول‌های بلوکه شده است یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/130759" target="_blank">📅 23:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130758">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / نایا به نقل از رسانه های سعودی:
رهگیری موشک ها بر فراز شمال اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/130758" target="_blank">📅 23:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130757">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
طبق اخبار و تحولات موجود، بزودی جنگ آغاز خواهد شد مگر اینکه اتفاق دیگری بیوفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/130757" target="_blank">📅 23:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130756">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
منابع خبری از حمله هوایی جنگنده‌های اسرائیلی به شهرک «میفدون» واقع در جنوب لبنان خبر دادند.
🔴
تاکنون جزئیات بیشتری درباره تلفات یا خسارات احتمالی این حمله هنوز منتشر نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/130756" target="_blank">📅 23:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130755">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نیویورک‌تایمز: مذاکرات لغو نشده است/ روزنامه آمریکایی به نقل از یک مقام بلندپایهٔ آمریکایی مدعی شد که مذاکرات فنی با ایران در خصوص چگونگی اجرای تفاهم‌نامه، کماکان برای روزهای آینده برنامه‌ریزی شده است. وی با اشاره به تبادلات آتش اخیر میان ایران و آمریکا تصریح کرد که هیچ گفت‌وگویی لغو نشده و ارتباطات همچنان برقرار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/130755" target="_blank">📅 22:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130754">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
پوتین: نیازهای سوخت کریمه برآورده خواهد شد و در حال حاضر چند روز ذخیره سوخت در آنجا وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/130754" target="_blank">📅 22:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130753">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پوتین: حمله‌ها به زیرساخت‌های انرژی روسیه باعث ایجاد مشکلات می‌شوند — این واضح است.
🔴
کمبودی که از حملات نیروهای مسلح اوکراین به زیرساخت‌های انرژی روسیه ناشی می‌شود، وجود دارد، اما حیاتی نیست.
🔴
تمام تأسیسات انرژی آسیب‌دیده در روسیه به سرعت در حال بازسازی هستند و همه چیز با حاشیه ایمنی بزرگ در حال کار است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/130753" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130752">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4fcf308f.mp4?token=X87ar6fjVtZRUHu6x19-anVWRXw0AzTBhRURIBUtBnLPoqUFkTb3RMKyiySxre1UStMCn05PEPJ8Kd7WuLryCYy1GmdSMUpIHByUgqfStaL8Qv5EfsUKaLlU6W9EzQ8AiAerbQq_Yk8-zcSqDrs-kA5AG9uYJ0XDqkJgu1Sn-7lH5GdCgefQNtN6Mn7dP1GCwwOW2E3nlUztnCsiQ6wHdmFxra-QtNDOc8LvPmNyweuj8LJqD9TR-w40Z1ZKkzZT9afkjvVAUzo0O_QlvqfmLSvxlz3jMJvcM4Qz6sPtxr0KsWJk5TaJSPZkCSgQV0Fn-MfAe64xJ38us-GQb7i2ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4fcf308f.mp4?token=X87ar6fjVtZRUHu6x19-anVWRXw0AzTBhRURIBUtBnLPoqUFkTb3RMKyiySxre1UStMCn05PEPJ8Kd7WuLryCYy1GmdSMUpIHByUgqfStaL8Qv5EfsUKaLlU6W9EzQ8AiAerbQq_Yk8-zcSqDrs-kA5AG9uYJ0XDqkJgu1Sn-7lH5GdCgefQNtN6Mn7dP1GCwwOW2E3nlUztnCsiQ6wHdmFxra-QtNDOc8LvPmNyweuj8LJqD9TR-w40Z1ZKkzZT9afkjvVAUzo0O_QlvqfmLSvxlz3jMJvcM4Qz6sPtxr0KsWJk5TaJSPZkCSgQV0Fn-MfAe64xJ38us-GQb7i2ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ولی ما میدونیم چرا!</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/130752" target="_blank">📅 22:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130751">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
یک مقام ارشد دولت ترامپ امروز به رسانه‌ها اعلام کرد که مذاکرات میان آمریکا و ایران که قرار است آخر هفته جاری در سوئیس برگزار شود، همچنان طبق برنامه انجام خواهد شد.
🔴
این اظهارات، گزارش پیشین روزنامه وال‌استریت ژورنال را رد می‌کند؛ گزارشی که مدعی شده بود این مذاکرات به دلیل دور جدید حملات متقابل ایران و آمریکا در منطقه خلیج فارس به تعویق افتاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/130751" target="_blank">📅 22:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130750">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6cf47261a.mp4?token=vryEETwhkVsmcNyZ5ldakO2tHopK7sUzV4bUNsAxOAEX5Zr1Ohx7AS3roQRgI_oa-hqExaFnp2dJZD3AuDDZXWFRMc6tLRjMZjjwTSryRyzVkWSCAYTLsE5uOoJs1_6g6EWolwtMjRfec89MWxFpITVR7fSTsI1FajC_LYcQ2QCFSLf-0vzHAjA3skziMBweU6DXySDueTR5p6Q5UnjG1STzXJHG08cmQVZgHpYbgbAS4epiFbbL3SPtEwqBwv_M5KmYmqVFPkYa0g8OuzMSBg-lp4ene4C-AY7kUzlo2VvxNL8sH_dDO2DHRLCSfGs_QQHuiAfne-KCm45fnx6I1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6cf47261a.mp4?token=vryEETwhkVsmcNyZ5ldakO2tHopK7sUzV4bUNsAxOAEX5Zr1Ohx7AS3roQRgI_oa-hqExaFnp2dJZD3AuDDZXWFRMc6tLRjMZjjwTSryRyzVkWSCAYTLsE5uOoJs1_6g6EWolwtMjRfec89MWxFpITVR7fSTsI1FajC_LYcQ2QCFSLf-0vzHAjA3skziMBweU6DXySDueTR5p6Q5UnjG1STzXJHG08cmQVZgHpYbgbAS4epiFbbL3SPtEwqBwv_M5KmYmqVFPkYa0g8OuzMSBg-lp4ene4C-AY7kUzlo2VvxNL8sH_dDO2DHRLCSfGs_QQHuiAfne-KCm45fnx6I1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک والتز، سفیر آمریکا در سازمان ملل:
اگر ایران فکر کنه ترامپ قراره در برابر ادامه حمله به کشتی‌های بین‌المللی دست روی دست بزاره، کاملاً در اشتباهه؛ چون همین چند شب اخیر نشون داد که این کارها رو بی‌پاسخ نمی‌ذاره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/130750" target="_blank">📅 22:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130749">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
آکسیوس: آتش‌بس شکننده ایران و آمریکا در معرض فروپاشی قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/130749" target="_blank">📅 22:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130748">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLyhB7-XERl0jkQq9wBHEarYxwWudNs8oz-QoqFVcHG5gmg26RhulPQ6a0FfTYexkd6zVZu0T8KsPuONj_CtlR3CbmAO1lysmwRr26mlhHzjN4i1kZIvZGnTSOoe0BxPOCSyirAul5UKzr9z1OUIYfHPwKc_lcwD73TVXQwq8vD95YrpG6cDJVgvG-6xVCXoH_8w_0IW2hjOUGiuietHgmAuoDw-7s2vRggtoYDgCY90m8WEnNg8No269uKlo_1BYtOKNp_x_YqZk1wrCcbPQ6KorMpY6OYADcpUJFecKjh3FSPEEKOJbzeFZLWBK4YWBMIoGwn55JTZFDIaS-bPBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت تتر در ۲۴ ساعت گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/130748" target="_blank">📅 22:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130747">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96c68e7570.mp4?token=rxFRZK1tMXQTPyqRRM1XmoRQ4bXvVErSnjtucQChvFDb2GFd1Gr6XuJ2vKdJrJr6K_Aj_h8LvbnlCMHwx_6gRGfpjPiL5LjXui9vjA2oUdL0jtbgYaPT5d94dNaZmiaWXbq7BrFOvaBmTc9EYJWp7xhxHwsPkSnO_LJ9GQIETriOb8uI6SmEK5VyQ1F0QNZ7KrfHIjXBZCmT54S0-d-1fj8y2EUpH1c80hdxeU2j5Ow7Xery8DttrCe9T7TTyKeKEse2GrRApg4oV7ppSv5c6RkKE_I3qdXuCVLZ01aEf0gni_ovV9gkxoLIdOFwJp1yLoqUkNmlR0c-UYI24x_tSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96c68e7570.mp4?token=rxFRZK1tMXQTPyqRRM1XmoRQ4bXvVErSnjtucQChvFDb2GFd1Gr6XuJ2vKdJrJr6K_Aj_h8LvbnlCMHwx_6gRGfpjPiL5LjXui9vjA2oUdL0jtbgYaPT5d94dNaZmiaWXbq7BrFOvaBmTc9EYJWp7xhxHwsPkSnO_LJ9GQIETriOb8uI6SmEK5VyQ1F0QNZ7KrfHIjXBZCmT54S0-d-1fj8y2EUpH1c80hdxeU2j5Ow7Xery8DttrCe9T7TTyKeKEse2GrRApg4oV7ppSv5c6RkKE_I3qdXuCVLZ01aEf0gni_ovV9gkxoLIdOFwJp1yLoqUkNmlR0c-UYI24x_tSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر GTA6 رو پیش خرید و دانلود کرده، این به کنار، 175 گیگ رو تو فاکینگ 10 ثانیهههههه دانلود کرد
😐
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/130747" target="_blank">📅 22:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130746">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
یکی نیست به طرفدارهای تیم جمهوری اسلامی و رسانه‌های همیشه‌طلبکارش بگه حالا که افتادین تو فاز «تبانی شد که تیم‌مون صعود نکنه»، اول یه نگاه به خودتون بندازین.
🟠
تیمی که سرنوشتش رو می‌ذاره دست نتیجه بقیه، حق نداره بعدش برای دنیا مظلوم‌نمایی کنه. اگر عرضه داشتین، تو زمین کار رو تموم می‌کردین، نه اینکه بعد از حذف شدن دنبال سناریو و توطئه بگردین.
🤔
به بدترین شکل حذف شدین چون دعا یک ملت باهاتون نبود.</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/130746" target="_blank">📅 22:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130745">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iidgsiMAvWb3PKZHHsHLy-OZRZClLcML-TbECipa5pRrmr4lqC9Kcfq13yyUQpyTi3nrpjMMRU-x9GAB_qJcosrJopawqeNUAE7ZS-bldr4zGg1vjcOAFg-dk0a_gZOCGkJnI_orEYv4iugQjCbqXCma0fYflxycDWGvz8pehCtvPzy4JoY94EhMrpEq5Uy2zT3JGX1ecF2-cd6J8v09QsfdOHlXob1qrJhfSzChfmmRkG2yt6X07hx1_LZk8qK_HY0boEGO3NzpZJ_jah1BHCNaTigrL_D1DQsx_7_eakSDl3se9cbdadB4kC_7X5khHGrCHvZA3ImJQ-XnjD5dXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدول بیشترین شانس قهرمانی در جام جهانی ۲۰۲۶
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/130745" target="_blank">📅 22:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130744">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
والانیوز عبری:
اسرائیل در حال آماده شدن برای احتمال حمله مستقیم ایران است، پس از امضای توافق لبنان و اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/130744" target="_blank">📅 22:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130743">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63c51b823e.mp4?token=GLRK1kL7oj7FCcPEEh7SdEqb00iNhzO0_1crcRehJuxH3C32c841OHoJvBL7Ep5DpjakpCE4Y9oRWuoqyakiHdkXZLe0wlZ2A0nZSPAlsU8ZgIeXN50SkzaDewYgq8D4kceYKusK9Vkp4pM8fRCeCv3NjECI2LBi7hlTaT2LWP91w31EwJMBeBXzGYJj7aili_BPRgYM3qoLc0rz6U0-bPlZ_zRVKdhQMz5TnWniIE5eIzMWrZHRUUoz1d75U_9OqU-jGf6ywIzQzfDaHHzZWCzGcQ0PfQR-e2p5flVS1guxl8crNbieZds1r-0LttameKXS8eHc4imGfSIfa5q5kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63c51b823e.mp4?token=GLRK1kL7oj7FCcPEEh7SdEqb00iNhzO0_1crcRehJuxH3C32c841OHoJvBL7Ep5DpjakpCE4Y9oRWuoqyakiHdkXZLe0wlZ2A0nZSPAlsU8ZgIeXN50SkzaDewYgq8D4kceYKusK9Vkp4pM8fRCeCv3NjECI2LBi7hlTaT2LWP91w31EwJMBeBXzGYJj7aili_BPRgYM3qoLc0rz6U0-bPlZ_zRVKdhQMz5TnWniIE5eIzMWrZHRUUoz1d75U_9OqU-jGf6ywIzQzfDaHHzZWCzGcQ0PfQR-e2p5flVS1guxl8crNbieZds1r-0LttameKXS8eHc4imGfSIfa5q5kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم‌ پهپادی از خسارات گسترده‌ در لا گوئیرا در ونزوئلا پس از ۲ زلزله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/130743" target="_blank">📅 22:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130742">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668abf668f.mp4?token=Lip9534otzUlNBl_N7UsNwP2gAqe7uZ1OQP81ZKjmghaS6DSRYOaCZ9xO0dCoQtic6cgTtloiEkhBZIT_myABg7q3u-21T_WhlwlExZsOevnkOdJuRmznkh7kEKhuUbR0JopBB_gPIdmoiRsH4VX_m5wgvCOybYKLNJnIJDrihDKd3U1b2J1udFN1LHmCYgmbiYqyz6YMKMt5YKpaN6JZFRAxKIH8atVaW1sDaJrtQYnF8PChi3Qyj3D1-DRsoiKwKySlPH15v1H0GEkF6k4Ps3V3CN6qfqzLc8ec75O1-sRkSeQG4aSUCLeziInPc-gU7Myea7g4mxuJvf1i97K8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668abf668f.mp4?token=Lip9534otzUlNBl_N7UsNwP2gAqe7uZ1OQP81ZKjmghaS6DSRYOaCZ9xO0dCoQtic6cgTtloiEkhBZIT_myABg7q3u-21T_WhlwlExZsOevnkOdJuRmznkh7kEKhuUbR0JopBB_gPIdmoiRsH4VX_m5wgvCOybYKLNJnIJDrihDKd3U1b2J1udFN1LHmCYgmbiYqyz6YMKMt5YKpaN6JZFRAxKIH8atVaW1sDaJrtQYnF8PChi3Qyj3D1-DRsoiKwKySlPH15v1H0GEkF6k4Ps3V3CN6qfqzLc8ec75O1-sRkSeQG4aSUCLeziInPc-gU7Myea7g4mxuJvf1i97K8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤴
تو این روزهای فوتبالی یادی کنیم از  افتتاحیه استادیوم «آریامهر»
🤔
اون زمان کشور های حاشیه با شتر اینور اونور میرفتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/130742" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130741">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEdEZazKX0kQLl2IJN4Ut0LzwGWOefDi8JjbJ79rT3Sbjc0atGgbVQEKR15CBfjcPZAU-9j3TD0lu3C2q5rws28Pk1KNb_KJ3x-kpTiGJ-eabCoCoduDQPQXMKof-0LAWQBhVnNZgSfLgcoVd9aqGksdgWaErTJ38bL9eiJHv46rXDyQW73_eeIvV-55vGF8_hD_oJsTDeAvdZUbscVRnLXe3MZU26BdmsteCV-0pDBhmLGjhm-CZlQ-pzndtEdeogpGsjcgJUIq7g08gwdb4YlE81ZntAGX3d5uxpmpRtl808csgcH5G9vPKXsLFq7kkMmhw2N_FkZguphTlOQE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت و عملیات پر شدت هوایی بر فراز منطقه خلیج فارس
🔴
از آواکس آمریکایی تا تعداد قابل توجهی سوخت رسان و جنگنده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/130741" target="_blank">📅 21:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130740">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
منابع عبری : افزایش حالت آماده‌باش در اسرائیل به دلیل نگرانی از پرتاب موشک از ایران به سمت اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/130740" target="_blank">📅 21:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130739">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjsQLkBOa8o4K0xyeQTrTdLKSDRv2Poe_kTojym9JxmfExjukBssc0TQx9_7Y524IIv7beX6zjz6sPxILVBNi6vsuQlv_m-MkmMA-3HAGqrg13ESYbP34LpHtgIAjzcSPs-TCnYHAQSiuulYxp8kBISGs6VVaBTnzIYAJjTU3-HIgpaALuRqDvbsEMRCQ3NPxbc1XSc-9aRpx7E7jw_GpHWLoIG0SfhcX5lAFHogrry9z0vBVZ9VneFye8oAeRUkT1u0Uf-wkA5NU8EhBHosGlLr5LGFl2cfWKBNKqlORpFh88NywHYdLl3txkHEyNxVz0LwMLnHu_42tn02NXFQ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس :
آتش‌بس بین ایران و آمریکا می‌تواند نابود شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/130739" target="_blank">📅 21:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130738">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ea40def.mp4?token=gmQbkjifes3Xf74IyJ397gk_lSX6om2YwkAR752vN1dYCVfbGfEscquz4uVkVW7VU3Smv77RvmwvlmwILA6RmVutEIXINhaFuxDzSm0zSvmaNf7CqJxjCwyA9C4m3CtZiSxXqykEfHtBsd-FeJTkKGCiXgj16JdSpwwkyxVQuW_noexUS-3VCswMjErFgmnIUtT5qqV1g4rsr70L8Y_PtYYvC94Xeqf1i746oOqyMHUIlYvBhaAViJ2e-aNmORhHiODrazCVlVj1W8bi8wVfPXmwwKSuTgcSBuLfKnGrDDyM-1KGq8gmqoIGk2jW75YOVVeHqWz6A2fW3nfnVtJQTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ea40def.mp4?token=gmQbkjifes3Xf74IyJ397gk_lSX6om2YwkAR752vN1dYCVfbGfEscquz4uVkVW7VU3Smv77RvmwvlmwILA6RmVutEIXINhaFuxDzSm0zSvmaNf7CqJxjCwyA9C4m3CtZiSxXqykEfHtBsd-FeJTkKGCiXgj16JdSpwwkyxVQuW_noexUS-3VCswMjErFgmnIUtT5qqV1g4rsr70L8Y_PtYYvC94Xeqf1i746oOqyMHUIlYvBhaAViJ2e-aNmORhHiODrazCVlVj1W8bi8wVfPXmwwKSuTgcSBuLfKnGrDDyM-1KGq8gmqoIGk2jW75YOVVeHqWz6A2fW3nfnVtJQTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
میساکی باز هم توهین کرد: کسایی که برای خوشحالی گل شجاع کلیپ می‌سازن همون جای خالین
@AloSport</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/130738" target="_blank">📅 21:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130737">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">حذف شدن تو یه مسابقه میتونه طبیعی باشه اما زجرکش شدن قبل حذف یعنی اینبار اسلحه دست خدا بوده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/130737" target="_blank">📅 21:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130736">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
دنیس راس فرستاده ویژه آمریکا برای خاورمیانه در دولت‌های جورج بوش پدر و بیل کلینتون: ایران در تلاش است «مدیریت» تنگه را به اجرا بگذارد. تنها دستاورد ملموس تفاهم‌نامه، بازگشایی تنگه بود که در ازای آن ما محاصره را لغو کردیم و به ایران اجازه دادیم نفتش را به دلار بفروشد.
🔴
می‌توانیم به تبادل نظامی ضربه در برابر ضربه ادامه دهیم یا محاصره را دوباره برقرار کنیم. گزینه دوم را انتخاب کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/130736" target="_blank">📅 21:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130735">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
منابع دیپلماتیک به روزنامه الجدید لبنان گفتند ایران چارچوب توافق اسرائیل و لبنان را به رسمیت نمی‌شناسد و می‌خواهد اسرائیل را مجبور به عقب‌نشینی کامل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/130735" target="_blank">📅 21:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130734">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: دولت لبنان از واشنگتن خواست که پیوست امنیتی مخفی را در چارچوب توافق با «اسرائیل» منتشر نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/130734" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130733">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_q__-Jybsessy2kFTRpxw3GWei1f9oGHyCFpksUp7GkoKgDDRQET9krXg49PgYnFyJjagXty7d-eacA6xDlj6R_Ak8amc4w6Eqo6RmzpBFlWavaCvu-S6lVkK-E3C1MUlwUxJaLWvLS3yHaTQRnASdYQr5Hgp_GISyX6BNzPNVzhr4V2o7iAu8kI18aoe46Ker3EFf0hFB6jhP8jewbasoDB0ID6gSOahjAaL2v4BKb2sgwepCQnvVolkWMyJnE7POWEgGEIRjR9Aq8JFMCu2c_I0rCEO3bsrSPHxqha7ofgoIRERrKv5b502CDEmgTl4ncnXnhOw20eBdtCsJDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت کشور قطر اعلام کرد تیم‌های جستجوی دریایی پس از عدم بازگشت یک کشتی در زمان مقرر در این آخر هفته، آن را پیدا کردند و تأیید کردند که یک شهروند قطری پس از اصابت ترکش از «عملیات نظامی» در منطقه کشته شده است
🔴
یک ساکن عرب که در کشتی بود زخمی شده و در وضعیت پایدار به بیمارستان منتقل شده است
🔴
مقامات تحقیقات در مورد این حادثه را آغاز کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/130733" target="_blank">📅 21:10 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
