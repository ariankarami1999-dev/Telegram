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
<img src="https://cdn4.telesco.pe/file/dTp_E5xS6yeMdCDKfFp5GGPnYs1mEnG8im2zqrLFZAxk46bCS8oneCM-V692Wh3bcbgg5V-cE5-JwVEda-X8FacDKouMb9_4awenYTl3wgLgqJeFH2QKICbJTBhCSwRddK5qEZhiN_uuIFFN7eOmEzkSqfrJwaa6RvC8AoOZpSSXyE6xOfzg5rlQGs5TXUmWZpScjjA92eeWZttB-N-lt-3aPhhyImwV3O1snwp4i0aD5XeyfxM_tmIeNZzWSwFrvmdCrdEoow2WsdfGY15glf0omfrkeUMfmezQ547TfzWjPAIOvE_zmbIP9P84eJn00R3OC77S-90OxKJsooOTug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 13:40:22</div>
<hr>

<div class="tg-post" id="msg-140448">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد حسین کنعانی به علت مصدومیت دو دیدار بعدی پرسپولیس برابر صنعت نفت و خیبر را از دست خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SorkhTimes/140448" target="_blank">📅 12:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140447">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
🇮🇷
بهت و تعجب ملی‌پوشان امید بعد از حذف از بازی‌های آسیایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SorkhTimes/140447" target="_blank">📅 12:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140446">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c126edce8.mp4?token=NEqOicUyWTMkH8OoFhVHvH2KHffjOQ9hOtEnTyouBfz-6Sb2wa2Hzb02VPTfqwtjKH8TKhHVLCswXnn-JRN7SHty_ZTeJiseynGu9OpY5epJU-Pe59VCmom-YL1h0Y8RVVQSYxNsmIVQwqcNhha4ZHD_p_fSwZeIPFiiEMK9JjDKB-qZOY7w-yAwgWjr388lsDnlLgZIRR4zbaPx5ZJF9__jHUr37Xv0kRH4fE7j8vVLdblj8dfqDtt5h2YggugGBkR-uIR1DDii3MvnRkDrq18AmqKPEqJMz09NSJ9L0L_UZenVLqqrV-59_5UmRdCkDSRItrt6jBMK5IPnDf1WgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c126edce8.mp4?token=NEqOicUyWTMkH8OoFhVHvH2KHffjOQ9hOtEnTyouBfz-6Sb2wa2Hzb02VPTfqwtjKH8TKhHVLCswXnn-JRN7SHty_ZTeJiseynGu9OpY5epJU-Pe59VCmom-YL1h0Y8RVVQSYxNsmIVQwqcNhha4ZHD_p_fSwZeIPFiiEMK9JjDKB-qZOY7w-yAwgWjr388lsDnlLgZIRR4zbaPx5ZJF9__jHUr37Xv0kRH4fE7j8vVLdblj8dfqDtt5h2YggugGBkR-uIR1DDii3MvnRkDrq18AmqKPEqJMz09NSJ9L0L_UZenVLqqrV-59_5UmRdCkDSRItrt6jBMK5IPnDf1WgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بهت و تعجب ملی‌پوشان امید بعد از حذف از بازی‌های آسیایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/140446" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140445">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6yCHJ1dq3YNzEdUhkknwnQeBI1BEht8wiSQorlC0Ei0QHL-PprHPRCL4ZKskBhRojFcZlEBw1zJDPimd9p3KWCasX3vnb1VJ4Cl8mWGLpFtkBynIOD-bRGbXFQBJq5hMlOSbrDUcG_giVheUaXr6h6ycEajiZK4jxEy8_EixkTZQJe-pWXS-JyICT5hC3Gg-vqG_nWNwd1E1TX9wmiEUmRQL9Pnp8VM8J3KSb7QsbqRMdPV2UMi3da9za8xQzJ1oYiPg56-JMzgJRtcDwj0bTxXXhx1QRKOlM-OYmzuQiSI70SVROeAVpWtHvaF8ZrE0avh9WxyAVPkD82UbpCdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تیم ملی امید‌ با این کادر با دانش به کره شمالی باخت و حذف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/140445" target="_blank">📅 11:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140444">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
آقای حسین عبدی ..بهترین تیم امید و ریدی توش و تیم و حذف کردی و از کره شمالی چهار گل خوردی ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/140444" target="_blank">📅 11:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140443">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
گل چهارم و ببین ...از وسط زمین طرف تک به تک شد ...این چه تیم امیدیه ..آقای عبدی چه گوهی خوردی با این همه جووون با استعداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/140443" target="_blank">📅 10:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140442">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29d58e82a.mp4?token=LLLIBZ1-YlppqxarX9pIvXw2oFqSNCB-WMkVpIokU-V84xQSer_FlxGmtgULdgDyQJzjJJ44DLBZBlDH5S-3bUov7Kh5S9nE3ot-P7H6YbkeQvS9H92XvtPYe0uByx9uThxsBR4lHDd9iQG1Ro12_e6O6fuF3A1YtvyrXAc-RoR2BYSp9OnQxYAMx1V2-w0uBDD7w25irtYDRpRrBiLN5XriqFJ-K9Xun1XGdooi9EJjvgBYNnRN2S6P9rW68NxepLlS29EuPn6-J1awvKDwR4To3FGJEv7sFQZc_vWLwx2epKXSxEdyTiwFemvKuroAcrVxABip6RURpLvren5YdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29d58e82a.mp4?token=LLLIBZ1-YlppqxarX9pIvXw2oFqSNCB-WMkVpIokU-V84xQSer_FlxGmtgULdgDyQJzjJJ44DLBZBlDH5S-3bUov7Kh5S9nE3ot-P7H6YbkeQvS9H92XvtPYe0uByx9uThxsBR4lHDd9iQG1Ro12_e6O6fuF3A1YtvyrXAc-RoR2BYSp9OnQxYAMx1V2-w0uBDD7w25irtYDRpRrBiLN5XriqFJ-K9Xun1XGdooi9EJjvgBYNnRN2S6P9rW68NxepLlS29EuPn6-J1awvKDwR4To3FGJEv7sFQZc_vWLwx2epKXSxEdyTiwFemvKuroAcrVxABip6RURpLvren5YdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل چهارم و ببین ...از وسط زمین طرف تک به تک شد ...این چه تیم امیدیه ..آقای عبدی چه گوهی خوردی با این همه جووون با استعداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/140442" target="_blank">📅 10:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140441">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
آقای حسین عبدی ..بهترین تیم امید و ریدی توش و تیم و حذف کردی و از کره شمالی چهار گل خوردی ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/140441" target="_blank">📅 10:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140440">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
تیم ملی امید راهی ناگویا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/140440" target="_blank">📅 10:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140439">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
چند روز پیش یکی از نزدیکان میلاد محمدی به ما گفت؛ این بازیکن بخاطر شرایط خانوادگی قصد بازگشت به ایران رو نداره///طاهرخانی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/140439" target="_blank">📅 08:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140438">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo3pb3M6RFPzGjCSZq_Sj0dMOVTdBQuBZWKh3xQZPAN96jl0HrDydOmLHrQlMLQVKBcDb-4asj7OEdnnMlKbT5r3nY-IQ1fxgiVG3ZrlYY3XW3DnS2bVBhtkkQqjOMdqz8m9tM969yhcea0d-BXOvbGdO4ra1eGAPIRdOBWpNHBzM4q4GWqjisnZEOtYyRnLiTh_zXEV_-1Z9TxWqbIiUe6B8-GvxKkZAtxVOM-iKV78rMjimX3HdZHYJojis5uIMIJWDaJnFBOFt-PF1nGqT6ioKaJGvjddL7eLOWb6RqLPsPOsn6M5HYq2dLqQOznMIlbG4RwGwF3yh8IGOginMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🤩
خبرورزشی:
🔴
🔵
🇮🇷
پرسپولیس و استقلال در نیم‌فصل برای جذب محمد قربانی اقدام خواهند کرد
.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140438" target="_blank">📅 08:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140437">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
✔️
✔️
علی علیپور به دلیل مصدومیت زانو حدود سه هفته باید مراحل فیزیوتراپی و آماده‌سازی را پشت سر بگذارد و در لیست تیم ملی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/140437" target="_blank">📅 08:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140436">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
ترکیب تیم امید ایران مقابل چین
✅
✅
محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/140436" target="_blank">📅 08:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140435">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
🇮🇷
🇮🇷
صبح اولین روز پاییزتون بخیر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/140435" target="_blank">📅 08:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140434">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqluuf_KLic87sjUhslEiEqljbBbXPUmkMBvo3-FDTGxuTWbXm0mvvPWyOYHxz-rV7PWp8k4IRPVQOG5YtYxRIkzcVsQ1JMp7Gf8QclslIHSwJuDk-O12YgmdkJGo05YNeYmk_4X439zcxHBcLP1oIf0tZfry-GZW6tUmgUFaV12mM8Vn8P_tHH5jhfltE1rkV9w-U15s0mS1rz8QePuR2qO0usMytoLM6MMwHVr1fYcT4wV_LgtIT_51rBKNHWTytqagQ5fGeCpKfw1QvVlLeDvpLzRq_OU-G-_Sqjg1w-QndTAtdIPyCA88eeh-tSLPmVtrQCpMPfTXcRWsWNXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
IRAN -
🇰🇵
North Korea
⏰
Today 09:00
🏟
Wave Kariya Stadium
⚽️
تیم امید ایران در برابر تیم امید کره‌شمالی در بازی‌های آسیایی؛ جایی که جزئیات می‌تونه سرنوشت بازی رو عوض کنه. ایران با تکیه بر مالکیت و بازی ترکیبی، دنبال کنترل ریتم و ساخت موقعیت خواهد بود. کره‌شمالی هم با انتقال‌های سریع و بازی مستقیم می‌تونه دردسرساز بشه؛ انتظار بازی نزدیک و کم‌ اشتباه میره.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/140434" target="_blank">📅 06:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140433">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
فوووری / میگن کنعانی مصدوم بوده و رفت شمال و از زانوش تو تعطیلات زیادی کار کشیده و پاشو بگا داده و چند هفته ای نیست ///فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140433" target="_blank">📅 00:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140432">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140432" target="_blank">📅 00:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140431">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd12c24d1.mp4?token=C8IOxjiMZhaVlEzWoMhJlgAm8DJLZmWnvBfUPbzAVB6IVccMIqqVePTHZZYPFEXeHOv9xgol3r4w82PjmY6yuo_OffZCoa9NcT8mS4PpmC16BeYF29sWOXzPTr0QZnGvzelcmw1chdzkb_M08Ekh9evOnviLxextD0jzpsE-yG-ejMQthkBRwu9HCb5hxVNlrurw3R5DRzIIDqxomcas0AVXCKM-rCDqPqbc0DwKDrcV3oNrGT9bAmV_Efeio8-tcd_-bIIJWuLu3_NkJuoXE4Z2ojF-RFZM_ug5bXvUKSnZ0_PzQA8hFr07x7Hit4l1nG5O0-U51gmsCS4-BmwA6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd12c24d1.mp4?token=C8IOxjiMZhaVlEzWoMhJlgAm8DJLZmWnvBfUPbzAVB6IVccMIqqVePTHZZYPFEXeHOv9xgol3r4w82PjmY6yuo_OffZCoa9NcT8mS4PpmC16BeYF29sWOXzPTr0QZnGvzelcmw1chdzkb_M08Ekh9evOnviLxextD0jzpsE-yG-ejMQthkBRwu9HCb5hxVNlrurw3R5DRzIIDqxomcas0AVXCKM-rCDqPqbc0DwKDrcV3oNrGT9bAmV_Efeio8-tcd_-bIIJWuLu3_NkJuoXE4Z2ojF-RFZM_ug5bXvUKSnZ0_PzQA8hFr07x7Hit4l1nG5O0-U51gmsCS4-BmwA6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
زهرا خواجوی: گذشته ام را نمی توانم انکار کنم ولی امروز پرسپولیسی هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140431" target="_blank">📅 00:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140430">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
بازگشا، سخنگوی باشگاه پرسپولیس:
✔️
از فدراسیون خواستیم رسیدگی به پرونده آسانی با حضور وکلای ما و آنلاین باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140430" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140429">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
❌
امیدواری پرسپولیس به محکومیت آسانی
❌
❌
از باشگاه پرسپولیس خبر می‌رسد مسئولان این باشگاه در مرحله استیناف مدارک جدیدی را نیز ارائه کرده‌اند و امیدوارند با بررسی این مستندات، رأی مرحله نخست تغییر کند.
❌
❌
پیگیری‌ها نشان می‌دهد مسئولان پرسپولیس موضوع این پرونده…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140429" target="_blank">📅 23:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140428">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
تیوی بیفوما:
✅
• سرعتم روی گل به ملوان ۳۷ کیلومتر بود/ سال گذشته اتحاد تیمی نبود و شرایط خوبی نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140428" target="_blank">📅 23:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140427">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
بیفوما:
🔻
از لقب میگ‌میگ خوشم می‌آید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140427" target="_blank">📅 22:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140426">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
تیوی بیفوما: مدیرعامل در اردوی ترکیه از من پرسید چه چیزی باعث اذیت شدنت می‌شود؟/ تارتار به من گفت به تو اعتقاد دارم و شرایط نسبت به سال گذشته، تغییر خواهد کرد. هدفم قهرمانی با پرسپولیس است و نشان دادیم می‌توانیم قهرمان شویم. شرایط امسال خیلی بهتر است
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140426" target="_blank">📅 22:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140425">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
تیوی بیفوما : بهترین دوست من در پرسپولیس حسین کنعانی است / شاید انگلیسی خیلی خوب حرف نزنه ولی خیلی خوب با هم ارتباط میگیریم / یکی از دلایلی که کاپیتان شده به نظرم اینه که خیلی خوب با خارجی ها ارتباط میگیره و شرایطو براشون راحت تر میگیره و این خیلی برای…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140425" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140424">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
⭕️
#فوری | ترامپ:
🔻
مقامات آمریکایی به مدت سه ساعت با یک هیئت ایرانی دیدار کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140424" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140423">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
❌
تیوی بیفوما: در خونه بودم که به من گفتن که تیمی بزرگ از آسیا تورو میخواد که تو لیگ نخبگانه و با النصر میخواد بازی کنه و به عشق کریستیانو رونالدو به ایران اومدم تا مقابلش بازی کنم اما یهویی دیدم استقلالی که من رفتم توش استقلال خوزستانه نه تهران
😂
😂
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140423" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140422">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
ترامپ: فکر می‌کنم درست بعد از انتخابات میان‌دوره‌ای با ایران به توافق خواهیم رسید
🔄
🔄
آنها منتظرند ببینند من در انتخابات میان‌دوره‌ای چگونه عمل می‌کنم. چیزی که آنها متوجه نمی‌شوند این است که من نامزد انتخابات نیستم. من قبلاً این کار را انجام داده‌ام و با…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140422" target="_blank">📅 21:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140421">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
تیوی بیفوما : از چیزی که کادرفنی از من می‌خواهد، خوشحالم/ وقتی همه چیز با کادرفنی خوب است، من هم بهترین خودم را به نمایش می‌گذارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140421" target="_blank">📅 21:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140420">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
تیوی بیفوما : سال قبل با انگیزه فراوانی به پرسپولیس آمدم/ پیش‌فصل آسانی در ترکیه نداشتیم/ شرایطی تجربه کردم که امیدوارم هیچکسی آن را تجربه نکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140420" target="_blank">📅 21:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140419">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
✔️
✔️
❌
امشب ساعت ۲۱:۰۰ در تلویزیون پرسپولیس؛ تیوی بیفوما و زهرا خواجوی دروازه‌بان تیم بانوان پرسپولیس مهمان برنامه هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140419" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140418">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
✔️
✅
تصمیم پرسپولیس درباره اورونوف
✔️
✔️
پرسپولیس فعلاً هیچ برنامه‌ای برای جدایی اورونوف نداره و این بازیکن همچنان در برنامه‌های باشگاه و کادرفنی قرار داره.
✔️
✔️
شایعه انتقالش به تراکتور به‌خاطر نیمکت‌نشینی تأیید نشده و حتی اگر در آینده بحث فروشش مطرح بشه،…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140418" target="_blank">📅 21:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140417">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
✔️
سربازی فرهان جعفری در نیم‌فصل به پایان می‌رسه و راهی پرسپولیس میشه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140417" target="_blank">📅 21:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140416">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2fqsBriHv7CtQzR5yp3nCeeQslF9bXGARHCfWm5QhRBrgpW4f3XEVEF0zGzZEYuvhY2qYk_84o_g5lNhrHTipHi6milylITsqqSdLPOl0MugB-49R8XwzdxwHm2uwneo8S1rkSq-CzYIsLsUpZiAUiocDNzymcUyNgWSe7gtvCMQT3Bmgfo8kvohaTqa2d0E31EVAlrOtoYekA0Uv7iWF7diR7ggZ-s0aFmvnjZYkUAbdKgxKjaZYmfQT29eZoZdyWBv7mpgBAjYCld3wGdBXl2M6HaO788PCVK3AEfyOtRCc8TPOzKdVJi0Dx6eEw0JLZXlQLxe77zwkv38pKYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
سرگیف و بیفوما هردو در تمرینات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140416" target="_blank">📅 21:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140415">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140415" target="_blank">📅 21:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140414">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
ایرنا: حسین کنعانی عکس جدیدی از مصدومیتش رو نشون داده و واقعاً مصدومه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140414" target="_blank">📅 21:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140413">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e46ZIMPuMu9eAqLYVcFtMNBMZGfZ3CyhLvO00VcPC3Ezkxg2DdiRi7fiRjHQSxp_6fReKlyLSlBkX2jFapwtYcI6fXcXqtEBEXzO1_XfHFNL84InMXfzWyc-OFZ5fa_XtPcTn5ZC14PPOikiXglzpl5ZXrFthN7qAs74K0GpIE7PsK3lPtO0Do-y8Eo_xChtvMfZ0dUouM4FuP68U9bWfxayVf8v6nd2m9A2f4N8Cd_3lQwRbdSUNPN7LFasPTDfeMk7WbSdhLS289M6HYeeEinpWQPv5pvO4ARQKBIoWUuHtCqvGKBkX2Gdtqi-ZegAkRjEe1ylhOisZT0Lh7J2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام ملت‌های والیبال اروپا
🇵🇱
Poland -
🇩🇪
Germany
⏰
Tonight 19:30
🏐
لهستان با نمایش مقتدرانه مقابل لتونی و برتری ۳–۰ وارد یک‌چهارم شد؛ آلمان اما بعد از کامبک سنگین مقابل بلغارستان و برد ۳–۲ از نظر فشار و فرسودگی شرایط متفاوتی دارد. لهستان در سرویس، دفاع روی تور و کیفیت حمله دست بالاتر را دارد و اگر دریافت آلمان تحت فشار قرار بگیرد، کنترل ست‌ها سریع از دستشان خارج می‌شود. آلمان با روحیه‌ی کامبک اخیر خطرناک است و اگر سرویس‌هایش مؤثر باشد می‌تواند حداقل یک ست را از لهستان بگیرد. با این حال، بازی از نظر تاکتیکی بیشتر به سمت برتری لهستان و تعداد ست‌های بالا می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدار هیجان‌انگیز امشب رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140413" target="_blank">📅 20:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140412">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ترامپ: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند؛ آنها یک اشتباه بزرگ کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140412" target="_blank">📅 19:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140410">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
#فوری | ترامپ در سازمان ملل:
🔻
با تصمیمی بزرگ در مورد ایران روبه‌رو هستم؛ توافق یا نابودی کامل
‼️
🔻
آیا به توافقی دست یابیم که به این کشور اجازه دهد به ملتی بسیار بزرگ‌تر تبدیل شود، یا اینکه آن را به‌طور کامل نابود کنم
⁉️
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140410" target="_blank">📅 18:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140409">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
سی‌ان‌ان: دونالد ترامپ به مشاوران خود گفته است که اگر شرایط مناسب باشد مایل است با مقامات ایرانی که در مجمع عمومی سازمان ملل متحد در نیویورک حضور دارند، دیدار کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140409" target="_blank">📅 18:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140408">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🚨
🚨
⚽
محمد قربانی: بنظرم در الوحده ماندنی هستم باشگاه رضایتنامه مرا صادر نمی کنه
🆕
👀
چند بازیکن جدید قراره اضافه بشه اما من در لیست فروش نیستم چون الوحده هافبک ندارد  ‌
📎
اینجاست که مشخص میشه چه کسی دنبال فالور گرفتنه و چه کسی…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140408" target="_blank">📅 17:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140407">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: حسین کنعانی زادگان به تیم ملی دعوت نشده است که هیچ ربطی به مصدومیتش ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140407" target="_blank">📅 17:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140406">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d84777f345.mp4?token=ujGeEeLoNTttbmaiqAZnStmgco0h0AalSmzf9Y7oU3AgW-Xs4erlkHLZzUNx5SGL79M0-GiseTqGuEfWejzMgIMPgs3d0K2_qqdYuM6Xyq-cubrypHxuW9dG_puofo50XDqxKxvIxtyztrmeHPXZlFkppBNMBRHABHARFZAWMvxx61ketdrVNjP7MCDl5wfzSJ_c7geSVjr-mQngWh9qAmFUI-L_LzEvpIpN69056PNZyAony9AYBCUDzZCVVvYCzblEqB7i5caSI3X2Go0VNKM31Oe28Uz-HpU08890P-Z7TMIT2UkVQxjQ1jYLVHKoSSiWuN3ntg87MfOosvgC4LAKM-s2FWoajD5VQzD3ofMBbz1Xvdc-wzJ6AJOUq3yDlugsPtz3ZYfykb-_qrLwXQsWwcTB0j-_d--1D73q06XEDQL33MfWNIn1bqQmyMiUg5f3aG8peWxVToTUvqlOlRKwULZgOqixzXNNi7PlYivJsthdhQD_RXYR6AolfxnbYW9-8AOWPdvhW7oJlnpeJ_AozSJoJj6KpzVH8XVTa8GXLjZ_TMo4f3RCqGhPGZZU-3yPVcYQpaCNZfS5UdbI-a_HzaOBOLR-vSqsxNAW9S8k27SJzTxP41SAC42fBf3S-7ghLBoiwhYtl3J7BxxIGRg-zDTpFucfgdA1tjmXxIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d84777f345.mp4?token=ujGeEeLoNTttbmaiqAZnStmgco0h0AalSmzf9Y7oU3AgW-Xs4erlkHLZzUNx5SGL79M0-GiseTqGuEfWejzMgIMPgs3d0K2_qqdYuM6Xyq-cubrypHxuW9dG_puofo50XDqxKxvIxtyztrmeHPXZlFkppBNMBRHABHARFZAWMvxx61ketdrVNjP7MCDl5wfzSJ_c7geSVjr-mQngWh9qAmFUI-L_LzEvpIpN69056PNZyAony9AYBCUDzZCVVvYCzblEqB7i5caSI3X2Go0VNKM31Oe28Uz-HpU08890P-Z7TMIT2UkVQxjQ1jYLVHKoSSiWuN3ntg87MfOosvgC4LAKM-s2FWoajD5VQzD3ofMBbz1Xvdc-wzJ6AJOUq3yDlugsPtz3ZYfykb-_qrLwXQsWwcTB0j-_d--1D73q06XEDQL33MfWNIn1bqQmyMiUg5f3aG8peWxVToTUvqlOlRKwULZgOqixzXNNi7PlYivJsthdhQD_RXYR6AolfxnbYW9-8AOWPdvhW7oJlnpeJ_AozSJoJj6KpzVH8XVTa8GXLjZ_TMo4f3RCqGhPGZZU-3yPVcYQpaCNZfS5UdbI-a_HzaOBOLR-vSqsxNAW9S8k27SJzTxP41SAC42fBf3S-7ghLBoiwhYtl3J7BxxIGRg-zDTpFucfgdA1tjmXxIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
7 سال از گل مهدی عبدی گذشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140406" target="_blank">📅 17:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140405">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💢
مهدی کروبی خطاب به پزشکیان: اگر شرایط فراهم شد، با ترامپ دیدار کن و برای صلح پایدار وارد گفت‌وگو شو.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140405" target="_blank">📅 16:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140404">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
ادعای عضو کارگروه حقوقی تیم وکلا امید عالیشاه: خداداد عزیزی با شکایت امید عالیشاه می‌تواند راهی زندان می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140404" target="_blank">📅 16:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140403">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
فرهیختگان:
🔄
⌛
بشار و فرهان گزینه‌های روی میز تارتار در زمستان؛ پرسپولیس به‌دنبال پلی‌میکر
😀
درصورت تایید مهدی تارتار مذاکرات با بشار رسن آغاز خواهد شد و فرهان جعفری نیز گزینه‌ی دیگر سرخ‌هاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140403" target="_blank">📅 16:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140402">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این دیوس یه کانال داره به نام پرشانا ساکر که اونجا بازیکنی رو که میخواد بولد کنه جوری ازش تبلیغ میکنه که کلی حق دلالی بخوره.اکثر خارجی های کیسه رو هم این اورده سر همین ضدپرسپولیس و بنفع استقلال مطلب کارمیکنه کانالش</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140402" target="_blank">📅 16:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140401">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm.m</strong></div>
<div class="tg-text">این دیوس یه کانال داره به نام پرشانا ساکر که اونجا بازیکنی رو که میخواد بولد کنه جوری ازش تبلیغ میکنه که کلی حق دلالی بخوره.اکثر خارجی های کیسه رو هم این اورده سر همین ضدپرسپولیس و بنفع استقلال مطلب کارمیکنه کانالش</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140401" target="_blank">📅 16:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140400">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140400" target="_blank">📅 16:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140399">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140399" target="_blank">📅 16:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140398">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKZBv4IHuhdaqkyChdW94EAJESkOsDaWIvQ0NfMhpeDCXyDHxW6JAOwYRqjED9GbUMe-vrK9R-4LZPKIUYdAUvBSz43EaKVbfdGrtnl02Cei1oWRl3A9koKc6OHEm1vL2qdti6-rlrBhY9ZgrFvmtwf1q1jcoxQU0Useew3F3oV3dcTC7xS8qjLc5rPMS1MOlm1G9Q_RB0FvnU80dnZ_GqdfIfXbpWV2FdH3VD7JXV8nWf2uiOabUfck3-GlvAYJG76MxYivMky1e9yBRI-MYYCiw883EzyaH8x23JXhk1yMsrnjufr0R55FZ1OtaCZQkx0PkVU2DSwh343vxfthHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140398" target="_blank">📅 16:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140397">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎙
🔥
تیکه
سنگین‌ ابوطالب به خداداد عزیزی در قسمت اول برنامه جدیدش: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/140397" target="_blank">📅 16:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140396">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4e645be8.mp4?token=oinRbbCWOQwoZ_dkLOpjPK0XSjw_cJMsH2PTSXGChsDqWrtNO8SW2_xURyLA3B75U138CVkPcxW6DL4jsJWjuTTk0OeIIJE7rA1uHiKEstycqaUHCexO_C0Vvf7WkwnBwpINWkYysY8taU6KrhPB5a_bTlzIhdBlzzfiUa-Q81HEtL4UDk03J8HPr_SVApGtteMmt4xdVnHMedmNCw2TdU5z6IteUTrSgCkbpSPyr9LEos5V0onYJ9htxWQbkDc72zf0DUXvz4HdYVE7J2tvjow94UzG7mxfCdHcBMX6uv8NIdVkYXxbZI7bmF-tyG4ZhOl6DDenSAqoMe6e2ci5tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4e645be8.mp4?token=oinRbbCWOQwoZ_dkLOpjPK0XSjw_cJMsH2PTSXGChsDqWrtNO8SW2_xURyLA3B75U138CVkPcxW6DL4jsJWjuTTk0OeIIJE7rA1uHiKEstycqaUHCexO_C0Vvf7WkwnBwpINWkYysY8taU6KrhPB5a_bTlzIhdBlzzfiUa-Q81HEtL4UDk03J8HPr_SVApGtteMmt4xdVnHMedmNCw2TdU5z6IteUTrSgCkbpSPyr9LEos5V0onYJ9htxWQbkDc72zf0DUXvz4HdYVE7J2tvjow94UzG7mxfCdHcBMX6uv8NIdVkYXxbZI7bmF-tyG4ZhOl6DDenSAqoMe6e2ci5tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
❌
جواد خیابانی: فصل گذشته باید از تاریخچه حذف شود و هیچکس نباید قهرمان اعلام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/140396" target="_blank">📅 16:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140395">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twStCw-g6LniHE1x4X6tOXk4RBoOYzr5ljg6an98_Bz08tB58Bc6u6HEe67fpr1wiGCG1uJvAW0eEglxi6pp-5bpTke57zx5WXlzDM4LRfCV5q8fKqY927BUwwlR2pz5IuNd2nNW9bkchyFuBOelGlCpY_YppLkGdfjIQnWd0HIGga9f952zczy1Zgy_BQdBRYlBsZVVaC1PhmAyFbmySJBAhcYj-bTLA7AXbT_QzBr5Yn4gFptzFYIWvnc4iU_8x3lpcYfsXvEJKZlPBoB_a00DyWHYpWYcZKvvFl49D2DmxjjIxJdjGj3azSg-IEWe_MPhIuhlstsHDkkk_RC9Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
مهدی کروبی خطاب به پزشکیان: اگر شرایط فراهم شد، با ترامپ دیدار کن و برای صلح پایدار وارد گفت‌وگو شو.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140395" target="_blank">📅 15:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140394">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qIeohKRVu9-6f47p7EaVlyd_1Y9MLPQD-CevfwlEVEXS_WSbMXG_SYBOAazVLi8uzx-QQizSgGOCiHQ_jKxEjEU8Zj8O8JGxOCtmIBgh62QcDQTvUawXoAG84rxprCDqZhZlOmQ22XMKrzvgwDIWujdbEyR1uIbDiOIiXuSiAEbqja0SZ8of2Pyqi3qgkyedNwEABaE5AlfHD3MidX71CpEyJXIBVLIThTjfVGiEXJmZVkMAy3SjXjc25gQ9EmWoKvCiQ47WHyqz9eyubWmMKwxC0XnVpbfhuCevOHzUz2nSQIkcgoLom9Xu__1go4NU94ia98lFodlJ6L6xQe7VIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری تسنیم وابسته به سپاه نوشته
:
🔄
دلیل عدم دعوت الهیار صیادمتش به تیم ملی این خالکوبی و حمایتش از اعتراضات ۱۸ و ۱۹ دی بوده !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140394" target="_blank">📅 15:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140393">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
خبرنگار دولت: ادعای ترامپ برای دیدار با پزشکیان آرزوی محال است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140393" target="_blank">📅 15:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140392">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
✔️
داوود رفعتی: بنظرم داور دربی کوپال‌ناظمی بود اما چون تلویزیون رسمی پرسپولیس یک شب قبل از اعلام این داور رو معرفی کرد،‌ فدراسیون تصمیم به تغییر گرفت!
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140392" target="_blank">📅 15:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140391">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYglom7-Q6mFj0yP04YxbFBdvY1xwxOZkkrP3qIybbvgUWAMDxu_2CnJhLgiKX48Kjrfps-cL1VCuL3sR-2f_zDsxRTbtXFMbNqeqZwwLh8kBSmIfwl8KWM7cvSMwXtPtuzdnq5ampT7QLcLHz6twNqARar2Cw4uM2plsMkoQBt1460Ovf3_myjnF7mZpqv8bPCq6v1u3cBo1cP7z73gSjnyze1pIZUljwxOAV_symV23sTzlWyBvxdhFsG09p-kcNkxZq0212TdHbGghGlrHnhs01sd6cUbW2TlrC_tTFeBLmxP0HqESxcoE8v-V9FplQLLoplbgE9oznMgvZFhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آلمان و لهستان امشب در یک‌چهارم نهایی یورووالی ۲۰۲۶ به مصاف هم می‌روند.
🏐
لهستان با قدرت سرویس و تنوع حمله، دست بالاتر را در این نبرد دارد. آلمان اما تیمی جنگنده است و در امتیازات حساس به‌راحتی از جریان بازی خارج نمی‌شود. اگر دریافت آلمان زیر فشار سرویس‌های لهستان دوام بیاورد، ست‌ها می‌توانند نزدیک پیش بروند. در مجموع، کفه ترازو به سمت لهستان است.
🏐
اوج هیجان همراه با اسپورت‌نود، سه‌شنبه ساعت ۱۹:۳۰ دوتیم لهستان
🇵🇱
-
🇩🇪
آلمان به مصاف یکدیگر می‌روند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140391" target="_blank">📅 13:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140390">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pfl7vodPDsO8C9qH9OKMK5qaqBZetn5QQiYdOmw1If2_m1OMpToOgZyCE3ubuJcgnJ3GEi9SNk8GwrAfTRUZGHjRcxSumoI8MnboEZ0jP7W-gmJJObnlduh2awFBaRcaRz0P1n_4-qEfTyhZiKirtXNqk5peBj58tiKXkyppOQttRxUF8oZE30EdE90LOLXqQ4MpwDMhRfIJABfYKLBXozvGA6VuILLJffS2HToaJlotNXf7R9ng5dR3nWg77Odv4cWiExkyKHW_7rsJ1XpRBjjb85UdUTxYoJh0i-vXFC6gHU71Df-0uMHBkpERKMfIOt1iincl_ad8l6keyxQW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
بیرانوند برای فرار از سربازی، این‌بار به بهانه خالکوبی، دست به دامن کمیسیون اعصاب و روان شده تا شاید با برچسب اختلال روحی، کارت معافیت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140390" target="_blank">📅 12:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140389">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
❌
پیام علیرضا بیرانوند به میثاقی روی آنتن زنده: اگر نظام وظیفه اعلام کند من چه زمانی باید به سربازی بروم به جان 2 تا بچه ام فردا می روم سربازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140389" target="_blank">📅 12:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140388">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140388" target="_blank">📅 12:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140387">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoUzUJdY0KFGPXnt9056SI1VO6ph7v7oJjZKSxWOuwP7fTRL5HsNjmCNEOdNFkocX7yw-Z6eKTBRb8n2vXanzBORJyqzkGSLJsN-ImbIl_2pPx3Vu1iGEFBmThssZMVTvKsV53smAO-YHjQrbci0FsiCYAalThUwLBevQUetlw2rwpZ67G4B2KN4zlQhrsiS3bfGGtjDmsbsAe8FfVlzxRJVhVc250aKHQ6zC3scHGpDHSF_pzRRamu5tUeMJmr8HhRCHP-b0e7HaQ131F1fPnqv2GJfYha7-M6fnABwU_kq7ob3iMiigJbQ-9T_j5eMkgA8ilimcEk3UN7rITfTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
پرسپولیس در تمرینات هیچ مدافع میانی تخصصی دراختیار ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140387" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140386">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
⚡️
⚡️
⚡️
❌
سعید الهویی مربی تیم ملی: هیچ بازیکنی نبوده است که در این اردو به دلیل مصدومیت به اردوی تیم ملی فوتبال ایران دعوت نشده باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140386" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140385">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
⚡️
⚡️
⚡️
❌
سعید الهویی مربی تیم ملی: هیچ بازیکنی نبوده است که در این اردو به دلیل مصدومیت به اردوی تیم ملی فوتبال ایران دعوت نشده باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140385" target="_blank">📅 11:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140384">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
✔️
فووووووری از فارس
✔️
خبر ابطال شدن کارت بازی علیرضا بیرانوند صحت ندارد و این بازیکن تا زمان صدور رای کمسیون پرشکی میتونه بازی کنه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140384" target="_blank">📅 11:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140383">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚡️
⚡️
با درخواست اوسمار ویه را ، امیر قزوینه گلر تیم جوانان پرسپولیس به تیم بزرگسالان پرسپولیس‌ پیوست و قرار است به عنوان گلر سوم در کنار رفیعی و نیازمند به فعالیت خود ادامه بدهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140383" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140382">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚽️
صبح آخرین روز تابستان شما بخیر ‌.امیدوارم شش ماه اول سال و با دلی شاد و تنی سالم سپری کرده باشید ....پر برکت بوده باشه براتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140382" target="_blank">📅 09:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140381">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz5pYevN6_qMy0rlM9zgmq78KMXZ3SdL8ov74cT0OcmbmkhI_YxMDBNeMjWXHoKYB3di-pa_cnenajP2Mfag7nvHJfUdD8ZPDfBMtj0gMoayO6_dMK4Oc0IxF_zvX6DMHZMVurAXONg92ARPg1456CuhV3Bz0smTzw1YbxNnnD2tNfNsAL1NbRVRc5bsPlFUnvH1xo7jDXumq1zkLNxOjAcL1Bnt1Ag5iHNnGGxhtjZcd7jgSYiAXoOHllTakj0f2NKgOJNRx7kOiwobrAjJy_rW6ITk3h5PBTtL_kWTbGmBsdg1B_RYN7wk0PDniAIU3uHk_h9b_AMYSZVWSQsBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140381" target="_blank">📅 01:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140380">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
✔️
احمد نوراللهی بار دیگر پیشنهاد فدراسیون فوتبال برای عذرخواهی از امیر قلعه‌نویی و برگشت به تیم ملی را رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140380" target="_blank">📅 00:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140379">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
✅
پژمان راهبر: علت دعوت نشدن الهیار صیادمنش مسائل سیاسی هست و تا اونا حل نشه امکان بازگشت صیادمنش به تیم ملی نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140379" target="_blank">📅 00:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140378">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⭕️
⭕️
⭕️
علیرضا جهانبخش به پژمان راهبر: تا دو سال میتونم معافیت بگیریم و به زودی برای بازی در پرسپولیس به ایران میام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140378" target="_blank">📅 00:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140377">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
علیرضا جهانبخش قصد دارد در پرسپولیس به فوتبالش پایان بدهد
✍️
ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140377" target="_blank">📅 00:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140376">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی : مشکل سربازی ندارم و معافیت دارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140376" target="_blank">📅 00:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140375">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
✔️
ابوالفضل جلالی: هوادارا خیلی بهم انگیزه دادن و تو تمرینات هزار خودم رو میزاشتم. متاسفانه مصدوم شدم ولی الان آمادم
◻️
من الان طرفدار پرسپولیس، عاشق پرسپولیس و سرباز پرسپولیس هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140375" target="_blank">📅 23:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140374">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
ابوالفضل جلالی: من سرباز پرسپولیس و عاشق پرسپولیسم، همه کار برای هوادارای پرسپولیس میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140374" target="_blank">📅 23:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140373">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
ابوالفضل جلالی مهمان امشب فوتبال برتر است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140373" target="_blank">📅 23:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140372">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ابوالفضل جلالی مهمان امشب فوتبال برتر است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140372" target="_blank">📅 23:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140371">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
✔️
احمد نوراللهی بار دیگر پیشنهاد فدراسیون فوتبال برای عذرخواهی از امیر قلعه‌نویی و برگشت به تیم ملی را رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140371" target="_blank">📅 23:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140370">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
❌
فوووووووووووووری
⏺
باشگاه پرسپولیس بار دیگه مذاکرات شو با احمد نور شروع کرده‌ بود تا بجای قربانی جذب بشه و احمد برای دومین بار در این مقطع پیشنهاد پرسپولیس رو رد کرد‌/ هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140370" target="_blank">📅 22:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140369">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
کنایه فردوسی‌پور به فدراسیون:
✔️
✔️
استرالیا با برزیل بازی میکنه، ژاپن و کره با اروگوئه بازی میکنن بعد ما برای بار N ام با ازبکستان!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140369" target="_blank">📅 22:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140368">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: حسین کنعانی زادگان به تیم ملی دعوت نشده است که هیچ ربطی به مصدومیتش ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140368" target="_blank">📅 22:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140367">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a200ac824.mp4?token=orLHF4gOtLh1Bh_TQ2diTEkDd6WovC6TA0i_Zmoz3Abx7XQ3YpAofnZH9YMMGv8zRF2DR5Fk9t4vABe5o5Fu4kqlt2J23E1sV6Z8_BfJhAY2NAqVX83neyjoL7dm9nT0-azmv9B00iy0DvCRun1sd-0nrXC87KeK3zeLu-KAU8kJ-_BTIscpLZf-0Vxc3bmasl6QxcDjd_WgSmDDsRz4y_fw6T0i7_GbWBQaT2eEDE3iTWjOc5hrpibVXYa_veKuru9j_CnfCI9g-UNnu7Sv6Zt4_RSVR8q3YuNnMnhN27ayQdLCrQ9YORfYxfEZuG6cPGGCD1s8jleLPXKzGKJUrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a200ac824.mp4?token=orLHF4gOtLh1Bh_TQ2diTEkDd6WovC6TA0i_Zmoz3Abx7XQ3YpAofnZH9YMMGv8zRF2DR5Fk9t4vABe5o5Fu4kqlt2J23E1sV6Z8_BfJhAY2NAqVX83neyjoL7dm9nT0-azmv9B00iy0DvCRun1sd-0nrXC87KeK3zeLu-KAU8kJ-_BTIscpLZf-0Vxc3bmasl6QxcDjd_WgSmDDsRz4y_fw6T0i7_GbWBQaT2eEDE3iTWjOc5hrpibVXYa_veKuru9j_CnfCI9g-UNnu7Sv6Zt4_RSVR8q3YuNnMnhN27ayQdLCrQ9YORfYxfEZuG6cPGGCD1s8jleLPXKzGKJUrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: حسین کنعانی زادگان به تیم ملی دعوت نشده است که هیچ ربطی به مصدومیتش ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140367" target="_blank">📅 22:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140366">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
حمید کرمی مدیر اجرایی تیم پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140366" target="_blank">📅 22:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140365">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
✔️
فووووووری از فارس
✔️
خبر ابطال شدن کارت بازی علیرضا بیرانوند صحت ندارد و این بازیکن تا زمان صدور رای کمسیون پرشکی میتونه بازی کنه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140365" target="_blank">📅 22:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140364">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ch6hxNtpsuJ25lzIP5X1aqPvyBuprlz2VBHSAdpcBVPQ1vxSw11mjUlyfN5iV1_fMz1J-I1GO-OEt-i7utaMqBeSZFX_eqJcISEBSvJblC_yIXRCmKZHRappREkORPAmEdnmwWEgRZxwAattbvBxf1rrmnS33ZGrieRAr_PCZfOi4Rl5XjUBPHHMZMqVf3AM6esj1M2zVP1zLeCRd1YctnxL4WI6iR8PSojwxDJHomZqEMwwb_7l0G3nCu-WT5lQEfjxRZVjgAn9QSmsqtareHSTUBSmuOvnh6Mq2HHy0ZMZL1aYd5WaC7SFQunfMIfz8NxJ_fTuWwiPQWLJiu_dKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
به نقل از رسانه ها دنیل گرا بزودی با گرفتن ۲۵۰ هزار دلار از پرسپولیس جدا خواهد شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140364" target="_blank">📅 21:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140363">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
✅
تیوی بیفوما که بدلیل مسائل سیاسی دعوت تیم ملی کنگو را رد کرده بود دقایقی پیش برای حضور در تمرینات پرسپولیس وارد ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140363" target="_blank">📅 21:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140361">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BExVCrEfvDhrADxLkzrBkafQ3xuym3eyU-gX5MBO8fGpoMXAMzGm9g6Pqgn-MeGgRHftF2U0PGYQTHPIJxep6dtmw68ugjg0iiPurdqbmYD8iEbb6euL1dHMDXvtwdVcFfJhTsyM11NVmHPVD40rzgYnDjTgozk4zPS-l5N-duEtGuX4R2_k865fiqUMmdts17B2cBc50NE4BeZZ81TCUpYolO3ZArpToNGnWCoUXS0CsjtkZNM82F-HgmVQzmVDOuAm1oHb9Z_IT2Uz7SC1JSznIUFJY_7wJeAD-LTqLJ7mV1iRRJUk0XMd0q2koxWRtK2728fdMuQE-ZWxIUnNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی جام ملت‌های والیبال به اوج هیجان خود رسید!
🏐
نبردی حساس و تماشایی بین اسلوونی و صربستان در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با اسپورت‌نود، دوشنبه ساعت ۲۲:۳۰ دوتیم اسلوونی
🇸🇮
-
🇷🇸
صربستان به مصاف یکدیگر می‌روند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140361" target="_blank">📅 20:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140360">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
🇨🇬
تیوی بیفوما به علت مسائل سیاسی کشور کنگو و در حمایت از مردم، دعوت تیم ملی فوتبال رو رد کرد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140360" target="_blank">📅 19:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140359">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140359" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140358">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
با ‌درخواست تیم ملی علیرضا بیرانوند تا نیم فصل اجازه بازی خواهد داشت تا در جام ملت ها آمادگی داشته باشد سپس به سربازی میرود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140358" target="_blank">📅 19:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140357">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmYrtjxpAPA3kis4Mp_YWqK-5OCb6a4B2kDylUYpxWn02Z6CEr9WIshYUwOGtqkaziV_Wc8VdlQ7zJya0ewH30oIUvS6Vtt68PiwGEwvsiAC-Bmh3PLQ9o5x8L7pQLSMAjggkzYczEihDm-1xQ2ZjLanF3Wtax719IV7BclwikzFymLVknGPFjZ3GnmMl5aQufgfBfsOVjM-zEdQIEl46-wareorMLcaetr7UMd6dng5tn0qc5-y1I6Rz41dv87QC1MgyvKPH2h1l5zKh33ZxIMlBIoJdvkRVrczSB6niANixexozNd4qL07qlsHE_wDx4Fnoc5LnLgsPKgjSreobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمید کرمی مدیر اجرایی تیم پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140357" target="_blank">📅 19:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140356">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری از فوتبالی
🚨
سازمان لیگ کارت بازی علیرضا بیرانوند برای تراکتور را باطل کرد.
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140356" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140355">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp3r1aw-jUpKC4ksfqD5AY3ArT_3m-3JkuGGXb0TcrjfpIh9bFI05tDwP6NTt5orJsYyCHFSYcMt__2Ef3eeqnCpCBVb_r2gJdc9jImVMVOyvo4NcfvNAgyzzg3jZWR18lQ6Vkz8983nxTvIlVhjR6eQ-TyV91wflvnOx_8cp-s9K8Gc_ylHWLpV2_McbaVL5gSjnBqOg7tEiJrzCc3JXjS4yBryY8zFzbWyM38GmeEWv_pXKQNHPCcUni6DGddyrSS5VoD-UPgy0rMjtzl1vSLI4YaROGplVImogZGpzwceu73XHsWDgJfkN1aInKKGTwLBYGPLtou2VWUYWgDs5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری از فوتبالی
🚨
سازمان لیگ کارت بازی علیرضا بیرانوند برای تراکتور را باطل کرد.
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140355" target="_blank">📅 18:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140354">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140354" target="_blank">📅 18:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140353">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFlUcSx4G8SS_nM8AWibKI78RdJ2O0UMkCEYrAgYNNJC16hVgVkmM5yzGFMdIH8irysHsC9fjIAtMMxjlaEpUTqboBxjOqIlN3ILhjxNdFvP75wE5_PyyrLTJXWfspJ2EsOTeqinyZWVmzormxasxSL1muZb-un1_frefaB639DQvILBPGLILlNOIJCsGvCaA5eJyF0e0oQdWbs8seERfskdBeqyWAeqq7awfoB2xu0zxsYp8FKccYNK-VmW_q-k6nzOntupe-4_0myVEXpnm7ubIV5Woy30up5x75m97wef21wxlj6p5hpyX0Coxcq0Npj92X35tZ039wHbTBVesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بسته شدن پرونده حقوقی بانک گردشگری علیه پرسپولیس
🔺
باشگاه پرسپولیس با انتشار اسنادی، خبر از تسویه بدهی این باشگاه به بانک گردشگری خبر داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140353" target="_blank">📅 16:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140352">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140352" target="_blank">📅 16:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140351">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
پیگیری‌ها از مسئولان باشگاه پرسپولیس نشان می‌دهد که هیچ پیشنهاد رسمی از سوی باشگاه‌های خارجی، چه از قطر و چه از سایر کشورها، برای جذب محمد عمری به باشگاه پرسپولیس ارائه نشده است و بحث جدایی این بازیکن صحت ندارد. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140351" target="_blank">📅 15:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140350">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
✔️
از باشگاه پرسپولیس خبر می‌رسد مسئولان این باشگاه در مرحله استیناف مدارک جدیدی علیه یاسر آسانی را نیز ارائه کرده‌اند و امیدوارند با بررسی این مستندات، رأی مرحله نخست تغییر کند/ فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140350" target="_blank">📅 15:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140349">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140349" target="_blank">📅 13:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140348">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q23aXDDxcGrTk2Hg9cRG_BGI5Fl4ipbPZyo9uFUlNEaAaxSCQtOrC-DoiERq-oSedjPaPlOdthqOxAFheXiqzi3lCOgPHqAnsWG7blqzeWBa1csOsVzUUvoA2fpk8PsLwSbSt-xYa_9ysKAVjmBiGVb4XYDZdqnmA5zQ16EGZsCHwEFogubxjSrIV05pm4JNEynkGMAqKrZvWDbK1O7nKAC2HPxX3N8iqyyqCS70xCjVCTr8VxWoGrYAycB-XIVFIm4LPekh7_DkpOZYc8Gxc1eA6HgC3wf3j4J5gAkl2c0WzI6p-zyzwYtDikIjzu3IUyPgw_8_BKahoA8HXBao4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140348" target="_blank">📅 13:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140347">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140347" target="_blank">📅 13:11 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
