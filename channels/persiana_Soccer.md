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
<img src="https://cdn4.telesco.pe/file/sY03fOO74UUqHjBwbIYUHnNakDRd_FWvEc3vMxQWpkj93fGTSGMN6vRgHYzTKCR5bZSoPIw45Dcr1iO9XknY9TmLARE62SAylc7G1tQgTTkjPsgZJ7TB9-DrkDfW8ULn3A5SsrC9cijMMOHJ8qRMiYSNOj5P0L58VX2KILWL99yM8BOqIBYqmea4WY-JnYIVUVUW8Pfsz8l1_Cgahn6nF4MRNM_eZu8GV4TvQoiCBs1cs8xGHvObU3hHGWzRDCu2HL421TSTJo16cNhU7Fl4esKuoKTM3yvphoHXKrqxsdmdsxf_H8CvYk_bkmnpMZq0D2t407-vBp2iYBMlr-pLdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 360K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 21:24:38</div>
<hr>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFO5eClSUwA3-Eyvjq4pK3-Jjlfrt_M6pHcuzVhBgHSPEESQI9f5FKRCafWZoHDXRuzD_RqbOlJIvLRWj8B5rT5BFB8q3k1YzKdOVTOeTuQfqQXbtM706x7Wa8lhRz9m2OvtkRFRKSH3JnZdo9vKjz5NVI6i9-pwuuhVHAn4XWefz5qHnWgcYMnjf1pZYTyrpT3YrIslzB4lh6a0F4Ok69LAe49q6VEUc2tOuRcRSSbOgOL38tTc44vlRKYYRv_NPjdJpptAoXWyZolLmvvad4KBS-MITBwdAEPLBkrMwoqion7PA3QlRS92oQ8ALi_5rzZaiyXaoOIPy_Qbq6eIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfPi4YxYvfEC9SrGLjRyrx06jCWgJTHrjoxHerPd20QLMFdJvAkgpqMpH6WXOiJ0uyONMzQsiZBid60AwyEsFRF6KZ_58c1Ba5BGeO5HBuM7mLV5Ase_W7QgyI2mEmTmznLDlcrxXupba43aRGjglyoOckgQabMswOQJUboucg8xV_VGGBb3INcAyUWkSzEkQQDjDM81zQcIdOI4D_QpQCC-a9Xusk9xcX1JHj7nA8luR2wM5dBwEop-d2hFGVrsjM7FVbDZ2XtIEr1eRtm0klKt3k-T0Wb3Ch8G5EpZi0U4fnlHWBODGn-LVeDbD4_r7CYcL2TDuc-6I3JM8ZfbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW3DUoUvCITgEOfWTmZHsMUvGRgSvZlOOwgxI37Hk2PaiGPjRoXH97MPQXfFekyxjD7UO2q-hhewAxinYRAf_5XeHkHgoxhYmwPanaKP1dox_mCQ709zt_nDQaPPwKzhSBjPDihTiDfGidn6ucsAXuTukfDBSulf9-D2e01-S9tICd2542imY1Xp4U2HUwdK22d09dcenrjS1oBVCP-Ya3MfYsO0eVWvxPIgvHzZaEfghwUhnKLEZrBBuYTbscuZxSXB8qV1J_c1uRLGVXYaW5AJrnVkX32eUkobH5TOC2SGfggTgLekU52r7yJO14eELZK3hjwZVhuNVDlcwA8VoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=XSHz6FjxGocusP3JX1b222ajkWyFQxa_PTy7T-a95xFWK2JuuyHe6ynV1I6VW6mByu_EHdjYYFfJrjPdJ-Gz0SlIqb1UQe5JWmnkIKard4tuv4gde9e9oH_3N_4TOFe82kt4ceXZSsX6FLIp1JgqISzrs1X0SPpy2wk4z2_NlREjkrPSYYCtwKksnYGGv_Kr9XwQn0SQWNmkBpr-owTbjhKr1RZbrGa071TTZq0JuV7W04k20fAjNoRrNr6EPv1NetzKfXCErdzD27XjbwP4CfUTq5BfQuSs5hlX0IwGAm0I3n5k7nu-uAnyNU07F3dOI4euMirXl85jG7GVa1vF1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=XSHz6FjxGocusP3JX1b222ajkWyFQxa_PTy7T-a95xFWK2JuuyHe6ynV1I6VW6mByu_EHdjYYFfJrjPdJ-Gz0SlIqb1UQe5JWmnkIKard4tuv4gde9e9oH_3N_4TOFe82kt4ceXZSsX6FLIp1JgqISzrs1X0SPpy2wk4z2_NlREjkrPSYYCtwKksnYGGv_Kr9XwQn0SQWNmkBpr-owTbjhKr1RZbrGa071TTZq0JuV7W04k20fAjNoRrNr6EPv1NetzKfXCErdzD27XjbwP4CfUTq5BfQuSs5hlX0IwGAm0I3n5k7nu-uAnyNU07F3dOI4euMirXl85jG7GVa1vF1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB8Rb9Xp01oC1g3rswv_IwRZn2BfQe0HsT9xFkaw6OQ05jiFyY9hTy_1ZZSMi1nbaqC79SYvpyLDTQkUwFa-jMUBuiFb9z6nsUZefMj6dala7begcfad-tALL7E0W0xIruJTvI5S1pxaz6qrk0W3Qk_5un2pSHUzw-okxFdIhkkbcygQhFMFe_P7gd4KvsM2iTQWaXk2X2RI1TE_8vE14JSm-ZnpQEZFYLj-WrFLENP0nT9Z0Rpqj3bjNgT1J6tCTo4DgIdQ04pUy9K_gLf4R-KdcDz6jD8xXVmrmnBFoiVHOKP-EKBsJESSoXDsN6bxAiQFUNTQYDZAW5db6P8SwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=njyodFnmz-zbJjlnvkYRxdranaG7G-DTA0B3l0VAZ6RWn2YIMvKZAd_ZN_WMPPnFbh2ulaq9TIQeNbTi1VxGxJpKdksxHJodoXWSTYSfi0YX9biQb8u8pbcdJNzYdEpfjjTZRu6XLMy_NiHde344Uq_i3X0WoVrvVQjDhyoXvCF4Yx4nl_r-LAUBG0a2faVHCj0Jz1ndslShF1ac1AQl1y4MtLuxZTEzyN8eueJH315ftUDFf7zT8r9OxST_lLdkFo8kCdI8KEAcN_xzJmc5itTeh2lvS2nhbM-gFr2e5DXexZtce4DhlXlbaYhPNbmOwUrAB74Z89l_piuxwmYs4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=njyodFnmz-zbJjlnvkYRxdranaG7G-DTA0B3l0VAZ6RWn2YIMvKZAd_ZN_WMPPnFbh2ulaq9TIQeNbTi1VxGxJpKdksxHJodoXWSTYSfi0YX9biQb8u8pbcdJNzYdEpfjjTZRu6XLMy_NiHde344Uq_i3X0WoVrvVQjDhyoXvCF4Yx4nl_r-LAUBG0a2faVHCj0Jz1ndslShF1ac1AQl1y4MtLuxZTEzyN8eueJH315ftUDFf7zT8r9OxST_lLdkFo8kCdI8KEAcN_xzJmc5itTeh2lvS2nhbM-gFr2e5DXexZtce4DhlXlbaYhPNbmOwUrAB74Z89l_piuxwmYs4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmSw7j-QyIUzaIXkDKrrxXZQMizGyBz_EoXAFZCUXKo8XDyg_aswwlKgJiDbyfrLLAD6G_-banJ9a7riEeBgHwsNHQR5LksHujkjMwOxrQ2zy8NtcwgWshukHsN_tsi6Aofdtr9iVCDSQgZyS2kMdIenqZG96Y1lhPQLhCxizStNdNzUx9CZsAU44hRljjfXVY4Nn4us3orRdlkIWTgFkhgFRWEhlHJ9it-N5UBOHFAHljTIeFFkycPZtbUFtCYGIKdZZZpPTEPwHRo2p17vWAmkLKp_0k0Ju7-aNoJgknWp5W7YN525NpjKP0Zy4tY1sPOcRVd06xA1BDwGO9uWxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=ICKjRezksHfdRw0iI1U8ocrPlnWw6D9Rsii0KUAkiI2FEfv-CeOFXAX5PxIJOkI1lGw2kR7wGCEkQI3g2hIMVcvNN8rKmwiWQ1lfa8r9DAY989UFd-DAI8GrZ9BffT_F9Kiym7DGhZyvfzHVFZENX3n_wiRyFhavjbrgLVcX9gj2ahvu0eO07zgMRQl0vXwGLHheAtN55HZAqharSJ0BkntbRyR8lWfopCasXE9bMiRpEAin_Mx6Z_mJJcgShNxZsUf4X847l64_e9qr5yhk2y8oeJF1lF2Zh_SOBILJG8wf6Cu98NPHsFCUTUgRcItIJJ5cY9DRTOud18xatbNCQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=ICKjRezksHfdRw0iI1U8ocrPlnWw6D9Rsii0KUAkiI2FEfv-CeOFXAX5PxIJOkI1lGw2kR7wGCEkQI3g2hIMVcvNN8rKmwiWQ1lfa8r9DAY989UFd-DAI8GrZ9BffT_F9Kiym7DGhZyvfzHVFZENX3n_wiRyFhavjbrgLVcX9gj2ahvu0eO07zgMRQl0vXwGLHheAtN55HZAqharSJ0BkntbRyR8lWfopCasXE9bMiRpEAin_Mx6Z_mJJcgShNxZsUf4X847l64_e9qr5yhk2y8oeJF1lF2Zh_SOBILJG8wf6Cu98NPHsFCUTUgRcItIJJ5cY9DRTOud18xatbNCQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=EWRoVPcJf6sx1wpfACFXUx7Du2ek4Io3MbqAbISc05DiF5m0uae8Ap_59ZC-T-GoZWqQLOJBA6ZZzeygyvoJSv3qjcMWFE6gVR2fsEE8QeUXkJ5H8M9KO62RmK6-R7vYH--zSy2MdOcU5kAnvwyYzJIG8wPMF2ZWSZKM6c-cTJ3hDSmpQQUxZwZ0ZPN6wNoLIdd2ubnxdRUwa8ChbXXwXFIzmbsAhnKSPIBNKxemMXxQ1XeW8c8jr2ddifDhZNpM4U_pX4YBmORrqhKE_kR2ZElHY1WOVhy6AEtnnt1gEyRyKVpwTOvDcSgRdCbJIpqX88a8YqO7L1ky8SS6YxreWDbM7ZKY2gyMti410XKgvIccjhXo12oBxxIHZdEk-5MCCHmvvlt6T3sGFKIFklwXX0S03erjg-tCImFZME7vILBYH_3NYZ-OIdxyCxtElEOBuBiVYZ3MZrpuQ9Nqek8M2BAEtFhjHlx-j8Nl_UCj0SE5bQ_CCT7sgBIcLqaJhApbA0A3se8Q4WXCxjc-7eDHHbqL5cwlkKnmqWcim3X958RJ12nz3k7sTGiFmkf2TEJM1XVw_LpcKs2oI2UdXxnPz9CitO8ZMoNEYBTELZYLr6hUReaL8vT_d4DQ1koGzOfcbzghtq8ZAC2F2iHxJVOgRi19-BT2OfuKbuumRLDg2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=EWRoVPcJf6sx1wpfACFXUx7Du2ek4Io3MbqAbISc05DiF5m0uae8Ap_59ZC-T-GoZWqQLOJBA6ZZzeygyvoJSv3qjcMWFE6gVR2fsEE8QeUXkJ5H8M9KO62RmK6-R7vYH--zSy2MdOcU5kAnvwyYzJIG8wPMF2ZWSZKM6c-cTJ3hDSmpQQUxZwZ0ZPN6wNoLIdd2ubnxdRUwa8ChbXXwXFIzmbsAhnKSPIBNKxemMXxQ1XeW8c8jr2ddifDhZNpM4U_pX4YBmORrqhKE_kR2ZElHY1WOVhy6AEtnnt1gEyRyKVpwTOvDcSgRdCbJIpqX88a8YqO7L1ky8SS6YxreWDbM7ZKY2gyMti410XKgvIccjhXo12oBxxIHZdEk-5MCCHmvvlt6T3sGFKIFklwXX0S03erjg-tCImFZME7vILBYH_3NYZ-OIdxyCxtElEOBuBiVYZ3MZrpuQ9Nqek8M2BAEtFhjHlx-j8Nl_UCj0SE5bQ_CCT7sgBIcLqaJhApbA0A3se8Q4WXCxjc-7eDHHbqL5cwlkKnmqWcim3X958RJ12nz3k7sTGiFmkf2TEJM1XVw_LpcKs2oI2UdXxnPz9CitO8ZMoNEYBTELZYLr6hUReaL8vT_d4DQ1koGzOfcbzghtq8ZAC2F2iHxJVOgRi19-BT2OfuKbuumRLDg2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY-UroLZkx0KzP_JwOHpGHwLFNZkBQ_3uxkOsJxW83JfdVllHsH250KxJ0RK0YyRHJlNFzL04RnAA_t3AvoO4sCDPAKUZJobFJIdrUKJoON30XjywATzPEm6kYKe9gzJMaWGBEbGYUUiZ7kN7UwT8BBZO6jyffcMWmhxxyqXmjJJdLBBhHqh9i_So6VSKsP55lYvPE4UjjKkS-BeLc7trUvE_JhntGSE4tmDFvfC5uEzIv0rvitH-V13W8UXrFz7F9UqiiGOaM570eESVltpOotN5dqVb5oPwTmqBolOWaPDllzAde1a8XWHZOXioZ-k6IGKQ4GBZWGBSpkyGxgEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=gh9hdwss9RTKakFXFKtwSZv2Aew_iuO0qIoXojk9rMUCQH8ZMv5GwxRoxxfu-wkz2LvpQwOXG7WUemwVeB88SXnUEbNA1BqgLH3_7Qc-6VnxVYdpMsBweGyf4rg33FVgvpa4yJaHjRnWb7ozTawM7bfIgQpZFVKaDwmajgPhVVwJUIcwaENFwtsKSlCfQ1OTjh4ic1VhoPGLAUbyS-g-TviLWulXGB8QHaDVhQzZgzF6Orih5oPSDNbON56NgN-1oZqpwYJj0mQe7zV_MtGZHEc3-UAyhVzS3IC7J1rNpkjQxCTKnp0BgclMPlSMFLbEf-2SbY3DvCSBYP5F0drNBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=gh9hdwss9RTKakFXFKtwSZv2Aew_iuO0qIoXojk9rMUCQH8ZMv5GwxRoxxfu-wkz2LvpQwOXG7WUemwVeB88SXnUEbNA1BqgLH3_7Qc-6VnxVYdpMsBweGyf4rg33FVgvpa4yJaHjRnWb7ozTawM7bfIgQpZFVKaDwmajgPhVVwJUIcwaENFwtsKSlCfQ1OTjh4ic1VhoPGLAUbyS-g-TviLWulXGB8QHaDVhQzZgzF6Orih5oPSDNbON56NgN-1oZqpwYJj0mQe7zV_MtGZHEc3-UAyhVzS3IC7J1rNpkjQxCTKnp0BgclMPlSMFLbEf-2SbY3DvCSBYP5F0drNBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OytFMgiMnjfHsr8cdy75rZ6poEAt1v3ka-BI6Q8G9WRjhhlsIOiFTk5QegOjRYPLHLn1QUfcY7KM3aDSbafV0JUfgOr5XLfbJGsY9Kg8kwGjLZaIQtO42wfr-YpiesaYtwkYxQygD2oy89-MQH2SxNy8R4FuDOm-yJGPdeLNBCzgiQwj-kCXkdqQG8tOWo0wgYtkHPrSyPRn-Ut4G-klaoSJJS64bha2phbk3-nTfckti-bLGaWj6i1t5AgDpUUgUDA5HOmtzHyIPJlBkvMbXvn-HQO6bVoWxU2ELKsqZUMhARrCavBe9QZpbJHQgTNBd4TECXENg_qk6XzqKRA9YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OytFMgiMnjfHsr8cdy75rZ6poEAt1v3ka-BI6Q8G9WRjhhlsIOiFTk5QegOjRYPLHLn1QUfcY7KM3aDSbafV0JUfgOr5XLfbJGsY9Kg8kwGjLZaIQtO42wfr-YpiesaYtwkYxQygD2oy89-MQH2SxNy8R4FuDOm-yJGPdeLNBCzgiQwj-kCXkdqQG8tOWo0wgYtkHPrSyPRn-Ut4G-klaoSJJS64bha2phbk3-nTfckti-bLGaWj6i1t5AgDpUUgUDA5HOmtzHyIPJlBkvMbXvn-HQO6bVoWxU2ELKsqZUMhARrCavBe9QZpbJHQgTNBd4TECXENg_qk6XzqKRA9YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=q3ktt_NlaTFhEv6LfnRs5fDyJ24A0yUH3uqZ0lC7oSK1bR5rLPXWC84yRAbGfAiQvPYG0I891UWMCv5Eyb3YcwFwH1cDCLGlNeALZgMpwd1EvW_fm8AAPHIdMoZ_7KnYt4CsPzQSCaDX6Psnyjh6a68qpH3Tm6-r93DQztD3GLsimN26vhDDffjwfq4ZZaZzIw02vm95Y_Sjxh2TeOvl-x2RFN0ShmYjObnkLiaCYQ81G6DME6GYjVN4nHDcDwdFeOQ_zQnv2A5tup5IHFPzVmfaHOpCqXliyO85hjfPqd7aWAgnSPX_-f0QOVgZLjZIxEhJH0y57GunN8LZp544QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=q3ktt_NlaTFhEv6LfnRs5fDyJ24A0yUH3uqZ0lC7oSK1bR5rLPXWC84yRAbGfAiQvPYG0I891UWMCv5Eyb3YcwFwH1cDCLGlNeALZgMpwd1EvW_fm8AAPHIdMoZ_7KnYt4CsPzQSCaDX6Psnyjh6a68qpH3Tm6-r93DQztD3GLsimN26vhDDffjwfq4ZZaZzIw02vm95Y_Sjxh2TeOvl-x2RFN0ShmYjObnkLiaCYQ81G6DME6GYjVN4nHDcDwdFeOQ_zQnv2A5tup5IHFPzVmfaHOpCqXliyO85hjfPqd7aWAgnSPX_-f0QOVgZLjZIxEhJH0y57GunN8LZp544QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et5SPxGSstU9yMwrVUohOuD81Tge1cyhqLfD-JCNwI6tYnpmxFiZVluFmZlLnEQjv8tJX6YHfE1j130WMaqQ_GXyvoqr8ZM4DuKzJ6rKNBX67AuurZXPVEWm5c7_69krUYmsKxVefWk1HkRF_p2DUJ-xYQIrq1pR63R4_x4I5RCJCqwLrI0ifCvovyVEE6z3ZlEd_-9CJ89KConZV2E31vgErIFzeqG_r9Q4vYZrCFRQpMp_F65IC_S1hLtLPI3pNQ59JXHHzdwWGncnvo4QlLxSQOUeUb2b4_IwRw6Y1wASM_Ru5YVyzggyKZ3_FU-5wF6HUaf-mKnLtZ6FZ-wFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKaG3wp4jIHgoNe8Z0mBdwfhgK1PcMxDBadN4L6nVCJDIC7Cm1ScDRzKJGLOwcZvQbJz1-k3idjSO5PscoOSMRkuIMfTkE0zQdfwBD3-0XjdlLUMMkUsLiWa5VQEjtD8EWTUf8Ds2SQ81rT9ChyF__UsGokf_CXTsM3X8eFPYH4tvZnmgP_dNOdclsiRu4nPT6zbaMfCK9YmCST6YInd2Z8hrvvVlwfpjzvm7H6s_IsyhTkVx526RTNnKKb0Lo56ymMdL_y_n1bZeHZn82vJ-lU1v3iSn3zBUdQlQ5ri9t04xUuiBVxKf7okeOYA1MJZOaDeYeJ_89Cw7vf84zJWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raw_V3scxhgMPK32d3vGN8DsVKKfyzX5EA1fALNuAMj4i-AaJwXwHaYJz-idojoKf39tGkiRTznG_j9Sf6P8_XmzHP5Y0wxa0HaZ0qOQjEI2pXrY7gJ5YjTg3asqaKhg9Aujpac3iAYUOF8upa0ohqzEKxMPjS6AHQj6pm1Wf6LuMqwqrMlXsf4eBVrcxY7GON04DxE5f18JKKgit4l-QEjDhqXVjubUbTZhkQVR3-u7PVKyeMZumLBjM3ih7e_AHo8oQ10eC_1rVFl-6Yk3pt2bchQGIvepW8O2_RPP0-KsAN8vInLWlHl0Mf4_9QnoL7Qt-J3HwjbCspr5sXJAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHduZ07EsXMH3c_rzFibHXTYw585b3mgj8TUKEAYx1waD8gYr6Cyy8F6QeReSBLZprKcnl09Gx7T6pztj0m41K7FDFo-mYWZlJA6ECAFvc-6mdza9bW74eHxLSy4ch-jMLU05V1R2IIYqHs-sZzQCSINco6-YVD2PPpSUWTlacCdRVPf8xXCiKuCJQRYqtb5xMlqc3rp2U4KpNnbM-kSN2fLFW9ZxawYEEK14_Ki3AZl0IaJ3QCfoSwU_LasrPDW_d9niKPHb3DsUZXaYYACdsUnVBii4W03w8PQ1rdlNPBZ2AP7yXWqrE2Dr3MKM62o1c4tI5ieqVHzEJVM1x4_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhvUGUReSA2Icn4DCwdAKCHRn2JsEe5B6NVuoO8tlLwRP-unpp1MGDivSHFtjDz0W7-9UF-aE5g_gDx7987CPuGHhs2tjJiIYUCutuNmBtzhPw5DU7CxZNxj-2HvmQX3QbDugmrnR4EHjhh1Z3BwTloy8RsxL2L9lmAkDCTLLtio9nrh0E6Finj9tupOsies2uHOfGaWOzqUr2tCDOpi0HBj9y6B0Sy9LHxwLIGhzHDeOl7d0YTrFIwdUvenqyz8wdaZRc8jSb3AuEA87rZO2aNXzmxMvEEgiK1JhkA9sFKdz1L363kGUOoOQT4Mxcz6B_5JqtIflafgvbpNKPR7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzK9tjm8ijbpG3UGBlluBRWppm3mmrM9ij9b_VauIOhYD0gpNSoDbjB5ApRPQwEklaBPZGPj-HZ1fU0CFFNb7iQ9EYsL3V_Oh4sw-cTpZ6BL9-KTgJjrGHeSZQbavhzCP8nzZSW-i1MevaMuU_rLls-yr-2CAu6icIqyrlDu6C-CyZJg3ZAKmAAEJdpTlUgzpCAXqD_BW-MUDFGNlD7wMaojpEk3c4Q-z8KajAFYJn-ty7iwKYcB2OjMJHJKRaIZWfFr90JXooG4UlaceFXQxDX58G1bZ_v1CfQfG6G4No85VOc6VhFLR-HPtm_U16D6VlRFaQI-9LI8N6cOTBPz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=vL_D0XeqzhxamSp4Ptk0dP-h0ihwgk3DTabnm3uJy6hCIE0uRf8TjdV4jcHQK5qGjcax4NwOxvIYHCiFpHpEw6ReummJd1_-Kcw6fYJlLyFjm7K1bim2L1FNeBsxXWp7Ys8TcTcI2Nb7DEL92OX58zLK1hYtrgz11hDOKyGSHjSsxhiOORvxHKxOJP8E3sc5pHkgXSlFnOYUXzgIZAKMnH_rWCE0Y0kcnDPanhi5XFo4zTgQeeyvGoyGmYBqG5YyRf_P2S81Sa04wIcJ4ULnfyBRXl0v1S2WH-wv5hCck1p17cYF7vnN_BskwC3lBuoAbqRhH9_njwwn7BIOJVc6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=vL_D0XeqzhxamSp4Ptk0dP-h0ihwgk3DTabnm3uJy6hCIE0uRf8TjdV4jcHQK5qGjcax4NwOxvIYHCiFpHpEw6ReummJd1_-Kcw6fYJlLyFjm7K1bim2L1FNeBsxXWp7Ys8TcTcI2Nb7DEL92OX58zLK1hYtrgz11hDOKyGSHjSsxhiOORvxHKxOJP8E3sc5pHkgXSlFnOYUXzgIZAKMnH_rWCE0Y0kcnDPanhi5XFo4zTgQeeyvGoyGmYBqG5YyRf_P2S81Sa04wIcJ4ULnfyBRXl0v1S2WH-wv5hCck1p17cYF7vnN_BskwC3lBuoAbqRhH9_njwwn7BIOJVc6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcevOrDPKtSbAQ7cHxSHRTzCm81mwmIHs7ZXl9f_GugWj619JQ0U429LbImiNh2DUklhUmTu-Y-WfXKKIRd1J_DiP0p3b-hScCzd2KWdB0aKkwXTQPMYCMvBoox2KSakr2Nu1CELlyC7ieLp03DBynNZj1WnaZetmQ2w1pRpd3bAdGTPsmQcX4TWWVHLrMV72hxYeq5M-DY2fx-Zw0HIsj__2MzFaDjOVP__kEQmK2PfFPyPTcpTg7u3NEbxcTZRV9CvB-uDbt8eeDnDIVT1OEN03n7hvItsY7Hiiig3bnmZnnw61i1yLNWWnw4NtH3LpwcA0iIbOxsKVVALA6mMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRSl7x7bo8zqZysfbyp0sHOYVG4O2JCxcopm4Y18JoTPhPyKFTR2AoCbfymcY__Fj8wSEC6u_w2XnWsrHGRX2cZ4Qhs3f8yt85WI1nl1d0Tkp3Sz8jRBjnyYVMKWHZSkIyhCtv3-CXXT3rXqVr3pt7alEKekl23Aen3PXnRUXFaMGgZujVTd5QALgBimfRnhlOSbSonqJ9sPpFgrHV8oha2aRRJ0Zy1y5EEIlFqCXSO2N2mCTeU6o5lUrLq-IhdMeoGyMQvthsIXAERvOSlGpcnzbIGs-p5I-DZmNYsWfFixchEtCBzD14ETipYRbBpp0fA65rCZnAXF89xpSoOLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehEYB31UlDU-B_YkCUljfu-rb5EQbXQ7ShBrGvlmMwF5-plQb8OEslUn8leY5ect7EdY-UMA2zl1xIPlEIeNjy6JwKu1SdAjoTQA88FOStUF8rKMS9YTHHbJ9L8EmmVZuzBYGwKTmvMCmktQZ0P_zfy3tiPwwT0L4LTNyMGjhaji9wDMgeCxXsQtOo66tlDxPUPRxas10G1rcrPJKmPoezgN2qkmmmVFoM9ZJGHwLBt9jNEjRINFDnKA5CgWNK191KeVKD3HKpoAwh0Qk2dXbx8_pviMarXn7g8h9laWIQOyoXeioiHjrPi_CEQFIMnZZhHZr3WVkFwiFFq-bIL2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhqwdVP7f9epjtHbBWvFAFpB3aqept9TLqIwluw54_sohdRd2cxo-bqDJ6sUaI7kuvguC0Ol_OhUWdoXr7P8ZFBSLGZjCWeDZx4iJ5D_lzTlTX9zObBBSCe_PEd4V22KyV_IqbuEo4vX9jltFMymRzvlmxExGNnH0-sUShZxzMBspd3XkeOhTuMEHncFhWxOxoKb6IOC96podfB-K5w9BRrJC2iAzEPoOu8p_4__ji8LdcnBcx5U2Jp_uGItzP9pLCmV_aQsJWSBDSCfER9FA9fIN6kQWkVrRC-cagpj0BeAjj9CEDj9fd0lzhdCYXZQcfZ21j6hQnlw-mF0IWJW9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjhgvK8kvbb6JM22Y_Z_2vsexBlT29RCJndJ70dKo0i2qf-W2-dbgLMaMoyoifUk8VR-LVgLTH0UyKblvaI-XKG36gxQOnKR9R1VZi_zpoR2sgfmWmSWep547fv2lmW73M2DXCIoTNmUY6a-uDWa3N102AXMOyynAtXtsRIjoWd1ncpclzp2DFCTXQPfkRPhx8AMRT4JyxW8ZNpmYBFvi64vvt1YDEBhDZBfHonrWDjyQ5mp_tSe5cQhgkcI7Oclsk3YkMUOJB2SgB9LrkeC_0SFd3KVXXArYD1fJvg2Am2zjETIkoSHvXRA9hQIE3UgHjtOGW8fWJ1tCTh2TlS2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJ9vVu8EoXm-GXTXCptmzcGmHc9uCCkBIGqjAHiJ3sBHyvZyThnSjx8oKxnSV-hgGAH2WN0ksVW0PRTuSYgRcQQcTcT4WAmXAUYoD4WBRNIg2mVut9JCIwnc-c-Q8rphNXR-rQT-a02SUfHZS-ZMJYh5f9fKaCQSJ5H2Sa0S9c5G3JrzhmSNFgisKKfpBiXi27X_XbnXHKz3E-i8wxWYyrvJmQKK9kPsI2v9zyDEvslI1sci9GhGqiFi_11-2hLuU2Xitd8oEUc1s9rdhlPsol-pL5Ukx_YDKypaijG3mxwSUcvXPI47qPuVNL2sRXZaIvyfF-I8Hc6erxe_Jiu_3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=s_2tmMV4vwwVI_MSmpBAhCIoElQmxyDttXZhXyDaVw1kIkhtAUh4S_oaf1XiQCqYDbqANX-nixcheOxIi91DUcAJ5Dm6efnNqSbJzQS5NZhZ_Sqh8SK-ETpKSTiOUr9Vm4P4tOrednp_-8HHT4kk0OWiwhXW7XtbHT2h4Tz7XKlAPJGIjVbx4aSM2Qh18Rfgg8d_zz10cxcRAcQT2hfV1u9byYrbRUmsZSIlrwo3qud-Sh7a6tstOUQVrtdKrxlNqABqE3IvwylHcUHz3mlnCZyhpZzjcI2xmMAjXzV_BFi8rkYLTs321VcXxGSCrSDK9OyttTynSW_voPjVDNhZQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=s_2tmMV4vwwVI_MSmpBAhCIoElQmxyDttXZhXyDaVw1kIkhtAUh4S_oaf1XiQCqYDbqANX-nixcheOxIi91DUcAJ5Dm6efnNqSbJzQS5NZhZ_Sqh8SK-ETpKSTiOUr9Vm4P4tOrednp_-8HHT4kk0OWiwhXW7XtbHT2h4Tz7XKlAPJGIjVbx4aSM2Qh18Rfgg8d_zz10cxcRAcQT2hfV1u9byYrbRUmsZSIlrwo3qud-Sh7a6tstOUQVrtdKrxlNqABqE3IvwylHcUHz3mlnCZyhpZzjcI2xmMAjXzV_BFi8rkYLTs321VcXxGSCrSDK9OyttTynSW_voPjVDNhZQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=Xapxi2jt7sAliOLKXnl5ILozEfjM350vrgjAPtPoVdEi8EwN4dj4AjuPLVgQY788rw2169iQ7gZIEa-Z145narhdDmRI9ye_tsxaOnHKh2BQzpPChYQsQ1iv3x37g7RnSJQ2WPqVuZDN78F2-DBDDNyfPaUkors269wSElRAuwsGj8g-HULFPQcLSx8rPrOOfbHv5aZFs-sirc-hYWK3P8X9lqiI7TO26HhO5o_Wz-0FqX9Riwro9x76oFoR9BgVj8oAo6xwoiYXDI9GVl27ZS7WLF2G5uAtnitowcwQFmSp7kSCkTONH1lWn7mZ2lpqzj1_yH41kUQp6SORgeEWGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=Xapxi2jt7sAliOLKXnl5ILozEfjM350vrgjAPtPoVdEi8EwN4dj4AjuPLVgQY788rw2169iQ7gZIEa-Z145narhdDmRI9ye_tsxaOnHKh2BQzpPChYQsQ1iv3x37g7RnSJQ2WPqVuZDN78F2-DBDDNyfPaUkors269wSElRAuwsGj8g-HULFPQcLSx8rPrOOfbHv5aZFs-sirc-hYWK3P8X9lqiI7TO26HhO5o_Wz-0FqX9Riwro9x76oFoR9BgVj8oAo6xwoiYXDI9GVl27ZS7WLF2G5uAtnitowcwQFmSp7kSCkTONH1lWn7mZ2lpqzj1_yH41kUQp6SORgeEWGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24850">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B42rBsp0JGdN3eNIHIjf-4iCU0YjrLWXw8_Oh4zVW0U6mNxRU0uB2_ZjASmSA_gB9CPfaPJ15nMFe1Pqi6lG0robeF2cmCSMMYhcM2MIn0MuGNT6gY5oAMuTsxTlucBRJmcUuoh7oW4D6CcjCHd5X6caSRNk4skWGZVtlOfjKCRhfZqY41OEdSIKqESZvG8UAn8y4812_b17MlbuQSd_yLuHCd8Km2fJM7rDr6zL9Ql-ltk2MGEVBH16suyzn6U16bxaC-Obc_vTnBDb_R3lmy8XvkHnjfNGlDT0NmcXYrKudm2qFAYZojHEosXWDHaKa0ZGRTAk3uNJNc8am916NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r12
@betinjabet</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24850" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2ZaZdng9RmIdspCVJCk4pbwT_n9ppCw54Tse4KWzNThg1zcqHKZ2jj7SuCZpek7RMWGy5fuMxgs2wDcMaSTGeQ9RdZ-WKDiWV1QsCNSZUxUBaczUEcTmIAEB0np30Fkn-Ft4Kd616L9HCIStq7KoMv25WgosFBbmAaVR5hnolw-MeTy2SnMJAz7W1VFl1djLbSoo0HzlQ0Iyiu4TZjLUgEdBUvMDvoWsieK9o0TuAhVsukVNCrv_Fh6lGrzLcEaC9UsJrxdfazuNJUUcLO65BiDDtaTVkC4Jl5IN0j8RhaPfE7vPQi4F1X-u4FuuOrrMo86eRYA3nVV24LU4_WEeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTMdpmrWcarX-J6fbnfzJo7x0Hy7R2_UedNifoWoXvodDsIm6l3y2afKJYah_IaTcokT0RUKgl8p7xobZceRPKwlr9_3DxZ5xG79TDcPKwfKT-lZAhhdFCCvsk8nuMetfJlCH3YEwxLI8L5j7-S3-syFIyYJsK18R7QdXJtk-UjNyE4_FAdat-MF6JHwoJ8LEcsT_Dvut_uduhTgoRwSEubTVD1MZThtqi8xq7cT84ne2mnDNqS2MBtu0_ivGqXbeoeY8Dhetn3kDmIUxpWxbuRjSkgCBCkCOwYfoGWoX6_mYMLpvEh_bkgAFlZ3_Fqr1PrDnvgZrllEslQLgN7VVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUSdhh3JDaeDpY7rR33BKpl-TYwME5byAhgmVP4_6toUeZLf1rJ1furMrE9DApEcO2BLFgXc0d-wJRLtjSirTxme9Z2fktPg37-n45QC-Z-26XQIVa8Qgc--Bizx5HsKseLR09WMjs3UJJJivosRAK_GH1S8xytAD1Kau2AT_RSElBqdZxL73Pf2lcilZIO1tngl42rpMs00-zNCPzT8Nqbt1KI2sQEvf87COUUREh1zRXdh1MSqywhg9NUQdAFn0XbVyyY7DSprohwmhd-pqDV3RZrpgUgvXEIU7PWSuot62LXfbJKDEuRtuErAGTywnKDBBYXIx-EUw54uf9s6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZJH_DdQV4R3BEI8f_1c4yrnsa5qB31rX1HyE7fkniEJQ6fQKlrbE_TaFIREJ30Qz0r2Y7d5dWByGLkLqJQoylJ_FgBpRQSnmI6bEhGrVT1O7mgYHJ6dz8WwIYwDfjEpqkcIPdafPfAvgRdnEoLzpypdikcT-sL6vo-mtPOrYDJ48rJtJCtrr_LHPO2iivrlvARE23qmWF7Hi4JacLowz0mnDW9_Qp1d60vRaVD1v62rFJReWKhbNqAt9R8v9yEO2ERZ1Gnx18XxJNghro0MB_V5-bbMAun74lT2_W3wFpYg5VCO2WWQeRWALRkVhL2VVTBvOHB3ZLv-9KdOI4cu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrAkjQkc1xnMoRK-767r087oonlAHmBLSkN5vdbwByMspZ8OWXrbokIGWpk0OvkkNxBlxR0nVIoLhMRcjoSjxeqg9y07vOwbNE9EC1pxZ8Y1_92WjAy9pyhiAJhUxo9URbBdn__rXkmnIenZkgnC27_OdTeuD3QEEA3qJX8OYVxX2L5uaeM4YGEhx_QXC73yNkas4TWmTl7tCKM7aLdEDZyd6f4CvOxmoxU5oLR3dBIwGwigZi8e-ENqq7ACJBjECyHuUuf5PYEHI6q7ly7dBw_3BwMN3atLbZ06Xif7IJrD_Pl8BVLsVsTTRe-JsirrP9OPyZHSrJe61G3zElCQPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr7U3ar2gEYMgYUr2F_9mu8gby5XQlnE4KRXeS3XnOniyMt0_Hj-JIc649u7A8GgPtN_joEn1GkFkeo3EvdhD83iFSIRu3RKwajk7WI4TMNqeFfjNR8Mdm10M8K_WWbmFb4Hqdozhed1P_VA-ykY3h5SysRck9gl8Tzf0FouCImGlh7lxZUb7vOSr9HEJmP1AV_K05hxPjZMvuFio4p28eFSkUzOwgAPyTsogZQ2v76v-m7cRO_sedEwHaeLr5AuUfQphQjQjDgZzrsG_lyG2pE1RuNF4x9HuHSmfeM7S5_faskIS4x2SWSW85IRyRbWGK1oiJTdO6du_EzQUc4bCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ku2XTwix42_TjCTvUnI7Ju2G1ygIp4XpIxWkU5VpgJ1u--Lxggl8F_MJE68ucx3NRsNTni1vpiCtBqRbce7sf89-uc0ZnbWOkUhkjx9Gl0l7wqLOi1kP0r54lc7E4pL3dVg-RPfDVEDO8snlM1UlRoHF6nT_mU9xwjOUdoeqVtPrbtgryXO0hVDn_9AZoOGMpyqxgVlp3UPJ5D60jzRoXcUOXufY7oi6YMgyhtaX-JZXOdzO-ipSKBpn-OUFY5zGoUQivRapqsz7657valSi3Zt08HQbj7siSTBHq3WJHEcY8E3WxERc1FZ5rKM0s15TITRISr4l9Hpl2gg9jhXaWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtSxbUQ-meSF_bH3itxDgpvw_R-ToM2lS3cOOeUHQUalVKH2nM-zFGf2JC_jeBKgMo6l4fuh2hELjPwR6L2luSxdzQdyM8RZuL-Iet9yWtd3hEPpt9Qn38giyv84-IYv2t8jFBRal2QcE7keyRPLRlk43KLpjuRThiWfsRYdLCC3lx7CY4-dZGSsMAVligMLMN9ARCf-KWiHu3Kj2qQKcBpgTrsMhAY0dcewMQFqao1fBIQWlTXE0afUtnGFQW7S4X0AvsddDFRU10DbDPGyiUzxomdIbAOPkuVbG8ckJqGAnYdhcmXl1TkqKqhDaYTQhrPXO-NZthyL0V4utA33-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swlr9SIaCrOQF4UWOreEPwTOScGoYV4mfQplUWCmdAG6kmQY5eEdMQO6EcTpGBPtJ-LC0PbaHxOE0FFlLD6gZPaug1g_y3p6fCc3bUR8GXZZeGlYEDKyVURd60m_574EXzCtIjmzJViOTvUQTDRAN2IcQ9Cni8joMovyvkK9omDEfPa5O2ot-vLUeHbOkXIkGCLs5XRFxi1QZRPvmQOaGv-NKOnrO3jsY75pfVrJjaSHbs_VpeywgFRrd0nNI1M8r_MWo3BRBJD5UJ9iwIGxL8w8nl4b092Ac4suMa7QNAWbV3ad-oLPXb_06FOQ6uVHMCijc-v58qzAOyRJ-uJJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSszuRasUzDwaXcd5rvbUBMJnSKuIA2bWq4gT-H1VwRo8-y-G29EYc7KrFI-6SgFg2RKNakwr4IudiMMCP2c7b5XE_9EzZ2HV0gD69655uaZX-svIZRh2fe90STIjQ39OvpjoDP5HVsjWUD94_3CyaneU-aXpSBZHw1uh4LV8EvcB8-z6Gkp3xBUsaFBVwwgaU_f_kNXBhwImluhHW2PA0ldOfPuplZRpLGhS9z6WaPJTQBHqwbTmaux5CxwlM2cB1GO2M6v71Xqg1mC-p_lcXH6zPljGQ_giumfqwkWfq8ijVpG2IoHFPJ-toZIqHx_uOsGrlDN-NtyKP1Ft3Bukg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAfeiP4kxIpeeYR6X1XLz2c6GXLnHdCI4tNoSFwhtz3S_OkEMaRRVfYpzWZBFd9QmNLz3hC3B0KX-ih_g3XrqBEwIv3Z7JVas0l6yRG38IpFqEaTmX4-43I8YV1zKWz0nQSKqsssItSJCogMC8iDlNv1G_T7mGj30aznvb3mK6LVsygdfJuotAsCz-dN6tV154AknuyhzmYFiO3fR4qQqAvGz1x9-FsdkERjqnuQmwiUc6nsgO5g1OptlT1KSesPVeL96G70RRaTnRgarVe-7WRB0nL_JNlzgpjAKiuhlwfDJ5vuZORo9NmhyVCUZ_5o4YxxCK7pta2e6nT8rhMvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2iRkjQzD1DCpsHXyy42up_A_obyQWry5D4E49bodm60_iBndcRHlW_ztntwKyYeQiaEBz0lGtrcjcuYfy7oxw-qWGrQpvoy9K_Xq-_lCu9LktRX8LkgAK70xYYJpQrVv3Mh1lyZ-k4QRTeHXe1jeV9ryYLt9XGl1Csr7q-PCXmeIPtRNY9S1bUTkY-jEINli5_mctY9x3GH90K7OEnKkYuuM5eYuYOj1NZz5Jfr9_ofNrAYLv3civE-YbLAtMeZJQDURMTYGHsrNvv-NT-QR_qBZ49C_HMeoZQt9b4X9aLEOeukRBErc3YIDNpmNwpfK_95eG7LjdVKgMGLBLsmBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsOzX5sl-eIvWDIMX6lTaEWPBC9saHuuR6abTophciE-vLXRign_OEhz64hYQBlK64h9A1lupz2OAUM2FKS7jogGzMD_bqLGEbi22pdciklNyQ0ur1OLfRSzk53UQokb0Q31pdtpAr9nwFwRKZtJ_7LnUqe_t95TPp1I0T4KtlI9FC-i9ayv4_WQz3KW94T9hyKy7Uqh1A0Rq0lYrvHSgALcu69j-orBn5GxCs_b097IkYAjQ3Q88hSKBaCBBNhqAZaLmFmwd3fp9xtyI9Zg3Io7wMuBgn5ODkM23dL3Pbopdt1_RWfv5Wyjr80ZWIhgk77RO2iHWvAnI93dum7adg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IcD9V6nMMthky_HFcnPlaqHx7EsS3mNLtNjKmRnlU39CFxZZ1_H6VhxNjWUB6fsLUep78YzPSVo8t-mbxiZiKrThs_zbePswaNB6nhzaddfNvIx9sXOKp4alaBSwsPcUmSD994HqpZpM0kj_cfvt96LaYz75QoeRlU5VVtJlfWiVCR5NfT3t5T5N-2T56U7vshEEpMwzGswHHzULBjYq9ziOFdAIvMFj7BE7twGUjJy9cuO2EaAbC3gReJaYEZsWFOZfqNwrUsaVNSud-GlCc0e8939rmYjoAEBFRY8OKBLbLsha2w2GKlZCB9-KiP9ZCrUm-qGYVplYyNIeZKa3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IcD9V6nMMthky_HFcnPlaqHx7EsS3mNLtNjKmRnlU39CFxZZ1_H6VhxNjWUB6fsLUep78YzPSVo8t-mbxiZiKrThs_zbePswaNB6nhzaddfNvIx9sXOKp4alaBSwsPcUmSD994HqpZpM0kj_cfvt96LaYz75QoeRlU5VVtJlfWiVCR5NfT3t5T5N-2T56U7vshEEpMwzGswHHzULBjYq9ziOFdAIvMFj7BE7twGUjJy9cuO2EaAbC3gReJaYEZsWFOZfqNwrUsaVNSud-GlCc0e8939rmYjoAEBFRY8OKBLbLsha2w2GKlZCB9-KiP9ZCrUm-qGYVplYyNIeZKa3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb6GYARKXo_LeY6wv9QOoipbyFfYfKNzf-6bnlL87A5vJt9OgNrYAMMBubPVmRdr0Zd_fg1_1onCxB8pcnwrcSWsDrCVSLQ-Kgspga5K443xjNjlVRnfxSJ-7TPtaEtcifKtJX9kztSpqBFlI8ZHrAN96Ux3hCuqe7Ts4tjFBwHOuHDKFBaNfCB0Rs-4sM-vqt1Kn8yhXgUCmAPuyiIcr3gyog_BcptiSAcjdUJyP0_7nzJiSvikjRlOUW27X78iLxaOQgpJ6yykCUAliZhq81rD6hSUqHARmI29gL5OgH04P_hoIbqGof2kwW2xsn4UyoVG0rDD_s9fsEp_ofLWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9kb44J2DriJowo-53AUA8WpRTGDfCVkB4974x4Cmq6kbply7vbqryVUMwYKgJ6ANS6zo-AuNeZc0MENISFT4rK-_tghGAmv5bGsRQCnkdl8OI9eRFbSGsZAGygSyVIxN8ujAc-RDVrpJZ9JuLRlXT2wLA_Y44cZ_1wMSX-ryAM4Pnh5QEs3032sHI2A46biExNi2pNqjZIw1Weoo0xJ0m-Ctm9FaeHkts87Ooormu0kQritn11SxQGxm6mnEZMBBAzvIh89Nr6u4dyz3tdWwPNTsKwJXRm9u3GVdxPYoCoSTYET0x5QNVX7FynmsMRF2p95cccd97XYdzT7ZNiI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXnBcJGnelOGdz_nnVwMZqQfChHIv6bnDlQNQlKSFOvvLnm9OeBePQB4bf8RRcd8wgLRPBWq5c138qsAqdLPGu_H89G0jCITfV-svpHjT_xNwqvedkxiYW9DA1Ag-cvzWEUl172Y4ZC8SHGBqt3S747jMe_U75FAis8yZjtofLTD-aS-lMyJZTm4Cbc8E2U14NNkdea5aFGUGhZWK1r_I9TJZ5m0lR7JOEP8ZFdIf5ZDr6jZXiVTc5vDYLujzbJ5TmFxgEGq3VfnUxuh414VxzBs45VIBPYxfuc0c2x1ftkzvy588EbHXeavHWmgFQh2hf2xQHI6rmZItuvqkvL07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=Z1ldoiR5OgQtY4Hp_wBcn6q7QXCCpRwmeKV2aU5z4xlaGog8S61ukfOLKUN99IJDsntCQkkvtf5jg17Zw-eoKzZlf6S7rz_MZyB0rICUz0EqlWcezR-kBAVMdrTAPDruMhhCws4TmapIP372sq6MPjB_JZ5A-DGlSVX5AFv8DAIXzCQS_gZV-lLajQvyZUEkq4sfcsbWAxHNkYn3gr1TKo5VhF4Wyf0TWtEEXmOvdmO25r0XoOHotVpYmsfDfoC3TxKdpbcE2et6EpohLyrKjowyj0PW_ice8ymuVvnozyxky8kuIfa4IqoorOrEeQnR8kqpzedSxEtFEq0UxHDa6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=Z1ldoiR5OgQtY4Hp_wBcn6q7QXCCpRwmeKV2aU5z4xlaGog8S61ukfOLKUN99IJDsntCQkkvtf5jg17Zw-eoKzZlf6S7rz_MZyB0rICUz0EqlWcezR-kBAVMdrTAPDruMhhCws4TmapIP372sq6MPjB_JZ5A-DGlSVX5AFv8DAIXzCQS_gZV-lLajQvyZUEkq4sfcsbWAxHNkYn3gr1TKo5VhF4Wyf0TWtEEXmOvdmO25r0XoOHotVpYmsfDfoC3TxKdpbcE2et6EpohLyrKjowyj0PW_ice8ymuVvnozyxky8kuIfa4IqoorOrEeQnR8kqpzedSxEtFEq0UxHDa6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd3-pF0_v2y9x9_bW5cXJWdtuWR9Z9xlqE0jBDugKNfDo0mrqAGTqQ_D9d6PWnlYl72xFD1P-TZjVVHK2Q59Nfc_-hWqv2kX3rJRwMALx0d8ObUydqDogYBWbE4Cur7jSP5gO4HfAOpslTWkFdqXHHD7q7iUqKFoXo4SyrTmnYTUpPDloohu88dGjeqOoDaHfoxP7GesOJ8n6x6zQ3_K-kOqLmrHwuEUZUsCEArqitGT3Kfl6z_AxO6PFVq1IJoOtez_wLkG10qBY5by2iG9F-0qW3P2H9VRYygV-IhkD2bfEb6DCTYBwUbxeeHflj5QPfT3iVzkCh-OHhrMcVtonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=j7WpER2sDPr58Gh9B4YVNLCSQAy_bYiomDh1G23OEia72h9d_5VYAUP6nSY1vIZHCePJDztSPU-_FaVL9T9rM73oNX56p1LiSERZ0YEdmPvnipaPR0KFtBocdvAkzDdaFFuq9ZTcfba2BzbmqhkjZ0UfKo1314nDAY6KZysJjhSRGtIivkVjjv_LAMYXCd-VZQvtrBQUfAsnfJ6VaFOEaF66dfv15Pu5SXTTtLubCEadRavDlM7iOVoezCrN3TvVo-sAGpV1FwKfCqkWkzZuDmZo7UQ_VwLsd6FCRDZMR84FBd5xxvms7knhGJ1aD33hh11EP-hzxliJ6HxycJr3yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=j7WpER2sDPr58Gh9B4YVNLCSQAy_bYiomDh1G23OEia72h9d_5VYAUP6nSY1vIZHCePJDztSPU-_FaVL9T9rM73oNX56p1LiSERZ0YEdmPvnipaPR0KFtBocdvAkzDdaFFuq9ZTcfba2BzbmqhkjZ0UfKo1314nDAY6KZysJjhSRGtIivkVjjv_LAMYXCd-VZQvtrBQUfAsnfJ6VaFOEaF66dfv15Pu5SXTTtLubCEadRavDlM7iOVoezCrN3TvVo-sAGpV1FwKfCqkWkzZuDmZo7UQ_VwLsd6FCRDZMR84FBd5xxvms7knhGJ1aD33hh11EP-hzxliJ6HxycJr3yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RncnpESqiSd8nyiM7nVB0A_4oB53N3ABu998fa7jwYI9kVa9yljpk8Bfvq0H_vYMPfVqnFPNW7irLidYpqRkpvjIR6p57fyF2FAMPtpOMj8EFNbpD6Yhu-CRuvLWmrPumwMdS-4lyJxfbXpBePi5PvdzvvaWJ6vN0pYEn5stHylGLSAsi-6ewl0lEf4s2_Eqo9p0ndnd8VNXrIPX8cK7PDF0ruiqM3qk4PU0EFPP2T9jQzaD_oHmjQG4JbkqpP1fmL2PSyjV9QgjWRRc99G1-Fkyv_FECE4bF0XNMK2koG28JF2wBi1vF4x8uFtse8ovCpEupQeiQNMqF3JWvCTf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC0ARqyvfJB4PMB2sL2Oqh2o4NZkzoi5NrNwCY3KZGZ-FZWH5_D6RCmKVXzLfN2D5k0vVVVHm1G3lOL6MM-6XiEEQh_iRM7bDrbvGfr-oxGZUjbEHjXBdHRmuF1eWI7pRMsrIlkW30EZK8mE64G5kIqlMfF7tCmrtPRlWn3df4m3ep5JwLmIyAYIYgOuL8RfsCNVDmufPi9xaipXuzcXQdHTC2ccfpHlP2haO5n3bkWgSthtEHsNLG7k_DyIOFb3A-01qimuQ3UswhZvaytsa4fMiJMnsJlB7n3uHOQCewBEvAo-3RsnttJheX7nq-26QeWu6cPlQsPrUOoXQGaxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8glo_Jlj5ehxXjsWXcIr_JzM0n5G8_MpWt-4xO7imSEfsEdGXYeP2WIJa7KY-VbdjOnlO37Uvaa3KF9krQYgukRtvEscIPeMKlqkhV-ZXKGvCNw6lxFbU_TKByvRFE-BD5_B6EiU8OzUIfi9EPU6LA1oKe9cEOzlPyFsMb8P3hR-I5Tu5xVxH785ItOCMepRPQDgn73hSoFdkwyKVWiiPYYYoGYkUipcZzER1AcJfBKhZiy8TEl4rR38ditL9x0OciCzUAt0U9ZVC5v1VGtB2c_5Ya5ZEG87zbnEkfKZ4omXJ7UPY3OFucaxf69C0hsfwo_yA42s7PBAt_0YJJ4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAN3qVqeVi__-YDs7ZXBp--t0CIkYy9YQWiyQL5ieScTrFPE7qCZjpFrEF_2wrKl_9_ROd-Q_VIowyvUCIz_eQqeitxit6N3c3oYfSnUlfA0x-CxluoTwiyX76rizZDm8iGKcs4MhRDyP7YZOX1AEEufCs3Hmr0gGoy6R1IAlh-8o13kRc8mp2SfAgqbMcOb-h85dqA-wwk6HW-JHtJXAlenO8IsBd2_pdLgV5b5RaG4on7Wk-MGo26DKH2F2yxsK3IrXpNZTJp4Vakiu1h6OvEwWbZVImRZQbmemHITrpMe9ilT65IlbrygupNeb2JBD1elW-nySVUGGm123Wg0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24821" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFVqhOPzi_9YgqtAM7XdY9EgkCsmQVAD2VJbIPAvbOutJSg4mHe_i5k5c-vtkKj68RQl7x_IIMdruys7rdykCrK-I4sEcyF0JZv8s0RFdv05Vycfv3kIgf5hJALfOvWMvJVrP2f1smEEQtgz41TVPeew_DQm-QHLmLmIbORL2v0hUhgrlDJyfdR_9V5_jXzUZtP8qJDsJamAOHRDqm1odjTbOAh9OpirL87-f8HIx8Vob28LoFc6FzwV45BSGk-4gieyCVtzv6j0QmT5cU1pkGnk9yjGTdffMmiN8Prm32Jo1vRt-YZElaBJcSQVYs_XKGKuEyTFUA0ElwXwPfPppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reYYAinnJUCKhdRGwaPcB_QSe33mZL-yR4h27f_wL4Rk1ynY9Ldzl2lu89W2Sz7Jrgsulz1J12j_djkpVuxe_cRrjSIGFCItEupf7EaMtALaSrq0yQlMG0neulV0opsBgba1RP0sVOqZ3TwR7argFB5DErgY7osJlm0ZxDJjlyL3z5rxrpzxunNXvnQZwxBcIWgmguak80uoVenY31NgmiO9xtkYyiHUGwUrAurBPeDiecof-7J9nWz3VzDyuIsFuMFt_f6gcZPT_tP-_8_cDN6hyvtGVRny0qRkj_lvbkhgDCwgm1MW1apRG5k9eLfyOmJkcEtT0x6dkzoAoZpoIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLBDFGVCxN6PvexJMNjlr5Tx_pYYyJhFbzANZI652Z35_IaJvvX7Z9p_9W1C04pAw9zta4CWbkl0HRvx3ZgcWKnE3R7P2wzW0tWAJxtJZmoCXvw17tAzDSJ8xM_ZWBPIalqf_7g2u-s2nvWSFPYNWtw7QtSInJhhsei2D3JUkkFPVF3neiif1o6y9QRmGIeGRJgz8IuVpQ4642QllYJPKwgQJEe5f88vn8CHD06pYfMdzrhsMw87m2VuFe8qo78_ed4pqsz263wFJvw_gt0psKEAmUjfybFEgxCSg09K95aeKiESv-uPvLZLZzUTH0rgulSLEaNRz7rOUHf94spVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1uW4VvcERveYiLOpFYOv5MXH7I5YUmYLvrvFCcR6QFdDKl7i4EvEKDdOSgtxVKSSWUirtsJgakzclRibL77rMm7Azvg93eLtwd7Xj1TsA9i68r5xyqXTvGE2Xu3bw4ZPdKBw9mvTWfDrLtySlCymvOYu4NP95fqzSrZhqJ9TDQqNLbbHEpQHouTd_Nc5itBVVw9nsX6poNFDj5lYYQgA-q8tL_ijZpoaiKf-CV4AfCSK9a4Du48anRi6rj34W8vcQmaciXGsoOxyk3haLG_54SvFLbRQI2GAZZZ9IWO768t24GS_BD6Vf9oFTNpyreyfzZ5QPefU3ZL2GnqZeCOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etpmk_Ly6YMsv1IKwYBH0Pd9IjkvvMeaR6IstXF7wahNrj7SiuBa60WANtsddRvTCYobVly2rOBbjqpVfQeJjyVcDXhMnimDz34HPo5TWtydJ2EFNwP6axk6dblmXFK3ICzPw7jptMpsfz1OrRAQ-RiRt1Gc1rwDGQj4fru7UndOfRyZYuI-_EZL8hkxW30XmacKu3Q08sD4_aANTDBq30Ens5iw2tzhGZ5CXdQIUYYGgMlYGR-2jqeVKNos-M1S-Vx9hjoV-P5dpf-O7jKUwIvja_02r1WqjVbt8FaWvBtz8PjAe7zmX0xTJZh6W_flvsdFAX3SY5r6-rBLXtzwXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ8otKv6pwuQ83GFxa8KSE4hweZNKLGdbZWH_w-sC6r-6MAHdfWPJyojB0d1_Z6OPPPUTaaEkEF6Dx1HJFmr4dPVQ135VlAhPPnHnZWAq37gaeN22cM4caxX3c11RwQF2W7Uz1jpVOnMjkvAazd28e_COGKXDlxYPhbTbD2GgWXGshBYgctFQNEHxpTq7sfpyvxcvWJvRdkPFpWd3Nqy2fDM1wc_uwECqOVoX_P6PuRWcNB2wh61o1H-anZwk5FFcDgr8-RD1UJNRcaNSMG9TR0fKbqAYlIvp7TP7AYmC6NKEulc6AJwev5hk1mC4PqRw2UpWqD2YhoFQCc8dGOskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jI4yw73ZXscEosxDbzjIaKPiL28n1llvzRBjYPmAieQoGSFtF3TKTs_dUiLSxVKpG4wCDVvIm2iqnv8MZcs3zVu-m2V1A64MtDeCcLsgNnM3MpITCrTlfpisdecj_pNKObk77_8FVtZ4wxtwKRKjjeE_JrjLs6E2PPLpVZFGhztLaXI6mBFl0O6I6IxURV3iL7tIyd_QBwZLEQ0UH7DcCEWZdIPJdSeskJboLyLDt4u1xPYGuqZlBi1YytOCyIA7ScZPxjjb6Z9HrMfizh0j_grRw9pScXaHhFYzmAU4T2d4qUot7KGsYnqHvHMk6O7T0ZJGf4c-icOiFLwcj8SjNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq5-y6b1cid8LhaWvEQSqDdKSukbTTA1EbZV4avJW0pLo_Us0x-9isPtRvpudaub4hXCiVshK3wjtUYBgX8LpZOx2YSF2pvBjbcBlZfq62IiYiKcuYEejwtmnowJ20A9KtE02ahNyx_2iNrc_7CMLsfN6ed3qyrsK-1ghjpHQKcY39gvv4cE8ay656AxGO9harqL0Xof1UAMlVmeyspxMD8BixKp8uDqxK6I8CDgL8x9Mn5vZQ9vGEkiX9CB_2ErrxC6Tq78e7wOOxyjO14Flt94OoZM0zg_NdOdSbdVML7cE9eK-dcr_OOgRHT7dbzDLN2mPY1yy-Z2LlhJ0WlrCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFa5AyH55vQ16xd8opw7bMK_JvMZ3MBwFAWIao5BOVVKJifZmHeFV2mvrMwyUzhsk74e0KcpHoz3M9bfYhOULfa01Wm0P4S6FLHT9RZBrelhyEnT6qLIgQQUuiRm0qhHf540Wb5FWB_G1WjxXJTF0Ow_c759xceAnVKApvdt01vI0js5DFYq_-DOGRWfSmdxrRGsYbqFQbIsYUEhV1VPmS-bEdiWMKvvpsHvQnOX0XJEdCY86jOMBBn3x8R7Q01yG0A2PNU0KnNPhqo6ZpHvjEWpOONahWmKsNgteq8svd1tuIM69V1FBJqF3tvaJPhhjYjMrezM-B4FtGKwvLpCNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ign0NVAw-Z3DnlqX1B1OBHtWTIDJHb1AuPEIxMLHF1Pbl1Dc3j2Y_a6ecRu-p382hu97XfIZYx6Ix1JcEpGOwepXb7fTs5AjuBg6iBsg38GCAcBz71dup6tjHdDd8sr9oxvBtg78B6LMpwfA1Skl8Jyx62gIYzWpL5CVIlzUBTowrigu6EQjpMo0eaNnT-_uqHLtQ61dKAQ7gygGjzDfS8zin7mGMm6_d9fq3LpnWlT2IkvR0Hi2doV-gsHMPotXpXXtxAsren007ZsbMIMmGNMmIXMN9uJJiLA45DurY5c9zB3802gUYkQFTBIPVISZIJVLhd4eWQzxR8asX86mjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSSj3PAV2FYssL2pGdVb_d5kgQYmKw8tqHgtYl14cJC07hpCey_LjmPX5VfZ6F2rdBtLlJiU3lCy6sWFbCkC76OclxBEgThC7rgo47EU_meZAfomIrYrek_P5ytMwVsFZAYqkMdeZwqgrDzvq0Nugr1FsLZw4AUGOMVxAgJ3EcDBpb-CyP2YC3FJ8Ibwc6tktaHdyUqjlX8MsG5Lz8kaj86XaKbBm_vbyeKwpawPmuqZxyFr6Sf-caLuX4NM_hD-_3tLk8P5M1Ig3F1QLTxK_mTEi43tZur1Vx6sSNQRyS6457tvSANp4MKBIazXkelPBBoI2RW6cu9u391sNh6cmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgheLQYCD2ReeSf0eVHifWX3FsDV9XspkTuPPiXSG2cbNqxXrDi9rel63P1fBtTDodBOgHEdKlunXW94pO0Q3HwbxHCef-slOIwRxTIPC_bv1ZofFmV3AigclhAzNuIkA_Lt08Qc15O9wv6oAhFiBHBtX1maqWzF_9Q9JG17ZdZg7eIMsbhKQ68pccgUmZbM0RunlxQR38IHJScSxCRHZ33cxTyiUH_u4xfCu2QGtynV6sRtxYXpMFKg-sWWgSV9LWHCJlZ-Ja24EKjToAE8GX4wHWgEHGajR8gAMskz6gsYYtI3mOj1XK9G3LK6tSY2IS2le43Yt2uht9tFJy7x4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rv_2zu_a2qcg3Iexy2y-61fMSvHJ1x0KnakMmFi-xDpXQE4LAQ4aOT14s5MexG1aoTMQDl0mCE1wKG0na651XpQT1saGY3om0GkFeKd_-aIkIWBsZ9HRkX5KFM7vje65IP-paYTR7qv9_2-mpQyMbnQEfA8fq3wkQUdTPg7--KIfiWcg5vv0zHtV6ysHL_G5lB8PBkFjwx8G3bmOqO7NEAumUh4dG7VOxyN9_AuPVeGRpKefhxCRPpR8XknZB4f0v9VBk0VPZ5m2jTX8FJuQuXoSDP41W0jbUS1XxlHqgEN9vMa8JDRIh62x1QBkl4ZUMtAMb7ezsjhFDyPCIqzGwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=EFIWKkmtRe4vEn2anixuwfd4NYpVC5Ho1a21xAh8bbVEjd1CThMmfWAJfxorHG3RYZoppPqC7HRjDDV-MQPpfGu16FS-x-lRcl-vELMHxPSIvBpN71UxVxM5QQ76a0SDY2dKkBWGKLDuvzBtY6WKnnPxtkZ2FJvuHhTJhFMKuI4-9vmRlcSm8jFiNHipM7rGMcA4XIX67tmBkyUVlG0CzVB6OPf_3hGYF6yjftS14CADBbJmhcRxaYXWdOJjv83LRWAhs5uvxhFRxJLsBdcfdTogfAisL54mqpjPdlmvRqpIry-N4MOlUnCu6DYz3cmV-Slq6VPsTlycohmqnOFycQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=EFIWKkmtRe4vEn2anixuwfd4NYpVC5Ho1a21xAh8bbVEjd1CThMmfWAJfxorHG3RYZoppPqC7HRjDDV-MQPpfGu16FS-x-lRcl-vELMHxPSIvBpN71UxVxM5QQ76a0SDY2dKkBWGKLDuvzBtY6WKnnPxtkZ2FJvuHhTJhFMKuI4-9vmRlcSm8jFiNHipM7rGMcA4XIX67tmBkyUVlG0CzVB6OPf_3hGYF6yjftS14CADBbJmhcRxaYXWdOJjv83LRWAhs5uvxhFRxJLsBdcfdTogfAisL54mqpjPdlmvRqpIry-N4MOlUnCu6DYz3cmV-Slq6VPsTlycohmqnOFycQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nt6kc5y5b9OT1jtwXrY_PnwqXI7UYMyfVP9_8GKO5fNi6oISuJ4GPE65LCrpc3MBD_QFZDoypcHpjd-ImjLk2vvUOeIapWRWo-hDGQDw8SgZQHOmS6cuS5mPIYkQNozQsz52FU4SyMVb1s4wsQgMfoNQP7EFjZNPF8_pZqfMT1gvLm37-ezLb1DZrwWx7qRYlGViQPVRCUMMM6N1Wjvc2ZZH4NdL4hZHHMZspL0i7AqCliiPIQo-RyiICv4rfa4eLIPZUPHa0OfwmPwofSCelYkqOj0DRZl3nByKvOY6-_6FJRKHlIixrvS1IrurXpwNbWptN-Z_AB-fFSERPojAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=YXep0QDsa_041cH4oxoLskcK9oVPs5PubSLRkxEQYHSVc4JaBNjy-9CrsFs3VxDLXoKYvviv2ilErOYGLylMmNTsII3gEqE8jaV-LVGld4GnofH8BHVu4uYt-3Aqrouqc4fIXFmb-Y-f5c5J1a57m6ghXf7bYISjIvriI2rO0ZGvkjIdq5JsQECaD_8odytm8A3BO00WkXU11Z7NYX390O2s12XUr5VE0L_Pw46wmD4WCS4m3Q193Kizt3qOTtWPrPlOUpLysFDePdiVnnTYOP2M1ErcCJkLqbrfMaa5FG_Z3uvqjRfCUar6Ja4F95SFbYZiXymZ_XQBR4-rzoCMXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=YXep0QDsa_041cH4oxoLskcK9oVPs5PubSLRkxEQYHSVc4JaBNjy-9CrsFs3VxDLXoKYvviv2ilErOYGLylMmNTsII3gEqE8jaV-LVGld4GnofH8BHVu4uYt-3Aqrouqc4fIXFmb-Y-f5c5J1a57m6ghXf7bYISjIvriI2rO0ZGvkjIdq5JsQECaD_8odytm8A3BO00WkXU11Z7NYX390O2s12XUr5VE0L_Pw46wmD4WCS4m3Q193Kizt3qOTtWPrPlOUpLysFDePdiVnnTYOP2M1ErcCJkLqbrfMaa5FG_Z3uvqjRfCUar6Ja4F95SFbYZiXymZ_XQBR4-rzoCMXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrF76anqSBn4GBsXNtwg2Y2TtQumHMw60yAXtokfWwxcF236c9x3975cLB1DWqYbzmu_2loJJ4Rp8WVxcir3pWUOiYZRXVwhjYPogiN_a_pxgzEroltVdXDxx8fgAL-lr-TfZbW9EgfucgAWdGu7Ag6_VC9IoqEoaCgyiCWQo_AKUroAX5BYxOnkYCx-8cDYrZaL0rDNA79MUN1MEFwyU5Kqzz-RwXWcKZ7RpUDA_H36-HykbDJsiO9Sm0dg22zm5IIxeswWdZTVdKuhCpHkHQfM3NULMuQ6C9QRfCWSO52-3e-nxRynp_d2DvBY2ph9Gk2Upc_sUNEJmEuHJNdMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=a1n7mXDLKbvzNqMahq8YTGEmuU8aTj3bhmpjOCyR7ZkptjSSwvQmHgnHOS2UofjTOjRa3dQ4MUb-spxxnFpvJQsY4qFpoyHtzU1dKXU1AH2dw_S0gKMzWsQviWogleWYQrv6H87VyznRTlI1JeU4SY9jUqk_BgogJ8cGpfwSufRsny5Iva0Fx5ZNeAxD4p_KpfPJgH5JZPkxOQHkeWez_xmIU865DHNtQW6nU-T8MslEoktbqVedcybB1_-lg0XtqlE7FFG15FcEeyT8_P1lU9-0Yw5u40inizHJAd8OHpkXaYGMDmj2lraQQTnchyXE2RUSauEfDN36FspmJ4f-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=a1n7mXDLKbvzNqMahq8YTGEmuU8aTj3bhmpjOCyR7ZkptjSSwvQmHgnHOS2UofjTOjRa3dQ4MUb-spxxnFpvJQsY4qFpoyHtzU1dKXU1AH2dw_S0gKMzWsQviWogleWYQrv6H87VyznRTlI1JeU4SY9jUqk_BgogJ8cGpfwSufRsny5Iva0Fx5ZNeAxD4p_KpfPJgH5JZPkxOQHkeWez_xmIU865DHNtQW6nU-T8MslEoktbqVedcybB1_-lg0XtqlE7FFG15FcEeyT8_P1lU9-0Yw5u40inizHJAd8OHpkXaYGMDmj2lraQQTnchyXE2RUSauEfDN36FspmJ4f-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcrAIomUQ9siiqyLXJeaCiPpR_dBQ1CTJN6OJW2thAkb3hTeB1eQBUqYsQP8UYd4iK1LAZviYrG-yk2Df-aXUhGdgFKM2vaRhMySjgqKz6VJI_OPc8J55pN0a6BnDH7cOqMrjFwnj52Ow8X6HsZEIeCLblaiiORqJxrnP3Gs4UQ2Eu12EOSKNiAG1_Dkv67UaAxmYOPCVAL4wG3PF32Gi06_bZIH20Tc90rFCiG5rDyXySb7QRoNYgCNRMEWx3OljO5hw9SwpZKuXqw0q25KKXtn154kCxmUmpHqAvPUln21r3OEoafojxsU8lq7D5rhhnpKJIfVDMhp7_1XYxwTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS_CDJh-9OxmtVt_pDj90yzCJ9C29tgjFYFh2MOvH2eSPw8kaAav6ZyiCl2AfRyeBahdBSaUb3MUp25C-aBErgdWajP2PXRjyFYAIRVlnU_0KNLqYDD7J-1RIzChs-crgij1kR0SQ7xBQQKYd8PJ3ae2-SFYtjS_jJQvpoCXs6_Y08tliwsZlGRz4lljv_AIBhFhfE4DbIRycPxD7_yJMVr3RMwR_rdXXTkYUxht5qsB4PsQyaA_bGB0Adglmhl0coviO3G50Qlfcd7fPOYQhjHQ_2zFql7-LksE71Uz1NK27XuheEuBxuqXMFFLoaTqiyMHVmlugPqJr_4T_WpOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEybPKR4SGAovaAtRSWVZfdtJ04UeDsz14M0DW9ZYCglrXvjo_AhaARwXwuSI6oxn9jgL83EDj91n2JwFgEjaXu0V8JSppKqHwR7N5k6LR-qFj1vX4LpK_F8l73gxcC9dvDsnrDQM3m_yqhS-ZBiiPAzs0d5leJDTlzYMXYiJM4_RMJkQCB1Utr004gY6bt16Xz6ihn01sUmZR6knxmPuvIPAwoKbjqksMoB6x5mWoKIokDuKc4RDe_Lk_sYbAhcky1C-QDB-Svs1tMYd0-LqqyYxuSz7saTZcTxvBfHOXUbFwv94CFyjcZBUzbW3uEWvIZMBoD0NOlQ_pw82mR8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=CSw6xQCm96cXfW_Qae3JwwhoilIClgoZzjtYbSt2NbUK2ny85gRSK1Li44YJlBc7Da5EO9tNx9cq7d0JeqIQrsjDQFOd9mD7eru6Kk038443Kq2dR8fhqnh8o4ehyUcemvuDrfOCUWLG1tO57UUdgawD0JiIFjsx5mGXvh4epVQx27_YdabvXqyndWoJtBlBrwPQuVba2zwDnEHqDom3_BKQu0VVg68cYzVTOnxVq_mOycZ97IIbdq7-KMjjhSEaF9BpmgA3S_WuVMMIyhTaBC1-uM3utPSoX8GuxuleQFOJCulcgyr1u_3sbrUuysNp7dxZFWfk00mhqEk3ujBgzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=CSw6xQCm96cXfW_Qae3JwwhoilIClgoZzjtYbSt2NbUK2ny85gRSK1Li44YJlBc7Da5EO9tNx9cq7d0JeqIQrsjDQFOd9mD7eru6Kk038443Kq2dR8fhqnh8o4ehyUcemvuDrfOCUWLG1tO57UUdgawD0JiIFjsx5mGXvh4epVQx27_YdabvXqyndWoJtBlBrwPQuVba2zwDnEHqDom3_BKQu0VVg68cYzVTOnxVq_mOycZ97IIbdq7-KMjjhSEaF9BpmgA3S_WuVMMIyhTaBC1-uM3utPSoX8GuxuleQFOJCulcgyr1u_3sbrUuysNp7dxZFWfk00mhqEk3ujBgzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCuTwXVb5VINnA_RLE1_6x4tLkJhk45MpYrol1OmrqwyHAfZ9KTuzsGoVZ1EvoDXbtqoBYrbaLp36MiZyAV7e4wpPleJlZfYARWTfuBsTHiNOE5yqVcuOCf3bWwlT7KUEhcTy8qZ_nCB5ColB7E1zDalFYBvkOyOtWhG-FIOSB4njk89cJqlvoY8_WF3Yfei3jSsErOXSLp7NUMLMFP1ZnLt67oRo0aFuPgoiowsHbfDWJs--aSHimgCsDyUDRfTdJe3s7reaSHDsc6ZzaFgQfF6FOeWqo_j3FEESjMIbyNDKoXFiOL6KQYUn13eIpWyPg0nO8yhVIb31hhPKljnQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhks3PeCLTRYOj9pt5bGfKU7m4KUvWoWXN14KYbNGpKNjDOki6MdqQFPQLFMaiyFIaKJOQgqX1yNtiGrlcZcL6mFwToMTHvg0KKCB2ptYPfT3riPehN0LJj8i82im75B7PAnJ3IZ9KF1FTQHBUOFZbSDnxy-qdo4t0YL4b6CRdtmwQzrkVQrlVJfcZRLbqcOmW21WygGawwJJO8YrgH3FPf6IAtK9EpuAu4xXmFOfNJeBzmRtISJ91mdbNPg9z-GtCMcqCsASPrLbG64v6j66dRpdtL0HMr-xf2VL00PGZlc6c067WYtozj7JkwIgxssv4PbdvPZzJ8uhLn0DdHpiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwI6n5WuE4WKh2u5GkvzK2HMd---SEb55B4_-EtCmATufWSnbGIIv1vt2nLwrL-VvQAGMXtYxQ-_NF0JprfvUqUlDT8G-_wJ36905bwA01d771ywHS3R2RKNqzoBB6sAaa5A66UBadNU_3O5PZ0sC2DHzpI3nJIgX6jgMLeFfQ0QGDKpt_a-DMBhktAHVUhY8QF3P2PCO_Jjcy-5EULeLkQSo5Hf1jiTsc7KSbRdj3_Ja2b6m6lPuc0F_ZV8JRAtuenmnXmyFQmMcuF8e0n4edx3UR5Q9poPdcw67VFVHzvtQEA38q4ENXQE_gITx9d5QOYBhlCZnZIenggdx1uw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0LTIrxioK436eF_ojgd1g3iq8d71X5Bw9oIPBysKNo0J_fyRdOHFQbUeeiqZOpFTyum3D6lwMzMYeXTR_p4guAUgjJrjr_N8edaMnOGyAPYs6BZNXGIfgtDpVXmsbndn6q48ZZyB7Xqvb6CarSTkIxC4MdZZKKrdEkXbt8lSNXXwX-99r71JpszODHckVgdey9gqdWl2Uy9EQX9Y9zF2wf7OnawKjyBKFRJF_tGK6alZOnHbL-NAPSJAhUQlbVuq448X1CryGB8JyZEug6tRr5mcP4VH24OdZtSKPSKaVmbghV1a9XlK6K67xXwEIfl8Nd1IYDVdE1VjSI-521eiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-Iq1-yYxXMfEWWbvzGQO5ocDKLLvP2S9OXi_aQJ_b8MhbJkAUo1Efbl8epqgkx03b8ZkpRPJgSPcHC5hVI9xRer1xR1IvEVY7CcidvckBrpD1rfqGs8PBc9YNzlO6JsJgPUtp_hPOxpSYdRxzuYBqqwf46k2Om0UF83S8I0rb6UbxAT3iMmZJ0nBC1cJ-68-pOWWUaCSui5hIGDodraRasA26lIkOOSq9N-6NlK4Jge6jbXrF62h8Y9Bm9B6XerBvLtqxHVplkn5dqvkqqA7QnsL6wM2PPilcgz6Qdz-J4NGlRb_2zT0MjaoTT_PncjIsBAcINk-26KMR_4Q5fz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOi0qS6EA5TnTngacnyYg4gPo3cAeBV1ZFddHsUIgyT3q46aUMicRiSWj_9mnOAd1lggVQA2G-ZaaU8wJ8TMBWhYeti6IdIC22b2AzsWGuY_NU9qNtWLRY8oqc7qoleRvI-DuFEdLVdGq_HlJQHYIGyYRrwpJMd4lZEKaOx3v5CrDiEDvvu_wznFpnKwaq_j5WhlTC5-OBnqvsd0hMcxM-TBxnqXJOgoy04cMrVdsiAkL6IwGNwsdHYKLKjMaL_DGx5rPiaXY0Qm9Rfelzfl8vByDOCpEpVYEZM1o9tRJ9wtLu2AXEI3YfQu4uj7XO2AChQEFrrr020hWE8NnXDqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYOosk4GJrn0ppewB2CpVxIi0AeVQ7c_RdjsMlD-Aecfp7-bZyLoG3rwkzF8REkEvRKyXTuGO1a-PENkmmGt2Fqs4iC-dquVoJyW-jEk2-Xg3989PwLer159BHX1v1YeH6hsvneyYRc8buhs8dQ_y-sfaWiTuqwsgWyFGuI2RD-HSHLUQC9cie_cAMgnlGHQ367HqVQ2Op0z4g24zX2wRFStzy2hPyViyNdFuUm8elRfSOE8LwfK9Z6ZfaSbPA9HSUOn3lsv1pY5jmc6gK0nncZUAfaW50ArKZH9Xdw8mKKXcP6yQykWC2Y2OmGsenNDj2zYtlNa13FH3fuQGS777w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmAydI8mkMZnC0KqjA3GLvIfjMkpekmlLzRStxoj9ytByk0pKheUlBGExsbW6rhxEmOWI1ULCv79jXqjij3EWdOWwOwUqzOBl_Xpz2TxKBxlXTduv35onATMR7OcSV7lfWWnM_LOIUZPI1JIQmUkAVsFuHdLxOsWJMXsiZtwtjjJbbQ0Nypok81JI28Ytml7tK-pIyNVQq85Jm9M6cTRE1BC0Ca_x2dnBkDb4GWOkkcqGJndkEYCn4xOBfS9GM5BBg6TF646g_zpI48_gyY-K2qkD52YJAw33u9ZM97en29rSqbOBxJzd31j3fg1DiN9lRplB2-MHtaSF8H8AmZHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZt02bXgoT8Kft32v7_8-ZN9nhLvgnbUPZ2x06okzQYyZulGtEfrLn0khvdpMRwyKN9dLcnmY4hqol2Us5L4wyWvK_Zw5UHfdoZdBjVJZIjWB8s04eJOeYfRnqH44anBPyelJ1P6homvP3ufeRlxUN0ZRGLEAsRC8S8UZcCfcrc9WBuXwi0fiCuBDkoTDL2NcIX0xxQazYMiWCm3FIgBbkY-OHhi4vRSVpZEbyQLs7nZgl1xHWMgfGUDK57B_BWxLBUYrByquvnv0lSrfPWSNxzVJhWczfVnqNWM1MTPI4NkDpNBh9hR5oKXxkaZ5GfeIcGqOOWynadEGqJKycASS_9qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZt02bXgoT8Kft32v7_8-ZN9nhLvgnbUPZ2x06okzQYyZulGtEfrLn0khvdpMRwyKN9dLcnmY4hqol2Us5L4wyWvK_Zw5UHfdoZdBjVJZIjWB8s04eJOeYfRnqH44anBPyelJ1P6homvP3ufeRlxUN0ZRGLEAsRC8S8UZcCfcrc9WBuXwi0fiCuBDkoTDL2NcIX0xxQazYMiWCm3FIgBbkY-OHhi4vRSVpZEbyQLs7nZgl1xHWMgfGUDK57B_BWxLBUYrByquvnv0lSrfPWSNxzVJhWczfVnqNWM1MTPI4NkDpNBh9hR5oKXxkaZ5GfeIcGqOOWynadEGqJKycASS_9qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8428lur9Pwi6v-OAMcZhZXuImxR77OwSTDWLRZ5ziZ16b6u8BH0kV42z6GcroOHxhjBkWtkYUU87oU6MfVzkLCtA13MAmzH1eglGFs1OV3_0kEu_P222m0WYQPy7LdEjvCfZCO5vC89kuuvHxo5YljCK45euEkwZ9Jrpb3TFieHFkCukQBIQ5Mq-x0dEJgVmqoQo2N0bHae_tzkSNKBOAdCZQedKH8pgdfNcxBS5zYU1tY6rgSIBeo0fUn2VuDLoKHB2Y50ijewbpKU0bx5sRJOGuoHHcSlKPenmsuddQoiDVZYMJAWl0TIB7WqluBU4qlQYTTndogI6eyI44EALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1Iacjr4cvGksyh1rCVsryuf72HIBzG3-McsnbfskhVGPap6Mlihhc3lq-gdARHUifsgE_yIiBUDBPtoCiZB3Aihi-Gl6vOVqUJkNpo36zfZHz1SmWXPjNgNHZrVtz9PltQZHhdMeldPUyWZWkopfr5rXAay9XLH4eHCI5cBlyPjtHI9_VJGD45cNFdeGTSqUXKlukInNnBf84H-4-k2HvlpKPhIOtGwTAzwhZNbCtlZG-a_JkyIpGXsOjuAiGlF5qRAdiiI4v2sCj9cGXv0VX3CPpm4e2rSBeYlDDQEgXembTkSuGGZ4kfdofS-y1vvpGJvO3G44r6djth6AVf1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=AGEgvh0OQhfpU8gkgL5tGOTY_oBVN3w4qqn6CP7bvkKU5Wx6nEjLZVzvuZY_59FlF5C0WT6Q8dK_P_8XVKZB-hW-puFw1oDI-viVsLWR4NII3d9VlNS7LO9GP_6ObIG6mQ3p-5E6UrQaLio2c8i_oWVi8wO7ODZEwen0NpH6-eSoB7IEkweW-wrQpng08b-2zQobnb81grI9StWekHilGAnTmCOgF8zzQBnjUKg7xrb8RmBWx1_HvtuiZSD5zKkdALKDNr2UnjOM3AlYPhvZSz2iyr81YFYQV6BQ4JHD0WerZYUbVBFDbbHg_ua1xcjqcdEEaK5daOX1c2yRM7Gxsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=AGEgvh0OQhfpU8gkgL5tGOTY_oBVN3w4qqn6CP7bvkKU5Wx6nEjLZVzvuZY_59FlF5C0WT6Q8dK_P_8XVKZB-hW-puFw1oDI-viVsLWR4NII3d9VlNS7LO9GP_6ObIG6mQ3p-5E6UrQaLio2c8i_oWVi8wO7ODZEwen0NpH6-eSoB7IEkweW-wrQpng08b-2zQobnb81grI9StWekHilGAnTmCOgF8zzQBnjUKg7xrb8RmBWx1_HvtuiZSD5zKkdALKDNr2UnjOM3AlYPhvZSz2iyr81YFYQV6BQ4JHD0WerZYUbVBFDbbHg_ua1xcjqcdEEaK5daOX1c2yRM7Gxsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrmPzpzWNAc_423nAlFgU56i78sjOUK9EXx-buAGx-l67R6UJhrODdGI1U6hG7y3tdMc66kAa_EB-rofufL-qnf75kDjVkGOtz0GaepSGYwk_VFw60BW46r81KmTeq-FolDjxve3oiFcFJPCmXiPTmmVzJH9FeUW9fguAOmYAXx2td76S4HAV2GOyA2GcOtom5d7sikm3u1GLjH70n_T3n51jeUOuVLzqqU0DfESmFVU455HWAqbacK7JcdryaZQ3cgyTVy54Qu-W95tQCivRouG0uLJmZo9Z5MG9DyvktakvOznRQEc879BMPWsImVh5ZsmEoQAfz4WWOMsXrcGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxjKb4zYYTSwRX_mzj6ztO6UM1GyajtWh_aw4qdpj5OV33giKQYUyI1zpR_a7DvNyWxWdXbIFcnVv-h0gCUe0-6iUrTsGDLcEOTqNQo3iCiS3fFO6e_fhbfzMOgPuJy1SDQ2hr1_CIInelzotVNgZdyfU8msQzhWYbjzD-YTREYwFXltdybVTKB04biqkHpUfTYSVR5YLpgvTTWmEMDBd4Xe6TU7ho-dn8MqBMm0B4Hs2yrd64mZYUrpaj8dMp5HnFlsrzwFbgmjY7Y2eYJt0mTbagg24EU0XQxbTC_EwS3XYF8zPhPYAfiqW57YV3OLEeeMcXoIPMyh4pMf-FnUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=Ecy4gzVLhy6gsehIzjyBPqs2o-FEEQBfcikNHS22H9moBgKBEjFqoV1vJMFAHMoKzgyxn8-geI7jGlqqKjI8TMslQ6B6m-3cJJXtndy7u2PRThj9CJadDkcRAH5POcGcTNuLkj2Foe5GWd29GBfvQKX56eiJkPJfb8fqN5qIYPxS_TNLBvKhaBGuFU_vRH24iXQoxVhFz2ZgwU6zp4XS1Ejm0_P-WGqgoh2HQZU5BsYW2NIRqlXQEh5lOZEsZ7XY9FqRxmMyPOag-BEfxZXCY4rHZMZ7zY4YntMnU1zghQEkTJPTEgsI-6pnXMktOPnYyGIC5Oc3-HD1pTpoNTfZsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=Ecy4gzVLhy6gsehIzjyBPqs2o-FEEQBfcikNHS22H9moBgKBEjFqoV1vJMFAHMoKzgyxn8-geI7jGlqqKjI8TMslQ6B6m-3cJJXtndy7u2PRThj9CJadDkcRAH5POcGcTNuLkj2Foe5GWd29GBfvQKX56eiJkPJfb8fqN5qIYPxS_TNLBvKhaBGuFU_vRH24iXQoxVhFz2ZgwU6zp4XS1Ejm0_P-WGqgoh2HQZU5BsYW2NIRqlXQEh5lOZEsZ7XY9FqRxmMyPOag-BEfxZXCY4rHZMZ7zY4YntMnU1zghQEkTJPTEgsI-6pnXMktOPnYyGIC5Oc3-HD1pTpoNTfZsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxL9i28jwq1Aqqekm9G6QKKZews8aDDDFrE-S9BGkzAzKNLpoQSO-s3Q9L0uUuYYfoyKfQhii0bk6Xr8fYQOBRDaBdG0gTxfzMMvQB6zlOTtaAZekBUHq6ceB_OnlHWRwHfsFVGAMF7LbuoHHcXA0INtKnxuGHG48mVTBo01OXKi4uqHBaqk6D6AqJR3hAe6Qk42HK7uobzp22Pbr0lGAMrzsguclVoYmQxN5-uuUMvTKV4cdvU1OBbGSDKlVNx5O1BPQCPX8d95O2Il2f1goPrhkkBVNsurJruqQZW-WZklcNst_PHfbXI3a_hMz1Z1ZHnJlY_aaKmFyZyVh3rtgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=Hju4KqdI_iLW-1QNvSUYFrv5bR3r1ak1SfMZOJpM_vJpmN48ZTTgbrDoV7o1WKWZapfm-7BmFtSWsJcUumY_VZ1bH4ZBqmFOun8qrrCrWjvWgXKc_PgXZBCgDVUqwqdF0siKQDyI4Opa_XDbLDSAxsvhxw6NvAR1Edg4K9q9ZQTOlz3vsNSNdii4zLHGMufgyiXU9rUT8GLQX81wtHwwpSVbAa_LTwVlT2vQlUuGawmtj4Lop305y1kqZpLuW3a2-nMGQ9Cw0DXpt23-9bcChxgkno-Dz5g7N9Y9LOIAQQ5jki2y6clMr-rnZq0wra6Je7XavNFIUH_0Hkss6zhTdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=Hju4KqdI_iLW-1QNvSUYFrv5bR3r1ak1SfMZOJpM_vJpmN48ZTTgbrDoV7o1WKWZapfm-7BmFtSWsJcUumY_VZ1bH4ZBqmFOun8qrrCrWjvWgXKc_PgXZBCgDVUqwqdF0siKQDyI4Opa_XDbLDSAxsvhxw6NvAR1Edg4K9q9ZQTOlz3vsNSNdii4zLHGMufgyiXU9rUT8GLQX81wtHwwpSVbAa_LTwVlT2vQlUuGawmtj4Lop305y1kqZpLuW3a2-nMGQ9Cw0DXpt23-9bcChxgkno-Dz5g7N9Y9LOIAQQ5jki2y6clMr-rnZq0wra6Je7XavNFIUH_0Hkss6zhTdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDMwKtlpJlQVlciC5YUT5Fq5GDbpcrFpiVpcpQ_wFYrmWbslsGZwTEqENfw0gQMFYYf5VGPRv-bWmWFxoGX0ppfwgTldyT5vcT2yblOg4P34aEQoL5-32Iyj4kRpDnJ1-7FqslnXUyLenP5LN8trNYvc0rmE_WGWQKfntim8nOtXcycnWW5K_YkxUEzGigk7cSFgY9Swb248dafapGz3cN4xs2tGGn0laMb0Rqasm00UPUW5WmsLKHq0ZlDMHzVGV7cnztl48H_ErlD4m4H_FPuifyQqt-XfQIqxHoXYGJnIWLL5gOw0DWVKsTPvyEEgyGnfQ1WNhJV8PQfoyGUblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcHcEHQchphS3xOoSdaNJubPeJpyv_EKJqL1G_5cpSymdJkiKPEBqYk1sHVIsj2-pO5emTg58W3hSg3mkuf1uQe1FbNjVQXAAhWYkPiVTPjrS9K-ANVK13vX4d_TxmaSiQWIA1xYOKXPhc8RjPOZr6Jo6TW0Om3h8U9TuWu7fJ_lgfvV8EGDeFqG0ALmDAlIs7lJloJ0v82dzwIZr35Vu8KoPTMx6ccGPWjZ73GQ4rzdN-cHAuCt0hTmWkGzbh2sBZ9Uwo2Tkd-_G4LmKOZqeYlD64ywF0W_HtQo8fyqfWldejZh_TDxrzTsmc4Ttn5T2LkWqosCmknjBzxvTPtckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=Q0S69JZ6WBJZn55CKCiWJANaM9TrHSYVqs1iEi6BRue8c0QluP2IvdrjyzrXu8fFOq5-zYLPzxcI38V6Gga1JEH4XnO9Cy9qNryWOJkoScekOSX4bGcw4SisKe8Sd9etlyBr88iB9USCPgPqkSsAZPRfc5kJaj3vd_kmxjQUTguOSKsE6iQaD7i6r-T16XVv1xS9JHv0OY6USKrLDPM5YBZ8hpReNLS6pp9WXhdTTRekqZicSf4Z0tjZ6nTata86q4Y9X9PVMHc6n0AeZuYz1Upe8naRGCZ1dvZswKnBRctmaxaz-TqCuLlhXCwG3Xl-0236bNUC5eNDTwzx6q8UCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=Q0S69JZ6WBJZn55CKCiWJANaM9TrHSYVqs1iEi6BRue8c0QluP2IvdrjyzrXu8fFOq5-zYLPzxcI38V6Gga1JEH4XnO9Cy9qNryWOJkoScekOSX4bGcw4SisKe8Sd9etlyBr88iB9USCPgPqkSsAZPRfc5kJaj3vd_kmxjQUTguOSKsE6iQaD7i6r-T16XVv1xS9JHv0OY6USKrLDPM5YBZ8hpReNLS6pp9WXhdTTRekqZicSf4Z0tjZ6nTata86q4Y9X9PVMHc6n0AeZuYz1Upe8naRGCZ1dvZswKnBRctmaxaz-TqCuLlhXCwG3Xl-0236bNUC5eNDTwzx6q8UCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=DmCFNzLbpkbHDQVbQQcDMKCD6Nx8z8GyzP1xVqqTTne0Fo02Z4y-IbtJ2_BOAcETQTELApseRCNchrjVrImWCiO6Zxzr6bxkmsQqjt27_mkkqcZnbvXotVFMvMkfYgG12ntIcBJ2ngoaXaYh3Op5Te2F1COSZ27MAJ1XQYyqkqhp_G8xrtXdnLWg5888m-d-eiq20xispNN-vRHkr40b2SCIGDwhSPArc8p6DgZmfRHV1PSGyGGV-qqTPx-mhPBbOcDJB6HgL5XgsbOo4u7GX2Z87PeicJ4yTvwFbkRanmSwgoEhnjm3ICPWL9rgHCuxOLBLHbwawNLLoqmvHwGUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=DmCFNzLbpkbHDQVbQQcDMKCD6Nx8z8GyzP1xVqqTTne0Fo02Z4y-IbtJ2_BOAcETQTELApseRCNchrjVrImWCiO6Zxzr6bxkmsQqjt27_mkkqcZnbvXotVFMvMkfYgG12ntIcBJ2ngoaXaYh3Op5Te2F1COSZ27MAJ1XQYyqkqhp_G8xrtXdnLWg5888m-d-eiq20xispNN-vRHkr40b2SCIGDwhSPArc8p6DgZmfRHV1PSGyGGV-qqTPx-mhPBbOcDJB6HgL5XgsbOo4u7GX2Z87PeicJ4yTvwFbkRanmSwgoEhnjm3ICPWL9rgHCuxOLBLHbwawNLLoqmvHwGUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRDaLKWrvVgp7ZWhKJbJwjJ5md9xLl-2ZjFqNxIsXi9ZErifSVgQC9fgUhtts2YuOwbx2aSi-vHmuuRJPbaommvHEFNPdMGgZGtn4UvPPegMQLdse658ErRFct29snkx3N7Ejiw2XsRPK5BJ0n8R68oAP6zVdsChWT5XgQhzoAXUA1eytx_bI5WWZe8kfiTCVHBFg5u0cRZGR7njjFeclvenkgXwubvkBAu6Q6gQxToVkJqYkKimrYKjMCJBLfqp5LF7Griu9zOCN5JbaJdO1edZ4HtZl5Wu4Wxrzb4KTZHWl5HzWbaPWdTE_crT_eNa6_0y0RSQ6RbAkk8SEgVNtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l25TE3ZbT3hQaQtTQDua7U0JQVIG_9QxZ0AEEuzfa9N_COp8a2534CLT6o_YPBrSQi1GpMQceSPl3P4jBoVpJGn5HCRofmrWPwToN2yxrz7R6shJXXoyb-geCGGXIQwgaIiCcuWpTUKZFix-PDr_ZHDqFjcxjCBWfQNJYvqIJGmX3TizplFnVPpGunmuuSkrp7JTDcj1N0uuIP1nttzzgn9dSZz43izFHuVWYUjqGROPrHoiQQJv9w0-fV-znjndqEMGy-eyu-_iJejJNQcCV9taTeKWHLh-mb-BnpOZwcYi-Uy8rz8EVNwPCje563ogUWixZitDPL7MkcnP11Q4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9J9s7E-phWdg4BoDXbodnAGlq9ViSlnvkfantdiWqNrGBpcolD1TclJIdP5v2Wm0Co069bkuGJWT3R2hhBvKErMP0AIZmpcJSPzM8eQhbW2xiJtgVoskWN36okeNyflpB5cNXbxAZMEBBabRAo1x0rT0BMJviPY3t9oFeN7pzFNwKzQ7lppJP7ZaPcDMgZaAdywTJ-3lADjNIsFn7b-hBOQWuMJuem_TKDQlQ0dZ9ZyaOVZ8xjZLZZJfrzF0NGkFg9t1x07CoLx4ui_IJA3obaG7ftehsFAmySd0liv09slr2NCHT2e7AFcZE4dMYRT0y-gm9EHczx1YC_BWWsGYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=ZKGy5D5x-MwSLBSxj57E9s9PworQAn95UcEl-okPGKvQAXTGMdOJqls-UgElsiO-527sE8Xsdq1FUCl-TFZ9QLHHZJRr22KGNlU9dsYNuzLaHxA7mZ4RCA_uNwuA80sKdc2Af1B5_L7RXgEsA32mjxSx4_Rh_MglDihUptLouIaPgzBJoqrh__iHLem4avJCzGX4oMlMIoqZYvli3adnfeA0_Tk5cnPpDBPYfOu0PCvOlouwQoKfcznFaNSsnjvgIWXoCi_VXvxKfgfQjqVRRGIZTdc63qeDa3vQ1taIMBgGZiP2WOBaKuACXOyTPTc0STQov6z7i4EtM-hJA8TMVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=ZKGy5D5x-MwSLBSxj57E9s9PworQAn95UcEl-okPGKvQAXTGMdOJqls-UgElsiO-527sE8Xsdq1FUCl-TFZ9QLHHZJRr22KGNlU9dsYNuzLaHxA7mZ4RCA_uNwuA80sKdc2Af1B5_L7RXgEsA32mjxSx4_Rh_MglDihUptLouIaPgzBJoqrh__iHLem4avJCzGX4oMlMIoqZYvli3adnfeA0_Tk5cnPpDBPYfOu0PCvOlouwQoKfcznFaNSsnjvgIWXoCi_VXvxKfgfQjqVRRGIZTdc63qeDa3vQ1taIMBgGZiP2WOBaKuACXOyTPTc0STQov6z7i4EtM-hJA8TMVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qm3jtIbLpTjRe-nilGjZATyWL9RNdssWcAjep1t8K8OUb_a1IImArgiB3IUO7KrXBQu2XmmiaBIrJe8ArQnJz8HO9aLbggZ1A2dvUj3WGWbbOq0qXoJ4BmhoPgMxKmEbkjug7WEuungSOFCiG5R-_4NvB0-LnjB1uSB4WPfdbc8dY9mzHL2jzQKvM5M5ergHhZEFjJJe32yaNUt6DaGd_vPKO837E7xSfmgWULb7TxfQ5-5QK1s6mXXEJuGmpWwbYGyfDuxCUuJi69b1EPxFyqaD4aT-XxBInPNZijPB50KjJoD7WFGuirlTrAy6whF3gAiCBCr7vTcLbOepre51nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
