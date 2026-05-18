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
<img src="https://cdn1.telesco.pe/file/M4I3l4xnUS9IEBeDLpKFwylp3F2u5GAu4tBpzM7jwAMVfOGEkaq_yYR7iqeJuJ12LbuaUIIJrmbYt-eydXPPf4MdaznEPMKc0dTzCJomE2tSQVe_-OyesFIfsuiKFEIGVwsl1h5hJPTi-IFznAgmVgIj0yup9X3egbl9E2aHQzKO3xHAntEnLp9Lc4ZH10UuTfMElToeHTrJFre-0lcOIV6KQAX0oYyT1l18YjikRiXeFZSlACbFyIfQEl46g0JJkrdMqVLu9tVuM0vyHt_u3x1fnL7NXsNI4y9SYSrJo1BQCkZP6WldoAUYOeSkhesnKVjddM0q4a1g--CDjRJmgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 122K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 21:57:14</div>
<hr>

<div class="tg-post" id="msg-3152">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">certificate_generator.bat</div>
  <div class="tg-doc-extra">56 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلهای سرتیفیکیت جنریتور(ویژه ویندوز)
و
کانفیگ MITM (ویژه اندروید و ویندوز)
لینک گیتهاب پروژه:
https://github.com/patterniha/MITM-DomainFronting
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/MatinSenPaii/3152" target="_blank">📅 21:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3151">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود
این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.
⚡️
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
لینک سایت Regery برای سرتیفیکیت جداگانه روی اندروید:
https://regery.com/en/security/ssl-tools/self-signed-certificate-generator
لینک فایل‌های مورد نیاز:
https://t.me/MatinSenPaii/3152
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد MITM، تحریم سرویس‌های گوگل رو دور بزنید.
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
💰
دونیت</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/MatinSenPaii/3151" target="_blank">📅 21:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3150">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی از دوستان توییتر گفته تامکت به قید وثیقه سنگین آزاد شده. امیدوارم که درست باشه این خبر
🔥</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/MatinSenPaii/3150" target="_blank">📅 21:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3149">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عالی بود
تمام 133.9 کیلوبایتی که برای این ویس دادم ارزششو داشت
🤣
🤣</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/MatinSenPaii/3149" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3148">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirmohammad</strong></div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/MatinSenPaii/3148" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3147">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">rdnbenet-windows.zip</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/3147" target="_blank">📅 19:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3146">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nVxR9PAk-fKZ1uOJf6eByx-4ROlXNrlhWQRqIpGIG_1FkO2xWVGNrTrHmOusZlZuW7uJZsPFVxygywGP-_tF5KnzF7x3wkIBJcJY0fm88QPJPO973qcj5QPbfE_HisJQaQ4nDQa7dUDa-5edFlcdrnUHu4AWu9ia6dat_X1HhckgWYBPI7v-alpjGUNewCieJsmiPf8UJWDplatBBSpakhJOuyBmF1AYdtT8UToTdabSVojyf__7VOK_cBo4iukJ_gkFV_I4q7BaqjKNeJvaxdMsMZAC8zCFP1vMhDuf_dEoK4M2P5HmvuysenBw2A4H1BGi4_Jra7lseNrCjdqLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه متد یوتوبه زیاد ساده نیست، اما خب قابل تحمله و زیاد هم پیچیده نیست. اون شکلی نیست که بتونید راحت برید توی یوتوب بچرخید، اما خب محدودیت حجمی و... هم نداره.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/3146" target="_blank">📅 19:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3145">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رفقا متد بله رو چندتا از دوستای متخصص توصیه کردن که اصلا نه انجام بدیم نه من آموزشش رو بدم. بر پایه‌ی سروش هم یکی الان دیدم نوشته بود و واسم فرستاده بودین. چون حتی سر متدای ارسال فایل هم اکانت یه سری از بچه‌ها بسته شده بود توی روبیکا و بله</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/3145" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3144">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خب با این اوصاف من آموزشه رو می‌ذارم. چیز پیچیده‌ای هم نیست اصلا
دوتا ویدئوی مجزا میشه اما چون خلاف قوانین یوتوبه فقط اینجا می‌ذارم</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/3144" target="_blank">📅 17:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3143">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-poll">
<h4>📊 اینایی که میزنن دیدن نتایج ایران نیستن یا حال ندارن چک کنن؟</h4>
<ul>
<li>✓ ایران نیستم</li>
<li>✓ ایرانم. حال ندارم چک کنم</li>
<li>✓ دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/3143" target="_blank">📅 17:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3141">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-poll">
<h4>📊 بفرمایید که،</h4>
<ul>
<li>✓ meet و drive بسته‌ان یا یکیش بسته‌ست❌</li>
<li>✓ هر دو واسم بالا میان راحت✅</li>
<li>✓ دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/3141" target="_blank">📅 17:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3138">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گوگل میت چی؟ :)</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/3138" target="_blank">📅 17:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3137">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qp5v5095_1IDgVH4nHGHc3Pe129wR31d9xG1oWeC7TSDHth-Ipea8tqhQL4qm6GE2qtusjq-WKtYTCF7IxLLEcP0XE3PQqm3f2hKCAjUbeOpx0CPwfYb1HJ9lnMzYV0xzcUEg1cLYuu9pSg0svEBcXwA6lqBhTsJiEkErmO-uemdA0smD9JLa93bJ88oDY8wDZlOnEbgVw1t8B3UQdhnOGn1IBX3zL6z2Fu_WdTb2Urn8YsrdpEE_zqqEYynTh3nD1nxQfG6bMMfWcKQ4uwQ67UMzwteL4_QATI1EXdqx7lCHfIpA_gE-ryGqkh7u6NKaiw2t6zsonafLBX_DocDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان، drive.google.com روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/3137" target="_blank">📅 17:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3136">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستان، drive.google.com روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/3136" target="_blank">📅 17:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3135">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستان،
drive.google.com
روی نت شما فیلتره دیگه؟</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/3135" target="_blank">📅 16:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3134">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بذارید بگم که چرا از زبان پایتون خسته شدم برای توسعه‌ی Back-End:
اول از همه، magic methodهای افتضاحش. یعنی هی باید __init__،__ str__،__ repr__، __add__، __getitem__ و هزارتای دیگه رو یادت باشه. که این باعث میشه هی دست به دامن ai بشی. و همینطور باعث اینکه خیلی وقتا نفهمی  چی داره پشت صحنه اتفاق می‌افته. یه operator ساده می‌نویسی، و یه magic method جادویی صدا زده می‌شه که اصلاً معلوم نیست کجاست. وقتی می‌خوای دیباگ کنی، باید بری دنبال این متدهای مخفی قبیله‌ی برگ(!) بگردی. و کلاً خیلی implicit و غیرشفافه.
دوم اینکه اینترپرتری یا مفسریه. یعنی خط به خط اجرا می‌شه. تا نرسه به خط ۲۰۰، نمی‌فهمی اون خط مشکل داره. باید کل برنامه رو ران کنی تا به اون خط برسه و بعد بفهمی "آها، اینجا یه typo داشتم" یا "این متغیر تعریف نشده بوده". یعنی عملا یه کد بیس بالای 5 هزار خط پیرت میکنه. از اون طرف توی زبان‌های کامپایلری مثل Go یا Rust، قبل از اجرا خود compiler همه‌چیز رو چک می‌کنه و بهت می‌گه کجاش اشتباهه. همه‌ی ارورا، یک جا. ولی توی پایتون باید خودت خط به خط بری و ارورا پیدا کنی.
سوم اینکه type safety نداره. یعنی یه متغیر الان string هست، یک ساعت دیگه int می‌شه، بعدش list می‌شه. تو runtime متوجه می‌شی که "اوه، اینجا یه list بود و برنامه کرش کرد". Type hintها هم که فقط تزئینین، اجباری نیستن و موقع runtime چک نمی‌شن.
چهارم اینکه performance خیلی ضعیفه. برای یه API ساده که ترافیک بالا داشته باشه، باید چندتا سرور بزنی بره بالا. حالا همون کار رو با Go بنویسی، با یه سرور راه می‌افته.
پنجم، dependency management و packaging اش یه فاجعست. pip، virtualenv، conda، poetry، pipenv... هرکس یه سازی میزنه برا خودش و شما باید به اون ساز برقصی. requirements.txt هم که دچار conflict میشه خیلی وقتا. Python 2 هم هنوز توی یه سری از پروژه‌ها هست که تبدیل کردنش بدبختیه.
خلاصه اینکه پایتون برای scriptهای کوچیک و زمینه‌ی هوش مصنوعی و ماشین لرنینگ خوبه، ولی برای production backend واقعاً اعصاب خورد ‌کنه. و من رفتم سراغ یه زبان compile شده که از همون اول بگه کجا اشتباه کردم، نه اینکه وسط شب production کرش کنه. مثل گولنگ یا حداقل حداقل تایپ‌اسکریپت.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/3134" target="_blank">📅 16:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3133">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">WhiteDNS-1.5.0-x86.apk</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/3133" target="_blank">📅 14:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3128">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3128" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر از مطمین نیستید، ورژن یونیورسال رو دانلود بکنید.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/3128" target="_blank">📅 14:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3127">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q44Ld-Z6r4KT9D_L0mZHRS2sWxxYDL6EQ076C7Qj7UaepCwyCkaBpKvAD6RiD6Wf9quoWGqYja6VpD_Cu3d0J_o-LHvfxGzCM-QjlZy16zTzjhhkBxBJ9RiM21tJ-Y5PwSiYkBF8p2h9udKMNtz0KFi6f4lkyEGVrIxAfdApbFm2u0RbBjc6yiE2Yh0SxjjTOpx73Y27_3-JdUvhHHX4mtKaREV3tl8qys9ZJ0BUizvweBZJ5SRrpQF6q1h3XAVrGU6WQrLwmS_gojfVbvr3M6Und6J9HIR9FlHRMzGo-SZvZnmMm2NOpdy_ZBj8HWBZEVwMFL7q-15XcqEmhYyGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچین موردهایی رو زیاد واسم میفرستید دوستان. مسئله‌ای نیست؛ من که چیزی رو اختراع نکردم که زده باشن به اسم خودشون
😁
صرفا زحمت جمع‌آوریش رو کشیدم. منبع هم نذاشته، نذاشته. مهم نیست که.  هدف، وصل شدن مردمه</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/3127" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3126">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">با گوشی هم میتونید باز کنید دیگه اون Index رو
یکی توییتر پرسیده بودش</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3126" target="_blank">📅 12:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3125">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه چیز جالب توجهی پیدا کردم که راجبش ویدئو بسازم. به درد خیلیا میخوره
ترکیب یه متد حال حاضر هست، با یه سایتی که اصلا هیچکس نمیشناسه. انقدر گشتم که پیدا کردم
برای VPN نیستش. برای دسترسی رایگان به محتوای یوتوبه
سر کار هستم الان، تموم که شدم واستون ویدئوش رو میگیرم</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/3125" target="_blank">📅 11:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3123">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OG_4DgMbgBfBE6sWyUuJ48_ndZdKG1-_ETS91fczE-3U5pMecu2N4gr4-PsnwRPtl_xJtsg9LlmahqeF1NCn59-qL54aC4gMX9Dngu4DBMafGiAr3ruJaQeWcgyUgqp9LBtnfr2_AAlMkhpLHniXYNLR3gZRWCgcdWxL7WTb5haYR6uz9hFPQGI0Vdwy7Kaz8k9DknpTCqcyC8LwCa4hciTSluYZLeHOZAlNvD571O0r0aXsDDSysY_RVywe_umLXBQBqV_YR8AFrknqqDloS_1lkAfjraVsIzE_ZRVd94GRf-Adk8p2fzZJ8qpsoMQsmPbZSWX4fhpMSv1xYoq4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LD_dtSodoSESRPctlBIDXWKYg87FPj0u78C3HNN_UgHWz8nB6VKBJb3uftsCjEXb3CMSYLXqU_2_DNrftTwuSIb_KmPKSRaoYjyXcU0yHb5fISXB9LrSE75ujh1ninegwp-scR6-5-gKOlKAobRBKcu-yJzOXAnLnbiu4jG8s2h2WmPI-oBFxvFHu2VgxxSbsnUk770sUSnVa5j5Z8Z2gjDwbRrJ2DB5OuY8OtNJl7FZ0LF9hMegxtZ1Pj3_vHyZ6WHTgf0ONlIBfAEXFMHvSQd22oEQCM--F46vPZ4g3rzcs3nVeyj99Xu_CjrmZmEFRJv5oVEe4AaVPNsetpngzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فایل رو روی سیستم Extract کنید و بعدش راست کلیک کنید روی index.html و Open with chrome رو بزنید</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/3123" target="_blank">📅 10:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3122">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">cdn-ip-finder-main.zip</div>
  <div class="tg-doc-extra">723 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3122" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/3122" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3121">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fle2obtsP6JjOfJ-QZx4Htni99J49wOj1isKwVPPRDH26R6nckE3tHuGLpJezcrrojfjUSljTJopFLrf-OZa65g-MfTrdTZscKcrLvHHEmaKOAo5rX3Ae1czNBIWCQcscq_WRzgk2YZLTKlBm6liQMNoHGXYF-DPB7rFzT6umls9Pk6hqEIFuL9rdmjQDA0s405Ffz6Bg_3F02v5WIjuQc8FN3yiP9p2HdMR8H1_0A5McrttfRkpRb_NhspUiQe_bs_tj0EhLSvOQBzgz42ThD9T8-h9GmKH9rNg8e53k_-_s6bf3lKLHFt2HPewf5hIIK8zsWPBkHLZhNMgAKHjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفر اسکنری که دیروز توی کانال قرار داده شده بود رو برداشته، و توسعه‌اش داده و تبدیلش کرده به یه اسکنر پر و پیمون تر. این هم پروژه‌اش هست:
