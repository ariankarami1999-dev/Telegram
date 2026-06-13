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
<img src="https://cdn4.telesco.pe/file/f_qNT3E3MIMIrLfMkDfQau8nTg45wvoAADe5ExpfLPCAs0QKHSu82xi_FemrUJIg35TR07mwYNB7DFgOlplcNB_UP0xOK2TBUqb0EukKp7mXIX_cxU_O71eFwY095VJXJb3vccU0hQkifq-x_yBRio3cn3sb_vG6aVsne93nBTVsmP3u50_PTDw-IGvbY-EruJvgoVt89b6_fxvMO2trSNGR8EHd-ImynaqxoxlTBdRntjn3LRFV0ZRUgmtz4GLBq03u1w7Yg7OcbPvDaHVHZTqJXouPFe740HsZsttZ0CrFs0ZcAwV2NYpyFTQFyrXSyxaZPJqQI3rnmoGaPn0m2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-127637">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9278a44709.mp4?token=EFB4fbsVr8tTjrnBIeCqbbD3X6a93u0ZPxjz2qWE49xpk6vvm20DkBumuasU_YIWwsBvalPzb5A6HdJylr7wkSXA8L6c7sbW_urSyAg4hQuqrXe2-tGOftMyMTkr1oWl56WB-aJkDPy8G4RUSsDVBlYiQ3NfEd2zj7Nw5iDgi5_yp_Eu_I3G441fyhGL7PpAGcosDyqODflGWY9SBB6leqJc-lswpOs1GG7ZKir_lkCeCHGlEgNEvPF4ozpHGkgdysGtXAnrUXUKRAHKRG-Q_BR_hFjHlDr9LoPG7dMYEYJopqUaDL0_gdk2_-223k39zLp8Mi-NXeEi3OabC8vItg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9278a44709.mp4?token=EFB4fbsVr8tTjrnBIeCqbbD3X6a93u0ZPxjz2qWE49xpk6vvm20DkBumuasU_YIWwsBvalPzb5A6HdJylr7wkSXA8L6c7sbW_urSyAg4hQuqrXe2-tGOftMyMTkr1oWl56WB-aJkDPy8G4RUSsDVBlYiQ3NfEd2zj7Nw5iDgi5_yp_Eu_I3G441fyhGL7PpAGcosDyqODflGWY9SBB6leqJc-lswpOs1GG7ZKir_lkCeCHGlEgNEvPF4ozpHGkgdysGtXAnrUXUKRAHKRG-Q_BR_hFjHlDr9LoPG7dMYEYJopqUaDL0_gdk2_-223k39zLp8Mi-NXeEi3OabC8vItg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی: اسرائیل و موساد یه برنامه دقیق برای سرنگونی جمهوری اسلامی کشیده بودن که لحظه آخر
ترامپ
و اردوغان جلوشون رو گرفتن!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/127637" target="_blank">📅 17:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127636">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
آکسیوس:
فردا توافق بین ایران و آمریکا امضا میشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/127636" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127635">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌
👈
عراقچی فردا راهی پاکستان می‌شود
الحدث به نقل از منابع آگاه:
🔴
منابع حاکی از آن است که یک هیئت ایرانی، شامل وزیر امور خارجه، فردا وارد پاکستان خواهد شد.
🔴
هیئت ایرانی بر مذاکرات فنی مربوط به این توافق نظارت خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/127635" target="_blank">📅 17:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127634">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8NhgjFdcRZffVrmcbCA_tcS0gnh9yHhs9fm0pAE1xCcoD5oYK1-KfnzB0ga863PkRdahIW8runtSBzsaDUoirMSz7T2xdUjcourUsDn7kZ6E56kFltWN2Gv2P3zr0M9c00HgoVALSWbBw-mHg20UgLKAd1Ia1qCgl0_f53CxEAQG05twtN4zUL4W_aWj3o2jjjRHdn3VjyQGwo1jnyyHRzFp8d15O6_x4XjqP0EcNe6uqwTGurA9PnKoSj8LCQXhuFJPtC-kmSq7GVejm3AZwgbU5WMRuFhkuTcQRJYkJMLnOZBpnob39oFxdAgZRbzpqNxcYCvS0Pdn9hS0NxgZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایرانسل همچنان اینترنت ۴۰ هزار تومانی می‌فروشد!
🔴
با وجود انتقادها به اینترنت پرو و گرانی چند برابری آن، ایرانسل همچنان بسته یک‌ساله اینترنت پرو را به قیمت ۸ میلیون تومان عرضه می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/127634" target="_blank">📅 17:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127633">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
امشب تو دروازه شمیران برنامه‌ها هست......
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/127633" target="_blank">📅 17:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127632">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BR6j2KBnaJWuHAMIPavUZAj5SC0dXPMqDdD8W6Y3NPr4jMxFQf95CwmH9k_obwZZRA2_WH5Rq1Px9i2lHGvAwr_iB5Pm-4i1M6fbRoa6Uw-2m1IZxGNRPYklRb-YZkjOtU7q9oWoW5YzH6DCMjart2fdB6SAE-Kc5QqShNOI8ZVa3xq5TxnLbaw2G-nNxmA1DjOVJ7q3zbl62jgHp71roXGF2clMOldKWwZvsQEdMHxmbvh1AfkSkLWUQ86eBh5oF4aO8k8lX--3Qd2KRaaCtkUxvx0K2AqTpMTupcPPMFHByaphph6SkS7mVTfB6PVvk8Z90sNji6fnL9PZinMTtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ توییت نخست‌وزیر پاکستان درمورد امضای دیجیتال یادداشت تفاهم ایران و آمریکا تا ۲۴ ساعت آینده را بازنشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/127632" target="_blank">📅 17:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127631">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
واقعا خرن؟ یا خودشون به خریت زدن؟
🔴
اگر توافقی بشه همه میدونن تصمیم کلیت نظام جمهوری اسلامی هست اما عده‌ای دارن میگن وای ببینید عراقچی رفت مذاکره و همه کاره اینه! واقعا خر هستید که فک میکنید دولت صفر تا صد توافق رو رفته؟ سیبل رو اشتباه گرفتی برادر من
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/127631" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127630">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
آرزوی یک تندرو: ایشالا عراقچی بمیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/127630" target="_blank">📅 17:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127629">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
قطر بسته‌ای به ارزش ۱۲ میلیارد دلار را در مورد دارایی‌های مسدود شده ایران در جریان مذاکرات پیشنهاد داد که شامل آزادسازی ۶ میلیارد دلار از وجوه ایرانی نگهداری شده در قطر و یک خط اعتباری اضافی ۶ میلیارد دلاری است، طبق گزارش خبرگزاری مهر.
ایران در ابتدا پیشنهاد دریافت نیمی از دارایی‌های مسدود شده خود را در مراحل اولیه مذاکرات و مابقی را پس از توافق نهایی ارائه داد، اما ایالات متحده آن طرح را رد کرد. سپس قطر بسته جایگزین را برای کمک به شکستن بن‌بست ارائه داد.
۶ میلیارد دلار از دارایی‌های ایرانی نگهداری شده در قطر همچنان مشروط به محدودیت‌های استفاده بشردوستانه خواهد بود.
۶ میلیارد دلار اضافی به عنوان وام یا خط اعتباری مدیریت شده توسط قطر ارائه خواهد شد و ایران تعیین می‌کند که چگونه از آن استفاده شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/127629" target="_blank">📅 17:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127628">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fb367f9b.mp4?token=Q5YGg6GYRMU_pS3ZTeYAiG4VGN4_SA5_ohIFLAKV5qOZ3_fYmKSzpmI1J8S1plDdBw1JW2klGf45WGvbxh03YETCXKjDAGLomwfTaknTyLeHBMY4i4zN3CZvr2wyR7T0D5VMqfCQpntaxXrcMy7lkEfa4XKpvRkuBpDtZv3ihB0A9nsxQORkCOX8bnzdDqzLjF8F967V-9fmFwLPlgecCOMTzt7sfBqAdcK-d7wSKP_qMYMWbQSbytEwKjc2OTCeOyxbzmx_iaJrighPm9qsvFam3EcG92MvDxVD2uhigiXNDvpsSdAzuR3w59t3v4mZumHFSj8m2h2V0pTC9kG_VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fb367f9b.mp4?token=Q5YGg6GYRMU_pS3ZTeYAiG4VGN4_SA5_ohIFLAKV5qOZ3_fYmKSzpmI1J8S1plDdBw1JW2klGf45WGvbxh03YETCXKjDAGLomwfTaknTyLeHBMY4i4zN3CZvr2wyR7T0D5VMqfCQpntaxXrcMy7lkEfa4XKpvRkuBpDtZv3ihB0A9nsxQORkCOX8bnzdDqzLjF8F967V-9fmFwLPlgecCOMTzt7sfBqAdcK-d7wSKP_qMYMWbQSbytEwKjc2OTCeOyxbzmx_iaJrighPm9qsvFam3EcG92MvDxVD2uhigiXNDvpsSdAzuR3w59t3v4mZumHFSj8m2h2V0pTC9kG_VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قابل توجه جبهه پایداری
🙂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/127628" target="_blank">📅 17:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127627">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMdyRUrY5FE0mlMPDVZhLr_TsiRZa8Z4PPtid-BnF-wfPurizsl9NdUqa1Mvzzcm--bMZuc1GEElj7Ox5MZqTtrLu8vCD9aBdNSFlSpfkAbndgO_dpbNkPdByj-di364mPPi3oQcaJvx-z9ytUv8uCEAwOQKByTt9c-I1Bptb2Ta_-MS-fnyOtzL19qT8kOPIjQDim0J_wqfH3haNKSBnCaEwXTj4C0RFOwkE35rH7M7UtqKW07LxamPvurNek_Xx8jXh_Q_16Hc8R2k4DIy9NWmyVxqx_6TjtQnRwtlYaHU0cKUf4WdvEuAZE0nO1oQ2JtnIhjCjQd_Q-RKacNs5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تجمع برخی از مردم تبریز در اعتراض به توافق با قاتل رهبر سابق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/127627" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127626">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3eee2c609.mp4?token=Zc25HXMSgYTLv_KElGaIDtK0nZEPCW7a_JNXH4-hmbsnm2L7BNafbyyoYs3i9nHxIsRKkyS2aPGK1TnpnRh1Y5rXAQ3ADg8hOjSoTJR-DLkk-RjY5h8iYfkJqstibcJxMw0YESY2APKEQvsH6YUW1EiaWrNBJ-aZKvm9fnE8ibFcQ5c3Cwcvkkd553DQBhF179lfpi2aXjI-ksfFO5Vs3WDRJ5yP4Ruh6n0i1KDz4UrOfwkDxumni3vfhgeDddNQeIXlhGIMNMpYJ8FndRpxXaudLLNka3T9pyKmifBHcB7-1mJfjRWRR3W3dvPpjiRFCYE9grotO2dGW5V67DqI_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3eee2c609.mp4?token=Zc25HXMSgYTLv_KElGaIDtK0nZEPCW7a_JNXH4-hmbsnm2L7BNafbyyoYs3i9nHxIsRKkyS2aPGK1TnpnRh1Y5rXAQ3ADg8hOjSoTJR-DLkk-RjY5h8iYfkJqstibcJxMw0YESY2APKEQvsH6YUW1EiaWrNBJ-aZKvm9fnE8ibFcQ5c3Cwcvkkd553DQBhF179lfpi2aXjI-ksfFO5Vs3WDRJ5yP4Ruh6n0i1KDz4UrOfwkDxumni3vfhgeDddNQeIXlhGIMNMpYJ8FndRpxXaudLLNka3T9pyKmifBHcB7-1mJfjRWRR3W3dvPpjiRFCYE9grotO2dGW5V67DqI_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون اول ترامپ؛ ونس :
اگه برگردیم به جنگ جهانی دوم یا هر جنگ بزرگ دیگه‌ای توی تاریخ، آخرش همه‌شون با مذاکره و توافق تموم شدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/127626" target="_blank">📅 17:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127625">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWOTRrJv-3KgUkPHpd6wGQm_L39oWoV6SG0o8HE6_Wt7PyiTeKtKbQlITSVGxptzsciVlEmKu-BRz4WQQXudQcmU0O7HSXVz6A6MRiPLQrx0xs4SNq7rOBxfOzo9Cy-_r04nQmc-VRnHUXRpcBYZ_odTV-tAelZliLqS5K7bTAY_a4GHYu3TbufDaCXL0gTchQdq9S7zm1838YwhmTnIZO2Kz3E8Ll6aqCk_lfgK1D2oAmBV4x0rH__j-gkv7dyYMnAHiz9UX3QkVG4CbEB_bBjkYnO3W61ceF9lw_ojTByYBN4IwzHm3ZkBqeI28iCDYtDj81n_K8Xv5DvSbP30Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇸🇳
علیرضا فغانی داور بازی فرانسه و سنگال شد
@AloSport</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/127625" target="_blank">📅 16:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127624">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33552400af.mp4?token=ugjhC7TgtbAQ5RzZ9aKhZubPRzEUOP9D1PGZwAt-As1eNfNdRb-HWkoRikyIKyOOu0YPP2EXzxoz6mRrUmfYGgrHz3hraKdwNiyGwUmZQcEgUqSkErnM8iZV0xNab3-fd2OPj5Ex_PcTbXxEMbocTkQC9cv2ZcZ95nrDefFM-X_ZcmGQQE2CTcsLqdXevXEY64ubHiYlyTw2r3PLEne6C01Vm0oEYE7trk0WJgM55nS5VIinEjthZereDvqgH58DK-ylC_NIgQL9prm-XVpelCFmclQ4qWuKWoNd629lancdYdMZOGuRzND3JKPxperSf0A7wYEka-q54hJBXS8U4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33552400af.mp4?token=ugjhC7TgtbAQ5RzZ9aKhZubPRzEUOP9D1PGZwAt-As1eNfNdRb-HWkoRikyIKyOOu0YPP2EXzxoz6mRrUmfYGgrHz3hraKdwNiyGwUmZQcEgUqSkErnM8iZV0xNab3-fd2OPj5Ex_PcTbXxEMbocTkQC9cv2ZcZ95nrDefFM-X_ZcmGQQE2CTcsLqdXevXEY64ubHiYlyTw2r3PLEne6C01Vm0oEYE7trk0WJgM55nS5VIinEjthZereDvqgH58DK-ylC_NIgQL9prm-XVpelCFmclQ4qWuKWoNd629lancdYdMZOGuRzND3JKPxperSf0A7wYEka-q54hJBXS8U4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی: اگر تهران را با بمب اتم بزنند؛ ایران به مدت ۱۰ سال تنگه هرمز و خلیج فارس را ناامن خواهد کرد
پ.ن:
😐
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/127624" target="_blank">📅 16:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127623">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
کانال های خبرگزاری معتبر فارس، بابک زنجانی، صرافی نوبیتکس، والکس، رمزینکس و بیت‌پین که تو یوتیوب فعالیت میکردن، به علت تحریمای آمریکا همگی مسدود شدن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/127623" target="_blank">📅 16:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127622">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
یه اسپویل کنم؟ جبهه منحوس پایداری بزودی دیلیت میشه. خبر دارم که میگم
😉
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/127622" target="_blank">📅 16:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127621">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THE9yh7Pixif5LKTSIazSGoqqKiwyu5B3JT-BBhXH74tBNsQXsJ4GCtg4YG-P-yQee24OOLTP4YmO5HrLKoJ6Le36y2GRTthbFOrqfoT2o9cv5zLLqgcMtcasPAZwzJBXSTUiqA3BAwH-pMLkaGEFmFPhULSZ3Uk1ILU6K9eussuxn-tnRb8fSMuw-ZtGZiVWuYhQ0jO9ZnRzVbOsO3NVvGQsXgv5Jc04j5NJDgHoYqkkmZhmHKLAl96cCXvT5AyRkpClosg7e4y64aIIxEW2cWqgorSkVR8c4FIP_x6eNnL-TIzesfUV5BCGVYlxVZDnzDQTPFR7mYUcMiqWkRXhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تمسخر لهجه مشهدی و حمله به قالیباف توسط مالک شریعتی نماینده پایداری مجلس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/127621" target="_blank">📅 16:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127620">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
بقایی: زمان امضای تفاهم‌نامه فردا نخواهد بود
🔴
تفاهم‌نامه اسلام‌آباد بر پایان جنگ متمرکز است و در این مرحله موضوع هسته‌ای در دستور کار مذاکرات قرار ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/127620" target="_blank">📅 16:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127619">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad147ae5c.mp4?token=s_JmXlPwivWOR4TKy8JrhB56TUcjmqKAPh4n4aRgfGy5LeKHx1YNdFLldxqx9CZXgPGD1JlN8LV6hU90UTk8J2tNDaxcVPsQNZV77Ye9LTyF_L-pDV2xMLyZbDqUxr-kxJarlp0I2yvBNvQxTFPj30pfs9ecmCmV7uKWC7aYOoAp-n6wSgX-WhgxRzcl68ZLbwZEf2SevQ3DFRdFYTb0q8SQLfVha4u_d6Q6EThqc8aU5YDmd3k62vK8iWmr8h5MyRjlRqEK_NKKXGJG5iqA7CGOoZvgDD_BaAhtIaKIC6i03H7w2DtYOAQSpHFk7u4qDzC_5b875ptGfTAyC4Weyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad147ae5c.mp4?token=s_JmXlPwivWOR4TKy8JrhB56TUcjmqKAPh4n4aRgfGy5LeKHx1YNdFLldxqx9CZXgPGD1JlN8LV6hU90UTk8J2tNDaxcVPsQNZV77Ye9LTyF_L-pDV2xMLyZbDqUxr-kxJarlp0I2yvBNvQxTFPj30pfs9ecmCmV7uKWC7aYOoAp-n6wSgX-WhgxRzcl68ZLbwZEf2SevQ3DFRdFYTb0q8SQLfVha4u_d6Q6EThqc8aU5YDmd3k62vK8iWmr8h5MyRjlRqEK_NKKXGJG5iqA7CGOoZvgDD_BaAhtIaKIC6i03H7w2DtYOAQSpHFk7u4qDzC_5b875ptGfTAyC4Weyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این صحبت‌های عراقچی به شدت وایرال شده
🔴
اصرار بر مقاومت و غنی سازی باعث جنگ شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127619" target="_blank">📅 16:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127618">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDkUEclxBwTQmWE81UrGZ2lQoGEtai-R6UZNmi2wdc2Lw6yfIbgnj9FSnquDTnaETzlClp61gO7Hfpd00l2MdYUNceLp93DfiVfydZOzlu1f4yapmLlX3LRPf9UoGTxfL3nYAXFDqi2hE5NzjI5rkWLcySKKgBC-A8Qeb0wyzd9eiyrsVPYORoAGqQ8yDhnuTPUFQO7F7UIu8LvIDGSmXIFdKqBOZo4ZphdZXTcyIpKQeX2yZG82SPUWCXuM4u9Wz4c_v3512lObQkxOZb83N5TZN2sQspbGIrhq-2tbIg6W0BIEa_eJM7yg7xmd87mGIIKW0AdjkT6AO_vmzANaaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/127618" target="_blank">📅 16:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127617">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بلومبرگ: ایران بخش‌های گسترده‌ای از زرادخانه موشکی خود را بازسازی کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127617" target="_blank">📅 16:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127616">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGB0vnM2St-GAmPfITfpIrAmc_0bGUCP7nOSJxr8cOoRSaggJTD3GOnKjvA9KNF4UWcNm7Fum2-3Rjq4Evt2AsEDWFugJRUthsxZQiHbyyXchQlWnRLgDYn4qR_D2yRNdV0IegU_hnCArm0d5Zm9Tm4vM30ym1lfoE-nTdVtabrysAPqfnlODe6ypJ2i6imTcveQh_FQjcEhoTRq106Cryp8XfAWEIWcsE8eDYnl03X7buMF7v7So92LMVDErX-iYKKeSL0jKdAGeQvAIThHTi7UwOB-qSorLQdsWBTbU2vQAnG3uqr90goDd7Fy2dVaopVTBgINIDn7T4eTNGYn9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با اینکه هنوز حدود ۲هفته تا شروع تابستون مونده،  قطعی‌های ۲ تا ۴ ساعته برق تو بعضی از استان‌های کشور شروع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127616" target="_blank">📅 15:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127615">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c36796d1a.mp4?token=lk-c4GNXr0bbDn67oqNFKJeaVl6XCrrX8kY4d1miN5ApqTBMUS76N7uQNCiX6WoT-gwrorlNmCDg-RYs5dUlZtYorEh05RPu8Iw4ORaS6k8oNQz4RMxqnJYmDgtbb7by6wVtMnYqTmkLuy8d32rXMoxpBbf73dfIfhTP5q1k8WjycGFpvq9a3NDZIjXL93JsYJyOudqvKTkTrwcwekKdsEJO8Qy6LtheqHNHE9e7cLaJPgxrZ1kUfh6OgwmlSSTqL30XZLE0HJTGZAdH2sbWPhkFWu3wlzJUlBx2M46TGOBpL65JXFtmubhZymZLDEzawQwMJ2HZce0cFtaQwIjXOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c36796d1a.mp4?token=lk-c4GNXr0bbDn67oqNFKJeaVl6XCrrX8kY4d1miN5ApqTBMUS76N7uQNCiX6WoT-gwrorlNmCDg-RYs5dUlZtYorEh05RPu8Iw4ORaS6k8oNQz4RMxqnJYmDgtbb7by6wVtMnYqTmkLuy8d32rXMoxpBbf73dfIfhTP5q1k8WjycGFpvq9a3NDZIjXL93JsYJyOudqvKTkTrwcwekKdsEJO8Qy6LtheqHNHE9e7cLaJPgxrZ1kUfh6OgwmlSSTqL30XZLE0HJTGZAdH2sbWPhkFWu3wlzJUlBx2M46TGOBpL65JXFtmubhZymZLDEzawQwMJ2HZce0cFtaQwIjXOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه هدف قرار گرفتن راکت انداز Tos-1A روسی توسط پرتابه FPV اوکراینی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/127615" target="_blank">📅 15:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127614">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k69Crgf-I90rFtThxFHUhCPYVGaT_D_JgKWJxwdf_XFWfA1gcI4-znuUBAMumJanVcxbHg92OHLZpyMoEuqCDyXwW5VJ0BVIXq49Qg05aQBYx1GSRQBkNmgdMINaGG5DQ-Sfpoq5pW37KYmNvUZnGATFDS8AlIopTZ0H4DxZarBvyoK22LCW3vGdbNirZDfTXwvitJnflghFmCSRcWO3SClTsQavr89q1mWfYNfkoVt5kP7YaxHyb-J7VdsM_BRZjEUNyqW-SslnAGPNBVyeq8kBRGogwuPdZYU6s1_ySxW017GWrgePu2etrUGtS3I-83oDb1Buwam0vHi63nuESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال دلار  هرات توسط تلگرام مسدود شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127614" target="_blank">📅 15:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127613">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4A5he4IX3nYqaNvvCmk9kNhwGK4H_3G68E9eh_QRvTVRPmcC47SjMbzsHOqtVkduByU6u1FpnNZUhOMZZ9N-SGX1jTniKRkpJk_uhwNPCwvzmfJ5a6CSl3JkGpDy7frv-4yGkJrOizUdavq55a71XjM4lzYagJ3UgJCXFR3wA27tUWJuvltm-srdiy0zVOcRYd2JfgNuicIznHwXiNZkMrxthosKjHMbUqRrITQ9GHZzfXOXh7Qtsi0rrnmF_dvTIgUb7zpD1srYbGGP5hfRnmlnEPiB1a6f2Who6yIyM3h0AVzqTBUU8pBCPqoas-G53lWPe_9JUH0GFX4urqx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رایزنی غریب آبادی با سفرای چین و روسیه درباره پیش نویس یادداشت تفاهم اسلام آباد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127613" target="_blank">📅 15:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127612">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تداوم تنش آبی در ۲۳ استان
🔴
مدیرعامل شرکت مهندسی آب و فاضلاب کشور : بررسی‌ها نشان می‌دهد ۲۳ استان کشور با تنش آبی مواجه‌اند و در برخی کلانشهرها از جمله تهران ضرورت مدیریت مصرف و استفاده از تجهیزات کاهنده بیش از گذشته احساس می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127612" target="_blank">📅 15:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127611">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
واشنگتن پست به نقل از یک مقام دولت ترامپ: تعیین میزان پولی که ایران می‌تواند به طور بالقوه دریافت کند دشوار است زیرا بستگی به آنچه آنها ارائه می‌دهند دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127611" target="_blank">📅 15:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127610">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsvPhFU2z2sHHNrb5EQ2VcY8hbKIXJ0-BG1ZgNhZcLItbM6uKOH8ALxwmI-ZPcxwhzVeM0_fpyGHcfE4SXZvGyQE4asFAbUSzAhI_O2i8VOM9GMK822IJyQ_dtinCOCAn1KHqDDxx38bmYkByNmRdgCMrondG2fpz5HfV5oLabZ6ysiZbIj3IscfUCP9d8_JK13lPwS2zrK7g2WE_GtfxdB48wEJa6rB0kwXJIE47-8xkq74iFdhswYMid6zwvtuqpYK7Ehq3uHVdVk4pDwCol1amoj3r_hdVz153am63kUmTqRNSWhnpMhYxNQ5cSxGzs136FK4iRTFYWu5c32Z7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهر انصار در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127610" target="_blank">📅 15:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127609">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
جزئیات مراسم وداع، تشییع و تدفین رهبر
🔴
شنبه و یکشنبه ۱۳ و ۱۴ تیر (۱۹ و ۲۰ محرم): مراسم وداع در مصلای امام خمینی(ره) تهران
🔴
دوشنبه ۱۵ تیر (۲۱ محرم): مراسم تشییع در تهران
🔴
سه‌شنبه ۱۶ تیر (۲۲ محرم): مراسم تشییع در شهر قم
🔴
پنجشنبه ۱۸ تیر مراسم تشییع در مشهد…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127609" target="_blank">📅 15:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127608">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نخست وزیر پاکستان:  ما اکنون به یک توافق صلح نزدیک‌تر از هر زمان دیگری هستیم.
🔴
با احتمال نهایی‌سازی در ۲۴ ساعت آینده، پاکستان در حال آماده‌سازی برای امضای الکترونیکی توافق صلح بلافاصله پس از آن است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127608" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127607">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سازمان UKMTO گزارشی از وقوع یک حادثه در فاصله ۶ مایل دریایی (6NM) در شرق عمان دریافت کرده است.
🔴
گزارش شده است که یک کشتی نفت‌کش در بخش جلو و سمت چپ بدنه (Port Bow) مورد اصابت پرتابه ناشناس قرار گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127607" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127606">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/ نخست‌وزیر پاکستان: متن نهایی توافقنامه صلح بین ایران و آمریکا به دست آمد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/127606" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127605">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
یوتیوب صفحهٔ خبرگزاری فارس رو به خاطر تحریم "مسدود" کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127605" target="_blank">📅 14:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127604">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری/ نخست‌وزیر پاکستان: متن نهایی توافقنامه صلح بین ایران و آمریکا به دست آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127604" target="_blank">📅 14:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127603">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14284d44cc.mp4?token=FNduyqOWb0PomEpBpFQ0mRZzDgy1LlhvzId8S-zODzW2LQb3Qjo7Cl6DVY1d_aAcw8e-3T4X__NbC7viQQnc_Ls-9AZ3wZjXkldEjaqlqClmcwSEmbv6Zp4dPM6R5WwtmHsbeYmJGSN9uPiO3iI5b32Gb-34VaBwUXPJRZe2a5WpcBz7PIGBNIFPwACjLKRvYa_8AeE1kUaUwoZcW0xwQ9GphKOYVHyJuyjcO7aAk1Em1Qr_pR4GR-hQr5Y9ynWa0_rtB0LZAWCQmoDaCvZbhL_wIm354IoMwLBX4drrvVafuhrIq-7ogaJ03JyAaQKo2RpbhcAFoqDwhOV28GjdWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14284d44cc.mp4?token=FNduyqOWb0PomEpBpFQ0mRZzDgy1LlhvzId8S-zODzW2LQb3Qjo7Cl6DVY1d_aAcw8e-3T4X__NbC7viQQnc_Ls-9AZ3wZjXkldEjaqlqClmcwSEmbv6Zp4dPM6R5WwtmHsbeYmJGSN9uPiO3iI5b32Gb-34VaBwUXPJRZe2a5WpcBz7PIGBNIFPwACjLKRvYa_8AeE1kUaUwoZcW0xwQ9GphKOYVHyJuyjcO7aAk1Em1Qr_pR4GR-hQr5Y9ynWa0_rtB0LZAWCQmoDaCvZbhL_wIm354IoMwLBX4drrvVafuhrIq-7ogaJ03JyAaQKo2RpbhcAFoqDwhOV28GjdWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر رفاه: همه موافق افزایش رقم کالابرگ هستند اما برای تامین منابع مالی به نتیجه نرسیده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127603" target="_blank">📅 14:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127602">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ارتش اسرائیل: هشدار تخلیه ۴ شهر در جنوب لبنان، ساکنان به سمت شمال رودخانه زهرانی می‌روند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127602" target="_blank">📅 14:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127601">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzU-om4oKhntuQlom7kVvR9VA_nvJxnyY_RW9M97DNjB_kfsFfzBrter4omLzevzHlzqTS4VXINLKGLCNytAoFCH5KI-z2lp5j1cj8aYLFkggug1ZrdXgXbVrIRGjLeWahFeP4NUWyKO6vhzyZTXvZs8T4gVon2NC94Mjs-xdm-WOZpuBsTzCOFxK51NlefPHJmw97oeAVHlvoIlVarMz7xxEeT_DG4WdMjeDoqyO2jAlETwIC0EifnDW3MpUIFhxmjpgVA5y3NJdypPOGJ7jpWzBRUmaxYLp0CkWIUK-vJE_rU8me6yFGX4-Z-Kaso6Z9o686e2ERgZWoZWSdxIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امام زمان (عج) فعال در شبکه های اجتماعی
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127601" target="_blank">📅 14:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127600">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
بلومبرگ به نقل از یک مقام آمریکایی:
در صورت تحقق شرایط، واشنگتن تحریم‌های ایران را کاهش داده و اجازه ادغام این کشور در اقتصاد جهانی را خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127600" target="_blank">📅 14:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127599">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
دفتر حفظ و نشر آثار رهبر: تا دقایقی دیگه تاریخ مراسم خداحافظی و تشییع رهبر  رو اعلام میکنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127599" target="_blank">📅 14:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127598">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دفتر حفظ و نشر آثار رهبر: تا دقایقی دیگه تاریخ مراسم خداحافظی و تشییع رهبر  رو اعلام میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127598" target="_blank">📅 13:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127597">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lsaVogyfSxD-F3Q2dPdfYmtLBFCV6yc0YHMR0MWBejPa-LN6eMJiQi2WZExxqY0PVHmPKTL2TmqfAg2RNo9t77QaNSVK4JDLRuYyz1p4eMFkVkXBLCvRarC2AHKPGTMDZdMjzZSVmvxFMi-GYLeM35dzv6WP73NQd9tCukNFBv6cmGZ1f1GEOOF2hOSmyH3mKSGvY0_BqcWGY7eiVse1ONiNwD8rgggkLVxyHQTAxfER-ICUjuqfXJvZsvsormIVtHwk9y9U7IdflEcd1SsUflqvimPz4sMR3fiRu6pCJz0eFU3fSw4MD_1v0MvpNGKDFoFuFlW6VhEPKIXpZ0JATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
16 تا نماینده مجلس به همراه قشر تندرو امشب جلوی وزارت خارجه تجمع اعتراضی برگزار میکنن و به روند مذاکرات اعتراض میکنن‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127597" target="_blank">📅 13:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127596">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZtNS5Qd7RzT3mt3ochLmaGmobRgCyk583vT8DfXGsknKlT4m0aiSGgsJ-eRCC6R35S6BbEeneu0zR7RObvbpBcPdwFA-_O_31bF50PCM-MNmoBcVXnyor2e51XlI5txPiDUfLohM_YThuEuG77t0Y0ArLA4h8uYHueTYgUH2UhXmByeR4n83Hg9QKke4_hTe2CXrkGbacWcp6YbzbYEuBKGBXXZ_HSG5gsk0GGTMWcsctj2HxoBguuEtJm9F88fBwETjcg4DXlRKNOptGHff9xqDIBRHG458m3M7ivo5SyCRiESvcuJG7jjb5wq_-FHVm6smOPgeAKmZu3f8k34xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله‌ به الرابیه در نبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127596" target="_blank">📅 13:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127595">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmRnor2zQVpdBkYw7fqnwMQEkbbACvFETb9QnbJ8OKHpr79YwBm7Nys7MbJn9Jv2Pnkggma-PUJ1xXQx-22Q2b6JMME7nuEPZNmDMfVFmCNOYbha3qAVI07PnRHo_mU3TgBLen7lQ46XzgKolwUlbQWIDpq2Ui9oqs1S1g1-9yVBI8eSMGqTdVU1MmWDRtuOIKlayx9TuiFsWwYaZeqdj5Tn7PK1lubVMaPiwqcM2Wzo9c4ZuLs_Ou9QTLVKM7UiEWc-1oYANclFh_M0wKNjf4tAMuy61oA1gBy20Tbh07s4oW32f7YDcDDns-1ghrex2E5zTB3RHr7kStaatEedhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش شده است که ارتش آمریکا شروع به ساخت یک پایگاه بزرگ در نزدیکی حصار پیرامونی غزه، نزدیک به پایگاه نظامی ریم در جنوب اسرائیل کرده است، طبق گزارش اسرائیل هیوم.
🔴
گفته می‌شود این تأسیسات به عنوان ستاد نظامی و غیرنظامی برای سازمان‌ها و پرسنل بین‌المللی فعال در منطقه در نظر گرفته شده است.
🔴
این پایگاه می‌تواند از اجرای طرح موسوم به «طرح ترامپ» حمایت کند، جایگزین ستاد چندملیتی که قبلاً در کیریات گات قرار داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127595" target="_blank">📅 13:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127594">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت آحارونوت:
میان برداشتی که ما از خودمان داریم و تصویری که از ما در خارج ترسیم می‌شود، شکاف بسیار بزرگی وجود دارد.
🔴
در خارج از کشور، اسرائیل به‌ عنوان قلدرِ محله دیده می‌شود و تهدیدی برای ثبات و صلح جهانی تلقی می‌گردد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127594" target="_blank">📅 13:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127593">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گفت‌وگو میان وزیران امور خارجه پاکستان و سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127593" target="_blank">📅 13:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127592">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4EOAejyXpoMCiKwFqXQKp-MMipmylSshcece9P_nFWisf6E-mGnjBewYCnfNaTOnxyL4RoYfnqYJZImO9v-P09PLFfCUc3Qhj76JdFNSZpSF36vAQIYXPBgcdFKAojFxjumEd-3iInbVpNQoFJ0tDw7ytMC5f5Xnq8vSrIwP86-Ht3zYb_lIMaqn6UhqJC8FqaRqXUeV_ENG4wCi-6LDsiPCUndNqjBFqaPBwaUnz--bvmBK_Hxy3O7rVEsWLygwytOe0SViFMwYk-w5swlejr9VGQI-AKyWcAcPjvfEFN7Byjd8JN-pOZLTloy4Zto6s4PWVb7YWwvdkqLgPKr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در نظر دارد از هواپیمای جدید ایرفورس وان که هدیه قطر است برای پرواز افتتاحیه در سفر برنامه‌ریزی شده‌اش به کوه راشمور در ۳ ژوئیه به مناسبت جشن‌های ۲۵۰ سالگی آمریکا استفاده کند، گزارش ان‌بی‌سی نیوز.
🔴
هنوز تصمیم نهایی گرفته نشده است، اما بازسازی این هواپیمای ۴۰۰ میلیون دلاری پس از چندین ماه تقریباً کامل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127592" target="_blank">📅 13:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127591">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / فارس: برخی منابع از احتمال وقوع حمله سایبری خبر داده‌اند، اما تاکنون هیچ مقام رسمی این موضوع را تأیید یا رد نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127591" target="_blank">📅 13:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127590">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سلیمی، عضو هیئت‌رئیسه مجلس :
هر توافقی که احتمالاً با آمریکا انجام بشه، باید اول به تأیید و تصویب مجلس برسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127590" target="_blank">📅 13:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127589">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/292cd09e0b.mp4?token=lNTLn1pbkC988auH2MDQwnwGmDEYYAsd9i_vFh6mQgVVIVg5Spi6cYsGHyC3_deYDUOw8mk6lMp6K-fWGHC0Ga1ttonn1kkZHzacFuJiVyr7Z_YVz8k9YPyaBvulyvBucUyi-LGAGHhYeAMGPGfKPloHkmV6bTxR0M2aS0zmMwWePVJfQpwn1GHm_xvCJ6Zr7Txuh6gdlgVh0y9x9QVoaAYicZRao26lY8sh0HRhel_YGLK86UUhJdaNA5yfXEdvnpH6-lcG2TRhOWsH-ZyRgryX_9DGCcT4tEgBLsp2TaKAf95CLtyWMH5UKZ3TpAgOKJYJ-L-BEf85j8ObcLFeeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/292cd09e0b.mp4?token=lNTLn1pbkC988auH2MDQwnwGmDEYYAsd9i_vFh6mQgVVIVg5Spi6cYsGHyC3_deYDUOw8mk6lMp6K-fWGHC0Ga1ttonn1kkZHzacFuJiVyr7Z_YVz8k9YPyaBvulyvBucUyi-LGAGHhYeAMGPGfKPloHkmV6bTxR0M2aS0zmMwWePVJfQpwn1GHm_xvCJ6Zr7Txuh6gdlgVh0y9x9QVoaAYicZRao26lY8sh0HRhel_YGLK86UUhJdaNA5yfXEdvnpH6-lcG2TRhOWsH-ZyRgryX_9DGCcT4tEgBLsp2TaKAf95CLtyWMH5UKZ3TpAgOKJYJ-L-BEf85j8ObcLFeeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عقب نشینی نفر‌بر‌‌های M-۱۱۳ ارتش لبنان از شهر نبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127589" target="_blank">📅 12:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127588">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نواف سلام، نخست وزیر لبنان، به رویترز گفت: حزب‌الله باید سریع‌تر از ما یا با همان سرعت عمل کند و حمایت خود را از مذاکرات ما در واشنگتن اعلام کند.
🔴
ما با حزب‌الله در تماس مداوم هستیم و تنها چیزی که از آنها خواسته می‌شود، عمل به تعهداتشان است.
🔴
مشکل ما با حزب‌الله، سلاح‌های آن است و ما این حزب را یک نیروی سیاسی لبنانی می‌دانیم.
🔴
ما تحت تأثیر روند مذاکرات در اسلام آباد هستیم و نتایج آن در سرزمین ما مشهود است، اما هیچ کس از طرف لبنان مذاکره نمی‌کند.
🔴
قرار است جنوب لبنان منطقه عاری از سلاح باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127588" target="_blank">📅 12:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127587">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر علوم: امیدوارم بتوانیم طرح سه ساله شدن دوره کارشناسی را به طور آزمایشی در چند دانشگاه اجرا کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127587" target="_blank">📅 12:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127586">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIH2_XtU16oredzNCDYTQ8qYZIoY1_egacK-M7mQIWOIvKJMKD3_y3crJcuISLL6KwREl0BycVVB_G_Iol8s69FNkPl4irlAxSXPKvrEGZ7itMmX-6oVCm_YKyVtqfkdl4KeHy23Od83_9ersBlitQEa0n8j-FEasmB-X-3X5tYkxb__mEPkPVWXj3pATvtYV4XbSGBF3LuSvvyjdjlAD2BnfQny_ZAlEOAfKq4heD2jHVZJlENpzljtZO-CLxPrGUFhtDy9ZpiFXd8WiwYamhF_Gwm-nlteQZhMLeGVZVCpcGKhocgnK1EMufGit4IFqgaFGCK1NKoHrfNAN4ua8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس با رشد ۱۰۳ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۶۹۶ هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127586" target="_blank">📅 12:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127585">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
از صبح امروز شنبه ۲۳ خردادماه، سیستم بانکی سه بانک ملی، صادرات و تجارت دچار اختلال و قطعی شده و تا زمان ارسال این خبر همچنان مشکل ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127585" target="_blank">📅 12:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127584">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ضرب الاجل جمهوریخواهان به ترامپ: تا ۱۶ شهریور جنگ با ایران پایان یابد
🔴
همزمان با نزدیک شدن به انتخابات میاندوره ای کنگره، بسیاری از جمهوریخواهان در گفت گو با نشریه پولیتیکو به ترامپ تا ۱۶ شهریور برای پایان یافتن جنگ آمریکا علیه ایران فرصت داده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127584" target="_blank">📅 12:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127583">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2lgTbr0saMYcY8fzK9-erNKLadbAws8qNmlL4vfij4UoaLuYZ9rNsh8EvyFng7aAN8bLujNGZk7OyvExUYvS-x85g_Oj0dFBk_1toe3qyjyP6S1Brs2O3uz2Jnr6kP-l5SPb_EbmvI8jctpF-2HDqvZYgDouYLMuZIRCcYK6Tti7Ugcpl8Aawii8kx1CdIIOrCnMaXHXV2IgW-HSX_ULXx7zTA8S5RZ2PBifKhPt3fs587WaBVj6qogx8mAYgInYXKWFTQnGMoy2ggkWCI2ZcIKD1EALR6ZO6PXR8_6s6O4Bn8HEZG9sI3NH7uwJIowiIwkpRnImqeBPF3JvrsY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی جنوب لبنان؛ ارتش اسرائیل پرچم این کشور رو روی تپه العویدات و کنار سازه «یا حسین» نصب کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127583" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127582">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
تماس تلفنی وزیر خارجه پاکستان با همتای مصری خود درباره تلاش‌های جاری برای پایان دادن به جنگ علیه ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127582" target="_blank">📅 12:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127578">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1c7db692.mp4?token=IR9fKTJZdZbEBC6rRiox_sGZKJBX7KB3dZCY9hXoW800miyGeleb7j3hVsDTXdB5OfGZXpp0OG1jtRJwAdlsrNWXwvTS9pu5vZyhHKFOjOP4H3_GpshbV5tWaVud5KUR5n-frqEFneI0GFLSolSd84LwS4YqdxyHP4r6cISihfpSIvyYqMX1H47HxCliz3tQwD6kNTBde3SILC0-PWH_Lo3sC8QqhE9iIMi1-O93KLYNV2nBoBVXzBnOPcWOKIFgZVLBptFbRvpr3DjfNtY-XQP5t922OE1E1gli0q_vSJiCAylRjJRd4JtF6qUQR_xeGtb6iNWWyapEDOukdJFRaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1c7db692.mp4?token=IR9fKTJZdZbEBC6rRiox_sGZKJBX7KB3dZCY9hXoW800miyGeleb7j3hVsDTXdB5OfGZXpp0OG1jtRJwAdlsrNWXwvTS9pu5vZyhHKFOjOP4H3_GpshbV5tWaVud5KUR5n-frqEFneI0GFLSolSd84LwS4YqdxyHP4r6cISihfpSIvyYqMX1H47HxCliz3tQwD6kNTBde3SILC0-PWH_Lo3sC8QqhE9iIMi1-O93KLYNV2nBoBVXzBnOPcWOKIFgZVLBptFbRvpr3DjfNtY-XQP5t922OE1E1gli0q_vSJiCAylRjJRd4JtF6qUQR_xeGtb6iNWWyapEDOukdJFRaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی به پالایشگاه‌های نفت TANECO و TAIF-NK  روسیه حمله کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127578" target="_blank">📅 12:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127577">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abae735a11.mp4?token=i6DJ-lLtwg8vY1ZpiGjuYgWPE80EvkD-p47YV2QsDXLlLDAxd3PrkaY8WTtlEtjEmM5_sTZJhad3Ghy3P7GAofinL3XqGtdOzVxabfPG72pONjQzip8DyiXqoNcpxDeD5R-CjecRnqP0A84lzFU8vLCydAJhG751asxhSnaVCD7ASofgReb4uUlboNjd4x-tKFWdDARZpwYmu1q1SObk53qKNAAFqTJmK_pBiheUbBBsTW1xv1fg2wrz7EuWQ8AZd65bJQ806NxaG4aL3rC7T0JSn8E4GZCtGKilTEqmjjmI1DyegDyGLqi0X9MHarJRK1uF6vQA8OSZtG90hKSE_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abae735a11.mp4?token=i6DJ-lLtwg8vY1ZpiGjuYgWPE80EvkD-p47YV2QsDXLlLDAxd3PrkaY8WTtlEtjEmM5_sTZJhad3Ghy3P7GAofinL3XqGtdOzVxabfPG72pONjQzip8DyiXqoNcpxDeD5R-CjecRnqP0A84lzFU8vLCydAJhG751asxhSnaVCD7ASofgReb4uUlboNjd4x-tKFWdDARZpwYmu1q1SObk53qKNAAFqTJmK_pBiheUbBBsTW1xv1fg2wrz7EuWQ8AZd65bJQ806NxaG4aL3rC7T0JSn8E4GZCtGKilTEqmjjmI1DyegDyGLqi0X9MHarJRK1uF6vQA8OSZtG90hKSE_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار مهیب تانکر حامل سوخت قاچاق در مکزیک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127577" target="_blank">📅 12:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127576">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5264c9f71c.mp4?token=OadbxhalsfAX-uz6TTI75tLYjEf4ufYkirrKVWjysFwc5atY5pRelREGOt-5L5SioLeqzGv9UO7nGXbhp8i6Am5-GhVUJ3E3ro2YG0_jSqVLHcErW5oxs3PWtJD9heYeg1U2-o6G0oNGDav7SLRmf6ipZZDuWDgoQ8XeYxlYWEUiNb5DWdiJXcMVw5As5KWBTsWFLRutJbLWK2Sbagio6bLS6MH2_UDtrOvqWwyVBV3DKXWE523zmnZYrBuqeddEtJ9i4JXgxPV1Q-bhQtXkQrPzyOT1ygjLpgZ8jcNRWgAeMtzit2km_hL_Ct9tVhUqTODc12bioakZ1hZVsVa1uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5264c9f71c.mp4?token=OadbxhalsfAX-uz6TTI75tLYjEf4ufYkirrKVWjysFwc5atY5pRelREGOt-5L5SioLeqzGv9UO7nGXbhp8i6Am5-GhVUJ3E3ro2YG0_jSqVLHcErW5oxs3PWtJD9heYeg1U2-o6G0oNGDav7SLRmf6ipZZDuWDgoQ8XeYxlYWEUiNb5DWdiJXcMVw5As5KWBTsWFLRutJbLWK2Sbagio6bLS6MH2_UDtrOvqWwyVBV3DKXWE523zmnZYrBuqeddEtJ9i4JXgxPV1Q-bhQtXkQrPzyOT1ygjLpgZ8jcNRWgAeMtzit2km_hL_Ct9tVhUqTODc12bioakZ1hZVsVa1uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس: طرح مدیریت تنگه هرمز یک اقدام ماندگار مثل ملی شدن صنعت نفت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127576" target="_blank">📅 12:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127575">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4260ab1895.mp4?token=iDtMaFm1v8cRcFxSuLBecIgPjJsoLztwXEglaexC8EuyMgCU5u733azh-Z-ZgA2ApCgG5aD2IOQyZgEFaIWIn5Lz327qf_SrLzLTWP9gjiq8-L3x6qiIDPB5Wmb-DYOdWDe8EkXVg5Wuh7FrToqtK3pwP4gZNlomsLaHrkimuGCazgjEk8P7g1NzafTa16A8GUF2wBuf_eUM6VM_aR2GvJhvwuiMsXidMgxm8ufNcTSg3NEQYD4ODFCs7E_4j8w8Spst3aU_Iecsu5DGdee8A-Z-UeHCqRMIUzrryMBk1raH5DibQVi6UFYpsOyOse8p4dW1vrOjPCAOJnGybOAmWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4260ab1895.mp4?token=iDtMaFm1v8cRcFxSuLBecIgPjJsoLztwXEglaexC8EuyMgCU5u733azh-Z-ZgA2ApCgG5aD2IOQyZgEFaIWIn5Lz327qf_SrLzLTWP9gjiq8-L3x6qiIDPB5Wmb-DYOdWDe8EkXVg5Wuh7FrToqtK3pwP4gZNlomsLaHrkimuGCazgjEk8P7g1NzafTa16A8GUF2wBuf_eUM6VM_aR2GvJhvwuiMsXidMgxm8ufNcTSg3NEQYD4ODFCs7E_4j8w8Spst3aU_Iecsu5DGdee8A-Z-UeHCqRMIUzrryMBk1raH5DibQVi6UFYpsOyOse8p4dW1vrOjPCAOJnGybOAmWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وسط اتوبان حکیم تهران، پیاده موبایل یه نفر رو دزدیدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127575" target="_blank">📅 12:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127574">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
اژه‌ای: به آمریکایی‌ها مطلقاً اعتماد نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/127574" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yw02O7T0DKK_4Pa4oKt4oOd3F9sZa10SStd7AujpWI2Dk43jhegl6yxXmKasIPSnfdKS2p0TX47jYpdCfRKtUsZZaLn0AR3Hpz2064Rv_UvYbcWtbGwfIviFVggloMOqGdBBb0mcdwkh6UvV-v63EoCQyK7ohc5qus7msbpZVMIXZnmkRqFE5Rrxd8F8fP6eOA8xDhstxcf87Ofqt1g2mQBIOM2K5sj2ZXqTzpbc-L9KlGFcsyFq5oaWLs5gSZE_DnUoM2fAyzz31uFeEj8o3tA2rmUwIfvtpjUiB2yTVIC1D-OBrtuGEKCz3XbFBPOTgKcT2fGCZH0TvjXtMpZa2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه سی‌ان‌ان به نقل از پنج منبع آگاه از سازمان اطلاعات آمریکا: ایران در هفته‌های اخیر تلاش‌های خود را برای پلمپ انبار اورانیوم با غنای بالا، به طور چشمگیری افزایش داده و عمداً دهانه تونل‌ها و ورودی‌ها را با انفجار مسدود کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127573" target="_blank">📅 11:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
آخرین قیمت دلار ۱۷۲ هزار تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127572" target="_blank">📅 11:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه داری آمریکا اعلام کرد که با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران «احتمالا تا پایان همین هفته (میلادی) یا اوایل هفته آینده نهایی شود.»
🔴
وی درباره پیامدهای جنگ علیه ایران افزود: «ما درک می‌کنیم که در ماه‌های اخیر شرایط سختی سپری شد و افزایش بهای انرژی بخش زیادی از رشد دستمزدها را بلعید، اما ما در حال عبور از این وضعیت بحرانی هستیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127571" target="_blank">📅 11:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127570">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از منابع: ارتش آمریکا برای اجرای مأموریت زمینی به منظور تصرف اورانیوم ایران در اصفهان، تجهیزات را سریعاً آماده کرد
🔴
اما ترامپ پس از آنکه به او هشدار داده شد که این اقدام به احتمال زیاد منجر به واکنش خشونت‌آمیز ایران خواهد شد که باعث طولانی شدن جنگ و افزایش بی‌ثباتی اقتصاد جهانی می‌گردد، این گام را به‌طور موقت متوقف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/127570" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b6b203f35.mp4?token=Zt8TDRy0joehaxxqX-N0EI1_oL1A_jVtkQDzpArcRXc-Ib5gclqylVMjJiWRm4fhaQvxTGQh6n07sSLDtiF6bd4uaBdeundGLF4s8J23_5HXlDHpuf0MCgekd3AoYaOTULUTj8U5_dS4RuJObxXjugB1ubTTf7iCCsFIGcGSM9bH32YGzrQ2gZuZGWob2rCZBS21-7-z5cpjdcwXG64QCT5og0wlxTP2wVXxTu4tAGpgHUviq1zXwwzRaKIKLe6bbBNnhI6UK7HZBjiCkCIbg-gr0MokPjeDAdQkDChIUtd9_Z_w4cGRz6vNeObKWwRePpkj_q8So14INmsNq07suA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b6b203f35.mp4?token=Zt8TDRy0joehaxxqX-N0EI1_oL1A_jVtkQDzpArcRXc-Ib5gclqylVMjJiWRm4fhaQvxTGQh6n07sSLDtiF6bd4uaBdeundGLF4s8J23_5HXlDHpuf0MCgekd3AoYaOTULUTj8U5_dS4RuJObxXjugB1ubTTf7iCCsFIGcGSM9bH32YGzrQ2gZuZGWob2rCZBS21-7-z5cpjdcwXG64QCT5og0wlxTP2wVXxTu4tAGpgHUviq1zXwwzRaKIKLe6bbBNnhI6UK7HZBjiCkCIbg-gr0MokPjeDAdQkDChIUtd9_Z_w4cGRz6vNeObKWwRePpkj_q8So14INmsNq07suA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عباس عراقچی: مسئولیت مذاکرات توسط نظام به قالیباف سپرده شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127569" target="_blank">📅 11:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
هشدار سیلاب و تگرگ در ۹ استان؛ گرمای غیرمتعارف در شرق کشور
🔴
امروز (شنبه ۲۳ خرداد) شمال غرب کشور به‌ویژه استان اردبیل با بارش‌های سنگین و خطر سیلاب مواجه است.
🔴
همچنین در نیمه شرقی آذربایجان شرقی، ارتفاعات البرز، مازندران، سمنان، گلستان و بخش‌هایی از خراسان شمالی و رضوی رگبار، رعدوبرق و تگرگ پیش‌بینی می‌شود. فردا از شدت بارش‌ها کاسته می‌شود.
🔴
وزش باد و گردوخاک در تهران، قم، خوزستان و یزد ادامه دارد و گرمای غیرمتعارف در نیمه شرقی کشور ماندگار است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127568" target="_blank">📅 11:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
تحلیل روزنامه ( خراسان) نزدیک به قالیباف: تفاهم ایران و امریکا قرار نیست اختلافات را حل کند؛ فقط یک فرصت است که طرفین خود را برای جنگی دیگر آماده کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127567" target="_blank">📅 11:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7YfEeOY4O6ZLQJPLDzr5_vIXmIZImgrZ7H5_x_XdF_A0Cic2CwJ6qK9K3vILC87S3hFcS2UfxxD_G7pThY9Td5PxVCgR41FkSL6z-cQraHI1wmEn0pkcDFEHplShQxphHxDiRhr2S4mgSaa1tYGqT9Facgsko4X1d3ujus2uPF65izpLoRBMLyKbgcN4zwjunFlqisNeE2rqh0IYdkMXLBaFbW35gdrmwibSWMmm5ckwjlsSNGw1wb32fElSmhu_G3T0vbCyeBLFRDkAWk3bp_yXC5kybSjwHqLCvmgzYmmsj9kdHg9P8nXmR45Aea2S_zxFgjuBKV18sSv5IOZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۸۷.۳۳ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127566" target="_blank">📅 11:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
خبرنگار الجزیره: حمله پهپادی اسرائیل به شهر آرامتا در شهرستان جزین در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/127565" target="_blank">📅 11:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
یک مقام ارشد آمریکایی به نیویورک تایمز گفت: «میانجی‌گران و مقامات نظامی ایرانی تأیید کردند که رهبر ایران از توافق راضی است».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/127564" target="_blank">📅 11:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ecd56daa.mp4?token=YQziUOjcTVQkzhHFuDJwVl5DHKaTgEnpFtftmKRIgRtKQyfAggBw7yLkVrj9gAZ3sh9j2O-KjeH_R9vzjmRiBZqcvMwbhSfUl-el_0xqyEnvNmUF4eYx3t7sWJ6yDdpfM_Fg7jqpnrQ5J0R_otovIoGoWDYntBgjuGepQ4pJr_IMUVyT1Cg3gr3Gd_bmC_Wj9Ue0djTnI-9v_-VHTSDxlO6JBZK4Pj8pbxzshe-KQ4E-iXvtDhFmfngBh4rosqHXI1iH-juYjj5y7_IqTyKhYR8eliwRWu7oIyKUU0Gm7BaEe3fAZQ7oz54v9dwJUjsXYLA5bZ2VhycD9_dMCNih3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ecd56daa.mp4?token=YQziUOjcTVQkzhHFuDJwVl5DHKaTgEnpFtftmKRIgRtKQyfAggBw7yLkVrj9gAZ3sh9j2O-KjeH_R9vzjmRiBZqcvMwbhSfUl-el_0xqyEnvNmUF4eYx3t7sWJ6yDdpfM_Fg7jqpnrQ5J0R_otovIoGoWDYntBgjuGepQ4pJr_IMUVyT1Cg3gr3Gd_bmC_Wj9Ue0djTnI-9v_-VHTSDxlO6JBZK4Pj8pbxzshe-KQ4E-iXvtDhFmfngBh4rosqHXI1iH-juYjj5y7_IqTyKhYR8eliwRWu7oIyKUU0Gm7BaEe3fAZQ7oz54v9dwJUjsXYLA5bZ2VhycD9_dMCNih3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/127563" target="_blank">📅 11:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453f586f69.mp4?token=TRAerWYM_9i2TNl8_k3W1sK5a2qqS-AN5nXeBc5ZKjAD7k_EJFSikjtCZ3Vv_UhnXSBDH8zopfSjbYJILMVfs6cORh6anm6YMhMIzCOit__wKGBnTSkMCshx2UBuNSEz3Evox4gvAG3Xc0sFm-2TvSGEfe9JLKbJTt_QejEeMrWlw3q8M8v_3QORmTzo9Ot-oP1eIeNzZp2apCrF2QJRAYkxbQ0GOrhpHiA0Bo5qoDaB97jNtIndw8qZ9w6DX6PaJ750up872IByGCnGtJDRK4MAArl1NgFd9DRVIEco_Kbf9ltm469kAFfLPOQJlsoldRdoum__ozZHczjLNDXooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453f586f69.mp4?token=TRAerWYM_9i2TNl8_k3W1sK5a2qqS-AN5nXeBc5ZKjAD7k_EJFSikjtCZ3Vv_UhnXSBDH8zopfSjbYJILMVfs6cORh6anm6YMhMIzCOit__wKGBnTSkMCshx2UBuNSEz3Evox4gvAG3Xc0sFm-2TvSGEfe9JLKbJTt_QejEeMrWlw3q8M8v_3QORmTzo9Ot-oP1eIeNzZp2apCrF2QJRAYkxbQ0GOrhpHiA0Bo5qoDaB97jNtIndw8qZ9w6DX6PaJ750up872IByGCnGtJDRK4MAArl1NgFd9DRVIEco_Kbf9ltm469kAFfLPOQJlsoldRdoum__ozZHczjLNDXooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو هند، یه هواپیمای روسی نظامی آن-۳۲ سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127562" target="_blank">📅 11:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKrBwIz3Pb58fL2R_UyzVRkiKiWXXYpwr8kmGC1DC6Hb311Glz20M_xx6-xn1XaUPh82EIyVBM7O6a6PiSg7y0P9s1tN5v7e4pqudZ9w3ee0jclsE2DzIB00XVNLd5EG3_6VI7wxJJuCi_mSDg1nc6SpksLdWHFoViuPWQTkmkIfCOpyatMysE5W46JHNHDWFqCxsh3JbdeaD9b18PWzdRwW3VvHvnCqRCqaPM5qgO_SA30CDIlDM_3pt5XAGSG1tPrI0O-6cT3dhFTyt7ii0yRZ5tnIWq0BS8aPvqWNVI4RGun1lHL7s9yqbASYZi601sh5QFp300KsML1-uiq_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: مذاکره منجر به جنگ نمیشه بلکه مقاومت منجر به جنگ میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127561" target="_blank">📅 11:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
روزنامه وال‌استریت ژورنال به نقل از منابع آگاه گزارش داد که سفر یک هیئت دیپلماتیک قطری به تهران، به چند روز حملات متقابل میان ایالات متحده و ایران پس از سقوط یک بالگرد آپاچی آمریکایی پایان داد و رئیس‌جمهور آمریکا، دونالد ترامپ، را متقاعد کرد که حملات شدیدی را که علیه ایران در نظر گرفته بود، لغو کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/127560" target="_blank">📅 11:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGE5Crfs_bOLG0JN1DwYD9tQ6aLNjQp0vT18eNsokagMvEbv-W7gxCd418UMwOjwKUve4cPn1nfSiHkvU9pwD9Pznrvvw0WYqxXPl4nb-jfUuXdzLQSW-8XeOgR3w2FhjN6tWMWsC00rBl1HcXvoyMWj8d1geYX8Wjm4JQHejKiPNqYg421HPnGQfrGKykFU5qyQ3aEtXxKBfcsLcCu2TrI4CHGhOC7Ri6ITa6kZXqRF_f2BIMMP1xKh5hdPhFEvbzcnOZ5Dh-lOukGoJQqCJePGvABgo_xuly8t_tzNcPrCHL3T8WGoADf5aK79dGH33uhTgZk5pAlb3GKaHgSxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرمایه ایلان ماسک حالا از مجموع ثروت ۴ فرد ثروتمند پس از خودش بیشتر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/127559" target="_blank">📅 10:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127558">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
لیبرمن، وزیر جنگ اسبق اسرائیل:
توافق، پیروزی ایران و فاجعه‌ای برای اسرائیل است
🔴
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، مسئولیت کامل این وضعیت را بر عهده دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/127558" target="_blank">📅 10:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران بخش‌هایی از ذخیره اورانیوم بسیار غنی‌شده خود را با ریزش تونل‌ها و مین‌های انفجاری در اطراف ورودی‌ها مسدود کرده است. این اقدامات در پی نگرانی‌ها از احتمال عملیات آمریکا برای تصرف این مواد، دسترسی به اورانیوم را به‌طور قابل‌توجهی دشوارتر و خطرناک‌تر کرده و تلاش‌ها برای حذف یا نابودی ذخیره تحت هر توافق آینده را پیچیده می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/127557" target="_blank">📅 10:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127556">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aonk2PKuTpFJC0A-vEsONXRBdOJ2lu8Jvu-fyVoa8LT9F7msjzdjS0yKvjQLd8mw4kCnv_lWlAkiJBJvY3zCzJGIzCkMk02DYOkUp2xwBA4-wRrpUsb7_zrkQbRQJ_qy_WFZw5_N7gmVoD_OVQfvOVTaGY1Etg3tGoiwnlJxW72un_E_1cJIshvi2hCS6AsS4m-U2FwBTKyJz3wZMzxHh5VI9c22KT1lNXHC94_M4zu7i7AR2L6xWmuE27vQM_rTnc0U3QZPzj7J0ddDdA_q4updPCtDM4tkrdIMc8gp_N4XdgPV6Je83JsNDniBDsLmNUaZSNQgB9jfpcTClbKflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس: نتانیاهو امیدوار بود که جنگ منجر به تغییر رژیم در ایران شود، اما رقبایش اکنون او را متهم می‌کنند که با پذیرفتن شرایط آمریکا، اسرائیل را به «دولت دست‌نشانده» تبدیل کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127556" target="_blank">📅 10:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127555">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رویترز: ونس توافق‌نامه صلح با ایران را امضا خواهد کرد
🔴
خبرگزاری رویترز به نقل از مقامات آگاه ادعا کرد که معاون رئیس جمهور آمریکا توافقنامه صلح با ایران را امضا خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127555" target="_blank">📅 10:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127554">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDONxOy8SQJAigvQb-APuUtMr7jr59rrLId6nMipnvfrNbPUqjsTA4r6NE_JgJV0gVGA58TzyRYYCPp8_5KvqRGu0WrWcv1ZDv7IpVEyHXLOfip8pQdMvA05QZSpkTMf7EaF2Ib8HgJqh4rJo1ZLGfHgW3OCC52kEG9Yo4mMihUVB3rJV0EijDrQtm47mIGhi_iueGnCK9tNxmGPuwFiQdody8S15wA_rLN0yfyASQqtMA21ex5Qfa_HVnhGuriMOIOXfr941HZiaSVZm6icCRnTT_gjNy4aViNeFdGBBUOKw-4LBY2M9Wc9i4p2M4NZ8k7VSBGiiE_0fLKaGYrN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس باز نشده ۹۸ هزار واحد رشد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/127554" target="_blank">📅 10:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127553">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
آحارونوت: احتمالا توافق تهران-واشنگتن شامل آتش‌بس در لبنان هم باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127553" target="_blank">📅 10:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127552">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل، هشدار فوری تخلیه برای ساکنان ۲۰ روستا در جنوب لبنان صادر کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/127552" target="_blank">📅 10:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127551">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در دزفول
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/127551" target="_blank">📅 09:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127550">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
طبق گزارش شبکه المنار، وابسته به حزب الله، نیروی زمینی ارتش اسرائیل در پوشش گلوله باران گسترده توپخانه، حمله خود به سمت جنوب شهر نبطیه، پایتخت حزب‌الله در جنوب لبنان را آغاز کرده است.
🔴
خودرو های زرهی اسرائیلی به به صورت گسترده در حال هجوم به سمت جنوب شهر نبطیه مشاهده شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127550" target="_blank">📅 09:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127549">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5tKfgPVNRuKfwAcKJOKs99-CE1VwLGOa5kdTFAg_YomH1k3lzhWOCci6qlojfBgGtqmt5ZR32am0EvxRz83C-HOvnAIMX9hFbuv8HXutS582ktpcQzfhj9ctgUVc3Qz5-ekqFdEeKSdQaIcp9HYdPaJdlrnzT1rLbD_QI4c-gFJ14MLOnquUKbLthx_dDjYnmElyQSHNf6QtP3RRbxSUoaFnGod4pd4brr_1cIZSVJOITSO4v_-1WsHU7gnPdRCN1-0sP0_tDn0TjFJhzeJi5Wt31IRIfHH6n0-vnW8rixFjOrv3Gs9K4aYCRiPuJnyRGkOJD0e74ecngiorRpYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشف ۴۱۸ کیلوگرم تریاک در یزد مأموران پلیس مبارزه با مواد مخدر استان یزد موفق به کشف ۴۱۸ کیلوگرم مواد مخدر از نوع تریاک در شهرستان یزد شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/127549" target="_blank">📅 09:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127548">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کانال ۱۲ عبری از رصد ۳ راکت شلیک شده از لبنان به سمت شهرک‌های صهیونیست‌نشین «المطله» و « مسگاوعام» در شمال اسرائیل خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/127548" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127547">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
دانشگاه شریف از امروز به روی ۴۵۰۰ دانشجوی مقاطع تحصیلات تکمیلی باز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127547" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127546">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نیویورک‌تایمز: ایالات متحده به شرکت آنتروپیک دستور داده است که دسترسی تمامی اتباع خارجی به مدل‌های پیشرفته هوش مصنوعی خود، «Mythos 5» و «Fable 5»، را مسدود کند و دلیل این تصمیم را نگرانی‌های مربوط به امنیت ملی اعلام کرده است.
🔴
آنتروپیک اعلام کرد که ناچار شده فوراً دسترسی را غیرفعال کند؛ اقدامی که حتی کارکنان خارجی این شرکت را نیز تحت تأثیر قرار داده است. این شرکت همچنین این وضعیت را «یک سوءتفاهم» توصیف کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/127546" target="_blank">📅 09:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127545">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری/ ترامپ میگوید ایالات متحده امریکا رهبر گروه «ترن د آراگوا» را به قتل رسانده است.
🔴
متنی که ترامپ منتشر کرده:به دستور من، فرماندهی جنوبی ایالات متحده یک عملیات ضربتی سریع و کشنده انجام داد تا «نیِنیو گوئررو»، رهبر بدنام گروه ترن د آراگوا، که یکی از خونخوارترین سازمانهای تروریستی روی کره زمین است، با موفقیت ترور شود.
🔴
پیش از بازگشت من به دفتر، جو بایدن مرز جنوبی ما را به روی میلیونها جنایتکار غیرقانونی گشود و به این ارتش بیگانه اجازه داد تا با مصونیت کامل، شهروندان آمریکایی را تجاوز، مثله و به قتل برسانند.
🔴
در طول مبارزات انتخاباتیام، قول دادم که این هیولاها را از کشورمان بیرون کنم و برای خانوادههای کسانی که به قتل رساندهاند، از جمله «جوسلین نونگارای» ۱۲ ساله عزیز، «لیکن ریلی» ۲۲ ساله و بیشمار روحهای پاک دیگر، عدالت برقرار کنم.
🔴
با این اقدام، ارتش ایالات متحده برای آنها، خانوادههایشان و عزیزانشان تلافی کرد. در اوایل دوره ریاستجمهوریام، به قولم عمل کردم و ترن د آراگوا را به عنوان یک سازمان تروریستی خارجی تعیین کردم، هزاران جنایتکار شرور را اخراج کردم و علیه کارتلهایی که مدتهاست با شهروندان ما میجنگند، در حالی که رهبران ضعیف آمریکا را درمانده و دفاعی رها کرده بودند، اعلام جنگ کردم. این اقدام با هماهنگی نزدیک با دوستانمان در ونزوئلا انجام شد که با آنها بسیار خوب کار میکنیم.
🔴
در نتیجه، تروریستهای ترن د آراگوا دیگر در ونزوئلا یا هر جای دیگر پناهگاه امنی ندارند و تحت رهبری من، این قاتلان بیرحم و اربابان مواد مخدر را در هر زمان و هر مکان پیدا خواهیم کرد و به اعماق جهنمی که به آن تعلق دارند، خواهیم فرستاد. خدا آمریکا را حفظ کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127545" target="_blank">📅 09:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127544">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
گزارش‌ها: یک فروند A-10 آمریکایی به پایگاه بازنگشته است
🔴
منابع رصدی گزارش داده‌اند یک فروند هواپیمای تهاجمی A-10C Thunderbolt II با شماره ثبت 78-0614 پس از عملیات اخیر به همراه اسکادران خود به پایگاه بازنگشته است.
🔴
بر اساس گمانه‌زنی‌های مطرح‌شده، احتمال دارد این همان هواپیمایی باشد که در جریان عملیات نجات افسر سامانه‌های تسلیحاتی یک فروند F-15E Strike Eagle هدف قرار گرفته و توسط ایران سرنگون شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127544" target="_blank">📅 09:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127543">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یدیعوت آحارانوت به نقل از منابع اسرائیلی: اگر ایران در صورت هدف قرار گرفتن ضاحیه جنوبی بیروت به ما حمله کند، ما تلافی خواهیم کرد و اتحاد جبهه‌ها را نخواهیم پذیرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/127543" target="_blank">📅 09:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127542">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کیهان: اگر تنگه هرمز را باز کنید دشمن دوباره حمله می‌کند!/ هیچ آدم عاقلی نقطه قوت خود را پای میز مذاکره نمی‌برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/127542" target="_blank">📅 09:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127541">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxEaJscVM8WveKyux8429vqevwFCbEmJyra7nIbtWYVGAzA6G4pijPbzROXg7EB7PP88I4jvqHrTsj-mDEJdCBOHXXhcpyQYizi0yAvaZwWNTH5jQrx0XIBS2LdNxgb-30vQKLxtmRqQh2aP6PA7N16mAO_65Htsads6khIkCdbuAQOJSMpz8iy9tG4lzc3uHqUFgMDQgkOORA1s9K_tkSxRZLqgXZFu0NFkkbTqEh0FzmzVVIpsXh2e6VTfmFedVf6Is1QGFb6mgAu3A7_ZVBzvFldbrCpmucJjHrCt-g07WxWqM0CHjeocqljDy06zoxpfT0K6DwuLOFcR7AijDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارآگاهان پلیس آگاهی شهرستان آستارا، با اقدامات فنی و اطلاعاتی نامحسوس محل احتکار و دپوی غیرقانونی کالا‌های اساسی و موادبهداشتی را شناسائی و افزون بر ۱۵۳ میلیارد ریال ارزاق عمومی در آن کشف کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/127541" target="_blank">📅 09:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127540">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران در بحبوحه نگرانی‌ها از عملیات زمینی ایالات متحده، بخش‌هایی از ذخایر اورانیوم با غنای بالای خود را با تخریب تونل‌ها و کار گذاشتن مین‌های انفجاری در اطراف ورودی‌ها مسدود کرده است.
🔴
این اقدامات دسترسی به اورانیوم را به طور قابل توجهی دشوارتر و خطرناک‌تر کرده و می‌تواند تلاش‌ها برای حذف یا از بین بردن این ذخایر را تحت هرگونه توافق آینده، پیچیده کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127540" target="_blank">📅 09:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127539">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر خارجه فرانسه: ایران و آمریکا از فرصت موجود برای دستیابی به توافق استفاده کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/127539" target="_blank">📅 08:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127538">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رویترز: نیروهای آمریکایی چندین پهپاد تهاجمی یک طرفه ایرانی را که به سمت تنگه هرمز در حرکت بودند، سرنگون کرده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127538" target="_blank">📅 08:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127537">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY8oZWIo1X-3eUjiyl-FYTxe_Qu15pSpcrbUMX7DeqtjpGFHmaEpuovCcYge9qknvRiu8f2eKhHE_R09P0E-6nZerKj2ICqHzsvFONorFAMpJ0t6SgNFa34Abq5ieY8YwC-FcfgkHCQe1RxQWAhpwjqnOCBcQGdaRiGtZ_OY1GKXO4H_XCGBk6VBkiLZ8v7NN9WsugSL7sNN5NXOyNtMZPenF2HXDQu36ol2TWVYZuvEYQUhqpdhCT52Mph3SLpGgspryKF0wcFiF5eE7gtgglyHtvZLqyey5PQNr2bWmvsLczdfg4CXCGAiUqqn3eyfJES3PEgn0DdzuzBHKMrNRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رافائل گروسی برای دبیرکلی سازمان ملل اعلام آمادگی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127537" target="_blank">📅 08:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127536">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سی‌بی‌اس: کاهش ۳ درصدی قیمت نفت در پی خوش‌بینی‌ها نسبت به توافق تهران و واشنگتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127536" target="_blank">📅 08:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127535">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: رفع تحریم در ازای اقدامات ایران در خصوص برنامه هسته‌ای صورت خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/127535" target="_blank">📅 08:44 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
