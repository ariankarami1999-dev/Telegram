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
<img src="https://cdn4.telesco.pe/file/JGuNNZd3XKJENXf6Am7_WNDLrtd-V9UGuk1kps_QC4PJ7BUhSMWHOaW00dJyHCNKyl-ukkgHEbmAHDRvGDbE6vzG8iXv7kGo7cNhJSU6xuE6GaGjYvMpNdDr-s2D6B9ordli3JgATto_bbTxJ5OTmHcquRUDsCovcZrHNezH1mLFzLmhu0hjrcJzIyk1rJ8vtj5bSRp7PX6MoouPjAqBmUryd2bZ-yOrmIqaDkwa10T54c7gh5GtR2BFNraw0pdWAgHfEhP-uDFN76QnXhUEnJPsfdxJbVULsS-fX1POAQOO-G5w5XNdT7HsqmXO7qdfYsPOZoCEpnfIvsObz4fq7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 22:28:47</div>
<hr>

<div class="tg-post" id="msg-17441">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر‌دفاع اسراییل:   رئیس جمهور ایالات متحده در حال حاضر با توجه به منافع آمریکا، از جمله منافع مشترک با اسرائیل - برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای - در حال پیشبرد توافق با ایران است و ما از او انتظار داریم که این اصل و اصول اضافی را در حوزه…</div>
<div class="tg-footer">👁️ 407 · <a href="https://t.me/SBoxxx/17441" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17440">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سنتکام:  کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند.   تا امروز، نیروهای آمریکایی ۱۳۶ کشتی را تغییر مسیر داده و ۹ کشتی را غیرفعال کرده‌اند تا از رعایت این ممنوعیت…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SBoxxx/17440" target="_blank">📅 22:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17439">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwEgGkCae1zhYtz_Z1oXGvq3MW4JUIqEO8C6AsI6Y1rA0iHA-a_H-awhLsZ_qGhoRolZc04IC4t2rS9Qx-SqFG0IGMnRS8E_md5Lo9iO4OWte0Ua3Ac2b0VF4uG1YKdLDYSAHLOuRMwLjudF2bfVmZuK0xVYASQ4BiTiSnCcXqoGKRiWlbwyCEs9i9yToD0K0TFs80Toyd4HDlKptY4ublqHwOs_gk34V0ETzvd3849ae8q0zy9Fwa5KsZ3PsdS_yAoEZPGiQr36V2y5Yeg0xK6gmhSTcaI0clU8HYFF_pMzv4SNyjs-wTMnL1lqcnIU1w1D7RavqzRj_AaI4GolEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
نیروهای آمریکایی همچنان به اجرای دقیق محاصره علیه ایران ادامه می‌دهند. سنتکام از ۱۳ آوریل تاکنون ۱۳۹ کشتی تجاری مطابق با این قانون را تغییر مسیر داده و ۹ کشتی متخلف را از کار انداخته است.</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SBoxxx/17439" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17438">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">— وزیر امور خارجه پاکستان، امشب برای ادامه تلاش‌ها برای میانجی‌گری بین ایالات متحده و ایران به ژنو، سوئیس سفر می‌کند.</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SBoxxx/17438" target="_blank">📅 21:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17437">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مثل این است که بگوییم شما نزنید ولی اگر لازم شد ما خواهیم زد!</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SBoxxx/17437" target="_blank">📅 21:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17436">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDoSRvrL6m-F7DEfBj1AakBJfb9oTMYmFT4S8cYPO_7vl-cf2c615oYhMQsVKZdArqdCoM5Bx-z_IEvjK1WvNEoG01VQf01cgmoeBNKC11yYSYAfV11zBnkV1wxV1UGeqGlEEtygGsfD9biehMgZNTWLLtCy--YMJgEFFll0ywMDuPydum5zcItqZN2aA9HJRVyEau5Ghw3XHf2CSzGqYOwVWBG3W0AcQLuwfqq-7_hOAyEjWxZE65BU7DLWSEZrzwA9FMgAUy-cRRUEVGWo06gKLpoaF8bCSx-gckCU6tJesJjPKQPTKVKZt_c-if_wm1L-PEc4PapgOkggeDkicQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/17436" target="_blank">📅 21:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17435">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:  ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/17435" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17434">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:
ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/17434" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17433">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مقام ارشد آمریکایی :   احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/17433" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17432">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مقام ارشد آمریکایی :
احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/17432" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17431">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/17431" target="_blank">📅 20:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17430">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/17430" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17429">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نیروهای  اسرائیل تا چند کیلومتری شهر نبطیه در جنوب لبنان پیشروی کرده‌اند و در انتظار تصمیم رهبری سیاسی هستند.</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/17429" target="_blank">📅 20:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17428">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خداوکیلی راست میگوید!  الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!  پینوکیو با گربه نره و روباه مکار بهتر…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/17428" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17427">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsaWIFlKi3NrVrhNrW5zmJ4ddD1hQSmhkQLIZGxNyApkwBsbCms-af_u-04gRkY2WJeVXNpKFVqJKK9WaiKGvfTnnEiF2aDnVZtph12o4rn_oCFAxsWcH9eqm3lfz7_790iEZ_sRKYrF8-SyVAolV8bXcqQH4zb9m_grXs2OQC5MF9G3eVvd2fhOgEQSeqRCL_Iu2JAkGPTvHbmYCaobnefJEKfMNtXX1UNfLGWQq_DsGo-Lrh3Tgx0be9zjK3yr_N5sHtUuJ8fg6RTM_qyeYxRC2mrUfjC14_UA57nModTUzI7H1O7B1GpufONH7eh6QrqZeFnw42OWfpOD518Igw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوکیلی راست میگوید!
الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!
پینوکیو با گربه نره و روباه مکار بهتر deal می کرد.</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/17427" target="_blank">📅 19:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17426">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه  اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.  این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/17426" target="_blank">📅 18:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17425">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه
اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.
این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به آن‌ها و کل منطقه خواهد رسید. این توافق پتانسیل بازسازی منطقه و ایجاد صلح پایدار را دارد.
در گزارش‌های چند ساعت گذشته چند نکته عجیب دیده‌ام. اول، افرادی که (به درستی) یک ماه پیش گفته بودند دونالد ترامپ رئیس‌جمهور تاریخی بود، اکنون بر اساس گزارش‌های رسانه‌ای تأییدنشده از توافق انتقاد می‌کنند. دوم، افرادی که می‌گویند نمی‌توان به هیچ کلمه‌ای از سپاه پاسداران اعتماد کرد، ظاهراً به پست‌های ناشناس در شبکه‌های اجتماعی باور دارند.
رئیس‌جمهور به هر حال نتیجه خوبی برای ما به دست خواهد آورد.
t</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/17425" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17424">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiRcc8u9O_qJk9hmbDfS-uaT1sS56qT1e723fxpby5HkCFV7HlkCB3LqKcggyVRi6lMM59FFoa22UlUwh2Rk9Zgodmb9ebo8-QMhcPLhTwLoNDqK8W7Uw0KAK5bWofvEJWyoQGMkfUhP7S5Y4KXkZm2umOiOneshAwRSwjCX8qVUMTfGJINZqE5MFB1pdWMK134RJ23TN3VwG_L4Ta16IaYpwVzA61MNKZguVco_e4_-M88HA6laYxlcLnmIuJFh2b2NV94T47xOSDWRHFX_4wBSbA5g59yfgRcQJx6Kt_GZpMlDpLdz3WNYf0OpoJWSndUVUHUQ8wwTjiuRD3j8uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه دیدید یا نه؟!</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SBoxxx/17424" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17423">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWL4VARGbroHTVDQaDWgkQXAqYDj08DUPp1taKAq6gkPRNynPXW0f9Cv4wibwPRtP1C47nxSzJ0jFQHC8pFLZ4W3_e6h8l2SGmgkxKYkgxM-zz8BxdfNbEhj_iYG6r8OQ3CN_R6vMALhXA1dsTkCvtLdwgJYaTNobX-bSPL6JZ7PCZk0jKK68EBpvxH1JSUjq4es3ydPkyY-fx8gJfQe0rBADW2Z_ngoGr4VqEDE5tGRlHeFrWrxTWgnJY5oy00XIbMIAOQBjW8mpN7DjUyn2RVaiovQxeCDNBdM6ICQiSdB_7ovfE8K-4Et0bxexY7FDGJ9NLqYnvzJNnZ5-YSMYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/17423" target="_blank">📅 18:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17422">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزیر خارجه ایران عراقچی:
تفاهم‌نامه اسلام‌آباد هرگز به این نزدیکی امضا شدن نرسیده بود</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/17422" target="_blank">📅 18:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17420">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فوری | یک مقام ارشد آمریکایی به الجزیره: تنگه هرمز باز خواهد بود و هیچ گونه حمایت مالی از گروه‌های تروریستی توسط ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/17420" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17419">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فوری | یک مقام ارشد آمریکایی به الجزیره: تنگه هرمز باز خواهد بود و هیچ گونه حمایت مالی از گروه‌های تروریستی توسط ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/17419" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17417">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfR6_5Lh47Y7rjPsoLfulVoZ7lY_OTF0IwTkAy2C_xpgvkvVxMZEQ93E18w1QGT0YseTPatWEkl5C8E61QVpt1VupKItQ6x2THxO9XJAM2y4htFuIMjhe0FbSriQFmnXWYrT3cny3kqstWheC22TGxmoPK1yiTfuMo5cXiwCH5tVyQV5sT9iyXHObKJpDS3_TRTHaRlo7DTRijnqGZLcoGUyzakZABzZHCx-LXLb-3oVmO3m1137Q7Sr42HfIuTi6pNfdjauv533Q8lkeNEG5A_s89kdGIS_Fkc_4mJSfkCO5F7t4skNio2ZlVqUn_j4fhRcBl1oPLHvDsycRPKSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/17417" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17412">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gAMh4h7jtF42sZVmVysO-rAFQGR71-ARhVFzk4ovy4r346Ux3DNmCadc3d31kx4u-h6JtF6xKbsF-wGu1RV7EEYLZjizFakS2wZv2wby4ZPlmsKwXpHLsg1HU3LMqksyycw-4V-hTUNeMLZraJnXc7KNISjeJgF28ilV3IToEjIGsKWP-2Arknj15u4iwsmrqwgIWRbBtgYGbdg4gWci3l_XpxVBlpSwCW_zssj6sKLfweXruB_1TqlBvsU-Ks4F-mJ8AYO1mIe3-XImnkduGWf4xEakM93b4mHwtFm3NY0OqoBHEq0KUpqO0Enovb9xKPz_sSGsvKjbWZePuHe4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwIh66K8XmCnZS8emoW8P9e5CZ07Bcfk-mvTYbKLstw_qUc6nvgdQPqW0-qorHTN2U2q3Nzm-OzK202DtQAOl5n4RAiS0M86kymb4VxPzXqGg5JQgyiqUE9TU8fzfdMOEFG0YQmfv8YjL-KZJM5_Jwa4FiYl6Q5UD2F1Xcm67JmCMFYCoKqiKqhydgW1nREgrSpDACwiO6AN0tEOy4tPmOyX6ciAh6BBrjSroLEMVrBng0tHStxerQmZRv2pP0RnZJ6EEMsur81gny7VZ8lg1OfOMgOXmzgJevyNlFDtOwiugqXOZPbwlHyfHTcmthAi_uSxD4f04MU5rqYJDAF3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aScgHc8n6LS-ucItERFAXjH_swqOkgDuJSuPuA_3GTEa_VnE1oiwsDNnWkDhdMV0XEgIXh9e3a1FinA1XJT1PeK3Mgw0-QUslf0XAj_kMNM3EC7sJtvhySzSdks0RLkVDHFn17lDfP9Btsf6PtrDjurdtKv-Sv5ofZUNHT9RkeX8ZM-ZWjhf7vMFQAhkmaog-GUz727GnlYniszOSxfrmV9AU9AJT45XogXN0d9PzscT8C9b3-YYWrXd0z80p5IY-70BQwU5QdqPYSdVEB1geYiJzuupP1fsohdFkoj85w8quRQH0dmVDaM4wOf15HVgb3elkm5mIRrZY1HFFyhjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G54t7ibw6bl9sOMLhmi0VbeLyImGK4Y35hljNWcG7ToTwGY5uZrJGo6oxuq5tZ5X7a-qYDsIKy3qe45VNSyXLRVOUyHvL9VChOQQ4UcZhGIkHaAb6mmzQMPtsAGRAXO6jSX2Tq_GroZHHHoR76aBK48O3TVMEhIgzz0iUhB7UXOkk2zMmP5oYhwjjOoV89Y1r5disjlJEVmu0w0rlbMruQPq5__SpzzlGphqK5ZAZYcCfmG0uKG-YSUIPkhA7yYxV41948nn2Xmyp-I-eozXqlp5IsOUzFuDAsRsfS5StBNNRbxfQir_6uM5w6QyEN36jKNIegHd1s2Ir2-Ye_cqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S51e4UjhkHppoOEG2fMmB1Bikqz_E6zc_kJgL4xkMfwrXcI1o-RoWNz5jW4Z026de4ucgfqbA8aX_Sxvvaw1F-mszvbcKr8pUcnWBlIfKEyGSrT36V79_B4GkgZ2slnjWpJLu1_ZEQHp92cCvpSizS2Itq8IpAFCSbEZFvNoVbDa5B-zKuUKnnCMcS74wvn8VFZbm3uSxDYBf3tsXFBki0-lwnBxMvEfIt7Suh8GjYL0Mqc_Ei9HPoa0NgWieJEb2hvztWDrpxlDPTi3JBSSuY_jm_7_7OpZWoAXVrGoA-TNxzDswaogAWH99KM0tsfGRbyNrrUu5CXi437jppzomA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتفاق جالب در ژست‌های قلعه‌نویی؛
⌚️
ساعت "رولکس اسمورف
"
چشم‌ها را گرفت!
👀
ساعت 10 میلیاردی امیر قلعه‌نویی در فوتوشوت‌های رسمی
#جام_جهانی2026
سوژه فضای مجازی شد.
🆒
این ساعت از برند لوکس و مطرح رولکس معروف به مدل
“Smurf”
است. به دلیل ترکیب رنگ
آبی پودری (Vibrant Blue)
در صفحه و بزل که تداعی‌کننده شخصیت‌های کارتونی اسمورف است، این نام روی آن ماندگار شد. در حال حاضر قیمتی بین 40 تا 50 هزار دلار دارد.
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/17412" target="_blank">📅 18:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17411">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">امیرحسین ثابتی:   کسی حق ندارد تنگه هرمز را به امید رفع تحریم یا محاصره باز کند</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/17411" target="_blank">📅 18:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17410">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این یعنی توافق بی معنی است:   اسرائیل باید اطمینان حاصل کند که در آینده نیز توانایی اقدام مستقل برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای را خواهیم داشت و من و بنیامین نتانیاهو، نخست وزیر، به ارتش اسرائیل دستور داده‌ایم که بر این اساس آماده شوند.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/17410" target="_blank">📅 18:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17409">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر‌دفاع اسراییل:   رئیس جمهور ایالات متحده در حال حاضر با توجه به منافع آمریکا، از جمله منافع مشترک با اسرائیل - برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای - در حال پیشبرد توافق با ایران است و ما از او انتظار داریم که این اصل و اصول اضافی را در حوزه…</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/17409" target="_blank">📅 18:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17408">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خب این نخستین آزمونی است که باید گذرانده بشود. ببینیم در لبنان آتش بس می شود یا خیر.</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/17408" target="_blank">📅 17:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17407">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390974dead.mp4?token=lR5Vuh0qGYcA75GSC2HuhLMekLvOnlJCAkaKEhGzNt9pQNuh66UMuTufe8Qcu2LGqWAL42Nc5JpHAzy6LdaJNH86BVBpcjb_d_hbRC28ReTNtVlMRvzmsvlbW26X_Ikky0rl6vlMiX0ANy3ZVzihsa9n3KaAl1hF0vnAw0HWLrv_DjxdQAs7HvS9_Ap_rX3YeVfcAv3CZF4U5VvIrHkIOgq984g0adMIQTZeVViH8UrFCCA-fUkEfd8nkQw9-e2V1n0_ChHn1DnO91_vE9LLcZXzbQDV5JNqSTuaBs34Y5vVTiixgO-oiMj3hsW2xHyPZZwSf1ZAA61ccr_XEn3QfYouG08KBc--AjiyoRmSEMsy3n-fDohWcVt6eYKwQAC05pHBQXPwKNVqaRHoEq91vN8wZ9dB8opgIEE5ajDXbLRDaqHXzn7ZPf_d_MNyhaoRT7-dNYdBG74-YBINDBDSxK1OODVFs1W3HuTyCI-Xt3AYL1-sxkRHG6jJztKlKLnVgqV1-Ia50zAi49buMSjVYgZKG6B1usDO17CoVAWQRzJdEy1UgPnCy9JCRx6_0d0M72GBmpYxLXnDC7_5wMEPf2QChXEKTkYKUC1Wo5yNXb_wLqWDd7goNlKLJg5Bo_xVnQvdT8jp001TZwhGX83_IS-Yid8ZWvxJbIE5GYABtYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390974dead.mp4?token=lR5Vuh0qGYcA75GSC2HuhLMekLvOnlJCAkaKEhGzNt9pQNuh66UMuTufe8Qcu2LGqWAL42Nc5JpHAzy6LdaJNH86BVBpcjb_d_hbRC28ReTNtVlMRvzmsvlbW26X_Ikky0rl6vlMiX0ANy3ZVzihsa9n3KaAl1hF0vnAw0HWLrv_DjxdQAs7HvS9_Ap_rX3YeVfcAv3CZF4U5VvIrHkIOgq984g0adMIQTZeVViH8UrFCCA-fUkEfd8nkQw9-e2V1n0_ChHn1DnO91_vE9LLcZXzbQDV5JNqSTuaBs34Y5vVTiixgO-oiMj3hsW2xHyPZZwSf1ZAA61ccr_XEn3QfYouG08KBc--AjiyoRmSEMsy3n-fDohWcVt6eYKwQAC05pHBQXPwKNVqaRHoEq91vN8wZ9dB8opgIEE5ajDXbLRDaqHXzn7ZPf_d_MNyhaoRT7-dNYdBG74-YBINDBDSxK1OODVFs1W3HuTyCI-Xt3AYL1-sxkRHG6jJztKlKLnVgqV1-Ia50zAi49buMSjVYgZKG6B1usDO17CoVAWQRzJdEy1UgPnCy9JCRx6_0d0M72GBmpYxLXnDC7_5wMEPf2QChXEKTkYKUC1Wo5yNXb_wLqWDd7goNlKLJg5Bo_xVnQvdT8jp001TZwhGX83_IS-Yid8ZWvxJbIE5GYABtYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط سیس پیروزی حماسی اژدهای بندر را ببینید خداوکیلی !
ولی ازش خوشم آمد میهن پرست است .</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/17407" target="_blank">📅 17:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17405">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">با Secret باش خدایی کن!  با Secret نباش فقط برگرد!</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/17405" target="_blank">📅 17:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17404">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نفت بخرید و شیشه ها را چسب بزنید که ناپاکستانی جماعت کثیفترین دروغگویان عالم هستند</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/17404" target="_blank">📅 17:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17403">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6ec42ab9.mp4?token=klUHAsrNUHuIdESm3G9Z66EgSom1lDNFC7n4Ouz0vFV5kVS6p5AqJCsWLZwoeAus2rtCj69LbumXk4x4HKnmPGQMR43kEQ93BEBb77ILCfoMrSbCFk08TWLYzoPtUa_Os0Tn0iVueOStdB1CSLslQABogFL2ZchbMaRCF_EQCWoNV98X9uPfX104tzhJ2j1yLOfoBCt0xVd2lEz-6oPA1IbORo79eK_TkP7-NDLEO4BlFK5O3SDo9zrbNTGpWyPChzqONHN-uyio8dIAazkztAC9Bw4Yzpwblb2fQJkoFtLB5YEuvwgITwsjUErtI_aaBVxtF9-pwmVW7He30sq43A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6ec42ab9.mp4?token=klUHAsrNUHuIdESm3G9Z66EgSom1lDNFC7n4Ouz0vFV5kVS6p5AqJCsWLZwoeAus2rtCj69LbumXk4x4HKnmPGQMR43kEQ93BEBb77ILCfoMrSbCFk08TWLYzoPtUa_Os0Tn0iVueOStdB1CSLslQABogFL2ZchbMaRCF_EQCWoNV98X9uPfX104tzhJ2j1yLOfoBCt0xVd2lEz-6oPA1IbORo79eK_TkP7-NDLEO4BlFK5O3SDo9zrbNTGpWyPChzqONHN-uyio8dIAazkztAC9Bw4Yzpwblb2fQJkoFtLB5YEuvwgITwsjUErtI_aaBVxtF9-pwmVW7He30sq43A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اژدهای بندر به شما نگفت ولی دونالد قرمساق گفت که منشا صداهای دیشب چه بوده!
یک کشتی هندی بدبخت حرفهای کله زرد دال بر باز شدن تنگه هرمز|ثابتی را باور کرده بوده و میخواسته از تنگه عبور کند که سپاه پاسداران به آن شلیک کرده و می‌گوید برگردد  و هندی ها با ندای :
Sepah Navy ! Sepah Navy
!
You gave me clearance to go! Let me turn back!
دمشان را روی کولشان گذاشته و برمیگردند
این به قول اژدها یعنی
نظم ایرانی
!</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SBoxxx/17403" target="_blank">📅 17:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17402">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شرایطی که ایران به اخبار جعلی نشت داده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده است، ندارد. آنچه آن‌ها گفتند، از جمله بیانیه ضعیف و حقیرانه‌شان مبنی بر داشتن یک توافق، هیچ نسبتی با حقیقت ندارد. افراد بسیار بی‌آبرویی برای معامله کردن. با آن‌ها هیچ‌گونه…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/17402" target="_blank">📅 17:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17401">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/17401" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17400">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Buy Oil</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/17400" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17399">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">The terms that Iran leaked out to the Fake News have NOTHING to do with the terms that were agreed to, in writing. What they said, including their weak and pathetic statement on having a deal, bears no relation to the truth. Very dishonorable people to deal…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/17399" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17398">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">The terms that Iran leaked out to the Fake News have NOTHING to do with the terms that were agreed to, in writing. What they said, including their weak and pathetic statement on having a deal, bears no relation to the truth. Very dishonorable people to deal with. With them, there is no such thing as dealing in good faith. AMAZING! Also, their totally rebuffed Drone attack last night against Indian Ships leaving the Hormuz Strait is TOTALLY UNACCEPTABLE. They better get their act together, and FAST! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/17398" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17397">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مجری فاکس نیوز در مورد توافق ایران، به نقل از یک مقام کاخ سفید  مواد هسته‌ای نابود و حذف خواهند شد  برنامه هسته‌ای برچیده خواهد شد  هیچ یک از پول‌های آنها تا زمانی که عملکردشان را نشان ندهند، آزاد نمی‌شود  تنگه هرمز باز خواهد بود  ایران هیچ گونه حمایت مالی…</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/17397" target="_blank">📅 17:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17396">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/17396" target="_blank">📅 17:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17395">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/17395" target="_blank">📅 16:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17394">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ایران وضعیت تنگه هرمز را به سطح قبل از جنگ بازنمی‌گرداند - ایرنا</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17394" target="_blank">📅 15:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17393">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17393" target="_blank">📅 13:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17392">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17392" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17391">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">متن کامل:  خبرگزاری نیمه‌رسمی مهر ایران فهرستی از اصطلاحاتی را منتشر کرده است که گفته می‌شود در پیش‌نویس یادداشت تفاهم با آمریکا وجود دارد. این خبرگزاری به منبعی نزدیک به تیم مذاکره‌کننده ایرانی اشاره می‌کند، اما جزئیات به طور علنی توسط تهران یا واشنگتن تأیید…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17391" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17390">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDKt2g6SL0uyBuo1IEVQCtSfP8CSibeyGY4QWbp9lrVrYY5Lca2sgF2jZ0W-d-aL7ZBptXnTdlksvcQ9InmLIU3RDLYGdX8ijtqdXGDDLxMfUF9T5yAREEmPWPxZXL2aFOBlc0P9OWFV-cZtrjrVKLPaCLexSbZJTkLLVpJ1LqVPVYTomSQ5iatSzLR0cRTBK-BUxMTRFztrSEFSi7zUzp1RqQ0mamHi_SYyeUoN9Uc2R5UR1zrnhs4jMFrTiLN5MWp5LBsWB9DsLldGnJNqxoe8Qh3efTwgIj45uSBbFKNLUmVNWrHekeVCbKDlxddFsQMLToIiny2WFMsZedkzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزودن شدن 1500 میلیارد دلار به ارزش بازار سهام آمریکا با اعلام توافق دیروز توسط ترامپ</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17390" target="_blank">📅 13:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17389">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو.pdf</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/17389" target="_blank">📅 12:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17388">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حملات سنگین هوایی اسرائیل به جنوب لبنان</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17388" target="_blank">📅 12:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17387">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB6SY76fO6wbSOhbvMIrhSB1zNlgyHyqXRB6DrAr_GgzrmhOXNfWRQqCkW9OtVfPsdkqszjfbuDFPjfMGQRAwBfSHCVvRbURe6uX-0shgCZIYTOnu78YKb8hkXm_UKD4X5dVs6hDksTA68JyU_0gaGwVYvpV9RH5R84aFAHs6Ywiop0EqJKw74RkAOjUqGaUlyLa9ansMi-o3HS4Xpz_wbsbne3zDHKnELt8RxZddOidbDoGC901Kv0ixS_94LfanY4HceG26p5jCOjuGGVA_nNWqsYBzHcdm-7EhSADsjPri0xo3VWU246lM6nA4wH7jQYypQaSKByS_dKmEiRweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این نخستین آزمونی است که باید گذرانده بشود. ببینیم در لبنان آتش بس می شود یا خیر.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/17387" target="_blank">📅 12:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17386">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسرائیل 2000 سال آینده را نخواهددید.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/17386" target="_blank">📅 12:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17385">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسرائیل 2000 سال آینده را نخواهددید.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/17385" target="_blank">📅 12:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17384">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سردار نقدی:   انتقام ما، آزادی فلسطین و محو صهیونیست‌ها است، اما این مسیر باید منطقی طی شود</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/17384" target="_blank">📅 12:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17383">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سردار نقدی:
انتقام ما، آزادی فلسطین و محو صهیونیست‌ها است، اما این مسیر باید منطقی طی شود</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17383" target="_blank">📅 12:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17382">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">توقف دائمی و فوری جنگ در همه جبهه‌ها، از جمله لبنان</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/17382" target="_blank">📅 12:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17381">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ایالات متحده موظف است طرحی برای بازسازی اقتصاد ایران ارائه دهد، در حالی که مذاکرات نهایی بین دو کشور باید در مورد مسائل هسته‌ای و اقتصادی و بدون بحث در مورد برنامه موشکی ایران انجام شود.  خبرگزاری مهر</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/17381" target="_blank">📅 12:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17380">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">همچنین ایالات متحده وظیفه دارد غرامت جنگی پرداخت کرده و از کل منطقه غرب آسیا خارج بشود و ایران را به عنوان ابرقدرت چهارم جهان به رسمیت بشناسد.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/17380" target="_blank">📅 12:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17379">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایالات متحده موظف است طرحی برای بازسازی اقتصاد ایران ارائه دهد، در حالی که مذاکرات نهایی بین دو کشور باید در مورد مسائل هسته‌ای و اقتصادی و بدون بحث در مورد برنامه موشکی ایران انجام شود.  خبرگزاری مهر</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/17379" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17378">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ایالات متحده موظف است طرحی برای بازسازی اقتصاد ایران ارائه دهد، در حالی که مذاکرات نهایی بین دو کشور باید در مورد مسائل هسته‌ای و اقتصادی و بدون بحث در مورد برنامه موشکی ایران انجام شود.
خبرگزاری مهر</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17378" target="_blank">📅 11:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17377">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الجزیره:
ادامه حملات اسرائیل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17377" target="_blank">📅 11:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17376">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ برای ۱۴ ژوئن جولانی را به کاخ سفید دعوت کرد.  ترامپ به ان‌بی‌سی گفت که می‌خواهد «حمله‌ای جراحی‌گونه‌تر به حزب‌الله» در لبنان انجام شود و دمشق را به عنوان عامل این کار مطرح کرد: «ما می‌توانیم به آن‌ها در این زمینه کمک کنیم یا سوریه را پیشنهاد دهیم. سوریه…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17376" target="_blank">📅 10:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17375">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فوری | یدیعوت آحارانوت از منابع خود گزارش می‌دهد:
نتانیاهو گفت به ترامپ اطمینان داده است که تلاش او برای دستیابی به توافق با ایران را درک می‌کند، اما اسرائیل نباید قربانی شود.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17375" target="_blank">📅 10:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17374">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ برای ۱۴ ژوئن جولانی را به کاخ سفید دعوت کرد.  ترامپ به ان‌بی‌سی گفت که می‌خواهد «حمله‌ای جراحی‌گونه‌تر به حزب‌الله» در لبنان انجام شود و دمشق را به عنوان عامل این کار مطرح کرد: «ما می‌توانیم به آن‌ها در این زمینه کمک کنیم یا سوریه را پیشنهاد دهیم. سوریه…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17374" target="_blank">📅 09:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17373">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آمریکا: دو پهپاد انتحاری شلیک شده به کشتی‌ها در تنگه هرمز را سرنگون کردیم
نیروهای نظامی ایالات متحده دو پهپاد انتحاری که به سمت کشتی‌ها در تنگه هرمز شلیک شده بودند را رهگیری کردند، این در حالی است که گزارش‌هایی از شلیک ایران به کشتی‌ها در این منطقه منتشر شده است.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17373" target="_blank">📅 09:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17372">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">در روزهای اخیر گزارش‌هایی از تحرکات جدید نیروهای وزارت دفاع سوریه در مناطق مرزی با لبنان منتشر شده است. بر اساس اطلاعات موجود، یگان‌های تازه‌ای به غرب استان حمص، به‌ویژه مناطق القصیر و نواحی مشرف به دره بقاع شمالی، هرمل و عکار در لبنان اعزام شده‌اند. این تحرکات…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17372" target="_blank">📅 03:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17371">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">در روزهای اخیر گزارش‌هایی از تحرکات جدید نیروهای وزارت دفاع سوریه در مناطق مرزی با لبنان منتشر شده است. بر اساس اطلاعات موجود، یگان‌های تازه‌ای به غرب استان حمص، به‌ویژه مناطق القصیر و نواحی مشرف به دره بقاع شمالی، هرمل و عکار در لبنان اعزام شده‌اند. این تحرکات در ادامه روندی قرار دارد که از ماه مارس آغاز شده و طی آن دمشق اقدام به تقویت حضور نظامی خود در امتداد مرزهای مشترک با لبنان کرده بود.
مقامات سوری هدف اصلی این استقرارها را افزایش امنیت مرزی، مقابله با قاچاق و جلوگیری از نفوذ عناصر مسلح عنوان کرده‌اند. با این حال، اهمیت این تحرکات در شرایط کنونی منطقه فراتر از مسائل صرفاً امنیتی است. مرز سوریه و لبنان طی سال‌های گذشته یکی از مهم‌ترین مسیرهای انتقال تجهیزات، نیرو و پشتیبانی لجستیکی برای گروه‌های مختلف فعال در منطقه بوده و تحولات جاری می‌تواند بر موازنه‌های میدانی تأثیرگذار باشد.
همزمان با ادامه درگیری‌ها و تنش‌های منطقه‌ای، دمشق تلاش دارد کنترل مؤثرتری بر مناطق مرزی اعمال کند و از تبدیل این نواحی به کانون بی‌ثباتی جلوگیری نماید. هرچند تاکنون نشانه‌ای از آمادگی برای عملیات گسترده نظامی در داخل خاک لبنان مشاهده نشده است، اما استمرار اعزام نیرو و تقویت مواضع مرزی نشان می‌دهد که دولت سوریه تحولات مرزهای غربی خود را با حساسیت ویژه‌ای دنبال می‌کند و آماده واکنش به هرگونه تغییر در وضعیت امنیتی منطقه است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17371" target="_blank">📅 03:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17370">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
🇮🇷
- دونالد ترامپ:
ما امروز جنگ با ایران را به پایان رساندیم و آن‌ها توافق کرده‌اند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن اصرار داشتیم. این همان هدف اصلی بود. این ۹۵ درصد از آن بود. و، اوه، آن‌ها این کار را به قدرتمندترین روشی که ممکن است انجام داده‌اند.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17370" target="_blank">📅 03:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17369">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فارس:   دقایقی قبل نیروهای جمهوری اسلامی ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه هرمز شده بود را ندادند و همزمان سه انفجار هم در سیریک شنیده شد</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17369" target="_blank">📅 02:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17368">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ:
بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل و تأیید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده علیه ایران را امشب لغو کرده‌ام. مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات کامل، توسط همه طرف‌های درگیر از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران تأیید شده است.
محاصره دریایی تا نهایی شدن این معامله به طور کامل ادامه خواهد داشت
— زمان و مکان امضا به زودی اعلام خواهد شد.
دونالد ج. ترامپ
رئیس‌جمهور ایالات متحده آمریکا</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17368" target="_blank">📅 02:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17367">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99919094c3.mp4?token=GIDyH5Sa-gJUN9Ru6MT9tzpM7xMwEq3RnVtZnqwunZ4kb2bdouzRCDujOz3nxM7EuPpyzu2G0zAyn8zK70g0TQfdkHwksdwCy4Rmz87FUaA-I2qKrT3piOwX7N8DV5MkR-sk_RbYhuTKMTdjRhYmapIBqYLJiHxTGLx_2IbfUxfuDWf_ZkjsthhshuwGhPqZMOcCZrmmoHix8cNpPwcbScxRwNkzuDs9QTRzry6NHQUXAFYWpsYj96JK4SMi8NHsNUHIZObXQy00mX_P-1uO8dq-j2hWlM8VBymZeEz0GnsdAlP40blWt1wjyitXUxlBvSDFUDW7jw7YAyQAlZjpOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99919094c3.mp4?token=GIDyH5Sa-gJUN9Ru6MT9tzpM7xMwEq3RnVtZnqwunZ4kb2bdouzRCDujOz3nxM7EuPpyzu2G0zAyn8zK70g0TQfdkHwksdwCy4Rmz87FUaA-I2qKrT3piOwX7N8DV5MkR-sk_RbYhuTKMTdjRhYmapIBqYLJiHxTGLx_2IbfUxfuDWf_ZkjsthhshuwGhPqZMOcCZrmmoHix8cNpPwcbScxRwNkzuDs9QTRzry6NHQUXAFYWpsYj96JK4SMi8NHsNUHIZObXQy00mX_P-1uO8dq-j2hWlM8VBymZeEz0GnsdAlP40blWt1wjyitXUxlBvSDFUDW7jw7YAyQAlZjpOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظر می‌رسد که شرایط توافق با ۱۰ شرطی که جانفدایان میگفتند خیلی شباهت ندارد!  از توجه شما به این موضوع سپاسگزارم !</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/17367" target="_blank">📅 01:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17366">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ایران تمام دارایی‌های اقتصادی مدیریت شده توسط ایلان ماسک را به لیست هدف خود اضافه کرده است و شرکت‌های ماسک را متهم می‌کند که در حملات دیروز ایالات متحده علیه ایران کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17366" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17365">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فارس:
دقایقی قبل نیروهای جمهوری اسلامی ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه هرمز شده بود را ندادند و همزمان سه انفجار هم در سیریک شنیده شد</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17365" target="_blank">📅 01:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17364">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش های تاییدنشده از انفجار در بندرعباس.
گفته می شود ایران به چندین کشتی که حرفهای ترامپ را باور کرده و قصد عبور از تنگه هرمز را داشته اند شلیک کرده است.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17364" target="_blank">📅 01:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17363">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رسانه‌های دولتی ایران: انفجاری در نزدیکی ساحل سیریک شنیده شد؛ علت و منبع آن نامشخص است</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17363" target="_blank">📅 01:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17362">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3u5Aco4UtUAK0xti0TyHGGCRrXLaLjazZYUJsL9-X60hGe93vi71gh1_RQuNxPhjZ-AACSfDZcBK8i-092iXBZUaHCjo5rAxGVmSyfMaSJNyxglCLB-1H7lL_mtWHHOga1gvOQnvwqt7ItEIVjgn-_qbjNH8VC4XbansNmCZFfhAX2GWh47BPjAHEto-F-NT-N7ak5akMZT-uiH_ilCBK-OXOa7ooROs5uQHSs2hRRiXI_9ilk5MTndnq442UEEPHjeN7Hkdw_koHGU7mwkSCejFfGIB6EdC8HX_mNSe4BIJy4eW-gJ-ee-SkGeDRI55jLLLsRqP_2krKR-RK_mmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی (ب) قهرمان | امید هر مسلمان!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17362" target="_blank">📅 01:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17361">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📡
حسین اژدهایی ؛ خبرنگار ویژه صداوسیما در بندرعباس:  در قشم و چند شهر دیگر صداهایی شبیه انفجار شنیده شده است که هنوز محل آن نامشخص است</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17361" target="_blank">📅 01:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17360">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رسانه‌های دولتی ایران: انفجاری در نزدیکی ساحل سیریک شنیده شد؛ علت و منبع آن نامشخص است</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17360" target="_blank">📅 01:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17359">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17359" target="_blank">📅 00:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17358">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خبرنگار: پیش‌تر گفته‌اید که ایران و ایالات متحده به یک توافق نزدیک بوده‌اند. هنوز اتفاق نیفتاده است. چرا این بار آن‌قدر مطمئن هستید که شرایط متفاوت است؟  ترامپ: چون آن‌ها کتک خورده‌اند. آن‌ها کتکی خورده‌اند که خیلی کم‌کسی می‌تواند تحمل کند. و آن‌ها بسیار بیشتر…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17358" target="_blank">📅 00:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17357">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرنگار:
پیش‌تر گفته‌اید که ایران و ایالات متحده به یک توافق نزدیک بوده‌اند. هنوز اتفاق نیفتاده است. چرا این بار آن‌قدر مطمئن هستید که شرایط متفاوت است؟
ترامپ:
چون آن‌ها کتک خورده‌اند. آن‌ها کتکی خورده‌اند که خیلی کم‌کسی می‌تواند تحمل کند. و آن‌ها بسیار بیشتر از من می‌خواهند که توافقی صورت گیرد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17357" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17356">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-poll">
<h4>📊 به نظر شما:</h4>
<ul>
<li>✓ توافق شده طبق آنچه نتانیاهو می‌گوید (تسلیم کامل ایران)</li>
<li>✓ توافق شده طبق آنچه سپاه دیکته کرده (تحقق همه شروط ایران)</li>
<li>✓ توافق نشده</li>
<li>✓ نمیدانم؛ اطلاعی ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17356" target="_blank">📅 00:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17355">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دفتر نخست وزیر اسرائیل نتانیاهو: توافق شامل  محدود کردن تولید موشک و پایان حمایت از نیروهای نیابتی منطقه‌ای   می‌شود</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17355" target="_blank">📅 00:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17354">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فوری | وزارت امور خارجه ایران: ایران ثابت کرده است که آنچه را که به عنوان خطوط قرمز خود تعریف کرده است، تحمل نمی‌کند.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17354" target="_blank">📅 00:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17353">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به نظر می‌رسد که شرایط توافق با ۱۰ شرطی که جانفدایان میگفتند خیلی شباهت ندارد!  از توجه شما به این موضوع سپاسگزارم !</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17353" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17352">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، اسماعیل بقایی:
تا کنون، ایران به نتیجه نهایی در خصوص توافق نرسیده است.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17352" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17351">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جالب است که ترامپ می‌گوید خودشان تنگه هرمز را پیشتر باز کرده اند و ما خبر نداشتیم اما الان گفت که بعد از امضای توافق با ایران تنگه باز خواهدشد!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17351" target="_blank">📅 23:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17350">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMuSiuSCqhW-X3cWM9FUK01DuKl_7P1CRurisbH9Zb1F6rswdgo8zjtKVxP895wnzKC37K7b9LDP8VY5bNe0Zhpj3FbQ2cnMp8c9oDQWkCP6oQGTCnUrjZKjxIMTDgCcvgykmjVloe4aqQJ-Wy0G17yWbNQUzMjq3O6Wzv_N4tx12orCpp8rDgHpT0QP1_DX_rNQCkSz0Fz6I41xP5i6F_mi1BaSXaA_D5ehGgwwv1-8PVjr01FWM3h3sQurr0ch1Y6J-oCCAZEpYzdngf1636r15WUINwTYFCJjcwVvUfNVig69grzYwX3Yxr8zDSk0Em4_GhSbs2df1QA51ChaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر می‌رسد که شرایط توافق با ۱۰ شرطی که جانفدایان میگفتند خیلی شباهت ندارد!
از توجه شما به این موضوع سپاسگزارم !</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17350" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17349">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دفتر نخست وزیر اسرائیل، نتانیاهو: توافق نهایی شامل خروج مواد غنی شده نیز خواهد بود.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17349" target="_blank">📅 23:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ:   اخیراً ایران را به‌ شدت بمباران کردیم و رهبرانش حتی بیشتر از من خواهان رسیدن به توافق بودند.  ما از همان ابتدا در جنگ با ایران پیروز شدیم، ایرانی‌ ها فرصت دارند کشورشان را بازسازی کنند، چرا که به‌ شدت ویران شده است</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17348" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عصر گفت رهبر ایران موافقت کرده حالا می‌گوید «برداشت» من است که موافقت کرده!   تف به خودت و برداشت ت</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17347" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عصر گفت رهبر ایران موافقت کرده حالا می‌گوید «برداشت» من است که موافقت کرده!
تف به خودت و برداشت ت</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17346" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17344">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فوری | ترامپ: امضای توافق به زودی انجام خواهد شد و برداشت من این است که رهبر ایران با آن موافقت کرده است.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17344" target="_blank">📅 23:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17343">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بالاخره محاصره را برمیدارد یا نه؟!</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17343" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17342">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فوری | ترامپ: محاصره دریایی تا زمان نهایی شدن توافق پابرجا و معتبر خواهد بود و تاریخ و مکان امضای آن به زودی اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17342" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17341">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
ادعای فارس: احتمالا مقامات ایران با توجه به عقب نشینی آمریکا توافق را بپذیرند</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17341" target="_blank">📅 22:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17340">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">قبل از اینکه ترامپ حملات علیه ایران را لغو کند، با پاکستانی‌ها تماس گرفته شد که ادعا کردند «ما با ایران توافق داریم»   – نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17340" target="_blank">📅 22:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17339">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قبل از اینکه ترامپ حملات علیه ایران را لغو کند، با پاکستانی‌ها تماس گرفته شد که ادعا کردند «ما با ایران توافق داریم»
–
نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17339" target="_blank">📅 22:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17338">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">— منبعی نزدیک به تیم مذاکره‌کننده ایرانی به خبرگزاری فارس گفت:
«هیچ متنی برای تفاهم‌نامه اولیه با آمریکا تصویب نشده است».</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17338" target="_blank">📅 21:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17337">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">منابع اسرائیلی و عرب های خلیج فارس که با کانال ۱۳ اسرائیل صحبت کردند، گفتند که از هرگونه توافق حاصل شده با ایران آگاه نیستند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17337" target="_blank">📅 21:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17336">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17336" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17335">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرگزاری تسنیم:  «ترامپ اخیراً ۳۸ بار ادعا کرده است که توافق قریب‌الوقوع است، بنابراین تا زمانی که ایران رسماً اعلام نکند، ادعاهای او را باید صرفاً در چارچوب دروغ‌های قبلی‌اش بررسی کرد.»</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17335" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17334">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">باز کله زرد حرامزاده دروغ می‌گوید  محال است سپاه چنین توافق ذلت باری را بپذیرد</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17334" target="_blank">📅 21:26 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