https://github.com/hossein8360/cdn-ip-finder</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3121" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3120">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ایرانسل:
95.100.69.108
104.83.5.203
92.122.166.146
104.66.70.133
104.121.0.17
104.83.5.65
92.122.166.168
104.83.5.82
92.123.104.67
104.110.191.57
92.123.104.7
104.109.250.232
96.16.122.74
23.40.63.69
23.73.2.161
138.201.54.122
144.76.1.88
94.130.33.41
95.216.69.37
185.137.25.214
94.130.70.160
94.130.50.12
37.255.133.30
104.81.104.13
92.122.73.138
96.16.122.55
104.81.108.51
23.72.248.214
104.126.37.185
104.83.5.201
92.122.166.141
104.83.5.216
172.237.127.6
104.81.108.10
23.73.2.148
81.91.145.2
65.109.34.234
81.12.72.218
185.143.232.122
96.16.122.66
88.221.168.138
92.122.166.175
96.16.122.82
96.17.207.149
96.17.207.151
23.220.113.51
5.160.13.85
142.54.178.211
63.141.252.203
96.17.207.135
2.23.168.144
2.23.168.254
2.23.168.250
2.23.168.96
2.21.239.29
184.86.103.210
23.36.162.202
95.101.29.30
2.23.170.80
185.200.232.16
2.16.245.188
95.101.23.82
185.200.232.34
184.28.230.87
2.16.19.136
2.23.168.174
50.7.5.83
2.23.168.47</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3120" target="_blank">📅 10:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3119">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/plQUwuPTBCLAuUhiySyMqxXjpGkEUPyL0DChPO_Vk6SlvQnproV3O5sQ_Oe8YW9kRI68k-t1Zb3daOPOol8J0fsa6xGN1V_k4BYa27r6O10cZHYUDc87mW3drdR5PCSwxWI-qEbJ5aHdIr7dsSMg5SCcWarvXpjSSyb7sgmScGn9NXE_vj1NPOHHSe2EpbPQPNeG4y2TmYtAqgvUpFhy5CgnG0LYFK4Ttqg72KsYr5j-fw8GAgMzWtyXDfALa_5vpjQJ3MiTPAawK7pjawUvczusH9uEp4BOmBcxCilCEbEHq41OFf0lukUKUvWoy1kQfe-P__hjxi07e6JjNdWgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همینطور تغییر APN به
google.com
رو هم امتحان کنید. گویا روی ایرانسل بیشتر جوابگو بوده. من خودم روی همراه اول فقط با همون لیست آیپی‌هایی که دیروز گذاشتم وصلم به شیر و خورشید</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3119" target="_blank">📅 10:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3118">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یکی از دوستان این نکته رو گفته بودش در مورد وارد کردن آیپی‌ها:
من چندین دفعه هم با سامسونگ هم شیائومی تو برنامه مهسا‌ان‌جی امتحان کردم
و یه چیزی فهمیدم که خیلی عجیب بود اما درست بود.
هنگامی که آی‌پی ها رو پس از اسکن، کپی می‌کنید که داخل برنامه وارد کنید حتما باید آی‌پی ها هرکدوم یک خط رو جداگونه داشته باشن
اینجوری مثلا
20.68.81.211
20.63.74.811
و اگه جداگونه نباشن و مثلا اینجوری کنار هم وارد بشن
23.96.52.41
86.52.17.76
و...
برای من متصل نمیشن و این رو امشب فهمیدم و با برنامه MahsaNG از سر کنجکاوی امتحانش کردم و در کمال ناباوری جواب داد و متصل شد الانم دارم آپدیتای گوشیمو انجام میدم.
و برای این که بدون زحمت خاصی جدا جدا هرکدوم یک خط رو در بر بگیرن، پس از اسکن کپی کردم، تو تلگرام ارسال کردم و از تلگرام کپی کردم و تو برنامه وارد کردم و درست شد.</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3118" target="_blank">📅 09:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3117">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3117" target="_blank">📅 00:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3116">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TCIMkhKEWu2kTrgoL0KzV5n4-q05qxfBj4jQLvvDqqWHgwHmkh5cnvtyhTefhi3tdUtqWe5dha0rgtEn0n9MnSklBOE11HLxSW_j-tX9fJyjNlF933_417O-mmk4Z4BqVsWASjxSapzN-Kr8JnEKr8Y8GDG_LT9hRkxSOcwQBkKH9NdY-EB_UHlfqI2eVphQY6q0SKg_LvWWTPu37qYMtlnK5qhzStKd-nWcYyMFtIQBO0CqHK7GasDmxb-FccdWC27m9EmrBYnOMKXLQBE04qIEtQYReDNKH501WAMIv7ZBM_14SRJIvQqHMm61Ph5T5lIDuqWzgv6Z6CICd91rFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جدی جدی روز جهانی ارتباطات رو تبریک گفته
😐
تمام آدم‌هایی که شبا گرسنه خوابیدن و پول اجاره خونشونو نتونستن بدن و به فکر خودکشی بودن به خاطر اینکه کسب و کارشون نابود شد سر قطعی اینترنت از جلوی چشمام رد شدن</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/3116" target="_blank">📅 23:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3115">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حس میکنم ضبط کردن ویدئوش ارزشی نداره زیاد.. خودتون اذیت میشین
اگه تا فردا دووم آورد می‌ذارم واستون</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3115" target="_blank">📅 23:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3114">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حدسم اینه تا صبح بیشتر نکشه که ببندنش متأسفانه. بله آخه دست خودشونه طبیعتا.
فیچر تماس تصویریش رو به راحتی میندازن سطل آشغال. یه ماه تمام کل دی ماه تمام اپلیکیشنای چت بسته بود اگر یادتون باشه</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/3114" target="_blank">📅 23:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3113">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این ریپو رو هم چک کنید. متفاوته:
https://github.com/theermia/BaleTunnel</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3113" target="_blank">📅 23:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3112">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/3112" target="_blank">📅 23:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3111">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد می‌رسه.
https://github.com/kookoo1sabzy/BaleVPN/tree/main
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3111" target="_blank">📅 23:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3110">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">thefeed-android-v0.18.10-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3110" target="_blank">📅 23:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3109">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.18.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3109" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه‌ی جدید نرم‌افزار TheFeed برای خواندن اخبار کانال‌های تلگرام در شرایط قطعی اینترنت(کل جنگ با ریزالورا وصل بود)
کانفیگ‌های این اپ:
@thefeedconfig
لینک پروژه بر روی گیتلب:
https://gitlab.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3109" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3108">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m9e2Ktsgkfz9IYNMrZ1rTvZ1-aayEdDYU2-FqrKLgco0iQ3mAzSo9T2JGiKr0hqPFHifLFo2wAi47Tl8Agnyt8MkRL7BYKAtC9Gr9hU4cBoiPIDqRV2NjlIycRU7qyq1TljsXiw6-c3eX1VVoF8LcZe6GCM_gm0TnCa0tK59RBLZXSBHveY3O9lUyRx0ftpQ0-T0DJIpgCDmpx4_Jn6YRAE8AzhUXtZS6Kl5zrknRvwvNQPBdJTE0IDvSqXtF7wYsDJu21Na66U_9y7tnNeiqCAT3j9nZvgSwJhkh1uEydXgJEkNBu-KAOVOsmGKWaEZ2VhJ901lFlWoP2vYsq8eNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیزاین با ai
:)))
دیزاینرای حرفه‌ای هرچند قرار نیست بیکار بشن. مخصوصا UI-UXکارها
آیدی طراح(پرامپت‌نویس؟!)</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3108" target="_blank">📅 21:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3107">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fRftwCQVT1ZXTnNvT-iejdN3MNsmKFq9ffv_pHBtFwqtA6IbIXVoFzXY26V_a1hsGysl4tQqjaYgPqM0OaXULplUa5C_9raUAhISFH2T_Y_MlZks57vZReRC6eURHGB7_eWG71bj1LqbfTPGh6v7xXbNvkQ5r9SlP4TzXHw58VBa1i_CERj8vLiPaN2aYgK8LevHZkj8iLm5-nDXvcA2v3sxlYmcCcNByiOQwjfrz04s8nmqZ-wwmTf2TZn6eCa6-RD6x9oF3hKVnOiQ_3-M-skJIhuSp9mqhePZufVo2KuRagUhzX1l61X5Jyt6G9OWqpi5MB1rOBVVPJfdNFA8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان این اسکرین شات فیک هستش و ساخته‌ی دست یه سری از VPN فروش‌هاست. یه دور بخونید از روش میفهمید یارو خیلی هم عجله داشته
🤣
لذا خواهشمندیم زیرا</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/3107" target="_blank">📅 18:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3106">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">CDN-IP-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3106" target="_blank">📅 16:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3105">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mTZRu_o8StXBc4Bz2VtDRBOk5lzqMA65N_M3ON7DUtw03AbKcGUXG6fqXa-o80KdDpvT4vsRGrZhHt3PDW7abDA1E7dgJwAY8AAAakgZW6kQEGLljNj_8Vk8DfPsN-YKU7SsFQewfe3_hJXBWj_i3DIUv5gdZQFK9cmIzdS79VoWbo1HHeLgcqaTILxs8ktbsEa5ScVIh1z9J2X2-9SE2mbhqoXrJWV3UZIdpdScgEOAgZDqSZnuk2ERa41zaNVR0ewYsf4pIoCOa5jUBPdYzCXjposBwauyYzsXnanwaCDeYzsmwI0yAbUpTd4DxdNsq_Xtc0GQzT3whLU-pnTgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچین موردهایی رو زیاد واسم میفرستید دوستان.
مسئله‌ای نیست؛ من که چیزی رو اختراع نکردم که زده باشن به اسم خودشون
😁
صرفا زحمت جمع‌آوریش رو کشیدم. منبع هم نذاشته، نذاشته. مهم نیست که.
هدف، وصل شدن مردمه</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3105" target="_blank">📅 15:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3104">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CDN-IP-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">4.7 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3104" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">هرچی آیپی CDN و ... از اول اومدن این متد توی توییتر و کانال‌های تلگرامی گذاشته شده بود رو جمع کردم، دادم AI تکراری‌هاش رو پاک کرد و واستون گذاشتم توی این فایل تکست. یه تست با اسکنر بکنید و بذارید متصل بشه.
صبور باشید
!</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3104" target="_blank">📅 14:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3103">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگر با شیر و خورشید وصل می‌شید، گزینه‌ی Share proxy on network رو فعال کنید. سپس به یه WiFi وصل بشید و کانکت کنید VPN رو. بعدش با هر دستگاه دیگه‌ای اگر این کانفیگ رو بزنید(با توجه به عدد و پورت خودتون تغییر بدید): socks://Og==@192.168.1.147:46597#ShirOKhorshid…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3103" target="_blank">📅 13:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3100">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MahsaNG_16_arm64-v8a.apk</div>
  <div class="tg-doc-extra">59.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3100" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش اتصال با آیپی‌های CDN از طریق نسخه‌ی جدید MahsaNG:
