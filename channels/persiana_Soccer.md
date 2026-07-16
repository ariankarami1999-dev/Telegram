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
<img src="https://cdn4.telesco.pe/file/t__wUD5960hfXh1yJzC1VboECe33bVVc130ScU6CzuLMnVPSJ1z8_IElWBps-Ya-jwkz3N-gF55iFyySrQSHJFl4XnWK8TUP-4TV9B1FXWUozqNLN0UW1BiXlXh5PvDY5i5FzPrCUgGUkInFiGcjmwSpJAMMfu5mkyOl3ixhfmbnYSOQxh77fdbFeexTdvgRUGl-n94PUl_BwykOCNRB1jqTfl7Po8aY7OU6oXwjej0mMqQdliB4KoojOuPbKyuq9gSEQM0kJd76mINUPOWVbehrU3VzpVl3nqFsi43_t1IPketbQsb3eea_J0a-UjZT_avp9lx1MddaDI4GNRWb-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 504K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 15:44:21</div>
<hr>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7_t8YG7nHgkimNhHNwdHjUWZrUDdsnIZ6W_-jCeJaktN8N5Hbu1wIvnyNyizEtzMEGsrBo2B1TJ6Kd75hMO6954Nuf9PoubPyYRKxl-oQwr_A72TKCbstsrPdqV3JHhAufSItx50GnrIfFo3ezeXsQn2wih8W3qqfJ27MCFB98engGR-mTL0GZGAZFEj6NJ69cNMCMyzhAwSRioHwpNyR6H-Pdkn3ncU6Yqni7kOVSh481lNFv39UleeM60APx3RbwWpUWOY6zZaYQTH85KkfM_HG1ZDO-EV9O5cKpzAYbmyG0MgeOlxHwbzeKGs1oKKgNbjwRQt8jSt7Kv5b0vgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTxws3QLMQeKMoY2cEldVLlBmTsFiX4przQjcoqTNEQKzYTMk6xguR0GnscwpmtFt5RmBOaFLm5cjqv0DTxqD3dbV_sKX9d9n_g5nss2fyR0mc7soG8dkjMoDIxrcJSt0ucx2seDnpKI-mFX5r8XC-3yoaM4gXLGgBP4QdZ0uxTPrKh-VgdOHVBufklxxfdRxoynrXk1IVS3UwxQc7WZHDuk4SOz9ivBhNNOuuqXg830l-4gNFx3NN5fX_pvtSfCPlSwZHF5jYZmaWu2F6kiwKa2KOFydZzHhNQ2zcyjcPkNdJgzZqrfxCQW9ijpdCUl80PYlOZkO0hojePB-UEZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYtM0AjHfsqWlE7e1a8x1HWbFWbEcoZDqwgoBKvlFr7iqUjJq0r3iIeA0nPV3gJYeJWobw7lg31yNTZscy9qQ46pslm-dWs0ay7kYZlGldgpv2bwVOaYyqnGF6pNNo7c6Co1IbwbfTZsXvp-ygCuVp5pelOicd8mJNUwRGkuPwEOqOAOHpHQdfqOkWRrDjyqq3VuBGEilI72sgHVzeAq1ew_48KlV1ixWs15nZr4k1LA81WeJ7Bkj11w9PQ_RqNQaBcBgjVXK58bLBUaeCZWc5GhvqZ_h866bZ63_U1dW4G3LLPIMc56G9BShm2I0gfR2JdVI2hy663ey9FTE4xoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLyYY9jpUt0IG1JhSmEO8iNm1ZytGtG7afvI8xFj2VlR9FMlGO9D3YOqrVgChsJX1XpO6yVyzY8F9oL4v9lqIutpwH89ENz-3zIcXiWy81FxzW-uFhoHlaD2B9VbyjvFjhhrzm09yOxfirNoyXS1DDMk-mGyYZ9MiJhtbulo2IJBPmVWhIXnpKt9xw9UwZUYs-USDVJxFmNuGUzxxomPt26DnMxGURSooZd3K5sAY2gQIEE6cgFQK3n7AVK3PH4DHTnIRLxX_qM51hyPEWb3MLYfGrielnfi7WtaFdIUILhjKKWit5LxJRO4ET2MsnCT-1o-T5PtBja897hript70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25849">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txz9Ynn8NcXlKa21Et12mBb70pAMD2DR4xRDt4azFLAecI282_K2Wj5KaS-FxbhJMdIB7aQ43-NeRrL3pCLXYn9Hi4G5nq9SMzC7FNP-D3uRzsyLTAj8xwdiSaqOPxSssu1kkS_PE7TdNA875x8OcTirHo9OmcpvujA9neQ8yfm-BtpGFUBSA97yiH1Y5TvFvzxhmGxbQfflu7hrzF3ZvFlWv11hlFWMRsXAAz101MvfvycuMiZdXx337n4OwqmoNSbF5x2wH8FLCgmX9M55qqf_ETvxFCfm13LTNMbeqU32vPk4r6nNtoWQqrita4qvDXhGVAElM8Xf9-0edjS58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/25849" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25848">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfKXy7vXCCDd20FIc-ay6vDfgNY1EpC2OYjHcgKDLgpuO1XqMvKOzU-mcq3QCaNEzD-nWPZI3zAJMfURXfcCsn8LBGv5A76b4diPHk-PTVuKLWmbFgWqpnJ5KBeVFXtXcXKcmI7OPKCAN8k5zPqfjKnd3vA0nbqIJBbFIi-3Ywev2HgS7W1OqdE-YvJTyiQc7jGaIA-55FAENkq0eQ4Cw-4ScWAQdeRKc9PMU8frtGzoUKAmALFECnG1SToz0OAYWXk0qaUtDFnBu2Az_GNEsimoRevI_ng9TM6_7es4sC8oHLXhx4RePGikTysj_xjOCWqtcxNavbSShKnLRztJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس امروز عصر جلسه‌ای‌سه‌ساعت بصورت ویدیو کال با مهدی زارع داشته و بالاخره او رو مجاب کرده که به آفر باشگاه پرسپولیس پاسخ‌مثبت بدهد. مهدی زارع به‌تارتار اعلام‌کرده رضایت‌نامه‌ام رو بگیرید می‌آیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/25848" target="_blank">📅 13:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25847">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY5bEj-6XX9dSyhVPdDoHkFb020y9SJtR8uX4ZzgCYIS8_LP8VrIL339aMRDeEREEoRqHnwR3E1NyvFxRZDFmHv31tEVxT3wE1XP_LUEwYDAqs1jV5XugAxzwUBRMW-iwh8TRGoTNUxQ2mwG-IPVTnA3PF6vLp9htxFzu9-WBNNCTTW7PIxs4Q4coCCtQHVrqeALmMnUPNDQsury1h0GC8VQalavyrTLEMGaz-EhV3zeuLuIsxGdTfXOXaqBKRcPS88dkT2uMoeAHbvm5V1BEmRZsp2axOlDRQv4ou3VSSTP3aoW_D9cctFxGKd-BMv5fZAu2pWH-K7haC-WO7QJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/25847" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25846">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uhm584W51J6op5PhOet63zlB3P8WagwQqTZ1wyEDrxHuxdDoa6q2rZpzT4-t_-HSzd0YSU717EBDzBbvbPheHKB5qCgH4a9iS23TfxccZ2AuW8ydNHIxnlp5Vk24Ycquo-THL2KjmcaQq590Zae4cntJ5BcDertPE6mEtC6KyanBnHb83zJ32cRcD2XtWujPMOzp6cu-PiFEwONM6nTwRSTP5E5YCNLXaHHD4W7Ii30a_eueMpwugW1ah6FmUuoSw5OF5wnAQn3XCaTMXABEdyhlndVYZLnKppym1xDLDwBuR2_pN9YcNmWwIgKQWwHBzP15lGl_2dfPCOsg6pqj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‏دلیل موفقیت‌اسپانیا مشخص شد! نهار قبل از هر بازی آنها را یک سرآشپز ایرانی برای بازیکنان تیم ملی اسپانیا کباب کوبیده، جوجه و چنجه درست میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/25846" target="_blank">📅 13:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25845">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇸
تصور کنید توی اوج هیجان و استرس فینال جام‌جهانی‌بین‌ تیم‌های آرژانتین و اسپانیا؛ نتیجه بازی دو-دو مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه؛
همون لحظه بیژن مرتضوی وسط زمین:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/25845" target="_blank">📅 13:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25844">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9hT6NWKkTiruRxQv-aUHKSCjcWMD7UdcDXdlIi2IQFSckuMJf9qyZQjHn4jjM8LTHnTap9MFqKyxwxBQK9YgeCOuZA-RR9JZDFLuje3eU0typ3crgu_WqbQYyV8wiGm7OHy1iFFubth5KtS6PU4IfUqtRKAbh2HEhyddoWaEaeub6hGtzuTndO8YZyDR3UvuR-UsjvwgwOgN1B3MFH20S5FYL0TvCRxg-xDAZgriMjf1n81fHxDzVfcfT1WtLtYjEOfvL4T94nUOaFYsLuPpuoRJfS5XnuoLwnowWnUNL3Hxey7oED6x_2dKrD6VwhNcy9ATEz2LrYtpLONB7N2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25844" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25843">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=Fu8ABEpNHu_q8zLNrv7hHyOK0fPcVCtSH-r1y4NwEo7BsBunyIqx2fkM1c9vrhzlTlLi9lqQ1Tlf_QT5R5Io3SVmOcPSAtEPkw1K7VEun4oTVWXTwwR7xTNSgvCmvpDl8gvsPKq3TcKPIzkKLWkNL-JTgnmLCizRRW9TJv3Dy0pTv_uBBODdE8ucEwzc10c-A0mRwWx73I7KXkk_cMS-6ByGr0jSn5BllNO6RdvDF5IXcmH0uqKWsfbY4erUw2V0M4ssNPboqQpQFfx7WMeAh0FBFtrmN5sbtuko7hrhs_NB1qXUD4kDe2lhtIIsjI1zl1islcao1ptnb4OnDmRB-V_EkWnEzaemhU1FRNdq-w5ZSQ3PN94aqqEW0s_rv9BJJcLJ3GCYIYuMR_aDNQL8Ovbzskv3x3ejR7u8PizT2atr7pcnepvLylLHpzPepQR6XywPZIjpT1FvaELRS7epbmGWd9PmCA1bHuTIo7rPMZ5H9K_kBgKqdB_C9RsNtzoFb3bLzcd4_TkcE94SbGlWiN-lwbvc0tgUNsD5BZ_Aoczxsy9x9-eqRkZb28BFxGJv7CzU7StlgDqI3AlGgDre3ddsY0fFNuCCg1isnzfgVjsxNLwCi4NVtsBeJkAm2NVjHaGkLY_zPJpvFYxUx7idoMKeSGrfXRTRuuJtqhSoVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=Fu8ABEpNHu_q8zLNrv7hHyOK0fPcVCtSH-r1y4NwEo7BsBunyIqx2fkM1c9vrhzlTlLi9lqQ1Tlf_QT5R5Io3SVmOcPSAtEPkw1K7VEun4oTVWXTwwR7xTNSgvCmvpDl8gvsPKq3TcKPIzkKLWkNL-JTgnmLCizRRW9TJv3Dy0pTv_uBBODdE8ucEwzc10c-A0mRwWx73I7KXkk_cMS-6ByGr0jSn5BllNO6RdvDF5IXcmH0uqKWsfbY4erUw2V0M4ssNPboqQpQFfx7WMeAh0FBFtrmN5sbtuko7hrhs_NB1qXUD4kDe2lhtIIsjI1zl1islcao1ptnb4OnDmRB-V_EkWnEzaemhU1FRNdq-w5ZSQ3PN94aqqEW0s_rv9BJJcLJ3GCYIYuMR_aDNQL8Ovbzskv3x3ejR7u8PizT2atr7pcnepvLylLHpzPepQR6XywPZIjpT1FvaELRS7epbmGWd9PmCA1bHuTIo7rPMZ5H9K_kBgKqdB_C9RsNtzoFb3bLzcd4_TkcE94SbGlWiN-lwbvc0tgUNsD5BZ_Aoczxsy9x9-eqRkZb28BFxGJv7CzU7StlgDqI3AlGgDre3ddsY0fFNuCCg1isnzfgVjsxNLwCi4NVtsBeJkAm2NVjHaGkLY_zPJpvFYxUx7idoMKeSGrfXRTRuuJtqhSoVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#تکمیلی؛ بازیکنان آرژانتین بعداز بازی بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ ای که روش نوشته شده هر بازیکن حریف پنالتی‌ به کدوم سمت میزنه.
‼️
خنده‌های‌انزو که‌مقابل اسمش‌نوشته شده بود که “وسط بایست”یعنی پنالتی‌رو به‌وسط دروازه می‌زنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25843" target="_blank">📅 12:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25842">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3ZkAtoveEhhRVQV5kd06YMu8FcrHimQzz1lboRO6ksc-e1A3qBBkmi1d2N_ITaBwLgeEovP9f1AIiXYMukdVsT29FrZWtcbcqM49k__lRPN3BJv-ZhGULF2G_AkqmPVuduXY3qFtf55DnrqmU9ZhXt6gNWiO4py4P9MHPI-Qn6xgqXnlpyWjU-GM7CJ9rn5Ev85VcwejkOR-inJ9LIo5yNR0zlSAQbSwaI-r__Qy3x-1tdQrXTMdiV6R_39d_pxcgU7P07bvTI_ri12Rj0q_ucVVKhhWhORvB7PK_b9pZJ6wIVDlY49GzbOa6abeFPIIo3VjvyRpptrMM7jaIwr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/25842" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25841">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZjT1p6dZVHhKgCdYBLiC8VU_40q2Wg7ihPwT_cuiLU5LQ6b1mq8zfeqkL6oKr80IjyhhF0wQSSo8TCvQcL9CCbP_1Vte8KjYMnqzWy5Eq5hsNik9tYtoAV-S9hy1IoDw9kztAusjiIpK9VsGfoTjLiZ-uVRZ4a4l5Z9TN_fOrVf_XaAc2WWy9FaFZeHsUK6la-ZDXudgue4iLVgJZM-6-K2tvQlZRsWWnKa12_5OsaYLwEkekd4n2lPv9Mr1hfE4XpqcLGom1FiO6PzeRlyNbdMCRcjyITfxUIZT5wY4C7PIrhortk-gJ-ncyAgWemSnKWbm0kmwRCZ6RjN_6-0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25841" target="_blank">📅 12:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25840">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSXzOGkKsDDbL9EOxh6QdHi1tk1w3fBYbhVk0-SyiBY50x-fgcmXMACaIdDy0YS5s8642-p6Z-KG4rTByOkoqXm20N-rfOXwt81Y9YcUbfqJk49ChHGPNd6AOy0DMamzmd2IDvianSpPVf2jpqxeI-Q7vAkYxnlJk4n6fWK975VoN9GdJZ3n14sX0NGEcLAHNAzqVaZgLqOH8MsoaTlbQI8E2WafU5FhWExVfhNZTLyBHX5z2I8L5s4CNhIvyI_2EYwDqJErsa_2cYy7-FoNUr14PRjc7TIIKbk_HBR3VGxG_-xIGjkcl7uU-I0UTArGHYWmqOyU10pHTIdnBAzdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/25840" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25839">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8168388efd.mp4?token=Ccttcyd9l9ht73YY8SZIkO65qEYpK5K7ExY_2RoDkL2aUQMuYI8PVtRNH7mESjp4-j5YsvqdQz3cM3Uuze2_jgDAw89uS8PcPODC1jr9O13zCfYcQ8U4kLtyAuoONFzqLoVT4_dlqznaoYPjdXXntBo0qjbVXL8UPJhEIfWLpIRLNWWhh6VyWAUuiVM1zo6ZNCOuLGa9E1EOTqEfQPcfHlyX78VgGwRJghJ-j38_59oU6iJ_uqEuB2bUH3hFuSZNPn8O0RvxpQBeiSTpHcD3_t6im4nUKd8dST6ke_ZVv4-NHgouRZkLwdDuz4d5pPEFfewz1JvY_1N_YoX-UEmUtIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8168388efd.mp4?token=Ccttcyd9l9ht73YY8SZIkO65qEYpK5K7ExY_2RoDkL2aUQMuYI8PVtRNH7mESjp4-j5YsvqdQz3cM3Uuze2_jgDAw89uS8PcPODC1jr9O13zCfYcQ8U4kLtyAuoONFzqLoVT4_dlqznaoYPjdXXntBo0qjbVXL8UPJhEIfWLpIRLNWWhh6VyWAUuiVM1zo6ZNCOuLGa9E1EOTqEfQPcfHlyX78VgGwRJghJ-j38_59oU6iJ_uqEuB2bUH3hFuSZNPn8O0RvxpQBeiSTpHcD3_t6im4nUKd8dST6ke_ZVv4-NHgouRZkLwdDuz4d5pPEFfewz1JvY_1N_YoX-UEmUtIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شش پاس گل تاریخی و حساس لیونل مسی در شش جام جهانی که در ان حضور داشته رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/25839" target="_blank">📅 11:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25838">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXkBEItC53yDj4HVMH_nKCZrGNNH68knPnfAr22eI1F8XMutcGi9apiHGpXExsEW49arPdfm8LmuXwi4GNjip8V4dGm-5sa7cqfcn5PA1oS5ofPe_PE2Wn5YAiR4Ub2anG4pnqiVz6zc3acMRgErce96PeYeFCmSYXEKFK3K-L5krozDlPN25wDYTCUoTtP-hn83n76jJXyw9FQmFtK_8TxOh-s9acFeAdXSvYNXKXdSMDdq37edPtnar4HdUaN5QqaPnqjtlpUpltmvtTCSKBnvb1tQPIL_UEr_KQTvAAQwDmJrlNPJzCU_cIDc1YpX0gsqvClFK0CY0Txh3vld9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25838" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25837">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇦🇷
شادی‌کارمندان‌خبرگزاری آرژانتینی در طول بازی با انگلیس؛ دولت آرژانتین گفته اگه قهرمان بشیم یک هفته تعطیلی رسمی در کشور اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/25837" target="_blank">📅 10:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25836">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=QnR6WA1tWVyluF4H7nYyRFzy3VMWb8-kBi-RCkbkpwzkp3mmFBjMCxM3-hYbf1TGhDwUp1Hx26a4NTV8GkxUGrcK-_Ld9oJsPN4jV5MUcATetTPd3mvzYI79GeqUz9ubVnOgXnmO289scwa87GqsSUWw-ORbqRAjf3Lg3kPRlMgPPsQYPY3xqcfPnVJDbR-OC7plvqMOD-1_JYXgVX9HBW6v7ponNIjD3db5wCSrXVCPFaoAadGDqyyL1lIEKXW7WP8vBmksngscrm37GlshiQYS0FODwnrNiswm3546r7mx4uJQvqqEWMQByU92trsYmAM5WqsJliy5K4uIn4ID3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=QnR6WA1tWVyluF4H7nYyRFzy3VMWb8-kBi-RCkbkpwzkp3mmFBjMCxM3-hYbf1TGhDwUp1Hx26a4NTV8GkxUGrcK-_Ld9oJsPN4jV5MUcATetTPd3mvzYI79GeqUz9ubVnOgXnmO289scwa87GqsSUWw-ORbqRAjf3Lg3kPRlMgPPsQYPY3xqcfPnVJDbR-OC7plvqMOD-1_JYXgVX9HBW6v7ponNIjD3db5wCSrXVCPFaoAadGDqyyL1lIEKXW7WP8vBmksngscrm37GlshiQYS0FODwnrNiswm3546r7mx4uJQvqqEWMQByU92trsYmAM5WqsJliy5K4uIn4ID3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌توویژه‌برنامه دیشب جام جهانی پدر تشریفات‌ایران رواورده میگه تو دیت اول چیکار کنیم طرف خوشش بیاد و مخش طرف رو بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25836" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25835">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whq92oQLf3fetoHvJvLJ0iGvlTr7GU3HpxcZ-igdHtACyk5T2niTkSAMMfAaiWT7wxZ97f1xsR_7ezrrg9tYV4EHnNQVQnQp8-JQcNUVWTCQizgr1UQqKb3XsXeIEQ1HHC2g8r1Idp5V7TdT1BvqUhrvkxYig-_SWmJRXCLQnDYcyh6MFih85Nih4WYzSaHdgjeRfeI54g2gih_bhLjiK1_bh7-GNhvZUtvlPll-WL5jbsAYMiMQBUV4fVVlnDvartFEdZKvb6eAYTF_Q25jV8h7Pkv1r4wmnR4M1kXpnDDgCzrBo6ZK8uKX5MWpTem8UWaAq6G3zmbnr0NoGe0D8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درآمد تیم‌های ایرانی از جام جهانی
2026
🔵
استقلال: ۱.۱۶ میلیون دلار
🔴
پرسپولیس: ۱.۰۶ میلیون دلار
🔴
تراکتور تبریز: ۸۸۰ هزار دلار
🟡
سپاهان اصفهان: ۵۲۵ هزار دلار
🟠
فولاد خوزستان: ۱۷۵ هزار دلار
🟢
ذوب‌آهن اصفهان: ۱۷۵ هزار دلار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25835" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25834">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=Pk8do904CYTsg3CFn1022rN2vkuFu_m7axQmmWbp4Y5Zu_Bso2eXl_KpcKFX9Ro25sZhbSf7hUSm34reewkCjzAOYA53ByYOEfQpGsCpia9ko8C3tMOgY-Uf6EPt4edtzWowUvU2niGXJjLpSb-c6yWKrary5I2tdb9d0VbA4letrGkWWJnS3qe6PczLtwoI9qfCnii3EQ3qI-zqMiHcXgeRq2nTr9aHiyBrQ3yuk2UWcjKMtp4rAQ38-2NH2yIWFt1ocTl90yV1xuS7m8hf2jXJhmOCVtewfPMj1nFWlgokoXetFwxcaRBZ3SOPMvoS02DcP9wRBBgmoL0XYkYqdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=Pk8do904CYTsg3CFn1022rN2vkuFu_m7axQmmWbp4Y5Zu_Bso2eXl_KpcKFX9Ro25sZhbSf7hUSm34reewkCjzAOYA53ByYOEfQpGsCpia9ko8C3tMOgY-Uf6EPt4edtzWowUvU2niGXJjLpSb-c6yWKrary5I2tdb9d0VbA4letrGkWWJnS3qe6PczLtwoI9qfCnii3EQ3qI-zqMiHcXgeRq2nTr9aHiyBrQ3yuk2UWcjKMtp4rAQ38-2NH2yIWFt1ocTl90yV1xuS7m8hf2jXJhmOCVtewfPMj1nFWlgokoXetFwxcaRBZ3SOPMvoS02DcP9wRBBgmoL0XYkYqdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/25834" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25833">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=pNJ0phUxWpi2qbpX5G3idGGpK9d_hrw6X9T5ftEfBxPacjZFYnaA26dqtGKGWIi89CfNV3Sj2OA8dFRzbRGzrXPzRyjB5DVRmzpDu1HobfdPBAAZi2f9Itt1GiAe6OemZNLaEKihWebo1aqIlaFU1-aBd19J0VRKUieq78cMnGi2T6ud2PEushCyVN7YFZufbI9qwVxperIHlYaKVm9KjZQVEtgoh-_DC5PP78psvktD72dbzGAOkoy_nKuIg8wKulqY1pZNv7XrsgWM2IpHd0uEZp1WeikS8LRje9pE9YaELx_nOwWRHNDubDfHC8umAsm3PP7dPPy4iEfLenqI5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=pNJ0phUxWpi2qbpX5G3idGGpK9d_hrw6X9T5ftEfBxPacjZFYnaA26dqtGKGWIi89CfNV3Sj2OA8dFRzbRGzrXPzRyjB5DVRmzpDu1HobfdPBAAZi2f9Itt1GiAe6OemZNLaEKihWebo1aqIlaFU1-aBd19J0VRKUieq78cMnGi2T6ud2PEushCyVN7YFZufbI9qwVxperIHlYaKVm9KjZQVEtgoh-_DC5PP78psvktD72dbzGAOkoy_nKuIg8wKulqY1pZNv7XrsgWM2IpHd0uEZp1WeikS8LRje9pE9YaELx_nOwWRHNDubDfHC8umAsm3PP7dPPy4iEfLenqI5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25833" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25832">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLXdhQvBpHP721VE-20ikVmNuBzY-fI-22ZrCiZaa7bg5Xt1DGoaDOIL_7zewlcycNdDDTwnyO7v1j5slMQalzNARX-l3yqjXBCboH0dUiW7-4UWxi6KdwZi-woTSd_2iQ5W7kbG-_RfgWm_kpoVmSnIxRsphnQylo1MnRCLzFyny5NDa_ic_hbNICs0aeAX6c-Fj_Wq0goFgf8th_TQkgImJ2we2LgS1HqghhnTC3QrXQrmGHB9fmYE_hJXwjiCz-jX71nHoF0t19zHlWR_0ZQY7yWzCRAYi_4PIyUmJ-wn2C62Zz6RRx2GGKhWAAjmZ06XmWB2YpJYki-8rdzx0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😈
لذت رقابت های والیبال با بونوس ویژه ی وینرو
🏐
🏐
بونوس 3+1 وینرو مخصوص والیبال
🏐
🎲
با وینرو همیشه برنده ای
💰
🎰
با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۵ میلیون ریال برروی رقابت‌های لیگ ملت‌های والیبال در طول مسابقات،‌ درصورت پیشبنیی اشتباه مبلغ 5 میلیون ریال‌اعتبارپیش‌بینی رایگان ورزشی از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr25
📩
@winro_io</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25832" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25831">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXBUO7FXEFyDV2FpwddXl-zpXpHgIm2yok1LT_yCGgJnLMGKJzYc5Hi07G_T34fRm8Vu0UA5LJTa5L50r1sFRB9Zp6qXaqsPVsG_GQDcGOMbnFWQ9bwFG8yEZNq6Y9vqqsfI79eVz6pxMSt8YDH-MuUqvcfITxUIw1E17gOvXNJB5dQL_cCKiNBGkhl-pJ-8fuvtyvNq_k8e-fu2F5y7TFNCucsMrdxvXFw643M1bBjRuS4CcESn2iMBOLOTrUoIbsJAKibBY3uZ4JOzgwLEc8FPSbw9dAhHp0Tx93Jq2JlF4tZV14E_DI0hagn_BAum2JxftCJ8sd__M0C1OI67YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌مسی‌داره باخودش‌فک‌میکنه که کاش همونجا تو تشت خفش میکردم که الان برا خودم آدم نشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25831" target="_blank">📅 10:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25830">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/25830" target="_blank">📅 09:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25828">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvfK6r1j7kp5OrV-WT5-nGNaMHzlDuVqUr4BOVH0Tn9EYDd2lkeCdVXJuQXz9gZ0mNd7cEar0uK96W8rxUVCdE5sgYScQPBBYGAkJ9L9u5eJqockFzVGs2t2ZeXZtU4LVjdwJCk91thWbzAd-foSrXm2vcW7YrLzAn8_fE2RKSMSl_mjs30u6tUUYf_sZ5xDfik7IJWplX8nGaBdJpY6DI4PzldMsMXf0xHll3hXJ34Hub2f8Krty2Y1BsNH1YEWdVyGyJQ9xW1CSpS2EM9JYQXY5aJQvP9uciODJSMX2wz-RolSthNYk3iFcFOu9oRbQ7CMxO_7fAY_bdWYjm1WLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnTUtD4xtpohC7B3_oip3WA9uMaGENyVVIxjTaef5bQ9hm3Sc8R60KLWbDkWLe8_a1A3AHX_0_Y6rDBzfpOVLb5sCOQwVtKleP7kDj8H2eBCt7R15Tb6do1sfb1tcZ-PDI1CZA4NJRS4nU0yEIdl728D43siUhE7z0JNnEQ9LlqywbBsR7XhHg-MHL3DR3p-8tnUIXOUpQJD2J-F5CCs-GKHjZah0Ppry-dpOCtv4c9_kVYuzbwppUwkg2ZjJ-AIw_eGlmlhmIcVZ_bYU1PCh8IB6geeoxatuw7hCkHBMvF5ujUabfqfO-C2yEbVOaobDpvUA3N0XNyZBxInGngp0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رده‌بندی برترین گلزنان و پاسورها رقابت‌ها پس‌از پایان مرحله نیمه‌نهایی‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25828" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25827">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvCD8qDAeopqRDw6C3vEdY_WK-w5KHw63vbXt8J_g7OTAWAQtckeeOYVj-N3sFAMC64iaXwO1bS__CNGtWQUTTbW1b0wRffrrpKUikxYR8waTHQ8tS6zabkFt8u68MXSicMTQkvLIq4a987MUnVwmm1tdBTZwsjxBlCCXi2_AmnvZ3z6dgmSLnKVS-C-tIO0xZplDAG-6xmx2Xn1HGQsUxeJS2hYktIY0-tfQOZH8lfFSTROlHmCuufuoT6pUyOYCKjTDpQ4Rdrgm_SJd0ZEr7rnKwL3AwY8pVn14qLL6v3znXCQs26X65k3a3lHUVCpAMNsjnsuFXjxHnOqDFGMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
هری کین:
باحذف‌ما من دوست دارم لیونل مسی برای دومین بار قهرمان جام جهانی بشه. من طرفدارش هستم اون سزاوار قهرمانی دوم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25827" target="_blank">📅 09:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25826">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=YHn1vkZiXT16AZLlpB9jU9z8bGZHHoSwo9_DEvoQaHWtfovlrsPYasQ8gQU_FbACY3TOuFPOlBer22SfA2CDHTpcIR6qrcLmKPD0pv_X4v3wvtx7kAtPk8GyZCsvynxFk-x85QeZUdWL4X8WC4yZ2zMWX9Xn5PbJWPh0jHQHiNYwB85JRbYtZR_Z2dAh8Bp0RrQ2ibG3YHrLaZL74dbLHHeNuTHM3WEv_iuncaOQCT6o00T4be1mQ0KLkzIp9hTZ572JEp86_O-hm6aIBAatSTBfHHDDmTh57RXiU8OKr4Tk48EJIyxHOSfy2p_Kj3s19z_ApLI0plvx1m_OlOHgVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=YHn1vkZiXT16AZLlpB9jU9z8bGZHHoSwo9_DEvoQaHWtfovlrsPYasQ8gQU_FbACY3TOuFPOlBer22SfA2CDHTpcIR6qrcLmKPD0pv_X4v3wvtx7kAtPk8GyZCsvynxFk-x85QeZUdWL4X8WC4yZ2zMWX9Xn5PbJWPh0jHQHiNYwB85JRbYtZR_Z2dAh8Bp0RrQ2ibG3YHrLaZL74dbLHHeNuTHM3WEv_iuncaOQCT6o00T4be1mQ0KLkzIp9hTZ572JEp86_O-hm6aIBAatSTBfHHDDmTh57RXiU8OKr4Tk48EJIyxHOSfy2p_Kj3s19z_ApLI0plvx1m_OlOHgVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25826" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25825">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl7yIoSIFVxt7bRdLSt2_wfDcjHE50AiBiqrduLpwfh2jTQGQLNFLfHVcj6oOnsDMQjuRpVsru00WkXRQOue0UWli0mPRuePsUCyK9mdevFrhUPf20KILLN5cH0y8KspkHx0HionXjXj12heDDqvDeuGV-mDg09klreecnKgHnEMcZWlYtbUp3m4RhB3OVsNHmN-sc4uzxHVhbrbNyak6homBNvk_uIdpJRn_1I0mRWp92j-rVqOnf-jOBHWOevgbG5znmPKPTKmLza7efCFNp8a_PJBT2Mo2gHKJDEK69dpdqXA28k6eSo4AkV2j1KvWwAh-z_9AIQcuOnumB9o-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#فکت؛ تو تاریخ بنویسین، مسی 39 ساله، پرایم هالند، امباپه، کین و بلینگهام رو گذاشت تو جیبش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25825" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25824">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiZZcVtczkCjPLF7wgdNyVFnMYgzv-vbsHjKU_G2pfMTxJOtdI2cWeuYDSQV5CVlICy9OS2duw0PqfPnPpct0b3SyShMhQ6uZVvl1X3LCSvka4ltWR-k3wsNZdfkZfo4zufWVqK2MyvxYsTjckRzhbe008uabGZ4Y8W_wGfMedspg4gJ6mM8znCyguqfFpmHUxebpvH9vR7lOHt16DLK-Af7ndemBd71nrH1q7ONYug71CxIJC8mahsG9MwalLa2neiGTEiAmPmsphAakjpt8-dxaImy-fmwUxrybCZyqxIQlq2XQwl1fqDm7_i0WG6uZxusSx4xjJfuL-nYuyWdBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه ‌تنها دیدار‌ دیروز؛
کامبک دیوانه‌ وار آلبی‌ سلسته مقابل انگلیس بادبل‌پاس‌گل لیونل مسی؛ جام جهانی 2026هم به‌آخرش رسید. روز یکشنبه 22:30 فینال و قبلشم بازی رده بندی. بعدش یکم استراحت و آغاز داغ رقابت های باشگاهی در فصل جدید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25824" target="_blank">📅 01:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25823">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=lYeZkKmeX4jzAE6OiDhSElINAJENgkXtl0b9APuvbvRb7NrWufXPFk05UvQrKVdoV3w3flzrdXUhl82pU0wuDKUcRk2Qr9vmce6Kp-EiqxnYu-OcKJAbLu85CZRvLAyz4asz1rKUJPSwIypwVkpkko_O7WLPCyPXuXVcjZpiOUGJRqw-c3T_u7_jh7_ccZbEtlMjYN_cWcDDO6Ue12JNWZtG39lrfCj4z-uh41qHG6k50Xgul1kjXz5DuDF71fu3uE46OZeNtmSQtmVtHBYH80RKHfYEWd1DxmORqtUO-BpvJlYTk1d_C2l326ryMOOjorUk5w3WzzJTr504RZahDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=lYeZkKmeX4jzAE6OiDhSElINAJENgkXtl0b9APuvbvRb7NrWufXPFk05UvQrKVdoV3w3flzrdXUhl82pU0wuDKUcRk2Qr9vmce6Kp-EiqxnYu-OcKJAbLu85CZRvLAyz4asz1rKUJPSwIypwVkpkko_O7WLPCyPXuXVcjZpiOUGJRqw-c3T_u7_jh7_ccZbEtlMjYN_cWcDDO6Ue12JNWZtG39lrfCj4z-uh41qHG6k50Xgul1kjXz5DuDF71fu3uE46OZeNtmSQtmVtHBYH80RKHfYEWd1DxmORqtUO-BpvJlYTk1d_C2l326ryMOOjorUk5w3WzzJTr504RZahDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25823" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25822">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏆
تصویرجالبی‌که ESPN با عنوان " لیونل مسی و بادیگاردهایش" از بازی امشب با انگلیس منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25822" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25821">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLrcfHAIJE9i6_dTJ8pU1QiIGR5dBaM2wjsQI70Z3QWfTdsBbojuVhUy_Ab3ycyQW_TSjFKUGlhOIq5K7YTUVF44-jHy33GTj7cPI-A5FL9u7-jkEm7N0s9ITDOoz4Sk5AFhPHwqjF69osqH4bC2amPhk9_K6SW84CaQ-Bs-W1CNZC2ZcKj5eRBX6NjWXvWvP9Qx08EQZmKuICBhmij9bMFwJ-8JvlrrdUXB07sR1M7AF3STd54qdCiC8qOgHx2XoncK1q1eVn6VqU8jDY9a7I-6XJr_aTxi2kgvamWWLUJ7S802s2Nx5h0jV-zy324wFKdoc9xRF92Vwd3sHDXvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25821" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25820">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=LaaVBJki3vC3xGxCur_sB_YqvAfahrj9Rg0oXOZklCecg0SIUGchnWg33ao4LjdvXxAJx43U7z8QBa8kMkXMyFvV44r0vHicnPTK8CdbCFUsNmbuNqR4S2RSJWDhxDuGf3nDMRs_DNQRuPOWufY0Qh7iWSrAL5kQu8ySkpkiCIFbyMCT8tZ3pztN0Z62SjsaYfQblpenqlxyVS5fzLJ312lY2Lxbo1Bad8k-i9_R8nRvn3DIkyvTR3IBadueBPKnv0lrLiksW1iAaYbtH1tADjzJtsyIFprGO2As50tBavZt4gc4xh7AutHfKETD3PhNgdc_BX3O1LTIOZ9UL_MGPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=LaaVBJki3vC3xGxCur_sB_YqvAfahrj9Rg0oXOZklCecg0SIUGchnWg33ao4LjdvXxAJx43U7z8QBa8kMkXMyFvV44r0vHicnPTK8CdbCFUsNmbuNqR4S2RSJWDhxDuGf3nDMRs_DNQRuPOWufY0Qh7iWSrAL5kQu8ySkpkiCIFbyMCT8tZ3pztN0Z62SjsaYfQblpenqlxyVS5fzLJ312lY2Lxbo1Bad8k-i9_R8nRvn3DIkyvTR3IBadueBPKnv0lrLiksW1iAaYbtH1tADjzJtsyIFprGO2As50tBavZt4gc4xh7AutHfKETD3PhNgdc_BX3O1LTIOZ9UL_MGPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرخیو اگوئرو که امشب بازی دو از نزدیک دید گفته اگه آرژانتین‌قهرمان‌بشه به هرکدوم از بازیکنان این تیم یه گوسی آیفون 17 پرومکس هدیه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25820" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25818">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmYJ6fiq_ccNo6ABk7L_Z2u-uJ0o2vpGlF43vplJkrmSP35c74BKqrlKjqq4MtzRuZCaDH2DCYTDVROuD10n4FA_Q889hanbeltrs2lV91iGAqvwqLfZJDWUQwRepXhlZZvHpU0g4iKgm4upbi4tcjLp9caGoZA-quhOdts9SpXs1z_7XhgNNJtZxkzgVPwZGx0NMBqb1-deoP3WkMnVzdQDWgYEUrMw5O6issSi9TPykYwN0OpmkuJytTxmIjMzBlCNijaB0UKtM-obnBwzilLdforuejy_jjVn33xdIcceSRlDATKpAEdBQKLj50Y_RatQ3jUWaPhFiiCpTt64_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگلیس‌دقیقه۵۵جلو افتاد و توخل درجا تیمشو تا منتها الیه باسن‌جردن‌‌پیکفورد عقب کشید و ۶تا مدافع گذاشت تو زمین‌چون میخواست تاخودسوت پایان تو محوطه خودش دفاع کنه. تمام این باخت گردن خود توخله. حتی اینکه بعد از عقب افتادن هم میخواستن سانتر کنن هم تقصیر خودشه…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25818" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25816">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1FPKZem2D_GqdXjMSEUjAC0k-1NLaVITW7SYVNi8z1JPmd9VnxLPXJHrXRgM5_-krdCqrDQk6g8T907hAFHWyNuJ_ZJjwOw_zw-R_u43P04fvrSDo8pGGSHJ6aQZzitGKInAcmVb-cKwnaWC0W7MAGI1cc0XKRTkSUQl2-kT5NnQ2ee5icMU-gOB67l-CZMDvTTW-x1OnuTGkpym_2ihHI4-I1fvAonMWO3-8pVTpnr6KMTMcmk1ISurhMENHxeoAcTOeOaL77-fM5L5nxSmqCSWqM2JSDyI8cZ6pJCilZRKt_y_I_yf29zHCa51tN-Lh3jO8FROpMnYiWWOItSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بهترین‌بازیکن‌جهان؛ اون‌حتی از جام جهانی ۲۰۲۲ قطر هم‌قویتره. لیونل‌ مسی همچنان به نوشتن تاریخ فوتبال ادامه میده. عملکردش رو ببینبد فقط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25816" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25815">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeP39BCQ9PziENzDbszGIpTEwcVJX-Vg_YKvvTop1Cw4saLAGZUEPRzCiy45BXRpnPsfV4YVF_3Kw97j7ZvrXoMuGZzFFrVL_SMasPbIlDyBcP9_CkmExorirNbSVfybtyNjZ-vKj0l1mgGy2wgkYcCP_pGCNxTRC0kpL147sdjTMogpPb8kOtDSBtPY4rF0vmzA6zjpT0yBegR1I2l6oy_KL9VmTvqE08tzI3021dHH3weByJisSWlK45zUvmGT7x0b52IAHmvAkkasg9X_CJRH_bTGRkMqtLyjtBwBAN4cijVgRdhDKke3444IJBE5L7CKVe5J_G7R1X_2x-UtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25815" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25813">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcEFqQhZ0DllI0yiTumTYgOkTUiCeXYtkbix7Z78b8x-eYXkesKG9tXZWD-1AYtQ2jfHpfK1wpj3mw0zqvW7hlsto4Qy4D3zMzdK5CA-vzgZB6xcreujEM2pOAxzf_fKgUl0vesQZnvAngOyNWg-vVaOte6zdnrnKim8KplGN5A-mIDxrvzDoOTOh3d6I5ll7saXcEjufqYOLPQ8UhXpwY6UIr1U2sWvlIBn5-SWZ2ylS90GX2B66MBxZwMmi3ZR0TvHmjjL3QoCRfEriM8cJXq9p5696-wn-CLyofKqmrY-YFSiUGjXAnhmtZ_Wyhz6xS8v_8DwwVXk6lP9vbK5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25813" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25812">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdtY3jA-fM_JVO4hJo8sqpQOGFKNKB4esiAHWTDCKRJ-uWegfCGOG4YwYTwEacUKZnYmTGxeDqMl_oIXi6mWMaieg07uDDQxh-e8jAAAnlnZJ95ZDBAXCtxj-J0kuhds0GlbFdzzy9YMFFGE49AN0eWBMlV4uVGqWXCtvS8mLNcLUk4yyEzi-6yRLm3ned1cQKzogO_d22PQniX8Ak3jtvfLrXlLfkGGRPQm7OtabNzcHCc8M2bky0KzZb2A8DbEscuK35sE_VttvFC3WA02rJyvyng9j8-Vi6GfzuQtncYjMRT6XKXQccF7-qbfuXoQSRyL6Wk_ETpdShGFfRq_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25812" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25811">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOCYWebnztwqiXGijjhcwocz_s9UUNfysrJuw89OiLiztK7wDN0_33SMA_MzRaOcx5ApA1wGl3D2GCNvRQpdxW_3_cUvIAFNryUGQH6UwRIroVpDmAMABA9PYWRDDZmWVHxtyFVQ9QXwbapHSD0iQMKSMkrINbvBNibanUV4qEgldZCMwV_UtApiG_uOMMFvXg4nErV3biLinxbsCrWNsLMCmk6178lJD9puLacQ2UffAeHNdJVhii2sbc7sYBhv_lfIyPqsa2FpBK1QyYuP1Y4Wji5PjzFOx6_nqPMhTzJnQHF-7BQT_BOOVRuIPTa4g04k_5Ry0i23sNkbaWHwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25811" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25810">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W00okSFxNfJ0D0N3HIX_XwP7bB-zLH1Ky5rYsZLue4J0X0G4tbK1FWK7yHo7UCrKyH4TXX8SvRY7mcJd6cKKhRrbWP1k2_PMITD7tbIVb8aPjSyWTpc5f9IOVGLct7j3_NDxqIoDY-YNpKjdG3vl9NLZAyYw0Z3Uvm25CwhwDRBXrejXdiAaYn3pGvyrmo0oGNZyTzDYNtSbx2YCaEQE2hrvUNa0rJVwqySruQj5vzB0bfShZ586CbJgoJFaDHMyvo65cl4zmaQqZ6azGmYa1n7IU6Y_TH2xoyE2VfTXO_fNbOI9kWQj9phLsfIqXsAmbahdhd_Gys1X8344OCio1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25810" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25809">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL-Q-RDq-_8XMFoCAj4POf8gUWrzvVIJAsoP3QNYjH9k_QY3R0_PJ3qgZThHkoHN3qjtWvwVMiKHMfZj14BASXi0x4gfPvu0_cDlNVXJExRK46xOXiDesXi7--ucG2vefQYWTYpSIfLNF4fyGKe2hQkV9JAQMaQOpgcxnBMwGGkbkfQUddDrHblYOtFjrMLttfCg3l1eU-s041UqxPiyZFBS8URBkdA_NxdNJTc0PRf0kX17RvvrvvV3-bIvmBekP3uC4Ri0c_GkMx9nft5r9vaNmKJzG5QIG1NjYSHtDwVwS96EfV_8-q0WkFPfuGfE0YaUmRfwlNTvmaayFvxWbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25809" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25808">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0JwCK05mSgC_k3CRdl48XzXFS78KGOTQ8EePKJJvBsxaYhCnlgrbtFyAZtcj7rv7_uV8ziW5zG78O0CdCjsg3UypOChJnM73P8WHBlxwOATeGg-6q4Ja4F-ZG5TKKQUBN41LzqC9FbnAm4qF1HAvBax8-FVBZMnZNQ3fxuH-RN_cC4tdaXlHTN76ZvJ9sw5KkfFWYyX3R1EB9ijpz5f1K9nTqnjEqgsyVVbrMvGs_5hR4WTR13GI61cL1HTu49VIV3AOeDjKHcA992AOgwxlnytT6TL0NmnjIH66HUa-feWX_fidcU4FpBoiNlOMku9ywKqWnKjrur9iZ-6GN_QKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25808" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25807">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTH1cvH-6lcF3SbG4q0TPyLNLOIv0VY8w_ekjob_1fgFpwwMANCWkXIaqryQdAV3_GcXQfj0nE-O_FmXCRnHnTaX6nA9-C-qkFqy5iM3IidXHH1htUoH6y6quINjRGGwS3hESTh7M0cu80gsAOZcluEOWNNq4nf6PW3JdoBjWi-GXQRdQweTQ3hiBDX7VDUvA4noJ6IRZ3jYk73TLYdUdcOpInsLsu3xVys-cgeMXe1C6NO4dzY_2owgm6nQKLw-XJkE47zSz1dy2Hl-a_4KhCCwldTaTiZ4zYkfHfe980f0133Eht4eeOrisczdxp9Sfuf_AJ2JVodWs2--zrNA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل دوم آرژانتین به انگلیس توسط لائوتارو مارتینز روی سانتر فوق‌العاده دیدنی لیونل مسی؛ این یازدهمین پاس‌گل لئو مسی در تاریخ جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25807" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=PKE2_iKijYoMnyOy_DxZyl0T8HwUkm0rBlp4kCRoCEvxOPTe2baY43NV4aDYw-3q8Jh1yPE9hQNGcxFrDYXbgNd5eqsIWcWGH4AY0qO0Q_uGYtxGGBaJOayX3Jvh48N_YHyxfkYB-ZCsOMsPpPvGIT6GRBkYjv7E8jBDRpnsqwZ6z3zkNRxlmPQwWB8t5q9lfSd0sTWIWSI7_d9B6oAIOzpDB4-vhQQ2BKlyoekQiwS2_vcDFrzHyqVm6QN-YSOR8wESs0NTXPvSrhObtky-nGt2TdDspIMOk01MFKS9AzY1p0YZrLf-Xjuvjy3qMju3GNBhKCuxYDfywCPVvQ131Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=PKE2_iKijYoMnyOy_DxZyl0T8HwUkm0rBlp4kCRoCEvxOPTe2baY43NV4aDYw-3q8Jh1yPE9hQNGcxFrDYXbgNd5eqsIWcWGH4AY0qO0Q_uGYtxGGBaJOayX3Jvh48N_YHyxfkYB-ZCsOMsPpPvGIT6GRBkYjv7E8jBDRpnsqwZ6z3zkNRxlmPQwWB8t5q9lfSd0sTWIWSI7_d9B6oAIOzpDB4-vhQQ2BKlyoekQiwS2_vcDFrzHyqVm6QN-YSOR8wESs0NTXPvSrhObtky-nGt2TdDspIMOk01MFKS9AzY1p0YZrLf-Xjuvjy3qMju3GNBhKCuxYDfywCPVvQ131Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25806" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=FUnmGUdL4rlIdZviFZ-v6h0vunQuECgFtMmjcvx5CEMHBk0j65Z-9wyySsiXPMiv6-NbFlfUo3ueauxpm1pbJtx1GZpbgwHJ3dc2YahaOpf4cT0_GR0i3YQ4-qOQHRsydVfRn5zG_tHGCP7gzF3QrWwN8_juS8_kUPzlOFLWLAyHRq4g12e66SkHnMPdvLf2DPeZlupLGHbsFrt2eilyDz9Azh0dvy38sQIpLrmjBmfv1omrYrm0RLScaJ0KbWf_bMdQRPRROwXKhJJXM6NwT6KQ3b2UaXDpmmt8pPC5DR7a_qNxzonCxStMjwkSa6tPkCCQ5AYekRmeSP_v1nh6VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=FUnmGUdL4rlIdZviFZ-v6h0vunQuECgFtMmjcvx5CEMHBk0j65Z-9wyySsiXPMiv6-NbFlfUo3ueauxpm1pbJtx1GZpbgwHJ3dc2YahaOpf4cT0_GR0i3YQ4-qOQHRsydVfRn5zG_tHGCP7gzF3QrWwN8_juS8_kUPzlOFLWLAyHRq4g12e66SkHnMPdvLf2DPeZlupLGHbsFrt2eilyDz9Azh0dvy38sQIpLrmjBmfv1omrYrm0RLScaJ0KbWf_bMdQRPRROwXKhJJXM6NwT6KQ3b2UaXDpmmt8pPC5DR7a_qNxzonCxStMjwkSa6tPkCCQ5AYekRmeSP_v1nh6VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25805" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25803">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=lGPw-6FfMrQBHZIDzpZNzs0A9K7RMMAXvEioiBbOGFB-yhFx2ERphvdIJIrebqP5nwrMyUn8nA1ik0sS08UBONpdwQlQ5Sujhw5SNNe1eQtHX1r6B8SpUov4hAuei_E9twMJMkDx6QEXcgrAIa0PFKIdUqhv1BZucPzyr3zUDQfIUXKkTQD8eTpxcTkxNRCCURS32QW2DZ4hiTPgDgUalWbjUFAMK55Z5KkWoRphqeq4k-V0jFXHniNGzxcaPHvNlJX74ndlvptfFfGLDUliGhvtIae1yzKC1DD8izX69x4d9rMKj49r_s-7ghgtHC0f6YZu6TDeb3tK1uvXulOpsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=lGPw-6FfMrQBHZIDzpZNzs0A9K7RMMAXvEioiBbOGFB-yhFx2ERphvdIJIrebqP5nwrMyUn8nA1ik0sS08UBONpdwQlQ5Sujhw5SNNe1eQtHX1r6B8SpUov4hAuei_E9twMJMkDx6QEXcgrAIa0PFKIdUqhv1BZucPzyr3zUDQfIUXKkTQD8eTpxcTkxNRCCURS32QW2DZ4hiTPgDgUalWbjUFAMK55Z5KkWoRphqeq4k-V0jFXHniNGzxcaPHvNlJX74ndlvptfFfGLDUliGhvtIae1yzKC1DD8izX69x4d9rMKj49r_s-7ghgtHC0f6YZu6TDeb3tK1uvXulOpsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25803" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25802">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-Msc5nshPLU1pUc85iZ4I2wLjJL8oBwYwdMl90vIwKQYaWqqeiU2b5eXR_iKt8uIBIh4O9jdv1NS1S7Pj5OnER4_ZYvRaCgvPCS29qmQ4iza6RZD0SOSMyr89zBor9jMLg_faDZZBEn5XvRujlM0TWurHgCpZPG8mCcbVd9X9WAmJoK1gixd0ilGz_dp8BNReO5lcrmUQwqxNAZbiI-3YXFERxJaP81hNK-CIcv_9eWfaJNoCtoxBRF005fPcAGeGW5Or-QS0vXnESZ5XMRm8-CRpA2XxJEN-1yEoy_aBKTKaQ7NjdQy1w6iahcqtqwMOuabhvXB9YJfEAAoUvyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25802" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25801">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu25WKhU0mBPfeTnZGd-84EZSn2CZHRGlGcYqZsHKivdnQPJ894xJqM_piKZv5d4mR_63wmrgKdpN-Xr3ZbLBdIfIthFuVtrjgUh3QFrN0t22VU1nXqXuSrtG-QL-jqZEzFH8x0SuHnEQcxlL6tbLBVAuvRbjyRVqpkKvWt3RdO2owNsFk-DRIEaefvYm-s1hgrrry-EwXXwfgjRi3D7-xcNyaZhYdmEviYeIBuE3DQWRNnnr65bseaBMTnUYBCf8CDmITetHJ12rZXFa4ltDNID0ZozeKo9AvcfNHHdwDLipXQxDCGigGhy0GxY-KX7wIFPs8cd16UYxTTW7_VbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/25801" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25800">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxG8xv4jgpZJDXVV3y46s51smyZ3FkQ13w_xk6C164_2uPA1RD-yPSZZmhDN34AgTL3jQu5YBgFNtFHeF95aF4BFEbH9-e8hg-yhkmWPMJnvjEOHgAh_cabhSH9_FHakng1Dy_xH716qd-fmdVTO-uzFK03uxZ_rIT5LRRrUEwbNjmWy2PxdC29YZC_2L6_ksw05VXV24NsFLytVOUY4m8SWAurPwDxb9MUmyhzNJSoUw5NnlmNPnAuGOuGNNWYcuBLjQ_zc3v0Z9RLseOurjrOHn3au97FZMv9FjJS-QyV4MHbtVijK1wLrnxw3Cj4TvAGT6lc4zOgAqyiqMqAlUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/25800" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25799">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=pR-Wb-WjW0RpuePR6WridQ4rKW2Ahu85sqpqptO7Ax8VGVm_m7GqZxWe_xW8y5JeWd6xnrmKLg2ZlISs1cU11AYkiKAexbzRHOOfo28yIZNqkFpRKV41U95mPyF6U8zhGmiTZMM4Gvx89392Ak4AIG3qhg2pkFY8IVDgv1eye_Ab5IBENwT2Kkd1PEiDy_V9SrleAeCRKssK1uCC8PoQ8cDCWRMjpQmdztjblsxuonNDQsPVoueW1uSGNfowE7FREEWF0d9_31BQCc8Aws_6B2Ru8SdAoVJf4iRx3fj0i09Z5ITCMHymDbXyR0wdfVmzb4IbIOenTKUwFawA41V33Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=pR-Wb-WjW0RpuePR6WridQ4rKW2Ahu85sqpqptO7Ax8VGVm_m7GqZxWe_xW8y5JeWd6xnrmKLg2ZlISs1cU11AYkiKAexbzRHOOfo28yIZNqkFpRKV41U95mPyF6U8zhGmiTZMM4Gvx89392Ak4AIG3qhg2pkFY8IVDgv1eye_Ab5IBENwT2Kkd1PEiDy_V9SrleAeCRKssK1uCC8PoQ8cDCWRMjpQmdztjblsxuonNDQsPVoueW1uSGNfowE7FREEWF0d9_31BQCc8Aws_6B2Ru8SdAoVJf4iRx3fj0i09Z5ITCMHymDbXyR0wdfVmzb4IbIOenTKUwFawA41V33Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25799" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25798">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUp4x6ZyuIAvcXJO6H1QWU115RtEej5HlLfm7rFHClfTifmCTzM7Mn9JXfBciaLqxXfMa83B49N-qOiCUzTnVoElOx2N1zA4j1qqiUhID8abeDzTO3n2k1IxWBRxNNPy4K358htfx2bVbm_97RKOmo6_nTTb8EoVGf6caGocYxYTN-AGfoIVyIRa-qd-STNsv8VVLxMM4JLYFbXDr7OQJSTWJOEeutZG8gQIQLfDiitLZgyybdDHs2x-ITpi-Ur0-Sa5JuK5s4u-UIXdrUR4aWoNCIVp_fL-gb9B9hPZXK7lDJkyJudOvBrGOgNawzAMVqMHBTYQMZwaHQH-MWg9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معرفی زیبای عادل خان فردوسی پور از مهمون‌های ویژه‌ برنامه‌ امشب؛ علی دایی: تیم ملی ما وقتی‌حذف‌شد که سردار رو خط زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25798" target="_blank">📅 22:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25797">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c436909609.mp4?token=Au05yFON9dE81-XPlBcw3yDMzyidlmp1liOt-rN8xryY4mOn4tRNkUurQj_MmGlQPSPqS8Qp7n-sH44ns8d4ZeWUOg6FdkFEdiYsBYSIN36rXsdCWTs9dCVvmsS3hddp1C5Vth_qAHFDnFRE5UlmRQe2mGcbpGKjYYYAi_0p0AX-iDKEs8LL-MA_iN-FXByUfACM9dYKKYtdU1ggqmg2qrXYGxG0Zfi32-dkyHN9q5eh5tlDhkr3fQYAoTwhPGVGkbLiQTU4Qe8NJjg87VC_J6NA8tfmT9GE0IwfhVSwwxVfVRE1KYk5qVz9d7skoCK-WLSctgmFCpyCz458SYgjcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c436909609.mp4?token=Au05yFON9dE81-XPlBcw3yDMzyidlmp1liOt-rN8xryY4mOn4tRNkUurQj_MmGlQPSPqS8Qp7n-sH44ns8d4ZeWUOg6FdkFEdiYsBYSIN36rXsdCWTs9dCVvmsS3hddp1C5Vth_qAHFDnFRE5UlmRQe2mGcbpGKjYYYAi_0p0AX-iDKEs8LL-MA_iN-FXByUfACM9dYKKYtdU1ggqmg2qrXYGxG0Zfi32-dkyHN9q5eh5tlDhkr3fQYAoTwhPGVGkbLiQTU4Qe8NJjg87VC_J6NA8tfmT9GE0IwfhVSwwxVfVRE1KYk5qVz9d7skoCK-WLSctgmFCpyCz458SYgjcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق دستور علیرضا بیرانوند مجسمه امیر قلعه نویی درمیدون‌ازادی‌ساخته‌شد. بیرو دیشب گفت هر مربی دیگه‌ای بجزقلعه‌نویی این نتایج درخشان "سه مساوی در ضعیف‌ترین گروه ممکن" رو گرفته بود تا حالا مجسمه اش در میدون آزادی زده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25797" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25796">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CohP8czqkviW753skHUc2ghZNa4sjhO7cU1x88VIFzdLetx_-pKFf9e6x_DLcLtdGRJaZEKFXcIGJaaexRgmVQe1IDYycXSGvMdnB1Yo-K1q6VsRteQtgnQJL53zCyxvHLotgxWGT15D9RXLqW69uEChQG89SHDUfy6R-re95h1vSCqUo3vD_FXjh86kaIq7-Jo9LC_l-WvY5rhK07xHY49V6vW7iweuxkOQ5IZnb8mu3G2w2aSMfz4Q0Ja70s3gHN-TN9RTtW4rpV0D4G-V5pnrUQSVeD-3MmY8qTlvAIpwQ4C8UO-obuE4U21uFKiVFgy7tq7aB_QwqpAuYZ97vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هفته اینده هلدینگ خلیج فارس؛ تغییراتی مدیریتی گسترده‌ای درباشگاه استقلال ایجاد میکنه و بچه بالاخره از هیات مدیره رفتنی میشه. شخصی که تاثیر زیادی در جدایی ستاره‌های این تیم داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25796" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=lR9ma-XLm99O07SddXDvrM9H3uclwNXEd_glFmo1VqrByzTHM4aTSBO7QgSa2bvbQJ4oMYHUdWuJ9UApSGkjTauyeKxDN9SX5on_vljX0zg310-jPlDY8rqaYHZy3JtqG-Wdy0PGiwZl6uh_zslADG9Z6PYrYbDNqWOlGsSNxOI-iuWfMaIu3LsZgAMbCuohbhlD2uPwwh3ucaZHEFYFVTpx7AUoxEc4MXRJmc2OIoKVGC6kESW9RQt5B1kjNe96xPK_caWPuv6AZEj9RxC_wA1F0rpSJwsJ0cAEMF1t3SGtEqS3VhFFKxDDA6NCFr8qgkLVDD2ZGjvhfSljIC5WfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=lR9ma-XLm99O07SddXDvrM9H3uclwNXEd_glFmo1VqrByzTHM4aTSBO7QgSa2bvbQJ4oMYHUdWuJ9UApSGkjTauyeKxDN9SX5on_vljX0zg310-jPlDY8rqaYHZy3JtqG-Wdy0PGiwZl6uh_zslADG9Z6PYrYbDNqWOlGsSNxOI-iuWfMaIu3LsZgAMbCuohbhlD2uPwwh3ucaZHEFYFVTpx7AUoxEc4MXRJmc2OIoKVGC6kESW9RQt5B1kjNe96xPK_caWPuv6AZEj9RxC_wA1F0rpSJwsJ0cAEMF1t3SGtEqS3VhFFKxDDA6NCFr8qgkLVDD2ZGjvhfSljIC5WfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قابی بسیار زیبا از سه مرد شریف و عزیز ایران در آستانه دیدار امشب دو تیم آرژانتین
🆚
انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25794" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=DZOslGvOeE1TRb_Xl9k9lX-NFQng0yZcmrha-8so-cwxgBxLo3Gz_uwq-fVyTfzUYlVAwdJR0BiJCyYoEzD7nPHGOyPkqcKB4YS10PL7GcZOW5Opn2234Alq8B7chT43SKSyV2tcmzyA5gukNRs_mk5a8lB1nCqun7mllgcUYRHq3eXf-wkdHGKsIra6lEfyW_WmSWuZBoW0h_vdY1_SfTZeYIIf1ua9Cos1yC-TcN4S_HTYrQ3ZKgSQlWGbrgJZm5a-NeZSk0jNjEC0Jd8YFCx0zNI0Q4b9ldPjwIJYMKzWgHMeBBYoCROjMuhJ5cNxIdGk2uo1CrQoKxj6FPxrSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=DZOslGvOeE1TRb_Xl9k9lX-NFQng0yZcmrha-8so-cwxgBxLo3Gz_uwq-fVyTfzUYlVAwdJR0BiJCyYoEzD7nPHGOyPkqcKB4YS10PL7GcZOW5Opn2234Alq8B7chT43SKSyV2tcmzyA5gukNRs_mk5a8lB1nCqun7mllgcUYRHq3eXf-wkdHGKsIra6lEfyW_WmSWuZBoW0h_vdY1_SfTZeYIIf1ua9Cos1yC-TcN4S_HTYrQ3ZKgSQlWGbrgJZm5a-NeZSk0jNjEC0Jd8YFCx0zNI0Q4b9ldPjwIJYMKzWgHMeBBYoCROjMuhJ5cNxIdGk2uo1CrQoKxj6FPxrSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#فکت؛ ‏بیژن مرتضوی تو فینال‌جام‌جهانی حضور داره، اولیسه و امباپه نه؛ تعز من تشا و تذل من تشا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25793" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25792">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og5q9iqcBY4Yw5tid7A8fIFpXaZTy4sLdSd7tS1I5LzDla3wUwijZ577FjGe65PqPhzVo3kG9GCAK65psnzW4WV1zWIJlLcVwL9f-8I8FCeNTbeswKYEd4co1JmNXx9kppQVu8qOLSn5g1Alb_RdML01H2Qr6D39CSzG3KEBQWwY8A99Ejk5qolnDHi50pzrylk-mt_lJsDljzvnnwC53QwsvhimLYcJgApAvKkl44tqiktUcIUEdFU0sZwXbauUpjhQQLFALM-EwVPZ13TAGnLftOF6J1rpr4tCr2F-6pFzeuTMir0aDRPjNkh8L6UIT4ECy5HM_63j_w1-g73QmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
🇬🇦
#فکت؛ با دبل‌دربازی‌امشب مارسی؛ پیر امریک‌ اوبامیانگ برکورد 400 گل‌زده در دوران حرفه ای خود رسید. امار فوق‌العاده اوبامیانگ در این فصل درمارسی: 18 مسابقه، 10 گل زده و 8 پاس گل.  گرینوود هم که در منچستر سرنخواستنش دعوا بود آمار خیره‌کننده داشته: 15 بازی،…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25792" target="_blank">📅 21:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4C4tFo3B4_ZNWfZ4O9Bp2rKIR8XbBHb7TqjY5FdGn250hDCTNYA8Ul8C5g3eYDqnyb5dK_N5xGIOyJYzXJLBxgmjN1ISFyF11nATnsMvCFvoHSfv6wHz_wk5_vb1uXD6VC5tjwTyGQjFy43-J0KXnpdreEoJ3hPDISaJcoMJWpHfN8mn5RqZNdXQwY1kplX9RL00vBc8w7e7yJ4UAO4Milq2UWH2bpsxZbHMpFKFfRMB5qY5bFHqREYKiwrG654veWVdcxtibb6U-U5MWD3wCN5y6lbNNwgTPGMwtQSGypETjZQBFJtnJEO8RT_Ka9uFY1S-Wq854a1r7JRu1neMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DusDORqUED4o7_DKAQt3oQdnbV-uBCGlsTUnnAxDw3dxassemFYfN6AlwQjgIDdMJHG2XNEB3EEkDBQ71boAoR46KYou_GZAnMatviz6zVEfS_JlwrdHZfghUfNmQ7qX3FYn3jlTUzHeCxPC7o3nMsx9wWXS5zrHbDRWMpQRhpB6Kqa17A8aQE2LKnB0TxrkU5vwRpXWjdc-OxN__MwbH7zuP-KVe6PUyP_21jDnTeIbajg8VlR7Gqj2CLrVHeubzYSLr0-F1-Pn1ypG_CKSBeIV6q292g8C0VsPs74EURO-P3UY7fNb2X5kz1L5NPB8-j4MtNHs9Tmhc_RIWTBnWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVJiZ_MkRVQvYg_zLxgLb-b0hqfv1npz8oCYZZ9nclwkmwtMXz-yHyeaVtdr4MG38jXDqJYp8vJ1dQZTIUJhs1j6mvcLn715cCZQhyNqOK4RkHYX2TjeIEX8Od-Byq4gA7Vjd5Q1XuDtWZdU0EhAhDq_A505FU2h4ovKAb5j53L4t-AWrS3P_uTBPY4meCiOomGG9NgKyNFxd-3ak12eW_S3iQl2e-o5xIWQUrBN2PoqOyRALcKSomWhDATQTX_TussAvZZbcrLiliQl3PkhBOfiwRE82e8Ccc7aeUaSELuDebhn6Nt1RZToC0m9gGGbs7fe1XNptHNhp0hdoq_Ufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4Cpla42Twqg8Br10Qd9diQztFrYsACoN2OCCU9Tvet5EVVbzwSd7phf7Kt2Vh3ypG1LwL7G8b8eMpFtVKTfKhwjTIIMW2g1HmeR7L_keWQDCHTtcfK8vqdga--wlLA7HEszdM7WEmSWl3pnxgiXYfgVxLs1AqcIxOhMgEzKamSpBzEHMy8zGeShx3ZKzffdXUKbuAInICMu7KTj2zSHmbxj9zNvMXLMxixm0Pyagu5vWSNAsQTteAF-mPEa2cMArnWmrrmHcFMPm9DFQp-1bSx9WUtpRoQajQT3xOvY6mxFUz79xuNpI0XLX-u17TYKLUYxMecT5bPkmya5MGCkOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25787">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=cywqd0mIu6F7kS1ExyoLnGQIfeRnATSznBx3_4pclFvC4bUa9NnKYbWFepKt1MNsSAf4eW-0wAV4JjqdRCkCghfNVn66p_NuXkdEiADWWl5CiNsvrqbSXDpCIuZE0f_eA-Fqhih4hebQT9WxO0dAok5XBDB4VpZwIEwX0t02anm7jvCayvqBLg0OSw8rnyfn64PqRahu7X_5nc4IIE8OxeqoPtBNpMYB1SpQeX9qgEVUJL2taPFKvUyMkh4YLngR2fozUuJKECadjiQvxFYMkUHzNkd0gQ7IZ8hDixrpfkMcj4Z2JT7d6zGM1U5st8c0Kf7NyLo2BMwzGbvhTjnTug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=cywqd0mIu6F7kS1ExyoLnGQIfeRnATSznBx3_4pclFvC4bUa9NnKYbWFepKt1MNsSAf4eW-0wAV4JjqdRCkCghfNVn66p_NuXkdEiADWWl5CiNsvrqbSXDpCIuZE0f_eA-Fqhih4hebQT9WxO0dAok5XBDB4VpZwIEwX0t02anm7jvCayvqBLg0OSw8rnyfn64PqRahu7X_5nc4IIE8OxeqoPtBNpMYB1SpQeX9qgEVUJL2taPFKvUyMkh4YLngR2fozUuJKECadjiQvxFYMkUHzNkd0gQ7IZ8hDixrpfkMcj4Z2JT7d6zGM1U5st8c0Kf7NyLo2BMwzGbvhTjnTug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
چالش ترند این روز های اینستاگرام این بار با آنا ماریا مارکوویچ ستاره تیم‌ملی‌کرواسی با خواهرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25787" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25786">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TebavhK45XOldypGREUq_OdR-T5ItGXyyEmZsudy6HjaWJkSiKGRs-paklofxOHxNcgOJnPPCp62LZgf7ziaHURkMa__0UxwY8RFTNzRQqQAUouzXeW-tUQj8-yW_WKozR9YDkaHVKKigwvdTjdlvNPT9vtbJZAip915b3j_VMZ45JYs3Lg8HPzoefe6U4vQDxnP4MBdietK_ABUAllLT-3eWRcmpPOen6_gSQxkwroFBc0TLBuKjXPYkRZ5VbrkEiXiTij22AjJKJl-Tqdm7WkqZ4vImd4ugbJDIRbKlaLttUBdPFM6sqEVS90fRmOuiyv7rTtzrRX7jZLtxfV1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25786" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25785">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p42cSvpAu5UH8eITKdMO3JOM16o4gwv0k83ybxMhGbToBPMfgHO_KavcNYjlWScG0WDoQVT6oMbsMWLavH5cFDh_fXXkGt9tgBVm8aO_DJ9cQ6X7f1pDJ55zXlglzX-QNtmmJtqbMIjUWyqWEeZ6KXPqfRevvt3uEWTW0HCvQHxFhVdJzB7kczqQYsnIw1UxQ6jhGlfW4WOXmwiSBrkIzZgI5IlF_09yj3AmW8Y0owaVBxN_BjwqDuWld9OkjQMNFykDq2ZxxiNmcw-Zz8e4-PRgPHEg9a7v2xgTCMI5Mh8LPFHN1DfgK5p4724VhJPuJp0wFeoSOufnZkymy2uylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌دایی‌ و کریم‌ باقری دوتااز اسطوره‌های بزرگ فوتبال ایران مهمون ویژه‌برنامه امشب عادل هستند. ویدیو کامل برنامه رو در پایان این گفتگو میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25785" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25784">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evRePtbIuKJEv8Mtk1DhCGbuaBVJV_7w6yaalzicTnrkjAfkjNieZc_X3yep1M1sC-_5qVPV5GjUqjApQbqEJZ5xSaxCmFlPaLvLUgG9J89F52owreoAOyZ7GCFO7GtzACcR_uAmCB-ZS-UwCX8AYqqoechxnQXjwa6p7Cl4bWtjZgaZxxqqq6Me304-vNK9mkw5I07EwT42-Ygpsz8b4JSp-OFNC6uVU_MhomUT1TnPufvrS-euAm3jjGUHBrQZFEL36C6PKl0RseLowZA9-WOaxziYuYbfQd2v8RzR3q_KGN40Uc3JsOxZkMFPhRg5UkejsnURB2Qg8IV9yguT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس برگ‌ریزون بازیکن جوان تیم ملی والیبال در بازی امروز مقابل تیم ملی اوکراین؛ خودشم فهمید خرابکاری کرده زد زیرخنده؛ اشکال نداره این همشون 17 18 سالشونه جوونن. اونیکه تو 33 سالگی و اوج فوتبالش مفت پنالتی خراب میکنه اون درد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25784" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25783">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs50JA5hIy90LujyWtpZHKYMLS3CvqrXF0oYNcCRDDv-4Ts-4-hpu73pgd53-toxSdJQys4wre1PpCf6jlPXSWAlZiis4MBiN4ScMnXf6lmE8tOQRhoZqXk662eOgXQDjU6PEifiZK-dF6qqsaWuAlzUjPVraDtRmglWmx3358y9ExMMCp0Vcq86Hon-JbcBXmN7CiIB-3dNW3FcIHTvurwSO8s9ToN8ZcUVPOoMxS2kMTHrCBNwVTxKU-_IQsRx3yKSOvcfDFJpOPuY_7z_mqlghKFFVQytHEfErQDRYRfQWqerSOjOGlc6PhP_fAbaJx-wvZQMtPy1IryA4LWTSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
واکنش جالب ابوطالب به انتخاب بیژن مرتضوی بعنوان خواننده بین دو نیمه بازی فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25783" target="_blank">📅 20:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25782">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=Lhgk7Wv8wtcFcBJdAbaoUN0mofy1G_Z8mKZJNsaV9T83yLO0hJecvXdxhU0wwcWs1Ine6JSEZMGGgorZ0u5pdKg0ehytAJvSfVAmdh9Q-6wlrdZKP1LaLgjJ3_dvezqiiaEjdgk5SGHt1wb5yRULVATHbUgqzBWkZtHlxrsfDoVHNJ8BSjMZ03SaHJXuZ3jiUA1-4c2gvQZzPeJGZJA8mt5DkVJkUL00wewiNaoLuEmZMFZR7OAo_SBsDE5WzCzkIb-he1ZyImDjLmtBVTp73xh-8TFWBWhmZ-tEqEl5YC_y5IM5k7rs2fpwflewRseM3wkk3iUUF9pOAEemvvDqqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=Lhgk7Wv8wtcFcBJdAbaoUN0mofy1G_Z8mKZJNsaV9T83yLO0hJecvXdxhU0wwcWs1Ine6JSEZMGGgorZ0u5pdKg0ehytAJvSfVAmdh9Q-6wlrdZKP1LaLgjJ3_dvezqiiaEjdgk5SGHt1wb5yRULVATHbUgqzBWkZtHlxrsfDoVHNJ8BSjMZ03SaHJXuZ3jiUA1-4c2gvQZzPeJGZJA8mt5DkVJkUL00wewiNaoLuEmZMFZR7OAo_SBsDE5WzCzkIb-he1ZyImDjLmtBVTp73xh-8TFWBWhmZ-tEqEl5YC_y5IM5k7rs2fpwflewRseM3wkk3iUUF9pOAEemvvDqqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه بازی‌های تیم‌ملی‌والیبال+جدول رده بندی لیگ ملت‌های والیبال قبل از شروع هفته سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25782" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25781">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=PBGM7iruGbU8EP6iCjTqC_W6Yx7RnsHVh0MdbNrBFnFbCUzPWT4u024bDp56CTPXG5iG9jfY2ROQiDBfEV6N2dHPUQQ1e5U1yx7_5kWHdP7QfwdMIiuXH9NOEnq8fTaomGeqX01fbY74_HdjVIhxMUf9O6UO4HU-T_IoJbsslGPQmGM9Yy7EWhlr0E6lZ2aFXdACFbjnBxdPbYG1gohWsS9W_TJbBcdt8jktErRE3QeUmdL8_cYR5SsLjiNaUi_MggwhBZjUMf4HvvGfOh7CELYXf4l6ZseboKdVw9Fn6m3_oSvKynHALrGXdF1cLeLJGdit7BvkTC20f9yvnf95Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=PBGM7iruGbU8EP6iCjTqC_W6Yx7RnsHVh0MdbNrBFnFbCUzPWT4u024bDp56CTPXG5iG9jfY2ROQiDBfEV6N2dHPUQQ1e5U1yx7_5kWHdP7QfwdMIiuXH9NOEnq8fTaomGeqX01fbY74_HdjVIhxMUf9O6UO4HU-T_IoJbsslGPQmGM9Yy7EWhlr0E6lZ2aFXdACFbjnBxdPbYG1gohWsS9W_TJbBcdt8jktErRE3QeUmdL8_cYR5SsLjiNaUi_MggwhBZjUMf4HvvGfOh7CELYXf4l6ZseboKdVw9Fn6m3_oSvKynHALrGXdF1cLeLJGdit7BvkTC20f9yvnf95Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوزیبا از حضوراسطوره‌های تاریخ اسپانیا در حاشیه دیدار شب گذشته دوتیم اسپانیا
🆚
فرانسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25781" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25780">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=Dj7gIf_PkHj8j7LBFBL3g1he3mAH7deIVj3TcZl706FmOH6Zy4ZcET1F-y9sfH-6l1UKnAXIZD0idRl4fDKXHFDFu1HezcweMDmKmyVL0O1FHxG1h7tUIgHxN_Xvsbw8vCE4Afwmmg0zQXfOJYLRqzkl7mwiAF7XOzG9gZR-xk89qiErmfE-Uc2LjcVO6Grgiy4itIVFtPMDoxmuocTKNfcIL1o2dxvc1fJ4siEkQH1htbldL5e9ebP-58OtDSB5Btc-kzR2UAX_1qmex1zn99qpNkAehvb5Ja2BlL-i4VqEcuOoot49U-tR2Kn44CCgu15o9DVn9_Oj_jDv5WMSSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=Dj7gIf_PkHj8j7LBFBL3g1he3mAH7deIVj3TcZl706FmOH6Zy4ZcET1F-y9sfH-6l1UKnAXIZD0idRl4fDKXHFDFu1HezcweMDmKmyVL0O1FHxG1h7tUIgHxN_Xvsbw8vCE4Afwmmg0zQXfOJYLRqzkl7mwiAF7XOzG9gZR-xk89qiErmfE-Uc2LjcVO6Grgiy4itIVFtPMDoxmuocTKNfcIL1o2dxvc1fJ4siEkQH1htbldL5e9ebP-58OtDSB5Btc-kzR2UAX_1qmex1zn99qpNkAehvb5Ja2BlL-i4VqEcuOoot49U-tR2Kn44CCgu15o9DVn9_Oj_jDv5WMSSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
#نوستالژی
؛ یک زمانی میلان تیم نبود مجموعه از سوپر استارهایی بود که همه جام ها رو میبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25780" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25778">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnI1vSM1Oj1Ztj25WNd4bFhlVhB9RfdSB5bqG0FksoVCh6L8U6IDiQkeD6kuQHyTQ9QpDjv_vwa5xGJCo4Cog5MGFvSlF6HCqlrdCS7iV_fZLjnSfElha15fboQaOmnoFUkW4zWqjPrLdxEbRvuumAS1EDoEBmX1gjPnEz_ioIGfKqaS5NG_Wj9_tLHRzM-BGhGt3EK0cwaFXdkYmwQqCqVZJG8vuRBT7M-JLJ31f0bzoP48eNBHJrRnJhIdSqEi3lj9L69COdlqmimmyKQhHNkRv8uO08Ub5P1rIOLxS_TM2vhdfqo0nEOZii6KFdHXFADmToZacztxtcE223XKNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuPh0QXjG47lKtNGhwxN2Bd80gIzXMgZAQ5EqSXJkfgSa7DKSiL8Qp5uiwGHolFOyBRgUjqu9pYRKkz3hCLs6wsm5T8GzcFs8oMUrWlA1d0NyXZ_iwaiOU9Olf4ycxbu8XVbNZ7gfYqI8Swe49-EUXhWHj-6NhSZe-cF1dQwm6X-kgZM92euKHyPpdGcpPAb8w6-eqL80Kr9BNY1M_mbRHbMRlJIG16d7pBHS8HXZALWNHy5NDKBszL0fwrP2oemddqHcLwzTzP4yPdZVktwcTFGphkfggrYJOz-N5rkNehY2s13KfUh1QAnviF_eRF_9Dplav4KDeWJeJVQ51GQHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
👤
مدل موهای جدید مهدی قایدی ستاره ملی پوش النصر امارات؛ اماراتی‌ها رقم فروش ستاره ایرانی‌اش را 3 میلیون‌دلار اعلام کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25778" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25777">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P__iOHYs2eEu3gHNscqKXyLBVxx8wJjMSfpFx882xPY514sTw7Giy-pHoAQgjXzXIEeaLwWgV2GgOTTSMNMSx3fERWruYyZHrO9xmiP7oUM9bIPEyiGcntc4DndhwsFA9Fabz3DyjgagvA4D1qeNjwMUrTeyT14oVZaB44ck6itjKCtdX0Phkg1mYZ2ENvcGwehNOLGGOoJSEYlYWHhLdWYy8lgsFz2Uxkc3JMoNiGrM2lRKInQ1kSqCJUrWM8Br8O1ZCQHyAM1_z8z702pK_qngjdHEFspSJJFPZxLphs_Ppl_ncbDDudJRjOYXb37i4VRMmjuxcRmgv1LWnwVO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛ جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25777" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25776">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELLj6WivRYH0jxuuUh5GkK2mH2UWnZBF3pMY3DPWMC_Ksaghk7hHT3VPFcdDFENPQ6yNNMOm6u6K1orLrRMx2VEH5qsyXh_pu36hMmxVLMGbizsm8LJelcDmYVSGkH8SbmyWCln4woJZBGaURVDMrYGXjribxIB4OCGPSORKWMrncId9MHdPuiJIMxYjyWHwkQDWk6AeYjT_mw-Qg743KbEk38p7EmRxjAktuZjCj82qdDlp-0HT-_BvAxq3ZJK4F_2osEjokRmqwgpIT_ZFEgiij_X9fOP9zA_1vsCxgP5cQf8anCrUWdcsL8cq7RxA1a-DnRrZUxFWeEy1A4zRXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25776" target="_blank">📅 18:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25775">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGgWGIBSrdxEcisyQfjfqdUrdaQuTBwXSJbju7vi9AezjH1EecKh4GaqA6FQwrjohfCCUQdFMCMsryvE26f9Dma6bhFe7a5nRqzw4Pxvq6rdB8o0yCRzBbMCYm52Ztl2NZbet1PTHiIGkfCn6oV68_aVE6r2IhpWkPh1bxwDjSW4kroSVhPEM_UgMsF9Vnqeqj4lKTkZEW-n2MasJIu8xcYeCIgUYX5Tj3iCj3upckXmHr9YBslw9-c0uuPtN7cM4D_WkqaU9jbgwYkADkXsEjsjawHuchC7eWHFUszzEse5f0QGQCgkEWmNLwIgh82Hwnru73YXacfJZ1tKx0sCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخبار دریافتی‌‌پرشیانا؛ احسان حاج‌ صفی قراردادش‌روبه‌مدت 1+1 فصل دیگر با سپاهان تمدید کرد و تا 38 سالگی در این تیم خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25775" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25774">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7Q9cbHqTu9o-0XeHIw_xxtyk9F-UjRM4PJi9gOgiWeRqvxVr9or9abkrWkem3R5OdXbVnuDp5WSCkQNw0l65tWZsgdZC3eC23VvgKBd9uhD6m-fAO9qx3xr_jf4DIhTBS4hLgqb2DujevJmrvD8tqXQGG5peNBn5eaObhm4HgVIyEjjlMm5d4mAIjGwcg21SNoFSNI5EYHdyHV-3TVvrMXrEWGeJ7oA_npWBcPbvOv57GgitRxQ1pswaRqF0gl0fmlLK5o_ofuHaqosIyn8P7S6xMkoZHrzfWqt_8DmOovMLiLoLZPHs4Bn7c9gSzlLD_VpzeWPBaLiQBs5pXDt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#فوری؛ سانتی آئونا: مایکل اولیسه می‌خواد درهمین تابستان به رئال مادرید بره و این موضوع رو نماینده او به مدیران‌باشگاه بایرن مونیخ اطلاع داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25774" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXaUfY8aUXYxIiqExxKEkLGw-k_h5gQKEGfbDQFjMXJJHfbmz9Qh6amiUirVMACgT92AFWurEUrnLqtNwbF37o6fEZ4HSrU6qAdgfIt_xq05Sbv_R_mYQZjf4uxg08SeuALqKVcRape4RHw5V_epTmIk7NWI7WGgTLAZ-PdTDD5X1E1nOcDcCQje1GECK4tZJguI4gccvBEPooqmB2eXZ7cvaZyjnsl30UeVTpIsdwp-7DCWF8c3-oVxWsEvehgT48fchWdEdkNd_g78eJFD1Mt_3VjnWmJespDUvYrq3A3IT9DNsIUD3gx2SKmOkhT2BA28Cj2nd2X3AcuX2j9puA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlsNk8937Fuzw1wIfWAYkz6G8WlM1oPJUovOQes5p0q2y-7dck1Avo-HFjwJ4Xp8_QClJE5DcFf0RJMhNt7v4S3na9869qPC-Oc3f9cux4K_9uWzPvXhsUH1k9b06lWH10X7N2UzfXUOLAWtdBEtTQ0z49znMqiCm56aGbGvlkrgpMT7kcHiHV9GtyT0Jo_G1Oui4Y6Wsvi5W2NzPG55N-ytm-cgKgTmSBTprUOjmjS-YTxj9fFVhhphOof1W5Zu9fw-LUPbaur0Vm2GZjQVRSl2CD3xtLm_GXwKKQ6TJ9YjRQc3w7-YIZYpXJ3ovz0aU_nv6jPvl9UXvBQqXicwfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEwm96s8f26e9van5_CigaB5MLBwTdwBEfhXi5X12ZWenD4cqAA8bQ6e3WOtVVNlUoN3fetWwSUMCczJPVz9S7mTVNS1X7azNerLX40G2Tg0MzKNRgfhV7lDur5ytl6FoK5Cjaa65UlDRXwJcruQvu7ZrONKccX18vh_VemuOlBtrGJPpeZC9PnAXV-f62cZztoaApHRA_l0xjPEuuHMykt-5HLINU-0ondpVdpafT8qNE0g7gnQ8qt47aWNRDZIrdPJT3za6SESJgCdgfijxmfAi1EmIKahF7DZSwCAHqWdJJOD9Zhu8CoTSr-jerSLqVXMpaMr8KwmN5QcVlY69Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XguCTYs4QAoGYnIbipj0Al9vnU_Wko8Ur9rebmTlp026YREZXh_GJYU0knSO20IGSRi32PuXC2BprHCQHAyErB7Pq320l_HGOUG1-biwTD_rY07Ccxo4JeNUmlLtEBKoEi0Ld6SGc7T8mtG0Hb37ml1nhD__-Rg1SJTFK19HSO__iyy2yeaMC4GMfCS4PolQDWOwdAcI3pvsMwWVuxT2HSMxcJNEZ5omcxgDyWZEjFdTfkhvmUvMZUTpyh-CCyTKXdik3nSWOdZ1jSr8vRZrkB6-VFZkFe6CYCMpLVtvYKcZD6oYHOVdZ4vP3ZpT-u_TNDKLLAPLUt9i56t56yEmjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cp1A3RomG4SRTqjnmFHlOUzt5hY6CcEXod5szwaoPiYL4MJp7CIX4PCTFZ2CTbshvCdrVPZz9YQ4vfEhcxvnbC8fGOWNlH6S-i7M85mC1M_zcQrlElbql1XRQ9cFig0Sgo8YeyYAfqn5RVhT5GUurk_9G5UrvJXqlpDaV_gWfwFIW541VF6aZsi5Ll5FysvqSVL2R6astFFZKMQxB1trcOyoUHZ-FsOYOU_6WTgTWOP_knVTgyKg1_nVLuO5J6diUZU0Y1HLAiQyvnJRhIsAos7HWtCRIWfOeu6GCpRXNBxZu1wkPLY9-Sbc9954iy1euZUj6SKNesWdK3S9H99uHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25767">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDvY1DhziiBgOEQxMgelgNNst7JpIA9LXYpQ_0sb8vtJEC1kNQsHU36i8R1QQJp1eYxhi_z5oHLJObu6OG8u5ZaCfwmK3sX2EEQPLTy1SmUZBhM1krNXboG5OIvWRIa_qj2afNLVAxbcnFpJn6OZdADpZUy8e8VLFY2qEhp5QVvWbxr-pi_l3foKzzMZ7JWvurD7iPgstA4wbQFyZigKtqLMvR-A3bwKqt2iwvuDZzMoqjRlxjv9ss5haOthq_8b8d9hd7o7_p2Ad1pRxGy0FYi2G5vSOV0oQKf-hiJGVcDP2vnkhGCph6q48tugTtDcyBAmp18qaiUCgIzPaslsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری:
باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25767" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25765">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=DOXCjLwPDiRJ3S4JUi5DODME3KD-75Zvn89u3OJML4GaDl3ZmqL7q-_EQF2iJPYzD-4gtNgl0p8_0qvsAqNXql9S4RxUUHdjEsJ2Ch3ArF_iQ07ASVh2j2efA6FGwrG3WF8KkFmbHLnchhOrj6Np3bxPbkXlkmN4p5cKl6SNcOwBQMjbdpZrqM_Q-f2r_td6s2wB2KzJVPYR4XOZzaggi_manZZKXnS8M4CypYzX6iqiXe_XEgnwUdMuxlAQRz2tDoj0dn5zGVmnhYD398Gvq3slAi9lymX6Gv7JwKgwXdoHxdFLJU6IComehuGyM3SI5CtbXW-ZDiw1EO8Wa2wiCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=DOXCjLwPDiRJ3S4JUi5DODME3KD-75Zvn89u3OJML4GaDl3ZmqL7q-_EQF2iJPYzD-4gtNgl0p8_0qvsAqNXql9S4RxUUHdjEsJ2Ch3ArF_iQ07ASVh2j2efA6FGwrG3WF8KkFmbHLnchhOrj6Np3bxPbkXlkmN4p5cKl6SNcOwBQMjbdpZrqM_Q-f2r_td6s2wB2KzJVPYR4XOZzaggi_manZZKXnS8M4CypYzX6iqiXe_XEgnwUdMuxlAQRz2tDoj0dn5zGVmnhYD398Gvq3slAi9lymX6Gv7JwKgwXdoHxdFLJU6IComehuGyM3SI5CtbXW-ZDiw1EO8Wa2wiCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25765" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fetr6WJUO2OVtDpIjnmcJEQbOKXv1wC_K_Cyls0iRFQRQYkroJzPBZg2VEQxlFkm1-dmltgPKgnRKzzkt-YfCXoHsLPXs1sUDk-RsADTxyxFCuIdILcVdLJr1w96z9XaR38XiEm4zyjbvtg21T9lnOPt7grbrgannhF4u7N8hS-opA0oP26f4O22qDTraAQUbC3W6TQbaEpSKP5vJ9lvzCDd5VtFG2UFQN3kdmTttfGusYI68kqG6PvkoPJ3JkQzdse9U8UY3EArwpemTVbFzVFx11v-zTtmRqj_JtT2uMYbXe2mn93HMu-utvOO2IQ465cugIELpsadIzxW63T4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8IuPVK1F0VfVdcgowp7OYmkxc4QXJVSgsMl2Er-GMbYS2Rb0Hd8q-dNBw9eu3mP-i0RLFLkwc9yBt4H1jYf3nteHsx2TOPRNmOTKUOWablojAjWFO66Zj_eZU1J9egxt4Ui0cEuV4Roiuq5YPMeRpcHon10qQzPHDcqbEfR49LGDeopWJxg6DX8-Rta67fOE0BSuxTMPSTGGOoLgg2FN0JjRgCVKx97_C15tkG_zykwc5rdW_isUs_3HDvLkHPXQMySfFOfS_Fu7xQTY3Td1aWcsmw4Z_BYKKt6UmH_7JkUFD3OJ0YYH5jJRP9VqI9uTGKwTaAOX7VBvsWCPk1Drw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ysji9fawu-mONIVUoAfyu53grgBne98yOSl5ukSmHn6WchITaYEEAacz5FTViZKwKpaYyaJoDLquLRbMNNTtU8OrkVk-eP68C1rfDXVI03Nce-95vAzCVG7bZSrr6THo1UdfTjxdJgxLg1B3hXKEDDU2HCZ-f_agYcHiX90VeJAOzJuQISE9J3cSkFIFRx1bhot58_9GrmfADS0kxuGfvK5fP19RHA4EuAyTJyKWs9FA5wdPxwyJWB6Vi74J-CPrHJUgraZEyE3vh8MbBsspbog-leDJ3vU-H3mEOaDV9UANM-wiQFweIIqKWr_4YM-W_pd3rfNSS7PrHb7IgwediQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=joiilBXH-DmgAAtl8yxfI5DC9EGzDCe0U89EQEG1G3dv0mivVG12ch0ts0kXtNHTYJOYizBdj9PdqVwGOBdWjeEnQt0-hRTZ9z69SStFUAcLucPaP-M3UZ7qGWsd8Z3RvFsaNWUpQ4KpCqXp8doyhel38u-vHl-CpEv4DIKqaIYmsDiKa0fMpKFwItFnm21t3qwCj1AgxP1JNY7nhaQ9ytImLzAE6eTEGIqJNz3jPzJBIL3ZJyW-gI6cMyVlxi5OGQt3-EAnkIDoWOnJUEIIcSzYyLVGMqnapQ_4mz0RILIehkSOlPQdIsHZAW4_Q_ZhsmVrZDolwAhE8DEjac8bjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=joiilBXH-DmgAAtl8yxfI5DC9EGzDCe0U89EQEG1G3dv0mivVG12ch0ts0kXtNHTYJOYizBdj9PdqVwGOBdWjeEnQt0-hRTZ9z69SStFUAcLucPaP-M3UZ7qGWsd8Z3RvFsaNWUpQ4KpCqXp8doyhel38u-vHl-CpEv4DIKqaIYmsDiKa0fMpKFwItFnm21t3qwCj1AgxP1JNY7nhaQ9ytImLzAE6eTEGIqJNz3jPzJBIL3ZJyW-gI6cMyVlxi5OGQt3-EAnkIDoWOnJUEIIcSzYyLVGMqnapQ_4mz0RILIehkSOlPQdIsHZAW4_Q_ZhsmVrZDolwAhE8DEjac8bjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRL6mYWf3djUUIcptrlIApXoVyRpwvq7x3UBkgMs2_QmEOVYGlKNOBdIeoxTMqdgJwq892o7LuEZ9rQ8dgb2vKCceyp1UA0gP6Uj24DcSw7zeb0git2iCIZlbjhORONpaYtOwQ4l28fpuypFc7RS5MvweCCYUMGfJ6YHhBqqTTVetsOirVSl_o_9I8yUMV4z-S7B7MbnFO9wGwsFBU-iCN5yIH2-4CQLBp5yMWCQ1rlX-5gnCDyC2V-49uqu7Uak2RLJAvXfH53nR0AxdVSCwbfIuoQDAOhO8UbMoqXF2tM9nfq5Zno388fil-daAcy360vshWFWitCSJkM1dsrHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nayul6htTcKyohd1tKcsnD8wrlhAuJrnx3YHSWW3nA1lEW5hD3LMuinUnPjASsSrJvW_JLfPUHG1zAaMTtOCfA4BdXxUKl5GhZABjpmIgeOgQdkwt3LVa-jLCgGmQwbyC1A4XVgb2Xjcfhl0sRIFTXYbAM47KxHGaSqPlVYFDtve0-jDIU0ZBj8XOD4nTgb4koibt2fB6PXO9b6z7Ix5UipEMox0xgoMgWyENJabXAZ85U5FGC7ORNl8RHZgTCgEEGAr66ZlJCOm2KTuNr6D8W9donBMTwlt_blD_NHu5s7LAt59FHn8JhBJpsuAt9RN2w_3jd0lypT54QKNnHyeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxMUtoJCI7pqPALDEC1ejWfVt_O9wfsbH_auG7c6o3612CWdP5Q3Y3c88b7jOvI3eZDy_xgVX04j-oke7g2yXENk6HCa0NqWI9EmyseNyxuZ_I7Blgx42CdHCh0YRr2tj_PfyA46VrClG5w7KnhL_0gDax4ZmuoTfedI80jVpki-PuB7ehg1Hik3IwrYZbFBd9cCiElh1ZIRKCelMPtkh52Y7-zUp-tzjro95Ew_MQr-rQLwa_CGuj_Rgd-6D15lrFQPstneXnlCwqqCnmvqkkpadluwcwkL0XDOEOl2sLCxEu0mnlGNc3upltNkPFfyXSviYSPp3dFaacTUaTJpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hfcr9Kspg6zBrZfCm_RNFfcvpuEoElgxkFykwznQIN8DBjSilAZ37nK_emgMFct1TXsqb3z61Yy-6g93fIEtWmma3X3QvfVM7F9QIFW3-IspIJ6pFEuSF8Yo_4P6E90AKcveoTABzr4rU_batOqVlsVupSZpT3nhSjwK8dzK0r_bhZg6ZY_5Her1W4NFuzxJy1XpzTJaRYqCeSHN2V4RM6lV6C6G57jtA9MJrpceJqr8Oh04uOKukNyBParXDHxxh8cBs5mMKFVjfWYBWwrVkZIK2NiSa0Hr36ZFYVVvKzFT6njNwie1qGsS2y7y2_WDYv_3_mPhOwPUaiAKYLmFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_EsLaOMug43n_eYzlWAUlVamOC5s8hKaevgaUAao7OvAzzghN_vaJe9ZspRWiNEjY-GYyDulNlMFaH3RcdANbUQyBC99xCyIZyi3HIjqCOKfeT0oTQzubQCdKASkmNsJ6B5MJmfV9iDBY1WbwOVAnQg7nFe4wRNxy2FwvsCHSNeREW6mbOegGTwOCm0Bvou_IK6mOUiyNCVAnMf0Y0ViDjf5EVhDdqP3WAt4YwGmPo0F8QkM4TtGqzlOZT5h-4yvby7dfWfUuGtRuv4DF05tjiBi9jI_Z4e0Dw4Nb_KJU0jBOGNtNpDjDbaIrsLHO11-eYWkecx7nERV4VgUJX93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af8WEv4-w9O5etFdeA35nDPGVoCELUpSurdIcp_3bvaMe88L5srJIAu-Ha5CQadDoavWk42EdTcjMY0rBzfFlGujx-10G7drc20wRHlfHljlSS2RHaE5V-UIfLik9A_6l-eWvnCW54tc_8I2FrIZLjOoRjpc7MKoPopJAMi7yFF9aZYoxa3ZgaTdfuMu9HI6UzpxaAbm1F33o34VaaTk8qWiXA6MitLSqMSIRJVYFnHr5IKdIvGuYgOSPulP8vPN2mGmDtAi9s9-n9NPK227LSuxHBI3-93hn-CxNaf4a3k-OWFbVzNJnBjNp_wazn4gUj4JZzV0z4XqrE0jeNtxFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2KO1wDJBb55gwVDrVVOM5fWj3LSu-tWfa2cmvdjcAKQjj_R0cMLyVL4CD61bjo44B84Oy9LrdpEZq7VFbk5H3JupelCzFECavsgsPW32lUXmTpPfaaQcm7aVcSPWxfmX4UeCxF9JE0LJx1MM6ThobSGEuzqPfVZri3JUw5BVdaJrQ0R4sMgYijbzwQjdztA5INSPhM_38BUWy0RGcse-AfJMk7tpspBf3iS-DPkQJS8MHB84rH-Iy3HMr4pduxHwUt2UaUzQ4Orxp0iT_5DgDkBYd8fUZWsfsXxnB0sZ6yvwojzFTrmruGpx-IBC-b0RYh8odOPVO5TjxFWhru8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgHwgtyjVs4Q3Oi-b6Ij22bG0jSbUvl8G7h-9IE0i-ZvxNgaHuQGOVEQ9xAO2QP7ap8zaMKFkBGUetyykv782aVDGottPARpwW0rMzmhh38JHHS3BKPbLH3NOH3FkobX3VX1jRZmXG7vWTmP9z15buwKZ4H_ZcEpaQl2KpWxi0TeVGfH7zN_6d3vuX92TvYyaGDl1Xy3eb3_3h82INi6wWcHPeyHNMEkhvKDy9N-ljfCH7sl7toU_bWQEK4AqkLbpIRiX6MT6vJ0P6IEnup2gapf2OPLhgIGJoPej1terH-3dUDnPEaKRQIgHyVqWor9Q-2kuQhBL6TZ0ZM6OstjUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuBBPSB236g88wUl9SwCw6TWimIp2jqxqEz0kS8qPhM6LA3x79ITo_N18pi6QddZY03umpsIy3sudPGVVc8jCX0pd-zoDoDBxww4rpafHsfS7HwZVS1Ao2Qpk7qSWRKkBWewyzGofhkSSL4norGs1XM30iiAsRBOhQBKTlnj2e3cWF5nihnrQYxWLMAZ7ZrKmAYb5WJhIeC24b-EQ9FWIktSYmK3UAhSqd7s5lggba7m_OtGukluwLhc17x6CA7jVtxgNNmhCgMY60BfVJ4ur3l4xInOcwfpMlTQX0JASNamk1y4-0bsvEiXscD6l3BvnoJDru15p15bPy8tNRZejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=sD7TkYcgkPR5_NFuuYGAPcbkLr3TxCBSoyaKR7RflkejkwE5uLuMcjdhnbD5MciMlXCBZy6EaN6gkzY6bG9p0kRaZdGRhyZDX4HIV_u6rJ-TmJZck_WV4Pcce9CJkhX0jtKLreYYlMM4D4zy5l3MYlSTQD0BQdFdIJbupgNKABFNG8ROG_JpK4nq7rBpQMrSbg3bRi0pC9heR_RvgvGTrb6AiG3zcV6Af1Kg5SmHgpFXL-AZ5pxz-zH6JpYq4Em1ZB4wZcw2BSpL9pFeIvWdjYIckWYvf2inWEzPQ7k3IBLmyx4K1aeU97zXj4CdbdZO7TpPaewyxv7WGjZRjJBCmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=sD7TkYcgkPR5_NFuuYGAPcbkLr3TxCBSoyaKR7RflkejkwE5uLuMcjdhnbD5MciMlXCBZy6EaN6gkzY6bG9p0kRaZdGRhyZDX4HIV_u6rJ-TmJZck_WV4Pcce9CJkhX0jtKLreYYlMM4D4zy5l3MYlSTQD0BQdFdIJbupgNKABFNG8ROG_JpK4nq7rBpQMrSbg3bRi0pC9heR_RvgvGTrb6AiG3zcV6Af1Kg5SmHgpFXL-AZ5pxz-zH6JpYq4Em1ZB4wZcw2BSpL9pFeIvWdjYIckWYvf2inWEzPQ7k3IBLmyx4K1aeU97zXj4CdbdZO7TpPaewyxv7WGjZRjJBCmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnO1PBHb5qmFYaIX8q2q1DAqcp6YOpyPCjtP3xVyzam_23DCgilJvss0PPMyxb3J-cHvhmt_i76IZEUx5VEiFyagcxy9CrJ_csAg7UQgyAAe3ZmN60eBGSL8Bzxq2dy0WD8E1cnFwmLvseFExzyEgkP_Zesr0Igd4nFTpOlpTp-98s7LSZBgTtBw4ojnnd6z9KGFDzIK-wNrP35ygARiwGb62beg2-nu227sraP2N7wV3tJbNOmvtn7axHZ2vKpqg97vT3_ZTADKlJtyRHiPeORQvC42e64WUbDPYZ0dxFUIuI4OiYjG2ueDu6g0MGIOJKTStthyEXKBN_9pA1oRcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiYpUJu3ZuyBcSsbBalKhDScgHy8hz0UoEdvajZuSk2kqAnYdPNBzLTJq5zyQs2Liw8nmDsojbt-zcMJU1pFnIQTgR4ALCfqIfaVpbTpxVafxAUapNZXiAZpJOKc9-ZvCtuNb1gAuX2H-N_wwwC7KhCxHIwhD_HNNmqp6b7KoR6mDJ9923FMGxZLjVgF_4cqkbPudLeGF2xNpgAhgM_b_psL8tU8MU6ee8zSTElx_m7JQ8vQd8qKNYSAWxFSi43bbI8Tl66jSjIs2aUsHmIKKxJe4ySMyX9deaD3FZ4Ptcqjl03MWuq8fulAOKkH-MD5-2QXUFtIK0AmIo1FMlfZsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ny98BHmQP67oTdE9W5W0g_HWe8uMlpnG18EX4ter70aAfMBuAaBfpIyFEDpDUp-0NaUfASEPUD84ogVqK3OhpPiZXHD3z4dHMrCG16iRwR5O9BWtcdV0GcE1fCSLFK6pqyvGfOw43dIYgbG33e4-2V3EqlplxO3AabLZwhxffzCGY2E6jGuV2w-S5iicuxa0V3XOWfOk8xEl5_UFt7Q9k9TYAyTpf9qdsVFlK5E3B2MOXfmeEfGQ9cq7nzeNq7il_2kKcnJVm2-EKpNKfUJ2k8vEUzhh0rCJdmBe4ApA_YzckQlujYWP-JY9vClzFxiTTogl1z1rfz3WQH4G-56kBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naZBRvLU-eZXVmPD5TyZy9pjnLQxfvjWgRFlK4fyKVjbNvmUOKNqyJU9NgmVOCIoSf_wT_Jf6iu_quKEUoPccbG12bMNA7y9nNhlwfGhHux0Sv98sFvpmeKkFO9yoFu1s2mAU2GT3TsuzbNUWEjIwtvPyDuHvvTQPjhYHOxVU9vEHXkOiP38L8fJWVWfqQoA5ZOIGZ3_wG_v2a67Sw0PFqNYvLvv8gO173wQbWIRwGNxlruCj-CQ0rZ5sFrZSPOjO6p2xk00td1Shdoqh6LMGWHkO3Qlhkl9zmj8TUM16LF37U-81FzuPlMUjPSvQL_gD8j-Qq2oBZ2BZMc35YW3Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDqHzWtbnyL-8Du0NJoH00lzptxdu50mBHTqjX_aPp9JyagHVqWcVQjKtH39mGgVwxHo_1Ce6GpZ2raHRQapZAOXatNqlaxiCLquOexd9CsOsZaRLt211n4KeveuvaCUEOGLiEoJUSpmlBNNJJAsyYuIq83hzITWkpTVnzaPjxw4_qKXH8FQq9k8xtFax6sWhRdNR5rjSvdaT-6rnsyEqYy0yLCcKAEB_pgzkbjagcS-BbgtJIUcI6zBEQCPdh0OpiKiQ_qM-cz6QpObfqY6RcZ_h7NUUzisE8uIx6GbV8gUHPJsMjg51LTmwkxHK3EUY2HhH0Y1TQrNciXNZZExkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=bsGTgb-VjonhujFV78lpRXIyLvKPivX0uZ45lhdnlcz2Kh3v0iGOfrg74MR2BvD0NZQoQLHrn_CQd0tm3QvAlZTrsCSGbtLihT34I2qes46FyTuBFjdxR75qJBZCb1X6ERsafjFozm-nvy5xxhh6hfPdsMTxTg4I12t-tN75nuSQun7G5TiPdVIZu7-PTlsV1cocGQo8EJxAw-e5WivULM4d9nbjtezEIp3qbVFoG_csIdU3UxUt8BIKKsOR7rADxhKMmI5K-1d0GS7jiK07IMilnlTWCNdVhXboQCdvlbMHxBhF2hOx_uWqjaVoheixg4kNfPGI5MuDoVMh8ssOfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=bsGTgb-VjonhujFV78lpRXIyLvKPivX0uZ45lhdnlcz2Kh3v0iGOfrg74MR2BvD0NZQoQLHrn_CQd0tm3QvAlZTrsCSGbtLihT34I2qes46FyTuBFjdxR75qJBZCb1X6ERsafjFozm-nvy5xxhh6hfPdsMTxTg4I12t-tN75nuSQun7G5TiPdVIZu7-PTlsV1cocGQo8EJxAw-e5WivULM4d9nbjtezEIp3qbVFoG_csIdU3UxUt8BIKKsOR7rADxhKMmI5K-1d0GS7jiK07IMilnlTWCNdVhXboQCdvlbMHxBhF2hOx_uWqjaVoheixg4kNfPGI5MuDoVMh8ssOfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
