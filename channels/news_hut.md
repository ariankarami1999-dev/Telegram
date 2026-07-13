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
<img src="https://cdn4.telesco.pe/file/IiwktjHCndONpWMQmVILs3yArRzo5kcY5jRWi9tZXtuIiWKdvPtwsbbjHhpz1yNQ9TfdvH_zGZlT1-kECSoX2mHVQJkFbfVsA-QgiNQCKbJovCWiqCzhnU682-710FkBaLeItKLj6Q-eKd0-cDART6ryllTXGBkauIJQqsxytB5G8ak2XVfT_MsQ4_o_07SBmyYsIVO4HwwOf0tFHg9jIq9FVZ7vPuGrV4gZwwrv1P7DkRSQGim36w55DBiW1aS0hvBJI8mj0bmPSppEhRUneW7ao1uyQHWaRyHkDRnXSu7GK8_4zDtsqullixtph6BMbSJKCDiS0WaoATp4Shxbow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 176K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-67993">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a38d8e8e.mp4?token=K_mg-Bfw2HGFYq6Zu4jgonQqrtPCWLku633aTV37lpfTLev_1jcHISUNHamkeCKv1MOujl-wiX6O9PwnInEv7z-ftmVFegPqMkfotKv2Gl2ifAz6bg0GA_FzvjaqoWT8-GUYWxQlOmAR4qssI6O0qMsWBz5EU5Aj_t_88S2ype7krXRi7dUpDGz1indSlVYej2Alv2x8YvAocDaaL6Qjshza3lNNrpZXSxNh6cFsoh4vzTzGXPDfZw2azwQ8Yk_WtT6dBKNqLichD45CNbKOS5HSjQIl4q82z4agBMl6MKr5vK9LeVr_ZyytquA9mVahRZ3vQ2N1rx9I0pZo_SSkHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a38d8e8e.mp4?token=K_mg-Bfw2HGFYq6Zu4jgonQqrtPCWLku633aTV37lpfTLev_1jcHISUNHamkeCKv1MOujl-wiX6O9PwnInEv7z-ftmVFegPqMkfotKv2Gl2ifAz6bg0GA_FzvjaqoWT8-GUYWxQlOmAR4qssI6O0qMsWBz5EU5Aj_t_88S2ype7krXRi7dUpDGz1indSlVYej2Alv2x8YvAocDaaL6Qjshza3lNNrpZXSxNh6cFsoh4vzTzGXPDfZw2azwQ8Yk_WtT6dBKNqLichD45CNbKOS5HSjQIl4q82z4agBMl6MKr5vK9LeVr_ZyytquA9mVahRZ3vQ2N1rx9I0pZo_SSkHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇺🇸
سنتکام ویدیو‌ ای از حملات دیشب ارتش آمریکا به اهداف نظامی جمهوری اسلامی منتشر کرد.
در این عملیات سامانه‌های پدافندی، رادارهای ساحلی، توان موشکی و پهپادی و شناورهای نظامی هدف قرار گرفتند
.
همچنین برای نخستین بار از پهپادهای انتحاری دریایی استفاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/news_hut/67993" target="_blank">📅 14:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67992">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3c5be180.mp4?token=a5bPe4AhiUI2yvLBIdZFxBo5twJX_px6H4lbQipzwkzU0gWB_zi7mqcrnVgLDbk29wvV5SVrHw0zXt43tu7nz-iDEkuQwqJmLFs2FP4ZKuB8w2wg7JN5S4uQozNo_pVG-yhYUUjI7I0v5t2U_-H6WB6bai3_oPq3wsv8b6OIyWm4rmqtnda6I4Cf36AhcW-WnJODZUopWOuyER-UkfYOetPwlKWkUVN75v4mY1rTTeddtIGdmVnvbWqCKKAKaBW67WtDtK34Lnb59LXd1qZ1Naa32d2KslsRgWl0By28oMKlrVt5vLcSOR3OF-VbpYmoBWu2vdgzlsiPi1oFIc-DkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3c5be180.mp4?token=a5bPe4AhiUI2yvLBIdZFxBo5twJX_px6H4lbQipzwkzU0gWB_zi7mqcrnVgLDbk29wvV5SVrHw0zXt43tu7nz-iDEkuQwqJmLFs2FP4ZKuB8w2wg7JN5S4uQozNo_pVG-yhYUUjI7I0v5t2U_-H6WB6bai3_oPq3wsv8b6OIyWm4rmqtnda6I4Cf36AhcW-WnJODZUopWOuyER-UkfYOetPwlKWkUVN75v4mY1rTTeddtIGdmVnvbWqCKKAKaBW67WtDtK34Lnb59LXd1qZ1Naa32d2KslsRgWl0By28oMKlrVt5vLcSOR3OF-VbpYmoBWu2vdgzlsiPi1oFIc-DkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تازه‌ترین ویدئو از حمله هوایی به فرودگاه صنعا
@News_Hut</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/news_hut/67992" target="_blank">📅 14:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67991">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbYr0IKYL8l-zp0C9RSDh8ZELAE0N_eAdDFkMSoz711-okHflwgTdzk7ViJuOvNqlPNJdRkzrJDen-VdAoGh7yeIFYXcvRB-d4-rPKuEbHTRr_Kn0IshdgVWVJeWrX9-3TF9AkfFvCDsLewLKiFuDSGN1DuXgYdQf7DqR3F2ygVjuCYefCm_KCEhcMmXj4-LnEvCQKpkyu27HXLgFg2Bh2J0b3L20A_skI1DF3ARuSLr7PGdmKErFcwEJkje2S1L8qAXaya1aa8PXv57u0bbozrIVLg7cO4OMqNmINCnz7tDqT11fNdeaq-9Fg9jpijWu9vB5KtMjvGtQ6f40mybDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
هواپیما جمهوری اسلامی داشت میرفت سمت فرودگاه صنعا، این فرودگاه بلافاصله توسط جنگنده های عربستانی بمباران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/news_hut/67991" target="_blank">📅 14:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67990">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsuLfZ12zNeQhTpgMU_OGRsAvW8sNGaZ7OtYBb7YfNWAlNNMzkRSMMBq024J8TFpJ8Mpnm_rUTsXGZR3Ru1jF54axGnvNoOIokgkL8eCs9r2HZw-ChKu9GnnAQ8EHfQlJ9z23oiiSHaHY9hb9UOMGgUpKE09XD8q9SDjKIP1PjNHL0eDon0gMxw6CF8Ijw7Zdpvjj7FanUN_AUS0va0v68NpYm_T7fi4HfO3VFkuUWPthpKH7p0SzjeimrAY_hmrDE4Q1p752urlFmQDj8aeToaFqAhoyLtiTLa1qJm_SMFTcL-xd5MCidHv5dD1qMF4ZPa5S5oshSSCTjXMo0d8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی، خواننده وآهنگساز ایرانی، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
جاستین بیبر، شکیرا، مدونا و گروه بی‌تی‌اس در این اجرا حضور خواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/news_hut/67990" target="_blank">📅 14:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67989">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gui1c7A-sQqyB81MPbEncYkeeG23LYJSwZ0avX06LMC49XVA8SGDglFSVLJLO4D3iyQ4HCqwnWi6uoMfjr7uJu8wpmIm1wuo84U_Z_MncUNoKGMsDnngnyIBLWPwI2whM1rzKmza6HIOd3akqzUfpYexv1F_QAeU9nm9r3FkswN2u3fp4fyGV1hJ67TvYMy1dz90tRez86vWRXMgRZdf-4Y09M-zxtJU1fadlF2azTGDIE9J_4odr_8IHKqaDTArsMrAq3ccDLYGoPQM8aBMVU6KyGv5O54e3FXC_GnDkeiQEb9yqTjZ05S9gPFrZXoIlXFJ0UHdQFscOz6pSpwntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های داخلی وابسته حکومت این لیست ترور رو منتشر کردن و نوشتن لیندزی گراهام اولیش بود تا نفر آخر بی‌خیال نمی‌شیم
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67989" target="_blank">📅 13:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67988">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
تنگه هرمز دعوا شده
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67988" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67987">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7891d1b9.mp4?token=MxHBDEqVNSGDNIMyXdltAt-A_oERz96Te3cfw65FGxZjQkz6-by62V2Vjdwhe62y4EZWBfR_PSBgBA3JPUDBixuQdjy0o0FdqUO105VcbvaIVgNHONlb9TFKkGIqS_LySv7kMpgtsDgBbJTK46j7qmpOv-yp9HsErlMPdNLZNX01Shn58dgSthRAuaYEw8ccc5tVRjBmxwyPJRyvfr6TyzNFFkkxPBXcQKkHFDr0_HOEumEzqyxS1bMZKVeZNnxC_wfcGWyQm6aDqE9pFEINV28DCYAgD0bt9IF-h_rTHdBX2Vy_fmc8n88A-I4nDQvRyCnROxnENPGBRiRzCgjlCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7891d1b9.mp4?token=MxHBDEqVNSGDNIMyXdltAt-A_oERz96Te3cfw65FGxZjQkz6-by62V2Vjdwhe62y4EZWBfR_PSBgBA3JPUDBixuQdjy0o0FdqUO105VcbvaIVgNHONlb9TFKkGIqS_LySv7kMpgtsDgBbJTK46j7qmpOv-yp9HsErlMPdNLZNX01Shn58dgSthRAuaYEw8ccc5tVRjBmxwyPJRyvfr6TyzNFFkkxPBXcQKkHFDr0_HOEumEzqyxS1bMZKVeZNnxC_wfcGWyQm6aDqE9pFEINV28DCYAgD0bt9IF-h_rTHdBX2Vy_fmc8n88A-I4nDQvRyCnROxnENPGBRiRzCgjlCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:با درخواست گروسی برای بازدید از تاسیسات هسته‌ای موافقت میکنید؟
🔴
بقایی:خیر
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67987" target="_blank">📅 12:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67986">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67986" target="_blank">📅 12:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67985">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=GUAexAA7iMNVwRp2I3RZDLcDMPq_jm3N0hSF7qoCKGbADcLiYzNt9G7fb05U_NxC5K2-7ne1HwMTBXtl5ZoV2INJGN9LFiKaYyp6YPZj7ci9l1JuiItLOXmDPHgIWr1TqtCIoOU3lpRkopIHNraCOXKI-tOFNUywDpqt3W3Wn94ojatUuhr-HSsELZGMRvKBf5sPYGcItR3vBWGT1BxolbJhKkRKSMmEdrKE0okYaYDI_GphKv7DStN9Zg3jABVJ_Cs1qF8seKrDlRoHGPXbyIS8_vdmETfNfvFo2xMruFj_7D_eq012Rv99XDKl4mpscZa224QV_JlkVzu1V_f7Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=GUAexAA7iMNVwRp2I3RZDLcDMPq_jm3N0hSF7qoCKGbADcLiYzNt9G7fb05U_NxC5K2-7ne1HwMTBXtl5ZoV2INJGN9LFiKaYyp6YPZj7ci9l1JuiItLOXmDPHgIWr1TqtCIoOU3lpRkopIHNraCOXKI-tOFNUywDpqt3W3Wn94ojatUuhr-HSsELZGMRvKBf5sPYGcItR3vBWGT1BxolbJhKkRKSMmEdrKE0okYaYDI_GphKv7DStN9Zg3jABVJ_Cs1qF8seKrDlRoHGPXbyIS8_vdmETfNfvFo2xMruFj_7D_eq012Rv99XDKl4mpscZa224QV_JlkVzu1V_f7Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
ایالات متحده مسئولیت مستقیم تحولات اخیر در تنگه هرمز را بر عهده دارد. آمریکایی‌ها از همان روز نخست زیر قول خود زدند؛ آن‌ها تلاش می‌کنند مسیر امنِ هماهنگ‌شده با ایران را دور بزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67985" target="_blank">📅 12:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67984">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ae996e.mp4?token=iNQiN_32D5p-9a0Rs0K3S7rPpDqaBGHte66V3wZVTNXneQJT8y2e4RAFy_luJO4bZLHN5YX19FpeaJj0-9MQ1A0QrmldkiP7GjVhwHbZ9dIDpn_mFpL6x3l4uWsMHBxsv8NJJFul61aHkoc6qsKZI9JiwF9hLsWTgiG96iWXmft5nQNjUZ32Fx4-pDFkNJihCK3Yf6pxtYb0dj1HZ0MNx-VGVY32YSZbeMT2h9EkvaQr_ygVc-Ivok4zQsEwxtGo5anzsVI1cW0SpXiq4gKkv9HBFNORWTL1_sGUtHvDN9ulE_7990NnAZV8BJgAfqgpyjvUY4lJv8latR-VDJ9xRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ae996e.mp4?token=iNQiN_32D5p-9a0Rs0K3S7rPpDqaBGHte66V3wZVTNXneQJT8y2e4RAFy_luJO4bZLHN5YX19FpeaJj0-9MQ1A0QrmldkiP7GjVhwHbZ9dIDpn_mFpL6x3l4uWsMHBxsv8NJJFul61aHkoc6qsKZI9JiwF9hLsWTgiG96iWXmft5nQNjUZ32Fx4-pDFkNJihCK3Yf6pxtYb0dj1HZ0MNx-VGVY32YSZbeMT2h9EkvaQr_ygVc-Ivok4zQsEwxtGo5anzsVI1cW0SpXiq4gKkv9HBFNORWTL1_sGUtHvDN9ulE_7990NnAZV8BJgAfqgpyjvUY4lJv8latR-VDJ9xRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
پیگیری عدالت برای رهبر شهید، یک اصل جدی و مطالبه‌ای همگانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67984" target="_blank">📅 12:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67983">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=kG3kMyx8DoyTWCW7jB6_Fr11UM-WkcL1Y-s3I47lrmDQCowMfmjuBOVdv_IijvQYNYJahU-cmbHmNB8zMGwP3wCavZft5-Pzau_86BnxerGKcpnmm0uSHRPFjXTKbDZyqrIGhQcygbuU0IpKgd1NSi_2uOozkgHkfPAro4iWmLatY0gB-SpqMo9j6xFXkDtZXwx4xwtSBAZ_z540dAhkCCFS7nERO_52UMciNZQ2UpIuYCwLsqXEGK7msw7QuYgB9o_bfSJzsIVwD5U8jeOGclnc-YqowoHz1nwsQ-UlHOjVQxP_AssbBv8xeZYt91qLYffP3N09m1gL_Os6N7V5fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=kG3kMyx8DoyTWCW7jB6_Fr11UM-WkcL1Y-s3I47lrmDQCowMfmjuBOVdv_IijvQYNYJahU-cmbHmNB8zMGwP3wCavZft5-Pzau_86BnxerGKcpnmm0uSHRPFjXTKbDZyqrIGhQcygbuU0IpKgd1NSi_2uOozkgHkfPAro4iWmLatY0gB-SpqMo9j6xFXkDtZXwx4xwtSBAZ_z540dAhkCCFS7nERO_52UMciNZQ2UpIuYCwLsqXEGK7msw7QuYgB9o_bfSJzsIVwD5U8jeOGclnc-YqowoHz1nwsQ-UlHOjVQxP_AssbBv8xeZYt91qLYffP3N09m1gL_Os6N7V5fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای آمریکایی با استفاده از مهمات سنگرشکن، یک تأسیسات موشکی زیرزمینی در پایگاه چهارم شکاری تاکتیکی ایران در نزدیکی دزفول را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67983" target="_blank">📅 11:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67982">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgUtZu77c33mr6hYVjs45HDMe3Joeh_ftkGpEbgUDMZHWmKnZ9Q1Z_9ywUfk5kRtLHOzXNmi9MrzCnAhGW5WweXgVlWWwGRC9XIx5wXP4ujtciC40JGWKDRxx7LvIjwv4d6F59MukGFsUR5klWFPLHHDqpOHyAsSEuZguk8umhogGfgCmI8QYjgPMb9oa1N4BYhz4vjLBt01-vB98bDI1F26ikoZPPS8D7mmUfWC6Mec6mtaQdFI9rYJtV7pTdRnX8c3zeXU02y32g71hX4VbXFTE0g1kmZ-Zd2PnO8otZ7Y8N42ocw-95Z9XcDag2UkaibTdJ-WcuNhC5ZRhKc1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ در تروث سوشال تصویری از لیندسی گراهام منتشر کرده با کلاه معروف:
Make Iran Great Again
ایران را دوباره با عظمت کن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67982" target="_blank">📅 11:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67980">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAQFv2J4l3BsbjxgbIxiVuGc23GlgoL_6t45ifoFVJ2KFbDB2ppUZlgTYCHZN44pr80JEdZuUQcwE1kTmFLXpAIzYT_bjekJ_ElFKmbO254JzrG076uP3qmRN9-r-nmOmCQTpx36tdv8u4SyPu0HHXUlPt1e2Blq_hrE4ZvEB8bcLN_Wy8LJUtXFmpr9W6cI9ioSzWTm33AQhlZ8BK2ChyTDlaAXijKZWyseCeTDAcfgfIhmCxLWe99Ig315O-Y6_vrAGw6_9cJkXCvOvE4k7-jOfcEZ0h5oS0CSO6r4Ce0aPRv17g3c9bRB9sXUhRT646LCJQt4ygAC8_QN5gGpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fd5R2HjAuMZbHy2_OqjcvmrX0hSpZUIlCVeE5IDanSdMYPqHnbsunK-ipGyeHo1tvDXjwgBk-VjeUOyOoXAwW4dfNZMSKiKo9IORstma8n6pZtOsVm6l2Gl_wfmtd4F9qXa2HwR6jjd5Fq-Sg7-hauhRv2RJMuM08KKnZQuJKlKBS8eZzc7Lb9SWKU5QZ2Hp7msfaLZafRStI_RckwpQuAWp0GvknCHnOTzs6H-uyykWLmVBqSnyB-tA3YAJB8kkaJG2I7I6pb5D8DGHFatsAmneGQEWPSgQMgd-erbzSdt8Sba3I2HSRmHYC0-3us1SDIlvOtQ7cNLNh8D5jWOESQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
انهدام پهپاد انتحاری لوکاس آمریکایی توسط پدافند رژیم در بندرعباس.
آمریکا در بامداد امروز برخی مواضع نظامی جمهوری اسلامی را با پهپاد لوکاس هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67980" target="_blank">📅 10:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67979">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddd337574.mp4?token=IwC_qqZALDbXZK-piKZA7-ihDV4rovCtaSHN_fE-MSgRyjT6ihsNNuqYKJXEngqQA_6IZsyDU0_4JpbDYLExu3iwkEWiPaFFrGugH7GvPPVC1kafiQ4XWTtfj0wlmbnmoYJ8Fnz0UIVRR_DguF7exILyRlfNi5u2kca656WlFQEi6MBkvIV4MTXMNa0jtGkwsw_MR2XkpU375oY0fYP3HMpkvhEW9j6F-J7dW3LLAbeBk7q31yJKmMthsBO_uLhPwvZgK8_wM9dQoDwSXet_Q-Gn3x-VidMDokMysoyt7TPmNUPpYuRdhed4htLqNw7xP4sFSU2vqwsPVfBKO6rDNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddd337574.mp4?token=IwC_qqZALDbXZK-piKZA7-ihDV4rovCtaSHN_fE-MSgRyjT6ihsNNuqYKJXEngqQA_6IZsyDU0_4JpbDYLExu3iwkEWiPaFFrGugH7GvPPVC1kafiQ4XWTtfj0wlmbnmoYJ8Fnz0UIVRR_DguF7exILyRlfNi5u2kca656WlFQEi6MBkvIV4MTXMNa0jtGkwsw_MR2XkpU375oY0fYP3HMpkvhEW9j6F-J7dW3LLAbeBk7q31yJKmMthsBO_uLhPwvZgK8_wM9dQoDwSXet_Q-Gn3x-VidMDokMysoyt7TPmNUPpYuRdhed4htLqNw7xP4sFSU2vqwsPVfBKO6rDNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید شاه
👑
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67979" target="_blank">📅 10:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67978">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5afa19317.mp4?token=ZfRqTxktr8AKFpOVZzg1q7oKtY-GwQeD6wmH803Qb1Gx4V1_CGT217L73EWnvRHSmQ3nvcdVO-IlJfKcOcK8QNvvcDC7xkbT3aASavT1KFIdXjz2GQqPY0noSlCt0FAPWdF_5zfVtWiKe7wPnIqVjqUGDYVYvV-AVCjPClosjETyOzCBy2nS2q-zdzfdnRilkizVn5c2zhCMoKBPABMGysemnKJ-HbU1VDWxunJS4GXD5F1qY3_pMk7oyxGinYD3WamNohLncrnRgLFn62i4bnT5X-NjaDMAzzIvUxfbZcSstq5GrAP5piF1JvaQ4VWtIjeshnclvyu882PrWYP_Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5afa19317.mp4?token=ZfRqTxktr8AKFpOVZzg1q7oKtY-GwQeD6wmH803Qb1Gx4V1_CGT217L73EWnvRHSmQ3nvcdVO-IlJfKcOcK8QNvvcDC7xkbT3aASavT1KFIdXjz2GQqPY0noSlCt0FAPWdF_5zfVtWiKe7wPnIqVjqUGDYVYvV-AVCjPClosjETyOzCBy2nS2q-zdzfdnRilkizVn5c2zhCMoKBPABMGysemnKJ-HbU1VDWxunJS4GXD5F1qY3_pMk7oyxGinYD3WamNohLncrnRgLFn62i4bnT5X-NjaDMAzzIvUxfbZcSstq5GrAP5piF1JvaQ4VWtIjeshnclvyu882PrWYP_Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستتو اینجوری کن
🫴🏻
لباتو لوله
😢
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67978" target="_blank">📅 09:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67977">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b2083eb1.mp4?token=E6r9iERejzQZSmx1DOHqnFcDLe7j2tyWBYsbv54amW2x6io5Dn_AQNrxASn5t-5qPVA1TDb7AyS31SIPO6ai5zecFC3hwo1wWe7NqW5YlJZ1tqJ-lDVPUHkiHzUIvpdaScv5FhvOX-vgi-fPHMJTdM3eRmxRjRz9wiS0gUJZmB5qIti2tOabGTmaNmKGL3S6Y5BWeCNlm7GIP8eAh6j7g-lod8VRDMkw35ALIjqLSWHPX9zLxk2uGTurl2qKH0YOAaDo7hoA7OIdxNCQv37omesNcHBCf9H6iUxSJxcI8OY21BcHZnt8PlJqhruZ88qGiNnAulBxstzpLoRdPCTGvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b2083eb1.mp4?token=E6r9iERejzQZSmx1DOHqnFcDLe7j2tyWBYsbv54amW2x6io5Dn_AQNrxASn5t-5qPVA1TDb7AyS31SIPO6ai5zecFC3hwo1wWe7NqW5YlJZ1tqJ-lDVPUHkiHzUIvpdaScv5FhvOX-vgi-fPHMJTdM3eRmxRjRz9wiS0gUJZmB5qIti2tOabGTmaNmKGL3S6Y5BWeCNlm7GIP8eAh6j7g-lod8VRDMkw35ALIjqLSWHPX9zLxk2uGTurl2qKH0YOAaDo7hoA7OIdxNCQv37omesNcHBCf9H6iUxSJxcI8OY21BcHZnt8PlJqhruZ88qGiNnAulBxstzpLoRdPCTGvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پهپادهای شاهد سپاه درحال حرکت به سوی پایگاه‌های آمریکایی در حوزه خلیج‌فارس
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67977" target="_blank">📅 08:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67976">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش‌ها از آغاز موج جدید حملات سپاه به پایگاه‌های آمریکایی در کشورهای عربی  @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67976" target="_blank">📅 08:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67975">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش‌ها از آغاز موج جدید حملات سپاه به پایگاه‌های آمریکایی در کشورهای عربی
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67975" target="_blank">📅 08:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67974">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67974" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👌🏼
تنها
#سایت
با بونوس های واقعی
😮
به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
✅
نصب اپلیکیشن بدون فیلتر
🚫</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67974" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67973">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIGRzh-ulHO6eaC8M-O25hSdO7eJh7zR2Rhu1R-iZjrBRxbgfm-pWvpQQAZ1cqDz3P3mOE4mGUtKSHgbm15d6ei7CyD7SO-WNSCKD3U8VkV9D2fGTFYpZTBZ0COFKnj8t4BGosSETzNa48jZnFCSKDoWn6_tATNjTE3aHuoiIXaNpfncDe2CMqUI9Mx1gJ1NdvPBzBITqtd8gzFOtLk6CSTHcRIc7EU2OncRbmgfQ3NzK1fn_rj4S9yldAHxMlnBrv1_j3zKpI7FMFMvA5CgaMEzmyAfeoL_h7NCnipclSEMbphyHiFFjuSYA6ffrZvxMhXDjIDG6KH8GhuPojvDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هر
1,000,000
شارژ مساوی با 1,200,000 شارژ در سایت بدون قیدو شرط
💖
💵
هر بار حسابتو شارژ کنی
0️⃣
2️⃣
🅰️
شارژ اضافی میگیری بدون محدودیت
🔴
اگر هم باخت بدی همون لحظه
0️⃣
2️⃣
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a22
@betinjabet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67973" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67972">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1a4493a9.mov?token=VtZ-B3zgxpA8lgbOo7rD0oGbreBEOxryTvIS0MFiibEeiOGsienWSXuWAFeImVGoPU7FoOmdDviMCqEHV7ZKbz1Un3VavNzkG7OftmIilVnaCVC982IRPfzzuVFzWxfpIlUmF9R-a_XFn_zrKxHfBIUkQ-BJzG_4MIqJKlVzevEEL2ePhCqxkUM6O3k9t0goj62FwKbh4KK7JUQsXaxbeweJ8kvLBlNlCWCiQfpOYVntkxEi6TSDAQVAbJ2g-3t5j1eXHOuIVN7b5qBpcW00xg9eYLOTKA-TiFlDWJr_xSJUibAyGw7f7AhueMstn0Xv0bVfGYB-GZVvow4-_DhEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1a4493a9.mov?token=VtZ-B3zgxpA8lgbOo7rD0oGbreBEOxryTvIS0MFiibEeiOGsienWSXuWAFeImVGoPU7FoOmdDviMCqEHV7ZKbz1Un3VavNzkG7OftmIilVnaCVC982IRPfzzuVFzWxfpIlUmF9R-a_XFn_zrKxHfBIUkQ-BJzG_4MIqJKlVzevEEL2ePhCqxkUM6O3k9t0goj62FwKbh4KK7JUQsXaxbeweJ8kvLBlNlCWCiQfpOYVntkxEi6TSDAQVAbJ2g-3t5j1eXHOuIVN7b5qBpcW00xg9eYLOTKA-TiFlDWJr_xSJUibAyGw7f7AhueMstn0Xv0bVfGYB-GZVvow4-_DhEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به اهواز بعد از حملات ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67972" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67971">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
نیویورک تایمز:
مقام آمریکایی گفت که انتظار دارد موج بزرگ‌تری از حملات آمریکا علیه اهداف نظامی ایران در یکشنبه شب (به‌وقت آمریکا) نسبت به حملات اوایل همان روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67971" target="_blank">📅 02:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67970">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فارس:
دقایقی پیش چهار نقطه در شهرستان‌های امیدیه و ماهشهر مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67970" target="_blank">📅 02:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67969">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
دزفول رو چندین بار سنگین زدن
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67969" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67968">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67968" target="_blank">📅 02:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67967">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=LxRDPI-oliAaIXEEjJQWrwV3YzglfJbNo0qIUYQHG0s8S512Byd-Kak6MdBdRiknZ2AsphACfqhv0V_GuoXDegka0PXiJU8BzeK2LKMt43NcZawSzao0pT6vimTGHhWuiNxjzPoSh5zWRoeiAqVylPA0jLago50N-6aJvZHiGyzNxZTpnU9ZHItxeq9ZRZ3whpFSkttEgtVE3gTtOuPF2fSsHB4p1QsuXCsNrJqcgrJK7qwQAXvVWE_zsu5lMTqwz0BmqU_ViO6-ryZ7zjhMNOB710oguILR2wfysmGk3uNWs4CaIUfmFmBuY8a10-2B3MpOdIB6ru8pxHqfcMCsLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=LxRDPI-oliAaIXEEjJQWrwV3YzglfJbNo0qIUYQHG0s8S512Byd-Kak6MdBdRiknZ2AsphACfqhv0V_GuoXDegka0PXiJU8BzeK2LKMt43NcZawSzao0pT6vimTGHhWuiNxjzPoSh5zWRoeiAqVylPA0jLago50N-6aJvZHiGyzNxZTpnU9ZHItxeq9ZRZ3whpFSkttEgtVE3gTtOuPF2fSsHB4p1QsuXCsNrJqcgrJK7qwQAXvVWE_zsu5lMTqwz0BmqU_ViO6-ryZ7zjhMNOB710oguILR2wfysmGk3uNWs4CaIUfmFmBuY8a10-2B3MpOdIB6ru8pxHqfcMCsLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال شدن پدافند در کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67967" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67966">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=fLKVf_vD5ZZOCnW_xGyp0yvDI96341P3yXmht0-kBuU05LIekaJ9pCOdVHDi-D5KpWHHBmdU3rSCW9FqYRGIpIJgoq9OlJGWEOEME7x2wwcSbyTMCb1nZZvqXQK8T9w125avIF2QKTYWD898fFwzoilVdPBHN-QjHPtTmCRZfm90357krbYN5qLTm0lFt50A4fXshrQTvEwaw1arWBn3DmrdHpmgyfAmWZzq2LYAbKrCcbXEGe9jX-kxPVdpxwQ6fv5TNA_M7kksLe8vNTAZVKh2rZqYxXsyoVLnjCOhChPjOF3dYqOwGvf54awRZr_XGOr9O38-nVKZ3dHaMhSq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=fLKVf_vD5ZZOCnW_xGyp0yvDI96341P3yXmht0-kBuU05LIekaJ9pCOdVHDi-D5KpWHHBmdU3rSCW9FqYRGIpIJgoq9OlJGWEOEME7x2wwcSbyTMCb1nZZvqXQK8T9w125avIF2QKTYWD898fFwzoilVdPBHN-QjHPtTmCRZfm90357krbYN5qLTm0lFt50A4fXshrQTvEwaw1arWBn3DmrdHpmgyfAmWZzq2LYAbKrCcbXEGe9jX-kxPVdpxwQ6fv5TNA_M7kksLe8vNTAZVKh2rZqYxXsyoVLnjCOhChPjOF3dYqOwGvf54awRZr_XGOr9O38-nVKZ3dHaMhSq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویری که ظاهراً پرتاب ATACMS با استفاده از HIMARS در کویت به سمت ایران را نشان می دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67966" target="_blank">📅 02:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67965">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
حیاتی معاون استاندار خوزستان:
در ساعت یک و ۴۰ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه نقاطی در شهرستان های بهبهان و دزفول مورد اصابت پرتابه های دشمن آمریکایی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67965" target="_blank">📅 02:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67964">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
مسئولی در استان خوزستان ایران:
دو نقطه در اطراف شهر اهواز مورد حمله با موشک‌هایی قرار گرفت که توسط دشمن آمریکایی شلیک شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67964" target="_blank">📅 01:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67963">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
مهر:
معاون استاندار مرکزی در گفتگو با مهر حمله دشمن به مناطقی خارج از شهر خنداب را تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67963" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67962">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=IPPsBvZrVZuitysqZPFNW2nV5i3eSLCfY_zfOkPJyc0rE4nB-XnWL8HYpiBbulnRsseC8moYII7BQDG9JBxaTZ_18HpAh8G4LBo7xXjKcsWrI7RwFfT4E9H6Cm0NJcuUMEvqzWqsg1WJEEqcV8-BRr7wOvCqPjJ99_r3musCLE-UsRthUL_OLoWjvykzsx0lmOPq9tftET0V-rGdBtTpfWCjSXGpHl1rteIsoB8xtd3Y1ZE1xoZOyi9NQ2YeqoFhqFkF6i9qu7UK7hoLVLnKPVbebkeaOd0u9bn-Attz8EGChSgnrh43hVtaJIYsKVqrqvOakEH5_poGPootAJFLew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=IPPsBvZrVZuitysqZPFNW2nV5i3eSLCfY_zfOkPJyc0rE4nB-XnWL8HYpiBbulnRsseC8moYII7BQDG9JBxaTZ_18HpAh8G4LBo7xXjKcsWrI7RwFfT4E9H6Cm0NJcuUMEvqzWqsg1WJEEqcV8-BRr7wOvCqPjJ99_r3musCLE-UsRthUL_OLoWjvykzsx0lmOPq9tftET0V-rGdBtTpfWCjSXGpHl1rteIsoB8xtd3Y1ZE1xoZOyi9NQ2YeqoFhqFkF6i9qu7UK7hoLVLnKPVbebkeaOd0u9bn-Attz8EGChSgnrh43hVtaJIYsKVqrqvOakEH5_poGPootAJFLew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67962" target="_blank">📅 01:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67961">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=Tw8Fp49mJbXrAx0yneZP3utzvXPrYsYEQfhmZ2HuYicWX54BVCbuOyqHkwNFHn1d5uaTeTnnwxdTHogA_a9phOikoV8tNknMFL7q1K7FtSXKaFPBSWMqdryIXELaDALiYBGXAa2GpjUu3yCoUgm4VgDN4YxROTw5RpCf8p45ltEIYfATebetRYaPbEKBhlnu2eK6pTIeh6ITE8mEIJzKwlke0JY8H7S7UAU9JVIfyJ7Y-XAXgX0mNX6O8CBA6I2jAEfUTfywbNndbwSJMgN61MChVerKlj4DK__WAnkII7j3TObCSvBIfsIW02MrwqDNej-Pe-qKWn3OyPpbLvQ9Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=Tw8Fp49mJbXrAx0yneZP3utzvXPrYsYEQfhmZ2HuYicWX54BVCbuOyqHkwNFHn1d5uaTeTnnwxdTHogA_a9phOikoV8tNknMFL7q1K7FtSXKaFPBSWMqdryIXELaDALiYBGXAa2GpjUu3yCoUgm4VgDN4YxROTw5RpCf8p45ltEIYfATebetRYaPbEKBhlnu2eK6pTIeh6ITE8mEIJzKwlke0JY8H7S7UAU9JVIfyJ7Y-XAXgX0mNX6O8CBA6I2jAEfUTfywbNndbwSJMgN61MChVerKlj4DK__WAnkII7j3TObCSvBIfsIW02MrwqDNej-Pe-qKWn3OyPpbLvQ9Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منبع عراقی:
موشک‌های آمریکایی از کویت پرتاب شده و وارد فضای عراق می‌شوند، به سمت ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67961" target="_blank">📅 01:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67960">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baSMUuSY-a_TjfNL8rCgSgLrFo9iga4bg0TmVduHpXBCrw0mP8aGdWNW8O0l9aHEdp8WV0nXOFewPQeDLriFgFXbyhZb6vwPQFi4mGSQLzf61ad5qdOAf6TRHZ0fYXa-a1YMBL5pk-P0H74GeczBOzNWrpst9aV1LswvcL-A9EQ7nU2nRiF9OvXvCkNReShoIFOB1tMpOT6cah-bk40Q24o8uK9RwLIJlPdQT2aXl-PCCO_SyAhnX7CdESo4kgHYC8tP1-cT4uE4cM5PFf9CTFMAfLC0GXMhg9sambI6UOvvupmght4IZT1eqjt1mUKTui4Zn7LQdpXWrBMZd1BTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
ناخدا دوم تیم هاوکینز، سخنگوی سنت‌کام، به من می‌گوید: «در یک ساعت گذشته، نیروهای سپاه پاسداران به سوی شناورهای تجاری در حال عبور از تنگه هرمز شلیک کردند. هواپیماهای آمریکایی تاکنون موفق شده‌اند یک موشک کروز و یک پهپاد تهاجمی انتحاری ایرانی را رهگیری کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67960" target="_blank">📅 01:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67959">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
اهواز رو دارن شدید میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67959" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67958">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
گزارش های از وقوع چندین انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67958" target="_blank">📅 01:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67956">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbSVPaF-dofIzdDgJmTpqwX5kj8sWHokFk6xT72yQyHtNBpRGdpy3Zc1EWv-YhEFiRr5mKn45UZZvzJt0NdI22rUyhwqh3rdQGDPupAdTswtPKMfCCf8f3SlnYGucM_Hj5MK_2-Rf9Cn2ggWEvI8sHfRaKuRxx1cavD-PUO_zCjd_lGsq1gq1py82KNdrkDK4erYO-rpHQfDHVgcc_8kGiHLGyuXK8nJHzLbdT0lOeSpazHmFOiJJr6WKoLcjGzxeL_vg85_IAoYeLDv7IZmgXHkuDFUZa9Eo09SOBP844kZaaQzIDaYODHP3ppl7GKM1JoGgYLCyncKl0gQJcFiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=JB6ucSnE2d4f1zoDVX82gHi1UjK7VHsEcXyZ93JlGLcTnEQ3jXXO2QNGH7OVD9Myt_XL8LgUQLd8yJHhYpD_XaihTpbtk0l-0GvgU_K8Pe0RomJaWxhbbH_sGqI1gblslSUX_hAuRZHMknE0M85C-aw-YMzi5vGnWZ-LJxfAlqJbqrHpcFuNTh0xl5J93DNhmhvY2i64QTbKIFN2sB74_Xjn60wiaGBo_xvFmY4sGd1p8ZcHc8DyAxOwb6odr_XF0ljEXbWUUKKItM7OIhHig5DE0WCBkoMU1wvITXp9LFJQ0NyrJ5VDNJkSLbLvWxWf-5xOUSmZXCHo2tdKvQG9Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=JB6ucSnE2d4f1zoDVX82gHi1UjK7VHsEcXyZ93JlGLcTnEQ3jXXO2QNGH7OVD9Myt_XL8LgUQLd8yJHhYpD_XaihTpbtk0l-0GvgU_K8Pe0RomJaWxhbbH_sGqI1gblslSUX_hAuRZHMknE0M85C-aw-YMzi5vGnWZ-LJxfAlqJbqrHpcFuNTh0xl5J93DNhmhvY2i64QTbKIFN2sB74_Xjn60wiaGBo_xvFmY4sGd1p8ZcHc8DyAxOwb6odr_XF0ljEXbWUUKKItM7OIhHig5DE0WCBkoMU1wvITXp9LFJQ0NyrJ5VDNJkSLbLvWxWf-5xOUSmZXCHo2tdKvQG9Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویر مربوط به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67956" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67955">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBeHrAd🇦🇷</strong></div>
<div class="tg-text">توالت + دکل = برنامه طوفانی پیتِ پرس زن</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67955" target="_blank">📅 01:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67954">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :  @News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67954" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67953">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
گزارش ها از انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67953" target="_blank">📅 01:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67952">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1ZOhp4DvjJGQ4Ztn2sbU3lcSRsMdZTKyuqDK-XEtr7vhmyqbZYf2U2LasN2vAQ3hqlAfnvqRXz1z70jOU6pna3khoe9vtaoPn4Gi6uUEEES3_hifu4pl_LcfJvdKnDm4yVLxXaB4VDzFPPbIcfCt0g3OCSTDdE_IRF8s1pw56zpm_cZEdyrdLoGlYWFOK3sX0d40QN_TE3ILW5f8e-aELGH-Kf5CXjQXo9Amw-4tQxEvJj_s_TstKUBxUCs9BzRtIzR9Prj_qJ8JHD9VvnjDoxDrV5ZurKPRZrvgWRI0mhsNmqN32Z06CSjJS33JXRQXGmZEIEXB0gVCB72bvEaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
9 سوخت‌رسان آمریکا در حال حاضر در حال پرواز در آسمان خلیج فارس هستند
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67952" target="_blank">📅 01:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67951">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ1t5VmE94l68eoXrmo_fEoXDtxrMfNnCOrvmICVH8_qI717PuhqMYZZGXPEuat30OFwrOvz-bGOHko0XtBcqWhlyKZhXn85ryVZW8tdazpBmWmrSkNE94Vo70550PDqzUxsf0jd3T1PnP3rMWvOYOgti-oTZO88qepv-Z1YmShzp2lyvuUlgyctrvolsl01Td_p40Cka9Pp-PqYj2Gynyg5DaykNfpetEeqanvZETinvP7jU6YUT3WxO8IN1wUHjZipmeGhjwE9rHs2AeNIWk0dqNU1Na1SiP3MlTphWDpk21Jf6iJwWnGi9YfHJmDndxGTI6JK3EQKZStzrvHDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویر منتسب به انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67951" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67950">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErirguEj3TqKLY1lK4jDpZ0-3wdZqzdJnr2-8EvYf0-3Olkw-tMjKnTrvT3Z1B4dXF4b0Zyt2LtrIuuX12fikYTBiJBeIOcYU1AP0TTkg2ZbYdzuR27Ub86N18ivu1wqKkPDeBH1rUVdsLFcyjxUJJgsUWv9HPHGt2U3UGQPWsQtgQr7EQRypRb49it1RqzdKGB0btpqOKvF2DnQL6YNs2RxhC8tRMl8djI96-dJ5UBy3I_DBUxbSSmpo9Qop_fTi-ytXHY4Ak5EAPbti8NeMXf5Y0iHm11_MRnHL3dHOb7RQ8kInoKzW2wsRngwSlEpowLx-1TCZkAvRmkk_FsZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر من زود تموم می‌شه، چون:  صرفا حملات جنوب کشور هستند دلیل حمله هم حملات سپاه به کشتی هاست و این یه حمله ی انتقامیه، مثل چیزایی که دیده بودیم قبلا   یعنی در واقع حملات، کنشی نیستند و واکنشی‌اند  #hjAly‌ @News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67950" target="_blank">📅 00:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67949">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
❌
دو انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67949" target="_blank">📅 00:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67948">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67948" target="_blank">📅 00:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67947">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z14Os9GBS8hrlEVVOGbqgjZoG03QNwmCtx_bDSY4WWeU8pDTMDWKqo3hiXKfRWf58kzvrBnM8b8pQHQjB0cF5R1y0Vo367KmURqWF7O4f3dgJ9V29QJGBfJZ7FaeTu7n4BE2Q9mB5mIh_9RrLZ09SoxgNe5PmbI5-hdkI8M6dNnrdxtZmYA7aBQ3bpGtZqw427JZLYiLRQJ7Vq4u-HNh6c7li11q-P2DzU0yWJa5O5AOdIFzDkSA_OunvopFaVANpOMRVhYwEymkbomSkc6lwt2_z-MEBf_XPPE2IlWL-45k-57HdgmAw0VRB-wWlpNV4-w1bxFSoWFZJ2BSRZkx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
ساعت 5 بعد از ظهر امروز، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به توانایی خود در حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند.
فرمانده کل قوا دستور داده است تا به نیروهای ایرانی پاسخگو باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67947" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67946">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpNBKWpWP66pOUHLrGAWiVg0katHK1hvls9S8v6BdMQH12l1FHglmkRA2MrUpKE3c94CneKzGVBUr1TrgpIaXPfZIrGJnKdpNsQD8qn0dj8_uvkTQZjJNaeqbMjuXpMDNHVW8RH1InZEyN4APm_tQIQJjhK8VRjTpAP_IlNByqcHtV1ze6F_12jfpOOfwV9HBRT1o_24G9lyaqr0gdBAHdfJkOr4k77zmTvDM5DXk52BmYjWHOsD5-feooYB2ve04rj6zWjsbi15d1AMaLOChRNj3q1LnhyNUCC2D4aS-8WaCHrwNC8BNjM-rSDyoFDtjSSYrvvgo5wokx0IimI92w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67946" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67945">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇮🇷
ممد سامتینگ:
اگه نمیتونی جنوب لبنان رو امن کنی،
پس جنوب ایران رو ناامن کن.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67945" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67944">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67944" target="_blank">📅 00:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67943">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
❌
گزارش های اولیه از انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67943" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67942">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67942" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67941">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به خط ساحلی جنوب کشور آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67941" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67940">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
پنج انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67940" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67939">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
❌
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67939" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67938">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار شدید در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67938" target="_blank">📅 00:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67937">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
خب مثل اینکه شروع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67937" target="_blank">📅 00:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67936">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=tQc6jEhX8Sa1dt6q3PYBxowxNh_pvjtrNky4pc9WGmdW6v044Fpr4OiKFOxGT_-sCKy5GtaV8Az79bQ4skawSDiINZIPMEMy8GIfNrEjMX22NECBAT-vSxc-IfEvbvqUzvIuQo6vwO7FeKMUepcZyoJtBIKJ4m5XkAPO2JaxG2BQ9rDgP59qQpi4LV4NVMYtjSzqs3-q_84otOEp1ZJWIageXwEUDeWMIbm9om7aFiOjF3bEO1Q2WkOwl5x-1rWza9l6gpN8pkHGWTc7MdnlJtyL7aUvvS01hoQH81nVI6oRb6-u-U2tirXcYMnCCRL7dNjzMz2CTz_YGsH5dDvQVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=tQc6jEhX8Sa1dt6q3PYBxowxNh_pvjtrNky4pc9WGmdW6v044Fpr4OiKFOxGT_-sCKy5GtaV8Az79bQ4skawSDiINZIPMEMy8GIfNrEjMX22NECBAT-vSxc-IfEvbvqUzvIuQo6vwO7FeKMUepcZyoJtBIKJ4m5XkAPO2JaxG2BQ9rDgP59qQpi4LV4NVMYtjSzqs3-q_84otOEp1ZJWIageXwEUDeWMIbm9om7aFiOjF3bEO1Q2WkOwl5x-1rWza9l6gpN8pkHGWTc7MdnlJtyL7aUvvS01hoQH81nVI6oRb6-u-U2tirXcYMnCCRL7dNjzMz2CTz_YGsH5dDvQVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#Rip
🫡
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67936" target="_blank">📅 00:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67935">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTbp7J_X24O3OJtuKsSw2ZHv7Fo7Co8VJZtmrV4JhdQGn-pPrRji9KeeP69VjSuXo7xfei0pP5eE66zjKqBdFBupQofgYgoc-Iv528jCGqhnBnhMlJbO056iGdspZK6nduHG8M_LgX-dZfddze0AvrGEzLMBpJq2rqxPrFhAvaFUaoCcYA5d0HTFpOK-bMqkzXn2JVIZwnoWHkylRsX_bwfX7uaRXmLyJWZzMhLihcOSxEZMsb77JIf7RZMLcZ7AAWVAR8TO6ZZOueN9txkEeB8f8DsZs-IOcyanc27jxr8JSe7ZmjhRC5MlX3JtrT7F5AkS-3Tf1eKqRCcmySpohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
❌
ادعا: دستگاه تبلیغاتی ایران امروز مدعی شد که سه تن از نیروهای نظامی آمریکا در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✔️
واقعیت: هیچ‌گونه گزارشی مبنی بر کشته یا زخمی شدن نیروهای نظامی آمریکا در منطقه وجود ندارد و وضعیت تمامی پرسنل مشخص و ایمن است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67935" target="_blank">📅 00:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67934">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=jA-swy61Fm3U0R2t3bb_nBvQ_Eid4catBc8nPNaDDibrEO0SOBuNCO0x4PTPO1qkwOHqAbVUc3-QwQGkwspMYO7e5cENM9tnXxIQWUhMrrXk9dXOABDOJX89uuBQHiw6OCVUKrB0yzerEcHaGuOJUkiiNk6sXocB5YcER_IUOgu9dwy7oaX9PrSunK-zEBOm3FAoP77ad5osiBe-UytWzfwnM3PvYflFjVDg6ND0vdDay3XMOD2N_7SgfJaDfu-fFbotAKteee7HNR07fauyx90CCd6PNfYeop3zOnYgiHB-g4_N1kocPG7QKeDpRv2DTgJyLJJje_DRP-HOOYS4gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=jA-swy61Fm3U0R2t3bb_nBvQ_Eid4catBc8nPNaDDibrEO0SOBuNCO0x4PTPO1qkwOHqAbVUc3-QwQGkwspMYO7e5cENM9tnXxIQWUhMrrXk9dXOABDOJX89uuBQHiw6OCVUKrB0yzerEcHaGuOJUkiiNk6sXocB5YcER_IUOgu9dwy7oaX9PrSunK-zEBOm3FAoP77ad5osiBe-UytWzfwnM3PvYflFjVDg6ND0vdDay3XMOD2N_7SgfJaDfu-fFbotAKteee7HNR07fauyx90CCd6PNfYeop3zOnYgiHB-g4_N1kocPG7QKeDpRv2DTgJyLJJje_DRP-HOOYS4gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
سخنان قدیمی زنده‌یاد مانوک خدابخشیان در مورد لیندزی گراهام:
گراهام کسیه که به کنفرانس های محرمانه بیلدربرگ می‌ره
کسی که می‌ره چنین کنفرانسی یعنی از پشت پرده باخبره ولی اجازه نداره چیزی بگه
بخاطر همین لیندزی با هشتگ Make Iran Great Again می‌خواد به مردم ایران نشونه بفرسته
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67934" target="_blank">📅 00:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67933">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZCLjimcLN4qd11T6T1puz5GR0ouSZToKW1DBlgWeEloqGvYVnJkxe3g1AxmseD2L6uwEfSW-1GOAMHJsVf07QSLjcE-pgtHpgl8hsB51FF6uKvCm48YH4b2ZMBtUU0Qny457BYK2R52QpFC2Rjdf9nD7VLHXDxyWDwMDroGgdN5AQ4zcUs91--KSjx3pDPrvCmcmFlQ68ypponcAx2iUv3sLTdwSJk_TLqGvqUVVc-cTWrhiYHo58cT2quvo8ONZMNu4outrCU-jOH5XOQ7vxfycAjzVe8HYqhz8DjMU7rLDOyC_Uk0zFI1LMisdgzFanigFNSvMzpR4glw5gLZsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال   @News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67933" target="_blank">📅 23:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67931">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l9FKT4bHDMtL-_ZO1Z8KFW6Ca8L31eFcYTNZT5YVPKX31N4ESHfIPH4opWkCUv2IzzooQLIR6mf5mOptn6QdbyUBbqFuXGDgUHtzCfQL1mwicNMA9jAx_0NtApK3OZMJdCA75YBwm4nGfKHh1ta_wAf2scYvxECL21hKzCZ4OwcVZax2-_1s8vRWcak0njzLTqQj147wp0UQi-ldj4NbJxghwoPGaIOcB5OZEsRXjC5W1_zeRhQEz7O4pYv4YUoUulG9dN_CHo8rzmX6dFs1jpoplPaKR80fQIHJMFyKYTIYKy9_kOG1i_PQY6svKAfIzQxpKJnaKY14dXFojQ-6NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WrSVUe5JF-qqdshtYWstEZtHT2k8UVB_i-9Emeg48ulBL_8A_d11mBfecalR-8-ZflacIkkbPTEj2pF0gdLwkeweAcLJ-R6FvZ11FXo-Y-nT3eXul7OE_jc6YK7Oi-uhqfSy2JVYZ8F3brH36sPCA7Rc9quXoCNlLvoE-8rdlKyJ0hO4jHrqGdR2b4S2fCnUug2h1TLpZUWcoF7jm07RaUfquSigxeOxPJ0hczshx_KjegFd0tp0uOOE_UD2vINyqf8ecRp0DIgBQblIBZbHaeBUV8QevXH1Y93tdYlvYIeCeQ5rKAtl0ESX0aWPuR191dC359cllEfjoEk6lckPhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67931" target="_blank">📅 23:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67929">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t89GpM9MIFrzGsESXtx2z4JvTnghU13aNk8wm9tYVFy2rTz0nN10ui_JX_swihDvgJ-ZQuZgByvwKWklFJpBbE_6UcsZfC8ynMHlddLVHlzb3R-wknSqkCRzQNG4C3Ti0HxuaytmeKGptb1U9eBWo_8YC24No3XMf0y2tvT0Zz_lrMjWQxGAyBu9XhHS54tfN0vlPDdwOPamh8ASSrgTIzm-d6qXwVAhui6-crDCut2pY0Ipp69os0M-Mb_HQcpeYXd77IlSzq3V8V_oMVCFxtWR2-Yc1i_isJ6ZVk5LtYOxWOMcwn3__nRRBzuvq0eVY2vwuSfg6xKhrbeFyzasvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0kv4XzHoh6MU5XcdPlvxKpHccjQoQalij3imVCjsC2c3Ep1VicpdtJ--h7KXH0nHlH8dQAnJkNOdmTowbvdq5nijR0zD7xSQucmchTTPgsbbG_1OhkHWaOd7i18WQpk_1eK4eblrvI4yZE9gB-cN0Fsr0if74JKFSfhZSzyxMl6cm1eXMHxZkfQ7-NobTv8dtGrk93Np3zK8jOQ3xNw_IaI7gV_FmAKjkn1o6DvzLYoAIm24psBqSpfZNMj8JMfLChYVpK-HbHLQy3L2H7_9O7PG262pX1ZwDBwhvh05X_r3EK6UNwbEIgoW_Lc7ZiPIctwITGtwCQMwuTUbYwxbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
🇷🇺
لومر، خبرنگار جمهوری‌خواه: ممکنه ایران و روسیه لیندزی گراهام رو کشته باشند، باید تحقیقات صورت بگیره
همچنین FBI هم وارد تحقیقات شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67929" target="_blank">📅 23:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67928">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=eQIOdkw8nnvEiSIuRToeofeOUAr7HAlv9q1lL2kVZm-ABTAtpXJGcAntL2isdMh71lcTNdtwKgjpgQ_cShE1rmHvgh5-j7dFKXCxE5LJFzqmmzHzWF0uyUW83yp4xLwkx254OCt1maFxXMz1t2FXOFi2H_OPnDZUiMrsbX6k6NM57DjkJ_-iNWdykTYg_vzjpWrnFTRJyT4lJFyQVm88f1i9S0nI8QwCpa7FPTLjd0TWRKIeC2kXt_QSw6-78CU7Rv9lldwZErYiAWQ-kqbaHWqRl6e6YIbUIr45R1lNhvCnyVZyHsTqGMk1SKZSa3A2OBM1HS7eqcVYTdAsB2NccQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=eQIOdkw8nnvEiSIuRToeofeOUAr7HAlv9q1lL2kVZm-ABTAtpXJGcAntL2isdMh71lcTNdtwKgjpgQ_cShE1rmHvgh5-j7dFKXCxE5LJFzqmmzHzWF0uyUW83yp4xLwkx254OCt1maFxXMz1t2FXOFi2H_OPnDZUiMrsbX6k6NM57DjkJ_-iNWdykTYg_vzjpWrnFTRJyT4lJFyQVm88f1i9S0nI8QwCpa7FPTLjd0TWRKIeC2kXt_QSw6-78CU7Rv9lldwZErYiAWQ-kqbaHWqRl6e6YIbUIr45R1lNhvCnyVZyHsTqGMk1SKZSa3A2OBM1HS7eqcVYTdAsB2NccQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خرگوش نر به تازگی جفتش مُرده بود و میخواستن وفاداریش رو نشون بدن که اتفاقای جالبی رقم خورد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67928" target="_blank">📅 22:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67927">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5o6dz7VoPHOd5Hx2oGeZbgaeRRjhYaC23qQMqXtAL8B8lFLWRmq2rPZlYv8SANcjMnCWcXlKkwCTZINUz4Hn-MUSIQgp4hLzt-6peM16QcEy_cbBW2PtbdeJjLmWa5i6f_1Cb0lg1-csKr0GkftPoo0q2SHaSS1_eO1j-6OZXDUX0Xuru6nljEjyHWb-q9Jj-cIPM_FcWdSlSd7AzwBnYm4c-UNv2z_28CxQ1fcwsgOHazln00re2FuPA3m6IsFBNC51XrK1v9waBuMGp_8T1bt5dayC5pyAiqa5n64RwJ5Te-hQDfhehV4BIvRNKakbn1YbRWz1U3L3ltEP0QIrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه های عربی وابسته به حکومت؛به تمامی شهروندان و مقیمان کویت، بحرین و امارات متحده عربی:
با توجه به وابستگی حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای پرتاب موشک‌های زمین به هوا به سمت ایران، از شما درخواست می‌کنیم که نهایت احتیاط را به عمل آورید.
در صورتی که هرگونه سیستم یا سکوی موشکی را در اطراف محل سکونت خود مشاهده کردید، لطفاً در اسرع وقت منطقه را تخلیه کنید و از نزدیک شدن به پایگاه‌ها و تاسیسات نظامی آمریکایی نیز خودداری کنید و از تردد یا عبور در اطراف آنها اجتناب نمایید.
از تمامی شهروندان و مقیمان درخواست می‌شود که این مناطق را فوراً تخلیه کرده و به مکان‌های امن دور شوند، بدون هیچ گونه تأخیر، به منظور حفظ جان و سلامتی خود.
پیش از این، هشدارهای واضح و مکرری را به حاکمان شما در مورد خطرات دخالت در این مسیر و درگیر کردن مردمشان در یک قمار بزرگ با سرنوشتشان، ارائه کرده‌ایم.
با این حال، آنها تصمیم گرفتند که در مسیر وابستگی کورکورانه پیش بروند و تصمیمی بگیرند که بازتاب اراده مردمشان نباشد، بلکه از خارج از مرزهایشان بر آنها تحمیل شود، در غیاب هرگونه حاکمیت واقعی.
بنابراین، آنها مسئولیت کامل تمامی عواقب ناشی از این مسیر را بر عهده می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67927" target="_blank">📅 22:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67926">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaPvGuoSA7at9etQGhkXkCrngwQlvMLbLIc2iyK4Jy7SDx0kA8T-VHpgXZJjY7ApFW_3UvxStkvkFmEYDfBA5cK67G5j7inmfh4b0vNODlvSdGBa0igTU8NOJ_C_xKlbuczoNTpUc88j-ntPIGUPVuODfNHg2bFspzFnU9_sgeuZnBWgC6EkEVUe7If6hM9GlJaUbbAJ_dfopLZI2qpGkNxi4OWDNlbie912XytnR28R6WCVIe3xeZr4JPBCgYaz1malcldUPuc9BAkJNUEhj7kEalXKQgbhMUd8wVGOteQfCoOG6JjXzZhYiBiH0-PwofRjc0g_kYpdNkCfY-6J5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آکسیوس:
اندکی پس از تماس تلفنی با پرزیدنت ترامپ در شامگاه شنبه، سناتور فقید لیندزی گراهام در گفت‌وگو با فردی دیگر از وخامت حال خود خبر داد، اما گفت تصمیم دارد مراجعه به پزشک را تا صبح یکشنبه و پس از حضور برنامه‌ریزی‌شده‌اش در برنامه «Meet the Press» شبکه ان‌بی‌سی به تعویق بیندازد.
وقتی به او توصیه شد فوراً تحت مراقبت پزشکی قرار گیرد، گراهام با شوخی پاسخ داد: «الان نمی‌توانم بمیرم.
هنوز باید تحریم‌های روسیه را پیش ببرم، تکلیف رژیم جمهوری اسلامی را روشن کنم و روند عادی‌سازی روابط اسرائیل و عربستان را به سرانجام برسانم.»
سناتور فقید لیندزی گراهام تنها چند ساعت پس از این گفت‌وگو درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67926" target="_blank">📅 21:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67925">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=GYDg8k_0qcNBrEm69SUiu1_2YWvvqMqTaGJzeB2SA_g5YpZqfecPK2P7_CtJHWWrlbUntJLzKKi4BmQNWqBVPtqQlgEZ9F2uvfSSk1rMztyoTNX7Ugikgtcr8KpbCcpVOFANmniUBaNJGpjUL5kEcQcMsd4TN8miiSRIaNAi3bQfiMbllSUD6nikMvb_UC_0B65RmmhPqvPBMiZW9P6X4YgfVmBIlw6llgZHUUeplkaIOOeZX-FInW4ifVV20Jhwr12PieJjUXJwpanIX-9MSaFIpPyNeOE3ikYuZGK-Nb5_qPMSLILh2iRRmSOECy1kbdaFwmJZwCSwYilaVG_F-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=GYDg8k_0qcNBrEm69SUiu1_2YWvvqMqTaGJzeB2SA_g5YpZqfecPK2P7_CtJHWWrlbUntJLzKKi4BmQNWqBVPtqQlgEZ9F2uvfSSk1rMztyoTNX7Ugikgtcr8KpbCcpVOFANmniUBaNJGpjUL5kEcQcMsd4TN8miiSRIaNAi3bQfiMbllSUD6nikMvb_UC_0B65RmmhPqvPBMiZW9P6X4YgfVmBIlw6llgZHUUeplkaIOOeZX-FInW4ifVV20Jhwr12PieJjUXJwpanIX-9MSaFIpPyNeOE3ikYuZGK-Nb5_qPMSLILh2iRRmSOECy1kbdaFwmJZwCSwYilaVG_F-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کانال 15 عبری:
ارتش اسرائیل با همکاری همتای آمریکایی خود، در حال تمرین سناریوهای مشارکت در حملات علیه ایران است.
ارتش در حالت آماده‌باش دفاعی برای مقابله با سناریوهای مختلف قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67925" target="_blank">📅 20:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67924">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
👎
خبر بالا فیکه و ترامپ با هیچ رسانه‌ای چنین حرفی رو نزده
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67924" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67923">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
❌
وزارت دفاع کویت:
۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت.
‌همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67923" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67922">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxZUnN-fGyx1r-5jOgfPCPJmoC54qiABuh6HmVAWDWYkHpw4w3ux22XOOWuYlf_b2_RzNJeDioiJinSrFHex03LPBfQepNiOnDSoT6qS3Q1UHGmkuGBD_QO-weZkolUHt4P_M3SpNZ7NIMu7UZmgKypv0bliiiCrlOWifbUnc201KDACeDpHChYwSZdpcjo2aVDNIpuLLGW9KJvsGpzcyIeVOAGy5KWcy3gCFSfuMs6YgEMnZ6OmV1MF0biTGewnUIi-KhC-2kpRGn3wiI0KIl-Crf7DSEUdRBIOyK_2ZdEb9RccxaUcRT1RO5eT8qUqtfy-eechtbhxqwOkIIlXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
ارتش ایالات متحده چند حمله را علیه سامانه‌های موشکی و پدافند هوایی، و همچنین قایق‌های کوچک متعلق به سپاه پاسداران انقلاب اسلامی در چند نقطه در نزدیکی تنگه هرمز انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67922" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67921">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
فارس:
خبرهایی درباره کشته شدن 3 نظامی آمریکا در حملات موشکی به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67921" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67920">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
منابع خبری آمریکایی:
یک حادثه امنیتی بسیار جدی در یک پایگاه نظامی آمریکایی در کویت، پس از حمله ایران، رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67920" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67919">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
منابع امنیتی به نیویورک تایمز:
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67919" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67918">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lL-PWyKqoyAW0IiBNKD1DsBVi0_sJNGUdu3tgMS55Sampy-wP0A9C_-asNa1vXppB8m1_qmwxssfVy-7Og_AihijoI0mcxwlt2TvNOARA8whHJExtlsfcZeiuZeTVbEhPC78WE18bWFMXh6Pbhm10VM6LTrCtBmpI406FgE6uBVXg949Ru-Nj5Sc4rof72BttrfULctqMD_OArB4ChunePbWjXZ6NAU2gBNXiFQG_vam5mPzYqqeQmwWK5hhgAw2Sb7WYoxZU62VdXHc2zxctA6Vu4Ogcrr9IBE_18KOaG8XfmSbJr61U5Mxp1EL3xVWQ1FwDM6MW4Gpt2immKsbNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قشم همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67918" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67916">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=EHiP8n5xlJ0mg7Hdhow8oNGU8tgYF3fdwUhf_xVPn5Joabymhz9TwlVALjafE6fiMO6x0lRmiuB7efDEcZf-icv95swmB5QXRbpDwmyXlHPQB-mZvfdDy0wsfqXX_5Nrnf08GsmH3jf2CL-Rera2Sn-yHvF6kUO-tF8JGpvD_w8vTHcgoAXMDkjA4VgbAGE66RV_q-UooOQYQ4tUlgLUinnTsz-xbr0BasSpU8mvz4l3kf3uQY5R1neoSYAjg-jmMs3I90GMkrBvxFcsg7xoWmGlhkauiaCYcdjM2vIMXfgwA6npEVmTCXZjuOcZo5iDOBi4vU8J2hQylSh8V5noQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=EHiP8n5xlJ0mg7Hdhow8oNGU8tgYF3fdwUhf_xVPn5Joabymhz9TwlVALjafE6fiMO6x0lRmiuB7efDEcZf-icv95swmB5QXRbpDwmyXlHPQB-mZvfdDy0wsfqXX_5Nrnf08GsmH3jf2CL-Rera2Sn-yHvF6kUO-tF8JGpvD_w8vTHcgoAXMDkjA4VgbAGE66RV_q-UooOQYQ4tUlgLUinnTsz-xbr0BasSpU8mvz4l3kf3uQY5R1neoSYAjg-jmMs3I90GMkrBvxFcsg7xoWmGlhkauiaCYcdjM2vIMXfgwA6npEVmTCXZjuOcZo5iDOBi4vU8J2hQylSh8V5noQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67916" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67915">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🇮🇷
نایا:
نیروی قدس سپاه پاسداران انقلاب اسلامی، کشتی‌ها و شناورهای آمریکایی را که در منطقه "کیلومتر ۲۰" در تنگه هرمز فعالیت دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67915" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67914">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67914" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67913">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVn1PzW_0JQ9gpF3yN-VaF6f-xC0M6Xbj9bFkPuzs3DXU9kcfIIYxBsOqAFK3OlLLiZbasI6i4kuSvstuHQCpSZpHqhk8PL-i202XbMpZLWaGWMAFt0MyJF3rCxEleycD48gc111BFUUTvAl6QWqDJAz5_y00Mz2gAcvQLcrJtzpsF5qniXYPV4cBjX6iBdsap-YmA2NSS-EW_sZ-iItlMGaVLS4eBLw_wYBq7UVCYjzEtsQpQZWgViT_yZgi8WYCy05Yyb0lgKvKBOGV6j0R8iSWFi2e-3nPrt37h-Rf1AZQ8vMTYiUpPA9rItHu9QSTMVeKd8UYkJ3xj8z1Lxodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تروری که روزنامه همشهری منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67913" target="_blank">📅 19:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67912">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=UxtAK1rdoO9siUbNpfrT_hnNgz3aV-yvtZBjFRdXiC4-UBr1YDvhAPDEDK1e8dTNYmft07rr1LC_vFOS0YWUmz4sF0zib-GVtDLMDKnB6HxmW-FJBWZBKL0c8tFkKVNsELwY5VlY1PuF-EPU2k65wSPeU9J22Czz_6Cp2cF2rXfkQAJPTdg6azSu3njuWjcUP_76numq1JJ_Hhz1b3Eg9p5vCSU0nTTthCF8-BRxS0h2ze9KrqmECvR88mtFMGgrzhZcQuhFBHUuVXOvCkT-eh8EsUgjQuu2AgCwha4RHqjHEoa3xNG5-EZTsUf1TUVQAtvIRXWkul5eAbASWQsrjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=UxtAK1rdoO9siUbNpfrT_hnNgz3aV-yvtZBjFRdXiC4-UBr1YDvhAPDEDK1e8dTNYmft07rr1LC_vFOS0YWUmz4sF0zib-GVtDLMDKnB6HxmW-FJBWZBKL0c8tFkKVNsELwY5VlY1PuF-EPU2k65wSPeU9J22Czz_6Cp2cF2rXfkQAJPTdg6azSu3njuWjcUP_76numq1JJ_Hhz1b3Eg9p5vCSU0nTTthCF8-BRxS0h2ze9KrqmECvR88mtFMGgrzhZcQuhFBHUuVXOvCkT-eh8EsUgjQuu2AgCwha4RHqjHEoa3xNG5-EZTsUf1TUVQAtvIRXWkul5eAbASWQsrjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
دقایقی قبل از فوت سناتور لیندسی گراهام با او صحبت کردم و "او به جز خستگی حال خوبی داشت"
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67912" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67911">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
حمله موشکی ایران به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت.
گفته می‌شود این یگان در حمله دیشب به جنوب ایران حضور گسترده داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67911" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67910">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=f2HtCucojZpb8741cpYzQdeTfHB5LEw5wA09inlBm1JilM8YCT2TIF4RC4T1bvr0wLPjFaAgO2Ny9muOGjBEQsa0CD7hfclLIdLIlCE-dR1miL2U-Z7nyKVU28qVhFE7LbnTqUmjRRsfCLh585s1GYar-ALjVX68PM7cwRu-1NtdkUS7-uaXLnw05_FkFAKYpStyqyTG6aNfSjTfMYcM_CDllY0_BrFrhRHrsdZmI7OWPjlmGUwyhEmhtYO9vL__XINx_cPZ-W_zg-hP2m5wRMUPwVgk3hL8kikIhKKLnF71n9Pbxkl16_SNpTYY2FcihF0dHUFgGALvylt9WMvnRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=f2HtCucojZpb8741cpYzQdeTfHB5LEw5wA09inlBm1JilM8YCT2TIF4RC4T1bvr0wLPjFaAgO2Ny9muOGjBEQsa0CD7hfclLIdLIlCE-dR1miL2U-Z7nyKVU28qVhFE7LbnTqUmjRRsfCLh585s1GYar-ALjVX68PM7cwRu-1NtdkUS7-uaXLnw05_FkFAKYpStyqyTG6aNfSjTfMYcM_CDllY0_BrFrhRHrsdZmI7OWPjlmGUwyhEmhtYO9vL__XINx_cPZ-W_zg-hP2m5wRMUPwVgk3hL8kikIhKKLnF71n9Pbxkl16_SNpTYY2FcihF0dHUFgGALvylt9WMvnRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کویت کمی قبل
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67910" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67909">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsRJIkAXPxguwsZSX3hV9ieDHL05YleDr10WVUkFA-HHs6r_nzjH9zJrRki1ijxrDCCVDe_uqCCpgGDTwDhHndlaEd8ck91UwtSqY6qmxfC-SLG57xglwdyo3qrJ55Dac5VI-eyYdisubAIweE7TASZ6S0vBDefzv3aKWtPcoPvdAtkS8lov14MCp84uaGAdS8bUOL2nhrPwegwj4j1iKVtJeOSqUeRkKXi1961u1HBuVLB_PuuyYIpOOaHte_eqTXemCIEtQ_z5G2hlmOQrxFYHAso8n5KVgUlCPf5G3E6vkpyutS2wTZ5HKuSpBKIM_4mG2p6maGUI1NrVXBp81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دو انفجار در کویت و برخواستن ستون دود
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67909" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67908">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=mP6eOeUFVQ2MDvUXRHO943IoqaPbN-ksRshvCbiI9WCKeVvSkNUVfbGwKsdhQytMEVw8aRQkUUkP3XVCXP6klTI9GfmfMtB4-RQtQllkq66LDwMg1hJ2LMHQ12a7vExFNr0F6hjXpNUlL17k_id5IFXY0_NqsSQtHCvRlAyi8enOuBjhNiGBZY0vbyFaaEAEdXafuoOy5o8hfMJJnVHqlUomYsg7crLS8VdPne_67u-BO0KKb-rzET-uplP5gZmebBTZL96N_1BxGoQh8lLfXRielDshYUkPc2skNXz0dDwdW4IxQTmTCa83_brHBU8HWozoKTi1VMZgaQ9oxPOabA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=mP6eOeUFVQ2MDvUXRHO943IoqaPbN-ksRshvCbiI9WCKeVvSkNUVfbGwKsdhQytMEVw8aRQkUUkP3XVCXP6klTI9GfmfMtB4-RQtQllkq66LDwMg1hJ2LMHQ12a7vExFNr0F6hjXpNUlL17k_id5IFXY0_NqsSQtHCvRlAyi8enOuBjhNiGBZY0vbyFaaEAEdXafuoOy5o8hfMJJnVHqlUomYsg7crLS8VdPne_67u-BO0KKb-rzET-uplP5gZmebBTZL96N_1BxGoQh8lLfXRielDshYUkPc2skNXz0dDwdW4IxQTmTCa83_brHBU8HWozoKTi1VMZgaQ9oxPOabA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پرزیدنت ترامپ:
ما آخرین جلسه را با آنها داشتیم، آنها دیروز با یک توافق موافقت کردند، یک توافق عالی برای ما. نه هسته ای، نه این، نه آن، نه هیچ چیز. آنها همه چیز را رها کردند.
و بعد از آن اتاق را ترک کردند. و سپس در عرض یک ساعت یک پهپاد و یک کشتی را به آب انداختند.
گفتم شما افراد مریض هستید. شما افرادی مریض هستید
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67908" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67907">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILBZBTl4sSN3CPu1nQAEECylJyTiqkRWoZpVCsmch80V8l8Q-qJNDLT1yiqU39SUDXVKbSdV5NuuEZgSr_8J-YBW4JDO6lJ8L5P-Q36tbFl8WlnJ2vaUhyb14JZmnp9Ek5R4l04Z-oIVDtYQ4cfY7JPMbMZM9S3bp_c9Oz3YPnWWADctaUkrdT6_YU8W3EraGcedGFjdfDUt7lq51U2WJIUzVsRQdiv_TnNXwOH0XwwPLXzvGUzGtwF0tRqrTNX8L0Bcm2nPHjXWQPS6kwHRLZWOzPYiQccWkEt08Jtight1q0asx9gaAmA-bCnCXCiMxAwntr06H6r-oZ--fe8P_WCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILBZBTl4sSN3CPu1nQAEECylJyTiqkRWoZpVCsmch80V8l8Q-qJNDLT1yiqU39SUDXVKbSdV5NuuEZgSr_8J-YBW4JDO6lJ8L5P-Q36tbFl8WlnJ2vaUhyb14JZmnp9Ek5R4l04Z-oIVDtYQ4cfY7JPMbMZM9S3bp_c9Oz3YPnWWADctaUkrdT6_YU8W3EraGcedGFjdfDUt7lq51U2WJIUzVsRQdiv_TnNXwOH0XwwPLXzvGUzGtwF0tRqrTNX8L0Bcm2nPHjXWQPS6kwHRLZWOzPYiQccWkEt08Jtight1q0asx9gaAmA-bCnCXCiMxAwntr06H6r-oZ--fe8P_WCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
و شما بدیهی است که یک شبه دور جدیدی از حملات را آغاز کردید. ایران یک شبه گفت تنگه هرمز بسته است.
سنتکام امروز صبح بیرون آمد و گفت تنگه هرمز باز است. کدام است، آقای رئیس جمهور، و چگونه می خواهید پاسخ دهید؟»
🔴
ترامپ:
"این باز است، و من نمی خواهم در مورد آن صحبت کنم زیرا می خواهم زندگی لیندسی گراهام را گرامی بدارم، بنابراین نمی خواهم در مورد آن صحبت کنم. قبل از تماس به شما گفتم.
آره بازه ما دیشب آنها را بمباران کردیم. آنها افراد بسیار بسیار شرور و بیمار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67907" target="_blank">📅 18:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67906">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
یک فایل پنج‌ساعته از مکالمات بی‌سیم نیروهای سرکوب‌گر در اصفهان به ایران اینترنشنال رسیده که نشان می‌دهد نیروی انتظامی با مجوز استفاده از سلاح جنگی، در ۱۸ و ۱۹ دی‌ماه با کلاشنیکف و وینچستر به معترضان شلیک کردند.
دقایقی از مکالمات نیروهای انتظامی در بی‌سیم را در این ویدیو بشنوید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67906" target="_blank">📅 18:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=kVroxItbkeO7GhWrVu2CLvXBajnOknDcJNhDXa1bqj2rjXv08IlaBdwlbti9MK7gNfiaoVQOoByFLKR3WQ1OMXr4AFa6RH4ICAQsn7LjDN6oz69u5H3Mka-J-Ih2VJZvKIpGIIgvoFWBbH31mqokaU_3Cbc0pjdKK2vQ2L6hv1hKqWMtG1eYNQ7qqnIRw6ifc_7HKArEr0ML3sZhGd87X_-EWnArkRMQoNzz3DPxXkuyYdQRWHdVP6UCbIEwM7MUJJjiL-2L8HgRJPp8UYLGSoCisfefZ1igev6kz7J0aelH_sfSUi8t6OEVYW13OvwkH1JpL1r0EcRrrgvs1Ae6r4Q035gRwDEBkBhUwyM-cfPVWOVjhi-eWvLEjOfuqp9r18WXHlQC1fMEcpoLURBMrgouleQu4d0qL7XX60G9_LiFQ--k1kEviEQnIw0aFJM5HYCkxsptubld2oJ732g1DF0EfebMJyQtdYqGR6mwnAGOQ_WuwSk8OQidTes9db_hzPHFxtjAguij0N3p-ijvuplNtYkG1ksmq1zSUC2NkYcdKSE84huXVZehZc-J9wK20vnXAHrp66ZUQ3l37yTw9VEGonwk-CfMKndRnxY5ymCNI_9hXK2HSmmHdBDNQ0zspK5Aie3kGjxs6c8Y5hNcp-v6UwU_4VGT9wGQpob_sN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=kVroxItbkeO7GhWrVu2CLvXBajnOknDcJNhDXa1bqj2rjXv08IlaBdwlbti9MK7gNfiaoVQOoByFLKR3WQ1OMXr4AFa6RH4ICAQsn7LjDN6oz69u5H3Mka-J-Ih2VJZvKIpGIIgvoFWBbH31mqokaU_3Cbc0pjdKK2vQ2L6hv1hKqWMtG1eYNQ7qqnIRw6ifc_7HKArEr0ML3sZhGd87X_-EWnArkRMQoNzz3DPxXkuyYdQRWHdVP6UCbIEwM7MUJJjiL-2L8HgRJPp8UYLGSoCisfefZ1igev6kz7J0aelH_sfSUi8t6OEVYW13OvwkH1JpL1r0EcRrrgvs1Ae6r4Q035gRwDEBkBhUwyM-cfPVWOVjhi-eWvLEjOfuqp9r18WXHlQC1fMEcpoLURBMrgouleQu4d0qL7XX60G9_LiFQ--k1kEviEQnIw0aFJM5HYCkxsptubld2oJ732g1DF0EfebMJyQtdYqGR6mwnAGOQ_WuwSk8OQidTes9db_hzPHFxtjAguij0N3p-ijvuplNtYkG1ksmq1zSUC2NkYcdKSE84huXVZehZc-J9wK20vnXAHrp66ZUQ3l37yTw9VEGonwk-CfMKndRnxY5ymCNI_9hXK2HSmmHdBDNQ0zspK5Aie3kGjxs6c8Y5hNcp-v6UwU_4VGT9wGQpob_sN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از  فعالیت موشک‌های رهگیر پاتریوت بر علیه موشک‌های ایرانی در پایگاه موفق السلطی اردن از دید سرباز آمریکایی طی درگیری‌های روز‌های اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67904">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=mRJC36dCPL6FsMU4XGvzvOSyV_ITFbDh2wC_jcBNBDh1O4t-UWpglZKukAWLfjpOI9Cnynulw9QdzDUsp-_RaGe3d82K8gREpbfOOZViiLmamFN7rlQhPruvn8UgypGgMzkFQ8xHRixdEttxT717fyYcqzi5_LCr2jzKcQe-wGR3JPXhnWL-MTsUvhIQEytcnkcZAOuNQVd-6XwLSYhqi7I0NB4nkOQ5J31gJtfpJU0nOPytW8AeJm6BPqd4jzvDM51a0eBGiHAyuTkpY40GyPf72R_KY0WN4xMoq2TuBcEZ9Y4tqLTgEu4FosYEKZpeB81C0rdLsMup0vh-u7tM3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=mRJC36dCPL6FsMU4XGvzvOSyV_ITFbDh2wC_jcBNBDh1O4t-UWpglZKukAWLfjpOI9Cnynulw9QdzDUsp-_RaGe3d82K8gREpbfOOZViiLmamFN7rlQhPruvn8UgypGgMzkFQ8xHRixdEttxT717fyYcqzi5_LCr2jzKcQe-wGR3JPXhnWL-MTsUvhIQEytcnkcZAOuNQVd-6XwLSYhqi7I0NB4nkOQ5J31gJtfpJU0nOPytW8AeJm6BPqd4jzvDM51a0eBGiHAyuTkpY40GyPf72R_KY0WN4xMoq2TuBcEZ9Y4tqLTgEu4FosYEKZpeB81C0rdLsMup0vh-u7tM3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن سرباز بر اثر انفجار اشتباهی در تمرین پدافند هوایی روسیه(نزدیک بود همرزمش رو هم بگا بده)
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67904" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67903">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1fARVTsDQDAd73dpAtFEuT5Ymaucwfg2drtZq3pbCyJpwajCquu3D6x3TVXjEhIN5kln-p4LaZFjQWYvUOAPlPoftWN-YhEjwwqFYRvpZOXyeJ9Nb2oIjajUYxYotyxvTC86ITe3iTLcS7kmQkEVRtYh3WgbT_AThW50Zqlitgmk7Hy820wdGdW7ZaekiQnamusY0svo3CqhB1j_Pl4gK3v_mmuFqaSP00bo0fGlYWV4xLgAkpOs9rJB3hFTAZGx76Fu09Gv7t5gzFWAZqVJWfCXzGTph4WUaag7mLCrpm6gQcAPOFzoOCB-TU4QOXFHXBaDrK6GxH59PcP1YFrzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمامی کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای آمریکایی در این منطقه مستقر هستند و آماده‌اند تا از آزادی تردد دریایی اطمینان حاصل کنند، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران. ایران کنترل این تنگه را بر عهده ندارد. ترددها به روال عادی خود ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67903" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67901">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AngQuHc1kSNhOBZe5jZ-GTPQFbexNxoEd0qBPgfY4lBciORd9JcHsIb35zVkj7XN6OEcrsN7zU-g_VLwhVTdjOKbnO7TnZKTCu3MuhCOAYHlyvGstNtZn7evreJ_0CK6T0NLkze_1yPSUa12U7o70F5xYH0x2rktB_3G-eF89E_wEArHsEmF50vzo-nl4grkHVkqyTXgVOOQS0wj4z4HkrcTwB1ErxTsrqci32JOIfJaiHQxDldWH8oD8eh7u0W4oiNSAwOOn3-wcDY6TRSGKtQcyZHPz-5eBVy4cQxYgP5hG8wPSy_lnclZizupGGKdkP8mWPzaVbmvi8Uva6awRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=M0TEV56Axg8L9PfndO1_oGQgKMKvLYXrvNWE-GkUJ8k1H7vWhu1TyFqXCEsmPrXyu2fZZk_MMUiGDseTJ6O_kecPlgUXOxkOuiK6vlAdDcNvin8uI6ygARKi6CzhHldxeU1P6jtqADwWaRBxugcYROtLY6t1Lr3SPQaMLzm2wk3aflPG_P-En34FZuvMnieD__xRq-SfSnoGjQC4M0l6e-v7QZ9obiY8HE06PcF5at4XbYtUEYu_Ylwa_pyPUoRQUOlWidvGGdvzQsCwMrZjC1xwlV6fuErhBh9oB9JXww4fq1du2us4xvnVy_Nd3L2Q-8RTcSDbCr-tBHPG-tUgCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=M0TEV56Axg8L9PfndO1_oGQgKMKvLYXrvNWE-GkUJ8k1H7vWhu1TyFqXCEsmPrXyu2fZZk_MMUiGDseTJ6O_kecPlgUXOxkOuiK6vlAdDcNvin8uI6ygARKi6CzhHldxeU1P6jtqADwWaRBxugcYROtLY6t1Lr3SPQaMLzm2wk3aflPG_P-En34FZuvMnieD__xRq-SfSnoGjQC4M0l6e-v7QZ9obiY8HE06PcF5at4XbYtUEYu_Ylwa_pyPUoRQUOlWidvGGdvzQsCwMrZjC1xwlV6fuErhBh9oB9JXww4fq1du2us4xvnVy_Nd3L2Q-8RTcSDbCr-tBHPG-tUgCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از اینکه صداسیما رسما مرگ لیندزی گراهام رو تبریک گفت
فیلم تبریکش بشدت در رسانه های جهانی وایرال شده و گویا برخی دنبال ربط دادن مرگش به جمهوری اسلامی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67901" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67900">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0jueHyLwRSLLpRs5I0t_9tG4u4bHTPUMQssWpZJB9H6P2SjA7WMMSZYIWyPPDe2C9b4BqlZWYpQYlB7zKLPbzgvMXPOevcgMEr_6u3ChKFuxosUpiDerg5otcn8B0dXtHzsIO0WtNGEetHDA7_Hg2wxhjzuyNus_9OWty7VjESjjU_WMhU5l3oI1SczOVEmqG-MCog68jxtCJc-18-vNwcTW_yToGZmCPeRa8fhlLTYbUjdHUpTFEbhZVBsTOWMhjswZJMa9qwmmRIYpzWRCthGVupB62TCHOIeOS4f8OKw5IqRtNs6EcLW3rpg5kW-tvzfbXRhLUjy9xctgZBWQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پس از شلیک چندین موشک بالستیک به کشور قطر در طول شب گذشته، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، ضمن ابراز همدردی صمیمانه، به خانواده و مردم قطر تسلیت گفت و مراتب تسلیت خود را به مناسبت درگذشت امیر سابق قطر اعلام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67900" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67899">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=qku9qQnS65abQw83nOFMzIBZztceq-41MDD9T3HE-OGJFvodBpMEJcjbZxvr5uKuQ8Uwa-wBAV9n8OoirMhhsNSf8XmE7znFW-j51z6W7PSOBUVjRJSS0XG87bi81IPU639-qBNnKxI2UY1bX8PaepTT2FcQcJL3B8DRzCQ3Kro2lFGfqRQ0-TQjPWJsXr8pbEnx04dWeTtnSWRbwaaCL_9Ohc54JKudQacNf3WoKbO_5o-5hxvHSXo7Xelv04WqEM02ONsGoiolqdvfPqG8MKs1rEOs2rwrtiAMeQq5Z-GBnS9vkkQ7KFl30GJz4gNxF6j93zXBFnp1BvI3kJ4PLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=qku9qQnS65abQw83nOFMzIBZztceq-41MDD9T3HE-OGJFvodBpMEJcjbZxvr5uKuQ8Uwa-wBAV9n8OoirMhhsNSf8XmE7znFW-j51z6W7PSOBUVjRJSS0XG87bi81IPU639-qBNnKxI2UY1bX8PaepTT2FcQcJL3B8DRzCQ3Kro2lFGfqRQ0-TQjPWJsXr8pbEnx04dWeTtnSWRbwaaCL_9Ohc54JKudQacNf3WoKbO_5o-5hxvHSXo7Xelv04WqEM02ONsGoiolqdvfPqG8MKs1rEOs2rwrtiAMeQq5Z-GBnS9vkkQ7KFl30GJz4gNxF6j93zXBFnp1BvI3kJ4PLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش ممد سامتینگ در حالی که تندرو ها دارن شعار
«مذاکره با دشمن خیانت است به میهن»
میدن در مراسم چالسپاری خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67899" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67898">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67898" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGx5imS5g6LicAjiJXGAQpS3ImCK7KtOsAMQxb9e6UC49g90g0kqvAkmLuyBaSy9WzExvp0fE0Pz19-1D1DsmtnklKDaXilbrrowwFHlCL2eBb7lcOSfeDUaQk0eXEAhQMrUfyXnzM0EIeY9IOxudeLkKd53_5F-_hus_dtPunWq0SPsAdre0q330Uy3GQvKp65CtBGqPwhYdwYmMOdsjSrAvqtI6iIU9mIqf1Y4SB_452upmfnuI2IvxVMJY_PDTlmYxeMMUCooiN8GO6tEQ5jqkWz4F8L-wk7KkhxvH29GweTRm8HqpFayOiLCWSkahx4raaTaSG3w-IkSOf4eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAB4NAAMTgBNPKw9vSuCDmfTNRpegFeORNfYl3sdTFFTHR_zF8zlXL8-wBii1GX2J8foV7hm4yhD2Txg9xcYbYxXHx2ZBonoS_7B8j1X7PNXqe_0qIV7uwo_6rvNAT4CinuCAEN3reKB9n5maZtBZX34-Q4nc9xTFVhbB0eWQy2fq07RhNH_JSxXV--dbK9j8oEYjqB7-BXGPORInyoLKDFUN3QCpFN6-z5ddlDJleF03KKann8QIlJCDyuTirb7a9GiGGbVghXEklOEs_0temx5fMM85D0__uyc4PCyWFGcIO8VLVMbyz65XYiTLb4o8zqb4a6gzJaJTsiQrn69DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmWNxtdxc5a4ET-Wfu22AzYsTJB-jfthp7DnsmFxIVA5JTMm0RUGWnGpcYhubzGOAqy-zGsvUoJp7aBYfUrjauk0ZZWRIoprBPwePX_Ct_5FedJIbskvebUwa4Z6e6hE4-A_p-ov_48xOrRB_9Y_8uveJO3smBl9UUtZQM9nI_fjkQHdWesJG6OHeDraQG8Ujkz7mUJImc-gS817TXBmESzHJsJ9iDjYu8LGSAl7ipmENMOcv8znBB-EfHzQhi3ABqngkkSqi-x7x_nq5VNP7ivB9sekhPBb1LX0ZBBJQ5leYJE8bGBmLOOxl75sFJsQw1Ciyn4PmRSeZPD20ktLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👑
شاهزاده رضا پهلوی:
از درگذشت ناگهانی سناتور لیندزی گراهام، دوستی ثابت‌قدم برای مردم ایران و مدافعی سرافراز برای آزادی، عمیقاً اندوهگینم.
در لحظاتی که نیاز به موضع‌گیری اخلاقیِ صریح و درست بود، سناتور گراهام در جانب حق ایستاد. آنگاه که دوستانِ واقعی کمیاب بودند، او در مبارزه علیه استبداد، در کنار مردم ایران ایستاد.
او از صدای خود بهره گرفت تا اطمینان حاصل کند که صدای مبارزانِ راه عدالت در راهروهای قدرت شنیده می‌شود.
حمایت او از «انقلاب شیر و خورشید» ایران، لقب «عمو لیندزی» را در میان ایرانیان برایش به ارمغان آورد.
یاد او همواره با سپاس و احترامی عمیق گرامی داشته خواهد شد. ما مراتب تسلیت عمیق خود را به خانواده، عزیزان و همکاران سناتور گراهام، و همچنین به مردم کارولینای جنوبی و ایالات متحده ابراز می‌داریم.
روحش شاد و یادش گرامی باد؛ و باشد که دیگران راه مبارزه برای آزادی را ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkSRYPDo8-un-L7cP0WRd7T2k4-NQwkh9S-fPt15yEOvEo74glHmNiz0GeVG4lowoH_Oso2UkRpYkCidZEJRrHEHikbEedUOZNBGrT3jf2cB35AvGNVm62F4j4S7Z-KvPBHlmfG87_tFInGbM_4RSNmSobqprnq1dNtdWCUhYGAx0NrUdje_WnEr_0OclcJbusPc1GvU9FfWu4g5xltQXY-38gpQi0XmVFpE4b3V5kZ1blLM5AjIP5Z2udPGP96nktJOkckJ6Ef-lpgVsj58AQqtsl6BSgF0mmKEIUDWZIbF6aN7LN4aN8ClV8-6-zlPXEzAowQdHfuxpukqM0L9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو نخست وزیر اسرائیل در سوگ مرگ لیندسی گراهام:
من و سارا با مردم آمریکا به خاطر از دست دادن دوست عزیزمان، سناتور لیندزی گراهام، غمگین هستیم.
در ملاقات اخیرمان گفتم: "لیندسی دوست بزرگ اسرائیل و دوست عزیز من است. ما هیچ دوستی بهتر از لیندسی نداریم.
لیندزی فهمید که امنیت اسرائیل و آمریکا جدایی ناپذیر هستند. او زندگی خود را وقف دفاع از آمریکا، تقویت اتحاد ما و ایستادگی برای جهان آزاد کرد.
اسرائیل یکی از بزرگترین دوستان خود را از دست داده است. آمریکا یک میهن پرست بزرگ را از دست داده است. من یک دوست عزیز را از دست داده ام
.
قلب ما با خانواده لیندزی و با مردم آمریکا در این زمان سخت است. باشد که ارزش ها و ابتکارات او همچنان ما را به سوی پیروزی و صلح رهنمون سازد و یادش همیشه پر برکت باد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSsHegptCmCMLwSd17qk2t5bUaBGrrZ95QjlBL_F7dSQnZGUtqLkKZKjsojnzpZbzBEKdN3zmSI2eW6TS_hqhO_yzmSOa79ZXPIEQlxV2NuLM-OIvfzeocza5ClE8ipNQ4qP0s6EHMSM4YQx8LbnfQhZXjEjOccSvqRYEmNuffOgjvXXajfDylL4RuxHDGJdWwaxqYyURk8DOd5XcvpIYSmyLxfKk2LgDyRXD5GDSoU0ghJrqUKd7ZimvWAwtsjPl00nHKRX8jIzIKUjTXajmf9D7LosNMsowo6W1uk5l3vUFxHepjMA1S3kn9RUWKMFStK1Oxc4rppFSnlxcOw6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAyhv2jFRgm3N4aoWDODVd4uJ_HNJA8oI7EN_nrJ7RPd9g_NM5GFbN_rcxlf0XdBGpdr66kUZaxTIhS2c52KeAQam1UxYdKM2qELTxrKrk9l9eJG0x9TjV_FBZDErTius6Ujifk5yIRdupllYKcb0d9Ts3abd-mmeDOLzTIQhsBZNBV6J5zNJWl3K4VHEEPdY0HmFk_0Eb4MGnd5ZVLxzDc7RVCAXn42b16bzL5nn2kPI2aOKmLO6hbHp-conwO5UW5YVSj5Ogsd2eiUF1K8bFBATzKKUYFjP2F_7boJJNDCjMMXFZ6Rcvf2v4qggTQVGFEGvMQTi0t0XY7Z8_aU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsHNkQmLQTTnZM1sz5py3pSjwYo3h_tOoI3Yo_4Tyf78CEL61WKi2RWERSfFFfaUrPt_VBTyRMZXNJ05_5HexvSYzHwifQYgwFuMrMx-0pE9RoHP9MJSTJTc-SgSz3m5Tux-q4CcLLUeFl7UVoIQJg0rd4YWe-t_nOUC9mnI3m7Zmyd7G9T1P9Dmd3RU8W5YExnF6cf2mNSEdOg_C7yg_GvOzb3mOyq0wjlcqb-DAxU8PZiZ4tN4DWZwZWxinfGVoeJMAlYgS4LCFfkCEoQePFeWvFWO0T82fhJj9yO-hXh15N2V4NL85dOasqgNWG4_7omtTZm_G3xReqJ9AbbxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIojAN5DLvesx_UNJ9HxlYj1OFlCNLtarJJjax1umiEllfaBc3vLLmbf1TVZBWlSQFf545bq5KA4TcpDTsNFqkZqb1uXFreBy0v9S8_xh0KSOyOSOP6JRl_H1smJb_0VIpMXHULHWkLu35JfUD9CPtITt-edcy_zmmkRIA3eynsPpu_anTsj9uQ677bsiq496cvxKzcuGIuYbat_kmrSod5qooY5d9mAy2tBafFrPj-y2rSZMPMg_71arcrZTDa9dlmgH9d5vAE8uOt2IdNbF7vaBrGmNswwsmfYJhYHsApY7xvgDuyZ0PF3-EFpuHs2WdTSSOh4261ohhKX2HivKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5RT1S5XATe9fojYRvKvL8kb5g5_rLA6yrGw8PZarYijSIzdfZHx91l2URpPgZ1mfhWzB0Yw0RNnPBaF-Hv3mD1US8CCfM4iq8MhUvzo_yhjjq7_sbJHwiYahnCfY5nTLr7MT4y7I5CGM2rbp7sEvy3bRy89Ue_LrrT8H82SS8qkvDv2yTr9jcCcHsfPQESrGdPitF34_RYSBfIGKuQEcLjbvfhE6CWQejlNVlfDWbpbUwHHC4Pd59LN37nf2D5JjuYalDhThTNdb4ewljQy-hW0brLEUMbmCrDZwWGZmgCfJJMzzbKjVwllbyb2Lb3C6E5auobxQFWY4lMKZNrvdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPjZNGn5Nis6lyD3i9cEeQmbYmwzRAl7kB-UTbJZCQzwSwKSq9_7QNG-fdtEhI0NP6o4XCz0WWSF_IOUN4PjAEJIy9Zoupncce9hGfsCJipdXaRzx_VwyFGeHnWuU1hH_t1u9Xj7hiOJafitj16snBgBINMkP9xsJAzNutCe4suOpu9VLx6PQnJ2ytTB_QNsduNIyYumRygeI_UmVRdanZl2Hs7oONiq7I2cMFv30ABT3D-07vshGCYxnWi-d0iWe6Oz6Vh6CYKVY92gTFav6oACi1a3Y3N_qvDUubruEBk1iRApMjLAaNYiHJG0cHZBL5SQs8eojc2FhKZPueDPxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
