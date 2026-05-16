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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 15:13:52</div>
<hr>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0peYZ67qDJI96UqBFyZzEknSGTpBXoQpbltrLVztRo4HDjFzvhhCUlFniDosQ38wfPMROFAMgTdPObYvDTNMJyGgIJQBsD644cJtUwvzgjDKDqbOcKXzoPOk4QMMkgdEgJVfqnQmihk9KpYROs2XAxZNq96oC4NJaJ30CIkGwL_fr8ASMVkGKdvRhKgZh8Pu5YctT_QGaF8JdnRtnTxxqlFs7poViivOXpaxZcZ3JKe6-XNJGjbctlfx65myj6eZlK8Q9vldL3dlY5oxk5l7VYsXkk7XR340IDYGK6kkZl5ttXjnipQ2_49bMHWuMtqPUD-F32LvrX5MwOsmRTt7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoRoYkfEyp5ZaVw908e6n-8jbGXUZnzyz6UkLAZJ1VFivww5szzYzuX98VKH7EZunTnXDuAbKknU9whzBKDdBwQ12atlVK0UYFBCt41sU_6hLBM7x-PBMiRUOx-un3Ng-p9bEEg1_RR2ze9QGsXjy9KVdg1hFjTjypqfJJpaIUaMAx_Jq4K5uC-NXaaS5fe1cVvbwO4ouib0qCCW65mlTJZmlTjRTthBwuOjWvzLN0OChga_grgokdtbp03DcOVYX2kvjRss-cJf_k1zu0_EcycxBzgiBlRitDgD5LQ7W2KKYCRyzXnuAtvHoCvPiOVfPNECYYICR_sDxMlPZW18Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_95_oN5pAOeuhObHOKCQu9U4mWRh_M-LUZ3jrIKQ60kINlh-_zbkm-Mza1VznxnDo9YzR10rp0MndseLQjReROMBURAs2Co1gD8vsSYVStF-bMTFkkTw72E6db9bhKPEJGatI7J4nMELPr9AXAr6gabP1NhzI3qtTj-gKLnLe64wwtZfbcZQouALraIbQdydCQ-sbmgTWfVK94pkh88ACgizGwrIKZmCsbKyexXbDbZKa0jW7hMQE65Xtstt7_0BJBcQBZ3ccx6Gsu4nqiwxXAn-OABMMvsn_5T_n0nALKGY-uSotK5cyITXXdSta6QU5NjPA80Hy4OrMJdXrIprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22144">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/persiana_Soccer/22144" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqP8iIQnxTTOT25mIf5zQacLD8XvYu8HuwF-cHeN8IK0sPAk2qVGPV5ncoDUQvBTkqjWYq5iIKRx4rUDbgqMo6IREGOUMh8krVtC757WwGTRNPO-VJs19uPYqoY-BcH2UqEv3QImFp0-M_fIKqqADJP9qlWTVyeGCLlGx9vOMDEiPaT6GnXcmB1eetNX0Fy9fre0U0fabceR8cXgXBCt8qDE6YN887tuLTDrlA8RcVizl8kSiH9ELXpLmGvB3plS30SCUOXz5vTSsz0ICBQFKApXGZidcVFPti9WO3k1dEF8EvIaHSrNMnzh7wO0eCgmrBeagOsLAXI25xpsg-RPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqgN5LOZD2Hvdzefze-K98Xw7NAEgWEMQ8VVk2KWOpkFuhGEZml1u6tmF61Hmt1LEu1FOtJEWO08BhbFpfqJKQ9mxtx0_dwQAcHyDqJwl2VHXzpysjdGqCiquvsOwbsv3z892Iy5No64pQjH1OG6YEDyBS727R6beTKja3cYzFDIydfbTYjG7n9niWEw2jKpi37qWIgq0_EAqL5zSN_3XijXXje6F2bTALu9l7tXQ2-w_UQSpwa6El04Buif_rFz_YTwmeIbsY3vR_WmPyJqXOhQeKnwURBSBZoEs-ng_0NWeylOZivw9m_njhCl8_h_r8c2mCb813jCB7IEWSV9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22139">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/persiana_Soccer/22139" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjf2OHSgb7yexZUvMdXBTOzPld8gXy-osMPF1JTjlB2qYFv35Q6Kmw37xCcrpUUlbg_H90Zixsa6pxefIThJZE9w5fDAk-p7B7a93mjzJ4hM9QDfo5xQ8S_dzLA0ipbs7nPifyhIxlVAqsdEVpL8oY7Rz4cRyLKpzFrH8UhtcBEm58hvLojrJMDNHMJFX6A1jXev0adGZAW3s0nfZnMFVZJd5okHV-Q_xMEGHjgqAYtXBITTdXwf1_Nt8gbiDZ6vLjqdYqxJYyUs2CY4a8nwdFtak8YSfjfvsD28z0dP6KHvi8MEQ87hpqEbQNw29Bw3f51LWVSmtDAcRYXN1oaCzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HouRGZKllC-DUxe38vEs5IL7bHXLe6J32Yhps4GmGvpUY4GRD4rxz0uY_k8VkFNG1QjPtjYpjeqJH6sve70pEfMpKmINOZQDPSekSjX4_9CN4PEPrVnGNnw8mhvcxWQjJ0oglcKE-0A9X6HdrCHXreBHnXGIuBEE9PyH7X4rDhoI147tazhpFglVZOC9NA3oJ9EjmXAOFn2UZpaDyXPtD4FKmKkWFFAeqBOP-zu3gN_s8_4P1BmYmSFGj9mplKTXhFalhI-pm-3YLFOLI-RzQ_96ihr8SX-wLUixL3Aq7YpC0U1tKdPmR9N-Dxi48zeRDHVYfl9V1XYAZ2ob08ifBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orGYViA2WqwKGWC5S7zwYlfhqbVViGhpBo9XtJVDAnXsleap-NkXTJIMFJFqa6GvigaXna33hyyknZp62UKa4gL6l5-83djYkLWwKrXdG5fdCmJG-tz_oItixoO7GJlU8JFrMFBHKfW6vxG0ixFgik-vqh7-YDmND7R9BQi8_6enYfu2Yt4idSrax3_PArNTtcQ42JhGor4crSTzZOv29gCXEsHY7WQ70fONggAHgL3Iu88bsLFgpdw6ybw12F_MNgxy7b_zsqMZBeU1JOrlVwLIO6jvvkpP8hMYnf5zIaWDMjUxPJBh2_CT9dnwsmXHiG0de9SL3dTRQN1_4FP-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neYhMqH43S4_rqGJvDPy_I00dT_O0mkEurFFRSobdRandEdbaPUk01bzs1lA0ufubWEdQr3BYzkUPHHuNiIAFaAvGq2Nw4OIOeK5l7kBGckKmubylqFZCK-ytoFO7d-lFUleZDQz1XhatsESBouyjDNuoDrmy6QplynT67WyWuBSi9aicqgq9GJZpRJi38CnDn_I36yn0QijXBzzsIHc9AjizdB4jDMQmoVWVVV3ZCpVbHtcdS8u4lgNL7pqFq6-89vMvgeMu3-sjQ-0750xP3-B-_kPruYBepFmhjsHjRxJ_CXYY8BeRLrNUlwC0gaTSYt4kpukS1gL5spJ5H0vHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce7s4ke_tTYnreXVKu_g7XaWnUtNn9GLe2UUZXhQxW1oM2BnwQ_0CFFk_IcpNAEgyfKLhU7PGCFsqfhvDk7qbCyvpwUs0ow6jQ47idiqEhNAWSioAhf4WW6HCW_kHTlixCjJeulAW2Jc38Mof32Ku8lirGrGXqOeo2iVldS0Ax3pPjolyhk-q7hvbiyHEA5-MdE5xZEa-_Fd6XZbkiBZ1ZGn9IhBWXoGzBGLlg0_RpbixdZoXTx1li5R9HCDmw7rjkhHvvuz8ibyWxeO79tRlWdSC-rQzvouUgfDNy1ZlS2lSn2pjHupCA2HsjFJ6pXRHFQ0ddho6SSJpy7OZjzp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK7NqZPJUM1FujZlkHxjMUj7BpxfP4a3Umu9D9YOuyUMoOx5rdCm84RNSPgZgepKGavhaY2LsI3t6-bIWUlkWdhTmXO_F0KnWDdvTv3ADhZlvw5lT0Oym2TYjwq7DsCjcWMkb2vaZRC5Br-g-__4CSNSPVT9bZopPdQ4XaX7qlxlyUTUrzut4qWY6lOomdEgkMDT31ecm1vBnPTm6wUOBdpti8L_PDT9Nkeft8q5XoZRgZjRMHL9lC1Jr8jHk7967Fs5XykEzh9DIfq-MZVu35O8XuTJ9vzPUaSfAGsf459qcTVOBnWxN9aJGtYQtSmgnVJczTNdVGlxYJJCIITtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAZsSP-KgjTz4DHFqH87D-GqzV4vcx4fV81bIu_5ByhFbmA04Qk6K_qlsbSTD9pv0TCa_ZuxfBzyxHfxZ6p8LOa2kGIOKAjgBN1EIqQt7nFOb0D9aLX6cv3-DKxDXXIs3_jS6EO_YTPAM7120mkRmwGb2exKhdyHBH0scjMW5RH0arDfDGdkUWxtBCPBHU-Q-M2E_gnAX-G2QPVRQLbG-gfWrroHCcwrxSbHqysB0ds30JoJLzjbuCrbovXqrG3mxBbJ8KcayvJ7JCoo6aLTOczFrD8M-ADGFaTR_EW9jRdCbOw6bzf2N4r7C6QUOEZt9ijTTfUU02uWS7WGvwpXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZjyqE7wTKuVz_YmjiUbCvRqdMi-kAA41obeYkhy3oWm0KX_PRtMkOE56z7H7y3sTLJrVtAc-MoQts5YudvY25uHyTjd_o49kFDOFdhf0qesIJDB--afvMl4VKBQs0i5uzBXth8_vOkqgSECk-FdaSohNYCaTaQmbhQd7VoS8gWD9gj5fWNBTJeaGupvEwGMly98QU4Z_AfahnoKoCX_2G799xnqlbJKz7JbxkvAnBXvh__9Eg8MyWh5jhpOsnOmUYIoiRMaG9PI7sF6XGBJj75gE6IlfV8d7YqDsI98eCAkfuKuCMI_6jZRFoQ2JgXBQkzT__ardqgMGuv5LtRj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k42BdJZEKdR8GdlL6DQ4-sEws1ucUJYRuSJbPKQJ-GM3Fx_0jYcAjvOrOqd6Hx2uTDK4qRO6zSw9dsHI24l-1JyDECYZxUNkPUj-vj8lPxLWJYd6aQvnnlG3i-QqAmKnGW4R0qp_fYZMBV79TmbUWcf0yh6a3l5ZFTiCyMEm6CYSmKOtqKnsTMvwYz0nfRk8FlNgyhbqf_k6QopipDumqrTc7JcWCmE1f7W8khuv5cewm1l6pH_FSMUI1fSM9uYxF3Uoi0l1UpoiaR6RhpL_joXDbW4TuW5uRXR5-Ib1XGRXw7c2SK8h2WwTm1SI9h97C2Ex07S2GHycu2anIxpOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImDrEV6CiVM7zbykIV5GZTr7PD24F5yyIlyYXE_FdELv5mGgnkx5urnSpCNTMoZTYtuFK8y-cwwvhqRCvOQsyOmqeCDPD2bhXtB2A2aCjYDU1a-ZNEqI168czD94fKzL8vg_jj1N4ylyNdcWf_IyI7xioNE_69A1zEq5utJq05reLZ6waBrR5j3v89BZ9cOGpzwKfDmPYdIe8Tm35NFNpwD-GpdTMu3haZgxzypu40wIVc7hoyR8LY3mQosO7Xd0Vwp91_2ufsqKd7EumFd0tCgbdGI94xs-ZmT3qAhAnVORY9SLIRZF5ctx2HBXf24bg8xvMZ9YBYaw3H3o0sxuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El4nrKeVzDG06g3g8gFV8IpoMEWwk9YhlTj5juzOYhRnSJTtyhe6lRPsLPn8MD-6AO_kIM8p8B9oU0Ow3nnBE_1_6ljDEUiJdbYf-t1nLm2busMBtFyX33iSgTP6hRQT5HUigfeXwq35thqo_w_2XsjIg5GA42Cv8ZRIIkFJrZy3wgieavigpiRdMHzRH9r91AmhmF1JbYCJNTpv7vrXrM9EZZ9YUAUyx2G14B8Mbfp_z-gnSDgqCm532dXGrnvnULBGzjgfF0FIox3n9t44vs_bDmlswWRX_L6YS5HTS9EsPoyoY-sNXRuouB11iA7Cohp1k5IQ6QpkaWWPT2seLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzfaFskVdTCMjDf3FehiGVdq7LHHdzoyBdof3cC2koS2dB6cAZDvBlF5Ufg-p3draDR-9K8bCz2uSzNQWpyIS_HpmzIgju2WGOknMcj5Suv7JmXuoo4Lk7ZxUhoOqObsttmlswBv130rYe_YvczHd7DF4J5OQbEMI0OZS0MAzitK2XOGc2jbGZ_xPjjjBe7vrLK5kE_bjYfsiJDkPUfH0gKyjp_rdw0P5OSgvw2-Pk0Q-sIfkXdMDgpzZ_sjWVVj2P26jH77OlVFUd-86zvyzQ6YqmbvKqnQyF5h7_uPVNnnnSA4lUCOwFKU2Be_euGY2Taq7tfZXWvwttQoNyNORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOfyFcLPZhaiRhUBpuyHLyZHSU5FQ-kFA9TnXkn3FsExCxlyb9GUhkolGI8wJmSXO2pN5PEB6xLEIovvXHtlxfpmh0IujrboarOxDV7fGO3MJ6V1z1j--Gnhd9LB0-g-zTpfEkUTHMVzhlLkeyaSLS8oiVT9SYBXFWjiZ5JjVet5tTItR8-gW1CzmxkDeMXfWEYmvqJD-QPltLbO6WtmjSZ-RnVC6EdmcclZXAY92tXJQK_hUqsvmejEhdr39AJXBdXZQm8y2ovRWWTA6QdjbU2qEGEjmvU05uOHWCXgaTt1r_pKZSWSHQWyPdlnyGRKvV1Hl2x6yTTN5cLb1qNY1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMy6AWIkGXY3opc4psOgw0v5Yt27JDkp1Pa8ouFJ7eERmDQyAwVtIcCNBFSOe-IJofn0H51p-EYfXHEzPUWukGZ9_G9aAquWQnX4FMKEyaKT2Yl2mxBDYPBfhTTtsd3nX0RUiVFtzq8S4BMkszcR_vAe0GsnFFxPY43oO8GOFH-GdoMC0R9agx9A_XVGhXsKMRN0zjRtDeUw297USoPUxzksY-yy_J9dQTypUpgJV2IEYhS1TxKfIEnXG9vJ5jPNPGWpW0ZYKotBNdNdWtlsX29nHQQnT1i7kKFfAivN3qu8aU_TLGH2p6BtmKx7N3SwmJtMXa21WYm5XPwBSAS5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHs4o3dnnLr1jZNJKfSxDrvT33D4HehH8520RPMuBSfxf_Xs_vp19g8RuzbVXXuFQ7mDDr2reVcmmjqLLuYOl3YaCzRocDqhiZOootjkJlqdEIukcbh2wpbHsuWhS54DCv8ZW3VPVeFwoAFlhxx7_2t0W2KFhcUfeZ8PNeIi0qyArsckOVhiTPg-DAWBDBfTPa56jI2orobIlbjw9cwWSPqKeOM4CrlIdWKW6Q3K-TbgkXIfTDulTh5P7Wbnb9I3OD33b8mFhXMcLGs_AH2a4YG1BwsoRdcYuWU4MlhNspq1kqIGXkHEm-7N5naU4v15QYzLrTYIO_j1y50Ctm2kzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9lGKKlhptUMuWdrZukk2Ppt9ukr7h9KTKEAFvUTwRI5G1XWsE1dGJwwZkxd9DS9VZbkx47mc6EluGJ6alWMD7o7LETcp88KjoQQY_8cPdqDpkSB8waDZ2zT-XXd7VPjumlbVWFdKf1b_3NqH38A8EXpgCSQGCnCd0cqzYqK1rFNwte10V3Ia5zfrX-YTm_WwgXodiB3im7zDSn47g6kIvVrGGAIW4tJn7guoXbiGk4N1WCeMj3ACjY9dJCoDLw3Q41hl30SUPnVBaLqvKEeN5NAG9Bz_7GqwDtjG5oz5qDZ5CuwaDcbBpcirMeEmMYZNLNKrHYaFFFh0Sl4WlaJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hvZfHtEjwoNwVONnprBkmdyEevR4_td6ACsnryHv2EOKprHJi6DyW9TeLnc9RImGC8orZGlE9d_dM--vvpXsCu9DUegMehlPuyILPPwOwRSxNYltOrm52N4EuTecVh_hoBYmtRilyovmIHEr2UhmuG6s4e1Cbv6Fh1ufxTn8NaY_JF1kZ5g-v4CpupDqePUxPVT13GKFZinDtx8SmRVGtYAQZrnDEjMtaQm-u-DMOdr4aCGIoNdzbJWn6_nt44jjKCCItEVbkaT5wZdasHa7UXrPsMDDZzFR5S6hDbdK3nXpIJjv8s4qpvtC9Wwv0WmnLqAYOoGXRPH5vzU9TmI2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuMbiGRzu8vs9Oc5G2EHmiu8nsG_WtA9ZNnJZXqzMJ6ER401biii9GkUO9gjZ3jJ8dxv61kxxaqywcxXOfs480Do5jecYRPO_RnGkOjj70RFL5R9XaElzQUe3d-5mU3hs4_Hq02-pq8-KgWgVDX7spA2mCCdEl_rIC1WfUbSOmzPqToyop2yhmoROKQpRiaJMI2PY8DrFRp_rHVtJKL_8464z5ACdrhFhiFw_S1PNOF4hoQAKb5Nin-t-R1WsK60WRm1QT89WjpOcaHDLxbz4Fahp3rKQG0B5sAchJNNM12du-NRl4R4b3oNPgTpath27oE_p8jY7IDsD5nSzO5JXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuthhMpSlspMj9yKcrPvBxBC1zX23pha9iH9lxOmSlKm-a2mAxmYwuPZyntE9TU1jGQ75ydbY2tRd2eDC6DN1F5aAStzP0pK_KVBwSSK4lQy95-w1s0u8t3TYkEMMM8eJDoHHs8B0af8DgPQtDugOGaSUfxNZOTA5k8CBr7e2s79n5qOs4oF4mthyL4CEDf95I4x8Y142iOe7LVIsdS2oop9E3Teah4gvCYiYrHAxXUc6hb_GzA-bpPFokptm12_CsPCuaelLlKJVP6WnjDF1VrGEwV6VTaljehSF1B7DH4zWihSWZf24u7dge0Cb8r5ETIz0tID17HGr7jNdx7YKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNA8Fnzo88MCihXq6P_7dqxZrUsm0HEw2Uz6dozBLFYQRb9jDiEJ1J4HonL9I1GoappTfrdWj7vtYF3el-ul9ol-bQW7XqA4kocZaH0szySzucQTJpU5mbe0huPXvKNjmKmz16sSQgjinrW_PT1gFYEPIwFGMtzYA2o9UR7YswLBUkdtpyOB0TQbQY_J9soPyAJGrNWOAKcho1Z71W-HpCkEmR327E_aJH97lFTe3KusEgfFxXXnj00e6rD7-cYWfKhVKwU_co4gbwTB3byo_J2KBQLigVn_hfr2ZMaefLCV2mxOMLIqTLCfg8GgUixin73JxJtqSa0esmRkkKOIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u684zVM2hwTXA_bOJ0r8HwO8zb_868fwlrKzrgDOc9AS-bVOycm9QvUZs64TUIHfLzMG0y-tSdH4JIFm-3RlYOqe8fEcg5qTEVJqqCHjzvqVgQPsP5YK8H4gK6hoBRp0rcxzmfgfn3M4VZbLTm6U9OYbJCi_bMb4rlHXyBaU5lrqRbQMv3OJu2QDaVx8rtu_EFb6iYrMJHBdYu7OJ756MiAbT_BXQiyzH670XmemCSL1K3hCVE9kWN3baStd_91NSDJLWxPVOFupg092FLohGg3y0JrKgD4E3cjaktpa4bt7gzFdgy-oI234qKXy1uL3NwiA1MWNPwuu2mEcVEKXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTRUR-nEFZqyHMGXN6roIllSzxzsv0cWCNmDdOiO6xrof2s_IB5G9kw5_-mBawnuhwhRN6Tpr9zYtgJRHhyDMLot64Nyr5otaxX3uyE6-qyekrh42uS7JLQuttXiweK_1HbmzhFrA5TKHF6r-fbOhRQqzkZ1bbJAsKNw4rnnPqAiRo_-iVQVmxk8K1DsAf7UqDYmbNM30-Zgk3IMOmkkcOVK6QVH2qOEd5g1LyfXI8CewXV5x-VJVPvo4GFCfY6u6pDlx9KjkkzoI3dM2A_8ezVxUohp02Ccdv4oTuy9zqyAWtXrmvsHo0GxHZhallZiZSDCy5jO7HCKB1DoAMilzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jpzuqe3apGurf1vMU0ZZjaHLI9aBC0n2nYkik8GpzwBapFdil7j4F-Ty60xHq_NgnmnJbsuqFiVJ4ITH06MREcK60lpHIheah7bG4bAXAmfpPnZSeMPtITWIyKGW2Y8oTzqjEIgpZtM88kvdPr8xH9xh-_7zOS69D85eHjA4fbmr1SCpDAOXzRC0y2z4hoZ7GB_QxmszelLu8UaFDo8xu4llEibwvxM6QBO2WKDiDzsgNgj1PiIGts21ZB96t1wxPjoK7ooOaORW21kshJrUS4txI6Ums8AnRh22n_bVAFZqS1L7R6cQUHvO41YrxJZMX6Dnu0z2o03Vs1AI1LJbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoNCAf3QjaaiwloGFqkOBg1AUKEu3O7RgCZV03z7BPEPkFJtNZThWKlA0YN0gd4No_hHmMlr8lSBlignpjf65RI5k3VM8kVaN_hhxL8phzsVG1pcVpfORPVaaKix7F7kkGTJ63AhlORP0wfs_bdH68q2p_Mra_dXa_LayszFVsFcJ0giDCzprql733phxizmxJB8cmmwYnlzGpl1W96qgCKW1XIXHHJXfDm2qBVG7VV_tA5BJJnDfsqllp0-f1KKfuFFU7UgyZezqubtHtAcO6WqfkLnIvvycqXfMpqvtVvap4TwBZGIXARvuqdsnrRKHXwSVli86NPiqbjpyLWgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYoo3Sf1Fyc3-7lYvd_fiA6sluqXKGsBJlqbLuqrTaO0DRhkpeWk-6U_GzPyD2wzsPeq1Lojm9K2Gpi_O6lmwQXGX0kB6SpbJ3gAzO8yTluEALrN3m2q59heqbwvZPtAa5yTz-Q_3hbcI1nb2akjJNvphtGOsoAI_lBWvWHQFxzr127EBuwCPXOcCgXuqHDtYhEaZ3976vZGKygvo2KgqKYxWFYt7_jkOmsgpEGy0524VoA1-1LCNRHhWrqqb4OknejeetU9mxNFVOyCMVpLgl2j5-LkD2iDVNptILSIPm8nEWEy9ciKeqJhvAAj3GF1fZu4JsIT-E1m6LS7LcYbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cK9JULZHeuHeo4IH5IjHPVNb_infu7AMWYZw2Xd3DqU-scOqCzg7ixu5a-EFLO-_O72duUUB3QR1EFEFclADS4Qs9Q0NgyuwCOs_M6lUF_mWpT5rahlTPS4wWiMOkVr9J1L-6U50eaL8hCrOm2zbWNcIgQGERFc9JRpQgHqySM3nKyLo2XBKdrumxQ0OPQ921ZdF8wFL8oABlhU9uhNIz-tJGNsAU2OTp8AMUwrDYRq4YmgdOSDtYMLIMHRBGE77SbtM1kL-6T11izX2BIRJ3TBm2XAM3uSqqbfVNeQVuGQ5cmpaaM49ECyMtKHMLyh48Ya2up4OPxt8TXxqcWSGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFZXrzn4j4S6G7SKiwc-5gsiimsyIt1YeDi7b6xBUfpq7J5woHtcfaedluV47oYsii_4xda_EncPJYfBrcNfJh1ctd7enCgoDszgZ_bI28QvqlKc--9EXcvjBUQdktQkW_HZnureRPg5qWQBMq8x0xDpjbCzNeSlKqMm2CRx5osw1Ux_Sxzy9sFNxykAB68YUM2lMGGibyNp5Ig9m1uOFxQw7HmbyriVZCbNBphRgv7hpSzcC1o2Mo92Y7zjIXX6LmxYeJxsQO9GMJJXu9NrrK7nKSmdtJEwIIOcWd0Zg1ZUHq3LEXyKOiS6Ea1Q9q_PWY69dL8zQQpjIpl5njPJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVQhG4KaLP6zd6IQ1cOUc7C49cL9fJ11rWO66H3WNmd5PnAHT_wDjyvl8rc-zpV0d5cUeu49suUVbnRbZKWbbVKmwfGm6ieBm4UA6hxF14K9UJ_5VByBcZJhH-Q3hDOajZ1evU6aa-AaNBdFnwMQnfcpXAG1FYCJbrziFQertyHw6JJqgb3s22ExkVYUSWwSE8Pgn4O1r7JkgKgSpe1dXcl1_ErXflaewA7WShzhhO9If15p9C8vdBdyvsKOcHqSEJxwgap_WfH8TFEfOSwBIjqFkQ4MHgDNoUaiCHn-WEQ9PXkpeiI9Z-kI-HpkiroaSHZ1h6fS5f8h99aEj4Eyug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLUR1f0y2rUyxqx4R9BuiS_TPzyHS_s3bdcyZ9Wv7_3oWwsdomADXtIEhqngWbdd6AjtgyD6JNFAJL1ovj2DheF80LzZNm5F_FOeOD8HZOcqThoyM203Uyjk4Ss4dje0ZVgsHZL9FgcvLd2alGGdmPj-7lsQ5sBovA0LeozVlIcVnaJ4BWVZw0c85vyNL5n421eKel_rrtJMXm9wv2go7lKornZIzZbevM8u_6hJnRbqmxI0yTfnPuYSXD-eBnUi0PxWJ2g1uJe1ho62o0CBPOKh1Evm4inhigade5HpcO_9mZFOQ3Ip-ElQQGQFIgJwzSRZC6B42-WKjm9ZQRUcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=ncybOJPiBJjzH1D1SUW5bVvA22SHCaJtd_vS0Be_ZjY2ueIBVruqGpQkftU5aoNH0vAOS6lCZluuLpNEhgDoQLt_vojrPGDJbT4JoAojZ3pY_RPinIl5ZwjxOfCsBf8CgB8o1iCnhx5k63FnFIMo50S62LMBDqj4JccTXBLrBlohtwZfjpzms7p9hUpqYTDu-ape4pdv5pSOVc0NJgKVzZAL2SlVhKPj0ReZD2z4PfEINbVgsjHWyU5UVW2fsaORZ4Y-gO9RYSnZHh6rTGW_ySAAccsUSG1WaBQwTdvubGXXaXG4QA7WdpUPahleCIMf49tv-snbp1ZffjoGvFy9hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=ncybOJPiBJjzH1D1SUW5bVvA22SHCaJtd_vS0Be_ZjY2ueIBVruqGpQkftU5aoNH0vAOS6lCZluuLpNEhgDoQLt_vojrPGDJbT4JoAojZ3pY_RPinIl5ZwjxOfCsBf8CgB8o1iCnhx5k63FnFIMo50S62LMBDqj4JccTXBLrBlohtwZfjpzms7p9hUpqYTDu-ape4pdv5pSOVc0NJgKVzZAL2SlVhKPj0ReZD2z4PfEINbVgsjHWyU5UVW2fsaORZ4Y-gO9RYSnZHh6rTGW_ySAAccsUSG1WaBQwTdvubGXXaXG4QA7WdpUPahleCIMf49tv-snbp1ZffjoGvFy9hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9jLHZ7Nsv8gKVDO7zYylxTWwovhZjBL-iu6HL9SatstFtZjTU6EMVGAhPi24kXcfKPANbfyBMnk6-XgiWa8RcvOFs1T_qEi57k5VUIQABphWnjUAGWGC2X7gvaprZh3mARmgQNWkB0YspMhHaKcbV3kkHBIiPSrM3wXoNwrcK4zHj5k5Ph78x72X1DjtGISUR1Je3lN4wyUUfiGjPzLIMM50TBGZQbBG2Zhe7yw-ttYGHjOU2rWuv0a1g1cgzpO6LqPuJefBpOfGBFwlu7ETh4NY0nO7eU-O1G3T4EosExccmL-_hfShNPAAxLqtZxVg8jfx2Jvf4p7CD2Gi0iaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc_kt3qUDGWMQk0Liyexvg5EwlFOnCsq33TpWehCtGAagSazennv1AQ8Z-mtDqmtz5M7Bx3tA33X2RyigLJcOOwkEXJWzrmIcP2cBf0a_1-EiygMF2nYthjm7Lt10OnHZBRBAk3Q3p6AQBMbtMRH03X1v41WN2rVeMN-lIj52C0DKdBIq5LQZuAsTwyf_2SM7UOEdowq-W6OTdMcg5knmDvcivefpkmo2r3_Mo7Issl2DLAMDh6q_JbFYWZ7mXAgaQCyHzpt9WQaUnc34dxoWRlx6Z4LwHn17xquoRWx3Kh2fX8twlNt6O_21lGxNJggfXpxB8O3StG6mp61ApA0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ13tRt4Zcw69aQ3mO5iV1daNNPe82FvVoKHp9KNW5BGpJDr7vxHUkCC33zR1CE-KEpbpNtmwGWMbINitteWkXesk5aw7sVhmpLufBYVhSaYHJQIXRYl9b6nBCVSAt2zFvzlLQfIQrkKR7KL9PpZpEVByEt4u8obgMW8ercn4tt6NFUyOVBAr8JKwAXMRH9X1lYapTq7CfPd-Fl3EU_22CCbodTCu7GLCNRD3knzrr5NA0OyR_yerH7PLHZO8tT2hY_2Cf_El14XDlIB_QAkbF1XsGOJMloGADKQVXVtwaRDu76rGBJ3T1ZkKV29t_WJZsoRG0ESOIldmq5CtyunXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REiorfb0wU0AZF412WwtkmF8QycAj7Sg90UJl-J1vm-4ZYJQoAAhW7MqL_QPVdPOMguz6QbK6ZLSwjbKvbCbFODVUwxxofdxm5WxiGLVAaPm-CmN4heC_bEgmcMXET8IY3Pv4niNvZp3zwRHPbkhBoGroeKTf6zaAfeu5aGNn8rG_Z3ADE041KOdLlbTp7RMefgIUVidRvCxT1O3tL6uySkRVDsvdAeURTQ7OsYHE63l4N-x-NXfRelThPurEsPM1ZFqMpkB9JTZ23EL80lQBzw2l-qDv6bU34j4rRTZJolChKk1clq8WMwcnafCHdWx0nwyYsCpBrO8G0GWs7N3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP0Sx6DySsopmyUWN6HfPdtbu6KK5B6UOsxztRMeQ1p_hxuqDtzcfkaCVVZQO4-Esya8t_dkSzKH6niEmiPwQWwlZKHekzGmMpaW25HS3pJ-jDAAbjNm_zuPMUkGmMNfllnEJ7oTwvJZJI3jn7XaCHKENCds5yLDTfNKOElW9GcVfF1e_uJSPBbrD7Wx92r99Z4EWuP2rynn5PuO_dFREavMBO4c1ZoxTJu_q5hj4XVBdkf7g9UItJAwiazJL6gQONKA9XtiVejxmcJVmdagjyheFnuMGQGyzXIHKA3f1CXcCq9zB4XtpGvYV-CDl1tuZtM73LPyTxZU6ZxCuG_FdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agScLELUeBcDGfkkwnmN8F4mkau6Y8YqX6-jpmK0r9lf7kG9Y5zMTcfgGyNBkzYsMtXCkaqLWhDyBa7FNiXTaqGR1l82kx46zringCAO6WoJzB5d-8LPJ8lgxyihic_zXquMPvMSHf-gvRqPCP7ONQ7WsW_NRDWK3S4OWHnXPDQCPfcdv5AC2Os-dRtuqYZhZIBYXtcF5wH6G8ZhlQJnVKkYdGVTXSQeYOOPSYSCVMxMSzYFL8VnPH5uSfwzDd8MyHmYD4g5M1O2ebYMyRlo2IZR0jjxpCrlALtXcKBfAmhh2fvzkXIOlqf5ndmAmOBKieoxoZ5cGIxnCNd5NR69gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIFydB6Sn1YW__iaR8PD-fQEQd3bhjVEOCRXu99SX4cGExbCWPMIXyMQHOA5_zRWMzCZfrJV_dlidZ_S4hiPtFgh2lOSDFqZB3teQBIaqdHxIOrPe1txgrttIHpS79W-klOmt2CiNvl6bZJSEr6jDK0ZF3Ze4lSoV7HtajAT93Ar6FMFr-7YfU9aA7sqUa7RbNcDiY8vQ3_VykKe5K9Z17ijea_GFIGkRN6HYMzYDV1UQKx3mgWfcnZbmwrHzorICAuaSQW41lyJ6YNc6zEUh2HbHZHwrMYcWc3rIOy0Z8kNrW8V0cMkwO60TmeWeIQBK-GUQ6DqPEFPFADdfAx5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTWc1BEiwVJbW-aecyk--2QfbwADmk4dQqo7KScSSaWHwFncLXd7OtwOXWDKqaXvK5qw6qam56wvuVMj6zIjKfMqQdGxk-76YDb8lTNbUbw2XR4pmlcIjfwtFtUttkDqb1987nV9rV0MpRb7DyyvL18d-pni9JDDX52UUhgZYvAJRCFCacx-qDMuqj4wn6HrZLomYsPQFREv_qzjGQ1U2XL7vdyn4GQiBIzgaffCbopv_Y2LL5YxEPer2bxbGKwtz51jmYMUqOCVWyL0ldn3KmEU7D6Ppv6wNriIuzD7Ur2ibSuaUa-BXH6fwpdmZ4qv3E_uxCs4QSC7so0yAc1qaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYYOZMKb003241xh2kjiN0cgAGPg3v-m-lQ7i_er92U7PtaKA6nSJD7X3eEl2mtZ7CX7oOATCgJnEo_HDx37TAVJzJWGsUTDmkCHzmXSFd6SM-Ao_q1c95BCmBPMhGIufzGRzG162_tQvF9I5Jx5N6pwx3nW4Ay5_EA8n7fSTzm3Mhl-1jkkIQ7B_KpqmNXXuvPPI8MvQSwvjiImSKsu7zWb7Pub7SJopna9FyIv0heKtHzlVQevfSbpx0FY8LWS96jOfRMRo890FJgUGBgwrdKxHCtREiC8WsyJJp1PHMkCNHg61QqEqhT1CC57K4O_5_aStFnoPzL0qTQsRleOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMAqjR_FvK8mogZIO-n-oRpqe8GZo6CXdRf3XfA_d6s6oG2kbHmfN_fE1uq3dQYa_huB5I-nXgtPU6a_Mym4elBzjnbcFwq9f4p0-3iTjWddQs2HxMymRA00X8hV36YLk1aIL4w9A6AX7307x78-kRGaGx2ONM5xGBRKVC20Byc4GDCLznk8Bt38MftxxTZl7xCiBRVwCmvrwXrk6o4ptRrPp756-Zx2CGBXiW-p6WS5TrSp3FcCHiqb_AElxDIqsSMXp7ZElOOJ6pfuWPi-R7uyI9Vw3Vtwa7FzmbR2Hxurhp-LfCs9fAbkLe9KsecItL02d3B75ER6-l0aS5ygPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBAtMLmfkFpmPI3-GXohL9byNJqNJCo4rbrpV-U93BT4SjQidQga_o8pJTE88F23IRP8NULFV9-JCiXjPtiFn19JTuymW32IyF4nHvE2MJiXztTF3NlALcHCnPYDBkZeUBCadYiXa-PUF0fg_GdfjurNczNx2b0oSiIg5vU_nAq33hm9rpMPlppSj9L74E4Xk9z0qA5kShAIyfQUuHS6hsDOQE5DUogZvLMN-zqqcQkQP29IbTRKZ37rQc-1QDNyrzsch-guAVuKV-sJqGKfAVQX9ZLU4rDkqwJyMLRxmqARwwo3z9rrUvnBHWyyERxgsWcN3r96hA_Budwz_qNJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Je-leNDpP8JYwYTqXmshVLmkcTj-KbecS6DMD7mW4UiGmWQe0DoAgK8NqTL6uPYLasPnneg-M1IrDdUinFIjdcwYz6sVuwKz3NNqytu6uekYniLXyIVCA6LSHirvQWSIWqTB_ZlsleBWWds3fGC63g_PHRdjtSEo3BNFpmv85w4MBP3lgSrpyvMjUGnRQRMc08Qtq-tNLMILafxS7pAyArjP18d2LEvuSSKOZYWE2eMTUdtDgphiYps3oquHZcMu7XtFPqpnwj2KxyX6uuQlTu0f_f0yw3PMaUjNS3gVgKHPraA3-P5hGW7kCQdCUkbYNRrCeVk-usnUqNAmVVaNRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl2CJ7-afUKEdAcO95YZUm56Zs1qQKo15DlFku5PYG2E02WkKKPK7LbGXYWkFl6I6vqVz4gMnuv51_i3Jv0Y_l1OWf1VOGN5l6d5p0F6wRVYH9_hrFTTqphy_VvWATU3BFxUVCaevlXuMfhwqMr_OWIol2qrAOrFov-ef7UuGbj8oCvaN308U6dq3xR2TqVbOg9FOdCeCR8Nxakz8uVkNGbaM1UQloxdQ2GfnfWjB4f7ZEZVduYr_uLGkHndC-OC81-v8FXqaiwRZ61azZZk8H1v24bqAVMWBo2kiJiK475BhC_wgvnIDQ5NAYVymKOQPPWtg4MXEMVxGLYVr-VsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjxh29CwsulkJXDruI9wUXuchTYz9Jfh2ej1QVk6nuMUf-m5pHCmI3y9vFlwpFMugsfs2wucVbXFuORAKIUfIUZa0L9ZFHDEUWkoj8aJ5U3JeQ7mmlds5tXd8V6bP2B3WEGqs7fVJnKOBMJWi7En_jRS5N2yDLVKGV8rNjzdEI3YP40rO4HAN4YjUIM0WCEVyHxbyWeuvWNLsDQddA9ATJ0zuY0wyef3Vk10E2HpnroOAZsZAonP7RU67JZElUjhlJ7n8czQmSalCyAO9TWmSNYyXoEloZ2cv1PINnXTLJwQAZe7ZibRxrmd9ZLKYz0z7lXhmBG7kpe5sdmPjS7Wvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_yLAFQ9jTMRRZe5j73fYnig4uzDKWH4jaSiWoZwiFtJVRid2e48LfIhqWpmVLhMjFxQUgyv544FeQF-HMPV5ZGCMs9NgdD_nPcVI02bLgeQHBGxhWT5kzeMUMEcQm9On6ywttxpOHpiTLcDg3rnQatxaAGOGF0XDQw8FPM8LMndiecaeKc6WpzErU_5x9UVDptd2yrq09iKBIFKWOxUSBt_BmkOUaJpwPBWKnAwhh-Q52BtwMDBmnhRfxIp_EDlxdezEUYrrzKOsCjHpQsbUlBGW4Zk8QvdrjdNDfbuzjG2jzuWaiJjFvJPvpftFj1Ddazr6eEhmaAxAfAJ_OryKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYuL8SP_W9vt-cTN_dsx3EGgBQWabB7iGIsUtKUaGNFWvE-A0TmKJ8dzi3A1UeKXKgp7Lk_eXuz5FEOKdao1CsB_Cb6s7J5R_GXaXO6jiynvHfL8g1Y8rIzbSvUA8aEFdNSdcErxEBCEvTQtQbDe8NrQI5nFrWWl-jjvBIVlYCDQXy3mUxGjqFVm1THWQyR9rrPKV3ejTcOX7IbT8hv2PYsVQHEoaIAxnDH-ZsHpXiLT7SR1MJ0FT-8G2OCo0gfu9EHsTSn4xolcUZocTH0-jeuAMiO7wMjgrzYB887LzmkYCc1s5zcPEmIm0UuVkWXqy69IcvoeZ1aMqQxkOCYrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0aOMn6BOV6oSl0I6ulyXCKqHDCeBQAtJOIzbBv2E22pNW5_MrKIIcF7jcWXi5oEQRuQlLc3lHK9TjY-D4pf62ZsyY5QXPnLQgyg0rKdaBUrFzTevp9Gho3_mh71HousYCmh8numBrcuKJ2vuXZWdwK4DihvzJz3juEVnP57VgCkt7W3b56bG1fXPQUg6SBna5hfrfdoHHi8-_YHybR7ZL5zpgdTSe5VVABgQRttHQXobLQ7Pu1BTmi42Nt1YxL89srAydE7kCJMzJfjl3z_aWNFSFB5DSKSvSVeHWgEveB1Nvo86q1XfqrFX6SfwuHf8XKDB-e5-AKWjmynOGubFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcIBxFb9gHiQ64cdz-eEF-1i_hokUCqlZ7uI92ArYVq1u-MczKDevNOYvGARbSTgkLJ1mHCFVEZ9u3LA7-1ATaJR-Q-ble-J83i_x_LI095yxR04lusV1XdGf79WGD46RbJvaMnUNcnSj8XsSpOcZKyslyrpMSl8dBuTpGsHR0QbtrPhUzjs3rP3syuu1qY44DK0FGzZy-cNQuaBfx8TYEpddxBiLHy-2jzjkKWzSoXjE2jub6RD4-Sd3AuEOUvm28Gdv5WlKQZqtpLiWKg_8-pf1AKa2x0sijbySU1RQczv20V5wUpaKSGPjIW7Nx8kSg9swiKuJsxbe36Voz3RnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5DL2CpnQSw7M8MpMGn0uBXeQixh6ZVzNS772-JRZWhl3U5sf44-qwM0zCPP4hY2uFK78FVAS9fahXESSTxsdSjy-Mnq4XuocFIY5kzXe429vOmNgZI-Iit-knl1Gt7chU0u0wq1-QMmLWU1VyQTVTHHYws4myv6XgrSmvLLgG3otXgUJJXrCTwSmCQVeGHD-KwUaTInbAAxVyBn3S8YC-eTDwkykdMeyExixs1MInKw08n4mL48otezCmYByTEkG8J8GQ2tCaLRQ61QunwSkn09vqAsNUaDwn7EAgg8saqgWFFF0IMo6ulc3zbMqN0AIpG005Pni3qenkSbFwnXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idI1fViXmF5MkIRJp5T7bbODwaNKq0vQSpPF4FVYN4ETTIHeRzLPFVi7Ep9eA0H_GUQKxw9yERewB_DGF6v49Zi7KppL4oV0AU1qnIiRIaBzytZzG4kde7mRF6MZLTOaIEP9c3c1_SOg7qCcGK4DFLrYfhA0TAp7QuRLi1JBO7A8SoFYv5UXrPYM7YhaApRMII9_dxEnAaYIt3rc1x9H5fRqYYgV0zKHxJSapeOzyR2UkqIOpa7EyXAVwsKZNQZgRy48f8QBN693W6oxxQBSjKg3vatkp-jk3bsbl41bsjLjH345mwealJAhTK5p5WOSymKYn193Wvya_s2fEHl16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rd0-ZIeyOHIhQSkkCmqTblxjJ1odsTSOw0FqV1ZRUurRJS7wehhLiq0lu6M0VYRIbFClFp9Z1pkoM20GzFZXvq8rschmEuceD9m2GQmFSrj3YmKZR-61xiBQS2i4xrc0xYsz-R6v33lWmkYjvekdi3uPjdmEko7a0jFS87Fpz-VOy7DcGA9O8H70A_LijnmhxvRaXPpk9H9L8D2mSmOTeVkaGVpVxgCadrL1r2LTKpqFQHUBtVlWt-FZRNIGaaUiNf-_3Gc-kVqxJyRpkrN_SYBnN88ERRsEboTsKxoIjW33bu1BjPJEi0HfoT-AQi_x77CS1Cyk3Oif4DmvGVyDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdGVVICsuwpK-InJvQ_6DiKTo1G2_wXZ-OwLRVxNL0958Gnu7xbqCvXo7rVhp7_d9Z68nDZk8lAu1DexhvfJTkmthoGYNWTJTjOtP7z6aLb86EEq6jgwE3I5JkLPviTfgfu7S0l0G9HaCSNC0btWJcgaVuUJHh49HEB3Zxwgal0QQodTvowLGvxr110jv55MElW5DzMlJMTIlsfDUWXQYWkmVUOmzlCNYEPjlMgS1WnDdBrWeRLY-hK1aYnbmkainVYI6zKMsDE1zEQJ6AklZl9_hTOXXF8KC8quAo-QxmvJ-mkZtK-dMz3o8VHeUeYok3DzEk_stima1bu8CDPgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlochXjfg3YQHSMHMsXFnEWxE0zVGI1FNsGvqJoHYf9p6l7bxAeqSoGDpy_xTUkh4AtE9ZhiXlOaOAgnTEJRcaqmz2lOWOv7wqPEaDNNQ8ng5BIH0pgXDyFpZJY-y5_ln_GXNp831_r0uf3xkvHnHG1wlKOrE5sOn1qljWa7Z3fCRHInPypqVK_4XXyLAnKFlOEENo0QqcY1m-WESAxYAgsO8MRMHsyTU0bisCk17Y6kn6qFSzphgWw8NG2eEVQwlzuDLHq-DUEhp2AldpsLYjPC5HrE3t0jybMp-WTsvEr16a60rnfIuAxmBZg0SSzqMNp9Swn16QFroxAlF6zhdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zk6FUuomm8F1uONiBgjKy-s102AxHFckyJ5mdutwP3ewH0tryRz131SSJmxfx46w2LY9vcIKtFje7Bot_jtX6IQ9HepNjcfUQicfYlhq6GNVNFLJF8DXEYtDeBt0qcnc0flphQK-cs0Y8Jb33oN-q4fM_j9p53pgIwkGsnwp8sHF3GjgEfs9I0k34LDfeVb-xtudKXWlB39t5sGgU64aiNzpessCNIvitZC-1vO7XuGYObnBbTOBHq9E6YFXLcY6iU7MyxmqY70s2C33d_AgRSpcuz3-Dhb-8KAdtk_s-ynIH6VmaILpPVESIOXKOa6u0QuCW_yqJ_mNOWamrMzVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFa0A9FeetJsV1gqLZZYBvKjDX5273wuV6BMK6wumw8SyDX7Ew88J-vorQBmr_zZaoBxvkOoY9Jo4DoNhiu7Nn2z0cT3p6U4DY5hnQmmZkIR1M5vSstKGI9JpsYZkypk0JfyBBSfh-aDHLIdrfjFUJzwMXJcsstB973TQHnfDZ7NSs0DaIHySL2Jdmr3J2jDitw_zzeXmxoEwAIaBlfxuPCcgINjkpwunRioCb0VfJc0JSG7dFEmDTT83D_mklj3ZSIlCiweUqAXTQxIk1XaOjhsiWJ5dlQ8Y1YrKcPHps_ceX3xEZcDDhUcjtPpTJyYgdjb1P4NvTBanWVq49FKPojU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFa0A9FeetJsV1gqLZZYBvKjDX5273wuV6BMK6wumw8SyDX7Ew88J-vorQBmr_zZaoBxvkOoY9Jo4DoNhiu7Nn2z0cT3p6U4DY5hnQmmZkIR1M5vSstKGI9JpsYZkypk0JfyBBSfh-aDHLIdrfjFUJzwMXJcsstB973TQHnfDZ7NSs0DaIHySL2Jdmr3J2jDitw_zzeXmxoEwAIaBlfxuPCcgINjkpwunRioCb0VfJc0JSG7dFEmDTT83D_mklj3ZSIlCiweUqAXTQxIk1XaOjhsiWJ5dlQ8Y1YrKcPHps_ceX3xEZcDDhUcjtPpTJyYgdjb1P4NvTBanWVq49FKPojU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h67Gz6p0bD14eGixBp20SCWNa_mkVHcqQIqMBfKXiC5B2iuE5_nm-EcU0I0e28peUUXGbnlJQqjlylM8xq0PJWt-fkuGpIV4Lli5n5ehxF0lcTCb4ibES4_FVcTYNjvxgjemWE7lxLjuEtiS0vBYAg9kgMkyfsKFeLnz3yIlyH554kTpUefVqV2_7MUBNgAGrOpqobsdx9tKixSBR4pWnccg3mJB2Cq5H_9_Wo8HfLjygv2v8956abVe9eggzt7MK9sn5FI59b9mCijmWnH8qomwMqsjBOlLHSKWxt-4G5rAjD9CEe9mjenbF1lHqQXiliN09NP6e7GQ7w-029eVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9HxKcGOBk0ePWYOFV8lpy1IwmS60XQm_g1M3thc1n1rXhEnC-L_bCc27ep7lTuHsr6fZeD4UXgOMMxsvvZosY6IODd5lHkrJOxfsUDKzx8uN1omS668iup0_h1ZL71hrLx-1FOZzyCzKfDmA1d5Ik2X5vIkVfF95I_GnV6QD84E_M4woMIRztkLGyUSbQ0U5vz7TNXGrwGOmEsosOim-Ykju7UrHm6ScaMbT2eIkZn83MigGSio09z9EhmJMGyYKLaKhmQJfuBbSdiXs5dBV2AmEyCZlDG_H0XpjwKV76yFjOwF9rQ_XjgpBwYllyJgPAN0ZjO4BspvPrtQ5cX33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyXFG515rWCm4RP-bXWwW8yYi0QCeBoPVK9H67L1l8sXvXRhLTWrS1w9otJYvm6BZsX0NN5Yy3aHIjCyKnhoFAkoNWhkcbWdnLqlE_Gv8E0c4g0ofB94RyUbJ_22K0KcBAEynJZkwMCy9R6VvlOPiy8MaHRQOhm35BCsVQRw-R8J91EPkLrA8fW28qfUJx4o7vpuWc8JDNUTSkukTtOaOBLrU4J9gBmPFF_PgzS87mFjqCnSNxGlAW9aQWRFc0UKo10bdKiB3yBXCQHzwllkmFongneYjFkTqv6FinpahZTB5JIc799aTsJOQxOEvkMrukm8CKQ0I8YjihEWby0JHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1GNjg5uTK8Pse7Hd1TBxTWk72Oj6Lt783MmDn7sbStSASS7NU1ybhcfsp3QdSYMDCW-ndpsEYiktZdQur7_6dlJwtu_dcK_j4U0wCYrGmhFSMwM56fw4fJMg241jot6nIXvZsmzeNthWVNFDQ2U22ZzRYvDpyOHRk8f1a9vam5YY6-8lOKBJhmCnMfwcfq6ea4zxtvFz6wwbkpcalOd27SQXDahtSAvI1Iv4wykdgRD7lD1n-CtKAKdUGZdPOINmu9vg_MTq-6VkZ7L6xjWtrMiKABPwKi5KUcJP-OJbnDFR550uuVxQQjkDShs_8iLJs64hv6jDpHaq5tHkyvaWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZjZybrr86qp52Z5ctl4AMzFm6EizvQWK6F5E3va9jitCgRzRT65DacvxL0hZvGcrbaMPH2iJwU_tgKWPiYwQMnE60tM182jsYvDBjfmMANtyWTiiTLhUi-kA8jxPubsaiYSIepFQu51t1OIny0bhDNQPwB30pbalmExlEuSGS1I7LwpCLlJbzYbb665vj2MTIH28OXhxHHFIzDgHOaB59EPVn-E5AmtHUFHGU07CS10ZAhhte_aAJ94p-q1ddmtuj6Pm-TsrH_J1d7_4DSjU8_XQc6_XCludMnysqmCU5aMGcqj0RijN0VHihyQO8UTBFIlHQwGP8M6JKNNFEnpqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYsYQEj-8FDZBNcMsFYqfVi9qE39ywJp8vY542ZuJDjnsY1x2k114kPL4hXDaHGa7ipsahhxdUo5GL2RfrlQAwYAE5qPZAETJwnprgau9UNXH7Ucwr8EK1rvjqIVop40e_PdHsM73p5QZCoCuJz3EQQoowZQWL79s9OrMpPwIKjiPXwz5RHvbBc79LorGYcWAY1_QzOHYmRQMZtziq4XPX4cTwOgUFcuqGjVBvqK3NUno-o438hdXlucsCLbznIwAex59BZeTd4C6kLpgovZFTyIz1DTDRoLrgo7VVuIaHzK7spz4Y6mopnLXZGSoLtb-d7GAsNMGKs1OrifyI2IEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtLOf1_xmY-nkrBCSYVfkrd0q7kGLGupI9DFv6t6jWpVNM-zn5kLA2g8OXAagwAYnxCRE_IqZKCIopU-YNLcqWUP9EFehmMcQoqBBDZL-hY6bVrEGU27VM94Kk6p4GNt74dgQD7GqQYnVI3qEmb1A7Mzw7YoUIRwprQRUJ_SBNimxI-MNUDGaK9HinK7eshlqdyDE6rdcsS4MX2zKtVATrgmhaBU1dTZYM4V91BGKJ2jDxJ5toiaThK8z-QcFiTXIBfOrb5z5VdW47jtrZR3--XXjee1Jgpd7kqgJW-_xTu8YhR8t9_tGaGgFK32Oc3g41C9r6yWVgpzLXaXqS2crA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvpUqp2g8JJV_1M4LkEKxcUuoCAnkPYslCgkQVy2mXp3R9eRJ-mPh4WA3t_ZIrkCSH3thPYlXdJeZBpMXf_170Uwj_x2Fm-Z4mMh9wYk2M5BgZuQiwPPXs3xUy6rzDbNNimZpRoF7nzcDrTVGF_YWvOVQ6ljHNb5Z6blqiCLeJ_TuODO4S7IiFm4q4kq6ap_qd-p-2DFdmN273VL0O6rCT762eetMyZnodT1N-j4wJVgD8MvdnCWvbOdLFQ66HPwpUuP1COoZ69j-ifaGc5G-XvBDVDMkzT2lCqIq9nkRS3KVyMy63CD_AxTmOvJSNRpXd899raRxIYDmSVfEtmRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_MAPFHMsC1jh606efTULoG7I1uehskW9-RyiSKFK5fJVxmfIYXFkAFJ0dxLMELn9Ii_nuB4BeSnto2RagKJk4YzYId1V6Cy5WSZBFdVb5TL_MPHixBbk2f5HIhIqN9ZtqRhp5oFul9el1SYq9jJ9Lx0tNxwH9guThLkM5O7qZhhAwOMqtvn-oJYPjkbIafzBJJNGKcgjPIQyBCun20OJFySlShmiJZ2vAvp72HBP23LziUCgbAG9NH8dFZOidMetbTk7eGodX-pFEfoK0NnVymJesXseUE5KDdAiMZmnN-erDY5l3-gjzPZscro3r0IdQxns7D4ysvRQBt6Edafgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7uTCEyK06ix2mGKJp_WsPiQmoX-CueS5kV39Jv7nQHmyVjleiTRsulgrwNprzzRIcHoVK3poFkJ_K2PNOfVaijFshqfAv3p8JWBNXkyiKnoNaUMC8CjoNG_tCalmBWAmrnQowGT2gnGGhsTkMj_MkD_tqDWnjM6bGH_USrNZZn4YiGk3o3y71sVge11fArcF7FBEoSETOqgKwFqP090HOovS0VlFE4R09_roSii0SU3zwxNqAbuNJ8-CkbPKn9aVSEVOb3K7giJfGw9g31dGqZSJ9ldiigpiQEJbFnyynaJkaHY-yA3POT1IMFjzd9G6J1zyDvPAcnwvn4xIiSOaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpARjlSrbFz1TP22urcppiL9u2ZjplemldCBHhNB-l7fW35tWiRpciLLHqILmlT6Emv7U636kIwTmMkxEhFhRcT8cpD2KObd7O597NSv4h4lc59R80O9CNBdUcV4c1BZ8P6Z74sx2ts9oZ31qJ3Tp45gS9Tzngecg-pF2fc5HLyIiSlC8sSc4UijowEMVV8A3ntesKF8oLoaFNXxZ1ayOAZom37jCcPOb0ypaQnRkhnmEO5iTaRWnDfuLAgZ-s2oekm9MPf1dojUcdddAEgRWbT3V7PtRkUKrobVKO1GvSSJsJ3rvUst-zfHmpzkGhddvJtlQbRGhzsL-_dHLlcpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=mn-6IK0K9MZiU8YJRi2oTQJuqMnpL5eXNzpIm4fYmkWBwE6WMB_SKb9w56MdywWFhiH5VBnxh-uEPmPwsOfKJ1Og-qy18C5dwq5kAYlA2i6XUsqabEfjcgACEJ3oJ9zveCc02_6tJehXfmzXT2Ibj1PSw8ZWHoOgGDSYKChUKuYtNFvZgEzFklrBFDo9jSwCyFZ0lHpUu9AMme-uUKSC8IriGjove7VsVOg3QpopbSKAAUqNY6zDvzUwVJ7cCWmbyjKYkzs5a1RMG3FCrWeua7nSpUYgIMfQO_eEHA3r3EQaQiXkjGyIPeS7g9PcD8d9sT-1WdnpkkSVBRI-OmnAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=mn-6IK0K9MZiU8YJRi2oTQJuqMnpL5eXNzpIm4fYmkWBwE6WMB_SKb9w56MdywWFhiH5VBnxh-uEPmPwsOfKJ1Og-qy18C5dwq5kAYlA2i6XUsqabEfjcgACEJ3oJ9zveCc02_6tJehXfmzXT2Ibj1PSw8ZWHoOgGDSYKChUKuYtNFvZgEzFklrBFDo9jSwCyFZ0lHpUu9AMme-uUKSC8IriGjove7VsVOg3QpopbSKAAUqNY6zDvzUwVJ7cCWmbyjKYkzs5a1RMG3FCrWeua7nSpUYgIMfQO_eEHA3r3EQaQiXkjGyIPeS7g9PcD8d9sT-1WdnpkkSVBRI-OmnAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBURjjLb2BQ2T2FArH-trdQC97Voupk38IhZmr8stFNYZswC7bmFhtAIdQlNcAL9huu6hcpyYazp90BMB0aIuVyTlROiXqIVxaqxlDeAu2V5Rvy3fMk3cxwlwG7eI0eO_AeDzePcvt6JbgqHVHR6C0nsaqtfxSNghGPW7EpfGFPNOV-18bEHFD9_8Voq82ocG0VqiGJVXQmna3ZvoB9gbcZ74kfuHXjFy9GhRXnWPuHsH8PsCq3Yb14a5f-l1r9UUsw2ldBnCVuPl-Wi543jL153SH40FddbpkW2uDxffP6qEQt9B41ZVa7wI1iiqD3v7zzVjZqekIlAV9BYZB7p8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiYnUSbqtaQQ8frV5orbI7wwiyDhrk65OI1nhTveGt_2oY0e35-RO6EzuGZ1iIQRqVx6HsbknLj6Bu3vSx3bE-UiFdVFFsDoWiqwvkmoOW63gvKrOjm3BgzDXwacvD60LnJcNtrIMmeoX7Klfc3uz74lyG8tRQilM7t_2yDYLEnVCp9AujSPjEZEq165sr1gCRW9QLOfhNnY7jtPZ6IDftr47ElqwsVVw1mu5N8ItvNl0nDTXgk72vt5nIy5j2bvUkNj_KTUK8z2S30hE8E_wDVaL7G0iJD4_GxfhnxCeEO7T9feVDL_n02jA5OyTvgNUE2c7wS9eawvb_uhcNaZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqQrEm_eRDH2EjhG18MkbRTwnHyX17Ve3dwUmjaW2CPc92K5fUYrXk2IoJDIuROIwsrdr5LvihgpRWveoknEyyS4iERepKzZAYimwQLOpidDJfPr2Q64Tj1T4kPL24PNvUT4IvlIdqym_o1i4PM1OdeGdcR4n8XyG-N4O4YXTf-BEX2K3MTlK017nRgQ8k8xb7K0ZY7UxnZthj2vvqtGUl7Kt2b3aX3vpUp41fYPl2JbEvgWM6SLJzQv_Ws2Gax7AFWrOemmeaagtQAM6eXAj9_TP6oeD0FO1PZp3Qkrwpr2uK5Vz5JmCZ2983qAmZplt8keUHgOOR8BqyyBnOKYxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf_N0Q7zeAATn6GSqlsOUW1jed20zfgPBltss_277kKSWIj1w1NAoaLVa6E5bJ90DjGnKiY1yt7oThroI0y5UouzXSKs-qMbVmwVplKvV2713noA-y9wv9G2VUmJQ3jwm2ZRrjvSOH1ehM5BDd1Vs9RgL5TW81hfpLCMCm8S1jNJRTIKg-MaeJ_UO5khXTuWOClyREbigjZF7e2PmAC_x9gUGEJQ3ce3L89Wv8UH90lpIJs8UOH1Gpg_mtMaFDiMqeYNqkuZdxmBvlEjfdA03_YyOTwkUx8z-2FDVFtrZ8qYZzpOXWtA0LZ_SXepLjMFpXje2l9LIa4474vzjt7mhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyFv-ZaDLCnsCEanGlofzVNqmqrnLm1uVCmcYHt13x80qtW9S1Vh_AvQspop2z2SBB_9GIqFzaNQIVvhor-SfUP5iHJuLgsFeOoSzLrr23QO3Kdbk-pn2_2CIur-pys08mdmRgle4DE3b5khQUjONxlHzjqdy84zFCI6ZutUmvPjrF1nsVTs6J7u-FWhJWwdpAjZgspD3rOxaodlUKDSmdOte_fdBotYZrMd0P5CRPGn3sA1D2F5yT_dzAHePqBySk0p7xTUlZHxzQbzRU91brTiNTVWt3he7lwFx9iBFwW9UpPfyUg2rLes3b2tqYKmply0QjrHqTJnYRv5zjW4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfhzVv8TZYYA9hdN0SZqI_hKOudGcCmL2KlRmIA66asZ4wVga3h3m4BT0TG_6at5aL4GjsSA6ptrWVi08XB02CCVa__yo5h2lNf4kDV1EMX0UAsrLEs_aGq1VdENrbGbN6T7F9DjQJNpRe3eGGRnWxxWnR_POdBPgmnsEFCwyIYhGuPj6j7XANHZmNQEwzbMqD9syCHZ3YhXnDtocZI6OidL4uGb2Fp5xMIWuR7vVpAXMky9-uClIaKjhAQqtelgHElihZTvWBesx_PMnDhanxFaWosyezL5p6uN5JVKD1KZr7DaklQwMYlZXekTi2zNlTdm-0JXo2hmP8ICiBzUIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTOOiOaLQULq56yCA55hX6GTE_I5gN2p9e4motmu7OsaHExUdgasTwVGtKXv8nY86s3wqRtQvcUtJ9xX7awfr21_S6RWwsQLcP9MzeoRig4LLTyxbgQ_TlgvhJgIGQBk8lMiLjPyVQYExMQb7hIlmhEMDTMQjDYozkDIve1a3HKYv8rvXUqW7gxf80Kxiu0r_FGYDz7EONiLky3CIVvFYHEU61-IhOa63yStelNba91337KI2qZ9qOhBmoJ-cb0bBQ8UuxVggADYCRydA3aIfXf8JKi6N4rUmdlmNwJFFTfZakM2ssXh-zy63Q_2Cb-IxX6IPtcPcSeAb7s9hWmnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=Z04GaK8NdnKqV7o1V1lqMqeNusUlYj_msOgPywzeCmbYjDsa1-r8DReUWdUzGrMLMrCKC78OLQtpvbFzeET4ggTjwHybB7uGD5O3Swg-tgBCx3fLO-lasey2zyj7vGEKvbg0kvNCZWa9cR_dJD7KaECz7wCYabirF68TDLFF84l_IIYvGrdVxxpRngqhfraJZGm5oAWueE_-SJp5a3Rhz-XyU_nMfK7uURyaU0WaJoNPhqHL-d4dBvsWVVps_AqCvnTgjX30u7FvXq1jBLQuJeCmWJQjBEX8ASNytrf02xOEbADZTAUFDwz_V_6prbnkw81XKw6rEqhUfoM_22gnfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=Z04GaK8NdnKqV7o1V1lqMqeNusUlYj_msOgPywzeCmbYjDsa1-r8DReUWdUzGrMLMrCKC78OLQtpvbFzeET4ggTjwHybB7uGD5O3Swg-tgBCx3fLO-lasey2zyj7vGEKvbg0kvNCZWa9cR_dJD7KaECz7wCYabirF68TDLFF84l_IIYvGrdVxxpRngqhfraJZGm5oAWueE_-SJp5a3Rhz-XyU_nMfK7uURyaU0WaJoNPhqHL-d4dBvsWVVps_AqCvnTgjX30u7FvXq1jBLQuJeCmWJQjBEX8ASNytrf02xOEbADZTAUFDwz_V_6prbnkw81XKw6rEqhUfoM_22gnfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuhSn_TZZKUw-IsJ-S6SIKFhnjSVkeAICTEs7AkZstK1gOODCx7ml8Xp-gGHYNQoRj4ZwQVR4nQuNs4aku6e-LIJFDy-8Qpl9AsT0cH5t5nhDHQRHkwUBVIjKAzaOk-sicPptc2jzVo1XloiVjW73zV7OQLd3kPEcRA4EDgVuQTjbs9FPzp-hLQKJ0IXKx-iN4jXOkJO6rulw61oQ1SxmSrqIOxl7uvtV5UBy9QT_4tOl763OFyl_bxUvK9NpcrztuS1Pp8W5AFsojm5KjjD8uwUqgXo-M_8tljlxT0yGPQrsXqx6YRp2JTZTlNDSc5j36i6u3Sg9SFDip619iJB8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV59ZUjibRZnRGSUPtrTXG283Zdy_2X8DJ3CvEEOp0bzIvz8Uvwlycy8d9l-xkeLNlkq7qQ90wau29qwQ3XAKtCNxj-uAWabTvlFCdFXORbu2aRqFZj08mItwF283XaEW3dYv2PZPgUZvxWPL1e4WUwo90qzOc-FTDqmNrTmXbapgUkTgoUfW3EyoHFgrTgG8hztQjFf-czZTTWUzJL_p_onW1d9XO7Hi33WgShuTw5m48B9qeRXdgT5BuxQcy7ICz_9O8FG_aVboR95M5EK5D7fO5gkjass6KdYxjSO6Eaa_OhLxJXvByHXz-zpnqihkekR2zxInB0QzPyNJwIKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfZu65cBWBOMr41NO37P51ZebrmjygVtOhJ5gkS2kY6UsvBOx6NUURGblGZvj2iRWBW01q1bU1_KZuP6fAn1E44WCe9gZ3-3Jc_p27dveYM0sd7KHBbyiDnrd1Ax_dkfJGyjdtWt0AwKQoOsL1uChcgZgFras9YQo-qt3ZnbV1L-UJXxLz3leq6VR_7R0Fat7hr2R48KRy4jdsLHgYrnT7sZfUR1wYyLWHli5yLuTVHkdhkUfT2lf0odb8c3QUetDbg4GODr9OnfIxhB3EtBGC3nJ53mZaDcxEYDLcJ0AAOWSvWKkYeRF6N4hivWfbxSrNmSmujUYal5JJ1cSYLTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6cquC6u2nH1jH2j48LRYfkHP2F9UHzyNpbGKdYnRLxocueCnwvMMLo20lYrNPhKYd96gzwrCIyQ5P8UmX7b_p6ZRJl8F4T9znVD942uztL3Hr-qCRoTXFd3vhFvYBICu3EHQ__uCGMGQzX4S_djumr-cbxhf_aYxJbbJqFN3oEpeX5iF8k5ewoCE1jd-11fmSKoVlU470GVg3J0vwisG7erjUiqD9EP_RRZEjpz_8pLAK5_ROZpZAg2LbaF3KBFEYRO20yRIEMvhnEKXJ2twmEEj-KY7HHQJZOsfyhxMfXgbg4AZWPl_0uzt3Jq0G1phcnwP7I2PsXHimqbQ_PY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JytOSiBR9aCbdWkyBndZn8uevqd0j0Z4t6_Sst0oC1tEtt8exh7oASf-k09w6UwG7rwsXan1Z7URaJ37SGQDRQl2bhj-eltC7cEkWYiWjqTjVHnHpgRqskDGXyfTBSSLDpnDIoUFev47H5Kf2rOsEK9tVxxYrjlWpZnQ_MCyf_UaBMtHWEqQtmVLYauXA57iyt_KM7siwoStRuYkJH6aE2mfu9KB9yXmpehnINV0pEO9cgdcQLH-Hb31nEb3p3NljDZ5HjcFe7BsIlvIdJw8H_wP1PyrLnEcNlw_WJW2SzFoU710K6euRtekOeIwOguYDK7SsX0cNmjEXO6O6zlotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn12vVNVWVIVH9nSfdikItEkCvwu8w0IVKDsLJjgKXZL1MHExLAr1APr5_X0UwUYw5B6u6bzjSJf2If-0meio0Poz_iVe5vgdfbPKLnk7Ao6amOxXvkfnLSVNS8VBvVaVEq-DvSECLGRJ1TBRgq7rzEURrSDt_oAtUFaNcT4L1dyrm72gtnXGoDymSHAIeCzLMTZPz4RTeuTBZ5fReCBot58oAraxSnu1290R9m9Qhiw7voiHIZGZqE6CEjrGYhWGPo623fW-AJpfumDJw80yzWrhRsYXHwS894F95dgQgRBAw8XRcOWVctWzJS1j2hGnJk1JGI_t_q3Ik3jYdQ9fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St3YXHPW90ORV7AXyyQeCvpRuX8cSjn7szjCgJeP5QyNTs8b1LDGzp2U9-TlkydQ67OJrDqXpiRLlnuZ7j6EwsPAZFhRqv8K7nlllvJUX4nqrACFVh69plwajq-4Ge2UbiSgDJN2WDHPVMb28ja9PKN5oIsR7sJQp2qwwRdQOvKVtpk3yr9cL-nIsVPf95EcXYDSXRcB98heW-e1NonAswjewwwhK7zuo1UYanFHDL_0tuxGDy_ZQ12ve9YFLuwEr2no80kXRVoESBMKiGeCz3mSlIAmM43ubrTLq5UGUa0hiPM5QLeqxXHbdBhAIgvKrXmuMdPAWqCLzNHazj0Olg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzrOS0wcyKIROB1Q9kLObl-REcTOPUPyv5mevhkTJf3_2oq6JTD-dYgD8CFCQ61mA2pjYDDR7dHMGTmXJRXRbbRnRQFlYUIfxhjiWVm0235c-bY4Btn7N-VVtX0Oo2mAGsQn5qoIdtzw-019HuTK_RkGeONAXTSBb10D_iXy6yNeauaOi2VLqh1Fn6L1c1omuURZxwJEYX3_8i4fjFNz0QIDSrPPBwsi8UrOLY3ua3d3oH7RzLzhMxtR_kkyqrU91UI6wSpYgXCswpVQ7YNt73muXcgf_xv7re3y7OVFkiyoXnWBRa1tBAVQUauw1Xt1oEXPanwSRKTse_iA-QCbKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYYJJiqRR5LcCvjU8tvIyUbEr8mzx3dp4rD_DnX_bVSCXewxfF3opLIR5uZyvFmkrCUW1KN3iihXsf_bYZJGwWiX7mwOcY1oAQd4mqBmbjF5NP1Cc1Ov_yoaZ-JiCsFod6bb5zNNHsCsm0qdJOvHji47p8JYxfh7WoD2l3t9UaU9yVHtGxaGSblBvP8BrvTFEuo7xmBdt-BJIQcL5_XxpdfYeoLtpGw0sAvPiZrfOWK1QPdV7tu9sMW-b0kPYDnTUuJ60yGLgkfdwoaHGk1FYgJWXBGmFTKGmHA2f_0UEc4JH5F_WJaMuXpe7u6RZaPnRyeSBQWJT4hOPV-wt7E2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1g55sSO72FJCyYybtpPo5-mvGdoxXx9NOvSSUDo9WzocfEuO6z9nrPCM6BDe8Wdfp_SC5pL7Xz5K-VNC7AfDLinMv1HW2sLzXqZxSkhagFwK0AmTxX_uQ-xyRsqn2eQjNPailGn2G1k8La9ZbKIUIBmbmAvrgfPkOOYQLjkoqMUK8DII3KIyJC5MWKySRxNXeTPckgBRKr6I8eEHXvb5r5q9HODTwBazgiRnaAs7NhIuHw19brELtlTQfUwZUPezZxhfXSU1EsRfDarRC441JPkYPRC5S-JX3qMdcXDvsPCS9Z16DrUiBPSHVmKEAT0XkGF1wyvEIZmayWowv3Zzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
