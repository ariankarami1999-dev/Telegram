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
<img src="https://cdn4.telesco.pe/file/t3KQqeGcR1_NBhvsWyql0PxRp4R6cuLImz-ePVi3w5nAE6lI0HTwIzLtLF_xmnkYU_BKmCQv87m9cjyrrGBecsx4f7ZZ1xVEbtjMOEo8QmKbnHCKmAV-DxyR6hnKLGCnhg_F6Fz45jC1LIhjTa0mPdqE96nW64kdmmfWimTLvK5DYvZK2pe2yppFGKxOkSSJRGx_P5usGmfeMejkRYhWAJH9nlCMoO39sxsQrTOoQsvXl_q62ZYqa_AU8XIUe8E5HwzSxQC8EaXd65XErPIxoRnoqVYSvBq5h6SQo_xAv6sKtDwhwliZU9QvSWfATF2sXboDBNixC14FErCt8seHhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 951K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-129752">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
قالیباف: بدون دیپلماسی زحمت عرصهٔ میدان به ثمر نخواهد نشست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/129752" target="_blank">📅 21:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
قالیباف: مذاکره، یک روش مبارزه است و ادامه آن است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/129751" target="_blank">📅 21:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129750">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5QHIfqtg7_c_Z6-_u-cWpkiSvy3Kf0EpvlnqVJbc0oJ6kOGlyQuO0JL1Pdo2jDErXazDemYUxWj6aghJEAk7_q1BuAzhf18o0n9bNhI_JSZAx0DFb1LZQ_Yp-qf-oeKkJ64Qbuw-bSp5w35PJ_VJtcCWNmgQ_PGG-4-IMRpYe0cB0t5JGcrfjtPi7uRAvy5CmNxOMWMEiRdy5IgNwuybhICJsZSzHcp9wmMQfeniQ0U1ah7TCw8AYUO_hnlTeAUTy_p7v_0LIppMqK8hRcc4mgf7ASN5SL2Yq2eWWpYn2ERPMJo6Wh6pyjvbPJSBt8hYywr4HJxQ6G9Nhb3MLUGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عضو تیم مذاکره‌کننده ایران در اسلام‌آباد: احتمالا اموال بلوکه شده ایران صرف خرید مستقیم از آمریکا شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/129750" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2b1eb31f.mp4?token=WjQkffRfu7UHz9k_bMWdlgFfLwexCzC6j3ruYZICYQWbS55j7oY0VHTZOGdI98pImBpr7Jjk1R3zA90PxOugyqlI8gpGGYt9-76y8WDh2tVcQoTkpUup6BOgYYex0WtloPj-1PdwJQkdfEenIYFazn-_PAvqTec6fKIwO5VMXqhntEV2VXXr1vnXYG-BjI9CJaeKk2p8xFtjFm_BwTwPGPy2YeWhXoDzEN816ME41ncc21pA3XEUa18-kcmJwE2H79eHum1o2AXa22HtKnB2Bl98VmBgxmadvrqhzPAd-GF6YpnhbAKxRyMbqMNHSAFBfuAGZfoToOugHuhdRJnnsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2b1eb31f.mp4?token=WjQkffRfu7UHz9k_bMWdlgFfLwexCzC6j3ruYZICYQWbS55j7oY0VHTZOGdI98pImBpr7Jjk1R3zA90PxOugyqlI8gpGGYt9-76y8WDh2tVcQoTkpUup6BOgYYex0WtloPj-1PdwJQkdfEenIYFazn-_PAvqTec6fKIwO5VMXqhntEV2VXXr1vnXYG-BjI9CJaeKk2p8xFtjFm_BwTwPGPy2YeWhXoDzEN816ME41ncc21pA3XEUa18-kcmJwE2H79eHum1o2AXa22HtKnB2Bl98VmBgxmadvrqhzPAd-GF6YpnhbAKxRyMbqMNHSAFBfuAGZfoToOugHuhdRJnnsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو نخست وزیر اسرائیل با ژلیکا کوییانوویچ، رئیس دفتر ریاست جمهوری بوسنی و هرزگوین در اورشلیم دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/129749" target="_blank">📅 21:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
شبکه اسرائیلی i24: هیئت «اسرائیل» فردا راهی واشنگتن می‌شود؛ دور جدیدی از مذاکرات میان اسرائیل و لبنان از فردا سه‌شنبه در آمریکا آغاز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/129748" target="_blank">📅 20:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129747">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_NIFbCiCuMIKYk_wiUjQSoZGRb0LKy7boMg-HstZqp7Iqjxru0OL58JO046gp9zaMK_os5vTA-wN_ZSEabtSRWRNzxD5oJKWLb2XTiWmWLio09_OeHiy8Q-Yb3RMabqBtvebS12g47VCtl2k7HUbEXpIm5kkkWIqPh1roa8CEYOhIuXNE4LHqJ7PEnMsMhG2_wpu21WlOtgDXc7YYlrBgCBBOvMi6BweO1Pwyc8soKOpFaJbn21FbUC3JzObZ54zeYQpskGsn0onhqgA8JWwEFo4Dbq_FtkbgZHTE0UWsCBlfOlTCr47Lb7UlwQGf_t8pPqMirG2S8aBgcUEv4iMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز ۶ سوخت‌رسان آمریکایی بر فراز خلیج فارس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/129747" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129746">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC5Vi4uYqWkK10g7bXM-2508ulk9LCfT-fkSymF2keq67rb98z0qU6LmABc0K19dy6KhKThiFgo5mHv-uqW0eLYmzfcEIGmhkSAqGGgCL9NrWRhOzgTq0lhbTp-dE6vfb7TiDG_XAhGTwpocba6w0YSM53NMpw0aBjCFfOKIjsCw5Eg0G6vsy8KgrzSPfewcuQBnXx0OqwkqiUkTnATCmNOsdeP19hYEdyO9G3FCW_nn3XkJoi8Zzk7Cgi2lO3yrRIOhNde8VVellN_SGkaEnnLdn7upuzZ9BKZWjIYh35BGUptk7lFcup8cpCQ89aONbcOpIlryoUm0cArhrc37aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:  همه به خوبی می‌دانند که ایران برای تضمین «صداقت هسته‌ای» در سال‌های آینده، با بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد. رئیس‌جمهور دونالد ج. ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/129746" target="_blank">📅 20:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129745">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
در پی رفع تحریم نفتی ایران، قیمت خودروها از دقایقی قبل در بازار معاملات خودرو کاهشی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/129745" target="_blank">📅 20:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، کاتس : امنیت مردم و نیروهای اسرائیل اولویته
🔴
ارتش با حمایت کامل دولت اختیار کامل داره با هر تهدیدی تو غزه، لبنان و هر جا لازم باشه برخورد کنه
🔴
نیروها شبانه‌روز در حال عملیاتن و اسرائیل تو منطقه امنیتی لُبنان می‌مونه تا تهدیدها و زیرساخت‌های نظامی رو از بین ببره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/129744" target="_blank">📅 20:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رویترز: ذخایر نفت خام آمریکا به پایین‌ترین سطح خود از سال ۱۹۸۳ رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129743" target="_blank">📅 20:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129742">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHHxAsRMYW7cRjriCiU5tDherX_fNHJ1RemK3IT9qe6_cG0DuBLjvvFZr8DSgIUXV-Eb9AU62PEVeXtSQhtQ7r0CNrLDJ8u1_qgCtPTfWwygsVWQSEnt77aurgLntDIfcLRMsEAY3n13kY2qubitBpWlKov4wqdMhXhM0SjtoseNCHhMgXcBiJvwCkduaGzSDQIYGxNijFQm5gob3xLFEMyqZLQvn6dvetIsfe3BI-_k4EW-HZNdJgVNdlveHUx3Y9zeLLq5Hj5ZMccqhOSM1kLlqRt5c8EtWqyEODxBXb37GwPgzl8C5RrCQup42nISFrhey5VkBhp3nTHWakUu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا ادعا کرده، این معافیت تحریمی در ازای اجازه تهران برای بازرسی آژانس از تأسیسات هسته‌ای ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/129742" target="_blank">📅 20:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129741">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZXOJO4tQPT6X49J8pw87nL7u3Ev5YHZSGdp3ZOJ8c1nObkBRE7LmgaYeGt7u-78EF8DE4Nhwhs7wOf_UMe2ewov_6GqA--YBpjPXDKbMUfSvWeQUHffm_-Emjtvx_UtMAKgWP42d-t3fdz_YLEcv3ZhVcFfRxkrt4ABqYUATyYKcLW_0rrfosFZxvQAQ8QDlJLRCF1P1SqhuNDsXcH_47j8dKX3QGBxACGIuZ8defOGoWTQBNYDi36Yrhda3vephEBYDqVItwUO_YlcTg_jykxurmlff4N6y0fXdfDNCcZASfBDjzRaXSNdDQ_jyj3WC9p5TVtygiYoMS9cCbYEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا رسماْ معافیت تحریم‌های نفتی ایران رو برای ۲ماه صادر کرد ( تا ۳۰ مرداد )
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/129741" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129740">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZYWxzqHfFmDxCT7vrQkL62KERbPpA00tspNtr85XgLKfjwZM-vfWeXeu26QC80UsrCmTf7CSanK_0Q3roFhtZjlGUX9Ya4CpgkQBE3460cZOHBe0DVxI2JC1-aem08N-9zSUue9KevRZzaeHVJRraEAleLotJqLT797_PnUav8BwzbLG0DGerJ-_3eDVqliC52l9-2Vpr5ab9l2Rl0wk8huiyJJfI7SDI6ThhDsJwFEL7lspLuo62vGcPY6FSMD7vqgho8y6FVN4dTWj0ZzBRT7mdE9-apU3q7C9ZagbLCCE0ranJsKcqB2CX1Rmc0sgwEzhcuWN2TJ0fwyJOSvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/129740" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129739">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21803dc203.mp4?token=vWI_CWb_JHG5J5SoIHbNwvLAMZIgjBJoBFS2vIP7jtIATEzsIRZZ9MhuO-BYtAp8lVC1KluotyXtyXiM1M1RQDsCSJXlfoJiwzKPVnneMlj7e_Ehua0MQIkp8w16OXWo29N5K4OQziZaX5rAtDH1JEQFW-PtYwN4jhtxJImFjrwWOXRuROGG60ixvxLSox8Y4BdfB1YhbQPh-8G9S4Mpz4cuZMFHUPalL5wj38aIQdK5Cy2Owa8JKAq-XVu8069jIR6Upaocn8mr82_vkOVSPRGwRZoHXymB5TpFZT9g72ZotC1wjyW7R__yMUmRQ0OT9X21FCprnz_epK4gteHv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21803dc203.mp4?token=vWI_CWb_JHG5J5SoIHbNwvLAMZIgjBJoBFS2vIP7jtIATEzsIRZZ9MhuO-BYtAp8lVC1KluotyXtyXiM1M1RQDsCSJXlfoJiwzKPVnneMlj7e_Ehua0MQIkp8w16OXWo29N5K4OQziZaX5rAtDH1JEQFW-PtYwN4jhtxJImFjrwWOXRuROGG60ixvxLSox8Y4BdfB1YhbQPh-8G9S4Mpz4cuZMFHUPalL5wj38aIQdK5Cy2Owa8JKAq-XVu8069jIR6Upaocn8mr82_vkOVSPRGwRZoHXymB5TpFZT9g72ZotC1wjyW7R__yMUmRQ0OT9X21FCprnz_epK4gteHv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان: به امید خدا، شهرت بین‌المللی آنکارا امسال بیش از هر زمان دیگری افزایش خواهد یافت
🔴
پایتخت ما نامی برای خود به عنوان مرکز دیپلماسی جهانی خواهد ساخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/129739" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129738">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر خارجه قطر: مذاکرات فنی میان ایران و آمریکا ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/129738" target="_blank">📅 19:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129737">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فارس: ادعای معاون رئیس‌جمهور آمریکا دربارۀ بازگشت بازرسان آژانس به ایران کذب است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129737" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129736">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
قطر: ایران و کشورهای عرب خلیج فارس نشست امنیتی برگزار می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129736" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129735">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
به گزارش نیویورک تایمز با استناد به دو مقام اسرائیلی، سربازان اسرائیلی روز شنبه دستورالعمل‌های جدیدی دریافت کردند که عملیات آن‌ها در جنوب لبنان را به «اقدامات دفاعی» محدود می‌کند.
🔴
طبق دستورات به‌روزرسانی شده، نیروها تنها در صورت وجود تهدید فوری مجاز به شلیک هستند، مگر اینکه مجوزی از سوی رئیس ستاد ارتش دریافت کنند.
🔴
این دستورالعمل‌ها همچنین شلیک هشدار به غیرنظامیان بازگشته به جنوب لبنان را ممنوع می‌کند، مگر اینکه آن‌ها «بیش از حد نزدیک» به مواضع نظامی شوند. علاوه بر این، نیروها دیگر بدون تأیید فرماندهان ارشد مجاز به تخریب خانه‌ها یا سایر زیرساخت‌ها در منطقه امنیتی نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129735" target="_blank">📅 19:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129734">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فارس: ادعای معاون رئیس‌جمهور آمریکا دربارۀ بازگشت بازرسان آژانس به ایران کذب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129734" target="_blank">📅 19:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129733">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4D5o6U-kXg2xBtJCeCZ7vHOU3pXrhsAk3xiOHRPLTRR80XuCRqKh0KgXvH1NZiKgBaCI4wf3ULoWtp4JhagvUoef_PO0BzK0Bo5aaqFKasj8Tmz9YfJY8X4yUS4MviCorzD3KOJa_v3iiFNSz9ol5uZTiNAHeOwjMl_2jt08Ol5STSgm6SiXmi2kVi-WEl1V6D1KU2-A_uAF82_jYrbXiMRM-JGkXlZiuJkPQt0jXSnfEG04mViCIYqMs-zorv3Mo1f0i7jRrYIxNLkQ5UVffHrQ0LDf844AJ32gl9V1EvffAMR5_sIyLTtFk898oVjDRM9HOFEN6HMeAO0yIUSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف در سفر به عمان با  "هیثم بن طارق" سلطان عمان دیدار و در خصوص تشریک مساعی برای تثبیت ترتیبات ایرانی اداره تنگه هرمز گفت‌وگو خواهد کرد.
🔴
در این سفر عراقچی، رئیس هیئت مذاکره‌کننده ایران را همراهی می کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/129733" target="_blank">📅 19:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
قالیباف رئیس هیئت مذاکره‌کننده کشورمان دقایقی پیش تهران را به مقصد مسقط ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/129732" target="_blank">📅 19:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9UPLzjJIkWYy2srKCoK2hG7oMFD_5LBSorn17XMBESeKPNEbESXp8yYPFBU9W_uiJesXjPBUwuONjbtb15NMENy-02CR5hRmXbgBD_tp5vrn7IrAUQjwvDuKGn00DAvEkmtayEcD2WgvV3frhonmKbfVdy6V_5VBkWrIB64YChTtbHv2iME_djDxmwtcxbwQPm-JI8vKCzsUtTPOi6W2zmtMBWPGUrkQ91kTQSRuCbQOSVeAehjqOOq25WqIkdLA54tKw10l6jwmY49tACDsmRA6J8O6eq5qRmYz9s8-cO0LyI3pB6i9DgE1zkVbY53MnPplL3My-Ngx5fYKUemNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس:
🔴
وزارت امور خارجه تأیید کرد:  روبیو از ۲۳ تا ۲۵ ژوئن به امارات متحده عربی، کویت و بحرین سفر خواهد کرد. وزیر امور خارجه در مورد طیف وسیعی از اولویت‌های منطقه‌ای از جمله یادداشت تفاهم با ایران، تلاش‌ها برای تأمین ترانزیت کامل و آزاد و ایمن از طریق تنگه هرمز و اهمیت صلح و ثبات در منطقه گفتگو خواهد کرد.
🔴
وزیر امور خارجه در بحرین همچنین با شورای همکاری خلیج فارس دیدار خواهد کرد تا در مورد اولویت‌های مشترک در سراسر منطقه گفتگو کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/129731" target="_blank">📅 19:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
جی دی ونس:
اگه پول های بلوکه شده ایران رو هم آزاد کنیم؛ فقط باید باهاش از خودمون ذرت؛ گندم و غلات آمریکایی بخرن. تا هم کشاورزهای ما پولدار شن هم به نفع ایران بشه.
🔴
تیم ایرانی رفته اورانیوم ۶۰ درصد رو داده جاش ذرت و سویا گرفته‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/129730" target="_blank">📅 19:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اسماعیل بقایی، سخنگوی وزارت امور خارجه:
تعامل ایران با آژانس بین‌المللی انرژی اتمی طبق روال جاری و بر اساس مصوبات مجلس شورای اسلامی و تصمیمات شورای عالی امنیت ملی ادامه خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/129729" target="_blank">📅 19:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/129728" target="_blank">📅 19:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129727">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4e5db99c.mp4?token=qzBT69H71Q4k-AZPO89rNuPog-gBgCTjhHKlZX3BzUW5a2neYOGO1idLV7pde5ALpM13q2uVjHCdyrFdzghQPlJl8ZVxtNZYQxsO-jPTN2mTrySGshkij9tm432IWKjATn8k42AGMnhvR_aFOTWpPaBhYmv6QX2o3xs8AOPcMr0JgRvwueFa58giVNoWpOPnhhzgIMimudDnHsejy3HYidGB_kywvpXjK6UK1DAdSByyVkXfVfJB7GBgFviiPUd3MQpJzYiBpkrXk4wlmBVUskcraNmTJMydZhtL8DgG4V57AxR4Ua_lsK58AfzSRy3o0pf4w-ZslXeu1adWyR3894WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4e5db99c.mp4?token=qzBT69H71Q4k-AZPO89rNuPog-gBgCTjhHKlZX3BzUW5a2neYOGO1idLV7pde5ALpM13q2uVjHCdyrFdzghQPlJl8ZVxtNZYQxsO-jPTN2mTrySGshkij9tm432IWKjATn8k42AGMnhvR_aFOTWpPaBhYmv6QX2o3xs8AOPcMr0JgRvwueFa58giVNoWpOPnhhzgIMimudDnHsejy3HYidGB_kywvpXjK6UK1DAdSByyVkXfVfJB7GBgFviiPUd3MQpJzYiBpkrXk4wlmBVUskcraNmTJMydZhtL8DgG4V57AxR4Ua_lsK58AfzSRy3o0pf4w-ZslXeu1adWyR3894WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوش‌چشم، کارشناس صداوسیما:
خوش چشم
:
آمریکا ۱۰۰ آب‌نبات جلوی تیم مذاکره کننده ایرانی انداخته است تا مروارید ایران که تنگه هرمز است را از آن‌ها بگیرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/129727" target="_blank">📅 18:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ایرنا: تا این لحظه موضوع صدور مجوز برای ورود بازرسان آژانس به ایران توسط تیم مذاکره‌کننده یا مقامات تایید نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/129726" target="_blank">📅 18:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a94bde71b.mp4?token=eCd9RtfIX7_bmNh5TJrPZ-DDkh5ModqbEOjgH-TEyB8Er4q44ET595w1H9Rhitd1IA2vJjGzfrrkiG25Yf4aDUSbKSpPZYIa-p7XOLFN5CWTult48lw2O-54_56DbiwuyxmQsEk3YsA-l08i17P0jswvk9aH0j68rOOxrMxJY6jh4D_wUtagriU_eE7XB7fAtplZTv4KbEMrCvUbs4D-zvrM_MIYF39gReI5Hbt_VK4QTAhTHjAxFBFKllKqOTq71YUIigneBEA2Hl55S6WA8O8LRSIRk7MHsDHk6hZWGETzwXCN0_Hg6ewN_GRgVI72DV_oG_xDiw_rskhUAEXJhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a94bde71b.mp4?token=eCd9RtfIX7_bmNh5TJrPZ-DDkh5ModqbEOjgH-TEyB8Er4q44ET595w1H9Rhitd1IA2vJjGzfrrkiG25Yf4aDUSbKSpPZYIa-p7XOLFN5CWTult48lw2O-54_56DbiwuyxmQsEk3YsA-l08i17P0jswvk9aH0j68rOOxrMxJY6jh4D_wUtagriU_eE7XB7fAtplZTv4KbEMrCvUbs4D-zvrM_MIYF39gReI5Hbt_VK4QTAhTHjAxFBFKllKqOTq71YUIigneBEA2Hl55S6WA8O8LRSIRk7MHsDHk6hZWGETzwXCN0_Hg6ewN_GRgVI72DV_oG_xDiw_rskhUAEXJhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله مجری تلوزیون به قالیباف و عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129725" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBEAIDzGn7aP6JBERsYZJp63N6vmmWKV0ElNRSFwtIie1sCKGqAbZT4hdOUyC62fQkyvKdDFzO0-LVJ4KTpnKKpa6FGjdFL6FYs1pJK36bCO7zyejdWA5aeCed-uTNxDbxfl0QGOAHqphgNYvXj5KfNz3Q7FvIXlhuv9fublrBWeTlAwF2Ym20EJtVut2SNB0QnIuQ-OPbXh78-875EPV7quK7gJWHYjgiL5SCk8g_XQeq5-a-8EjJk6JoLo5wGb8QsJrFZ8ekvDhHrAWeuit8jyNI7mf8tlLItZ1qHK0Rp-vK5cGEpFCGDTpPMX0iL3MjjJeFk-_E2CAJKjCNYU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: قالیباف، دستش تو دنس ونسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129724" target="_blank">📅 18:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129723">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBLMKN2SlloCSHUoxnZmQkK-q6bOZzC-Z75ILd2L4vaCcmGmuYPq53m9RDE1z6Jirm0rkk4qi94VolLNz8RPDK6T2-nDLZSGDToZ18trDftE12W8BOo1f8KOmccKGEVvR1l1UkSHU3LTQrdjOiwHlaxallL4lcW04ronr0oIiBDAPiF-SQAYxC1rO1PyhjCVJxPBGsbmrLcxQlxw7NjSvD3i7hHswAD0hxgR4P7holnlZvpinkVQG8e4jvXWtTqQHZljTLfTNA88brZZQKA9XhDHjSvxduS3ALIqUtVcv7eyLj_NuKn4v_5i0m1YtnbnxZZ0Am12bbKhLPn7PFzjxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کت و شلوار چروک آی هیمتی در مذاکرات هم سوژه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129723" target="_blank">📅 17:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129722">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5102504900.mp4?token=FM6vqCry-CRWL8EaO2HrSSw_tajFwOxTbeKA6036SEGEKeMYSlRJZ-diHPkLPP0pefjrjkpaQIO218R2ftQV0NyNitgk1vjlRUvPYT4oMx2jVyUkTJffvoTDLCwX6ZswtqbLaDn4L6fPtxmuqOgykPWtQl2GMzaN85FgMcOVq2yJMGN_1G2GgRLan9EpwwuQM8HEPKZbZ_6PQvAWZz-GrhyT0qCuMZByeqAum6PboFO1wYwfzXF4RNRzWJP0eM_IjFe3_pTXdbW9FrD63-nCD0V_w3rDnujy6d1xRxj2yl-T7jq59iEE8arTJjAbVqgcVTAgbvrjquaPamLwLCXez3vrkuVjxvicquPFqjt3Svaf-9MY3dE1ZtwHF9ZCKvNpnaSziH55b_SJ5lSJt3Z_DQWitQfjFx9rkrt3DaUI4sPrsL5cdL1c9y5nSFYVSs7Vj1VGc60bORUuR9TzFLBvuPXAgR0wHGHUEsYTJzi0YXo7G8AHfC8iEO-_befX_AjJeN58TyvEAKf3uIHvAp_ELj8fEGkUayT1O-oElC7OB9IErsFQFGvILeJsGT3RWMGQGMafBcGrVW92HG4o94kVMge_h7W5Flcl4Q1GzQi01GCqWxHqqGUWbfjJbmFAbjoxYBjLpzn3KxMXn4Rgo64jYE6WOrJuRSAXLqFjRB9jsHk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5102504900.mp4?token=FM6vqCry-CRWL8EaO2HrSSw_tajFwOxTbeKA6036SEGEKeMYSlRJZ-diHPkLPP0pefjrjkpaQIO218R2ftQV0NyNitgk1vjlRUvPYT4oMx2jVyUkTJffvoTDLCwX6ZswtqbLaDn4L6fPtxmuqOgykPWtQl2GMzaN85FgMcOVq2yJMGN_1G2GgRLan9EpwwuQM8HEPKZbZ_6PQvAWZz-GrhyT0qCuMZByeqAum6PboFO1wYwfzXF4RNRzWJP0eM_IjFe3_pTXdbW9FrD63-nCD0V_w3rDnujy6d1xRxj2yl-T7jq59iEE8arTJjAbVqgcVTAgbvrjquaPamLwLCXez3vrkuVjxvicquPFqjt3Svaf-9MY3dE1ZtwHF9ZCKvNpnaSziH55b_SJ5lSJt3Z_DQWitQfjFx9rkrt3DaUI4sPrsL5cdL1c9y5nSFYVSs7Vj1VGc60bORUuR9TzFLBvuPXAgR0wHGHUEsYTJzi0YXo7G8AHfC8iEO-_befX_AjJeN58TyvEAKf3uIHvAp_ELj8fEGkUayT1O-oElC7OB9IErsFQFGvILeJsGT3RWMGQGMafBcGrVW92HG4o94kVMge_h7W5Flcl4Q1GzQi01GCqWxHqqGUWbfjJbmFAbjoxYBjLpzn3KxMXn4Rgo64jYE6WOrJuRSAXLqFjRB9jsHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل یک تونل زیرزمینی حزب‌الله رو در زیر روستای مجدل زون لبنان کشف کرد که حاوی سلاح، موشک، پهپاد و گودال‌های پرتاب موشک به سمت اسرائیل بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129722" target="_blank">📅 17:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwlx9fXi5eSsWz-u3j-C7tGCMItrVpyYBlkBe3K90BYhV3HPTW0ufuYfLV7gcZpJRNZwyrcRZ6vk12X8nJCxi-jqLSu0IqjSOHtUT12pSx5BItNMlxS9o2kNF9wMFaAKwhUuQEAdmUBtohoCw8gr9y0Zx-PTFih45CwUlvcOCZYXS9dGUOaDK4RIDWItrtyscvJcP9Tb8br2qizZzBwBz0F7BuKnQJVYugZOdhSus7qVZCrmnfSL_JFV6TFjkKKyMBdJMkvP_nTV4EdJ2vKZIMF_XBKSK0Kj95pJqX1KfeN8Geu3D_Yj1ZIB-otPGrusu8V6rVZwZ625DlTv0JuYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد زیادی از نفتکش‌های ایران و چین اکنون در حال صادرات نفت از ایران هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129721" target="_blank">📅 17:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129720">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aebfeb0373.mp4?token=FxlOj4YL0UjIIWjjVYpgPDyLHGLmiQOGQFG4u600iG7wfspHwIyRFWFLdW0Ppi_9Lr0SLYisYvNu6AYltNvzBqGahFL9zklDQ_LYOmA8fQGgBcsIenEpqiJIXCYc9RSV9MexpYfh3o47T_jBRtCFs58N8EGIzBhw6fJWv3XxQG1qSsvn4KVDn9FL8_Hqjq6dlx9RUOBZkvSrMMi6gQzDKboc5lU3jCPG8dem0kbgME62cuyhwfq19mtDbKb_Eqtip0XlsTU4tObVpkYS9OhM_CgfcbZFlxyO3MMCx3Qy58kJ9zSRWYKWFVaks3-AMrnrMck77M0E-0TYio5U8KvQYnKbLYZUv6qFaZQEjijhrBDfZ3Dw0N34MsO2j9CMpDL8uODSxPL9g3BNGNnOyH0NMmeK5zgvdq7IzIThUdk0MrYm1KkMexVahig_vIWLcfx43QjDJM59IjHvFLQ4xe02-82NPPd0AmgAcbr-FFYt2Qj9gbUO2hDcWYWmSeewIPDgPAoPXzWawz8C4f8OFogzX0i4AhMLnALwCn61W2wMrLObOU8KzxQPNsLv2QKOHsfBRflxGf0LkNKntqY8ILasc5xWNRhKnPUH5F21kF9qGEB5bcIA6Z73CZk1MhPBJDpOoPgLez5SCaOfmVdMY3mwnCJeA0R4FzRH1YN7r6vfHtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aebfeb0373.mp4?token=FxlOj4YL0UjIIWjjVYpgPDyLHGLmiQOGQFG4u600iG7wfspHwIyRFWFLdW0Ppi_9Lr0SLYisYvNu6AYltNvzBqGahFL9zklDQ_LYOmA8fQGgBcsIenEpqiJIXCYc9RSV9MexpYfh3o47T_jBRtCFs58N8EGIzBhw6fJWv3XxQG1qSsvn4KVDn9FL8_Hqjq6dlx9RUOBZkvSrMMi6gQzDKboc5lU3jCPG8dem0kbgME62cuyhwfq19mtDbKb_Eqtip0XlsTU4tObVpkYS9OhM_CgfcbZFlxyO3MMCx3Qy58kJ9zSRWYKWFVaks3-AMrnrMck77M0E-0TYio5U8KvQYnKbLYZUv6qFaZQEjijhrBDfZ3Dw0N34MsO2j9CMpDL8uODSxPL9g3BNGNnOyH0NMmeK5zgvdq7IzIThUdk0MrYm1KkMexVahig_vIWLcfx43QjDJM59IjHvFLQ4xe02-82NPPd0AmgAcbr-FFYt2Qj9gbUO2hDcWYWmSeewIPDgPAoPXzWawz8C4f8OFogzX0i4AhMLnALwCn61W2wMrLObOU8KzxQPNsLv2QKOHsfBRflxGf0LkNKntqY8ILasc5xWNRhKnPUH5F21kF9qGEB5bcIA6Z73CZk1MhPBJDpOoPgLez5SCaOfmVdMY3mwnCJeA0R4FzRH1YN7r6vfHtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خب تبلیغات حکومتی تموم شد/استقرار ون گشت ارشاد در خیابان‌های قم برای حجاب اجباری.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/129720" target="_blank">📅 17:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129719">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfe1hxK3x99NyQxnJyj2ZkpAZE2H76WIWbwqBAVsFgBJySXsY1NOPOThWr7ymXbvKI141UBLZlsqCdECC_yU_T-VGUaxvVEOmXz69p2wYCuGmc7I1uw1h3K4uOOT8OC2w5ur4DxJhtR8Ld2cds4Rp9-4-XhKaOAHI0o4ZnVI8nEB_7NeMZFt_-dJqchzkjBzI439ieqEhqGYqhduqcZelaK301OHEAjM4PRgr7a02HpGuJ_MzqLuQrP-anD9ZANH62D6wOhVuxX5UZXTImVjWYHHSZVPHJOEUitx82tcB13T-MZ4iUOgTny7mPrzNnCh6bD-_mnyInr0ArwoDL9pJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارجیا دارن میگن قیافه بیرو شبیه کوروش کبیره و مارو یاد اون میندازه
😂
@AloSport</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129719" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
داده‌های شرکت کپلر نشان می‌دهد که چهار فروند نفتکش حامل گاز طبیعی مایع متعلق به قطر، امروز در مسیر ورود به تنگه هرمز قرار دارند.
🔴
بر اساس گزارش رویترز، نفتکش‌های «وادی السیل»، «مکینس»، «السد» و «مسیمیر» برای نخستین‌بار از زمان آغاز جنگ در منطقه، از مسیر آبی ایران وارد این آبراه می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129718" target="_blank">📅 17:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6c5b042d.mp4?token=Uhv6p_Wsq006JuImaHtCWmMANNGjsLNG_b1q_1PGrCQbljPa4l0bNtjEdhEo_P63gYHWrczaUXyv38vTh09dcuW4HA9E3db3pacalgOqKmH4e0_uSmEqtRj01honaVXf2xbJY5oi_KjWTfdsaUu4aj44qb_3Ema54Ef12F1XoOyyEscvDH9GNa6nGAluD7YltVhYy66oLac0Wjhz29MDyRfOnkdfwRVjeJ36yez0ShdBWEcSgasga3JzOzN0KA9rRRhxDcwrhFhlIZmrfWyztIlgadMPibW7iakeQ8yLyFgJq94LDWkStf7swpolNffuIbSWeJ-3I_IE84AznyfEKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6c5b042d.mp4?token=Uhv6p_Wsq006JuImaHtCWmMANNGjsLNG_b1q_1PGrCQbljPa4l0bNtjEdhEo_P63gYHWrczaUXyv38vTh09dcuW4HA9E3db3pacalgOqKmH4e0_uSmEqtRj01honaVXf2xbJY5oi_KjWTfdsaUu4aj44qb_3Ema54Ef12F1XoOyyEscvDH9GNa6nGAluD7YltVhYy66oLac0Wjhz29MDyRfOnkdfwRVjeJ36yez0ShdBWEcSgasga3JzOzN0KA9rRRhxDcwrhFhlIZmrfWyztIlgadMPibW7iakeQ8yLyFgJq94LDWkStf7swpolNffuIbSWeJ-3I_IE84AznyfEKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح و بدون تغییر است: نیروهای ما در جنوب لبنان آزادی کامل عمل برای مقابله با هر تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل در این زمینه هیچ محدودیتی ندارد.
من پشت آنها ایستاده‌ام و کل ملت پشت آنها ایستاده‌اند.
من در موضع خود ثابت‌قدم هستم که ما تا زمانی که لازم باشد در «منطقه امنیتی» در جنوب لبنان باقی خواهیم ماند تا از ساکنان شمال و همه شهروندان دولت اسرائیل محافظت کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129717" target="_blank">📅 17:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129716">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnPA4Oa5fBfFO8L6JT6pCiV4n9bbsO8BF-YcbnaocaX6Lajdg299JwuR7177t3BXsHwlqcCjM63BRKzXqKaB4oRfZEMPSajY4wq2SvQ84WcuLYGPMHsyRk8g35_VF_6VeZpagDNzzDuRJko-Jmxco4HVX-DAyiWz-OYhDZuRF-n8tNRYSOrdhUKqxQy1e6b2NTAQX4PcTh1n1tpRaacFUHdIJG0RnVJXkoRUUTG1zYdsIgOHgDSMP5CthgciDPbRSnYCznfoRNjl_ZUal0OTCMTy2htre1AQQ20UCehl5XgNfHmFCmZ7amUTjBgK6YM1uDACPxx9DZXRpw9ZKJK7UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه داری آمریکا:
وزارت خزانه داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129716" target="_blank">📅 17:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129715">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
العربیه: وزارت خزانه‌داری آمریکا مجوز عمومی‌ای صادر کرد که اجازه می‌دهد واردات نفت خام ایران به مدت دو ماه انجام شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129715" target="_blank">📅 17:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129714">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
العربیه:
وزارت خزانه‌داری آمریکا مجوز عمومی‌ای صادر کرد که اجازه می‌دهد واردات نفت خام ایران به مدت دو ماه انجام شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129714" target="_blank">📅 16:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129713">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEh3mlb-9AYoGQBEo1WzmCdi4tkR5hDHnIReGcUK33cDBuHxR46e2zf49q-_gbySCC8aFy-3Ild-ODA7M1KdS0Gk0vS7tHgluDxPY9vcbpuu3L-1g91sN-RsSDOt3AHbyYjQTng1xnPeSM_AZ4hc0Jt7Y5rAzZIWX6TrRLhiKH9GQHRudFgzDJRTYR0U9vvfCNJjEWZIVaDUpYOJuJgbvRbZMURDdgfDLSVbhj-GlpDkNuy0ETz2nEze5PAKtYWWA2NcNEmeyKFNVa56J4iyNovcX6dkxqq-ta6mvHFIxGQ2N3QERf-cZoYm0dhEQFzx2ZVOLFD80z839t4zeH3e-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون بمباران توپخانه اسرائیل منطقه المشعع منصوری و منطقه بیوت السیاد در جنوب لبنان را هدف قرار داده است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/129713" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129712">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
مهر: تحریم‌های نفتی و پتروشیمی ایران هنوز تعلیق نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129712" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129711">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/981bb19642.mp4?token=PW6wImi3ytsoDQE0pvVVM4F_MeL0ekfKFuEtCvmnDPNAUyP4O3oAEic_jGHhRxvvqsmD85ZP2gTNp6EpboyEBD4IQxk3RXPyrhywXEG4kA7y3DzXeDwMHoHxGT4bfOvQsYXKbsi6a_Ba41I-9sPLuSx5fs1EaALWX-GbP22ZDsCb-Uc3PihalNayJbhlzpOiTHBsLmBCy5gHVaN9tMc_HHvsEx_TsP6h5Msr0s2IBl93h2qa6CDrIP2sggDfe5HjcFMHN2bPYnCqnbUstB8hwpjiBIFcmpLRyJ8ackMZKbwUL6wI3FOJ6Rl1kznbHMdSoljs4zdvckahHyUHRzQdww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/981bb19642.mp4?token=PW6wImi3ytsoDQE0pvVVM4F_MeL0ekfKFuEtCvmnDPNAUyP4O3oAEic_jGHhRxvvqsmD85ZP2gTNp6EpboyEBD4IQxk3RXPyrhywXEG4kA7y3DzXeDwMHoHxGT4bfOvQsYXKbsi6a_Ba41I-9sPLuSx5fs1EaALWX-GbP22ZDsCb-Uc3PihalNayJbhlzpOiTHBsLmBCy5gHVaN9tMc_HHvsEx_TsP6h5Msr0s2IBl93h2qa6CDrIP2sggDfe5HjcFMHN2bPYnCqnbUstB8hwpjiBIFcmpLRyJ8ackMZKbwUL6wI3FOJ6Rl1kznbHMdSoljs4zdvckahHyUHRzQdww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از عجایب ایرانی‌های خارج از کشور همین که لحظاتی قبل گل میگفتن بیشرف، بعد که گل شد خوشحالی کردن، بعد که آفساید شد هم خوشحالی کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129711" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129710">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b975a3371.mp4?token=q_JutGAwNbM5eUZjM42cArbEPW8Yg8vTQLZPXjzVnhwRmxv_1E6nCzspetP-Dxl02pWahMr4JyPtcm1x-2qFkbm_gLDGJj_0ldMqf6LSLI0jkUd1GhGpJ_3RvoK_NqipZhFRnQ-RSxtOlhgjBTq93Il8Q09WF2RyoUwlls-_5tprTO9sjC7sd4Oj8-CkhtBwKvp01tOvj_DmUPFxMAa7pdewVeQUhFkgO_5TRrV55gybl7Z0iWP2OBXvbn61TcdLrgPkhph5wMciTH9gI0FChGjjIUnLW18aBcUc6wFFkV3-YBuGjKwKQGoEg1IW8QkOCbEmVAPWhPfaMVcnTnUAdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b975a3371.mp4?token=q_JutGAwNbM5eUZjM42cArbEPW8Yg8vTQLZPXjzVnhwRmxv_1E6nCzspetP-Dxl02pWahMr4JyPtcm1x-2qFkbm_gLDGJj_0ldMqf6LSLI0jkUd1GhGpJ_3RvoK_NqipZhFRnQ-RSxtOlhgjBTq93Il8Q09WF2RyoUwlls-_5tprTO9sjC7sd4Oj8-CkhtBwKvp01tOvj_DmUPFxMAa7pdewVeQUhFkgO_5TRrV55gybl7Z0iWP2OBXvbn61TcdLrgPkhph5wMciTH9gI0FChGjjIUnLW18aBcUc6wFFkV3-YBuGjKwKQGoEg1IW8QkOCbEmVAPWhPfaMVcnTnUAdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که بلژیکی‌ها برا بیرو ساختن
@AloSport</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129710" target="_blank">📅 16:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129709">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
جی دی ونس: این توافقی نیست که ایالات متحده آن را به منطقه تحمیل کند، این توافقی است که منطقه با ناامیدی، از ایالات متحده خواسته است تا آن را اجرا کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129709" target="_blank">📅 16:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BypDjd9M-xXak6qbnF55JmvvZKkje1_3wCgUYT3DSaBhdGgaBy_kiW8JZylL1YeWxE9TFo3enIJO0lx7j4ij9Bam7jSA-YwaV1NFs49n72dp5TWuLLOf2oxAo5-VGFP7xLg08O7ANAXNDAMiIOPergGTxgLpalrmoGpYmwMYvuMW-rVOnio5KXIBlQaFip89qzERVCvl_6EUowdoKwToRf69Frx1pEHKlVOoa4TOL8n0s9LvhHS2l4De2jmLBu5D9RKJg8tp7UxqgLilybn8QKxGZdX9ajeDmC7i6V2ouSGp46kZz3n1vjXQm-262TxhwZZJquzISo7q7kPtA2y5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله ثابتی به قالیباف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129708" target="_blank">📅 16:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129707">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4efa68723.mp4?token=DOjLgj5KAK7pKaw5kqQ6lJQF2CjNzzZf8ON4qhLtjwUMFRBVS5HbXWNMHuWJ8owksmVTl7sDgvnN1tjJzudtWNMlGU7LpuIEeVqT-1-321rrLoVUUN-W625yYTa6jVr5LP7t6oEijw_SybxqhKzwdKrzs_H54zWVS9z7xm6BeIed-0rHQ-PgDfHtIgSEIDByjw1uKcoTs1cJvTP6c0j43G50aEONaB511RmK2di2GRUmdpx6Sy7_XZYs8AqaDqawTPnEPCBpPMfFEEw4vhcwhXRrB5XlK3YT9HuJKASDSGmtJ4tEdCG704PCsEJRj1cifpDvLZaj6NQ7Qmw3E2kDTKTi_Si6Nbot0LxNcMgpZJ1nfykNt2ApUM_BupK72LU0Q-F6HpIIrItwq3kDBZ2vpGz53uPde0wdRHXc4M0fKxkh1ZQVKE_b7Si9_YG8g5hvBHMTIyDjHbc7JzqcuanyhjhuhVmKQbZSqHFZaQ0iYMU2ouh7wfMeNFZmhRTO9xCFL6HfY-TwPcTFK0BrTv5WPPrkL5JgsLA8muOEowBjxRBzMV8GK7BBEEMVqaInu1B8EmmfDCpvP1IxGV9YL8o7yauxK-H6memhB4unlbsMz7OFDyefQMKwfhgEejnlth3J7w1SA4HgY7eTEUeBK9iY6OqjjrsSWAU3-urUq8eQOL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4efa68723.mp4?token=DOjLgj5KAK7pKaw5kqQ6lJQF2CjNzzZf8ON4qhLtjwUMFRBVS5HbXWNMHuWJ8owksmVTl7sDgvnN1tjJzudtWNMlGU7LpuIEeVqT-1-321rrLoVUUN-W625yYTa6jVr5LP7t6oEijw_SybxqhKzwdKrzs_H54zWVS9z7xm6BeIed-0rHQ-PgDfHtIgSEIDByjw1uKcoTs1cJvTP6c0j43G50aEONaB511RmK2di2GRUmdpx6Sy7_XZYs8AqaDqawTPnEPCBpPMfFEEw4vhcwhXRrB5XlK3YT9HuJKASDSGmtJ4tEdCG704PCsEJRj1cifpDvLZaj6NQ7Qmw3E2kDTKTi_Si6Nbot0LxNcMgpZJ1nfykNt2ApUM_BupK72LU0Q-F6HpIIrItwq3kDBZ2vpGz53uPde0wdRHXc4M0fKxkh1ZQVKE_b7Si9_YG8g5hvBHMTIyDjHbc7JzqcuanyhjhuhVmKQbZSqHFZaQ0iYMU2ouh7wfMeNFZmhRTO9xCFL6HfY-TwPcTFK0BrTv5WPPrkL5JgsLA8muOEowBjxRBzMV8GK7BBEEMVqaInu1B8EmmfDCpvP1IxGV9YL8o7yauxK-H6memhB4unlbsMz7OFDyefQMKwfhgEejnlth3J7w1SA4HgY7eTEUeBK9iY6OqjjrsSWAU3-urUq8eQOL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
همانطور که رئیس جمهور ترامپ گفته است ، گاهی اوقات این آتش بس ها به این معنی است که شما کمی کمتر شلیک می کنید.
🔴
اما ما می خواستیم اطمینان حاصل کنیم که هماهنگی مناسبی را تنظیم کرده ایم تا اگر تیراندازی رخ دهد ، اگر حزب الله به اسرائیل شلیک کند ، یا اگر اسرائیل پاسخ دهد ، یا اگر درگیری های دیگری در منطقه بوجود بیاید ، ما در واقع با یکدیگر صحبت می کنیم و می دانیم که چگونه تیراندازی را متوقف کنیم و چگونه منطقه را امن تر کنیم.
🔴
ما هم اين کار رو کرديم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129707" target="_blank">📅 16:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b2b64c80.mp4?token=vu48AiiNBnLfXK8F8aZAY3ZRgBxYpanEuG5ZIMECp5cFKh6byc7UL9uX6dK61HmQq2zolIk6Tn7lnsHdCc2koNzt2FiuFd39qkRRzYQEL1cMJuKX0P5E_9TV7OvhZMD6DEdAxzSNm2PTm2LqWBHgF1OnGV2ONJfJxmp4n2lBTX8ofdj34pVZacrHTNevWsOT_Ev1aQgKVc7vNNRxZOhmugK-cVoxVlVBe7DXgjUMJXEJaVYqiRz5RcWvzXF1GgCQJnl9tWex4u3MdOCuj5_nP3UwCl4Bu2P9xHF-0uSMenEIiCq1kqlhu2dzV_vJ-vwb2-lfoqc3eMWuyGU96f7KV72z7Hk9XOfXGo_z9FBsmgdpzIO1GxV3v5H6ISYnbmFPrtB_SUAZHNB3VzMmbRYuPgpjiSrmmugWT--d_gHTEfA_qPYC0brjNC6yI-WVgcy0LWlK_VXd76vOodbnomAl4KC5xrZck9lLIVEBbxa3_6KGPos2xedfsLzJcpsr0-wF-OrZgf-irUaV5IwXmmadDs11G8CQwDc5RV5-rm8PD96MrkMYGpNQyRuxGOFjoJuJ2TqNvv14H3MEHKZg5nSOhgUwodTUh_kC1Iao0csK3Co8-AXKACOPY1DGGpSA1Oqqc2YToBr7B7yMzOwXcDaOcK4zRImenQJe4-jqxtQEYrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b2b64c80.mp4?token=vu48AiiNBnLfXK8F8aZAY3ZRgBxYpanEuG5ZIMECp5cFKh6byc7UL9uX6dK61HmQq2zolIk6Tn7lnsHdCc2koNzt2FiuFd39qkRRzYQEL1cMJuKX0P5E_9TV7OvhZMD6DEdAxzSNm2PTm2LqWBHgF1OnGV2ONJfJxmp4n2lBTX8ofdj34pVZacrHTNevWsOT_Ev1aQgKVc7vNNRxZOhmugK-cVoxVlVBe7DXgjUMJXEJaVYqiRz5RcWvzXF1GgCQJnl9tWex4u3MdOCuj5_nP3UwCl4Bu2P9xHF-0uSMenEIiCq1kqlhu2dzV_vJ-vwb2-lfoqc3eMWuyGU96f7KV72z7Hk9XOfXGo_z9FBsmgdpzIO1GxV3v5H6ISYnbmFPrtB_SUAZHNB3VzMmbRYuPgpjiSrmmugWT--d_gHTEfA_qPYC0brjNC6yI-WVgcy0LWlK_VXd76vOodbnomAl4KC5xrZck9lLIVEBbxa3_6KGPos2xedfsLzJcpsr0-wF-OrZgf-irUaV5IwXmmadDs11G8CQwDc5RV5-rm8PD96MrkMYGpNQyRuxGOFjoJuJ2TqNvv14H3MEHKZg5nSOhgUwodTUh_kC1Iao0csK3Co8-AXKACOPY1DGGpSA1Oqqc2YToBr7B7yMzOwXcDaOcK4zRImenQJe4-jqxtQEYrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
دیروز روز خیلی خیلی خوبی بود ما پیشرفت های خوبی داشتیم.
🔴
ما دقیقا کاری رو کردیم که میخواستیم انجام بدیم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129706" target="_blank">📅 16:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc60009d0.mp4?token=tZIKOLnKAOgSSQc9zVWfKH_bfvA3I9dSJmnsqmUygIWTDR7HTYzhRTcVUmGKRSyEHazQikGh5Smdv0dCEGIh_rzwPhrj89phzdC7ui858-2ODLxFZ0MojA-Tth2W0HAR4HjY32pdrrureb3LIQn5Jc2Anii9hcRRimmBpXq6QMInKVN3uZglgMNGE8rMShB3H33jZ4nc5BQc98SN79B_WzIteskageyULdyCkG91MXT8sXnw6K0qzga2n3zcfcwoDqd-qKf90lnNsx1k13lKH_n5kaC1ubiXMhGxBqXxyISsekIVgqZki3-2ejwpq2M6SpHnGD7NWKh5eEjcT9w-Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc60009d0.mp4?token=tZIKOLnKAOgSSQc9zVWfKH_bfvA3I9dSJmnsqmUygIWTDR7HTYzhRTcVUmGKRSyEHazQikGh5Smdv0dCEGIh_rzwPhrj89phzdC7ui858-2ODLxFZ0MojA-Tth2W0HAR4HjY32pdrrureb3LIQn5Jc2Anii9hcRRimmBpXq6QMInKVN3uZglgMNGE8rMShB3H33jZ4nc5BQc98SN79B_WzIteskageyULdyCkG91MXT8sXnw6K0qzga2n3zcfcwoDqd-qKf90lnNsx1k13lKH_n5kaC1ubiXMhGxBqXxyISsekIVgqZki3-2ejwpq2M6SpHnGD7NWKh5eEjcT9w-Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فشاری شدن عوستاد خوش چشم از عادل
عوستاد خوش چشم
❌
عوستاد معکوس
✔️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129704" target="_blank">📅 15:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129703">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a16e823a.mp4?token=fs3kXAK9c9YyhyS9bmcT7WLI2_BOIOKc_-_VPOBkXwrWSvGoRXMmV6WyqoQcu16jim133X5moGuKDg1JiZ7m1v6_GuyK5cA6rz6o068UHNWiz0A2jT441rd4rP30e8wV60ysEkcAQMmm1RXqDpG5nx-kUsfMaQiKF2h7yfOLqCDaONnGDcA37cr5NLfjJ22dXoF18ZeDMGNekLbbcyEP2EiugrhjkMaJjiYieWp31DAIVeXdJYyoM3_jLF7qRTFl95X005UfIzYb-P9CwbNyCOLZcDZ0hP2o9zgG7FfUtVA9VNOoq2rK44oTT7Zq8kJY3K65Vj12KVwfu4YO_Lo-zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a16e823a.mp4?token=fs3kXAK9c9YyhyS9bmcT7WLI2_BOIOKc_-_VPOBkXwrWSvGoRXMmV6WyqoQcu16jim133X5moGuKDg1JiZ7m1v6_GuyK5cA6rz6o068UHNWiz0A2jT441rd4rP30e8wV60ysEkcAQMmm1RXqDpG5nx-kUsfMaQiKF2h7yfOLqCDaONnGDcA37cr5NLfjJ22dXoF18ZeDMGNekLbbcyEP2EiugrhjkMaJjiYieWp31DAIVeXdJYyoM3_jLF7qRTFl95X005UfIzYb-P9CwbNyCOLZcDZ0hP2o9zgG7FfUtVA9VNOoq2rK44oTT7Zq8kJY3K65Vj12KVwfu4YO_Lo-zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی : ایران از تنگه هرمز عوارض نخواهد گرفت، بعد از ۶۰ روز آمریکا از تنگه هرمز عوارض خواهد گرفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129703" target="_blank">📅 15:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ونس : من نمی‌تونم ۶۰ روز اینجا بمونم؛
برمی‌گردم آمریکا، تیم‌های فنی کار رو ادامه می‌دن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129702" target="_blank">📅 15:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129701">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
جی‌دی ونس: معامله نهایی خانه است. ما پایه را گذاشتیم. هنوز خانه را نساخته‌ایم، اما پایه‌ای موفقیت‌آمیز بنا کرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129701" target="_blank">📅 15:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129700">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af1ea714e.mp4?token=HFuqxJaG8vfB7UhGO9LU5pt3_4lEOpBruwlSFsvEmdSax0yTaLRjiaXDuMvjj6c5a67eW2Lt1ehKBuPEdfWROsUKynjDncp-f7M1nI4qXidVzGl84k-NkxBawmXSJFp0_BayL0LKIk-3wGD2fwayTbJk2rsPyCe9f9rswMB1_z-5vqEi00JSbTYurmr_pimpdfVjWPM7J1mWoTVgGg_Y99uB03pckGXiGcW4YrbjaYc0V0KTd-lHGIPKnVspw1nXtC-ddF99ueffSJ3sDC5UKOnXMbFJDHqCi0fn_0PmdIUwgUd7LEsLERDSFLJNYt0Qu6FoPXBKEuRgjUSP6c1Sow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af1ea714e.mp4?token=HFuqxJaG8vfB7UhGO9LU5pt3_4lEOpBruwlSFsvEmdSax0yTaLRjiaXDuMvjj6c5a67eW2Lt1ehKBuPEdfWROsUKynjDncp-f7M1nI4qXidVzGl84k-NkxBawmXSJFp0_BayL0LKIk-3wGD2fwayTbJk2rsPyCe9f9rswMB1_z-5vqEi00JSbTYurmr_pimpdfVjWPM7J1mWoTVgGg_Y99uB03pckGXiGcW4YrbjaYc0V0KTd-lHGIPKnVspw1nXtC-ddF99ueffSJ3sDC5UKOnXMbFJDHqCi0fn_0PmdIUwgUd7LEsLERDSFLJNYt0Qu6FoPXBKEuRgjUSP6c1Sow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل در رسانه‌های اجتماعی تهدیدهایی مبنی بر ترک جلسه وجود داشت اما آنها جلسه را ترک نکردند.
🔴
ما دیروز به ایرانی‌ها گفتیم: «وقتی شما به چیزی که ما نسل هزاره ممکن است آن را یاوه‌گویی بنامیم، می‌پردازید، نمی‌توانید انتظار داشته باشید که ترامپ پاسخ ندهد.»
🔴
وقتی آنها چیزهایی می‌گویند که حقیقت ندارد، ترامپ به آن پاسخ خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129700" target="_blank">📅 15:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129699">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
قطر: مسائلی مانند موضوع هسته‌ای میان واشنگتن و تهران در حال بررسی است
🔴
محمد بن عبدالرحمن آل ثانی نخست وزیر و وزیر خارجه قطر به الجزیره گفت که با یادداشت تفاهم میان امریکا و ایران به پایان جنگ دست یافتیم.
🔴
بن عبدالرحمن در ادامه هدف از یادداشت تفاهم میان واشنگتن و تهران را توقف جنگ و زمینه‌سازی مذاکرات اعلام کرد.
🔴
وی اظهار داشت که مسائلی مانند موضوع هسته‌ای میان واشنگتن و تهران و مسائلی دیگر مانند امنیت و تنگه هرمز، با منطقه در حال بررسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129699" target="_blank">📅 15:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129698">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
جی دی ونس: آنچه جارد و قطری‌ها و کل تیم انجام دادند، به نظر من، یک توافق کلاسیک ترامپ است.
🔴
اگر دارایی‌های ایران آزاد شود، کشاورزان آمریکایی را ثروتمندتر می‌کند و به تغذیه مردم ایران کمک خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/129698" target="_blank">📅 15:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129697">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ونس: اگر صلح در منطقه اتفاق نیفتد رئیس جمهور ترامپ همچنان گزینه‌های زیادی در اختیار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129697" target="_blank">📅 15:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129696">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
جی‌دی ونس درباره لبنان:
در ۲۴ ساعت گذشته، احتمالاً وضعیت در لبنان از هر زمان دیگری آرام‌تر بوده است.
🔴
۲۴ ساعت قبل از آن هم نسبتاً خوب بود.
🔴
البته ۷۲ ساعت قبل مقداری تیراندازی وجود داشت.
🔴
این یک روند در حال پیشرفت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129696" target="_blank">📅 15:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129695">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ونس: ایرانی‌ها با دعوت از بازرسان بین‌المللی به کشور خود موافقت کردند؛ این گامی‌بسیار مهم است
🔴
ایرانی‌ها تهدید کردند که مذاکره را ترک می‌کنند ولی نرفتند و تیم فنی آنها در حال حاضر در حال کار هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129695" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129694">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
جی دی ونس: ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم. این تنگه باز است.
🔴
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
🔴
دیروز روز خیلی خیلی خوبی بود.
🔴
ما پیشرفت خیلی خوبی داشتیم.
🔴
ما دقیقاً کاری را که می‌خواستیم انجام دهیم، انجام دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129694" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129693">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سی‌ان‌ان : اجرای تفاهم‌نامه میان تهران و واشینگتن به مسیر صحیح خود بازگشته و تنگه هرمز برای دریانوردی باز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129693" target="_blank">📅 14:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129692">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
خبرنگار العربیه: ‌جی‌دی ونس و هیئت آمریکایی همچنان در اقامتگاه بورگن‌اشتوک حضور دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129692" target="_blank">📅 14:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129691">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
المیادین: احتمالا پزشکیان فردا به پاکستان می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129691" target="_blank">📅 13:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129690">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پزشکیان: بدون وا دادن وارد مذاکرات شدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129690" target="_blank">📅 13:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129689">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f72e9e80d1.mp4?token=Fe9w2jtTprHOqkGGOd6seV_o3s49pHP-1SVq5rNovLSMJ-BfROsV8Ry4LQYGsiHpfxfdyl5vAWmSWxUs-JobB6tDj1dHYANN0pvtukvHfx7UBN_FdKgApt_V45wmuUwjnJWQBars9TcqVQNnzNKMY0ik45onniomugRZGnsKTFG3xc2zI6opl8TgQ00qLfymI-V5nRI0Pic7vXo8OxoFAdE5C7xiu1RnrsXq5rB8BQDVuywEldHaiHx1YgAv3dDdA8HfRicFe-sxql9OwOu2XYgpA8qauBCzNXJagVO44BS0mcJI3GaKyGxFd6z5OfXIyUnQmIPEI5UNGqGwzVPoag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f72e9e80d1.mp4?token=Fe9w2jtTprHOqkGGOd6seV_o3s49pHP-1SVq5rNovLSMJ-BfROsV8Ry4LQYGsiHpfxfdyl5vAWmSWxUs-JobB6tDj1dHYANN0pvtukvHfx7UBN_FdKgApt_V45wmuUwjnJWQBars9TcqVQNnzNKMY0ik45onniomugRZGnsKTFG3xc2zI6opl8TgQ00qLfymI-V5nRI0Pic7vXo8OxoFAdE5C7xiu1RnrsXq5rB8BQDVuywEldHaiHx1YgAv3dDdA8HfRicFe-sxql9OwOu2XYgpA8qauBCzNXJagVO44BS0mcJI3GaKyGxFd6z5OfXIyUnQmIPEI5UNGqGwzVPoag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از بازسازی پل B-1 کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/129689" target="_blank">📅 13:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129688">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
شهباز شریف نخست‌وزیر پاکستان: نخستین نشست کمیته عالی‌رتبه در چارچوب یادداشت تفاهم با موفقیت به پایان رسید
🔴
گفت‌وگوها منجر به پیشرفت‌هایی از جمله توافق بر سر یک نقشه راه برای دستیابی به توافقی نهایی ظرف ۶۰ روز شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129688" target="_blank">📅 13:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129687">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مرکز آمار ایران: رشد اقتصادی ایران به ۰.۲ درصد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/129687" target="_blank">📅 13:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129686">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
🔴
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
🔴
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
🔴
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/129686" target="_blank">📅 13:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129685">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پیامرسان «ایتا» دقایقی پیش از دسترس خارج شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/129685" target="_blank">📅 13:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129684">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
توانیر : در تابستان خاموشی خواهیم داشت/ محدودیت تأمین برق در بخش‌های کشاورزی، خانگی و تجاری در بهار امسال نسبت به سال گذشته ۶۸ درصد کاهش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/129684" target="_blank">📅 13:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129683">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
تسنیم به نقل از منبع نزدیک به تیم مذاکراتی: ایران بازگشایی تنگه هرمز و مذاکرات آتی را منوط به اجرای بند‌هایی درباره لبنان و ایران، صدور اسقاطیه‌های تحریم نفت و شروع آزادسازی اموال می‌داند
🔴
تا بند ۱۳ با اولویت ماده یک درباره لبنان اجرا نشود، ایران تعهدات خود را بازگشت پذیر می‌داند و مذاکرات هسته‌ای آغاز نمی‌شود
🔴
هیچ مذاکره‌ای با رافائل گروسی، مدیر کل آژانس بین‌المللی انرژی اتمی صورت نگرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/129683" target="_blank">📅 12:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129682">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppwGICnXbR8RC-xTazPF6y1IsLI3xyRHsjFs84ZdjuH1UHRy8X7CGTK7QkABjXlndgQvdMoNfQ6qUeXlBZ9CDt2T_tl-Ir4mrYmCZSBqllqX1aknErEUBQ8dC_EFD0kmiHTRInhN8H4uLvJP8VQBer41XYqwJBNAtB0wM88XEgPNsyQIjJxLOFC7sS3YjK8DQlZYF8L7vMH-qu7A6Ymx374fzJE20jAtF8qAQvnBh0bTYmGnXbcqXsZSEmrWPTfBHsYSbZgyIqUjwQS5_0YI04RbDcHGDpZNaI_KIPwI5TVzVSCj0H_y5iUR2AZSe63BL1m2Hxzy8YXjvL-s-dNt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی :یا مجلس رو باز میکنید یا اونجا رو به توپ‌ میبندیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/129682" target="_blank">📅 12:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ایتا از دسترس خارج شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129681" target="_blank">📅 12:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129673">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXwM3ujaTpRFRGmBGEFdwgNp52neT7KNebILdih-Fr-wJkTiuzwTzCZ-aEDZ9NzrZhK_Vu8YhhN9BUrPATa8AE5T4enMtb0WQyK5t-mzCHT7KSphZTLfPFGN8eRSl8qUdsijKW5VbDiCyiyOfN1XH_9HEBzi6CKLdDd7NJx_bRuquY06lTBK5UeTTNaT569ucPA7chKhSviOdrHHh_2E_NQRnfDn4tdl8ebg4GujUaAFE5BNHDstJnyCk0cu64CL8S5xKTTHdLPuxNMkgC8jPhXPS2wA-VlnRt5B8hAxjZY-1djVxiJeNz-4xCD9YdRb_9A0V6ENeLrDn2y5XrJ9-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfUwmtLY5RS7lyqW6AgbtUN1eagGfKtF8jSyEFcmITesUetxJ8s4UjBrekMxAIHKR3Xz4XlT652CLqcCWJq3ayftoMTHJwRW6rM-lDUuvMJ_C6nX_P4JOaBxkGaR4dAdGMYYvBqrn0e7HUbtn4KS0sPf4YRGTbr6nCELZnZvi7cwoxkcYUbGR8h5i6-_SHGWm4pf4ARgKp1PhAZm7QzGaOWeywzf18QzGnPPZfV4ydP_yfm5K9DV4153OUynqD98nYvV-mgd6MypDIloYDFgZZhlJM3p1OPQrMnHlIFB1YAp8G3lCsUVdwGdfCee4T7BCFtj3ZTL_7bsS9xLqUDeTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HV6E9PQDAbp7OGvhdiS1SkSGcNct6jnGQH_M4e0tNzHP44XF2AgWx2x8e66-M4TFLyiKYvpTZgi5hLuXdJwyl2TRU1qdEl7vzMtEsawF_Qr6nQ0WP0AkvjpWAFVmXOiNwTuATPOyVoWcmEtNPw3KHmsEUJsyS4c06Hk9zAgKGk9W8vhUsb9ah4iEpfnggRxKaKu0xR3A5dMCZxWqvMPTXKprNe_X0n5kbPctDCNNIjLIXQu1UybP0u094q4OxGQ7fNX3SKUecYgCG2kVMdxT0jLicHIajTw3AmhhuL_LqfXh-eYUoK7lSLF-8m_ecuMi1rH1NFB92CwsfgOS8hTJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZV6MP6V4NkoppjGQ5rZHMgsXCODmaSy1fELOe4cjwnopG_a7BHN9Xq7EawwMk3ZZlbTMJHGwebbKycBNByM3d1ZmIkz8E6fQD8CLZ6S2j_dZk_Jt472v0_2HbzOP95iKgPiRSDTwI2xInmVbvxMChFUCT3_qChzJ9DtrJ_Wht33_Jy6V5B2xC1iqc5LXK63U5OGzEjyY6kwsA3qwAVLA-W4kNpvA6CL43-zOBdf9AUGsCHjMh6SH4jThlCb2zDhQCO933XVD1yR8mSD5n_oZ-aex_XtyqGsnqDMcNjNFYMuzJ946OZpIxxTQCjL031RMIwUvfBMpB6cQDbMhEx89-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DsYPzcvx--k9HfBTBxnZAZr4fttR7wnNvs1nIvw1ZO1ZrBaaT-nn6jzTbP-7JbmN-wrP14hfpItHPW4_4xVLl3R5o5PdHTRAqK7T6W0kWbBhutQxMpxnTZVvGEhvZ4jnDvmKQSlroKpj5xVCzw60yncNk3ichGWIUyjq-iDi4K0JuBVmXmyF-4xycZ10w8yroR_98prGO722NWZ5hloltFMJ-4gLySjUsdylepzYo0D04-Uq1lrnhVrrbYFVzOiRRqrqzmaQmubqToH2SQsbxoBgUdGrszvohbvgsuCdpFvx3kngt0TS7-J0yrqEPTqzOpziRtIDgkTmfqDCGaN4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODU25yKivjvAlhwa6zSoC3vbhghkF1L8MyNf2s5NJOSwfl9TdvG9l7S7kohuMs7W8sE59BBckIcfU9CPUhR3j_tZrI-4jfJrkLOpCEwm_O5rAIsjB0UjUB4--ngZmhobNX7H9-m5MENsTlc33QQFW2ULeLb27_HRCTZfceLZ2waqBCByH4AHuuBjic_Mm8avxUfGpnbujChtPIRmS6zJgZwJO8jLU7twvZWz1tW0lHvSOnNqFfMRHY0fBuqWqtMCKtMj7GeqP3R9hB4mk6kUZfjWmI4A4y8Sq6U2yX4dqW7nM_BdWBVPLmriE0ZhY25UVZdiUB3myp_OXfVtQddhyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e7d85b4c4.mp4?token=YxhU2EoKQzPHXA-DItg0tW138O3Jz0AO9asncTkO6ywguAZ3GfZfk4IVY62g81WN_OMgleFqHLKCKl4CE-4bVBPLwNBc3D40FWFWQNgXNikp1FXKnnK-R9joe7PbJgtiXgd5cQ6LyqH5M1YO8k08HqNTXboh5gPBqFtERXx_NaMf5YWBmmUfzbJqoEaMAiYr73pz2ZMnkITbeNwqnDmwoR3jzbYGxPW7fmRU0MQYpg-fT9hiyO0Gd2PzX-Pktu9n8-DgJORVrMsaoE6umQSwIS5ngmYpDIGtEtBDLKeTu3O_dJxuw6IeRnnJuh9aDdm-PyNUiX5smOlbKNKKXPFgYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e7d85b4c4.mp4?token=YxhU2EoKQzPHXA-DItg0tW138O3Jz0AO9asncTkO6ywguAZ3GfZfk4IVY62g81WN_OMgleFqHLKCKl4CE-4bVBPLwNBc3D40FWFWQNgXNikp1FXKnnK-R9joe7PbJgtiXgd5cQ6LyqH5M1YO8k08HqNTXboh5gPBqFtERXx_NaMf5YWBmmUfzbJqoEaMAiYr73pz2ZMnkITbeNwqnDmwoR3jzbYGxPW7fmRU0MQYpg-fT9hiyO0Gd2PzX-Pktu9n8-DgJORVrMsaoE6umQSwIS5ngmYpDIGtEtBDLKeTu3O_dJxuw6IeRnnJuh9aDdm-PyNUiX5smOlbKNKKXPFgYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از تجمع امروز دانش آموزا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/129673" target="_blank">📅 12:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129670">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krBHTo-t5BkdwSIpIx0cmvvfM5MWaoGyudmBSdTMOSXXMJnz-toNXkEvWQ0xaSvHZGCFhpwM3IXPfjcxPpHWONfAEn7MfcYAI0D7I4aE85Bh3EzgmD28YUQF2CFdAXjOOLw6uZZV7vFjE9Sjon-4Ov3Z0xIh9447qyWjqtcGa6BO3NeW-FcyquifU-w8CXDzbcN3mmUxNzDscAGNO3yMDZY-8398ot3-BS7x4ZXaErEooBkiqE4b-gu2sQrfuJSK3S14b1h5svwxyF17I0oQhfbnbLit2Af0m-MSrEcm-bdN0L9SKN3VM3WLQ1rtVDaY5jhSlXhzuj7fHWg9AISNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2759594a5f.mp4?token=n27pU8ETUUGyb5SOO6DfUHvLskXaDa68GJZSU3zmZJMBvktIx2MNKfFN4Wn0Exkc1h5p9g51G-mIqmmOYccLqzrJs_WLBQG0bBYLrcy5Rmwq0do8k2sMlXEoqbK7LGwm4KJYZtCAasuZDq8zztA6R3kUn5b5PL8szmDzS0bbOp5I92ImICM6Cj9NbsGqoRDknPLQBDDPXEnVKFs-wNR6aTI6_miE1Ca5D12nqU53J74euSQUZd6RZWt_fyHEhsl_i34R4ZJBTe5pMBkH-MmNtG9CNjsg3QU6aSyTMMD8RnjINdJ69mXDjrBB6vaMRaZWzY3urHs97nUHAqI-Cd-u9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2759594a5f.mp4?token=n27pU8ETUUGyb5SOO6DfUHvLskXaDa68GJZSU3zmZJMBvktIx2MNKfFN4Wn0Exkc1h5p9g51G-mIqmmOYccLqzrJs_WLBQG0bBYLrcy5Rmwq0do8k2sMlXEoqbK7LGwm4KJYZtCAasuZDq8zztA6R3kUn5b5PL8szmDzS0bbOp5I92ImICM6Cj9NbsGqoRDknPLQBDDPXEnVKFs-wNR6aTI6_miE1Ca5D12nqU53J74euSQUZd6RZWt_fyHEhsl_i34R4ZJBTe5pMBkH-MmNtG9CNjsg3QU6aSyTMMD8RnjINdJ69mXDjrBB6vaMRaZWzY3urHs97nUHAqI-Cd-u9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دانش آموزا امروزم تجمع داشتن و تونستن خسروپناه رو تک گیر بیارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129670" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129669">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DD1qrsmjmWzrYpX4W9UwIPy56QXx3f10HBLJpXckWBkDw72Y8o-1ujeaq_6rTRQ--W_hvaHR4bhIuIRP94ycNfuacKuT3WU-jvUFr_fO2mqs8WYOvVIX-6T-zL2KU0ZPCPGYmYfYqc30wLErzHmVtRZWmlTkFDG6aQKm8sjKXQhxinJVUwNEisg6NmARcl9QcdIr3THejXn--OAkJRt4JaymxnEXSZwNH48hahglTt81HAlETygH4PFjxtmRi-2vx9LcRWDjlNBTdjNYbufC_hH1sa4qK5DGnvcjhd-YYsj2HMP7SQnbpEtC4bg2MEZ9CShGrDq6KCH7gvWk5QJBdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عباس عراقچی: میانجی‌گری خستگی‌ناپذیر پاکستان و قطر، پیشرفت قابل‌توجهی برای پایان جنگ لبنان به ارمغان آورده است.
🔴
محدودیت‌های صادراتی نفت و محصولات پتروشیمی برداشته شد، محاصره لغو گردید، بخشی از دارایی‌های مسدودشده آزاد شد و طرح بزرگ بازسازی و توسعه برای ایران نیز آغاز گردید
🔴
اولین آزمون: ساز و کار هماهنگی و کاهش تنش در لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129669" target="_blank">📅 12:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129668">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd3MIBZY6tXNwecHNHB6uvGtMrwnOZvy5Ou9tagx-QOe1lCp2unJUozI5ur58WomBgZQABhbPnG2FSy2oLZd2IhUTfE79oJf1JtsOd2R76WY8pvufnGECo9iVUmbm6C7QU0jXFM0bsHwbkbooDtLy3KWNS515bn2F8Co_dQjada98dWiGF44Hq81isP5vEhg838h316CqHKagTInevB4oOH0Iz06RqRD7MYfQI43fpbMq6LnM5hHghA7ta3dfvwOv7Z18TN-6LJqVRHIBNxUFTv7G4EzXlMt8G0MaGla4w1SMppjwMxWNxYxoLbWfr7oI21L3e2tvRHUloRJDjOrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: یادداشت تفاهمی بین ایران و قطر در مورد اجرای آزادسازی دارایی‌های مسدود شده ایران امضا شد.
🔴
وزارت خزانه‌داری ایالات متحده (OFAC) معافیت‌هایی را برای نفت و پتروشیمی به مدت ۶۰ روز صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/129668" target="_blank">📅 12:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129667">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcY4pd_GfF9oEBHeLK4U9h681Q-RILkjIKsVjgMG-V3fNcqO5rkflRCuB2hdP-J5mRbP-LTuvheoS83FAlaMfCljXPjqEKXO3HapW_Z967D3KVsMa0F0PnO84aMReoGYIU9V5NFJSKQrOrlThjg-UN5fsxyiu6YUyj1wTCoEQ0hgBPn73DfdbwpCrcoo53riKZ1KgITqx84z239jO8Wtl65zAcNHvs9Gwh-LT0B6cfJSAK96EEgISCIu2KjSbmX8gK67hqcH7wgHRa7C7iHnLT0m5MKvPa9uerFQ-He2mIARl5ZHagRja1U9uRS8RkqMSwtZmwqBwbPfoSH_G12oJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای هیات ایران همین اکنون از باند فرودگاه زوریخ تیک آف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129667" target="_blank">📅 12:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129666">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
مذاکرات فنی ایران و آمریکا در مورد سازوکارهای اجرای یادداشت تفاهم اسلام آباد و تشکیل گروه‌های فنی مربوطه از امروز (دوشنبه) در سوئیس به ریاست غریب‌‌آبادی برگزار می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129666" target="_blank">📅 12:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129665">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
عارف، معاون اول پزشکیان: ما برادر بزرگ کشورهای منطقه هستیم؛ برادر بزرگ، هوای برادرهای کوچک رو خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129665" target="_blank">📅 12:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129664">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6112aecb98.mp4?token=h8NQO-MFcOEv98yQtq62Z_3U4yY6HbE-Bf3_tXB6vEHbSUKT8yoC3lNkcI0_z-kS9BChNLzxV4J-T2QiTbsMrJo-mQ3j33nPp960Cv18NC9OWHL8UyCtDAFLZN5izamXhhnfhMfvFYaAjuUynIkr6A9bYtUZmLXVDWdQ_FkRWhBo74pD88V6VkySQOV9pMu05hyC4iqnSlauiT4fM4VQVOZEE6IfRHqbirhaTT988NeUzWTbNNdI5UovJErKPDEQJfRpJ6nTuF6JR-5UVuFeMtrkmnQhKe4EpyIswi46vPJt9r4aKad2iWr55yGdw7PnSrhCDHEbfN_0Mem8WDMDLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6112aecb98.mp4?token=h8NQO-MFcOEv98yQtq62Z_3U4yY6HbE-Bf3_tXB6vEHbSUKT8yoC3lNkcI0_z-kS9BChNLzxV4J-T2QiTbsMrJo-mQ3j33nPp960Cv18NC9OWHL8UyCtDAFLZN5izamXhhnfhMfvFYaAjuUynIkr6A9bYtUZmLXVDWdQ_FkRWhBo74pD88V6VkySQOV9pMu05hyC4iqnSlauiT4fM4VQVOZEE6IfRHqbirhaTT988NeUzWTbNNdI5UovJErKPDEQJfRpJ6nTuF6JR-5UVuFeMtrkmnQhKe4EpyIswi46vPJt9r4aKad2iWr55yGdw7PnSrhCDHEbfN_0Mem8WDMDLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون حمله هوایی ارتش اسرائیل به یک خودرو در شهر غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129664" target="_blank">📅 12:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129663">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkw_HDGK6UkXtL9Ame3CIdl_XqH6whW1Bgf_AgAYKP9h5MTMS22qRASBh_iWkDG8zkV9IXaN5jAIOihe0QSmsi-wUFufAJQwbK8LWEVzjfYqNVX3OFAjcTRKn9tHMNAwKDrEMqLwGDhIjp2aopCUlzmHZTyM4brHEzlkMV1FBh4kwmukFBl9As3P9Z6k-R8VkKiG-iOBF_x9RidzJGHa8S2-y50uffSa7QccmGxilu7Tb24FlbZtXvFMFPlnU9GlDzd7h_h830viVqut_gw0Hec54QVxocXvlVf6VyBW6WKyBA6TDRG1b24AWa1i4jfHH7mF84DYDlQZPWGEenZKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط کِیر استعفا داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129663" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129662">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITkl-P8eLfF6Fn8BLoCWnRRjs8whij40fDO3BOk2N3N8DFyWDBlgqh6NaBYKYlImXjuP5MsufuAeLoiR29hXf3mbvBVP5eAGlwKW2vp0_kJl3I7ANqwSEVDQlrSh7C4oFF7GVlUUGus4cCoas2WfPZrbylEeI1l7a6AlxMqrlID1dSDLjtl-QNvjFjlGOpqu85ux8ZKc_aoF76_78YWJfhMvkE3Z71pBp2Dg4-hnn3dl0V3T0e_8KvIsuXuedkHy4ZNDl7YdiM5zkHq8Cl7FvP9tb7tSCvslNK28t_1Z887Wo24IRc7Mc9lpr44Whw2FSJCPnt3czNhsM9n-5rbc8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: یادداشت تفاهمی بین ایران و قطر در مورد اجرای آزادسازی دارایی‌های مسدود شده ایران امضا شد.
🔴
وزارت خزانه‌داری ایالات متحده (OFAC) معافیت‌هایی را برای نفت و پتروشیمی به مدت ۶۰ روز صادر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/129662" target="_blank">📅 12:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129661">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر اقتصاد: آزادسازی پول های بلوکه شده آغاز شده و بانک مرکزی اقدامات لازم رو برای دریافت پول فراهم کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129661" target="_blank">📅 11:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129660">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVU1udDGBCU49PQsno4KAHKkqpKjL79ay1VXCYUX6fRzT0Kg080xxgzK8spFBEONWZXablidty6wdwm4zDNJR_UDVt4Kc1ifTGw9T2CgVX9hEK1ntGJvihRg787af_zB8rSm4ZazlIbC3XRIPRfZZponUY5BPKQQcoQANBFNbO4sFMxqjZ_2146Cq65MMes1BRjALqDB0h0AYVzoH1uIRb8WHii8ATDEprvoLPwI1rbXpYSEMAdSWIvoCMpM3W7DD1sFQkEVpTiaB1tfsEn8DcmaYWQhSVoCJthmuvMMCFxJ6gwvcdp5pe_xwK3oVMqMidKP50rGGGD6YJBlXCbOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
چشمم آب نمیخوره که توافق انجام بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/129660" target="_blank">📅 11:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129659">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر خارجه ترکیه درباره مذاکرات ایران و آمریکا: دو مسئله وجود دارد؛ اول، ممکن است که حل فوری جزئیات فنی آسان نباشد و گاهی شاهد بن‌بست باشیم، باید برای این امر آماده بود
🔴
دوم، همیشه اسرائیل در کمین است تا به محض یافتن فرصتی، در مسائل کارشکنی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/129659" target="_blank">📅 11:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129658">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
هیئت ایران محل مذاکرات سوئیس را به مقصد تهران ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/129658" target="_blank">📅 11:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129657">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خضریان، نماینده مجلس: در توافق با آمریکا تثبیت نیروهای مسلح این کشور(آمریکا) در منطقه را پذیرفته‌ایم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/129657" target="_blank">📅 10:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129656">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NS2cezWbGvWB3xmcYQrpVa_f6hAsuvNofN4zyIxz_oKK_LWvInlBoJsncUyfkW2G7n6o1c91WArBO0LtAL9_z6UTdsNXkKcCoGyYroCA-K8DtoK0XBoF2pUx1mUzW9nmDE2DFSasw8ncYZgxqc6uVrzYSevy8ozNPvWDKoxDNZtVlHvwXO-PdI5vutBSZb_Zxhko1tHDCRJqxbKqzFJ0UqNEgOlblFWaSgULB_SfkjWjc08i1cNdO3HTIRJCmuKLcgbEPQNafg-C2UDKxz8cdhPTf6-72W1WdQhVaMCDuAvWVVqnFbuZo6DGy2IQ9oytG2GYti339ZathsN2Uua0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس: عراقچی نوشت ایران معافیت‌هایی برای صادرات نفت و محصولات پتروشیمی دریافت کرده و برخی از دارایی‌های مسدود شده آزاد شده‌اند.
🔴
مقامات آمریکایی این موضوع را تأیید نکرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/129656" target="_blank">📅 10:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129655">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
هیئت‌های پاکستانی و قطری اعلام کردند که مذاکرات آمریکا و ایران در سوئیس طی شب گذشته «پیشرفت‌های امیدوارکننده‌ای» داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129655" target="_blank">📅 10:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129654">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBUam4lxAVXeJh93rOIukSj6MJCGHXkZtRG1OkKdVRLm4El3Of_LRdJVL7P15AaQ9qpzx16MECUjfUB3G_EMCBrORLVGe1oTM1WBi1akbuAh8eHQRKqLEMQEy9tnno7sZd-1ui4kgqED-levYz2ILFeThPhv4uzbvfQHe45yjZKFwAMtDkLdpw_IEfcYbjO_cJ8_VYBr4F2OFZ1pk-_hDiZM-NW2lNWd9zVExKtZWwlUe722gb0z4H-muhfWk_Ky9mO74ViSmiFtq59FawwsFCB_FHJ3ZOPoBGpKVxer_dpaGheJ97Utop6yn7Klzr-0wADWCZYVjMgWB3FJLFA93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس:شما تهدید می‌کنید؛ ما اقدام می‌کنیم
🔴
تنگه هرمز نه کازینوی شخصی شماست و نه حیاط خلوت دزدان دریایی مدرن؛ این‌ها آب‌های حاکمیتی ایران است و تصمیم نهایی با مردم شریف ایران و نیروهای مسلح شجاع آن است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/129654" target="_blank">📅 10:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129653">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزیر دفاع آلمان: در نهایت، دونالد ترامپ مشکل بشته شدن تنگه هرمز را ایجاد کرد، نه ما، اما ما در بازکردن دوباره آن ذینفع هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/129653" target="_blank">📅 10:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129652">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmiTaBekHfI61mLs_CRHhU2SuRYKTwvg1_qQm183PmGljypaZJDgbN2F0UWcN7rzFagTNmr8NczFic7mZh6QNpdGFWtQTMIdFh7ewhkX2c2WgQrNZeaT_JZYxDql8zI-jH6Bp7l5A3-ldOgI9cWwMLZ_hq5Ap2qgULAUZH9foN6wrp_yCZ4lc-CW73R5mumxO7WDLD7u-fNB52MRDEk8pZy5FL0P6IBJkX6kvoyDCHTKnf4_Vzi8HbElc1mAuKTgtOY4EqY2GDee4fmelXhi241rIGZs5UHWoZON_FOqtwai2TIWagqoawEf7zz4PKA1Q0EiUolEMpywmiggbA-nNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از مذاکره نخست‌وزیر قطر و ونس معاون رئیس جمهور امریکا در حضور جراد کوشنر داماد و فرستاده ترامپ در حاشیه مذاکرات سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/129652" target="_blank">📅 10:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129651">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">️
👈
وزیر دفاع آلمان:
ترامپ مقصر بسته شدن تنگه هرمز است
🔴
وزیر دفاع آلمان اعلام کرد که رئیس جمهور آمریکا مسئول بسته شدن تنگه هرمز و باز شدن این تنگه در راستای منافع اروپا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/129651" target="_blank">📅 09:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129650">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
تانکر ترکرز:
ایران از پانزدهم ژوئن سال ۲۰۲۶، بالغ بر ۳۶ میلیون بشکه نفت خام صادر کرده است همچنین معادل همین میزان  به صورت محموله‌های شناور در نفتکش‌های مستقر در آب‌های سرزمینی ایران ذخیره شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/129650" target="_blank">📅 09:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129649">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Enw7jiXRIefbMKE6SZUdHLUtAh7f_HNQyM2JksslwQHWvzsvsc1CtOLm3WYRVpypGL2glIhuBinF2uDMVzfeqjALuCEEJCS_SdPeQer6zpspT3jXxuqe_3BuOn0KMLxx0gbVIvY3bICVD0EqkBplhxXuLQkRcrALSCNKrNLFHp3KXls3ywZwnnR4kY4vMYjmoStefFrnUNu_2Ncn6q727t_l_zkvMvjx-bgRlrWMXFNnh2w9d4rEMU4FBG1iHS3Q91CqnKa9dG6WO3bmHbs-51w0PlhU73aFudrIiaBwc8aAecqAC-4o0T2W82iNiLtkVCXBp3EAbJwqqhs7u1UbiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سدهای کشور چقدر آب دارند؟
🔴
بر اساس آخرین آمار از وضعیت مخازن سدهای مهم کشور، میزان پرشدگی سدهای مهم کشور تا ۳۰ خردادماه، ۶۶ درصد است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/129649" target="_blank">📅 09:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129648">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
اولین تصاویر از دوحه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/129648" target="_blank">📅 08:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129647">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
شهباز شریف: امیدواریم مذاکرات به سندی منجر شود که صلح و رفاه جهانی را تقویت کند
نخست‌وزیر پاکستان:
🔴
انتظار دارم مذاکرات جاری در سوئیس به میانجیگری اسلام‌آباد و دوحه برای پایان دادن به جنگ آمریکا و ایران، به «نتایج بسیار سازنده‌ای» منتهی شود.
🔴
امیدواریم وقتی به خانه‌هایمان برگردیم، سند فوق‌العاده‌ای در دست داشته باشیم که صلح، پیشرفت و رفاه را در سراسر جهان ارتقا دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/129647" target="_blank">📅 08:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129646">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
بقائی: اظهارنظر تهدیدامیز امریکا باعث شد ایران حاضر به ادامه نشست چهارجانبه نباشد
🔴
در زمان نشست چهارجانبه اظهارنظر تهدیدامیز امریکا منتشر شد که باعث شد ایران اعلام بکند در چنین شرایطی حاضر به ادامه نشست چهارجانبه نیست.
🔴
قطر و پاکستان تلاش کردند گفتگوها ادامه پیدا کند و ما گفتیم به صورت چهارجانبه نخواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/129646" target="_blank">📅 08:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129645">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnNqVmzz5SzgD205dC1rCGzhnv7JqAYWoMWP4LyWgJjIae4yyx0941_nW17Jxaexr-YpcOiR0LZweQO8QdmCPCWWdOdNT8jCGurETXaWBhrKJUzHKhR-HELLAhUYODSoISoh-rT-KjXwfKhuQ7mTH0ieAprlqy7aXzDf5Pi-mABx008m9FLT9GooIXG3qrq9eSnbqBSB8bzHlMnJdWovciBJCLny2qh3Aa8i11LGUIS4TUlCf2Z1Rgq4OSw4xvxmI_sx3vKe8CZBUlDqr1j-LWhN81dVWm2yTTBFAy1LN4ctkJ2Q1g3IOVg0-Ac2ItdIgEG70cPpg372Jj8qN45z2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی:
ایالات متحده، بر اساس تفاهم خود با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تحریک‌آمیز رژیم صهیونیستی در لبنان است و باید پاسخگو باشد.
در صورت تهدید علیه ایران، ما آمریکایی‌ها را مسئول خواهیم دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/129645" target="_blank">📅 01:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129644">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLVYmujhH_TpUtMlu9kEBOZLeqZQN1DD83xw4xCfYuz63OmqoFDCjkE4cD9yeidGpGEBfd_rGEp2K5gfgtf86ViwQsQ0RU_BDmXSREDQab8eHpYliufMM_FDeo-d5MMwT5RxflXyTm0LRwRysLwyZmC3y1NACV94ZBRGMYh4yaeyPNu4WtevEOgUAY0wzsl_OU0k8Glzwn0QaUarra4C2E8csj8QGrEFiqyKuLiE3tPO7GJa5PHwNIPSAbQ18Nkf4vaYoXpdLBStmlmyL-mvbsec7QMc0K6XcmsRfCOHFg0xbcleOr0kcFnQpYre-N-76AyEzUnZu2O0Ql_40TNr1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جای اینا تو جام جهانی خالی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/129644" target="_blank">📅 01:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129643">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEk3cAp8FaLaux8yA1kCUsd4_86dH-j0UOvnpMyI-baS0idCnuyPZTIYsQimxpNWBsaaxXS7zQhQPvHaWRRMlQSnVsI1ydpnDQKiP4HLYI8ZCyMPc5tRryeX5pAqGBd_sHnLCR7-3l8i8CTHqujpTfICCYG1I5vSgLQJ9Jvwsa6-dv63gp9l14DKEC7kJQTO58869Mo8D5ESB46nptYYt4ZQzZh9PBjnihRWsH8PEnQyaYHnVSVZjWT0g1TgqKTGRD5jyKQ7dThIXfeschC9XsyaZCihEveC_Q3GGrf4EG91Hm7C75VTzHg1_WMOKUzpj6ulf7njFLTfOMiYOTEd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : نیویورک تایمز نوشته بعد از نزدیک چهار ماه جنگ، تقریباً هیچ چیز عوض نشده
جدی؟!
🔴
ارتششون عملاً از کار افتاده، نیروی دریایی و هواییشون نابود شده، موشک‌ها و پهپادهاشون و توان تولیدشون تقریباً از بین رفته
🔴
رده‌های بالای رهبریشون حذف شدن، تورم سر به فلک کشیده
🔴
اقتصادشون به هم ریخته، سربازهاشون حقوق نمی‌گیرن، تنگه هرمز بازه، نفت همچنان داره جریان داره
🔴
و بازار کار و بورس آمریکا رکورد زده.
ایناست که عوض شده؛ و تازه این فقط بخشی از ماجراست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/129643" target="_blank">📅 01:04 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
