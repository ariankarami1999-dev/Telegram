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
<img src="https://cdn1.telesco.pe/file/J9NhCxNyTi8ec7ZC1gEhtyig-YVD1cJiI6270WLwvorfb-Cl-AxtyBhVKR9ksCYj7ECTpVFAJn1YpYyVRwpumg_LP9aW6YbYPpSxMP4fY3TetrDql1xKUnJABSiLqWt9Mwr-O0oq_wFdev7DE4OBpUA7jmPVJOlED5btkE0bvhpgkd-Nwm4XgZLls2PcGM7JFiSqrE136VMbWNzyUaAAE4g3bAqA4hfKYs7kbswfDBM4om7kOnrqrbBwuEUI3EPbb_oS2LM1V6LMsZlXyx_llW1fA5yzNo2MYD5VC6_gv9ky60cVhoBj9elpu1jSK2kbiRRu_pcZ-mVpYLGbjyZtMQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 15:40:45</div>
<hr>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OO6Pqs_RBpSSAf-6qqn3LI5vdFiyldj50D2h04dKMkShPscueeJfckuikVp8IQAAnT4d5H0e2O2LuhrBHJpHSE1NJUNnTwfKd5XqqNNedaO7b0VOi2N9f6gdzephi46JITlluGCP5NZMwmhrllimBhIQjCEiLadQyeTXeNoK6qY5HVM-Z095Sq8Mv_IqSCeaG2Q5XaVP5BKnE_aNWnsTIGq9PdcYLPK9foz-sH6m37G2H2PrJkJYAbEO4s8rIEjF_y94LidwuHhZ81XMfgTZvrItFG_gWYsLyGoDz6KpEVXQf6Sf2tzePtDCcabVGBbNHXII9WO9MkTip80vSImmNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ewZnr2vMNnwdbniwjVHUpjaCbmiXiWj9N8SaUUm-2Q6_u1370fKAPZEVIORGumfWiPTjYlQtNNXP1F5Lyb4SiJWd7eDPPcGFYCY0FF7HIL4mFSZ15Hi6Vx5vV8ceTkXOmTLtuxV1USZeDi9avuwjzB4dWXCjcjqW6LKy6-itX5anqD1IPlDmpx8wrftdFRxAK44JmkB8GgnmJwRnZTBcAS9_9HLe16AaBQm3dfSyKX72dnfV6T_V6KjJSvGxjEkIVyVUZxXoJU7wWmDuoa-z0nHZHZ7hrCj_6L2i_y9iwlgknzxiuobBw8scMUu2FmWkgKhb6qw5GYZ1pNhFrJLpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QGlt43YaUNq6pla28MbEPdttNsxwKnQQ96XHJ4IO6tiBeP3EOFWX1K8RQQ0XwUVH6_8RuXqKy4YLqHfY9ygCdfoSGJD1NqvonOxqz4HvnmtbVg5Z6I5r-csBoqRgOKAbv50t647zsQepEZ9l4d-7x_xt0QAddaJx1RJnRcCAFOxHPpWfOJfYS4C5XYXCaEvmP07Z2tq5NhQUktLbj2FF-9EToluSzJt05VbpcinxsYegcuqNafp_fX0jc0Bx9lgPCkRWTT4yVovDUSvJ-yB8L2JT5FCU_-ZZutfaFma4YAf19qCaasiAoPQd_TFG4Ftqkb1PRRxmhcenp_pzKaBUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LEdzTnBz7YQ4rvlZmuTBxaHLuP-Pn_VGFqQZfFr0KF7KJYiY9MeIr0CtwXmMesPgzdAhiM_ePnwJgquZZPQLXg_ID0FPUpe6JSTiTuZK8vxEP43rQj1Ol-nRMA9PlsSDTux2lq97q4MQH5xWcZFl1BBypmdov6pca-qWI-AplXKg8XU5ewxR-qr7E2vMb-Dz-AP6tbJiCcVIL-9bKjkXgBQbwL_CPRXgIdO3TgFhRL0p6BPUQjWxV1Fb1II32uPaLB9GOA2MUUaHMkcRXUnhoZ4LULpYGaZJ-lPzo9BLj5DqDpsWSin0UB25L85WLlO5FJesnuSBGBT2JEK4GTtUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zo6UaH2H0dGgeEKBrMyiS6i1U3Y_vEZYnEKMxfEs6-VWw1Vsm-gEdVxukDJPFdVi_bFvJlI-8VplsB-RoLh87hcwPH6Fs1txMzlBcCA5qLaXuXoA5FUcnrYGxvBs-B-ZBF4sSWFzVjaZLCNkUIZJXOgTGgUDEsAVOAs_wXmEGB1kTRTjB0ma8kDlwcptTURhVCmQk4ssdyeYw3pWxN-SdQftiur6lpK15b7vfM_idIrYNbwUTCVxv4yUCMyM-Zus6V6jHRKBhnuZB8lyqvjcXykLPpxD9LUtOAazDTd3RTx9OEMvnxlY5CeTO8igJwHAwXCepqYfSa89ljzKfbHFHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DXP5eWAEXReKvMoFp-U3cPGH4ODV-PX25kyjLK9ZnThMT02y7YUQ0OzaWaAVR4mOx0Gie3uorRioHyALwEHaHWnpZIs2cY3Y6wYfu_XAVFyHeh79elHb2mX5PG13wEzgp6hbc_IMic1gWlRbJHVUEvaCkB_3wQnDwQ3M4WVx91J7AMaIQt2riwyZnPvtWHcgcYf2lCBRteTYhK5aQeR3bt3P8At8WhFnp_qVhZ9oamtv2Zv-PM2TjOR52gHngbTH-uRSHqOrIlIH0CvJpdkhhXvIeVdN3RmpVntfi2R31eBZ6SBQwVlBS0M-7q6xBXvRa66rua51tQD2-Qz20jJX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vhnbMq7T21_hdvJ_C8vWbbAAGRvFRf-5wUJyXejd_nA0D7TlxZAygSJC5q-Ze_YKJYRqTN95BKnYYHlxMRHnFrteGCd0C9O7JJMvF1q5X7AaulWxYxyBlJl-ofA2TiZ60EdXQmKdmclbCzmdjVLJcF8KRHfg-D9dhfMp8B5qDmrX3-LvVOqqEqTlRvj54cO9zFajj6chGUchgcfqK9aRZtA5CMWO7XTTYxlBrm6Ji353pzsw9Rd6l_lxObVqQs8suLnYea4Mb6KLTxeLNZSCQsb2_IFFzNosn2pUjE1dWvz7zcimfwyhzrPvnT2USSRKU0iDNRAVACwWLSKGRds7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CPxfXTueRhOhDysP9AXSW9ICBzGMiQ21rBytr8ldkKCNTYMV3SRsO3LJkADJ5Y94i5iXPhbvZUzwYNnp1YNJGLY8NP3xvGhJWg0Dn1Un_zRsWiuaiaJ5MPKdSTA4rFvZxnrluCG8XajpJPYaxVfLKmGi9hTmSnUqUkrn1cen9HFQFvKHU8u2Sha-a6tyy3F45PlzIhSfjhjt9HwCGYyVLKc_xCvOBBXPvKCKD2f1d5d2K2XT_GzQyPGoBPtIwPaa-fVjRMy7AhenY4VrIvt8odh8s-EC5hpgeT_npOQphMHaPpkLVq48irxuIpFmXJ9WOXxfwn1-0MU-SLE-1EDSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T3bsJ8S-l0FJW-3KUNZU2IEHyQ306F2oBFY98wwL8Y_ckJQPUFhB_NRCl7YN9PWU1Xc32I6JoItZrrDlSl4NtjLzoD2bsU37dwQWEjfYUfqOCmueGs4dP4V8vcH_cCxldj5s3_JSZ5jOw9YErwEi3XrtUIE4-mqdG3afCPqNy9QWzsevV8YERQ2eNSVWUHM4qXqEpFmpZinWpxabnl-14uPH1-bhajDfTsQtsI3W-qL1kKVeDtFGuPj__cvri4y-q2IO-NBqLsIQ1DZAkZtf00QTrlRvse-9la2FX-7o4SLs9dBhgjzG2Ayp9ADFqvCm2WYQGnXYoNTp2FgDaH5wyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ow07qmSplaZ8TmcPZ2TST_Hy_73rCb6mkNzc8msV3lWjNFXNld30T58oOTYtkFKFmDb-qzpqroc8EQsovo0d9dnyeSjD7iuIrdq3ePAWeTciGKGSapIo0_AMzK_mQKoGMPfckv59lu8iH8qg3ZAydsEKiqFQusBPHLufG05pQTtUvwm6NtxTecMT22nQ6Xg9_eWhTt0Y1RF7YlTO3JjiQbsMxjrbdmTn9pejrtTMVFoR9Ti_XXdEjPhOfPxg2elPN4xAPOZFI0cHbDCw5bzY18XkHEfUwmYRFNRAvBYcnxo6wAZnGJhSvAyjigqhr9XamrXMThD57VEVgwn81JQwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o5rfT42JowguGWvMkMEC0eKt2fq-wi4Kej04i-HL29v0yE4lTkswX8QDsXWsaBaXgeEYTvGp8KXa4RgXLYoZBgxQO139Ra-0JzwjpKknqqktVn1lf2J-EC8VM7EqEQpYgNmw2GQMkeJU9w27hWwWYseDf8MrXC56O0dkfXardgaxIeexeqxY0lAwrUt3nq1Ml8sVzLGxDey3uEJNUJBuMd5p5EPlifBaDKcbDj_i81YiPgrr0FcGnc560OYuc-0rJyRnCDXABLC7cEYW0dknDothsXLXE90CX5aj8Kw5lGbS1nETQYzFVcP-FeRgiLquN5cZGg3nK3z4PvuFIv5Lpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VPvQpDGe1i42jZp3EyGVYgB0L60A2mmyl4jZu9f7ZNUJdhNAvXw_j5XYOByM8ujaPepl9mvQydN4rCYimtZGg59V4kK8dYi2VoYDVpXZlhkls48CjMKtx5kb6_1HtsSh7hzEUW1nztsgCBu2xz8bHmuPhYE38QkpMABEFJd3gwAQWBu_erWnbrIx3fc_iPtbkP75LieAki_GR5sMl6GGpI3xfXxN9wa2aUQbQvP-AJd5Ft7xieldcwYIwF6zPkA5TOviQ_WN3AtejLUZpBw02Nipg1_-zOmZDbjrPXIX8ZfwWpbQi4CgqdlkNPW85aQBF6u8ND8479sf_1b-8NvNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uhSK9X-EKzxBLGgipGZXqLGv-N0RC0m_upd04N9ckScnVzI_pZUgYu99IPGBHLVDEEH2uC3IIenoPuHP6r0rj0atHamHBFRFoj0uiC0L0PkUvAC9ZvRodimm6tVn0IaxDlayFDv80BIjKTj69RRNjmHmwNHb3NjzLDIwyhcKpBM-FpJdKLDaTXZRa3FhGk2ci8LXY7VcVV-WsdVtdNWV9-rKKDxI2oWrHD2wH9hVYK1kCie0MjhgnFRvmbwRPq3Qa2Dp5xNsL7iuQn-Z7_we8xmi3x08RSgNAoFSZWkX4zwsLrMW7GaOaIcCRP9bDSsm4c3l1fHUKN2Xm_PADu2U4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YGEU3PhXxUtRUlDIXDA56b7CuBMYo2wMm6siV_ceaEGIns7uuymYF0PjMrnd2jHjhhC-GN9pGv7lGQOZ1OkM9PInFV7AC6MRVU5-y_T8KLwkVIK7WLsr7NIDgGWXH2eXHl9woxP2ZM01op2X1IkfECY2zJ7zqr4kQDNbg9vHiSDh3r8TBeqMyljgKRv6oXN3yOwlICtgonfYmIuq5EMmwro6wBbTYJWZcGuzUlz21YG13rryNbjXZZiIS-qdCyYVFeEbEEiLA-IFWGnlbwEy87eRViaj5GXLy89GRuvbx53mD5d3JQIc0x7eOUg9xDUXa_Bb7mblsO4K-DQ1OgmEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6M_t1BwyahsM4n1BBAZh8gJlk_O86g06JjvzEiWrPX3XtNBh0JTeh0wRm5shn5qxcSQc5iRkA3pP8yEkFi172c4rYQv5UQIOnfCpmLDVC02ZhIe1hnaArMjxgc3qXtoyYAWsTSSR4XRGowAzBWxA2KGfxPDqXNpeVb8SCrnvPfYlOOhmidYLW-pMvmjhP-0z3xrPJcHBU0hnJxFGkVCYGAeZdspVv08Kb30PPd9xcKUy1ry-NmwfUTe6B4v-mUwsZxCAQnbGyq7zb24-rpq25BrtfyggFzmHsfDl3FdvkV0dRCDL3LpdC7vel4GvcfEqQmr3Qz9h3JsvcxWA-9dpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGL5qn7MQLo7THDqS0HY-4DTU5WHfNlwKoxdcq7FRxXt6E8r1sCzoRFA0mLdMKNfKdzzVYn6RPpRf-IDWtOSXhEK0p_3ZhSaDNvaoi335OoBrQGB7BzZ0a_6oyGEuWJRLD-jkd4wtcfJYnVNraKF9RsH7P6X-W6D0lmpK3Cpg_DLEz5-GtSvwD8Gc25353plqafUYMcamQsQ7IondNIPRAppdE0nud8fPfCP9uONkJVcwVabVEXF03IGElkW9YaSm7rMyZvGXySw3TKs03KUHYo7zfJfcadqe9mNyBLv0X6o8qKBPUzNlD8rSbFg41pJVERp7zqqQwTw6Yb-yTCpPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZjCqR-v8E9GhXoh5FdLRVHTWyJQcxrbO8ATB_pwXmNeRuwaEzNNYHP5zp7tUfU5ggPR5MYs0QET91cKUFU59YQ7Atird8MmUTb5-6riLNMyJ8zTWbiFwrGC2o-hVzS7Ex6JYrzjUK-itUygP1dW4zzH_IhRg1IEsEQyGxjkf80cIhiFOFSp2FR35WMpjUcM4yLbucDwA8tCkoD0SaS-Umyu4o44LYIqrNOYZ_NqS4J0H3ExPw-AsP0ph3eCvN9EQmWwnmzbZ3XdkFoakcYZZlQiu4jf_st8R5OMShOQm-JnSGHFiZIZrqXxqRcBtxmfoz-IH3IZuqTjqFaexKX_KHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mT5b_2Zrz1yW6tv4QOOYwbbf32lnuRDsfQyLvJyLd27HNSYH_BtHY17c5J4T-HKhvDrQNqKxa9k9nVKfIhW7N1mifqe6bvEm42nzcPYbZ_G085gHx9nwS742RypxVJkcyeWOV_mEeKgs9ABmXph2HNzWmSI4Hew4yfbykQMuJp9TG_ol-tTrJERAi7NySsVELcU5sBDEi6uce-wEvc3-u8ryoAE6OF0pm5N_SCN1mLA4zfbj8XcnUoZhRqxtgsIsvKVPToNAlKk69eIsTXxrsfEr-xRnJfV-67ywtlnAvwIt3x0huYi40rqb8_rAsKnAYim5OMtpJyLw4RsWZ8itBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hdmP-oAzFLo1LpL1h_TWKIt8IoPBFc-ORJdkaV8rJTu06TpkFeCmMTjTJtcX15I8HLoqgAg7KoSZe0Mu09RxvYl0lVQpXEtEu9vrXZyLrQk6YIoYzRD1-Pmzf2St437zMEiXzyFzpPgWXQkxk2AXRSuCjUsvhx4PELP9f46u9fBtveVv2eYwhGFnvkAeVQxmGheo0of-pFUijPS2rVMP_QS35tzCXXceXTGAGwuVGhEMwR6XCujb_ZzQijgGnlSXTZkJnIiaiAdiLKw0fIYxLZOqG8RKnshT2GCBr8dAn03UaHqx30D2idXVceQRjbh_EiB9JEhQZpA3h8Awyd3fTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ru-F9Cvow6RO1iWBwf-N_iuRZ3WuhWoUabf_ChWsv_PysCKN1q0jgoIiaIkvZiAEUQvvc0sFtgfIlyf0uk--7VIlWNaUG6dmZfYyFo0q1BIT0hiTPAiVEvmKpHEtKoo6EbCO00bjEPicwp7XdlqZsQXuxMXpxhDClZgkqHaHY5RLI-1avAvAmDSHG6gUQcoVTbwuWo2EBnjY-57Y7V_MPHA5Cv1HIiNzdwTQmW6ONnk859Xj78Ct6hs_M5Nctz1vmK9DRuTet63PjL1Fu989U5n03w6y2O9LyLfaFCz_MMeG-rmQCsbBgtKgXtkNQmNA3cUnnT9AXG9i0O7_crdOpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MmDBWCHsOzf0StG7hDmUkGmLJZJwEbnYVzk6RTvhlDecBxYBJH3bs9bmdFfJaZ92Vj0mec1HQMEbH_ENP-T8akrYevsm_dHXw6eOM1qaSP311ZF4r-XpOyFFMqWEW-ZraYx7Q4Le_-ApluNJZeEW9M55uY4bqojj7ZvM8TTfNX5vE0Q37Po6Yu2O0eZz5Gew1BFKAwL76HqHXfXQ3dlx3A_nNtExoMNCrlg5u2s8cqyCrcliPZcLN7K0TAIs32k54M9LRV13NhbEfQpQzb0dwFqIR0ICefK120Ox26exwyoLa1FVaXg5BQXhVKKZd0ncbUM2gbF6M9NdgFWDsQwR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a62j1_HAwwVqhoxKZByfg_S2zWSd45fHaVXW48x3Rfs36sCTJ1UgcrHSgyf9GdXrmyg1XK16lf2eaKEBfi942cVn5rLgxzzF4eV41HN2aCZ_dp4StmfrV_G2FxTC77fhCGeYrvfGq8KBZ95UnknrRAb3BgTthIhWF6szzjg_g8Lw06zVdjgtZvOYAYk7K4SDkzOOcESlgG9gsHgSKAEmgL1kNwix1uN5XSxK8x4SqE8PFGGabAnia3giUnG1Gj8KslHeYcItOkJ0_4yhYu5LDJpE5lLBT8EuCvubnZ6feI_BmKiCrvnYIGe2hWh5yci2d5eF-y1VgfHtlZGYJ91pjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sM2uIdish4d9s24_onxobN4tQ-hn6Twnksct_0sAlBqztDwXsVatNaFm_rl2CbldchLX0ivE1TrWlBUC2Fa0H5iLsKPXeBJAk4UpqIohV7dVkaAQIBq-sv6M49EEm0tn-OFWqD_yHWjrF75c40JHR1p1O6u9sYbpZSoRkeW70U6Mv6BJbLkR4Gmk4Su4Ojb5n0xo7kV0hxWuvVRJ6JTR6c0lEf0KVuvPL0zSQzYAat80fPSQaqv-PSKR8bQ5uX5OoFbqPZK4Z22kcC1zMsQvY2hGvZKl8io-A7ybGVaiLZCmTZN0qEfgYT7uSDrTtf91ApoOUv98dcom7E5kE6Ci8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q7WdU92sk6IE-1OCJJ0ygOaHqcsTErxTaI8MWzZhsaVsblzZ187nJKap3n0HRqIoqy2bWwHA-_stc0XElcVXozvwxbIjZx-tbGQTI7nybwJAvwAStnOVpaEyPyEBidsRFsghlHfdmfTL8Hjq38VZ4yLJffKwXZzpUtSWd2ss3DPJF6esJoxBSxyCabsdiBwn7FHYUPHWpn9aU0bXTE61dil6Ja64cILN3GSuX9G6iEM3_f5IqQ9w4NRKJAmbLxnVzxA7Jcy13JJugjNtBJqrEVyIwsNLfWLmlf6W2WJWc6WFtxZyV_yn3QFFe_wbNsspdh7c1XYArCJiEmmfGimE-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eyUGjsmEnF3eIXM71JJh--V-pQjYGnXrweuc0b3AV46I_TnuM0qN7XiHzLzhzJxvUe8ROZtdha-zI1Up-z2yYmW7OsewLPTzJW0kIn8x1m8WT00LAAFnaMLx_O6_l9soUoRIhxhFBupKqt6XQ3GaZ_ggQb7RdKdbTuH7JBy4RtNFddK9pQdyXo_UY7YCNZwTu1OOWpStyxAQ-EBPxTo1PCovyMuNRYERI9loxxe9mLMXYIvgZl5Hi_xUh9I7zuiGpR9DrNt_aCc0XLu4IsMzmmyj-BcK-1_0xFxIpRd4OB0VdbtQqV1h_kXGdwPvW_QUsTLf0SlJcMp88Qx3rlaPdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BbGrOusRF4U_RmnnBhOHa07FdHEbJLO1u3uw2-aT9882ZyMXKq9155wdrFejazk3kr7KfNV4-dgsFfzUUFYpt63K9xNurHsrFotpFgzajVqtsu-IgyGJqkyMruJleSkZ4ySdmZ7dogj6nY4h4n8rioGmVNPTmK1jTG0zl07Eav24jA2vbLaaIno48vqDjJsH-PEQ69MTSfi2EbG-rEi6HLaxL-s-kQ-oTxxwfJvt23UiqabSKD-Plizf0DRTLO5wpLh7kYUwgdPIvf-ctjDnk1gyNAurgZfJ6YDkZOqdvpSYWlrdRuEYlImOlg02lKUKrGihp5PV6hVdvlS8eGWXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DNhShDyZvcCbBRRT6gsHc-1zVCypYzjw543KSkI_qRZzcWVsknr69IKswT0kCLXna3b9TV0_c-VMzlWbKsi17gxmmmDmAWMHR7-ixeFsvQnzYkeJWGliX1s7YTokHhHRqaLr97BNFjBeBjH64EJU1QK_-AFb2hrbgGqzV59iEa1eX2Iujc4gN9OpFEkY5UWdR9yMKgjFihrP_z9FzzJ_TKSY-Wzai4ILoVtDSqyW5N7g71g8AKiTA4u3K0HmzvipV4T2LG9EAxqTjHKGC_PfXp3nzwIkpHnbwn25BNNW64KcXebAWIgEjxDHc-5XdGNnllV1Mi2qoALc1P0PbuSCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T5DEBjUAI2aOWa4I0zneyd6iNWd-OqfPOxhciSwv5ZEyG3_jZEDbakIU6xMAhSZc4bLCtNaatqf9q1qrxOUrsj2PCqJl613Lpz1yRPStL4xpMOgpbgQsmP876Sj_hz0A5D5Qy44ua8-22A3Jv_fbTKlnmyx6dnsYsmCsxMfeIt4HnEA1L_o7KYb4ZLpmyqm9WHim71qwZx_aCMY1OkC_vaDCrwFlPqc618kAeDSIiNnWuZO8ZJEt2KFlTdymT_MlDsAwRIXclt5fnbxtBdpYx3S2Kl2kOfkm2OOMChcIcBwyW4UCDj-MHM4m5ScOIHcxtPgE54lIK3NLkK41CYI2OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FSDc21zv-kFSLQKsDFD7Z0tlVJtvR_LaQYTSlLueOTH9rzpLzv-AcSXrGURtYnk9hcKbX3bqMzEFf-TN02LaEfgV09jUrP3miut-EYcLc1afLwJFpjigiSenqYBqvliuP6jo_QgnGcyH02_yCSeBb_b6GcUhxwaKoCLNt4uNYfta5WW3gyCSQ8DNItzOvxp5tgHm_NqVx8aCX7Nfiy_D_GEp0rCBGsNGlVOVUYF-r42NQKgfYshaXcgIRf2IBsgJOdXeuZTqbChKBHgNu6b_OO6ABVx01-3uon714jJx-IqOgNf-IPOMAIIyq6LFEdR4m0PgsZa4hNJcm0d_HFAQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sku9yRw4XksuMEwOi9uujTpgJwy_PQ5QWPmDVZj7C0lC2fz29bN79g7-Cc3IKuF-3NzAceoRvYhxnvz8lvSd6HIFdlGBwfqlPFqL8Gplyg8F1l5M8K5dYx4ijgTJC4MSe9SzecllzrRkk5nGXaeKrgrszI1lWA20QUjKaoVWB8S3bH8NXptPnN0FvDLJXkiM4EV6Ez1D0sRqjevqoEWCdxVmtF2cqwA_R9jd986omKjo7yJfaOGzRslYZXPXR7eAf5_Wk_Lh7R6xHbX3RYPoB4y67rXh6phLo5dXvLUVPDrITgbA70z9BxwZrWoz5hkGt7me8bIMWbIcMe4ubEgr3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X2mwtKR_6_2-eiShPz_iODu3vf5NVMmpqXA2iEoxXwg5q6_UlKlcT-cxbI_QytV3YXV0KRdt-bgAA_m_3BHopq4vq0sZh_XgdOnVtk6H-iCBelZBXuYKRfyF6iN9zItbMdzKG4Q2ezGTHBn5DgmourHvma3IpORyZgZlyO99QolSVudPKlnxeHJgFDjzzUvvAHgqhiWmrNlh3P4tgpDPMXY-mvkJFn4VgxCo4EVAfP3i5Z97XA3kMjIUAIMbVbdqlfejiNTtjmjeL8bGv_80aRZaIRE2IGlSAiMpKuobGkyVRQy6t1UPA3n-t87LrSFxPgSZd3j8S2mfK_fp8IypkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/niABclIrrsedy4KX_Kjkic6Ei65NdkiGZT8kNlFY0DMKbduhjV8ex4K2j6knt2vFcNfSzPuVT4oqEncNchAM7it-W-4J1fIJLawNNu0jFygVCEmbjV94w36TgxDNyDRUvti_yIk8vA3wbVz6RFV-_RExcizAsNPLN2zTteyUpmIoWrsEQCHrpi0GxRKA7K2y0RGR0PJPwphJ-CDdq8pTsYJxE6rsw3HnxSoDAA44aInOHfOcwfXdaGQA-Xy72NRq3zgb5DGHS5Q6It4vQeQ_fXKUY2QyFqhfohGpQ1JNfbDedJ27auS-AusC2qc3sOuXd7Vtn3UgOxQt3K-o2nzopw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bUpdo6qs_OQXwAgz378E81kGVpxwz1d0C4OKi_hln9WiY8aQ7NS3lg-rzp1eX5WfCC65bf-qslIg3k8HNdnaPL-lREJMkhe3HBoYyckpHYJvJ7Z4YZ-R1rm5ZQ5Oipb7qbVYo4uJPHlF3-riH3y8E2JY6FhjaWWK7tgec10nXm6lbtOBCAuS-1DPKbSFZUdKBETt-Sk4jQVkHPpofmU0h1pXpL2qSyDe2EGrWHcFBOAFzu69O8i7DsNI6DjRRPe_Yex7M1LL4kB8o-9zZt6qEpJA9yRH2ZV4Kf_APRrtC3xej0Qiy4gT1JL8IDfcvTLzWsjOKOliaM_LjZ5m5Kezrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=sS2tery0udSczoL6bdtbUE1sZGOF4EXKbxia6CN6gYi--550aClH5a4jdTnRrKtdZBSfK8jGM1W_KzOfWmJtlUQX6bjTuzs-Dg_ZiAz7nB8VQEOL7Bi_hFRLS7cIYyt_oQYjzBmLj5yDwiIsFJd5x62pGNR1K3Apu01ZtGKkF74AJkB4Q66Z9nRb5AYhcGKH13jPOwMwrQZhWhUoC5UVgJ2QiRHYY7lkLPA026vSp5Pk0EX653fSJvJkhNssBlWbcWoaYJUddtMagMW94k-1vK7AHmvcdm4wTJdGn10RFY59LRDzekKi0689nKnA9WnKjIp7n1Qw1kXHPj7BGLn55w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=sS2tery0udSczoL6bdtbUE1sZGOF4EXKbxia6CN6gYi--550aClH5a4jdTnRrKtdZBSfK8jGM1W_KzOfWmJtlUQX6bjTuzs-Dg_ZiAz7nB8VQEOL7Bi_hFRLS7cIYyt_oQYjzBmLj5yDwiIsFJd5x62pGNR1K3Apu01ZtGKkF74AJkB4Q66Z9nRb5AYhcGKH13jPOwMwrQZhWhUoC5UVgJ2QiRHYY7lkLPA026vSp5Pk0EX653fSJvJkhNssBlWbcWoaYJUddtMagMW94k-1vK7AHmvcdm4wTJdGn10RFY59LRDzekKi0689nKnA9WnKjIp7n1Qw1kXHPj7BGLn55w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0  مشخصات کلیدی:  1-مقدار ۷۷۰B پارامتر کل ولی فقط ۴۹B برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/dDUqGTF8YW7D6ZX9Qfot2egSo9EyaPTtXzCgOR01TnZ7e4C5deHE-EDD9gwXVUM_GjikveDfA0Nk9-RGp0X8tic_L2uSso16_6FjmNSLlmUzMl4TtE4aZxnHvZdnhy08_FXQppHkcuLlqgIdXZrnizx5JuSJ4ZRvqHApG8gIh9o8tSbNpU9p5vMcoorfmpvBzOkn61TQ91FKw7nQ77Q1BynITtQqP678mKI_7wu3bXWXrw0pbVYUXSJQF7KE5Cdvh9OonIk6E2u5acRo4njkZZmnQI2j7-_8CjbOSOLYsMXLJWDEV-ASDMRpWT6J4rDEFGNznnIImS4U1GWDV7ZBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/kNz30R9pKbxPCN9pcH7OLQ6uHiGNvnKAY7RhnLekX-8vNT7UnvEMaOmebqBR0e2qWpPka3yvk1cFmmtFnUQ_aLGvzNopuOn9SfeRGF6Cb6cQyDzVrC46TAs7Fx-MSTzkUqLzRJlX5mI3cavQAZ3wsCK4VaU6qs7xOYpcysEXiNZLOiK_RSrTj2U58wgS6KrtEhOD1zx8XrTGMkVwMxurYa7Vmszs8T9QQmVbzoj4KiK6wXiQTFGymzvG8cuChk4thC7WSzTYs872KiYIbLpIn_33eKFGixWb5C8lXrJcTPMw_WZ-mHdw7ZxwCjB502mQWnXwxTkqcHmQIX4wL3MBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/tIklDsfsz3ertr0nKcPQ_Jq0xoDHMfw9rAp824YNyS_HxkHvp1WXaYvq75rlbey1sXJMTuBdqs8BNQ_juxiU6DKYOP9zokPZgelxkmCKyBMC7-ahE8fy9i-u6qc8anoEvvdL3kso5bPgsFxzww1DA1XuigWUcoqzu2nr4MWsNMmuQMZx87-a1JsgdGuYxL0c0QKdnZM5Aa9EYTQuwnPIfj-GmziaoDv5qbzwTPfqS21OfXY3Ig0Mx4-Qeu6WmUtR8XKn2NlSZVunYWFhp-jaQFNQKEmMrv8GdmZ0XhB9n6yvr6ZuuuWpZ3v4LzmwOQq_U9uM9AtmjM7sZ0LD2msvsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YOn0jFuQ4aprD5YCfz3ANvX1U8u6ydlYAOOraZlUtsrDZCSKzBad0IFg3yDD78PFmW4XRkE-HWUz1LoPvsQcD7LOnD-QbMXfUiQmn3PCwSEI2Ej4StyAEthPy9RSY0W57I26NjY05ul9ZbNd9IBZEyhONlBfP3McZOg5Ox91Er9JxdPDy5M916QH0l_qp35tsn3NHBrA3qIWXVJcDiYn6MXzBn4I0C-uueoujUao-QtVtb4R31sykOi3au258Ym3AwlDdtxqb_ogc-Myoj4C0caRZRQM72muU-DWbR9j-DCF8O7W9izRc3v3mJDUTIOlfcCFdOJH90VnTv__Q3mAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A4LbCXw6r-At0rN3jp28C7ZYf_MnL9neTBfBh8nVOUIZ1ksPvvqU0xoUStZJOgWez6B65WTcryRwcc5w_Wg4_RxjdWCcaK07ti9JnddoyYnqcdwPy6q2lj80fjydy0uuY2A6Plz6IABWAAh6NRwPQUIkkkUMyKMTvQhqwmHQGQEhRivfvABYw2luYDWfEiGXQSzgyI8WH5PFjwKvdB6o9qNG9NIaITK7_Prt4PbMaoQLyWc8inF-SoqxbVUePPhRbK4M8kQ1NN5dxp2AuiBmg7JCaCtWiUvyO2dJ0HMzjRMsbnBe-hPlSBUPBfHm8Rqw4wB_3by_8Ttxrdavl3qITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mj6Ly_YkVLKHk6w8kB7SizS30DSChLHvG7BkfuuQ1eqgmhda3ul9sDKUJgK-ppUmlF57H4n8Or4i3Ga9PAIXTqJGPpJn3oh8IG-9nOHRrf0Ptoy4cBcss_4rAt7oZqKmFd8cBNgYl2RkiXL7JT9ox8FafZedrhCdm4HbM5AdEezVSO9XYR5-1-zx_FnLcLQKr4sOB5tOgjXO64mQGA0ZInsBgLpANt703kP_M9WTdZq7xBNWJaFLDiUPB5CzErNtdQ_CsDu1BPCCXWq-wN7UD_fXrDCIfpzZBqyWDNG07jWboaMIUob_bxIEUZXf3qovs5LnqTadoU4N0CvEPwjY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/riQtRZxEzKrQD54RGwDG2Hd9lA-uFbvLcL6g6sZ8ats5dJg9DZEOomOTDwgLTXKIyg7cxh8NMxL9QrNRHfInWKN_50UrsdXtuYmwelUQNF29AtAPji_qctG3V-5QA1gzJqE9DpZ2zsszTrt2CZwDID1ayoA8IBXRLTDcQkJZI8ivTx9AdUrCFf-TOzJFe2ynPJ7m3R9TknzImUmshh7VZlHA11kVL6_jChjWryRXzpco9dix13Iu-XZMcKoSmAkKllffQuHSRcaiBVh9gaqdKpqOPlj9CafE1Kg2cRrteQVUVSiDxUHITXFhOBb49uHosdvh2xQxd3agTWqQsYvxgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NiNyzx46vviNd9enXlwIIuMO2rDeIrILHnDohapuLF7wcoNROziVc-SWj85FZ24wKsu1Q78EXsGifTOZLFBtqy0cmGO_14DaOvnu4mZAN3R8YEDsBBx2W79oBZgePmhC09Atme1wnluM4Pq7MLOoReTbRDlLc__Rz1GhfHunjih-zVAOiSBZxpfm01QdBTjiFzLSBjyReRkkDnac6Ef08I28A1iRguMFI_qnG5INozDstRr0XsUqczD0MheadE7FKFH06eGdxb11cS1o-oF6YsRWO9Gvb2T4SvlzLSQqNkebj9-TD7JLsm3OecyCam_cLTXzW7xZiDn6-ZIPQ53xGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HjWekqRTNa-wn1IzTfgSEfN-Z6TXe3Bmk8mVkDlilJW51mnHOpK0_ha5HiToX1GrEGkljyGMRC29GBAiUA5Wk-Y-5XN8YCgPqQ-1QZPfxC_LrdEPt52jhV9Dk7znGPfHZxM_SxLCO9ANhk8g4QLXeZZU2PJaf7Sp8xQRFFJo2nNPxu7mR_Naiffb8kPxrqHQdGVrQcqu_wwHzGNHC7sJpgPSIr-NDJTt715TCtPh5HAsnI_thrvEWv-0EfeLuT1xkwzl8CEcH4c1nBZI-FkorvIFa0lPa1WvGZ4lsdXZa-2DylbVIKxUizBDdQ9Y7I1VafWDKGyhBL8M9FgN0bh0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=d5wbS5Kx1DVOD4iu4SrkekNQ3k8neCC8EfIrfAZMJaOyZ2kkOFf5nNyeMswCpf8z5gEdg2EBY5rTHVujyFiRl6gkk82BexNAe3v8rCbRGuodugOfCNWe1GOTyfT7cARTzIM9EbdPdjgS3WSXtcIHYJAtR_Papk3zyye2DGU04pYthnEiSGDDas7MR3cVViCTbZO8L9fwBRWThqpTqusXUsfgVQTLT7y6CjXXenPi3hdYX4E6MwuuRbeKX6ck8mUELzDuMaA0znLFfTS2qsKCPqITnzehDmPRoxr_2Mq7WO69DuD4Qnr28F4rf5CeHzVmyz1FSF1quPI28bhOJA6Weg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=d5wbS5Kx1DVOD4iu4SrkekNQ3k8neCC8EfIrfAZMJaOyZ2kkOFf5nNyeMswCpf8z5gEdg2EBY5rTHVujyFiRl6gkk82BexNAe3v8rCbRGuodugOfCNWe1GOTyfT7cARTzIM9EbdPdjgS3WSXtcIHYJAtR_Papk3zyye2DGU04pYthnEiSGDDas7MR3cVViCTbZO8L9fwBRWThqpTqusXUsfgVQTLT7y6CjXXenPi3hdYX4E6MwuuRbeKX6ck8mUELzDuMaA0znLFfTS2qsKCPqITnzehDmPRoxr_2Mq7WO69DuD4Qnr28F4rf5CeHzVmyz1FSF1quPI28bhOJA6Weg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VdCjuXT12Tx3xq8F9dlikDuDlGoJ63QmMHG7LDK30tPtgAHmHRA2EzM00uP3lffdmsjHpDqnTi0DmKdlNHpWkeQli_n7DrpVQb7ntbjVxGpFwOyhOS7JgDQQp-gf2wyHHmSDWR0uoO80iCudijungPjeydwjfzx43i9IAq_-6PpG5L7ZAgd8RQjkkkGczeBcJeOt5r8hWcfmGFejMqcBgfL32SCub1Quj5Vs9joobs4aeDuem6hjsRX9h9dHSd9zdgHncloCfB2J2aPVg19dVSB-qYiIHoHLLql-QJIDHXwxrGAttKr88y-UNwKU-DI3vaxXirJ--inQZM4fnvo2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X4xz8tsqRkClhk2GhjFzWHcTgYoYwVlSsX1ldoxwUcBfePImuFo8YC-e3wZ3-8NCP7RMV9Oq3GAthehqTK3tWP2rgMpOJjLN2guxeg-kFtOYwuveAKK44tBAE6KCqEKeaCu0wtyuI6deaFAtnX-KgxnPqeyV7IFn-Se8vIjmz6ytnlEKFS1MSz1W9iCAvzs-97GyyNKZAZflAiuFJPOXkKB8DsY5uei5CAVICuMxZwmt25dbXeETUR-SX2_npdSyWgFnFJWeXJqK3t3GFe0voOkqbir53IpOa20SPdSIvCULHssqcWHMAuJhA7HfBnuFJ_yn-c9vqkgmmt1ewkqM1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPywZp4l3O2WQFPXTb2dKauLe0Bfb9ICzfTv2pCo8-huZkBSnVLpqczIQLL05I-0YKRwj7CTkQ7qdR0-KEys7KtcKYnz7JrbveV4AddS0OxecoCYF0q98aT0BDg_pSDhAcsh2xiOTmk4tXVZCsn_Jn1I6unURvod5bbS8JaL4754kwlnN14zGwMcC92SAuSwzMEHLw15eIzs4yftirAbuMPZa_8fpZIysl315c0dkrtCfPK9-kXojkrEEeibPq7KUHDZxHOfj8A5eM_iNuUWjcKAeo3p9G7peHfIoAu1oHN_fY_0389zNLqUcu9UEZ0rsqLufYcdRu2nU0O5W3mQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YMUVUHRzTwB0hxBCVmXJWdGJavTJWx96YJyIEBimHjPvhFoN2Ji99nXm0cb-c2up9eKrkPNUyL6uZYQQAyEBhgL5ss4veBFY0THgV_lGDubAtV7rLAq3Q-MeqoMlBFMEbb2ualB408lB1JtTSBaXWhREV63Qt4ImDW7eSDKVZKU5rreKDFS4GWTHYGUgjLEXWGu-zMvA3CUUxOshqD_j6zuHpx0wHHBFfY4WL4bd0GxGdRPyZ9D9VjUS1lmF8DgnHFALS9EpTn0fETwVOQcFZH2VJ8QOlQtHlOjk2p65bKm3hW2Z86-Zw6Li7uI5lyDXT3omyPhE7he-fzsOABXwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aHtv1TdM8SZpSJyn4dTP6PnsExSQu7Bc29Tg40HYWqWFdMlUQu-5ZRd86wKLN6keLQostgNcoQ1EMjfuMqEm8WO0EGGiZ8vdOrBKkoUfbZHHdnHANfCEp9euB9Iks0-uJesQ-ojSIGoGvP1V04jJCAterrTW6SG9mbqDPHAXz7ox37vETRztltLxph9QAtw11K0mt7IQQVe1eJPmoLOMelsm6ht0cPavaSWYk78b2-7C503Q6lGkiTWPL20v83pODHjKPDTZg52NfPauV0pDPHrDdCy2TbFo7XsZfIP5b-snrM6aDmYkVpypQBIp_OzUHOAUUmXWNqUeLVol97PI2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KrLnYMc3QHcajZtTt8ZIMh0kZJs5MsJzSTzbLlJd8X26k5fSWb12FyRsa_pzJSh8klH_Nigv0DkzBzvQxCcidIhXR6970-DW3Lam7U9AwcZwLoxeCJ7rjUhNYLdzcc8IJkQ08DA32JUzvMZwkoGThgKLUzNRQeAT4raz0BMeF77m0QjZSh0LFmbCyVuCupR9F9HTTgCKFGwnuD9OKWpg-2Zg8litOF2jK0cjbxsuYiQSn3RGcw3K0HtTn4qCYxe__wPr1lII2OOJbZ6zW6wK65BMvILTLa8PKSK78RV5WcGXj5I0ZPSL1ekm2s_aXCKcTsG8x9ZE1FeRLvHDivykjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S9EeKUCWWD5pRiOyvGnTVFFHfuyNpXMT0zgJH0dNl9_cY8d2-UxzQ5Q3FQzhcAf4WqqRcNDBEIwqHRZHhL7pE99DBd68VG_eY3fwqnXWM9ocmmFwjkwreghW1V_aSyMNWy_VofZ0LFPHRUa9Z0FU-mMb2-66B4lU_8EivV6-LY6gBb2TKryNjWMZXw5sr5B5SMtOPjIvVxJT2LlptZRdvnZXXkthBuwZULQCii968GYQ8TL-XM3ldHeJE5Sp1lmW0MmP5D7SR-Z1KXfgu9braRYdaPTlAsBD4_3QdNEO0_HUYB_IuQxcsfqTyW1w3LIXkt2Bq79gHbVTIqAVziw_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NW1uqlvr9ZPTSU4xJkACX3xVvnrGe_de0bcbv8i_I8z-Kgb_ufqB7vISQLr1Z9wt0KLht2C59khv6ukYbbPsg-A3T0K8mVMVb5-11jEVB44n32VTzyIDdKDQi78r6BbH5p2l_og9UaA9NhucpZDw7zDfh_lPvTOfcnkXBfFUOCrETWTUDTk-1LfflOPgzqR2pwYui9ivM0D4DxqiORK7o0Pnrto54O59wsl5wxtFLHv83vAOKOx_D7MM437bNcBsNx30q5yfDyciQ97eRCCt2t6_snzhbukvu9Z6xkxXTzAcYFNa2ttNAatptRabWnL6e25uMuytq9BbcuA0JxFJ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D-hKLLlaNXecmqzb2D5SsT0WQCmzKLKAwf2b0lt8TtrA1Zr9_wSsDvyGpLgk6QS8HqUJDhLROF6-doHzcSL77Q3Bgy-V1-ggcBwk9eGmRPu6vkuIiP7cdVvDk2bR0GEF-UqmSxD3DDdKJ28XrmnXjdM8XzAwXVifimL3Z08Gy-3VpNCbgrcLxP17TQNELAJzp_kVO-ZpFcti3S90zQ9VHbv25bcvwiSAcABPWNj4z9hOOxrB7tEQObnEd837CqHGuXIsUWAo0XYenc2jqCXqrVRLd6g_uuNHM0p_t7SWg-NyCW4FEmJ8e-sdEy32MG74leQtPXC13YvTyMmFT4VwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mfD2FDoH1gmGTEQKby5OuXKyMfQigkcvChLeBtfccwtSgE63gRi2iNKp4nwB0KoMEL4DwYQrSpfSEklHnKW6_F0LqO5ChjXtOBMObXByNHMCW3-K-fqJ-oJVkwDwY5fYMrLCnl3E2LT32YuijvcdDViKR2PPufCZSL9TCuN3Ep8jcayfyZl84XTI2efx5Ey-ff_sXyI3-_8THV6LpeI1W1N1ruVjK6xgt9A4y_JwetBmXi3YLeZVyFYPrtdVbUD5Tgbwev1-99tMXl7DZAagUbAHnpkHvWXVvBEW_WthDAObopNNhomE0NMcm-Fu9LE1H_wDfJwg5imx2v8feIhZNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dx1hjbfP6kfFx-TF4imwelpPz7eOwoFYpemUmcwCc-mHffjsF7RQ6oup_L7hoFwJF2QzCC0QSp5Ve3hXO_oxzjAwsnl4K-P-huP324S6pNIb3keC_cVWlXPFA57Ab8n2YXXFIQD8oO6e9bVt0oKMOCNG3V0Qpn1mXtHhFqknUu8mi3wbVowcm5uWJstVqFas701sS3prhrXhfvKi0481rguputwxDrQCKcT8A4faozgTKNn_A8_fVj5W8mdN2PrluyaqTnyDvUIhTE8RavT49u1SjitFhiycxlZ1UVF4ftu-vrSGJgsGoIivCsbNVSPTthN_wcBRAmaH3ojFMqGq4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HJiuD4UfVJW2cT6muzLljqzFWpWTq3OlOH9rVoX1q2PdnKBdAKdIUj6iGVqx2nM2MTdH5FmG0CTLbZqjLr0AOOFQufpwfvstkIQ2Thq45Xh0wfzPElTeAn5auE8D2njugmP7_kG_SUyNHHgTgWcRlCDQcSubf-IYzRoe3vSynlFhe0xnLOWDNB7uPDhMt4WBMzhUXfastW-Yb_DtLdmKndysqv12eqKF2_hRM65nrvhLxp8h1YOrqT-VHfMuGfn19XbeXtQdyZyXi7SqUR5P_zLqjAeBedLHyqM6CeN6VuLPKTbj2774f6sihPu7p8QOP1UcaJ3rhWSDYXtWWPoeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uzxkdspXUOL6gVuMicdkxkhzZblbpeuAlJhp39im5S7mZHv4Uroa5rVi8PYhW1Kg5lqYJ-LJLz_A_hDtCiSnz56xxLTMcRlD70TZVT2Un5i2QbWTcxiLa5eq-ilJkbkyOZOFXxP_tnqReeQwCzHzP1kKwgnXf25-X2i2kDcLcWmrcZJfROlsYfcpr4vV10ZPlovR1rr7hLhwadVYbtcD1Iv-jkGuqNo67ekySrxtHeDhrgepaHYqQ3LEvBdMXnbftRdLqbayNEWJvzD75gn3kF2ERTX39y8p02XVR_N56Wx3BD1qrM1kmfF4XF7GYac5vCsiymwuBawplSWwOc1hWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P3WI217OuSVvg7cJbtZYKtInF_UgX8uWUhMUO23RxGfjtrz_-i-9V3dUNcPAvoN50LLexFTAsBraR31bw9-53UE-nRjg9Q5ucG_wtQ4zKssjFMlayMi2kJJ0mVLBbHScOBy6ud7E4Yn1Tfwz2NGbsVB9mRnQtXO4zM5fIpcJGCWdo1VxB0BqIpo3AxrPxjbfKs6aJyVi4E6Z4Xh1IgUbtngSxaSZKVq_JECcssR5xdlAZQtQOXEvh6G5BZtuFLCXUIeq22UaULst-UXxk0AkD7VbKG9ZUP73VdBFuISlV150e8lbe49E6wRU3AMEz5eLn-tj84aLsYf8zdlX0zM3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i0zLfiFBP1uYgQfrSe_xlk_bBDn8uinDl_ukOs4Yeltd-dCdNl7VVWUXCCH_HilRFj1IX-BlUw_iZGflDqYvPWxg-n4DzFa7_09fuP7dWDQ7E85hbMtFvgrgYQQTwQxaFjVWBDGnEyHBO7KBTHVJznBH-YzimLq74M6eDSVa7lLgu8FOL-JiBawX_XyZg6W9fXvKwaR4gMlDhLnnkiG39CtbKyul_PvfDjzuCuxvVfGEOnF4aB6qIn8wvTeyuNTe0Lic2pzVdvapbh7x0P0KdOLusVAJJMj_Iw9mD09RK-gEKU2lTNv6cWWuHNZMBKHaMGGAbzlwINmx8AjxuSNR0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LpixvnLQAbnPyR7WhGxiKnCeb-OFurrbnWlNUxU5z3eBNMRksVbzwCVRVonZBDGIbCReNr3rs84kXLs_aCg5TIfFgzzVBdDR4KnDW6S6KywV3UbKK4GYpBaoYA4KR2F7dDir7xl2Bzby7z9V92EcaKZw3ELcYKeSNymVLFnsJFP0W0no57NUkzK3-uTcBsYTxswT-rzOnvoFd1fO6-LZlouhFv7EtEOm9FfsSI3lIB48At6s_G_KpxeIOrRJYV7fvwAemkjVWuvRG2Dz1EerTsOkOvmQSYXII0nXXt0HVNartfB8S89mQRsF6nc-94jztcdm4GvArYqFUiW841Z93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=SLUtADwnCPLVhDdIGGQ7HL-ZdaPbKJe24HiBwS9WLRWrCZMSzhulxYKubomyjfdKnhNTUyesYkKgLtBRVEleoNbaVJ8YTmA9KM546-UwBF_FoCKwjLJZqZ1CmD45dZA0jbSMCuMfVwpPCKmWzvF2hwiz4h79fMNj45wN7hKBdas3csNxU8fAnqgpyxZHWwf8gBaWDAPVl4OKGyGXs2ettNY1fMzpTzppImY4ir8lr60GKgj6KtnS-s4mbrK71S913thOo8ziX1rc8oCP8t3fIDQsJLuAySHe-4qI1DEcdeD4rvwwhaW7ILCKVOB2gVVbNFcIinfJVbudHAw2HSspFRWX9ISddbK6LPcCd00_5-IFWtJdWsGk2BUCH1JwIFzxehqPWYUF4vxW3m3-wN-Dew0-1VvF83tYlueaUSUrFIMCCRvfHTkI7heppeXUvsHysZn_ZNKU9Woph8Cq2dUB1HbHD8DCC0aYFtDRydyXx8hfNmNMWTqHw8ljh76EpDPZqOukYJrUTJnK3XwDPSCJLluSAPCpjHdvl6f_1RHYUqm4HeEqNxfHLJJ9jzXCGsMtn2615ARhVJ3QY5lDBwRrwtBbzoLFZMKE_avLHzJSp5nxcNsq6kxrY1MEob03PYO520yo2WBkvAVBnVDKieTPBIEg5cu_9bzB46lJb_OWmpM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=SLUtADwnCPLVhDdIGGQ7HL-ZdaPbKJe24HiBwS9WLRWrCZMSzhulxYKubomyjfdKnhNTUyesYkKgLtBRVEleoNbaVJ8YTmA9KM546-UwBF_FoCKwjLJZqZ1CmD45dZA0jbSMCuMfVwpPCKmWzvF2hwiz4h79fMNj45wN7hKBdas3csNxU8fAnqgpyxZHWwf8gBaWDAPVl4OKGyGXs2ettNY1fMzpTzppImY4ir8lr60GKgj6KtnS-s4mbrK71S913thOo8ziX1rc8oCP8t3fIDQsJLuAySHe-4qI1DEcdeD4rvwwhaW7ILCKVOB2gVVbNFcIinfJVbudHAw2HSspFRWX9ISddbK6LPcCd00_5-IFWtJdWsGk2BUCH1JwIFzxehqPWYUF4vxW3m3-wN-Dew0-1VvF83tYlueaUSUrFIMCCRvfHTkI7heppeXUvsHysZn_ZNKU9Woph8Cq2dUB1HbHD8DCC0aYFtDRydyXx8hfNmNMWTqHw8ljh76EpDPZqOukYJrUTJnK3XwDPSCJLluSAPCpjHdvl6f_1RHYUqm4HeEqNxfHLJJ9jzXCGsMtn2615ARhVJ3QY5lDBwRrwtBbzoLFZMKE_avLHzJSp5nxcNsq6kxrY1MEob03PYO520yo2WBkvAVBnVDKieTPBIEg5cu_9bzB46lJb_OWmpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5038" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQP6nf3g9zh3nJXnDNTGunEPGbzCJRF4Nf4GVYlsA6nSCEG0A_CWJ5Eg9ArdpnW6vn2uikCLY3hCF7zXm7mcguTqA1YESJ1RGfTy3l-PwayANsnH32-ova4l5vVbE_y3oiuCKLNv8oX07_gKzp3I-ahXfvHUq2ap07q8Bf7v3WSpOIGT2pf2LbQ9t3PYG-n54dJgGe41GAAxhL2zI5xzLTmuUcBR0R2lU_c-djCqc5rxUQBYuA0DR4NWlkZpX_Y0NvrbSQUAqj-xuJ8Od-PJvMu5SOyme8elf2Mq51QzwCRmHcT4OpCmfEOtZpbvu9ty35XBIRsLEnPZ20TJ3VvuVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C_Cne-42eLichPNyLWXLVpcCzrO5zsIH_FlIKajt0q6nw_ztQ7JAx-F47uhLgvptXnDWMHkT1zBqeV-m5AAQXprxsX9loFcbzsq8b0RlXMXgoliuuvjax0EhmfvrRzjRK8VoIfhpn3B3NeK6ArmcTWbYgProfUcL_gIEuC_TMuLwXHBJAVHsby5hr2BxyBUoJUxNkaT_6_E0HoE25OcUh9H4vNUb_Uo7AeKGnvMXf7Fp2W90yvxrYHM30Hk3loi5SzIPQeJD5weNOYndUnXR_0V5idc-aBXYunsRCsonkrbeh70X7cr3b0xR2-RJa9i9AZDf-Few-JQ7N1hc8ZtTKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو:
1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه)
2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید
3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی بعدی که پشت این میاد فردا، قراره حسابی ارتقاش بدیم)
4- آخر ویدئو هم توی ثانیه‌های آخر یه چیز جادویی هست. اولین نفر برید ببینیدش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به هیچ دانش شبکه یا کامپیوتری نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