1- وارد نسخه‌ی 16 میشید(نیازی به هیچ کانفیگی نیست)
2- اون بالا روی حرف F میزنید
3- گزینه‌ی Psiphon Only رو روشن می‌کنید
4- روی Psiphon Setting کلیک می‌کنید
5- بخش Protocol رو می‌ذارید روی cdn_fronting
6- بخش Aggressive رو قرار میدید روی ON
7- توی بخش CDN Fronting Settings، آیپی‌هایی که من بالا واستون می‌ذارم برای هر اپراتور رو قرار میدید
8- روی Save Psiphon Setting میزنید
9- برمیگردید به منو اصلی برنامه، روی دکمه‌ی گرد پایین سمت راست(اتصال) میزنید
10- یه نوتیفیکیشن Psiphon tunnel connecting میاد بالا. اون وقتی تبدیل بشه به connected یعنی وصل شده
توضیحات:
1- نسخه arm64 برای اکثر گوشی‌های 2020 به جلوتر مناسبه
2- نسخه arembi برای گوشی‌های قبل 2020 عموما
3- نسخه‌ی universal روی هر گوشی‌ای نصب میشه فقط حجمش بالاتره چون تلفیق تمام نسخه‌هاست اما حجم نهایی نصب شده روی گوشی شما همون دوتا بالاییه
لینک‌های داخلی:
1- نسخه arm64 داخلی:
https://guardts.ir/f/ee1f60ae6d33
2- نسخه arembi داخلی:
https://guardts.ir/f/9d474d75a4fb
3- نسخه universal داخلی:
https://guardts.ir/f/7af85b518302
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/3100" target="_blank">📅 12:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3099">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompng(Asal)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.html</div>
  <div class="tg-doc-extra">21.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3099" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📍
