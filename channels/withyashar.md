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
<img src="https://cdn4.telesco.pe/file/R-2G-6ZRbML_SHh4yUJa_DcAibIynRy-jfbi9pWdgUti9xO885JSKZNFcbxjePOD4SmTdipJ-34Cjf-0aXPCEqEUb-a8hjWRkK5MfrMxpn1n-hdWXKqGL2bB0zBGEUwdloRuPk9w_dL_IyQq8htZvMPfqJJGDJU4OctcDVIcE14F1RoEMYsxUd-zmkgmMl92G4Iobn9R-FOsknfZGp5DU5Wuhx0pTiP-c3jLCGToe1SJY9tClxz7XWoXqhiOs7oF4u1UZDIQokcKdJ_SpkMpu5eXcXIw2Uv0xb1DreSBkLgaCoc17XsfFGCNmLgv_Da0NF6gK63ie_O8YIGqM0woSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 19:58:23</div>
<hr>

<div class="tg-post" id="msg-15343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آسوشیتدپرس: ایران به امریکا اطلاع داده است اگر اسرائیل ادامه دهد. همه چیز متوقف می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/15343" target="_blank">📅 18:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15342">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">محمدمنان رییسی، نماینده مجلس:
خوش‌انصاف‌ها(منظورش قالیباف) مجلس رو باز کنید، رهبرم تنها مونده.
@withyashar
قالیبافم باز نمیکنه تا جا پاش محکم بشه</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/15342" target="_blank">📅 18:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15341">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال 12 اسرائیل: نتانیاهو با مسئله لبنان سعی در خراب کردن تفاهم نامه بین آمریکا و ایران داره.
@withyashar</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/withyashar/15341" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15340">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خبرگزاری تسنیم:
هر دقیقه باز بودن تنگه هرمز خسارت مهمیه؛ اگر آمریکا فشار انرژی رو از روی خودش تخلیه کنه، وقیح‌تر و تهاجمی‌تر هم خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/15340" target="_blank">📅 18:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15339">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حمزه صفوی، فرزند مشاور عالی رهبری افشا کرد:
یک روز در چهل سال گذشته نبوده که ایران سودای ساخت بمب اتم نداشته باشد
تمام اسناد IAEA، تورقوزآباد و آماد نشان می‌دهد که حکومت تمام تلاش خود را کرده اما همهٔ اینها در بزنگاه‌های تاریخی لو رفته‌ است.
کرهٔ شمالی وقتی در دههٔ ۱۹۹۰ با آمریکا مذاکره هسته‌ای داشت، در دو سایت دیگر خود پروژهٔ پیش‌برندهٔ بمب اتمی را داشته و لو نرفته اما دو سایت فوردو و نطنز را ما اعلام نکردیم بلکه لو رفتند.
برنامه هسته‌ای ایران، گران‌ترین برنامه هسته‌ای جهان، نه برق آورد، نه بمب، نه امنیت
@withyashar</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/15339" target="_blank">📅 18:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15338">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سخنگوی وزارت خارجه: برگزاری نشست سوئیس فوریت ندارد
یکی از اهداف اصلی نشست سوئیس در روز جمعه، امضای متن تفاهم خاتمه جنگ تحمیلی بود و قرار بود در حاشیه مراسم امضا راجع به ترتیبات مربوط به مذاکرات توافق نهایی هم تبادل نظر شود.
با توجه به اینکه امضای متن یادداشت تفاهم، در بامداد ۲۸ خرداد به صورت دیجیتالی انجام شد، برگزاری نشست مزبور در سوئیس فوریت ندارد اما درحال برنامه‌ریزی برای برگزاری یک نشست طی روزهای آینده هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/15338" target="_blank">📅 17:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15337">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">از زمان آغاز آتش‌بس، نیروی هوایی اسرائیل بیش از ۱۱ حمله هوایی در سراسر جنوب لبنان انجام داده است.
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/15337" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15336">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک مقام ارشد در کاخ سفید به آکسیوس:
«نتانیاهو با تمدید آتش‌بس در لبنان صد درصد موافقت کرده است.»
@withyashar</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/15336" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15335">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حزب‌الله: هنوز هیچ اطلاعیه‌ای درباره زمان آتش‌بس دریافت نشده است
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/15335" target="_blank">📅 17:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15334">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کانال ۱۲ به نقل از یک مقام ارشد اسرائیلی: آتش‌بس به ما این امکان را می‌دهد که به تخریب زیرساخت‌ها و اقدام علیه تهدیدها ادامه دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/15334" target="_blank">📅 16:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15333">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرنگار المیادین در جنوب لبنان: همزمان با اجرایی شدن آتش‌بس ، حملهٔ هوایی اسرائیل به النبطیه صورت گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/15333" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15332">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">باراک راوید از آکسیوس: یک مقام ارشد آمریکایی به من می‌گوید
اسرائیل و حزب‌الله بر سر آتش‌بس مجدد در لبنان از ساعت ۴ بعد از ظهر امروز به وقت محلی توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر و پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/15332" target="_blank">📅 16:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15331">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش ها مبنی بر آتش‌بس بین اسرائیل و حزب‌الله هم اکنون به اجرا درآمده است
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/15331" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15330">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWI3_URizy64ZVI07XpvWliKxLR0Ggto-kzwQIFy5nKPit9RnuwtGIxnF_DJXy8HunEnMt89UyDpo4N_JCwp6uV8L013XssZB6kvfgRWHssN51WWjyhJx6eHfC9jpMqvvoXegmbj4dZ-PGV6Gu9r50I-xUyZbvXfqBnWOqSE6BjJvVwBsFdk93WualJ9AkFkl88z4pvOsXjA0_Z7r2Mte6_CGTtuOiwjVbj5O2tZD7Os2cQQRYXEulLtNpBxhuMmITfyL8ncfpVncA5YpzE6gEM5WzSyLfHbrSddEpJV2PbLeyL1RIfiQt8R4JPlnEdsO_QrPuG3naSHro92XLWUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از یک مقام آمریکایی ادعا کرد:
«حزب‌الله و اسرائیل با آتش‌بس موافقت کرده‌اند» و افزود که مذاکره‌کنندگان از آمریکا و قطر با حمایت ایران به توافق کمک کردند.
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/15330" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7oEgEysSkE-oNE6DDCHFL5oYHtIwuXoboMVWBjTSUxxpcrk9Rs9GgRBRXUgNEWWdq70_Gdn4WsdDJn0roa5LERsqhJIzN47HEvUfgcs2_rN4Jh9QJOK79bSyPAwMVFBvgELkFQSonPj3q_i7grY9A1SLLTVASRDNoN5CpXdQNCZ60x21hnBSuLD1Xau0kzstDKXwLYDufaQWVmlymZGJHUvzpv8aqaKaqCWBY60_Bnf-gVBGwisEq11DGxWnaBiN_Tx0SlMuPg6TsRj588qvPvncb47bt-5oTk1cOS5vCAMOGkYNPacIHh0MqUVWeQ7yEr6V_MBsf_WKlA95k4KcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : ما از روی استیصال نرفتیم سراغ مذاکره
این ایران بود که بهش نیاز داشت، کارشون تمومه!
همون ۶۰ روزی که گفته بودیم رو جلو می‌بریم، هیچ پولی هم گیرشون نمیاد
@withyashar</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/15329" target="_blank">📅 16:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5PInIuhAf-ppET1BAybZ9ML0ZXdmfmzI0g8uqT68cPjPSyJOnU1KNTZkGak7rqe52gmq-w3U9WkCSxbwhSdPWIog_smXa5tKhfXmiSJEpiY57jWQPQy7DrrA0_k-OrqW6knFtc4H2iX24IaXeU5wx1Ph7z-hsUUn3aLmSOfERJBbifHkOaAhg4XUPW6kjCoaFFQLqItujSWLPvFM9sirI8jnxkTPxO16Dzr8IYh14N6apmFiiEHlFOYi8VyjrmHglwIfCgyWuy0ooofqKsKZ1CL_z_rlexSlRH5HaGknn6n4NH0vlsEwHW7zIoVVVD9UyUPXqvhtP7M_YW7q_VGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ در‌تروث : جنگ ایران را تضعیف کرده و دیگر نیروی هوایی، نیروی دریایی، پدافند هوایی، رادار یا تقریبا هیچ‌چیز دیگری ندارد؛ با این حال دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش در وضعیت بهتری قرار دارد. باور می‌کنید بتوان چنین حرفی زد؟ بعضی افراد چقدر می‌توانند احمق باشند؟
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/15328" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سنتكام: جنگنده‌های اف-۱۶ به گشت‌زنی‌های خود در خاورمیانه ادامه می‌دهند و آماده مداخله هستند.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/15327" target="_blank">📅 16:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15326">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">طالبان استفاده از گوشی‌های هوشمند رو برای تمامی کارکنان نظامی و غیرنظامی خودشون ممنوع کرد!
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/15326" target="_blank">📅 15:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f67ff589.mp4?token=aV01hN8PpIKjr9Ai6IB-xYvpANd4Q3XdolJfB73Bn405dkGoIl1mXbJCMIVq39vtwxDuWpnneh3Hvsjt0FxCPvOI5Vi3bj334-vehRGpIB7GsQ-LgVP8cet0eteohv0MZcZdm4d75aPL__uIwIIyk9TIEp_CWij7d-_F7yhcH1Opx3E9s1623v3wx89Uf0TFA14ylyIxDHSzRqqGc9AnNsq5Rmts5Aw_8YoFdmBNyhc2lJOBDSt9vDqFsMFK6QwBwwdQ4_rLittI-LXFES4KzvWhOAct9xAQ969KnRE8F-6SWJPO-OrIyH8OKP96fT2hJRiJ2qENc80s5vZVIND1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f67ff589.mp4?token=aV01hN8PpIKjr9Ai6IB-xYvpANd4Q3XdolJfB73Bn405dkGoIl1mXbJCMIVq39vtwxDuWpnneh3Hvsjt0FxCPvOI5Vi3bj334-vehRGpIB7GsQ-LgVP8cet0eteohv0MZcZdm4d75aPL__uIwIIyk9TIEp_CWij7d-_F7yhcH1Opx3E9s1623v3wx89Uf0TFA14ylyIxDHSzRqqGc9AnNsq5Rmts5Aw_8YoFdmBNyhc2lJOBDSt9vDqFsMFK6QwBwwdQ4_rLittI-LXFES4KzvWhOAct9xAQ969KnRE8F-6SWJPO-OrIyH8OKP96fT2hJRiJ2qENc80s5vZVIND1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاهره و بیروت ما داریم میایییییم
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/15325" target="_blank">📅 15:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تحلیلگر ارشد و رئیس کل ستاد مشترک ارتش اتاق جنگ ، سر ادمیرال یاشار : مسیر قاهره از بیروت میگذرد @withyashar
🎖️</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15324" target="_blank">📅 14:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبرنگار العربیه در سوئیس: مذاکرات بین آمریکا و ایران ظرف چند روز آینده آغاز می شود
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15323" target="_blank">📅 14:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ به طور هیستریک عصبی به ثانیه در تروث در حال پست گذاشتن است. خواهیم دید چه خواهد گفت.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/15322" target="_blank">📅 14:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تحلیلگر ارشد و رئیس کل ستاد مشترک ارتش اتاق جنگ ، سر ادمیرال یاشار : مسیر قاهره از بیروت میگذرد
@withyashar
🎖️</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/15321" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الجزیره : نتانیاهو: حزب‌الله بهای بسیار سنگینی خواهد پرداخت
نتانیاهو افزود به ارتش دستور داده است در واکنش به «نقض آتش‌بس» ضربات شدیدی به حزب‌الله وارد کند.
همچنین ، ارتش اسرائیل حدود ۸۰ هدف متعلق به حزب‌الله را هدف قرار داده و «ده‌ها عضو» این گروه را به هااکت رسانده است. همچنین امروز یک مقر فرماندهی حزب‌الله در منطقه بقاع هدف حمله قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15320" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15319">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مشاور هیئت مذاکره‌کننده ایرانی، مرندی: نظام ترامپ به توافق پایبند نیست. و ایران در این شرایط یادداشت تفاهم را اجرا نخواهد کرد. اقتصاد آمریکا در معرض فروپاشی است و اسرائیل مجازات خواهد شد. @withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/15319" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15318">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نیروی دریای سپاه در بیسیم کانال ۱۶ دریایی: “از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/15318" target="_blank">📅 14:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15317">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش‌ها از شلیک مدام قایق‌های سپاه در تنگه هرمز حکایت دارد.
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15317" target="_blank">📅 13:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15316">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">باز‌ تنگه دعوا شد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/15316" target="_blank">📅 13:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دقایقی پیش براساس گزارش مستقیم از چند کشتی در خلیج فارس، سپاه پاسداران حرکت تمام کشتی‌ها رو متوقف کرد و عملاً تنگه هرمز رو بست.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/15315" target="_blank">📅 13:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وزیر امور خارجه پاکستان: علت آغاز نشدن مذاکرات سوئیس به دغدغه مقامات ایرانی به مراسم ماه محرم مربوط میشه.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/15314" target="_blank">📅 13:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مشاور هیئت مذاکره‌کننده ایرانی، مرندی:
نظام ترامپ به توافق پایبند نیست. و ایران در این شرایط یادداشت تفاهم را اجرا نخواهد کرد. اقتصاد آمریکا در معرض فروپاشی است و اسرائیل مجازات خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15313" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شبکه CNN به نقل از منابع آگاه اعلام کرد که پیش شرط ایران برای شروع مذاکرات در سوئیس توقف درگیری‌ها در لبنان است
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/15312" target="_blank">📅 13:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b3d24142f.mp4?token=HpzeMUFvKgmCZC5mYz8vS3MxXoZ5zagqlXLyExxOUHoUdEcT_yjssvCN_RuqdoDUKnuAVHGLVF-HIEtNiSvK89h1W55QswrVGqM8KW_ejWNuO7nfvkTxixn8hMo-afAimh5QtS10FWrWZj_zs4-ms9h3NfencqXaYVkQ1B_lwNzWhM8E8y-FVIAlHHlks6xJS-VlXl9hED3efY20mBu2BLDurdazSoBM-p3hfq0qm5Q_OygiSt6lbj6jxKXh8VxlTY0pVxwMWr-J5aWsda12rtBq66bkEv9ZSuVOsH1i4ZvBVGXLxEvT-C-OXNzr3O2i7sYdhuLvXkLakcSnhv0YMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b3d24142f.mp4?token=HpzeMUFvKgmCZC5mYz8vS3MxXoZ5zagqlXLyExxOUHoUdEcT_yjssvCN_RuqdoDUKnuAVHGLVF-HIEtNiSvK89h1W55QswrVGqM8KW_ejWNuO7nfvkTxixn8hMo-afAimh5QtS10FWrWZj_zs4-ms9h3NfencqXaYVkQ1B_lwNzWhM8E8y-FVIAlHHlks6xJS-VlXl9hED3efY20mBu2BLDurdazSoBM-p3hfq0qm5Q_OygiSt6lbj6jxKXh8VxlTY0pVxwMWr-J5aWsda12rtBq66bkEv9ZSuVOsH1i4ZvBVGXLxEvT-C-OXNzr3O2i7sYdhuLvXkLakcSnhv0YMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توقیف یک دستگاه نیسان گاوی عجیب برای اهداف خاص توسط پلیس
@withyashar
🤯</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/15311" target="_blank">📅 13:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bffa7007.mp4?token=bqI7-R2sEvzDtz4BZcvDQdBeOQFikrg88ad1gwUnuO4sijRc_3cu6zWD9H4bKKmCAZFwUMj9q3sbO237MW3A7RXsSl4tRjxoMxjzXBqUqz0N8nNa5ypCKzm1DPIrbOLezqMBuy-B8f98sQq5RFn69D4XhRMO-krlclfAv5ZWWvTxZ7V1W0-SOLzya_DxD7N5K310KUHQY71k-nlIeoQcPIrx5nc9Iiw9IM9PsGS04ka3minzP80RaX2890KKPkFKrVPZvS8o0uQvKWtAzLPlyWSjTVTBgj8IKzUUmGp5vWMpr0D6yDJvcqMGiNenJHIgyTmDl1HnwL3ju1W6TAS7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bffa7007.mp4?token=bqI7-R2sEvzDtz4BZcvDQdBeOQFikrg88ad1gwUnuO4sijRc_3cu6zWD9H4bKKmCAZFwUMj9q3sbO237MW3A7RXsSl4tRjxoMxjzXBqUqz0N8nNa5ypCKzm1DPIrbOLezqMBuy-B8f98sQq5RFn69D4XhRMO-krlclfAv5ZWWvTxZ7V1W0-SOLzya_DxD7N5K310KUHQY71k-nlIeoQcPIrx5nc9Iiw9IM9PsGS04ka3minzP80RaX2890KKPkFKrVPZvS8o0uQvKWtAzLPlyWSjTVTBgj8IKzUUmGp5vWMpr0D6yDJvcqMGiNenJHIgyTmDl1HnwL3ju1W6TAS7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حساب رسمی‌کاخ سفید: دیروز ترامپ تو نشست سران جی7 وقتی وارد شد بلند گفت رئیس منم
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/15310" target="_blank">📅 12:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15309">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B07PdT2OvqF0WW-Xs1lXpcwWwpoPmNlj4flyF4G8BfuJsgIRmH3grW9dzbnOCJkcmA7sMnXfXS3XCdk6Qw2wp7h4SaMt1lmG5goY21mbbyFFDA5YlJ_jRDZaFZ_l-xS25WZ6ZpbVdtdrRP9neWLpaAFMAsGWZ8nl92KKImnxdlivRJTVmXVl6yGTsR7WINVRGm2F0AoGmvnouRzaFJoX_U5yIOf9tj0eFg7bzdWLEXc4vX0LSn2RkXNDp9mktCYox6v_d170HAom8qoDG1x6FL7heRIFmn9ELwRyFWbEFg210zaPLcpIiRMyuhm4PNI_MSQ7-M4cmw1IkNGo_X5-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: ۳پا چندین سلول مخفی در عراق ایجاد کرده است تا حملاتی علیه کشورهای خلیج فارس که میزبان نیروهای آمریکایی هستند انجام دهد، که خارج از ساختارهای فرماندهی سنتی شبه‌نظامیان عمل می‌کنند تا خطر شناسایی کاهش یابد
سه تا چهار سلول، هر کدام متشکل از حدود ده مبارز شیعه عراقی نخبه، حداقل هفت حمله پهپادی بین ۲۰ آوریل تا ۱۷ مه علیه اهدافی در کویت، عربستان سعودی و… از محل‌های پرتاب نزدیک بصره و سماوه انجام دادند.
برخی اعضا از مقاومت اسلامی در عراق جذب شده‌اند، اما سلول‌های جدید مستقیماً به سپاه پاسداران گزارش می‌دهند نه به رهبری شبه‌نظامیان مستقر.
@withyashar</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/15309" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15308">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c913f668.mp4?token=nLArA8TCaSwXElcGcBUWVaY6xtGjGtPPcslM2geE3yN0ioFLg77o67_ypnn-a1yF1U5obe09VklIhpuUVzg7W-eJr5cypbYK2oNctofK7BlMT9qagEwHA6SWyQQJVBpItYJmea2hw7h8xOhpWfc7JBZclGQFtMzLIVHVrT_7K0m2Yr8GvNvITeu_luspiTNQP_9i-p_osxRXXptMYlYdGPkCfDfeGXVmMolLL8yCNZTj4P1u9zJa9Bgxe7me36s1sFtU9ymD16D7k-l8FZVMRrDWr-LTGsdofEXNi0jTlqEwL4uaTBNsbcGYjHsjXKUtRqOU0WXfiVnXyVl0TKJSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c913f668.mp4?token=nLArA8TCaSwXElcGcBUWVaY6xtGjGtPPcslM2geE3yN0ioFLg77o67_ypnn-a1yF1U5obe09VklIhpuUVzg7W-eJr5cypbYK2oNctofK7BlMT9qagEwHA6SWyQQJVBpItYJmea2hw7h8xOhpWfc7JBZclGQFtMzLIVHVrT_7K0m2Yr8GvNvITeu_luspiTNQP_9i-p_osxRXXptMYlYdGPkCfDfeGXVmMolLL8yCNZTj4P1u9zJa9Bgxe7me36s1sFtU9ymD16D7k-l8FZVMRrDWr-LTGsdofEXNi0jTlqEwL4uaTBNsbcGYjHsjXKUtRqOU0WXfiVnXyVl0TKJSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:حملات را یادتان هست؟ آنها وارد می‌شدند و بیرون می‌آمدند.ما وارد می‌شویم، نابود می‌کنیم و آنجا را ترک نمی‌کنیم. این کاری است که ما اکنون در لبنان انجام می‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/15308" target="_blank">📅 12:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15307">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuAfDZcMQKHGxbYegFrW7lk_ibgpxXKeglN4RY2ooklsOtOA7A07007paPIZPjDkvTE5Beo_J2w1-suq3_AC_kW1erTq4_1-KGXOZxscxffZMgHGjd6-7dKjV-VJUWhlEgnbO3q_IFNzDtbjAM1THeZSLXRvzrVSoXb07v48-Z5y7gfIDzQGasTFtugYyCrdf3GGDiMjGaOKq7QHfjwy-RGOlKQ3vHW11GtRglNSLzaarPBBxrbOhCHtDuOLpj3TkfzZftS_C64GGvDpVHsaYOXOzFQXLvvd34ICKGs2I4I4VwqCdD1rqrEnmipgLCnKantY_gr1ZBGibog2uPeJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات ارتش اسرائیل ساعاتی پیش در بعلبک، در عمق حدود ۸۵ کیلومتری در عمق لبنان. حمله‌ای غیرمعمول در عمق آن - ارتش اسرائیل در ماه‌های اخیر تقریباً در دره لبنان و منطقه بعلبک حمله نکرده است
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/15307" target="_blank">📅 12:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15306">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd1e599ede.mp4?token=UUC9s-ussMWLqEPE-SIr3iu5fg9kUvN6bMu9Blx2i4i9kFpTc-fETFjJ6ojVLpmy6SAQ-oLWfRWnD5Io2j6qaIbHvv9vqNUHMlDP3QgS7mTi3738RxMGF9uSGtg91ce0vCARePs0K9V0xjcPifPYGziijVQ9Peoa6xKvR8P8wTdBL8DKy4ld-euKPexDKHJG50tBFUM3XCbXHG-I9TqRasG8Us5wsH_XamXnvWWXcWlYQKM3snniD8FUlItKPDYXuQr80VxpwDc837VUGtc0KH5feXxbp5nkseJpPbw_RrJZCXAT7NE9WeXaCgyw8Ry1UOVqT-XHkucHG7HSuEFvfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd1e599ede.mp4?token=UUC9s-ussMWLqEPE-SIr3iu5fg9kUvN6bMu9Blx2i4i9kFpTc-fETFjJ6ojVLpmy6SAQ-oLWfRWnD5Io2j6qaIbHvv9vqNUHMlDP3QgS7mTi3738RxMGF9uSGtg91ce0vCARePs0K9V0xjcPifPYGziijVQ9Peoa6xKvR8P8wTdBL8DKy4ld-euKPexDKHJG50tBFUM3XCbXHG-I9TqRasG8Us5wsH_XamXnvWWXcWlYQKM3snniD8FUlItKPDYXuQr80VxpwDc837VUGtc0KH5feXxbp5nkseJpPbw_RrJZCXAT7NE9WeXaCgyw8Ry1UOVqT-XHkucHG7HSuEFvfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز، درباره لبنان:تمام خط اول روستاهای لبنان ویران شده است.ما در حال ویران کردن تمام خانه‌ها هستیم. ساکنان دیگر هرگز آنها را در مقابل چشمان خود نخواهند دید.
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/15306" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15305">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم. @withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/15305" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15304">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هم اکنون منابع لبنانی می‌گویند:
ستون‌های زرهی اسرائیلی در حال پیشروی به سمت نبطیه، پایتخت حزب‌الله در جنوب لبنان هستند و درگیری‌ها سنگینی گزارش می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/15304" target="_blank">📅 12:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15303">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575f785e69.mp4?token=bSEdfUcD0dRUfExkB22jBTbh4z1B_No3kJoyhV-zoCR5F3gR5NAeTkIZXBGIge5N2STni0rdr6zX-HH7d4NtfTOIOq93BhWis6gBL0bc5j2x_GnQ1SKroqjy1jMK85pwirQbMEmU9pQqJfb2joEwgbjFMThn3dXJkFQhPTJETrrSuGvVN818LlKFE1aOe6Zo_oAHYcaBopwEl9fbwvKhw7b8HbcffkD42TNPPatTzfskKaHGq9fCdU4ZNpS0IjWPdbQCkXjxYGcyltDp_GMf3xu5cQ5Ab34G1D0KwmHPymR5byweXY6hn2mUwngL8oGdfy5NAQ2In-U6P8UdG0VVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575f785e69.mp4?token=bSEdfUcD0dRUfExkB22jBTbh4z1B_No3kJoyhV-zoCR5F3gR5NAeTkIZXBGIge5N2STni0rdr6zX-HH7d4NtfTOIOq93BhWis6gBL0bc5j2x_GnQ1SKroqjy1jMK85pwirQbMEmU9pQqJfb2joEwgbjFMThn3dXJkFQhPTJETrrSuGvVN818LlKFE1aOe6Zo_oAHYcaBopwEl9fbwvKhw7b8HbcffkD42TNPPatTzfskKaHGq9fCdU4ZNpS0IjWPdbQCkXjxYGcyltDp_GMf3xu5cQ5Ab34G1D0KwmHPymR5byweXY6hn2mUwngL8oGdfy5NAQ2In-U6P8UdG0VVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم.
@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/15303" target="_blank">📅 11:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15302">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سوئیس رسما اعلام کرد: مذاکرات ایران و آمریکا برگزار نخواهد شد @withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/15302" target="_blank">📅 11:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15301">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دو حمله هوایی به لبنان
الجزیره از دو حمله هوایی اسرائیل به شهرک عین بورضای و حومه شهر بعلبک در منطقه البقاع در شرق لبنان خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/15301" target="_blank">📅 11:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15300">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1fHrfVI6CbeOV3bRgznb2B9cq0Ydvbnb690qkB6p6kR56i2sKKZ9KGW8FXm2zxFY-kH0qlIeKqZlViQ3gVplnl4ytsdFo-c0r5Xspbz2mopL9IRIEdE4_oGRn1hrwnud0AoPTDM2C8ddxbVv1EVmRpZJo_l_HPZ-ZVTALgJMp_sSo8OlxvcVvSomqfhr8CtB-f3Kfc7Rsz-edaBT1V8iKfLPJ_UpRldJkq0JG-wIH3M6rBxZuIoD1MS6g9PMxV4HLSycAd4rNPgM2SL1DPq8SgPSZrxymcDEJXBHNeZouGewsDDZESi-dl3RNj-aaTfI0D_CuuzvGRYpqpM0zpT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : یک ایده جدید:
دست از قلدربازی برای متحدانمان و چاپلوسی برای دشمنمان بردارید.
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/15300" target="_blank">📅 11:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15299">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سوئیس رسما اعلام کرد: مذاکرات ایران و آمریکا برگزار نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/15299" target="_blank">📅 11:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15298">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بن گویر وزیر امنیت اسراییل:به ازای هر اشک یک مادر اسرائیلی، هزار مادر لبنانی باید گریه کنند. کل لبنان باید بسوزد
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15298" target="_blank">📅 10:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15297">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TERpVbhLAOMYPHHYnHOhB57TDyThl7X18mI8Fgxr3UonjhN9BCJJ2uIlo32cLHPzgQfsWUjiMzT_9BYD6vO7ZZzzdmR1HJF-8Re6enU5V1_d06USk9dlkH6oeGruXyE_qMih8DS1JnCHAWQ1FQFWCqdcQfm2WXeARDEXUtZxMpjwSO1wDFChVXGcLm8oNS8WrMMxEjFtpoie_bTkawrkz3ZH026KBIVZhnaWEnFuchW47JhhhtTQFON3GrYy14CPQ1eDMDYOrG9e29uUp8-vHJ83T0TaHmMDwqoU2OXaQ9WQuzvACXoLyd4Yg3q8t2puCPkozLrgZu10ghp48hScqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لورا لومر خبرنگار نزدیک به ترامپ جاویدنام های دی ماه رو حدود ۱۰۰ هزار نفر اعلام کرد
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15297" target="_blank">📅 10:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15296">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602da85ed4.mp4?token=IcFR7EU3iUqeJ1fDnwxIngj9h5Hu-qTap5NYOFMfvTE4krPVVcL9mjdk-0CHVjNj9jBA18aWc9AInCMP56NrPD2HyqAe7xGevHEcC_W7UWZI0WOhOfeVSOMu83iZGXXKPBiRlTh-mydY2KaAUPsSJCaU5AwFABPv5a0CpjdlMMMwxXNuOu2FNKJfw1knd3jViWTDczDEdajFra14ohqWIhjbIGZDlRJIgAPh9jkEWDWJd0EqL9cFmEOlTU4mXueH4k6RTdZqtkIFBeJd-PAtyWHfvZdnAA-nkZoCsRrlW02xsbbf8vZy-sbMzZnaGiE-3SYD0AQv_CHSlkVIOZZgKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602da85ed4.mp4?token=IcFR7EU3iUqeJ1fDnwxIngj9h5Hu-qTap5NYOFMfvTE4krPVVcL9mjdk-0CHVjNj9jBA18aWc9AInCMP56NrPD2HyqAe7xGevHEcC_W7UWZI0WOhOfeVSOMu83iZGXXKPBiRlTh-mydY2KaAUPsSJCaU5AwFABPv5a0CpjdlMMMwxXNuOu2FNKJfw1knd3jViWTDczDEdajFra14ohqWIhjbIGZDlRJIgAPh9jkEWDWJd0EqL9cFmEOlTU4mXueH4k6RTdZqtkIFBeJd-PAtyWHfvZdnAA-nkZoCsRrlW02xsbbf8vZy-sbMzZnaGiE-3SYD0AQv_CHSlkVIOZZgKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری اکسیوس: در مورد نه تنها اعمال قدرت، بلکه محدودیت‌های قدرت خود به عنوان نتیجه از درگیری ایران چه آموخته‌اید؟
ترامپ: هیچ محدودیتی وجود ندارد. من هنوز آن درس را نیاموخته‌ام. می‌دانم که وجود دارند، اما می‌دانید، هیچ محدودیتی وجود ندارد. ما آن‌ها را کاملاً از نظر نظامی شکست دادیم
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15296" target="_blank">📅 10:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb0c5fe35.mp4?token=lzTz3TY3Elx4AoCQkh9sPpuv0MZPmbxjfdDj9LPdLZJR3ScTuTi14rTy58n7ZmGa_JMGdmZgYhTj85q1u32BkEnrlOUwV7kp17JI71n2w76Dae0bibTwQTsBBwPp4w20Xl6tPB52MODVsjwaFFh3CykFtIgDcNpyYvgWLzk8rtOUSZOD9l2Sz-6K0YSrpBd4NugOwHBdj07ud81fH0Du3ul3yYpQRwkANOh693Juvj_zCSyaxW375vGSfzwzRzBEgynGZMrPkZ4P1JEuKSqAywBNv7Av_er0wY7CO4AN-L6GTdr4m2snJhGsIVj2CjoFSpFIjJYWQRmej7eQZrvPDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb0c5fe35.mp4?token=lzTz3TY3Elx4AoCQkh9sPpuv0MZPmbxjfdDj9LPdLZJR3ScTuTi14rTy58n7ZmGa_JMGdmZgYhTj85q1u32BkEnrlOUwV7kp17JI71n2w76Dae0bibTwQTsBBwPp4w20Xl6tPB52MODVsjwaFFh3CykFtIgDcNpyYvgWLzk8rtOUSZOD9l2Sz-6K0YSrpBd4NugOwHBdj07ud81fH0Du3ul3yYpQRwkANOh693Juvj_zCSyaxW375vGSfzwzRzBEgynGZMrPkZ4P1JEuKSqAywBNv7Av_er0wY7CO4AN-L6GTdr4m2snJhGsIVj2CjoFSpFIjJYWQRmej7eQZrvPDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در آغاز درگیری ایران، شما صحبت کردید که فقط تسلیم بی‌قید و شرط را می‌خواهید. تفاهم‌نامه شبیه تسلیم بی‌قید و شرط به نظر نمی‌رسد.
ترامپ : واقعاً احتمالاً تسلیم بی‌قید و شرط است. من اینطور فکر می‌کنم
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/15294" target="_blank">📅 10:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزارت خارجه آمریکا: حزب‌الله باید خلع سلاح شود
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/15293" target="_blank">📅 10:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دلار داره آرامش قبل طوفان رو تجربه میکنه و ممکنه بزودی حرکت بزرگش رو آغاز کنه  رفقایی که نمیدونن دلار میریزه یا رشد میکنه عضو این کانال تحلیل بشن بهتون میگه:  https://t.me/+hLt81qXCGTQzOWQ0 https://t.me/+hLt81qXCGTQzOWQ0  لامصب اطلاعات رانتی داره</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/15292" target="_blank">📅 02:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دلار داره آرامش قبل طوفان رو تجربه میکنه و ممکنه بزودی حرکت بزرگش رو آغاز کنه
رفقایی که نمیدونن دلار میریزه یا رشد میکنه عضو این کانال تحلیل بشن بهتون میگه:
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0
لامصب اطلاعات رانتی داره</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/15291" target="_blank">📅 02:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش های محلی در جنوب لبنان،
از حملات هوایی سنگین جنگنده های اسرائیلی خبر می‌دهند،آسمان جنوب شرقی لبنان به دلیل شلیک گسترده منور های روشنایی ارتش اسرائیل روشن شده است.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/15290" target="_blank">📅 01:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، لاتیش کردم
😂
فقط همین کامنت رو لایک کنید . ترجمه در کانال تلگرام.  https://www.instagram.com/reel/DZvkK0jpILu/?comment_id=18367681780225433  ترجمه :    ببین ترامپ،  می‌دونم دیر یا زود این کار رو به سرانجام می‌رسونی، ولی رفیق، این…</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/15289" target="_blank">📅 01:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15288">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، لاتیش کردم
😂
فقط همین کامنت رو لایک کنید . ترجمه در کانال تلگرام.
https://www.instagram.com/reel/DZvkK0jpILu/?comment_id=18367681780225433
ترجمه :    ببین ترامپ،
می‌دونم دیر یا زود این کار رو به سرانجام می‌رسونی، ولی رفیق، این دیگه درست نیست. مردم ایران از این همه انتظار و بلاتکلیفی به مرز دیوانگی رسیده‌اند.
این داستان را تمام کن و کار را یکسره کن.
خیلی از ما در این ماجرا کنار تو هستیم، اما باور کن این آخرین تغییر رژیمی است که حاضر به حمایت از آن هستیم. بعد از این دیگر چنین چیزی تکرار نخواهد شد.
عشقی.</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/15288" target="_blank">📅 01:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15287">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزیر دفاع اسرائیل:اسرائیل توانایی انجام عملیات مستقل علیه ایران را دارد و در هر لحظه برای اجرای یک عملیات آبی و سفید در ایران آماده است.
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/15287" target="_blank">📅 01:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15286">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزیر دارایی اسرائیل، بزالئل سموتریچ:
غزه در ویرانه باقی خواهد ماند. در نهایت، مهاجرت رخ خواهد داد، زیرا در دهه‌های آینده چیزی برای جستجو در آنجا وجود نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/15286" target="_blank">📅 01:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15285">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: پیت هگست قراره خیلی پیروزی های دیگه بدست بیاره پسر خوبیه
من فقط مردمی رو دوس دارم که طرفدار من باشن
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/15285" target="_blank">📅 01:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15284">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این پست جنجالی را از دست ندید، کلیک کنید و کارهای اداریش را انجام بدهید. حتماً تا انتها ببینید.  https://www.instagram.com/reel/DZvdCMHxeYT/?igsh=MW50eDUzOWQ0MnFzYw==  اتاق جنگ با یاشار : Bagher.exe</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/15284" target="_blank">📅 00:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15283">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">subseven</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/15283" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15282">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15282" target="_blank">📅 00:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15281">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این پست جنجالی را از دست ندید، کلیک کنید و کارهای اداریش را انجام بدهید. حتماً تا انتها ببینید.
https://www.instagram.com/reel/DZvdCMHxeYT/?igsh=MW50eDUzOWQ0MnFzYw==
اتاق جنگ با یاشار : Bagher.exe</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/15281" target="_blank">📅 00:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15280">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBgs_SxSGv6S_VLQ_TG-NFd24lwQVF-4xGOnOvpw_qqxLPTW8n2QzM8P96-9jQo3sC-4hV_sHY8mXDBIj8DirLB-7yoMT5Da_LL2mmAM8gn0iJl_SWZF0C0FRixJSvLnQVxZwoY6WnhihNWBy2sIK29UhOb27IggbzCO4k-NKiuLr1qVBDEGr6Z1_3LfE5_fA5ob9kJ_HybCMxpgPQPHAmHvt1LTZVUfdobr7i011gAXBSnsh3esBldx4A9eeN4siUi4-ZeaimLB461CTCwDTCKfFCrfvUGTPTh_GnleRgU2CT3Hsfm0MXkDC4bYTaL4s9Ib2brqjkiiofH90wDylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/15280" target="_blank">📅 00:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15279">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزیر جنگ اسرائیل: قدرت ایران را درهم شکستیم، رهبران، دانشمندان هسته‌ای و زیرساخت‌ها را هدف قرار دادیم و برنامه هسته‌ای ایران را از بین بردیم؛ اکنون باید اطمینان حاصل کنیم که این برنامه دوباره احیا نشود
اسرائیل در هر لحظه برای عملیات مستقل در ایران آماده است
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/15279" target="_blank">📅 23:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15278">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">المیادین به نقل از منبع آگاه: هیئت مذاکره کننده ایرانی سفر خود به سوئیس را به دلیل تداوم حملات اسرائیل به جنوب لبنان متوقف می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/15278" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15277">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7NJSK8GWrdEfbq8uflhldA2t5n8jhWogc9C1TK6Wvv2P2EZoCNBSZNZC0NbGtwJhGn-zgy20pGX5lnZX7mtJa75g3gpQ-21OHHozJ-l54JZYIr53uP-tyaugXHhlQBSqK8XU6p-y_Zwib9jOUcS1YCXg_0pxiUOwH5Kgj8Ss2dj8gkuEYWgkbgLI1-j4E1dqssHTpiznDOZVBmG3tYeiwJYuOq1W1e-RHRpQcLdcP_0Dh_dujvI_Nb232nGIi7MFLQzSG1lBd499LGlnocD5MjR2Gf51_W0qjZ9ppFR2je9FnNna5nLib2sqTh7FCdCqAVAObuC9GZ7rHglLlMiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: ایالات متحده به صلح متعهد است و ما از همه در خاورمیانه می‌خواهیم که به تعهد خود برای پیشرفت عالی مذاکرات ما پایبند بمانند.
بازارها از آنچه اتفاق می‌افتد هیجان‌زده‌اند:قیمت نفت به شدت کاهش یافته و سهام به سرعت افزایش یافته است.
ما انتظار داریم آتش‌بس کامل در تمام جبهه‌ها، از جمله لبنان، «حزب‌الله» و اسرائیل برقرار شود. از توجه شما به این موضوع سپاسگزاریم!
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/15277" target="_blank">📅 23:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15276">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شورای عالی امنیت ملی:
بر اساس تفاهم‌نامه منعقد شده، تا ۶۰ روز هیچ‌گونه عوارضی از کشتی‌های عبوری از تنگه هرمز دریافت نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15276" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15275">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromyegi❤️</strong></div>
<div class="tg-text">به یزدان قسم فقط کانال خودتو میبینم و طبق تحلیل هات روانمو سالم نگهداشتم وگرنه با این توافق الکی که پیش اومده خودکشی میکردم
😮‍💨
دمت گرم
🤍
من به تغییر رژیم ایمان دارم و میدونم طبق گفته شما زمان بر هست پس صبر میکنم
پاینده ایران و جاویدشاه
👑
✌🏻
❤️</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/15275" target="_blank">📅 22:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15274">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آسوشیتدپرس: کاخ سفید توافق با ایران را به کنگره ارسال کرد
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/15274" target="_blank">📅 21:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15273">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فارس:  تیم مذاکره‌کننده ایران تا حصول اطمینان کامل از توقف حملات به لبنان، هرگونه گفت‌وگوی تکمیلی را به حالت تعلیق درآورد
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/15273" target="_blank">📅 21:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15272">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رهبری سیاسی اسرائیل به نیروهای دفاعی اسرائیل اجازه داده است که در داخل «خط زرد» در جنوب لبنان تیراندازی کنند.
انتظار می‌رود مقامات ارشد نظامی در ساعات آینده قوانین درگیری و راهنمایی‌های عملیاتی به فرماندهان میدانی را به‌روزرسانی کنند.
این تصمیم همچنین شامل برنامه‌هایی برای نابودی هر «زیرساخت مرتبط با حزب‌الله» است که در داخل «خط زرد» شناسایی شود.
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/15272" target="_blank">📅 21:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15271">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله به ایران و حزب الله آماده شوند
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/15271" target="_blank">📅 21:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15270">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKYJjVbUS7VkzGh5BLBrnJOI5o6OwhYTupw1Y7k8VBafXtVhZ2nMCZCjVvNn_A1TddjctZgkInRGPLNSw9vmugp-0y9IXVBNF78pxitpljVZ-T-RhAzQjWnUVQ9omz0NwIfTMg-eMSDCT4xxh-alRoT9naNhkw9ky8bTprPfTuRPr9HGQAJc0yaLQpvLsqtG5s6s9ql_COVbtDUdxyBg53GczzOpXpU6zSpqZ7qyoefJgY5-T386yhcqJ7zMmHOBEMoQi372Bvh2vMhDtyZADdQ2JOMrVv1nw8XbrfVfItiVgMuBOsvbL2ZacGlnbpcis3Itk0qCxO3JvfTdBdAhYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس:  پیام جدید  iRahbar
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/15270" target="_blank">📅 21:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15269">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/15269" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15268">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnTdbbl9gOiHESsMeyCNy7w7-ItFqug2w2CuOYKhUPWO1qFcFCof9wuFtt4DWNQnEboBIkyxtpNgRtD54jfmpzpEluwG98X_e0bFMWnehQYNKYGBGE_OGY0L93YZcXG5rxWEWlGaU2Cz6EsT65ftUznh7gwxL0Vb_QPINXiEuoHPCOq1lPJT72vQG03rE5Soz3p2C7Wzd4NmDKXUY3XgmA5vGcsltwV9fgI-U3sKq72MmACOpXlk6cjHjvAcG_aGZVwi56ocjPwPuYtIXAfiuFKRVTbqld23Oi8a3HyXYFSlugUcZG823HavrlOCCvouu5ODT7DIs-uzCjwYJxO3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : هیچ پرداخت ۳۰۰میلیارد دلاری از سوی آمریکا به ایران در کار نیست.
این خبر جعلی است!
تنها چیزی که نصیب آمریکا شده، موفقیت، کاهش قیمت نفت و پیروزی است.
بازار سهام را ببینید.
تبلیغات «دُمکرات‌ها» در جریان است!!
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/15268" target="_blank">📅 20:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15267">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/15267" target="_blank">📅 20:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15266">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCVqyFcdnd_ZLhvwgntfdUnpGv_Dstk94q_Wm8kTxR_edj3HofpGqnfbCygqXW-PtSKIuTnpY5oOiTNKFWr-On6Hfy0GzNXY0CghuWPibzDAeh184NIBx5zwJFEBGLN0DMrG-by-6-qDnqUYKD8IlvoJCLIm095riqtDOnBBiWFQBSxPBxFoE3BavzVicghvgDroABg9o0yPBrVxQG3rCPw0elbhYilCF0Qm7MqAnacY1l9XiUXLOImG4PVwvoRBINdAdMBr7w8s410K0R04JHmbw-Hfl6nEcAhxFuUhs0pcMnBeLb-umJxpkCFn1kyr0edcF6FRHJJvgPraRdfHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نیروهای ایالات متحده، بنا بر دستور رئیس‌جمهور، محاصره تمامی رفت‌وآمدهای دریایی به بنادر و مناطق ساحلی ایران و از آن‌ها را لغو کردند.
نیروهای آمریکایی دیگر مانع تردد کشتی‌ها به مقصد بنادر ایران یا خروج از آن‌ها در خلیج فارس و دریای عمان نمی‌شوند. تمامی اقدامات نظامی آمریکا برای اجرای این محاصره متوقف شده است.
ناوهای جنگی ما همچنان در منطقه حضور خواهند داشت تا اطمینان حاصل شود که همه مفاد این توافق به‌طور کامل رعایت و اجرا می‌شود و از قدرت و اعتبار کامل برخوردار است.
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15266" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15265">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ونس درباره نتانیاهو: من گزارش آکسیوس را دیدم که می‌گوید نتانیاهو عصبانی است.این بازتابی از گفتگوهایی که من با او داشته‌ام نیست. شاید او چیزی به شخص دیگری می‌گوید که به من نمی‌گوید.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/15265" target="_blank">📅 20:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15264">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a543e5cc9e.mp4?token=ASvT3SBfts0bRldldDSJLkb-ZvaESqJMpp0q1fYQWEUGRFmqk2VmPWAYTDkCfHDB8vpgHjkTpqe9chxfnvk6u9hIf1jHdFJJoqsORa1eNVuoPdy6aSw3dmhONMIisC7Wp8NNZM9TE8fnApia5LUAKZTOIKrlMDuyL5VrzM9Q3DpDIq9FIwHm0SA_-G340Hl9GwWBNg3Aldkf10uh_eshjHunRhkIH-V7gn_a7sYJWCt4z8ws5ABSATcfE67RLHOWRLwyzhsnxVhrttg--ZFmfFQ56cx5c1R1A6fWbEM0-Gume4_JH8OBeIu5zdRDDFVbtPtjpLR-K30PYDR7M8SEHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a543e5cc9e.mp4?token=ASvT3SBfts0bRldldDSJLkb-ZvaESqJMpp0q1fYQWEUGRFmqk2VmPWAYTDkCfHDB8vpgHjkTpqe9chxfnvk6u9hIf1jHdFJJoqsORa1eNVuoPdy6aSw3dmhONMIisC7Wp8NNZM9TE8fnApia5LUAKZTOIKrlMDuyL5VrzM9Q3DpDIq9FIwHm0SA_-G340Hl9GwWBNg3Aldkf10uh_eshjHunRhkIH-V7gn_a7sYJWCt4z8ws5ABSATcfE67RLHOWRLwyzhsnxVhrttg--ZFmfFQ56cx5c1R1A6fWbEM0-Gume4_JH8OBeIu5zdRDDFVbtPtjpLR-K30PYDR7M8SEHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی.دی. ونس در مورد لغو تحریم‌ها:
«راستش را بخواهید، ما این را یک امتیاز بزرگ به ایرانی‌ها ندیدیم — ایران هم... این را به‌عنوان یک امتیاز برای خودشان تلقی نکرد، چون چیزی که مانع فروش نفت آنها می‌شد، تحریم‌ها نبود.
آنها بدون هیچ تخفیفی نفت زیادی می‌فروختند، چون تحریم‌ها اساساً ناکارآمد بودند.
در آن مرحله، کاری که تحریم‌ها کردند این بود که سیستم مالی ایران را به نوعی به سمت سیستم بانکی سایه‌ای (غیررسمی) سوق دادند.
با لغو تحریم‌ها، در واقع خواهیم توانست کمی ببینیم که سیستم مالی آنها پول را به کجا می‌فرستد و از کجا پول دریافت می‌کند. این یک مزیت واقعی است.»
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/15264" target="_blank">📅 19:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15263">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9L8BbTYSSXwqcqNS2FhbToiMo01kQQCPacfRikJvKaqvGol4DSDRSzR6V1ZHF-8gzXxuyWhQSuazamrQU9PvZKBDd9bZjwvG6F-eaNXylp8QcCvOidpSLwNXOHj3f6qg6RQLlqG-h31_S9nwxFs9W8ynvJ3DbZn89ncYcM8crK3RKusPWTZjIyx3MM4zRW1wqKNTQiq-UAw7lWxt4aCXZHw1PljgM8CxHvwNoKhKxjFT70-hAsa5Vj1qCRyUBSSIPmfQMTXwKwIW89U1n4CT8ojekYxlTCxRTN64mPlwhWLTp35wrOc6E4X26C94EEAoG2U5aFw1dZyJEKPmeuUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ترامپی که امضاش اینهمه بالا پایین داره انتظار ثبات روانی دارید ، موج مکزیکی هم رد کرده نوار قلبه
😂
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15263" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15262">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ونس: اگر ایرانی‌ها رفتار خود را تغییر ندهند، ارتش و برنامه هسته‌ای آنها همچنان نابود خواهد شد.
ما در حال حاضر یک تحریم اقتصادی فلج‌کننده علیه ایران اعمال می‌کنیم و تا زمانی که این کشور رفتار خود را به‌طور اساسی تغییر ندهد، به آن پایان نخواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15262" target="_blank">📅 19:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15261">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آمریکا حتی یک سنت هم به ایران نمی‌دهد
جی‌دی ونس: "آنچه از همه شما می‌خواهم این است که صادقانه گزارش دهید که ایالات متحده حتی یک سنت هم به ایران نمی‌دهد...حتی مزایای اقتصادی، کاهش تحریم‌ها و غیره که با این معامله همراه است، فقط در صورتی اتفاق می‌افتد که ایرانی‌ها عمل کنند!"
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15261" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15260">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">معاون رئیس جمهور آمریکا: دوره ۶۰ روزه مندرج در یادداشت تفاهم با ایران از امروز آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/15260" target="_blank">📅 19:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15259">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/15259" target="_blank">📅 18:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15258">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ایهود باراک، نخست‌وزیر سابق اسرائیل:
احتمالا نتانیاهو در آستانه انتخابات، به لبنان حمله خواهد کرد، و در تلاش است یک جنگ ابدی را با ایران و حزب‌الله آغاز کند
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15258" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15257">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ایرنا: ایران به پاکستان اطلاع داده است دیگر نیازی به برگزاری جلسه حضوری در سوئیس نیست.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/15257" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15256">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubUeRmTwwlnN2aJrIb6Kr_1gnHmO6NB2NyWGG11zhQPsoVXAD2ta6vAqHDO-kbTlH_9MvSfMNnF_x5XdKkucF6XWNJj1oZ9K0rU4ejbqFYzVDIq0dNYqsDZBOJXRwuAmCHQWJZSSdn-ZN0v_X5co57G1WrVAMD8POWuWXTuY37q5fmyCn18_-asO-A5pf_MsqRQqBXLVU4PKbjaK1_FIiOKSQ01syktwnPFarK09YdX4ANha4fkzyBzb1FeKXWyRplJ5PIM5kzRWrxUBRy3vlHI2SzFS8euyuXOcQIp2kfoOozu4LY7YZBJ4p5dWhnWE3Ae2xSiUTpiIi1_yyCDgEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نفت در حال جریان است، ایران هرگز نباید سلاح هسته‌ای داشته باشد (جهان امن‌تر خواهد بود!)، بازارهای بورس با قدرت در حال رشدند، اشتغال به رکورد رسیده، و قیمت‌ها در حال کاهش‌اند (امکان خرید بیشتر شده!). کشور ما قوی، امن و محترم‌تر از هر زمان دیگری است. “خواهش می‌کنم!
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15256" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15255">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تلویزیون پاکستان:
سفر برنامه‌ریزی شده نخست وزیر شهباز شریف به سوئیس بدون ذکر دلیل لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/15255" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15254">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">از صبح حملات اسرائیل به جنوب لبنان پر قدرت ادامه دارن
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/15254" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15253">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3483473645.mp4?token=Feq8ViYd9_ITJVKKbKaRVA5iSDkno2w7cBMVDKNdpDE2iE0CfBL_1A8qOF3N_paGbYXD49VFebm0quFsV5xTMzRSsBv0mdzlCzTZJdE43_mchbZyVlD4RH51jpyxW-leJbc0VxasIDAfb2sOhXq0HjXJPehIzbwu33BGohCVqLPydw8dHnk-GCCUFUHp0F3zIuvRI-XcX345vnyqGsx0LXWVRj5cjErqLZC-UMW7nAzlV5WbI5UWEb5Bibmo-SXX0zYzYM2Wmar7-G_TwVUk4txWXBY2KtrqqfggoZdQYCi25BbqZeFlDTSrO1kb5z3aYjXKsNvm8TgQvS4mqaYRfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3483473645.mp4?token=Feq8ViYd9_ITJVKKbKaRVA5iSDkno2w7cBMVDKNdpDE2iE0CfBL_1A8qOF3N_paGbYXD49VFebm0quFsV5xTMzRSsBv0mdzlCzTZJdE43_mchbZyVlD4RH51jpyxW-leJbc0VxasIDAfb2sOhXq0HjXJPehIzbwu33BGohCVqLPydw8dHnk-GCCUFUHp0F3zIuvRI-XcX345vnyqGsx0LXWVRj5cjErqLZC-UMW7nAzlV5WbI5UWEb5Bibmo-SXX0zYzYM2Wmar7-G_TwVUk4txWXBY2KtrqqfggoZdQYCi25BbqZeFlDTSrO1kb5z3aYjXKsNvm8TgQvS4mqaYRfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز شبکه پویای صداوسیما اومده و یه برنامه کودک در مورد توافق کردن و سازگاری گذاشته که تندرو ها به شدت عصبی شدن
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/15253" target="_blank">📅 16:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15252">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ4ktO0y3Ojg4UiNPdgzVrkOB9wYlrKtOogRH2NS-8XiS8M_Fj8ZBaDBTY5TBXBQjrJLVCChK_GVp3msA-tjz0OphDSBONuiKKuPepFhNNpisR7MPgLYRygRzsS4tsuaeYIPb_xIbubHM2ZGMy6H1S746nmwC295O1gYdrNWvAYeTi_uti8KPG-aC-nAfBOP0ENA6DBIY9xGjybhPeye4X5pMFwqBpZQtyqBcVHDXybl7-syXrI5qMdpZur1ZTeLxmOQAgc6pilpc7izW_s5vDcmxyeMI4D7GOwnF6vW8hvlqQIigTAMGw65N-powxoKaKn0ChE6MWEyn6mp0IhTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : پاپ لئو از توافق صلح آمریکا و ایران تمجید کرد
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15252" target="_blank">📅 16:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15251">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">محمد محبی فوتبالیست تیم جمهوری اسلامی که در خوشحالی زدن گل به تیم نیوزلند، به مردم شلیک کرد، رفته و عکس مهسا امینی رو کنده و انداخته توی سطل زباله... @withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15251" target="_blank">📅 16:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15250">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15250" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15249">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آموزش و پرورش
: ثبت‌نام برای ترمیم نمرات تا پایان هفته جاری امکان‌پذیر خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/15249" target="_blank">📅 15:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15248">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=OLGiCtqg3jO5lDCw5A09a_N-NenBLkiQx3m-G0rEpKKQf4c2ihLXNKcAkDZ47iHI9fIiQp2wvBTY-hS4uAnfE9MWDhmy_7fTRDRGCPshLE0Lr3OIiZpn9rQraB-HwuUDQFKYroKCsoYvocT79ixkv4i5cOsS5HpwMgAbxDDyU2vXZVhsv4yB4NxyT3a8hANKHxANzQCHBRDMlAreoUFCC8AsbQJ-q40ggzTiTEWonWa6jDXlLueQlAw2EpfyLfV7C0mHkO0QzMpITC0lOeSUo3mOa7fAVwRq9TsNQnnxNZrR9OmPYF9vfero3V3SK3FMDSvXQcV-vg-eA7XboC6Cwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=OLGiCtqg3jO5lDCw5A09a_N-NenBLkiQx3m-G0rEpKKQf4c2ihLXNKcAkDZ47iHI9fIiQp2wvBTY-hS4uAnfE9MWDhmy_7fTRDRGCPshLE0Lr3OIiZpn9rQraB-HwuUDQFKYroKCsoYvocT79ixkv4i5cOsS5HpwMgAbxDDyU2vXZVhsv4yB4NxyT3a8hANKHxANzQCHBRDMlAreoUFCC8AsbQJ-q40ggzTiTEWonWa6jDXlLueQlAw2EpfyLfV7C0mHkO0QzMpITC0lOeSUo3mOa7fAVwRq9TsNQnnxNZrR9OmPYF9vfero3V3SK3FMDSvXQcV-vg-eA7XboC6Cwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درست خوندم؟ Porngraph?</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/15248" target="_blank">📅 15:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15247">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirAbbas</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd2kM-S65O5AtmirliAdgbn3__4A5TmuCUVKWuUIeJobf5dJvrCVk_6YyWvekIafTYMnT5OqMA8PcaU5ZprOZz0e3ud0KDHHAddTNMXWnZheCTRo-DPdVhvODUsMiJIQtd21yFgnq8qdhX453JyfSt-8rBiXAIMDrsra4680N5CnjNk-Bk-ZzbiUylZU5qMvmbtjtvCyJus0BdaDdnJAEZ6h6yQh5mhsTwXPQZ6cE3AyLwReimzQMUDEtdYec6_bh3fIxU98wdw8Fk13IEglzgPNCsvXlCtzyZkWrF0hGXlmNixjZuCQ9ZvkXB-7KVk4adOdagcj2r4x_GX1wDayFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درست خوندم؟
Porngraph?</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/15247" target="_blank">📅 15:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15246">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/15246" target="_blank">📅 15:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15245">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شبکه کان اسرائیل: موضوع عقب‌نشینی از لبنان هفته آینده با هیئت لبنانی در واشنگتن مورد بررسی قرار خواهد گرفت
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/15245" target="_blank">📅 15:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15244">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرگزاری CNN : نتانیاهو معتقده توافقی حاصل نمیشه و جمهوری اسلامی با پایان دادن به موضوع هسته‌ای موافقت نمیکنه
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/15244" target="_blank">📅 15:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4YiJkQeSRMBC_KtL1W8Wo1IcdB-2EjdgyCIHy7fUGseikMyyl1prQ3j-itXMN78C0SQ0DGdNDTMHVhW_yo1PWrG0hdJZfOghFIug-7XpjYXcbM5IpR7KVzUE1V-Us2qApCB5eAiZjHS8qJx4jGH9v3dPRLfzk_V3q1yc--mfhc51d2t7xqPbyoOPrIrMEF7pKEP77yiPsUpEK1d9AHt4it--4P1snL2WJRU1kxvHac88t8c3_7yX-vCY2uUEbV32uNb1a166xq-31Y5XW8gX1-8-V4z_0Uwm2b_srmZODKZWMbDvy1Feu9XEmrKZmSd6k1VPTLz1ttPAE4MvCXh1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRhN-uLoqOS1et-EeVAWcc55S41irOAsBq1DQlY0Knx1ltc5RkRGB541NPQ_ZG8tD9NM86ixCCyu1Jj0MJWS_i40Ih2kUvM3g2awc1frjHrBEjbrq4nw9nEaqLNDqoOw4ArHUKWPOnRfDjBmurRtfOA6Nm8nRP4dthqb3I6-vfBCFrZHapfiYwMLZA5svOGdTXfiXvw6CFIS1kZfjoITOcidC0_CurCt2r6rJ5XT0cTGwFBrietSAcKCIoGoAIVnma5xKN9zWTap_cDucYsdxdxKMa2E5Tf-RhlLwcFWHxDVtuHsx29uAN-JJwvspaU244T9iP0tNUU19odx6zd2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BINc9vYDuHEhLs2Zo-GB5GTvtwBg_2sFBRWOJdPnrDsKvPGwe5MKiXHeFEoXY4ywY5c6Z2Ctth_6vM6GIG06ilHaJu3Kqo9UOvaEtiEgmy_Fj0WeCRYRE2CeXyLDx0yO-glartGga-7-1oHiFQT-6hFaEhv0E2aZn-4MCdSIwLNAyNPrhMYWu-_qRph5uxy0NKQXzqM4hKmE5kuSsAaGo1f46BclL8PVzHu9s5NqaioRWhRxwmTV7km96Ul-LQ3tPeUOERr7QQCuHe2MZ1K87UM8_1YsRZKa7udsIYEzZr1qIh3n8FJeXNBPj6DZuM-vJ79d5umziZkBQvgWvHaPpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکان نسخه اصل سند امضاشده را منتشر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/15241" target="_blank">📅 15:11 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
