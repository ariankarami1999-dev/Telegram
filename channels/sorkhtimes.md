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
<img src="https://cdn4.telesco.pe/file/nt0QD6r4PMY3f9C8KgJSoDVGyCNedM2O3oaS8GUg_FCunRK_2YTmprsmGLK-zY_Tpb4H9Z-KsQPaVua3X7aob48tq1AwA_YdlSPVHz1Dt11NNmJG4V2TwQMSGEvaM0cM_WKedHFwfh5_8gS6IHj6sJjxK5Sf0U1ws20mp2Uk-zjag_jF0cITtqLzFXhTyC2ciUjmKwQDf7Cs4FH9iYyGWgQkPZv1XkLYxN4J7OciVehMzDz1RnAi-zooXMLnlMz7aQfIskXozYiA6Tr_dysKM2DZOanfi0F_12wKH1Wy5hyOgAex_-PuHAKzdSOaC1_mjl_7YnhnQFsFz0RCAGEudA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 23:31:04</div>
<hr>

<div class="tg-post" id="msg-140332">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJdxeteDII1kJv-u87poPWgFgfX1ArYD0JbkS7ssOmjTSYEe0krQsm94xhrgoEChzwaZ6cqlffM6WnxnUGX5-H8As0icnCN_bz9gI78j3LCngYEIbVNXqR4ExYrK_Z6ADVXAUkato-soOoXsNIZlCmkOH-_7Nh6sK-haPI4hAFlxFi5iWFKb1QHjrU_ZH9k47HkXmGNm2zTAOKt9wkD67V_GAEoI7usuOuVhpiqp_8yKpV6qEJlw3AzjmYc9uPtEA_gHXz3nW0B3xdNbOTlt2VvlOjI8ZVaMsqSOCI_uA63BIAgKIq6GRHWHetWAUaLNeGyXVqAGnQKejPaHv9aosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
مهرداد خانبان به کادرفنی قلعه‌نویی اضافه شد
❌
❌
پس از پایان همکاری آندرانیک تیموریان با تیم ملی فوتبال ایران، کادر فنی این تیم با یک تغییر همراه شد و مهرداد خانبان به جمع دستیاران امیر قلعه‌نویی اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/140332" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140331">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABez6zyR-YupFhK4txhvfTbvzyjDLhVXE_qTggChVPBHVhPM6stkwW0Cs-TTMdpen-_r4GZJWa0d3kqQXMFoAFEYOiGZGLVHhySlNH0CuY8waa0pGxaIZVMirKYhGflfiG_wEGEn0qapzOhUjNbmSDWIMWllGJ2S18q8k8ZC5NfF7ZPLhEBQvVDqNbhdC2Vq-yrb1A3yl8t-7hzUKc6WzY0205Ka7EwCDKfJzbm-Ngd78Lk9Y4SWM3s_kB7l2PwlFLoMyT77aL1bmJIwauJtdlciPIlxuvK5XC06_Y54QyiRklYd4v5F1Y7AUQVHbjzq6o9pQC0MNNLnjHZsEpNT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
خبرنگاران عربستانی: کریستیانو رونالدو نیم فصل در انتقال آزاد راهی فنرباغچه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/140331" target="_blank">📅 22:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140330">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nauoFQd55XF7QSCgm6rSHz-6EswmODJofCLWXcZLTTu62VZ0risamVvxYdj0_TGRVt74ub6ao2hyzge9O4jBvzQIIaATWJLCuJ9XDWZnbJr7JbEpEdqHIsaxYRbCmqrzxf7ft-EuYdYNuwnVi-uu2LUDRyKM3Cy7QLc7h6M8yTz9espf3LsmG1Xd5es-s4a5xQuQHiB-OoIPSaw8PD4fD95l44jGHwUwM8LSbT6PxN-xASOdUnruvKNv8GtWNckRbrex4clNHJ_yYnrSxc27XyktMR9l_r9jSGcL2fZ9nHwzGnVEl0s-iT3NZ4Va7jR4hO9QNDO7RIuJ7CDHNGLLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/140330" target="_blank">📅 21:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140329">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/140329" target="_blank">📅 21:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140328">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
رسانه‌ های عراقی: باشگاه پاختاکور ازبکستان با ارائه پیشنهادی جدید به بشار رسن قصد داره قرارداد این‌بازیکن 29 ساله روتمدیدکنه اما فعلا پاسخ مثبتی به‌این افر نداده. اولویت‌بشار بازگشت به پرسپولیسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/140328" target="_blank">📅 21:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140326">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8hi8jOK_IvUkunsIeRcy766t5o0Km-kb7u-PM_MDzX_GM4Hhqip256UCHeSXKr1ux8W_FiReQ07BYJefWE6ABOMrzbuqUvnwGvjV3_f2gQIFn8AgAKK2r5pwRU4_WmmCoWjQJAIfcx0bQ04vTS0M6TIxACXQo8jMG_B2tGCNeHWN-P0UgVpaqM0epADGwtPSrZWoLNucebaQbNo5B7rXMhrwKQNcGe1deTqnO13lHxBwsdtrlWXVJcIIBic2bK1yA1-dI6QL8Ptejkdyu0YyEI2n0rKsPtCpQeZO8dKwwARuyZ9riYNK28Bk2U9dWmoUenffYfymsN9d2nQsTPThg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Marseille -
🔵
PSG
⏰
Tonight 22:15
🏟
CEPAC Vélodrome
🔵
مارسی با شروع ضعیف فصل، در ۴ بازی فقط ۳ امتیاز گرفته و ۳ شکست داشته؛ پاریس هم با ۵ امتیاز هنوز در حد انتظار ظاهر نشده است. در ۵ تقابل اخیر، پاریس ۳ برد، مارسی ۱ برد و یک بازی هم مساوی شده؛ آخرین تقابل هم با برد سنگین ۵-۰ پاریس تمام شد. از نظر تولید موقعیت، پاریس میانگین ۱۸.۷۵ شوت و ۶.۵ شوت در چارچوب در هر بازی داشته؛ مارسی به‌ترتیب ۱۳.۵ و ۵ ثبت کرده است. با این حال، ولودروم و حساسیت «لو کلاسیک» می‌تواند بازی را نزدیک‌تر کند؛ انتظار یک بازی پرفشار با موقعیت‌های جدی دو طرف می‌رود.
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
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/140326" target="_blank">📅 21:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140325">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd1-Iqw9QV36oSfmDw59MB9EbdV3qzDzNFG2-8Ps8UcC8ZXVB3iaJ6PnMo6unvZPihPzaHye4sZ3spT-YkmLcHXE4m1enq0ZWn08mV1piQ3Pk0qEj_kSyqVG5z-DYjd3WxS1RP8XLr-rTehR9_03Dhn6R3Pxo3ax6nznWakQ7-D85XpgaW4L3Wpmcd5RnlqBKVhOpGyrKsZQ9ystwY2W9CjA6sCADo_hZwsXS4X9nDdYrjtJxoS8SUADNAAetcYVrqCOTT0fBG7nTZNLS_yXfsLDlg138B2RamuEbTESQxXAfYXTeHOFzrMX6UHMHRJHebXTnfQBe3mNg25YdiZlew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/140325" target="_blank">📅 21:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140324">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/140324" target="_blank">📅 20:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140323">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/140323" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140322">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/140322" target="_blank">📅 19:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140321">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEtwTFdxdlxG3xym4XTJmz9jEMTRJGDmt43YM_MuGcRapLuOewLGtBUaMbwFvewhYxNj0ZS6ieb7i6KLOtCZ8BZDHi4-Je7PtOZu_TN21L2udVi1pQq1zP16nmtmxW_nKERHm7aPFKVffF1Q4iDyeN07cznGeTBxjUJFgJBbydWopjJQq3GOuGm4BZDqaJAc0FO8YyqnD4oDIwqMU-sSSe8CWXHrmbphf9X2_jOZC3rEo2e27Dflh7R-fxqLZ_xtRAfw2zuH3hyBxzSElqjvMJEz5ZMR4isC0VdKaTfjWLNZj_D3PEV7ihMPFJ_yVgUEzdlxANWwSNyR64IHVXIjFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
گزارش تصویری از تمرین امروز تیم ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/140321" target="_blank">📅 19:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140320">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbqgqlBu-wPP-wZyceEQYr3Hm_IWJH1_r-l0rgkc0Y5P4mmu3SjGx-in_Ptk9SOZwBhLGlyurrSU-ojxx6l9KsTiw5_271mcQkE49y4A04GnYRie5lObGxIqqupHE4qvB2MmJNWdfTrmA0I4ypOArXaUuEBV-2s7Ei-yYwBy3Z-d8mRyY2toCpOJtzh81Z6maEVF_vwSoEepgZSUlEvL7oRQYBq6uSKn9H5ow2wSEWDTxCioQg0ew2nXVCCF9yKulMbzIaRyGwpj0Mm1pj5bMh42Uqm8TW0H3hxjaYDBv9O7rW_yNq0GZjGOIOl-8MRHf1UuZ_PZT6epEZDWO9hGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140320" target="_blank">📅 18:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140319">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✖️
✖️
✖️
🇺🇸
ترامپ به فاکس‌نیوز:
❌
من می‌خوام با مقامات ایرانی
🇮🇷
مذاکره کنم، ولی چالشی که الان باهاش روبه‌رو هستم اینه که اونا مثل موش تو سوراخ‌هاشون قایم شدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140319" target="_blank">📅 18:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140318">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/140318" target="_blank">📅 18:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140317">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
فووووووری ...شنیده ها
🔴
قرارداد استون اورونوف با پرسپولیس با دستمزدی ۲.۲ میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/140317" target="_blank">📅 18:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140316">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
رسانه های مملکت گفتن آمریکا مجوز لازم رو از چند کشور منطقه برای شروع دوباره جنگ علیه ایران رو دریافت کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140316" target="_blank">📅 17:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140315">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140315" target="_blank">📅 15:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140314">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
❌
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140314" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140313">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
❌
⭕️
⭕️
فوری/کانال 13 اسرائیل گفته آمریکا و اسرائیل تو تدارک حمله سنگین به ایرانن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140313" target="_blank">📅 15:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140312">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=DTF1gMgSVfRPpIrg6ZIwFKO0NxkJLyjxQY0Xx_Tv5jj-1xdLiKxeaxPbV8Y7yTeHtiVu4w2pDT6s8dZ_wPM86w70xTUnLyJoj6Iu4Bx2FqeUY_7lHAMRqFOSvrnpdbom3FclAV052HUy1skn0DcAzh0URiN7gl9GPxgxQXRyZ1l9CyMF1FlMp7hsw6XVXQlSkydtmvY6OY5mi90jwwFF5cFn3UxVj6MqQXoNzgVSEdw_24ytul8UNL4SBjDVOc1pbGRrSqe9fgMTU2HMbuAHupHisqmS1iJjOdr9Soko03WC9kGflJV7LLeeZQQR2I3jmGvhDavfd7SW2f7yMQUk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=DTF1gMgSVfRPpIrg6ZIwFKO0NxkJLyjxQY0Xx_Tv5jj-1xdLiKxeaxPbV8Y7yTeHtiVu4w2pDT6s8dZ_wPM86w70xTUnLyJoj6Iu4Bx2FqeUY_7lHAMRqFOSvrnpdbom3FclAV052HUy1skn0DcAzh0URiN7gl9GPxgxQXRyZ1l9CyMF1FlMp7hsw6XVXQlSkydtmvY6OY5mi90jwwFF5cFn3UxVj6MqQXoNzgVSEdw_24ytul8UNL4SBjDVOc1pbGRrSqe9fgMTU2HMbuAHupHisqmS1iJjOdr9Soko03WC9kGflJV7LLeeZQQR2I3jmGvhDavfd7SW2f7yMQUk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
| فوری از برنا:
⚪️
❌
ظاهراً عباس کهریزی از ناحیه رباط صلیبی مصدوم شده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140312" target="_blank">📅 15:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140311">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140311" target="_blank">📅 14:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140310">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drmUpS-ARIcc0V4h3swJH9UiQNA6rTM3iYGCH68N68KVbhccgHClni6CspAe3sJ_JOiG0YlS41xjgj6669cicce5qbSjbVCa1UzuU6kdNImyCBUjwOM9P9y_I082lE_57NYpGY7YUtCH8GwgSBxq-r77ptmBxNwt7HKXyM688RWpOrf6BEtUoS6qeiIh-qIp9xyUjfIQDiwqg4itmMq2rwSWP05jH1KCSuqIoBU6sDIBDQO-y-heMtGyONmdtrqMhp1j7bFCADlKW-bWHArprcvFP2eXSixkXFQz_nrrw9BNcv8ULMYwkY4JRBSOnwRxO4FVIlEQRWuxIEZXc3hfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مادرید در انتظار یک شب داغ؛ اتلتیکو یا رئال، کدام‌یک حرف آخر را می‌زند؟
[
اتلتیکومادرید
🔴
🆚
⚪️
رئال‌مادرید
]
⚽️
اتلتیکو با بازی فیزیکی و فشار در میانه میدان می‌تونه ریتم رئال رو مختل کنه. رئال اما در انتقال سریع و خلق موقعیت از کناره‌ها، تهدید جدی‌تری برای خط دفاعیه. دربی مادرید معمولاً پرتنشه و استفاده از کوچک‌ترین موقعیت‌ها می‌تونه سرنوشت بازی رو تغییر بده.
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
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140310" target="_blank">📅 14:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140309">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
اوستون اورونوف و ایگور سرگیف از پرسپولیس به اردوی تیم ملی فوتبال ازبکستان دعوت شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140309" target="_blank">📅 14:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140308">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
✔️
#تکمیلی؛ فرهاد مجیدی سرمربی سابق استقلال ضمن تشکر از حدادیان‌مالک‌نساجی آفر این باشگاه رو کرده و اعلام کرده در ایران تنها حاضر است سرمربی استقلال و تیم ملی ایران شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140308" target="_blank">📅 14:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140307">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">😰
مدیران نساجی دارن با فرهاد مجیدی مذاکره میکنن تا این سرمربی جانشین مجتبی حسینی بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140307" target="_blank">📅 14:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140306">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNigPGC7cn7g-_wj-AaUdNGdkq-bNDsZ-GynvHwoszQqm4BZo6nwyGtm0ymb5Gun5jSiM0MO31KnCw7dDdLZM80yT81oq9vAXVmsc8EkzaiTm7-wSVEymgHFcho07NDVVDCFje_RjzOFFyZdJNbNuSyWw5fPRYlRFxbM2NzxVGveKExRdtVqx3NJq3NDyNcWxdGH8viAuSF0HG8SK2lJhV7uiO3gBnhsRZ5BJWLB6wlcpbmNoesyPIGJWdy7C5i4OZRZ7A-R8_vFD4GrQm-LAof61xG6KbnAd_La3mfAuzgzhR1Epkzp829jGMMnt5PpKUmGRwHJFWBBPX8RVa7gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا جهانبخش قصد دارد در پرسپولیس به فوتبالش پایان بدهد
✍️
ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140306" target="_blank">📅 11:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140305">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6v9Xs3hNZ9602BmbefK199h-C7mr2hOUHp2ScIB7ejHm8tMo2-aE3OkpqW1sf8F6Nz8MUJtI7TcTuC6p3D-jdiS9FDQWEkPmMwD4iPfQ_zeMa0vU6a1-QSS1ZVYdz9sRd-tOYcIZ2TbuyYTTNCB77vcztXS3YyV2QxSmD1u2kedgZuyNs8TH-C1zRwoV1A8Zzs950hbko09aO_7A2bpnSQxVXoJ7YYvtUGFgPKVp20vbBEpWBDvHrhwNruC9erK7GycNq9i82CINJxoS1HggQznws-u0CdjbaJWt23uKF4Ooixs3n0Fww6dfbO-NfpI-4Sr_ARWU0CGQej_MZCt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140305" target="_blank">📅 11:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140304">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZCCa6YmageUjgQ11s9uKPYfRPCKq52xIJph_INt9SIJ3p9F3nFoO2z6X5ZKzQgeSlja1FJzB6kXLE_KMfdqpGF9zYsmFYbFsg0pF-XJ_i1Kyve6dhbTXXanUYB2_pTaeXU6ppVtllccK6-xGlUUUUIG0D5XsB0jNcxmQiiTSEspWdvwNx8cURbafEWxwBM_An06FDOwP4riDAOJ5A7LyoXKZE3sUoub9Sy6ZBeXc1zwSOU_DvfYis4QmnFsmhH3EUTUfoWWbZ2DSpNtoCxt-ZghJcdbGt2Wp15CE1ALsE7qu5qR2lHKn9hLXaUgXUjXHIj4iQ8XnCBb2ZDaUbyNhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
✅
امیرحسین محمودی بعد از اتمام فیفادی برای تمدید قراردادش به باشگاه میره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140304" target="_blank">📅 11:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚪️
مهدی مهدوی کیا: مجاهد خذیراوی به حقش در این فوتبال نرسید/ حیف شد و واقعا سوخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140303" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140302">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140302" target="_blank">📅 09:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140301">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
ترکیب تیم امید ایران مقابل چین
✅
✅
محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140301" target="_blank">📅 09:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140300">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140300" target="_blank">📅 07:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140299">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">■
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140299" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140298">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7qv9MokZpGj6Ih7pwmBePtjHssBeeuVEi4ZyUS_bPnq4CqfC2TFt0MQ6fMds0B2rD0O1YMXB3mKTU8Ro-FDtJRcpx4-F4MAA56nbnRF1YCFwFhZ7YCs_VzcMciUL8o1h7X9lTCMwcADh6sHQ336sNWbafQ_5pkXjjhr7pKTEjFAj8i8vdEkWw34shPZHcobL6HgeY61BKSiwFBnpIXMzHYFEySzTaRQJqE7-oqaVMMEwnWCslJ4ju_xtpNs_PoXVo61mBZawyR9xllKdOlc__xCwSpZWuBEQy0M52FFaVtTx0O4wtQIFp6vspQOQM5BuyUfXkldoj9dINAQ2pfuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140298" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140297">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
باشگاه نساجی مازندران کسری طاهری رو با 703 هزار دلار خریده و با 863 هزار دلار به سپاهان فروخته!
❌
❌
قطعااااا این انتقال پل محسوب میشه و باشگاه سپاهان تا نیم فصل حق استفاده از کسری طاهری رو نداره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140297" target="_blank">📅 00:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140296">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
❌
دوگزارشگردیگر نیز با صداوسیما قطع همکاری کردند؛ نیما تاجیک و سعید زلفی دو گزارشگر مطرح، خوش صدا و با سابقه تلویزیون بعد از قطع همکاری باصداوسیما به پلتفرم نماوا اسپورت پیوستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140296" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140295">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140295" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140294">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140294" target="_blank">📅 23:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140293">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140293" target="_blank">📅 23:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140292">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emcZQMkkDnDAVATFeHT_CMkSgriHT-3_lat_3Zz612nmsaWEgeGKIEiEFGvhl33enCcUPakGhZsIxV2GpCs_PYQADD-oy4TAUcVrePjRLQWWW-n7NVjk6j8VOhM2XzMIXdUwDI4vS9U-r9adZ9cYAp245uRjqsxXqOkWO7syxF405-z5v_vV8EfGao6vqdJrc1XDD8fYqeicyENdlIq4jA5UFNqtoTEIU0xF1AsZg9sYhzL34s0ra8SL-OkOtRquVkI8gqatBD--aoCs0i-t4o14STbOSz0Vq_I21asXROlZVQOf3UGRFvFekJ9IsuKMirGhiASMrsbQpuibtH488w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گزینه جایگزینی یحیی در دهوک مشخص شد
❌
باشگاه دهوک به دنبال توافق با گل‌محمدی برای جدایی است و رسانه عراقی «روداو» این موضوع را تأیید کرده است. مسعود میرال، سرمربی سوئدی، گزینه اصلی دهوک برای جایگزینی یحیی گل‌محمدی معرفی شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140292" target="_blank">📅 22:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140291">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=kIgcvUvxQP4-nwOqp1TRRa4b1Q7hUOriRjWh_n91-dxsH2gK-E0iJg9pvPY5zWeiVntDfIjBlPqN6iIrZDQ9VpYCjohccXEa1wwpOPOI-8vIEyf6aauE_HQvqONc1Kbzbc0ANq5WxCUEO7pukWkdRGlUmygs_8rgoVbebPEAMZOF_D6fWpSYuesle31EOl_slpyAx2WrYApYHKxdytf2BVqtfzR7t0kWuzhtxac7KlYXW3fng8r690vM6vDvJahtxho087LXaZs3icNvwyAxxt8LP2yGctwL0QEL2mRZtoZcOWYwOtzp9Sb_MxvXvvTE90KzU0YMBN3G9ExLabrK8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=kIgcvUvxQP4-nwOqp1TRRa4b1Q7hUOriRjWh_n91-dxsH2gK-E0iJg9pvPY5zWeiVntDfIjBlPqN6iIrZDQ9VpYCjohccXEa1wwpOPOI-8vIEyf6aauE_HQvqONc1Kbzbc0ANq5WxCUEO7pukWkdRGlUmygs_8rgoVbebPEAMZOF_D6fWpSYuesle31EOl_slpyAx2WrYApYHKxdytf2BVqtfzR7t0kWuzhtxac7KlYXW3fng8r690vM6vDvJahtxho087LXaZs3icNvwyAxxt8LP2yGctwL0QEL2mRZtoZcOWYwOtzp9Sb_MxvXvvTE90KzU0YMBN3G9ExLabrK8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
مرتضی پورعلی‌گنجی تو بازی امروز تیمش دقیقه ۹ اینجوری ساق‌پا بازیکن حریف رو قلم کرد و خورد کرد و اخراج شد
❌
بعدش جالبه اعتراض میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140291" target="_blank">📅 21:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140290">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngkPp96QdqaWratkPTSa9-I2QxyiA_eChPusPWZVMQCbSn5cSS6tJIJNG_Xe45rH1OXbCT_7QhijDtUZJY_XsXz_TjWNEVZX6BkwfMuPNXSOp-qsGq7ulxFkj0tdTefbhdrAyrTR0jenU_fUTq8O-vX4rvBZLo0Reth7TwnjGWVk-2I_pGV9nU2yWJIfSLP6hqZuwCPoDY9yZEn2khNqcdk5xx62jNOOzKdm0hHrhSqYMBDmpfh_0ABQ49n70mSsd0I7Y2zotcdYS3dKZqdl5zx3z7QkNgQ4AWbXsc_RLU_Vf4wgeEQxP1whUdR0f33VISpB9sR0qvqI8YmDLmRDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140290" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140289">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140289" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140288">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔄
🔄
محمدرضا احمدی از صدا و سیما به طور کامل حذف شد و حافظ کاظم زاده مجری فوتبال برتر شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140288" target="_blank">📅 21:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140287">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
بشار رسن پست مربوط به بازگشتش به پرسپولیس را لایک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140287" target="_blank">📅 21:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140286">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
❌
❌
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140286" target="_blank">📅 20:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140285">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmSHfTZK9kbLhDT73sd58xnNItF8nvkFqzcHh5UtMGJgnWqe00iCUOGS90jWB7CRBUs6TaIs7UhkkinjxefTEGXK5yszT1YcU2U9vcPpuzc1cWzepAWizxlrAK5oVosAg_gCsBvTnLuZ_3X8GMqLSjVYPIdH1P011mR77AOsJfk1fHtNoRXS0zDTti98xc6UuxNbbYV2G_8H0EUW5XkYdZTyV7U1rg4_l9Phm0fk-LIA7yXsOQbZtS9nDdF1aP9Favtn0Iz7LC_tpF0VD4dhBwVLdNfdAOqcubQHW2_sbm2VzVW02M6Oz6zhz1TO1ivLu0TRxo9wT8E5_rCV2TZwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزگاری سیدجلال حسینی با وجود اختلاف قدی بیش از ۱۰ سانتی متری که با کیروش استنلی داشت با پرشی فوق العاده سرزنی کرد و رکورد فوق العاده ای از خود به جا گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140285" target="_blank">📅 20:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140284">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140284" target="_blank">📅 20:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140283">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA5e-TwtBsDY-JeLwLN3AHrZgbyCYAjg7TBNYoTItEcQEKmNnM4qa7UAxSJAhDJ5Gw0Tq-vn8hSoZilA8SnTNtIHZntl6pgxhdrwYbunnTlHYrsrbBZJAPQI_ikJgOLQfG90FjjdWrFtw-DMUjQvvkJ969HlnLgVjqT99g4rFbqM-xpxFnKU1oS45eQiaUJTCqmT3FJDHW7MvTn_EdfO-P1L0C3lLtxvvNMDNcYz9hWDn_hpjFP-YITFKs-uyqYieijUuzT-IRnosVvtb7Ou72u-bnp9GifpYaSfrRU65icFziBPCFiTVwIGZBPKGq-_oiCzs6yUDYoBHr3MwREs3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبرد آندلوس با کاتالان‌ها؛ سویا سد راه بارسا!
[
سویا
🔴
🆚
🔵
بارسلونا
]
⚽️
سویا با اتکا به بازی مستقیم و فضای هواداری، می‌تواند کار را برای بارسا سخت کند. بارسا از نظر مالکیت و کیفیت فنی دست بالاتر را دارد، اما مقابل فشار سویا باید کم‌اشتباه باشد. تقابل دو سبک متفاوت؛ جایی که مدیریت فضا و استفاده از موقعیت‌ها می‌تواند تعیین‌کننده شود.
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
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140283" target="_blank">📅 20:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140282">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiTuvgA6f4UJcv6nJV2DojavLUGnwvBztwAK6Va-RBwEkMZziX4sFuI5MPzmSTbpMmZSYjiz-j8Xcyfs8iDUagTpIJgYoWImi4-TqHafKX5RI0I6Wy1Zs9jzd33lhn_YG8bjtsFrX5Qa9kaLToi88H7l5zgH4wvydG6qsMB8Z3fTrFU2P21XQ3gD38ZzBJTD4saWf90doEQGnfh8_QtEs8L54puHSm0O-4yAXNpU1ew7CKFBfbo1Tl-xVtBXveIyYB-LTDjPuc7bYacsdokSiEgn9iKqJa5ns4ke-lMzZ7E_tjRIU4rY8UIor33g0_QHCJDhTrLRYrPXJiYfmE7T5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140282" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140281">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNNLgrdu9xDGZQFbUC-rR8OJTOk6rRAqfeMjVuMzjCy4Ij5SeNvT0RuJPahaqcLJ6EI3Y7UklETeljaKwNNwYhqYvlQe6ZZVKKDfMR8KI7Pt4fXwu-z8lQCDcGchf3gtzIb8dVWTqaItTIRZ98zNWBL_VuPxwzJmdUvHnt-ocfMktAH-prcYBCHs7-LMHuYsHTPmKFrobPNr1yZ-LSAnn2zypT9oiy3WMqDRTue4OE-Ztc9sJM-Md0TqMAHfw2NhOgKxrYNsckCXCC4vbb3YJtg7zeH8MPG_Lg3WIpidU4Gp-JGTpfgkJv6OZDTeY4qvpiI7Jd-oGgginpyriVXWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽
بازگشت سرخ‌ها به تمرینات
⏺
تمرینات پرسپولیس پس از 5 روز استراحت امروز با حضور 15 بازیکن از سر گرفته شد.
🔻
ملی‌پوشان و بازیکنان خارجی تیم غایب تمرین بودند.همچنین حسین کنعانی؛علی علیپور؛محمد عمری؛حسین ابرقویی و امیرحسین طاهری به دلیل مصدومیت زیر نظر کادر پزشکی تمرین کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140281" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140280">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDn5M1uZG3QBqnfcoGKs25N6SOYZ1ifRtd_H7N-Q_0N_ooQVvtT5P_DkOV_PrWTRPEDn_wsKHZLaP9zDdOJ2pxGaOf1_CDSj8KoTQda4qQ1kNHadIRxHSsb5eMdsGjIxRmpDAHB55k9P3WIQ7WyfueMFgJ9MWuSxEn8tMgef1hr061mG_7D1ZXNtqwJ2JghWJLJc9zJzj_Jmtv8Q8p7JTk6hHpv_W1rR8A10TH6-1DGww0MPfy6HQm1sEhAfPMiz5VTG3SBsQEh1pUenlpO2UuhO3D49MaDQh5YAFyodWWG0idHy6FuCAia-v3SbRzYm5GfgG-dfeTqzYbW2ooRhGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری شایعات
🔴
🔁
🇮🇷
ایگور سرگیف پایان فصل از پرسپولیس جدا خواهد شد و مهدی طارمی به پرسپولیس باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140280" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140279">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227e813e97.mp4?token=FsqUGWsj5JVTVNXf6uGghCnhLih12pfo0d2jFofyS6l2BCnElmXdDuGGovjCbxup3u51YUVcdWB61e6fZK_p-WyMpxzJUzPfdVv0DzrIbv4pzxcCXdrqta0EwurslgNkcoEVq-ra6dd7Lk_K_6jBK-EIvMLE5F9j1SP9lBSwJ0H8stkmZE1SLlqqIl9z7LRYmd80rumj9TzQy8HKl2tppUy_jcA1VGXwb9LYwMlYtfxv9OqMhCiBiITjKSnme-prczu50CdTDXngeKW3XEjUasaMhD4goFxapNswLcF_3atVHSoKnP3CzPkUQD5bxTdrkp3CFm8lws-8LgNdcXq-Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227e813e97.mp4?token=FsqUGWsj5JVTVNXf6uGghCnhLih12pfo0d2jFofyS6l2BCnElmXdDuGGovjCbxup3u51YUVcdWB61e6fZK_p-WyMpxzJUzPfdVv0DzrIbv4pzxcCXdrqta0EwurslgNkcoEVq-ra6dd7Lk_K_6jBK-EIvMLE5F9j1SP9lBSwJ0H8stkmZE1SLlqqIl9z7LRYmd80rumj9TzQy8HKl2tppUy_jcA1VGXwb9LYwMlYtfxv9OqMhCiBiITjKSnme-prczu50CdTDXngeKW3XEjUasaMhD4goFxapNswLcF_3atVHSoKnP3CzPkUQD5bxTdrkp3CFm8lws-8LgNdcXq-Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
گلزنی احمدنور در دیدار امشب کلبا مقابل خورفکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140279" target="_blank">📅 20:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140278">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG17T2O-mDprEfHqHT0gSUJedeLooij68QeZaIyftZVMuIHPL1NZ-2atzfWyQ6F-E60XshEHt-WhEuau5LmzCWRdoI6xZF-8v3sBPuGtkYDSrQ_TV1Tsp8dz-oMhFi0G4UQq-Tc2mTLCorEnKfDyOn3caZwuHeFPuCcdsAIMdoP9BtyB2jyZtGdG0QS5p4TTCkqLUb4OTKzPWluhC1mlHf0P29Y0qAPtvvc32jutw7Lb1FzNo5gCkM4yKaeRUJDJ2QpLrKPne7rt1bNOaiWU-lWuPQRMH4VCbZrNSnMwGvZhcZkGqv5SZ5xuHGnENw-L_D3dhApwvY5ZniTmxl17mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
با درخواست علیرضا بیرانوند مبنی بر انجام معاینات پزشکی موافقت شده و او برای بررسی‌های بیشتر به بیمارستان معرفی شده است. این اقدام باعث تعویق موقت زمان اعزام او (که قرار بود اول مهر باشد) شده است. اکنون مشخص نیست که اگر او موفق به اخذ تاییدیه وضعیت پزشکی…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140278" target="_blank">📅 17:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140277">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140277" target="_blank">📅 17:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140276">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140276" target="_blank">📅 17:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140275">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140275" target="_blank">📅 17:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140274">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
پیام صادقیان خطاب به امیرحسین محمودی:
✅
بهش گفتم سرت تو فوتبال باشه و فقط به تمرین فکر کن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140274" target="_blank">📅 17:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140273">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
بیرانوند قصد دارد پیش از رفتن به فجر سپاسی، قراردادش را با تراکتور فسخ کند تا مشکلی بابت چند ماه باقی‌مانده قراردادش نداشته باشد. با توجه به بسته شدن پنجره نقل‌وانتقالات لیگ برتر، بیرانوند از ابتدای نیم فصل دوم می‌تواند برای فجر سپاسی شیراز به میدان برود.…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140273" target="_blank">📅 17:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140272">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4idIeU5ElhQqZR2l6EnqOr5fG7jHMmMFvysnspgGSI-EIZYG91ppkvNG_HnPb9qXi7kta7eF2AqpDjtWZMVUykVgaSej1oSszNTWAgux_Z8ZiHrkrTxd1ONtv_V_ADuVXLyCAzdwUaHkCG4yCsBkN4suFLhwhyepzcI2AqkeGlDPkLJeBBwVryKk_YbPrcxaWFWr1V3NZo5e00SmULgUAdV-NfeUzO_ur5BA0btKgsIkkc0Wu3nkBhg4Ey0Wroay2wP7KMqpleB2si0MCd0grXC1EWYYb_HV4Oc7Ew3VfC9Qezh-7CA6SGF2VXMnL_npXaqBj_YpOvmI2O6cYs0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
ROMA -
🔵
INTER
⏰
Tonight 19:30
🏟
Stadio Olimpico
🔵
رم در خانه با تکیه بر مالکیت و فشار هواداران، دنبال کنترل ریتم بازی است؛ اما اینتر برای تغییر جریان مسابقه فقط به مالکیت نیاز ندارد. نبرد اصلی در میانه میدان و انتقال‌های سریع رقم می‌خورد؛ جایی که کوچک‌ترین اشتباه می‌تواند ورق را برگرداند. یک بازی نزدیک و تاکتیکی که احتمالاً تا لحظات پایانی، نتیجه‌اش باز بماند.
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
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140272" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140271">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc94830254.mp4?token=h66XTJjTDD1onERDC3LxrLFqy6tAAuolv5fLlMvSqu4K5u8uwHwsToj4_G4IZXIkKz00HGo0zM_ItuL3STnfgoFaDgORdug_wN8UNQflhE8M1_ebvkcKVdDiTARuwWxpVgIMtwwwHWDAEv19YczxSv3AZG0KqksfzY7ZFkN5HNGjhuaT54ayksz8TbqlfGZlfvBH-VgO1MXoi9ICe_6iYGeJI2WmL9j-Er1NSAIIwaUC2ls2G6ObM9V6dBzzFnQ7d4Ac3n0dgRi0ZyvDk3_Q61H9lP9xkyI0n1ykcUCzL0KfUGiZU0b31hNy6cJYLrUUDiwP_mEEuJPRbkdlbf50Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc94830254.mp4?token=h66XTJjTDD1onERDC3LxrLFqy6tAAuolv5fLlMvSqu4K5u8uwHwsToj4_G4IZXIkKz00HGo0zM_ItuL3STnfgoFaDgORdug_wN8UNQflhE8M1_ebvkcKVdDiTARuwWxpVgIMtwwwHWDAEv19YczxSv3AZG0KqksfzY7ZFkN5HNGjhuaT54ayksz8TbqlfGZlfvBH-VgO1MXoi9ICe_6iYGeJI2WmL9j-Er1NSAIIwaUC2ls2G6ObM9V6dBzzFnQ7d4Ac3n0dgRi0ZyvDk3_Q61H9lP9xkyI0n1ykcUCzL0KfUGiZU0b31hNy6cJYLrUUDiwP_mEEuJPRbkdlbf50Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حمید مطهری سرمربی فولاد: پرسپولیس تا الان نتایج خوبی گرفته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140271" target="_blank">📅 16:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140270">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140270" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
💢
💢
✔️
✔️
مدیران باشگاه پرسپولیس هفته گذشته‌ مذاکرات برای تمدید قرارداد پنج ستاره آغاز کردند
❌
پیام نیازمند
❌
محمدحسین کنعانی زادگان
❌
تیوی بیفوما
❌
اوستن اورنوف
❌
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140269" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140268">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
قراره در فاصله تعطیلی لیگ، برنامه آماده‌سازی پرسپولیس با برگزاری ۲ یا ۳ بازی دوستانه دنبال بشه تا سرخپوشان از شرایط مسابقه دور نشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140268" target="_blank">📅 16:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140267">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj0kQUUvPX5uuloyhccizn8yz3izkEK2PQm3b2lhIirf8jO6qGykcGAYgGg2KJQLYEjnvvH8U5te5_EOGMlS4QvMzowE5pY0GMNkEFe2k_VviBjE9XMggmPqbAa9ON9n9pxb9TIi9P4URWy_m9qewwB1NHr-kVl3nGcgSOC7csErnPyMrCfVygQgqXbVJGaCwzdrnTUrwx0-jExfw4nP-mLn7Clvu0FQd5Hnc8IeDQkbTPMTxpdvMTcW8XTv95ICKVAm7bo6PSXJv7V5nOnGWx9WLes6Mp-IEiwgFIsILVnKNCYHJuYUUT6dEeC_LSr2fXVKHm1S7i2EVqXkokc6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تیتر روزنامه‌ گل درخصوص دعوت شجاع خلیل‌زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140267" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140266">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140266" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
فرهیختگان:
❌
مدیران پرسپولیس معتقدند که مدرک کافی برای پیگیری شکایت یاسر آسانی در CAS را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140265" target="_blank">📅 14:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140264">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140264" target="_blank">📅 13:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140263">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
❌
🗞
فوتبال۳۶۰:  بشار برای برگشتن به پرسپولیس پالس مثبت نشون داده.تارتار تأیید بده برگشتش قطعیه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140263" target="_blank">📅 13:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140262">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
آغاز تمرینات پرسپولیس از یکشنبه در تهران
✔️
✔️
تمرینات پرسپولیس پس از چند روز تعطیلی از روز یکشنبه ۲۹ شهریور در تهران از سر گرفته خواهد شد.
✔️
✔️
برخلاف برخی شایعات درباره احتمال برگزاری اردوی خارج از تهران، مهدی تارتار در شرایط فعلی برنامه‌ای برای برپایی…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140262" target="_blank">📅 13:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140261">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052167cdae.mp4?token=PUpeOpbugQ7a5BGUAah4ujiJl0RQ_BidZyGKRu37z51ytJKlJYrFK0G7Fu5FhODRDcjUF3k-Ea_zd7DxFQcSBx-S2ZJbUg4DZyK_fRlswSWZXm2wX0juJGUP_fRGUPQjcHLYLSF5HDeCaQwiRbTGRNIvMgcsP7ci8ib4V12roa-mjxc-B3AxCTqkUtUMvnsGY0_lESBhzVeiViHvJtXxJcl6vHGokc0ub_AslTvEhTsLrrz0VY_-hz7dmvfDF7BxARBts5LtPZ9xp_-erUDCk3Ts9efdybmZRmrbJvi1jc3Q15vl4wDmURQBMISCWwSw50HjfSV1VdvCiMd_mrhXeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052167cdae.mp4?token=PUpeOpbugQ7a5BGUAah4ujiJl0RQ_BidZyGKRu37z51ytJKlJYrFK0G7Fu5FhODRDcjUF3k-Ea_zd7DxFQcSBx-S2ZJbUg4DZyK_fRlswSWZXm2wX0juJGUP_fRGUPQjcHLYLSF5HDeCaQwiRbTGRNIvMgcsP7ci8ib4V12roa-mjxc-B3AxCTqkUtUMvnsGY0_lESBhzVeiViHvJtXxJcl6vHGokc0ub_AslTvEhTsLrrz0VY_-hz7dmvfDF7BxARBts5LtPZ9xp_-erUDCk3Ts9efdybmZRmrbJvi1jc3Q15vl4wDmURQBMISCWwSw50HjfSV1VdvCiMd_mrhXeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
آغاز مراسم افتتاحیه بازی‌های آسیایی ۲۰۲۶ در ناگویا
❌
مراسم افتتاحیه بیستمین دوره بازی‌های آسیایی در ورزشگاه میزوهو شهر ناگویا ژاپن آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140261" target="_blank">📅 13:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140260">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140260" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140259">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLwXuGbC4q0wDGBZgOqzX33OgawwLQ7xlZuwQpfd1jp3JoJgxauOXLFtQCDHURBwFJQzxCKIga3D7AD-gHgmp73Lvh-EArhSpB6HPN7892AkTxRzigFYK7OrpuC9iEM1pqZv9Nxt_AKwHXjKJVTRqhQtkiFBJqvj_uTosF-1EsmOAFASS5qEDaqU-QGz96J0dAm7LjFI0PkAU-vqn1V1KydrtjtMbP0FfEnGJoD2QpHq7KsMSVwKZJlpG1Pnp68t_JlAK8FsELbk1tKES7sQnfeyUXKTmfavX2syxEKNX3N6g-X7PEqo8rIEFAlrJAiKrfZxijjXY2UlwaIVSIMyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140259" target="_blank">📅 11:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140258">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140258" target="_blank">📅 10:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140257">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140257" target="_blank">📅 10:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140256">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Znq75IZJnBE3NAmX8taC8LsqVqZ8VqzFQS00ezyK8yqKC1GHr2azLfIX3l24zful_ns8ZfenaDwIpWDznCkxYFy36oCMOFJOwm9w0K_AHjhPPuwzu_mC6HHKTbk0RcofRkdc-tflnUabe4Hav0Ucs44oio4Gdh4l5nPLfOqqhWaV6zdzMjV9ZLQzZrNLUeqbSptDkbStWP83PNg84VZ1UjY_2GDCLB7mnYfUp90ACXPDDg-FkKoOcajgfvBRPzYu-04oP4xTXePbHGnSM6413QX0Y7RgN_YW3f0daMcLpCDbVCgqa_o8n7lvf8XbgJs0CSvei5RVTDaHKINOMWqUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140256" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140255">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFDRdmQlvswD4_ctNHYshiplraeNGAfuOPHeW1jVaMJJGnqHSeufaAwlE-pLceKwoQdbLYI2MQKCJVTpOJUTwDlbkKdmJNCfyB4JVaPjqi4Y0ezZei9C3aRt-tem61uUF5RnqED0Wp_OciJRgp410uv55GUyOc9ua6fAsZgPXpNdZnzrYG6t3CjXM5VqNHGUbs8MlFdcDj7d9N-KG7wf6QbDzppT0uybIcajOABqh90JtxXgmRp9R6IH8a_MJkh_4abuuSIV527yYur5BRoLEzqonTYMA7KZTifURQse1KPNbLKiz-IDwpFtEUvrw-Qk_S54up1jGkCei6flRn0_AvqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFDRdmQlvswD4_ctNHYshiplraeNGAfuOPHeW1jVaMJJGnqHSeufaAwlE-pLceKwoQdbLYI2MQKCJVTpOJUTwDlbkKdmJNCfyB4JVaPjqi4Y0ezZei9C3aRt-tem61uUF5RnqED0Wp_OciJRgp410uv55GUyOc9ua6fAsZgPXpNdZnzrYG6t3CjXM5VqNHGUbs8MlFdcDj7d9N-KG7wf6QbDzppT0uybIcajOABqh90JtxXgmRp9R6IH8a_MJkh_4abuuSIV527yYur5BRoLEzqonTYMA7KZTifURQse1KPNbLKiz-IDwpFtEUvrw-Qk_S54up1jGkCei6flRn0_AvqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140255" target="_blank">📅 01:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140254">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
میلاد محمدی که تو تیم جدیدش حسابی ریده گفته میخوام برگردم پرسپولیس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140254" target="_blank">📅 00:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140253">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
❌
❌
پست خداحافظی میلاد محمدی از پرسپولیس
✔️
✔️
امروز با قلبی پر از احساس، از خانواده‌ای خداحافظی می‌کنم که همیشه بخشی از وجودم خواهد ماند. از هم‌ تیمی‌های عزیزم بابت تمام لحظه‌های فراموش‌نشدنی، و از هواداران پرشوری که در هر شرایطی کنارم بودند، از صمیم قلب سپاسگزارم.تا…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140253" target="_blank">📅 00:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140252">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140252" target="_blank">📅 00:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140251">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭕️
⭕️
پرسپولیس مهدی تارتار در این فصل ۴ برد ، یک مساوی و یک باخت داشته ؛ ۱۲ گل زده و ۳ گل دریافت کرده امید گل تیم تارتار ۱۲/۲۷ بوده که با این امید گل موفق شدیم ۱۲ گل بزنیم و امید گل مواجه شده ما ۳/۲۴ بوده و از ۳ گلی که دریافت کردیم دو گل روی اشتباهات فردی بوده…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140251" target="_blank">📅 00:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140250">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=gubmxaYvSkLsSS-DfpWJft41ArpnhGmYeg7dhBbCvFYy9v9G_BvIhcChFnF9xVfTInUpSn30aQn4cv20y7j0RKOW80QUUO6Kg4PjT1SpTFYCf5cHgqR8lkNa3GEGa1vKhHLuMUcIMePr-ag3j69lI0AupuABcEpsjFaaCZvTDW1JnULmIXs6LoKWv6sBR1Sq2-hFtvUyjd1BGDhjZNl3_v5X0327fuOII1aFaP_Tv96TNC5XfEcAwUIaJlDmK0LLo-hBVlFnOSzZXmPew4-yFLmB8eT4isWOP9eAYMCu07S-LAFTVsRyjPL8PEfEGNzE0bPz0kCu1Y3zmXn-48EazpLsI_MGJgG5WaR6Ey8SoBq9BZOG7Lcn_uu0jaZ7aw0vFSb92cwyF9GRE-LeYFUfyv4AO-a72CCGgP1wb-NWq4G5nw4dympGgKXct-mhhYQAYQziMQv-N1ifZByqZ_U46jm99uR_hQF2z7leV-97It5L_HP6hB1F43W-z62DjDnMY19WqkSNz6dXj7SLqmV-5C8k2kZuYctjpb_cP-TTU1jjKW1uY9hYe3cHqmtqmLHrS9yhkrn6u4msbCa4vpZalWHmA-2rIYRH-yz0TC2Ukceds8UL1GcVDo7kLH-drJzLHYhl3COgtCmJlBOvpR1nHoVSLm64e3smeL9Aqr7Fb3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=gubmxaYvSkLsSS-DfpWJft41ArpnhGmYeg7dhBbCvFYy9v9G_BvIhcChFnF9xVfTInUpSn30aQn4cv20y7j0RKOW80QUUO6Kg4PjT1SpTFYCf5cHgqR8lkNa3GEGa1vKhHLuMUcIMePr-ag3j69lI0AupuABcEpsjFaaCZvTDW1JnULmIXs6LoKWv6sBR1Sq2-hFtvUyjd1BGDhjZNl3_v5X0327fuOII1aFaP_Tv96TNC5XfEcAwUIaJlDmK0LLo-hBVlFnOSzZXmPew4-yFLmB8eT4isWOP9eAYMCu07S-LAFTVsRyjPL8PEfEGNzE0bPz0kCu1Y3zmXn-48EazpLsI_MGJgG5WaR6Ey8SoBq9BZOG7Lcn_uu0jaZ7aw0vFSb92cwyF9GRE-LeYFUfyv4AO-a72CCGgP1wb-NWq4G5nw4dympGgKXct-mhhYQAYQziMQv-N1ifZByqZ_U46jm99uR_hQF2z7leV-97It5L_HP6hB1F43W-z62DjDnMY19WqkSNz6dXj7SLqmV-5C8k2kZuYctjpb_cP-TTU1jjKW1uY9hYe3cHqmtqmLHrS9yhkrn6u4msbCa4vpZalWHmA-2rIYRH-yz0TC2Ukceds8UL1GcVDo7kLH-drJzLHYhl3COgtCmJlBOvpR1nHoVSLm64e3smeL9Aqr7Fb3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشته کریمی، ستاره‌ی سال‌های اخیرِ فوتسال ایران، امروز اولین بازی خودشو در قامت فوتبالیست، برای تیم فوتبال پرسپولیس انجام داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140250" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140249">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140249" target="_blank">📅 23:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140248">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140248" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140247">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofB3rwhkP9rG_Bq8fi1wLxKf9GPs8Zv3g_jnz-iKMxfDQTCG5Xq4Kv9hUWBiWAE4WnTDwDrUk4XaQfmPxY8GqsRHVqtDwtvvFNeLgRyPVYqxqPbPabOIBjq02ZPcXoC5T_Uew7SCrizLa1saGYFblRMOVVs8WzCmNWW1ZosHTHZbGYHYv_tTNqgTXY81TYcfkGnKSp4Vy31jWbtrt1u-pDBo56WlmyGplJh2g2jcWv7NQXUJQiMXgveB8Ew26SGYJxY8hVKDz6DUK1bJ96jXoFkUu46F30RobcKOvXU1bFYb4U4eiywm2W-5IuuS0gZeUKhcJlgQJdWCXd9RjcqrvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
اینم تو یه دنیای دیگه‌ست
😂
⚡️
آخه اسکول، تو این گرما این چه لباسیه؟!
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140247" target="_blank">📅 23:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140246">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
❌
اوستون اورونوف به مدیر برنامه ش گفته آینده ی فوتبالیش رو میخاد در پرسپولیس بمونه و با مدیران پرسپولیس برای تمدید قرارداد سازش کنه تا قراردادش مجددا تمدید بکنه
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140246" target="_blank">📅 23:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140245">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140245" target="_blank">📅 21:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140244">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140244" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140243">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140243" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140242">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140242" target="_blank">📅 21:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140241">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrPb5LpxwcZuaHyySbzr1RjQ_kl1nMzrNX0xPppOxS1z1aOZsqFunaAS9k2s6-mWmzqdHN4_ZeOBPmgKI6ZzQMrQ1DezPBpgZXuZrv7hywK8S-98OJfAnhBm6CNUnyq599frTr7EMVzdYoOsOO2cMZTL_klI2eEOUQMh_DY_2jVhF_1Nt1VGucRGziKpiKROPolUgBIncj_1PXKfvsj0bGXyVujiK7imZzhKQ6lZleTTKebT44j0PxHuMGn0sohgWWgrNksdQgjX6OqzlZ_r5KDxD5I0ABT8VGN4mq0p9uWYI8gfH5O0kDUz3f8jEJtc78_nX_mOWI0B1lmuViLcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی بانوان‌ پرسپولیس در فصل جدید
♥️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140241" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140240">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM5awiHxsK_GTgRUO_b_M9oKqUJrff1sW-jFhkX_iRkT4P1U_pe-tkh4dp0H2BaksZwhjbXxDFWU5v3eRU52ZY1qBvxr_pE65NJZsRHFs_b-WkaBr6QI0MMjSVvjSjUzZfpv1pd2jGeUUgCgzErWTzU1nYYrOl34RHSSlKnVReOlrGyvxKVyCvx_eQkz4T10FquMi5oIfH3ru3WoyA2gdbbPQCoHALA5i8B05MQ6HOJmHjR8mgIjttnnnRZwT7GhUed1UvGZgXknl3IlTBsBDQXqwu7nSc2y_xpCtIYE1vDcSUEvphQ7GG42qtKW6zFIdrNPOeM8oUGYZGgxVhTraA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Brentford -
🔵
Chelsea
⏰
Tonight 22:30
🏟
Gtech Community
🟣
برنتفورد مقابل چلسی؛ جدالی که برنتفورد با فشار و بازی مستقیم می‌تواند برای آبی‌ها دردسرساز شود. چلسی از نظر کیفیت فردی دست بالاتر را دارد، اما در بازی‌های خارج از خانه باید مقابل انتقال‌های سریع برنتفورد مراقب باشد. با توجه به سبک دو تیم، انتظار دیداری نزدیک و موقعیت‌ساز از هر دو طرف می‌رود.
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
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140240" target="_blank">📅 20:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140239">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140239" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140238">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=FA-qrUMcu3IPJoJbi6ye4QIhGJJwaWC4teCC6Fh7KYVY8hI5cXz_WBJoPX1bCjoX7KhMA7rh5bGZkUFI5gCho---n7nXzwlHsMRNZmz6OV7zrkgWuONBURbYZ5UdVgGWwqeAxOaVzgDF1Vor51N__v_vcSiOmvdKAQT27Enqaf1H7-hY2NhiWpudDDgz7uMDGVSv-JMjQDnGnHb_b9qjhsH0yn1Z-H7OfTo_MWIyEuTjg53rt5BCy235CbpbDrANmrAW_clCU-sD6FPs8nJiaYWXwqtkFhk7s8K7XHITBcjG2xHReKUNlO3jRzVNvjHctwr9VNcU-OKjkYeqOPeBLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=FA-qrUMcu3IPJoJbi6ye4QIhGJJwaWC4teCC6Fh7KYVY8hI5cXz_WBJoPX1bCjoX7KhMA7rh5bGZkUFI5gCho---n7nXzwlHsMRNZmz6OV7zrkgWuONBURbYZ5UdVgGWwqeAxOaVzgDF1Vor51N__v_vcSiOmvdKAQT27Enqaf1H7-hY2NhiWpudDDgz7uMDGVSv-JMjQDnGnHb_b9qjhsH0yn1Z-H7OfTo_MWIyEuTjg53rt5BCy235CbpbDrANmrAW_clCU-sD6FPs8nJiaYWXwqtkFhk7s8K7XHITBcjG2xHReKUNlO3jRzVNvjHctwr9VNcU-OKjkYeqOPeBLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امید عالیشاه
؛ به جای عزیزانی که اخلاق را در ورزش رعایت نکردند، دچار شرم نیابتی شدم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140238" target="_blank">📅 17:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140237">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140237" target="_blank">📅 17:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140236">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro2FenBHUK5OzkoPBFD4xxHOWzt_cWeTt103CoJd6KWoYi-a6Fdp--bGe5y6aQsjBv97OX8RygYk2m3i2ZNlGIGiUANhkEnrK56oLqbJ71y1ZqJUuNdRNfMKd1UfCl3ig9YHV59WcE5UyMs1BOeFKw5LL7y28mCjbcGMsgKiEOGDVfsKvQYvqSQuZEQpS8KjvqiWKdyXuDoWpXQxPWWsTQobOgj6YZ3EvefMPZZRuhiBUuD6st_bokueaAwWTQ77Sim3O2oRScjOxMU6WP8gr3keoMFeVEWOt3NBR1Wi9gFuH3gq_5aVGiGzINqwk-uZ1k_h-Nx2Sc6JIVfYsqel0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
یکسال پیش در چنین شبی رقم خورد
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140236" target="_blank">📅 15:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140235">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=A31hw3fwwFiax8s-Eq2aLHwtfT6KBUPodmhIQKAtJn4Wf1LhZQ44c3lwK10vUxvLyJ9HRwYtkMrrT1rEnlwKPUAtvGtUhNljXFwWHkeW9e_KO4ru52HR9i2n9wLgKT9hiaK7D-cHix1-YXWz0UVBjnbFKF_T08IgB7YIoiMHAPpMH5bjmG5Fy--Gt00by9gUuuGIS3eyhq4T3Pw1kmMrCotUejB2nHNCwMdSofkHIjKUyanBTjdCdx3dhbRxWmSFWl86T8xyr92BL9nTI6GDshgoYw7P664rBCcLNXBLScepyBZag2tg2PoApVgjYues5i3hYhJgfSBKyDNn6UZp0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=A31hw3fwwFiax8s-Eq2aLHwtfT6KBUPodmhIQKAtJn4Wf1LhZQ44c3lwK10vUxvLyJ9HRwYtkMrrT1rEnlwKPUAtvGtUhNljXFwWHkeW9e_KO4ru52HR9i2n9wLgKT9hiaK7D-cHix1-YXWz0UVBjnbFKF_T08IgB7YIoiMHAPpMH5bjmG5Fy--Gt00by9gUuuGIS3eyhq4T3Pw1kmMrCotUejB2nHNCwMdSofkHIjKUyanBTjdCdx3dhbRxWmSFWl86T8xyr92BL9nTI6GDshgoYw7P664rBCcLNXBLScepyBZag2tg2PoApVgjYues5i3hYhJgfSBKyDNn6UZp0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل تیکدری تو بازی دوستانه مقابل شهید قندی یزد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140235" target="_blank">📅 15:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140234">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=rPc-vZ3HhA3PomJ3Khb6_OamvIvPw4jESbCK6eT-WlkgI47KOQD8BDwBAwCqHw45yDHI38Drorm-XNU4wvbjZInVxpDcTi_lazSVYineGT_Rh8kdgEmzJ_KhhPoeY52Kc0ByATL3DKF6MjSAhrXRaaHDSCtKjGrl6FAWzSLs4sOPgnlq4eLlRRoyDMRxlsZozqz5YsZ9_PD9ROCi3h00kKnDLV3-z1dOUJuIEFQoFQnEMcDwTlFAPu8IuMKGsY5RO9uryBzck_N5VvV7UFIhVJP1RgeocUlyzcfJ8I5tQ4FZCjMgioq9_l5c_QA1hnIz42VjAYjLUPHL41KrWrNuEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=rPc-vZ3HhA3PomJ3Khb6_OamvIvPw4jESbCK6eT-WlkgI47KOQD8BDwBAwCqHw45yDHI38Drorm-XNU4wvbjZInVxpDcTi_lazSVYineGT_Rh8kdgEmzJ_KhhPoeY52Kc0ByATL3DKF6MjSAhrXRaaHDSCtKjGrl6FAWzSLs4sOPgnlq4eLlRRoyDMRxlsZozqz5YsZ9_PD9ROCi3h00kKnDLV3-z1dOUJuIEFQoFQnEMcDwTlFAPu8IuMKGsY5RO9uryBzck_N5VvV7UFIhVJP1RgeocUlyzcfJ8I5tQ4FZCjMgioq9_l5c_QA1hnIz42VjAYjLUPHL41KrWrNuEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی: اونایی که به من حمله میکنن مشکلشون من نیستم بلکه تیم ملی عزیزمونه، اونایی که حمله میکنن یه مشت وطن فروش خائن هستن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140234" target="_blank">📅 14:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140233">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
❌
محمد خدابنده لو درحالی به تیم ملی دعوت نشد که در 6 هفته ابتدایی لیگ دوبار در ترکیب منتخب هفته قرار گرفت
✔️
✔️
همچنین این بازیکن با نمره متوسط 7.37 یازدهمین بازیکن برتر لیگ از این نظر بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140233" target="_blank">📅 14:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140232">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌬
پایان بازی  نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140232" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
