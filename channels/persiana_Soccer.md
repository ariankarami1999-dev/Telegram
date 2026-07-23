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
<img src="https://cdn4.telesco.pe/file/poSPcI5yPdJdgU3hrGWzQ8eNlNE3zapgCh-p1KY9EzWFshZrrmk6g8xv_jMz-lhmpSyZdgVhD96EHbQiIylh6-Bwd9mBM_kB3yOweKYxrHTPobLrvL_8U-ytcw3NjalGhISMqmKXBIqv1jTAiCzuTQkO_J1nsIYUqcpCwS_yLrudASTBEtKh1kC7fW68qXIpZshIMQLuPVh-glr5Bru6M-W0_R3wK2bckl5dJVscMkdk_HhOKeFxve6XW0VkbzPAViy-a_52UxoQOBpAMwnSqqC-b79L0UOn2o6CdmcpLuPMI9F5ffHC1egyLumEt46PMdoKSbNdP-qD50Dyt8KtQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 555K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 13:47:57</div>
<hr>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=DkttDk_L8YCwlmjYANErDHhniJKAM0ky1GHmbSc4ron1iZVFCaKgOuc-rpOVRrP4raimdFt21M5DkuQgjn8_7m3WfDlRJyW_XkK664SOGrROakoGFvwHJeZvMNmddcpjtcJ2ccjJT0nzqAnRfLYNb_gZRpHVxd6L4woiJr8jj47hoteIonQ3FlzvT6hoLRG1lqsQSBMcHUmX_QPNHEPCHUDyxgrRxF741jBSlI_gU47B9uYUxXYoSeW2zRG_bB6KbCyLtADqJOqEFsDvD44UeU4s-660guNWZMwzUDLX7lemRuMTA0FBshIMYiFMYfPg8K_JIFNy8tjDMc5gWx_GZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=DkttDk_L8YCwlmjYANErDHhniJKAM0ky1GHmbSc4ron1iZVFCaKgOuc-rpOVRrP4raimdFt21M5DkuQgjn8_7m3WfDlRJyW_XkK664SOGrROakoGFvwHJeZvMNmddcpjtcJ2ccjJT0nzqAnRfLYNb_gZRpHVxd6L4woiJr8jj47hoteIonQ3FlzvT6hoLRG1lqsQSBMcHUmX_QPNHEPCHUDyxgrRxF741jBSlI_gU47B9uYUxXYoSeW2zRG_bB6KbCyLtADqJOqEFsDvD44UeU4s-660guNWZMwzUDLX7lemRuMTA0FBshIMYiFMYfPg8K_JIFNy8tjDMc5gWx_GZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIT1fTrPzu4C_PhQM5ozlU9oNZHkzbbUsD178TQLukRksm9ARnJ6Wngptn2IpJOOs4Rsm8gfwbzI0QCWIF5PG3H3a2dzxXNrKnIHFTsTc_oiXZVL43EwQDFySGul8__TwPgxqBhbo2ksc8XlSkTc6MNbLJAhW4HP6rgSf-o8LYqeK-1CJfmFlufxDsgXpbJxL_91c0LaTpdTBVUqwUldOCSetjP3TFNQSCj2RnbOE2CLpWa_5eW_32h0_-kqzcOF35BYKd3j7tfaM1nHElxeAh4VG17QFVw7Bey9o6HYF43jV95P5-XsQ0vdNKjkAQDp_BoYFV4WfqhUBiUzWq8htg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=QBPmLcMwIhVaY7HRXtnXm_ft2r49Z_aklSO41dLU0kIpUdH4lZ5QFkGwjaRpstlZ5h_awy4jU3d-JtqKqCM4Nj2I03rXc3MSR5wxxI5K3-2Ii-LDPN4DvY_WqLoBFYe3dwI5S4uq7SZGCFx2Bg0Nz28dmuLaKpgvO5bcR1Gii_h7MQEFEy3mAjILFbGf6Nwewt616SZafYcs97BllFJCbEpumaF_EMkbq4F3wl53eHTI3JHW-Bu44zYMWm6WJMiuHpLpyA2wPYvltv_2EHGV47wGq8iZgD9FnuTWtYH2pKkHccYiFeCxH2gOembDHhQ2aLK8E12xFqYsffWw_NpS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=QBPmLcMwIhVaY7HRXtnXm_ft2r49Z_aklSO41dLU0kIpUdH4lZ5QFkGwjaRpstlZ5h_awy4jU3d-JtqKqCM4Nj2I03rXc3MSR5wxxI5K3-2Ii-LDPN4DvY_WqLoBFYe3dwI5S4uq7SZGCFx2Bg0Nz28dmuLaKpgvO5bcR1Gii_h7MQEFEy3mAjILFbGf6Nwewt616SZafYcs97BllFJCbEpumaF_EMkbq4F3wl53eHTI3JHW-Bu44zYMWm6WJMiuHpLpyA2wPYvltv_2EHGV47wGq8iZgD9FnuTWtYH2pKkHccYiFeCxH2gOembDHhQ2aLK8E12xFqYsffWw_NpS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur1OfUBdn70HhtK5vDyYNONIbGvN9v67zx3ogAYV9i3AFjs4_y8O358j5ucieDLgmByhvRPK59j8onOUBztuQnIP11h_QhpYeUlqAZwp4CzCYQ_VUyECUaIxiVE1sDgQOyjNbvtp8hhToYtG_QU6RaYBVq_K0JLBuGVXkR-JVcwuwn2iMI1w5G7mO4dyhaMfjetBZ771dUyOfGnUv7Fn8ULra7UxsGITyJdVmhGtohQBhGGVLzHdBE1jlGenStg6aL7c5AZsHJuioiLNrXpmK_X287m1IwbkvtDKTFfn67sKty2X33__5Y9PeJ1jRHlL6Y-9dbU8ltQbp6jOTl_oNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhL-7w1TUQ_33jcbFyVaTyHSpO43OwVbkXaT16pg-m9LWn6KBKmgE_PVFlXTiawy8RZetw8W5DwysSWNdhuWzGvThaM8oyUm7Cbff4aDwOMm7jWqnNpkByOu6HDOWJBdaYvaMrpbvfCiVuPg2botEwBI_vUM3NX2DVgz_-U2LNXrGsRfyCAx4k1np8ai2ZCBjm1rQjYRVwEAirhEonOJ4xcQJorBqYrVSVm3gNDREFIgw6mRB_cS5N1Cn-qWsLkyyXxgMLgNlk6hXDTGsd99-jEI-Sx6DijnxulP0G-G_96RJXPQfPh03snrd0LY3W7KxZdH9vtrPj2TYOYgzb-euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3uSNg7L8uWofXmLPQTIWhn7Hl5KVvVUv6BjrrP4vdv74YopVYBmE7_OVjp67gpiyn9Feims7H2-oKIcAPLZNxpXoZVC5sPPo68XyKMVIf8vHtRSFnDqg_x2k64ylRVmd-pWiF6lQG9sUBhhdbOhV_imejhnvqmVu9zcHPqxdsRe8-RBvIRuNbw_OlNi3d0S9__Xp-K68bvB6gTdKgFPICZo-HZOJBBP3Gn0UnYCv7xozKizOJcOCx2DzzRtUfy4-j5ArhMxu0rjUxLqZRK4uxUlfSWqEPja7JaOcdQW359vykt-G6OuD8ZhRB4ALcRzcK2GYjc_k34uXVJDli4nYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6BQ2CTzMycdQfKgUqs1yGsHdzUAqXA6-VdS-F2QcJIfzKQL6M8kdjOf_oCJZydW3-zf9Bz5u4H32hAMhcGF1zpixw82gG6NHDfbuTzUbb3zHXLnUKUMHVPNNGk3swBVWtZuBBlsAUTRXyiFAplekbbiEeeH8YhkF-6m8Rrgj6Is1cMu2_FtSfPku78vJKWYLLDM88clSkJqyXjzFz9h4w61NV9gaHQj2WsIoYYG3Ic-P7btHnJpEW2d7YTJlxCV6F4_L7CKQr7001y0ErJ_FOPejCO-vj1UFzG0_tkmXWPJaXh_3CEidJoAPRPIdYGPf7wtm__CxbO15DvFE3IU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIHrhGH1pginezTNwD6O6DitAxlxUpWXaKBuAWsCNxgPPGeno17E4AdUFatZxq1gSEwhbQc79l6DX2PxccafKddqN2j4gW27vwzqJN54gPqthDp4j5A9fVdBMuXrPmZC0tDrFZbrqoQtULt1bf_0juWz7EvsVM_8aTcnijaT05yqO8dBYFLHCBnoua3nM6IKnTWNIA3-tLyPg8rgM_43vvLkeJDmfuPaaXnYuHymfh1FuuONm5lQutLEQCpXl9zyn16Kg_Qlh08b67ulxzvff5h2hWMnNwKVJrgMEhSL98FeJT9HZcPfV1TTZC_-0gIT5Mn81jS1P6WUVWVvKbCyug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUAiyg11op--ytOQghfGqaBnUXCmvMAXbCjlUGQGNKJcdaEyRVRJwf9bsqmDxItU3xiYgCx-J5gCmxpI3L4kJfaTTvyCFuzrTd7YHFTHnhI5i0cxT115r7DzZr7mo0R9YXSai4Z8Fbw9Jq8MTBVBgovmy_4xCbr24hqrBEtAgNPg6AQnK99f8t3Wsyyu6RJMFx3wSxv8UJa6x2-V5JjIPlRB3CkTMO3LJZ8e0ypzavpfy-_c7XaM2JpRzqEZYPYBVOutcFXZaMCKl3wcJiFY4ZQYjb8C7iutXoWm8WFjq70ZMOg_RHPtEPxxH38QsjeiyKr4UysljYXt_WFBbRvH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=YDCiPPh8RcBvFHKiteHA7PjpNUGczdROZxTYh6G9KltovGfyP1THDAEYhlfsgcyyeCAi-dXx6So_AXD9tRjEJo9DT1hOL-dDIAhczFOWqZYXjIwjKwvhQfSPpPymC-IzdSgI7RGdP7ib5BquHnHiDyiURinLtQS32RbJj4tbvUt51LViTuphMHlvapyukvRCNHJNMVZzMluGyl_Xn44XoyqV3EVUXg2hPXUx0Naw2xMyF-fqZlzXURiOr8U98Ow4B-DJCCqN2x6R4VzwZaX5itk3-UzOKCW9dMHxxOr4nf5bJSMP1bU6IaU0L3dyX7ZR6CARKZixyLco2-b57TRSxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=YDCiPPh8RcBvFHKiteHA7PjpNUGczdROZxTYh6G9KltovGfyP1THDAEYhlfsgcyyeCAi-dXx6So_AXD9tRjEJo9DT1hOL-dDIAhczFOWqZYXjIwjKwvhQfSPpPymC-IzdSgI7RGdP7ib5BquHnHiDyiURinLtQS32RbJj4tbvUt51LViTuphMHlvapyukvRCNHJNMVZzMluGyl_Xn44XoyqV3EVUXg2hPXUx0Naw2xMyF-fqZlzXURiOr8U98Ow4B-DJCCqN2x6R4VzwZaX5itk3-UzOKCW9dMHxxOr4nf5bJSMP1bU6IaU0L3dyX7ZR6CARKZixyLco2-b57TRSxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKbK4wD3Fh6Kbk9HtkoT4SJZK1-66q4VMZK3AdYbEPv7ufuqITZb3qISMVmBK6bas3xQ302_V02_0K27KKCtEHzBwhqAcByst1dQFywYsQCPRwa0mdGRzfGuP6WDRZVEzTVPADDENdLOOWq7qtXD2dadXsS0elkz-H5CNi__XFxVQilY-oOf5X-MyP_2Fpcg0KvsBabeB10zvZy1JvX4GIZPzqNKNwg1Kpw_cZ6_iKmzNWF3KBsDXBYZTcZyNFK8-EqkZPEdBnzH8Ej7FjOyMOyaEiF9njTzdmnKkxcV0qTlSDPQ4MDGQc2RM7m2cV5IZmQmdK7vhBfEGjpmZUZCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSuZ_MLKdZldb2qdw5pDQ6OZD0aoTz3aRfbRIUyUIZf5RJaUoAo27EmixI--QBSMWj7BkIHlvSiFyZaGQ_uzZVMVup0WSwqx8_b50a7YF4vFx13EHApTMRMSiD1wDd_PECKICvJD7Z9UX2EfIH2B9GNST2Ycdw270osXYEquwg-GQvnnSPoJXJ3rVOFXJgyYnnWZfKmpSF5qABMpTS0YA1XP3tE8dvZLVf2UgxqN-yZK3-abMT00iQfoEb_m4PV8ELn3B69PBfC0N34JLYd368zhQqe4y95ygzmg3WeeAlm9UbMYLvs1s6jUJ_AdRZpcFP72Su3UbQeltprzKxnZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZkCYgIYV8y3JYVt-Yuj0XQyWszcVRJcyigYZSf7mORjoP7GIgqMWkzAhcIkCdCJGZIvvBXpC5qh554APCVwserbybHv4l2DhQnroKl8m48BVQ9Hy7rLL01Lnm6gMvpgbnmGHQoAl9W_aNiZyrWmdP2ct8Y20C-LuHldYCRREBh9I6PMxmh6M6EU4fpJPk4ie66Yg6IexPQjBtq72rg6HPS_R6Fc5mByWoKv8ZvTHNMMKwH706YM-XoubZCR1zCvaKWETzUCq4Nb5JHlVy2oh_qzO6CO-d5rL2t3can1Ye43a6DKEdf7RWP5imHvbou9M_PEgp_cWaulIqDNR9grGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TudvMNuO2Ukk6PkXPQBUZno566PU96Cfb-SKAuWGQR2oo2vSsjXtVGYWXSxraDNJNdxwE2zBVm51RUYMETBccjSjJVMjyNRYZmqRzOlUbflg0p5gdADwJeKI7TEF6wQUOWGdxbGKfkNfc4QZgBl4UXLKR-I3vk8ZeL-CYLsu5BKPU5WDRei8vFaA3tmTYAveCGCf1wasr7ETIKKvCTuZtmkXkbqE4ImoIN_y4HOspjih7XF9f5cn5RnNg5vZ12cOQFyXBsOGe7DVvLz9qKhvh3F-0ZWw1NJhMIqSB3AE1HOHStSNSKnJD0FxYtIq6BsNYIKCvxbZ3zkspXjnNaECgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔊
با چرخ بخت وینرو ، برنده ی ایفون 17 پرومکس شو
🔊
💰
هر هفته شانس این رو داری که با چرخ بخت وینرو حتما برنده باشی جوایزی مثل گوشی آیفون 17 پرومکس ، جوایز نقدی و فری اسپین
✅
حداقل مبلغ شارژ برای دریافت شانس 10 میلیون تومان در هفته می باشد
🚨
ورود به چرخ بخت وینرو
🎲
با وینرو فرصت برنده بودن را تجربه کنید
💎
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr1
📩
@winro_io</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26331" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=L0O7i81QtjcuWjZSrGqMsBYhTahzvwj6s02j0g0xHal7oub-HCotan9OrC9df7b2sXF-EqHfD-Du4y7aa87Vk8WvwYewVCXTmSdUR6Qbk9KTgoxHyJT-LInYlz54VJzlsBzZloXYJSlIfR7_ugKJJiwkmgZMBgyN9ZHiAl4DDfVntZlTFzaMkivHEdURLG6K45AS8l0417b6H9lN5A6yfxm9Xmuuv3s8c-AYPQL6i39kOakQ2OlXZKJdCwNUrIPfjYyyeH9epfSSUcLMPiixjxtHl-4jWbXgsfTRYoxSPYWLDb-MkK0tlorkJPdFKfNlrE08vXmaW3xuRHcHGVD6YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=L0O7i81QtjcuWjZSrGqMsBYhTahzvwj6s02j0g0xHal7oub-HCotan9OrC9df7b2sXF-EqHfD-Du4y7aa87Vk8WvwYewVCXTmSdUR6Qbk9KTgoxHyJT-LInYlz54VJzlsBzZloXYJSlIfR7_ugKJJiwkmgZMBgyN9ZHiAl4DDfVntZlTFzaMkivHEdURLG6K45AS8l0417b6H9lN5A6yfxm9Xmuuv3s8c-AYPQL6i39kOakQ2OlXZKJdCwNUrIPfjYyyeH9epfSSUcLMPiixjxtHl-4jWbXgsfTRYoxSPYWLDb-MkK0tlorkJPdFKfNlrE08vXmaW3xuRHcHGVD6YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌مهدی‌قایدی درسال‌های اول حضورش دراستقلال: رحمتی و حسینی بشدت‌باهام بد رفتاری کردند. تو یه بازی درون تیمی به حسینی گل زد گفت دفعه آخرت باشه این کار رومیکنی‌ها! مهدی رحمتیم گفت این کار رو بامن‌بکنی شلوار رو از پات در میارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=FsDTzig3t9LNc6dmqr2LbKAczK58Z4d7RYupy1gjrj7UrBmLrPJn_p4LnpPg9gFEHuj9IrD6DdCQZQDzm9AF1AcQBkqfa4jhDsRB8WbnoQFzwmRQapSlU5I1oosurqjPM2oDWi2Pii80V7kHhUz1-yxZSV1Jb7pHQH6y8L4DtSW83UmGIUJr2zxJzwbXqUlfOgfuZHAbzb_YT20y0RDAQMsMdxk6OhluAILQxwQ1LB-zDwYlExEsNDoJffuupEcBE3NEjSdbr1JHzz8rKz2RwuvTkswWq6i_oAmTxr3R6ClqC-Q1Ptt34kVFs8Ccqt6YgYO0jCYGeDK4kWnGRZqxBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=FsDTzig3t9LNc6dmqr2LbKAczK58Z4d7RYupy1gjrj7UrBmLrPJn_p4LnpPg9gFEHuj9IrD6DdCQZQDzm9AF1AcQBkqfa4jhDsRB8WbnoQFzwmRQapSlU5I1oosurqjPM2oDWi2Pii80V7kHhUz1-yxZSV1Jb7pHQH6y8L4DtSW83UmGIUJr2zxJzwbXqUlfOgfuZHAbzb_YT20y0RDAQMsMdxk6OhluAILQxwQ1LB-zDwYlExEsNDoJffuupEcBE3NEjSdbr1JHzz8rKz2RwuvTkswWq6i_oAmTxr3R6ClqC-Q1Ptt34kVFs8Ccqt6YgYO0jCYGeDK4kWnGRZqxBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
بدل ایرانی مارک کوکوریا ستاره چپ پا تیم ملی اسپانیا و باشگاه رئال مادرید هم پیدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=lnk4F9ZtjaIQA-0zKLviKZL9cTcL9bSnPVJz17hqSXDmgaQVO9P_uYGnofIWs7yGAPGeljWWhqHZyI970o3zrpEWuP95h576AMZCglkJITZvp9DHxJ90_n7CwEeBXUnSomgrt-DC2rEH_TGcD33wQbfDlmhC9EZcOIkz_WXPlzmRkmVau2T1Cx9BbVzt18LwQ6ZbyMNscsIFLc0nM0UE00ZAXaXou9bdJSq0aLKhfo7cNZfESyea2X4N_jc1u4C4DorqOAi9Nc1wuaXmrZtqxRivIzVenT-ZIlQEtRM5beuVOQ1lqIh2qhsGZW-A5I-dR1Os7w-iGinQLE7dGIDI_I8--vPzA8Ltrf8yjzfdrTcNRkLp2VFWPHmANWmt8cvfOkC4PN2vKcwaYkJVvRy8v_NASlhxabSYOYMBemywKt8bie7-Omhjpv6XXDzV5OOichIh-uQ6X2OsK3ZZUJXeazfTAke9yn8vS8DQ1CfaoueSH2eRLRWm8W2DnXogLK0f9pRi0P8H8DyI0Qd2yAoQusN0emF0N4BLmFY3YHWPeu2NYo4EU1Hmx03mqxglZPgfkFh-Nhr5c02pdDIw8ClBSa-b9U5MyYsGpOBuIuVxyriN1W28Klav69TqE1vcddApYr96euFjEnoVeQOSotkhFtbIVjk2DhNzgj2GaAf0_KE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=lnk4F9ZtjaIQA-0zKLviKZL9cTcL9bSnPVJz17hqSXDmgaQVO9P_uYGnofIWs7yGAPGeljWWhqHZyI970o3zrpEWuP95h576AMZCglkJITZvp9DHxJ90_n7CwEeBXUnSomgrt-DC2rEH_TGcD33wQbfDlmhC9EZcOIkz_WXPlzmRkmVau2T1Cx9BbVzt18LwQ6ZbyMNscsIFLc0nM0UE00ZAXaXou9bdJSq0aLKhfo7cNZfESyea2X4N_jc1u4C4DorqOAi9Nc1wuaXmrZtqxRivIzVenT-ZIlQEtRM5beuVOQ1lqIh2qhsGZW-A5I-dR1Os7w-iGinQLE7dGIDI_I8--vPzA8Ltrf8yjzfdrTcNRkLp2VFWPHmANWmt8cvfOkC4PN2vKcwaYkJVvRy8v_NASlhxabSYOYMBemywKt8bie7-Omhjpv6XXDzV5OOichIh-uQ6X2OsK3ZZUJXeazfTAke9yn8vS8DQ1CfaoueSH2eRLRWm8W2DnXogLK0f9pRi0P8H8DyI0Qd2yAoQusN0emF0N4BLmFY3YHWPeu2NYo4EU1Hmx03mqxglZPgfkFh-Nhr5c02pdDIw8ClBSa-b9U5MyYsGpOBuIuVxyriN1W28Klav69TqE1vcddApYr96euFjEnoVeQOSotkhFtbIVjk2DhNzgj2GaAf0_KE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش مهدی قائدی به حرکات عجیب و غریب قلعه‌ نویی کنار زمین؛ خودش از خنده رود بر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=T4uxifSQcKAf7iEzyWmGCGk7lj6w_xWvmlfZc5Y81SGny1LWC_uhyXyP9xg3Yt3sVP8snF-_P0lmdjmRV2LrG_re3lScnySxoHlVJP43EeT9InWg8b6GuNleCWRGlyswF0h7RY6cURUlBd7_8pQ2FfHwRFUGkfnrO1kbdPaPiauIjBblWah64pUFPBG5rSZLgStsI3X52C4-Q00vAmHlechQrs3Z24T_In-CPaVe3mHNfDW6jkv0XYJperl5QSUOFdUSrVnO0vLnqGH0fkQrtbv_IfzqNh_-AunrN0iJ4IEJZEjGMFImfAS5ayFCiQp_yDP6o5GcU99ualNeJc_iQG192mt4jqCEqx6Ed0tVwLP9qDhCpzFlZmUHk9AOT-9siBC6Jdp-VQLtK8fLlxUtPtbHT67ZWZ23-PUDy7IFfgjQRzbKOAhBCTgHvhgL1FDz54BcP2GpZEx14a0h1AfKwiQEX9CNJcvA0GMun78gWjT2n4h_e3j-0GxwR7Te6meNdRV1BkGxmId6c9aekceAuRp8aQO8o_67gQnGJXoGkVwbP5RiV3tudmpNEKIXyLuTVFyzrqNRj4zbSLrfvVQA37m44u_SmdLiHFCSiB66WGrqR8Aiu_lKza1iytgIXVZm3DB8kaQKMgTQpnKate5jxQeUGzORK4q2ESiO6MOZdoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=T4uxifSQcKAf7iEzyWmGCGk7lj6w_xWvmlfZc5Y81SGny1LWC_uhyXyP9xg3Yt3sVP8snF-_P0lmdjmRV2LrG_re3lScnySxoHlVJP43EeT9InWg8b6GuNleCWRGlyswF0h7RY6cURUlBd7_8pQ2FfHwRFUGkfnrO1kbdPaPiauIjBblWah64pUFPBG5rSZLgStsI3X52C4-Q00vAmHlechQrs3Z24T_In-CPaVe3mHNfDW6jkv0XYJperl5QSUOFdUSrVnO0vLnqGH0fkQrtbv_IfzqNh_-AunrN0iJ4IEJZEjGMFImfAS5ayFCiQp_yDP6o5GcU99ualNeJc_iQG192mt4jqCEqx6Ed0tVwLP9qDhCpzFlZmUHk9AOT-9siBC6Jdp-VQLtK8fLlxUtPtbHT67ZWZ23-PUDy7IFfgjQRzbKOAhBCTgHvhgL1FDz54BcP2GpZEx14a0h1AfKwiQEX9CNJcvA0GMun78gWjT2n4h_e3j-0GxwR7Te6meNdRV1BkGxmId6c9aekceAuRp8aQO8o_67gQnGJXoGkVwbP5RiV3tudmpNEKIXyLuTVFyzrqNRj4zbSLrfvVQA37m44u_SmdLiHFCSiB66WGrqR8Aiu_lKza1iytgIXVZm3DB8kaQKMgTQpnKate5jxQeUGzORK4q2ESiO6MOZdoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIF666WOdbsz4II-VYTtzOhl8qKJNXwTP44KwdYZJ2m4rM-6iE6gNjS-6hdMwv9tfms9wkxAph9mQkI4GcHdxLWt_0t6m2G_gVL3P5KJ2CLs57uvy9UHPcXJcqvw7e1XHfap6FQeo0FRDc-KySsE5u6jkW7e-U_9A9aoRNpwAL0RdkQScRqqwRa3T1v-9gKyedh_DvENCBmY5R3mBd9XMDS1hqTKfthILCRS52moh4c5DDlywO45xWQLTfnppbcZJuM_f5p7iB8ALUrMQUC44HR_CzxrCLZhB55inXLQ2FB0q5HsaJE_Bj8w9S7LTqB1Kti1Dcb4dVbY6FC4ew1uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=aDxo6AWg8SYJmZLGU_OGdXFtiycVQusAR3wA7fJ5SUyxyA9QgzsrX7OVT2OYroAxd__2sBsrz3OutZVvAN4lAsjViDYckXSJjE7PlQvT59g3CavZfASfXrhyousk4hvZgqYOlBzSR6a_agyNqvD1f6TEi7EcWxSd3LQndJ83nyL_FqPGzP7ZyRP58Wxfr7lxtANZaxTHamTbB6AciSup7GkDh28cxlNt0FnN1qLoN9UAYN2QU32g7HinZrxl6-r__A-u-GrGUFp0gLL_lPVydgJURrC3yfzdJVthWhOv8Si8KXfDQ3Im-webASuN7aw2aclxnEiWnNInnsdgK3XCZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=aDxo6AWg8SYJmZLGU_OGdXFtiycVQusAR3wA7fJ5SUyxyA9QgzsrX7OVT2OYroAxd__2sBsrz3OutZVvAN4lAsjViDYckXSJjE7PlQvT59g3CavZfASfXrhyousk4hvZgqYOlBzSR6a_agyNqvD1f6TEi7EcWxSd3LQndJ83nyL_FqPGzP7ZyRP58Wxfr7lxtANZaxTHamTbB6AciSup7GkDh28cxlNt0FnN1qLoN9UAYN2QU32g7HinZrxl6-r__A-u-GrGUFp0gLL_lPVydgJURrC3yfzdJVthWhOv8Si8KXfDQ3Im-webASuN7aw2aclxnEiWnNInnsdgK3XCZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
تیم بارسلونا دربازی چهار آبان‌ماه با رئال مادرید با این کیت جدید به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=vosaQ9OV0ocnEFHQwckHzG9Ws44jcEw6eOxf2sjcPtucoi2lHc2hoapoZ8sGNPRT3gvsg1z9tmxQEH70XzWyv0uot5gf3NIgJxlPAbm1EKrLnzMB9H90yJFWKc5TJhoKSAkNYxvJl5Aobfg_lIC6bjwsFp0JphvGw7TQ_loGjV2imEgTssxVwRwVTykARHiFzSVg2ArM1PV4oqd2x_l_Mma-eZqZMgxPZMfXlvx-QPhGFHxF0dNq2WIptNKRbE5cgyW5wQTh6BpajMMNViRfVeRtgnthi9mCxTsvrAENPrHelSXYoKYdkLMamdQHQS35BTWbO-rr_n7yn5o0LDrGIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=vosaQ9OV0ocnEFHQwckHzG9Ws44jcEw6eOxf2sjcPtucoi2lHc2hoapoZ8sGNPRT3gvsg1z9tmxQEH70XzWyv0uot5gf3NIgJxlPAbm1EKrLnzMB9H90yJFWKc5TJhoKSAkNYxvJl5Aobfg_lIC6bjwsFp0JphvGw7TQ_loGjV2imEgTssxVwRwVTykARHiFzSVg2ArM1PV4oqd2x_l_Mma-eZqZMgxPZMfXlvx-QPhGFHxF0dNq2WIptNKRbE5cgyW5wQTh6BpajMMNViRfVeRtgnthi9mCxTsvrAENPrHelSXYoKYdkLMamdQHQS35BTWbO-rr_n7yn5o0LDrGIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukJ_B01CaSBwt7R6RaF4WpI2xyOCOv8Z0vJbb5hCTWvWGj0-9YB315EwGDUwBhwwiHDwngNHoo0Lj68X47X2w6pxRXe1QDmo7Bpb59kAGFM2EwRzjuSSmR5WjNx63V3Tubbf8YvtcVY3KZpXST0k4E5BRIIRHSXFtHiH1JgwVL4sjpGWSlh1lPE1a8IsncZ0MsitScVqRNpfv_onA4Oim744rBjftn3xLb4Ogy5G6Y1_ddSbRBo_KThDaiZLO2qoxr1Zv9LWZMc_LsgVEhNHV2HZEAtqm2VV1CtUUu21u820OzR_ix0bq-irvSM3Ou_X0qUE2zDVgmGjd8GycJS9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=G1lceH3I998iimQdTmLNicbsA6Sh0frKwZkih2_WgVxaBHKb2-vJ7jfsiLnaVwhjMZfIsUaIrcHoM6u9W-E_GB1nMrSPxF3OPD-8pr78H66Y36UMZF5D0-oSfZ_rXiA30eAL3vJg0aZTpqNRpmSNIvqVJrqXtrJmTDfvfbGe4SGQJUivfkVqkDiNFZnrj1wWgeDcp-5E1vdYwvUvU7CPHLFrpLXzaG42mHE1qgwR66MMkOua3yhbALRmqSx7xrYI4oxArvhtyDWW_meOxWteCwUiXK8N8JWvr8xu6vPDvslSfwMPtmFuFjIJ2B344zn33yPQKH51HqNb-7gyGAYq6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=G1lceH3I998iimQdTmLNicbsA6Sh0frKwZkih2_WgVxaBHKb2-vJ7jfsiLnaVwhjMZfIsUaIrcHoM6u9W-E_GB1nMrSPxF3OPD-8pr78H66Y36UMZF5D0-oSfZ_rXiA30eAL3vJg0aZTpqNRpmSNIvqVJrqXtrJmTDfvfbGe4SGQJUivfkVqkDiNFZnrj1wWgeDcp-5E1vdYwvUvU7CPHLFrpLXzaG42mHE1qgwR66MMkOua3yhbALRmqSx7xrYI4oxArvhtyDWW_meOxWteCwUiXK8N8JWvr8xu6vPDvslSfwMPtmFuFjIJ2B344zn33yPQKH51HqNb-7gyGAYq6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMR7MXafpxlt4ommh7HUAWR46X4-w4kP8MHRdq8RAPkKd198KuK8gy29w3GLJDR1X5Pnbs1wK-AY9YzZBtyGxpnrHfXmFyebNHYS3dTm9SEtd3OtPFPsmqztkJj6l5OAkqAGnWY-LNILy_xnD7dAEUjeFyEzFvWgQk6lTUQ0TfpITswcuqPpqqHjmzjFnhgwwIlRNmbAbNTifzmJkIbb4P9Ya04KsVp7o6LJymAupFe9GarfO__nJUN46AF2usBmYjtbKMjxM7gL36lgbnutyVFlILCclfXbmp5-1j0KG53ppAri7CIjclUl5VFrSH4RVR-qcRmYa3okg6yl9OOJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXntRCzX5_llerWe8I_BojAodCJKRdLkRSTaKEzcwfA7LM_0RXLs7Liwin0cWRZDOwLeYWp1MM_mMw4vM5-l-_Jr4fWO3gdx2DpAgE_rEUvGPQznrEQl8sYTOq0iziTdcIgGHfoup340Ioof8gi5KpV3TitkKTFwd9hBeKuNUWYZkweF-RM8i3tQysz3YWR35DP3de9QG00pPDBFHNLeCjfxlbZZKzuGoqNC6AcfUesEm4SvjLarbPMGB9V7IJ7MfYlRrxIax_vI2nqC59VkhYZUXFkyo8asySVa4rDnJJ9hjcYwM3FWPHOVrat_2UBpE4lLt8mUfq7tKSTWswsDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwu5L_IszwIcMwcL7q68HkFtctbYuSyM6ia3IyluQ98_kTuVehJlUe09z3H4UKYfAX39wcdk7tAPlPyT7ghroiHDIVkZAwa3Bmhv2T0g0E_-SKX9e6S6GsUVIVPNFz5ABpFc8dkDCZ_6OU3zoHcMj786hc49D-riW1z_QA-JDln9seULUKafU-r7YBVxoCswsYomxFqsfWNiTG6kBG-1H7P_srLsVaG0x_tQS2eNmlZpZrCpcmpQFMb4q_qWPjSUcWEWB0c1hY2OXH_EEdDn1eQOIq2qmw3B4o4xPHxriIIWG5bjNab3F0O1WTCNT5nc-Co9PPXq1fYJ7acx169WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjMdbhSYQEWjQUmy0VvoCtrSuHypGsVJ8GJjEXv-yQvAbIFV5NfDjBKkdC4CvUHwLoRPhGuibHtEluMVRuxufUZ_nd7K-MYW9nLeUSeJ-HRuKgpZFqg8ga5rT6MqZ55Vv5bI_Y6RUdbTg3FdknBa6_huii772iL9Iq5dylG7wde_BfMmWl-LhCYaOuZyb0RD-6kGsFKmvdlBedWZ9h_2RU_r8116qCgzwIkMOcQK4X0y1J2KTxzS9uvWNsuHJ8dz-l6Ic6uJgHsEMWzJxmSzj9wnGdhJV6hx5bSzQT00cT4FesVZKlsOm4fQYaUpFAQygfw1L_CYkul7r_aaM99yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqVFtM3NniFHa5J4RseXNmyMGrZo5HFKlLOIc6V17ihBOhdAg1-su2zDR7FTWR1V4T1zcnjHtkMSW_23nhnpIcWUqUWU9V0Mg9WOcMnELfX_gbNTrCDrrYmUTP6-hlpmj9-SkpHqnMZLfPNE8bK9aqPXx2_sQvEQtCPKr21FWng1cQ7GJ6bt3oxyX9O0TFd3O32dceq5-xFn26pGyXDWS462iN1FBABU0zjN8_cn-GCjePLYWVf_RUlMuaOvhBz-TiRMktIAUY6zv4S2Fn5dCywhrnHNwm_itYML_N7lsIPUlWakPSN2gIWL7EsdPNYmx2T9cMyJw8GjZyQExo4bNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH-fL3kUYiuQSKyh1HbE2Zh8ZUGlUmiPpLn6fH3TxDbCIngRwRtSJ0JOP5HbApmhV9ePRX4c-9PCwi_20A9Z5QWKWgTmdFWdG7my7wwwfCiKnF6V9_IzFOfXxW2HavCztdxHX2xxiNKytnfnq-XUezVm6kmV9eEC0yqJs7Ud_BXBBkiDfEI5BbC5qrev6CHWqav6EU4Fln8QOKykA_P5hUZyguExTv4wGCVsoZZK42K9PrmDVto-RrJAJEpsYMoPsN7-D2mG8zkoxncq6yU7_CTAxYSK4UuVJSWG5zLet8edRcEQHqVgeg5VAh_9iJSgsVcP3jHDkRfqAOcjxVYFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kximxwa1xSeOGT5EhPtdRmGBA8AnZ5XlycBuPLj3apMswUNnmEBVAj0cxJMYIonDL3X-iG6GfxQGUAzLM7kZJUns8TjYOEkHU0djHtVhoI7n_lyLz18abFk1flfyAODGaZB4g4p7r-yaSIgFUGM_vRt37RoFaaRx7ZiytgL_h-PWgYTRyzJ-FYFWJF-Aj1AGF4lcRMIvowzPgM3A6O4nQR2e1JsvpLSXvzhUh70zu02hOv1NKcsQQjybTgELhgflErpSnKg0kDzpv_CUsBib-LodrVTjrEk-OmRWDMWScOgJVgWzZS9iHE4vib8DjQ6NKX65N662h4HakPFnE2cGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCDQ53dVRSVLigWPOWQioIONilyG8qyKOqzB0JikvX4OqovCjmzVk7DrhLEKo21yZpv45r_gzvl_cLUXxRAl8IUiPoVC2t0bxqLjXQ3g9zoepr-CHPAuG-BsAioQnYZtNeML3vmAOe7VoZGSPGRmQAwVJTY8kFaFSAVVTK4PKJEq2gGtkyJWXVise7Ftu9X713qtl2VrgM-oLhM2KsEhLljDsCxLyfwrii_q3v-DgmJj6H_C08JGVw2T8BNRJapg9_APcDQ8vStxjwcbO2OPaAhrWIw7jjVvMtamU8KE-VBG-rCD0t-1qJl6Dd-Uxgf6FPVd3pbFS4sXXdJtO1GQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plEyJ4c3D_tK9Xst36asfQ1kkjS2ydDTgo68ed8d06Pg99POE0mOko03hzNdVKC2settf9OCE64jQqtIk8SooNchm8gU1khGU-XYr7uxiMVJzKXX-1EmlyhYCz3tOPQMG5M3AVgKbGfS1Njz6dtpkIMiKuL4Nay4Hg9kkzIBpx3sjEu8Uj0cxNtlsZBI8pufB-RKaYsuisw7C6WMgnifrSKHcGumwIyXjg865W-iIpkBCxxHcemjyFLE_VNTc1Txr2LVIu7HFwzuYU7sp92D1WAcXp4eKt5wRTm5fC91OsziDLhgrvOkilcK1KnXT4WCUF4evKSgsOEfXhJ8gu93pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xuzg5Un35W2yUu9F6gQcKtq-6u2Ed6s1WjeP_Z9PkIImX9A2f5rRk8blZvgFT8jNTKGcfACuIfaNLkGw5dNYxf_w27E41Kfz7avMO9IY_dVLg3Bftjmm25ij4K686u0OCvJ-udRHM9DHNyonTbPR2KncLXETYLmNMCK9l6SYTfC8SjpnYwHIVqVKKTJ6bKpO_R54-6Ao1pDlW-0UVpOR5QNcMSuqEGt9eeE4LQzfbqtVqU2BuVRLYmYvdPLjrxPytvsMB5SvhcoXqL5SYjO8-xqctmnyqvXCUgbxloOajxZidnSjrhWT_EvsOvFVtaGvQPuFY9uwcrUVNHGVPjQ2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ0HJqAh26asGcJZtmV9ucW08X73JdSHIZIsMiOACeqjBtfQV0s6fr_sVNSQANf2Mk1vOODnrfZMLP2jxOmmEtWskNPpsJVvWozhYW3ZKfKHDnL_3bzo5Ug5518eP9jm8gF96GW41dvEuG3N43Z2tnFh3GvIM1cBSyXWq_7ffFmX70zpWs2CJpTsHDZ5yitJGCpv5En2h9m79XtnOQlDIT6SrmRrBjnLxmUDSB0fvwuL7qf7bEEF1VBdvOhReWUQFVwIEEh_vVOuExDfrc4YzciI9x7LC56AhMhvZ-bpF80T9U4udlUv28378PWCYiJCnUZ_bG_Q3LSaUDUm4SLf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u52p_3XRjDB66XHHcd3eXrPxCsAO_1p7_ZKI7xv3NvEtdSASDAqkjsC2pBB6nxZGQ9ZdNh25WO7QCwSIxbBrp5w_o01kz8FZ5LZkEuwWwkDTBwnARJRRe2qq4JChcNFDjyUWW0s2M9TqyIJ9RNrQ-OltY8ZX2dsJkqEeG1h45SaBsRGm5NYXcMnCqixUPSbeQGYfR0SlVMoUO8XvDylSamyWOq6-xd7RXhxm9R_yL6VJGeFOnTSP0vOdU3AF550NsMKW3XakkuPy3XbJ3YU8KPWdC01soY9m7hCpz01EVX-oE18tA3yYA32CX6C2dbbC57EoQNRLpzyFtH5I6zVUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=jX6v9fGnE1w9T-mO-xMpLax8dq07_tmR_8h1klGe4f0qRRiF8Y2DIroN5zvpQMqN-C0LsOVcq4nuvPcB_SK78hwReO7JM6m2MbDaGdmNzLWyD-2alQzr0cjhrKFGN_0Nn--yKXAW81BqNe_bJP2KgCNODWnTJ5A1_Q2pfeWnN-v5K-8bq1ni8yveo8dA__zERCcrFR45VYtsr4yFKATW-LbXMO7Nm-mecZ-N4TvBHnpb88HTlJ23bfMLyioZZRqtmoPRIPpO25zJqyj5jcNCZaZnX_2rNn8ckp3SpophYT2EhtNOATrDUxKj8r51pjBFrChAsg9uJ9HorLQXB5iljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=jX6v9fGnE1w9T-mO-xMpLax8dq07_tmR_8h1klGe4f0qRRiF8Y2DIroN5zvpQMqN-C0LsOVcq4nuvPcB_SK78hwReO7JM6m2MbDaGdmNzLWyD-2alQzr0cjhrKFGN_0Nn--yKXAW81BqNe_bJP2KgCNODWnTJ5A1_Q2pfeWnN-v5K-8bq1ni8yveo8dA__zERCcrFR45VYtsr4yFKATW-LbXMO7Nm-mecZ-N4TvBHnpb88HTlJ23bfMLyioZZRqtmoPRIPpO25zJqyj5jcNCZaZnX_2rNn8ckp3SpophYT2EhtNOATrDUxKj8r51pjBFrChAsg9uJ9HorLQXB5iljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=adP7pPJc-vXZiBZiGtPskDGPfCxyNWMbFnwAU42R0sEd3B7bwc6jgOiqE4buP1JzmtKd6ly31njubTohgsYKxu4NvyLHwcgds1Yg1CUtt6B5g65g2WFH2fnR2R7tBeSjC2gY2pEKDnP867t0OkO7yqaivZsq704mqUAyI4e3E1nO2cyaJZhpjt20WHlw0FWBIzZBxdVSYG2wytazvRST4Qmn-sDqoVXf4wQSRIZFzlRFy67Fy6zwTNhtAzmSPExw5BgBHF-YSGXEUI1qlcWKK16EOjTOotqt6sKJHfPbY0RZIwTkvLY7nW0ER0Y3kEbDZYj-h2qyAMeBu3H5ybyqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=adP7pPJc-vXZiBZiGtPskDGPfCxyNWMbFnwAU42R0sEd3B7bwc6jgOiqE4buP1JzmtKd6ly31njubTohgsYKxu4NvyLHwcgds1Yg1CUtt6B5g65g2WFH2fnR2R7tBeSjC2gY2pEKDnP867t0OkO7yqaivZsq704mqUAyI4e3E1nO2cyaJZhpjt20WHlw0FWBIzZBxdVSYG2wytazvRST4Qmn-sDqoVXf4wQSRIZFzlRFy67Fy6zwTNhtAzmSPExw5BgBHF-YSGXEUI1qlcWKK16EOjTOotqt6sKJHfPbY0RZIwTkvLY7nW0ER0Y3kEbDZYj-h2qyAMeBu3H5ybyqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1W6pJlD1zYMdlHA3BL78qOA08yY2Qj4oJvjkI1JzjmxkZV_ceS2qvc8e45HlU097LMMMOBOjEzZsGITbF48vLHPNrDx6E9wfcmrUcQus2K5MiAU4RDsLMmC2ejZIpEnWD3ET2Nn8oP-20rNTSsOQ7MN7UQ9qsKB4TvD_OFFo6QSA34Mm7LqXNW1UYsRu6gHR4R-ZAjcoGUtRbdeSGgalJpwQXx-e0dUUMgf4ksUOshhc0DwW8Rj0BGpP1VIY-o6JX5l0LJ7b9FTQHIjTRoDOQWy07dPaPkL2x6DAp0QWU6BF-HE_XHQnPyWshqIPaZL3eK968xPfZdRjj8EQ_PPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJUCgor5VbZ8K66NFXQ28mA09IAIss-qmDgkWwLsyAu3r2kbhsfx87hcLMHkvDsxlBc-0D9gpmmcpAc6-NjipBUEM6Skf60iJARVX1-vj0rDBmIUThFFYWApiyNcIWM4e3smB5vjHdqskxFlbvC5QNQLQ2TLtqhtmnTU5czvf170CBNIyX9lok4FAZdxbMMqdGVlR360bFUrSxQo5sNcRCzK6ROKvd46aBfeHY6IrdwyJn9e8senUPYpsdSLrMomPGIQ-QWWjp08VMEYVmRO-pxFVEZ19mAsR8-kJkBz32ilk1H6JVp_NcJLDFVxeV9qCRhXuQ6UxURAbSWVWDIOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoVDrE2BZcH5fTLEdGoGuK1NkMf5CSSYE0Dw_w67gE1WdzZVeLSMWiPWepAfSIr6CNUsiMDQf19i7cQ9_ObLEGnpO4rLK5NEq6DJS8msQAyAv7cia03V5xjEszX3nE_l2Re66vO1CRGxiTC5_GA6BStNBJGxQVR6vf7i03eceBhSTaTrlDqDXinMnCmXQZh-Y7hdpCLAP0EnnmOYjElwUc4ueWAAzu4dlI3LXNa0wm0eR0QjdWO7J8al8KvWFz_SqGd4m_P3q71RZE48-er-zY62_lHvFd8nrUTC5MYMToqBodijIsAqViacHLKbEpU9pwwJNRzCPPG8xJWADIdgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-UOZGvrhoLMm0LxYdc9PLcF0um46JqCJbklLZXFE_xX7BJ59hOU9WoFC9kkCMZqjfSNVwB57Gi4ZowdxmW5CaU8XzpTaKtHbCkr22m21EDgS9F-_b03M-wfXq0Al_hByTuXyBekpJZlJw-EqApGGWhcdnAIdRaxslqLp92u5J0Q3-yJsVDeLzBFh-V4Xtke7LTGZLMUj96qICCsmAlYKoUydpszslwqWqHk5iiTsQ-O5tFFabxT6iGoIEKXE3aBOFRLAv_jA5SDX4PLnn7cwt7GXJGAhK8rsoOFGOBpO4EnW-OZJOKx_zQJoUAn3dZgtNrjp_2vqfNzim4BBgSaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G60uWOq3VCMfmlaOs3M_GgpWcIqr7YKvt8hN4AdR_oviN_cuzR3txXsOIiEr4owiUBvLnNinWaJDTS3_PRWN74j6rEir5QuPPLXqIQQLi_zAYaSNUvu8HPMSI7yZBCCaos6RVDEqz4BtasQ4nzJQ4wB8XVH2cD1w6010KSrakwwunMyCYryk0hx2KtKIWz3ClnXasKZG_eAVColIL0i6xrayYr7Ptkf9FlVYEWBrE-NfIE_EvzXTx_FwBoONEhMAZ4oqtj1JFdYa0X54T1Na2y7zbzi9cT_Ao8ClK1Ar5VOjEr7gIq5ADhVzaBTAkHqEdVZaKYZIvhWJv7RQaPR5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W89DA1e2JC8ORGPYgBg_HRIu8trAK4W2kzPS6cvV8V1rRjBciAbxthHuZCy_G7iVjVaz9p6PyfQ_EBfvtk8xhaCykKRtF1Hz715CwLP8IJe3H7r9jUoT4ys0mC4GhPai__g5-Biz6qJGfE89pq3CUwrPrBlqC1-fJVNIOfqT1qPRAtXHlOALlBAAYP816Y7fRsor8YiRUzQpfboKfh1ElQHaxCgwqEgCrfKgfXWPYJKl3wW44hd5IIryq0IXX_7tYHCiZXPNKp_YsPX6dsyEWf0CdSMD3KaQT7g8UM2RdhMrSrnha1lbIXnZnmyRQmiG11jZlYBWeCeqGcUNfh1Ejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx9LXdV1H2SKcYt-WsvjNAOwgnaIVozCBFIZDSOHc918-g9sRfXsCnOG5eKpeXlJ8MP50OCpuoIGEy_IWXLcl_vh0NQxGLC0VR4192fLAZCKthgZPoVTTyPE6Y1oJOoRnGvs1gtE3tsNg4tEiR2w7aRGkFKQlOrFeHB2BcderLEnaWuQhUl8-XL98x-F2yOOXgfZ5aODfpTId2pCLcvoqxLHDIZ3tFIFEL1k2TL2UdggokekCH40vgkRd3JLOKN-xq-yqaYu9OwiKMLr3I4Zow88bhhOoAj_gGA6emrqZxWt8RpbiL1MRK83aE0DNCB7UTw2LxkJkWtzfL1vCu9aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ1rHbkMoBOmHlPgc_lt-JrSLNZECPCIftHu18-DyybZ0uWGb1N-g5Jv2vp18Jj6UQXP38GRK5fYV8u-lNlHkgasyw9i408yUAiIfCsdBEsdLs55DCHZibxdbHiXNgnHfImeihYth5EEaUicAHIg5vyPSbAeIrfGPa_5GNTFEt6ZFuSBDRvf-gm2pZHrgNJQ1iFPb-GhBZ9lExNYklMjsY6eLIPwfuKtimzpnfRLcTU-AayGF9l4qHMc8dCIQXNRoceWGC9A4KkOzH9bkt5NWgcvZBvtMon2PYkRR0sJ_owJYZOzhNx6UE-CGx9rI3_-odELKJohzsLDqvfbYBfZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OemgJYU3j0XvuRE6JrISGeYLvj99pf8sOMMWJh7VFxxdw9Lf6dqQhL-1PtWv6LPqYdrvdDTOoiY1xCIf60V44PaTioIrLPCpD3KVQuUOvYBuwOUFofqjixsXX00w2nqGr0_BhPGNOu6OLoe5hqnvv2pfMclt3I19lj9InBP8fRM43v68SYEmvH7lKsOJCXm6596BeljD5sF9N5_98mYopXsEy4Bri5LoZpo7VQejrpPshZWqx9JydWOzPnArqg3URX_YXDzxt28l6NX1FVDoYOxstDPsfDb_x4ldALc-AhTHtV0UUvtIHl51WsWKoagLVEsh7fRyfvG1ovWOcp7wSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjtkxRyTDIeQDnRCZIfTjN7jpOOHlqdrBcdUz5aMStYl0dJ10ME-Kt7_80uEvzwRS6XPS5i7sxvBgp0U1HoVA_zAx0zAwOmgnA90F9M5cEcbDTRWvFUMtGRqvhnoESS_jUjeiefD5U1u9spkc7W-KYZDDCeITjhc92S3bNUXbrqwkYk2QhSS4PQqZ_uWg3jXzyqPl2A77G4-3yMTKHrUxYhQjB-xk7G0ffs5-vCwCJkki9b27hbfPMjfMe3BWoZSpvb1jXp8h6Xr_QRkrYlZTMZHO6Y9E-1U4XwmQrrQ8DBv-ACv-j-gSQJMn-qRrBUHC8EEZSe-3Oeyu0oKIJjruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUjuyaV4yXw6UFmpuUkZtGOEUB3prV_gqndkMXM5U3Pe-GzNC1eLJIrBWb9gbeWO7Oshvn5bLQBmldPDR5nB3csXniBvQhJkjq0jyhHQlwC9L1xcWnb9Hma0UR0yp18sOS67oOPqBhLJ3Fikeurx5FyuvM49cDN91dICgZ9fabcpv3wjFEg7BzAqvxRdcstV_ugzSUFo4NVP-jLKjF6rJak6mtaVj8tsV02qbziNTiD-1bMeqXv4zpLK_Viqk9BJeU-5nDKSgs9Bvs3kME-ZZbGeo207EsX1QtQnfGjNfdtOh6SrRI_GOAxIDcHEMaNzAUEp5-kDMVIKfMwUTKmEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwvOzMokkoLYNAotFP2S7_AZBkYVoZs1bDiDefzSnC9FwEiEt71aCSvEbrt0fmYM9RY8veF5kbm3NJkj8CqDKOYVPlHteuoDhrMzi2VVNWYIo92QLQ71dRd_7nQBoAyrZMIwg_RfIVB5pvmcyJTMhb5zN7shGS1XUR-cdf18pRABzmrc2RJd2AHdD2ynDwSqcghpsxvSlPHc810-hwm8IaqrIZN4ML8kubFtX3UqaseiIgkGlObpR0agkOUcgwSnnUgtW6VbrV-NH9du5twx53PqLkY481C0cjG1FU3lgLlhOEW-D0FJaFjxWMI5aU6pZVo60TL0jrmlvB_mlY1MIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf4m-Ou536GVcn3vg4mUYr0edSLq6-hH4O29q_15G9y9ik0yQvK1It78cRn1aB64OL7aG-2iw2WIxb2d7G69WoJcZ86DMCMn-cSFs-0xFtDcF54Ykk58FIAg_cj_u2bdOhxLiL8ydT4T9SyrXqmehd0ZSGsVNeGKlh8pipQmiWq6QPn3SchiUtOCL_DckRwl0eGUDIhVT6BQvFCm0Y1MbU4bjiqnmw00x-6FAphnm2Rfg0L2794exgmBMSk9zww_nbp0Exr9zWjlmRGswklPQQmPSEzCO24gowGn0NTvVKRjwcVpft6z71LDHC3u7czzQRGKlWMvvRW-pmX_0nLpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olteHfHhY6FAGPyNwYPVpjyNozzi1-b3pQhxs0CNhfKf95ngvEx7XDfWulWNJz9GPEYUDRZN9ogw-xZkhNCXIYVWOY2ckts0SlonmYlBoKa85ajFlEgbrspQ4bI6MYPpdLXxqTA2aSFnNoAjTRFhXaF1tAmOkdKyWesraXweIV5dhEDE-HwKgaROIDUYHtL2mCpmrlvzz2ehGJta0PVpuzePRfxBOe37fV_PZl1yVwYRM48NwuMlt75eBl1EqX6RQ8pcMj-QZrIADsPvWpL1k8If4tzRV5-atp_Ap-1Y73_Ie5h25ygNiGnXsUPOTplelVnJou-Sdz7afHBrr7nLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0F2hCZWzazsyCu-F5KGXkjlmCkR6NOvd9fO8f-rQqTBLWqjYBnroHbqDbteYu0b_2gtmu7UIXHzW502-UBj9PhDehMa542M8rbaZNLbMa4_HLtZPheOCe6FWkeyYV6WdBY4CX71KRATXkths2jXAIMnMo_zj2FdToctS3FGQWaChQwBU_tuTKDysjcPsw-1WEbzwayt3xycCZG0_YWto0NQ_FVFw_vwg-1kEqvapi9KfDVb37lnqVDxOO5zPABggnZACAyq8Jhh7iBvCSZroWWGBBxJ6z5W7cgGo9DgqOVYx5k4lJbD7KgN6GIJQs8GZ7dUPH36eaBw-TnsZPHXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kmv5EJ0QzTGJarhrvJ54TkcchW0N0nBkk2HIxoi53ulU_gvjaBe1GEZz9cR3AUW4F0I8nqa5-gq0GBLvMwCk7xELL9fr0KDTyOL5PDmnOjT6JKgOPoSk8d7jSH9JpgBWPEbpEYwneltLE7A1lXmN_Fw-Q4BD3TyHk-7Y8nbDWdJHwnZbxzeFSryS-q6mGVv8l3h34oAL5SOtko6h3xaiM9wxx5qnZGb4IGOOafiN6o-CXEbN-hy8xjbCtbcQbjAzvtomUBbq6KnL1b1Bm4HrcJDToeL00lXn0RlUY3fi3LMpOFn-AAZuIt3kv7p7-US-udZ8xChd-X9hEhS4JzS6RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy2-tY8LzaIU7AwiORYqmPh8Wy0bYwdD_6GWhDMgT-8m1oa-QhyvFHTf5ZBrl7DQZ_SnQJk19pySOE-DINIHtxkTZ-EqoDjxoMEoTxmCiMxDavflu-1STKMCsCvsWnMVKncWx9Bm4lGpJ-6q6Ufgit7hikbvP58WSS444LI-VF0wMQzIOYws6b0dZP3QdFBqfMOAES8ip4Hcr-oS1SHp-In2pznaRviNgi-Nbt8rlWExlFN3CtcR45fIyjB5tRO_0zYOysz6Z70kGQXLQUPpgDF2wtw7yF_Ek3FE7PEdnt8L7_fLJzxD9TWsUjEMRZTkNFB6qJcK3hrnA7fCYhWygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqFDAKniYAtGC5HhYFlo8SqWZFsdT8PvEpjD2w9sEf82o0hcc9zGXtFuZIASHO-69PRyvISzz9iyfwpkKqPboKkfTnADCZq-pTCzzW8oXZgQq69I5k1Gy2mZZX_c7781u0vlSXLzU5EzxWT79XEnd7CNxtfIXd2trElQXCB49TGphWw3eDFyh-uSLdC8MvHvRdAGOh17Kl0THrQ-veIwEqFE6aeNMaRJ5lZRIL3qfmFJ7wzDZ3yhdyS1S_TCl8eRevoUfTiAVEfolNW1FLljPyXQdBw2Ogy-WExtUmivEcleWDtTIiqJMDyfTMflU5_iNoPyxhbvyNFAbGtmSHItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1XMSzXkzJTqAhzWeMJlLB_oKM9aPdJof4jvLoxZJeNhpJ2F1f859NN0T_VTpM9FNaPSlfuT_Z5ywh887CYvL_hNk98m3WJwTwJvftVSO1gmUYIu2Ujj38buJVBWu9uT9vhgGR9WlXQkThgYXZ3wIiQtd4EZtEiyaSV4KnluBQ7Jj3uW2JSxaURNy5CZ3d1S5idpW2KNR48u-nyl1DUjqE9q7DzUiMEUl7TiWytfcbbZPvM_LdXZovHXqVTMGAPdgVSg61pWO_JHk7h1yQQw6ccWyjmUEKmBGhiB58i6swoz4H_IlNeFhKLLEhJyBM_BK2_7DPhE2vPv7Orypf5KYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAXA9ot-zBHuWgXCfsF8qNPe7-kjf319pRVSqO1N_d2l3rl6xG1-YxQa2t8tnFT_uURJY2MnZb9NaXI9f7ZiQ12RIKW1u2pzi-86otFqHtu-k8y9gwWlKVPKf7HjAwlkDN0G5ITrW-poq3klY9DJ8apZXbJ9syALtZ1-7qwLBww9w-fSi04VZjuXnkDJSL0uA-BM-Zn1oR8xco_G1RpDNNwzjmuyd5waTPLE8qkntO2ZQCm2lF_jhPEd3yN1KcK5Op6reXKUTGHE7_GQtXtdjlL_ntyQN6QIgOWrdK0KtEkvSAP0V2tgj6F5NM7IMF-HflZbniePxNpAxtZWrpvo7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGKh0u8PQD6egENk4XU5qAysJjFu34llfYl56CSl6h_GlAPXTSIzvfcxSEAdAPAOKv6-SWcfUITMPGz1_JcO66NkeXQ1kUFG5zUjJNi_6kvePlZm88mb0trkV6XWo50uKSVUkIqaT9Ar9bq-MXh5p8YVVELrjpuGM8ksG5uSmfgJzSGCZH92e2E8WDsEHogcJ0s8XA8B3cBJ5XAQm8_Sq9mqRD2hJWFAE95adnJekAYp7CfGmMB8NWL9yVsxlH7fuN-45dS5RGFuDBKIprk3zynzOQXc-3q4zslykWSLYsu9TbUN3G0smcohTrSDl4SXXK8J4rw-znE2t8mCdjTu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkYmOsvFB9N8qE68B-MQ6S4a4Zy0GIaXEIdR9NNsKCvy9vxEBqWnm_R7vAxahDgZOsej8eJWQ__GTYU_E6D5iTzrUN_HPdpeL8x6VCqUmJqS4mD4mGueI1yt5NrgRZVDvH2mNNdOpaNsNQNEAn40IlWnunJHxlp_qWIsPzaCiJ-3BZRitEoEF7--9opzCHHWY6JuNUR0US50fvTNPQ3UyDui_GuREgsa59YHV_suRx0s6Ns982joWPRHplQIsvh5UbEUDiHzoz8iG6TRBj8UHi__uoy9KJ9A-3b-LuxlF23lbA4h3mjaWWYlfrOcAM3w3WedYa_NthTg7qSbd2OT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUJcgR032Qr3jnFDKMiPY7ytUDKKd9A0_mv_MUV8glBqsjG7ZW7PJ2v0-Ookio4t_bS_t1dHw4kHF6jE-0T3wH-shCuW6zt5Izu9xINrm36Z56GgX-vkIj6bwPjWtOlIlwU0w2_B5lz9I4NY0teyvZSkr3JPp_3gruMKrDd-f2-de4L-kzpuy38dNiUOhFbiqvOKT162dOJCxe2GmiCAXQDoB_D1DWhn27qgv7myl7_6QW59DVNuu7X5C7qeM9SjQda3ZdWPAeiSlp7yK95CnyS6rC1OMmv5M3XZ_piZcKa6h__1zn612iMil_rCkSKj82zu9JVA8_rfNa_4XVyrCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oz3jTW1G0_xvif4rDQTe2ZP9zlnl1r9nxAipSAT_N86piwDshYj5m5B6P09dRCd9gN9airevrP6H0L4vswKyROihmyY_9lXBJOPb1g1NbC5Roc4J5gFVtfjrUhvvK4Hj_LHbd_-NcJnAPivjo3yJgnW8qvB6jdEvI-HkONENQMJT8oGaH1ZWcKvfCQSSS2BdSOUmUhpvBlKGgsUn2uo0t0etjliofxcuXElNJSu3v3he22S_hoZ_hHKoG-ofhzmFlat0IttEl_Kre0qvw1Kc6dBfCBHzVam5kSCt6HfgHLNnC-cw9nzyXOw8nBmRKzYWHgdPYVFKX_GPq0tYDnw0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpEUP328Wz2npLk7Q9qF01NaJ9g0S0OllZpiBaoySTgJ6IJU1f08QMDvFZuIsbO3UpBvP04W_G-JoFayprKkyjyvSaQrs-qpOGgdC0EJly9G0FH95GD6H9QDmlGzo6DBjOrodhLXPUNawfqi-u7abQrbnb5z-rZmp2J6Ob8GqT4x3m2NXnLMmi5mf7mpm2XKvlyTckl-0aMX-7J7TbyL_0MPOQm44PjxcCbO1JN8XBehp4RxC5xp-QznNbb9h0tfT1HaLUmL0LOGBEBBTw4QdCYAAh8nToWMW2grx_5M3czO4Y6f5tjLXiaMhv_gV7FqrOFQs829H7RaSHASxOAZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvxxUs7wQAoqVJCvAU0qArKmESRwNl4cTvpBb-tLV5aC-3_OdYuKuMQuve-lsnK6Y08ViOlNiFIAFcYS4k5mFaymbs_jJ26bfezXs3epzoCFhMqORSZI1BXNZdilCaO351KZ4o98J2XFVE5T95kuyiLqKyBmgfiUFuyY9g1K-zmjBp77oxQbc-M2p-tOBI3FkCXpJh4goJOm94rysuMQbrFww5MrluIi8NwrXMPrQspNbscE618nbOdbf1Bi-y5Sjif4ly_sVTcMXQSz1UHLRL-wPGncLDMvTlcE1yVVX45qlFdr-vAQWuE8ryIBWrwCnWP9hhUPNj1hFsvLH4QNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJPOLzFlUnruPQduQIqNwu4G10KQbOZOBcbdkKAvHLa8IazvOJMdr3Xog_I123xKMD-0ueINYq7l4l7Z1YslLxGyuUr6OydHCuSwiGhJ_9EwcHG_LPf-5sJuAemJGc89nP21Gt-QRWpQ_UaiC-xGEToMERMtWeg6ZimHOZWxbFpyteujiyn0qsuitWEKku-g2FtQC_q_d5O7NHSba0_hDdOR_KTDrGOqhEErZjqW2A63QKyGXiw1IgCdfEOWqyBxajzIKhWMFQs5Y7WJIA9Gs3ksxxuADn0saD5b6eEk2P53-UGNYzbMfCadz9eRuD7CdQFZRsx7_3DNcI8pACyupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0aP3XkZcIFqSnWa4RnpbdRS01mW_ZU_AA8yHxKXrIcGViDHzTb7W4GQnP3ugUz07JloqIazbLCkWQhiRAAp4QiOsiCGvadQq_LG8bAffuL6jEs7DO6RdFgPyZA8ukYXXdy7x3c1gZBBSLGWIPpfj9_bc18m84rbzkj7sb8Bu_wyjMKcoxRQo7Dl6p_rf03C3NanA5lo9b46D6-gspi-QwY48PFi-k3Ab7Rv5cM1-5iUxQTxMwO1B87gaEWz8DYNSxDWJ4LzNvF2h_fUm59dzWIeGs4_W7B0fnhiizSnZcyw91rta1bCao7IK9JhXwXBEr6dDQLMhFJoOVZK0ZKiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0k-TGidLsfdcWGal_2I6jqBZAr2MqYsD3QwTPt0G4s0P959DAYd1_BcDvzP4Kwq5p9xmRbHVj1ndgj2AtHE917Uj67jBqk4LCJ0tR7ui75Wi5A62xoBd4tiWUvijRQFRSyMfVFboyuvogMYGdSo9qxqilXH5A8SlNxQdyjpfNCehjknNI_oAsG9IJVX7YbVrhcnnO5xGFnCoBgQQszcNTFCdhmYDxk2saCteKQl3GA3Sjtpn5T1H3u4LKP2-qAEXHmRVxBSq1GxscjdHRQoo8XH4gYfP4Vl1Au8klceagsjeF0Q2zynjV_g1QIwIHEqdz3XgFs57a6W4hNrza1iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4FzlqZMoCYHN5zlMATrZwh_Ez3zoz1igOddFXgTEvV14Auyr32V7VBQMGmtSmoEUfZu178lfEaDRA-0mHDASVU-OQKtBu-n_HavXCvcemOvvf8NGzFX_oOk77lV0NFQDPwD7wPy1lqEgHEqIR6NS-SVVTWqODXGqzUMF7Hrs-v9qp1LaMtebMZ_Q2rENYUfj8nNW3AVHP5QwpzGJoZF7-erzXoGylEAyGS1wRHMeQUuHfuyMAzSIXwSxOTO1HqLN_-LhSNigHDFHswnRMlOdP0BWVjBy8VJXgYXPI3HruX7r39CULjXIBZFyayFOIRSTImhfKRZK1y2ARBGLRyelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMtFOa6bgoS7kp8xrlCF6U9N4dC3wjGXK1zR_I3nfIc8c0jw3Jhy7NG4FdLm_0g2BaGhWNDGp0CtCCqFpdim_7O0JtY-XrvvnKlHTgd1MtBHYY2MrtxF-u7A4MQrLqDhmrVmYIgdtLu6F1pDaW5e7vR8DDPh9eBe6vhqJefhpDtySVSMiJ0V_FcRJCdX5402u85NXQLOEy8x9PvzzSN5bCryDOvjL0P0-KTXHxIoDlce98pg9193NJdp3fli0tpSPMYXgTf-swHPmJybWdqR7hoWZsSe3PbzWPI9I9lATXvwbZbSPe_jOIT_Nva7VCtH-G-I9-KURzHDSRUToOMq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY-khBlZUhuufMxxnbXVDkQVMTBHqP6QrvtsH9ocYPInlxB9l-5c2SUeQPIaTCxtRLGz7zc4kncHsbRwzN_FPOZQemA67AXjuYvLUXfsMmzp_tedoDJP8Gp_CWbTIqFOwqvPTBpbrZQ9mxoLRip_1YmAo6rvb0uPlZGbbRMVDvVUSeIoWP5wrHd5UsmpdkNOEmUoKxT2bFGHxncJGFCvaBRWScYIcsCStFfMuXFbRjVNWsRc-FSAPlxNr4Upugqu5Y6fgbI5YNI887Yzv8BPH7HfZKnhHGL9voIpEUGkVteG1r0QFVXVYBkVB_rog6CjduV6Ps8FId37HXG9RZNDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=Wiwu5c3yYSuCnw-fh4skh7DLA1oohG-VEotEfLwVyg3tNy0BqBaZYoK4gq0eU8pZf8jFo5BKYAhjQ8QMXEOIkYIMisFqDOWhdHPsMF2KTP5M7uXtYDj_uJTq_H4gAIxF9JBo7voxOgSpdLK8roTdwgqwmHrVtlNOmP4AoTyJpkyDrlgQ0v-o0lx2aoKali3xcLbulinnDogi4klaZ50aSWFZvk7E-el0h0y43u67su83d6oBleEv1bBuGYjV8PDba3zTWU-IQVUHyiI1thjMzd0a3qY1DDANx4Ojkzg0aGjC2pULrJhXIVMyFTcCDsGmbjwOPi1Zk4zdNLHro-loO4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=Wiwu5c3yYSuCnw-fh4skh7DLA1oohG-VEotEfLwVyg3tNy0BqBaZYoK4gq0eU8pZf8jFo5BKYAhjQ8QMXEOIkYIMisFqDOWhdHPsMF2KTP5M7uXtYDj_uJTq_H4gAIxF9JBo7voxOgSpdLK8roTdwgqwmHrVtlNOmP4AoTyJpkyDrlgQ0v-o0lx2aoKali3xcLbulinnDogi4klaZ50aSWFZvk7E-el0h0y43u67su83d6oBleEv1bBuGYjV8PDba3zTWU-IQVUHyiI1thjMzd0a3qY1DDANx4Ojkzg0aGjC2pULrJhXIVMyFTcCDsGmbjwOPi1Zk4zdNLHro-loO4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dviznLvexbngBz7DkdOWI5ANKWxV8SVsnKxiacn_JrWL1xGzf7m9-JJ7YOaTM846A1vWIxElNGJiVHQySAZboz5FKIBE9dYYjJN4r6s7mUHDejH8lkhLjfDiawUwZOBcIeaTH0CVy9K4peJILTM_tdKRQ7D0hblyZutlAGKXXrpBXhjSXGeOHYbAuOwMNoI96GWA1JUgS8_AQZJkznZXnk8ZnV1dz3KxGqc9GDJ5sHzc0laaJ-mR1ZNuoSCB0sEEdQrNAKGGIWUZYx7WllrsWefIsZYC5Ryrzhk-15B1nQoOFQVdZOOJEeas2ucy6eUZthwmLAN-bRcWr4qVMPtVFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=NWyJ-Q7VmIxJtvyoJhNRD9qPLctKskFF1MzFhgTOXqnGbrWgn-8KqVNutKfFJJsbagofq7Oo8AUrcvtPaOxxVpbLQV0Li3ZUrHSsefKklkB4lC_8TLZeXOwljctpdWgupC9HC6tVEBeQ2lSU5VO7o1F-NLhIxxFIUIMuqkd1i66iALT7IMDpvMiIhXUTm0IZlHj_gNmnd25UaIUUS9GB3VFyYux3JjZiUOPDBGFZScdzlcWctVyIK2SVeRZG7qRD5Q0-QQuK0ckIHvx9LXoe6GY-kBySatEcECwpXeJ3D6T3xDUB-AAdM8jCx6kt0_zaIOEQ0ldihtTCEcSUCfXFqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=NWyJ-Q7VmIxJtvyoJhNRD9qPLctKskFF1MzFhgTOXqnGbrWgn-8KqVNutKfFJJsbagofq7Oo8AUrcvtPaOxxVpbLQV0Li3ZUrHSsefKklkB4lC_8TLZeXOwljctpdWgupC9HC6tVEBeQ2lSU5VO7o1F-NLhIxxFIUIMuqkd1i66iALT7IMDpvMiIhXUTm0IZlHj_gNmnd25UaIUUS9GB3VFyYux3JjZiUOPDBGFZScdzlcWctVyIK2SVeRZG7qRD5Q0-QQuK0ckIHvx9LXoe6GY-kBySatEcECwpXeJ3D6T3xDUB-AAdM8jCx6kt0_zaIOEQ0ldihtTCEcSUCfXFqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0xVc1STssav7FT8kOEn3ce9oqy0PZC8zNKWnthG7z3L03iDm6r619935hiAjjaKXjfbEafSTMhUQgnSXp-xD7nifM8rBWl5Hd-tdXENxSes2Y57czs2gX-FGq22TR714K3OQJlhjU3BuEXtE_0zxONE_UBxMZJbmLVLZep8u9KXkDW4frJlmtw7pjIt7o83TH4fzvOtBstewox-pE3-tEh_adYcEJf7ND_OYjHWDT8tUWiJASz5vH2kHdVRB_Z5tTCXTwGEEC5t8ZPAlaPOyP5e-fE1t74N_wu2yaoPjG3ltGvNAgfYirJIIZ7sRfVSYzlk1Q81q95-0Gn9V3qpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrW232pOqYvSaloKOD1wsA5N3eK30e8WibmGkDlkW1UoRrXykHTHOeNVgsy6cvhdCSZo-K3jg-Wfik5R5VZhK8-MaU2nkMEUiSzWT256m-KgmnMeIyEpxOiYEgtVd1cfTOpx4-aGURhNA3Exp0xd1MgrwOS61PWmifTMU_G45lrCJF7aOPuqFgSnfDWb8qRHZq1ypBF9yPaDRrpGpRh_8FVR5lraSXF_62AJW8jdzUenI-3t3eIUXoPZtjH_UJ3-R2d-mXCq0ZtZ2asdyxSk60J1TXjzLHYhEnPP8JhhNTPoZrRb9ZJaxum7GXv-jFiQt45Gy8I5dmshXz3lOSGfQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=FtzHb4ATDxU5gN4Ev3CpjMVWU9MFufRBnxDc-YBR3WHOiD1hZ5DeZroTwC-uAxK4NSXRzq1V3CRr_q_NRGlxso6UCS6lx2s6YMefR1vzlF-APiZ-uzhguiP8Opu2hekb4TNRIJQfP0PVk4TIuxJ2w_zJJiD1TO_MUaLnt4tzMuNVYp2v62vyKniqbc24pbdUyZSu_39fdGmx8BrLecKoq-ZGjsqEucy_KTPvUOb58qEu7DtIaUZlRsJ3zybZoW-QKNnuLfhZIZ-eExH6xP18S1BO9MMwhK7x6NCwa-nlON2ug4dTwZ7YqY6nG8mnw6lLmZxTohvyw9u3Z34NLBdGWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=FtzHb4ATDxU5gN4Ev3CpjMVWU9MFufRBnxDc-YBR3WHOiD1hZ5DeZroTwC-uAxK4NSXRzq1V3CRr_q_NRGlxso6UCS6lx2s6YMefR1vzlF-APiZ-uzhguiP8Opu2hekb4TNRIJQfP0PVk4TIuxJ2w_zJJiD1TO_MUaLnt4tzMuNVYp2v62vyKniqbc24pbdUyZSu_39fdGmx8BrLecKoq-ZGjsqEucy_KTPvUOb58qEu7DtIaUZlRsJ3zybZoW-QKNnuLfhZIZ-eExH6xP18S1BO9MMwhK7x6NCwa-nlON2ug4dTwZ7YqY6nG8mnw6lLmZxTohvyw9u3Z34NLBdGWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilLV4XYBTGtWnqaAay1cCRU55LpNTYMExF6y9s-NNVf-3gOfwyWTBo4VfP_z4t1Vu9UI8VLpf-wtesz62l3aUCHF_nXmtysT5pH_uKKZE3l24NtGKDNk_oeMXSZkXr3RAehcZ0vZWBv7FJR9U36C-8fTSANmX2xwfE8sBz-8T4Nae4bbb0WiDTDvBr9S3BiRU01fmejJ4EShGiG_Y1cKl9S_Qkx6cAyAqhEKa1-t3JnCplyrXx7sM7EF10mHKJjU5y0JZ8hHrax6Ys47ajaNJsiYmPDX_Yz63_BnXtNPtZB8Ml5kLCMlwKDNT5l8SP0ljv4OABFlg0RhTsIXlix2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ng7uN-zAnfB9vMyZFiM6E3WVCZfAyn1EcLT_Tadd1aG5M6SJKVnlgMoxbDmc7FuwGcuRMcE7qr-gMeSWrSpogpquhgpE-69SCrs7DfQzZGdP5UCz86iATDDGjWHv2JiFSgdAEMJtRjuo8VhdYwaJoY2FrdvoICJ2MZbgovBf0R0If31PRbHMfkeSlrl4xBcj4Pg8R0Tda1tAkRy55P5jTmFNTryQ6T6_qjoOpiV834c-2IdsjQqew8tO7WXhdhXwGcCnamOJA69QZY-JuvxwLIOV9xTMJX8Tt-jQKwgrQKuuJqI-i3xlu_V5tvXZPbFiKFODA8yflYs9qSJHCHjCig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWT244AVI2WCymktmZsNcQNbDwW0K5bFpcxlNhhCrL5EM5qR57Gpsl77fNZomjLnt7wY_1iHg9KARQwgxG92Pjdn2n875McEHpZ4H2ugNrNI16EdTpGD_wuUOMquMJ79jibjul7d2BbZVv4_QmWJyVBv3-fp0s2d5AdBDsM0P8-UW3VZkVlX7fB-C9kJDsetXfl1pGXtRM8uTkg9HTCvLGgu1CuqiT-KTBcyxY1-a5XXX8jYhEdz4VK5PI2_xv10i6a5oGk5P0PQ38p3HilCHF4uz6nj8w4tQOylh6S1jQsdW4Ufb7xawlxLf_uf_eH1Fm3ArPkuCgrydBAtZqSLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=Pwy_TfIPT5Fa8Du_FEdGsivFGCjkauv_iI-DQkistzSY_LjdPgr5xJkEg0mvtRqJTTI5YgtB0YxnGct6hjBfnj5u2g7w38_OJKJnEQMkns7D0XIyB5KIXbJNzcd4o1BqcoMqa7N5xdwDPzETSMnjb8T7zF6LigAbRucB77yYTjlae71Crn6-fQgq13T4WSDR95vaaK2zORhGU-EldOpB-7OEf5D1HAeo0VnRRoCCnYNGIh_q67Nh6lTRfZZnlO9vbtCSpRkdrxX8-LiJIlaZErYVpRe2uMeMsKBt9LSm3iA8Y-gHOD-XMm2f-F1PRKvFl3aXsLf4dP9O7W9AOaD_3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=Pwy_TfIPT5Fa8Du_FEdGsivFGCjkauv_iI-DQkistzSY_LjdPgr5xJkEg0mvtRqJTTI5YgtB0YxnGct6hjBfnj5u2g7w38_OJKJnEQMkns7D0XIyB5KIXbJNzcd4o1BqcoMqa7N5xdwDPzETSMnjb8T7zF6LigAbRucB77yYTjlae71Crn6-fQgq13T4WSDR95vaaK2zORhGU-EldOpB-7OEf5D1HAeo0VnRRoCCnYNGIh_q67Nh6lTRfZZnlO9vbtCSpRkdrxX8-LiJIlaZErYVpRe2uMeMsKBt9LSm3iA8Y-gHOD-XMm2f-F1PRKvFl3aXsLf4dP9O7W9AOaD_3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=viIriKOaw8BcRi3m93Iy9jRR33l5RrcF5lHMHjjL6PpzRFp2wZ1s2m7QFq2tRTJxU80L269834ZMtQw1MWwTCiE0XtqwMwUMAGbybRI8d93gdPDgZ7T1bP0I8satdOcNsy_LRuI3caYIAfmgpVasQjk9kn6MAx4EcIqKqxzyL5IXEZvj4SlN75F52z2vjNhxSeWt8OmKBt8gPAiPdGRSr7xb2PbVrPf45p6hY0A0cRZZ2IL4RzyJC1CeIn_xvSsnwABM7viQF-oSPRYWJv3PK65QEpO5Qy0H4qir3v7ADhzu5tYOXiclCkvExnBCmQc2HqNlb2Q4l7AhKzjfoYYe0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=viIriKOaw8BcRi3m93Iy9jRR33l5RrcF5lHMHjjL6PpzRFp2wZ1s2m7QFq2tRTJxU80L269834ZMtQw1MWwTCiE0XtqwMwUMAGbybRI8d93gdPDgZ7T1bP0I8satdOcNsy_LRuI3caYIAfmgpVasQjk9kn6MAx4EcIqKqxzyL5IXEZvj4SlN75F52z2vjNhxSeWt8OmKBt8gPAiPdGRSr7xb2PbVrPf45p6hY0A0cRZZ2IL4RzyJC1CeIn_xvSsnwABM7viQF-oSPRYWJv3PK65QEpO5Qy0H4qir3v7ADhzu5tYOXiclCkvExnBCmQc2HqNlb2Q4l7AhKzjfoYYe0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFSGx1jw3hH5neG67drXJSkmNZxRH3VuWs-gpKVVP-wq_5XrnY1z4t5qWMu8FuTaQhNN9YEQLK61-ELHKDgdqj1nGfIp3EEbV-xA22cfkqRBPX0soOQDwYVpg0VdT7IlseFOi_BVzngtnkLCFmM5hegZ5tNNsziYHmKcpW4VeLi-aO5ALBX0fwCZunlZGVwmPvwBoZdQLhrul-CLBdG4G-c0MLj6Hw_isCYvYO9Di288GmjNx3a9JE9iH_ecSx1muHZXWqH07TTEAm1B3MX9FATtbpxl9xPkXS9BCUEMYRDfQPJo5-2Dba-HB2bN4DsDQC190z4lQ8_d4bL46Luzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=eLFS9cY_8ey-4c149bz_zInFm3HvvHKJjUjAkaA3I5y67ndROkU1IlWX1i4XFxCwK9eVfhMdsuIWMOY_AonTqZp9m8vcQ9niBzrgGLlOi-6oexKmyWnllZDp2Eoru8oEB4SUt8BW19UoSSyOk6Alg6-IPjXrnDt5Y3EY7zK04kOJeuQbFdl3QKnAeuWM10MLOUuHWMcewJYn6uM0ToyYDAIdlnNa4g0pso2UBvZp0wpcekQMvyyIaZ3PLRjl1LW0-cLNJQHtKmW7sMa-Ar5_TLSJqkIKAgzYUkPguncCvLpkQ0Igrf-2sgIxW3OaeP1nLVITGFowjyTsRoy7URU8zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=eLFS9cY_8ey-4c149bz_zInFm3HvvHKJjUjAkaA3I5y67ndROkU1IlWX1i4XFxCwK9eVfhMdsuIWMOY_AonTqZp9m8vcQ9niBzrgGLlOi-6oexKmyWnllZDp2Eoru8oEB4SUt8BW19UoSSyOk6Alg6-IPjXrnDt5Y3EY7zK04kOJeuQbFdl3QKnAeuWM10MLOUuHWMcewJYn6uM0ToyYDAIdlnNa4g0pso2UBvZp0wpcekQMvyyIaZ3PLRjl1LW0-cLNJQHtKmW7sMa-Ar5_TLSJqkIKAgzYUkPguncCvLpkQ0Igrf-2sgIxW3OaeP1nLVITGFowjyTsRoy7URU8zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FasFpDYq-Fsw-JW1jZr98eL7FSTNz0IrWg9AAa9jNDhRzA6ygFzSsXBeGpThACbNmpUjpghxD2gK0OVoPd2sI6RMH6kqfr-_RU1owaoCmrhX-QljuRavYyhLEBrQhW6LIirwYXLm0ehvmJH1Qs5WJirMTMdnCwxO_dZYgcdTRV2tFP3GFHrGQ5bkFI6Q5lRLNpfhgNrEhMy7xfV-FzzROktStmEryxjoUzWWa0jopbK7KQ7GCl3xTXyCfuKSOs2u_qGDcpbZVlKwTcnfuQczAUQY7RDvKxpX4zBcHb04OhLJMv954_npzxu6pp7oOMGNkhlVJHtdrLakpSNgW0pS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9qeEe4vwj3-9gvrw-DPIFw1spFU-zU9VDX5xq5odaza9xlkOLCcHR_nqiQFDEttE4V-7gBv-JF3nsIgtUo8uWA79l1yBGCXB84Cma9OB37Oo9BdgRe5f_60NSE7ZoLbbazfdXsFRm2tYz4XsWPG0GUvpHVqwOxxwgeprrhMtPfLK8F_qGjlwvhazsGzDTv2LpwnNe-yM4f72vHQ525zavCjZq17GObVlDNZC9TBjIFYXg9L0gHB1jPjxTWNWUXUV_wAY9XfjPfU_GYsSysFwYsYjY_1KTuieMvym_HZEjYv7GutvEOssclB3STbawDQLNMvfXuEYne8V8UfQKVL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRZWPV-ENlZkqITda81UAcQVPQJJxUDrSuW6j857o0q3rTVdpP2mu1bcufx03x6scspavGAI-caVFOq4KuVmeOws-LphymsashXe6YWVeuG79iMrhfdu82T3-QAWqEIKBRN9eb5OsmYdGnhXQIxwQ__HbwgEggbPo5Z4DZy5SdYPnBNku4yUe3Zjse6wNvaor2zYJ_IRWWrZO4WB3vwFl5eYdMTmAwcAP1LBse2txLdmjHynsLO9mChpc9aEvsoXw2ID-SyQxjYIwtuhYykdf8rlsC2RdekSP55BiWx-VaWwicNxLoQOIauSCClR_oSdo8G2_6RBiDIRDjcJuOix3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjL9dkFNnjMtwXk1GfE7TuYzrMo-ZtxUugfAJXJ9bgFiu2peo3fcMy3gTwdnHwFRkvMjkCjbdvfoa8ZnzFFQBmto8lSO6p9cNaNkRk3WlWANa8O6V3Y-2MWSdYFil23BzVcKMlPN45xDNkkgqGzX6I-yzW92Cs_AHjjutRKMInTG_eTyO6JMExfrw7EzZ4_NuPupdwjbU8gAYtFjdLeHTXmAMeMmjwlCVC0dgviN7LLl7mYnONiU4luBQExA-QMQvfVJEUeaZEPR4BK_1YEVS5LOgVzrCLx__K0E1bvJBqVwAa_CCBX7_jmwv1wxjDVRRUTd27VcNa5zmtb0MfLHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QebmL8Bi_0PPL_T2tIMNF7ZV8SotZVM6R49HsoBR3ZBcFoOX6ChGCGvgN-Hr4QABxRbUAySfr0EV7UmEr8F0nBmzC3t08T7qFvbF7NE9gCif_7I0_a1mvdelCLtj08e7OVOTFzGMNBEzARqF_Iv_JcX0P9AVYczTDK2-hEPh7k07JUL-ka-demQDu-h0qBDJ-gII52xx2xRzQ97tAmMH24Dc_v89GDg1eevLN34JTxfYQ1uG_gIVSKgkQctz_lsPj9Nh9cMO5ZV9e0CLcFWs0vwXnNF3QbtbrgP5UVc3Enbfvol4aYVr-tQYZP4HQ80FQhQmJdYw-AFO8XXjSPe32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=lemj6utGNerDhNf8YAaiMvaxvzNKLV0AHKMXZrYPEetYigRkXsIjsUdcHTg7gi62NBfiJZUnocIzueQJfrBZn6W9po6KaxguYvmfjBvNUD_plmC7NgRkzztrvWNGV0PhlXkFdP9MBkhMRs1lPcCRKT1FmSRSIdgTFNRqlUOuoxsAeOeP1T36XER_PywP1UnWAziLxZvKEwrPV-Rodx8JEWuILyLOnFfurWrS5khTGkDBQLpy0ZWs4wJKZ0DjWY-Ynwp_laEgcTknPD1CVnY_MFg1ZpVyhRHXzx1ApaDrbDunFzuCy716a-mkaMMoGzKefs7bwdLYRBmHX86SXKvGMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=lemj6utGNerDhNf8YAaiMvaxvzNKLV0AHKMXZrYPEetYigRkXsIjsUdcHTg7gi62NBfiJZUnocIzueQJfrBZn6W9po6KaxguYvmfjBvNUD_plmC7NgRkzztrvWNGV0PhlXkFdP9MBkhMRs1lPcCRKT1FmSRSIdgTFNRqlUOuoxsAeOeP1T36XER_PywP1UnWAziLxZvKEwrPV-Rodx8JEWuILyLOnFfurWrS5khTGkDBQLpy0ZWs4wJKZ0DjWY-Ynwp_laEgcTknPD1CVnY_MFg1ZpVyhRHXzx1ApaDrbDunFzuCy716a-mkaMMoGzKefs7bwdLYRBmHX86SXKvGMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=OqQgAiw-oQYLQ4maJv4LHLA-tWNzoRX6L-QPj-yPZVjwfo-8-fyMlv0oxk3LjSG5Iw2L4KKDG_Hg7xSRw6NwGgurTEQL6Eu1wX7KUobMNAVch8p0n1cuwF5mlZMjKbboOVpta-MuLeTb7IIb9o3ZDleCta-J5vTcHMyq1Uxbzdpn61wCQVpOLyKqvK8L85QRAIOT-TQq9kddU1arTWLvK7LvMFxCE6WQE_usSEOkQpqVOJicGfJwH088ZT1lf7_4YK70vB-s3XTDeJeWnHeJpMO3DplbyDayaArLCdj0xvIDLLtfA-rizjsHRqwwkCxsm9EJ3y7uL91Kg52CiTiEjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=OqQgAiw-oQYLQ4maJv4LHLA-tWNzoRX6L-QPj-yPZVjwfo-8-fyMlv0oxk3LjSG5Iw2L4KKDG_Hg7xSRw6NwGgurTEQL6Eu1wX7KUobMNAVch8p0n1cuwF5mlZMjKbboOVpta-MuLeTb7IIb9o3ZDleCta-J5vTcHMyq1Uxbzdpn61wCQVpOLyKqvK8L85QRAIOT-TQq9kddU1arTWLvK7LvMFxCE6WQE_usSEOkQpqVOJicGfJwH088ZT1lf7_4YK70vB-s3XTDeJeWnHeJpMO3DplbyDayaArLCdj0xvIDLLtfA-rizjsHRqwwkCxsm9EJ3y7uL91Kg52CiTiEjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNF8Mbm2-SKdLtAM-6g-5sZAF3pcYrbgrEy5-2hz6JmgFgcfGkuPr1z2S9DVmvKqpkQ67keZ5L7i1TfBlnGrwhXfjL7J9kDLjhy0Igqr-FgkVviumcjaA5gPO_p0vRvD5h4433vxp6Gip9eNCd_4jg-nbuzxorzT8VDs2TOPOUVRPgNsYI6qcw7e6HwNYSegnY6XDrnrh98LzWUmuf_UvEnms7CymcjcTQsg1Ign1Kfsd92WR0NOOOQx4pEp-FE-Lh7qqPJamUuf40lOzLCPjIU8KihyIqn0vlxVEv_8klMspAHs4tG_ubu6hgdI6xodcuMh1SiFwLPK_BmeIrftLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=o8t2gh-HNW6kFWkH0XCocE8a1mUlXV7GFmqycvPzXtgshzQNhZasseV5ra3vFVViqubUkeWMv-unr01ucEqbTY2tuMONMaNsN_eZY1l_Ll0SWrmqWodDnZKPa1L99XNBMSllSS7OaTGy2rrCyQWEuhUVon6KUiyD5PcdRKkOPvGddt0AsLjVuiqVQT7urjbQ9Q9i-4lmu909isNjltVCjix_07VsAZ12riiq0L_56DhL4iCxgGp0jKh-1J0UM4X3KoJ8pSTnetLwTgn9e7VBgG1tNwAkSYYwjVjjhIAtWRoQd3Glh72JexWE5mVIcVyVhhlMqCwDbsZHAlFMauFSFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=o8t2gh-HNW6kFWkH0XCocE8a1mUlXV7GFmqycvPzXtgshzQNhZasseV5ra3vFVViqubUkeWMv-unr01ucEqbTY2tuMONMaNsN_eZY1l_Ll0SWrmqWodDnZKPa1L99XNBMSllSS7OaTGy2rrCyQWEuhUVon6KUiyD5PcdRKkOPvGddt0AsLjVuiqVQT7urjbQ9Q9i-4lmu909isNjltVCjix_07VsAZ12riiq0L_56DhL4iCxgGp0jKh-1J0UM4X3KoJ8pSTnetLwTgn9e7VBgG1tNwAkSYYwjVjjhIAtWRoQd3Glh72JexWE5mVIcVyVhhlMqCwDbsZHAlFMauFSFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=IB5qOsQuXElkGxSeMu4UZj59KM0xtQwR-IM9YuwuvHiZhA8wA6Wnu6wY2V8yW0jHpwMTJzCTEPmt8mu23jkOg_OjqgCXW8AxRS5kfm_kMM7AVRt9BI6eeCCVFAOpsIQ2DSrSkDI0CCM3gokaeNG7J-7NR87w676soPNuwYxiG_V-rudyH05sRJPUbtn9M44ZA2K9Ft9L4m0bHkEcf6kqp8Rj5gXrox6MNS2R4Q3AOWHTxuDyDPpRzyQg1e9fU7N3gUPQrOKS--n1nECn9N8q8caMueRHPxkDDZxEHS8jalI9FKuK_Fo5H9vuT5REc1oItvguHza5JElqyTnHJyPutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=IB5qOsQuXElkGxSeMu4UZj59KM0xtQwR-IM9YuwuvHiZhA8wA6Wnu6wY2V8yW0jHpwMTJzCTEPmt8mu23jkOg_OjqgCXW8AxRS5kfm_kMM7AVRt9BI6eeCCVFAOpsIQ2DSrSkDI0CCM3gokaeNG7J-7NR87w676soPNuwYxiG_V-rudyH05sRJPUbtn9M44ZA2K9Ft9L4m0bHkEcf6kqp8Rj5gXrox6MNS2R4Q3AOWHTxuDyDPpRzyQg1e9fU7N3gUPQrOKS--n1nECn9N8q8caMueRHPxkDDZxEHS8jalI9FKuK_Fo5H9vuT5REc1oItvguHza5JElqyTnHJyPutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTRDFs6HJWpIsvvf-HmmjkHooMExjv_ohcYCIxxJ7h5pudxPzg9FAfuFisujxZ-D7Ww4SrJ1-gbBIXHBP3bWaGl_egcxVb1_5hLJAYsU1kH_oymWq0GccEZyI1CZlFhnA8Ur7ezUFUB3QuUGC2YqTbBZTOL9pUv5eIPA7q1AaNE3blwNSd2vvwGX71gAXLLALYXvm9A78PAQPNcTMf0m0S7zdvozXLR22WGFhjOAlGSfunhXzRpUDNNoWiW_j7U1SwXGMTQTL_eLDiijWAPOzi5918kImpyQ392tM6oKsN6fSKyHmAGTYvIabtMvYAv_hta4MTfqtXjVIwRHFMtqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c786hY8RiTWNhVy4JkrcaEbziqPb6yWIIliFSPyrUIkTl5dOj5uoZ2cscrt3IbJD0QavzcXJrQHSm03oUXC69wYFTnJ-x5iHPtVRxlRt16wXprXBGFmYWAOyYC1xkls_HLRpJMhpgzyk8mmqfuj04Ym4NEm0ITZm0t0RFQCghoBJ_nHQgXNZuvSYenbj0y1_yOuHxi12PdO3whXlLse3xDCjvsmDZP1m5X_FUujzJQMfwzcVdY0Vo3NCbwaE4ravabcH2b6RmiO2tNuofcLPA0Ul6ZcOb3XUbtVPSFdrYSuCMVTcSW7Ll8P2LbuZbOuylrUlVjmzDZK10eDfm9pauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCcQqwyRAWLQYvyD4DAZs2xvFRd7Ck7tfa-5OycR9jWkvlNe_ja-fy9E1zfFbjQObzCUsX57BOG3quWQbpD8RWW-OEwowIKUe461JHaKVqkejH4-Hft_Abwwy5XwCY7ACpvpeoJIC2pRRKv38Viqrqy1saAorA44QSndKU6gQydwvaLty9wWDqfjwsTEZxY59b3Qb6H5DENSOWZpy4vK_may6g1iFYUTYxnjOr6sK7qwV3xPr9g1XgtqEKmYxoDEbEdcCqjGR1e1N0iPDcMBV31vVGZNM3HfWXHI86QofUQ7LTurD9kNLH804D6_uVv1AOY4T15yQqV-uCnf8cRE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=fe3P5I6hLQ5ncMbN0OtGLggByQvFNcgpvYG1ZEZUDCHE9znmNeqGfVGxmufc1CjzLEtncTah24NiWqsukkEHmJi4KQpEZ1_K3m2SEhIRV7TwDwLEuSFQubrWrPP8uz9fpriFLgMYufmiXXRxbnTcZG7KMT4pNdgKVpP2BuoVgjuPNRbldxf9X6t85Su8KqlXsUlx-jZeTIJUKy8zWCYJF9B2uUFWbArHstEEwOG9gXbsafU5bA0GHRiI5dqugiXF17iL-H4fubJFBPrjhED7kDkZkj7AXyBA-hS-lg_hTAsDCmk6DVW87DtB3ZSbQNG5vmlmbmC3d-KffU3jCyDC-JxUTQDJsE3VZH9GMfXIrF5imvyBh1q5ZZx7iJJlx7ipQRH0wpO9ryTX6sTGQ-tLSbHhlpvHoI0ylRhmmsSoX5wZihsBypdaJIQZtYK49U_O3yOMcbc5qQCRepiR6muCkOf5oGlsje3y0ObNyVcN_ct-Ytk0ppF4bO_rLB1S0-bqc3kBktYDHTKJMm9Y0VLLC_8kB-sDqb0qpUiDLbZH-WRMnEhdB76nxFscQO8W9PBlGHvvSPmGSuptpBfdvhifMgaV7OnktgwBOiDog5iSFTKwmDB9fkvPdiWX7ni9w41cym8OHhuUrkUBFkbQYUl9DCSGF9zcOc2Z5Cqb8aazv30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=fe3P5I6hLQ5ncMbN0OtGLggByQvFNcgpvYG1ZEZUDCHE9znmNeqGfVGxmufc1CjzLEtncTah24NiWqsukkEHmJi4KQpEZ1_K3m2SEhIRV7TwDwLEuSFQubrWrPP8uz9fpriFLgMYufmiXXRxbnTcZG7KMT4pNdgKVpP2BuoVgjuPNRbldxf9X6t85Su8KqlXsUlx-jZeTIJUKy8zWCYJF9B2uUFWbArHstEEwOG9gXbsafU5bA0GHRiI5dqugiXF17iL-H4fubJFBPrjhED7kDkZkj7AXyBA-hS-lg_hTAsDCmk6DVW87DtB3ZSbQNG5vmlmbmC3d-KffU3jCyDC-JxUTQDJsE3VZH9GMfXIrF5imvyBh1q5ZZx7iJJlx7ipQRH0wpO9ryTX6sTGQ-tLSbHhlpvHoI0ylRhmmsSoX5wZihsBypdaJIQZtYK49U_O3yOMcbc5qQCRepiR6muCkOf5oGlsje3y0ObNyVcN_ct-Ytk0ppF4bO_rLB1S0-bqc3kBktYDHTKJMm9Y0VLLC_8kB-sDqb0qpUiDLbZH-WRMnEhdB76nxFscQO8W9PBlGHvvSPmGSuptpBfdvhifMgaV7OnktgwBOiDog5iSFTKwmDB9fkvPdiWX7ni9w41cym8OHhuUrkUBFkbQYUl9DCSGF9zcOc2Z5Cqb8aazv30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWrmb8juFZLOX6kvo4tsqi_r5ID6Lx4GpGj_A9QTV1an3OTda2NA1m3V0jO2X9fdcrTGJD0_mZLJniAoSxklzbiPapPgR1CVv6scJ90IvSdnnCoumdEmdbSkOO9Ap0eKtYSbzNFS2ognmNnmlGKnrDOYwezQVGGWa480sm4w2jjrEVGdlHivaKLeQ-CSo66DCQ8IkhwWrZhMRkrL-q9AKwrgXr_FKiz7R2BriZMKRIhe9OFkmrBQBcR73A_zLEwI3_fs58gUCvl16Qt8kzWZD1MT3CxGPDM80CXs7hz1kUvbq1Ce-ysKrMC9SNnFx3dDwy_7NRymIE5iytbW8TdC1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9V18QFCC-o5Js_fvIUUzl8XT39bgRFROxkrSEwhU8ySOd80h8U4UVO0LPgm2jgVpvwkFPDkY1yuG5q22sQ4sL-lND45TrAQ5FN8l5R9teJga1xADuaLixXd5Bvpk27qlxXr39LsFSXUwvFC9K2eJQW8ZpwWGiyN760ex8zacI3T4Mn0pZYa2_E0EHLQ2wfQsWDJZJSKOk15VWOqvMDbKeJ1phY4Ic8D_aVkn9XqRxYN0TxEQEwOVQKX0wkH6tHltCEdFLNfTU5EVQc1rerEh71Vl08Ha_lgIJk0TSkI_NS_uUM0LrgbdOuSntfYjdpd18ZefzwYzc92QedtR2iocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWszwtpwT1VXTVYfKcEoQWfq3HC0AFgV6lP-jKOxKpuafyot6b2XyFLv5nDYU40-ps4rXdYUSh_WroDcMEaKCj-mt6ZjS4uoWL8k70TJpSKUWcYFAT62NvfD94ydXDfgZOLwScUkfSARe2ZRrUlLtYMCZIinIcluTNesVTA45x1VBiHYv-jr5tqvpBenItApje4zlQA_oYwjwMCPoArfGDQcOTbZTohykllJLHYOwbP3d7hGvuD3aOBj0XviV93o7H5Y8E8MsBYsQkv0hR6MFNBZ7oA7biKc0uFkPQg2a6gOA_Yo8FhgJE72DJxkWB79LG3OKIJGpOSCAcRVdlQDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRQj67yhT066VzV-rCgraayyDYEiqjjEUSGUL4AuVRX6R5so9R-HJRMCLAjGMv4RvE8P2SKjAhN617-jYfTifzcpAZ-3syZwTQdox4dhnkp1_tckZ0KorRWy1OFHna6wxnsPAKc2wsrDyWMt3FGtyv7jq0Pqs-uvFTtof-0pqWSbLs5XJBxd02qm4zEEnsJFu88fJEjKi15vx5tkueGg7U4oNJXA41khOpi_XIjKFWsrRgTGocl_SKpgxlx_6lxYe4PW9l3zKoMcZpJ3_b8j-UoOI9VcPdp6TwvXYtkY8nlnSfqxuJJrkUiveieZ92ROZQGBiNy_JXegtz4QnNC0mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3QldbNOvyGm1yLXwZFIN8CALsW1RQOzppVZlbj3pEhjMchcOLiNVqMx9iAEL85xl5IyZxx8qWhCTGTEs2uCDDx9BeVtPKDczPPHQRXElACpPNgim-BLnj-LQoi2UUJ3XvLTt3BBpzLvvsaSTmadf3ou0laY2UquowRvcaSb1zTwylco5AaZP7q7LLI8oXdH4ONiNYgvwvUWyWX38hZOhNzCOfyOsBsxJhfKIuLCjmwZxzgtq3FzZd1vOL-xGR5NtDMTzYKt19cgpcEauUcqfTKASLUK7q2UCODP7y4kADoVaOOQd09OgGRW7Xv-VOVV3BOCm0HV2ENW6aFONpRgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
