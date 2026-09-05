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
<img src="https://cdn4.telesco.pe/file/SN3MWV-wzQYAq2seln4eToVb3D4kGTvU45xzt3k63VMIPqIGkhsfxSl-eUchaxrsFVeP0PlVM7nPERlEft6S6EKmTAMCUgUPCyCc6oiFvuTcFc7hIczuXMRNfhQ9Jc5_IWX6sMHXTKtHzH6e2zBG-LmurMz41VkTcEACsv-jU9LO8oZhMswM2BC-RXuPj48rRddZYydMjLWzVOn2792ABev6rbk--5PojWwx_9xYDFW2D5Ahk3t1Ddw_NP2NqjBQV9boGe02UK9cpETGBFNoqI4qbUdITPiRyQxILaKDZch6XnAkyn6f6XlVMCmjUb6L4yBBhJCCGF89FZcOBuOt4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 940K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 10:30:28</div>
<hr>

<div class="tg-post" id="msg-145680">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رویترز: کاخ سفید گزینه‌هایی را برای جایگزینی استیو فاینبرگ، معاون وزیر دفاع آمریکا بررسی کرده است
🔴
با این حال، هنوز تصمیمی گرفته نشده و کاخ سفید و پنتاگون می‌گویند فاینبرگ در حال برکناری یا کنار گذاشته شدن نیست.
🔴
کناره‌گیری احتمالی او می‌تواند به موج اخیر تغییرات در رهبری پنتاگون اضافه شود؛ آن هم در شرایطی که نگرانی‌ها درباره کمبود تسلیحات و ظرفیت تولید مهمات افزایش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/145680" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145679">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
یورونیوز: نظرسنجی‌ها نشان می‌دهد سیاستمدار راست‌افراطی مارین لو پن در مسیر تبدیل شدن به رئیس‌جمهور بعدی فرانسه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/145679" target="_blank">📅 10:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145678">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
بانک ترکیه: علیه تحریم‌های آمریکا اقدام قانونی خواهیم کرد
🔴
الجزیره اعلام کرد: پس از آنکه وزارت خزانه‌داری آمریکا بانک ترکیه‌ای «گلدن گلوبال» و دو نهاد زیرمجموعه آن را به بهانه ارتباط با ایران تحریم کرد، این بانک اعلام کرد که علیه این تحریم ها اقدام قانونی انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/145678" target="_blank">📅 10:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145677">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
طبق گزارش منابع محلی : نفتکش هدف قرار گرفته‌شده در جزیره خارک، یک نفتکش کوچک بوده است.
🔴
بر اساس این گزارش، این حادثه تلفات جانی نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/145677" target="_blank">📅 10:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145676">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری / فارس: دقایقی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارک شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/145676" target="_blank">📅 10:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145675">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری / فارس: دقایقی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارک شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/145675" target="_blank">📅 10:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
تتلو: مردم منو فراموش کردن، چطور دلتون اومد؟ حتی اونایی که تو پلی لیستشون هستم هم فراموشم کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/145674" target="_blank">📅 10:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4411422981.mp4?token=IZxvHTvceHmbdiV4W6yQUy4hf9NdK590WkYnfpKS46APjm1HLyQX4sLBLCdOq4WefC2juDytWwCyonFAaWEn0_9yPN0mwaxPV9b-oEb_seV5mfxy-KSDPE3CuR5umepV7E9JHWxp7W4PGCLjnzsNE7nW6c-I5c0vzVGhi4x97bY8c2EcY1A-SnRasvVtzqeKED63fErLnHGQL5KbKwWt5iumgW9ENKy90TnSl_yXBv-090vGMMFsi9iEvgfKc8c0ETN4-QSwWgDhYbRVD1UIPAMivovTI9zfL4_wvML9D6uvk5y1wdYKFu8JjHK5TGrsOlyuxSqG4uZc8ch_Wkey7jq-crsifaI_5a46mtlPxsnHEnTP3z6lS-s1ENlGA9X9i5I2DsdkiRNStTZy-vMoXxgRE4nYkEIBUnsyoach9v4fB2gWETbdfnLSYVO-RiR7fv90nBWvWlaTfAmmzJbm6FOCExpfhHJyqpjgBgJvRpHBT51750_i3AiUtSyXY2FE9F2fHwmSGb70nrA8GcX6s9HDESJCWmkphIlmWPaTlCypQS0aA2WBhmGpVDeIODTw12W7BPFXc_PhceTeN1p4MshDn0-srZjl7kqCvyvMPSBjn7Tg8Ga363_0r9Zpq2xNEghmL1RoqSELA7WMsZqkZlVS9fCayoJf-hCh6agLDiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4411422981.mp4?token=IZxvHTvceHmbdiV4W6yQUy4hf9NdK590WkYnfpKS46APjm1HLyQX4sLBLCdOq4WefC2juDytWwCyonFAaWEn0_9yPN0mwaxPV9b-oEb_seV5mfxy-KSDPE3CuR5umepV7E9JHWxp7W4PGCLjnzsNE7nW6c-I5c0vzVGhi4x97bY8c2EcY1A-SnRasvVtzqeKED63fErLnHGQL5KbKwWt5iumgW9ENKy90TnSl_yXBv-090vGMMFsi9iEvgfKc8c0ETN4-QSwWgDhYbRVD1UIPAMivovTI9zfL4_wvML9D6uvk5y1wdYKFu8JjHK5TGrsOlyuxSqG4uZc8ch_Wkey7jq-crsifaI_5a46mtlPxsnHEnTP3z6lS-s1ENlGA9X9i5I2DsdkiRNStTZy-vMoXxgRE4nYkEIBUnsyoach9v4fB2gWETbdfnLSYVO-RiR7fv90nBWvWlaTfAmmzJbm6FOCExpfhHJyqpjgBgJvRpHBT51750_i3AiUtSyXY2FE9F2fHwmSGb70nrA8GcX6s9HDESJCWmkphIlmWPaTlCypQS0aA2WBhmGpVDeIODTw12W7BPFXc_PhceTeN1p4MshDn0-srZjl7kqCvyvMPSBjn7Tg8Ga363_0r9Zpq2xNEghmL1RoqSELA7WMsZqkZlVS9fCayoJf-hCh6agLDiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سریع‌القلم: آمریکایی‌ها بعد از انتخابات کنگره به سراغ عملیات گسترده نظامی علیه ایران می‌آیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/145673" target="_blank">📅 09:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9a950b3d.mp4?token=MMUbEqthlmssHXiQan_tnXvSmH2-SYF5ytSuXFyaCkEsGa0TSs3nyVui_rakiTE3NDOSM7ObKyyPphRiQEakh9qQaZvfutN4_L16KNnskhs-D29X7LbgFDtcZUKtNlPsQJ_cojxm9IW0DDi2uMtexuKnZAvbZejaeAqkseCMXKIs7fltHqmadE99CQmsez44jC1-1uOChbx2tV5KXgAbiF9LvQcsIP0eFWGzt05NTN_MwV0ncvBCzF5c18809UpCc0paVDS_ZBo2nMuxoqv4vgSzKCwI0CYwNmQO-8wvqxhXFqrRpb9HlULb9xDRW5zkZDNU7KdfDJSu-QnhuKa1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9a950b3d.mp4?token=MMUbEqthlmssHXiQan_tnXvSmH2-SYF5ytSuXFyaCkEsGa0TSs3nyVui_rakiTE3NDOSM7ObKyyPphRiQEakh9qQaZvfutN4_L16KNnskhs-D29X7LbgFDtcZUKtNlPsQJ_cojxm9IW0DDi2uMtexuKnZAvbZejaeAqkseCMXKIs7fltHqmadE99CQmsez44jC1-1uOChbx2tV5KXgAbiF9LvQcsIP0eFWGzt05NTN_MwV0ncvBCzF5c18809UpCc0paVDS_ZBo2nMuxoqv4vgSzKCwI0CYwNmQO-8wvqxhXFqrRpb9HlULb9xDRW5zkZDNU7KdfDJSu-QnhuKa1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی سیل‌های ناشی از طوفان به جنوب چین، خانه‌ها زیر باران‌های سیل‌آسا تخریب می شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/145672" target="_blank">📅 09:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
یک نماینده کنگره آمریکا: اگر درگیری با ایران پیش از انتخابات میان دوره‌ای پایان نیابد، آمریکا در معرض گرفتار شدن در «یک جنگ بی‌پایان دیگر» قرار می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/145671" target="_blank">📅 09:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
مکرون خواهان آتش بس در جنوب لبنان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/145670" target="_blank">📅 09:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس‌جمهور چین، قصد دارد در سفر آتی خود به واشنگتن، هیأتی بزرگ از مدیران و فعالان اقتصادی این کشور را همراه خود ببرد؛ اقدامی کم‌سابقه که در بحبوحه تنش‌های اقتصادی میان پکن و واشنگتن انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/145669" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bd7d8bb1c6.mp4?token=E2VNHs_PjkvjQdoAFWvZFP3apseXvzlBI5A6AmgRkJZyarxEDBqqsRfKJsmUjQeZRMvRlIRpZACxhcg7Yr_YdnPv0GKgF7HhJg-7xg3qWJXNpnuMIb25iAXqOQO5W-3LPI-PQ_gxRYCJXLQxL5Ke2CGS3klWCv2zW-fMSJx8SJgSWdTsgXxgYN9mo4ModJQWodkq9YQ6F_yA7kS-Z18CjjGaBo8xFvYceWcV_FRB_pR7Aub_1oEJzR48I2E3dMrnNDcqxCfiDTkjDhQ6vMARh7mFvefZnBQkgKF4di13aQ6zVrhH2h4ILQI1M0gsX2NQCJIDxG9lykgsPHELW6zppA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bd7d8bb1c6.mp4?token=E2VNHs_PjkvjQdoAFWvZFP3apseXvzlBI5A6AmgRkJZyarxEDBqqsRfKJsmUjQeZRMvRlIRpZACxhcg7Yr_YdnPv0GKgF7HhJg-7xg3qWJXNpnuMIb25iAXqOQO5W-3LPI-PQ_gxRYCJXLQxL5Ke2CGS3klWCv2zW-fMSJx8SJgSWdTsgXxgYN9mo4ModJQWodkq9YQ6F_yA7kS-Z18CjjGaBo8xFvYceWcV_FRB_pR7Aub_1oEJzR48I2E3dMrnNDcqxCfiDTkjDhQ6vMARh7mFvefZnBQkgKF4di13aQ6zVrhH2h4ILQI1M0gsX2NQCJIDxG9lykgsPHELW6zppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رانش زمین، رودخانه‌ای در نپال را مسدود کرد
🔴
رانش زمین گسترده در منطقه «آپی هیمال» در شهرستان دارچولا در غرب نپال، بخشی از رودخانه چاولانی را مسدود کرده و نگرانی‌ها درباره وقوع سیلاب ناگهانی در مناطق پایین‌دست را افزایش داده است.
🔴
مقام‌های محلی از ساکنان حاشیه رودخانه خواسته‌اند در حالت آماده‌باش باشند، زیرا ادامه رانش زمین می‌تواند مسیر رودخانه را به‌طور کامل مسدود و در صورت شکسته شدن این انسداد، موج ناگهانی آب ایجاد کند.
🔴
گزارش‌ها حاکی است جریان آب در حال عبور دوباره از میان توده رانش‌کرده است و این حادثه ارتباطی با فاجعه بزرگ سیلابی اخیر در دیگر مناطق نپال ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145668" target="_blank">📅 09:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نیویورک پست: تا دو ماه دیگر ذخایر سوخت ایران جوابگوی نیاز درون ایران است
🔴
۳ حالت پیش رو است:
🔴
۱-سهمیه بندی شدید
🔴
۲- گران کردن بنزین
🔴
۳-بازار چند نرخی
🔴
(با محاصره اقتصادی٫ برای کسری بنزین از ترکیه و امارات و ونزوئلا سوخت وارد نمی‌شود،  روسیه نیز خود کمبود بنزین دارد)
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145667" target="_blank">📅 09:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145666">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1a3ab30eb.mp4?token=pTMs1mxwvm37hK1bMb2sRRtpyGUYaPBSCQQXmRTyZOydteuQtPzAeNzJRySbGokOxvrd0Crm-4kBdTnmeb8mvS5MeIbDRXGo1qUyIgfenTAYBGSVK4yCeTzJcxlheXaseJG7y7Ezr9RCIgHlxL3KauUpd8x-h2SMsgxS3TzPYwWorxkT5A75jsBXNYC3YrYqYlTVeJ6g6tCfLaXYYAE-1YPEbK15Yr9tdh7qUM6WAXlfrIOAogJFxi860wJ92ZFHuGW2j0XnEvlo6Jt7_jrHQvhDo2fIxdTyUhQM_3F-7oCUEOXgLN6oXv_aoaQzYojDuUY0H_PzWgoftjFtUo1Jwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1a3ab30eb.mp4?token=pTMs1mxwvm37hK1bMb2sRRtpyGUYaPBSCQQXmRTyZOydteuQtPzAeNzJRySbGokOxvrd0Crm-4kBdTnmeb8mvS5MeIbDRXGo1qUyIgfenTAYBGSVK4yCeTzJcxlheXaseJG7y7Ezr9RCIgHlxL3KauUpd8x-h2SMsgxS3TzPYwWorxkT5A75jsBXNYC3YrYqYlTVeJ6g6tCfLaXYYAE-1YPEbK15Yr9tdh7qUM6WAXlfrIOAogJFxi860wJ92ZFHuGW2j0XnEvlo6Jt7_jrHQvhDo2fIxdTyUhQM_3F-7oCUEOXgLN6oXv_aoaQzYojDuUY0H_PzWgoftjFtUo1Jwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امارات به لنج‌های ایرانی اجازه بارگیری نمیدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/145666" target="_blank">📅 08:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145665">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
تانکرترکرز: ۷ میلیون بشکه نفت آماده عبور از هرمز با حفاظت آمریکا است
🔴
داده‌های کشتیرانی TankerTrackers مدعی است تانکرهای حامل حدود ۷ میلیون بشکه نفت و گاز در آستانه عبور از تنگه هرمز تحت حفاظت ایالات متحده قرار دارند.
🔴
این مجموعه همچنین اعلام کرده روز گذشته ۱۷ مورد انتقال کشتی‌به‌کشتی نفت و گاز در خلیج عمان شناسایی کرده که حجم محموله‌های آنها در مجموع به حدود ۲۴ میلیون بشکه می‌رسد.
🔴
این ارقام نشان می‌دهد با وجود ریسک‌های امنیتی، تلاش برای حفظ جریان صادرات انرژی از مسیر هرمز همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/145665" target="_blank">📅 08:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145664">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از منابع مطلع:
بازجویی از حدود 50 عضو ستاد مشترک ارتش در رابطه با افشای اطلاعات به رسانه‌ها درباره جنگ ايران.
🔴
این تحقیقات با نظامیان بر نشت اطلاعات مربوط به کاهش ذخایر مهمات حیاتی ارتش متمرکز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/145664" target="_blank">📅 08:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145663">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=kh33Wvnh1wC3oHMgdhAneeO3f8GaI7rgrO4CpA-EVfSXK75QFHpOF8Ffoh0wIKIftBbO7PQOf927R1JzHdsJOH-YBSJqRFeJEH5tnr_hI2PscQb8CPkF9dHF03cc1OaGPcnaH4xTnisfgF-LNzwVmHFptNojlQHUdmnv6lCgaz04EGLuaIMS47Lz8KkHeop3B2Wy83qb5UTu7hdISp0G51drnnPBrYDqF6aqBu0_qVCPx7MbUio-JGmPyBPZ3CNUc4NhMB25m7qVGUSN-wbocLyFg0GquvufYbC-wIZpc3dXmcPFznmzrpES8Q4voOEzIFNkxyH5LdzbWv4RJhz4Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=kh33Wvnh1wC3oHMgdhAneeO3f8GaI7rgrO4CpA-EVfSXK75QFHpOF8Ffoh0wIKIftBbO7PQOf927R1JzHdsJOH-YBSJqRFeJEH5tnr_hI2PscQb8CPkF9dHF03cc1OaGPcnaH4xTnisfgF-LNzwVmHFptNojlQHUdmnv6lCgaz04EGLuaIMS47Lz8KkHeop3B2Wy83qb5UTu7hdISp0G51drnnPBrYDqF6aqBu0_qVCPx7MbUio-JGmPyBPZ3CNUc4NhMB25m7qVGUSN-wbocLyFg0GquvufYbC-wIZpc3dXmcPFznmzrpES8Q4voOEzIFNkxyH5LdzbWv4RJhz4Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون وزارت ارتباطات :
حتی اگه جنگ بشه هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/145663" target="_blank">📅 08:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145662">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کپلر: کشتی الغشامیه که حامل گاز طبیعی مایع بود و در کریدور جنوبی تنگه هرمز، تحت اسکورت آمریکا حرکت می‌کرد، از ادامه عبور انصراف داد
🔴
بر اساس داده‌های رهگیری کشتی‌ها از شرکت تحلیل کپلر که در اواخر مرداد ماه منتشر شد، کشتی الغشامیه به همراه چهار نفتکش دیگر حامل محموله‌های LNG از تأسیسات صادراتی رأس لفان قطر، به سمت شرق و تنگه هرمز در حرکت بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/145662" target="_blank">📅 08:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145661">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=UY2q1D-ebvIDJ0paPzkdO0MuN06NvEhnqw8a_brK3M_Xm9MSVXUa9uQMX1NBNFQCWu8WpAZI-6XgMS9uNY2tS8tCTBW2Ko1ZHQOtN1AFUHx6cBB13tNq2JmJKshdwUfPiMhusSW1DaJ5sm1SlCsvXJ6wwRK3KUtfwJr-HW4v8dYHUZ9hj23qNUmXmEkG92LqWwpxagjrKfb5I5rgpL6QdQDOS7s8unIxUE77PaIVaNafOf65NQTzRECUa156GrXIhVEvHCaXgq5u6QA0zKspB-vF7HIZPCwE9b2PtDCNCbiw3craySyZcWZtwjTc1KeTmObVNOMXJhLAaY9Hh2KmDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=UY2q1D-ebvIDJ0paPzkdO0MuN06NvEhnqw8a_brK3M_Xm9MSVXUa9uQMX1NBNFQCWu8WpAZI-6XgMS9uNY2tS8tCTBW2Ko1ZHQOtN1AFUHx6cBB13tNq2JmJKshdwUfPiMhusSW1DaJ5sm1SlCsvXJ6wwRK3KUtfwJr-HW4v8dYHUZ9hj23qNUmXmEkG92LqWwpxagjrKfb5I5rgpL6QdQDOS7s8unIxUE77PaIVaNafOf65NQTzRECUa156GrXIhVEvHCaXgq5u6QA0zKspB-vF7HIZPCwE9b2PtDCNCbiw3craySyZcWZtwjTc1KeTmObVNOMXJhLAaY9Hh2KmDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از منطقه میفادون، جنوب لبنان، پس از حملات سنگین اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/145661" target="_blank">📅 08:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145660">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a9c103ed7.mp4?token=cqKstRQjFN5h3vnztEJtudiOip1uTcW9FNam-xzwBAVBm6IZKwQjc2_V4DOtuiKDqoJOJ1p0JeJUJ00d9QSLf-g4gCLuUdwcvUCSf_ptKbl4SqfNp4XskAay1pjB-Wba26UOAkktcw6HKEi0wKM2UggellxGRKpul2TzFhvCFiP9Zvq1FLB7heWhcVoJO-A9FfiERSrF8Joc4V3A55XqA4e-4zoj_yHRh81EiG1vfNetOMq0H72GUQLdVIHC8LMcxqRmh0kkX25fI-TI1UjJCZEcLSMfZZpy3q-Dvq_cq2s_9OEmC3gx_O_De_ESoEC_HrJR8dWFwOXHzSg7AqOwag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a9c103ed7.mp4?token=cqKstRQjFN5h3vnztEJtudiOip1uTcW9FNam-xzwBAVBm6IZKwQjc2_V4DOtuiKDqoJOJ1p0JeJUJ00d9QSLf-g4gCLuUdwcvUCSf_ptKbl4SqfNp4XskAay1pjB-Wba26UOAkktcw6HKEi0wKM2UggellxGRKpul2TzFhvCFiP9Zvq1FLB7heWhcVoJO-A9FfiERSrF8Joc4V3A55XqA4e-4zoj_yHRh81EiG1vfNetOMq0H72GUQLdVIHC8LMcxqRmh0kkX25fI-TI1UjJCZEcLSMfZZpy3q-Dvq_cq2s_9OEmC3gx_O_De_ESoEC_HrJR8dWFwOXHzSg7AqOwag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روحانی: اگر قرار است با قدرت‌های جهانی ۲۰ سال دیگر بجنگیم، باید قبلش از مردم بپرسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145660" target="_blank">📅 08:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145659">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f34f2cc3.mp4?token=LuFi2iXEPuplMtYx4NGqpqnbBqmjPuIhQeFot9TuejkppxuMDL_NoaYtC63EVd0I1LT8W_DXwIEA-_9arOL-1ziSMl-Vad4Jqg7ZDy7r8ZqwbtGSMmpXbYxLsqb1rkF6ZJ_CZhs3isB0djwv0LBbEgj2N-9pI7F-ZZMQO5Fcyu7mUKRM0Nx9KAUCIARymXJtePlrHjglSlZJSyW89JVWs8tTtjMk8KOZsC-CumbjkH3VI-H7hF1ZABSJbQCf5chzDWyReiB4WxlSxWeMch2mC4SNz8ngYx2HUESleqwU4i7Ber-VmDON9WAeHzlwh5ZB7WZ9vFEH8rC8_8uJzKiuEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f34f2cc3.mp4?token=LuFi2iXEPuplMtYx4NGqpqnbBqmjPuIhQeFot9TuejkppxuMDL_NoaYtC63EVd0I1LT8W_DXwIEA-_9arOL-1ziSMl-Vad4Jqg7ZDy7r8ZqwbtGSMmpXbYxLsqb1rkF6ZJ_CZhs3isB0djwv0LBbEgj2N-9pI7F-ZZMQO5Fcyu7mUKRM0Nx9KAUCIARymXJtePlrHjglSlZJSyW89JVWs8tTtjMk8KOZsC-CumbjkH3VI-H7hF1ZABSJbQCf5chzDWyReiB4WxlSxWeMch2mC4SNz8ngYx2HUESleqwU4i7Ber-VmDON9WAeHzlwh5ZB7WZ9vFEH8rC8_8uJzKiuEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موتور نیسان پاترول 2026 تو حالت عادی ۵۰ سال بدون مشکل کار میکنه و باز نمیشه
🔴
بنزین بی کیفیت باعث شد ۷۰ میلیارد تومن ماشین، سوپاپش ذوب بشه و موتورش بیاد پایین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/145659" target="_blank">📅 07:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145658">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/145658" target="_blank">📅 01:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145657">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpdzuqHqNrLadSqEoHVTMoxuC8PTz023InJL9pO7YYBkFJeX7sOeCu_CmLrDFI-YrrqrrPWJTxQ5C_Ard56RL4BOJlAMQ9brJ1vpSuIRZ09ngKCygMOO4YctknPsEHJk0rgDRVOfTVnnsFpKVFXMYrqYU3YKKlMhrc4EH674p4fas_Iv5Q6_H2fFEXxJbK7uJdvJkv9ec-VUdv1Qo2-EPfRkKTwvEJy1AzKCO3m3zsgnLsoM-1ZO5xD07EGQfwP-eMwHdczKn7iLWRn95XotAEahOeBlKzxXrOFXzCCmIrn4Noi5fm6Osw55uYtrEPrfIiy1BjtxEU8q2JZWW8CMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
اگه اجازه بدن من فردا عازم لبنان میشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/145657" target="_blank">📅 01:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145655">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=Dk2afqOEOzZ9FmI9-Pk7JP_pfI9FBpIsM-S9Z9yPYZsHAzZ71q1pRNA7KJSWgFiCa3vEz0vMR76Zb3lhDu1LIBWyFnnMpm1q7_vjx8pEEhiG5tePnzcjRginCf0WcBBrSgNksihE5Zln_Kzn8VkPV5BnD-9jLkGEqoGNh4mKtSuvu3UAqvUQgIcbw_Qc_agsxNzown2Un1OJmpLjrGaakd7DwgGg_zxWZQ_xSbc6ZrOtoXeYWZ1G8YuFdsIOiqnYcRB7KZUZflKtNxiBFHngnIbUVvYtLz-0zlxWEB7gtiW3TNSttMq7BTpoxq4Ip_JLhSW3MU9T4V_P_7TCLN04Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=Dk2afqOEOzZ9FmI9-Pk7JP_pfI9FBpIsM-S9Z9yPYZsHAzZ71q1pRNA7KJSWgFiCa3vEz0vMR76Zb3lhDu1LIBWyFnnMpm1q7_vjx8pEEhiG5tePnzcjRginCf0WcBBrSgNksihE5Zln_Kzn8VkPV5BnD-9jLkGEqoGNh4mKtSuvu3UAqvUQgIcbw_Qc_agsxNzown2Un1OJmpLjrGaakd7DwgGg_zxWZQ_xSbc6ZrOtoXeYWZ1G8YuFdsIOiqnYcRB7KZUZflKtNxiBFHngnIbUVvYtLz-0zlxWEB7gtiW3TNSttMq7BTpoxq4Ip_JLhSW3MU9T4V_P_7TCLN04Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
معاون وزارت ارتباطات :
حتی اگه جنگ بشه هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/145655" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145654">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نتانیاهو: جمهوری اسلامی سقوط میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/145654" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145653">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">خواستیم روزیمان حلال باشد
جوانیمان حرام شد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/145653" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145652">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فعالیت پدافند هوایی اسلامشهر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/145652" target="_blank">📅 00:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145651">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxIebNQYTgd1XvqjoMlyseNzLKaQNyC6KX8BsOhfns0QfAebAzBOzdlwtiOUSU3AQ3YQUm1y5nX-qvgpPcVbeHdjnBchB04QOIuy2q2K07_Dyw3A8c9nOHRHDhiPef2cxiduJuC91LK5et4bCGMKEHH6rduJ2_5h_X1L-u8gAlO9xsKx_RAEhn0YiEJTV-H6Mhv-FgATKqUurXknFY-JfZHe98LqOW61mFFkU22LFt_hDHd9UTHZO57DOkVVCRRcOH5OQUpPrvskh8tzcXjVFVxZj1F3faspfjaUqRbMs0CsLVyifpSWsyDDZ5H3NlZU24gi3dBcWkeJjwblSCBsng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این وسط گروه هکری عدل علی تصاویر برهنه و منشوری مسیح علینژاد رو منتشر کرد
😐
😐
😐
😐
😐
🚨
مشاهده فوری عکس‌ها</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/145651" target="_blank">📅 00:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145650">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=HVnBknBIgrQUKzfeyfW6mBa1tFRdvwEygc9PzBwqbI_jLxIvhjXfin8mjIn533_nfmAykURakmd23iCrkT-6teexb3qhWR0MI_D-n116VWA5ufygHQoy8Am8JdQsyrmj-lFwG6VwTC0MrThoEoE5w9YVYnKntnU4VnoqjtFXcwVVVp57bZIcnjgKfawVghpqI4_rxy8FHMRUgJKAaGR__lJTt974O1B9sZ8qTJg3d9-PB5edocU2otZNSHpsNvMhLVvuICf4ntkO0JAn-egQ31Ugg1665h00201QBBVow2-tcAr3url2-pujfrkh6ty-f76eVHmCopoc-ToABg535Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=HVnBknBIgrQUKzfeyfW6mBa1tFRdvwEygc9PzBwqbI_jLxIvhjXfin8mjIn533_nfmAykURakmd23iCrkT-6teexb3qhWR0MI_D-n116VWA5ufygHQoy8Am8JdQsyrmj-lFwG6VwTC0MrThoEoE5w9YVYnKntnU4VnoqjtFXcwVVVp57bZIcnjgKfawVghpqI4_rxy8FHMRUgJKAaGR__lJTt974O1B9sZ8qTJg3d9-PB5edocU2otZNSHpsNvMhLVvuICf4ntkO0JAn-egQ31Ugg1665h00201QBBVow2-tcAr3url2-pujfrkh6ty-f76eVHmCopoc-ToABg535Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه خبر:
گازوئیل ۳سنت تو آمریکا گرون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/145650" target="_blank">📅 00:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145649">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ارتش اسرائیل: نبطیه(از شهرهای حزب الله) را هم بزودی تصرف میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/145649" target="_blank">📅 00:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145648">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd277</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/145648" target="_blank">📅 00:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145647">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ارتش اسرائیل: پهپادی را که حزب‌الله به سمت نیروهایمان در منطقه امنیتی پرتاب کرد رهگیری کردیم و هم‌اکنون با حملاتی پاسخ می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/145647" target="_blank">📅 00:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145646">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا روز جمعه اعلام کرد که فروش احتمالی مهمات تهاجمی با برد افزایش یافته به عربستان سعودی به ارزش تقریبی ۵ میلیارد دلار را تأیید کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/145646" target="_blank">📅 00:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145645">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945968d3e7.mp4?token=oZGa_KcIG6Ns-Fu60LuTQdKAN-ETNTXF3d2oIUJKS6gfZMQQ5QiaxS3EOOYVjmrAgqP18Tn4nOjS_FKfJ1eHyRtPegQdrPOtijT3Ts0hUra-ydL_k2z-z2Fs-luL33jkqkD0IDP8aimKpNpvIF7Ph9bJX9UgFk4CpWB6soUG5Y8wsswFJIclG-Ymfm16moftnCYe0Poth9N4BqhcG2J6vwZ5GjRM8ksX8afU87v5lF41W0RTcLDwqWi3I069rmITl6beMBPuCcQ-ACPXTA_BLTUffHOAzQ-EDNSnCZQBykKBVuCqaGny7hEQpTGwF7q1nQKRid0Pwmig-NjLGS0jTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945968d3e7.mp4?token=oZGa_KcIG6Ns-Fu60LuTQdKAN-ETNTXF3d2oIUJKS6gfZMQQ5QiaxS3EOOYVjmrAgqP18Tn4nOjS_FKfJ1eHyRtPegQdrPOtijT3Ts0hUra-ydL_k2z-z2Fs-luL33jkqkD0IDP8aimKpNpvIF7Ph9bJX9UgFk4CpWB6soUG5Y8wsswFJIclG-Ymfm16moftnCYe0Poth9N4BqhcG2J6vwZ5GjRM8ksX8afU87v5lF41W0RTcLDwqWi3I069rmITl6beMBPuCcQ-ACPXTA_BLTUffHOAzQ-EDNSnCZQBykKBVuCqaGny7hEQpTGwF7q1nQKRid0Pwmig-NjLGS0jTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: مردم آمریکا چه زمانی باید منتظر حل‌وفصل مسئله ایران باشند؟
🔴
ترامپ: چی؟ انقلاب؟
🔴
خبرنگار: منظورم حل‌وفصل بود.
🔴
ترامپ: فکر کردم میگی «انقلاب» جالب‌تر بود. حل‌وفصل؟ نمی‌دونم
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/145645" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145644">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فرزند سردار تنگسیری: تاکید می‌کنم امکان ندارد بتوانند تنگه هرمز را به صورت نظامی باز کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/145644" target="_blank">📅 23:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145643">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
المیادین به نقل از مقام ارشد ایرانی: به کره جنوبی هشدار می‌دهیم که هرگونه مشارکت این کشور علیه ایران در تنگه هرمز را به منزله مشارکت نظامی در تجاوز تلقی خواهیم کرد
🔴
سئول منافع و اعتبار خود را فدای سیاست‌های بی‌ثبات‌کننده آمریکا نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/145643" target="_blank">📅 23:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145642">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
اعرافی، امام جمعه قم: آمریکا با روش‌های جدید جنگ نامتقارن و چریکی جمهوری اسلامی آشنا نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/145642" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145641">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=rN6Vs00zhEXirDf5Z2Z2VpeDoK27HwUlpOQ1Ibl2j1KLRBXivKfO9-wXITE6p2Zf336U2BibaUJ5t49-abTmmH54EpyQTcokPyNEUCd4Ownl5EPh0oQ4DqafR0gC8KZsbAyVAJOBFiiElvUWlGfiZhB2ZpWUyf4HQ9iBOLA4prBLhhH_MO7riUynEYOgltNOBaXAwxYxXPw52YSPF5Ywkry53oW7sdmnnFL39V-1vR__v2R8dlLpC8U3SbRCNxP4LMh8LOk4cbrMMfvg3kNlZ7DO20XfhrJF20UXaPWE9cMP8v4BlEqcxNg8-kg7DEuhbFzUpCd7hXDYIqwTfHvJKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c61211abd.mp4?token=rN6Vs00zhEXirDf5Z2Z2VpeDoK27HwUlpOQ1Ibl2j1KLRBXivKfO9-wXITE6p2Zf336U2BibaUJ5t49-abTmmH54EpyQTcokPyNEUCd4Ownl5EPh0oQ4DqafR0gC8KZsbAyVAJOBFiiElvUWlGfiZhB2ZpWUyf4HQ9iBOLA4prBLhhH_MO7riUynEYOgltNOBaXAwxYxXPw52YSPF5Ywkry53oW7sdmnnFL39V-1vR__v2R8dlLpC8U3SbRCNxP4LMh8LOk4cbrMMfvg3kNlZ7DO20XfhrJF20UXaPWE9cMP8v4BlEqcxNg8-kg7DEuhbFzUpCd7hXDYIqwTfHvJKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از منطقه میفادون، جنوب لبنان، پس از حمله اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/145641" target="_blank">📅 23:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145640">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4plMtd9lJ8t5-w8QzvusW4-NhLhQj2tbhTZn22BmV50M6am5PRAPQlmHpyEitzEux8x1HeT6y4os_VLGDKVyAriKb-MiVi3dgDQJvr4_5Hgo31oCGDfV6zaa2E4xGciBvYBf_H2jCmPUPrsp8GwwBcjvmvFek67P3W51oy59f76zEkoRmJOjhS-QoLaNtEr02ltG190PJQLzGYoZ1DyZLbAvquH2TbtVhXvZhZR3KgaYTbuWyJ-EOQ3uHoPbG8TBVLKFjjrqm5OfJl2NtEbrv1y4NueZ8lqIvIoWQhNUz7jTX598h_2yuVi61YR4xMLOay-D5moLbUMmgysSbxHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایید حمله پیشدستانه ایران توسط رئیس کمیسیون امنیت ملی
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/145640" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پولتیکو: ترامپ قصد دارد به‌طور گسترده برای جمهوری‌خواهان کارزار انتخاباتی به راه بیندازد، اما نامزد‌ها نگران‌اند که حضور او شانس انتخاباتی آنها را کاهش دهد
🔴
برخی از این نامزد‌ها در گفت‌و‌گو‌های خصوصی به تیم ترامپ گفته‌اند که به حوزه‌های انتخابیه آنها نیاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/145638" target="_blank">📅 23:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ درباره کانادا: اگه ما نمی‌خواستیم با کانادا تجارت کنیم... فکر نمی‌کنم کانادا اصلاً وجود داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/145637" target="_blank">📅 22:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ: اگه می‌خواید به‌عنوان یک ایالت ثروتمند بشید، باید برید سراغ مرکزهای داده.
🔴
اگه می‌خواید با فقر و جرم‌وجنایت دست‌وپنجه نرم کنید، به نظرم مرکزهای داده رو تأیید نکنید.
🔴
خب، انتخاب با خودتونه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/145636" target="_blank">📅 22:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
دونالد ترامپ درباره جنگ اوکراین گفت: «در مسئله روسیه و اوکراین یک مشکل شخصیتی وجود دارد. زلنسکی و پوتین واقعاً از یکدیگر متنفرند؛ نفرت شدیدی میان آن‌ها وجود دارد.»
🔴
او افزود: «این نفرت در مسیر حل‌وفصل مسائل میان آن‌ها مانع ایجاد کرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/145635" target="_blank">📅 22:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ در مورد تنگه هرمز: در حال حاضر، خطوط لوله در حال ساخت هستند. جاده‌ای از طریق سوریه در حال ساخته شدن است؛ در واقع، این جاده باز است. مردم با کامیون‌های بزرگ حامل نفت از طریق سوریه تردد می‌کنند.
🔴
تلاش‌های زیادی برای ایجاد جایگزین‌هایی برای تنگه هرمز در حال انجام است.
🔴
تنگه هرمز دیگر آن‌طور که قبلاً بود، نیست.
🔴
ایران، اگر نتواند عاقلانه عمل کند، که من نمی‌دانم آیا آن‌ها قادر به این کار هستند یا خیر، در نهایت به تنگه‌ای به نام هرمز دست پیدا خواهد کرد که دیگر آن اهمیت قبلی را نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/145634" target="_blank">📅 22:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران گفت: «به شی جین‌پینگ گفتم لطفاً در موضوع ایران دخالت نکنید.»
🔴
او افزود: «چین واقعاً درگیر این موضوع نیست و دخالت بسیار کمی دارد؛ در حالی که می‌توانست نقش و دخالت بسیار بیشتری داشته باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/145633" target="_blank">📅 22:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها رادار نصب کردند، زیرا ما قبلاً آن را از کار انداخته بودیم. حالا ما آن را برای بار دوم از کار انداخته‌ایم. اکنون ما هیچ فعالیتی را مشاهده نمی‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/145632" target="_blank">📅 22:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145630">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ درباره روسیه: ویتکاف و کوشنر پیشنهادی را برای پایان دادن به جنگ به مسکو ارائه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/145630" target="_blank">📅 22:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145629">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ: هشت جنگ را پایان دادم، اما جایزه نوبل را به من ندادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/145629" target="_blank">📅 22:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145628">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: هر یک از بخش‌های مهم این کشور که ما برای آنها هزینه می‌کنیم، حدود ۶۵۰ میلیارد دلار هزینه دارد.
🔴
ما باید به سطح ۱ درصد برسیم؛ نباید به سطح ۴ درصد برسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/145628" target="_blank">📅 22:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145627">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرنگار: ۱۸ نفر در جنگ با ایران جان خود را از دست داده‌اند. ما شاهد حضور نیروهای نظامی برای مدت زمان بی‌سابقه‌ای بوده‌ایم.
🔴
ترامپ: بی سابقه؟ مگه نمیدونی ما چه مدت در ویتنام حضور داشتیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/145627" target="_blank">📅 22:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145626">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68db4c2c5.mp4?token=L3gdl4Vbkvqyv2FWfcBvVymZqE2wLxRfGuZmRbB-Q5ethmGxG20BZ5V2-QW5taQtm8XIRpnUnseWL8S4lyYGHC6VLzmzdQPl4RTn7qo0wh0xwFogEPxiVhtgqjlxFs4bCVZzFkgT_d4vL22QjNasFyYwJgd25D2hj0_XOi8R-F6gee2EiDwUOiJFnW6_e7DlsmQZCjS_-QCyjnFf5vJbPQuJLWLDjibO3KkBhrmNknuEJXDOOmgdbTdUMdvu43LUY3T0niNde426CI9zWGk6df088wzoP-cG7slYr89uMkr9GxA13SnazeKDalM-YL8oEbVxEKRKEVYiRzyDckCa5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68db4c2c5.mp4?token=L3gdl4Vbkvqyv2FWfcBvVymZqE2wLxRfGuZmRbB-Q5ethmGxG20BZ5V2-QW5taQtm8XIRpnUnseWL8S4lyYGHC6VLzmzdQPl4RTn7qo0wh0xwFogEPxiVhtgqjlxFs4bCVZzFkgT_d4vL22QjNasFyYwJgd25D2hj0_XOi8R-F6gee2EiDwUOiJFnW6_e7DlsmQZCjS_-QCyjnFf5vJbPQuJLWLDjibO3KkBhrmNknuEJXDOOmgdbTdUMdvu43LUY3T0niNde426CI9zWGk6df088wzoP-cG7slYr89uMkr9GxA13SnazeKDalM-YL8oEbVxEKRKEVYiRzyDckCa5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره پوتین: من با پوتین صحبت می‌کنم؛ من او را خیلی خوب می‌شناسم. پوتین قصد حمله به خاک کشورهای عضو ناتو را ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/145626" target="_blank">📅 22:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145625">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d6d722f3.mp4?token=SqbaW6HczeYgmukkYtXLhvupFQ-98KTAHYJZbaFjo6_WQliZvYGSirtk5jbSriCB5psOqJuJIbXHzN9rDwea08jOBp1Tzq90ggSSkiOcGOI-BrXFTOsOBYGhwIe55aoUyFfsT8qcIZ2xmFnZu7ajNA-GuA2KTWwisDjYo9eM_2j511Spo1psZYcHJkUAMYGxJGy1ibRqK18ToncmO3y52ar3078QxelvF4oaiXZkYzWitt5pPf5ZeJkppSYo3fJJcqyo_ya1Lmokghs0Jv9nppLUulbZd1cs_3HLjsdgmjpVQsp8GwrYx1ulOZ9D1DoQ2a5EqhJssO0VyIRQQSBQWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d6d722f3.mp4?token=SqbaW6HczeYgmukkYtXLhvupFQ-98KTAHYJZbaFjo6_WQliZvYGSirtk5jbSriCB5psOqJuJIbXHzN9rDwea08jOBp1Tzq90ggSSkiOcGOI-BrXFTOsOBYGhwIe55aoUyFfsT8qcIZ2xmFnZu7ajNA-GuA2KTWwisDjYo9eM_2j511Spo1psZYcHJkUAMYGxJGy1ibRqK18ToncmO3y52ar3078QxelvF4oaiXZkYzWitt5pPf5ZeJkppSYo3fJJcqyo_ya1Lmokghs0Jv9nppLUulbZd1cs_3HLjsdgmjpVQsp8GwrYx1ulOZ9D1DoQ2a5EqhJssO0VyIRQQSBQWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما ونزوئلا را تحت کنترل خود درآوردیم و در واقع، ایران را نیز به نوعی تحت کنترل خود قرار داده‌ایم.
🔴
در این چند روز، هیچ درگیری مسلحانه‌ای رخ نداده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/145625" target="_blank">📅 22:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145624">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532c884d67.mp4?token=hR71bes4PE5kSXL1Fb2rBAK2NtbrXb13WmEOQujGuZu8VGrAkPwDz1ThS3m6QxzXMQjClQgjFsngmgDpuqjZ3XjocqFjk0tisTb62vAoBi7c9q5DIyutG-Zh05g2TniPyCRZiYFGaOwZbRpeohw_78mGMjiDgs0MZSgNGjomOvgRFwE2hQojm-pe455S0CltHabzRENFktvqN0Ji4-5C-fMFrqSApXbopVcarpTcWtc32vPS1EdcCXF6KanczhYqdEYd6DDQ-P50uK9iWGlcRTOd1Air0HqId6CR0m_HTXPVTGSuv2soMMmzFo31xZ4S-XyeFB-q5ijN-27yiWUTq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532c884d67.mp4?token=hR71bes4PE5kSXL1Fb2rBAK2NtbrXb13WmEOQujGuZu8VGrAkPwDz1ThS3m6QxzXMQjClQgjFsngmgDpuqjZ3XjocqFjk0tisTb62vAoBi7c9q5DIyutG-Zh05g2TniPyCRZiYFGaOwZbRpeohw_78mGMjiDgs0MZSgNGjomOvgRFwE2hQojm-pe455S0CltHabzRENFktvqN0Ji4-5C-fMFrqSApXbopVcarpTcWtc32vPS1EdcCXF6KanczhYqdEYd6DDQ-P50uK9iWGlcRTOd1Air0HqId6CR0m_HTXPVTGSuv2soMMmzFo31xZ4S-XyeFB-q5ijN-27yiWUTq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: اگر این درگیری با ایران جنگ نیست، پس دقیقاً چه چیزی است؟
🔴
ترامپ: من آن را یک درگیری نظامی می‌نامم، زیرا برای ما مسئله‌ای جزئی است؛ یک موضوع بزرگ نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/145624" target="_blank">📅 22:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145623">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: رشد اقتصادی باعث تورم نمی‌شود؛ نادانی باعث تورم می‌شود
🔴
ما باید این امکان را داشته باشیم که به جای اینکه همیشه شاهد رشد اقتصادی در سطوح ۲، ۳، ۴ باشیم، شاهد رشد اقتصادی در سطوح ۱۲، ۱۳، ۱۴، ۱۵ باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/145623" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145622">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: اگر یک کشور با ما رفتاری نامناسب داشته باشد، ما هیچ تعهدی برای انجام هیچ‌گونه معامله تجاری با آن کشور نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/145622" target="_blank">📅 22:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145621">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5G99L4NcA7BFQigV3EZEdrzh0TAdGNtd77OeGelPjyRdvKyfkJIGl0Ev9qshEXI0ACCo8W83jHHRiRueIA5RJDw_c7m_aiIqjj3DqNEgKP3Rb76NnTAbO7wiBhztXDzE0qgO6scE-Kr5nUCgLLl7LD35V0nfcRmjYIDaQNN65wWFvq9-BiJNV8_E9coofaihAntfZ0cyJCyqQuYuUb9TW09NxwLtZD7VR6VGZabt8oGESy6rV1EEP0iDcUBlO4jggWCWn9flvGkOznJmeZb5SNAbbrLDhsz7JBYFeLOOTvev4lzoiiUFfj3_9QMC16KjLv9-yFAVgepFYgZD7N-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هزینه آبدارخانه شرکت بورس انرژی: ناقابل ۱۱.۵ میلیارد تومان!
🔴
صورتحساب کدال منتشر شده از شرکت بورس انرژی نشان می‌دهد در سال ۱۴۰۴ این سازمان بالغ بر ۱۱.۵ میلیارد تومان صرفا هزینه آبدارخانه داشته است.
🔴
همچنین با استخراج صورت‌های مالی بورس انرژی مشخص شد میانگین حقوق دریافتی کارمندان این سازمان دولتی در سال گذشته بطور میانگین ماهیانه ۹۰ میلیون تومان برآورد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/145621" target="_blank">📅 21:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145620">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95b5c30eb.mp4?token=nJAqduqHAb2qTh8g-n4xj-IqvuUzAzJGp4bBoS4eC1n2o3qDinNpkuRx3WgwHdns4Osx04_DYShVEZP4ewxcyypJhmhMSu-HRxFho9luPjoC_xfGD_koY68mLOC1ntme_Imk1yf8cgtxBrT0D6d6DJF1FnhVnQR8keSg5gyFvDSVaN9hdCmSgpeo39I5ouN27VjcuF9_Qvn0V0oR9j-C_zQurHs26M_wTgTwlhECuCdglzDVxqQAGaomKDzL8wJU46fjFbyISgWvfabRwo9S7X_O52suhYY024wtjxMqtw1_9u2I2k81ShOOQO6bWNfZgxjN99crKZkjejv2NqYHug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95b5c30eb.mp4?token=nJAqduqHAb2qTh8g-n4xj-IqvuUzAzJGp4bBoS4eC1n2o3qDinNpkuRx3WgwHdns4Osx04_DYShVEZP4ewxcyypJhmhMSu-HRxFho9luPjoC_xfGD_koY68mLOC1ntme_Imk1yf8cgtxBrT0D6d6DJF1FnhVnQR8keSg5gyFvDSVaN9hdCmSgpeo39I5ouN27VjcuF9_Qvn0V0oR9j-C_zQurHs26M_wTgTwlhECuCdglzDVxqQAGaomKDzL8wJU46fjFbyISgWvfabRwo9S7X_O52suhYY024wtjxMqtw1_9u2I2k81ShOOQO6bWNfZgxjN99crKZkjejv2NqYHug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر یک کشور با ما رفتاری نامناسب داشته باشد، ما هیچ تعهدی برای انجام هیچ‌گونه معامله تجاری با آن کشور نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/145620" target="_blank">📅 21:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145619">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: با فروش احتمالی بالگردهای بل ۴۱۲ به عراق به ارزش تقریبی ۱۵۰ میلیون دلار موافقت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/145619" target="_blank">📅 21:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145618">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9abd049084.mp4?token=CSXQOY24biT-5CBOnXLICV-Q06Rw-IiRp8MdWmrU3IcYmuRthZ-_3ZY0CSiZqXHR_HAUfeWqVxoaeDoe2VnxULWQ3Wr6iH9EjLesLXubj1CSL2hCa41xA2g6waZOPKw1SyWp74FWpW0G7jW_AlD7urjUNk58zH_ZGNGrLX7ufPYnMBxjZtjd33qvi0PupcMyO2TdZJfzrkMWQZ0Sj1F7XED-_jgyxb3-a5s-9byZE1hZJTgPLzHF_zCn0qlvbN7XKBrZPYPPq04Q7QhhgW-8s4IXc4p9No52xu3PPvhETDUwjVL2rkUL-d22kk80hYVwP-KVtJvkWBzOCoRTPU9Siw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9abd049084.mp4?token=CSXQOY24biT-5CBOnXLICV-Q06Rw-IiRp8MdWmrU3IcYmuRthZ-_3ZY0CSiZqXHR_HAUfeWqVxoaeDoe2VnxULWQ3Wr6iH9EjLesLXubj1CSL2hCa41xA2g6waZOPKw1SyWp74FWpW0G7jW_AlD7urjUNk58zH_ZGNGrLX7ufPYnMBxjZtjd33qvi0PupcMyO2TdZJfzrkMWQZ0Sj1F7XED-_jgyxb3-a5s-9byZE1hZJTgPLzHF_zCn0qlvbN7XKBrZPYPPq04Q7QhhgW-8s4IXc4p9No52xu3PPvhETDUwjVL2rkUL-d22kk80hYVwP-KVtJvkWBzOCoRTPU9Siw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین پاک خبرنگار مقاومت در جنوب لبنان: منطقه علی الطاهر سقوط کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/145618" target="_blank">📅 21:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145617">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWujYjioO20AjXtGgyPKXN9oH4FdEv7qk9q5V1uwPvSBTtFqUZb3qeI5dKOEjiOF-YadMQCQzWTvT0PnlRexE5yFUMFXm469MyZkZ34fZi7t34W6HpXO_cNYoxssfMKkvJWs-Tfr3NYq7Gb3mBScBWckzl4tUt3FeV2RAe3OAK_lgv3sRrUFEXcwKnxhCSEjU5uL-YMbS2WWH-B9f1vAsaOWBlkH0Ee8H8XT9k2pUAeBgggYGEstWQLsoujtXbyl2OJjGAhVM-xXHzUE9gG-3ZbjO0T61JmlbBM__oZS-m30g20zxNtRrZ3lZaRBGOB7u9cpE9dZ1bfbazNa7LH82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه NBC: سربازان آمریکایی پس از درگیری با ایران، دوره استراحت خود را در یک تفرجگاه گردشگری در تایلند سپری می‌کنند؛ در حالی که فضای متشنج ناشی از جنگ با ایران همچنان حاکم است. این صحنه، تضاد میان فضای تفریحی تفرجگاه‌ها و وضعیت آماده‌باشی را که ارتش آمریکا به دلیل جنگ در آن قرار دارد، به تصویر می‌کشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/145617" target="_blank">📅 21:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145616">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T22MUkWbqcDuIqeRCPTbzRo1B349jZCGYs6pkUxP_E6KRyPqDSvaPnA_JtyqBZXZQASekJ2jSMjq3i56phyIdw3qksptyo8ymLvH-dxutb5abFNVxmokgj42GJP4DCE7s7J8LfWSl6wZAI5sd9Gf13kMmk_r4fdtOYSHtED3utVNpujemdQngzVFUQxyTxrWWN4wWWONPbE04kN1HCzbJ3k3Pd4L9RW1X1EF5MrM0iSA46LJstO2mgSmphFTeJeGgbUb3JKUhtHkJ-XpHwS6rf9il8NMoRZSXFx6rVvux0YH1ay0ivi-L0vsWc4WhUEd3fZDfwG6ug1lDpB0H_aKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وب‌سایت رسمی کاخ سفید بازی‌های ویدیویی راه‌اندازی کرده که در آن‌ها کاربران مهاجران را دستگیر کرده و دیوار مرزی می‌سازند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/145616" target="_blank">📅 21:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145615">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
به گزارش سی‌ان‌بی‌سی، آمریکا یک بانک ترکیه‌ای را به اتهام تسهیل فعالیت‌های مالی مرتبط با ایران تحت تحریم قرار داده است.
🔴
هم‌زمان، اسکات بسنت، وزیر خزانه‌داری آمریکا، تلویحاً اعلام کرده که در مقطع کنونی برنامه‌ای برای اعمال تحریم‌های بانکی بیشتر وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/145615" target="_blank">📅 21:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145614">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKOOVm7TUTAJH5VaXUpZVlz-ooZw2i6dXSTX_TPyW1au4ncpb0OVY__GQzytFJslwMyCenrO-vdQcnOx9vbmEAnfXNLX9IQW-uCp3v9qWZuE8KucqwhEePabVUJXcIWYGHeO3nrNZLkuS7kuFcrRHt2mm-qwF9JH6foF9ATRXgB6szLw2hOKX4A3sotLi0wXWIkgvozt7fUMu6LVLRVdUO6IkBwy7wQaas1XgEbCFjgl74s2y5OkWVs3kBYTolJqgVMSY40lPfQw2uCiAh44oGkA_aq69DKt9xooKTJYRwXE7WECJJl7Iafc9tXQCLTQTnU4RQ_DvMHmMKbhgNJ1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرنده همای سعادت تو طالقان دیده شده:
تو روایات دیده شدن این پرنده باعث اتفاقات خوب برای مملکت میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/145614" target="_blank">📅 21:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145613">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F810VOGXaXuK_MjNJ0qNXJD6DS_ITq6pWN68cBIbScotxxVXcozqooFKNPUFfnxmVa_4rBOV7dlmvh020qNYRrtgF9WzklDT20D2zbUPohcwhRhK9QW4OVR5fVOEruPjedPIfTF4e-omEBnpKXh1tD1PgKrDLdOBFvJe0xiZmSTXsYxGedHESyb5YBLiynRXTvanQ3UlROpRA3375_Xp3BJZEoVnd1SSFmM7VEmgO6rEUkxiUYplw_2p1j67dgnXUq8EBhu4Gzp0crCQEEL902mcj1zU6-FJw1Mae47zZm7Gz3ibgEaIBOObdCLAqETUiXdmxrVPv9ks23Tp_SA0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این متن رو داری میبینی
یه نشونه‌ست برای آغاز مسیری جدید از زندگیت تا یاد بگیری که چطوری،خیلی سریع به موفقیت برسی!
💸
✅
اگه میخوای درآمدت چندبرابر بشه
💰
اگه میخوای لایف استایل زندگیت متحول شه
💡
وارد کانال شو بهت یاد میده چطور دلاری پول در بیاری
اینجا میتونی روزانه درامد داشته باشی و سرمایتو چن برابر کنی.
لینک عضویت کانال وی ای پی
✅
👇
👇
https://t.me/+nTm6gDB4A8gyYmFk
https://t.me/+nTm6gDB4A8gyYmFk</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/145613" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145612">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt5TLGTVdpV0c9S5oAUukpUyE4ibfCONoNYiDIMx5TIE_85Oe_xiXkyDbpd0-ckJL0wTYC9lHFKREML97gNZmTknFrPRWa5Agbt_mnfCCXO-D3VdwMrOqttheqyz8-0OXvEbqzpj73JgzPJKx9QS_VQ4YqFD4xqvS8HjyRiJSK2AGQCHLV4J_TkzJrycH5y8FjN0dULd_KmRT7Shstwk5SYQj9fKD0HgDJB8XkiZYGMpM4E-MmIz4M1jWxUYYr-u24SMhLRYi4WrqYYX8-XgrnB4lQpBYLsSGomiSCidn8sU0LUBFNG3dnRmCFJjOYzFz-hnecmwGi4x-KBRGSb3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت
🔴
نفت آمریکا (WTI): ۹۰.۹۰ دلار
🔴
نفت برنت (معیار قیمت جهانی): ۹۵.۶۵ دلار
🔴
نفت امارات: ۱۰۲.۲ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/145612" target="_blank">📅 21:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145611">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
قرارگاه خاتم الانبیا:  حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/145611" target="_blank">📅 21:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145610">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از مقامات امریکایی: ارزیابی‌های اطلاعاتی آمریکا نشان می‌دهد ایران ممکن است به‌جای مذاکره به دنبال طولانی‌کردن جنگ تا انتخابات میان‌دوره‌ای آمریکا باشد
🔴
تهران درک روشن‌تری از توانمندی‌های نظامی خود پیدا کرده و ممکن است در حال بررسی یک تشدید قابل‌توجه تنش باشد
🔴
ممکن است بار دیگر به سطح تنش‌ها در ماه ژوئیه بازگردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/145610" target="_blank">📅 21:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145609">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سخنگوی ارتش: سیاست ما عوض شده و به دنبال حمله پیش دستانه‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/145609" target="_blank">📅 21:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145607">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7d1ENEltAEbvWAR_kqngNVNLWKzC5UCrYW6Gbi4XeiljvI4bDlQHD2UyfzzzhYylS9jU0_g_La1xfWq6-7meJQCku4aIQaFQ2Bv9nmSvhlZt2AP4xnNEmX0NkH8ocAsCeaWQ5yae3LwkpM5FBuOsRPeDFU6pW6pWz1J0UjjxI5ailg9ixZJmdglbpQ8VZPYd4nnpLet6po27254s8jUXKPGS8SHkFmOAXEMTVFTlvYqukjWCQua2w1bPn05pIMfrBQSlabGpk8F_Nm0NFMZiVQqzks7k0-SI1urvr8uywvx6pjqoIzdVT5dzU9PVZd677FH7WxNrlQ6M4WVqeST_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: تأکید چین بر پرورش امنیت مشترک، اصلی را منعکس می‌کند که ایران مدت‌هاست از آن دفاع کرده است.
🔴
کشورهای منطقه باید آینده خود را به دستان خود بسپارند، و ثبات واقعی تنها از طریق معماری امنیتی جدید بومی می‌تواند به دست آید. ایران آماده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/145607" target="_blank">📅 21:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145606">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
کانال ۱۲ اسراییل:
امشب جمهوری اسلامی شروع کننده جنگ بود و به پایگاه امریکا در اردن موشک شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/145606" target="_blank">📅 21:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145605">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مقامات آمریکایی به اکسیوس می‌گویند هیچ گزارشی مبنی بر شلیک موشک به سمت پایگاه‌های ما در اردن وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/145605" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145604">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f8f7a2582.mp4?token=nHJcCdjDamx8uWtZOrOyEP1vwrRJQZeHyJYd9vuxRNGLj5qeyMOqHPLgNOsdMEaod1K3hry3aSNKrax8ZwNJdZFswqC1abTxFkIqXcEhagMrYZ1q2sF7hiZXok1e1MrM4EGvGzgssGdlFwk9MLlFrk-tOj9NCC41cNveHgER5r1ouP4WQLOOussDLHkL0lg5qms7v5v7-Ow7_ndYaJjzYWqF0Ng2y0u4qCvtKnISMtd2Hci_Yx_FZiZ9LawwbRVVBLMnykdv4uvgaNiTXochNKlIOzI10QO_9ReHpirTfqG83im4YYJd0ZbMQuwzm0kCPHTsVhuW3dqTeQk24pcgLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f8f7a2582.mp4?token=nHJcCdjDamx8uWtZOrOyEP1vwrRJQZeHyJYd9vuxRNGLj5qeyMOqHPLgNOsdMEaod1K3hry3aSNKrax8ZwNJdZFswqC1abTxFkIqXcEhagMrYZ1q2sF7hiZXok1e1MrM4EGvGzgssGdlFwk9MLlFrk-tOj9NCC41cNveHgER5r1ouP4WQLOOussDLHkL0lg5qms7v5v7-Ow7_ndYaJjzYWqF0Ng2y0u4qCvtKnISMtd2Hci_Yx_FZiZ9LawwbRVVBLMnykdv4uvgaNiTXochNKlIOzI10QO_9ReHpirTfqG83im4YYJd0ZbMQuwzm0kCPHTsVhuW3dqTeQk24pcgLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری که به طور ظاهری پرتابه‌های موشکی سپاه پاسداران به سمت اردن را نشان می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/145604" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145603">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
گویا سپاه استارت جنگ فراگیر رو زده
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/145603" target="_blank">📅 20:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145602">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری/پرتاب موشک کروز ضدکشتی نیروی دریایی سپاه پاسداران از سیریک به سمت تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/145602" target="_blank">📅 20:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145601">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
این حملات بعد اولتیماتوم فیلد مارشال محسن رضایی به ترامپ انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/145601" target="_blank">📅 20:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145600">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فعالیت‌های پدافند هوایی در شمال اردن، به دنبال گزارش‌هایی مبنی بر پرتاب موشک از مرکز ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/145600" target="_blank">📅 20:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145599">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری/هم اکنون آغاز حمله موشکی ناگهانی سپاه به پایگاه های آمریکایی در اردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/145599" target="_blank">📅 20:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145598">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری/هم اکنون آغاز حمله موشکی ناگهانی سپاه به پایگاه های آمریکایی در اردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/145598" target="_blank">📅 20:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145597">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
دو موشک بالستیک حوثی ها مواضعی را در جنوب مستقیم‌الخواخه، در جهت حیس، در جنوب‌غربی یمن هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/145597" target="_blank">📅 20:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145596">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlLVL-_pD6-nV5sfDAQLpUL6IaP70MnA53ogIlt9yGHoqNqwVyDQbVCoGJIDgd6HgeAi9RIZAKJ0MmWUitUuEzkfPNmsHnrRaRIDuqPsArDNODAXODJbzhEbJVLGeIajh6ytVM2kuqAmnD4A_DY4YMifCOFtSXMWH-73ie_59bZCqJO7Cq-pBY94YZ82I56aMNW2pvZqiUTc8WKZ2gR5NIddXlZWb6dsd2wXz0UNBevW0earpO62FC0uF-Hn7sGocUoSn5cyZxJdjR04R2w6yhgwR9SKZceN7POZ1d6IANcTZ_Um5yAITstPu2F0kNZkpJu3DbbI0zDJa-_kea7kIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
چپ‌های افراطی و دیوانه، دموکرات‌ها و کمونیست‌ها ترجیح می‌دهند ما در جنگ با ایران شکست بخوریم، تا اینکه دونالد ترامپ جنگ را برای آمریکا ببرد.
🔴
به عبارت دیگر، آن‌ها ترجیح می‌دهند ما ببازیم تا اینکه پیروز شویم!
🔴
این‌ها آدم‌های بسیار بیماری هستند که از TDS شدید رنج می‌برند؛ همان چیزی که گاهی از آن با عنوان سندرم جنون ترامپ یاد می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/145596" target="_blank">📅 19:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145595">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecaed841d6.mp4?token=kXvXcXsKYZGy48pUUNcIyuWtMOkeTyZImDjgbk7WGli-JEJkQMyfk3fDsxZi0WHeoE4VHQAc9WIVhmBLJFMcrcElbBsOK9Nl4ySvjl6ODSzkepqpvauSmHU7Qjc-M_vFuh7VsdRpUmN8bEbWONUsfCXP4XooDtiKXsBTp7vj_8CEhC8OIU8-Q105lAhA75Mp2TjY9M6dBDgIrZRw-zGOkeVk7cFbFTG_H3DIkPxsi5nXFn9mRZX0VaGyiAUUOGkndfZH8CDZ9H47S09Vt_UmMRl_LOuKbkhS7ImVjrEYsu3i9FUcCob8gyIq1q_IrH6MWWknex9w_i7s-y-mVn6FYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecaed841d6.mp4?token=kXvXcXsKYZGy48pUUNcIyuWtMOkeTyZImDjgbk7WGli-JEJkQMyfk3fDsxZi0WHeoE4VHQAc9WIVhmBLJFMcrcElbBsOK9Nl4ySvjl6ODSzkepqpvauSmHU7Qjc-M_vFuh7VsdRpUmN8bEbWONUsfCXP4XooDtiKXsBTp7vj_8CEhC8OIU8-Q105lAhA75Mp2TjY9M6dBDgIrZRw-zGOkeVk7cFbFTG_H3DIkPxsi5nXFn9mRZX0VaGyiAUUOGkndfZH8CDZ9H47S09Vt_UmMRl_LOuKbkhS7ImVjrEYsu3i9FUcCob8gyIq1q_IrH6MWWknex9w_i7s-y-mVn6FYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر پرتاب موشک از اصفهان منتشر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/145595" target="_blank">📅 19:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145594">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751015f665.mp4?token=PVlz1QtOkYpFsEZiquWaFkaBSFeI61dR9mVGRm4evFgNq-AkFLmk_Zv_dd7P0pSLumSmCO3AaTFTzilNOjPW8xaGnsmCqLjx39r3LhhykKV1kgnTKSquwJ3gwfYHvO3Tvu5QTixNit8PVJCPWUkamPRqSwTlAZgA-slZDbNnZ1ymO-H6eWKu99UYm32132PHf-qb5H0PG57jj80RWHLA7fMU3leM0WrnXERVe0X9UyePYYbi2Nu7fGIS5fV6Kygl0Qh_g9jf6CYzT6kr11yBwBWBHmEnraOpDah2zdzpXJ0vxCU7TOpfksHrzOkcxLScHHRhbMlzAsPp8vV-si9gAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751015f665.mp4?token=PVlz1QtOkYpFsEZiquWaFkaBSFeI61dR9mVGRm4evFgNq-AkFLmk_Zv_dd7P0pSLumSmCO3AaTFTzilNOjPW8xaGnsmCqLjx39r3LhhykKV1kgnTKSquwJ3gwfYHvO3Tvu5QTixNit8PVJCPWUkamPRqSwTlAZgA-slZDbNnZ1ymO-H6eWKu99UYm32132PHf-qb5H0PG57jj80RWHLA7fMU3leM0WrnXERVe0X9UyePYYbi2Nu7fGIS5fV6Kygl0Qh_g9jf6CYzT6kr11yBwBWBHmEnraOpDah2zdzpXJ0vxCU7TOpfksHrzOkcxLScHHRhbMlzAsPp8vV-si9gAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت: نفت ۴۰ دلار خواهد شد!
🔴
در واقع فکر می‌کنم بعد از این، در بازار نفت با مازاد عرضه زیادی روبرو خواهیم شد. احتمالاً قیمت نفت خام را در محدوده ۴۰ تا ۵۰ دلار خواهیم دید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/145594" target="_blank">📅 18:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145593">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=uNjmA7cXmoI7ZKZGfyzXy544NdC9_24AjrWWRvoikdNnq4lIgip6ktw_Y2H1Ogxtkrk_Vc20pGgY9w1jZ58m869pvJXvZ5QYqJSjByNNGO8wAihHzSfiMXJPUB-wsROSifvJEuyqxTcsbu0lqSBShtVUtfW8j7TmB24TTfaBDbVCTQHbZS2qkpE6gziPGmHzUxmSI4SP9L2UrTig4ZSolCGNJKexUaxre0IaDc7NWcPDzCo-PeNUnT-8jEOJpq4IU3EP_g-PpQVE-_dWiXAens_w0giRkMVVy9CEDNyXkDmY7DbDl7vzGLDM2blV2kog6JwlIgGyI9Z7U0-9EY4c-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=uNjmA7cXmoI7ZKZGfyzXy544NdC9_24AjrWWRvoikdNnq4lIgip6ktw_Y2H1Ogxtkrk_Vc20pGgY9w1jZ58m869pvJXvZ5QYqJSjByNNGO8wAihHzSfiMXJPUB-wsROSifvJEuyqxTcsbu0lqSBShtVUtfW8j7TmB24TTfaBDbVCTQHbZS2qkpE6gziPGmHzUxmSI4SP9L2UrTig4ZSolCGNJKexUaxre0IaDc7NWcPDzCo-PeNUnT-8jEOJpq4IU3EP_g-PpQVE-_dWiXAens_w0giRkMVVy9CEDNyXkDmY7DbDl7vzGLDM2blV2kog6JwlIgGyI9Z7U0-9EY4c-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده، بِسنت، درباره جمهوري اسلامي ایران:
ما یک بانک دیگر مرتبط با رژیم ایران را تحریم کرده‌ایم. هفته گذشته، یک بانک مصری با پنج شعبه در دبی را تحریم کردیم که ۱.۸ میلیارد دلار به رژیم داده بود.
ما امروز یک بانک دیگر را تحریم خواهیم کرد و احتمالاً هفته آینده نیز یک بانک دیگر را تحریم خواهیم کرد.
ما به سیستم مالی می‌گوییم: بازیگران بد، ما می‌دانیم شما کیستید. شما می‌دانید که کیستید. تمام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/145593" target="_blank">📅 18:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145592">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=W_49c67_mf88iyE-9USKie6YpTMvKfPNY33jkkI0Qd7lv59AG8ZbhXRRCfhgeY1YB5_UmWQwPwZsFKUg-0qjlABAufodvwVmho67I0KO4U2LuxIJ2TTjkwbOENAVJqyWitx18iLidNqZ3TZwKccUstDdEQ0NkS-plAacix0_DgUgOldLgpQKTeTfkvsFmyhtsO04zfyYXxt2Z_tBZOgQr1hAZOsrE4LEGi9p_fVej7_Czl1AzMMJ2kD4Vv2Qrb9MaX3NqiOX4gi40IvPuEiIKFWEbVji7v8yqR2TcnhZBovMN4t98lAUJV5GKdJLH9s11GGLBxdzTuECVC85ZbKm9qS_lVQ4gY__4NPr4Yjz_0mE_EkEeRRvqlZN2sjSgi3nvUnnifLoKts1XyVRaMxuLkIigzMrng9CarexUNVa07_HPbgWEVLitPQ2KSEDBGlBIvD45I1rnyz3RaoQAkzBjq3odcQ6fwMDFS7YFuxl6PHwOrMGMuucHghhbWwePzefCFCwaiFfUoUb9HimP5Z-LWh9w7iFuOKBXRzuwAoWveyI8FurQYnClHfCaOqzhcKbRMy31ygr_uwT6mMjzsGv5wFF0MrLa1pCI4Ku0P5FfOhGWPTrFW8EK2hEUOc5Z5EJ0rOEiE_QJ81bbYj--408N-qcAJ7X3ekghTcQ25QjLXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=W_49c67_mf88iyE-9USKie6YpTMvKfPNY33jkkI0Qd7lv59AG8ZbhXRRCfhgeY1YB5_UmWQwPwZsFKUg-0qjlABAufodvwVmho67I0KO4U2LuxIJ2TTjkwbOENAVJqyWitx18iLidNqZ3TZwKccUstDdEQ0NkS-plAacix0_DgUgOldLgpQKTeTfkvsFmyhtsO04zfyYXxt2Z_tBZOgQr1hAZOsrE4LEGi9p_fVej7_Czl1AzMMJ2kD4Vv2Qrb9MaX3NqiOX4gi40IvPuEiIKFWEbVji7v8yqR2TcnhZBovMN4t98lAUJV5GKdJLH9s11GGLBxdzTuECVC85ZbKm9qS_lVQ4gY__4NPr4Yjz_0mE_EkEeRRvqlZN2sjSgi3nvUnnifLoKts1XyVRaMxuLkIigzMrng9CarexUNVa07_HPbgWEVLitPQ2KSEDBGlBIvD45I1rnyz3RaoQAkzBjq3odcQ6fwMDFS7YFuxl6PHwOrMGMuucHghhbWwePzefCFCwaiFfUoUb9HimP5Z-LWh9w7iFuOKBXRzuwAoWveyI8FurQYnClHfCaOqzhcKbRMy31ygr_uwT6mMjzsGv5wFF0MrLa1pCI4Ku0P5FfOhGWPTrFW8EK2hEUOc5Z5EJ0rOEiE_QJ81bbYj--408N-qcAJ7X3ekghTcQ25QjLXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا در مورد ایران:
همه می‌خواهند این وضعیت به پایان برسد. ۴۷ سال است که با این رژیم شیطانی زندگی می‌کنیم و مردم جهان از این وضعیت خسته شده‌اند.
مردم ایران، مردمی بزرگ هستند. اما متاسفانه، یک رژیم سرکوبگر بر آن‌ها حاکم است. یا این رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، وگرنه باید ببینیم چه اتفاقی می‌افتد.
ما آن‌ها را از نظر اقتصادی به زانو درخواهیم آورد. آن‌ها در چیزی که من "چنگال مرگ اقتصادی" می‌نامم، گرفتار شده‌اند.
ارز آن‌ها در حال سقوط است و صادرات نفت آن‌ها به صفر رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/145592" target="_blank">📅 18:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145591">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا یک شرکت مستقر در ترکیه را در چارچوب محدودیت‌های مرتبط با ایران تحریم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/145591" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145590">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e30b8bea.mp4?token=Rt6xd1jA3GkyAYlVqBRCm-L-oiieBlkC_mODTc5e9HC3s4jgBnYxzXHn_5hDh473v34DE_MwaI5i_qopIRX3YTPJuUtShxK6JC9tHf7O3EKhFWqQa-p9lMBP4_2T3NvWR6AUe7qRf13KJzCuLcYVm63r94DaP5iGTnnYmQUh7ukjDlfFGr_F6lRZN7dqAz6LiuHBJCWtPsrFORBJtpNegT4o9ub9TQlxG8_-e41GRCTc64CuJ7MjIWl5l7hdpN0pHUulwRUVqdbUdXAyidWlq5so7sJzqah5kZDc21JnmLb6q0fimpyouFffr1zzm1dM7qphG42t0TYTSvKf-Gx5iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e30b8bea.mp4?token=Rt6xd1jA3GkyAYlVqBRCm-L-oiieBlkC_mODTc5e9HC3s4jgBnYxzXHn_5hDh473v34DE_MwaI5i_qopIRX3YTPJuUtShxK6JC9tHf7O3EKhFWqQa-p9lMBP4_2T3NvWR6AUe7qRf13KJzCuLcYVm63r94DaP5iGTnnYmQUh7ukjDlfFGr_F6lRZN7dqAz6LiuHBJCWtPsrFORBJtpNegT4o9ub9TQlxG8_-e41GRCTc64CuJ7MjIWl5l7hdpN0pHUulwRUVqdbUdXAyidWlq5so7sJzqah5kZDc21JnmLb6q0fimpyouFffr1zzm1dM7qphG42t0TYTSvKf-Gx5iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتشر شده در ایتا
‼️
بمباران ناو جرالد فورد توسط جنگنده آذرخش
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/145590" target="_blank">📅 18:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145589">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4589b78c3.mp4?token=F1MjZy-ijjY9LY5LZFlsvH-J8rOMqcdiliqNNJTenP6EAad2HSWXpP1kHTtIN36MzPV3ALOTpRfSBoAdetUcSNGLSxIGibck3s6BqdYjgv9mAeQMHpkUSu3CbcqbDF9hti7ks6VRJJRRHV_hAX0NV-rOz5avPacPLzL7poSmVNZLQtv_91_iCFuy_lf-T6XrDXlreUJjzFL3NOBX7oeuZq1SmPzCCI7g3gOBXPBHRvw3-y9yZoERR9mQcqDfr71iRyjhgIMIqAaJ8xZ4KYwgqZX_DuIgS-h0eLu5_niYRauo69vVSpzNgek5dQFc6R9qFJQ7T1qGQUN5i5Y7LUSCdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4589b78c3.mp4?token=F1MjZy-ijjY9LY5LZFlsvH-J8rOMqcdiliqNNJTenP6EAad2HSWXpP1kHTtIN36MzPV3ALOTpRfSBoAdetUcSNGLSxIGibck3s6BqdYjgv9mAeQMHpkUSu3CbcqbDF9hti7ks6VRJJRRHV_hAX0NV-rOz5avPacPLzL7poSmVNZLQtv_91_iCFuy_lf-T6XrDXlreUJjzFL3NOBX7oeuZq1SmPzCCI7g3gOBXPBHRvw3-y9yZoERR9mQcqDfr71iRyjhgIMIqAaJ8xZ4KYwgqZX_DuIgS-h0eLu5_niYRauo69vVSpzNgek5dQFc6R9qFJQ7T1qGQUN5i5Y7LUSCdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از لحظه اصابت پهپاد روسی به ساختمان مرکزی سرویس امنیتی اوکراین (SBU) در قلب کی‌یف
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/145589" target="_blank">📅 17:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145588">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t-LkaELWTwWbeeXEBRnp8u2OvogEOKV37s-GzuovdqlzSnByGu0cqFVTEP49HpgEFrcj7TYHI2AJWKYlc_vJsQpapFk1iDTjMgFRZvf49kAjAkXB7FhgRQQ1jyB41MxSFPYB6E7Eo_VadzdldNTdztmQ2gKVw8YRdYniFvwQhwX-9lxFv_OTwFXO5SDEtXwNmv7A_ZbZvXU4q7qcDEPVGUc2V-iqhHHR5Yam2GStUkL5GSBvmGMskw3ITtcYgxTHQHAvD5No58uuKFzgT1GbOFHL0s1V85gob9C3h12T28N8JkkNpF0XRPmEkVgp6oT7aQXTxPdu8qhPmUtc5L3HIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با کاهش قیمت طلا، ارزهای دیجیتال هم سقوط کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/145588" target="_blank">📅 17:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145587">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100451e13a.mp4?token=ABfv8l1x5WymMDhrT6mmy9MlGah4quIz_rAEwXQSxhBhtdPfx0fI6oUkMgMXPtT_SHypv-s8WfSO-uQmAnIEjcgdbbcZgUVnOPr6WrI3FT87qIGzxHDEkFNb4cA9X8tn5Y5IFYtVDH5CCih4U4djwL-vScKMN1nc4RieIR-u0QZ2AJpyBJL5ysA0XJ5Z3IV7u3RphXxdhLTRVqevuQL0OYbJMfN8nPcEPJeCr55TVcezodPTd2FuE_d5ESouWTzUI7Inkaeow39mDl_uzoexLCPMfAJ_JGBEzOJjFP8a3ozRpoZTZcOVlbPG65rGlUiIIZ3jfBA5KsCZ57iliW_fRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100451e13a.mp4?token=ABfv8l1x5WymMDhrT6mmy9MlGah4quIz_rAEwXQSxhBhtdPfx0fI6oUkMgMXPtT_SHypv-s8WfSO-uQmAnIEjcgdbbcZgUVnOPr6WrI3FT87qIGzxHDEkFNb4cA9X8tn5Y5IFYtVDH5CCih4U4djwL-vScKMN1nc4RieIR-u0QZ2AJpyBJL5ysA0XJ5Z3IV7u3RphXxdhLTRVqevuQL0OYbJMfN8nPcEPJeCr55TVcezodPTd2FuE_d5ESouWTzUI7Inkaeow39mDl_uzoexLCPMfAJ_JGBEzOJjFP8a3ozRpoZTZcOVlbPG65rGlUiIIZ3jfBA5KsCZ57iliW_fRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بابک زنجانی: سایپا را ۱ میلیارد دلار می‌فروختند، ۲ میلیارد پیشنهاد دادم، نفروختند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/145587" target="_blank">📅 17:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145586">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCk1RGMTdbcIXn_Yvji2IsFfXb1ksyRMV1tBjh1toG1w70pcxkA60B237HEQ7pjwjruf7LIfNwvd4WEJqOShwApIkHNglDru4OqgLc-JrSSddN7ZvITjoWEYhrSa7864ZQEnvPw0MQ94obagPyYVhvM7H03Wog653A7_hxw6dRVwU7eMP22MqvViLglBPxBVWMnHu2OrIzO1Q0aoyhJpv3MUZR0r8HIkB16lDJLBvXPKIppjni8KIFHNm-tUuYvasZm47IUBLVPCdvGsG-CwI7JRmZ8vo08SbtDYlolRjQz519SNLIi889RgJlhplsoMHW9lH6GpGi_lcuvABTGr8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استقرار ۱۲ فروند جنگنده آمریکایی مدل F-16C در پایگاه هوایی "شاهزاده سلطان" در عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/145586" target="_blank">📅 17:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145585">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سی‌بی‌اس:  بر اساس گزارش سی‌بی‌اس، پنتاگون از نظامیان آمریکایی خواسته است هنگام صحبت درباره جنگ با ایران، از عنوان «عملیات خشم حماسی» استفاده نکنند و تأکید کرده که این عملیات رسماً در ۵ مه به پایان رسیده است.
🔴
نکته قابل توجه آن است که پنتاگون بر پایان این عملیات تأکید دارد، در حالی که پیامدهای درگیری با ایران همچنان ادامه دارد؛ موضوعی که این پرسش را مطرح می‌کند که واشنگتن دقیقاً چه اقداماتی را بخشی از جنگ می‌داند و چه اقداماتی را تحت عناوین دیگری تعریف می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/145585" target="_blank">📅 17:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145584">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2SlCDiaV2CiQJeT-30zSUV4-s1O0OjEm6jY42quq1Z-TxiL_LPKB5PGUiIi6O6MW1NePUhsmWjdc_rKXBZXqHR00Uj_3yryJkbURDg9MrF1JLpaww-veC4IfHUUjGgpf4iymS6pzwz7FXrnul9KNLOrh6Ys1-fmPpApEDpoYN-bup1NvGGOxt9u2IX7raJ5hXLQCwf6_qRvumKrWnmCY3aAnzw06WV2XNFlJBxG_ZLGAQBaM_2L5cZSw7Al_Tzg9yll-TfwYHOhgGA_paKGrLhWiE3JReoFJ5_XxH7-PWVQNLj2eqNeNKiGpmtI91WdISaLR98lD9m_DaUz82ViQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت سکه نسبت به ۱۰ سال قبل حدود ۲۰۰ برابر افزایش داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/145584" target="_blank">📅 17:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145583">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b6764494.mp4?token=kOsLa0ENBRG03i-xwHt30c4E7NeLh-VIJdDjthp86o_un2xqCZ8QS5e50LNWj1KQ3LMJPt3j6KufvkN39PHhMF1RBSXPDNOR_4gpxHioGGhft1U-gN1mDn1WLGRhITUBkdlbd8dwqO50bC54r8xJJuckVdRj55mzq1WpGBdtNqvJrXpbuinHRWuT-uCgRmGk-Eo4tIFd_JNQdrENWDgRKLhpBVxiEbGY9ZuKMH54MfHTV_pxC8NKxSOCuV3HSo38xp5ZMcmEAzEeSwRkgHQ_gTe-ferBROAfHGnSYaja3U78rlz3R_qQxPFEt0bKqUCnOnPbQATVAjX5V2jWj8xRKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b6764494.mp4?token=kOsLa0ENBRG03i-xwHt30c4E7NeLh-VIJdDjthp86o_un2xqCZ8QS5e50LNWj1KQ3LMJPt3j6KufvkN39PHhMF1RBSXPDNOR_4gpxHioGGhft1U-gN1mDn1WLGRhITUBkdlbd8dwqO50bC54r8xJJuckVdRj55mzq1WpGBdtNqvJrXpbuinHRWuT-uCgRmGk-Eo4tIFd_JNQdrENWDgRKLhpBVxiEbGY9ZuKMH54MfHTV_pxC8NKxSOCuV3HSo38xp5ZMcmEAzEeSwRkgHQ_gTe-ferBROAfHGnSYaja3U78rlz3R_qQxPFEt0bKqUCnOnPbQATVAjX5V2jWj8xRKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله توپخانه‌ای اسرائیل  به شهرک «بنی حیان» در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/145583" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145582">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی:
سفیران ویژه آمریکا، ویتکو و کوشنر، به مسکو و کی‌یف سفر می‌کنند تا در مورد پایان جنگ مذاکره کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/145582" target="_blank">📅 16:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145580">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fftpOsTXGHGeZUrlW_darR8gLswpiIp5WFXLmHvK-bW6gASxe35EEAEg4HXyo4RgL-uz2x0Cvbk2UtEZ-Jh08giwd847t7JgDF5fUnAN7BTqJwCP2mMNuMkgtrcJJlnEIRTdll0Pl8zFKYH5CSYcYXgWZ2LUVj7i0BOc50w7G3GAerfBpeOGcd_Rs-Szd4nIxh9BZD6qGnwx4kAWpD9fSeH-Zl1mrlt-wADOUmUQTxNp8tF48EQB_inWsvQifvsoCXYelW6bYabKzXQw911By9dC9D4_nV32m0bMWfp5VflOSA3OvCDMEfr2T4osWkSd8Y3jhdb4AYRLRFSXsuBNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل فرمانده حمله به سوفا رو ترور کرد
🔴
ارتش اسرائیل یه فرمانده رو زد که حمله به پایگاه سوفا رو هفتم اکتبر رهبری کرده بود. این فرد تو نگهداری گروگان‌های حماس هم دست داشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/145580" target="_blank">📅 16:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145579">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
انجمن اتومبیل آمریکا اعلام کرد: قیمت هر گالن گازوئیل به ۵.۸۵ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/145579" target="_blank">📅 16:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145578">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سپاه هفته قبل: اگه اسرائیل به تپه‌های علی الطاهر حمله کنه با خشم ما روبرو میشه
🔴
اسرائیل دیشب اونجا رو فتح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/145578" target="_blank">📅 16:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145577">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
قیمت جهانی انس طلا ناگهان ۱۰۰ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/145577" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145576">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7wPttF1EX4RMVIKljtaQleIMmoOI0ArGuoAuTQ370jExYcy9UwFLjgdv6yqLLszXevJ9c-3M5fOaQoswRMjlFhsGNmMs5t38QvEyJpQmEicreHnjTQmXhCZkGZljMcH_cWKFtXYAm3fjNqnjQJorqFnBi4-W-imdvGgBULnNTXCuLwUjknK0xnJDaDVWv5SncNhmHYJwIba3Hx8XoCUx3YhbXyK7QpRx6IG-FUq8WlbIoa5mp8_hS90MsX2XjfGI0cas0vfNf_64BNX2kWv__Qb8y6B-kzc-l2_lhFHDiqUDZWFO9o9mS0CGU_T-bQuK2NOMHZZ5nVNSAbVFtpEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی انس طلا ناگهان ۱۰۰ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/145576" target="_blank">📅 16:06 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
