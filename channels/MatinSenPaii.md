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
<img src="https://cdn1.telesco.pe/file/pINAfCe3NJcSmRidlr5iBT3tJ1zi0E-RB9SCQRQcITzTzddPoDh1ZRodv_RQR_dnrH84ZqnBZpd7BVEoa-Qpewjtv6Uhdcpt27jgHlEN1a_5a2Hcm9r_1aZbLl-4sGybDO0h1rXNeu2kWJ2tKkV1ngMIuMrzk_Az7MO-obVLQhH68S2XKOVMohSSN1TlI4XTIThcbFJ7Zj-2d40-rsJwP18PMFQ0OSVCkkCnn1mc8A9tSR88UZaTOmSnF7Gf3RRpLw8CNXpBJ4c4YfoSOasz7tBaZHQzkcyjN8e3nWVGpkziRsBiPxoLVPzLF5widU6nWD8A_GGYFvHl69oT0G8M3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ces-zIFM96dYAVVTSL8zgZkiWc7_w8RiYLQNiJzCGS9kp6vEF1d-4vTBSh4zdPr510zGCe0WouI92cCM6WLhwZSGuUCBZFZ9n3aQyWBUDXwbAnq8EydJBTrMbEgQNT8DPh95jYC9uZz6MdRxSC5KQeQC0ExS8RigxA3zb1_MfrHdA1N3u2vjyRbnyzXzmPKS3m3vmpUHubiIXpfS7Qr6CLTcFUXAn8uLc6GYjyeI6XXolitub44LQwww5dNgUCrBf4yDq_sF8fIlYbUa3y6YFy_ETcwEFUgDIGhnT9Qbnqw0N8x22LW_s-O04Dvw0gAFLY6b_C-gSb8Z3yZTE8KaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q0gQXJ4_B7GMl-DZMp9nHhhuOrSRCEdzgj-As4wHP43GpO2WaczHcdjhwGhXrfkrn9-8LmXnlUtaIvNhw-7KsmMLFpAO-IqAT8oKUiWRc2UFZyk27vuy_LftcCCK1IrZ4qf0cfe1HUr73HX64iBQf890jucBeAvwSZyH9Tl47I6L7nNB9XxSxAE6wZ52gSaZiPwDniEYu7nweTqBu2GrEuQgfP_m9NgDbjlb1ghyPZ72PVhiG-u4TKX5oqgzOEjuuDEn-vrk1jgPKoU_YrDOJFtPlnO2Yl87Pfnk7t9eQ3XPRj9_IRxHiWb3PkncEfnKyAh_ZSVSHdy1NbaQPKHWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ReyvfLWhJaeba2mHVQzubRMYPa8xTwDHSQMU2dWmWR0AKr696CswvfSJ65XIB537bAZUJ5KDe2Jl1AvIqLYuSDFlCZpqPxF343gw696ulzq_IaIeX8I39UlHIcQqrfPBMYufz378HDtoS918DFyLIrdA7o3B4P-mE7xN_51-XkOlUKKB-3yW_Jmmk3eGC5JZujE3QpSKKhZrt2Im9KmRjgST3L7kMmv8hKcGp0ozM9EV4UY9RD85x0UaUp41sy_h9fBjXwfM6u28Urj3d8_mEnTHiovWssSWOfotSTEZhuoRX3yBDpkvbVEVM1Cxr3d9B1E4u2q1EGfazIhnFKsvPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SJeG4P-Vr-BFB1uXMfL2w1fQL60VXz1HjTaDOCiq3vM7ezQhzL7t_OY25-d5EKZzjSVOWyG0zRSEm5qvkWeXr__Jc2-VWev6jxPMP_kagA13ekTu8T9xklmKyNL6fELE5DKBvLM5P2Q8lqg4r9fNH2MO-qFeK_m1k9T0ubbpcv1C0CvOIRYX7hFflq5aBYZMxnzBYEQLa4Hn6SoGAxd6C0gEakce7dtSuzYFAswEZd_Zfc9WFqTced1idJiNUVE7R18tu_DLq54C15tGSE4noUrPzXQDu6hrEh50B-wMO7_WxiTffw0clk2zdfTmUX8mp6Iq1HFm4l9rnCHlbAiiRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hQuzOXmclr1Ra1x9CVSi3F8AFHSzAV8xS3KeB6gxpra1jLMXykAz0kLL5eI8Ti2KHuj_D2WIz_UTv09pOyUgfBrlRCkJqSSb88WnYUZud5GcjISox35RASeM556ACpg4zKGwGxSoWXsksuqRR_IbJ6Z-1w_FXFO_H3lAKJZJzMdNM7xJsvCPpYnDJuYCNCjwDjSQvhtGIHh53cINxhNRr2JCx_rVwkDnclBQ5qMXRkDfagTz9M33Q5QX_Xhlivgq06iDCbHkd_aYuk8cvofKqeVz2g_YHpzGAIj1n7j5yoJAfvD_AdAIXnGo8AwYJviucLefpWIegWuidspPtjSZww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GWxWpqLVRJ_bx7IbPdVL2AHuxf9ibugY8Z2fszoIpgA2bI-udyFMZLoQs2nCSqAthFfUHrP3Ov9MB-cP56My5wBab_O-VzovQiIW-jaG7Lhyo8EqryVrTkTlSILv-T907CDoSEHSr97RGoEn6_YJS00rI4zpg-h62ODIaCCOiMn67CQraNf5TTEWZVaIOXkmFcdNoleDaLObZXlmohZY_zzUIvUc8Du9htzQnef336Oo7vZJ4iMWogDIg6g3c8JHmvj66MY5HMEgbxXMkhhPTHC6Ha3VOrE-fyQX7_eKJaErf6GXpqVFJvTwPA-DQRmySEbUupiLqEbmqle3b7OSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oTFDZBIYBVVe5SVMkT3gvcOY1j3IYY2N7rgPEXqoiRU5B69lF19--J-a1kseL_e6xuPpZimnY4WuereH_eoJaaoU1-qzqMuT-RqfZPwA7MGNcJ5rxpKHhE_sCIJlqqg_LrfvS-5uJf1ni8KcuLxFiHEcOZdPVoXGkTHQik08rlG49Clg4ZXLxCuwDNzaR8IdBQFAiF5XgXlD6RlvZ9tjzQzMg7WtBL-J1bPicKMiurGn6DMhklAeu5BfM8-tG4Hl_tYdOHI9SDE7amvc0lzb8ADvt7-rO7mToNxF0jFUYbwJP3rQ2ScBYtCd1Lonu3zuQYDHV-1LSB7XwN3tT3KS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ObB0s1om3hnfE30ymNFPL9ZW1Go1ezPqa7nLPcOGzxAPAq4dZ9DpK-HQ5HtCwjT95eK6oyYDYgy6Hb2kIACwLkb2cpaW-l9Op8JLm2ap3nmAQGPZA8G2FGKHVaPsozpEXQDAgsBICb4-tdr6zL086vE7UzXhK_oiDwMPutTfdCDmuBMdfZ1kEQhy7iNPB_OJoujQuoXqvMC04cCEqJija39TSTO-47nP2AGzWBP57m2ur-eezkV2xw6bappcIGVcZ-mcI3NDRWqaCGM_ulJnZ6sWpAGvOJ0JH0KWYAvlfJMXEJ0EykZMEMKQB88RjrgAngK1XFXOq8TeeaPtTe_8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pcTh788CwC8ic6oe1S6uJHbypCSeI15HRM_wEcJxfKZ3TdIw4z2qHa9cVstoTuoi81ZcgGlgFTKnJqCVesYxpVNTxu8UcL_5qX14dXMgqlYgdkrr8ttrvIXZOS3-0cBGnK6V9G_3NbcWuhoKphgjZXIumWhqJRDNmd3HFEx8jheM4R56hxoaBSIbIOGjQ12EoXMk0qOLFd6MJ-8CJGcynJo9uxVPmGf-pD5LLC1fR66PiaEa1tNxlnmJ6U2wGhCeA7-AmquTThwEjofY7JYsnUeo8f3eudTTnXbMICEr8nPILfqFC7VXm5Ky737mTj5FmOgYG7i4OBi3T_LPmeZChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DXeTqtQpZM_2aNEgvb1nj1dVUgjih0wOZ9xZhTg9ZEWxzjf2u4rzieMUAUwc-xHzYtC4bMFG1at-4XvaiS50ZHE7KiF2Z03lMYwlH4qixFpRMoTA0FTAZ1dUvd9emJMnOg6VAKmCxBs8BUTg1vE3crQta0YCQsgWZsIxBFRs6iUI1kBFlLOHnnl0wkadVJIw4BxNmGxZf9l2azgQIUNFIoGV545QjBzLu6w9BjPQef311j1j1dbEYw0h1__l0a1C_CtmF0qU8ShzLlq-G8xkzpmfgz1rwtBcDdY7vF88VvF3hE_wTGI0ZNSPVrKPNIDTUVNj_0jSBn-qeqokJEiqLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gyRretu8sNtXTak-yP1yvJBTdRuyJnxfbCFQ3KQWPdWeRXLvneQEaB6mkk9_qasqfrrGMtnH4v2MN_JB_YgOk195lLDfwBc3_ftB8D775fYK1r5qCLyoTirEZJ9I3FnT1EabrjBarLMsTEzBLgXDmFvQCIMdFq2IrbPrBspb_wCNrvUkNuUcjjRuIGI3FzXKzH-izS6gzHIm5CBkWI8a_y-hW_lSbj6INzshiOXT_RuBWtzu6CGC8fDA2oThaWbnx84wasKPMwxqvjBcEKdwVomOWbso-EXvhAhFww2T6qdBm1lG69xML33lHc_sJ1GCdUfl5-tnGrNHy23EzZy4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qlVkWuPEnNEhhGWBO7m6KHDnuR75CZ-IAlOnPx6HMeVRWEpT96mYVBA4D9u3MUPT-BwiesOs9ca04Whn-Q2MyC_HJcIRqPNcBjjLxXyV8bCsPU5oXiv5I7GqxH5m-yhcVQTFhSDMCvsLM4Vst6jJlBMA7PLaJcOOIaOU7W0dBsZUiVgBftsgekHRO4M-Qlj7AVNo93wlpGX4U8hZex7qVYwfmN60ZjvFWC3M9Btefp8S0khNmEzGZbUKYkZiCK_cxK0C_TU-e8Te17q5bu6w06vgVaWHlUlPeklKmgwALUKfJpt6UNbxXJBU8kISKCw6tGt1d37bwjJJNvXJqexF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GOEixMFBsW2NVSYFCSbOgUfKJgbIP-4Xu76RGYZFpPlVRtXxeII1w7NLIgFII6udz7NJMbfuwgHcoZLzRAzP5e6zysFLJc9fDfvNs9hJ0UuJdkuVPAx1BUenHMd-KJLtoYXjd9cBV68C_uuDwBwD3-vT0HqNepNb5fsMisxNTXRUNMNladJKdVWOiqS9MLErJoMhOJTwT4WT68L0eIJllKlR3LYdIEuc2Z-IWIXgCAa0uhtU1wYk97m8LwnlccHNg8h9NJShCt7DdVLVox6oM78rlBSuRFr4zzj-DxEypTAB3YCUYgV9XDOxPxmOm9tl4o6syr5TEQzbD7DRtrmnbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r4U-LS77hhOoG5axzLOQDVkHUmHPTpT2a3F-V9fvETgSlmr9quxaGL1fou5_bOBXfnONG1ou6HEiS4g3HTh_f2FA1if3eBCZYJlO0wmJk_kXY4SlBiHaOoatmGNSXnXDy8n3uaACcWrkjByk1l5ZHDsH3wG0lwIwbvplbMpVc_IJzmm1lDvWgkmYH4XEjtsu8cze79e9TxQU9tX9NlhuCDWK-v35TLPp-Nm5AAChHxUaY_StRoI7xwoYyVS5sayAhRoVjwNub4aw3bNC096YG3a2LlZTXqgy_fPMDwvap0NVNgfCw6W91wOFNmqSYLp9GSXcU1fg31qWTbIE46kh7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NFmpKPlT9pAMsbUH-JotuSIZxgvEU2pW2y8tIhORiWiOFXQYgkMEk1-EZVqpHpVHzoaQyo8YUnz9MrSUXFEc7f96fOfKifOls3XCY5HD7pB-MiBiOkX0CHH5G8Z-zYWgsWGiQ0dBXp88JkUaN_xgLmHynpaqEu_hXfvZAnER9tLO2__rLqBas7Cd3RqA3pzTADRzeI0UdQ2B8f7q_mhsGGxBGUAuaBuoV4B2mX0aWX4uREZMyYH6_HjChR_OfaO9ekEpn25_Y0yCetPD0RQ4o2NzEFyLvrUEvBYnSkreGYqQD0QOuMx7Km0HpUiLjJ0BJBiBFxnRgp28mEEq1SjJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CvnE68tvgHWk4l2LAo_9ZYeH47KeOAQzaZXPpwzPvHnR0JflFik3dJuYpF02WvE2JjHSLxpeohwo-QoZjwHxC0DLRLhGGGtiX8399KomHcjWA8G2HOKieCyLPaAZS4cCMt0ME_FtZJeMvNvljpKcZ6xbe-25xkfSVx1BG2_eaN0BikzCtq5COKyvfjKxdqcXjddoQySnh5Z1ZKmwplYHhnCbLVvZVf2VrzD8ZUKW93nT02URn_3lLSLCt53UwHdO2XSCniI2EI4z40WKvoRaP6Q3rI6AYXUPUKOruBYVk2cNxGMhjMjN0Sqqoy5WdG4PIuU7sqDaKKOYZw41H7AKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f2qibg0IpwRtDz2BPY0JDI5bpReq85D4iHqm10t_63HEiRpiJC_opmmb0RBpWrIVcTsLhH7PqbiTq2RwoXwh7BRFetKwVj9QiDpIbcAXs1tdQ-3ZA64TDSilvTxHPqHGXEok4nr7pKcU7MMWy17pmDcOhxd0CGie19RP2Rs3513RwnF_hBqbjbVnSTqcfEogj5IBkXllXWrhYiyOzuamjWeP1yclskSHAJjuuaS4XaYOMH-0bArRCpLnDlc7pd5uGc00xWmXsn19CzK9x4In1UdWqkUyaTOfgA_pZR1mWUY-cyf5T96kwCF7B-LBEQAPahRdm68chIMCrPeXoWndnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون
با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://aws.amazon.com/free/
میشید، و روی Create free account میزنید. بعدش سایت خودش شما رو هدایت میکنه به قسمت ثبت نام. VPN هم زیاد مهم نیست چی بزنید. من با کانفیگ‌های BPB رایگان رفتم که آموزش ساخت اون هم اینجاست:
https://www.youtube.com/watch?v=iAbYpjXyLpY
3- برای آدرس، یه آدرس فیک از سایت
https://www.fakexy.com
وارد کنید. شماره تلفن هم من گوگل ویس زدم اما نامبرلند و سایت‌های شماره مجازی، همه‌شون برای Amazon یه بخش مجزا دارن و زیاد هم نیست هزینه‌اش
4- یه ایمیل تأییدیه واستون میاد و تمام! 100 دلار کردیت رایگان میگیرید، بعدش هم با انجام دادن تسک‌های بخش Explore AWS که تصویرش رو گذاشتم، می‌تونید 5 تا 20 دلار دیگه بگیرید.
5- ممکنه محیط آمازون واستون گیج کننده باشه. نزدیک‌ترین بخش به یه VPS معمولی و راحت، توی محصولات قسمت Compute، بخش Lightsail هستش. چندتا نمونه قیمتی هم واستون گذاشتم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D6eCZQVe8f2wy8GBrJHb9Bn1p0U6jwaqmc0i3op7IwF0ozEl9jU__8r1KTP-BFVXib5kxWhXPPC3gDw9dtUlHQO4GJpc1OzPMqeK7-yTKYZHyZHZwKyJhPx_mNx7bom0HHkgCQT6CyD1-BA2Q4ldlEazf7Ij26OKQHwvZGC4qaE4D-L7SdUZnJjYzE6xX0xHCQbIFRKokNpJmoPI5JDwopPxlaSEjw2fhwjvuvO3Is4w5DtjjNs44Blb_9MOojIIuNMf0u-rYVMojEFaAIXhBfrpNI4akY6HnchBxoOd_jhA5ObdWIOW23-0aUBC08po8F-n10dn2Ll_WMqyeTfONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrqLzy_tLzDpWzRna02sbqHU1XbgML5MIzw6VK9l_Ru6tQ8-1qpsgAREZ0QQUyKFCeq-K6ppuRqeQxstGELIqnnhNsyKPv1OqIyB0MJ1w0Yds7ZHHQBYDVehdL_pxqg4O11H1EuUKkUzL7i29AqrTEgHwx0KnmCNDNZSmc_NF8ChdlsWopp2pwFVfoUbgE1umBzQyV0erLTG-flcv2wVbZQBQurHPuwhdH9WpGD9sWBoayk-a1Q7vmCesGsY1SnpAmoyhl2MK2nb3LkPg2Fp5YXU8fqH4DezmGtz_eVP1lxu8JM2AnHNMlLwME4qOVkCaUoo9No2iVj8qAeNazSk8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDU_bCQR4z9JkFue9a4K6SKjc0KIQSiqrCfaXMnsT67Rvl_u9C5as1NxTVOVeW3VjyF3sQbUZ6kiNKIbWUa39xN5CPi3eG_XHpw-sXQZ4sZS73WEXc83sHj0yvGbS1X-hn84rRdj2NjCdY3bR1-GMvmLdP8wuCHXqE38oan-peq_CyL7Vn7SsMiyPOInnnRjjMpmXCPP1HqFS-SUQPu7lmAUfypu6ubAbknlQMtkTxwa4SLtfhZxFoxB9f7-Gtxuii4_nKzDZ1ns7-b_ZTVxD5uPPIN0NZsWp2l7C5-1v_bLt-FFwCQ8YLhcw6L934hOzMFq9KxBGqJf2C0kFReHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iwHPdMQ03UaouPHKH9rhZyklUpFENidN1aA6Y3Z_5FXQg9eje6cLDW6XUjzDR6dX76rI90V6nJWGxomtPmuUjUK-BGOrGpERSSXqDiciI7iZV2Kja0niiUdL20ej4jUUaI3A1kMKCYeVdCCk6U_e5EvAKlHT4Fh-hkidPBSeaAbsje4UH6cUuJaCoeOQW-IQKBrL9tA7KmHw8eAX-aVfx9SXnmmunCZARRMPPrN2o4BBZxizr2gLZpPJif4yG7mxKYeUNh34Y6xa8OWTxZKNLuvAhnHHTRfjf0fov33lbGj575inDIYkY40_Hqo5xNvHr0IBze-XsWMrPJhA1Bf9Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u9hWGlYNPwUno6VptZTKTrawqb_YqVWQfl7x0VadLd3Ve3byq_rF7Vf-l66roVbdCXae_M6hDrg9vdeNeAcRD07uRKSth7L7_VFJclWG2kq0ShvcpSV_2r-jtnbhFn-_ypDxRM1FoSGHkFUPmIEA3qaeOISlgO0iXGQwjwX6G5N87vZCZ0DJMtt-CS1wQUxCK5hqE9Iq3TmEIqs1Fl3mTrrdU18o6fwpe3u30TyVoT4C2zBtfmzYsVp6M5zxaXTxDUfYTVFf8vqMUdLbCDQMXw-SKbB_U1kke1UGA6UwQYm1fx0duDkOx2WL-P7PN9amtZKBHUw-FtGIf4JWxwGxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hdIwAbN0T4IWgGdWs-ZC5C4Agn1z7HJTe3h9l1R1wZHP-lWaYme_63iEKsB3QG-gZ4kiZ12N6CBKW-v7dIJ9jVoan--uffILS-crH_FafBVT7Q8OKARf_7F_yrWYKXE5UmXgOmg7zH69kSAIB6f3peSWqzvbaqmYIvs0cRoCxR3pdi2TZco5fy2PLrPjgEHWlzlTE5GUEGU_mqF4mNLRAJsC1CIC3jd-LjIB1v17MEIc_5CfOxJjVuw9z3ZrgH7-XkW1eu2OykjF1dP1MZnKOb6vBePVWmmWpX2Da6uWsTGF_P5qWFgkHWoeR_W_TDVMidYGkZzN_lvb95l0h5DdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ugVVfNFJjmP_D_MwJL3KH_LSsQcGN32kvlrxCi_xakH2alr0XKJwB78cOspnC8FUgCHdnwDEAVXShPKpJwwvaWyUXb_g6ENavrMFXTS6gU2BdPWuYDgaMlME3lp6w_CO39ZXwksmz9NSVbj-hHkkyOMsU7bsi-2xBZZKs3Xf1qrnoOJjTDAgae7m07QAWLUZjOH9pc9LXfDsVNewMN3uwCecT5vsVs3TBx95WG4L7Hk_uqK9m_6uuz70t9HDHFHoJUWZ2F3ssg_Df1Xz8xtygFQxiGYF5bGng4dZRXNaGgYSHzr81-OyFo6PXk_Oaa3SWaavjXs8vCiqEVVwbFV6hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfoHVcXU97Gq-BsR168mOKZ7wEwAMT16RaWznve1kkZOTq21ovoAEu3ul13D0x3JQSldChK5hM0KEpfPVBCJ3xH_ic_LDTYelwxuWflymgQnfJN5axXJK5ckckAKNOhuhqrvT2Edehhfz5dEqa9Mssd6nkSo1pzVY94VvVPBKiEjM6tgH8sQ_sfKg7WfFHUcIQ3fCir4hDPH2tfpgUpSkXBfyEoRwud6u6TENGDHPmVwv-Xc3GkMwlN6YwQ7YADvRx_5OqbOcCwBZM39eHH0VLq2F92BgWxI6i6EUAr0sKuMycczkGWnqdNJOPZKren_f-S-9gynqrVwiR3xqVd9kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f3rhsTxLaXf03lO1ajtKNJNFo_pbj3WsMmpt5QW2VrDcOiSdmupa8QrdfenxFLpRoddDFbOsGQ7SvFQFo4d6YpYsTsW9Bh_gOKkbOhrS8p95ID6kELKpcZHR5YZ6Eb5YhhPPtm9Nw2V7PuMtUH_tpClNZlIadJYZqgLvid5EleL4v6Gt6ypEa_jsh9uFN8NCNhHbFLTMHl6sKISIvvjo9yfdffUS-0qARlnymYpte3bzehppMPTHPTOBtoWMmOWRxaJFwDKyKtePI7_xgi5WXpZuzTeWBBxoVEXOf06bLTs15UU1sJL0UecujS33V6emUoh5qm9cMfsHek9Iq0FeAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eey-FU1e3GrYCxkd2E_YQqNVV6w37r1C0TrdGpV8psdSDWkTkDdRZ_HJr-AvbQs2_V5TYhll5aCq3gt6IIQPzSKg_g_tD_jxkWrs6bMTNymP7ZlSe50O8UyhU8eWAFGuPuSRu6VsocSg1Wb8LNsmCzm-dY9B4-eI5Q107ArncTRXvjlhJy41rCZ8Z-RnestXgJY-bQhfbHLeR3biUpNE8v_8wphTbASGqam0bAwZfU_Fe5biM7cKlylZA3e-6Kop05G1MhRSOV79SG1yDLGPNarIbJXU8DvsJzSzfUhoh3rnKy4NdK4lOkqxaMXjikhKr1y7EuLappb1l-5ol4YFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AC58B2GWxxx5Xktb6q-336L48_cpEdwgoiHKqmOWLoEMKi-Lx72pEljIUYosAuCyVpSMY4M632T2qzFFzqudRCGwy-bY_zcd-7E9RZtcDN0pXm6ACt30lg-Yt5WQEnb0x6RMpleM75VKiBqzrEfPtAo-p8Y1N9xS4trPtuQ9NK0jZXlssLnL6_rt0wAVAiylwptHt_J4f4nS1piNnhnVhGDg5c2h_XzSyVegOyoYkir6oqMju3MhM2UsDdLMmk2OutVVXIWBuK3-Fj3G9nYQUow1f1aGEs7u6vVYidJcPLjuZbAD1BzCsMjZvmVhbcSldHMTD347eQaquZtpgnteDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tMR7SxwXXrCmY2LBvVHCrB2RI4PIn4jPeZrNqrpL_8SQUEljUqBfXc1IoI6LQKwBwABsa9fcpAMmSPR1ETbb2ib0b1aEa31L5eIQiPSpSgbtnGDkKmz4E7ZG1y2ckhUAmBKxCryrvCcgNatYgpF_GmJusOas_M6Nn6MjegES-lBr_zxXq_z6vtEcLIabEzRnsdoA8AFMag-gIPhr3B-wQGYg0QLGw6OY5Be0pTp4kZ0_cwNGYvcH1kOBtTAc8G5H8uoeJz1aolV4UmoILgKGu8wMBs56Gc1KMsZMz4uW3ArAmC5X9vFj9uSb3qGJlbkEY6SGE88amEVmfCKoJ_-f6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟
توی این ویدئو، با
یزدان عزیز
در مورد این مسائل صحبت می‌کنیم:
1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور
2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن
3- تجربه شخصی خودم و شروع واقعی برنامه‌نویسی و مسیری که خودم رفتم(به علاوه چیزایی که به درد شما ممکنه بخوره)
4- تغییر قوانین بازار کار و حذف جونیورها
5- اضطراب، فومو و جو الکی شبکه‌های اجتماعی
6- درس‌های حباب دات‌کام برای هوش مصنوعی
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k2OW8-VFG-gwNHcam_NvtnVVHWX74XLsINHhcBHinjyCBUaVXaqojpe7JgX4Ys0cfAsEVU_YE-W3CXq7EVJVX4FBi8e7THw7GmI076Ca9gdxRayDRi1K71O1mXJhRb9KTONuLRa9s59Z2T5L3vwbejTDaT9hhMhwzcSY0P-JnjVK5BTjdRDmAh9Ab3Tx26D3E3XmEdq4tbF8eYE3JNNrQ3wwJjYLdK76okV8GYzeVggnEBXuBMmaFo4gM7lM_R4EhZxm9ynst-QIMyUs9izXx8G7b2dJaAA4wws-o8h9pipwrVk5wsx16rVYy_92G7GxVGB1ViXGZAxmNQwGhmgrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t25qe_yBQ34eG_jcGMhqdDi2_Fs1mIKb2PXqZexANcWT0w-niXQM_FRao5XJB-Q9ba4r9WRLYNbYNREiRAAEDt4WGQucr2RBm6LlaPzTYoJGc4R3DhDO158jvd0b5rI9Tl-wx5uaBLl2tKCQR-uYcCWXnfjeuXbZNJ3legm6PzgsyR2e65XAWdof8xvLwXdEpH3p-UoR79zwbJfwLrI6oANg9cG9NnJgkimTLm4joPuCGS7gVid3XqdT051glP-NBrHPH8tAFu5M07Xv_tgRRwl93y5FiphD2lCeu_Wry8MHxoQT_FQJx4J-v1XkHYjUzvVXKqDKvU09P1l5tQcI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oXOofNbw0-BuH0nCviN97eezmU3frzs-4ygwnQ_mp5aAOXo_SseR2yxQ-55j2Xxm-ByfgukQHXVTeabeCH-L3gTaj5sFdkheXVUsZSCRI0Fv9LvDxwWuM-p1K7ajn5Xjv_rG70_Dm4vrrODOBPxl33aoedpUi6PmJgQEd9gy-WqwOpfEy8nXAT97o9S-SgkFZ6kbbJS6wZ0QhROGdmnXHdAnx7MU30kQFpi_AXLWxvZungIxtlU7Sjhr4LHC_KK6ch-KGB1NuTtRc6aZUWAg3Vyx_phtEMq3iaxa4CnuxpHLecXo9TSvPy88YSIFl1mt1hNo8xiQtuB4IcTXx5y8-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:
با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.
1- خود 9Router رو
که اینجا آموزشش رو دادم
باز می‌کنید
2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline
3- این مدل رو از بخش Add Model، اد میکنید. دقیقا همین رو بنویسید: z-ai/glm-5.3-flash
4- می‌تونید چندین تا جیمیل اد کنید و استفاده کنید به راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W68N6SZ4LYKY5OKH5Xx7OqE4FWYbSvWQ1vgmFBEF5DzIaqL_yvkcXej_60lvhTSc1XbMki7QbezDJVWJNVG6FrujDjPjP4dj6enJ2IBRXGFU4C4KKpnB13MrJUkr4DDNGUiAx-VHD0LPOPuiubdeTq6dUH3816bNObcQqUbwckwFAAAykO04avOpJXKQdg2KKKJASo5opuRrMUQ5LZT6bCZ9WaHW9ZY-dl3yYhhKvb6efLETBlLBVTuhtUnlzQduZHc4gJ_HF5lqWORsvFjv6OJdHaO7PiMG4quLV76i0Wmtty8sXP2pvksrjr163Bsgd1RXtIqSjMpoQsbn07dN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfYOLbD7comflPcCbr236lk-Uh5KfkM33CArQOYXjvI4dYeLvxSdluBohDoCE_1bL2AMWcQaW5QXWUf54rSsnWmmGIQJiSnGJAR1QmHrKLmOsc2Pf58aGVQ0wUfVgF_Ygtn5NIH_METvahlo0v_ymPvLnNNWZzKr_cldHAPnJ5QtSw80fgzAY8C15CNpTUXjEFol-0Ny9MJngwZ2TPl5ctnrlRP4pAB3HxXkUtFc1lENG4tngI4tNkawtOOdTJKmWEud7EQfCzVuZucuOeOytmuK3rHI2uGFGiaDkufJk7P1mhfgg6YAi15ywKg4xPtZbzKtT5gsfte6pqHIKjk0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K3O4dhmoumouhlR4hxglJO8qcryQXLmhw-79ADoSr_QIPdTq8iclDT-2S-WG5U58p-NME6-kS1YpwNgy9ag8kPFr1pCCj2ME7EvkmwucFYMzaojQeQtNshyc0VeP1BS5p--H-k6_B7hHqfu_cKClWtgZ2_LxKwhz_bIp2y8tW2viNkO8e53wNup3pU73-__2BKSohE4RCpWsuPj-B6uzpC2saWaSYqKAs89fTLOLprtaDUsakyyu1kearwDQxmFhPlPTW8I_I93kHL8XTqTlIs-3ultGTqwCq5LGLg8JrE99foxEU567n1hF6Y8NtCaikUyRv-EP97KyWA4inu_yFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ببینید من خیلی از نکات رو نمی‌تونستم توی ویدئو بگم به خاطر قوانین یوتوب. اما برای اینکه پرداخت موفق داشته باشید چندتا نکته هست که باید لحاظ کنید:
1- برای خیلی از جاها می‌تونید به راحتی از Google Pay استفاده کنید. یعنی میرید توی
https://pay.google.com
، کارت رو ثبت میکنید و تمام. اما نکته خیلی مهم: برای اتصال کارتتون به Google pay، بهتره که با آیپی آمریکا وارد بشید که با همون روشی که توی ویدئو گفتم من تونستم وارد بشم. اگر کانفیگ‌ها واستون پینگ نداد، کافیه که Chain کنید با یه دونه BPBای چیزی.
2- تمام چیزهایی که روی گوشیتون از گوگل پلی دانلود می‌کنید، می‌تونید این کارت رو بهش وصل کنید و خرید کنید. حواستون صرفا به اون آیپی آمریکا باشه
سؤال1: اگه یهو بدون آیپی امریکا رفتم بن میشم؟
جواب1: نه بابا. من دویست بار با آیپی آلمان و حتی ایران رفتم. صرفا ارور ممکنه بده یه وقتایی که ارور کانکشن میده و ایپی آمریکا که میزنید تازه درست میشه
سؤال2: آدرس و اینها که ازم می‌خواد و کد پستی و... رو چی بزنم؟
جواب2: خیلی راحت سرچ کنید Fake America Address و اطلاعات فیک وارد کنید اما سعی کنید همه جا همون رو وارد کنید. حتی یه جا از من کد مالیاتی و اینا خواست من الکی یه کد 8-9 رقمی زدم و گیر نداد دیگه.
سؤال3: کجاها نمیتونم پرداخت کنم؟
جواب3: ببینید یه سری سایت‌ها احراز هویت با Passport و... میخوان. مثل اکثر سایت‌هایی که کریپتو میفروشن با Debit card و اینها. فقط توی اونها من نتونستم پرداخت کنم. تا الان هرچیزی که خواستم رو گرفتم. که اکثرش هم توی همون گوگل پلی بوده</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b7-iYfCe1_Y3hjV2pyKFY2XbCAK01Eq3mkrlcIYBVO3BYjbzak_UVSzSiRK8Fi39bYgQhQoaz1OrtqNhwAgU6_OyzWeYHtsW7Lpu4HjAyAShPi-vNdHBd58Rpn8mfeBOUaRrnsIUfXmkTU_qWMJv56IthUnPGkkais8SRSfyISceOLdmf2dwQN3MhZ0mkbIIxsskvCU0snnJ--gxuPWDr4VpQSpmkuefyTZ3oqrkj33XqVdAtHuADjqCzn-olbPVcZRP-YP79KMVBcSJW7A6yVaUn1P8Q2O3OhLdvqapATYFGYQJF2BFkijD7DPyGiVNfKLmRQHPiG4jbfHPGVibLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت:
https://app.mpay.cards?startapp=ref_S4FPMh
ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر:
https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت برای گوگل پی و اینها:
https://t.me/MatinSenPaii/5092
⭐️
توی این ویدئو:
1- بهتون یاد میدم که چه شکلی می‌تونید توی اکثر سرویس‌های خارجی دنیا پرداخت دلاری داشته باشید که وصله به ایمیل خودتون با اسم خودتون
2- با کریپتو حسابتون رو شارژ کنید و از هرجایی خواستید خرید کنید
3- حتی بدون شارژ، کلی آفر رایگان بگیرید
4- و یه صرافی با کارمزد پایین معرفی می‌کنم که می‌تونید به راحتی ازش خرید کنید
5- سرور رایگان V2ray آمریکا بگیرید و ازش استفاده کنید برای پرداخت‌ها
6- اشتراک Command Code رو هم با همدیگه با همین کارت میخریم توی ویدئو
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jvdB4XRTw3ND8wVPdyu4Bg99oitFfSpN54L9OTm4emB70BBtZi-c5c5rkZX3fvLDSI2jveohh3wO40E5TbwcOt5derVtnl2Sqj3YqNY4R3Qf6Fjmq_3yMCEziciHzyATzxY6Kyi8kkDaVzxYWh8vR2Ypro2Q8ANcFaHiYYJWODdUS8iA4Lyfy753m8cqN8rYRP5ukpzdqPCnwJICvDQmxN1xqb-nA2p8Srxi_aMeP2usHGjuaof8vK3O0BENB4V9V0w2OKB3wFexTEWFNG4URs_bx8MhnKl1N4aP9uHl1k5owGOBUK5BLcyddcIMwZ8yILFzl7unSXaaorczrsQlBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=cUhFkQFom9ys4g-ctt7JbAnN30qPVW2csm-hBN6KpZId5anBimi0g8Khcna9fglPF1B0ZCJN2isqDc_IGThjFfKVesGsPzeclcKY-r8cEs6sFX2tgmRT1TduqM-qO5SVZSxl92i6pp2wL_3tal5v-ppQo5anuKTELnhFkfgUGn6BNTdKY_wHRrLQvQ8JPlQbDMjb2e29HkE-pYn40yXOXume67WbI18iUULYdnhep2qIyOsH0A7cLSf1wfmsESeucY4mSxgKYpLCHoHkzDzF6baxynZgzaqJ-85D7FgzXYXp-8xdonTVuryrmDN-XqwXYmC8u81nGIaJVRrtjA-Ruw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=cUhFkQFom9ys4g-ctt7JbAnN30qPVW2csm-hBN6KpZId5anBimi0g8Khcna9fglPF1B0ZCJN2isqDc_IGThjFfKVesGsPzeclcKY-r8cEs6sFX2tgmRT1TduqM-qO5SVZSxl92i6pp2wL_3tal5v-ppQo5anuKTELnhFkfgUGn6BNTdKY_wHRrLQvQ8JPlQbDMjb2e29HkE-pYn40yXOXume67WbI18iUULYdnhep2qIyOsH0A7cLSf1wfmsESeucY4mSxgKYpLCHoHkzDzF6baxynZgzaqJ-85D7FgzXYXp-8xdonTVuryrmDN-XqwXYmC8u81nGIaJVRrtjA-Ruw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0  مشخصات کلیدی:  1-مقدار ۷۷۰B پارامتر کل ولی فقط ۴۹B برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/VhZEXWRAC6HwQ4Af3XoS4fd-YHbgsWkgC67xKmrkMnY8h2m_p72I-P8p695K_iA3EluiNIrP9vsgXsxXr-P8nYdpNBd6_gCofCbySE2El_phpASA2rldA6NeaE3pzt20CQy1gtQ44pATN6v8n-sDY_OwVYv8nsmOvUVR7HXYK7x9IVokjYAlUcyljrwstvI0u4jCLsq79xUK43ldOjmywLF_0hsB0mMcawhDCHA-HDxYpYQPTGvdfmrumJWKvl7CQL7VJqtQcXhMX-bAdMgz0eDsKS8_IHWaQtbhlVmkgR8dfDv_kqXpQjgzPN6LibM-35LnvSboTLcGztE3wAxOMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/iigEiC6aas8IbvQirRxFaJS5YjXWdSAcewbI6jx1nhhgfT82-zTMS2GCB2_4RHQO8yJFDKlHygD-EIM-EbMcXnKiA5tkzIk5o4FDA3Nfn-CKIQdRmAxAJevZ918cDgDNmUvfEplyp2bmvTVYL_xd_8Fzd9eCddh4O6xmAzd6D2buxuIsPBhdqdA0ra9XWxBJREyFuSCwxPhGuXG_vgd27sg2xlzVBQZI7xNifFSVkpCkIPQJqejnIvu6HRx0YoSYSiSq-8isrzqB_D_9ODG5FURMZun12csQCIf7s40Me6WzuKBAGPx1idohyiQrxambtGwiHEprGM920LR4ynIN3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/d71VLKPElzGaC3whhbw73eVR4ImLh1L-WMfLWHjyYMip8eUDEnQ-o-tVZyKo5HdSSbgKWvNnDMSRLwzQKfl3-j8I4UQk-5b0JjtumQ3yu-mmG4_PQlifR6K1WXRI6vqm0K1JBGtf7q2OxkeXg25GFzIoTSHAawNAKIZuwaaJraDSbOOdKH87DJD5Cop9M7FDh3z1zL95Iipsc-aaqJmmvGheFE2nnr-QNBagDdqcME715f4GuF_El0PCJNWT9VDXqXH1Gm7ersB3Dj6agjExfuc2EwKtXodEnr0WYhu6BYRixkyF7o53fl5z46G9twtHUm2tGO7guvf5GALBkpTxiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mr8F7ofPfiXb5E0i1fnEXZOBwH1mSvIvCR0QfzbO0qwslZcCeXzi2exCeE6zbloMLnWo3salGCi62IgAtpc6xvezH0hh8PTfUG3HhCx74fFzf5qNGX33s3m1d8PQm_UkiEJrfO2pUxdtXUhY6ti2fekFmBvm0dE-j1ffJNevKWAJhQV2LPsLi9fi69HnxBdjqA6SiJVPQ32dY1MR2VQh4EqDIMn1JsHZUBdHtnc0D_tfqt4iyIaQq2npghIAA9rVz0BYt5P3N5FZyiO3DR64VGb_XLvfV0Y-SnhrrEB4fluuueke1wNIUAnki9eTJ2KVR8QCxjee-r0zDy5w8q_9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P2FbGmlTd6vH_SEctqrzlzWfTdmhFGwH5t-n9Yyehw6YSgwCxXBDqWojd9JnSDDhFMBT_b2o6XNSTUYL1gqxskD0opFWq0CxuXOJpo6t8o8c-8S6Arkb2pyyQ3PTmz2OPHpxnJFVGhGy04d3rhXqyECq2FWxvZRJh64HjH8aefwTxQRh-HIRcrHVlX-r2QZdU_PYsaEwFx5pNSkDm16MzoVlu2_d1YZYtfttsuJIO9RhdfOA7s3GfjkV2_rShldrD1UpD9zc61XWdCBsScQNqbbdLEEYp93EDGdBiMFFe5IOdXi1hFBlxt63lYQB1LaVb8TXL1Tj7BmYWL55Dd9L9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OpDnVvckayQNGtezqS2cy3MlFBdzOKishXvLF4pPLxgYU4SrMub1ZwO65I5pFngLLxtyxU9_z0229KrHBWegBGfkGxSw6eBifqFifUIH1mWtC4SbuSrtdQ-7ukQF45RA-1rH6Br7jNi9KcTw1aQ0EfnNwkqfdSQpeYdBgit-u9-lWOvG0vuWrCISbWCxC91GnuTuUBfuFH5KJL7Qu0iTmsAdeSoU_6NiER8-gT6HG-Uj9kNqlTmsVV1sGCns87XFiQSOpDSD377Cv0nK9rsDxd4k1UA-WjcZxHQmE9ZEr-wThtg4SZuNmTa9c4cctaXH1ZuOPlGrKKUJgvHJn8tUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FOtgiSKFp43AvJcKmEFy0_e4OSqOQMzFisxPGOY-k_-ZZtkXbLAzuMjwSfDkHkIRLVRcC1nWaiWGxrV-e5vbg5NK2l5pCPasw0yPGX_YojwWROLdJaPpZd-6PRErEFleraoC1vYfXfVLgVYvrDmaP6AlVk8Vc3p8DL21iMcH95K8K2A7n6DxwBheYW4W2O9RwU6iwgw7wewCsrdYwa362Dids4DJPRtehCBwzbJF1Xy5LndS5z93mD8QnWzUN7_jEoMkOzOv4ev69mF39VqsZuyk71i9aByayGkvdbEWvTt1bCgRZXqV72xhWoOsZ9RggmhlOI-U8LH5fizWPgr8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0
مشخصات کلیدی:
1-مقدار
۷۷۰B پارامتر کل
ولی فقط
۴۹B
برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر
2- روی بنچمارک
DeepSWE
از ۲۸ (Hy3) رفته روی
۶۴.۳
— تقریباً دو برابر
3- بنچمارک
Terminal-Bench 2.1
: نمره
۸۵.۴
— هم‌تراز GLM-5.3 و Claude Opus
4- بنچمارک
Code Arena WebDev
: رتبه
#5
با ۱۶۳۳ امتیاز — بین مدل‌های متن‌باز
#3
5- ارزیابی داخلی با
۱۶۳ متخصص
: Hy4 با
۲.۹۹/۴
بالاتر از Kimi K3 و GLM-5.3
قیمت API (خیلی رقابتی):
- Input:
$0.83
به ازای هر ۱ میلیون توکن
- Output:
$2.50
- Cached input:
$0.04
اما هنوز، رقابت رو به GLM 5.3 Flash باخته به نظرم</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PL-OC1KKJsJhJJ7_1W8vdKQqpGf1l9M8ljHb2MwlvqLOcrHJa5ojnmUGrEP_HYe_HJBxPhGSlYQbqN7Vq2_xbPtq0B2rUDSZ5TELNbn0uE6iVRwYyMyeTNE6_4Og318pXLz3WXdcxvgZKBccaOpf_rp7yRzD8v_CJDi6C5rQJZE5Af_zZg3od7LmN5NJWn_zEudihabX4_inUmAkhY5km9_nENB8jUiAaW_tMrhp-z8k7AP2W6XpYVJ-sVwX0sqdYZvMOO1WkmRrw_dwMUsyFFtgLZzSOqgkfn9YmTlFTnYgCnfFciBm372LSb6ixBGTRurKJi8ejUgz5qCaTEooFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/culaNmunrhkPKsoIPZdiNX76m_fm5Jhg7cho5UO_8r7yPMQGzJxtiRUTVWHuWsX1bd5v5MpeTcI9RZEJMQaPpFhIybACIyW30lY7eXCR0KHbsLEUEBZJRLVGnIFrztgivcxmQBUHnkLpH5WXN2ta3cQmnAG8FmRW7rUHseexDhJ8xTfIdArPbonaue5GL0hoamK_QHJX8X3c4-__QdHdaludExqz4dC27Itihy_arWP3IefjGlXT0nreq4YMtuqldtW2P65RmCQMki9dRdPKRaQ5fjkaPb-pYonRsRsak_hiYXzrF_4_LJ4aJKL7P2sibhGe58_pzduGyHz99obkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=f0JTq80OsMrIvBtQ72SYNgPO2D9yaz2-aL_vpi65Lae61ZV8H9m9Bp7U4mHRc_P2qXXu61vbAleJjHkH0nYC6u5vRAR4A-w9Z_KOmK6dSjGnSn0Skl0LqdMtokERGXlhBeqfQ7AT4tENBx0wCJUFysSsEBaW5BkmvEm7c2rupk9YiSjMjEHAwTMPBFyAeMH5AQgSnuBEMY7A7-_H6MTVjT1DjEv6fKwU1XpJdrv8D8Do2LCSmWfziVizWH2K_5N7gHrxqgI68PEshuudUwBiVDwx3085Ee3rLyPfBYMD0z0j24yR3bEHVoTomrCcZ8l-EVXC0uplYFD_kAHf_tMHXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=f0JTq80OsMrIvBtQ72SYNgPO2D9yaz2-aL_vpi65Lae61ZV8H9m9Bp7U4mHRc_P2qXXu61vbAleJjHkH0nYC6u5vRAR4A-w9Z_KOmK6dSjGnSn0Skl0LqdMtokERGXlhBeqfQ7AT4tENBx0wCJUFysSsEBaW5BkmvEm7c2rupk9YiSjMjEHAwTMPBFyAeMH5AQgSnuBEMY7A7-_H6MTVjT1DjEv6fKwU1XpJdrv8D8Do2LCSmWfziVizWH2K_5N7gHrxqgI68PEshuudUwBiVDwx3085Ee3rLyPfBYMD0z0j24yR3bEHVoTomrCcZ8l-EVXC0uplYFD_kAHf_tMHXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zjhchn0RqvIQ1q8VkJnS78ChpYNlDxW7AaEnzZC-ESTf6MT3v5-HAqpiHdbR2S_fuB3Se5cWhQrLRNLGYyZijTCvCk4ODuSOaK6lMFFB9rvwsGX3stthfUBpLSuvCi5aetrT41ByNw9WI8pGGOs3otQ5-7SrDBkmccnuZEql450ZTjpXtuHWcEidornsIzouY7cnw2vsTGXr9syX0MAI1vkuEJgeu2QZ3ailrPjAXgiksTv9b9wkw9MgwQ_m-RprQzQb9CtmzwjbpoASwDjpNiS6b8ahVUwVrSMp3QWEVRlQmnzTYsaR0rJDyw0ZzMOp-f9qDhCe91GpfMG2CM6SZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bRs5uC-66_CJXyQ6Jcg_Uy50Qfx1TM-5YHLPscgRMKvIQMAQl2TEzFHDeGnNkfXgzjq3Ragou6qaekn_LfsTUmAIva4Qo5pZDfFEU4XIWHOnFbG_UZp4gYcoFm-h3I3lh-uWVWVm0Rqak2rRGHIKe1yJ8EfKOzKpsz30GVQ8JGa5Z7wX2hOKjhfW7WxboC7l7PDCNJdAgcbp1bJGp4L4ta7-6rnsk5Z8fzjJRkIsZwREozXRpFXlNAjgiatwCbU8wj4yDXiPzWHt6wbAImeJ5Me8B0LcUiwYZQqn6eCycMoD566xpgT7XmhUAhr2EFK0TTG_krjz6ZwTSNLKezQPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HoKpbCOAlwAJd7zxHUlgm886cw01g6t7hv3QURP1LUjYhmWjiJFEb9g_adFO8dh1CM-t3XPu5rb978DPptmuAIP_dRikD5-0rwQwtQdtluHu_BukMLvCsDG1YEvfEyXIKH661neCXloLaBQwVqxrZ3wqTYsfG_c6aGUM1Ro25vlTTt0-fvQ0CY3to0ngq67ne1woO6WXe9PeW5P_loGgrPvouWaW6fcB7hroWzxcxLXMdZEEgLYwR3aFxTYX3LX0SHviQDVIQ53Y-L0kiicpunGtuFnk7aYNHJETO0JKSMK437EYfo4BoaiQTR_LFJ6pwY4sWtX4bp6poX59MKiBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GM1d0zitfIkYQodphxHbeaqqIaYerToHIa2fhbarYFYlIFi1UWaWQLDGxW4rhanJvUCUGT4pj4zSW0t4iYiAjK4sgR5b89VlPknT_UfhWW-pYFqMhDLTFBmfGNqXI5RpIeZzcGCoDRUVWP2LUnXs9B6TDCWnEj6Sk2usUo6eQZmrD5z6mfo3Zv1JSImtd2nSQ7kzTXmULhRoBhX8Y4unvkg-nKatIGRnnTfDetmVcjmAxGKcv0RGOCwuRRPvkh5Lsc2V-Auazu3PT_ogBzTEwy4hD2GmatZOdPLX6bFwcSxZ-kHhfl5eudQm8Z5X3PF3PVpYi9MLAWugEiK0_NlJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PnsRJD-nLWDX2DgrfITdobCvn1vrgOuVXs1EGR3A721u9DqXxZZGkn4KqoHySN-7SI6cwV1n4V-4o86bDbCvCncZF6TEkoqVgOCHNtBvcrAri_p5vQfmX9KkfmojUm83KGTZjKyWuqAJ76pjgU3RmuHeCEl8QXHydOD-4gOoSyK0hpblX3pEMxUdX3fDOdLK-nBOwIa7XZa8cUQc7GBwHGvSZ2kY4blcnngVNNq0jaJfgQQR9ySOZovSO8HCv6ZZWjDqrokQjsUJwCETRDQvelSg479xVQr3DSx-Mk1CXmR01iKtc2shsxr3i2pPUMfR0kE32J9xeKKCNKiAt9Sw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AwalqTfeNImbID6NJM7TBtIMQNCN01QkFyAnVuR3WugvI3gBWUHiFuFNDtVDiocSck2kpjou8OgJTEp99hCJuh1C47X0lTTtYHgmaqGxZEQEzWzKChwV9mvY3iMRqpGfieasYBMNvmf1QGe_RQfKSMhrCb2pK1HseRaOcW-vp-xKSy0JlSjNPDQ29pDBY5UGjvz-NxBceeHlYbua5TeGxHYMeBENZUWZOu4QN71A_8LyIYow8HlOUm8MhNpiYy6LGl4XCt5PpKTQ6xMnFwyu3G3QpX7Tnx-G7s9TIDEF4Wnwy8-BCHLoLybaT9tJHSryDYSz32xt3TtTdefKjQtmcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CQpdIrg3RmV3hcuz-0iPK-bCFEbWTd5FwTLSs-HEgrR-M3t0nFTD196xKUGJzqRhE98RsoKRcv98mJkHJpqJTyRslW4oNsGrtKjk_qPbyD5YutvcrCuXPHThKQxmR7RrfWl4Ku4OIhedfsuniz_loW3xv7TB148HvhG1a83JLe9jLv36JIYt4ioURRb6EP4UveU3GwrRvbtADIWgiOjbL70SVpOHmvBiA53wDv2_yQ1h5rGYCUawafGbWEP77fiFAaC0SQvkAuSF9MiBzmQ_fvw4hfVcyab6U4eel5kYezvyvc100DcX4LoR2e6WVpVr2m501vkM2FfWr1dxw8hAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hEbomwWujcLUfrslJaFNudYjVemTos1BymHSadhVQQxVwyg-RJLgOLZF6Dj1tcbSelpBdSS3BpEi_5yAW0R89VCMI2F5xLqhWfTA02EYjepoJL43G0Film5i2PutMjJoJYZQgTjSu0w1Li329tCl3_OQ9OUdkKBxuJL74wuUEBJGimdSabUBO_9waUwj6tqd-oeNyuuqQCxK41l-AJ1pClHCcEQZ1UV6b5K4CbOd_QLAj_eml0o4AqpuCSHJqlgZvxD94sx3QGj-3QlHW7zs1Sw1QUc3oZe1WT0simqgLv3nsdBtYQcytkqw7polzwKqnWFYRjnbgKO4c7ALge78fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a09f2eV8IUtPRvkuMWRsSEvCMsTwLceJ1lWOTmu2H_vph3WpIMUXD7mhab5tpRJ1wYDyn1ZFNj7q22QY_zG5rQrwwh7eMfBkMmh6iqAAd2sUnn9SM6fI92_dRMb4AOsyCURCXiLFJINMHCiIjSLAjh7n9pypvINGpr5oUv6SY4HZDvG2AKYPrSXugibQwsR7lfL-B-f6LP7N7hjcr4hCDHoTamAsnRYQR1_tSgzrPgvZ8J2OjLsh9fla76LyF7fj66BODLClxQQKhYop8_oPorckBS2aREuUv2750dzpyTti9vq_VIw_K0_V-ZsyLp4i6_dTpj_tFpQKONjZUK_d6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eOWjC4mwcfsVU4X_mZlE_U_mIZVDpEnHbpRM8UDRmcjXfuGbRPnxXBtMu7WWhVggZ6k9phNMKyQHVGEYIuugqtq2dnrifq-ytXiHHzagWiHfd4zqGiUtXiDcDJtgYOyL7IdEPaVdhVWKFYfG_uAxeMVylS_GSk0PPK-TiQSiG5WbKAvp8c7LW6rGOKt4Smy1o8qE8s1EAB2tNdXZeNTWZqmQ1of5da3Voo9SsG5wFKxCwfL0G6xvZssr2Cpjwq5KB5oy0ncxXZmGTaVOXW_URoKx0CDma5hewyl0vuHu9b0r5fMasZUZ0jSzJaKyBe8_heDvVK0idlUEBmGg7J7wiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معرفی GLM-5.3-Flash و ماجرای Ox Alpha
شرکت چینی
Z.ai
بالاخره مدل GLM-5.3-Flash را رسماً معرفی کرد؛ مدلی با ۳۲۰ میلیارد پارامتر (معماری ۳۲۰B-A18B)، لایسنس کاملا متن‌باز MIT، کانتکست یک میلیون توکنی و قابلیت چندوجهی (multimodal)، که به‌طور کامل روی تراشه‌های هوش مصنوعی داخلی چین اجرا می‌شود.
نکته جالب ماجرا، پیشینه‌ی این مدل است. حدود یک هفته قبل از رونمایی رسمی، یک مدل ناشناس با نام Ox Alpha به‌صورت رایگان روی پلتفرم‌هایی مثل OpenRouter ظاهر شد و به‌سرعت بین توسعه‌دهندگان وایرال شد؛ در عرض چند روز، حجم مصرف توکن آن به رقم نجومی ۴۲ تریلیون توکن در شش روز رسید و صدر جدول‌های استفاده را قبضه کرد. جامعه‌ی فنی با تحلیل نشانه‌های تکنیکال (مثل نوع توکنایزر و کدهای خطای مشخص API) به این نتیجه رسیدند که Ox Alpha احتمالاً نسخه‌ی آزمایشی همین مدل GLM است، تا اینکه بلومبرگ گزارش داد
Z.ai
این حدس را تأیید کرده و وعده‌ی انتشار رسمی وزن‌های مدل را داد. جالب است که Ox Alpha پنجمین مدل ناشناسی بود که طی شش ماه اخیر همین الگو را تکرار کرد (قبلاً Pony Alpha از GLM-5 و Hunter Alpha از Xiaomi هم به همین شکل رونمایی شده بودند).
از نظر قیمت، GLM-5.3-Flash بسیار رقابتی است: ۰.۱۵ دلار برای هر یک‌میلیون توکن ورودی، ۰.۵۰ دلار برای خروجی و ۰.۰۳ دلار برای ورودی کش‌شده. روی بنچمارک کدنویسی واقعی (Code Bench) در همه‌ی سطوح تلاش از نسخه‌ی قبلی (GLM-5.2) بهتر عمل کرده و با Claude Opus 4.8 برابری می‌کند!
از نظر معماری هم ترکیبی از MoE، Sparse Attention، Linear Attention و لایه MTP به‌کار رفته که باعث شده حافظه KV-Cache به ازای هر لایه حدود ۴.۴۴ برابر و محاسبات attention به ازای هر توکن حدود ۳ برابر کاهش پیدا کند؛
خلاصه: هوش وحشتناک بیشتر با محاسبات بسیار کمتر.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OSvbRPdfHtotyXmWEOplUXPe0c981qCfBzjrIBBLlDFyoQoo22qJA5WAWzTsCmS0piYDtHLNWUgUFb_FY5XmDwONNZduzOpkF9-PTignVj_F6SBzepg1--zemmz2RzPWhQGKe8JfZYSBmrJUxgNpsCTdB-mkHyHPs5zD4XztZtaIGt7aLTnA5KcRegBjgK5ansagKYzWNSOig7HCINW19tg_d_HzfjaWPILac5sMcQ2xn3_DOifixsmFb2AHA79N4rzx2mkBjBWAwZcXk81tXV08hFB0746iG-COgLC662Qv87wCK_o_XBG86G9KvQ-qUil-35FdaX1iUUjHqME8uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k1Nu49tjggzuDoKx-KSZUfnQhyOvu__wf4zeNKDbvl5lG3imkNVNrLzy7jmj08SUDi1ku2-xuU4b3P4glf67SFhjCmAOyfepLQ7TCgEnZ332prsSowZx4zxEHMaoAM8c94GTmfTPdu0K4HtwzadEwtZTlZTKp9naow8KKQce0C0OyEZOYblZU4QbWXwLGBeaa6GV4mjV7FKnQ_rR-wAEzj6dO_uhPeqhinsv-KVB6cV3_DEWv-I1h7udPfaJQBDN9aSoeyYSRzXHhSC_d5d1wuUweLjityyIXc-eBjHueOE-vSkQPBMx9xxCxnnLuf6AyJ_-ho6MFGxYzURooiKRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AsFRxbLWHlV7NMNJmAqWlv52wOA3n_vGGXPzbqvRg557wKnRLHYj3AdjSdYJ3LftnrScL8YPfntrfwHJuwk1S_pM9SIKpeenUkTPcWmoLK1Ds2qnIZujf7vJqxPK_jPkDHRThVSSIgGGT1Uf_AzxPdSLM8upJl4WruzdrCzvve-Atn8jt2Lp5-I3Lym60xEYQMx-F79jT3agM2PT5oWUiaBZzB7_k9mzzYK1-5_rarXeX07lBmEHnUT_YfseLulzty3UIS2xqzNrNo0F1KLqjpBfa5ncNOZWWl3hzr1BGCYRT0ZufgVfV09o1-kmGD8rYOncq7FQKRwz6CNgFROSRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lkde2Hw3DTnGtXrrZaIZ5sgnoVqOo0lYe55GQYdn1JtRJcM8PZbFPspMJhmJvyqdRLqnM24rvvml6nIhnU7d0g2hEeR_dOyDpNLpVPFYtEEw9mAiEOCLLfwPXwlk0rwhI1_XTsoeUHbMzxc7xC-zQoI7-jTHbBiuoF0YbIsiRXsX31ptFXnPUGvLR158fLLsdhw8ZZdI1WAJUFdmNYJ-vwXQ_I0112rnt2k431RRKFjLLU7sh74moW8R-3yIAVYp65xGGuczX3_h7kIp3KY0p2EuYLeSFrvPSumb3-KVnk6I7l9r0hJQp2PmRLc9_HTqMvZt3XnOiMLIzHj0Rb0fqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WtRoIxPeYxIStEBoPxqz0nSa4ZzK7nA2yei5vb8PQnF3o6aC5h8Wfi0BmV0tpkO46o_5l5Ha4YMVo9rmAXh9AxeKzZ_v9wPNXRp_rEj6vD-93EKkFGpx51I8ScDv2AeDqU0ESle1eT9zWcSBvkMjrGvVVzrGOFBQet_NV-Oub73ct-D9drJYwTc2OeHJHYNJQ1pMyQRZUU7U8tcvDbliCMlGujNSe5GA8YpDlq8i7LTTMEgtfgRTDb3vKQARxb26GpIVkfekILTjEsKW_h4FZbASbhg3RXEWMT4Cu-YV9FjTQk8lqU_6E3ZifrX5DewEYnAXB3Y6ZIkhD29EciPRhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha
با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.
هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha:
https://youtu.be/FIhoccZtpZQ
برای شرکت در چالش:
1- ابزار یا پروژه‌ای که ساختید رو همراه با یه توضیح کوتاه و ترجیحاً عکس/ویدئو ازش توییت کنید.
2- من رو توی توییت تگ کنید:
@MatinSenPai
3- عضو کانال اسپانسر چالش، Lira Candles باشید:
https://t.me/liracandles
من پروژه‌هایی که برام جالب باشن رو ری‌توییت می‌کنم و در نهایت از بین شرکت‌کننده‌ها ۵ پروژه برتر رو انتخاب می‌کنم.
🔥
🎁
جایزه هرکدوم از ۵ برنده: یک
شمع صدف
و
توت‌فرنگی
از Lira
🕯️
🍓
معیار انتخابم بیشتر روی خلاقیت ایده، کاربردی بودن و کیفیت چیزی که با Ox Alpha ساختید خواهد بود.
تا فردا همین ساعت می‌تونید توی چالش شرکت کنید! چون احتمالا آخرین مهلت استفاده‌ی رایگان از مدل Ox Alpha خواهد بود طبق گفته‌ی OpenCode</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ISsAEyFv4Iil_EpeWErKIYtSpHcGdnrEvYHOO3LImpFm4VwtJnp1_yndmkdFF0uNJlhCEkJtE0CiBzLUejYyyc-QxEX-8aj6XXht_6b6uhoRVvZgzCjB0ApOKxb0IqFTAQB9wTbaC9IKf06dlSgjQ6QTbQVsq2MHsXbPUBhzBTf3PBu-AhhjIKWG1qFI1XZlae_Bo5SJ443fWbMypZJlkulHN4I4DcXHm5eyo1hOo0Mv6kl_nNSq0nIpAe2wgrO5eqAasQTOkOPgAm1ljobSpChA1pGDQAZfdPCix0e4VAnfHczTQdKPiXQxK0uhavz8abm5pxu0wDx6nEEOVOszpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=D2tworFqGeuhGyWzmBRtmyDmcwUtRMUOHkc6f1dwfhknQhg2iOZov2V5Hm9X25U1rZcKh3TVvapjQ9yDWew8OQR6c7XSq6kKPHzBWsyBBvzGTKlpkMeyhqVLlu5BZN6YU9axHekTk5GaEh-cKtBluHIlozvCobVURkPPUSofN9BYRoLUnlK91duEEdos6h8UGBlg4_DrHs-MyHt2tTvd4XYnn8cEO2vARGMOiARab_GAqbb08vuRYo4VHUjRmJlf_5J0d38JrvbmAh_GPLc_n_LzMEEaIMC8Zjcv_xpOUFiViNdviJIzqM8NIBASi7bYtrH1BAJWnG8vTzzFQiEKybXcPoqfX1zNif_XYyIpkCvjL79CEGsVg0mUIYg6WRQFVn0JrpqvcMV7g9sjSuEWuSzIdfi34RAr9W-KegDWvNJHP5156fbmuuuUlA8av-57sUjX7NAbfZ47EUbJeFlGFBOdo_wjCwWyVXceeIn4A0rlV1-JyAiC5e0Q0dvTxHFOUasBlEsSHXgW3sB4AZuMdAyjE9JGXwXloN22FHm4ph7KvfofmPb5wXhPK_udBwVM_akPeiL39hHrIANpBHfftpV9JtzZtqsoVtEUChoTL1oFYiI4DPkIdsQ4qbncjcBsvPmjFVxoo0v_oON-ESWIFg9Id_CTovgmC-cNmJxp1-U" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=D2tworFqGeuhGyWzmBRtmyDmcwUtRMUOHkc6f1dwfhknQhg2iOZov2V5Hm9X25U1rZcKh3TVvapjQ9yDWew8OQR6c7XSq6kKPHzBWsyBBvzGTKlpkMeyhqVLlu5BZN6YU9axHekTk5GaEh-cKtBluHIlozvCobVURkPPUSofN9BYRoLUnlK91duEEdos6h8UGBlg4_DrHs-MyHt2tTvd4XYnn8cEO2vARGMOiARab_GAqbb08vuRYo4VHUjRmJlf_5J0d38JrvbmAh_GPLc_n_LzMEEaIMC8Zjcv_xpOUFiViNdviJIzqM8NIBASi7bYtrH1BAJWnG8vTzzFQiEKybXcPoqfX1zNif_XYyIpkCvjL79CEGsVg0mUIYg6WRQFVn0JrpqvcMV7g9sjSuEWuSzIdfi34RAr9W-KegDWvNJHP5156fbmuuuUlA8av-57sUjX7NAbfZ47EUbJeFlGFBOdo_wjCwWyVXceeIn4A0rlV1-JyAiC5e0Q0dvTxHFOUasBlEsSHXgW3sB4AZuMdAyjE9JGXwXloN22FHm4ph7KvfofmPb5wXhPK_udBwVM_akPeiL39hHrIANpBHfftpV9JtzZtqsoVtEUChoTL1oFYiI4DPkIdsQ4qbncjcBsvPmjFVxoo0v_oON-ESWIFg9Id_CTovgmC-cNmJxp1-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نکته عجیب در تست‌های اخیر کاربران از مدل Ox Alpha دیده شده که واقعاً سؤال‌برانگیز است.
همان پرامپت روز اول، بدون حتی یک کلمه تغییر، حالا خروجی بسیار دقیق‌تر و جزئی‌تری تولید می‌کند؛ مخصوصاً در مدل‌سازی سه‌بعدی موتور Raptor که اختلاف کیفیت با خروجی قبلی کاملاً محسوس است.
اما سؤال اصلی اینجاست:
اگر پرامپت همان است و آپدیت رسمی هم اعلام نشده، این جهش کیفیت دقیقاً از کجا آمده؟
آیا مدل در سکوت روی داده‌های جدید Fine-tune شده؟
آیا وزن‌های مدل یا پایپ‌لاین رندرینگ پشت صحنه تغییر کرده؟
یا Ox Alpha واقعاً نوعی یادگیری مداوم دارد؟
اگر این تغییرات بدون اطلاع‌رسانی رسمی در حال رخ دادن باشد، ما فقط با یک مدل بهتر طرف نیستیم؛ بلکه با مدلی مواجهیم که رفتار و توانایی‌هایش می‌تواند بدون انتشار نسخه جدید تغییر کند.
و این، از خودِ افزایش کیفیت جالب‌تر و البته نگران‌کننده‌تر است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
