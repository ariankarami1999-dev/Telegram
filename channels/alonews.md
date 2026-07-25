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
<img src="https://cdn4.telesco.pe/file/iAxVfNDfbUhAPEbjiIMNtdLkwvqpQHsCe0S8vEat5uo-iijOSsuWHSiq4GvpfneEbRlmUFO7yGEftEiNAO_iR2XgfkdYB9ZPThUSwqJCEVLY4h0tXkvca3AuUU6J9hzoWvrayX6hDOZeeoilcw31Tw7I_m4h9k0FIJ8nGOZOdZFOjDaRv6QsdaW_ClIl_cBpinRveKR5B09GvVcGSIDljUzHuGwdGOQL-VSkwL5d-ilgxI3FgaAf-yVYQgLmynJySXAk6pAygGxPLEFHUqtJcWoyCCkAmBaKKvxU9CL0RILHTv8vowh2fo-XsHUcEMFF3x2vq84yxCI4ZbJZEdb3KA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 931K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 12:59:04</div>
<hr>

<div class="tg-post" id="msg-137436">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
دلار هم اکنون 190,750
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/alonews/137436" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137435">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
تمامی ادارات مازندران یکشنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/137435" target="_blank">📅 12:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137434">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyiqxri-QC3W-SlCz0RQEPrAOHxvh9Q-Y6yFfpMTo1NmP1HQ58xcbVYYyqV3FY94q5im3oVc12ow0PnyblnGI9ErjSRh5WXmN8irYXoH8e3vXoRhwf1CQn1YTg0rUnzyWNLi0rdIJl2EYspdhzoJyVP01khMg0s_h-D_yRTqozezj0T8InbWFHQs-3SZ3RfvXzOHMsvKFbOeUQ6SO2GOlctVbsQKqK9WxDZyEgmxz3j4bjkT0mgzSsoVJ_bhlmq69n1Hvmn7nMyht6vtDYRKMUL_xqfEDtVwCNTYFhnCLhtkUtXfFpwUv1I2gxphlmlK72idjOTvCxKN4hlXxF0Yrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش فرهیختگان از آخرین وضعیت ذخایر نفت آمریکا: کمترین میزان در ۴۳ سال گذشته است؛ یعنی پایین‌ترین سطح از سال۱۳۶۲
🔴
ذخایر استراتژیک نفت آمریکا در تیرماه ۱۴۰۵ به ۳۱۱.۴ میلیون بشکه سقوط کرده ‌است؛ پایین‌ترین سطح از بهار ۱۳۶۲
🔴
هم‌زمان، قیمت هر گالن بنزین به ۴ دلار رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/137434" target="_blank">📅 12:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137433">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH7hlyb_CgY79MNOcUcCzMdaSOhAV8lfeAeDROuIjhHwCaet9Kah1JxTSkHyhsFUqlU2fjbUwiIJJ9SBiuZxQh37WcTeWVgbnVwbZ9Eat4kHk3k-vNDJtuQ77P3qW0FUAuUUXH7KAm6IBI8QDZor5ie0beBupMua4ikpAGuVOekF0Ac93MDBG_-EGrrnYGWsV5NF0uiyw16hWKfedt1x22RZiSaoKGzB_-WCnd3uo73sVCa0pblqLC-ymijP3GkmjAqPZG617EKUO9PSAnddK2vq2PwZSk09PMksO9pCbdfwYB5E2Suw0EuwTkuySTmradXxoVqjNQ-CZFH-7SYv8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت فرانسه در تهران روز شنبه سوم مرداد ماه، گزارش‌ها درباره بسته شدن یا تخلیه این سفارتخانه را تکذیب کرد.
🔴
سفارت فرانسه در پیامی در شبکه اجتماعی ایکس با انتشار ویدیویی از نشست خبری سخنگوی وزارت امور خارجه فرانسه که گزارش‌های منتشرشده مبنی بر تخلیه سفارت پاریس در تهران را تکذیب می‌کرد، نوشت: «شایعات مبنی بر بسته شدن یا تخلیه سفارتمان در تهران را تکذیب می‌کنیم.»
🔴
خبرگزاری دولتی فارس روز پنجشنبه اول مرداد ماه اعلام کرده بود، فرانسه به دلیل نگرانی از افزایش تنش‌ها، دیپلمات‌های خود را از تهران خارج کرده و سفارت این کشور را تخلیه کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/137433" target="_blank">📅 12:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137431">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4TOt17j5yE1RP6QkStuB-es5oaNO0sooDYi1wTsKXRC6F4HdcQ6b0UCzAJ4srFwfHkMDhreAaLAyeFu4MERrhVKsOSKNBAhNlki6OOOtTeDXskGtuOuDYoHlDWrXtW4LTOugsAfNaButmES1dk7L0lIhNNDcJ7WEaxT7VX1fkOZkVupbXZRb5Dkt5qg14v7qjo3wlPk8rmtQqj-rpFVx-FcLb3P1UreE7c-ddnfCj29wizuEBJWUiY8gPiKZaa9mYFna5u-ol-x49RdF8xmGB1CEfPfXv-8LhUc8EczqSv12W6LiFCGPHaket-gs5-yCxXDIVXMf6qajzX3n5no9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1gV6hlFGDGFCwj0paKqyW4ICMPxSFiN6U4vfy_JhufRgyMUMYweWgsRnPIUpmueK1I07fgUsO4vU7eWdOv58IRgWFD-g0iuWB6s8N2zend2m17s43TwvOg5kCvMnBZlCOpQPf1b5VPszp7WiXWlhjOSWibPxP2M5gWM-xEMMoBwSnF9LpaQ58nx6R0kIQ6rUbhlGs1eH2p5C1tPIaCQMjqxopWuSngTEcE1vBnrSiOvExpYgzqgzO1WH8X8ybimOsYQ3NLw5X4j8j00AcXB0w8iLvwEl59oAwkQmG3hzTmo-uVNrO3mSwPbGSthxCHlzD2s51Y74PxYrxpmq_5F0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بعد از ایمان صفا؛ مهتاب ثروتی بازیگر، هم پیراهنی به یاد جاویدنام حمید مهدوی به تن کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/137431" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137430">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزارت بهداشت: شب گذشته حمله‌ای به کشور انجام نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/137430" target="_blank">📅 12:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137429">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgvtU7fE4UrIf-jbMpaVCvq3n1Nc6A7H41srAjkvhNE_bD4YhE-yQR9ehkgHG32iEN-F8s5riA9C99Ce2b9kbmHURqWr4Kx9Rjop1k4qUcZTEORdqUq87iUPevWTRRUuc7BrJ8ANfHuJTVKvAG8inWgWlAgMlXow8GSnDqEEierNsmhOfH7y_2MxyVnl43NlbuYwBpbuClEMcYytg6g04oyIByCQN0EN8afVW7A0L6ZFEsoRgZnOXI0SXqioiWc8KK4edMEtEmQf7ZCrY_4JnOfUtbDnWALfOVqMpAQaq7sa-ndncYnGQl1a2fC2hq4IkqpmG0sWr4PV1rVNgLz8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با رشد ۱۰ هزار واحدی به ۴ میلیون و ۸۹۴ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/137429" target="_blank">📅 12:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137428">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مشاور امنیت ملی کاخ سفید در دوران اوباما: توافق هسته‌ای آمریکا با عربستان می‌تواند مذاکرات با ایران را با چالش جدی روبه‌رو کند زیرا تهران چنین چیزی را نخواهد پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/137428" target="_blank">📅 12:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137427">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAwZI26yW25GRMjJQ3Buw9NS9GBXouVVtKmN_F-hvT5RiPst3KO4haqw2moeBRyke488YE5z1vPTyBZgMQbSfHRUuylplFs1Bbuf5rHS_w5kQ_1-O2Lq1VlV3u_pCmiY8Lhvtpx9HqqvIc6oHvz1noVjEdgOeTA5XoCdX6vo6j7FbcRgoffzhMhB-ID8HRTFyO0akr3P2NosCUQnWtLNprSzEKS1RGv0qbJwp8XWvu6knbwNLDqHGvi8Hql4Nr9Fq-w5aLjw7MhZaxQ1ftkA6zSbBGiOI5BCZtWsfs35DvvP3foxEbgDQyyAzEk2UWo7P200kIKU21xTSZhXR2DlZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) امروز اعلام کرد گزارشی از وقوع یک حادثه مرتبط با یک نفتکش و نیروهای نظامی در دریای عمان دریافت کرده است
🔴
این نهاد در اطلاعیه‌ای که در ایکس منتشر کرد، افزود مقامات از این حادثه مطلع هستند و تحقیقات مرتبط همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/137427" target="_blank">📅 12:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137426">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری / گزارش ها از هدف قرار گرفتن یک کشتی در سواحل عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/137426" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137422">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIuDJMUZUGbbDrr_UecvVPhDi7jhm-DPo1rC9j2NMljUKAuxxNmESMSGGNYLoXQbIN8Tc_FNmqzdYpxyBkTmo6Z-3B8B7i4qO5ZOF30UTBF7SO0SCy5mXau2rixOsemj8L3qzpmhSM2SjeoE50EVU37RpPqwCJywu3LwttaGzUBnvmQB8halQ-zke3I_T1n9b7q2WoRl7rXmoMGMgX0M0KuJwIGItNczLRGyXcgkV1BpAQgbEb07weA7SQ4Z_02UsWIFWpGwtvnCfEu3Fuyj_70HDEde58xJv1v5nr21n4eu4zSjZFuYHwE2ZJRlWtPYvMYqdBOVyTADl9KIcCg7qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFqmRZb-u3jSxCqyDwDEW6LwV9XOeWrrqeaeh3352V0hb_P0I7ctSqL-EZjkeWF5aqL0Z64X941RscP_CR5z09Y6XLU3i5735pZPCCLAyiPTKmnujnN_2ST3l24RT-LBRap9y1rFjan7UJ_04bbYMrGs5bOnjHAm-xhDB_hnm1FlnRXcIerEWi39OeJjiqWzw5qqT_Wl3rbEzTBMKWUHVdsrlBKH9mz-1h4FLgU3oWosZaVCxAMbDSWMrYvJ3g8W8YLaTxJtzHJhnlYOKxF9Ft8Y5uBjA-M6XBZk4xFeXGFlVDueM8qG514g3716Ebc2Qu14ap3SYBUtbkt2_NA3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZXHVdzYE2MuWli0cXydPOUZc5MIbUE5bivS0HjwJeSRKF6ZsexAzauIpJB-AhVaPi5MO9vS9qYEHiyz1IXxgs2bcAkcPBYW_Zg866HiRyHaJhn6GElGaFYugSMkuZYWt1-V9kQ6rwHvRpGDEsoKKPgnhoO6GBmRxc6m1gyw3-_6hfSCbw8-VRmOApqo4CqdVNBvQyic05GhTLYvapU6MB3q0z6FDB7cbvI62k72JhNcbB_zEEwUaV_Qj3gGmeWWpGeUDsmXA9CAyFoI3OURSq4Sc1DO74I4fGI7weYfo3x-AkVxA-BAMXqvW-nm80S_v-jZe9xqC716qZFMNX3NUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da4780fd8.mp4?token=uf-tTTbK4DbKrjfOQluyWgA1LgWGzxXyw1LizJEyeHH84w2T3vo281G9RPDCgs8vIDVl47f9mT4n_qHGruSxhtvQcBxhk4Tg9S5BkCWNOhuSPi0TSXClCj_NeZqXTB_kCu2HEC9W02WL2holvywSYvQQKSAxoNjBGhxZDef1_d3rrV9sxhZ3B7aCZ6cIhnWsEs_EI5CmeioPjvOhKcr9IP3AGiI-j1TLcN-0XaWRjp_npxmbyr0o0il5IHEV2_3yJTnNFqG9cyYXx7JXBDO7TM8wcfDNwiKy8CSqn6DTjQTTRlf211qTOify1g0h7CBiFprnd-oFx38_HfyCXqeWkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da4780fd8.mp4?token=uf-tTTbK4DbKrjfOQluyWgA1LgWGzxXyw1LizJEyeHH84w2T3vo281G9RPDCgs8vIDVl47f9mT4n_qHGruSxhtvQcBxhk4Tg9S5BkCWNOhuSPi0TSXClCj_NeZqXTB_kCu2HEC9W02WL2holvywSYvQQKSAxoNjBGhxZDef1_d3rrV9sxhZ3B7aCZ6cIhnWsEs_EI5CmeioPjvOhKcr9IP3AGiI-j1TLcN-0XaWRjp_npxmbyr0o0il5IHEV2_3yJTnNFqG9cyYXx7JXBDO7TM8wcfDNwiKy8CSqn6DTjQTTRlf211qTOify1g0h7CBiFprnd-oFx38_HfyCXqeWkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تأسیسات نفتی تو استان تومِن روسیه، هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/137422" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137421">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رویترز: سامانه پدافندی یونان که در عربستان مستقر شده بود، توانست دو موشک بالستیک پرتاب شده از یمن را رهگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/137421" target="_blank">📅 12:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137420">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی هیأت رئیسه مجلس از ارجاع ۱۲ طرح راهبردی تنگه هرمز به کمیسیون امنیت ملی مجلس خبرداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/137420" target="_blank">📅 12:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137419">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANHJOp5diAotLQO4C48JtazgngvuXS5UUo_k_QOgrCtr6yq90UvGT0EgONleLPfFVPmON5It6dgBtGmOet9BoRlVgKD8yNU8IhWsJ4buzVCvJM2z3NVhJ_qXXcwGLyrcDKdhVawJWJ8mG7ZKM5m8-2Q_0gFxcwK-sYZXIu7P9BV8upllbniz0THiS-z3BxZ4IDwWV-mZs06ANxwLQG4czkzEDzGSX_ZmCb9Z2zP0mX4B9PAK-iCY7WZ_zAkcatVBPosfHX-GPjqsDMe4hb6YAqqfpTSm9jiUKcN35mrZVkmh_U5V92bJjcmSGCqTEaTvT1nvDYp7EqV-R5c_UU_pmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیم ایل سانگ رهبر پیشین کره شمالی که با وجود علف خاری و بدبختی ملتش پروژه اتمی را پیش برد و تمام ثروت کشور را صرف آن کرد و سپس پسرش کیم جونگ ایل بمب اتم را ساخت و کره شمالی به یک کشور بدبخت تبدیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137419" target="_blank">📅 12:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137417">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSFNZFWA7ihgaTArurNkGJR0pUDvHG32dSlSj7Xn-eh1rqKb5946g-TaRsQCvYadj9r107_G0X5vscdd5uEQF1lXfFKRepirFL3IPmE92m57SjhqNU0_r0KjWgJQFqHeRHOcVG8_Lnj0mPP6lkp2P5k1-Jmd0mBK0pPuTUr1RaYRjo2mBTYBdaFqvt3QetzbNc2vshFdpDYE0LDpFjErtWXrdlWqx4oPScnsERL_mtdmE9naxLIbDE5YIDKCaDYJFnRlcjFx9T4YZVHFlb9MtCleRVqWtgcSfchHUkYnQEr6o2dupT0zqlL5DsAbt_eIcubxn5d2B17JRHVpy251hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9zDYUGo5wM_W90YYwED2w9ZElE793BqFQRXkKL1J6gwYrkjueOQFQUOSpGOUR6jTxM0Ct00G0C_ehG-ox_PKAtFZC5yeapw1QJINstHyFAksjhQE2iSg4ieuI4VjEDL45ntvWoUEhR9DttFYKs6N6ETukVu8L3DSq1Ht3GH2u_X6iYN82ahNW_vPt_SKemadqT89luSC3VCoJG_Z5dmE6UfcRD8rz1ZLI82p7nh5hfX49iz-dNBnDRXJe1J91M7qsQHqFy5wkdjjP5TnHQ_Uav0fzVEvzteZEq3OOCFUM8tvGtq3hCdrzkeagRj91aC8ZjDeMFomLgA3IqOHbf3Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک هواپیمای سعودی که برای سوخت‌رسانی در آسمان یمن پرواز می‌کرد، پس از شلیک موشک‌هایی از سوی نیروهای یمنی به سمت آن، از حریم هوایی یمن دور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/137417" target="_blank">📅 12:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137416">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162e46ebc4.mp4?token=SqOxBDaArMKJvvENl4fkHGKQ9AqMkJYcrzgTeuMMZ5RWkBQzlDIyGFZtFR7Rg25ucx8JyokksNpOVMrhtbS32A5O40h-iFn7hUaE97KysBrkXS3_3zumDGKMUn07EqNqFyza8yp9aoG3XDzOmICRuzaV0un4rUvHevhoUiEj34ASjL5Z5JemAIdUyexNdqdIESZf2aph6i3qyAZmwu2h49XOM3QB2j7cSyRwKDpBhglFZGA0EJP09aCzlKGTMNWscpWADoBFrkUV0tHAkvyA8GMb9W_26RkdoKHDsOfQqMEBT9d8B8Ng0qT3f8UJQXnP0xwcNPxleh4GuRmAcBH9Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162e46ebc4.mp4?token=SqOxBDaArMKJvvENl4fkHGKQ9AqMkJYcrzgTeuMMZ5RWkBQzlDIyGFZtFR7Rg25ucx8JyokksNpOVMrhtbS32A5O40h-iFn7hUaE97KysBrkXS3_3zumDGKMUn07EqNqFyza8yp9aoG3XDzOmICRuzaV0un4rUvHevhoUiEj34ASjL5Z5JemAIdUyexNdqdIESZf2aph6i3qyAZmwu2h49XOM3QB2j7cSyRwKDpBhglFZGA0EJP09aCzlKGTMNWscpWADoBFrkUV0tHAkvyA8GMb9W_26RkdoKHDsOfQqMEBT9d8B8Ng0qT3f8UJQXnP0xwcNPxleh4GuRmAcBH9Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آبفشان چابهار با وزش بادهای موسمی اقیانوس هند و بالا آمدن سطح آب دریا، حدود سه ماه فعال می‌شود و از نیمه شهریور دیگر این جاذبه طبیعی قابل مشاهده نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/137416" target="_blank">📅 11:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تماس تلفنی وزیر خارجه مصر با عراقچی و البوسعیدی
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/137415" target="_blank">📅 11:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137413">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oB52eIqWik-C_7CevxGfGmDZYWa01MdMA-87KvKyQUPNL5KVUGvvy00HHypabUoOHkrqwJC4Mgk39Iz1CAmaDLW1sTBLW7EENPQpYDOs9pUbNL3b127ysqau8dHuhq4OceEADN_VEEai_JBmp6FaIWlQNZhVB06cINZFeLL2AgA7FR8xSHPZg4XPNjjPS5OXKct8SG9COyM7tH6q6SJ-lBGhDM1SGxylBQdm3x3BsJuMh4vTwXWVTgTOLTbXBCdwMw7qP2u1pzI-cwYnfuLEIwj0kQNG59-sCu5YaoAe5eqjNOAffV5E_S6tmcqNqAPDC61ZycKgVJeDmbU-C99Nbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qwsv6LMUH8-ZigOEcEUVTJ7TCbgPPV9xukougT2w478ebs56Vqp-Bt7NL7nqEk38PQLjcBYFUHZfeZeBjiv4lcoNVfkzYOHkKE2PBiJRmX193QjyDyaZYtY1OM0ZLQcppcOVtNtVfgtpCSAFtb2aF6GkLZWO-DG5AFVw2JGZBMH8fNK4_m3c2mPOFKVzFgpjJVZke-ACndK4Lo5niQu9i3_Qt5rsNVi1E9gDpj0G1hP6pPf_apFGluI8IFfKwD873YDqoOs4ODUs8-UA6IybMad4mIpbh_VaFBvjC3Zzf13JpdRBNvm2wTWp-JTWdnn6oPHGDU2O-MYiRwkqs91VKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اوکراین بار دیگر انبارهای شرکت لجستیکی وایلدبریز (Wildberries)، بزرگ‌ترین فروشگاه اینترنتی روسیه که به «آمازون روسیه» شهرت دارد، را هدف حمله پهپادی قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137413" target="_blank">📅 11:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137412">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وال استریت ژورنال: کویت و بحرین با پشتیبانی امارات به ایران حمله کردند
🔴
وال‌استریت ژورنال به نقل از منابع آگاه گزارش داد جنگنده‌های کویتی و بحرینی اوایل ماه جاری با پشتیبانی دفاعی و اطلاعاتی امارات، حملاتی علیه سایت‌های ذخیره موشک و پهپاد سپاه پاسداران انجام دادند. امارات نیز پوشش هوایی دفاعی فراهم کرد.
🔴
یک منبع در همین گزارش ادعا کرده عربستان سعودی در حال بررسی پیوستن یا عدم پیوستن به جنگ علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/137412" target="_blank">📅 11:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137411">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
زلنسکی: حاضرم در آمریکا توافق صلح با روسیه را امضا کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137411" target="_blank">📅 11:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137410">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d41997f2d5.mp4?token=Vrc9dT9dVRRgOWH2F7JRjUd1qs39WgmV-32fQhH1ofmuhdMzZZEJOu06PTtB4iNkk3mndpPZMxfaTela7J1pLWltzb-tY7r1cdpegvEQ3nUrH5cNK5G0iCP3BqPjrQDXtZ6wiqf6K4K59BMQQyaYewUkMAeLW39oPVlWu89T-NN4ygsXYUEoz0BH7S3KjY-vtGiBElPfcO06IyhlyNlULnMoH7TrWjOJQoHi4kle1k2YuwTxFiPOvtjPB41u5SzQTOuH9-zqQGFlqbaWhjYu57756c874OpZNA9Za50zY0pfU1r7OWuUvmRBO8EfzW-FkmlHs2cAxy4laeSs2U1qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d41997f2d5.mp4?token=Vrc9dT9dVRRgOWH2F7JRjUd1qs39WgmV-32fQhH1ofmuhdMzZZEJOu06PTtB4iNkk3mndpPZMxfaTela7J1pLWltzb-tY7r1cdpegvEQ3nUrH5cNK5G0iCP3BqPjrQDXtZ6wiqf6K4K59BMQQyaYewUkMAeLW39oPVlWu89T-NN4ygsXYUEoz0BH7S3KjY-vtGiBElPfcO06IyhlyNlULnMoH7TrWjOJQoHi4kle1k2YuwTxFiPOvtjPB41u5SzQTOuH9-zqQGFlqbaWhjYu57756c874OpZNA9Za50zY0pfU1r7OWuUvmRBO8EfzW-FkmlHs2cAxy4laeSs2U1qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد صاعقه با موشک چینی در حین پرتاب
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/137410" target="_blank">📅 11:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137409">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFvfHEoou6SK7mR2B7889du-xsQOeM4BQFMdBwhVmI8Kl3tEMQROAy5J6-CE4OH6jd-ZZrnJaug4qkkOcGjPTXz0eyHfYThWK3rNIaFe0CMsw3zSam3YACRogc_gUmXBRB9Uyr-qlW1m6lhQ9I962i94ApEhikJH0cwdY2CDRSTojfG4TDTAFdKw2PnLARfjx50nxByPON7ZppPH35P_GSG0hUruR8nXLoyvC8YCkPf8dWADZmGa1glLq1E7C3Op6oPEsirgmoN1wSjau8mE-dWvl2hG_KXScAzd8DP-LiRDv4zi_zOXsg5Jwuykd8lmZ_e4MYDG2nF-Ly-6XmTPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهریاری، گوینده جمله تنگه ارث مامان ثابتی:
متوهم ها باید قبول کنن‌که آمریکا ابرقدرته و حریفش نمیشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/137409" target="_blank">📅 11:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137408">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
اتحادیه اروپا به درخواست دولت امریکا پذیرفته است تصاویر ماهواره‌ای این برنامه را که منطقه خلیج فارس، از جمله دریای عمان و مسیرهای کشتیرانی منتهی به تنگه هرمز را پوشش می‌دهند، با ۲۴ ساعت تاخیر منتشر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/137408" target="_blank">📅 11:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137407">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مشاور مالی نخست‌وزیر عراق، مظهر محمد صالح، تخمین زد که جنگ ایران بین ۴۰ تا ۴۵ میلیارد دلار برای عراق هزینه داشته است که ناشی از کاهش شدید صادرات نفت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/137407" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137406">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK9aL7xTbwq0KyNUsrxDchK9HW8eQM3gXR4McbrGlIuKtE0eT5B0_0FkEQbxAMaRvHO9U0AQdWX51ETWWU4b9T9iLeJ3yA5RgoAOEenpdNH2oHVRHc_uaClR9X57W8y9HsJUs9VSUyC-V5TnJO6zi8QGX5XrJOnH1umc8BU42ly3eddoWCcPunbyF9ciKnwb4dCipwdFh3v_TMRhiuqFAQa5IcF1PrCdVM48EdEOtp9UVqzSYu5r4mW10PGDRGOOvRA3L5lLc2SPWx1vF3PLpT9Z4aQrpcgmtX0S79TNE44-OZewNeV4GxnKPEDEazL3tXppnBa6QVJC5SysnLk3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی: توافق قطعی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137406" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137405">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/137405" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137404">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزارت دفاع یمن اعلام کرد که پدافند هوایی این کشور با شلیک به سمت جنگنده‌های عربستان سعودی مانع از ورودشان به آسمان یمن شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137404" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137403">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شبکه سی‌ان‌ان: پس از ۱۳ شب حملات متوالی آمریکا علیه ایران، فرماندهی مرکزی ایالات متحده (سنتکام) روز جمعه هیچ اطلاعیه‌ای مبنی بر انجام حمله جدید منتشر نکرده است.
🔴
هنوز مشخص نیست این موضوع به معنای توقف عملیات نظامی است یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137403" target="_blank">📅 11:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137402">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رویترز: برای اولین بار در دو هفته گذشته، نیروهای آمریکایی از یک دور جدید از حملات روزانه علیه ایران خبر منتشر نکردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137402" target="_blank">📅 11:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137401">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
به گفته برخی منابع ترکیه در حال ارسال تجهیزات نظامی به حکومت جولانی برای حمله به حزب الله است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/137401" target="_blank">📅 11:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137400">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در شهرستان ری
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/137400" target="_blank">📅 11:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137399">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
بلومبرگ: عربستان سعودی در تلاش است تا یک راه حل جایگزین پیدا کند، در صورتی که حوثی‌ها مسیر باب المندب را مسدود کنند.
🔴
طراحی یک مسیر جایگزین جدید که از تنگه باب المندب در جنوب دریای سرخ عبور نکند، یک کار دشوار خواهد بود. این امر مستلزم استفاده از یک یا دو خط لوله اضافی، تعداد زیادی نفتکش و همچنین تلاش‌های دیپلماتیک پنهانی در خاورمیانه برای حفظ جریان امور، علی‌رغم تهدیدات موشک‌ها و پهپادها خواهد بود. این کار نه آسان و نه ارزان خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137399" target="_blank">📅 11:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137398">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlUzoXS74IYTiixyBv85IO309-DO--cxDk1dulItCcpnyxgi9mH_yMQ9c0R8nq6w_t1O4iRU0K9RCzeVttEreazBmcqklBrOq5HGosaxdLuM6t-6X8joZlwMTWYPwRU2M-JM5bUJIgx2MfbNOPPJPFtozxDbqVVGEfLvimz4b8XsAx0I5a6qqkabjL3N8s3_5P78v1xhbAbFWCYhzJbgNSP_WFAaP8TBC5N_jiYY8aXEVMULH1QLuWSR5uzu4Pl7IPq_spZGX8cr9nET-44OnsWUjLcVfp_C3hwNwocXFtrG1rOlRIOFUyxEX4EmlsfnEZ66ont6QOBhIV1s4-kPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری اینفانتینو رئیس فیفا، برای تولد مهدی مهدوی‌کیا:  «صمیمانه‌ترین تبریک تولد را به یکی از بزرگان فوتبال آسیا و جهان، مهدی مهدوی‌کیا، تقدیم می‌کنم. دوران درخشان بازی تو در سطح باشگاهی و ملی، به‌ویژه نمایش فراموش‌نشدنی‌ات در جام جهانی ۱۹۹۸، هرگز از یادها نخواهد رفت.»
@AloSport</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137398" target="_blank">📅 11:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137397">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / آکسیوس: آمریکا و بریتانیا در تدارک نشستی برای تشکیل ائتلاف دریایی در تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/137397" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137396">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
مدیرعامل شرکت توانیر: از ساعت ۱۰ صبح امروز (سوم مردادماه) برق تمامی صنایع دارای حتی یک دستگاه رمزارز غیرمجاز به مدت یک هفته قطع خواهد شد.
🔴
تاکنون نزدیک به ۴۰۰ واحد صنعتی مشمول این مصوبه شناسایی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137396" target="_blank">📅 11:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137395">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
شرط واشنگتن برای فروش F-۳۵ به آنکارا
🔴
سازمان‌هایی که در ترکیه فعالیت می‌کنند از طریق شبکه‌های مالی و صرافی‌های ثبت‌نشده و فاقد مجوز، برای جنبش حماس پول ارسال می‌کنند.
🔴
این سند همچنین آنکارا را مسئول تداوم این وضعیت می‌داند و تأکید می‌کند که فروش جنگنده‌های اف۳۵ به ترکیه بدون برآورده شدن پیش‌شرط‌های لازم امکان‌پذیر نخواهد بود.
🔴
ترکیه باید تضمین دهد که در آینده سامانه‌های اس۴۰۰ یا تجهیزات مشابه را خریداری نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137395" target="_blank">📅 10:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137394">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
استانداری اصفهان: احتمال شنیدن صدای انفجار در اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137394" target="_blank">📅 10:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137393">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
هاآرتص: تل آویو می‌خواهد تهران را به حمله پیش‌دستانه علیه اسرائیل سوق دهند و در نتیجه برای پاسخ اسرائیل، مشروعیت بین‌المللی فراهم شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137393" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137392">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2e0a325d.mp4?token=DzRzHVzrunNmvvjAUqRFXSoSab_ms3g-03n2rxLSQckpZ7k3LPlKC5Ggx73jo_CcZ4a_ojmfXhngxCnNimA17kaIz0nuXDkeqXNEezH5HZ0TeV6oJO-xIt86IUvYDLuhxM9kTtgstDAqw8t62NhFgdseBGdq7fBIztDj565_Soi_Up8PggsJWp6I2o5PFArqSeKcBGCffMFbl4owabFZdJQUVEDGAP-euLyPELryQJkCjA6zEJEtjpGqBVlvSb-UZ1edcBwjBr_otAWq1EiHT-g-_hidyWsi-y8STfHVm1aaZx8zID4AAc_pPS4LmIxtlAfXfAqBJnj7dsBYSmfpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2e0a325d.mp4?token=DzRzHVzrunNmvvjAUqRFXSoSab_ms3g-03n2rxLSQckpZ7k3LPlKC5Ggx73jo_CcZ4a_ojmfXhngxCnNimA17kaIz0nuXDkeqXNEezH5HZ0TeV6oJO-xIt86IUvYDLuhxM9kTtgstDAqw8t62NhFgdseBGdq7fBIztDj565_Soi_Up8PggsJWp6I2o5PFArqSeKcBGCffMFbl4owabFZdJQUVEDGAP-euLyPELryQJkCjA6zEJEtjpGqBVlvSb-UZ1edcBwjBr_otAWq1EiHT-g-_hidyWsi-y8STfHVm1aaZx8zID4AAc_pPS4LmIxtlAfXfAqBJnj7dsBYSmfpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کتک کاری پسرها بر سر دختر در یک ایونت ورزشی در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137392" target="_blank">📅 10:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137390">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزیر امور خارجه: آمریکا می توانست از طریق گفت‌وگو ابهامات بند 5 تفاهمنامه درباره تنگه هرمز را برطرف کند اما راه دیگری را انتخاب کرد
🔴
استفاده از مسیر جنوبی، حدود ۱۰ روز پس از بازگشایی تنگه آغاز شد. از نظر ما این اقدام واقعاً مغرضانه بود.
🔴
آنها می‌توانستند اجازه دهند مفاد بند ۵ روند طبیعی خود را طی کند و سپس در پایان مهلت تعیین‌شده، ارزیابی کنند که آیا شرایط به‌صورت منظم و مطابق توافق پیش رفته است یا خیر.
🔴
اما آنچه برای ما روشن شد، این بود که موضوع فراتر از یک سوءتفاهم است. به نظر می‌رسید آنها اصرار داشتند که در کنار مسیری که ایران برای تأمین عبور و مرور ایمن و آزاد تعیین کرده بود، مسیرهای دیگری نیز ایجاد کنند.
🔴
آمریکایی‌ها کشتی‌ها را از مسیر تعیین‌شده از سوی ایران دور می‌کردند و در عمل آنها را به استفاده از مسیر دیگری هدایت می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137390" target="_blank">📅 10:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137389">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f61992002.mp4?token=XlEFNcZmwEhTzJfnrnCKUZiNVieNspGYr5gjswzcXyJpxlAFla1jdxreO_1skoaZ-SG8-RHopKgcM5qMprOFAZu5wPJEnMu_3cwtAHe5_hMKsklF5ibp5DPJgGfrmc6h-ed_w2I38h78A5y52vim96yCCr2hvuo2Z31Glt-PHTRIPJ9B2i8sumiv5Na27gzAiE6djLQwxv9JgdxGx0F9KEPg6Has1pLuUEvYRT3-wVdt7fJOuntHbx2Z15PIgQqwkhx_bTRJXh9fcY9cYAAdL1ytKCRgCrSM2_Vhld9j4nJodVO_V4hYaED6ZtX1IeLPfX967CNtK1pjtw4ACAKOyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f61992002.mp4?token=XlEFNcZmwEhTzJfnrnCKUZiNVieNspGYr5gjswzcXyJpxlAFla1jdxreO_1skoaZ-SG8-RHopKgcM5qMprOFAZu5wPJEnMu_3cwtAHe5_hMKsklF5ibp5DPJgGfrmc6h-ed_w2I38h78A5y52vim96yCCr2hvuo2Z31Glt-PHTRIPJ9B2i8sumiv5Na27gzAiE6djLQwxv9JgdxGx0F9KEPg6Has1pLuUEvYRT3-wVdt7fJOuntHbx2Z15PIgQqwkhx_bTRJXh9fcY9cYAAdL1ytKCRgCrSM2_Vhld9j4nJodVO_V4hYaED6ZtX1IeLPfX967CNtK1pjtw4ACAKOyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روی آنتن زنده، مشاور قالیباف و الله کرم، نماینده جبهه پایداری دعواشون شد.
🔴
الله کرم: شما مذاکره کردین که هسته‌ای رو بدین بره، من به عنوان نماینده مردم نمیذارم.
🔴
مشاور قالیباف: تو خر کی باشی نذاری؟
اصلا کی گفته ما قراره هسته‌ای رو بدیم بره؟ شما میخواستین قالیباف رئیس مجلس نشه ولی شد.
🔴
الله کرم: نذار بگم قالیباف چطوری رئیس مجلس شد !
🔴
مشاور قالیباف: سیکتیر بابا
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137389" target="_blank">📅 10:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137388">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
اوکراین: حداقل ۱۵ نفر در حملات روسیه کشته شدند
🔴
در ادامه جنگ روسیه و اوکراین، رسانه‌ها از کشته شدن حداقل ۱۵ اوکراینی در حملات به کی‌یف و دیگر نقاط این کشور خبر دادند.
🔴
ولودیمیر زلنسکی گفت که در حمله روسیه به یک نمایشگاه دفاعی در کی‌یف حدود ۱۰۰ نفر هم زخمی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/137388" target="_blank">📅 10:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137387">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ایلان ماسک: تا ۱۰ سال دیگر هوش مصنوعی از کنترل انسان خارج می‌شود و کنترل آن دیگر در اختیار بشر نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137387" target="_blank">📅 10:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137386">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
بلومبرگ: کویت با وجود حملات روزانه ایران، یک همکاری زیرساختی ۱۶ میلیارد دلاری با بلک‌استون، بروکفیلد و KKR در زمینه خطوط لوله صادرات نفت خود به امضا رسانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137386" target="_blank">📅 10:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137385">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsraDnT-tM_QuotEhQzwV8D7vR5rvxL5BWrN4UPMCMs3nUII50ndclHRJcHp-XpvJlPcL8ZYq2d-qyLKOWVThKdrQ9uoxeZn8MY-dtiKUe86tqbAI5C7r8o1kp18ZCzartQjykVYf7vDnr4ID6TSHP_GgB5XHv-4NxOP9F3Ldt589mNMG3g3RxY8T1tArp_uNvUvTOfn1eZPKHo64ZEhSjK2-LFvrPlKi4l2UOhyQaP3FYU2H_krsCvG2BUByUL3U5eKR9SyM4EjJL0QtGH5OATG-UFnr-ygxPdumP_vqycrcauTO2SVY3lqecK2j8ymT2fj6Wb9WH-_8Kau8Ff81w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص بورس کانال ۴.۹ میلیون واحد را پس گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137385" target="_blank">📅 09:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137384">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
پایگاه‌های ردیابی پرواز از به هم ریختگی در جریان پروازها و عدم امکان فرود تعدادی از هواپیماها در فرودگاه‌های جنوب عربستان خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/137384" target="_blank">📅 09:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137383">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137383" target="_blank">📅 09:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137382">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeLCL-jbpHJ2AlDz7D317fo4nAhOJz20rXQPvlHdORoWiuc3D40g799y0LKPE-y7rf5zvkhjDAJjshH9yIXt8iMktU2mM94PJpdqEmmvg7sMFvA3Z95tRyQY0tNiGYPgtXg4pflPnobNEnVSe6skmCNE2YqNsOvCl4WtdKCCcGh39fP2RCOz0z2irbiizN9Z-1CptI_phzX8QxkzNKg3X96oOMUysgIr9SNcEaPaP076qPHP9rEAyO9Xe0Rl0s0mTtCrNAWXqC4aufwwxNAKfWEvrnjy7dNr892YmzkQKwRQEX2bO9gPPPhWpdZLeEHONbq91585mdmkqGzHmhul8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تأسیسات نفتی در جیزان همچنان در آتش می سوزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137382" target="_blank">📅 09:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137381">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گاردین: ایران توانسته توانایی خود در حملات را از طریق پیشرفت فنی در برنامه موشکی و بهره‌گیری از تصاویر ماهواره‌ای، تقویت کند
🔴
شواهد نشان نمی‌دهد که تهران در این مورد از پشتیبانی اطلاعاتی خارجی استفاده کرده باشد
🔴
از برجسته‌ترین روش‌های ایران، استفاده ابتدایی از پهپاد‌ها با هدف خسته کردن پدافند هوایی ، پیش از حمله اصلی است؛ این موضوع شاید نتیجه تبادل تجارب نظامی با روسیه باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137381" target="_blank">📅 09:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137380">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137380" target="_blank">📅 09:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137379">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ:  کارها در ایران فوق‌العاده پیش می‌رود. اخبار جعلی را باور نکنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137379" target="_blank">📅 09:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137378">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRvJbcADHT-KXuxLvPnSu-QPWYObq_qa8q1G4Hsc4r6dI58g-7Sq64-LBIdo7PCtya-thu-WXuIS2Ydwot6h1Eyp-I9ILORkbZln5-UycDULoo01z7uFFZZNIlrRuRIHo9AiXAukQV49-iOOGeX8cpYiV8OTLYCn7jn1-vxSyOsYtYowg8UrRapayDjwTTyC09_ou7yUOYRQvZ3q2CVASE4g0uVMI5G-964aH0bc6IuS9sFA_J2fPQ-6OcZmstE8CIBiUch8wgV2P694pTPUwRLLTF1_vqCUhE8Obd75wF_LfYtSoaoXCFlt6GyPF_lud70iXdj_1APEmys1oSjt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ازدحام بی‌سابقه در جایگاه‌های سوخت عربستان پس از حملات موشکی یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137378" target="_blank">📅 09:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137377">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
دونالد ترامپ: "دوباره این کار را انجام خواهم داد. باید آسان باشد. من واقعاً در نامزد شدن برای ریاست‌جمهوری خیلی خوب شده‌ام. سه بار پیروز شدم. بار دوم انتخابات دستکاری شده بود."
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137377" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137376">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: کایا کالاس(مسئول سیاست خارجی اتحادیه اروپا) از نگرانی‌های حقوق بشری حرف می‌زند، اما در برابر جنایات و حملات علیه ایران سکوت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137376" target="_blank">📅 09:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137373">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a61b348325.mp4?token=lEm3QnWgx8f6qqj7P_VwGgCtipVOYFojLH5KOqTCAJwC5-nCo5sTXL-IjEV5KxTcv5fFN03phOxQjbwBV3ZnsxPf2KHMjzKswcbVOR2XAbxu1_MHBcmcEfcsNvpWxRlyhsLc3Xsb8oD4YYs2PNChUrQQnnlInen-OQNRSsfyllQMFod2Iac3p0uSl_EjQLFWf79glnG7HUtY8I16Ps1oc5bKFTd9Gc6NAHcraQpeEPZh7iZVMASwuZ-VRE58m0rY34IeY0JHYt1sMssynuZc4fa_OjeLTUV-Ej36eweFejUjnl_eY_rPrRWYF4bs1SxOtv1xfsSVGotxclwvRJQXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a61b348325.mp4?token=lEm3QnWgx8f6qqj7P_VwGgCtipVOYFojLH5KOqTCAJwC5-nCo5sTXL-IjEV5KxTcv5fFN03phOxQjbwBV3ZnsxPf2KHMjzKswcbVOR2XAbxu1_MHBcmcEfcsNvpWxRlyhsLc3Xsb8oD4YYs2PNChUrQQnnlInen-OQNRSsfyllQMFod2Iac3p0uSl_EjQLFWf79glnG7HUtY8I16Ps1oc5bKFTd9Gc6NAHcraQpeEPZh7iZVMASwuZ-VRE58m0rY34IeY0JHYt1sMssynuZc4fa_OjeLTUV-Ej36eweFejUjnl_eY_rPrRWYF4bs1SxOtv1xfsSVGotxclwvRJQXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات سنگین شب گذشته پهپادهای اوکراینی به شهر روستوف روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137373" target="_blank">📅 09:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137372">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO_UdhMgmZpzvgKPtpUx-N6dOyt9qsaodgdI4GK31jT0OgBF_5LpBvxZzIS5Z4IeIIHqzGjCZMWrr4Nj5me36Yh9O4M95MGRqKxbZKe1XSJLhb0gOrp_cPHFm5MkpaU4Ir9ygrGKSTUznrSy2t0pHzWl9BjBss_RIHyjI3r9Dzk1WRtJ4n4nNqRmzcXFKSRiZDcS_6gavpRSK9UC-0Mpp4JmyuhpqdpOPLhCdriuRSONfoY2ZC7XI8o2AfOkNDl3u2IgpH5KNBNzaxosAs-7vUS88DuuVGyB7CoLJ-8oQfaNiVbDFtk9a5WQj7SDUZfyE4LqhYE7YKhvrjD8BDRmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت و WTI به ترتیب با ثبت اعداد ۹۶.۷ و ۸۹.۳ دلار بر بشکه وارد تعطیلات آخر هفته میلادی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/137372" target="_blank">📅 09:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137371">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxB3oOkuaxXvmyfKGrgRHMh3gSsBq4DiLfYZDT4xIHuyu0we2aNn2jg6rar-VqaJjMvWpG7p4owG8oBKHcnSDC3ueeRnuSYWB2ozU1jfvTUUXo_m0Gtc_68v6DY0GkTHlKP75ubgzSJRrv8-c4XBsFp28JEE_zWyLoZVDpJiIiJCsDDeYzMZa4eLqWtjs8aWdJmhmsyKaN9n-Zz7c3imnkk4AWEFwqQtgoLyOO7PIWajbiCjLJhZGX7wJALUWVwK173J2wQhQGTACZdjLzrGfQ5230ySIKGGYSykMv6ICV1R1k_suqC_iLvkOG75Lbl6Re6uomSCyUzW9_579L5Tlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای تایید می‌کنند که آتش‌سوزی در پالایشگاه نفت واقع در جازان، در نتیجه حملات یمن، رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137371" target="_blank">📅 08:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137367">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d2b02766.mp4?token=tyzg0503uEn6_5mY-Kj9BP8ezHBRX5kBtYNN9o52sD9O5Fw-jBprx86cwfzIW1CHuurhD-Uds3-qzI7y3i6UEej0Tz83QP2wqz2hW25TJHae56ng8JncnJDHsiSAF9kYCt2XIE2G-6Ba8GE7CNlcWpIz-b42gXjilikKffLdh5ux2lDQVF9N_I9pQlGIwQVKL6_uXQk87Nm9-IpHbpTbT4deFecPuCHS5moCbqKtzAi8JM0V7DABAW2CpFV-Yrn_DlgrgjaFhE8ZMzp_Z9PPukIHCUO3HZG-_wLeDDFD3eP6aVCnZi8KB1dE3--HXQKMzDQWFeuUlSbssRp4DcHkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d2b02766.mp4?token=tyzg0503uEn6_5mY-Kj9BP8ezHBRX5kBtYNN9o52sD9O5Fw-jBprx86cwfzIW1CHuurhD-Uds3-qzI7y3i6UEej0Tz83QP2wqz2hW25TJHae56ng8JncnJDHsiSAF9kYCt2XIE2G-6Ba8GE7CNlcWpIz-b42gXjilikKffLdh5ux2lDQVF9N_I9pQlGIwQVKL6_uXQk87Nm9-IpHbpTbT4deFecPuCHS5moCbqKtzAi8JM0V7DABAW2CpFV-Yrn_DlgrgjaFhE8ZMzp_Z9PPukIHCUO3HZG-_wLeDDFD3eP6aVCnZi8KB1dE3--HXQKMzDQWFeuUlSbssRp4DcHkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله یمن به تاسیسات نفتی عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137367" target="_blank">📅 08:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137366">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTgGkRDBuLyxetuq5laD1XaEL4bTFh7eCI1cB1_0POez7meckMqzeOe_gZg9c6iDNgHxG755DPVfRG5hyuBkjjKaA1mfrHi2e5H5Zqlb1piQSgnAHkwB37Embt7sPMawC7BLqq6xItzt_4LLeSH_hoDDZ1542Z7aCGfhyF883AGQzVVyWiDycV0atZD8UwXo3qW25BV-VzQVTz2qFeFvT6m9pUVQXqMx0c5-asqLRXZaIJpeq7gRZNOeY9Exu-8q87-1Fh4s5Hi_DMBWH0lzCFUqcVCkJy6vmdj_Y4dE7RoD1feooOYJ4syuRWdlLNKBYpdI_MdpEqwS_-VU_4Tf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا معتقدن مجتبی خامنه‌ای، رهبر جدید ایران، نسبت به علی خامنه‌ای تمایل بیشتری به دنبال کردن برنامه ساخت سلاح هسته‌ای داره.
🔴
با این حال، مقام‌های آمریکایی میگن ایران هنوز برنامه هسته‌ایش رو از سر نگرفته، اما به گفته اون‌ها، رهبری جدید ظاهراً آمادگی و تمایل بیشتری برای توسعه توانمندی‌های پیشرفته هسته‌ای نشون میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/alonews/137366" target="_blank">📅 03:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137365">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66640af45a.mp4?token=kSgNNsm87byclsghNccbgH3T5ZkqF7EIbwb5_H4ICVJ2pvJ-OdcpTeH7z0Ysme6jZ24ocxxke2CY_HIFtaSfLviNF6Ygg0sHTQmWCyEmbBdWxfoUkgRKj0GCYjwuTyMlMS5YEhpnTWzSCesUAKed8J65Qmkd7BdpxjfHCLmt0gGKxDA5xRQjv06cf3D4G4bRVdTrOhb6ehCSYRgIiIe5f6uFRxQZj2UkmYMQ1V4vg-AViYLD-ar5la6LtVXWFGza9dlf5d4BWw-Pb1fxZrRQUT0d69kLWFZmxlPlS4tqYTLEQUzurBaZSkYM17cD3wptFKUJJ9RiuO--zQ-zq7-yqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66640af45a.mp4?token=kSgNNsm87byclsghNccbgH3T5ZkqF7EIbwb5_H4ICVJ2pvJ-OdcpTeH7z0Ysme6jZ24ocxxke2CY_HIFtaSfLviNF6Ygg0sHTQmWCyEmbBdWxfoUkgRKj0GCYjwuTyMlMS5YEhpnTWzSCesUAKed8J65Qmkd7BdpxjfHCLmt0gGKxDA5xRQjv06cf3D4G4bRVdTrOhb6ehCSYRgIiIe5f6uFRxQZj2UkmYMQ1V4vg-AViYLD-ar5la6LtVXWFGza9dlf5d4BWw-Pb1fxZrRQUT0d69kLWFZmxlPlS4tqYTLEQUzurBaZSkYM17cD3wptFKUJJ9RiuO--zQ-zq7-yqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لشکرکشی شبانه در عراق
‼️
🔴
گویا ساعاتی قبل نیروهای وابسته به جمهوری اسلامی به سمت پایگاه آمریکا پهپاد شلیک کردن و ارتش عراق یه ستون زرهی سنگین را راهی پایگاه‌های حشدالشعبی کرده تا پهپادها رو جمع کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/alonews/137365" target="_blank">📅 02:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137364">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فعالیت شدید جنگنده ها در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/alonews/137364" target="_blank">📅 02:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
چهار سوخت‌رسان از اسرائیل برخواستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/137363" target="_blank">📅 02:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137362">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137362" target="_blank">📅 02:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137361">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/ هاآرتص:
تل آویو می‌خواهد تهران را به حمله پیش‌دستانه علیه اسرائیل سوق دهند و در نتیجه برای پاسخ اسرائیل، مشروعیت بین‌المللی فراهم شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/137361" target="_blank">📅 02:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137360">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شرکت هواپیمایی اتریش، تمام پروازهای خود به تل‌آویو را لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/alonews/137360" target="_blank">📅 02:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137359">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
عوستاد: تا فتح قدس یه یاعلی مونده
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/alonews/137359" target="_blank">📅 02:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137358">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEK_1yWkKkGMeTX5WuFiAQ6_iVfuahFw7WJmn3IZ25ckH94VTew2A0lI0llZSeXCbFcndm2GmKsRENeBCpD8uM8hhrZjYbLugWsJuLWvbE3BXOZ6lrDa5vbW1HqXlWetljQcRfOmN6qwBzmQ6lQ0vTgHFO5XzMf2nDr-wvGAlEIvevqGp0a3GZKp3zddgOW8lqRAFFMBpbr3cm1zqHtGcQvwyhbDz1TDPbkec-Vy414VNdaWv8oX-Q9CCl_w4P4AVo5RVlmUaj77JBzwNk6S53hEvf-N9YkqTnSPDY2I0Q_QUbrxPZlfbFJmxRySZk4aPgBC-q46w4ofag5TEfiHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد: تا فتح قدس یه یاعلی مونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/137358" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137357">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
شلیک موشک از خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/alonews/137357" target="_blank">📅 01:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137356">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فووووووری/هم اکنون برخی کشور های اروپایی در حال لغو ناگهانی پرواز های خود به اسرائیل برای فردا می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/137356" target="_blank">📅 01:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137355">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hect9TDCNky-HB2rXYcqOA1TlFhpRZXY_pdL4fUGDiQM8600ZmmJ7S7LmtqNt1BeAOGxuhc0_1SxmXVf8RrlwkQzM-ToBcwRSZ-pNU-mKWBLbW9wUVemBQfFIUCW4IwE-27h3FP3hRZQsoePYe9vr9ZcMEwDCYhZVDlhPrhV8zo3xBXpzQWUoXONZAQ49LxxqGlt-WaN42Exl8p4hPAe82EKgSIVqVTSSDTuwclnnNUjVzDZDItq7glK2J6VyaSy6nyzZ9buXGWLFO_zhYJ3JKSnWMDfOrexOVv3_GWdD-09D3ug_gB1DGWgRTHj33flj3BuzsK1UgCJa0TdcGsoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای ارتباطی E-11A BACN نیروی هوایی آمریکا در حال آماده شدن برای برخاستن از پایگاه هوایی شاهزاده سلطان در عربستان سعودی است تا ارتباطات را برای تیم‌های حمله آمریکا تجمیع و هماهنگ کند؛ این تیم‌ها در حال آماده‌سازی برای انجام حملات احتمالی گسترده علیه ایران هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/alonews/137355" target="_blank">📅 01:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137354">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e29cb2148.mp4?token=eIBTus2mcGQku30IvVl0KunvXKIf3dmecgUVboOx_HY557N9YQgx7FisUfR7n24jkM8BfxHKePQmjKHRr1yPlo0T1StSR0lBdIUNdK4MMR3WrMqmR_W3CwBkfgaZ9paznjSCLSA6U33p7Xru3kV5rreanydGdEx1g5xY-Eik_uTziHxKgb0tEdstlMsZklT2aeV-KvAx_yXqNDyhz5wiUzX-4yUxDajmekYF9b5C4fCJ4sv-O1VvJdIh0DACMsztjx7JwmhHb3gOjhGNXzzCxuis6mfQr4Ml-yfWebHOTdVz67uId5WnFo3f1RJULWCHd3fSNGQm3uzw9reP5ohTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e29cb2148.mp4?token=eIBTus2mcGQku30IvVl0KunvXKIf3dmecgUVboOx_HY557N9YQgx7FisUfR7n24jkM8BfxHKePQmjKHRr1yPlo0T1StSR0lBdIUNdK4MMR3WrMqmR_W3CwBkfgaZ9paznjSCLSA6U33p7Xru3kV5rreanydGdEx1g5xY-Eik_uTziHxKgb0tEdstlMsZklT2aeV-KvAx_yXqNDyhz5wiUzX-4yUxDajmekYF9b5C4fCJ4sv-O1VvJdIh0DACMsztjx7JwmhHb3gOjhGNXzzCxuis6mfQr4Ml-yfWebHOTdVz67uId5WnFo3f1RJULWCHd3fSNGQm3uzw9reP5ohTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این شخص ارزشی این ویدیو فرستاده برامون و میگه حرفم به مخالفین حق هست بزار تو کانال تا ببینی
🔴
جوابش با شما:
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/137354" target="_blank">📅 01:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137353">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
خبرنگار کاخ سفید: سنتکام گزارش داده بود بعضی اوقات ما به ایران حمله نمی‌کردیم ولی میدیدیم که کلی موشک در آسمان به طرف ایران میره، بعد می‌فهمیدیم که کویت و امارات و بحرین و عربستان در حال حمله به ایران بودن ولی به طور رسمی اعلام نمی‌کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/alonews/137353" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137352">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/سیریک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/alonews/137352" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137351">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd-ANm1gW3vuWm0NHuVjv4JiY-FDqPLelKbNMGCeumXx4g2FX6Sg3qVcWasvo8B9dhZhkIp2tz6rC1LgQ-xu7Q8JveUNX5J6k8re1GdinT48G_cm2YU0ibTmkRK3w2H-Omz0HBjDWdmUO-dJPx6vYz6noc_iO1cvg094lV_F3onYhCuOqGiebr1cz7nU-Hu4Nawl7rm0wVLZbdeC_WQmbyCbBf8KE7MmbMK7couKgO-cSqy_yPKfCDo3xAdaPIT3FuEv_-7l5qQGnrgw0u-GOJ_mnvgnYkwJ_yDyyr-DgjbxgbsaH-DI34gIxmpxOvTsrg9by6vvokGeabrHEJdgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همراه اول قیمت بسته های شبانه خودشو 3 برابر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/alonews/137351" target="_blank">📅 01:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137350">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
به نظرم یه جنگ سنگین و فشرده و حداکثر ۱۴ روزه در راهه، از لحاظ شدت حدود ۲برابر قبلیه و ترور هم زیاده. خداکنه به زیرساخت نرسه اما احتمالا میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/137350" target="_blank">📅 01:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137349">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: هواپیمایی اتریش و شرکت آی‌تی‌اِی در میان نگرانی‌ها از تشدید تنش‌ها، پروازهای خود به مقصد اسرائیل را لغو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/alonews/137349" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137348">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq7Pit73x2P6yJVTgbJ_VvXLpcTBZ_yXJ1qt9V6vl6mvUz0cFgsov_zANxVxUHy5GK1RXY0vDsB0di_XXzsYTqD_ytDJvsmmF5fPl9G9HQtwClsebDvx0h-A9eOT2dpSuQs2I7kbg_DdZyknTc5yJ_69QwDvgKQ1kWdjWfYKM-vVrjW0fVlAGMaOXzZXJ0I45G3ZOJbW_tIw_Do9sx9wcdXXTuQBgD4FfA_spQAClTrDH7CtWWn-kQuS8x078ghejMiRR2Su83Nnvf7RXastN7EbGATpowu_-7A1NgLmP8FnEaPOgEz_bnbzRnufaZKJT7ELN7WLcBct_SKnSnOtIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرویز پرستویی: لعنت به پهلوی و همه طرفداراش
✅
@AloNews</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/alonews/137348" target="_blank">📅 00:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137347">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
دقایقی قبل یک موشک به پایگاه آمریکا در بحرین اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/137347" target="_blank">📅 00:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137346">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKR0mHZWXvlSZljtq_-yHMWPpVRr26UYttbTSNFlECOPu1ssNNGPVoItSBiusdCt672oDSy9z8m7k1ovjJmHeE1SqlykuPKXt7lz9cnDRg4RvqrkmzNeinr6NdrJ4BsOG6oVa0UBii8kj7QVLk6PbZsOyHWJtBSgAWvrsdu8xjJuHJGwN8rF1WNfUlX4bDOs_IhRwvdgoY8oFmC1Pv-Kl1OG0y1VpTrKYyf08bdpc_Sko_JyD9F0XhDb8CtTjEMuexyeL93IrSilKGsVclBW1HK68EwnB_bmZFnbeMTEEE6CdvtwTN1MDs6t4ooisN5FlnydGP0E7ngxXuA5tIWaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: یا مرگ یا ارث بابام
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/137346" target="_blank">📅 00:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137345">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2479a179bf.mp4?token=K0XnH7_0cPdaXCJZsguT8G6OgRY8JtvX1zzDykymvifm9Zp9AfvL51nM3QahQQInWuyNQLV_-1pvD6zIVo-hdzIzrfSDJDBoU_HIxn1BbZkJ1NxIQw-EA4X8CTji_r8nEfyMjkKizTE4rmALDO2MlgK3HAt4ipM0pStzmy83q518CxT20vNWyKl63AJic-SMwoEpMCKdsUuJPeTNQVizeQpFuIBuzL0ugTUz4pfLi8GT3tM_Q4m9G8nhgrxNALLvXODk-H85cU15TE4k2KuPTQxA3MtgmbvsERw1exbpuupjdYtorTS41EvhbDQwTPTociRFD2Il_VioL1ak2AQ6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2479a179bf.mp4?token=K0XnH7_0cPdaXCJZsguT8G6OgRY8JtvX1zzDykymvifm9Zp9AfvL51nM3QahQQInWuyNQLV_-1pvD6zIVo-hdzIzrfSDJDBoU_HIxn1BbZkJ1NxIQw-EA4X8CTji_r8nEfyMjkKizTE4rmALDO2MlgK3HAt4ipM0pStzmy83q518CxT20vNWyKl63AJic-SMwoEpMCKdsUuJPeTNQVizeQpFuIBuzL0ugTUz4pfLi8GT3tM_Q4m9G8nhgrxNALLvXODk-H85cU15TE4k2KuPTQxA3MtgmbvsERw1exbpuupjdYtorTS41EvhbDQwTPTociRFD2Il_VioL1ak2AQ6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی قبل یک موشک به پایگاه آمریکا در بحرین اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/137345" target="_blank">📅 00:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137344">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
گویا سفارت خانه هند هم در تهران تخلیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/137344" target="_blank">📅 00:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137343">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مراد ویسی؛ تحلیلگر اینترنشنال :
🔴
تا جایی که من آمار دارم تعداد جاویدنام ها ۳۲۲۲ نفر هست. اگه آمار بیشتر هم باشه اسمی ازشون نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/alonews/137343" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137342">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT_ZpPWK5ESCvx7a_1GOc2NhPWLOAHZVnX6k2feLPFk7QpFGguJtbkcJ5DtQtzfMQ6lhyfSPesg__sqeN7yo2xRDnWqarhpiJenGThU3koVwHHyTKkmIHcPNAgo9j93ut6kkkw3hHw0CxyaotFO8d_jwPGl325vvran2OTEZcj3akAk3frC57w9tE3Nm1cB_Z-s_kDqy_iJzTcpV1C-3KEx70uaKLRqNcXv9ZQXR7mzfZ_io1I5eXMMUNpZ9hxkHW0TLNSmSPDnfajYQ4NVq98homlbwoi8vLA92QU4TU_FJNCgJr91tJxUVxpfZay8bfkEGsucXNmK8HWQj5qQzSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرویز پرستویی:
لعنت به پهلوی و همه طرفداراش
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/137342" target="_blank">📅 00:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137341">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ائتلاف از حمله به مواضع نظامی انصارالله در استان الحدیده خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/alonews/137341" target="_blank">📅 00:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137340">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=u_i3QOy7C41AjOdAx8uubkmLbiXWeVSGnnEhSE9zQ1JnfkHSSswYFcJWPwq69yuEpFlft6JJbwmRpMooAkR7Nlc9FkPmHSPrJVEPEB0hgCuUcyG6vKozLWElAqP8FSRmEA9xEQsxZeOX4RDLI0dGmFETBfT2iIWUT4fS1nNZ-SrrCBldgy450rWk4YxkEZOSMUR6xB_S6YQe0Ycrf05zK4q9KaU5tN-NHO5HjhGFU_c9IIkXwmf4tL9wz-SOUChQcwDoQxz2fqzk2o10YfTPgKS0mXt8_3tkSVmZjUELCRyJHMJzUnWpa5bg3DRw5M7GAC-RiNV0uJG2ivUR9M5dJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=u_i3QOy7C41AjOdAx8uubkmLbiXWeVSGnnEhSE9zQ1JnfkHSSswYFcJWPwq69yuEpFlft6JJbwmRpMooAkR7Nlc9FkPmHSPrJVEPEB0hgCuUcyG6vKozLWElAqP8FSRmEA9xEQsxZeOX4RDLI0dGmFETBfT2iIWUT4fS1nNZ-SrrCBldgy450rWk4YxkEZOSMUR6xB_S6YQe0Ycrf05zK4q9KaU5tN-NHO5HjhGFU_c9IIkXwmf4tL9wz-SOUChQcwDoQxz2fqzk2o10YfTPgKS0mXt8_3tkSVmZjUELCRyJHMJzUnWpa5bg3DRw5M7GAC-RiNV0uJG2ivUR9M5dJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آژیر حمله موشکی در بحرین به صدا دراومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137340" target="_blank">📅 00:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137339">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8mLzRo_iYaF-17W7AtfyPoNP7BiQso5FhGSEQnWjf1GSCHEw8X38Cw-YVV7TTMb2DBXD-AWQiT6hKQz7zxiyuxCDtH9xkkrEaeYBC-TRZg57HprN1hlWvQazvaByvuLRMfp7KVyqykyLgvtRP1sprUO7yLfiJLzperH9ohjnjn39dcJzcfwM5EWLVlX6pl_Sn0G8d6wp1suif5KvGZI31CE2RBobBTiXjUkm9RoAXc3IfJXc8LuDpxLbgX-sThOpwYKL405Yo2TFL535FDfZhlS7VqeNrLOWv8R1UeX6P2njBpU8WNXoCISw2Vcb4CCzNm092h6LpM5VLwGKm7L4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید
زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/137339" target="_blank">📅 00:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137338">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499b17bb9a.mp4?token=EqpkphaNHS37P61bMFCCcF9JCq7EbNiQclFHg8FAr29YfGH0JQy_qDrpyeM5w63QFRfKxq8XS_46f54xdc_F-JCAiUUUw0Ciw8xGneSTrAdI7RbO6Jv3NPjUS2_4Ssg2c-DrNzXuYgE_Ly9BzVi5D45zr_e3GZRfLKGPnAVdphhFz_SYTZx-wJ6fG1sXTmFMb6amheEefxjCy2BQxKBKocQ6YzC4MggVyxj9WBkxkOKwXn2KPgXQWhBYmxkUPMDd1_4dopdemukIzQA1k3QGzJVocAAQQqZ8Dv5raTWLKOz1AeHRZtmJdg1W1DyQ0I9y3-eEyw4Oq-QPDmeqTncxvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499b17bb9a.mp4?token=EqpkphaNHS37P61bMFCCcF9JCq7EbNiQclFHg8FAr29YfGH0JQy_qDrpyeM5w63QFRfKxq8XS_46f54xdc_F-JCAiUUUw0Ciw8xGneSTrAdI7RbO6Jv3NPjUS2_4Ssg2c-DrNzXuYgE_Ly9BzVi5D45zr_e3GZRfLKGPnAVdphhFz_SYTZx-wJ6fG1sXTmFMb6amheEefxjCy2BQxKBKocQ6YzC4MggVyxj9WBkxkOKwXn2KPgXQWhBYmxkUPMDd1_4dopdemukIzQA1k3QGzJVocAAQQqZ8Dv5raTWLKOz1AeHRZtmJdg1W1DyQ0I9y3-eEyw4Oq-QPDmeqTncxvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیروزمند، کارشناس صداوسیما: تا کی قراره مجتبی خامنه‌ای بیرون نیاد؟
🔴
مجری: تا نابودی کامل عوامل جنگ.
🔴
پیروزمند: خب اینطوری شاید ۱۰ سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/137338" target="_blank">📅 00:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137337">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری/هم اکنون وزارت خارجه آمریکا در هشداری جدید اعلام کرد:
تمام شهروندان آمریکایی باید در برنامه‌های خود برای سفر به خاورمیانه تجدیدنظر کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137337" target="_blank">📅 00:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137336">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Djcxnx2FT4FeDY3xbWMmecG6DI2zp5R8amD4nxE-IPNx95sA1ekG-DOLqIjP8bY1xkLWEZng_JUrwLOHaATG-yzkUQkGYMssi16d1lMSYt6wO8_7Lhx091odx_0Ll7FzEYIbhgiB49eN4dpkGA-HXERDuvvbIX5FkhvBcUbiQB2o7Ri5aOnrR_e2kAw77pOBTcQgVc6Y2crrKDYzeu74hJsoMQv56KlwyjjPwJlqJRJQ8dzH0xolDGat8gUBSyd942LgIXOc93HmY8gHPZNKo01SXHxpb3chV_-hGwmHPUdS4K1oDlvsGnV9FEZZ2AcB2_Wz354Gk0CB39B6jZx8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارشات بمب افکن b21 raider که جدیدترین بمب افکن آمریکا است جهت عملیات در تهران به اروپا منتقل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/137336" target="_blank">📅 00:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137334">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نیویورک تایمز:
مقامات نظامی می‌گویند بمب‌افکن‌های دوربرد B-2 و B-52 در ایالات متحده در حالت آماده‌باش کامل هستند و هواپیماهای سوخت‌رسانی هوایی بیشتری برای پشتیبانی از آنها به خاورمیانه نزدیک‌تر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137334" target="_blank">📅 00:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137333">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری/انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/alonews/137333" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137332">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bd99063.mp4?token=NAAIepF10mrEXzNVBluviUOESM6IDioMMgDU2cQKtgALnAgRpgZypFAeJz0YXaMDWzLMA-s5BAKZkTbo_2YSdsYGNhY8Zi7J9AmdVmMaY2khg7KrDEF8k5GvjLOkHn2cPDORHzG-2mjP1XGupFdxzJkw53movZ93XcAZk9nsOf22g3x02UQfstB3EE-cdYBzbvKo7FUx0NsHWim87Orf9vblSVQDfd85On8-hBSqAsXXwGvOh6rFHhScWSwyM9tw7ABFVNgvFE4lHEyTBAIeF_biyfJBtmQY3Ei-k7CPlZ_kNT4zZDuDO1ysxFHNCxUlUHlypWZYFt7jXrgudsPrDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bd99063.mp4?token=NAAIepF10mrEXzNVBluviUOESM6IDioMMgDU2cQKtgALnAgRpgZypFAeJz0YXaMDWzLMA-s5BAKZkTbo_2YSdsYGNhY8Zi7J9AmdVmMaY2khg7KrDEF8k5GvjLOkHn2cPDORHzG-2mjP1XGupFdxzJkw53movZ93XcAZk9nsOf22g3x02UQfstB3EE-cdYBzbvKo7FUx0NsHWim87Orf9vblSVQDfd85On8-hBSqAsXXwGvOh6rFHhScWSwyM9tw7ABFVNgvFE4lHEyTBAIeF_biyfJBtmQY3Ei-k7CPlZ_kNT4zZDuDO1ysxFHNCxUlUHlypWZYFt7jXrgudsPrDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی؛ تحلیلگر اینترنشنال :
🔴
تا جایی که من آمار دارم تعداد جاویدنام ها ۳۲۲۲ نفر هست. اگه آمار بیشتر هم باشه اسمی ازشون نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/137332" target="_blank">📅 00:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137331">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
خبرفوری/جنگنده‌های F22 آمریکا به عربستان رسیدن</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/137331" target="_blank">📅 23:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137328">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34fd806b7.mp4?token=OUSTERarqDk0hG8W4421y9kGdAKnN7aknSyMJYwun82jhn9EaA44hWMhytbmK6qe3ChARjvECEjMPQFjzWp5Ro0SVHcd2IvhYuCYCA2qXNyU3bP8Ew-Lv_nMvnPDOgZ7Bem3unxqjZLo2XSs5qYk_2frX7rrJPXMIhrtzMxdtOVtoXDrdAmlesdKjUX4VG9JOAEx3UCkvv5NFhrTABGtzeUbwH4NVvLJsNHhfgZIa8Cn00Rmhf3XivzxWfDn2EoVCTMA7KO-oz6k5YmCrzJh2PZBH_goiE-2BpWYvRda9n3_yGPar5fOBMWIPAnKj81ILoAxU4zRnGjhTMexJ4bcVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34fd806b7.mp4?token=OUSTERarqDk0hG8W4421y9kGdAKnN7aknSyMJYwun82jhn9EaA44hWMhytbmK6qe3ChARjvECEjMPQFjzWp5Ro0SVHcd2IvhYuCYCA2qXNyU3bP8Ew-Lv_nMvnPDOgZ7Bem3unxqjZLo2XSs5qYk_2frX7rrJPXMIhrtzMxdtOVtoXDrdAmlesdKjUX4VG9JOAEx3UCkvv5NFhrTABGtzeUbwH4NVvLJsNHhfgZIa8Cn00Rmhf3XivzxWfDn2EoVCTMA7KO-oz6k5YmCrzJh2PZBH_goiE-2BpWYvRda9n3_yGPar5fOBMWIPAnKj81ILoAxU4zRnGjhTMexJ4bcVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران گفت: اگر من رئیس‌جمهور نبودم، اسرائیلی وجود نداشت.
🔴
ایران، به شکل شوکه‌کننده‌ای، شروع کرد به شلیک کردن به همه در سراسر خاورمیانه.
اگر آن‌ها یک سلاح هسته‌ای داشتند، از آن استفاده می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/137328" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137327">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ظهر امروز نفتکش عربستانی NCC MASA مورد حمله حوثی‌ها قرار گرفته بود.
🔴
خبرگزاری دولتی عربستان سعودی اعلام کرد اسیب وارده به این نفتکش جزئی بوده و آن به ادامه مسیر خود ادامه داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/137327" target="_blank">📅 23:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137326">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
خبرنگار: شما می‌گویید که با ایران مذاکره می‌کنید. چه کسانی در این قضیه دخیل هستند؟ ویتکاف؟
🔴
ترامپ: تقریباً همه. جی‌دی، مارکو، خیلی از افراد مشغول گفت‌وگو هستند. این موضوع خیلی مهمی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/137326" target="_blank">📅 23:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137325">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_hDO-vWutDEOx2hCi3HqYIs3sBbBo-JHWI1R4MAqwtyKmuTArLBs3xIqefAJKmrEZ_Im6-P8XHpTkuJgQRRSWLIrIKjDpu4rdUg9HOINLvm8UkdoCw6rKXoIr3zUMIWfn18WPtIFUJlXs4nUTQ1t3CD0CDSnFvjh1g4IhjUhd_zDHbTEVlf27qn9p-7gml6RgWXMxA2w4efsT4TfXu_KOegyKRv3zmmBFUUwmCTny73YbcLD3NPo7he8_4hnRodPOlRxNzIDCgUTg0iCtqNI9NduwJb5ngqepZXvMCjKRP2CJqqKNO8bDiKoORTS86r0XLvJtn1ek6etaFvUiCgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون بندر الحدیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/137325" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137324">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ : ایران، باورنکردنیه، شروع کرد به شلیک کردن به همه‌جای خاورمیانه.
🔴
اگه سلاح هسته‌ای داشت، حتما ازش استفاده میکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/137324" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137323">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea64c7c35f.mp4?token=fu9WV0lpyqSuhX7shlmY2TPuMlyjqSJd3ORf5_xQnLhZ5FoATdMWBgv4xkgVg8reuxfqiqT7wJTNHxIaPWsOZ4hRN5ZXPA0xyMznu02vCO8bRMOAUZLJT3qTJdWnzHughN7pXQejM5XIo4PX5XF1gPzsWAZbXYT356U19rj4JOXQgU3p8tJuuPk8I36dQejxCQsGbD-efsihnbRgFVVi57BilrWnrEHHWqLIFrCoWF-HHAlvh35HhIN8oMwUHaZqqk6phY9JcLzCZzo_tI60MPpQncQKlDfmyDCb1Al2crV1XrJYfroVIGaQG0WY1wNr-XsSelr3r9bF9BQVP8XRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea64c7c35f.mp4?token=fu9WV0lpyqSuhX7shlmY2TPuMlyjqSJd3ORf5_xQnLhZ5FoATdMWBgv4xkgVg8reuxfqiqT7wJTNHxIaPWsOZ4hRN5ZXPA0xyMznu02vCO8bRMOAUZLJT3qTJdWnzHughN7pXQejM5XIo4PX5XF1gPzsWAZbXYT356U19rj4JOXQgU3p8tJuuPk8I36dQejxCQsGbD-efsihnbRgFVVi57BilrWnrEHHWqLIFrCoWF-HHAlvh35HhIN8oMwUHaZqqk6phY9JcLzCZzo_tI60MPpQncQKlDfmyDCb1Al2crV1XrJYfroVIGaQG0WY1wNr-XsSelr3r9bF9BQVP8XRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : باراک حسین اوباما خبرنگاران را تحت پیگرد قرار داد، اما هیچ‌کس چیزی درباره‌اش نگفت.
🔴
وقتی اوباما این کار را می‌کند، اشکالی ندارد؛ اما وقتی من این کار را می‌کنم، می‌گویند اشکال دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/137323" target="_blank">📅 23:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137322">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
گزارشگر: چه زمانی ایران تسلیم خواهد شد و واقعاً پای میز مذاکره خواهد آمد؟
🔴
ترامپ: شاید آن‌ها تسلیم شوند، یا شاید فقط به یک غار بروند و مخفی شوند.
🔴
آن‌ها غارهای بسیار عمیقی دارند که می‌توانند در آنجا پنهان شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/137322" target="_blank">📅 23:32 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
