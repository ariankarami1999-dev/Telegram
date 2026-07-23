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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 15:38:44</div>
<hr>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJJbFZb63tFVSKU_S6oS4yPXsafURms0CrcF_5A8rEIQjXhxLhbGAj-ucIk6QW111CmWXlcj5Q-6d1fSJ8Snp76mNC4VkF2QmU-2wbOvtWUMhvl190cKgVFgVewBG-V0qlJuUQjdrv6S8DYiEWIrX3R2aJ9VfO4Z34790s6TYx921XVIrNYyjyPfVPTjFwwS_fEadmNymgpAkVKhjM7Ey8qxg35Pudj20J5zecjfaK9ZwR8X-67pnRBjF0UiUznhsko6lzVIGxW_eEnJ9Kak9qiMxpGcg40hHlr6q_RtmzMt2Gc91g7ntsSxvgXx957GMjkT2aFIUzWPhYcCcATpJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJFb7yQgoTuZtg50X1f2eXsWSiBQM-l4suzT6WYQvpGGmfyQnXal3gyatBAFkg7CgxrAImcA9iRyt5TYOhE_NW0f4RFLtIoN9hH1l-O1pM3L7QvxKCLPAxfXlC2Y2EavJP3dvwKqC0iQiNHoqK_NmoMGurZfNss1k_79mwcM0xOkbLE2aHy1fO16xMEKYAK-xPiJG39_Ee6n7fTitxI_XJTHRDe5rBlgRHB-OX3Uv7bjxy15cBM7CbVdaOPZHL6em9RlcvqqJ3outtzMEweeLWG3ON9a1R7z6wYx0FdGN7hlrWNyAEKDqToiXslBUVAToiaLeVqd_hbaMqaskJtnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26346">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWagqnPWTc2Rgnz37aT8k3zGW4d1jGTmGFZ8aIBdnKLNywpsxBMzm5ruXOWctfQZdfNghkhiIaqThmiqEopC-AbRrqvP2cJMHnkbL2WJmCV03IEmtw8BhdBeQF0WtPlSRVbSGl7Q6cmVjwglgNRbZQzD2s_ayPwElYqFM1SwtQjF08X7AfneA-yb2TiBdRgdQzaM93xjsShm9CtK3imDiwF0PEE2S545TUvwancZBhRhq__XFSq3Y3t5gjBUHV9fwlFEh02jwT6USsRfbyI7_0FIQH_TCwRuc5kqGSCfSfK04aZs6zFPxGm1mLTluq8Daa6IzOl1k7E8X0aPwXh9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/26346" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=DkttDk_L8YCwlmjYANErDHhniJKAM0ky1GHmbSc4ron1iZVFCaKgOuc-rpOVRrP4raimdFt21M5DkuQgjn8_7m3WfDlRJyW_XkK664SOGrROakoGFvwHJeZvMNmddcpjtcJ2ccjJT0nzqAnRfLYNb_gZRpHVxd6L4woiJr8jj47hoteIonQ3FlzvT6hoLRG1lqsQSBMcHUmX_QPNHEPCHUDyxgrRxF741jBSlI_gU47B9uYUxXYoSeW2zRG_bB6KbCyLtADqJOqEFsDvD44UeU4s-660guNWZMwzUDLX7lemRuMTA0FBshIMYiFMYfPg8K_JIFNy8tjDMc5gWx_GZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=DkttDk_L8YCwlmjYANErDHhniJKAM0ky1GHmbSc4ron1iZVFCaKgOuc-rpOVRrP4raimdFt21M5DkuQgjn8_7m3WfDlRJyW_XkK664SOGrROakoGFvwHJeZvMNmddcpjtcJ2ccjJT0nzqAnRfLYNb_gZRpHVxd6L4woiJr8jj47hoteIonQ3FlzvT6hoLRG1lqsQSBMcHUmX_QPNHEPCHUDyxgrRxF741jBSlI_gU47B9uYUxXYoSeW2zRG_bB6KbCyLtADqJOqEFsDvD44UeU4s-660guNWZMwzUDLX7lemRuMTA0FBshIMYiFMYfPg8K_JIFNy8tjDMc5gWx_GZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIT1fTrPzu4C_PhQM5ozlU9oNZHkzbbUsD178TQLukRksm9ARnJ6Wngptn2IpJOOs4Rsm8gfwbzI0QCWIF5PG3H3a2dzxXNrKnIHFTsTc_oiXZVL43EwQDFySGul8__TwPgxqBhbo2ksc8XlSkTc6MNbLJAhW4HP6rgSf-o8LYqeK-1CJfmFlufxDsgXpbJxL_91c0LaTpdTBVUqwUldOCSetjP3TFNQSCj2RnbOE2CLpWa_5eW_32h0_-kqzcOF35BYKd3j7tfaM1nHElxeAh4VG17QFVw7Bey9o6HYF43jV95P5-XsQ0vdNKjkAQDp_BoYFV4WfqhUBiUzWq8htg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur1OfUBdn70HhtK5vDyYNONIbGvN9v67zx3ogAYV9i3AFjs4_y8O358j5ucieDLgmByhvRPK59j8onOUBztuQnIP11h_QhpYeUlqAZwp4CzCYQ_VUyECUaIxiVE1sDgQOyjNbvtp8hhToYtG_QU6RaYBVq_K0JLBuGVXkR-JVcwuwn2iMI1w5G7mO4dyhaMfjetBZ771dUyOfGnUv7Fn8ULra7UxsGITyJdVmhGtohQBhGGVLzHdBE1jlGenStg6aL7c5AZsHJuioiLNrXpmK_X287m1IwbkvtDKTFfn67sKty2X33__5Y9PeJ1jRHlL6Y-9dbU8ltQbp6jOTl_oNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhL-7w1TUQ_33jcbFyVaTyHSpO43OwVbkXaT16pg-m9LWn6KBKmgE_PVFlXTiawy8RZetw8W5DwysSWNdhuWzGvThaM8oyUm7Cbff4aDwOMm7jWqnNpkByOu6HDOWJBdaYvaMrpbvfCiVuPg2botEwBI_vUM3NX2DVgz_-U2LNXrGsRfyCAx4k1np8ai2ZCBjm1rQjYRVwEAirhEonOJ4xcQJorBqYrVSVm3gNDREFIgw6mRB_cS5N1Cn-qWsLkyyXxgMLgNlk6hXDTGsd99-jEI-Sx6DijnxulP0G-G_96RJXPQfPh03snrd0LY3W7KxZdH9vtrPj2TYOYgzb-euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3uSNg7L8uWofXmLPQTIWhn7Hl5KVvVUv6BjrrP4vdv74YopVYBmE7_OVjp67gpiyn9Feims7H2-oKIcAPLZNxpXoZVC5sPPo68XyKMVIf8vHtRSFnDqg_x2k64ylRVmd-pWiF6lQG9sUBhhdbOhV_imejhnvqmVu9zcHPqxdsRe8-RBvIRuNbw_OlNi3d0S9__Xp-K68bvB6gTdKgFPICZo-HZOJBBP3Gn0UnYCv7xozKizOJcOCx2DzzRtUfy4-j5ArhMxu0rjUxLqZRK4uxUlfSWqEPja7JaOcdQW359vykt-G6OuD8ZhRB4ALcRzcK2GYjc_k34uXVJDli4nYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6BQ2CTzMycdQfKgUqs1yGsHdzUAqXA6-VdS-F2QcJIfzKQL6M8kdjOf_oCJZydW3-zf9Bz5u4H32hAMhcGF1zpixw82gG6NHDfbuTzUbb3zHXLnUKUMHVPNNGk3swBVWtZuBBlsAUTRXyiFAplekbbiEeeH8YhkF-6m8Rrgj6Is1cMu2_FtSfPku78vJKWYLLDM88clSkJqyXjzFz9h4w61NV9gaHQj2WsIoYYG3Ic-P7btHnJpEW2d7YTJlxCV6F4_L7CKQr7001y0ErJ_FOPejCO-vj1UFzG0_tkmXWPJaXh_3CEidJoAPRPIdYGPf7wtm__CxbO15DvFE3IU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIHrhGH1pginezTNwD6O6DitAxlxUpWXaKBuAWsCNxgPPGeno17E4AdUFatZxq1gSEwhbQc79l6DX2PxccafKddqN2j4gW27vwzqJN54gPqthDp4j5A9fVdBMuXrPmZC0tDrFZbrqoQtULt1bf_0juWz7EvsVM_8aTcnijaT05yqO8dBYFLHCBnoua3nM6IKnTWNIA3-tLyPg8rgM_43vvLkeJDmfuPaaXnYuHymfh1FuuONm5lQutLEQCpXl9zyn16Kg_Qlh08b67ulxzvff5h2hWMnNwKVJrgMEhSL98FeJT9HZcPfV1TTZC_-0gIT5Mn81jS1P6WUVWVvKbCyug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUAiyg11op--ytOQghfGqaBnUXCmvMAXbCjlUGQGNKJcdaEyRVRJwf9bsqmDxItU3xiYgCx-J5gCmxpI3L4kJfaTTvyCFuzrTd7YHFTHnhI5i0cxT115r7DzZr7mo0R9YXSai4Z8Fbw9Jq8MTBVBgovmy_4xCbr24hqrBEtAgNPg6AQnK99f8t3Wsyyu6RJMFx3wSxv8UJa6x2-V5JjIPlRB3CkTMO3LJZ8e0ypzavpfy-_c7XaM2JpRzqEZYPYBVOutcFXZaMCKl3wcJiFY4ZQYjb8C7iutXoWm8WFjq70ZMOg_RHPtEPxxH38QsjeiyKr4UysljYXt_WFBbRvH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKbK4wD3Fh6Kbk9HtkoT4SJZK1-66q4VMZK3AdYbEPv7ufuqITZb3qISMVmBK6bas3xQ302_V02_0K27KKCtEHzBwhqAcByst1dQFywYsQCPRwa0mdGRzfGuP6WDRZVEzTVPADDENdLOOWq7qtXD2dadXsS0elkz-H5CNi__XFxVQilY-oOf5X-MyP_2Fpcg0KvsBabeB10zvZy1JvX4GIZPzqNKNwg1Kpw_cZ6_iKmzNWF3KBsDXBYZTcZyNFK8-EqkZPEdBnzH8Ej7FjOyMOyaEiF9njTzdmnKkxcV0qTlSDPQ4MDGQc2RM7m2cV5IZmQmdK7vhBfEGjpmZUZCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSuZ_MLKdZldb2qdw5pDQ6OZD0aoTz3aRfbRIUyUIZf5RJaUoAo27EmixI--QBSMWj7BkIHlvSiFyZaGQ_uzZVMVup0WSwqx8_b50a7YF4vFx13EHApTMRMSiD1wDd_PECKICvJD7Z9UX2EfIH2B9GNST2Ycdw270osXYEquwg-GQvnnSPoJXJ3rVOFXJgyYnnWZfKmpSF5qABMpTS0YA1XP3tE8dvZLVf2UgxqN-yZK3-abMT00iQfoEb_m4PV8ELn3B69PBfC0N34JLYd368zhQqe4y95ygzmg3WeeAlm9UbMYLvs1s6jUJ_AdRZpcFP72Su3UbQeltprzKxnZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZkCYgIYV8y3JYVt-Yuj0XQyWszcVRJcyigYZSf7mORjoP7GIgqMWkzAhcIkCdCJGZIvvBXpC5qh554APCVwserbybHv4l2DhQnroKl8m48BVQ9Hy7rLL01Lnm6gMvpgbnmGHQoAl9W_aNiZyrWmdP2ct8Y20C-LuHldYCRREBh9I6PMxmh6M6EU4fpJPk4ie66Yg6IexPQjBtq72rg6HPS_R6Fc5mByWoKv8ZvTHNMMKwH706YM-XoubZCR1zCvaKWETzUCq4Nb5JHlVy2oh_qzO6CO-d5rL2t3can1Ye43a6DKEdf7RWP5imHvbou9M_PEgp_cWaulIqDNR9grGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26331">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26331" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIF666WOdbsz4II-VYTtzOhl8qKJNXwTP44KwdYZJ2m4rM-6iE6gNjS-6hdMwv9tfms9wkxAph9mQkI4GcHdxLWt_0t6m2G_gVL3P5KJ2CLs57uvy9UHPcXJcqvw7e1XHfap6FQeo0FRDc-KySsE5u6jkW7e-U_9A9aoRNpwAL0RdkQScRqqwRa3T1v-9gKyedh_DvENCBmY5R3mBd9XMDS1hqTKfthILCRS52moh4c5DDlywO45xWQLTfnppbcZJuM_f5p7iB8ALUrMQUC44HR_CzxrCLZhB55inXLQ2FB0q5HsaJE_Bj8w9S7LTqB1Kti1Dcb4dVbY6FC4ew1uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=mzk2HssewZkCK3kuxCA8l9i8xrPHFhQuxOSS1gGXiAOXANoDVRZcpIc3Q6XjbfgrwqkEPqH7SVDs9H19uGRG0UxQ4w_OQmPq9peN9DAJeViCRq8K02c7rkKG5TA1qSAw5hNf_eJQgibvKKwjsIwC8PKsJ8nssFTzpqAFECaPBXUjYku0shi77XSWlnJQS8YpBhb9mOblcgmb6f4Fdwt_ZxxvpI2qB5Vi69mZQJ86KFnrgdAPILtmyhZ7kTg9S8PRTW7g5-GDP_R3ukTzgT-lCd8a8FNnGSJJ4flnnN8ImDZnjH3nVNanHe6B0PBpW04q-ls8R9ZIWKINr01CpGktxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=mzk2HssewZkCK3kuxCA8l9i8xrPHFhQuxOSS1gGXiAOXANoDVRZcpIc3Q6XjbfgrwqkEPqH7SVDs9H19uGRG0UxQ4w_OQmPq9peN9DAJeViCRq8K02c7rkKG5TA1qSAw5hNf_eJQgibvKKwjsIwC8PKsJ8nssFTzpqAFECaPBXUjYku0shi77XSWlnJQS8YpBhb9mOblcgmb6f4Fdwt_ZxxvpI2qB5Vi69mZQJ86KFnrgdAPILtmyhZ7kTg9S8PRTW7g5-GDP_R3ukTzgT-lCd8a8FNnGSJJ4flnnN8ImDZnjH3nVNanHe6B0PBpW04q-ls8R9ZIWKINr01CpGktxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEpBcrEuMwQBYIKmF8caJlkyxur3g5lDJTMvtZlgeGLruau9txQXq1Rqho5m0-7yCUDw5gU8eogi_UrSQ1b4-vV8h356_MzPAD2fbNA4rXRHMhK01YE6napQLICATiCZXuebGQIuYjzPa_2Fsk5hU9AIrgngVMm9Mso0j1vmB_odlhle3qnNsA-1jZBpjVnlO2-GSxwl2xhkIRnYbq1pQDIKh-9ONcA5rMuAlNdr-ABCqnnTTrPypjZSW91qkAOBfDs_Y-hdfyIk4cIiwGK0Iu4sTmHFD8Ma8_LUQB_Zk9u9V6c6ty6bPPfbky4zm-5Ao46R6cElptxZcmmNaS657Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=rBzSCAb0L49aJCVyZX07tP1Ihp2BIyWRgXRoEaKTQF-2oI94x8v7xmbUyxS1XGL9tX3RryVFI0jJwg0GYlF7rs23_1VDIhpbAAnEXoV7rZ3eJwxZU8cxFhMFVaRoMwEnwlZ8n3kl_I5S_WQeKkBBAKTC7sBGjX9RgGUjdfZ7lMd83SgXNmSi0-7auhpLPa8HKGMVaTaqVQ1aPATt6j0wJRII4nFlbeneymZTQBU1WfyRVxgZ5o8d6wskdRY0A2MUrRqO_Ex5Nm9RLLq3olGG6cIAVpb-pesN3TyetfYsNdB1mveuyR_jpskcN97QELSx0opkz6dG_4nCKd1c4simSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=rBzSCAb0L49aJCVyZX07tP1Ihp2BIyWRgXRoEaKTQF-2oI94x8v7xmbUyxS1XGL9tX3RryVFI0jJwg0GYlF7rs23_1VDIhpbAAnEXoV7rZ3eJwxZU8cxFhMFVaRoMwEnwlZ8n3kl_I5S_WQeKkBBAKTC7sBGjX9RgGUjdfZ7lMd83SgXNmSi0-7auhpLPa8HKGMVaTaqVQ1aPATt6j0wJRII4nFlbeneymZTQBU1WfyRVxgZ5o8d6wskdRY0A2MUrRqO_Ex5Nm9RLLq3olGG6cIAVpb-pesN3TyetfYsNdB1mveuyR_jpskcN97QELSx0opkz6dG_4nCKd1c4simSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iF4f09gUrdq6dlQ_xt8gv6CUFEO6fMNL9zhzvBaF1sxGKON_i-xr8G5gN2eOVJlChXMX5GkquAw4rFCNs6edy9X5ixIO5Km-6-eWJZrrKDvTJt8TMg2iE4ij7Van0pv3FfDYW8kHgor1GLs1E5jWpRpIKOgtPwn57EKw28vuDqyg5eBvL_7YWknm7wGXe-LSQjV4z-LygwRsn1JANWENle7VJtNCuE5vImwTjsG7o3h21eKcHYxZqYBMJA7ryFOJ44zxolf-VnvhCYDRXLZ6eN_w7yf7odvWOBfsnY8SYexQzK_yjcY37kiiRLCVlUPP8l0Rc5Ne1PyiiKwjQAFrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0EYK9PCFraGcbhv2tWMJym22TnN4cRcK0-cPYrPX4PRXhjuU0gCPljWlpq6tQpyJK32epU5_xMlaNc6FbSQyzY6bLnoblEo9YkqFKFt1WIRaJGqqCVlgxrBN62RjAIn0S99BYtqRGE96fR99c2-HUZBGjZNm_09qELgWHnsXJenvyREUUdYmkxu4MM_HOsIemqrs46T_iVOLw8t2Ma_RT9e8Hah0XSDS1ldndN9rRa9hAqU_WvX4wWOkdEex1RbhmYkTI1Er37_3eN2XeFRlEjRow7nwGuoAK4i81U0XvetX1_hoMd_jgG0GvqAawf4jQS1GCE2dejAjnKpJ034Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8H4GyVHJCYX86j1ePEy_e78Ducdgyu2cHF4uWugpuqlymNg68L6f8jdvQ_Qnq1Q68dXA1o4dK_uw3zKv_lj1MGaui7PYZXvqwdN9NwItEKU0eBvpbF_oSpDxEZs3dn8AOphZIqbBh1eJUD8edeM342TioHYQapBgRArXY7s-sREvkOJrzmb98nwWN_L8-MqSfairOnjOzqnGIkF7IrNJj7Sb7DMk_SWn4TnwXaZqvZpAXt414u9PzGtn077k-KTpaJ7y19CzCdCoyGPQ7AZPwQHvSakACdutip7o431hsJpX4Ee68PG91d2F20Q9eE5rPxW8jXUDsOJsRFlTMxFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMGgPyrHMNb328GrN90HUuB6kfcSWaVybBcj6fC3dYK_EOJn_KdcgInKvCgFtrVYIO7BcmkN-ElKuxRx2BdIuklhpxFZHzh4doy-sqPHO2LITjLBbVQK4YoClVSxDfqLrpctV16CO60IyugpDWPvuQtyhSfdzvUqaQ6j2rAs2QgRRwqRz5qglBQ-D6oq8ifGOQ-iUjN_f0hgRn59xx6OBvm5cNUZe2bdV07CBnn_XknW2kVSFJF1dfwnOW-5J-GnfVXFY4dC79bmsz6eeD3tYbDKcCoSZ427Lg1uInXwun_0xBfmwfViTQkI-8tOGKmIOeEtwGl9i78knMu8WrGkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaAJi54IsaRkGV_-U0BiYrP92rxCQAcqKs1rgSdwHIID7NOBQ5HRvcZsf3PXU6w_Gku9PqvqyZY8kVdxyFxigBHgu8qeyyHo8G2yR4VnpvR81J15l3l56iqYUqJip934l-BEUIPm8PNSkkAOHSf9zAyyfQHn-ob359BdLEK6vrTgJiiSrCQY2tv_cJTR8uDqHEI6KOF4mxBdf7qmZlXwqma9lW_e851K-SWfCn699hLSvHTE0hs_rLMe7OUx3VZCNJngE-OEGnPRBJtpRRYj8d11a9MO89a0rbq29xw7umgBN1tActqC5gQkCqfMVKR8w_KvpZkJLXwaZSIOs7qDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSPzzzwzeYf9Lv6TMbKuGjdikS24M7M-WfvYJ3bC4dIBlnBhUPI4YDoqhK3OCXSlyKIlpKm1ktJbaAywyOHkM5A2lDZMnm66khJnQR6RtSQVK74x2w5u-HJ_0ekCpeNHqmMhl8UiIpWHoOnnKVwogWYB5l86iiKUOZKAacsZerrgsNBPBuvO4Eq2npfM5eEnp8whvBbYR56lmMJq17H1soiSnaG_vp-dRdkEJaQfvN_HAjCPFVjLpTS3U2S1x4eDloAdE0yZR5N_Skct1KkwhRpHCVdR-_0k2qEY9Ci_UEsz5za_fQFxJJnYUpWyF6bcqj3TtxfPfIj-hwV4w2TKcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH_JgbpKp6bD_yNEdAUQ5yC_WEjMrAFjf4X-_TSWw0SEcpAaDEqsZY-Jo_DIxd1nJGdIapkHSkIBoPkFjjH4fcOHVfx-O60LEgdHgIVQXIVRfkpXJda5yAZtuIYU_kt-AO0lz_T2s9FvlpQv2M_5Df-afcDT35GMNuLqf6Y9UiRg45W4oeVsSgoBTN6XFK82sq7p3Ns-uzW5HivegwzBuYf9zqYAQU5VxV7ZRqbhsqFU_Hlp4XXJeOIJwUinlf1JFb7-hwT2BtSe1cytxDcFN9MJhn4mUWbPTkK0qqeSG19_HtNIaKr8lqjeTsmrHGRi8RfkBBQP1bJcRxSOmis-yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCDQ53dVRSVLigWPOWQioIONilyG8qyKOqzB0JikvX4OqovCjmzVk7DrhLEKo21yZpv45r_gzvl_cLUXxRAl8IUiPoVC2t0bxqLjXQ3g9zoepr-CHPAuG-BsAioQnYZtNeML3vmAOe7VoZGSPGRmQAwVJTY8kFaFSAVVTK4PKJEq2gGtkyJWXVise7Ftu9X713qtl2VrgM-oLhM2KsEhLljDsCxLyfwrii_q3v-DgmJj6H_C08JGVw2T8BNRJapg9_APcDQ8vStxjwcbO2OPaAhrWIw7jjVvMtamU8KE-VBG-rCD0t-1qJl6Dd-Uxgf6FPVd3pbFS4sXXdJtO1GQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tH2RbeMeZ7DMJBy2lDS_-W7TnEmp2wMRJSkH4IGplnlYVQBCHGeznUKowB99nA5oEWh36A4X7Te6f79uMrY1ykoBzX-tP4ZlCe3wQY5A0cq29ojYuapogSgkErX-UCyEKeFJuQNyGVnBXrbQM0B8xCN8WQeWvzYbkUhm_CoW6NK24xE7bNrkEuvjsDL6o1omr2IpLKavehvNSk57oz2uPkKIWsiPtDlh29AJye-cgahFvWlD0UR2-Ooe0hjbB1kMtDuvNHacvja89NIk9-c_zf72tEohLh2kmxZoeYIqC-ZwlV5UEny97gSuGPJpGq2gZPvsa17OkUgRJYZOvRFfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfgB8Nb7qHGzfA-pvinF325sFS5XcYtj1VO0CFdbtqd8zMZCIjaWTbeaSg7tIZnvkwrTrXJ0sAomXFy_4tUubemmMzjwCMm36RFN4BT5JnHQNjj8b-cEpZs_mZRfZxdmfxm-bPWcPqz9BM54eHo-D7mz1vKrOgwbq_mcI7MAoxaxpHep6pTTEMTQ9hx347iBkqNKw0HVy_0VkCca7mlTnkZgSFpecot_e54bYlyQ1BS3UxgEQLKThczxTfmPzaVyhBQrTWRUjKMik9OtQQ3juWBfxUe6aUVXktXIc6iwJnR8oQH_OnRdNcNEiwTSX8wR6p0mvp3U8CPV37N1HjnnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ0HJqAh26asGcJZtmV9ucW08X73JdSHIZIsMiOACeqjBtfQV0s6fr_sVNSQANf2Mk1vOODnrfZMLP2jxOmmEtWskNPpsJVvWozhYW3ZKfKHDnL_3bzo5Ug5518eP9jm8gF96GW41dvEuG3N43Z2tnFh3GvIM1cBSyXWq_7ffFmX70zpWs2CJpTsHDZ5yitJGCpv5En2h9m79XtnOQlDIT6SrmRrBjnLxmUDSB0fvwuL7qf7bEEF1VBdvOhReWUQFVwIEEh_vVOuExDfrc4YzciI9x7LC56AhMhvZ-bpF80T9U4udlUv28378PWCYiJCnUZ_bG_Q3LSaUDUm4SLf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u52p_3XRjDB66XHHcd3eXrPxCsAO_1p7_ZKI7xv3NvEtdSASDAqkjsC2pBB6nxZGQ9ZdNh25WO7QCwSIxbBrp5w_o01kz8FZ5LZkEuwWwkDTBwnARJRRe2qq4JChcNFDjyUWW0s2M9TqyIJ9RNrQ-OltY8ZX2dsJkqEeG1h45SaBsRGm5NYXcMnCqixUPSbeQGYfR0SlVMoUO8XvDylSamyWOq6-xd7RXhxm9R_yL6VJGeFOnTSP0vOdU3AF550NsMKW3XakkuPy3XbJ3YU8KPWdC01soY9m7hCpz01EVX-oE18tA3yYA32CX6C2dbbC57EoQNRLpzyFtH5I6zVUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=BzxeyjQ1nSyVU28m_ae-zhPcoTriKh9NHWUuH4YjNNeHfHTFsOiFdqAOBO9P_Ak1IUw0JBpndlg_q3Gylb3i7Gxw8_HOxMjWLGE6M81NsyhcWexmC_5GtoBxxNDIEOPw9WGTz0cx_yg_8NY_rXCznahwM4En_kjL5lYoqo2EZzOiry_GU7OUUB2s_RggAT0ckIYVyIlULINmQ2YLaqQQJd1dU2hqGPhzZWmOHHKhTsC_lyu5TyLMN_SEfN-YSAVQNi_1GKAT2I-oQ9LvBVM7K9R6-pukcX-ujUljMw3YjS_VdGkuETs0NR9M8pcoPwRcWqr_dGVfN2mkojuwi8Ikmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=BzxeyjQ1nSyVU28m_ae-zhPcoTriKh9NHWUuH4YjNNeHfHTFsOiFdqAOBO9P_Ak1IUw0JBpndlg_q3Gylb3i7Gxw8_HOxMjWLGE6M81NsyhcWexmC_5GtoBxxNDIEOPw9WGTz0cx_yg_8NY_rXCznahwM4En_kjL5lYoqo2EZzOiry_GU7OUUB2s_RggAT0ckIYVyIlULINmQ2YLaqQQJd1dU2hqGPhzZWmOHHKhTsC_lyu5TyLMN_SEfN-YSAVQNi_1GKAT2I-oQ9LvBVM7K9R6-pukcX-ujUljMw3YjS_VdGkuETs0NR9M8pcoPwRcWqr_dGVfN2mkojuwi8Ikmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=D9sPiZC3jTfxY7QNLGfCqnYUWMo5U19D_YvpQwtfVJuxBiWHN0jjzMvoGbbbj5WwNmkB1JduCBoS-3gg--pzbtnuBee15As-MQJfHEn2QuhBjUhkFDm75dpTdqoDGMBWPs-T0f7HCWbwkDVr6iMeRbsdvafnq9vcYZppSumjLS8l5hbCICPc5KZzAP2vi-nvsVTWBgS8wT63oioQCLR6GEWvbS7fAybVU37OLWjJrA2OJ3aw8fjjsrvn0mqVPGyrHDuDGmvBjmYu7VTNj2bQorHfH-3WdKgzh8mxNMQUcyjaj0Ew618eXZJ-ulCDluaHNSc2GrBpm3TDZsKZZjOfwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=D9sPiZC3jTfxY7QNLGfCqnYUWMo5U19D_YvpQwtfVJuxBiWHN0jjzMvoGbbbj5WwNmkB1JduCBoS-3gg--pzbtnuBee15As-MQJfHEn2QuhBjUhkFDm75dpTdqoDGMBWPs-T0f7HCWbwkDVr6iMeRbsdvafnq9vcYZppSumjLS8l5hbCICPc5KZzAP2vi-nvsVTWBgS8wT63oioQCLR6GEWvbS7fAybVU37OLWjJrA2OJ3aw8fjjsrvn0mqVPGyrHDuDGmvBjmYu7VTNj2bQorHfH-3WdKgzh8mxNMQUcyjaj0Ew618eXZJ-ulCDluaHNSc2GrBpm3TDZsKZZjOfwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abcYmctNUPMmG4U95oW5hL2ZXXhYV0_-O5nhOzJt7rKw51UfE-wAq7QDvnHqxqWsRZrjcIv2ySxx4QK4j3C3VA7CCBRg5K0a6kdEtBWx_q-LssZ8ceAMNi_GQ5Fb0V491rb4HtW38YFw5_TDvIQCQ73YHuFYzk_NsKynf2D_3elbMOMT7OUoqQQtzDIYqs4Y4yP_RB1ETVmQCR3f7SzMBrgABlM8Pjt9Zuel3W3aJjJIqCa6j31CcFL2CgjqBscs3kcINl_XEJT2wp03UIiXExipN-7oOo3AxUylDD2r1hooVDcONxJQXs8Xfz5E98eKfSZQRcw_75ZWh6Xei7rmGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp_Y8Oz2dbm0nHDuNm2ozQB_ezl44Zj63BtNa6kAVcUGYel39nnWpBZDs6DetlTg2nc_PA2WzBMmXCB36AqI2bjRjUk0wTnyaJwyC6_2CLrxwkhCJv3j9iAqe_-HCpBkzwxGLvmrzTAHi06oZ5xc3AyhzDb-7ot6dQy4EZRNWTA17G9z1VQAZq1z5uW6pJdNFyFpk4s8gTFEfTm0X9QFJ2YruZvGTLJvptmiwzGrBiUnBs34J98VEh-xXkZ1ZdVnVFdggabTo8gOEH_V2t3cYXXDLlRN3c8mhmGJGfDpdxPTlys-pnRCtdLqdDmYz3jxtfkVsic2HDT0xbjlQE0ISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JH38ffnKyOET-QOvf4eMBikA3tfusDo-cysWHBWVYxVcuAz5Mi9T9CBHqBkYOIkGMyY0P-UOvD_jUllqdJrf8PGADBdoG-_HtNDdm6ZSZ2r5OSMfUG_NAjV86tiDQ_MRx3yO4PgGp4LlxmcHbBjHV7Z-EVU94zWOJIquZ7gzHNXupsRgvUYjuef0q6HWoXV5jgkehktg811M__l9yz5KDIoc8b79XPhz3VUz2pyiZaWh9R2-1HFAo-yV3rLZ--Zko9WR_LLCNylS4eQCKCHF-jcFujjW1v_Tvy7C6pXI1NLObjGG7nzMGJ0x-TXtQhB7fGyVUVh2Zl3BryFCWWNvUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_0pWWRx6fcOa3Yo8A6lJrKgnXhgHp4ghO77tJW1LAC6tMorWXwmMFWeI12nuDNXEAfGHN-DuBkOD34OkEwjMM3k4tCqMnzbRxTmQRC_Jm1rXx3kNRmnLzslxF-ZF1C468ldhUpbfspQ6td34JTEDhw3RWdDCCsLstYlQIdOx5b2p4MAQWnFIYF73z4UgrtXJUx-0av5zRArQmv8jwf--xPt0ksdobWGMEN0EW4Pj5XoQu5TkeqXrda4oFWitXkvMpMq6y6t-axaSb9kqo8uouEQVg5enUCHCW_rNrGfZoxUIbBw7qbPYW2aPmK_i3HBvzJSO9RQG86i591b-lhm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpiY3t7BiIhH_jw6cV7eeFyKtD7JGyXHKktjWKWW6_K420x6f6XmgEiJ0SGjQBSB78mwFnX5VjL2DlYnyTWudl8AwHvoF7Klpv4gF8o28P3zpeBm5JMvcZm7puhfzrRYsULEJROzjPyvsSAWG0Qyl7HsQ4R5dWEGhB2TZuDaPKP_i_g-nPEkmEN2fnRsS4i2Cz14RqOVwLTbTJUCxpPZhAre1hZjnhdgjubmtjCcHMLmNyWmJgEMqazVws3nhSrdbEstIzV8_ZlKRObPBcLS6JwoQtO9lmwRrCY3eWdTWzbW8-8ezBirbuLdvepnVI97hDMs2IFDvj0ZcMRVOql6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BffbDpbqXPTagY3XkHgTNuuiVOtRSZiMdfw_I0RmfHvNxmedJKW3lQ72zKLp_UF-HgF_IAevO85n3hy8_nsYSAa5vss3__zgOT4S2vC-rE4YQE-UrVSDBOT9MALg2j29us4yDE7cLBI2H1YdyoqZDZqy6L0FkWLS4UTORIFOaFOZejywsjWgWorhUzk297gvqfwx1GsxrUjJR_LIjSiGaiECy2YXP7_4MpPGBR47f-A7EwzfEk4UMutwv4iu-N8Sb7PW0svb4hM8JXbQi4S50LRBs2dXc78e-XtHX81fxVUK2RlNxAobE2DU1v3zOCsFWf1f2Ov6UrlFonXjmeERMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uz77MX6szQVQjHxesh6ADyNRWqXpCzR41u-PdfDHlMfG19NpatTnhauhqTtdTew4ke7rPDxIR5_Zx3w3WP2wdEPUJfLySOLaVqMDw0m89jqxJOHI7TaoqhwhTHlr8OPfTjdy6UdXVTbzFLyXmFcQUth7Tc3-8Tz1rBzmiLWz6Ck3M0RFV9nqP2ESCpHD0VEdMo_pC2vknB3KQE5pR1MtAivlWH7uPdxXP-WyC789PScWS-XciCSxciY1sQ9JKNgYxCoE1g4rqq_azvkY5mkmwKQWGumbA_YvilayS-OH6EBWNIqCJ0kekow0cWeOMTp-qWKwHXZXWVfkGUls4YWtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBXBwikY8F8OVXqU4rLmqPqrnmJwUubtww2_0O_mWFiwiuSV2UoY0Re_i68F2k9AxKZZFgBEDgCrwY-NrpxnvKrAy_2uLYcBnNQcxGaubs-8pLbpMiCeeMyXp3pWcGnVmU0T7R66Syelnk2nf4mO-FLJr_7fCgVXP_RD7qp-fj_ZykromteMogS_yvCXIdSrhHZ3vvYKFBxsW5bLRGxEQ5yYgKbnUAMcpV278OUCDxLXnF_1OQFHGZUI5xJz999JGiYU8bDoaCFxxXs6_iqgI8wJB4H_PgQiP5evI3NUhG-W-X7VV0evmyyz3XHj3-93T5rEuBrFu9c771MaA6v_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TutRP_CyTrbkNcs9Mc3kIArs28wo9YdSke93Cwf0BG1oycwFgt7jAmBJRb3d18Lgcfa2II4BeuPnXKxR-SK_32Z2b7Vz_zlchANdzWTp-vzeUWDymk9S4l86vZg2WfXzYhIwNaB079oLMal_d17S-ze7OB1goYuYi9ShzgnlHEL_Me6RKrvWAx25S-gSBM5xD4_rA-tDEpkNfy7Mw4bcJWmSVpIP8620lriXLhBguHwhn3c4LJmwU4xl17mxyLHHxtTcHYchPSKj1UzgHr7EaHkipvb2EYaN-kTEdLbg9qQBkFc_peqYs55Cy_ughGbZK-KUNsJ_YnEB6S3Ksoi_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WshPJtK6HBvXfHcUZCl3gbgtDbyf3WVEU5ANnMaOlP9civgbfgGV6NPzP4TT2qvSBgtAkLzywWiMNk5uHGMG-vY01BfSsJWCKzVD9pR8d_v5d8u4q-vONLLN7qpVnL0iG7-QsN6Fa_zprVb_cBRycFcIhZpLPz9I1JzWv0RS4m1CBeq0OUlkZmddLvo25_P9o2cuNoYQk5IwO2_owUJ2PvqMLGYTNmVdVenOQE3UbwDxQfjr0yPodDd78QBZ3Smiw8u7xoOpVcH4hllHISE7ENUWPN3WIzG-jg95CY3Lk5UOWMt0dNR3wzB-Tb1g6UaAGvHTlWwFd53YHXcL2qWwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL38OpLSLtemjKupq8XiD86oB84rx7-yAG9CMy1DIgERkBzEmJ3yGJrPOaLm5Csxa6ag2MbyTsIhCyzDCrpe0Rg2BaN_oa_GhpVw_zcRlaVeA8eYg4t94u5TS8KQO6qXq136Zo2ONFahgo0BgkbYjGeoaYpyTstdmW80gF5swGkPq1BNntAOpbKdOwQhxcw1P4uoGd6uYIRVXZ60Q6IfkJOpMrcw3qrnx6KeP_nZ3ifWaiQm6savJUdUbeIhqwtiHZSeuuua8okoH0njC_J7roIufVGZ3juVfGcAf37Ehmj3ZvLnx75FqgetvBTv9fHbIqaCgLlDu85D5WbWlx19BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEe92U-UCztfvgtK3IZmXw4LKJTmyV4w4UJa6geTX3youFzLAu_fiCHdLI2_sH0rOQGdceMuPNv6oE8tIK6-IpzjwVm97L9AS_Cbg9Yf_XsvuXWCVoG0ep1x5yqVDvNhKVlGECVxu6l43PbPMHT4bV5mF8KwyYSA08QXMZCUEUR0CyRm2mJBCtsAFdRi4MmpfMGdJ0Lx4-LzgF6txnQ5NkHCRqGqk1EarkCWHLZdXO7b6p55T9Iwvox4wbXk0cBlo9JMtVFqpPKPMcdt2ON7gZXCA1KgFzbL45mTyzmMZvej4XCbQUBhoPve_QGu1F3nZ25eFZnvQ8vlNDafE2LO9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz_4q4nanarfgyeKT8bOc0CB016A0JD3UcZnQD6tSq3JKyjiCzs2Cn_KuDQ2WcCJzgYA8-q94W9aqfvvvsn8TbSwJvB8VmgejKFaAXTBrL1ya-R2Bbv2pvrIzEKAxxiDNmAAmQr8fvsUJr5nMkRWMKJX23vjfkqlnXYPWhBL7otR-tNaBpSluPW7q6KWhn4rLhn3Cg3VYoFxKRwiRAJvtRajrW1D7lP4n1Y1ZD1YCGO8DudzokUdXGLR0yLRhyr5hmmbEBSAopZjC5X5jckamEhSPifGi7oaC8_t3DXMgoFyyyhSgQM8O58QS8kh0P8QLDf948eC69OxdkNxs6wZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoPKDVY5K6EVPfozGP2Ul1xNzR6ESAxc9BUPIVHQm1EpeIlDH8qzSGw99uu_XAvne5BHSf2xlsKrqker8SLlGT3DeMLHc4dSam9eBexBDt1oKuc5OjLotJ6lvDcU8kd0yufjgY8l7qTmad0gCAXuU42Oszbgr7FwElju4dj5JXucf00FDVLSPENNQhImkY2qkhvs3hpHwInvlheMdldedoGHrOtAiwqzPeA_s3mDQ6hCzIngFUOStgCC06eJl7PY2z13BJswuy0mBo2Zxa24nOy43hUxBvU3wyt6CBV2r3dHeYRoRz7B00SLXZk8knqED0thcPV6m3kJ_J9MRhBZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2LfDsyt84_9b5JkOV6tN-4ZBR_OylRs1-wqx-1jnEc4_XABBq0HmiHaSFb2lT2iskyhUh7mw2bgcWZFLpq1P4AHFiJ1tcHaXvoArBHan76s_uR5iPkEtpRl3-cl5OLenXtaBzwZ1dw2wDj613VymeN0FzBasDdTIpFtaJr89kU_z0hMhtFyCWew2vrykilU9j3sZMS1Us9LPGKDL8XKRJRsx34Xtd-drPYPKF2kE1Q0YOtFdHewU6djo3QZbF-AsGM1CMX3dWxOdLJsmgb6ZfmHU_DKUGTzDGWiAttNMK1lSnKkrJw38haMsy7xhv4nPC8ixRyoaHsF0iyYUJ2YGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqOLjOKBLgFQOORkvDGx-co9h_X-cek-Lu_MuSITFOQWZu3-zKeLa6AAoOK68ohROJr9V0kY3t1Y6FsHI7qAXteLUGq5L9zLRMSBaXD76leWejGh9z33vLrlPppF1_WJl6JucTkyZr74X-hjdr1-A_WFeFQ3Lci5zTUu8nhYyypr2tvjmy7P6c9Uow77Jxkqqes16uKTZN_7DP07FGMB4z5U8nNIuHURI0pwf7zUpGo6reeTs8lYjbT5cpjzQRncJjemflN-vEl25tt1LWcfLlLM9R7vyUEQzC19ksS1zsYlYj8Il6E0CYZ8sZEQKgpR2epJYClx2-MTi5UqgbubaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9yqARTu8URH_mKaodWQj14iqGWorue-3ipabo0kgXKIhlQV4Krjmv7nhBSdpD63WkhaHZksi6Fbw6tERQOKItyG6V0gzJ-xClOAUuBCDYM1UEVlUsJ8gMMCbWMYO78cFScg1GZIMdRJQEKLCzMA928lZzEOHY9dvOAP1OWAlBXKI3aQ4RrE2LzKo_x6McvNbmlGJsU0wPiC8upzddRJBi4xCXr6HETek3LhDnbnIFa4pDcFvESijCaOJtAYPts4cibevPMn3jcj5YKEOWeSyH9mN-6KydcdhNCvAUYrcF4MDMKpwnx6hEw-TgGQdFFsJhftMAlAXftSro70yELRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBgoBAasX4ZnmtCZji-xICa9Xrp39kls6j2Ud0mWkgkH1MHpGKxX3XNNXQ8RWoNocyFI9m4aBX85qbkYTw63mr8jn_JMBVC9UMnVOCJVHvS0HLHknxnOStbM4YxKbMLKVXHs_ZwNJ8wwrT71cdnAz7mJ6p3-UlfG1kXCekPwOHGWKtLkWiIna1VtaKM1vqpmVvc3DOG3UKrOSruzliM6v7xshfYUn74ELZDnscdeEJ9IOA_6-OWQF1GHmxF3tu8LYBz8Bi6ZINxZV3GSCnQbyfHfIf-YjVe1-7Gez8PYiQefDPFjnpXMrE6zQEEj4nVMGtWKPqZA2Z4ns7eSurLjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUJ__K5mgFONPyBVB4LmavbjTkytITEwkxTumaRfuOM7nSIIwBqbnvQn2gPOVXkEJM3gvAvdnOuvxFPCBQkMIoP0jS0FF8xrLOFjjp-4bWYNM-UtPXPcZqFFtN6hSq-yjPkLc65fuixgTsGMTLUL6eyoNmt9mNEq4wNs7TlAyb6s6LujnDultakSOQtKkF5UFk7AkJ7CTzqWXWViKFxbe4EBnPlnhsbmPfb2N5TLUtQjmbr3oPPZsdwVLBKtaFM4wFZoQnIGj8_chkITZcw1oIOD2rz1H0y-PH0n7xo8MTGA9jTStk5vYZ4-L8v2F-Vkj85-YJ0ZQ2CevN0ktZriPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3rgTPRIH8w3SiFXOxGAvXShu_WaX-eGjmdnJn9bj-I9tF-DO8Wo0yQMlqaCuu8-R2v-NKGWH4EVzbTrc2rAM22UaECKwJnLquaPPqoXpoAdzvxLZ9d1lKPJq0Tnm_Iv5lBYKns7ffqHC2LWn4krsZsprsz1qLxVPzGdI48SuPuIkdHWJ3n62lOQEZk1M_YIINa9bvNKKEbO5DiDdoy0sTcyhtIH-L3Lonq2hk3VtBZW8ESX8rL1uJ7oQQgD6xm7YksKiLvMXxyS3B-NFQ69PbA4dpeC8JiGtBJIZTT4o1Hr9MjXHvsGRbQPX31uMtBTJlPQsM_dckhUbc1ilD3PRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVwLsvYeFtQjqkhV01HqtTSHM2O1NfrSGZh5fx_mE2sCOh7J2ScZr0GHEnsiVcps2FBuN2W57HCW-zbIqUpM4yC-qhXGl0mG8J6vIM15dgKNHwQHpOl1tsq9hBeKil6vgjzO0xIBYBOskhhFLpnwAu9o6j9epxhWeFC_xU03yCM89CJ8ceAXYOkNtK7ehymX2P1wVuCU0UTLV9uqgZtlQtbNe9R0kW-FBClkGN-yBigzdeYR06WDQ4zSnHC7342TVEFDho96kEG1dn6BQ8QYDJ47WN_rPAx4kBsC02FNw8ho-maavJfwq90mysGXqiMTW8QosJwUCtV9kipJB9J72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnaplLufUsm17UMolH6KqIeWXGWsUON7pB8oJOyFJiYYjV2qPN1jF4LMQq0jc3MTXy_MTm0ihob80h_9Q9KvHV_aI3T6hW20_7CpbEkChcYnytX_05_FUMOyo07qg2IBc1op0lXTNxLbze2D5Kf8RQXemmU2DPDfXtzFgWkQdPns9oKGwoBH1lJ1uwZFd2MWTxO70WNZLeh-M38KSfMGJs4AKnARBI2Q2dxozyx4DpSm0xRHVS59fpBPjpHAyIY4Yl8dxPVLar2j-n1G1XVaSyeY4_cWEFgDgRmJsn6tTANFo9sHbEdfMrtD3MyPDtpIn5gVD5p-y8OPmwlyTpNnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyjmANjhOR4jLFNNfL2nu6n9t1QblmkRK4tCdboCSYBFe9KrwrV57rc3LH2yMNhr01dw7Yt_cLyOxEhtJQgzD6LJxeHia0L1MkGHAgb_IgxSl42o2vm2Dacw0AXvcnD7q7RBfAvmoQ5pxsIzrWP8PVXaQ5K-G7Z4T4CHpofdOj6wNGtC56-0MDydbegu0IupMNxI3QGgAc6u_A0itNGTLYAcnCfXDItAc2iL-WH3XWCphO4nB6AvgpbVUvoHJvIgFWDGATJdB486k5VgtgtqmvUEnfNs4DfwuHPAOTMk0vliY0pgpH_NlwnS6CiXlC70hVkhhkSmDXdbkG18F3vD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIa1bRED0Ejhhdu-blVyTA4So4W_ALZfbY9_X9RkhNzU8Mkwq0-0klhc3db6Stb963res_79Ste_IHB55YloinJzjmxEMomwtuB2DkvKUaldiX6xkoxzYnDvIiT5BEM7I37mGirFAvSTfjAU086m_JiYx_Rxa6Scy9XPWKAVpeRFl8tpF081SRU-ZR19eLu2du4Xjfh7atUxP7zMIxALkYlOCLihV6p8K6_SfaxxZF8HZuhEvZaGFgS2xYyp8ALs7FfPDVHETEpj9Payy7Gk9DCCkUC2iDJLR3r_FkzH5VG-_RixPpY3RKyYw4PKQWVjD9BfjHiXukIPxdB5Tz_09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEMn0Ybdd-Pb6fEPjgkeAC9a1wUW0vvUh3ZUcI3FO4UZ10gIjgJ2NoITIJF3m7kjXOWlI8ogMWHw7TkF-rpm4R-4z4oav5BXmFbCmjFXPxqsNRUD_ATp66uCeWQqANFD2avDR5xw2Pq5Q2_rkRZoiCV5r7dqnTxAuX98BmL4xQPQ2Otw6DMVM6fmp7YGUfUYLF4e72M_MbOri8uhKlKs89K5NeQJ1H-598I7JOc7GrjG-f5ED7TCDfPnYhBJTkJY91gjokQN3wsgsVoJJjyWYcfR39Odf9wXvjHMx5SnU-2xrtFmyOhmAR_d8unx26WRx7q2qna9JVJA5YrQAQ9wNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM7DZrc4ksGUdlAjVtIVL5AK-9dvEcFpKxcXnR7LueX4EOD474iuJDXUrbPOgX2TXF6TarIyxF6Yi_j4xtfemBJEBmr982JCJ1dKx4YRdj-k3Uhm6LrLYP7lAr7_PeWgAFAaFyB7Y0M6z9U3oySk0Y_jDH2GF8qod0dAEvsBcfY8Ek3WBgD4m7UheT_s75_tDT0Q5Ih7_PusYegMpWkWcELP0_4WgtPlFm4wrVub2NeM1mI-9GPyo3_slYwSahsHielUAq-xnQOedOCVihvn3CRDwq8zRCIGJ13LMW8-j42oKHUD7LzP0Qz_G098nGhEA8Z5yIzz_KueAaXQg0Z2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er15554HV0oDCPAd51i4Y6jqNB0erDLvdnlf0Bw51PpjSvKiKTN_95j1LK7d5V51EjU5VCjGAvNPu4_5Am6Dc-yqxFNJw1Tx57EcU-g3t5qLCzwTERBbFTQvC0_y6ETmISMQqkVXyw5ysbAH-Ki0p9XZL2qPwqLl0k874ctASSuyGVI7j-jATuBhdOMaSWU0X1myXPkhL0fCfHOTFfi9bfdlJwDmtDq1lm9SkKZ1qlf_myoyPxGavXBj7E9UhJLcC7Yg56Ox4gzhR7yjjdOu-KuK6qrsJu26E49k7GQIxSKoPo_IMaj3xmgbjbLwZn7Ok21ElDpoPp30Q1qF1q7PPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aF2ik_9gsVBidVgmPQ59oOFQIs8H5GDur3tuwgkUG7JukFyBYlWdY6oUNs6hVt9m-euu17jl4jVUbqFSuT_mCsiqpCHcte29vV-eKDu2SWhlW7H3h6j6E8_VqC5kdWo_E7VblFQtrqeINXlMfl9Ycg1agkjX5vxWkNorgT1VvmMfOKoHzS3adhvx9fTr23vah62uLkihYNEkx1xHQ7kMF7HhcVvnT3E_YE3JYhhLT7fIVvyQMuJgvW9GAo-9E2Lveedw5AAmSigsbQLUJozV1KLtFtj9qFB1QZE9xCc6pXH0TCuzxHQ3We7v0MaphyR7cVuYgxCMhqp7uNCzxeSYLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffNp3iaws9mi9dm6ZD6vYhlOFYSMU0_B7UOSdrAKb0KOx0JEO5Oub_tLtWo_ane2kDjoSSAZf-QU7kFOFgCAcKhgBqBKZNHyLBzXuLm4h88GH0YbaRTgu0oMkjaUDpRpjSqEdHtYrN0bCU6zl0ifqP5DUMfeRAgQymmxCjS8UWfapUs1-jB2S0UaiF5DtYtFwb1ZJBe4KTppFA7h46SLFkTPuupAqBtG61qgaLTEwoe8FHnzFpuMje6EWPkxT6GzCfnQLmELTAK8f00IP_wyizTawhMwFfWFTxBlYRBTyazHuVGJGYydk37YYPNa99VUGJ2sHmJ2MEUTSQq3K2GAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBSaz_Gmj3TDEzGzOxycJb9n_2I39YgMldiM9XYYdxuyBkUMOLw1heEFFDlCkNNVWcVIB-Mk2JTKH_t2fypI-nC07pk1VbEgX9ubMCMNy7kq6dVvHufD98lxH_M8sVJ4aRKiuIHyMeiWT41OoO-nS78hRwOQmmN5IICWEuIybseZdsgbrSldrl8RpbKMUQc12j0amHTFOhaetHf-ysFeMQXSXVzkrrBmkMmTn_K_pVWOw9XRspF9LWuf35_bW5UwMUR9B_8BhokxsbN95Lzjk5LXkmdVHUXP1yHUSQbsomu3OjUKsZYzdYNTlcEJSo5Ju9WNF9DELpVm4sSBYklm2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERnEUYREOyY_-i2RJ0d2i9-bixH_TouENjGxwePcTmurcCH7-ZOZKCL-dErDtYT-jZaXSIYbyTjg-GhQku7TS4T5k0BtirZp2NVQ7oc4PblA6GyzrbRrgHyo26WZaZYTeW_e5Mcu6WCz7Z0qtEQrwgDcVNS8suluTFZIu_61-9i6efRhImutJgTlNy8EBMmO9SDvaPFqxxAMH1THHoahvyc39RAmwOEDi9YQpnKmM_wyOjEcFvAcg7UKzmlaiuaF26Tij2avV15voSFfJI6va7W7gvtlKdbiqcEdVeJr4ExuaZMuS5M1aCyqpQZnmXA8kO0GRtTbqLf5uQ--p0rfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gunGrwOUOrrHnPZjZgxIlbWFUFWAQ7F357o4KOTAGKyyzvNFQ2n21E2qaQpFW4pmNt9HMRmGiS4eqbxSSthIl35SMsYLrbuujdkA6imk0xNG6Z5PikhOlnI1RNCVMGV2RklEAykJSNV9bp4ddXJ9RWoknn19W3lzEce68VCfIvCea9OHmInN-lS8c5GUCWWBX_Ob4UYMQWsCamKh67ZCqRTdLIjVcF_lJsnMPG3qb-8h-JruR1ebhVfxYGMEIp1798YTc7I0uqP9Z9ih1RjyibbZKPySXAiIIVzYAFNOoB6DTU1MKs8PyEX7h98VJG5rhEb5KSTrUaYQlb2qc9BEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=AxgMKDZqcmzpsg825Lxyb5h17Z4onYCuOAjz2nccGT5rVUCiBCm0g8eHEMaxZGp0KFaWbn4_YvDweVsc0FeaUOr45ekgQZGpmQm_Mn57YZDLRRP_6fvbdpiiS-vk-U72qizySsAA1WnCBZiCYOmkgFDUrRAqErAp9t-zK0-PMTA9sBugtJ_fm5DFWbPWqlRK-FJojTkj3v87BZP6aWVaWMZXEgFhe5deCFFoCe81Jtal0RGsct2X4Kqqui9kzKi3wccsvCeQJfXlywVI_BCRYHLL5z5BPv09Hcsrm_wFN-NeoKmF-M9VB9ur_AWOJbxfJsqKVNpLG5Y4gDAnQka4MjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=AxgMKDZqcmzpsg825Lxyb5h17Z4onYCuOAjz2nccGT5rVUCiBCm0g8eHEMaxZGp0KFaWbn4_YvDweVsc0FeaUOr45ekgQZGpmQm_Mn57YZDLRRP_6fvbdpiiS-vk-U72qizySsAA1WnCBZiCYOmkgFDUrRAqErAp9t-zK0-PMTA9sBugtJ_fm5DFWbPWqlRK-FJojTkj3v87BZP6aWVaWMZXEgFhe5deCFFoCe81Jtal0RGsct2X4Kqqui9kzKi3wccsvCeQJfXlywVI_BCRYHLL5z5BPv09Hcsrm_wFN-NeoKmF-M9VB9ur_AWOJbxfJsqKVNpLG5Y4gDAnQka4MjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qx1Bfsx-7mfjNcZFlSb4vGHawjS6qHY4W9taeurbXFTEInuUAQM9wydRVUMvw1uN9ihhqvGdudvXzyXJUiuieuT7i_zMye4FxaGL-oQ9rD8kaKgO3YiDUmQSC3vWfeF8Ar4k0omYFwPdrtcgmPtI2CEPZ1PyY0s5yESL9znsgPpNJJdLUq28ru_MkAvKQWUxuPSudH8LzN54hiR-5w_NR-Jk3Jd7fU4_MK_vawXP28hPZipaB6FX0cAec-j6jaGIPtDenXdhXxE_NEZ9w1MAyH8tfXiLxBcXbt6RU29xzY3tV8wAe2Q3fSwhMbYMtdu86msHrIna-jJjMAq-TmnhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=p9FC6EpXHWAU_rKRoEAa6oktqzIr1HSEjK4Ei7JYu_Bbsh1XcS9tyE4U2zRRV4AxBFmiJkEwhdJE-OiMKSam7F0wjMvYdcwaHcrUZMbnKc8vd-xc4grGsucFc4GEgmgTyOgGIu2Id2Xw0kOSTynWIBNwDH8iGuysdfE_2da5xVS1_IN099D0L_dHi4u1tj92VG5FYUWQn8o3nBnovXyHoDPkuHuhB1hwOKRz1dXUgAF4k_8BDuMm4A7wG6l3FPNWbh15SSZNwJrAlsf_xwujtK5jKqzOi3s6KxEiUGEEmOT-cWESJ6wPDbYPmjcsdDT1kPaDDJ51e4JGYVqw9m3J8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=p9FC6EpXHWAU_rKRoEAa6oktqzIr1HSEjK4Ei7JYu_Bbsh1XcS9tyE4U2zRRV4AxBFmiJkEwhdJE-OiMKSam7F0wjMvYdcwaHcrUZMbnKc8vd-xc4grGsucFc4GEgmgTyOgGIu2Id2Xw0kOSTynWIBNwDH8iGuysdfE_2da5xVS1_IN099D0L_dHi4u1tj92VG5FYUWQn8o3nBnovXyHoDPkuHuhB1hwOKRz1dXUgAF4k_8BDuMm4A7wG6l3FPNWbh15SSZNwJrAlsf_xwujtK5jKqzOi3s6KxEiUGEEmOT-cWESJ6wPDbYPmjcsdDT1kPaDDJ51e4JGYVqw9m3J8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA1aemxblr6NiOCenw1ihJk4Vj4IElI717nUgh2dxE1OLfkQ3BfhOn8_M6-qT1YWW_JFkk3X50QdJPo5YT9HA0sOkklttQ2L8IeloPVdleTVus9p2CYVuPssEP0DBmZ7mlJYIUbuJmsp4NPAra-o4GtwNDkLUEwkpwxNquD-_D7Rn5-iWK2ynx1FS-pN6dCpKqrLG2bCztOxgurayzC8FgKcWZw7M-djMVP818RSjysNRd-d3pYTPBjvLdUUCv9MLgI6FkR8BDEogsEVZ373Zksr0KnDJTovOjbDJXBSOOIaQ7d0LzMSgAgHwkvBvzpdXQFy7S5knU2Uj9s26Lchfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYB6XwEYg3d4OqD4rARCefWMHouGzrzSv3kjKJdHucT4KYhNs3BMzc8LTfftQ3Mhg4ivdVGLztZGLQGSo8bT-FEXCyNQrekaQeTkwumrLuogyTXHvbe2uHkmqP3Vu5FWOSPJJVA-n_vvodwHtnbenHdI1coZ-KyKXHWbeq5NpzErdtU9i4CJUMdxlbLv7lk4VRXZkDPSMh_00YHol34sWnWQy88OnMsWauYZ-tBp4XdEY_XlSw38KcLK_UVSrsYaaoMFvKGxyrkdTb-zsv3VuMT6GtjKjkvpA7u6i_7W2Eui5dPsg2mrdw0NfIxGIZVdM5x7T2w-YHILXDNpnp-klA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=c9Xa2SihKL37CTz-d65sNmOGeSlRp_6C5BJ93_0Rn0XUYPkme3-TWhNBWxJaOfD0kiYM7aahRvSNHMrNPmM5trwov_yjDfJXb4hcceqZ5apIhIBZ1bqzMTuy2LdL0EtYOuRH_OYeVZRzm1IWkvBfRKCc934cKJfWe0QURkxrEt7BvSq-PNCeEdDFs4VaLKz0xH4xXCwBSA6WHTU1-cgYrqCxsW1_0xz7nSZd639nqZ61VVtUacL7H_h364Yx4i05Eg-1VI6oPxk54qhXlerk_w1bSaZZV4YNRmujAjo3qvzqfzyWXlGVe53agShLQqgS3Ye3YFsM1sABZUmnv0i70Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=c9Xa2SihKL37CTz-d65sNmOGeSlRp_6C5BJ93_0Rn0XUYPkme3-TWhNBWxJaOfD0kiYM7aahRvSNHMrNPmM5trwov_yjDfJXb4hcceqZ5apIhIBZ1bqzMTuy2LdL0EtYOuRH_OYeVZRzm1IWkvBfRKCc934cKJfWe0QURkxrEt7BvSq-PNCeEdDFs4VaLKz0xH4xXCwBSA6WHTU1-cgYrqCxsW1_0xz7nSZd639nqZ61VVtUacL7H_h364Yx4i05Eg-1VI6oPxk54qhXlerk_w1bSaZZV4YNRmujAjo3qvzqfzyWXlGVe53agShLQqgS3Ye3YFsM1sABZUmnv0i70Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjNxaArijOz3H5hFHNnlk1oxky5qG6_WeN3n8x8NB2LB6PHuDhPnEJ5jR_jkBy7xBqo-H8A4xAQcDQtHZB4stQBC6iQePSxQ47HNKA5C5FLQrItpYfLVrZ2dUnrNYsrCiAFzQDsg52JTJ9xr_N66zb3sw0P05w6ifZWtWRKBWzUxIUudC8YQxU1LNwTm8xLVZ5RmSXrPa0E2bmQEXE7ZO8JLFChJIAl_v21YGc-SSYjS3Hy6Mhx9Ssw7o0Ss06bihBhxkmpnPD4xtIV4XrcVLlzEYmZi7H04k8MEGNe6FBovMKnXK-B1OQ34z2cR0XfE1P9jPnTMMZ04Fb2FtCyZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwG94PZxRO1NZVtilbSIECjLDSkWVpl3g32gC6ettWu_jzLKw7Wok25f9BKrgPdsdyT_heZneprdKW6ebASDXsWViOJAg8HxAM5fMpSdY1rkCORSybXxczWsXkdfPqKFbTtklgoKl6pDmxzFKJb2yBD8dr7tdv2fkdLjIby_nSMmyQzWE0s4retfZQN2uw0--gemzY8i3u6wf3_BQsS_vNFhDZxpHD77ZLHPsRhc8EhCVWkRr8KyVnBtbIEpEgCYIBL3-01Z6iptddKa4F4LE7X642vkuwe3nY13cFyY_FjcFdQnYVmJbQu0Qro3w2mqerzmiJ_xZd3Z79itCHkuRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTX2fj-5mgkpvLPfQPaU-imYbQLo4k5bTKtYx82801Iv3dHUaWW-UPiqR6WH9RZNS4EPC7ROrIqHXkOZDeYX1aI_rNyt0vEikyrZ5BKC86Opsm2xIg7TRBMzEUr-hC82AFC0DDOnNkCJ2bhqDBnYER4aT-u75DHxoPqtVKM9MlhvmVM5GyPnGxUyOxpruEtrCSzTsMmzvEIWkgKf4wtHFmOp_zXFQ8ROHbYEznxGj4PbTrzKk8wTl49GSlF10QpjjHUYTiojfZlseCUwVqGulS9rWobxwTyA2Ig1U67F1Q45SafZ51DUP49AewZLNsfZdYO_Qp-xYlx3gVF10pcYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=VpVH87UWceNUdlWMQ7ycpgl7kf9-bR9ONEZDNxvj0BnhZYRSfZwyjVIpgNIouB3OsvFKWfQwRQ2-DahmjDOVcK1eO0WB7YGE8nAXALf4kSHKF842hAlgQyYIsAb8OzStTCHuHXNz4GEMvCkujzbq8hNsiHN9zTSu-h9PSczfGPCbh80Iv7LMmGWfQLvDsVOkHmWx-ANFC8dOaTjTlFEMD5RCa0SOQ54vJ08uwrz8CurfwcBLEHLljYKOuJIwhcFDPU_1fw0bK_0qQ-yX2i0lt-BogUHZmmB8-ZwwCGYZqlJI6vVkCkIWA6zZ4VGL5SlxcI1upmMgVkh8oFIqiTLDKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=VpVH87UWceNUdlWMQ7ycpgl7kf9-bR9ONEZDNxvj0BnhZYRSfZwyjVIpgNIouB3OsvFKWfQwRQ2-DahmjDOVcK1eO0WB7YGE8nAXALf4kSHKF842hAlgQyYIsAb8OzStTCHuHXNz4GEMvCkujzbq8hNsiHN9zTSu-h9PSczfGPCbh80Iv7LMmGWfQLvDsVOkHmWx-ANFC8dOaTjTlFEMD5RCa0SOQ54vJ08uwrz8CurfwcBLEHLljYKOuJIwhcFDPU_1fw0bK_0qQ-yX2i0lt-BogUHZmmB8-ZwwCGYZqlJI6vVkCkIWA6zZ4VGL5SlxcI1upmMgVkh8oFIqiTLDKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=RRdMqpXbwF9eTMgjeQq4lDPr7ooV3POs15iMHFyULaT3NlFyruKps1efk5jTwplQvFIU8csITFRYUVmPDYxMeUg7UlW6pLl_nLA8J44M64RSP2i-yvXZQTyxe9KYpO9ITm-q3jF4XzHHJJehWf0-5tSvlxqZk5bvXs0x8x1Tlfvvx_7KZfCy4kkbDRou8PoW2OFW8J5xsDL-FO8y5VlZ_y9pL1-2WnQHDUY8j7CW6_n-Svy10bEktNjC4EmXHT3c9yoSkWB0Z9YeFA08csmEqCTs_F0ARszHOiee0QGv2_6KrICK-E2nf7ikt1fKhQhjZRqtz5b30ZdJKKehyD1HVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=RRdMqpXbwF9eTMgjeQq4lDPr7ooV3POs15iMHFyULaT3NlFyruKps1efk5jTwplQvFIU8csITFRYUVmPDYxMeUg7UlW6pLl_nLA8J44M64RSP2i-yvXZQTyxe9KYpO9ITm-q3jF4XzHHJJehWf0-5tSvlxqZk5bvXs0x8x1Tlfvvx_7KZfCy4kkbDRou8PoW2OFW8J5xsDL-FO8y5VlZ_y9pL1-2WnQHDUY8j7CW6_n-Svy10bEktNjC4EmXHT3c9yoSkWB0Z9YeFA08csmEqCTs_F0ARszHOiee0QGv2_6KrICK-E2nf7ikt1fKhQhjZRqtz5b30ZdJKKehyD1HVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR9UdytV2y-WwanNzudyOsUiHol2JU7rQSBCAM6q1om7Ku71J4ZskPC7ioC8f7dL6HoGEbFx7dl6zmM9J6HTUy1CbFYHsHtGaUEeRIMfwU0sWnZ-t0nhRdRaob1VXHwUaMSuAFIxsrlZnpBQW59udlp_0x6YzWF6GSpzoWqZhtJh9lhjRcFGb04tvgdiGDvEQ1wq9R40K_MCn9ro8KRQBaZbOiZmezilYH1t6c3EoJAinz7dt1PjtSVGedhSi6w_Tp6TP9690fbrsV8qRhPl7bVJJ9Bl0BsAt_O-hPOFQZTrKDba5hgVSI0TJBNjzMApmRpohSPJEahmKlcX4nQtzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=r7udUEGzjMKtWuTc13RbmRRP3Ybwi-E96aTy7dyGhPxxXAheorLIFUYMfTQxFbuYii9Yys6GDF_Xs77gO_lDH-R18vHP-3uay0APRdBGRlbja-3OeJDNxeGpWRDp-Gl3ZcQD5Ur9zZdyFaM9wcX43mT2rUXRCCKUTIQnnR3FGrhCeDmMpoyILiPNluEfyqZjYUWTs7BrHKdRfyRNcifc4s_jZQtdpQpWYisNSz26MtEILTHrd35mtJKhfruJ8C6ArDRPafzS_pKksQBQ__NnFaYR8ZGG8cfvjAJXzY_vQ0ICiZaO9GlP7ArR93CTMCSi343uFlIt-d6kgW3bNuctmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=r7udUEGzjMKtWuTc13RbmRRP3Ybwi-E96aTy7dyGhPxxXAheorLIFUYMfTQxFbuYii9Yys6GDF_Xs77gO_lDH-R18vHP-3uay0APRdBGRlbja-3OeJDNxeGpWRDp-Gl3ZcQD5Ur9zZdyFaM9wcX43mT2rUXRCCKUTIQnnR3FGrhCeDmMpoyILiPNluEfyqZjYUWTs7BrHKdRfyRNcifc4s_jZQtdpQpWYisNSz26MtEILTHrd35mtJKhfruJ8C6ArDRPafzS_pKksQBQ__NnFaYR8ZGG8cfvjAJXzY_vQ0ICiZaO9GlP7ArR93CTMCSi343uFlIt-d6kgW3bNuctmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNIb-sH8XaKEkDWUga0yaT76lJpi2CwChBGXGNiEh49RKjVIy2NwjyMu0nZuJTeHwnkZgUmUCY0oDuOMIDbBJPENpopy5RCaHostTzK5oolZNI42AHLHEyoVl7C3u9P1fGOMQfeIkbIi4W2MFew--5bTlOlkNtpLEww-Kxgz4O2Cs-_Mx4njnX3wgoz1GT3a-6mg-Cyfcpr-BZDK5rQnrM5o3jEyV-ighXdECS8C2ibE_gdEl2lbKCpbHFqNOoS8y9C4RWDPBQiGluyOEvgf_ybrWhxpHHejwRU6anj3v0gqq8Y3YfOX0jRZz6MGKoLcSxoPhSoN759QAK1MXWNjZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COqVg8olMQL2RILpboTSsv4zBUExiSekf51R8R0FfgRKQMlcvJPTxrU1-SUnAB7cqBRTThvoig9w76mwKFkgwRDjpKyLXVRXBuxibsO2AIyTngWwsmV5R5v-6lzc9xPnZj5vJfpVlaYxybDpffZvSDyq220Ikp8-ad82p9IzCUVw7G8__2VOurMEVZDhpJXUYalWOgFIkhkijS6VovQv0amLneZHQbobIjTaGn-tBWvH0up5xH09_ST_9wHMPbMQKevj2pM76ql9i8_Q__n9CrZrviBljZwMGAFJB0LhrsyqJ5OLo7eeIKrV2ADg_XLp3ThZgqkUvDm7ws6dkc7s3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gigi2qnHNVKoyeXN7_ZN5pnNY-wvmywymcCLbyW51jADAZJ1DJoAffNrc3z_bhpKLFL0lYVdXPQYcUWBwibC4g82udO1Til3Ers4LS2FJMpy7Q-aigClWh7S2LDFWOvAxdahW6GMiKdT9oEKwAbu0AfdxOYpVGG0BE5K349aVlWsqMBjdzo9dMXOmGyzjonwWYkGF0BGC7yK8FxbkRHNyQ4w4y52MZAZjNSn3ZV3Vyyguin37pmGNe8Lmw_puotFly5O13tMVdGWcLrvcY1z2BYsUQLW2FuL9BiOU5tVwwnuGroPqt1hcGPqemFRAARmjRVDLkoxUdp36lGmPpqdvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbAfgVRmTDkdMP7VuOQY99shXKWl2obNIb_EN3gtmnxRHk2h4UR9bJCS6u4RcS4NBSFDvVD5a3pOFgOer1pPbKqbZWQJU1S2b7uZZ7NcLZAE_OJ4HPMN4DZJXQO5jKl9q2IKCoJ4iq3HDDQ14uCnA9H3IpVJfPzTYmoL4LFeFWfLjQ14ZTWqA6b0W7pV_FZggh-JIxyQX4DFZRhvIEttps40L6YtM_GUdukqFv0WB_TG9Zc9BeS9xvK7O45daEjpPJjwodHu5X_NoSmusiV02fxoBMvu6OcYBdFUwUkdX2lIlD2cnL0t3dJVmXJu1Ea-gB2EgdPxDn1KZtS069zMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3EhMJ0IQyjyFQ4fqf3GVYoVTncrwP6o6VKTDUA6-fZpGfe1JmFDXsfEj9BuVW-E4Gif4opiB6vuRcG6tCgMp3DMKzhBUYwQuKqIuPqj8JYbRVBLl8fHdWstaS-Db1v63SPjj6AAnafg7vRuNkF3Ky0uRiaaxNvnl6peK9QvuLL-TKKsHXwsTZIX2Ls5EUjEI1ZyKilDLNkBa2Zfoo6wLHD7q4lblZoazydtSHzb4h5nIM3FboUbsvf36-wB4mt2AAdlPYULNov2lyZYgBNayHsJOpQAMYPZ1hIiHV4d007iqx1i3wjWNg_uGlCwF2xpZ245EktBAymn05xLm4tThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=tFRrtgArneLMAm8enVTlGkvrvXOpzLsZNgCVd7ZM603XlYrWW-UESpOtFZrn-oMk4g1sKqggr8jdM1gSnZiZY3jm-Y4bwj0EZT2zavTtlijBgNcrKG9W6MPxJmM1fbzt6lOFKskuqcKFtku7C96KpHoKqaotMlcFCSNcMNTbwK7ssUwOFSnMAgJCZTNjpcn0WMxahLJb3Wr7H_RqZUDsq1UyjiOW3rvXw7mQkqjZx40eKFEorHDVmdTBvj8o7jz3UJyHWck8o_ijSu8V_Yqy0Hx4R_LQ0tjBRPc8ZxHU762IH8njWxi0jMkAcpm_R4Iif6_bXCZ_3-gkj1KgbBa6kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=tFRrtgArneLMAm8enVTlGkvrvXOpzLsZNgCVd7ZM603XlYrWW-UESpOtFZrn-oMk4g1sKqggr8jdM1gSnZiZY3jm-Y4bwj0EZT2zavTtlijBgNcrKG9W6MPxJmM1fbzt6lOFKskuqcKFtku7C96KpHoKqaotMlcFCSNcMNTbwK7ssUwOFSnMAgJCZTNjpcn0WMxahLJb3Wr7H_RqZUDsq1UyjiOW3rvXw7mQkqjZx40eKFEorHDVmdTBvj8o7jz3UJyHWck8o_ijSu8V_Yqy0Hx4R_LQ0tjBRPc8ZxHU762IH8njWxi0jMkAcpm_R4Iif6_bXCZ_3-gkj1KgbBa6kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=skKYE8fLQGaPFs4Uw61Z0ykvIlp3lOobhpPTd0c9aUJuWPVlHBwJdPnPS70xvqh9fsLt4XggmJD0q6tMoW_zdbYEvuoZPKSisZiglU_dqJW71c_G8ysvGvk9xa_bpYLAQLT0D_YBMLn6mfutLtxkuhy-iZZff7pEyl8pWiZ27Kq0CDC_ZpbzVvm650jz9C4FrhQGzXwiFocYf4r5IiaBZiu8BS0ek6e9FG-jlg_x-W9CsVB0YlNSRFDYr1JXeTJyVEGOtZZI1MH5colyX3WwYAPW-xdVZCIcCtO4EUdA-b4xPaAphJ26YJRNVZtUuIT3xM3Isoyp2hmjT1Z-wPsQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=skKYE8fLQGaPFs4Uw61Z0ykvIlp3lOobhpPTd0c9aUJuWPVlHBwJdPnPS70xvqh9fsLt4XggmJD0q6tMoW_zdbYEvuoZPKSisZiglU_dqJW71c_G8ysvGvk9xa_bpYLAQLT0D_YBMLn6mfutLtxkuhy-iZZff7pEyl8pWiZ27Kq0CDC_ZpbzVvm650jz9C4FrhQGzXwiFocYf4r5IiaBZiu8BS0ek6e9FG-jlg_x-W9CsVB0YlNSRFDYr1JXeTJyVEGOtZZI1MH5colyX3WwYAPW-xdVZCIcCtO4EUdA-b4xPaAphJ26YJRNVZtUuIT3xM3Isoyp2hmjT1Z-wPsQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZxMZjBALD3cXLaMuFD2zIb9i4IR5U11d_963joT-GJK3F1hNeEIOVlWW5Q6iiIEVPa6fpjeiGL3KdANqmsf8VgMi_CPXalm8ib9oyb2lLF-z8W-wwyhmh2bZt3gf6CAvHuuR8G7JfVy6K3J13cUNdAoT7hqShz3R8HrwdN_Wwg6klwiAjq0aeTVmSKVhI41AjBiI8RTHyeO1yP7xgg7ZBmls1_6oBAk9sdMcLQmeuTbwkaO3mMCo5K_4Jv8jWWemPSNDnwfYrZsK8MKsDZukIMhsFAdMPil1mJYiL0LDUdL8hiReWrSjMJa1t_vXEI4gAzVS6LX-e9tY5m4KdQ9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=lFr4o7UMUh28R7dAW9PFRk4aDLyrzPeBbTj5Oywh0YDo_b4FtNIxL4MxznDPwaDHa9lQtczA5YbZW4eOYJJ6bgTTmJLhsdJUtLP2i19_7Nj1HbzHyp3Q03vsrluydRBlEVKXhuDbSUmN9DMXCN824MQDA6XQoIv1zhPHrwHf9RbsQ5P-7LS7M_PzqFrC3KCH-4emA_tIaTAy3B1Vg8rjRv3HRjD4rNStt_gBObMZbHUCbKysDcpzVtz6-ZkXEfu-NgX0VucGttAV9dXJDtwJ3SjoQgXoZOYKI8q7FRbkQINtRofbDqDaOiXNmoynb8XThvRD9PWah9o1QtvC9sknKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=lFr4o7UMUh28R7dAW9PFRk4aDLyrzPeBbTj5Oywh0YDo_b4FtNIxL4MxznDPwaDHa9lQtczA5YbZW4eOYJJ6bgTTmJLhsdJUtLP2i19_7Nj1HbzHyp3Q03vsrluydRBlEVKXhuDbSUmN9DMXCN824MQDA6XQoIv1zhPHrwHf9RbsQ5P-7LS7M_PzqFrC3KCH-4emA_tIaTAy3B1Vg8rjRv3HRjD4rNStt_gBObMZbHUCbKysDcpzVtz6-ZkXEfu-NgX0VucGttAV9dXJDtwJ3SjoQgXoZOYKI8q7FRbkQINtRofbDqDaOiXNmoynb8XThvRD9PWah9o1QtvC9sknKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=WSTe67gqHb8fric7RnRAZTXut36_hRoh6hDyFr-KTkE5eHYLz-_IICuEY-VZy8yUQh-l9r5Au5FjT07ROo1QqhBNK6mkM2uQN8mzHvfErzxKY7E75S6yxKwmj9wDH2cBaQHvRcEmztOlkfadLms4FYRureRsNbLgTexyjkMhFwJldiparyZjp4SnmEJDsmbwr4ZoJx10UAcXBaTIomYjwBUzb2wphQfOTcVyaDmjmZvpN5K3z-ClAMZACV-Nox6_mn1lhVeAjTqc7MYpJJBGA-kufSSf3dFgBxJPT-5vdRuSpKL_JYrWG20d46GbeLS6WonHiaLuwek9s7YhgiDVIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=WSTe67gqHb8fric7RnRAZTXut36_hRoh6hDyFr-KTkE5eHYLz-_IICuEY-VZy8yUQh-l9r5Au5FjT07ROo1QqhBNK6mkM2uQN8mzHvfErzxKY7E75S6yxKwmj9wDH2cBaQHvRcEmztOlkfadLms4FYRureRsNbLgTexyjkMhFwJldiparyZjp4SnmEJDsmbwr4ZoJx10UAcXBaTIomYjwBUzb2wphQfOTcVyaDmjmZvpN5K3z-ClAMZACV-Nox6_mn1lhVeAjTqc7MYpJJBGA-kufSSf3dFgBxJPT-5vdRuSpKL_JYrWG20d46GbeLS6WonHiaLuwek9s7YhgiDVIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUL7Muh-qRKCsgGh6R3z2U7UvV_vI_XxCL-AmPt9sgi4wEBD-2qsEAP1Iz5m07EpDX1oFake1QyswjqkKd0-4PrDL0jjpKSfLfd1SNBc1JoN4-3bAsAelrN4GL_bgYO9b9FMjd7WR62qsUr2F13Gy9PEdeHNn_rf9tnnsYxJPLA1nvlP-YcoEAxBwXWfoF1pMLxxE1_XcWMJWmbzKGGMD7c8GLh-R42lBlJi-_znP68gU-4kgt07MV_2dWDwJqexXzyvjA4enebH3qvunprs8UOfzu5Ovgo0Ef0phrgHc3BmE5iXaf_kB7VYzoCHTnGVXFg4b-Q4RlwpZsQohLPrBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2k0Gp3_4f4jIL6BxVa7JqNcxfURTG5Y0lpGAuKqLnplz3-R4tEhwoCvnuRY_gi5XPfC4IVz5jzyOoPJwBYXrAitfplxtfFHBZgVYHrwmyt7FRX2AstUrQG6MXdrzsi_pdTybNqHiZ23UR7BEFkNBz1Icau3pQYx3NV6L-0uLVUExBYiOzfGPQ9Hk62WX1Kr2mJ-8tb980Ff-WiE1j2pcKEkSxL0gwBZXQrDl9LFfXAWTTytOuTh7OG_R1Ef8Ai54qHDGuNfASbzmbsc8V2TbeG_gu1uRCHVTt3bHxVNqWzALWsR__c3iLzY8e5VOH2zyG_MQ6CaQR-kq8euJfF2Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zn4-68cjZXTH_2cfg5NrJTukMwrGvviYZAjfU-g4E931AvruQnht_cZ2cKrOlV1RssosayYK0_1z4RwmiR5buKcCLRWr4OcUb1RxrPz7gbmLOG7WlHqUwdW3M-8GAijGjtI6n5D2vTZPEWvs49cEVt_VZk7oSymmIqf7ngLgomsp1_7_0z_brjXSXkV6uKf2HjBaQJIEhP120wQ9Hqr6Tu14tO2QxXg3LQMy8wNS19cJZ8G_8pUo0Y8VaHGpCZAsibWW0_rTihmfLcJ5g6ZmKNMdO6gzf7SzhRLW_29feJHx1Zsn7aTTXCusKNKvlS7uoZb26VDpzpLjlG53uX6fig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=cE28Vpz386snoqzKb3Crhv-cLuyQrYZ_hNrwkL10yEBlbHfcG7CWfIfsiMjXQttJXpt7FhUzh00ERmasckkIWfGxXLovj9VaUqYQfoB7Xq0kx5ZGLvTfH9vN2AeeLovLlr5T5ohymD8JbCR87avZ3y6MLekyzbP8o1s0fmcWf65Mcrmf_CQkVFPsoNNJ2VR3n-aYiPPm3pmeQbk9Yr0d1mMJBVf_4eAo1bwebC13D81i94Gzi_OUwDi9zcSi7gdMXJyOGoitx97AdFe9JnUD05_XAcYXPpdQ88_zhPNY7Huit0xhmboK1hTGpPFFA3zAUA29QFOMLB4TftuV52im5i7XNAcEsBe8vaIeUC__nmHv-kjCuiECt64ssCJi_6RZ7mPVEdJfcppVnjwrwCFwMxk2XpUffMH-zIC4I9Fpd3VMx8kYUcLQ8I0bXy2l7K3FcCbbmvoV8jKaIm_DEUn6fJVzptp98R4FdmnfOYH5s4T7rJBL4f-w1tHsX6hd0Jtau5kt3KX40mgh8qT5Bd_NYD6AneFuYyYl3DnBoodEoS8MjFz0-JRkiv7uocMc8c3R1DnoDQCKEhPE91YC0ebu9Xaf8BpQEqYwZKA3TCU8pT-4XKcG0_5RGZ8-O1LGAiY23Zi4hkpgTpIKfb88UAKLxdU6NVDvV1BLXfYEq56rUWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=cE28Vpz386snoqzKb3Crhv-cLuyQrYZ_hNrwkL10yEBlbHfcG7CWfIfsiMjXQttJXpt7FhUzh00ERmasckkIWfGxXLovj9VaUqYQfoB7Xq0kx5ZGLvTfH9vN2AeeLovLlr5T5ohymD8JbCR87avZ3y6MLekyzbP8o1s0fmcWf65Mcrmf_CQkVFPsoNNJ2VR3n-aYiPPm3pmeQbk9Yr0d1mMJBVf_4eAo1bwebC13D81i94Gzi_OUwDi9zcSi7gdMXJyOGoitx97AdFe9JnUD05_XAcYXPpdQ88_zhPNY7Huit0xhmboK1hTGpPFFA3zAUA29QFOMLB4TftuV52im5i7XNAcEsBe8vaIeUC__nmHv-kjCuiECt64ssCJi_6RZ7mPVEdJfcppVnjwrwCFwMxk2XpUffMH-zIC4I9Fpd3VMx8kYUcLQ8I0bXy2l7K3FcCbbmvoV8jKaIm_DEUn6fJVzptp98R4FdmnfOYH5s4T7rJBL4f-w1tHsX6hd0Jtau5kt3KX40mgh8qT5Bd_NYD6AneFuYyYl3DnBoodEoS8MjFz0-JRkiv7uocMc8c3R1DnoDQCKEhPE91YC0ebu9Xaf8BpQEqYwZKA3TCU8pT-4XKcG0_5RGZ8-O1LGAiY23Zi4hkpgTpIKfb88UAKLxdU6NVDvV1BLXfYEq56rUWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTwRcmDaCkHAJklkltV7Wfe8Aq8dvfmJ_7rDlN0OLgWyMJGQ6FXgQ-DkeVXACR50wSAnEIwwtHBXwoy6U_wDPALLVyz-Rp1O_WhPis7R7kiLs2vJzUsGVttpCHuEy6Bfs02MjY8PMNXP7CVJdVEg2VJla3lIfptNva_A7yGreu3855rGtYVh488UUFbwnoItOHeQJW1oKCOGaqQtyG4FxGxaoGpOBk41g6-Rx-Ah81Rwqp99vk3AgqoLCVF0m3U71Eq-TP6GQLFuWFYYOWBNWpw35BkPXEsY43jF6grcDbDgYVUKrvUJApnK9Q2Dr0MY2GbO6niJsyJSXvMGEXkQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
