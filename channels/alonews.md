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
<img src="https://cdn4.telesco.pe/file/R-Gx3Mz_-1VjddNgHpdHQYlLi50S90lyzFtJoT9VcsHiidNeojEi7Kja1faHJacZt63hd-dLI-JnWxoG2Q9lTETruhOCxHMEKzyF7WpPHgpU9gQNbSy2FcxtsaYvRRc2xFyojbHkHZLZvJ25l92iYaPrVoBD981nMoYXhtDPmOLXkDX1DzZrbNV9iiK9sosTd5rv2VMSSOk1hkwOhvQdhRg_qE1qQBtKaLXmV0UKeWUeCqrNnVz348Nge5nco1Ait1EdAR4a_LtYvJ5mFyufSUfl8V5iwUIpSgE_BpKAtG3bHyV7Le6IggbrTHNLlKFBVB1XUdr3GBUBp86EMUhAfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 927K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 10:19:16</div>
<hr>

<div class="tg-post" id="msg-131006">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سپاه: انهدام مهمات عمل نکرده در محدوده سرخون و ایسین بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/131006" target="_blank">📅 10:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131005">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
پزشکیان: توافق اخیر در هماهنگی کامل با رهبر و حمایت شعام به‌دست آمده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/131005" target="_blank">📅 10:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131004">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سخنگوی اورژانس آذربایجان‌شرقی:
حادثه واژگونی یک دستگاه اتوبوس ساعت ۶:۵۰ صبح امروز سه‌شنبه در ورودی چهرگان شهرستان شبستر به مرکز فرماندهی عملیات اورژانس استان گزارش شد.
🔴
عملیات امدادرسانی به حادثه‌دیدگان آغاز شده و بر اساس اطلاعات اولیه ۱۵ مصدوم تحت اقدامات فوریت‌های پزشکی قرار گرفتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/131004" target="_blank">📅 10:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131003">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ8mAY4pU7g3oMyihAPc_HB9VPCN1P-JhXk5jbM8R3TaxPagW3MjYBGD2fWLjrnVH5oyzknDl49MoXIbvVlgDO3HZTZSBUPRXiP-Z7UxR8occWClUKE9subMxDmGM5lEI-TvuXon-Kewxw3e8aY533anIkFN6YQe7lSOWoLmgq_BYzMrBOtabfKFN8wWkfkm04RnY1FSrbSbijdLy2Q0ebX0K2NwOFdiKI1sE_tFd01hQYMxWHAx2Jg4YpGCf5xEZeWyjoeKucSj2yJ_6FoVrMvxvixhROCLQghVIRQpf37ys3CYO47faCjEPO3T32X4xOvtdBCioEt8MTmZQ4wkeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: هدیه‌ای طلایی به کاخ سفید به مناسبت دویست و پنجاهمین سالگرد تولدش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/131003" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131002">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزارت خارجه آلمان: توافق آمریکا و ایران برای ازسرگیری مذاکرات، گامی مهم برای دیپلماسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/131002" target="_blank">📅 09:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131001">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
روزنامه جمهوری اسلامی: در جامعه سالم، مداحان نسخه دیپلماسی نمی‌پیچند / دیپلماسی با شعار اداره نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/131001" target="_blank">📅 09:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131000">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پولیتیکو به نقل از منابع: روبیو و ویتکوف به قانون‌گذاران تأکید کردند که ایران تاکنون هیچ مبلغی را بر اساس یادداشت تفاهم دریافت نکرده است
🔴
ویتکوف به قانون‌گذاران گفت که تیم فنی مسئول مذاکرات هسته‌ای، سوئیس را به مقصد قطر ترک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/131000" target="_blank">📅 09:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130999">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
دونالد ترامپ از خرده‌فروشان سوخت خواست که قیمت‌ها را «فوراً» کاهش دهند، با این ادعا که قیمت‌ها نسبت به قیمت نفت که در حال کاهش است، بیش از حد بالا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/130999" target="_blank">📅 09:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130998">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ادارات شهرستان کرمان تعطیل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/130998" target="_blank">📅 09:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130997">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbc09fa73.mp4?token=hNKQ6V-tdtKqp3YaEm6rookbYyuvJa4E6Fi8jq8Ifd8IosCn76MVo5CeD5pc0uD_QMSbKB7yl3de9sRlittE2_v_o07cP4VwL992TiNK0t9nUXpTeJATALl5MsBQTRQwM9jwZgRfTyQ2eN6W9Tne8FwDuqV542lKL9F7G1r-1rjAoPSuFrlpzWDtQhDC5QhShIZhwWgEMkbFx0rHSs7ViScly34DFk_IT75cCle3TPZraZg9A5xWKS1krX1m0EkDsRiwFwIr7h5jj5NlbkoPds-n2QGwyLezsM6lYgD712mPwaIdjbNaBECSV6njoJY6TTlIrA8aDpxLD5Xw2xQb9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbc09fa73.mp4?token=hNKQ6V-tdtKqp3YaEm6rookbYyuvJa4E6Fi8jq8Ifd8IosCn76MVo5CeD5pc0uD_QMSbKB7yl3de9sRlittE2_v_o07cP4VwL992TiNK0t9nUXpTeJATALl5MsBQTRQwM9jwZgRfTyQ2eN6W9Tne8FwDuqV542lKL9F7G1r-1rjAoPSuFrlpzWDtQhDC5QhShIZhwWgEMkbFx0rHSs7ViScly34DFk_IT75cCle3TPZraZg9A5xWKS1krX1m0EkDsRiwFwIr7h5jj5NlbkoPds-n2QGwyLezsM6lYgD712mPwaIdjbNaBECSV6njoJY6TTlIrA8aDpxLD5Xw2xQb9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در اردبیل جلوی پلیس اینجوری به یک نفر حمله کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/130997" target="_blank">📅 09:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130996">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnq3t7n30hxDOE288c4g1SQnM7JJbeKfgmUULMsl_nsVwyoH1bhFCxQOSuVX7_5wmyaf6xFCwIt10tG7MxaoQib7avYuqZNiiPMSZWdvD7LE5NPeDbHq5K2eHiSaEceecvyOdeXnkwyxqTi2XFFsCN1rzDkeFTtLtIv_u_VHROFhqxujZnXBtYtHi0I34bwIJsEnNj9uIvtK-qKTtgRdCWtucqvAfz-Tj8hlSM_Z0X3MsIKFSUWcSG4X70R3Km0o28l2yq3-z_6aTXpw4kb82cBeqGJlsgHJq8uapdKH8vvu-UsznzADpipGwaHkHH3AT1YrOrUohHAACD1w0kFpWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دریای خزر در حال کوچک‌شدن!
🔴
۲۴ هزار کیلومتر مربع آب کاسپین در سه دهه ناپدید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/130996" target="_blank">📅 09:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130995">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDxy-eo6I25_XsaNtKY4qJ4l3rZwT3GEL7nj3CI7IXHTbJQnYQTodq3d6PZzp9aMo3_Fwy266m6jcEnk8PuywV3boSr-15uWrrztNZ6IfDaIF-x-Svx8XkbWs73-nj39BAsFSJOJWrBPrFLg1T355GxPgMwYITDTIO6ZGtEW17_JG9NJr2Zb8nn_WwFhzAMAyiF6NcHY82wWtasAZRjGvIhbMEG43pzgnyTilQUQ24YUaZ0eTnu7O9xPL5B3Acf2xo7I7Ddkf8b44-4oi4fLhUDJ-5NjXtJI43uwTjJPhHgJpPqdJ-RO1wuYRNuyKj8z9qZdkT9xEpx45l7d6Lz9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش مشاور رئیس مجلس به ادعایی که نبویان درباره کودتا مطرح کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/130995" target="_blank">📅 09:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130994">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTqOXrWtNfQXI5JCi0OQt8sA6nHjAVqqEr6TiDdm6Bfa_6UZrtuEmKbduhz-scxd4CerrTlzrjqhlA3UXhajNCnhBeV0UlSfBWgUYfEWu517pvWmwzz6qruPjXk-4w_q9i7-3fTZaE8y_bx1qzYRww8ceQlD5eDwxww99HR_zjErVDFX30VEVCrufofBevBRI77HAmC1kCNpoFZoSJ3UybjurhY9XJGM7Y2QzBlEgSrA3rn8gSFZEhdhRLpy4WtML4yj0nk5RNH-1OYS7NyOPSRJsKBeae0DzUBaT-aVmdMPH8lhSEET6h16YfPzLr50Ow2h7YrMQ9_l-sBPk-tfvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: ویتکاف راهی دوحه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/130994" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130993">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
شبکه «ام‌اس ناو» به نقل از منابع مطلع: روبیو در جلسه توجیهی با اعضای کنگره آمریکا، گفت که دولت ترامپ هیچ توهمی ندارد که مذاکرات با ایران آسان خواهد بود.
🔴
روبیو به کنگره گفت که احتمال شکست مذاکرات وجود دارد، اما دولت می‌خواهد به مسیر دیپلماتیک فرصتی بدهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/130993" target="_blank">📅 08:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130992">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G46hkXXUV2N6KOTxWNc53w3JbSDTcahH4kVYYkErnutoEC-ySziOfv7R8Pk-lO7edArN8_Vcmal-ABQet1ai-vPHM46x0pngKJJBjAokMPxuPr6BL6no-1Hhw0WJm_cl-MJ2sYjFdSxrCENUO9a0hy_m2ndIC5-H59ILKjYFqIJtIUOYOpBfoCNt2vM5nuNyLZUn9RqpJFdDpUb8cDnAe1GfcTWa44w0B70k9zO8eLOEXkBpiIkOz419sFP9WxN_Lbo7DZWAXKbTbn8noicNH8d9qN5EGevH9M0V5rM1ybNXKeu-eas2xDpAc_rFXDXjJ6mHxdvc6fVxua9sB16G4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی 170میلیارد تومن از فدراسیون فوتبال حق الزحمه جام‌جهانی دریافت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130992" target="_blank">📅 07:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130991">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSCHJH1uCRwQe5m1YCSEZILqYYWWW5v0IRzFZehCk5D8579rAv_33Grr5c0szu_jinaX2D_O6oLJjLmNRh7MkdOw2NU0Vm7Gs-ARYw3yCBd2zjPsmOg39Cvz2Di238mfVdp2Yk-PRFhW1kBg5NPH8iyv-gBRSLFobBl8_6oidW_D5d1ok0lxW10MN8Msah_-kIKKIsDpKjhMzKJPCZBWD6-xaXqF5vGXKq9EfGvmmHkMtIzaTevAvvzNIeM14rysbZ3wHBP2Qa0bh-w8WMe0kvSxp8t1gdtu_e2OfomP8mqxxsXp_39JGjsGUpoX_L0Zm41-lGrcGhnEjxsbIhiU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: باید ترامپ را اعدام‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/130991" target="_blank">📅 07:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130990">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSooraSkyvia@chToolsBot</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4RfI7CpdUrH7S9uS135CmwlQ4P1Sfs6QK7YD4Ro6TwWYmW_-dWkvUMyhRJIqKTVaVderZ4mGub4-GA6pNpyb20XU3dUuv4Uliv_tgnPDKXGAdHmSqVHOaQNrngv1CsbcazAetBBMSsjPdhup_Odz0iVkZoUQe2TOXgMtIe6wAcTxX6_OmTgldpa6EeLIP7y0ZvzQDlW5YiVql4B5RJO-r1De5X7g8E0vLgxOX7OuZAJ2NuSAataLAAPZ9m-pIsN5e0godvgcA0cFpigUiBKWQOjooR6Aoerj1quum8G5q6Pe4Zx_x2bV67AWo59e6Saxv4hs5dDmHKRCAf5jj9QOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اگه تحمل شنیدن حقیقت‌های تلخ رو نداری، اینو اصلاً تست نکن!
❌
همیشه به این چارت تولد و ستاره‌شناسی می‌خندیدم، تا اینکه خودم امتحان کردم و لال شدم...
😶
دقیقاً همون مشکل‌هایی که تو
کار
و
رابطه‌هام
داشتم رو مو به مو آورد جلو چشمم!
انگار یه نفر از بچگی داشته منو آنالیز می‌کرده و می‌دونسته کجای کارم می‌لنگه.
👀
اگه می‌خوای بفهمی:
✔️
کدهای پنهان شخصیتیت چیه
✔️
مسیر اصلی موفقیتت کجاست
⚠️
این آنالیزگر روانی رو از دست نده.
⬇️
فقط یه بار تستش کن تا بفهمی چی میگم
⬇️</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/130990" target="_blank">📅 01:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130989">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=rXwpycFR1JVUq37WKv3ipVY0rESnO6eO9a0BrBLtgpb8mPvyFF0lfdyXEkfr04FtdjJQz_I298V02ZEHQh4w_BsmPrpYKVLsIsyKtEghRq10EDgfGmLIVwLyoiyidmM8YN_9MTvJwOl6MNVIzemvhamPMmzoPDNBprFMgg5oQU3rasbDGP-yAu8hVMJM1kgIRGz7CRMts_r96teHfwzAFP_a0q8JXrI4xh8HWgbnIzSk45Y8n4KHxlMxFGy7jFY04bSJ-9FydxW3BJ-UGX0UO-9Vm-8LSIrQ9GNizP4ECmRjChf-BRd8UQg6a1bBYiTWt3L3qLK8Tbk80GRFWPQnvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=rXwpycFR1JVUq37WKv3ipVY0rESnO6eO9a0BrBLtgpb8mPvyFF0lfdyXEkfr04FtdjJQz_I298V02ZEHQh4w_BsmPrpYKVLsIsyKtEghRq10EDgfGmLIVwLyoiyidmM8YN_9MTvJwOl6MNVIzemvhamPMmzoPDNBprFMgg5oQU3rasbDGP-yAu8hVMJM1kgIRGz7CRMts_r96teHfwzAFP_a0q8JXrI4xh8HWgbnIzSk45Y8n4KHxlMxFGy7jFY04bSJ-9FydxW3BJ-UGX0UO-9Vm-8LSIrQ9GNizP4ECmRjChf-BRd8UQg6a1bBYiTWt3L3qLK8Tbk80GRFWPQnvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مداحک:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید
🔴
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/130989" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130988">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
شمار قربانیان دو زمین‌لرزه ونزوئلا به ۱۷۱۹ کشته و ۵۰۳۴ مصدوم افزایش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/130988" target="_blank">📅 01:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130987">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndy6RAiOKaMhzGOVLPxEdNcylou2cvKplIyMavqt_dxf0GRUWbmK5s5mnXX6iiRug3C700reMXYBjaMWrCDQvnkxCpkoeIUAixZ5DvxthFVjplgHGZ4PATyYj7GoOFahTqzlaTTE9OCEUz9q-cQSIIMIiYuuGmpZbXV7tL3bVVRwHGAXVLj8uApJ2EjO9p3SibMNEZLU2xOnxDyxF912b-hbg4ZHqJiy5FAwQ_4FSyM4uz8JtABjpMsKXgfbhBF8-MS0TxzDlZmeFlXf6N1l7VmW-UWPC6essaUb0nV91QV8rOIW1mV94sEkUFIgie5pBHiL11iE02oQshSZoTGgLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه اهواز(مِگامَن):امتحان نهایی هارو به تعویق بندازید تا بچها از امتحان الهی یعنی اربعین مردود نشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/130987" target="_blank">📅 01:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130986">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDHfTv2imygSrp40neFTPGJXRiisCxxEzIsgil1tSXijMzTxlGOI3eYCr88RheUoJgJK792wXlm4epNg7RarFlRuWPXnMyuVb13jch1YKzNd43mXHJITfsRxHySqTWsxaTglN_g87l_tPSHhpQThbz1Wj3Ta8kahKzq6pk3fLxtVKIJLNX4gRReEw2_o7QTzVj5AzdSbiWmIqADHgwYuK88uLqrzqZI8fQnZQrz_XQbjvuw1G8GzLiA09dnWNWi26sc_qs0QPhmJTnyT3P-zt7cJrYadcIZCup0m-bsBvDd7EpyXBCm5a14ATG4breOM3Ol1ZUSjy5gmrICfNW-W1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در شهر موناکو فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/130986" target="_blank">📅 00:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130985">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ48TBNqtPo3bEUja5fXnwhRjono4JJJmCi8XjtE4MpIiwdQr4CYoiUXKA_yTyBCj2_S_HHUEQALnT-vSBSHwTrqrQwZX73TQSXE04YY1TFR_iSwB-xH4ZHL0P38st2xkmu633CJ_Q5xJ2-y84de9BHIWOscOO7PtlT3Ft_YfQdGllwIYShFDz3wk7d_JiOxgqwUs4BTPc8ZAsI9pk82wsYz5CurYV8oVyX3lUxV9SVUbKqbfFyPw9io-NiWIDUWxDYdnhyZpohe4cCScVLM0EqQnAQ3SCkgF4-rDvFRj7qJOqGfWLiXjhTyd_cCigbizq-FPLJlyYVRwn3R44yVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امسال تعزیه‌های محرّم چرا اینجوری شده؟
🔴
داستان عوض شده یا فصل جدید کربلاست؟
🤔
آخرین باری که اینو آتیش زدن خودشون پوکیدن</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130985" target="_blank">📅 00:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130982">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQJWR6RIWKuDJKTdQOjmCXvLJNlTM8o86yoTVJZAncLbMQOzDa4Eg9z7jvSuJhmfBEs87HHx5cpZI4XNU9ARpHfpEy40uocpIm4qJb1V7fTV1YhSwma6u21Bj9QiTpaTYFgbottWOtfCfncWbnFfzjiprXPXfDyj9u4P9q_Aon_TFGlc89jlaNRTuaCPz9JyWR7iRX2RBgdnHySoDben7AySnnxCy1MgQFAVrRA_eD9qrPMlk8hHm1aAnwFQEKvj4R4T7VuxaktDonYbTn50KP9DFRgvJURyQPlZRHoyeuQaa0PXr9EJwdCPOUjoHom8aOj1Rcvdsz4Eg6uaxsSFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LI3LaR9gSF_X4ZExFOru6gxzqxkUteJCUzZXA_Wiqzn_wCHDosBvrvSW3Sfmrh-P5-t8lsiDujJaDxDBcTUeYXJw7h2ulfrGLZ_tKq6gzKD4UYSQJPP-B0aEJoQLjEKfsO9I73jAaEifT4FmyCbFRRkTfiAGHOtleE6MkvEB4kZN-1Oj9Y0jUwyGiT4juqrQxOgrvzsUJRjTBrnqJcs07975P_fyQw6axTUatUFV--5U9yrXsxjAUTyKOStUMfLZzRrq6x5HxKXgR52lja7GYLYsHeISRkV_6WJ0hzHOeO8xUoXMxEOP3czjOCxmbxMwLWiJ2s-L8DyRahuJri6lyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سرویس امنیتی عراق از منزل این‌نماینده شیعه پارلمان عراق که طرفدار مقاومت و جمهوری اسلامی بود، 20کیلو طلا و چندین‌ میلیون دلار پول نقد کشف کرد
🔴
در روزهای اخیر از منزل صدها مسئول طرفدار جبهه مقاومت میلیون‌ها دلار پول نقد و صدها کیلو طلا کشف شده
#مرگ_بر_آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/130982" target="_blank">📅 00:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSFyQwOuAGxwJgZg9FMTW2O_Gqbf-vevi1G0taCLZNCsQOmbdcmiCK7U0QU_kGaUfQProXL6koKdczuK2Kd9xOWST-_cLfm-Nn77rTivz5DSfF7tvO_R_z5mmillNgZLtQXFU4z2WrihmHF2UGKCjgB6QZg6j3O5oMNk6YjlThxstxJXcbNt-QXzq5v4SWFRXuGb6-IxK66MFG57PJBKAXa_CzuhbDYt2JWP3mp-R_03ZV2x1HybsLfo-M7XjNFS0Bf-G5gGNZ1MN3nszvPSIT3BhqQll_Ku0d4c9knQhHq_OGxrj7-SkjewHEjAwCEg01B5VtCcadzpoRTHZu32_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط یادی کنیم از شغل جناب حدادعادل قبل انقلاب که در دفتر فرح پهلوی کار میکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/130981" target="_blank">📅 00:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❤️
حداد عادل: محمدرضا شاه هم مثل پدرش عوضی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/130980" target="_blank">📅 00:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngG9tRf_7bUJ4QwFHp4htz3fxEZrvbVqy45K_7djZcv5iXCjFr8pWc_IHNWoWNCfZ2fQ71gEfIrnfjuXkOc0I4xAaoSBlXc_VL6DecpCLxE8JWgazAleYwh1SCFUsmBYzNLqKVjh2lhqNgVlfst5WchUhVw2CCEaFxhC02RMtDnYl5vt-kFnmfV7VjDILc44a7D8uNQq6snL9uwZCL0ZRqX2YCN0cNYLM7YQ0n19PC8zp3_zajCMR4Zimiqdtfi5qSNOyXjS3NHwIcEojXRTs6V8Le3YSzTum3WCI-U2MJsqxVYayf7wXTHqqyMzib9J4M35CqXdml2tKTh2FiI0kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
محمدرضا شاه هم مثل پدرش عوضی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/130979" target="_blank">📅 00:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwGWXSQk6jHt8MZwrotXMnX1GvmYXdg-qG1TvHOLxoxZLbVr4alNskSlkdHAVbl3has66FrBlqynRTLJlRy_ZDYhSJHH2EnSPGm2yvk6r5DdrDoNXO7UPWcEmsfIUELySgFycb-zE4WfjOT0jQBXY_pCYek4cnfB1jQKSejbdLGohktFJsmvUmm_zLwxzbJDDBJy0xxMSVueNt9er7xlsPMztuACOBBnYLwfW2pnyhkiw6F6ujkowrNL9C-RpdEY26R_BA3osC5YnlY5hxPF2JuNQadxeWQs5NFv-MXe6yRoZIFeuoROE7JHlei1UwzSOKOLVu2zBgRP5Lyn56Antg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه ایالات متحده، با سدام حفتر، معاون فرمانده ارتش ملی لیبی دیدار کرد تا درباره تلاش‌ها برای یکپارچه‌سازی نظامی لیبی و پیشبرد شرایط برای صلح پایدار گفتگو کنند.
🔴
ایالات متحده اعلام کرد که به همکاری با رهبران لیبی و شرکای بین‌المللی برای حمایت از لیبی‌ای صلح‌آمیزتر، متحدتر و شکوفاتر ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/130978" target="_blank">📅 00:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شبکه خبری فرانس ۲۴: ایران روز دوشنبه اعلام کرد که نخستین دیدار خود را با عمان درباره مدیریت تنگه هرمز از زمان امضای تفاهم نامه برای پایان دادن به جنگ با آمریکا برگزار کرده است.
🔴
آمریکا در تلاش است قوانین قدیمی عبور و مرور در تنگه هرمز را برقرار کند، در حالی که ایران به وضوح اعلام کرده که قوانین جدیدی در کار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/130977" target="_blank">📅 23:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری/وزیر دفاع اسرائیل: آغاز جنگ مجدد با ایران ممکن است در عرض 2 روز آینده و با شلیک موشک از ایران به سمت ما رخ دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/130976" target="_blank">📅 23:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130975">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
روایت الشرق نیوز از متن کامل پیوست امنیتی توافق لبنان و اسرائیل: ارتش لبنان متعهد می‌شود اقدامات عملیاتی لازم را برای خلع سلاح حزب‌الله و تمام گروه‌های مسلح غیردولتی انجام دهد
🔴
تأیید پاکسازی از سوی یک نهاد ثالث مورد توافق طرفین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/130975" target="_blank">📅 23:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خبرنگار نیوزنیشن در ایکس نوشت: یک دیپلمات آگاه از مذاکرات به من می‌گوید که فردا (سه‌شنبه)، استیو ویتکاف و جرد کوشنر، در دوحه با نخست‌وزیر قطر و دیگر مقامات دیدار خواهند کرد تا در مورد مذاکرات با ایران گفت‌وگو کنند
🔴
وی در این باره افزود: روز بعد (چهارشنبه)، تیم‌های فنی از ایالات متحده و ایران به‌طور جداگانه با میانجیگران قطری و پاکستانی دیدار خواهند کرد.
🔴
پیش از این کاخ سفید مدعی شده بود که مذاکرات ایران و آمریکا این هفته در سطح بالا در قطر برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/130974" target="_blank">📅 23:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130973">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
موافقت عمان با اخذ هزینه خدمات دریایی
🔴
وزیرخارجه عمان تفاوت میان عوارض عبور و خدمات دریایی، زیست‌محیطی و مالی را توضیح داد که می‌توانند به‌طور داوطلبانه با کشورها و شرکت‌های ذی‌نفع مورد بحث قرار گیرند.
🔴
او افزود که برخی خدمات ممکن است شامل افزایش ایمنی ناوبری، حفاظت از آب‌ها در برابر آلودگی و ارتقای آمادگی برای مقابله با حوادث یا شرایط اضطراری باشد.
🔴
وی به امکان بهره‌گیری از الگوهای موجود مانند تنگهٔ مالاکا و سنگاپور اشاره کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/130973" target="_blank">📅 23:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130972">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ: ما تا حد زیادی با عقل سلیم حکومت می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/130972" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130971">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d045164058.mp4?token=aAUPs5hb9NTH-F_BI5B7Yp48QddbGT7wr_bCLGbpuuuzXD1mt-7125g15YmhfkUnDppYUBXhQGXi0ppLz3YKPhYjMwVIGRDn5bwJDhXWYhF3yCa44dDoebikKmt-36SwkOUZ4O4EBPWokIzpgjmnvIRWIElTTudBYytQ21nG9KWlAW3wLyCiO5YCvOgSeQum2IL7vVgySmS-Rb_xopUWLpWTjTsh-ln4mpOns9XqwX9e1z4xAbyoent8gf0RVjloVnwmcGH-YxlrfbPMe1Hvibd3dgmdCXDBXDc6CKlVI6j72W8lApt3SIysox9xPGtLjFwGU5jjOVCG8ajU_47RmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d045164058.mp4?token=aAUPs5hb9NTH-F_BI5B7Yp48QddbGT7wr_bCLGbpuuuzXD1mt-7125g15YmhfkUnDppYUBXhQGXi0ppLz3YKPhYjMwVIGRDn5bwJDhXWYhF3yCa44dDoebikKmt-36SwkOUZ4O4EBPWokIzpgjmnvIRWIElTTudBYytQ21nG9KWlAW3wLyCiO5YCvOgSeQum2IL7vVgySmS-Rb_xopUWLpWTjTsh-ln4mpOns9XqwX9e1z4xAbyoent8gf0RVjloVnwmcGH-YxlrfbPMe1Hvibd3dgmdCXDBXDc6CKlVI6j72W8lApt3SIysox9xPGtLjFwGU5jjOVCG8ajU_47RmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من قیمت داروها را ۲۰۰–۳۰۰–۴۰۰٪ کاهش می‌دهم. هیچ‌کس حتی درباره‌اش صحبت نمی‌کند.
🔴
دموکرات‌ها با این مخالفند. اگر آن‌ها به قدرت برسند، قیمت داروها ۳۰۰–۴۰۰–۵۰۰٪ افزایش خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/130971" target="_blank">📅 23:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130970">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8fc62c34.mp4?token=gPmI-2KWUjb0fGMIZ_ppeF_Zu9Eb29TBZZAUf0s5301mk45dH3Lmrx6QqXUzjZzUSToMiczbGDX2u5CzMWGS6vk55C4AvxPKqR25lG02JFdQ8y0gst88aNxl2mXPiCwwjUhStPkyug8x80oCUB3HnV8t7XgHGv7wvVdd9zCRiTEi6Kw9DpQfnBhgq9v8qZnxJwD-R6ejoxeCX32z4Dq_NTJlEgpTfSRJXLSUYWYYnf2k1RbIlDSglv3xal_lPg7xmiVWPeL63eM4p51kEldloGAZcTXHt7UmEToAsLt7brTCmphLERr2SDLoI1U1fQ7-1QM-2NOeSGXXiXuagu6ZpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8fc62c34.mp4?token=gPmI-2KWUjb0fGMIZ_ppeF_Zu9Eb29TBZZAUf0s5301mk45dH3Lmrx6QqXUzjZzUSToMiczbGDX2u5CzMWGS6vk55C4AvxPKqR25lG02JFdQ8y0gst88aNxl2mXPiCwwjUhStPkyug8x80oCUB3HnV8t7XgHGv7wvVdd9zCRiTEi6Kw9DpQfnBhgq9v8qZnxJwD-R6ejoxeCX32z4Dq_NTJlEgpTfSRJXLSUYWYYnf2k1RbIlDSglv3xal_lPg7xmiVWPeL63eM4p51kEldloGAZcTXHt7UmEToAsLt7brTCmphLERr2SDLoI1U1fQ7-1QM-2NOeSGXXiXuagu6ZpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در میدان نظامی پیروزیم. می‌توانم بگویم تقریباً در میدان نظامی پیروز شده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/130970" target="_blank">📅 23:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130969">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262fb7eb01.mp4?token=WGAaIYw2BZ9FjJe1tWvIj14uDHL00vJ_maqrrqub8OqUdgqMrwJzJoHXjwPAaiwfbYe6M9u1raVZya9W_m523n3F6I1zSjpol9FK5DTtbzaKWuj9m4wWDmUmMl_qD1UzKa5DcJqdGCLLzYrh4y_mF8-ZBNALt80LFKz5uPidUNwame9blpaMap3B5MRCmBpWSi8Am-y4NuBF3swrWgYMXxnrjqp6GoFSNH-7b9cCAWIEcIjRj06GqkT3FRgKNx7QPWNnnXrF8vak6I7-mVA4a2-_Z2YMlllH10TWOYevhA9SRnra6OIRSWvvkt6BTDAnjo3YbATvgKzxUUtJ9iNryG31bMu1zzku9Ei2BgpEzCPxfBCJwQkLVH6bGst5hOeWUwMYH6GpRYBF9gRN7kQSLCuuDm-lejQ_YZyhXVb86APYd16YO2FTxntn5_NieyO3FUoaEN_ZfddAxPA1j-cxCzpZt2-hF_SsV_yBpVPGESWwBkrt-_NnSUO3sa9xWWPWBdl7zRLAIcotiVQxaIqCGqq-JdGZqHMKr_QB_AHqGej2Pkkt8r4_kc2pMV-vkAQeeNs1Mk47RWW8Ctlw8jp6QIu6gTYOauJSPVw_tCwb3hdLv-bqR1g2hw4D6y7l95hJYMgaHggizVuPX_yrTmRID72XE5SenLo2KdpimFkx5nk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262fb7eb01.mp4?token=WGAaIYw2BZ9FjJe1tWvIj14uDHL00vJ_maqrrqub8OqUdgqMrwJzJoHXjwPAaiwfbYe6M9u1raVZya9W_m523n3F6I1zSjpol9FK5DTtbzaKWuj9m4wWDmUmMl_qD1UzKa5DcJqdGCLLzYrh4y_mF8-ZBNALt80LFKz5uPidUNwame9blpaMap3B5MRCmBpWSi8Am-y4NuBF3swrWgYMXxnrjqp6GoFSNH-7b9cCAWIEcIjRj06GqkT3FRgKNx7QPWNnnXrF8vak6I7-mVA4a2-_Z2YMlllH10TWOYevhA9SRnra6OIRSWvvkt6BTDAnjo3YbATvgKzxUUtJ9iNryG31bMu1zzku9Ei2BgpEzCPxfBCJwQkLVH6bGst5hOeWUwMYH6GpRYBF9gRN7kQSLCuuDm-lejQ_YZyhXVb86APYd16YO2FTxntn5_NieyO3FUoaEN_ZfddAxPA1j-cxCzpZt2-hF_SsV_yBpVPGESWwBkrt-_NnSUO3sa9xWWPWBdl7zRLAIcotiVQxaIqCGqq-JdGZqHMKr_QB_AHqGej2Pkkt8r4_kc2pMV-vkAQeeNs1Mk47RWW8Ctlw8jp6QIu6gTYOauJSPVw_tCwb3hdLv-bqR1g2hw4D6y7l95hJYMgaHggizVuPX_yrTmRID72XE5SenLo2KdpimFkx5nk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کمونیسم: این سوسیالیسم نیست؛ واقعاً کمونیسم است. آنها از عبارت «دموکرات اجتماعی» استفاده می‌کنند چون زیبا به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
🔴
فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ما است، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، یازده سپتامبر و حمله پرل هاربر می‌شود.
🔴
فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ما است. مردم وقتی این را می‌گویم لبخند می‌زنند، اما افراد باهوش خواهند گفت: «می‌دانی، احتمالاً حق با اوست.»
🔴
در واقع این معرفی کمونیسم به ایالات متحده آمریکا است. هرگز چیزی به این خطرناکی نبوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/130969" target="_blank">📅 23:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130968">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/681f6a849a.mp4?token=b-kYqIKw3ND0ZsKffHhWSZNXKCIfD0QBOJf2G9jtXQvthSLermQrGF5_K80XRWmniJw_dhl_U0Pe0h5WLhxZJau5igiIYAmbu0dIF6Lsa3qrHV7ptN3XlbdD0s7RjXEvU_c9-FUpQ-DFENJY-QpZt0qNjIOqKLsoEL1XIX1kxC9Psg_IZOv7PUQtQ4krNxj5GEwcxgpItdDMHp6nUqBd9tNdRQY6B6GVUyaR1x9oPzci4NDAyR9PWzFlp9X206APmZtftvJB31eVDwlWGbbRRSFnTBmVjFQ0ieqD9xhdc6qi-SiS3t02aezWiztfCrFDKuSXy_KcVUJC44ZeB1d5Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/681f6a849a.mp4?token=b-kYqIKw3ND0ZsKffHhWSZNXKCIfD0QBOJf2G9jtXQvthSLermQrGF5_K80XRWmniJw_dhl_U0Pe0h5WLhxZJau5igiIYAmbu0dIF6Lsa3qrHV7ptN3XlbdD0s7RjXEvU_c9-FUpQ-DFENJY-QpZt0qNjIOqKLsoEL1XIX1kxC9Psg_IZOv7PUQtQ4krNxj5GEwcxgpItdDMHp6nUqBd9tNdRQY6B6GVUyaR1x9oPzci4NDAyR9PWzFlp9X206APmZtftvJB31eVDwlWGbbRRSFnTBmVjFQ0ieqD9xhdc6qi-SiS3t02aezWiztfCrFDKuSXy_KcVUJC44ZeB1d5Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آنها مردم را به خاطر تعمیر ماشینشان دستگیر می‌کردند.
🔴
این حتی باورکردنی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/130968" target="_blank">📅 23:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130967">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ : قیمت نفت خیلی کاهش پیدا کرده، ببینید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/130967" target="_blank">📅 23:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130966">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca333bc10.mp4?token=O-nTjJzJhNN42-4x11fTcQBHpBf161wvOxLvMfIRjUAJ3iIQcZBpHV5yC8ptQ5n5oVsi6DNurJQmo9Rq3goV1Jv0gMqM498B2r4bdcVz8lCgnIeXmo0rl2B3S6EP0dtsZmv3PDfylakbCHwKZA7Lnh_6yLTvnx7g3AccYZzyyMft9C7RJucsHjEYiZ60i3_LSAXES8RgTt8vjC7JFvd7ngaLfxIsHtNAQ2bBM_LUKNf9f37GEhdYN0ZiscHlfmJuNZsF_6y1rZyghyNxDx-r4webRR-_Hgt2gZiF35sxVBB4zSOiA5iLhxCd3bHPLvFcHXlllo3Y9ctbWynLvydA8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca333bc10.mp4?token=O-nTjJzJhNN42-4x11fTcQBHpBf161wvOxLvMfIRjUAJ3iIQcZBpHV5yC8ptQ5n5oVsi6DNurJQmo9Rq3goV1Jv0gMqM498B2r4bdcVz8lCgnIeXmo0rl2B3S6EP0dtsZmv3PDfylakbCHwKZA7Lnh_6yLTvnx7g3AccYZzyyMft9C7RJucsHjEYiZ60i3_LSAXES8RgTt8vjC7JFvd7ngaLfxIsHtNAQ2bBM_LUKNf9f37GEhdYN0ZiscHlfmJuNZsF_6y1rZyghyNxDx-r4webRR-_Hgt2gZiF35sxVBB4zSOiA5iLhxCd3bHPLvFcHXlllo3Y9ctbWynLvydA8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: نشست دوحه برگزار خواهد شد؛ شاید مهم باشد، شاید هم نباشد
🔴
خواهیم فهمید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/130966" target="_blank">📅 23:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130965">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
گزارش ها از آغاز دور جدید حملات هوایی در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130965" target="_blank">📅 22:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130964">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7ybxJMdgmA6iB0ZOVNw6VD8jhDyc7AHrO5-rzzJx25Ym9AvRyta3ygIXCPZYWH9-XojnxW5lON7NXlVFcM-2VaNLynDjxJuEgbxBT5yoI-w2LUnoTQ4fa3mnPtJrNZgK7O-naOVRWL9B0Ukk0hpifbHWkrgIrsKPN1MiRaGFTQ-xG0jofaFeEl9x2V88rnxpn74MkC6Ckmcl3dEGt-IdzhLTQIFmGBp5mQ2sHPBYTzqbZd0ZQxRq0O2V9n3Tw6wcvVbvgMd_UOHOhm73n4hMkv1gucE7ZInj3SVfRFaZer5QmEJRT5AM7Y8xQvumgGir3q-fUu4fq9yoysAUvt_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاضل میبدی : جنگ‌طلبان اگر عاشق شهادتند، راهی بیروت یا غزه شوند/ رفراندوم بگذارید تا ببینید مردم چه می خواهند، مذاکره و صلح یا شعار مرگ و جنگ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130964" target="_blank">📅 22:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130963">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8EQKejbyEgz38ZIl0AdPBA_iGe-C9IRYTNWncsc9Xybrh93vaEzdw9E_hdPDqyGrBl-3BL9nbucCmCHQ40rhwIRvbGa4xw16lL7ZfdyppGD_Q2X4VjSNlswvCOGpriaXuJe3birSPwV_03aYC1VD_XcQX9itV-QRUOPdUqnM0FbhJmOZuw0p6OeSeZvUmXU6r-5Z5laFBEmMZzMJPwt7F_pS9o_xE6aBLdK4Gx1qHrIT3fHG2PSy8JEazwlTPUKJHj1LqM6grgDdNLBEM7PrzpO7VREUStTwvgR1Lscni7BPOR_ut6ko3N413gtVtUxbWZXpGLedi_P0fHVzCfQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ادعای اینکه من با تهدید به استعفا موجب تغییر تصمیمات نهادهای عالی کشور شده باشم، صحت ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/130963" target="_blank">📅 22:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130962">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAWdy0sia1DrDchASvlIuXNay6SprrrgAleTgmFTshkujqKEPxH9sFOVScqMmksBLiZ-2Pn9vBkvl8lyzBNSfaYILaLKrHLIDibCDOjWptXa6uTiR7P99zLKVakugsv_3rshCa0J4ircngxkVc0B7KSPdfWn4YYpAu8LkFU-amjxnTkVW6hXK9HNv2snSQ-WhcvmsNPdHhUm3AHqTLfTsmgN36tjtLUpoh03q4IqXSrGLZeXoX6zQBUWhhidoNdjT9-NhqT97EZG0UNEKsxOK7t2NbTqef6hVntDhH2yTV5ZIX1q4TP5VbazOuhMfzKXHbK5Fc0HyUn_LZk9gdBROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
رضا شاه یه آدم بی دین، فاسد، عوضی بود و وقتی مرد کل ایران خوشحال شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/130962" target="_blank">📅 22:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130961">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">➕
حتما یک بار تست کنید تا سرعت و کیفیت رو متوجه بشید
✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
خرید فوری از ربات های زیر :
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/130961" target="_blank">📅 22:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130960">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
سرویس Vpn(v2ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/130960" target="_blank">📅 22:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130959">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
جیک سالیوان، مشاور سابق امنیت ملی آمریکا: کشورهای منطقه دنبال توافق اختصاصی با ایران بر سر تنگهٔ هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/130959" target="_blank">📅 22:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130958">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزارت امور خارجه ایران اعلام کرد: ما خواستار دریافت هزینه خدمات در تنگه هرمز هستیم و این موضوع را با سلطنت عمان مورد بحث و گفت‌وگو قرار داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/130958" target="_blank">📅 22:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130957">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
حجت میرزایی، اقتصاددان: نمی‌گویم ۲۰ سال اما حداقل ۱۰ سال زمان می‌برد تا پس از لغو تحریم‌ها به دوره اقتصادی سیدمحمد خاتمی برگردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/130957" target="_blank">📅 22:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130956">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=h9bOwFF06NYoOsbSDoAcAnzGnWoHVjuImwMeKBGmJg1yFAjEaECtaLQJ2ahXVsmIevhOOyWsZ9DEIUAPuhfWg1fW6THL-6MZ-_sFlLbWbE72q5oZIau2e3XTFZLYlnYMoWTvKU7OwxefT8HMbimPIDajnWV30ED3pbt7D7qq7XbNCrwquiQ_RZzLaT0_8CbRwdmjcbr1EBca5DXZ_tAT59hmTvlrRa_Kao-7tF274j1JR5zczztFb4whPFp81rCqC7WOplXdcHQeBtFnpUQkyYogeFs9THylnK3cMsTzq9V3_69yYRlF6WQ74ehT_N8BfbngIIxsG_yDcDpi6PhX8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=h9bOwFF06NYoOsbSDoAcAnzGnWoHVjuImwMeKBGmJg1yFAjEaECtaLQJ2ahXVsmIevhOOyWsZ9DEIUAPuhfWg1fW6THL-6MZ-_sFlLbWbE72q5oZIau2e3XTFZLYlnYMoWTvKU7OwxefT8HMbimPIDajnWV30ED3pbt7D7qq7XbNCrwquiQ_RZzLaT0_8CbRwdmjcbr1EBca5DXZ_tAT59hmTvlrRa_Kao-7tF274j1JR5zczztFb4whPFp81rCqC7WOplXdcHQeBtFnpUQkyYogeFs9THylnK3cMsTzq9V3_69yYRlF6WQ74ehT_N8BfbngIIxsG_yDcDpi6PhX8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس تلویزیون: جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/130956" target="_blank">📅 21:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130955">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
آنتونیو گوترش، دبیرکل سازمان ملل متحد: تروریسم در حال تحول است — فناوری‌های نوظهور از جمله هوش مصنوعی، پلتفرم‌های دیجیتال و سلاح‌های بدون سرنشین را مورد سوءاستفاده قرار می‌دهد. هیچ کشوری نمی‌تواند به تنهایی به آن پاسخ دهد.
🔴
ما باید پیشگیری، همکاری و تعهد خود به حقوق بشر را تقویت کنیم تا جهانی امن‌تر بسازیم که در آن مردم بدون ترس زندگی کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130955" target="_blank">📅 21:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130954">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjGqpeSBcUv30ea0ddMSioScTpLix7Kmu1pSgq1HzZMp13tlC6ebaM0SZplFu-ZUM0sgSZkz7vkwQ36iokGa6yU5R68cd4Jl5VEKZz6btto6VnVk3nb2sHz4e-ZQZluigzUWtOhYlPd5n7Ttf1_uZtN-c1ncToU9iwsAwkpbpNEl6T6--cZ5vraOMFhzPTHERb_Pt__fkxFNTLdRfZSt3vig2Krf3_yF7KkNodZ0xRr2Doq_E5m4pwlwqeVQhvwTRFzFbaiEp_WSX-w3NHQbeqqKmrnZzSiLfXKc0aIr09tjwPZcSxbcQuKVl90ko3j1IYo6k477rLRE9tKaAmvGaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: آمریکا اگه توافق میخواد باید ترامپ رو تحویل ما بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/130954" target="_blank">📅 21:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130953">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9395da4b1a.mp4?token=r8yzPsJbVYzdSYvbaoLnO3v64m41y3lGOvjM97-8eQW9-nnatsPa7ox7_auCOt3V8HQf_jGw2zgazMyBwZFv-dEnh1QEVTx5fF1HMkypQz5q2F7G2viwAHKcsY-mdY3zA3nvi6ewiPtH37ylVcMLZwHpx9mxeeOF8ESA-iQNinBbg79iE-gkGc9A-Mj-M5PogghCCRm-3Uw8e1pz8vIIFW49yqJPpfXQUwEh8MpBsBlImoAZv1CWDCSP3_u33ZOIilo3JP6sQPQkZ2ISvAOG8x-BPGURAabqAhwDhOW4OvOUTzYPLmZGvKtUFnVeIREB5frEdFPZdk9jVjQ7OO3rDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9395da4b1a.mp4?token=r8yzPsJbVYzdSYvbaoLnO3v64m41y3lGOvjM97-8eQW9-nnatsPa7ox7_auCOt3V8HQf_jGw2zgazMyBwZFv-dEnh1QEVTx5fF1HMkypQz5q2F7G2viwAHKcsY-mdY3zA3nvi6ewiPtH37ylVcMLZwHpx9mxeeOF8ESA-iQNinBbg79iE-gkGc9A-Mj-M5PogghCCRm-3Uw8e1pz8vIIFW49yqJPpfXQUwEh8MpBsBlImoAZv1CWDCSP3_u33ZOIilo3JP6sQPQkZ2ISvAOG8x-BPGURAabqAhwDhOW4OvOUTzYPLmZGvKtUFnVeIREB5frEdFPZdk9jVjQ7OO3rDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیا مذاکرات هسته‌ای با آمریکا آغاز شده؟!
آجورلو، عضو رسانه‌ای تیم مذاکره‌کننده:
تا الان هیچ مذاکرۀ هسته‌ای با آمریکا انجام نشده و تا عملی‌شدن شروط ایران هم مذاکره‌ای دربارۀ موضوعات هسته‌ای انجام نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/130953" target="_blank">📅 21:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130951">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خبرگزاری معتبر فارس:
محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه،
در یک سانحه رانندگی ساعاتی پیش درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130951" target="_blank">📅 21:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130950">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/130950" target="_blank">📅 21:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130949">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: هنوز وارد مرحلۀ مذاکره برای توافق نهایی نشده‌ایم
🔴
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آن‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/130949" target="_blank">📅 20:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130948">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=NFxzZFgARXStIHcb5SXBIPVgNNehQ0DWA2JueSJqqXlUI8N4osKHdnru8llNYvMVXytroMI7gkE_aAao-iKv29sclo-kp8ziGe4ihUDLXDFb6NTl2jbhj6HLjg94c6C8t841u6JkJC0H8VSAR-wLgt0cJYWuVdcWWPBrfmfCWq8y5p-wVeT1TcMmc_blLgfSRFtB4JLClG1veMxlWV0ljFnnNv1H39reIaahrUfra5GFIDgQeLphuNqij6BPr0_wcATZRerQJj7lQcMXTP9S8mnWzOMsel99GvTMTkyCLY09-njjqJw7wV_zDpBzhgpAq5Bxi2VmuXZE1lMJ1-MNOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=NFxzZFgARXStIHcb5SXBIPVgNNehQ0DWA2JueSJqqXlUI8N4osKHdnru8llNYvMVXytroMI7gkE_aAao-iKv29sclo-kp8ziGe4ihUDLXDFb6NTl2jbhj6HLjg94c6C8t841u6JkJC0H8VSAR-wLgt0cJYWuVdcWWPBrfmfCWq8y5p-wVeT1TcMmc_blLgfSRFtB4JLClG1veMxlWV0ljFnnNv1H39reIaahrUfra5GFIDgQeLphuNqij6BPr0_wcATZRerQJj7lQcMXTP9S8mnWzOMsel99GvTMTkyCLY09-njjqJw7wV_zDpBzhgpAq5Bxi2VmuXZE1lMJ1-MNOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات حق استاد محمود سریع‌القلم، مشاور سابق روحانی:دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.
🔴
مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.
🔴
اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/130948" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130947">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJTVeSfDzEIThxlBMJ1V_u78JeI8VzJojRubYo6PFX_7-KokiDRf1SOdXU1OtEbACqPGpQKwYPpQb4bXFQXkDOKsezNJaY8UjGK4xGbWtlOdIFnoxqqa0MXu5NIRA2kssbKCZci0rHtqL1V0lJ7ol9DJJDUyLFpAG4uNuu3tGirWtzGr1M-ikf1OxPEcJCsgRkl1R3_R2curc6aXqim-p9CvlNwV94nXoH7dJp_3yWpEpXNxVBvO_jn7snKoRNdcXWVrdUE9ekHueA0DO3QVV9r7nzfyClWWLGNWY6AUKog_kaBaC0PDKwzVX-cbuLH98mTEpT2WZ9WmWxo0UWUs_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ژاپن موشک هایپرسونیک «تایپ ۲۵» را برای حملات دوربرد عملیاتی کرد
🔴
نیروهای دفاع زمینی ژاپن نخستین یگان مجهز به موشک هایپرسونیک «تایپ ۲۵» (HVGP) را عملیاتی کرده‌اند؛ سامانه‌ای که با هدف تقویت توان بازدارندگی و اجرای حملات دوربرد علیه اهداف دریایی و زمینی توسعه یافته است.
🔴
این موشک از فناوری Boost-Glide بهره می‌برد؛ به این معنا که ابتدا توسط یک بوستر راکتی به ارتفاع بالا و سرعت بسیار زیاد می‌رسد، سپس سرجنگی گلایدکننده آن با سرعت هایپرسونیک و در مسیر مانورپذیر به سمت هدف حرکت می‌کند؛ قابلیتی که رهگیری آن را برای سامانه‌های پدافندی دشوارتر می‌کند.
🔴
«تایپ ۲۵» به سامانه هدایت ترکیبی، ناوبری اینرسی و ماهواره‌ای مجهز است و برای هدف قرار دادن شناورهای سطحی و اهداف زمینی با دقت بالا طراحی شده است. ژاپن همچنین در حال توسعه نسخه‌های پیشرفته‌تر این موشک با بردی بین ۲ تا ۳ هزار کیلومتر و سرجنگی ارتقایافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130947" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd900cb7d1.mp4?token=Pooik50Y6iBXae71om9vWk4lpQw0-NRMK-4WplUf0KjCIMlpsKK69lIqMNspzm1AEhSOI598lFoM7g-Vq0VQKWN8hlKc9wMJdC0wc1-0pvYf8sBMne3L8eNMAxRFbmn7jJJ3yJV6tqYpUYxouDrkeXtmeATgz6-gaetr3XpihjWhe-Bk0GHVqWzogJVDlCm-PZA0NHftX8qfJlJ_BoKxOzpgc_x3uIeBFSXXrisx-t6FbiHkPzPe_AYNqcWJDxYwnP40oLNofw8lPxAk6TyX368a7lO34iS6N1nekO027ReWvWOMmJukYdCfYBvBcfM3pqJYbSgpZUS9HDjXqYNGMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd900cb7d1.mp4?token=Pooik50Y6iBXae71om9vWk4lpQw0-NRMK-4WplUf0KjCIMlpsKK69lIqMNspzm1AEhSOI598lFoM7g-Vq0VQKWN8hlKc9wMJdC0wc1-0pvYf8sBMne3L8eNMAxRFbmn7jJJ3yJV6tqYpUYxouDrkeXtmeATgz6-gaetr3XpihjWhe-Bk0GHVqWzogJVDlCm-PZA0NHftX8qfJlJ_BoKxOzpgc_x3uIeBFSXXrisx-t6FbiHkPzPe_AYNqcWJDxYwnP40oLNofw8lPxAk6TyX368a7lO34iS6N1nekO027ReWvWOMmJukYdCfYBvBcfM3pqJYbSgpZUS9HDjXqYNGMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: آزادی گروگان‌ها بدون پذیرش شروط حماس و خروج از غزه ممکن شد. فشار نظامی، فشار دیپلماتیک و حمایت آمریکا عامل این نتیجه بوده و اگر اسرائیل با خواسته‌های حماس موافقت می‌کرد، رهبران این گروه و دیگر گروه‌های هم‌پیمان همچنان در قدرت باقی می‌ماندند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/130946" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130945">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHAYGKAJ_j21jEQuVK9ctxsB92fn5Kt1bQ0OM-9or91y1Dtv92jttf7imuHZe0Xo8lnxlxHTCnuLgW1HPvc3BntajAeplyWX8yKV1C0EXOSaQGwdD8WHpcXyrXIgBfCG3z3Kkh1pUdTsvm_8p7sV92sHNgLgjyTr1LGApwnDKmDGIONNucel4eWwoJTG5xzX-_QUqPHCGHO1rkSXO-TMSF9N8HGgS1HB642-Z6LpaIWfteSIPFqwkJCd_SpRiIEFg2W0VklnmcgOxjb4xR-dRcVbTXAByYEh097neouSqhzAne8p5jcwiSuYGGR3Iw9A9drW4eHKtlhJsfzkRT2NCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری میکند. طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام میشود و نه هیچ کشور دیگری، اصولا اجازه چنین کاری را هم نمیدهیم.
🔴
شرایط حساس و پیچیده است. توصیه اکید میکنیم فرانسه آنرا با تحریکاتش پیچیده تر نکند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/130945" target="_blank">📅 20:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130944">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ایران اعلام کرد که برخلاف ادعاهای مقام‌های آمریکایی، هیچ برنامه‌ای برای برگزاری مذاکرات مستقیم با ایالات متحده در این هفته وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/130944" target="_blank">📅 20:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130943">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سخنگوی دولت عراق اعلام کرد:
دولت به کلیه گروه‌های مسلح در این کشور تا ۳۰ سپتامبر سال جاری،‌ هشتم مهرماه آینده، فرصت داده تا سلاح‌های خود را تحویل دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/130943" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130942">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfaeV9UrP3VhVRllnKkVhinrK2whrCW9CmQd7p7_PB9Et7d5ashwUXYQiPjxKzsSZf4-J_z97K9551SFagtj6391pFy6Y1okgOG4WUPhOqPlQDJ4gJ9EJuyT6SrbdboqAIKCY5umcx_-8-HTCod7Qvxe2JxJakQ-OLkPqlHpABDoHQG93tSlY9OkJFKGrbXQfdiL3BOLeIvnfQoH3mhXfljpwPn_N8ug1sb-wYpbrCh8EAHgq83D3_gV9bw_cEdcVmk7C3_HUL7ieuRLIWXcZatqWg8JP5aSXc3KiRWtCzQfCRfQCLRm1Ah-aZDv4L0gHO41a7XGkz9r7AV6KNLGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوان عالی ایالات متحده روز دوشنبه با صدور حکمی، اخراج روسای نهادهای مستقل توسط «دونالد ترامپ» رئیس‌جمهور آمریکا را آسان‌تر کرد؛ تصمیمی که توازن قدرت را از کنگره به سوی ترامپ تغییر می‌دهد و می‌تواند نحوه فعالیت بیش از دوازده نهاد فدرال را بازتعریف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/130942" target="_blank">📅 20:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130941">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8041c64fe8.mp4?token=tThsbdsGid4qgVcQIyCAxmNPtwLUb-eul-5uI0pv-Lm5OdLRZZ5ryiH5U5idVext9sVkh6MGa-M4iByCH4mGaDm_V8jiLLmOHCjwe1sXLWr4IqQJ-lCnVIhzMVpwvvjDTH8xO8mXLq3onC4B7gsUB5A-zSiER3arbEYoViBInQrchCaTWv2mhGjO_TWt7SrGgt1vv__FQ4w5v9W3WnIc0vjcfGea59FPgd7DLhqVxTcNSLml-NpMzHsFZtQMC9-6ik_d1VuF17FW49dqa2lH5dtAwkpUN5sKuS-GIRN7_4ldpWrK4N60T3jtf3X3HgGzhTIdESayjzU4Fm4OJ1Vrsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8041c64fe8.mp4?token=tThsbdsGid4qgVcQIyCAxmNPtwLUb-eul-5uI0pv-Lm5OdLRZZ5ryiH5U5idVext9sVkh6MGa-M4iByCH4mGaDm_V8jiLLmOHCjwe1sXLWr4IqQJ-lCnVIhzMVpwvvjDTH8xO8mXLq3onC4B7gsUB5A-zSiER3arbEYoViBInQrchCaTWv2mhGjO_TWt7SrGgt1vv__FQ4w5v9W3WnIc0vjcfGea59FPgd7DLhqVxTcNSLml-NpMzHsFZtQMC9-6ik_d1VuF17FW49dqa2lH5dtAwkpUN5sKuS-GIRN7_4ldpWrK4N60T3jtf3X3HgGzhTIdESayjzU4Fm4OJ1Vrsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال مکرون (رئیس جمهوری فرانسه) از سلطان عمان در کاخ الیزه پاریس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/130941" target="_blank">📅 20:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130940">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3dcc1c10.mp4?token=HGBKCRxJ94blGuZ8S-DVDvbnujiWlKrPM8CgkwNPkGEObiumFhmNJukKf6Gb1wwafHAQBajQbS9SzXMIWPM8pP2x-95Z8_sEky_LjvOw_caAVo5COzTQFoL55F3MDIb7IqOcJTyKY0wVZogaGkpYPqEKCXfMjqITLTs5fghOL2aSH65D7YsJp53_qwtXYY_HRPWZf7sZc_7lG57yfbjQoUsam6BH9lPn9rkSq3tzy97UF1IfTq04bLJvC_VZOYrE8GF0mLprF-qmcsT34Y9yC1rCDFROtQUST5_zqEW11bOE2hIBXb_3ZlcJf4aAIhAn_cXo_ECEpH2USmez3wirkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3dcc1c10.mp4?token=HGBKCRxJ94blGuZ8S-DVDvbnujiWlKrPM8CgkwNPkGEObiumFhmNJukKf6Gb1wwafHAQBajQbS9SzXMIWPM8pP2x-95Z8_sEky_LjvOw_caAVo5COzTQFoL55F3MDIb7IqOcJTyKY0wVZogaGkpYPqEKCXfMjqITLTs5fghOL2aSH65D7YsJp53_qwtXYY_HRPWZf7sZc_7lG57yfbjQoUsam6BH9lPn9rkSq3tzy97UF1IfTq04bLJvC_VZOYrE8GF0mLprF-qmcsT34Y9yC1rCDFROtQUST5_zqEW11bOE2hIBXb_3ZlcJf4aAIhAn_cXo_ECEpH2USmez3wirkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پروژه تانک ساخته‌شده توسط دانشجویان طالب دانشکده مهندسی در افغانستان: نصب دوربین مداربسته روی تانک کنترلی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/130940" target="_blank">📅 20:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130939">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نیویورک پست، به نقل از یک مقام آمریکایی: ما به ایران روشن کرده‌ایم که تا زمانی که در موضوع هسته‌ای پیشرفتی حاصل نشود، دارایی‌های مسدود شده‌اش را آزاد نخواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/130939" target="_blank">📅 20:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130938">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: اگر ایران به اسرائیل حمله کند یا ترامپ مذاکرات را بی نتیجه قلمداد کند، جنگ با ایران دوباره شعله ور خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130938" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130937">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
والتز، نماینده آمریکا تو سازمان ملل :
۱۱۵ کشتی که حامل ۲۵۰۰ دریانورد هستن از تنگه هرمز خارج شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/130937" target="_blank">📅 20:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130936">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwekd2bbkMX90EeFw-LP5RmEdaQnSOhqg57Hpf6gmxwxeNs8CdK7K0IaCl0KRwBrzwHGa6cXvzCczwqYVoYmaFCc_ZIScDB1VAbhwioUKK3HZXE4JvH-CeCqT46IU0Gar5W9-yZhBdaz5O5hMVLnmPGz7CTahO0yJU-EPPwlPOUBnTbIpDgcsx02vfb_Gf7Q7IVQipvcdomICHJcnFH0e4GVqS2AwJEZ0RGMmvA1YW-ghIU2934UlH9-ACkP150YP0HFpsqjqrCTOL_5WYsH4s9pWyLXUGYftddu1Sp5AyFMVLwcoTG-9hFx4QERAeXQbiNRQuJt4i-8XtUU0nNeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
دادخواست کوک، که مربوط به صلاحیت او برای نشستن در هیئت مدیره فدرال رزرو بود، به طور صرفاً رویه‌ای توسط دیوان عالی بازگردانده شد، ما فوراً اقدام مناسب را انجام خواهیم داد تا اطمینان حاصل کنیم که کسی که مرتکب تخلف شده است، تصمیمات حیاتی مربوط به رفاه ایالات متحده آمریکا را اتخاذ نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/130936" target="_blank">📅 20:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130935">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پزشکیان: برخی تحلیل‌های صدا و سیما با سیاست دولت منطبق نیست و انتظارات بیجا ایجاد می‌کند و منجر به نارضایتی مردم می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/130935" target="_blank">📅 20:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130934">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سفارت ایران در قطر: مقدمات مذاکرات با آمریکا در دوحه هنوز آغاز نشده است
🔴
ما تاکنون هیچ اطلاعات رسمی در این مورد دریافت نکرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/130934" target="_blank">📅 19:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130933">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuwCoETrZw1FCtiSSYX3T6s9-5JXgRaLOhdbQYf57sT9Q1Xd27Zzk0CRCGIjRwhz_R4rttBmw4Zin3b-u5EeTmIVjev2DmOF39BNhB3O6PT0P0Ee92cOuANVz5LSGzFqBvZUVUf5Dsryfx-3owseKvKoO0vjNJoeX2S6o0plZWrBMPlwH9gqO6CRPMw6NJ3AhThUjY6OcaQcHlYH14CWliWkj_whyyLYObrIm6twX6vGc_UjDdbLEt0wWRRGcLkl7IIhRoK85Mm-AYpkSI00bJjvPhiEy2p3U6KscFKE4gVEPcPRZR_nRmKiE2zlHkK_KvEixZtrF-OTbDVngXlL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره امتناع دیوان عالی از بررسی درخواست تجدیدنظر او در پرونده افترا علیه ای. جین کارول:
به طور شگفت‌آوری، دیوان عالی از «بررسی» پرونده جعلی که توسط زنی که هرگز او را ملاقات نکرده‌ام علیه من مطرح شده بود، خودداری کرد (عکس چند دهه پیش از یک سلبریتی، ایستاده کنار همسرش، حساب نمی‌شود!).
🔴
من به مبارزه علیه این پرونده تسلیحاتی و حقوقی علیه خودم، از جمله ادعای مضحک افترا، با تمام قدرت و توانم ادامه خواهم داد.
🔴
این پرونده در واقع علیه ایالات متحده آمریکا و همه ارزش‌های آن است و هرگز نباید اجازه داده شود برای رئیس‌جمهور یا نامزد دیگری اتفاق بیفتد!
🔴
ایالت نیویورک قانونی را برای مدت کوتاهی، که به چند دهه پیش بازمی‌گردد، ایجاد کرد تا به ناحق مرا «گیر بیندازد». این قانون به طور خاص طراحی شده بود و این بی‌عدالتی نباید باقی بماند! از توجه شما به این موضوع سپاسگزارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/130933" target="_blank">📅 19:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130932">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG0m_rVRvnsfKtX09C8cP3pX4wviMoBPPdZN4cZgv-tbQN5lCBuQNxCHgrX0ifyvorATwsFfpzugMfYib6NhOOUue60S1_9ZSnEPBnLqugBy_xASOySeOBqaS1IjoEhrftL1JFz70CfpZk-9PbrEiSljqmQF350ESXxWDyfzjoStdb_EmWFBwC3v9SIVCKD_vYhntgrzKhEQ3wpl1WFyS5Jg9AEEs0BAlW0m1OsuzIjvZfLnVi5d6vDHF_Fk46nH5WcvVRPT1M6-RO3ph-5FuQx0qQAhmaYhynZ5JrxjdJxsvf6pwnxeDOGiQvJbePgmHuGC_AbUksH4rrf8opIszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
با توجه به خسارت عظیمی که امروز در دیوان عالی کشور در مورد حقوق رأی‌دهندگان وارد شد و این واقعیت که رأی‌های «مردم» اجازه دارند مدت‌ها پس از پایان انتخابات شمرده شوند، تصویب قانون نجات آمریکا از همیشه مهم‌تر است، که عبارت است از:
🔴
1. همه رأی‌دهندگان باید کارت شناسایی عکس‌دار ارائه دهند (شناسایی!).
🔴
2. همه رأی‌دهندگان باید مدرک شهروندی ارائه دهند.
🔴
3. هیچ رأی پستی پذیرفته نمی‌شود (به جز در موارد بیماری، ناتوانی، اعزام نظامی یا سفر!).
🔴
هیچ بهانه‌ای برای یک سیاستمدار یا غیر آن برای مخالفت با سه الزام فوق وجود ندارد. تنها یک دلیل برای مخالفت وجود دارد — تقلب! مجلس نمایندگان این قانون حیاتی را سه بار تصویب کرده است. به نظر می‌رسد سنای ایالات متحده قادر به انجام این کار نیست. در زمانی که یک جنبش کمونیستی قدرتمند در کشور ما در جریان است، که خطرناک‌تر از جنگ جهانی اول، جنگ جهانی دوم، پرل هاربر یا یازدهم سپتامبر است، همه دموکرات‌ها و پنج سناتور جمهوری‌خواه ما، لیزا مورکوفسکی، سوزان کالینز، تام تیلیس، بیل کسیدی و میچ مک‌کانل باید به نجات کشور ما رأی دهند. دیگر هیچ بهانه‌ای پذیرفتنی نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/130932" target="_blank">📅 19:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130931">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر خارجه آمریکا و فرستاده کاخ سفید در منطقه قرار است کنگره را در جریان تفاهم‌نامه میان واشنگتن و تهران قرار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/130931" target="_blank">📅 19:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPCT_kQ7fUxl0rDytbcY-yBteah-uBAo41bkGYwyD_qr4-FUZW4L-cNMG1rUZ9t0UHeo02VVHcExTPZT0WPwhLi79VvhyJagzEjAUKaN0lF0ssofBelpkWlpjNsqd5BWn4LyKb5mka8gOO7xskQoPsH6YQ1_fQ1eA9JQ6USJX-unD7sLGemN68zm8XyfKQoq7_BUngQFAC_erCmPPKlrznAwZMPlr9BPaCihO3q1OonkE2BTW7c-8wIzr3FKdyIK0rXttZL2w_Xlb1L2t6S-iz7IfT3JJt74iwNjfWDkOyP6DnC61Krm_8vk7Tq6-5RAQ9sNALn6Ct1Gyrv0ALd8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvALy21ybj9Tn3Fz4wCCMwF6t__hbcj51W5PBK3x7BNkNBGtsyhkvFP1v-QL39NWYJ5l1H7GGl0fMCd0FlzPNqlwyMyKOAxQgoMsyddOzMaKiOrXzKr79rlM2g6rjR19AHTAgq7ILwEbK7FDrAAI_VCf98aMcbNPMXI9Iwosttkm6GX4Uyx4CCxuahTRU7IwnAQB6aYLgxh-EiZrX1ArkB1mlJ2VpzkHS6o45UAEG_boXdAYwe09XA9rxJ4UoVpvzgnCj9zJcG8id-Hw1HCywoWqI8bXYzu8Y_KlFXwjUsY2d3PoPOQZP6wswA3xtBIPypluWR9gR54TlwmjWi0LVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbXPHKsm67WTHRMuCJa6jGpzchiB9FScFJ7Bzc_T3HrPWQgIn4FUCeA9OBZi03CoN8qlWodXML6NL_MWFolHrkJxB5e-peHB4g8PrurAlxi7Z0zdtiiJmkWHEuNS3N_zcoksByGAxuZa9nx2LY6slRc9nONDAXpa17V5pUYUU0Gpznoh2kIqBkdOpAN1lJOUTQdJ6xTTlqp_3bLQDJgbZTM8nei1hWdcc2xRUx2-k8Agj1yki5HoWU9l4f76JQgEhww64BTBHBUEoFMlLRzvsgqjgaBjv401NSbPD9aBnWpcsbMzOY1w_m93DhTRhxxxUzV75v3wwefajtSBRgKfAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از اجتماع تعدادی از قبایل یمنی در صنعا، در پاسخ به فراخوان عبدالملک بدرالدین الحوثی برای بسیج عمومی با هدف پایان دادن به محاصره یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130928" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQcd0gSbs2rWFxSDsR4GeewTqk3fHtOJMg9qqkQYhs80ZKiR12tX1ZwOZAYIg8821vjsKeY93QTm-jDD-uFtPYE_IiAVQLnq0OK4jVt5vz-3cNU_iJEEuxICnfzt9sGMBZTlW5yjlWrGjABnImGTKHHAgZjVEwhXg30Jak9gQyBN8IJuNh254oWbf0dZ65Dhjds0Ypoj1RKdvlgmm_YBhTFP5WuQ3KNatQunjoJnMsUEaOAq2P9bElVCaq4mvcoxN5IrENvZP_--SMZAxTiVrebd1_pmrc5DRU12uoOCIo2IvxXtt5AxGeFGp5pYqHaAExxM6hoDQUivTKuhQ_b9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داغ‌ترین شهرهای جهان در ۲۴ ساعت گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/130927" target="_blank">📅 19:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130924">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاطلاع‌رسانی | لگ‌لس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjF8hzCyFXqJffc6lLY_lDLm0DZHhNqHAiMNvuwLgrwyXFK2On04zT72LI5FBi6pC6Bh3F8b892Cbvu1IUqDDiqUuEl_bHBELwfNtIob9WJ8VDUZR0vFIwoVKZ29vtIv3pPUKAb9sV3BvxY6zTeaFVffux81wUUEV8BaquA66beKPXLkchGi5RmU4RLN5ThCbMm5SQI3oxK2M0jgHEPPHIuqwkbJ8Lfz2vakGd9ajzgL_6OyM_jzEvTo66L4RnnbcBHB49AanIq9ZxQzNwbY4ti9jLBG0iPK-hTE7EXB8OKe6q9p9IVPbpo8A1v7pIIhyYq-cuoDIz2h9u9ff6iDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
لگ‌لس٬ سرویس هوشمند
کاهش پینگ
مناسب برای پیسی و موبایل
کاهش پینگ و جیتر روی همه بازی‌های موبایل و پیسی
با ۳ سرور قدرتمند اروپا٬آلمان و خلیج فارس
مخصوص بازی‌های آنلاین
پروتوکل قدرتمند وایرگارد٬ بدون قطعی و تضمینی
برای دریافت تست رایگان کلیک کنید
👇
@LagLessBot
@LagLessBot
@LagLessBot
@LagLessBot</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/130924" target="_blank">📅 19:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130923">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B29PKVKoZgP9L5qwbeA5irCYLznXuA71wWHy9cWuTr6y-CgABLQDQYv2R20p30BAPWzsAg-Ie809S10wFYLrkpz2BbwbcYALAaPCpQ8RRV9np-v-da7NQFlxQ0qbCi89RPFJJuJm4e__W0UB7f2ypl9Q0ZUEbjwA967A59OcynOCNV27J9MdkGNX9dOav8iQ5QqNq1iLRKt5OLfRTSh5bmf62TyKz-SAah6OY5llRO22_RuabGwkE-IgJJ4BTVaeZh_fOa997zENzQIXEBRM5MxPG5Xn7YKQdNYqAGwUM3RBiWEh2cdb9T9pB_YX8LqLJw6qzELHdfYvwbZXRFRNkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع خبری از وقوع یک انفجار در اطراف منطقه دیر میماس در جنوب لبنان خبر دادند.
🔴
تاکنون جزئیات بیشتری درباره خسارات یا اهداف این انفجار منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/130923" target="_blank">📅 19:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130922">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سنتکام:
بیش از ۵۰ هزار نیروی آمریکایی در حال حاضر در خاورمیانه و در حالت آماده باش هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/130922" target="_blank">📅 19:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130921">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1tQoXvgahydYbYWvqA9xLxYHL3ByTkSUn1mKXJqMdrSyIho3qGb8TarsEz0m4kkoi9OG17NXsgG81-gWekp43FL6YWTB9aLq0iWU022ouEkB1waeUQlxNW3vry5O6nXzkFu-o75zQilGGwvAF69H0drwL_2kWOM2INNNuNgXRn4OVnFwU2fXp0uDt2Z7FAih65gj7L90RGFhYR8yOJ9gr3zJRULDWG2nr6E1n5rAJMp0USA22cRf6RgY7VHraRNaA8C13hlMpW2aQT181RgXRNiS-uDfdAXNg6h-S6cI-eh24FOFxaJOWtQm9HsddTumhio2J0oEuU_13BzEGUEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خراتیان،کارشناس حکومتی: ساز و کار انحلال سپاه در برخی محافل درون نظام مطرح شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/130921" target="_blank">📅 19:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130920">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
یک مقام کاخ سفید: روبیو و ویتکاف تلفنی کنگره را از توافق پایان جنگ با ایران مطلع خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/130920" target="_blank">📅 18:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130919">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سیمایی وزیر علوم : نام رهبر انقلاب آیت الله خامنه ای ، در کنار کوروش کبیر برای تاریخ ایران خواهد درخشید،چون مثل کوروش کبیر تسلیم نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/130919" target="_blank">📅 18:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130918">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کاتز، وزیر جنگ اسرائیل: ما چندین هدف آماده در داخل ایران داریم اما اکنون اقدامی نخواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/130918" target="_blank">📅 18:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130917">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJDVDhy8HetOrrzlHQ-J-co5sGhlZ8E5bvMHSp_nMUDemAGaVsCHgvYr31zEpcF2Oo2w4FmV-_Okpnc8oQoWXslojiv7z6goShHCnOnEUQtjB9Ej-6RHPBUcAryxs_othNRGDwZeq2P_A1_Nxm7PGPbijfvJIGXJdWsbk2kgmcUjnbii1l2DMv3TnPAbyQdRRyUhytLHapRJwA7uUGKVIhY3nJ_-T9nklEhkgko3bDm797t4RzSFZ4sfc5ZqtJP7cVYl_rIup8Wt7-TCUDj0uATYuL14oACCg6nt0NsE6aEjNfs75-qNR_PjiLc5YRayzLUDHmJHKgB6v10vqT8dXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه قطر: حملات اسرائیل به لبنان قابل قبول نیست/ بندهای توافق اسلام آباد باید اجرایی شود/ ایران همسایه ماست و می خواهیم شکوفا باشد
🔴
"شیخ محمد بن عبدالرحمن آل ثانی"، وزیر امور خارجه قطر در گفتگویی با شبکه الجزیره ضمن انتقاد شدید از رفتارهای جنگ طلبانه اسرائیل علیه منطقه به ویژه لبنان، خواستار اجرایی شدن بندهای یادداشت تفاهم اسلام آباد بین ایران و آمریکا و صلح و ثبات در منطقه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/130917" target="_blank">📅 18:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130916">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUTpH66zH_eEcwKKZGuZNWA1KM55BcTtOsPhdJVyKb33DHmz6e4JXUT0aTXyEOk7leFWoQTicb82zoLDinp7-vQxgMsPCoyWdR4VfN5s-oGY0gUli4WILgSCPcFNkLSM7H6cq2dvsE0UDwsjw37k8oRoxSBr9BSfp2K8HzJzVgID3JBdektNmh3lqzwE_lV5rN2Lhid9gr0SDmybTrN_ne1Q7xkWyfjmLGvXCFHZKbG-wFRwksWJMKb-yR4wARsp8rqGeeYpwYpQ8afS4kJagiX_pAfOSGL-CF2-3817NlvCZxK84j3GbaRQPzWVlJXrtO4mI0uVIlpj6hD4QtyVaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماسه‌سازی تاج بعد از صعود نکردن در جام ۴۸ تیمی:
🔴
نه تنها در هیچ مسابقه‌ای شکست نخوردیم بلکه به میزبان جام جهانی هم باخت ندادیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/130916" target="_blank">📅 18:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130915">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
طبق برخی اخبار گویا به هر بازیکن تیم ملی فوتبال قراره ۲۰میلیارد پاداش داده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130915" target="_blank">📅 18:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130914">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtszfKszxiteO_3AiMnYn3Xayx6NIYdJw1mQLy3Ka3zmQTz75JBKyYNDJcWDnz_WaR6-QNfp6OyUS5U15BmlJmr9VTqOynmz_b964j1evkCJbllJ8arTMuAgtjXcU5teZm8CUhjyX0-fRZX2frocROx6MZixjjT1YSKu4IgNAmezg0kbH2P7jHvcoBHV_s6FKQYyZQ5PRKdIsqyroVj1FfMTIslB1KziyuIYgeJenRKFfCkrJqNVshU48Y8KcP5sOvJJ_dEqRjIFKu4Zz2pI7axSpubK9MEDflm-Qb54SGY1L4mzFdaT-KOQxbrnKDFDUypGz83v_tya053rp1Hxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از 1500 سال تاریخ درحال تکرار شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130914" target="_blank">📅 18:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130913">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXQ3bhdmF_3P1cHqQRcpD5qg5gRFvZCb_a3zagmoEpg8HRui5FIcF4vA0qNzrnYaBR8vRB3BmkRX4FG2KdRebBRftiNZH8SPp1cFoPa2-CRuXRCSNFE3Iu-w752kBWxSBdZMIs2ZIsBTcl3PDDWxjYabu2ME9qWNpQw_Jr6IcAcrEkufVzMVhGcgs2z2_iFD3NuM-84nDfnUxopW3zT5HCN1MQvJGrAoIUWeSusBdROrcK5nWNOhmn8IVHKxDeFAHLVJqA5aWRFBiT8RRfPbSUOZWazg25Sa-va24PX7i1sRaTYO-eHf3eBH1x1W_97B5-55iKL384XU-SFFtRv-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار فرمانده سنتکام با رئیس‌جمهور لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/130913" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130912">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26cc6d01b.mp4?token=RSp59Vou43u95ddfzGU3qlxoXNzRi0z2b1yogIL7Wj3QP-3ZknA9H4iEh3kpCDItOcSHMNqC-XRVTFGkWvtKgQ1hwk-DYZorJCZycb57dF9so6UkeQamDMZJg4uCAQ-xIh2YdV5yyNAq7tOKVP6jsMsCoepEyzCQhD15HsNW-yBj6_lyG-xJMHJ_P1Wjfxyjkn7rla_vaWrEHNiY7vG1sW2_VcM8D7Rd4CkDfmCEqQMKXhNU6DHGUFNjEUEZd3IFARtHyKWEWtwdbuqCVD5pQLp0x6xcS9lWJ4RVM3sXx5e3z8kubWhhnF8pts2G7CHwwxSgL83XHHYKEqy27p8agA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26cc6d01b.mp4?token=RSp59Vou43u95ddfzGU3qlxoXNzRi0z2b1yogIL7Wj3QP-3ZknA9H4iEh3kpCDItOcSHMNqC-XRVTFGkWvtKgQ1hwk-DYZorJCZycb57dF9so6UkeQamDMZJg4uCAQ-xIh2YdV5yyNAq7tOKVP6jsMsCoepEyzCQhD15HsNW-yBj6_lyG-xJMHJ_P1Wjfxyjkn7rla_vaWrEHNiY7vG1sW2_VcM8D7Rd4CkDfmCEqQMKXhNU6DHGUFNjEUEZd3IFARtHyKWEWtwdbuqCVD5pQLp0x6xcS9lWJ4RVM3sXx5e3z8kubWhhnF8pts2G7CHwwxSgL83XHHYKEqy27p8agA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله خوارج با شعار مرگ بر سازشگر به عراقچی در کربلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/130912" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130911">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
دولت عراق تا پایان شهریور به مقاومت عراق مهلت داده است تا سلاح خود را تحویل دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/130911" target="_blank">📅 17:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130910">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/130910" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130906">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHMLimsMLlWr51lqcMkDf7RvhWdRxBOkdLlqESnj2DTGJyvyzkYajxUbS_MCjvCKFz1-L_ASfSskiu4IuxEwQMLqA5qMr2jI_SrLGPWDpouEIj02rAeeIByHtSeoyjd7WBseZNDlQijEkH_gReB3AmR-ygFNkSP3gwcuFsOwZky0BzSGOptJSveP7NAkX6x24t1noUAq6wwT_rPQ7u0LsR3DRQ-iJ8JYDeJeqEiLG2xUo0QA8ZY6pFlMp3gvEnlDaxKjRStxdGisnzOVlutwAvSXVlVO8Ywwc2m23MnOzqeEZq394vRWUZaLy4lmbrjQ5iI3C5iMl26JTZIcvf-_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39e76a3148.mp4?token=ArRGzbZOLPYzIjsSqHzTgmcOt1683A3K6Xwf7grqjEpyDJnie-ZJGw2QBkdjBRF6oq9C_WKST36V22hQYSxG9MtstNMtf4zObCWdtvXGFv7_h-iWIjAFguXTlyXHBcUmwGRnK1x-rDL5Of0lKIX9jUbW3pi66PQP71yq9D740gN52J-0wO3_HHQ9BW_oYvOB07Sp2UbsQ5LausCRicQhDYLRSo-OQM4wsH2VfmEmfdUnw7_eDlTS8-MJgF_xaHCzHUm0VA1Zf887MRfRTBuwPwTpUnhEr20n57FDXdddU4IeLZoLqlwOsYuVbWnOSEAYLLUDDqTac0bChBsZCTez3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39e76a3148.mp4?token=ArRGzbZOLPYzIjsSqHzTgmcOt1683A3K6Xwf7grqjEpyDJnie-ZJGw2QBkdjBRF6oq9C_WKST36V22hQYSxG9MtstNMtf4zObCWdtvXGFv7_h-iWIjAFguXTlyXHBcUmwGRnK1x-rDL5Of0lKIX9jUbW3pi66PQP71yq9D740gN52J-0wO3_HHQ9BW_oYvOB07Sp2UbsQ5LausCRicQhDYLRSo-OQM4wsH2VfmEmfdUnw7_eDlTS8-MJgF_xaHCzHUm0VA1Zf887MRfRTBuwPwTpUnhEr20n57FDXdddU4IeLZoLqlwOsYuVbWnOSEAYLLUDDqTac0bChBsZCTez3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پس از ورود دکتر عراقچی به خاک عراق، از دیروز تاحالا تو این کشور داره کودتا میشه
🔴
بنا به دستور الزیدی، نخست‌وزیر عراق، عملیاتی برای بازداشت تعدادی از مقام‌ها و چهره‌های سیاسی این کشور که متهم به فساد بودن صادر شده.
این عملیات با کمک نیروهای ویژه عراق و سرویس مبارزه با تروریسم (CTS)، خودروهای زرهی، تانک، سلاح‌های سبک و سنگین انجام شده.
تا الان 47 نفر تو این عملیات دستگیر شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/130906" target="_blank">📅 17:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130905">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgwKJkG4Q-5MUZa-DEY_fNA0w4-Twfjwl-BPadc5XrCALw-60teNu_3G6Up9DCsE4EOf_jmCSNJAIfRowdXnlbfYF3htZt76e4vXrjfT7jQojSB_cLxY6QDAS7NXF0dTDceiPXLhkvLb0NMhgYZkQ1tVg0BdifU6UjmOlaL63XZXHzdtGOoWl4wu8yiZ4hNVELOyL1NY5l9IWLYj6w_ufxOYK946SP1tyyNPtPJagKEmH7Tb_zvhJ9zomuQ9lAiF9qFtacej5esV3tYoqoXZwJVaQwfSQ0Reb_y50lll8Z2ElpJTyvHDoqBRcSeaJf8Y2wY71XGejk62-wBlo_Ngng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده سنتکام، دریادار براد کوپر، برای دیدار با فرمانده ارتش لبنان، رودولف هیکل، به بیروت رسید — هدف اعلام‌شده، نظارت بر آغاز اجرای فاز آزمایشی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/130905" target="_blank">📅 17:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130904">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کاخ سفید: کوشنر و ویتکاف به دوحه می‌روند
🔴
سخنگوی کاخ سفید اعلام کرد که فرستادگان آمریکا به منطقه و مذاکره کنندگان آمریکایی، قرار است برای رایزنی با مقامات ایرانی راهی دوحه شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130904" target="_blank">📅 17:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130903">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / ترامپ: ایران درخواست جلسه داده است. این جلسه فردا در دوحه برگزار خواهد شد!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/130903" target="_blank">📅 17:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130902">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سپاه : انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/130902" target="_blank">📅 17:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130900">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_2YS99NpzUk1kmOTxP6cfdo71acc_lGqtsrKfQf1Nr4RfNTUkHEnuQiOlkhU8N2R8cGOd9YS0U2wNivtHju9uG-MHPq_575x7RKSSwkMyHslYqZIN_S7tTXFXketZ13lgFD-TXZOsC3O0aDkHhlkQwrZWMkZbNrUIYmPUeRJRLOOrzeXQlqb7loVo2B94XIUeIaZ4iCe1iihQsPUCwgid_vznBmlP9CJm8uNfAFhLHXaABTZKbHOyu_W6pJIHsF_8levaEVNpWSsM1tGIiFHQ68WnC0rhLbDvQpGoAuTr4-lx6O2wv2N2NxBexuV7fP7gTlrQDWrneFIRxCWnHO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIQBErW8XbY0q36ijEgB1Ti79bBwjPL8JWGaw7HxUE3MMYjgrOUzoNvDdfl1xxa5uYjv3XN-jxdp68FsZ7xxurtsWudwhzHm8X-ogrZNcKV0c6muN0ul7FvPmZ8sictiW33TSJh6ZSsgYu5okyREE37DbLJIZdGo797AzsPYpugR9jTvBO7EGC3ytM0X4AsP1ObKgLdhLgJ8hqZuSIlSKk3Tk8WEeUo3UF2lgceEk6pnPXgneOLLn3e60RGbNKpVUw8rUEWGCIW8mWkAWVkmJvyRfcK-UBrAYnIj3YnZB6guAKhy2NLpH3--jIdhjrek_8QOleYSgzQy9uGFgJzb_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه، احمد الشعارا، با وزیر امور خارجه عراق، فؤاد حسین، در دمشق دیدار کرد تا درباره روابط دوجانبه و راه‌های گسترش همکاری در چندین بخش کلیدی گفتگو کنند.
🔴
دو طرف همچنین تحولات منطقه‌ای و بین‌المللی را بررسی کردند و بر ضرورت هماهنگی نزدیک‌تر در مواجهه با چالش‌های مشترک تأکید کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/130900" target="_blank">📅 16:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130899">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
هشدار نیروی دریایی سپاه به شناورها: تنها مسیر عبور از تنگه هرمز، جنوب جزیره لارک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130899" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130898">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbMrOsnOmJbLSKnicEMA2wLAtV1_9UnCoKN6Tev9vDJzBOs2dp-alnzApAsQ5AfOZfmE7VgITe5V-BH2owRbozdpPYguE6UQZYTtP7knmaJ_mRInL9GdLLvRBpFvh1dolFbskmMDmz7MUn6L2yTRQ631CrTmQvrCUBbRE1s96T9nYIoiiPVwEdc5CecA5ga4EajwcOUVQxRn8XSZvxTLKN1pcgBgZMYi-3cmksUsC2j0b4UGJ4ScRxHF_0v3rGmL20RqbxilsefTSj6W_ykGNXv4GhXPzJda9VSk2aCx3CWtdZnx6Pp5MtXVHwo2eaeotSuEEDT1oR1vEA9Dh75XwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: کودتا در راه است؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130898" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130897">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HC0Pyg00OxUmnIgJTKMUkun9L3mEuG8SU-9BLH8wG2MH3ogPTH5uBH_ux0CPrGeVj2Qj2z4NiAwDbYmEO6aZ8js2mKbU_UxXz0u2bnwEcnKTTpippWqnM7qKhBoIVk71tVWGCSxz0iS5wS8v-Fdu4DXGT-1HXCbnc_ngEa7kFuVu8Z9FOF2tNOfDQPSQFRiK5_hjuJ-b3_rjEnZcHfZkqfdZTuS9FHR5avt43YJVLe2A5n_SMbpjFDViAe316YRgOFVg991v7pBzYk0iSzFNYVE7giSq0eYnavMR_gRle0mxmjrCwRwaL2GK5cGYHKWJQs2igmGNzVsuw1P5a8u6Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکی از کارشناسان صداسیما : تورم تو امریکا داره بیداد میکنه و کمر مردم رو شکونده، مسئولاشون بی عرضه ان
تورم امریکا تو 1 سال : 4.2%
تورم ایران تو خرداد ماه : 89%
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/130897" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130896">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر کشاورزی آمریکا: محصولات ما آماده ارسال به ایران هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/130896" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
