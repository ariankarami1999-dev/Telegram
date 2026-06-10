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
<img src="https://cdn4.telesco.pe/file/Wnddt4d1UHGbXjSYSQL33owErkEaAUxMdSx03aFpSPMjgVIN0J-8sPQTfo_y7Yxw9BmqaaUaVnTIhEyGtaj5qtaKUjQFMu9bnj6Vqtu-bqYhqjeNrNO1aE_OFf5Uo21W4KfavVRiDrgoZsS5vLV3TtXQO7mbjCrvKvlLgqXaHa9aRW3pXLrZnGVsGMrQClxITzoXAc1_kfm1a1cVoOy2-a7Ilj6M6OWoPPD8HlaYnQm3Np4mq_vCqMn6DLv1Gcvx6d0qCUvFT7gxndjr0k4f-1y0gBfLmYeN55wSkF2gzjPRyjNTcJvdSuCUdvLedpp1riLKOigX4dee9dPySGELrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 14:36:43</div>
<hr>

<div class="tg-post" id="msg-77453">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کن معروف ترین آرتیست مملکت از پشت تلفن زندان موزیک خونده داده بیرون</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/funhiphop/77453" target="_blank">📅 14:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77452">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">واقعا این ترک جدید تتلو رو گوش دادم خیلی ناراحت شدم، درسته خارکسه بود ولی اگه قرار بود خارکسه بودن جرم باشه نصف کشور الان میباید زندان میبودن
ول کنید این بدبخت روانیو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/funhiphop/77452" target="_blank">📅 14:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77451">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دستاورد طلایی جنگ های اخیر تو سهمیه کنکور سالهای آینده شکوفا میشه
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/77451" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77450">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دیروز روز جهانی سکس بود برا همین تو خاورمیانه همو داشتن میگاییدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/funhiphop/77450" target="_blank">📅 12:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77449">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سلام صبحتون بخیر، متاسفانه دیشب خواب بودم متوجه حملات سپاه به کشورای خلیج فارس نشدم.
#بیکینی_باتم_تسلیت
💔
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/funhiphop/77449" target="_blank">📅 11:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77448">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ممرضا بنازمت دیشب بعد از مدت ها خندوندیمون</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/77448" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77447">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سوپرپانچ دیشب شایع که جنگ فیدش کرد : کونمو مشتی بخورید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77447" target="_blank">📅 09:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77445">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSvEga9r9WYbTKOSFbnrG9O2YyyIDeiKuCBGXnKTiWfvPTU5p0XZi-Jye3kTyUdlX171mkLxWP_GGGVUWnlJHLx8owdvpzsR03nxICn-Fv4Tgy01owqv6bxTrpX-CFCTxthfHaVyKze5h_j1s2JI6ye09ErMZq9GFV3BCLlTfNmjH255Pib7J3wkcdj7fRNV1M9iNhqrZMb4MEFtxI8fyTTrq3qc5es3NVT4cNkSMC9jxKWEghqCre_Qu6S_4RLC5Pa-JivcVmWqzlP-9VYebuDa-GxNnyZKEC5cEPI25tpRntavCoGWqVvW6KRi3klIuDJu5vsPzjWiIoD5FeL_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGs5yjKmJVHY1jVkN1rTEPLND5ECC4gzAruD-uD2OX-A-HoVihnMLx5aM0aKFTZnZXui_DJfq4a4gwmk_cmnBIMgEL10CQf1oyGKHrNuwJB39W-VauAVRXZtxaR2O9PKx5U9rNVH7n1m1xwHKd9vS4hH_CgNnQxrV-lrMZvPJ2TAnb9DAcFdtWJ-9P-OUyJwdhQeli4MbfGdQx-RwUypWivf19Xhot_Uy_bNhPoZP3x29AFb8gUL6waB4M-RnP0RHcS19WY9BbBuT_bMfZ_I1y0L25CDzwYV-HrmQ9qlYY9NDu4lqBmF4E3-UIZadpHUXyMSRXGwi5cN2uOqQR1wRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط و فقط یک روز تا شروع جام‌جهانی.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77445" target="_blank">📅 09:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77444">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6KaNWgNCKMr8k4PiUZyg97Jqtu3zrO_C4WSo0iqXpBr_R6c8enXGY1ARiLRohxb2D_M5zMx1DztGc2KElC30oS05Rm9wqkJaZMGxpWaK_UUsdPY6h0ASbQL1mYWN2-EAfuFFR3eimMoajsKfY5pn4CM-17iUVXZ0EFxoKlSkoX7LxOWs9ZWn53ltsNA4wu0a4fpKTXDnRSlwda11OerdbYQCkRN6yApC_vDvxRg3UQjWh0Kzf4negR0haIiebM8V00caY_Pxxg-JXK-jJh329oWrCgrxnQRGmJt1us_YOlFKWPipGF-a0TlY5gd_G3Evj9mb6vSmD0AXyp6SESDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پرتغال
🇵🇹
-
🇳🇬
نیجریه
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
چهارشنبه ساعت ۲۳:۱۵
🏟
ورزشگاه دکتر ماگالهیز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
نیجریه در
۱۰
دیدار اخیر خود،
شش
برد و
چهار
تساوی کسب کرده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیجریه
۲
.
۶
گل در هر بازی بوده است.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
👍
ورود به سایت با فیلترشکن
R20
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/77444" target="_blank">📅 09:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77443">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وزیر علوم: سهمیه جنگ ۴۰ روزه در کنکور ۱۴۰۵ قطعی شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/funhiphop/77443" target="_blank">📅 09:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77442">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هرچی نخاله تو ترکیه و امارات بود کم کم دارن برمیگردن ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/77442" target="_blank">📅 09:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77441">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وای نه تروخدا بس
آژیرها دوباره در بحرین فعال شدند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77441" target="_blank">📅 06:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77440">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آژیرها در کویت فعال شدند.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77440" target="_blank">📅 06:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77439">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آژیرها در کویت فعال شدند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77439" target="_blank">📅 05:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77437">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی: بسم الله قاصم الجبارین فمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن ۲۱ هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77437" target="_blank">📅 05:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77436">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=DSbG5dPjpmtJoky6oCThT0GKfG45jVwJUvLS93UUfbfCic5gR19Ftv5bPYDrRZ7V2nNnM97VmkobfYSlT-p7V7tRkKmfwN_TUXQZOmgnKaLE-Vh1QU22cpU_z5zRPUrP2ZXfxITb6h1iKdsvBTcg0xhviOo62qGQJFsVGRFgU8CLPMZ4BUbuYonKBiG8F9uiO3AvZ6LCyD7u_bNu7Rc5HUm63_LGRTy9fGp7Ce1M0y_ojCR445UFpDcARsjoq1eyH_FBR_XDI03hsctDZPFaIjNV2R4tCNkfWVG59N925Ngfi2dui-wgeaIBUf9r3NHMRSMwwC4DN7nxwMV-a56orw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=DSbG5dPjpmtJoky6oCThT0GKfG45jVwJUvLS93UUfbfCic5gR19Ftv5bPYDrRZ7V2nNnM97VmkobfYSlT-p7V7tRkKmfwN_TUXQZOmgnKaLE-Vh1QU22cpU_z5zRPUrP2ZXfxITb6h1iKdsvBTcg0xhviOo62qGQJFsVGRFgU8CLPMZ4BUbuYonKBiG8F9uiO3AvZ6LCyD7u_bNu7Rc5HUm63_LGRTy9fGp7Ce1M0y_ojCR445UFpDcARsjoq1eyH_FBR_XDI03hsctDZPFaIjNV2R4tCNkfWVG59N925Ngfi2dui-wgeaIBUf9r3NHMRSMwwC4DN7nxwMV-a56orw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
فمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ
به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن ۲۱ هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط کردن یک فروند پهپاد MQ9 در آسمان شهرستان جم، با توجه به تداوم شرارتهای دشمن در تکمیل عملیات مقابله به مثل، قوای اسلام و رزمندگان شجاع هوافضای سپاه توسط موشک های سوخت جامد دور برد خود ۴ هدف مهم از جمله آشیانه های جنگنده های F35 در پایگاه هوایی و مرکز فرمانده کنترل ارتش کودک‌کش آمریکا در الازرق اردن را مورد هدف قرار داده و منهدم کردند.
نیروهای ما آماده پاسخ کوبنده و قاطع به هرگونه تجاوز مجدد دشمن هستند و عواقب هر تجاوز مجدد بر عهده دشمن آمریکایی میباشد.
و ما النصر الا من عندالله العزیز الحکیم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77436" target="_blank">📅 05:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77435">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه موشک بالستیک دیگه از اصفهان شلیک شد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/funhiphop/77435" target="_blank">📅 05:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77433">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه موشک بالستیک دیگه از اصفهان شلیک شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/funhiphop/77433" target="_blank">📅 05:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77432">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزارت دفاع بحرین: تمام موشک های ارسال شده رهگیری شدن.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/77432" target="_blank">📅 05:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77431">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزارت دفاع بحرین:
تمام موشک های ارسال شده رهگیری شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/77431" target="_blank">📅 05:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77430">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">احتمالش بالاست که موشکا وسط راه فیل شده باشن. چون ما تا الان باید گزارش برخورد می‌داشتیم درحالیکه هیچ کشوری تو خاورمیانه هنوز آژیر هشدار هم نزده.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/funhiphop/77430" target="_blank">📅 05:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77429">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انفجار تو بحرین گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/funhiphop/77429" target="_blank">📅 05:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77428">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IntkDPpWvSEdijC044DSK5yt6LqzX3X8dSsRh0D4kyH-6SdUEzel0Q04NhjPE435YQ1ZZee1VqzFKPXmrdAzq0PIdnK1NDfXzWLbLTQnqVbED_0Zhk6_ZSFQWlLWCIkW5vadMcQk9jxwO8aBwhzfH3Po9bsE_fqzcmydhZTtnxbgGIJFwuLEwKuJlPClZM4l9H3ge5maCl1qRMbgTMe7lu1vKhX0GC1aiOYgLcyHxy2IMY7NSPb1VQK_1gqS-MB-OdpVIPmefC1wvsY25INYITeFXUmulINwkhvOVWKUOZt8OmKJ4AnOlk_3gmmRjpj35G5rVqv60cGL2hAFPcevvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحرین به شهرونداش هشدار داد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/77428" target="_blank">📅 05:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77427">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اوه اوه سپاه جدی جواب داد.
گزارش‌های اولیه از حمله‌ی پهپادی سپاه پاسداران انقلاب اسلامی به مقر کردهای منطقه‌ی اربیل عراق.
🔥
🔥
🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/funhiphop/77427" target="_blank">📅 04:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77426">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">احتمالش بالاست که موشکا وسط راه فیل شده باشن. چون ما تا الان باید گزارش برخورد می‌داشتیم درحالیکه هیچ کشوری تو خاورمیانه هنوز آژیر هشدار هم نزده.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/funhiphop/77426" target="_blank">📅 04:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نخوابید که سلطان بیدار شده  ۳ موشک بالستیک شلیک شده  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/funhiphop/77425" target="_blank">📅 04:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=HCLQATnDZOtgKj_C7QEXTAbS4f0FKOL-DHaKe6trB1yPplBNXWuB8Gzu9afDMjeYrSaeIkniygiIgedDEucMmhie1dfIjmaaS6LDXTRISUiRzSwMQsWXGqtZUObO5OchfkFlp52-spVWole5whPZ_MFBJhjIgZtDNUwMSKuEEHXzGQPeBIzRSdQP4NVmvEOlN9s8khxk7gQB39m8bK7zEPgk9zwsyqWbeNS4mB_Zav43G6VvXX-2O99cn64EwcafCS8xkATlTTZD9evof4u-RN_o2IApFVeWRp-ECOoDdmTUSAWdWeHnSDVHKcidqcut-U6QqX4uhgGt27XEiOvkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=HCLQATnDZOtgKj_C7QEXTAbS4f0FKOL-DHaKe6trB1yPplBNXWuB8Gzu9afDMjeYrSaeIkniygiIgedDEucMmhie1dfIjmaaS6LDXTRISUiRzSwMQsWXGqtZUObO5OchfkFlp52-spVWole5whPZ_MFBJhjIgZtDNUwMSKuEEHXzGQPeBIzRSdQP4NVmvEOlN9s8khxk7gQB39m8bK7zEPgk9zwsyqWbeNS4mB_Zav43G6VvXX-2O99cn64EwcafCS8xkATlTTZD9evof4u-RN_o2IApFVeWRp-ECOoDdmTUSAWdWeHnSDVHKcidqcut-U6QqX4uhgGt27XEiOvkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا همش برنامه امریکا واس جام جهانی هست ساعت خواب ها با امریکا تنظیم شده دیگ میشه راحت بازی هارو نگاه کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/77424" target="_blank">📅 04:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77423">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نخوابید که سلطان بیدار شده  ۳ موشک بالستیک شلیک شده  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/funhiphop/77423" target="_blank">📅 04:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77422">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بزارید سید مجید نقطه زن بیدار بشه تلافی میکنه امشبو</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/funhiphop/77422" target="_blank">📅 04:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77421">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حملات هوایی امریکا تکمیل شد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/funhiphop/77421" target="_blank">📅 04:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77420">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حملات هوایی امریکا تکمیل شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/funhiphop/77420" target="_blank">📅 04:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77419">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا می‌گه ما پاسخمون دادیم تموم شده رفته شما داغ بودید نفهمیدید: در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانه واهی سقوط بالگرد خود، برخی از پایگاه های آمریکا که در منطقه که نام نمی‌بریم هدف هجوم قدرتمند ارتش قهرمان…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/funhiphop/77419" target="_blank">📅 04:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77418">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا می‌گه ما پاسخمون دادیم تموم شده رفته شما داغ بودید نفهمیدید:
در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانه واهی سقوط بالگرد خود، برخی از پایگاه های آمریکا که در منطقه که نام نمی‌بریم هدف هجوم قدرتمند ارتش قهرمان جمهوری اسلامی و دلاورمردان سپاه پاسداران انقلاب اسلامی قرار گرفت.
ارتش جنایتکار آمریکا بداند در صورت تکرار تعرض به جمهوری اسلامی ایران، حملات سهمگین و گسترده تر علیه بانک اهداف تعیین شده در منطقه انجام خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/funhiphop/77418" target="_blank">📅 04:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77417">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f906ee6c6a.mp4?token=cTvk2ugR9OjwCdzTkOjgylfo0vJ6Oxy-qW71YRkij53cz1HWNjMJKo4nZkXKW7mCeHl0w12aQstk1nRXoAys84QXWjC4FziYy1hTgdsHHp9cFW_s9gAH0IBqONBKqchFMIl3yYgGwuA7UqO8pMCnXF2AGXEWbUqmhQgGNUWfi88c4tPl3Pl_ORPSe6YkIiYYTiNa5qpW2gY-MBLN-U49fshfJYU5h6Pvpf_qPAMmE4C6cyQ7fAZiitLDj6XspmUmhujK4jsj8DOhmEwddFV6YL4F7RygxavznOtEJypce03_YQkNEhhzI6nYF_FfMjzdfyjruLlEedwkdqC6U0MAj1xyM3fDvyfgM9IRDF5c9pABZlNizfdvMCMWgdurc1KWWMGJJNJ0Q5VzcUSOp4G4_FGyUXEEWbTi9Fe6FLAl6dviI6oI6BHj4q68IaOMWHTLVZhUeyxZRDyrEphmgtmhwPRrDaseCla8zixi-r8XnY16XD7Nf1hlXVrWUEMmzRhX00xzrvWD12hqtNAu3sVGztm4mvEGKAygK8QqS2OufOqqbF3EZV0Pdz8MtL81nNPPyci6xCeecWk6HuzFG9c4HXN1VXyhoXlaW0h3vqrmDpZizL5hNdBeGTZZdKIiY3Yvum8K1vNwurzIYWhZl2zTWY9iyD9oelOHuB7XwPqr_TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f906ee6c6a.mp4?token=cTvk2ugR9OjwCdzTkOjgylfo0vJ6Oxy-qW71YRkij53cz1HWNjMJKo4nZkXKW7mCeHl0w12aQstk1nRXoAys84QXWjC4FziYy1hTgdsHHp9cFW_s9gAH0IBqONBKqchFMIl3yYgGwuA7UqO8pMCnXF2AGXEWbUqmhQgGNUWfi88c4tPl3Pl_ORPSe6YkIiYYTiNa5qpW2gY-MBLN-U49fshfJYU5h6Pvpf_qPAMmE4C6cyQ7fAZiitLDj6XspmUmhujK4jsj8DOhmEwddFV6YL4F7RygxavznOtEJypce03_YQkNEhhzI6nYF_FfMjzdfyjruLlEedwkdqC6U0MAj1xyM3fDvyfgM9IRDF5c9pABZlNizfdvMCMWgdurc1KWWMGJJNJ0Q5VzcUSOp4G4_FGyUXEEWbTi9Fe6FLAl6dviI6oI6BHj4q68IaOMWHTLVZhUeyxZRDyrEphmgtmhwPRrDaseCla8zixi-r8XnY16XD7Nf1hlXVrWUEMmzRhX00xzrvWD12hqtNAu3sVGztm4mvEGKAygK8QqS2OufOqqbF3EZV0Pdz8MtL81nNPPyci6xCeecWk6HuzFG9c4HXN1VXyhoXlaW0h3vqrmDpZizL5hNdBeGTZZdKIiY3Yvum8K1vNwurzIYWhZl2zTWY9iyD9oelOHuB7XwPqr_TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیکرها با استناد به منابع معتبر سیزن آخر ایران رو اسپویل و یه فیلم از شبیه سازی انفجار یه بمب اتم تو شهر وسط اخبار صدا سیما پخش کردن.
🙏
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/funhiphop/77417" target="_blank">📅 04:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77416">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اهواز رو هم زدن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/funhiphop/77416" target="_blank">📅 04:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77415">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اهواز رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/funhiphop/77415" target="_blank">📅 03:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77414">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صدای انفجار تو برازجان گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/funhiphop/77414" target="_blank">📅 03:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77413">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش‌های اولیه از پرتاب موشک‌های کروز ضد کشتی ایرانی از بندرعباس به سمت ناوهای آمریکا.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/funhiphop/77413" target="_blank">📅 03:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77412">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شین: سه موشک شلیک شده  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/funhiphop/77412" target="_blank">📅 03:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77411">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
آتش پرقدرت پدافند مقتدر و یک پارچه‌ی نیروهای مسلح، یک فروند پهپاد متجاوز و متخاصم دشمنان جنیاتکار را بر فراز آسمان امن جم در استان بوشهر ساقط کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/funhiphop/77411" target="_blank">📅 03:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77410">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صدای انفجار تو زاهدان گزارش شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/funhiphop/77410" target="_blank">📅 03:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77409">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ایران بالستیک شلیک کرد   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/77409" target="_blank">📅 03:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77408">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ایران بالستیک شلیک کرد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/funhiphop/77408" target="_blank">📅 03:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77407">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بندرعباسو دارن بد میزنن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/funhiphop/77407" target="_blank">📅 03:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77406">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جم تو استان بوشهر رو زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/funhiphop/77406" target="_blank">📅 03:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77405">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک مقام ارشد آمریکایی به کانال ۱۲ اسرائیل گفت که موج سوم حملات به ایران اکنون در حال وقوع است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/funhiphop/77405" target="_blank">📅 03:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77404">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بندرعباسو دارن بد میزنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/77404" target="_blank">📅 03:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77402">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">صدا سیما:
حملات امشب آمریکا تو سیریک به دوتا مخزن آب بوده.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/77402" target="_blank">📅 02:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77401">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tY6_XUH9x_gDqJWw9tcOhT9JFTgyTseh1d_cIoEH6I-C2_X0qOjcAm5o8DeEn7hWfM7VcRkntiOewC22V2HcgDCIageiqzfGU_SwfetLOtj0Yz6ecf6qFlhS76ZLR_DXaFiNatwM7gcLipuMVFQuYj0G7MtNeeSemnHn0yBA6ogKf2qEA_EunPq7mla7kNFvChBuFatsQtm_FksioWTfWdCrKOWFAWtMANYabQ4qWnXkmqzfNiMjeqMisF8-hdf75XuhNmHKeAo6b41kz-09KUpdysEH790rJH3xxaIANQszkBzfqn6kFvb7Q5Edwv5AmMpaRco707M5OgD_yoVJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور عراقچی می‌گه جواب می‌دیم و تنها راه در امان موندن سربازای آمریکایی اینه که از خاورمیانه فرار کنن:
با وجود شکست‌های آمریکا در میدان نبرد، آمریکا تصمیم گرفت عزم ما را آزمایش کند.
نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نخواهند گذاشت.
اگر می‌خواهید در امان باشید، منطقه ما را ترک کنید.
تاریخ خلیج فارس فصل‌های زیادی درباره سرنوشت‌های تلخ متجاوزان خارجی دارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77401" target="_blank">📅 02:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77400">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رئیس مجلس نمایندگان آمریکا درباره ایران:
یک حمله دفاعی انجام شده است — این حمله متناسب و محدود است.
این حملات هدفمند به سایت‌های رادار، موشک و فرماندهی و کنترل بود — ماهیت آن دفاعی است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/77400" target="_blank">📅 02:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77399">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسرائیل هیوم:
ارزیابی مقامات اسرائیلی این است که حملات آمریکا آنقدر حجم زیادی نداشته که سپاه برای تلافی به اسرائیل حمله کند.
احتمالا حملات تلافی جویانه ایران محدود به کشورهای عربی خواهد بود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/77399" target="_blank">📅 02:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77398">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یک مقام ارشد کاخ سفید به پولیتیکو:
ترامپ همچنان معتقد است توافق صلح با ایران نزدیک است، حتی در حالی که ایالات متحده امشب حملات تلافی‌جویانه‌ای علیه ایران انجام داد.
این مقام گفت: «هیچ چیز وضعیت کنونی توافق را تغییر نمی‌دهد.»
این مقام تأکید کرد که توافق با تهران «هنوز نزدیک است.»
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77398" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77396">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ای مو موردوم سپاه هم داره کردا رو میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/funhiphop/77396" target="_blank">📅 01:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77395">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">روسیه 6 تا اسکندر زد اوکراین
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77395" target="_blank">📅 01:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77394">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عربستان ----» یمن
پاکستان -----» افغانستان
ترکیه ------» کردستان عراق
آمریکا -----» ایران
اسرائیل -----» لبنان
یک شب عادی در خاورمیانه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77394" target="_blank">📅 01:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77391">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هیچگونه انفجار یا حمله‌ی جدیدی در بحرین یا هرمزگان یا لبنان گزارش نشده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77391" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77390">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">CNN:
یک مقام آمریکایی گفت که حملات اخیر به عنوان یک هشدار به ایران در نظر گرفته شده‌اند و انتظار نمی‌رود که تلاش‌ها برای مذاکره به منظور پایان دادن به درگیری را مختل کنند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77390" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77389">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجار هرمزگان
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77389" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77388">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صدای انفجار در بحرین
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77388" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77387">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مقام آمریکایی به فاکس:
حملات هوایی علیه ایران «در حال انجام است» و اهداف شامل سامانه‌های پدافند هوایی و تأسیسات راداریه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77387" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77386">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سپاه: بزودی تاسیسات نظامی بیکینی باتم را مورد حمله قرار خواهیم داد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77386" target="_blank">📅 01:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77385">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این تو بمیری دقیقا از همون تو بمیریاس
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/77385" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77384">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سپاه: بزودی تاسیسات نظامی بیکینی باتم را مورد حمله قرار خواهیم داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77384" target="_blank">📅 01:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77383">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پاکستان هم افغانستانو زد
🤣
🤣
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77383" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77382">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جنگنده ها از فرودگاه مهراباد برخواستند
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77382" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77381">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سد مجید :
و ما النصر الا من عند الله العزیز الحکیم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/funhiphop/77381" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77380">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS1Jz4w7vc5w7MRC_xF7I7UfztseJFjUvEuhonlTybSQNwcHuBEDpmWzJwwWMXQgB1qj2m2IpzM0iKku4MeTuTrrj_SBsWxHJCFSoJBqsPYUlOulrcGmR0KMCjaA6vbmPUytUfqwyeUwMbLPpg3Lwf9yWOdVpV7SN5L1sibGc0-EK4Ogw0osu7qpQ0sLWK_M8vFcDJezIUMbIHgwlm2Py8vhbKOnJn3F6CjjHuUNY6M2N-u2uDRBeE6pQhrLSu66vH8BCv-cRtx2s6p2HbxWO2UD1pFujZ8Gtk-iHT0Ygbc9oME2OSIZ4HtikQ9km4mFZyJ6ZzzIsEjM8S59Fx2KBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمون ایران سوریه و لبنان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77380" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77379">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تو این هیروویری اسرائیل بیروت رو زد که ایران به جفتشون پاسخ بده تا شاید آتش بس نقض شه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/77379" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77378">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قطر و کویت حریم هوایی خودشون رو بستن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/77378" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77377">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">لبنان رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/77377" target="_blank">📅 01:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77376">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هگست الان زیر بغلش تموم شده داره بارفیکس خلبانی میزنه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77376" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77374">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حوثی ها: مالک گپ مگام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77374" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77373">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تسنیم:
ایران همچنان که ساعاتی پیش نیز هشدار داده، پاسخ قطعی به تجاوز آمریکا که به بهانه سقوط هلیکوپتر آپاچی انجام می‌شود، خواهد داد.
@FuunHipHop
| Nima﻿</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77373" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77372">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صدا و سیما:
پاسخ های ما تا دقایقی دیگر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77372" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77371">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فوری از علیرضا تنگسیری، فرمانده نیروی دریایی سپاه:
سریعا به تجاوز آمریکا پاسخ خواهیم داد!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77371" target="_blank">📅 01:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77370">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ به آ‌ب‌ث نیوز:
فکر می‌کنم پاسخ دادن بسیار مهم است. آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم.
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، و من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد، و این همان چیزی است که این پاسخ نمایانگر آن است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77370" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77369">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجار تو میناب گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77369" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77368">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هم اکنون جلسه اضطراری شورای دفاع به ریاست علی شمخانی در حال برگزاری است
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77368" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77367">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ارتش امریکا از شلیک چندین موشک کروز به سمت ایران گزارش داد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77367" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77366">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الان ترامپ زنگ میزنه به خودش میگه حمله رو متوقف کن چون توافق نزدیکه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77366" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77365">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سنتکام اعلام کرد که حملاتی را در قالب دفاع از خود علیه ایران آغاز کرده است؛ این اقدام در پاسخ به سرنگونی یک بالگرد آپاچی آمریکایی در روز گذشته صورت گرفت. این مأموریت، پاسخی متناسب به تجاوزات غیرموجه ایران است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77365" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77364">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">درود بر فرید جان عزیز بندر عباس یه صداهایی میاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77364" target="_blank">📅 00:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77363">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری دولتی مهر:
شنیده شدن صدای انفجار در منطقه سیریک، استان هرمزگان. ساکنان محلی از وقوع چندین انفجار خبر می‌دهند. مقامات رژیم اسلامی هنوز درباره علت آن اظهار نظری نکرده‌اند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77363" target="_blank">📅 00:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77362">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دیس جدید شایع به اسم عصبانی 2 ریلیز شد    Youtube  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77362" target="_blank">📅 00:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77361">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیس جدید شایع به اسم عصبانی 2 ریلیز شد    Youtube  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77361" target="_blank">📅 00:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77360">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOicH8_vYWARlrp6e00yivJSqg5VhZbS6DliebMOHeE35wP_nSp3X1JX_7bui7Fkx7oLH8fbXrqwvXjJgE1-NJ-FbuypElWLKKhvt4rYUBKDvCAffULtza3E2MazZJ1xfxLiV-3uvrBGhy_nguyz1aQdaDlU4hIQ_NqBGm-tQaC91cSJ_7aXVJKhzqgZve2nI5Hf-Bc--32aBczSaFqZ5oD5IVaqtOu2GOkyEiS8bOalu4oTxF-IzpMp-e38QVx-7PqdrTa8I-1zXjB1XKqe89JO4bd8jHjw-7IT7vynLVcu41uGsZo0HsFMxRHE4KbAMl4zBuWUx6WIfWqvVeRscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس جدید شایع به اسم
عصبانی 2
ریلیز شد
Youtube
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77360" target="_blank">📅 00:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77359">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYbta-nZH8euYoeer61rpiydSUiRuhACJ1j9rEmGMCqm9P7iGkNBNy0AEBb0f4Ji4WpfNynQNjCVJ-TohjXHGpWgv5Eh-5M8w5yZUIOHedl9TSWOMI98xI1aonRVU0IDkdgZ0QkqpFoJpnnWCERbr1XXmOnbsTH3-w6vfNr5Gmm65qtcbP4G4j2Pqe87wJpnDGnrDt43KbzBWMo41pgHTnrvLA8Bi6C4JWwFXHWjVBPCLBb3pBqXexnB67T9VHUWb4U1szd16mIpX52r1XXThbKsftgLA2RcBOJivJaTcb7uB4wJGm0348FlK2ueAH4fkf1BAfP6Af6oohs4THxueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاشیدم به در و دیوار
معاون دکتر عراقچی در مصاحبه با الجزیره:  ایران پشت حمله به بالگرد آمریکایی آپاچی در بالای تنگه هرمز نیست.  این احتمال وجود دارد که چنین حوادثی به دلیل فضای پرتنش در تنگه هرمز به صورت غیرعمد رخ دهند.  هیچ هدفگیری عمدی از سوی ایران علیه…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77359" target="_blank">📅 00:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77357">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtYINo5wVZoCUdHWk2u4IHhLqOlf07nDQSLxwkN-k5s7zdpnpc8mEZXoe95m4lg1R-5GRAk3DTsxHbtGCi-gE0k7wsKiecsBkRcjUottGN0pdR_eZwKahIOARaswSipZs4cwM5tadxDR5xUlcWKx9TDXvTDRY7u82k-DPwKf4Ou2ascpLWsOAcHIsZjybuzNUoLjgBZJHq5BlltIJZnWl8ucLfjRT6ezkzCGAWs0h7-yX0wQUvNaLUOQuP0dOG0GCKoJmUq0QGaRl4ZmRS0ZMqsLM1CXmUl1D1dgZ0aBqC8o38T6rNY6UnsytrSOwN9oav_R5Q6AQ8yl3_EkSOkIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ورزش:
به قلعه نویی دستور دادیم اگه وسط بازیای جام جهانی کسی پرچم های غیر رسمی (مثل شیر و خورشید) رو بیاره یا شعاری داده بشه سریع بازی رو متوقف کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77357" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77356">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ به وال استریت ژورنال:
حادثه هلیکوپتر آپاچی موضوع بزرگی نیست و خلبان حالش خوب است و مادر بنده هم جند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77356" target="_blank">📅 23:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77355">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پاشیدم به در و دیوار
معاون دکتر عراقچی در مصاحبه با الجزیره:
ایران پشت حمله به بالگرد آمریکایی آپاچی در بالای تنگه هرمز نیست.
این احتمال وجود دارد که چنین حوادثی به دلیل فضای پرتنش در تنگه هرمز به صورت غیرعمد رخ دهند.
هیچ هدفگیری عمدی از سوی ایران علیه بالگرد آمریکایی در بالای تنگه هرمز صورت نگرفته است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77355" target="_blank">📅 23:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77354">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy8ncIVO5NLnZKdckwjYqqh_s5VvTyIcWU_da12qNWaGDiZITTajxM2ha9_kfMbl62M50qmYjdVUpdydj7G2LZl-YN-qgCxFEhngVA_F_tCTMOFexRMi4gp4xXO1ak2kMY3nNX8zeEJ5LhsVSHa6tW_S6HWbWWZklk545ViqDROYFHgNM_TEEh7w-rGTzH2crFIhceAeTO-qjIjQc5S8nAxspRM--Qcs2Z49LfgOR20wF6lCo0ATxSlslShUPfH8yKvXVWLDhuMjMkKWigWeuDLqy3cATHnz9Onw-msgpcjlSb4jj92xx9GQVtiiHYH1cMZ6YW2l_tsQSsXLt4FxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77354" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77353">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hzd4KxwtGvceX9eB9ZkBdB4HnUsrhRUampGO7W5xm8DA8Ah-RZfuVb86ClmoG0RNItIvXHJ9Kma3kHlH78EnxwsApjW5mk_YbCbhQLl3BgG5XEGuhSbsBNy0xomtB1uDGEOIYwny_NmKvoOWX1I2mvOL4vfqyeA8VB9zV2mwgBFJ5efZN7ARu3zKYp2J0mY3G3CarjtYcMLFHdYEy28VCuqn3Ysss-4WmVa0c1jeTTDA3rbOYU5O3Wi5PMj5llNKDT-Hqyg9Fs2pm0CgrvS5JhVvoPVKDr1qPT1qYgqXE2eHPq3IKGvJCWqVisudZryvj9A8IE06QpfWUwmOwutlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلایه ی پزشکیان در توییتر از نحوه ی مدیریت جمهوری اسلامی و سلطه ی سپاه بر کشور.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77353" target="_blank">📅 23:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77352">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubgph6WVZ8v2Vg56DhXpRIy4nAfZETo5nvjdL_YFmlaZFBcFeqJnONaEg6LbfRPQZ7RdJyDc4yJ7FlHoYGSQppPJluiEqHiYcVdzUQtFBHlE77ldwZui2QK707eDwKl_tA3ZyywewXY0tlYBZ4oxlCq02iZ9SYfeK4Wo8LZ3QhgbT4K48zR02fXXkBT-95qtD3BA9ygR49pfgPLl1uU7ssrauNd6R_meQdKM9Kjwm0Prpt4TjF1DKxSHEHvUWnp2WJEtytJTm0hc4Ik0vW1CghyHTY1wMzIInXSCrLgtXyEEZApx60-Hu9Ki2-VO72qzxesfWEOClv0fXgYhY7lBpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلایه ی پزشکیان در توییتر از نحوه ی مدیریت جمهوری اسلامی و سلطه ی سپاه بر کشور.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77352" target="_blank">📅 23:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77351">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">داش بمولا این سری، این سری دیگه میزنن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77351" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77349">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خب امریکا میخواد بزنه ولی ازونجایی که ترامپ دالگخیزه تبادل اتشی بیش نیس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77349" target="_blank">📅 22:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77348">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnK5lhJXQ9yaFdNx-H1jHLxL3gq2OudqOWeuGmhSuP48RZMj1TrsLcFnA-tHUKmK437HEZa1HF43IwpLNkt4N_QKkHIt0RKKbZztmjGjHSd0y-ZZ1_AqmBNHxzFeXGydQ-gjD4maZTPAgq9YIIKpK5rymgZZcpBHB4fCvP42emShhbxWT-YN1uaZNJjuQJ6bu61atDmoKIqzpzY_TfuHd5SFUo4-oW15-dWkF76qXNt8sJQJ6CLOrGN21IM8YKbtheD004f2ZwjqlUM4HKunA9oxz99-clMYuZvIXEVpaUc_H77uoG72rRdlHmqkcTB55UGgZeA_yRnFi7CYklGlxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77348" target="_blank">📅 22:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77347">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپارس شو</strong></div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77347" target="_blank">📅 22:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77346">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfH2R03rPDgGFP0EX7dtY9j42gxgPMSR0-8udLqR1g_1gl35jngGZgx-zJqqLzUZsWAIERzJ-gD79Sa_y4C4a3o4TgxAOkoY322RXMQajxpOnxVoRJ8lJPVBrLaAhXTjn1z8LzKEwCNr1RecbZL7sV5w2szSwXnnugQ8lZEOChjgHbMMomJb3QJBisgq_jelormHMnpvJgOTYKVAWXNUH-kopZf3c4fnAlrpn5O47SDQyhu9NVRoH7Wy57XuIYaaIj0nUnAqSqSe8sQSqZCzv0ZdS-RqC5s9x6S6FLUYAcUCSPJpBhRyzC8U4QZ_01g4PDxlMTzsTeFzWHkk5AVHPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرت مذاکره:
نیروهای خارجی در نزدیکی قلمرو ما به دلیل اشتباهات انسانی خود، حوادث ساده یا احتمال گرفتار شدن در آتش متقابل، همواره در معرض خطر هستند.
برای کاهش خطر، بهترین راه حل این است که آنها منطقه را ترک کنند.
ما زبان دیپلماسی را ترجیح می‌دهیم اما به زبان‌های دیگر نیز صحبت می‌کنیم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77346" target="_blank">📅 22:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77345">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ به ABC : اگه یه عده بخوان احمقانه رفتار کنن
ممکنه کار به جایی بکشه که مجبور بشیم کل زیرساخت‌های یه کشور رو نابود کنیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77345" target="_blank">📅 22:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77344">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوسی خبرنگار فاکس نیوز: «او در دفتر بیضی شکل بود و از او پرسیده شد که آیا خط قرمزی برای از سرگیری یک جنگ داغ علیه ایران، کشته شدن نیروهای آمریکایی خواهد بود یا خیر. و او گفت که این دلیل خوبی برای از سرگیری عملیات نظامی خواهد بود.»
«در اینجا هیچ نیروی آمریکایی کشته نشد، اما به نظر می‌رسد ایران واقعاً، واقعاً تلاش می‌کرد نیروهای آمریکایی را بکشد چون یک هلیکوپتر آپاچی را سرنگون کردند.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77344" target="_blank">📅 21:40 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
