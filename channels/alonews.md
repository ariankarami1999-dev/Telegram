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
<img src="https://cdn4.telesco.pe/file/mbbTpbiP-x0ZqK1KzXCWUbrs852sdBOhPrAYE0No85g2Y88GNYKUCfUfOBN_rvuDFRbKSWnnmFb3MjSDP3rTj9y_ZTJiCgVkBNQB8dji_vV9KYcmdgHrHf6kw3dSooWjxnKt_edOHtJf073N6hQqPaTn9xMg0dHycFIvKWAu7NrHdWhDskrA_l-rkWJoyU2w1LNTSoga6rbA9lSdo1u7kNiUoBMUi2PqDEX5beUkGx5zeLJ9CCY1QEuuYV4lmcQ5wq7DMpXE9jRqgRKnUvp-QE1I7iuZeNovHRN_MghbnaUFsof4DyNnIfKr9s4PMMQtdHN74dMug3VVO09hMoo0CQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
<hr>

<div class="tg-post" id="msg-151796">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
امام جمعه تهران: توقع مردم، تجدید نظر در دکترین هسته‌ای ایران است
🔴
از ان پی تی خارج شویم به غرب می‌گویم هسته‌ای ما به شما ربطی ندارد، غلط کردین؛ برید گم شید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/alonews/151796" target="_blank">📅 18:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151795">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VDHBSYxIsdSpJf9j0wI1hG8UG3-9mJLoP3sQabTOBJ6v__L7YPYvTtaUYbcRXv1rZGgsM6DiD1NnTFMHhqE_tEmVggKvpEvcxH3sUx6iO8MsiAqDKDOgdWFnI0gMQ5VhGW36WzGZBPxvsl9RHBclxNMARoz4JrFokO_shN0vG8nGkBxYfDicOKkAaeJPTRS7R3EFIGptRQhl-KbhjOGo9oMyoS3rz6ubXcl2vduyzkTVSxkWw6ja65sEKeQDp2ovQPnnDbOGmeYf9GinnO_-_p8mtUx5TcvE__p7mU5TY1zNoXnbo5NwyMN1pIlVaTAeMXlugXxH2iEB3KzTsKI8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اطلاعات بیشتری در مورد کشتی که در فاصله ۱۳ مایل دریایی غرب منطقه الخلیج (الجزیره) در امارات متحده عربی غرق شد، در دسترس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/alonews/151795" target="_blank">📅 18:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151794">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b67cd80c6.mp4?token=J3hFqVALBYQ2TCXG7pUy0hLfIH_tRgcUHv_orRqQfHyfMo_1yS5lUj7uglQVG3UNXc5IQZmr2nOfdbDTUOEASMw8ingGpIvgPeFcg2Vw8XXVsieWnWdcJnkqE7uWJ28RLcHn65PvnHHI73hv8kfkuftL-AFtgHiLm6_xhNqjGdLe1Tf7ztM9_026clyf3QICzCR9A4Btt6uphW19c2czzZ3dvYGVTbpIdtuIbFDEAlJ3U-GlWhJnjKk55oBl02fWabgo09qcyl68dWlgbp20192Wz7tHHZXuFyJun3Ud8bhbJAhct94TA6xohOty9Pb9YYrGUuoPgpfxzONxO4K9Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b67cd80c6.mp4?token=J3hFqVALBYQ2TCXG7pUy0hLfIH_tRgcUHv_orRqQfHyfMo_1yS5lUj7uglQVG3UNXc5IQZmr2nOfdbDTUOEASMw8ingGpIvgPeFcg2Vw8XXVsieWnWdcJnkqE7uWJ28RLcHn65PvnHHI73hv8kfkuftL-AFtgHiLm6_xhNqjGdLe1Tf7ztM9_026clyf3QICzCR9A4Btt6uphW19c2czzZ3dvYGVTbpIdtuIbFDEAlJ3U-GlWhJnjKk55oBl02fWabgo09qcyl68dWlgbp20192Wz7tHHZXuFyJun3Ud8bhbJAhct94TA6xohOty9Pb9YYrGUuoPgpfxzONxO4K9Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو دربارهٔ تحریمِ دادگاه کیفری بین‌المللی: یا دادگاه کیفری بین‌المللی تهدیدهای خود را متوقف می‌کند، یا ما دادگاه کیفری بین‌المللی را متوقف خواهیم کرد.
🔴
و ما انتظار داریم متحدان ما، بسیاری از آن‌ها که عضو دادگاه کیفری بین‌المللی هستند و برای دفاع خود به نیروهای نظامی آمریکایی متکی‌اند، این دادگاه سرکش را مهار کنند
🔴
اگر این کار را نکنند، ایالات متحده کمپین خود برای تخریب دادگاه کیفری بین‌المللی را تکه‌تکه ادامه خواهد داد، تا زمانی که آمریکایی‌ها دیگر تهدید نشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/151794" target="_blank">📅 18:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151793">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بقائی به فرانسه: استفاده نامتناسب از زور علیه تجمعات دانش‌آموزان را متوقف کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/151793" target="_blank">📅 18:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151792">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: امارات و عمان در اجرای سیاست انزوای کامل ایران با واشینگتن همکاری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/151792" target="_blank">📅 18:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAw4H6YChx36A4r-MgwdD7RulkQH9mTr8nmF0Spr2NUS7PWdKHQlfEr-yYEWnX_nyXUXlFovR_r55dCuDrSPa5-PAxGvGhcxCQJY6DFukQ9W21iTLbX4q8hnUlQQRUAzgiyLa8KUU__ppb4dvSSqHM3pXMP88AsZvvhmTGYXwAqtzD7M4Xva08966_xhEy5mO1GVKkdUjsBtWDPeO24smvWweliAfRKXN4EzhGdkAzpo0i6LhNvaJ7gRYl6HTpHI6tSo1EcOAe9eB9yX-naXAHxmfdOfFUjAcD1Dt3ujuadIKu7ShlmcnHF9Eb_Cbu4UlqO9OVeesiWwH_G4TY0B-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H07mjEVEwrnLW26DsgYiThZhCXXf_GLSjrMDju5Ld3Z_PyjYeMvYOv0iHlNDgXEgKhuNrJJTVjwwFarBZZL8Pk36HjivI10vG-QKf8wrB0FcKnq61GU2nCSea9KFdXlfN7kcEJXBqFlLnAbxay3fri-k0tehrkWCBOv4nW0ORajlcLlqvHTMQ1M7NT4f1tyM-5VXt3XT8KkbRrr2YCTn4aohLg-_VKP4psy1RZo8zul4CG2W8iZ0J5Nqn0TXuQfKp8MPxssAjTqL6u6kpkU07VzolNMkTuWAoz6fwGyZRhV89yvusgV6ZEMN450kBGAVNoZ1d9UooKKPjkMi3nRelw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=sMMasTh8hRNaSUMDOj7JclPQwbc5_Hc5vnlkhj9FDzUXFrnqAVDQcphu5_z16dKsWeSocJ1vyeEqorxPTE1-nczmXuwoAJjxrtYGx1MyzQhOmm5lpuoP2ZBzbdQ3DpMDYu-nIsKrf3Hlt3zqE8FAZY6BUpyc3IigR6TcMDhl8OuEsW9j4Nd6_DXq-4Ur6rwqcchlRuEjMyt8MkSNWjgpnJsCcyQ_sdcNCAaW4dNGA11u6Z4lEDBwueB2BBOPutZxbvwIxHXAykK3austALe4NgsrLpH_zKEleX6MtkC8fq_YQulPw51zn8zgCaBycxKfseW6mQSSfLEx00CM1MUz-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=sMMasTh8hRNaSUMDOj7JclPQwbc5_Hc5vnlkhj9FDzUXFrnqAVDQcphu5_z16dKsWeSocJ1vyeEqorxPTE1-nczmXuwoAJjxrtYGx1MyzQhOmm5lpuoP2ZBzbdQ3DpMDYu-nIsKrf3Hlt3zqE8FAZY6BUpyc3IigR6TcMDhl8OuEsW9j4Nd6_DXq-4Ur6rwqcchlRuEjMyt8MkSNWjgpnJsCcyQ_sdcNCAaW4dNGA11u6Z4lEDBwueB2BBOPutZxbvwIxHXAykK3austALe4NgsrLpH_zKEleX6MtkC8fq_YQulPw51zn8zgCaBycxKfseW6mQSSfLEx00CM1MUz-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی عربستان به صنعا
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/151789" target="_blank">📅 17:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
صداوسیما: با درایت مسئولین و پیگیری ها، سیب زمینی ارزان شده و به کیلویی ۷۰ هزارتومن رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/151788" target="_blank">📅 17:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVeHCJNeGzL94xJSLLjO6I5dKZyvoL1ybijcBe0JO0CWwcMX3GLQD5k_ZyolaDnVnlmXXiU_MNGCuK1ON48Yq-RO2godW4tlXo3MKZsCwuOYjreWTPZLF9Q-I1pDyeNcfKYoiHd0BhlaXHVvNKBQjBbB9wqjKfqrztE6FQddfA9vf0mAk08atEcfv4YYRS54BGDvJZmJpwIa5Uh_-u4kt_j06vsYYEHGXlJ4weohfE2W43T5TeFsEpc4utbUsWmxypggHpg08-vO0p3N7rO6ommXO5pyZ-ScggNEc6VE2vjVcJhHvIUzkgfdfXzZMsegwKk80vSiSL40AvDjHPlu3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) پس از دریافت گزارش های متعدد مبنی بر اصابت گلوله ناشناخته به یک کشتی در حدود 13 مایل دریایی غرب الجزیره، امارات متحده عربی، در حدود ساعت 10:00 امروز UTC هشداری صادر کرد. این برخورد باعث آتش سوزی شد که از آن زمان تاکنون خاموش شده است. وضعیت خدمه، میزان خسارت و هرگونه تأثیر زیست محیطی مشخص نیست
🔴
مقامات در حال بررسی هستند. این حادثه در خلیج فارس و خارج از تنگه هرمز رخ داد. این در پی حمله روز چهارشنبه به یک نفتکش در حدود 51 مایل دریایی شمال مدینه الشمال قطر است که بنا بر گزارش‌ها تلفاتی برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/151787" target="_blank">📅 17:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEESZojdXnvZyIVHqvY_0TwMkKmcD3s8IBmd7ltAaDzqawj00LL-VvcLKWTpl6SiFBFJYdsw2sfjh0KmD7S37OGmrHZWPIwnbKP7tQAonwqrPSoFpg-BAW2wyet3QUvNNUwQ8hd-K40EbUopqLyRTdsgsSpFdemIFFOw3mHLXUX2Cr8-tYaQdeCIoxT_1kvhTxJiL7JCZwq1k7YHamkhSUwzDVrCnkkT7OE2JLp8P9HmH-TMe3uiLgBG5cp89qmTQuMPIqUMcqKsYrN94QkDgEaOPtPxsC7x_Brg2Y1mQTVBk3w9xs26ruIXpKXRh7O7RedkHof-xS7vWst1430zZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: مردم آمریکا میگن که آمریکا در مقابل ایران شدیدا شکست خورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/151786" target="_blank">📅 17:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151785">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وال‌استریت ژورنال: پالایشگاه‌های نفت آمریکا از جنگ ایران و اوکراین سود‌های کلانی به دست می‌آورند
🔴
اختلال در فعالیت پالایشگاه‌های خاورمیانه و حملات اوکراین به پالایشگاه‌های روسیه، آمریکا را به آخرین تأمین‌کننده عمده سوخت در جهان تبدیل کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151785" target="_blank">📅 17:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری/ وزیر خزانه‌داری آمریکا: دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/151784" target="_blank">📅 17:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
دقایقی پیش یک بمب کنار جاده‌ای در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان منفجر شد.
🔴
اخبار اولیه از جراحت چند نیروی پلیس در این حادثه حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/151783" target="_blank">📅 17:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
هم‌اکنون گلوله باران مواضع حزب‌الله در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151782" target="_blank">📅 17:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74a32557b.mp4?token=c4dGzkuqax9UcKXjSsfFS3HqoeWtkdQeF2EZNEe8kZXmTweoA9j0amtQ-4oVQpqu6hjJuHAENnEvxmZhhMnZ1uQTPd604wijUJCrmPFyH7T70Be1T0PcF7AlkIU8w8tiTcL2h3thiqLTlzykYQc7Df2SWzWp9iAIcvyU05AKGwAycTwY56yIQCteRrIxpi5u3LfF5GXvcGK55lUadmmqB_rF0qiV4ifJuToMxiFfDy_56XYxZWoxYxjOznvKUkzkdvBTxunI_tt1SWzJD7IPR6IQ8O_5FVFi0g52Rk27IzU34ZmFW8OQoZ802V_ObQcbVRwmK6m2OhK-fHOG3Mmvwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74a32557b.mp4?token=c4dGzkuqax9UcKXjSsfFS3HqoeWtkdQeF2EZNEe8kZXmTweoA9j0amtQ-4oVQpqu6hjJuHAENnEvxmZhhMnZ1uQTPd604wijUJCrmPFyH7T70Be1T0PcF7AlkIU8w8tiTcL2h3thiqLTlzykYQc7Df2SWzWp9iAIcvyU05AKGwAycTwY56yIQCteRrIxpi5u3LfF5GXvcGK55lUadmmqB_rF0qiV4ifJuToMxiFfDy_56XYxZWoxYxjOznvKUkzkdvBTxunI_tt1SWzJD7IPR6IQ8O_5FVFi0g52Rk27IzU34ZmFW8OQoZ802V_ObQcbVRwmK6m2OhK-fHOG3Mmvwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تریتا پارسی: بعید می‌دانم جنگ سوم از جنس جنگ اول و دوم آمریکا باشد که به بن‌بست خورد
‏
🔴
اگر چینی‌ها درک می‌کردند که دور سوم آنقدر بزرگ است که آن‌ها نمی‌توانند خودشان را از تبعات آن دور کنند، ممکن است وارد عمل می‌شدند تا جلوی آن را بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151781" target="_blank">📅 17:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پزشکیان در نشست سران کشورهای مشترک‌المنافع: جنگ‌های اخیر منطقه نشان داد که امنیت و ثبات منطقه‌ای مفهومی تجزیه‌ناپذیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/151780" target="_blank">📅 17:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab6397cd2.mp4?token=uTlWtbsyhyfLzVZ01cex3yK_F5BcTSTCVDUcDckm7bnzZSKEWN8AJfVwe3x5Gq_WNDsEdMFK7ENtVUrC0ohFV03FdK4k7ifamV90Zv7_GkFpXL2RSBPHOuQ8cXCm52TRFYOKAfuo5_6WQnb9WpvK1Qbc1Jarl3Ca_lK5Z0kVostQmjutmyQELKTNLDvYHcDZk8l3uZ3ufN830bDwCnmCwsIuQ-6DdMLv08MQVaxvutd0iRwZQWDBwzcusqMBs-jRe4lGXoSJfqSafPXl7lOOxupJsYMJGryQYk32tHWGCKkuZRuKfoRClTJU0o7QbcBWrH-___UJE_xOadBbO311lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab6397cd2.mp4?token=uTlWtbsyhyfLzVZ01cex3yK_F5BcTSTCVDUcDckm7bnzZSKEWN8AJfVwe3x5Gq_WNDsEdMFK7ENtVUrC0ohFV03FdK4k7ifamV90Zv7_GkFpXL2RSBPHOuQ8cXCm52TRFYOKAfuo5_6WQnb9WpvK1Qbc1Jarl3Ca_lK5Z0kVostQmjutmyQELKTNLDvYHcDZk8l3uZ3ufN830bDwCnmCwsIuQ-6DdMLv08MQVaxvutd0iRwZQWDBwzcusqMBs-jRe4lGXoSJfqSafPXl7lOOxupJsYMJGryQYk32tHWGCKkuZRuKfoRClTJU0o7QbcBWrH-___UJE_xOadBbO311lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان در نشست سران کشورهای مشترک‌المنافع: جنگ‌های اخیر منطقه نشان داد که امنیت و ثبات منطقه‌ای مفهومی تجزیه‌ناپذیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/151779" target="_blank">📅 16:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
عوستاد رائفی‌پور:  الان دشمن دنبال اینه جای رهبر رو پیدا کنه، حتی از روی پیامای متنیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/151778" target="_blank">📅 16:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b3a06504.mp4?token=bcX-x5HRnZQKAfkmelWm_QLgG5l7FE1WZwn1LrZWecZrTcmEfrKB6D4uVK2YvzIJZPIl9E7up5ZZC3wOTlqm5wqPNZYZXa8Y5oGgvySPEbRxTRXVhl_CkNiVM79SMoBGlambPZ3fVHL-HT_S0ssZ1xGQaYRUHd04KuTRkBUYidy0IkXuJLso7sIyPVcLFR04FkO0Orw_wuyvJgmBXRkFW-CNejSEUmrRp0DFdctz2ef-eVUyOwL8UEjSaypT9UYdYlgO_2rDapeO8Pnx_CRkVj31_o7u1fcq2Z6DE8SidoeY_w8Mo6Nj6qlq5al6YdSXDIo3BEtdlSLRlO5WNosNBXRdzlteA5QR50MwKFKAcTGliSYuGcs6wdIdEfscaoWPyUGFBxaaYEnJ6bVaj3hx_cd59GNhTpzUomJ1uLPxNhr1HR0xtLehTKDAKDvv9SjPeTe_jlLJRboP_BOSSdztt5EmQykXJQOglFD_Nmv36w1Nxp50LMywEtl0FYzl3g3rEO5UpoxdxTSLotPB9YhSJTZwH_lG-a8Lskf7DermS_KTSjgO5uJOq7cwF0bO36im2bk-p9I-MdZFl8YQY965y82tEziiALUKDdTnQX3WSisROts65sBO_Qci1nQ9NCWs0wvVIbpkqPYz12H78sZmILCZZNhfCQhJbtX_SaLGUVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b3a06504.mp4?token=bcX-x5HRnZQKAfkmelWm_QLgG5l7FE1WZwn1LrZWecZrTcmEfrKB6D4uVK2YvzIJZPIl9E7up5ZZC3wOTlqm5wqPNZYZXa8Y5oGgvySPEbRxTRXVhl_CkNiVM79SMoBGlambPZ3fVHL-HT_S0ssZ1xGQaYRUHd04KuTRkBUYidy0IkXuJLso7sIyPVcLFR04FkO0Orw_wuyvJgmBXRkFW-CNejSEUmrRp0DFdctz2ef-eVUyOwL8UEjSaypT9UYdYlgO_2rDapeO8Pnx_CRkVj31_o7u1fcq2Z6DE8SidoeY_w8Mo6Nj6qlq5al6YdSXDIo3BEtdlSLRlO5WNosNBXRdzlteA5QR50MwKFKAcTGliSYuGcs6wdIdEfscaoWPyUGFBxaaYEnJ6bVaj3hx_cd59GNhTpzUomJ1uLPxNhr1HR0xtLehTKDAKDvv9SjPeTe_jlLJRboP_BOSSdztt5EmQykXJQOglFD_Nmv36w1Nxp50LMywEtl0FYzl3g3rEO5UpoxdxTSLotPB9YhSJTZwH_lG-a8Lskf7DermS_KTSjgO5uJOq7cwF0bO36im2bk-p9I-MdZFl8YQY965y82tEziiALUKDdTnQX3WSisROts65sBO_Qci1nQ9NCWs0wvVIbpkqPYz12H78sZmILCZZNhfCQhJbtX_SaLGUVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان در نشست سران کشورهای مشترک‌المنافع: تحریم علیه ایران، اقتصاد و نظم منطقه‌ای را تهدید می‌کند؛ ایران یک مسیر مناسب برای اتصال آسیای مرکزی به اوراسیا و آب‌های آزاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/151777" target="_blank">📅 16:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وقوع انفجارهایی در اربیل عراق
🔴
منابع عربی منطقه از وقوع انفجارهایی در اربیل واقع در شمال عراق خبر می دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151776" target="_blank">📅 16:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نیروی دریایی سپاه : ساعاتی پیش کشتی غول پیکر حامل گاز ال پی جی به نام اِن‌وی‌ سان‌شاین متعلق به شرکت نات‌ویت که قصد عبور از مسیر غیرقانونی جنوب تنگه هرمز را داشت مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151775" target="_blank">📅 16:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
به گفته برخی منابع جمهوری آذربایجان به معلمان محجبه یک هفته فرصت داده که حجاب را کنار بگذارند و یا استعفا دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/151774" target="_blank">📅 16:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151773">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJIW70Z9ow39g-dcYRt1XcIOqwxY2zUj5gQ8FQlAQs_6gpqbL8Tqy2b897rVjo3gxz3omiQ8i5wsr7p9QmcCWpQXmc3B8tgOkykJIdnklXEbNJmvyeUsJHeqpE1l8eUv1K_2BcRiWHYPFRLUmcMulfieZl-41Dv8QADm1tljlA43qGMAwDa4Js0NHks5hACND2gpmOImZRkKv3pSk_a1VisLUrOeaLa6lX1VcVAN2qBBc4JytX5YlG2TG3hgktv86JvCN1YN-xtLHKMOoa1uFD7hTO7yncPyH3HG1nziGnND8RR09iduz-xe_wf78u9FZF7cPtHOWoakU4J8I_aPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان، بار دیگر دونالد ترامپ را برای دریافت جایزه صلح نوبل نامزد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/151773" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151772">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbkxkSpKvqjwDJgnh5CDxokit7f9UlkFSrRfahoW85jCDkzG4rglPju9rtAgHs1QzHcdnoQXUin6gR2caDwdLw6EDU81Z1AIYInpvxw8OLOnGgRKQ9Z2F_ty-o-AW5n18xkxfu2z7tZo4DcU0Fq3Sn1HOxZURO_VuaHG_s2Dur4k91a6ITW1CgYI5ed40USANYCFUa9zLmNdDy7noVCcTMjW9uxthG-yVimNjgWKeEQtnd_5x4hIwrn6C4vp6RkFi-IeLWIYY5lv1PKuq1Wap9tmnr2sI-1pSn2MsELB44ZrWsWlwmnr_zYYIEVPhl1OHZFZJ8G9_iTL6QJJv9cvoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثروت ایلان ماسک امروز به ۱.۱ تریلیون دلار رسید؛ این رقم معادل ۲۹۶,۰۰۰,۰۰۰,۰۰۰,۰۰۰,۰۰۰ تومنه
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/151772" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151771">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اکسیوس به نقل از یک مقام آمریکایی:
واشنگتن رئیس ستاد کل ارتش اسرائیل را در جریان آمادگی‌های نظامی آمریکا برای ازسرگیری جنگ با ایران طی سه هفته آینده قرار داده
🔴
زامیر در این تماس گفته که ازسرگیری جنگ می‌تواند انتخابات اسرائیل را به تعویق بیندازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/151771" target="_blank">📅 15:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151770">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5QZ7lqUVzlUG4sXf-y7QkMqLCo9tu7qBaIs3r5dnvsujQGcM-2Ox3tW0r_67hbK-VWy9-dqRKaeIbTyC9Lt8It-9O0Cc--sDIdHLaiCeFquuCm3g2TUBzsFLZe0aF0UW3VzZqEPfRbH6xcCuGPeOWHWSfFtYQEgvPdg_54rnUnnvfqmUK3PTJT6t8P72db3qpc63SK_Ab1gCkbRlZoOxHHFGo3CMZ8QnI88sh7EOk1_eTDSuXQDbMo62Bq_H9BG5UflNbLRwDSq_Y1N3Y6kZwu92LK74g22fxOSH2cPM7Jzdosj38CvWDZGSHt8VhEFPATW5wzAEJDqX2UdsqUgMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ورود توده تندری به همراه صاعقه‌های شدید
🔴
چیتگر تهران هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/151770" target="_blank">📅 15:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151769">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پزشکیان به دبیرکل سازمان همکاری شانگهای: تاثیرپذیری از آمریکا و عدم استقلال در تصمیم‌گیری، منجر به از دست رفتن قدرت و انسجام شانگهای و بریکس خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/151769" target="_blank">📅 15:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151768">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اتحادیه اروپا:
توصیه می‌کنیم از پرواز در بخش‌هایی از حریم هوایی عربستان سعودی که در منطقه اطلاعات پروازی جده (FIR جده) قرار دارند و مشخص شده‌اند، خودداری شود.
🔴
منطقه دیگری در شمال‌غرب عربستان سعودی نیز به فهرست مناطق پروازی‌ای اضافه شده است که توصیه می‌کنیم از پرواز در آن‌ها اجتناب شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/151768" target="_blank">📅 15:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151767">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ابراهیمی عضو دولت رئیسی: آمریکا نمیذاشت تو ایران بارون بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/151767" target="_blank">📅 15:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151766">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
بر اساس یک گزارش آمریکایی، ارتش آمریکا در حال استقرار و تقویت سامانه‌های پدافند هوایی در سراسر خاورمیانه و افزایش نیروهای خود در منطقه خلیج فارس است.
🔴
همچنین گزارش‌هایی از تقویت قابل‌توجه پدافند هوایی در اردن، عربستان سعودی و امارات متحده عربی منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/151766" target="_blank">📅 15:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151765">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیر انرژی ایتالیا اعلام کرد در نشست وزیران انرژی که قرار است هفته آینده در ریاض برگزار شود، حضور فیزیکی نخواهد داشت و به‌صورت ویدئوکنفرانس شرکت خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/151765" target="_blank">📅 15:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151764">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
آمریکا دوباره به سفارت‌های منطقه هشدار داده
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/151764" target="_blank">📅 15:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151763">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مقام آمریکایی به العربیه: ارتش آمریکا روز یکشنبه در آستانه حمله تمام عیار به همراه اسرائیل به ایران بوده است که در لحظه آخر حملات به تعویق افتادند
🔴
نیروهای آمریکایی تا نیمه‌شب به وقت آمریکا، برای اجرای حمله‌ای نظامی و گسترده علیه ایران در حالت آماده‌باش باقی ماندند و انتظار تا ساعات اولیه روز دوشنبه، برای صدور دستورهای نهایی حمله ادامه یافت اما در نهایت ترامپ حملات را به تعویق انداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/151763" target="_blank">📅 15:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b45c931b.mp4?token=O_f63tABzcKSdGXGjjQ00N3C4rCUnMIlPM-Jy59RpXE-RUP4ohQ_w-yGoyApc2CNqeov60IxV6V73jtSINbsyKQil7J1dsphZMDEeHfxRsraudw_4_TGwQmv6mTNMx2tS99V5L6aLeXBvnHLf2XyfMwXNjZyLRKz3zWkM3lNDZhuQluhPefpNLoF7D5686UBEHMy9zapSOvvG6FqEYMzsc6s1Qrm4seBLiaxUbUA7Z4NvUZJhi2wbvZTQnPnJwJeWbnAbquwxa74L-1SNWIWPx7k1v8a3fKNrlw3Wp5IyqcHPRQd2_kVqr59PN1EebD5L_ZBaUmXCOy78RgnBV0E4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b45c931b.mp4?token=O_f63tABzcKSdGXGjjQ00N3C4rCUnMIlPM-Jy59RpXE-RUP4ohQ_w-yGoyApc2CNqeov60IxV6V73jtSINbsyKQil7J1dsphZMDEeHfxRsraudw_4_TGwQmv6mTNMx2tS99V5L6aLeXBvnHLf2XyfMwXNjZyLRKz3zWkM3lNDZhuQluhPefpNLoF7D5686UBEHMy9zapSOvvG6FqEYMzsc6s1Qrm4seBLiaxUbUA7Z4NvUZJhi2wbvZTQnPnJwJeWbnAbquwxa74L-1SNWIWPx7k1v8a3fKNrlw3Wp5IyqcHPRQd2_kVqr59PN1EebD5L_ZBaUmXCOy78RgnBV0E4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراضات بعد از فرانسه به بروکسل و بلژیک نیز گسترش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/151759" target="_blank">📅 15:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دو مرد ایرانی در لندن به اتهام انجام عملیات نظارتی و شناسایی مقدماتی با اهداف خصمانه علیه سفارت اسرائیل، قدیمی‌ترین کنیسه بریتانیا و چند مکان دیگر مرتبط با اسرائیل و جامعه یهودیان، متهم شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/151758" target="_blank">📅 14:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ما قصد داریم به عنوان بخشی از تلاش‌هایمان برای منزوی کردن اقتصادی ایران، تقریباً ۱ میلیارد دلار دارایی ارز دیجیتال را توقیف کنیم.
🔴
هدف از کارزار انزوای اقتصادی، محدود کردن دسترسی مقامات ایرانی به منابع مالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/151757" target="_blank">📅 14:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
میرسلیم، عضو مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151756" target="_blank">📅 14:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swX-EOnWhXBx51efiI9WqZERHWb-Jl4Rl625S5AUsR7Vry_gfUSUEOak9TA8yulu1vc-NTSipvozVwzMYEQQs03Z_37118aRWwqQhGzBC0ZmWxbAFNnAioBauJqgYheg3GUchj7B2PSIhUjmIjXkgFcDOYi8oXLUwFkv8YG2sjpffHCRwCbuznmHdWBINpcGzw6wUkaz6edwVDqSWGC7jzIzUYy8A-Tp6YKGjHjV18oCFDa7zT62JV1etPhZtBBSahkGYr1gh29H2GBEY4rnxi4wLsMjqp3kpFOsue5q3cW1VXcIBn-gl2gX05-LGerXSAncBIlB-BRiLmAIHi_5VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور پزشکیان در کنار سران حوزه خزر
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/151755" target="_blank">📅 14:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5K0ybWLSAkpq2XOxm25zWVergKuHB60JUrgtMQ15hj1nN1ayxn7brpj3LukKqR0zeYks1cuMlFXc82yvsqzPm-FkXZFBs_Yh2UFznMiPYgSCqlmWLo3RZIzPZqx39XaPGi7HI2Q2A2v4yvocmpeK8M_ot6gwMr8KXx4YPl7UohTr7cVBZtRnOGK2dqKNpJkZECE_CB5bDhyERAAgKCD7cI6kM-o5InwQa_UV_H2wUgjOnfcZLeeixtK72Lg_hdnSuGQEawD5Qzs4exC-k79nQwDKU_JXYuKzpPOxZPmsQwzDMMkwMmak6B17HgGoUWhx8vhbfAwnwLM4tiH5ojWDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلمان:ایران در حال آماده‌سازی برای حمله به تاسیسات آمریکایی در آلمان در صورت تشدید تنش‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151754" target="_blank">📅 14:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پزشکیان: ایران همواره به گفتگو تاکید کرده است اما گفتگو زمانی کاربرد دارد که در سایه زور نباشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151753" target="_blank">📅 14:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
زلنسکی آمریکا را به انفعال متهم کرد:
نمی‌توان از یک سو با روس‌ها درباره پروژه‌های اقتصادی آینده مذاکره کرد و از سوی دیگر گفت که در نوعی بن‌بست دیپلماتیک قرار داریم
🔴
پس حقیقت کجاست؟ این چه بن‌بستی است؟ این یعنی بی‌میلی
🔴
استارلینک را برای اوکراین فعال کنید؛ به ما کمک کنید از آسمان‌مان دفاع کنیم و در آنجا برتری پیدا کنیم، آن‌وقت پوتین پای میز مذاکره خواهد نشست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151752" target="_blank">📅 14:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
لوفت‌هانزا و پاکستان پروازهای ریاض را لغو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/151751" target="_blank">📅 14:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سفارت آمریکا در بیروت هشدار امنیتی صادر کرد
🔴
سفارت آمریکا در بیروت با انتشار هشدار امنیتی، از اتباع خود در لبنان خواست با توجه به تحولات امنیتی جاری، احتیاط لازم را رعایت کرده و سطح هوشیاری خود را افزایش دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/151750" target="_blank">📅 14:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nslwBzncUqCbDZtc9JL6d0XXhLjCbQMsaqAYnWFTAULvNZk6z7pTpQLz1zHo3tTqEWytPEatjr7SMR7kpwCIcIw4SMEcm_LeyxfDzlgT1WTWNpYYWbNkGOsWsNHW98w8g4avHF8Nf786gRt9aYTZm8s2byLaEnKDu9xuD43upCsEQRhTL4z0oNy8jzyj6Eh3kyE5cdaQoQza9_aAzRo4hnqOveRBdCw8_QHtFQ5ZzWv1Qe-0c-cZM6tp2y79YamIkxgY85XB9YSHwDoo2TzwbZoDCQokhZdoOSSw5IDTWgEKDgGsQM2kyMeLXpYjqy17e06L_A9gVrdx040c79RL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منطقه خاورمیانه شاهد رفت و آمد پروازهای متعدد هواپیماهای نظامی ترابری مدل C-17 است. به نظر می‌رسد این فعالیت‌ها مربوط به استقرار سامانه‌های دفاع هوایی باشد، احتمالاً به منظور آماده‌سازی برای از سرگیری جنگ علیه ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/151749" target="_blank">📅 13:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
خبرگزاری فرانسه: پاکستان تأیید کرد که نیروهای این کشور در عربستان سعودی مستقر هستند و مأموریت آن‌ها دفاعی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/151748" target="_blank">📅 13:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ادعای نیویورک تایمز: شرکت‌های چینی برای عبور از تنگه هرمز به ایران عوارض پرداخت کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151747" target="_blank">📅 13:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSItvvrkz6i33Nd_abmhTq1sh8Zb0tuNHXAvB0tGycdiRspytQNG_ndqz3aHmXVsm46vqW8_H0a2Eg9smNyNLM90wOTACZFC4d6Lo7zumZUmyu3vPhlhgYPNlHr3iME0BUx-bbYc_oNS21napJrA8Fcx5yVlZov9NAfDqDIbm9jhXZNRA3C0ZG5OdxakcyxUKG-uwVgMIxYlNB3VHdJHoZuSHH3ReYl5_hkC_ABAL4THyf9eggNNW8AnTKs1lRjWmzgWLDRJqi4D7g_mXQripfPWfPgXc2jpZoq4TmGuSWYrBRsaG1lZN9KJVpThL-j21L5HU3BQjM3q4iLow_6Nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار امنیتی آمریکا در اردن
🔴
سفارت آمریکا در امان، پایتخت اردن، از شهروندان آمریکایی حاضر در خاورمیانه خواست با توجه به «شرایط پیچیده امنیتی منطقه»، هوشیاری بیشتری به خرج دهند و آگاه باشند که احتمال لغو پروازها، بسته‌شدن حریم‌های هوایی و اختلال در سفرها وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151746" target="_blank">📅 13:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
یک منبع منطقه‌ای به خبرگزاری فرانسه گفت، عربستان سعودی با آتش‌بس با حوثی‌ها موافقت نخواهد کرد تا زمانی که دولت یمن مورد حمایت عربستان تمام سرزمین‌هایی را که در هفته‌های اخیر از دست داده بود، پس نگیرد. این منبع افزود که ریاض تسلیم «باج‌خواهی نظامی» حوثی‌ها نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151745" target="_blank">📅 13:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151744">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
روسیه: آزمایش‌ها وجود طاعون را در مرگ کارمند آزمایشگاه سیبری تأیید نکردند
🔴
این کارمند ۲۸ ساله به ذات‌الریه اکتسابی از جامعه مبتلا شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/151744" target="_blank">📅 13:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151743">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf5cc17a.mp4?token=dga7MuA46_xSks1TgbBq49k03HxxMDOYJyc8VsOqQbRitjYUXnP6bvBi3MgFKGLeV4crrljiBNfuQjQwr9UifEGNy_d3qKc4uQpCYdMP0dXWAlHMCjUzxLBs7l266-x4_w1bj6gRm4jipbrKhuBC9YtgylT6EAwxJ2qbx6AYDl2XwTfKLvN3sKGaCfwAkXGbrTSLs-o6paL26zWYW7v7PJwVfcHxfrusVdrHgZHLSbaGMV1IAgZw3K3SePbjSQ5ll6lLgX0Z8lqNKN-AGEZ51H2iDwlOI4cz43uPHZIr-82boIGMUXBQEWArxCQ0lj87ZbKqkMHkHI1WDy-iSAI-rw0NPX40f4D5yAIe-eMU8fmFnlUYLDXf9d25J2e-9pXch2pdwQeNwQuWqShGLdSkUHwlcfUhBbHCLZXaLk4iq3ULK9E3xjdqdKX2WEVw16ulUrJZer_f3eVPjtnvv7YsVcoE7mgzfgK3kQU3BT7DBSwZq79Q_xtJPP_n82haZfgHm4EA-TgjlxwHrapCza4GsxCB3seUgyBN2vM9GmPDXXyU3BUEznLuw9lTuO46IilhmSORE7GCm99SgVjl8WD1Bn319B2hUnwwEJq3t-t3WOyIBHVrRTU2ji4__ntMUM6vMlsTdrO0c6cd4iWUghkFLoTJr2YjJRC1Mem97jvfUiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf5cc17a.mp4?token=dga7MuA46_xSks1TgbBq49k03HxxMDOYJyc8VsOqQbRitjYUXnP6bvBi3MgFKGLeV4crrljiBNfuQjQwr9UifEGNy_d3qKc4uQpCYdMP0dXWAlHMCjUzxLBs7l266-x4_w1bj6gRm4jipbrKhuBC9YtgylT6EAwxJ2qbx6AYDl2XwTfKLvN3sKGaCfwAkXGbrTSLs-o6paL26zWYW7v7PJwVfcHxfrusVdrHgZHLSbaGMV1IAgZw3K3SePbjSQ5ll6lLgX0Z8lqNKN-AGEZ51H2iDwlOI4cz43uPHZIr-82boIGMUXBQEWArxCQ0lj87ZbKqkMHkHI1WDy-iSAI-rw0NPX40f4D5yAIe-eMU8fmFnlUYLDXf9d25J2e-9pXch2pdwQeNwQuWqShGLdSkUHwlcfUhBbHCLZXaLk4iq3ULK9E3xjdqdKX2WEVw16ulUrJZer_f3eVPjtnvv7YsVcoE7mgzfgK3kQU3BT7DBSwZq79Q_xtJPP_n82haZfgHm4EA-TgjlxwHrapCza4GsxCB3seUgyBN2vM9GmPDXXyU3BUEznLuw9lTuO46IilhmSORE7GCm99SgVjl8WD1Bn319B2hUnwwEJq3t-t3WOyIBHVrRTU2ji4__ntMUM6vMlsTdrO0c6cd4iWUghkFLoTJr2YjJRC1Mem97jvfUiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۱۱۰ هکتار از خاکِ ایران به افغانستان واگذار شد!
🔴
محسن زنگنه: قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
🔴
البته قرار بود سهم بیشتری بهشون بدیم اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151743" target="_blank">📅 13:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
صلح نوبل بازم به ترامپ نرسید، حقوق دان آفریقایی "پیلای" برنده صلح نوبل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151742" target="_blank">📅 13:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / سنتکام: ما دستور حمله به ایران را دریافت کرده ایم و در حال آماده سازی طرح هایی برای حملات احتمالی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151741" target="_blank">📅 13:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfUZdZJcE12sIspAxu15vZEjC5xh3qpjRCpv0AWVSh3HAn_WTiJVIue-dzZjeGCi_4-QbuHSj89s6zQ7HUkWHoVPT-9X4jyYL-WIznUVzQt4RZ4aoym_6xs_wBfRoVEiru7lp14HBHSBbVZgrEy5wOhzPOuH9OfhjSLUjo3SKSSlOfvU6oB97_M02SMVwH0fEcygvFw1_OnEYEah_AgiySE5i8K3Eg7dWBKGnStDfwMZn3ZcCwROWCJEnEAfr_3duiohvF4odjDhQKmiX3TeHolFKprO8qtek8jgjcwTAUAyf_Y3w3ehNTpz1T9eEXMkXKWNV3ONYhFBceLpQZ4m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنتاگون: اعدام عامل تیراندازی فورت هود به‌صورت زنده پخش می‌شود
🔴
پنتاگون اعلام کرد اعدام ندال حسن، عامل تیراندازی در پایگاه فورت هود، که قرار است با جوخه تیراندازی انجام شود، به‌صورت زنده پخش خواهد شد.
🔴
حسن، روانپزشک پیشین ارتش، توسط یک هیئت منصفه نظامی برای تیراندازی نوامبر ۲۰۰۹ در فورت هود در تگزاس، به اعدام محکوم شده بود. او به ۱۳ فقره قتل عمدی و ۳۲ فقره اقدام به قتل عمدی محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151740" target="_blank">📅 12:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trdNssRlNRTRgrG8JQ66qs64M0WTwJ8BZ2ZE4YsTHRQx4zc8iNqUdE6iup4ZerLzCYgxssIXphXr88QQLer2SqzHh991sV8hrqSHUpx6PiPgW9icacpS1cFIxjnT_MpS115YC52YhaCFkMPmCbvwr0N39hqv6CvD_ngf67CaLZSq1rznLJ5RTNoblCuFk7RxEY3CimgznfNWP2FTLE_oMPqUQOD8rFTJA8QdrmIFUe5vqws9Av_ZvOSaKmp37wteXFovcVui5xgzNrzLphujiP5x3DJ0s-KpgNMnZ0KBuBJ34swlxkmxmhe6LDgtoJ8OF8vkzp03WpkOpAoJpTOMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: «دموکرات‌ها کلاهبردار هستند؛ این‌ها واقعیت‌های واقعی‌اند!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151739" target="_blank">📅 12:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یک منبع نظامی آمریکایی به خبرگزاری "الحدث" گفت: پیشنهاداتی به ترامپ ارائه شده است مبنی بر اینکه به توانمندی‌های نظامی ایران در امتداد سواحل، در عمق ۵۰ تا ۸۰ کیلومتر، حمله شود.
🔴
این اقدام، آسیب جدی به توانایی ایران در تولید انبوه موشک‌ها و پهپادها یا پرتاب آن‌ها وارد می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151738" target="_blank">📅 12:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151737">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
جایزه نوبل فیزیک به شکارچی ذرات شبح‌وار رسید
🔴
جایزه نوبل فیزیک ۲۰۲۶ به فرانسیس هالزن رسید؛ دانشمندی که با ساخت رصدخانه‌ای در اعماق یخ‌های قطب جنوب برای شکار ذرات شبح‌وار نوترینو، بر تمامی تردیدها نسبت به عملی بودن این طرح خط بطلان کشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151737" target="_blank">📅 12:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151736">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد که پدافند هوایی این کشور 505 پهپاد اوکراینی را در شبانه روز بر فراز مناطق روسیه و دریاهای سیاه و آزوف سرنگون کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151736" target="_blank">📅 12:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151735">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e20fa5bba.mp4?token=VMismDL3Rbv1pGZs6ZHmAirYOMCpzRL-CiIV5Sab5BbNpl4N27MeHRMLRwQtC3R0P9_91nhJAND4ewH-sIQIA1kCa3SFTDon8trJT6w9OvrsJMAATL5YdGZQXZGJGnGtsViU503xiLsVncB66VdYc7k_S-umRk_d605vNz9I1t05ZGiFdWFNLtoDlwWfleBv8wESvTH__dr5laZ7iNzyNDTSBBuCRxd7eYhGvMjeaeGZOKaF6NNtPaOjQBGjWJbgs9FAGycM-rFY1XdHoqysQgLFuEyzYs03BUkcIAUEHsDaZ5Lo7PPj0Syrxe-UMexTKX3_v5fTLq7_SGIBiiqfIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e20fa5bba.mp4?token=VMismDL3Rbv1pGZs6ZHmAirYOMCpzRL-CiIV5Sab5BbNpl4N27MeHRMLRwQtC3R0P9_91nhJAND4ewH-sIQIA1kCa3SFTDon8trJT6w9OvrsJMAATL5YdGZQXZGJGnGtsViU503xiLsVncB66VdYc7k_S-umRk_d605vNz9I1t05ZGiFdWFNLtoDlwWfleBv8wESvTH__dr5laZ7iNzyNDTSBBuCRxd7eYhGvMjeaeGZOKaF6NNtPaOjQBGjWJbgs9FAGycM-rFY1XdHoqysQgLFuEyzYs03BUkcIAUEHsDaZ5Lo7PPj0Syrxe-UMexTKX3_v5fTLq7_SGIBiiqfIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که صبح امروز، آتش‌سوزی جدیدی در میدان نفتی خریص در عربستان سعودی رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151735" target="_blank">📅 12:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151734">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
پروازهای پاکستان به عربستان تعلیق شد
🔴
سازمان هواپیمایی کشوری پاکستان (پی آی ای) اعلام کرد که تمامی پروازهای خود را به مقصد ریاض پایتخت عربستان سعودی به حالت تعلیق درآورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151734" target="_blank">📅 11:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151733">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بابک زنجانی: تا وقتی نفت بالای ۱۰۵ دلار باشه آمریکا ۱ موشکم نمیتونه بزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151733" target="_blank">📅 11:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151732">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MN7TinqgqPu9S5Rmw715xDGGe1m1wStM9joJO-tkhBdBP4XhqDRjvzf78FbcbOq-2Va5X8F1lLZbuKYhZmHzj9HrVkXwigVT2SKmI4TA03lALpwZ9ptSq8ufceYwjQQMuFzkRItgV8Sry5oPIuqO4BbFXqMP-R9zb-7eIS27EZ1dsz7BaDd3WR31u3xPv1RBWDx7c3zFHPKj2PfAW52pNN5fqHpFu9vmQiTJif9hfkrMWJKAlJdBuv3NlFXQaYU_QTdWrlxzOKVKObSkZzwT5ExtITte1_hgqEyKyl1U-s-oKdY31TN2VyBuLzBnNkvA1TG81Z_lLZZa3p2edsMajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
درخواست از گوگل برای حذف سایت همسریابی «آدم و حوا»
🔴
تعدادی از سازمان های مدنی و حقوق بشری خواستار حذف اپلیکیشن ایرانی همسریابی «آدم و حوا» از گوگل پلی شدند.
🔴
این نهادها مدعی‌اند این پلتفرم «ازدواج کودکان» را تسهیل می‌کند و دختران ۱۳ تا ۱۷ ساله را در معرض جست‌وجوی عمومی کاربران قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151732" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151731">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LPHUpnbOtEYbokU4yT4jXzi_P8H2dwz7QrNpKnUVq6LXYPg4MxnHScp3TI3AJKCELQL-5iljhyliPDMSZjTH5efXMqTbDklWfq_6ZFHYdwPfqQcZaH5OHE7S5wAVsC9v1-TUZsM_9J-xvMHLU-3DPG_JyxcAykCalCLyMQtKYyDudji_vKYmSJRUiSutEadWX-p87NyI01_x9ziQVa2rKpZC3-STqGKyqxFx5P7N9NhO40o9heJbcMV5RbNKSgiF4eOtwX04FyoMhQPi4II2YkcrUwvmwhWYJAJtclyvoaRo79HauMYiFxXs7VTnLNWkQdXIDevRPRxZIjCd2x-hGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بالاترین هشدار امنیتی در کره جنوبی صادر شده است
🔴
دوربین‌های امنیتی بخش زایمان زنان در مراکز درمانی توسط یک سری افراد هک شده و درحال انتشار و فروش فیلم زایمان ها در سایت های مستهجن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151731" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151730">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWcthvLlOpWOtQnz7hY_oTW4Czu6DcLQgwNZJrDHoGa-0HODD6CQMGMFWwyVIjwreWoUQa9J7ASQXwIjiV_SQNa2x7k-o25kT9hbAhnhKEHOUrQjZWU5r9NGVkJCP1Im_OuutjYUtcFyBtjRlA7HI0-mlzfPlmBPGidN0-yHFfzkBaA1oAbe2RPFBKqC9-PSQd9fPWxCGvT1Ze0x7e5o-A20ysX8sbUiJzS28Ogg_qLbtNlbTVu1-rahYrJanP0aIlH-lA1HpLQTynx8tnIPzwMZtf5MR9zR9PRPDSh9eM9PNVwS4G3vRaMoi834JOWflaVV53SaVyJIKfH0CCZrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان هواپیمایی غیرنظامی عربستان سعودی اعلام کرد که فرودگاه ریاض مورد دو حمله قرار گرفته است. حمله اول به تاسیسات فرودگاه و حمله دوم به یک هواپیمای سعودی انجام شده که در نتیجه آن، ۳ نفر کشته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151730" target="_blank">📅 11:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151728">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVQtZiUbNQgUbZ1ef7DaHdt1_FQwgc8toJnsxcHDGk9zeVcnToNOKKQy8IROdzlEuAaFiY1b0HmtrFryMdqpAarhzyYUeGkJAPDhYspF_JC6_ny3HhAvv3yt1TfR6ZqiFgWRHaF-TQjwagfAJJRY8mvO6BHa6W8LnygG7_c64StTYr3zdzxPDPSoqguQEY0Eta8mN1Rl9Dhk2-jxSm5NfigfjlcxLAGDez9A6jdcjgNRXatAae7LT0Ki_rHAbLxEpEEQBWxI_S_Vt02RTALw4gBAtukTIhekEkpnR9x6V65eb8Jg2yNnDS05p9zyHiv3UbLW64S-BIXot9kMOLxUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حداقل حقوق کارگران در ایران و کشورهای منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151728" target="_blank">📅 11:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151727">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: رئیس ستاد ارتش اسرائیل، بنا بر گزارش‌ها، دو روز پیش از مقام‌های آمریکایی مطلع شده که کاخ سفید و پنتاگون در آستانه یک حمله احتمالی گسترده آمریکا به ایران طی هفته‌های آینده، دستورالعمل‌هایی صادر کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151727" target="_blank">📅 11:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
طوفان «سیمون» جنوب مکزیک را درنوردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151725" target="_blank">📅 10:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سفارتخانه های آمریکا در منطقه برای شهروندان آمریکایی هشدارهای جدیدی را صادر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151724" target="_blank">📅 10:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccb7bcf6e7.mp4?token=F4iu0G2hb5gcuwnT6Bczg6gDXY76HZC9awsirZ51kqBEcv6sZpYZKwfkfompLikbxArSmWRC0FPxesHoJLm6yfVzTr6NlZxfpQDnAHxtEFamO-1wj0HeRzl7lO7v34VNZDJbRdsgzP259Vis1TO8GOQ2mWCG4j_0SCSK5ogpXwNZm1ZChH6pwmYsN04dzb02tJPULWs_LlomYLIaCUepoAzoRkXM_Y43ILqaij47SbgkeAMCAEp7buYCseAog8-qrGXGg9HKwaDK9SWRh-w3ekoXi2Aq1z-fVvkMoLufQZfFZt2G0GYXaZ-NCRTyICQ8P05-2X-jZrK92okDiliORg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccb7bcf6e7.mp4?token=F4iu0G2hb5gcuwnT6Bczg6gDXY76HZC9awsirZ51kqBEcv6sZpYZKwfkfompLikbxArSmWRC0FPxesHoJLm6yfVzTr6NlZxfpQDnAHxtEFamO-1wj0HeRzl7lO7v34VNZDJbRdsgzP259Vis1TO8GOQ2mWCG4j_0SCSK5ogpXwNZm1ZChH6pwmYsN04dzb02tJPULWs_LlomYLIaCUepoAzoRkXM_Y43ILqaij47SbgkeAMCAEp7buYCseAog8-qrGXGg9HKwaDK9SWRh-w3ekoXi2Aq1z-fVvkMoLufQZfFZt2G0GYXaZ-NCRTyICQ8P05-2X-jZrK92okDiliORg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل ناگهانی در پایتخت شیلی خودروها را با خود برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/151723" target="_blank">📅 10:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151722">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
بیژن مرتضوی: بعد از ۴۸ سال برگشتم و به جرات میگم که میگم هیچ جا ایران نمیشه، عالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/151722" target="_blank">📅 10:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151721">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
بیژن مرتضوی: بعد از ۴۸ سال برگشتم و به جرات میگم که میگم هیچ جا ایران نمیشه، عالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/151721" target="_blank">📅 10:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151720">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کرملین: پزشکیان در دیدار با پوتین، پیامی برای ترامپ نداشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151720" target="_blank">📅 10:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151719">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mf5tdveRs8VY4treZwR7S2rZjaAV9--V36DAmNAQsf7CpiNoUgcMRrwe8ErwS46CKs2piXFgrENEeV8mppcv6NbQ95LfJfBvjPqjRwpyIoujTlxfUnGRmi0ANJhuiNTX-rw1CEqJq3_9zslCrp3Me4IWGKmPSLpANPRaRqY-qC73nqIPwOQTc-Jb3ro3kn7-PL7_fCGuJiYBt0LsZDFvut17QqmSuV_jnDAjHuo5eXPcuGAJgW1vEcf57UxjzhdEOVIJj50y_g8Ru3DhEuQAXka_2fjNKKErpdrncecaubcnMBq1YDulQLhHvLzc5HZMvm_r8mkcrLv3evvKUYoqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر آبراهام لینکلن آمریکا در پایگاه هوایی دریایی نورث آیلند کالیفرنیا تصویربرداری شد؛ بدنه ناو دارای نشان‌هایی از عملیات «خشم حماسی» علیه ایران است.
🔴
بر اساس آمار اعلام‌شده، گروه رزمی این ناو مدعی است ۱۰۳ پهپاد تهاجمی یک‌طرفه، ۳۴ شناور سطحی و ۱۰ زیردریایی را منهدم کرده و ۲۳ موشک کروز ضدکشتی را رهگیری کرده است. همچنین بال هوایی ناو ۱٬۴۶۳ مهمات به کار برده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/151719" target="_blank">📅 10:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151718">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCkt5wxOON4uOchpDwPu-bx3g3XMRkElpdRpjVotOLVaoyV2rKi3zT26ggfq6eit4RQcyq8juOWRBqkK2PXWcgz_CoUOgenKABlLgUDQKv4kZSqQ9LdpIbDdbuIL0Cini-d49YAo0C8tEdNulDE-4RVPNSSUYG7sRDGpZJ6OZNRPqrnrVj7DYpCFgDxiOBHQcLujXxmyPxLFFqsXG0mdr5Ch7JaG9PNocPOc-uV8BFJqXq3AvdvlowwbrAtyrRu6S3t9HTsxqL5NqBzcRLeT2RoP3ndtAyRFMn8nKLdR0X22Pg-ozohnC739U0VmSVT0AHdlbib4_wF4br10fM2Cng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاتی عجیب از شب نشینی جانفداها
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/151718" target="_blank">📅 09:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151717">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7eb764da2.mp4?token=eG85ChDSvWv6PpmnZ1knnZCNfjW587bJOIsacGxUerHctk2u760ULQ42zvE190UqN32p7fSVf6D7kush9r8Mzd2qkR3BK8dmOUfKai0ZReE34vywECWrvMAynfE3-oHq9gRVrj16itwOE0WS6Z_1da6v1EYUbiU--TOo4__wiFTPaOXdI94GQgR7OWWlVd9brncMr7k13IIYFc-VrZxICrYbBv3kMYYI84bRisFLcnyxv4k_GxdZDgPNN2bm3ffGW1KP6ds3Ythul5OLLP9Ga4HHAKlh29xiHXkoy83NNTUiZfiP0vb-pgvd2mUpuXC6cV_XbqDdtiId1wJamqnQgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7eb764da2.mp4?token=eG85ChDSvWv6PpmnZ1knnZCNfjW587bJOIsacGxUerHctk2u760ULQ42zvE190UqN32p7fSVf6D7kush9r8Mzd2qkR3BK8dmOUfKai0ZReE34vywECWrvMAynfE3-oHq9gRVrj16itwOE0WS6Z_1da6v1EYUbiU--TOo4__wiFTPaOXdI94GQgR7OWWlVd9brncMr7k13IIYFc-VrZxICrYbBv3kMYYI84bRisFLcnyxv4k_GxdZDgPNN2bm3ffGW1KP6ds3Ythul5OLLP9Ga4HHAKlh29xiHXkoy83NNTUiZfiP0vb-pgvd2mUpuXC6cV_XbqDdtiId1wJamqnQgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور پزشکیان به عنوان «مهمان ویژه» در مراسم عکس یادگاری نشست سران کشورهای مشترک‌المنافع
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/151717" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151716">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزارت دفاع: حتی توی جنگ هم، ۱ روز تولید تسلیحات تعطیل نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151716" target="_blank">📅 09:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151715">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
فرانسه حفاظت از پایانه نفتی «ینبع» عربستان را بررسی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/151715" target="_blank">📅 09:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151714">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزارت بهداشت: هیچ مورد مثبت یا مشکوک طاعون در کشور گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/151714" target="_blank">📅 09:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151713">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb307e7cfd.mp4?token=NYlR1BhjsWLigifmPGRigJGu5Dp_R_8si5oDJWQsLrTSYCPyztxklafV9FQk0YM0D7t-grxPmFWkHZpGCHjxMNZfbpIic0eCOmBxCCugru3fNxwki5jux4e9QAWdm45YMKfCzj7rFgtpoPbcWqeOFQOxaJDaLn8L10_l3MVAg5UD0CmBGqV2Z-hKLxgBfnnnzapmhfxuoznPu2CONRl5ITgLHVscrIn5LrDK74Mp_dyi6cpZkdJkvRbV6CQ6NvkBqRErKrKHrL_dUSR9jIv512h43kdSaG6vey37dPnQKgOEMYhTe0IVOoaWve8r6uYowzIChA6TVWUb2Hd4Y2PL0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb307e7cfd.mp4?token=NYlR1BhjsWLigifmPGRigJGu5Dp_R_8si5oDJWQsLrTSYCPyztxklafV9FQk0YM0D7t-grxPmFWkHZpGCHjxMNZfbpIic0eCOmBxCCugru3fNxwki5jux4e9QAWdm45YMKfCzj7rFgtpoPbcWqeOFQOxaJDaLn8L10_l3MVAg5UD0CmBGqV2Z-hKLxgBfnnnzapmhfxuoznPu2CONRl5ITgLHVscrIn5LrDK74Mp_dyi6cpZkdJkvRbV6CQ6NvkBqRErKrKHrL_dUSR9jIv512h43kdSaG6vey37dPnQKgOEMYhTe0IVOoaWve8r6uYowzIChA6TVWUb2Hd4Y2PL0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایلان ماسک «توماس ادیسون عصر ما» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/151713" target="_blank">📅 09:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151711">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de895b67a0.mp4?token=j51Lyl6tjUUsbV1wMML0PsN_yFmEsv-sd7GK1a-OULFJ6ie0PONpvA01JtZxN_cIo9qOOLibDdecpobh94fVV9KApiDRGLIEGUJNuOOhUqZm3RZSLJe3xUDJJN_qA6L6UagFngbUGo0cY9VW1EdmIJRUna39lHdhv2HUOEO8b0JP6R1vI4ugkevokeG-aak2hbJQhvnUwWXqaS67SQE1e65RMF0_NkYXTA96_ulIQIQpjvOE5s7ZWIceSxe20majSE0t6Mt3Whk-HxsPA39B-u_VsVgM2-Nr04JotJckEU_esQdTFMMnnWS9GqFZsXMtfaGR7BeRoLNFEfGOzq10yQPpdaOmUJ_4a-jMUi__FJEVUAeMNH698mKGpUL4ceDuZdmX_zf_Qz2DAPiSpvYPg8HUhK38QmtHCkhcoqgNduglvT3h8oewXtfRHaKTxGFMmlEGiCpK0hGv_PzO3wjXsOuRda8AeiqrSZZZfuCE4o_U8LveHAvr6s_AiP-4esxvyayIcsJVVAcJeRRRagyYBI4YZ-GUfTbejsjO1NLrFn9qHEziSeJ91elhvyRp5_4Zx8RkxJHTmjrWBAQCUPkZ567ufOMI63to1kMTdjaL0lBEH-hPMj1g__7Pfv4b1RvTeAepBbzNPju8SYGtuBz-BtUuJTl5wtKNsCqbDSj-gYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de895b67a0.mp4?token=j51Lyl6tjUUsbV1wMML0PsN_yFmEsv-sd7GK1a-OULFJ6ie0PONpvA01JtZxN_cIo9qOOLibDdecpobh94fVV9KApiDRGLIEGUJNuOOhUqZm3RZSLJe3xUDJJN_qA6L6UagFngbUGo0cY9VW1EdmIJRUna39lHdhv2HUOEO8b0JP6R1vI4ugkevokeG-aak2hbJQhvnUwWXqaS67SQE1e65RMF0_NkYXTA96_ulIQIQpjvOE5s7ZWIceSxe20majSE0t6Mt3Whk-HxsPA39B-u_VsVgM2-Nr04JotJckEU_esQdTFMMnnWS9GqFZsXMtfaGR7BeRoLNFEfGOzq10yQPpdaOmUJ_4a-jMUi__FJEVUAeMNH698mKGpUL4ceDuZdmX_zf_Qz2DAPiSpvYPg8HUhK38QmtHCkhcoqgNduglvT3h8oewXtfRHaKTxGFMmlEGiCpK0hGv_PzO3wjXsOuRda8AeiqrSZZZfuCE4o_U8LveHAvr6s_AiP-4esxvyayIcsJVVAcJeRRRagyYBI4YZ-GUfTbejsjO1NLrFn9qHEziSeJ91elhvyRp5_4Zx8RkxJHTmjrWBAQCUPkZ567ufOMI63to1kMTdjaL0lBEH-hPMj1g__7Pfv4b1RvTeAepBbzNPju8SYGtuBz-BtUuJTl5wtKNsCqbDSj-gYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از تشدید اعتراضات دانش آموزی تو فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/151711" target="_blank">📅 09:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151710">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وال استریت ژورنال: پنتاگون در حال بررسی ارسال تجهیزات و مهمات پدافند هوایی اضافی به پایگاه‌های خود در منطقه است
🔴
همزمان یک گروه ضربت ناو هواپیمابر و یک واحد اعزامی آمریکایی در راه خاورمیانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/151710" target="_blank">📅 09:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M4Tg4hGxqJC4w_wA-tvB8jN0JoBpF49EYJyJGQE2_qWkR65KwLWA-6S7G7z5Xq_-EDwRMss-AiUbYZVKRmHHT5s9U1kgSiN96sVlp2JutDN961VLO_6vB8Kkogh-TmxpxYe5wuvFvgy0ToCWi0-2D3MMzg1MsB19rjODYkiUFQKGg8sZrd1kYbjLX7lNcWJaE27Rnc1i51AgUdLdm_98Rz8wY-2BlinFZALlZ6Ai9LnAbmTKrnDwtL29EH37QyX9vUJGrG9EFs2eIrnzi2uqiTRXlqiAG2MqEHZeggU8-9ekw36OUZfAOyqTnwerbXHtZ-91IJvveMJPNwxnv1PgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی کره جنوبی، دوربین‌های امنیتی بخش زایمان زنان تو مراکز درمانی توسط یه سری ادم مریض هک شده،و دارن فیلم زایمان هارو توی سایت های مستهجن میفروشن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/151709" target="_blank">📅 07:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151708">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RM8N9p5lIHQ94WKVH4NfoG4d1V9-54hOkCOy_-7qjM_MGvyb_zbnrFQ6uXfr_HqKyZkKiKkg1OqU7VqLbnFtZbOv_pa--GCcng7EhqiSgr3lHjCX7GqIRCgHhbReRJSPMs9APiCOIGE4hiXsR-EjdygLXFFxeCMSuZwBVl7UW3vuPsmV1YGqGU6fdP2hGcqMBw6F-MS3yGocLT5mMdc5avJvRFTtqDZxxSBcmN9Dk2iGhasL9ERle3vjdoj0o-RZ7gGl_VJ5A6MpWiPJ8UN2-FvnF_yZepd-jtIRtGzbTQiXu0Uh_kB9spwg23gURW6hYWgu3gsxJT0h5m8YkVYLzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیزنکوت: نتانیاهو برای عقب‌انداختن انتخابات به ایران می‌زند
🔴
گادی آیزنکوت، رقیب اصلی نتانیاهو، میگه نگرانه که نتانیاهو برای به تعویق انداختن انتخابات، ظرف دو هفته آینده یه حمله گسترده به ایران انجام بده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/151708" target="_blank">📅 07:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151707">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTURBO VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th9zySOR2ou6xMLKXagXlBvJ5zRb-L81x21mavhQY5QFeYYNIcP0jsd7rw02LIMZky4iELXY4atIQV5L9_icM4UGr0Z-ezkRRElRqbKoDO2x1pbh7g4-scWULBFsJ85OOJsBiZq1KRC3r7QYUwLQefG7Q28g2RGNsXnKFz22FGeZQjfubrMIOeBTZXmyKJt0UEqnOa3jJzTilg9TuD8ksga6j8_BRyaZpD_kcol6IQCGWNgEuq-Bxxi1zIvLowm1WB8DSZgFjncc2NSHqmBovx1pTZ1YZs-EsgEyXvai0QkVmSs3qVRgYYe601aEnZwVQnVoULgd5EmoaLH5-0_AvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
TURBO VPN
| اتصال بدون محدودیت حتی در شرایط جنگی
🐇
ورود به ربات و دریافت هدیه و تست
🛡
اتصال پایدار
حتی در
سخت‌ترین
شرایط اینترنت
🌍
بیش از
۳۰ لوکیشن
فعال و پرسرعت
🔄
آپدیت
مداوم سرورها و روش‌های اتصال
🤖
سازگار با تمامی
ابزارهای هوش مصنوعی
🎮
سرورهای مخصوص
گیمینگ
با
پینگ پایین
📈
مناسب
ترید، استریم
و استفاده روزمره
🔥
🔥
دسترسی رایگان به
فیلم‌نت و فیلیمو
🎧
یوتیوب
و
ساندکلاد
بدون تبلیغات
🎁
۳۰درصد تخفیف ویژه: ‌
TURBO
🛒
خرید از ربات:
@turbovpn_new_bot
👨🏻‍💻
پشتیبانی ۲۴ساعته:
@kasrazandi
.</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/151707" target="_blank">📅 01:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151706">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e2c521e1.mp4?token=BeQtkvWMGw9roSGsw2XEe3PVaTH3tZ49WokfCMGpN7dawDFL5bS6plSe2oxotQYbr_bwy6m7ZzXxfOj4hvHo83nGK4wVhDF4Flcmy7WZhMfPXxTqf6XKFR1KmMLT2JODR9j4nwNJRMRjrg4F7gLUBsyvQRTGfapgInIQ47AVtwubMI0qolGOuFM1kQRNO0qIJDvJ---5N_qTfCwspHjS_5f7gDu83HWJmyX1MdeB6KVonMdDo4IMQl2SEyQUn_lJxcZB03TFrz-D1swWfZATpaLIBHM6k6SIHThxw5bujnw-ZXeGH7t_eMPnRXHY3Hxng7Wvs7LRUZE7cQ1zSbaO1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e2c521e1.mp4?token=BeQtkvWMGw9roSGsw2XEe3PVaTH3tZ49WokfCMGpN7dawDFL5bS6plSe2oxotQYbr_bwy6m7ZzXxfOj4hvHo83nGK4wVhDF4Flcmy7WZhMfPXxTqf6XKFR1KmMLT2JODR9j4nwNJRMRjrg4F7gLUBsyvQRTGfapgInIQ47AVtwubMI0qolGOuFM1kQRNO0qIJDvJ---5N_qTfCwspHjS_5f7gDu83HWJmyX1MdeB6KVonMdDo4IMQl2SEyQUn_lJxcZB03TFrz-D1swWfZATpaLIBHM6k6SIHThxw5bujnw-ZXeGH7t_eMPnRXHY3Hxng7Wvs7LRUZE7cQ1zSbaO1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های مارکو روبیو، وزیر خارجه آمریکا، تو آتنِ یونان درباره امپراتوری هخامنشی و لشکرکشی خشایارشا به یونان:
🔴
480 سال قبل از میلاد مسیح، ارتش خشایارشا وارد آتن شد و معابد این شهر رو به آتیش کشید.
- تا اون موقع بیشتر مردم آتن با کشتی به یه جزیره نزدیک فرار کرده بودن، اما تعداد کمی حاضر نشدن خونه و شهرشون رو ترک کنن.
- اونا خودشون رو توی قلعه سنگی آکروپولیس محاصره کردن و تصمیم گرفتن تا آخرین لحظه مقاومت کنن.
- از بالای صخره‌ها سنگ‌های بزرگی روی سربازهای ایرانی می‌انداختن و تونستن برای چند روز جلوی
قدرتمندترین امپراتوری اون دوران
(هخامنشیان) رو بگیرن، اما در نهایت شکست خوردن.
- ایرانی‌ها معابد رو غارت کردن، پرستشگاه‌ها رو به آتیش کشیدن و آکروپولیس رو با خاک یکسان کردن.
- وقتی مردم آتن برگشتن، بقایای بناهای تخریب‌شده رو جمع کردن و توی همون تپه دفن کردن و چند دهه بعد، در دوران پریکلس، معبد پارتنون رو ساختن.
🔴
ما این روحیه فداکاری رو در مقاومت افسانه‌ای 300 سرباز اسپارتی می‌بینیم.
- اونا در برابر ارتش عظیم ایران محاصره شده بودن و تعداد نیروهای دشمن خیلی بیشتر از اونا بود.
- با اینکه هیچ امیدی به پیروزی نداشتن، حاضر نشدن خودشون رو نجات بدن.
- ترجیح دادن تا آخرین نفر بجنگن، اما موضع و وظیفه‌شون رو رها نکنن.
- این همون روحیه‌ایه که بعدها ارزش‌های اخلاقی تمدن غرب رو شکل داد.
🔴
اما این نگاه کاملاً با چیزی که امروز در بین متعصبانی مثل ملاهای تندروی ایران می‌بینیم، فرق داره.
- فرهنگ مرگ‌پرستیِ اونا، کودکانی رو که عملیات انتحاری انجام می‌دن، به‌عنوان قهرمان ملی معرفی می‌کنه و شهادت رو به‌خودی‌خود یه هدف می‌دونه.
- اما قهرمان‌های ما این‌طوری نیستن، قهرمان‌های ما ممکنه حاضر باشن برای آرمان‌هاشون جون بدن، ولی مرگ رو پرستش نمی‌کنن.
- اتفاقاً چون برای زندگی ارزش قائلیم، کسی رو قهرمان می‌دونیم که حاضر باشه جونش رو فدا کنه، اما به اصول و اعتقاداتش خیانت نکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/151706" target="_blank">📅 01:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151705">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vgdeMH2I4smvvo_wy2qmN-GrGoJ0g3TahJSxA7xFia94mmvovEXbZbNo2b17P10AJqGfXfYwkl9CdmplBzNsM4mHmYFvrbeMr_XFXCi1PkxfzuhJILLsKoye52G-NLnZUH1nt2RKR8amZrQ8krohFNFCMtpC-ahgQe8P_1VrnPYIMmxFeqyEc0yJxjesOindD8VzhHVj4wnOMr3jn3kP4QfnPBmpt1lACJarnB1WGJIdxa00wwg_WxQkcn8kG6PS7rUDKvN8dzQCc7JcJCe7HkfgLRp0JYhzFEKFaSv2cxJNySU2KnBYMLaqBJP-OrKb9yeN8cRHj_OvX31HBbDbbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو یکی از ادارات مملکت، کارمندای یه شرکت همگی دهنشون بوی بد می‌داده، اسهال، دل پیچه و خشکی دهان داشتن!
خلاصه میرن دکتر و آزمایش میدن معلوم میشه الکترولیت بدنشون بالاست!
در نهایت دوربین هارو چک میکنن و می‌بینن هر روز صبح آبدارچی شرکت میشاشیده توی سماور و چای می‌داده کارمندان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/151705" target="_blank">📅 01:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151704">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نیویورک‌تایمز: پنتاگون طرح‌هایی برای بمباران شدید سه‌روزه ایران آماده کرده است
‏
🔴
اهداف شامل زرادخانه‌های موشکی و پهپادی، تأسیسات انرژی و مقرهای سپاه پاسداران است. ترامپ در ماه‌های اخیر ۵ طرح بزرگ را رد کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/151704" target="_blank">📅 00:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151703">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGmkUk9ekub9l-HBvUeHKHuoyLP5Pn_sFi3Zyg_dj36SkYPhW3U1Pc29ok4P362yglYxLzaUA3cn_maBQDT1vItoOC1isNDJ6u--M2LzT-gUYqzPNY5I-Xyn-LFxC5w0W_iFMdAHg0e_75vNwyDu21F3B-_EjgVgB1nFeTxC8vSaWj8LUAgSiA2uHFV_1RFeoFpfXVYIlvSB2_GrDBaRf091yQ3A577tsLX0JTcMCDXg3_0bdzCz5y4Zptvtt-llU9tRxhNqsGcJepkO_xVvqMOGQCXNzYm4lDZ-X6sJAbQFdXIxPgkbJPRZ3y0_ULZGKSxQuLf37ld53LDbfaTmag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اورشلیم پست: ترور تنگسیری برای جلوگیری از فرماندهی او بر کل سپاه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/151703" target="_blank">📅 00:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151702">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB9gqa7RYuT286Z1jMDYLFWodP0uiUa5B9wvaBw6TN0DA3aV2SW5mHX5Pf4P9Zc_Rym85Ow-NcgBBdrt2z0nrTMdA8giJew6THZY02xzr1s-ng9VTuAp7zEa03d7focLRC1i2YbqY_-JMZZ9Nu2Mbp2xfUB5kwbasj0Oj96y-2ktG4Ihx06GcuihJn5C-TKnN6MK_ysBHwqX18nnGwczU5-sagocylpnPOGAMCdMwtlkthT8PgL4keB6Ii1_vImsguCY5lsTIWmacBQZkROoQTWFukTgQrX4RcN6gJslRTfRFCIBm-tiAhBSJOgWYG5HT6BzT-XjXagPnRqpknXF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس:
نگاهی به گذشته: در ژوئن ۲۰۲۵، پیش از عملیات «چکش نیمه‌شب»، کاخ سفید اعلام کرد که ترامپ «ظرف دو هفته» تصمیم خواهد گرفت که آیا آمریکا به جنگ اسرائیل علیه ایران می‌پیوندد یا نه.
🔴
اما زمانی که این اظهارات مطرح شد، ترامپ از قبل تصمیم گرفته بود به تأسیسات هسته‌ای ایران حمله کند.
🔴
در ۲۷ فوریه، کمتر از ۲۴ ساعت پیش از آغاز حملات آمریکا و اسرائیل علیه ایران، ترامپ ادعا کرد که هنوز درباره ورود به جنگ تصمیمی نگرفته است.
🔴
اما در واقع، او پیش‌تر تصمیم خود را گرفته و مجوز حملات را صادر کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/151702" target="_blank">📅 00:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151701">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=mFT2DVXhWyGAp1HdoH03PbBJ0CrU4eNGbw30UbGtY2OTSz_GGyEHUzYlgjqf3V4Zv8PaJn-XkUUmLUy3ZbIa4qxa03Lwa5wLWtMjSpiSbBHYNkpw5ZJVmTlL2O3P9Jyho245vGWh9QrZ20POjywwWE7jLbJaIor2OF9HnuaJJapDIhIFeVyApdcwBEqG4xXmpHi28cRIAPROCpZmtE4gvW-GO-Uoj6-YECSEM0Xm-xnveEil8n778X9FyN-bUvbv1WYjt-v5W0HVYAsl9syT3L1eO0mJeycL-YdzxfWtAJEl74Ccs2VfhAsrfmODbxBkSZ-ZVTju9psq9wpoG4KMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=mFT2DVXhWyGAp1HdoH03PbBJ0CrU4eNGbw30UbGtY2OTSz_GGyEHUzYlgjqf3V4Zv8PaJn-XkUUmLUy3ZbIa4qxa03Lwa5wLWtMjSpiSbBHYNkpw5ZJVmTlL2O3P9Jyho245vGWh9QrZ20POjywwWE7jLbJaIor2OF9HnuaJJapDIhIFeVyApdcwBEqG4xXmpHi28cRIAPROCpZmtE4gvW-GO-Uoj6-YECSEM0Xm-xnveEil8n778X9FyN-bUvbv1WYjt-v5W0HVYAsl9syT3L1eO0mJeycL-YdzxfWtAJEl74Ccs2VfhAsrfmODbxBkSZ-ZVTju9psq9wpoG4KMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
باهنر
:
ایرانی که صداوسیما نشان می‌دهد کجاست که ما به آن پناهنده شویم؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/151701" target="_blank">📅 00:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151700">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏
👈
جرد سزوبا، خبرنگار المانیتور: سناتور کریس مورفی می‌گوید پس از آنکه به‌طور جداگانه با امیر قطر و میانجی ارشد دیدار کرد، توافق با ایران برای پایان دادن به جنگ «به نظر نمی‌رسد در آینده نزدیک محقق شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/151700" target="_blank">📅 23:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151699">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ارسال تجهیزات نظامی فرانسه به عربستان سعودی
🔴
وزارت خارجه فرانسه: هدف ما از ارسال تجهیزات نظامی به عربستان سعودی دفاع از زیرساخت هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/151699" target="_blank">📅 23:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ead6bb1f.mp4?token=PysDjjU5Zi7i6wVjtdtW0rb9H9xR1uS5nzq6mugJn2a9VrzMr27ruN7DBjy1SBBNS-H7gVn56LCylzFUvJK6OJtKI2NNS058R_HL6K5nMjcSr9OovxtX_WnY8ceL-bghNrgu6F6gUQZ778CxMxsAG15MAjRgR-8vOxMVhkCp20MmK92mqOxq4uERxduxGobwTFCZXTiQy9QFOX4cVZdPOtGKPAixkJTqL5lAOO3LNmYQaee7eOlLFlS5TyJ1KBY6RSorY2gbIQip_lpg1y9bRY-HVqiFN_V4gZZx5JP8KlQm5dKbO30hn9RqexL77t-FXbfLwgw1lMAkGfRRdFLV7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ead6bb1f.mp4?token=PysDjjU5Zi7i6wVjtdtW0rb9H9xR1uS5nzq6mugJn2a9VrzMr27ruN7DBjy1SBBNS-H7gVn56LCylzFUvJK6OJtKI2NNS058R_HL6K5nMjcSr9OovxtX_WnY8ceL-bghNrgu6F6gUQZ778CxMxsAG15MAjRgR-8vOxMVhkCp20MmK92mqOxq4uERxduxGobwTFCZXTiQy9QFOX4cVZdPOtGKPAixkJTqL5lAOO3LNmYQaee7eOlLFlS5TyJ1KBY6RSorY2gbIQip_lpg1y9bRY-HVqiFN_V4gZZx5JP8KlQm5dKbO30hn9RqexL77t-FXbfLwgw1lMAkGfRRdFLV7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه به اربیل کردستان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/151697" target="_blank">📅 23:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
هگست، وزیر جنگ آمریکا: ایران بین دو راه انتخاب داره؛ یا با مذاکره و به‌صورت دوستانه این موضوع رو بپذیره، یا آمریکا از راه دیگری وارد عمل بشه. وقتی زمانش برسه، مشخص می‌شه کدوم مسیر انتخاب می‌شه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/151696" target="_blank">📅 23:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پارلمان اروپا ایران رو محکوم کرد
🔴
پارلمان اروپا قطعنامه‌ای تصویب کرده که توش ایران به نقض حقوق بشر و خشونت علیه غیرنظامیان محکوم شده. جزئیات بیشتری از این قطعنامه هنوز منتشر نشده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/151695" target="_blank">📅 22:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
تو اعتراضات فرانسه هم شیشه میشکونن اما در کنال تعجب هنوز کسی کشته شنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/151694" target="_blank">📅 22:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn9MLNO-Y-TJVx51Nekx8HcKCrXOsZ9SQwheOb1NL6U4NvWbvlxIsPMn2bs5OGxN_Oy2Qd2TASojCsWBJL5bZg8Gc4lv3DHPDZ7FW_WXRJtp63CnShkpqC1RptNMdD-lIofTItFE58Q6CVWaQ423GxuL_0QKxgapdzy4zzihlbryCOfXUjRRXpgCm4fpGgQsxNlix3h5IGpdsjZ1eQQv9y8pS22B6vVBGU2feNZ2Ska7gLPPzOCOjahn3pWYBp7_pxekPka8JNz_RbcvJIm7uk-mxSfQBTI29NcBToaVApoFqjEBZI43AQuHmYFtdkSoUs8LP91LFOORa5cmYc3N5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال:
رسانه‌های دروغین و ساختگی در تلاش هستند تا وانمود کنند که من از دشمن می‌خواهم شهرهای سن دیگو و لس‌آنجلس را بمباران کند. در حالی که در واقع، من در مورد این صحبت می‌کردم که افزایش موقت قیمت بنزین، هزینه‌ای ناچیز است در ازای اینکه ایران سلاح هسته‌ای نداشته باشد. و اگر بخواهید بدانید هزینه واقعی چیست، تصور کنید اگر آنها سن دیگو و/یا لس‌آنجلس را بمباران کنند چه اتفاقی خواهد افتاد؟
من فقط در حال مقایسه بوده‌ام: پرداخت کمی بیشتر، برای مدت کوتاهی، برای بنزین، در مقابل بمباران شهرهای بزرگ ما.
همه این را می‌دانستند، رسانه‌های دروغین هم این را می‌دانستند، اما آنها همچنان ادعا می‌کنند که من از دشمن می‌خواهم دو شهری را که دوست دارم، بمباران کند.
منظور من کاملاً واضح است، اما این افراد، افراد فاسدی هستند و فکر می‌کنند می‌توانند به طور مداوم با انتشار اخبار دروغین، از این کار فرار کنند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/151693" target="_blank">📅 22:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
ان بی سی: ترامپ قصد حمله داره و اینکه گفته تا قبل انتخابات حمله نمیکنیم دروغه
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/151692" target="_blank">📅 22:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151691">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c550ea18ef.mp4?token=Xp-8NXFFXLwxL0ZTSJDJs8_t2p9IKbP1y3f2mQPhsROYhKJCGlKM7JGFNxHoL9krGAUMHUU-yJG9Zbe2SgG6P-xyxd-V7xPwnlUHDycsJmp4Q0HXnUmUePTirAsU8um7ZFrMd53JI_PLwPxe-Wz3aBITDfI00o9jnvWCsykfhTSfrkzLpCqoXcv5SW-3m1yz0Vko4SfkSmBu94YYCt1eVpB0WYihOB5OYKF9hQjWy0N8oJkJxvCTr0mgx3uR66JMP9eT8jKDmz-1EMKiNJSM4DXmzCTj1Sug6MFew8KEXeHcZtaDuIY0i60e8fu9Z5g6zbkKV0asBWX77uwpEQB17DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c550ea18ef.mp4?token=Xp-8NXFFXLwxL0ZTSJDJs8_t2p9IKbP1y3f2mQPhsROYhKJCGlKM7JGFNxHoL9krGAUMHUU-yJG9Zbe2SgG6P-xyxd-V7xPwnlUHDycsJmp4Q0HXnUmUePTirAsU8um7ZFrMd53JI_PLwPxe-Wz3aBITDfI00o9jnvWCsykfhTSfrkzLpCqoXcv5SW-3m1yz0Vko4SfkSmBu94YYCt1eVpB0WYihOB5OYKF9hQjWy0N8oJkJxvCTr0mgx3uR66JMP9eT8jKDmz-1EMKiNJSM4DXmzCTj1Sug6MFew8KEXeHcZtaDuIY0i60e8fu9Z5g6zbkKV0asBWX77uwpEQB17DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست درباره ایران: ما قصد نداریم در ایران، یک کشور جدید بسازیم. ما قصد نداریم تعداد زیادی سرباز را به آنجا بفرستیم و بر مناطق آن کنترل داشته باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/151691" target="_blank">📅 22:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151690">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ به ایلان ماسک: ایلان، تو دوست من و یک فرد بسیار، بسیار خاص هستی
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/151690" target="_blank">📅 21:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151689">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9PrSm9MJnKuLPpRhOHAXkdU7K3b1TL2lhJJchD6SoDpmevXQH7s2KXzzYLm3sA4uT0hhTNrhAR7pUjoXnfviZJ__ugEKQJ7aI8-CM-u9e232VxWgNv_kEz1PeErpYqX2aRsNYdsRvXHgmxts4fAb0wa8p553T-M_sc2KyFVw7AA2lcYNtcbLy1MiUYFJ7yj_8XJGHOyspVMUkEWloD-zQ75Uqj59Os1ly-Iz1onmsLBhie-qY1DhtNl4uOJT0-sNLCCzjMDlpvSe9V_CMmJQRRM3ZEKn3NvllrFR4ZWAHNXT09YPXlUZZXc0Y_17nD96FV7uFLPL9BcmRiCYKQcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان و پوتین باهم دیدار کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/151689" target="_blank">📅 21:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151688">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
کانال ۱۴عبری: اسرائیل در حالت آماده‌باش کامل قرار دارد، و خود را برای بازگشت به درگیری با ایران در آینده نزدیک آماده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/151688" target="_blank">📅 21:40 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
