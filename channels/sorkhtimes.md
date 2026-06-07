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
<img src="https://cdn4.telesco.pe/file/SV-X8qIEAhCrTii2W2xyXwK5q9buMEONZifqd3Y2RFsMyEtMQyS_nqAkmAULgEJfchOSINOtIxXqXl9Esij153xnEfP8DKKipNFiEL7V0dl42pdTM8N_7N3UUNK0MRXqF8HZImQv7xd9kN1W4E0nR_jrm3_USHNNX2Y1G1r5Gjxms0gTYJ6jlfeInGe5Mb4WqpoSYElNSJZJ1J9XWwdUzPl2LX5WHNqusxiLX5iTuTjsFAcLZqh_Z-Nbjw-V8drurRMysr6mkJZQ-0q070DId3KFjw68dJukJ8FbcRepvRkhTrNTlB0f8YuyI9oo_28nsJNMoJey8Lb4n1A-I-tj2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 08:32:57</div>
<hr>

<div class="tg-post" id="msg-132904">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd44R0LUMihFCzH9FCR7KsqgrBbO1uJAiMZ1JyL75_nllZLATqY6JiY0EjZZVvXbY_807dzQa5TJpC1x7eNoIUkZBBlOiK8Nf_U56gIhv7a76Ki80KTqzdXtN5qFaa5hRB-smPtBbOYaZ4mcTkdHSifPdDDsy7bSGTqVl0_zkBkJuQW_67tIqtc5xjjh_fP8WQEEuQMkQnvXWt1X0QNAw2BogZ3frY9-juETWBp7B-Sru_V__tBwzC2EYhdvamuQ44FaTF41gX1yWr5BiZH9qp3OEMUXsrHyRLClaKX7tG2aqnQanHobwAD6Sja1Ens9MPLN4t0ok_oNrMpWtELS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/SorkhTimes/132904" target="_blank">📅 01:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132903">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OesdnI4fb9XqVMiGCscSWMCNZ7AGBRzfIkx_S5kumsoayCh5zQdT5AhvWq3W7hptLJFO8c0vA1Lbb3u5pr_M-fCSTqiaWTySSZre1DSsk46x62ORmQ4c0t1Q2F4KEbC6CTpIAzfKg0BioyLBso1NEWq72puq5vVKZMC7PM5hIO4-y4ovuegisCrUGP0-C25xugtYLn571TJd0uNCFJMsIOfFcN0W-FtxSKcINjbUUdbzTwtfNGH0t1Vx9GCqlDVh2On3srXEc2pBzfx32z6CzE5BE9qeEYorPT5ZmT8GpiXkMqK3XjD-4IgPH-BP_txmiGjP_Fsw3RK7lJ5HqGViGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
PulseGate | اتصال بدون مرز
🔥
اینترنت مخصوص نت ملی
⚡
سرعت بالا
🎮
پینگ پایین
🛡
امنیت بالا
📱
سازگار با همه دستگاه‌ها
♾
کاربر نامحدود
💰
پلن‌های اقتصادی از 250 هزار تومان
📩
ثبت سفارش و پشتیبانی:
@PulseGatee
⏳
ظرفیت برخی سرورها محدود است؛ برای فعال‌سازی سریع‌تر پیام بده</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/132903" target="_blank">📅 01:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132902">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🏆
موزیک ویدیو رسمی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/132902" target="_blank">📅 00:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132901">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mITg_veiwYQJ-pSpMj1kNNW6_YdhooX-cpoEaQCeGSYMbH56YcAYE5iJg8htAp9qB1cU-HakWGHPds_gIo4nps_C8I4iHTzk3T71W-K0baGLfyWCng-ca_WFPoD0vQp6pOdOhFOM-mEtd2vEXWV-uWVwk4z_oVf5XxgJXlBbgJtkt8tGhXKS66ZzOXMIgiSZh2VOaU2eKry1hdXl64I3LTQTEOVreWL8RrzLjU8Qm_jBMyb51Bx1PWnjhZQrJoS1JmuI5YjvM165Bfk8tV3WP_SgQoPUlMHeUDeJm8rCR8hQcDDG_bTG7TFW6gHjQ9xWuV6TMPZmae11FI4bGQRm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اسفندیارپور، مدیرعامل گل‌گهر: «تورنمنت ۳ جانبه من‌درآوردی است و در آن شرکت نمی‌کنیم.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SorkhTimes/132901" target="_blank">📅 00:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132900">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
🔴
برگشتن سروش رفیعی به پرسپولیس خیلی محتمل نیست. او با چند تیم کانادایی مذاکره کرده، ولی هنوز به توافق نرسیده. اگر مشکل‌هایش حل شود، فصل بعد در ایران بازی می‌کند و دوست دارد فوتبالش را در پرسپولیس به پایان برساند.
✍
خبرگزاری فوتبالی
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/132900" target="_blank">📅 00:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132898">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S_me0XKKebEAMfcQaWvcTsa6xwmXDwvWSgVWWENBqv62EEUAPS0_bEzJ2cxbGewmJHEfepLvQFtpzCdAkBO9z8JvSJfmn1qH0ux4Z5wRx2aJmpJU9lQUDsPEISPTf7SYsAZnGU0e4_7FaYsA8AB7eS9LnZwYxHZhewyP8dCzHFtEILZI7i3zqT0cMBAmgIprrtGtK7iZinFTPMC94AM14IvWgosstBFCcXi3FOQKJTsdA3rgaEKL_uB_6Zw0N13fonaJrkpKd8FlpeF8eWQ0CPQQbqholUFyIALGmVLuViV3oS8B2nPHeEvDx0PBZxfEg0fF68v5igpMR5ymnIDNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فدراسیون فوتبال عراق به دلیل همزمانی بازی‌اش با سنگال در جام جهانی با شب شهادت امام حسین(ع)، از فیفا درخواست کرد مجوز پوشیدن پیراهن مشکی را برای این مسابقه صادر کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SorkhTimes/132898" target="_blank">📅 00:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132897">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
قدوسی: اوسمار احتمالاً چهارشنبه یا اواخر هفته به تهران برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SorkhTimes/132897" target="_blank">📅 00:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132896">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
🔴
امید عالیشاه، علی علیپور و میلاد محمدی شانس بسیار خوبی برای تمدید قرارداد با پرسپولیس دارند
✍
خبرگزاری فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/132896" target="_blank">📅 23:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132895">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
🔴
امید عالیشاه، علی علیپور و میلاد محمدی شانس بسیار خوبی برای تمدید قرارداد با پرسپولیس دارند
✍
خبرگزاری فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/132895" target="_blank">📅 23:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132894">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
🚨
#شنیده‌ها
💵
پیشنهاد مالی جدید علیپور به پرسپولیس برای تمدید قرارداد: ۲۵۰ میلیارد برای ۲ فصل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/132894" target="_blank">📅 23:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132892">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
همه تیم در جام جهانی هستند تو این دو تاریخ  ..و باید بگردیم یازده نفر و پیدا کنیم و بتوانیم این دو باری سخت و بگذرونیم و جواز رفتن به سطح دو آسیا رو کسب کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/132892" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132891">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
🖍
غایبان احتمالی پرسپولیس در صورت برگزاری تورنمنت سه جانبه برای کسب سهمیه سطح دو آسیا
▪️
ارونوف
▪️
سرگیف
▪️
علیپور
▪️
کنعانی
▪️
محمودی
▪️
سروش رفیعی
▪️
میلاد محمدی
▪️
پیام نیازمند
▪️
دنیل گرا
▪️
تیوی بیفوما
▪️
مارکو باکیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/132891" target="_blank">📅 22:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132889">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
مسئولان پرسپولیس به اوسمار ویرا، مربیان خارجی و بازیکنان خارجی تیم پیام داده‌اند که هرچه زودتر بگویند چه زمانی به ایران برمی‌گردند و برنامه برگشت‌شان را مشخص کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/132889" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132888">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
در صورت برگزاری مسابقه، این دو دیدار در تاریخ 5 و 9 تیر برگزار خواهد شد.و بدون تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132888" target="_blank">📅 22:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132887">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
‼️
مجتبی فخریان، وینگر پرسپولیس که به صورت قرضی در ملوان بازی می‌کند، قصدی برای بازگشت به پرسپولیس ندارد و به صورت دائمی جدا می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/132887" target="_blank">📅 21:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132885">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
مسئولان پرسپولیس به اوسمار ویرا، مربیان خارجی و بازیکنان خارجی تیم پیام داده‌اند که هرچه زودتر بگویند چه زمانی به ایران برمی‌گردند و برنامه برگشت‌شان را مشخص کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132885" target="_blank">📅 20:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132883">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
از عصر دوشنبه تمرینات پرسپولیس شروع میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132883" target="_blank">📅 20:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132882">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
در صورت برگزاری مسابقه، این دو دیدار در تاریخ 5 و 9 تیر برگزار خواهد شد.و بدون تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132882" target="_blank">📅 20:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132881">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
کسری طاهری تا سال 2028 با روبین کازان قرارداد داره و الان قرضی توی پیکان بازی میکنه، هر تیمی بخوادش باید با کازان مذاکره کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132881" target="_blank">📅 19:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132880">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#منهای‌پرسپولیس
🚨
کسری طاهری مهاجم تیم پیکان تهران با پایان قرارداد قرضی اش با پیکان به روبین کازان روسیه پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132880" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132879">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#منهای‌پرسپولیس
🚨
کسری طاهری مهاجم تیم پیکان تهران با پایان قرارداد قرضی اش با پیکان به روبین کازان روسیه پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132879" target="_blank">📅 19:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132878">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcce26bb71.mp4?token=ntTYTl3LSqgsLxNuLP7PTc_Vp2cYk7dQcsxmRbb6lV54vSvuQE5gyPm6Yuk7pxU4HIEEBGPpC8EakRjIB2VVlSip1-j-O0nV6Y3a6KAlgAk7vn5Tsqb8ACWM7SFpABP1STuwoXb7NVhDNxOnwIqVx8ojESEbSx4zBCex4OTrDLlN_2jeOz64yKGYM7f-lStZ--IQokszcNWRc7qBFu3J-sa4AyZePT_kzLC_rC1LodBOtmbgpso8lGNywV-rT2-NugZ9p1ckgxTfTMp-F97Yxyovp0tL_Qmo8JbvaoaE0_5M1HFz04zaCMA-xHKmOmOOiBb_wJyYKDAxFHVHnP2G_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcce26bb71.mp4?token=ntTYTl3LSqgsLxNuLP7PTc_Vp2cYk7dQcsxmRbb6lV54vSvuQE5gyPm6Yuk7pxU4HIEEBGPpC8EakRjIB2VVlSip1-j-O0nV6Y3a6KAlgAk7vn5Tsqb8ACWM7SFpABP1STuwoXb7NVhDNxOnwIqVx8ojESEbSx4zBCex4OTrDLlN_2jeOz64yKGYM7f-lStZ--IQokszcNWRc7qBFu3J-sa4AyZePT_kzLC_rC1LodBOtmbgpso8lGNywV-rT2-NugZ9p1ckgxTfTMp-F97Yxyovp0tL_Qmo8JbvaoaE0_5M1HFz04zaCMA-xHKmOmOOiBb_wJyYKDAxFHVHnP2G_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
حضور علیرضا عنایت‌زاده هافبک جوان سرخپوشان مقابل فدراسیون فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/132878" target="_blank">📅 18:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132877">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTGC6mC-6scblIIIqK6UOxxWJGt4wZDHWVoCNEpZF0FK6wPPeocNKytWeEK1flxW-LtQdJy7lWRHvQ8uE5lS1UhC0z9zxsqwh8mpIDT4e8p9U7Cf6vHpJBKXtvCHJoCKDPYYlThMr76B79MnZlWY5rcaEmBNQCTGc8QYZHdfag7SSbAWydvd0MhrM-qV1o0nWV26-m7WH9IozoZR9dxvFc69he7HzZ-7oTnWMWe3jQMv2UDJzyAFibIF1VbDpnOBgZp2COaHNkU49YaQg2aYvtkb4tHElNdacVkA-U_5fUKCQJxULTtWv5O52gH3y6hqz0ki1x7WUbI4sjs1lbaeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132877" target="_blank">📅 18:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132875">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/132875" target="_blank">📅 17:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132874">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
جنپو با گاوداری قراردادش رو فسخ میده و طویله گاوداری باید چیزی حدود 4 میلیون دلار به این سوپراستار غرامت بده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132874" target="_blank">📅 16:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132873">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132873" target="_blank">📅 16:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132872">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132872" target="_blank">📅 16:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132871">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
پایان دعوای سهمیه سوم؟
🔸
امروز جلسه‌ای برای تعیین‌تکلیف نماینده سوم ایران در فصل جدید مسابقات آسیایی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/132871" target="_blank">📅 16:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132869">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
باشگاه پرسپولیس پیگیر پرونده سینا خادم پور و دریافت 2 امتیاز به علت غیر مجاز بازی کردن این بازیکن می باشد
❌
یا در غیر این صورت کسر شدن امتیاز این بازیکن که به استقلال و تراکتور داده شده
3⃣
احتمال تورنومنت 3 جانبه وجود دارد و طی جلساتی سهمیه سوم آسیایی…</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/132869" target="_blank">📅 16:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132868">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGIrZt5iwRP5fhVDpg_vHwTGMkRpx_CdZugsQP_q7zDOI5p2-CMhml8kAAaX-PkKJcV_Dbhv5Hv1k3qowxkwQf5lVDu87xrUle4oTpqhcVc-lc16k6bTJaold20V2Rsrnye1EaYWpapCQB5k_urhOHBVdnT4028oDjY-UWNHhUT2bIJW3sui7-SHUDUZm1mDB2O5J1Q0zGs39--IihHdLDmgqqnNc7MW44uqAEnX0K8CggF5bQ5eeaHi8MYMeClhYuRDN4347miHPlaYfhKRLuYbldtXFXv5qOZMlN_GblTebRsFmQ0qcxFn8i6hUHju2MXD4a_9iPw3rPfITk5woQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
۸ جفت برادر تو جام جهانی ۲۰۲۶ حضور دارن:
- گیلا دوئه (ساحل عاج) و دزیره دوئه (فرانسه)
- اینیاکی ویلیامز (غنا) و نیکو ویلیامز (اسپانیا)
- دریک برابی (غنا) و برایان برابی (هلند)
- جان سوتار (اسکاتلند) و هری سوتار (استرالیا)
- لوکاس هرناندز و تئو هرناندز (فرانسه)
- کوئنتین تیمبر و یورین تیمبر (هلند)
- لاروس دوارته و دروی دوارته (کیپ ورد)
- لئاندرو باکونا و جونینیو باکونا (کوراسائو)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132868" target="_blank">📅 16:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132867">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
چه پولای خرج کرده اقای پ.ج
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/132867" target="_blank">📅 15:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132866">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
چه پولای خرج کرده اقای پ.ج
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/132866" target="_blank">📅 15:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132865">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
محمودی همراه با تیم ملی به آمریکا میره و اگه کسی مصدوم بشه جایگزینش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132865" target="_blank">📅 15:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132864">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
با رفتن سروش رفیعی شرایط تغییر نمیکنه امید عالیشا هم باید بره…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/132864" target="_blank">📅 15:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132863">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
بازیکنانی که به صورت قرضی یا حتی دائمی احتمالا از پرسپولیس جدا خواهند شد:
❤️
امیررضا رفیعی
❤️
محمدحسین صادقی
❤️
سهیل صحرایی
❤️
مجتبی فخریان
❤️
ابوالفضل بابایی
❤️
علیرضا عنایت‌زاده
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/132863" target="_blank">📅 15:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132862">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
❗️
پل پرسپولیس برای صعود به آسیا
🔴
باشگاه پرسپولیس در روزهای اخیر پیگیری‌های خود را برای رسیدگی به پرونده دیدار این تیم مقابل ملوان افزایش داده و امیدوار است با استناد به موضوع استفاده از سینا خادم‌پور، بتواند ۳ امتیاز این مسابقه را به دست آورد.
🔴
برخی منابع…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132862" target="_blank">📅 15:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132861">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c98a8b0a5.mp4?token=E5Pmu-PtqI1JxeshtOQHA3T97v5nVexLvI3OZOrffDDz3sj-Nu0a-IhhmMrEsPO4ijAsYVnaitNkA300PqOktua7ulimKnJLQM0_75LfXosMdPh0jur1u7nvKFBBlHQVB60cVgr7pI3ekZ_1OeWHNTMXwzG7xropOMOwtWrXI1b4hFcK2AwVCqU-Lmwwz1eakJLrF5NNT_Hfy_UbBUtEgAhMF26Zzrh339uOmZ4Rza5NpCfT8F3zukMmAXSMaSJ4xT_2qKZRH10Ukb53xgJRQVb8ZxQz1sL-jQJFkzjKbaOPK3ZYlEXPqSkA2FIN9uYdfq2Jo2T0skSc-5PDIvtv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c98a8b0a5.mp4?token=E5Pmu-PtqI1JxeshtOQHA3T97v5nVexLvI3OZOrffDDz3sj-Nu0a-IhhmMrEsPO4ijAsYVnaitNkA300PqOktua7ulimKnJLQM0_75LfXosMdPh0jur1u7nvKFBBlHQVB60cVgr7pI3ekZ_1OeWHNTMXwzG7xropOMOwtWrXI1b4hFcK2AwVCqU-Lmwwz1eakJLrF5NNT_Hfy_UbBUtEgAhMF26Zzrh339uOmZ4Rza5NpCfT8F3zukMmAXSMaSJ4xT_2qKZRH10Ukb53xgJRQVb8ZxQz1sL-jQJFkzjKbaOPK3ZYlEXPqSkA2FIN9uYdfq2Jo2T0skSc-5PDIvtv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جنپو با گاوداری قراردادش رو فسخ میده و طویله گاوداری باید چیزی حدود 4 میلیون دلار به این سوپراستار غرامت بده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/132861" target="_blank">📅 15:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132860">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">💢
با حضور در لیست تیم ملی، میلاد محمدی سومین تجربه حضور در جام جهانی را خواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/132860" target="_blank">📅 15:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132859">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
اوسمار ویرا به مدیران پرسپولیس اعلام کرده است که به پتانسیل رهبری امید عالیشاه برای فصل آتی در پرسپولیس نیاز دارد و این بازیکن حتما باید به مدت حداقل یک فصل دیگر در پرسپولیس حفظ شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/132859" target="_blank">📅 15:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132858">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
بازیکنانی که به صورت قرضی یا حتی دائمی احتمالا از پرسپولیس جدا خواهند شد:
❤️
امیررضا رفیعی
❤️
محمدحسین صادقی
❤️
سهیل صحرایی
❤️
مجتبی فخریان
❤️
ابوالفضل بابایی
❤️
علیرضا عنایت‌زاده
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132858" target="_blank">📅 14:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132856">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
واکنش تاج به ناامن بودن شهر تیخوانا: کاری به مواد فروش‌های مکزیک نداریم و نمی‌خواهیم هم اصلاحشان کنیم!
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/132856" target="_blank">📅 13:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132855">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚡️
⚡️
۴ بازیکن استقلال از حضور در تمرین منع شدند
⚡️
⚡️
عارف غلامی، ابوالفضل جلالی، آرمین سهرابیان و موسی جنپو با تصمیم سهراب بختیاری‌زاده سرمربی استقلال از حضور در تمرین آبی‌پوشان منع شدند.
⚡️
⚡️
آن طور که پیگیری ایسنا نشان می‌دهد، دلیل کنار گذاشتن غلامی و جلالی…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132855" target="_blank">📅 13:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132854">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
👈
تهدید جدی تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132854" target="_blank">📅 13:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132853">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
پرسپولیس نمی تواند نسبت به رای بازی گل گهر و چادر ملو به cas اعتراض کند چون فقط دو طرف دعوی همان پرونده حق اعتراض دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132853" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132851">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
محمد مهدی نبی مدیر تیم ملی، هدایت ممبینی دبیرکل فدراسیون ، مهدی خراطی مدیر اجرایی تیم ملی، سیامک قلیچ خانی مدیر رسانه ای ، محسن معتمدی‌کیا مدیر روابط عمومی و یکی از آنالیزور های کادرفنی به همراه افسران أمنیتی تیم ملی موفق به دریافت ویزای…</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132851" target="_blank">📅 11:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132850">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
👈
خبرگزاری فارس : آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/132850" target="_blank">📅 11:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132849">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f698e5343a.mp4?token=VjKQ-YE1retLC9LOSHmy_rc6Fyl4rENld87uX3mik_ds5-FPsvIwPaADJ9ZRbn1XPovHHYcjPrTPyfnrnLWGuvnojLUolNdKDDs6OmAcSwPTJy_hLBZv45NCoi_GwT6Z7YFuNz_wW2BltfYzBfg2vul7tEb_6-1yOM_GE0kdel3UU9CUhHc0pmQuytMUj6MsS5l9WU46TJPzTTcPUTAyko6gTUKHvIIdxwvRnP6MgmDtEkoJF_DjAsHcqJ5Kdp5EzaYJdsyIiQObOUFzVM96iJuWpiR2dWTgRjUFRMeTuARzZxEhxtFjJmryox2fKx4dBiYMLS65u1-s1hPRTabmsasVlqxXbJPvvCHNT0cxovGyRqNz59FYytnddwoeMPJbnWMRMVyYbjxwAV1D6NPo9ry0MdViyNMCH5aMeYBgYRyn65GJub7L_YSlkTt61Q005rNXshjkzKYuuhWhoo1HjmmbTY-v6A3FP6YAMRW5cTvhq9Gao1oK-ABRFVUUbQL1WmifJNy05TMBooJnVivXTRFsyv8vvlyFMfUBqtzMiVDveWkWXp0XOu9Y00KR-LsrAmsr28-OIovwovY5cNymdYpMHXjT3AsuqIMGOH8hjfXh0aEwt3rw75aPFsasMKBiIe0msIZUN_crrMeAX9Dz5laprOqJCyCUfot7pJJo84M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f698e5343a.mp4?token=VjKQ-YE1retLC9LOSHmy_rc6Fyl4rENld87uX3mik_ds5-FPsvIwPaADJ9ZRbn1XPovHHYcjPrTPyfnrnLWGuvnojLUolNdKDDs6OmAcSwPTJy_hLBZv45NCoi_GwT6Z7YFuNz_wW2BltfYzBfg2vul7tEb_6-1yOM_GE0kdel3UU9CUhHc0pmQuytMUj6MsS5l9WU46TJPzTTcPUTAyko6gTUKHvIIdxwvRnP6MgmDtEkoJF_DjAsHcqJ5Kdp5EzaYJdsyIiQObOUFzVM96iJuWpiR2dWTgRjUFRMeTuARzZxEhxtFjJmryox2fKx4dBiYMLS65u1-s1hPRTabmsasVlqxXbJPvvCHNT0cxovGyRqNz59FYytnddwoeMPJbnWMRMVyYbjxwAV1D6NPo9ry0MdViyNMCH5aMeYBgYRyn65GJub7L_YSlkTt61Q005rNXshjkzKYuuhWhoo1HjmmbTY-v6A3FP6YAMRW5cTvhq9Gao1oK-ABRFVUUbQL1WmifJNy05TMBooJnVivXTRFsyv8vvlyFMfUBqtzMiVDveWkWXp0XOu9Y00KR-LsrAmsr28-OIovwovY5cNymdYpMHXjT3AsuqIMGOH8hjfXh0aEwt3rw75aPFsasMKBiIe0msIZUN_crrMeAX9Dz5laprOqJCyCUfot7pJJo84M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هوادار پرسپولیس: سهمیه آسیایی حق پرسپولیس است. شعار سیاسی نمی‌دهیم. طبق قوانین جمهوری اسلامی تجمع کردیم. سه ماهه درآمد نداریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132849" target="_blank">📅 11:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132848">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
استقلال با پنجره بسته خلیفه رو خرید و ما با پنجره‌ی باز همچنان اندرخم یک کوچه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/132848" target="_blank">📅 11:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132847">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqmwOfxkxLT-7WNs7qtuKqYrScAWmPI7dNfCD-rEUH18GTcf0CxpwSu9wAJmBBL0osjjxwktNCJ8gQCGlv7QiL9zlS7-VgEibJYXBVFTTtW8GUq1DqMby_cqFHLsLhsort5Iqaw1rIDK3qlgNd4XmtcwP2jR7skcbXFCYV6pIF1U-uqu2gXKnPvW0eN_07MVKBNSS2wiu30LibxXDN908dREdN1XfUBtVsGoljqTT8CnZRWAlyPueBVSn89KLjD0kGMtd5L2LDZP9oHU967U2xBt1-Zj7KVOIFlAKEkmBim5-tdAuSw-JsWUtswL2pdt7_zYgUT-NlHzFWbnFNOASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمودی همراه با تیم ملی به آمریکا میره و اگه کسی مصدوم بشه جایگزینش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132847" target="_blank">📅 11:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132846">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAGm8LJflm_vgbXb9NbIVLQzF3oA8OY8jjIYzow8xYD290NZOpSZy41ruqXWAx5WXLfwBczKHRwksSGGjWHlfy_ukhyf9f6t0foJ0UNn-sNgrxcO6hfnrv4VN1iUethFZSUJ4si-KQyFuf9PLK2ZrhgcFLcMN96Anhdlvh13Jzozl1qN90vQZsXqYhPRcAsohBEWoV3PAoByhXZIW-Cp1qyt1ECFY2FnTZ2XWjFb6U6VIRsYNrM6ZT4JOfh0GbR524h9DXQqu76ESyLDWOS9Q2vv1HQqNPlnacnQLYR44etwOtkv7pTdHcuF5gpPirGJbclSQR0A1MewsXz2ZdRaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
اوسمار ویرا به مدیران پرسپولیس اعلام کرده است که به پتانسیل رهبری امید عالیشاه برای فصل آتی در پرسپولیس نیاز دارد و این بازیکن حتما باید به مدت حداقل یک فصل دیگر در پرسپولیس حفظ شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/132846" target="_blank">📅 11:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132845">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوووری/ حدادی مدیرعامل باشگاه پرسپولیس: در صورتی که سه امتیاز بازی گل گهر و چادرملو به باشگاه گل گهر داده شود به فیفا شکایت می‌کنیم. چرا باید فدراسیون فوتبال در روز تعطیل رای صادر کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132845" target="_blank">📅 11:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132844">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=MYsd0Ra52OVxPBEnaMkLc8aQktsMDVRM-mwBA60JcGGTKbMNy1l3MKcI428RYZ9pfIHDptjMc9dxvLXXLgCdI3JcaZolPuxpoA9ybAayCLWIELTQ3QIsX3arhGV-hCwnShqIzmTAK277E7XR2WrLjX3rYJm1jeZunb8aErHimcuF0G4ciWHZNVhKrArqMDPzzijUn426GE-RfJ94hS7buFnxfAm0yNNkgwb2I_HzdSsq67yfRGrjcI81XygCYaFSdBwVGJ_X-_acqdzdh8DNU66mJpE9pFgnN695tvdrmKJ1d9fwaVgXfNkWXLndDkL1exJMYWhrqeullfhap4QGyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=MYsd0Ra52OVxPBEnaMkLc8aQktsMDVRM-mwBA60JcGGTKbMNy1l3MKcI428RYZ9pfIHDptjMc9dxvLXXLgCdI3JcaZolPuxpoA9ybAayCLWIELTQ3QIsX3arhGV-hCwnShqIzmTAK277E7XR2WrLjX3rYJm1jeZunb8aErHimcuF0G4ciWHZNVhKrArqMDPzzijUn426GE-RfJ94hS7buFnxfAm0yNNkgwb2I_HzdSsq67yfRGrjcI81XygCYaFSdBwVGJ_X-_acqdzdh8DNU66mJpE9pFgnN695tvdrmKJ1d9fwaVgXfNkWXLndDkL1exJMYWhrqeullfhap4QGyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فوری
👀
تجمع هواداران پرسپولیس مقابل فدراسیون
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132844" target="_blank">📅 11:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132843">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwQ9AFVUpo0dHuwZo4_3kx5AEUrxojUWzdqld05yylDu-SoxZ9KVVrHokswir-yP6LJD8Te-0v4ui3Gr9YdIH_dwerf0Eh7XAZZHXodELkRN6-iunz_lO0feYiNEJoHkc1eA-Yu-9BJOO83t7xCSHDnXXJ_HYLca5AMOi8OQGyhRGWNYVBmDHJ0LajUt5ApY6k3THNk6XjnN1ZANP-NJkR-BMethTW_W-0VHA-KUAQK_FpywweeIhO50HYQ6PgE6AytMYwtBw7Gly5zVwkq0AxbXOXlXrX0EfuwQQuVVnkRB7yaLuTObNbb4FB--X-JG9_kgsGquIYOAl2IQMtjGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
این یک فاجعه است!
😆
به
بازیکنان جام جهانی ایران
ویزای ورود به
ایالات متحده
اعطا شده. اما اونا شب رو در ایالات متحده نمی‌مونن. اونا در
مکزیک
مستقر میشن و سپس برای هر بازی به اونجا پرواز میکنن. یعنی اونا باید در همان روز بازی از طریق
اداره مهاجرت ایالات متحده
از مرز عبور کنن. این یک فاجعه است/ تریتا پارسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132843" target="_blank">📅 10:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132840">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
ادعای الجزیره: ١۵ نفر از تیم ملی ایران ویزا نگرفتند!
🔴
بر اساس ادعای تلویزیون الجزیره، درخواست ویزای ۱۵ نفر از اعضای تیم ملی ایران صادر نشده است. هنوز مشخص نیست که این افراد شامل کدام اعضای تیم ملی هستند اما به هر حال جزو نفرات اصلی درخواست‌کننده ویزا محسوب…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132840" target="_blank">📅 00:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132839">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIxIunE10j6u4j7H3CXafXvDf8uY-urSAOoT34s7L0dBn9TpMEBj5b5Ay0IRZ1xalnTLgzVDuItLluxrmJJyYOujUHdPlEBrlIjI9f2K3lQwbpNweDKwdzMz4apml9G6lEUUeVgnAsxsjEbSx9yes4RZefgEWHfX1H5_ED8Agrhp6Wz2OROwu_ov7lEsNI2ddhL329T4Igx2HtuZfQg81e3Fw7Wx9C4mDcDBoMnunoSfdtHWSREgT5XZ7MAADq7UCA9p0NWWgfJLbc6tjvO-UT_vlUuiBLceu_JRDtqGbUwFXuwsxcU99lglVaHqTi8coZS_3s_ur5Xqy656ukNnkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
شهریار مغانلو:
❌
می‌خوایم سه پیروزی بدست بیاریم و با ۹ امتیاز به مرحله بعد بریم
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132839" target="_blank">📅 00:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132838">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGRBXSTyrZiS4mSeXikcZFS9mXMzu0KC5Ln0s-HKoyDCI_EiNL5oilIO1LjxeLnWr5DgQjs9HN5A9Qk_vobClrD2d2pYbobwug2kXyOmLOI8Nn7nxHIkcYVvaZ5im71fxRI5rcy3iLm4_XqCg4LVfnFmOKnV8OnOiql6SC9-0lbIaJtw7f_EMQQmZmn4VSAqVZsEpIx0yWd7rIQXD3Xl3BK88ccrmH8lWByQGTojZLNRRLjHlIklxgkAnQ8drIGS8W8UgmGgWR0K1VhK4wP_RfZnD2w-JXeRcnb_-6h-34dPAAbyhbuQe_Hl7XMru7R-LSdj-vN1y4ZkYFWm-2d5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرهیختگان: پرسپولیس پیشنهاد داده که میانگین امتیازات سه فصل اخیر رو برای لیگ 2 قهرمانان آسیا در نظر بگیرند و طبق اون نماینده ایران در این تورنمنت رو مشخص کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132838" target="_blank">📅 00:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132837">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
👈
خبرگزاری فارس : آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132837" target="_blank">📅 00:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132836">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎙
🤍
مهدی طارمی:
⚪️
اتفاقات تلخی رخ داده که همه دنیا از آن آگاه هست، اما کاری که از دست ما برمیاد اینه که با بازی‌هامون لبخند رو به مردم هدیه بدیم. ورزش از سیاست جداست. ما در ورزش نشون می‌دیم مردمی صلح‌طلب و محترم هستیم و نه اون تصویری که از ما در جهان نشون داده…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/132836" target="_blank">📅 00:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132835">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a60445fb.mp4?token=sxJduj_2X4s2ttSOgpLxSAFN9Qta2uBw7oskftue0sDp4bz89VUfDlZzD_UebC3IcCeY_JEazWZs7lvakBq1L0C0XlnSyOCGfJqVBdp2N_YNcXOrmxaOkACpdouk0yzWW7laW6BC_SKeWbjvbyveT2dJPlDhuK-am1y8iwSEHek8kTi_jwfkfep0KIcUQnwLw2FeLe1rQWLMKik0xPEmlRcuAyEOpGySdc6-Ot7_KHX8SCkzHJIvEVpMIFHwGwyI-QGxJRMtYXXvZPoET2u08kzJ8xvMugGFT5VGoM7s3NnMDFuB0Bk7cA8tmMy4jxwYCGxQ_MsyqyAnq8mIsijVdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a60445fb.mp4?token=sxJduj_2X4s2ttSOgpLxSAFN9Qta2uBw7oskftue0sDp4bz89VUfDlZzD_UebC3IcCeY_JEazWZs7lvakBq1L0C0XlnSyOCGfJqVBdp2N_YNcXOrmxaOkACpdouk0yzWW7laW6BC_SKeWbjvbyveT2dJPlDhuK-am1y8iwSEHek8kTi_jwfkfep0KIcUQnwLw2FeLe1rQWLMKik0xPEmlRcuAyEOpGySdc6-Ot7_KHX8SCkzHJIvEVpMIFHwGwyI-QGxJRMtYXXvZPoET2u08kzJ8xvMugGFT5VGoM7s3NnMDFuB0Bk7cA8tmMy4jxwYCGxQ_MsyqyAnq8mIsijVdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ترامپ: اوضاع با ایران خوب پیش می‌رود
💢
رئیس‌جمهور آمریکابه خبرنگاری که از او درباره آخرین وضعیت مذاکرات با ایران سئوالی پرسیده بود، گفت: به نظرم وضعیت با ایران نسبتا خوب پیش می‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/132835" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132833">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👍
🔴
استرس در آنکارا به 100 رسیده .شایعه ویزا نگرفتن 2 3 بازیکن.و خط خوردن آن ها از لیست جام جهانی.بد جور در اردو داغ است  .و چند بازیکن استرس عجیبی  دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/132833" target="_blank">📅 23:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132830">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🏅
حدادی مدیرعامل پرسپولیس: امیرحسین محمودی در حال حاضر هیچ پیشنهاد خارجی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132830" target="_blank">📅 22:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132829">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d48505e0e1.mp4?token=hVRjAkzLbX6BrIqk-9H2NN5Yp6OxkFJPpou9U6hny-pKSuvju5w29dlblnv41qPGRW_vBt8CYW6F3l_oa2vKnYGl1bkpIj_buew2_yS3-pz2cgrzlInKZq721yQi0R6LW2um-gMvNYpJENw-1Fg6YCt25mblazJdBDtaNuy0O6DYeaQPRxGufIXNmbviXPf85IPk8UrjLX5_bG1oD6aN0uVcSciTycR1xvLm_HuQ1R3JqAbsk8L4JafJHjVS4M-Mj7-4dc2IHH7Iw_MbRmfDgLGXUMAg3DOCBOKxtbojHV_usidBlqXpNjWykEkdFr0gRepJJ9AXOag5Vidoe7NLfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d48505e0e1.mp4?token=hVRjAkzLbX6BrIqk-9H2NN5Yp6OxkFJPpou9U6hny-pKSuvju5w29dlblnv41qPGRW_vBt8CYW6F3l_oa2vKnYGl1bkpIj_buew2_yS3-pz2cgrzlInKZq721yQi0R6LW2um-gMvNYpJENw-1Fg6YCt25mblazJdBDtaNuy0O6DYeaQPRxGufIXNmbviXPf85IPk8UrjLX5_bG1oD6aN0uVcSciTycR1xvLm_HuQ1R3JqAbsk8L4JafJHjVS4M-Mj7-4dc2IHH7Iw_MbRmfDgLGXUMAg3DOCBOKxtbojHV_usidBlqXpNjWykEkdFr0gRepJJ9AXOag5Vidoe7NLfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
حدادی مدیرعامل پرسپولیس: به هیچ بازیکنی نگفته ایم که برای فصل آینده قراردادش را پایین بیاورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132829" target="_blank">📅 22:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132828">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f362ea01.mp4?token=ZvVe4eBWYnzsQ6Wn1ClwFqJUFGDO_uyj578QOPCL8aEif3XWEHLllpO19UNkXDNwV2ksa8lSiholGpCM6IQVDOy4dpVa7sNkjZFEEbK5ZcZHLZVB0PLCWWt62vySZwF-texd2KfBz_DNVKOwl8MuyYYYNH5M1s-ZyESa0E2Sk_3hlNBwA7FpNRIabJmdxA1yuM2LBvKgl6tcLd78i82-ka94vxyv6OhgrqYCgZQOYOPQU9CEpEuEA9Sum6CdsGi5ZhP_qmxb8Q3Xj5jQdpPQfCe8wFW1oR8kdar0Y0YJlvzqIsCL_lvJSimMpXo6AqOoSLTiU5HMmbPtlhCfR9vt_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f362ea01.mp4?token=ZvVe4eBWYnzsQ6Wn1ClwFqJUFGDO_uyj578QOPCL8aEif3XWEHLllpO19UNkXDNwV2ksa8lSiholGpCM6IQVDOy4dpVa7sNkjZFEEbK5ZcZHLZVB0PLCWWt62vySZwF-texd2KfBz_DNVKOwl8MuyYYYNH5M1s-ZyESa0E2Sk_3hlNBwA7FpNRIabJmdxA1yuM2LBvKgl6tcLd78i82-ka94vxyv6OhgrqYCgZQOYOPQU9CEpEuEA9Sum6CdsGi5ZhP_qmxb8Q3Xj5jQdpPQfCe8wFW1oR8kdar0Y0YJlvzqIsCL_lvJSimMpXo6AqOoSLTiU5HMmbPtlhCfR9vt_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
حدادی مدیرعامل پرسپولیس: اگر نمایندگان ایران در آسیا معرفی شوند دیگر انگیزه‌ای برای ادامه برگزاری لیگ باقی نمی‌ماند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/132828" target="_blank">📅 22:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132827">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوووری/ حدادی مدیرعامل باشگاه پرسپولیس: در صورتی که سه امتیاز بازی گل گهر و چادرملو به باشگاه گل گهر داده شود به فیفا شکایت می‌کنیم. چرا باید فدراسیون فوتبال در روز تعطیل رای صادر کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/132827" target="_blank">📅 22:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132819">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cfc635883.mp4?token=jsiojbWKCvMeZLjZXyI_2Hq08rrn27B1GE76SAHLORnCO9gf8yG1dECR1Q_IVxyg-csbzifKzW4nz3DXnVSsecy1JaZ2QifnG5empl5Fkr5c_mUKrak_kh0mdnXUrCWE1a3XFpLP61bA1Umg6hCfxqjFlk6ALYZ0Na57rU-lkdDC-D8pn6BzBiA_XpCJ2Ibh-Jf6hprJZz0QlGmVoUJusmN_Cf11j8vMtOU2ukDE0-dr0pe8SGpcDdzxMb9Xuam_zZUiXjY-9poySs_rwRjA9NeVnEUShq-kkolC6jA3U1f-jVRXt7cGeagLjspqXqc700yvzLZCV-uLO9rfVQuWrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cfc635883.mp4?token=jsiojbWKCvMeZLjZXyI_2Hq08rrn27B1GE76SAHLORnCO9gf8yG1dECR1Q_IVxyg-csbzifKzW4nz3DXnVSsecy1JaZ2QifnG5empl5Fkr5c_mUKrak_kh0mdnXUrCWE1a3XFpLP61bA1Umg6hCfxqjFlk6ALYZ0Na57rU-lkdDC-D8pn6BzBiA_XpCJ2Ibh-Jf6hprJZz0QlGmVoUJusmN_Cf11j8vMtOU2ukDE0-dr0pe8SGpcDdzxMb9Xuam_zZUiXjY-9poySs_rwRjA9NeVnEUShq-kkolC6jA3U1f-jVRXt7cGeagLjspqXqc700yvzLZCV-uLO9rfVQuWrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس:  گزینه اول و آخر ما اوسمار است مگر اینکه ما اعلام کند که قصد حضور در ایران را ندارد که فعلا چنین چیزی به ما اعلام نکرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/132819" target="_blank">📅 22:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132818">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b0f1c642.mp4?token=CWShza7Dj3yxJCOz0Wy5n_JikH0POZAq4QD189TnkjPfNpMVi3rfmDI-zW86B49suu7kbDmt3NpG7ZWREzzzL_ZK7Vo-Q86B82nT6F54Kjl2j5oB3MkKdrkLH7jeNKtU3OB4Hoaah466AjM3s0oJtXV1anrqBN1rjsesugeFFhEGJvam3jRYTPKhM5QJ-7WnhX4Bz2OC13jX_lYGtWNfPtStYq25RWCkFGmjp-68Ki1cGPOrzyXOVbjP_DNXx_mcTUw2DbhuppSp1j62XKnyWo-wG6LJqYnlj5UXmsSIj-ORvou5tBj2cGPUnA_m5I2bz4KbNbbF9VNenApwIYb8Woi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b0f1c642.mp4?token=CWShza7Dj3yxJCOz0Wy5n_JikH0POZAq4QD189TnkjPfNpMVi3rfmDI-zW86B49suu7kbDmt3NpG7ZWREzzzL_ZK7Vo-Q86B82nT6F54Kjl2j5oB3MkKdrkLH7jeNKtU3OB4Hoaah466AjM3s0oJtXV1anrqBN1rjsesugeFFhEGJvam3jRYTPKhM5QJ-7WnhX4Bz2OC13jX_lYGtWNfPtStYq25RWCkFGmjp-68Ki1cGPOrzyXOVbjP_DNXx_mcTUw2DbhuppSp1j62XKnyWo-wG6LJqYnlj5UXmsSIj-ORvou5tBj2cGPUnA_m5I2bz4KbNbbF9VNenApwIYb8Woi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مدیرعامل پرسپولیس خبر داد: با هیچ سرمربی داخلی و خارجی مذاکره‌ نداشته ایم/ فقط با اوسمار صحبت کرده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/132818" target="_blank">📅 22:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132817">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e073252128.mp4?token=Lm4R9nw29_jummsGbQr2zo52kDnHNTqcJhDgeS02JvzF5JEGIYAh5_5lwlgk4Ct-vS6YsNbWJmRHcZgid_OKUJ9Buz7e3LbvIwU6bnjBtPrCVquyOCgJ8we1vWLREZLCjLWFBSuEQJsR4PRLWzp7Q54LCEI69u5sAQPx9PJoaKbCmi-DZWt0ZM-WlSkxbzypZCq6M3jf2Zf8zXYbl3_NEu2FmsEf3QzdgWxrKpJHFiLGdyBVL0nn_Ix74udAIFhnngAuX0YLlN0Roj77N2RcUeeNWBUZDaKba7wobIW78ntqyXlrOWct8gNtEEagv6o-TBtGnKZDZajZssvpoMOeBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e073252128.mp4?token=Lm4R9nw29_jummsGbQr2zo52kDnHNTqcJhDgeS02JvzF5JEGIYAh5_5lwlgk4Ct-vS6YsNbWJmRHcZgid_OKUJ9Buz7e3LbvIwU6bnjBtPrCVquyOCgJ8we1vWLREZLCjLWFBSuEQJsR4PRLWzp7Q54LCEI69u5sAQPx9PJoaKbCmi-DZWt0ZM-WlSkxbzypZCq6M3jf2Zf8zXYbl3_NEu2FmsEf3QzdgWxrKpJHFiLGdyBVL0nn_Ix74udAIFhnngAuX0YLlN0Roj77N2RcUeeNWBUZDaKba7wobIW78ntqyXlrOWct8gNtEEagv6o-TBtGnKZDZajZssvpoMOeBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: اگر عدالت رعایت نشود حتما پلن‌های دیگرمان را اجرایی خواهیم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/132817" target="_blank">📅 22:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132816">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: برخی‌ها می آیند روی آنتن زنده و می گویند قطعا پرسپولیس نمی تواند در آسیا شرکت کند، بهتر است دوستان در حیطه وظایف خودشان صحبت کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/132816" target="_blank">📅 22:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132815">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b4c5477e.mp4?token=OoqJ_pVeGXYL6_ozgNaIvKySwgHsS7-7I6cy2Qb7hG7yuCSULbdocqQdHUvL9o_2hR9-I4FYvuPV-49mV8aRwNu5kI2JOexTXGWDy3K3nRd79ogJH_bWIwEsB2fq6JccOZEkyHlfr0olMAXnswj2auDXS6px_kXeEEisLCi-xmPhkS0iG2G7DijrXE7zHKuihnqDUSXU5p6diOrIUqFOUL5FpI1DWqL9UrGctk78ZqsKsoDPkQ3BZtbDPvm8UlSkSi_kNRQoKtMNg6GkESuyRRksgjLDjaVLobbPty44t4Nk-vARPsf_Xr42Lf9TJyX5I_ATF8uxOMUNUHtmSbianZD3AVYigZpmzqGF336Ransaoi9GQGHiQPSG6yfIcjvuBxugr5iu0DG84IpRXIoiynCnaS8m0N8-iBQWCbkzE7Cl6M8yhG90QKLbmG3c5S9zF-Mf6RroQ5GDuO5nOtAkREmFf1wJFsGm6VbUM44TLRKwxrAyXU2mIksfH6E99ehagDWBRvTFyDrwSpspJPS9LC-58ip27oIBN8WOv4uDhhYjYjkPIMkircM--VDT7g_92NogIv--FkL59aHdRQDlq--KtFzymqaxhCVECV6CEs1c5J2hQFvbYuY5XOTVSdXuh5Vr-MqEVRcq5LfBtrAftPj1UnY3kkhj2_AIIpDwYd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b4c5477e.mp4?token=OoqJ_pVeGXYL6_ozgNaIvKySwgHsS7-7I6cy2Qb7hG7yuCSULbdocqQdHUvL9o_2hR9-I4FYvuPV-49mV8aRwNu5kI2JOexTXGWDy3K3nRd79ogJH_bWIwEsB2fq6JccOZEkyHlfr0olMAXnswj2auDXS6px_kXeEEisLCi-xmPhkS0iG2G7DijrXE7zHKuihnqDUSXU5p6diOrIUqFOUL5FpI1DWqL9UrGctk78ZqsKsoDPkQ3BZtbDPvm8UlSkSi_kNRQoKtMNg6GkESuyRRksgjLDjaVLobbPty44t4Nk-vARPsf_Xr42Lf9TJyX5I_ATF8uxOMUNUHtmSbianZD3AVYigZpmzqGF336Ransaoi9GQGHiQPSG6yfIcjvuBxugr5iu0DG84IpRXIoiynCnaS8m0N8-iBQWCbkzE7Cl6M8yhG90QKLbmG3c5S9zF-Mf6RroQ5GDuO5nOtAkREmFf1wJFsGm6VbUM44TLRKwxrAyXU2mIksfH6E99ehagDWBRvTFyDrwSpspJPS9LC-58ip27oIBN8WOv4uDhhYjYjkPIMkircM--VDT7g_92NogIv--FkL59aHdRQDlq--KtFzymqaxhCVECV6CEs1c5J2hQFvbYuY5XOTVSdXuh5Vr-MqEVRcq5LfBtrAftPj1UnY3kkhj2_AIIpDwYd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: قطعا برای گرفتن حق پرسپولیس کوتاه نمی آییم
◻️
ناراحتی دوستان از رفتنم تا دفتر ریاست جمهوری؟ حتی اگر لازم باشد از مراجع بین المللی هم پیگر حق پرسپولیس هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/132815" target="_blank">📅 22:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132814">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7fcad3a9.mp4?token=ZcKPuDe6V_3F9pxnmbDI0Nh1si5fOhb672va8QYoYGSN8pWvV-JHdpOWKFVJDeSIKOYlxeO2Ae7cNW0n8_PldgFcpSF5YjOrkjFzNb2vGceZHGaSINvkWIaAn7h0JBBr-ZXuUzm8EclqmHbXCL4RXUBgvmbtI61GV1KG_ujhXAqMONgYGCvViWan0q9rh3In_6OjR5PyLBM_5OhsVcDNq9cnEeAhHpAdVkgs82-pNLHg693cwjYoyWMzm2_XX3QHx4JzxuHbsLqPtUwkfN3yEZCIrwxqulHbvRUg9-htH4HJgJXBpEbPMoFsKaSweP4DQhpxxntNWRni8gWL3Q0VYzopJcnMBXH0hy9cxfC4wOyS7EtUxAkWln-Z0xben5cVdYuQmVUDM2aKKrXXoN0hVsYFJSL3ZZkbLFtnLE3jdplFrSkVSvBGzk-JzWl5LEqWFF2TO-OO46QHWCmCqqIp9BgUNqW_Akem1RLj43dJbszf1znJ6rxX6zpsPp3tl4Nto02BX6czkp3LIpfE_AClHgoT4GKM9nYT9lTBtPoZkkjYw6emrjtsjfvm2IdgoQnKW0ufxUUVube9bcGlonW3v9MOFsn1FbtdcjyseommHzF1_e1sAMagOpVAEXffVIqXJ29N2aLMKcIMWWU1tGvF25zrOxGuyRK5TBeDG4HXiGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7fcad3a9.mp4?token=ZcKPuDe6V_3F9pxnmbDI0Nh1si5fOhb672va8QYoYGSN8pWvV-JHdpOWKFVJDeSIKOYlxeO2Ae7cNW0n8_PldgFcpSF5YjOrkjFzNb2vGceZHGaSINvkWIaAn7h0JBBr-ZXuUzm8EclqmHbXCL4RXUBgvmbtI61GV1KG_ujhXAqMONgYGCvViWan0q9rh3In_6OjR5PyLBM_5OhsVcDNq9cnEeAhHpAdVkgs82-pNLHg693cwjYoyWMzm2_XX3QHx4JzxuHbsLqPtUwkfN3yEZCIrwxqulHbvRUg9-htH4HJgJXBpEbPMoFsKaSweP4DQhpxxntNWRni8gWL3Q0VYzopJcnMBXH0hy9cxfC4wOyS7EtUxAkWln-Z0xben5cVdYuQmVUDM2aKKrXXoN0hVsYFJSL3ZZkbLFtnLE3jdplFrSkVSvBGzk-JzWl5LEqWFF2TO-OO46QHWCmCqqIp9BgUNqW_Akem1RLj43dJbszf1znJ6rxX6zpsPp3tl4Nto02BX6czkp3LIpfE_AClHgoT4GKM9nYT9lTBtPoZkkjYw6emrjtsjfvm2IdgoQnKW0ufxUUVube9bcGlonW3v9MOFsn1FbtdcjyseommHzF1_e1sAMagOpVAEXffVIqXJ29N2aLMKcIMWWU1tGvF25zrOxGuyRK5TBeDG4HXiGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: اینکه هواداران پرسپولیس را مقابل فدراسیون فوتبال قرار دهیم کار درستی نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/132814" target="_blank">📅 22:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132813">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73ccb46629.mp4?token=ppxxlNnYjVWC0WX0s2ccc5kNwzwCw-FeFjGpkY9XZmI0UaoepVRVqdPfe7uD8zZymmpzdN3NsanzX15WEgxMYLINyr5fVJOE3zYe5rY1RGMRz_m8F8eQqZhF8Mlf43teH5TQgV4QkWcnn52pReCT_pWmzNBZHNLx_09NyaCtAdTkQbYw2BaZXxrdAYaKLut9xMd6XJTwdBC0inoOXspXItZx8Tj8NxV8Sy3k4kT8lDMWeoNrGlbGQ7oLA3n3HwXrPcBG4RDI7GprZ3aeNsgpxVpL5SPWpZ0mzvcjPz6L6EmojDKnWyyRzFEyxt0kNxlLmovyc7EfKqb6Gm0eWFhmhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73ccb46629.mp4?token=ppxxlNnYjVWC0WX0s2ccc5kNwzwCw-FeFjGpkY9XZmI0UaoepVRVqdPfe7uD8zZymmpzdN3NsanzX15WEgxMYLINyr5fVJOE3zYe5rY1RGMRz_m8F8eQqZhF8Mlf43teH5TQgV4QkWcnn52pReCT_pWmzNBZHNLx_09NyaCtAdTkQbYw2BaZXxrdAYaKLut9xMd6XJTwdBC0inoOXspXItZx8Tj8NxV8Sy3k4kT8lDMWeoNrGlbGQ7oLA3n3HwXrPcBG4RDI7GprZ3aeNsgpxVpL5SPWpZ0mzvcjPz6L6EmojDKnWyyRzFEyxt0kNxlLmovyc7EfKqb6Gm0eWFhmhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: واقعا چه اصراری است که رای کمیته انضباطی شکایت یک تیم از تیم دیگر در روز  تعطیل اعلام شود؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/132813" target="_blank">📅 22:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132812">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d515e687b.mp4?token=FSOf1wRdrDHugSFoz7HFRNyAxoLovO_6m7leK8eESedozlkFUzI1ORQHIBRGqmA3m4R6DLE-iuNt4MF8qbcN0w329diiHm7FnJj0RzHPGNo3JLUrqTdoec_oT4P5RepQTLB12fq0GgzP-wm8VkSwA2G6GFcWXeI9841Vibxx10pE61vK5zyD1yyExUjxu2sDMYypWeydUQS4ApEyYCYgEI60xGnrlUt6BPiHdFyQiFBgUnlAPB1ykoMeTfXJFiQXa3etHhWr8Tgio-ygWo8ceSEg1w_qs32b4LAkgd-LtEvjZ-ivBRdcBXFizjJohyygW6SJGyvSJpu5kKGVHlAL3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d515e687b.mp4?token=FSOf1wRdrDHugSFoz7HFRNyAxoLovO_6m7leK8eESedozlkFUzI1ORQHIBRGqmA3m4R6DLE-iuNt4MF8qbcN0w329diiHm7FnJj0RzHPGNo3JLUrqTdoec_oT4P5RepQTLB12fq0GgzP-wm8VkSwA2G6GFcWXeI9841Vibxx10pE61vK5zyD1yyExUjxu2sDMYypWeydUQS4ApEyYCYgEI60xGnrlUt6BPiHdFyQiFBgUnlAPB1ykoMeTfXJFiQXa3etHhWr8Tgio-ygWo8ceSEg1w_qs32b4LAkgd-LtEvjZ-ivBRdcBXFizjJohyygW6SJGyvSJpu5kKGVHlAL3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: کدام جریان به دنبال ضرر پرسپولیس است؟ همان جریانی که دنبال این است که پرسپولیس به آسیا نرود، همان جریانی که مانع برگزای لیگ برتر شد
.
نباید از این موضوع به سادگی گذشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/132812" target="_blank">📅 22:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132811">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس:
اینکه چه جریانی باعث شد که بازی‌های لیگ برتر برگزار نشود واقعا جای سوال است/ در سال‌های گذشته هم که پرسپولیس قهرمان لیگ برتر می شد در هفته‌های پایانی امتیاز جمع می کرد و قهرمان لیگ می شد/ این احتمال وجود داشت که باشگاه پرسپولیس به صدر جدول برگردد، واقعا این جوای سوال است که چه جریانی مانع برگزاری مسابقات لیگ برتر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/132811" target="_blank">📅 22:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132808">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
لیست مازاد اوسمار از نگاه رسانه های تلگرامی:
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
میلاد سرلک
🔺
محمد خدابنده لو
🔺
سروش رفیعی
🔺
دنیل گرا
🔺
مرتضی پورعلی گنجی
🔺
سهیل صحرایی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/132808" target="_blank">📅 21:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132806">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
ادعای علیرضا محمد، دستیار تارتار در گل‌گهر: باشگاه پرسپولیس با تارتار مذاکره کرده و اگر اوسمار برنگردد، تارتار سرمربی میشه! او می‌تواند پرسپولیس رو قهرمان کند! باید چه کاری دیگر کند تا سرمربی شود؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132806" target="_blank">📅 19:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132805">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
خبرنگاران کاخ سفید میگویند که ترامپ پستش را بد نوشته و در واقع اعلام پایان محاصره نکرده و منظورش این بود محاصره رفع میشود اگر رژیم ایران با این شرایط موافقت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132805" target="_blank">📅 19:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132804">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
یحیی گل‌محمدی به تیم دهوک کردستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132804" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132803">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
شانس دوباره محمودی و حبیبی‌نژاد در تیم ملی؟
◻️
امیرحسین محمودی و هادی حبیبی‌نژاد هنوز شانس حضور در فهرست نهایی تیم ملی را دارند و به‌دلیل احتمال مشکل ویزا یا مصدومیت برخی بازیکنان در اردو نگه داشته شده‌اند. در مقابل، امید نورافکن ظاهراً اردو را ترک کرده است/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132803" target="_blank">📅 19:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132802">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
باشگاه پرسپولیس:
‼️
ما با آقای تارتار مذاکره نکردیم. این حرف‌ها برای بازارگرمی است. پرسپولیس تاکنون هیچ‌گونه مذاکره‌ای با تارتار یا هیچکس دیگه‌ای نداشته و این ادعاها صحت ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132802" target="_blank">📅 19:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132801">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
علیرضا
محمد:مذاکره تارتار با پرسپولیس را در رسانه‌ها شنیدم / به خدا نمی‌دانم به او پیشنهاد دادند یا نه
💢
من در آن مصاحبه ویدیویی هم گفتم که در رسانه‌ها این مطلب را شنیدم و منظورم این بود خیلی از رسانه‌ها گفته بودند که مهدی تارتار مدنظر پرسپولیس است. خدا شاهد است صادقانه به هواداران عزیز پرسپولیس می‌گویم من اطلاع ندارم که باشگاه پرسپولیس با مهدی تارتار مذاکره کرده یا پیشنهادی به او داده است یا ممکن است بدهد.
💢
من فقط نظرم را گفتم و هنوز هم می‌گویم اگر قرار است آقای اوسمار نیاید مهدی تارتار می‌تواند مربی خوبی برای پرسپولیس باشد. ولی اینکه با او صحبتی شده یا نشده به خدا من اطلاعی ندارم. امیدوارم پرسپولیس موفق باشد و وضعیت کادرفنی زودتر مشخص شود و نتایج خوبی بگیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132801" target="_blank">📅 17:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132798">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNP845R0ZCuMSreG2fcPDvwYenzS9ZdEp9OFzu7z_l9JA7gcdfUFvPBr9hxL2rVF_36IDryxCDA-ElWIUbmJD59SdplJlvgtUXgaK1xOZidV7qocGcUfCJvzrRuw7jkoEdMo97hhAqrA-AeaS_Ut0LT77oBN25dL_wIjMaPIgZ8jxVDfhrQRjVQG86jDRsyE4VQqzTSrJF-RP-8MqUxk33-AG-rkkBvDQnOH1igwYxHJGfrYRXPC6MOIczN9vHpp7zoK5j9eWpGrEeRhvrMm21_qCjxdbS1dPs3C7DqxO0mj_Ef1a7EeOVkXbMojcBZo7sSlvupr5R_GaojxQ0T_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عکس تیمی بازیکنای نروژ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132798" target="_blank">📅 16:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132797">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132797" target="_blank">📅 16:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132796">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEkCss9o58e5dip6scvbHkG8CQo_IzJo5OzB7cdKabAFI0onEcBb6jric41B-g8wyUo39kKMmO5SvI47ztfzlvVHCOAU3B9UVVg6CuCYv5ARGLRANETHWEV5P161prerJON33bxh8lrz_ZpHHy9uUS-7rHNtxyaoHMzfPVvCvqAVhMfPKB2W2ktoC5NutVtfIOkfjC0P7Wb2E1sQLhaYdVMrSix2y9Dkjm28jIAF56_tOSHYPXc8k5Vh5c4kQFLWr4qneupAQI9x8I-JrwlujqbAmG4xod9twrfKpGyJslgTaAaBcCC62GFB4KzpemQaYz4p2JrlxyQjSCVZcek_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔼
صعود یک پله‌ای در رنکینگ فیفا
؛
🇮🇷
ایران دوباره در جمع ۲۰ تیم برتر جهان
🔴
در فاصله ۶ روز تا شروع جام جهانی، رنکینگ جدید فیفا اعلام شد که براساس آن تیم ملی که در آنتالیا گامبیا و مالی را شکست داد، با یک پله صعود دوباره در رتبه ۲۰ جهان قرار گیرد.
📊
در این رنکینگ، آرژانتین تیم اول است و سوئیس و دانمارک تیم‌های قبل و بعد از ایران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132796" target="_blank">📅 16:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132795">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
🇮🇷
🇺🇸
🇵🇰
العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132795" target="_blank">📅 16:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132794">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCl-_HwibYD6GwX-Sz8SfheFB8Q_MAHXIZ3RVjTJ7y0pgT53JTGzSb1UlnTnllU6V5g0jADOLvo6dSc0mbQ1LVaJoKhc0KPffZ4PD3BLZPq_HxwAIhqukRWlbS9CpwZBGmY4K8uO5jjBHJpCWpOc-OchqcsZkC-KESUhHgS8_04VOMVEjGziImWFyTgr5COsUzbTulIPXbGSZYCx1_yTAO0edKaDitUjlV81o1FjlfGJXezcFAr7WlUfwWk9O2PHcHTFGewOjvXrlEEY-ZDHnsA2HSx8PB_nhxU-KUl48rmo107Uytq0nBltzdBnd0okYTqowEGy1CE20I73x1C8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/132794" target="_blank">📅 15:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132793">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCguYZn2GeNn1_JAPB5SZ_lvcDpHyrT4s4EnGqLIagiFyN-I09ahEA_nLtKtAudH2TsiK_FpGKtdhDN1HuF5nJdCGvZLryDXpjxs7DL8fY8XYba6siyDdDWicZtZaj7HOoaqW_m32J-1Hcswcjr3lYM-LYSAgtVNojbGFDDyAv4D-kD0WQJ36hqXJaFli8YbuxqjZ6aj4jIsoaBCW0iOcjMU6O2bPLZ-UBWGoVjYIatU2bxmNPItnRthlpH9-CjJ0hs63SreeGn7N_wsiwyNi2TOfIF0ZNQha6GVz2f2uqYvi9iHhUkgJEJahCXNSnqg893wO0hTLNnu4_14O3Vbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سروش رفیعی به طور رسمی از پرسپولیس جدا شد. سایت ترانسفرمارکت هم این بازیکن رو بدون باشگاه اعلام کرده.
🔴
رفیعی در فصل اخیر طی ۲۳ مسابقه به عنوان هافبک بازیساز، آمار صفر پاس گل رو ثبت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/132793" target="_blank">📅 15:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132792">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7zbz-DbqpNPEMRoLYYWv1z60RnUKbKC4PGBbbOAh6ONjaLyX0XYfdCspzKBWRtiVkCgOLGCUj03UUw9deN2oxZDpGs54n5uW6uzY8nmbaH9NDoQiYYPYjVv5Zl-4y5YnKOznyxXPbk4pgwPJV0LLOUMAidOEeOYZPSMQCi6_AYGmtnwrvot1BFlR4v5mqJuJ75WQYL2APLtI1JDuCHd-bHxceRbSWmgoVjDf_4RqVKrMnY5mc4y-ihhMotY1jbtYKnmgnpFSB1hO-malx3JX1taC-TFfdO8B5JSeYcbXwhiL0phlomskFNcP_2EL8K2UUxhDsDCUvCECaYkMPFoCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
با حضور در لیست تیم ملی، میلاد محمدی سومین تجربه حضور در جام جهانی را خواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132792" target="_blank">📅 15:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132791">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
🎙
مهدی تاج:
⏺
فقط با فیفا در ارتباطیم و هیچ تماسی با ایالات متحده نداریم. کشور میزبان حق اختلال در تیم را ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132791" target="_blank">📅 15:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132790">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
شبکه العربیه از منابع مطلع:
🔴
جمهوری اسلامی میخواد اورانیوم غنی‌شده‌ش رو به چین بفرسته، به شرطی که چین تضمین کنه این مواد رو به آمریکا تحویل نمیده.
🔴
به گفته این منابع، خیلی از نکات مربوط به برنامه هسته‌ای جمهوری اسلامی تو مذاکرات الان حل و فصل شده.
🔴
بر…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132790" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132789">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
با اعلام ایجنت سروش رفیعی، این بازیکن پس از سه سال از پر‌سپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/132789" target="_blank">📅 13:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132788">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت  بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/132788" target="_blank">📅 13:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132784">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
اول یا اخر هرکسی بیاد و بخاد بره؛امثال سروش و هرکسی که حاشیه سازه و از نظر فنی به تیم کمک نمیکنه باید بره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/132784" target="_blank">📅 09:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132783">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
در سکوت و سکرت....  فعلا،مذاکرات داره خوب پیش میره///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/132783" target="_blank">📅 09:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132782">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
امیرحسین محمودی علی رغم خط خوردن در اردوی تیم ملی حضور داره و قراره همراه تیم ملی راهی مکزیک بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/132782" target="_blank">📅 09:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132779">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
امروز عراق با اسپانیا بازی می‌کنه و جمهوری اسلامی با مالی!!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/132779" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132778">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
اوسمار ویرا :
◀️
با 40 روز تمرین پرسپولیس را مدعی قهرمانی می‌کنم.
✅
اوسمار ویرا سرمربی برزیلی پرسپولیس همچنان تاکید دارد که در صورت برقراری صلح، به ایران باز می‌گردد و در جمع سرخپوشان باقی خواهد ماند.
✅
ویرا از بابت شکل تمرینات و نحوه آماده سازی بازیکنان…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/132778" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132777">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f9110aac.mp4?token=Uf0bzPeXcCZhIwInhrERRb5Jv93OzFnVDzM_UHXq-PrnYLEbVuH1Nd0heJ8XNpPitzbR3g0Vem0QbfaLo3oW5Wou8Cp94yz1Ro6oVF0yjKfbfnarkMEkQ0h0hBQSVMlKfugp28InQIWdepCPtUGY46OZWjtnL0tnIXlth0BmWebAz3RmCKtuWCLAuT9SJvbGK9xIASbajE2YuARg6uODkLFvleOkyMFfusljICSOmAtR5hqVJHm6RFKK97O_xztb0jwVbI_PzaXyZZmIq_Me-KMWuibjeoYxnbh01CyNBTCKWBOd6jkyS1DiwDtPtkMfzbQpcfrdBuunzugA4bs10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f9110aac.mp4?token=Uf0bzPeXcCZhIwInhrERRb5Jv93OzFnVDzM_UHXq-PrnYLEbVuH1Nd0heJ8XNpPitzbR3g0Vem0QbfaLo3oW5Wou8Cp94yz1Ro6oVF0yjKfbfnarkMEkQ0h0hBQSVMlKfugp28InQIWdepCPtUGY46OZWjtnL0tnIXlth0BmWebAz3RmCKtuWCLAuT9SJvbGK9xIASbajE2YuARg6uODkLFvleOkyMFfusljICSOmAtR5hqVJHm6RFKK97O_xztb0jwVbI_PzaXyZZmIq_Me-KMWuibjeoYxnbh01CyNBTCKWBOd6jkyS1DiwDtPtkMfzbQpcfrdBuunzugA4bs10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ: مجتبی خامنه‌ای کاملا تو کارش حرفه‌ایه. البته یه سریا در موردش بد میگن که دروغه، مثل من که یه سریا به دروغ در موردم بد میگن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/132777" target="_blank">📅 00:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132774">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
فووووووررررری
🔴
حمید ابراهیمی : با توجه به نیاز حداقل 2 هزار میلیاردی دو باشگاه چادرملو و گل گهر سیرجان برای حضور در آسیا وزارت صنعت با این موضوع مخالفت کرده و به زودی انصراف آنها از این موضوع رسما اعلام می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/132774" target="_blank">📅 23:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132773">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIKkqa30OZ1tfTh_x8nNvadvUCGuQOxUhN8IVoK9i2ONt0omxNTghhROXTyKIrljSy7ESYTRpP8JgQYKAG3G48nLXuZ9jRk9cWlAFkoVfsUtjWxrOhO1UMTLjWo60agxbvHQxsf50G4IG7j3oYp-L3oxZufF6QqiBST5hEyPmN_Gbh1Bd_DGV45eeDoTTuqhG4FslIztoWMydpo-YCXRS0jfSJcgigIPSc_wa--VAOX8z18fGJUgp-2rhwzdDEd3vfwoluS6O8xhLacZe77IH2ZV8XkugqvOAbsDSJWLseZy8iOnBMpXxueQVTvnUzuc0lGxoJJTF8LbQjbc6bnHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ایران با دو برد مسافر جام جهانی شد | سعید عزت‌اللهی دقیقه ١٢ و رامین رضاییان دقیقه ۵۵ گل های ایران را به ثمر رساندند
ایران ۲
مالی ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/132773" target="_blank">📅 23:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132772">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
فووووووررررری
🔴
حمید ابراهیمی : با توجه به نیاز حداقل 2 هزار میلیاردی دو باشگاه چادرملو و گل گهر سیرجان برای حضور در آسیا وزارت صنعت با این موضوع مخالفت کرده و به زودی انصراف آنها از این موضوع رسما اعلام می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/132772" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
