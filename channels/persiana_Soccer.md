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
<img src="https://cdn4.telesco.pe/file/ggGghNIMJQL5jo3J_LRLvRdDmkejktCp8maJjdyhijlzEUsprybG_GTi5pUJ5US4FTg41QB9Q_Mvv06jZZpUZIx-bh_jkSlS2QTN4C0ymx_pyfzNbQ5jAZSnw_PK4Yh2HktpOwN9EA06QcPGn9QhqOrO_b4iZYO0hAWgxZlqCILGFhHqRLKrVeA7zlkJkU-3taHbWWyJLNF4Mqo_PPdlAeygH_r7bK-hkQmeFu0jawB7Kd3Bs6f_q4ixiFfAJ945C2i8bS-z2IvXWKAAKRNH2y301DwzN2KF01bfpWSC23aXZguUjBqAxWpHSafm4Eg3cetBmk9BJGx5SZon7MLQtw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 209K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 05:42:52</div>
<hr>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuR8yUjKm4Sr07tFi4oEFaIC-DD8AgWzwbcg1grdcEmnO4U8oWXeTaxPpkV4mUf-nQRgA38KOuf7pi_pYc3dppnHtccZNuBVFfTuYR_H1FdMjQwhPnNBrHMTo63cft4BYYRkNw0njidWX2wUdE9y7hXRQhIJ3sJW2CCsLFnpKicCafvw8WkNlts0NDCUH9kFVWR3JYcdTfxp0RSpd_ItypCJWrGaFhBA2H0f91st-3M8SCXQTKX3Q0rGsNZT59Hh6zx3b8vM04BBs4WCAPDH471a7jVr5hHyuNaN6bechX_G3FUOdpBsQx2QF3lSi9cWyPIniga4PwHEsDYuipJgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzX5PQf1aB-sUGiiC4kzqBd1igphy4wrzkRlFVgFcBOXxSxFor7lOQn0L6f0w4Rw54HgCzCV48VZYoma4IyLE0-mahJX5fVJj6dCPm__Tq1TXzublHzJyIe-0aey7azdPzxJzvpgadmBvc1a3S9_7w8z9AXPDwvm6jGxXKx5JzBIePKJq3dBJgT-BcSdztzOUWSQ1ggu-cmydW-ZLlqzXNU50X-H3O0xPIvYFHcqRiP2dFudgfYuCGcv9DSBORZqMq6VibeI8t5czCz64h-QDeUChiBXQuAi_cjGWE4qN3-7Wof1cWOhAahoeaXLc92h6vwGlG8hRIax_obuR2_muQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTvBdT5O3he3iXNQ_T9TkUAgpxvIgdlpLBZChjlykofWJjixvIFmx1qHRu-xSuZ5AqUt1-Q7-PTehOTzRmNHNeHXHlo3HnDw65l9r3ecNNpUveOi30xxiK5FYUk36izdi8hhp60R3RMIIcUY4d3iCKVuv1LzMapRksfWvGjDwZCxPciSZ98YBWU8vC6lRV8j0tzIW878ozVKey2pcnuZoUA-9bF1tZaRK4Z171PYRoID7P-DGPtDjL-tewyjydP8qibLAI6aDF4uTZJbPBgFayyi4-ozSi8q_da64MUlvuVLzPZ47RGdAOJeYkDxQarxOOImyR1pjPq8JPYq6vy5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22155">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az2oeAI1OVjGLCQmFibqwZ3tAFSTzzHyge8dnH0x7SeMHu_jtNJqVxfOGTfNDWw3ipASw381bovjfOZcnuaIaCp48JL6QyHOrOA8uiUKjgFUL8etNkGtPS_QCa6F0Ee9PInin07Jd3eH3_f545qnXq9yydro5qVVmjJgKWpQ4E2NQeeXoi4DHlCeI5MEgdtrPMru_P0O6bMXs_iToY7Da_IUIJAD9-yLAHKSEXeQnrnt8PgAxYjW4wqmjbAM5tXJSSkVEctzjCZKYN1bJVbacU76fg4_Cx_58YbGTuv6CkfEttNufT-BUIPyl9Kv5dVFYEgHU7OUwOg4nUG8OU-VBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورودی کانال VIP بتمونو رایگان کردم
؛
خواستم یحالی بهتون بدم هر کی جوین شه تا ابد میمونه
💯
https://t.me/+--L2Hz5HpiY1YWZk
💎
#تبلیغ‌نیست
💎
👀
کانال وی ای پی رایگان برای همه
👀</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/persiana_Soccer/22155" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqKsLyRRxVSosebzIb8FQZxOWO7o13EJh-l2Tfn6zD1LQ7ae1lbzRsexwJi3zSzVuzDUC7khoIRQsIpQarlGgSO2L9TM022XK8rmNztMIVblIITuLGHlC80Tm9STroRjp84zWCT_a3LhABi3x_6iq_tHLltl-WmZB-CvMOigbyGVSfCwTQ3UOTC8tkV5hKd7IRNRUFjIl6VNWW-nQgti-1JhWDzNZlVh9Clu0jc3kQzki9jv-GUumXhTvRNS8yLz56FSDba-A5wRfpJzI4_nQbU8esbn5sqw4pP2r9JFqFF9d8BZu5H06t4UhH637LO4_cdjA93ee3LbDkZ0b8uMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8q6zx_HiEuM0S0Y3TUDI-pbISV8MlBq7bo2l4fOmC4edY8UlTLzN231YEHsL43Ajd2FAohHDC7k8dp2sjSlP0MUXS9uMaVjX6tn3GxTlNWtmVP9ugzX7Pp85_mLGgD2TZ5LSyNsNXiFbXOCJcptoVzrSvGAoaRWgRfRh_Qw8E_MNchTFkAmekPNmXKlEaGcXaTTqBvGsPmiYB2CZzalsfLu2tTvw6wBKguyCUICzEb1YrGbgAtowcEHES31RkjUtDQC2T1eDIUDhanZinx0TcBGxpfrymLNlFFHL51LAzBY6th0-m03gvzW7fBwhKIIZbpICZrCnyzGFWM30VTFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMk6Uw_Y14ZEF_EupnPjaL_-Sw4A0rez3d3N2Y0VTt-P8sgk1vzwMB7uHWgK0UXyyhP_5OHWrHtCUQl6-nYL_rApdQo67ovAPQ4_xKkgGFEgGeX893dgMLm8H7QhnGA4ey7FqRsqQRlK0UF0_6BqbLYjwEw6O6EGMywrc1-Mp3fh9Ov4xUXoyfcAd3spiIKO88PbAvrytTrD2-l4_I0I-2c2Exg0pbMNEixwwCg0IkSSdg879N__HWFvOEdrsvmTzCmoXxPQKx-scGJVXtodPQNU7VBo4gHeuSU4ZT06as_t3GmRJgJiJNil953_IjgZNYRKRoBZiNgow5SBSSLEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkfivIllaoio5IAlGjcXwTHtTow38Hvmo9GumBdwuOdF36HgnOV0V5wQX8qqU6Ac_rvgm9uZn0rnZ_nzA8huoMke4QfzlAGUidkAt1Ut2MdkFSls7QpYnNacIQjQxrYnMB5_FXmpMKLBWzSMxOOHncf9t0ueuuJ3s1vdsdEC9ZxyEpZG2YWSp2Sg1bD71xFxN5Hvgta0ToASK1zSm5VKqOSsxXrGmhRYaEMM0RxTIkMt3seBKR1NmTp9c1TXiq9rsa4w-7fETVKt2p4JF3uRXq8pY8QUNK8R1bMkj-ReCy6hNvtHd-kEjpgGJTLsUSQEnv-Gh6USsJzzc4MMzPDNgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22150">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
⭕️
⭕️
بچهای پرشیانا
باعلیرضا صحبت کردم هر گیگ کافینگ‌رو ۲۱۰# میده‌سرعتش واقعا محشره اینستاگرام توییتر تلگرام به راحتی بالا میاره
✅
تضمینی
✅
بدون قطعی
✅
بدون ضریب
✅
به همراه لینک ساب
✅
سرعت عالی
اینم ایدیش برید هر چند گیگ لازم دارید ازش بخرید پایین ترین قیمت تلگرام میده
👇
@Alireza_mosve</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/persiana_Soccer/22150" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5WmAy2L3npaHKzYY90VST8SGb4HkQTQyKmmeyWEe5VtEL4sVGV9QAtncPC8cZQst9ZFD4fb8fCo9fliMYHeq_oC1CbQjY8IFfkdbKsnCULpkTZAUrxSxCtTPoeh6JVVHfT94oOrkvMAoYrHFsc4FooV5MxaHliOtTc6tcpoTfsWXxEDMH8IWmay8MYHR_D2usA6rZuwfdwOXSdptYV-1o2RIxalerxfldI5CeD3UPbrEIhrKEGtwWAG0C022tPz68yh7OuaTNpSGO4tXhkkYZnFIgLqbItFpMn4TxVgahcsReDGTiXb4QGTJ1OIPM7xsusSs9GpEm9C2Gotr577fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMUguFVPyTCdzuLRKZC2CY8Hd2li6CVPAdckTgYCgE0OFOqSzcDK7YUeBbFQYM2fXZ12tFO1j3uK3xrl8Ww9i9VK8ORxfnP3QHli6pDSZ8ztU77zn8DYBAFeLSmnYD2_zHY6h183nwnoZ_93oF1gdV5vsC5-uF3FWnwgF4sGjGUIskhZDbuoAo_YlKvnGvLh9fYCAeP5bU1Kx8_bLCf74vMbr40k-UdRhCB7inp6eP6Traoh0iyNIMQ1SzrI_qfz9ho55dWF_5CrBPbY0ebTmCEatfZse99zG08ZN6FG4d48SMOQucQiq_kcRbVEf0-Q3HSjKp0_7vMrspqbQ-40XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0peYZ67qDJI96UqBFyZzEknSGTpBXoQpbltrLVztRo4HDjFzvhhCUlFniDosQ38wfPMROFAMgTdPObYvDTNMJyGgIJQBsD644cJtUwvzgjDKDqbOcKXzoPOk4QMMkgdEgJVfqnQmihk9KpYROs2XAxZNq96oC4NJaJ30CIkGwL_fr8ASMVkGKdvRhKgZh8Pu5YctT_QGaF8JdnRtnTxxqlFs7poViivOXpaxZcZ3JKe6-XNJGjbctlfx65myj6eZlK8Q9vldL3dlY5oxk5l7VYsXkk7XR340IDYGK6kkZl5ttXjnipQ2_49bMHWuMtqPUD-F32LvrX5MwOsmRTt7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2nHPpiWWgmRaFFfTRlBV6IQYw0-0XDnOMyPPxZAv59anRgEnEk_7wqIyZOZGYCd2rKbn3AfCurx91f2QbFtVblTQVaxKO-Iq0qu43vR5nIRYpr3BWEIMnYA3-11bTtAV6LbVnsCM54bw6ZTIcArHR5ludhd7KlSpmH0Cw5UazMgN2vn40iettmihWpZgOp0DYxS5NrCiYPNDrUnLjEzTYo4Fide7_bmxm8UtWCQsKGUYsSB8pTYOlZapyuXFYTO2WxEIdNljPCW81M6Do3RiYTxWezyYTMlHM_93qF0U9tsRzAT5nf0_h9ohglsYlmUujr-X-Dq50w0Z3w1xM0-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMjpt8NwCiI18hC1wwQ619bS-TB1eiDDVUwVlzFECRSfRU5TMw83P1SbvD66pHW3OgH3rKK3bPjssFWd08ELs8WxHEYBOlIHwtl6DK0CJPh8whTCIdkJpO5DivjoaHe5Pm4RF7TXohwCUVbIsUzIkzQYrJsn16_SeWZonTbUJvVAWSUQK8c_tP3SK0yfiSpLMPW56LRtHwkUs0cclJvxMVhW1uy48Xy1flASRliKDGNuniFpNOUVBAfOdiPXBcy1lpYmZm94UxfE6CQyTJwtFjSSaJXIamLrwtr-4na5z5YRPhE8LQwrFR3_KgmWs5Vn8p9TMTJ5ZNHx4T-3JSbGUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrJT9fBce5nRb9W634bhGsxRXsYgP7yFZ41ZFWejqchKZnansxGsfamcb-LCr5mcUoFNLMdHiRErww3W8q_1eDhYwLqy6nCWSvY-KbZNq0YUTXRMu1_hqI69EHDIsF5pLOXu_EBnRkNTg4Lln_Urq6XsCOD9e5kr3lDZkfcY0BhyQgxX_pvCuae2g-dG-mqK0uW6X8VamduBxNg3MxTs5x8QoVN3E5GzVy6eoxdDo2LWpw1uRpn5HzOTQJgpLZQWY5ewBuGsmrzfPDLVOXYlA-LMTkqdZgzJwo2_7Nij3QR1oOyfnPS1hBn4GLiECnjzEDKFsbxfGpXKLyGE62yfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مانوئل نویر، گلر ۴۰ سالۀ تیم بایرن‌ مونیخ قرار دادش را برای یک فصل دیگر با این تیم تمدید کرد.
📊
آمار:
✅
۵۹۷ بازی برای بایرن
✅
۱۳ قهرمانی بوندس‌لیگا
✅
۵ قهرمانی جام حذفی
✅
دو قهرمانی لیگ قهرمانان
✅
دو قهرمانی جام جهانی باشگاه‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdtZipxJofYurxyx3T75NDEdbM3b3NrCwLT8_4Pdi-RBwo9sfk4TFBiw0MeMKEqlGOwrHoUJY67JVwa2_nOX9bHuvEmpZo7uqZc7dWCO78HY87tAYz2zaaPmq8I4_IUA3ay37dUEwY2uhRUS2qnoQV1_-OyKfrroDs_1pKH2-MUCtsMh02Te0s7bb3Gyscd72XC_kE1KLwSu28638-NN4-puXfylCGtn4EPvuHpSwTvOYGD78g766PFO2PdU9FeG6OZ2EhNjnPbtW0mNCxx4NaVhgvGMARTW42mFWNcMTwhVUEggB9vWc8o89hRnsARbPh97rViny91Gm5xa8Rplfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKMJpiqFIzp9JgwxvhZCTsrTGcwHyXIwS_Skdf5n6XYel9XETSuq3LFGlr5Ned2WILA6CBs4BNjS20zg82bIx3Sx5VJiWHNgUwWuwGdgB27BhWVQ7mhHGIYTVwVRiMavulgA0vKxblVsHpVQOu2GODkqf2_zLQxAUeX7avMW8uugaTUikIygKVXHP8Ih8OAs6SB6ueEjsY6DNv85wh7khqU6mjjTR61ycPF6J2o9Xgvoaz3aOU4MSmtRGihOdpOT2pD-ovnJb5Y4uVTqDVtumbbHEgjRi-14f9W5_LFiWDL3M4yBt7DrPgfuotjje-2ij7SCGKNlM8yD4iUqDDrQ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjf2OHSgb7yexZUvMdXBTOzPld8gXy-osMPF1JTjlB2qYFv35Q6Kmw37xCcrpUUlbg_H90Zixsa6pxefIThJZE9w5fDAk-p7B7a93mjzJ4hM9QDfo5xQ8S_dzLA0ipbs7nPifyhIxlVAqsdEVpL8oY7Rz4cRyLKpzFrH8UhtcBEm58hvLojrJMDNHMJFX6A1jXev0adGZAW3s0nfZnMFVZJd5okHV-Q_xMEGHjgqAYtXBITTdXwf1_Nt8gbiDZ6vLjqdYqxJYyUs2CY4a8nwdFtak8YSfjfvsD28z0dP6KHvi8MEQ87hpqEbQNw29Bw3f51LWVSmtDAcRYXN1oaCzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZr6CZDAKm5Y3ruFLLroPPw0izxnihGJFiL7VdSqA9L2Vd1whexLSR8DP-6PotoQ4PKb5lwEFNuvsL-83tfnZH_84qWwEzAkTUWwHGEPWrz3XwEFRVDOhlhZt4y2QPGCDd1QUsKsOGXyPi2F79RtFC9FZ3Irvq5DfWjIcy84B3a9zh1SbHFN9LcaoyV7_E_BZ5O5MwYr4R9ZNhI2UthD-jPvveCPOFTeBIdDWWZVyaQDTw8-tXHiw7WU4gIMmZOvGuD_GyEL7VdAjROHnlJRavt9oZXcAd9rTDRUFQzf2-Hfz8Q_SNGqQGZBl8eIoOP_tt8XfokJfyZg33rXAjv7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FI9868W7GvPhJeI8CtWH0UO7tQB6YSHZwUWahsd1lhoE1qkC491BEAQ3CL14cKVhJnUMmZLVLQ_SerOhCbeEN5dU6gPiMHf_-GqhhBCcdwL5grmq-6aD1r22SBZTR-QqnXL6LwqRt76p302r3OhTSWik9cv804ZH0BP60uq4tQHYWqhmgBo5Uu_20HWmQ9mtxf0zTBbihIIFNyvB3IBt0amPFo4Slu_59-2_9kVxsVFzlgibO5MIWjhB75Hv6WEc_I62v0s0N7CjLkVlJTsRnlmdOXEXv-5FA3N4Ofrc4ZulPB8bLqks3IufAw6G5Nzq9rZO28POcu2MDGJ2J0IQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-uRnzsw4Mvlw76qSIzgJ_GiEmKSEdv4Gp-cly52oTYzhP4CCucUc4mtjs0wdTAntUIP8aj-cBLN2ozxXUSPx5VkZ3j-ryZovsg5v2nDv5bjn2X6ha3BcNzk-sd8LvoG2hYCdrxadI8Mmi_S83LVq8vdtdNWQxMDnzNT6P5Mv6HE6GMViViypwg7BLQzBiXlIK1tEOyDpwRpTFK8Evh_dwkgA4UNaoiScZpF6VulnNUe6nIjEgZFqUYxacRD79pHvcc3dSJt6hfYIWVcOB48MSzZHvftBv16vl7KU68jI6V3jhcJVH_f3xHqJ-L1GwfuO9tqYNO22hPx1VGR9CMeuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orm4ow_HA7lSfMqPbDWFR187iOPBqzXray55JkTeEBEUAzCOgr1pNusvrt0YAk5o0eH_itxPCWFGFWKRsX5Qs9pIs6I6IWHtZXCp-6W-VCz9hFNT-_iccYTgvOHC0nd2XBIkD6N9HCCxiTD63VxnNqkJLCx4rGybug8oGPAuFhVmx_kB73rbS0VpgebkBDSQpkh9g09NpFGP7r3mGUHobR-VDcrKXV7Wa9oBgJ2d5Wu4wVk6yjnop1HOA5poPQqthBShQ5V4utWU7aPgKwXLQt8utiQSuTKkiNtrUQcT4GzD9QJbo9ncQjAGP_en40nIiGppy9vP1exu0dk6OMvO6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=A8q6Rovwkd7__obZ0OCMXz-VTnb5WF5aPeUAbFQ2cfhS9MWJkbjDgOUYWyeMhQ4KKRUD0yEcJGnawobaKtFiZV7Mlfnco5T9bnbeI1HCei1Po45UhHm4Jz0ztaN9gIH3mR5CwPsn0dfLirK_tdOfq9U-_Q-ZTRL5Z5v62iqGFpZglzFfagCpwc5Im-hfHvcvdL9W2kXmq63b2ZS9mno9sSMEkFZvvuT9xcIky0whA0BDqBncy5LZue69m4IsxOSdHOMUWBcy79RzhhkDqCdctgQUv-bqxWxP1oWeiDdWbyrvJ3sjw42VpqBABfWzxTvvhRtZeKSFULyl4VKwXK7p3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=A8q6Rovwkd7__obZ0OCMXz-VTnb5WF5aPeUAbFQ2cfhS9MWJkbjDgOUYWyeMhQ4KKRUD0yEcJGnawobaKtFiZV7Mlfnco5T9bnbeI1HCei1Po45UhHm4Jz0ztaN9gIH3mR5CwPsn0dfLirK_tdOfq9U-_Q-ZTRL5Z5v62iqGFpZglzFfagCpwc5Im-hfHvcvdL9W2kXmq63b2ZS9mno9sSMEkFZvvuT9xcIky0whA0BDqBncy5LZue69m4IsxOSdHOMUWBcy79RzhhkDqCdctgQUv-bqxWxP1oWeiDdWbyrvJ3sjw42VpqBABfWzxTvvhRtZeKSFULyl4VKwXK7p3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK7NqZPJUM1FujZlkHxjMUj7BpxfP4a3Umu9D9YOuyUMoOx5rdCm84RNSPgZgepKGavhaY2LsI3t6-bIWUlkWdhTmXO_F0KnWDdvTv3ADhZlvw5lT0Oym2TYjwq7DsCjcWMkb2vaZRC5Br-g-__4CSNSPVT9bZopPdQ4XaX7qlxlyUTUrzut4qWY6lOomdEgkMDT31ecm1vBnPTm6wUOBdpti8L_PDT9Nkeft8q5XoZRgZjRMHL9lC1Jr8jHk7967Fs5XykEzh9DIfq-MZVu35O8XuTJ9vzPUaSfAGsf459qcTVOBnWxN9aJGtYQtSmgnVJczTNdVGlxYJJCIITtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAZsSP-KgjTz4DHFqH87D-GqzV4vcx4fV81bIu_5ByhFbmA04Qk6K_qlsbSTD9pv0TCa_ZuxfBzyxHfxZ6p8LOa2kGIOKAjgBN1EIqQt7nFOb0D9aLX6cv3-DKxDXXIs3_jS6EO_YTPAM7120mkRmwGb2exKhdyHBH0scjMW5RH0arDfDGdkUWxtBCPBHU-Q-M2E_gnAX-G2QPVRQLbG-gfWrroHCcwrxSbHqysB0ds30JoJLzjbuCrbovXqrG3mxBbJ8KcayvJ7JCoo6aLTOczFrD8M-ADGFaTR_EW9jRdCbOw6bzf2N4r7C6QUOEZt9ijTTfUU02uWS7WGvwpXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZjyqE7wTKuVz_YmjiUbCvRqdMi-kAA41obeYkhy3oWm0KX_PRtMkOE56z7H7y3sTLJrVtAc-MoQts5YudvY25uHyTjd_o49kFDOFdhf0qesIJDB--afvMl4VKBQs0i5uzBXth8_vOkqgSECk-FdaSohNYCaTaQmbhQd7VoS8gWD9gj5fWNBTJeaGupvEwGMly98QU4Z_AfahnoKoCX_2G799xnqlbJKz7JbxkvAnBXvh__9Eg8MyWh5jhpOsnOmUYIoiRMaG9PI7sF6XGBJj75gE6IlfV8d7YqDsI98eCAkfuKuCMI_6jZRFoQ2JgXBQkzT__ardqgMGuv5LtRj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKmAlB1fTxpDXTGHHFvefvl67BqMm9kWNemF68Pn89fKcIaBHIgSC56zNpBKBKDoVceIIpw-ubV_zFGv77CG7UsNHT1d1AKRyapRKNkIvUHrn0KaUdWpSw8n0b-UnY551kI-Y0xfgHmnFfOUCUzZL3_WqfezRPCBzSM4NuOPCEjsrZBq319YiiGW0BhqogAgHR7pJI61sWyLwRQir4c6U2MN70z-TkiXjso9UzbGOceNmKZWGv_GvakUCN3fx5X9a5FfHh3BgHppDiMS7SwSeh4eLkWs0_fAlfVCdYXLMiT-04HA72HpNMs0EtL5hKJFZjFZmNmXTnL8Tnaj7pU_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImDrEV6CiVM7zbykIV5GZTr7PD24F5yyIlyYXE_FdELv5mGgnkx5urnSpCNTMoZTYtuFK8y-cwwvhqRCvOQsyOmqeCDPD2bhXtB2A2aCjYDU1a-ZNEqI168czD94fKzL8vg_jj1N4ylyNdcWf_IyI7xioNE_69A1zEq5utJq05reLZ6waBrR5j3v89BZ9cOGpzwKfDmPYdIe8Tm35NFNpwD-GpdTMu3haZgxzypu40wIVc7hoyR8LY3mQosO7Xd0Vwp91_2ufsqKd7EumFd0tCgbdGI94xs-ZmT3qAhAnVORY9SLIRZF5ctx2HBXf24bg8xvMZ9YBYaw3H3o0sxuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El4nrKeVzDG06g3g8gFV8IpoMEWwk9YhlTj5juzOYhRnSJTtyhe6lRPsLPn8MD-6AO_kIM8p8B9oU0Ow3nnBE_1_6ljDEUiJdbYf-t1nLm2busMBtFyX33iSgTP6hRQT5HUigfeXwq35thqo_w_2XsjIg5GA42Cv8ZRIIkFJrZy3wgieavigpiRdMHzRH9r91AmhmF1JbYCJNTpv7vrXrM9EZZ9YUAUyx2G14B8Mbfp_z-gnSDgqCm532dXGrnvnULBGzjgfF0FIox3n9t44vs_bDmlswWRX_L6YS5HTS9EsPoyoY-sNXRuouB11iA7Cohp1k5IQ6QpkaWWPT2seLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzfaFskVdTCMjDf3FehiGVdq7LHHdzoyBdof3cC2koS2dB6cAZDvBlF5Ufg-p3draDR-9K8bCz2uSzNQWpyIS_HpmzIgju2WGOknMcj5Suv7JmXuoo4Lk7ZxUhoOqObsttmlswBv130rYe_YvczHd7DF4J5OQbEMI0OZS0MAzitK2XOGc2jbGZ_xPjjjBe7vrLK5kE_bjYfsiJDkPUfH0gKyjp_rdw0P5OSgvw2-Pk0Q-sIfkXdMDgpzZ_sjWVVj2P26jH77OlVFUd-86zvyzQ6YqmbvKqnQyF5h7_uPVNnnnSA4lUCOwFKU2Be_euGY2Taq7tfZXWvwttQoNyNORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOfyFcLPZhaiRhUBpuyHLyZHSU5FQ-kFA9TnXkn3FsExCxlyb9GUhkolGI8wJmSXO2pN5PEB6xLEIovvXHtlxfpmh0IujrboarOxDV7fGO3MJ6V1z1j--Gnhd9LB0-g-zTpfEkUTHMVzhlLkeyaSLS8oiVT9SYBXFWjiZ5JjVet5tTItR8-gW1CzmxkDeMXfWEYmvqJD-QPltLbO6WtmjSZ-RnVC6EdmcclZXAY92tXJQK_hUqsvmejEhdr39AJXBdXZQm8y2ovRWWTA6QdjbU2qEGEjmvU05uOHWCXgaTt1r_pKZSWSHQWyPdlnyGRKvV1Hl2x6yTTN5cLb1qNY1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=onkrHglNhpxBI_lqnb8j62pVF-MkcqEL2xRat_3MhcvxvEd5X21xU1P_7jQtgMM8hW4ye2MHPlO6Foa4HVh50jqm2BrJU3oSzFpph4bHg83AT1p6W1yDD1rOP3GavtDBVjAzGv8UX8fMU_0LIXHAQvgYgFtlt1H1LlGNcOh6cYcd5H_FtLcJDMivGe1cfwsVPg4YVoKtv-pJghX7ZH6yseHoBFJVMNM2lQtY6TyJlaVJZVzswW8jr2ieIWqOwo8ZOkgbeEiwNq3hGIvSJBJbJJtg621V8FPTrltb5npVFq6LaundL81NGqU3oPPBWAGQnScerO-kWYph6yVw6LuG0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=onkrHglNhpxBI_lqnb8j62pVF-MkcqEL2xRat_3MhcvxvEd5X21xU1P_7jQtgMM8hW4ye2MHPlO6Foa4HVh50jqm2BrJU3oSzFpph4bHg83AT1p6W1yDD1rOP3GavtDBVjAzGv8UX8fMU_0LIXHAQvgYgFtlt1H1LlGNcOh6cYcd5H_FtLcJDMivGe1cfwsVPg4YVoKtv-pJghX7ZH6yseHoBFJVMNM2lQtY6TyJlaVJZVzswW8jr2ieIWqOwo8ZOkgbeEiwNq3hGIvSJBJbJJtg621V8FPTrltb5npVFq6LaundL81NGqU3oPPBWAGQnScerO-kWYph6yVw6LuG0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4_12Lxxy_t-WVwUXmhhoj914_LOYs66IiHoanhDa4IOe5549Abk9qb4Ki59uWaX3MjOFEf6YSSXsDGnT91iWFoFzxyt7KfcJ1_XFZ9hxN-CU1vmoG11L7yYGNVqmy8DzXUfn_yuLQyJvRD-wJF9eJi3XXujk0qrqgIW67eQMy9GRYs_hCuWjfW8CVq15PwVX8633c7o0TxN8uwNjRemXTMxnGLqgqIHXfFJfXfKUVOPkJTbyGRmdWmlWusm7MVk_GaZguz7Zf5PyAnAtxoNp9fUo64UoT1yVI1EJOt2RErkFM46iiSpjHMTWfqFOuDglhV20VbrncT4QW6AkF-7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCXqvwED1Q_XTibCe-YDVSZbgzEcJaVValoJTUHsOamiRniS93StD6prgf6bjZKBxjHfw6qFhCRjaxBI71Ocrdekxg8YnjfgJAY4wqtLvOLV45ZcXu-LnVjX_V3VGou_cCF0i0dlKFH8foofV2_HrGpcOofHXrpMixKvSQZQhhhSE_gByVBJ6Dx_W1B1n8dBC8Fg-G6xTB7IWQagaA13WZjKTNDJb7xoHVwt7cfsnpaMD1IxnzT2fE78MbVnhUB0vHirlT5OnSxQnDesjF4xHmwsTXMN_QFv_TUuSUeuIvuCsU7V7QzwY8o0joUsyBmb-W--q95W9rMEQ_1IxesxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=X5hUEgVC0YPcESjL-jgKwDb0HWZ1AGpnxTT-XgZcrDbWp_PYm8QXONvdwBVFgBy34Dlyfi2un-FGrFPFz0j8ZfDGgkmmXunyWgGrl_Mj71QKX6yzuRUBQUKcM1h9nn9iZWBcWdTt3H9zYyDLy_fgxAMROlfp0K8SU0LvTzAZxWu1YIAlN98_I0DNmPaBGMLaqJ7ir3bog0nTO95BoIzMVg5t3Tusm28CR0dzDcs1ahvW8jqH0zSBtvLNqCLn0FvOKVZGdpwdE-4r6NYmbxUVUdVbnrRD_kgO52QL9fszEzxiDTh9n_s3ianFPIVvNtxCQn-dJW0gJYMzVb8Cn3MgLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=X5hUEgVC0YPcESjL-jgKwDb0HWZ1AGpnxTT-XgZcrDbWp_PYm8QXONvdwBVFgBy34Dlyfi2un-FGrFPFz0j8ZfDGgkmmXunyWgGrl_Mj71QKX6yzuRUBQUKcM1h9nn9iZWBcWdTt3H9zYyDLy_fgxAMROlfp0K8SU0LvTzAZxWu1YIAlN98_I0DNmPaBGMLaqJ7ir3bog0nTO95BoIzMVg5t3Tusm28CR0dzDcs1ahvW8jqH0zSBtvLNqCLn0FvOKVZGdpwdE-4r6NYmbxUVUdVbnrRD_kgO52QL9fszEzxiDTh9n_s3ianFPIVvNtxCQn-dJW0gJYMzVb8Cn3MgLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9lGKKlhptUMuWdrZukk2Ppt9ukr7h9KTKEAFvUTwRI5G1XWsE1dGJwwZkxd9DS9VZbkx47mc6EluGJ6alWMD7o7LETcp88KjoQQY_8cPdqDpkSB8waDZ2zT-XXd7VPjumlbVWFdKf1b_3NqH38A8EXpgCSQGCnCd0cqzYqK1rFNwte10V3Ia5zfrX-YTm_WwgXodiB3im7zDSn47g6kIvVrGGAIW4tJn7guoXbiGk4N1WCeMj3ACjY9dJCoDLw3Q41hl30SUPnVBaLqvKEeN5NAG9Bz_7GqwDtjG5oz5qDZ5CuwaDcbBpcirMeEmMYZNLNKrHYaFFFh0Sl4WlaJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hvZfHtEjwoNwVONnprBkmdyEevR4_td6ACsnryHv2EOKprHJi6DyW9TeLnc9RImGC8orZGlE9d_dM--vvpXsCu9DUegMehlPuyILPPwOwRSxNYltOrm52N4EuTecVh_hoBYmtRilyovmIHEr2UhmuG6s4e1Cbv6Fh1ufxTn8NaY_JF1kZ5g-v4CpupDqePUxPVT13GKFZinDtx8SmRVGtYAQZrnDEjMtaQm-u-DMOdr4aCGIoNdzbJWn6_nt44jjKCCItEVbkaT5wZdasHa7UXrPsMDDZzFR5S6hDbdK3nXpIJjv8s4qpvtC9Wwv0WmnLqAYOoGXRPH5vzU9TmI2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuMbiGRzu8vs9Oc5G2EHmiu8nsG_WtA9ZNnJZXqzMJ6ER401biii9GkUO9gjZ3jJ8dxv61kxxaqywcxXOfs480Do5jecYRPO_RnGkOjj70RFL5R9XaElzQUe3d-5mU3hs4_Hq02-pq8-KgWgVDX7spA2mCCdEl_rIC1WfUbSOmzPqToyop2yhmoROKQpRiaJMI2PY8DrFRp_rHVtJKL_8464z5ACdrhFhiFw_S1PNOF4hoQAKb5Nin-t-R1WsK60WRm1QT89WjpOcaHDLxbz4Fahp3rKQG0B5sAchJNNM12du-NRl4R4b3oNPgTpath27oE_p8jY7IDsD5nSzO5JXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuthhMpSlspMj9yKcrPvBxBC1zX23pha9iH9lxOmSlKm-a2mAxmYwuPZyntE9TU1jGQ75ydbY2tRd2eDC6DN1F5aAStzP0pK_KVBwSSK4lQy95-w1s0u8t3TYkEMMM8eJDoHHs8B0af8DgPQtDugOGaSUfxNZOTA5k8CBr7e2s79n5qOs4oF4mthyL4CEDf95I4x8Y142iOe7LVIsdS2oop9E3Teah4gvCYiYrHAxXUc6hb_GzA-bpPFokptm12_CsPCuaelLlKJVP6WnjDF1VrGEwV6VTaljehSF1B7DH4zWihSWZf24u7dge0Cb8r5ETIz0tID17HGr7jNdx7YKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNA8Fnzo88MCihXq6P_7dqxZrUsm0HEw2Uz6dozBLFYQRb9jDiEJ1J4HonL9I1GoappTfrdWj7vtYF3el-ul9ol-bQW7XqA4kocZaH0szySzucQTJpU5mbe0huPXvKNjmKmz16sSQgjinrW_PT1gFYEPIwFGMtzYA2o9UR7YswLBUkdtpyOB0TQbQY_J9soPyAJGrNWOAKcho1Z71W-HpCkEmR327E_aJH97lFTe3KusEgfFxXXnj00e6rD7-cYWfKhVKwU_co4gbwTB3byo_J2KBQLigVn_hfr2ZMaefLCV2mxOMLIqTLCfg8GgUixin73JxJtqSa0esmRkkKOIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u684zVM2hwTXA_bOJ0r8HwO8zb_868fwlrKzrgDOc9AS-bVOycm9QvUZs64TUIHfLzMG0y-tSdH4JIFm-3RlYOqe8fEcg5qTEVJqqCHjzvqVgQPsP5YK8H4gK6hoBRp0rcxzmfgfn3M4VZbLTm6U9OYbJCi_bMb4rlHXyBaU5lrqRbQMv3OJu2QDaVx8rtu_EFb6iYrMJHBdYu7OJ756MiAbT_BXQiyzH670XmemCSL1K3hCVE9kWN3baStd_91NSDJLWxPVOFupg092FLohGg3y0JrKgD4E3cjaktpa4bt7gzFdgy-oI234qKXy1uL3NwiA1MWNPwuu2mEcVEKXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTRUR-nEFZqyHMGXN6roIllSzxzsv0cWCNmDdOiO6xrof2s_IB5G9kw5_-mBawnuhwhRN6Tpr9zYtgJRHhyDMLot64Nyr5otaxX3uyE6-qyekrh42uS7JLQuttXiweK_1HbmzhFrA5TKHF6r-fbOhRQqzkZ1bbJAsKNw4rnnPqAiRo_-iVQVmxk8K1DsAf7UqDYmbNM30-Zgk3IMOmkkcOVK6QVH2qOEd5g1LyfXI8CewXV5x-VJVPvo4GFCfY6u6pDlx9KjkkzoI3dM2A_8ezVxUohp02Ccdv4oTuy9zqyAWtXrmvsHo0GxHZhallZiZSDCy5jO7HCKB1DoAMilzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jpzuqe3apGurf1vMU0ZZjaHLI9aBC0n2nYkik8GpzwBapFdil7j4F-Ty60xHq_NgnmnJbsuqFiVJ4ITH06MREcK60lpHIheah7bG4bAXAmfpPnZSeMPtITWIyKGW2Y8oTzqjEIgpZtM88kvdPr8xH9xh-_7zOS69D85eHjA4fbmr1SCpDAOXzRC0y2z4hoZ7GB_QxmszelLu8UaFDo8xu4llEibwvxM6QBO2WKDiDzsgNgj1PiIGts21ZB96t1wxPjoK7ooOaORW21kshJrUS4txI6Ums8AnRh22n_bVAFZqS1L7R6cQUHvO41YrxJZMX6Dnu0z2o03Vs1AI1LJbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoNCAf3QjaaiwloGFqkOBg1AUKEu3O7RgCZV03z7BPEPkFJtNZThWKlA0YN0gd4No_hHmMlr8lSBlignpjf65RI5k3VM8kVaN_hhxL8phzsVG1pcVpfORPVaaKix7F7kkGTJ63AhlORP0wfs_bdH68q2p_Mra_dXa_LayszFVsFcJ0giDCzprql733phxizmxJB8cmmwYnlzGpl1W96qgCKW1XIXHHJXfDm2qBVG7VV_tA5BJJnDfsqllp0-f1KKfuFFU7UgyZezqubtHtAcO6WqfkLnIvvycqXfMpqvtVvap4TwBZGIXARvuqdsnrRKHXwSVli86NPiqbjpyLWgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYoo3Sf1Fyc3-7lYvd_fiA6sluqXKGsBJlqbLuqrTaO0DRhkpeWk-6U_GzPyD2wzsPeq1Lojm9K2Gpi_O6lmwQXGX0kB6SpbJ3gAzO8yTluEALrN3m2q59heqbwvZPtAa5yTz-Q_3hbcI1nb2akjJNvphtGOsoAI_lBWvWHQFxzr127EBuwCPXOcCgXuqHDtYhEaZ3976vZGKygvo2KgqKYxWFYt7_jkOmsgpEGy0524VoA1-1LCNRHhWrqqb4OknejeetU9mxNFVOyCMVpLgl2j5-LkD2iDVNptILSIPm8nEWEy9ciKeqJhvAAj3GF1fZu4JsIT-E1m6LS7LcYbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4vELjgjZx_UbnQRUcqsX_bYqUUnDKexnXNvW7radO9_OZTZEwpiqD0bOau1ezAn0GKZRGE7Jqd11IREH77uFY67VqZAIBAU32WMAOe6piQcsLgnGWBQoAQhKtAU4yqKw5JtzXgIBORiimxYBnMzvh3KaK-B1koWwafTmQX5ZHsBv8IzO1Aput6lKAXgA7z5vA-jYueG7WuvN0M0KY2Ndh5IeiH4YX88EWCz1CJ74tRNkclNzyYPZNSuS4jXeGwJGXmAtZ81FlICsMuAG2FMVoDSpkzuh5F4-ExluCIh38L3wc-bILUn9LXBx6zBfqi4rTuOLBedHkvw6ujYAdRGtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8L-TyyHA9kD32qEluoh7w8zZtpWt1MQVIcWQ0YQvW89Z4r0ekDJxMDR3g8p0UpllZndscoz2GGWwbuUwpKKMtVGx7DYjyviyDwfYU7_HroY31bgNEcaX8hhE_Xv867HMPJDiMJkDuQsJ0AXs8QQKdh-PxkaxH9Bs2TWgtL_3_Ykl61yrhMQQgP28GOU_2-xMcGRMnVK91jtOM3r6ueIXrkSqXHOvHuFSl5x0n2xEyG4zWk8OmH9zPqoZhSbbXttAQfBGabdMSfUwqKY7_zC-BV_WjoLHdAvUuOKfe7mPRtmlR9xcmh4NFmiloXHOafi5U8UB1wdDc36LXLoaZWyPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5XlGBm0YyZfjHCCt35gUPpVDeBtZOAq3H2AbdR1LZFCIGkqYy9LRRZuTYiGffOVPXWfVcS2FjHQYRCODouAIs94wNte3aJgE4EzOe6_IoRatrnlA8vwlaMM3jYY44xWxbbqKijR_djnmCgQBDh1SRsCUckqYFJyrdAKwY-ajsVmbct6Nzhztfkx61ZLd4OomvYQiZM5hdQUFvmeNqZ1QQzHDCigIBY9NgZPye3lfKtRKjNummllPRwMDhtAygnfd0njoSDNQvMtLLSJfUELAk2mXyXayV0lPIyswTnOU3mVarOkvxEOm8dnY3Yh0PQHyZoVDzt4g58-YhERNhYQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVxxXL2Pmn1CSha2ENczUDex43hn80L3vxH7TjGf18-2vnIMcrlEgMk22OWlePWza9gPbTbpI100Wo3cS0X9OJUMdcYXwHx5DGlvQtr_Hwhvmn3ylb0byBD8eVwitc0m9wr7lGe6zbqQO_Bj4lXPeR71sphbgP6d_W9PF1o9gDCF8IsG9bOaaeJI91ggsKSQVrSQK2F1S7k6qSviEfVl7PT4ExZ9LfV1rEO0CFO6MkiRdsfFFU15BameI0DlWFGqefSnjUnkJLB-76XnXHqJp8kVgdlwBElpgqoTQrLJrqPXlyiK17KkMfEDWsiKLtKZj7kwrkKxHVfABFYKrtwDMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=qai5PbgRQoixGW2VRA8MY_SpUfJEudnl54TbUOOLlBmpqIhwlZ4qB2KmpO1oU8lYqCPR7eCn-rbgFjp3KHZklH-LUCdO0RNAdSHV4xqa-l3yPSgkogz4U-kFywRRvrRPYxim6nAqQy8TFzmq6Ulf-sdhN5-aeWCucHu0HLihobfIxPo2qATvK44n7HRWyzHQKSZpa7YWM_VEsOVqW6CVCPrntH-P6IyJK1DvUNY-LMqccLG0o7cfkmzd8YagpxyCqI951dhWHWfLyxlnGA8RL07zIe56vnUCUOdU2swDt7PFroQrj3s5YBCjnwZms4GvD_zyR5aAjMwsArEyiL9ofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=qai5PbgRQoixGW2VRA8MY_SpUfJEudnl54TbUOOLlBmpqIhwlZ4qB2KmpO1oU8lYqCPR7eCn-rbgFjp3KHZklH-LUCdO0RNAdSHV4xqa-l3yPSgkogz4U-kFywRRvrRPYxim6nAqQy8TFzmq6Ulf-sdhN5-aeWCucHu0HLihobfIxPo2qATvK44n7HRWyzHQKSZpa7YWM_VEsOVqW6CVCPrntH-P6IyJK1DvUNY-LMqccLG0o7cfkmzd8YagpxyCqI951dhWHWfLyxlnGA8RL07zIe56vnUCUOdU2swDt7PFroQrj3s5YBCjnwZms4GvD_zyR5aAjMwsArEyiL9ofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7JyNpbOu8RSkVCcsksXavD05ONmkH4fPTKOWVhiEgM1Zif5nXoqb48NrGayTp2hZpbSfxHYQUgjEs-yRQTOYtRXu4kqi9D6WUp8VJ0u1M5I_xSJJDjkt6IYIeVEcVjd1Um6Rw7WU8pDgBTVCOgwxjLIbuYsft6mUXRpUpuv5di5ISAouRUeknhGJ2tpN1wmwtEpGwqls93zJoCLepJQ52I3fKE-BpVNBqTE7DnRwuVQOWYf57CKF4OGpFm5pcvPFCBCzxX73wmnOvU2L-ndMWswmuGHsWLIsMdhzvlGq6qIuctflQAgxUVBcdQsAZM0jBay1R3Djzr96Dg2rjDYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE3tYriGxzsGKYH0xVWuzty1OQeipUWPpz7hsIEFTi2dBuJZAZpmMooTbiCkbCGPwrAK_dk54ZN6SZF8FI4e8_2C1DLp2UI_bpY0jJvt6DJbciGfODVICUK6dPI53qkESRl10dZCOSbu9XaXCWtQ8A0rq-4M0yznyrV26Sdvz1o3pXlLi263to7jz_ZzxTdX2YBE5dGNOAlkn1bfNxFy8kXCOFPxvcrfAdh4nNewXLMfP9jkoycOs4U7i_memeI91ZxNG7VN2A8PGykVsHvfra8et9n4YNVZ8M1RTysPSIPcTUMHKl-NJgT1HtyozEqkPReabYOL7y6pwytR_ezOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1ofqH3vHTNrSK3c1CWbbYy2QBBWEHTkvgtmKXMv4GmNFgalBmZOWJTQ_ddff724G7_ha3bJz5Ym8bu3nf12tvTxjGglN__saNq72c3_ozIs78j3RHs-Q0X3a6uelK0zxVv44PQj-Eet_oY8usROzP1g1Wp4Au6zLAN9fUArlkybDhy61RLkJdnYd_kFn1em0RGmws9_je_-vXV1RoEcXk9OuvOrBVKqikgrCiWFjAK765yNBMpr1bS4W2kSybo-0j-obLAiBv2jfwYARHyXqbVCW-LxTSPizrosMr3jU-3o7cdLCzhqg31I7jepFR9cySNbg3QUaeWfMoL4Wua5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e82N7X8xvzUAkugoP6v6N1tuM9boeHrsKijtDisFVVfRWnHQW4JuECuIws3DElK5M5_aIO7ULCurY3jg-XL6QGO0GAk0lhQBm-OWtqe6ntKaoznH3fO7Y9HFvJnGxPY8SGRkxXH7FdtojC0XiB8jEw-hbPhljmrX9X-AsKmeQnY49tQWs6jNxQrVFNbBFCOymcmddwW43c9YxUvw2jFP9hLqwkcve4QXXGlkVT2uIjCElFYIHY9MPNdr9j2mlQ7r5xK7R9ePwdGnAJEahTrq5vAwNUcbrXWLlB1sP5S8zXuiJOmpm__BOqcsM1p2NOgFm6qd_csQ0z7Ty6lkIi_t0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzWygBBEhCqLB6Lnpz7yuy3vOoD6iF0_O0SavKVv_bK_RktAga3kiwXbjALagKrew3Kp9LVRmg4MI2w-z2bsXoZ-Je2mcF8kJ3bM_1n8gpXXU8HqhdPjI3btB2sD63Ma9PfeJHa0N7oEnFAy7ey8hPVIcMRYzH_OG8Xtlx1JKllULc4f6--_6LE_FqHXjAaqkF1D65jaUOAL-zbf5M3X6Ch5Z_wHkXRc8XyTYIuOBGeIT2FfJztbYIJMtt5XwPWU1_vt2K3GmdF6UMjks6dr6zGlJEMNg4FB6eMMjseR_wvQrk8BG_0vI_4UiFTk-cDapu8nyRdJqnV5O84CiHQ8tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUWV_neh8sT-mZyNJlVqbqlqLEsKg1feeP6InF5CxZpvcAgCd5AEVE3oK-LgSb109iG0XWawbVB5WrI93IA1WsAdrRWezT7UsyPvOh1XKgQtPQCVk9jDQqSzXkQKCIhMoaE_m-X1y2WFgwV3bbwoDqrb2dwkOl0sCeoZLiEeCPPia9oA-Ub_lSVmCPYaUx9kMXqgTQ_vjwV799uAc1H8tugEIMZmR9wXKGaBoU4A1JbrSMGdJ5pt-Ok6-h8be7_9-Yqb6zSnEW_nw9qhDMinOoZ2JluZnumBcicgrfSgrovip2hjuAuwAciBHLF4Kl_ByM2uDunNrtPdqFe6jMEf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPWXMiwLJeBpZtaLRhJg7w3N2wFCRlfV-gPGXmcrP554ZFymyg8M16w-fmbgB0Hc5HUDoPPhrfamPl3e7NbDFJyjU6zim9DFptWMMS2u3f0W3Ag3yKvNQ4FY6s9XKAuYTIPOBXips2NNNAECzX78SFBz19LyYANqbuZSYvh-U5pMGmo76PyhwQ85fv-BUG7YDCrMqiCNd_J4yJvONiJFjjfLqLDSm_VD_NkGgF8x8qlv4n7TqHVoEh89Xca99QuF7qTb5N_7mTKRx46ARLdvzTTpVzqRUaTdi8rKWR9nfTe_CsxfcDwuc03438r5p8_GgY4ee3I8bOh3tX8XRtryTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cukTrcIkeJ38rWPu6kDB4dT9sSNjYwzrHPw6x5T3iW0_yDCG6iOpuq8sDv7188YfZVXxAxEN_nMxJhW2UZtUGTrkmBUVN3yK1WrtPXxfo24wCUUjFoyoabSf2vPMhF3CXOevxtgAEHQIOwnTy9JcdyToRRAkj4whOPzBuOdzH9xjUliBRwFetgN2oVGNKsTO-khhWuLhX6NQ9A5yxAI8MxxWCZvaZuJ6GBA2tc_IwNdrV-KtZhDpe6c0KuzKruwoPrFTXYmcG3t9y_RKMIGdOaYEhPioE6WyQYGSFR65FiUS5bjuWLIExweKrMqf1WWvjeTy-0BceQgAYzx23MLjPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxXo2yf-THFOziM6CmVs6F8iPmzDNuOYjzuj836sShFcrBnXbj0F_yERnRqg5yh3a8WZbTC732UbZlDxfiWIqAcnEbhCk-R-39i10R6Z90zW2av-ilrHrO1meBKttbU-i498HBvQMKopbLkab-_ZT4HQ67-3qxc0AA2CZkH__j7yCwBoBPhsrmFh3A1r1HtO9mN7laKWuE5SAy4uGOJcCto3bFBhaYKvj84Hn9_c_R9kjH5NvFCH2ufpQR9glGtI9eko4zcuLqvpO7_PedkKpc6lqYfh2H4Rmsr4UkZTNM_008w0yvM8Dj-pzWcvjpqMXH5csXgQqrQox_4_5avWLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPdXjoVPNHxs42xg0JENo-uu4ejnF2dh6awvDU9GSOdSy2BYbBTPQWUvERBtTHJ_CDb7REiPErZfKAL6xW0WeURZ2CkGLK4zRbIpqo1IDvFo5RnE245Ss19MkBO1OyUgsYFvc46aqXN7GoDmP4O1eswr842a4Dj0KhJodDhUimYRJldNhvWuR9xKAwgcod7JC64ZS6rZ0xElOgPbpZbpWDOctsqWuXCc-OM-97vgX-HH0coZbzi_ffK0ynw1z4qUfzj42rkTojMJnfXwcM5fryqu8vhE7nsWk16httCaA6a3WD-N0LmdN5rSbgHgzw2g3ZTijGGpGdW9RbJY-0HIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtpIXNGJ4ZxHS4SqCpe34Y21V5sIiv0ZlEO8KJj5Q_s-OtDFZTN388i9EuqYPVBkaPyWY1FxTbQiD0QAUWRG5uJK10AgHlebQJbILhqK2TGS38OyNgWtwmHw0h5VKsuowTiYjat8ACpFguvExZCUuvBbs-v6IN13D1pexmXtMK80FVmLprJzk-Ul_awPPSAAH9mnbIPoe9Pgn7A-5ArvhnXwgRBIXeEKORIaxcXOkZVGNsMPglajdK1sjf2zxAcdfIMorrqk84Ow3Iai4nCJVMJdESYg-TRoQr1Xpctzf8CAW6_XD23hdLgOBgh0d18coVMPIOAxNQE37jLiJ1bghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNM7-XTf6XWyr6VMzN-yZt4YI3Cnxb1RCg3GgrrDAsbSPRf6Ze7Cbv1aHxfkAiCII3JTAFNO5CxRffgrTkXfCh2upVQte24oAW6HzMEmBbCAZneISj741rbcplPFkSrMS96qU9fmG73XeMhmj7SeaFHvS5G1p2loQSM5FWZ2M0o1YcVywwXhNj2jbpOsBGUpqjDGhUsajQFwRjJCbDy-lWzHJPhXhThl3Ixn1FmfV3EExOatSUqV4ZhyIO9qKYr1iL1RohGsRbovATYe0WgDDFNxfFoUQIgzB0ivvN1k5xUn3d75AO09mJoNQWWctQQvXwJyif0mrxcM_Rjno3KZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu-7d1WrWU9FhgO_R_Ukl0Ga_YETzDAk6CZIbh1lq84M_cowi5Df8E-GBDczkPfWoGs7reHmi2VwcS2TH_7EmMgXRuLDV4FQEz7ZnLqhgdAx4IUNhvA5mXuaqJG4X_mi03cLoQqi92Gy8nCgAKj4aCyU8DpakQo9_2oYyz9M3vxtG9B50NmpykUabZ5rYhKLFTBiRBLYucbuZNhDlwtFaGwzx2tJUnDaU9Zf0R0E2ninZJF-MjkhUKW4MgcNXweY9tKKurpXA-xnEi5JZTczaRK_Iy12Q5FIyN9LZSP5XsrX4nghDVDeFb0oqV8uILJOPHoX8duYNEwfdwq-NXnmbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfKcD-XA8KVRkKRkV3LyJ2dEvRPy7JN7oa_c54OVDFh6dGX-v4xIfhDJMYYeJY0VKwDJet_aTPOk_ohh2t_0vRLBNIruQ-mlMIBFKPKhQLzzwJ-Ba0hgptIs-18Uvd0mWJL_zPFFILSBtj8mCtrWLdCLKsQGQSfMkzG3TDNiIBBDT3FM2oJO6fsSQz-_jr51hfjhvl9hIyfuEwSfS8i2OjqnFAAOEkjJq8tqM--yDUpue6JgMIQhmAa957v_pCgKq5zlKLQYCCSGqyBXZplYBNzZzwN-CNQjhs1Bo9Q6WmOQO9ObwV9sFoIimPP8-7k916NjAwdJPBs_5ELHmXU5SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbcJTpK1I6VYtRrkbI_tEBr1T5W2uVvJhixPvSReez8bC3JKuITyvTlEdJMwuP77K2Pq9Qd-EKUTfstvooSZhl8rUWYqwhOENDoSp8dkyK2E4WVFhgyyqBA4YD7b3qUM8UQDVuT7Wu1ZKIphh92_mphdVq1XzgJR6J8Oy_KWC-9LjpzIuUoD7aZKll3uDob4K3vgKEWBo6J-z7luNqMNO_sh5LWg2G5Q8CIC95AhhnL_k--ClaL13muc8_-CLQnYBXiNUflnXWyIA9ONok_WUVEMmc09afGI42SIElS0G1to-Ls8ScOhE-3u_Bbt34LeuJdwtwN18J2KKSdFZPDfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU94V0dL8iPu6ZmDFPtGAsHsmwBmjQLeVR6ZH0vycM6L5e0aW6oxL_ZzGM-BIqwkUDN6gl8kOQGXDqL9s1qA1h3dBvCnP7DgGv5YIyqPHrQfYWYQeDOmoHYLsTSuHtJq--u8GQ262nbP9nc5-JLhiv3mhyuZI1AHjpjxzxRoqvfyhrzPAu97LLg414iUzUFjVLMKLLRZd2uJpsNhXpPH_shUl1ivVITKl1buPEhBKukrTq9Q42CLizxN2ja17QIuRWe1E0fnPEbHogkydCkzT8QzcNxTXwoI0tzsCeVyu2HldwjsmjA1Ws6l-bXe05yNW-mplUYBR3p9ID8u7yvUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsJATGxvPOoq4knYn80kv49hCYD9NzaamTG00YsrrnpM6yXSU6hp5fa75Wmk8d00sv1BkQle_JBwqUHsIFoJesKOEbG48q8Dqsg-TFI0vNjxE55N9iD3xwP5ucqz_XbHOZFpyqs76MnVWBMdyGEgpfq-NCcigoGsiyPt6wN2G20AhowUGe2K7ojARTJr9KUhcP1SfMmpJkBhg7d1aJHY0pgU7lRvGQBHh4VfH7g5CPmoyiOiJJ3XHKGDiAOvKVD_Ht6079CUqm89aYM9TI3YnGBH5VUpRubs2_Z9JlRn34Iw_Ga9HzGCSPs6ITjsuwPH0-HvLIxq95rAC2yothKYiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcrPK5sxFL1VF8FloNV44DEmn_TjgUjyzVWkI6-WtHeetg01EK3zScCi78lNXg5kODMQdHixqaCEuOdW1fn-zDSzcsRiVm6LQei70LzuUtPl9KB0LESGEWlBG0nfUuSJPmJ-I4-kFg1Q53JSZQWaNVZs0JPMT8yhtj063melXg6mhWxMMDOk6ghKuHjVCblT9vRnuiL_whpgrBM7FqbKCvXcLWu9zR1Mz1NACCwrUx9Izmu6LR4FEoLAFJcFFuzu22hUwPaGsXbmROxD_ZngyJYFJ3jx3qNa_Tka7bfLK9Oa-h84NxsrMhQvfhb9yz5fZDRGK03X6Cv64u052YGaxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9hFJuKiRkC9HC5uQFzi44RsW_CK1iDRhJaM25nTPWqAQf-wC5f0d3Rub_M1WkSA7ME_15b1YL9pPwMrcNE4iYh0RAEY430bBfTbJvvsnCuoehlu1te3yJ6If_p0afg_k-PNDez8kPTNjYoe5L7Xt1NQPJAZ6IedNhhoANAluNwgh83etc-5-htc-Oj9NQQFm1wLBQB6HS6kMmMU9EYLzw-yxnBW_kxa7DtUz0fyNTTtxlqVgky1wESZ7nFvDnnO063Us9FV2gcFcHElf5gOtAd0mJDlrxpn9N3WlShFa0hjugvZ8fxLcsftyCKcTMiXISKi4LHrD6gqwxpwrwbpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7MYnD4L9IfYZWLQh0aoBW5sE5b0WD3sdBJqTcqB3Ok5B-ZNx1neqwLHH6KL0hrth9IbfnNq8HM2ZKGoutXTvWNSz7gN0G8QDvyopANT4kaWEU0GkguFblxOoTk2eWTUxJrlDG-XknGVGYztHz0rB24-HKMPqMY3O9T-j-W-ponCE9ZaBfnlGQj-Pq3iZVQGXDDEX7bokplKmpoK_quchAz0mmmdF-ksHNwhwIk-csMYSQyCKqpZ8DJwS8Jd7v0_1SNEK_Uh-bwmg6ojHoqxQZFxI7NHegcbUPOniPr7rVonYjEAto0DYfxtPxotPuwNWat1RkSXDO-jYSyFYiES7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACRiZNmt5Fw1rJIHvkyTJUVLY0QK15zAmtfag-LYsufnBgSntdFJeTlplOcCJdsZBRSk1hrrTCtNDu0SLzWDZLmHgSEVj46M9_gDT--bXCsKkmvnDQkmLBE3bEcURl6Aw2p4snPtM0PMJZGzsWZbVZAHbV-HcrjmwhMgWK6bq0flAxLTljljbo0cmLjOQC-W-0G3TEX4YtnGb7HN3PgYV2bbFLuwz-GyQsr1YGDJNgnz6QwCjAtN5O0pv2OjO08rzqnaiucNQ5uopavWS0RAlAcKqid_hBHk5CFK9BkxJ4pr8vRDJvjCbxePNs-jb9clMzLO7UxSaKsis0MmwPR3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-6zeArpwLvsnp8hhqZz_qlgcSYhiKxph-7RTXSYMl468HQiFml77z5g_ibnfGX6EnvZtMXDIjhzAq38qHPF_ON-3QK1N1Im6zqZksozyEe-bIVKS5R2hTW_lWz1WnVfuPFppsaOQjmn8ciz_7r-8pK8gpkLOlq45U2q4lav2HDEPNtS8UsWj-YdL-4LywSIvGf5laQqnWVMjcSQaNO96KqTA9QsYO2oRJiUmiCzSv0EHGRSZYfoeKlTpg-gGsTcAO7_zuF5WCXWuyREA6KU1yRbdsd_l24NCviYlCMHu-Pk5Fjie7x4_rHZyBXJ0VMIRwjjQE8ADDpOgDUGGU_nNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn8_XlE-5qDdByUIj1HMmV3EQ_cxR8irsF3dN-gXjTJ64NnuekhvGEr8oEz8igESLlPhLd74DEDrBcuOrdGEtISVhI65M5VQB41f2h4dqef7PSq831cUf3eH1x-BAa6O2IVKYfXKoHNgLYB3tSwZgcFmcvodaUBxwRm8U-ZgAaCXEeWrIdenWoStk_ITDZzzKb7q8I9CBbr3TNEU5sQOD6EXMoYzIwpbDWVdbmkRHGkec2MBdQ7X6-0x9WTiOMAe1Y-N6b71d7KMEl_ux-oaPrpWiecfKkvBneOLX-k-VuHbbBp7OhyqPmyGLELTKzK2k5TuAy9kSWToHdYl1OnAIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=dl_ABFoP4s64QZmWWAEj-SqvsDezaiOtXYqPplvDl02WNqtQfJqsr6UnOCB-Zci0nmuJ7KCLY2yXG_Cg7rqrBNizfI-iCwk1N681GtTdTAZnpQY6EgLuWP7M_Q_mGDVGKHpYcCYYPzHgYIB3PC9l1r7AThBouSaYxiFGdPMkEUUrQE1rNazcZU2TcgekswANg-8mkDyQIpKnhLztqvHfzwEqgXPc8wnwn0WyGcIvgojNCSusIm8NbVPbQVvqnO8GGNfWEGQeKS3QF-StGnioKRTmTylZaeZiL2iAksCXJK41KPkbBtRsFPqd6hE590CPxyAuSRPFzkO0nrPv-XIW4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=dl_ABFoP4s64QZmWWAEj-SqvsDezaiOtXYqPplvDl02WNqtQfJqsr6UnOCB-Zci0nmuJ7KCLY2yXG_Cg7rqrBNizfI-iCwk1N681GtTdTAZnpQY6EgLuWP7M_Q_mGDVGKHpYcCYYPzHgYIB3PC9l1r7AThBouSaYxiFGdPMkEUUrQE1rNazcZU2TcgekswANg-8mkDyQIpKnhLztqvHfzwEqgXPc8wnwn0WyGcIvgojNCSusIm8NbVPbQVvqnO8GGNfWEGQeKS3QF-StGnioKRTmTylZaeZiL2iAksCXJK41KPkbBtRsFPqd6hE590CPxyAuSRPFzkO0nrPv-XIW4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-FvrpW9FYXtj0vleB-XdLquX9R82VDL0SIMqxWtz1OGufnLtLNb94bbzoDfl26oRPmgweUgSGqGMAalqQMJMrqbU8kPBfsBGJZephHXMfLAgJ27qvRKZ_FekcXxE-wYbUdCUZpyjZa2ZhIe3uLsEZbBDw9T2UNxTfdI11hmGV-VQpCkuuhUj932A1jJefKO39ePY-cYi1ZV0URbbXN3L6d35k4-V6N_cOBg8xBENkI_nTccAE9mGxjGTrgQuGvyGPTTzYVokTKBLq3WgxGDMcLiDJ1dBUN69cwCVZezMC7o0FIHT3YYzOVPCXF7h9NT5Y6gMff4JYSn7sRYr3V_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFXpxVKydy3G6i2vaxT31XMvWSX67zXxCo87HGYoLM3A60yktD4i0QPwRUO5NRJl1rh55F1sFcAWH6bIYtIhI246HuR13u8izVw5ZjBnEBWQvvVOOVXU_peCnBmxo_5PWCkkMf8Vsx1ynIUZ_V6kOHLaT0KPkTZmdBhvhaf7uNFscHde1FrfE71JmG0WTzgs46B6DLpEjHCSt0YIxA2q5Ka0zlY7hwA9cwQw--Lq9W-NzT3qgt5NuzcM1wn1wccEuUhI-8vmF4J4FGpD13w_BL5So4AhJPNHdfNMkuRzo4NNK7_M0GGE3BiSxlcIDQxK46biUMsZg8IDJZtqbhQsi7F8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFXpxVKydy3G6i2vaxT31XMvWSX67zXxCo87HGYoLM3A60yktD4i0QPwRUO5NRJl1rh55F1sFcAWH6bIYtIhI246HuR13u8izVw5ZjBnEBWQvvVOOVXU_peCnBmxo_5PWCkkMf8Vsx1ynIUZ_V6kOHLaT0KPkTZmdBhvhaf7uNFscHde1FrfE71JmG0WTzgs46B6DLpEjHCSt0YIxA2q5Ka0zlY7hwA9cwQw--Lq9W-NzT3qgt5NuzcM1wn1wccEuUhI-8vmF4J4FGpD13w_BL5So4AhJPNHdfNMkuRzo4NNK7_M0GGE3BiSxlcIDQxK46biUMsZg8IDJZtqbhQsi7F8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk8_ZefuLwoO2raYNY4weSQ7WYXcUdVvvmBv42TlcevDTRai8n6_SyRYLRa0U-NH5SCrNaENftPH7w6J0rBkvN5XvWR0ohllhvSooBTbBO13IMnmrq1mm-lT3GRsrhVWB6Yws2SwQ7ra9t3ZO28M0LmuaDgyvb-yQKFzHJ1wSHXrxeQGq_34iCrCm6FhtnUla4l4tSnBwLBVpqz-kr2b02QfDXNQQVoimCBKYnt-JvKOSnJ0oZNNCWs1zI2FybPUYvRjqGOBRJYQN8DEJlsbqSvetafRvXn36kF1S2QV0LElE504v8LTpeg8fR4FYvlnpF0DCzrBeMqQzoRtB-PZTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkF3sLPPx8Fm2bpvHGhkmHCs6EW6DeQcoJqNNqian4lyarLhnCB-UVLGdSuZ8QvMR7BdUBujwoGW-PKTXIke1YUPLOmDNr89X--p8ymgVKcEsYXZ0mKnBCTTzrvFxrTBJZaTMWoPREYoFN4RgiFvhlAKnZqx6JDGZk6nHcD14wLcKCcKbQbYqciGR-zoGnBza1rcG-asIhHeFBax9O7ro5O-TJ0dX4ci6uDvwA_wUirdoxWoLphS_9irA9caO7B3EZV5xCOZZ3c8cBolKruv1GL54mtavz3TuuiT83FQZyN28waC6fk-6KI3fNIGdolecsAim6whcAwi-Ichz69V7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR33ZqH4fhslNqeQRr3U1zHmxxm1vjDc2i4MvG5XHj7eEGPSTcuvoLW9li9icWjawJsmp7sUtK0_gifb_bDtb1pW_DzahziE8LsUc_k49hbbV9yDanj4SMdRo0PzNmDw76g3N5keARkqZfpl8MP3mV4sPGLpuxH1Np6aSExAsK_wxbQMl0-C0pZRHvQr3rqh9Jc7gGuZVpk9BEbCGtOHmf7KRftP1KxnPt_2sEei6lWzn3_p8OGSLThPVLJ91T7shfM8CD0WJYMDyxdBFd59dv-T36UZxOk3RxSOLSxSj9IjKHczu5Mz1UyMi4bhJqGH42_IBUB3Zi_bx1RRDNvUMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OveqFwpXnvzaftg34gvU6v9drIIIsFTzlDN_SWxMB2YgXEtiDMGtnoppPF-UX4El0HA7QDNUFDxyjZ49iR19kjm1KEAv2F00mDC3lyDlReD0NocPbpQ_aGpAjKYAi_74SGtWQ0A2iGNBmMkzj5QGS6uj8fbUUumejOkBtvtzWyvkQhpgDDaeAKfzMwAvwcsfn40wb8rVH_S-SfRPHbYng3cI5zo96_1c24H_SiXt7_k1JTQE75_ryLHBU4y7woW2kCAtlPaeLVbgZRgPeQFw0NAfTCIQ1z0-nuPclYJtuD9rjGilEAo6gHJUjYyrGY6BmbmoMvBqtQWukFeY0oMoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQr7QKDd_GGQKxZm-7SBARdElWSjEp6YVFL1GFdbCrDH34srkajDBKbjj5KLM3UhIbnsNASnG0wnqp5TqV5bvNMwypHrGnD3QtoHm9ppaoohSya9VpHvn-75fD9SNlgqh26n8axRwRB3P-O5xhWNy_-XbsthLk5NxubespXvJYaHbr6hiTonhPdvVEiOyd9raZyTyPrL6pFgC0ZGt2UikqIj4SB2XHqDxMNrdJrRqhjNMFEq-vK31Gnmn4RzrfozdjkCa_2-SbNaPslQTFILei1V-WO12kyKWINw0DSstaZXns6Bo5VR6YXoZxCzzRokXqy3ZKg-YXsyP6L9kyzdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wj9usR4H8q_uLzZTFsVTUpEvUotBEtJBSOoU_HMR56xY_QeWwfgSP-4f0Qu9OTFsUbkVvsYRQ813IjyqqxTxee4LkSCVivkZOVPCx6RN3SZ3r45r6CBU_1VW0rk50zDjmjH2ZTnr1bQNS0VBOdy7nc1LAOLej6aS3S4sc5qHqWDQUm4EvL7hV8nw6CJyCMFgMOc2nODMucrpEhksaUkor48FN-SSnDMFeTmtzr0dv88e66aeQTnp1OQmiEKeZce-pmvAP49dWwUw1gyN6tiIY4YLqwz4ke0sWNYkMHYM1sIDp0YEuN9XvfllxgaeVFuo-W9yMzF-7xlWzCE5Zpf8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNJxZ8LYFC_4U4_XR2vUqmqO6mLSbHF9rW0XVoLYki6BeMKO_-rXVFerFWncW5JHDWJflg_b7OsOzoJt6A6_ZkOECiuJ_dpyW-jF_rrAmN3jhCeSLd7lc70aI4y0MFM7PQxmUPS9nJfdThrC5eQwzB1XCJtQSv1EE035MdxhKoO0RXEcuComVsXx7dnxAnTWZ12ffeZsF3pNGNZPG2oivOV7DocCq9uNOQIzsd7cmX1l90LKx4_pRt2_Kq3rIetcCzCzmvnJyqITmTrdTXWl9rjqmxsxX7q2lsyVlpFqoCJwwVS2-X4rCRF7robp9Q5tgOBsWsJwIfP6Ij7bbb7IzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnaR4BQKOjVJP2li6WUSBk6MsGjBb1qbG0bxlGpe7kd-0d1V3c5ydJr1qyAJt0LHfUZjstyh1ZVme4vjBcgRJit_RYMVmqvnfQnZe3YbtiqYiw4c9jt8ZkfEl8a4nOZ6ar9DkR4DQvND3COytwb2llNd0O916x0THWKGvtpk5sgyne7kDNTEij3qMWJKFf6TPxOSoXur4dQycIl9uzgrLtjI1eX9jEe-IOzl8Ra-beYv6x7lTH21CGBb2ZULdnfdqFk7pskB7JiD01U_3z4-kIWryHXEx1abPJFOOJZoXBnVgEcAf7BmpnfifeEQ8hjiM3upGUYoUzMXdMqAVL18Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3JXoq7RoSo-bTPerZUxXWNIpDXW1cjbOCKQgkMVkVdipVQQFy6V4TSvr6KxZW_DE_J2Fp_sM4oh03L20nvFBlc6WZDYv3xy-L8VjbeJave5qie8JFx2Li3if-QbT1k8f2KSwN-Ms8yKemhaLEI089MA4PkSPMTrZQB8GiZA0cFWiNc3hEHaSmEv8HFTRh0gNvVeVQmTDljR8qkWQlbPVoQD_Ax1osMjGkT8TfP7ppnVhzJ_loQghIoFILI9M9n1ZVMaYMwBWl9Gv6iwvnQMZlp_FHUCMYZ77uxK2JSVVT2qq3eZe1kHWQiBG3w_fcMmTI6iCjlqxr83eSeL8-Okgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyU5yt-odNNJeg0qgV0GQguLWOlLsOFulqjxaHSfGNxjvPAvC7CyuXO2cp_5x7M28vm75g2zvHX2njiGXcfEt38RtIlhCxEOqAyZO_Qg2htRzMBUKi1PoN8I0CUpE1AZz8PD9tl3pLQaym1HJlO_EbXFNYAjXggco4Ui9jd3m1s9bMk5HD0141hcLezyPR8yv0D0N5ke6pXvNxg878CiJ1LH15iPtI8r9ecEUMkjoeyRo4SCYarx2YcERXJZvGM6SssW-mXz9uALD-ZZqzgfrog9Nk8J6cdEZSv39tbwR_YfuklqmyCtHfwsxgCzs6-4eR_KLcoVOB45VSAUI_oB2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni6wz8k-KA48JFyH3PJb1qVhQGA65WZ6LfOSrxapOBw6KYy63M4p-uZ7q1BlJa0e6DUaYWfcl8GhPCMVpfu0dHPJky2BBj_EQ4EMe8RZgbznn8UEjTohv4OVFGrtNIeLdTMWUCN-seUPVh7JgBsnNqUkPmLuP0cIoSQ8da7aVnJmpuoEYpJu6njJvBeiig-R-VDDvYI4l5iRzJ3hVYiHxCfTTR1s_zvcTbsp6MPNSDEmxWkbQPQfoEYfPH1uXlNMDbZZpX9D3VdV-DVLr5M5K5Ff567ZXhR2_Rl9J4MaVg1FcyLNgNLGEGGR2Xzr8E6KzufumdqJN2TYMHxC8DWXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=JywHwcPszykRC5Ww2GOTDmkocjewoO7mUwox8oUMgH__hpgmpaW0A3-ribOG5yXKut2tG8koAsTrUjQvNbC0UqaBKCMzsCsNfgELfle1bB7ioXbenvEv0iwkRdIvJfBypOjFmAKG9E1dRxi3Qp4fFAfhACodR4FpdT05KxOi_gDTTC_RWKeIrFgr1HF4fJLlePTPEpiiGf3cW5xm4-H7WHCifPc-b5YHmmAPDSniBUlIQf_maQIr1wCDTnorkXUPLEDuegpMisDzBGzyodEkPnCOYPyCbdlMJygdXGQDwuLriZfeX4pfo9VaIVyfBpjzcvJIbO3qSWVrQr3uhmaSgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=JywHwcPszykRC5Ww2GOTDmkocjewoO7mUwox8oUMgH__hpgmpaW0A3-ribOG5yXKut2tG8koAsTrUjQvNbC0UqaBKCMzsCsNfgELfle1bB7ioXbenvEv0iwkRdIvJfBypOjFmAKG9E1dRxi3Qp4fFAfhACodR4FpdT05KxOi_gDTTC_RWKeIrFgr1HF4fJLlePTPEpiiGf3cW5xm4-H7WHCifPc-b5YHmmAPDSniBUlIQf_maQIr1wCDTnorkXUPLEDuegpMisDzBGzyodEkPnCOYPyCbdlMJygdXGQDwuLriZfeX4pfo9VaIVyfBpjzcvJIbO3qSWVrQr3uhmaSgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbLdblJbrwT629Jn0uMrMzXOE7vov1rEXJ2-xmfOiaCuQ_BcwdFIXaPNZ1mKJ5MTlzyQtZExHXlptBWk6txwVBwV2ElsgZfrlGNy3e7J7Me-SPdCXEimjg0vlybcQ5aaa6HQh1F-wbfr0ydEf7eqdhGCHB4ZEK3aMXG0gxbCV4irqqF3fJr-h8vwQNdaeHrSGHkGJtAKKDX7sZnPIiPt-WJZP2FgcL1fnjP01kD6ACUKx--5W-tEtoOxAzTWzSyYPy-DQ64z_tJPon85a7TY4wYKktkREE9_64otw2afIB8vCx4MQpCodTJGkT7zTCx5UPrb_BTRjeY8e3FElBk84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_RyImK1KjJ-JMgLHind7i0G3rICXQUg3aQETIOgejYK9xN3T7IgRwJjHX8wHIl3XxWZR_VPEurfzxYpsJVeqHHQ7STVgvI8dIUskq8mtgcra9hV7VvOl90ihHkXAxsXAR9KjsZEgOb1_AhIHhS9typUeXxQ9Ls0PmS9yBMTx84YxukIyvOPOozecfLaRGgxQQVODj_jAKIy0YGWoiD_m-wBXVvOctGJnLqsccZTbjcJd3PZvAGkEoZAB1KqnoET5hWRQMNejUMU0rvTFcHuNVVNhqfAhz27Ae6fGkE-wxv9ouE5QxrN_AHeQdlV2MTwu-R39_iib71palB9I_7alQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQArh7GdRUxSkP2NocUhbBpaAoyQCDTaHP27CdPV3EfQ-CpI4c_fQZgs23FPP2i_MPKJCVgj5U8M5z9tz0kGTse8coqffd5zLIVDR9EH8OkDK9PIyrUnKHLaektJytKJO6XsE0SnZB-lXRC2ic2zzp1Ivi8lPmtsQWItVr4dZCqBVVnsMLWphENtz5Gmn0HH2Lq3u392qV94eLVJfQfbJeK6HWgK7uFsJbbruCrk6asrv2B2psYa-YWORkNrKLIUBtjTXqeNkJfB0MtPES6vKolpw_bjadsQ_MiJOMmQsE2teq8AemYVBTZJl390E4oDIkK-_CGbeV9ZokSXV_NYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb-hwI3FoMqY7TQPcYmt3ASJPjnvPWitLsQ-fx8TvS_byk_bNbEbQYmGhRabcDwEiHCJg2qzBcc6wHJ8Cvn_vzQi4cRQbWcFruSDT3xdwfK8rryUW5azg_kjZj4QFwulPohTaMuSfjirAcWsOLDIHrZxznM1IS-U1e9Ylw2KWfzybEorZNPBFcyfSnFXszfUwE16_ppQajkYbikR5kelOYMva43BSo5lg4Ul8TSh1LJ9E2K6Z6dehv1A2NK5_6j4qYHiQLWXZ8Ns0-k8XbVFd7IDmQ4t-GlaEbE3jhDl3WP80AN8X0GRU6rKZhxIstkJHk1-vc3Y2wo3fau8-_clTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nvk0-LgzxNfpOojZetOqQcHP1GJBcKulj9ihipNjs3jjdNdFoaShIc7HlTlTnMHuZ1vEKC5vpxmBzFBorafTXw4vyX2CdphweSuB8f-m6nu0-wleAEviSumoVnNF_V-bNPpn8BaqRFKE7iEvQMETQK_GZIsfi_bRSlRIfjVU73yiE5LTpfad65mjKnzkBLgsZFggFB2f9z_5vsJa71-zBlGBJ0ipMlyKE7vNDEf6we1AMzLFGj0HIJArnu3csiHPiNHzfVvQkn6v6qjPawshZO0WJCcAO6_ev4RLABanW_V_Uvf_AGbCtVNXIX7Vn3WpVipZDBk5_NyiwBoaBvBtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4PkowYIOY9lzIlY14MCiTRk91jAiw_ZoAPzlRgR2KSVq2-S6m0m7CExmyy9r9fLN6gKzuwB9CVwoeAovpEceariO_JH_JSPl8UOGFURSXLn9_wR4iEbrD-uX2Q_gSLCGUyquLvLo-MDAIvxjfCWgc5wDIej8uzOtK7iGlgD1JC61_xUhcGzneXdycWAOuPtm64CRtEizqjHORDCYhLbuZO7GErspRSB8w-6zSoNDjBOTsR8t98xqL1Vv4lP9bPnf-by0bLlQTuc_w9wgBrc8AE69mTB-aZd8pbM_IeyK_Af9JqFANCq2Z15UPTQ6g8cSlDtnM5OVmMDSphEJ0SI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFFqjcErpv2ybjdJVoiiAzu53Nh5fDGPDcjztjyKYoieivXuVD0uoiE29-ZxSvBKHGGAqJExFiIzvNMjdHwUtPZE0Lekpcl_QCSReRTI81YCwQwF3KQMPYjqQFTVTGcMHpQljx5bDvgOXZJkH75RxSbX1u-f-On5X5mqWhhqwf-3Q1hBcTmdIlYGrL2COVE3EOC3Fc2Lkx06M6Ev_yX1ZwFKkIqNTRynwjxLABAWKbEfdbUUr_Kd2YtyeebBX-zp1nDfK1J8foblgyKViNK4EgfSnSPJk4-7mRsv6YYBZl-wgsjWp5TL0_gj7zPnvhFB8B64BWZ8enOofBhXQ1gcxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=Ajg3z-dLNzw0wBT5_mWP4MhMkKh053zAkNdCgqSsUZ0YjmLUQpIquDyvdHxl_qKzsNTW9wuZogziPhUkHBBFRURpzWRlpKRJLeeSJxOnKzvFsuo1BSeRWEvI_suwDXs0oohkOstWwQfRIllkxkxCN1AfUuV0uvwb9kw7m7j4tX90JhA6B561HOjzAeadunAY13IYlh9sD09QGTn7lRAyqHUphEiNyKhUs-EuxJbZc7d5wTAbGzg26PSC-Ouy_fAalRDnOuiRGAODkLbud_nhQ7cVnwHOpBQ3IZPtm1moqKqWu0U_riHu7wp0hdtomT3lzefFVaHYfjxEJxRh98YdSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=Ajg3z-dLNzw0wBT5_mWP4MhMkKh053zAkNdCgqSsUZ0YjmLUQpIquDyvdHxl_qKzsNTW9wuZogziPhUkHBBFRURpzWRlpKRJLeeSJxOnKzvFsuo1BSeRWEvI_suwDXs0oohkOstWwQfRIllkxkxCN1AfUuV0uvwb9kw7m7j4tX90JhA6B561HOjzAeadunAY13IYlh9sD09QGTn7lRAyqHUphEiNyKhUs-EuxJbZc7d5wTAbGzg26PSC-Ouy_fAalRDnOuiRGAODkLbud_nhQ7cVnwHOpBQ3IZPtm1moqKqWu0U_riHu7wp0hdtomT3lzefFVaHYfjxEJxRh98YdSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=BkQZ5SFOikzjSBjZDHM4VbuqYFvQHArft41uMEzAvDSMgRCBUQm7Mi-brtBCWsIYBD4U7gPomFKEN-Sr66uwm2gvwbOwERbchsXhxSRtKgotVxjngJEIIX0IBbnGTNJHWQXYrhOd8hJDwNjZpQtByl6I7VmquMtHIJoOsrzgwgmG6JM38i55hOeF3xbMmbNC0ZiAYQmPSBG1rCuekVbxh2YU6YzN34xYU8xv069ucsZQDCsGhPthIwhMZK5W1Y1lLt0d9I0ZtqcJbhDXGVsXnGoTKP8CiG_K366DSNz7w1Yzde6nk_8gNap5sdvMtRyBVP38hTGeY98p_Jk9NpcVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=BkQZ5SFOikzjSBjZDHM4VbuqYFvQHArft41uMEzAvDSMgRCBUQm7Mi-brtBCWsIYBD4U7gPomFKEN-Sr66uwm2gvwbOwERbchsXhxSRtKgotVxjngJEIIX0IBbnGTNJHWQXYrhOd8hJDwNjZpQtByl6I7VmquMtHIJoOsrzgwgmG6JM38i55hOeF3xbMmbNC0ZiAYQmPSBG1rCuekVbxh2YU6YzN34xYU8xv069ucsZQDCsGhPthIwhMZK5W1Y1lLt0d9I0ZtqcJbhDXGVsXnGoTKP8CiG_K366DSNz7w1Yzde6nk_8gNap5sdvMtRyBVP38hTGeY98p_Jk9NpcVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9wup04ewDrLaUK8vpyOGdi7KRqjA2BHmtqwyOlHoaCnZZhz3OlN4YthxXdeLXAxi38Nts7BAVbABtmFtZ7F2YRk2wmEv5AhFSGWbILtsixp73Dx0VejCqF8WxxnIEOgFfm977QVpBDCaAz6M6LUuknTtNoJcUULQoAUp0z4QZ9g6J9aOtWkNHf-ecPkB9zXUxBQpp3SXBSEHa6T2n3-VIYTGKMQ8Tuy5N1Kcbb2-ZMn73AfEV3H4kZ_UTFw5OHjZsSF2AtFuQzao7lPrY5vlbpwj7y44mxwOJhxfFr7pH37tUC4ITU6v0duDz6Jmycx32lQorAIiWN9aaXlmA76Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpxEbm1BBnFukm5Eyc6k8j_VU4s00jykn6A4LadzVZY2yf1UdSmGJaVtQfFBDJPWu9sMLapIpB0TAY078M0dNZ4snyAenWwYeSeRHqlKDhyFyZOhaQ3vA_NrhxymbwmL0XzjWU41Xr-hkno3Ibijh0yGGrdRSJwQlO5uoF5RLCFBiDqXU6kQIWzYLNGchXnhvo0CezKVZGsfwGshnhPqaUPmoFwq9vUZBPJ_HSO6MtPHqk5N3qjunGFSGEOHecWQizzO42YbnHEXuDYAX551N0lYwa-LfWSCdQQbhcS3CSBz7O6vdV2Ow8x36cOi1VCObQmkSA2zOcPRLzDQaQu9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
