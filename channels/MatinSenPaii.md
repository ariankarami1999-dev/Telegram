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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 08:17:51</div>
<hr>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q0gQXJ4_B7GMl-DZMp9nHhhuOrSRCEdzgj-As4wHP43GpO2WaczHcdjhwGhXrfkrn9-8LmXnlUtaIvNhw-7KsmMLFpAO-IqAT8oKUiWRc2UFZyk27vuy_LftcCCK1IrZ4qf0cfe1HUr73HX64iBQf890jucBeAvwSZyH9Tl47I6L7nNB9XxSxAE6wZ52gSaZiPwDniEYu7nweTqBu2GrEuQgfP_m9NgDbjlb1ghyPZ72PVhiG-u4TKX5oqgzOEjuuDEn-vrk1jgPKoU_YrDOJFtPlnO2Yl87Pfnk7t9eQ3XPRj9_IRxHiWb3PkncEfnKyAh_ZSVSHdy1NbaQPKHWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ReyvfLWhJaeba2mHVQzubRMYPa8xTwDHSQMU2dWmWR0AKr696CswvfSJ65XIB537bAZUJ5KDe2Jl1AvIqLYuSDFlCZpqPxF343gw696ulzq_IaIeX8I39UlHIcQqrfPBMYufz378HDtoS918DFyLIrdA7o3B4P-mE7xN_51-XkOlUKKB-3yW_Jmmk3eGC5JZujE3QpSKKhZrt2Im9KmRjgST3L7kMmv8hKcGp0ozM9EV4UY9RD85x0UaUp41sy_h9fBjXwfM6u28Urj3d8_mEnTHiovWssSWOfotSTEZhuoRX3yBDpkvbVEVM1Cxr3d9B1E4u2q1EGfazIhnFKsvPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SJeG4P-Vr-BFB1uXMfL2w1fQL60VXz1HjTaDOCiq3vM7ezQhzL7t_OY25-d5EKZzjSVOWyG0zRSEm5qvkWeXr__Jc2-VWev6jxPMP_kagA13ekTu8T9xklmKyNL6fELE5DKBvLM5P2Q8lqg4r9fNH2MO-qFeK_m1k9T0ubbpcv1C0CvOIRYX7hFflq5aBYZMxnzBYEQLa4Hn6SoGAxd6C0gEakce7dtSuzYFAswEZd_Zfc9WFqTced1idJiNUVE7R18tu_DLq54C15tGSE4noUrPzXQDu6hrEh50B-wMO7_WxiTffw0clk2zdfTmUX8mp6Iq1HFm4l9rnCHlbAiiRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ewZnr2vMNnwdbniwjVHUpjaCbmiXiWj9N8SaUUm-2Q6_u1370fKAPZEVIORGumfWiPTjYlQtNNXP1F5Lyb4SiJWd7eDPPcGFYCY0FF7HIL4mFSZ15Hi6Vx5vV8ceTkXOmTLtuxV1USZeDi9avuwjzB4dWXCjcjqW6LKy6-itX5anqD1IPlDmpx8wrftdFRxAK44JmkB8GgnmJwRnZTBcAS9_9HLe16AaBQm3dfSyKX72dnfV6T_V6KjJSvGxjEkIVyVUZxXoJU7wWmDuoa-z0nHZHZ7hrCj_6L2i_y9iwlgknzxiuobBw8scMUu2FmWkgKhb6qw5GYZ1pNhFrJLpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QGlt43YaUNq6pla28MbEPdttNsxwKnQQ96XHJ4IO6tiBeP3EOFWX1K8RQQ0XwUVH6_8RuXqKy4YLqHfY9ygCdfoSGJD1NqvonOxqz4HvnmtbVg5Z6I5r-csBoqRgOKAbv50t647zsQepEZ9l4d-7x_xt0QAddaJx1RJnRcCAFOxHPpWfOJfYS4C5XYXCaEvmP07Z2tq5NhQUktLbj2FF-9EToluSzJt05VbpcinxsYegcuqNafp_fX0jc0Bx9lgPCkRWTT4yVovDUSvJ-yB8L2JT5FCU_-ZZutfaFma4YAf19qCaasiAoPQd_TFG4Ftqkb1PRRxmhcenp_pzKaBUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LEdzTnBz7YQ4rvlZmuTBxaHLuP-Pn_VGFqQZfFr0KF7KJYiY9MeIr0CtwXmMesPgzdAhiM_ePnwJgquZZPQLXg_ID0FPUpe6JSTiTuZK8vxEP43rQj1Ol-nRMA9PlsSDTux2lq97q4MQH5xWcZFl1BBypmdov6pca-qWI-AplXKg8XU5ewxR-qr7E2vMb-Dz-AP6tbJiCcVIL-9bKjkXgBQbwL_CPRXgIdO3TgFhRL0p6BPUQjWxV1Fb1II32uPaLB9GOA2MUUaHMkcRXUnhoZ4LULpYGaZJ-lPzo9BLj5DqDpsWSin0UB25L85WLlO5FJesnuSBGBT2JEK4GTtUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zo6UaH2H0dGgeEKBrMyiS6i1U3Y_vEZYnEKMxfEs6-VWw1Vsm-gEdVxukDJPFdVi_bFvJlI-8VplsB-RoLh87hcwPH6Fs1txMzlBcCA5qLaXuXoA5FUcnrYGxvBs-B-ZBF4sSWFzVjaZLCNkUIZJXOgTGgUDEsAVOAs_wXmEGB1kTRTjB0ma8kDlwcptTURhVCmQk4ssdyeYw3pWxN-SdQftiur6lpK15b7vfM_idIrYNbwUTCVxv4yUCMyM-Zus6V6jHRKBhnuZB8lyqvjcXykLPpxD9LUtOAazDTd3RTx9OEMvnxlY5CeTO8igJwHAwXCepqYfSa89ljzKfbHFHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DXP5eWAEXReKvMoFp-U3cPGH4ODV-PX25kyjLK9ZnThMT02y7YUQ0OzaWaAVR4mOx0Gie3uorRioHyALwEHaHWnpZIs2cY3Y6wYfu_XAVFyHeh79elHb2mX5PG13wEzgp6hbc_IMic1gWlRbJHVUEvaCkB_3wQnDwQ3M4WVx91J7AMaIQt2riwyZnPvtWHcgcYf2lCBRteTYhK5aQeR3bt3P8At8WhFnp_qVhZ9oamtv2Zv-PM2TjOR52gHngbTH-uRSHqOrIlIH0CvJpdkhhXvIeVdN3RmpVntfi2R31eBZ6SBQwVlBS0M-7q6xBXvRa66rua51tQD2-Qz20jJX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vhnbMq7T21_hdvJ_C8vWbbAAGRvFRf-5wUJyXejd_nA0D7TlxZAygSJC5q-Ze_YKJYRqTN95BKnYYHlxMRHnFrteGCd0C9O7JJMvF1q5X7AaulWxYxyBlJl-ofA2TiZ60EdXQmKdmclbCzmdjVLJcF8KRHfg-D9dhfMp8B5qDmrX3-LvVOqqEqTlRvj54cO9zFajj6chGUchgcfqK9aRZtA5CMWO7XTTYxlBrm6Ji353pzsw9Rd6l_lxObVqQs8suLnYea4Mb6KLTxeLNZSCQsb2_IFFzNosn2pUjE1dWvz7zcimfwyhzrPvnT2USSRKU0iDNRAVACwWLSKGRds7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CPxfXTueRhOhDysP9AXSW9ICBzGMiQ21rBytr8ldkKCNTYMV3SRsO3LJkADJ5Y94i5iXPhbvZUzwYNnp1YNJGLY8NP3xvGhJWg0Dn1Un_zRsWiuaiaJ5MPKdSTA4rFvZxnrluCG8XajpJPYaxVfLKmGi9hTmSnUqUkrn1cen9HFQFvKHU8u2Sha-a6tyy3F45PlzIhSfjhjt9HwCGYyVLKc_xCvOBBXPvKCKD2f1d5d2K2XT_GzQyPGoBPtIwPaa-fVjRMy7AhenY4VrIvt8odh8s-EC5hpgeT_npOQphMHaPpkLVq48irxuIpFmXJ9WOXxfwn1-0MU-SLE-1EDSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T3bsJ8S-l0FJW-3KUNZU2IEHyQ306F2oBFY98wwL8Y_ckJQPUFhB_NRCl7YN9PWU1Xc32I6JoItZrrDlSl4NtjLzoD2bsU37dwQWEjfYUfqOCmueGs4dP4V8vcH_cCxldj5s3_JSZ5jOw9YErwEi3XrtUIE4-mqdG3afCPqNy9QWzsevV8YERQ2eNSVWUHM4qXqEpFmpZinWpxabnl-14uPH1-bhajDfTsQtsI3W-qL1kKVeDtFGuPj__cvri4y-q2IO-NBqLsIQ1DZAkZtf00QTrlRvse-9la2FX-7o4SLs9dBhgjzG2Ayp9ADFqvCm2WYQGnXYoNTp2FgDaH5wyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YGEU3PhXxUtRUlDIXDA56b7CuBMYo2wMm6siV_ceaEGIns7uuymYF0PjMrnd2jHjhhC-GN9pGv7lGQOZ1OkM9PInFV7AC6MRVU5-y_T8KLwkVIK7WLsr7NIDgGWXH2eXHl9woxP2ZM01op2X1IkfECY2zJ7zqr4kQDNbg9vHiSDh3r8TBeqMyljgKRv6oXN3yOwlICtgonfYmIuq5EMmwro6wBbTYJWZcGuzUlz21YG13rryNbjXZZiIS-qdCyYVFeEbEEiLA-IFWGnlbwEy87eRViaj5GXLy89GRuvbx53mD5d3JQIc0x7eOUg9xDUXa_Bb7mblsO4K-DQ1OgmEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrqLzy_tLzDpWzRna02sbqHU1XbgML5MIzw6VK9l_Ru6tQ8-1qpsgAREZ0QQUyKFCeq-K6ppuRqeQxstGELIqnnhNsyKPv1OqIyB0MJ1w0Yds7ZHHQBYDVehdL_pxqg4O11H1EuUKkUzL7i29AqrTEgHwx0KnmCNDNZSmc_NF8ChdlsWopp2pwFVfoUbgE1umBzQyV0erLTG-flcv2wVbZQBQurHPuwhdH9WpGD9sWBoayk-a1Q7vmCesGsY1SnpAmoyhl2MK2nb3LkPg2Fp5YXU8fqH4DezmGtz_eVP1lxu8JM2AnHNMlLwME4qOVkCaUoo9No2iVj8qAeNazSk8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iwHPdMQ03UaouPHKH9rhZyklUpFENidN1aA6Y3Z_5FXQg9eje6cLDW6XUjzDR6dX76rI90V6nJWGxomtPmuUjUK-BGOrGpERSSXqDiciI7iZV2Kja0niiUdL20ej4jUUaI3A1kMKCYeVdCCk6U_e5EvAKlHT4Fh-hkidPBSeaAbsje4UH6cUuJaCoeOQW-IQKBrL9tA7KmHw8eAX-aVfx9SXnmmunCZARRMPPrN2o4BBZxizr2gLZpPJif4yG7mxKYeUNh34Y6xa8OWTxZKNLuvAhnHHTRfjf0fov33lbGj575inDIYkY40_Hqo5xNvHr0IBze-XsWMrPJhA1Bf9Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OJ4yJ52QbFHYzG49s2aTIUZ12BkOSlXQuL8M9Efy5HF4u87zg_rGRHs8fLygQTpJcuxIgQgwiIoRGpXnou_bJdOXN13p7Bm0uBA5HUHFDGU8fobMrFm42O28Bf1BzoVAM7HHp4Mc8g0Q1F3INJr-UlxNPxD_7NHwSdjAV4WjugCKK8tKrK6IzHOvDZC_iYdw3vqVPAw45ybHnIAA7MzvXBqYEYgrn3IS99s-d6B-PyGBIhqWx1oPQwgVjlOYpO1KtaxMZlQ2W5UAOayLlJ7Y0918NQKxoc3WP21Pb40qIu_74lKAzKUzmFdHkH6HPALtFQCHI300fBnFxhWy2WAK9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kPIq3qvDBDMqKg7Z-K5NEe9wBFMmx-h_5FnZLvaDChjU01FbiJ30NH7JJuFUud3JmVyNz9EDnKqnesBB5ff2k9-mdSlsknNOKCSGyf4Gt8C2wbFgbP7K8vxOH3Csl_84UEEpmVNpbd66IfBqAL2zmP6OAYr3hUcoi1XCmHqyywmgeIAWxVxyrQaJ96egoYYJB-ST9WHs4xrEnD_TJS9U4R2v9mHwyD6oPHbdSnZRi115ty07PISAlVoIDzljImoydx7BCFT3ObkyrDUqK-bZLvGXY3CzzWBqP7TIUa56hMsTO-_-wX4YNDV-tokDzlpsj34xSQgxhO45srLvjBrXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aPaRWTtXBFeo8gAjd8oI_cJFfAlduvsU3nbP7L2xL_4Idu9D_-vrMfrjnl0d7MAceTuBWWDj49e3zG57tA-ni05_q7KzIuCiRMqlpjGbdn1zJ9ja9jY1xxGI2mIjwZuyD8tNGB1tBsGVPkt7QeGD_uKVTq9IZASqJolRX66WXUb0HuwGuPIXHDHEEDxXvy5ItrrDXGinnkMMa3aq06b5bXVt8BFg8VeE8rCAVoQZQdehE6rxrv4RgLpD6UDg1pasTRVYvzr7Loes-qmTh7shtIM6ovx3tdDgEkS8w08I4ylY8bnHHYFwmKW23-qMiD2iA8C0M6s_LqvgfapdNoyBqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfoHVcXU97Gq-BsR168mOKZ7wEwAMT16RaWznve1kkZOTq21ovoAEu3ul13D0x3JQSldChK5hM0KEpfPVBCJ3xH_ic_LDTYelwxuWflymgQnfJN5axXJK5ckckAKNOhuhqrvT2Edehhfz5dEqa9Mssd6nkSo1pzVY94VvVPBKiEjM6tgH8sQ_sfKg7WfFHUcIQ3fCir4hDPH2tfpgUpSkXBfyEoRwud6u6TENGDHPmVwv-Xc3GkMwlN6YwQ7YADvRx_5OqbOcCwBZM39eHH0VLq2F92BgWxI6i6EUAr0sKuMycczkGWnqdNJOPZKren_f-S-9gynqrVwiR3xqVd9kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u-fEtaICUq71b-GlZmzHFvimds_fwyfR87xQA2daZQA8x1vaKXZ19SfxfIF7qVPdg1Tv95phpnnmayNGDeAtB99xRpOp4wOdnGbegDO8DuF21SB9GZZgtG7VMZp8PsGIIEK-X9AVUy4PFycCTdDxSWwB3CISgHZMKy_JbPX7_6N38jk4-ct-1CO3FlZBsczV9M33uIgfNu_qoqB0QAmaKEArEGHSd7lBTpe2IpWdgxI44Xw6rI0f0MGgmDe-hTjfrdciNgr8lWJwk5byGZ3lRy0aJCACOQLQVBZde-RfwgEboXP6ecbpk2PcwwG33MuIpjQXMtdmSGSkiopG2evMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/khHE6Jcoien9PYZ7thUHtEg_D3PcqEk8MizL2HWkj7HNkW7X-I5nizDRv9UrbVh5LflgrTt1-8KNijCi_qj1TmxPWRzg35CClUVh73CvTq8zVb6b_KJtWmna_ajpNC2z5ZZL5ib6oMDhL-ukANDczVm44bUC3hcdwSk_m579UmFUaDgK9ugPWOadizVYYIVM2z_Gkiag2CP3-OOh8IDRq1Gyk54X5XtaI2sn5WIeIszd_Y2s6FyGdMn1WAcr4rF6J9Bbsps43kPqJfnfH1kStrWmL86OzGAyaz0qpzSFDuI-jiKaFZXI7CJBEJsLrpnOyIS8OmQ7zZEYKwnE2CZ8HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HU2T9V4DoKt-WSQSMRdM9RaMeX7nQioa6c0TJa1dNlIfZjMDaT3lC5elftXsUVncbhJ4JEQbWcka1NiXFsxVVwbNJuDJlBo9atxN0hk6wnl-JS7JB9A2brcQaTcMKpaG8hTsbXf1_9LORjbQyiJ_qiEKvLejwctx7dnDZ2LR1CMh4gyaf4PJ-WBv6ytG5TxjGuEs0e2KVZWjw-gAmd1z6395lwcF5dVaE1w_jGE5I5ofPB7n-2qXxL4a7xkQtuwHCEk4f742qXWLEDILC5SSwtdcXnScOIrmvUPsrhnEo4Ee6jZxeyeKRXPKN9A-vZ32LqgohU_LE6qhrBQzWsnC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cIo4q7lgupsFnrwlQONP7SdzANRNy7Z1_eLGwSqTNQTaYT6PcexFu-mbddzqh6FTOItlklHceg74XUlqJoPRcmYEkmfnoNaduGczrf4_TDMIuJWiA2OxVY7B66HVBN0xhaH_v65XugguWxCw3U3sJUxAI2zwR_lQtqqA-Z8ntGDgWE08ntGzQkrJJ1cy3EHIyVWLid-en9XFJrI-iVeO1lWO_Z3u37YAiEpT1s3EMrDpTTWrG_UCRoLdKhf2HAeVI15_fBPsJtTXRFzMqkYKMBwiCNc0vtIuppyb7wPR2q6i7RONH5nRDYilKd_MfKI1gZaC_iWHxgNgnlm6DZU0nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q6ublWRqSHCWPunlQMB5ri4O4YxWJYQq5QRnSRjEm9IbII3DNb_MedJSbiNoalygvxBxoM-TYt_32t_cn7UVP-IsaK0r3_EWFqNvkPSPILEUvCFXKxVnRKHZzNpNkNUD1MY42hkTA5IolFRNns065R6G3XkIsi2vmgpG3WP3GVVDIjgNkaPRVqNNggKFQXUpCMNdvdcvarO6uoG4031i89UqJbuvvStfeQJBWqTJHOKnkl07doDsEHDUK64r9p32be5wpXq44cnRNbPcBOPK6dS4Q19IM2aF3tUwhPrba83t7LqylIGYjjPZTd-Tk3lfm_KUWOGpbBxE52uPXE5vGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fwePe8IDJ3LJbTebyfy8CafHgQcFcXd6FXbHM9YTTDGpZaDSyUlgY48DtQb2cBhSkLkTKBoQTT_drDkqFa_cH5NWvuidLN_9YjR7PeZP8-dqkrLctcSbRB7lVfY5NkdEhDcqylA3UL9KnT2p_VwXvtScEOkzVykkAT0UMWo8QoRyfnSF386mGb8rBd7-cLeUW6jVzAAdlMPlH3YVvYOH4e6TBaFTuG8aCTGbdoh5IJIxdob_ifDmLNFgDUsOl-uFnf-Ym1rQfY5Y71M85QT954Blbc8Ez0iMLX1_bbH2_ZSt8m6P3PNoXFoozx5RSBhgaHm8CtSSu70OXmWjVu4eSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FclzN4J6pKCQR2iNUrXm8e3-YsxrvGfyiVKd9sAngUavEmN12fSJy60rU9k4EZnWe23PgjFKWCulkh6R8PjmEF-dyBrg06qyru5Nt7p1CDfv3Gb8FdZ5z_5J0jSx69q2-SpOsFIJToZyuGvXHxSCYbue2WjSRcpSzi97C4uOK2UiNnpdUpHOu6ydwYqZsKA4XwBp_JiJIhuwhZII0YjABWP0jmemGfLBIxZ-SJp8JleMnD0XyYlMAPxBaHuevRRJ2bd8Sz7fmPZ1WDVmMCiMHLFaNAn4BrOxusPxgcBaW9tJuImzeN2O5em3k95X-k0y536PIsdDogkydEW3D24yPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fiqlLJsdNp0wUqTiXIW3BYys9Aza9F-D6rccH0o_TY1OfWA3Y2WaZbRoe2Fq6yhw9h5AMnBxfMJhbIsM3HknpiecvebPzEqLekB7dq_fOVjUvG1HxlIodNz6GZYoP9_vIzy7xpQioFF3PTSZtdZCx7dy63shKoIqo14qtFR2v4sVFtwt7wDHYZ_Dc88ykqqLjasTIsaV3Nz_QUUGy4izln8vqN0-5BVotTsam99_87DnhxGHSUOEWXii1xQiDmc--AIjKkshQHra0Xw1s9vFWRQfJZhzFlGyVwUFUHkCSozy-TAhb-m5s-VkGPjNSmqtYUknWupkaGwhq67vmMUTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VDcezpMVPJ_rkXCY3cw0RPXgjEkHO5vjQeRsEjVniL50oDAdQj4tmAd93-kAx-lLluEKeJjQsIdEhzAtHsBtSVLzWusZbJ2khXkUp_XQZtqF-yXFt2Oa9Y_UP6f7e-wMcM-9iBMouR8GvVnkzbrIJlw16qNw0nO8cdxoPbLoKrXLLDY7Ztq0MeSmDduAxmVHL414vhhP5BdeNJWO3UeXMF5U-JPeXSlD9eHKtJ_1L8IGpTjgjJ_orEs4I3W2fc5lscm8RkyGwZdXmDkoUEsMAjhcRAnEZ5E_QLU27l1TnHakz3FN1wMi4LtHgJ4NxqbPaXZYas1rWb2GqH_UluMT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZwT3SoUe_eVs3TWL6Cfue3oInu_9G7ZoQeDg0NI3M1ECR3mmxrC9f1OComJ8KTQp-PbHUgu16RiLXsFf4CWRJPf2kGwSXh1ttVt_Tn4W8b_Mf3X2SnWhFqHKuyJKUPe5mRoZbd5BtvgijMLxg6DBKYkpcSkLy9cN0LPcQORqDM6jXp1mDqmun_lZM_ThVMU8Vz4xIbC42Fd9vwQUHTAGd5s_I9DCO5fQpVNYWa5VFr_svITdqvwDTkVWX2FNpP2CKR7AZPWNaRDSFlNXOaRcJbbCoxMjl4-eWl-CP9r8zzDEaktJSZcGGJ4d2tnwEZF5JEPKyIUTulXqMYS82kH_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/RS2Km5hwOHFXbUu9dXNIg0WjL_EtSheSE4Ta5pN2FBNLU56sZ8ii2VDPq3_MPFNdFEGpVs26LDN6JVyb2DAH0jPwhamcZjh050w9mEhLc-Yr1koY3vjC_zOoQQVQUcNE9KFwQj4Ts3jSlofbAnPSaBKmi-pqHKfTsJ07VF4icYD2Rz50Jcuekh8fgmJtskCtNgYlbao4N_aVf5atzGeIyRQxFLlk4iQmt35-u6vEgmkiiIw_XvgyOdfciKlQWUbomOYSTrwOoGmT0y70c7-F9ICUbJ6y_i6DODVto3kbGMwb1nqztyU1t2jN5nsJRKEJT_sJGuOvCZVYmbVH2crwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Oq20IRyFrgOPYvGFsDg6_9kxnCLUhCf1_WMlPuZNYXZeFmEKA-_BE3pq-OMbQ4gHxQAFd8DmXETM5o1G2LWWYQcPEwG5utymvX-G66nqfLISmQTYylc6haf6YJkZ5mZz4zcT4SM8rijanhA8JRGFyQULpKHEfg46ktFSkph6llzsYEA4iefBXq5gILg8eYqJ_bDZ_yDktXmXvf0xqThv8sth02WwI2QXc5jRdXg0AiPG90HdFUx7R3Rap-Cfsu8pb9kckw1koftPi8cQgzMl4Evau5Bny3WnR65O9rTPRy1oWEey643gqD6NjUkfz7XluXneO8AVggmxGRLUhOwADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/dvrDbBHWAleqH2-M05MdiWIb3duKcz3qomETywrGh3KshRx9lkjjV3q7BX4IF4ROOh41UzpNolt-_w-28thRGAVpC7l5wZxQxCntPE6_fTYs3psPsCS3UygUsXmxihpWyTxE-_EHAyZjHOXs3om0ZRmIIFwrdtVdrQp_tYuKMG_eLaGC7oz3imowobz07_FV8eeTyr_EnU9vvWywWqbSyCoTu20PCGzibSaeBm1dToCpfjv8irPNowY4MJDzj-JqBTlAwLJmfZuzZXw35E3w8h4qyM9NPvVJqAG-ncKJxAbQNIj1mSaNNhqtyH397QWyZ85bZYMxIhdRtUdWz7kBgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mr8F7ofPfiXb5E0i1fnEXZOBwH1mSvIvCR0QfzbO0qwslZcCeXzi2exCeE6zbloMLnWo3salGCi62IgAtpc6xvezH0hh8PTfUG3HhCx74fFzf5qNGX33s3m1d8PQm_UkiEJrfO2pUxdtXUhY6ti2fekFmBvm0dE-j1ffJNevKWAJhQV2LPsLi9fi69HnxBdjqA6SiJVPQ32dY1MR2VQh4EqDIMn1JsHZUBdHtnc0D_tfqt4iyIaQq2npghIAA9rVz0BYt5P3N5FZyiO3DR64VGb_XLvfV0Y-SnhrrEB4fluuueke1wNIUAnki9eTJ2KVR8QCxjee-r0zDy5w8q_9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aqYKSNcaVEa8k6vteoTYiYlWjkPUhLmwKR37iO0y_i7_PUcg7OPx-gQ1G79xU_YQpwoIeRAVZIeHKEthaj4ueLoNpZlxUMwspdhwfKZBKtYzHYAG8zG50t5-CIBmnKTIsge0ytojuukCAom6Nr2nIhe-vZa7PsWwEWrmQpSuxDKapRzx24fTioSmB9Wfv2FerQAK8AjlzUlPIGXtBZGXlh0dzpjG-XYBiP1dScMFPnrBghi936R7cD2ismHa9QI5vvN7OeEVuhLqIpAEozVyx98N05T6qNFg0PCH6YTf9JNLU3t9ydyhadF-cy5j29Yk7U043JEm5tmwn_mBF-uIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r2YuD4CN-XmtCdklRXoeDvV42PRuoAKi1EJKafkZaDUvD8hT5rMyRNjjDFQ1ViQd9gTy2MaLZxvC8n6eSm7wFqsJMvW5GWhzebcMf-LlWD3mhKxgiaB0sHH8jo6F0iaTO3tBmtcCWiNt4VCFUKI8SMW7eLVJz3nbYxiTEg4DmI5MBSby3qjwU44IKxRffqg5_gYL-HwrG5x8fs2c1A9pvz9MPd9mcO4eoBQjt4ke8FsknPNATSu95ZoPCqkRCRdgFYHSpdNAYPYZmTpR3qww27aZLPSk9ylmNX2vl7tCXYGveDSd2p6Th99AYI1zeicA6sKN1z02l03ab9LM4vlZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nUJsf9IwkMPJjiQKVJB4XzvYzvd8OARp8X_on2YXNmxNKz7YfIcKn2fQnyEoPAp8jOE66sJYbgqWSsAb0vxcaEZq-_oo12lmJ-CPnHK-Eq9u3pHIjSobkc5IzDPAp62zilKDDRd9mR4o0wbSVEnKr3aor5t047XOiQvbavNsCvav3ww2VDX40DHv8u13bwBCLNQT87mehXtgE1eeXUZB-Jh4lYIDhh9Yu2RTz-cqM-yxl7Mlvi7Rj7T-i95PJBXRFC_kM89vqLX8zc7-O22w7yvd4X7cLBTsHtBr6ai8qd5YqxZG4WYqbpKQYoMT8KR6XH_Z0v3GKcMaBprv88Qv2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QL5OXyLA48F28RtOurNtPCuy3NUWihdKcz9f5_ucaG8TVOkDMFVsiGtmAT3gT3jx5PQGh1E-6VCodV1C9yVp_biNRbVr5Bg5bcYgT07hGNo6Kv3x9-Mb8b8qNGJqhM67Sswm1q38l0SdlSkckxaR6z0fN_MVlVkrtID_q4v8Emc2oJ2ABDFoI-qMAjqECfjOe_anNE-o96dipX83Drrn2jT4f0XF0XIJkl5M02tw1NGeyBna-q1q49fyjbUY1qXSfdkEFqvsg4xymBkt6NzsKdHKXuVRQh-lLdXugZiWyVGWbzankel3cUaZqJK3Sp7DkfsbcHuO8rXnxjZiuJRrBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N7XY2-T5GpSngMYqFMSsfVX0GlmCOxbi--mLOgM4zCNARWprx4BPOedk53cj_X_jmJuBBgeexDLQvTKdQiWUaVhK5QBzYm5nvtNJCY9QqDEaw76FQKuK823cIcnMPfaT_l0V6GdLLPiBb2FHFIn_O8bOXltVO3N4ECvmhtMpuxM1tgoIP5dUw5qIiX-_C1qXO1bqGEJWOLIzjVurmA9pvZq6HmaLvY3TejbHQWLLgE1YOQET0gBC7f2NtqPva-Wd5BafdoIFtsvhZYgIkKE6yPw9Rr1XY5dzeEvbtoXJIYEeWi8S9XhgGZJn58n-tGargDyoNMEh1EvmZFQu8i3DeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=AmmOLG22Q_Pbyufgk9XGMe6NtCts8igeTZyGkyL9Tm__EfVFdC_Q7LkEjmp0Zuv3DA39hc9TCsVtsFZTo3I2JjBG4Cj2c9AV17rcAhRpUTx89vJDItQmZKIiGSgSos2uWvqudgj7lPTSbdMiHg65s8so01xkLHVMRXvn4oIBMoUaIjxo_zMmM5nV7XTXFY9g1RzeT5FvIKwP2l4mRyQoxLBdZ8OxRVcqIGyNBOsbsE28vv9CAMeXOzHHlACEC_v10iBOtTDis0TJmLCcQhwnZq9tpn7bnc_3X8RfPXZh-TKJfQXYw1QqpAklE6eK0C0nld55wLJbPtP-VlVybNyb0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=AmmOLG22Q_Pbyufgk9XGMe6NtCts8igeTZyGkyL9Tm__EfVFdC_Q7LkEjmp0Zuv3DA39hc9TCsVtsFZTo3I2JjBG4Cj2c9AV17rcAhRpUTx89vJDItQmZKIiGSgSos2uWvqudgj7lPTSbdMiHg65s8so01xkLHVMRXvn4oIBMoUaIjxo_zMmM5nV7XTXFY9g1RzeT5FvIKwP2l4mRyQoxLBdZ8OxRVcqIGyNBOsbsE28vv9CAMeXOzHHlACEC_v10iBOtTDis0TJmLCcQhwnZq9tpn7bnc_3X8RfPXZh-TKJfQXYw1QqpAklE6eK0C0nld55wLJbPtP-VlVybNyb0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zjhchn0RqvIQ1q8VkJnS78ChpYNlDxW7AaEnzZC-ESTf6MT3v5-HAqpiHdbR2S_fuB3Se5cWhQrLRNLGYyZijTCvCk4ODuSOaK6lMFFB9rvwsGX3stthfUBpLSuvCi5aetrT41ByNw9WI8pGGOs3otQ5-7SrDBkmccnuZEql450ZTjpXtuHWcEidornsIzouY7cnw2vsTGXr9syX0MAI1vkuEJgeu2QZ3ailrPjAXgiksTv9b9wkw9MgwQ_m-RprQzQb9CtmzwjbpoASwDjpNiS6b8ahVUwVrSMp3QWEVRlQmnzTYsaR0rJDyw0ZzMOp-f9qDhCe91GpfMG2CM6SZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ow0gwzU2O_zP5VFgZTf1slUa1Moi0885JscTPux5Sn3dyurydSASSHyh3B0Uljc_RAOj6OQDq1DfMsGLIyDu57bLangEcWUE7VFQRimEX0wPFVNEdQQ2tUk2-qb0Q8Mt7gGLZ17oaTteNckCKTNb8eDdFprK5UAMmgXwsb80MrXRPBrqEhG-Jw94t_-B-1FH5JHgPvIRrjY--gGM0YP0WS4I9FoNdYQrZct164yZH-wm7owYnLFg248rJolhWM60mKwLuLlF4eDkXsVZAYS-CP_a6h6_4FTvMnuf33Pto6KYfzrQ33Wy8tLNsD1Wc9K39_MGgHwiPjNSaRaxAN1wIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HoKpbCOAlwAJd7zxHUlgm886cw01g6t7hv3QURP1LUjYhmWjiJFEb9g_adFO8dh1CM-t3XPu5rb978DPptmuAIP_dRikD5-0rwQwtQdtluHu_BukMLvCsDG1YEvfEyXIKH661neCXloLaBQwVqxrZ3wqTYsfG_c6aGUM1Ro25vlTTt0-fvQ0CY3to0ngq67ne1woO6WXe9PeW5P_loGgrPvouWaW6fcB7hroWzxcxLXMdZEEgLYwR3aFxTYX3LX0SHviQDVIQ53Y-L0kiicpunGtuFnk7aYNHJETO0JKSMK437EYfo4BoaiQTR_LFJ6pwY4sWtX4bp6poX59MKiBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AKNKqIAWfF7yuzb6u88mQUjCaJ-wOFA1x3cbNrM8pDU-KB7quJydDCRBNiMhZNj866cCCrRVX_S68RJ406qgS7Oxnvv789xrx8Sa9IjOFXZSKM336JI4q8v4QeF6aRtdXrS6w89O_LyoiJH30iDFYuHzL6yn24xqZnEFSUwg6JzyeWxWdXnBP1EzZ_ek2GDuXmA-Hek-jdG0S-ohJF01MfxXqd1eic3Ir8NMErIGXmqJOFCejAZ0eBdHY1Q6Tf6fun1huffl45DTH4ET4DtRMoBJXa0rZW1NGigHw3i-tFPOUc3KvEHEc-OfqRg_8XLUw_FqLKyWU8Jk0xBT-YMOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ldDEa2xtiSzGX-sT3Zn7dfi15o6ZWapOu8-a_lULbjd5kv7r410LamYdP53swrqxBwHJ7Tn4RVuT9CMpQ6BH1CrhlLBrJ-pxhSzxHPGoQrcAc-M12D_qWY_CBhjfFfLX9bX0sZtWD0Bilr4L7BlQ9LCB0hyNhi74gihEI4CgtW4GeMkXBSdb6CnLq0JZU5iTacGwH6NuR6LZUt_FjiiuSCksggp-54LT1xEVzhwKX67vp8OwWE6NXfw9RSSbxvEehDI61JKxjXeWdbnn8oofk7W-d-jzPr6FUOr_5usLWUkvAw--w-twst7XdSSBwifJ2Uc1RucWHmwHqzlW9N5cGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P2bcrVqu6WvuZOvSW6WY73oP9zmL8WO2KnOFBsSMwldrw423e7RpAeEZxePPlYi7j85_ME0DpwKsoV1YMr-l_jak5tDE-OXgpfUkHgrGTVwoyx4g1S_lPNvx9ZVdcEWgmrS8pVNktESjF-XKLhUggNjhEJIT7dPT9biRAdhw2Aj5774N8EEBn87r88XnFN5_jr4ctyQ72Wc7Y5G7wl3umPjht3VDG5xB8oCMQywBISeyTw4_6Me8dVLYHUDNXYpxzCPLmXyUAuCm21lg-qA9MVTXDgWYDcg6AJqxJ8jLgp15fUPJrI4Usz6sGwQUo4YqdMF9zqKg5kWOGQYLwXy3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iJJPMenGFJ2YUtnB424oFqf6O2UYE15jgK3uJ07selR9f0IXVQ4XjSunB3BTV-pkiqdrnL4DwUWTQGn5wDyD0Q69xHVRr8FJLsgmrvidZKs8sTbdqzc7xh329jK-E5PIL7PbJPTFpYaUSXXAiMaTkkGOaPWMdfwntlLDC0SpbYp2sB3mIqhAXkGv7YpcCDJ-SwGNc-fHlXaOvZLgidyqXbPrx_POaBOQBIWraD9xQJUY2GbaX6YEyDI5fruvX1g3xxip3fse21EsSM1J_5VmqDOqv6P1mXX1yjK4Na1DVLVS23b_9g-Ss5Q5lBtYF-5d8xyHWr530wHNxwBlfK-xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hEbomwWujcLUfrslJaFNudYjVemTos1BymHSadhVQQxVwyg-RJLgOLZF6Dj1tcbSelpBdSS3BpEi_5yAW0R89VCMI2F5xLqhWfTA02EYjepoJL43G0Film5i2PutMjJoJYZQgTjSu0w1Li329tCl3_OQ9OUdkKBxuJL74wuUEBJGimdSabUBO_9waUwj6tqd-oeNyuuqQCxK41l-AJ1pClHCcEQZ1UV6b5K4CbOd_QLAj_eml0o4AqpuCSHJqlgZvxD94sx3QGj-3QlHW7zs1Sw1QUc3oZe1WT0simqgLv3nsdBtYQcytkqw7polzwKqnWFYRjnbgKO4c7ALge78fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aPmf_iN9SiFpdLL94A2k85KXwXYPZGQFOLnshCSw_kZE2LexhRtF65vuOTrrrksZy1nuKq9J8KPso9JR0Y0wR09oIAaOrV2Zv266h5UtbS1W0xAeNyk1Zgsj4pkvxGgGCPcpK6ELWEjGkPaJfUmdXID2FGuYgeW0a5JCeg0S65VIhbWaqri4iSEpo8S5v9wNBADL_p8zetTaydl-X92LiOyPSQFvPEXuYXhdRDpE5VWxUTy6_zUFuL1gMJ3B43iZWvIRZh9tDywivzw6iBY9TCix8gjRPhfdBaaWpovQnIje7B3Ll7oHp84VQcwQcwB9WZh0hxKhQLJhGYtNDOEIjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eJWP88PMXanK7PzJQE4fg4kCemG3_I6IdM11L-F8bUMZqI7mTjXcHdet6M8w0lz266JrloSzHY8-OvIucF3yknHcqG0A_7D0Qv34cQCTe9fVWflG25e2kjy1IC7uagfeKZaL_tabJv56NS7N_POhW0f4CA92d40BI_JLhw95buVuxx-hb6XPhc6XWAt-7Ty9QAfHD1EaxsQK_6tmxP7FcCld1xNv0yqtIkNU48XyIx5ytyZvLnOGeY-nAvUKMK4nUSekpEKK0ep-M1W01pBwF7rodP4LrmMvCB7YS5mSsDzGn4tfN6Gt1PKSwRmlUs94-UJDPlX0y55jPsCQaygBpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OSvbRPdfHtotyXmWEOplUXPe0c981qCfBzjrIBBLlDFyoQoo22qJA5WAWzTsCmS0piYDtHLNWUgUFb_FY5XmDwONNZduzOpkF9-PTignVj_F6SBzepg1--zemmz2RzPWhQGKe8JfZYSBmrJUxgNpsCTdB-mkHyHPs5zD4XztZtaIGt7aLTnA5KcRegBjgK5ansagKYzWNSOig7HCINW19tg_d_HzfjaWPILac5sMcQ2xn3_DOifixsmFb2AHA79N4rzx2mkBjBWAwZcXk81tXV08hFB0746iG-COgLC662Qv87wCK_o_XBG86G9KvQ-qUil-35FdaX1iUUjHqME8uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k1Nu49tjggzuDoKx-KSZUfnQhyOvu__wf4zeNKDbvl5lG3imkNVNrLzy7jmj08SUDi1ku2-xuU4b3P4glf67SFhjCmAOyfepLQ7TCgEnZ332prsSowZx4zxEHMaoAM8c94GTmfTPdu0K4HtwzadEwtZTlZTKp9naow8KKQce0C0OyEZOYblZU4QbWXwLGBeaa6GV4mjV7FKnQ_rR-wAEzj6dO_uhPeqhinsv-KVB6cV3_DEWv-I1h7udPfaJQBDN9aSoeyYSRzXHhSC_d5d1wuUweLjityyIXc-eBjHueOE-vSkQPBMx9xxCxnnLuf6AyJ_-ho6MFGxYzURooiKRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DYuycOttJqV3j-iCFuwgF3sFKM4XDVZAnk3mrLZ4K1C2R5VThAIdwKUyy4IwvFuSmda3rJS2nx_n-Wz2VI7d38uAJkpwdjMEZNHNd4j5ieoFSHQSbV14KnbGsh51SWcpYyMpvZkDUSaTqTj7qdEtIOcTGMRpOBCq2kTNFqHAoe4QRjUPhqKBlu_8WSf8o86xLgOCm3lR5OcAFVPsqYYnV9Fm2N-IWXKjvoDhLpF2nnAqYB0Q7G-8fv8AwB1PCtwYQXTVrnH29mMAvLcPg_3aPUWFgfcqtO3Z7IWxQZ84q_8jkly_Q_N1KbBDiqEztg-KDUg1-ln-u35ruQkDlVt-fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S5BdFNRwDw0fJaa5DMb9c0-aleHTyvI9ayWWlN-Qk7azO9ZuicH-zgjYTdVwEo3Vj3Hz09yUeGzWFRiAz67cKmUr84fW1RJMSN9ZBb8ucj8fSBbVEmz4Phd85DfsE-b4e19dxj1bpjfu1A7m7m7gmsk3giEoM2i779PGW0h8tyv8BioQP9zCmNYRi56Cvk4aIZqH1bPn6Lzz1ZU-UgvJc1tyEd6S71duvvdHQEgQ48nyWQ9NaCPTbLU_uIRVHQ36RLCSTEnr_uSeNioJjfBPFyq-ToEgjaoScuvmb9AZtDi-3WAm8typtmylaywqPjnLiQ3qsCI4z-EhgL6AU9-rHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ISsAEyFv4Iil_EpeWErKIYtSpHcGdnrEvYHOO3LImpFm4VwtJnp1_yndmkdFF0uNJlhCEkJtE0CiBzLUejYyyc-QxEX-8aj6XXht_6b6uhoRVvZgzCjB0ApOKxb0IqFTAQB9wTbaC9IKf06dlSgjQ6QTbQVsq2MHsXbPUBhzBTf3PBu-AhhjIKWG1qFI1XZlae_Bo5SJ443fWbMypZJlkulHN4I4DcXHm5eyo1hOo0Mv6kl_nNSq0nIpAe2wgrO5eqAasQTOkOPgAm1ljobSpChA1pGDQAZfdPCix0e4VAnfHczTQdKPiXQxK0uhavz8abm5pxu0wDx6nEEOVOszpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=URkKKZtw7Eigibl-1NCrHZv_jeZz1tGLfaFpIXEkHyMJFXCF45EUL5YTgYO7VBdL9Q-_sSIGMGy-KEnMtL7RnlDWa-UBNMbeC55tfmKbNaMFztGar5zdFYLbCWDqk7j66tpkUX1F6CXjX_aW9W13JF-HcYyljWQB5zEtVEm6O2W2EMJ_GE3yItOtLm72ehYtuLSNEc4NQcPkOnYTIhtYIiyfCUtcAFPY1N5aVTfqP9Rx2PKMImObxGeDRSw1Nb1_sJCQh3ShALafYQaQssW_uEz2HGmW_qQrIHbfnjuZtg2dJ5jcMSlTxZ63rDGfGzSZmyAsCJElONaVgopmJHXxEUOYzDXwILzPs18Ei6iIg68vdm0pjpjcTuVN4pNiQ7KNuQyUb61Yg7S9IztW9lnHon_MvycnihMvMAyHtVIiq2zOYIfhS-X1w7-iuB4jtOkXzlWj4zdbUKd17GCD6sOJ_ZVcJpfoQVpqqr319TwjprAAkpaoBRCTTyP4fnIH5WwwFgbShIuTp5NzXMZaDEciCX5TDrWvPU6qT6yYZ34a5fecIMbg1bJdACTg8ZCUc08E4G2O5g4ZB9aYfGt3HilBFRxRNTVLDyczMUVG_36I_B0yYnzPfhEXwjN4ATasAwGSn3XwQhevgumFy9XFlIgwklCjCTC-MkkA6RptkRbGXGM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=URkKKZtw7Eigibl-1NCrHZv_jeZz1tGLfaFpIXEkHyMJFXCF45EUL5YTgYO7VBdL9Q-_sSIGMGy-KEnMtL7RnlDWa-UBNMbeC55tfmKbNaMFztGar5zdFYLbCWDqk7j66tpkUX1F6CXjX_aW9W13JF-HcYyljWQB5zEtVEm6O2W2EMJ_GE3yItOtLm72ehYtuLSNEc4NQcPkOnYTIhtYIiyfCUtcAFPY1N5aVTfqP9Rx2PKMImObxGeDRSw1Nb1_sJCQh3ShALafYQaQssW_uEz2HGmW_qQrIHbfnjuZtg2dJ5jcMSlTxZ63rDGfGzSZmyAsCJElONaVgopmJHXxEUOYzDXwILzPs18Ei6iIg68vdm0pjpjcTuVN4pNiQ7KNuQyUb61Yg7S9IztW9lnHon_MvycnihMvMAyHtVIiq2zOYIfhS-X1w7-iuB4jtOkXzlWj4zdbUKd17GCD6sOJ_ZVcJpfoQVpqqr319TwjprAAkpaoBRCTTyP4fnIH5WwwFgbShIuTp5NzXMZaDEciCX5TDrWvPU6qT6yYZ34a5fecIMbg1bJdACTg8ZCUc08E4G2O5g4ZB9aYfGt3HilBFRxRNTVLDyczMUVG_36I_B0yYnzPfhEXwjN4ATasAwGSn3XwQhevgumFy9XFlIgwklCjCTC-MkkA6RptkRbGXGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
