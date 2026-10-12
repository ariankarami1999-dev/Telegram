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
<img src="https://cdn4.telesco.pe/file/ErUBJj5DlLH96z_Io5gwWDsCCGkTI53ukcG3jGjPTKIc3PtQs8I78vxK06ry5ouzOf4Hn__jtiKFh44FkSTmrmYiLKEpME1X98sIjCVJjKgvVsDC340fdfvapDWp7iPAylyyf-LIt9UdbVnvPAC7AJDFe-l4AYLEJ_pX9o17LsuJa66i4WmLf8zBVjD3ue_x-5Z9Qe9K_Btj8w9XGrKs7elecr9n4rpdCIzUCZDcnAOWllDz3oEk0cqFvBB5MHkn1Tdke76luZDERr2wHGS4DvS-fWD3vCSl0IdppVQ0n58ZxJhskHQwE7pGj6GHqEpq55duDPCwv4_ofeV-lDTCSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 04:57:01</div>
<hr>

<div class="tg-post" id="msg-697617">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buwPJo_FdcncFQ6DJ1080inH13xTGMrZD6hn37aQB-vbg1aFqmTe7mf8HdBxa46Jl6BPw4A_UDHFlJNmK_UY92Q0bupwAExLIrbWmXEjce50thxlCZ4ExFi0rePASqaxszy2Jz0YgAyLiULykjqWol-dnujlMw8RekjEMLkt-tQ6eA4CTAIL07iqEpQ0x2AtCYS8mpTRPMloNj3cbtBmtSNJGMj1fDrr8BvlN8v-K1EWDgZ77kk41gfQbFNKoRlg5Ha1ZNBDczErSCwPsvwJ05wMvcnZiQ-lnbqovf6D5LqeGT-b0G7e6yWmKybBVEcgbXVh5mtBeNwFqsBX8vC7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👟
تجربه‌ی سبکی و استایل؛ نایکی مدل فرزاد
وزنی به‌قدری سبک که فراموش می‌کنید چیزی پوشیده‌اید!
«الان بپوش، زمستون تسویه کن!»
❄️
💰
قیمت نقدی:
۱,۸۵۰,۰۰۰ تومان
💳
شرایط اقساطی: ۴ قسط ۵۱۵,۰۰۰ تومانی (بدون فشارِ هزینه‌ای)
📏
سایزبندی موجود:
۴۱، ۴۲، ۴۳، ۴۴
تعداد محدود است. برای سفارش بزن رو لینک
📦
https://memarket24.ir/product/fast/59406/180124/</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/697617" target="_blank">📅 00:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697616">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bc07a869.mp4?token=KliKaYZLyX89hbtU8-kytUdVwSyYSoR95LO6Gw8dnMMkU86zVp-8WLjmHJajrrDuOQvLtdI-thNPVc8RYx8XxkSiavwVVReZUfu9-8Ayts5gLpNwy754yzYaF9oSMN-NrSYoEbRNxTqLmjT5ddoKlfhTqoTuSsJ7oP86hRhePrQRcMGrICQZRGrh3z-pq349j23eG_Qy8eQoPqSB-nA0mcX1oPaf56uNFVF68I-3or_QOieMBVVxX78FjDLdmMEikvRSzMdHV-kW9A4l_uu-uIbsbP7LU7VWajaQlITXv0CTG3Z4Lzwtt5EvgqydoqA8bs17-_K6VgcpUjR7NKsrvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bc07a869.mp4?token=KliKaYZLyX89hbtU8-kytUdVwSyYSoR95LO6Gw8dnMMkU86zVp-8WLjmHJajrrDuOQvLtdI-thNPVc8RYx8XxkSiavwVVReZUfu9-8Ayts5gLpNwy754yzYaF9oSMN-NrSYoEbRNxTqLmjT5ddoKlfhTqoTuSsJ7oP86hRhePrQRcMGrICQZRGrh3z-pq349j23eG_Qy8eQoPqSB-nA0mcX1oPaf56uNFVF68I-3or_QOieMBVVxX78FjDLdmMEikvRSzMdHV-kW9A4l_uu-uIbsbP7LU7VWajaQlITXv0CTG3Z4Lzwtt5EvgqydoqA8bs17-_K6VgcpUjR7NKsrvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساییدگی لاستیک، از مشکلات فنی خودرو خبر می‌دهد!
🔹
نوع خوردگی آج لاستیک می‌تواند نشانه‌ای از تنظیم نبودن باد، مشکل فرمان یا خرابی جلوبندی باشد؛ تشخیص به‌موقع این علائم می‌تواند از هزینه‌های سنگین جلوگیری کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/697616" target="_blank">📅 00:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697613">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df7ca88cb3.mp4?token=v6sfAe-El3r-0vMV0H-_j_ayEgT72A5V_MoQPP9OWVc8PJ0ZX-CM8FL7Y9E58P5oj1d2xdUePaaW3bWA4KrL6kh9RRxE-h-Yt7GN_NoJ4W2mCUoXko6Sl63IPAWx463BKDGM-MQSfd5H9gxHMi-Jhkt2scKWLlDlCulqXUOxc-9Igmk6Oe8SvrYar9qqR1JrhAVpl7rtc3OyIJp-WYnsE2f0MOwJ6srKUNHUVqvruMVntkl8ZlVVtRdXV77ll_THY40t8JQ18oVMGRFEufOIXNGAQy-bXX_xpPJRx5wgg8nRYSXHj8X2VlunkUV0QyLzzKx2mRMti2baY7rZevDicQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df7ca88cb3.mp4?token=v6sfAe-El3r-0vMV0H-_j_ayEgT72A5V_MoQPP9OWVc8PJ0ZX-CM8FL7Y9E58P5oj1d2xdUePaaW3bWA4KrL6kh9RRxE-h-Yt7GN_NoJ4W2mCUoXko6Sl63IPAWx463BKDGM-MQSfd5H9gxHMi-Jhkt2scKWLlDlCulqXUOxc-9Igmk6Oe8SvrYar9qqR1JrhAVpl7rtc3OyIJp-WYnsE2f0MOwJ6srKUNHUVqvruMVntkl8ZlVVtRdXV77ll_THY40t8JQ18oVMGRFEufOIXNGAQy-bXX_xpPJRx5wgg8nRYSXHj8X2VlunkUV0QyLzzKx2mRMti2baY7rZevDicQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله مرگبار ببر به مردی در انگلیس؛ ورود به محوطه ممنوعه پایان خونینی داشت
،
فرد توسط ببر کشته‌ شد
🔹
ویدیویی قبل از ورود این فرد هست که میگه «من میرم بین ببرها، ازم عکس بگیرید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/697613" target="_blank">📅 00:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697612">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
قدیری ابیانه: حسن روحانی می‌خواست اروند را به صدام بدهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/697612" target="_blank">📅 00:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697611">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DORqptQXeWhiHS9Z6FZyYJf8kSPciMvWSv679Ql8EtPuRfcTJg_4tv1S0aZ14ehyrHOVZ4ZWbTil5JED_Okm9QPvbVDRGOrXf2gukme6mhPxNmVj9O9cSiTdj5c42fBFNnEF_P-4FkLzu0rUha8yG__xP9VQJUa3zVWLSvJ1TBhhE-sESbPKbbA9xJI2_TDoUL0PSUFLWDX9wWiRIKnTODsNYKxcixvAkoCTHR3CzDCskY-ziLRWQ7V8ow2zsAkR8IXoht2pCR1546FWhD4ztANxUJG7g3AasE8flGQ0agxE7bqTeIsdaS9C_kumiTmk9IpPpURVZQBJZJ2ptRtOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/697611" target="_blank">📅 00:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697610">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سفر برنامه ریزی شده استیو ویتکاف و جرد کوشنر، نمایندگان دولت تروریستی آمریکا  به مسکو به تعویق افتاد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/697610" target="_blank">📅 23:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697609">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkDDzsIWyVNJcAWfLbPS8H5xN1f4KzKtYU7usImE6qdZd2y944bFq1Wfhb3Qzv42QPJ4fHjl4vRqweSUMZpJbDEEWxJvXe_11qC-vG0PrGJITDHuuTR5ydPYNx9_eMjke3l4cW-xcQepo1IvPJsk-R97k3g3GuNZDujAF6kEv8vJE4nXwWL1cwAhyPoOz9rQDUyEzy51vVH6FSkoxS5IZ-pufS1BJdYYB2YciQ_RlkhRbLI7nrsnq8VASzIRIsEBMJUViHxYEKgDc7UgCqujRwrOCNo4sCbdAvP3WK87JtJBlr7QAPzrTyob9uDhZtO00X-ia8QWJ9GL11iiLiqg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما منتظریم
🔹
سخنگوی سپاه با انتشار تصویری در فضای مجازی نوشت: ما منتظریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/697609" target="_blank">📅 23:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697608">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را ا دست ندهید
🔹
🔹
پروژه شوم ترامپ و روبیو علیه ایران در آستانه جنگ
👇
khabarfoori.com/fa/tiny/news-3251656
🔹
دلار بی‌سابقه خواهد ریخت؛ آماده باشید، طوفان در راه است!
👇
khabarfoori.com/fa/tiny/news-3251427
🔹
این چهره‌ها در لیست جدید ترور اسرائیل هستند
👇
khabarfoori.com/fa/tiny/news-3251640
🔹
از اورانیوم ایران تا گازوئیل آمریکا؛ معمای سیاست دوگانه روسیه در جنگ | پوتین، میانجی صلح ایران یا معامله‌گر با آمریکا؟
👇
khabarfoori.com/fa/tiny/news-3251551
🔹
حکم دادگاه اعلام شد: قاتل خواننده مشهور زن، دخترش است!
👇
khabarfoori.com/fa/tiny/news-3251333
🔹
خبرهای جذاب را در خبرفوری کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/697608" target="_blank">📅 23:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697607">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75db946e2.mp4?token=c95cj_GmwBTlAUDMXqbSJL9SNBwX39VcHCapnoK1ykURBf8YezKkZqniOSEK0fzXl7m513VCXJiTjnXKvVPIejRXuh7ILEWFqZjoehshpXFq1QeaM2tV2D86Xm9FrTgMbGpZgZk-ALqDz75SwKp2dBbXL5YybXfkRmhEsMTNNLpfmu7Tj1iNYx1-CWjzwbauQPjvOIwJIENyJlBK-oTPYuiE06UTA50gWWlaLulnRJmcZp6QGSFdUv2PlZQ9mxf22oh9zVKrZG8DDhNxhd-NgdtpDgR5h9WUr1b4BMm_0aVYuOdVwEjY6lZjd9Fa3u_e-PhKQntwaF9Xr0QRWnizIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75db946e2.mp4?token=c95cj_GmwBTlAUDMXqbSJL9SNBwX39VcHCapnoK1ykURBf8YezKkZqniOSEK0fzXl7m513VCXJiTjnXKvVPIejRXuh7ILEWFqZjoehshpXFq1QeaM2tV2D86Xm9FrTgMbGpZgZk-ALqDz75SwKp2dBbXL5YybXfkRmhEsMTNNLpfmu7Tj1iNYx1-CWjzwbauQPjvOIwJIENyJlBK-oTPYuiE06UTA50gWWlaLulnRJmcZp6QGSFdUv2PlZQ9mxf22oh9zVKrZG8DDhNxhd-NgdtpDgR5h9WUr1b4BMm_0aVYuOdVwEjY6lZjd9Fa3u_e-PhKQntwaF9Xr0QRWnizIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر در آسانسور گیر افتادی، این نکات ایمنی را فراموش نکن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/697607" target="_blank">📅 23:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697606">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7joKIow3Uqk7ct7HbO6GKElz4cc5NDxdNsSist5J8bBxokDaA2Ntd6rSe1JTOXe9C93ItbaonAETGWPNjvuKz5utxKFE3ZfHmnu3E9fj8JQDcK-pigXxORP8ClyhpcK9ywZXZ3WCTLaEtIywhYZx1hIb0iU5_yw-JLYnXlGbzEU7jvaz0mGyMuZtYis6uZpakvtUPVDUbrE4OKhcCBu1hrg-gCP-Bj0skZpxPLSUzwBkI-ZvOHlnZuX4f4_w1QfGfBxdsZoQibzx4-h8Et_PsJmx6AZClwCrb1V6mzvOEgld4BKPUZScYhbtDHjbfze3EIXG95NJ6OwVQY9IZafHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شریان‌های راهبردی هوایی اسرائیل و ۵ کشور منطقه در بانک اهداف احتمالی ایران
🔹
بر اساس اسناد و نقشه‌های منتشرشده از سناریوی پاسخ متقابل که توسط رسانه امنیتی جریان منتشر شده، مجموعه‌ای از مهم‌ترین فرودگاه‌های بین‌المللی و قطب‌های هوانوردی منطقه به‌عنوان اهداف احتمالی و راهبردی در سناریوی واکنش متقابل معرفی شده‌اند.
🔹
بر این اساس، در صورت وارد آمدن خسارت به زیرساخت‌های ایران، مراکز کلیدی حمل‌ونقل هوایی که نقش تعیین‌کننده‌ای در جابه‌جایی مسافر و کالا، پشتیبانی لجستیکی، مدیریت کریدورهای هوایی و حفظ پیوندهای بین‌المللی کشورهای منطقه ایفا می‌کنند، در زمره اهداف اولویت‌دار قرار خواهند گرفت.
🔹
این فهرست، مهم‌ترین دروازه‌های هوایی رژیم صهیونیستی و کشورهای عربستان سعودی، اردن، بحرین، کویت و قطر را در بر می‌گیرد. از جمله این مراکز می‌توان به فرودگاه‌های بن‌گوریون، حیفا و رامون در سرزمین‌های اشغالی، ملک عبدالعزیز در جده، ملک خالد در ریاض و ملک فهد در دمام، ملک حسین در عقبه و ملکه علیا در امان، فرودگاه بین‌المللی بحرین، فرودگاه بین‌المللی کویت و فرودگاه بین‌المللی حمد در دوحه اشاره کرد؛ مراکزی که بخش قابل توجهی از ظرفیت ترابری هوایی، پشتیبانی لجستیکی و ارتباطات فرامرزی منطقه بر آن‌ها استوار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/697606" target="_blank">📅 23:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697605">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5652cb8a.mp4?token=XfqudERxHcNS20uLXrRrqpq1gDc0mbShM5nf18Fh59YZKzrsSMJ6JRq4oFfgdw3pqAepCsLLTmO-0UX5W0yFOAdIAl_S06JoMQZAGfSf4EcFA-6WrlSVcTKjubC-IgZO8WUuiomS2xP9U3QXGSuSOfCEQ_prrw409eRaFiumWPHoMJbi0RRDUDmwnOxlu9tGNvx2189gZG6Pju9RRLnIUZgoQzvf8x9HRtq1ikg_I0Ga_jvVYyyRCFlHL6pKjhffNPJHSxjpy2UB0BFEQuvnLOlViXQD_vepk99vczNEE92CbV5TMuOvrVw6DwkpyIeTc44UfmMzIB0pAOZ-oVMCX4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5652cb8a.mp4?token=XfqudERxHcNS20uLXrRrqpq1gDc0mbShM5nf18Fh59YZKzrsSMJ6JRq4oFfgdw3pqAepCsLLTmO-0UX5W0yFOAdIAl_S06JoMQZAGfSf4EcFA-6WrlSVcTKjubC-IgZO8WUuiomS2xP9U3QXGSuSOfCEQ_prrw409eRaFiumWPHoMJbi0RRDUDmwnOxlu9tGNvx2189gZG6Pju9RRLnIUZgoQzvf8x9HRtq1ikg_I0Ga_jvVYyyRCFlHL6pKjhffNPJHSxjpy2UB0BFEQuvnLOlViXQD_vepk99vczNEE92CbV5TMuOvrVw6DwkpyIeTc44UfmMzIB0pAOZ-oVMCX4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرار سارقان موتورسوار که گوشی و طلای مردم رو می‌دزدیدند از دست ماموران پلیس که در نهایت با شلیک گلوله متوقف شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/697605" target="_blank">📅 23:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697604">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 12- میدان دوازدهم، یقظت</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/697604" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح کتاب صد میدان خواجه عبدالله انصاری
🔹
میدان دوازدهم، بیداری
🔹
انسان بیدار و هوشیار، به هیچ‌وجه نباید در غفلت فرو رود، همچنین مسئولیت‌های آن بیشتر شده و می‌تواند حکمت اتفاقات جهان‌هستی را به طور کامل درک کند.
🔹
در مسیر طریقت هرچه خود را هیچ پنداریم، موفق‌تر خواهیم بود و آن زمان که خودمان را برتر و سرتر دانیم سقوطی بزرگ خواهیم داشت.
🔹
عزت و رشد بشر در خاکساری‌ست، جهانی شدن و به نمایش گذاشته شدن با خلاف این امر سازگاری چندانی نخواهند داشت.
یقظت را سه رکن می‌باشد:
🔹
نعمت‌های بزرگ را از وی دیدن
🔹
جرم‌های بزرگ را از خود دیدن
🔹
عیار روزگار خود از زیادت و نقصان شناختن و مدام از جمله‌ی مکر ترسیدن
🔹
اول، نعمت‌های وی را به سه چیز توان یافت: به نیاز دل_شنیدن علم_پاکی قوت
🔹
دوم، جرم به سه چیز توان يافت: کوتاهی امید_دوام فکر_بیداری سحرگاه
🔹
و آخر به سه چیز توان یافت: بدگمانی به خود_بریدن از علایق_تعظیم حق
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/697604" target="_blank">📅 23:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697603">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE6X9IJP8AjW87jdaevQqrDcr0vxg3NgpJy0iJ8s-9q_GKXPmaD9176hnNuSxM0R_ZIeL3yq0vC6O9_5p_tcqVlAFivOybDq7dAfwNb3JsLoLRd5ob-o3SO1fHbArPkoj84ny-_ErAWwS5kOnMaQgc1ikFPeST_RQnHOrah9laCmXqWnOCCtbDqik8iB4OL1_ootfRWGNRYYip6Twm4DwAwyPd-0mIKhKLAlSSUq19Gw84fpcBOf9XPe6uHq_S-eR4W6TfC85XwhekBe3vegANiS8N2aEKCn-5xm0kXJ7p-ph8faX-LV3gtTHMpBEUe9F0MPuQUT2Fna3u4TpHERww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا ایران پیش از انتخابات آمریکا حمله پیش‌دستانه می‌کند؟ | کدام طرف زودتر دست به ماشه می‌شود؟
🔹
پرسش از احتمال حمله پیش‌دستانه ایران، در شرایطی مطرح می‌شود که تهران با فشار نظامی آمریکا، تهدیدهای مکرر دونالد ترامپ و نگرانی از دور تازه‌ای از حملات روبه‌روست.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3251638</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/697603" target="_blank">📅 23:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697602">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxnLuqDvUDy5cSJobI35MKYnLOyHPxyM1UVTrsr1uxbGNZQ6J19D3H8xOM6cXgo_sXW4V2elTHTCYg9ZZX5145F-AhmthOmvftHFZqx-3PnBeNrz4l0CrInNxQGDQQM1w3QMlzeM-94lhnS-EFsvqQPu5ZTK-4ibQTplsXXV3HGMjge7Y7VsIkyJiAVpgKGg-M4oAdxc4xMj_h_B-eEfVPeFNX3hZeATnpueCm_iLvR6Uqk3hu5_a8d0C-pgJHxlJMrJgietT8i4mCW0UhehuzXkYKV95m3ADLVIOsrCTjvunOWEie2kMCVUjjgsY-_RG6gtOZioSHu_pNIiqhRdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چشم‌ها چه هشدارهایی درباره سلامت بدن می‌دهند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/697602" target="_blank">📅 23:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697601">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSLkHcsfEt3FlQOKy8jEAQKqfreQGem905hRdhpte8aCqeQSC-wKq_zueoxaC7EL2aloDTnkplJI9fVSRYbVCnNcR9qUSaDWBYBuTee1NT5eV1j841xQWAmakvz1pxTWqq7UvIqqZ_W0C8v91ByuFt5K0dgEYifNUje2lN2iJikAOAZwC1JcSyx4HBwAGyhoPbSHvqZ2BRlcfEbHShrz5IJQs9t5QvDxLLS3O6b1hrT8grtlbXCyIFbCFmxKKZQWor0-5ZTlM5U55oZVfUQIXdrte98kW_LuqIz1qHiSMNMmswlqqJUgvAoCdEwt3wowUifs7epCrarsuDqr8JSfpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای عضو کمیسیون امنیت ملی مجلس در مورد تذکر رهبر انقلاب به صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/697601" target="_blank">📅 22:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697600">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
نشست امنیتی نتانیاهو با محوریت ایران
🔹
رسانه‌های اسرائیلی از نشست امنیتی نتانیاهو با اعضای کابینه برای بررسی تحولات منطقه، به‌ویژه پرونده ایران، خبر دادند.
🔹
این نشست در آستانه انتخابات کنست و کاهش محبوبیت او برگزار می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/697600" target="_blank">📅 22:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697598">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/829439bcfb.mp4?token=g90GZwxvuJ37ozoXXRdG3k2xscOntWhD1GhuHNCCilCpYhhBwuyMi9TUxlIHRzFUgKLfQAZkfqRvNkw3RG-sdA-k9ij687zCp0YpS14nvdMaZLBoP_rVtXVmVH2XQYT4y_nMHAwkaxtQqnAZlCotiJHSSuxRP3YQ-pYfdcTnwsuoxh0l4kNerYUubAqHTnikULm8FQ_RgoLbN83pupsve0auI1VZvhTDvwHRMvWofKIDd2vu56_dQ1inxHvez_hcrNs-PAvie9bdnOYCNlbYXoboINDhmKuPAgu-71HDJzhMFrzbS1I-xedvx23DoL5adk9qgu3yD-qFFGTQbHj9Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/829439bcfb.mp4?token=g90GZwxvuJ37ozoXXRdG3k2xscOntWhD1GhuHNCCilCpYhhBwuyMi9TUxlIHRzFUgKLfQAZkfqRvNkw3RG-sdA-k9ij687zCp0YpS14nvdMaZLBoP_rVtXVmVH2XQYT4y_nMHAwkaxtQqnAZlCotiJHSSuxRP3YQ-pYfdcTnwsuoxh0l4kNerYUubAqHTnikULm8FQ_RgoLbN83pupsve0auI1VZvhTDvwHRMvWofKIDd2vu56_dQ1inxHvez_hcrNs-PAvie9bdnOYCNlbYXoboINDhmKuPAgu-71HDJzhMFrzbS1I-xedvx23DoL5adk9qgu3yD-qFFGTQbHj9Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوباره زانو خواهی زد
You will kneel again</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/697598" target="_blank">📅 22:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697597">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2db05af4.mp4?token=Z51Bc0aTxbvPkf7W0-8d8pLm0oTn2bGSKDkXkcGf14wReBPZHKMu1vKGRWCvDvct8b_ImVvGkqI_KXDYUvj8CcA4bAM6Aio551fxEgV3k-OB83N0JSNUlmbzjksyqjTjfAB1di803dNYo3UzaWL6uF-xIjc5wF4B2vevaFdK8Ielga_abF1HcKGq0Z56Pts0tgkSaFhply4qUoEFvZyQWu5XXliyfMS64B9D-L1KGkhLOlOiusPWwiMMnxtjROwNh16ULQnYJXnSW7rFYAROP8atOsHvmpWbTZzNiMan1bYyECo0Xc-nLG3QbCKYOjdHRuktYhtcHLoLfDYtlslQFoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2db05af4.mp4?token=Z51Bc0aTxbvPkf7W0-8d8pLm0oTn2bGSKDkXkcGf14wReBPZHKMu1vKGRWCvDvct8b_ImVvGkqI_KXDYUvj8CcA4bAM6Aio551fxEgV3k-OB83N0JSNUlmbzjksyqjTjfAB1di803dNYo3UzaWL6uF-xIjc5wF4B2vevaFdK8Ielga_abF1HcKGq0Z56Pts0tgkSaFhply4qUoEFvZyQWu5XXliyfMS64B9D-L1KGkhLOlOiusPWwiMMnxtjROwNh16ULQnYJXnSW7rFYAROP8atOsHvmpWbTZzNiMan1bYyECo0Xc-nLG3QbCKYOjdHRuktYhtcHLoLfDYtlslQFoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا مطلبی: دلسوزیِ بی‌حد، حتی برای عزیزترین آدم‌های زندگی‌ات، گاهی بزرگ‌ترین ظلم به خودت است؛ لطف کن، اما خودت را فراموش نکن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/697597" target="_blank">📅 22:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697595">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzxD_UyxnMLuCQw-jovJ166d8XVlsuoTr7z_vY8vH6-2wM-taOipv7QHeG0LL5HMUbPXc2aRga4cgOq9fB3UJUG85N_WVN2GvmM-7aTzNiM41XYzJYtn8hHYLioZw9xfhuWDK6MioQ53R2qQid5-21oOy9p0HSA12yQXATGym1yNeWnuc7NdFtwfDXgGjjUb5rL7NJtVUo7PX_NXzxOgPoNzNaTWhGNPZYKYTdNpaQL9u6atGc1FVMslIe8MTjoI2MC9A-t1PUkrBNEpKBf5jOJktaJVhYmjkTo7LmcnR0y2FVwUPkk2fZ2kKiPyQz54stIdsYWD0bD3qiKBdIXhIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sw_VVqZT2UNZVz8KONBkC3wlkNhXp9ECiepzgv4AfpCiKBHskjQIMRNXRinzUGM5bjAdej_a7dhbqVumiCSl09IrIfhleNMeJHROd797pcJpqUeO2hroJUUk0Lsq--7zNRBHb2EPv5HrMbgptqjktjmtkP_baznUjYtz2l1T3fbvS5P-VK1HWNPxW8fb1NMp_2PNOXoKXbE29EfIARB_cflnKtk7NUoN1XY3yolKH9SW709iceAaaqpexQlupOIPNVOauq1GYLHkKg726NpjykP1rtpN9esLAiHzBj38MBwp4a84HIRaP9yIwLbaGDLV88qhMemoxoe3CjtR8_A9CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سرقت ۲۷۰۰ گربه برای فروش گوشت در ویتنام؛ بازداشت ۱۲ نفر
🔹
پلیس هوشی‌مین ۱۲ عضو یک باند سرقت گربه را بازداشت کرد که حدود ۲۷۰۰ گربه را برای تأمین گوشت رستوران‌ها دزدیده بودند. در این عملیات، ۵۰ گربه زنده نجات یافتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/697595" target="_blank">📅 22:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697594">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
محاصره زمینی ایران شدنی است؟ | نقشه ترامپ برای بستن آخرین راه‌های تجارت
🔹
در حالی که آمریکا به دنبال تشدید فشارهای اقتصادی علیه ایران است، اظهارات اسکات بسنت، وزیر خزانه‌داری این کشور، درباره رایزنی با ترکیه و پاکستان برای محدود کردن مسیرهای زمینی ایران، پرسش مهمی را مطرح کرده است: آیا واشنگتن می‌تواند با همراه کردن کشورهای همسایه، راه‌های تجاری ایران را مسدود کند؟
نظر شما چیست؟ بیشتر بخوانید و کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3251621</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/697594" target="_blank">📅 22:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697593">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-MEcqlVWFB5WM0d0OJVL5GS3sHmUEl1ZN9VLpXI6O3FupXdQtvMnxd2XzbhmLeHYhSwTgOaM1W4eT-SMSGFsjPfl6ojsQW2rY_Pm4o8RKNbS-lDKijZ0ZCU4Xo_qBiAPUL2wS9hBFFIkRtDRBSYFwdX40DPeAfI6fV7to3vhXfFWMPC01M6suyc4xMKANyS_z3au4DQkGiJ1cYooLAX0TcYuAtrEQaKdhM8T0ue-khhz8ouJ5VOWKByrk_NvFsWSPqEPTVqBOvDSrQxhC0-jv2IwmjY-Cvs7JpH9tlDUG27x348tG88UMtys38bVUpG9bIQBObd7jUjo_SqUyWplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش قسطی شمش طلای فیزیکی
با پشتوانه
گروه مالی فیروزه
✅
بدون بهره
✅
بدون کارمزد
✅
بدون ضامن
https://in.firouzeh.com/gold2
https://in.firouzeh.com/gold2
🔙
مشاوره تخصصی و رایگان سرمایه‌گذاری
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/697593" target="_blank">📅 22:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697592">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATUu0KxwZYHvucECXHVM7DLZKRjeySuC8mHK5FoEOPKIMf_6ciez4ne-bNPHqJ2isi4XwqfSgc6cpHeZysy25elK3b_4UXVCtyYMUPdvfCO1PvfmAoNRwkakLGvxyQFtSTUDrBhLmatrl2GjRrzzkeToikfTKd5sscxz5h8aItEuymnw2vgpiEedYEWXmgtpf80CzdvYeLeVUxZgyON-oXLQyXeYzfy5CzwxNbvIZ8kSuujjqh0Ot1K1_gxzE7d6y6UzPL4I7N-neZkbLBGWe8-kMtl9UZDaWg_pVa00YY8d2tyHBl7k8WzkKM5Iii2qinpRkLPncwTrWxr1TjfYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای خرید ۱۱ قسطی، بیمه، بازار داره!
کلی هزینه توی سر آدم هست و همیشه موعد تمدید بیمه موقعی میرسه که اصلاً انتظارش رو نداری…
برای همین دنبال جایی بودم که هم بتونم راحت
قیمت‌ها
رو
مقایسه
کنم و هم
هزینه‌ها
بهم فشار نیارن.
راستش برای خریدش رفتم سراغ
بازارِش
!
چون فهمیدم تو
بیمه‌بازار
می‌تونم بیمه‌ام رو
۱۱ قسطی
و با خیال راحت، تمدیدش کنم.
👈
خرید قسطی بیمه، از بازار بیمه!
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/697592" target="_blank">📅 22:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697591">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZK3g8eF2tdOuSJsUEURr16D89SAGKsDefcdUIpiI5M5vqt_cHWOdJhxRjRA39aNWiDRtEbcEGH0B0p4nyUADkb_JdmOoYd-wUx2gMo7W_CzLv1C8hWMZ86Q_SsEStfdPwuErYPsPbW_n-WOknrAt-FnZVlE1iIc7wXs8BTMkrpCLiBz9T31AZDmpwnbpYVn5z0Zk1ZMv6g5ZPqK_75gzkjKD-O4HzGOL54NBBHWgF7qGIHyg9vJrPpEOkk7JrMa07-mMRIbNHJAtZRBcib0LT53RghGAk5YJv0hqgkFlLEHsUTODbXANw8kSkr3j8njRTncNHLUMLnPasGG0ro_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر خروج زینب ابوطالبی از کشور تکذیب شد
🔹
خبر منتسب به باهنر درباره خروج زینب ابوطالبی از ایران که در برخی رسانه‌ها منتشر شده است، صحت ندارد و وی در ایران حضور دارد
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/697591" target="_blank">📅 22:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697590">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec619d00b.mp4?token=slDwpwJpvfZu2XlUbT30NGem6Ya7w6dh1OCcy_wS4Zaf4xwlm8rEuhf4vDUTh0tzyYbTdReNoXDzmHF1X9rX1N-EaCvmndFZMqZQHKquZHfC8OpItm7I-8v1I5h8P0xy92Ur3HhalF6rBqjM-Z-b0zAif_vqTrXtib5oMkmXxePOcEkfEGC5NIcWa9mB1EOURKWJ37aj2KaPWFMx-XdUmqidsoa6VHdRuhPNpAUFevFW7_P6JrKHObhPpwqWeAcVs19dSIsZvTpCCFMTUyTdyPRoo7ZyPxrNsBQoevlwhYrOYo_duV6mifm38gJ1eJ0Lq9SmgX8EOFeBwTtRCmVUxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec619d00b.mp4?token=slDwpwJpvfZu2XlUbT30NGem6Ya7w6dh1OCcy_wS4Zaf4xwlm8rEuhf4vDUTh0tzyYbTdReNoXDzmHF1X9rX1N-EaCvmndFZMqZQHKquZHfC8OpItm7I-8v1I5h8P0xy92Ur3HhalF6rBqjM-Z-b0zAif_vqTrXtib5oMkmXxePOcEkfEGC5NIcWa9mB1EOURKWJ37aj2KaPWFMx-XdUmqidsoa6VHdRuhPNpAUFevFW7_P6JrKHObhPpwqWeAcVs19dSIsZvTpCCFMTUyTdyPRoo7ZyPxrNsBQoevlwhYrOYo_duV6mifm38gJ1eJ0Lq9SmgX8EOFeBwTtRCmVUxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌گرفتن پاوربانک، هواپیما را مجبور به فرود اضطراری کرد
🔹
یک هواپیمای مسافربری شرکت «ایندی‌گو» در مسیر دهلی‌نو به چنای، پس از آتش‌گرفتن پاوربانک در کابین مسافران، تغییر مسیر داد و فرود اضطراری انجام داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/697590" target="_blank">📅 22:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697589">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d71afbb8.mp4?token=nIJUqw9T58JGqZNcNPmn7X5L3wTxUj5rlDZnJJxjxSA0t42v4GsuQ9B7fzI6l7INt1qkfyNJFpL97HjmW9lRFQEJqIyULbgjQXzmuYTvlEDC1FB_sOt--7ohdDVoSb5ovNqqtlVUJM3RObvhMKizGNfTMLxoBfoAT79M4r9k0yAbeQsvPjfgNmxCZbPY7qKtPeY73J5BScTZyg0uH3vx3glZGCEitIxIwhZk61tgPoz3o_KHvMukLF7bFfWJMKymtNI2MwIbq27LFH-VIS8tARWTdnVCYfkV7xVoK0fnV2Ds4nYP2brYyQFgd1aj287TU4UTk9jf5d9mDSCZzXgAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d71afbb8.mp4?token=nIJUqw9T58JGqZNcNPmn7X5L3wTxUj5rlDZnJJxjxSA0t42v4GsuQ9B7fzI6l7INt1qkfyNJFpL97HjmW9lRFQEJqIyULbgjQXzmuYTvlEDC1FB_sOt--7ohdDVoSb5ovNqqtlVUJM3RObvhMKizGNfTMLxoBfoAT79M4r9k0yAbeQsvPjfgNmxCZbPY7qKtPeY73J5BScTZyg0uH3vx3glZGCEitIxIwhZk61tgPoz3o_KHvMukLF7bFfWJMKymtNI2MwIbq27LFH-VIS8tARWTdnVCYfkV7xVoK0fnV2Ds4nYP2brYyQFgd1aj287TU4UTk9jf5d9mDSCZzXgAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار عظمایی فرماندهٔ نیروی دریایی سپاه در اجتماع مردمی
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/697589" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697588">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/697588" target="_blank">📅 22:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697587">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
گزارش وقوع حادثه برای یک فروند نفت‌کش در نزدیکی لنگرگاه صحار در کشور عمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/697587" target="_blank">📅 21:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697586">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN8v8SrfGjtFwXC7eiHpXmedjblwr-6Ng5_k7MK0fKxSe6c6E3kp7tsNjH96rWSacAm2hraroWHWGSTZJcIX1bNprMwzEb9Cvb79VF2vulkHA61TriFOVPVQcdupW1YZ0QJ8sy4g91H-yLngFqIF4EEOp7f_wvx1-25VP5CYIZW2tGMjJhw2KQFDR59ddIrx5P8f04gpRiv7rVj2wH-R6pi8wFAZTAJAQOYn4qDtABppVmCPF98O1STkdiKDbL4Yr3KzMB_2__f4HaKLsrmAVkEZzb6fBfcF8UsMPgp8ndsHXDm5rjKF8thkzbfkKysWd-00zgTxWleLBIN9ykl5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رصد پرواز جنگنده‌ها و هواپیماهای نظامی در حریم هوایی عراق
🔹
۵ هواپیمای سوخت‌رسان KC-135، دو جنگنده F-16 و دو جنگنده F-35 با مبدأ پایگاه‌های اردن و اراضی اشغالی، دیروز در حریم هوایی عراق پرواز کرده‌اند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/697586" target="_blank">📅 21:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697578">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8aoxTygta2TMKib_czugoEEADE5BWAEL-jHHUH1bUhUMce86RdlGG0g4NOdYcoWQqoziPR_A3ub2qxZgr_VD9pY5lrouSnpQn6Rj9Gw5rdYjR6UwUBS_wruOJRYozyVOEeSlquMPpBGxCwd7_UZoVjVVGWImDmQAUmWavi4rPWVZPLHU4OzTurCkrKmYzHdKLyliU1QD1UfYhDf_fyIowcs_C1n0in8meD0l9dJpd8I8EVaqNEN2hdJHXuYFvJEn3k-ePCNPQur-7pTjX0WtApxl-f4HBAjaWxHPvfJyEvkMpGUfF2Wz2yd0RwVJzxb8XqY5Lk9IYt2apFdMXBjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NVNYbaci962S_Mk_4HCJvonp8Br0wbgpKhVnQeRWzrDb3TYhRuJK_CR5fUoca9ylRA5BgQSxa1ATKeSr5AWqPdJcNW3aALh5GdKW1G4EMcnxLrwKngeEo0gHwWEAgSyeKDlieo6jnGbl0tUOAWBT_WpcV-Ar0fQ6xNzhXXJEdL_SPvr0KMk8Ft5fGqocmCZkOXh3v5KW2ervMXndSUI1vIAh2rxlSM5My1Td4_NWgT1XS7m-fOfIpQLOqc1_eB2ZMwm60QMLhRQv0cBYmYm2TTpM5jSdNolBzNdeeswqcVWuSvbw23k4HxkulTCw0XTcma3UHIxX-ucYjO9-2GbOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqAIP8lEx-aIQlzZMynwDCyQ_BQY9iixHFz_PmRFIdsQSodcDdZI3-2Keye9xCMhYh-upDUH1VFwajhvym32PxMKNUpvOnzxw_IrrBdB2bq685Um3GL9_m3qrFMIq4edaP5UxGVmVEgShvHQiIie0HKrkopGZFJnI7gAxwpajIsSqZnkl_zWrmyrF7P5h9ZWKfasOyI8NT0m-AgCgqrX-rbRf1Q36WNnfq2Cu3GN7XVEu_6F_k7E8CP8KcnL7YUn9-T7Mz7vyZf4V6sYNu4weve5_PBil8LJCBbyyrxh4iQCR-GI2Y5YhkROjMdxi7WFuyP3r5FzxFYpv4E9ghskGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhQ63qjWSOcts8Ddt6v9Od3tVMVbxCuZu2lqw5CTv9w9jL1ZXkvDNpUxpWPEpWLeIu0Ihihj8BdgXoIFNmnWF562UQ-f2IH6ydXdYnleLIIXB4Zv8Lbkd2W6ZUuUZ-Vo6bcIlyRvTRpKcFYwyYDp9UFfu9m7GwkoR8S5eoTGxDNSPvHtsFzZsomTodE9X3WetctBkXH9xtD8FD8j15lnScgHHr6YBxyHRKv5luTQDEu3i3dohCwEGi4Ebd0FF0_2QuBmU0iGC5mXhj6ASqvXqE-WlLbAab1zXvmHpaehSoTJ7K_NOzTBr826KnjYBLOINw8fcqD0mfFYanm0FmARSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDUE941fI43_qrwWek6zcMu4edBR5FZcfvhDsT8y_08BUWtdai5u1-mMy2g5Hy8-VOfQHOjz87TUSvXiEtmX56vFGEwHCE-dVw8czl9jPLRjql7Oi0VXYyVKuFB-Dy3Jp_VPavdXWCfn5k-qC33kNSzKKimeGUb--s2lP2AW8j655SjAOnJF4ZTjtBRHB54Zk42pxoLhbFUsbKvbKz9YO7xEZ60vQi1Uj54eCo8OA8ZLI3heO-8VoY88JJDEXA8YzwiXEtKuaEfZqrdOl0EN-h_d54g-bmYhUm6U5tcdqG6rDybAlX63uhpzteYc3IlA22VNpZ6kQZfd1LAgrqvtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBN2ko2JJW064JgN1kMkp1Dy7QL46oh9QpzLa58VPlBNWmYi7I-1khmr4ZIYOA84DF7if1C6qPM8JGt9Sl8ilMTwL4pNh_qty1EcUwWX73YdbhGk6oX9npAlg3IYfSU_u3SYhGTkhR8To1kz0naNk8gibDn4e1NdK9Y4Ik1gs49owux15m6jJR3FZDgKA7SP3jLwJdRqNHjowSU1ZCt0IHLGY7ZBaPf_J6jhGThRDXzU9Bo4ugwBAJnk56DWELbuQ0cqE6dCFexd_WTdkLiNm0BHfsBpUqM2OGzDD1Cv1dkXi8jAbbCICYRyN6MS6FbUOpzgl-s9L5RpNtrVaupwZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/splocHU6fGrgU5p8i8LvskWLLcjFbKUvm98wtIzXyyM_OToRNSBZGPr-1vtgSQUuXBDqZBqo6H88qZW0U6-FsZkxlqupkCnvw6MMNu6R4-CFfZ7emQEsZQYu63J4CDQN08_ZN1Nicul9PP4pVUiqARQuQnVwjwh1TIzaRZFA5hXDCHTWEJxC9KtuxkEZERlF0_7zCN-AiDkVdkoBRZFHofCl-zeBq3VI4rQK-T0F8snOCGap1fSwOF74KEd-nanNJf5hhaBU8UGwL_ywEiX7X5rMfizHW0G7aj0Z3oo3cv99RGm1AFtwNvjlN8ClWApuCm4-ti5ezcti-rkKpa7Ohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9zQpokKO6w_pcrqs-xSzuqlBmpaIsnPp03EWGw3Yn9fH6fFpAsRKvSHSugh5AH0B11wING3kAJPvaqFDgbMq4oFma6QFRTIf5cAMGTYQQtDFkNIR3MYz47fg7QzPnEqpl38feO4wmX3jcL4r6ZONG5rzDuTgXSFRMJfbtCqJjkA6LJA1u--MGjq7f7AjUtf9f89CN-qLhOAIdxlEWE948AX93gAwrCYV1gph93s2vIbUjaWxr74k8jaA-wgnZz3sTbb8yzeYpUJXV1yzPbIT28CVBMFk7MpMKbNwgudG6iK135LsPabd5rs-kcTIlVx4zsK_tXjJZf3FQKIhfHaVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با چندتا کد ساده می‌تونی ادیت‌هایی روی عکست انجام بدی که معمولاً کلی زمان می‌برن؛ از تغییر نور و رنگ گرفته تا ساخت استایل‌های متفاوت با AI
🔥
#هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/697578" target="_blank">📅 21:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697577">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a5a7390.mp4?token=VKG4GnsPH1q19ZNkVLubUz3KCMhHGdy425yzRAQ6H_a8rYNQzlBxuMoKcBvAeo6tgo0TrOjR7jyOff7vgSKnq3j3HluPM9LSRNMp1k0NfRcZAIMpC20_d3UpHcPkXT6fXSaxK0CwT_NdhZfDwIH9AOjWO59kQYLdd44o_9yCyapD2Wr8fctb4GTy6uC0chH5x_xSSaTrw4NyhZsxRBWeMikxfsuoyPcjLpe0QMhCWmQSlbpIuTJzEVe2m5kHFhQ2rg8vjmj26Wyy7xIpGlBI7IDs4BW4J1Ex15vqeO5spX2YU-nBTgnMj6LX4ckkbedYsGR9qV7hr_gSZSg8b8j_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a5a7390.mp4?token=VKG4GnsPH1q19ZNkVLubUz3KCMhHGdy425yzRAQ6H_a8rYNQzlBxuMoKcBvAeo6tgo0TrOjR7jyOff7vgSKnq3j3HluPM9LSRNMp1k0NfRcZAIMpC20_d3UpHcPkXT6fXSaxK0CwT_NdhZfDwIH9AOjWO59kQYLdd44o_9yCyapD2Wr8fctb4GTy6uC0chH5x_xSSaTrw4NyhZsxRBWeMikxfsuoyPcjLpe0QMhCWmQSlbpIuTJzEVe2m5kHFhQ2rg8vjmj26Wyy7xIpGlBI7IDs4BW4J1Ex15vqeO5spX2YU-nBTgnMj6LX4ckkbedYsGR9qV7hr_gSZSg8b8j_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعضی همکاری‌ها با یک جلسه شروع نمی‌شوند؛ با یک گفت‌وگوی متفاوت شروع می‌شوند.
در گراد، ما به فرصت‌هایی فکر می‌کنیم که هنوز شکل نگرفته‌اند؛ به ایده‌هایی که می‌توانند به همکاری تبدیل شوند و به ارتباط‌هایی که شاید مسیر تازه‌ای برای کسب‌وکار بسازند.
این بار در شیراز، نه فقط برای معرفی یک برند، بلکه برای شنیدن ایده‌ها، شناختن ظرفیت‌های تازه و پیدا کردن نقطه‌های مشترک کنار هم هستیم.
اگر شما هم به امکان‌های تازه فکر می‌کنید، شاید این دیدار آغاز یک مسیر مشترک باشد.
گراد در Shiraz Expo 2026
|
📍
سالن حافظ | غرفه‌های ۴۳ و ۴۴ |
| ------------ | ---------------- |
GERAD | G NEXT
www.Gerad.ir</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/697577" target="_blank">📅 21:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697576">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
🔹
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/697576" target="_blank">📅 21:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697574">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
محققان: هوش مصنوعی و جنگ هسته‌ای می‌توانند تا سال ۲۱۰۰ بشر را منقرض کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/697574" target="_blank">📅 21:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697572">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای ترامپ : از همین لحظه، در جنگ میان روسیه و اوکراین آتش‌بس در حوزه انرژی برقرار می‌شود؛ هر ۲ طرف توافق کرده‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/697572" target="_blank">📅 21:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697571">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuFbTtKopCj0_XqNonGmlBPb6xZxOC0f2QShPj8o6TAziXDmcwDxMkSsR13l3-zc7xDLbcDV5CCl6BSypM6NgCseQJZq9mGeZ2E9Kh1fZd6YbpVWz6B3H4dMmXAb2KqINEC58W1jo3PJohVMxw2mopDKqLkXgq6xM3crTP1ZQCO2RE5_k_QpfWsSFKsyMG4t-6OQEtfVaEYnzzQBwD1751RU3wALNLBVtITO5JBm_3ryy5X9xoQnS_v95eosBzOCfbDX3cuqI4WRxHyIEiJ6XbivX1DX4HMHZMTIjwr3e6PjmvMiglSvA8cD9BK0CmEDD0-GoeNjXPeYtC4uRuFalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از دنده اتومات چطوری استفاده کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/697571" target="_blank">📅 21:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697565">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOKP_BwCRncO6z4_TAqKZoY5a2qWRN68UXyHehJYmem8lX48mrfML4Eo5x7nV63uLFHtvGFgA1RT6aTrt3_4set4IYoqE9Jpg7jEaD3e_CIPRMBA8NOTVk_oR1RnuUdUV2zIEyrjLUmsXIWzXL6w7yedQnDF3KpWw4gtbF8Ge6IdtJpN1HckprfA0GWiHRAl8KCq_vyEmkFkCBq8PoRJEwhK78673VN2VDH2kvohdENq86T-sEu3dUyN3_4dwXvp0OZXgrhixt5Lq_14jpotLdQWHmzIfTtkpFcANV5vLCzsRWSayrerJuoOTKbP3KSX0m6si9PVs2VZdsMdtgpfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsICzV7j5ewKDrX64FgZT5pul1vwMmuIHdG3Rn3U6fUPQ7UFeW9idcyZ5TPxkrmSljKvRvsLtrDjLOCU3AHyrKHc4Kk9dqq8ZGaMchNCz3iBFiNoZs1Umevb04FxSAywBVRB28Po9AbVLU-jMw-TrqChOWEjqKcKcnZK9x3WSHTg25Hra3PW7QikFusyd5ZUt9icbpD7aCw76LV5CPV3vohyAegd_k67hGAEWzKOgTmDHeAx20wwCoU5dJFAQZpua30z5b1N6t1bN2XEFXIIIGooJVpHb-45JoCRUBJGxqny8NCtrgH4teipl0d8TtUVid3ylFkPsnLe4FXzWz9ZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UV44nkwG6entJLXsyvikRzbgiDyqxH-XOPt0lTIOqZzbyKT77SM50UC7XFsn24LWFZ4F3TgRUq2oTIw8cXJ0RyLyeR3_MvYghhvcpNLR-_SSEvoMTOIJOw8wKWpNG81vELWgYFuSIi-g9KPoO2M7q8Oo0giiqXopckxJ3hq4IlP_oCeyPdQREY5xFD99lWqGCquhMR5zARoGRIKjKhFxxk2TimOgxaez8ueOUx8T25cv8n-r05Fuj9c-4RoA5qC-Kz02Idi9COeN7e-W-l2mYQtUw6BsrRiJzBO_XLDjBCB9NX7aa7ztksYinkEhtAfLJDTYmnShCZ-PUVK1oyGSJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2e4wWjTgGXwDNgQGrSeuy0LFiyv_R_OSudFGu7bJqudN4etkimLJ-9n5r2Rd8pw_VUTQXPWqeV4YLYYt-pHQ7qSkLxfkoYEElE34YpgkBkzXs40MPccjKhGSSZ1YiB81WhdBYhGoyhg8o38npG-dxrXlBdtnSrxW89E9dU_nggbQZHFFvSRMBm5tPvmwq0Qy632d0PJdTVyHMTBWKEyHGFG-L58zTPg8nTTWOqXpQcSHRVZZfGWx2PJfodGBQn4kBbgclwrUP867yfckR6XI1CSZLtpLoO_aS4nYb-X-McyHZVvqaZHuXHqHvsiz6htUdGK_8p6tjRn_BKOtOwW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QB1PC9tFRiJWOYuM1XK-j7-libUmeyQlENf1VcN7ueBUMEyteEv_oghTpd2A6pBaHTSLJI8N5O2sapCRLH2vBDmPzgJW1DT7IfkN5ES1ItEmk0StvrZ0eM2zAdoVAp-sqCqhcChiQUMwgbrSbIcHZlpEKdEObpM13uVR2Li4hstNSxz7hTvXjp-mvw3ZPf9ht32SURQyIl1sbpGggqz2Df3Vs4uZsLeC4xoCWxRrUFj8vzXjkDTLTxGdfUFvQDs3zlEVlf9v-dkqFVZtMEvF8ipGFo-bIPUE62oXJH3dNI5okaUWaAQCv-AxuXo4yqs82q--jCIntHiVL6PuUodrfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
"پیام محسن رضایی و قالیباف خطاب به وزیر خارجه آمریکا" روی بیلبورد‌های شهری
در مقابل ایران زانو خواهید زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/697565" target="_blank">📅 21:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697564">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مرشایمر: به نفع امارات و عربستان است روابط خصمانه ای با ایران نداشته باشند، امریکا دیگر نمیتواند از انها دفاع کند
نظریه‌پرداز علوم سیاسی:
🔹
از این به بعد هیچ کشوری در خلیج فارس جرات اقدام علیه ایران را ندارد؛ ایران خیلی قدرتمندتر از همه انها خودش را نشان داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/697564" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697563">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92dec01ca3.mp4?token=j2rLeCH4WI2As9qzTQCSfGxE6s-gF1vRytM2IiNFzvjjTP-Uws3DhzJN6SEJoFDrpGRI5xhFNQuC17HxTE8VjF6H5y-4y14mhSSI6qLPk6fFb32XolwvLNB2W8CsNcJabpNc1mgzkBzTAqhaw93IYSbtZCtgKRdDGyPpb7Rx1ITAbOWOwhEpSr9TA77dET-DX00kFPO11pZQpAJgFqIPY5eeKOOsDINvOBXqx5waYNAo4zItojgH4BgjZtZX8me8fDN08On5RmIx1czbVf52tIT5-ykVCRv3VHRrak8u2ycmduIVGRfpeAUeBGK6ixx-v5WJObns95JeEir8l_Jqzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92dec01ca3.mp4?token=j2rLeCH4WI2As9qzTQCSfGxE6s-gF1vRytM2IiNFzvjjTP-Uws3DhzJN6SEJoFDrpGRI5xhFNQuC17HxTE8VjF6H5y-4y14mhSSI6qLPk6fFb32XolwvLNB2W8CsNcJabpNc1mgzkBzTAqhaw93IYSbtZCtgKRdDGyPpb7Rx1ITAbOWOwhEpSr9TA77dET-DX00kFPO11pZQpAJgFqIPY5eeKOOsDINvOBXqx5waYNAo4zItojgH4BgjZtZX8me8fDN08On5RmIx1czbVf52tIT5-ykVCRv3VHRrak8u2ycmduIVGRfpeAUeBGK6ixx-v5WJObns95JeEir8l_Jqzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازهم فاجعه در فوتبال؛ کتک زدن داور این بار در اصفهان
🔹
این اتفاق در لیگ‌ زیر ۱۳ ساله‌های اصفهان افتاده است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/697563" target="_blank">📅 21:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697562">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5fee01983.mp4?token=BFIjz2nBF9kjZT4YZ1f8FfPqrP35TNeApnVc_ofgCWJ1O0q85V8qbsAVoSaDhAsXSTvo_0G5fB5oUtNXftKxIalA7a52gvL-GJgD8yTt2VhaYfWY9_8RjFEGfK4g0_CN2ldiECbZaRBCruPw23VpFSZZ3vs27B0DmBpheVpjHpQK69FLAWiL9sjw9nYQqr9wJDUeYJIN3UWzj3Tg1ZYH0lnNeSI4PBk-1rI7eg7ueLyuE87afVyjI5Yo1GlQfutISLOn9APOf27hs4OnfD8yqMHWAlAVf1DU5M13MKe8CipLs_FvEui7z0NgtIzJCN05gbu0AiZ6nlmOOdi5cc1d3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5fee01983.mp4?token=BFIjz2nBF9kjZT4YZ1f8FfPqrP35TNeApnVc_ofgCWJ1O0q85V8qbsAVoSaDhAsXSTvo_0G5fB5oUtNXftKxIalA7a52gvL-GJgD8yTt2VhaYfWY9_8RjFEGfK4g0_CN2ldiECbZaRBCruPw23VpFSZZ3vs27B0DmBpheVpjHpQK69FLAWiL9sjw9nYQqr9wJDUeYJIN3UWzj3Tg1ZYH0lnNeSI4PBk-1rI7eg7ueLyuE87afVyjI5Yo1GlQfutISLOn9APOf27hs4OnfD8yqMHWAlAVf1DU5M13MKe8CipLs_FvEui7z0NgtIzJCN05gbu0AiZ6nlmOOdi5cc1d3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف قرارگرفتن یک کشتی متخلف در سواحل امارات
🔹
به‌دنبال صدور بیانیه نیروی دریایی سپاه درباره انفجار نفتکش متخلف در خلیج‌فارس،‌ امارات هم از آتش‌ گرفتن نفتکش خود در این منطقه خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/697562" target="_blank">📅 20:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697561">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04822bdcc.mp4?token=acQDceWyOlDHUBaoCu2YtDBAv2a5fUG4hzbb-V2XRYLm4qrxDMEdCbQ-ydueFJLo5jMIJF44tAtTXRCEGndwKygkQyIEWrcKSsp2qipQESusedFc65nzBhf9RomoFDjWadZiqst3VAqfgeSAfj4UC8i9NxuvpXqDuZrkh26owMq97JmoDrXCcWtCp3t0VHxOnNiRzCz7Deb0ScfcUmHHltbUQQQ_SGI0trgb-jT8L8Jg2IaaRVs1GM7HXaeDSqtY3c7CvzSdlw1kvukgo_CLRPgkPBq5KxK9LUjIBTp9OdulcJ9u8M5yIW8cmHMY-Q0DP4aLdvGvUt0tFx_RRtGDyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04822bdcc.mp4?token=acQDceWyOlDHUBaoCu2YtDBAv2a5fUG4hzbb-V2XRYLm4qrxDMEdCbQ-ydueFJLo5jMIJF44tAtTXRCEGndwKygkQyIEWrcKSsp2qipQESusedFc65nzBhf9RomoFDjWadZiqst3VAqfgeSAfj4UC8i9NxuvpXqDuZrkh26owMq97JmoDrXCcWtCp3t0VHxOnNiRzCz7Deb0ScfcUmHHltbUQQQ_SGI0trgb-jT8L8Jg2IaaRVs1GM7HXaeDSqtY3c7CvzSdlw1kvukgo_CLRPgkPBq5KxK9LUjIBTp9OdulcJ9u8M5yIW8cmHMY-Q0DP4aLdvGvUt0tFx_RRtGDyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قهوه رو اینجوری بخور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/697561" target="_blank">📅 20:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697560">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec4ba8b0a.mp4?token=MtKrrhBuhBFeAuPSGMi2GDVjNQHY2g1eJggetX7XqjueoUngODKGJutPt1oOlz0AYIjwZHBanWOJ_IZ2d2Ph4RnSWNtz9E8QfAMozCzsdWYve40z-Jpn043Ijg-_o1FeDl39P0ZQx_QItgCYlvXZo2ICGnUHSUu9DPL5FG3bDX1Wrb6udooQiRxgOD9twp2FO_WXO-gzIsvAJPnmU5dozPID3rxXRajse4XRmzbGKgWdv0-M8T6sGD7LARG5EJoes0cqpMnM9DdVv01FhtZhYNRpwpMEyJ7ImEbHmQ0tMGay4oAMII8XsB71WKhbF0dSh1GPBgOC1x5rDJoeoMBwJh_K2K2dxoe16NzfBVZI-KEc11_R2hVkhlASvzAm8h_Q6TPQyD9SHeHutqfixgXCl9jvoQbwo_sVfHbYP4uqR1Vqe-DkImVTpelUMBHu0FYzAOR3bQAJn4M91w2aAsq-q7H25diTGP-jHVUqxHgLsHqnXmRT0eTT06UETRTS-DPWW8rB0M5a6kEbM12iveUnP9BuM6jx2naRJDLXZWCmOAtzDGISitlbFCmLU1tPyDX9wtxEb6B7Xv6QrnEUYyggHFNdVvT8stzkQoGi_23ZEjT5mqqfyGUt9ioUWLnF_2EtqalWvt1xVIPOkHjgC8-zm1Xf4_vX-mpStpy1pktfbZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec4ba8b0a.mp4?token=MtKrrhBuhBFeAuPSGMi2GDVjNQHY2g1eJggetX7XqjueoUngODKGJutPt1oOlz0AYIjwZHBanWOJ_IZ2d2Ph4RnSWNtz9E8QfAMozCzsdWYve40z-Jpn043Ijg-_o1FeDl39P0ZQx_QItgCYlvXZo2ICGnUHSUu9DPL5FG3bDX1Wrb6udooQiRxgOD9twp2FO_WXO-gzIsvAJPnmU5dozPID3rxXRajse4XRmzbGKgWdv0-M8T6sGD7LARG5EJoes0cqpMnM9DdVv01FhtZhYNRpwpMEyJ7ImEbHmQ0tMGay4oAMII8XsB71WKhbF0dSh1GPBgOC1x5rDJoeoMBwJh_K2K2dxoe16NzfBVZI-KEc11_R2hVkhlASvzAm8h_Q6TPQyD9SHeHutqfixgXCl9jvoQbwo_sVfHbYP4uqR1Vqe-DkImVTpelUMBHu0FYzAOR3bQAJn4M91w2aAsq-q7H25diTGP-jHVUqxHgLsHqnXmRT0eTT06UETRTS-DPWW8rB0M5a6kEbM12iveUnP9BuM6jx2naRJDLXZWCmOAtzDGISitlbFCmLU1tPyDX9wtxEb6B7Xv6QrnEUYyggHFNdVvT8stzkQoGi_23ZEjT5mqqfyGUt9ioUWLnF_2EtqalWvt1xVIPOkHjgC8-zm1Xf4_vX-mpStpy1pktfbZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاح کشتار جمعی زیر کت مکرون
🔹
رئیس‌جمهوری که برای ترسناک به نظر رسیدن، به‌راحتی آزمایش اتمی انجام میده و دنیا رو تهدید می‌کنه! اما واقعا چه کسانی دارن امنیت جهان رو به خطر می‌اندازن؟
🔹
جزئیات رو توی این ویدئو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/697560" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697559">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YccbDzWAFyzEd-19rY_xMa7c9-YyJjNNrdF5zxcf9QdbinUNnkkkljvQ4Is8hiNkbiS3BzdyJ_p-rbiUfAAySV1X383kSutW2VclTsL5lZXClwxavotmmFhtmM2ll1rjUZAUd_D3tZpj1hQyBThr3ws2P7g6Vs4MdS5AGHwgchD9mkUiv-5kvXUwb0eXnZUJ7PYzLlb8bE8W7UCHrjRIicLuW82wFULWbwVVeH0jdsIkoFqLuFOy0zXMLA2_L1x0BntgSGYbANsEx4VFPIhBxnQZIvIZd5oqCcangkh00rncS0JElIHvm6UBHjas5wYssDTiswuknrEA27jP7YnZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان صف تسویه در میلی/ ۱۳ همت پول به کاربران واریز شد
🔹
میلی از پایان صف درخواست‌های برداشت کاربران خبر داد. بر اساس اعلام این پلتفرم، از ۲۰ شهریور تا ۱۸ مهرماه، بیش از ۱۳ هزار و ۲۱۳ میلیارد تومان از مطالبات کاربران تسویه شده و ۶۹۶ هزار درخواست برداشت با موفقیت انجام شده است.
🔹
همچنین ۲۶۳ هزار درخواست برداشت از سوی کاربران لغو شده و تمامی درخواست‌های معوق از طریق تسویه ریالی تعیین تکلیف شده‌اند. با پایان صف، تسویه درخواست‌های جدید طبق روال عادی ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/697559" target="_blank">📅 20:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697558">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c020369ef.mp4?token=oxO_C6uQ9ce_E7Satgz5PQrQk_lXJq6CzrRq6gqnBl6DG0ytoWgaEKoSXNUF6TQAlvTi9sg8oKlfUu3BqxJKjYhrH-DrjehM24r07bqUK-zYyK9JU4F3lLDKtYYXM9vDl8FeF8k9_TFKQz_P1VqQgYb0QY6_HYMx3JTVWKksKsK-V65Pos73h28iHD0VpZQY9alhsfkkihIKxsEZvAvJZ5qQfj_aAY0fqupuLBLNFqminZTMCRVLNt3aqsqnDbKUCCHUo1mHxX2gUmiTNUz3GU7TXIYrUzF0BMUynFZzAYy98Ez-CLvyjuIUqwSAWI8gRc3Ro7UshJMCs7Ssc9DjJamhS3nqwt7CT8RKRNSqbSIkHQecTndpwsUdSNVWlV0R95RILbi3Pe3cle_FIqin418wSe72JZd_6jSR8VFORCMLumPTSXmhP4q9fzsWx99aQeA82TXhILbexLbNTt3H53wHxn26OyXuk6kUwjUTXxqzAGjyczqdC4C86RGferpUezy7OQJ5yOzfRTc-SSXjGcc0j8huS3Rh-x5y16NdyijZasXKVRiXmR9oBgM9_z3hmTSopB0lG4r5XBQ4FGa3vdxFagzTUKZaL0yO9gBusclVPgbAchMIlBVFhFGLG8vqwsjjzAuTfITLLXdz2Vi_PbfOdLjMosqyGFdv7kMSnyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c020369ef.mp4?token=oxO_C6uQ9ce_E7Satgz5PQrQk_lXJq6CzrRq6gqnBl6DG0ytoWgaEKoSXNUF6TQAlvTi9sg8oKlfUu3BqxJKjYhrH-DrjehM24r07bqUK-zYyK9JU4F3lLDKtYYXM9vDl8FeF8k9_TFKQz_P1VqQgYb0QY6_HYMx3JTVWKksKsK-V65Pos73h28iHD0VpZQY9alhsfkkihIKxsEZvAvJZ5qQfj_aAY0fqupuLBLNFqminZTMCRVLNt3aqsqnDbKUCCHUo1mHxX2gUmiTNUz3GU7TXIYrUzF0BMUynFZzAYy98Ez-CLvyjuIUqwSAWI8gRc3Ro7UshJMCs7Ssc9DjJamhS3nqwt7CT8RKRNSqbSIkHQecTndpwsUdSNVWlV0R95RILbi3Pe3cle_FIqin418wSe72JZd_6jSR8VFORCMLumPTSXmhP4q9fzsWx99aQeA82TXhILbexLbNTt3H53wHxn26OyXuk6kUwjUTXxqzAGjyczqdC4C86RGferpUezy7OQJ5yOzfRTc-SSXjGcc0j8huS3Rh-x5y16NdyijZasXKVRiXmR9oBgM9_z3hmTSopB0lG4r5XBQ4FGa3vdxFagzTUKZaL0yO9gBusclVPgbAchMIlBVFhFGLG8vqwsjjzAuTfITLLXdz2Vi_PbfOdLjMosqyGFdv7kMSnyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/697558" target="_blank">📅 20:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697557">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
تغییر جدیدی در روند مذاکرات غیرمستقیم ایران و آمریکا رخ نداده است
🔹
بررسی پاسخ آمریکا به طرح ۷ ماده‌ای ایران در داخل کشور ادامه دارد و پیش‌بینی می‌شود این پاسخ طی چند روز آینده از طریق میانجی قطری به آمریکا منتقل شود./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/697557" target="_blank">📅 20:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697556">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
بدون نظریه اینشتین، مسیریاب گوشی شما روزانه چندین کیلومتر خطا داشت!
🔹
ماهواره‌های GPS با اندازه‌گیری زمان حرکت سیگنال‌ها، موقعیت شما را تعیین می‌کنند؛ اما ساعت آن‌ها به‌دلیل تفاوت گرانش و سرعت حرکت، روزانه حدود ۳۸ میکروثانیه سریع‌تر از ساعت‌های زمینی کار می‌کند.
🔹
نور در این مدت بیش از ۱۱ کیلومتر حرکت می‌کند! بدون اصلاح این اختلاف زمانی با استفاده از نظریه‌های نسبیت خاص و عام اینشتین، خطای GPS به‌سرعت افزایش می‌یافت و مکان‌یابی دقیق مختل می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/697556" target="_blank">📅 20:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697555">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
مهلت انتخاب رشته کنکور ۱۴۰۵ تا پایان روز دوشنبه ۲۰ مهر تمدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/697555" target="_blank">📅 20:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697554">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e933c02e46.mp4?token=Y3QYQ_piPHfiu7spwZuEQc9g1oIA-UqU1VKZYLWWncqB0jcWnRvLXgrabhk-vZqPMhMd7Nj76N5g-gIsJSFACV3gOKz4mISQPquepNbGVV0L8X628Ca2kWaISdCzF4saK9Rw_c5d8HSj2f6YZAKtSSrsyTPboz2vpPAoKarcD3pzAjYho3skJrM2aI7Kprlb-4BQ-hKQkiTu8Q47Nu1C82ub4Fw_iiRvixp2BCXI3eb3MIQxm2gx7WsMXD6kl73KjkQICMW3xA95SPK92lAPSozE-Hm6zrshgcv0bDelCLJUnw8iFue6YUJfE3ifNqgRPGy-EYq69Ir23v_uveqknQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e933c02e46.mp4?token=Y3QYQ_piPHfiu7spwZuEQc9g1oIA-UqU1VKZYLWWncqB0jcWnRvLXgrabhk-vZqPMhMd7Nj76N5g-gIsJSFACV3gOKz4mISQPquepNbGVV0L8X628Ca2kWaISdCzF4saK9Rw_c5d8HSj2f6YZAKtSSrsyTPboz2vpPAoKarcD3pzAjYho3skJrM2aI7Kprlb-4BQ-hKQkiTu8Q47Nu1C82ub4Fw_iiRvixp2BCXI3eb3MIQxm2gx7WsMXD6kl73KjkQICMW3xA95SPK92lAPSozE-Hm6zrshgcv0bDelCLJUnw8iFue6YUJfE3ifNqgRPGy-EYq69Ir23v_uveqknQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در نهایت متوجه میشی که مسیر سخت، تنها مسیریه که ارزش طی کردن داره …</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/697554" target="_blank">📅 20:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697553">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e753101023.mp4?token=b8hyg6gaiR-06qr9yn5rstgP18bcuD-ykJ6viwlKHKFZFTBLoLdq-fnTE1evGv6pp5VFOFiQy6tgOmjRqzjt1gnWbOsFq8wMngi9cfcQKKeMBTXPD1txfo5ve5ycr6ino0omNWMTN5AT0O2uPfhFHd34brdALQQ4XI-LOydfIrMqCqitTN0OXGf0josKCxOqPS9aKba_pNQo8snKRcsCw7aVnupUnxd4fJhNF5g6wOtEYrEmPpuZa1pwt2XDIbN1PHs20lNBuXP1rQ9obKlOWRaQ_XHPJTAErNv5aOYv4BUv78odRB1ksoc0mHrM28tok85btTZtPv9hqwUGk1PSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e753101023.mp4?token=b8hyg6gaiR-06qr9yn5rstgP18bcuD-ykJ6viwlKHKFZFTBLoLdq-fnTE1evGv6pp5VFOFiQy6tgOmjRqzjt1gnWbOsFq8wMngi9cfcQKKeMBTXPD1txfo5ve5ycr6ino0omNWMTN5AT0O2uPfhFHd34brdALQQ4XI-LOydfIrMqCqitTN0OXGf0josKCxOqPS9aKba_pNQo8snKRcsCw7aVnupUnxd4fJhNF5g6wOtEYrEmPpuZa1pwt2XDIbN1PHs20lNBuXP1rQ9obKlOWRaQ_XHPJTAErNv5aOYv4BUv78odRB1ksoc0mHrM28tok85btTZtPv9hqwUGk1PSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مدیرعامل پرسپولیس به پیشنهاد استقلال برای از سرگیری جام حذفی: قاعدتا نمی‌توانند مسابقات را از سر بگیرند وگرنه لیگ هم باید ادامه پیدا می‌کرد
پیمان حدادی، مدیرعامل باشگاه پرسپولیس در
#گفتگو
با خبرفوری:
🔹
بحث ادامه جام حذفی را دوستان فدراسیون باید بررسی کنند اما فکر نمی‌کنم عملی شود، زیرا آن فصل تمام شد و فدراسیون و سازمان لیگ به AFC اعلام کردند که مسابقات لیگ و جام حذفی، نیمه  کاره تمام شدند و قاعدتا نمی‌توانند آن مسابقات را از سر بگیرند و اگر به این شکل بود، لیگ گذشته هم باید ادامه پیدا می‌کرد.
🔹
فکر نمی‌کنم که اختلاف امتیاز زیادی در لیگ گذشته وجود داشته باشد، اگر مسابقات ادامه پیدا می‌کرد، حتما در صدر جدول شاهد تغییر در رتبه‌بندی تیم‌ها بودیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/697553" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697552">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/697552" target="_blank">📅 20:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697551">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
♦️
دبیر شورای‌عالی امنیت ملی: آمریکا دارایی‌های بسیار گران‌قیمتی در امارات و پیرامون تنگهٔ هرمز دارد که ما هنوز آن‌ها را در میان اهداف خود نگنجانده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/697551" target="_blank">📅 20:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697550">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d86d3bae.mp4?token=iK_mL8CAYf6UV56tRmDuQa3TXRS_8Vr6vNRocX7Dly7u-vnUlr-lEzujC65cxiDKp1addmpajN31En0uPEIVOYndODncN8jvLgEPihiKmPmWEtAC_hvaVHfG-brBxyPswz99j8mYbhJbOcfQc20-hWUAr6My7CEbb88ODVlgEbunwyqmrMa7mp7L9Dss2gyCRZq0Mbmc4sBhg83u7aWwt5-BuSMpCoE5164cwP3SvAwtggQGGznswScGvzKMXJNRCXdKurqXtwwhNhNq8fmKs31Mo30-ZlB0CoBNa9dIuFuUmDQv0lozpzQ874qFrOdBcBIyHPzobNhT3INNcF_VUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d86d3bae.mp4?token=iK_mL8CAYf6UV56tRmDuQa3TXRS_8Vr6vNRocX7Dly7u-vnUlr-lEzujC65cxiDKp1addmpajN31En0uPEIVOYndODncN8jvLgEPihiKmPmWEtAC_hvaVHfG-brBxyPswz99j8mYbhJbOcfQc20-hWUAr6My7CEbb88ODVlgEbunwyqmrMa7mp7L9Dss2gyCRZq0Mbmc4sBhg83u7aWwt5-BuSMpCoE5164cwP3SvAwtggQGGznswScGvzKMXJNRCXdKurqXtwwhNhNq8fmKs31Mo30-ZlB0CoBNa9dIuFuUmDQv0lozpzQ874qFrOdBcBIyHPzobNhT3INNcF_VUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند، قدیمی‌ترین لکه‌های چربی هود و کابینتت رو ازبین ببر! #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/697550" target="_blank">📅 20:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697549">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-o1czF6Z7l8zOSlA5SDPnN65uZqbCV-53_mz6_LWD1ob6uFrw2dUQd8eq2zPmNSH6Bu9xlh859jebfoY8KIdokFb7ZWm28c9t7SVcPtKenXJfUQUEmVBOTWB-bwh0WNhHrq_BjKOKvai2_LVJKAAUR7Sw94tKtGM99GL2yJ7pGQY_mWloZa2eTF0dw5O1FUDpkJE6x-IDx45yZXQK9WKT_VLsO68K7G2w55ais_v_tHU4WxE4DOgk_tQ__GTJnoySgFW5lTem-4Ksc_LqudL0k7wRau59VGfD1Lutj_IKrak9aChWFtD_nMcGGXb1k0cpT3jelDIiP0HdkQHU-y3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه آبگیر با سه رنگ متفاوت گیلان زیبا
🇮🇷
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/697549" target="_blank">📅 19:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697548">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYmQnQ2PN_s0OZr4crEil-fMiJ6Fim3leyhrmk_Ia7XvOuaXTP9GunIZ_tbIUJQ_-VhSXXEwJDAbUXT-LHoiRs2Mkwkewv9tRmmmT4sbcFSMIR_MCL2O-1-qvAEStMkWcaalM-i2QbROLqKcfR-KmCvC-ntaYr_LLcdA5h-IWhzljZtbdpEuzQhG8fYevO6-K4fIRmczyl4rDnK1d-JnLcJ7ay0dp1BOetHqSE9vuKQRKinA-F4wpuFsWkU2d8EcLZR0y1fLTHo2UML8fSpKTfSRcTZB0KiwTIC-lpe29447hWgnb2U9GOUjbLZOPTrhhb4TC8foS1k8sgdcIJf2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران نه، ریاض
🔹
پس از ۸ ماه جنگ آمریکا علیه ایران، دامنه‌درگیری‌ها به دیگر نقاط منطقه کشیده شده است. آمریکا که به دنبال مختل کردن پروازهای ایران و اعمال محاصره هوایی بود، حالا در پی تشدید درگیری‌های انصارالله و عربستان، با توقف فعالیت فرودگاه ریاض و لغو گسترده پروازها روبه‌رو شده است. این تحولات بار دیگر یک واقعیت را یادآوری می‌کند، در خاورمیانه صلح و آرامش یک‌جانبه معنایی ندارد، یا صلح برای همه است یا برای هیچ‌کس. جنگ‌افروزی آمریکا اکنون بیش از هر زمان دیگری پیامدهای خود را نشان می‌دهد، پیامدهایی که از مرزهای ایران فراتر رفته و دامن متحدان منطقه‌ای آمریکا را فرا گرفته است.
🔹
هشتصدوهشتادوسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/697548" target="_blank">📅 19:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697547">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
لایو ای‌آی‌اس به نقل از ملوانان نفتکش‌ها در تنگه هرمز: اسکورت‌های آمریکا دیشب پس از حمله به یک کشتی، در میانه راه متوقف شدند
🔹
دو کشتی خروجی پس از حادثه امنیتی، مسیر خود را تغییر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/697547" target="_blank">📅 19:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697546">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcff288f73.mp4?token=tbpMFe0P-XPw-khlCkcDCmeSyma5ihQLzGvEix7XsdNzvG1Cg5dER8dpcdWMeIYYsZSPrT-YbrvPcfjJmSIAwAB99lT0YGZqNiFWqu_0wJr5PcK3RcLrwviIne6rIKN6rEw_k3D7PDhv5dYMv4AF2OQTzZiPThO52XANxm8Gnzc4wF-c2_vAv5TVu-Y1loJGKxsyOZvKgGxTR_Huiy8fA6oVFypIiBefxT98t7I3fcbX7JbcDRJxzPz66vH-lMUZsELCdYeDAzMRgIpY7Kv9Us0s1trqSuZDBm3Q8d8ZiCs2TPt8li_VD1BrFRZEw2hNXNjvLSru_liKyy_l04Yvsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcff288f73.mp4?token=tbpMFe0P-XPw-khlCkcDCmeSyma5ihQLzGvEix7XsdNzvG1Cg5dER8dpcdWMeIYYsZSPrT-YbrvPcfjJmSIAwAB99lT0YGZqNiFWqu_0wJr5PcK3RcLrwviIne6rIKN6rEw_k3D7PDhv5dYMv4AF2OQTzZiPThO52XANxm8Gnzc4wF-c2_vAv5TVu-Y1loJGKxsyOZvKgGxTR_Huiy8fA6oVFypIiBefxT98t7I3fcbX7JbcDRJxzPz66vH-lMUZsELCdYeDAzMRgIpY7Kv9Us0s1trqSuZDBm3Q8d8ZiCs2TPt8li_VD1BrFRZEw2hNXNjvLSru_liKyy_l04Yvsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساخت گل‌های زیبا و دست‌ساز با وسائل دم‌ِدست
🌼
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/697546" target="_blank">📅 19:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697545">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=g8nEuwJoqEwR6Y8jsVOAo8dPyfn5WrjZny9rmMkpATcZOwdQw0-OZJU2mq3WvkNpRxIWSMp95nLMWICYjgqmJU6DUMlgUyvhlUjSekq9aWH3GaX0iOWsaBWtwa2dXKm3XE5q4xh7KWJR8ZOSBse6ARBgjlmnR5IXsrph6oWIaEJDdws6YVdmmSfZdtSQu12uweLy0NEujjlZ3IIr0IItA1VvKCqJj4g-CMYZ6KAshSKLGylyqGEcEcSFfyIUZCuebEhfPx4Cr3R__5uYaEnhJfatS56GIjXKw20hcuLOgvbnjW84I12sOilVxwWkokSg7gMbMFf-xinim_z_1uvuBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=g8nEuwJoqEwR6Y8jsVOAo8dPyfn5WrjZny9rmMkpATcZOwdQw0-OZJU2mq3WvkNpRxIWSMp95nLMWICYjgqmJU6DUMlgUyvhlUjSekq9aWH3GaX0iOWsaBWtwa2dXKm3XE5q4xh7KWJR8ZOSBse6ARBgjlmnR5IXsrph6oWIaEJDdws6YVdmmSfZdtSQu12uweLy0NEujjlZ3IIr0IItA1VvKCqJj4g-CMYZ6KAshSKLGylyqGEcEcSFfyIUZCuebEhfPx4Cr3R__5uYaEnhJfatS56GIjXKw20hcuLOgvbnjW84I12sOilVxwWkokSg7gMbMFf-xinim_z_1uvuBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیرعامل پرسپولیس: در ازای هر گلی که بزنیم، یک نفر را آزاد می‌کنیم/ در این فصل ۴۳ زندانی آزاد شدند
پیمان حدادی، مدیرعامل باشگاه پرسپولیس در
#گفتگو
با خبرفوری:
🔹
از آذر ماه سال گذشته، باشگاه پرسپولیس به عنوان بزرگترین تشکل مردمی غیر دولتی کشور، کمپین مهر سرخ را شروع کرد و در این پویش یکی از کارهای اساسی و بزرگی که به کمک هواداران انجام دادیم، آزادسازی زندانیان مالی جرائم غیر عمد است.
🔹
سال گذشته در استان تهران، ۶۰ نفر از هم‌وطنان که در زندان‌های تهران بودند، آزاد شدند و در ماه گذشته، در بازی پرسپولیس - استقلال ۶ نفر دیگر از هموطنان آزاد شدند.
🔹
امروز در آستانه بازی هشتم پرسپولیس در لیگ، در شهر آقا امام رضا (ع) نیت داشتیم که ۸ نفر دیگر را آزاد کنیم، اما به کمک خیرین، این ۸ نفر به ۳۷ نفر افزایش پیدا کرد و مجموعا طی این پویش ۱۱۰ نفر را آزاد کردیم.
🔹
از ابتدا این فصل قرار شد به ازای هر یک گلی که یکی از ۶ تیم فوتبال پرسپولیس می‌زند، تحت عنوان گل آزادی، یک نفر را آزاد کنیم و در این فصل ۴۳ زندانی آزاد شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/697545" target="_blank">📅 19:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697544">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517f29697b.mp4?token=QMBd5s6RGMabmmbido5KL_U8rfy-vuz09tvk07f0ci28MR_JjvuWIEuPJtRD851oG_F_qi7tdJ72U6ZCZFSLmeoEy72-dr8_zBtDWV_S6MjeVVcYDCkOyTLcxqxy0NFcSoMPpyYetTglRqrAE_M_VnVzOXAmb2M6EsOtQdH3C1xOH6yYDfX3QrQKLVUX7198GH-0yOaB6iOZZGS0rjnF7gPKGW8c4AEaltMXtZ71F8zmSh5FNwpDLTUzUWQP4NL-HDImar7QDGVeQyNHgcl1z2pKTXvz5TNJNEkx1uBjKBcLjID60_97syH1rektxBgtxROESRf7wIgPCW-92X7GHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517f29697b.mp4?token=QMBd5s6RGMabmmbido5KL_U8rfy-vuz09tvk07f0ci28MR_JjvuWIEuPJtRD851oG_F_qi7tdJ72U6ZCZFSLmeoEy72-dr8_zBtDWV_S6MjeVVcYDCkOyTLcxqxy0NFcSoMPpyYetTglRqrAE_M_VnVzOXAmb2M6EsOtQdH3C1xOH6yYDfX3QrQKLVUX7198GH-0yOaB6iOZZGS0rjnF7gPKGW8c4AEaltMXtZ71F8zmSh5FNwpDLTUzUWQP4NL-HDImar7QDGVeQyNHgcl1z2pKTXvz5TNJNEkx1uBjKBcLjID60_97syH1rektxBgtxROESRf7wIgPCW-92X7GHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیلی از خوراکی‌هایی که روزانه میخوریم احتمال ابتلا به کبد چرب رو افزایش میده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/697544" target="_blank">📅 19:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697543">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/714574dcee.mp4?token=YGF4hr1ox2ii3l8NW9cwi0rOJgEG40vH7v5huskwoGjlTBvLpQzuDTrq-jPsLt93x0X5ZI9ZosHZphcbyvWJNoPFwKXaQlhB79R_J0lA2KmXISAKTZc5PkwdFCPgR7Y3StNK5s-tvZ42P0_YUjJb82Ln_00oD4YCknIviO8qWovTXf4YBtMhFdSVMiI92agM6ERi1IgI3xb_uu5JAvb_miazl1yx_vuiInG8DAK48oBwOzexBsn_9zeVKGCgQH3To4iJTzuU1qgGMmDOe2ZNyCRWXk2TptQuUfdFK6msPHNPYOHZtyh-ar2Xs1D0cLLeiH_dGSeZhemKrfcWPrQyrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/714574dcee.mp4?token=YGF4hr1ox2ii3l8NW9cwi0rOJgEG40vH7v5huskwoGjlTBvLpQzuDTrq-jPsLt93x0X5ZI9ZosHZphcbyvWJNoPFwKXaQlhB79R_J0lA2KmXISAKTZc5PkwdFCPgR7Y3StNK5s-tvZ42P0_YUjJb82Ln_00oD4YCknIviO8qWovTXf4YBtMhFdSVMiI92agM6ERi1IgI3xb_uu5JAvb_miazl1yx_vuiInG8DAK48oBwOzexBsn_9zeVKGCgQH3To4iJTzuU1qgGMmDOe2ZNyCRWXk2TptQuUfdFK6msPHNPYOHZtyh-ar2Xs1D0cLLeiH_dGSeZhemKrfcWPrQyrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دانشگاه فردوسی مشهد:
روایت تحول و تغییر رویکرد خاص در معاونت علمی، باید مورد توجه نخبگان کشور قرار بگیرد.
🔹
عبدالرضا جوان‌جعفری، رئیس دانشگاه فردوسی مشهد، با اشاره به اهمیت سخنرانی دکتر حسین افشین، معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، درباره «تغییر پارادایم معاونت علمی»، از نخبگان، استادان و دانشجویان دعوت کرد این سخنرانی را با دقت بشنوند.
🔹
این دعوت، بر اهمیت تبیین رویکردها و سیاست‌های جدید در زیست‌بوم علم، فناوری و نوآوری کشور و ضرورت آگاهی جامعه دانشگاهی از مسیر تحول در معاونت علمی تأکید دارد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/697543" target="_blank">📅 19:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697542">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
محسن رضایی خطاب به روبیو: قدرت‌های بسیاری در طول تاریخ رؤیای اشغال ایران را داشتند، اما نامشان از تاریخ پاک شد و ملت ایران همچنان باقی ماند
🔹
هرچه بیشتر علیه ایران تلاش کنید، بیشتر در باتلاق فرو می‌روید و بار دیگر در برابر ملت ایران زانو خواهید زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/697542" target="_blank">📅 19:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697541">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 اگر بخواهید یک مشکل اجتماعی را در محله خود حل کنید، کدام را در اولویت قرار می‌دهید؟</h4>
<ul>
<li>✓ آلودگی و نظافت</li>
<li>✓ امنیت</li>
<li>✓ کمبود فضای سبز</li>
<li>✓ کمبود امکانات ورزشی و فرهنگی</li>
<li>✓ آسیب‌های اجتماعی</li>
<li>✓ فرسودگی معابر</li>
</ul>
</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/697541" target="_blank">📅 19:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697540">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/697540" target="_blank">📅 19:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697539">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
محسن رضایی: می‌توانستیم تنگه هرمز را کاملاً ببندیم، اما به دلایل انسان‌دوستانه این کار را نکردیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/697539" target="_blank">📅 18:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697538">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499fae8935.mp4?token=QKUuflA8n1cF32XbkaaX-_1-iHP4aeE5c6aZWQLlbkEtejNak4ElKku1lMGHq0fO3t9bI9t-1sokWDL_BYPoBzLte7cniAXyHrvJniqqHQ6LcGTM3dmfz9_6AnKMFbTi6YDsqo60ntB4mIrt4XzhbHdB32w-fxfdhabKOMJh3afJoSOI_DfPUaO5lq7uEhzNJQhQG4Lfkd_OIIdWlVQvsgOeVckEM2duVQe2Ko90ewvp3fuJGdmknsjr42RJ_vjr455RDFNLIS2OxY094nvSaPUxrB8DNpRb53xjXNMZ17aWwAyc5ysXSEJ-gPMWW9XSldj8VFDOBVGibyh8nwVT3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499fae8935.mp4?token=QKUuflA8n1cF32XbkaaX-_1-iHP4aeE5c6aZWQLlbkEtejNak4ElKku1lMGHq0fO3t9bI9t-1sokWDL_BYPoBzLte7cniAXyHrvJniqqHQ6LcGTM3dmfz9_6AnKMFbTi6YDsqo60ntB4mIrt4XzhbHdB32w-fxfdhabKOMJh3afJoSOI_DfPUaO5lq7uEhzNJQhQG4Lfkd_OIIdWlVQvsgOeVckEM2duVQe2Ko90ewvp3fuJGdmknsjr42RJ_vjr455RDFNLIS2OxY094nvSaPUxrB8DNpRb53xjXNMZ17aWwAyc5ysXSEJ-gPMWW9XSldj8VFDOBVGibyh8nwVT3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: تهران به رویه‌های دیپلماتیک گذشتۀ خود باز نخواهد گشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/697538" target="_blank">📅 18:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697537">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d461159826.mp4?token=Jk8OL-jM-1JDaMJjTI_xOKlxl4D3Ory17G0VDxJstWNrAYLjCOv2eGooFj4u6OLGhY3utuw8K3BxPqd8njmxBBwtxwPYXjkdmOpyasduzW8nDPHW92Ob95C9NO-RNPz-SIMyjqluxW6MzbmowwaeI8VPAAL1wkYvblvPRqNXTBXIGzkEMH6IGfLbTYxh-wCogxuCUr53MFTkQ0KByXpwKrVymL4oAeH0ofjQvywJ9pTL6Lr6o5XkWSdnKHeD116xpa5Y5aRjSIXhSklsPaq01UyrJvDTFGFBehRRQq5P4I4xAQ1plBF5YJasS8FpzQedMhEpZRW2FteNEJYpJBxrPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d461159826.mp4?token=Jk8OL-jM-1JDaMJjTI_xOKlxl4D3Ory17G0VDxJstWNrAYLjCOv2eGooFj4u6OLGhY3utuw8K3BxPqd8njmxBBwtxwPYXjkdmOpyasduzW8nDPHW92Ob95C9NO-RNPz-SIMyjqluxW6MzbmowwaeI8VPAAL1wkYvblvPRqNXTBXIGzkEMH6IGfLbTYxh-wCogxuCUr53MFTkQ0KByXpwKrVymL4oAeH0ofjQvywJ9pTL6Lr6o5XkWSdnKHeD116xpa5Y5aRjSIXhSklsPaq01UyrJvDTFGFBehRRQq5P4I4xAQ1plBF5YJasS8FpzQedMhEpZRW2FteNEJYpJBxrPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: اگر این ایرانی‌ها کشورشان را دوست دارند، تبریک می‌گویم، شما باید آنجا بمانید
🔹
آنها نمی‌توانند اقوامشان را در لندن ببینند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/697537" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697536">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
محسن رضایی: بخشی از محموله‌هایی هم که اکنون جابه‌جا می‌شوند، متعلق به خود ما هستند. ما این محموله‌ها را مدیریت می‌کنیم تا غلات، اقلام ضروری و سایر کالاهای اساسی را وارد کشور کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/697536" target="_blank">📅 18:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697535">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: حمله آمریکا به ایران جزو احمقانه ترین جنگ های تاریخ بشر است
🔹
دولت ترامپ چشم بسته افسار خود را دست نتانیاهو داد و بدون برآورد دقیق وارد جنگ با ایران شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/697535" target="_blank">📅 18:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697534">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvXw2QwxgRGFar9w_RmOBcnwdegBmdwj5xh-iHWtgL0NDfGLke_sb6nbCPjez9ijDL_DA5OCCYtgZT1rMDFCsPLIlKsDQ450LuU1Z6KSZhuQD7sjHGz62Egb4qzs4zpzozp9lQmx-cll2fhMM0Hcm06tAACEm_-8OrHNzjAiwdipABniu6g5UjrQuxZP90tcxGzeffoRqIAr3eI-cdZc3zCMLamIXnJPBSkeb0Dp5XSBhzHvRIkthzeKLvf6Zb31g4Wiql2k5H15-Cp12H5otrIy1N2R0Rzsl7AAxAZMX8hg-B1zXfj-NhtbHX_MSAJ79XP9yfb6Jj0G_j6VLJm97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ سناریو برای انتخابات اسرائیل | نتانیاهو می‌ماند یا سقوط می‌کند؟ | ایران چگونه می‌تواند معادلات انتخابات اسرائیل را تغییر دهد؟
🔹
انتخابات پارلمانی اسرائیل پنج آبان در شرایطی برگزار می‌شود که این رژیم پس از سال‌ها بی‌ثباتی سیاسی، جنگ چندجبهه‌ای و تشدید شکاف‌های اجتماعی، با پنج سناریوی متفاوت روبه‌روست؛ از اختلال در رأی‌گیری و بن‌بست سیاسی گرفته تا پیروزی نتانیاهو، تشکیل دولت مخالفان یا ایجاد ائتلافی فراگیر برای عبور از بحران.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3251597</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/697534" target="_blank">📅 18:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697533">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
محسن رضایی: آمریکا برخی از شروط ۷ گانه ایران را پذیرفته/ ما پاسخشان را ناکافی می‌دانیم
🔹
تنگه هرمز برای تضمین صلح و امنیت منطقه تحت مدیریت ما باقی خواهد ماند و ما در این موضوع عقب‌نشینی نخواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/697533" target="_blank">📅 18:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697532">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
‌دبیر شورای‌ عالی امنیت ملی: اگر دوباره جنگی در بگیرد، بسیاری از کابل‌ها، دیتاسنترها، تأسیسات هوش مصنوعی و سایت‌های دیگر موجود در منطقه نابود خواهند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/697532" target="_blank">📅 18:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697531">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
♦️
دبیر شورای‌عالی امنیت ملی: آمریکا دارایی‌های بسیار گران‌قیمتی در امارات و پیرامون تنگهٔ هرمز دارد که ما هنوز آن‌ها را در میان اهداف خود نگنجانده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/697531" target="_blank">📅 18:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697530">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ترامپ با استخدام تعدادی از اشرار که در آب‌های ساحلی عمان فعالیت می‌کنند، به قاچاق روی آورده است
🔹
طی چند ماه گذشته، ما هر شب در تنگهٔ هرمز ۵ فروند از کشتی‌هایی را که قاچاقچیان استفاده می‌کردند هدف قرار داده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/697530" target="_blank">📅 18:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697528">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای ترامپ : از همین لحظه، در جنگ میان روسیه و اوکراین آتش‌بس در حوزه انرژی برقرار می‌شود؛ هر ۲ طرف توافق کرده‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/697528" target="_blank">📅 18:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697527">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/697527" target="_blank">📅 18:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697519">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igGGntxwE4xALoM75dt8XrHIqQo-GrRTaZUGW-ZQ7XfBV2jz0ZvcnYAtw-zm_YBHRgZmYuzgY9al5XzW-lf4pSbH4qzoJC3-mRJ_v22nRDUuYXTY29uJC3gM2II_oKziaFLsbTVYnrgNOLXM3rUow5p2W2Yehnj6Zg5Qi5lkaYC0t-ZMlS3UKKia0EeQ0R-fyZQPtDWk30lcdew-hnAqEQST7t9hZBLg16Ybm5-_-kQxORgiHmliJbCdEkrOnCMdTJktYLE4FikWjsy3c9sDQV5xitZy0WKZxwAoYJa6XVlMJw3h2bTu_aZBxsyKFC2V9D6oFGHKDNT_0KO7urGvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIOAv0QgN9qC7uV5cQqurvGJ2ljFzS864jV4wJGTKoaf824sUkgmFiYW6zhyoRneJeV-7sJcM1ZtCuUsLXhILoQsg9uLzHwY1Q_xhc2-bPjqel0fn8JskoJ0jUbAsanzbvXsmFDufwervLbDvmXXwO1Am8Q3DGINoKo65gEUwlK6mUQMBPpeidsxcCY0mIY-4ykyJaUh7KlSbmPfcsQcfgJjpksYjhYt5kRCYWfLkPnPQQHEuGC9BhQ2C9V4OCgyKn5yTjwYitVX3tG4OD5XUxzgn00l15cBZ5GWsLrcpd55Y0CBgTBhP4OUa-Msq5x_nEF4_lkSnmBpd7o2vIdBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LB6Z8t9BnZ5KNYdlJY_3TfKQOvoN0qZlSvtbrUw5FvJyAOwIVsafpdNDaUvAwU3cwdhTOd8MvjQ7qkiSeaYz9Y0WNS_7K7bNz0n5-IkSuvUIZ3E7BQ9-T1bmYUKYY5ua08lBZpsjO50YmdE_sQGsFl29HN9ubbNBBJ45aE8ZZYy_Gj_cwbmhtUIB-ARxXNlDX_wwqpN7KqIckeyIeg3VskP9YkNulPoL_wj1uKYC1rMmqVrnYUL6G79diRakj69xanGVbwVGSbUcyK9jlNvLEFoXJhd7MmMCjaZJWIU2KzjbQmzSo78gDAe04LJIvlOW4-_mcQlYCFB5tlHDdBQtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rd5zgy8GcRqeX1Fvx28ALzBc6hF6aGMNOmfBVJ__SJczBy7-5Z9bfj_KTrf7D86F17vyH_p9Hi2S7Q8vHC1TkBfEwPSbnRvhe8MsQWs-dncaaR3ftQ1K0ikhE8aP9GsuWIPwCD0JNE5cSi-E22RS5ERA1gHZUF8KDUA63xmk6iuSRpezslomJvHoDgHuMBDR3nXM5NP46iCV5mT0inIYJOSZKNZ-K7Gl_--3uWJi23yVPqkREJPKytRPU9JNzP3sZNwbNTWj_An1FMHctFLFMA7acfmy1L9KWW_wZTMwWaQKozbspNCDChQrwMtKVC8TOj3i8h8Nz9_yKGmCokRMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/daVwBQUAOeR4B4hS6caa1I6uc42qpaivi4UXhjJumNszwMRja6N_LFLPSEQTO6AOInRfHyhzQNbtVyTl00XSmKcT0dHVUwNoVtce-zvgih6Pruk6k4BaM1bhf2Y5QWU7jXoeBiyXWMTnY0gUk_sMSRH3oYlbso7n2cPpuHGhoBt8fsRD_8o7lMr7wrQqdOH5CK8mNJKIs1vTi8KQSj3xJ-RiV-cypH4yV8XFHi6WlOIUsNtMdIv3ZonmKneU8sW8v2DD5B89zQCx0QbfO7DXHMz1jUPhNxOL-mfYtjp6_CANCtcSl8LkAcDrpgRd3e_NeRok-rZ_erERXuVXWOBQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_v5Qe6EMzpenJz3bjYUHmiTrrrQ-v62cTUk3U04zm1cwump7I8uswaZ3KGRz017td8iZQ1eHnjG-9w5f9rb_HAx1gMynYYWt28aWwUmwADGCfzvrNq-LcPYQXx2mtg1eC2ERr1ddoHtnOWtVxMb6ZSdQ4qaES1ExKCjpN__p3230WSjKfxiA0dMSzFFyeA_5m37K6XV_UoU0j2PA0QDcBv1m467Eu9Z8vhiuhsfl9jDOYbDhGZ3XD8BXLuoALDN7gEJWR-uNIra3firUmgMtEzRBcf7qZj0e8uTPheMQvWa85yLqI4tRjsCEClq9uxc9IpPgZlXDhAOpP1jAzduUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaW0TQeEsEuYpg4nBd1xz9Zjy6rmpFOvBGXCbAn31oebKApbs4m2QKcbBFmzjjpg0nvQ8X5yQc0Hid-amQstZxRi3Q4QBCNgi3rRbbROPC-kMnqfStMmzTlaCMi7VMvfCR-ZUaqtRxVuhsha-yg7_yLeFnX91cGPOZWeA8eDWUkOQB6isU6Vo6UeCmgSMuhvuBRaE4O5Yv6dxZ3MJp2PFktUIJqpiD18gK4ip8PUVDHULPqV-pU_rDj59zB2nXfekJwRAEXQmhqCUGGor6mUjvUExm2ZTWNbRQlTd0vKO47PBHO1NnHNxRT0q04120OhgAvyKZUAhL-CKM9QbMKRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfRe8qJEa4lP5HrUljYGq2aiIzGXOoGkueQfjeX14HzB9Jx2mQ6r-8N9eHs-3jk4MFTCHB9BThlA_oYt2Wm6F4hIjPE614iS5sv6JOED1uRoA6RsqM4HjOb8oXMJQVV1dCfRcGL3tQgkNp5qd152AVhxBDz0qBC0yVl4DSU8X_P1MhVG6fESEHRQTHu6gBUMYpsSyW-__RIHFZtj3mtUm_WSdZD-6OjWbc_Ud9O7qBVSk0Hbsm10u6wyn5U9RZSwVnd2sgNtj_HHlj8GS3ocWS-Zv0CFNkTUvXWu78IBKY5yqtLCYU4HGUfX7J8CKDr2TaFNKMPj0rDGcxNGTDnRDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازدید مدیرعامل پرسپولیس از هلدینگ رسانه‌ای خبرفوری
🔹
پیمان حدادی مدیرعامل باشگاه پرسپولیس، عصر امروز با حضور در هلدینگ رسانه‌ای خبرفوری از بخش‌های مختلف این مجموعه بازدید کرد و با ابعاد گوناگون فعالیت‌ها، ساختار و سازوکار سیستم رسانه‌ای خبرفوری آشنا شد.
🔹
در این بازدید بر لزوم ایجاد همکارهای مشترک بین دو مجموعه خصوصا در بخش مسئولیت‌های اجتماعی تاکید شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/697519" target="_blank">📅 18:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697518">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جبران خسارت‌های آثار تاریخی آسیب‌دیده در جنگ ۷.۵ همت هزینه می‌برد
علیرضا ایزدی، رئیس مرکز ثبت، حفظ و احیای میراث‌فرهنگی و طبیعی در
#گفتگو
با خبرفوری:
🔹
از مجموع ۱۴۹ اثر تاریخی آسیب‌دیده در جنگ رمضان، ۴۲ اثر تحت مالکیت وزارت میراث فرهنگی است که مرمت ۱۱ اثر به پایان رسیده و ۳۱ اثر دیگر در دست اقدام است.
🔹
برآورد جبران خسارت‌ها ۷.۵ همت است، اما تاکنون ۵۰ میلیارد ریال بابت پروژه‌های متعلق به وزارتخانه پرداخت شده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/697518" target="_blank">📅 18:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697516">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822d3d5c4f.mp4?token=BUhK8p4YrbDchYOQs-zAcu71khxKD3mmbg2bWMyGIjyc6h8z8KDOPma_DHip58dAEzrFtX7dJfe3FGVLaiNQSj-614Mltlpsn_IfvatekSDOW2PFmNp5c3u4LnNuxa_Nu_VaAZDCPWlXCTleFg5LhV_ss5LQQWW8CSs0lifNJYvp3k9yDVSVg7odSYoHtdB8sYQ8qTm3jROli9CySRmRjP1GM__U1zY0mEfdY0wlhg5jJkuHJ-jK4Grp2xRieK5yJKaEXlbuhO2K_kpTmUctDHzSbSK7DWEokmOMtGSNQjzDOrSOvH57O9mEbVBXSDMLzpgk1JFw20llvpLErKFW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822d3d5c4f.mp4?token=BUhK8p4YrbDchYOQs-zAcu71khxKD3mmbg2bWMyGIjyc6h8z8KDOPma_DHip58dAEzrFtX7dJfe3FGVLaiNQSj-614Mltlpsn_IfvatekSDOW2PFmNp5c3u4LnNuxa_Nu_VaAZDCPWlXCTleFg5LhV_ss5LQQWW8CSs0lifNJYvp3k9yDVSVg7odSYoHtdB8sYQ8qTm3jROli9CySRmRjP1GM__U1zY0mEfdY0wlhg5jJkuHJ-jK4Grp2xRieK5yJKaEXlbuhO2K_kpTmUctDHzSbSK7DWEokmOMtGSNQjzDOrSOvH57O9mEbVBXSDMLzpgk1JFw20llvpLErKFW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از خم شدن تا دست زدن، همه افعال حرکات بدن رو به انگلیسی یاد بگیر
#زبان_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/697516" target="_blank">📅 18:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697515">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vg-tvDcDuraliS7JamtbXj3ryT3w9dMnv9fd0rwDQWLMBYE9n26u4j8gRvlQ3JBYuDGTi1cXf8LbjVaJgzWv8LDMGtL6r3hudtYIGhxJ28bmIBdKgnwzvyqhx4b4xH2KSAKubdWaRTtGjvPegllD0ZnAuhwLqsbHltKLviidSiAFhziI8C3MR-DRbFCByBAf1-d66fdY7gQ1YBLm3tTRQAVlzvpjJtyuog5otuvaIbsMTULbP7fECQaCrtpyCY6235fsI2Y_2g1noGlrHtOkDybP0hflaP_4rPf7COgf6cS_1XurvCltaepkdx-ehI9Wyzi1ZPPVELg_fEQHXbevzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎀
یه دختر قشنگ، یه پک خوشگل، یه عالمه ذوق و عشق!
💕
🌸
پک‌های دخترونه‌ی ارکیده شاپ
با رنگ‌های ناز و ملیح، آماده‌ان تا روز دختر رو برات خاص‌تر کنن!
🎁
😍
💗
با خرید پک های روز دختر هم تخفیف داری ،هم اشانتیون میگیری ، هم ارسال رایگان میشه برات
😍
🥳
✨
برای خودت یا دخترای دوست‌داشتنی زندگیت کدوم پک رو انتخاب می‌کنی؟
😍
🎁
https://t.me/Orkide2025
https://t.me/Orkide2025</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/697515" target="_blank">📅 18:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697514">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt6h0Jipv-sx8FPGU8Ii5QTsse_I3BFLZhMDSaNTVcr50Yg8vYEolfjVRwm43WaXvJ0Ze1_eKzhRK7Pm4Lr3iSOU6FT2sqabkqvTIxhYnBZSuVSnIqCJzRaJxWz8ZDxzf_23rabTWgt4-Ir8j99jN9CmIqrPTGb-B5pqe_Hq8iQX5P7laxYIzaetTJA_4rhknv75wBomMDpNh6tEJc6ZVt_PyX3J8gTd-ch6mBt6g2_UgHBOrglIgFs_fi8zRGjzcDqLbGh6tjZ1HbI5o6ooPLwLg5yuZ7Rl6UAiW-QhRxyqMNSo45YMuvF1mldiylvvgn9ae4Wb4vmKMnra6eXCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ : از همین لحظه، در جنگ میان روسیه و اوکراین آتش‌بس در حوزه انرژی برقرار می‌شود؛ هر ۲ طرف توافق کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/697514" target="_blank">📅 17:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697513">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy8o5bHNUKJIYucRsfc0t9F0U303fjIB8YpzeRgtAequrE8F0zwFMz4umVxMqCt0BOg-QL7y0aei0GdNxHDsOMsnnAcGQImnycMkSTj7tnymi-RrfvEuaV1YLvdvoWfUo5yhC6ok9r9zdbcDw8Fqpg6ielaN9FMD1R0zBDcR10iE-a0kBUCGxzWn_Eud2ZeD_uJH_8cxz14kNtKJXw8OyFwmoeOALovpqyFlBruh1IpLCqVq1Ue4dcMkh5oAxUdYUTVInLwp7Z0mPzOITRsWH6jttp80S2ujXV2A-XyFwkhUwdOmlYOuy-jAiTd6257eg6Y83y9D6yk3YE2LtaKwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنیامین نتانیاهو:من به شدت حمله تروریستی وحشتناک به فرودگاه بین‌المللی خالد پادشاه در ریاض، عربستان سعودی را که جان ۱۲ نفر بی‌گناه را گرفت و باعث زخمی شدن صدها نفر دیگر شد محکوم می‌کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/697513" target="_blank">📅 17:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697510">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: عاقبت قدرت‌هایی بزرگ‌تر از آمریکا که تلاش کرده‌اند ایران را فتح کنند، زباله‌دان تاریخ بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/697510" target="_blank">📅 17:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697508">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f14ba63f5.mp4?token=R3xJm5KWKF-6KECJqfk7HJb8NNd-Jivz9QvXq5aSpYGBcwMycE3izWf27wluvn3_96ZyZRLHy9g1GKe7yvKdhl0siy3wF0Z4271tRmfbZCWJlZiqjMzzLBQbD2thEVXZdjrwZRdF9gv-oNnGsSoKyyr-J40tmSv9k9Mt3dkAzq-dW-bsGx4053q39pG3mbCDBSqUNz_zeN6flMAiQi0Fsic7AtB9zsRBupQloDD29IjdqAxw0zODnM39okyyggRkLUO063l2XsIbUdNBPCJTQmKRwR2mg8L6GWiVtH-M6kC9dz82GZVl41lGlnjzJgT1pyYEGCvegkayM5gJPSvkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f14ba63f5.mp4?token=R3xJm5KWKF-6KECJqfk7HJb8NNd-Jivz9QvXq5aSpYGBcwMycE3izWf27wluvn3_96ZyZRLHy9g1GKe7yvKdhl0siy3wF0Z4271tRmfbZCWJlZiqjMzzLBQbD2thEVXZdjrwZRdF9gv-oNnGsSoKyyr-J40tmSv9k9Mt3dkAzq-dW-bsGx4053q39pG3mbCDBSqUNz_zeN6flMAiQi0Fsic7AtB9zsRBupQloDD29IjdqAxw0zODnM39okyyggRkLUO063l2XsIbUdNBPCJTQmKRwR2mg8L6GWiVtH-M6kC9dz82GZVl41lGlnjzJgT1pyYEGCvegkayM5gJPSvkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
وزیر خزانه‌داری آمریکا: اگر این ایرانی‌ها کشورشان را دوست دارند، تبریک می‌گویم، شما باید آنجا بمانید
🔹
آنها نمی‌توانند اقوامشان را در لندن ببینند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/697508" target="_blank">📅 17:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697507">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZT87MXVxA_Fc52SDxjNOs1Fo69GuuJaUvNnaQeRgdNqhwOFa2PGdZYcmlmqEOAk6QuaQIii8xK9VaRxS6ySVDG4vVDT-iOx5IDF7rfq6Bq770tZ_o2t5PFZK61Yt-dHxTk7LNZeYdKKOpTnwEUePp8fBTiqMUFRVygo3b8F1gm1o8JJlbusefeUcb0KVyUdG2k32upz1qHMZ7yxblcPlJAldDk1F9eBAXFYWZDuMXelNFg0mStcOY7Jts_mTUIEC7wIrmc7d91CmWsr-tUMbuX2zXUHYuNIp6vt-nb2cqotD-TXDa3vbKeWlgYwus1BNcsFQgw9x1j6nOap_Boxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد موزه‌های ایران به هزار می‌رسد
🔸
بر اساس اعلام معاون وزیر میراث فرهنگی، در حال حاضر ۸۳۳ موزه در سراسر کشور وجود دارد.
🔸
برای تحقق هدف برنامه هفتم توسعه، نیاز است تا پایان این برنامه ۱۶۷ موزه جدید به ظرفیت کشور اضافه شود و تعداد موزه‌ها به ۱۰۰۰ مورد برسد.
@amarfact</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/697507" target="_blank">📅 17:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697506">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: عاقبت قدرت‌هایی بزرگ‌تر از آمریکا که تلاش کرده‌اند ایران را فتح کنند، زباله‌دان تاریخ بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/697506" target="_blank">📅 17:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697505">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaac3fd9dd.mp4?token=Uwt2Qj3Rq_zYjU6SpqZYUKIGC9I1yMUCjnzoH_PnoLa0nGuLm66uAVLdw1taiwquEvRskVo73wWdBhu5c9FP8_WVX_VAEMNiJsR4IQ-Z1HC3rz4fGP144DhHy86tFEq7--ZN7Rc6-yq2P1jWgC1LbFY4Y_IY06HqVf1DNdETE3v-6vg2XkGTp7lzusepnKg5MS04RaDsloCODGpBTvrBsKJASUhfb5SyWPy0BI3tzP6kswFav4ov5qElnIfz0nGgrPW9xGibhqDr7GMoZDwEylMsVWTYKNXlcBhHkvUq-HHnyYKtfLxuj4zNH2whkedyo9qCB9n3v0U3v7r9allIow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaac3fd9dd.mp4?token=Uwt2Qj3Rq_zYjU6SpqZYUKIGC9I1yMUCjnzoH_PnoLa0nGuLm66uAVLdw1taiwquEvRskVo73wWdBhu5c9FP8_WVX_VAEMNiJsR4IQ-Z1HC3rz4fGP144DhHy86tFEq7--ZN7Rc6-yq2P1jWgC1LbFY4Y_IY06HqVf1DNdETE3v-6vg2XkGTp7lzusepnKg5MS04RaDsloCODGpBTvrBsKJASUhfb5SyWPy0BI3tzP6kswFav4ov5qElnIfz0nGgrPW9xGibhqDr7GMoZDwEylMsVWTYKNXlcBhHkvUq-HHnyYKtfLxuj4zNH2whkedyo9qCB9n3v0U3v7r9allIow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای بسنت: ایران در حال حاضر هیچ درصدی از نفت خود را در حال حمل‌و‌نقل دریایی ندارد. آنها با کسری بودجه مواجه هستند
🔹
ترامپ انتظار ندارد تا حداقل بعد از انتخابات میان‌دوره‌ای، شاهد درگیری‌های نظامی جدی باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/697505" target="_blank">📅 17:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697504">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
اذعان وزیر خزانه‌داری آمریکا به موفقیت ایران در تنبیه کشتی‌های متخلف در تنگه هرمز
وزیر خزانه‌داری آمریکا:
🔹
ایران هر شب پهپاد پرتاب می‌کند اما توانایی‌های رصد خود را از دست داده و پهپادهایش به برخی کشتی‌ها اصابت می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/697504" target="_blank">📅 17:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697503">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: الزام دانش‌آموزان به حضور در کلاس درس با پلاک، دروغ‌پردازی رسانه‌ای است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/697503" target="_blank">📅 17:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697501">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39237cc31f.mp4?token=tLm5leFEWm9BoU0ixr36ShQNhOuskeWBipqaJnBdzsFSQd6zQU8L_3DL1OnjVLLwqQYxBxh1CbkVdDs3GNbS2TEu8BCH3ybtFx_iiXco4n3Zah7caw5rO0O5iQ0OZm6ttZlpR9UeIa6f_wxGqtD2wuJvIB7PRBrDgw-5d6dAOH0k4hV9ZX3LW_dTeZlAUH-f7S6eOxxJPR-MJeUIjIvjAzitmSp-ZSY1WQ4uiPyljaaR5QBpmi0em4FecXlyZjjylvV9PDgr7LFpO2VRqZHXR6-ufAyY0lSa60Xzjx2UL3AMDWWOHzdNn_waytjM1ckKXwxidXC08la2Reo6zBn1Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39237cc31f.mp4?token=tLm5leFEWm9BoU0ixr36ShQNhOuskeWBipqaJnBdzsFSQd6zQU8L_3DL1OnjVLLwqQYxBxh1CbkVdDs3GNbS2TEu8BCH3ybtFx_iiXco4n3Zah7caw5rO0O5iQ0OZm6ttZlpR9UeIa6f_wxGqtD2wuJvIB7PRBrDgw-5d6dAOH0k4hV9ZX3LW_dTeZlAUH-f7S6eOxxJPR-MJeUIjIvjAzitmSp-ZSY1WQ4uiPyljaaR5QBpmi0em4FecXlyZjjylvV9PDgr7LFpO2VRqZHXR6-ufAyY0lSa60Xzjx2UL3AMDWWOHzdNn_waytjM1ckKXwxidXC08la2Reo6zBn1Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش هنگام خروج از تنگه هرمز، از سمت چپ کشتی هدف اصابت یک پرتابه قرار گرفته و آسیب دیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/697501" target="_blank">📅 17:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697500">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
دلالی با کارت آزاد بنزین | چرا رانندگان برای سوخت‌گیری باید پول اضافه بدهند؟
🔹
در برخی جایگاه‌های سوخت، دریافت بنزین آزاد برای رانندگانی که کارت سوخت شخصی همراه ندارند یا سهمیه‌شان تمام شده، به تجربه‌ای پرتنش تبدیل شده است؛ تجربه‌ای که گاهی با بهانه‌جویی، انتظار طولانی و مطالبه مبالغی خارج از نرخ رسمی همراه می‌شود.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3251584</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/697500" target="_blank">📅 17:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697499">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ec39cb19.mp4?token=a6hodUX-8m922GRZO3fyxH5AHFtmmPrZF5Hd4dOBYQrBv-u3pPjvb2onsr527FJMtusNa7ExvIAbW52xveeDRdDa3RUEhOZhs3CCMbbDG9dYZeHbNTzjUhvU_ljgE8U80JwpZMK_-TeyZnkdwL7NScttCXs20enP6qPFDWRdRgtIouOuLGyi1UrYL_iX_t_56BHEjHmXdmWDCyv7eCgjDjPKNowNvcy-kEjamzixjqQDKj2h25Sxa9n52dB9IRYL_m92kO4SRSs1ijtjXJzCgKXPxkqh9wAvxhgL5EzOx0xwxzIsNGwU-vyzgqtjcjTNE8jmIrkvqAkoFSHenefbBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ec39cb19.mp4?token=a6hodUX-8m922GRZO3fyxH5AHFtmmPrZF5Hd4dOBYQrBv-u3pPjvb2onsr527FJMtusNa7ExvIAbW52xveeDRdDa3RUEhOZhs3CCMbbDG9dYZeHbNTzjUhvU_ljgE8U80JwpZMK_-TeyZnkdwL7NScttCXs20enP6qPFDWRdRgtIouOuLGyi1UrYL_iX_t_56BHEjHmXdmWDCyv7eCgjDjPKNowNvcy-kEjamzixjqQDKj2h25Sxa9n52dB9IRYL_m92kO4SRSs1ijtjXJzCgKXPxkqh9wAvxhgL5EzOx0xwxzIsNGwU-vyzgqtjcjTNE8jmIrkvqAkoFSHenefbBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا کاهو رو این‌طوری خرد کرده بودی؟
🥬
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/697499" target="_blank">📅 17:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697498">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f3ca69e6.mp4?token=NvWXekl4ncqkN6D9eu8bmrNLyAwaiDsFVV9lEnkgCyYKoUCH2T5P392uM8niUfcHYXYMsAI6a37J5GB82vbV6vrKUYZ_kZFvDadw7h3iub1PqO5ZcOLYQSgkdrbJjEE4vJK1V7qvaoeeFKU43j__JK3TS07T_yWD1mB34lvBHZHcezxnEFrxwt2Glb0WmPLo_jsC3v2i_fML4XRy_aTsJBaqVM3AYK9P4UwONcQHpfpWErDNozXpME_Xx5Jy7KQYDlECrbTWMpgJRzyCpapOIaPW7IMDEy5qL-dzOEbfc9p7KPynAe3_pPiTqn1tz5SxicJD5droYEkhqvoEUBdNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f3ca69e6.mp4?token=NvWXekl4ncqkN6D9eu8bmrNLyAwaiDsFVV9lEnkgCyYKoUCH2T5P392uM8niUfcHYXYMsAI6a37J5GB82vbV6vrKUYZ_kZFvDadw7h3iub1PqO5ZcOLYQSgkdrbJjEE4vJK1V7qvaoeeFKU43j__JK3TS07T_yWD1mB34lvBHZHcezxnEFrxwt2Glb0WmPLo_jsC3v2i_fML4XRy_aTsJBaqVM3AYK9P4UwONcQHpfpWErDNozXpME_Xx5Jy7KQYDlECrbTWMpgJRzyCpapOIaPW7IMDEy5qL-dzOEbfc9p7KPynAe3_pPiTqn1tz5SxicJD5droYEkhqvoEUBdNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات در فرانسه با حضور گسترده پرچم‌ها در حمایت از فلسطین
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/697498" target="_blank">📅 16:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697497">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
«روایت امروز از هنر ساختن فردا»؛ نگاه اسنوا به آینده زندگی ایرانی
🔹
دکتر میلاد کوچکیان، مدیر برند اسنوا، در گفت‌وگو با خبرفوری در نمایشگاه لوازم خانگی، از رویکرد جدید این برند در طراحی و عرضه محصولات متناسب با سبک زندگی خانواده‌های ایرانی گفت.
🔹
اسنوا با معرفی سه سری محصول «اوان»، «بوم» و «هوم»، تلاش کرده است نیازهای گروه‌های مختلف مصرف‌کنندگان را پوشش دهد؛ از زوج‌های جوانی که زندگی مشترک خود را آغاز کرده‌اند تا خانواده‌هایی که به‌دنبال محصولات با امکانات و فناوری‌های پیشرفته‌تر هستند.
🔹
هدف این رویکرد، ساده‌تر کردن انتخاب برای مصرف‌کننده ایرانی و حرکت از فروش صرف محصول به سمت ارائه راهکارهای زندگی است. مدیریت و بهره‌وری انرژی نیز از دیگر محورهای مورد توجه این برند در توسعه محصولات به شمار می‌رود.
🔗
مشروح خبر
khabarfoori.com/fa/tiny/news-3251632
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/697497" target="_blank">📅 16:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697496">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
حمله موشکی یمن به تأسیسات نفتی و نظامی جده، حریم هوایی را مختل کرد و پروازها در فرودگاه‌های جده و الدمام متوقف شد
/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/697496" target="_blank">📅 16:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697495">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4746484ff5.mp4?token=qATEcP2neHqEBzXgEuZ1xktTO6ZjqdDkeulf8i9j0DiKwV7CjEGPcznUd9g_vanlVRuzBPCD9MlJqc3wYbojleF0gSyD5j7zhawYKLxAJ7gpaQoZUvnrIXtI8lD4AiOEbw5avzLAyfCwVDEXxz2UrvcEDv8Lmh7heqYhviHEil40X1MrIf6eERf968CP5lJSUP78C2Z3O3NjiokpGM0EBSpqQ4OT_F01THvlwPfve0L2ceNvUHjymUDCZ3hZLGKoYcEfoBYZiyvGLiTzvapUTuWvr9KstrWiuOJoarDhu4Zkpa41sM9gDbCWbn9sJP1781N9mtIp3j_YDt18CMBeyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4746484ff5.mp4?token=qATEcP2neHqEBzXgEuZ1xktTO6ZjqdDkeulf8i9j0DiKwV7CjEGPcznUd9g_vanlVRuzBPCD9MlJqc3wYbojleF0gSyD5j7zhawYKLxAJ7gpaQoZUvnrIXtI8lD4AiOEbw5avzLAyfCwVDEXxz2UrvcEDv8Lmh7heqYhviHEil40X1MrIf6eERf968CP5lJSUP78C2Z3O3NjiokpGM0EBSpqQ4OT_F01THvlwPfve0L2ceNvUHjymUDCZ3hZLGKoYcEfoBYZiyvGLiTzvapUTuWvr9KstrWiuOJoarDhu4Zkpa41sM9gDbCWbn9sJP1781N9mtIp3j_YDt18CMBeyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی که به تازگی از حمله به یک شهرک در افسریه تهران طی جنگ ۴۰ روزه منتشر شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/697495" target="_blank">📅 16:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697494">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4auLfVKrZcWBi0p4JAO_K7vXd-qYfJ4yNQenGgYRDkfZTsagHyd4jL06u53vpKFdTQ4xhkhzyV0E8m1nByy1Jbdax1Avrm62mhcRAnlBchJ9tPkfEe4F114tEjoN0JZzvZX6Uttn2Udbwu5vty5FhBJnVPoDD6ohEq3uzZr7B5iWT7RvlLjFth8nfOUVViulMc4KedojlrzrEskXMbXux_CAm4QJYm_HS-xfzM-FhNd1KnducjvYK4jyf0VMdnTD3_zxcr2uuOc1VJzp4WF0s4yr7t-r-lIEVUi6GZC9eIERYZJajX9cM5cESEGWJ2LjltyeUk_3MHEYTuEuWERAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش هنگام خروج از تنگه هرمز، از سمت چپ کشتی هدف اصابت یک پرتابه قرار گرفته و آسیب دیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/697494" target="_blank">📅 16:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697493">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42feee0627.mp4?token=mfudG6wiahNSoLDuG5MZezfZyUMHR_4772Tx4FatdnNVABzo3YKLz6ydtEMJQYO2DsB_SHiYPYxNUp7f7TOEzdV9RCpgGNNyoILQKB9zfOXNFAHKGfw41pGfNZMTW2Q9I3YQn6bLJWL5-fL7tCsvH6LxC8ejGaf7RxgblBTq3Y1YTSuRNcrkZ0t9RcVN3gYIzS3Ax_rq9DBpwuBtGjzAqSfNlvVc1eymx31Hg1JsVaMvuxdShgVSck_zjeyDE9vsgLsH1r3cgePa3VJvJ8wGJM6mys5P2Ho7bwq3MXuXTRJpLrKNFaK20flt8Ep_-XzxQKrYJcH0bYKdKglbfrd-5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42feee0627.mp4?token=mfudG6wiahNSoLDuG5MZezfZyUMHR_4772Tx4FatdnNVABzo3YKLz6ydtEMJQYO2DsB_SHiYPYxNUp7f7TOEzdV9RCpgGNNyoILQKB9zfOXNFAHKGfw41pGfNZMTW2Q9I3YQn6bLJWL5-fL7tCsvH6LxC8ejGaf7RxgblBTq3Y1YTSuRNcrkZ0t9RcVN3gYIzS3Ax_rq9DBpwuBtGjzAqSfNlvVc1eymx31Hg1JsVaMvuxdShgVSck_zjeyDE9vsgLsH1r3cgePa3VJvJ8wGJM6mys5P2Ho7bwq3MXuXTRJpLrKNFaK20flt8Ep_-XzxQKrYJcH0bYKdKglbfrd-5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسام‌الدین آشنا: راننده تاکسی بازنشسته سپاه بهم گفت شما اینقدر نامردید و لج منو در اوردید، که از لج شما می‌گویم رضا پهلوی تا بسوزید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/697493" target="_blank">📅 16:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697492">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
فارس: با پایان دو هفته، وعده بسنت درباره فروپاشی اقتصاد ایران محقق نشد و دلار از ۲۷۲ هزارتومان به ۲۶۵ هزارتومان رسیده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/697492" target="_blank">📅 16:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697491">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
خبرنگار جنجالی آکسیوس، افسر واحد ۸۲۰۰ ارتش اسرائیل از آب درآمد
تسنیم:
🔹
باراک راوید بیش از آنکه خبرنگار باشد، افسر واحد ۸۲۰۰ ارتش اسرائیل است و شاید این قلب فهم ماجراست! نیوز وان (news۱) از رسانه‌های اسرائیلی چند سال پیش درباره او نوشته است که راوید پیشتر درجه‌دار واحد ۸۲۰۰ ارتش اسرائیل بوده و با درجه سروان از آن {در ظاهر} خارج شده است!
🔹
مجله Vanity Fair آمریکایی نیز درباره راوید به صراحت به سابقه او در اطلاعات نظامی اسرائیل اشاره و حضور او در واحد ۸۲۰۰ ارتش را تایید می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/697491" target="_blank">📅 16:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697490">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦
می‌دونستین این خطوط زمینی در ایستگاه‌های مترو چه جوری طراحی شده؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/697490" target="_blank">📅 16:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697489">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1_WSJ_oa0vxsYiH_pVNOCnvV4Iz63JtVZFJyGJVNlML1p_BqK-EM6RcoAi4ezVzTKoc9MG24IzTeCKPssykBkBQcprDKvTar5XDY6f1MgyOAa8rbIKJf-DsNJnR5Z1TgRKOht3_1HuXYKaKQR6HlFzw4iBMkuxGtdb9DFd4Aog8TtXdTiDNl16ZrcDJVJJyetdf03rxctfr0cQWA7e4Hae3poy73Pc9JZdYopVSzGf4lEWpv3P1qtBlg5NNi7DSZRQnGa_cBZ6hwTsCo7PIptimF89JOsuWqIGz-oEfcyT8kfRu1HjzkitCFRShsluysgyCKzpu082pNcpMmyRRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ نقطه راهبردی در کنترل انصارالله یمن
🔹
در سپتامبر ۲۰۲۶ مجموعاً ۱۰ نقطه راهبردی شامل ۵ پایگاه، ۳ فرودگاه، یک بندر و ۲ جزیره در غرب یمن در کنترل انصارالله قرار گرفته‌اند.
🔹
در میان این نقاط، فرودگاه المخا، فرودگاه بنی‌الحکم، بندر المخا و جزیره میون به‌دلیل نزدیکی به باب‌المندب و مسیر کشتیرانی دریای سرخ از اهمیت جغرافیایی بالاتری برخوردارند.
🔹
همچنین جزیره میون با باند هوایی حدود ۱.۸۵ کیلومتر و جزیره زُقَر با باندی نزدیک به ۲ کیلومتر، از مهم‌ترین نقاط جزیره‌ای این فهرست هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/697489" target="_blank">📅 16:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697488">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جامعۀ مهدوی/ج۲</div>
  <div class="tg-doc-extra">استاد علیرضا پناهیان</div>