اسکنر سبک آیپی برای شیر و خورشید
-فایل بالا رو با مرورگر باز کنین
-رنج آماده آیپی رو انتخاب کنین(با میتونین دستی رنج‌های آیپی مد نظرتونو وارد کنین در بخش لیست بازه /ip)
-بدون وی پی ان اسکن کنین .
-لیست آیپی‌های سازگار با نتتون در انتهای صفحه در دسترستون قرار میگیره و میتونین وارد شیرو خورشید کنین.
@p1ctok</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/MatinSenPaii/3099" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3098">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef65e3054f.mp4?token=KVNCHbalY40y05TLwdOcnRzv-FdeDm6hzeU2rsw8vVD9xnW12SNT1at0GvDbRl-Mq3J5wzJDpFDv4LAPOmmmGCr82YNhwJ0OQ11Y16AGg1U0quyVEZInPWqLnCUcR0zhCTeLJZ64Pq_ZAl54H9N4ZQOuFQrmzNYmsYs7dHeYJoakHd23I_xIu68esZKfjS7_FZYjOoBRlE9QN31qK5Ke0DUZTsiaMc1IqsiFCXS9hiNJB_PKElc1BH9hY_vPYuPCS30NLt4B0zLFCrUglCFDOyDnqYnPi96VYLfkpDyXPjwjjyPfBIBbgR-fGOM_cqsaIPGiBsIZwzO90dSlX9DwUovMYy7oNl4Z3Eba4XSJXfuBE3o4QDeqMdoB5ZS5w7oRiDAhncjbehZmL5eGl2peLqhtDrf7XfiVQB0mU1DXujXj14aaSneMzpGOV3gz7vYseShVgH5CbXalif9XAXf6GQufBGQ6IaoeeJ7tOFbxSZhqS9E-5y-vgOG1eLiamsYWMEXn1vgGFNNVAh7lGzOubaihHFeVitJwdvLwDma4byso-J32TVpjKdx8zGWuUwUPhbn4yKUTH3gZC9oRqR_VO61pB924PgEo2TZ7TJ9cpaqDm33ub6XDbBg-5eF-kbs_71-EZU1eLkcVffGQ9BJK_HRbGcIJOP-VknaeygUR9rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef65e3054f.mp4?token=KVNCHbalY40y05TLwdOcnRzv-FdeDm6hzeU2rsw8vVD9xnW12SNT1at0GvDbRl-Mq3J5wzJDpFDv4LAPOmmmGCr82YNhwJ0OQ11Y16AGg1U0quyVEZInPWqLnCUcR0zhCTeLJZ64Pq_ZAl54H9N4ZQOuFQrmzNYmsYs7dHeYJoakHd23I_xIu68esZKfjS7_FZYjOoBRlE9QN31qK5Ke0DUZTsiaMc1IqsiFCXS9hiNJB_PKElc1BH9hY_vPYuPCS30NLt4B0zLFCrUglCFDOyDnqYnPi96VYLfkpDyXPjwjjyPfBIBbgR-fGOM_cqsaIPGiBsIZwzO90dSlX9DwUovMYy7oNl4Z3Eba4XSJXfuBE3o4QDeqMdoB5ZS5w7oRiDAhncjbehZmL5eGl2peLqhtDrf7XfiVQB0mU1DXujXj14aaSneMzpGOV3gz7vYseShVgH5CbXalif9XAXf6GQufBGQ6IaoeeJ7tOFbxSZhqS9E-5y-vgOG1eLiamsYWMEXn1vgGFNNVAh7lGzOubaihHFeVitJwdvLwDma4byso-J32TVpjKdx8zGWuUwUPhbn4yKUTH3gZC9oRqR_VO61pB924PgEo2TZ7TJ9cpaqDm33ub6XDbBg-5eF-kbs_71-EZU1eLkcVffGQ9BJK_HRbGcIJOP-VknaeygUR9rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
آموزش کار با اسکنر آیپی برای اتصال از طریق CDN با هسته‌ی سایفون اپ MahsaNG ورژن 16
این آموزش رو فربد عزیز زحمت کشیدن ضبط کردن و برای من فرستادن
فایل‌های مربوطه رو هم در ادامه قرار میدم واستون، و دارم فایلهای MahsaNG نسخه 16 رو واستون روی لینک داخلی هم آپلود میکنم</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3098" target="_blank">📅 12:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3097">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تمام آیپی‌هایی که روی همراه اول جواب میده و شیر و خورشید وصل میشه(حداقل 10 دقیقه صبر کنید، بعدش که وصل شد دیگه خاموش نکنید
😂
): 184.24.77.42 2.23.168.213 2.23.168.174 2.23.168.7 184.24.77.32 184.24.77.5 184.24.77.7 184.24.77.16 184.24.77.36 184.24.77.21 2.23.169.111…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3097" target="_blank">📅 10:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3096">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تمام آیپی‌هایی که روی همراه اول جواب میده و شیر و خورشید وصل میشه(حداقل 10 دقیقه صبر کنید، بعدش که وصل شد دیگه خاموش نکنید
😂
):
184.24.77.42
2.23.168.213
2.23.168.174
2.23.168.7
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
2.23.169.111
2.23.169.105
184.24.77.11
184.24.77.29
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
104.78.170.186
96.17.222.31
23.41.37.129
23.2.13.227
23.222.126.108
2.20.255.113
2.17.251.98
23.2.13.152
95.101.23.27
2.21.239.21
23.211.49.252
88.221.168.5
104.103.90.156
23.79.20.249
88.221.132.162
23.59.235.208
23.60.69.118
23.46.188.71
104.122.212.92
23.219.1.4
23.57.43.195
184.51.252.135
2.22.6.68
23.217.11.56
95.100.69.108
23.40.63.69
96.16.122.74
104.109.250.232
92.123.104.7
104.110.191.57
104.83.5.82
92.122.166.168
104.83.5.65
104.121.0.17
104.66.70.133
92.122.166.146
23.73.2.161
92.122.73.138
92.122.166.141
96.16.122.55
104.81.108.51
23.72.248.214
104.126.37.185
104.83.5.201
104.83.5.216
92.123.104.67
104.83.5.203
96.17.207.151
88.221.168.138
96.17.207.149
104.81.108.10
23.73.2.148
92.122.166.175
172.237.127.6
104.81.104.13
96.17.207.137
92.123.112.7
96.16.122.75
96.16.122.70
92.122.166.182
104.109.128.153
104.96.143.134
23.73.2.141
104.83.5.202
23.67.136.200
23.67.136.202
23.65.119.52
92.122.166.236
92.122.166.234
92.122.166.237
104.110.138.190
173.222.200.5
184.51.252.36
184.51.252.38
104.83.5.208
96.16.122.146
96.17.206.214
92.122.166.197
104.94.100.73
104.83.15.66
88.221.213.81
172.239.57.117
104.117.76.40
184.51.252.4
96.17.207.30
96.16.122.83
96.16.122.150
23.73.207.11
96.16.122.77
96.17.207.155
92.123.189.82
96.16.122.82
96.16.122.66
96.7.218.219
96.16.122.137
184.51.252.157
92.123.189.41
184.86.251.12
96.16.122.154
184.51.252.152
96.17.207.12
23.79.48.162
151.101.0.223
151.101.128.223
151.101.192.223
151.101.64.223
65.109.34.234
142.54.178.211
2.23.168.47
2.23.168.96
2.23.168.144
2.23.169.207
2.23.170.80</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3096" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3095">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یکی از
بچه‌های توییتر این
آیپی ها رو یک ساعت پیش منتشر کرده برای شیر و خورشید. همچنان متصل
🔥
184.86.103.210
96.16.248.183
92.122.16.5
96.16.249.60
96.16.249.9
23.12.156.115
23.216.77.16
23.62.61.53
23.39.148.245
23.210.73.133
23.44.201.136
23.205.46.167
184.30.150.142
23.220.161.217
184.28.165.4
23.46.230.133
88.221.168.204
104.96.158.174
184.51.252.4
172.234.199.15
104.85.26.14
172.237.145.27
92.123.103.24
172.234.159.58
185.200.232.43
2.17.100.200
2.19.205.42
2.19.205.50
2.19.252.134
2.20.169.70
2.20.170.91
95.101.111.144
2.16.245.188
2.18.69.150
2.16.106.4
23.58.222.107
184.25.28.31
23.47.124.134
23.50.131.147
23.46.190.18
23.58.222.147
23.56.162.186
23.44.203.68</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/MatinSenPaii/3095" target="_blank">📅 02:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3094">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دست از سرم بردار فیلترچی</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/MatinSenPaii/3094" target="_blank">📅 17:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3093">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گویا یک سری دوستان با تغییر LTE(4g) توی تنظیمات شبکه گوشی به 3g تونستن راحتتر کانکت بشن به شیر و خورشید.</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/MatinSenPaii/3093" target="_blank">📅 17:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3092">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/MatinSenPaii/3092" target="_blank">📅 16:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3091">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kEoJ4ra-QSp7jNFE55L3XJSDNF64yl1exQSS9Ty-oUhU9G-JrqIJ5z_6CHkQD-T3l2QHQdybWnCnqilf_Y8arz_OLoxueBywajqO53lDeEmi5SGp-JsUy3xZWlrI6LjR4qG717meBEhQLy9u4-kTSqidVNEPBRvyrH1MWwAvJ_E9kP85JOUtPWbVr1WMWtzosiWScOfg9oHMb4rq9lRmWKESTRI7nIqGgfh7PuhYZTEh-DUljTCCIz_Wunfy_wDUZXxOIdFICWuXVZktiT5U_88W_XcClKz-h4njj4ve4lZP999gARBud9ev9bk6inu_DHBkBsdbkEDSgTvpK3jOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست رو یکی از بچه‌های توییتر واسم فرستاد و گفتش که از دیشب(و تا الان) روی ایرانسل با یه کلیک وصل میشه روی شیر و خورشید. اگر کانکت نشد، مجدد عرض میکنم که بذارید هواپیما و بردارید، آیپی جدید بگیره: 184.24.77.42, 184.24.77.32, 184.24.77.5, 184.24.77.7, 184.24.77.16…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/MatinSenPaii/3091" target="_blank">📅 13:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3090">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3090" target="_blank">📅 12:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3089">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این لیست رو یکی از بچه‌های توییتر واسم فرستاد و گفتش که از دیشب(و تا الان) روی ایرانسل با یه کلیک وصل میشه روی شیر و خورشید. اگر کانکت نشد، مجدد عرض میکنم که بذارید هواپیما و بردارید، آیپی جدید بگیره:
184.24.77.42
,
184.24.77.32
,
184.24.77.5
,
184.24.77.7
,
184.24.77.16
,
184.24.77.36
,
184.24.77.21
,
184.24.77.11
,
185.200.232.49
,
185.200.232.50
,
185.200.232.42
,
185.200.232.41
,
23.48.23.186
,
23.48.23.133
,
23.48.23.195
,
23.48.23.178
,
184.24.77.29
,
2.22.21.152
,
95.101.23.82
,
23.215.0.164
,
23.197.161.35
,
184.28.230.87
,
23.220.128.221
,
96.17.207.142
,
23.50.131.18
,
23.36.162.209
,
23.219.3.212
,
23.223.245.150
,
96.16.122.59
,
23.2.13.138
,
23.2.13.144
,
96.17.207.135
,
23.220.113.51
,
96.17.72.41
,
23.203.185.105
,
2.16.27.71
,
2.16.244.11
,
2.17.147.89
,
2.17.251.98
,
2.18.190.26
,
2.18.190.27
,
2.19.10.30
,
2.19.196.105
,
2.20.255.113
,
2.21.89.66
,
2.21.239.10
,
2.21.239.21
,
2.21.239.23
,
2.21.239.29
,
2.22.6.68
,
2.23.176.166
,</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/MatinSenPaii/3089" target="_blank">📅 12:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3088">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TZOSMciVXrpFWTegJ2uWZxoTCKW7bsVTXVxnmJ0m96QZxhJynQeJg_rWvHRHK9NkLAbuZvmeLxRX0KHPIavrxlRX-oVaumaZUXF7t8nVTc2d2wcjJnVQ44eeIQ7PiOFNMVG_gXh6DSiRoVvR_yeUigJc9THEF7KYCg6LKqY6mEak7Z1LkfFqSaeWHvyN7VTs-bgHU1QprHRwb_TtoWSo_vruUhkHO71Ifgh1X8oVAqXMb3F9hD6yztWXUmB88wa9MSVztl3YxEg0sSzUOe46xIQmFa0-VYwZLm3zR9FHfkuZoT8Zg7IEEgiz8Rmj4tt37kO7NVb9hRsIBlP8dv5iYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر راس گلر
:
روی ایرانسل تست شدن، مناسب CDN شیروخورشید.
23.65.119.52
23.73.2.141
104.110.138.190
104.83.5.202
92.122.166.236
92.122.166.234
92.122.166.237
96.16.122.70
23.67.136.200
23.67.136.202
همینجوری paste کنید اوکیه نیازی به کاما(,) نیست</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/MatinSenPaii/3088" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3087">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nh02v3hRGLNcVYS-i92JyWX10sakvSng9dWE5oF7ruARgmQ5bAqpJjWAqdNDUWqACrON9Z9Rml0jyh9VXahGJuONLyH9MX3USU5gaIDhUKJjGrrDoSEo9YTnkdfITHdZETEqwFLLoflbKmEMifAar51yH8shFQj4rEi97-u_K8AO4S8TMRGavwGpcq5zrFbMqgwOV1Pt6qC25rTvFFgKKayPLXxWY34CPWHLot1NCfBeM4v_wC1UAOAQrsSewALr5nccCJvwDy6eLWX4Fv3kF2ZAq2GCLJS8Ce_WQNfRe15Bh-SGr29LD1ZGbATwD4vd7ikpLSjda8_lTYql3NrDIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود اپلیکیشن‌های اندروید از گوگل پلی با اینترنت داخلی
از طریق این پروژه، میتونید ربات تلگرامی‌ای رو ران کنید که به راحتی لینک گوگل پلی شما رو تبدیل به لینک داخلی میکنه:
https://github.com/ZethRise/PlayDL
این هم نمونه ربات پیاده‌سازی شده:
https://t.me/APKNitoBot
✉️
@MatinSenPaii</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/MatinSenPaii/3087" target="_blank">📅 10:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3086">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه 1.0.3
یک آپدیت متمرکز بر پایداری است. در این نسخه پایداری اتصال بهتر شده، مپ شدن تنظیمات Advanced اصلاح شده، تفاوت بین SOCKS5 و System Proxy شفاف‌تر شده، و احتمال حالتی که برنامه Connected باشد ولی سایت‌ها باز نشوند کمتر شده است.
WhiteDns Windows v1.0.3
- راهنمای سریع تست
لطفا برای تست اول این تنظیمات را استفاده کنید:
1. برنامه را باز کنید.
2. وارد بخش Connect شوید.
3. گزینه Proxy Mode را روی System proxy بگذارید.
4. وارد بخش Advanced شوید.
5. گزینه Transport preset را روی Balanced بگذارید.
6. این موارد را بررسی کنید:
- Compression = off
- Base64-encode data = Off
- DNS listener enabled = Off
- SOCKS5 authentication = Off
- Packet duplication = 0
7. در صورت نیاز ذخیره کنید و سپس Connect بزنید.
اگر سایت ها ناپایدار بودند یا باز نشدند:
- فقط همین یک مورد را تغییر دهید:
- Transport preset = Stable Iran
لطفا این موارد را گزارش کنید:
- آیا اتصال با موفقیت انجام شد؟
- آیا یوتیوب و سایت های عادی باز شدند؟
- از چه Proxy Mode استفاده کردید؟
- سرعت مرور مناسب بود یا نه؟
- آیا برنامه یا سایتی بود که با وجود Connected بودن کار نکند؟
@whitedns</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/3086" target="_blank">📅 08:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3085">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اینها رو یکی از بچه‌های توییتر جمع‌آوری کرده و منم واسه‌ی شما می‌ذارم. آیپی برای شیر و خورشیده، بخش sni رو خالی بذارید. خیلیا تونسته بودن وصل بشن باهاشون: 2.16.27.71 2.16.244.11 2.17.147.89 2.17.251.98 2.18.190.26 2.18.190.27 2.19.10.30 2.19.196.105 2.20.255.113…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/3085" target="_blank">📅 08:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3084">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اینها رو
یکی از بچه‌های توییتر
جمع‌آوری کرده و منم واسه‌ی شما می‌ذارم.
آیپی برای شیر و خورشیده،
بخش sni رو خالی بذارید.
خیلیا تونسته بودن وصل بشن باهاشون:
2.16.27.71
2.16.244.11
2.17.147.89
2.17.251.98
2.18.190.26
2.18.190.27
2.19.10.30
2.19.196.105
2.20.255.113
2.21.89.66
2.21.239.10
2.21.239.21
2.21.239.23
2.21.239.29
2.22.6.68
2.22.21.152
2.23.176.166
23.2.13.138
23.2.13.144
185.200.232.50
23.2.13.152
23.2.13.153
23.2.13.186
23.2.13.201
23.2.13.227
23.33.126.163
23.36.162.196
23.36.162.198
23.36.162.202
23.36.162.208
23.36.162.209
23.36.162.215
23.37.197.128
23.37.206.186
23.38.49.97
23.39.249.249
23.40.63.69
23.41.37.129
23.44.10.10
23.58.222.147
23.59.235.208
23.60.69.118
23.65.119.52
23.67.136.200
23.67.136.202
23.72.248.214
23.73.2.141
23.73.2.148
23.73.2.161
23.73.207.11
23.73.207.16
23.79.20.249
23.79.48.162
23.192.46.51
23.192.237.208
23.192.237.209
23.192.237.222
23.197.161.35
23.200.143.71
80.67.82.179
88.221.92.177
88.221.132.162
88.221.168.5
88.221.168.138
88.221.213.81
92.122.73.138
92.122.166.141
92.122.166.146
92.122.166.175
92.122.166.182
92.122.166.197
92.122.166.234
92.122.166.236
92.122.166.237
92.123.102.104
92.123.104.7
92.123.104.67
92.123.112.7
92.123.189.41
92.123.189.82
95.100.69.108
95.100.156.147
95.101.23.25
95.101.23.27
95.101.23.82
95.101.23.168
95.101.23.170
95.101.29.12
95.101.29.30
95.101.29.54
95.101.35.73
95.101.35.83
95.101.181.125
95.101.200.63
96.7.218.219
96.16.122.48
96.16.122.55
96.16.122.59
104.83.5.65
104.83.5.82
104.83.5.201
104.83.5.202
104.83.5.203
104.83.5.208
104.83.5.216
104.83.15.66
104.94.100.73
104.96.143.134
104.103.64.7
104.103.90.156
104.109.128.153
104.109.250.232
104.110.138.190
104.110.191.57
104.111.202.158
104.117.76.26
104.117.76.40
184.24.77.32
184.24.77.36
184.24.77.42
184.25.52.200
184.28.230.87
184.51.252.4
184.51.252.36
184.51.252.38
184.51.252.135
184.51.252.152
184.51.252.157
184.86.251.12
184.86.251.27
185.200.232.41
185.200.232.42
185.200.232.49</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3084" target="_blank">📅 05:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3083">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نمیفهمم چرا هر متد جدیدی میاد و هر راه جدیدی باز میشه، یه لگد به گیتهابِ بدبخت می‌زنن
انگار فیلترچی می‌خواد ما رو تنبیه کنه
😂
داره میگه دفعه‌ی بعدی گوگل رو هم فیلتر میکنما، حواستون باشه این سری عصبانیم کردین</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/3083" target="_blank">📅 04:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3082">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">طرف بله و روبیکا نصب کرده بعد میاد توییت میزنه که اپ شیر و خورشید(که اوپن سورسه همه کدهاش وسط گیت‌هابه) بو داره نصب نکنید امنیتش پایینه🫩
امنیت؟
با من شوخی میکنی؟</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/MatinSenPaii/3082" target="_blank">📅 00:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3080">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6hiEt_4HbDp_bxYrw_mBj355J2InfMPFlCX1a8lPskoD4Cnyb3zAEc6r8drq3sX-5qozvC0hKu7DxylkaRw--RFZfWpyZmRFQ3WjNKn0DOeYnjBCdLC1QdrAxoFb8QMU0zyLR9eys_dz7QYCjbrlAlH072dmcW1D16w44i5RWGwi3gfY_4a4QA-lNVeeJ5Iyej3u3RI7_tpHgsUTNHIf1Bj5bmykeYUfU-EE9-pqjAc1_fnqokhyuKR1hH_QElf7fDcDMZfcLXh_BUuJOaLpmISAGL0oljNgcOYsK9Y8UahLpxb3iLTtnw9vEYU8wAbFcnELUAguemTyOx1vYxUGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62c2815606.mp4?token=vO2JwYAFyL2GNR3ZWFM4lu5oLTRlZfeMaB2PK1l4_JpGip7XlwQGLpmcgSDx0tNJg0gob1tjyNONn3HgF3VS1ILwk0_DEVSw47J3qnCM6zzFWxrbpS9jQU-RIm8dnd_jSTyzmXgQ1cxFf2UMdYx7Oxhqn1c1IGE6PW-JeJEFKumYuZoLqc_yiaUJk7_HmHFDS_6s_kyVkB7qdfQMI0yUNyfl84KZvUUXiMlo35oCYQohIqVN_6a35lWAUpGC7Mlo31oHUm5b3QBUbhIIkswR2ps73CQ8fBaYgaCrj8GvzbPrUFzvbaaiV1KcfDsj12T-WnvVu6sTCvJsXjTKa-U4vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62c2815606.mp4?token=vO2JwYAFyL2GNR3ZWFM4lu5oLTRlZfeMaB2PK1l4_JpGip7XlwQGLpmcgSDx0tNJg0gob1tjyNONn3HgF3VS1ILwk0_DEVSw47J3qnCM6zzFWxrbpS9jQU-RIm8dnd_jSTyzmXgQ1cxFf2UMdYx7Oxhqn1c1IGE6PW-JeJEFKumYuZoLqc_yiaUJk7_HmHFDS_6s_kyVkB7qdfQMI0yUNyfl84KZvUUXiMlo35oCYQohIqVN_6a35lWAUpGC7Mlo31oHUm5b3QBUbhIIkswR2ps73CQ8fBaYgaCrj8GvzbPrUFzvbaaiV1KcfDsj12T-WnvVu6sTCvJsXjTKa-U4vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چیه درست کردین
😂
😂</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3080" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3079">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبر خوب:
نسخه‌ی اولیه‌ی WhiteDNS برای IOS منتشر شد:
https://testflight.apple.com/join/GfUqXrFz</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3079" target="_blank">📅 00:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این آیپی‌ها رو موفق شدم از سرتاسر توییتر جمع‌آوری کنم برای شیر و خورشید، این بخش‌اش: https://t.me/MatinSenPaii/3070 کافیه که با کاما(,) پشت هم وارد کنین:  2.22.250.149 23.58.193.140 23.48.23.151 2.19.126.81 23.202.138.125 23.43.237.239 104.112.146.82 23.2.13.136…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3078" target="_blank">📅 00:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3077">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این آیپی‌ها رو موفق شدم از سرتاسر توییتر جمع‌آوری کنم برای شیر و خورشید، این بخش‌اش:
https://t.me/MatinSenPaii/3070
کافیه که با کاما(,) پشت هم وارد کنین:
2.22.250.149
23.58.193.140
23.48.23.151
2.19.126.81
23.202.138.125
23.43.237.239
104.112.146.82
23.2.13.136
72.246.28.37
2.18.63.49
2.16.53.11
2.16.53.50
2.16.19.136
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
185.200.232.8
185.200.232.43
185.200.232.40
185.143.232.122
185.200.232.9
185.200.232.11
185.200.232.16
185.200.232.17
185.200.232.19
185.200.232.24
185.200.232.25
185.200.232.26
185.200.232.34
185.200.232.40
185.200.232.42</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3077" target="_blank">📅 00:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دور زدن فیلترینگ با کانفیگ سرورلس با ترکیب nekobox و v2rayng</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/3076" target="_blank">📅 23:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oqMQwOfuKK68Z4Y96QP3TxTKIJtMkU3x4XT1M2bv_6dkpTBLuaUOWaLCFwgTI5677zGv_fvaTcliSV64x2n_Xof4mhlujsQQMR4jJ1pxNgfYKLL81s7SytnRv4HBwsc_g0mkLLJcKRuzCBBNEh5Pj-EhkLUHRIvQUw8J0TyNmFoXeLo_lA6pAIuarUUbU2vNLhBcXkAB5jv7TA_5HyScxhhGv-JzJBRvp3umLwJ8YvHcFbzJBjKfNsehEoswhTXd1E8yRWneBalVMxp53Yc88wTi_n4TPVKTfKQdlkvBAXGII6zfZZ7ks_otzr4xyMw10DzEebZVwJSKyKpLeMQ6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I1QB_dbh0dqVAAQ6pFDimoSmKD2BlLFxa6lGlpU_KPhPLai7P9EiYoxToFzut7jz1LQkBFk93llJtQK2nHgrXYzS_oJs0wmeITysZafhWJNRJjdmOjoZDFJhRuBE3Mqk4oKLy1gKIDWDTbhHAnkUUREYeRXB2Ep_NGVaA7V08KjnFOerTX2f40nNEXsnnyE0yOucE_wcjMvMSTY7WnOsrTpH3U4bo8RdofWGDm7A1NKXzQG9gYKebxFAfkqmjhBbn-qlG-lfbENBqcLQnaw2SZu6brUn6TfT36tyavvvIVNUjTOxgrnz3Uo13-Xqh9d8nthXRTx6LHVLiGMOkpsePw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر با شیر و خورشید وصل می‌شید، گزینه‌ی Share proxy on network رو فعال کنید. سپس به یه WiFi وصل بشید و کانکت کنید VPN رو.
بعدش با هر دستگاه دیگه‌ای اگر این کانفیگ رو بزنید(با توجه به عدد و پورت خودتون تغییر بدید):
socks://Og==@192.168.1.147:46597#ShirOKhorshid-MatinSenPIi
و توی گوشی آیفون(با Streisand)، مک‌بوک(با V2Box)، و هر دستگاهی که کلاینت V2ray با پشتیبانی از Socks داره می‌تونید وصل بشید.
خلاصه‌اش:
ببینید، گوشی A رو داریم که اندرویدیه
گوشی B رو داریم که آیفونه
حالا دوتاش رو به یه مودم وصل میکنیم
روی گوشی A شیر و خورشید ران میکنیم
میریم توی V2box اون کانفیگی که دادم رو(با آیپی شخصی سایفونتون که توی صفحه اصلی وقتی این گزینه رو فعال میکنین نشون میده) وارد میکنین
و میتونین عملا به شیر و خورشید گوشی اندرویدیه با گوشی B که آیفونه، وصل بشین</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/MatinSenPaii/3074" target="_blank">📅 23:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vH6zvpAqHmHY2bcp9TRguFKPk5hjvd0pjpUA1_mTKyINfVr0RoHOQxfA4X2dQwnGfp_xfHc1s-l7i0fbBltpfg2hZuJonj6_x2xsmzEaMpJwNkNxXmDl0thNBf1SRRfwRCV6Vn2mLaV3nKzAmsRYFsItbGfyp3GX03H2TFPXNM8tGd_RcRA1uoBIihEeiYl_u24_L3hbkp6Av3W8SV1hpBUi8UIxuEdnsglPIJT3akd4tVeymV8ylSb9edu6R8jJnYEVzfm3MJzdy1UcdSeBXs5Qje1jRsz5lDdoVE3o1CsYct2okfI-2Sc-XSMRKyKO1wsXkkbajw-rzF3SkCzGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
‏این دوتا هنوز وایت لیست هستن، چک کنید ببینید میتونید باهاشون وصل بشید یا نه.
sophos . com >
185.200.232.27
,
185.200.232.16
> Akamai
www . mathworks . com >
2.23.169.12
> Akamai
برای mathworks حتما www بذارید.</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/MatinSenPaii/3071" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3070">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eVx3XXpC53NeU1e0VqYb4mgXyMpZz1gKSgVSD3c0cM0hQn-UaiMVpNKi4jsyNPHjHFaWj63ylk4BgEFPSGId_X6eYNIQzsFjuHfQwuPUZQCnKli--1NXFK61wTJ9ML6hp-sp3HtUHrYstIvcoU5vbgZBxgCLfGEKbArqP9Tg9RcOAyRj5qL8ZkfY-7PUzKFbdzAGSidqpV_mTpTR1QvTpCv60YPM2bw_fiUB6D9vWjkXxn8-iV0xm_4fwKasRGZdl0v6_WnVXDE3Xu0VNi8lVIToyUbgdFNahaNusUX8SLrPfa__G7jgyggxkPHvHA2l3mnn4m4gd8Ol3h1p64AVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان توییتر روی ایرانسل با این دوتا روی شیر و خورشید وصله کاملا اوکی:
CDN Edge IPs:
151.101.192.223
CDN SNI Hostname:
python.org
‎
توی همون قسمت More Options هستش</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3070" target="_blank">📅 17:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-MatinSenPai.npvt</div>
  <div class="tg-doc-extra">3.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3069" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرور رایگان</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3069" target="_blank">📅 17:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3068">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkE0X2r91vihMo83r8gJtX5xH1XF5yGZDZI1AIMFzK6duLYngPfn7Hxg286Ar-ryLeLSiVXIDeAEuvBtdsM9lzeP3JVQ86Z2WblEHyAsb-Kv1qyRkKYeCI-c9rXiiIn-SQNT6RzFlZ1VPbsdt7nIzNFNMnKP3eftz2dOmuTRDwS1uZkiGXjQK83aMhrnndpmDgtwhQ-ff7tQyIeARRnsJmSGJmjYS0PRbdohD93hGyRqDNzfIFbsiizMp2CrgDBUBqJzs9mQCjk9V0_cP3dN7MsF19AbmY68QUw6-7kDjVYOXKUfxOC9bQlOylzckE_nQTaGgG4jp1gBkPeNXjcGEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود راحت‌تر پکیج‌های Dart و Flutter
