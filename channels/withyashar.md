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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 17:23:16</div>
<hr>

<div class="tg-post" id="msg-15337">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">از زمان آغاز آتش‌بس، نیروی هوایی اسرائیل بیش از ۱۱ حمله هوایی در سراسر جنوب لبنان انجام داده است.
@withyashar</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/withyashar/15337" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15336">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک مقام ارشد در کاخ سفید به آکسیوس:
«نتانیاهو با تمدید آتش‌بس در لبنان صد درصد موافقت کرده است.»
@withyashar</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/withyashar/15336" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15335">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حزب‌الله: هنوز هیچ اطلاعیه‌ای درباره زمان آتش‌بس دریافت نشده است
@withyashar</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/15335" target="_blank">📅 17:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15334">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کانال ۱۲ به نقل از یک مقام ارشد اسرائیلی: آتش‌بس به ما این امکان را می‌دهد که به تخریب زیرساخت‌ها و اقدام علیه تهدیدها ادامه دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/withyashar/15334" target="_blank">📅 16:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15333">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرنگار المیادین در جنوب لبنان: همزمان با اجرایی شدن آتش‌بس ، حملهٔ هوایی اسرائیل به النبطیه صورت گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/15333" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15332">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">باراک راوید از آکسیوس: یک مقام ارشد آمریکایی به من می‌گوید
اسرائیل و حزب‌الله بر سر آتش‌بس مجدد در لبنان از ساعت ۴ بعد از ظهر امروز به وقت محلی توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر و پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/withyashar/15332" target="_blank">📅 16:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15331">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش ها مبنی بر آتش‌بس بین اسرائیل و حزب‌الله هم اکنون به اجرا درآمده است
@withyashar</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/withyashar/15331" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15330">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWI3_URizy64ZVI07XpvWliKxLR0Ggto-kzwQIFy5nKPit9RnuwtGIxnF_DJXy8HunEnMt89UyDpo4N_JCwp6uV8L013XssZB6kvfgRWHssN51WWjyhJx6eHfC9jpMqvvoXegmbj4dZ-PGV6Gu9r50I-xUyZbvXfqBnWOqSE6BjJvVwBsFdk93WualJ9AkFkl88z4pvOsXjA0_Z7r2Mte6_CGTtuOiwjVbj5O2tZD7Os2cQQRYXEulLtNpBxhuMmITfyL8ncfpVncA5YpzE6gEM5WzSyLfHbrSddEpJV2PbLeyL1RIfiQt8R4JPlnEdsO_QrPuG3naSHro92XLWUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از یک مقام آمریکایی ادعا کرد:
«حزب‌الله و اسرائیل با آتش‌بس موافقت کرده‌اند» و افزود که مذاکره‌کنندگان از آمریکا و قطر با حمایت ایران به توافق کمک کردند.
@withyashar</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/withyashar/15330" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15329">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7oEgEysSkE-oNE6DDCHFL5oYHtIwuXoboMVWBjTSUxxpcrk9Rs9GgRBRXUgNEWWdq70_Gdn4WsdDJn0roa5LERsqhJIzN47HEvUfgcs2_rN4Jh9QJOK79bSyPAwMVFBvgELkFQSonPj3q_i7grY9A1SLLTVASRDNoN5CpXdQNCZ60x21hnBSuLD1Xau0kzstDKXwLYDufaQWVmlymZGJHUvzpv8aqaKaqCWBY60_Bnf-gVBGwisEq11DGxWnaBiN_Tx0SlMuPg6TsRj588qvPvncb47bt-5oTk1cOS5vCAMOGkYNPacIHh0MqUVWeQ7yEr6V_MBsf_WKlA95k4KcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : ما از روی استیصال نرفتیم سراغ مذاکره
این ایران بود که بهش نیاز داشت، کارشون تمومه!
همون ۶۰ روزی که گفته بودیم رو جلو می‌بریم، هیچ پولی هم گیرشون نمیاد
@withyashar</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/15329" target="_blank">📅 16:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15328">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5PInIuhAf-ppET1BAybZ9ML0ZXdmfmzI0g8uqT68cPjPSyJOnU1KNTZkGak7rqe52gmq-w3U9WkCSxbwhSdPWIog_smXa5tKhfXmiSJEpiY57jWQPQy7DrrA0_k-OrqW6knFtc4H2iX24IaXeU5wx1Ph7z-hsUUn3aLmSOfERJBbifHkOaAhg4XUPW6kjCoaFFQLqItujSWLPvFM9sirI8jnxkTPxO16Dzr8IYh14N6apmFiiEHlFOYi8VyjrmHglwIfCgyWuy0ooofqKsKZ1CL_z_rlexSlRH5HaGknn6n4NH0vlsEwHW7zIoVVVD9UyUPXqvhtP7M_YW7q_VGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ در‌تروث : جنگ ایران را تضعیف کرده و دیگر نیروی هوایی، نیروی دریایی، پدافند هوایی، رادار یا تقریبا هیچ‌چیز دیگری ندارد؛ با این حال دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش در وضعیت بهتری قرار دارد. باور می‌کنید بتوان چنین حرفی زد؟ بعضی افراد چقدر می‌توانند احمق باشند؟
@withyashar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/15328" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15327">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سنتكام: جنگنده‌های اف-۱۶ به گشت‌زنی‌های خود در خاورمیانه ادامه می‌دهند و آماده مداخله هستند.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/15327" target="_blank">📅 16:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15326">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">طالبان استفاده از گوشی‌های هوشمند رو برای تمامی کارکنان نظامی و غیرنظامی خودشون ممنوع کرد!
@withyashar</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/withyashar/15326" target="_blank">📅 15:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15325">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f67ff589.mp4?token=aV01hN8PpIKjr9Ai6IB-xYvpANd4Q3XdolJfB73Bn405dkGoIl1mXbJCMIVq39vtwxDuWpnneh3Hvsjt0FxCPvOI5Vi3bj334-vehRGpIB7GsQ-LgVP8cet0eteohv0MZcZdm4d75aPL__uIwIIyk9TIEp_CWij7d-_F7yhcH1Opx3E9s1623v3wx89Uf0TFA14ylyIxDHSzRqqGc9AnNsq5Rmts5Aw_8YoFdmBNyhc2lJOBDSt9vDqFsMFK6QwBwwdQ4_rLittI-LXFES4KzvWhOAct9xAQ969KnRE8F-6SWJPO-OrIyH8OKP96fT2hJRiJ2qENc80s5vZVIND1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f67ff589.mp4?token=aV01hN8PpIKjr9Ai6IB-xYvpANd4Q3XdolJfB73Bn405dkGoIl1mXbJCMIVq39vtwxDuWpnneh3Hvsjt0FxCPvOI5Vi3bj334-vehRGpIB7GsQ-LgVP8cet0eteohv0MZcZdm4d75aPL__uIwIIyk9TIEp_CWij7d-_F7yhcH1Opx3E9s1623v3wx89Uf0TFA14ylyIxDHSzRqqGc9AnNsq5Rmts5Aw_8YoFdmBNyhc2lJOBDSt9vDqFsMFK6QwBwwdQ4_rLittI-LXFES4KzvWhOAct9xAQ969KnRE8F-6SWJPO-OrIyH8OKP96fT2hJRiJ2qENc80s5vZVIND1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاهره و بیروت ما داریم میایییییم
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/15325" target="_blank">📅 15:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15324">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تحلیلگر ارشد و رئیس کل ستاد مشترک ارتش اتاق جنگ ، سر ادمیرال یاشار : مسیر قاهره از بیروت میگذرد @withyashar
🎖️</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/15324" target="_blank">📅 14:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15323">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرنگار العربیه در سوئیس: مذاکرات بین آمریکا و ایران ظرف چند روز آینده آغاز می شود
@withyashar</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/15323" target="_blank">📅 14:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15322">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ به طور هیستریک عصبی به ثانیه در تروث در حال پست گذاشتن است. خواهیم دید چه خواهد گفت.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/15322" target="_blank">📅 14:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15321">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تحلیلگر ارشد و رئیس کل ستاد مشترک ارتش اتاق جنگ ، سر ادمیرال یاشار : مسیر قاهره از بیروت میگذرد
@withyashar
🎖️</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/15321" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الجزیره : نتانیاهو: حزب‌الله بهای بسیار سنگینی خواهد پرداخت
نتانیاهو افزود به ارتش دستور داده است در واکنش به «نقض آتش‌بس» ضربات شدیدی به حزب‌الله وارد کند.
همچنین ، ارتش اسرائیل حدود ۸۰ هدف متعلق به حزب‌الله را هدف قرار داده و «ده‌ها عضو» این گروه را به هااکت رسانده است. همچنین امروز یک مقر فرماندهی حزب‌الله در منطقه بقاع هدف حمله قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/15320" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15319">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مشاور هیئت مذاکره‌کننده ایرانی، مرندی: نظام ترامپ به توافق پایبند نیست. و ایران در این شرایط یادداشت تفاهم را اجرا نخواهد کرد. اقتصاد آمریکا در معرض فروپاشی است و اسرائیل مجازات خواهد شد. @withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/15319" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15318">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیروی دریای سپاه در بیسیم کانال ۱۶ دریایی: “از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15318" target="_blank">📅 14:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15317">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارش‌ها از شلیک مدام قایق‌های سپاه در تنگه هرمز حکایت دارد.
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15317" target="_blank">📅 13:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">باز‌ تنگه دعوا شد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15316" target="_blank">📅 13:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15315">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دقایقی پیش براساس گزارش مستقیم از چند کشتی در خلیج فارس، سپاه پاسداران حرکت تمام کشتی‌ها رو متوقف کرد و عملاً تنگه هرمز رو بست.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/15315" target="_blank">📅 13:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15314">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزیر امور خارجه پاکستان: علت آغاز نشدن مذاکرات سوئیس به دغدغه مقامات ایرانی به مراسم ماه محرم مربوط میشه.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15314" target="_blank">📅 13:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15313">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مشاور هیئت مذاکره‌کننده ایرانی، مرندی:
نظام ترامپ به توافق پایبند نیست. و ایران در این شرایط یادداشت تفاهم را اجرا نخواهد کرد. اقتصاد آمریکا در معرض فروپاشی است و اسرائیل مجازات خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/15313" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15312">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شبکه CNN به نقل از منابع آگاه اعلام کرد که پیش شرط ایران برای شروع مذاکرات در سوئیس توقف درگیری‌ها در لبنان است
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15312" target="_blank">📅 13:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15311">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/15311" target="_blank">📅 13:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15310">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bffa7007.mp4?token=bqI7-R2sEvzDtz4BZcvDQdBeOQFikrg88ad1gwUnuO4sijRc_3cu6zWD9H4bKKmCAZFwUMj9q3sbO237MW3A7RXsSl4tRjxoMxjzXBqUqz0N8nNa5ypCKzm1DPIrbOLezqMBuy-B8f98sQq5RFn69D4XhRMO-krlclfAv5ZWWvTxZ7V1W0-SOLzya_DxD7N5K310KUHQY71k-nlIeoQcPIrx5nc9Iiw9IM9PsGS04ka3minzP80RaX2890KKPkFKrVPZvS8o0uQvKWtAzLPlyWSjTVTBgj8IKzUUmGp5vWMpr0D6yDJvcqMGiNenJHIgyTmDl1HnwL3ju1W6TAS7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bffa7007.mp4?token=bqI7-R2sEvzDtz4BZcvDQdBeOQFikrg88ad1gwUnuO4sijRc_3cu6zWD9H4bKKmCAZFwUMj9q3sbO237MW3A7RXsSl4tRjxoMxjzXBqUqz0N8nNa5ypCKzm1DPIrbOLezqMBuy-B8f98sQq5RFn69D4XhRMO-krlclfAv5ZWWvTxZ7V1W0-SOLzya_DxD7N5K310KUHQY71k-nlIeoQcPIrx5nc9Iiw9IM9PsGS04ka3minzP80RaX2890KKPkFKrVPZvS8o0uQvKWtAzLPlyWSjTVTBgj8IKzUUmGp5vWMpr0D6yDJvcqMGiNenJHIgyTmDl1HnwL3ju1W6TAS7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حساب رسمی‌کاخ سفید: دیروز ترامپ تو نشست سران جی7 وقتی وارد شد بلند گفت رئیس منم
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/15310" target="_blank">📅 12:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15309">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B07PdT2OvqF0WW-Xs1lXpcwWwpoPmNlj4flyF4G8BfuJsgIRmH3grW9dzbnOCJkcmA7sMnXfXS3XCdk6Qw2wp7h4SaMt1lmG5goY21mbbyFFDA5YlJ_jRDZaFZ_l-xS25WZ6ZpbVdtdrRP9neWLpaAFMAsGWZ8nl92KKImnxdlivRJTVmXVl6yGTsR7WINVRGm2F0AoGmvnouRzaFJoX_U5yIOf9tj0eFg7bzdWLEXc4vX0LSn2RkXNDp9mktCYox6v_d170HAom8qoDG1x6FL7heRIFmn9ELwRyFWbEFg210zaPLcpIiRMyuhm4PNI_MSQ7-M4cmw1IkNGo_X5-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: ۳پا چندین سلول مخفی در عراق ایجاد کرده است تا حملاتی علیه کشورهای خلیج فارس که میزبان نیروهای آمریکایی هستند انجام دهد، که خارج از ساختارهای فرماندهی سنتی شبه‌نظامیان عمل می‌کنند تا خطر شناسایی کاهش یابد
سه تا چهار سلول، هر کدام متشکل از حدود ده مبارز شیعه عراقی نخبه، حداقل هفت حمله پهپادی بین ۲۰ آوریل تا ۱۷ مه علیه اهدافی در کویت، عربستان سعودی و… از محل‌های پرتاب نزدیک بصره و سماوه انجام دادند.
برخی اعضا از مقاومت اسلامی در عراق جذب شده‌اند، اما سلول‌های جدید مستقیماً به سپاه پاسداران گزارش می‌دهند نه به رهبری شبه‌نظامیان مستقر.
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/15309" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15308">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c913f668.mp4?token=nLArA8TCaSwXElcGcBUWVaY6xtGjGtPPcslM2geE3yN0ioFLg77o67_ypnn-a1yF1U5obe09VklIhpuUVzg7W-eJr5cypbYK2oNctofK7BlMT9qagEwHA6SWyQQJVBpItYJmea2hw7h8xOhpWfc7JBZclGQFtMzLIVHVrT_7K0m2Yr8GvNvITeu_luspiTNQP_9i-p_osxRXXptMYlYdGPkCfDfeGXVmMolLL8yCNZTj4P1u9zJa9Bgxe7me36s1sFtU9ymD16D7k-l8FZVMRrDWr-LTGsdofEXNi0jTlqEwL4uaTBNsbcGYjHsjXKUtRqOU0WXfiVnXyVl0TKJSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c913f668.mp4?token=nLArA8TCaSwXElcGcBUWVaY6xtGjGtPPcslM2geE3yN0ioFLg77o67_ypnn-a1yF1U5obe09VklIhpuUVzg7W-eJr5cypbYK2oNctofK7BlMT9qagEwHA6SWyQQJVBpItYJmea2hw7h8xOhpWfc7JBZclGQFtMzLIVHVrT_7K0m2Yr8GvNvITeu_luspiTNQP_9i-p_osxRXXptMYlYdGPkCfDfeGXVmMolLL8yCNZTj4P1u9zJa9Bgxe7me36s1sFtU9ymD16D7k-l8FZVMRrDWr-LTGsdofEXNi0jTlqEwL4uaTBNsbcGYjHsjXKUtRqOU0WXfiVnXyVl0TKJSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:حملات را یادتان هست؟ آنها وارد می‌شدند و بیرون می‌آمدند.ما وارد می‌شویم، نابود می‌کنیم و آنجا را ترک نمی‌کنیم. این کاری است که ما اکنون در لبنان انجام می‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/15308" target="_blank">📅 12:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuAfDZcMQKHGxbYegFrW7lk_ibgpxXKeglN4RY2ooklsOtOA7A07007paPIZPjDkvTE5Beo_J2w1-suq3_AC_kW1erTq4_1-KGXOZxscxffZMgHGjd6-7dKjV-VJUWhlEgnbO3q_IFNzDtbjAM1THeZSLXRvzrVSoXb07v48-Z5y7gfIDzQGasTFtugYyCrdf3GGDiMjGaOKq7QHfjwy-RGOlKQ3vHW11GtRglNSLzaarPBBxrbOhCHtDuOLpj3TkfzZftS_C64GGvDpVHsaYOXOzFQXLvvd34ICKGs2I4I4VwqCdD1rqrEnmipgLCnKantY_gr1ZBGibog2uPeJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات ارتش اسرائیل ساعاتی پیش در بعلبک، در عمق حدود ۸۵ کیلومتری در عمق لبنان. حمله‌ای غیرمعمول در عمق آن - ارتش اسرائیل در ماه‌های اخیر تقریباً در دره لبنان و منطقه بعلبک حمله نکرده است
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/15307" target="_blank">📅 12:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd1e599ede.mp4?token=UUC9s-ussMWLqEPE-SIr3iu5fg9kUvN6bMu9Blx2i4i9kFpTc-fETFjJ6ojVLpmy6SAQ-oLWfRWnD5Io2j6qaIbHvv9vqNUHMlDP3QgS7mTi3738RxMGF9uSGtg91ce0vCARePs0K9V0xjcPifPYGziijVQ9Peoa6xKvR8P8wTdBL8DKy4ld-euKPexDKHJG50tBFUM3XCbXHG-I9TqRasG8Us5wsH_XamXnvWWXcWlYQKM3snniD8FUlItKPDYXuQr80VxpwDc837VUGtc0KH5feXxbp5nkseJpPbw_RrJZCXAT7NE9WeXaCgyw8Ry1UOVqT-XHkucHG7HSuEFvfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd1e599ede.mp4?token=UUC9s-ussMWLqEPE-SIr3iu5fg9kUvN6bMu9Blx2i4i9kFpTc-fETFjJ6ojVLpmy6SAQ-oLWfRWnD5Io2j6qaIbHvv9vqNUHMlDP3QgS7mTi3738RxMGF9uSGtg91ce0vCARePs0K9V0xjcPifPYGziijVQ9Peoa6xKvR8P8wTdBL8DKy4ld-euKPexDKHJG50tBFUM3XCbXHG-I9TqRasG8Us5wsH_XamXnvWWXcWlYQKM3snniD8FUlItKPDYXuQr80VxpwDc837VUGtc0KH5feXxbp5nkseJpPbw_RrJZCXAT7NE9WeXaCgyw8Ry1UOVqT-XHkucHG7HSuEFvfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز، درباره لبنان:تمام خط اول روستاهای لبنان ویران شده است.ما در حال ویران کردن تمام خانه‌ها هستیم. ساکنان دیگر هرگز آنها را در مقابل چشمان خود نخواهند دید.
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/15306" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم. @withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/15305" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هم اکنون منابع لبنانی می‌گویند:
ستون‌های زرهی اسرائیلی در حال پیشروی به سمت نبطیه، پایتخت حزب‌الله در جنوب لبنان هستند و درگیری‌ها سنگینی گزارش می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/15304" target="_blank">📅 12:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575f785e69.mp4?token=bSEdfUcD0dRUfExkB22jBTbh4z1B_No3kJoyhV-zoCR5F3gR5NAeTkIZXBGIge5N2STni0rdr6zX-HH7d4NtfTOIOq93BhWis6gBL0bc5j2x_GnQ1SKroqjy1jMK85pwirQbMEmU9pQqJfb2joEwgbjFMThn3dXJkFQhPTJETrrSuGvVN818LlKFE1aOe6Zo_oAHYcaBopwEl9fbwvKhw7b8HbcffkD42TNPPatTzfskKaHGq9fCdU4ZNpS0IjWPdbQCkXjxYGcyltDp_GMf3xu5cQ5Ab34G1D0KwmHPymR5byweXY6hn2mUwngL8oGdfy5NAQ2In-U6P8UdG0VVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575f785e69.mp4?token=bSEdfUcD0dRUfExkB22jBTbh4z1B_No3kJoyhV-zoCR5F3gR5NAeTkIZXBGIge5N2STni0rdr6zX-HH7d4NtfTOIOq93BhWis6gBL0bc5j2x_GnQ1SKroqjy1jMK85pwirQbMEmU9pQqJfb2joEwgbjFMThn3dXJkFQhPTJETrrSuGvVN818LlKFE1aOe6Zo_oAHYcaBopwEl9fbwvKhw7b8HbcffkD42TNPPatTzfskKaHGq9fCdU4ZNpS0IjWPdbQCkXjxYGcyltDp_GMf3xu5cQ5Ab34G1D0KwmHPymR5byweXY6hn2mUwngL8oGdfy5NAQ2In-U6P8UdG0VVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم.
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/15303" target="_blank">📅 11:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سوئیس رسما اعلام کرد: مذاکرات ایران و آمریکا برگزار نخواهد شد @withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15302" target="_blank">📅 11:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دو حمله هوایی به لبنان
الجزیره از دو حمله هوایی اسرائیل به شهرک عین بورضای و حومه شهر بعلبک در منطقه البقاع در شرق لبنان خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15301" target="_blank">📅 11:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1fHrfVI6CbeOV3bRgznb2B9cq0Ydvbnb690qkB6p6kR56i2sKKZ9KGW8FXm2zxFY-kH0qlIeKqZlViQ3gVplnl4ytsdFo-c0r5Xspbz2mopL9IRIEdE4_oGRn1hrwnud0AoPTDM2C8ddxbVv1EVmRpZJo_l_HPZ-ZVTALgJMp_sSo8OlxvcVvSomqfhr8CtB-f3Kfc7Rsz-edaBT1V8iKfLPJ_UpRldJkq0JG-wIH3M6rBxZuIoD1MS6g9PMxV4HLSycAd4rNPgM2SL1DPq8SgPSZrxymcDEJXBHNeZouGewsDDZESi-dl3RNj-aaTfI0D_CuuzvGRYpqpM0zpT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : یک ایده جدید:
دست از قلدربازی برای متحدانمان و چاپلوسی برای دشمنمان بردارید.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15300" target="_blank">📅 11:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سوئیس رسما اعلام کرد: مذاکرات ایران و آمریکا برگزار نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/15299" target="_blank">📅 11:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بن گویر وزیر امنیت اسراییل:به ازای هر اشک یک مادر اسرائیلی، هزار مادر لبنانی باید گریه کنند. کل لبنان باید بسوزد
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/15298" target="_blank">📅 10:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TERpVbhLAOMYPHHYnHOhB57TDyThl7X18mI8Fgxr3UonjhN9BCJJ2uIlo32cLHPzgQfsWUjiMzT_9BYD6vO7ZZzzdmR1HJF-8Re6enU5V1_d06USk9dlkH6oeGruXyE_qMih8DS1JnCHAWQ1FQFWCqdcQfm2WXeARDEXUtZxMpjwSO1wDFChVXGcLm8oNS8WrMMxEjFtpoie_bTkawrkz3ZH026KBIVZhnaWEnFuchW47JhhhtTQFON3GrYy14CPQ1eDMDYOrG9e29uUp8-vHJ83T0TaHmMDwqoU2OXaQ9WQuzvACXoLyd4Yg3q8t2puCPkozLrgZu10ghp48hScqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لورا لومر خبرنگار نزدیک به ترامپ جاویدنام های دی ماه رو حدود ۱۰۰ هزار نفر اعلام کرد
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15297" target="_blank">📅 10:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15296">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/15296" target="_blank">📅 10:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15294">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15294" target="_blank">📅 10:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15293">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزارت خارجه آمریکا: حزب‌الله باید خلع سلاح شود
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15293" target="_blank">📅 10:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15292">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دلار داره آرامش قبل طوفان رو تجربه میکنه و ممکنه بزودی حرکت بزرگش رو آغاز کنه  رفقایی که نمیدونن دلار میریزه یا رشد میکنه عضو این کانال تحلیل بشن بهتون میگه:  https://t.me/+hLt81qXCGTQzOWQ0 https://t.me/+hLt81qXCGTQzOWQ0  لامصب اطلاعات رانتی داره</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/15292" target="_blank">📅 02:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15291">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دلار داره آرامش قبل طوفان رو تجربه میکنه و ممکنه بزودی حرکت بزرگش رو آغاز کنه
رفقایی که نمیدونن دلار میریزه یا رشد میکنه عضو این کانال تحلیل بشن بهتون میگه:
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0
لامصب اطلاعات رانتی داره</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/15291" target="_blank">📅 02:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15290">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش های محلی در جنوب لبنان،
از حملات هوایی سنگین جنگنده های اسرائیلی خبر می‌دهند،آسمان جنوب شرقی لبنان به دلیل شلیک گسترده منور های روشنایی ارتش اسرائیل روشن شده است.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/15290" target="_blank">📅 01:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15289">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، لاتیش کردم
😂
فقط همین کامنت رو لایک کنید . ترجمه در کانال تلگرام.  https://www.instagram.com/reel/DZvkK0jpILu/?comment_id=18367681780225433  ترجمه :    ببین ترامپ،  می‌دونم دیر یا زود این کار رو به سرانجام می‌رسونی، ولی رفیق، این…</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/15289" target="_blank">📅 01:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15288">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، لاتیش کردم
😂
فقط همین کامنت رو لایک کنید . ترجمه در کانال تلگرام.
https://www.instagram.com/reel/DZvkK0jpILu/?comment_id=18367681780225433
ترجمه :    ببین ترامپ،
می‌دونم دیر یا زود این کار رو به سرانجام می‌رسونی، ولی رفیق، این دیگه درست نیست. مردم ایران از این همه انتظار و بلاتکلیفی به مرز دیوانگی رسیده‌اند.
این داستان را تمام کن و کار را یکسره کن.
خیلی از ما در این ماجرا کنار تو هستیم، اما باور کن این آخرین تغییر رژیمی است که حاضر به حمایت از آن هستیم. بعد از این دیگر چنین چیزی تکرار نخواهد شد.
عشقی.</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/15288" target="_blank">📅 01:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15287">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر دفاع اسرائیل:اسرائیل توانایی انجام عملیات مستقل علیه ایران را دارد و در هر لحظه برای اجرای یک عملیات آبی و سفید در ایران آماده است.
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/15287" target="_blank">📅 01:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر دارایی اسرائیل، بزالئل سموتریچ:
غزه در ویرانه باقی خواهد ماند. در نهایت، مهاجرت رخ خواهد داد، زیرا در دهه‌های آینده چیزی برای جستجو در آنجا وجود نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/15286" target="_blank">📅 01:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15285">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ: پیت هگست قراره خیلی پیروزی های دیگه بدست بیاره پسر خوبیه
من فقط مردمی رو دوس دارم که طرفدار من باشن
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15285" target="_blank">📅 01:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15284">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این پست جنجالی را از دست ندید، کلیک کنید و کارهای اداریش را انجام بدهید. حتماً تا انتها ببینید.  https://www.instagram.com/reel/DZvdCMHxeYT/?igsh=MW50eDUzOWQ0MnFzYw==  اتاق جنگ با یاشار : Bagher.exe</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15284" target="_blank">📅 00:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15283">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">subseven</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/15283" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15282">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/15282" target="_blank">📅 00:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15281">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این پست جنجالی را از دست ندید، کلیک کنید و کارهای اداریش را انجام بدهید. حتماً تا انتها ببینید.
https://www.instagram.com/reel/DZvdCMHxeYT/?igsh=MW50eDUzOWQ0MnFzYw==
اتاق جنگ با یاشار : Bagher.exe</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15281" target="_blank">📅 00:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15280">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbbJPgIu1vXcbVP0xxCwZFXVUtoeyvqWY6BTXDSX5TZ95rfbGwYwNBFSV2KACGDXlGXSCBDX97hq-XTaBaFgSqShcXpsb7ahvJuXFHEL4EfeQSdSLZ4p5neo8wKxNpE1L8xv6voMBd5OuVq7xCRRuMa0LQHXsote_WEwwrznjOlQGyN43kG0ZXBrJEWm2qq4q8gOUQrfjn1t4hDtkplycLVxHev4SpEgNxnUnGqksbI8XeDZu7DPCDtJBKiY0DSwDTJ_5FiLQLY1PwW-NqdK3e-Yxjfa_frAQBsDAL9RJNc5c6kOsrLXGhjJEuVvLnPEY4_YkUsMDJ-P59RSYiPYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/15280" target="_blank">📅 00:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15279">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر جنگ اسرائیل: قدرت ایران را درهم شکستیم، رهبران، دانشمندان هسته‌ای و زیرساخت‌ها را هدف قرار دادیم و برنامه هسته‌ای ایران را از بین بردیم؛ اکنون باید اطمینان حاصل کنیم که این برنامه دوباره احیا نشود
اسرائیل در هر لحظه برای عملیات مستقل در ایران آماده است
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/15279" target="_blank">📅 23:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15278">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">المیادین به نقل از منبع آگاه: هیئت مذاکره کننده ایرانی سفر خود به سوئیس را به دلیل تداوم حملات اسرائیل به جنوب لبنان متوقف می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/15278" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15277">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNWruP2TkQbOVehSMcW5TM4pdblKFewcLxZpPifvLFscx50Rz87z0e9NVqMU-lME1wBV4LdWO6OCdcP90aj7sFJ8Zg8QQP-whspQCSkIHVd3t_L79y4Sc_Q02S6M8vHYvnEdxPZi-BGzkH1vysfxfU65zQe_fwHmyNNV0fAUj32DUnPm2e5h-u7SUIQngSOBIoD7-GQ-kS1sA2ySeWzfsPfrHcajs-TOBFPu6dFP_uPfp7C3IcPS55sUHfGmyf9munmvn68m5yBL-CUHd8nU1GYAx-SSq87wqjSij1x5jtIl5cH73D1TF2Pu9vr6ulsUDbKgfCAO5x4FAODaO984KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: ایالات متحده به صلح متعهد است و ما از همه در خاورمیانه می‌خواهیم که به تعهد خود برای پیشرفت عالی مذاکرات ما پایبند بمانند.
بازارها از آنچه اتفاق می‌افتد هیجان‌زده‌اند:قیمت نفت به شدت کاهش یافته و سهام به سرعت افزایش یافته است.
ما انتظار داریم آتش‌بس کامل در تمام جبهه‌ها، از جمله لبنان، «حزب‌الله» و اسرائیل برقرار شود. از توجه شما به این موضوع سپاسگزاریم!
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/15277" target="_blank">📅 23:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15276">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شورای عالی امنیت ملی:
بر اساس تفاهم‌نامه منعقد شده، تا ۶۰ روز هیچ‌گونه عوارضی از کشتی‌های عبوری از تنگه هرمز دریافت نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15276" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15275">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15275" target="_blank">📅 22:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15274">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آسوشیتدپرس: کاخ سفید توافق با ایران را به کنگره ارسال کرد
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/15274" target="_blank">📅 21:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15273">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فارس:  تیم مذاکره‌کننده ایران تا حصول اطمینان کامل از توقف حملات به لبنان، هرگونه گفت‌وگوی تکمیلی را به حالت تعلیق درآورد
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/15273" target="_blank">📅 21:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15272">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رهبری سیاسی اسرائیل به نیروهای دفاعی اسرائیل اجازه داده است که در داخل «خط زرد» در جنوب لبنان تیراندازی کنند.
انتظار می‌رود مقامات ارشد نظامی در ساعات آینده قوانین درگیری و راهنمایی‌های عملیاتی به فرماندهان میدانی را به‌روزرسانی کنند.
این تصمیم همچنین شامل برنامه‌هایی برای نابودی هر «زیرساخت مرتبط با حزب‌الله» است که در داخل «خط زرد» شناسایی شود.
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15272" target="_blank">📅 21:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15271">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله به ایران و حزب الله آماده شوند
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15271" target="_blank">📅 21:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15270">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfHy8Of3YQ4G812jSonnjPlox0Z6GHf6lzzCxseuMPlH-lREvb_E4ZcgmfHG_OuqTxNO5f6XJ2Fqaw0APmEDNTSXVL40Bvl4U5g7hja8bTAUeJxEN3wHsRDcU07brYhH8-FZjbOWzFX4tigK4WNtE2-R3I1EGtUTL5jTxbK4b24B4OLZJmNKCffS2rM_aL4tD_El2xHd93jnAbwwODwGjfD6RwZYy5bwi8c7AbT0WJSsqtlmYjnv-CH5XJ2P8tDe-ijW9aOwrilNV6DrG9HSYyl42ioq6XHmFdIZd3ik2dlagW5Wfv0dErnTLgioUYv6cDXvCo9oa38NSnb-XfkO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس:  پیام جدید  iRahbar
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/15270" target="_blank">📅 21:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15269">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/15269" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15268">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQlCkmjfLq57LGIdHC5TbMxbDZsoay2JFNPWEWHyucMlgymMHjrJuhUumdz5uHRdLNcc09p42tnB0IZiyYSRh7udNogQBR_QvffP-6X0W7EARP7orxgnVDwblcxjSxtolZgIiyiLfE3UA0-tK_2YbkyAf3QymqwNEL7vzXLc4-mnJEE6vOL5-IrZUJ0Xpo9zZsktcSVpVbvkmHlbqo26GhRsUEfwNkRHQRu9n6v2jAOyKW_akjecfu6sBQq1oMF61Xc4fgubqVsbix23P4OVb4IRu6zjJpPp7WeGDieprMCvaq-sRpSEjNkLb1W7DmNas0eBVMBXmP5P_B64FnF-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : هیچ پرداخت ۳۰۰میلیارد دلاری از سوی آمریکا به ایران در کار نیست.
این خبر جعلی است!
تنها چیزی که نصیب آمریکا شده، موفقیت، کاهش قیمت نفت و پیروزی است.
بازار سهام را ببینید.
تبلیغات «دُمکرات‌ها» در جریان است!!
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15268" target="_blank">📅 20:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15267">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15267" target="_blank">📅 20:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15266">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbBJXqg9hzou-_lSUpG4InNHhoKyvOiKoBO6wlPysLhW0u19oaR1h4-A1A92gdETJbpcimNh-tdz10FnjgF9qiOmkNyZ0V9XcgTKa7JjyyA397XsOdd9amf0qFuhk2TtlOwAGIaligcpnOPjJk2HDOdNKp_uLscXuUCKqdr8yRlCPJRmREgTy7qVimRjXSfZLHFgqIyVFV6xUzRdVZqi6yB3qULJ0wKAGHjj8zOj11JG3ptA3cEsU_czsux-q5tNa4gG5Jfc-a49Rt03tJ7MGFzlcWHDoASKNoM3IK4iesHeyUrn3xaH7Bk6qcvfg-AUI3bFnH3wV-P-wHijDhkKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نیروهای ایالات متحده، بنا بر دستور رئیس‌جمهور، محاصره تمامی رفت‌وآمدهای دریایی به بنادر و مناطق ساحلی ایران و از آن‌ها را لغو کردند.
نیروهای آمریکایی دیگر مانع تردد کشتی‌ها به مقصد بنادر ایران یا خروج از آن‌ها در خلیج فارس و دریای عمان نمی‌شوند. تمامی اقدامات نظامی آمریکا برای اجرای این محاصره متوقف شده است.
ناوهای جنگی ما همچنان در منطقه حضور خواهند داشت تا اطمینان حاصل شود که همه مفاد این توافق به‌طور کامل رعایت و اجرا می‌شود و از قدرت و اعتبار کامل برخوردار است.
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15266" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15265">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ونس درباره نتانیاهو: من گزارش آکسیوس را دیدم که می‌گوید نتانیاهو عصبانی است.این بازتابی از گفتگوهایی که من با او داشته‌ام نیست. شاید او چیزی به شخص دیگری می‌گوید که به من نمی‌گوید.
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15265" target="_blank">📅 20:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15264">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a543e5cc9e.mp4?token=XJY5OSAr2vZzsqwsscroWxe_53RmWzLm8ER977GyZqDGkjruuoeKd-FH2imQR9w7WDHLWqhDvNnlM8xGJAKFKiBodp7Qk4UlHh3tuiPfLqyFOD7A4aLyUYtIqT8C5LeEftRwbJhnUnk64TFYsPqMBPQtR-8nRZd2oqSso0h5kKxcYvkbK9YAw8eiJOcN2LPPZD4EtQwboy57fwIA_R1-U5om4dfyvI_NOegZ3SWyxL_4ultdItKBdvYcTbT_S8YCR-9F_P2ikKSWR4lbVwnEvb60No_l3FdMhbWkiXFODRslwHatWYIeGFCmdzIc_XmOSmrL5tSLTJAKm3Bs-I35wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a543e5cc9e.mp4?token=XJY5OSAr2vZzsqwsscroWxe_53RmWzLm8ER977GyZqDGkjruuoeKd-FH2imQR9w7WDHLWqhDvNnlM8xGJAKFKiBodp7Qk4UlHh3tuiPfLqyFOD7A4aLyUYtIqT8C5LeEftRwbJhnUnk64TFYsPqMBPQtR-8nRZd2oqSso0h5kKxcYvkbK9YAw8eiJOcN2LPPZD4EtQwboy57fwIA_R1-U5om4dfyvI_NOegZ3SWyxL_4ultdItKBdvYcTbT_S8YCR-9F_P2ikKSWR4lbVwnEvb60No_l3FdMhbWkiXFODRslwHatWYIeGFCmdzIc_XmOSmrL5tSLTJAKm3Bs-I35wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی.دی. ونس در مورد لغو تحریم‌ها:
«راستش را بخواهید، ما این را یک امتیاز بزرگ به ایرانی‌ها ندیدیم — ایران هم... این را به‌عنوان یک امتیاز برای خودشان تلقی نکرد، چون چیزی که مانع فروش نفت آنها می‌شد، تحریم‌ها نبود.
آنها بدون هیچ تخفیفی نفت زیادی می‌فروختند، چون تحریم‌ها اساساً ناکارآمد بودند.
در آن مرحله، کاری که تحریم‌ها کردند این بود که سیستم مالی ایران را به نوعی به سمت سیستم بانکی سایه‌ای (غیررسمی) سوق دادند.
با لغو تحریم‌ها، در واقع خواهیم توانست کمی ببینیم که سیستم مالی آنها پول را به کجا می‌فرستد و از کجا پول دریافت می‌کند. این یک مزیت واقعی است.»
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/15264" target="_blank">📅 19:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15263">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_eaI9qc5sA83vnnWzT4dI5IlsVL7u0vDoXahVZLT1IHtGuLrobTwC0JCG4nk7-5KtUqo_snZI7JfMxsekjTR6AL7yUZd1afnJMEFQdP3ISrLIjxT3N1AXzQIVDw7mEn_GzuZXn5zWGERs1ukpvkuOTEpsvd_yMPWLomU0t3iFons2oRgFvd7QCJR-GJb7AyWOmZ4Ycd0JP1zkuyxCvAt_2Cvq1e_I_uioYjy8gJxBGfk_7qHM_i9cl0BmwJAjUGZC_yUkW2fHypXItxgws-G9KN1VdNe6f_P46mzPVQaXbrzA03j9bETl61gapyt8UBpXgzxJGAWMdDiIn3d84p-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ترامپی که امضاش اینهمه بالا پایین داره انتظار ثبات روانی دارید ، موج مکزیکی هم رد کرده نوار قلبه
😂
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/15263" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15262">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ونس: اگر ایرانی‌ها رفتار خود را تغییر ندهند، ارتش و برنامه هسته‌ای آنها همچنان نابود خواهد شد.
ما در حال حاضر یک تحریم اقتصادی فلج‌کننده علیه ایران اعمال می‌کنیم و تا زمانی که این کشور رفتار خود را به‌طور اساسی تغییر ندهد، به آن پایان نخواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/15262" target="_blank">📅 19:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15261">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آمریکا حتی یک سنت هم به ایران نمی‌دهد
جی‌دی ونس: "آنچه از همه شما می‌خواهم این است که صادقانه گزارش دهید که ایالات متحده حتی یک سنت هم به ایران نمی‌دهد...حتی مزایای اقتصادی، کاهش تحریم‌ها و غیره که با این معامله همراه است، فقط در صورتی اتفاق می‌افتد که ایرانی‌ها عمل کنند!"
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15261" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15260">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">معاون رئیس جمهور آمریکا: دوره ۶۰ روزه مندرج در یادداشت تفاهم با ایران از امروز آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15260" target="_blank">📅 19:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15259">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15259" target="_blank">📅 18:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15258">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ایهود باراک، نخست‌وزیر سابق اسرائیل:
احتمالا نتانیاهو در آستانه انتخابات، به لبنان حمله خواهد کرد، و در تلاش است یک جنگ ابدی را با ایران و حزب‌الله آغاز کند
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/15258" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15257">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ایرنا: ایران به پاکستان اطلاع داده است دیگر نیازی به برگزاری جلسه حضوری در سوئیس نیست.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15257" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15256">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5U_mcW6ytZgCbb5n2KQmvdyDUwLcx9aBsWKHjd9mxglZHm-fJ8Byo6vY0FzarMgs-Az6GsO_SvkC6AJeytZKHbUQ0NH3JmXk0Kymq7wfGcCf5O0lFW3GNmK4gDU9VKhOHAXMEQzMeLpVnDTzdKFwa8Nzu6NdxA9lhqWR5UtX9KsjupmWtp4cHAjED77Px1GGrfYJOAZnc7MK90IAS2wT0LMkWuocYqfIi5c30DnOEIHUJqPPIiRw8pFNrypzPjvywclBFGptaPNh9WMUF883F8WzpkR5ZtPKG_EcPn0O_XfvClN2A1rfUIatygyZe7cKycq6PND9yYx7ysHtXNmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نفت در حال جریان است، ایران هرگز نباید سلاح هسته‌ای داشته باشد (جهان امن‌تر خواهد بود!)، بازارهای بورس با قدرت در حال رشدند، اشتغال به رکورد رسیده، و قیمت‌ها در حال کاهش‌اند (امکان خرید بیشتر شده!). کشور ما قوی، امن و محترم‌تر از هر زمان دیگری است. “خواهش می‌کنم!
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/15256" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15255">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تلویزیون پاکستان:
سفر برنامه‌ریزی شده نخست وزیر شهباز شریف به سوئیس بدون ذکر دلیل لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15255" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15254">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">از صبح حملات اسرائیل به جنوب لبنان پر قدرت ادامه دارن
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/15254" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15253">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3483473645.mp4?token=Z7MT8Nz_DyUfGIS3yMXVMulOQr9QUxuZJ7V4kLCOEI-zvg7f2O-0-HqqBiQUOlcVwcxdF57NTKy8OUI2I5exsXAowc7EXklksE35stBzMaN1Oz0OMc1jLsBtsqCoO9Y62wHeeksGg-C898D2qI3-Giur1hzLCyogSYvJm6ec5wILFkKUQiB-8M6QEA6q6y7eTy88Bcj2S74bD65tbCvX1Ck7t_1_3mrUU064_jvef-JgsNWBSe1S83udnH1RmKLwUY4Cei1wuAhzgOnJ72m3-OTG24axnyD2MltD1JdH9gD4sVJSo5JriTsHEFG0nSIeQUQ4wGYjvZltjG831MsWwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3483473645.mp4?token=Z7MT8Nz_DyUfGIS3yMXVMulOQr9QUxuZJ7V4kLCOEI-zvg7f2O-0-HqqBiQUOlcVwcxdF57NTKy8OUI2I5exsXAowc7EXklksE35stBzMaN1Oz0OMc1jLsBtsqCoO9Y62wHeeksGg-C898D2qI3-Giur1hzLCyogSYvJm6ec5wILFkKUQiB-8M6QEA6q6y7eTy88Bcj2S74bD65tbCvX1Ck7t_1_3mrUU064_jvef-JgsNWBSe1S83udnH1RmKLwUY4Cei1wuAhzgOnJ72m3-OTG24axnyD2MltD1JdH9gD4sVJSo5JriTsHEFG0nSIeQUQ4wGYjvZltjG831MsWwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز شبکه پویای صداوسیما اومده و یه برنامه کودک در مورد توافق کردن و سازگاری گذاشته که تندرو ها به شدت عصبی شدن
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/15253" target="_blank">📅 16:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15252">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sa6BlNRLMkOgtwzgARENM66YT--_Czp65YRC4tCvFZiuN1NRrh-bO4AG9mr3CaY02f9u8KO_Sqcm1RtFKaHKYzur7g-z4OBEitoePzG6-NeNhbdAw_OhFyAP--xjOdrFbzfCKHU93UjuYpNG8JWna0A5pVPjiK6IukTey_JLU92ykWhah_QmpJ58jeA1pkA4lFJMakFUiWtRkP_mGCsaMbLmTSi7PNGqyQ_p1Kekh-D_JfdR12H8wocxfuFhA2ES3PyH0Arq4SsnkrMnQDvoI8Xjk7SrAEISbW-ZznQBgA9dm-Zx5vMjExaoIBXK8FQpKHO5UcT8qX4ZwNq-F7U7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : پاپ لئو از توافق صلح آمریکا و ایران تمجید کرد
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15252" target="_blank">📅 16:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15251">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">محمد محبی فوتبالیست تیم جمهوری اسلامی که در خوشحالی زدن گل به تیم نیوزلند، به مردم شلیک کرد، رفته و عکس مهسا امینی رو کنده و انداخته توی سطل زباله... @withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/15251" target="_blank">📅 16:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15250">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/15250" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15249">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آموزش و پرورش
: ثبت‌نام برای ترمیم نمرات تا پایان هفته جاری امکان‌پذیر خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15249" target="_blank">📅 15:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15248">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=YAe6IzuV-waczRC3bKED_0CmbXh6CRBCPsCSDFvSjED0LlLgOgOkMiT4_jo9c_DdXj4_VjCmfUyTiT0B8Ssin2xzZ0-E_x5enEhtjbUKqayGSb3jJqWpp7IaKQW0XSZkab9VKkrZFfujcovE_KDtNzQ2E1itYlzFIsDO-Lnv-umE9gTTkuWMlzlkOiuZc7RFMj1yVf0RaI5zqzINLACiJvl0fXUeuj-EMpa9odASn-95aN5Qxmp8BjMAELffiHqK_g2wUkNDULGGlH3lF7_-Th2jJ1zBf0WbUXtlm5uB1QRrlkYVn-E_3fk1XuuxA7QwL-VbedWdS45E5KGou3rXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=YAe6IzuV-waczRC3bKED_0CmbXh6CRBCPsCSDFvSjED0LlLgOgOkMiT4_jo9c_DdXj4_VjCmfUyTiT0B8Ssin2xzZ0-E_x5enEhtjbUKqayGSb3jJqWpp7IaKQW0XSZkab9VKkrZFfujcovE_KDtNzQ2E1itYlzFIsDO-Lnv-umE9gTTkuWMlzlkOiuZc7RFMj1yVf0RaI5zqzINLACiJvl0fXUeuj-EMpa9odASn-95aN5Qxmp8BjMAELffiHqK_g2wUkNDULGGlH3lF7_-Th2jJ1zBf0WbUXtlm5uB1QRrlkYVn-E_3fk1XuuxA7QwL-VbedWdS45E5KGou3rXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درست خوندم؟ Porngraph?</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15248" target="_blank">📅 15:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15247">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirAbbas</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxy9muVWe8fd5k_mgx9HCB_p8ryR-9J179RRt9iFehTbYjNa-EdP1YOfG3pkOEZwQJryhicVgSqTbH8ELXMRZDb5AfKfclYlw6CLpBTazerF3kG-GkdCWuvYOpt3yZ2HMD2q8WCe_f09C7oTYMQYPyDDmj84b3XyDSXDXKqbMhwGX3EAj-iYa9f0AepOMWMUQUIYob6W-hHmZ6vnVD79nCEDMlc-n5cCFRcoNaztrg4-8ss_fvXuItrlJtSMXQU8hfjjb0LgMSvZBrx-w3xE_7mOnkMRrw3dZ6DiHb61q0F8HIbw-geN83fL5BdEhn8YD-b1f1bPrlsywdlOdHcXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درست خوندم؟
Porngraph?</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15247" target="_blank">📅 15:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15246">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/15246" target="_blank">📅 15:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15245">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شبکه کان اسرائیل: موضوع عقب‌نشینی از لبنان هفته آینده با هیئت لبنانی در واشنگتن مورد بررسی قرار خواهد گرفت
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15245" target="_blank">📅 15:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15244">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرگزاری CNN : نتانیاهو معتقده توافقی حاصل نمیشه و جمهوری اسلامی با پایان دادن به موضوع هسته‌ای موافقت نمیکنه
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/15244" target="_blank">📅 15:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dImYhezr-P_W-YNxEccmI7R82XE8W0hz8HoIafNu-RcWZAp7yMtH-XK8VNrTO-XZGh43clY2U5ayZFwZVUSniMH9s2lM88EYVkuJaokfaw0p5Ep7jbeJfm5Foj6jeywaL-wQ7V5ogfe76TfC1j9nFxDuzbvnAwKD4Jd69w9FOecx3_WLG6K_NC-yiLkFwrDviHEJ5NDIR-jlFwKCjEd4swLjq7ex27kQD-wtGtAiEbUw_0MfisuP_EhNLsV6B2G5jzlSZ5ROu3Uzh3bIurFeDI2qmVi05bFFBWzL97SrG07lrj_4Vsk06_c7ooOmPClykTvgS6FU29zKnb4VWnrdlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeDt2jDQ0EbY9gfu94xoZRavg1WtL1c_u_sMjUaZUcgDKmifnH33JkQQxyg6677lJ-xJS95THmtwEJZ57W0kU52udmXhV_N0CZLfvc6QJFdewyHp2Fn10EZDgTRzS3Uwt0xPPHm3H8wufAWNHYOlvTZsIRrmr_cA48v02nN-Qx5E7voYMN2P-XST3UrZ7A8tq3LWjM6--GK9UdnkxdIoI4igS1u6-2f6t3r_jQaAgBNvrfydeoLmaLPVtS3FphQpBedWTEwxmcxUT4MiASLaZaChbRQcaASTFQCe55d3Fror49Jji2TNXeM18sMHLn7jR1khlar1XwB0NHxGWVNhmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OaHP8CDh6lQ8o1zNHLW5ZHJH-IgLpIB-wK8bhtczIoTiKFZE8dsf13E74GrJuZyo_BkAudILNt2Y9mllseZ5ZfuwmfoLsRPKKAh2Q_IrBVk--0Yxl8nE2fDFk08KLIt7L07ghj62-Uc-5xoxtQtRPEXVQQszWVi-VraxXwgURxJykAo9-6DZg7HzrlMOiBuN_yFirno6VtD-d9grpXzY3nV7Ew-Yv8_eKEUo4a4NoNJvY1umy6FsQ3Psc-9f2_oVxitDtNJDGa0HJE15HkYKaxZcdElF4HhenzJ0oOYCICWS8lqvZT5o0iQH5a-Ec03XUqprcQpJ6QpPNY7A4f-P7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکان نسخه اصل سند امضاشده را منتشر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/15241" target="_blank">📅 15:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d36518f3c9.mp4?token=WhmiK5wbIc65Ea_BfKsr0DzQX_0qvksGFvR119V1JNfCCq7nRGbaaXf6m6P1OOXnvtY3bzv6Suu_qm2F7ILAIy2Yx2oTZeQT1pOtdz5W3yOryUmO4s1xon_JWuZoEW0l3PFOSxnNyB8MxyEoIiTIjcT8DTC_tTEE9keZd3fGG-3KgKktmHNMNFbiX7mZBhlNzusIDo6vVnYPIH2pjBDxspUejD8u6nAZ_spp_a5oHG3wIJXRBKXs2ATl3tdpRBnKe5pjUoeXQRP_8gnY6v1zpmkcQKMoTe7VgCZCBgJFeH4IqAGRMyjBUmgG1Pp0AYIaChH3bI2w3efvrqWfTTyzRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d36518f3c9.mp4?token=WhmiK5wbIc65Ea_BfKsr0DzQX_0qvksGFvR119V1JNfCCq7nRGbaaXf6m6P1OOXnvtY3bzv6Suu_qm2F7ILAIy2Yx2oTZeQT1pOtdz5W3yOryUmO4s1xon_JWuZoEW0l3PFOSxnNyB8MxyEoIiTIjcT8DTC_tTEE9keZd3fGG-3KgKktmHNMNFbiX7mZBhlNzusIDo6vVnYPIH2pjBDxspUejD8u6nAZ_spp_a5oHG3wIJXRBKXs2ATl3tdpRBnKe5pjUoeXQRP_8gnY6v1zpmkcQKMoTe7VgCZCBgJFeH4IqAGRMyjBUmgG1Pp0AYIaChH3bI2w3efvrqWfTTyzRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی :
40 هزار ایرانی تو عرض دو روز برای یه توافق هسته‌ای یا باز موندن تنگه هرمز جونشون رو از دست ندادن.
اون‌ها برای آزادی و دموکراسی جونشون رو فدا کردن. اما عجیب اینجاست که تو هیچ‌کدوم از این مذاکرات، اصلاً دیده نشدن و هیچ اسمی ازشون نبوده.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/15240" target="_blank">📅 15:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15239" target="_blank">📅 14:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">راستی از لحظه ای که ادمین بیارم به شما اطلاع میدم ولی دایرکت رو هیچ وقت به هیچ کسی دسترسیش رو نمیدم و پیامهای شما تا ابد فقط دست شخص خودم امن خواهد ماند.</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/15238" target="_blank">📅 14:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15237">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دنبال شخصی هستم که برام ویکیپدیا بیاره بالا خیلی کم لطفیه بعد از حدود ۲۵ سال فعالیت در حوزه تک و کارهای انقلابی بسیار بزرگ، صفحه ویکیپدیا نداشته باشم و افرادی که خودم به مارکت آوردم و معروف کردم داشته باشند. امیدوارم یک فرد فوق‌العاده قوی در این زمینه کمک کنه و واسم بسازه.</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15237" target="_blank">📅 14:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15236">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/15236" target="_blank">📅 14:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15235">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فقط ‌یک پیغام</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/15235" target="_blank">📅 14:26 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
