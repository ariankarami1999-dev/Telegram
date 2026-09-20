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
<img src="https://cdn4.telesco.pe/file/gUkzXDvRQKSYAdTwVyn94PbukzFkyfYOnyG4B3Nms8L9ycX_4L241Igcs7NVU2qYxC0WwVLSLCAEXmupKppzVOVsA_2FUXfuAThYKx8wiEun4rKRRXgUbHgpxBhDPSybJETOzS6gGY3p4KJSyrKNSH0-MEqu4lS1mi_GnbqsXMKL10h5pte2pFj_1gUsSatDK0MtJMbCM5GXKiOxoJ5CHn8_DpAiC8eQ_FOn7Tpak-wW8tx1I_yjhmuCXZCdJ9WRLGGPitz2U_Tsm172xgFB0BJTG8FsQ9lc_3iLN471sWVF7XGNqXJ57wO7KHTU4XKzvd9YT3voqL1IRWuutB0OXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.03M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-691483">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be98fe0e5a.mp4?token=BjJvEDmNyDk-s2x1OhHXt4PlzYw9QedAWz0MFHt_Kr5ykNfjt1BcpIrIKSwjZ5ED2Of3PkHmwkJIWzFpTpE77smk-7gNgNKVQPsauiMVo668th1DoloMPWMdHB_uDBhzZ7_e4h6wBjE6wJwYELIXtOrIzB9G3s3vSsI0xOV6WZ-i3rT_3s9jqo0WT8LIZtR_MOPDpjayFosRcuAu9CkLF6rZbkVON1rvpaPr7ihkXpqSmuFFZES0PGxOpecO9bWCEYLD_F4CCm6_aqgapuRYhpPykz9oBjD_0Ee-OEaKBWlUnFgDhr8sENMEBaDW-FzCXPFkaxCg5A35XH-dadvlzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be98fe0e5a.mp4?token=BjJvEDmNyDk-s2x1OhHXt4PlzYw9QedAWz0MFHt_Kr5ykNfjt1BcpIrIKSwjZ5ED2Of3PkHmwkJIWzFpTpE77smk-7gNgNKVQPsauiMVo668th1DoloMPWMdHB_uDBhzZ7_e4h6wBjE6wJwYELIXtOrIzB9G3s3vSsI0xOV6WZ-i3rT_3s9jqo0WT8LIZtR_MOPDpjayFosRcuAu9CkLF6rZbkVON1rvpaPr7ihkXpqSmuFFZES0PGxOpecO9bWCEYLD_F4CCm6_aqgapuRYhpPykz9oBjD_0Ee-OEaKBWlUnFgDhr8sENMEBaDW-FzCXPFkaxCg5A35XH-dadvlzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری عربی از شنیده شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/akhbarefori/691483" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691482">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzg80iKT5hZ_wptmkRpGoJtLVZTuQ3Co1mNs2cmVhpxcXLlDb36DgfEkFqLae_cuPsw1hRDCRtJEDxvILOn8Feh0xClL_9DOjnD-dhZ3ohGqEV6tURUPT9q4oTzzcTj9PfAKN7ytKK8hrx7UxEvflNsK7pfyAivNDpq_02drt8JgH5pogs-ksYhpu11omB1Oc8tSBFiEcbvY2yyWXz7RabyIFaOU9sMiJCV8W-VPqcEpKOYsgAHGa-ypZxVrA7qwxHVOLFbCenFKiizvRfA3hEW9_XE8QeC2OYwPIEPODBoz1y5uo0fwVJTf83xj4rJ_sj6373fBu1UbhKrfv5BA_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهانه جدید افزایش قیمت خودرو؛ مابه‌التفاوت گواهی اسقاط چیست؟
🔹
قیمت پایه هر گواهی اسقاط خودروهای سواری از ۳۵ به ۶۰ میلیون تومان افزایش یافته و خودروسازان نیز طبق ضوابط جدید باید به‌جای یک گواهی، ۱.۵ تا ۲ گواهی برای هر خودرو تأمین کنند؛ موضوعی که هزینه خودروهای صفر را افزایش داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/691482" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691481">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6aa19afc6.mp4?token=f59hDdjAOHfFt8oAtPmaChF70UNigFyRrbwqd1HC5Ku603rcVOZDHN1NC3tmfkjn8U-g67B0bLi6npGkhDdWCb3a1a-Oc591NvqdvrxTUYdH3G3szURImi7KYbmAGGBZROD-A9AIUUp8a6KQp0kUrVLv6SNux6HgY9sb90wAFh8WHXL4y0hCC1fxL61f5IfYPkbJOdezkzPTwjrIGftOJfwsi-qFRZoism-xsAQ77iA23qLjESSb_tdpzqqq9vr2Gw0tbMf-5smoLBGj5YIWLGljsaxJPwlbqS6RqI3gOqqE78-MhDJjWoQ45x1M98WPerhamVrf8iTvLutPz-52YRIdwUe8fybkp-AgzWhNiP6DC_lObb8xYi1-fJWfkrfXaAT_FK-kGvYBm6NW6b0ykf9iKlgbgtQEmQuMKGiK-BEQX4Uc3_R7kG_OilzOHVMQGcEyEX4ecCQdDDydIUpYaKq9tmCff9BGCMPouSsfWv8mLrTgPknGRYeedrLHVhROEWOLqrgimNABQRS4-CzkC5OvfqppacgOxF9JK0zgzV3Mqyby0M7KVw0q6d_Zf14YnbCOolnZh4cAydcdDAFvwrfpJPW8fpL3dAG4GDGnS29Vyhn4p5sK5CPZzzmaAlN7JlIZFasN7HGWq4y7oYKLM_cAHlACg7TJO9kMevbUvTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6aa19afc6.mp4?token=f59hDdjAOHfFt8oAtPmaChF70UNigFyRrbwqd1HC5Ku603rcVOZDHN1NC3tmfkjn8U-g67B0bLi6npGkhDdWCb3a1a-Oc591NvqdvrxTUYdH3G3szURImi7KYbmAGGBZROD-A9AIUUp8a6KQp0kUrVLv6SNux6HgY9sb90wAFh8WHXL4y0hCC1fxL61f5IfYPkbJOdezkzPTwjrIGftOJfwsi-qFRZoism-xsAQ77iA23qLjESSb_tdpzqqq9vr2Gw0tbMf-5smoLBGj5YIWLGljsaxJPwlbqS6RqI3gOqqE78-MhDJjWoQ45x1M98WPerhamVrf8iTvLutPz-52YRIdwUe8fybkp-AgzWhNiP6DC_lObb8xYi1-fJWfkrfXaAT_FK-kGvYBm6NW6b0ykf9iKlgbgtQEmQuMKGiK-BEQX4Uc3_R7kG_OilzOHVMQGcEyEX4ecCQdDDydIUpYaKq9tmCff9BGCMPouSsfWv8mLrTgPknGRYeedrLHVhROEWOLqrgimNABQRS4-CzkC5OvfqppacgOxF9JK0zgzV3Mqyby0M7KVw0q6d_Zf14YnbCOolnZh4cAydcdDAFvwrfpJPW8fpL3dAG4GDGnS29Vyhn4p5sK5CPZzzmaAlN7JlIZFasN7HGWq4y7oYKLM_cAHlACg7TJO9kMevbUvTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تراژدی تلخ گردشگری ایران؛ جذابیت در بین برترین‌ها، درآمد تهِ جدول!
محمد درویش، کنشگر محیط‌زیست:
🔹
ایران از نظر جذابیت‌های طبیعی جزو ۵ کشور اول و از نظر جذابیت‌های تاریخی و فرهنگی جزو ۱۰ کشور نخست دنیاست، اما در کسب درآمد از این حوزه‌ها حتی در میان ۱۵۰ کشور اول هم قرار ندارد./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/uH-2rlDLEnw
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/691481" target="_blank">📅 17:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691480">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de4dd6b96.mp4?token=kUwMqMH_fNrQAcrJtrA7aaOYtD9deBVzu1_WnXXPZeucTKnACc85AylqFbsmxlWoSHHqLunnRRC07ZnCHsgEUX1ukJ0n57_5an_ofA90XQBwFbvM-zfg82ATbaGmzC5IRBA14Euqc55KwcgaB4zGClG3NgoB2j6F9_NN_UkKrRTx3qZhny-6QP34oMZYVWezCNOnWFjLvDMxmEpeJIbi_mTWEQ9PjzanCS9NqEPsKKIeByTazFha1qKkQIavb57RrWpDr5tpTI5PzIkPXSsh3zDygvBUdqMZwznw5JWTDtfUUW2S9I36WK22ATm7iW3n2NBuOmy9Xnq4FmTY9YrRkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de4dd6b96.mp4?token=kUwMqMH_fNrQAcrJtrA7aaOYtD9deBVzu1_WnXXPZeucTKnACc85AylqFbsmxlWoSHHqLunnRRC07ZnCHsgEUX1ukJ0n57_5an_ofA90XQBwFbvM-zfg82ATbaGmzC5IRBA14Euqc55KwcgaB4zGClG3NgoB2j6F9_NN_UkKrRTx3qZhny-6QP34oMZYVWezCNOnWFjLvDMxmEpeJIbi_mTWEQ9PjzanCS9NqEPsKKIeByTazFha1qKkQIavb57RrWpDr5tpTI5PzIkPXSsh3zDygvBUdqMZwznw5JWTDtfUUW2S9I36WK22ATm7iW3n2NBuOmy9Xnq4FmTY9YrRkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیر گرفته شدن فوتبالیست انگلیسی توسط خودروی چمن در طول مسابقه‌ در تایلند
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/691480" target="_blank">📅 17:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691478">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e978e35310.mp4?token=i3CH_Dti88NoeqvAFMeAue_X9dvYZwFehjifc81FOJZIlMlMUDVHIqft1UD00GStWbgTSoSibJYHhd9OriSbPz3FsE3YUNALeXiqJJ7nGTdO9sCfouu7rauraKBnG2VA9aZf1F2I3nqkqeCgrV_bAOCz4kfaY9hRZSRAqZxAYcrv2YeMj4_BAx4A78fqsIK-TMvItWTAFcKDewYZpAhbYL-fJIb7AmRCe-pBNeIYR2Yh0chL8FA1DeUjlBigF_HR4Ts6oBgWe_UqMQIeumDlrmKGup5bkaEOyxOSsSvqAqRxIAKdYZkXLXbHsu30Stwu_FADhaIRbaPTzRF3ei0Hqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e978e35310.mp4?token=i3CH_Dti88NoeqvAFMeAue_X9dvYZwFehjifc81FOJZIlMlMUDVHIqft1UD00GStWbgTSoSibJYHhd9OriSbPz3FsE3YUNALeXiqJJ7nGTdO9sCfouu7rauraKBnG2VA9aZf1F2I3nqkqeCgrV_bAOCz4kfaY9hRZSRAqZxAYcrv2YeMj4_BAx4A78fqsIK-TMvItWTAFcKDewYZpAhbYL-fJIb7AmRCe-pBNeIYR2Yh0chL8FA1DeUjlBigF_HR4Ts6oBgWe_UqMQIeumDlrmKGup5bkaEOyxOSsSvqAqRxIAKdYZkXLXbHsu30Stwu_FADhaIRbaPTzRF3ei0Hqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ قمارباز: گزینه‌های روی میز فعلی، محو ایران، فروپاشی اقتصادی آن یا دستیابی به توافق است
🔹
سوال من این است که چه زمانی و آیا کل ایران را منفجر خواهم کرد یا خیر، و بهتر است خودشان درست رفتار کنند. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/691478" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691477">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتامین مالی جمعی رضوی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLP5X1TPHzql_1GWfb4VIsz-QkFpwVl2DxSr0xEJOdro4fde54PJ_ZIRrlc2pC7S9zQVrum_qz_JBYkWRfyARV92AiJyDs7PzCWvC0gPcO-p_3zrMbGcEogZ0uCjLl4WTBmWC6kPwcnAwZr0mCUBqnL8e9LVBAmWRrD3tzcHtPeeVAf0pnkItwpq8fTYn1zYVopzY9HNSFu5WKMA8OGujrEqvUQr0BCpfsFEjMmuT0QTB1dPildfqc4EI_fQxObw8LzbpP25YlQZCvdSk8gzne1NrT8YYs2gEXSCKrMFS7eEY_ZZ994E6aAwcvDaT4d9dn2IUI-MP_SBYTuR0FoSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
همراهان عزیز سکوی رضوی،
فرصت سرمایه‌گذاری در طرح ارائه خدمات آموزشی تخصصی زبان های خارجه آغاز شد!
✅
سودپیش‌بینی شده:
۴۶ درصد یکساله
(پرداخت ۳ ماهه)
✅
دارای
ضمانت تعهد پرداخت
بانک ایران زمین
✅
شرکت تعاونی راشد جوان مبتکر
🌟
سودمندانه اعتماد کنید…
کسب اطلاعات بیشتر و سرمایه‌گذاری:
تلفن تماس:
05191008000
سکوی تامین مالی جمعی رضوی
cfrazavi.ir
آدرس ما در فضای مجازی:
تلگرام
بله</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/691477" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691476">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">برنامه‌های «شفرونی» و «روشن» با دستور قضایی رفع توقیف شدند
🔹️
پس از اعلام جرم ساترا علیه برنامه «شفرونی۲ » در ۲۱ شهریور ماه و دستور دادستانی مبنی بر توقف پخش، امروز حکم رفع توقیف این برنامه صادر و «شفرونی» می‌تواند از همین هفته پخش خود را از سر بگیرد.
🔹
ساترا در شکایت خود به دادسرای فرهنگ و رسانه، انتشار بدون مجوز و محتوای غیراخلاقی و خلاف عفت عمومی را عامل درخواست توقیف برنامه عنوان کرده بود که با حضور تهیه‌کننده برنامه در دادسرا و ارائه توضیحات و مستندات و انجام برخی مراحل قانونی، دستور رفع توقیف «شفرونی» صادر و به پلتفرم پخش‌کننده و ساترا ابلاغ شد.
🔹️
همچنین برنامه «روشن» نیز با استناد به قانون مطبوعات و آیین‌نامه‌های اجرایی آن مشمول موارد ادعایی در شکایت ساترا نشد و دستور تداوم پخش آن نیز صادر شد.
Asriran.com
@MyAsriran</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/691476" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691475">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای ترامپ: احتمالاً آماده دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در حاشیه مجمع عمومی سازمان ملل موافق خواهم بود #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/691475" target="_blank">📅 17:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691474">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e18660f7.mp4?token=g-xBROToyQTZMq4E-CldrkKzagPl8doHc_DMSKnQrVuPNNu8yAOdCck-DLF_oxw1Zf_o6cPiSQ8UpC6TAuXyLC5-542kiwxoFQcuf2cck_hE7aBEmtsX8F7vx65iV1Cz1GgN0s7v20t23rdqvhBr28lOfUnAB5C1nGFfGMkxk7jNNiQedjGUdtsXD9V5R5C6OvYIVzw1zIr_cz81kskLlce4RvPsnQ9U_e7RjawP49AqHp2oP78A23cQrHN-yKOCuQ7azHTENRkjH-P4SR82BSv8q8Jp9FQQm_Io62U5YEcEnZsyZDzE4ZRHlK2DO7C1xKkaX3JftUB31LYib9zg4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e18660f7.mp4?token=g-xBROToyQTZMq4E-CldrkKzagPl8doHc_DMSKnQrVuPNNu8yAOdCck-DLF_oxw1Zf_o6cPiSQ8UpC6TAuXyLC5-542kiwxoFQcuf2cck_hE7aBEmtsX8F7vx65iV1Cz1GgN0s7v20t23rdqvhBr28lOfUnAB5C1nGFfGMkxk7jNNiQedjGUdtsXD9V5R5C6OvYIVzw1zIr_cz81kskLlce4RvPsnQ9U_e7RjawP49AqHp2oP78A23cQrHN-yKOCuQ7azHTENRkjH-P4SR82BSv8q8Jp9FQQm_Io62U5YEcEnZsyZDzE4ZRHlK2DO7C1xKkaX3JftUB31LYib9zg4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ممکن است به زودی اتفاق  بزرگی در مورد ایران اتفاق بیافتد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/691474" target="_blank">📅 17:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691473">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای ترامپ: ممکن است به زودی اتفاق  بزرگی در مورد ایران اتفاق بیافتد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/691473" target="_blank">📅 17:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691472">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=ZhsLP5_dF3bWS02JSppbLT3nKiHlQ8Ynm7SE8zlYCglOQh6zyEH8TBks-ri3GFG-bH0MnYe0gbatXoPpZD1eVdczS6bhVHq_2AiMv-lg5YMg4aeBYVcij5n0DdDWPRe7Y7qdF53ZYGTGd27Z0KCV0oF75m1u8HRwPhCVnzkyJDUt9F0bjragaJYnoe8JyqQ3St0GypbdsT2toX3bPimy-iQZ-83hYf3rMR0aySBRSDOQ6_7PNO2FgTcR5qrvG7k2okmmg59bI3G3TfABXmc7wo8Ef4-LqZSEIwZ5PtU-WzUyn1Bm0PIv1oacQJhcsltxNDmkP2guBkIFPCSDOs0fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=ZhsLP5_dF3bWS02JSppbLT3nKiHlQ8Ynm7SE8zlYCglOQh6zyEH8TBks-ri3GFG-bH0MnYe0gbatXoPpZD1eVdczS6bhVHq_2AiMv-lg5YMg4aeBYVcij5n0DdDWPRe7Y7qdF53ZYGTGd27Z0KCV0oF75m1u8HRwPhCVnzkyJDUt9F0bjragaJYnoe8JyqQ3St0GypbdsT2toX3bPimy-iQZ-83hYf3rMR0aySBRSDOQ6_7PNO2FgTcR5qrvG7k2okmmg59bI3G3TfABXmc7wo8Ef4-LqZSEIwZ5PtU-WzUyn1Bm0PIv1oacQJhcsltxNDmkP2guBkIFPCSDOs0fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نویسندۀ آمریکایی: ما از منطقۀ غرب آسیا بیرون رانده شده‌ایم؛ به این معنا که پایگاه‌های ما دیگر کارایی ندارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/691472" target="_blank">📅 17:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691471">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80061ce38a.mp4?token=TqaR2EADI0qW1KLgdAFvQT81OAjy4QgjVnHQ47Ay0Ck8tRnbdEp_iFYFgZ85sqmhItKRnqADToGW9Fs8rs3U4GKutWoiFcWF7DJUuIVvLrhN0_ohiSaqfbbVpnpnSBtY7RxuOZusRgLKExIEkG2gXkE-vT_gjrBOKfmdXwtg_aJ7AJYAaC-vv7-biPV9Q-hbg-isV_uMMbFFUEdtClRJ4aO49jm5hH-0vwUQN_5SbDcTNJVWl0nmxncs8-iw3qx_BhIR-51asUgSjm98ZVpyYxSEQv0LFlgC0AyXDd11EcLHbcxuhhN-eqmP6KUQ8x_2OeaEvCm8XtZtfFGt-M8PUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80061ce38a.mp4?token=TqaR2EADI0qW1KLgdAFvQT81OAjy4QgjVnHQ47Ay0Ck8tRnbdEp_iFYFgZ85sqmhItKRnqADToGW9Fs8rs3U4GKutWoiFcWF7DJUuIVvLrhN0_ohiSaqfbbVpnpnSBtY7RxuOZusRgLKExIEkG2gXkE-vT_gjrBOKfmdXwtg_aJ7AJYAaC-vv7-biPV9Q-hbg-isV_uMMbFFUEdtClRJ4aO49jm5hH-0vwUQN_5SbDcTNJVWl0nmxncs8-iw3qx_BhIR-51asUgSjm98ZVpyYxSEQv0LFlgC0AyXDd11EcLHbcxuhhN-eqmP6KUQ8x_2OeaEvCm8XtZtfFGt-M8PUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن روزی‌طلب، معاون سابق صداوسیما: ادعا شد در حوادث ۱۸ دی صداوسیمای شهر کیش سقوط کرد و تسخیر شد/ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/691471" target="_blank">📅 17:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691470">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
صحبت‌های تلخ محمود بصیری پس از مدت‌ها؛ تلویزیون بیننده ندارد، من برای کی بازی کنم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/691470" target="_blank">📅 16:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691468">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52c097554.mp4?token=lAHh4ZsVK4AgSZpZw-Ef2p4muBr6nsmhuTFlIdfT8ClmTLIU6lCmDXP7GxzisgE1CZ0NAe7aNNbMWk5ebgWZKV3dEu3Q38hnfxozgBGkZWR1_IJrizS8fR9_qSjymL_mov8gzLzLHZfkdNGc_nE_IQ_BxxePGlLDFsFOR5EI4RooUf9BIwcrHnVw7zLvnSrPArRGz-puu6AJLDUIC3l9w_77ZSIK4_j-xOwlU6GIr3cwl1TF-V0vJ2jF2ap4tmWvOCOMc1YoIQ7zypEZIbTUBNNExfwp8ncQAehi622nQG4KbSCZNMTYOAtljMqjgyVHrE_e4dUmCxrcU56Dx9N3cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52c097554.mp4?token=lAHh4ZsVK4AgSZpZw-Ef2p4muBr6nsmhuTFlIdfT8ClmTLIU6lCmDXP7GxzisgE1CZ0NAe7aNNbMWk5ebgWZKV3dEu3Q38hnfxozgBGkZWR1_IJrizS8fR9_qSjymL_mov8gzLzLHZfkdNGc_nE_IQ_BxxePGlLDFsFOR5EI4RooUf9BIwcrHnVw7zLvnSrPArRGz-puu6AJLDUIC3l9w_77ZSIK4_j-xOwlU6GIr3cwl1TF-V0vJ2jF2ap4tmWvOCOMc1YoIQ7zypEZIbTUBNNExfwp8ncQAehi622nQG4KbSCZNMTYOAtljMqjgyVHrE_e4dUmCxrcU56Dx9N3cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منوی سه‌بعدی؛ ایده‌ای متفاوت برای سایت رستوران
🍔
🔹
می‌توان به‌جای منوی معمولی، هر آیتم غذایی را به یک صحنه سه‌بعدی و تعاملی تبدیل کرد؛ ایده‌ای جذاب برای منوی رستوران، معرفی محصول و کمپین‌های برند.
🔹
این مدل اجرا برای Restaurant Menu / Product Showcase / Brand Campaign واقعاً جذابه چون خود طراحی چاپی رو تبدیل می‌کنه به بخشی از تجربه کاربری .
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/691468" target="_blank">📅 16:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691467">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt9KQpMX7NL6Xdyx3RzM379RbhFta4HodB_D0cSDq9023AZ1wEVvMs6wuPuWmzXkgTNhN7seljxEwTdyDgwhjyhbQJ_llLb-pH1uHBrL5hjnE2BC8Q0Vi2hdIG8KUzZAThMFD-1cxkylDJT-U7SYinJbnZ24EMHMA6aUwWz5JsTXBCPnBP8tatgUiNNipSTlbog3bp4rzIOmg2c2y4kQqCmDz72qhASRQGuVE241xThK7tyE_NDfLaNZh2XyAid5BG0PiJxob58BxUB1lUPPPfEvlyZ6c_sy3-cYHgCB9JqFFKl0t6db0NAgvLdIyhQlnFoUb13coaEuEQORcFHudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارخانه‌ها روشن، بازار خاموش | لوازم خانگی؛ صنعتی که نباید قربانی واردات شود
🔹
صنعت لوازم خانگی ایران در سال‌های اخیر یکی از معدود بخش‌هایی بوده که توانسته از دل محدودیت‌های اقتصادی و تحریم، مسیر تازه‌ای برای توسعه پیدا کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246628</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/691467" target="_blank">📅 16:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691465">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6167b311.mp4?token=J6Qv6hGv3fR9GBeINpkby0p2vgCwbxiyJS1qEJubC_T2n9fYqFkQjai6fQ7U2Gqjw_xOYRKVstkLas5-cYpmmYSQVpQMGufF8UPzh6AbnDotN0x2keEydhb3Ja1azvRKKu90UlBCqyIzWAwpDsvufEwqG3h9iXU18A9Cvl5jB5lybXV7snL3APxTVSCXayjotfIEFeeBHYPqreypuJH6Pc3kgXGsLVyGzRT7H91FCN_9XxF4To74zTaHS0jq59mcdycgoCRB6tLXp_FJqPfpu5lEvEmOlUfTM5-MvHc4ZSrUy38g0Jd6UNPMhDk2EYFpOV3eA47ZetKxc-CxZeXylQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6167b311.mp4?token=J6Qv6hGv3fR9GBeINpkby0p2vgCwbxiyJS1qEJubC_T2n9fYqFkQjai6fQ7U2Gqjw_xOYRKVstkLas5-cYpmmYSQVpQMGufF8UPzh6AbnDotN0x2keEydhb3Ja1azvRKKu90UlBCqyIzWAwpDsvufEwqG3h9iXU18A9Cvl5jB5lybXV7snL3APxTVSCXayjotfIEFeeBHYPqreypuJH6Pc3kgXGsLVyGzRT7H91FCN_9XxF4To74zTaHS0jq59mcdycgoCRB6tLXp_FJqPfpu5lEvEmOlUfTM5-MvHc4ZSrUy38g0Jd6UNPMhDk2EYFpOV3eA47ZetKxc-CxZeXylQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی عجیب از آواز خواندن آقای دکتر در اتاق عمل!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/691465" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691464">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f97800973.mp4?token=Sb4wOCdyPUgMNinQTuaCc295j4SkB1M1TqA1G0jDOVlsd85B_YpW-Yub6WZEbQx_NBA798cX1KnjTWZWOr-reg6x6SqrRTZLL5vrDBd2uMUz2pJpRotHHMW7xbE8AVoRgnUDnFP_TrQHu6zPix1kY34h_yK9575bD2TkHqr2d3Q5aNwWcVGdwesOjVCBnoQfCALn6A5n8MhPlhL6Qannx3WhPglAqIFwj4PszbtsTqI-9zx-4YmdYfZbeD5aLCDLR8d9Vh4YyPzX6QdGTOwFwjiAomz75MaqBytbWr_4O6KfuENIorFbSAiOHMp6pJMSwOhRsHSky0lgTINjnBHqQidtDkmCNIJz9w3lnFmdff8R_1vOGsY3d3KcflzcRCk4CKpzixUF4YEVkb2IUVVM5uGIM8ayQ-qIpaHHVqO9MgR9OIOXvavnsUVClVDeWxkyLR6V8Jc2ep0F7xRRH4PTdyekXQ4yGrfDn0qm-VoywkbfCM9XawPt6TLJ-0IUcBY7dUYRSiCGdvo9gMxKFpUOgIG2rH0XQqPiljev9IKyp_tograe9lqU0dX3ID6gr7Qczb-6uUErh0LTFP6jThUcWtBCWgFSyYMNEUykVrBIH-19veMsBqkhwGYdvmdLwwUZyTX_8oRaoCQKxF3EGo8Q2geFzAqoxpNwZPB82BF_SJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f97800973.mp4?token=Sb4wOCdyPUgMNinQTuaCc295j4SkB1M1TqA1G0jDOVlsd85B_YpW-Yub6WZEbQx_NBA798cX1KnjTWZWOr-reg6x6SqrRTZLL5vrDBd2uMUz2pJpRotHHMW7xbE8AVoRgnUDnFP_TrQHu6zPix1kY34h_yK9575bD2TkHqr2d3Q5aNwWcVGdwesOjVCBnoQfCALn6A5n8MhPlhL6Qannx3WhPglAqIFwj4PszbtsTqI-9zx-4YmdYfZbeD5aLCDLR8d9Vh4YyPzX6QdGTOwFwjiAomz75MaqBytbWr_4O6KfuENIorFbSAiOHMp6pJMSwOhRsHSky0lgTINjnBHqQidtDkmCNIJz9w3lnFmdff8R_1vOGsY3d3KcflzcRCk4CKpzixUF4YEVkb2IUVVM5uGIM8ayQ-qIpaHHVqO9MgR9OIOXvavnsUVClVDeWxkyLR6V8Jc2ep0F7xRRH4PTdyekXQ4yGrfDn0qm-VoywkbfCM9XawPt6TLJ-0IUcBY7dUYRSiCGdvo9gMxKFpUOgIG2rH0XQqPiljev9IKyp_tograe9lqU0dX3ID6gr7Qczb-6uUErh0LTFP6jThUcWtBCWgFSyYMNEUykVrBIH-19veMsBqkhwGYdvmdLwwUZyTX_8oRaoCQKxF3EGo8Q2geFzAqoxpNwZPB82BF_SJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب کفش به تصاویر ترامپ و نتانیاهو در کره جنوبی
🔹
حامیان فلسطین در سئول در اقدامی نمادین، کفش‌هایی را به سوی تصاویر ترامپ و نتانیاهو پرتاب کردند و اعتراض خود را به جنایات این دو نشان دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/691464" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691463">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
پنجشنبه‌ها در استان قم تعطیل نیست
معاون توسعه مدیریت و منابع استانداری قم:
🔹
خبر منتشرشده درباره تعطیلی پنجشنبه‌های دستگاه‌های اجرایی استان تا پایان سال صحت ندارد.
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/691463" target="_blank">📅 16:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691462">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f20de068bb.mp4?token=d1JX22ZM0bO7adilZhZQilYMS_Y5usmTl8y6tEiR55l04FPCt2b4Lvj7yuE3-NWVutEJJNAzXdnsOnYExGE9hgU8Ewz2qBKYaZ70xCauJ2lvaqkaetyTtG92COvR4Vkmdo7KQCP2lA0Mnw3WS7JD_6J0tj89zNAJgXPLfDXzaCdPB4ou4iu9ZC0rF3LEocxKvaW7q0I8XNTBC_WEidouwky-Hfxz3uQ9lOk1DPh9PU_df3G_925w35dpq6I1N81t2zjCVy5JgSNy8Se7b4wAs6f6vlhzdx1XYWKZYEe48p85k-S1M41Tmwh1NRd4jfkR8-QXZiu1hVZUbx1CJc7gHjfT0SevryPmMUwNPNzdxNUI0lFxP-pr7W7J6qvFKviCfb9AOVikC_8EF8DLs4Lj4mdacMcWQV5cZvboGE2nj8gkAxuBtUdh_U9O2YEF_gWJ1m9HwsI4gOpaLB1U5dHbg4wk64I8k6FYXtlYj_THtSVDxJ-zHTotOnL_0Udk2rEfaRci-gdSDKMpDIWCF8QaT7CGhkvetvzcb_NyHRg1BNv6F31tWp6e-lKxW-krjIMytAwauQMKCzZeGYWPbKTbdLIr7Hx5tQrk8krP7ozZnj7GrAp_STmW4wjgG62vbCCary4jVYD67-rxGiv8sTH8VK-PL8-jHCXNXtfe0Z6gqcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f20de068bb.mp4?token=d1JX22ZM0bO7adilZhZQilYMS_Y5usmTl8y6tEiR55l04FPCt2b4Lvj7yuE3-NWVutEJJNAzXdnsOnYExGE9hgU8Ewz2qBKYaZ70xCauJ2lvaqkaetyTtG92COvR4Vkmdo7KQCP2lA0Mnw3WS7JD_6J0tj89zNAJgXPLfDXzaCdPB4ou4iu9ZC0rF3LEocxKvaW7q0I8XNTBC_WEidouwky-Hfxz3uQ9lOk1DPh9PU_df3G_925w35dpq6I1N81t2zjCVy5JgSNy8Se7b4wAs6f6vlhzdx1XYWKZYEe48p85k-S1M41Tmwh1NRd4jfkR8-QXZiu1hVZUbx1CJc7gHjfT0SevryPmMUwNPNzdxNUI0lFxP-pr7W7J6qvFKviCfb9AOVikC_8EF8DLs4Lj4mdacMcWQV5cZvboGE2nj8gkAxuBtUdh_U9O2YEF_gWJ1m9HwsI4gOpaLB1U5dHbg4wk64I8k6FYXtlYj_THtSVDxJ-zHTotOnL_0Udk2rEfaRci-gdSDKMpDIWCF8QaT7CGhkvetvzcb_NyHRg1BNv6F31tWp6e-lKxW-krjIMytAwauQMKCzZeGYWPbKTbdLIr7Hx5tQrk8krP7ozZnj7GrAp_STmW4wjgG62vbCCary4jVYD67-rxGiv8sTH8VK-PL8-jHCXNXtfe0Z6gqcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلایه شهروندان نطنزی از تأخیر در رسیدن آمبولانس/پاسخ بحث‌برانگیز اپراتور ۱۱۵/تأسیسات هسته‌ای نطنز در نزدیکی این شهر قرار دارد!
🔹
تأخیر بیش از ۳۰ دقیقه‌ای در رسیدن آمبولانس به محل یک حادثه در شهرستان نطنز، موجب نگرانی و اعتراض مردم شده است.
🔹
بر اساس ویدیوی منتشرشده از سوی یکی از شهروندان در تماس با سامانه ۱۱۵، پاسخگو اعلام کرده که آمبولانس در مأموریتی در سرآسیاب است. شهروند معترض نیز نسبت به وضعیت امدادرسانی و تأخیر پیش‌آمده اعتراض کرده که بنا بر این روایت، اپراتور در پاسخ گفته است:
«بدبخت اورژانس! اشتباه می‌کنند خدمات رایگان به مردم می‌دهند»
و سپس تماس قطع شده است.
🔹
در ادامه این روایت آمده است که با ۱۱۲ هلال‌احمر نیز تماس گرفته شده، اما اعلام شده امکان اعزام نیرو وجود ندارد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/691462" target="_blank">📅 16:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691461">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb09df83f7.mp4?token=tvi9CQZhSfbVzBINlHDnyJUF4H5d6mWRI2pxZwsKuXA4wEjkIcA6Mtk-SkuGeX3FrDfqgdat5HdFRaezwp4vXf8T8HnjRj-cvgblS-HR2D35ydZ5L-1P4HogaVECBB0KIgS5lv4v-VngY7kO3krGbefQhq3dpYpmOWDAtB8L_hMAN8_aNPXDQs2qFv6LNYCx2TBYFr4-rnt1IIDFVQrz7HFQn-sjnrSu97TG1zl0EYTlc7oP1-L5NIxrrflLjZ1XEdmbuH0HxfJSLpB2d-qYtZCmOxBNEIZrDj7WIQvnYmMnIznIvoavnSZtANFK12U8IHrkLQVKFP5SPtVK8NTtgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb09df83f7.mp4?token=tvi9CQZhSfbVzBINlHDnyJUF4H5d6mWRI2pxZwsKuXA4wEjkIcA6Mtk-SkuGeX3FrDfqgdat5HdFRaezwp4vXf8T8HnjRj-cvgblS-HR2D35ydZ5L-1P4HogaVECBB0KIgS5lv4v-VngY7kO3krGbefQhq3dpYpmOWDAtB8L_hMAN8_aNPXDQs2qFv6LNYCx2TBYFr4-rnt1IIDFVQrz7HFQn-sjnrSu97TG1zl0EYTlc7oP1-L5NIxrrflLjZ1XEdmbuH0HxfJSLpB2d-qYtZCmOxBNEIZrDj7WIQvnYmMnIznIvoavnSZtANFK12U8IHrkLQVKFP5SPtVK8NTtgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا حباب صندوق های اهرمی در بورس منفی است؟
@Titretejarat</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/691461" target="_blank">📅 16:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691459">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
انتقال جنسی، شایع‌ترین راه انتقال HIV در سال‌های اخیر
رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
انتقال جنسی در سال‌های اخیر به شایع‌ترین راه انتقال HIV تبدیل شده است. او همچنین اعلام کرد وزارت بهداشت آمار بیماری‌های مقاربتی در میان دانش‌آموزان را در اختیار ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/691459" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
فرانسه: دو دیپلمات ایران طی روزهای آینده اخراج می‌شوند
🔹
وزیر امور خارجه فرانسه در پیامی در شبکه ایکس ضمن حمایت از اغتشاشات دی‌ماه نوشت که قصد اخراج دو دیپلمات ایرانی را دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/691458" target="_blank">📅 15:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
شمارش معکوس تا انتخابات آمریکا و اسرائیل
🔹
انتخابات میان‌دوره‌ای آمریکا ۳ نوامبر ۲۰۲۶ برگزار می‌شود؛ از امروز ۴۴ روز باقی مانده است.
🔹
انتخابات رژیم صهیونسیتی نیز برای ۲۷ اکتبر ۲۰۲۶ تعیین شده و ۳۷ روز تا برگزاری آن باقی مانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/691457" target="_blank">📅 15:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoKEd3EGTfK-K473_kUlOWXGopv6jQ_UugC_7qgZ4Z8IJyzR17aro7BuZ6p0PpRiKveIQWyfxvAf8eUNMmBmkwxUcUKP6tXbMVk8tCA94NZ9XKY4pFVb10E_u4U_JuPO8nMzHV-JHDJCsRJLHk_Tc7GlmDAg3IECCA1cJJIKp6H8u61s3SkkeOzofqHbLESIf67ycqWzzgyrO3dxB5mzGE01GKVJ2FQL0vm9VKRLr9WbOJeMpA-E6MysUVemPH1c6U1d9QxiOnmRIkY6DQljmIAZIK_A7mBs_sQKtPwnkD0Rc6IltvyllnVApkVwJD__6ReCv8U7mQwt0YFvgcNhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش سی‌بی‌اس امریکا در مورد پویش جانفدا: تجمع گسترده ایرانیان در نمایش وحدت و مقاومت
🔹
به گزارش
CBS News
، صدها هزار ایرانی روز جمعه در تجمعی سازمان‌دهی‌ شده شرکت کردند و آمادگی خود را برای دفاع از کشور و دریافت آموزش‌های نظامی اعلام کردند.
🔹
بر اساس گزارش‌های رسمی ایران، بیش از
۳۰۰ هزار نفر
در این تجمع حضور داشتند برخی از شرکت‌کنندگان پرچم‌های آمریکا و اسرائیل را زیر پا گذاشتند و برخی دیگر شعارهای
«مرگ بر آمریکا»
و
«مرگ بر اسرائیل»
سر دادند.
🔹
رسانه‌های دولتی نیز طی هفته‌های گذشته مردم را به پیوستن به این کارزار تشویق کرده‌اند و گفته‌اند آموزش استفاده از
سلاح‌های تهاجمی
به‌زودی آغاز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/691456" target="_blank">📅 15:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
هشدار قرارگاه مرکزی حضرت خاتم‌الانبیا (ص) به آمریکا و کشورهای منطقه: خطا کنید هدف حملات دردناک قرار خواهید گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/691455" target="_blank">📅 15:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691449">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F52kI26KbtNCqvPpSSY_08jMZU_9nKB9RjxDTyjuEiWbIHzHKZi53_wVgE6l7QdRRPe6H9OpGjRGW6jLPcibWQPuHZeWKRIW6oJRy1CV1QoWZOPEaU4sQWspbBxWRKHObRpxEneGhazvgszKUbc_DagR-hqyqOAa7dtVZZsXMUWbT6w4ns9bF8RuEm4c3ygdNwn6paM8yuzJbwL6EUZxOtPYFKUp_XijaAAWsLG23uCIh7y1RD63kMpTB7cJFtcxQGsd6E16KzEme5Sn8HjOx8xPXtDysAOZIxnEwwjJYUDhsYaBiKPEfxotIn653tx3QKUEEew5Spl5eYmKzPCY0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2NA8iWTWo4uWp3pwLshnpElfOUwuO6wSV3O9cFw7-T6-FFi5ATOdXwJA3Mn9aGnjpT5NN_5WN4CfLjQpi3lAXiTu2PSCkhbkTowt4ZN476DLZBvCGP6SgDcYxhLYAEkkAiWWvPZ4E0AtvbtrjbszUAdiDQYIlu15Y6BmdybKGDu-_2YKIqST00_UretVKmfa4oPhbxVbLTdxw1qXTQWvRZdHWWWh_JLDHZz2CtYAmEVaolI1VcCYGVgOhYr-66r1OWrHyVRbHblL0w-lKOBBMf4KCqk_8s9UrDsNIxGhYPN9WEjXVNIUnY_EhubxySNKX9WLq0cllFeDu3Qyy6XgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nKXfiH5bMNL8eTiVCwJbkwpeujcACuQx09uy4pTP0NEaeIjtGuf1_dPORF-NEUw8iM6i3SjPbDmUhV3req8XNEeA1nwJSE67HeeWKbzA6VV1ot8SstCG2YJ_7pryugdWyCJKw8Nkb_qUZeGowiF8QWZj_h6d0k47BSX5foBhVSxJdUYYnaUYXrjuui66xpHtuLvCZGB2B3SDG9uLaKb7Hyd3BtRSGUnaTPL41gIBAn2amFsaOzj0JNLK4PesUg0ot2biK4ZG_rVXNiGfJ6zf5H7J2HV6VlKk4tm5hHPtr41zpzYeSZHpKk0LSJhtQJ5MjkO8dO7z4RRI2yZsA4qWsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008e331b03.mp4?token=qNuVIu_ca_wn85AuUv5TI5Dk7haTwem-vc6cbQGRdxrQ6byK5h0iDPAeEZihoDx7X43TeIQ_UBUi3vLrXeiRjjahmjy6IIPlJjZgNFzdCW7VFj1I2fD9nbo-h1BaYZqJGBrhK0qL0FDGFUerlBSw0Why-hiIVpPu_YU7iH62sfV6x_pOcM6rTAp4qcgMtrFev8xuvxULsHnm-fG6FBqzmWE-IEeVhs-LwlvrbAigeEHmNjHIfXRge3NJgnZvKYRZtUVHmije0I-CZfwwYn3jN3xGeueTvm3JkzEoTb_W6X6oPdkwYlYgkuU6dggmh0IGBKRyzpemV4P_5nJ_MWdOEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008e331b03.mp4?token=qNuVIu_ca_wn85AuUv5TI5Dk7haTwem-vc6cbQGRdxrQ6byK5h0iDPAeEZihoDx7X43TeIQ_UBUi3vLrXeiRjjahmjy6IIPlJjZgNFzdCW7VFj1I2fD9nbo-h1BaYZqJGBrhK0qL0FDGFUerlBSw0Why-hiIVpPu_YU7iH62sfV6x_pOcM6rTAp4qcgMtrFev8xuvxULsHnm-fG6FBqzmWE-IEeVhs-LwlvrbAigeEHmNjHIfXRge3NJgnZvKYRZtUVHmije0I-CZfwwYn3jN3xGeueTvm3JkzEoTb_W6X6oPdkwYlYgkuU6dggmh0IGBKRyzpemV4P_5nJ_MWdOEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای اعتراض به جنگ تحمیلی ایران در سن‌خوزه کالیفرنیا طنین‌انداز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/691449" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691448">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
فایننشال تایمز: سقوط ۹۴ درصدی تردد کشتی‌های کانتینری در تنگه هرمز؛ در برخی کشورها حتی کلاه ایمنی دوچرخه برای کودکان تمام شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/691448" target="_blank">📅 15:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691447">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: به همه کشورهای عربی و همه کشورهای همسایه می‌گویم اگر آمریکایی‌ها سعی کنند روابط تجاری و مالی ما را مختل کنند، ما دو کار انجام خواهیم داد
🔹
اول، ما قطعاً به شرکت‌های آمریکایی حمله خواهیم کرد - مانند شرکت‌های حفاری آمریکایی که به طور گسترده…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/691447" target="_blank">📅 15:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691446">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75fec65264.mp4?token=c549p-b9g7ZtXYVI0NJwvpbqGBz0SzmKtUnZ1l7hH-loRc-rgY3_sZnt6l2Gt-uusH1ocQBj6orTN60A4A3ZvSbk07gdcZpHSDedbK53hkxokmGumfg1L0nGOPbz6sp7lewM6QUQKZSqiDxOhSFiQPN5_LZ8Bt0rkIMG5sGifhllFHb3vdGb9yhVpJBM9YJoydDwcNIdgGC2o2pIEzhfJa00y9ErGfwvjZ7jeQ70_LsClyDy-GmmviB7cZ8fvcJuVku1DQfv6G67JicWq6tSiH7QXa5vtGHGfiYiUirmsaJeWueBpd5AMXAKCFHldXU_Jrseb3nd-rMBOiGREq74fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75fec65264.mp4?token=c549p-b9g7ZtXYVI0NJwvpbqGBz0SzmKtUnZ1l7hH-loRc-rgY3_sZnt6l2Gt-uusH1ocQBj6orTN60A4A3ZvSbk07gdcZpHSDedbK53hkxokmGumfg1L0nGOPbz6sp7lewM6QUQKZSqiDxOhSFiQPN5_LZ8Bt0rkIMG5sGifhllFHb3vdGb9yhVpJBM9YJoydDwcNIdgGC2o2pIEzhfJa00y9ErGfwvjZ7jeQ70_LsClyDy-GmmviB7cZ8fvcJuVku1DQfv6G67JicWq6tSiH7QXa5vtGHGfiYiUirmsaJeWueBpd5AMXAKCFHldXU_Jrseb3nd-rMBOiGREq74fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه ترکیه: ما قبول نمی‌کنیم که عربستان سعودی به عنوان بخشی از درگیری جاری بین ایران و آمریکا در نظر گرفته شود
🔹
عربستان سعودی باید از این معادله جدا نگه داشته شود، زیرا خودشان تمایلی به دخالت در آن ندارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/691446" target="_blank">📅 15:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691445">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=jyz3QMzhm_1Dee6UWcI7-SkA7kJeyjgYi3EZR3JqOe3xYd8qUxyV3ll_G5WPpsfqgZs17Suy-j00q12CwiLmFIahLmY0LkYhn4s2snCe7sWlywCeICL7HR9bxavV4i1V8h5y3o9v-rXsJ9xNwMJYzk6l4kKMv4L4Bucpf8i-aRu4DE9mlD2MSynlt1Vw_Z-Xx4vQpCl7EQm-lOdueV9cNeNVg9-FQaHYbGkezfMLNuM-CSOHflQevhETHC9XrH2Odv3rPtVNRJZMN_suwEvj31muWz3eUOdMzUES33FAlEzZZfpETB0sf85srGXi2E8yRgh1tCPAjUZnpNW49qZIeCv8Rtzj2mqxB5SdKSRgBfPUo_EN8-mZ-7ZdR1ZVwLHVi4tg2mOC4RLCDo5h9WiEbtsA1mEjgFELXdwQzN9EyEO6RPupXhVdSpv5dFiioXah0dWbVZ-LDquEB0-YS7aE43EYCfm-g7fjj9us_Q0PIO9qE2nquivqvXLS2h238fyLqVPjck4i1tzY7ScMQ7eCQ-thDuy_ni1VQSPUzMlXO6IsSkO__BOGuOgGlMObxbPpWhjJfY3D-z28PyUapacRkkd9aRbU-mixP1JCpMf1L3AqbGYcE4k0iBnt9izk8681eumPtLRaBigB93qvcPJ8872Z5QfzE_rtK95VurLPNfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=jyz3QMzhm_1Dee6UWcI7-SkA7kJeyjgYi3EZR3JqOe3xYd8qUxyV3ll_G5WPpsfqgZs17Suy-j00q12CwiLmFIahLmY0LkYhn4s2snCe7sWlywCeICL7HR9bxavV4i1V8h5y3o9v-rXsJ9xNwMJYzk6l4kKMv4L4Bucpf8i-aRu4DE9mlD2MSynlt1Vw_Z-Xx4vQpCl7EQm-lOdueV9cNeNVg9-FQaHYbGkezfMLNuM-CSOHflQevhETHC9XrH2Odv3rPtVNRJZMN_suwEvj31muWz3eUOdMzUES33FAlEzZZfpETB0sf85srGXi2E8yRgh1tCPAjUZnpNW49qZIeCv8Rtzj2mqxB5SdKSRgBfPUo_EN8-mZ-7ZdR1ZVwLHVi4tg2mOC4RLCDo5h9WiEbtsA1mEjgFELXdwQzN9EyEO6RPupXhVdSpv5dFiioXah0dWbVZ-LDquEB0-YS7aE43EYCfm-g7fjj9us_Q0PIO9qE2nquivqvXLS2h238fyLqVPjck4i1tzY7ScMQ7eCQ-thDuy_ni1VQSPUzMlXO6IsSkO__BOGuOgGlMObxbPpWhjJfY3D-z28PyUapacRkkd9aRbU-mixP1JCpMf1L3AqbGYcE4k0iBnt9izk8681eumPtLRaBigB93qvcPJ8872Z5QfzE_rtK95VurLPNfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی
:
به همه کشورهای عربی و همه کشورهای همسایه می‌گویم اگر آمریکایی‌ها سعی کنند روابط تجاری و مالی ما را مختل کنند، ما دو کار انجام خواهیم داد
🔹
اول، ما قطعاً به شرکت‌های آمریکایی حمله خواهیم کرد - مانند شرکت‌های حفاری آمریکایی که به طور گسترده در اطراف ما فعالیت می‌کنند
🔹
از سوی دیگر، ما به کشورهای همسایه نیز می‌گوییم: با آمریکا همکاری نکنید، زیرا ما به طور مشابه پاسخ خواهیم داد.
🔹
اگر یک کشور همسایه با آمریکایی‌ها در اعمال محاصره اقتصادی علیه ایران همکاری کند ما کشتی‌های آن را در تنگه هرمز مجازات خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/691445" target="_blank">📅 15:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691444">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gth2LoGGPfVUFj_hH_vykMEtfAUJsQQKBxk2j2Ef-1oJB9f-33EffAkvhiarN9MaIMPJCWeLBu5rkj-P22igDg4jEWQUaLu3Osx0Db7Nv_OcRmIBPEWWDPjPFnDsW4NhjEVGxXjbJqFaE-wfXDgZbdqEAKcIJDkLE-QXc9-EJcYxoeu-YmWpqyn90U0B9IuNosv3r6sjanxwEo2hJkcOCDchWhBse0LApLIDfbaajUqjeZ6S64u8hZhex4quVqXdEOGoWUQWzjRO9PE5Ic5a07novaougupulc9ksaklCVOXIcr9R97NgK1NEJr4HKXQCMYRxzOmy1AAImI48BozeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت یک سقوط | کوچ اجباری از گوشت قرمز به مرغ | سفره ایرانی چه چیزی را از دست داد؟
🔹
سفره خانوار ایرانی در دو دهه گذشته فقط کوچک‌تر نشده، بلکه ترکیب آن نیز تغییر کرده است. آمارهای مصرف نشان می‌دهد گوشت قرمز که زمانی سهم قابل‌توجهی در سبد غذایی خانوار داشت، به‌تدریج جای خود را به گزینه‌های ارزان‌تر داده است؛ تغییری که نمی‌توان آن را صرفا نتیجه تغییر ذائقه دانست.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3246556</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/691444" target="_blank">📅 15:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691443">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
جنگ در کمین انگلیس؟  بی‌بی‌سی:
🔹
دولت انگلیس از شهروندان خود خواسته است که مواد غذایی کنسرو شده و آب آشامیدنی ذخیره را برای جنگ احتمالی با روسیه آماده کنند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/691443" target="_blank">📅 14:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691442">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI-LITfnuw6rj9XrgghQzazrFY2CAKNBCpXcs30B7WRCY7WPJruDQqT7wxVJYebpUIimTj1VNjce-jLLXPWXToYt4-gv2F9pDt5WYj_HouvP4RDpBxuMLy7YFisNc0xRsZKOIcNHE0IWHHzauHL5lJzro_QiAqDkyFiyQtUatXuYoWe3Eyod8LghI5ZadsuHeCf1b7fQBFYYYKiAFD2Ndoyw7BTkITUryBADxt2RLPgGISev_cmpnzS-TMHedX3_p8ez3zHZZO9hdgt-Bwo18aoowkxd1QcrZgN3ZXk0mwDRmmQNcwhemx6b7Z5yneGYroCej1-VYyXRlBtKH4Touw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر برگزیده رویترز؛ حضور سربازان انصارالله در کنار جنگنده ساقط شده سعودی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/691442" target="_blank">📅 14:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691441">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
مصرف سبزیجات، لبنیات و میوه‌ها در مردم کاهش یافته
احمد اسماعیل زاده، مدیر کل دفتر بهبود تغذیه وزارت جامعه بهداشت در
#گفتگو
با خبرفوری:
🔹
بحث گرانی که اتفاق افتاده دامن‌گیر اقلام غذایی نیز شده است و انتظار این است اقلام غذایی مصرفی خانوارها مقداری کمتر شده باشد؛ به ویژه میوه‌جات، سبزیجات و لبنیات.
🔹
سبد غذایی مطلوب را در سال گذشته منتشر کردیم. تا قبل از این اغلب اقلام غذایی در قیاس با آن سبد وضعیت مطلوبی داشت و کل کالری دریافتی مشکل چندانی نداشت، اما در حال حاضر با توجه به گرانی ها احتمال می‌دهیم دریافت کالری پایین تر آمده باشد.
🔹
اقلام غذایی را که برای تامین مواد مغذی برای ما مهم است به وزارت رفاه معرفی کردین که حتما در کالابرگ گنجانده شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691441" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691440">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcHnFyFmK9MAyr4gAB0bURfO5sUSIZ9RwFH8XebS0cLl5qWmEguyN6pvIHAa7BNC1KsvLShvv0U0UNXnADDdVOxOGHWHTm2fj4_Drsg8UVR6XIZxytsOChhX3i8P4cSmN2Io1lWM-_zoUUoROV89mjKvELRFH1jIGr-m8p59SruZqhUAYIVPlgVNw3Q_3kIWLfFtwIZ5ifnjdFDj3yhvNvtakjzlWLFvvR1U7tMppeq5CvK48r2P5eMGQImcVU8wYMRJUqdlcfPHMVseKVpOyD1GDZsPUcuUmA97F9Lf4YsDGRFLY01kS6DpB9ncEUNkupBJcHA-vH2rEsmzC9nBkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کف قیمت موتورسیکلت به ۴۰ میلیون تومان رسید
🔹
قیمت ارزان‌ترین سی‌جی ۱۲۵ کارکرده به حدود ۴۰ میلیون تومان رسیده؛ یعنی یک کارگر برای خرید آن باید حدود ۲.۵ ماه کار کند. قیمت برخی مدل‌ها نیز به ۳ تا ۴ میلیارد تومان رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/691440" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691439">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq6e-QWhptYY1dJU0oxwDvYtCw3Y1i0SVkXoN-KBLvFFlt_uiYZLrdjRDFSYCKiI749hEZGB93kwWNHl2QfWnb8x1XNFQbeDPVCzLZwEpb9pWW7TgrrzLLiM0TPxEjwa-TXEe5WUyHEw4NLUCCHVpHh7BE92-1tRhnCCwmC3_Y0uSOkdUFmrO_sRE7PRoP8iSOLk28FjKzh4R4_vWnFMfgcSQ3hIBT-7Nm14faHRiiz0ifnHLJhFKhNON0KRZP46kpb_TUt3qt2g7_dgyVOolvha3RPxmzLw_J8QaozBcrd48Fp8s67wlL8WXT6PPpe96zRWQzcbAS7xYjLSXcN95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست شقایق دهقان برای شهدای دانش‌آموز میناب: امسال ۱۶۸ نفر غایب هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/691439" target="_blank">📅 14:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691438">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادعای یک رسانه اماراتی درباره جزئیات بسته پیشنهادی ایران برای کاهش تنش با آمریکا
ادعای ارم‌نیوز به نقل از منابع غربی:
🔹
ایران توقف غنی‌سازی بالای ۵ درصد
🔹
آزادسازی بخشی از دارایی‌های بلوکه‌شده
🔹
بازگشایی کامل تنگه هرمز را پیشنهاد داده است
🔹
این رسانه همچنین مدعی شد آمریکا همزمان برای حملات هوایی و موشکی احتمالی به اهدافی در ایران آماده می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/691438" target="_blank">📅 14:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691437">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
پزشکیان به نیویورک می‌رود
🔹
بر اساس برنامه فعلی، مسعود پزشکیان برای شرکت در مجمع عمومی سازمان ملل به نیویورک سفر می‌کند و ضمن سخنرانی، با برخی سران کشورها دیدار و رایزنی خواهد داشت. یک هیئت بلندپایه نیز او را همراهی می‌کند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691437" target="_blank">📅 14:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691436">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1c8fb3e26.mp4?token=O8h2q7Z_pGjoJFlXm1emO-nkyjPpad8dl6jSvQNiZBP3qNqcworits0kTtRyRIcJXpB4QyUVuopuy4tHZXozGTJoOLp6w5f0_tqcig5TnRZ9qy96lCDXY6agkH_0Q5nJSxP3FL9kdecoLDFuwXrtcGjso7b6lv5Ay6srATgug8Ox2NYfoyd8FCOf8GyFJqH13Q7uTUKBrhTJB3SDBzGX1x5_0SW-5EKb6gN2sOEJuCfZVjo0TNcs_c4CHesnemsdlylWGbBy3VgPq6HebhjmpLnMMD8bkdEiFDG5f13ZCyId46AKVdamNhDKP-ZwDpECOFTiacYJGsG1yJJprH2PEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1c8fb3e26.mp4?token=O8h2q7Z_pGjoJFlXm1emO-nkyjPpad8dl6jSvQNiZBP3qNqcworits0kTtRyRIcJXpB4QyUVuopuy4tHZXozGTJoOLp6w5f0_tqcig5TnRZ9qy96lCDXY6agkH_0Q5nJSxP3FL9kdecoLDFuwXrtcGjso7b6lv5Ay6srATgug8Ox2NYfoyd8FCOf8GyFJqH13Q7uTUKBrhTJB3SDBzGX1x5_0SW-5EKb6gN2sOEJuCfZVjo0TNcs_c4CHesnemsdlylWGbBy3VgPq6HebhjmpLnMMD8bkdEiFDG5f13ZCyId46AKVdamNhDKP-ZwDpECOFTiacYJGsG1yJJprH2PEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین ۹ ماهواره را با یک موشک به فضا فرستاد
🔹
چین با موشک «لیجیان-۱»، ۹ ماهواره را با موفقیت به فضا پرتاب کرد؛ این ماهواره‌ها برای پایش محیط فضایی، مقابله با بلایای طبیعی و آزمایش‌های علمی استفاده خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/691436" target="_blank">📅 14:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691435">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
سفارت چین در عربستان از شهروندان و شرکت‌های چینی خواست با دریافت هشدارهای امنیتی، فوراً به پناهگاه بروند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/691435" target="_blank">📅 14:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691434">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIdlRMAONZKilPyKn1xzxkRJk_fIaB5Xszx3TZmT-NoA7azA6MHGG7VreWNP71rC3gd5Qf73dcibwN2HrvUuLik_qMjLFCmefFQsCC2F43qjJW2rC4vwODLAyb9RtC6CipEOydiBFN0gVmuB-149LIpNlTIWp4uzg9CDOTsylXTC3v0u_TqFNSsHOeyYQWeblAMyJgQ1PPS5rz16CUZbX7aKPUpcLNWUlNRFjvLUJu4FfKXF8AT04NDf4y2J-pUcarm9ZTtV0vAvpiTrN7ti6mEHfsYRyyHZJyazlbH8Y-CR3Q48Fvj3t1ms83sNxmKQD5Ut5AafA2yQZQKf4uzdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲ الی ۱۴ مهرماه؛ برگزاری هفته فرهنگی ایران در روسیه
🔹
کاروان میناب۱۶۸ متشکل از فعالان فرهنگی هنری به روسیه می‌روند
🔹
دیوسالار معاون توسعه همکاری‌های علمی و فرهنگی سازمان فرهنگ و ارتباطات اسلامی در نشست خبری: هفته فرهنگی ایران در کشور روسیه از دوم الی ۱۴ مهرماه با سلسله برنامه‌های متعدد فرهنگی برگزار می‌شود
🔹
این برنامه ذیل اراده مقامات عالی ۲ کشور شکل گرفته تا روابط ما در ابعاد مختلف رشد پیدا کند
🔹
این هفته فرهنگی با گستردگی بیشتری نسبت به قبل برگزار می‌شود و قوام‌بخش روابط دو کشور خواهد بود
🔹
این بزرگترین رویداد بین‌المللی کشور در خارج در دوران جدید و بعد از جنگ تحمیلی سوم خواهد بود
🔹
کاروان ۱۶۸ نفره متشکل از چهره‌های علمی، هنرمندان، فعالان فرهنگی و هنری و ورزشی، فعالان حوزه صنایع خلاق و صادرات فرهنگی در قالب کاروان میناب۱۶۸ به روسیه اعزام می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/691434" target="_blank">📅 14:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691433">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
دولت کویت مدارس ایرانی فعال در این کشور را تعطیل کرد
🔹
مدارس ایرانی مستقر در کشور امارات نیز سال گذشته تعطیل شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/691433" target="_blank">📅 14:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691432">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
در کشور ۱۸ تا ۲۲ درصد زنان در سن باروری  مبتلا به کم خونی هستند
احمد اسماعیل زاده، مدیر کل دفتر بهبود تغذیه وزارت بهداشت در گفتگو با
#خبرفوری
:
🔹
مکمل یاری با آهن را پیگیری می‌کنیم. برنامه غنی‌سازی آرد با آهن و اسیدفولیک دارد اتفاق می‌افتد.
🔹
با همه این‌ها آمار کم خونی زنان در سن باروری بین ۱۸ تا ۲۲ درصد است. به نظر می‌رسد در این حوزه باید ابتکارات بیشتری داشته باشیم که برنامه‌ها اثربخش باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/691432" target="_blank">📅 14:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691431">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
هشدار قرارگاه مرکزی حضرت خاتم‌الانبیا (ص) به آمریکا و کشورهای منطقه: خطا کنید هدف حملات دردناک قرار خواهید گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/691431" target="_blank">📅 13:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691430">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSKVXosGD9hz8aM6tmda84VN8suF8BI2-Masqw3vpSWbJhJQtw7sobXBsMTP-eoM8uxFz_lUnpUSHjiugavfCYswPNyfvnf8CNGZC6JavkrTTLHYGqtdEsrRyf37XGJ4nlDQuYiRQJ3HyrbMFumF_2w8daMf5p0WxoKPbFFuKtQssf_ya8aJ3p15vFZIxsZRXcHZM_SwX6Ra3VWaOVBJUwKSYiTtye4CtIeZtMax8dALlEi1LhkkVaTJXEP6QGWJis5RaB9KMUCYu4_FdaCsQn3ozXcwbvSY41i6XrkJ8x_Oa7tVeWyJrflOs-cgKTYy9fhLkswaRv6mVQvIgFimnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای شبکه فاکس‌نیوز: در تأسیسات هسته‌ای طالقان فعالیت قابل‌ توجهی دیده می‌شود
🔹
شبکه فاکس‌نیوز با انتشار تصاویر ماهواره‌ای از تأسیسات هسته‌ای طالقان مدعی است فعالیت قابل‌توجهی در این محل دیده شده و یک سازه بتنی روی آن ساخته شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/691430" target="_blank">📅 13:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
۸
استان دارای بیشترین مدارس آسیب‌دیده در جنگ
رییس سازمان نوسازی مدارس کشور:
🔹
استان‌های هرمزگان، مرکزی و شهر خمین، آذربایجان شرقی، آذربایجان غربی، فارس، اصفهان، کردستان و کرمانشاه از جمله مناطقی بودند که بیشترین آسیب به مدارس در آن‌ها گزارش شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/691429" target="_blank">📅 13:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سازمان تأمین اجتماعی: واریز حقوق شهریور ماه بازنشستگان از فردا آغاز می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/691428" target="_blank">📅 13:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691427">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJy_Pm5OTMlLtgeOIfsDHfBkxxlqei_r2_SQR1gNlNIOP2UrvsS4cksFUudTpO5N6zXA3DKlIVWn-NlDKby0gpKIpuW79eM_-o3UVUlUQAWATldscPuTUfq7ZR-ftynWWBYtFAAJObDu7V8OXcMSOdrfRwgU02k3zt2S-AJCOovuLb1q4MGRIMkruAyuEc26WJEmJrB04DZ2in_5nsthbOqnvxppbtrKmo8tOdeLRbEb593jxkr8_aE4YTijeBlpmC_l44yAItwEhAEodvCLeuMxa_55zFAsuiNl9KPv08_GTn4nAu8fInSOFAhzXGh2-bzrjvllngTd6szGtCtvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پک ویژه سوغات رضوی
یک هدیه معنوی و ماندگار از مشهد؛ ترکیبی از عطر، مهر، قاب‌فرش و تسبیح رضوی برای کسی که می‌خواهی یاد حرم را با خودش داشته باشد.
🤍
داخل این پک:
🌸
عطر گوهرشاد — ۸۵۰,۰۰۰ تومان
🕌
مهر تربت مشهد — ۱۸۵,۰۰۰ تومان
🖼
قاب‌فرش ۱۵×۱۵ — ۱۵۵,۰۰۰ تومان
📿
تسبیح رضوی — ۲۰۰,۰۰۰ تومان
جمع قیمت اصلی: ۱,۶۳۲,۰۰۰ تومان
🔥
قیمت ویژه پک: ۱,۳۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
قرار؛ تجلی هنر و ارادت
@ghararshop</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/691427" target="_blank">📅 13:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691426">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUPqGfRP4TzqGSilfr6Ft91mCiRkbNw3bVSuMFDakuJ9h6Bl-cwJjX30N-vTubcBRxl4kCI9Ev8AVDM4ej9zBMig449r6szm_UCFcfkUCcnwpy749kvW4tEbpr053kSv6cOUuRwET64bCfXPcKGG_v_qtIBOtfIYrYBsSQqNhAdpnOHhbw7ynP3KovPuqr8c542z5nFHnAkG67ZAOuMV1LaDWjl8SsZrEnWFYnYsDFPDH2HyJ3syqClkkilKXo63cVktSpChaDtu-InPXMN4YknUSK-44_Wr4d4FMA-AorrjYuAhYnbU2uN3T5CcPzmBh6QS-RWTk1aRAjBSws-ztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت اطلاعات: سه کانون عملیاتی وابسته به گروهک‌های تروریستی که قصد عملیات ترور و تخریب زیرساخت‌های اقتصادی را داشتند در ۳ استان ( کرمان، آذربایجان‌غربی و البرز) به هلاکت رسیده یا بازداشت شدند
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/691426" target="_blank">📅 13:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691425">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
وزارت اطلاعات: سه کانون عملیاتی وابسته به گروهک‌های تروریستی که قصد عملیات ترور و تخریب زیرساخت‌های اقتصادی را داشتند در ۳ استان ( کرمان، آذربایجان‌غربی و البرز) به هلاکت رسیده یا بازداشت شدند
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/691425" target="_blank">📅 13:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1048d146b.mp4?token=vUIQkYnJtZGzozQ9Fc9hLbOMuhWP-uQW8gRgr_sfwKHCwhdS8BrgfrgXMVKpg1TBXrEwez33J4Mt841Qr63GgQyGmIH0OUMEC73x5kF3I-Se8hYE1HkUOmMfTy02xyip_kS4A5sfgLHPGFlBuxrUPSJWpMTnQqiAgdrIga60bXkPSAuPi90DWcX5I6ZNIHF2UNPuWeeDd_H-kN6v2Vyc2wRS0x2PgAS0UwLWD_Su8tI-fS0snY6Sou0txAB80wsQOijFXdATFX-dXpVMD6s-I1gjRtEgPTl-TtZEXZ31wFMKcOK3BKTa948VtPYRNG1DOhVh2-9v_xoAWf0AhMjRfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1048d146b.mp4?token=vUIQkYnJtZGzozQ9Fc9hLbOMuhWP-uQW8gRgr_sfwKHCwhdS8BrgfrgXMVKpg1TBXrEwez33J4Mt841Qr63GgQyGmIH0OUMEC73x5kF3I-Se8hYE1HkUOmMfTy02xyip_kS4A5sfgLHPGFlBuxrUPSJWpMTnQqiAgdrIga60bXkPSAuPi90DWcX5I6ZNIHF2UNPuWeeDd_H-kN6v2Vyc2wRS0x2PgAS0UwLWD_Su8tI-fS0snY6Sou0txAB80wsQOijFXdATFX-dXpVMD6s-I1gjRtEgPTl-TtZEXZ31wFMKcOK3BKTa948VtPYRNG1DOhVh2-9v_xoAWf0AhMjRfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میکس‌های محبوب قهوه را بشناسید؛ هر
ترکیب، طعمی متفاوت
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/691424" target="_blank">📅 13:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691423">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
حاجی‌دلیگانی: طرح سه فوریتی خروج از NPT تقدیم هیات رئیسه مجلس شد
حاجی دلیگانی، نماینده مجلس:
🔹
با توجه به شرایطی که کشور دارد و تهاجمی که دشمن در ۲ مقطع به ما داشته، ماندن ما در NPT جز ضرر چیزی برای ما ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/691423" target="_blank">📅 13:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691421">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_L-vcuMkXyt2dZT52EuQsBbHxPOjpYBWfaBEKP2P74mirEn33UmMCBhfEtvCTXeOfee7r1rYtrXC6oYuYF2jMqDP_8f7P_knvB8lvsQL31EbGEAKSJnbozoYMZVVfpNIKrrlFjWInCqT8m20S3mXWtjO88z0uqEAkv2jNGVkdzAOqnGI_Zy-vogmq8_kvU-iaWzWFtenozIhIcKPpzIEX9NWgkcvdo-AnOfaK6eEy0Ib4p9ZeIcFfyRpi_s7ZsOXVeXD1GVoBj18kvHrRE7h6eyhi8P4pcUC51fpFyp6Y1NUcjZOQpuUYFfPY8IpPZM0kzZudxHJBJ-fJCT9frMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1F0N76uzgbRgR_cRKdRaIUJmxjnuiKBd7Z-fbWPeemha3B-PxIHZjA_tCJ1yrW8GbbysvrZtSwBONf94Gy6-XfeFNq5vxhNeKlu37A34w3L6cFbu3KIKfy8ICWF1Gi96Y6TQHxjzHkIiKLCZIqgvdin2PNSsGJoTRiHKO5o5F47aw-YZ8Px4GmDgfaJpmw3iGphLqYSiXRwWceev2TFKcRw52Nrm1L0jdfhYhD7zK1WYqOaRbyZEkKN_I2OX7bJYnOlXFLjWS3eJKBaRRvh9rIef0pFqw99YQz7vjseabf3i1RY8HiVMBbugWn1Rjv0PZ-q1tHy3l97-NB6woRcTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دکمه های کهکشانی/ یک ایده خلاقانه برای متفاوت کردن لباس‌ها
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/691421" target="_blank">📅 13:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691420">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAuBC0KROSJz6IkSQx70OVk7gayglUS1SgLCvL0Q-7qCahZDghcPk9pMo3jz20rns4fRB_61ToJhMmPQqc6f2l3PfaWqO8y2XoltMcXjR0iziXjjpPiUt7GsAqSYoUyfV7h2GVsQA6d90HQ5iDjoP2JNo05j9zKJu1C63ltMJUnLoynWKhypQ2G6MC8JHC0_sTc33o0KPyPaq0a88WZgYOwNq-ATxoTg0nAmNDyMwr1pzYLRO9AXH_mQQ5eUfpB011RSSyrCJ1YvXxK3lSn3_UAkYjjtT1FVDfRtgXFHUlN85r9vZydDUfgOx7QWwQEoxgs6pvbe7Gres2ynlB8KoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: تجمع ۳۰۰ هزار نفری در تهران و آغاز جذب نیروهای داوطلب
🔹
به گزارش The Independent، بیش از ۳۰۰ هزار نفر روز جمعه در تجمعی سازمان‌دهی‌ شده در تهران شرکت کردند؛ تجمعی که در آن آمادگی برای دفاع از ایران و آغاز آموزش‌های نظامی اعلام شد.
🔹
به گفته این رسانه، بیش از ۶۰۰ هزار نفر برای طرح «جان‌فدای ایران»  ثبت‌نام کرده‌اند و انتظار می‌رود شمار شرکت‌کنندگان در آموزش‌های نظامی به بیش از یک میلیون نفر برسد.
🔹
تا ماه مه بیش از ۳۰ میلیون نفر از جمعیت حدود ۹۰ میلیونی کشور، به‌صورت آنلاین یا در تجمع‌های عمومی برای فدا کردن جان خود در راه حکومت ثبت‌نام کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/691420" target="_blank">📅 13:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691419">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d3fe8bc3.mp4?token=meEGa3V8ICAHTltQU_oLkOWTf_eBrlDx81SEaCAI090CrOu8yy18kEcY6WQTkOYZZ6PyQKMaO4Fw7MOhYwNouYPy-SjNoZT4TNdXcEvhm-3PvWZ5UpElnqjhxu8yYbfHuIXQbaG73OxQ_-cUg7XuX4bty1_cD_CYbsIR6AmVOimN7Pc4wMwjY9CspILiYd8nMF_7E87dx9Pfx_verURAmifxHGAkv9wcEAJhuyHHTa7YccDZn3eHyonRpEOijEJDDELgjClf5s_6R8EdwFHqOFDz2pjsklRcMPHwbrgLT7BPptuO8SzVaHe_FNJI6vhkGZdKb8mr9XqROkrjBxgitw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d3fe8bc3.mp4?token=meEGa3V8ICAHTltQU_oLkOWTf_eBrlDx81SEaCAI090CrOu8yy18kEcY6WQTkOYZZ6PyQKMaO4Fw7MOhYwNouYPy-SjNoZT4TNdXcEvhm-3PvWZ5UpElnqjhxu8yYbfHuIXQbaG73OxQ_-cUg7XuX4bty1_cD_CYbsIR6AmVOimN7Pc4wMwjY9CspILiYd8nMF_7E87dx9Pfx_verURAmifxHGAkv9wcEAJhuyHHTa7YccDZn3eHyonRpEOijEJDDELgjClf5s_6R8EdwFHqOFDz2pjsklRcMPHwbrgLT7BPptuO8SzVaHe_FNJI6vhkGZdKb8mr9XqROkrjBxgitw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسکتبال ایران با شکست چین، برنزی شد
🔹
تیم ملی بسکتبال ایران در دیدار رده‌بندی بازی‌های آسیایی ناگویا با نتیجه ۷۰ - ۷۹ مقابل چین به پیروزی رسید و به مدال برنز این رقابت‌ها دست یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/691419" target="_blank">📅 12:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691418">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd62af64b8.mp4?token=Pkr-TOdKQtlRzdD3_rnJeQBBsQG0ZZPjePJ9BgUcsy2b8_D8Fdx9lur-mXMM6UyogTy5NjPIGBATw9vNnXXc_VGy7F3HpvVjEImT2o0ljeEK7rZHeXct5em2j4_x-UV0OQ9P2x1_uOMqWKFxWG5p7cLVw0nVzSQ7U10b7SEXhRzEvZXUsAuDH0JA-QZ-JvNmbU4M2MgFAEhOTw7BRTTqMalq3TSQ7ZqSpExG97XHunMOcd-G8cEj82qarQni51RY_3Vk5Ef0Xi0mqOVp4TfLi-LVxgdpSkpl2_sQVyEkZQnrVrVS7SUp7Y3smJBNh0DHq_gQrgdDmpYDHBMXuUbBtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd62af64b8.mp4?token=Pkr-TOdKQtlRzdD3_rnJeQBBsQG0ZZPjePJ9BgUcsy2b8_D8Fdx9lur-mXMM6UyogTy5NjPIGBATw9vNnXXc_VGy7F3HpvVjEImT2o0ljeEK7rZHeXct5em2j4_x-UV0OQ9P2x1_uOMqWKFxWG5p7cLVw0nVzSQ7U10b7SEXhRzEvZXUsAuDH0JA-QZ-JvNmbU4M2MgFAEhOTw7BRTTqMalq3TSQ7ZqSpExG97XHunMOcd-G8cEj82qarQni51RY_3Vk5Ef0Xi0mqOVp4TfLi-LVxgdpSkpl2_sQVyEkZQnrVrVS7SUp7Y3smJBNh0DHq_gQrgdDmpYDHBMXuUbBtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه بیماری‌ها از سرماخوردگی ساده تا سرطان التهاب شروع می‌شوند!  #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/691418" target="_blank">📅 12:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691417">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای ان‌بی‌سی: کوه کلنگ هدف اول آمریکاست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/691417" target="_blank">📅 12:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691416">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: در جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند
هدف قرار می‌دهیم
رضایی در گفتگو با الجزیره:
🔹
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا — مگر اینکه اقیانوس هند را ترک کنند — در هر نقطه‌ای از این اقیانوس که باشند، هدف حمله قرار خواهند گرفت. ما به این توانمندی‌ها دست یافته‌ایم
.
🔹
ما سرعت موشک‌های هایپرسونیک خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم. همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تدابیر دیگری نیز در اختیار داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/691416" target="_blank">📅 12:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691415">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba30f7bb3b.mp4?token=eX4PjRJHOEtg8pEBnVTYaiZUjZaVGQHkSMaRYP2b57mOW2Q1KCEZ-uBSzPxcpjLAy7jS5HyEDmVm-d54eSZmYAmr2qjMj6PlswgAu15KXFBNLtqDrCWn8RZlKl5p1wD6hZQ7kTBwZ5SNL_FsEYkKEbwtzf8iTdlU9CEbDktCNndUfFx3VpMd9fdJ992NbMBDj-F39lRPgooOQt5eeqURVTlZfNCcnegmW5HVgmB7mwDGPgEbYJWXkrig6SZaQb7-s8zyfyRaj7oGM6rA0sOSu1Px6PiGRoEzAWVnya_Ia-eRaCj5q85G4UsMgW39eKN__4-Ii93Z683QxvMmjhHEJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba30f7bb3b.mp4?token=eX4PjRJHOEtg8pEBnVTYaiZUjZaVGQHkSMaRYP2b57mOW2Q1KCEZ-uBSzPxcpjLAy7jS5HyEDmVm-d54eSZmYAmr2qjMj6PlswgAu15KXFBNLtqDrCWn8RZlKl5p1wD6hZQ7kTBwZ5SNL_FsEYkKEbwtzf8iTdlU9CEbDktCNndUfFx3VpMd9fdJ992NbMBDj-F39lRPgooOQt5eeqURVTlZfNCcnegmW5HVgmB7mwDGPgEbYJWXkrig6SZaQb7-s8zyfyRaj7oGM6rA0sOSu1Px6PiGRoEzAWVnya_Ia-eRaCj5q85G4UsMgW39eKN__4-Ii93Z683QxvMmjhHEJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«مرغ شاخدار کرکسی» پرنده‌ای زیبا با پرهای آبی خیره‌کننده و گردنی شبیه کرکس
😍
🔹
گردن طاس کمک می‌کنه در اقلیم‌های گرم و خشک گرمای بدنش رو بهتر تنظیم کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/691415" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691413">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای هگزث، وزیر جنگ آمریکا: گزارش تلفات نیروهای آمریکایی دروغ است چون می‌خواهند ترامپ را خراب کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/691413" target="_blank">📅 12:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691412">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Em0evChjS8lTAFNWhF17CCANvU-7cfs6cMUsttXt6jtx_q9gjWOSvIhjylme8eedUYMJmZ0Ig7arZGIbLl3kpYoetWSmesxNCSAGTNZI0o5oHsyuQkM2IfVrjxaS5w61a4yCV8eb3WJ7lyGSk4D6lN-nvx1ehEX4zQQza-yfCReOKhWSL-ju8cfbMuds0xzoSMMqDLaojcW1nhUmba5opnJQ0hvKj6OqIDLsgUxOCXiO93HaRCFCiPPOIKsAlSIzAovw-lNAho8h_gZrOZjYZd-bhz9fR0mZPX-tFZ_ftRn1zc6GMSzy4bTcjXm4_ykgKoqyzCrTNcrMItaoqHWc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو
قطعات وارداتی شامل:
کیت‌کلاچ، لنت‌ترمز‌،شمع،وایرشمع،تسمه تایم،تسمه دینام و...
مختص خودروهای داخلی
شروع طرح: یکشنبه ۲۹ شهریورماه
ثبت سفارش با محدودیت کد‌ملی
تحویل رایگان از ۱ تا ۳ روز کاری از طریق پست
💳
امکان دریافت نقدی و اقساطی
🌐
متقاضیان گرامی جهت کسب اطلاعات بیشتر و درخواست اقلام می‌توانند به وب‌سایت ایرانکو مراجعه نمایند:
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/691412" target="_blank">📅 12:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691411">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a98dfefe4.mp4?token=lIFIlikopyigcN7ZkLQCFSFejY6M7NWnJ8ytbEsN9mZyVrKlSyhLf3snrbu9D3OwtoT14zf8R-6sQFG82y9NHGb7cR6_qkG9xn7eJv1jdoIlwnaMCsd0RSDSVJkl8lzbHW_G-92AdJjH1yTdu8TY45IpCm4ct1Z4_01-JRn8a-OdSQeu5HQonp5Rl7exkqkwA1OeFoTVBOMmzI44hXptQxLEZCZhefSsKiwU1bhLWj0kPILJAjDXG7qCfeWbSkhQbbUNhJVDBc4iYIDYL2MuSH2VcW6Yzj2Mn1fpXjmGwkefhW1Dn6haLUT98aStQSrtmAFvKes0PB0TeCF9CgncGz8WD0e1gRBCLE5fJJMBhK95CiB02aiLfDseIop0rP7frG3nqxjTvHpPhfwXoo4Ry-e8qZU4lemqINCatSkxCGHRT65OI151VsAtV3yk7jwSE6Kqbn29HIJTaUX7Wunn5qxj6Qk0_T0m2Qq6qIn3J1OWDsAUh3W2PatLfDhd19W8BUFz30vpRZLnsobF2k2rRN3ZP-42uqJQdoqaVi9XGmwl2Wwrd1Rkm75-hd7uObmEs8LFuAisGijvrrGJaDOOGL3EsDx1jV7bMkBK6LxysLn4QyzUdCH9Pw_61nW6k6UoS9xMDurBV9bY-NGYxgIUlWEnL1YSUNkwywoSv5HSj94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a98dfefe4.mp4?token=lIFIlikopyigcN7ZkLQCFSFejY6M7NWnJ8ytbEsN9mZyVrKlSyhLf3snrbu9D3OwtoT14zf8R-6sQFG82y9NHGb7cR6_qkG9xn7eJv1jdoIlwnaMCsd0RSDSVJkl8lzbHW_G-92AdJjH1yTdu8TY45IpCm4ct1Z4_01-JRn8a-OdSQeu5HQonp5Rl7exkqkwA1OeFoTVBOMmzI44hXptQxLEZCZhefSsKiwU1bhLWj0kPILJAjDXG7qCfeWbSkhQbbUNhJVDBc4iYIDYL2MuSH2VcW6Yzj2Mn1fpXjmGwkefhW1Dn6haLUT98aStQSrtmAFvKes0PB0TeCF9CgncGz8WD0e1gRBCLE5fJJMBhK95CiB02aiLfDseIop0rP7frG3nqxjTvHpPhfwXoo4Ry-e8qZU4lemqINCatSkxCGHRT65OI151VsAtV3yk7jwSE6Kqbn29HIJTaUX7Wunn5qxj6Qk0_T0m2Qq6qIn3J1OWDsAUh3W2PatLfDhd19W8BUFz30vpRZLnsobF2k2rRN3ZP-42uqJQdoqaVi9XGmwl2Wwrd1Rkm75-hd7uObmEs8LFuAisGijvrrGJaDOOGL3EsDx1jV7bMkBK6LxysLn4QyzUdCH9Pw_61nW6k6UoS9xMDurBV9bY-NGYxgIUlWEnL1YSUNkwywoSv5HSj94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابستان امسال، همدلی اعجاز کرد
کنار هم ایستادیم، از روزهای سخت عبور کردیم و نشان دادیم وقتی ایران، «قرار» ما باشد، هیچ فصلی نمی‌تواند همدلی‌مان را تغییر دهد.
فصل عوض می‌شود،اما قرار نه
....
قدردان همدلی‌تان هستیم؛ برای تمام همراهی‌ها، تمام «نه» گفتن‌ها به مصرف بی‌رویه و تمام قدم‌هایی که برای ایران برداشتید.
🇮🇷
قرارمان برقرار است؛ برای ایران، کنار هم
🇮🇷
#قرار_همدلی
#همدلی_برای_ایران
#تهران_روشن
‌
💫
با ما همراه بمانید.
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/691411" target="_blank">📅 12:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691410">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
روزنامه کوریره دلا سرا: ایتالیا آماده اعزام ۴ کشتی جنگی به تنگه باب‌المندب است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/691410" target="_blank">📅 12:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691409">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f9ee41a0.mp4?token=s2JkYIZih4aIorW35LB8LzBvS0sbnsCXgfwXc3idW9XOqbLt3keNha-KsXDC0Hz_Iy-xGrOOZb_qchyBHM5EjGU8zYPhbpXOU59tA4ute8R-MfzzQ2wpgk3ShWNgbKHRCBExDaVgb5FHskoAq88S7d9LkNytLfkMlOGLBGzeDTSiinZuqez95j0fuK7QTMov73C14l7d3r9knDaSmSl4wj66f2DGhCsjzsztb-xxteZJU-5phMIwmhy-JgHoV9Wnw253K-EBtIRVI_6ZENj1kNY1RO7Di5jooOshX808BHpRoT42tfopIjkZnpserxYuFBqPO0dpLbStzJqd-7KSHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f9ee41a0.mp4?token=s2JkYIZih4aIorW35LB8LzBvS0sbnsCXgfwXc3idW9XOqbLt3keNha-KsXDC0Hz_Iy-xGrOOZb_qchyBHM5EjGU8zYPhbpXOU59tA4ute8R-MfzzQ2wpgk3ShWNgbKHRCBExDaVgb5FHskoAq88S7d9LkNytLfkMlOGLBGzeDTSiinZuqez95j0fuK7QTMov73C14l7d3r9knDaSmSl4wj66f2DGhCsjzsztb-xxteZJU-5phMIwmhy-JgHoV9Wnw253K-EBtIRVI_6ZENj1kNY1RO7Di5jooOshX808BHpRoT42tfopIjkZnpserxYuFBqPO0dpLbStzJqd-7KSHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازار بورس ریسکی شد!
کارشناس بورس:
🔹
وضعیت قرمز بازار در روز نخست هفته، نشانه‌ای مهم از اتفاقات پیش روی بورس بود. از حالا باید ریسک‌ها را درنظر گرفت و معامله کرد!/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/691409" target="_blank">📅 12:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691408">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f26eb5c361.mp4?token=MQPXdWrQLYDGRmdtvRvmUBP4XIuqS7rNFdJccSXUf_IHXlLpmx3iiuCYVCJeFFVf4vRKFuKxRQ1W4RbjWKeVU4ggaOdwR8BosAXB0Ambr-7HCb2G6tKQ9az6XbpLlc5WlGNssX11qKht-Ptuh7HCCG-vmC7YTMauEfdrkH6Jf7gcLfpajmmY71Bkyx_NCP62xbLaEskmjQjCiIdIeBMwPnLl7RWkoKEvVYD5p1SJpNf56hvb9xKh47pf8Iu165q5RpPKKx92e_ckHNUtt8apmDTzNtPYfiHzPbLAFFSKYwyOPtxhmIrMscP1gdfNmSChZtmlMhf86G0I-ZW6oJ_NHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f26eb5c361.mp4?token=MQPXdWrQLYDGRmdtvRvmUBP4XIuqS7rNFdJccSXUf_IHXlLpmx3iiuCYVCJeFFVf4vRKFuKxRQ1W4RbjWKeVU4ggaOdwR8BosAXB0Ambr-7HCb2G6tKQ9az6XbpLlc5WlGNssX11qKht-Ptuh7HCCG-vmC7YTMauEfdrkH6Jf7gcLfpajmmY71Bkyx_NCP62xbLaEskmjQjCiIdIeBMwPnLl7RWkoKEvVYD5p1SJpNf56hvb9xKh47pf8Iu165q5RpPKKx92e_ckHNUtt8apmDTzNtPYfiHzPbLAFFSKYwyOPtxhmIrMscP1gdfNmSChZtmlMhf86G0I-ZW6oJ_NHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های تلخ محمود بصیری پس از مدت‌ها؛ تلویزیون بیننده ندارد، من برای کی بازی کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/691408" target="_blank">📅 11:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691407">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b684f06d.mp4?token=RGP9JZZfrW9U_FU-qJNQWR9fuD6Ff5qGClwyQddyr3SEn6-HVRn7r8IsWnUp0vpoRdWu5_MYGzGpm6akPkvgIDbkIU3jvVfoHgmxdfS7PhHJf3OOXRd00nWH_r-8TViEmiLEQbmDTc7uSRE0CNRQGbal0Jn-KlNsY2jA890pmqhMywexpP1Gj4c6yIDEBpRvaUuT3RTKIST-383sU9q_fO0qzR02zuYxhCBBN5EuvJNiBhGff-Ds4bZcq7mlcnex6_2DUpq0i_5oyCHBIgdzIrVRCfmjXdfuwKTWavia4MvFNhAegGgbIhn2rIggtde0orjGpwaRfUFzlBfyDkrcnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b684f06d.mp4?token=RGP9JZZfrW9U_FU-qJNQWR9fuD6Ff5qGClwyQddyr3SEn6-HVRn7r8IsWnUp0vpoRdWu5_MYGzGpm6akPkvgIDbkIU3jvVfoHgmxdfS7PhHJf3OOXRd00nWH_r-8TViEmiLEQbmDTc7uSRE0CNRQGbal0Jn-KlNsY2jA890pmqhMywexpP1Gj4c6yIDEBpRvaUuT3RTKIST-383sU9q_fO0qzR02zuYxhCBBN5EuvJNiBhGff-Ds4bZcq7mlcnex6_2DUpq0i_5oyCHBIgdzIrVRCfmjXdfuwKTWavia4MvFNhAegGgbIhn2rIggtde0orjGpwaRfUFzlBfyDkrcnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به دستور تولیت آستان قدس رضوی خوابگاه ۴۲۴ نفری دانشگاه علوم پزشکی مشهد به بهره‌برداری رسید
🔹
خوابگاه خواهران دانشگاه علوم پزشکی مشهد که با حمایت آستان قدس رضوی و اجرای شرکت صنایع معادن و عمران رضوی احداث شده است، با ظرفیت اسکان ۴۲۴ دانشجو و زیربنای ۸ هزار و ۲۶۱ مترمربع، با حضور تولیت آستان قدس رضوی و رئیس دانشگاه علوم پزشکی مشهد به بهره‌برداری رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/691407" target="_blank">📅 11:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691405">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4d41e2f0.mp4?token=EFnsr2QrfPM8OfGp9q9vII_vCDMSuFnJrVNzMIQFnR8icaP64RIyEkEvxjFNuWAu0CP_5CyMAMx16nrSHmjb8Kp-zs2xuA8rdhMlhk4EuQ_VZdduoSEce6LMuyoV1f2buD6MmFc4rBrVY2_LmCyA72g118tC3RdGeOF7XWwJGcW7f9c3Y9jsI17qFeQfLG9wWWfmmX5cohgS5hTTk_O5Id7wbwQig6pvCNoc8NV20T2k0jGrTjRK2YIQCVS5S_LVhB9XebejVdpuEogUF-lmr6bwo4CxPnLGLIF450x0B_od06mn8YCRv6YAcKp3bzaVJ8oaGZTCdZ7xlet8HQeyLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4d41e2f0.mp4?token=EFnsr2QrfPM8OfGp9q9vII_vCDMSuFnJrVNzMIQFnR8icaP64RIyEkEvxjFNuWAu0CP_5CyMAMx16nrSHmjb8Kp-zs2xuA8rdhMlhk4EuQ_VZdduoSEce6LMuyoV1f2buD6MmFc4rBrVY2_LmCyA72g118tC3RdGeOF7XWwJGcW7f9c3Y9jsI17qFeQfLG9wWWfmmX5cohgS5hTTk_O5Id7wbwQig6pvCNoc8NV20T2k0jGrTjRK2YIQCVS5S_LVhB9XebejVdpuEogUF-lmr6bwo4CxPnLGLIF450x0B_od06mn8YCRv6YAcKp3bzaVJ8oaGZTCdZ7xlet8HQeyLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی انتشار تصاویری از برگزاری یک جشن هنجارشکن در یک کلاب ساحلی در نوشهر، دادستانی و سپاه این شهرستان از برخورد با عوامل این مراسم خبر دادند
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/691405" target="_blank">📅 11:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691404">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05cb7ad599.mp4?token=P96C7kq1l2qSRCLxb8C5sotlEh6A2JJHH9bgNxdesJ_42-fNMm796CAFH4wPbPDk1wJi-qwLYtgBQgax2Mq3SvPBCPLjVU0eR12udwZQ54xk6D7Yrckg0kZz8nXvLFtwVoFy6aXb0D3vCHegqHb_8Gyy0r7jAOzSVKCC3sfgNVVER1YzQkInzUEqpVZSzlCqWJB-YjbgFxlgOQmp79d38W4HbbiSJutP4i_3rR8pccDfaElvJRG7MdBQaxifCY32LAp2Sp4zHjwLh8sqDNLEj1CNbVQgS0ziAVA4ixdxJcqdyE9EaOsx-WBlK5cfOUdDOAckIRh-aDwKdH_dmbz3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05cb7ad599.mp4?token=P96C7kq1l2qSRCLxb8C5sotlEh6A2JJHH9bgNxdesJ_42-fNMm796CAFH4wPbPDk1wJi-qwLYtgBQgax2Mq3SvPBCPLjVU0eR12udwZQ54xk6D7Yrckg0kZz8nXvLFtwVoFy6aXb0D3vCHegqHb_8Gyy0r7jAOzSVKCC3sfgNVVER1YzQkInzUEqpVZSzlCqWJB-YjbgFxlgOQmp79d38W4HbbiSJutP4i_3rR8pccDfaElvJRG7MdBQaxifCY32LAp2Sp4zHjwLh8sqDNLEj1CNbVQgS0ziAVA4ixdxJcqdyE9EaOsx-WBlK5cfOUdDOAckIRh-aDwKdH_dmbz3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند ساده، پلاریزه بودن عینک آفتابی‌ را در چند ثانیه تشخیص دهید
😎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/691404" target="_blank">📅 11:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691402">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
محسنی اژه‌ای برای پنجمین سال پیاپی به ریاست کمیسیون حقوقی و قضایی مجمع تشخیص، انتخاب شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/691402" target="_blank">📅 11:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691401">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
مقامات مصری در اختیار داشتن حساب کاربری در شبکه‌های اجتماعی برای کودکان کمتر از ۱۳ سال را ممنوع کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/691401" target="_blank">📅 11:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691391">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSP29Mq9Qwsh6MJ21O3KxEi5M4OI0M9aCTB_RgM6IC7jn7uojcdVOTAwfChFi2_8L0h42teDhmLNKG6p1NtbA9ZiXb1ltxm8Kbm0j9eySbJMkePW5Ads5emL-kji5CbN0JHUd7dynk8Gt8qDxtTKLNQ7SvC5hYQm9xTxl4cgnPvtFGFDZ1AYwf6cXI3GQf23-K4Q0DOvOgTFvguOqkRUhoB1dFbf4xx0BuXCtfPqf6JyHRtXeqR5Y4zTGkGaclGWcPR0fuRBKGSv2z_PtSttX72UKIz9SnFjLcImUapdn38xwyJr55rOEgj_L4vNe_WKg16jBlvcJHsDtjRbgizFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYctKmYZEpThjrWqccc7-BtQXY-yCBjIONfi8RYEVmMuicHqjYvOQLI0DRGEJC5vmhJXeKGivvmY9o-HdaGWpkWgaVmM_Ws1W8cyLxY6JU9ocNw8znvN9BmTHnIYEZQ5i6gGyHXeItuB-0Tx2tHX-NsLU_s03me2b6WqZJh95E-vFvT9_mrPwN4OtS91YnL2SB090icNDtNxx5ir2gMLaYde6Ja_bGNkFsPOTRzxzVubwQ0FkOiyB7mVT9_NoREMOUwnGM9IKzo-Hy-0H6vtY4wdgNG9mMyIxzgo7KxwyBvw0CxtjTEf2oyTc2YWwIUluumtRy0knkzi8tNEroyRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6y-COc1Cmy6dO2wVBc1tlw79aUNjsrnIWV-uKHLWu3CBlCQR_8swdlB9z_JctVJ0Ws71ZkFztZWM0VZiP-pyt-g50DySFdDThVJD50eTN40kkrmQaW9kgqBYgEDU2Py7ooKBpWg33FvN34C-0E3LL8H7M8EKIzIyzzeMIaBeyHsQRAlC9bITifXMxoC_HJTu_JTq-i_3QSixICvqqGyTdU7P1XpzUrmF67goPB18FSaSS1tzUahk7OE9Y-QEu_LQaewmrz5TbPXtmWkqKSEvwggIvXkgiZcawlIkHVyvHccVfrkxiHkDZFxCBYxpBJS5qF_Fxn5zYJrVpjrRFo49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4qmLmu2q5iSyCE5kNRqdX0wNN5aFf5ac9d9h2PBHEP8aj-_BDiW5G-S2Vi9Q6821zV-dS6uNENEf9c_M6PmORH0r7g-1mMr-Du6Gwx9TOPKL-BUSDlvqbrEkZOg9XvRi94y0xT_nPmLue9sL1q2sd7wkGGNlyT1gVdnmhOkbfnDD05oZBB2Eaw21WFkgq3_DI5BgmGyXIYrWkjfZ27Exp2hf95UazH8bYwYk6GEKkY9H8JxC2QgtSy-N7grzb3zJ4ueE0bR60aG3iVWY_8k2-UJgO6y6r_qllOITEPGIAWzaMtMWvNBuaQN5w7hdEBO-EDsc4FLnKPKiCVl8CcODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxztIspCpBRMQo82FYRabZMhBaNC7VqIHRjcTI3TCMpaopoT00P8xsCBHtEPhctneKDiRb8G9iiIAGcC4aRbf-YZKZASYCHWXU-a6rgoV99wTEbVVl3-75OOJM7Z_yaa4ZqGAd_VlzVD5EG268n2YiBrjVBhy9kf_wp0J8-p4z0bY12MOoNc62LTwp3tsZDZMQcT2J4Aj-TvW3ZN32_5UI4FwqC-VBLVWL2HRf4BY5nubXQ--IsQCh-vXhAAaxhZKoPXvmv82LK6nrN7q1uWgoQ220mmY3d9xUCeO4I33UNo5Sq3I0gxpC8aHkxD5b9gceeAqbgkXlTRisyDClTwrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8q1Y9EdtPJYijFk9d9SKANLOe_873k42nGzpGQYF4J7Pl_28tnDx8WYh3VNG-BlqW3JBpVWerqiYtS3Vb6b_v5eKKMyq-qdyhinqKwflKhTEr4TAQwTTh3Xk99gYUMalIlWDWheYNlI_qheTYQmh7wKPHIX54GJYpw9NiTwJQ70PRRI9hX-jM9zPxu-JJ5w0z0xO6CgsX41_Bzw9couucLOAGYK5yUPhc6cHWB_x2ld0vYX32QgLvFWEuT1utpmRhT6GD3FEZ8qFyJ5w5nBNELb7Uhe5MQKyIU6HtpZG0Ja6a7bcgi56O0rIcopvGI9vOv9Uaqv-rWgxP6gJz-95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pffrADjmJHg6hbM2k_uNsFlgSvKLJ39Isxxq7mt0mTitBSh9gl0LGRF2EiRjbtNdm97VkqzOa7woqNscvhLMTQWekce9CilSkxbUQFUwiaIfobxfBvB9VGUk_gr-oJPRFYGXgxvbB7LUTQHOrYnZeS9rIyY0z3kfj_l_D9ea782gKy8PWQxh1IzYQ7QlofdzQyfToeXglfKGed1-28affHVzD76ghMkqYvvm9Tv_aVZOJnDTodt8nxL_bsYz9TU3cIm9TfiyaSYJfciw0IkW_3TB0j1iydWmgSE7Hu2Vbi4VAnrDQKOVSiqGIOlKqhu1LD6gh80kM0bXHYbSlv0wmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9ppImqCRBBh37acP5Csj_sGzYfBRLyMv7ZK2xeWuabmY0R_KmvQ8MbxCruC_5AGpM0dCwxTVie54B_CU3B7-ZwlIq6u0eeHaTEyWF6NEFct_Q3qJ9gYrfg0zVY92-9OTro2rFgm5xwXJznPiGiLG8JEoIdWwO2uTv0-ErjbsziPjl6pqLYkxvygr2gT5b99z1aN8zlxe9myJLci7mazc_87slFswhpHIWukFpbUSW4lgLlRvYPacfuqla5gPQrrpPaPq_23ubGy_WRYCcQwPwe-Q8m8phGaBVrHZX3S8jqEV7CisXRziMhNi1kguRqmZIcnmBjtJDNFnoHy7cF7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFm-BxUlC6DIlZ0rOEmqAr2JutXTtiEOhiHqbysXD8T56VpC_ODgGb1YQnOfIIM2563SHyrntlfqNDSJ24QrU8RHkLxBoNpFr3ftXJu8sbv0iJHDt7X38I6ldHEUSuIQtmMBNTdyMKksefHB4LZJzUddPT-DsCKNaczINW1GV2lapjStBBwMjj_sTQ-pT4HYqifLWK7_3DBJRY4tEONHNWn1_ZNXGSX_i9H8MQ5mtcDjsFxzt-_vQJMEM5JHdXilFstfqLaDye5RbtOqoF3r337JMI1-7ISgQIcdW549HJgTdxIjxzo2pW5gnGjBZ2mjGlBU5JbspjSk0V3m95FVJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5fSpDa6UvUHVayXK2c3fqIG5EwP9HhlDLOagYpf-D9QruZoJuOhABRSD1sV73xPB2AXmxPIPu48afAh2XRc7aMLFMtoyys-x2SVKx8ZOvcceF5pmlMimoLUc1QG5F3p7y0XkulFNex4Z3VnfwQom2fcoRW4UaE2ohxbZeGu4UNaf0dsUF2gT8WFK5IvCeT08zIwEPO4wzJmLRJOYps_U7-UzDTJ7PFFvmnov0-BpVspRix3bjLhEj3g_XMwZgf730TcqK2x-zrW8_v-Yq5S4r84SdbmcWXIawLh5dMtZMf8TfR1-pvCGX25P9SVjt9A8I9tSywYkT0yS3SzJnHMZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
پیام‌های ارسالی شما درباره چالش‌ها، گرانی‌ها و دغدغه‌های ثبت‌نام مدارس.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/691391" target="_blank">📅 11:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691390">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان‌ به نقل از منابع: پیام‌هایی که از سوی ترامپ ارسال می‌شود، این سیگنال را به ایرانی‌ها می‌دهد که او تمایلی به حمایت از متحدان آمریکا در منطقه ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/691390" target="_blank">📅 11:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691389">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
مدیرکل دفتر بهبود تغذیه جامعه وزارت بهداشت: در همه مدارس دولتی باید توزیع شیر انجام شود؛ اگر در مدرسه‌ای این اقدام انجام نشده بود، به آموزش‌و‌پرورش و وزارت بهداشت گزارش داده شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/691389" target="_blank">📅 11:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdNySZrbaeQffcQND-XX_sTExY4p2HrXM_XdXJMZdV6h5KjdJJlVy6yVd6fschleVv2V_7dYrE9IRKu2Ir6Fh0FbSyTC3Ne0D-GSoe2A3uiIgC8NueSnMait3L5SRc5aF7ZvzsSYE6Hy8YnzGCED15e-xSRhqWd_NzVZMIoR6tPP6xLIqf2ZUEO9wB8xQIWvi9KilIGFXH0BbDnPc_zkjvaFWnAbXXDlaAkteNKGqsYld6AVBTb2GuKURLrG6ki4md7LuEJxkEn4mOjNDYt9Tb6D5tkfQuKVheLlQMG3jQwufPM-QppF5x0afhqRKQYnq5dYax6mc2f-a_DGaB0nXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بادگیر چپقی، سیرجان
🔹
یک معمار سیرجانی، ایده‌ای از صنعت کشتیرانی را با معماری سنتی بادگیر ترکیب کرد و سازه‌ای ساخت که هنوز هم یکی از نمادهای معماری سیرجان است.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/691388" target="_blank">📅 11:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691387">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سخنگوی سازمان ثبت اسناد و املاک کشور: مالکان سند سبز و زرد نباید دوباره در سامانه ثبت ادعا، ادعای مالکیت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/691387" target="_blank">📅 11:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691386">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
پزشکیان: با هم‌افزایی و انسجام داخلی بر مشکلات غلبه می‌کنیم/ قابل قبول نیست که ما مسئول باشیم و فردی با مشکل معیشتی مواجه باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/691386" target="_blank">📅 11:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691385">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34df6c957.mp4?token=EtL3u4JhGTraxvAZpvPv1iOS2NKO_Gpu89MoHmYz3NeiAIP231yRA6SgbwGBuGDkBlXFCTaLSAxXXQl8OCJ3ieM1zEkLJT2nsSSYpxckE1R59QxBpvYyq59j9AknrSRZVMhvHG9-m9qR9o7Ev-KwzfuK__GYK_o2IixJov-XpS53tY_7THB1R8xJNIatZ0CXKa98JlftDBz1Fv_AR4PjlKiw23jSH3BuDXZeeUglwzA-iOXxd_pc3KQRaKdXRTSFYsY9fraR0luMTs7Q68qpf3uZPoRq0BlL4zIAEvpj-eLxTMP6YeMkQcWtkpW0wQaOPtvI1EszX1-nJ_uyanJ9u0yRsBu6-FTcN-MIjYR6BIAuBlFyc6_FrE71dF4rgfa2EgWSXClkMuHo4X9JAyyjEzVNzdaNlEsyOroN6s2eo_tqwzppOE847mBXYKGFWzvZqCGRGVFKzSrkq00lXt6ndGdTadwEddgvmB0yHXvzs0EnkS_N_U-gbrnkU71O36vwfe4LJxqsCFrA6KrjcyzsgaPWD_VNbCT8UOBR1VuZULIEC1uTPIO4TDJjr3tctwLLE0fGoTX2jINQzkXnNS5lMyNpfHBe5gC3z5QMg441sCKRrxDy_1WBFAt6CSeOtDo-quPNUTB408_NCI1wcIdypTh_YegW8RRrZbaQZwa_9dI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34df6c957.mp4?token=EtL3u4JhGTraxvAZpvPv1iOS2NKO_Gpu89MoHmYz3NeiAIP231yRA6SgbwGBuGDkBlXFCTaLSAxXXQl8OCJ3ieM1zEkLJT2nsSSYpxckE1R59QxBpvYyq59j9AknrSRZVMhvHG9-m9qR9o7Ev-KwzfuK__GYK_o2IixJov-XpS53tY_7THB1R8xJNIatZ0CXKa98JlftDBz1Fv_AR4PjlKiw23jSH3BuDXZeeUglwzA-iOXxd_pc3KQRaKdXRTSFYsY9fraR0luMTs7Q68qpf3uZPoRq0BlL4zIAEvpj-eLxTMP6YeMkQcWtkpW0wQaOPtvI1EszX1-nJ_uyanJ9u0yRsBu6-FTcN-MIjYR6BIAuBlFyc6_FrE71dF4rgfa2EgWSXClkMuHo4X9JAyyjEzVNzdaNlEsyOroN6s2eo_tqwzppOE847mBXYKGFWzvZqCGRGVFKzSrkq00lXt6ndGdTadwEddgvmB0yHXvzs0EnkS_N_U-gbrnkU71O36vwfe4LJxqsCFrA6KrjcyzsgaPWD_VNbCT8UOBR1VuZULIEC1uTPIO4TDJjr3tctwLLE0fGoTX2jINQzkXnNS5lMyNpfHBe5gC3z5QMg441sCKRrxDy_1WBFAt6CSeOtDo-quPNUTB408_NCI1wcIdypTh_YegW8RRrZbaQZwa_9dI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ مردم به چند معمای ساده، به یک نتیجه غیرمنتظره رسید!
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/691385" target="_blank">📅 11:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691384">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
فراتر از یک میلیون مأموریت در سال؛اورژانس تهران ناوگان خود را دگرگون کرد
🔹
سالانه ۱.۲ میلیون مأموریت امدادی؛ اورژانس استان تهران ضمن پاسخگویی به این حجم عظیم از تماس‌ها و مأموریت‌های روزانه، فاز جدیدی از توسعه زیرساخت‌های عملیاتی را به اجرا درآورده است.
🔹
افزایش چشمگیر ظرفیت پایگاه‌های امدادی در نقاط پرتردد، نوسازی و تزریق آمبولانس‌های جدید و پیشرفته، گسترش خطوط موتورلانس برای کاهش زمان طلایی امدادرسانی و اجرای طرح‌های نوین عملیاتی جهت ارتقای دقت و سرعت پاسخگویی مهم‌ترین اقدامات توسعه‌ای اخیر اورژانس تهران می باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/691384" target="_blank">📅 11:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
افزایش کرونا و آنفلوآنزا در سه هفته اخیر/ موارد بیشتر خفیف است  رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت:
🔹
بیشتر موارد خفیف است و با استراحت و مراقبت بهبود می‌یابد، مصرف خودسرانه آنتی‌بیوتیک برای بیماری‌های ویروسی توصیه نمی‌شود.
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/691383" target="_blank">📅 10:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691382">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سازمان غذا و دارو: مجوز محصول سلامت محور به معنی اجازه برای هرگونه ادعای تبلیغاتی نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/691382" target="_blank">📅 10:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477de95318.mp4?token=fvQEWpDQQMXdehOIy2ylaDq8o9xguljDCuRzRRi-24CB09xKxO8Pi9yDww5ThZS6j5v8Im6_ASfOmnzySzisTEAJjyCxKtrBDQTvL0L1GEZzMgUaKV2d7XS-EnLlWnQxDuR3pD0IIvIdi8cHcHZOOrBIJN-jY0wSRVlwjRZ3Qaxl8qrnTShNagq_PlMXdHBqqRksudXrQ5yF2YzEkCdTJo0_5hlZXrpHYZFf0-F2eCeeswQD8elJxHUk4GoGmw93vWLPGe5MixsYC39tFhqdfHBzF-5fNJMnQ4nP2aJRNepcNpl-GeqZjdw7XmBIh3joGVUbBTgl16AiDZi1kXCGdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477de95318.mp4?token=fvQEWpDQQMXdehOIy2ylaDq8o9xguljDCuRzRRi-24CB09xKxO8Pi9yDww5ThZS6j5v8Im6_ASfOmnzySzisTEAJjyCxKtrBDQTvL0L1GEZzMgUaKV2d7XS-EnLlWnQxDuR3pD0IIvIdi8cHcHZOOrBIJN-jY0wSRVlwjRZ3Qaxl8qrnTShNagq_PlMXdHBqqRksudXrQ5yF2YzEkCdTJo0_5hlZXrpHYZFf0-F2eCeeswQD8elJxHUk4GoGmw93vWLPGe5MixsYC39tFhqdfHBzF-5fNJMnQ4nP2aJRNepcNpl-GeqZjdw7XmBIh3joGVUbBTgl16AiDZi1kXCGdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ سوژه شوخی نخست‌وزیر کانادا شد
🔹
در بحبوحه تنش‌های تجاری آمریکا و کانادا، نخست‌وزیر کانادا با تقلید حرکات دست ترامپ، حضار را به خنده انداخت.
🔹
مارک کارنی، بارها هدف طعنه‌های رئیس‌جمهور آمریکا قرار گرفته و ترامپ از کانادا به‌عنوان «پنجاه‌ویکمین ایالت آمریکا» یاد کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/691381" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691380">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
مکمل آهن و ویتامین D در مدارس توزیع خواهد شد
مدیرکل دفتر بهبود تغذیه وزارت بهداشت:
🔹
در مدارس دخترانه هر هفته مکمل آهن به مدت ۱۶ هفته برای جلوگیری از کم‌خونی توزیع خواهد شد.
🔹
همچنین در مدارس دخترانه و پسرانه به‌ صورت ماهانه مکمل ویتامین D در تمام کشور توزیع خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/691380" target="_blank">📅 10:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691379">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b05cdb98.mp4?token=F8HU-OFsg1UBa1oLRRMUeKIC8cuyVUNdfMsUzaypsfaStG89fvyzkl4U-wX7T7QxKsjJ_1fLct6HuW8mSxfOSUfj_yMhYYto62SgPEd55EVqAmERYR9eRGy42ELdVkIOeX6QeN97vl3OSDSx9GJxt8OMOjBEkxFoH36rFqexCy8LdVBix3F7Npk3_tdz1X2QZRR3QuVptrsFyaRMxTzLc4-kmMDdcsXFU-ba1-Di_w2yXreTbfOKVeWndos49_fNfLkfbCeeSVn1a_rQ-pxL-DL429W0EaUyw1QoAfcQgonbSJhEPDE6fcwGDt57syWRQlTpd_ia4UtTAwGAXWjs4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b05cdb98.mp4?token=F8HU-OFsg1UBa1oLRRMUeKIC8cuyVUNdfMsUzaypsfaStG89fvyzkl4U-wX7T7QxKsjJ_1fLct6HuW8mSxfOSUfj_yMhYYto62SgPEd55EVqAmERYR9eRGy42ELdVkIOeX6QeN97vl3OSDSx9GJxt8OMOjBEkxFoH36rFqexCy8LdVBix3F7Npk3_tdz1X2QZRR3QuVptrsFyaRMxTzLc4-kmMDdcsXFU-ba1-Di_w2yXreTbfOKVeWndos49_fNfLkfbCeeSVn1a_rQ-pxL-DL429W0EaUyw1QoAfcQgonbSJhEPDE6fcwGDt57syWRQlTpd_ia4UtTAwGAXWjs4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گله بزرگ گوزن‌های شمالی در چند قدمی دوربین عکاس حیات‌وحش در ایسلند
🦌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/691379" target="_blank">📅 10:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691378">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/691378" target="_blank">📅 10:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8b7ba2ca.mp4?token=nSyp_YSVMIPP5w8jqlUiRselw6TwNy3nFGdBzZMrRjUoNds5LxSQqQZdhihX1Oxfji6OUqNFCCkVQ7LZypmy216MTxoHaL7Ihd_PitttuRMmjmsNO9i7qDVBd6JgY4rmlliJdFU79xQznHj8pHFWICHcshM4xiKQYOspqmyPfrnAyfcmHrHwbp50HGcEhD_QaVyetlGgHfBXfvI8uOPdwtUipaADtL-D6K5HjnaBCUCEGKNmlC2OVdj9PHtEkjgobZ7jXehpz9hF49nWKdq2ENrhMP3-NGa79hhkfY-swOtNGu7OImt6YiElvYjVrqUpKld0_CVQXR7d0-2cSVpNWg9ESA-exy4K5QGsVbeO4l5MdBgHn9IfaOHPEYlSbFQyuXuW0XE_JLpNVPE6MKZjJcxYxB5W4gZsB1LVcvq-5NpL9OOT6UlPFshev2rXBIOzJqs03R6Cz02B_iZKEZPrlRFaTlfvJsU77hEHKMuUu5yi2G8eTZYbNXZt4Q11EFv5k3IWKaGbeC6JQHd53-MZ8CTfdVRoh4CPjiHaV1JbQaYlRIIkMEvAh4699S_H1kvij1GI7LuJHauCra8gLqNqKSaeeTBNzKZY_GiazystV2YK6jGnmyI80CUOleK2AHo9SUeaH6wZjSJVofQL8KiYJlxsNrss_B-CIHF406zZMFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8b7ba2ca.mp4?token=nSyp_YSVMIPP5w8jqlUiRselw6TwNy3nFGdBzZMrRjUoNds5LxSQqQZdhihX1Oxfji6OUqNFCCkVQ7LZypmy216MTxoHaL7Ihd_PitttuRMmjmsNO9i7qDVBd6JgY4rmlliJdFU79xQznHj8pHFWICHcshM4xiKQYOspqmyPfrnAyfcmHrHwbp50HGcEhD_QaVyetlGgHfBXfvI8uOPdwtUipaADtL-D6K5HjnaBCUCEGKNmlC2OVdj9PHtEkjgobZ7jXehpz9hF49nWKdq2ENrhMP3-NGa79hhkfY-swOtNGu7OImt6YiElvYjVrqUpKld0_CVQXR7d0-2cSVpNWg9ESA-exy4K5QGsVbeO4l5MdBgHn9IfaOHPEYlSbFQyuXuW0XE_JLpNVPE6MKZjJcxYxB5W4gZsB1LVcvq-5NpL9OOT6UlPFshev2rXBIOzJqs03R6Cz02B_iZKEZPrlRFaTlfvJsU77hEHKMuUu5yi2G8eTZYbNXZt4Q11EFv5k3IWKaGbeC6JQHd53-MZ8CTfdVRoh4CPjiHaV1JbQaYlRIIkMEvAh4699S_H1kvij1GI7LuJHauCra8gLqNqKSaeeTBNzKZY_GiazystV2YK6jGnmyI80CUOleK2AHo9SUeaH6wZjSJVofQL8KiYJlxsNrss_B-CIHF406zZMFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژنرال بازنشسته فرانسوی: مدام به ما می‌گفتند ایران به زانو درآمده و محو شده، نه تنها ایران نابود نشده بلکه امروز می‌بینیم که نرخ سوخت به قیمتی بی‌سابقه رسیده و برخی جایگاه‌های سوخت در فرانسه تعطیل شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/691377" target="_blank">📅 10:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc38481e6.mp4?token=MeLbQlRCHDpTNAoi_KF8oExk-VkxB_rB4Io9zIPhNTuaHkFBEMwA5qwAZU_-4fxt9eGZj351pT5Si2kEMp4iWH696D4sdp9DnTOKkrWDkfJdyZV6ZLT5NN4FyqzxSjO_l0xO7R-TMqHLVB8ymmATj0UOMLcFD8jZy4jIvMt5x0ohhLhYNhOM3G8wDYhNmCqUuHNPsPaRkV9QPSdLnJhnyT87TlMkIQf6DQb9XOIixTYF8dK08fCC4rAyys2x2QXp0m0qFpuIkS8jNS2Y2GpNp0AYOSDZX0LiUpoMuXniQOIIlrOEjtD6wrHarnw9pHtCkqEnGmH5D1SXit1lbblr6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc38481e6.mp4?token=MeLbQlRCHDpTNAoi_KF8oExk-VkxB_rB4Io9zIPhNTuaHkFBEMwA5qwAZU_-4fxt9eGZj351pT5Si2kEMp4iWH696D4sdp9DnTOKkrWDkfJdyZV6ZLT5NN4FyqzxSjO_l0xO7R-TMqHLVB8ymmATj0UOMLcFD8jZy4jIvMt5x0ohhLhYNhOM3G8wDYhNmCqUuHNPsPaRkV9QPSdLnJhnyT87TlMkIQf6DQb9XOIixTYF8dK08fCC4rAyys2x2QXp0m0qFpuIkS8jNS2Y2GpNp0AYOSDZX0LiUpoMuXniQOIIlrOEjtD6wrHarnw9pHtCkqEnGmH5D1SXit1lbblr6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«بشقاب پرنده» رسماً در چین به فروش رسید
🔹
شرکت چینی «ئی‌وی‌تول»  فروش یک هواگرد برقی دو‌ نفره به شکل بشقاب پرنده را آغاز کرد. این‌ بشقاب پرنده می‌تواند بر آب و خشکی بنشیند، تا فاصله‌ای نزدیک به ۳۰ متر پرواز کند و تا ۱۵ دقیقه در هوا بماند. به خلبان خودکار مجهز است و برای پرواز در باد شدید طراحی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/691376" target="_blank">📅 10:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691375">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12cafc3c9.mp4?token=UeJredKU8-lNnfsd4Yvu_RK9ZBDKPdwjZqzbnqVatvODxRsMVZu-ei6MbCMvDm4qNkE58L4O8W6zrv5bBOeCiEpIMVWMdCxObVz1QUP8Dm7_pQqflI7ShS6U5nFY3To6EGexR-xr57q0P3bnWhiyzFum1QEC4XPlub0b84iqvQPOCSCWbMKtR_HMMWF2jJhyVkh4FaDxHPtPAAmbE1DCZqeku6xNSGCDYXpe1D5TUddfzegbr1XJQaMSa-SygbfxZ-exVlM1izc5XteeH2wJm39QPBrwBeEG3hg1zualumM9VZIneIsNYKNlWQInqgzf4Q5z2bg9IEZb6KNy_F-3yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12cafc3c9.mp4?token=UeJredKU8-lNnfsd4Yvu_RK9ZBDKPdwjZqzbnqVatvODxRsMVZu-ei6MbCMvDm4qNkE58L4O8W6zrv5bBOeCiEpIMVWMdCxObVz1QUP8Dm7_pQqflI7ShS6U5nFY3To6EGexR-xr57q0P3bnWhiyzFum1QEC4XPlub0b84iqvQPOCSCWbMKtR_HMMWF2jJhyVkh4FaDxHPtPAAmbE1DCZqeku6xNSGCDYXpe1D5TUddfzegbr1XJQaMSa-SygbfxZ-exVlM1izc5XteeH2wJm39QPBrwBeEG3hg1zualumM9VZIneIsNYKNlWQInqgzf4Q5z2bg9IEZb6KNy_F-3yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیاین باهم اسنیکرز سالم و خونگی درست کنیم   مواد لازم:
🔹
شکلات تلخ
🔹
خرما
🔹
بادام زمینی
🔹
جو دوسر
🔹
کاکائو
🔹
کره بادام‌زمینی #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/691375" target="_blank">📅 10:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691374">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkxLvWXAU3CrHy3ICRV0H8DzQAdFM9Y2igGGKIY02U4lwDGldUKgvjwoj2eSiQs4YWYv0Mi46MDuvzuusuGARojKN--NEr2WRckiEV_LUFXndHpnXNLHtPvMIVhtepRAo6QX9I4DNoj9K8XzjGcX_YtLFlMLCwnEWRDnNiNhrFr_s5LqnaHfonHpKCJtpvyQDEoRci2sDGiNGDedceT8GylXMt6XSRaSpK3xtdDXnT4fKBwJRaND4DZxHS4AN7Uxy_UKR_SfNxRgFCyqadcRW3gSdS_SrdouRs_BO9ETMzhBMvUU_0CMK2fwYymbyRhFAtYuJ9RhM-MLV6HyrH8Cbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارشی که در جنگ ایران، آمریکا را تا مرز حمله به چین بُرد | گزارش نادرست چه بود؟
🔹
یک خطای تولیدشده توسط هوش مصنوعی در سیستم اطلاعاتی ارتش آمریکا، در جریان جنگ ایران، نزدیک بود واشنگتن را وارد رویارویی مستقیم با چین کند؛ روایتی که بار دیگر نگرانی‌ها درباره استفاده از سامانه‌های هوش مصنوعی در تصمیم‌های حساس نظامی و اطلاعاتی را برجسته کرده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246396</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/691374" target="_blank">📅 10:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691373">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObIEyVtaKWmhCx_WUE1o_NgHvPGuqtR6jNiPhTHkF5-JXoSkJnl36fHsN7hQcfnpf9tQaB5OPSMKmJUZdEzhE_fHX8msJPPDSAtR7HhdIx1Mg9QN4MoC8TfiVSxWxiE5xPnuWFeLFqiLXJyvGKPTmtSto4Sdt0Swa1XQHZxij-SxHavYAT1O838vg53ooa7kR4901M8JZ790oxRbfRCw9k-GsIp0oQk0LgBSdmx-LQd3d8muEI7wASFWmf90ySzXg7FvdbdAyLk3YVGjksgp9onUdSWHEKQthnjcCH7DRuNz_hVAaGHlGmXjSom_aB0-QRMJrBrL_EHGFDDVEWlH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت جالب کاربر یمنی: حتی قدمت لوله‌های فاضلاب یمن هم از قدمت امارات بیشتره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/691373" target="_blank">📅 10:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691372">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4Ymaop3_zHjXeR-OQ601cmhdxjcXr4mDjCIkb1HpWc_JFXsrxiJph9vPzIImqb2RyKjTmClKxPsU13CEtRQHiWORwySmGZjE3jCLheSudDPG_rNFTEoAN6xZeK4OfyC81p3abQvzpQWTXTZSFuL5PxA__G4TGcQU3_yziw4QwRN7XUE_3y6hubhBXVDZkzTAz8JaoX2mRaFMFq1Jvcvqo9tQ1aAiG1tya3-Vl4D8JYy6XfBdlj9BLV4xa5wBchoKOL5dOKJoBL_JFA4EfOG0MElf4UNFx94_duNzgx8mvPUAUMp4Laz0Z8pzovnA-Yeg3wkEY04j2On_9D908KtsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوکراین یکی از بزرگ‌ترین موج‌های پهپادی خود را به سمت مسکو پرتاب کرد
🔹
روسیه ادعا می‌کند بیش از ۱۶۰۰ پهپاد سرنگون شده است، از جمله ۴۵۰ فروند که به سمت مسکو هدف‌گیری شده بودند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/691372" target="_blank">📅 10:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691371">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=C9KMsCZTsra1jSHZM5NPrhct5NNJ0HlKDA__AH0BqmTQDShFTcumNuWrnMb31gEln1wpikR40VAeFrKgb5Eyl3qhNAlVyMPEL5W2zCR4sVYE4bNU8nRwrh71Mz8lqcA7XAOtQM80IP101SHr-AlLzwCTrcr7skWIJGDb7C4GZrw8BiM0ylOReegIGyMayrGgBzKvjFp74Y6T-ktmq1n2Gl_OsfkNbcUlrehrwRYTYe59XgkRlHkEFcGLXAY8QZRO-ilwPLO0b42T2k2X1pm_XxVWA7ZmwmFuj0FMSIDTSF2YCeTGysY4u0uuRTcs-vpr7vd7HzNADpK_0qUMP8QU8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=C9KMsCZTsra1jSHZM5NPrhct5NNJ0HlKDA__AH0BqmTQDShFTcumNuWrnMb31gEln1wpikR40VAeFrKgb5Eyl3qhNAlVyMPEL5W2zCR4sVYE4bNU8nRwrh71Mz8lqcA7XAOtQM80IP101SHr-AlLzwCTrcr7skWIJGDb7C4GZrw8BiM0ylOReegIGyMayrGgBzKvjFp74Y6T-ktmq1n2Gl_OsfkNbcUlrehrwRYTYe59XgkRlHkEFcGLXAY8QZRO-ilwPLO0b42T2k2X1pm_XxVWA7ZmwmFuj0FMSIDTSF2YCeTGysY4u0uuRTcs-vpr7vd7HzNADpK_0qUMP8QU8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوکراین یکی از بزرگ‌ترین موج‌های پهپادی خود را به سمت مسکو پرتاب کرد
🔹
روسیه ادعا می‌کند بیش از ۱۶۰۰ پهپاد سرنگون شده است، از جمله ۴۵۰ فروند که به سمت مسکو هدف‌گیری شده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/691371" target="_blank">📅 10:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691370">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQAyTF9uf-CvocjtkuArjflHqRFd0QugpM29lTuhOoPSr6DMwql2hMTswDmVHR8KV93NBfzcapWUTRJbgbptPficup6bmzm9OaS01QaAPuOKm3tGHlQ2TguhgffaNW7WGWTDaz7K9TpxF41IMX_8pf5MwM_AJ8E6SohNKqQR_XEyF_PiHzf5aBzYOdg802zAKrUSRf-BDJmqmmPrGNCoVCScfGE7g33Y7CoD5cOXl173fCFcAx8kPhq07i3v1GWqBBVRDzzIJrB8BcXtz9SIpUiPfLaSIzRPJdAAQt-8g7z3zZjkXJnC75Eq_puw55gI88Lkc5z7K2n_x6B83AKrkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفند درست کردن ماست سفت و خوشمزه خونگی
😋
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/691370" target="_blank">📅 10:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691368">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e8e48689.mp4?token=AEa9n19kF-YXI_iFzSODROZm8tc4-GbAWGSx_WcRL_zlj_vrK5N7TOLq3adScbdpcZjWBtcD5yO5Acjl1MtXgOGDbaKmz0WNtb6IQifZqYLUcj_4IA3uYDkWU5JMgJlmDbgvst5GK-bhweIBGPSuHh2WBAUr4tV0MnXWihoVcB-g5qbRUvEN8AXF_OcViIJFb_UetS2uYC4rVCOmvguXbZOTOC7226aFz4MEAYjdGx7XwOfiv10pDC_B1wKyaGoMXJizTroEgQpO-i4kmeo3E8Wog845jmhhVhne6Q1TGFzJgiOPvVTfuUPr4Pvbm9jDATuhhWBYc81M5F6cEP5nYoHJ1G7sj0_K7lCPDl2Rlot7R6rfTaqHiU30nHJMmexZCrHcL-r9BHHB6UQJ0bA4ZbFvp2ez4e6q8lQ8VLJEKfphqWqmRWBWKikivMUScZyhsJhAoyDhfi0npvC3sKhpYM6a_KID8poVjNZwKAvFsUf9KeYUe4jsrat6PKetfo_ssFiIiWcIOU-w-LWSW60npl1G8dz_8uA2d5_qmAHCcZ9VLX3w0aPHfhN5lNOjipkoZZu91_xwnj1Pvv3JeEp8mflBpGwelXhbkOZdtGD9QP4VgJwxEyLYzAbzQO-tSczA0H891gcyop2wDhqz1ClsM3jN6HV2eHUfhkVwGQ3DaAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e8e48689.mp4?token=AEa9n19kF-YXI_iFzSODROZm8tc4-GbAWGSx_WcRL_zlj_vrK5N7TOLq3adScbdpcZjWBtcD5yO5Acjl1MtXgOGDbaKmz0WNtb6IQifZqYLUcj_4IA3uYDkWU5JMgJlmDbgvst5GK-bhweIBGPSuHh2WBAUr4tV0MnXWihoVcB-g5qbRUvEN8AXF_OcViIJFb_UetS2uYC4rVCOmvguXbZOTOC7226aFz4MEAYjdGx7XwOfiv10pDC_B1wKyaGoMXJizTroEgQpO-i4kmeo3E8Wog845jmhhVhne6Q1TGFzJgiOPvVTfuUPr4Pvbm9jDATuhhWBYc81M5F6cEP5nYoHJ1G7sj0_K7lCPDl2Rlot7R6rfTaqHiU30nHJMmexZCrHcL-r9BHHB6UQJ0bA4ZbFvp2ez4e6q8lQ8VLJEKfphqWqmRWBWKikivMUScZyhsJhAoyDhfi0npvC3sKhpYM6a_KID8poVjNZwKAvFsUf9KeYUe4jsrat6PKetfo_ssFiIiWcIOU-w-LWSW60npl1G8dz_8uA2d5_qmAHCcZ9VLX3w0aPHfhN5lNOjipkoZZu91_xwnj1Pvv3JeEp8mflBpGwelXhbkOZdtGD9QP4VgJwxEyLYzAbzQO-tSczA0H891gcyop2wDhqz1ClsM3jN6HV2eHUfhkVwGQ3DaAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فولاد خراسان در ۲۵ سالگی؛ از رتبه اول بورس کالا تا پروژه‌های توسعه‌ای
محمدرضا سجادیان، مدیرعامل فولاد خراسان در
#گفتگو
با خبرفوری:
🔹
فولاد خراسان در بیست‌وپنجمین سال فعالیت خود در سال ۱۴۰۵ تولید در حد ظرفیت اسمی را دنبال کرده است.
🔹
این مجتمع در سال ۱۴۰۴ رتبه اول عرضه میلگرد در بورس کالا را به خود اختصاص داده و حدود ۳۰۰۰ نفر به‌صورت مستقیم و ۸۰۰۰ نفر به‌صورت غیرمستقیم در آن مشغول به کارند.
🔹
توسعه پروژه فولاد شرق خراسان در سنگان، احداث نیروگاه خورشیدی و پروژه جمع‌آوری، انتقال و تصفیه پساب شهر نیشابور از دیگر برنامه‌های توسعه‌ای فولاد خراسان است.
ادامه مطلب در سایت خبرفوری:
https://www.khabarfoori.com/fa/tiny/news-3246426
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/691368" target="_blank">📅 10:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691367">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdssC_NEZRQm1NPv6fpJCDMlowbhRYCv8Wc-FSVapFXSwDgZX_sNHOiuH4ZoIUTba0l0mYHhcEB-cTGbxm5UhpHV9HlU_RpLM30yiP2PuaYuafUptKpKTjwrKFfDibPb197FAuxwQtevk47m8pmW_TIUkv09vOlQ_WvUWpGZHSzR1iaPC-TCS74YsEMFoDVNVUKsD1yMC6hfjw-F5DSvZ0j7dfWPYO3ArVDePpTv1DrC0h58zyqRHg_zWc-H4loKVooqUeDsnvrP9MxfGnToNqjVoJcp9X6z9RtkpcEmCOmUvbrM34yuuujUF2vOENoBdf8ASYRM_IbF4IwVZnQ91Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف گُل جدید ملقب به گل شیطان
🔹
پژوهشگران در غرب تایلند گونه‌ای تازه از گیاه را کشف کرده‌اند که ظاهری عجیب و تقریباً شیطانی دارد، گلی سیاه با زائده‌هایی شبیه شاخ و لکه‌های نارنجی درخشان. نام علمی این گیاه «تیمیزیا دِمونا» (Thismia daemona) یا «گل شیطان» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/691367" target="_blank">📅 09:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691366">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
قالیباف: نگاهی که از جنگ سخن می‌گوید اما سازوکاری برای پایان مقتدرانه‌ آن ندارد و جریانی که نسخه‌ تسلیم و پذیرش شروط یک‌طرفه‌ دشمن را می‌پیچد، هر دو دچار خطای محاسباتی‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/691366" target="_blank">📅 09:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
قالیباف: مقاومت مردم با شکل دادن به نظم جدیدی در منطقه و جهان، باعث گشایش‌هایی در حوزه‌های‌ اقتصادی‌ و استراتژیک خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/691364" target="_blank">📅 09:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
قالیباف: هم باید جنگید و هم مذاکره کرد  رئیس مجلس:
🔹
ما معتقدیم دو گانه جنگ یا مذاکره واقعی نیست بلکه هم باید جنگید و هم مذاکره کرد. باید معقول و مقتدرانه جنگید و در زمان مناسب با اقتدار و عقلانیت مذاکره کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/691363" target="_blank">📅 09:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691362">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5xR-4LnWIm2gnZNU5Sv8Bwx7Q_n0qYH_Zd_BM-N-fnYe_qABf3euWfVwSbODd-COw9Y_bbCHnmA5UehsrkGkpdtY1-cTS1qYNzxdgC1cey9MUGhW4egblSB-f9rASi5g1RmV5Dpsqov97BylfIRx4a6wOUdICdlX9TLBl8W6n13hbkICS1JVyDpCdxjYxp1QyGYJrgjG-Oku57Apgw0uRG1cTOKnbZE0bLPOoVv778aFskCDGIUQ7Tnlzmjb3999RnozBH6XYiqDZZ0UUPBO1Fkhe2UeImDjdUvGWdefCG28yBpUCSWSNE92e6c4FIj635S9EdVbIzj3p6QWRXyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش شدید عبور نفت از تنگه هرمز
🔹
بر اساس داده‌های منتشر شده در شبکه‌های اجتماعی، حجم نفت عبوری از تنگه هرمز در سه‌ ماهه دوم سال ۲۰۲۶ به حدود ۴.۹ میلیون بشکه در روز رسیده است؛ رقمی که در مقایسه با حدود ۲۱.۶ میلیون بشکه در روز شش ماه پیش، کاهش قابل توجهی نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/691362" target="_blank">📅 09:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691361">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
قالیباف: هم باید جنگید و هم مذاکره کرد
رئیس مجلس:
🔹
ما معتقدیم دو گانه جنگ یا مذاکره واقعی نیست بلکه هم باید جنگید و هم مذاکره کرد. باید معقول و مقتدرانه جنگید و در زمان مناسب با اقتدار و عقلانیت مذاکره کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/691361" target="_blank">📅 09:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691360">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-text">🔹
روایتی شنیدنی از شجاعت راهدار «جان‌فدا»
‌
🔹
گاهی رسالت یک راهدار، فراتر از آسفالت جاده‌ها و حفاظت از حریم راه‌هاست؛ گاهی این رسالت به وسعت پاس‌داری از جان مردم است
‌
🔹
رئیس اداره راهداری و حمل‌ونقل جاده‌ای شهرستان رزن، داوطلب خنثی‌سازی یک بمب عمل‌نکرده در جریان جنگ شد.
‌
🔹
یمینی در آن لحظاتِ نفس‌گیر، ثابت کرد که «جان‌فدایی» برای ایران، تنها در میدان‌های نبرد نیست و در هر گوشه‌ای از این سرزمین و در راه تأمین امنیت مردمان آن تجلی می‌یابد.
‌
🔹
شما را دعوت می‌کنیم به دیدنِ روایتِ یکی از راهدارانِ جان‌فدایِ ایران..
‌
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/691360" target="_blank">📅 09:31 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
