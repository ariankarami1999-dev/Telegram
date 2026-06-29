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
<img src="https://cdn4.telesco.pe/file/GsDeYrn3V35NNQqVK3veh1S-g8yaYYJ02j2BpV-oN5Am5x8jQkIP_huKJCNp2O9m_aSZt4WuB1D132rdJJfjxyKGNND6wi62lOiUG_d92gyQOX3EeGYxGMEQ9ihqerBN3HhYRhpZRO0ZCSQ8JaNloG1P8AEFyoolq2aQ9rpUsi8AXtLQpCJUogbmFm4NiLXqIpxdoFyzga3yU0rgqhXkT7T3BoEJWb-jFzAMPsB2uokZ6NG4q7wB1E136rVkwdRiT26A92z6chHtbv7cmQ4Hu_UFZ0JEqc0bQG9lYiY4F3PV58wQBbco7CiqU9ilIw-usqmzL8Bg_PcPCFEh9R7j-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 13:34:21</div>
<hr>

<div class="tg-post" id="msg-18087">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الهام فعلا استراتژی مالش را آغاز کرده تا مثلا خود را در دل آمریکایی‌ها جا کند، غافل از اینکه ارمنستان با چرخشی عظیم به سوی غرب، در دلبری از واشنگتن و تل آویو ، گوی سبقت از باکو خواهدربود.</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SBoxxx/18087" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18086">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هیچ حمله سایبری در کار نیست.  MV = PQ  وقتی M را با چاپ پول برده ای بالا و از آن سو Q هم اگر افتی نکرده باشد دستکم رشدی هم نکرده، قیمت ها یعنی P باید منفجر بشود. پس تنها راهی که داری این است که از سرعت گردش پول یعنی V بکاهی و آن را بندازی گردن اسراییل و نت…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/18086" target="_blank">📅 11:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18085">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcTD5BzFC1FRw21M22gGwPRTEfNfpHNXQLKNDZYCsS1JO6HsvtJoEvLRPUiG09cqBYFBDL-JraWgua_NxQ661A4a52H3tJ3CWhHDN5qr4EXmHzREjRmc8lr-sFX1yCKyZZsjQE_4S0BHzsMmwI0yEbcuHKOM6986cN57m0mpSHLpM_DvLEyFvofbNunjDN4OqeZZVOdg-wLUSxUArSRuRilL4rn8aCkuBxFjz_OJhdr9IePGnwkX3-dfmvvqPmc0DKhesVrxks45SGW3XX9nWBNwyjMai79dDJvITFURTCMfxa0bgmdHHVUnLdLr4IHrpUe66qmnI6NIEkS_sNgp8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا رقابت هوش مصنوعی میان آمریکا و چین این‌قدر سروصدا کرده است؟
رقابت هوش مصنوعی آمریکا و چین فقط رقابت فناوری نیست؛ هم‌زمان رقابت بر سر ارزش بازار، سودآوری، امنیت ملی و برتری ژئوپولیتیکی است و هر جهش جدید می‌تواند انتظارات سرمایه‌گذاران و موازنه قدرت جهانی را تغییر دهد.
مدل‌های ارزان و باز چینی در کنار جنگ تراشه و محدودیت‌های صادراتی آمریکا، معادله اقتصادی هوش مصنوعی را تغییر داده‌اند و ابهام درباره فاصله واقعی دو طرف، به مهم‌ترین سوخت این هیاهوی جهانی تبدیل شده است.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SBoxxx/18085" target="_blank">📅 11:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18084">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmpISCn-0RPvVIAJu6zhzdjsYit564yiKMrJSFdp4ysmKxrISPaB7lpyuHv2s7nRa8Qzp46TfNmKD8DZQuSAvBrl2N7Vr6NbjvfxCaC5iFYAzZEFnY0WsdXo0XVJNtqlRK_nRyx5LFsWP8CN4Xa4f2ll9Z_4fJjh3L5tUZYfw5UrAnrOYPcSBkpirEdUHgRzArh8PYmslsU8ABZckYPeStuNqT9mO98KVUr7EsFeiwjsTJsm1PZtgUkGFhB_38FGY-2RYCIzTs8SV9c5Fxk2XpVi7nZk4k5bNT-00YgkJIB-6NIe76a-cVqYGpj_7AdpH0eOQD97EIgGWbhXZpgpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم عبور کشتی‌ها از تنگه هرمز به طور قابل توجهی با ترافیک سال گذشته متفاوت است.
پورت‌واچ آمار جدیدی درباره ترافیک کشتی‌رانی در تنگه هرمز منتشر کرده است. در ژوئن ۲۰۲۶، ۵۰ نفتکش و ۴۰ کانتینر عبور کردند در حالی که در دسامبر ۲۰۲۵، ۱۱۵۰ نفتکش و ۴۰۰ کانتینر ثبت شده بود.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/18084" target="_blank">📅 01:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18083">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حمله سنگین اسرائیل به منطقه "مجدل زون" تو جنوب لبنان</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18083" target="_blank">📅 01:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18082">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آکسیوس با استناد به مقامات آمریکایی  ایالات متحده و ایران توافق کردند حملات را متوقف کنند و گفتگوها را در این هفته برنامه‌ریزی کنند</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18082" target="_blank">📅 00:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18081">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترور یک عنصر ازبک در سوریه  بنا بر گزارش منابع محلی یک عنصر ازبک با نام خالد الجزراوی روز گذشته روبه‌روی منزلش در الفوعه در حومه‌ی ادلب توسط افراد ناشناس ترور شد.  برخی منابع محلی این ترور را به داعش منتسب کردند، این در حالی‌است که داعش هنوز مسئولیت انجام…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/18081" target="_blank">📅 00:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18080">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترور یک عنصر ازبک در سوریه
بنا بر گزارش منابع محلی یک عنصر ازبک با نام خالد الجزراوی روز گذشته روبه‌روی منزلش در الفوعه در حومه‌ی ادلب توسط افراد ناشناس ترور شد.
برخی منابع محلی این ترور را به داعش منتسب کردند، این در حالی‌است که داعش هنوز مسئولیت انجام این ترور را بر عهده نگرفته‌است
چندی پیش یک عنصر چچن با نام مصطفی الروسی از اعضای نیروی ویژه تحریر الشام موسوم به العصائب الحمراء نیز ترور شده‌بود.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/18080" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18079">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/18079" target="_blank">📅 00:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18078">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آکسیوس با استناد به مقامات آمریکایی
ایالات متحده و ایران توافق کردند حملات را متوقف کنند و گفتگوها را در این هفته برنامه‌ریزی کنند</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/18078" target="_blank">📅 00:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18077">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر علوم و فناوری  اسراییل، گیلا گملیئل:   وقتی که از رژیم ایران عبور کنیم، نوبت به جاه‌طلبی‌های امپراتوری عثمانی می‌رسد که به دنبال گسترش و نفوذ خود است. شکی نیست که ترکیه با آرزوهای گسترش فراتر از مرزهای خود و رهبری منطقه بر اساس دیدگاه خود، تهدید واقعی…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18077" target="_blank">📅 19:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18076">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk7NqxhFOiIvGmNOpm6AFNMbRaTiFd-0oBoBCdg1mIjQlwZlxM_vgQzKt3bR69YnKBjlkg9C-eQ-GE7jSyEt52n6hSO7yKtXj-jqb1WEY3K0rv4ia80AqU_TIZTzoNWHRwkj3JOtm-cGFMPFJc5246FUrS60KhfuoF7JYnuEC8eKRK_pdLaPviMOwa0lKZtJvuXxwjEw9ZbmA2p2l_Msu7gKlcWbHe-tF7bkfWFDY0i4wm8ROJZuTkLyrRvHBL86eUOg5yzcTEBQGKoBbW6yQ-Sxl4c4JyX9UilhVHXJetdi4FRkPHLZV9fxloUAraIsX1fLlK5puST5tFVU8cM76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا شاخص سهام کره جنوبی در روزهای اخیر ریخت؟
ریزش اخیر کاسپی بیشتر از اینکه نشانه ضعف اقتصاد کره باشد، نتیجه هم‌زمان فشار روی سهام نیمه‌رسانا، نگرانی از تداوم نرخ‌های بالای آمریکا و خروج سرمایه از بازار بود؛ بازاری که وابستگی زیادی به سامسونگ و SK Hynix دارد.
با وجود شدت افت، کاسپی هنوز فاصله زیادی با سناریوی «ترکیدن حباب» دارد و سؤال اصلی بازار این است: آیا چرخه رشد نیمه‌رساناها ادامه پیدا می‌کند یا قیمت‌گذاری این صنعت زودتر از انتظار به سقف رسیده است؟
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18076" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18075">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هندی ها جوری هستند که یکی شان میخواسته از بانک پولی بگیرد به او گفته اند برو گواهی فوت خانمت بیاور و نداشته؛ رفته جنازه زنش را از قبر کشیده بیرون کول کرده برده بانک که پولش را بگیرد!  حالا شما فکر کنید بین شمال تنگه که پولی است با جنوب تنگه که صلواتی است کدام…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18075" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18074">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن، می‌گوید دولت جدید اسلوونی به رسمیت شناختن فلسطین را لغو کرده و سفارت خود را به اورشلیم منتقل خواهد کرد.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18074" target="_blank">📅 14:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18073">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بحرین می‌گوید حمله ایران به ساختمان مسکونی آسیب زده است، تلفات جانی نداشته است</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18073" target="_blank">📅 14:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18072">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b2ebb26.mp4?token=UCCouAxOILUejtV9NSK5wAFj5w-6RXkDSv_BXIlzHjexhfBBpM0wYBQ8UblhNrBTPSyb2yPxcrnpNEmoVaH4foC1lhzd7pMMzCeNQC48klF6PlTy_qt3VkefVGn5hWPe63UA_WXJF9dH1KRJd9zM2R9JavA8rx4vBw3t9GBazLwG46Y12etgdzXRO_CpHz5Ktaq2X6LbwaqGpZNEBG5RCsysNBZ0LWtPs2XsTMJ5EfIdczNahgH4g5v2oPeOp0Dm-bdCS7ZxGAFwAWfF6uzG1SfAhAub6fYpOdygEeOFySY0sjsdCyKNoPIR48Q_zrnQcIDMptiTRRKU4oXECvP5hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b2ebb26.mp4?token=UCCouAxOILUejtV9NSK5wAFj5w-6RXkDSv_BXIlzHjexhfBBpM0wYBQ8UblhNrBTPSyb2yPxcrnpNEmoVaH4foC1lhzd7pMMzCeNQC48klF6PlTy_qt3VkefVGn5hWPe63UA_WXJF9dH1KRJd9zM2R9JavA8rx4vBw3t9GBazLwG46Y12etgdzXRO_CpHz5Ktaq2X6LbwaqGpZNEBG5RCsysNBZ0LWtPs2XsTMJ5EfIdczNahgH4g5v2oPeOp0Dm-bdCS7ZxGAFwAWfF6uzG1SfAhAub6fYpOdygEeOFySY0sjsdCyKNoPIR48Q_zrnQcIDMptiTRRKU4oXECvP5hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی نجاسات الجزایری پس از خوردن گل تساوی تیمشان از اتریش که باعث شد تا در مرحله حذفی به اسپانیا نخورند!
بعد پروفسور جمشید خیابانی به عربی از این نکبتها درخواست بازی شرافتمندانه داشت!
حق شما همان گیوتین فرانسوی بود و بس!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18072" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18071">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.  عین بلایی که سر ما تریدرها…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18071" target="_blank">📅 10:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18070">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18070" target="_blank">📅 08:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18069">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=DoQl7kOfFR_6ogmOcTU9v-kuQXRKGoHk8qa7xsuvNXnUXmJt0htwAyzaJOm2T-G1eixw1gJezJ3ggZT3H6kEgW1WeRr58mYlBE4w7GtYPvgXNQV7VTbOMBsZ4uy9HwjWxK5n0tgHlujG-u--mHqSX5OnxH3IX4BlQGjzsA4ok1dybpF4FKJR5vheaVB_aHummthg44vtsLAYhVovXacxW0ngTdJ0xBA3HERhsw8vAQr1vg7RX2oA92zWg_IG27uhMvdtcNEZlvkD4T8XU4AWasLGd2WZQn_bS7ooknemykkSGhUYcLbxJ9YTYt2OEpd3mDz5Jvj8kKssqVcoVcnWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=DoQl7kOfFR_6ogmOcTU9v-kuQXRKGoHk8qa7xsuvNXnUXmJt0htwAyzaJOm2T-G1eixw1gJezJ3ggZT3H6kEgW1WeRr58mYlBE4w7GtYPvgXNQV7VTbOMBsZ4uy9HwjWxK5n0tgHlujG-u--mHqSX5OnxH3IX4BlQGjzsA4ok1dybpF4FKJR5vheaVB_aHummthg44vtsLAYhVovXacxW0ngTdJ0xBA3HERhsw8vAQr1vg7RX2oA92zWg_IG27uhMvdtcNEZlvkD4T8XU4AWasLGd2WZQn_bS7ooknemykkSGhUYcLbxJ9YTYt2OEpd3mDz5Jvj8kKssqVcoVcnWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در واقع دارند می‌گویند از مسیر عمانی ها نروید چون اینقدر خطرناک است که ممکن است ما بزنیم تان!  سبحان الله!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18069" target="_blank">📅 08:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارشگر صداوسیما یک دقیقه قبل از حذف ایران از جام جهانی:
یک کشور مسلمان، کاری کرد تا کشور مسلمان دیگری صعود کند!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18068" target="_blank">📅 08:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18067">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شبکه ۳ بعد فوتبال یک روحانی  را آورده او هم آفتابه را گرفته روی همتی که چرا گفتی از دشمن گندم وارد کنیم مگر گندم تراریخته نشنیدی!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18067" target="_blank">📅 07:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18066">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وقوع انفجارهای جدید در کویت و بحرین
هم‌زمان با انتشار گزارش‌هایی از وقوع انفجار در بحرین و کویت، وزارت کشور بحرین از فعال شدن آژیرهای هشدار و درخواست از شهروندان و ساکنان برای مراجعه به نزدیک‌ترین مکان امن خبر داد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18066" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18065">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عراق عملیات گسترده ای را علیه سیاستمداران عراقی وفادار به ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18065" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18064">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تحلیل همین است.   این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.  پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18064" target="_blank">📅 06:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18063">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ
:
هواپیما های ایالات متحده بار دیگر ایران را بمباران کردند چرا که بازهم آتش‌بس را نقض کرده بود.
احتمال دارد زمانی برسد که دیگر نتوانیم منطقی باشیم و مجبور باشیم آنچه به صورت بسیار موفق شروع کردیم به صورت نظامی به پایان برسانیم. در این صورت دیگر جمهوری اسلامی ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18063" target="_blank">📅 06:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18062">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
نیروی دریایی سپاه: آمریکایی‌ها جهنم را در این روزها تجربه خواهند کرد
فرماندهی نیروی دریایی سپاه:
شلیک‌های کور آمریکا به سیریک معمای اشراف ما بر تنگه را حل نمی‌کند. اما شلیک‌های ما به متخلفین، راه روشن عبور را به باقی شناورها یادآوری می‌کند.
حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.
‎</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18062" target="_blank">📅 06:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گویا صدای انفجارهایی در بندر لنگه و قشم نیز شنیده شده</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18061" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18060">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بیانیه سنتکام:
«پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی M/V Ever Lovely، به ایران فرصتی داده شد تا توافق آتش‌بس را رعایت کند، اما وقتی نیروهای آن در ساعت ۴:۳۰ صبح به وقت شرقی امروز با پرتاب یک پهپاد یک‌طرفه به کشتی M/T Kiku حمله کردند، این فرصت از میان رفت. این نفتکش پرچم پاناما در حال عبور از نزدیکی تنگه هرمز بود و بیش از ۲ میلیون بشکه نفت خام حمل می‌کرد.
نیروهای فرماندهی مرکزی امروز در پاسخ مستقیم به تداوم تهاجم ایران علیه کشتیرانی تجاری، حملاتی را آغاز کردند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی ایران، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپادها و قابلیت‌های مین‌گذاری را هدف قرار دادند».</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18060" target="_blank">📅 01:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18059">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک منبع نظامی ایرانی به صداوسیما گفت:
«صداهای انفجار شنیده شده مربوط به برخورد چندین پرتابه به برج مخابراتی در سیرک است».</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18059" target="_blank">📅 01:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18058" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی به سمت کشتی‌های متخلف در تنگه هرمز تیرهای هشداردهنده شلیک کرد. صدای انفجارهای شنیده شده در شهرستان سیریک و جزیره قشم در استان هرمزگان به این علت بوده است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18057" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش‌های اولیه از حملات هوایی آمریکا به جنوب ایران.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18056" target="_blank">📅 01:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مجلس خبرگان رهبری بیانیه داد:  باز کردن تنگه هرمز ممنوع است و هرکسی که به ترامپ و نتانیاهو دسترسی پیدا کند، بر او واجب است که آن‌ها را بکشد. ﻿حاکمیت ایران باید بر تنگه هرمز اعمال شده و از طریق آن عوارض دریافت شود تا خسارات وارده بر کشور بازسازی شوند. ﻿</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18055" target="_blank">📅 23:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e39aee93e2.mp4?token=WrBx6DmQjsh_KEHl6CU7ftwqwrkJf_bWms67nL_KtPYufw_cOuSqJBezLEhjnn74Vz2V9aH3UecFKuVZksqklEsDo6cn128fvnwaNZ-op5iCATq1w9qsjuZbVHyoPmAKmmddgVkgTvHeDtcGanP6zKmev_J6tiK52X6I1gMS0Zc2UhaILXKZniNc8v45cc6CFKoPC8GpInGCSHSYGHxmSd89Rf2DX06J_J-t-WGCjoQx-PnUJvuzqXdEEknlqwZd4NAe4g8feaP2EUi5x1Le9qUX07vXBw_a89GfVu86zY12C_qcI04GAplY0pIO0IdK5qAG2wYOlLQvBaf_0DJOHoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e39aee93e2.mp4?token=WrBx6DmQjsh_KEHl6CU7ftwqwrkJf_bWms67nL_KtPYufw_cOuSqJBezLEhjnn74Vz2V9aH3UecFKuVZksqklEsDo6cn128fvnwaNZ-op5iCATq1w9qsjuZbVHyoPmAKmmddgVkgTvHeDtcGanP6zKmev_J6tiK52X6I1gMS0Zc2UhaILXKZniNc8v45cc6CFKoPC8GpInGCSHSYGHxmSd89Rf2DX06J_J-t-WGCjoQx-PnUJvuzqXdEEknlqwZd4NAe4g8feaP2EUi5x1Le9qUX07vXBw_a89GfVu86zY12C_qcI04GAplY0pIO0IdK5qAG2wYOlLQvBaf_0DJOHoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داشتم به این فکر می کردم که ویدیوی التماس جواد خیابانی به الجزایر برای مساوی نکردن با اتریش را دیدم!  یعنی هر چه شما می خواهید به خودتان بقبولانید که دیگر به نوک قله فلاکت رسیده ایم و دیگر  تپه ای برای ریدن نمانده یک دفعه می بینید یک کصخلی پیدا می شود تا به…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18054" target="_blank">📅 23:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مدیرعامل شرکت خدمات انفورماتیک:   تلاش می‌کنیم اختلال بانک‌های ملی و صادرات تا پایان وقت امشب برطرف شود</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18053" target="_blank">📅 23:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18052">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الجزیره: اختلاف تهران واشنگتن بر سر تنگه هرمز بالا گرفت   اکنون شاهد آن هستیم که ایران و ایالات متحده در تفسیر مفاد یادداشت تفاهم با یکدیگر اختلاف دارند؛ اختلافی که به‌طور فزاینده تنگه هرمز را به اصلی‌ترین نقطه اختلاف میان دو طرف تبدیل کرده است.   دو بیانیه…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18052" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18051">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به نظرم در شان ابرقدرت چهارم دنیا نیست که اینطور بانک هایش فلج باشند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18051" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18050">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هیچ حمله سایبری در کار نیست.  MV = PQ  وقتی M را با چاپ پول برده ای بالا و از آن سو Q هم اگر افتی نکرده باشد دستکم رشدی هم نکرده، قیمت ها یعنی P باید منفجر بشود. پس تنها راهی که داری این است که از سرعت گردش پول یعنی V بکاهی و آن را بندازی گردن اسراییل و نت…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18050" target="_blank">📅 22:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18049">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.
عین بلایی که سر ما تریدرها آورده شد که آخر هم نفهمیدم ترید فارکس قانونی است یا نه! عمداً فضا را خاکستری کردند — نه آزاد نه ممنوع — تا هر وقت بخواهند باج بگیرند و هر وقت خواستند رها کنند و هر وقت خواستند بزنند و ببندند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18049" target="_blank">📅 21:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18048">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الجزیره: اختلاف تهران واشنگتن بر سر تنگه هرمز بالا گرفت
اکنون شاهد آن هستیم که ایران و ایالات متحده در تفسیر مفاد یادداشت تفاهم با یکدیگر اختلاف دارند؛ اختلافی که به‌طور فزاینده تنگه هرمز را به اصلی‌ترین نقطه اختلاف میان دو طرف تبدیل کرده است.
دو بیانیه اخیر ازجمله بیانیه سپاه مبنی بر نقض ماده ۵ یادداشت تفاهم درباره بازگشایی تنگه هرمز و همچنین بیانیه وزارت خارجه مبنی بر نقض ماده ۱ یادداشت تفاهم درباره توقف فوری درگیری‌ها، شواهد این مدعا هستند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18048" target="_blank">📅 21:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18047">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18047" target="_blank">📅 19:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18046">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5LF66roMdK1WHrERSe45wIpjJOkYUKkSii3VLBSA_Ltta6ELStq3_iGVxPNVLXyu2OCE5sTaq9junyuMt2mh6PzCS1RIqLXjf0KUUfay-ebh-8ubWHwHk1XICXCylQEoEENFLfAz50CdqotaK_KKqK9xHXUmZ0CqOkQi-ZYwJVbQrd74k_Ao8-tyq8kqJ0iG_VRJ1_fNSnOtI9_0JYTAdkbl6MJmGwgWnvznNloC1nc8D66XoeS_qBymaNijKYluN4srllxddXKLE6Ns9TTWiPC5fts8hXVGWZxQE2lUO8duAs_g2OdgOAZVyUflat08qk1LApi3PLycB8xvFKsFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شادی فلسطینی ها در غزه پس از گل مصر!  مصر برای اینها چه کرده؟!   دیوار کشیده تا از شهر موشها (غزه) به درون مصر سرازیر نشوند. یک بار هم ارتش مصر فاضلاب خود را به تونلهای حماس سرازیر کردند که باعث شد چند ده تن از اعضای حماس به دیدار خالد بن ولید بشتابند.  آن…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18046" target="_blank">📅 18:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dafd3cf871.mp4?token=S3Hg0vOh9FmDk4YHKfNmMSYO7Z7zUok6HyVv0mbishJP6XhIDm_EUlSo2XIPV5XGgAA_6PUeDwp6aFvRDZSB-AUYoiKe33EUuGNRFmDrT53Mk4NPPVa-GYZvbzTotkfBZ7TNh-flunLnfH8U1wea7IivieKGlEYwGP8sj8LYFWzRJ9X4S5JkFmqjTgDT5yxKHWbb-4mPA3_vBwV3pqlvw-FJjt5R5LZSZlMdzxO5rYxeJKYVUy7OGGfOAk_KxV5EEeWTl64Y63DtwIrsxmbqbSwQqIjmrEbAoBTmG2HMrtlTs-gtvBG2kOHnoK2Nl3yda2R1JdGItT1N6mMRykfElA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dafd3cf871.mp4?token=S3Hg0vOh9FmDk4YHKfNmMSYO7Z7zUok6HyVv0mbishJP6XhIDm_EUlSo2XIPV5XGgAA_6PUeDwp6aFvRDZSB-AUYoiKe33EUuGNRFmDrT53Mk4NPPVa-GYZvbzTotkfBZ7TNh-flunLnfH8U1wea7IivieKGlEYwGP8sj8LYFWzRJ9X4S5JkFmqjTgDT5yxKHWbb-4mPA3_vBwV3pqlvw-FJjt5R5LZSZlMdzxO5rYxeJKYVUy7OGGfOAk_KxV5EEeWTl64Y63DtwIrsxmbqbSwQqIjmrEbAoBTmG2HMrtlTs-gtvBG2kOHnoK2Nl3yda2R1JdGItT1N6mMRykfElA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فلسطینی ها در غزه پس از گل مصر!
مصر برای اینها چه کرده؟!
دیوار کشیده تا از شهر موشها (غزه) به درون مصر سرازیر نشوند. یک بار هم ارتش مصر فاضلاب خود را به تونلهای حماس سرازیر کردند که باعث شد چند ده تن از اعضای حماس به دیدار خالد بن ولید بشتابند.
آن وقت هواداران جمهوری اسلامی، ژنده پارچه چرکین کشور خیالی فلسطین را با خود به ورزشگاه برده بودند و این هم جوابشان!</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/18045" target="_blank">📅 18:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18044">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">UKMTO:
گزارشی از یک حادثه در تنگه هرمز دریافت شده است.
کاپیتان نفتکش گزارش داده است که توسط یک پرتابه ناشناس مورد اصابت قرار گرفته است. این کشتی به پل فرماندهی خود آسیب دیده است؛ گزارش شده که همه خدمه سالم هستند. در حال حاضر هیچ خسارت زیست‌محیطی گزارش نشده است.
به کشتی‌ها توصیه می‌شود با احتیاط عبور کنند و هر فعالیت مشکوکی را به UKMTO گزارش دهند، مقامات در حال بررسی هستند».</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18044" target="_blank">📅 13:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18043">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رودان هم جز میتوانست جزو گزینه ها باشد که ولی خب.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18043" target="_blank">📅 13:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سبحان الله! با Secret Box روزنامه فردا صبح را داشته باشید.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18042" target="_blank">📅 13:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سبحان الله! با Secret Box روزنامه فردا صبح را داشته باشید.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18041" target="_blank">📅 12:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18040">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18040" target="_blank">📅 12:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18039">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18039" target="_blank">📅 12:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18038">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDtkx974fXkzZb3Hv7c6Wky5cyU6uhbLIjywnBhSrMRQvWR-dnksG66KNSwD3Cyf1i9TAb9kIlr38XZnpXm-3qTHMXJES6mahDkI5pLY7XAiLCRQkt6f4HEmzqX_cR6OU43-iiRuDnn7fNv2OOBzsugl1y3NJaqgSxTQUQh4kVoDrx726DPrn09JB55hYCqhFyYUr0pG8b99V4jW_pzapHKAyhAW1OMNyjhy37_aq4UpfuaIz8IC8x8VjPji2zDppwT9rBraMzkHDhJmvzlr2b15cyZCjCwRh23lFLCJTbJAaJTFSAu_3ntGh6YxS4VeNzb3wZ6-jCg7BArownUZuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران
آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.
برخی تحلیلگران معتقدند کاهش تنش در خاورمیانه می‌تواند علاوه بر اهداف سیاسی و امنیتی، فرصتی برای افت قیمت نفت و خرید مجدد نفت در سطوح پایین‌تر جهت تقویت ذخایر راهبردی آمریکا فراهم کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18038" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18037">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssYgn_fE0KxlAWMmdeavnipFTPA04--TdGVF3XccrF1mTW9f9JQf7LAXczkW7Tt1tLbiKH8ru4xfhrS0a_ZNr01MRAHl6u_mx05nrvOBynWLPQeGsPHUDAjQ8ymXW-LF13HHSMu4XKGLJl7lm5NS1sD_FNGYujazfLEh_BaurivFsEq2wM4VBy3OQxhzo61oCIKBBIkrZYn50QDK2P_TDa3ti4LVRT49DYWTJ3y8lojy5u0lKdFdYsql8CKjh5DBjQ7PrFYY8kkAsS0xJYKRKFBvYVsVXlGCAMYi1ST6ic4kpSD2qI3fjs91BeRI1JAWKG5IONAe5XRev2NudeFwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه بازی</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18037" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18036">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t41xYFTsAHrrI-w5ijcdtKQehDj8GQmxLOGibU7x1-kpGbeUxFy7m2Qe-Icwqva4Ojf3hbh5ZSiSeMGrsA8q3r8WTMGml7HZDNUzV30WGjzvmiYhZ707XpX3qBs2lEyHAdzrjS8n5m2KN6RdRn07itwRCYjQb1s4Pg-HyPM7gWhNUSbk2P1aLtg2hZbsvDznKrjfgndCJjLBlQUMxPFq5QBJAnwNhFcWz3JCm5NSUhMpYK8EY-U5PJGldpDgAd9E0-chH3fCOAajOwrOciReZCpbanBTtlheswczPpX6IyBBfyn7NnrGocJSTd7LY37O6OBrHXdE0_tlmHmnV3e6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18036" target="_blank">📅 08:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18035">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">الان تو زمین بگی محمد‌ حداقل بیست نفر تو زمین و ده هزارنفر نفر تو تماشاچی‌ها برمیگردن‌ میگن جانم؟
• میرزا •
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18035" target="_blank">📅 07:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رسانه‌های دولتی ایران: سپاه پاسداران چندین پایگاه ارتش آمریکا در منطقه را هدف قرار دادند</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18034" target="_blank">📅 02:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18033">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رسانه‌های دولتی ایران: سپاه پاسداران چندین پایگاه ارتش آمریکا در منطقه را هدف قرار دادند</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18033" target="_blank">📅 02:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18032">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس ایران: ترامپ هیچ تعهدی به اصول مذاکره یا آتش‌بس نشان نداده است</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18032" target="_blank">📅 01:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18031">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">متن اعلامیه سنتکام:
حملات ایالات متحده به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — به
عنوان پاسخی قوی به حمله دیروز به یک کشتی تجاری که در تنگه هرمز در حال عبور بود، نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در تاریخ ۲۶ ژوئن حملاتی را علیه ایران انجام دادند.
پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد حمله یک‌طرفه به کشتی M/V Ever Lovely حمله کرد، هواپیماهای آمریکایی به محل‌های ذخیره موشک و پهپادهای ایرانی و سایت‌های رادار ساحلی حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
این تجاوز بی‌دلیل علیه کشتی‌های تجاری توسط نیروهای ایرانی به وضوح آتش‌بس را نقض کرد. علاوه بر این، رفتار خطرناک ایران آزادی ناوبری را تضعیف کرد در حالی که تجارت به طور فزاینده‌ای از این گذرگاه حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM به ارائه هماهنگی و حمایت برای عبور ایمن کشتی‌های تجاری از تنگه ادامه می‌دهند. نیروهای نظامی ایالات متحده همچنان حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اطاعت و به طور کامل اجرا می‌شود.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18031" target="_blank">📅 00:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18030">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حملات تروریستی گروه های تجزیه طلب به ایستگاه های مرزی در بانه</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18030" target="_blank">📅 00:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18029">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سنتکام   به دستور دونالد ترامپ و در جواب شکست آتش بس توسط جمهوری اسلامی عملیات محدود ما در ایران آغاز شد</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18029" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18028">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjB9m2iaEX4sOqGoXQtQSX9pTX0HgPItb7cyvf2B1RecQLAzloc39r7f_IcutyMHKvAJk00KBOTDcXhvxn3o6elmtfEDaTTfWKXdUUPBrv7K5AlwVUT-1LIgjrr_W9KluPLdj1wZJYjw8a1bn2mNIj2pK6hPNfDcxZXv_N0JR7Ej-QIaZfEtvQtamZhV79NotS39Kbs3HsX0q-pie8Vtox9LUEZwxfeZaSFxaJa4c9jac61NvMf10P0Z6pEgzOcev6b_sLTMB2hltD8heSNLS7jiy6wYyFIoUWze-kH0Uklm3k_nqlznGr_uk7ijkXq-_v-PfsDT-vvNKpqggRbxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مثل ما نفت را خریده.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18028" target="_blank">📅 00:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18027">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18027" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18026">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چادرملو! صد تبریک! / مردک نزن تو سیریک!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18026" target="_blank">📅 00:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18025">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فعال شدن پدافند قم!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18025" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18024">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پزشکیان را آوردند که جنگ نشود؛ هر 36 ساعت یک بار جنگ داریم!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18024" target="_blank">📅 23:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18023">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">به نظرم بهترین پاسخ زدن رودان باشد؛
هم آتش بس نقض نمی شود هم به هر حال پاسخ داده ایم و هم دل جمع بزرگی از مالباختگان خنک خواهدشد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18023" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18022">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1ilMlPYHr8K_vW9yYnoGpzkO_oJqlp1QsI3sy3td3cxR3_Fn7eci7XM3Q0KBxujZOuKQP_YO7KFMpTHx0dRh6m9QzAYd4S0QCvHMr_IgVYoMi0zpnwqPglYsZVAEeMIT900_MJrNJDWJdjZTDod_BCclvPbA9MZe2G4Z4VevNqdgBR1y_hxV9OhUnxWwqDY-b4Wst6CRHcqtbLNBqV7H4MEvkWm5ZEThDAJkqIdkOlXwveIF_-kpYulkxuxfZ9VLArAyHTXT2wLHqc--0OqqzWx2hGsw3CPAExZlQO-2YQmESL9SCTgz2RHB33Ra0DczqTmNRwYc9Cq46PrdVb_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید حمله آمریکایی ها توسط یکی از همراهان باوفای Secret Box در بندرعباس!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18022" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18021">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این مواضع ضد و نقیض تعریف همان موج کذایی 4 است.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18021" target="_blank">📅 23:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18020">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سنتکام
به دستور دونالد ترامپ و در جواب شکست آتش بس توسط جمهوری اسلامی عملیات محدود ما در ایران آغاز شد</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18020" target="_blank">📅 23:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18019">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ اشاره کرد که ارتش ایالات متحده ممکن است پس از نقض آتش بس توسط ایران با پرتاب پهپادهای تهاجمی به کشتی‌ها، با زور پاسخ دهد.  "خواهید فهمید! آیا من پاسخ خواهم داد؟ خواهید فهمید."</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18019" target="_blank">📅 23:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18018">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ اشاره کرد که ارتش ایالات متحده ممکن است پس از نقض آتش بس توسط ایران با پرتاب پهپادهای تهاجمی به کشتی‌ها، با زور پاسخ دهد.  "خواهید فهمید! آیا من پاسخ خواهم داد؟ خواهید فهمید."</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18018" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18017">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18017" target="_blank">📅 23:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18016">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هیئت مذاکره‌کننده ایرانی قبل از مذاکرات، کتاب ترامپ را مطالعه کردند  طبق یک گزارش، مذاکره‌کنندگان ایرانی قبل از ورود به مذاکرات مستقیم با ایالات متحده، سبک مذاکره‌ای که دونالد ترامپ دنبال می‌کرد را از نزدیک بررسی کردند. این نه تنها شامل روانشناسان بود، بلکه…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18016" target="_blank">📅 22:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18015">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هیئت مذاکره‌کننده ایرانی قبل از مذاکرات، کتاب ترامپ را مطالعه کردند
طبق یک گزارش، مذاکره‌کنندگان ایرانی قبل از ورود به مذاکرات مستقیم با ایالات متحده، سبک مذاکره‌ای که دونالد ترامپ دنبال می‌کرد را از نزدیک بررسی کردند. این نه تنها شامل روانشناسان بود، بلکه آنها کتاب «هنر معامله» ترامپ را که در سال ۱۹۸۷ منتشر شد نیز مطالعه کردند.
این مرحله نشان می‌دهد که چگونه ارتباطات غیرمنتظره‌ای در مورد فعالیت‌های ترامپ در رسانه‌های اجتماعی در طول درگیری پدیدار شد. بنابراین، طرف ایرانی سعی کرد درک سیستماتیکی از الگوهای مذاکره او ایجاد کند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18015" target="_blank">📅 22:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18014">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آمریکا، اسرائیل و لبنان یک توافقنامه چارچوبی امضا کردند که بر اساس آن اسرائیل یک منطقه امنیتی در لبنان را حفظ خواهد کرد.
ارتش اسرائیل نیز آزادی عمل خود را در این منطقه امنیتی حفظ خواهد کرد -</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18014" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18013">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ:
بنیان‌گذاران ما در اعلامیه استقلال چهار بار به خدا اشاره کردند. چهار بار.
من حتی یک بار هم ذکر نشدم. من بسیار ناراحت هستم. حتی یک بار.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18013" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18012">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8r7SoTcf44BSMskfIYRC2c5W_MnaGQngOo1v0k3rLn_1QBuzgBGk1h18HCHvNY7cMwKZoaHGQmJh9kbO-Frz28pHO6Le2qppTgYgHdgzDsmw5GfifUZBMM_RVVBgQfsyZr17LmrB1htppN7s_qQSEEVtB8cQD6zsUu9-puV2kd2nzoBd1vbllm-UPZYNM-yd31gVTeQjTlGJW7PYRndTCFWnKRgszZbaRZCXLyMUaXoy8J2V8Tq8dZ3q9wCDfmww_2-3X6aRPixgn7cz0W7B-WVSyBdZ6UAeYm601SRsRN15AU-pMgISPYqQpMvWrF03L5iggv1cQJvvu9LhdXiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18012" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18011">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18011" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18010">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18010" target="_blank">📅 19:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18009">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0QwZmwZlHbIaOYQE7ELG3vb7fiCPa7woV7ko7yAuYGYOCKkhJ17zMu7BD1bxXIF3Y5leuksmiZzByokaseU2xjninrKqwz34Q71sy6NQSWIop9KUlddrQWtS93fT4Ekk1IJZpwhTzcFQSDO5A6Um9v7Ovs6qC9gSt3GPHxZ7qAWuGsYO8JSusZaff2bWBcplIPiFmu0v9FFzii9Yxdlh2kWZoA_7RzZk-caohpdGqDAHZewFF3LDPsJDIi0Yn7brK4iwZ4J4O3Ib38Ry2RZYcbQdC4deV_IS0arDiTIZ1alT4z9FlZf_uA3A8gRDYjYtR1aS3S6yKF7wHWaWKN1GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق کنید.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18009" target="_blank">📅 18:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18008">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/18008" target="_blank">📅 18:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18007">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18007" target="_blank">📅 18:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18006">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اسرائیل درصدد به‌رسمیت شناختن «کشتار ارامنه»  وزارت امور خارجه اسراییل پنجشنبه شب اعلام کرد که «گدعون ساعر» وزیر خارجه این رژیم روز یکشنبه آینده پیشنهاد به‌رسمیت شناختن «کشتار ارامنه» را در دولت مطرح خواهد کرد.  شبکه المیادین نوشت: بر اساس این گزارش، این اقدام…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18006" target="_blank">📅 18:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18005">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ajo8Vp-3FeyXFltckuu62NW3xaYzwOJ69GHmaf_XAElMJWTuMRLBsGmhIQAv8pClgnhU2FVHkXncNzOgjJUFVUXxMGXMg6A8W29gPGkLjHHAxo0s9-nTvLw2zZxbo6KVvGbeMNQjOF9p6PtmPC9nu3c9AJtriL7x-ItfHZr0S8I9zONdc9lWYM-r0S99CVrVSBZXSHiEwhJP4q9A5nHdlKr90VRO7moCCi-xh8Fnmk_NJq2lg3yiu_8LSHxZi9lz2yLywdedF6ImFWqSOrOuWNw8Z3psURQl2UJs5cUKK8awp1yBrDePYhkViUIrmj5NHUnUgbeFV3gvzDJbLVmn2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.
🟢
وقتی دکتر مسعود، نمی‌تونه از کاراکتر دوره جَوونی‌ش فاصله بگیره!  پزشکیان [در سفرش به پاکستان] به نشان دوستی یک درخت تو اسلام‌آباد کاشت که رسم پاکستانی هاست.  ولی نکته جالب اینه که هی شهباز شریف نخست وزیر پاکستان اشاره میکنه مسعود جان بسه کم خاک بریز. نمادینه…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18005" target="_blank">📅 18:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18004">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qa_02eNok2xbyxsXOliP3lj4o5aKeghfSinTX2CdZo6bADWu9j7kebr0zAR9bJKXF7Ph4KS-yHoNGE3ETco2B0QhtB19MuswHsCQA0IoA1vZcJSn2Ao7hz8vhnF5QlvBRzTmseJwQEApHQup0Zq2FJ6-eU7ORttW6HfsP9RWv_IjNuRkhviCcr-d3VUCHByTGGgWjzfV_gkE_zA8qCkwGoMA-5D4C_955ZkoN9thjZ_oRS9gKlFWdaQXJv1tFtRZTiUOYq1yCHa1GLfrI4W2PjzJvg3WIKP94BISqNpx_o4fMvtVrc6Y7CioiD1BNYbPbn-IpIa4NyeIItBZqrYbLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاتز وزیردفاع اسرائیل ضمن تهدید فرمانده سپاه قدس، آمده عراقچی، پزشکیان و قالیباف را هم تگ کرده!
در یک لیگ دیگر است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18004" target="_blank">📅 16:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18003">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0ONAfl3m2N2LywO8FxmjKhOdoc5l1yXwcyn8UEm6rLyedhVZV3CQozyOIEINEE-q84vVDdZVaL7PQvbvK2cQEGwTYJz59HodJLiHnf7rDNc-gIQrLd-coxMNxJ9HL-9jVTjg5gqWY_xZ5UF5FIMZYC1oGXKh7GaAwIq96DCKabGmKdVSe1J76MnEsMZRbpmjXH6PgzfKxWCKGHM9GRvgIt86jbj-7T4L3RxqRY0OjgCWhABG7CEZ11iokr6ywMQ-pC9xBvUFMV_v9P5uGTuHsPy9VeHrvsPfKCWwzeCdz7UPWlq6Y6pOAm1vcWlwsEZxNJAtMALNsJ2mYH9zWwplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18003" target="_blank">📅 15:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18002">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فرمان پوتین برای ساخت نیروگاه هسته‌ای در ماه تا سال ۲۰۳۶   این نیروگاه انرژی لازم برای زیرساخت‌های سطح ماه را تأمین خواهد کرد  پس از سال ۲۰۳۶، روس‌کاسموس قصد دارد خودروهای هسته‌ای را به فضا بفرستد</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18002" target="_blank">📅 15:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18001">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18001" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18000">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18000" target="_blank">📅 15:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17999">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/17999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_394
🗓
june 26, 2026
✔️
تحلیل گزارش PCE آمریکا
✔️
بررسی تقویم اقتصادی روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17999" target="_blank">📅 12:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEXqBJhsCqMXQvEpJZ1Q6pNtDMTPpLgll-63qYpi8FOIHLincwHp5yqyFlgOPy-BJWQzAtQPedkXt5EXEExFPRLms9NgAT1WV4_R2R3ojWYa4OCA77d2IAWvxvCuRfikmyueBeqHnG3I6dDGvrIIRukWavWeb5fQItSruOLb17cLEKe-64b3h_qXyreG2IRmdnk-RSpPiuz7QQQ7orqTjTspR0but4BIUvVxgbu-7fqU9ieHfv-P-gMv4EdDDcMzmHYuyUgZC981bG2v_UPWg6rNQ1Q6FV44FqSLoVmXwXGRn5Auf5uJI-Kp_Le-A4Beak7PfvqDYznBYvFih4M5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8z6KbQrf82-7b3Lm3cWRoNOn11fY-vcZ22t4Y270dRGUKpN5nOzc1uLQ4ulEOfhn7CpJzAvyCt5wWdSPj5u0ZerVvjCf1Oj5hnTCasmE9V0AJKRxwmd7qpO9_DIXiNafHT2lZOi67MpcgfUBtpRUi_vs4PeGdYW_O02LLul4G5pyMnq1UQBoht73xWLNmO-AqmmV9Co-b4SiYqZ2DAsx9Q6C0u-iympfhVf4T6aSAfKCEAYuPU1acLtoGLuyi4JkKR9t4XJXAVtj9K_V5aVrYp-Bvavcqnkvtysb0yvkMYFVD8YRykc7CypJipGwkHs6MIAuN2xP94xh3La9FKukg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه وزارت خارجه ضد مواضع مشترک آمریکا و کشورهای عرب خلیج فارس</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17997" target="_blank">📅 11:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پنتاگون در حال بازنگری در استقرار خلیج فارس است و جابجایی نیروها به اسرائیل را در نظر می‌گیرد
طبق گزارش‌های رسانه‌های آمریکایی بر اساس تصاویر ماهواره‌ای، ایالات متحده در حال بازنگری در وضعیت نظامی خود در خاورمیانه است و در پی آسیب‌های گسترده به پایگاه دریایی کلیدی بحرین، جابجایی برخی از پایگاه‌های خلیج فارس به اسرائیل را در نظر دارد</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17996" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بیانیه قرارگاه عملیات مرکزی خاتم‌ الانبیاء (ص) :
تحرکات و حضور جنگنده ها و هواگردهای ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران را اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17995" target="_blank">📅 10:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ حرامزاده تا کنون همه ملت ها و رهبرانشان را — از کانادا و مکزیک تا اروپایی ها و عرب ها — تحقیر کرده جز:
— چین
—ترکیه
اولی را به خاطر قدرت خودش و دومی را به دلیل مجیزگویی رهبرش
برو قوی شو اگر راحت جهان طلبی
که در نظام طبیعت ضعیف پامال است</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17994" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17992">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یونجه و سویا واسه من
تنگه و دریا مال تو</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17992" target="_blank">📅 10:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17991">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بوی گندم مال من  هر چی كه دارم مال تو</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17991" target="_blank">📅 10:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17990">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">#نمیپذیرم</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17990" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17989">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ:   ما یک بازار جدید داریم، نامش «کشور دوست‌داشتنی ایران» است. جای زیبایی‌ست. کسی دوست دارد برود؟  برای تهیه مواد غذا مشکل دارند، قرار است مقداری از پولشان را بگیریم و  گندم، سویا و ذرت، بدهیم.  به مقدار زیاد. روندش به زودی آغاز خواهد شد. معامله بزرگیست.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17989" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17988">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ
:
ما یک بازار جدید داریم، نامش «کشور دوست‌داشتنی ایران» است. جای زیبایی‌ست. کسی دوست دارد برود؟
برای تهیه مواد غذا مشکل دارند، قرار است مقداری از پولشان را بگیریم و  گندم، سویا و ذرت، بدهیم.  به مقدار زیاد. روندش به زودی آغاز خواهد شد. معامله بزرگیست.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/17988" target="_blank">📅 09:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17987">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📡
ترامپ فرمان جدیدی برای ساخت کامپیوتر کوانتومی قدرتمند تا سال ۲۰۲۸ امضا کرد
دونالد ترامپ با امضای دو فرمان اجرایی جدید دستور داد تا تلاشها برای ساخت یک کامپیوتر کوانتومی قدرتمند تا سال ۲۰۲۸ سرعت بیشتری بگیرد
این اقدام با هدف تضمین پیشتازی ایالات متحده در رقابت با چین در حوزه های هوش مصنوعی علم مواد و شیمی صورت میگیرد
همچنین آژانسهای دولتی موظف شده اند تا سیستم های حساس خود را تا سال ۲۰۳۰ یا ۲۰۳۱ به رمزنگاری پساکوانتومی مجهز کنند تا در برابر حملات سایبری آینده ایمن بمانند</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/17987" target="_blank">📅 01:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17986">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الهام فعلا استراتژی مالش را آغاز کرده تا مثلا خود را در دل آمریکایی‌ها جا کند، غافل از اینکه ارمنستان با چرخشی عظیم به سوی غرب، در دلبری از واشنگتن و تل آویو ، گوی سبقت از باکو خواهدربود.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/17986" target="_blank">📅 00:47 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