</div>
<a href="https://t.me/akhbarefori/697488" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جامعۀ مهدوی/ جلسۀ دوم
🔹
سخنران: پناهیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/697488" target="_blank">📅 16:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697487">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7a0589fd.mp4?token=sn5lRCzeX-5t_hAWb7ABnS2CG8O00L8H55Ob6p-BGXZfP5KizsXo0L2Zk2dtWXQkq2XlLBSrDjaB92Q6ukwst0EyATrsvdEA-pouu_qMJCkPLmnCZpBqSYad4PsPmpS6VRZDwYWRWf41JhRupBYXrw-eJ7-LdEtMkeb5BYO516ZMjAPEpKCLmVgUadaaxxlz7TZDkwbFKg_SOWEuHmQ6FVzmqScZ0lM-xO33vXyuFytU9m2X06FizfLdJh0ibbIGoCKqoS2m9Yy3OFWbu0YHrXGQE0IP11zyTjFdFwKVg4fQWawwLMwYADXpT-xJjSMiLkeh8l4qw1wnDCUzyJ66TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7a0589fd.mp4?token=sn5lRCzeX-5t_hAWb7ABnS2CG8O00L8H55Ob6p-BGXZfP5KizsXo0L2Zk2dtWXQkq2XlLBSrDjaB92Q6ukwst0EyATrsvdEA-pouu_qMJCkPLmnCZpBqSYad4PsPmpS6VRZDwYWRWf41JhRupBYXrw-eJ7-LdEtMkeb5BYO516ZMjAPEpKCLmVgUadaaxxlz7TZDkwbFKg_SOWEuHmQ6FVzmqScZ0lM-xO33vXyuFytU9m2X06FizfLdJh0ibbIGoCKqoS2m9Yy3OFWbu0YHrXGQE0IP11zyTjFdFwKVg4fQWawwLMwYADXpT-xJjSMiLkeh8l4qw1wnDCUzyJ66TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موزه‌ای شگفت‌انگیز در اعماق آب‌های قبرس!
🌊
🗿
🔹
این موزه زیرآبی در سال ۲۰۲۱ با نصب حدود ۹۳ مجسمه انسان و درخت در عمق ۸ تا ۱۰ متری دریا ساخته شد تا به‌مرور به زیستگاهی برای آبزیان و صخره‌ای زنده تبدیل شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/697487" target="_blank">📅 16:23 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