وقتی "
pub.dev
" کند یا ناپایدار می‌شه، PubYar کمک می‌کنه پکیج‌ها سریع‌تر و مطمئن‌تر دانلود بشن.
پاب‌یار فقط یک mirror ساده نیست،
مسیرها و DNSهای مختلف رو بررسی می‌کنه و بهترین راه دانلود رو برای "flutter pub get" انتخاب می‌کنه.
مناسب توسعه‌دهنده‌های Flutter و Dart
PubYar.ir</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3068" target="_blank">📅 15:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3067">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گوگل من روی همراه اول یه بیست دقیقه‌ای بسته بود.
نمیدونم دارن چه گندی می‌زنن باز</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3067" target="_blank">📅 10:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3065">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vpRY-MfJZW4LTbN7rE0PqyU2yi6ldQNsGyIiyZYLquxXTY0VDFVdl9Kd1BTN-4NK5wtFyL3G_S6gAgA8JcL-75JQcPbb-WyoEukKq_-cbpBrkheDAbRLFbIL59A9hrWye6grqrPuPSdFisF5pl7PARePmn52pCEqB_XjZ2PRtCgXsYaLcD3Hddg3Aoi23p5rN1LaCfmPH3d6hONnNYiv7CfmkHvFvd10bULlb54WErbt-RUsaQXwlj64vVboPRZi4tS-fD3RY3_lzx_YrsHg2lq4SxzQRLqsQQ02EOPYofogXUzCqcopM8lGxQdEVa1hZvth8kGN2biOwFDDAUvEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k7uL-KQz_xR2TvIHxP9D0fr0h7pfLmHFr9jrb8Sb_HskBIh2e-MRg-HMCbxioo2OfJMWEjtsxB6XXqd3gwW6-sGeyZf8F7Hpv31VWqC1FCJ2Q0xLPmBRlUNyqSKO1VXbAI6aEvWGM2f7HvWNUb9gqd6F0Z52ZY24b0SkbKBu4cArI1j5o5SVte6RP-unw-7EDCUgmw8kHdM5JnkzN-GuBs8Bh5YjOpcMkXj8SAmmngN1Ge-U8bXkkklryJA5qfKru0g2GbzlJeVZ4eiZRKLVsuAn_WK78a6RFvBR0nW1fyRppN8SdxwJ7Qb6jzk28qm3ecSk61mArWUnUl0LGZ_FzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرور رایگان</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3065" target="_blank">📅 08:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3064">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ورژن جدید White DNS با یه سرعتی ریزالور اسکن می‌کنه که آدم باورش نمیشه</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3064" target="_blank">📅 07:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
آموزش خیلی مقدماتی و ساده برای استفاده از این نسخه
@whitedns</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/MatinSenPaii/3063" target="_blank">📅 06:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3062">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">masscan.rar</div>
  <div class="tg-doc-extra">1002.7 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3062" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینم نسخه gui مس اسکن خیلی کار کردن باهاش راحت تره
