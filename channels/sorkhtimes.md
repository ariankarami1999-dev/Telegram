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
<img src="https://cdn4.telesco.pe/file/dS6vHYsGDyfg8pavuCK7fg8NQ1tWp-euV6hrptJD9ta2EJ_PC5ehFCf_6QFyvapZpao35851s4_qx698UEYEw7YHVdaGj2_PRWjaxqhB-s8ucY_O1PPeiKbFbrerDF-87SeP-Oa8qhZJoTxyK55VEJH7hOtVnqFItX30NS5A7wHXTKUSafQ8bePM0BPKzBCBsZXcJWtJ1t-ykZtVjmd5REXycfPju6NvIcyDqh4IMDg8wkOUe0TJ8joEdqkTPKnBF7cvzKT6rqGc03uvmWWDbaAQBbdv-95z5KxOQE_hGdFWlkwQbmxCATsVWBKyq2OJQwMOm_Lmkqaekv_vam9etg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 18:02:50</div>
<hr>

<div class="tg-post" id="msg-133188">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
فرهیختگان: پرسپولیس دنبال درخشش اورونوف برای فروشش با رقم سنگین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/133188" target="_blank">📅 17:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133187">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/133187" target="_blank">📅 17:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133186">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 280 · <a href="https://t.me/SorkhTimes/133186" target="_blank">📅 16:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
🚨
اسرائیل هیوم: وقت تمام شد مذاکرات شکست خورده و پاکستان از میانجیگری دست کشیده!
🚫
ترامپ بعد از سقوط بالگرد و حملات دیشب ایران بسیار عصبانی شده و میخواهد هرچه زودتر به جنگ باز گردد. پنتاگون طرح های حمله جدید راه به ترامپ گزارش داده و اسرائیل را نیز مطلع کرده…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SorkhTimes/133185" target="_blank">📅 16:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133184">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
فرشید حقیری: اورونوف و می‌خوان بفروشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SorkhTimes/133184" target="_blank">📅 16:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133183">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚡️
⚡️
حدادی: دفاع راست اولویت علیجانوف بود صحبت کردیم گفتن 800 هزار تا 650 هزار دلار پایین آوردیم یه سری اتفاقات افتاد بنده قرار بود برم ازبکستان گفتن تردید داریم باشگاه بتونه کل پول رو برا همین خواستم برم ازبکستان که پولو بهشون بدم قبول کردن پاختاکور گفت چون…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/133183" target="_blank">📅 15:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133182">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
#فوری | به ادعاهای رسانه های عبری تصمیم ترامپ برای حمله به پل ها و زیرساخت ایران قطعی است./انصار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SorkhTimes/133182" target="_blank">📅 15:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133181">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوووری/ترامپ: ارتش ایران کاملاً آشفته و بهم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و هوایی آنها، دیگر حتی وجود ندارد.
🔴
آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و عمل نمی‌کند. قلدر خاورمیانه مُرده است!
🔴
آنها برای مذاکره بر سر توافقی که می‌توانست…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/133181" target="_blank">📅 15:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133180">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlQIglvOmnBxjnMCOou332LgEbA1pAJPI94yDGySWTPgrfqSc4Q1j4a6W7zyMyu6MU1baBjlqVhnYX4mrMcZ0WuTLrBDcwerzgy8SsPcrxiXTHT4FI3Wv79nMvIQUdMTYPWzTfl6c__LZtiZS3YpuS0n8IsggqkvLoMynnfd6UpUk0HvGBkyLOrID5CM14TCI1CE3buNyCu1jcuIFfq3XuB9G4miBA0BPJjrteVyKH9RMx5jhMulVJQO6zIw_Sr06W1XC1kODgRUUp9BthfbJjpK7LhBuF9JINtMZcoMKQy4hDigzGMdaxpEuEisW0HTKnv3HdRBtv2kIf7EMSEL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووری/ترامپ: ارتش ایران کاملاً آشفته و بهم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و هوایی آنها، دیگر حتی وجود ندارد.
🔴
آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و عمل نمی‌کند. قلدر خاورمیانه مُرده است!
🔴
آنها برای مذاکره بر سر توافقی که می‌توانست برایشان عالی باشد، خیلی دیر کرده‌اند، حالا باید بهای آن را بپردازند!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/133180" target="_blank">📅 15:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133179">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
فرشید حقیری: اورونوف و می‌خوان بفروشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SorkhTimes/133179" target="_blank">📅 14:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133178">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
اسمار ویرا سرمربی پرسپولیس بامداد شنبه به ایران می‌رسد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/133178" target="_blank">📅 14:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133177">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyFHjaUHrf9o5SGAyCW_Q131QAWrLDt7NpcrBDCYxEOCqnZEzJRpAipHXAGYJTZ6NZGa4yfx_gAxshsi67XObiHjVlyCr6wupDh6cOWlABTlJ33LWQGeaASSGSK3UNCyh-WnxXdb5rYPRB_TDX2FIr8aJN_1se_V5lLlw-oWqsdppTCGvfZ7wcBtGmbioylTv6qsEHjUA8sCaHYfkNph_Av0HjCrhzhNozUGoiggru-d-GYHnXVKEPuMsxA8HLBdT2N0BpeJ8ZqK0wD68MUfTFd48pxAZa3uOfOuMnl8JfC_G1G8EqMdbIm3SFdOltPHZKqqSXc_CAQ0H5YxtsET-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/133177" target="_blank">📅 13:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
فرشید حقیری: امروز جلسه محرمانه بوده و سرپرست جدید پرسپولیس انتخاب شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/133176" target="_blank">📅 13:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133175">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
وجود اعلام AFC، پرسپولیس، چادرملو و گل گهر برای آسیایی شدن همچنان شانس دارند/ معرفی سومین نماینده ایران تا ۹ تیرماه
⚪️
در شرایطی که کنفدراسیون فوتبال آسیا دقایقی پیش اعلام کرد که تیم فوتبال گل گهر سیرجان سویمن نماینده ایران در فصل اینده مسابقات آسیایی  است…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/133175" target="_blank">📅 13:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133174">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
فوووری ، پرسپولیس آسیایی نشد
🔴
کنفدراسیون فوتبال آسیا AFC، نمایندگان ایران در رقابت‌های آسیایی را اعلام کرد!!
🔴
استقلال و تراکتور در لیگ نخبگان آسیا و گل‌گهر در لیگ قهرمانان آسیا 2 شرکت می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/133174" target="_blank">📅 12:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133173">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei-d4UHCee8mUd5BNgmb1tcuBu9ve7NdrINNL_8qRWDDO9Muk5eGRB6rMF9OLqJIvvqUTUIudoZ_XsRDBcdy7do6DtdpWsxezeofwH4ncelXICM2ag6CW0O-01umzxR6wQJ5NdKUNcPsAfPUwtY0zWr2WBUFIcN6It4beIrwqT9X-xE_9EKxykO_NgDy-xK1_b-cKelsyXYxXD9Tivq50RqptXbQ-89h0s7jGMFwTBmB36TweHgryvxvAZ3lyZ-GyH8wu7-lWNbCOflifkLuKKt5FzbH8TkxrwojtSBWP_gdWzdsjQc-GRTMPUBJdEdZ54P5qreY_om-yHMg1biVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت خاورمیانه واقعا عجیبه
‼️
🔴
افغانستان و پاکستان که دیشب باهم جنگ داشتن، امروز بازی دوستانه دارن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/133173" target="_blank">📅 11:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133172">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdMK0ddI3NaeBmsspm0iHw9Sl0_z8KMF1CW3w-A4tE-EuToG3CFk4Pmz1DxwFr8dH-OBuMX8BNhELZe2p9JhBBKu7g14MCVBX5KxSJF4FSMw59BXCimZBi5scHWCLVBP3mJEoL_JeWTi7F51Z0STtBHl2R3fs8oT7TA-1aB9T5BBt8vmd5LJFRok1Ra1qfmfm6sHBD-vq2qeVyICjnhCz7c7NGX0t5wFqJMucGBmhAw_x3-X07FweY36g1IWeNo07frndY6GK05KuZJEuTupndDmhEeVvQCtLaYHd_TSdefyq1NQz1WuS9YX5zPF4zChrV50Mm1JyN6H7g-udPLpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کریس رونالدو کاپیتان 41 ساله پرتغال : من میتوانم چهار سال‌ دیگر بازی کنم و در جام جهانی 2030 نیز حضور داشته‌ باشم. حالا حالا ها برنامه ای برای خداحافظی از دنیای فوتبال ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133172" target="_blank">📅 11:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
فوووری ، پرسپولیس آسیایی نشد
🔴
کنفدراسیون فوتبال آسیا AFC، نمایندگان ایران در رقابت‌های آسیایی را اعلام کرد!!
🔴
استقلال و تراکتور در لیگ نخبگان آسیا و گل‌گهر در لیگ قهرمانان آسیا 2 شرکت می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/133171" target="_blank">📅 11:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133170">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/133170" target="_blank">📅 11:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133169">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
اینترنت بین الملل در آستانه بازگشت به وضعیت پیش از جنگ؟
❗️
رشیدی کوچی: اینترنت این هفته به حالت قبل بر می‌گردد، یا ۴۸ ساعت آینده یا تا پایان هفته!
🔴
جلال رشیدی کوچی در واکنش به زمزمه های اتصال دوباره اینترنت بین‌الملل طی ساعت‌های آینده:
🔹
من فکر می‌کنم در…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/133169" target="_blank">📅 11:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133168">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری
🔴
پرسپولیس به دنبال جذب محمدمهدی محبی بازیکن اتحاد الکلبا/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/133168" target="_blank">📅 11:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
صادق محرمی درخواست خروج از باشگاه تراکتور را داده و قصد ندارد فصل آینده در این تیم باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/133167" target="_blank">📅 10:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYThtLiS4sAj4UOtil5I4G4iCR7vGLS9Q1MCUzYLjAPGDFuZIb7O_4dmePhfiEZTKjNheD6tq3LCA_tRF5SSqFTjB65fweDCCebsPy-S2s_n5XQ9k2qOV0MCpr34BW1kly1B8YvskDqH7C308BeIvCk5yCFjesAVOGVzb-635tkINR-K4DJCZ7K2ceS39jPPXVLDy8kQN_lTR_uLXlZ6ypgZG_qRb3Z0yjn7XnDWHdOrk7sX5BkwLLKCGb6NMK8_mDScTLAJZ__fe3Znx96kVpmy4KmRBb0P6wvaWfTH-dvitL-dZVTyw97Ten4Dj7gk5VmqT5VclAh0RtE7TjtT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووری؛ پیام صادقیان بازیکن سابق پرسپولیس که به ترکیه پناهنده شده بود به ایران بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/133166" target="_blank">📅 10:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/133165" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
● آخرین خبر از خارجی های پرسپولیس
🔴
• دنیل گرا تا ترکیه خود را رسانده اما نتوانست روز گذشته به تهران سفر کند و به محض باز شدن حریم هوایی به تهران می آید تا در تمرینات سرخپوشان حاضر شود.
❗️
• اوسمار ویرا سرمربی این تیم هم تا آخر هفته با بلیتی که باشگاه برایش…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/133164" target="_blank">📅 10:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmZYSQX2KhprWoouVrVa9VWgwygoAB_IVnDwaIYTivIcm_SAcWtRQNXx2UwjiRp5IEmaIJt8qDbbXA2e2tffOaH8x7poGdWInkaA0GHwhjQuizAo6OqPSiS0ddP6vUet6ohxqmHmcWC7P08V3kV81Nh8XlR6XypvraJ2R01QZmu0Jj5RUFUsY9XXrq3KFLmNuO1wim58VCPsLzxYNK5uRDBY66Ty48Xl2jgRSgfXBZFbe4og627fKM_R0GbhlNSHQQjsmRVZdGg2AgKUROuTLrjIRnmE6xVfk45oKMMlkfcmp39OZoEPE6M7OaSDQ9oMWr6KA7j5tXKq2UBEValOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهروز رهبری‌فرد: درست است که همسن و سال‌های من به تیم ملی دعوت شدند ولی با ۷ امتیاز صعود می‌کنیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/133163" target="_blank">📅 10:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
#فوری؛ سنتکام: عملیات دفاعی آمریکا در پاسخ به شلیک به بالگرد آمریکایی آغاز شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/133162" target="_blank">📅 09:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBaDoFYMoWUutRtJiOvL38foIsrjF3Wtt1WE-k60mgkXj1zPj1PLEqFAdFkOezv_c9dcUBb1duglOrSNWBdCGecByR0jXjf7FmZW4EevQNSiudVMdna6L1Klet1kJv1oHeU6Agg7RGADYn-0csGmzrdmfEamGfprKEC7hQXQFrkMM11AXW2la2Rnw8IWL4QVcKw2ZeK89__DZr-bUYsXaaBLUumnNX460Zt33tPxNOwDkIreuid8JZUm3cvVpOFQ5NIA86ANm-r6yQc0bJIWz_83xAXWTQ45ygZeI_trTV6iKbERvFiUmPzeSRHTGlAWtIDyKPvUoxG8yFEqOHRPFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133161" target="_blank">📅 01:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4opBbzP8KryUjDbiqVkBrgd6QbUnYrfAegURkH9TjxJ-h6_3fm3Y2a--Nw21jVGC6f82rXCFYMRJ9fMMuQ0eg3jrErx5povLyEXvTZgmsmxjaILCe4LoKx52fusFrlCoYXPPaZEC8wzVcABJRTJUbTXurY-sUBgF55QlpjrsKOKowJJ4QODm_XmPv0MZVCy-4RBspyG4pjQQcZlx_pKZQs_x4YB1Bd0SsmWXVJvI3brkmVk1qZQCqUwELvfUqUNPv4v6M8mKZ-1CFqklW6AlKpo0XjK3r0kOfnpOykt49ZyIC7uAID_u1OpS-rfJuJYaXOuopTmiaPPDF-55J8Acg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ سنتکام: عملیات دفاعی آمریکا در پاسخ به شلیک به بالگرد آمریکایی آغاز شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/133160" target="_blank">📅 01:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| پهپادهای ایرانی در حریم هوایی عراق به سمت اهداف خود در حرکت هستند
‼️
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133159" target="_blank">📅 01:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
#فوری
| مقام آمریکایی:
🔻
هدف از حملات آمریکا ارسال پیام هشدار به ایران است
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/133158" target="_blank">📅 01:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
#فوری
| گزارش‌ها از انفجار در بحرین
‼️
‼️
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/133157" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
#فوری | حریم هوایی کویت بسته شد
🚀
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133156" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
#فوری
| آکسیوس به نقل از یک مقام آمریکایی:
❌
نیروهای آمریکایی به چندین سامانه پدافند هوایی و راداری ایران در مجاورت تنگه هرمز حمله کردند
‼️
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/133155" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133154">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
#فوری
| حریم هوایی کویت بسته شد
🚀
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133154" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133153">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
شایعات،فهرست اولیه اهداف آمریکا:
– پایگاه دریایی راهبر سیریک
– پایگاه دریایی ولایت جاسک
– موقعیت پدافند هوایی بندرعباس
– باتری موشکی ساحلی میناب
– باتری موشکی ساحلی قشم
– بندر قشم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133153" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133152">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7285144264.mp4?token=TBwjOAZfF-7oswt4O2YBnzwNixmITHjfQNWcsPKEVF88AKOPeZ_qAcp8MdFu03PPbsiEmsLpkXJOKa1kM50OB-mA2WIHu_FeY5o1TDVKQ559pFjogPIUe5p7kts0Sl-xQfel7aEXvkLJfy1aUCWTVBtk9tfi63Qd6JUuLohtvM1ZQfgZxSKmd2Tj-Anv_iWZK_IjPajkrLOyrEzZE6s_-hPt1YcuwZVOK_XBBEkGaSqF9lsknfTpRkadorOOHTynpDt8qwkFlzWmW3etFZ-PO8m6EOFynlnkxpWiPLI56_0fUgQMxoLFC32uH7MIW0aLFWAA0SFmKpGIqm4-02HR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7285144264.mp4?token=TBwjOAZfF-7oswt4O2YBnzwNixmITHjfQNWcsPKEVF88AKOPeZ_qAcp8MdFu03PPbsiEmsLpkXJOKa1kM50OB-mA2WIHu_FeY5o1TDVKQ559pFjogPIUe5p7kts0Sl-xQfel7aEXvkLJfy1aUCWTVBtk9tfi63Qd6JUuLohtvM1ZQfgZxSKmd2Tj-Anv_iWZK_IjPajkrLOyrEzZE6s_-hPt1YcuwZVOK_XBBEkGaSqF9lsknfTpRkadorOOHTynpDt8qwkFlzWmW3etFZ-PO8m6EOFynlnkxpWiPLI56_0fUgQMxoLFC32uH7MIW0aLFWAA0SFmKpGIqm4-02HR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
سوپر گل کریس رونالدو به الخلیج برنده جایزه بهترین گل فصل لیگ عربستان شد
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133152" target="_blank">📅 00:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133151">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/133151" target="_blank">📅 23:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
🚨
#فوری | پیر دوسی، خبرنگار ارشد فاکس نیوز در کاخ سفید: ترامپ در حال برنامه‌ریزی چیزی بزرگ و مهم تو ایران است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133150" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حضور وحید امیری در تمرین پرسپولیس  وحید امیری بازیکن پیشین پرسپولیس، برای طی کردن دوران درمان خود در تمرین تیم حاضر شد.  به گزارش رسانه رسمی باشگاه پرسپولیس، در نخستین تمرین تیم فوتبال پرسپولیس بعد از تعطیلات، وحید امیری بازیکن پیشین تیم هم حضور داشت تا روند…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/133149" target="_blank">📅 23:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133148">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⏺
نیویورک تایمز :
🔴
فیفا قصد دارد دوباره ورود پرچم «شیر و خورشید» ایران پیش از انقلاب و لباس‌های مرتبط با آن را به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع کند. این پرچم در جام جهانی ۲۰۲۲ قطر هم محدود شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133148" target="_blank">📅 23:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133147">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm_BJuiNZ4uoBdoXui6WjcbXcP17qObOLNlmgy66Avgnn6LN_w3SKNHoE2JQ2f7YOd6W7r1wEZGWOrU7yUQAPINnWKaWDwsZxKRAZoHeXgEeteuCDVL87yOR0Uv4aH68OxhaH-jlsTiHmF4EFLNl-kzuOmEOg6cg4edvIXznNEhiFy17Wb8IzI5kT8nVsoAKPSC39VFr7N-gfbzFPVSKPGvUaDeWJJeFwwRK9drnnPtTvwM55TJP4QOcuRN1TCxt_rFaTBr-NBqxjqOx_IFwaGcbtWFPoa60cYoZiEtfPfcBIQWSiJFLwMcw8oqYnMWmf1mFBNs02Yu0zsje-TNg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری
🔴
پرسپولیس به دنبال جذب محمدمهدی محبی بازیکن اتحاد الکلبا
/
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/133147" target="_blank">📅 23:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133146">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
فاکس نیوز: ترامپ می‌خواهد دستور انفجاری بزرگ در ایران را بدهد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/133146" target="_blank">📅 23:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133145">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RBiaW40VUZuzTwiRV80R4my85Wclf5tppN1No7Z1jE8c6LD6pKqYIiXfk4m4odKO1Hi_tOkqcLLV7Lf7IgEGrZcprPuy8E3R2rLElOl_bhS0Ko40XhmuphpbrhKbPobf5ih62oCrokUqgO47RzDL6A_N9IVnGaCFpCEEzjYeuWhIV6_nNlwg373VqUMPAXYYRTb-E1yZqYn3Uid20WqU6Z6bNqkZyVZIYK2b2XFeHE7dpWLjnUgm73aQViw_iCQykOKW-FOpoZ-ZKbUhEQ90YZP6TQ-0nrbMCk6MJFvO_1kzyC9n0GyuWQyovCAug1lwOxMq-_itAKksLmPllCMRag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
|  پیت هگست، وزیرجنگ آمریکا هم پست ترامپ رو داخل صفحه خودش منتشر کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133145" target="_blank">📅 23:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SorkhTimes/133144" target="_blank">📅 22:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133143">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
ترامپ: شب گذشته ارتش ایران یک هلی‌کوپتر اپاچی ما را در تنگه هرمز زد و خوشبختانه دو خلبان زنده موندن و به جای امن انتقال یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133143" target="_blank">📅 22:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133142">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
ترامپ: شب گذشته ارتش ایران یک هلی‌کوپتر اپاچی ما را در تنگه هرمز زد و خوشبختانه دو خلبان زنده موندن و به جای امن انتقال یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133142" target="_blank">📅 22:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133141">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
رسانه‌ "چمپیونات ازبکستان" در گزارشی اعلام کرد، جلال الدین ماشاریپوف که در بهمن زانوی خودرا جراحی کرد و تلاش زیادی کرد به جام‌ جهانی برسد به‌دلیل عدم‌ آمادگی این رقابت‌ ها را از دست داد و یک بازیکن دیگر جای او را در لیست ازبکستان خواهد گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133141" target="_blank">📅 22:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133140">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiosCZwvmeSFck9forGbRv9giz70NEUGgvd-YNRqPGc0A4rGLr8RNEcHx2XnTV13kBaNvF_w3K-ulplJoQcAhsn-157WSgyCT7LKctaljCho3GrAXMBCBq4YH5Xn0u8vUZORm71ju_GHtw9t-Cp4kQgr0gA7_n8nAb_jryeMby5xFgc-726dLj5u__X4PtFDcyioNl4lRVvIUgUx12HAueE_IPT858TY569Ee4Sx-Rn_tMfDPxV5bYGVEmAJ0WG83YkOpkna6VWJ_6jf6VIxhyqOWygRD6YboLvsG5QlZisAf1tjx6mlSmXgFYcF0GBpKDEgS_Z_WRwlxIJQZGsmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان: بالگرد آپاچی توسط پهپاد شاهد پرپر شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133140" target="_blank">📅 21:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔵
⚪️
افسری(سرپرست گل‌گهر)
:
◻️
ما نماینده‌ی ایران در آسیاییم و توی هیچ تورنومنتی هم شرکت نمیکنیم و اگر هم غیر این بشه ، شکایت میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/133138" target="_blank">📅 20:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133137">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRYf4Nl11Kx6-6Y7wGc1y9hheIc3Y28CgyiFrVjTxPUPA_CaTnjVBv7wx-QGr5Jy8NQkHDGZ9jat2_vbVQKfKXKnlr8nI9pv-QlpnbcrhDQFZonLrInNid3KC44BWPRqyImWoUBaRcTkUQMsAYZ0BJzDMKorC5uGtuBpHC5zL-UFaRkGN5G4c9fgbzGnVyyTUYQbSB9lYzsFyFon08wICGb4a76q-HxpTFY0AQiY6saxJAo2PjwIqCHkg5CsRI_LN-UjqeFSwzgbvYWqJD6v4Pw7TOs1k0uaIxukYnhFP5TqYYn29rjKfkSK041inqDg6wxC2SfHch8N5JfU7tr8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
شمارش معکوس تمام شد!
🏆
تنها ۲ روز تا شروع بزرگترین تورنومنت فوتبال باقی مانده، رقابت‌های جام‌جهانی ۲۰۲۶ رو در سایت معتبر
اسپورت نود
با بیشترین آپشن و بالاترین ضرایب، همین حالا پیش‌بینی کنید.
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
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133137" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133136">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3d7HjZmAuX8KHYIyl_8qYr7134EEjhj-poKnEP-GtmaanN7W6KDnxD3wd5S5km7RVGJ7d31qgLrPd_95ZKkH4-K4aN-i2uooPYwX2wXaCno3n2NPSsd_LWo__pMvc5X4b4KcapZj7PKEgvWwtyeAv0vlbFmpSGLV005HT0FztZHEPrIhgNaqiFwmANqpBkjDy-ZkJv9kJCDw_O30pILR166Y8A9MrzoIOzxnSFMVY8yLo8INor2GxcWnW2GMBgxMAmIxPxCIK6U7nRg-_pCo8aRBCm6Z9Ttef9MdrKI35XTXzB6O2mCFU5NAUFyxz223rXs5RrrAFPrlSrVphSXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ: شب گذشته ارتش ایران یک هلی‌کوپتر اپاچی ما را در تنگه هرمز زد و خوشبختانه دو خلبان زنده موندن و به جای امن انتقال یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/133136" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133135">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spVjGtJREaEd1NG2nszWXh6jQxW6xOh7_cjKL2FU45hi0X5W90Ndz86eqABtXs5yGBn9d3_4Fs5LrDpqdDbXsFv07XN3ifurjg5GdOJSS7PDrbP54hGqm02npdofgF3DyXwVrnMpG3oNVUp1ObRfewP_ksemfjKJzMYeBjz-ri7BcYqadEcUL7OVRWMxEtrYJK1BQFjdtTFfZW2Ci0fGwH8xYyObfP78P9iJ7NVn_kVYnswqQxTCqqgBj-g_Gy15xVGtL4IbHOqvOQUCq7KQakD7w_9fGh1gFIQ3uooKMvFQKcxw3fbcQwDLPbmSNzLtoqLDkPtB9fE8arL5_sdbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال افزایش سهم بانک شهر در مالکیت پرسپولیس
◻️
بانک شهر پس از واگذاری باشگاه پرسپولیس، با دریافت امانی سهام ۳ بانک دیگر (اقتصاد نوین، رفاه و صادرات) سهمش را از ۳۰٪ به ۴۵٪ رساند و سهام‌دار اصلی شد. حالا خبرهایی منتشر شده که این بانک قصد دارد سهام بیشتری از اعضای کنسرسیوم، از جمله ۵٪ سهام بانک صادرات، را خریداری کند تا کنترل و نقش تصمیم‌گیری‌اش در پرسپولیس بیشتر شود. با این حال، هنوز هیچ تأیید رسمی درباره این تغییرات منتشر نشده است
✍
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133135" target="_blank">📅 20:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133133">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
اینستاگرام پلاس ام رسماً رونمایی شد و کاربرا میتونن با پرداخت حق اشتراک ماهیانه ۴ دلار (تقریبا ۷۰۰ هزار تومان)، به این سرویس دسترسی پیدا کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/133133" target="_blank">📅 18:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133132">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNJOa5OgqX2x1bU1Eq6AbBQ0wygb29eRYqdXFFjYd4asV-mznjQjeEniPYE-CPhnMuBMrOO38u8DprYWSbQFLjLLMsRZ-qyr29Ejpoqh5TAPxzRzfHFY_rN02RqXrmRl2tLBTSJyjPkFWVVf6v1M_sfa5Ph9uJjbyFscqy6IQwsXKaJUVf0Yk19a_9L_86eo_GelutyonR5hh5ODEkXrAwqVdHMCO6I-hvuxl72RL4kK8KPW0Ae0_j92NcX6UqexdwQzYrj5lGN5VufGU8uWZiNlj__MqhpvfpibmtUs8aXwI4_BPiJr-gsyBcIT8oKIr5ETD0wvjid-eDzhsqsV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اینستاگرام پلاس ام رسماً رونمایی شد و کاربرا میتونن با پرداخت حق اشتراک ماهیانه ۴ دلار (تقریبا ۷۰۰ هزار تومان)، به این سرویس دسترسی پیدا کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/133132" target="_blank">📅 18:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133131">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
💢
مدیرای باشگاه هنوز نتونستن با سروش برای اوردنش به تمرینات ارتباط برقرار کنن.
🔴
این درحالیه که سروش بیشتر مبلغ قراردادشو دریافت کرده و کلا 10 درصد طلب داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/133131" target="_blank">📅 18:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133130">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
مطرح‌ترین غایبین لیست تیم ملی: سردار آزمون، احمد نوراللهی، الهیار صیادمنش، علی قلیزاده و محمدجواد حسین‌نژاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133130" target="_blank">📅 18:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133129">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/133129" target="_blank">📅 18:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133128">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">#شفاف_سازی
❌
از بیخ و بن این خبر غلطه تاکید میکنم پیمان حدادی هیچگونه جلسه ای چه در رابطه با سرپرستی و چه در خصوص تبلیغات از این دست موارد با خداداد عزیزی نداشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133128" target="_blank">📅 18:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133127">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
محمودی همراه با تیم ملی به آمریکا میره و اگه کسی مصدوم بشه جایگزینش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/133127" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133126">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
آقا کریم در تمرین امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/133126" target="_blank">📅 18:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133125">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
یک تراکتوری در رادار پرسپولیس
◽️
با توجه به نیمکت نشینی صادق محرمی در این فصل در تیم تراکتور به نظر می‌رسد در انتهای فصل از این تیم جدا شود و با توجه به تمدید احتمالی اسماعیلی‌فر و حضور مهدی شیری در پست دفاع راست تراکتور صادق جایی در ترکیب تراکتور نخواهد…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/133125" target="_blank">📅 18:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133124">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
● آخرین خبر از خارجی های پرسپولیس
🔴
• دنیل گرا تا ترکیه خود را رسانده اما نتوانست روز گذشته به تهران سفر کند و به محض باز شدن حریم هوایی به تهران می آید تا در تمرینات سرخپوشان حاضر شود.
❗️
• اوسمار ویرا سرمربی این تیم هم تا آخر هفته با بلیتی که باشگاه برایش…</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133124" target="_blank">📅 16:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133123">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoD3o1z8VGBwJUA_4GNYX5xkgGqV0XvPohjrRF7hTYD7FpKvUBzDmf-C0DtlBRl_zGRc9pD63pIpS9e8nwl8ef85ngyUolK6iVG4nrhU1fMG-r9vHiO_aykWFiMKIpfXvV46G4V3qwLqHp6jMvD4uYABz3G58Yumzgn7mwXMxXmEFWLYru-4efrxP7I1__dg3B2e4dpcNrE_xl36HNBdw4Fct2AV_LVngOV5VLol5pYlifRHitI8P0dWqGvEEiovJgwYuG0SkJdIrDmpggXGYDn3yJ8rf4k5j4rj83xww3fD-yQJb58I7Cj8O0iNL0IjaD9VpiwYB3Ck37ExIOGRSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / اسکای نیوز: ایران یه پیش‌نویس جدید برای آمریکا فرستاده و گزارش‌های اولیه نشون می‌ده طرف آمریکایی اون رو قابل قبول می‌دونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/133123" target="_blank">📅 16:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133122">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🚨
🔴
به گزارش رسانه «سرخ تایمز» و با تایید مسئولان باشگاه پرسپولیس کسری طاهری مورد توجه باشگاه پرسپولیس قراره گرفته است مکاتباتی هم با باشگاه روبین کازان انجام شده؛ و قرار است در هفته های آتی جلساتی با ایجنت کسری طاهری برگزار بشود!
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133122" target="_blank">📅 16:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133121">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
یاسین سلمانی با عذرخواهی از هواداران به تمرینات گروهی پرسپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133121" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133119">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
پرسپولیس و مسیر جوانی در تیم
♦️
شاید بعد از چندین سال بسیار واژه مسبر جوانی برای سرخپوشان مهم و حیاتی باشد چون تیم از لحاظ میانگین سنی در وضعیت بسیار بالا قرار دارند و شرایط ایجاب میکند که در فصل جدید به جوان گرایی رو بیاوریم تا از لحاظ سبک بازی هم شاداب تر هم بهتر بازی کنیم یک فصل جدید و نوین باید رقم بزنیم و دیگر نمیشود با بازیکنان سن بالا مسیر را ادامه داد...
♦️
اگر بخواهیم قوی تر ظاهر بشویم نیاز به یک رنسانس بسیار مهم داریم که باید مدیریت و سرمربی تیم روی این قضیه حساس باشند و مسیر از فرتوت شدن به جوان شدن تغییر بدهند موضوعی که خیلی ضروری میباشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/133119" target="_blank">📅 16:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133118">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt9niHrI6e4MU7-pmBcHH4_TFfjvT9JV2vexl36YpfXSNOKgq0xhYOiV9YU75YJhgILQsZa4xjufoeW4L7fDgd68iB7oUtoOGqOBpGYvEspGOd7ApyDVgB04OTKJz_Jw37v89jHsQxM4slNxLWy3UoZ5id2H6WKeIwnP2opWxD9J2-ZC4ToJZvBUUPc16lAwAZYoASOOdGQqmMwgTvjYj2nm7DlJwkW9FZTGvmwc3_zAHQgUc5QAI2Tg-pXsrOnZyEd362eJPhzgvKPcMcsKSo10GQLRS0AUuEYvXetOr1hkGgtcwW03FMs9Qqs41q5i31kDJJ8S77stA_jj1K8Bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دستیار اوسمار به تهران رسید
◽️
جولیانو والیم، مربی بدنساز اهل برزیل که قصد داشت راهی تهران شود و روز گذشته از عمان برای پرواز به تهران اقدام کرده بود در نهایت امروز وارد تهران شد.
◽️
این مربی از فردا در تمرینات سرخپوشان شرکت می کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/133118" target="_blank">📅 16:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133117">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf3nvMOgQ3J_zRF1Q_I46uypncng_4E9Q8Mj0n7ZWoRnmyTYlicTzON24_z3yqlijrxHB18jbmuVpG7SuZO1NZDwHKQMpaw23ZnY5ec_P48Fm1W_4jvgz1E3UOYiM7-5oPmxldQ9JtAHzRvR767MGJdiffuhp9HIzrKOYDR5kZzNbcKb5JOucrmjfwFmlVO7cMGkWO94UH-uwcLWcWDtbc7_97Cui2AVReOu1UKJpmVjD6v7iIrCL8rHs6dMlz_VpndkJx4pwGkCSYunybRDe7oz2tsR00zESoBkDFhWXR_uUmUi-kSihyXNdhQOXQG9n7H1rUX6PJCbSkPyG-Z1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
آقا کریم در تمرین امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/133117" target="_blank">📅 16:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133116">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
فوری : یوتیوب رفع فیلتر می‌شود
🔴
مصطفی پوردهقان، نماینده مجلس: وزیر ارتباطات در کمیسیون قول دادند که فضا را به شرایط عادی برگردانند و بعد از رفع فیلتر واتساپ ، رفع فیلتر یوتیوب  هم در دستور کار بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/133116" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133115">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv2r7rVmHWAlJKapQWcnlcrdOcAvOkAlpAN6RhALVA-rGDmYnVLSPws9F6evStbTLLtjZF2S4f8wtwq9gvwbLSrgm9TZoyWxvJ4zcP0bCwqzeRQAyJQBJtGiDXz-1xj44dDbi4eDM_BPs7Us24jUMmCmP23b4V-nAGWlY5uOCQnmMzLv9ORXjFFxax-D0hYxb4fdess7sCrHyMYROZoGWhPlMc_P3lP_MXHg_keKeazFOdXOgtuJ_FtrSdBgwnU5uzLyevrAR-NbPlGBogq83qwUA302MzjGTuNp7Qk3c-srgsAV9fpQmTkfMUpne4fjE8MCU_aaf9x0l1SQRgyShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
باشگاه با ایجنت کسری طاهری مذاکره داشته و شرایط جذبش رو جویا شده...با روبین کازان بند فسخ داره و میشه فعالش کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/133115" target="_blank">📅 15:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133114">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_koj8wNDCAyQMgnjLa7beApNP4EtCiVIFljxfxM3mcz9CHHCpOdIWqom--1ENJAlOOe4WOZhJa7YEXjN7Bchno6Bq2Ls3R25fhwgAibQ1DdrrQVTuXqFgbTB5xKTW-zmN_nEc1yLmL6uEQYrr8WGvor1zAbMOKWrFcgx8-GSR7maE4dLEM0-O-WIXPLsfNE3NLJS9heX3SMbhCKvF4tOLdEXkaP4sFyjZQv3bsumiAhHjmxvtWFImOcBStk_A97I356uSXRrGL91rHuSnI-muX3puZiSzhL9YkqGPULuLCbcg7EONGb25X5wYZ1qpW2bX3ZBR7L6WemE4KQ2r8oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/133114" target="_blank">📅 15:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133113">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🔴
پرسپولیس در مشهد کپی می‌شود
🔺
مدیران پرسپولیس در ماه‌های اخیر طرح‌های مختلفی را برای تشکیل تیم دوم مورد بررسی قرار داده‌اند تا از این طریق زمینه رشد بازیکنان جوان و مستعد را فراهم کرده و مسیر حضور آنها در تیم اصلی را هموار کنند.
🔺
گفته می‌شود یکی از گزینه‌های جدی برای استقرار تیم پرسپولیس «ب»،
شهر مشهد
است.
🔺
چندی پیش
پیمان حدادی،
مدیرعامل باشگاه دیداری با
استاندار خراسان رضوی
داشت؛ دیداری که باعث شد گمانه‌زنی‌ها درباره احتمال
راه‌اندازی تیم دوم
سرخ‌پوشان در مشهد بیش از گذشته مطرح شود/
فارس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133113" target="_blank">📅 15:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133110">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbj45pGR-Jur4VxbphmS-O8czyZhlCYLmEJHZhIpGCJlFsoru8X5KI9-6GNI4O6Pou3x71D4jdd3c3zv79g-uSzazR1omKdOPJre8K-ipCKwU5sOW-ZJbbVH1ikaSNcLpGi1doYVwAk-BLgaYWDKIpuEDheXBJ5d0Cvb3KBons3ToJ4HcX-dqSPpmdCeOqp-o1XVdh7Q_MIXiCn5pWipRYh-KDC5ZKD6gHmhRRyDcNKVxk0KuFLxjU_wQ-2rXJWufpuM9oP_QJd3rfEwNFJbaYLH3OBlLmBmd-sWL36iTffUETgzUJBAUC7YbxINSxeJOerNDBZaUtHb08ylqFF-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z61TIbxxogiFUQ-DgWZ5DuyTrvtqMEYkkpyfJK6ewKqmUYwBnT9ZxyMrEI5eMEvUz6ATq1lVDhjhf-y5ALYXq22B3N7TglPGiT0GKRXVlfAkeIUFGHza2jvapqPSKkh-MRSZdLLGLcjvag5fNoyG-_eee1oqidW3KUQ4X-Ggg2aDcW6BId75PCorPupWF_DOJNvyZczx2F5F_0F6VpAVo2zivSkPXGnSxUhk71dy_zD3rfwtPR8Ys67SbJLqLSB3WARfTxes0xgh-7AdD64hWgQwJWh3tfI85oi16OSVim-rDg5mDY1hNvH3ZGZ_PZs0iFlB_S-l-pfH_9pT_lL_BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
انتصابات جدید در آکادمی پرسپولیس
🔺
طی حکمی از سوی مدیریت باشگاه پرسپولیس، رضا جباری هافبک دهه ۸۰ این تیم به عنوان مسئول استعدادیابی آکادمی باشگاه منصوب شد.
🔺
همچنین حمید علی‌عسگر دیگر پیشکسوت سرخ پوشان نیز به عنوان سرپرست تیم نوجوانان آکادمی معرفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/133110" target="_blank">📅 15:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133109">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWMIq-VgWT_O8ZhSIHggt4kdR84tT29XzjmFBLWP9D_xxr-OTzPcY1v5T3Fxo3CsJmD5MqVH_dK_MY8tUlrR_b_m0kYnt8J7pCXpR9c3YwZDbD0OEyRzNYoOYO1ej0lwK1GMlhq3KpoCoHpiBMfOo5Ww9x0Q5zAWFe0es-i6nhHUS7saRs7dBqNI9dn7_RQR1F3kXiA1muqapr07YEkYCVvwa06XFGc7Nj01rvVXgcmN0vjIE6GndQtpPA1jx-8uTODX1VhyuY301nNPv5Bvz8lfqe-MrqbvQruo-8b-MQvBxGephSs_6yYpFxDwueLPCKH3Z4O-0Flz5ThUzWYVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
تنها ۲ روز تا شروع بزرگترین تورنومنت فوتبال، رقابت‌های جام‌جهانی ۲۰۲۶ رو در سایت معتبر
اسپورت نود
با بیشترین آپشن و بالاترین ضرایب، همین حالا پیش‌بینی کنید.
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
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/133109" target="_blank">📅 15:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133108">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
کریم باقری و محمد عمری از امروز به تمرینات پرسپولیس اضافه میشوند   سروش رفیعی همچنان غایب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/133108" target="_blank">📅 14:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133107">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
کریم باقری و محمد عمری از امروز به تمرینات پرسپولیس اضافه میشوند   سروش رفیعی همچنان غایب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133107" target="_blank">📅 14:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133106">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
‼️
مجتبی فخریان، وینگر پرسپولیس که به صورت قرضی در ملوان بازی می‌کند، قصدی برای بازگشت به پرسپولیس ندارد و به صورت دائمی جدا می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/133106" target="_blank">📅 14:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133104">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
✅
پرسپولیس برای تورنمنت سه‌جانبه استارت زد
⏺
باشگاه پرسپولیس: نخستین تمرین تیم فوتبال پرسپولیس بعد از ۷ هفته تعطیلی برای حضور در تورنمنت سه جانبه اعلام شده از سوی مسئولان فدراسیون فوتبال، عصر امروز از ساعت ۱۸ در زمین شماره ۳ ورزشگاه آزادی برگزار شد. در تمرین…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133104" target="_blank">📅 12:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133103">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
🇮🇷
آمریکا بلیت هواداران ایران را مصادره کرد
⚪️
فدراسیون فوتبال خبر داده آمریکا، میزبان بازی‌های ایران در اقدامی غیرمنتظره، سهمیه بلیت اختصاص‌یافته به فدراسیون فوتبال ایران را از آن‌ها سلب کرده و در شرایط فعلی امکان ارائه حتی یک بلیت از طریق فدراسیون به هواداران…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133103" target="_blank">📅 12:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133102">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
هو شدن ترامپ در فینال بسکتبال NBA
🚫
وقتی دوربین‌ها هنگام پخش سرود ملی آمریکا در فینال NBA، ترامپ را نشان دادند، او با صدای بلند توسط مخاطبان هو شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133102" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133099">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
بیانیه رسمی فیفا: دیدار ایران و مصر قطعا دیدار افتخار همجنسگرایان خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد.  در این دیدار ارزشهای همجنسگرایی را به جهان نشان خواهیم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/133099" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133098">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ویلای علی کریمی توسط قوه قضاییه مصادره شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/133098" target="_blank">📅 11:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133097">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEwr1-9E6dSgC6GEVs9HszrzKtVki5Xc-smy0VTKb0XNdkiwE25KaDdgeGpb8Lz8M5KU58ah-n4Jcf7e6jnLgH202V7dh2BuMw3GrjBp1SJwNcHGfvLr76ZjC7vrZlGR0Q4WBccOKGmvW0zjEm_7BR6iEpfi_rqoZLyvL5CS3kuQByFlnM6ZAhaPjURZAa3qeOcUZjpWDJXLd3wi4TXhbJtrXPaJ6EUheXMIwenSELjOQJOIal0OAYSfhP98hm7XErR9GNK2dwn0XaD2eV7ye9S_C3D0yu78aOmiUF9xePOw5IFgKD69VLLNbF1UqzzSHf_OpDV-Pwq_8N74qtCq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ویلای علی کریمی توسط قوه قضاییه مصادره شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133097" target="_blank">📅 11:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133096">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0309c6ebab.mp4?token=WwrwHf2iUXRUmq1vd1GHs-LpE_MqeqsjIHSexfk0Y-0rZbBZIMv8_hY3elzUpTqAyIITxZv7DWReD91_KQ3tZQkXd5A_iGQDrgbL3yzHHHPebnxM658iewdNU4K0VMmMba5CXvrUg8MOw7TSYJtV2bcczQwl6zUsS4XRAIbgf6VbVyUyUnmxPPpAG0C51AOP5bbDr_ivfrwFA3as3x21p1ZMZ1qttqQT05MslEVL_Ogr86ucHTUpsjfBj9-nBb9HfmDjhtkJVWxk4loKTGdHxC8s6pmuySU9Cv3zPd53WXW--G5qRx3_QYqQBrraNSRQMwS0MTGcTFHDbQ_isL0S9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0309c6ebab.mp4?token=WwrwHf2iUXRUmq1vd1GHs-LpE_MqeqsjIHSexfk0Y-0rZbBZIMv8_hY3elzUpTqAyIITxZv7DWReD91_KQ3tZQkXd5A_iGQDrgbL3yzHHHPebnxM658iewdNU4K0VMmMba5CXvrUg8MOw7TSYJtV2bcczQwl6zUsS4XRAIbgf6VbVyUyUnmxPPpAG0C51AOP5bbDr_ivfrwFA3as3x21p1ZMZ1qttqQT05MslEVL_Ogr86ucHTUpsjfBj9-nBb9HfmDjhtkJVWxk4loKTGdHxC8s6pmuySU9Cv3zPd53WXW--G5qRx3_QYqQBrraNSRQMwS0MTGcTFHDbQ_isL0S9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هو شدن ترامپ در فینال بسکتبال NBA
🚫
وقتی دوربین‌ها هنگام پخش سرود ملی آمریکا در فینال NBA، ترامپ را نشان دادند، او با صدای بلند توسط مخاطبان هو شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/133096" target="_blank">📅 11:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133095">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfMryw8EpReLaW2qwd6CFEHODLEixqYpI1q2XexnPOZf1RZY2aMshtRPfgavzR1pWDInhd1JZ62uuIWcnQXrcewn1t63_84OO3lZ_nI03xoGSu_YoXfV-GVrMxCfdFqaST1dzlA-BxcHzUJXPobZc5cYcBISFXolEun8nJFA8ro6hiu8KrZwrT1D8q6ibGCEHaiINQw6VK975ojXo0fuRfoZXMgXSJlb64PBpPyvK5rBMqYnCSggEhnFox7a5ldb-m8QMDIklwVD_6a8J8-X-WPLuqP_3QBM1v-Cm5qKQQT2b06hcWzoWuerfWGUjdBLZg8vDVuVGlvFDtyc5GElQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فیفا در آستانه جام جهانی 2026 از طرحی جدید با عنوان «سوپر شات‌اوت» رونمایی کرده که به تماشاگران این فرصت را می‌دهد در ازای پرداخت 79$ ، نام خود و کشورشان را در جریان مسابقات روی نمایشگر ورزشگاه‌ها ببینند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133095" target="_blank">📅 09:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133094">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
🚨
🇺🇸
ترامپ : فکر نمی‌کنم که به این زودی‌ها اسرائیل با ایران وارد جنگ شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133094" target="_blank">📅 09:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133093">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ynl_XhFSIPYcXrMFY3fDgx_f4nPouEfu_s7a4Sq_BZ9AoJNzd7lus-_ZoetAsm7xODZl2Zs0yHFf1FJ62YrfjIrTf9zTRH09b_0nV91EwfE_7_EOxG-1_xPMU71yEd4nHWujF8sNFkwEvITe8_ida4iVvP8c3djM_Bi8WKqPMMBNnAlyWDnVqbPm5N1TbgmUMzlmotDI8dRFzZQg_xEE38wjBOlZLtatAofQbPJthdRGyd506lbE9WjIjdFKX-S0wrRAQGR9WYCpJ_pn0VsvHuuQOpgZizaB3rKcvK7P9sWErxSP5zzJV6NFEpcDf6zwpRasz-Z74h9wml3cMY2ybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی تارتار: پیشنهاد پرسپولیس؟ اول اینکه هر کسی من را از نزدیک می‌شناسد، می‌داند وقتی با تیمی قرارداد دارم با هیچکس مذاکره نمیکنم
◻️
من به آقای اوسمار که سرمربی با شخصیت و کاربلدی هم هستند، از همین‌جا می‌گویم که به ایران بیاید. ایران امن است و هیچ مشکلی برای کار وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/133093" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133091">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHiPfg0CubnGrPhYGT6gQuRokkrWPhMEyMznpA3wDV2rqWUSgOw_eNEn9pUNfEBQpta-wtt2VD6ZzCcJuoNNgSDkSqWHquS2Tqa3C_iJLUGqzjMrT84x0IQFXL-FxilR3ktdgLFLbkScV4sg_pEqFSvaQXyVygyBWeoXb1caJ2tBsXATZAu2Kbpyg4K0lpkN5oFyu2RjqP40vBeZUdTzREmgQuv3PUCcDsb9Os3uR8WBoSvexCDDcL4_5Sz64hUJYaayMIoUIo3dmduQ6kFmY2BXscPGh0IKtFflExH3MbtVNaj9fObGc54XNqYK1-wVlmsxicJxYEqxiQFDIljBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🤐
دیدار سوم از فینال ان‌بی‌ای رو بین دوتیم سن‌آنتونیو اسپرز
📀
و نیویورک نیکس
⚔
رو در سایت اسپورت نود با آپشن‌های متنوع پیش‌بینی کنید.
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133091" target="_blank">📅 01:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133090">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
‼️
ترامپ: به نتانیاهو گفتم درست رفتار نکنی در برابر ایران تنهات میزارم!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/133090" target="_blank">📅 01:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133088">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❤️
❤️
گل اول ازبکستان به هلند توسط ایگور سرگیف مهاجم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/133088" target="_blank">📅 00:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133087">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57eeddf50.mp4?token=VamOAJSPmDgH-y55fM6CetuvwIN0xy1-7E5RMO4uRvyYgtUR9FVO7nPuoX2ku2xOOUOXiGcIau3UrfeoCk7rEyyIvmiQqTASDUROsH-pe1kdNssDE16Iy6OWg8jSdteWOB7oa-Iyt_K5Gz5-RNZmVgfiGqHFQxLoI36TCZQDWzh10AThMGSYWCGq9hWNtG43GrTQ5z8pNsAK-j-phlib74UmR8Z8_Gyb6BKKrnDDnyWXKsbF_kk81E5FbTKLaTsUmliBziX4L89rYNZN3EiAXYjXZN9MIyU44L1dO-OF9b2Tt7uZpH_5N7UG4HS9KE2K30lOOWL77-s99vRMk8DjIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57eeddf50.mp4?token=VamOAJSPmDgH-y55fM6CetuvwIN0xy1-7E5RMO4uRvyYgtUR9FVO7nPuoX2ku2xOOUOXiGcIau3UrfeoCk7rEyyIvmiQqTASDUROsH-pe1kdNssDE16Iy6OWg8jSdteWOB7oa-Iyt_K5Gz5-RNZmVgfiGqHFQxLoI36TCZQDWzh10AThMGSYWCGq9hWNtG43GrTQ5z8pNsAK-j-phlib74UmR8Z8_Gyb6BKKrnDDnyWXKsbF_kk81E5FbTKLaTsUmliBziX4L89rYNZN3EiAXYjXZN9MIyU44L1dO-OF9b2Tt7uZpH_5N7UG4HS9KE2K30lOOWL77-s99vRMk8DjIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
گل اول ازبکستان به هلند توسط ایگور سرگیف مهاجم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133087" target="_blank">📅 00:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133086">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
اوستون اورونوف یکی از ضعیف ترین بازیکن تیمش در دیدار دوستانه مقابل هلند بود و دقیقه ۵۴ تعویض شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/133086" target="_blank">📅 00:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133085">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
🔴
غایبان پرسپولیس در تورنمنت کسب سهمیه آسیا، پیام نیازمند، حسین کنعانی، میلاد محمدی، امیرحسین محمودی، علی علیپور، سرگیف و اورونوف هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133085" target="_blank">📅 00:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133084">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQIuVC_tNU57QbF_CtO5NfGK-30oUJf6Un8sNZjfQ6MS6lHjfitphJjNn5kkGx0xSOL2XZoFYVYS-scTW7jeCVNBe3ZTv2RjZKrgWlmimRcjdIE4eQThh7-1Ird6JoXlHDIFglcCnVwAVy6qO5dv1JmRtzedQpgHFgEqr274ZiHNbf7h9Qn6meGbNYEXP2jY3Rt7c2jKEDkDso7VgXv56FN2rMzT8iplqAbrmI48aLUNj1MwG-aokEiuxxSJyZr1M3qNEahXUUtzCxmvJ8Abyi1IVND-WU_DfGS75e6HN_dNKSCtc5L8E3huM2K-MEayrYDOgRnI-XbWeCLDyQDgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اورونوف در ترکیب اصلی ازبکستان مقابل هلند   دیدار دوستانه
🕙
ساعت ۲۲:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133084" target="_blank">📅 00:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133083">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
🇷🇺
شنیده می‌شود که باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده، هر باشگاهی که این بازیکن رو می‌خواهد باید مبلغ یک میلیون دلار به عنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133083" target="_blank">📅 23:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133081">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
در سکوت و سکرت....  فعلا،مذاکرات داره خوب پیش میره///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133081" target="_blank">📅 23:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133080">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
اوسمار کراش زده رو آریا و لیموچی و حزباوی و باشگاه در تلاشه برای جذب شون راهی پیدا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133080" target="_blank">📅 23:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133077">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
حمید درخشان:
🌟
من خودم خداداد عزیزی را سال ۷۵ به عنوان یار کمکی به پرسپولیس آوردم اما الان نباید او را بیاورند چون بی انصافی است. پرسپولیس این همه پیشکسوت دارد، از آن‌ها انتخاب کنید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/133077" target="_blank">📅 23:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133076">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
🔴
حمید درخشان:
◻️
کار فدراسیون فوتبال و سازمان لیگ درست نیست. اگر قرار بود که این اتفاق بیفتد باید بین ۶ تیم بالای جدول یک تورنمنت می‌گذاشتند و آنها با هم بازی می‌کردند و قهرمان این تورنمنت می‌توانست به آسیا معرفی شود. متاسفانه این تصمیم شخصی فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133076" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
