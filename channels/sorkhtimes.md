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
<img src="https://cdn4.telesco.pe/file/FDV-TlqD8hcFIxULa7MZzl8HGhmL90mwI7NEpZe3qhiiLzkssm4CH3hUledV_Yf0LUKblsBBerFtYhsxJox_IQqJqmn8feW7TaTHQ07smAVzInZB4LWAXXai3wFR8cJlsyDG2YhDfUXqAzEudsal5TPPHzKdTUyH6Nd_qt4kuRc2BnkrIp7F88QbHMUdCq73sHv0l9lQLY8Vlx9BnvvaS1QHOESSMIqrhEU805T2lJ1D4dHxveq2Q7Mu3vGNqvZzltmBPt_N-v6MrRhv_aDE_b8U2jFg9sCkaagXwT-6YkkV8tucy51ilEzYhyBhSfaswBSQRV4GI00UogjCvwIa3g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 20:46:10</div>
<hr>

<div class="tg-post" id="msg-137060">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-VeI5iUqCNa7kJA7NGmR7ul7nyoZ7URfzflB0itjf6t21GHXEZUx59CLDmPnNTjOeaC4qo9LbhMAsHvGWFatRJrW32E0mu__BgcgPYkQ7fLH88FO83-tO8SOHNvox2lhr8UPhcx2JFwQgV0Z8A3zGuL4m04ZWL0kq1O85r7bTQ0_fWcgZT97BcKp8JNpukjkYVkNb0x0tWtoa0uziUiHsneEYBM-pzaKQP3S0uMIZ7F9GE-VkP6ngeBE82n0nT8UE62sqHcdtvxghhHY8fmOHq97v46xEeZJ9gRUT88v1oCfFbCftYQArVQ08GfgVnygbWjS8dvdrj5vClY_lYs6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 31 · <a href="https://t.me/SorkhTimes/137060" target="_blank">📅 20:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137059">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
❗️
عیسی آل کثیر یه ویدیو از زمان حضورش تو پرسپولیس استوری کرده، پروفایلشم به عکس پرسپولیس برگردونده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 426 · <a href="https://t.me/SorkhTimes/137059" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137058">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu8wJbeWX2PqOgoa6tq1-_byP0HLuehmaF8cVleWb7xBKEDIxUlF2oU1M32b9vCmuYb_UR3DFno2wgcGVQ9WE6l5dlwj3DsrD7vaecRIWinTkpfe8wgthB9FjV6KxygVbxdK7cgZne_PC3RvqTr7iXb8omTUyGp-lvnkNADfnXqi6JfS9NCm_KvoG3Cj_Q0gC5_JIu2GgebruOxZDZnDX4K4zFGVTy3l1rtEaYMjg0ykUSKM_CVOpXIK2_z3xIRqicJEas_uSPeIjlwAXLRc2K_nJjIRYgZTWVfUj6dD4sXk3V-NiLd89NPNqXXNE2KCJUTnlG6t0Zb5mIvTVYwtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی پرسپولیس برابر آلانیا اسپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 762 · <a href="https://t.me/SorkhTimes/137058" target="_blank">📅 20:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137057">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚡️
پرسپولیس به مانند بازی قبلی در دقیقه نود به گل رسید و بردهای یک بر صفر تارتار در دقیقه نود ادامه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/SorkhTimes/137057" target="_blank">📅 20:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137056">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
🔴
🔴
توجه | مدارس و دانشگاه های استان تهران غیرحضوری شد
⬛️
استاندار تهران:
⬛️
با تصمیم کارگروه اضطرار آلودگی هوا تمامی مقاطع تحصیلی استان تهران بجز فیروز کوه روزهای سه شنبه ۴ آذر و چهارشنبه ۵ آذر غیر حضوری اعلام شد.
🟦
دانشگاههای استان تهران بجز فیروز کوه غیر…</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/SorkhTimes/137056" target="_blank">📅 20:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137055">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-s0yl22q0n3WBlqGjUmP93AtLQwdopO1aZ5qSXruMiW0Smri16mMUhCtIzKliSnj11ZISrEQhMhbFSpDn0Yk1E0jkc2p9tJV4T_AprE-BU6j2YfJOtbqY2SOHchtvnDoZ4AnrS_J3ufIfXzUdAOyoPrkZrswPUdzRlqU0zg57v_th6-7dL_iDfTlkKgsvXRZNR6-pj1iBXPa4NHesTg2fmBfQJ-rqFRkVs0W5gZnhGIePD_TX_UtvzZfHVnWgRY5dA69M9-DU4f1whMgiETpJHSCvXj4nErtJXwqQpNDjQaph42KNiSw0bNKQKdDODhF6ZvOqQrtkH2gMEgypkuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
برنامه بازی‌های مقدماتی لیگ اروپا
⚽️
امشب لیگ اروپا بار دیگر با تقابل‌های حساس و تماشایی، فوتبال‌دوستان را پای گیرنده‌ها می‌نشاند. تیم‌ها برای صعود و نزدیک شدن به مراحل بالاتر، با تمام توان به میدان می‌آیند و همین موضوع نوید مسابقاتی پرهیجان و غیرقابل پیش‌بینی را می‌دهد. شبی پر از رقابت، گل، هیجان و لحظاتی که می‌تواند سرنوشت فصل بسیاری از تیم‌ها را تغییر دهد.
⚽️
بازی‌های امشب رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/137055" target="_blank">📅 20:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137054">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⚡️
پرسپولیس به مانند بازی قبلی در دقیقه نود به گل رسید و بردهای یک بر صفر تارتار در دقیقه نود ادامه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/137054" target="_blank">📅 20:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137053">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔄
🔄
🔄
جونم تیم ..پرسپولیس دقیقه نود گل اول و برتری و زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/137053" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137052">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚡️
نیمه اول دیدار دوستانه پرسپولیس و آلانیااسپور بدون گل به پایان رسید.  در حاشیه این بازی، محمد عمری و اورونوف در کنار محمدمهدی محبی روی نیمکت و زیر باران نشستند تا یک قاب جالب و متفاوت در ارزروم ثبت شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/137052" target="_blank">📅 19:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137051">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
آلن هالیلوویچ فردا در تمرینات پرسپولیس شرکت میکند.
🔄
مهدی طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/137051" target="_blank">📅 19:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137050">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚡️
⚡️
تایید شد
🔻
🔻
آلن هالیلوویچ، بازیکن کروات با اصرار محسن خلیلی به ترکیه سفر کرده تا به صورت تستی در تمرینات پرسپولیس حضور پیدا کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/137050" target="_blank">📅 19:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137049">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚡️
⚡️
فرهیختگان: مذاکرات تراکتورسازی با الوحده بر سر قربانی به بن بست خورد ؛ چرا که زنوزی دنیال تخفیف هستش و قربانیم حقوق بالایی طلب کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/137049" target="_blank">📅 19:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137048">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyMbwjnjdy_yCcvN5bgWPEI4z0DX-fJ9oMtO_YH7I9uWUJ8mAo45jlSsbu_mwK06rlxL-fhLHSwmwp3Zb6yu4u5BQHklBuiQ-jMzVCVn57d2u6vb_CQxf0EPPHZVc7NgAca1B3URXnrg67hpOPRjSxqb1ev0XEdWSEarhNpci7VgogqSPa3A_VqFR_LXqMa3wnJmfv7oWGl9X8be0x8tXjyGCZGShBg2MQJwylTAw-LSdPXdxisqIvJTMOdvYKmzkEXGFV-7Q8FsScQXO_1lEB44STQUw7d9IbQ1k6VsHje90GU1Bk2967OCLWVX-Cto9jyY-pB7vokl59H6YwpUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
نیمه اول دیدار دوستانه پرسپولیس و آلانیااسپور بدون گل به پایان رسید.
در حاشیه این بازی، محمد عمری و اورونوف در کنار محمدمهدی محبی روی نیمکت و زیر باران نشستند تا یک قاب جالب و متفاوت در ارزروم ثبت شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/137048" target="_blank">📅 18:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137047">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🫥
🫥
با موندن امیررضا رفیعی پرسپولیس میتونه 5 بازیکن جدید در پست های دیگه بگیره
🔴
دفاع وسط
🔴
دفاع چپ
🔴
هافبک بازیساز
🔴
مهاجم
🔴
دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/137047" target="_blank">📅 17:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137046">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
✔️
طبق اخبار دریافتی غیر رسمی : باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/137046" target="_blank">📅 17:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137045">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⚡️
⚡️
فوووووووووری
⏺
باشگاه خیبر خرم آباد رضایت نامه مهدی گودرزی رو 70 میلیارد تومن اعلام کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/137045" target="_blank">📅 16:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137044">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚠️
⚠️
⚠️
تغییر ساعت برگزاری دیدار تدارکاتی پرسپولیس و آلانیااسپور
⏺
این مسابقه که پیش‌تر قرار بود از ساعت ۱۸:۳۰ برگزار شود، از ساعت ۱۷:۳۰ به وقت تهران آغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/137044" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137043">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
✔️
طبق اخبار دریافتی غیر رسمی : باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/137043" target="_blank">📅 16:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137042">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT04ujgiDr_WW_0yaCjaZ0ZTz_SpeYm2zgv0rd8YyTWNRRe-TOnB8g5rkT1F2y8HmBfmfpUvkbpM5WJQhg6wRNWenZakpLrlGWOE3mUYLrJ3WQI2KsAZ2bRCB1xmit46QM1_c-nPGF_W2F7dKw7vbAar8k9DE707kR1DF5MhjutYFkz3rCnTZynDTHqUhzDUvus8q4vi0TVCrhF-4LwIakbx3THNifo7HcsAq1JSanPlFlEUSr0Ddntg1t-rdlfRubZpW5fltaLT1An9ZYX2o_dpKXVesNDjQaLZyDAi8ila9xFKJ2TVX9Q6ZVxTAt2kK2R4E5aVsGqKJQB2ie6VlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
اوج
هیجان و جذابیت با لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
پنجشنبه ساعت ۱۵:۰۰
[
لهستان
🇵🇱
🆚
🇺🇦
اوکراین
]
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/137042" target="_blank">📅 15:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137041">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
🇳🇱
رسانه‌ی هلندی:
🔴
آلن هالیلوویچ در آستانه پیوستن به پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/137041" target="_blank">📅 15:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137040">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_sU3dysQPoBuTdGOCse_VmEacGd6eLz2XwvbEQXWFiZyXPet1vbi92pT4tz1H2Dkkrr7oZaif9jPNS481IgKh4AElzxq0xNtpdyeW8JTlsSkn8gDqLSg41fbpndo_3Elhf_zYEM0w9tPcVDD4EowJduYEazzFrAJYuR-iAQle3unbZYNi0oYWkVHjMUO-sQcY2rDA_WN8i_iWthmtZ0_u8BwBUY1TPR5Flsq-TkBQrCMQkDKepadj0psikaK4ZheNONoMhLBD0ono1Jv9bW_0JY_eC4M51o37b31eOS5HW-bsnUNPZTiZaC8-KA2u9WscCJFMpDDyPBxgv3KVRm3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ورزشگاه دستگردی تهران حداقل تا‌ دوماه آینده بدلیل تعویض چمن در دسترس نیست و امکان برگزاری و میزبانی از تیم‌های تهرانی را ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/137040" target="_blank">📅 15:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137039">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
❌
حضور مسعود محبی در روسیه منتفی شد/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/137039" target="_blank">📅 15:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137038">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏅
آلانیا اسپور حریف تدارکاتی بعدی پرسپولیس در ترکیه
▶️
با اعلام باشگاه پرسپولیس، شاگردان تارتار، روز پنج‌شنبه در دومین بازی تدارکاتی خود از اردوی آماده سازی پیش فصل در ترکیه، به مصاف تیم آلانیا اسپور خواهند رفت که خود را آماده فصل جدید رقابت‌های سوپر لیگ ترکیه…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/137038" target="_blank">📅 15:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137037">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
تارتار گفته عیدی تو فاز هجومی خوب نیست و ازش راضی نیست  پ.ن مگه با نظر خود تارتار جذب نشده .مگه بازیکن خودش نبوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/137037" target="_blank">📅 14:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137036">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/137036" target="_blank">📅 13:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137035">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
#منهای_ورزش
✔️
باز هم جنوب باز هم مردم بی گناه
💔
❤️
✔️
شهید و ۲ زخمی در حملۀ آمریکا به محله چاهتنگو شهر قشم
✔️
دانشگاه علوم پزشکی هرمزگان: در حملۀ دشمن آمریکایی به منزل مسکونی در محلۀ چاهتنگو شهر قشم، پدر و مادر خانواده و یک کودک ۲ ساله به شهادت رسیدند و…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/137035" target="_blank">📅 13:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137034">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/137034" target="_blank">📅 13:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137033">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915de24844.mp4?token=CmcLpqGvp1x5TcwAPIqC2X1-y4wwH9TEtEK1khEH4tmOIRStvC8qA2pQd_SS5S_KU3iWGXerxOx22yDPEY90BrvnglzrD6hN-dDwfpbbb-c8RkcY-nT4XieyxjEgF0NhWPSm655L6FUfWgoTj5xaMjgB8FrZf4hD7w3-W2w8kn3lx75WjdTLQ4So9kgRzeOynKJXUy9JTTgPV4XwrjDpW-Gqfh6NR-9a712vhVSshduFk8svhqQZDTokm0Vk129N82qPKnq12OUdBply139AhhS8ldQzHYElTZroFmoxi4qq-ODK9NoTf4fm04h9vO36rdOQysKjcwlXjV6BgXU9z7QkjYULQqLdWiVFO9fAeIGyAz7hlMR8k5nl2myzU3bBV9i0dyiC5c4O8Son9sKXrNEDy5ti1Z_ZsBZpuJQwKdjCq3UICIRvLrJh2Yd3qSSqR0AMhRmN3_j8UAz_OHmauzRPpzDBFS0mo33yeTy_mO6lkwMa9FULlySrS0oMcw1I05T2ciEQvFN0XQnsTpOfD5a21lReLl4L2GBjwEy1rhVBVu7R-XaEBjumO3O8MhnXRaBO28lr3kze7dod8nSrcGQ2aDDNHqhPuZEYVltWrgJ77l1-GitiwOmlJlNBBxg-mxKxjfavngY34FWrBfp1TA8dFv6kYE2g0CkKanHttGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915de24844.mp4?token=CmcLpqGvp1x5TcwAPIqC2X1-y4wwH9TEtEK1khEH4tmOIRStvC8qA2pQd_SS5S_KU3iWGXerxOx22yDPEY90BrvnglzrD6hN-dDwfpbbb-c8RkcY-nT4XieyxjEgF0NhWPSm655L6FUfWgoTj5xaMjgB8FrZf4hD7w3-W2w8kn3lx75WjdTLQ4So9kgRzeOynKJXUy9JTTgPV4XwrjDpW-Gqfh6NR-9a712vhVSshduFk8svhqQZDTokm0Vk129N82qPKnq12OUdBply139AhhS8ldQzHYElTZroFmoxi4qq-ODK9NoTf4fm04h9vO36rdOQysKjcwlXjV6BgXU9z7QkjYULQqLdWiVFO9fAeIGyAz7hlMR8k5nl2myzU3bBV9i0dyiC5c4O8Son9sKXrNEDy5ti1Z_ZsBZpuJQwKdjCq3UICIRvLrJh2Yd3qSSqR0AMhRmN3_j8UAz_OHmauzRPpzDBFS0mo33yeTy_mO6lkwMa9FULlySrS0oMcw1I05T2ciEQvFN0XQnsTpOfD5a21lReLl4L2GBjwEy1rhVBVu7R-XaEBjumO3O8MhnXRaBO28lr3kze7dod8nSrcGQ2aDDNHqhPuZEYVltWrgJ77l1-GitiwOmlJlNBBxg-mxKxjfavngY34FWrBfp1TA8dFv6kYE2g0CkKanHttGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
❌
بهترین خبر امروز: نوید قره داغی حرومزاده که دخترا رو کتک میزد، دستگیر شد.
🔴
امروز صبح موقع دستگیری نوید بیشرف ، این حیوون وحشی به سمت پلیسا حمله‌ور میشه. پلیسا هم سه تا تیر توی پاش و یه تیر توی دستش میزنن و حسابی کتکش زدن، اعضای محل هم هر کدوم یه انگشت توی کونش فرو کردن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/137033" target="_blank">📅 13:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137032">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
شنیده میشه پرسپولیس دوباره رفته سراغ مسعود محبی و با پیشنهاد جدید دنبال جذب این بازیکن
🔹
محبی هنوز هیچ قراردادی با تیم روسی نبسته و امکانش جذبش هنوزم هست همه چیز بستگی به نوع مذاکرات و پیشنهاد مدیران تیم داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/137032" target="_blank">📅 12:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137031">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎥
⚽️
ویدیو باشگاه از تمرین تیم با کپشن:
😀
از ضربه‌های تمام‌کننده تا واکنش‌های تماشایی؛روزهای پرانرژی پرسپولیس در ارزروم
❌
پ.ن حال پرسپولیس خیلی خوبه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/137031" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137030">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🫥
🫥
با موندن امیررضا رفیعی پرسپولیس میتونه 5 بازیکن جدید در پست های دیگه بگیره
🔴
دفاع وسط
🔴
دفاع چپ
🔴
هافبک بازیساز
🔴
مهاجم
🔴
دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137030" target="_blank">📅 10:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137029">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
پیوستن پورعلی‌گنجی به الطلبه صحت ندارد
⚠️
⚠️
ساعتی پیش برخی رسانه‌ها از پیوستن مرتضی پورعلی‌گنجی، مدافع پرسپولیس، به تیم الطلبه عراق خبر دادند اما پیگیری‌های خبرنگار فارس نشان می‌دهد این خبر صحت ندارد.
⚠️
⚠️
پورعلی‌گنجی هیچ قراردادی با باشگاه الطلبه عراق امضا…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/137029" target="_blank">📅 09:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137028">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/137028" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137027">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⚡️
⚡️
امیررضا رفیعی قرارداد جدیدی را امضا خواهد کرد
🔻
🔻
رفیعی یک سال دیگر با پرسپولیس قرارداد دارد مشکلی برای همراهی این تیم نخواهد داشت اما احتمالا با تمدید قرارداد در جمع شاگردان مهدی تارتار حضور خواهد داشت و زیر نظر حسین اینانلو کار خود را دنبال خواهد کرد.…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/137027" target="_blank">📅 09:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137026">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/137026" target="_blank">📅 09:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137025">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/137025" target="_blank">📅 09:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137024">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/137024" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137023">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toPQA_r3cSjHxgtkMwSAncsfvEt_987yRkBaHwWYO8e6co8_ObuxUp5YhtCpjqt6rYXud52AwJj86SqN5G1XdjJ__hyI8ifD51mCnSkm30FPtqRAMl7GCgm14K0hxNUhuLorsC9g0ujYCzMnaWRKJzXVwPXtiH4ACWt_sfYm8xdh5-RLqMz2Pwu-dvdeeASCLzXkBhlszyWruiQAi0eCnGQ3snHuz0PSDBnCRtuDEgk0HvghlNMW-oNSPaXjxmYPH5q8CYqWr692Z10aqgY1h6DES749u1Lnj4vABi6nXUr4QNEboECERiMIIoDaJhacIPbhg7sg-qH7Bq9d5Qe9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/137023" target="_blank">📅 08:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137022">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwZBVBAAPatRFo12_rgS0jf353mM5TwYSlI_6FJMeUwDMRgTPt5pyEfavQJAN8Y1OorNMr_RtQwx05QMeE4bRJHNE3egHOi5-25-mBOKnhqeLSPBIGmcKN1h3JCjznS5N0bmyGt0dCgD7j_Q7c1bm9zWia2Fz9OpCnpf3aJoEIP2j5mQckFi_ZcJWCsaxiN-I1b6oy0jQeCijE0TFut2DFpsKKH8veq3QuByY5IY7213u4Zw9hRYIY0t5Yz2_NAcy_sN9An72WVKHtxp9JPeybLLWheyFAOfWMNyNSf__4jRgbRsubRUZU4aBwybM_Kr0yMbUJDn1NMt-mM30hVmCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
اوج
هیجان و جذابیت با لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
پنجشنبه ساعت ۱۰:۳۰
[
ایتالیا
🇮🇹
🆚
🇺🇸
آمریکا
]
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137022" target="_blank">📅 01:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137021">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-VmDaQOCgr7_1K49nNInRGWtNy8tWbD0PBxXwDBhTO0vfpVZGKLFllFzEK2Va2ZoK6AiyudATxkOC-x3YASV6Cn1CBNEzs4TzdOHMF5xJ73tyw8MYRCU3L677grzL2ohK2qEsc9nt_aVkd-BJ8_R4qfX_AqfkmVeY_b_t9jzpdughuAfu9UnOkfLC9qZadd0NtM7mgE8ltgYWguWAs-bcsC8JoXvJJfSqptF0yByEOz3YSb4ODERAKRqsyH5qPpJvKLCEK1098ZwLW4QgIG-ixglITdYzmvpu6n6TcLJfXwpWV-i_RZ1m-9RoAEQCsUCeaiLGAst-szlqb9XkEFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137021" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137020">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❤️
❤️
❤️
❤️
❤️</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/137020" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137019">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137019" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137018">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
تراکتور از جذب قربانی منصرف شده و کناری گیری کرد /فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137018" target="_blank">📅 23:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137017">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137017" target="_blank">📅 23:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137016">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
فرهیختگان: اولویت های تارتار در پست‌های مختلف
✔️
گلر: گوهری
✔️
دفاع راست: محرمی
✔️
دفاع وسط: افسرده
✔️
دفاع چپ: رزاق‌پور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137016" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137015">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔽
مرتضی پورعلی گنجی با باشگاه پرسپولیس   به توافق رسید و قراردادش امروز فسخ میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137015" target="_blank">📅 23:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137014">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔄
🔄
🔄
آنا: محمد قربانی با رضایت نامه 200 میلیارد تومنی به تراکتور سازی تبریز پیوست
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137014" target="_blank">📅 23:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137013">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137013" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137012">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
دنیل گرا در تمرین امروز هم حضور نداشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137012" target="_blank">📅 22:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137011">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
شهاب زندی مدیرعامل نساجی:  با استقلال درحال مذاکره‌ایم، با توجه به بسته بودن پنجره شون اگه بر سر مباحث مالی به توافق برسیم این دو بازیکن آینده‌دار نیم‌فصل راهی استقلال میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137011" target="_blank">📅 22:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137010">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⚠️
⚠️
⚠️
مدیرعامل باشگاه گل گهر سیرجان :
⚠️
⚠️
امیر جعفری مدافع چپ مدنظر باشگاه پرسپولیس قرار دارد اما تا این ثانیه به صورت رسمی با ما مکاتبات نشده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/137010" target="_blank">📅 22:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137009">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
دنیل گرا ۶ هفته از میادین دوره و ممکنه باشگاه باهاش فسخ کنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/137009" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137008">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4994f708ed.mp4?token=ie1NGtPCUKqUh7_XFrY9ZLOc9v-KxcMryRlxtq6D3DYJWuTtdMYwGg86iffUZini6FHj0mKi722m3-3m1h5-L9pkbnv5T3AtrgqVzsR-GY-c7npvyjo3cs8rDeWRm8vkhrI2pH4KTw7_eKdYniR3RD8n9LLeo5L5ovyMFXPP4KsWeY-JPAl9bat_MM4tZxYb3FZqAHJ1DYNXyTu3ZJOubWxnETo7qoUuK5OCdff0Gm0ifvXnbFpnSqSAPzezkzg0_owdwfRNN-g0qt6kV7-OaTCGIDt6erRutMd8yX9XW-7sW7wP0AKYxySaHOaOiVjamNLnLlz8SZuAsa_ITJ_Buw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4994f708ed.mp4?token=ie1NGtPCUKqUh7_XFrY9ZLOc9v-KxcMryRlxtq6D3DYJWuTtdMYwGg86iffUZini6FHj0mKi722m3-3m1h5-L9pkbnv5T3AtrgqVzsR-GY-c7npvyjo3cs8rDeWRm8vkhrI2pH4KTw7_eKdYniR3RD8n9LLeo5L5ovyMFXPP4KsWeY-JPAl9bat_MM4tZxYb3FZqAHJ1DYNXyTu3ZJOubWxnETo7qoUuK5OCdff0Gm0ifvXnbFpnSqSAPzezkzg0_owdwfRNN-g0qt6kV7-OaTCGIDt6erRutMd8yX9XW-7sW7wP0AKYxySaHOaOiVjamNLnLlz8SZuAsa_ITJ_Buw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
تمرین سخت امروز شماره
1⃣
🧤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/137008" target="_blank">📅 22:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137007">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
🔴
تارتار همچنان ولکن گل‌گهر نیست
✅
شایعات؛ باشگاه به دنبال امیر جعفری مدافع چپ گلگهر!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137007" target="_blank">📅 21:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137006">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mGJy4HnY27iWelaU6IHhlOW_-Kdoy84XDZuy_FBYn5om9i4eCLMSwLNnaDnzkwLnFPGzCGl9xuOufIvhYnPJcg1KPOp1bLtM0_wapq5Bf9gU-WEg_nmw82EyZj-Qhv4RXju0YVUE3nhmgjJWSDaGGQGKKDIxwWLkVJBsDK7zFvqtrh9dQUs0h7WiqA4pIaZpkUa2kiZrzSEZ4mk2WX_RgG2VdWNlM_xnAiCSAvHMLay6Rtpw8_PaB90akrSv5XmZGwM9swoKW5pFa9IaoyBLsjy6iPJ4H6AkEMKC_iNDA9nslPXPVdMXSeMORqrnp2kQbxBYXF0C08Cav-Q-Db-QuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شنیده میشه پرسپولیس دوباره رفته سراغ مسعود محبی و با پیشنهاد جدید دنبال جذب این بازیکن
🔹
محبی هنوز هیچ قراردادی با تیم روسی نبسته و امکانش جذبش هنوزم هست همه چیز بستگی به نوع مذاکرات و پیشنهاد مدیران تیم داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137006" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137005">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
یاسین سلمانی ۲۰ دقیقه اخر بازی دیروز اومد زمین همه جا حضور داشت چه حمله چه دفاع
🗣
🗣
پاس گلشم روی یک ارسال تمیز شکل گرفت. با وجود اینکه جلوی چادرملو هم بهترین بازیکن زمین بود نکته عجیب اینکه چرا رسانه‌ها اصرار دارند مازاد بشه.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137005" target="_blank">📅 21:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137004">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoI7sm-o36eGeYgsmQaGNfBnmEHr_O2bqY1wG91tqtfJPQ7aRSyX3fiByzcu8E-T0pLhzReT2SKOkQrv3IxrNGiuWp5hM5IeS1Da_pyDfi7zbTMbEize3H5WvJ-MokaHdSmjKyPfOSGd9gKwQ2iVJ5tr3GERjqJUznEzjtpm-Noymd-BQHQqW0WwpUTNoFtW2bOcB5n75sl60U5DDYUXOUHgYoWr9dzXCUJroXhVgBeD4Rqg6i6cRIlB5dwXEOM9WvBRP3FWyPL4kwt1-QS8N_8yeP9xVS7p7ZOcaCp3zjYIpzQoPR7xukSy8df5vEsMDqLQYy5_VaJIO3woV89-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نگاهی به ۶ بازیکن ارزشمند لیگ برتر در سایت ترانسفر مارکت با حضور سه بازیکن از پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137004" target="_blank">📅 21:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137003">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlB4yv2swfiGbCsj59ip0TUJmwnb992t_gnYsFzNWvYOUEW1GTp83gmndurk4adHlIvswpjpqvPj0tY0hLqpFrkVVmftFwcqw-0WcA8PAu7kM8G39B3dt2c_0W9NGG4Gx9X2-sPLodGEyxF2j2GNOo9nM9CQFq2lgTx_wJJKz8XI-tSw88pdj5OHxoQe2sztptlhSxQjZpSx-G8UsYJQULgoeblpdxakagLknpoo8ICjWc7SpVS2DfnX9n3Lb3xXGdsADNmqBW6XHginx6u7i9x4eG5LNYTrSd3wcXL4PNStpj9KOsaytT9pJSHzN64094fQK0-v9CDWwOsX4MxYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
زیر و رو شدن چهره پرسپولیس پس از گذشت 2 سال
🟪
🟪
از ترکیب فیکس پرسپولیس مقابل مس رفسنجان در روز قهرمانی، تنها حسین کنعانی و استون اورونوف در این تیم باقی مانده اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137003" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137002">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🫥
🫥
🫥
تارتار امیدواره بیفوما و محمدحسین صادقی رو دوباره احیا کنه. بیفوما بعد از یه فصل ضعیف، تو بازی دوستانه اخیر گل زد و حالا فرصت داره خودش رو ثابت کنه. صادقی هم که فصل قبل فرصت کمی برای بازی پیدا کرد، امیدواره با اعتماد تارتار بیشتر بهش بازی برسه.
🌀
🌀
از…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/137002" target="_blank">📅 20:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137001">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN485V3dxf4j0PpnEDG5QMjMe9XEqt3MubwWRX8DnM-aWo7KYlE1UeKlhVlrGiBh6FSK65SN52E1V3cGo9UTVOg2AXQHmWoRHTd-XkJ15hcf-GzT6CwZghJl-AyF5JYEeKP7yKWzDlqC_pmLcy3WT34NhGW0zzgBea3k3jFgxfswITpI5aTvgUlvpkTwkf49YoPM2szchHIdRFXYmMBvyGQZR8ffXjYvOEp-dPBiX3LuFSJjeI-tRxC5tq1LwTf7drNLH8nl2UQJhN5_JaZ4Ft0OFQ8iydaLHATy8Krqjzelaf_PCao5Cav5y4Wlf2USOpR5s6kfZCRhU97pMW3NYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
اوج
هیجان مرحله برگشت مقدماتی لیگ قهرمانان اروپا همراه با
اسپورت نود
🇪🇺
شبی پرهیجان در مسیر رسیدن به لیگ قهرمانان؛ تیم‌ها برای یک گام دیگر به سوی مرحله بعدی به میدان می‌روند.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137001" target="_blank">📅 20:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137000">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc30274f9.mp4?token=UKojlm8spPO2IOfzhT8tfNJD0hA4l6myRgXB1cBc69w7k2r9sYQUFH0ax0Dp_3oW3RbO6ZVKr2rcFhWGnHztSVSVpK9Itb21hNgNC4DUi54I29kAjgPxg61zwpniOPxD9ZGevs4JS-s7pd8hygiZ1_L_1nHAtpmPMnPi4DlG4RWNldASY4yL4y16gw7DlDWxzwn6of0dD-bjGDcOdfvc0AoUOJMN23qHyJ69LpP0Leqqlxvej9XaVrQcYuoOY-qMWhlzBnR5pwLrKUI6rl82XYd0ysGdSV-JuLKncWwjfGLGiRhQjJh6th6f7D_eWbgGWybTq_CeT9GyP1oA7J-ZUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc30274f9.mp4?token=UKojlm8spPO2IOfzhT8tfNJD0hA4l6myRgXB1cBc69w7k2r9sYQUFH0ax0Dp_3oW3RbO6ZVKr2rcFhWGnHztSVSVpK9Itb21hNgNC4DUi54I29kAjgPxg61zwpniOPxD9ZGevs4JS-s7pd8hygiZ1_L_1nHAtpmPMnPi4DlG4RWNldASY4yL4y16gw7DlDWxzwn6of0dD-bjGDcOdfvc0AoUOJMN23qHyJ69LpP0Leqqlxvej9XaVrQcYuoOY-qMWhlzBnR5pwLrKUI6rl82XYd0ysGdSV-JuLKncWwjfGLGiRhQjJh6th6f7D_eWbgGWybTq_CeT9GyP1oA7J-ZUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
امین کاظمیان در حالی اولین بازی خود با پیراهن گل‌گهر را تجربه می‌کند که شماره ۱۰ گل‌گهر را بر تن کرده که نام تیکدری بر پشت پیراهن اوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137000" target="_blank">📅 20:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136999">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⬇
⬇
بازگشت جنگ اعصاب به فوتبال
🔴
فوری - جواد نکونام به لیگ برتر برگشت
🤝
جواد نکونام پس از ساعت‌های طولانی مذاکره با باشگاه پیکان، به توافق نهایی با خودروسازان رسید تا پس از یک وقفه، دوباره به لیگ برتر برگردد و هدایت این تیم را برعهده بگیرد.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136999" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136998">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2G5gWYdwp2orjf7ziaxXj7fHm0tWOYiz6EN2QHvL_lTDSNVcu7O8QuO_hvVvGmbCZubc3efNqSIaQq8OfKSnLU_lAbCkN3DtMdN2VEkaFmb_Ce9wvyPsjbxdWWbdZF2IMF5hTPkI73YZVNCFIEIMAiYPQpxeEAt_vb5urE__wEYdoHND5BC8jYQq03hPzaTk01Z9OBoSEuAEEGzUh9JJKpq-DFI-OZIxEbcHPp62A7x5Jy45PipRJaQ6-uNnvW7QMdjAdjpSTqJ1I7oYek4bnz3Xxt33XcCAFlR-sb-7zWaq0-UaUJgypRd6rJlqNAsrxtcw9Uy96Bmmu_0UpcoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
در عربستان پول پارو کرد!
🇸🇦
کریستیانو رونالدو از زمان پیوستن به تیم النصر، مبلغ شگفت‌انگیز 625 میلیون یورو به عنوان حقوق و پاداش کسب کرده است.
😇
فوق ستاره پرتغالی در کمتر از چهار سال، ثروتی بی‌سابقه به دست آورده و او را به فوتبالیستی تبدیل کرد که بیشترین میزان درآمد را از قراردادهای خود در تاریخ این ورزش داشته است.
🟡
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
🟡
پاداش برای ۱۲۹ گل: ۱۱ میلیون یورو
🟡
پاداش برای ۲۳ پاس گل: ۱ میلیون یورو
🟡
دو جایزه بهترین گلزن لیگ: ۸.۵ میلیون یورو
🟡
پاداش قهرمانی در لیگ: ۸.۵ میلیون یورو
⚡️
مجموع درآمد: تقریباً ۶۲۵ میلیون یورو
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136998" target="_blank">📅 19:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136997">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4qax3dXtqWy_TDF6BmA8NRSIoF8IPDqkNA2jqeSEOOZtn3oXk0RwqoOw6H9_zZv0fyNm_S9_YEpjU3CkUwmGmfPZoBA7_YaQTX7YcYWrfRYP0wcQTZJEGAVGhFIt7zNPUsWgh75Ka2-09SJOZyscH59H51T9TcA2H6hcV7fwJBRf015c77yYUrSgkN8awth1qwn63A0LUqeXY9_7GJ8PpbbjKN8C_HxNtIT0l-KJ-sQo08F64QMis6X0WwwmmF08XkXye6rWW86A1BQD-_VR9qxMYllwTHuGiy4WFqkrsUeHStRwoMmTPrCe6Yqg1lD9gWd6pnV8-LWTxzMw9axRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👤
ممد مهتی امشب به اردوی پرسپولیس اضافه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136997" target="_blank">📅 19:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136996">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌀
🌀
تارتار تو پست های دروازبان، دفاع راست ، دفاع چپ و دفاع وسط بازیکن میخواد/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136996" target="_blank">📅 18:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136995">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚡️
تارتار: حداقل به 4 خرید دیگر لازم داریم (دفاع چپ،دفاع میانی،گلر و مهاجم ) بازیکن می‌خوایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136995" target="_blank">📅 18:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136994">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
میرشاد ماجدی، رئیس هیئت فوتبال تهران:
◻️
مسئولیت استادیوم‌های تهران با من نیست. ورزشگاه‌های دستگردی و شهرقدس برای لیگ آماده هستند، اما درباره آزادی هنوز تصمیمی اعلام نشده است. زمان شروع مسابقات مشخص نیست و به وضعیت جنگ بستگی دارد.برگزاری منظم مسابقات،…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/136994" target="_blank">📅 18:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136993">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136993" target="_blank">📅 18:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136992">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚡️
⚡️
فوری/ دونالد ترامپ: در پاسخ به حملاتی که سپاه پاسداران به اردن کرده، ما ایران را به شدت مورد حمله قرار خواهیم داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136992" target="_blank">📅 16:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136991">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚡️
ترامپ: اگر توافق نشود، پل‌ها را ظرف دو ساعت و نیروگاه‌ها را در یک روز از بین می‌برم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136991" target="_blank">📅 15:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136990">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
گل های محمدمهدی محبی خرید و ستاره جدید پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/136990" target="_blank">📅 15:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136988">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
🔴
🔴
باشگاه پرسپولیس با مبلغ ۵۰ میلیارد با وحید امیری تمدید کرده و حالا با توجه به جدایی و بدون اینکه بازی کنه، ۲۸ میلیارد میگیره و توافق می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136988" target="_blank">📅 15:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136987">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136987" target="_blank">📅 15:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136986">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136986" target="_blank">📅 15:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136985">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
🔴
🔴
🔴
توجه به پیوستن محمدرضا اخباری، احتمال بازگشت امیر رفیعی قوت گرفته است. برخلاف اخبار منتشره، باشگاه پرسپولیس، با احمد گوهری و سایر دروازه بان هایی که نام آن ها مطرح است مذاکره ای نداشته
🔴
رفیعی به مدیران پرسپولیس اعلام کرد توافقی جدا شود و باشگاه به او…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136985" target="_blank">📅 15:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136984">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136984" target="_blank">📅 15:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136983">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💠
💠
💠
✅
پرونده ایری و طاهری به حدی جنجالی و پرحاشیه شده که مدیران پرسپولیس فعلا هیچ رغبتی به توضیح ندارند
🌀
🌀
عصبانیت هواداران هم مزید بر علت شده تا برخی از مدیران ترجیح دهند اظهارنظری نداشته باشند.
🌀
🌀
وضعیت به گونه ای است که حتی جذب محبی هم موجب ارامش هواداران…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136983" target="_blank">📅 14:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136982">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
امیر روستایی مهاجم سابق پرسپولیس به سترة بحرین پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136982" target="_blank">📅 14:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136981">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
شهاب زندی مدیرعامل نساجی:  با استقلال درحال مذاکره‌ایم، با توجه به بسته بودن پنجره شون اگه بر سر مباحث مالی به توافق برسیم این دو بازیکن آینده‌دار نیم‌فصل راهی استقلال میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136981" target="_blank">📅 14:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136980">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oovRSBaCE6fQqCjpkyTCrDWWOmzm-s7iXLCyRPb1Xh6WEXIqhW8vB_TZBbZ0m4h4BHU40RILoemrc_3F0UMvlKpWB2wtrD-gcLnmuFEgHhKhwMJZQnRsmZJtDptJ9Cwy4BPhnOsQQGrv4OL8fv-FRGRIX72aqVBYodOjznPF0lx937re46qH336sosma_y-JaQC3jHXjkjZ4eglDQ0mgYRH8mDoO5rbnWGhbTyoGp-Gu5sWmoRrzQK3fx-nTs4_q1v4xuD7EEW8iv0pnGZ-NORsfO6RdgqF7OLxyz9kcNP4K3OLp8gZyTAbyW2ep2zCEv5aEKyeKnoOOx1tzGfzH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی لیگ ملت‌های والیبال از راه رسید!
🔴
نبردی حساس و تماشایی بین ترکیه و اسلوونی در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با وینکوبت، چهارشنبه ساعت ۱۰:۳۰ دوتیم ترکیه
🇹🇷
-
🇸🇮
اسلوونی به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی بازی‌های لیگ‌ملت‌های والیبال با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/136980" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136979">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
علی بازگشا، سخنگوی باشگاه پرسپولیس: «اینکه پیشنهادی آمده بی‌اطلاعم، اما ما می‌خواهیم اورونوف و سرگیف را حفظ کنیم.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136979" target="_blank">📅 11:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136978">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔄
🔄
باشگاه نساجی: دانیال ایری و کسری طاهری رو دیگر به پرسپولیس نمیدیم. بانک شهر ما رو سرکار گذاشت. اگه با استقلال توافق کنیم اونارو به استقلال میفروشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136978" target="_blank">📅 11:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136977">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
✅
کسری طاهری رسما توسط نساجی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136977" target="_blank">📅 11:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136976">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">💢
💢
قرعه نه سخت نه آسون گیرمون اومده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/136976" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136975">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💠
💠
💠
تارتار دوست دارد در ابتدای شخصیت گل نخوردن را به تیمش منتقل کند که حریفان به راحتی دروازه تیمش را باز نکنند.
⚠️
⚠️
تارتار در مسابقات مختلف خطاب به شاگردانش تاکید کرده نباید به هیچ وجه گل بخورند چون وقتی تیمی گل نخورد شخصیت پیدا می کند همانطور که تیمی که…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136975" target="_blank">📅 10:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136974">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🗣
🚨
شیوخ ابوظبی اعلام کردن دیگه ایرانی‌ها جایی توی این شهر ندارن و محمد قربانی هم به این دلیل از الوحده کنار گذاشته شده / هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/136974" target="_blank">📅 10:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136973">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
خالد در آستانه بازگشت به پرسپولیس
🔴
❌
مدیران باشگاه پرسپولیس بعد از منتفی شدن حضور محمدرضا اخباری در این تیم برای تقویت دروازه خود به دنبال جذب محمدرضا خالدآبادی گلر سابق استقلال و فعلی شمس آذر قزوین رفته اند
🔴
خالدآبادی سابقه عضویت در آکادمی پرسپولیس را…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136973" target="_blank">📅 10:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136972">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
محمدمهدی محبی احتمالا وارث شماره ۱۰ پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136972" target="_blank">📅 09:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136971">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfptWtxNj107vTBrO7dJ8WeEjpQQTLsdh4o-gPqIoFq-CYIheksIqis04IX8lSR7RoIhgxVjihFhRFcvqgc3Ba1px0mS3EJ2v6UCvoF6RfIq-n9yaQ1FFbYQkMUE_ah5NfbDKzRdf1ZQkTEHEPO57NY5v_H5q7SNyr2_QThSJDNHh4bDr-__4TtJgCsVsjI_v08fUzRKN_A-HdSltt1v3tvEudC2V0e1mQYhk7sJiFCo1xgMXsb6lODDLW5Zecp7yhTv77nx3F2hmq6JlICW8pwP33OKabKjvkRrW0-ATCU9dWcR5q3hKO46LStJigsAv835U7VxD0OYrm8hiS_07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خبرنگار ورزش سه حاضر در تمرینات تیم در ترکیه: اسکواد سرخپوشان همچنان ناقص است و احساس نیاز در پستهای دفاع مرکزی، دفاع راست، دفاع چپ، هافبک بازیساز، مهاجم و البته دروازه‌بان ذخیره احساس می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136971" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136970">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✖️
✅
سه گزینه نهایی مهدی تارتار برای جذب هافبک بازیساز مشخص شدند:
🔄
⏺
1_ فرهان جعفری از ملوان
🔻
2_ مهدی گودرزی از خیبر
🔻
3_ مهدی نجفی از پیکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136970" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136969">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✖️
✅
سه گزینه نهایی مهدی تارتار برای جذب هافبک بازیساز مشخص شدند:
🔄
⏺
1_ فرهان جعفری از ملوان
🔻
2_ مهدی گودرزی از خیبر
🔻
3_ مهدی نجفی از پیکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136969" target="_blank">📅 09:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136968">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🗣
🚨
شیوخ ابوظبی اعلام کردن دیگه ایرانی‌ها جایی توی این شهر ندارن و محمد قربانی هم به این دلیل از الوحده کنار گذاشته شده / هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136968" target="_blank">📅 08:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136967">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIsDz090ZxJn8dtLg-lcnLM78xSDs6Lx3tNZbftnAbpB_o58P0ykjnN7LsbpUIQO098EYy9BAm2zvctkkPbpbY-spe2qjvzuH9bD0qgcwYdFGfcOG-8gSoxOGrjyORwGGWtUFpKrqCF5lPbZOiA7tDjat07b_QWsj-ZUw3P1XX1E7fdEiM5rDT6V6edu0OgMw0gRsspOFFE1qTvLxWyzrqowYMNZZH6k7dz2OktbPjGT1bHxk7qenWG__ET284BfmC7fA2tqhAQ4kY0f0bG2aP7YOlrZ7CCy0T_ONLUB_aKwhCDydVqn6y6bo7fb6ReyjiVgDOMieu-XkrOwJjDf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136967" target="_blank">📅 08:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136966">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBurtmWz0pJzP2etxcfPTdiFRGt2K72OHmIpDszCXgRx2rQ4MQ5-U53m_NvoFljx69W0-jcQZCIrg6zixGJ_NB2xpCYBVuW3rU1jCLb-s0U2pSRSPzyubbiB9lPg8R5WwJtiWI6X8TPr0ZDLWfxFXOYrTbwilVBkpSMeKG2YsvCZ6v8OCN8OHBxzwVmJSGG2RXCZmAL2pt6DlY-MI6f_Dlt3mYLjbvJ-dhEfGwDLr4hXxmsrAYoqrV4sI-vRiQv1PyqNB6edJJKY_DqENbwm0DNgiVKLKbbxXf91a8X8F8sYfxjm968c5S8quAbzThf4N70NJDGlcQnxJ-pZFF4Uug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی لیگ ملت‌های والیبال از راه رسید!
🔴
نبردی حساس و تماشایی بین ترکیه و اسلوونی در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با وینکوبت، چهارشنبه ساعت ۱۰:۳۰ دوتیم ترکیه
🇹🇷
-
🇸🇮
اسلوونی به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی بازی‌های لیگ‌ملت‌های والیبال با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/136966" target="_blank">📅 01:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136965">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⚡️
⚡️
قرارداد دنیل گرا با پرسپولیس ۶۵۰ هزار دلار است و این بازیکن اعلام کرده تنها در شرایطی حاضر به فسخ قرارداد خواهد شد که کل مبلغ قرارداد فصل آینده‌اش را بگیرد. گرا در مدت زمان حضور کوتاهش در پرسپولیس به اندازه‌ای ضعیف ظاهر شده که نه تنها باشگاه‌های لیگ برتری،…</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136965" target="_blank">📅 00:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136964">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⚡️
⚡️
فوووووووووری
⏺
باشگاه خیبر خرم آباد رضایت نامه مهدی گودرزی رو 70 میلیارد تومن اعلام کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136964" target="_blank">📅 00:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136963">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⚡️
⚡️
شنیده ها: با درخواست مهدی تارتار؛ باشگاه پرسپولیس فردا برای جذب مهدی گودرزی اقدام خواهد کرد
🔹
پ.ن: گویا خیبر هم مشکلی با جدایی گودرزی نداره و به دنبال درامدزایی ازشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136963" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136962">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚡️
فوری از مهر
🔻
برخی از دلال سعی در فرو کردن قربانی به پرسپولیس دارن ولی تارتار گفته من چهار تا هافبک دفاعی دارم و نیاز به این بازیکن ندارم
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/136962" target="_blank">📅 00:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136961">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
شنیده ها :معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن باقی مونده.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/136961" target="_blank">📅 00:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136960">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌀
🌀
🌀
اظهارات کنایه‌آمیز محسن خلیلی: تیم‌های دیگر هم دلسوز بازیکن گرفتن پرسپولیس هستن. برای جذب هر بازیکن تیم حقوقی ما بررسی می‌کنه تا محروم نشیم.
📎
📎
📎
خبرهای خوبی درباره انتقال یک بازیکن می‌رسه.
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/136960" target="_blank">📅 00:27 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
