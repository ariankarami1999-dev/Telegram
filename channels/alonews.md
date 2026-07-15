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
<img src="https://cdn4.telesco.pe/file/dwZbFyAdL54vlTBLUUxV0mghyeE0dOLbv4XHH1_Xn9lDEwb1L5yhzv_wRnHqPIUeyhwzm6zpPthsNI7CFw6_XDqJRb8wux9jU7TVh3DxkptjTWRGIWr0Td_fFn_F1_QCIHNoz8fF3KDaGSVH2aL0hfJAdZH-rLqyrnrnN2bEk1yYRmNSnGNmd-xdEcrruSd5d-I0ARstqwRkSI-R33_jmQb-neA9CxYGiFuSy5d2_sgXA8hPXa1-Ko7f0fjTCvgh2evvfTTlzlsjt0gewOaM4uCabowKDnxwpMVgOSWmqeMmQIXdwfgmIzYDuvGcorpwJqHrjEBZSHUGASY9YDiFvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 21:13:29</div>
<hr>

<div class="tg-post" id="msg-134498">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
قالیباف: مذاکره در این مقطع همان‌گونه که بارها اعلام کرده‌ام معادل سازش نیست، بلکه در کنار جنگ،  بخشی از راهبرد مقاومت و صیانت از منافع ملی است.
🔴
این هماهنگی و استفاده همه‌جانبه از ابزارهای دیپلماسی و دفاعی، برای حفظ ایران عزیز نه تنها یک وظیفه بلکه یک ضرورت اجتناب‌ناپذیر است.
🔴
جداسازی و انتخاب یکی از این دو روش  به‌عنوان تنها راه حل، خطای راهبردی است.
🔴
ما در جنگی پیچیده با بزرگ‌ترین قدرت مادی جهان مواجه هستیم و در این جنگ افتخارات بزرگی کسب کردیم؛ پس باید فکر و عمل ما همان‌قدر بزرگ، پیچیده و مقاوم باشد.
🔴
این مثال را می‌توان در مورد  لبنان، رفع تحریم‌ها، آینده پایگاه‌های آمریکا در منطقه و انتقام وخونخواهی رهبر و سایر شهدای این دو جنگ تحمیلی هم تسری داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/134498" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134497">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY5E2sGLxExHPvU5Eap6B8I5TSjjVWVHCBfWU4E3GNtu-y8mXJEwfX88FKTyx9tqzrwpptSCQJ4h5XINYjBazFeigUu8lcBiNVw2q8pY6gTFu4eDvZN6FH5HWuu7Pd9eg7VTS4kgh06FoMRMKu-cgKptSqQarWifBPp5jgZSBG_pEbapGvJ9tiG6ForyzD7Esbw9UMkE2vcbL2T_ahX92HVq6dbolyhM7ckpgI86hEUbGJikQ8DoyD3UtvA08tr_sslA1_W7V71bU6TQgy2-tB_S12a0M6ti8y49xGM4U5d99iekULGFb-QOPP8FEM4rRtm1UeIXdGP41-f01aVW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیرنویس شبکه خبر :‌ وزارت آموزش و پرورش از برنامه ریزی کامل برای امنیت حوزه های امتحانی خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/134497" target="_blank">📅 21:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134496">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
قالیباف: ما باید بتوانیم بین دو روش نظامی و دیپلماسی، هماهنگی ایجاد کنیم و نباید از جنگ یا مذاکره هراسی داشته باشیم؛ جنگ و مذاکره دو  روش حفظ منافع ملی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/134496" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134495">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
قالیبلف: با شروع جنگ تحمیلی سوم در اسفند ماه، نیروهای مسلح ما کنترل خود را بر تنگه اعمال کردند.
🔴
در طول مذاکرات نیز ایستادگی و ترتیبات ایرانی تنگه هرمز را در بند ۵ تفاهم‌نامه تثبیت کردیم و آن را اهرمی برای اجرای ۴ بند دیگر ستانده‌های خود، از تفاهم‌نامه قرار دادیم.
🔴
حالا هم که به مرحله اجرای تفاهم‌نامه رسیدیم،
آمریکا که به لحاظ حقوقی و دیپلماسی دستش خالی است، می‌خواهد با زور ترتیبات ایرانی را کم ‌اثر کند، ولی ما بر پایه دستاوردی که در تفاهم‌نامه به دست آوردیم، باید بایستیم تا حقوق ملت محقق شود.
🔴
دشمن برای جبران شکست خود فشار وارد می کند ولی ایران با اتکا بر قدرت خود اجازه تحمیل اراده دشمن را نخواهد داد.
🔴
ما بر خلاف جنگ ۱۲ روزه، به درستی در جنگ ۴۰ روزه تنگه هرمز را بستیم چرا که باعث ناامنی و به خطر افتادن امنیت ملی ما شده بود. امروز هم امنیت ملی ما در حفظ «ترتیبات ایرانی» بر تنگه هرمز و عبور و مرور حداکثری ایمن و بی‌ضرر کشتی‌های تجاری از این آبراهه است تا برای ایران امنیت‌ساز شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/134495" target="_blank">📅 21:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134494">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4HqCVsGvJZVdnNrSCScSsuwa89b_jPAXLrlskNoXPlcOqXvAH6BCSO41XhRVPaHPqO7zHrM7VQpNj_w-_QezFnLaaOkXj-eb4Fs179boROCc0L-jRuhDGOYPMaS6_XHpnRxMFQPIz6Tf8jNcrswbrQ5iwdJDyGEMrU9QLKuZJYG__q6zvgimh9CLz_2jmOJWYvD6YykiKNELrg0KXSaIrxAWWnfEjBk_QeOUTMSTT-wctJSghjGjMnhgvuFe1jCY_XpW6wDFbeOEi1994mh9NAVvEgqToRVNTK4vIbiahMtc5hUqO29Pj_a4NwN-LsmvSSpUaliDWifHd5YdbyndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت یوسف پزشکیان درباره موضوع انتقام
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/134494" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134493">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
قالیباف: تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد
🔴
اگر قرار باشد ایران از تفاهم‌نمامه انتفاع نبرد، دلیلی برای پایبندی به چنین تفاهمی نداریم
🔴
باید همواره آماده نبرد باشیم و در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/134493" target="_blank">📅 21:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134492">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
قالیباف: نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد. لذا راهی جز تکیه بر توان خود و قوی شدن نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/134492" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134491">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
قالیباف: آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/134491" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134490">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
قاليباف: ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/134490" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134488">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLt-DhRabEGngxiz2pcjxGgXvUx68WpPEMrMEtMp1yELs6aYqB5hfITVzDRPpVGcw5Eq98nb-P7oBRhQjAn4kbXImH5DVNkADu2AjErWn-FQo0cU2MIzIymTG_tOLJNo353qFUrWcLw7sqQx8BYislK4QwXMtSt66tWTGP7PRGfYipwvA7qaeRS3S10yCUtc-IARuEKWDSf7aw-6qpckJgYM2SkSuC7Xo2HCNh-1JcAiUB1-AAin3_fJyGC5TEjGU94HAo4ukq4zxVbVUDzHJQAiDzHsHE8Ay8Q7acL3-u9zgcg90opWKnuRoFnQ_UQE_lJJ7a2vL4EtbYpQ02mG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFL39BXQ0b6BRrwmfvtqC9O5plI49P1lIlBeQXny7AreEJz6wv_zs9n_QfaLdz3-2wRM4_6R97VC-EEXII7tNDyBF5-op-L3bVxqVa549uz44GkX3HzoGLQcNYoHf39fCkqOIDoN_v8fH8rpXYRArsJQhNDUDDBfRqN1PnbDE_97SWyIMq4SBerHn5DFBwIOOqab6zMQU9v-SBciEbXX2s1R09iHJ-Auhhxsw0OCzi5Ef2hcTzX_6ImElWlgZ4hA6DcJ1w1m7lWhHhybicq2J0fKT8wDtjYyKg3Yd26thzmHpbgpqOqGvDX37uX0wHRVhCPoUjplZ_k0A5T51G8ZOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سیلو ای هویزه در بخش مرکزی که هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/134488" target="_blank">📅 20:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134487">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
یک مقام ایرانی به المیادین: تهران پیامی خصوصی برای جی دی ونس، معاون رئیس جمهور ایالات متحده، ارسال کرده و در آن جارد کوشنر و استیو ویتکاف، فرستادگان ویژه، را به سوءاستفاده از اطلاعات محرمانه مذاکرات ایالات متحده و ایران برای منافع مالی و افشای اطلاعات حساس متهم کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/134487" target="_blank">📅 20:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
صدای انفجار مهیب در هرتزلیا در شمال تل‌آویو
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/134486" target="_blank">📅 20:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134485">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
گویا سامانه‌های پدافند هوایی یک پهپاد انتحاری یک‌طرفه به مدل FLM-136 LUCAS را در آسمان بندرعباس، سرنگون کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/134485" target="_blank">📅 20:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134482">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VU9HWlpOrXW0M_Xzr2LB5G6-y5jHMS0YmaAD9VvaVw9cc_v-_9A-PR2Bk1V-uaJzAWlscHVYM0rm_3uWzwv8qzoTfpyPtWp9SlJj41jgEIPNqyPdztU3WBi6pC2Ih5JyGN_5gOG3mkJ8zVlpfmrwh6fvd38kLuXKX5wXjh7i3g9RuQbbCVlGGpZAr2oVIrWCoCt7tKQ3cZLLLAMTHC0cGj6hde_tftcLCre-Qp6JM5wrbi6XPeugX4MGq4V8oDl9iNJPgj1gK3TFT72yag-VcfUpH48RuKGY1SxXRDLjXQp2Z9UvMitZ5BvNZ1zxhNCc83NZL3_Y5XToWdFkJ4tYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qu8DefpiBhBcdsDbi97H5ilRnhvV3IJYqlyk2jt8zESF6Acgmh4Lj54yu_oG5sXjL1QUjSO6ZyOwCyOCyDeqWn7u5JcctG8oUwx6W37gjKTV4oJBbao0UCD-Xm6nyoHKk4XHUtTY3YXe4pdmU5hOEa6n4G_jH_SSuud2fwovLqq8jjGxs6C19MV9Ppdwhsbzlo8JvcICRRywysLKU3nEI4unaxQlPY4y_WSDl1lsQYppxONSqZS86txPCeZT-K0FjCii71Y8KS14JFnZCnV6HRMTU7KsPsFjGs5LIQhIG8dJh_IdjTf7vhUYgOayJanY19PNK17o_BsoWuf4BooqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOCLPNwAYasCo3AoXfjVjU3y1sCuk0pwbCpnItHQMVmQ50nsfPIWUBAeF7rlV7OI64kBAMc8hua-5Xj-E76zKpEPRYKuoivn4AHHUimXTI_kNfHTeC3tNvVZsKi4aVn0TI531gzxq2l851bp0cXB4IGRk5472pwUlF6Uj-yHpNZX88jw0jSv2DsEEGrurczzrRpR9k1eNOVtEcx83Klz-AbXPPgRKwlsSD3WIfD52VjONxIP4j4TgXUgNaFuYv8vvJkNo1SzrWrSBXHqj7UXPHzN_1ja5nuAJQCEcUEocJ8vcL-oUCUSjNnGdHDJglmsVUelF_qL_q4xR0IxnSaqxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
خبرگزاری فارس با انتشار تصاویر بالا مدعی شد:
انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
این پهپاد متجاوز ساعتی قبل با رهگیری و شلیک موفق سامانۀ پدافندی رزمندگان سپاه در بندرعباس منهدم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/134482" target="_blank">📅 20:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134481">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/134481" target="_blank">📅 20:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9n6wMr8FeN40rUfYN-L_-Ja0mtAiQRxxMeu5cKj3jvxg-76MzYqJkzwoIH2xdF8F8wBL53iMvP1MOx-KoGLjJ56GqIGCk3BZq5dswmm46P9-Gv_AUHwszx53aq95r3Z_3-pJGZKk6yMvGBgddz6z7jGcZNOEo7jBQqm5LERTt5KMW3WL3HxDQGF6Q9K4Tf9spwn11ckZKO_6mHGv0xpylK2FTbnYX6gj7iPVoAm-mNm6hM6WK6BEdiLncE5g7NyqH-FCXzgBLxQSwIxdUNNXDOBLHds121G27oUsnTvazXtETE9kMzlOtHppgVR9Dc3-G7o1D0VWjjSqYAXOuyVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/134480" target="_blank">📅 20:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134479">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری / صفحه امور کنسولی وزارت خارجه آمریکا در شبکه ایکس با صدور هشدار سطح چهار و بحرانی از تمام شهروندانش خواست، فوراً ایران، عراق، لبنان و یمن را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/134479" target="_blank">📅 20:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پروازهای شیراز – دبی پس از پنج ماه از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/134478" target="_blank">📅 20:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134477">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: یکی از بزرگترین نیروهای محرک آینده برای مشاغل، مراکز داده هستند. آن‌ها بزرگ، قوی، جسور و ماشین‌های پول‌سازی برای ایالتی هستند که در آن ساخته می‌شوند. کاتی هوکل، فرماندار، به دلایل سیاسی، تمام مراکز داده‌ای که در حال ساخت هستند یا قرار است در ایالت نیویورک ساخته شوند را لغو کرده است. این شرکت‌ها اکنون در آلاباما، فلوریدا، تگزاس، آریزونا و بسیاری از ایالت‌های دیگر جستجو می‌شوند. هم مالیات‌ها و هم میزان مشاغل به طلای مایع می‌رسند! ایالت نیویورک تصمیمی فاجعه‌بار گرفته است.
🔴
تمام این درآمد و سایر مزایا به ایالت‌های قرمز و برخی ایالت‌های آبی خواهند رفت، جایی که مراکز داده به عنوان گاوهای شیرده پول با مالیات‌های پایین‌تر و مشاغل بی‌سابقه جستجو می‌شوند. آن‌ها باید هزینه آب و برق خود را بپردازند و هر مازادی به ایالت و جامعه محلی بازمی‌گردد. مراکز داده پیروزی‌های عظیمی برای ایالت‌ها و جوامعی هستند که خوش‌شانس هستند و آن‌ها را به دست می‌آورند. نیویورک باید سیاست خود را فوراً تغییر دهد. نباید به دموکرات‌های رادیکال اجازه داد که باعث از دست دادن مراکز داده، هوش مصنوعی و تمام این فناوری‌های جدید باورنکردنی برای چین و سایر کشورها شوند! پرزیدنت دونالد جی. ترامپ
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/134477" target="_blank">📅 20:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134476">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RrF1MNsX38pbB7TyopusK8MrXBfWTuVkLjdhyriK6mf-OLoAsG5iv2cdnUddS62cy925L64qlVFfwe8r7CyOWPmbaFFaklXpViskZoCmCDGlN7c8fnehbCFhbvbkJ8LY6y_VNyGth8J5_O_KSioQl7Jo0eDQEOgdJeIN0-HMKF_DsgGl2VST5v2p0Z4vM0t92Te5h7l4ttPUAFKEzYRIC37KeMPhXf9YvzH7D1iphNZVPxbf7eSs8sFEJt4muaxLO8vtTt9B-RnD8Ktkpgi7tVhwN_yP7vrcmFBWiFbUfywo9Q3PpeWyS4ncoRLoNni5ELs7xb5tMa7s14cvRx0wIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید در حال بررسی تمدید مجدد معافیت‌هایی است که به کشتی‌های خارجی اجازه می‌دهد کالاها را میان بنادر ایالات متحده جابه‌جا کنند.
🔴
این تصمیم در شرایطی مطرح می‌شود که تنش‌های تازه با جمهوری اسلامی ایران، نگرانی‌هایی را در مورد قیمت انرژی و اختلال در زنجیره تامین ایجاد کرده است.
🔴
خبرگزاری رویتر به نقل از منابع آگاه اعلام کرد دولت ترامپ در حال بررسی اعمال محدودیت‌های جغرافیایی برای کشتی‌های با پرچم خارجی است تا ضمن حفظ ابزاری که به کاهش فشارهای زنجیره تامین کمک کرده، به انتقادات گروه‌های صنعت دریایی و متحدان جمهوری‌خواه نیز پاسخ دهد. مقامات کاخ سفید به همراه وزارتخانه‌های انرژی، حمل‌ونقل و کشور اوایل هفته جاری برای بررسی این گزینه‌ها پیش از تصمیم‌گیری نهایی در پایان ماه ژوئیه تشکیل جلسه دادند.
🔴
یک مقام کاخ سفید در گفتگو با رویترز، با اشاره به اینکه معافیت فعلی تا ۱۶ اوت اعتبار دارد، تاکید کرد که هنوز تصمیمی درباره صدور سومین تمدید اتخاذ نشده است. او افزود که اقدام قاطع رئیس‌جمهور ترامپ در لغو موقت «قانون جونز» به جلوگیری از کمبود در زنجیره تامین سراسر کشور کمک کرده و دولت به طور منظم نحوه استفاده از این معافیت را رصد می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134476" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134475">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
انفجارهایی در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134475" target="_blank">📅 20:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134474">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بلومبرگ: نفتکش‌های فوق‌بزرگ به‌طور فزاینده‌ای هدف حملات در تنگه هرمز قرار می‌گیرند
🔴
در ماه ژوئن، پنج مورد از نه حمله به کشتی‌های تجاری، علیه نفتکش‌های موسوم به «بسیار بزرگ» انجام شده
🔴
این نوع کشتی‌ها، ستون اصلی حمل نفت خاورمیانه به نقاط مختلف جهان به‌شمار می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134474" target="_blank">📅 20:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134473">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نیروی زمینی ارتش: پاسخ حمله آمریکا به ایرانشهر را خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134473" target="_blank">📅 19:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134472">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
انفجارهایی در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134472" target="_blank">📅 19:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134471">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / صدای انفجار در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134471" target="_blank">📅 19:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134470">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کرملین: اوضاع خلیج‌فارس رو به وخامت است/ جهان نمی‌تواند نگران نباشد
🔴
پسکوف، سخنگوی کرملین: متاسفانه اوضاع در خلیج فارس به هیچ وجه پایدار نیست و بار دیگر وارد مرحله‌ای رو به وخامت شده است و این وضعیت نمی‌تواند نگرانی جهان را در پی نداشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134470" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134469">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سی‌بی‌اس: ذخایر موشک‌های تاماهاوک پاتریوت و تاد آمریکا به شدت کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134469" target="_blank">📅 19:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134468">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران و روسیه خبر داد
🔴
وزارت خزانه‌داری آمریکا روز چهارشنبه چندین شخص و نهاد ایرانی و روسی به را به دلیل فعالیت‌های مرتبط با اشاعه تسلیحاتی به لیست تحریم‌های خود اضافه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/134468" target="_blank">📅 19:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134467">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/moSn9qGzXxp4W2YmC4k7NfHVhfd5hYrfMGZyHEx6Fap9QfNpeQfgVatLnRVY8tLM3nvImHNMtCPuJQBO2xnEiVuPQlxWe00_hL4kQI-ArKHsr3iqUewOgHcplYTF_Jj_S30hh-NAvU-Nr0LNpSnnr44x9KYU3qKFML74-UqKjphfSbbqba_sb07wOWgqnOmbfe-8oWCb-VoLndqWL2yhIyiyd22spNfIGngowd0GkA9yR3UIeSnvMTO2XntpQ2VogjaPcfjp7gxBlg5eD_4q_z16s0hBlhw-3yZ1ZseX7-UsQg6UfROC7SpyC7T2tV002heivdRjlm2J_N0Bpnmkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ما به یک انبار ذخیره گندم در هویزه خوزستان حمله نکرده‌ایم ولی در عوض ایران به کشتی های حامل گندم در تنگه هرمز حمله می‌کند
🔴
ایران در مقابل، غیرنظامیان و کشتی‌های تجاری در حال عبور از تنگه هرمز و همچنین کشورهای همسایه حاشیه خلیج فارس را هدف قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/134467" target="_blank">📅 19:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134466">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بقائی:  فعلا برنامه ای برای مذاکره با آمریکا نداریم ، روی دفاع متمرکز هستیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134466" target="_blank">📅 19:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134465">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری / صدای انفجار در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/134465" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134464">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
بقائی: فعلا برنامه ای برای مذاکره با آمریکا نداریم و روی دفاع متمرکز هستیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/134464" target="_blank">📅 19:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134463">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
موافقت شورای نگهبان با جلسات مجازی مجلس، در صورتی که جلسات به شکل حضوری در ساختمان مجلس از نظر هیئت رئیسه ممکن نباشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/134463" target="_blank">📅 19:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134462">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJjKYLfOsj6R2XfpYS4UwvbO21TrM9tx7vTnKKdqfCHBfukfRfGMFxGnpJ5Me5GBuFtKHIVBkMN9hRYU2lL4GoTivV-OfeJnNgMhx-j47F4EYC8FHprQE9P6RAJnxgZxN_161zyliIeCp9iz1Dq5ymkBTS3buHjqPdf75KjlqndKDuzujNqh747OpJ8Hi3zp_xYoCgogL8DGweIl2yufi580M1ZoNieRYSEoiOTt-DYcNkMcpBJKD4ctECQmArj9nFaEgWHCEUVrgQ6dHFIwyVk9f43ZxKSnOwYqC4sabrIDTjekYGFBQIZM7fDEwj55fNLw1B4lkYbbdY1lZvM6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
استوری حامد‌لک:
@AloSport</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/134462" target="_blank">📅 19:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134461">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
خبری که تحت عنوان اعتصاب در چارسو دقایقی قبل منتشر شده مربوط به گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134461" target="_blank">📅 19:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134457">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران و روسیه خبر داد
🔴
وزارت خزانه‌داری آمریکا روز چهارشنبه چندین شخص و نهاد ایرانی و روسی به را به دلیل فعالیت‌های مرتبط با اشاعه تسلیحاتی به لیست تحریم‌های خود اضافه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/134457" target="_blank">📅 19:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134456">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رئیس ستاد ارتش عربستان با معاون فرمانده سنتکام دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/134456" target="_blank">📅 19:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134455">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فرودگاه بین‌المللی صنعاء به چرخه عمل بازگشت
🔴
وزیر حمل‌ونقل و امور عمومی یمن: فرودگاه بین‌المللی صنعاء پس از تکمیل تعمیرات ناشی از حملات هوایی ائتلاف سعودی، به‌طور کامل به چرخه پروازها بازگشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134455" target="_blank">📅 18:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134454">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بقایی: تفاهمنامه مجموعه ای از تعهدات متقابل است و در صورت نقض از سوی طرف مقابل، ما نیز از اجرای تعهدات خود خودداری میکنیم؛ این یک اصل است و در ادامه نیز همین مسیر دنبال خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/134454" target="_blank">📅 18:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134453">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دو انفجار شدید در جزیره هنگام شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/134453" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134452">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فایننشال تایمز: ذخایر بازار نفت در حال اتمام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134452" target="_blank">📅 18:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134451">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / ترامپ: جولانی می خواهد وارد عمل شود و حزب‌الله را از بین ببرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134451" target="_blank">📅 18:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134450">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
منابع خبری از حمله توپخانه‌ای ارتش اسرائیل به شهرک عیتا الجبل در جنوب لبنان خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134450" target="_blank">📅 18:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134449">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
تعداد موارد ابتلا به ویروس ابولا که در جمهوری دموکراتیک کنگو شناسایی شده است، به ۲,۰۱۱ مورد رسیده است که شامل ۷۵۴ مورد فوت نیز می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134449" target="_blank">📅 18:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134448">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
دقایقی پیش زمین‌لرزه‌ای به بزرگی  ۳.۹ ریشتر با مرکزیت انبارالوم آق‌قلا، گرگان را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134448" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134447">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
دو انفجار شدید در جزیره هنگام شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134447" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134446">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
طبق گزارشات، تا ساعتی دیگر قالیباف درباره جنگ و تحولات کشور یک بیانیه مهم می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134446" target="_blank">📅 18:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134445">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
اکسیوس به نقل از یک مقام آمریکایی:
مذاکرات اسرائیل و لبنان در رم مثمر و مثبت بوده
🔴
بر سر ساختار و دستورالعمل‌های مناطق آزمایشی توافق شده
🔴
اجرای مناطق آزمایشی طی چند روز آینده آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134445" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134444">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HouZT4tgB7Cf3fD1W_rfXtN3emmY89Y_Yt7f3rH0h9bTeFaDnyD3In5oIBJOzZLm89bDlxEtC8yWis3tHKR_ZZJ8un2z1rHk3jot40HKlPtf1dZYYMpggI1JUfHneHuM2XFEmizGn0XuMQaFirCE9_cJZAHZ1hGPXSPX6nIqNX_PRN-hPM8z8Bm2vogkh9Ry6zo3eV72HaRaOPjIqj-zKNtwJzBGcUy2jVPggUGL6rRnPGpymvr72y31Y3fdASXb62Aj1Q4sw8ahsYPkUg-bp60LBtVp0s_TaQ5VqdNXikoWEvCXMx1ymS2LVvJE1-q9jfQmwU43Tz2GZ5gVd5J5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی، امام جمعه مشهد:
موضوع خونخواهی آیت الله خامنه‌ای فقط بحث حکومتی نیست، بحث اسلام و دین و قرآن است. ما الان ولی‌دم هستیم و باید انتقام خون رهبر شهید را بگیریم. این تکلیف شرعی و دینی برای امت اسلامی ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134444" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134443">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt4LgrDrdP3Hg0JW0t3eNQzjJQmB9brtzYhRLzDKZIgHLwxXMcjK3uF1i9FZn2h74UKEYXXKu0RIAcgP8jgjdeIVFO0rZ1d1x2EkZ-9jUoBLCAQV5XNPj75e4AIypZcActV_Br257oE4CeTujVCUrZye3pv21-LaAeWYXDaO-lb3hMi1dk3TmmNFKwnjSVOoldk2TNOWCOxPViXmaccDh5DYVEkZOy6twuq43sHAgdnLoYRfo106x4qZd2N2D386RoYXzdxBTmWta0nUTtpQ4_jlpZVdGztxSw46g224JB932yRTvEKwl59zQNbm-_PYCF0C_rBaKT9ql6jksXYF1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون آموزش: به وزیر آموزش و پرورش مهلت ۲۴ ساعته می‌دهم تا آزمون نهایی را برای همه استان‌ها به تعویق بیندازد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134443" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134442">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">غزه که نرفتید
لبنام نرفتید
سوریه هم که گفتید آسمون بسته هست
حداقل جنوب ایران برید یا دیگه گنده گوزی نکنید، زندگی مردم بگا رفته
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/134442" target="_blank">📅 18:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134441">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMfv13-tvulJjtw48XhY5dcGDyTp6zJzr1lX86cv15fLT5dC8LCD9dmVljd19N0cV0WJEmBsfKu3aFO9auPD6Ia6rxMjf2Gr-zPtQvBMdW7g5XamXsQ9qp-9cOF9rF-3P3hrIE3EESXk_chJQASRtsVIOS2YgwNPPD3HKdqLwR5-BcuGsfRCqkblgxa1iovZ59390IVjQaGPK2S17z4itq5OWjYhqUic2_v2TIgE3tPbTM_KioXmWM0hn8hW4GveQ4r0ZUawZrt6ZBi4hFyeW3-RScueF3o6Wz_KkGdiy1gEc8bB0a5vz5UDMOWfAZLhoJQOuv3E3-EmJHeXc84SVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون آموزش:
به وزیر آموزش و پرورش مهلت ۲۴ ساعته می‌دهم تا آزمون نهایی را برای همه استان‌ها به تعویق بیندازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134441" target="_blank">📅 17:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134440">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: ما نیز خواهان توافقیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134440" target="_blank">📅 17:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134439">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a47ba115.mp4?token=qZ9fSfz7p6CNi22kwQ1f3z4AplDK7F5Z1slei9kJaQ4KhoxIVx8kgGjftFmJ-mrK1RoZQFF_S6hxEpgcIke43_xobFyf8UZNx44FfrJe7wdCKU74wdDC9gUIez9JSjqh7Ym6owgsuk4hN7_aXssQFW2xdFd9ltXq6a5Esd3zFGCNVZ1PAwQazDvi_SkYzylX1wm8Dmfcx27vvJNwhwF6pJz89Ze-yBan7K7xaTnzT73UXHXpe8sMm0gyLd9pKVLs_2oMnE0Mp5Ymna5jU2W0igecATKUiyqB1TDkkR--C89kKyKgtgdU_l53SG1u0KWkUxt5ZEJhho4W1Ha_LGxf5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a47ba115.mp4?token=qZ9fSfz7p6CNi22kwQ1f3z4AplDK7F5Z1slei9kJaQ4KhoxIVx8kgGjftFmJ-mrK1RoZQFF_S6hxEpgcIke43_xobFyf8UZNx44FfrJe7wdCKU74wdDC9gUIez9JSjqh7Ym6owgsuk4hN7_aXssQFW2xdFd9ltXq6a5Esd3zFGCNVZ1PAwQazDvi_SkYzylX1wm8Dmfcx27vvJNwhwF6pJz89Ze-yBan7K7xaTnzT73UXHXpe8sMm0gyLd9pKVLs_2oMnE0Mp5Ymna5jU2W0igecATKUiyqB1TDkkR--C89kKyKgtgdU_l53SG1u0KWkUxt5ZEJhho4W1Ha_LGxf5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ریک اسکات، سناتور جمهوری‌خواه:
ترامپ نمی‌خواد وارد جنگ با ایران بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134439" target="_blank">📅 17:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134438">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ:
ایران مدتی پیش با من تماس گرفت. آن‌ها می‌خواهند یک توافق انجام دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134438" target="_blank">📅 17:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134437">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGienamLLQRHZ95kGsuI9dzvDmhRKv6N3JIfQCkvZg1OuzdSYkt0CvyNdQwCMGClhxNiYa8O55j64OTXjKcvVpw8Aoke7cUBsw4gHJ63xS58_vO_z2y7oEjgg4JiJOUadqY4-aZJ9lnA54-pOVW8HOfdLPEEiGI1klUw9pPp-DzSf3NgIhbgoXIJVajNA6m9ltH2A_Z4IVwxDXYjkP65iHKrHd6cRT45kEb-crt0jSOkg94VLBk89JYqXWAZulGNRRyjgViJSc_9JovQHvBA21rSlNJ70_tsNJk-HFxUCFSo-doX2QZmdibYSNkVRycAf2nTlbNQjm82-cPqRqupKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یادی کنیم از روزی که رسایی و دوستان کفن پوش رفتن فرودگاه مهرآباد و گفتن مارو به جنگ اعزام کنید
🔴
الان که جنگ خودش اومده نشستن تهران زیر کولر دارن آلاسکا لیس میزنن
🔴
همینقدر بی....(ایمان)
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134437" target="_blank">📅 17:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134436">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3KovOHCx5yLpoWr_SdsfoJaJg75MblRmRVt6Xc396OAhsl1ijx1RwZOMORUj27jD4cnEY3iiAPMkJJPvJJmVAfjxaa3zjVkqEgFtIsBAUF1C8jB7xqaCCiNr4U1haj3xi7UzSamz9HXePOQ_faWpLtmyN5rYdZc1suAheygPmx50D6VV7OmVHLmPTKFrSkxS4Uvc09GAJ3v-TswpjXA55_kRzs-O1H5XTxY5v_T1nThwcsUcgdzTixD89j-GIRmA_EivJfmh1OwOQB6dn5k7Fm0BkYerGEEDgH8uKj4pmcwcR91HTNpZOFvsVexsOkChZDgXlGY9pt3kxgBenDxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلیل حمله اتمی آمریکا به ژاپن این بود که امپراطور و رده‌ بالاهای ژاپنی در توهم این بودند که درحال پیروزی هستند اما یک روز صبح صدها هزار ژاپنی تنها بخاطر توهم و غرور عده‌ای محدود کشته شدند
🔴
دلیل جنگ هم کاملا مضحک بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134436" target="_blank">📅 17:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134435">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4Z8XXUuxh8oNYj3lpolEaFpPcy20W_Wy6cIu8wnDxs-N2hJNOtzqICilXAChr3IEJ9qp3RdsKb1elIjEeaWptJ4VECRRHO5Mtaxs8NtDKtuU8zuAJfR1f7xihCncMZvgZsHLLM5mS12soYpVu7vrFtWLjKLh3oOTjK7D5aQH4CcOU42iHk6aYbWFEngIkKRKw6Nrp-4Uix0X0NjznbdnhwJrkgT7S9BA1w3KQYtwtttQ4cnn19TNIaEwmhExevtnRaeFVB14OoFFX8sN0kv6CDRFDKQcPWtCafj4v8S2_9ZppnOBuSiBMy25T8t39nusBRbClvHTiiduqBMH8lPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
احتمال حمله اتمی به ایران وجود داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134435" target="_blank">📅 17:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134434">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
قیمت بنزین در ایالات متحده با افزایش ۳ سنتی به ۳.۸۹ دلار برای هر گالن رسید. این رقم مربوط به میانگین قیمت در سراسر کشور است. به گزارش شبکه «سی‌ان‌ان» و به نقل از انجمن خودروی آمریکا، این افزایش ثبت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134434" target="_blank">📅 17:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134433">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2816fc5cf7.mp4?token=C3aC3zKA2qZFnh3FTgUeV5C1k-f0BRNP_79a8VDTdDQLWxnQHMqqCwItkx2zgXf_eMfjFtW0To3m8vuHrSpf9kAUtdlDsIfx3O6jItktMZYTFuqn28INM7k63FljbGdf3c0xXqKimAX_nalKI3FXpCzFSNVFaF0KftnCteV6dDuBuDhcXc8TLn3O1dgwIx_6JvITCr7-xEAez1_kdUaRSFnVc-bo4ZjQaluuYm4T6qHtORkiIGNhzwGsQK6o2XosEZeurdcLCIiPgARbw0ueRR9PpK8D7KjQiJjATquKWfDSXDxZbcbajIzoRxZRAaL3GXCGDn5B7QMrAJAbRL5SgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2816fc5cf7.mp4?token=C3aC3zKA2qZFnh3FTgUeV5C1k-f0BRNP_79a8VDTdDQLWxnQHMqqCwItkx2zgXf_eMfjFtW0To3m8vuHrSpf9kAUtdlDsIfx3O6jItktMZYTFuqn28INM7k63FljbGdf3c0xXqKimAX_nalKI3FXpCzFSNVFaF0KftnCteV6dDuBuDhcXc8TLn3O1dgwIx_6JvITCr7-xEAez1_kdUaRSFnVc-bo4ZjQaluuYm4T6qHtORkiIGNhzwGsQK6o2XosEZeurdcLCIiPgARbw0ueRR9PpK8D7KjQiJjATquKWfDSXDxZbcbajIzoRxZRAaL3GXCGDn5B7QMrAJAbRL5SgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی حمله سنتکام به یک لانچر موشک ضدکشتی در جزیره تنب بزرگ در خلیج فارس صبح امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134433" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134432">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c482140313.mp4?token=F-L2GOLbmAC2n-u-w72uRlWsAb8JFlRTnhDrFeG1j_lXrHW4zlgvcCLNUvoFADSYnj52UHBLZqRa1t0Ton8gOWWunMJq1Hten_t4E_GlldGnlx0CvKIC4EzlidcIzEg19BYQTeFA8Sq0YjFoPJ7zG81NC729TkuQ_8Z9TOn8tQikne_r_Ilm30QaRHGMmeef1ayklYhYnfife4zNVZq-_Y4x7ljdXRkNm4KHpwDDxGkLZyaLjWiSPIJSNiO0Zx5i22Pk7uBLsP3-ByCttw0_H48UgWQbEwtpM-lY1uok3u45TU8vh5Qx-bKPJ5Pl-iYTNydWpydfTrLvsfWwtK1QFEskQXZQRjz0JJJmGu4FtTnPf6dio6RvRgzqUiwJd7Hay2bSVTWwKi3ZYSGz0baHx7i_qA1HVSieHn3px0lbgSz-nGI2F6KN-rISHclZX1akxNBRnVGNGdhUcn6m7k8LsQmvn77OFoOP8a98dH2v1EyNk61kDxXQxlorGGkuatGZxYEOg50WHl4FOeh1KvmjLFtDhi64Jqw_XIeQ-3H7AXBSvhlvtg-mlnUhyjzZ2j1IcAfMuWbBHEXMFvyHAJXee_G2B09_hi9lrYCVuek1pDlgoJFr12zkmgEFUG4PZTFy1s6uIhyWJzk8qCdFDAbsJnSfflDdVa_sgw0MZsDNDpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c482140313.mp4?token=F-L2GOLbmAC2n-u-w72uRlWsAb8JFlRTnhDrFeG1j_lXrHW4zlgvcCLNUvoFADSYnj52UHBLZqRa1t0Ton8gOWWunMJq1Hten_t4E_GlldGnlx0CvKIC4EzlidcIzEg19BYQTeFA8Sq0YjFoPJ7zG81NC729TkuQ_8Z9TOn8tQikne_r_Ilm30QaRHGMmeef1ayklYhYnfife4zNVZq-_Y4x7ljdXRkNm4KHpwDDxGkLZyaLjWiSPIJSNiO0Zx5i22Pk7uBLsP3-ByCttw0_H48UgWQbEwtpM-lY1uok3u45TU8vh5Qx-bKPJ5Pl-iYTNydWpydfTrLvsfWwtK1QFEskQXZQRjz0JJJmGu4FtTnPf6dio6RvRgzqUiwJd7Hay2bSVTWwKi3ZYSGz0baHx7i_qA1HVSieHn3px0lbgSz-nGI2F6KN-rISHclZX1akxNBRnVGNGdhUcn6m7k8LsQmvn77OFoOP8a98dH2v1EyNk61kDxXQxlorGGkuatGZxYEOg50WHl4FOeh1KvmjLFtDhi64Jqw_XIeQ-3H7AXBSvhlvtg-mlnUhyjzZ2j1IcAfMuWbBHEXMFvyHAJXee_G2B09_hi9lrYCVuek1pDlgoJFr12zkmgEFUG4PZTFy1s6uIhyWJzk8qCdFDAbsJnSfflDdVa_sgw0MZsDNDpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع و اعتراض متقاضیان خودرو سایپا به دلیل تحویل نگرفتن خودرو
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134432" target="_blank">📅 17:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134431">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کامران یوسف خبرنگار پاکستانی: پاکستان به نظر می‌رسد یک گام به عقب برداشته و پس از آغاز دوباره درگیری‌ها میان ایران و آمریکا، رویکردی «صبر و نظاره» را در پیش گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134431" target="_blank">📅 17:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134430">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
یه کارزار راه افتاده که میگه کسایی که موافق جنگن(بیشتر جبهه پایداری(خوارج) و وزیر اموزش پرورش و نماینده های تندرو مجلس) به جنوب کشور فرستاده بشن و اونجا اقامت داشته باشن و کارا رو جلو ببرن تا از درد و رنج مردم جنوب که هرشب حمله بهشون صورت میگیره اگاه بشن…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134430" target="_blank">📅 17:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134428">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یه کارزار راه افتاده که میگه کسایی که موافق جنگن(بیشتر جبهه پایداری(خوارج) و وزیر اموزش پرورش و نماینده های تندرو مجلس) به جنوب کشور فرستاده بشن و اونجا اقامت داشته باشن و کارا رو جلو ببرن تا از درد و رنج مردم جنوب که هرشب حمله بهشون صورت میگیره اگاه بشن…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/134428" target="_blank">📅 16:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134427">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jWi1I-A16Fr6Ukoo0eDrY2vQPlYNOv3WBz1rOEAkbse2UMFfRMD91XB1LCXdUKB2N4Mea_lvwaeUQpq_mp8IU01Mw6Nwd4YNDaoNp9lVBeWultnofCbQctTaQ8Vr5Nsx9NLV52ig_xsVTryw1CbsN5GeH1A4JdE6VIQF3MOefayti213qrqfryYDUS60EwV8OxWef07r96Vnni9mkpVQH60C_6M2_JV5a3ApTsznZYgJQ0d6XnVzxGBlTIkC2hO_SRLe8tO0hoXX6AWtNLmM7mL5IqTMOHQZTjRVrMNDG9PwA0jXnLUBKWF1fNX6svptnyAdKNmrgIQiTHh1jzgDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه کارزار راه افتاده که میگه کسایی که موافق جنگن(بیشتر جبهه پایداری(خوارج) و وزیر اموزش پرورش و نماینده های تندرو مجلس) به جنوب کشور فرستاده بشن و اونجا اقامت داشته باشن و کارا رو جلو ببرن تا از درد و رنج مردم جنوب که هرشب حمله بهشون صورت میگیره اگاه بشن
😁
به شدت داره وایرال میشه و همه دارن امضا می‌کنن!!
اینم لینکش
⬇️
https://www.karzar.net/333344</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/134427" target="_blank">📅 16:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134425">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63af64b487.mp4?token=YwRWHs0wlU6MDJvc8UUJAtqY7ifDe1CKCzQR7l_Ib34YVj5mLka2IYGb9xUR_h_RktIys9oPGl_s-sEw1Mj-E7zsJ6VOXgjXd7Lu_Rm05HhWsbs-ntSufLx4OyPlj_QlN6xmHIdUxOSO0rSj3_EiaO2rXHHfsr9Dq_YB3S_6UmwBPYz8YnDUHML8gfu_h9_K5IJqXnmcVPogC8Bjqecno2o6CajOxugKurkJ9ySQYMeLlZmPWSWY8WCPP2X1w3acb6f2auVGHyJg6XkJfD3u51RrItbrnsKm3_3m1gXBSofXRyK3TqeTC_AT6XqShrrkoCCPzCf0x4b0JKwINtzPTyfju36WQQwvdOZw23A_D0d4p1IXYDTngca1Hkj2nfiMPAypsjQ_VPIMHbtL_hqhpdHDtV5sNBp2M0q8Bf-mTypmsLaPbIyb5G7S1N7K3Z_HxjUBdKiRZAgC6Kb1_x2NMaskNpnNzFinYz-ZZqKiTzSqvpQ0fZwcz2JIfW0H9SWE-2JUX1dDCRWhrzz2IN1roYkwILNYAtZCMcsN8e44NDm25SeOjVsFXg21ZC7RsZb_muBFsk24pcdZXHODx5jLy1zNmkDza4Cb8J9f4qJybSzHbOdQhu5FV1ht3Q71ChBUOu97DnglnDuvGykwiZ4BoFq0csx1GLb5blzrBPD1IFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63af64b487.mp4?token=YwRWHs0wlU6MDJvc8UUJAtqY7ifDe1CKCzQR7l_Ib34YVj5mLka2IYGb9xUR_h_RktIys9oPGl_s-sEw1Mj-E7zsJ6VOXgjXd7Lu_Rm05HhWsbs-ntSufLx4OyPlj_QlN6xmHIdUxOSO0rSj3_EiaO2rXHHfsr9Dq_YB3S_6UmwBPYz8YnDUHML8gfu_h9_K5IJqXnmcVPogC8Bjqecno2o6CajOxugKurkJ9ySQYMeLlZmPWSWY8WCPP2X1w3acb6f2auVGHyJg6XkJfD3u51RrItbrnsKm3_3m1gXBSofXRyK3TqeTC_AT6XqShrrkoCCPzCf0x4b0JKwINtzPTyfju36WQQwvdOZw23A_D0d4p1IXYDTngca1Hkj2nfiMPAypsjQ_VPIMHbtL_hqhpdHDtV5sNBp2M0q8Bf-mTypmsLaPbIyb5G7S1N7K3Z_HxjUBdKiRZAgC6Kb1_x2NMaskNpnNzFinYz-ZZqKiTzSqvpQ0fZwcz2JIfW0H9SWE-2JUX1dDCRWhrzz2IN1roYkwILNYAtZCMcsN8e44NDm25SeOjVsFXg21ZC7RsZb_muBFsk24pcdZXHODx5jLy1zNmkDza4Cb8J9f4qJybSzHbOdQhu5FV1ht3Q71ChBUOu97DnglnDuvGykwiZ4BoFq0csx1GLb5blzrBPD1IFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که در پی حملات موشکی اخیر ایران، به یک سیستم نظارتی ضد پهپاد و یک انبار هلیکوپتر در پایگاه هوایی شاهزاده حسن در اردن، خسارت وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134425" target="_blank">📅 16:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134424">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری / زمین‌لرزه‌ به بزرگی ۳.۲ ریشتر خرمشهر رو لرزوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134424" target="_blank">📅 16:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134423">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ44KHzCT1ez5VIHhvZKZa6DqLdHGfNkJPQZW39P1oM2LEMCVKP0BEo3GXjcauND0Ri42jW-dmY4J_tegvJ9RfReqmysSKcfNuu2Q7Oca-4eNKM-quLs0lZ1PdZBnf0Dpyxgn6iCu-8P991PxDVLKV2i1N0ZVVMw7lqO4Krtp5H-pJZpfIx10p4_oHworwLWKazHqIgOy1Wy3OTxuTcPcYXl_tqBZSVIGXP_C4_Ufo_u52qCZXjVXSumE6r5LwpnWVNFkDVcEKFxZYAC72A0h_Lo5qOKmzIcYANY2Zs-kzONPdgHI24Zlv68iRDUx86d_fvrjFCoLkRH-NWu7uX97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارزار مردم برای حضور اعضای جبهه‌ پایداری در مناطق جنگی به ویژه جنوب کشور به ۴۵ هزار امضا رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134423" target="_blank">📅 16:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134422">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/979e817815.mp4?token=MXkAJGIqxqvqDjP5wR-iovLxqg2UQlgVcUFTo68aUQY1nBrewDJ4hddTCe6vQbb3U6OXeI5lbkaFMXGsqHSwOpzmd5qkMDyD7BVmPfHL4PbeoGzpZg1O5hFBP6NIIe3F4YrS3vDGSXE00UAL7KT0pKneXHZSDTWeLZ0BvdADhyDJQkTFd67ctsT4vd6c-eXyyGMZ3jIcviNqN83eAJDDQQcHAIep0c1g7kOy8ZBblneq-Xi_wmYuYq3EThcCNSq0pQh0xMaqKKpZweGerThHrNYqdq1S-wJ0ctHPfO7IpzVkWvP-bg3sgrC2_d39X9mE8q21cw0YZoFss7oI96XjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/979e817815.mp4?token=MXkAJGIqxqvqDjP5wR-iovLxqg2UQlgVcUFTo68aUQY1nBrewDJ4hddTCe6vQbb3U6OXeI5lbkaFMXGsqHSwOpzmd5qkMDyD7BVmPfHL4PbeoGzpZg1O5hFBP6NIIe3F4YrS3vDGSXE00UAL7KT0pKneXHZSDTWeLZ0BvdADhyDJQkTFd67ctsT4vd6c-eXyyGMZ3jIcviNqN83eAJDDQQcHAIep0c1g7kOy8ZBblneq-Xi_wmYuYq3EThcCNSq0pQh0xMaqKKpZweGerThHrNYqdq1S-wJ0ctHPfO7IpzVkWvP-bg3sgrC2_d39X9mE8q21cw0YZoFss7oI96XjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمو پورنگ در مراسم ختم مادرش
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134422" target="_blank">📅 16:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134421">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رسانه‌های عبری: برآوردها حاکی از دیدار نتانیاهو و جوزف عون، رئیس‌جمهور لبنان در سه‌شنبه است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134421" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134420">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
کپلر: بر اساس تازه‌ترین داده‌های ماهواره‌ای، روز گذشته هیچ کشتی از مسیر جنوبی تنگه هرمز (کریدور عمانی) عبور نکرده و شمار حوادث دریای عمان به ۵۶ مورد و جان‌باختگان دریانورد به ۱۷ نفر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134420" target="_blank">📅 16:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134419">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jJBaske98GncTAMBS-JMZnuw8dU2U-hdUHK9pKzQR9HodOp8QqFwo5fCLfgrmjn7M2p2Snao9mGPmQ7aJXh6l_InOGqCAsMob2DPF4cGjH7yGgXTE-HYY8n0I1vOjefvcdQ3NFuI9HnQbj6ISADj6dI0oHML-3hqL3oIKR1v7PoF7ydNICcUWX4jRbjd5DZzV7ZI_pkRnBiHYXDW7WzNQ0a2Q8XN-u8jhjQstRGNK9KGdcvovW6gATiKOwJFSxGU2zNHke8kPgx6E2F394HoF_V2e0lJAZ7PJMct7bYGdJ7KMj_plzuNyFMczL4mLXRcXoGq9zXjSNXDWJGOgHo_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / وزارت امور خارجه عراق در پی درخواست وزارت خزانه‌داری ایالات متحده، بخشنامه‌ای صادر کرده که حزب‌الله لبنان را در فهرست سازمان‌های تروریستی قرار می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134419" target="_blank">📅 16:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134418">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSDy47bkNl37_20kT-aV81tRQj8YzbcBXPkBOI-gzx0ukOIocaS5YWHw-cPuTaJHgY9oJDyi1vxixN2DiHxgnopHyABvHEiii7huYsY4ebmKviDVLjhIJhC5Ga4_YsrTAIFGKaeCzOVWHuOWoelfoqjV7i27l2sZsNCY3i5MBSfxoN1ay3lOxX2pz1_G5FguudILjna1fv6NFT-6CKaxPlHacwf6Q28BC_7GqCc31z8tzh5cQVDpjZVNJY3sk3nCrCaeKY4H4SsX9p-nHuIgcSLQJq6jsiFtz2bks-QC_SGMxaJsderlqCoJY-0lx1Bcr9-dwTLEnGSxthB0Q1Y_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز گزارش داد حملات سایبری ایران از ضعف‌های امنیتی شبکه‌های ارتباطی قدیمی SS7 برای ردیابی موقعیت پرسنل نظامی و پیمانکاران آمریکایی در خاورمیانه در طول جنگ استفاده کرده است.
🔴
در آغاز جنگ با ایران، موجی از درخواست‌های مکانیابی از طریق شبکه‌های تلفن منطقه، از جمله بحرین، مشاهده شد و گمان می‌رود از این روش برای ردیابی دستگاه‌های متصل به شبکه‌های محلی استفاده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134418" target="_blank">📅 16:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134417">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
صداوسیما : تنگه هرمز همچنان بسته است و در ۲۴ ساعت گذشته دستکم ۲ کشتی با شلیک اخطار نیروی دریایی سپاه متوقف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134417" target="_blank">📅 16:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134416">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
فاکس نیوز: ایالات متحده صبح امروز به جزیره تنب بزرگ در خارج از تنگه هرمز حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134416" target="_blank">📅 16:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134415">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGYtUCHB0zVKcmm9oqgfdxRDwIIQnC-RSi-BhBpvt41WmOA5fPU7oHiMBipZCZ4id-43KYqCCsSsusDVwsBReJkbP6eptPVMnRghMH6UBu5t1o9KOsVKEnROkjyioUsXcGTqZgzAJGGJM-Ur7EQtlX_6CYqBeoeQ95brrJ7Rrfs53tScVILynkPwZ-pOAB13jFlgoCJEdXLXj39n6pjCZHkOzAOvIDt7D6x7cNudaRWD3LhBiyqNgVEkoB-YWHRhSsT4g7K897m6wqb907Uj2R3SMrVqrqUH5CVZkzjAgj-derXSdcooEBaw7flITNTvCG7gTCAePv93akUZGZf_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عباس عراقچی برای ابراز تسلیت به مناسبت درگذشت امیر سابق قطر وارد دوحه شد
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134415" target="_blank">📅 16:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134414">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/رمضان رحیمی عضو کمیسیون آموزش: کنکور سراسری در صورت ادامه‌دار شدن تنش‌ها، به تعویق خواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134414" target="_blank">📅 16:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134413">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5c5356b55.mp4?token=VYoTzrLU6jBEnmCmY_lHPOFiR3F6pUxi2p1pQ90CmMTGCGqIrHkAaWhCv0uVD1DulWcpcYCc6WYm555M9gyj6YMVn-lSE_kduPYAnZKQpZJiH8PDHXHZE7FIkrwVwFmvxr5GG8PfVf_8ECqFXm5fRRV4uCnJQjsyfjSG7QAo9v56_eK1Kcoa40rmrUvgf6yOzdjK_AYmCmso6NTeGA1tM_-YGh9QZsIdPziaieNTGwxZYkwvSrA-J1PTHKm3_9hY6kVOPXIRPJl4TTdHU6kVcEWi7f_ZJKM570QlBQCptOfXU4Iu5aCM2Q7w4n9t5e1HfhosaDVIUTWF4ZrYst2bew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5c5356b55.mp4?token=VYoTzrLU6jBEnmCmY_lHPOFiR3F6pUxi2p1pQ90CmMTGCGqIrHkAaWhCv0uVD1DulWcpcYCc6WYm555M9gyj6YMVn-lSE_kduPYAnZKQpZJiH8PDHXHZE7FIkrwVwFmvxr5GG8PfVf_8ECqFXm5fRRV4uCnJQjsyfjSG7QAo9v56_eK1Kcoa40rmrUvgf6yOzdjK_AYmCmso6NTeGA1tM_-YGh9QZsIdPziaieNTGwxZYkwvSrA-J1PTHKm3_9hY6kVOPXIRPJl4TTdHU6kVcEWi7f_ZJKM570QlBQCptOfXU4Iu5aCM2Q7w4n9t5e1HfhosaDVIUTWF4ZrYst2bew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌ها از وقوع انفجار یک تانکر حامل گاز در منطقه الهرمل در شمال لبنان خبر می‌دهند.
🔴
جزئیات بیشتری درباره علت انفجار و تلفات احتمالی هنوز منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134413" target="_blank">📅 16:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134412">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رسانه i24NEWS: انتظار می‌رود که دونالد ترامپ و بنیامین نتانیاهو روز دوشنبه در واشنگتن با یکدیگر دیدار کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134412" target="_blank">📅 16:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134411">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUWuOuiW6GPslRx5ycgIDBAF0jdpXASHasDa24uA7uRCs7zJeMFYadkjAr99V_n8uOvDK5b8ingPaUfUHwxpAZMdMwG3ZJ_uTJvR_el2zMrBOUEe60ogP43cTUZD0IiS3VncHv3_ibOPreIhgzIG0JgQpXt1DTPAwN3weazo4pdX7_bzgu71N-dOukubjqWkbTkJXfY-HDiT35R3UqdKXl-8y9H_pCrzzy_x5WrTa31-Fp5B6_235bYkQp-JYgMuDx7r3fJTR8l1AtXgX6LQY-Jb8L9ITrUcBv0Jl8ckdrEKkL6or4EFbNgTQ-7ZRW-OFSr9OkuVHtqQK2VhjX8cnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور محمود احمدی نژاد در سفارت قطر در تهران برای عرض تسلیت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134411" target="_blank">📅 16:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134410">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ولایتمدار، عضو کمیسیون امنیت ملی:
به‌زودی دولایه از مسئولان آمریکا و اسرائیل را قصاص می‌کنیم
🔴
مردم نیز خود را برای تحمل شرایط سخت آماده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134410" target="_blank">📅 15:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134409">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سنتکام: در طول موج حملاتی که به مدت حدود ۹۰ دقیقه ادامه داشت، فرماندهی مرکزی با استفاده از سلاح‌های دقیق، سامانه‌های دفاع ساحلی و همچنین پایگاه‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134409" target="_blank">📅 15:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134408">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
یک هیئت ایرانی از تهران عازم قطر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134408" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134407">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی ایالات متحده: تکمیل دور جدیدی از حملات علیه ایران/سامانه‌های دفاع ساحلی و انبارهای موشک کروز در جزیره تنب بزرگ را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/134407" target="_blank">📅 15:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134406">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
صدراعظم آلمان: ایران فورا باید وارد مذاکره شه چه در بحث هسته ای چه موشکی، و تنگه رو هم باز کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134406" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134405">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
عراقچی به قطر سفر کرد
🔴
عراقچی به منظور شرکت در مراسم ادای احترام به حمد بن خلیفه آل ثانی امیر سابق قطر به دوحه سفر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134405" target="_blank">📅 15:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134404">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رئیس مرکز ملی اقلیم سازمان هواشناسی: موج‌های گرما تا پایان مرداد ادامه دارد، اما از حدود ۲۰ مرداد به‌تدریج از شدت گرما کاسته خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134404" target="_blank">📅 15:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134403">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
مدیرکل شیلات هرمزگان: با وجود شرایط حساس کشور، روند صید و تأمین آبزیان بدون وقفه ادامه دارد
🔴
مدیرکل شیلات هرمزگان با تأکید بر تداوم فعالیت ناوگان صیادی در تمامی بنادر استان، گفت: با وجود شرایط حساس کشور، روند صید و تأمین آبزیان بدون وقفه ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134403" target="_blank">📅 15:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134402">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jPKnDi7tpc7NCWf0jpR6K5c8CF75Ny1cp6f9-KUgF8DXb5wMgfTKJtIVpDA8gQzCDB3-aQnVH2XwBlHnO1UOSUaBXdXuWqWsKUXDZmV92G2ZWPARZaETgkPZ8S3fC4F_2SFe3Q5g4cZJzyLOdQlNN9DTavjohWiubLlxwA_lt_A-mvtr7bR9ZmqfIIsV-bDVtPWosBLMBVK0md5M6o-RJHvEJhj0bscNmrWwDV4RbkaD3FdivxTXmhud2H2LdgFqZchR-dUBoJwOLgPEcgfSkw6IiyWfdRGUqLWqVaM2mQ_XqWMo5yWlT3SdLrIC51C_20Pa9R8_uMUPRgTc1_J-3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هیئت ایرانی از تهران عازم قطر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134402" target="_blank">📅 15:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134401">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔹
🔹
یه چیز عجیب و خفن پیدا کردیم...!
👀
🤖
وقتشه با یه ربات هوش مصنوعی خفن آشنا بشی
😻
✍️
نوشتن متن، کپشن، خبر و ترجمه
🖼️
ساخت عکس با هوش مصنوعی
📦
ساخت موزیک و آهنگ با هوش مصنوعی
🧠
پاسخ به سوالات، ایده دادن و کمک در کارها
📚
خلاصه کردن متن، تولید محتوا و کارهای روزمره
🚀
سریع، راحت و همیشه در دسترس
✅
فقط پیام بده
✅
درخواستتو بفرست
✅
تو چند ثانیه نتیجه بگیر!
اگه دنبال یه ربات هوش مصنوعی کاربردی، حرفه‌ای و همه‌فن‌حریف هستی، اینو از دست نده
👀
🔥
🤖
لینک ربات:
@AIBotLabb_bot</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134401" target="_blank">📅 15:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134400">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نخست‌وزیر مالزی:اسرائیل را به رسمیت نمی‌شناسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134400" target="_blank">📅 14:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134399">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDmjcUDvkF_cZ28YeC4qjwMukd2Y_SFlaP8d9aTA4Xb6s1IpkhRwcq4DHH4KZJGogRlAM2dkGWR3-EA6b71BuiocHFDlJELeUCtJ9WnF26hyBwQiY8VHn7_0RZSEwgz0UFrdjVXsy-Pir3yJbHmr5wPQcPJzwUWRd9JR1ZEbkQmwWCADwFYg9ZgxAQrYMYE-6YSrkl6tNpbx4pau1rla4Ud9whnn-7_-G6vPWsEBUGrorazUPhcL5W3Wvigbk88POCvN2E73YvcENgKLZaF0mK7Wz3OWrEytg5zilDIqyZn-YJS0ce31NeVuX16ORxhGiBcyeE6QXNvyl0gFnRhfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی: یک میلیون پیام سین نزده دارم
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134399" target="_blank">📅 14:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134398">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وبگاه آمریکایی پولیتیکو: میانجیگران منطقه ای بین ایران و آمریکا، پس از تنش های چند روز گذشته، فعالیت چندانی برای کاهش تنش نشان نمی دهند، چون فکر می کنند ایران و آمریکا قصد دارند طی چند روز یا هفته آینده با  زورآزمایی در میدان نظامی شرایط خود را برای مذاکرات احتمالی آینده، بازیابی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134398" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134397">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlmToZur6tZVHnJoSGUtk1FpjEi2H866HGST6wEvQdaa2Khjp6u7JnpoQJ5qRQh6GL1Hvybs6vU0VpMccPRiKuZu2g8ZDiEujbV65i6E5KjvlITgfpoWbuyeMNu4KDLDEt8_K6UZAZ2dVrbaiqK-i2P70x8JYY67XpcjTF2GSI7sKeYb_Nn2bWPMvnKAU6pNEnl8khM79giXUZUf15vuLba4XBUzBxFo-RVha_3Ld9C5PFaJAXYhpLGKHEmzXbL7YDIp0cZtFVG9Cnuw2UGUIZW4uwT8PcDlZxacgnyXKroZKsN5IAVh0u5JUTorSAMYTQ1Gmvu_qHshy0f_i-FieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: خبر عالی برای آمریکا! تورم ناشی از دموکرات‌ها بسیار پایین‌تر از چیزی است که بود، و ما آن را باز هم پایین‌تر خواهیم آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134397" target="_blank">📅 14:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134396">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت بهداشت: واکسن HPV فعلاً به سبد واکسیناسیون رایگان کشور اضافه نمی‌شود و اولویت وزارت بهداشت، تأمین واکسن‌های فعلی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134396" target="_blank">📅 14:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134395">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت نیرو: جدول خاموشی منتشرشده برای تهران مورد تأیید نیست و شهروندان برای اطلاع از وضعیت قطعی برق، فقط به سامانه «برق من» مراجعه کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134395" target="_blank">📅 14:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134394">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پولتیکو: تلاش‌های میانجی‌گران برای احیای مذاکرات، هیچ نشانه عمومی از پیشرفت نداشته
🔴
احساس کلی این است که درگیری فعلاً ادامه خواهد یافت
🔴
یک مقام سابق آمریکایی: حملات ایالات متحده بیشتر یک پاسخ تاکتیکی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134394" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134393">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q148rjwLg2ZkNl1Ik91UdocChRpVvnrD3emwPUln4g8txWdhP5evfSO8ZsFsVS_yE6dkEUR6Cdm8k8LGw1u275LAoWjHjw6pKL4eua3xv1s6gMA9zxn_4svh78fZ-k4U8NdAyUiqUpli4m6rDwn-dQgH2bgeEiGLJXY1SvE0rZDPQfFX0JT6IjCfnudVu9XLaclSrOaea-M1HeWECCKP-xzL7of0pPJTuoa-pQTjxBHv5_0HzopdxHsuVXjT4_2hAPth20JR9LVuWmjM-Kr3FG1RtE_kiTG9nPb3jrxmElfTFdegAKr-STpwd2wVpCNFTNmIJ___y5LnMGxWXibhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا از ضرب سکه طلای جدید یک دلاری با تصویر ترامپ خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134393" target="_blank">📅 14:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134392">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btch0V0SGONLpbWm6LqO0AK1P5kHzYEdefHw8uJnarec_BvXV8nUN0WugvzbJamHWvezEc-M_eNcuPksseOonALURMuxrwPLxsGhG_IqpoiEbt9tYMLnKPMknc2DpCssEQZSHRQaovtxKLQpCvviD0vhvy8ZWSVL43bR7IDBw0YW8FT-cTGffySC79OffbqO4KgKkmCyvb8QhO9ZTbLHZEeslyaUiPjBZGOAEOToUKgchR75AngObY_OZ40JbZeyBjs72sHpF_kQFW-HkB9JL7PNycvjZu3o5xCzsYc3yyzXNmLthGDDBxqGmkqM5KVBJmTIYQ2qKSz-Ssh2EB0PJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سالار ولایتمدار، عضو کمیسیون امنیت ملی مجلس: مردم خود را برای شرایط سخت آماده کنند. ممکن است با محدودیت هایی در تامین برق و سوخت مواجه شویم و به این دلیل مردم تحملشان را بالا ببرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134392" target="_blank">📅 14:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134391">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری/امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد
🔴
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه ۲۵ تیر و شنبه ۲۷ تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
🔴
امتحانات نهایی سایر استان‌ها و امتحانات بعدی استان های مذکور، بر اساس برنامه ابلاغی در موعد مقرر برگزار خواهد شد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134391" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