قبل شروع اسکن باید winpcap-4.13.exe نصب بشه روی سیستم(سرچ و دانلود کنید از گوگل)</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/MatinSenPaii/3062" target="_blank">📅 01:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3061">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.txt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3061" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر بسیار پرسرعت Masscan برای اسکن آیپی‌های Akamai:
یکی از دوستان این رو نوشته و خواست بدون انتشار اسمش منتشر کنم این رو:
متین اسکنر سم و پینگ خیلی کندن
از masscan استفاده کنن چند هزارتا در ثانیه اسکن میکنه، من راحت تو ۵ ۶ دقه ۹۰ تا آیپی پیدا کردم
دراپ ریتش ولی رو نرخای بالا زیاد میشه.
کپی از چتای خودم:
چجوری اسکن کنیم؟‌ اگر masscan داشته باشید خیلی کار راحته صرفا این دستور رو بزنید:
sudo masscan
2.16.0.0/13
-p443 --rate=500 -Ss -Pn
جای اون رنج هر کدوم از رنجای زیر (رنجای آکامای هستن) رو میتونید استفاده کنید:
104.64.0.0/10
23.32.0.0/11
23.192.0.0/11
23.0.0.0/12
172.224.0.0/12
2.16.0.0/13
23.72.0.0/13
172.232.0.0/13
184.24.0.0/13
23.64.0.0/14
ریت هم می‌تونید زیاد کنید
https://github.com/robertdavidgraham/masscan
این خود پروژه
ویندوز هم داره
کل رنجای آکامای هم اتچ کردم با فلگ
-iL
میتونی بدی بهش
همشون رو هم ۵ ۶ ساعت بیشتر طول نمیکشن (خیلی زیادن)</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/3061" target="_blank">📅 01:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3056">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">psiphon-helper-force-fastly-1.json</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3056" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چند کانفیگ سایفون‌هلپر متصل.
تمام اینها صرفا با تغییر ip یا sni در کانفیگهای
force-fastly, force-akamai
که در
https://t.me/projectXhttp/354790
قرار داده شده بدست آمده.</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/MatinSenPaii/3056" target="_blank">📅 00:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">برای اسکنر آیپی که خیلی‌هاتون پرسیده بودید دایرکت، ساده‌ترین راه اینه توی ترمینال(چه cmd ویندوز چه ترمینال termux) بنویسید
ping
20.20.20.20
(آیپی مورد نظر)
حالا اگر اسکنر هوشمند بخواید، میتونید از پروژه سم استفاده کنید که اصلش برای کلودفلره، اما میتونید کلا لیست آیپی بدید اسکن کنه:
https://github.com/SamNet-dev/cfray</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/MatinSenPaii/3055" target="_blank">📅 00:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3054">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یکی از بچه‌ها(abol) گفته بودش که:
از وقتی سرتیفیکیتو نصب کردم رو سیستم
دیگه نت سیستم به کل قطع شده
هر چی میگردم راهی برای حذف سرتیفیکیت پیدا نمیکنم
و این شکلی مشکلش رو حل کرد:
ریست شبکه در ویندوز گاهی همه فایل‌ها رو پاکسازی نمی‌کنه. این دستورات رو در حالت ادمین امتحان کن:
توی منوی استارت تایپ کن cmd و روش راست‌کلیک کن و Run as Administrator رو بزن.
این دستورات رو یکی‌یکی وارد کن و بعد از هر کدوم اینتر بزن:
netsh winsock reset
netsh int ip reset
ipconfig /release
ipconfig /renew
ipconfig /flushdns
در نهایت سیستم رو Restart کن.</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/MatinSenPaii/3054" target="_blank">📅 20:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3053">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوستان من، خیلی ممنونم بابت حرف‌های پر از مهرتون
🥰
خیلی خیلی زیاد خوشحال شدم از دیدن اینهمه پیام‌ زیبا
🌱</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/MatinSenPaii/3053" target="_blank">📅 20:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3052">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوستان من، خیلی ممنونم بابت حرف‌های پر از مهرتون
🥰
خیلی خیلی زیاد خوشحال شدم از دیدن اینهمه پیام‌ زیبا
🌱</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/MatinSenPaii/3052" target="_blank">📅 20:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اگر حمایت‌های پارتنرم نبود، مدتها پیش سلامت روانم رو از دست داده بودم حقیقتا. و اصلا بعد از دی‌ماه نمیتونستم هیچ کدوم از آموزش‌ها رو استارت بزنم و شاید از مبارزه ناامید شده بودم. تشکر ویژه از شما، بانو
❤️</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/MatinSenPaii/3051" target="_blank">📅 19:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3050">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خب گویا آی‌پی دیفالتی که پشت جیسون بودش رو زدن. مجددا موش و گربه بازی سر آیپی و sni تمیز.
Pypi رو زدن،
خود
python.org
بذارید باید اوکی بشه. همینطور از آیپی های این پست استفاده کنید:
https://t.me/MatinSenPaii/3040?single</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/MatinSenPaii/3050" target="_blank">📅 18:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اگر حمایت‌های پارتنرم نبود، مدتها پیش سلامت روانم رو از دست داده بودم حقیقتا. و اصلا بعد از دی‌ماه نمیتونستم هیچ کدوم از آموزش‌ها رو استارت بزنم و شاید از مبارزه ناامید شده بودم.
تشکر ویژه از شما، بانو
❤️</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/MatinSenPaii/3049" target="_blank">📅 17:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G5J-x90Gyb_t_KBp219QFcuOhmUYJ6S6p0vKn46vmqZx1xdg6Qe_dGi1u-DeV6AaX7HBMxlbc5Nm11_aCkQ3sdGl8-UtZzhwJsj_HCGJbVdtqcx4l3D22MWjUe7wf5E9NAQHs7rLnntfOs49Ipu0FEtzXGn7-CQ-spTXkumimF-w1ewCpyKC4xGEEw-0CEv9n7pJ-XKhMhpTxx8tZGL9qYQNWyHEQTm2839YQGqzq-2rGSkZBkl71Hntr657F-3WnjWGWys8G96KHVp3PCWdpaVpJkGy56tWJvaqnEuELi4DyOXGXl4rBu82Yv8h3b3QahZDRBeSDnCt7tBgVhWHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
وقتی رو سایفون ویندوز upstream proxy ست میکنید دیگه اجازه انتخاب لوکیشن نمیده برای دور زدن این محدودیت ریجستری ادیتور رو باز کنید برید به این آدرس
Computer\\HKEY_CURRENT_USER\\Software\\Psiphon3
و EgressRegion رو ادیت کنید و Value data کد هر کشوری که میخواید بهش وصل بشید بذارید</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/MatinSenPaii/3048" target="_blank">📅 17:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3047">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اگر به ارور Upstream proxy میخورید، یعنی پورت رو دقیقا اونی که توی ویدئو گفتم ست نکردید. یا توی بخش مناسبی نزدید. باید مو به مو چیزایی که گفتم انجام بشه دوستان</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/MatinSenPaii/3047" target="_blank">📅 17:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3046">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">روی ویندوز از این آموزش استفاده کنید:
https://t.me/MatinSenPaii/3035
روی اندروید مستقیم وصل میشید با این اپ:
https://t.me/MatinSenPaii/3038</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/MatinSenPaii/3046" target="_blank">📅 16:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">Matin SenPai
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3045" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lPTtlFmHh0QMpg3GY9_Xb6nvEeeih0pqSEEOUlP5yJq4TJr59M3TYcnuE15lkDoK027AZCuKT6a-kJby6lnkYm0GAeaFauQrNjaHHZvgC-YbG63Sw3cOC3k7wkaWpRPURIUWVePBfc_Z_N7I6oj32LVU-XLVgDAN-7U5wFkTiuO4ukP0ZQmDDB5zxZTJb3Q_h7QCZOXToyh8TvN3rr2CcbYUODbJ5-yzcef3sYLR6IdmeFvyf4_EHwQ8CHHEknyqgEx9rbRy9s6wwjc99bknHKUisyL15THWbhhgygHi7Qyhv3KowR2votdO_W872_q0GOtuOSg7qZnZbWz1HHw0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/MatinSenPaii/3044" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/MatinSenPaii/3043" target="_blank">📅 15:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fct5QRjLcXPjrRQgKdUhDdB4kWDm1b8t-pLzBVc7D-eunr7II2dmhq0tby1wz-jPnva0BZBgwhsEtxnDVXPKWtW82RlaBH2DCh1MYKL99bSjdazoVF9E86hGIm2OHO6U0oxVlJfJGl40Y9t5UbbvYR-Zj6BIKsOOcJ2mvKQakNHPd3D3Fe4yh-bfbXVrEy-O0Isldh4tTQwR2Nz8UUU4_rD6CmdtJrmpBFJXP1UbiXDGLbsP3pXtTO7lm1wo_uGI5EX3-DlopVlYaNo786ff499mz0o5_pE34h7vtBrIu_LJcbOUHklxF0or40rA_04jqcAKAimCh3ytGfZXeYow7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/MatinSenPaii/3042" target="_blank">📅 15:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3041">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3041" target="_blank">📅 15:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RrVUvFjJUUmHs5josJnX6WLXw3gytbTBfqKWJEj7VVs2ne6gdqOHe78dlM_lukjw2__PZFp-5bATcCMtmdaG3_ZFEz9XisqYipGDvW-VT5EBNAYizheUHKgPsH6HqYh6-5G9IAMnz_3ui5eeVAfDc3-GI0YekZFwFA_VjJnXmE5hul1K8zL3kh8AJajx-r5WmaEYk4_61iNM8NuQZCJnH5gIBs4cVUafBK4YLzfrl_YbKVjMcyGb2mtepAV-5CL3Cs9h6aOaU3u3a31eaYiIblI2r3EZodcfRNoTkXQGmILdCTvOsWnOKVWp87fRrFtEe8UD__EST1jC-yV-R1PLsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dOhYtfR-LU5fsNpscz2haHq-VwmgYl30OdSD0upvlK-yzlLANxbA4Tatysn69zr9EpRuBSHOIc3ZubOLDqGju-7fk_Vf1qsbjLi42XObNuq-Jsc1RiOPGXXGdK90rCvs7PTqga8Oc0yvfHGnegh2q5A9_EJQCnhNJMPgTsOBO6js8JN0DS5AItSX8wrxubgmnyeA50pGCpdzrNUoU1OaCgg5qFVksF4iIShtRGeE5b5wNS30DUymAkJ0j7-JK6qhm3V5QuCyRDdOHL8H2muyUjOt8rL42DjTYe6CsF862B9E92GmQq10T87M05HswiWy9nR0m6QG_YDIZ_4Si5UQ4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ShirOKhorshid-2026.05.14.apk</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/MatinSenPaii/3039" target="_blank">📅 15:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3038" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛡
مهم: اگر این نسخه رو نصب کنید دیگه دردسر ستاپ کردن MITM و... ندارید!
این نسخه حدودا یک ساعت پیش توسط برنامه‌نویس شیر و خورشید آپدیت شد و به راحتی می‌تونید طبق این آموزش بهش وصل بشید:
1- وارد اپلیکیشن شیر و خورشید(آخرین نسخه که امروز منتشر شده) می‌شید
2- وارد بخش Options میشید از نوار بالا
3- روی More Options کلیک میکنید
4- گزینه‌ی  Connection Protocol رو قرار میدید روی CDN Fronting
5- میرید و عادی کانکت میشید و به راحتی وصل میشه!</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/MatinSenPaii/3038" target="_blank">📅 15:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3037">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حالا دیدین متد ترکیبی سایفون افسانه نبود و واقعا وصل میشد؟
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/MatinSenPaii/3037" target="_blank">📅 15:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوستان عزیز، خواهش میکنم به DNS بها بدید. معلوم نیست کی مجددا متدهای حال حاضر رو می‌بندن. از نرم‌افزار و آموزش‌های
@WhiteDNS
استفاده کنید و الان که اینترنتتون شاید اوکی تر باشه، نصب و ستاپ کنید</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/MatinSenPaii/3036" target="_blank">📅 15:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">☠️
آموزش اتصال رایگان و نامحدود به اینترنت با متد ترکیبی MITM + Psiphon
⚡️
لینک‌های داخلی جهت دانلود:
https://guardts.ir/f/db4006f1197c
و
https://uploadgirl.ir/d/1f4fb76a-c869-494a-b439-b11cb8d35947
(شامل فایلهای V2rayNG، کلاینت شیر و خورشید، ویدئو آموزشی، V2rayN و فایل Certificate Generator و خود فایل Json پترنیها)
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد ترکیبی سایفون(کلاینت شیر و خورشید) + کانفیگ دامین فرانتینگ پترنیها، به اینترنت بین‌الملل وصل بشید!
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/MatinSenPaii/3035" target="_blank">📅 15:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چه حالی میده رایگان وصل بودن
📚
از زمان SNI Spoof اینو تجربه نکردم خدایی</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/MatinSenPaii/3034" target="_blank">📅 11:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3033">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بی‌زحمت لینک سایت‌های داخلی برای آپلود(هرسایتی که میشناسید اوکیه) واسم بفرستید، تا زمانی که ویدئو حاضر شد واستون همزمان به همراه کلاینت شیر و خورشید و فایل جیسون و ... روی چندین جا آپلود کنم:
https://t.me/MatinSenPaii?direct</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/3033" target="_blank">📅 11:43 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
