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
<img src="https://cdn4.telesco.pe/file/dr-oemOtFIAJqvXa_OycHatoHKAKxeJF_F-fA8cpf_eUbeHvuHElIpacv66i27nsAc0kog-naMveZZcEPuw1nmEwuP-KR9Gppf_xOga5Ih1JPTx4xt5_dS0G3U2sgLIuZRv2NBlwx-bXUSamBUTXrkuvub12iL3jhTOpJZ5JtP3IqJtHA6i0XPS-91NhL_GBSF27XEzLGZNyY5u1oexxry5VW2k_2sY4VyMIX1VjpmAb-BTnJyecOXuPvNudOlFmCktUuzAFiu3_9Vf-4keHdX3VIQmMpTeykEqp0vLkv8YK5-W_UsfrVw1p5oUAJ1Gcfou1lVSmD28-dweaj97rew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 440K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-21684">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a3d293ea.mp4?token=dnv-P0vdBF-9hDSZPuTJRt7y_Vv3cpXPUDzETclUmKSzrLdKSANMzA8o1QXW-tSJjsKo9KRs0eqmZrnPDNhWHvd1LKO7NB9axriX_fghB_YsvPFgVa7_xrHBuMRIsQvPWChLH08Sh-xL0MK2MiaJLxDjpIakvZiyCIHfFprVlqWAUUMiwvAiTq21VHSOKfTN0Q9l3469A5aB8sdJzXFDzMwPRCyfG4jYTbot-4Jv0DKhP3jeKNYZMQH14cwwmZW1N9r1nSqSAMs7WrZhAvGxgKbg4mWCIlINF5qIbHXjZhOKAfsE2Dp8v6rWOui_qfsylErkQxFMzkpH4XgUahPr5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a3d293ea.mp4?token=dnv-P0vdBF-9hDSZPuTJRt7y_Vv3cpXPUDzETclUmKSzrLdKSANMzA8o1QXW-tSJjsKo9KRs0eqmZrnPDNhWHvd1LKO7NB9axriX_fghB_YsvPFgVa7_xrHBuMRIsQvPWChLH08Sh-xL0MK2MiaJLxDjpIakvZiyCIHfFprVlqWAUUMiwvAiTq21VHSOKfTN0Q9l3469A5aB8sdJzXFDzMwPRCyfG4jYTbot-4Jv0DKhP3jeKNYZMQH14cwwmZW1N9r1nSqSAMs7WrZhAvGxgKbg4mWCIlINF5qIbHXjZhOKAfsE2Dp8v6rWOui_qfsylErkQxFMzkpH4XgUahPr5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در تروث : دریاچه آمریکا توسط اردک‌های دونالد محافظت می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/withyashar/21684" target="_blank">📅 18:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21683">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ‌ در تروث : «سی‌ان‌ان (CNN، شبکه خبری آمریکایی) در یک مارپیچ مرگ قرار دارد و MS NOW (شبکه خبری آمریکایی که به‌تازگی نامش از MSNBC تغییر کرده و ترامپ با کنایه آن را “MSDNC” می‌نامد) هم همین وضعیت را دارد؛ واقعاً تقریباً هیچ‌کس هیچ‌کدام از این دو شبکه را تماشا نمی‌کند! بهترین فرد در سی‌ان‌ان، هری انتن (Harry Enten، تحلیلگر و نظرسنج سیاسی CNN) است، چون حاضر شد نشان دهد که دونالد جی. ترامپ (رئیس‌جمهور آمریکا) شش برابر محبوب‌تر از آبراهام لینکلن (رئیس‌جمهور شانزدهم آمریکا)، جرج واشنگتن (نخستین رئیس‌جمهور آمریکا) یا هر رئیس‌جمهور دیگری است. او اعتبار دارد؛ اخراجش نکنید! سی‌ان‌ان را می‌توان با مدیریت و مجریان جدید دوباره احیا کرد، اما MS NOW را نمی‌توان! چون یک برند بزرگ را هرگز نمی‌توان واقعاً نابود کرد!»
@WarRoom</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/withyashar/21683" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21682">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مرکز اطلاع‌رسانی فراجا : الف.ل، از سرکردگان شبکه تراستی که طی سال‌های گذشته مبادرت به دریافت ارز حاصل از صادرات کرده بود، توسط کارآگاهان پلیس امنیت اقتصادی فراجا شناسایی و دستگیر شد. بدهی این فرد به شبکه بانکی کشور، ۳۰۰ میلیون یورو معادل بیش از ۷۰ هزار میلیارد تومان است. این فرد تاکنون از اجرای تعهدات خود امتناع کرده و متواری بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/21682" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21681">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTjW3DCG9Q6SP90Z7mZ9qWdnddcvkskYJc1yjr3lKyb1Yz5bGWFsRRi2kxmT0iA0cpIv-teZ2ukIOYGkb_1EChClmz_2my3brrg-25nEHPY5l7zGWodhz3so2BevvH4j8B-CVBs7NQm6eUW_2u3xwUoZWre79__otshk7wDtDesIt1QmygZBbhjZfswlBXd2p-Pep1PNbvQTI1culnXf1Ut0cOlQFw1pvOoTKkEQaOBO09HRQq6M8LReXaGqnvH7_fOib6lkRON808hi8k3pDscTij9CxTApmuAz8y5k1n9sZ1kKaGOoQhim3ljLu1byJ5S7_vJKD1tXuZkI5_A0WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت کارکنان ناو لاوان به کشور پس از 7 ماه
@WarRoom</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/21681" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21680">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرنگار وال استریت ژورنال:
هیچ چیز به اندازه احتمال ادامه حمل و نقل دریایی هدایت‌شده توسط آمریکا از طریق تنگه هرمز، به اهرم فشار رژیم آسیب نمی‌رساند. اگر این امر ادامه یابد، اوضاع را تغییر خواهد داد. اگر چنین شود، اوضاع بسیار بد خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/21680" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21679">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCM3pO2HSVxGnSZdJf1Y52aDlFd4N0RhcH0Oicb8w_B3-3Y3bnGL4dKLLONqHRahKlcKlY-rPGmCtb1WAuvTk7gIrfUSlOiB_Gk47Rr77a4QWYBHM7m1PyQuYmmyAwshZpxCRNDgIjAPGscHnG1_5Mk9FvMPmDyIxOANGNkStkh_iCpCjIw0J64Yk1XmvyznYge8qWLx0IBjhip1pCVSNypAFpbwEs_Zt6FzXR3_WwPp3DAJ6ZZsvQEqdAy_KKfjLWP5zKMXu3PUy5hNEQdCMqEfwtXOw9olb_WBrQVF8t0iXNtgPFPjpqnPCTajkJx4v2vP2o8P0q4HIy1W7LEG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ماهواره‌ای از بقایای ناوچه‌های جماران، نقدی، بایندر و چند شناور دیگر
@WarRoom</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/21679" target="_blank">📅 15:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21678">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اتاق جنگ با یاشار : شکاف و درگیری در  بدنه حاکمیت
؛ تنها ساعاتی پس از آنکه مجتبی خامنه‌ای در پیام خود به مناسبت هفته دولت تأکید کرد بیان ضعف‌ها و کاستی‌های کشور در شرایط جنگ می‌تواند به دشمن روحیه بدهد و به انسجام جامعه آسیب بزند، مسعود پزشکیان در گفت‌وگوی تلویزیونی تصویری کاملاً متفاوت از وضعیت اقتصادی ارائه کرد و گفت: «پول و درآمد نداریم» و دولت با کمبود منابع مالی و ارزی روبه‌روست و مشکلات کشور بیشتر شده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/21678" target="_blank">📅 15:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21677">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رویترز: جنگ و تشدید تحریم‌های آمریکا فشار سنگینی بر اقتصاد ایران وارد کرده است.
مقام‌های ایرانی برای نخستین‌بار در این گزارش به ابعاد قابل‌توجه فشار اقتصادی اذعان کرده‌اند؛ مسعود پزشکیان می‌گوید تجارت خارجی ایران به دلیل تحریم‌ها و محاصره دریایی آمریکا حدود
۳۵ درصد کاهش یافته
و تورم سالانه نیز به
۶۶ درصد
رسیده است. مجتبی خامنه‌ای هم از دولت خواسته برای مقابله با تورم، بیکاری، افزایش قیمت‌ها و مشکلات بازار اقدام جدی انجام دهد
@WarRoom</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/21677" target="_blank">📅 14:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21676">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3UNTm82g9CUiMTt-d7IMb-Wn89_gJkPXbyKBPZ-BVz7Fa5SM36Bxw-1McOQYlRrdJasUYPctMBPdpmhO7nKw1E79AibqTNsYjB1jpnBw6LREBXS1e6Ak26YDZifyjPNtYQ1ut8iJjVO2PkBK9QxaL6JcE2ZLY6thZDjgadtMhm8rRu5Fmt4Zo3fGwTq32nMi16YulXeMy5c-famBAZ70mvltgPJ7ste0jgUnAvxou4rr2EmQ_yAOskoAmJAg4o7Aaio3NKXhDZvmEfjwpwH_UqR7NUZefhQsKHc-BxYNifDM6f4CW8zDelWHGb3KTR3iEqKxjKL_VXYBMO7uvbfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب، یک تانکر نفتی به نام "ELLIE" تلاش کرد تا از تنگه هرمز عبور کند و از مسیر جنوبی استفاده کرد که توسط ایالات متحده پشتیبانی می‌شد، اما این تلاش ناموفق بود و تانکر به عقب بازگردانده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/21676" target="_blank">📅 13:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21675">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری هاآرتص در تحلیل‌ خود درباره وضعیت ایران، با اشاره به تضعیف موقعیت جمهوری اسلامی، افزایش فشارهای داخلی و خارجی و نگرانی‌های فزاینده در میان مقام‌های حکومت، ارزیابی کرده است که احتمال به خطر افتادن بقای جمهوری اسلامی نسبت به گذشته جدی‌تر شده است
@WarRo</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/21675" target="_blank">📅 13:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21674">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مؤسسه نیروی دریایی آمریکا USNI : گزارش داده است که ناو هواپیمابر تئودور روزولت CVN71 و ناوگروه رزمی آن در هفته‌های آینده از سن‌دیگو حرکت کرده و برای استقراری بیش از هفت‌ماهه در خاورمیانه آماده می‌شوند. فرمانده ناو نیز خدمه را برای مأموریتی حدود هشت‌ماهه آماده…</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/21674" target="_blank">📅 13:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21673">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نرخ دلار ۲۰۷،۰۰۰ تومان(سقف تاریخی)
دلار کف بازار ۲۱۰ هزار تومان(سقف تاریخی)
تتر ۲۰۴،۰۰۰ تومان
بیتکوین ۷۷،۶۳۷ $
انس جهانی طلا ۴،۴۵۳ $(آخرین قیمت)
نفت برنت  ۸۸،۱۰$(آخرین قیمت)
@WarRoom
۱ ظهر تهران</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/21673" target="_blank">📅 13:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21672">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الجزیره : ترامپ ترامپ می‌خواهد سایه جنگ ایران را از انتخابات کنگره دور کند به افکار عمومی داخل آمریکا و بازارهای جهانی اطمینان دهد که منابع انرژی دوباره با قیمت‌های قابل‌قبول در دسترس خواهند بود و ایران دیگر این سلاح مهم، یعنی تنگه هرمز، را در اختیار ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/21672" target="_blank">📅 12:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21671">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">استیون میلر، مشاور کاخ سفید:
تنگه هرمز برای ایالات متحده باز و برای ایران بسته است!
@WarRoom</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/21671" target="_blank">📅 12:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21670">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فرمانده مرزبانی فراجا از کشف ۳۸ قبضه سلاح جنگی با اشراف اطلاعاتی مرزبانان در غرب کشور در مرزهای استان کردستان خبر داد.در این عملیات، ۳۸ قبضه سلاح جنگی شامل ۲۰ قبضه کلاش و ۱۸ قبضه کلت به همراه ۳۹ عدد خشاب و یک هزار و ۳۵۰ عدد فشنگ جنگی و یک دستگاه بیسیم کشف و ضبط شد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/21670" target="_blank">📅 11:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21669">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ در‌تروث مدعی شده آمریکا با ونزوئلا به یک توافق تاریخی نفتی دست یافته که بر اساس آن، بخش خصوصی با حمایت دولت آمریکا کنترل اکثریت بیش از ۶۵ میلیارد بشکه ذخایر اثبات‌شده نفت ونزوئلا را به دست می‌گیرد؛ به گفته او، این قرارداد بدون هزینه برای مالیات‌دهندگان…</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/21669" target="_blank">📅 11:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21668">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ در‌تروث مدعی شده آمریکا با ونزوئلا به یک
توافق تاریخی نفتی
دست یافته که بر اساس آن، بخش خصوصی با حمایت دولت آمریکا
کنترل اکثریت بیش از ۶۵ میلیارد بشکه ذخایر اثبات‌شده نفت ونزوئلا
را به دست می‌گیرد؛ به گفته او، این قرارداد بدون هزینه برای مالیات‌دهندگان آمریکایی، ذخایر نفت آمریکا را بیش از دو برابر کرده و در آینده باعث افزایش عرضه نفت و کاهش قیمت بنزین در آمریکا خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/21668" target="_blank">📅 11:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از منابع آگاه گزارش داد دولت
ترامپ
به میانجی‌های مذاکرات ایران اعلام کرده است که
هیچ علاقه‌ای به بازگشت به چارچوب تفاهم اولیه‌ای که در ژوئن با ایران شکل گرفته بود ندارد
.
@WarRoom</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/21667" target="_blank">📅 10:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21666">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد واشنگتن با سرعت در حال انتقال مقادیر زیادی مهمات، موشک‌های رهگیر و تجهیزات نظامی به خاورمیانه است تا توان نیروهای آمریکایی و متحدانش برای مقابله با تهدیدهای احتمالی ایران تقویت شود. این انتقال شامل سامانه‌های دفاع هوایی و موشکی، از جمله رهگیرهای پاتریوت و تاد، از نقاط مختلف جهان به منطقه است. مقام‌های آمریکایی می‌گویند این اقدامات بخشی از تلاش واشنگتن برای تقویت حضور نظامی و حفظ آمادگی دفاعی در برابر هرگونه اقدام احتمالی ایران است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/21666" target="_blank">📅 10:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21665">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیروی دریایی سپاه انقلاب اسلامی: رویکرد ما در مورد تنگه هرمز تا زمانی که اقدامات آمریکا متوقف شود و این کشور به تعهدات خود عمل کند، ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21665" target="_blank">📅 02:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21664">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxFx7keykmaBbvQYJvWSKZANWB46xOajSZ0-oiEWDiCeMj3RUiQN8F6zmidh4ag1p5-N0Dtu7vqBaLUDpFs-CsSVDpl7qDF1TAX0tQppuU-QeV4PFcr4fj4Wxvzswa8sqpojI43SEb3dsS7ECNFwEJoo4-hJ3898Q02D7cUxCh3aRJmghSiZ00wTrdYvZMPegk6nm4CxG2c4K3trNfZSXu4wdQnZv3LrxNZ1F1Q49sh1Z64e_mL8MhtHLNhyQaly-r0THy2Ptx7NyW0EA62xuqGibobJvzNAm7Q3bc6Sgsauz9HTKWNbZS6riC4SS3nemjGoib5YdMoOHtXobOdwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای جدید نشان می‌دهند که یک عملیات لایروبی مخفی برای ایجاد یک مسیر دریایی جدید در سمت عمان از تنگه هرمز در حال انجام است.
این مسیر دریایی حدوداً 1600 فوت عرض و عمق طبیعی آن تقریباً 93 فوت است، که نیازمند لایروبی محدود برای عبور تانکرهای نفتی بزرگ است.
آمریکایی‌ها می‌گویند که کشتی‌هایی که از این مسیر عبور می‌کنند، به دلیل جزیره مسندم و انحنای زمین، خارج از دید ایران باقی می‌مانند!
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21664" target="_blank">📅 00:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21663">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتاق جنگ با یاشار :  امشب مارگاریتا زدم
😁
ببینیم چی‌میشه … بیداریم
⚔️</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21663" target="_blank">📅 23:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21662">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18d571649.mp4?token=kJD7qHyo0ow57hCSt5h_51tDLIfsqJwJcbkg63s0b_z8p6SS1EMy8Zse35rfz6QyD0am_ycO4PRZyd1t-UH6AQ1pZ2EE_WevWa82q7WqWyf8Tec9kX9gkBsh6lhZKUTWM2MJEd29OjwNeWO1rLCaNztQaJvHVSUAmaWxv-Fc457ZLvd-TCe5WaBNaMHtrohmth13qcpOBKrrsO505TobIsBm6VNM93ScdAi5QIN1aK6LNZyEcG6rOrzQNts3AN8S_CQBR9gHBpgR8nqwVMsB8WHfpDoXlp8ve0itn4UH0g1Bx5_MGNY9ZpPN-sjyhX02xMWZJIDTwbKlH3ubaGQbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18d571649.mp4?token=kJD7qHyo0ow57hCSt5h_51tDLIfsqJwJcbkg63s0b_z8p6SS1EMy8Zse35rfz6QyD0am_ycO4PRZyd1t-UH6AQ1pZ2EE_WevWa82q7WqWyf8Tec9kX9gkBsh6lhZKUTWM2MJEd29OjwNeWO1rLCaNztQaJvHVSUAmaWxv-Fc457ZLvd-TCe5WaBNaMHtrohmth13qcpOBKrrsO505TobIsBm6VNM93ScdAi5QIN1aK6LNZyEcG6rOrzQNts3AN8S_CQBR9gHBpgR8nqwVMsB8WHfpDoXlp8ve0itn4UH0g1Bx5_MGNY9ZpPN-sjyhX02xMWZJIDTwbKlH3ubaGQbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: اونایی که میگن تحریم تاثیر نداره عقلندارن
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21662" target="_blank">📅 23:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21661">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufDWwX0PlY0OYJjgfoIAbjaItdFKBuSCcw73wT0vOOPLB2pFrssWdr2HI87CH-AqwL0knDsGoPwdHlu03X3PWTz3ViIoP3ZXC4yVA_O02i2cGCxmIUeR4PpcuAcndLebmRUghgdWOl1-xvpNROgdB9JqlOq6KZNertW-7OdsN2LBym8PRsIV1Z3hguplWXZ41kpezBRPN8HO7ENsMGhiY447JQqszLnnavVoZsQyytZbhc4OmguCq6fY49Fw1Z--JuGR9_tkQuyOJFO8PTOr5ERT15J75Mm76SD5F2hQzlQNLWegWsA1d0ojGHZIVYSK8p7ZMi4WD6JwcJZdoCgz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : مخفیگاه دقیق: سه تا موشک/پهپاد ساعت نزدیکای ۲۲ از نزدیک مدرسه پرتاب شد یه تونل دارن فقط چند صد متر با خونه ها و مدرسه فاصله داره یه جاده اسفالت فرعی هست رد میشه  صد یا دویست متر بیشتر با محل پرتاب اینا فاصله نداره..سیریک-بمانی @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21661" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21660">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دیدبان اتاق جنگ : مخفیگاه دقیق:
سه تا موشک/پهپاد ساعت نزدیکای ۲۲ از نزدیک مدرسه پرتاب شد یه تونل دارن فقط چند صد متر با خونه ها و مدرسه فاصله داره یه جاده اسفالت فرعی هست رد میشه  صد یا دویست متر بیشتر با محل پرتاب اینا فاصله نداره..سیریک-بمانی
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21660" target="_blank">📅 22:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21659">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مسعود پزشکیان هم اکنون اعلام کرد نرخ سوم بنزین، از ۵ هزار تومان به ۱۰ هزار تومان افزایش پیدا می‌کند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21659" target="_blank">📅 22:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21658">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دیدبان اتاق جنگ : سه تا پهباد بودن یکی افتاد نزدیک ساحل
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21658" target="_blank">📅 22:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21657">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljOJodWABGdLH28-XYUuEe5OpFtNKFEwZ1XW2Nzjy88JIbc8DKoLDKvNtuNjlUS1vLJVu4GDHYRQz-T9XXaOS0ZwLtW4rA3zCprw_JlSztJ-fjuZZcGoEAhx4jSGo07pWysgmeett0kBzwBMrM_cVZc0Bj4EAjHWRSgZyQoM6IG9luRf7DeBJ0_Tu7VXQZrOAnADDxG1KIcB4Ra-fxvcPvGsNntysCpWlVg2G53YAGJYUGObQWA_mgz471tbesug6FJzzqueowP1EFTq4h_6bTYLwh0Ax5gcmr9NhZUuVH67JbAEYy_izWyANZG_PM9RgfgFF6AIw73_1mdYvkZEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در تنگه هرمز در آتش میسوزد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21657" target="_blank">📅 22:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21656">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش ۳ پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21656" target="_blank">📅 22:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21655">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش ۳ پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21655" target="_blank">📅 22:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21654">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مستند و مصاحبه جنجالی کامل تلویزیون إسرائيل با یک نیروی ایرانی ویژه در موساد با نام مستعار آرش در داخل ایران ( در این مستند صحنه ها بازسازی شده اند ) که در طول جنگ۱۲ روزه نقش مهمی را در انهدام سایت های پدافندی جمهوری‌اسلامی ایفا کرده بود. با زیر نویس فارسی…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21654" target="_blank">📅 21:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21653">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کرملین
: پوتین ۱۰ شهریور با پزشکیان دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21653" target="_blank">📅 21:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21652">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">موشتبی ای آی : گاهی اوقات، بیان صادقانه نقاط ضعف ما، کمک بزرگی به دشمن است.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21652" target="_blank">📅 21:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21651">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52453c0c98.mp4?token=szlAAtOmSUSx57XZvLAh1HE65RsjlRb6odCObxKsCz63-HdxdMMm_0Fa0pPahnX3tGnmhe_IV9XLdl7he1TwA-LXS5LmyrPfMUgjfitQ0wLDQ0uiajykUCSLMEJbSs2TXMZelLAhplGlQ4lbwMzTWvcAqxxw4kwQqxcPsZkwmJuyb0V6MP44bP2B2Ygelh7Ih5Vbxg0UQdAQNBcHoobA4x_-JNNJI623cc0D0r9doSuddlq-PR0rQ-GFATLE3bSzbtLb4bMgAGgko-kpSafdNoY9gcJ7jORT6VTe9ppWNbHQkvP0E9KKNNn8xEQ4srtQSXiNrwQqJuxs8yv7ZS4ziA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52453c0c98.mp4?token=szlAAtOmSUSx57XZvLAh1HE65RsjlRb6odCObxKsCz63-HdxdMMm_0Fa0pPahnX3tGnmhe_IV9XLdl7he1TwA-LXS5LmyrPfMUgjfitQ0wLDQ0uiajykUCSLMEJbSs2TXMZelLAhplGlQ4lbwMzTWvcAqxxw4kwQqxcPsZkwmJuyb0V6MP44bP2B2Ygelh7Ih5Vbxg0UQdAQNBcHoobA4x_-JNNJI623cc0D0r9doSuddlq-PR0rQ-GFATLE3bSzbtLb4bMgAGgko-kpSafdNoY9gcJ7jORT6VTe9ppWNbHQkvP0E9KKNNn8xEQ4srtQSXiNrwQqJuxs8yv7ZS4ziA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
می‌بینید که چقدر خوب می‌جنگیم. ما بسیار خوب می‌جنگیم. به ونزوئلا نگاه کنید. فقط ۴۸ دقیقه!
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21651" target="_blank">📅 20:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21650">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f934b07069.mp4?token=OVyihWniYv7rAzb47L4Fi3CK7ypwpih8BCZ9hOPwV_agnrmEF-LVn0BbNUs-98I1QFbI_-6rvPlMDxh52bzqMnfRSssUrP65bb2AiyVnO9unjER0ZM0V8WeSD7wQm2j98OPAfZFEkevECr9FRMUFqFwDMX4XVvARqi2_c0BWs3OiSBvjfkjgnmVtdlCDPGV6gdU6SeouYR8P5bIPbvgwihuL-TCZKV7xs4bEYSR5a4O_VXpuabtK_INz28eQgB7xfTmbVeMokNCsOUcaK5L07HIKTBOtr-Zwnrk2PrTxPRF_B3oSv-WUoYpOVL47FThDz_NrWrgrOJ-oIRrjL-dWTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f934b07069.mp4?token=OVyihWniYv7rAzb47L4Fi3CK7ypwpih8BCZ9hOPwV_agnrmEF-LVn0BbNUs-98I1QFbI_-6rvPlMDxh52bzqMnfRSssUrP65bb2AiyVnO9unjER0ZM0V8WeSD7wQm2j98OPAfZFEkevECr9FRMUFqFwDMX4XVvARqi2_c0BWs3OiSBvjfkjgnmVtdlCDPGV6gdU6SeouYR8P5bIPbvgwihuL-TCZKV7xs4bEYSR5a4O_VXpuabtK_INz28eQgB7xfTmbVeMokNCsOUcaK5L07HIKTBOtr-Zwnrk2PrTxPRF_B3oSv-WUoYpOVL47FThDz_NrWrgrOJ-oIRrjL-dWTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«رویای آمریکایی دوباره بازگشته است؛ فکر می‌کنم این بار قوی‌تر از هر زمان دیگری بازگشته است. در حال حاضر شرایط برای ما بسیار خوب پیش می‌رود.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21650" target="_blank">📅 20:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21649">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2130ad167.mp4?token=SZxwYseufnyymFAKe5qaMSsuU9yYyHlL5UcCPMOus75xIc0P78Lqxc4Vq5kbhB0qe5tztWnADlwjNxeTO-MDYoCIUhwvZKyr_BhIdODjcYOqV-DodATw0DA6DaOjTJGznq3XMRrhQNG3CJV_1jsAJazz5OQOjEls4j1yEkGCPCUVf_49PBdaa5yq8DuftqBOPIQuLqRG4ugn1ZA60kAesi3Iz23pxQ5REnXyi49kP2GFK2x_QjQpNbblWmsUV22NiAb1o8BXHTwKb_0Up8v8vt7us7DEmtIZQjDsuosRkTLEJF16qLlQ36ALgF_dYO_DoFhPV1XVq8rd8xIgofJ1hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2130ad167.mp4?token=SZxwYseufnyymFAKe5qaMSsuU9yYyHlL5UcCPMOus75xIc0P78Lqxc4Vq5kbhB0qe5tztWnADlwjNxeTO-MDYoCIUhwvZKyr_BhIdODjcYOqV-DodATw0DA6DaOjTJGznq3XMRrhQNG3CJV_1jsAJazz5OQOjEls4j1yEkGCPCUVf_49PBdaa5yq8DuftqBOPIQuLqRG4ugn1ZA60kAesi3Iz23pxQ5REnXyi49kP2GFK2x_QjQpNbblWmsUV22NiAb1o8BXHTwKb_0Up8v8vt7us7DEmtIZQjDsuosRkTLEJF16qLlQ36ALgF_dYO_DoFhPV1XVq8rd8xIgofJ1hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی های
ترامپ:
«راستش من دوست ندارم با آن افرادی که پشت سرم هستند(ناسا) صحبت کنم؛ چون بیش از حد خوب به نظر می‌رسند!»
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21649" target="_blank">📅 20:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21648">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: وزارت خزانه‌داری وعده داده بود تمام شریان‌های اقتصادی باقی‌مانده برای تهران را قطع کند و به تهدید رژیم ایران پایان دهد. او تأکید کرد حامیان ایران نمی‌توانند همچنان به دلار آمریکا و نظام مالی جهانی دسترسی داشته باشند. بسنت…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21648" target="_blank">📅 20:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21647">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وال‌استریت ژورنال: پروژه عظیم «نئوم» عربستان متوقف شد
وال‌استریت ژورنال گزارش داده است که پروژه چندصد میلیارد دلاری «نئوم» عربستان، به‌دلیل هزینه‌های بسیار سنگین، مشکلات تأمین مالی و بازنگری ریاض در اولویت‌های سرمایه‌گذاری، عملاً به حالت توقف رسیده است.
بر اساس این گزارش، بخش‌های مختلف این طرح جاه‌طلبانه نیز در ماه‌های اخیر با کاهش مقیاس، تأخیر یا لغو روبه‌رو شده‌اند؛ اتفاقی که ضربه‌ای جدی به یکی از نمادهای اصلی «چشم‌انداز ۲۰۳۰» محمد بن سلمان محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21647" target="_blank">📅 18:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21646">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT-Dj9FLpRmqyqBSwUH7dBJtABkgo6YMfMIYobZUp-fmqXFUJ3U1FwsejNeMYzW6RGeNJnqMAPQIv3iiMzrpCgQ3JOZgz0fGmvnJ-WZmAC-aqOgVaEVoC2nwGoYwncDPpnFKobSk8wIVUIxz4eUaHyPPZFslsiysBt6wHmH-IWiIFC0OgPg1y0d8UgVB9jsHg5mufboT65mgJ3DTdeOoG0z9uPIhTbZbXapQoq2Rkn_d_h2eDXlSmJLlMh9JKVSDzPC9fV4sZMf0jMCO4nGQe5YIpaMGjwN_76g82Rm4oi2LkckA-GldywLaG_BHCNVGeIoV_d6yQqNP9A-zdn54-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داده بود تمام شریان‌های اقتصادی باقی‌مانده برای تهران را قطع کند و به تهدید رژیم ایران پایان دهد. او تأکید کرد حامیان ایران نمی‌توانند همچنان به دلار آمریکا و نظام مالی جهانی دسترسی داشته باشند. بسنت گفت
بانک مصر امارات
این هشدار را نادیده گرفته و آمریکا امروز نخستین گام را برای پاسخگو کردن این بانک به‌دلیل آنچه «حمایت مستمر و فاحش» از رژیم ایران خوانده، برداشته است.
وزارت خزانه‌داری آمریکا:
در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)، شبکه اجرای قوانین جرایم مالی آمریکا (FinCEN) پیشنهاد کرده است
دسترسی بانک مصر امارات به خدمات بانکداری کارگزاری مؤسسات مالی آمریکا لغو شود
؛ اقدامی که عملاً دسترسی این بانک به بخشی از نظام مالی آمریکا را هدف قرار می‌دهد. همچنین
دفتر کنترل دارایی‌های خارجی آمریکا (OFAC)، رضا محمد تأییدی، مدیر بانک ملی دبی، و یک شرکت پوششی مستقر در هنگ‌کنگ
را تحریم کرده و مدعی شده این شرکت در پول‌شویی وجوه برای یک صرافی تحریم‌شده ایرانی نقش داشته است. خزانه‌داری آمریکا این اقدامات را بخشی از تلاش برای
قطع آخرین شریان‌های مالی مورد استفاده حکومت ایران
عنوان کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21646" target="_blank">📅 18:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21645">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش ویژه فاکس نیوز : ترامپ ‌به فاکس نیوز می‌گوید ایران با افزایش فشار اقتصادی، صف‌های طولانی بنزین و تورم فزاینده‌ای که کشور را تحت تأثیر قرار داده، «برای توافق التماس می‌کند».
وزیر امور خارجه ایران می‌گوید دیپلماسی هنوز امکان‌پذیر است، اما استدلال می‌کند که فشار ایالات متحده مؤثر نخواهد بود و از واشنگتن می‌خواهد که اعتماد را بازسازی کند و به حقوق ایران احترام بگذارد.
در همین حال، مقامات نظامی ایالات متحده می‌گویند که خطوط کشتیرانی بین‌المللی پس از عملیات مین‌روبی در تنگه هرمز باز هستند، زیرا رهبر عالی ایران همچنان از دید عموم پنهان است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21645" target="_blank">📅 17:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21643">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-hFsvZ9sNiSG8Cay548GW3COQYH-J4HNUCbLhFFJ3clBc50Pinz3hkH8ToahUENfkk20Eo6JQG8-0cEkj4qg2TNhZmKcBMiU3X3jQDGCA7AwchCwWpeX-I9FBOyFAgajpTwHp1TkiOK2Eps5pV3JfSR3xXo3UCCQfJE3YLBmItoh0vHCA8lhvTUp2BgaYHJ3FlDrvugrucA18zbfWaxedfK3-eOAnajM4tHj7FuiQcT1M9peqQYp9pFtIXNPiYd1ObqguDgfgpqrNFYd8d8M3_UzHae-p94seWVm_TzlmP7QAf-nSFSIM7_cCI88DBmk8ZR_-GIM6bphiLbYUpzhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دید بان اتاق جنگ : هم اکنون ستون دود از سمت شرکت کاله آمل پیشتر کارخانه کاله آمل در ۱۵ دی ۱۴۰۴ (۵ ژانویه ۲۰۲۶) دچار آتش‌سوزی گسترده شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21643" target="_blank">📅 17:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21642">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دبیرکل سازمان بین‌المللی دریانوردی:
حدود ۶ هزار دریانورد در ۴۰۰ کشتی همچنان در تنگه هرمز گرفتار هستند
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/21642" target="_blank">📅 16:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21641">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EV5-oMKjgBQDgHtLWPQvx1OuW8Sg78rHf_HuGIRRclWuJ1oqPV6wjYauwf5puisyaxGTNz-BbzaZp7x_a0vCB6ICcKl704YeZyhZwMyu_vbPQpnGoNUKvvGQ1ygy9wNb2yoVpqhXH6ur4G0TbVwlonPTMdU0u72MTonz3qLP08Q-ibFx1FsAWE9D4PTNw5rvrqetqolW1aXFQgI1hZC6XyUQuFnCFskApGZfOigOAXA8sFFC7YX1uDXuN1Rejat02cS0BC3qxw05ZfKVtkvwraRioheV76GZDnd7l4mrhiJuYyqe1Zr_gAOAPAYuF0Bv9ocQeysgDX3drFljJ9TtnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیگه از اون آدم مهربون خبری نیست.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21641" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مستند و مصاحبه جنجالی کامل تلویزیون إسرائيل با یک نیروی ایرانی ویژه در موساد با نام مستعار آرش در داخل ایران ( در این مستند صحنه ها بازسازی شده اند ) که در طول جنگ۱۲ روزه نقش مهمی را در انهدام سایت های پدافندی جمهوری‌اسلامی ایفا کرده بود.
با زیر نویس فارسی
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21640" target="_blank">📅 15:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21639">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-VmtjaW8TgmNIUZJ_uQgc_MGXcgSTVI1BryUiN0Znz3Tzmf-b9YMuNxOPkuYAv1bCLFccpVM4VLpLtNnIOyjukVDPDQfosW6tbumGsGdMq8QEiBCaPXJHVjn5al1hJtEtwd0XBM3LKBi_XMsfAsHIeQV8vWa7s84UUKxfXMRf6xitww8k8wFbl8-zkpefTjuuWggcRArsMVjb1h8jyU-spyy2BYN1GHanjiXszRLK_r9bx1i96yQ8rXMgX4OlfTKZgFQ-qysc9lOj8MiwtIJeoHbP6Pi7kND7YgFFq3BhR7RP2Ke5HKTuMrDA_nXkGbhv_mGB3KWRIflJZNj7U2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دید بان اتاق جنگ : من با یه صدای لرزیدن شیشه اتاقم بیدار شدم دوباره خوابیدم  ، بعد نیم ساعت رفتم دم پنجره یهو چشمم به این افتاد @WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21639" target="_blank">📅 15:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21638">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b72f483d.mp4?token=v1bjXkeFc6jmcfFZLnRhlzdbjElhzZQJGH_0k8NikM4SxM3G--aKF4_Uebq7aRmelvaRxfJ5iziywkcq-k2UBB3FXK-cxf3GFYkRVx5x1lRD0oKyR-dClTf8OXp43-nLEAdjmvS3X0YB8xT9iSEew4kQJxnBcvuABgGdXg6Ln63qbKYwLRvqhMb5fFgePVnWPqEUyhLucQPxEa8A0-RhrIURuX8B8ZAU2C9RstMnKGtkwinXEZMyQ7ElwOnH5HNJcj7PS3MNepZn3vgwE38L4L4fTkFSY-QsUQUwTE6FrRP-lQO-90LpUYeStvYm4f70TVkcbM8WI6hhnVC10MgXKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b72f483d.mp4?token=v1bjXkeFc6jmcfFZLnRhlzdbjElhzZQJGH_0k8NikM4SxM3G--aKF4_Uebq7aRmelvaRxfJ5iziywkcq-k2UBB3FXK-cxf3GFYkRVx5x1lRD0oKyR-dClTf8OXp43-nLEAdjmvS3X0YB8xT9iSEew4kQJxnBcvuABgGdXg6Ln63qbKYwLRvqhMb5fFgePVnWPqEUyhLucQPxEa8A0-RhrIURuX8B8ZAU2C9RstMnKGtkwinXEZMyQ7ElwOnH5HNJcj7PS3MNepZn3vgwE38L4L4fTkFSY-QsUQUwTE6FrRP-lQO-90LpUYeStvYm4f70TVkcbM8WI6hhnVC10MgXKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگر ایران سلاح‌های هسته‌ای در اختیار داشته باشد، این پایان اسرائیل و پایان مردم یهود خواهد بود. و مهم نیست که چراغ قرمز باشد، چراغ سبز باشد یا چراغ آبی؛ من به رنگ چراغ اهمیتی نمی‌دهم. این برای من مهم نیست. ما باید این کار را انجام دهیم، زیرا در غیر این صورت نابود خواهیم شد. ما دیگر اینجا نخواهیم بود
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/21638" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21637">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175422b47.mp4?token=Z3P8VBGOtPLdjpEQpGrb9MSqullr12CTu1Q0vi5Y61JuA7IfzFutsNNsD5OzupDrPkb-yvcnMvWo-thgkVeeQQlHyrc67yvLxaMJr2oFlR06LfN5bl_RdpLuQYV64DrNI1AkanJ12ooLkWB_WfbaxZ4YtCIKTvuTk8Zr-wEbQHs5kzEn18fkDS_aXyGSFjtFwm4hSMsXLlrV54D8nui9s73G5ASYLfjSIY2fnTgu9sX8MOZAWa-uhsSCaNHWTJv1uxaSxFsPrE1hQ3HircH6J1FvX8KSKLJg6mgLu3I5KL-IZUD6jfqS0cQQh5b597e6pqxGUhUTw5ENehy34_mFiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175422b47.mp4?token=Z3P8VBGOtPLdjpEQpGrb9MSqullr12CTu1Q0vi5Y61JuA7IfzFutsNNsD5OzupDrPkb-yvcnMvWo-thgkVeeQQlHyrc67yvLxaMJr2oFlR06LfN5bl_RdpLuQYV64DrNI1AkanJ12ooLkWB_WfbaxZ4YtCIKTvuTk8Zr-wEbQHs5kzEn18fkDS_aXyGSFjtFwm4hSMsXLlrV54D8nui9s73G5ASYLfjSIY2fnTgu9sX8MOZAWa-uhsSCaNHWTJv1uxaSxFsPrE1hQ3HircH6J1FvX8KSKLJg6mgLu3I5KL-IZUD6jfqS0cQQh5b597e6pqxGUhUTw5ENehy34_mFiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویری که ادعا می‌شود برای بندر کنگ و لنگه امروز صبح هست.
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/21637" target="_blank">📅 15:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21636">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2bad7297.mp4?token=Q0vfOiRlt6_h68AYSwfR8lQxSzzSFDKt6ZN9yVCQWrQDmMiWSo4nX3tyFet43mgxNpOYK4TTxdOYMANvyCBaMsEWYe5BvV7oYTlTCw3o10uN3XIHyIv6fiHifWAp7fGbWjdw8STZwheCoMwJPxhnDFneoKcVOyUpM-cKpnKWIvKA3_Wa4xMq26rFt98u9KshZjewiXGFHbw9wnKA50fOXKarxVL_3LZBkqMY6L1G5VBEA6PNnLYXwKdRI-E8SOGgRA_v1U3brFauMLy22WRQB_C1V99K2_ZpB7WmEpuuFB6mXj3GkKu9CkzUGXwoR5xJ6YGLfzZxKeK9tuKHjbcSfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2bad7297.mp4?token=Q0vfOiRlt6_h68AYSwfR8lQxSzzSFDKt6ZN9yVCQWrQDmMiWSo4nX3tyFet43mgxNpOYK4TTxdOYMANvyCBaMsEWYe5BvV7oYTlTCw3o10uN3XIHyIv6fiHifWAp7fGbWjdw8STZwheCoMwJPxhnDFneoKcVOyUpM-cKpnKWIvKA3_Wa4xMq26rFt98u9KshZjewiXGFHbw9wnKA50fOXKarxVL_3LZBkqMY6L1G5VBEA6PNnLYXwKdRI-E8SOGgRA_v1U3brFauMLy22WRQB_C1V99K2_ZpB7WmEpuuFB6mXj3GkKu9CkzUGXwoR5xJ6YGLfzZxKeK9tuKHjbcSfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دید بان اتاق جنگ : من با یه صدای لرزیدن شیشه اتاقم بیدار شدم دوباره خوابیدم  ، بعد نیم ساعت رفتم دم پنجره یهو چشمم به این افتاد
@WarRoom</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/21636" target="_blank">📅 14:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21635">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آکسیوس گزارش داد روزانه حدود
۲۰ تا ۳۰ نفتکش
از مسیر تحت حفاظت آمریکا در تنگه هرمز عبور می‌کنند و حدود
۹ تا ۱۰ میلیون بشکه نفت
جابه‌جا می‌شود؛ نزدیک به نیمی از صادرات پیش از جنگ. امارات، بحرین و کویت به این مسیر پیوسته‌اند و عربستان و قطر نیز ممکن است به آن ملحق شوند. آمریکا قصد دارد با
افزایش عرض کانال اصلی کشتیرانی تا اواسط سپتامبر
، امکان عبور حداقل
۵۰ کشتی در هر شب
را فراهم کند و در نهایت
۶۰ تا ۷۰ درصد صادرات نفت پیش از جنگ
را احیا کند. آکسیوس همچنین گزارش داد حدود ۲ درصد کشتی‌های عبوری ماه گذشته مورد اصابت قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/21635" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21634">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ed644e27.mp4?token=D-Dss4mQh2HuwXv2Bhwgc-qDC8TI3JE96PSxqXepBhiNc35AqnPNIh0kogb1PEeSsABJCes2Diekiz95XSZu-Tdeau3Q5YvsVGzxcToOmBeH2Uq9FCXZaazmjJN35l7TKD8zVuTmo6W3w1TtqABpKylOcaMYyHJeSUDFxpYEiu2rxJbG6lE-kRJB9_qIN9Gk_sf3X2thp0_ThaIQJPydUckI16T9T-4-ddWUdlBBR6x7DZIaX16xWEa-aFIO03cTC0GMZwy6XH1BS8tp2HtANd4XU_dGUtLv_ITwEE02z5aE83QxQAH05zT5KnTy68bPnLvhePG3ZaOCfCJEkKfVqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ed644e27.mp4?token=D-Dss4mQh2HuwXv2Bhwgc-qDC8TI3JE96PSxqXepBhiNc35AqnPNIh0kogb1PEeSsABJCes2Diekiz95XSZu-Tdeau3Q5YvsVGzxcToOmBeH2Uq9FCXZaazmjJN35l7TKD8zVuTmo6W3w1TtqABpKylOcaMYyHJeSUDFxpYEiu2rxJbG6lE-kRJB9_qIN9Gk_sf3X2thp0_ThaIQJPydUckI16T9T-4-ddWUdlBBR6x7DZIaX16xWEa-aFIO03cTC0GMZwy6XH1BS8tp2HtANd4XU_dGUtLv_ITwEE02z5aE83QxQAH05zT5KnTy68bPnLvhePG3ZaOCfCJEkKfVqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف پمپ بنزین پشت زندان رجایی کرج , ساعت ۲ ظهر امروز جمعه
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21634" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21633">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیویورک پست: پسر ترامپ، زندگی منزوی را سپری می‌کند، در حالی که با تهدیدات از سوی ایران و تلاش‌های برای ترور پدرش روبرو است. او به شدت تحت تأثیر ترور چارلی کرک، فعال محافظه‌کار نزدیک به او، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/21633" target="_blank">📅 14:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21632">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پروفسور جان مرشایمر، استاد علوم سیاسی دانشگاه شیکاگو : وقتی فشار اقتصادی یک کشور را تا مرز فروپاشی می‌برد، معمولاً آن کشور تسلیم نمی‌شود، بلکه برای بقا واکنش نشان می‌دهد و دست به حمله می‌زند. مرشایمر با اشاره به حمله ژاپن به پرل هاربر در سال ۱۹۴۱ گفت فشار اقتصادی شدید آمریکا علیه ژاپن و قطع دسترسی این کشور به نفت، در نهایت به واکنش نظامی ژاپن منجر شد.
او درباره ایران نیز گفت اگر تهران احساس کند بقایش در خطر است، به آمریکا و متحدانش پاسخ می دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21632" target="_blank">📅 13:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آکسیوس گزارش داد آمریکا در نبرد بر سر تنگه هرمز به‌تدریج دست بالا را پیدا کرده است. بر اساس این گزارش، نیروهای آمریکایی با هدایت و حفاظت از کشتی‌های تجاری، عبور نفتکش‌ها از مسیر جنوبی تنگه را دوباره برقرار کرده‌اند و مقام‌های آمریکایی می‌گویند کنترل عملی این مسیر اکنون در اختیار آنهاست. اگرچه حجم تردد و صادرات نفت هنوز به سطح پیش از جنگ نرسیده، اما نفوذ ایران بر رفت‌وآمد دریایی در هرمز نسبت به ماه‌های گذشته کاهش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/21631" target="_blank">📅 13:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزارت امور خارجه رژیم :
تمام کشورها موظف هستند از اعمال تحریم‌های یک‌جانبه توسط ایالات متحده خودداری کنند، و تحریم‌های اقتصادی ایالات متحده علیه ایران غیرقانونی و فاقد هرگونه مبنا هستند.
@WarRoom
یاشار : بابا شما که قوی هستین چرا ترسیدین ، تحریم هم که برکته
🥴</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/21630" target="_blank">📅 13:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21629">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ در مصاحبه با شبکه 12 اسرائیل: این موضوع «تنگه» هنوز باز است.
واکنش ایران بسیار ملایم بوده است. آنها نمی‌خواهند ما دوباره به آنها حمله کنیم، این تمام ماجراست. بقیه چیزها مهم نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/21629" target="_blank">📅 13:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21628">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بلومبرگ : قطر در ادامه اختلالات ناشی از بحران تنگه هرمز، وضعیت «قوه قاهره»(حفاظت حقوقی و قراردادی در شرایط اضطراری) برای تحویل گاز طبیعی مایع (LNG) به مشتریان آسیایی و اروپایی را تمدید کرده است. این تصمیم به‌دلیل ادامه محدودیت‌ها و ناامنی در تردد کشتی‌ها از تنگه هرمز اتخاذ شده و بازگشت صادرات گاز قطر به سطح عادی را به تأخیر می‌اندازد. قطر پیش از جنگ یکی از بزرگ‌ترین صادرکنندگان LNG جهان بود و اختلال در صادرات آن، فشار بیشتری بر بازار جهانی گاز، به‌ویژه در آستانه فصل زمستان، وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/21628" target="_blank">📅 12:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21627">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش‌ها از سوریه: نیروهای ارتش اسرائیل (IDF) با آتش سنگین به منطقه تپه بت‌ال‌ورده، نزدیک به شهر بیت‌جان در مناطق روستایی غربی دمشق، شلیک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/21627" target="_blank">📅 12:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21626">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نرخ دلار ۲۰۱،۵۰۰ تومان
دلار کف بازار  ۲۰۰-۲۰۵ هزار تومان
تتر ۲۰۰،۰۰۰ تومان
بیتکوین ۷۹،۷۸۰ $
انس جهانی طلا ۴،۶۰۹ $
نفت برنت  ۸۸،۰۸$
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/21626" target="_blank">📅 12:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21625">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فری استایل یاس به همراه من (یاشار رپفا)
۲۰ سال پیش و زمانه همچنان بی رحم است…
@WarRoom
@RapFA
✅</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/21625" target="_blank">📅 11:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21624">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2p4_cOoC_8Ne-iK_oyNzD3Rb9iuyQ_trgg7pftd0gpMc40TnlVu80MIZ1KxfjHKZeTB96wk5sZSVphvp_cEcyXTZyl-Js9GpI0E8Iv8qDKc6YKVA1e1fzE0Xk1vVrK1KgxdNGG8S0To8prpepa40vixp6Z3OAVmNnDHRP6yp0ozymmoAPP1TxNXWe5HAOgYnZ0quvYQbHPNkvNrWa1lYylh6qacqBA2DNhuYyegPB6DeNI3PdtxnobLXAy2AcvYRqEzGBe2giW15owiwDpHqtcZEe4NeZMY0qICraQirsw7kATumTu68-Nnxpy_OLsGxBJTfZSyhZN_VpbDmmXsdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از دیدبان اتاق جنگ : کاری با دست خط ندارم سطح سواد عرزشی جماعت که برای ۹۰ میلیون نسخه میپیچن (اسرائیل)
@WarRoom</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/21624" target="_blank">📅 11:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21623">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آغاز واریز سود سهام عدالت:
سبد ۴۵۲ هزار تومانی: ۴۴۳ هزار تومان(۲.۲۰$)
سبد ۵۳۲ هزار تومانی: ۵۲۱ هزار تومان(۲.۵۹$)
سبد یک میلیون تومانی: ۹۸۱ هزار تومان(۴.۸۷$)
@WarRoom</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/21623" target="_blank">📅 11:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21622">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhCsDkWZMgtocV2CSijns6Jd15_PdMZBx_BwPUPsZXNaZUVncYqo1LiOCKCPf7G3D4ic0Ywub-orc0h1OJMQLaJKY20x300q5q2cM9Rex0Pfmrh203kk0mhn1Z_t7iEEZx3hIb_7y6Eap3yir_fgAqUVQW_qsEL06YmxnXZjeRtCdUGSOecyWbgqxWEZWa9ISAzj_PwHpc0TCmca7gNjou-A8nPifhEEgbtgwB3D6ZZlp23wzHyH1ozvMYUwqH34hNipoB1WM9Joxlm6h54ZtZrOx5Ya1wOzQTWL1BlSVvrtj2QTiFZJ7Z_henXLhiSYcvqPJJhv0bIBWTARg3Wquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث دوباره:  تنگه هرمز در حال حاضر قلمرو جدید آمریکاست
@WarRoom</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/21622" target="_blank">📅 11:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21621">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aji7UU8QpWPDm5iIHhKQwDK9YcuBX8amq6Z4CXwqnGx26MdjctvmDEwgDQV2Vp4qjySBV4-m_VBi7_IOiItnhsIhV9apFeMi9J3DTdVtr9zGxLGqG8W8FHEytjMz6sRXAhtqNEu4QySW-AfdokYRwxtU25qNTfIEO798cYKDYjFbxbAjed2y8uRnqt8N0VbnmMS4xI-naiW9KtRvk3hK3AIpE_19U0c548l2Mu-AqOpOpPaB_WTeLbZ3R6eaLvwoNptDVIY1E65nwf6_PlLOF6ObFCCPr8YmA5zPyfZ0_LaKcs71Yv4wKjqcVsTH9O4Dj0SrSOW5PyOESXz7aVlRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هارالد پنجم، پادشاه نروژ و مسن‌ترین پادشاهِ در حال سلطنت اروپا، در ۸۹سالگی در بیمارستان دانشگاهی اسلو درگذشت. کاخ سلطنتی اعلام کرد او صبح امروز جمعه ۲۸ اوت، ساعت ۶:۳۵ به وقت محلی، درگذشت. هارالد از ۱۹۹۱ پادشاه نروژ بود و بیش از ۳۵ سال بر این کشور سلطنت کرد. او به‌دلیل کم‌خونی همولیتیک تحت درمان بود و پس از ابتلا به یک عفونت باکتریایی در خون، وضعیتش به‌شدت وخیم شد. پسرش، ولیعهد هاکون ۵۳ ساله، اکنون پادشاه جدید نروژ شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/21621" target="_blank">📅 10:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21620">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی آمریکا (سنتکام)، مدعی شد نیروهای آمریکایی از زمان آغاز محاصره بنادر ایران، عبور حدود
۱٬۵۰۰ کشتی تجاری
و انتقال
۷۵۰ میلیون بشکه نفت خام
از تنگه هرمز را تسهیل کرده‌اند، در حالی که به گفته او، ایران اجازه صادرات حتی یک بشکه نفت خام را نداشته است.
کوپر همچنین مدعی شد هیچ کشتی ایرانی بدون اجازه سنتکام وارد یا از بنادر ایران خارج نشده و تنها در موارد بشردوستانه اجازه تردد داده شده است. به گفته او، تاکنون حدود
۷۵ کشتی تغییر مسیر داده شده
و
۳ کشتی
از زمان آغاز محاصره بنادر ایران از کار انداخته شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/21620" target="_blank">📅 10:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21619">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«محاصره و عملیات “
طرد اقتصادی
” اقتصاد ایران در حال فروپاشی l را درهم خواهد شکست. آمریکا طی ۱۴ روز گذشته با مدیریت خود
۱۳۰ میلیون بشکه نفت
را هدایت و منتقل کرده است.
ایران: صفر.
@WarRoom</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/21619" target="_blank">📅 10:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21618">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ny7jaM5GExw-mdh0HovevS9BcA9wKyN-C-vqXLg9G2yNql0xlSFl1cIWs11ciFXGPJl4r7sEiFQn_uA2yk5-HuN5dq-CcMB3k_mtuKvNysv6u-TxX7UV6WOx6oLMQtW-5ODaYd0rl62OlFIxl7apAsovbbjK4poyFPoj4eaA_CQFtKrqX5fbLkAJVK3ockAWdAYnUAIuUn9sBhdi5COJ0BfjNz3QwUq-ZOweSil8oUC-I8L9_CZ7nr2kM1zZPK4DCokX9HnDyZVMAM3a0ZdeFxpi7mSL9EA7N_oLlmVsrlDba1dKnaM_2E86Pi_EtVADefrbmkWtnu36elXS7efc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ با انتقاد شدید از گزارش جاناتان هانت، خبرنگار فاکس‌نیوز، آن را «بسیار نادرست» خواند و گفت: «من نمی‌خواهم با ایران دیدار کنم؛ آنها هستند که می‌خواهند و برای توافق التماس می‌کنند.» به نظر می‌رسد این یک سوءتفاهم باشد چون هانت در گزارش خود گفته بود مذاکرات مستقیم میان آمریکا و ایران فعلاً در جریان نیست و دولت ترامپ به‌جای مذاکره، در حال تشدید فشار اقتصادی و تحریم‌هاست؛ هم‌زمان کشورهای عربی، از جمله قطر، برای گرفتن امتیاز از تهران تلاش می‌کنند. ترامپ در ادامه از برت بایر، مجری فاکس‌نیوز، خواست «زیردستان بی‌کفایت خود را سر و سامان دهد». بایر نیز در واکنش گفت هانت «خبرنگاری عالی» است و تأکید کرد فاکس‌نیوز اصلاً نگفته ترامپ خواهان دیدار با ایران است، بلکه برعکس، در گزارش به صراحت گفته شده بود ترامپ نمی‌خواهد دیداری انجام شود و مذاکراتی در جریان نیس
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21618" target="_blank">📅 10:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21617">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سازمان عملیات دریایی بریتانیا بامداد پنجشنبه گفت که یک نفتکش در آب‌های نزدیک منطقه «الخصاب» در شمال عمان، مورد اصابت یک پرتابه نامشخص قرار گرفته که باعث آتش‌سوزی در آن شد. @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21617" target="_blank">📅 09:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21616">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3iD1xtRhoST_6oOioeCVgF0WMI2hlGfdZMpBaieuLBf4KZv1FrJY41xjsUWEmwhiuvreESGh7LmG5xdcHkWSTWCJ19mwvj3FWSlPRFibe2tcmrpCnZMgrAIBOZlQV89X8wQE-OdXW8FsLFrT9sj6UNQDD65JnpbD_rXHCVJVx_AW-c6fdKoPEFZ0CHrEJnaw_XNcWF_OhJXcUUiCLOZTQPph9KChoEldnV-Awa3SUaohq8vneB5-aEy7JKqhJU096dRPcQxi-XPhVRFAdAzzaNaU9sI6LeFYf-N84t-Yq-ahnJSKKxEx9XRpSWeV1r4qTKKtqMw8J4H75n0V0H9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایران کشوری رو به فروپاشی است
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21616" target="_blank">📅 09:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21615">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkDxCRZrsMy6qASZ7AxwV10X1HBj4SoHKOL-A5dlkbQuuJorbMoUKdeCA6ltG-2DcFW1WVrPU1lWZWo1QAm4iYBZjOSO-dHGZqRSDPMj7yL21n7UDxEpj08S8Zl__Pe0e3HurkTFWcMK9BZs1TWPeobT3IE9nf_Ka9OMiDDKdhRbUjLp1sZwGpfqnfMlTrX5nqP3ZKjyPaHJm3MlsGvEk6q52n3B-QnisXcNCHpKxIcT8NprSfNCbbckjB8zTBCajAa0uwYetkRM8xNKHnLwbf8vvpLcvrSzUAQZEdmt-tLT6YAZMMfu9ipHJNvLBf2b02ZA3mO2oD30hdXTJCJ2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ سوخترسان آمریکایی و ۲ پهپاد در خلیج فارس در حال مأموریت هستند ، بعد از مدتها این حجم مشاهده میشه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21615" target="_blank">📅 00:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21614">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6860a3c4.mp4?token=pS98_7qbmMqJrMjAxpLyOFT3oNlfJ0p_yJPi7BSpzFaJZf_FdId0pT5oLrmIjWNW0wTa5NzJPr4CEManM0w2Tr6AlYBeZZmlcUxBrj3ZVUQLY_mwTLWDfB7xGVLhi61HTGz1OkUwlP6JCQF5aKgiJpKTMdBDhwuAo08WfSYKhNj_QQkI8er1U271ivJ9v_bl4foo8frFAMlwmoaUc1RvgXeYmg6lPsNd5mcTZGUALVVTgeiPYL5MnYcMb9H-rzxoM9ZInQQfwVTto8DGC_DshadmrDEKskorK1ZKMdc9AgvWuJlg4X5N7dHH0yBje-23WUTWvdwGc6A9Z0h6RHQhuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6860a3c4.mp4?token=pS98_7qbmMqJrMjAxpLyOFT3oNlfJ0p_yJPi7BSpzFaJZf_FdId0pT5oLrmIjWNW0wTa5NzJPr4CEManM0w2Tr6AlYBeZZmlcUxBrj3ZVUQLY_mwTLWDfB7xGVLhi61HTGz1OkUwlP6JCQF5aKgiJpKTMdBDhwuAo08WfSYKhNj_QQkI8er1U271ivJ9v_bl4foo8frFAMlwmoaUc1RvgXeYmg6lPsNd5mcTZGUALVVTgeiPYL5MnYcMb9H-rzxoM9ZInQQfwVTto8DGC_DshadmrDEKskorK1ZKMdc9AgvWuJlg4X5N7dHH0yBje-23WUTWvdwGc6A9Z0h6RHQhuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : هر کسی میخواد برقش قطع نشه میتونه از بورس برق با قیمت آزاد خریداری کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21614" target="_blank">📅 23:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21613">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">محسن کج بند رضایی، دبیر شورای امنیت ملی، ادعای وجود توطئه ایران برای ترور پسر دونالد ترامپ را «دروغی بزرگ» دانست و گفت این ادعا ساخته بنیامین نتانیاهو برای فریب و ترساندن رئیس‌جمهور آمریکا است. او مدعی شد نتانیاهو با انتشار گزارش‌های جعلی درباره «توطئه ترور ترامپ» او را ترسانده و بر تصمیم‌گیری‌هایش اثر گذاشته است. رضایی افزود: «اگر تصمیمی بگیریم، هیچ‌چیز مانع اجرای آن نخواهد شد؛ اما این گزارش‌ها صرفاً یاوه‌گویی‌های نتانیاهو هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21613" target="_blank">📅 23:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21612">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دیوید بارنیا، رئیس پیشین سازمان اطلاعات خارجی اسرائیل «موساد»، می‌گوید جمهوری اسلامی در نهایت در اثر ترکیبی از فشارهای اقتصادی، عملیات علیه حکومت، و اعتراضات مردم ایران سقوط خواهد کرد، و تحریم‌ها به تنهایی برای رسیدن به این هدف کافی نیستند.
@WarRoom
🚨
🚨
🚨
حتما چنل رو دنبال کرده
🤣
🙌🏾</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21612" target="_blank">📅 22:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21610">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش پرتاب موشک زد کشتی از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21610" target="_blank">📅 21:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21609">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داده است که دونالد ترامپ با بازگشت به چارچوب اولیه توافق ژوئن با ایران مخالفت کرده و ترجیح می‌دهد با تشدید فشار اقتصادی و تحریم‌ها، تهران را به دادن امتیاز وادار کند. در مقابل، ایران تأکید دارد که بازگشایی تنگه هرمز باید بر اساس همان چارچوب ژوئن انجام شود؛ چارچوبی که شامل کاهش تحریم‌ها و محدود شدن فشارهای آمریکا بود. پاکستان، عمان و قطر نیز برای میانجیگری و نزدیک کردن دو طرف تلاش کرده‌اند، اما مذاکرات تاکنون پیشرفت چندانی نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21609" target="_blank">📅 21:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21608">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ به شوخی می‌گوید:
ما یک خلیج(مکزیک که شد آمریکا) داریم. ما یک دریاچه(انتاریو که شد آمریکا) داریم. حالا چیزی که نیاز داریم یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا اقیانوس آرام را تغییر دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21608" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21607">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خبرنگار: با کدام رهبران در مورد قطع روابط با ایران صحبت کرده‌اید؟
ترامپ: چیز زیادی برای صحبت وجود ندارد. ما نمی‌خواهیم با آنها صحبت کنیم. تنگه هرمز باز است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21607" target="_blank">📅 21:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21606">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: ایران در وضعیت بسیار دشواری قرار دارد و نمی‌تواند حقوق سربازان خود را پرداخت کند.
اقداماتی که ما در مورد ایران انجام می‌دهیم، به این معنا نیست که ما از گزینه نظامی چشم‌پوشی کرده‌ایم.
ما نمی‌خواهیم با ایران صحبت کنیم و قصد نداریم جلسه‌ای با آن برگزار کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21606" target="_blank">📅 21:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21605">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شرکت روکِتسان ترکیه موشک کروز «چاکیر» را با موفقیت از یک پرتابگر زمینی آزمایش کرد
. این آزمایش نشان داد چاکیر علاوه بر پهپاد و دیگر سکوها، قابلیت شلیک از خودروهای زمینی را نیز دارد و می‌تواند اهداف زمینی و دریایی را با جستجوگر تصویربرداری مادون‌قرمز هدف قرار دهد. برد این موشک بیش از ۱۵۰ کیلومتر اعلام شده است.
جنرال یاشار گولر، وزیر دفاع ملی ترکیه،
نیز درباره تسلیحات جدید روکِتسان گفته است: «ما این سلاح‌ها را عمدتاً برای بازدارندگی می‌خواهیم، اما اگر استفاده از آنها لازم باشد، ترکیه بدون تردید از آنها استفاده خواهد کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21605" target="_blank">📅 21:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21604">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ: هیچ نگرانی‌ای از حمله روسیه به ناتو ندارم
دونالد ترامپ در گفت‌وگو با آکسیوس گفت که «اصلاً نگران» حمله احتمالی روسیه به کشورهای عضو ناتو نیست و تأکید کرد: «هیچ مشکلی وجود ندارد.» او همچنین گزارش‌ها درباره سفر محرمانه جان رتکلیف، رئیس سیا، به مسکو برای هشدار به روسیه درباره حمله به اعضای ناتو را رد کرد و گفت این سفر «یک کار معمول» بوده و «هیچ پیامی در کار نبوده و هیچ چیز غیرعادی‌ای» رخ نداده است. با این حال، گزارش‌هایی از جمله گزارش وال‌استریت ژورنال و CBS مدعی‌اند که رتکلیف در مسکو به روسیه درباره حمله به ناتو هشدار داده است؛ موضوعی که تاکنون از سوی مقام‌های آمریکایی یا روسی به‌طور رسمی تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21604" target="_blank">📅 20:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21603">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رئیس سابق موساد اسرائیل:
اجتناب از یک جنگ دیگر با ایران غیرممکن است
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/21603" target="_blank">📅 20:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21602">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏ انفجار در اربیل عراق , منابع عراقی از حملات پهپادی به گروه های کورد در منطقه سوران در اربیل خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21602" target="_blank">📅 20:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21601">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHWtvBzjzAEm-oLThrVVVNTUH4b2tZ28jP29GWdjxSY9BhtmljoNMV8aY-PI-aOZkSYO50rKjVmvrcHo9bsLxKMOdSn9r2nXheFYjdaUBoWifT9nbh9OxKrgIRm9reSh0Qn600DruGsKPM15gh6XLgrSPY9h6DFIdtARPIVcXjwiLE8NbChtGgkHqiROXiPsKx_9_2Jkb10WQ7PJC_pZjB0-h329rVsYcXhMpU_pYJLjITlnyzlFZRLgGK0OSVKfy3lCkcHAStB9dMvwVFA2VYSlKkqvVoOcMzFsbsvnY5CXUNb_XyN1fk2qO2Gj3v5y6VoQK2WUXxGQq17rnYzClQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امبر اولر، ۴۱ ساله و دختر شایسته میشیگان، امشب در مسابقه میس آمریکا ۲۰۲۶ در میامی روی صحنه می‌رود. اما تنها پنج سال پیش حدود ۱۳۶ کیلوگرم وزن داشت و پزشکش به او هشدار داده بود که در مسیر یک «مرگ زودهنگام» قرار دارد. پس از این هشدار و تجربه‌ای تحقیرآمیز در یک پارک ترامپولین، تصمیم گرفت زندگی‌اش را تغییر دهد. او طی بیش از سه سال با رژیم غذایی و ورزش حدود ۱۷۰ پوند، معادل ۷۷ کیلوگرم، وزن کم کرد و در سال ۲۰۲۴ وارد دنیای مسابقات زیبایی شد. اولر که مادر سه فرزند است، امسال به‌عنوان میس میشیگان آمریکا انتخاب شد و اکنون در میان ۵۱ شرکت‌کننده میس آمریکا ۲۰۲۶ قرار دارد؛ و در ۴۱ سالگی مسن‌ترین شرکت‌کننده این دوره است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21601" target="_blank">📅 19:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21600">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مقام آمریکایی به فاکس نیوز:
توافق ایران و عمان برای ما اهمیتی ندارد؛ فشار اقتصادی را ادامه خواهیم داد و مذاکره‌ای با ایران نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/21600" target="_blank">📅 19:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21599">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزیر انرژی آمریکا: به ایرانی‌ها گفتیم می‌توانند با همکاری با ما، فقط برای تولید برق انرژی هسته‌ای داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/21599" target="_blank">📅 18:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21598">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ارتش اسرائیل: دیروز، یک فرمانده از شاخه نظامی حماس را در حمله به منطقه خان یونس به هلاکت رساندیم.
همکنون نیز ارتش اسرائیل در حال حملات هوایی به جنوب لبنان می باشد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21598" target="_blank">📅 18:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21597">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3ZqnTqnF5OIV3kdBUwfWCnMW0lRTNt-F6N_-m-ru4gR4cnra0FUkzrJ5evtr6ZbSedVVyWv6tZZq4NMDiO_Y-qgWUmjmIQfGGX-kFvePyVhnp6WLwmKe-0St1BBpAAIKG7jvEjWRFn33GmntyP7E8FgqDj8EuiH9hYagn-FIWowUoO_csqvIaNdAuP7_zBfSBRqqFba9hyRiiZK3z66tGV7wlI6Th8nIgeknm3OOZMgrvMdwTU2blZi2A6AV_3x7u5AT_QEvaPo27o1iqyZpV6QNPPZiJY14LSXBokmqUolwWHzKGtNgAO_0iKJt63Q1pMb0-bOTkMgI-kNSrqXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماهای جنگ الکترونیک E/A 18G نیروی دریایی ایالات متحده در حالی که ایالات متحده همچنان به اعمال محاصره علیه ایران ادامه می‌دهد، بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند. تا ۲۷ آگوست، نیروهای سنتکام ۷۵ کشتی تجاری را تغییر مسیر داده، ۳ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده‌اند تا از رعایت مقررات اطمینان حاصل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21597" target="_blank">📅 18:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21596">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21fec76a7.mp4?token=CIEXbgJ6alw3UfU-tTpqF4AWMvAFajKedzE_beZGpEHdKeSc2OjU4E_7SopbbMJcqH_1FsEY611fhmnI-7o3SkFMlx40Am2pbKoC54JALkoKsy1HmT1js1_lk9V67Pb5I2DYSw9fGpVRh12-EfWvA_cKXFs7B44tDBtpUMNbYJ3XZG9aP6faqJJV_kUNDQfYUXspwKEN7EkYyukxoZWs3c91MVf8KtQ0oQ9ngz025oJRHd5CfOlNdYsVWS7w1rPrmq5px4Sc9m4Utm3ZC3Nk0KWv8X8NE9bECJnxTJBejSrkxsCufkq6sFkFq2yTLRvPVQQc9vqpygeDsYLqYI1uJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21fec76a7.mp4?token=CIEXbgJ6alw3UfU-tTpqF4AWMvAFajKedzE_beZGpEHdKeSc2OjU4E_7SopbbMJcqH_1FsEY611fhmnI-7o3SkFMlx40Am2pbKoC54JALkoKsy1HmT1js1_lk9V67Pb5I2DYSw9fGpVRh12-EfWvA_cKXFs7B44tDBtpUMNbYJ3XZG9aP6faqJJV_kUNDQfYUXspwKEN7EkYyukxoZWs3c91MVf8KtQ0oQ9ngz025oJRHd5CfOlNdYsVWS7w1rPrmq5px4Sc9m4Utm3ZC3Nk0KWv8X8NE9bECJnxTJBejSrkxsCufkq6sFkFq2yTLRvPVQQc9vqpygeDsYLqYI1uJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو در ویدئویی از پیش ضبط شده مدعی شد که هنگام پخش این ویدیو او در ایران یا در پرواز ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21596" target="_blank">📅 17:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21595">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏یسرائیل کاتس، وزیر دفاع اسرائیل، در جریان ارزیابی امنیتی با ارتش اعلام کرد: «مهلتی که تعیین کرده بودیم به پایان رسیده است. از این پس هرگونه پرتاب بالن یا بادبادک از غزه به سوی شهرک‌های جنوب اسرائیل با پاسخ سخت روبه‌رو خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21595" target="_blank">📅 17:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21594">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">معاون وزیر نفت ایران: حدود ۴۰ درصد از ظرفیت آسیب‌دیده میدان گازی پارس جنوبی به تولید بازگشته است
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21594" target="_blank">📅 16:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21593">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">@WarRoom
losing my religion</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21593" target="_blank">📅 16:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21592">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وال استریت ژورنال به نقل از منابع آگاه گزارش داد که هدف از سفر جان راتکلیف، رئیس سازمان سیا، به مسکو در روز سه‌شنبه، هشدار دادن به روسیه  بود که از حمله به ناتو و کمک به ایران خودداری کند. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21592" target="_blank">📅 15:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21591">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b30ac12425.mp4?token=lA3ExWsTTx2AwGGj6wo8bmB6h7Z2zWKMqOuAtiAHtkC8bDFTvbeQ07oS89HQbq8WFBkJ0oKyimGAFdk_S3OqjAlqiwgjR3JTMgBA9D6zLWgxYDieoW9PoTYlqEARDgU0ZAht7P3Xm3Qq2dsVPY_ARl20Ii6JhULMOvjFFl2bKx67qdsiL1k3LrK39LsT83xOHv6snN34BgljoN_0TO8WgLZdk_avSrg8YF1hjuvUqa8bkYpXMPlrR1CDdOq9pmzu4PWI2sL69IQBpzqYYGVcGuROHqCmaP439ZzridJpweyic-KOFbrju-cvihECcx4V5R3qY3KcEYL0qVI6KFblHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b30ac12425.mp4?token=lA3ExWsTTx2AwGGj6wo8bmB6h7Z2zWKMqOuAtiAHtkC8bDFTvbeQ07oS89HQbq8WFBkJ0oKyimGAFdk_S3OqjAlqiwgjR3JTMgBA9D6zLWgxYDieoW9PoTYlqEARDgU0ZAht7P3Xm3Qq2dsVPY_ARl20Ii6JhULMOvjFFl2bKx67qdsiL1k3LrK39LsT83xOHv6snN34BgljoN_0TO8WgLZdk_avSrg8YF1hjuvUqa8bkYpXMPlrR1CDdOq9pmzu4PWI2sL69IQBpzqYYGVcGuROHqCmaP439ZzridJpweyic-KOFbrju-cvihECcx4V5R3qY3KcEYL0qVI6KFblHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21591" target="_blank">📅 15:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21590">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شیخ محمد بن عبدالرحمن آل ثانی، نخست وزیر و وزیر امور خارجه قطر، امروز در تهران با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، دیدار و گفتگو کرد
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21590" target="_blank">📅 15:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21589">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آتلانتیک : کاخ سفید به‌جای تشدید عملیات نظامی، به سمت تحریم‌ها و فشار اقتصادی بیشتر علیه ایران رفته تا هم فشار بر تهران حفظ شود و هم جنگ به موضوع اصلی انتخابات میان‌دوره‌ای تبدیل نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21589" target="_blank">📅 14:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21588">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">روزنامه نیویورک‌تایمز گزارش داده است که عربستان سعودی در پی هفته‌ها حمله حوثی‌ها به اهداف سعودی، خود را برای احتمال آغاز دور تازه‌ای از جنگ در یمن آماده می‌کند. بر اساس این گزارش، حملات متقابل میان حوثی‌ها و نیروهای مورد حمایت عربستان شدت گرفته و خطر تبدیل‌شدن تنش‌ها به یک درگیری تمام‌عیار افزایش یافته است. ریاض در حال تقویت مواضع دفاعی و نیروهای یمنی متحد خود است و در صورت ادامه حملات، احتمال اقدام نظامی گسترده‌تر علیه حوثی‌ها وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21588" target="_blank">📅 14:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21587">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfkbV12XB6oSUHOaHa8DYDAh4gaqSC_U4M89fHb23fk4Dm8wEiPCTkGsN8gsXNaV123_TNiisexpI-7MX0dZAott-7SDYC2UUrPrbjW7l9dS_fvQ3wI9HwwFdG5DPOBKBirGAUv1nqlIICzBZTdjgSq2O0oHPeje-E-3VBnTTb17JXtu4doS-OVW4kvJS7Ddbwvn_PpPitdvSN5PgId1b4z25QstHCxvYVuVJfEOgI7PkpAMhEYAogPl43gDQpZb0iWaY3lOo4xeo466_BtWzBBjEm9wDQr66BU1nutqPltqfDpLk6zFjvVG28wW4DiQ3D7KeHHTxtSR9SC-tu2rHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون گزارش آتشسوزی بزرگ در پادگان سنندج
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21587" target="_blank">📅 12:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21586">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Bitcoin = 80,080$
🚀
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21586" target="_blank">📅 12:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21585">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرنگار: آیا می‌توان گفت که در حال حاضر حملات نظامی علیه ایران متوقف شده‌اند؟  پیت هگست: نه. اگر لازم باشد از حملات نظامی استفاده کنیم، این کار را انجام خواهیم داد. اگر ایران آن‌قدر احمق باشد که زیاده‌روی کند یا با ارتش آمریکا درگیر شود، ما هر کاری را که لازم…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21585" target="_blank">📅 12:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21584">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به گزارش MS NOW، یک ملوان ۱۹ ساله نیروی دریایی آمریکا از خدمه ناو هواپیمابر «آبراهام لینکلن» در ۳ اوت ۲۰۲۶ به دریا پرید؛ همسر ۱۹ ساله‌اش هم این اقدام را تلاشی برای خودکشی عنوان کرده است.
او پس از حدود یک ساعت در آب نجات یافت و حدود پنج روز در مرکز پزشکی نیروی دریایی سن‌دیگو تحت مراقبت بود. همسرش می‌گوید او پس از تولد دخترشان در فوریه، چند بار درخواست
مرخصی پدری
کرده بود که رد شد و پیش از حادثه نیز درباره وضعیت روحی خود با فرماندهی و کادر پزشکی ناو صحبت کرده بود. به گفته او، پس از حادثه مراقبت‌های سلامت روان محدودی دریافت کرد و پیش از نخستین جلسه درمانی، دستور بازگشت به خدمت گرفت. اکنون این ملوان با
اقدامات انضباطی نیروی دریایی
روبه‌روست و طبق اسناد اتهامی، به
تمارض (Malingering)
و
غیبت بدون اجازه
متهم شده است. نام او به دلیل حفظ حریم خصوصی منتشر نشده است. این زوج یک
پسر سه‌ساله و یک دختر نوزاد
دارند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21584" target="_blank">📅 12:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21583">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه ویس های دیروزم رو گوش کرده باشین ، خودتون صحبت های همه را میشنوید بعد تصمیم میگیرید به هر حال ،ما در راه شخص شخصه، فقط شخص خود شاهزاده ادامه میدیم و با اطراف کاری ‌نداریم و این بحث اینجا به پایان میرسد و تحقیق و تصمیم بیشتر با شما است
🙌🏾
اتحاد باید حفظ شود و رمز اصلی است همچنین انتقاد هم اگر محترمانه و درست بیان شود نیز باید شنیده و پاسخ داده شود
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21583" target="_blank">📅 12:25 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
