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
<p>@persiana_Soccer • 👥 210K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 09:08:48</div>
<hr>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoRoYkfEyp5ZaVw908e6n-8jbGXUZnzyz6UkLAZJ1VFivww5szzYzuX98VKH7EZunTnXDuAbKknU9whzBKDdBwQ12atlVK0UYFBCt41sU_6hLBM7x-PBMiRUOx-un3Ng-p9bEEg1_RR2ze9QGsXjy9KVdg1hFjTjypqfJJpaIUaMAx_Jq4K5uC-NXaaS5fe1cVvbwO4ouib0qCCW65mlTJZmlTjRTthBwuOjWvzLN0OChga_grgokdtbp03DcOVYX2kvjRss-cJf_k1zu0_EcycxBzgiBlRitDgD5LQ7W2KKYCRyzXnuAtvHoCvPiOVfPNECYYICR_sDxMlPZW18Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_95_oN5pAOeuhObHOKCQu9U4mWRh_M-LUZ3jrIKQ60kINlh-_zbkm-Mza1VznxnDo9YzR10rp0MndseLQjReROMBURAs2Co1gD8vsSYVStF-bMTFkkTw72E6db9bhKPEJGatI7J4nMELPr9AXAr6gabP1NhzI3qtTj-gKLnLe64wwtZfbcZQouALraIbQdydCQ-sbmgTWfVK94pkh88ACgizGwrIKZmCsbKyexXbDbZKa0jW7hMQE65Xtstt7_0BJBcQBZ3ccx6Gsu4nqiwxXAn-OABMMvsn_5T_n0nALKGY-uSotK5cyITXXdSta6QU5NjPA80Hy4OrMJdXrIprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22144">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjTs5jayIV-MbS72Il4zGGnh6DGhE2n5T8bAuWGW8gfGL9DehB_9Pj4lxIHh0IMn_1_cb4FLwmBT23omLUcT7k5756U1zxtXLXt6FmBGuZweRToCzDlC3hI5FL2cwkcpYfVvYQ_hYTFS9TVGg6B1Xecr_-jbGhpJ-Bx4pILvZzuyaZBgSr5newFJTkWVfSHIeefTH0T5hLqfPdelH7MnOdcnm6jC2Zvi_3ICWJZCcWsDPYR8501Ru1A1PwJ0jrYRGmxz7kIDoXdMUF3OwXdF0GPdumjw7E-Tdyw0kTJxQc-_Idn0vmn07W44Ar95_S24S_Z1R4xKMlzpU0A4_kHhkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/persiana_Soccer/22144" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evrGIhgOP7NiERScBMSeJEUuEbb-8bAwB0KMVHYhtyFAiJUbVvLFiosecGwjseJWXbAM0QABGF8Pvrtvl0AE31ljH2GLPwWQ8E8eyqn-pCXlJMeXJtf5_vhsVpBFz0OsNoWYdt8hpujDpd4_pOKLMtVuqWnuWKCjTVhwD_swRogAXo58deXhrV3Tm1EXbTDJEl1A6Nen-8mDTnpczva3KDDykm_ysgu3QcVpYSUpEevJKQg-WE2Pv-6EPs3qQ6tbz26XcntySNQTL8VhEN50rtXhToqkQyHnTdLkMGY_vsF9nkYV6ehmMWv9BAzIUen_IcTGaUr1Uz3Hj64_UwPBDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqP8iIQnxTTOT25mIf5zQacLD8XvYu8HuwF-cHeN8IK0sPAk2qVGPV5ncoDUQvBTkqjWYq5iIKRx4rUDbgqMo6IREGOUMh8krVtC757WwGTRNPO-VJs19uPYqoY-BcH2UqEv3QImFp0-M_fIKqqADJP9qlWTVyeGCLlGx9vOMDEiPaT6GnXcmB1eetNX0Fy9fre0U0fabceR8cXgXBCt8qDE6YN887tuLTDrlA8RcVizl8kSiH9ELXpLmGvB3plS30SCUOXz5vTSsz0ICBQFKApXGZidcVFPti9WO3k1dEF8EvIaHSrNMnzh7wO0eCgmrBeagOsLAXI25xpsg-RPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqgN5LOZD2Hvdzefze-K98Xw7NAEgWEMQ8VVk2KWOpkFuhGEZml1u6tmF61Hmt1LEu1FOtJEWO08BhbFpfqJKQ9mxtx0_dwQAcHyDqJwl2VHXzpysjdGqCiquvsOwbsv3z892Iy5No64pQjH1OG6YEDyBS727R6beTKja3cYzFDIydfbTYjG7n9niWEw2jKpi37qWIgq0_EAqL5zSN_3XijXXje6F2bTALu9l7tXQ2-w_UQSpwa6El04Buif_rFz_YTwmeIbsY3vR_WmPyJqXOhQeKnwURBSBZoEs-ng_0NWeylOZivw9m_njhCl8_h_r8c2mCb813jCB7IEWSV9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22139">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗘𝗣𝗢𝗦 𝗜𝗗</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZkgQzIh6HZctZyzEa27Vwm-i0KBreWyJQcDqQy6k4BkULvVv_u7nKbQ49CHmlpxR5WjR-aor_smeztIQqL4goc7F4GemmvbG8nuTNqU5tl0iNwfYAo3gsDTciJvtLm4FDmCIVFpKxNOWtv4vJmyyyMI3CenS9zcLaVNxETkbXh5o0k02J0PLwU-cLyDvsZ-ZXlJXDyP1kJNyyTOV4ixKrgspwhFtkbGz34iekg88T_x7FxaXaxO5eBmtIMlv59SnzDly3zFNtbK3CcLd8i6qjyz2H-oUiUiaWn9c5CbKVCyWQuY4DvXgcvQ73hxhMvHz9OO5MytrQSvOn5D-xnZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
💰
شارژ وان ایکس با تتر ترون معمولاً دردسرهای خودش رو داره؛ کارمزد شبکه، نوسان قیمت تتر، معطلی تأیید تراکنش و مراحل اضافه.
💸
من ایجنت رسمی وان ایکس هستم و با پرداخت ریالی(کارت به کارت)، شارژ و برداشت شما سریع‌تر، ساده‌تر و قابل پیگیری‌تر انجام میشه.
🤝
⭕️
برای تاییدی، شما اول مبلغ ۵ هزار تومان رایگان شارژ میشوید، تا اعتماد شما جلب شود
⭕️
✅
بدون نیاز به خرید تتر
✅
بدون درگیری با کارمزد شبکه ترون
✅
شارژ سریع و لحظه‌ای
✅
برداشت ریالی منظم و قابل پیگیری
✅
پرداخت مستقیم به‌صورت کارت‌به‌کارت
✅
پشتیبانی ۲۴ ساعته
🔈
آیدی چنل:
✈️
@EPOS_ID
💸
آیدی ادمین‌ها:
☑️
@Agent_ir1
☑️
@Agent_irBet
⏺
⏭</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/persiana_Soccer/22139" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7rOnYaNqSM3-x-3e4Mi-FHsiG0ewKdbh7iHfgsbP7nDYtG2RhiSWXk1qi2QOj95ItR1aog1403wlag_eMNJoNeXdoYyEbl7yw2_qP_PNiWtp1GnGQFcLMA_xDybJ0GYs81t2a4LUrwDgpVbRvXZQJymnQFDzxdaRVKdUU01BHqtu5QXg3nziR9sET82hb1ikAkMJiPNcQJ5wv6trZZIsfV_D8obE5qVVwodvzKCW9nXCy9qqPt6CugdCUn-OG6C6n_p4apj6MawAxit7QmX4Xx6qsRFsAsY25lIi0qfnYmP7SpBP0jqrwEsdepn4StGSpw7jkTzTK3MH7chi6NuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HouRGZKllC-DUxe38vEs5IL7bHXLe6J32Yhps4GmGvpUY4GRD4rxz0uY_k8VkFNG1QjPtjYpjeqJH6sve70pEfMpKmINOZQDPSekSjX4_9CN4PEPrVnGNnw8mhvcxWQjJ0oglcKE-0A9X6HdrCHXreBHnXGIuBEE9PyH7X4rDhoI147tazhpFglVZOC9NA3oJ9EjmXAOFn2UZpaDyXPtD4FKmKkWFFAeqBOP-zu3gN_s8_4P1BmYmSFGj9mplKTXhFalhI-pm-3YLFOLI-RzQ_96ihr8SX-wLUixL3Aq7YpC0U1tKdPmR9N-Dxi48zeRDHVYfl9V1XYAZ2ob08ifBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orGYViA2WqwKGWC5S7zwYlfhqbVViGhpBo9XtJVDAnXsleap-NkXTJIMFJFqa6GvigaXna33hyyknZp62UKa4gL6l5-83djYkLWwKrXdG5fdCmJG-tz_oItixoO7GJlU8JFrMFBHKfW6vxG0ixFgik-vqh7-YDmND7R9BQi8_6enYfu2Yt4idSrax3_PArNTtcQ42JhGor4crSTzZOv29gCXEsHY7WQ70fONggAHgL3Iu88bsLFgpdw6ybw12F_MNgxy7b_zsqMZBeU1JOrlVwLIO6jvvkpP8hMYnf5zIaWDMjUxPJBh2_CT9dnwsmXHiG0de9SL3dTRQN1_4FP-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neYhMqH43S4_rqGJvDPy_I00dT_O0mkEurFFRSobdRandEdbaPUk01bzs1lA0ufubWEdQr3BYzkUPHHuNiIAFaAvGq2Nw4OIOeK5l7kBGckKmubylqFZCK-ytoFO7d-lFUleZDQz1XhatsESBouyjDNuoDrmy6QplynT67WyWuBSi9aicqgq9GJZpRJi38CnDn_I36yn0QijXBzzsIHc9AjizdB4jDMQmoVWVVV3ZCpVbHtcdS8u4lgNL7pqFq6-89vMvgeMu3-sjQ-0750xP3-B-_kPruYBepFmhjsHjRxJ_CXYY8BeRLrNUlwC0gaTSYt4kpukS1gL5spJ5H0vHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce7s4ke_tTYnreXVKu_g7XaWnUtNn9GLe2UUZXhQxW1oM2BnwQ_0CFFk_IcpNAEgyfKLhU7PGCFsqfhvDk7qbCyvpwUs0ow6jQ47idiqEhNAWSioAhf4WW6HCW_kHTlixCjJeulAW2Jc38Mof32Ku8lirGrGXqOeo2iVldS0Ax3pPjolyhk-q7hvbiyHEA5-MdE5xZEa-_Fd6XZbkiBZ1ZGn9IhBWXoGzBGLlg0_RpbixdZoXTx1li5R9HCDmw7rjkhHvvuz8ibyWxeO79tRlWdSC-rQzvouUgfDNy1ZlS2lSn2pjHupCA2HsjFJ6pXRHFQ0ddho6SSJpy7OZjzp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=jlX6cApVaGAJ3eIfdIar7Qa3z5hbBMZ4rwPfvCHQ8boNw6z6LmaCopdFD8XVO0MWazwHv3p9cF8sll5iYsvCtjcPnyhS7gCjX6ozgtYn4Gu7mMt6b58V27boOQ5F976TDRmKJziV4fWOLrFtS7PuzrDim5_bDYSME-Pp8LUAZhs2LHRrPazN7Viq2wjWzd7PMNaXHcTuRXibd2NUmfDDOEs_TvsOvbH_OgsBdqelZJB27G_idgrPYh052VidhGzVFDD1sCpRrIGK7nqljtKYKpA-STsZ6ZJZIZP4m8vVR7OjQaJx4D_DR938aw61UdiAWrO_BYV4dRaDnuiLIGjCVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=jlX6cApVaGAJ3eIfdIar7Qa3z5hbBMZ4rwPfvCHQ8boNw6z6LmaCopdFD8XVO0MWazwHv3p9cF8sll5iYsvCtjcPnyhS7gCjX6ozgtYn4Gu7mMt6b58V27boOQ5F976TDRmKJziV4fWOLrFtS7PuzrDim5_bDYSME-Pp8LUAZhs2LHRrPazN7Viq2wjWzd7PMNaXHcTuRXibd2NUmfDDOEs_TvsOvbH_OgsBdqelZJB27G_idgrPYh052VidhGzVFDD1sCpRrIGK7nqljtKYKpA-STsZ6ZJZIZP4m8vVR7OjQaJx4D_DR938aw61UdiAWrO_BYV4dRaDnuiLIGjCVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK7NqZPJUM1FujZlkHxjMUj7BpxfP4a3Umu9D9YOuyUMoOx5rdCm84RNSPgZgepKGavhaY2LsI3t6-bIWUlkWdhTmXO_F0KnWDdvTv3ADhZlvw5lT0Oym2TYjwq7DsCjcWMkb2vaZRC5Br-g-__4CSNSPVT9bZopPdQ4XaX7qlxlyUTUrzut4qWY6lOomdEgkMDT31ecm1vBnPTm6wUOBdpti8L_PDT9Nkeft8q5XoZRgZjRMHL9lC1Jr8jHk7967Fs5XykEzh9DIfq-MZVu35O8XuTJ9vzPUaSfAGsf459qcTVOBnWxN9aJGtYQtSmgnVJczTNdVGlxYJJCIITtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAZsSP-KgjTz4DHFqH87D-GqzV4vcx4fV81bIu_5ByhFbmA04Qk6K_qlsbSTD9pv0TCa_ZuxfBzyxHfxZ6p8LOa2kGIOKAjgBN1EIqQt7nFOb0D9aLX6cv3-DKxDXXIs3_jS6EO_YTPAM7120mkRmwGb2exKhdyHBH0scjMW5RH0arDfDGdkUWxtBCPBHU-Q-M2E_gnAX-G2QPVRQLbG-gfWrroHCcwrxSbHqysB0ds30JoJLzjbuCrbovXqrG3mxBbJ8KcayvJ7JCoo6aLTOczFrD8M-ADGFaTR_EW9jRdCbOw6bzf2N4r7C6QUOEZt9ijTTfUU02uWS7WGvwpXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZjyqE7wTKuVz_YmjiUbCvRqdMi-kAA41obeYkhy3oWm0KX_PRtMkOE56z7H7y3sTLJrVtAc-MoQts5YudvY25uHyTjd_o49kFDOFdhf0qesIJDB--afvMl4VKBQs0i5uzBXth8_vOkqgSECk-FdaSohNYCaTaQmbhQd7VoS8gWD9gj5fWNBTJeaGupvEwGMly98QU4Z_AfahnoKoCX_2G799xnqlbJKz7JbxkvAnBXvh__9Eg8MyWh5jhpOsnOmUYIoiRMaG9PI7sF6XGBJj75gE6IlfV8d7YqDsI98eCAkfuKuCMI_6jZRFoQ2JgXBQkzT__ardqgMGuv5LtRj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k42BdJZEKdR8GdlL6DQ4-sEws1ucUJYRuSJbPKQJ-GM3Fx_0jYcAjvOrOqd6Hx2uTDK4qRO6zSw9dsHI24l-1JyDECYZxUNkPUj-vj8lPxLWJYd6aQvnnlG3i-QqAmKnGW4R0qp_fYZMBV79TmbUWcf0yh6a3l5ZFTiCyMEm6CYSmKOtqKnsTMvwYz0nfRk8FlNgyhbqf_k6QopipDumqrTc7JcWCmE1f7W8khuv5cewm1l6pH_FSMUI1fSM9uYxF3Uoi0l1UpoiaR6RhpL_joXDbW4TuW5uRXR5-Ib1XGRXw7c2SK8h2WwTm1SI9h97C2Ex07S2GHycu2anIxpOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO8XcOtst7VVpY8r0O9dtEIHmkL0qzEwnhiBxtvpJYbMcPC42Uo-4j5h43fledWMl7UunckA5nLJpxdgnamBLs7zymmgeUISupfevebD0gtld6AaC6nTyLpaE_M6uvul-O2eYDhtb4Z8ppLrzs4qEUUWxo8Up1ijWuMTFLIqqs4DkvVtG-4U9AmXitTLAk8U7g5ez0Kf67OOknk1Y3IedK7KVBeSWD5wzJRIu1CO9Lgs1VFeXUVTK7e_-dz9de78M516mqMTL32VAhO9wMw50dWIaKocNAZzevShds4ZlrxoxQeqB_gERAfedOUzCx97bOOp3gLKngBNjAUofJgQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORGSskuYyOPVS0-TgRAEc2s-AGWcefXloFZgUf_2RPpm-5KIlW-65yZ1dqjfg7z2kkH17QaVNN9o3Dhg5RaAy7OJ10yNm4tvpp1C_2U3-HIcuycbj_mHuQZ1bIKT5cd_clD9X8PEYpunQVHfTH2BagB26V7FkqtWi9jFP6yCWDyjGGmsplsZ0nTNGElPIn4xlv_PbS_ymdwyXaBMiEhFg3kvNORDYFUneTFU7Nk844GIXecqXWcrMdVEquOp2rgBrinyEot4l4HlgsVMyaocj3zV0xEo_YisZLeLSpEb94G4t7IMZVd78YYYw8bpdmKF3JLV7CwOUueQKnfu4QlQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxx-7-CTz_lpR-MVsUSxSeW8Pff0-9qHGQQCz-MvM2VzT2WUd8kN3JY-09m_wroeptCvEg2ANh7SF9D6v6D3aASESQ2BF_kDXfpUupMqq02J1ab12nCwB4VJZkasNNHbq3Aamm-WqyyxncsIsCNSHRPztVi-60f0a5qmiCRoMHY5y0mg6zaHbfwreiUJK5KRMIrzjZD4qLy_p0-lranrj547IIB-QmNClroJ-UIi9Yf84Xa46EOlEONseg_-kSDCGeQSP_wBGOdIryXGtewFa9Em9Z2z6aREzOi9pXMrY6xNXU6ZCeFSCzaR_Pg2PdH5thjb2UPH_bsw_KHuIJpgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDt9YIQILsKHApjR4cqV7_9uOn5x_0iqoSph9JEUbpHWTaRISBohlYV-e-sgyK4ZXrypHXBBKvLC6gb2Hua0B0HvJ_eGrY-M5E8kaQX1P0cjy_yMkUofmDhir-sFRG_ho-q3tnTZOA0IpMqZg1nOB9FghkRs4WeUHbzBB-o_C-znWFuN7GlYJR7TYDPbIq8bhHwTa0S9rrEzWmBXof39RxSt0Zi3fTJDJD8DbIH3O5hjsuqgm2LeSN1VF0mebAWOhssi7V_szefm3c2Er_M9iZzWhlxO2QsHfh9PLL1eFCtTf3cM5FQrE3u0RhN9xhfWWjKNv3Vlid_EpsQqdnCAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=plyM8Q4CpJZcXtRz7yziC_xhHYm6pd07MtrJKK-ehmdVG2mzccgNaZS07lLiO3if16pqDf2YH6Fq7ghqta9lQ1QEBxIwgcnE-OEhvUuSJxHRpyovLJkwD4kn8TXYCtP0hpU24HhOsgEl0UDSkNULz0GsIUZe6b5ZO21RRdleres2OSNeyhFMC1MUldzmwVlYEVbbjx5mWsGXzQ6eS31TKcSkiHRmmRxEwcZ-figxox_I_bSgINhyRq_HwGxKZKyV-iltAWkYmjsYKY4DKgzPffNlBSa-kTVqh_Co5cGWqBA-XQqKKPtyK0nNB8KV-UcervIYMCyRLdMGvoIxd3L7Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=plyM8Q4CpJZcXtRz7yziC_xhHYm6pd07MtrJKK-ehmdVG2mzccgNaZS07lLiO3if16pqDf2YH6Fq7ghqta9lQ1QEBxIwgcnE-OEhvUuSJxHRpyovLJkwD4kn8TXYCtP0hpU24HhOsgEl0UDSkNULz0GsIUZe6b5ZO21RRdleres2OSNeyhFMC1MUldzmwVlYEVbbjx5mWsGXzQ6eS31TKcSkiHRmmRxEwcZ-figxox_I_bSgINhyRq_HwGxKZKyV-iltAWkYmjsYKY4DKgzPffNlBSa-kTVqh_Co5cGWqBA-XQqKKPtyK0nNB8KV-UcervIYMCyRLdMGvoIxd3L7Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMy6AWIkGXY3opc4psOgw0v5Yt27JDkp1Pa8ouFJ7eERmDQyAwVtIcCNBFSOe-IJofn0H51p-EYfXHEzPUWukGZ9_G9aAquWQnX4FMKEyaKT2Yl2mxBDYPBfhTTtsd3nX0RUiVFtzq8S4BMkszcR_vAe0GsnFFxPY43oO8GOFH-GdoMC0R9agx9A_XVGhXsKMRN0zjRtDeUw297USoPUxzksY-yy_J9dQTypUpgJV2IEYhS1TxKfIEnXG9vJ5jPNPGWpW0ZYKotBNdNdWtlsX29nHQQnT1i7kKFfAivN3qu8aU_TLGH2p6BtmKx7N3SwmJtMXa21WYm5XPwBSAS5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHs4o3dnnLr1jZNJKfSxDrvT33D4HehH8520RPMuBSfxf_Xs_vp19g8RuzbVXXuFQ7mDDr2reVcmmjqLLuYOl3YaCzRocDqhiZOootjkJlqdEIukcbh2wpbHsuWhS54DCv8ZW3VPVeFwoAFlhxx7_2t0W2KFhcUfeZ8PNeIi0qyArsckOVhiTPg-DAWBDBfTPa56jI2orobIlbjw9cwWSPqKeOM4CrlIdWKW6Q3K-TbgkXIfTDulTh5P7Wbnb9I3OD33b8mFhXMcLGs_AH2a4YG1BwsoRdcYuWU4MlhNspq1kqIGXkHEm-7N5naU4v15QYzLrTYIO_j1y50Ctm2kzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=SKTlnC2G58CjQj89SCZgzb7ZKybNFwUDTRr3GVQxmYwrB8rudI3HT-ibAYnG3fMotAmZEBvVVkLFy3-F2qW_StohvvTN-eQW-GseyBd9kUm98fOEMYEtTBCLojkdePbWyagTwix8WYbF01wjajjDkyDT1KfHRaorA-ZZuYff15QayQmtnznpi_MPykFJ13jUbXrauF6-zHYpi5iYWBEiigfdn7D_iAqdWGcSWtcKbWmyY_3KxGjpUc8r5N-KnxD9VdkMUFMiwN7Lkkh2r3eosEar9Uj3NEjjcoRDhDBaTdTtcfUIB6Q_gwM1Dij_jErg-mE3SVf4j7f_iRj8VQJd9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=SKTlnC2G58CjQj89SCZgzb7ZKybNFwUDTRr3GVQxmYwrB8rudI3HT-ibAYnG3fMotAmZEBvVVkLFy3-F2qW_StohvvTN-eQW-GseyBd9kUm98fOEMYEtTBCLojkdePbWyagTwix8WYbF01wjajjDkyDT1KfHRaorA-ZZuYff15QayQmtnznpi_MPykFJ13jUbXrauF6-zHYpi5iYWBEiigfdn7D_iAqdWGcSWtcKbWmyY_3KxGjpUc8r5N-KnxD9VdkMUFMiwN7Lkkh2r3eosEar9Uj3NEjjcoRDhDBaTdTtcfUIB6Q_gwM1Dij_jErg-mE3SVf4j7f_iRj8VQJd9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upI8cSriONBh34NdwZnyZSvqSgB7dvLEPYe7CSGhH1AjpfbgRu-zQIEEdluaPxFdGzxAbLUxq6hIk9CB6V6GoxMHOkHS0aU8GOlC8rPUZ1OvFwimnS0DyXklqlTUu2CBzAS5OlWnU-zKrqY_WEVw-p_acfnO8A-Kk-A3ONG6H8WK4klcIFxZMnLFnhlwYcBfMwYpMGQ4kpwEgMnjQaJsDZ07Hc1HpLozn00hFXCgGjbDLiHEHnRhiVnMaBrFzT8m2VOkKac6vk26l1MfrjMTndXXOpGellzXE0Z9w19qFdpv3rviQSdTdW1CMisPUN-bg0WUg0TFMrizNkXwpjslMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IjzbfOgCQbuhkMnifWda0uUUYTGwgJkJuOiniyqILgo8js0WIm0HCkstZ5nWQO7wqN2kHzMg_FZZALb2GIAa9b3DVF7OyY-yyuBGipPWSZEbKIp3r1xdArwA2bNyEi6R8Xe58WV5gmjjyFhDikVrXpHFtNm7h8qMme-MZlkq1hZYfKELFAVoxZ89fZE494FaMGtMK8wP_1sCoBJCOm2fNFeVKN32uXLRlbkLemj0_Qy79D9qDG8-Zv1_ws2ir6XtKMz0mjDQkqYSGFHLDPNlowe2r4_SfXrBrSpq211EINxSUZiTIEe-mfttemhFqEoyYy5gKD5i5WLClBLr6xI2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjY_iB1N95n5FnTOI-dbNxBnan1MoHllayXWQ4CagFsN-Z-XoK2OKqRStQRNnkZP8u1OElfVfjd1e7au3k8QMPSWiVw4_USCbf26pW35PbiJXkruRuO36fJ2NGsvvc2ps8650xD79fukpQjo-nrWNHRvMVnoYvSZXxfALxKGkWRYWyZyi0U7GXJ2VvfOr9FCnIxBAzRWZ86My5iXUDCxq-1ODHrtLFZwg6hDtBmzOUgfB-SBWqmhNwbB-b9W3grppJefMXOi3ZeYOj2hj388GnZxx5WD3t__f80zGC3LwPLAu4TQMhOho2h1V8T4k7E9PtZw4nGzYWiToLECVMGEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rusbEwlwyV5fAoCQNV00Of3qiAMUJ5L1GKwedPDLPFucaq2aFcwpks1RaHf2u9DyA17c_tyFqgFBAmnPQ1kFpVsSD45U9hBGjWNGtSA09_HilE5luPTjlbjDfWbhua2EGeuRN2_3g_qy8IlBVcGvXduAQovQ1ckYyOi8RnUDzEvHrbqtYYRboCZAu4S9xKlw5hUK0NqCa7PFIj5wDT9vxkqQrq49gZPz6-qW5MYgiL-ycXQ3R_iXJc_KYz964NIyvi4o9rgpfdz3QiVMWqog-heDAObxMgVKTtDAh0Qqd-nQRQFeVM9Wg3UE_yRwhNWlnzZjg7q8lpbXjKyV80Pl1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHdJCGKTXXOTx2icsstEETZp6zE7BDl_dVfXelEFeC-w00X_FC8DQBaizZrnn3WtRxPsDAKu9u-SuFIoZxohQGY0UHFTHL6FMDLfJIrRlgUgqxodvW66Ti4yMKaZNY-xwZUDFCmiU_PhGXIwP_b4vN0qBjjlo-h6W1rL4uXi4qFsPvmz1npc--5_sqT2XN8U-nr8uURo8KyufiHvNawgJ35MR5hLBgFlN_fERtoQ50XrigsM_9imgnGcK3V6OQN5SEbhfrrhL3r7AHykHCEWZqwZWGrAvFnsBdmnOka1AgLlqg6uhMFVjVXz120Yw6Jre9t-XL1qhxMO_bIJprkABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihbhDSswl1d4OHuZHJHXR2tscxx2Oi2AddnK53yaL-e9g_EO-pkW06955cdZbrL0LFOkOEDr35prTLs5UFK5v7EtoIeOqFVPAUeSLrKlXM8s4Xk6nW2ZUvEdwe0yig3-hwMu8DvDMSxoz4hIvqJ9ZBf7OxvUQ7y1oxQ3TjzPe0FVFRr-d_RpyAKxXa_fmKP9G7hESG2Ui9Vv0ijTVepE0rQ64FKtb73c9v_a9wogd5q0nn-d155pnEJw_MLBLe5TJ9sPnNdBNnTvLJ4f4zyOKitI9putlgc8w2E8eeVoaHufTDhRvum0hMfsaTq9hprpVB54eFUpGiDCK905VZXL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw6JnK7AruH_WftKSVqNrLQJC3tSMaeSSrDAkoZSbcKTGNQVyFzQSdP2SANkchwC83fEgR_fqRxwBuxI4SbjH7bUpHWrDeddjlaggy9sSFxmLX1eqw-iDbImJ1DLWV1azWwugHpkldwxsgsOFFHPlkEI0h0udG9xHpbtC0GkPhQj8eVaILiRGb27XCOwC7HXpLbRnDGC4rLA6PiA3KZnZae6sustzJzdakFwDLo_hL3HyHCZDSqYenGN6Z1rNQy5IT08hiPoW0vYjocFPhP_OINhK5596nHDP9bseRvQ3Lpq0xJDCI3uFMxC7cT2WCbM-_4D_8pwUBp_m2m6to0uYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZjTSBJFrkpe04OO6b5wM_HVmB8z0WYK-A1_J8Nt-WUFoao8f9ECyFYb4T8tAOvpyHmmrqMoz1rcStG6eWKjE3dLDXC22vp0qWDReUdpIzi5u3aGrnvfRuLZYY7EdXTcvB7a6LSlE5ZrZxtr7Z7PVJrmYGYpnyKVeMqi7ghjBvV9J0C1Aoh4k9ZYUk23kqHSJPvxQi2n7lXbzsJ9P4heXtc3dFDx737xEZcP20_S9hS1UyPJ204VvjvGLGOmUTdhg1zLrSJ5-WzxxJt-kOrZnxeodr2QIDiJXVf5KisiHND08yEgG_RdqD3aZ-78WFViXouS9WsXx9JycoCpgeHD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FepaBkJBjSFjl0bYSFRoeC-KwETsXFBj_0wuCP-puHKrDBWIAyqNRvXYJ91KRf8Ednf2L3q-WTGgGWE4-1X36JAcrk3k5EOJEPiylJ15d-YiJTdni5gUxOgsS8oYhF95ekiNKGyPVMUklS1vV64oGTX7K13g_s3Q0EUiGYuyu0qsgVLHp4wCx9WcvK2cD1gSljVUjgUPivUAaxtPKvQJ-tFnIx1Xk0jO2uiiBlufrb1pfj66t8dmN99NbnXJYI95HRn_S8jpCM4btHLia4PnYMygTLilMfkE3aElV3FonlINDJMs63Cy0nKdOf2BNTJjq4qEzyFjp0n41CfxzeAUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kq_740McddqbgY1OnNN4JVPV7ZQWhAT0iNhy1AYN-VSzmtxMZI30SFOi7hG4qisSMrmw7JsAnz8U5QIIw1BjIm89G8xm_9u3MnbuHkiBI3ypI7-oKswSKOmVJhwmXawXMqOu-8uBrwQqnv9_XCkB---K4KdvXHQvSJIF5WWPbpRG_Gj77E3atfdwRa5hC2KUbWpZNWn1A94vbbJRzkwyWpMXknyaycmm3ve5zhhxsVX5KeZ361g9KHfXXevpB8L3v4sCu4MgIxDKjLYvW-JoGMbEe_9osoJUejJAd3Qy6OT9NuWqkl0c92p_4WqOP8qeto1JKw3FPClYcnxyEaCx5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjmvyGhSbtxYNvyIHIeHqV7nIX45UzaqO4NZ2JTW19Ajx2gtIICgeTTwZYhD-jhunLCfWZB8KGIAHsRLZJWn9AOTo3TMoT-mttoBF1bzNFbiST2d9qs42ocav5Sdxu31MT4gjs7dlvBcquFO9jHrY-SnqZENImsBdv6P27nowHgCs9eBTkfHipkjtS0ywgM-tkXtVsLzrLvf-NnuzUBJJGlNrHpj5uIbL3DqoCwLncXf26gsITVp0Rrjqz-kCRLqyA-gsW2ZItIY9aofCp_au_gJy2dZTo3SO_CBlS0o8M2W22MWDMPrUg-_u6DnONRWycAqBhoL58GsS34dWoQxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bhlfgw4hznFXyK_2nJ4sFxL5qdRnDjcHc0fHxOFruPL9mLEiThcAhtVo34eNIGqhq65wjFms5TPEllbNERyT74QQTZ8V9Al7d--tzjGjdXPgWLxSESrg8dpeOXAMmgH25vq7EAyfldt0t0rK7jQIS13_4Rq2D_NCHfshQSf7GhIyhygWqWjC3X4xYKC-OXo_y75yzTh6H5H0VAL7Dj6Eely2hVKSs53RolK0mDegPcgL2jQfz3H3NMs_6n2-xCwKfHnNkNJ8EzCz55qC-PfmBcjK0B9unycDQo1NkK9ZFpUNhuAU9jcGVK7JnTNrvE2dI-96yKBjgwmPEP9L46QK8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgV-IOu96IV1V3CqINAW3NInUZjtGSzRlfU0JsWCHY9ZD5CiaKn4D78BEWRZ6nPHbiksqWSrF8tdhqDkxacFXAUT4AJLVb339gCHnxJPaz0Ax88EunbbC2QaXDpNhvVNeiu_Lmd_VQX-iM-iCTCihoLHFwcXjwaVr1CpBP7g7nD2NnSCfUmrytho4DdqtB6mCbbtFreMjl8RpA7ugiCGWPj50Oq8pglEpsdxiTp77HOg8MKeig7Fi336e9keKy3YJvgAzOulHSp5XCmsXsFY2imArofRfHNgQm-XHrtfUzf-FEH4laUKoNv8D4Pu9tID1LoB_zrQ6OwMrjf2EoQKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov3MwGUTW_APdxwrvwf-9gRwKnDK0UgZGdT2Mf6J5c36TQ6R8DkJ0Zmn-8VCjWK6gS8LW7_7xMSJdROKveX52TIYzL2OUfEPM-sXzSXXDMD1wGG8gDMnkxFWdpHYQ4FFnnoC8eR9Ku3uCsf7UHi90nd3GLxlpi8pcX9G2WIyu5zt8LLDwwXyLc6piPstHw4_uK2Webv5y9rIDmtEMRgk8zWiselBH9LpzW-B4I8zKZ7dhmBtNU49HOjmt_o05G1L-LlybXaPG-8V3-Si8YpL6B_iA5Swj3SqCXFmNX0Gj-tTMjvsgXiuTsIHtpXy9OL8jXVtb36qFtWYX83OOF_m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=VRvy7P7tNEW-72XwWHxBj3Sw5PT8WT-TD4x1ZcDUkHGDmDAS98_S-HD0zXzA4gnarrInRtrmKaqVQBV4KB9bZpXGuc2dbhI37nM6d8EfBR-YHweuuB5nomXu215ZgKrG4vj4ao7ySnBTwkhO9KSsdHF2NFrrm6vYt6VgMT3kRXh8ILA20z75Nb3vT7R0uHSaa3Kfkqh9xh5NYbuhcXq21bCOVLMygJlHUOnnz7LqD4pHR_j1PLXmaT48bge9vwa7_98GvI3LReCjy7kEwmJWTNuhgIgQ1sf8c4CNhdVnle4eKGuDw_FlGRSO_VlhUWTS3o8sRDhmqXNWgvrkPhIcOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=VRvy7P7tNEW-72XwWHxBj3Sw5PT8WT-TD4x1ZcDUkHGDmDAS98_S-HD0zXzA4gnarrInRtrmKaqVQBV4KB9bZpXGuc2dbhI37nM6d8EfBR-YHweuuB5nomXu215ZgKrG4vj4ao7ySnBTwkhO9KSsdHF2NFrrm6vYt6VgMT3kRXh8ILA20z75Nb3vT7R0uHSaa3Kfkqh9xh5NYbuhcXq21bCOVLMygJlHUOnnz7LqD4pHR_j1PLXmaT48bge9vwa7_98GvI3LReCjy7kEwmJWTNuhgIgQ1sf8c4CNhdVnle4eKGuDw_FlGRSO_VlhUWTS3o8sRDhmqXNWgvrkPhIcOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXn_idULDtCoRkyEQS2SthyateM8kZjDMwhwtmGe-AjJ3DIY-KIN3sUkvgocyvMRTrCw5iF_p8EAdqNUSbWFKh53h4UNyYLVahUb6zuNMzsSv_NO_mxjC-tr0m3NF20PAgC8Y3FI_Y5wB72FAv2J3Gp_77A3Sr4GkT9oDSo4xzEvHwFQ4NEWnDtmsI1q1ObSp5W-rCTsW-jHaaCOiZBPokTxF3MJm9WGQ_XqW8VSMvup8cunNniBF90paKRY5Jt83ZXTNcANCQmORX9vpCeWBxc9x7MUFvZeduYbgiY3zQPJErxOe8v6zwQ6uQMlFe7hwMSbhhVPuNDfayFkF77dNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMYFgkd9EOnsBgAXyCZZn4B7QG0LXOeQfTWgN9EyX8ZGAgVnGSY-5HFS5-ZJsxOdb1TIXINxU6wjd8uUKK7B94acWg5QJONDCUcJyjCC3VK7HMpbuiFG-6GRtNUKtWha7R8I57nWh7dTBzWjti3lBiDmE0TJ2JHTBr4uyGeaqXAQQeFfpXLYYjhq3-9qO5u2x0XmRCGIwRfRBYrsjX42a60ABEDla-Q5lWj7e-gxFjRPe4BMOk9-wLFHovrrFmqyDr-L9-RWwlPVgGHlFv5mL4NSlV89dywTcEa2j6I4Ipu1YlARW7az7XAUJ5pw4XOy_7EBxLIuV7rmDUGpzhZ8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ13tRt4Zcw69aQ3mO5iV1daNNPe82FvVoKHp9KNW5BGpJDr7vxHUkCC33zR1CE-KEpbpNtmwGWMbINitteWkXesk5aw7sVhmpLufBYVhSaYHJQIXRYl9b6nBCVSAt2zFvzlLQfIQrkKR7KL9PpZpEVByEt4u8obgMW8ercn4tt6NFUyOVBAr8JKwAXMRH9X1lYapTq7CfPd-Fl3EU_22CCbodTCu7GLCNRD3knzrr5NA0OyR_yerH7PLHZO8tT2hY_2Cf_El14XDlIB_QAkbF1XsGOJMloGADKQVXVtwaRDu76rGBJ3T1ZkKV29t_WJZsoRG0ESOIldmq5CtyunXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REiorfb0wU0AZF412WwtkmF8QycAj7Sg90UJl-J1vm-4ZYJQoAAhW7MqL_QPVdPOMguz6QbK6ZLSwjbKvbCbFODVUwxxofdxm5WxiGLVAaPm-CmN4heC_bEgmcMXET8IY3Pv4niNvZp3zwRHPbkhBoGroeKTf6zaAfeu5aGNn8rG_Z3ADE041KOdLlbTp7RMefgIUVidRvCxT1O3tL6uySkRVDsvdAeURTQ7OsYHE63l4N-x-NXfRelThPurEsPM1ZFqMpkB9JTZ23EL80lQBzw2l-qDv6bU34j4rRTZJolChKk1clq8WMwcnafCHdWx0nwyYsCpBrO8G0GWs7N3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP0Sx6DySsopmyUWN6HfPdtbu6KK5B6UOsxztRMeQ1p_hxuqDtzcfkaCVVZQO4-Esya8t_dkSzKH6niEmiPwQWwlZKHekzGmMpaW25HS3pJ-jDAAbjNm_zuPMUkGmMNfllnEJ7oTwvJZJI3jn7XaCHKENCds5yLDTfNKOElW9GcVfF1e_uJSPBbrD7Wx92r99Z4EWuP2rynn5PuO_dFREavMBO4c1ZoxTJu_q5hj4XVBdkf7g9UItJAwiazJL6gQONKA9XtiVejxmcJVmdagjyheFnuMGQGyzXIHKA3f1CXcCq9zB4XtpGvYV-CDl1tuZtM73LPyTxZU6ZxCuG_FdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agScLELUeBcDGfkkwnmN8F4mkau6Y8YqX6-jpmK0r9lf7kG9Y5zMTcfgGyNBkzYsMtXCkaqLWhDyBa7FNiXTaqGR1l82kx46zringCAO6WoJzB5d-8LPJ8lgxyihic_zXquMPvMSHf-gvRqPCP7ONQ7WsW_NRDWK3S4OWHnXPDQCPfcdv5AC2Os-dRtuqYZhZIBYXtcF5wH6G8ZhlQJnVKkYdGVTXSQeYOOPSYSCVMxMSzYFL8VnPH5uSfwzDd8MyHmYD4g5M1O2ebYMyRlo2IZR0jjxpCrlALtXcKBfAmhh2fvzkXIOlqf5ndmAmOBKieoxoZ5cGIxnCNd5NR69gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYmPQoPP8EUWKElPuaIlJWj9obLP-7oql3vQifGGAhVLOYiWCTHOm4PMfBofL2LrXFTTKupdawUde25Pxi3KE2o-pvB-OL29QyCP4D2kCHVJS7sDZ4O3pF5aG7vYDRWCPrmz3U4m4E9xRj5CzPK5O-WiS5-7N1_g1indnLWSG7f3KPLc3esmHy9Zk-9skW9ogQVRE3iSxOxTpDYo4RAZFR2gy64_XjfO9psXbqA53hZEcF7w3DVXcR-6tbOLn9xeFrYCcY5t15PSn5NHggGgKKYLze6Pjm_X_VWuuraEWHdSdnpXyCVFi4WknFlxFQly56WGMJwoUGIqytNv3lRm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDHwD6ySipQazZXbTFkjPZpyRj3vrqLm7g_L4OiO_ZTdornJnu1cKiTFO8NBd3AOV6odjL9hbCmefETDXFAe5k6IpyntCVkM3tMHOjOTvmFIu0CJgtkMYmF1eqkN0zFP_BbrFwhwXC-OAMjS1g7inFmR0_DEM-yUQJ9LJG5R_Quqi-E4TRP4YSk8NxQaBGdSTXAynuiy8IQSavx2L7xe8dw6GhCiCw_KVxufDyh_v1zLUlZxTGaSJDmOD1WajeWTk4JwA5gtrxVWB0oV0xMzhSXEqp6wwwXbsyrIaWvxRdyCKfwCf5XU_a0B9S-PJpFk6YsFAx0DoStOjg4KrMCPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwTVkXyBTwDo_J-eqMKkbdpzqt6JapUqkePr76WbcAWm1UUy2foB4ugDAB8CJbTaNfrZAgQz0tXHfs3KNNaZY1jYP-Is0WO_ek_XOVpuB5_VMp07X8_xvgHuzB04ovRr0iNW0y23gw_R9TAdvUxepnDCTbRqibed_ZCy-PD-IoHSeJl-tTDJaw-7l6aQOR5dBRODOw5GJar8EJEOPHlGf7loC9DVufmSLqaAvJv9LTsu8YkPFHheGbVyScqlS8Jajay1caS6XbnfVx7y3hyYJuI5sUlI6CiKIbOghtLVIalLZDwUnKdaB_qRi3JOOPIdHvYq9mzbKzryUKSrTEPMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMAqjR_FvK8mogZIO-n-oRpqe8GZo6CXdRf3XfA_d6s6oG2kbHmfN_fE1uq3dQYa_huB5I-nXgtPU6a_Mym4elBzjnbcFwq9f4p0-3iTjWddQs2HxMymRA00X8hV36YLk1aIL4w9A6AX7307x78-kRGaGx2ONM5xGBRKVC20Byc4GDCLznk8Bt38MftxxTZl7xCiBRVwCmvrwXrk6o4ptRrPp756-Zx2CGBXiW-p6WS5TrSp3FcCHiqb_AElxDIqsSMXp7ZElOOJ6pfuWPi-R7uyI9Vw3Vtwa7FzmbR2Hxurhp-LfCs9fAbkLe9KsecItL02d3B75ER6-l0aS5ygPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBAtMLmfkFpmPI3-GXohL9byNJqNJCo4rbrpV-U93BT4SjQidQga_o8pJTE88F23IRP8NULFV9-JCiXjPtiFn19JTuymW32IyF4nHvE2MJiXztTF3NlALcHCnPYDBkZeUBCadYiXa-PUF0fg_GdfjurNczNx2b0oSiIg5vU_nAq33hm9rpMPlppSj9L74E4Xk9z0qA5kShAIyfQUuHS6hsDOQE5DUogZvLMN-zqqcQkQP29IbTRKZ37rQc-1QDNyrzsch-guAVuKV-sJqGKfAVQX9ZLU4rDkqwJyMLRxmqARwwo3z9rrUvnBHWyyERxgsWcN3r96hA_Budwz_qNJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Je-leNDpP8JYwYTqXmshVLmkcTj-KbecS6DMD7mW4UiGmWQe0DoAgK8NqTL6uPYLasPnneg-M1IrDdUinFIjdcwYz6sVuwKz3NNqytu6uekYniLXyIVCA6LSHirvQWSIWqTB_ZlsleBWWds3fGC63g_PHRdjtSEo3BNFpmv85w4MBP3lgSrpyvMjUGnRQRMc08Qtq-tNLMILafxS7pAyArjP18d2LEvuSSKOZYWE2eMTUdtDgphiYps3oquHZcMu7XtFPqpnwj2KxyX6uuQlTu0f_f0yw3PMaUjNS3gVgKHPraA3-P5hGW7kCQdCUkbYNRrCeVk-usnUqNAmVVaNRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl2CJ7-afUKEdAcO95YZUm56Zs1qQKo15DlFku5PYG2E02WkKKPK7LbGXYWkFl6I6vqVz4gMnuv51_i3Jv0Y_l1OWf1VOGN5l6d5p0F6wRVYH9_hrFTTqphy_VvWATU3BFxUVCaevlXuMfhwqMr_OWIol2qrAOrFov-ef7UuGbj8oCvaN308U6dq3xR2TqVbOg9FOdCeCR8Nxakz8uVkNGbaM1UQloxdQ2GfnfWjB4f7ZEZVduYr_uLGkHndC-OC81-v8FXqaiwRZ61azZZk8H1v24bqAVMWBo2kiJiK475BhC_wgvnIDQ5NAYVymKOQPPWtg4MXEMVxGLYVr-VsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOS46OrWeEMcDvSSUegQXoxWWitxVTvvYTR_9mkEEO1H5s7getgwtGZp-v8uJAiKbTWAgIrb0UQ7T7upaE5UWcslYufgFu21jn8QMZltI1xJjeYy176v7Nyd4c8ez91ZNZHQYqBaMkWVhjWSjBlrr-qoUb2ritAn8qyKmam1TIfYxi5Fpd6bgbsKHA2ohuYdi3FQ6q-cBeT3BTB_mYrTTHdGmy3H5Ft6TZWwA80oC5qNYGB7iQnynMLHoCy-8UCO4dw15QR6bog91juhHDVas016YYMe6kORtW5-0fVEDWTIRXRGM8NULi_dU3wLrq9N6wJbov9YwIqKtvHwQG3koQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_yLAFQ9jTMRRZe5j73fYnig4uzDKWH4jaSiWoZwiFtJVRid2e48LfIhqWpmVLhMjFxQUgyv544FeQF-HMPV5ZGCMs9NgdD_nPcVI02bLgeQHBGxhWT5kzeMUMEcQm9On6ywttxpOHpiTLcDg3rnQatxaAGOGF0XDQw8FPM8LMndiecaeKc6WpzErU_5x9UVDptd2yrq09iKBIFKWOxUSBt_BmkOUaJpwPBWKnAwhh-Q52BtwMDBmnhRfxIp_EDlxdezEUYrrzKOsCjHpQsbUlBGW4Zk8QvdrjdNDfbuzjG2jzuWaiJjFvJPvpftFj1Ddazr6eEhmaAxAfAJ_OryKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYuL8SP_W9vt-cTN_dsx3EGgBQWabB7iGIsUtKUaGNFWvE-A0TmKJ8dzi3A1UeKXKgp7Lk_eXuz5FEOKdao1CsB_Cb6s7J5R_GXaXO6jiynvHfL8g1Y8rIzbSvUA8aEFdNSdcErxEBCEvTQtQbDe8NrQI5nFrWWl-jjvBIVlYCDQXy3mUxGjqFVm1THWQyR9rrPKV3ejTcOX7IbT8hv2PYsVQHEoaIAxnDH-ZsHpXiLT7SR1MJ0FT-8G2OCo0gfu9EHsTSn4xolcUZocTH0-jeuAMiO7wMjgrzYB887LzmkYCc1s5zcPEmIm0UuVkWXqy69IcvoeZ1aMqQxkOCYrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1IdLWJkyfDpM-6KRkZk6zS4IDU2fPo1u7cB4FmbMf7J2pa_3DE4WGqO6LBuaz5j32hz1yxMNo04qH_MXWYQ8W1tfmbWrf-dV5QKj-v4GLBypOiF3-3pUtosJCPfy-4WVbY2PSuU3oz73z7jvTuTTuUL7ujhiwd-ZGp5bEwfglsNcpvbzMRCeu_0s0vzlMbRaJG8Q98ghIe_VTVkSrukIH5nTQzD4Gqx1J8cSCXjlb7PfkdHzavTraK0LgpTAdQz3oe0896J0tk9zICyaTd43vVCrEQPXc5DcC6AdZcz-3mv_v5sEAd5xh65jb-IbjPIFoUcy6auAVukKhTLduMSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcIBxFb9gHiQ64cdz-eEF-1i_hokUCqlZ7uI92ArYVq1u-MczKDevNOYvGARbSTgkLJ1mHCFVEZ9u3LA7-1ATaJR-Q-ble-J83i_x_LI095yxR04lusV1XdGf79WGD46RbJvaMnUNcnSj8XsSpOcZKyslyrpMSl8dBuTpGsHR0QbtrPhUzjs3rP3syuu1qY44DK0FGzZy-cNQuaBfx8TYEpddxBiLHy-2jzjkKWzSoXjE2jub6RD4-Sd3AuEOUvm28Gdv5WlKQZqtpLiWKg_8-pf1AKa2x0sijbySU1RQczv20V5wUpaKSGPjIW7Nx8kSg9swiKuJsxbe36Voz3RnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8Dzgfu7_sYAxOxTN9vcfF-lat6BOKmH-YvoMjIOZqGRmDVrYDpIJU6peNbo9fwDDRHgygnRkgwwuitkpvlaq7EASM8S7iPcvdfh3EC5Pa2F5gajgfGh7k02JP0yB0Hqx9FZnUmJsWlaZ56Ttynr4lyG4tVV3GI0JKrDUbrOOSa8Dn8AojpgWKQu4_p48FImAC1vezBLqnlcsToS0tBIApnWsTdAm4tQJPdUEMmqHenkdzIDOCue542xampXeUUYlonICa7YLh9O4izt2m-X5JlAi2qnIcWNevZRBS2AUWjHSlkZSAw3ym8Ma_dSOBr7-WpP5fOAprvl040Eg7Ld6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idI1fViXmF5MkIRJp5T7bbODwaNKq0vQSpPF4FVYN4ETTIHeRzLPFVi7Ep9eA0H_GUQKxw9yERewB_DGF6v49Zi7KppL4oV0AU1qnIiRIaBzytZzG4kde7mRF6MZLTOaIEP9c3c1_SOg7qCcGK4DFLrYfhA0TAp7QuRLi1JBO7A8SoFYv5UXrPYM7YhaApRMII9_dxEnAaYIt3rc1x9H5fRqYYgV0zKHxJSapeOzyR2UkqIOpa7EyXAVwsKZNQZgRy48f8QBN693W6oxxQBSjKg3vatkp-jk3bsbl41bsjLjH345mwealJAhTK5p5WOSymKYn193Wvya_s2fEHl16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Njvqx1jVkYXNJqPgs-6wTuPOVOePnD_YSz2b3bFRUUwWxYHdWNt8hz_xWgYs-niruCr1KEz4zhsSnBs0ox6qOKxHyFfZ-5g88gUyILd6pdNG9sn8XijpgWGM5bKQmS7RrHo9ht_9YkSyuMeBfb6p2j0065cScGNrwzUZzVM_2C5uJSd-XqKFXoJTROGzcRNaqq30e0BW5OgGYPWIW8A7R590d4QVqStw8dk_aaS_WqC8FRDa34tTZHt5BiGHyZLPyxrd78VejsExqoNX5HUgRMD6nR-SkDFhtJ95Gsa4OigNOEvRTfTGZaj-ArpUCSExIE0EhurcXYnDVO9dJWRdsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdGVVICsuwpK-InJvQ_6DiKTo1G2_wXZ-OwLRVxNL0958Gnu7xbqCvXo7rVhp7_d9Z68nDZk8lAu1DexhvfJTkmthoGYNWTJTjOtP7z6aLb86EEq6jgwE3I5JkLPviTfgfu7S0l0G9HaCSNC0btWJcgaVuUJHh49HEB3Zxwgal0QQodTvowLGvxr110jv55MElW5DzMlJMTIlsfDUWXQYWkmVUOmzlCNYEPjlMgS1WnDdBrWeRLY-hK1aYnbmkainVYI6zKMsDE1zEQJ6AklZl9_hTOXXF8KC8quAo-QxmvJ-mkZtK-dMz3o8VHeUeYok3DzEk_stima1bu8CDPgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOFq39dOmW6AQ5D4xjD2E2x7thBH51b1lX3baTvp1E0Ho3fFiHXTO6gJSQgKO16ONRMHuccKI2L3ZxFR8MNFvd7zcVYlRTD6l64rmx0vC2I9vPoo7EA4XRXU-g9tC3S4OyfWn_wx1GbQZ5fW9lel1gGFkMKAnq6dJp0djXHlz9zKPOSws6PKEx7fNx2TlzvJtvozPxXpdXqrLEmT-zMNQFSMBqC1rviXrPmeOnHegMislKHH4XA7UWZahZYNbIWsCdEmVkvPGxCpRRpOPrFWuTwCYDtmDpW74dWbPlSf7idRDwcEWz7DA8jctWmXGylKn3yf7ueuDZSCsxNOzsu0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=DhxdjbI4o80jNaUksLXMPr3SXwagR3mylLbqfVieXDwoDCDG-KgvXoBhC2jltjeMOMljLGeKoCHiELCT3EKZ85ZC81Aiezswh6FMw1NLDGB064swr-qtnmnwaA4kkGAxeVuHyJDcxq-yKCBkB4uipNGBLGEjjKHBCLSc5s8oXukkSCgQsFrrFr9XzrPiYYT0GgYBHvv5LoJjrA6mn1uAurciV-BzkE26-LP6FK0pjFnkc4NDQjvSe6bo0QOSO7IKImTLa9VTunbsbKpGJ9-dGQIJ2bazGsXNmL-umvBJcZ0ZI0x4gShB6CJZgdaFd60ktRkSLDt-RjpNDQBgjvsEDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=DhxdjbI4o80jNaUksLXMPr3SXwagR3mylLbqfVieXDwoDCDG-KgvXoBhC2jltjeMOMljLGeKoCHiELCT3EKZ85ZC81Aiezswh6FMw1NLDGB064swr-qtnmnwaA4kkGAxeVuHyJDcxq-yKCBkB4uipNGBLGEjjKHBCLSc5s8oXukkSCgQsFrrFr9XzrPiYYT0GgYBHvv5LoJjrA6mn1uAurciV-BzkE26-LP6FK0pjFnkc4NDQjvSe6bo0QOSO7IKImTLa9VTunbsbKpGJ9-dGQIJ2bazGsXNmL-umvBJcZ0ZI0x4gShB6CJZgdaFd60ktRkSLDt-RjpNDQBgjvsEDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxC3-lWuKw2bnC2iL46Zj7UJqJE7VQ7qkucIsqoGEgxv3VURYuk0ct_NRauzeTSFFVhDGLtpxI0RVaCH5PHqYFOumv0G2wH1LuFJhaxh2qyjrsibb_GefGjJL6SyAxEyGLS0miw2BxHDRn4Nm2TbeKexz2nAUcYo5nLcowEWHop3aiRwenEcUACMaWg_irtqATeAQsg3ASPI-67eOzOukcWpHqPLJIo9gGRtCVN4nhap_g5UcE-AyhnAOVWlzOnRHWp_pPplGZ_gN7X0lbybvXSxgubAzltq8kDprVvSHzQcZinVum_aWvsXXFeoXgi8a7gbPykpt2ZY2E_pC7Vc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor1ln0FYpQa9joPOGrWLmtrN8avoeu6_wGeeRgcPrDM8agoC32eTTc-pXgM8Tty1k3lRDOdzndagqrVmLo29GsOqmL_HgrZhy3IXdj1QwDNDOfOZEksxcGlMQK4zvz-UilKQiqoDl5f5-0Fr1pU1i0Q9Sg4FUrefJZPY-jMFHSY97U1brCJdyNNWwsf_zC3eCWm6u8fv-ZhXfJIhpK03VqLDYCEiUnn3g5dLRUxaeGEEz_Otv2z66RW9YkcHdnYXAeZD8DeYMfjJez6HaPBxHt61ZD_c7A8g1MjHysIWtXBM9bMB7uQa7O59rp5lTOrQ3iZ77STaHi6yjlUenGJZsPCE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor1ln0FYpQa9joPOGrWLmtrN8avoeu6_wGeeRgcPrDM8agoC32eTTc-pXgM8Tty1k3lRDOdzndagqrVmLo29GsOqmL_HgrZhy3IXdj1QwDNDOfOZEksxcGlMQK4zvz-UilKQiqoDl5f5-0Fr1pU1i0Q9Sg4FUrefJZPY-jMFHSY97U1brCJdyNNWwsf_zC3eCWm6u8fv-ZhXfJIhpK03VqLDYCEiUnn3g5dLRUxaeGEEz_Otv2z66RW9YkcHdnYXAeZD8DeYMfjJez6HaPBxHt61ZD_c7A8g1MjHysIWtXBM9bMB7uQa7O59rp5lTOrQ3iZ77STaHi6yjlUenGJZsPCE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h67Gz6p0bD14eGixBp20SCWNa_mkVHcqQIqMBfKXiC5B2iuE5_nm-EcU0I0e28peUUXGbnlJQqjlylM8xq0PJWt-fkuGpIV4Lli5n5ehxF0lcTCb4ibES4_FVcTYNjvxgjemWE7lxLjuEtiS0vBYAg9kgMkyfsKFeLnz3yIlyH554kTpUefVqV2_7MUBNgAGrOpqobsdx9tKixSBR4pWnccg3mJB2Cq5H_9_Wo8HfLjygv2v8956abVe9eggzt7MK9sn5FI59b9mCijmWnH8qomwMqsjBOlLHSKWxt-4G5rAjD9CEe9mjenbF1lHqQXiliN09NP6e7GQ7w-029eVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9HxKcGOBk0ePWYOFV8lpy1IwmS60XQm_g1M3thc1n1rXhEnC-L_bCc27ep7lTuHsr6fZeD4UXgOMMxsvvZosY6IODd5lHkrJOxfsUDKzx8uN1omS668iup0_h1ZL71hrLx-1FOZzyCzKfDmA1d5Ik2X5vIkVfF95I_GnV6QD84E_M4woMIRztkLGyUSbQ0U5vz7TNXGrwGOmEsosOim-Ykju7UrHm6ScaMbT2eIkZn83MigGSio09z9EhmJMGyYKLaKhmQJfuBbSdiXs5dBV2AmEyCZlDG_H0XpjwKV76yFjOwF9rQ_XjgpBwYllyJgPAN0ZjO4BspvPrtQ5cX33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP-z5cvLiiOjeb7XA1VaQekqddLYGJjualChwocO5gynpThkrIR67wWDRB1ZdIfXP9YVj47RpF6MaZy4RrRY4co3zGUJf-V4H1_eWbUSIUamAF98dfZhADiB0YB9U3HOSZmIG_WCLgggL6RjO5RYpIzPPAYSGWylzkUe6y60oNWELUHUA56iTQnJ7GlGZFQZffHeTnaTWNXPvFFGUDtLctetVDMmnilp1cT-EA9gAtPSDnYZTJMc5YwAqyGVZhiCexA_6q2dqehvD4Sjsw7IZ6TMAEHygLRwXkoMuwyucTmPNWluRY4eFbjzb6CIJo_ouE21T3sPX5_Ebx7VNKDxFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgjX7GTvB7e84vesoInoRRHBbVTKDmyAnrAtYiPxYLWU53ld8I0JQMYcI-b_3JMgN8cWeZ4KmtuQ78IfEje34UJjFtteGL3MPblmWb1nk3gqstqy2ECxP8YW1amN8VSwFRI66L1K389ILWp6NLSBL868h5uiaauTMCcAkTK22xbBlXftCogCYYaYBovC6pmm7sqfyatO4q4t4RSSzRYVyzsXQ9tjep8qaLnGuSQ7xj1vFjLRDiWANfhqChhBh4uFEnk_Gcqizd9OgCgfcrytzRJU010gnltcJ2u-I4xu43uuEZ6gziUs7p0lAd7j0vodS6CANtk5-bnDcWQ-4TmP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI7dRPEc71ywjUHa1HQEFcflERFchQoWxj078TMPsRaWDdYSZRvDWFxyMuoTm4r3oBDiPUN0FaVaSXhxL0TstIWcmeJ_DVAZ1KTK561TPCcwwWRlQqTbZy4M3P3g2G45Hkwk2u2NvDqnO4P5VsCyzHswvFKBcQJIzyNiBH93I1_QtchD6nJnJbCXK6c5mhS5NPaB765__NTy9qRYXzvceomYRd-jiaZlvxdB49JnKLHGZZjc6HEy7VON6s4K0C4Ln5ofM1SvDASiwk144ALnq5sJlL1d3BMscK_LOIMWbljWK1_bOx08ZnspEbGjyVoOXs723DW2P9cRY_OZpbK_tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYsYQEj-8FDZBNcMsFYqfVi9qE39ywJp8vY542ZuJDjnsY1x2k114kPL4hXDaHGa7ipsahhxdUo5GL2RfrlQAwYAE5qPZAETJwnprgau9UNXH7Ucwr8EK1rvjqIVop40e_PdHsM73p5QZCoCuJz3EQQoowZQWL79s9OrMpPwIKjiPXwz5RHvbBc79LorGYcWAY1_QzOHYmRQMZtziq4XPX4cTwOgUFcuqGjVBvqK3NUno-o438hdXlucsCLbznIwAex59BZeTd4C6kLpgovZFTyIz1DTDRoLrgo7VVuIaHzK7spz4Y6mopnLXZGSoLtb-d7GAsNMGKs1OrifyI2IEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACu4SxgmuWQkrQEL1Et-WdHJ2IAox2XPL0hy-KkP8oQkGRUMToHMl_F-0yfe_ywlk7AuEHEP8MyrBywBnEN9TLDfp2JNF-Ypj289u2LQN5atP30tX3kTcCtBUYQNoQUbJlvQ16yxXZPDpRyGoq71pGdCfCz6sOjqhHHt4ehK1I4m1wYu0rt5pasxv2mjpjVt7w-WuiR5xhl8f2m69E8Q8RPhP0k9Z1o2RkL0wwMAOMSwFIOcRFKbvyFxVMNq7uMjgS7Fzj1GMpsoMANvH_hVzRXIPiEpLdOIa-IvyMilJlEyjZEWdw-jvL9z1kjo8y_93d5TxwCMaIbYlQNhhhmMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvpUqp2g8JJV_1M4LkEKxcUuoCAnkPYslCgkQVy2mXp3R9eRJ-mPh4WA3t_ZIrkCSH3thPYlXdJeZBpMXf_170Uwj_x2Fm-Z4mMh9wYk2M5BgZuQiwPPXs3xUy6rzDbNNimZpRoF7nzcDrTVGF_YWvOVQ6ljHNb5Z6blqiCLeJ_TuODO4S7IiFm4q4kq6ap_qd-p-2DFdmN273VL0O6rCT762eetMyZnodT1N-j4wJVgD8MvdnCWvbOdLFQ66HPwpUuP1COoZ69j-ifaGc5G-XvBDVDMkzT2lCqIq9nkRS3KVyMy63CD_AxTmOvJSNRpXd899raRxIYDmSVfEtmRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTXDGphGARLWLw9QVIT3HUJBwHFHn6vARErB5ZDbLtVGjaiRUH8F0ChmahCl1sZaylM_3j2jvBqQaIskE6tnKMzStAP6zTFQXzrBQVjxY4Z15STcIQazVyQc0Ix4ReH3zKMo3oLV58Q9_921ZkKFWV4Cb2YAw-4cRUJ6NSGMJNKQ5dgLcINzh-1xBe5H2tCDqBeeiH20mjHizmmike7awdkQ8h3sF2CsGbtupYcGRttA8GK1Fuz-8LFSODPxViXbhVxqfrdJXU-pGDiSurshquayQw6qrvHT5XKmyqx96oiDGh3gnkGbj8UQv5QO8FW8ygTwFwI6Ra3iT5M9pWUvmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHOB6fM63QYgRCbJBI-a2mYVC2CKYbML8sx5hLGwQXEnB4AnKxA25tbcGOEza7FkAFT-83_jMIc0jIK6jcLukLf6Bi_Zl7UI-5qS4yTTG-45oWxjpeUTL9VAa0puYBD-Ra4gTKXSA_VQMNkEMJYgX6r9eLLlMWKv0S5C5maPsdtJFDNSbbJFd-t5ly2GTcyWzsiU2OuJNMCG2C3s0ctNdeYNLRRTlBJTMZaiXmgSOPqFMfK-cd4gdxwcSmJIzNZMLEsWxjp2bZ5ge41y5VfMREG1kTkhRRUiK6fSijCG8NyCtPRT0i1x0vcXk52rdbj0wVsDH8eewtydcTtf2pm-4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-Mq-_eoayLdpB_nd1TrhtIdLsm78TT4vtsvM4DMVIFkWESK1eSwdOZF-2_53vOPtLt0owXUOmxejdSgtkn5a--xivU03QHcj6LjnunKKPqhunO1h-tvryb82z5i4DXcF1_YrcTwBLc_ZSQ73dgmKwBOU4RF0mjDN5bqDcQt2Rk7xRoK-4yDJEa_2BPGXK1Bub65CPvIjVCs0wtq8rQ1O9sX7dI7A3VHyrjRbaDwus9-4RIDO1ykvBj9fzjueOaWJPciIG0bFSGuwmqaN3z1mOize-u89k41d9rkS4w3np3QeQS6gAMEcAMFJpN9NwEsRlhKE5ohicRjsW8EIkmdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=OA81LUXmC_Woq9ZDuQZ7gQQqN7fYvM_vTCBSlNUWulzr796VbPbu4VGuCFz9cNKbJSKVE2Xgmav-Bz7R-FThMMXLAyCMbRQeEM1iqpF_2iX8I1HSPJnS3KzF7W2_zIAV_qJXASeyjq4YBBB-_BQ9Agb3sKZIN6_3VFvhzmZGlw9fYmRBxZghycO5t_xaX6AJs9IZzEVX72d2l631hOAMeSvxJKCXJ3TuinB1YsZW92ok4lfXoTeiMwypp-Xwat844g7sgljpsyzCYXlGXmmT-UL1nMxt9RnOkAS2-i2K2ENCSmVn0vFBypdblsEpbxtgNBKDpcM7DppTL67As15jgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=OA81LUXmC_Woq9ZDuQZ7gQQqN7fYvM_vTCBSlNUWulzr796VbPbu4VGuCFz9cNKbJSKVE2Xgmav-Bz7R-FThMMXLAyCMbRQeEM1iqpF_2iX8I1HSPJnS3KzF7W2_zIAV_qJXASeyjq4YBBB-_BQ9Agb3sKZIN6_3VFvhzmZGlw9fYmRBxZghycO5t_xaX6AJs9IZzEVX72d2l631hOAMeSvxJKCXJ3TuinB1YsZW92ok4lfXoTeiMwypp-Xwat844g7sgljpsyzCYXlGXmmT-UL1nMxt9RnOkAS2-i2K2ENCSmVn0vFBypdblsEpbxtgNBKDpcM7DppTL67As15jgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBURjjLb2BQ2T2FArH-trdQC97Voupk38IhZmr8stFNYZswC7bmFhtAIdQlNcAL9huu6hcpyYazp90BMB0aIuVyTlROiXqIVxaqxlDeAu2V5Rvy3fMk3cxwlwG7eI0eO_AeDzePcvt6JbgqHVHR6C0nsaqtfxSNghGPW7EpfGFPNOV-18bEHFD9_8Voq82ocG0VqiGJVXQmna3ZvoB9gbcZ74kfuHXjFy9GhRXnWPuHsH8PsCq3Yb14a5f-l1r9UUsw2ldBnCVuPl-Wi543jL153SH40FddbpkW2uDxffP6qEQt9B41ZVa7wI1iiqD3v7zzVjZqekIlAV9BYZB7p8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiYnUSbqtaQQ8frV5orbI7wwiyDhrk65OI1nhTveGt_2oY0e35-RO6EzuGZ1iIQRqVx6HsbknLj6Bu3vSx3bE-UiFdVFFsDoWiqwvkmoOW63gvKrOjm3BgzDXwacvD60LnJcNtrIMmeoX7Klfc3uz74lyG8tRQilM7t_2yDYLEnVCp9AujSPjEZEq165sr1gCRW9QLOfhNnY7jtPZ6IDftr47ElqwsVVw1mu5N8ItvNl0nDTXgk72vt5nIy5j2bvUkNj_KTUK8z2S30hE8E_wDVaL7G0iJD4_GxfhnxCeEO7T9feVDL_n02jA5OyTvgNUE2c7wS9eawvb_uhcNaZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqQrEm_eRDH2EjhG18MkbRTwnHyX17Ve3dwUmjaW2CPc92K5fUYrXk2IoJDIuROIwsrdr5LvihgpRWveoknEyyS4iERepKzZAYimwQLOpidDJfPr2Q64Tj1T4kPL24PNvUT4IvlIdqym_o1i4PM1OdeGdcR4n8XyG-N4O4YXTf-BEX2K3MTlK017nRgQ8k8xb7K0ZY7UxnZthj2vvqtGUl7Kt2b3aX3vpUp41fYPl2JbEvgWM6SLJzQv_Ws2Gax7AFWrOemmeaagtQAM6eXAj9_TP6oeD0FO1PZp3Qkrwpr2uK5Vz5JmCZ2983qAmZplt8keUHgOOR8BqyyBnOKYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmL863U7Go2t-W0lRnyXfLgHIUzHYzgvYvD7bkExne9JBAsgfcXAIkOvBygyXCK_00Tr_y6Sxw1vAfv3A2KfYPuln-ADDYzoTdUhRd6JfWKR7M7FTwS-BGZrQm31Tcu-DIPtZpRZYNMS7ek4HF-ABpHFo28kfsjMmvLJ7cQqH1bP0mI5TWJAA2K3fZ5VEYjWZ2-ak2m1D5S6g-zk4CfIZePztedm8iOIkkG4dFbTyzgPtYzpL-73C_gZhBx9xbnCPEhDT5ESngZvH86Qy7duOZ7XpYmxM0D4IuruGIJGUYdpPClx7wj-4VKRe3c6mJon7R72jvqQk6SwCrlHlpg6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyFv-ZaDLCnsCEanGlofzVNqmqrnLm1uVCmcYHt13x80qtW9S1Vh_AvQspop2z2SBB_9GIqFzaNQIVvhor-SfUP5iHJuLgsFeOoSzLrr23QO3Kdbk-pn2_2CIur-pys08mdmRgle4DE3b5khQUjONxlHzjqdy84zFCI6ZutUmvPjrF1nsVTs6J7u-FWhJWwdpAjZgspD3rOxaodlUKDSmdOte_fdBotYZrMd0P5CRPGn3sA1D2F5yT_dzAHePqBySk0p7xTUlZHxzQbzRU91brTiNTVWt3he7lwFx9iBFwW9UpPfyUg2rLes3b2tqYKmply0QjrHqTJnYRv5zjW4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfhzVv8TZYYA9hdN0SZqI_hKOudGcCmL2KlRmIA66asZ4wVga3h3m4BT0TG_6at5aL4GjsSA6ptrWVi08XB02CCVa__yo5h2lNf4kDV1EMX0UAsrLEs_aGq1VdENrbGbN6T7F9DjQJNpRe3eGGRnWxxWnR_POdBPgmnsEFCwyIYhGuPj6j7XANHZmNQEwzbMqD9syCHZ3YhXnDtocZI6OidL4uGb2Fp5xMIWuR7vVpAXMky9-uClIaKjhAQqtelgHElihZTvWBesx_PMnDhanxFaWosyezL5p6uN5JVKD1KZr7DaklQwMYlZXekTi2zNlTdm-0JXo2hmP8ICiBzUIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f613FKkT7kXkdB3Gf97mUN-hCgDWp5upN3sH_Qc4LVENbKaMzYp6GLbIjPvhhZ9wzJ8vWaRtoV-pyzUyNt7q6wMroI2kP3eZUE14531rCSJO-4g0ocSiBIQx6qpRgSXHqO2JrXOlCFUsi92pYEHoqCZFZeB3kXiEX6744FLz49wqOayCbfsiAW5kvB9t3js1VM6jJ2x8VjXITzj5MPtygQfZjo4SV8JTaef4JMOWEsnt-G0g5zr8lepvmu6ez9-m5Fz-HgXo62qk-1D40EC6Ov2c5zEq0R4XTIZGxGN9oUbv96KWGcuQ0Ztzlu31DzYVQpWuxG-Vbidt3JzF5wJMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=p8J5UpBjLIr6SHUKdy3ui9G8lu5yP0k09kpSqd4VBV6uZutIvuereqVpi5nxQe3Bqs5Bt3kJD4JspQOFlN5LD37Ls3tTHFtR20gHdCHbcxQVv4gAe4lAjrsoPaZbBnlVqdP1Rx-25M7Icd0kjvdL-rUXlBOmuAjuhYuZIwgeZzVsmUt_XxjsfHHrL8Jx3DcoqdiEPDb5w1KcAqWfh2-gqRfoa6d7tSjG7ztKBH-M-kp_57djMs9842Li_oOT4kbPQWbFBdAZgGzjM_0ufu6NVIXXcbCoDBKGQyfhSEESLBR69BYDUpFkmFvRVC4eCtZVD1GTi4UkE0Sf3nghS13U6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=p8J5UpBjLIr6SHUKdy3ui9G8lu5yP0k09kpSqd4VBV6uZutIvuereqVpi5nxQe3Bqs5Bt3kJD4JspQOFlN5LD37Ls3tTHFtR20gHdCHbcxQVv4gAe4lAjrsoPaZbBnlVqdP1Rx-25M7Icd0kjvdL-rUXlBOmuAjuhYuZIwgeZzVsmUt_XxjsfHHrL8Jx3DcoqdiEPDb5w1KcAqWfh2-gqRfoa6d7tSjG7ztKBH-M-kp_57djMs9842Li_oOT4kbPQWbFBdAZgGzjM_0ufu6NVIXXcbCoDBKGQyfhSEESLBR69BYDUpFkmFvRVC4eCtZVD1GTi4UkE0Sf3nghS13U6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=jqWNm_-KNXF8KYJDiubSm_8-RAEW5B1quM5q5kiCfIl7w364K_aPUovPpK-4v2RTaOlS08ZR2k7Z-j_AzJR67_RxkRfQvfvmzYDLyGtT0fBmkBWKIgDJRSGuQUAOLV4PzfXa-wIO7gOPq7oxyKp0yhJ9_HNV_8A84-wv-dQUAgAbtlKnrHqoflgiGlgQKORqQtDEUbI_u6Ynhpf2U8aSpt76jDf0EFg6anu40HL0my2sd_Xb4yLGekOeVaj4-6FATJoC5LXtiFe8Lg7-SbB4x-JRIXJm-x9AVUdOY_4nO_ThTSGXiRiPHAkStNyXExC2MbxeUxUwPrMRZE8m3rctTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=jqWNm_-KNXF8KYJDiubSm_8-RAEW5B1quM5q5kiCfIl7w364K_aPUovPpK-4v2RTaOlS08ZR2k7Z-j_AzJR67_RxkRfQvfvmzYDLyGtT0fBmkBWKIgDJRSGuQUAOLV4PzfXa-wIO7gOPq7oxyKp0yhJ9_HNV_8A84-wv-dQUAgAbtlKnrHqoflgiGlgQKORqQtDEUbI_u6Ynhpf2U8aSpt76jDf0EFg6anu40HL0my2sd_Xb4yLGekOeVaj4-6FATJoC5LXtiFe8Lg7-SbB4x-JRIXJm-x9AVUdOY_4nO_ThTSGXiRiPHAkStNyXExC2MbxeUxUwPrMRZE8m3rctTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuhSn_TZZKUw-IsJ-S6SIKFhnjSVkeAICTEs7AkZstK1gOODCx7ml8Xp-gGHYNQoRj4ZwQVR4nQuNs4aku6e-LIJFDy-8Qpl9AsT0cH5t5nhDHQRHkwUBVIjKAzaOk-sicPptc2jzVo1XloiVjW73zV7OQLd3kPEcRA4EDgVuQTjbs9FPzp-hLQKJ0IXKx-iN4jXOkJO6rulw61oQ1SxmSrqIOxl7uvtV5UBy9QT_4tOl763OFyl_bxUvK9NpcrztuS1Pp8W5AFsojm5KjjD8uwUqgXo-M_8tljlxT0yGPQrsXqx6YRp2JTZTlNDSc5j36i6u3Sg9SFDip619iJB8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV59ZUjibRZnRGSUPtrTXG283Zdy_2X8DJ3CvEEOp0bzIvz8Uvwlycy8d9l-xkeLNlkq7qQ90wau29qwQ3XAKtCNxj-uAWabTvlFCdFXORbu2aRqFZj08mItwF283XaEW3dYv2PZPgUZvxWPL1e4WUwo90qzOc-FTDqmNrTmXbapgUkTgoUfW3EyoHFgrTgG8hztQjFf-czZTTWUzJL_p_onW1d9XO7Hi33WgShuTw5m48B9qeRXdgT5BuxQcy7ICz_9O8FG_aVboR95M5EK5D7fO5gkjass6KdYxjSO6Eaa_OhLxJXvByHXz-zpnqihkekR2zxInB0QzPyNJwIKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfZu65cBWBOMr41NO37P51ZebrmjygVtOhJ5gkS2kY6UsvBOx6NUURGblGZvj2iRWBW01q1bU1_KZuP6fAn1E44WCe9gZ3-3Jc_p27dveYM0sd7KHBbyiDnrd1Ax_dkfJGyjdtWt0AwKQoOsL1uChcgZgFras9YQo-qt3ZnbV1L-UJXxLz3leq6VR_7R0Fat7hr2R48KRy4jdsLHgYrnT7sZfUR1wYyLWHli5yLuTVHkdhkUfT2lf0odb8c3QUetDbg4GODr9OnfIxhB3EtBGC3nJ53mZaDcxEYDLcJ0AAOWSvWKkYeRF6N4hivWfbxSrNmSmujUYal5JJ1cSYLTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6cquC6u2nH1jH2j48LRYfkHP2F9UHzyNpbGKdYnRLxocueCnwvMMLo20lYrNPhKYd96gzwrCIyQ5P8UmX7b_p6ZRJl8F4T9znVD942uztL3Hr-qCRoTXFd3vhFvYBICu3EHQ__uCGMGQzX4S_djumr-cbxhf_aYxJbbJqFN3oEpeX5iF8k5ewoCE1jd-11fmSKoVlU470GVg3J0vwisG7erjUiqD9EP_RRZEjpz_8pLAK5_ROZpZAg2LbaF3KBFEYRO20yRIEMvhnEKXJ2twmEEj-KY7HHQJZOsfyhxMfXgbg4AZWPl_0uzt3Jq0G1phcnwP7I2PsXHimqbQ_PY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JytOSiBR9aCbdWkyBndZn8uevqd0j0Z4t6_Sst0oC1tEtt8exh7oASf-k09w6UwG7rwsXan1Z7URaJ37SGQDRQl2bhj-eltC7cEkWYiWjqTjVHnHpgRqskDGXyfTBSSLDpnDIoUFev47H5Kf2rOsEK9tVxxYrjlWpZnQ_MCyf_UaBMtHWEqQtmVLYauXA57iyt_KM7siwoStRuYkJH6aE2mfu9KB9yXmpehnINV0pEO9cgdcQLH-Hb31nEb3p3NljDZ5HjcFe7BsIlvIdJw8H_wP1PyrLnEcNlw_WJW2SzFoU710K6euRtekOeIwOguYDK7SsX0cNmjEXO6O6zlotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRprLvyqlNDQSFttiu9C-ZnGkhW6DomzMhUTi9at2eXN1lRaretIGZiMDkPev6GDhnecG_LZ6hhYJCwxzrkNSnUDOmcl1DzTgnFBH1e3ep0dctzPiXyBqOGIqPfkWKUNj1o3hgR52WfpTzJW7yIzsILuuqdD3hWtPe6TBHcEVaCR8y0te-35zyuFXwA_Q_U0nGi8Dl0qRJhlPkj1TZhhobM_LH6q56PHwi4JO2cCahjD8OBRpQYiNb6ZEsj7_7kjhm-PXdnsTp2oBd2c9LvloWbIJru0VwOSLMVSIYeqODIcMgqOILESfs-xwHbQa1sdXDBp6nDOMmndLU6RRewgcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=eQQTFmpgCNWn2xXLjEdDpwWhO8QewEb0NL-2lBdPSpMTnQYNsGBSrs_lfX2kaAQDBbt5ivynlXgg5RjZtr9_75D5ariFA_ez9sgCY8ivaxxaagTKgyCZABqCF2Byx9YVs12e3rLvYYIIkntW1WgYsLkPidE_zTNgy5mybr4ooa9RPe1twYqiRt7v1Qao_9-JyYtMvXPrYteJIeZwFpyVkht54OAJRz-01PccV_WWiSX59UYtDLINehSV8XNnwdiIx-milUtwII9haBYTizP4An6TyfbMKdn6Ax63r8yRNllMyzrcz-Ac0kHvyFS0TguoLXmYE2myUacRn9FeWlzkpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=eQQTFmpgCNWn2xXLjEdDpwWhO8QewEb0NL-2lBdPSpMTnQYNsGBSrs_lfX2kaAQDBbt5ivynlXgg5RjZtr9_75D5ariFA_ez9sgCY8ivaxxaagTKgyCZABqCF2Byx9YVs12e3rLvYYIIkntW1WgYsLkPidE_zTNgy5mybr4ooa9RPe1twYqiRt7v1Qao_9-JyYtMvXPrYteJIeZwFpyVkht54OAJRz-01PccV_WWiSX59UYtDLINehSV8XNnwdiIx-milUtwII9haBYTizP4An6TyfbMKdn6Ax63r8yRNllMyzrcz-Ac0kHvyFS0TguoLXmYE2myUacRn9FeWlzkpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXgGcWbTxi1qZIGPl5YrWETNhs9VTk_npUl9eNTbudrkaNHLwq5nQzpxTgai_jtoLmk9D0aP6bvIYDWzlBwr4iekTI4yjFVQnPAny1ue4kCKRngojvw6Q5rdm0Crf6pIeEl8_nll2zadDRaMpNaGXTtwUDtMwmES5TyOiAptzu5vL-YbryoU8zw2T2ws2GMLTJWqfgs0SGEF1LT1u_7ebTlU4HdoN9_rPLQa_GLSvTtzwvRi4Fs2kWcLs6Rooh_eiVx-5YyaCWeWkl51aK1wtAvoNug39Jpfc_TjqNN0pBCGxENciMy3W0ln-8P1XlAOmx9vyIi6bsCuOHH4lbzL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتیجه‌دو مسابقه امشب ¼نهایی لیگ‌قهرمانان
🇩🇪
بایرن‌مونیخ
2️⃣
-
1️⃣
رئال‌مادرید
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
اسپورتینگ لیسبون
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kv4LcnIuSVnq6s_WyVqmng1f3EDI3ikUd-1KUolBKi4UwEAe0K5T7ZWv291p_1hHgMyXc2cee9qM583EVd2KfxgKWV97IHh474QLzEX5RVcKfZvtvlyX7ILDd3dbCKKv7q3gdQ7lZ_2zeurjetC4Z6sp_oSULAKCgitH5haMBZg8hHK9mKhvY4DgiRT1z01Y9Qh5bT15WiXAgiopcKlYYnOcyZstuRdjZwy2bJLvpVh4JbWDorg6yBlKaOYT-SXcw1YhB66DfPSji9-b7Ap5HqBkRoMSdOwVZND6Ztju5KSCRSvGygK6murRYN_zAnRfm0lBfQ-_zDhFRUIohKfbHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYYJJiqRR5LcCvjU8tvIyUbEr8mzx3dp4rD_DnX_bVSCXewxfF3opLIR5uZyvFmkrCUW1KN3iihXsf_bYZJGwWiX7mwOcY1oAQd4mqBmbjF5NP1Cc1Ov_yoaZ-JiCsFod6bb5zNNHsCsm0qdJOvHji47p8JYxfh7WoD2l3t9UaU9yVHtGxaGSblBvP8BrvTFEuo7xmBdt-BJIQcL5_XxpdfYeoLtpGw0sAvPiZrfOWK1QPdV7tu9sMW-b0kPYDnTUuJ60yGLgkfdwoaHGk1FYgJWXBGmFTKGmHA2f_0UEc4JH5F_WJaMuXpe7u6RZaPnRyeSBQWJT4hOPV-wt7E2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUlsjqI_vI2Q4L2F4dqTRyzpZbhksAkkBucuj8BE-JKA7hFmFxtMzIBR5BrXNJTs_DoJKuk63IknYygGovID0JFB6XSOh7252IHR69mqtigwAMBw4R1bmiXd1b81NMhpa0PVAip5H0UMbjVvBJRXSQeN1eQsvR_btpu9P2nUICGI9zC2R797E0qAO-k2ALm7-fBcdW2W46belpYSH7RPrqmt6ImsHB4rTBQ11BCmrVjuT5ajlYLHC3b4MPeK7gxRvPdFtpoUz28Ti9edsOfHzCDYT7_GK4J6XwgeL_fbnp0RNJ2blIXKm2KucAP4LGzSpp0-5fiYH2BCfGo0UNjZog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQriL42BHxsPG50XRJ6dM6DYT-H4U80Y5Wf0MtRwSyM1cBMq_A8bLQafvcC6IpU2gHtIHvxZNBQk8g9Vu_-9l0a0mfZaqgzev_kWx63kaIrtx0VWCuqGKa0SYs2hCSLq50Fs7dkyAjkcBO-qWDZU-hHJfVa4x0FkUCcWNZeG2gvcgnj2ZBN77w4hUtairSGoS_sg_lrHz2CZj3hgNGX0AfobS7ibuV1ejnSz3pmUm4Jt5i4wTWQnvSCZt5ZtG4wA_r4bxJfpzQlBs1ypDjMvYQ2JhQJg1bWuNYpg5PX0YT5jnMekBitnCSakS1Rub23fNOGmc9PRPEeXPPaL45w_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
