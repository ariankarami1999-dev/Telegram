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
<img src="https://cdn4.telesco.pe/file/YPO5RjznOiyMGhISp0pVl4Edv01brtpJVfeHftxgiTe0kT8kFfxtsRmWLznrpyDLdSZwTbngc9HpnMzzPOpjt73f5rO_jhVrmrSQf4L9ZsUTnKLdV4PERYJdhfKaHJofvo7FKOyx4x-NdEpGZdV7sDUI0RToU3KQjgt4OnKSEZTxmDKes5Mu5uG8YP6KNk3K_M56_MBpw7A-e1CD4-6wQqQtArhCUC3fKPPp1r0RnYsg599nsTgE-zsxbFxJiNWlK8t3eFrfBX8mD9ROsTjby5gfK69Fdl5d4J_qvUk-H1E9snK8Ub2Ig3HZUHNDBIw5evxehtashM9vMR5kALTx9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 22:11:38</div>
<hr>

<div class="tg-post" id="msg-127214">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ادعای اکسیوس: منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/127214" target="_blank">📅 22:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127213">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نظرسنجی شبکه ۱۲ اسرائیل : ۶۲٪ از اسرائیلی‌ها به ترامپ اعتماد ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/127213" target="_blank">📅 22:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127212">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
رسانه اسرائیلی : همه چیز در پست رئیس‌جمهور درست نیست!
🔴
هیچ توافقی بین سپاه پاسداران و اسرائیل وجود ندارد و اسرائیل ۱۰۰٪ هرگز آن را تأیید نکرده است.
🔴
تنها چیزی که برای گفتن باقی می‌ماند این است - به اعمال او قضاوت کنید نه به کلماتش!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/127212" target="_blank">📅 21:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127211">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
طبق منابع العربیه، عباس عراقچی، وزیر امور خارجه ایران، ممکن است در ۱۳ ژوئن به پاکستان سفر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/127211" target="_blank">📅 21:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127210">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فارس : منبع آگاه: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/127210" target="_blank">📅 21:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127209">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ_pLRavlgiainAGQrepR_Pt5khhR5datDLww_mi7Su4RXkUleOhl9WShWfE-gS3fwNrELutepKVjgIFxXCAqJVNWUys8nkN3r7FuShq6ZIV6craU6sWEyvlf4P4iAQUX_Zt2RqlYGBspFoF2cIV9K_SQFtG1TjldotsH7CuyHIz672WpJ5d8Dje7N6vrxpwUVcmm3h04_rC_sJZ5DZLowxZA3A1derpjrQpJaldJa1mqEuJpDdtJp5bBWf1ZS-es4xIYUngWs_N3mv5kOp3jF-FCvgO5PJPveJW8Lyxeh9kzRXdSUBvWQXy8HTgLYJjXkYhfaLcca3zzQT4NISDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیبالا تو ویژه برنامه جام جهانی فوتبال360: من عاشق ایرانم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/127209" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127208">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وال استریت ژورنال: توافق قطعی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/127208" target="_blank">📅 21:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127207">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سه منبع به اکسيوس می‌گویند که شکاف‌های کلیدی در مذاکرات ایران در جریان مذاکرات چهارشنبه با میانجیگران قطری حل شده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/127207" target="_blank">📅 21:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127206">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مقامات اسرائیلی از توییت ترامپ غافلگیر شدند.
🔴
یکی از مقامات به i24NEWS گفت که مقامات اسرائیلی در حال حاضر به اظهارات علنی ترامپ متکی هستند و تأکید کرد که اسرائیل پیش از تعیین صحت ارزیابی رئیس‌جمهور آمریکا، نیاز دارد ببیند پاسخ رسمی ایران چه بوده
🔴
او خاطرنشان کرد که تجربه گذشته نشان می‌دهد این ارزیابی ممکن است همیشه دقیق نباشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/127206" target="_blank">📅 21:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127205">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فووووووووووووووووووودی</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/127205" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127204">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فووووووووووووووووووودی</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/127204" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127203">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سه منبع به اکسيوس می‌گویند که شکاف‌های کلیدی در مذاکرات ایران در جریان مذاکرات چهارشنبه با میانجیگران قطری حل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/127203" target="_blank">📅 21:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127202">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4B8e0fU3H_YB9RrCks3LK5Rd82kbZJ-VqShFedbud7D7XoUzL0M1X0ZOFzuHHwAcn2F8bBCKNBhnHKc0zwKh1oDE_06HbzLBhykaRQ_j1SWYtHs3LWVTV9Wl0sW6-PgBfY6EmrcoVwt1qtAIFt1_MlTpY-K-hJD0tRytfG27p6tXOpMSR3QgPWe4mzqMoCu0KEO6t6scxqo7eJGGxcIgNM4irjYz9kl8AVQBVtsnBVG7X7pgYhr_NGPXQYbdi6nM7vBMTSCT2avs_FiDxP4KbZUE2bvtb3jwVCtMH4goM7lSVIVJcMO2R3UbcHn8DDUybMXQiZlYtfWfWvuLYjTvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت به زیر ۹۰ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/127202" target="_blank">📅 21:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127201">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سپاه : ما کاملاً آمادایم تا به هر اشتباه یا اقدام طرف مقابل، با قاطعیت پاسخ بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127201" target="_blank">📅 21:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127200">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
قیمت تتر ۱۷۶ هزار تومان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/127200" target="_blank">📅 21:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127199">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
صداوسیما:
ترامپ بازم عقب نشینی کرد، الله اکبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/127199" target="_blank">📅 21:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127198">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
شبکه کان به نقل از یک مقام اسرائیلی:
آمریکایی‌ها هنوز از مسیر مذاکرات با ایران دست نکشیده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127198" target="_blank">📅 21:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127197">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YscMO7U4LpYnCvAsGXCno5cZRK3dTf5Wqzu1elgmJt4IWVM4KsgptwLnK7Md_K-pJLIpbFGKPtXZrmMuSdIfGlNTI-ARNoVLsxB5HqzAiHDvvTwjMVuft_pag080rZUDA3-djCChGdUoE45ozmFOUWPzpeO2hJh8Uw3s3HwIb7APDS2wzi7ZlHXd_G8R5PXHhTo6r2yS9B7a1Np_2sawmEX9ahEiWMm46hssFAuX4PMKi7_mxg95vbsFP2xxQDyvY3HCkPqqXOyAA3VOqPRr0ksPYHGDwOn80yipcVMiK3gMwk-urSYrv_59uzLxTruBN0rRcmCuErSLCi4DwCnG8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ: حملات امشب رو لغو کردم
🔴
با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایرانیان برده شده و تایید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده علیه ایران امشب را لغو کردم. مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات فراوان، توسط تمام طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران، تایید شده است. محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل و با اثر باقی خواهد ماند — زمان و مکان امضا به زودی اعلام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127197" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127196">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کان: یک کشور منطقه‌ای در طول تشدید تنش‌ها با ایران این هفته و در جریان حملات هوایی نیروی هوایی اسرائیل، مانع استفاده اسرائیل از حریم هوایی خود شد.
🔴
این اقدام برای مقامات ارشد اسرائیلی که انتظار همکاری مشابه درگیری‌های قبلی با ایران را داشتند، غافلگیرکننده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/127196" target="_blank">📅 21:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127195">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
العربیه به نقل از یک مقام اسرائیلی:
پیام روشنی از سوی آمریکا دریافت کرده‌ایم مبنی بر اینکه در حملات علیه ایران دخالت نکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127195" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127194">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4056b84464.mp4?token=IhsVBsDvav-JIwp7SNQisBDpUJisFwP9UeGX1A_ZFI28GWQsmSZv1BlSDl_ZzxxrODzRqxWcCN6appnkUECzWsnQlOow4G0gPMsAjofICCq1mGT09v1mqPIfXvcqZuO7M4iqo0ODA_QP7CvVqqW6O_rt0R2Io7-lLfS-RIzaLXgHiGYpHxzqp9prDRtAYS3eoaVacOICoxGjD0o9dB5tWwKi0ZZJMLH8XAZMVNSqkeJknqq1upCkrFSMjOLf0dS8Q1_SnHkI_5q9wR9N96ifsW0mchTN8sFVAhnDBMNpXQEeawyEBo1g-7mTZUH4Ytji_hznPhKMn_eBk49BLQ5v_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4056b84464.mp4?token=IhsVBsDvav-JIwp7SNQisBDpUJisFwP9UeGX1A_ZFI28GWQsmSZv1BlSDl_ZzxxrODzRqxWcCN6appnkUECzWsnQlOow4G0gPMsAjofICCq1mGT09v1mqPIfXvcqZuO7M4iqo0ODA_QP7CvVqqW6O_rt0R2Io7-lLfS-RIzaLXgHiGYpHxzqp9prDRtAYS3eoaVacOICoxGjD0o9dB5tWwKi0ZZJMLH8XAZMVNSqkeJknqq1upCkrFSMjOLf0dS8Q1_SnHkI_5q9wR9N96ifsW0mchTN8sFVAhnDBMNpXQEeawyEBo1g-7mTZUH4Ytji_hznPhKMn_eBk49BLQ5v_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اولویت من همیشه تصرف جزیره خارک بوده است. راستش را بخواهید، نمی‌دانم آمریکا توان تحمل آن را دارد یا نه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/127194" target="_blank">📅 20:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127193">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
روزنامه هاآرتص به نقل از منابع آگاه نوشت: ارتش اسرائیل برای اولین بار از زمان امضای توافق اسلو، در حال تأسیس یک پایگاه نظامی دائمی در شهر جنین است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127193" target="_blank">📅 20:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127192">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ab48468c2.mp4?token=K5NvysCv1qZiPBK1JlJZNiKfuvaDopaaci9oiNQLV3WmrnAdUozN0GXDdMYjThHbJ1nyxNurZk50D1TEr6SCVC_6q6Iek2pcBWWLqOGuEThZplwlEghEiTF1sGksnu7V5hC6etnrCntmPsA4Be8_f0ZDzZosuK7Ay_Bh7dEo7OtzC4bCYlrDHUzLnpcFykuwlJAm1el-VP3hU2Cpi58pH8_UM5BRURk47G22HtE7FiNYAqVoJewPYTZEDvZXuKSXarQuVTMZWVpoGBljtotBk5mh9gYpx7o7mPUZ-eHgZ4e5c7qBeJRyrKs4xgaqCBlPAVOOdZuTeI1IeWROr3X2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ab48468c2.mp4?token=K5NvysCv1qZiPBK1JlJZNiKfuvaDopaaci9oiNQLV3WmrnAdUozN0GXDdMYjThHbJ1nyxNurZk50D1TEr6SCVC_6q6Iek2pcBWWLqOGuEThZplwlEghEiTF1sGksnu7V5hC6etnrCntmPsA4Be8_f0ZDzZosuK7Ay_Bh7dEo7OtzC4bCYlrDHUzLnpcFykuwlJAm1el-VP3hU2Cpi58pH8_UM5BRURk47G22HtE7FiNYAqVoJewPYTZEDvZXuKSXarQuVTMZWVpoGBljtotBk5mh9gYpx7o7mPUZ-eHgZ4e5c7qBeJRyrKs4xgaqCBlPAVOOdZuTeI1IeWROr3X2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / انتقال تعداد زیادی از ادوات زرهی  توسط ارتش سوریه به مرز لبنان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127192" target="_blank">📅 20:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127191">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل : نتانیاهو یه جلسه امنیتی فوری با مقاماتش برگزار می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127191" target="_blank">📅 20:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127190">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: برای دولت کوبا عاقلانه نخواهد بود که تلاش کند به انواع تسلیحاتی دست یابد که توانایی هدف قرار دادن این پایگاه یا خاک اصلی آمریکا را داشته باشند
🔴
آن‌ها در این صورت وارد تقابلی خواهند شد که نه خواهان آن هستند و نه توان تحملش را دارند.
🔴
هیچ کشوری در جهان نمی‌تواند با توانایی‌های ایالات متحده آمریکا برابری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127190" target="_blank">📅 20:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127189">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZQq0WMIPa8_DRNyjZYt0q36iRPUZhJRRDoQ96XS_rnBNZo3MvtIV-kZlJJ-F3uS4Cwj_Qu_1vjqKnUTCH4Sb5x98uo6d-OoKIzmVz3Nq9lrws_k0_2pXCvxmwW5h-sXaSh9xKg6kTb9ERzXalUHue8JW6Pj5gx8Hm0Mui51MONQ9WrVjENcDjOqabnJlcoWj-I623Y8hceKnI8rriewbexOBbHsxJuJ40jfN65RBjwIGxz9VcM6o-e23r29eKEOPDP2XFvLEiKDvrGyZ2PNzefUk61Y1QP7t8TEPCljpzYvnpesgbduu8e-gEvObCCLOqqDQRi6G2USM2T3eUkDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظاتی پیش یک قایق ماهیگیری در سیریک هدف یک پهپاد قرار گرفت
🔴
مصدومان به بیمارستان منتقل شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127189" target="_blank">📅 20:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127188">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
خبرنگار الجزیره: حملات پهپادی اسرائیل به شهرهای کفر و تبنین در منطقه بنت جبیل در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127188" target="_blank">📅 20:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127187">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98745e731.mp4?token=q8jFjRVBQaKF9JFmWNv1nya5R-BswW1ZbNpWi47bfy8yOP9lo83E41ZOASKR4lpynlo03LbJARyDv7rvj8BVKNaY0mQIsBuVVUleASh0s4ubniGdvaFF84vEQc7STZlQj5wNcVk0lBgdBa-H0Z9YX7oynRD3h1IgtPbRJcg8rHPGwThQeExmIJyPTs37rjG8TKFwDPr36OOIarjIAPDaZJkCyA4qqy_jEocTVAU7Yu_KBAGz-4lQA6T6rV01s5sx7Pvlw501oYAZ6gqfIuGhSNbHGtPVlK8gCxsAbP0XnAIT5wt_vgJsqiilm2G05eKQK3bigdZg-rBzSPq1VZKwww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98745e731.mp4?token=q8jFjRVBQaKF9JFmWNv1nya5R-BswW1ZbNpWi47bfy8yOP9lo83E41ZOASKR4lpynlo03LbJARyDv7rvj8BVKNaY0mQIsBuVVUleASh0s4ubniGdvaFF84vEQc7STZlQj5wNcVk0lBgdBa-H0Z9YX7oynRD3h1IgtPbRJcg8rHPGwThQeExmIJyPTs37rjG8TKFwDPr36OOIarjIAPDaZJkCyA4qqy_jEocTVAU7Yu_KBAGz-4lQA6T6rV01s5sx7Pvlw501oYAZ6gqfIuGhSNbHGtPVlK8gCxsAbP0XnAIT5wt_vgJsqiilm2G05eKQK3bigdZg-rBzSPq1VZKwww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کمتر از ۳ ساعت تا شروع جام جهانی؛
درب‌های ورزشگاه تاریخی آزتکا مکزیکوسیتی برای ورود هواداران باز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127187" target="_blank">📅 20:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127186">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diwBEviIhUUwk9ZqjCSzLXb87-HdMnRLQPgPn84zpBwzfUDpBzYp3CO1fBt2bGdkYH5mb_q6AGARbo-J2ef16kSwLwHYKt72gZX9RQRlPuN6WmtqdDzNxJxgJod138R6EgdEe4uBHrxsZ8hGb4PRWm1w0Js8LXC5ptm3N5vI50QW7iLiFD3yfwpdohKLj8AUdz97e-3CEqHfpAr810SpRscZ4-dfbo3bPkVXg6Fyw6fUNV9uGd272H27IFxop28bRqVY0IMwBV7mhQFaGm0XxFd7y-ojS_HI_IqBqvfv2DhZF-yQ6_Sr_TIXuayf_in1cq95vIUdq9D9dtZ7SEHAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران تو گروهش در جام جهانی دوم بشه و آمریکا هم دوم بشه در مرحله یک شانزدهم نهایی جام جهانی باید باهم تقابل داشته باشن
🔴
و بدین شکل ایران و آمریکا در 3 تورنمنت متفاوت با یکدیگر رقابت خواهند داشت :
🔴
جنگ ایران و آمریکا؛ هرشب ساعت 12 شب به بعد؛ از جنوب ایران
🔴
والیبال ایران و آمریکا پنجشنبه 4 تیر
🔴
فوتبال ایران و آمریکا: جمعه 12 تیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127186" target="_blank">📅 20:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127185">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سخنگوی سپاه: اگر آمریکا می‌خواهد شکست‌های قبلی خود را دوباره تجربه کند، پشیمان خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127185" target="_blank">📅 19:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127184">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw5fJk2XGnd-pZ3FRBSD33yoec6P-l44iutK0ERpwwAKac9vGMi13O7Q3GtDUcIkaCvRFhUfyAxJqBAzrYYHym-0sDieTK0V8gZ1Vw7BMYk4bcYHZa_1oqYjxaGY7gU0S4K_ZgT2UXefk3KNS3olXjigprwdZ-Sfd9jsV-4lrhR4DgWi-_H3Fyo60GDMrbeP33qbO9p2UGpdq4i8oHMbpV66rOVTVXacSLaPWdwNoUBRcv9I4t870_5_Xr9X8kRlnMN8lUlzYFa3zNqUQr1qLvqgn0ax1Sv8EggNyx_YZ713w2mhNdoAgMh704ewcf2Fk6Llyvi8zMnuPYoQIqBMyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام:
تنگه هرمز همچنان برای عبور و مرور باز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127184" target="_blank">📅 19:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127183">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مدیرکل مدیریت بحران استانداری آذربایجان شرقی: حادثه خروج قطار خاوران از ریل در ایستگاه ترکمانچای رخ داده است.
🔴
این قطار از تبریز به سمت تهران در حال حرکت بود و در این حادثه  یک نفر مصدوم گزارش شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127183" target="_blank">📅 19:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127182">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38adcb12ff.mp4?token=Rt0u1OcfaVLkHohvJOjdeAd12hzDjcbaqACfhs5Kf87oRYJuDodFUjvdu-ZVC77eWaKo1jTyOoj5y1StbB_oBGvyoYAJpgqxkRoECTfu_pscWPDQ1d9lMMABV3fwElubqKC8KqjzEINuBKErIQjUsoc_AY0bNoels82uufyYr9RPjhPoYbhgxKnCHVzIgd-zLzqjXYeS02Egy9GuoN-RBk2xq13T3dTZm-oYXD0dlNpaJY_4xaCnKkfnE3pd4E1i0qq68ESNzQQMYc4i_UiX5bWNkBRnKSEu2Fb6gxAJZrpoTgcEaXssND767u-WsJ1pLu8PBylW1o2VM3JxJYfFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38adcb12ff.mp4?token=Rt0u1OcfaVLkHohvJOjdeAd12hzDjcbaqACfhs5Kf87oRYJuDodFUjvdu-ZVC77eWaKo1jTyOoj5y1StbB_oBGvyoYAJpgqxkRoECTfu_pscWPDQ1d9lMMABV3fwElubqKC8KqjzEINuBKErIQjUsoc_AY0bNoels82uufyYr9RPjhPoYbhgxKnCHVzIgd-zLzqjXYeS02Egy9GuoN-RBk2xq13T3dTZm-oYXD0dlNpaJY_4xaCnKkfnE3pd4E1i0qq68ESNzQQMYc4i_UiX5bWNkBRnKSEu2Fb6gxAJZrpoTgcEaXssND767u-WsJ1pLu8PBylW1o2VM3JxJYfFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پنتاگون در وضعیت قرنطینه؛ تیم‌های هازمت برای حادثه مواد خطرناک وارد شدند
🔴
پنتاگون ساعاتی قبل به دلیل «حادثه مواد خطرناک» در قرنطینه قرار گرفته و تیم‌های اضطراری هازمت (مواد خطرناک) برای بررسی وارد ساختمان شده‌اند.
🔴
طبق اعلام آژانس آتش‌نشانی و خدمات اضطراری شهرستان آرلینگتون، واحدهای این آژانس از جمله تیم مواد خطرناک، در حمایت از تیم هازمت PFPA (پلیس پنتاگون) در محل حادثه حضور دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127182" target="_blank">📅 19:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127181">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
اورژانس تهران: آتش‌سوزی در یک واحد مسکونی که محل نگهداری بنزین بود
🔴
در این حادثه یک تن جان باخت و پنج نفر به مراکز درمانی انتقال یافتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127181" target="_blank">📅 19:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127180">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/872df98e52.mp4?token=iqVfsIpUAuvm2STVVL2s5rEvTm4r9cZTY6wBkYR2M7u3iSJbEP7Bat8ideIua35mgLqA_obsG2qwsRl7dsMo57rneutuxyUHOWSOoBjpMKd_z1CXlD3TmGikrJ42k3TIZwe91ENXfdsREg2V4GbMmqNHaqrSpskKzYJyAxEMc0YQWLUuiY35c-cqwKKG7XOY0tfcIK8XpsOSrxfZ6YP8BMUGWOsHrSPn0QQkOJKSiHzLiRvCo12j_eD402w86uKEWgjCI1TrbHrbX-8htbgd7uHIE5V6X-YJeLJHGkJKLnurrNe6CyfTdICWJiuf39DAohJTGjDCoG3MLYghcVYymQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/872df98e52.mp4?token=iqVfsIpUAuvm2STVVL2s5rEvTm4r9cZTY6wBkYR2M7u3iSJbEP7Bat8ideIua35mgLqA_obsG2qwsRl7dsMo57rneutuxyUHOWSOoBjpMKd_z1CXlD3TmGikrJ42k3TIZwe91ENXfdsREg2V4GbMmqNHaqrSpskKzYJyAxEMc0YQWLUuiY35c-cqwKKG7XOY0tfcIK8XpsOSrxfZ6YP8BMUGWOsHrSPn0QQkOJKSiHzLiRvCo12j_eD402w86uKEWgjCI1TrbHrbX-8htbgd7uHIE5V6X-YJeLJHGkJKLnurrNe6CyfTdICWJiuf39DAohJTGjDCoG3MLYghcVYymQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد یک پهپاد انتحاری سپاه در منطقه‌ای در اربیل کردستان عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127180" target="_blank">📅 19:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127179">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ng2TKwwUzb8wrZUQPoeVdRdJUc-8sbkbLBwjaokm5T4SspLKeYGsrjqVeQD-FN8GVLsJQQnpoSMoNyK8_Jeqi3dB7JLZ2Jc2h7FTxJzkdiPe12jsxT1rxJsE63iEomq-Ld4LZqGdz35H875bRYLRYy2mj9p8fUfG_HAeTrTwsgyCfaDito9vi6L1NW96tYrpKBbzm1EUB92fDFvAuQ2CQ7yHtSeW7xq8fSe0YVP4n81gTj5bR9LApuUvC3zuNaFMC7gADDtyq7xUZMWmm-oqRpQ4T2g8bxsd6iJD1ELUv0Qamkim2Kd_yFwwuFTsVSOv5DSZVkYylZQaa2SrmaqkVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:
استراتژی‌های اشتباه و تصمیمات بدون فکر، صحنه بازی را به شکلی فاجعه‌بار به نقطه صفر برمی‌گرداند
؛ زیرساخت‌های انرژی و بازارها را به انفجار می‌کشاند و مردابی بی‌پایان پدید می‌آورد که سال‌ها در آن گرفتار خواهید شد.
ایرانی متفاوت خواهید دید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127179" target="_blank">📅 19:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127177">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔥
هنوزم ۱۰۰ و ۲۰۰ گیگ رو به اسم نامحدود میفروشن؟!
🚀
مخصوص جنگ
😎
💙
5 سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی   وصل بمون
😎
✅
بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/127177" target="_blank">📅 19:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127176">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R4skCh34XVhLNKMlxEXu_RRsb2qu9g8WZX0otpxUxhbAylbhPF0YqQwT4tV-uFFxMi28mQgvytUrN1HYDfI6SGIOe5YDupYi81lDVgvQ8FePobONzjDCRyBa5MMrMduEGj2LIGnSxCePpC2lVl6ZxyO0ni3xBny5ZzfcTnWfJuUQw0oU1-UQSBsamSVCVhHumbeEy93GzEzWUKAcHJiA8VgsR7rybmxmkq66DeWcrdv25usFgEjkwd3pcNzptqmitei5553VJ0b8uxWBFzZI_MgNZXiVojPO2bPYkG0YycjFACxOzUvWkzRp2C-fMhga-ot1Bb2VYo8RvAA2OhVatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
هنوزم ۱۰۰ و ۲۰۰ گیگ رو به اسم نامحدود میفروشن؟!
🚀
مخصوص جنگ
😎
💙
5
سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی
وصل بمون
😎
✅
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/127176" target="_blank">📅 19:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127175">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdd68900e.mp4?token=RpJL9s0c4vrPxpuCBARGabCd2r0FP5qGlijNGvDRiTTeOIDuntQVHDM8pR-Cyc2bsmyDxue_UfUzqfKaUx1wvfmClI6ni90f0kw_QrNrLDVub6c4IU3nQhbccP6J1oYfx--N2RM9ALq5heMDk8ogZjcbdm6skNVOHIYqR1xFbuHOftSODeW7SokMh4fJGrTGE1LxHC3wp3a4XIPImFhxhsEZzz1yO40HKL244V8krzp3T9b09CyChMfU0R7phrofgYGXSy_n3-3Qi-plkYrH1Dphlkz5qygVlNUsGku4uyMKWLY0UoRYLmm4uhhnqQGv5yNz_CDkg0m5NdWUYe-1fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdd68900e.mp4?token=RpJL9s0c4vrPxpuCBARGabCd2r0FP5qGlijNGvDRiTTeOIDuntQVHDM8pR-Cyc2bsmyDxue_UfUzqfKaUx1wvfmClI6ni90f0kw_QrNrLDVub6c4IU3nQhbccP6J1oYfx--N2RM9ALq5heMDk8ogZjcbdm6skNVOHIYqR1xFbuHOftSODeW7SokMh4fJGrTGE1LxHC3wp3a4XIPImFhxhsEZzz1yO40HKL244V8krzp3T9b09CyChMfU0R7phrofgYGXSy_n3-3Qi-plkYrH1Dphlkz5qygVlNUsGku4uyMKWLY0UoRYLmm4uhhnqQGv5yNz_CDkg0m5NdWUYe-1fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون ، طوفان و رعد و برق در تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127175" target="_blank">📅 19:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127174">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
هلال احمر: امشب در آماده باش کامل هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127174" target="_blank">📅 19:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
الحدث: ترکیه، مصر، پاکستان، عربستان سعودی و قطر قراره جلسه‌ای فوری برای جلوگیری از شعله‌ور شدن جنگ میان ایران و آمریکا و پیدا کردن راهی برای توافق بین این دو کشور، تشکیل بدن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127173" target="_blank">📅 19:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmf2G_3nVDSlJBYwf-Nh3hSyJwBp3_a_CohLhHfcfnaxYy6Uj-p1d16bxHecoY_owwCD4GUZKRWmv65Rwie48PaejxM2z7LnXBYsHGPY7j8CGaLw090eY7YMOD4iSLRf5wxNa2UCMwL-HEBVCrPv-Vc92gz4olG3quZdlTE0OATyWG8fPHMjABV6_nCZHn5YEZTPpAIpMrtGrE-0xbgscraSWv3JYlkme_EIc1nXwP3SQjodxWPvdJ-Wo64N-VqIXh59L_y8-joQxW9ZlgX11Rgb9jClG0t29ungYYWkQRNWJP_8waRlIblYk7FGAUHW6Zmds_phsv9K8JgjR_UdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127172" target="_blank">📅 18:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری/ سی ان ان: پنتاگون در وضعیت قفل (لاک‌داون) قرار گرفته، یگان‌های مقابله با مواد خطرناک و بمب گذاری (هزمت) در محل حادثه حاضر شده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127171" target="_blank">📅 18:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127170">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
منابع الحدث: نشست قریب‌الوقوع کشورهای میانجی‌گر واشنگتن و تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127170" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127169">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e13_gUsXieEI2g55PHJuylPMe-NN5OSbHuz_A56_4Iy7ZrPC7ZcsF9TgjybcKF_aacr4uZ4yGk857bMgqAIXHnMg52jFdZn9PDtSLsn9bAM142zl2a28qts6d3ODC8wApry9u295Nf95LPfLxtCDWJ-qWfIW54BSIKxx7X2-4SGcGoKsHNFq1CUTqnJH3IW7slh81Q4zi3P45m_5RqnvrBAs8HhL-Rlq8V92mBjN58DdS5N2EtQA1LL-GX7HhUiddGQ0ef6Od_fn1ztUEP3cAe3PXlkLeU-NUIMBvc4lQ4WLu-iSMaT67TsHwqqxlBSQcyUc18HnEEm8tuBJSYRzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌ داری آمریکا: هر آسیبی که به متحدان ما در خلیج فارس وارد کند، با وجوهی که از حساب‌ های ایرانی برداشت می‌شود، جبران خواهد شد!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127169" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127167">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری/ سی ان ان: پنتاگون در وضعیت قفل (لاک‌داون) قرار گرفته، یگان‌های مقابله با مواد خطرناک و بمب گذاری (هزمت) در محل حادثه حاضر شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127167" target="_blank">📅 18:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127166">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی در حمله‌ای جدید، شهرک «مجدل زون» واقع در شهرستان صور در جنوب لبنان را هدف قرار دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127166" target="_blank">📅 18:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127165">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
منابع عراقی از اصابت دو پهپاد انتحاری شاهد ۱۳۶ به یک انبار گروه‌های تجزیه‌طلب در منطقه «قوش تپه» واقع در شمال اربیل خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127165" target="_blank">📅 18:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127164">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGAPyN1MxuC-lHf57R9PqHSf8kWkt0d2IECY5lRUognL3Z2Yahom66B6mlLlC-9-dDItaPxcXk_XOFUgJaXepMdoYDmi1k3uHX-zG7EEzJrsfKwWuxjQV6SMh74UD59GFj1RNDpocsUyLU8bl4kFRG-0gAW8_dcns95SD8CRy0844RHiVRVsGA32H3sgjuCavuD9gBXNJZwnwT_O0Gs0ppQnJsTz1cdy_vj7bp18rrxWmrzj0OA-rwNk4WT-Y9OuDayA4Eg31X-Kr8gVAh4M9VFgvlpmXhJomNHvRQFwHKWNu-9mm62UY8lGUqIL7jfLOi63HOvZG10ZWx7ggd8zaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی عجیب در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/127164" target="_blank">📅 18:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127163">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پزشکیان: باید از وضعیت نه جنگ نه صلح خارج شویم اما مگر در خواب، تسلیم شدن ما را ببینند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127163" target="_blank">📅 18:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127162">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
بلومبرگ: امارات و ایران اولین دیدار امنیتی رو در رو در سطح بالا را از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران برگزار کرده‌اند.
🔴
این اقدام نشانه‌ای از حرکت به سمت کاهش تنش‌ها پس از ماه‌ها درگیری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127162" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127161">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد از ابتدای ماه مارس گذشته، 30 نظامی اسرائیلی (افسر و نظامی) کشته شده‌اند و همچنین 1302 نفر نیز زخمی شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127161" target="_blank">📅 18:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127160">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / خبرگزاری فارس : ایران داره بررسی می‌کنه که دارایی‌ها و کسب‌وکارهای مرتبط با ایلان ماسک تو خاورمیانه؛
🔴
از جمله تجهیزات استارلینک و سرمایه‌گذاری‌های مرتبط با اسپیس‌ایکس، رو به فهرست اهداف نظامی خودش اضافه کنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/127160" target="_blank">📅 18:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127159">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
گزارش CNN: ایران در حالی که ارتش این کشور در حال انتقال محموله‌های موشکی است، سامانه‌های پدافند هوایی خود را در جزیره خارک نوسازی کرده است.
🔴
ایران همچنین در امتداد خط ساحلی جزیره خارک مین‌گذاری انجام داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127159" target="_blank">📅 17:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127158">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید تسلیم موشک‌های جمهوری اسلامی شود یا دیپلمات‌هایش...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127158" target="_blank">📅 17:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127157">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سی‌ان‌ان: مقامات ارشد ترامپ تصرف جزیره خارگ را به عنوان گزینه «بازی نهایی» دیده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127157" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127156">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آکسیوس: تهدید مجدد ترامپ به بمباران ایران با هدف اعمال فشار بر این کشور برای نشان دادن انعطاف‌پذیری بیشتر در مذاکرات بر سر برنامه هسته‌ای‌اش است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127156" target="_blank">📅 17:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127155">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
جوزف عون در مصاحبه با رویترز : آینده لبنان در دست مردم لبنان است، نه در دست ایران یا اسرائیل.
🔴
ما نمی‌پذیریم که ایران به ما دیکته کند چه کار کنیم. ما یک کشور مستقل هستیم و ایران حق ندارد از طرف ما صحبت کند.
🔴
ما نمی‌پذیریم که لبنان به عرصه جنگ دیگران تبدیل شود و مصمم هستیم که مسیر دیپلماتیک را دنبال کنیم؛ هیچ راه حل نظامی وجود ندارد.
🔴
ما چاره‌ای جز مذاکره برای پایان دادن به این درگیری نداریم، و اسرائیلی‌ها هم همینطور.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127155" target="_blank">📅 17:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127154">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHYSBYyWizFPg8wk2bTTcLUoNHPU0tKT5x2dbRC1RqyeBmADJcDnDIrbr7iFX5HEPL0SCxtKeozSx23eCIIGr_Gd5HgvY8FVuGeW4M1hXQ4X2kmX8DD4948aYCjBaE2rQukNS5GrukT3j4n7o78hteEbmdJcVo9OXWaW8wsK27UPuE0-8c0hfHu2btaZDraU-JteuXVK-TbPOK9fs_Z_CBw7lJGf02ZhhsWZwhs3fQsp2G9fC4OZVCcQgR7mcMR_ZvTNrnXgRBErDRRrUn9qJOs8hOtWBi5CG8P9kAlfstrDVsPd9ZJYTSv8yv0My0kK1pZ_Lp3wstW6crLxDMoelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران ماه‌هاست که برای یک عملیات احتمالی آمریکا با هدف کنترل جزیره خارگ آماده می‌شود، گزارش سی‌ان‌ان.
🔴
ایران پس از حملات نظامی قبلی آمریکا، دفاع‌های جزیره را تقویت کرده است، از جمله استقرار نیروی انسانی بیشتر، سامانه‌های دفاع هوایی و موشک‌های شانه‌پرتاب (MANPADS).
🔴
ایران همچنین مین‌های ضد نفر و ضد زره، از جمله در امتداد خط ساحلی، برای مقابله با عملیات احتمالی فرود قرار داده است.
🔴
مقامات و کارشناسان نظامی آمریکا پیش‌تر هشدار داده‌اند که هر عملیاتی با هدف تصرف جزیره، خطرات قابل توجهی از جمله تلفات سنگین احتمالی آمریکا به همراه خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127154" target="_blank">📅 17:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127153">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
حزب‌الله : یه پهپاد هیرون اسرائیل تو بقاع سرنگون کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127153" target="_blank">📅 17:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127152">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b01cb957f5.mp4?token=S42upN4ZU6QchT7DB02R7g7RclhuLewpkYD9zHPLcHO4Of7f0R8cuikwGaAQZITJRIk7hvuo5TTv_i9k7SyG8Fdd6fTLXC5SNAMRhXgV8l7X1nDlptvWsm1Zg25Nz87ZXR6ZLqtOZb7tF9tkOHL8akmDjHwRSfZKeMM9xJ5Dn4uifkvtKdn5rPOdtu3bCScMICN5yscO6ZqGV5zSH-CSF9M3c8eUQ5WQO7vTsTndg9RNLUE-2lOXnGpsLcWalG6vyuUWdgWfKMQhcio0iWYpC7uO9PM7CdC8n3JM75XiCcywgzTBE5ePBbHglWdkypm_HTLZb4sNIeW40mCtcYvSWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b01cb957f5.mp4?token=S42upN4ZU6QchT7DB02R7g7RclhuLewpkYD9zHPLcHO4Of7f0R8cuikwGaAQZITJRIk7hvuo5TTv_i9k7SyG8Fdd6fTLXC5SNAMRhXgV8l7X1nDlptvWsm1Zg25Nz87ZXR6ZLqtOZb7tF9tkOHL8akmDjHwRSfZKeMM9xJ5Dn4uifkvtKdn5rPOdtu3bCScMICN5yscO6ZqGV5zSH-CSF9M3c8eUQ5WQO7vTsTndg9RNLUE-2lOXnGpsLcWalG6vyuUWdgWfKMQhcio0iWYpC7uO9PM7CdC8n3JM75XiCcywgzTBE5ePBbHglWdkypm_HTLZb4sNIeW40mCtcYvSWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان:
اسرائیل تحت مدیریت فعلی خود به کارخانه‌ای از تفرقه تبدیل شده است که تنها مواد اولیه آن خون و اشک است و چیزی جز بی‌ثباتی و هرج‌ومرج تولید نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127152" target="_blank">📅 17:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127151">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در استان اربیل در شمال عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127151" target="_blank">📅 17:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127150">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP-tgSjnYwS0nd8sG5DMcDo8rstdXgveXAKpbeawqDP5sQBgFZ4rhlGjg4tyCJ4wuXMV_v1OLDdAQmtBWQ3r7qXb7_goFgOkKVl244iEEz94BiLDS-B2e62tDBBPtTuV5vf3kCbxDccBX4_UJDh20T4J5ucucD18j_mFtn6uHDXRYl0A7FlJliOIBDTf4B9KQBRpQckx2F4mfIOA3i_kr7_oA3HSSiZfTAaX5jbCTQzo3m4ydC-8HfjifTMh6C4Go7rrX6neNzRPtGQEG5jbwbJWC6ONler--cpMySe-ZlS8Z9yNpcUpVzrRDo6cBaSv9uRO_g0rJMPVcjEU_Fek7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلویزیون سوریه: احمد الشرع، رئیس جمهور سوریه سه روز دیگه تو کاخ سفید با ترامپ دیدار میکنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127150" target="_blank">📅 17:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وال استریت ژورنال: از این به بعد آمریکا «هر شب» به ایران حملهِ میکنه، تا زمانی که به توافق برسن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127149" target="_blank">📅 17:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6599e2d096.mp4?token=IKblTu6tzTIuVJMeNrtQ2DmedQ75htSfPhBrYK94vi8AU4T_2g-cZIUK1ue3KCpuaQZJLR_br5O9egIJQKeJTqzWXoPSFK19BXny0Xcv--gHtFHNuigkFLxhZkL8vY-RRX4Vn1z9GYkQorSX0W1uwNGcTl6JeWnKGoILO6z4MN5Rhrk24vy8qABCzf4bqCfJvn63RBFeVTioq3GxqR_zSpp34IWT9HB6Sq3FOjpIGNtXvlNRNbB-eVBd8w3OKXEjck62LnFTHORltTAZmT_6GI-JlYfJiTcuvyzn13wVjDZ5X2v436b41cCjr5_igreSLcTwaJNiDsgMX45LBUvAfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6599e2d096.mp4?token=IKblTu6tzTIuVJMeNrtQ2DmedQ75htSfPhBrYK94vi8AU4T_2g-cZIUK1ue3KCpuaQZJLR_br5O9egIJQKeJTqzWXoPSFK19BXny0Xcv--gHtFHNuigkFLxhZkL8vY-RRX4Vn1z9GYkQorSX0W1uwNGcTl6JeWnKGoILO6z4MN5Rhrk24vy8qABCzf4bqCfJvn63RBFeVTioq3GxqR_zSpp34IWT9HB6Sq3FOjpIGNtXvlNRNbB-eVBd8w3OKXEjck62LnFTHORltTAZmT_6GI-JlYfJiTcuvyzn13wVjDZ5X2v436b41cCjr5_igreSLcTwaJNiDsgMX45LBUvAfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کرد ها
: ما واقعاً برای معترضان ایران سلاح فرستادیم و صادقانه بگویم از کردها خیلی ناامید شدیم. کردها ما را ناامید کردند.
من با این تصمیم موافق نبودم. می‌گفتم: “نه، فکر نمی‌کنم آن‌ها این سلاح‌ها را تحویل بدهند.”
فکر می‌کنم آن‌ها سلاح‌ها را برای خودشان نگه داشتند. به نظر من این یک رسوایی است. اما من این موضوع را فراموش نمی‌کنم، کردها را فراموش نمی‌کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/127148" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزیر خزانه‌ داری آمریکا:
هر آسیبی که به متحدان ما در خلیج فارس وارد کند، با وجوهی که از حساب‌ های ایرانی برداشت می‌شود، جبران خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/127147" target="_blank">📅 16:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127146">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: پل‌ها هدف بعدی حملات ما هستند
🔴
ما برای معترضان ایرانی سلاح فرستادیم، اما از کردها بسیار ناامید شدیم زیرا آنها سلاح ها را به معترضان تحویل ندادند.
🔴
مسئله ایران تمام شده است و ما می‌توانیم فردا نیروهایمان را بیاوریم، اما نمی‌خواهم نیروی زمینی اعزام کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127146" target="_blank">📅 16:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127145">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:
ما در حال مذاکره با ایران هستیم
🔴
ترجیح می‌دهم جزیره خارک را در اختیار داشته باشم
🔴
ما هنوز به اندازه کافی به ایران ضربه نزده‌ایم
🔴
من از ایران ناامید نیستم، این توافق خوب است و ممکن است بزرگترین توافق تاریخ باشد
🔴
هواپیماهای ما بر فراز قلب تهران پرواز می‌کنند
🔴
ایران در تبلیغات خوب است اما در جنگیدن خوب نیست
🔴
اگر ایران توافق را امضا نکند، آن را به شدت بمباران خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/127145" target="_blank">📅 16:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127144">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf4jOZTdP13w5ibbx2zNO3gEa17GO98xXzc0iAtTmKyC6Kh_-DBS0ZOUpQIptdB-BcbT9zRBedWnPzF0d0KVjDZmUj3vtSyGcbMNvBP0fBJH-qHknsYgP5kWGZ1wt-bb9o0Lln__bIVIj3mb5Y0cbG-O57C1Ief_qeEqbUXtyw1CT7XxTzUaZ52NtoMD5GFWioaRtp9hqLAuNBpt8ziKcYzxFFUevJa6v44SrGX96BGKMDyINCbwinqk3lfz3ZgpIFzIyrmJDtQsIsUBoMRNx5llngSXT2wqWphkSw52qvB2zwlNsQQzes75kqyqePJUykvMuPIOHgoySZg81z7uIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ونس، درباره نتانیاهو : ببین، قطعاً یه جاهایی اشتباهاتی داشته
🔴
ولی راستش بعضی از این بحث‌ها بهتره توی فضای خصوصی بمونه
🔴
چیزی که می‌خوام بگم اینه که در کل شریک خوبی بوده
- ما به همکاری ادامه می‌دیم، ولی هر جا منافع‌مون از هم جدا بشه،
🔴
آمریکا کار خودش رو بر اساس بهترین منافع کشورش جلو می‌بره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127144" target="_blank">📅 16:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127143">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epqu1YjW4Bag6qkXWfegrjcAvE7uZtTpi6t4Gan4LW51Blr_XhZc8ySI2cdixEVbZsTQWZyvKApQgELHytLaHz0HwYsspOghktM-swkksWNqQKWC29wH4pJnQIt4zYvfTBcEqaY-o6csHzKK0sb_TjxkV52vK7_mukefjGOzJvlfvhNCVrdTGpNOarwQ5WgjU0j2lCE9WwiPQKXTusrel9vTA-cHoU5a2tqC4YtzZxcdh0ySjD_YCWmMf7rYvXNhTuX9MhZFoqq6Nu-dew2l_YODu8noVd20qVMW4EqASWqT1eOLazUluvbeDdmZwO7TEgdfRCug4CElgUy8HpThVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اصابت پهپاد انتحاری ایران به رادار هشدار زود هنگام آمریکا در جبل الدخان بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127143" target="_blank">📅 16:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127142">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb295fdb6.mp4?token=ScX4uHeGwz7qnH_o-lxtHCUV0EIbOePo64k10z4a1dAMNlNMgig_rKr-N15kBnPtPAIgT41i3nfWBDzZuZccQmKBrd-ZnmUjc_kRuzHo1ZWmTUaGgq6N0nZPro2vBMTHnPTen2TLW8QS9U0TbLHMats5MEDPvLndEnJQYINRc43B5F6o3jCdrYzRRTbtpSl4p-Ix5BYlLpgFY3T72AA4qvxfSLGGwvdn7t4lDCTx6rxVD8EC4ORzXh6rUjRuLbXRitTeRLudhgNpa3A1czSWZ8KLiCZDFzrpSXLcefjY3_R7ooRkOQ6KdCRxj6840S6T_8iSSNhTSf6zv6ULS21HLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb295fdb6.mp4?token=ScX4uHeGwz7qnH_o-lxtHCUV0EIbOePo64k10z4a1dAMNlNMgig_rKr-N15kBnPtPAIgT41i3nfWBDzZuZccQmKBrd-ZnmUjc_kRuzHo1ZWmTUaGgq6N0nZPro2vBMTHnPTen2TLW8QS9U0TbLHMats5MEDPvLndEnJQYINRc43B5F6o3jCdrYzRRTbtpSl4p-Ix5BYlLpgFY3T72AA4qvxfSLGGwvdn7t4lDCTx6rxVD8EC4ORzXh6rUjRuLbXRitTeRLudhgNpa3A1czSWZ8KLiCZDFzrpSXLcefjY3_R7ooRkOQ6KdCRxj6840S6T_8iSSNhTSf6zv6ULS21HLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ویدیو رسمی فیفا برای شروع جام جهانی با نورپردازی خوشگل
☺️
😍
@AloSport</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127142" target="_blank">📅 16:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127141">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">😳
هنوزم ۱۰۰ و ۲۰۰ گیگ رو به اسم نامحدود میفروشن؟!
🚀
مخصوص جنگ
😎
@NetAazaad1Bot @NetAazaad1Bot اینجا از اون خبرا نیست
😎
⚡️
💎
نامحدود واقعی، بدون استرس تموم شدن حجم
✅
مخصوص این روزایی که اینترنت پایدار از نون شب واجب‌تره
❤️
🚀
فقط امشب با خیال راحت وصل شو و…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/127141" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127140">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K_kUEqOcQVh9XUdKNxeZnd0v1mQVFTcZvRuXM_W-7q_JycP0lYc6KlKjmt6yLtwgUpNEBPLAEsGNpesoJGOERPl2sfQ_tEHwZZIQxCacWLlpdtfAT_xB1R5M8uHtuUJAJX5O6CRlkzYhfOj7FbNNnK8dk7CJsrph_xWsXy0EgbEW9EI4Z5X5R_YtY9VXsq0XMpsSeFYadnB0iyOoYtQTSaMcESlmXkIkX7g3fsndzNubxhZaGw0vOaILX40IYDkYnen6lV3bqma57XCbBpC49VUg0tp-OZ_gEFrHpZQqtr8hH2MvFxnFMiI5bIvelcvK3u5qigwTf4Rxmvs2SnXxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
هنوزم ۱۰۰ و ۲۰۰ گیگ رو به اسم نامحدود میفروشن؟!
🚀
مخصوص جنگ
😎
@NetAazaad1Bot
@NetAazaad1Bot
اینجا از اون خبرا نیست
😎
⚡️
💎
نامحدود واقعی، بدون استرس تموم شدن حجم
✅
مخصوص این روزایی که اینترنت پایدار از نون شب واجب‌تره
❤️
🚀
فقط امشب با خیال راحت وصل شو و لذت ببر
⌛
ظرفیت هم محدوده، جا نمونی.
✅
@NetAazaad1Bot
@NetAazaad1Bot</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/127140" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127139">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر خارجه بحرین می گوید صبح امروز 36 فروند پهپاد ایرانی را منهدم کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127139" target="_blank">📅 16:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭕️
الونیوز فقط در تلگرام
💬
و توییتر
❌
فعال هستش
🔴
سایر شبکه های اجتماعی چه داخلی چه خارجی که با نام الونیوز فعالیت می‌کنند مرتبط به ما نیست و پیشنهاد میکنم که لفت بدید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127138" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0kH1Y9TddHrF-z9whG0QUT5UXgbqktOdWFWe6s_3uW_qxrxolfL0h_9tYrlEWFFFLkv72rxHUkHWkY7fwO-KVTzgR7ITz2T6SoBc9E1vzR8FDCD0-5LTWOmMHRdOc0NSSuhpmiSzsv5qIyCBT066kk0KVJRMYnJ4gavG6ah6dYWra84tfeT9dcrDLWxvMb62U1bmYJDvZsXzE6KkNYjXPA38qL6jcpASuDTBxzJjHVqcCeuTrx5NM_u4w_fQIu-OhBHB050auva9dGTcSEztUayo-5AS01LMYVz-XEnL6QCRU4QFZ6VXI_M8uqEOJtm9MGBHRWZAbY9gqWvZQMFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووری/ترامپ:
ایالات متحده امشب به ایران ضربه‌ای بسیار سخت خواهد زد (ناوگان دریایی، نیروی هوایی، رادار، ضد هوایی و تمام اشکال دیگر دفاعی آن، همراه با بیشتر توان تهاجمی‌اش، از بین رفته‌اند!)
در آینده‌ای نه چندان دور، ما جزیره خارک و دیگر نقاط زیرساخت نفتی را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم گرفت، درست مانند کاری که با ونزوئلا انجام داده‌ایم، که برای هر دو کشور ونزوئلا و ایالات متحده آمریکا بسیار موفقیت‌آمیز بوده است. از توجه شما به این موضوع سپاسگزاریم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127137" target="_blank">📅 15:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127136">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJDY1SzRai6WRzSiT8G9tqmJD8QJ1j-POiTmC_5KEMzQOCDJfXtU_8OS0zGi7NXG_vuV1AEuBu8yhnvtdG0pLJhrOLuclgAUwlahLIKNQmFkGJb4c1CnsKTekLQmY7ssbyUHYU7uX5dq_xd_L-l3bJaalSj60QlMpikRE8IkjY62i_Oqjvsbj6YKMHEleEJxKe6E_CST1oouNK6alPKKaIN45pH8lFGEjNC4F7RXLZORei79DmT4KvL5ZpZD5PnfwxKkVNq_Y-lzTpKfVdQPwZiR9pvN1aLIMEQc44CCkUqpFYvdZi7MxH-sQ-oLNVbTAK8jewS0pi6-7bJSaCdPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری معتبر فارس:
ادعای سی‌ان‌ان درباره مذاکرات جدید ایران و آمریکا تکذیب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127136" target="_blank">📅 15:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127134">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lvBkUwMQkAh8aqTfgDH-narFDEmFWZls1PVyLyqRrxAb-FASsg50_eMYSxKpsa6dXdO9fiB8SB6Wd6Uv1RrvMzCkVXqaMalxgYkzuSCatcWisz9W5Z8ajRRTYINTu4JJN-w76X-KJsCsz9yb99wgiZRKF-BSoWxLp_vhC63c3CMP_z-1YGHOx4wg4k4DepV4BUAS1zqM2o3x7k5FNIfIBtyfucB45Os21YpTrTRvusmibqEG6SrjYXbx992VRyGJjgU6ELEpO4EainItX0ZLvq8qcU8njC7A2mlleXbvx7ZL7N_8m1_hUJssO1ChSiCOuBIuuiEs9IMCJf_zANOywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gbAnHL5aFcpKLP4KxDXOE_pIOSnFJUupo8_AiPvwhdZ5CCzslP6W8v5lbYS2LB3KfK8KC2ZDd9ZdeaaDod7TvQkIL-EehMMiAThNVnGRN2hDnJ7IS1AY6RAFXt01St-Y7Wb2DvRDe0ACsblEZVwUWdQ8DjuwnPwchoKli0ll5GfTUPO_UK6SYTcemiqZ6stByBKUkIwbvHIekVCAl1VS3hFVg5Lu2p-EdfLUsobdEV6IJGlCLqKVOfgziVc2-HZvhLxx9Wux-EKvwuVGVZSXnEwWBt8gSqCKz3VL6R0PighXvLJctf_EZq-LkAhIAnxsELEio59hVwqK35iDuGlz8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دو آتش سوزی در نقاط مختلف پایگاه هوایی شیخ عیسی بحرین بعد از دو راند اصابت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/127134" target="_blank">📅 15:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127133">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
العربیه:
پاکستان و قطر در ساعات گذشته تلاش‌های خود را برای پیشبرد یک توافق افزایش داده‌اند و این منبع گزارش‌های مربوط به عقب‌نشینی‌ها در مذاکرات را نادرست دانسته است.
🔴
منابع ارشد همچنین تأیید کردند که ایران پاسخ خود را به پیامی که وزیر کشور پاکستان، محسن نقوی، تحویل داده بود، ارائه کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127133" target="_blank">📅 15:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127132">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
کویت: رفتار ایران نشان داده سازمان یافته حمله می‌کند و ما مجبوریم پاسخ ایران را بدهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127132" target="_blank">📅 15:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127131">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جی‌دی ونس درباره نتانیاهو: نتانیاهو کشوری را اداره می‌کند که آشکارا شریک بسیار نزدیکی برای ایالات متحده بوده است.
🔴
اما حتی زمانی که شریک نزدیک بوده‌ایم، گاهی منافع ما کاملاً همسو بوده و گاهی منافع ما ناسازگار بوده است.
🔴
نتانیاهو به شدت منافع کشورش را مطرح می‌کند. گاهی این به معنای هم‌راستایی ماست و گاهی به معنای عدم هم‌راستایی است.
🔴
آنها در بسیاری از جنبه‌ها شریک خوبی بوده‌اند، اما ما همچنین باید بر آنچه به نفع آمریکا است تمرکز کنیم. و جایی که این منافع متفاوت است، متأسفانه برای اسرائیلی‌ها، ما باید طرف مردم آمریکا را انتخاب کنیم، که همیشه این کار را انجام می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127131" target="_blank">📅 15:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127130">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
یک منبع دیپلماتیک عالی‌رتبه به الحدث:
ایران پاسخ خود را دربارهٔ پیامی که وزیر کشور پاکستان تحویل داده بود، ارائه کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127130" target="_blank">📅 15:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127129">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be3c800123.mp4?token=f8XK-urS6MfhQxQsTEh7kjwQLpJu_j44pOc84DO80rYxL0eslp9KfrWxdWHeN_S0kguk3tloGue8Ukj3jufOxRUMawBslcAENFuQE1Kp5TQ0w9uMXlqHb91NwaNS32gMERM2i_ErjAq1JZEJBWHFR5xbWj_O-NZQmnZm-bV9A4ay5LmzLI0MSBOSam4knXkg7ZzvMEvX4XmYsOwa6qAjuyOLhc56scT3MntGUP1Mwdj8mcoOrmBL0ZAorVTV_iL1vfy11Q6nhk-DL-ohk86jvWQIgmOdW47h6qIKDQzmA25tmRr7Yd7MYTTQEk-rHDXqBES6FAuTApRySVx0v6MECoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be3c800123.mp4?token=f8XK-urS6MfhQxQsTEh7kjwQLpJu_j44pOc84DO80rYxL0eslp9KfrWxdWHeN_S0kguk3tloGue8Ukj3jufOxRUMawBslcAENFuQE1Kp5TQ0w9uMXlqHb91NwaNS32gMERM2i_ErjAq1JZEJBWHFR5xbWj_O-NZQmnZm-bV9A4ay5LmzLI0MSBOSam4knXkg7ZzvMEvX4XmYsOwa6qAjuyOLhc56scT3MntGUP1Mwdj8mcoOrmBL0ZAorVTV_iL1vfy11Q6nhk-DL-ohk86jvWQIgmOdW47h6qIKDQzmA25tmRr7Yd7MYTTQEk-rHDXqBES6FAuTApRySVx0v6MECoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام:
نیروهای آمریکایی یک نفتکش را در خلیج عمان در ساعت ۱۱:۲۰ شب به وقت شرقی در ۱۰ ژوئن غیرفعال کردند، پس از آنکه این کشتی با تلاش برای حمل نفت ایران، تحریم علیه ایران را نقض کرد و این سومین کشتی تجاری است که این هفته توسط نیروهای آمریکایی غیرفعال شده است.
🔴
فرماندهی مرکزی ایالات متحده (centcom) علیه نفتکش m/t jalveer که پرچم گینه بیسائو را داشت و تلاش می‌کرد نفت را از ایران از طریق خلیج عمان حمل کند، اقدام کرد.
🔴
یک هواپیمای آمریکایی دو موشک هلفایر به اتاق موتور کشتی شلیک کرد پس از آنکه خدمه بارها از اطاعت دستورات نیروهای آمریکایی خودداری کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/127129" target="_blank">📅 15:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127128">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0R1AT6hZLOup7IuQKDuXUs9et6oy3uPZVNuOLK91AoGtpeoBDbqtv38KF6oUR6F301LPP6jkFtTlZ5COQWMIsHyO0J_z1Lwv0NS1SCNERZJznVSssIKHs_sUKdqS2VnfTeGGCf__09ZZs_MyMowCXakwsuGcBoo_zDJoABxz2152HaUJThSo1I2rxtCK9KBOIpWWvlXsFCEvgYk4drRf4l7ZkUzw-EdEbGIt67QeU6IRs_f7E9V2zNaKkPSbMoRNnljNrlZ_jD3EqVQME6Xou18U1-m_rve5S5ylkn2b7y291QzdJzivCljf1eK5GlBzARsHETSewdqqw56CUE48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127128" target="_blank">📅 15:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رئیس جمهور لبنان: با وجود فشارها از مذاکرات عقب‌نشینی نخواهیم کرد و تا رسیدن به آنچه به نفع ملت ماست، به این مسیر ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127127" target="_blank">📅 15:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127126">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9zcvBK1VtoiPOKLdR9qOMD_gK50jNhFhUQOgPlv-yUK-I_BB7HapwajhULjo-ffyWAwBlv9T7-1jfR1VsEyUQozl-pXRaPvqPIJhColnzKAB2q32xS8nzwSVnnAtawthtGZd1bvXdcIkUmBkOU3piSTfC1nuM9K4xwEzHrjACxoBf6PjZ_VRs-P4NTDcpmY1i_6gqCkXpffUmeqj7VbhwmY2KCgP4wU9cc_FcZystZTm6ANCIRHRfQqzyBGpuA8pRyQKDOs0zHwwVVAxWqT7o-PbqY6fTU0W4DQlT8Z7_cvZ62pL9863z0ha4VqTtG9QSSdI7S8r_q3twDLJXO_mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۲.۰۳ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127126" target="_blank">📅 14:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127125">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
خبرنگار صداوسیما: لحظاتی پیش صدای انفجار در محدوده سیریک و از سمت دریا شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127125" target="_blank">📅 14:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127124">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAT-jhJaU4affaYUEhf66tGKc-bD4fJSDUzrR8jFPVFt_BZsm1JAT2O938r3tLNkpuPy1KY2Xmlo0xj6QltLSSn6Ndd7B6uku3rRrSG_z6OQYbbFU7bVijDpQMYwOJXUoIc18cnbf1sC1merkBEQ6hvkuBI54iYGhnl3DOYaZw6ZllwOzvpkZgzyEux2JpdMlluCO_QCKze7hmD5Eacu3OTYusHHOahktjGVyr-nB6ZpKJ4y5mJkjrDYIPSaSBgwJYpStttB2TgmhjYoUMAsvF58HEDwWQwq4GA3mTbvbrz-GjMA3Ov1FQMCxes23G1VG_lElmmdGTluiH_vCcvHJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع بریتانیا، جان هیلی، استعفا داد و اعلام کرد که نخست‌وزیر کیر استارمر و وزارت خزانه‌داری منابع لازم برای دفاع را در برابر تهدیدهای فزاینده تأمین نکرده‌اند.
🔴
او در نامه استعفای خود گفته است که «طرح سرمایه‌گذاری دفاعی» پیشنهادی «به‌طور قابل توجهی ناکافی است» و هشدار داده که این موضوع می‌تواند آمادگی نیروهای مسلح بریتانیا را کاهش داده و این کشور را «کمتر امن» کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127124" target="_blank">📅 14:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127123">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
خبرنگار الجزیره: یک پهپاد اسرائیلی یک موتورسیکلت را در شهر حبوش در منطقه نبطیه در جنوب لبنان هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127123" target="_blank">📅 14:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127122">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
گفت‌وگوی وزیر خارجه ایران و مسئول سیاست خارجی اتحادیه اروپا درباره حملات اخیر آمریکا
🔴
عراقچی: این اقدامات آتش‌بس را بی‌اثر کرده
🔴
مسئولیت پیامد‌های خطرناک آن نیز بر عهده واشنگتن است
🔴
انفعال جهانی، موجب افزایش ناامنی جهانی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127122" target="_blank">📅 14:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127121">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نخست‌وزیر ایتالیا: اروپا باید در صورت تمایل ایران به مذاکره، تحریم‌ها را کاهش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127121" target="_blank">📅 14:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127120">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9650d1637f.mp4?token=XRdMclMZnUf6NL2vcj4cupqSZXrR-ra1qBoa2e5paQsyJOYlw6Zs70cEv-7EzfSowFU3wpHptHrucicOs2bh8OUtvCYy3c3oJ_7XjIsx268oJ_68AMfk4wzmzt8H3hAI_RSCKAn3DyPsbaM6MSrh_J096F8WDmb-7H15Y0r05xOrxiSg6Cx-mq8SuOlYMKwXd7-dLOtagbDpYTtFqHyOZOIOAhnBOVEXrnSh3tdFp_uNS1nDzolGhQi9ntpYtiJhIGVUMNVd7wUez7pdlpJ0yVOCTFTKSdq6aQ2VT49o0XMzsItEuoY42ufKOAfMrJIS-Q9F6ngiqMzDFuKIIYV_K2zuRYEjYNd7rHT7LQJ84mcgQzKrPZ8yq4qNQ1TeQHtZdnbL2fXgAD3_K1eb4TnURDHYjpetQuaKMQlLZx-PElNQrXFf8wz15TKBnyHaElimbAim3wGPIiIyJosEdVY-3inZFXWXXXW8eu2BzkmF5deV1mcWRib6UAwy80Nv4xua8VQga3F49L6oa6jnFwb5wV4BvPpQfwSkuYMzq7dHOfXr7b6X4UsNXE4Tqy_UPKau7wKaNBgJjbtlulKoxIfCgtG2DD9er2IVyVporWcVJjN8DRC0gTCBMrA4svM_bRnimd7wwEVH03RPUSuFcYWaE8mtHu5owc91BPdbEJ6C0os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9650d1637f.mp4?token=XRdMclMZnUf6NL2vcj4cupqSZXrR-ra1qBoa2e5paQsyJOYlw6Zs70cEv-7EzfSowFU3wpHptHrucicOs2bh8OUtvCYy3c3oJ_7XjIsx268oJ_68AMfk4wzmzt8H3hAI_RSCKAn3DyPsbaM6MSrh_J096F8WDmb-7H15Y0r05xOrxiSg6Cx-mq8SuOlYMKwXd7-dLOtagbDpYTtFqHyOZOIOAhnBOVEXrnSh3tdFp_uNS1nDzolGhQi9ntpYtiJhIGVUMNVd7wUez7pdlpJ0yVOCTFTKSdq6aQ2VT49o0XMzsItEuoY42ufKOAfMrJIS-Q9F6ngiqMzDFuKIIYV_K2zuRYEjYNd7rHT7LQJ84mcgQzKrPZ8yq4qNQ1TeQHtZdnbL2fXgAD3_K1eb4TnURDHYjpetQuaKMQlLZx-PElNQrXFf8wz15TKBnyHaElimbAim3wGPIiIyJosEdVY-3inZFXWXXXW8eu2BzkmF5deV1mcWRib6UAwy80Nv4xua8VQga3F49L6oa6jnFwb5wV4BvPpQfwSkuYMzq7dHOfXr7b6X4UsNXE4Tqy_UPKau7wKaNBgJjbtlulKoxIfCgtG2DD9er2IVyVporWcVJjN8DRC0gTCBMrA4svM_bRnimd7wwEVH03RPUSuFcYWaE8mtHu5owc91BPdbEJ6C0os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : ما تو همه جبهه‌ها پیشرفت قابل‌توجهی می‌بینیم
🔴
هر هفته صدها نفر از نیروهای مسلح دشمن رو از بین می‌بریم
🔴
همچنان چالش‌های دیگه‌ای هم پیش رو داریم
🔴
یه چالش ویژه هم موضوع ربوده‌شده‌ها (گروگان‌ها)هست که روی اون کار می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127120" target="_blank">📅 14:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127119">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=PgHpTMGcu9S3nlUQ18zLjWJR0sgBB0aK7-IsxBFqLJue_BWHrB7kjm_FIIGnlZS1hZ5G1q9VCBBKXOwCzDa21XtpFfDGk0l9iHAsMhN-X08ZjRRj2O5oNhgmT7U8L2o2D6gZKKHrN-_oqUl1PM1kMcu31ZT6OLXH3_smOMUtzwbDAYApWCzIO87AJjnIrZ94i58hne2vKzotDILnmFydgvEJqKn8bdSuEc3JZwNHOjmK-5e2nYL7xJ8_xPJGAnh7oauH-GSYHWy3qk_bXlp2Omr76raKGnYpFX0mBqZSRBr2nH19533mD-zn2DIAHIB3-Zdg6OkNZ5eS9_StbuGNPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=PgHpTMGcu9S3nlUQ18zLjWJR0sgBB0aK7-IsxBFqLJue_BWHrB7kjm_FIIGnlZS1hZ5G1q9VCBBKXOwCzDa21XtpFfDGk0l9iHAsMhN-X08ZjRRj2O5oNhgmT7U8L2o2D6gZKKHrN-_oqUl1PM1kMcu31ZT6OLXH3_smOMUtzwbDAYApWCzIO87AJjnIrZ94i58hne2vKzotDILnmFydgvEJqKn8bdSuEc3JZwNHOjmK-5e2nYL7xJ8_xPJGAnh7oauH-GSYHWy3qk_bXlp2Omr76raKGnYpFX0mBqZSRBr2nH19533mD-zn2DIAHIB3-Zdg6OkNZ5eS9_StbuGNPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از حملات امروز اسرائیل به لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/127119" target="_blank">📅 14:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127118">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRpnuNxUQZJCCjYZNbmMqtBnt4wBeyokMZCjASqbXw0qy5JmStwbeKVW707fuF9R6eSx1zNDQmTJvou8gPQNR9mdOxehUZ0bYm7UywCfEMh4EqgE94w8Ur5gQzWSpv7enyIMxOPCBL-P3hGJI-LFaY464sxYL57AODUF8GrK4Jfm1Q1L871incZtZDFOlUGK-dcHbwHKeY2fNAQ7nJterI7XxzPaJYoShKfJ8I4ra6Ltz2qUvcIoCbyZ7utkBfu1o3GwqGq91EwvULwxM3D5VbPU0FSKiFML9Rev6GjnFpTU650ChCk1d4mERu8KQAde5clGq_YwAYYwzxmjul0oHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد ، مارشال محسن رضایی: رئیس‌جمهور بی‌ثبات آمریکا تصور می‌کند که بمب‌ها می‌توانند او را از باتلاقی که خودش ایجاد کرده نجات دهند. اما موشک‌های ایرانی او را حتی عمیق‌تر در آن فرو خواهند برد.
🔴
واشنگتن باید بین پذیرش شروط ایران و از دست دادن آخرین ذره اعتبار خود در جهان یکی را انتخاب کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127118" target="_blank">📅 14:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127117">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
صدراعظم آلمان فریدریش مرز:
ایران باید برنامه هسته‌ای خود را به طور قابل راستی‌آزمایی و دائمی متوقف کند.
🔴
امنیت اسرائیل و کل منطقه باید تضمین شود؛ در غیر این صورت، صلحی در منطقه نخواهد بود.
🔴
امروز، ما در حال کمک به شکل‌دهی نظم نوین جهانی هستیم که در آن اروپا جایگاه قدرتمندی پیدا می‌کند، تا اروپا بتواند به عنوان نیرویی برای آزادی و شکوفایی، برای صلح و دموکراسی در جهان باقی بماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127117" target="_blank">📅 14:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127116">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت خارجه کویت: حملات مکرر ایران نشان دهنده رویکردی سیستماتیک و تهاجمی است که کویت نه آن را می‌پذیرد و نه تحمل می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/127116" target="_blank">📅 14:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127115">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
تسنیم: ادعای رسیدن به متن نهایی برای تفاهم بین ایران و آمریکا خبرسازی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/127115" target="_blank">📅 14:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127114">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رئیس سازمان اورژانس کشور: ۵ نفر در حملات بامداد امروز مصدوم شدند که ۳ نفر در تهران و ۲ نفر در هرمزگان بودند.
🔴
همه مصدومان پس از درمان مرخص شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/127114" target="_blank">📅 13:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127113">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزارت خارجه هند: ۳ کشتی هندی هدف حملاتی قرار گرفته‌اند که توسط نیروی دریایی ایالات متحده انجام شده است.
🔴
۱۳ کشتی با پرچم هند در تنگه هرمز گرفتار شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/127113" target="_blank">📅 13:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127112">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه: ایران و آمریکا باید حملات را متوقف کنند و برای پایان دادن به مذاکرات به میز مذاکره بازگردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/127112" target="_blank">📅 13:36 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
