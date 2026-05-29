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
<img src="https://cdn4.telesco.pe/file/fQYvqGzRE0SKhC4z7cWwHNAsdDrQUWsUBW5DYnr23rG_zXk9n90U_6mCyhcKCvUpnqLWDyOxoCVp1qfl6R_dmIg-Btfxrc7Dxxgbv0i446N75ByPAA-mntxPNOAVOzYXIwGMhvwR-FsB-i0DTk-NQBwbu_Nb7tQSHt6YFQaorr1sBu7EiWdIAZVVvl_s9KBtpRWIzVl2hUA7_4mPozPIlK5hvXs4KwgdDkDkySUSmhJRFx8c7pIoUxafJVvhsHra1gWWLnqeg-L75NDjAYVFVQzMkkz3o7B3yNNagcWFZJwvirXbFH3e_NcOErdaGkEYxlKc3qAzd2gPgwHw1a93Hg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 180K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-76256">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">واقعا تلگرام ریده، میبندی بازش میکنی ۲۰ تا پیوی میپره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/funhiphop/76256" target="_blank">📅 17:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76255">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینارو خودش لیک کرد که کسی لیک نکنه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/76255" target="_blank">📅 17:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76254">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">قبلیو نمی‌فهمیدم چی میگه اینو میفهمم چی میگه و کصشره</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/76254" target="_blank">📅 16:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76253">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وایستید یکی دیگه انداخت بالا</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/76253" target="_blank">📅 16:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76252">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Demo
Amin Tijay _ Members Only
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/76252" target="_blank">📅 16:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یکی تیجیو نجات بده</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/76249" target="_blank">📅 16:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">محسن رضایی: محاصره آمریکا رو می‌شکنیم؛ حالا چه با جنگ و چه با مذاکره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/76248" target="_blank">📅 16:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزیر امور خارجه عمان: امروز با معاون رئیس‌جمهور جی‌دی ونس دیدار کردم و جزئیات مذاکرات جاری بین ایالات متحده و ایران و پیشرفت‌های حاصل شده تاکنون را به اشتراک گذاشتم. از مشارکت آن‌ها سپاسگزارم و منتظر پیشرفت‌های بیشتر و قاطع در روزهای آینده هستم. صلح در دسترس…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/funhiphop/76247" target="_blank">📅 16:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0gP2lOi7StsABOqcmvnv2GkyyVA9uUKeX7wBPK1C_Ph7Uj84WnRYdweM4AKEb23-7b1anBew1UXLw22-4aSBCS785I9Ag5Xc5KHl5kx6k9wBn1DPeQiaTMFCYGH6s9pg_RfgyR36ANGY6s7eiNHIMg-vQtlN4izIcatRPZ0tC5-jiqSfak2tsiTRl_rZGeCFW2dIgvX5OXrVPlPxFfsW-01nFkqddWU1gPBtc9gPp2nlhwMYJaOmsBarvdqya6957pAXXNWa1i-JQvmKD0aJ4g1HsPRxEEUaIuUMUO7jGKCblVDvt7ZMCYzeuZgurtnAjggpZ3OM6_Zy6TtpWxYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه کاملا آماده مذاکره و امتیاز دادنه:
۱-ما امتیازات را نه با گفت وگو، بلکه با موشک‌‌ها می‌گیریم، در مذاکره فقط آن‌ها را تفهیم می‌کنیم.
۲-اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است. هیچ اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد.
۳-پیروز هر توافقی کسی است که از فردای آن، بهتر برای جنگ آماده شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/76246" target="_blank">📅 16:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟ هوش مصنوعی میگه برمیگرده  @funhiphop | reza</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/funhiphop/76245" target="_blank">📅 16:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟ هوش مصنوعی میگه برمیگرده  @funhiphop | reza</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/funhiphop/76244" target="_blank">📅 16:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟
هوش مصنوعی میگه برمیگرده
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/funhiphop/76243" target="_blank">📅 16:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بارسا هر خریدی که میکنه فناش فرمین و اولمو رو میندازن نیمکت، تهشم این دوتا از همشون بیشتر بازی میکنن</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/funhiphop/76241" target="_blank">📅 15:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گرمه خوارکصده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/funhiphop/76240" target="_blank">📅 15:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObPfgWSHCHnizKRNGsHLKLJiP6JYw5cdGmzfdrMq5Kc0YwcQ4ZtOVDzmdd-sXObExOl-aCbxcPuTkeQFdd8HGRd6aHSEFqu9NaaqwdOARcf5lYX0DFvtfA9MmObA3ASFY4dsEVMji5Berv8pJoDv_UogAcdpVfBDw3A8Ya5Gr4pmvquh8QfC6vijWylYLq8F7JZZop8j9QHu8mV94sC70sniri5pwiir8s0u0GzF0Ud3wKOYGVx8Ma3qWt-x3OzzQ_R6Lqb-TP62VdxKC-Qq04MF9CHVLH4fzoMvGvM1d0Nc2w36N24Iw51Bk0X_SZKhOid75eYXjnNmTDv8TOSndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده: مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم جدیدی در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده. شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76239" target="_blank">📅 14:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده: مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم جدیدی در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده. شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76238" target="_blank">📅 14:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده:
مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم
جدیدی
در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده.
شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق سرمایه‌گذاری پیشنهادی برای ایران است - که طبق گزارش‌ها حجمی معادل ۳۰۰ میلیارد دلار آمریکا دارد.
ایران در ابتدا این را به عنوان غرامت خسارات جنگ (که بین ۳۰۰ میلیارد تا ۱ تریلیون دلار آمریکا برآورد می‌شود) طبقه‌بندی کرد. طرف آمریکایی آن را به عنوان «صندوق سرمایه‌گذاری» بین‌المللی که به تسهیل آن کمک خواهد کرد، بازنامی کرده است - چارچوبی نرم‌تر که از کلمه غرامت اجتناب می‌کند.
به نظر می‌رسد این ایده از سوی استیو ویتکوف و جرد کوشنر مطرح شده است، کسانی که پیشنهاد دادند پروژه‌های املاک در تهران و مکانیزم سرمایه‌گذاری گسترده‌تر به عنوان مشوق‌هایی برای این معامله تقویت شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76237" target="_blank">📅 14:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مدیران اتلتیکو:
خولیان نخواهد رفت
مذاکره نخواهیم کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76236" target="_blank">📅 14:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ناتو: روسیه شب گذشته یه ساختمون تو رومانی رو هدف حمله قرار داده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76235" target="_blank">📅 13:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آه رسایی اینترنت و گرفته
هر لحظه داره ضعیف تر میشه
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76234" target="_blank">📅 13:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رسایی آقا مجتبی رو به پسر نوح تشبیه کرد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76233" target="_blank">📅 12:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkZ_zW-hK3wdtNqjySHS5iqEUiIqwxUur_3l0NGUXxnMTjb5y4eK2b19pNKjNZRrwB-HwZ1OLS7ntQKGyVADOV1uIyHhxoK8Zb_NwiPSlCwzB0wQzc5vk7K-580Ypi7tO50-2UU3NI-9u_auuLoSuO6efzQ0fT2DZW5T6JxqPh5qwpieHt0PdR93gc1ytfyu9XaO6XUDrrxn_2p7MijHhcYSKx8m6MN5sw-kzjaW2TJEnCKZka6ZD71V7cqkBrBIv3Chs-3MPEhOixi4Q66mtytxi4XTCmlF7v1rsWEzRH0vLxxLBsDyGGY523_m5YefzLVfcZGgDG65z1WUmXSWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی آقا مجتبی رو به پسر نوح تشبیه کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76228" target="_blank">📅 11:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8334aba596.mp4?token=U7N-bLTeax2DOSxxllKIj0M1ztC3pUp5_OhRIzapBHRHsXzReXVUqfmhSmdbQQ8bgfZ_bDvCUhdnM0XdDdagJToF1W4g3l9WJ8VOjFyVe2F4vSi8LSVlw3j7wp_gKFhgY9QLU1nyuuCq7hz_i4FHwznRB0jscdx2cUocGyZjUtJI7-w_L4nlqHf2j67mbD14q-3C0I0vDKjVGhm3Rouod_T1-74D4si7Mnemjvr9f2RnZfcaYfvc3PbAu4nR_6RIi9XLiNhJlJ1o_2GXWu5L7-t8oIVoPLht2PCbmIGd3-BCXGV8BpYLAGDLtP6l5qZI4niuvUguPuTM67ev69oYXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8334aba596.mp4?token=U7N-bLTeax2DOSxxllKIj0M1ztC3pUp5_OhRIzapBHRHsXzReXVUqfmhSmdbQQ8bgfZ_bDvCUhdnM0XdDdagJToF1W4g3l9WJ8VOjFyVe2F4vSi8LSVlw3j7wp_gKFhgY9QLU1nyuuCq7hz_i4FHwznRB0jscdx2cUocGyZjUtJI7-w_L4nlqHf2j67mbD14q-3C0I0vDKjVGhm3Rouod_T1-74D4si7Mnemjvr9f2RnZfcaYfvc3PbAu4nR_6RIi9XLiNhJlJ1o_2GXWu5L7-t8oIVoPLht2PCbmIGd3-BCXGV8BpYLAGDLtP6l5qZI4niuvUguPuTM67ev69oYXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب ایران ۱۲ شب به بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76227" target="_blank">📅 11:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چرا وقتی اینترنت وصل شد انگار قطع شدیم؟
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76226" target="_blank">📅 11:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq_3o4yFSixBiybGPvC7Ke0jVCAzlB7X7TNbFlkfyu7Lqf6OkJTwzeJO_RdI6bMtZMvC2iyyjhCQKLBDrgiWW5ouIl7g0NPYviqxq_LgXrzVd6JD2Uchwf7AE24w9EbvQNsQbDCYx3uqUGraBrH0WbP41eSCXs7e4V82GMr3Aj-XDhyueF_VgbhBG17eKtipHJtwMiPljAuom2tMGsFh_yXw9zuhky0zyYWiV_sgeLpTa-Jki-J8j5bPAkYzSungl9MtgKjgBq2-kLzttYGClyPg6PNjdWQzrOQ1ADogZVwjP1w4g4RfECa9Ubn7-3cP7ChRXmB1xl1h27RlHDevZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت کتاب پاور آف نگوشییشن، امروز به دلیل تخفیف، ۵ درصد افت قیمت و تجربه کرد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76225" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76224">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک جنگ آمریکا و رژیم اسرائیل علیه ایران را تجاوزکارانه خواند و اون رو بشدت محکوم کرد، او تاکید کرد آمریکا هرچه سریعتر باید از این جنگ خارج بشه  @funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76224" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76223">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUocsczEU2YwFzumEHE35JE3HXtNHt0xn_CAXnHtKcUFhqxn2hLdhFucJYU4IbYWG-m2FZkK681oYb7zQ4BxvzVyZMSq8uB2P5Wc8TwjLx6vFuoRTCgV5eaQvKfFjTj9u-wmd6E7ivfilfeKMdS5ZadL88NhvL1wCe1tEeAb3Vxl5C40_k3Y4I-xgNAWJSBhUIrpBEhBPm2vLoLOFO0-htLG2ZT81kL7e5fYigjKflv-TwpnXHonZyPoXf0e3PjrYF0eHLvZ-_Y5X_RReKCsrG5u2wqhJE3n9L9I9lF6dnRC6yqZ9Jln0bJVtnHe7SZ_Cw23PENvwzGCqa-a0BTsNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک جنگ آمریکا و رژیم اسرائیل علیه ایران را تجاوزکارانه خواند و اون رو بشدت محکوم کرد، او تاکید کرد آمریکا هرچه سریعتر باید از این جنگ خارج بشه
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76223" target="_blank">📅 10:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76222">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhixyyaI1tw8D6lW4QdmJoJTOp94skGhYjIWo-AH4_D1r9hgNHL1t85I2UW9JDGnwb37LuBG4iZsyw09QH1kX63aBvt0jyBZbGR7ET0DO3t-2mztyS-RRrxKwIar0AbtwB9jHV29IcSchCZHcPAPQ2_oOPpsKVPXhYtCKiQlhpS8YgaYZEkHI9Hc-k4Ir_VAYdtO3n4x7NtTiftmGceqf2NELFqyElv77zs6-e1L6Tmw7J83ti2T2Jkfs5CU2_p213m_0wQpSwdSF34-1N_MFKZqGUtK7wWxeHyw0NgDW3sPeoJNV1bYMuZlH-ouzrf5z-5o3Qv_SCBa7iKVirBtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا افتاده دنبال گواردیول میخواد باهاش قراداد ببنده.
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76222" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76221">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76221" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76220">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSSrhXXjbEL7WI8NrrmH-hgrV5X9CTgsowzzXA24mo1JUqoRUQwc0H4P88uADb-m7kVtf0Dh871wfh_yELS7cWno58-hQAbUsA1SKtBSUMXVPumgLR7ECjcoaY_7nDDenC7_K8dLXnEIhAgHZOgh7ucfikLhDYzGXERwN30gYxmU9A69pxQOnNTFsiB1ZJDgJmc5HM3rnhysWPExCq9jxfDq_xlA9MVvC7Isc6TuTD34NxZ5arhNAOaFbVRPM_5t7_iTKijPgOiXAfeFALw8YhpJ5-B6l7-CDTKWfeYdNTEEAFQolZURit-1hJN3FZl06LSbbvUXe-vV7bATIV7fYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r8
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76220" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76219">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سی‌ان‌ان:
حداقل 50 تونل دسترسی به شهرهای موشکی در ایران پس از حملات اسرائیل که آنها را مسدود کرده بود، پاکسازی و تعمیر شدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76219" target="_blank">📅 09:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76218">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرگزاری مهر: هنوز مطمئن نیستیما ولی فکر می‌کنیم یه پهپاد MQ9 دیگه از آمریکا رو امشب نابود کردیم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76218" target="_blank">📅 02:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76216">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دکی واقن دکتره؟</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/76216" target="_blank">📅 01:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76215">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اینم گذاشت چنلش گفت بگم اینایی که باهاشون عکس گرفتی شغلشون چیه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/76215" target="_blank">📅 01:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">۹۰ روز از تـرور سید علی خامنه ای توسط اسرائیل و آمریکا گذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/76214" target="_blank">📅 00:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امشب وحید جان خبر از چند انفجار مهیب و لانچ موشک تو جنوب کشور مخصوصا بندرعباس داد و تسنیم هم الان گفته به سمت ناوهای آمریکا و کشتی‌های تجاری‌ای می‌خواستن از تنگه رد شن چندتا موشک و پهپاد شلیک کردیم که خب چیز خاصی نیست خاورمیانه‌ست دیگه.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/76212" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=L52u1P65q_Tanr0tD32-HvUwpJngUlNrmLI_OWrJ7CbSlMv_rq_TsBMvgCb6SXFrK8cj7A1XE5YBM5dFDwf2T_mRRYuu-RmrvRQjWGwF3zdIqOfiWRBG3DGedxgwpqFp5EDwR_rPYQCeN_g4-uWRyRzX21gBc4JfV0Liwy7edu_D_ZsFYZ-1syltAZyJwM7vtu6cgBHH73TD6-KkoOIhhKUYXkvGgGFo04cfWSdu0YOYRHsJUEyE2ZnqLZzlvgrGccCRpRZa7xvcMI3wDNkPj3quUFVkMpMHmtI9JFEMA2ro_oucY2lB_wD4390rIdIeChoj2GhbYmXPLwBYBtoFyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=L52u1P65q_Tanr0tD32-HvUwpJngUlNrmLI_OWrJ7CbSlMv_rq_TsBMvgCb6SXFrK8cj7A1XE5YBM5dFDwf2T_mRRYuu-RmrvRQjWGwF3zdIqOfiWRBG3DGedxgwpqFp5EDwR_rPYQCeN_g4-uWRyRzX21gBc4JfV0Liwy7edu_D_ZsFYZ-1syltAZyJwM7vtu6cgBHH73TD6-KkoOIhhKUYXkvGgGFo04cfWSdu0YOYRHsJUEyE2ZnqLZzlvgrGccCRpRZa7xvcMI3wDNkPj3quUFVkMpMHmtI9JFEMA2ro_oucY2lB_wD4390rIdIeChoj2GhbYmXPLwBYBtoFyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هنوز مطمئن نیستیما ولی فکر می‌کنیم یه پهپاد MQ9 دیگه از آمریکا رو امشب نابود کردیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76211" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76210">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">میدونم برای وصل شدن داری سرویس میشی، منم همینطور  ولی دیگ بسه بیاید یه چنل آوردم براتون سوپره کانفیگاش، کانفیگای رایگان میزاره که وصله همه کانفیگاشونم از قبل تست میکنن رو همه اپراتور ها، خیالتون راحت. کانفیگای اختصاصی خودشونو هم میزارن  خودم تست کردم عالیه
👌🏾
🤌🏽
…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76210" target="_blank">📅 23:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76209">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">میدونم برای وصل شدن داری سرویس میشی،
منم همینطور
ولی دیگ بسه
بیاید یه چنل آوردم براتون سوپره کانفیگاش، کانفیگای رایگان میزاره که وصله
همه کانفیگاشونم از قبل تست میکنن رو همه اپراتور ها، خیالتون راحت.
کانفیگای اختصاصی خودشونو هم میزارن
خودم تست کردم عالیه
👌🏾
🤌🏽
اینم آدرسش
👉🏽
📡
@VPNir404
👉🏽
📡
@VPNir404
👉🏽
📡
@VPNir404</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76209" target="_blank">📅 23:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امشب وحید جان خبر از چند انفجار مهیب و لانچ موشک تو جنوب کشور مخصوصا بندرعباس داد و تسنیم هم الان گفته به سمت ناوهای آمریکا و کشتی‌های تجاری‌ای می‌خواستن از تنگه رد شن چندتا موشک و پهپاد شلیک کردیم که خب چیز خاصی نیست خاورمیانه‌ست دیگه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76207" target="_blank">📅 23:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNuf-4Wduw8uUESY_9Y8HFCy5HvN2J7hjmKXl2wMm8mFWnEDsmxmQ7qrLWoPSugYGJBMMNtCkOjMm5WcsjPMtx5ktFRD7hDmJ8M1j0Yji9IBEGqSYUznovSOM35w-MoGmJq4JHogxNy11g4NGdLkqgBSQoseWdUF-gWkIx4BWBKjRo9NDsz3_hZrj6tkWATn2U0B96IUm1L17KDAehtEo-mwUwTPRB70yCPjGHLlWGgJWX2vYQr3xSCxfhJFs1vlzjBnyVbYJ72GkzerI6UPxQn5ZJa7nO41Lp-aGKVgYGiXOVEU1qbiWgdoHLNLSDdv27MVdRZGmFZ2hPRKuNrt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه داداش بخدا من خوشحالم از این که اینترنت برگشته و مردم میتونن وصل شن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76206" target="_blank">📅 23:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76205">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این گروهو زدیم که فقط میشه موزیک فرستاد
بیاید موزیکاتونو ول بدید و ی پلی لیست خفن درست کنیم
(فقط میشه موزیک فرستاد نمیشه پیام داد)
@Hiphopiplaylist</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76205" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76204">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیمار:
حتی اگه جام جهانی رو از دست بدم خیالم راحته چون برزیل وینیسیوس رو داره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76204" target="_blank">📅 22:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76203">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epmEbh-5gKv3qGqwC9V2c4_3ZmVfSAdKgAByg0jGvYY-4A_5tIysqosvDct2FiNr-cXtZ7UpqOLHwUITqY4AfzI6XTM80kgoPQbSoK_l96vjKKHY9syL-eymMjFFf6fTT_XGI-UJvDp3k7j_S8ym2hUPlUPHPYyDSsr2IxqnrzfXU1pjPEBmwKdffdpm2544FAOmYc5DBB-P32g2zYQvcmUT66vlsXyz8JbR_J5CD1VZL2_e1lPpSNvNPcks_umX2sPZ_mBW8pWlLtrnLJL93tg87zWwl_AQqEF8dE5hraRSrQ08MAkmwU_KkTv32Jy1dDkN0t362cFfT8L2Iwg_og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی انقد کصخلید یه توییتی رو باور میکنید حتی بدون این که به تاریخش نگاه کنید یا ادا در میارید
یا واقعا با این شوخی کصشر خندتون میگیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76203" target="_blank">📅 22:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76202">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نیمار تو تمرینات برزیل مصدوم شده و معلوم نیست به جام جهانی میرسه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76202" target="_blank">📅 22:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76201">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76201" target="_blank">📅 21:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76200">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پرزیدنت پزشکیان:
ما مذاکرات را برای تحقیر و تسلیم انجام نمی‌دهیم، برای این انجام می‌دهیم که از اول هم گفته‌ایم که به دنبال داشتن سلاح هسته‌ای نیستیم.
ناآرامی‌ها در منطقه تقصیر اسرائیل است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76200" target="_blank">📅 20:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فرید رومانو:
برناردو سیلوا به بارسلونا
هیر وی گووووو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76198" target="_blank">📅 20:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76197">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">من کاری به این که ویناک قبلا چیکار کرده ندارم، ولی تمام این فشارا بهش سر موزیکاییه که داره میده و اینه که سر پرونده هاش بهشون باج نداده و زده بیرون از ایران
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/76197" target="_blank">📅 20:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76195">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnlNgAsW5kej9mic83GW_P7JahYAs5tXpupEVWb7Xw1d3rYV2FYFxxRb8OX_4lZ62n63326D7wQm9aD_jDi19youhcA2MYM0FC6WE-A5hSj6Kg1iqXqJEAE0v8lVXrfaHFNBh8WRKB1h-1TIjZfWnu0-f8WZTYezhHziB7uxsIz-qQaM78Cf4vipb3crBErz6JTvWw_5Bin2xCudPO4_S4CvLmB7CIP-sjeKz-B6Tk18fDg74pTGiAtXkDScRrQ4SJ4ngQ4lt8HFid_du5c_vUIhXIbR4frpzIUtORITrz6J2dSM19YvRnqV_8US0QZy9btQsM1K5Z1NV38LxUTWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76195" target="_blank">📅 20:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76194">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">امین منیجر سر کیری که ویناک بهشون زده و از ایران فرار کرده فشاری شده و داره میگه تو ایران بودی خایمالی مارو میکردی الان رفتی بیرون بهمون دیس میدی.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76194" target="_blank">📅 20:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76193">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان من تازه آنلاین شدم، ترک هایی که سورنا و بهرام بخاطر اعتراضات و حمایت از شاهزاده دادن رو بفرستید گوش کنم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76193" target="_blank">📅 20:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76192">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک دیپلمات ارشد اسرائیلی به شبکه ۱۴ اسرائیل: تا جایی که می‌دانیم، این توافق توسط رئیس‌جمهور ترامپ یا مجتبی خامنه‌ای تأیید نشده است. اگر توافقی وجود داشته باشد، در حال حاضر هنوز در سطوح پایین‌تر قرار دارد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76192" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76191">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یک دیپلمات ارشد اسرائیلی به شبکه ۱۴ اسرائیل:
تا جایی که می‌دانیم، این توافق توسط رئیس‌جمهور ترامپ یا مجتبی خامنه‌ای تأیید نشده است.
اگر توافقی وجود داشته باشد، در حال حاضر هنوز در سطوح پایین‌تر قرار دارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76191" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76190">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_5jNX2iMltaOFCcdD3t5Rv-1H6DzkFzBFBcFh9dSL_UYd0RmaV_UglTFiepJBvVwx1m5LXOITjcuzhdYoZ0rbOky0ZXr_P2TiO7FetLE2VYyE0jys5-qe5MLZzxYjgffVuxVP8Gwl19OXjAso1GgwgzF1JRGwoGj8p6b9rDWTtzyuRAf41z9849hY-aGiHL2a0COCx6E8_rydZMuLmrl-mmB2BOTklyi-HP_PDNzgz3LaS69QmA9mICcEbL8JYST2jJ4BwhoLkii01-0JSN67yoy-VewWM1fKrsrLfWGdMG3rplw3J5pr3JxaadC7vM36BguYn-dh6DlIjVseL1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76190" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76189">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل: مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76189" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل: مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76187" target="_blank">📅 18:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل:
مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76186" target="_blank">📅 18:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا: ایالات متحده قصد دارد دسترسی خطوط هوایی ایران به حقوق فرود هواپیما، خدمات سوخت‌گیری و فروش بلیت را مسدود کند. سازمان مدیریت تنگه هرمز که توسط سپاه پاسداران تاسیس شده، مضحک و خنده‌دار است. دولت ایالات متحده هیچ تلاشی برای تحمیل سیستم…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76185" target="_blank">📅 18:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
ایالات متحده قصد دارد دسترسی خطوط هوایی ایران به حقوق فرود هواپیما، خدمات سوخت‌گیری و فروش بلیت را مسدود کند.
سازمان مدیریت تنگه هرمز که توسط سپاه پاسداران تاسیس شده، مضحک و خنده‌دار است.
دولت ایالات متحده هیچ تلاشی برای تحمیل سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
روزهای ترساندن منطقه و جهان توسط تهران به پایان رسیده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76184" target="_blank">📅 18:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آکسیوس: توافق در واقع همون سه‌شنبه به دست اومد؛ حالا فقط تأیید ترامپ باقی مونده تا همه‌چیز نهایی شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76183" target="_blank">📅 18:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">واسم سواله سود این تفاهم نامه واسه ایران چیه دقیقا؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76182" target="_blank">📅 18:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76181">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جدی جدی حزب‌الله و مثل آب خوردن فروختن</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76181" target="_blank">📅 18:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76180">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76180" target="_blank">📅 18:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76179">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76179" target="_blank">📅 18:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76178">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76178" target="_blank">📅 17:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76177">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76177" target="_blank">📅 17:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76176">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل:
ما باید ماموریتمان را در ایران را کامل کنیم و من هر روز در این خصوص با دونالد ترامپ صحبت می‌کنم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76176" target="_blank">📅 17:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76175">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">روسیه:
ترامپ با انتقال اورانیوم غنی‌شده ایران به مسکو موافقت نکرد
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76175" target="_blank">📅 17:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76174">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLCOrpH7fybh5Nrm_jFEceyx72sKAwGhLlnnfmzL2y1l_8E6tazFBsnB5kbofQj0hnvx16AgaCD0Sxlh1XJ1Bv2U5t2R10MLUUwAtuhiqhkN3vfJfX8jOAxfOBliGrlAYulmUSpWKUMaa8vj9E1csbivP4Sx_wxh12_AMAEMtl08PloinDc133Mo_FHiGfEegDWzFXLzujwSE3KdouzqH8rzm07ys62VDoVJd2NH54pR6aXLKlPjEAkk89XLZSW_bbuok8bxxrFEK0HkQBf-gFAc0cBzBYIcndm0Cd_IIsC1WI5qss3x89tWnDI_KuXN7mNlwpuwDYbOret2YT0gYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اما مسعود که بود و چیکار کرد.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76174" target="_blank">📅 17:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76173">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkbgaLLDmgjukPG-wXVUIfcKuV1Pvzf0ffQx7FFkUHGo1a9rRsSZ8yPuh8N_r_VNc2wFTXX9iX-YAYAo50lVXvXoP-OWqxbYgmR3-hoVYTWV0YppUAXYD8DmLRnbOGQmKTHWdoS0Ew_hzMXF-i3zpKBJj07PzPSnPkb9vYlQJjmhuu_x_K2--wjUWXtMnqe_Rfp8IzONZLaHboSh7yRGdIHYCuNN4_kvj8IbzBU5DUgVGiE9opx4fZRKosj3nZwMr66BqmKDWADEvZKiEDX1wV2WEh56fMNY6WNjIdYxYgqbs1MkdPmW7RyjIz5nfClU1wHf8WZjaBxZSB4rzVvoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g7
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76173" target="_blank">📅 17:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76172">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارش های تایید نشده: فرمانده توپخانه حزب الله توسط ارتش دفاعی اسرائیل ترور شده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76172" target="_blank">📅 17:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76171">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pju_zNIA8e37F-NBYOF1d9MEsr3jY2O-4dZRxyFj-Ze4g_T2fN_N09TEitBAKMs0_wa9LhaxwWk72TbjDwAL88DYYnZH1akwD9x-abnz11IRK46O_0FIk4xOJmqQgWxZLJuZDjTfXAxzUh6DmwUHdi_IYHmtInjYPYa8ek8HIYSsrsx8DpsxUmfUY30uPfbPn4lPwRrAuOu6QMdHOj7Zh4C7QyXxc0v1oU4T3iVuR8lZwnvR0wI4VLgcWoYYgJxj7e6jAe5qfUuUktjU4HGkISST4VCGpBKI5mZ7U7xGQ9ucG-ep5TJ9Le8C93j-NVm_vbrk4CRZ9P6T4D_S_mjvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76171" target="_blank">📅 17:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76168">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الان وضعیت جوری شده نه دیتا سنترا کامل باز شده کانفیگ فروشا بتونن تانل بزنن ارزون بفروشن نه دیگه مردم کانفیگ گرون میخرن، همه به یه استوپی خوردن که معلوم نیست چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76168" target="_blank">📅 15:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76167">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">من الان دقت کردم موزیک یه رپر نو نیم به نام مارسلو تو چنل ارشیو بیشتر از ترک جی جی فوروارد خورده، بعد این پلشت میگه دیگه کسی ابی داریوش گوش نمیده مارو گوش میدن</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76167" target="_blank">📅 15:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76166">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JI7QKlBejqnma_uDVhKzDc0B-5AMH2ZDX6XchuwPv_PiKV-Otn0Lfi0mHtp9lOQ0kR0PgRy_eikTpD5RP6wGHhh1vngnCGdWRQgsLB-WYjSHm6UkAxP3UjISVHv3CkTcLye40arxQJ8k0qgLsbG7Z0lbTSYsCa_r7omsqDkbtHXb7st9bCSy5doTjb3MoqU4Ymn-k7ZID3z355z_gjE9NeaB84xJUHJUVdiQzHAtC7nvJCDA09EUAjLVv0DzNRY7I_J0kB3PXLlAGRmskjajF0qa3EGc8PurGXqP4Hx0zt_nuYkJvtxkoy9TOyFllbonVfj9MPI9icBo65pfDEUsTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به اسم پس میگیریم منتشر شد
Youtube
Download
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76166" target="_blank">📅 15:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76165">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ویناک ترک داد
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76165" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76164">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سنتکام: حمله صبح امروز سپاه با یک موشک بالستیک به کویت، نقض فاحش آتش‌بس بود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76164" target="_blank">📅 14:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76163">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">با شرفی ازمون تمدید شد
سردار آزمون از لیست بلند مدت تیم‌ ملی ایران هم خط خورد و دیگه به جام‌جهانی دعوت نمیشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76163" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76162">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانال ۱۲ عبری:
منابع آگاه از مذاکرات خبر دادن که طی ساعات اخیر پیشرفت نسبتاً چشمگیری از لحاظ رفع اختلافات میان ایران و آمریکا صورت گرفته هرچند که چندین اختلاف همچنان بین دو طرف وجود داره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76162" target="_blank">📅 14:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76161">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بارسا که دیشب گوردونو خرید امروز هم برا آلوارز پیشنهاد رسمی فرستاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76161" target="_blank">📅 12:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76160">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بنازم پرزیدنت پزشکیان
جوری اینترنت رو باز کرده که آدمایی که موقع نت ملی وصل بودن الان قطع شدن
@FunHopHop
| ALI</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/76160" target="_blank">📅 12:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76159">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه لحظه یادم افتاد قبل جنگ یسری جوک ترند شده بود که میگفتن "کشورو بدین دست وی پی ان فروشا چهار ساله دارن یه قیمت می‌فروشن و گرون نکردن"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76159" target="_blank">📅 11:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76157">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صداوسیما رو باز میکنی حالت بهم میخوره، هر اوب زاده ای رو آوردن تو هرشبکه ای داره تحلیل جنگ رو میکنه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76157" target="_blank">📅 11:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76156">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oywizCOzOSoTVezRHLqIo3V7z7X0L9UMLkcXMrpeFbxzaJ3DG7_TsWTyQHSD1zCHFSZ3Snj1itPH_cFEw1Clqx15bSn_M1xRPwi2nS_oslty-22swLoEMWmHodFlaiw0Y2MzZtMTqO6ZoVwN4wZeH6WJPiPJFnpLimQO-iCpMS0oLuuW6qzpk1_B3Iw6VGoYM5yperQjodyEr7p7m2qqxbfS1or0cLkEnVqvCtdtNw29jSxrzpIUYqZiRmMumABMJ6fIuHNSNt-kSPHxPIacVKHKemCgfGBPKcCl0CPXtYpRwTXNgUZb_f0Z7BUQMertHUXjJ6HumIKRvTIEWzUHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکایت وصل شدن اینترنت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76156" target="_blank">📅 11:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76155">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQYM7mD_P-39ykEvv2X-4OB8BlhsirCezxQf0-EzfMHgr1SdRmrMvyrFtooIaoE23wOjoqnZXnwAaaBA8aej9mdcMdJIV9MdZbAGluSEAcvGLPmE31p8jS05zDyws0K2yMPAHqlQeiZI9B9qTW2wzvUV6xqgtqz3yTDgj1qqp2EtPHH_Dw4wcqWJjIy01tDmJQwWJ82fL0pvijujY3C7NCxLicdAYdON1A9Trm3wCZazgeyTJObW8pniHPZV1mI7EgH4NprCZv0j3Oi0I9xCtg0VVMjZTF3Open-41lqWWf8NtdjlPAUYPlp5vPUTN_bb7J6rpRowCvIVEx0OEkgbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امسال عجب کیتای شاهکاری داریم.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76155" target="_blank">📅 10:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76154">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بامداد امروز بعد از شلیک موشک از امیدیه خوزستان به سمت کویت ، صدای انفجار شنیده شده و ستون دود دیده شده که ظاهراً لانچری که موشک ازش شلیک شده بلافاصله توسط ارتش آمریکا مورد هدف قرار گرفته
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76154" target="_blank">📅 10:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76152">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-ZDIswVJVeaOlhb7PSLDG1FA7J3B8JksC_sn__fez2Cxr5XSY15JKCBIVoFypIrI7Lsk0NbI7orkT34iRKSziA6AzF6DpsTGji3X2eOImNEAbZweu5-puJlk-wzdFIyg7lF7MvdV9yqhbft517QLS58z-O2GZ5cZqPVdgfpl4wt4RfuhqCAlyQOsxCAFR316uf11qPhwFebCCN_PYFmZ7m0tJzgup-aokJW7E1jsZh2rIGwF5n71Nto8WDWaaD1M9tV9fG7ubnMjnLFOrOApF6wZ5ZYtPGfAgvab4XFiIuS59ObYJaexL1LDfc8KdhGi5k5RXbBxt9PcFFn6tSXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvRLPim5Ybc84FWoWzMWoiPLPP4QBQUIWzS7kR2mrztjTDBKuj8sD5e7Hy2_v_dhb6Blzv9KCqwCk264hQVe_dHppEXammYzER5ABstmhjyQPXi9XL0aDaNLwnZse4TygE5euJ11_sUja4Mmm5Lcr-5MStfQzM7TgARMXvVWQOBVoYSRtAq6phhDWA8phHFfR-M5N4idFKb0zFjDMhg1YfraBQf55fa_uNrprpeMIZ8FHL3kjuoF-uTI4ic2L8bK35x20FhUJYndGgR32szFzTB7D0idz1q2qQn32-OKDHPxMS6Z_Q1L-l7q_eAL_vf9mMo-rbc-HcN-vasP7rPb5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایز پات معلومه اوب داری پسرجان.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76152" target="_blank">📅 10:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76151">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrAz5yPfhozORcmTNekEhO56TeWsM5rrgFyj68W2vhE8GLB8zKG-iRPa3rxf5XqoWk6iHCXZUSPYWVEt8qqxl-Vyymko-4pIQE3dqsqHpcROpn6UnjigC7eeUw507ZtiYxAqElRXWL-D4ldJlmMhFlgcYmV04E58IU2qTtQOH9HMay16sQG1dTgjGMx8j2-8NbTfQLCSJBkZqCPpGvJIO5CiitzRQAzAono8qfkPojhU4fjrJSTw4Dvss0iCJqHZZtTIgpO_NNUzIXptLP5j0_CsEiNOz3bJ_rE-2fLrDj-_wcEVs7wErJL0a-wUFAWqI34gghJjUcsZ_G0lba4aTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت هیچوقت قدیمی نمیشه.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76151" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76150">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8zZsZX_E2Dr4fGevYdkDlDwmobeNv4FE68JLlByBZp5dlZzMHOrSGDbrOJ2LDITEmlDTh6YmMnXp7HOKUD6Brn21pBtQXfOrQ_SZyH-IRJf0LRVJqsVVT7upTTgklpFK56GtoFl9k5PmNreXWdRz1wD1GGszwSVk0Owb8VoajZHKqxGx8RIermdGE7Ul5h9jcKfNYe08e8KK9E7PQFxzm3dx0whOZ0yLg9lIRQO4JNmlKRGFaPDmHWpHRVAEiAzat3YF07N92P0RobfI84fg-wRi8LCmWvAW1-dVSM0B7ONTEsuB0Hdmjo1klD02scyY6s0gYEdZudt9sQG42xyqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیمی نام ببرید که توان مقابله با این طوفان را داشته باشد.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76150" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76149">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76149" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/76149" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76148">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRM8TshSwPaCoHSMinvFO2muyi9DtBDrFFPT67i1AZkBz5XEPV565ZcttYQ-VeTxCF8thnDbOV0RsaJtZeM-mureg2VIRJUoNHMzgPClZtPmd-fZ6KJvZr0wLCEs2IHfyJjay1gJMjWXgw-GCCk5cIG1ilpChVXtrbb4IHnmZg_nlJ5Cy0TBAV7f1sSt5vaIBq6SqWX8Ju31t4ZyHR4eb1z3hXzdoHQyVAi3B0eHalSooCOPWXFzn435RwjiORYOp9RePYkjr9D0zMi0R7boT5Nd0jVs0Oo-SvAx8EziaZwz6QR1qIMgSqBS2ls2mNNGpmGw8BLwQ-4vY0Tj6885dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r7
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/76148" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76147">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-GhiYlHhfUsHVeYru9GUBpbRYCx1NttA_ZRfbx_wFQH4h5ScmRcOPieNdPObdMn-tFrsunFuj-fBJp09Co4r-qH6g27yLbUG3AimxDRZbv2uYa_gzKMOmshQJDyMNubgjlnW7XU_TxKpogbETkXQVKFRsuz1JmLLjnVMFmdXZLrTjm9hDD265cXbTuEf5rGIPObbkTA_Ol2NnseyqUWAAar7QWJY8GNaMe5KoGk1KetqEjEj8oo6TUUqTG_85-o2SIVEcfOMD_Bf5UcTB4NlcSQbRhPZ-Bf4A4U2jFufEdSWLspv-pC-0E2Um_WQ_f2P0h3BvneQOo390h8m_pqvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرف
🇮🇷
🙏🏼
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76147" target="_blank">📅 10:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76146">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=FytilNhItNBtlzx9iVtny1K5fLX79Cux0CpZAOn_vNnc4mQLUkbCn5Tppbiazp2rhbac3885TEdElYHG_426ONJokYWiagjN7QTSFLNTm-UOrYUb8kyw0oNW0aqJqUHRhysuToPRQlaiKXW4XmGtdnWc7lLIWvpmX6W0Uq2HOZ6pVBriNXLuFfgQtDLODs3ieduJEpDOcfXU20Bcqo69a37s3CXglG62xCvsX2jVQBrxehzkbyVd88zqSaGvqNyejJlR61OoL4WGn8eqZtcTqQwUYrpu3m0gzkJivzvmznAoV3nKlVfxxEuqOmT7TrkT6TJGpV4qkX1lyLNmczmfYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=FytilNhItNBtlzx9iVtny1K5fLX79Cux0CpZAOn_vNnc4mQLUkbCn5Tppbiazp2rhbac3885TEdElYHG_426ONJokYWiagjN7QTSFLNTm-UOrYUb8kyw0oNW0aqJqUHRhysuToPRQlaiKXW4XmGtdnWc7lLIWvpmX6W0Uq2HOZ6pVBriNXLuFfgQtDLODs3ieduJEpDOcfXU20Bcqo69a37s3CXglG62xCvsX2jVQBrxehzkbyVd88zqSaGvqNyejJlR61OoL4WGn8eqZtcTqQwUYrpu3m0gzkJivzvmznAoV3nKlVfxxEuqOmT7TrkT6TJGpV4qkX1lyLNmczmfYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه که توش حرفی از نقض شدن آتش‌بس نزد:
بسم الله القاسم الجبارین
فمن اعتدی علیکم فاعتدوا علیه بمثل ما اعتدی علیکم
به دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه ای در حاشیه فرودگاه بندر عباس با پرتابه های هوایی (گفته می‌شه تلاش برای ترور یک مقام بلند پایه تو ماشینش بوده)، پایگاه هوایی آمریکایی مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع تر خواهد بود.
مسئولیت عواقب آن با متجاوز است.
و ما النصر الا من عندالله العزیز الحکیم
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76146" target="_blank">📅 06:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76145">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فان‌هیپ‌هاپ نیوز:
بازکردن اینترنت نشون دهنده پایان جنگ نیست/ تقی به توقی بخوره باز قراره ببندن و همین الانشم درست حسابی باز نشده. وآماده قطع کردنش هستن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76145" target="_blank">📅 06:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76144">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نمی‌دونم چرا و چطوری ولی همین الان آژیرهای خطر حمله‌ی هوایی تو کویت روشن شدن.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76144" target="_blank">📅 06:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76143">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3Ffu7eKyuFHJq4rhVPmyXU8cYl5FHvAuWMi9C-ZjGx4xn7DRJ0j0yJQF0ChoGLkQ9JHTNgirQJTj46RfIf6srJ_1x-tvMFSI6n_TcDsWGsSCv0F7UyXLXIqiWYdXjPNyYWWst-ipbOdfROf4S109xilJp_QGoWLGhijzzjXfb_GZ0_oyWkzm7CwPq2cdTRlqRjJqoJYynYcK-1nW_fjTACNxoPHOla7Q9g4xS5jISBFn2Jv4v0EKCBUsYKIal06JrAmPUZqhGPWH92JRzjQuMl9CqTFofCOaW-22bv3ZJbcjpsnHCTMBJRjbmKWEnAUGWnMaAm0zP3oROfVC2iSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم چرا و چطوری ولی همین الان آژیرهای خطر حمله‌ی هوایی تو کویت روشن شدن.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76143" target="_blank">📅 05:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76142">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اشتباه برداشت نکنید، قطر داره پولارو با جنگنده جابجا میکنه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76142" target="_blank">📅 03:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76141">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به گزارش رویترز، ارتش ایالات متحده حملات جدیدی را به یک پایگاه نظامی ایرانی که تهدیدی برای نیروهای آمریکایی و کشتی‌های تجاری در تنگه هرمز بود، انجام داد.
ارتش آمریکا همچنین در جریان این حملات چندین پهپاد ایرانی را رهگیری و سرنگون کرد.
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/76141" target="_blank">📅 02:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76140">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فارس: سه انفجار در بندرعباس  @funhiphop | reza</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/76140" target="_blank">📅 02:28 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
