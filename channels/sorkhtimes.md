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
<img src="https://cdn4.telesco.pe/file/vP-6_qDtNeRC8pQMHUYdqrWO0NT6C0u-IY6vAmDbFOmJ8HmnDTj69JQdg1rQ0HThugrjzWKcWwlusRxb9DBu9AL1fF78alIAEDgcw5PrPB3p2MrGWJ3SFjVM2mZZYscKOTBeWZo8H5K0J9fzpGQdyN4BkfggooAGyQpSxkWdRuw97Oqhb90HNUOiA35hl_X9jWYdpeP-WLoSM0gjq52_q3v7QPcE4IvUKRT2ntcjtUzmxdq0zbgOuFB239qI9e7bDmu2Az97nBAUUJu013d50wCxYWqfC3QXUJvm0DbkC3MjSl_h4JQXAtAUWWsndU4apSCWSgSgcUDvZgLJBHPs2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 15:42:25</div>
<hr>

<div class="tg-post" id="msg-136813">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 393 · <a href="https://t.me/SorkhTimes/136813" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136812">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/136812" target="_blank">📅 15:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136811">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/136811" target="_blank">📅 15:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136810">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jL6xED61iOQyRv-cT_MAC_sdo--Hc5mRAeckrNrW4frw82XfMgT1Rp_0NU7QAliV48P9YXl4xEDevvRYTAs9XhDIwCWj6n27aF6nX9iNdnff8rkleKGJPqG_dSZmZZlAkn4YQAJnZfmOabjq42f9-IVVeeaSrJYOCskXq2WV5Ofy3zp0rJJPAbuoBn95_o8N_WXXWoDmfUo_1aJMYZYVvkiHAytTqFfJVwoZ_Ss9qDzIMTxYD7shOLciLfFtNhRij9U5rKH--WhX9J3byD9PzQlH0g4ji-HcsEz7zKYfbWfuzeTP9XdoFg39wtRFEWqGkPErxibKXXxOpGw0hLOp9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کاظمیان به گل‌گهر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SorkhTimes/136810" target="_blank">📅 15:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136809">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/136809" target="_blank">📅 15:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136808">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/136808" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136807">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/136807" target="_blank">📅 15:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136806">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBvg9y8gsgwcgnCZ8GWb8JMRMd7ybnbKKeqS8zLQcxYsVYmo9ZbNbm4Z-7RjVknr2yi-Kcur84X1EXIPU91upkXdfc1Eq5lw_yNGS2MtxvXQIeFnGtqF_gQg-Wr9w0ygxcRGNop_RSM-ywoo3NovLgBFQfNLvHoahjmykoQVxk9JCm7XHQWVFGKF0cJL3DuNdexARuw7haxF01AW72L9VRRtucvDZ-vm7auJUYkumxZ07xTnYiL4472B85IjDNED7JPKejK0e--O1LjqNxXAG9ehuyXLGuaxco6czsWj9AJdF94OtHU-9VkYAsuCzYlfaP4UrsWZPBQu9qvHUHQZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
وقتشه پوکرو حرفه‌ای بازی کنی!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/136806" target="_blank">📅 14:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136805">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
❌
باشگاه نساجی گفته از اقدام پیمان حدادی به شدت ناراحت شده و میخواهد دانیال ایری و کسری طاهری را به باشگاه های دیگری بفروشد
😀
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/136805" target="_blank">📅 14:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136804">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
پرسپولیس میخواد رفیعی رو برای بازگشت راضی کنه؛ کاری که خیلی سخته چون امیررضا میخواد جایی باشه که بهش بازی برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/136804" target="_blank">📅 14:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136803">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
شنیده‌ها: با توجه به عدم جذب اخباری احتمالا یا رفیعی برگرده یا گوهری که بازیکن آزاد جذب بشه
🚨
پ.ن: برای گلر دوم رفیعی یا گوهری هم جوابه بعید برن سراغ گلری که قرارداد داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/136803" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136802">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه تراکتور پاسخ هایجک محبی رو به پرسپولیس داد و محمد قربانی تا ۷۲ ساعت دیگر تراکتوری میشه/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/136802" target="_blank">📅 13:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136801">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
به دلیل تعلل مدیران باشگاه پرسپولیس در جذب کسری طاهری و دانیال ایری حضور این دو بازیکن در پرسپولیس از سوی شهاب زندی مدیرعامل باشگاه نساجی منتفی شد /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/136801" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136800">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/136800" target="_blank">📅 13:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136799">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
به دلیل تعلل مدیران باشگاه پرسپولیس در جذب کسری طاهری و دانیال ایری حضور این دو بازیکن در پرسپولیس از سوی شهاب زندی مدیرعامل باشگاه نساجی منتفی شد /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/136799" target="_blank">📅 13:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136798">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/136798" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136797">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/136797" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136796">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
عجیب اما واقعی؛ پرسپولیس و سپاهان داداشی شدن و پیمان حدادی کمپ شهید کاظمی رو در اختیار سپاهان گذاشته تا اونجا تمرین کنن…!
☹️
☹️
🫥
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/136796" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136795">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECnPGG8LS9qpTrXUhRehnKP63xKY-2zvJORu_gwOh58eJVjSTW0OUXiDlEhQCVw-kee3b7NIByQsgrBgW01HX1nqX7q9tV9t_6cDVgLrSDBS6PkOD_1LHRjuN0fQCUYRGw5jKRwqTggDe2KQSa0OsAA3kgZT8VP_YoZqW-su84rqTPfj0Wf_H6nS1FpIv99E0__BcJA4KdYj3nuOh17_pXrH9_V8NJkqacvtfwweBRn0-0q5LytAwHx2GdOqVYUrwKHUhX20_ypkavhkUMCtPzM1hrFzpHC22CcP_WAyjZC8uvS6wDyIebOMdY8IbxdTpxBfBoM-muZaIBT6JH3fSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
باشگاه سیرجانی با انتشار تصویری از محمدرضا اخباری به صورت رسمی اعلام کرد این دروازه بان با قراردادی دوساله به گل گهر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/136795" target="_blank">📅 13:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136794">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
#ورزش‌سه : ممکن است به زودی یک قرارداد معاوضه به اضافه پول نقد بین دو باشگاه پرسپولیس و سپاهان شکل گرفته و احتمال دارد نام‌هایی مانند محمدامین کاظمیان، حسین ابرقویی و آریا یوسفی در این معامله جای پیدا کنند. حتی احتمال رخ دادن این اتفاق برای محمد عمری نیز…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/136794" target="_blank">📅 13:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136793">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2EJX4XCT71kmySEuaR62P2JVSthM165jmkWmAIARAz2ecMTyuCgR6lsTXhjbqcKJ02MdqikR1Oq7pMLkgykLGchcn08rBuAPYA500OXtDIwDk2z6JvPIYxvKTBqr7T5xRnTPkXkTWJ4MKh77YZ3mkF2WxJOW0BmIYyVSkCXHrJTLChpeQgBecLFgrGO_ZIqFW24V3IrWhza6bhtHLkIHmtLJMFjivXkXuUCTCQVuA7GgoGydDXfGEWvJNcLV6IZHjainhs3CUpxLRgrrXYRzr9TOAmS5GReLochLvITZKSXzUVm5bxbaE9XxvoESmq1Vjs0wr1RtywxRJmWuRFvGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووووری :
محمد قربانی به تراکتور پیوست!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/136793" target="_blank">📅 13:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136792">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">➡️
➡️
➡️
➡️
⬅
تارتار به دنبال پاکسازی پرسپولیس!
⏳
💬
مهدی تارتار پس از بازگشت از ترکیه قصد دارد چند نفر از اطرافیان باشگاه را به دلیل لو رفتن ترکیب تیم کنار بگذارد.
⬇️
سرمربی پرسپولیس به چند نفر مشکوک شده و پیگیر این موضوع است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/136792" target="_blank">📅 10:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136791">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
🔴
ورزش سه: هیچ کدوم از هافبک های پرسپولیس بازیساز نیستن و دو خرید جدید پرسپولیس در این پست (لطیفی فر و پورعلی) بیشتر وظایف دفاعی دارن. پرسپولیس اگه پست 8 بازیکن نخره تو شروع فصل به مشکل میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136791" target="_blank">📅 10:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136790">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
❌
امیر عابدزاده که به تازگی بازیکن آزاد شده و احمد گوهری از گزینه‌های باشگاه برای گلر دوم می باشند ناگفته نماند وضعیت اخباری همچنان مبهم است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136790" target="_blank">📅 10:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136789">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌀
🌀
🌀
پرسپولیس خواستار جذب مدافع تراکتور شد
🌀
باشگاه پرسپولیس با ارسال نامه به باشگاه تراکتور خواستار جذب صادق محرمی مدافع تیم فوتبال تراکتور شده است.
🌀
محرمی پیش از این سابقه بازی در پرسپولیس را داشت و از همین تیم راهی دیناموزاگرب کرواسی شد.
🌀
باشگاه تراکتور…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136789" target="_blank">📅 10:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136788">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
صادق محرمی درخواست خروج از باشگاه تراکتور را داده و قصد ندارد فصل آینده در این تیم باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136788" target="_blank">📅 10:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136787">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/136787" target="_blank">📅 09:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136786">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
فرشید حقیری: یاسین سلمانی دیروز پشت دروازه تمرین کرده و احتمال زیاد می‌ره مازاد تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/136786" target="_blank">📅 09:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136785">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/136785" target="_blank">📅 09:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136784">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
خبرنگار پرسپولیس:
🔴
امروز محمدمهدی زارع و پویا پورعلی در تمرینات عالی ظاهر شدن .تیکدری هم مثل همیشه خوب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136784" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136783">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
🔴
گزینه بعدی پرسپولیس برا گلر دوم گوهریه آماده س ولی برخلاف اخباری سهمیه لیگ برتری  حساب میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/136783" target="_blank">📅 09:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136782">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxrBg7B5tVsdMVtg6rnQkAp0iwbc0vVpW6BK-bsH-z3JxQ42pwYVxiAaKmDFa2KjUUw7fWtKf0m23fu6EEVDhlotYxOgfSLGrbvyBox4YV9V8DflkXrn106Jm0edSRPk8tY_CeY2wCILBBCHXDw2x7y287AEVDdfwkwrTlch1YeoK3aoRPVNaORFMbphvZXKaG5qQPrubafxOuw4BdfLMVql1hM49OZowWhSg-fAYA2jnwn_f7-LRteOuinoHRt1_jeFbrnsBA6TX7VyBpQmYbBguhhfD3sCTvN0mz1OTIg3nPfY2VeunnpU3dNfehTWQr2Tdr7G_6mdl3ZWCGiZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کریم باقری : پرسپولیس فصل گذشته مشکلات زیادی داشت و من خودم شخصاً جزو کسانی بودم که از عملکرد و نتایج تیم راضی نبودم اما نسبت به فصل آینده امیدوارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/136782" target="_blank">📅 09:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136781">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgN3Ar78lUMA37-yQem0fEi8HQTxOUlR61lSMHXEyXVSDl_0yU9mSTVPjOAHp4I2qV1rZZ5DtN2HaQ5F6EFkz67mvu0sWrofrBHSZy6UJ0izCdABWFglavMxYiTKvi2gNYfTFgenGaocLhegmr5JVVYBXm8T_PeVzjdf3z9HyrbMRwgWp8Z_wNF4nOC-kknE8oxIi6W6sAKr6eDpn4RA5a0aSl3zX7d1604PYPSp2AVkhn55MBj4f5j74NOZtf3MACEdnrNQg3aGhL_58b40qMZFAmhSnaRWuMruK8-cnka-iY1UZ0lOtUZaWonuC80WW3lro0Csd9LKK5HGjG42Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبح 5/5/5 تون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/136781" target="_blank">📅 08:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136780">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Guk_EbYDF4Ye3z7-wQtGfQOnrdh2bn9PJayxqsND6BxcPN9LYew09de4eG9hXNCr3eLw_wTH76nFBLecg3ELmojRMf8e2F7pE_5lsmw1zn-gOns4fTipAlOW8XsWQ-Hqb83PZP-mVg4rHpF81NxQgUo6S9ZrhDWd-qEWdDgiCb4E3A4U7-zWrlq_lbv5chiK4ktrxXJoVo_tx22Zfjx977IqU-gOh87nIB1f88eEt3NBHVk1ItdritICkoD_f78XhgAGYUk87VSsVkwGeQvnZfdSh2ulGshEGV8Tw2rXRCqrGlSVTPF1vc0H1DkGmUwMSP5_cCPcW9SnUu0dAg3-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ربات وینکوبت در دسترس تمامی کاربران
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136780" target="_blank">📅 01:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136779">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
✅
✅
نظر شخصی :یا به گندمی اعتماد کنید که  الان تو اردوی تیم هست .یا رفیعی و برگردانید ...یا به امثال آرشا شکوری و آرمین عباسی اعتماد کنید و جذبشون کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136779" target="_blank">📅 00:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136778">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">➡️
➡️
➡️
➡️
⬅
تارتار به دنبال پاکسازی پرسپولیس!
⏳
💬
مهدی تارتار پس از بازگشت از ترکیه قصد دارد چند نفر از اطرافیان باشگاه را به دلیل لو رفتن ترکیب تیم کنار بگذارد.
⬇️
سرمربی پرسپولیس به چند نفر مشکوک شده و پیگیر این موضوع است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136778" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136777">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
تارتار اسم یه مهاجم خارجی رو به باشگاه داده و درصورت جدایی بیفوما و گرا مدیریت برای جذبش اقدام میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136777" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136776">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136776" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136775">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136775" target="_blank">📅 00:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136774">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
مهدی طارمی: این جام‌جهانی فاجعه بار است، فاجعه‌ بارترین. فیفا باید هر مشکلی را که وجود دارد، حل کند. اما متاسفانه از همان ابتدا نتوانستند چیزی را حل کنند. اکنون دوباره برای رفتن به تیخوانا سفر خواهیم کرد، بدون ریکاوری. این منصفانه نیست. اگر این از نظر فیفا…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136774" target="_blank">📅 00:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136773">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
وکلای باشگاه پرسپولیس گفتن جذب کسری طاهری خیلی پر ریسکه! باشگاه پرسپولیس مجدد از یه وکیل خارجی داره مشورت میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136773" target="_blank">📅 00:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136772">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136772" target="_blank">📅 23:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136771">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔘
🔘
امیر عابدزاده هم تنها گلر بزرگسالی هست که سهمیه لیگ برتری محسوب نمیشه چون لژیونر بوده   جذب گلر بزرگسال اشتباه بزرگیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136771" target="_blank">📅 23:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136770">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔘
🔘
امیر عابدزاده هم تنها گلر بزرگسالی هست که سهمیه لیگ برتری محسوب نمیشه چون لژیونر بوده   جذب گلر بزرگسال اشتباه بزرگیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136770" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136769">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
شنیده‌ها: با توجه به عدم جذب اخباری احتمالا یا رفیعی برگرده یا گوهری که بازیکن آزاد جذب بشه
🚨
پ.ن: برای گلر دوم رفیعی یا گوهری هم جوابه بعید برن سراغ گلری که قرارداد داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136769" target="_blank">📅 23:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136768">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136768" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136767">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚠️
⚠️
اخباری قرار بود امشب رسمی بشه ولی انگاری تماس مهدی رحمتی باعث شده به فکر رفتن به گل‌گهر بیفته ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136767" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136766">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🫥
🫥
حالا باید بگردیم دنبال دروازبان مطمین برای ذخیره پیام ...حالا چرا این وسط چرا رفیعی رفت دلیلش معلوم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136766" target="_blank">📅 23:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136765">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136765" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136764">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqvbi5qyLOA-OeCVaGoZRMdmRKY2vAAV86afDd0bKShrNzo7yozRm_o-7szt5r34h2KaBgAcac1bXeakrXd1O14dO2uJxqPMHVACoxUq5j_sF3djLo1UPxKlhFwRCeYUAmjO-XC_bjsgdQvbbqPvITMRc5cP0E_cw6J1yV-ROpBq1tD1pBHGEZsjQ7LrOO-e2dADNh2ZtyuwxYk-IKejvBo7ts40Slcrw7dLrgR9Mrb8utpGrjD-ml50fYJnknbz5wrsOSSG5Fi6e9fRYG2J1fn8e2oUxm51YepMLIEGU3P_nVx7G11o7mf0OTaGTx9dR1W0UpveV5ofXO6y_V4DFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📸
از بازی دوستانه امروز با نماینده فوتبال مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136764" target="_blank">📅 23:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136763">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136763" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136762">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136762" target="_blank">📅 23:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136761">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
محمدرضا اخباری تا دو ساعت دیگه قرارداد شو امضا می‌کنه / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136761" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136760">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔻
⚽
ویدویی از حال و هوای پرسپولیسی‌ها در اردوی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136760" target="_blank">📅 23:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136759">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🕹
هیجان واقعی کازینو؛ جایی که شانس و مهارت به هم می‌رسند
!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🎰
چرا کازینوی وینکوبت؟
• تنوع بالای بازی‌های کازینویی
• میزهای زنده با دیلرهای حرفه‌ای
• گرافیک و کیفیت فوق‌العاده
• بونوس‌ها و پیشنهادهای ویژه
• محیطی امن، سریع و کاربرپسند
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136759" target="_blank">📅 22:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136758">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🟠
🟠
🟠
مهدی عبدی در لیست مازاد مازیار زارع قرار گرفت.
✅
✅
چه بلایی سر خودت آوردی پسر..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136758" target="_blank">📅 22:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136757">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
فووووووووووری و رسمی؛ رای نهایی دادگاه پژمان جمشیدی صادر شد و نتیجه آزمایش تجاوز منفی اعلام شد و پرونده بازیکن سابق پرسپولیس و فوق ستاره فعلی سینما مختومه اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136757" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136756">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
ویسی:
❌
اومدیم که امتیاز بگیریم و میگیریم
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136756" target="_blank">📅 22:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136755">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
رامین رضاییان نام استقلال رو از بیو پیجش پاک کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136755" target="_blank">📅 22:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136752">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJNRyw8FyHV_vYlk3kVuyAeXPK5oIJmuCfFMWBcbm-CsMZh1rfAQ96GdbvAFURSIIrLGUhdHkRgp0GyErAOdGbpd23MBOw3zFppgKtcGiMHd5xIBrft8twln3xiA7rBqLVjMc58ES8TSgmISxlusgZRkERy7GalYmhnOzho8m0q7Lmf7I2KGObjLpXRda26_G4SWcatinnC0p3XpXvQf2BjKiZZR700opXTcbFapDqt2AxlOj-y4ybhkmx7MhxpJAuKphTRF0niJf9_8ouZEZTXktEY35a72MFOTOvxHzjkyR0__ug5T7NV6hZHNywi9SchfipWKuA-OLYhSoPqZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووووووووری و رسمی؛ رای نهایی دادگاه پژمان جمشیدی صادر شد و نتیجه آزمایش تجاوز منفی اعلام شد و پرونده بازیکن سابق پرسپولیس و فوق ستاره فعلی سینما مختومه اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136752" target="_blank">📅 20:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136751">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726dada166.mp4?token=cx6ionVbUF1qjfmDbJzoQCk_qgPTeUQZX5u6jlIaL8SWqJ7Ht3BwP4AgJ-Qi9VlCkVU2E5f7rMq69TiZNgcoOurxuGu6pjqZrzfc7O50c5tcWpAYqQ43o8JXgTj-oYueQF0Gb-B7jeHJZaWjUii1pD43CuDmAkfEQuGQ4lZKgoza5X9J3HsyVC2FSoX--UDzv52rNG2aknYqv6R0jbMJVrgGkpQxoOAwsqeuQqJSr93GJ0SfJALdoNWcU2EdEts8MzgrDaOCTdgMv7fC7jzPyVt6ZmL4dF-rPRCMLGoAkLtHec-j5K4BPJJdT94NL90JLPs7x-JlizE3lM0qWdzoOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726dada166.mp4?token=cx6ionVbUF1qjfmDbJzoQCk_qgPTeUQZX5u6jlIaL8SWqJ7Ht3BwP4AgJ-Qi9VlCkVU2E5f7rMq69TiZNgcoOurxuGu6pjqZrzfc7O50c5tcWpAYqQ43o8JXgTj-oYueQF0Gb-B7jeHJZaWjUii1pD43CuDmAkfEQuGQ4lZKgoza5X9J3HsyVC2FSoX--UDzv52rNG2aknYqv6R0jbMJVrgGkpQxoOAwsqeuQqJSr93GJ0SfJALdoNWcU2EdEts8MzgrDaOCTdgMv7fC7jzPyVt6ZmL4dF-rPRCMLGoAkLtHec-j5K4BPJJdT94NL90JLPs7x-JlizE3lM0qWdzoOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136751" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136750">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚡️
⚡️
🚨
🚨
🚨
🚨
فووووووووووووری
✅
محمدمهدی محبی نهایتا امشب یا فردا قرارداد شو امضا می‌کنه
🔽
تمام توافقات با کلبا نهایی شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136750" target="_blank">📅 20:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136749">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⚠️
⚠️
نیمه نخست دیدار تدارکاتی پرسپولیس و پیرامیدز مصر با نتیجه صفر - صفر به پایان رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136749" target="_blank">📅 20:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136748">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏅
ترکیب پرسپولیس برابر پیرامیدز مصر
💢
پیام نیازمند، حسین ابرقویی، سین کنعانی‌، علی رضا همایی فرد، مجید عیدی، پویا پورعلی، مارکو باکیچ، مهدی تیکدری، محمد عمری، علی علیپور، ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136748" target="_blank">📅 19:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136747">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">💠
💠
💠
آخرین خرید ها از زبان قدوسی:
😀
با محبی به توافق کامل رسیدن
🔹
اخباری تا چند ساعت آینده امضا می کنه
😀
ایری و طاهری هم باشگاه داره محکم کاری می‌کنه تمام شدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136747" target="_blank">📅 19:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136746">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
اعضای کادرفنی تیم پرسپولیس :
🔴
سرمربی : مهدی تارتار
🔴
دستیار مربی: وحید فاضلی
🔴
دستیار مربی: علیرضا محمد
🔴
دستیار مربی  : رضا جباری
🔴
دستیار مربی  : کریم باقری
🔴
مربی دروازه بان : حسین اینانلو
🔴
مربی بدنساز: یاگو
🔴
آنالیزور: میعاد قاسم زاده و محمد کهن  …</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136746" target="_blank">📅 18:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136745">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">💠
💠
💠
آخرین خرید ها از زبان قدوسی:
😀
با محبی به توافق کامل رسیدن
🔹
اخباری تا چند ساعت آینده امضا می کنه
😀
ایری و طاهری هم باشگاه داره محکم کاری می‌کنه تمام شدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136745" target="_blank">📅 18:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136744">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">https://www.facebook.com/100050246329900/videos/1060805676383532
لینک پخش زنده بازی پرسپولیس _ پیرامیدز مصر داخل فیسبوک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136744" target="_blank">📅 18:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136743">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏅
ترکیب پرسپولیس برابر پیرامیدز مصر
💢
پیام نیازمند، حسین ابرقویی، سین کنعانی‌، علی رضا همایی فرد، مجید عیدی، پویا پورعلی، مارکو باکیچ، مهدی تیکدری، محمد عمری، علی علیپور، ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136743" target="_blank">📅 18:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136741">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
خبرنگار پرسپولیس:
🔴
امروز محمدمهدی زارع و پویا پورعلی در تمرینات عالی ظاهر شدن .تیکدری هم مثل همیشه خوب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136741" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136740">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚠️
☹️
کانال ۱۴ اسرائیل مدعی شد: ایران دستور توقف کل حملات به کشور های عربی را صادر کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136740" target="_blank">📅 17:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136739">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
تایم و رقبای سه دیدار دوستانه پرسپولیس در اردوی ترکیه مشخص شد.
❌
سرخپوشان در تایم های 8،4 و11 مرداد ماه با  تیم‌های «پیرامید»، «آنالیا اسپورت» و یک تیم دیگر به رقابت می‌پردازد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136739" target="_blank">📅 17:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136738">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">💛
حسن روشن علیه قلعه‌نویی و فدراسیون
💢
حسن روشن:
«۱۴۰ میلیارد برای قلعه‌نویی ناچیزه؟! خدا رحم کرد تیم حذف شد! لابد اگر صعود می‌کردند به قلعه‌نویی و بازیکنان هرکدام یک استان می‌دادند!»
• روشن همچنین پیشنهاد فدراسیون برای تمدید قرارداد قلعه‌نویی به شرط قول قهرمانی در جام ملت‌ها را «خنده‌دار» دانست و گفت چنین پیشنهادی اصلاً منطقی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/136738" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136735">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚡️
⚡️
🚨
🚨
🚨
🚨
فووووووووووووری
✅
محمدمهدی محبی نهایتا امشب یا فردا قرارداد شو امضا می‌کنه
🔽
تمام توافقات با کلبا نهایی شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136735" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136734">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
🔹
🔹
فوری/کانال ۱۴ اسرائیل:
🔹
ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/136734" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136733">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
شنیده می‌شود در صورتی که امیر قلعه‌نویی قول قهرمانی ملی پوشان در جام ملت‌ها را بدهد، در تیم ملی ماندنی خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136733" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136732">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
❗️
محمد مهدی محبی با عقد قراردادی سه ساله رسما و شرعا به پرسپولیس پیوست / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136732" target="_blank">📅 17:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136731">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
خبرنگار ورزش سه حاضر در ترکیه: محمدرضا اخباری هم اکنون در تمرینات پرسپولیس حضور داره و تیم رسانه ای پرسپولیس در چند روز گذشته هیچ عکس یا فیلمی از تمرینات گلر های پرسپولیس نمیزارن / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136731" target="_blank">📅 17:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136729">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
#تسنیم؛ پرسپولیس سفت و سخت افتاده دنبال علی نعمتی و میخواد با یه جلسه حضوری کارو تموم کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136729" target="_blank">📅 15:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136728">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136728" target="_blank">📅 15:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136727">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
مشکل رضایت نامه حل شده و قرارداد هم بین طرفین نوشته شده و مشکلی وجود نداره و ظرف چند روز آینده امضا میشه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136727" target="_blank">📅 15:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136726">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
✅
اخباری تو تمریناته و به همین دلیل چند روزه از تمرین پرسپولیس عکس منتشر نمیشه
🫪
/ورزش‌سه
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136726" target="_blank">📅 15:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136725">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
محمدرضا اخباری در حال حاضر دبی حضور داره و امروز با دریافت برگه مجوز خروج راهی ترکیه میشه. طبق شنیده ها قراره اخباری امروز به صورت رسمی معرفی بشه ///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136725" target="_blank">📅 15:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136724">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
مشکل رضایت نامه حل شده و قرارداد هم بین طرفین نوشته شده و مشکلی وجود نداره و ظرف چند روز آینده امضا میشه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/136724" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136723">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
آنا : محمدمهدی محبی به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136723" target="_blank">📅 13:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136722">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
🔴
قدوسی: اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136722" target="_blank">📅 13:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136721">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚡️
فوووووووری
💥
💣
اتفاق خاصی رخ ندهد محمد مهدی محبی خرید بعدی ما خواهد بود//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/136721" target="_blank">📅 13:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136720">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
شنیده می‌شود در صورتی که امیر قلعه‌نویی قول قهرمانی ملی پوشان در جام ملت‌ها را بدهد، در تیم ملی ماندنی خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136720" target="_blank">📅 13:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136719">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
🚨
فووووووووری از خبرگزاری ایرنا
🚨
پرسپولیس نمیتونه کسری طاهری به خدمت بگیره و تا نیم فصل باید در نساجی بمونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/136719" target="_blank">📅 12:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136718">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
✅
پنج بازیکن جدید پرسپولیس از نگاه ورزش سه:
⏺
محمدرضا اخباری
⏺
دانیال ایری
🔴
ابوالفضل رزاق پور
⏺
فرهان جعفری
⏺
کسری طاهری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/136718" target="_blank">📅 12:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136717">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
پرسپولیس در انتظار امضای قرارداد ارسال شده برای اخباری
🔴
با توجه به اینکه محمدرضا اخباری در کمتر از 10 درصد مسابقات فصل گذشته برای سپاهان به میدان رفته، سهمیه لیگ برتری محسوب نمی‌شود. / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/136717" target="_blank">📅 11:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136716">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
طاهرخانی: احتمال داره فردا از محبی رونمایی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136716" target="_blank">📅 11:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136715">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
✅
پنج بازیکن جدید پرسپولیس از نگاه ورزش سه:
⏺
محمدرضا اخباری
⏺
دانیال ایری
🔴
ابوالفضل رزاق پور
⏺
فرهان جعفری
⏺
کسری طاهری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136715" target="_blank">📅 11:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136714">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💥
💥
با جذب محبی و لطیفی‌فر سهمیه‌ی لیگ برتری پرسپولیس تموم میشه ولی قراره یه سهمیه بزرگسال و دو سهمیه زیر ۲۳ سال اضافه کنن تا ایری و طاهری و رزاق‌پور رو هم بتونیم جذب کنیم/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136714" target="_blank">📅 11:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136713">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136713" target="_blank">📅 10:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136712">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه پرسپولیس قصد داره‌ تا ۲۴ ساعت آینده از چهار خرید جدید خودش رونمایی کنه ///فرهیختگان
🤝
محمدرضا اخباری
🤝
دانیال ایری
🤝
کسری طاهری
🤝
پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/136712" target="_blank">📅 08:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136711">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
دیشب و بامداد امروز هم حملاتی به کشور عزیزمون نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136711" target="_blank">📅 08:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136710">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم در واکنش به صحبتهای قلعه نوعی که گفته از خودگذشتگی کردم اومدم تیم ملی تیتر زده که آقای قلعه نوعی میتونه دیگه ایثار نکنه و از تیم ملی بره و برگرده لیگ برتر همونجایی که تو ۱۰ سال گذشته هیچ افتخاری کسب نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136710" target="_blank">📅 08:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136709">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
بعد از 13 شب .دیشب و بامداد امروز هیچ حمله ای به ایران و نقاط ایران از جمله جنوب نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/136709" target="_blank">📅 08:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136708">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa3erCnLd-rE4dKbFEx0ft_XuuN9HdavO-HxA-wAu_vVASvDeZcJPHJQO1jkBQltU2A59oo3LXJEHoD4voTF3x4zZhj5cyfubYzRLDeLfBI8myyA-dkFVfh05x_wnfWupOLEHEjsDQAhNhmY3okLubf46uYdPxgNKGWKVSG0a9-aHkz7U_eZqwoky9r2HCb7FZfFf_4BFnL5XHIUE11IHZe7JPu6J7QbAMg-ziHs77bra_w2IcM-UFgbXlHjLaehKWJHJAXKz9-Vs2IvvgNysJV79ldPS_Mmu56yBdYoXL5BJzK2ptmJG9rHFrIyashXU941_RuzQSh-73i75HWWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136708" target="_blank">📅 08:43 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
