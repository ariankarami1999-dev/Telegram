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
<img src="https://cdn4.telesco.pe/file/J5wUx1ecuigg8FHemIEK4JBpFcDnOGFT1VXwFPSLUZ9_rPlcWhO_KfWxZPvS9GXGuyP6pmJQQHRiccnzfyCYKiAPIVfyNWV7p0I8tNO7UB7zQVgaOE8FpBKoCCEIC9wLdgAva5I_zco1z0-k1lz2_tYTr8r1dYGUtnS2nbyKxbYAz-7zgsVIYHx1cMInLbQLEYiMXc_vWypdJMm77pbyMfFMf1sGc0nJedyiRwCifykBPrJGAE5AzyqPBbigQSyjmyRjpBWefuznKuxVam194w-Ye9HOMGIsXFDmggUm4UmaRJKHtza6qTnP5MGwjh0XDI679OJK6EKsRamdv9xSjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 939K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 13:09:54</div>
<hr>

<div class="tg-post" id="msg-131587">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=ib3kuZF7u5odnh210UXIQelfnSAHoWPGMmVFHnrGLZWwENKpUlaFdflyju3HWByNu0Xhh3PgFkCRVYmGUmNhM-11RQcmGcg6EJeUoaYfQkPrkAnILDoMe0XNOLWTh6wMmrytSZJQcug6szB7nNYOVjWMBssDkAH2tNYs6OdDGU-Y8_iB8dZjkkMHaeH2WVp_znN_zEO9W10Xr8MS0f2x_i6IqzlQ09eS0SJDb-eUS8FC2rdn3ajd0CGYDVj61gL72QINUqnBHrAB_nAzgn_kbM5sepXvgGl6A8QpBzmMG1Kz056HYm7S9vKfEbhfFM5yoJqb3SBosLJKHtvKObMx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=ib3kuZF7u5odnh210UXIQelfnSAHoWPGMmVFHnrGLZWwENKpUlaFdflyju3HWByNu0Xhh3PgFkCRVYmGUmNhM-11RQcmGcg6EJeUoaYfQkPrkAnILDoMe0XNOLWTh6wMmrytSZJQcug6szB7nNYOVjWMBssDkAH2tNYs6OdDGU-Y8_iB8dZjkkMHaeH2WVp_znN_zEO9W10Xr8MS0f2x_i6IqzlQ09eS0SJDb-eUS8FC2rdn3ajd0CGYDVj61gL72QINUqnBHrAB_nAzgn_kbM5sepXvgGl6A8QpBzmMG1Kz056HYm7S9vKfEbhfFM5yoJqb3SBosLJKHtvKObMx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
دیدار رئیس‌جمهور گرجستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/alonews/131587" target="_blank">📅 13:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131585">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت آحرونوت: انتظار می‌رود «اسرائیل» برای مدت طولانی در منطقهٔ امنیتی باقی بماند و این منطقه همچنان یک میدان نبرد فعال باشد؛ اما این بار با اجازه و موافقت دولت لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/131585" target="_blank">📅 12:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131584">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
شرکت آمازون سرانجام به تعداد ماهواره کافی برای راه‌اندازی سرویس اینترنت ماهواره‌ای خود موسوم به لئو(Leo) رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/131584" target="_blank">📅 12:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131583">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
گروسی: درخواست دسترسی به تاسیاست هسته‌ای ایران را ارائه داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/131583" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131582">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
تکلیف امتحانات نهایی دانش‌آموزان مشخص شد
🔴
رییس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، با تأکید بر اینکه برنامه امتحانات نهایی و کنکور با هماهنگی کامل سازمان سنجش آموزش کشور تدوین شده است، گفت: امتحانات نهایی پایه دوازدهم از ۲۱ تیرماه آغاز شده و تا ۱۲ مردادماه ادامه خواهد داشت. همچنین امتحانات پایه یازدهم از ۲۲ تیرماه آغاز می‌شود و تا ۵ مردادماه ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/131582" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131581">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBlioKFXI4dkqilQnKCf2zInwudWVo92Zr3LSGJLVdc_r13vnFlYyEw7XPRJVhYngEVV3wfBGCYurQiO6D3bN3qeKRpk8L9ZLZU6EjX2CXn_kg94GYn4hz7DlMaJPosPQmon5b8ZHrWXM9oV318JXajfeOH9mzomcv3NB4sV8nEjbA-t2estsA-lq-vbfZFXcb-Z_V8bic4nBd2bznwUrC71n--_vQM2bfrhhOxbMcDR_Rd0FdbM7rW8Z7WghBCFRT6uRhFTQDehWC8v3FI_HHFiTdkpE4Q9GlyFB0BLiI3xegpU3sOPKxBE_nxsTr88V1aiIP5OYm2vRjE_JIJ_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
15 سال پیش در چنین روزی؛ احمدی‌نژاد: به هر خانواده ۱۰۰۰ متر زمین می‌دهیم
🔴
مردم بروند ۱۰۰ مترش را خانه بسازند و در بقیه زمین فضای سبز درست کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/131581" target="_blank">📅 12:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131580">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ab2ff613.mp4?token=kNihjiINQy4oP4ibiNIRFdUWkBadHcPVBm7IwvK3SgOGvZ9TxCBaXIQn7pOZO0wJP-GWzU3_OrpRY6j9UptAzAQE8xlAio3p4HTfsAxuyklv-y_QKCwKmbrDevEtYm3CIKB68pDSp59j8borHTJ4rLS5QCEXnd-zEWtxcDMMesjZfDMZPNlcfO4X8xReh-5zT0WZKrzS6wKWJvEmrAPSrAvu7tI25OZuTMa-32LY1QGLa_PJBiD3MCnPZDmJJtIRoCpML_g7pN82Hbu3e4o2JyQ0YnxHmDn6gVkul-zEs0YRcXccN97GJRRP3uxu5DqnWpU4YgBudP1-joAWP851SjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ab2ff613.mp4?token=kNihjiINQy4oP4ibiNIRFdUWkBadHcPVBm7IwvK3SgOGvZ9TxCBaXIQn7pOZO0wJP-GWzU3_OrpRY6j9UptAzAQE8xlAio3p4HTfsAxuyklv-y_QKCwKmbrDevEtYm3CIKB68pDSp59j8borHTJ4rLS5QCEXnd-zEWtxcDMMesjZfDMZPNlcfO4X8xReh-5zT0WZKrzS6wKWJvEmrAPSrAvu7tI25OZuTMa-32LY1QGLa_PJBiD3MCnPZDmJJtIRoCpML_g7pN82Hbu3e4o2JyQ0YnxHmDn6gVkul-zEs0YRcXccN97GJRRP3uxu5DqnWpU4YgBudP1-joAWP851SjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس‌جمهور عراق با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/131580" target="_blank">📅 12:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131579">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
قالیباف: آمریکا و اسرائیل به تعهدات خود عمل نکنند، اقدامات متناسب خود را از سر میگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/131579" target="_blank">📅 12:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131578">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f39132db.mp4?token=vVPl7dowVH6y_CuYf3e8hHTAqBuYdMZaGZENNHS4Y0J6k32vr7vlkwjnrqx_JsKXY5Y-6kYd48l6uC2WM3sGZtDVnjZfwddT6GpslIM4dPGoRFlWnuX6IKsFDr-YFINbwt9n6elIdt3fdHu3SlBELaN8KuPZqt9GmzwmUhsVcazYnSckxO_VdFIjonYW63U8kpcH7F9fFvYvJiV9Z8gRguVnijsP6dQHrOzDEWj62RIaxufV-mUx0nLa-g7bUJd2xqd-_SpatI9VZgYqkfjI95Xc1AgOhgx_Pc89s7Pal0yrqXhpOqx9e3s7V5iuiZ6wLQtWGElSF24T53JXwmUdmpPTWpw2GpE6a_Sx174mkIpr3vMtwgMTNaPaht_CutQ2qROVau2sBVfy5k4LhyC-KIVjd6qnIxHtk1uSO_9mv4RgjvswrJncpJ_-NejmyChMyMoXUABIwl4JoTNBFSxdV7bKimmvfIUs8UGdImPkaW8DHT17rzvPy9LnE_yTMU8_Aq7QM_QERumztwiFm6tEo2TlwDPJmtCeHGYEGsoDQdoRUmQUm3dk9OY56KmHxXZmpqSM-1uZ6c9BFfuoOd1K5BZKg9Qbg_wXF4FdG70F0fAXzwcXRSnGY_cyvY06d3RyivAjPzOpQ0Drc55o91AgPfvErr0mSdzaO7YgDzOhRww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f39132db.mp4?token=vVPl7dowVH6y_CuYf3e8hHTAqBuYdMZaGZENNHS4Y0J6k32vr7vlkwjnrqx_JsKXY5Y-6kYd48l6uC2WM3sGZtDVnjZfwddT6GpslIM4dPGoRFlWnuX6IKsFDr-YFINbwt9n6elIdt3fdHu3SlBELaN8KuPZqt9GmzwmUhsVcazYnSckxO_VdFIjonYW63U8kpcH7F9fFvYvJiV9Z8gRguVnijsP6dQHrOzDEWj62RIaxufV-mUx0nLa-g7bUJd2xqd-_SpatI9VZgYqkfjI95Xc1AgOhgx_Pc89s7Pal0yrqXhpOqx9e3s7V5iuiZ6wLQtWGElSF24T53JXwmUdmpPTWpw2GpE6a_Sx174mkIpr3vMtwgMTNaPaht_CutQ2qROVau2sBVfy5k4LhyC-KIVjd6qnIxHtk1uSO_9mv4RgjvswrJncpJ_-NejmyChMyMoXUABIwl4JoTNBFSxdV7bKimmvfIUs8UGdImPkaW8DHT17rzvPy9LnE_yTMU8_Aq7QM_QERumztwiFm6tEo2TlwDPJmtCeHGYEGsoDQdoRUmQUm3dk9OY56KmHxXZmpqSM-1uZ6c9BFfuoOd1K5BZKg9Qbg_wXF4FdG70F0fAXzwcXRSnGY_cyvY06d3RyivAjPzOpQ0Drc55o91AgPfvErr0mSdzaO7YgDzOhRww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس‌جمهور تاجیکستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/131578" target="_blank">📅 12:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131577">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رئیس مجلس عراق با قالیباف دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/131577" target="_blank">📅 11:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131576">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbWnqaYBMVSKevkEG4HEH4gjYdIa738xvqZ4e0WV8Psm2pEWKQhHQwlg9IkS3lFMvkDdRD-x-Tz73Dp6E1DshCQ1-nxAJ9BNLeN5LBSd0t1DR8Wo7tr94n9PUgwCfCshWcyjcX-KVYSElU1UNGBxROAOX1CsrQwKImKbe8vRt3fSf_BmVKBg33Tm1h8B5LmUJ9kzF_nH74CX8XxPL8eG7Zu3Kua821v9dI0jF0yAXiaWuUGEln0syTRVNiXoqGR_AAWWBXvyZXSikNXqGIVkgCiMpn6GxL0T6aYUexrETh4hVtZAWU4OavtuQ_2I22s1woc0-pyT2OLicIOMOFNiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس حوزه انرژی: با روند فعلی تنگه هرمز، آمریکا به زودی عوارض می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/131576" target="_blank">📅 11:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131575">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس سازمان هواپیمایی کشوری: فضای هوایی تهران دوشنبه به طور کامل بسته خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/131575" target="_blank">📅 11:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131574">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیرجهاد کشاورزی: هیچ الزامی برای خرید کالاهای اساسی از آمریکا وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/131574" target="_blank">📅 11:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131573">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سپاه : «خطای محاسباتی دشمن با پاسخی کوبنده‌تر از همیشه مواجه خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131573" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131572">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojQGOnkElcQRbrmVWvcm3UAtV18XS644iKUD3Rf6XXt1bGB_rksC0nmxbHV_ljURS_1zWQRbYY6mN9abMP4AoZJWa9UA9qLdF1maI7JsLoIQIC8eUFsXH6Euilg5yRqVFIzXwouZrPlVm5l4N6wCtxH-b8jv3YMa6IksW7uJl0Qq3DnSAX_KyHEV-RlS8wKw0P1ORdYw9cKqW6K7BV-Cv4QHGY9wurl45jcRDFdDN-Tm0HRbbSRuNusgP8c0UbzAlkB3SgWM7-IuQlNB6AasAOG7RTlbJUbGLMweDjq1qogFQSF9xw24wIdsz9kahNJxm6eeYD93ctor8EWyEO5C-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از پل ارتباطی دو استان کرمانشاه و کردستان معروف به پل بین دو بهشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131572" target="_blank">📅 11:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131571">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی اتحادیه جایگاه‌داران سوخت: برای تسهیل سوخت‌گیری، تعداد کارت‌های سوخت جایگاه‌ها افزایش یافته است؛ هرچند اولویت همچنان استفاده از کارت سوخت شخصی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131571" target="_blank">📅 11:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131567">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYpLJZGsXqXMntRAv9ZUA9JB6ON2paRSvPCTG0Z9lCzSVmaaIL7rNNPUjmwhPAyrfZVHZ77XEyCkHNL8pqcg2-ZZQkJntkKr9EJS1OqnZTGCx3HpZgYXVz4g38JUTrlzvaekAzxGsGrbeSGfg0D28RuRJtgh_psQxphrzTRakPtVRSSkGyfPixWyE1e94_KP0YxSqwb9lTQi08xuWDShOYhMMMDj1beWm3KnbdUfvPClF9hYn_W5E92U79VHlrWjg5245TpzgQawcdLpsaIFnjxGyEFPxBgMJolCRmEk2zF9WJk2q1_HRpToWEUq7lcEIkrMNtWGP8Vr55Gz8A6DeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5EpYt5_wr0KPYOPygqVJGE_ZiPh54NaTogNKVa-MB2PA7lOl-sb8TacgWm4RQgi2pO_3XgV0IOVpP0z0B_9wc7NQffljnl7S2IK21jNuSJMnDw16LcnyqvoZqNkPkt4NFx2onvPAEAq0uKhAXx34ptov1ccS8-FXC3KLx1en3oxjaCyLl8bbuYurx_0TEWUhIlY0nnJSgPK2pUExlX5Htx4Gat4wvUlA2edPjqWdKWY2EVP87MIE8jm2BIU5vGHX8nQMVUvygXk8jEPeDgm6rvUnShorNvuMJbt5JVA8YMDLe0erByWU7MQy2XwnbKV7XsFTj9xK0yLXnGtlE3n9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBXgbNfTLxkr30l3JETk1i4kV-LCMF3PcMIhjzV0rjdikVvuXsvUzP02layrS3pN4vOH-JXIpdKS_FV9lsrCt59Pi52Xp6AsdfK-aO_pzhPXvvbArAEAOYGoXQSwFkSVofgbuaXJ679lav5vGr2UzBhUF7Ka3fjasFtcp8vXMqr_MwReorRz17Wb7zP47eoMvyM3LKeNx0HYbr1KyGUIteMtXr5kulcZadO1yRT30pMzJhPrjDb9yl7ioc6FObhPPJ-T4G98qNxec9pzihvSAPxRrvpS4RXfYi_v1md7oMSKOcZFi7mhLxNSuS9hGsSJ5R1YkNKWztorld5LcS41zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYREvYn7pHGosOtI0kCPvtG_qCM7_cxK1baMQUd-prqjDzjkYPLXbIiqgnWOqYp9wnVafsA0y5XjV6jfhbz4XBbzPZUbH8hT0rVLoV-kLIBGx_dgkcbo2GLONo-CSfCoCscXmgcVllS6S24vWO9sYSs4Ts9wgPj0h3e9VzJrUnF7VrKLIYzMtzJNDQs0dr7iQSMasWOwCvNfGs7OIm37HaIjm8O7yMEkjUdiPLAhXUbe2CJphooDihjj8qJxisekprsGRcW93fNr6T_JPD2y1ejC4NqtSrhvN1XtLC6c-e_yczUuLKZ8nd7RlUfiNMC91Dt3Ktwx_g2cp9XfOvd4hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار نخست وزیر ارمنستان با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131567" target="_blank">📅 11:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131565">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qd6HXuAZdsm7QqpfqimNBcDJhf-rKBKznphbGgipniBaBlumOkfU_CiJhEu7XUbP1oI2KWCL3IGOpJt8MdvQWUDb_2T69Nri4l8Fd9FG1OuQkNLtzxPrgqgO3xM23HyZRphkpm6VQdbgoyyxW7v8zQ5QPxC9MVajVkIKaMDhQ-kP1sSLFK7fjh8av7s-F40j7viEAazvon4FN6_yJt9RbZ7w8Ltg5FWQfARw55dsozqPAds2neq3MvjafPldSO32NXkkCaq8a-6xe290fJapbzYsDvC_9LghPF7CC5Png1aLxiF_CeeUQuziQc2vPBAFNQLn1VC_dQHtgwBnynVHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwZY-WWHrbOIpNECxRDWJkhy6_UwR6XDRHkwA9EDNc297KGms2cXYm_n-H6J3IMwwEyNt8P45kb2ubyyg4txmtyQbJ_qPmam06mwI2dciVfyr1FsK7155oar90xtKy_MQOlGhm0e83rOudNXFWX0_1u-YTHP--b99jtMttlNOLmofTT9EXrezjBtPnhOStKvFn-Xc1wZrAUi5DDMbbjbvjwzYoINPC084ekVIoY8d1A7D7i8EFamotD_ZDeJVK60W2vHEqnPT-8guDZBUSPr260sV2K2E9HpWtpIm_5iUQNLeHOi9bsFqJ_ik7iQU0BxJKP5t967v4AcabZsmeVRlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
براساس تصاویر ماهواره‌ای به تاریخ 7 تیر 1405، آواربرداری و پاکسازی اغلب سازه‌های آسیب‌دیده در جنگ اخیر در حال اجرا است و برخی از آن‌ها کاملاً پاکسازی شده‌اند
🔴
هم‌چنین جزئیات موجود در تصاویر نشان می‌دهند که فعالیت‌های تولیدی در بخش‌های سالم این مرکز با شدت بالایی دنبال می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131565" target="_blank">📅 11:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131559">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYSwr_AFZUcs75GTF1x_886HeJZRIsuNsGMe2SfqUXIQV2XCEZVVOUGIw0l4ZHiqAIudp4UmZnsJXtXTKUHynFmFdwWBPjoaMZ67hvmPzWBXUjiV6ZE0tp3qK6Ssyr6L8ZtEZus1zU0K3tHI354Co6PFJaG-_H449_r7Ydmkrlgufen_-qyq1rU6oY3BQ2yg7CuRwZAvtEBnosgvJP62NGkJftc3YAqG-8Poennbm0wc_LrQ-3UipKRj90KUHLliOsVr5zV997CokmxrqCcdqF-p5gow8GltGZBZvRiNWI6YDjZSpuenv8z5JKKyJxF_86YDf8aZZDzIJmdtR0kieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFlSLbM9CIIAA0FF8BPRspKKCDrIgkD9cQpyFzicJlodkHVGQc_1hnjwc-lcvpDn3r23d-WQJDY1-RMMDLOyvxF1FnOzVe30Mgev94MlF-v1EylbOSxs84s09VpwnJPrH8clMqAY3_Xf7yPYwrBxLlpDt-EUsAkUzIzFBqG5qInXIG1T0bD_lboewhg_U-c2QbSvyRxSVjq3RnhpyXFEm6nOKQ_t6RNpg7vd1btjIX2dImawb4x87erYoCC65MrDDJQ5WgCDmmnW_1L5x5bW3j8LhtjFfAQBctUl8LAG1k67iyl43mSTWEui1b1oTGiuBUl91QABDfyTEBBzB_XKhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vY0sOsHyeyx-Pbnmrff8iG0h0JZqZ7BdEiHgRiSIYHN2LKPp1xthYckDtDAI9ZkUnexPrHjN8wJUvCWxxQl3hlZVXO8ffdc3f2h2WYgcB6pX0BhpyuLLnMcicna9hjQo1FYmGay4WSjAD7yUcJ2ZVHJ_u18gpRpcYxZ7MLzN4B6hhDt0kotiNfFRbHMZG4rq72RhQrKSvJ80I45tGHtActIvYn9bCDU4hNQCBLXF7pHzmRx8PjywVWHtNEUBEhW4hph_THhVUJyhGnnoyTyVE3LH2_YLYTYpAgvwhjwhMatOrXIdZNtxy25upbx9FAjBiHzTohRWEZQpTKV-4F447g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jg_wnyKNqKtyRaww95FA2AqOU8HwnT7ZzrJ5EHzzo0ugBIm1TfEh98DyBc9s7R2MQMCwbj7vhpgat6tZs2lB9jHElZqdoodYrmC873EBk6lVq0V5BKVkS6U_EkLvp9DdVSqir0nNZONsxRm0DD6RQ4NC32iqI2syHFMxpd4WDJFz4lLgljrE54uKVcJ6Ht_335vqn791gI-U50nZ-7NWuhAj7fyJ8WxtogG42yD1TC7M1zyqGFPz8ismZjbjz62IKbDEaKTsmHyNtZl0abd6ZTzrsteKqWXEpICblR-LonMeSe_cLTJFzi8cOVlW3-qXu0o3VNwQXmwxKhTEoc-iUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBR64w1Q5aVmMTNue1TAUo0dAH4S60QgtNdDO1Bns3BTDd3jkf1BIojx6LgLMBElHGiYl_U0tCL13g7xhwIF2Diqjs_vkNIVafcmiiGUcxMNV339dUciyKd3aKa4kS2LYMKakzI4eQeNBE-c98-YhXInRLKgXexjnnvx2VTdVwBv__cTxyc9lnQLk-0R-4OzTJXJazH0CGI5wQ4U3UQBlKi2KXr4D3pSde-a2B-O8FvVFN8C5Ad_lZtbwR1kCG0yB1VDCjW5BREHTYmIkuUoy_AXZGZxvxIAmiOdQWoTK-TXJq9nsGOaUo59CBDBtGJ3r_JvOd9RSYY6zScSYPMZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTJ-PlNM5CYYqLXMGdkPrPQwMVLeImIk1WgUoc-IjkU6YKuos1DlL516zV1eFeVSFCR7WGEH-4uZYyjrspcmy4ucyVFrovEEAwQR9N0GfrvnAP8i5EHn73oOsTj34NKbVoutLHCt4LxWKtX9g3slwsFcNyhfq2adjKlphlEAj1wFYCO8X0nzHCtp1HSwClQ2bRTPKWgGajI179Zs4tEXOtr4zwtm9l_8JV8BwmKn5V2at2IJyjS8r-TF8qWXZnInzZv6KVE3wUNhhREQaRv0BHSZL5CO566xk5Cg3_AUgbpjARCdOgc9miGuZtxgoenJiHx3wCkU0Hw6XCn2EGCWxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار رهبر ملی ترکمنستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131559" target="_blank">📅 11:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131556">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fwa6qsvV9nGXZSkFmbxr_LtLkSWmXhzmIxLvUYueINWkZhGM_WACE_6gs5ea8EX4jKQLwo4bHUmy9pNcr0hJ1KwmZ7BadG4sRvmylb853ffdVI0eWaL9LNXzJGjqJNNHpHjvEiGq4Zek5kGEwqfgifTPc8PvIMpfXEIq0Qk8lLPiNwsLPFL3_PvkclWUl6ukaQ7-uCxqGNbIxwJhm4lnGo9gwx7hwKIdYFCnvfInhoHGVWuLGh6N7Q5bxuOqxNbcruocLEIpHx0-EgPaEuxdUtd16r3hIOQE_NgpDgHtZ0dNF416XgfRMtXhcychviZHplrc_7d-Ueaz4L-LN6V5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqQEFqqrwxKBChDjXeFc5MDgte45tM8ByDZoTGdxPjcN8AZ3Tq4U_VH-JjmAA5w8usi3ka1RNUSWAXmOrVkCKrszfsr55S8itNZd-nH-32aUj8TG7eptEOn3BLTK6NZvVkAhVx8iJeCCOKBoSdgDW7DHl2fQqCFsQo1L75doPHITGEitLVsjJEUHhODoTqeYFcodzyHbWg2f0-bOAQKIG9acZsv278NnJXvHqQ8XGzjx5uxWNw3-n_xQzbTHaJq-evJI1DkRJKiAVCgIOhpvrAboQtmQkH9MyxYfkr04Lduvnk5yJHeuBXrKLiXd5DI0xANuOrxd_qKlP1VkpEhW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1CbrkXT86Sb9PToKLPRQjGlNSrzX9VhPG0z8MguVloOJA5DIkiOl57MZLEMTRIcq_0-p1uf5Ql9jLK1JUYIO-35s966RW12M6OKsLp2eJzKbMUIav8fF8ZM0BnS3cpYwHAgaIxkqcGPGh7hDyXJreUN9xQ8PBhskPbS-ihVuGTMxUIhZZ9sytQTHBU7aJ0EmdnT0sICU6rSQZ0DsGQjfzn7dYs8HV-GM76MPHppeJ5CPKRsgfLb8ir-4L1uab_xP55ibmc3ccqfl8Lv01vnq6EsSg34tJPnkJXp1wPh_1_hFLeLqKYtPKTSdyN3M8kbcL0yjsBsuKi5rkOa86clbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار چارلز موبیتا وزیر کابینه ریاست جمهوری نامیبیا با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131556" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131555">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ3UBGaTKJ_qs8v0fAIgbICQ-rE9RzupLhfMVH_cyI9SnaThUq0pk-8qUY58vgw_IHA7Z_OlosjeVRCgigQA6DQFnTuPpov3VgJBnHp9_vEL4QMudku6wGeqrQFJFKOfXcDHww96ROq_DGBAWz0QH6F3Mn2IOh0Q3fjZW6OvujcZl16HzINr_W2eI4EdbWVaMPE3uGyVC21VCY1x78YtdgIg8vlK4NgRUGjV3ZcBMGMmBmCFD5IoGjhZ707jjiTdqjKs1xpf6b_LTqiejIW-pkc-V6En3vwn46qZq8m5jhl7Hfx_iGnQTN2t7hxC5Dj7GZaoEqRBCslpAsNVYNaIgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت جدید ظریف ، وزیر خارجه سابق
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/131555" target="_blank">📅 10:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131554">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
قالیباف در دیدار با معاون کنگره چین: اجازه دخالت آمریکا در تنگه هرمز را نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131554" target="_blank">📅 10:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131553">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9742057ed5.mp4?token=AgHPB6LZe1udpTTD0IWRIZ-KrTI1uq9OZtlahcx_4CVwbHpNNsboEY38GGKhRb-pB6tqq9-NzbC8NzhpY3DfPDPWt3UxjBLBAL5DusA_GaMWGMp6UQWxCKeieFcHRqkeXwzGpPKURaJwRc-9p7LDVgy4oqEjOofMDlhCDAbJM09Rnk_m3-Ywws9lYe6wOMQDqvMmtVsfckCIo9KPKqbNOGA1_8LvsIThupXMrMtsoh2u3iMjUSdHYbNgFFTahP53PkpsxtWiUxmZ_Ev5_7_apBQSamMPeuuTzrWFq0FzkpXUYBJsFaeRI_vmdO4skyn1j8rYb_8hOw87q1dF8D36tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9742057ed5.mp4?token=AgHPB6LZe1udpTTD0IWRIZ-KrTI1uq9OZtlahcx_4CVwbHpNNsboEY38GGKhRb-pB6tqq9-NzbC8NzhpY3DfPDPWt3UxjBLBAL5DusA_GaMWGMp6UQWxCKeieFcHRqkeXwzGpPKURaJwRc-9p7LDVgy4oqEjOofMDlhCDAbJM09Rnk_m3-Ywws9lYe6wOMQDqvMmtVsfckCIo9KPKqbNOGA1_8LvsIThupXMrMtsoh2u3iMjUSdHYbNgFFTahP53PkpsxtWiUxmZ_Ev5_7_apBQSamMPeuuTzrWFq0FzkpXUYBJsFaeRI_vmdO4skyn1j8rYb_8hOw87q1dF8D36tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشت جوان پول خود را روی هم گذاشتند تا یک موتور بخرند و نوبتی استفاده کنند...
✅
@AloNews</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/131553" target="_blank">📅 10:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131552">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
فایننشال‌تایمز: ترددها از تنگه هرمز چهار برابر شده‌است
🔴
یک رسانه انگلیسی نوشت: اعتماد به آتش‌بس افزایش یافته و ترددها از طریق تنگه هرمز در هفته گذشته، بیش از چهار برابر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/131552" target="_blank">📅 10:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131551">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزیر کشور پاکستان پس از ورود به ایران: اینجا خانه دوم ماست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/131551" target="_blank">📅 10:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131550">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd05539a.mp4?token=bg1iD0Phrgw9-xm3SJg3Mc30KyYczJZzJJgqzDHj7EhWMec1mFTOXezJjaY_9qw2VYAp91pM1RXsQiilK9QOyCvqwsZSW7-3g8yAK83gxcjX8z8ZjXIJ5j7iEGLt-Iovmb9H0Or2UaMX8nHt8IAJUKGC4kgjHrRjMXcUusM1qMVBGcc7hYUKD80c2BC2qtKPQbPzPHyZi1LMVWHTWHoYvydU6MBW8udSWgHS1Ri93jTzzAbnfWqKmHkW3rR_R1pe7iPffTir4VkLAj9eBIZRQAHKv7Gk3pEpIslFqTUOcfyAVBV5ko-LzrSUegL5uX5Z4onHqtaMI6rvA0KIElmOQLc2pK3jR-cV5A3ypkcJpJXlheIOJ1Xf8FYN4ea6uANexRQQLFZkkDZTrm3PnCwKEmZhi7Iy19KvxUZIrC1V-d0xFONPY1C7jG4pvzoSREh-oIbhfT24jLyyba9wOTubadsR3677YTBXYVfWeUV5AGjb-28nXvYs_L7dmF56J1F8FLaglBbjN5ZqdIWUoy21pv7v2muu8tROP43OTrP_9G5Dhd84NEYBnoEMtOBlNNtiSEhWVTdVzjveBJY9W-Klf2AHxFYgO5SLm-k-B3EX_-ZWpAfs-8d-4eRnwTTkx06Njtdy7lBAMYzOf7ewLN7HGJufzRvQXbdYOY9TO8dEt5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd05539a.mp4?token=bg1iD0Phrgw9-xm3SJg3Mc30KyYczJZzJJgqzDHj7EhWMec1mFTOXezJjaY_9qw2VYAp91pM1RXsQiilK9QOyCvqwsZSW7-3g8yAK83gxcjX8z8ZjXIJ5j7iEGLt-Iovmb9H0Or2UaMX8nHt8IAJUKGC4kgjHrRjMXcUusM1qMVBGcc7hYUKD80c2BC2qtKPQbPzPHyZi1LMVWHTWHoYvydU6MBW8udSWgHS1Ri93jTzzAbnfWqKmHkW3rR_R1pe7iPffTir4VkLAj9eBIZRQAHKv7Gk3pEpIslFqTUOcfyAVBV5ko-LzrSUegL5uX5Z4onHqtaMI6rvA0KIElmOQLc2pK3jR-cV5A3ypkcJpJXlheIOJ1Xf8FYN4ea6uANexRQQLFZkkDZTrm3PnCwKEmZhi7Iy19KvxUZIrC1V-d0xFONPY1C7jG4pvzoSREh-oIbhfT24jLyyba9wOTubadsR3677YTBXYVfWeUV5AGjb-28nXvYs_L7dmF56J1F8FLaglBbjN5ZqdIWUoy21pv7v2muu8tROP43OTrP_9G5Dhd84NEYBnoEMtOBlNNtiSEhWVTdVzjveBJY9W-Klf2AHxFYgO5SLm-k-B3EX_-ZWpAfs-8d-4eRnwTTkx06Njtdy7lBAMYzOf7ewLN7HGJufzRvQXbdYOY9TO8dEt5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مأمور پلیس آمریکایی، یک زن را به ضرب گلوله کشتند
🔴
مقام‌های محلی در اورنج‌کانتی آمریکا اعلام کردند که سه افسر پلیس پس از مواجهه با زنی که چاقو در دست داشته، او را هدف گلوله قرار داده و به قتل رسانده‌اند.
🔴
گفته می‌شود تحقیقات درباره نحوه عملکرد نیروهای پلیس و جزئیات حادثه آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131550" target="_blank">📅 10:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131549">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پنتاگون: اروپا مسئولیت دفاع از خود را برعهده می‌گیرد
🔴
وزارت جنگ آمریکا مدعی است که تلاش آن برای وادار کردن کشورهای اروپایی به برعهده گرفتن مسئولیت امنیت خود، موفق بوده است.
🔴
«البریج کولبی» معاون وزیر جنگ آمریکا در امور سیاست‌گذاری، در صفحه شخصی خود در شبکه اجتماعی «ایکس» (توئیتر سابق) نوشت که ائتلاف «ناتو» اکنون به سمت تکرار وضعیتی پیش می‌رود که در آن «اروپا مسئولیت اصلی دفاع متعارف خود را بر عهده می‌گیرد».
🔴
این مقام آمریکایی اظهار داشت که هنوز کارهای بیشتری باید انجام شود، اما واشنگتن به حرکت به سمت نسخه جدید ناتو که مبتنی بر مشارکت، نه وابستگی باشد، ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131549" target="_blank">📅 10:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131548">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
به دلیل تهدید مداوم وزیر دفاع اسرائیل به جنگ و ترور، ممکن است در دکترین هسته ای خود تجدید نظر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131548" target="_blank">📅 09:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131547">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سرپرست وزارت دفاع در گفتگو با وزیر دفاع ترکیه: ایران توافق آتش‌بس را با هدف کمک به بازگشت ثبات منطقه و به درخواست کشورهای دوست و همسایه امضا کرده
🔴
اظهارات اخیر مقامات آمریکایی درباره گشایش جبهه جدید علیه حزب‌الله لبنان می‌تواند کل منطقه را با مخاطرات امنیتی جدید مواجه کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/131547" target="_blank">📅 09:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131546">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
میخائیل گالوزین» معاون وزیر امور خارجه فدراسیون روسیه بامداد امروز گفت که مسکو آماده است تا مذاکرات با کی‌یف برای پایان جنگ را ازسر بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/131546" target="_blank">📅 09:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131545">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی:  مذاکرات با ایران همچنان ادامه دارد
🔴
ویتکاف و کوشنر، در قطر نشست‌های سازنده و ثمربخشی برگزار کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/131545" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131544">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
تعداد کشته‌شدگان زلزله ویرانگر ونزوئلا از 2500 نفر فراتر رفت
🔴
به گفته دلسی رودریگز، رئیس جمهور ونزوئلا، تعداد کشته‌شدگان زلزله در ونزوئلا به 2595 نفر افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/131544" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131543">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
گروسی: ذخایر اورانیوم غنی‌شده ایران هنوز از تأسیسات هسته‌ای خارج نشده‌اند
🔴
ما دقیقاً می‌دانیم که این مواد کجا بوده و می‌دانیم چه مقدار از آنها وجود داشته؛ پس از جنگ ۱۲ روزه در تابستان، ما با استفاده از تصاویر ماهواره‌ای و سایر ابزار‌های مشابه، اشیاء را زیر نظر گرفتیم؛ هیچ حرکت قابل توجهی را ثبت نکردیم
🔴
بازرسان آژانس انرژی اتمی هنوز به تاسیسات هسته‌ای ایران بازنگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/131543" target="_blank">📅 09:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131542">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=If_pAVA0KHZByMjPN6j3Pq5El7JvOopE4e5tcGTQHXAZnUzITqgigvNIcii47o7E2hD5eqpI7nAL0u2omFkpV4AfaFY9Ukkxo1r_PRmyo2LAg3_Dy3vc2QWWwqQpBa6IGSU71q_LlTv6NyTKTVP771vutEzw2TtSdxECWZ8CgnI0H0hZJQj4-RzhUyKfBmuZQZKfD1DS_5Ta-mwemgL73M3N8q-PWIjFoxfdWqjyyIOOB9A3BDLCUyLF3dhWEmo0kAoY3DzNmK5NRKbt5TUcYfK50rgS0mrPc2048h1VOSKn179rT_aTvJaXk2oZNZLuOS2UyBVdNOwhCD4Kxfm9tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=If_pAVA0KHZByMjPN6j3Pq5El7JvOopE4e5tcGTQHXAZnUzITqgigvNIcii47o7E2hD5eqpI7nAL0u2omFkpV4AfaFY9Ukkxo1r_PRmyo2LAg3_Dy3vc2QWWwqQpBa6IGSU71q_LlTv6NyTKTVP771vutEzw2TtSdxECWZ8CgnI0H0hZJQj4-RzhUyKfBmuZQZKfD1DS_5Ta-mwemgL73M3N8q-PWIjFoxfdWqjyyIOOB9A3BDLCUyLF3dhWEmo0kAoY3DzNmK5NRKbt5TUcYfK50rgS0mrPc2048h1VOSKn179rT_aTvJaXk2oZNZLuOS2UyBVdNOwhCD4Kxfm9tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل : اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است
🔴
این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/131542" target="_blank">📅 09:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131541">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
فاکس‌نیوز: مقامات ایرانی نسبت به برخی بازرسی‌های هسته‌ای روی خوش نشان داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131541" target="_blank">📅 09:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131540">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فایننشال تایمز: با افزایش اعتماد به آتش‌بس، عبور و مرور از تنگه هرمز هفته گذشته بیش از چهار برابر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131540" target="_blank">📅 09:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131539">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO8eo_VUtykfSMa2sEa68eW8HJoMr-VLcmzmxeeT96s1C1HeunxFqU_dX3O4At78Rjwitd4zPiQ8OS73LIT25GxLvJzh5PT0gaRnlBwhwF-fEpGs9crSdZSYhL7liQmzyAGgiUAWpPpdzTfh_AnB-5UAUOnfXPNBoc8AJ6ZF3axJlhDqtwMRxb6to8xdpAAZ_eH9fTIyEOozmmEhXYYYEEoBYDiKrJR_EOYmQ2qP71bSevc3n91t3THjczfMPwSzvYHLiwy0YLM6FER3p5Tw9R5F4bEuIwHrkHyQCrr4zo9lK9C9z_9N_PXcZSJ7RgtLSbmy04bOVuKVU48vlTvWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر کشور پاکستان برای تشییع جنازه سید علی خامنه‌ای، وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/131539" target="_blank">📅 04:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131538">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6y4P5XPNXN1E1lPH_7lq6Ngk4DjerPqlf3bL2iSlbaDhIHhqlLE575xn-APjHeBoPFQLGCLwVSRmEFqYlTTUVHkdDF-A7CsVI6aLoS_wYOeyBZpVUMPq0HkXMNbma6Kp1d5q7ld2SOqg8O8tZ_gTUf1i__twWJmgjtU7yGhWZ9bF8yqtKb3hfraAzZCNBjr9EtugTWKllnqXIedcEFUret38xwc0T6A4X2wEwLAc7Ah0t4rgsj5YVyELwuNlsOVge2xlqWtILuTpsa87o7gARSvC6Blrdly1KdulYcSVF4MzIskYRwha_R1EuDVpitzhG3O6noiiYa4pEVER-v0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از آسمون منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/131538" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131537">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
منابع خبری از حملات اسرائیل به شهر صدیقین منطقۀ صور، در جنوب لبنان خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/131537" target="_blank">📅 02:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131536">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: مردم ایران از من تشکر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/131536" target="_blank">📅 02:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131535">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/131535" target="_blank">📅 02:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9Di4o5Yp1GJin7u1zKlg3boR6EG34qJ8KCyY-g5L-YTrzVIFTgMF0A5nLfGtfDgFOBgRKRuF_rXx9jKuynL3D6xmiIM8N21tENkbM7MumXXdXikN2LjgeFgX3Zn17AhEetFf2YHXazd4DhVsIIvKiV1h8M4SyqZFIC5ovMw0nalV4iirr0AMcWi-MKjZTej7sz0qIZcSy_yOMl09HZiSaMgVRBx_jLF4rlMjqkjM-_eoCNcjWA4__iH0Kha9yKzlWKe5AifETIyhIdV3QAsmMXRTqOdnVwB-QoD_KABLNerDahRkoYSGqEJKePdXB9ZRr4MhfRUahrqhv05ebuq9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/131533" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3df6d8da.mp4?token=iMLVQjAlbdvWsQH9uCW9E7c3NUj3FkLx02JpASOM3CDXB4lKTjuhZxYSs1Ba5RAy3dkCBRz7_oanBJFCtzSmJzmdgOg_zouvBrKaa5I_H74gYRgsEGSkspm29bLI2K5RBXLF0wo32C5m7LInEB1TKqq-TdIGux_p0xV4iv8Wmrb3PXeWWd4lDiC_7L2NQwBeknibG9i9K-2i051aGVy8tHVqiFrr6YSxJI00wzfH2iWSVuDt86lnCdc1mrVQxqY9XnE9_BTV2sqOkohFk-mn6wRZl1n7F_u-UHFjArbBTxWlBsA_BN6UtMMW09dDfYd7bJAeTOxmyd9yWpgpXmJWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3df6d8da.mp4?token=iMLVQjAlbdvWsQH9uCW9E7c3NUj3FkLx02JpASOM3CDXB4lKTjuhZxYSs1Ba5RAy3dkCBRz7_oanBJFCtzSmJzmdgOg_zouvBrKaa5I_H74gYRgsEGSkspm29bLI2K5RBXLF0wo32C5m7LInEB1TKqq-TdIGux_p0xV4iv8Wmrb3PXeWWd4lDiC_7L2NQwBeknibG9i9K-2i051aGVy8tHVqiFrr6YSxJI00wzfH2iWSVuDt86lnCdc1mrVQxqY9XnE9_BTV2sqOkohFk-mn6wRZl1n7F_u-UHFjArbBTxWlBsA_BN6UtMMW09dDfYd7bJAeTOxmyd9yWpgpXmJWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور:
نمی‌فهمم چطور یک فرد یهودی می‌تواند به یک دموکرات رای دهد.
من بهترین رئیس‌جمهوری بوده‌ام که در تاریخ اسرائیل وجود داشته و آن‌ها هم این را می‌دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/131532" target="_blank">📅 01:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131531">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac200869f.mp4?token=p9CqZzHTYn434WoDJ989Vnl_kNValWgyv3v0JjgCOFB10DUG-gRjsf0aGXDDMSFaWIRd6CNiGwth8GreUbiZA59EI9GeSTZDKVBDE0vQ-z08a3yfr2-FbBRWz2zxPBwBat2vZ4IinvzGDCHUzYyFeMyla6OnYJiDVoa1HLQiZMWJ3pLqTI0FXZbI_iJf-IpiHAjG7eKIfXaqm5mkbdObESHv32649nQn6nb0FecqH9UccKfm3migkb0qmwEVsNu2Fd155UZOae1n5QePRvkJpSLYQMpj6igx6wtSr8eFXXS6JQL3orH8ZY6tef91aKGK2XAI5nWs7kxA_bMg-x9D2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac200869f.mp4?token=p9CqZzHTYn434WoDJ989Vnl_kNValWgyv3v0JjgCOFB10DUG-gRjsf0aGXDDMSFaWIRd6CNiGwth8GreUbiZA59EI9GeSTZDKVBDE0vQ-z08a3yfr2-FbBRWz2zxPBwBat2vZ4IinvzGDCHUzYyFeMyla6OnYJiDVoa1HLQiZMWJ3pLqTI0FXZbI_iJf-IpiHAjG7eKIfXaqm5mkbdObESHv32649nQn6nb0FecqH9UccKfm3migkb0qmwEVsNu2Fd155UZOae1n5QePRvkJpSLYQMpj6igx6wtSr8eFXXS6JQL3orH8ZY6tef91aKGK2XAI5nWs7kxA_bMg-x9D2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همزمان که تو تهران با بیت المال داره اینهمه هزینه چند صد میلیون دلاری میشه برای یه خاکسپاری، بهتره این کلیپ هم ببینیم
🔴
ان‌شاالله که همه مردم راضی باشن با حقشون داره اینجوری ریخت و پاش میشه و دینی به گردن مِیت نباشه
#بیت_المال
#تبلیغ
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/131531" target="_blank">📅 01:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131530">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937314ac6d.mp4?token=TGYiYkrdMaCajwSGx8AEEShhHbRQamxKCZOyMU9xmNTeFGbpZPPwkapHv_emSxyUE1TkpdFP4x5jrRt2EIWa9Bs2YuijD-mgCw_tzJ0lUTVmurI3YZqJOuMAWH2pha8-Q1QHq7aSkbaAgSvKIlSTLNFVgvcibaBlrVpbOSkhA6HXDZixhzhtuxYdqNqyeWZRomQ1spzB6SYHOZFQm44JStFhzBTo4RCv_nJvd3Jfq6WGMKyc_HbHM9FIlnecuH7buU8t5NpAmWfvSrQLfsIXgUSP84hKWthQTdbyoohxvp_CPJImv9ERxVEXG_jNDBHeEylG2R4QsbUyupWdQYyCHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937314ac6d.mp4?token=TGYiYkrdMaCajwSGx8AEEShhHbRQamxKCZOyMU9xmNTeFGbpZPPwkapHv_emSxyUE1TkpdFP4x5jrRt2EIWa9Bs2YuijD-mgCw_tzJ0lUTVmurI3YZqJOuMAWH2pha8-Q1QHq7aSkbaAgSvKIlSTLNFVgvcibaBlrVpbOSkhA6HXDZixhzhtuxYdqNqyeWZRomQ1spzB6SYHOZFQm44JStFhzBTo4RCv_nJvd3Jfq6WGMKyc_HbHM9FIlnecuH7buU8t5NpAmWfvSrQLfsIXgUSP84hKWthQTdbyoohxvp_CPJImv9ERxVEXG_jNDBHeEylG2R4QsbUyupWdQYyCHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: تورمشون ۳۰۰ درصده هیچ پولی هم درنمیارن برای همین یه بخشی از پولشون رو می‌گیریم
🔴
اگه به جایی که مدنظر ماست برسیم، تأمین غذاشون فقط توسط کشاورزهای آمریکایی انجام می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/131530" target="_blank">📅 01:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131529">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌بی‌سی: رهبران فعلی ایران منطقی‌تر هستند و ما با آنها کنار می‌آییم و این تغییر رژیم است
🔴
من به دنبال تغییر رژیم در ایران نیستم، بلکه به دنبال جلوگیری از داشتن سلاح هسته ای هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/131529" target="_blank">📅 01:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131528">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddfe688da3.mp4?token=Gfcsspd52r9rc5ZpUtVdvC8U_zFysMU7aXRYXPNQuF2rajw0dCEG0Ej743oM54gbbONANatKplRX9Xr5sVlUUnkdcyvTJLmdEu0jfuxbP7QADPn2jcpqyzFPjRgeWlAOux4bFUxbUdB_zVCgcEPdkU_s31TonEjrQMRave5ayf-KwP4IfFz3MKb50mUwznkX3iJnzhyC9G7SY9BuFd_IjRABQ32MZQqZFw9K3ZrQofNHF4ddZqhx7RrD2OTM3rHTOO9-nW_qYh9zvmYZ7KFSng8DGPGw0ZiP2L8Ys8F6VkVhPK3e8J2zQdXM5h4IYpPGcUBK7pEpCiK8HJsmkfAz5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddfe688da3.mp4?token=Gfcsspd52r9rc5ZpUtVdvC8U_zFysMU7aXRYXPNQuF2rajw0dCEG0Ej743oM54gbbONANatKplRX9Xr5sVlUUnkdcyvTJLmdEu0jfuxbP7QADPn2jcpqyzFPjRgeWlAOux4bFUxbUdB_zVCgcEPdkU_s31TonEjrQMRave5ayf-KwP4IfFz3MKb50mUwznkX3iJnzhyC9G7SY9BuFd_IjRABQ32MZQqZFw9K3ZrQofNHF4ddZqhx7RrD2OTM3rHTOO9-nW_qYh9zvmYZ7KFSng8DGPGw0ZiP2L8Ys8F6VkVhPK3e8J2zQdXM5h4IYpPGcUBK7pEpCiK8HJsmkfAz5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
🔴
ما شب گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/131528" target="_blank">📅 01:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131527">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/673b985d42.mp4?token=kM0VqkrEAM-AaeKeOdxASA47wBqpUjNPFC62k-KkbxJGkOeEDLu50-VTRqXR6PeHlhNw0t9RueDUAkTcKdwd7_9H1TELWmPy06PVoKzOvGNUvv4naGLbMxGkAXzheCyZ9J9dcAf-Xz3DtGimxrNONmFWm2MQ16IgWYh1SNh7mfh8Tu9Dp1Gs_HGNmu3EWOpiC1Vc3AIR2jJLuDctR8UzpPIbtJgP47SbdnKMK0Z0bCIJ7JWeFRmXabsiwv4anEgYN9xDS5aPeNMd1GDEI4IHyjitY9iESaN1_KNZKsc1MeFnmSUb373NXSnmbRGBwfgTAPZS_Kx3JfUR5_xBMG9NeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/673b985d42.mp4?token=kM0VqkrEAM-AaeKeOdxASA47wBqpUjNPFC62k-KkbxJGkOeEDLu50-VTRqXR6PeHlhNw0t9RueDUAkTcKdwd7_9H1TELWmPy06PVoKzOvGNUvv4naGLbMxGkAXzheCyZ9J9dcAf-Xz3DtGimxrNONmFWm2MQ16IgWYh1SNh7mfh8Tu9Dp1Gs_HGNmu3EWOpiC1Vc3AIR2jJLuDctR8UzpPIbtJgP47SbdnKMK0Z0bCIJ7JWeFRmXabsiwv4anEgYN9xDS5aPeNMd1GDEI4IHyjitY9iESaN1_KNZKsc1MeFnmSUb373NXSnmbRGBwfgTAPZS_Kx3JfUR5_xBMG9NeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/131527" target="_blank">📅 01:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131526">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌بی‌سی گفت:
ایران در طول 47 سال گذشته، با بهره‌برداری از ضعف روسای جمهور سابق، زورگویی و ظلم در خاورمیانه و علیه ما انجام داده است.
🔴
اوباما 1.7 میلیارد دلار به ایران به صورت نقدی تحویل داد تا از آن برای توسعه سلاح‌ها و موشک‌هایش استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/131526" target="_blank">📅 01:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی گفت:
رویارویی با ایران به خودی خود یک جنگ نیست، بلکه یک عملیات برای خلع سلاح هسته‌ای است.
🔴
به هیچ وجه نباید اجازه داد که ایران سلاح هسته‌ای داشته باشد و من از حدود 4 ماه پیش، تلاش‌های خودم را برای خلع سلاح این کشور آغاز کرده‌ام.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131525" target="_blank">📅 01:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌ان: ایران تقریباً با هر آنچه می‌خواستیم موافقت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/131524" target="_blank">📅 01:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQOQnTDm2tovS_mS_h_8ZU7qcSmcrVD1PrGMTIDMBXbKUYZj2AkCn1gz8ktGRTft9uRgArcsUm-pQhtnxTl4sY5R8BPfV7WmEE6sZoqXZKSjv_Xo2sXpXJfO0MPWRjXmyd7I1WCIx2wskiTZAF26p2zPp3sF1BYdtPrPqkwHxLCP3ePHsS0w3uEYIGf07Th4DwL8oaU0jnvODg9Tn8nKX_MDKosBbQE2z2nc5AxfEBuHEVm-5al6Xi2mFDdjirNg4Q81C46cxXm1IpN-h5mfyEKYQh1otEjUZ0_2XUmLFyaX-1KITGmo4AtAkVioL79Gnyws6tF7riDwG9IA7GR9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی، شهردار تهران: ۲۵ میلیارد دلار پول نقد دست مردمه و میتونه در اداره کشور استفاده بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/131523" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/131522" target="_blank">📅 00:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
بچه‌ها
الو اسپورت
و
الو توئیت
هم دنبال کنید
@AloSport
🔵
@AloTweet
🔵</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/131521" target="_blank">📅 00:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131520">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f6f491fa.mp4?token=I9KczZkC0MehxEWgGLre0al56PysCWcu-4QfX3MOeDMfnYMN6jFFHUr4gZ9L9cSx9-DEF360p_LNL-q1-QitcLWr8hfTQ1kOVnfAAfl9whjT1BRIIm5578qbcvaZWSKgbhE2oj2uTR7me90QuYuHd0jVahdZWkvImAIZBwSb7rZoy8ohYiNgdNgw7FmNJbG_tGSr9dFydQmUebhjm2aU2srGesgmStx8ewiuCpQwlepWZiaUqCCzVosVRmDlxAz7T-5aMI9txrY_lVLQ1aLDfc3tsrCeASiUOv3bnbsuXkWkrviwOP1LUn-m3I-qSpBjMtEjFAn6P_yxFxkVKvjAZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f6f491fa.mp4?token=I9KczZkC0MehxEWgGLre0al56PysCWcu-4QfX3MOeDMfnYMN6jFFHUr4gZ9L9cSx9-DEF360p_LNL-q1-QitcLWr8hfTQ1kOVnfAAfl9whjT1BRIIm5578qbcvaZWSKgbhE2oj2uTR7me90QuYuHd0jVahdZWkvImAIZBwSb7rZoy8ohYiNgdNgw7FmNJbG_tGSr9dFydQmUebhjm2aU2srGesgmStx8ewiuCpQwlepWZiaUqCCzVosVRmDlxAz7T-5aMI9txrY_lVLQ1aLDfc3tsrCeASiUOv3bnbsuXkWkrviwOP1LUn-m3I-qSpBjMtEjFAn6P_yxFxkVKvjAZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه 14 اسرائیل ادعا کرده که قراره به زودی یه گزارش کامل از صحبت‌های دونفر از جاسوس‌های موساد تو سپاه پاسداران منتشر کنه که این فعلا تیزرشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/131520" target="_blank">📅 00:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131519">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
هشدار سطح نارنجی گردوغبار در تهران از پنجشنبه تا جمعه (۱۱ و ۱۲ تیر)؛ کیفیت هوا کاهش می‌یابد. سازمان محیط‌زیست به گروه‌های حساس (کودکان، سالمندان، بیماران) توصیه کرد از تردد غیرضروری خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/131519" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131518">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
هلند ۴۸۰ قربانی جان باخته دیگر به دلیل گرمای شدید ۳۵.۴۰ درجه ثبت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/131518" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131517">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoc526SM-D9xMZKO2rVbR4y1k3fXkmvn021TB3vuMSjc1o4pHL4TRsahYxhENCydHDoFO7pZcWrYg4940g5x1Ae-6asb1LS-5ZjcsYLn4eAIfQKygWt8aWAqgO-LXsc1ns4I__hM8LdNuie7wV4ozeN9bu5RErOuu9mTZiX4WjoP_cg4fTgF7vorRqIjqGq3W4gdVe3wPxFD3oNHXp-b9AHbUHKWEdyt7jmupBvdKGVLAuWGdHFdWBa8_Waft47TZiZSrS2o3-QomLSYg2CR4rJKQ0ufdHS3YQthcpOnhIQzFlI6aRAybx6LII_Y3CMjHNRrW4T7xvsW6MJ-mYuq-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ:  ۵۸ میلیون بشکه نفت و میعانات ایران روی آب انباشته شده و ۹۰٪ این محموله‌ها مشتری یا مقصد نهایی ندارند.
🔴
با وجود تعلیق ۶۰ روزه تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خریدها محدود مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/131517" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131516">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خلاصه هرکی بیت المال و حق مردم رو حیف و میل کنه در دنیا و آخرت ذره‌ای آسودگی نداشته باشه
👍</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131516" target="_blank">📅 23:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131515">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یادمه تو کرمانشاه که زلزله اومد مردم برا گرفتن یه چادر و یه بطری آب پدرشون دراومد و آخرم‌نگرفتن
الان برای یه تشییع جنازه(تبلیغ) صدها هزار چادر و .... به خط شده</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/131515" target="_blank">📅 23:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131514">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چه پولایی داره خرج میشه برای یه خاکسپاری</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/131514" target="_blank">📅 23:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131513">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131513" target="_blank">📅 23:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbvnDfoJh9vKAYJWRV-vqkDpC42KqmAYLTP_aVOAt4yE3ihalU8dsL6FV5GTi4-7_li57eiZLlw13GHnvu-xMlBF_n81sFaArO-xdzOcm0RAoFoRF-sD-_-0zmbQnUvW6d4RXx0fg15FRrAKX2hv8TJ5gTu4eMTXJPsfb4ji7vFdr_Hy-gmc-HKaA4ZlUrDVPYSl6gh2Mqvyqk9_eNTRHZ3s-hx-rawJBay0xEdFlbA_H_Zh_rGorPex7AYKxWWJOcSYFRjn-WgkcCdeBCtFHEHg1QNI-AKSwIv6TyjryCwKtIubMAijPDwd99ZrDWG4sSAsZgy-J2ki9mJ3HLimhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده تو تجمعات شبانه : وای برما؛
تو تاریخ اولین ملتی هستیم که خون پیشوای خودمون رو به گندم و ذرت فروختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/131512" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
العربیه: فرانسه، ایتالیا و آمریکا ائتلاف نظامی‌جدید در جنوب لبنان تشکیل می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/131511" target="_blank">📅 22:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131510">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سفارت اتریش در تهران فعالیت خود را از سر گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131510" target="_blank">📅 22:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/131509" target="_blank">📅 22:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: مذاکرات با ایران ادامه دارد؛ ویتکاف و کوشنر جلسات سازنده‌ای در قطر برگزار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/131508" target="_blank">📅 22:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131507">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oRTiDNPnnT918gL0BHoffkL41lrOt_TRb4OoGbNysn8vjSFZlMoOYmjNTdJ3cUYa0hgljoiH4BW10YdiOifERNAy1R0Ydyi49vw3NQ0yO5fYu0mGLdKmWUZnb6ZPu7d4f6-RCFPdiAPr7zZIrodhXw89-C1ybomod8a0sCgun1aQCqBlCMCxHESGw8-5LlllpBWPON-sJf5L9IDq7PsAhAGvfhGWlFTsvQrcnreckkWuN2S_8oukHlTj4llF0LToCPT0qC__MlFtGVZAwdZxAYRcOO4rZF_I68t8qkDA_Wk6g0w-8zx3HnFojtFCQq9o7JpJzkazZTVS5y6f3gVuCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی در واکنش به جلسه فرماندهان منطقه با فرمانده سنتکام: فرماندهی مرکزی ایالات متحده (سنتکام) امنیت را به منطقه ما آورده است یا ناامنی را؟ پاسخ کاملاً واضح است.
🔴
همچنین، نیروهای مسلح قدرتمند ما ثابت کرده‌اند که حتی خود بیگانگان نیز نمی‌توانند از خود محافظت کنند.
🔴
صلح در منطقه ما تنها زمانی می‌تواند پایدار باشد که جامع و فراگیر باشد و هیچ دخالت خارجی در آن وجود نداشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/131507" target="_blank">📅 22:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131506">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه، فیدان: اسرائیل در حال حاضر به دنبال یک دشمن جدید است.
🔴
تا زمانی که اسرائیل - یا هر بازیگر دیگری - به گونه‌ای عمل کند که با منافع ملی و منطقه‌ای ما در تضاد باشد، هیچ دلیلی برای ترسیدن از کسی، تردید کردن یا عقب‌نشینی نداریم.
🔴
ما مشکلی با رویارویی نداریم. اگر به آنجا برسیم، برای ما مسئله‌ای نیست.
🔴
اسرائیل فقط مشکل من نیست؛ مشکل جهان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/131506" target="_blank">📅 22:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131505">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزارت خارجه فرانسه به «العربیه»: با بریتانیا و شرکای منطقه‌‌ای‌مان برای بازگشایی تنگه هرمز تلاش می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/131505" target="_blank">📅 22:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131504">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
صدراعظم آلمان: ایران فورا باید با اروپا وارد مذاکره بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/131504" target="_blank">📅 22:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131503">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWxDjx-tH0eESx-DL1kn1aBHozNP_oT_j1bQRkU7i5eJJr-d2P8NGx33H3m8z8Tr96E5cq3uW6SCetFsKn7CAiYy-yIW3QRAufi_0hHrXFKSRy-lDcZvl4pJQfeSN0yOl98XtRLJDQjgY46vmopinDI7yl_Pt9QBg1wbgzQb8ijt75RvlMTdaCUwmeq_21v9rQUWceA0hbM174hIuDLj9xcn3vFig0JhpXrcZWrPhxSt3mscx9_Si350OkD5SyAZgxATgf5uqKpc9q6oM3AtLS104ygEYGbih3IhLhnY3pHvaFAR4s89Xl2kYR1hxspl6TOvWKaOqHNtkoBgq0sGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم پناه: آماده شهادتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/131503" target="_blank">📅 22:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131502">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر خارجه ترکیه، فیدان: هم رئیس‌جمهور اردوغان و هم رئیس‌جمهور ترامپ تعهد قوی برای لغو تحریم‌های کاتسا دارند.
🔴
در سپتامبر گذشته، این دو رهبر به‌طور عمومی مواضع خود را در این مورد بیان کردند و ما به عنوان وزرا دستور داریم که این مسئله را حل و فصل کنیم.
🔴
من معتقدم که لغو ممنوعیت فروش F-35 به ترکیه پس از لغو تحریم‌های CAATSA رخ خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/131502" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131501">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
به نوشته فایننشال‌تایمز، کشورهای اروپایی که اجازه استفاده از پایگاه‌های آمریکایی در کشورشان را برای حمله به ایران ندادند، ممکن است در همکاری‌های نظامی آینده میان آمریکا و اروپا با محدودیت‌هایی مواجه شوند.
🔴
فرستادهٔ دونالد ترامپ در ناتو گفت آن دسته از کشورهای اروپایی که بودجه نظامی بیشتری داشته باشند، امتیازات بیشتری از آمریکا دریافت خواهند کرد و آن‌هایی که دسترسی نظامی آمریکا به پایگاه‌هایشان را مسدود کرده‌اند، باید منتظر مذاکرات دشوار باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/131501" target="_blank">📅 22:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131500">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
روسیه: اجرای کامل تفاهم‌های حاصل شده میان ایران و آمریکا، ضروری است
🔴
در پایان هفته گذشته شاهد تبادل حملات شدیدی بودیم که می‌توانست تلاش‌های دیپلماتیک در حال انجام را تهدید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131500" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131499">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل: در بحبوحه مذاکرات دیپلماتیک، ایالات متحده همراه با اسرائیل دوبار به دیپلماسی خیانت کردند و در نقض آشکار منشور سازمان ملل متحد و قوانین بین‌المللی، دو جنگ تجاوزکارانه را علیه ایران به راه انداختند.
🔴
این تجاوزات تهدیدی جدی علیه صلح و امنیت بین‌المللی به شمار می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/131499" target="_blank">📅 21:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131498">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FptjOcpP1hq3wClGemYf2Tz9h-ztmI1Nq2kPHWN27RJ3bG3MPxLF14ERo9qnpY7cBB1oMb-HAIHs0nO2TAYEqAIxSKI4INorZq1dmN9WmqYk-hweNt4Vl2DSicK4QOXEDZ265JnANL6vwtkqXmXn9mn6BAu2UvTo8lKK8ojLv6X0PsVVXsCnA_wOZg99yppdBgCbv2446zMElhS9WPldZdkJ7WygRzikXw_hoRec6Bc7eWMcQw-Ee_H31VueXAm7uR5-idNATW8LEjr970-VZJs2USsw6U4rGOARAZR1mCrARXkzW49E6dHGKaFIfMfTeDgL01LuKHvY1nTYU8f2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روسیه توهین به پیامبر و قرآن را ممنوع کرد.
🔴
این قانون با دستور پوتین تصویب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/131498" target="_blank">📅 21:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PDGY1qwHGUaqlC9WefjEOaqpgN7QQyT_cpRqlxImXuRzSu3PI-AZZiUOyKrNQcTNOMw8xUwbBqHRMz7ZEXVPSBRmAix9LXPQNcsEDthw3wwTtZPAbh0BkluLro12IPt82Nt78qBk-ccJqfxzqLtCXexxaeTNlNfZDI1CsD4YzmckzbFO5UYGVc1cKzJF-gZ6T02O43pGOoAd7zjIiZU5cY9-Atqxi8OfkY-GKszPCUXq8rj6L8e_bLSixkc9aGSQcTgeUerpXkEC-wlB0O1iaFDXD4Lo4Qv440DxYai4vKsu456cUwSnK_5I2Cy7r4sCaXaje9u8Tw2Wm9z5XVJ4Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه حزب دموکرات کردستان با انتشار تصویری به نقل از مصطفی هجری سرکرده این حزب اعلام کرد: در شرایط مساعد تا ارومیه پیشروی خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/131497" target="_blank">📅 21:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUTA-Y_CmcaPQ0jKjFiCA6f9TrfC_8kTj_28fmr3cDxUQLpoTz_S6ejCXz0vSlWmxonVNC3qZwco-WDAVOYNHr7qOhBdjvUT1k4tRKEqj91jAcKT28tcNeXHf0UdGMbMJxwEpoO79ZmEwyy-cZqsSHa_ssBFUEaH3VcBvm3bQhHtlCOBr8zLejrLUBSfWY9Bxau18WBNKo9Z9B_pfJIsf0LhruAqt6eBFrdyAEyt6viJGJ0ps01Ggb_OO6_JAjrgEb9rDrlylajub_8NYDf1cfiGPRU-Rtm49wauycbmexSDyJuJUoKJz717bE3IZPI-1lfNtO9wgyqkg7OmDZhAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
بیرون بروید و در انتخابات میانه‌دوره جمهوری‌خواه رای دهید، زیرا اگر کمونیست‌ها وارد شوند، دیگر هرگز ماهیگیری نخواهید کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/131496" target="_blank">📅 21:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e3603b94.mp4?token=JqVIW7m6PXOH0-_iVWkPVRxgC7Nv5TTUZ7GYcaT6uyOie30JiQdSpnYpfvfMpHPKGfB8lT4NUnOZIecpgO2cLZt-zHJMg5FT9HNJUr8VHIA1Rtez8hnJKQjaUeGD8eQmvjv-OS1fnN0gciEUQE04so0sO3XQrI-QagA2IimyS1ekUDS0mZGRgQPcqwKtsKwKx0LLGW9_D89iye9mToeZU8HK4K4vKOA2s8fftLVrYwYPPezQBNXlGuEVo2JsIXEd1uLx3t0rIhFJyhBqlnJK17ss03NYH5_gliK6buKy7VM6fRBRL3nVcJSX4tF1wk5m6zrLAYHGirGxg-yHKHQQnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e3603b94.mp4?token=JqVIW7m6PXOH0-_iVWkPVRxgC7Nv5TTUZ7GYcaT6uyOie30JiQdSpnYpfvfMpHPKGfB8lT4NUnOZIecpgO2cLZt-zHJMg5FT9HNJUr8VHIA1Rtez8hnJKQjaUeGD8eQmvjv-OS1fnN0gciEUQE04so0sO3XQrI-QagA2IimyS1ekUDS0mZGRgQPcqwKtsKwKx0LLGW9_D89iye9mToeZU8HK4K4vKOA2s8fftLVrYwYPPezQBNXlGuEVo2JsIXEd1uLx3t0rIhFJyhBqlnJK17ss03NYH5_gliK6buKy7VM6fRBRL3nVcJSX4tF1wk5m6zrLAYHGirGxg-yHKHQQnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی که موسسه کپلر از تردد در تنگه هرمز در ۲۹ و ۳۰ ژوئن تهیه کرده است. همان‌گونه که می‌بینید تردد در هر دو مسیر ایرانی و عمانی همچنان ادامه دارد.
🔴
این نکته هم قابل ذکر است که ترددهای ثبت شده توسط کپلر شامل ترددهای با AIS روشن می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/131495" target="_blank">📅 21:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/وزیر دفاع اسرائیل: ارتش اسرائیل باید برای انجام جنگ مستقل علیه ایران آماده شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131494" target="_blank">📅 21:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در بندر امام
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/131493" target="_blank">📅 21:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
زلنسکی: اگر شرکای ما آنچه را که وعده داده بودند، به موقع تحویل می‌دادند، امروز می‌توانستیم خانه‌ها و جان‌ها را نجات دهیم. این یک مشکل بزرگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/131492" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا: مهلت ۶۰ روزه برای مذاکرات بر سر توافق نهایی میان ایران و ایالات متحده باید به دلیل تبادل آتش از ابتدا محاسبه شود.
🔴
احتمالا جزئیات مربوط به جدول زمانی مذاکرات به‌زودی منتشر خواهد شد و کنگره آمریکا نیز تحولات را از نزدیک دنبال می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/131491" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rycyb1vcX6Lc_mMWFETNFtsdRhe01vVKAZz56gcSyN2ttlDJIwwfWzVZ-S2UqKsAnJFd9BV1bLcvXFEkrYMVePns6koy9dHYj2hhZUUq8TTD5C6hGFuiKGGgjaed3M80sWDvrCirZB482pNaL4xFOZXXc6D1199dcbwzA8zQPtBVlauK0HLbcY7Va-XAfKYSDLbcmUtOir36Dh8wibUEBB8FshxbVYxuw3B4zS2RXeZ5aiPbidRv5ignAig0Ow8hqQMFJPyFXiIWDQEKlgFBz_M3oco-oHFmlh4w6gowbVvvaL_SkdAqsSqza176n3lfD1G68HeM67Mo6vqCfZIluw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جبهه پایداری:قالیباف مجلس رو باز کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/131490" target="_blank">📅 20:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
یه بشقاب پرنده داخل فلایت رادار تو آسمون آمریکا ظاهر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/131489" target="_blank">📅 20:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
قائم پناه، معاون پزشکیان: قرار باشه هرچی رهبر بگه رو اجرا کنیم که باید در تمام نهادها رو ببندیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/131488" target="_blank">📅 20:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzBP5IxL3woOrSW9M72noL6QTo500BCVBXWxMfmbUuqDiRg3eOioQjVhT8JLGf_C6ar9WEYCXMLBhM-fL2ctedwx-PJYuKfYTUkfoB5w3u8G8fPEZGYd7kzu0sUdPC3xkpvNE5429dmPYSXX_UvYumaKroB-7hMvTbazlVDp2BND24ZdI_p3KpfwAb3rAyOQTrxkGwUM2SvZ4jO9T-9xIxAyi44cQWROUfZwEIpMsKlFDa8PKcCCIyky4e_sRbj12WaGv9n6HsEktSQ30tMus15vgoTdFiA3fH2u4_U9SBDsXA7ViVWr_kZHjSm-RUugqUlok7wFDdYJAtDocWyv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه بشقاب پرنده داخل فلایت رادار تو آسمون آمریکا ظاهر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/131487" target="_blank">📅 20:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131485">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipEglZg9xVwXE-560UCp370NOlH-ZQeg1IzX6eTJZnEcvUIWb14QIqZcTBk0mo7wNoyQFNzuh10mkz9BO2iCIf9T2fTupsSpP693UYUVr2ZSSwgcKH393-vCPqiSZAfZwJ-usx6ceJKZ7MHatQ9ne8pZ87JMqLpuczjJARtR4ItHyNinucfIBrFGrFejH3u99qmpMvLDPs1pYWEuG6qQxthj7JlyDcob9-hyrev6Bm1tsxxRH8swNSru4Zp57EKpvByySuyA-1rKTA0FL7SOn_TJp7Jm1Senovp0F6cOZ2gOC2UE50Q9j07roDBuiL7zdZIgySvzKozwyEaJuZ2LYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار بزرگی در اطراف منطقهٔ کونین الطیری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131485" target="_blank">📅 20:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131484">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317cc5baf7.mp4?token=iBIolumvIS4p4628lJkn7qrPBQgxYqrMJ2jLjkArkdaPnTHu_jTbMLwVE25ymTF_2Eyol7uJBqYEkLqOe0OwrN00Td20-6mpnPecS_kouV7NgerCr0Mr5W4dnD0HH3eNfPUTwdZZtc8af8_cWykS915I2HkpumwcslUqPUwCykRAEp-dgrwel1QJhN697oB84hRjg27UTnz4GaG0hWoWL6g0l3AERO_lAkxlRXPnP5MH2IlLeD5NTK_WjUr4nE9zn2ONcDWU9YBj-4g82kLD7cdKzE4cZtJOnNYqmBgIUq_k7DHUD4Tw-1VjROPrGXhUpQbrb6bvY4CTfyWVlcqFboi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317cc5baf7.mp4?token=iBIolumvIS4p4628lJkn7qrPBQgxYqrMJ2jLjkArkdaPnTHu_jTbMLwVE25ymTF_2Eyol7uJBqYEkLqOe0OwrN00Td20-6mpnPecS_kouV7NgerCr0Mr5W4dnD0HH3eNfPUTwdZZtc8af8_cWykS915I2HkpumwcslUqPUwCykRAEp-dgrwel1QJhN697oB84hRjg27UTnz4GaG0hWoWL6g0l3AERO_lAkxlRXPnP5MH2IlLeD5NTK_WjUr4nE9zn2ONcDWU9YBj-4g82kLD7cdKzE4cZtJOnNYqmBgIUq_k7DHUD4Tw-1VjROPrGXhUpQbrb6bvY4CTfyWVlcqFboi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیم های جستجو و نجات کاستاریکا مجبور شدند صبح امروز جستجوی ساختمان در پلایا گرانده را پس از نگرانی از اینکه سازه در معرض خطر ریزش قریب الوقوع است، رها کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/131484" target="_blank">📅 20:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پزشکیان: نمی‌توانم ببینم مردم مشکل دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/131483" target="_blank">📅 20:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پزشکیان: دغدغه ما مردم و نیروهای مسلح هستند.
🔴
من هر کمکی لازم باشد به نیروهای مسلح می کنم.
🔴
جنگ بود، ماه رمضان بود، عید بود آیا کسی  احساس  کمبود [کالا] در کشور داشت؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/131482" target="_blank">📅 20:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131481">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پزشکیان :  در مورد مذاکره رهبری فرمودند اگر سه چهارم [شورایعالی امنیت ملی]  رای دادند مذاکره کنند.
🔴
از ۱۳ نفر، ۱۲ نفر رای دادند.
🔴
نه تنها رای دادند بلکه دفاع کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/131481" target="_blank">📅 20:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131480">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=BxD0PFjkuIRl6Jpdv4sDBQO3pdCnoZARA6svs7wMlUzSwhdqejHxqnd1N6lm-FzOHePC8ywBZzNfyc3wlX8pc9WIjynLYWbKx3XVK4uqnSc30-AnHoZl3BZI9B_iCypZPXcEt8dRg3fzhk93Qkaqcoa1N-aRwZ7Kg95P3K-oSGaWKe9q_NV0KcLXR0v4_cN0J33bliFC0jpudiFzvVS26ACJZCaW9JgAxkqQ-k1rrqHps6-Mc2v9MzfwoDga1iqFqEiIAdqLQCZT-Mv1yYZdk3z_NtdYFn-lE0WFUyhEyrCo3SF8ZCCoXEINCH5tHcJ8wIAxLU_MkggGjWEW3hLVQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=BxD0PFjkuIRl6Jpdv4sDBQO3pdCnoZARA6svs7wMlUzSwhdqejHxqnd1N6lm-FzOHePC8ywBZzNfyc3wlX8pc9WIjynLYWbKx3XVK4uqnSc30-AnHoZl3BZI9B_iCypZPXcEt8dRg3fzhk93Qkaqcoa1N-aRwZ7Kg95P3K-oSGaWKe9q_NV0KcLXR0v4_cN0J33bliFC0jpudiFzvVS26ACJZCaW9JgAxkqQ-k1rrqHps6-Mc2v9MzfwoDga1iqFqEiIAdqLQCZT-Mv1yYZdk3z_NtdYFn-lE0WFUyhEyrCo3SF8ZCCoXEINCH5tHcJ8wIAxLU_MkggGjWEW3hLVQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور
پزشکیان
:
من به عنوان مسوول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
🔴
من نمی توانم دروغ بگویم
🔴
این نیست که ما مقابل دشمن کوتاه خواهیم آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131480" target="_blank">📅 20:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131479">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نماینده پاناما: از ایران می‌خواهیم به قانون بین‌المللی پایبند شده و تهدیدات خود را متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/131479" target="_blank">📅 20:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131478">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
یک عضو ارشد حزب الله لبنان گفت که مقامات لبنانی باید از سازش و خدمت به پروژه صهیونیستی در لبنان دست بردارند و فرصت ایجاد شده توسط ایران در مذاکره با آمریکا را غنیمت بدانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/131478" target="_blank">📅 20:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131477">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26179bf871.mp4?token=oQz2cIjvGSwmhbgq3n-CG6n4dDyLGwcwxHSkLQiTyx3TEv19SngCfWcjwHVdIMz5q2bu5yrGIFiS8NWV19-fJb-30twwLgkJGvt1LGcMGx7dr1vi4cF6i9KUp40mFcf6goPdpW5Lw89Spt3VvudMAPIzYQYZttZwy3QS1K9c99jOnbUCxy0yWjLC5LGmWKrzqY66fLsPl3HlfXyqODC8Xv1zCit-p4yDbmMBXckEwpvuej8OpkyBIppcg0rLMw1teXFBHSILqWgSSCalcjF_i0BwiBREIV4UuiMyjarPvxa0QjJ9yclGSfJ5tf3n62d2Sjr_5LN23nRYERUGF4qhtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26179bf871.mp4?token=oQz2cIjvGSwmhbgq3n-CG6n4dDyLGwcwxHSkLQiTyx3TEv19SngCfWcjwHVdIMz5q2bu5yrGIFiS8NWV19-fJb-30twwLgkJGvt1LGcMGx7dr1vi4cF6i9KUp40mFcf6goPdpW5Lw89Spt3VvudMAPIzYQYZttZwy3QS1K9c99jOnbUCxy0yWjLC5LGmWKrzqY66fLsPl3HlfXyqODC8Xv1zCit-p4yDbmMBXckEwpvuej8OpkyBIppcg0rLMw1teXFBHSILqWgSSCalcjF_i0BwiBREIV4UuiMyjarPvxa0QjJ9yclGSfJ5tf3n62d2Sjr_5LN23nRYERUGF4qhtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هجوم فرانسوی‌ها برای تهیه پنکه و دستگاه‌های تهویه
🔴
مردم فرانسه به دلیل گرمای شدید برای خرید پنکه و دستگاه‌های تهویه مطبوع به فروشگاه‌ها هجوم بردند. فروشگاه لیدل پاریس به میدان نبردی بر سر پنکه و دستگاه‌های تهویه مطبوع تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/131477" target="_blank">📅 20:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131476">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وال استریت ژورنال:  ایالات متحده به ایران پیشنهاد کرده است که در ازای باز شدن کامل تنگه هرمز، بدون دریافت حق بیمه، وجوه مسدود شده را آزاد کند. در حال حاضر، ایران به این پیشنهاد پاسخ منفی داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/131476" target="_blank">📅 20:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131475">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iVPs2bTP4b6f1bbaJ7aC_-GF7UPHw3_D57fDExoJWDzQaJ4PBsDeSri-RJABnWGpMgzieQMFFk7FpBBypxPZonkt22ga5GzAI7Yqh_EEj7Le7DpVDkbywWGpmALvrHbBhLxljOO5j2i2DwAThFrVinb6LypsvuLXeJVpyaGLAhFghsR8mQZvMwueY5SfowsegvH8NeKGB1MN5IzrnTW3Xi30kwAyBL4BkFCXcwuytPugRjvY7CbQwCielaN8CDD2IK17g9ItqkUDTBBfxXzwAmLcx1mJkFimqClqpGqgur4BmxveSxz-LFM7s5-qKRl_xT-hsZ6VrCWWkUI3OijZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روز گذشته ۳۸ کشتی از تنگه هرمز عبور کردند که از این تعداد دست‌کم ۷ کشتی در مسیر ایران و ۱۶ کشتی در مسیر عمان ثبت شده‌اند
🔴
۷ کشتی که از مسیر ایران عبور کردند ۶ تا ایرانی و یکی عراقی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131475" target="_blank">📅 19:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131474">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOkuoD5qxECsFv9yN1X4MEtugGmP0xIptWifpfdFdRgpQWU4m8Et3XyDkft1U570G26GA9TYg4yfdTZp9Ho9q9evSub-pWYW4lzlc44PK9oucdX9iv28_NL6-we2FvrUI21L82GbsrClgUz5h7tHslvGdppeK8Cwn_Yqtxm18sH8tT05LmdjQ8FwEcVXJc8Mcq8EkXMSybZQFzAhKJwF_Xs8yxuFzqBcmD2JLY_2saaHsgOa8LsKoKvwyfYV0bk7ZMRXWsgIyLgVRXqYoHPf4ea14aXRytnLgrXcZs95X97uoojqwaW_IxjSbGca0fEbOP_Xgn-ijxePbea2jtg1cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس:  ویتکاف و کوشنر تلاش کرده‌اند تا به ایرانی‌ها بفهمانند که درخواست آنها برای عوارض می‌تواند توافق ایالات متحده و ایران را که در نهایت برای ایران بسیار سودآورتر خواهد بود، از بین ببرد.
🔴
یک مقام آمریکایی گفت: «پیام ایالات متحده به ایران این بود که «بزرگتر فکر کن».
🔴
این مقام ادعا کرد مبالغی که ایران می‌تواند از توسعه و فروش آزاد نفت و سایر منابع - در صورت لغو تمام تحریم‌ها توسط ایالات متحده تحت یک توافق - به دست آورد، «برای آنها ۱۰۰ برابر ارزشمندتر از استفاده از یک تاکتیک گانگستری برای تلاش برای دریافت عوارض خواهد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/131474" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
