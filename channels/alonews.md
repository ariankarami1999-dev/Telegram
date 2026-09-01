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
<img src="https://cdn4.telesco.pe/file/nh5aeHiWNH1jU7Uic6mVf7nFzueFjz5ZEeBoT1fOnNEefMU-ZkUZ4OxWbdAqy8e_V6crzg5_6fHfSzOeRmeA8nevbivucJ1Y6qAf1I0nKmLw9Kxy7-CeO8QUtLat5bJVSLaGRHVxGwUVLiNRWWJSaIy_q-sxDtvv8ONj4JfwgsROBVw9uN4MsGVWqDV7sMhn8C7kJHOmNrmGRi3NJccFQIYhDUJKOdBGtUlmT74qIZWDP0BdL8NGwLP6iYQhavFHhDJmSFcLhMOPhT--cPR-NYJOr9rXZnkcWpen6oKyXbnMOKN_ccB7lOuUN_5EjFTC7i-fbGpVKjNVeIz_zdvpDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 956K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-145027">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سیستم‌های اسرائیل پرتابی به سمت اردن را شناسایی کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/145027" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145026">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
خبرنگار فاکس نیوز: امشب چه اهدافی در ایران مورد اصابت قرار گرفت؟
🔴
ترامپ: تعدادی از رادارهای آنها
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/alonews/145026" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145025">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فوری
🔴
حمله بزرگتری در انتظار است و زمانی که به پایان برسد، تقریباً هیچ چیز از جمهوری اسلامی ایران باقی نخواهد ماند.  ترامپ:  ایالات متحده، در حال حاضر، به اهداف ایرانی در نزدیکی تنگه هرمز حمله می‌کند. این حملات گسترده و قدرتمند هستند و در پاسخ به تلاش…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/145025" target="_blank">📅 22:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145024">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
معاریو به نقل از منابع: اسرائیل هیچ نشانه‌ای از تشدید درگیری با ایران یا ورود تل‌آویو به جنگ دریافت نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/145024" target="_blank">📅 22:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145022">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcH18tfGMekhFsiOZIgVWBHAy9-bQX1eMyP4oqeMzke7bphKgO_4ldWXzWz7paIRqBPy4mYFpdYJu8hjySYnwLiQE5qYbbuWZKDj3GVtFVra8du4mQ0O8DjDk8UlxIQ0yxNtOXFLiSFl1w1Z0xNwiuE2UzccR1m0tivH1nwfL_JXS2YUADuyuKFdxJWmKQ9-XjmwHgDWhv7uWww4dSiuRYoLvQQQ20wH9-ZUUaTTTsE_u9QVw4GfWEV4lpSqV_dCQLVw1raPJHnfUi5RxtKL54cT2WoqdWhEBXF6UtMLjldK_hHtKnN5hCLQdU1CVHSHoC77QW0gUCRLsgAVLYry-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: ما شاهد بازگشت چرخه‌ای تدریجی از تشدید تنش‌ها هستیم،
🔴
چرخه‌ای که به طور قابل توجهی بی‌ثبات‌تر به نظر می‌رسد. یک تقابل تلافی‌جویانه می‌تواند به راحتی به یک رویارویی منطقه‌ای گسترده‌تر تبدیل شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/145022" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145021">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نفت خام آمریکا بیش از ۴ درصد جهش کرد و برای نخستین بار از ماه ژوئیه تاکنون از مرز ۹۰ دلار در هر بشکه گذشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/145021" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145020">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cO8kETsgEVt42sv9X2P1g4QQLNubwdAlseTVH2xpzZlDN4o1groLXax-meYLhBpZhXL3glJyNV8JUQX-lzgXhe5y0HKv0DAo9fPRyurKvhlbWE__DRTCdGrJ9Dgc8f15ngQbXofaUHLl1ieBFIFq9qCJqhifxZhHc_CbTedTw59PvSne04i1Sxd6d8GjV2SpAp6cgYc48wfFUvCeVHLf4etgBmCK-D8eR6FneHNrj3TsIk628DBnSG49q_ea90utlZm1HVspsjoyoQMyzaoMJkFThni_gqfj-Q-BW-WgJzibmK2SsLnIpmuBy1JSLzG7cNN5mKdLhlsNCqGt-0ntIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوخت‌رسان ها بالای تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/145020" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145019">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/145019" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145018">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnyBNA9pHUXoCFNVVAPCM4XIu_z2Dv3hWBcJ7UQ_ZTBWCWQ0kTMeuFjUQMcDGFlY3iuBW0YYbAw7ELTYwXcND6C6mlfZcNfsFXgTjbRWus7LBZkiJc9AFuVel3wk35unrwEVtBYCE4cHbWADOjJW09w3UPTh9hhiycGe4xu8hIpDrzwQX6naoXmKsM6T1npVLiuQH0MCzG3g3TU3rKF2Qd3w8znbw9IaQZ6Qn-iJt-Fm7CWeVhKoXDENcmb17lCHqPu4RJwLc-79u4hVdt_XMMgRyZL2MnhacoL69k9ZJ4EQvWDJjjqWpGsOJ9aqX9Hiwcc2K12opyhbLOxpQvux-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت فعلی آسمان ایران
🔴
تنها یک پرواز استانبول مشهد مشاهده می شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/145018" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145017">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7fb757104.mp4?token=c8ieUmq0e5jFA__64tA0I_TWOHUp_5pnHrLI0QNP2M97m3ralHpbE6OPAGhjyLByX-lxSLHK5y1JKDPwPSSYmAvPE2r2NcYIfw8NZvUkNt8oV0G8gb1UNz76SeGmRtpVh1k1ns8G-S7ySatvSDexdFRPLH5-1CrL5F5iCE800B9OiQcg4d_vLFVtthDDr00c4ZRjLQQoMUthTbD5jurkVHQ_QlKXBsl5rKPmtrXgz4XYzgId7sgIvmXdjR46RNu0fPcangpDIhumQPoUOHOCLaVveBwTnXc6CLz0i2OhwZvF6T06KHhTA4hp5BrFWMnWAxxGEQEGsWRzbOWb-PfprA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7fb757104.mp4?token=c8ieUmq0e5jFA__64tA0I_TWOHUp_5pnHrLI0QNP2M97m3ralHpbE6OPAGhjyLByX-lxSLHK5y1JKDPwPSSYmAvPE2r2NcYIfw8NZvUkNt8oV0G8gb1UNz76SeGmRtpVh1k1ns8G-S7ySatvSDexdFRPLH5-1CrL5F5iCE800B9OiQcg4d_vLFVtthDDr00c4ZRjLQQoMUthTbD5jurkVHQ_QlKXBsl5rKPmtrXgz4XYzgId7sgIvmXdjR46RNu0fPcangpDIhumQPoUOHOCLaVveBwTnXc6CLz0i2OhwZvF6T06KHhTA4hp5BrFWMnWAxxGEQEGsWRzbOWb-PfprA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرنگونی پهپاد آمریکایی در خمین
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/145017" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145016">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/981e07149f.mp4?token=Jc7lAIS2_6GRJhtadxSu3K9WZz1IggaQO20EUbrtxg3hqsn-Q6gQq8SY0F0p-Tk-Xj2tekhK0I2d1RF8BrpnS1zcpJ1B8YGL3zfl2fz9yO-q9w-17Af9cQRiqrclTF-_sYvShMgLTG_03tbQHWH9_Ak_WvrBnOTa2GcWEtmq8Egqi8YAeN5SL-QM2-UyFRA6SPWvdAVvwf5PllMW_0YNEMRHwZMWBTeiOJdQ-Wr406_KvDduzjEp5we7B65aFyAyb9-8cp2AfSdYDCEfMUzZgef_zmoardP4z0z1SciXanTrYqj7EHoo422_t1cGy5MPnA7XUIx5rtrXIrw-hoI7V7gayJWOXoFeske-wgHmbmAQmZkecTH6H9YShsBhAvwgn1Abr-lvpQtaaGq9GCrJayFnSwpOw0SQ-avxqApcGSOM6g09aMdBnpCb5ntpCoroT_eLd-TmXiMcL1NhZCS1D_yg98ByddCaxsBffDmjbIsvyThDsozlhA9cdQPcSPzhpos0xf-KolfXHlUZn7K8goAo-p1vEl3jTxybf--7aDVbYQmLWFZwAEZ4_AftrDNaauHYlkVp923RGaVv7DDzVVVzb1wCOLCWH9tiJgSaVECVJP_pwOkwxvehNTDJI97iYeNqfaE0iI1hEfiuRxyyCwFE2Pel6hvdG0NDrPrZmTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/981e07149f.mp4?token=Jc7lAIS2_6GRJhtadxSu3K9WZz1IggaQO20EUbrtxg3hqsn-Q6gQq8SY0F0p-Tk-Xj2tekhK0I2d1RF8BrpnS1zcpJ1B8YGL3zfl2fz9yO-q9w-17Af9cQRiqrclTF-_sYvShMgLTG_03tbQHWH9_Ak_WvrBnOTa2GcWEtmq8Egqi8YAeN5SL-QM2-UyFRA6SPWvdAVvwf5PllMW_0YNEMRHwZMWBTeiOJdQ-Wr406_KvDduzjEp5we7B65aFyAyb9-8cp2AfSdYDCEfMUzZgef_zmoardP4z0z1SciXanTrYqj7EHoo422_t1cGy5MPnA7XUIx5rtrXIrw-hoI7V7gayJWOXoFeske-wgHmbmAQmZkecTH6H9YShsBhAvwgn1Abr-lvpQtaaGq9GCrJayFnSwpOw0SQ-avxqApcGSOM6g09aMdBnpCb5ntpCoroT_eLd-TmXiMcL1NhZCS1D_yg98ByddCaxsBffDmjbIsvyThDsozlhA9cdQPcSPzhpos0xf-KolfXHlUZn7K8goAo-p1vEl3jTxybf--7aDVbYQmLWFZwAEZ4_AftrDNaauHYlkVp923RGaVv7DDzVVVzb1wCOLCWH9tiJgSaVECVJP_pwOkwxvehNTDJI97iYeNqfaE0iI1hEfiuRxyyCwFE2Pel6hvdG0NDrPrZmTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «آنها سعی کردند رادار خود را بازسازی کنند چون هیچ چیز را نمی‌بینند. ما صبر کردیم تا تقریباً ساخته شد و بعد آن را زدیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/145016" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145015">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
هم‌اکنون دو انفجار جدید در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/145015" target="_blank">📅 22:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145014">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8ea8cab388.mp4?token=C8QSNRjoFFHWcm5hwpIeveMLd5IfEaiJeaT-r4qsFeIh4TFXlGgLqfZyOqVx0koaQUqxTE-QHNLXnDF0y_aUUhE3u_cQsmYrI8CUq_KqG8RXC6QYTmngjMj9rPwyz147tUnLgzuYyL_oMF2laFnMIXPxJpuRjGw1BVNTacY_dDRN6Bo1IzHRpPtomTTt4SDOPRHludznJnFow4bl6BIMXbkVgUgrRfu1lysrYCCgefpbr-yLhZSn5AtRs5npMZ7XPVNcC4I6kLM3tchV4gwtAZ4ejV6eeMLBTNAKI5EoemAi1t5ZzG61Xv5gcST_OjCpiXSu9VQsuJGMvqUrb5m0wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8ea8cab388.mp4?token=C8QSNRjoFFHWcm5hwpIeveMLd5IfEaiJeaT-r4qsFeIh4TFXlGgLqfZyOqVx0koaQUqxTE-QHNLXnDF0y_aUUhE3u_cQsmYrI8CUq_KqG8RXC6QYTmngjMj9rPwyz147tUnLgzuYyL_oMF2laFnMIXPxJpuRjGw1BVNTacY_dDRN6Bo1IzHRpPtomTTt4SDOPRHludznJnFow4bl6BIMXbkVgUgrRfu1lysrYCCgefpbr-yLhZSn5AtRs5npMZ7XPVNcC4I6kLM3tchV4gwtAZ4ejV6eeMLBTNAKI5EoemAi1t5ZzG61Xv5gcST_OjCpiXSu9VQsuJGMvqUrb5m0wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145014" target="_blank">📅 22:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145013">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
پرتاب موشک بالستیک از کرمانشاه، ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145013" target="_blank">📅 21:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145012">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
صداوسیما از حمله آمریکا به فرودگاه جیرفت خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145012" target="_blank">📅 21:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145011">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارشی از حملات آمریکا به نقاطی در کشور
🔴
نقاطی از شهرستان کنارک در سیستان و بلوچستان
🔴
قشم (هرمزگان)
🔴
بندرعباس (هرمزگان)
🔴
سیریک (هرمزگان)
🔴
جاسک (هرمزگان)
🔴
بندرلنگه (هرمزگان)
🔴
نقطه‌ای در جیرفت کرمان مورد هدف آمریکای قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/145011" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145010">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65659b88ab.mp4?token=adj6l1DbUmFgr9-xjRJeY0n2ppMVqK8IC6qyJEy4AsxuPafbwSEfBiuXhG1rBr8GoS6pu5eoc6y5jmXDMM1MKO983hLFHrbGOOjWNGCzBTadKE6TjX6L16OTT5JEyBBYtNcJwhLf_IWTzEKhY52XLThv8F34SpoFsYrGw90Nyi6E0TZPdd6edumQbNdeoplXC-YlDpvw4aBT-NfFC5mRdwWY_jUbK16V-wj0p71tdSL2mVXxvIRwTN0-0gPu8LFymeznWg_8VQz_DUz8GxbUTFCX9SdzRyI4phxZn3Yh5-RKjVUMUJV3kE0t4bmWATKKPVNI_tNii1ff54X-7cvRnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65659b88ab.mp4?token=adj6l1DbUmFgr9-xjRJeY0n2ppMVqK8IC6qyJEy4AsxuPafbwSEfBiuXhG1rBr8GoS6pu5eoc6y5jmXDMM1MKO983hLFHrbGOOjWNGCzBTadKE6TjX6L16OTT5JEyBBYtNcJwhLf_IWTzEKhY52XLThv8F34SpoFsYrGw90Nyi6E0TZPdd6edumQbNdeoplXC-YlDpvw4aBT-NfFC5mRdwWY_jUbK16V-wj0p71tdSL2mVXxvIRwTN0-0gPu8LFymeznWg_8VQz_DUz8GxbUTFCX9SdzRyI4phxZn3Yh5-RKjVUMUJV3kE0t4bmWATKKPVNI_tNii1ff54X-7cvRnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ناو هواپیمابر یواس‌اس جورج واشینگتن تا سقف ظرفیت خود از مهمات پر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145010" target="_blank">📅 21:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145009">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: آن‌ها سعی کردند رادارهایشان را بازسازی کنند، زیرا چیزی نمی‌توانستند ببینند. ما منتظر ماندیم تا این بازسازی تکمیل شود و مجدداً به آن‌ها ضربه زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145009" target="_blank">📅 21:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145008">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e1284509.mp4?token=IvVVhw0QCK4_XRu7P0sKIXkSsYAwJ3DsQvjXNno7_NbLORJ_tFPPF9hLSGv3WCSGPAZ--gpJXi5g6L5WigwomYs5iqj0iB8GLvQQH44Rb4X6uDKTjE1qdX7tLAkFh05kGNfBRpxUqbcC3hkNMN2xSUxN2aV8-X_9MhpMEwMU7q4AP5E9yupqyneGzP4nwOvF_J40D4aVRM86qkGFXqgM4C47RcjFM-lKGvf4iTPj3Kx_RURqZ8AjPRYAFSunQlUNz3KKbz7Rbx4ohe9rxlgC4bvG7jqXQB7Qf50Rlrdmc4bjJGz2yZP9j4E3EnkP3h5StHN4yW_NGuiFTY_NWDBdPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e1284509.mp4?token=IvVVhw0QCK4_XRu7P0sKIXkSsYAwJ3DsQvjXNno7_NbLORJ_tFPPF9hLSGv3WCSGPAZ--gpJXi5g6L5WigwomYs5iqj0iB8GLvQQH44Rb4X6uDKTjE1qdX7tLAkFh05kGNfBRpxUqbcC3hkNMN2xSUxN2aV8-X_9MhpMEwMU7q4AP5E9yupqyneGzP4nwOvF_J40D4aVRM86qkGFXqgM4C47RcjFM-lKGvf4iTPj3Kx_RURqZ8AjPRYAFSunQlUNz3KKbz7Rbx4ohe9rxlgC4bvG7jqXQB7Qf50Rlrdmc4bjJGz2yZP9j4E3EnkP3h5StHN4yW_NGuiFTY_NWDBdPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک موشک از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/145008" target="_blank">📅 21:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145007">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: اگر ایرانی‌ها تلافی کنند، ضربه‌ی بسیار سنگین‌تری خواهند خورد. و اگر باز هم این کار را بکنند، دیگر وجود نخواهند داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145007" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145006">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xwb2crElgSdZkkutpPJQlhJTaDHdoqgOTd8FHCieaeo5G1j0HkngrrufpHBw4FJdXqLcsHnqOevNMoU4CZ_BloHoy7WQMXYB3Sp8BsEQ2-hvePmbNAo2ZnRFqx2ETjaZBPvp5ej7l2JiWH1wJQo6ipnWh4WHCQanm6P7DIxHiAoOrr2JNNkRcvBxR9GWz1fClazSBJ-pDo0DPQJBVsTllGWrX9d6yHD2CvPyWJMCK9t8D0qeeWOdcnt9Eb_7M84x0AnDoeTJl6_XXro76bcmR5MgrJds6mjAqBg_yW6HalxUfB_N5iwE7b9Rl32OYJaRk2ddFKQE6HaiREX8atlhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش‌های اولیه حاکی از آن است که موشک‌ها از ایران شلیک شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145006" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145005">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری/ حملات جدید به قشم و لاوان هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145005" target="_blank">📅 21:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145004">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
انفجار جدید در شهر عسلویه استان بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145004" target="_blank">📅 21:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145003">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi-kzgVo_OorHXl-dTzFY_TDwsS2-iYEUthtTjO1qXR9en3hBd8EkwK_hWWxOxT4ov8FLPIZCKouv4lPgTyEPl9xKr6U4e0gwUlylM-62m6s6qlcE92ifj23m2e2brpmffSMT8RYswFPlW9mQLnfm5gHZ5E5ZykTVXzPEbbq96ChuHG4djpr7b1zc1j1RbwI8FcOHoG26KdZkfQTHzktRjQkJSpc1fPZuc18TN3vMdaNDK__pVYaKC3hsIz_2OcmNEg5DKOfLTCW05eR6l85D_t-lrI-laCIXnbk-Gj1uhkQ1Vq_6RpDRJpfn9PaAY-pXzibbkjyajEoDif6aCq5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی: پرواز یک هواپیمای اسرائیلی برای شناسایی و رهگیری موشک‌ها در آسمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145003" target="_blank">📅 21:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145002">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: شهروندان آمریکایی همین الان فوراً ایران را ترک کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145002" target="_blank">📅 21:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145001">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
مهر: در حملات ساعتی پیش ارتش آمریکا به سواحل جنوبی ایران یک کارخانه پودر ماهی در قشم، یک اسکله صیادی و دکل اداره‌ی بنادر در سیریک مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145001" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145000">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دو انفجار جدید در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145000" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144999">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سخنگوی سپاه : تنبیه سختی در انتظار متجاوزان است، آمریکا از حملات جدید خود پشیمان خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144999" target="_blank">📅 21:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144998">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsiDrPAM7FbU283_yXz_-9ptsvj8tfXhKvqOtVcQYUohSPckUTOVAIoTZia1rw1GxUxN8FRXV9uJ6HOhUkhXQj-QZCnhXWTbaLKCKn5XtaS8JgtOMRYPIjylTdtQWBatlGY44gXWzujuOqR3TRZeMs0IjmbFwo39sqtlgK8JXs-Dzu5RU3aIa0nXKV49Z0-qFZxDlckzQsajh644B3EVKk0HPbJyYG6Xk107N-XyZtw6i4KTvoZppoXyU7x1Sg9A56iuuDsF3P-leX8IuNJ6OIFDTO3dc3gVG7XnyTWGP3mINN8AZGK2mV90Azw6wkxlq9mPwAtlxEj5OkrMeFv78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این متن رو داری میبینی
یه نشونه‌ست برای آغاز مسیری جدید از زندگیت تا یاد بگیری که چطوری،خیلی سریع به موفقیت برسی!
💸
✅
اگه میخوای درآمدت چندبرابر بشه
💰
اگه میخوای لایف استایل زندگیت متحول شه
💡
وارد کانال شو بهت یاد میده چطور دلاری پول در بیاری
اینجا میتونی روزانه درامد داشته باشی و سرمایتو چن برابر کنی.
لینک عضویت کانال وی ای پی
✅
👇
👇
https://t.me/+nTm6gDB4A8gyYmFk
https://t.me/+nTm6gDB4A8gyYmFk</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144998" target="_blank">📅 21:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144997">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
صدای انفجار در مشهد مربوط به ترکیدگی و آتش‌سوزی خط لوله گاز در جاده کنه بیست مشهد بوده؛ علت حادثه در دست بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/144997" target="_blank">📅 21:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144996">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aov_0DQCt82hnCPqwhNgp-3zxdfPC2t_Dl7aM_ZGpVW2Q_ioA2QK9ieNyhui7N_t8V5zcTJjLXdgejpVchdXgZfKvMI8EX2SKEbQd7EoNTuhTN3yiTsFIfTrhFXmevLmxzD-ipjjdv4GDMYPxgTWqLozRK-yj7pPJeFJF59ahcNC11DutJ68tdBtmSzHLEWWkXDzxo7jOrd5ZOqCoDBLijWu0BEEiCCk0XcoRmlTguhH1LCgIif-ty_J1qoMdOCMCWvF_qWfui89l4yvzDU10M2Bu7qajOahmngWt8ClvWuHTH7-GJH-kh9jJEE4-uZ_FFO-8x7Y3sC3mQOZQYNh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ: ایالات متحده، در حال حاضر، به اهداف ایرانی در نزدیکی تنگه هرمز حمله می‌کند. این حملات گسترده و قدرتمند هستند و در پاسخ به تلاش ناموفق ایران برای نصب مین دریایی در تنگه است (که در حال حاضر هیچ مینی در آن وجود ندارد، زیرا همگی به طور کامل حذف یا منفجر شده‌اند).
🔴
همچنین، در پاسخ به شلیک هشت موشک توسط ایران به پایگاه نظامی ما در اردن، که همه آن‌ها با موفقیت منهدم شدند.
🔴
اگر کشور شکست‌خورده ایران به این حمله کاملاً موجه پاسخ دهد، بار دیگر مورد حمله قرار خواهند گرفت، اما این بار با شدت و قدرت بیشتری. با این حال، این بزرگترین حمله نخواهد بود.
🔴
این حمله بزرگتر در انتظار است و زمانی که به پایان برسد، تقریباً هیچ چیز از جمهوری اسلامی ایران باقی نخواهد ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144996" target="_blank">📅 21:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144995">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
آژانس انرژی اتمی: نمی‌دانیم در تأسیسات پنجم غنی‌سازی اصفهان چه می‌گذرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/144995" target="_blank">📅 20:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144994">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله مجدد به بندر عباس و قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144994" target="_blank">📅 20:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144993">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله مجدد به بندر عباس و قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144993" target="_blank">📅 20:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144992">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u15uM_6c0fYbX8KlFItqPNV9sKjNB20Hce5fpGiF3Ti83Eql3ClhUFfBNKu7N1wEY6Y-KwR9zMAv6nrUApwDBDEnZhDN4AsLmKvNcb4sMbXa4jWku14vnGMUtPkFprobM9Rclnj4d_Lp2DMtV2s3sgalYQ5falA_0oCwuUSZGq302XIGehqXM89UkeXWJoJHtJ_TSbHrUiOci9xeff4tRF_CEWZIqUEDQ3ewJXuN92Fkhj8cnHiodct4Di21yFyQnrLsLHj9PHxt2vvA94wF9fyPPGqLaNBq_t4hIr3WkY27HMQrgdyeITH--G5MGIwCvbmiktlV4qJ8lYil6bWz0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی: تصاویر ماهواره‌ای نشان می‌دهند که یک نفتکش بزرگ سعودی و یک نفتکش لیبریایی، در حین عبور از تنگه هرمز و طی کردن مسیر مربوط به آمریکا، مورد حمله ایران قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144992" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144991">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcUp-uOun41hX2ETZBmzzq77zRtFkUTmUnxzU_6STy3N316bi2kqQVaV8ppr6Mmz5O3jW1LCzl3GO_S46mSVSFiBT5_DQGDFJxZknWAB2zVPwyDf4pabHwtOOxdGv47etPoSpBmkKMUaLJFLgHAgosot_YaebfYcoGWvt7uP8XvKDe2luvRK2cA_W9Qgrg9IgkNEAzuLEz2GkjK9Di8GqlbuVqbsEoPdM61uBjJ6qW9PJNYqJ6pXLEfgV6jAzQ_DG33yM21Xq2OxZE0SrPYhKhD5X4PEQ-v1hpF67MyDFFwEbSY9Ia4aHamSd5Smn5Jz8FBFgSA5vnKR2_c1pvgr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت هواپیماهای شناسایی و سوخت‌رسان نیروی هوایی و دریایی آمریکا همچنان در سراسر غرب آسیا ادامه دارد و گزارش‌ها از فعالیت هواپیماهای KC-135، KC-46A و P-8A در نزدیکی خلیج فارس حکایت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144991" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144990">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
گزارشات از حملات جدید آمریکا به نوار ساحلی جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144990" target="_blank">📅 20:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144989">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فاکس نیوز» به نقل از یک مقام آمریکایی: حملات نظامی علیه ایران همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/144989" target="_blank">📅 20:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144988">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / اکسیوس : ترامپ و مشاورانش درحال بررسی طرح های حمله علیه ایران در تنگه هرمز بصورت بدون توقف هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/144988" target="_blank">📅 20:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144987">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: وظیفه من ترغیب ایران به توافق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/144987" target="_blank">📅 20:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144986">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
حمله جدید به چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144986" target="_blank">📅 20:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144985">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه الجزیره گفت که حملات آمریکا علیه اهداف مربوط به سپاه پاسداران انقلاب اسلامی همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144985" target="_blank">📅 20:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144984">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری /  مقام آمریکایی: تعداد حملات ما امشب به ۱۰۰ مورد میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144984" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144983">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRy6onhGKDqHQBiQgXCDRmhztEY12eYHY-upRG3XBqSxDElwgFb3r8C-JI1Sq0m_PJ4p2lOULltHlPSYMmk6QvlNGoRxvLEsAUIAHAyXjXz8CGt1oieK9l29XI8W56OjHfCBa8-UMo-d_kVG09egjPoQGnD8wMO4EiI59JZAg5oQudUsnHQUmkM5UqJSgjupCc8785VNMCDcCPMzYzcjwwyYFzE51At_4YjZm9PwujRof3mZGmo0m3_yWKzZAF6_lMktozqAbLmYmmkqBRFV27ljDkf-k6CcVsgbNefD8oYJ3xtHbrG1Wsxyo-QWgI68Ir97wJ2Zx53oJmJZ0K9M9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان آمریکایی از قطر و امارات به پرواز درمی‌آیند تا به هواپیماهایی که ایران را بمباران می‌کنند، سوخت‌رسانی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144983" target="_blank">📅 20:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144982">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
2 انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144982" target="_blank">📅 20:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144981">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
صدای انفجار در بندرعباس، سیریک و قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/144981" target="_blank">📅 20:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144980">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
گزارش ۳ انفجار شدید در لنگرود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144980" target="_blank">📅 20:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaF72EHx61hR3ZHGw2_cX-mnEonxqiIMuZEXx2XrEHv9np3euC2UpMMS-oisIUfEBYt70160nQnsY43ArbBndtJaYmaOomNb1tPUOCY0lsX-u1E_qwt1E6RSrl-pjVrBhr4uLL-l5gG7fi5pJVX8OCKKwAZFp-31ABD2Fn7G22odyibgDpl4NmKv1HUhZCoSZDBzFxw2Q4zMxQwGnF_fMrSCAz4QbUodrTd651CCzQJQ76NuqicykNp754GlQ8IAVoCxBe45IRXdEEvvxI4IKrpq8h6qmg7Ddh5lNEzpsL9_iW_6TJYc4g8pmXEV3nwKGuEMsSZwstmngRn88T_0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت آمریکا در اسرائیل، اخطاری را مبنی بر احتمال لغو پروازها به دلیل تشدید تنش‌ها منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/144979" target="_blank">📅 20:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
خبرگزاری تسنیم گزارش داده ۸ انفجار در جزیره قشم شنیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144978" target="_blank">📅 20:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144977">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سفارت‌های آمریکا در اردن،، بحرین و عمان هم هشدارهایی را برای شهروندان خود صادر کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144977" target="_blank">📅 20:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144976">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سفارت آمریکا در قطر: به دلیل تنش‌ها در خاورمیانه، محیط امنیتی همچنان پیچیده بوده و احتمال تشدید پیش‌بینی‌نشده وجود دارد
🔴
شهروندان آمریکایی که هم‌اکنون در خاورمیانه به سر می‌برند باید هوشیاری خود را افزایش دهند و از احتمالاتی مانند لغو پروازها، بسته‌شدن حریم هوایی و اختلالات سفر آگاه باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144976" target="_blank">📅 20:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144975">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مقام امریکایی: حملات آمریکا به ایران تاکنون با ترکیبی از جنگنده‌ها، پهپادها و موشک‌های کروز تاماهاوک انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/144975" target="_blank">📅 20:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144974">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
قیمت دلار به 215هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144974" target="_blank">📅 20:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144973">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
قیمت نفت برنت از ۹۶ دلار عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/144973" target="_blank">📅 20:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144972">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏
✅
️فووووووری/موج جدید حملات شروع شد
✅
@khat_akhbar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144972" target="_blank">📅 20:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144971">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKCakaulSxHShAo9mAUpfQkqsnqAYkvOnh_MlGzBVtQ8qWAHNL6meRFaQGSvbjnHuw5HZ2tZlWWphhIsjRWfgbsW0ayWP3kDwMGA4I6GJgGD3hQIHW9HM5vKJLAOcrljHAWyUQjr97DosCo8vn-An7qX6mHBveZ2sFlJw6qKipNoj1tuO37rnfFuUu9D8HdWVmuI2RiEwF2zU5H22mx0Kjnvctvn7zV54VcMXD-dPzo2tVK-rRReCbukozg2F6_zgc2NiPwRCH_Lkws3YvhUQTyxQlfaXF3eH7xpvFDf3WvpbwXukE6rBTFGBNLutZv2vtS1-Cq2ATzEQ1n4vNr8jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه سنتکام:
امروز، ساعت 12 ظهر به وقت شرقی، نیروهای ایالات متحده به اهداف مربوط به سپاه پاسداران انقلاب اسلامی (irgc) در ایران حمله کردند.
🔴
این حملات، در پی تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و همچنین به نیروهای نظامی آمریکایی مستقر در این منطقه، صورت گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/144971" target="_blank">📅 20:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144970">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سفارت‌های آمریکایی در اردن، قطر، بحرین و عمان، هشدارهایی را برای شهروندان خود صادر کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144970" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144969">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=a4nlctj4lfa1xYqwSUAqnT1KuUPLRhbLu0K5K9byEh9J-hUhGzArsG1slJuRriMi3oj6Sfmu0LHMYEJ9f7Je3NZcWhCAVXwUUNj77wVsKCOvJ1ZJOGy-CvgSTrkoK4c2ky04TUL5FH7Iu1-1H0Ha2ufk6rPPjcflWXzy5NWxu2F-_49vtkG0L_ngcHD37q5zO8wfliznwVn8SMKuFQeRb1GZp7row1euaR4LqmYbPnazv0c3nMQs4b-OmkQZlyWZ6KINrTOl_UsjFVjx4bUPcgkSrUi3OXCthuGpOW8-EZ00CS_g98a3_5u55Q70eEli9G6GwqUN07na4nFM0kuCiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=a4nlctj4lfa1xYqwSUAqnT1KuUPLRhbLu0K5K9byEh9J-hUhGzArsG1slJuRriMi3oj6Sfmu0LHMYEJ9f7Je3NZcWhCAVXwUUNj77wVsKCOvJ1ZJOGy-CvgSTrkoK4c2ky04TUL5FH7Iu1-1H0Ha2ufk6rPPjcflWXzy5NWxu2F-_49vtkG0L_ngcHD37q5zO8wfliznwVn8SMKuFQeRb1GZp7row1euaR4LqmYbPnazv0c3nMQs4b-OmkQZlyWZ6KINrTOl_UsjFVjx4bUPcgkSrUi3OXCthuGpOW8-EZ00CS_g98a3_5u55Q70eEli9G6GwqUN07na4nFM0kuCiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
فارس: به سمت کشتیای امریکایی تو تنگه هرمز موشک زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144969" target="_blank">📅 20:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144968">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏
👈
آکسیوس: هشدارهای امنیتی در چندین پایگاه نظامی ایالات متحده در سراسر خاورمیانه صادر شده است، به منظور آمادگی برای یک تلافی احتمالی از سوی ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144968" target="_blank">📅 19:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144967">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
طبق گزارش کاربران یک فروند جنگنده آمریکایی در آسمان قشم درحال پرواز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/144967" target="_blank">📅 19:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144966">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o22KZ_Hgqhc2dsHUY3PbD9hgePQiLH_dyx5fVpzMlk5MiHHgzuMex_BtjgT6yqXRw4AATQuVhW_-uUGOkEG4z37UZlh6zxB2wuDvIM_680DNYstg2-oUuxCGNewgEED3Ra_6mP7pUKAKFJiPFzWHMjGKNFjWHsAlStL_0_uWY0D40tRfqEYF3xIHYXjIPFjdlFBVJaoeihRWbtCdCmhJMCzwxDZu0vRFV-PJVezIPVBLkNA9offY6bnW9BvRClx450FYj74o-pn22jcdBXilteeyn1TBMhmYSAvDPf96rr7RuZ0Fwy3Fw9awwQ31Bxwk17Thw-od4YJW-nXIFBeq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نقاطی که تا الان هدف قرار گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/144966" target="_blank">📅 19:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144965">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
حملات آمریکا از بحرین انجام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/144965" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144964">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoxUXx54Ex-WtlfNU-CpsTC0NnBmi1b94XqmTHvHjU2X3TPGE9reKSrA0GyZ36AfRCkiVSQxkMTzfO61uapfv0w89yyH4UpTmDuV2pCwcUjKkhzzCHFbhXDVqWWlEYT1-fQ8sNMU0O9r9VXhQES9FqDq0e40BZysZ39Ey7O5bDR51Z5DnZDni5ZqD4kI5sgJmLx1kE2RhKeucIuZEU9BOP5Wxo5mvCgitYTT3QWOUV7yNJ7zOgFAZXHdQxZ6853pMRYtKm5xzbVyxdkgPeKS9EKMK-wTyTbsItVR-Yy-JZCRYdxtIIY_fcJFhUydXzBunE11YwpbMTkI32NYuEjOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/حملات با موشک‌های تاماهاک انجام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/144964" target="_blank">📅 19:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144963">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/144963" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144962">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144962" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144961">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری/منطقه پنجم دریایی سپاه بمبارون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/144961" target="_blank">📅 19:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144960">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/کنارک رو هم زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144960" target="_blank">📅 19:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144959">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری/بمبارون پایگاه شکاری بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144959" target="_blank">📅 19:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144958">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری/8انفجار تو چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/144958" target="_blank">📅 19:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144957">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/جاسک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/144957" target="_blank">📅 19:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144956">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری/سیریک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/144956" target="_blank">📅 19:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144955">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری/قشم رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144955" target="_blank">📅 19:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144954">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/چابهار رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144954" target="_blank">📅 19:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144953">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/حملات آمریکا شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144953" target="_blank">📅 19:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144952">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
گزارشات از شنیده شدن صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144952" target="_blank">📅 19:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144951">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7931d249d1.mp4?token=hN7Qpap3g47crMgg3Y37wdpF-iku3nHAsYteHA4ScWnHnRKQnfpD-FjzfEEwQ051uQZBwfDnxNEtqQvW_M0OaEzg95SAL_t0VKbdSitDsLX9lyysfCsTL19eq95hwLk2BXYLFPVs2qWge2UJW3PxCqawiFEzB-gHbBrnZTqn36lE6Y0UH-A5uARfNJnUIysDxkL9euDbFXzWvVhntBwwggT9ef9qhx8ekKhVs48UWI6jZCYytRv_2ntdPwZlfBGw5HF5wmRydxC_5HVahk4ZZcAh5SIc6glL0CFb98jyNnDIRtb0COUvuQI3g2s493M3KoFXqaWZ_JlKkdq1_ND4Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7931d249d1.mp4?token=hN7Qpap3g47crMgg3Y37wdpF-iku3nHAsYteHA4ScWnHnRKQnfpD-FjzfEEwQ051uQZBwfDnxNEtqQvW_M0OaEzg95SAL_t0VKbdSitDsLX9lyysfCsTL19eq95hwLk2BXYLFPVs2qWge2UJW3PxCqawiFEzB-gHbBrnZTqn36lE6Y0UH-A5uARfNJnUIysDxkL9euDbFXzWvVhntBwwggT9ef9qhx8ekKhVs48UWI6jZCYytRv_2ntdPwZlfBGw5HF5wmRydxC_5HVahk4ZZcAh5SIc6glL0CFb98jyNnDIRtb0COUvuQI3g2s493M3KoFXqaWZ_JlKkdq1_ND4Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت:
ترامپ هرچی زودتر میخواد مسئله‌ی ایران رو به جای سازش، تمومش کنه و ایرانی‌ها باید بفهمن که میتونن یه کشور عادی داشته باشن.
🔴
مردم ایران، مردم پارس، مردمان بزرگی هستن و فرصت دارن که دوباره به سیستم برگردن و دارن سرکوب میشن، ولی یه گروه کوچیک نمیتونه همیشه تو قدرت بمونه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144951" target="_blank">📅 19:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144950">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd39f7dc3.mp4?token=TAFq5Jepaat1oprOESbxLCQZdqnGH9crfR2vhJVJjKjhmpS87Jpcx_abMsmBkrMfXDtXLP-v4yzfxLLyWLr2TiIHxeOpYtBrD6q5QyhH7UfANAMIkDOWKo0aeWg00HDV21LVThh0oe8zAB50id0Q4x1scZTfdqeed1DqWZhnGDnVZy_AhuFmFPxscgDLP77vIuwPtTH4NgqGmuL5salF1T9AUVtzSJAi9UE55bBYE7jDpwOm9s5skUll7srtdoPpagZGnAbMC7PPz3at4kSrcKcJNgIQWHd8-vTHLxYpdqI6DKiEpDmtNhcQKt_pJDgTxFTokKoI2gOAd3UEwyURCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd39f7dc3.mp4?token=TAFq5Jepaat1oprOESbxLCQZdqnGH9crfR2vhJVJjKjhmpS87Jpcx_abMsmBkrMfXDtXLP-v4yzfxLLyWLr2TiIHxeOpYtBrD6q5QyhH7UfANAMIkDOWKo0aeWg00HDV21LVThh0oe8zAB50id0Q4x1scZTfdqeed1DqWZhnGDnVZy_AhuFmFPxscgDLP77vIuwPtTH4NgqGmuL5salF1T9AUVtzSJAi9UE55bBYE7jDpwOm9s5skUll7srtdoPpagZGnAbMC7PPz3at4kSrcKcJNgIQWHd8-vTHLxYpdqI6DKiEpDmtNhcQKt_pJDgTxFTokKoI2gOAd3UEwyURCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا درباره ایران:
دلیل عدم موفقیت توافق‌نامه، این بود که آن‌ها آمادگی بستن یک معامله را نداشتند.
🔴
وظیفه‌ی من این است که اطمینان حاصل کنم که آن‌ها مایل به بستن یک معامله هستند و آن‌ها مایل خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/144950" target="_blank">📅 19:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144949">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J4NGi4d1Gz_n3JuDaQ9mdybQC-DvvDGxLzofBaKhMlPeBzsr21i41HiiMswQRPP_jNZsj52KhYJYCrcKHUC7LgKrWmtm8zPtci9HEKfAlu5dA7aaJDsKzfOjtqlH98UINA-5NwFray-tUXNJUUxVi8R0ty10fFxoWxTyudVaHmYKWhHNI-dn4Cu0hGuMl5h5kA8VATbNnhLGk3PhaBWdEGY0vCOxLGlRuJQA_defGCfnA1C3bfwdY-seouAIjetiVKVwgUvDWiK55AuSQjwb3ZIm227IaZsls_LnQyMwgyy8Oy3_8Yepf2HMZVCbvQOUjaazNltMTawXth1YckMCkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز فرماندهی مرکزی آمریکا اعلام کرد که ۸۴ کشتی تجاری را به مسیر دیگری هدایت کرده، سه کشتی را غیرفعال کرده و دو کشتی را بازرسی کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/144949" target="_blank">📅 18:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144948">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5bbcb4367.mp4?token=VLOMXSvOMdVfO-lAyDWLudKqd2MfZ_yHow5V02LBTiD2aXWUvgdKrSpP91MrLuWhQzgCcP2g-7W6NEfU5H18JSszJT0nBydqYDFCSgw9pF3ZG2kqgcDdXDCSpfFdeH_9o_aRxcmPXMTBpGMZSXqFZ1_bUSFDor_Kv1lt2kVFmvmarU0WoEMm1_0Ike0T8VZKzdIGFQZjaNlcT0L18U5YPWxEmjGPny9TFdZXpi13vqcS-dlnBGucqy3cpWKwyCguPJ13xadJzsxdJ1M3VxFWrhwgD7oeDtweq0BNqWiPWKoWYjwtv0QYytTBg4poRdyrdhLek-Fjlj5cRhMHK06NMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5bbcb4367.mp4?token=VLOMXSvOMdVfO-lAyDWLudKqd2MfZ_yHow5V02LBTiD2aXWUvgdKrSpP91MrLuWhQzgCcP2g-7W6NEfU5H18JSszJT0nBydqYDFCSgw9pF3ZG2kqgcDdXDCSpfFdeH_9o_aRxcmPXMTBpGMZSXqFZ1_bUSFDor_Kv1lt2kVFmvmarU0WoEMm1_0Ike0T8VZKzdIGFQZjaNlcT0L18U5YPWxEmjGPny9TFdZXpi13vqcS-dlnBGucqy3cpWKwyCguPJ13xadJzsxdJ1M3VxFWrhwgD7oeDtweq0BNqWiPWKoWYjwtv0QYytTBg4poRdyrdhLek-Fjlj5cRhMHK06NMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا کشوریه که هر کثافت کاری رو میتونی انجام بدی اما اگه از حکومت حمایت کنی بخشیده میشی
@AloSport</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144948" target="_blank">📅 18:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144947">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
دلار 214000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144947" target="_blank">📅 18:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144946">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
خبرنگار حوادث:
هفته قبل یه پیانو رو توی دیوار آگهی کرده بودن به قیمت ۴۰۰ میلیون تومن و وقتی زنگ میزدن به طرف پای همون گوشی ۱۰۰ میلیون تومن تخفیف میداده و مشتری ها رو راضی میکرده تا بیان پیانو رو ببینن؛ وقتی مشتری ها میرفتن اونجا بهشون میگفته مال پسرمه بهش نگید خریدارید تا غصه نخوره فقط برید کارشناسیش کنید و بدون حرف بیایید بیرون. وقتی میپسندیدن و میومدن بیرون؛ طرف میگفت ۱۰۰ میلیون بیعانه بدید و شب بیایید پیانو رو ببرید. ولی بعدا مشخص میشه طرف اصلا صاحب پیانو نبوده؛ بلکه خودش این پیانو رو توی دیوار دیده بوده و به صاحب پیانو گفته میرم کارشناسای مختلف میارم تا این پیانو رو تایید کنن. بعد خودش همون پیانو رو توی دیوار آگهی میکنه و مشتری های خودشو به عنوان کارشناس میبره سر پیانو. تو همون روز سر ۱۰ نفر رو اینطوری کلا گذاشته و یه میلیارد تومن جمع کرده و فرار کرده.
هر آگهی دیوار رو که دیدید قیمتش خیلی پایینه یا خیلی راحت تخفیف میده بدونید مشکوکه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144946" target="_blank">📅 18:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144945">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80781901b0.mp4?token=SjHZ8i47K_q47feHNSEdVGEIUBr4jymHmv32Y02qaVJ-tY3VuKGDL6_dCl8hpxRWb2bPfsv0MU9-uebNIXpwAwxHlLEYo0mmi7gvbHKnHPENkRYx1P57LYfsxBK3RUC8tsqXHDzKx-tvmrSlhBmZgIIBy4OHE60MEOhnn2goKe-0WWLnvDditLpjx4NQPKpj3_mUGsI_uAa_8LpIjxIiw-MI0z2ZyaCyaRMRwsXFKKx25jJQqeVXmKBp-90nIxO-smkqfmVEFH-ZEwr2YJCIj2nVym81ChHMVtUIprTceM0Q-YF_oYjyFcv7VfILySFCLBWpNEQIpx5AeaQ_5EsDB5AeCji4k1EhUttUQwCC5cM9eTaA2slpbGPz42KAiPWq5XSPyCMio2df34wgeKF3jX1vsw7fdrvHzZXSNMohLdDTAq7emWdekTo5xr9CM8p3pY3ueCQQWk_ZVGtT8drxIsd_fCNDS3Vp4Rl4PG85fdr2jX_y7neV4QifWCdW10STI5DB3-GfT4SWcDfasBdmfNWQ-nhgCkmYKD3ZN-rw2mnSh3-bN4afJ-sZ91ILAcH2QVQvHnesrIb7jQiQghP_4psKvl9ayk8zy0LTsdDf8nGaLDnIdVEOR0zu9fKYhhL11w1wibIThE6phMQXO1EOLUhfB-MWjz90wUA4PYi-ERw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80781901b0.mp4?token=SjHZ8i47K_q47feHNSEdVGEIUBr4jymHmv32Y02qaVJ-tY3VuKGDL6_dCl8hpxRWb2bPfsv0MU9-uebNIXpwAwxHlLEYo0mmi7gvbHKnHPENkRYx1P57LYfsxBK3RUC8tsqXHDzKx-tvmrSlhBmZgIIBy4OHE60MEOhnn2goKe-0WWLnvDditLpjx4NQPKpj3_mUGsI_uAa_8LpIjxIiw-MI0z2ZyaCyaRMRwsXFKKx25jJQqeVXmKBp-90nIxO-smkqfmVEFH-ZEwr2YJCIj2nVym81ChHMVtUIprTceM0Q-YF_oYjyFcv7VfILySFCLBWpNEQIpx5AeaQ_5EsDB5AeCji4k1EhUttUQwCC5cM9eTaA2slpbGPz42KAiPWq5XSPyCMio2df34wgeKF3jX1vsw7fdrvHzZXSNMohLdDTAq7emWdekTo5xr9CM8p3pY3ueCQQWk_ZVGtT8drxIsd_fCNDS3Vp4Rl4PG85fdr2jX_y7neV4QifWCdW10STI5DB3-GfT4SWcDfasBdmfNWQ-nhgCkmYKD3ZN-rw2mnSh3-bN4afJ-sZ91ILAcH2QVQvHnesrIb7jQiQghP_4psKvl9ayk8zy0LTsdDf8nGaLDnIdVEOR0zu9fKYhhL11w1wibIThE6phMQXO1EOLUhfB-MWjz90wUA4PYi-ERw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان، به پوتین: قدرت‌های بزرگ، صرفاً به این دلیل که قدرت دارند، حق ندارند بدون توجه به چارچوب‌های بین‌المللی و قوانین بین‌المللی، به اقدامات تهاجمی دست بزنند.
🔴
اقدام تهاجمی که ایالات متحده علیه ایران انجام داد، هیچ مبنای قانونی، هیچ مبنای علمی و هیچ توجیه منطقی نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144945" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144944">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9df57a2bc.mp4?token=BbN-wZtcBifJ3lIwluV8ITQ0lRIhtqzDgnYRtO5lwreiC6FTr4AZ1F2o30Ic14IgFb0k4oa2o64bakCrglvN0328gB5pencch9GEhM4_3Rq9Xr3er2Q3nduSa7ckpCQyIE9mTSJKoWqi9Ue1q-Uch80gLSfGOLvtyFf64vDn6SPp3p5dqsQgtBno4Kk9xBlzKI0xnEWvZpxxWYrbto6HU0L2Pmgrvcey6bny8QFB5ayKHvdDdiWnQugfqjAC8KfX3Ny4aagWsBxotQyCLSTvIajnqkxG04BHRwVZB1CUTvDx1XCnWkKeHK2FM1Gtonl6UeGwizUUYFt7MTIbzexnbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9df57a2bc.mp4?token=BbN-wZtcBifJ3lIwluV8ITQ0lRIhtqzDgnYRtO5lwreiC6FTr4AZ1F2o30Ic14IgFb0k4oa2o64bakCrglvN0328gB5pencch9GEhM4_3Rq9Xr3er2Q3nduSa7ckpCQyIE9mTSJKoWqi9Ue1q-Uch80gLSfGOLvtyFf64vDn6SPp3p5dqsQgtBno4Kk9xBlzKI0xnEWvZpxxWYrbto6HU0L2Pmgrvcey6bny8QFB5ayKHvdDdiWnQugfqjAC8KfX3Ny4aagWsBxotQyCLSTvIajnqkxG04BHRwVZB1CUTvDx1XCnWkKeHK2FM1Gtonl6UeGwizUUYFt7MTIbzexnbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر پزشکیان: در مورد یادداشتی که ما امضا کردیم، ما همچنان به آن متعهد هستیم.
🔴
اگر ایالات متحده به همان یادداشت بازگردد، ما نیز طبق آن عمل خواهیم کرد.
🔴
در آن یادداشت، ما چیزی جز حقوق کشورمان را درخواست نکردیم، و این همان چیزی است که ما در پی آن هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144944" target="_blank">📅 18:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144943">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
قالیباف: اگر محاصره را تشدید کنند، حتماً پاسخ نظامی می‌دهیم و همه ضرر خواهند کرد
🔴
دشمن در حال حاضر در جنگ اقتصادی، بر روی جنبه روانی آن متمرکز شده است
🔴
بخش زیادی از تحریم‌های اعلامی جدید، قبلاً نیز اعمال می‌شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144943" target="_blank">📅 17:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144942">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
یک مقام کاخ سفید به الجزیره گفت:
رئیس جمهور ترامپ تمام گزینه‌های موجود برای برخورد با ایران را حفظ کرده است.
🔴
ایرانی‌ها می‌خواهند با ما معامله کنند، اما مواضع آنها همیشه دیرهنگام است و از آنچه لازم است، فاصله دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144942" target="_blank">📅 17:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144941">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: احتمالاً این هفته و هفته آینده، تحریم‌های جدیدی علیه بانک‌های ایران اعلام خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144941" target="_blank">📅 17:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144940">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
رشد اقتصادی مجدداً در حال افزایش است.
🔴
رشد اقتصادی بهتر از آن چیزی بوده که انتظار می‌رفت، با توجه به تنش‌های موجود با ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144940" target="_blank">📅 17:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144939">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914636c9fd.mp4?token=j16SRhA3959IxtvFrKc5Mww3bsltm7Lk-UpdXRfKmK58t_XOf_p4X6dYfBne3FCuV1-Fg4Up5XGRAWGYu6uRYZoUwmnDHMMyCvhEtnYjsRUA9HywW-AYxeUv2uSfACcKq1tgOJ1x6LxU-F92EgvsO6Zdettdmt--Fq35MNGkKtAg2Q1BxUYFOwOuHEJwN7Jbo6GW7hTHEtXpevMM_Mn6JIEw0yJxpTCcZ3RkxlsIxdgagecyVrIr9Glvu9kwKXxSrM0SLkKR2ZO-hDcdEuGELd-a9og93RbHnhDd61xHPqIVFIYC80OROA0I9SfGpxGp2Whipy_ERSM7dEy-puwMxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914636c9fd.mp4?token=j16SRhA3959IxtvFrKc5Mww3bsltm7Lk-UpdXRfKmK58t_XOf_p4X6dYfBne3FCuV1-Fg4Up5XGRAWGYu6uRYZoUwmnDHMMyCvhEtnYjsRUA9HywW-AYxeUv2uSfACcKq1tgOJ1x6LxU-F92EgvsO6Zdettdmt--Fq35MNGkKtAg2Q1BxUYFOwOuHEJwN7Jbo6GW7hTHEtXpevMM_Mn6JIEw0yJxpTCcZ3RkxlsIxdgagecyVrIr9Glvu9kwKXxSrM0SLkKR2ZO-hDcdEuGELd-a9og93RbHnhDd61xHPqIVFIYC80OROA0I9SfGpxGp2Whipy_ERSM7dEy-puwMxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه، اردوغان، به پوتین گفت: روابط ترکیه و روسیه امروز در سطح بسیار بالاتری نسبت به هر زمان دیگری در گذشته قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144939" target="_blank">📅 17:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144938">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6df48cd02.mp4?token=rRdg2xQdHz6oOhmN2aAk1UyxLsYvkAPGCYVSygUZmaUj02pYkOd5jrJgIz4WatjXI3razy7djqicHSVsPm5-TO-7msDe_Z5PhLl8qxtySZ_wNRmb2dvDySCk3Xd1DAkFbz3Z8dsT2RWLOooV-PfksaksN6JOVms3P-uswurwFKp5hwZesuPxMhmguW9whVnp6KcMiXcATF-QV2qcH1-Q6dfDVqbQ1zwNLewnahP07iNsJyk3L6AqyH1K8tagKBBeZCH6k1Y1tLWoh-ehvYyS3D1VhrC2EOAxWEtKeZMUnulnVK9h-QD6_SwE-2AhGBgSJT6BzZ27IA4je1VCMwifrL_-l_CzO00gdwwZ70Ujs_XWsJnbys13YfbV0dTPueKGJ74UIAM8FbnDB6KGeZHQjkf-pFntnfTctUhLdmrpJXKR94EFH43IT9CYD5C9uNJWs6F5c1Wb2m6ERcrtYPyH0LjeNRSKnhhsUUkPRPquAWcqgXYWhEhRcYLHwiBmSuqbkLey3hdexfjPvaxttkZxxP7G2RKGDQn_ODPCTeSi70f-D6V9vtAsnK6AgtNNfv_Oka9d1caM2ZAYP4_x5zeKdhh-k-v-GXqbodPW5CwWqw99BLtLDZWxqJsjfPtiZmlkpygrXGBpyeGVbd5f_jtMqNeD-qkR_sEJNLf-8n5RlMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6df48cd02.mp4?token=rRdg2xQdHz6oOhmN2aAk1UyxLsYvkAPGCYVSygUZmaUj02pYkOd5jrJgIz4WatjXI3razy7djqicHSVsPm5-TO-7msDe_Z5PhLl8qxtySZ_wNRmb2dvDySCk3Xd1DAkFbz3Z8dsT2RWLOooV-PfksaksN6JOVms3P-uswurwFKp5hwZesuPxMhmguW9whVnp6KcMiXcATF-QV2qcH1-Q6dfDVqbQ1zwNLewnahP07iNsJyk3L6AqyH1K8tagKBBeZCH6k1Y1tLWoh-ehvYyS3D1VhrC2EOAxWEtKeZMUnulnVK9h-QD6_SwE-2AhGBgSJT6BzZ27IA4je1VCMwifrL_-l_CzO00gdwwZ70Ujs_XWsJnbys13YfbV0dTPueKGJ74UIAM8FbnDB6KGeZHQjkf-pFntnfTctUhLdmrpJXKR94EFH43IT9CYD5C9uNJWs6F5c1Wb2m6ERcrtYPyH0LjeNRSKnhhsUUkPRPquAWcqgXYWhEhRcYLHwiBmSuqbkLey3hdexfjPvaxttkZxxP7G2RKGDQn_ODPCTeSi70f-D6V9vtAsnK6AgtNNfv_Oka9d1caM2ZAYP4_x5zeKdhh-k-v-GXqbodPW5CwWqw99BLtLDZWxqJsjfPtiZmlkpygrXGBpyeGVbd5f_jtMqNeD-qkR_sEJNLf-8n5RlMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: دشمن پس از شکست در عرصه نظامی و دیپلماسی سراغ جنگ اقتصادی و شناختی رفت و آن را به جنگ نظامی خود اضافه کرد
🔴
محاصره دریایی به معنای جنگ نظامی است
🔴
هدف دشمن از جنگ ترکیبی این است که در داخل کشور، اغتشاش را به همراه ترور و حملات نظامی کوتاه آغاز کند
🔴
نقشه دشمن برای همه مسئولان ما روشن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144938" target="_blank">📅 17:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144937">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
کره شمالی، خواسته‌های ایالات متحده برای خلع سلاح هسته‌ای را رد کرده و اعلام کرده است که به تقویت زرادخانه هسته‌ای خود ادامه خواهد داد.
🔴
پیونگ‌یانگ تاکید کرد که "سیاست خصمانه" ایالات متحده علیه کره شمالی تغییر نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144937" target="_blank">📅 17:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144936">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fd2a26f4.mp4?token=nU-_H8BPzqFUBamVqmCkPe0Ex-BTNnd0Xp3CekRGessANm3P_PM1BQZ8hHZPPhZy3qQtgwolPo_8TxbbCwlV9iTvPwhpCLrGDE4ww5BNFUlWKPVFKiRp-wiyKr4C-AmoANj8M2xD78DjF3mHx4esqI0plCWx0YpMeQLMLfoYlSy3gMqklR7fnWM7sCltwaPX8FwICC4udDnFtHFlN5avQqO7p3D54ure1mRHs8VUfSXfp_IiAt150yIXgj7yGzVkxfVho_qrks5FPVrsuBMKmD7iI5dzS1uy2OCPh2NY5sqCh83kL4O96HwVzVEHjpD34pENnWvb1C4xjWShyDKFnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fd2a26f4.mp4?token=nU-_H8BPzqFUBamVqmCkPe0Ex-BTNnd0Xp3CekRGessANm3P_PM1BQZ8hHZPPhZy3qQtgwolPo_8TxbbCwlV9iTvPwhpCLrGDE4ww5BNFUlWKPVFKiRp-wiyKr4C-AmoANj8M2xD78DjF3mHx4esqI0plCWx0YpMeQLMLfoYlSy3gMqklR7fnWM7sCltwaPX8FwICC4udDnFtHFlN5avQqO7p3D54ure1mRHs8VUfSXfp_IiAt150yIXgj7yGzVkxfVho_qrks5FPVrsuBMKmD7iI5dzS1uy2OCPh2NY5sqCh83kL4O96HwVzVEHjpD34pENnWvb1C4xjWShyDKFnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: در تنگه هرمز علاوه بر اعمال قدرت نظامی،
در عرصه دیپلماسی نیز پیشرفت‌های خوبی انجام شده است
🔴
توافق با عمان، به‌عنوان کشور ساحلی تنگه هرمز، با دیپلماسی به دست آمد
🔴
قدرت نظامی ایران در تنگه هرمز حفظ و ارتقا پیدا کرده است
🔴
اعمال مدیریت ایرانی بر تنگه، هیچ منافاتی با قوانین بین‌المللی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144936" target="_blank">📅 17:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144935">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: در 2 سال آینده، تنگه هرمز به یک مسیر آبی بی‌ارزش تبدیل خواهد شد و نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144935" target="_blank">📅 17:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144934">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده، بَسنت:
تحریم‌های ایران ممکن است بر شرکت‌های اجاره‌دهنده هواپیما نیز تاثیر بگذارد
🔴
ما گفتگوهای خصوصی با چین داشته‌ایم. ما در حال بررسی همکاری با چین در مورد مسائل مربوط به ایران هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144934" target="_blank">📅 17:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144933">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cdaf5608.mp4?token=dmRkCqQNvJyV8sBx2F1Uiq_meD2dg63MkU5HLyu57AciTNu_nBe4yQjfnrUPk6P6PJFILjaFoKEd1fTilrLSG8uHdhIMRbZ4w6qL3MUMQvw3Dbxgaxq5VVuwyxbzR0g2pWxt44LQ8EUA7Lo9dcY5Odg9tX9r1vh46l1p8CAm2ZeBCp5BFAHuRcbpxf_pHwbYGVLIrsIV8L4KG9NQzq5BUrpg5E-erlf0bDvl1Ingq3vLT63TMI7rzM4VoglO2_teJFeRRA5g1iC_O-SFOrGf5665DzOkONHGONzgCqCa-AQlZ7IA4acpbsnwGY0vOfnoxbpqFDcQWr8DSn95mmdOZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cdaf5608.mp4?token=dmRkCqQNvJyV8sBx2F1Uiq_meD2dg63MkU5HLyu57AciTNu_nBe4yQjfnrUPk6P6PJFILjaFoKEd1fTilrLSG8uHdhIMRbZ4w6qL3MUMQvw3Dbxgaxq5VVuwyxbzR0g2pWxt44LQ8EUA7Lo9dcY5Odg9tX9r1vh46l1p8CAm2ZeBCp5BFAHuRcbpxf_pHwbYGVLIrsIV8L4KG9NQzq5BUrpg5E-erlf0bDvl1Ingq3vLT63TMI7rzM4VoglO2_teJFeRRA5g1iC_O-SFOrGf5665DzOkONHGONzgCqCa-AQlZ7IA4acpbsnwGY0vOfnoxbpqFDcQWr8DSn95mmdOZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: آمریکا می‌خواهد برخلاف تفاهم‌نامه از مسیر جنوبی تنگه هرمز عبور کند که این اجازه را نخواهیم داد
🔴
قبل از جنگ، روزانه حداقل ۱۲۰ کشتی از تنگه هرمز تردد می‌کرد و حتی اگر یک یا دو کشتی هم از تنگه عبور کند، به هیچ عنوان قابل مقایسه با قبل از جنگ نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/144933" target="_blank">📅 17:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144932">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC185cPi83w8BYzXx_ZlwVIePI8u5W0Dp7NQ819-24bVuxfJ2JGuANNifMehzphkGGXW7MuEMxe96NmUNLCk-Fv3xaqqEmmdz6VZ1SVzEJLosBqX4RN8MKxni9K5RpDjunQZ8BxwNSfItluJ9GhBjBIG45pHFrhhSnQbFb0-tiIDCRSBQuflagDHSQvQ4SLcqgMXTlG7wquFkvN5Lfqds_f9bRt38qxbqf5Ja47Fb9pb5TSBgPqA93vASZntL36uENMR50xVIQUDBm5le_Q2XXiCFdPh1lxDM7pFEOfL7-2tKoVwEhqSyePhpCvmNUqHY6dox94c9OZr1p7Xv0euBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: پاسخ و حمایت عالی و فراگیر از سوی هر دو حزب در کنگره برای طرح احیای صنعت فیلم، تلویزیون و سرگرمی.
🔴
ما این صنعت، که زمانی بسیار بزرگ بود، دوباره به آمریکا باز خواهیم گرداند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144932" target="_blank">📅 17:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144931">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ایلان ماسک: هوش‌ مصنوعی تا ۳ سال دیگه پزشکان و جراحان رو از کار بیکار میکنه
🔴
چون ربات «آپتیموس» از بهترین جراح های دنیا هم بهتر کارش رو انجام میده. دانشکده پزشکی الانم بی معنی شده و هرکی داره پزشکی میخونه فقط داره وقتشو تلف میکنه.
🔴
پ.ن: این ربات میتونه به جای تمام متخصصین تمام رشته ها عمل های جراحی رو بدون خطا انجام بده‌!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144931" target="_blank">📅 17:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144930">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
مدیر عامل توانیر : خاموشی‌ها تا اواسط شهریور به تدریج تمام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144930" target="_blank">📅 17:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144929">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ماکارونی گران می‌شود
🔴
ماکارونی تا پایان مهر بر اساس نرخ‌ مصوب فروخته می‌شود اما از آبان و همزمان با آزاد شدن تامین گندم صنف و صنعت قیمت این محصول تغییر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144929" target="_blank">📅 17:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144928">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
قالیباف: در ۱۵ ماه گذشته، به اندازه یک دهه پیشرفت در حوزه نظامی داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144928" target="_blank">📅 16:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144927">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZH3QPzREbYix1lIDQexMzTrqS333Z1UVZLzNVu5Xe0yNQo-NaR2cPG08AAgLZeKnMQTjb48rij_vTxuXTHhBB5I7aXesb4EK9VhzSFVq5V08P0ze5Zi09vftzhwnB8Yl80iqEKIjuxXe2CUqmUBLHEgqpnD163sBqy_LMMcYLjHW8_jUXqWGxeFu4RYQ-JXpNeZ2VfWBa7nM6YmDNEcWHpmjo8ttT0JlzmsYLWrMaGpa_s2SqfalZ-q8LO-eJQEeC5ffRBIWfqFwCWNT7KaGIXjQRukbFIyW4phhAqKgTcecA3ZqNB64-dVpO_fmghgDAoZ2Hj5ZPUqf4xT45BSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه آمریکا با فروش احتمالی یک بسته تسلیحاتی به ارزش ۸۰۰ میلیون دلار به عراق موافقت کرده است که شامل بالگردهای Bell 412EPX و Bell 407M و تجهیزات مرتبط با آنها می‌شود.
🔴
این بسته پیشنهادی شامل تیربارهای سه‌لول GAU-19، راکت‌اندازهای ۲.۷۵ اینچی M260، حسگرهای الکترواپتیکی/مادون‌قرمز L3Harris WESCAM MX-15HDI و سامانه‌های هشدار موشکی AN/AAR-60 Block 2 است.
🔴
این قرارداد همچنین شامل تجهیزات ارتباطی، قطعات یدکی، آموزش و پشتیبانی لجستیکی خواهد بود. شرکت Bell Textron در فورت‌ورث تگزاس، پیمانکار اصلی این قرارداد خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144927" target="_blank">📅 16:44 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
