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
<img src="https://cdn4.telesco.pe/file/RI29yuMDmhC8nT-RFW5gqbtpq6Cf8qHj6U33ZayAbSr2eRvMmm-uDabdzA0nls_MoPaTN8HfAQ0T0nICRhnfAXdmw8cqe8BjqvtqiKmbhmLpVYRfNwCuU6wlHVphyImd6VRHpCjA83BFkcOahU87ZxABa0-irkWrd8z01eMP3Z58M8vlwtcDZojDQbt_wCdZXSj5-FXkO6_2g8idHZTkSHH2oNJIYgVuFJ4je4fBZrua91cCQyq8zIipygSXWUJCCAwBdJSyHOnb5sn54A7p1wxHr7NmsYlgkHtuKboXG2czXXKwXXq_5DIMpNAnpvv-tNgZ22nRtg9FZ2DWm--wYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 495K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 04:57:01</div>
<hr>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شبکه ۱۳ : ترامپ و نتانیاهو طی هفته‌های اخیر، در پی گزارش‌ها درباره بازسازی کارخانه‌های موشکی و پهپادی در ایران ، گفت‌وگوهای فوری داشته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/withyashar/25465" target="_blank">📅 04:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hK03Xg2VoRicEURmoFqTwMIVQ2AlVLsX7-NYofaH02RMmMK2SuA2Eee1QrZ72NWJ3SPQT9eQdPKSu1mvQK_ZVFa6xDecA-NWCgYmYArsq-GjofDs9b-D5CfnHhi3L3MZPp8AQGb2fG8ziPYAljjnQeqlh4eRvRM-R4w11u1pHDnUp63UsiPrUOIvXyGdJQnNSlgLJdAWwLawOn1LEV3vszUwb7gLe_E1G7BtR9l9EieE6q_7hU6h10g72fOBJe6cBXHj3o7kpdZATwZUj7RVkhO-SAEJKgXBkbmRcvkzT3IJTdm5q5n2poR9dy7IRXSqmwxN4mDy-i7dhzk7_MvZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله افراد مسلح به پاسگاه مورتان در بخش پارود شهرستان راسک و درگیری شدید با نیروهای مستقر در پاسگاه گزارش شده است. بر اساس اطلاعات اولیه، درگیری از دقایقی پیش آغاز شده و دو طرف به تبادل آتش پرداخته‌اند؛ تاکنون جزئیاتی درباره تلفات احتمالی یا وضعیت نیروهای پاسگاه منتشر نشده و هویت و وابستگی مهاجمان نیز مشخص نیست. این حادثه در حالی رخ می‌دهد که طی روزهای اخیر چندین مورد درگیری و حادثه امنیتی در سیستان‌وبلوچستان، از جمله زاهدان، سراوان و ایرانشهر، گزارش شده است. جمعه گذشته نیز سرهنگ زن نصرت افتخاری پودینه، معاون فرهنگی و اجتماعی فرماندهی انتظامی استان، در انفجار بمب کنار جاده‌ای در محور چشمه‌زیارت زاهدان کشته شد؛ جبهه مبارزین مردمی مسئولیت آن حمله را برعهده گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/25464" target="_blank">📅 03:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a2b70e41.mp4?token=ulRHHvIYJf_sObIwGFNtElhqdxsI9tKTB0TX0TpQYTj-zBo7HueiDaIO1y6UVO2frMclyId-wDDxAcbOFm6-ZGTA5lLQGzo_yM7lm-ImKmHjbEZzDwmOMDjcTpqG3m5Cm_ZmFPqJbI5d2sQ2fe_pvLf76RoaU_fB09Ijua7SYUfBDymzwRqkyAJfgqJ8ombZIgPb0FUSy0KqtXDcDEaPvld5t0ATcPEZrwH3ALjmuBbbFU6x2fSCc28gOFQorWyco5hvoF-uUYIW9OmJIFJxif-fvKp5zxOr0aqXKjsoAKXHhxnuX5e9owMXOXTnNOAI9V7JbkxmnNsJU57UpF_UFjW7_DcToQ6wVZTI8-ThIPdXv-UkugAPnRuI7JSF55Rmg1myPReM1-uWu9QOtqvDzQkVPvOsQmglHjlEAlYtCqDa_aUUZDixxxdjLEWIblrx2W2p5OrJVslRox1KgoDTcsRrX3F1Z-ejHTOYfGzeZCLBVW5uSzIAeKUBYV6uNFm36J_cPsNY4cBhxw3_iy2P89Qw6ruTeDs_gYgd1OdR3tADvp0x1eahU8MvO-6VRs5L8_Z_mHWPFPpdJHWqzvvixHSc8LuK6Tu0ilUCMaIyoEq001QrViqEvpcwjJ3MS5i18aSayryoaWPtwEev1Nc-Ngtf93_F0Q-E_7LRNMTX48I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a2b70e41.mp4?token=ulRHHvIYJf_sObIwGFNtElhqdxsI9tKTB0TX0TpQYTj-zBo7HueiDaIO1y6UVO2frMclyId-wDDxAcbOFm6-ZGTA5lLQGzo_yM7lm-ImKmHjbEZzDwmOMDjcTpqG3m5Cm_ZmFPqJbI5d2sQ2fe_pvLf76RoaU_fB09Ijua7SYUfBDymzwRqkyAJfgqJ8ombZIgPb0FUSy0KqtXDcDEaPvld5t0ATcPEZrwH3ALjmuBbbFU6x2fSCc28gOFQorWyco5hvoF-uUYIW9OmJIFJxif-fvKp5zxOr0aqXKjsoAKXHhxnuX5e9owMXOXTnNOAI9V7JbkxmnNsJU57UpF_UFjW7_DcToQ6wVZTI8-ThIPdXv-UkugAPnRuI7JSF55Rmg1myPReM1-uWu9QOtqvDzQkVPvOsQmglHjlEAlYtCqDa_aUUZDixxxdjLEWIblrx2W2p5OrJVslRox1KgoDTcsRrX3F1Z-ejHTOYfGzeZCLBVW5uSzIAeKUBYV6uNFm36J_cPsNY4cBhxw3_iy2P89Qw6ruTeDs_gYgd1OdR3tADvp0x1eahU8MvO-6VRs5L8_Z_mHWPFPpdJHWqzvvixHSc8LuK6Tu0ilUCMaIyoEq001QrViqEvpcwjJ3MS5i18aSayryoaWPtwEev1Nc-Ngtf93_F0Q-E_7LRNMTX48I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور دارلین گراهام (خواهر لیندسی): اسرائیل متحد بسیار قدرتمندی است و من کاملاً معتقدم که باید در کنار آن بایستیم. همان کسانی که می‌خواهند به اسرائیل آسیب بزنند و به آن حمله کنند، به سراغ ما هم خواهند آمد. تروریست‌هایی که به دستیابی به سلاح هسته‌ای نزدیک شده‌اند،( جمهوری اسلامی ) به آمریکا هم خواهند آمد. بنابراین، باید از قوی‌ترین متحد خود در خاورمیانه حمایت کنیم؛ نگران دموکرات‌های سوسیالیست هستم؛ زیرا در ۷ اکتبر، زمانی که حماس بیش از هزار اسرائیلی را کشت، دموکرات‌ها در خیابان‌های نیویورک به‌خاطر کشته شدن این افراد جشن گرفتند. حماس گروهی بی‌رحم و شرور است.
@WarRoom</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/withyashar/25463" target="_blank">📅 03:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">طبق گزارشات دقایقی پیش یک نفتکش در مسیر جنوبی با پرچم هند در تنگه هرمز توسط سپاه هدف قرار گرفت؛ دو نفر از خدمه مفقود شده‌اند و ٩ نفر دیگر نجات یافته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/withyashar/25462" target="_blank">📅 02:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25461">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faSyzEWDZaI2yAe8M3nYnxZSRMftaJxDgykLshyVLLMoyXnM3pYdx_UX4MEg4SBEeFYBUQ8_AGQFhofaJGY0xNU7RgUQC7C8NB1NTlLVUl_57Mo6MEc2gY3V_VPMmxvuaqTn0g5ALAmLArf454YGtFCh_0VcNGTuBw0vJd3pX83GqWP7rjnrIsVyjLBuT-T-OMndXD5aKwNlzl7YIrl_Tc3u1dqfgAUzAoGkx1_Ra6ZwrI9EnBb3bkBcw-d6CSlGnVfSuvaLKXl6BZPxt0aBwGjbeck16qi69rQUWsZyQsUiD83IL1CX6cHO-22QFLGPQ1qJwxWLAQpx-5lMuC5RBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با بازشدن مارکت ها قیمت نفت برنت به ۱۰۵ دلار افزایش یافت
@WarRoom</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/withyashar/25461" target="_blank">📅 02:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZXLtLDYeE1ECnNx0RTEcfrjjM_gVr7tDXzDoFtRhG22vsxku9s1FgaEkd0NAJ9GgEgsV7vVuVUO6MGFvFbAN_5cTRrDUKV7HH2yPKKqWo0_f6DtG3EImXg2P37aNkw4MKa5_6Lxtr1lM582VkXbDsoKTDV0s7dhCU4SRkqr3RuepNBCfSYcRkRTdcPCV_Ufj3pKjPtjlO8vVGoTGVF6eA3fyHU3Vl3GibyrrzX9JayS_4gki6NTAm1MfSdmIQ1g8E6GU-GSE8RrYymxCUN5PHB_2QTo0de0XTB5IgYcvNbQx8yFkcUpb_hDbdVCAvcvJds9B0ODXZYgQWiF1Fo4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاطمه مهاجرانی، سخنگوی دولت : پروژه ایجاد ترس از ایران و تضعیف روابط این کشور با جهان، «افسانه‌ای است که دشمنان ترویج می‌کنند» @WarRoom</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/25460" target="_blank">📅 01:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYDq2l-xIYeu28v6Jyl2-bdScmzUQRKepcQlEnU4IrzNpWUnfy3jBujlqFnRXWoahqv95hRIYUHKqfPp89-_EwD7jZWpC2n6oCxiq6LudOnCd5JofaX33EL9J2CJSfqesYC2PpNtR8ZKOwwU3dOOdJhNImj2FwbGX7Z6selcuw_yAwWv-DF25ARbY4gNAyTkrOULtZoNO2ZAL8Dt_7otJhYRa9DZih3SnEMn9kJbr5Jo0ZiN80-StwafiWC4ovdnUs7KRmpwAUR4dmnoNXGBas_kLc7vSD5pgT8aILEHUQtclpLqy3MzU_U1gchwiv0yklbXAgSOgH84oySluHnQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند جنگنده چندمنظوره F-15 نیروی هوایی ایالات متحده (USAF) در حال پرواز تمرینی حمله به ایران بر فراز عراق مشاهده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/25459" target="_blank">📅 01:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25458">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyYAiN4oyNbjh8zMFr8mFMaaFlVWFUKHDofnouYjglDF2Y3sjU0cugaCMivkY3f6WR-4v1C7bLGFrtAgJFx9UFaEBHfatvCU6PoDblyXVDVhDX42oLybupK1fa5iKKE5HPXfVzSWk32dq3rkcjztdyf_pf3FibrbPck6n9GJsS-8RxeI9jDSi0-FH345PYa3vrC04O1tdNc4fC_eH0pzPkdUbN5-_mgb3nMGzRtufhr1Dp7NofP7K5_iFLvsaA9tnWafR_LI0vAOAy2tdNjBNzhxLIaYNElze8ZW_gbHnW5UJp8WUnv8A83QNtmEdR3GbGaeGKeeOL5bQktJjDPUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای برای یک نفت‌کش در نزدیکی لنگرگاه «صحار» در عمان دریافت کرده است.
پس از تأیید اصابت یک پهپاد (UAV) به نفت‌کش، UKMTO ماهیت این حادثه را به «حمله» تغییر داد. مقامات محلی در حال همکاری برای تخلیه خدمه هستند؛ با این حال، در زمان این به‌روزرسانی، اطلاعاتی درباره میزان خسارات و پیامدهای زیست‌محیطی در دست نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/25458" target="_blank">📅 00:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گنده‌گوز منطقه کنترل بخشهای زیاد و جاده‌های سیستان و بلوچستان رو از دست داده
@WarRoom</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/25457" target="_blank">📅 00:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ممجواد ظریف : هرجور شده باید با آمریکا توافق کنیم. حتی اگر عین قرارداد ترکمنچای یه جایی رو هم بدیم.«ترکمنچای امضا‌شد چون بقا درخطر بود»
@WarRoom</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/25456" target="_blank">📅 00:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترابری نظامی وحشتناک آمریکا از ۲۴ ساعت گذشته تا همین الان الان. شما فقط سرانگشتی حساب کن، اگه اینا خالی بخوان برن بیان، میلیون‌ها دلار هزینه داره. ترامپ بیست دلاری رو چند بار چک می‌کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/25454" target="_blank">📅 00:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فایننشال تایمز : آمریکا تهدید کرده که جریان تسلیحات به اوکراین را از طریق مکانیسم PURL متوقف خواهد کرد.
این مکانیسمی است که در آن اروپایی‌ها از بودجه خود برای خرید تسلیحات آمریکایی که به کی‌یف ارسال می‌شود، هزینه می‌کنند. واشنگتن هیچ هزینه‌ای در این زمینه پرداخت نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/25453" target="_blank">📅 00:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فیلم لحظه برخورد موشک بالستیک گروه تروریست حوثی‌ها (انصارالله) به ترمینال ۳ فرودگاه بین‌المللی ملک خالد ریاض در روز گذشته را نشان می‌دهد
این حمله تا الان ۱۳ کشته و بیش از ۳۰۰ زخمی برجای گذاشته
@WarRoom</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/25451" target="_blank">📅 23:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یک مقام کاخ سفید به اکسیوس : ترامپ واقعاً عصبانی است. او احساس می‌کند زلنسکی آمریکا را بدیهی فرض می‌کند و قدر حمایت‌های آن را نمی‌داند.
استیو ویتکاف و جرد کوشنر هم سفر برنامه‌ریزی‌شده خود به مسکو را به تعویق انداخته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/25450" target="_blank">📅 23:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNK1LXJ_ziwGaltx1Io4OYaDynm1lYHSD6ZNLgi539tN_Adz84oPSuEIrn-ruXFcEv7hnhUav3ehOaROlxCbTRNiRrs8IKlqq1Iwwo-VfFwMAdvInZpE6J1HEiGrbe6GmIWtBV1E3vGItlcHrXbg0EpHxJ0xLFelAf3SALHYhdWQzXUuRqtyYO7z6SysUI9H9-w7R0RkPv1IqmaOe5PWLeonPCslpMF6LV0C2DH-pue_o68-BLNbRdCiYQ3946tgFWjzxLgXGbs24Gz54aS3L0Zu3nIamepzxCf-V--UGCWqH1v4xkkpjpT30vLQZZOYvb_d7gulh-Zof8ODT7ELtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جنگ حتمی سوم، سخنگوی گروه تروریستی سپاه با انتشار تصویری در شبکه ایکس نوشت «ما منتظریم»
@WarRoom</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/25449" target="_blank">📅 23:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به گفته مقامات اوکراینی که با شبکه ABC صحبت کردند : خارکیف یک نیروگاه در شرق اوکراین امشب حداقل دو بار مورد حمله قرار گرفت، این اتفاق پس از آن رخ می‌دهد که ترامپ از توقف "فوری" حملات به تاسیسات انرژی خبر داد . پیشتر‌ مقامات روسی هم گفته بودند این پست ترامپ…</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/25448" target="_blank">📅 23:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ورود گسترده هواپیماهای نظامی آمریکا به اروپا برای پشتیبانی حمله احتمالی
نیروی هوایی ایالات متحده در حال انتقال گسترده هواپیماهای سوخت‌رسان و ترابری نظامی از خاک اصلی آمریکا به پایگاه‌های اروپایی است.
حدود ۲۰ فروند از این هواپیماها طی ۴۸ ساعت گذشته به این پایگاه‌ها رسیده‌اند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/25447" target="_blank">📅 23:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آسوشیتدپرس ، بن‌بست مذاکرات ایران و آمریکا؛ تهران پاسخ واشینگتن را ناکافی دانست:
محسن رضایی اعلام کرد پاسخ اخیر آمریکا به پیشنهاد ایران برای پایان جنگ، خواسته‌های تهران را تأمین نمی‌کند و واشینگتن باید موضع خود را درباره موارد مبهم روشن کند. به گفته او، آمریکا برخی از هفت شرط ایران را پذیرفته، اما وضعیت سایر شروط مشخص نیست.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/25446" target="_blank">📅 23:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کاظم دستکج ، غریب‌آبادی: اقدامات کنترلی ایران در تنگه هرمز تا زمانی ادامه می‌یابد که آمریکا به این نتیجه برسد راه‌حل مسائل موجود نظامی نیست. به گفته او، ایران در حال پیگیری ثبت تفاهم با عمان در سازمان بین‌المللی دریانوردی است؛ اما این تفاهم به معنای بازگشایی فوری تنگه هرمز نیست و ایران تا زمان اجرای تعهدات آمریکا، خود را ملزم به بازگشایی این آبراه نمی‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/25445" target="_blank">📅 23:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szeNtTMlAYaXADQJqGpbcB02lFopV4z1WO_FfiDfR-eVm9F-gE-EGDo9IlTVB9s_rnI7YWi6cfI19mXgjncQvACBWIdsS8waXgCOLptJelE4NwOjNnEtvnlRI6onE2dY_MfxIRm1e8fXn16GQjlvHoIOJzUIiuPMNbG_nndUqmRJ8GyNWX6TyLEd2xpIkkGi2XN7a-q1UbBn4bVy_iHHnUyFBXK0VOgpBnWi6JOKrw5r0bbXEnBp1XEWRU-_f0MsTQo8PaVbSMg62eJ4QBjUFpAvZ4AsmH4pku7Lm5JjHSrKE5Fbv5TdMa8KETNCTf5aUOAJ8lkjAMxuurYMxE4V_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمایش موشکی دقایقی پیش
سپاه پاسداران در این چند روز آزمایشهای موشکی و تستهای پدافند خود را بیشتر کرده تا بازدارندگی را ایجاد کند و هم از عملکرد خود اطمینام داشته باشد چون میداند که جنگ سوم حتمی است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/25444" target="_blank">📅 22:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ادعای شبکه ۱۳ اسرائیل:
نتانیاهو امشب پس از اظهارات ترامپ درباره احتمال ازسرگیری حملات به ایران، رایزنی‌های امنیتی برگزار می‌کند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/25443" target="_blank">📅 22:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرگزاری رژیم تسنیم از رصد پرواز هواپیماهای نظامی آمریکا در آسمان عراق خبر داد و مدعی شد پنج فروند سوخت‌رسان KC-135، دو جنگنده F-16 و دو جنگنده F-35 در این پروازها حضور داشته‌اند. این پروازها از پایگاه‌هایی در اردن و اسرائیل انجام شده‌اند و در حال تمرین حمله به ایران میباشند
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25442" target="_blank">📅 22:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به گفته مقامات اوکراینی که با شبکه ABC صحبت کردند : خارکیف یک نیروگاه در شرق اوکراین امشب حداقل دو بار مورد حمله قرار گرفت، این اتفاق پس از آن رخ می‌دهد که ترامپ از توقف "فوری" حملات به تاسیسات انرژی خبر داد . پیشتر‌ مقامات روسی هم گفته بودند این پست ترامپ برای کنترل مارکت است
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25441" target="_blank">📅 22:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCQYhM0FiTzrYGwaxmsqvls3HQz12elxEASmbJ12xAE_AGCoVhUTvj7kz1e2AWO5k7HByN5J6rb_iDi0NSwOJ3TByfD7iCqAa4qAaGvLZeo-ZkWx0N5LwLQBitAqsgbgvL0xJd6XPrpzw6ENs7VvLlpbI03wTPoSK-5eg5GHCDW7O6Cf0z7C7l-DQOirqhmbZPmuzzwRD9h0mGH1AdTT3yta5O66PloQqi3CZeSB-LPfe9Tt2cEJnl0sV9OrH_gH12TfgkEqQSkog8gt2DVYAr4DibL2oqTIca2W4jEKG11lDz1_im3zV4l6QeZMFV7XrmvyVVjDgAZsPJNve3IB6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرمشهر
😁
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25440" target="_blank">📅 22:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghiPQgN1Ee5FppvIUgPTWbl_4Xpvqm2y7xTFEDXZysMTMCIaK9NkL_iz37NlBsN4kkh5oQ5i3RtmPLzRu1dVIWcaNZpQtxzgcKCdX7oX6Emu-hKuC1aFO3kDxTs1RBcgtKVS5fpIaOEINQBN8kRZ9Vo93zI2BsO341ER3cH6Q5H-vMwiuIfTLaFYz_g7EoaSaCkOx3bVHVA_ZC8ZoXsNCpE7qfU1aRasPXXCV8HWoR3pq9Kbq2TtFaL0jBc4f8icqA5WJSTMnoFA5kBJYF3zbOsV89pQDhKVmCJqpYzdaAuB_qpRDy-onda7FWVjT6TQrY59s723HafV--_M40-nPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تبلیغ فیکه مراقب باشید ، فقط هی روش الکی کلیک کنید اعتبارش بره کار دیگه انجام ندید
🤣
🙌🏾
⚠️</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25439" target="_blank">📅 22:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
گزارشی درباره وقوع حادثه‌ای برای یک نفتکش در نزدیکی بندر صحار عمان دریافت شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25438" target="_blank">📅 22:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فایننشال تایمز: به دلیل حملات یمن، مدیران ارشد شرکت‌های نفتی شروع به ترک کنفرانس جهانی نفت (WPC) کرده‌اند که قرار است در ریاض برگزار شود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25437" target="_blank">📅 21:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25436">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db3e49ede.mp4?token=j2HQMWYUPaSJy3ihD2OY3BAHbeiUFdpvP0bywNz6AuBgysySDVLzNCbeOlavJzxfnSaywTvHXKefekk0ZHmGoLvnRqChA7ZRtNGZrPOZvkL7EhboDLEElOGw-ncfcsixQY5DuP_OhRAOPxT04eUh792p0NKYIi5rHlD9YoyBUDM-zcGCBrA3C6Tgkp-TmGv_svbp47fPNEbtwQ9QLR3hBJftJdpC7W3qhPahumKb7CUzxC0b1DE9e27zRaQphBcd3kx639DxKFsDvEYOW41pko_8o-wZlLzRQ2ZvGLKtV6NZ-DWwjwBbmS5lDyA05FVNGJPwEdX5pZ975jJnUOZ0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db3e49ede.mp4?token=j2HQMWYUPaSJy3ihD2OY3BAHbeiUFdpvP0bywNz6AuBgysySDVLzNCbeOlavJzxfnSaywTvHXKefekk0ZHmGoLvnRqChA7ZRtNGZrPOZvkL7EhboDLEElOGw-ncfcsixQY5DuP_OhRAOPxT04eUh792p0NKYIi5rHlD9YoyBUDM-zcGCBrA3C6Tgkp-TmGv_svbp47fPNEbtwQ9QLR3hBJftJdpC7W3qhPahumKb7CUzxC0b1DE9e27zRaQphBcd3kx639DxKFsDvEYOW41pko_8o-wZlLzRQ2ZvGLKtV6NZ-DWwjwBbmS5lDyA05FVNGJPwEdX5pZ975jJnUOZ0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفت‌کش منتشر کرده است؛ نفت‌کشی که به گفته این نیرو، در تنگه هرمز هدف برخورد مین دریایی قرار گرفته است. @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25436" target="_blank">📅 21:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانال ۱۵ اسرائیل : تحولی در تحقیقات مربوط به پرواز تروریستی: سفارت مالدیو اعلام کرد که دو خلبای دیگر شرکت "فلای دبی" دستگیر شده‌اند. به احتمال زیاد، این دو نفر در همان ساختمان با کمک خلبان تروریست زندگی می‌کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25435" target="_blank">📅 21:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f5401b52.mp4?token=TTO2KysPU9ZDTz0Mo9y-hG00SBFW963X6RmyW72WDVIrjdrqcIeyKRgYHC5EJvAK2zC_6M951gnbSdv7-rel_XviUxwrM7tJ3oicJno95nCJokmF1PbuDIkB0ePzwNGxjcbWaYAX03xA-8OP416wsqt1sZwPFysJt0K1Rpo2Wf7zufkph8dKwFi1fqvkaT1gbdO0yq9fpOpUapuBf6DRVQcge2QrGgFsukYvl7C3SxkfK8FbeSDqQM_FoQKLSSzfSBlnjRqhLvqrSnHTck_BJuKBtTJjgqfualknoSBJalsuuxPVQXlknAPPEUm2OUVtyZtvy3bj0653i33vpPSYjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f5401b52.mp4?token=TTO2KysPU9ZDTz0Mo9y-hG00SBFW963X6RmyW72WDVIrjdrqcIeyKRgYHC5EJvAK2zC_6M951gnbSdv7-rel_XviUxwrM7tJ3oicJno95nCJokmF1PbuDIkB0ePzwNGxjcbWaYAX03xA-8OP416wsqt1sZwPFysJt0K1Rpo2Wf7zufkph8dKwFi1fqvkaT1gbdO0yq9fpOpUapuBf6DRVQcge2QrGgFsukYvl7C3SxkfK8FbeSDqQM_FoQKLSSzfSBlnjRqhLvqrSnHTck_BJuKBtTJjgqfualknoSBJalsuuxPVQXlknAPPEUm2OUVtyZtvy3bj0653i33vpPSYjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روباه قطبی ، ممجواد ظریف : هر کسی که هنوز فکر می‌کند سلاح‌های هسته‌ای می‌توانند بازدارندگی ایجاد کنند، کافی است به اسرائیل نگاه کند. به اسرائیل در طول یک سال و نیم گذشته نگاه کنید.
بله، اسرائیل غزه را ویران کرد، اما آیا سلاح‌های هسته‌ای از اسرائیل محافظت کردند؟ آیا سلاح‌های هسته‌ای از فروپاشی اتحاد جماهیر شوروی جلوگیری کردند؟ اتحاد جماهیر شوروی بزرگترین زرادخانه هسته‌ای را در اختیار داشت.
علاوه بر این، ما به اندازه کافی اورانیوم برای ساخت یک سلاح هسته‌ای نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25434" target="_blank">📅 21:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نبرد سرنوشت‌ساز برای بازپس‌گیری باب‌المندب از حوثی‌ها
دولت یمن‌ امشب اعلام کرد نیروهای دولتی با حمایت ائتلاف به رهبری عربستان، پس از بازپس‌گیری ذوباب و مواضع راهبردی اطراف آن و قطع مسیر ارتباطی با المخا، به‌سوی کنترل تنگه راهبردی باب‌المندب پیشروی می‌کنند. دولت یمن این عملیات را مرحله‌ای سرنوشت‌ساز برای بازپس‌گیری حاکمیت بر سراسر کشور و پایان دادن به کنترل حوثی‌ها دانست. همچنین حملات حوثی‌ها به فرودگاه بین‌المللی عدن و فرودگاه‌ها و تأسیسات غیرنظامی عربستان را محکوم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25433" target="_blank">📅 20:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25432">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کابینه امنیتی اسرائیل : امشب (یکشنبه شب) جلسه‌ای با محوریت بررسی اوضاع در چند جبهه از جمله لبنان، سوریه، غزه و ایران تشکیل خواهدشد @WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25432" target="_blank">📅 20:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXiI14A0872tyXJP0z7_fbEe4M5csjmcNNlUoA9kzeTFOwQA0M3leA_mBeyoSiwR3Dac07SqFKHb6dpxvYPdnRRxFUwlqLOPsrHyPRTNvRdv7SrG5ZAQ815Fl8IIyzK36quBX_IjXw9WL3S8ap-0eR9-Lo_yfIWKqsg-SAxuToQgoNWM_ay5mLAOXjh30Dsia5kPC7Q0qLDzVfIFnIAHjKRRgPrBXxNFDT1JxfWsOy_9TrouVJ1zZHb0gtmi7pBMUKOgPGfTKS4ZXn2f0zKEgVwywguL_5RQh3LBty5o1bbgTtaSd7o75X4cir6PoASEfgEgaPPkJkWQ1FV4EL9M2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های رژیم : زینب ابوطالبی مجری جنجالی «مملکت مال حزب‌اللهی هاست، هر کس نمی‌خواهد جمع کند از ایران برود»، از کشور رفت
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25431" target="_blank">📅 20:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کابینه امنیتی اسرائیل : امشب (یکشنبه شب) جلسه‌ای با محوریت بررسی اوضاع در چند جبهه از جمله لبنان، سوریه، غزه و ایران تشکیل خواهدشد @WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25430" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEJq9sskJ1GZucvPQbv0yDxmBkW6o5DTk5dyY0UWvoIoA1Z_ZeyfedU8lbjp4Xx_bGckTpWJ7SyKx3TkgUqXyVpjfbksZ-Nlcf1mf3N_7f9TDP4Wf_RzgX7j1GzR3xg2g1KCR6TsLHKVquSP-FgihIeNyvfKp42YSWQS__TizL9ubO89W7tyIGBx6IMF8P4K5_mUHcNzcm47p5tLvBYPoFnmJ0EIqq_LCJygJz_pUW45kbFv99bS29g-YLlj_x2P0EJQSlJtiDO7ZqQWUsNvIGv8TFn7feNdbvnJdoTNXtHKq_kjF-aK6AUlRCf6PFEiBZj0scqtKP34i-jjWqkLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی ، کج بند : می‌توانستیم تنگه هرمز را کاملاً ببندیم، اما به دلایل انسان‌دوستانه این کار را نکردیم
اگه دوباره جنگ بشه اینبار به تاسیسات هوش مصنوعی و دارایی های ایلان ماسک تو منطقه هم حمله میکنیم
تهران به رویه‌های دیپلماتیک گذشتۀ خود باز نخواهد گشت
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25429" target="_blank">📅 20:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کابینه امنیتی اسرائیل : امشب (یکشنبه شب) جلسه‌ای با محوریت بررسی اوضاع در چند جبهه از جمله لبنان، سوریه، غزه و ایران تشکیل خواهدشد
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25428" target="_blank">📅 20:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP9tiVRXJNjwoCR_CHxruBaCn22F3V7vMHGDxbSeJCPOjP-S4oJjeXnbvRbl_b_q6-HirNabVZCdWMFvCXZ9Q0xHV9WCqXMSh88so2TrQwCuLCF0niw0kQsjfCs3396eOjI6YJGs0S4bSmg04K_PKMMcjryVQWKE1w4xFY9Uq1qIKHM9Q_Qbl-OP-78kK1S-QauaRhmbHx1RSxf1BsffmfUw5CCTgyuG3eZ5NZIarM0Y4Sf02v-UPRO4GO1bT2cHvJ06SASZ7yCNfO3xa76p8DQ37T6MaJj0RPxnawoUQfCoVc5uCyzxG6HVZj_VWwhyRp1zdeqK_KF5jaSy-HIplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ملوانان نیروی دریایی آمریکا در حال انجام تعمیر و نگهداری جنگنده اف/ای-۱۸ سوپر هورنت روی ناو هواپیمابر «یواس‌اس جورج واشنگتن» (CVN-73) هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25427" target="_blank">📅 20:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شاهزاده رضا پهلوی: «حمله وحشتناک به فرودگاه ملک خالد در ریاض، تازه‌ترین نشانه آن است که رژیم تهران هرگز به دنبال صلح نخواهد بود. از سال ۱۹۷۹، جمهوری اسلامی چه مستقیم و چه از طریق نیروهای نیابتی خود، علیه عربستان جنگ به راه انداخته و به دنبال بی‌ثباتی بوده است. به ملک سلمان، محمد بن سلمان و مردم عربستان به‌خاطر جان‌باختگان این حمله تروریستی تسلیت می‌گویم. کارزار آشوب حوثی‌ها زمانی پایان می‌یابد که ایران آزاد شود و روابط دوستانه میان دو کشورمان از سر گرفته شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25426" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">روسیه: شمار کارکنان روس‌اتم در نیروگاه هسته‌ای بوشهر به ۱۳۵ نفر رسید
الکسی لیخاچف، مدیرعامل شرکت دولتی روس‌اتم، اعلام کرد با بازگشت ۹ نیروی دیگر برای انجام تعمیرات برنامه‌ریزی‌شده واحد اول نیروگاه بوشهر، شمار کارکنان فنی و مهندسی این شرکت در محل نیروگاه به ۱۳۵ نفر رسیده است. این نیروها در واحد فعال و دو واحد در حال ساخت بوشهر فعالیت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/25425" target="_blank">📅 20:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسکات بسنت: ما بخش عمده‌ای از موشک‌ها و پهپادهای ایران را نابود کرده‌ایم و ۸۵ تا ۹۰ درصد توانایی این کشور برای بازسازی و تولید مجدد آن‌ها را از بین برده‌ایم. کارگران در حال حاضر سر کار حاضر نمی‌شوند، ایران به بازار دلار دسترسی ندارد و برای جبران مشکلات مالی…</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/25424" target="_blank">📅 20:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: ما پس از یک سال کارزار فشار حداکثری، اکنون وارد کارزار انزوای مطلق ایران شده‌ایم و هدفمان قطع ارتباط این کشور با جهان خارج است. تا روز گذشته، حدود ۱.۲ میلیارد بشکه نفت برای آمریکا از منطقه خارج شده، درحالی‌که سهم ایران صفر…</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/25423" target="_blank">📅 20:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: ما پس از یک سال کارزار فشار حداکثری، اکنون وارد کارزار انزوای مطلق ایران شده‌ایم و هدفمان قطع ارتباط این کشور با جهان خارج است. تا روز گذشته، حدود ۱.۲ میلیارد بشکه نفت برای آمریکا از منطقه خارج شده، درحالی‌که سهم ایران صفر بوده است. ایران اکنون هیچ نفتی روی آب ندارد و با جریان نقدینگی منفی مواجه است. ما خدمات هوایی ایران به جهان را قطع کرده‌ایم. مقام‌های جمهوری اسلامی دیگر نمی‌توانند به بستگانشان در لندن، دوستانشان در پاریس یا پولشان در سوئیس دسترسی داشته باشند. فشارها را از طریق توقیف رمزارزها و متوقف‌کردن کشتی‌های ایران ادامه می‌دهیم. ایران کنترل تنگه هرمز را در اختیار ندارد؛ پهپادهایش را هر شب به پرواز درمی‌آورد، اما توان راداری ندارد و گاهی به کشتی‌ها آسیب می‌زند، درحالی‌که کشتی‌ها همچنان عبور می‌کنند.
@WarRoom
ویدیو کامل ۱۲ دقیقه ، متن ۱/۳</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/25422" target="_blank">📅 20:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25421">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سازمان هواپیمایی عربستان سعودی تأیید کرد که فرودگاه بین‌المللی «ملک خالد» در ریاض عصر امروز هدف حمله جدیدی قرار گرفته است.
دیروز ترمینال ۳ و امروز ترمینال ۴  این فرودگاه مورد هدف قرار گرفته
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25421" target="_blank">📅 20:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فایننشال تایمز به نقل از مقامات ۵ سازمان اطلاعاتی اروپایی گزارش داد روسیه در حال گسترش برنامه‌های ترور مدیران ارشد صنایع دفاعی، به‌ویژه تأمین‌کنندگان پهپاد برای اوکراین است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25420" target="_blank">📅 19:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ_cDI_Pi847BiVyVd2EnA1rm5M8czdt4Fd1GEe2A8wk46Xa8ERlg4I8bkqsHc6Yh3DKqjkEQbE-5ehaZ0m0VKRkeLaYXPYjp3WAjGQjJV8QPzMTg9rf0WcddmGU3QmaOT86581T2PQJdyo4C-PuxssuDY1gMYcCQ6lcw_ZeJ3JGVD8DGOoJGBZjmUIfYO2tDXrT6-AdwuK9khd7uIknXo1qBBz1e5XCQbTCoMx2LaCHX1t7C4yuZzPzoe_B_T3JXadghPlVnGorAoZ1og6O1G-mPYGMxZ1MB0IW9cjdH5SNVvQU18kr41mq-AYSN1zzi1-8APqAm1O-6CU7mT1EHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: «از همین لحظه، آتش‌بس انرژی در جنگ روسیه و اوکراین برقرار است. هر دو طرف موافقت کرده‌اند. آن را نقض نکنید! از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25419" target="_blank">📅 19:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c92b0af8e.mp4?token=TmxQP7zYowcbAqGnlezs-uHE2sWZYqXP0_Lpd8KX15EoUBvht9OEoqjpWcQ7y5XDe9HWrIPpCFMSXRvPtvd2YIIBYqdSvLJU1TyD81EcS8QJDce2NBzOg9naFyhioebyiFNV7MgRoAMYO0j4Ol1Cer7hFm6H_G84rI9Ow2hdW9AXh-mzEH5rA1akc7UsyLXU_X7awoqToCAHKwCr_Q0vgEI4gAvyn4Tue6RVI5M85GKkCctBL1z5xtC7jyPAFMO9uQbGtw14oC5aJibGCj8iX0Fgwj6hkZWNfnL2JhDpQLAOvqz4GZKN5HmalT-0DUgNa76qRvrHgtyz2cpIlUt5UV8rICoN44DNn5N4VCuxMgTYW9hi9ohbdoHxjPuNRj7Zmu0Z7KCl18JmFQcSx4_keU6EzEL76uNOpy6OVZ7wJAU9TWo_g8AOhul-xmgup1XpvndwQCo8_qe6SjKupr3ohQo9EWdwTfJaxY0m-jQku0pSpx4IBt2IV_msFc3FhMHN2wh2pmx3WEFGlMW-BhiNbn9X7JVV0Z_E9VGVD-Lad2W_YIOU26WwbgMk_yUamxUBpgK4NZgad8ahstsQnc1e6vlPh1DyJaleg3VQkdPz-juAfW94Z7GzCDK-giDILIPxQw5xljWj2X_ux31qFqEU_2zKDF2b11BeJ-_ixpXcNWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c92b0af8e.mp4?token=TmxQP7zYowcbAqGnlezs-uHE2sWZYqXP0_Lpd8KX15EoUBvht9OEoqjpWcQ7y5XDe9HWrIPpCFMSXRvPtvd2YIIBYqdSvLJU1TyD81EcS8QJDce2NBzOg9naFyhioebyiFNV7MgRoAMYO0j4Ol1Cer7hFm6H_G84rI9Ow2hdW9AXh-mzEH5rA1akc7UsyLXU_X7awoqToCAHKwCr_Q0vgEI4gAvyn4Tue6RVI5M85GKkCctBL1z5xtC7jyPAFMO9uQbGtw14oC5aJibGCj8iX0Fgwj6hkZWNfnL2JhDpQLAOvqz4GZKN5HmalT-0DUgNa76qRvrHgtyz2cpIlUt5UV8rICoN44DNn5N4VCuxMgTYW9hi9ohbdoHxjPuNRj7Zmu0Z7KCl18JmFQcSx4_keU6EzEL76uNOpy6OVZ7wJAU9TWo_g8AOhul-xmgup1XpvndwQCo8_qe6SjKupr3ohQo9EWdwTfJaxY0m-jQku0pSpx4IBt2IV_msFc3FhMHN2wh2pmx3WEFGlMW-BhiNbn9X7JVV0Z_E9VGVD-Lad2W_YIOU26WwbgMk_yUamxUBpgK4NZgad8ahstsQnc1e6vlPh1DyJaleg3VQkdPz-juAfW94Z7GzCDK-giDILIPxQw5xljWj2X_ux31qFqEU_2zKDF2b11BeJ-_ixpXcNWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک والتز، سفیر آمریکا در سازمان ملل: ترامپ توافق بد را نمی‌پذیرد. او کار این رژیم را تمام میکند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25418" target="_blank">📅 16:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ارتش اسرائیل و سازمان «شین‌بت» اعلام کردند که طی ۲۴ ساعت گذشته، زیرساخت‌های حماس را در سراسر نوار غزه منهدم کرده‌اند. از جمله این زیرساخت‌های منهدم‌شده می‌توان به یک مرکز فرماندهی و دیده‌بانی در منطقه «درج-تفاح»، یک سکوی پرتاب راکت و سه انبار تسلیحات اشاره کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25417" target="_blank">📅 16:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چند آبگرمکن گازوئیلی و پیکنیکی گازی به سمت تنگه پرتاب شد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25416" target="_blank">📅 16:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddvJY01NTqMFjjyAZOxJejwMKOl6Ol4kScxm_eoDdJDY9oHNVaCtUc1jombj1zY4QVcn3qaPuplcsv1AgPE2J0CRLC5Dk7vFERTkH9kptfYn7KalXxe85SqV20ojfA0I6pcNO7J4g5Vpzmfk0AEg54uSfgFaE2dvtiqjtXHHmkkO3Q6PSg_ZaxiNBJaG3S167KHCtsAI186RfoMPS4afcFy8ZvnzShzTmwLNiFu1qbzbfl8k8JYEnVPJj46w5CX-1CRGuTLIYzJb6hnwjNiL6ULloUVQqBOQ_eM5UqiiFzpZs_omLC290ep8DQvRJ3lvLSNxVnnH2mGD8TAQEPwCwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلان ماسک : با ترامپ موافقم وقتشه اوکراین یه رهبر جدید داشته باشه.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25415" target="_blank">📅 16:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc67Qi6RJaelXvY75ICmvPx00pDGUYLfHr02b0dWNos9yfenk9QmHsMjV8jI4pLyPRrzRNkEEMqka1dgIQcWDTmXOhkDu7BbuNE_CJa4zd5JhFLYTtFC8p67gE_gYP64emydQodPfPVCs1go7_MHkIGzi55MmR2onYuE49T1sdIF8lN5ZaiT-UHr_yd-gQCq7SZRpmaLK-6bLFGFemCDc2cS2SjARztG3oJ3llhPT14Fu9TOmFVX992cglwl0rr2EZWJ90id5AjtZpU6p1TFceVFz7HfS14x4pTtpAgMrtUMePmy7Jy5gUxwrLFftFDCvIUhzRNIKsuOQvNfI1P2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامبیز حسینی‌ مجری‌ اینترنشنال ، مریم رجوی را در پلتفرم ایکس(توییتر سابق) فالو کرد
@WarRoom
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25414" target="_blank">📅 15:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبرنگار رویترز: آمریکا ممکن است نیروهای نخبه را برای عملیات های خاص قبل از شروع جنگ در ایران مستقر کرده باشد
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25413" target="_blank">📅 15:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb45997b4.mp4?token=fNKXcvaYK1cxQlBKHrsJnFsNcZGBym6lMRMoX9fcTS_8dNwUz3RK_KEvgkEksUWJUASFdigcY3W6AkSn3Dwi06OyzswiNlkffzexoVghLdAkQQUjXwL5G9CBbfNRdVLQWVDRR9rC7OXaBiuFqOi8liz7D1gdr8w11hiZNxRbBfv8BnioxWa7tfcK5HSOd5jFDEYP5f3Qd0eFbSD25Ip8upka-v8J484C0F061oO9T3Z9n63_ab9n_xkJTMOwYmiAfSC8z1sVOMrHKp6Fz69ciyIOQ03EOYZsjaoggn8T4VazLtDeP7uZZfq8t6qOUfP8a6RuEppWjPs8jYN6DbsmHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb45997b4.mp4?token=fNKXcvaYK1cxQlBKHrsJnFsNcZGBym6lMRMoX9fcTS_8dNwUz3RK_KEvgkEksUWJUASFdigcY3W6AkSn3Dwi06OyzswiNlkffzexoVghLdAkQQUjXwL5G9CBbfNRdVLQWVDRR9rC7OXaBiuFqOi8liz7D1gdr8w11hiZNxRbBfv8BnioxWa7tfcK5HSOd5jFDEYP5f3Qd0eFbSD25Ip8upka-v8J484C0F061oO9T3Z9n63_ab9n_xkJTMOwYmiAfSC8z1sVOMrHKp6Fz69ciyIOQ03EOYZsjaoggn8T4VazLtDeP7uZZfq8t6qOUfP8a6RuEppWjPs8jYN6DbsmHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تنگه هرمز یک کشتی در آتش میسوزد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25412" target="_blank">📅 15:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3515553bf.mp4?token=E7o_BKgBWJObOPvlcXQgxw3Regw28hnfQpY7Xe7Scrn5KgnMBSMl9Pj7XJbvPdrUbfNRU8kCyYxlmAXffMcwgIL8rLHLPVQD2UkNhA-C5gseDV6uuZBhhOXERHhHKQDzbEum4gBUjhyYkPXgBzcwp-Gf8vnRRS-6lShvAWY0t41b0WbqRfY7Dll81X2iayShAbIXfZtM0H3SUCAN-U9JIW5EiTHvRzuhh57As-SGVTMH9XDO4wYuNjgSW2un0Fmd_oN5YO2KThuUVAaK7PA9ZkxzukZ54nW77hkQ0Q0JPPYD-tQOr1yfj5UuDcCMSsNClfzU7XcNrADDJ4s8HNaLqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3515553bf.mp4?token=E7o_BKgBWJObOPvlcXQgxw3Regw28hnfQpY7Xe7Scrn5KgnMBSMl9Pj7XJbvPdrUbfNRU8kCyYxlmAXffMcwgIL8rLHLPVQD2UkNhA-C5gseDV6uuZBhhOXERHhHKQDzbEum4gBUjhyYkPXgBzcwp-Gf8vnRRS-6lShvAWY0t41b0WbqRfY7Dll81X2iayShAbIXfZtM0H3SUCAN-U9JIW5EiTHvRzuhh57As-SGVTMH9XDO4wYuNjgSW2un0Fmd_oN5YO2KThuUVAaK7PA9ZkxzukZ54nW77hkQ0Q0JPPYD-tQOr1yfj5UuDcCMSsNClfzU7XcNrADDJ4s8HNaLqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ‎صادر کردن دستور یک حمله تلافی‌جویانه قاطع علیه حوثی‌ها توسط محمد بن سلمان، ولیعهد عربستان سعودی
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25411" target="_blank">📅 15:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: منافع‌مان را یا با دیپلماسی می‌گیریم یا با نبرد. اگر منافع ما در دیپلماسی به دست آید، چه بهتر. صنعت هسته‌ای ریشه در ایران دارد و نمی‌تواند با ضربه از بین برود؛ متاسفانه دشمن این را هنوز هم نفهمیده.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25410" target="_blank">📅 14:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a78cb2396.mp4?token=AzAhI22v6256pgfkqJJq8IY5yU6xqpovW0Q8vaTes6rAYHEjeCy3V0i5v4Z6LxGRSjSlg3A520Lyt-RWHarEO_i5tpdUUIDNUaHBHJZA3xS90mv8iPb19PrfNRUtofaeVhvULQnUK84hgJCW8FPRdQTqzDicP7eE8xKr1B_4VlxGdCHC2KutO-A0uo8sba6SkE570NMpRfw1xrMANSUjifN1Pz6KCrWQr1jOzJltkB250cb73oEIMRH1jgnxfKoDKu-xIeOVcUUS3llQLtiZ2mtPxHOjUp6_mzT0qCFb7Ef_cnFexMPwOCmZ4_qMK4Llee61_dsnJtDc_H614gPCgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a78cb2396.mp4?token=AzAhI22v6256pgfkqJJq8IY5yU6xqpovW0Q8vaTes6rAYHEjeCy3V0i5v4Z6LxGRSjSlg3A520Lyt-RWHarEO_i5tpdUUIDNUaHBHJZA3xS90mv8iPb19PrfNRUtofaeVhvULQnUK84hgJCW8FPRdQTqzDicP7eE8xKr1B_4VlxGdCHC2KutO-A0uo8sba6SkE570NMpRfw1xrMANSUjifN1Pz6KCrWQr1jOzJltkB250cb73oEIMRH1jgnxfKoDKu-xIeOVcUUS3llQLtiZ2mtPxHOjUp6_mzT0qCFb7Ef_cnFexMPwOCmZ4_qMK4Llee61_dsnJtDc_H614gPCgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: حله … اشکالی نداره این موضوع منو آرام می‌کنه،  آن‌ها احتمالاً پیش از انتخابات کمی بیشتر داستان درست کنند ، چون فکر می‌کنند این کاراشون به ضرر ما تمام می‌شه . ما می‌توانیم خیلی سریع به این داستان پایان بدیم باورشون نمیشه چقدر تمیز کارشون تموم میشه . آن‌ها نمی‌دانند من چقدر با آن‌ها خوب تا کردم؛ نمی‌دانند چقدر تازه باهاشون با ملایمت رفتار کردم
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25409" target="_blank">📅 13:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3u8Xmm3QekCEnc63nZ20pqgNc1gOqDeJTD7QvXAGycF2YfOX7MTFZbEJ0G1zfSu2q3eRV1-lpxNsBD_z-qFHiwVn0WG6Bdv8-4bJjnHMbTOkNb8mWgo0DWc7_zPA7RHXC_qRDipxnRV5zMvxHmLuvUy_ihWRE5RTUAY5qhytAk5kFqOkdHbV8S3cpInjxu8ysKoDUy2E2TVIew-YjHTDASJwp7fhZeFJeJAAgvwIZiu9vcsEavWml87QdDg91m_wx2F8Dl5jsfREh6YD6j2LEwSfr-8wKlGkWdM4AyGQ5ZALC4W0ftNokwdtdHckcAEKpjCHZa2DUvIlSUJ6wkb9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tY5JnJVLI70ZrbcqXH83UbPro0TXvjDReRbCjkifQhAMnN9I2IfqIXWFBBN3uX1tk0lAWwQLpqkD7heRtG5xKSKeJP8ClUlhYzQI_6E___jEgKjvLBd_P1STTUm_L8MPmwBQbjuHmL0dFQ7Ol1Hx73PvahLyB7KqMTNfW89sLN8EqdX2yhJmV0fBdBz5Fl4xK5kFFU0bvlzhHzpKGLdyIV6TjQID25n7XllMrOOcBssgo2mZ3KaGGH11ZIdBV8zYoTRTKO5R5GRLWWkSJ3KsZdK_RE0MDTf_Zli7yQ3MM614vvDxhsmWLagSVd1OUxKMJ555XIT6CBL5TJZrbYSz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOWnNcTHvD52p7BodSmk7628hrfOJwSTJC6xIlOe58dnxavuXcbeT6FmaUoRX02p_wJToFjeI6GYAHo2_niGfN35C30LUFvADQTOf3Z8AggqRMKar_25CFLPgP9qpNXPUrz-FxSbUELmWjfXryS9-UylL3PhLtiR_KjW6sbW32bfqjheguQl5ER7Ls1baOyBH7EjElAOTsCYlfUSev19_nCleWGk0eTnwGDQIGyRd3JsesVZ4y7LMs9RzjllLX2CsN_O6aWQnY-OqE92pDWUoODveyGQy---NU20HZf3eLoXZWKCdR3PJC_pYCJEeNWa8wZEYijYK-LX9tEnQPRWDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آسمان تهران ، آبگرمکن رو کات دار زدن
😂
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/25405" target="_blank">📅 12:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارشهای بسیار از‌ پرتاب آبگرمکن از اطراف تهران/کرج
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25404" target="_blank">📅 12:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">محمدمهدی هاشمی، نویسنده روزنامه خراسان نزدیک به ممباقر قالیباف ، در یادداشتی که امروز، منتشر شد، مدعی شد با بررسی تحولات و اظهارات هفته گذشته ترامپ و روبیو می‌توان نتیجه گرفت که
آمریکا و اسرائیل تصمیم خود را برای آغاز دور بعدی جنگ گرفته‌اند
. او نوشت تبادل پیام‌ها میان تهران و واشنگتن نیز احتمالاً تا پیش از درگیری بعدی تأثیر ملموسی نخواهد داشت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25403" target="_blank">📅 12:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25402">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzfV28fmODkSWYcaj2c0VPQnSCT6lU8XVaUakcg-VxP54crNs6loK-13M_ONO3PbHpM-Z6SlRNfOhTMdsZrgU_PwlSg9Dau_5ZF8P0TgQYHft_rXyOOTJKjuKZ7bwLL86MDCCdQ9-dUqmodUo55k761WLak_WaCKV8e9p17F3NtsVTgodSGFhx-f0qew_FisGMBHpcOYBhbjReYMtiRFNHt-GN_tfC-xBYuvVpyo3WChGMgINPjeyadZsgE7oQzQItc7TTwpqqQjtWOtO-5TOdSh0YDidQrGZ_aQsjl_9Xl8uGqlK87Gy6R65f8Kb6oogNgojNZ2-xSLzgs4SDURJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی دختر بر تمام دختران ایران زمین خجسته باد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/25402" target="_blank">📅 12:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEMV8ZHeidBpG8Xz25HR_7EEx38BHJlWXtkb4fi9EHRNhtaXmUQPZtnnEKvBOhaWyeHoqL6FF0PASHsjZeKfX6HXmZ7qeJ8ErxI80m0eeoRd8PwXETgPU46VXJN_9hMCzOMUDkuAxfK6YuVuPwPEsfnwvBDCvgPX2vrTXg54AMyr-BpwOg_-SvqVCntFUsRtwpA0OmJEyd9S8OXaqx48XKGNhk8b771FiZzaD-xtf8r0OIFvmG-EoB2Q5_bRlV1gvWtlzLp6t4lqasmMEr_ONHLNIWYhqhQEbcPVNQHkAx_ORY9Vshy8MPPgoKDAM19rm6hWCIuRXca8qkW8acqDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود یک ساعت پیش، چندین انفجار در نزدیکی کوه صفه در اصفهان، واقع در مرکز ایران، شنیده شد.علت این انفجارها هنوز مشخص نیست؛ با این حال، بگم که این کوه محل استقرار بسیاری از پرتابگرهای موشکی رژیم هم است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25401" target="_blank">📅 11:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پزشکیان : اگر ما ایرانیان کنار هم باشیم، نمی توانند ما را بشکنند و به ما آسیب بزنند
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25400" target="_blank">📅 11:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2f5a8ccb.mp4?token=MYNiUu1szi2CgjOvYN-ZxZsdDcJlyastqc7Wx6LgyBKZQ0oRuT4yNya4fdK0LaoqvuXLfLqdAlH4fnm4Th779AAqr8ds5ZcF9P7x1FGMBRduXLvcitl6StUy3vZ4UbX0Px-pKpHgG35gmjZ0-bkUCBli6g3CLYnqIFca8LpIPayhEStM2IkhNR966TlQKjUkg5ynXat8WDDYkFv0Hjd1q6O_yX0njcNGPYbIekyjJOi-iskvySddy_Nqkm0WaLf9ktiBwe819P-eKjI8CCsnzzZaiRBedIDUaW6rTmEmhQHP5r0JQTTFyNkX2ZeBzY9S0Fw8EbCvZfS51QKlinom_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2f5a8ccb.mp4?token=MYNiUu1szi2CgjOvYN-ZxZsdDcJlyastqc7Wx6LgyBKZQ0oRuT4yNya4fdK0LaoqvuXLfLqdAlH4fnm4Th779AAqr8ds5ZcF9P7x1FGMBRduXLvcitl6StUy3vZ4UbX0Px-pKpHgG35gmjZ0-bkUCBli6g3CLYnqIFca8LpIPayhEStM2IkhNR966TlQKjUkg5ynXat8WDDYkFv0Hjd1q6O_yX0njcNGPYbIekyjJOi-iskvySddy_Nqkm0WaLf9ktiBwe819P-eKjI8CCsnzzZaiRBedIDUaW6rTmEmhQHP5r0JQTTFyNkX2ZeBzY9S0Fw8EbCvZfS51QKlinom_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: قبلاً هم گفتم که باید برای خاموش کردن آتش به ایران حمله کنیم . ما با یک مشکل جدی روبه‌رو هستیم؛ با دولتی بسیار شرور که رتبه اول جهان در حمایت از تروریسم را دارد. نمی‌توان چنین سلاحی را در اختیار آن‌ها گذاشت؛ آن‌ها بدون هیچ تردیدی از آن استفاده خواهند کرد. می‌دانید، خیلی‌ها حاضر به استفاده از چنین سلاحی نیستند، اما آنها…
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25399" target="_blank">📅 10:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB9bm7IItD98_YXVYKvubgvdmwLP6tHiTFld4T1oFktiJS-oMbgIsVW8U3UIQU1-_oB4fur3MwHR5B3zn5g3itiK5-0rrRrg-RaAse-ThufkvAgesQZW9tpBiYKxZj2Kwx4Ocyb8K8sqqsTIe4wSURTbnrUainUTIWIspu3SlQDvJF7qTpWmD9nuFmoid0rSvf_XWPglLmuZCNkvh-cUIthIfUeAO3cvQ26h5I7UNA4zKJ5BA4LXugIfGFBQUT9sOBqASfS35pVsP37ywL5H6i0oUoi0NrR941SKddX8a0cNe-bPJ_uyCyXopOLROQKtLgeG0vZtrg0W9d33_8x5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاطمه مهاجرانی، سخنگوی دولت : پروژه ایجاد ترس از ایران و تضعیف روابط این کشور با جهان، «افسانه‌ای است که دشمنان ترویج می‌کنند»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25398" target="_blank">📅 10:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce60ee997d.mp4?token=eQ0ofRAOYd_JDWiViSxwmZrk3EfaoH8eZOCSPElgC5h-wSZO_unU3OtncwaSUUAhojzA3-kDcUaaj4E99z1mErmjzPriazFABGXXdXCMju3CxyYM0TKdb5NMTiMWIHjonYxCpXHX9IEVAt8fJvjhJogeIxx5px71pRrXgYfXfYOQRup9vE2yYlxAI5o1G1qa3_qS1XiFfkxZYA9TOP651j84KEBXO3UTq22ICyk5CBKF36UqlI79aE2rCOUGc1aCPauBK35JpazeV8lOlppRXSKHd5EQs2tWcKHS4y4FCiQ3Q4rHu9-l7JDVqn1WBoj2uX_XBe9s5xErHmA2jsTsiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce60ee997d.mp4?token=eQ0ofRAOYd_JDWiViSxwmZrk3EfaoH8eZOCSPElgC5h-wSZO_unU3OtncwaSUUAhojzA3-kDcUaaj4E99z1mErmjzPriazFABGXXdXCMju3CxyYM0TKdb5NMTiMWIHjonYxCpXHX9IEVAt8fJvjhJogeIxx5px71pRrXgYfXfYOQRup9vE2yYlxAI5o1G1qa3_qS1XiFfkxZYA9TOP651j84KEBXO3UTq22ICyk5CBKF36UqlI79aE2rCOUGc1aCPauBK35JpazeV8lOlppRXSKHd5EQs2tWcKHS4y4FCiQ3Q4rHu9-l7JDVqn1WBoj2uX_XBe9s5xErHmA2jsTsiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره حمله مرگبار حوثی‌ها به فرودگاه ریاض چه نظری دارید؟
ترامپ: به‌نظرم وحشتناک است
خبرنگار: آیا آمریکا را وارد این درگیری خواهید کرد؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25397" target="_blank">📅 10:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سازمان حقوق بشر کارون: بیش از ۱۰ کارگر متخصص و بومی شرکت پتروپارس در هویزه، پس از اعتراض به اخراج و تمدیدنشدن قراردادهای کاری خود، به ۷۴ ضربه شلاق تعزیری و پرداخت ۲۰۰ میلیون ریال جریمه نقدی (۲۰ میلیون تومان) محکوم شده‌اند. به گزارش این سازمان، حکم شلاق اجرا شده است. این کارگران که در پروژه توسعه میدان نفتی آزادگان جنوبی سابقه فعالیت داشتند، پس از تجمع اعتراضی با شکایت شرکت و پیگیری قضایی روبه‌رو شدند. حکم در ۱۳ تیر ۱۴۰۵ صادر شده و کارگران همچنان خواستار بازگشت به کار هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25396" target="_blank">📅 09:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/564786cc15.mp4?token=sEpN-3WU9e_ga7LqQ_a6WWA9G8wOZ7n2GTydEa1PKxZX6OwjWdQ2MW65DHVA_F_CmLBnBTboV0tnX9dIf64YLKy3O2tlUXKhKCIYRzj1xjnBq6YM7YQ9Dws3Hf2BZvXA1IY29NnjSI2uQa5L4sjMy69ghfrux17-1OKbW0GTIBNw_NM2iLTNsfzNp3SKXtCKWKeGcmHpF57h-I8_zR2glG3P_8NpG6iDwjt9lZwkZ5h_Z5VgB1T3Du3ljqDTvBz64GwePuIVGOoZ0ljwmYE2YXWdXz_gWHMNWCk0CWysDIEGHB0RF8nnI44NxWuGCgopo0rryH8pjXd_ZYcpBa2pnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/564786cc15.mp4?token=sEpN-3WU9e_ga7LqQ_a6WWA9G8wOZ7n2GTydEa1PKxZX6OwjWdQ2MW65DHVA_F_CmLBnBTboV0tnX9dIf64YLKy3O2tlUXKhKCIYRzj1xjnBq6YM7YQ9Dws3Hf2BZvXA1IY29NnjSI2uQa5L4sjMy69ghfrux17-1OKbW0GTIBNw_NM2iLTNsfzNp3SKXtCKWKeGcmHpF57h-I8_zR2glG3P_8NpG6iDwjt9lZwkZ5h_Z5VgB1T3Du3ljqDTvBz64GwePuIVGOoZ0ljwmYE2YXWdXz_gWHMNWCk0CWysDIEGHB0RF8nnI44NxWuGCgopo0rryH8pjXd_ZYcpBa2pnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون آمار تلفات نظامی آمریکا در جنگ با ایران را به‌روزرسانی کرد: با اضافه شدن ۲ کشته و ۴ مجروح به آمار قبلی، شمار نظامیان آمریکایی کشته‌شده به ۲۱ نفر و تعداد مجروحان به ۸۶۵ نفر افزایش یافت. @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25395" target="_blank">📅 09:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شفق نیوز نیز به نقل از یک منبع امنیتی عراقی گزارش کرده: دو هواپیمای عازم ایران بامداد یکشنبه پس از آنکه مقام‌های ایرانی به دلیل ملاحظات امنیتی اجازه ورود آن‌ها به حریم هوایی ایران را ندادند، به فرودگاه نجف بازگشتند.هویت پروازها هنوز روشن نیست. جزئیات بیشتری درباره علت این تصمیم هم اعلام نشده است. تردد غیرنظامی در حریم هوایی عراق نیز به‌طور موقت متوقف شده، اما بسته‌شدن کامل حریم هوایی تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25394" target="_blank">📅 09:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25393">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آخرین آمار حمله به فرودگاه ملک خالد ریاض: مقام‌های سعودی کشته شدن ۱۲ نفر و زخمی شدن ۳۰۹ نفر را در حمله موشکی روز شنبه تأیید کردند. در میان کشته‌شدگان، ۴ شهروند سعودی و ۸ تبعه خارجی از جمله
یک شهروند آمریکایی
حضور دارند. مقام‌های سعودی از وخامت حال تعدادی از مجروحان و وارد شدن خسارت به فرودگاه خبر داده‌اند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25393" target="_blank">📅 09:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اتاق جنگ با یاشار : میانگین ۸ نظرسنجی انتخابات اسرائیل تا دیروز: حزب لیکود به رهبری بنیامین نتانیاهو ۲۲٫۴ کرسی و حزب یاشار به رهبری گادی آیزنکوت ۲۱٫۲ کرسی پیش‌بینی‌شده دارند. در سطح بلوک‌ها، بلوک نتانیاهو ۵۵ کرسی و بلوک صهیونیستی(یک جنبش سیاسی و ملی‌گرایانه است که با هدف ایجاد و سپس حفظ یک خانهٔ ملی برای یهودیان در سرزمین تاریخی اسرائیل شکل گرفته و توهین نیست )مخالف او ۴۸٫۴ کرسی دارد؛ احزاب عربی و سایر احزاب نیز در تعیین امکان تشکیل دولت نقش مهمی خواهند داشت. برای تشکیل دولت، کسب حمایت دست‌کم ۶۱ نماینده از مجموع ۱۲۰ کرسی کنست ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25392" target="_blank">📅 09:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سنتکام : محاصره دریایی کشتی‌های ورودی و خروجی بنادر ایران از ۲۳ تیر از سر گرفته شد و طی سه ماه اجرای مجدد آن،
۴ کشتی از کار انداخته شده و مسیر ۱۳۵ کشتی تغییر داده شده است.
نیروهای ما در همین مدت ۱۰ نفتکش مرتبط با شبکه مالی غیررسمی چندمیلیارددلاری سپاه پاسداران را منهدم کرده‌اند.همچنین از دریانوردان خواستیم به هشدارهای محاصره توجه کنند و هنگام تردد در دریای عمان و مسیرهای منتهی به تنگه هرمز، اطلاعیه‌های دریانوردی را دنبال کنند و در کانال ۱۶ ارتباط رادیویی دریایی با نیروهای ما تماس بگیرند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25391" target="_blank">📅 08:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a18e92af.mp4?token=GLQOx-oOps_ahsZUZimRMjpLCenIRAXVsIYXZvvvruHjWFrJC5zUWu3ePGN4lbON9DBoYUwP9llo3qtGU7WCGsGCkaMsxCZea9487H2PsHnIbdnKqoHfSqz09EhjX5jW0WZ6U4ZHVUK2GDDXq9z3vpXRRWJ_vmd6mGuzahXv3xD21IpkPXn-G4mTdHQOkGA0mb74sP2St4FYtr4XcRYVPluL68bF5aEoq40QKDvtgTHsCT5HKyLLCPegkK_rQAr_aY17__ODA3OL0kyh5FxCnxNVBY24PpwpfMwW9Hf5uLvHcXhGCLL3X7ubwEL987FMpgqfNEewLWlR3tQKI5_l2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a18e92af.mp4?token=GLQOx-oOps_ahsZUZimRMjpLCenIRAXVsIYXZvvvruHjWFrJC5zUWu3ePGN4lbON9DBoYUwP9llo3qtGU7WCGsGCkaMsxCZea9487H2PsHnIbdnKqoHfSqz09EhjX5jW0WZ6U4ZHVUK2GDDXq9z3vpXRRWJ_vmd6mGuzahXv3xD21IpkPXn-G4mTdHQOkGA0mb74sP2St4FYtr4XcRYVPluL68bF5aEoq40QKDvtgTHsCT5HKyLLCPegkK_rQAr_aY17__ODA3OL0kyh5FxCnxNVBY24PpwpfMwW9Hf5uLvHcXhGCLL3X7ubwEL987FMpgqfNEewLWlR3tQKI5_l2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام :  نیروهای آمریکایی دیشب ، یک کشتی باری تجاری را در دریای عمان پس از بی‌توجهی خدمه به هشدارهای مکرر و تلاش برای عبور از محاصره دریایی بنادر ایران، از کار انداختند. به گفته سنتکام، یک جنگنده آمریکایی با شلیک مهمات دقیق به بخش عقب کشتی با پرچم پاناما به نام
M/V Ocean Molica
که با نام «Arika Sun» نیز شناخته می‌شود، سامانه پیشران آن را کاملاً از کار انداخت؛ اما به خدمه آسیبی نرسید. این کشتی پیش‌تر از یکی از بنادر ایران حرکت کرده بود.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25390" target="_blank">📅 08:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65cc3b20f5.mp4?token=IFAM4BxLmig1GFJ4RgYc8sjfQ63DEngv4ZUeqPbqOSAz_3PZ2RyOlUWq-ZjrOJ__NZ_XFNkpEl89SUHBv61mnNlxQ59QzbaxruTPLcbIgZy3MBnRZTjjywMB5t7PV5dhoDNdDm-vXgVsD6j5Wt4oU4ENWnLw-kaXRi-mcFbMFJfc1ekgBBHjFX2C-s84ZgJY6ehdVex6l648IwsswOFtNSUgUUzBTieczU4hvYstuRcaXidbHGfPSl-g6iZSIDPJIEP_cv46dilgTIHtCFvH0jVem7fwx4UDd_UN0Dl7kQaxYdo7H11XTbMPlFV0iBCWxAKMqgDG6RD6Fqalp3IEuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65cc3b20f5.mp4?token=IFAM4BxLmig1GFJ4RgYc8sjfQ63DEngv4ZUeqPbqOSAz_3PZ2RyOlUWq-ZjrOJ__NZ_XFNkpEl89SUHBv61mnNlxQ59QzbaxruTPLcbIgZy3MBnRZTjjywMB5t7PV5dhoDNdDm-vXgVsD6j5Wt4oU4ENWnLw-kaXRi-mcFbMFJfc1ekgBBHjFX2C-s84ZgJY6ehdVex6l648IwsswOFtNSUgUUzBTieczU4hvYstuRcaXidbHGfPSl-g6iZSIDPJIEP_cv46dilgTIHtCFvH0jVem7fwx4UDd_UN0Dl7kQaxYdo7H11XTbMPlFV0iBCWxAKMqgDG6RD6Fqalp3IEuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور جک کین: پس از انتخابات میان‌دوره‌ای، احتمالاً ترامپ علاوه بر فشارهای اقتصادی، در کنار اسرائیل فشار نظامی گسترده و کوتاه‌مدتی علیه جمهوری اسلامی اعمال خواهد کرد تا زمینه سقوط رژیم فراهم شود. به گفته او، در مرحله بعد، سازمان سیا و موساد می‌توانند با تضعیف حکومت و کمک به شهروندان مسلح مخالف، به پیشبرد این روند کمک کنند. کین معتقد است این سناریو محتمل‌ترین مسیر پیش رو است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/25389" target="_blank">📅 02:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سخنگوی نیروهای ائتلاف: حمله به فرودگاه بین‌المللی ملک خالد، یک عمل تروریستی است و به شدت به آن واکنش نشان خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/25388" target="_blank">📅 02:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اخ اگه تاریخ تکرار‌ بشه ….</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/25387" target="_blank">📅 01:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25386">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fdb2d73bd.mp4?token=r9U7FmvzVTSeJezneWAo3N-g8ko3ywUC36lpVGSIlhZytO4NWHQr4yFC3qAx26zYkTlTDZ3XL-Civx5aMFJJho5WFOJaGtTVDQf6IzfXK-Oq1rbYJi7izQ0Hhye8l9v7-00KxdZZXN2yEJiYKv-CwStYG0XssLrOD7Onymju4SqnQbAgMHo6cQqFzEriOZaNjVKvX40lXfAmdJCekIi3QZu9DTt2g0O6lpBZX7Cjyp0mjBIy2mgmfaDvDpRu6uikuzT3EJqCxNiKMOslFvXJGbqXEzkbFF2hpd-yuQnLZFETjQFxDzytB5rxBmK-HpgC7_VQgCALFkvxZgH0I-M-aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fdb2d73bd.mp4?token=r9U7FmvzVTSeJezneWAo3N-g8ko3ywUC36lpVGSIlhZytO4NWHQr4yFC3qAx26zYkTlTDZ3XL-Civx5aMFJJho5WFOJaGtTVDQf6IzfXK-Oq1rbYJi7izQ0Hhye8l9v7-00KxdZZXN2yEJiYKv-CwStYG0XssLrOD7Onymju4SqnQbAgMHo6cQqFzEriOZaNjVKvX40lXfAmdJCekIi3QZu9DTt2g0O6lpBZX7Cjyp0mjBIy2mgmfaDvDpRu6uikuzT3EJqCxNiKMOslFvXJGbqXEzkbFF2hpd-yuQnLZFETjQFxDzytB5rxBmK-HpgC7_VQgCALFkvxZgH0I-M-aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:میتونیم خیلی سریع به این جنگ پایان بدیم. اونا هنوز نمیدونن چقدر باهاشون راه اومدم و مهربون بودم.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/25386" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1194293ab9.mp4?token=GZrylLuUW1whl4d3bMGYE4iYwP70W1G3kobADTQ7RMXQKodzWzEBTg9t8RiqF3vFPYVkpaYO7OqblTY4t-6UZJ1M1_XsrWYXg-584YMrovh7qw_lwToTqU1HNY0biHEloXr4p-Z8qo96uTlM5Z4Hetw1rw3oHRdCn4oviNkFApRWVsWtxq3DotMy6VrA3p-R45UPZvbhTpCbx-DTDSxJcklAvd78zPqXEV4rkMChUJnEddkI8WaqI1VEn05Fe-kg1h7B_QmZKWv6Gc7ABSdLoC0saFA1UYluUKv9uwoOeBvJpasqnxQIQa9CJs01gL6qx9IrWD1PrzVNQd1dh3BcsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1194293ab9.mp4?token=GZrylLuUW1whl4d3bMGYE4iYwP70W1G3kobADTQ7RMXQKodzWzEBTg9t8RiqF3vFPYVkpaYO7OqblTY4t-6UZJ1M1_XsrWYXg-584YMrovh7qw_lwToTqU1HNY0biHEloXr4p-Z8qo96uTlM5Z4Hetw1rw3oHRdCn4oviNkFApRWVsWtxq3DotMy6VrA3p-R45UPZvbhTpCbx-DTDSxJcklAvd78zPqXEV4rkMChUJnEddkI8WaqI1VEn05Fe-kg1h7B_QmZKWv6Gc7ABSdLoC0saFA1UYluUKv9uwoOeBvJpasqnxQIQa9CJs01gL6qx9IrWD1PrzVNQd1dh3BcsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
رو یه مردم آمریکا
: داریم به این فکر می‌کنیم
( از باسن سوزی رژیم )
که نام تنگه هرمز را به تنگه ترامپ تغییر بدهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/25385" target="_blank">📅 00:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a5493e67.mp4?token=MXjCPfxU7Oimb8tipB0raR2tJSPyBfbErqdK2aCUcMIXt8sdhg7JOSFc7g8CLgPR1pEjqdZOR3MLrVEx1hmyTqYGLB3oFBqNekZI_s1m8HrVTjEDNwzjuiKcSQbKnr0L_vlLI_-G9XfuxzhUzL2cz7r2QdH-rfJDnw-71UcWvyvZWGEaIAmF2lyKIgKuc5-wWF6L2O0MAsSMzF9_AfOW6PDgR9wuoLukAGtxGfvl0VyyJiWdxJWDgi-AkkxttMA4_W1l1cRFS80NQXqgG4OoyahREeYRGrAohBazhzuBakgjdyvZNcxaDC3PoMoEDGq3SkcSQbX4g9cMKOwbkh48Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a5493e67.mp4?token=MXjCPfxU7Oimb8tipB0raR2tJSPyBfbErqdK2aCUcMIXt8sdhg7JOSFc7g8CLgPR1pEjqdZOR3MLrVEx1hmyTqYGLB3oFBqNekZI_s1m8HrVTjEDNwzjuiKcSQbKnr0L_vlLI_-G9XfuxzhUzL2cz7r2QdH-rfJDnw-71UcWvyvZWGEaIAmF2lyKIgKuc5-wWF6L2O0MAsSMzF9_AfOW6PDgR9wuoLukAGtxGfvl0VyyJiWdxJWDgi-AkkxttMA4_W1l1cRFS80NQXqgG4OoyahREeYRGrAohBazhzuBakgjdyvZNcxaDC3PoMoEDGq3SkcSQbX4g9cMKOwbkh48Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «حاکمان ایران می‌گن: ما همه رو می‌کشیمممم! همه روووو!
همچنین می‌گن: الحمدلله! الحمدلله! الحمدلله!
منم می‌گم: بابا، شماها دیوونه‌اید! واقعاً دیوونه‌اید.»
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/25384" target="_blank">📅 00:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رویترز: در حمله روز شنبه به فرودگاه بین‌المللی ملک خالد در ریاض، چندین نفر زخمی شدند و بیش از ۱۲ آمبولانس به محل اعزام شد. طبق گزارش گاردین، ده‌ها نفر مجروح و ۵ نفر در بخش مراقبت‌های ویژه بستری شدند. آمار رسمی نهایی تلفات حمله شنبه هنوز اعلام نشده است. ولی بر اساس‌آخرین اعلام رسمی عربستان، حملات امروز به فرودگاه ریاض و یک هواپیمای سعودی، ۳ کشته و شماری مجروح بر جای گذاشت
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/25383" target="_blank">📅 00:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/563c5da19b.mp4?token=arFv7H6-VrO5ofNeIL53EX6213NyKgIp_ZpPSkq5zD3NePJ1j7uDfx0QFkrVZWbHYr_mrDfIvqsH4GMIhHYw5XXLyXw7OcNqZUyZvX0PFWz5Avg2latdWFfw4PL25IZr-h-sgVBOQEFPHJny_-lXRGKR_h2w1CQErrM5LjZwXFYqcbNAZnsWfjGYQvfjDWf2vhUrkhZ6Yk4TPtNub7p4FcK3kSBIBXSEHj1nT5VKAwUAWPZnVkiXMeYuiIipbTthgaGz3g6lEdrJRYxhNdBSqS4kgegGhMZtC0pnlhkgeIS46xnQL-CB13u4-glutpwUz1qXzU8URU68CKdOIoPZpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/563c5da19b.mp4?token=arFv7H6-VrO5ofNeIL53EX6213NyKgIp_ZpPSkq5zD3NePJ1j7uDfx0QFkrVZWbHYr_mrDfIvqsH4GMIhHYw5XXLyXw7OcNqZUyZvX0PFWz5Avg2latdWFfw4PL25IZr-h-sgVBOQEFPHJny_-lXRGKR_h2w1CQErrM5LjZwXFYqcbNAZnsWfjGYQvfjDWf2vhUrkhZ6Yk4TPtNub7p4FcK3kSBIBXSEHj1nT5VKAwUAWPZnVkiXMeYuiIipbTthgaGz3g6lEdrJRYxhNdBSqS4kgegGhMZtC0pnlhkgeIS46xnQL-CB13u4-glutpwUz1qXzU8URU68CKdOIoPZpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/25382" target="_blank">📅 23:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadf07bd65.mp4?token=hpDzKUQAo4y3vFzdDbEFQfoaEG6lxWRKykMNdZ5VInSVoNOIlOo-Jk-GwQg29htFK9A6xWoi3rgwmZshIRm4D0MLLwKA8Zczeo_OJfbgHzIAuF6NttM0NF9NhYIdSdeYw1qmL7B9vg88ZihU3FOrF-ydYXHT9MbPWp7SgdnYMTN8dtGKB1VinkQZEjIgGdwZCyeqTqkdpHtakcps8U-6J52dHXSRkZrEF3BnUpIYkb08mJXxQUEMGcWxbJU_B_mTSSLSnCJ_jcH74dr8KftJ_ME8s2DgLHBW3uqkcMprajUFwSyWqG6Hb3-AX3tamsYPB6EYXV4VXKHVqjgkoE8r0GOOMk3CAjcbu0wL0XaQ2rSLP79YPAswqMnRLLoiY6Szc6DgR52tk-tw8JSBnOyvVdOvbv-_a6duh7TquW0I4ITpMYG7_l2MVZZGj9AY6z_flv6q8OOEmZkYjzd8H9yimGebhbHXO9eWjKaAj_y1AAHbaZAHKJW9brOOw_Ll32pCk-bV9hNERacerLEpjhbSujW90tMpoZjjUb85q1vub2WDbqg4Lbss-BZTWo0V-6hDDdQ8rFVUxqqegyo9ke10NQa-k3Gy1WpS0-KbuGv7D38h_mqpDFC6aT9Afahad-eOgBLT0Bihvy71o5oTOSoGMpEqLMEsSci0Hp6BGRPLAJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadf07bd65.mp4?token=hpDzKUQAo4y3vFzdDbEFQfoaEG6lxWRKykMNdZ5VInSVoNOIlOo-Jk-GwQg29htFK9A6xWoi3rgwmZshIRm4D0MLLwKA8Zczeo_OJfbgHzIAuF6NttM0NF9NhYIdSdeYw1qmL7B9vg88ZihU3FOrF-ydYXHT9MbPWp7SgdnYMTN8dtGKB1VinkQZEjIgGdwZCyeqTqkdpHtakcps8U-6J52dHXSRkZrEF3BnUpIYkb08mJXxQUEMGcWxbJU_B_mTSSLSnCJ_jcH74dr8KftJ_ME8s2DgLHBW3uqkcMprajUFwSyWqG6Hb3-AX3tamsYPB6EYXV4VXKHVqjgkoE8r0GOOMk3CAjcbu0wL0XaQ2rSLP79YPAswqMnRLLoiY6Szc6DgR52tk-tw8JSBnOyvVdOvbv-_a6duh7TquW0I4ITpMYG7_l2MVZZGj9AY6z_flv6q8OOEmZkYjzd8H9yimGebhbHXO9eWjKaAj_y1AAHbaZAHKJW9brOOw_Ll32pCk-bV9hNERacerLEpjhbSujW90tMpoZjjUb85q1vub2WDbqg4Lbss-BZTWo0V-6hDDdQ8rFVUxqqegyo9ke10NQa-k3Gy1WpS0-KbuGv7D38h_mqpDFC6aT9Afahad-eOgBLT0Bihvy71o5oTOSoGMpEqLMEsSci0Hp6BGRPLAJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترابری دیوانه کننده آمریکا در ۲۴ ساعت گذشته
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/25381" target="_blank">📅 23:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25380">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : فیک نیوز های دزد تلگرام یک عکس‌مربوط به خبر ۱۷ اسفند ۱۴۰۴ را قسمت بالایش را بریدند و پایین را به عنوان کیل لیست جدید اسرائیل معرفی کرده‌اند که جو بدن! فاکس نیوز در این گزارش قدیمی میگفت چندین مقام ارشد در جریان عملیات مشترک آمریکا و اسرائیل…</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/25380" target="_blank">📅 23:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFjNhiCOTIdKq6Q9pNLZBp4hkZ63R8ifdxOP7EN0d6u0N0tkPcd0I3rQKxtLy_jPj0jQMBY6pc17iDgZZ-vrNc2ponU8JG0A1kIAxtTdHc97zScaNi8UZ3JHjIJRDt-RAMeJuATHXmX12wwDkvaxT1_NFgSw_b928_rKzGSJvaZtdaS6PLQblHfCXnro4XUG6Ho5dJe04b8AmDeUEZ7YTxiiIo__YELEkIaHytkb-78Sj3CuyiGbT6e5GTbN22cZ2oU6e6JEX30D86rhrFsFUYAz_vebXBc0QH-eI-mxEUAfgrNeZ6dyVqqvNKqMPhwXps4Aj8fATFx6QY6Sem7gPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌:
دموکرات‌ها، همراه با شرکای جرم خود، رسانه‌های خبری جعلی، در حال تلاش برای ایجاد روایت کاذب هستند که دونالد ترامپ آنقدر «نامحبوب» است که جمهوری‌خواهان شکست خواهند خورد.
در واقع، دقیقاً برعکس است. من آنقدر «محبوب» هستم که جمهوری‌خواهان پیروز خواهند شد و این موضوع با میتینگ‌های رکوردشکنی‌مان اثبات می‌شود (از جمله میتینگ در تنسی که تا چند دقیقه دیگر در آن حضور خواهم داشت — به زودی می‌بینمتان!).
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/25379" target="_blank">📅 22:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس، به نقل از دو مقام آمریکایی و یک مقام اسرائیلی گزارش داد که آمریکا از اسرائیل نخواسته است پیش از انتخابات میان‌دوره‌ای آمریکا، حمله‌ای علیه ایران انجام دهد. این گزارش در حالی منتشر می‌شود که موضوع احتمال ازسرگیری عملیات نظامی علیه ایران همچنان مطرح است و پنتاگون نیز برای افزایش آمادگی نظامی در منطقه اقداماتی انجام داده است. انتخابات میان‌دوره‌ای آمریکا قرار است ۳ نوامبر برگزار شود.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/25378" target="_blank">📅 22:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/905abba452.mp4?token=e12WttytAFHAETbwP8rQPNU4sSv6iJUxqDQMJcFFM68tgY7BaJfnhHvLye5gPsteYhRjuX5sCKf-9Ho0Emt40iHZalB7tIg6_j3mt19pEloZRyMnHdfOniYV_-MDlllk515H0rtitjF3vdZ8DajNOiEZjT9yr1p7UzRxSqjuzmLJkdAVEHWnLKewOpNNrMoD_Vc3yDvnw9VT3h7g8wTqzAQ4ZRPKTPTV3DJhiC0H9SYBiG5BnfdwIrXhVOTl85Ml7Rjx3fDJ0bfjErzy0zCJjcZZuIgg2VEQrKMvPNZVQAUIqTVZlMO3o-2hjE7zwwnuERm4MLTp8HraJpfythNTQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/905abba452.mp4?token=e12WttytAFHAETbwP8rQPNU4sSv6iJUxqDQMJcFFM68tgY7BaJfnhHvLye5gPsteYhRjuX5sCKf-9Ho0Emt40iHZalB7tIg6_j3mt19pEloZRyMnHdfOniYV_-MDlllk515H0rtitjF3vdZ8DajNOiEZjT9yr1p7UzRxSqjuzmLJkdAVEHWnLKewOpNNrMoD_Vc3yDvnw9VT3h7g8wTqzAQ4ZRPKTPTV3DJhiC0H9SYBiG5BnfdwIrXhVOTl85Ml7Rjx3fDJ0bfjErzy0zCJjcZZuIgg2VEQrKMvPNZVQAUIqTVZlMO3o-2hjE7zwwnuERm4MLTp8HraJpfythNTQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفت‌کش منتشر کرده است؛ نفت‌کشی که به گفته این نیرو، در تنگه هرمز هدف برخورد مین دریایی قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/25377" target="_blank">📅 22:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الجزیره: بمباران‌های اسرائیل، ۳ خانه را در شهر غزه و شمال منطقه تخریب کرد
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/25376" target="_blank">📅 22:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شبکه ۱۳ اسرائیل به نقل از یک مقام امنیتی گزارش داد که اخیراً میان بنیامین نتانیاهو و دونالد ترامپ درباره گزینه حمله به ایران گفت‌وگوهایی انجام شده، اما هنوز تصمیم نهایی درباره حمله اتخاذ نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/25375" target="_blank">📅 21:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کانال ۱۲ اسرائیل به نقل از یک مقام ارشد گزارش داد که اسرائیل تا پیش از برگزاری انتخابات، هیچ حمله‌ای به ایران انجام نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/25374" target="_blank">📅 21:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5697d70b60.mp4?token=pCszno_De_S4U0CVjdi6VyvgmI0ZuwD6DjeezZtoBqUF53A0MZoZiRn57eeP0P_Y70XAXtmmzYu8F2aQyO_U880B5xsiqTbmHXN1zBCq2XCieYqPl8UOu7OZEi04ItNAqWJPSzDOYOS8r255LYgihOq3q5Jb_wnRJjrvfRWFr8vclrkYyw2wYsz40JiUI67GUS9q9Htdvdm4RTNVOQqsOLNDy_ZMnS8CxcoiPGWZpXQmihzHGrDQr6CV2Hk8bkWpyxLU57kebiVSifXwfD477GQk69S5MnHILLMU4dvU9b_vLpJwaEna4w5MouwCwh7Y8piIIJMZdn0Kfe0UerIKVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5697d70b60.mp4?token=pCszno_De_S4U0CVjdi6VyvgmI0ZuwD6DjeezZtoBqUF53A0MZoZiRn57eeP0P_Y70XAXtmmzYu8F2aQyO_U880B5xsiqTbmHXN1zBCq2XCieYqPl8UOu7OZEi04ItNAqWJPSzDOYOS8r255LYgihOq3q5Jb_wnRJjrvfRWFr8vclrkYyw2wYsz40JiUI67GUS9q9Htdvdm4RTNVOQqsOLNDy_ZMnS8CxcoiPGWZpXQmihzHGrDQr6CV2Hk8bkWpyxLU57kebiVSifXwfD477GQk69S5MnHILLMU4dvU9b_vLpJwaEna4w5MouwCwh7Y8piIIJMZdn0Kfe0UerIKVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: شما گفته بودید که قبل از انتخابات میان‌دوره‌ای به ایران حمله نخواهید کرد. آیا این حمله اخیر در عربستان سعودی این موضوع را تغییر داد؟
ترامپ: ما این موضوع را بررسی خواهیم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/25373" target="_blank">📅 20:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cbf3c2b2.mp4?token=c0ltpZ0pj1t6V4xlAFcB58gOTGUf7xH9KQRr0-fZCrBb-ELkbI9zxQhL_kmVHeqLvcKLW17gaGzCrptmLx9eUCEa1_gV_rVpvicEZj-8jIqKJ7QuP4kTKfge3t7GU8U4nGbnyAadJBxLs0EYw95tFoTuRnHF-GCQqD64KvjTn4DdXrTtYHzGjcAPtlD_4Hm7XH7QRRhTWn9jdUIM38HfcIS2bvkM1_InMo9DUO8mXBYy4ti136TMu5ICWxVTFuFdYD_t-qMyGcbt9AjSekq2pkoFBG-QqbkFguTfqe8oVKRLtqp6FSKRKEz9ABXvNHCSXJZczuTJes2_BL_Dn7oaqa2dIclDSn-q0Ma5Ap379zdEioGy1Ul0at7A9G-hzvvj4HlBRLBvVpLaAY2NKtgbTipPOjLsZf2LGn9fPtzJ0H6nfj6YJ06reMh-i-nYDF1hL-WZzXlEab99V6BufGp7x3XlE4fQOgvaAYRhUzWImRbMw1x2d25ZnWebAG9VWoxlnmtg-TF7NXBCYJt_W6x3vCWCPk0R1mCaD9_1H5R3fao4nmlY8YPYWVuIDQDRNOfY27piCBtkZkLXyXrkrwhBZkrH4BmtArvThWZRnBXCjhyVj6owgfrVImJL0CjyYJ2Ysrueq1e5oHJmvaVK7HKvrTB63AmxQFfAhcM6kZqQVws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cbf3c2b2.mp4?token=c0ltpZ0pj1t6V4xlAFcB58gOTGUf7xH9KQRr0-fZCrBb-ELkbI9zxQhL_kmVHeqLvcKLW17gaGzCrptmLx9eUCEa1_gV_rVpvicEZj-8jIqKJ7QuP4kTKfge3t7GU8U4nGbnyAadJBxLs0EYw95tFoTuRnHF-GCQqD64KvjTn4DdXrTtYHzGjcAPtlD_4Hm7XH7QRRhTWn9jdUIM38HfcIS2bvkM1_InMo9DUO8mXBYy4ti136TMu5ICWxVTFuFdYD_t-qMyGcbt9AjSekq2pkoFBG-QqbkFguTfqe8oVKRLtqp6FSKRKEz9ABXvNHCSXJZczuTJes2_BL_Dn7oaqa2dIclDSn-q0Ma5Ap379zdEioGy1Ul0at7A9G-hzvvj4HlBRLBvVpLaAY2NKtgbTipPOjLsZf2LGn9fPtzJ0H6nfj6YJ06reMh-i-nYDF1hL-WZzXlEab99V6BufGp7x3XlE4fQOgvaAYRhUzWImRbMw1x2d25ZnWebAG9VWoxlnmtg-TF7NXBCYJt_W6x3vCWCPk0R1mCaD9_1H5R3fao4nmlY8YPYWVuIDQDRNOfY27piCBtkZkLXyXrkrwhBZkrH4BmtArvThWZRnBXCjhyVj6owgfrVImJL0CjyYJ2Ysrueq1e5oHJmvaVK7HKvrTB63AmxQFfAhcM6kZqQVws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: من جلوی چین و تایوان را گرفتم، اما جایزه نوبل را به کسی دادند که هیچ‌کس تا به حال اسمش را هم نشنیده بود. فکر می‌کنم او به‌شدت ضداسرائیل است. با این حال، جایزه نوبل را به او دادند. به نظرم یک جای کار در نروژ می‌لنگد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/25372" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5bf39d5eb.mp4?token=VoOtw9nXcB1jTQ4djF3c3PxDcx-Ll4JgWgI3NIqQitBHJfV496JkVFVI7ZklJlsgfflbXJT7kNh2TrAygvSIJqN1IMM_i0EOM7SYUtC3kZFOfK0ZNWF_VaNK8zbRGAOrA7FVUGpOY5JJrwpaJqgLtqxlKFxD25nUyQ1rpJl4w5daeTt0l4M3IyWDdWmieE0chrCwIfZaSQMgXu1fBS9vbGnigHcdgo1hmYGwg82zG_9T3YG47eNBjxFYoFwsUTJ8NeJFBzF9CR-QawNj9ntylcEqWwl2Tlv0zV1-HMGoYbA7Rva9lMktPnR6z9p-AXWL3274lxe40eFtWbR42DYbOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5bf39d5eb.mp4?token=VoOtw9nXcB1jTQ4djF3c3PxDcx-Ll4JgWgI3NIqQitBHJfV496JkVFVI7ZklJlsgfflbXJT7kNh2TrAygvSIJqN1IMM_i0EOM7SYUtC3kZFOfK0ZNWF_VaNK8zbRGAOrA7FVUGpOY5JJrwpaJqgLtqxlKFxD25nUyQ1rpJl4w5daeTt0l4M3IyWDdWmieE0chrCwIfZaSQMgXu1fBS9vbGnigHcdgo1hmYGwg82zG_9T3YG47eNBjxFYoFwsUTJ8NeJFBzF9CR-QawNj9ntylcEqWwl2Tlv0zV1-HMGoYbA7Rva9lMktPnR6z9p-AXWL3274lxe40eFtWbR42DYbOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: متعهد هستید که نتیجه انتخابات میان‌دوره‌ای را، فارغ از اینکه کدام حزب پیروز شود، بپذیرید؟
ترامپ: البته که می‌پذیرم. اما نمی‌خواهیم تقلبی صورت بگیرد.
خبرنگار: پس اگر جمهوری‌خواهان شکست بخورند…
ترامپ: نمی‌خواهیم تقلبی صورت بگیرد. متوجه منظورم هستید؟
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/25371" target="_blank">📅 20:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ: در جریان حمله به فرودگاه ریاض قرار گرفتم و تصمیم خواهم گرفت؛ شاید به حملات عربستان به یمن بپیوندیم
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25370" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ: زلنسکی بارها می‌توانست جنگ اوکراین را پایان دهد، اما نخواست , زمان آن رسیده که اوکراین رئیس‌جمهور جدیدی داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25369" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6ed719e9.mp4?token=giQuTmmH9k8ARQgS9wG0gk4O8E1ta5gMycKUEZSz4LrGE4PvzHbCWbK2T-9gIcS3_fKrx9YIfb254QMaEVTeLC237ECUez9UaI2nCEoF_VC6stoA8AI-RsLsz0bV7wMhYEbEBhYyr-O2FO8kiJM0PE68zXvA6-2VJwYeRR09dit03f23wXZtyx9HTGFYg1hLvxcBBPnto8RckEKkeGCxclBhdxm6jBLzVL-GrJ4-n0ADVaOabQSD5Qs3X03TtV38878GdgcaMoiLHMAcFuzrdJ2Of9yG8Q_9iERySL9NNYbTWGkSgBq2cgOp9qZ-u5hROiZQQivCZSSUgkunUcUTGY_nIKiLzKXPjFhUed-DXqgY8-Wi_yaCd_ClJ2XDLuXMtGbPrSgNpX7cSqNsNTQkX8JXeH2qPg4pS2vDaaH1QBlXlhk2odASLBImZikMn7LnadTYJ4ZIBnbLTf94aUHp0hyQvWdnFiArVuy89QGDcypH2Ckfkv16i-UpMm1WEm7FnJbFFT73PaRga3xvj8TkTI9ABT1AU0vEQyMguXQ3CHHnXb4pPtnTxycLxW6dQpVvTXGynx1ya64y3viwTH9bCS1xCgFW1wbzi_m8WV2xuhmuV_XroQyGpgQnbfScmVCM9nAFWb72E6vpkjjrMfo9oxcI3-5b9piWpCZEOoY-0Ao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6ed719e9.mp4?token=giQuTmmH9k8ARQgS9wG0gk4O8E1ta5gMycKUEZSz4LrGE4PvzHbCWbK2T-9gIcS3_fKrx9YIfb254QMaEVTeLC237ECUez9UaI2nCEoF_VC6stoA8AI-RsLsz0bV7wMhYEbEBhYyr-O2FO8kiJM0PE68zXvA6-2VJwYeRR09dit03f23wXZtyx9HTGFYg1hLvxcBBPnto8RckEKkeGCxclBhdxm6jBLzVL-GrJ4-n0ADVaOabQSD5Qs3X03TtV38878GdgcaMoiLHMAcFuzrdJ2Of9yG8Q_9iERySL9NNYbTWGkSgBq2cgOp9qZ-u5hROiZQQivCZSSUgkunUcUTGY_nIKiLzKXPjFhUed-DXqgY8-Wi_yaCd_ClJ2XDLuXMtGbPrSgNpX7cSqNsNTQkX8JXeH2qPg4pS2vDaaH1QBlXlhk2odASLBImZikMn7LnadTYJ4ZIBnbLTf94aUHp0hyQvWdnFiArVuy89QGDcypH2Ckfkv16i-UpMm1WEm7FnJbFFT73PaRga3xvj8TkTI9ABT1AU0vEQyMguXQ3CHHnXb4pPtnTxycLxW6dQpVvTXGynx1ya64y3viwTH9bCS1xCgFW1wbzi_m8WV2xuhmuV_XroQyGpgQnbfScmVCM9nAFWb72E6vpkjjrMfo9oxcI3-5b9piWpCZEOoY-0Ao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیراندازی‌های متعدد در ایری، پنسیلوانیا. به نظر می‌رسد که این یک مسئله خانگی باشد. تیم ضربت به خانه رفت و احتمالاً 9 نفر از جمله 2 کودک جان خود را از دست داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25368" target="_blank">📅 19:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال ۱۴ اسرائیل : سفیر عربستان در یمن مدعی شد تنگه راهبردی باب‌المندب از بقایای نیروهای حوثی پاک‌سازی شده است. محمد آل‌جابر این اظهارات را در شرایطی مطرح کرده که طبق این گزارش، نیروهای ترکیه و پاکستان نیز به‌تازگی مستقر شده‌اند تا از نیروهای یمنی مورد حمایت…</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25367" target="_blank">📅 19:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏یزدانیان، معاون توسعه شبکه ملی اطلاعات وزارت ارتباطات: در صورت وقوع مجدد جنگ یا ناآرامی، احتمال قطع اینترنت وجود دارد. تفاوت احتمالی این دوره می‌تواند این باشد که اگر قرار بر اعمال قطعی یا محدودیت در دسترسی به اینترنت باشد، بر اساس آنچه رییس‌جمهور مطرح کرده است، نقش وی در این زمینه پررنگ‌تر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25366" target="_blank">📅 19:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حادثه‌ای با شماری تلفات در فرودگاه بین‌المللی ملک خالد در ریاض، عربستان سعودی، رخ داد. به گفته چندین شاهد عینی، آمبولانس‌های متعددی با شتاب به محل حادثه اعزام شدند و افراد از فرودگاه تخلیه گردیدند؛ همچنین گزارش‌هایی مبنی بر مشاهده «خون در همه جای» ترمینال…</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25365" target="_blank">📅 19:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25364">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کانال ۱۴ اسرائیل : سفیر عربستان در یمن مدعی شد تنگه راهبردی باب‌المندب از بقایای نیروهای حوثی پاک‌سازی شده است. محمد آل‌جابر این اظهارات را در شرایطی مطرح کرده که طبق این گزارش، نیروهای ترکیه و پاکستان نیز به‌تازگی مستقر شده‌اند تا از نیروهای یمنی مورد حمایت عربستان در عملیات علیه حوثی‌ها پشتیبانی کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25364" target="_blank">📅 19:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">لاکهید مارتین از رهگیر موشکی جدید PAC-3 Edge رونمایی کرد. آزمایش این سامانه قرار است از سال آینده آغاز شود و استقرار آن برای سال ۲۰۳۱ برنامه‌ریزی شده است. این رهگیر نسخه ارتقایافته PAC-3 MSE است که برای رهگیری اهداف در ارتفاع و برد بیشتر طراحی شده و مقابله با موشک‌های هایپرسونیک (فراصوت) را نیز هدف قرار می‌دهد. PAC-3 Edge همچنین به جست‌وجوگر جدیدی مجهز است که با افزایش مانورپذیری، دقت رهگیری را بهبود می‌بخشد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25363" target="_blank">📅 19:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">روزنامه اسرائیلی معاریو: آمریکا از اسرائیل خواسته بود پیش از انتخابات میان‌دوره‌ای آمریکا، به‌تنهایی و بدون مشارکت نظامی واشنگتن به ایران حمله کند تا مسئولیت سیاسی و پیامدهای احتمالی این حمله متوجه دولت ترامپ نباشد. به گزارش معاریو، واشنگتن تصور می‌کرد اسرائیل…</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25362" target="_blank">📅 19:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJhpjsWFRmGPWLG_sr7r-RRT4nI5W41s-F0Bc6AstYGyok4vsosONuDVcmww5A9P83E0X97gqWNICOq5sgV8znsAlu0A05MduAAKu-6648jdI88uboe2Qu-MSjUVcDNKDwap9454cE6fyRIYGIo8riEHiVJMK7vQLYwYSBByP9M3vCCvzBn_P4Ug51ba3L6xvUOCVMP6-OM5qXCq0YPT20ccoJJirn3Sv5gIvQmtwYOqgvX6gP6_XWXQrki0IAadXsivjdf5eJyn1fGQZ9SBtqOr7nSFwD_FVEXNLmS7fjjWvyvGNBJr76OhZWT6JaK2sy8ylDB8XuZWjy7gW6rw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/731112f8da.mp4?token=sxFQxrJymFiqOJgdvGZozkeKKhTVw66tlfpxYnJh8TWSlGpu5cLvR2kmwmoDfWSlQe_qiP2CgnGHc9M9G1K_eCWH3b3IC16rV03V_iHNJuYjSQLDZjz9YskuByJXWmuZSdKeWm4_UFRcSxIm7I7CJHdhI4aviwBfDo5uJYYFgAAp90WLTXoE-mntphSPo7GTM0xNgzpjTUJH3ZeH_6Guednk44zc-OiyaozkgS8jMXMBz_ZGhe6e-5NcBv8owtxx3N1uWWYk8ZyY9vYUs5-MfYHP3OfUPPf6a-kCnQMl1O2qhnj1pnwlquvMKpYNO_GHTPB12QQUtZZ6jPM8dl16RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/731112f8da.mp4?token=sxFQxrJymFiqOJgdvGZozkeKKhTVw66tlfpxYnJh8TWSlGpu5cLvR2kmwmoDfWSlQe_qiP2CgnGHc9M9G1K_eCWH3b3IC16rV03V_iHNJuYjSQLDZjz9YskuByJXWmuZSdKeWm4_UFRcSxIm7I7CJHdhI4aviwBfDo5uJYYFgAAp90WLTXoE-mntphSPo7GTM0xNgzpjTUJH3ZeH_6Guednk44zc-OiyaozkgS8jMXMBz_ZGhe6e-5NcBv8owtxx3N1uWWYk8ZyY9vYUs5-MfYHP3OfUPPf6a-kCnQMl1O2qhnj1pnwlquvMKpYNO_GHTPB12QQUtZZ6jPM8dl16RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادثه‌ای با شماری تلفات در فرودگاه بین‌المللی ملک خالد در ریاض، عربستان سعودی، رخ داد.
به گفته چندین شاهد عینی، آمبولانس‌های متعددی با شتاب به محل حادثه اعزام شدند و افراد از فرودگاه تخلیه گردیدند؛ همچنین گزارش‌هایی مبنی بر مشاهده «خون در همه جای» ترمینال ۳ منتشر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25358" target="_blank">📅 18:39 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
