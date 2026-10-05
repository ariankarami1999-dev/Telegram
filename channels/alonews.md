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
<img src="https://cdn4.telesco.pe/file/QDeIvLv3KAu5kkncoJ48Jn__K1Tm3rtzzer5r2MJAVn_eO-E0EzBqDMGJHh3bi6F_XHRgf1EVYrD_Tm4YfjQPBAbfiM4QA7ji7ezkbXXy9Ad0kYlDooYL3PveqMe3KfKtu-QhneeJHbMiBNqjzpo-2I2C1djgZRcC10o_McucTNjLoOxHzT0F1lRKwX0ZnBG-v0yVXcACBszncNNOHHtlYjGdEURDrdZwvFijN2htO6q42jdG0e1CkKos3B3r1cA8G5SkH9Tn-ZdGtWSASPHhVIijjcFZNALFx0HaEI9fbAxA1JHsJPJ4HPZLqZrlIYsMMbWhXRWFcpBgAAa5RCUxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 12:49:28</div>
<hr>

<div class="tg-post" id="msg-151048">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
تحلیل الجزیره: ترامپ قصد دارد حمله‌ای غافلگیرکننده به ایران انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/151048" target="_blank">📅 12:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151047">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e7be5e65.mp4?token=VmyZtW12jrSa8nSGtg-q_1mgDe4ugjYp6_4I7VYAHJzlxkzNhx7RKfYmdPBuXTVHXnDit4fl3-pqhlK6wt_T7aX_MdD42npCg1AAFYhCBGjh7cN0co_b7PDuMAxXVKeTMqdrmPlexCLnyS1uqLqpyap8MuR4534_3cS1denlmycYC5cAGcldVA46QaPcDJF3F6TiJr1923z1Tj03bFH9hfDg-JPM10v7y8kVinshcCRwSoIB-OtyVMgHjrC2X_tq8geOaqPuimZoaN6CtFi5B_ntwRBNFoyJD46egdqKoektBvzn8W9_AAsu2BGCC3PnNgbSkZCx8uVt5fbU-CN8JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e7be5e65.mp4?token=VmyZtW12jrSa8nSGtg-q_1mgDe4ugjYp6_4I7VYAHJzlxkzNhx7RKfYmdPBuXTVHXnDit4fl3-pqhlK6wt_T7aX_MdD42npCg1AAFYhCBGjh7cN0co_b7PDuMAxXVKeTMqdrmPlexCLnyS1uqLqpyap8MuR4534_3cS1denlmycYC5cAGcldVA46QaPcDJF3F6TiJr1923z1Tj03bFH9hfDg-JPM10v7y8kVinshcCRwSoIB-OtyVMgHjrC2X_tq8geOaqPuimZoaN6CtFi5B_ntwRBNFoyJD46egdqKoektBvzn8W9_AAsu2BGCC3PnNgbSkZCx8uVt5fbU-CN8JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی جالب از ناظر مسابقات در لیگ افغانستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/151047" target="_blank">📅 12:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151046">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh4B8ae9KZwRBEZvBeJfNIs2oLIKsIEfnB8kMnpfl7YOJNpLkC2-MMGE4E0fN1JNHSqiVuCjYTR3UK7cRkhAOIKVtLGjw0OJ8RrR9obd3Gpkp1dJobkmC3sM7RMyYQUb4M1B-VxWb0eD1GKeaHH-z0vd_A-5OqBLltaQk9ulABwnkRvrbCsx7xY-NcmgHsrTzJ8f21lHprAPRd1zWRXwOSedmlCjdejoDrh8hV-AT7rokqo1o6cSAF_48_4U54TVV3c3TbH6V1qeltgBoP1tLprqc_czS1120fPFVzFAFUt8bFs79rxMAL3UqoJV_xfX7wfaFZv-cRRX_2_8uIc8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر می‌رسد که فرانسه نیز در جنگ یمن دخیل است، زیرا یک هواپیمای فرانسوی مدل A330 MRTT در حال حاضر عملیات سوخت‌رسانی در نزدیکی تنگه باب‌المندب را انجام می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/151046" target="_blank">📅 12:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151045">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نیویورک‌تایمز: محسن رضایی،هشدار داده است که وخامت سریع اوضاع اقتصادی، کشور را به یکی از دشوارترین دوران‌های تاریخ خود سوق داده است!
🔴
این اظهارنظر صریح و کم‌سابقه، روز شنبه و پس از گذشت بیش از هفت ماه از آغاز جنگ، در یک جلسه عالی‌رتبه دولتی بیان شد.
🔴
کارکنان بخش دولتی و خصوصی، از جمله پرستاران و معلمان، با انتشار مطالبی در شبکه‌های اجتماعی اعلام کرده‌اند که به دلیل ناکافی بودن حقوق برای تأمین هزینه‌های زندگی، قصد ترک کار خود را دارند. همچنین، بازنشستگان بخش دولتی در اعتراض به عدم پرداخت مستمری‌هایشان دست به تجمع و اعتراض زده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/151045" target="_blank">📅 12:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151044">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evuiCJGYRy_R9dPimPGUzuicyREbSoROU3JJMq2BWNgONdbdaUIrpLTYqxbhgOQ2q5G8WhcfhW4zZjwZ-87ImglL3WzfDU3KBb8DJzJ9xJop7KoBJO6gcAsIA5WOlr26Nx-Y6ZeIOtqHQYxyLNWB41KjDpvankbrY5YWbmDpxPo5xoR6DvekekRLrNxBQ9qBlaohoJ2GjG1Um7HCf-p1pwVFgxlh3mQRblvbtjsb7DlArOlkMAh78U2VXevjICeSDRb1rFLAmw9ArMse7A9Fc7syoYSLOIGECx9ypLZo-lhChhMqWJ3-bpbAFTVp1I9-ZQBCVVpzPjB3unrT4msjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فدراسیون فوتبال یه بازی با فلسطین ترتیب داده تا قلعه نویی بالاخره ببره
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/151044" target="_blank">📅 12:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151043">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=NytsSjpOEv8P0kmuKZZUXPHOAZvP_sARxPM4hvlT2cQMcBhTReq8H1xewe7hiB0R17ifp13oP9pl2OoDXT6Az5vpmdqnUVIDJkowHf6MoHi_thhSP6_v3EnHtCM8oNM4Uu3iwQ8CPpfzZujPzAQQYpb0X1L3vOgnTR0MpHW-7-y99UTO8kFg-W_2sxSfdl78u31z2MMQnAnSMyzySu6ZKcOzC-nFhdeCvWN0OVfl_UoyWzTQQlUr7czF5G1W6oC6N7nirhtQHjQ7wbfDMYl4konwgqbnA8SNOrqjEVSohtRIJDG08eGhRMQqKuBpcGmmrYlXNB3qXdjMpsxtcx2lfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=NytsSjpOEv8P0kmuKZZUXPHOAZvP_sARxPM4hvlT2cQMcBhTReq8H1xewe7hiB0R17ifp13oP9pl2OoDXT6Az5vpmdqnUVIDJkowHf6MoHi_thhSP6_v3EnHtCM8oNM4Uu3iwQ8CPpfzZujPzAQQYpb0X1L3vOgnTR0MpHW-7-y99UTO8kFg-W_2sxSfdl78u31z2MMQnAnSMyzySu6ZKcOzC-nFhdeCvWN0OVfl_UoyWzTQQlUr7czF5G1W6oC6N7nirhtQHjQ7wbfDMYl4konwgqbnA8SNOrqjEVSohtRIJDG08eGhRMQqKuBpcGmmrYlXNB3qXdjMpsxtcx2lfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدنی وزیر دلقک اقتصاد: درمورد قیمت ارز از همتی سوال بپرسید
🔴
خبرنگار: همتی هم گفت از شما سوال بپرسیم
🔴
مدنی دلقک: نه دروغ میگه از خودش بپرسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/151043" target="_blank">📅 11:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151042">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41508d2063.mp4?token=RPWfE50sWfPQdigU6OdO_GUgFpJ4X9kfhYr3YPR94fEnQbMxlth7elbW5lW-_XWGl0nyYYjzZNk2fQEYFocLOrZVVLYRpn-O3oHfK5G6_lYEmXnN_Bei0jgc8jmB-i81-4wno4vDRQ3Bj8nbtQcqytnjJUkIOQrfdvtjlf3rXE4xadf4GiVZ8d5DDv86I_dWmJVjm0Qw_Tx0LC4kaSP2kg0sWvEvkQjmQ1nwe3eOfgZazTGJ8wF5n85asL-ZGsll6Bn-yzUlef1FyNJZ-4I1kwOhMg27F4op9z_dFEmLJ4rWUAdqbcBsYyA-E-G1HJPJ-DPZxwk9LqXWZCJZH6pdTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41508d2063.mp4?token=RPWfE50sWfPQdigU6OdO_GUgFpJ4X9kfhYr3YPR94fEnQbMxlth7elbW5lW-_XWGl0nyYYjzZNk2fQEYFocLOrZVVLYRpn-O3oHfK5G6_lYEmXnN_Bei0jgc8jmB-i81-4wno4vDRQ3Bj8nbtQcqytnjJUkIOQrfdvtjlf3rXE4xadf4GiVZ8d5DDv86I_dWmJVjm0Qw_Tx0LC4kaSP2kg0sWvEvkQjmQ1nwe3eOfgZazTGJ8wF5n85asL-ZGsll6Bn-yzUlef1FyNJZ-4I1kwOhMg27F4op9z_dFEmLJ4rWUAdqbcBsYyA-E-G1HJPJ-DPZxwk9LqXWZCJZH6pdTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صرافی omp فینیکس امروز تمامی پول کاربران خود را بلوکه کرد و دیگر در دسترس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/151042" target="_blank">📅 11:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151041">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
هیمتی: دشمن بازار ارز را هدف قرار داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/151041" target="_blank">📅 11:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151040">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
خبر کوتاه بود و دردناک؛ علیرضا سپاهی، امروز همزمان با اذان صبح اعدام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/151040" target="_blank">📅 11:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151039">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HRY_prHYOBLpQebY0IycfOvDmW7tlrtLbOabT78WTtMLZm6BeY1sGwu1sJkaA_q0_hW_2AVHiIFnqDf4s2-CvCNixeEQ_E3D6HPTtGuW96gxg2xSHFmTPuc5s4utrqTaxxLpEsnRJNZOR2bI63fTYQDilh3-3nCtqaltl4cqDov1aUjfNLvP0GDsWzGHEIr7xuSe3WJ4r0wxLjuq8jtau8zXh-YEBrKbMm1-C-yd-ektKUU8SM2Hh6NfBFDS95SWDyXtxVFLbnBZUK8a81TsWBhUv8c6jXWhfhHfZt_tYTGd0D2Nt_QQ58LqD_CmurZYY-lnEYaOJZxLXqhqEsehWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبر کوتاه بود و دردناک؛ علیرضا سپاهی، امروز همزمان با اذان صبح اعدام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151039" target="_blank">📅 11:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151038">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
پشت پرده ترسناک دلار
😳
‼️
خبری که بازار رو ترکونده
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/151038" target="_blank">📅 11:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151037">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e89d14aa1f.mp4?token=sNrv-T2xDhq8uOdia9eQqEspyngWJqTkrdE-fvfL-ucT3W-q6DsihflQUvXhjLXal0AE9IIYHi6tZRAknzs6_e4239ylapB3xKivCFjhUvcJrxfdWwxf0z2N8ul0PvMzHktAX9YJ4ciDgkX-xB8np5I4eedqvOB8vQLmkPmHgyOwk3utQOh_EweLLvxFxfadJPQPI9t7mOE1tRhVZnUCDWVPiQZIm1874huE9u3FlTkxWEGrE5xI8Da6DMuJ0cJvdDutV7BX5q-twOsGM5PbjoDY9v_Q20lFXyQjjxsSGqA3u2h6Q_o1B_848TLoLt5yZhLA6fXs1VWzgYTeEriXADsZG3vpiLfvMllvibljMX83fwmLJ3LhFbJpaW9EzNEO-FySF_ErVBmsVaU8nXWBt6OxOnxEoe0WKdV5xvI7LsGeC8CcbsaCQC-jnFV2gaTyg_erRLf32a-3c8kIcJ2PqITl3_qtelcD8xoqlJAGioxmJJ3DNdVTDiwMbjMZ0z7GinAzRxakZ2JyhppcmeFZL2UOJxKOcy5qeQusTuYrrz_bYzvkfGyhmO1b9TVpvHT6igKemUYxMdI_OECkoYn5F2uuG6TOZSKrM7A4ax6RZDF_ptFVLa-43c8eIqkU2m71WVLlwDBAszMDBpu0i0uAsLIYVlzE_rgtok30O98HM98" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e89d14aa1f.mp4?token=sNrv-T2xDhq8uOdia9eQqEspyngWJqTkrdE-fvfL-ucT3W-q6DsihflQUvXhjLXal0AE9IIYHi6tZRAknzs6_e4239ylapB3xKivCFjhUvcJrxfdWwxf0z2N8ul0PvMzHktAX9YJ4ciDgkX-xB8np5I4eedqvOB8vQLmkPmHgyOwk3utQOh_EweLLvxFxfadJPQPI9t7mOE1tRhVZnUCDWVPiQZIm1874huE9u3FlTkxWEGrE5xI8Da6DMuJ0cJvdDutV7BX5q-twOsGM5PbjoDY9v_Q20lFXyQjjxsSGqA3u2h6Q_o1B_848TLoLt5yZhLA6fXs1VWzgYTeEriXADsZG3vpiLfvMllvibljMX83fwmLJ3LhFbJpaW9EzNEO-FySF_ErVBmsVaU8nXWBt6OxOnxEoe0WKdV5xvI7LsGeC8CcbsaCQC-jnFV2gaTyg_erRLf32a-3c8kIcJ2PqITl3_qtelcD8xoqlJAGioxmJJ3DNdVTDiwMbjMZ0z7GinAzRxakZ2JyhppcmeFZL2UOJxKOcy5qeQusTuYrrz_bYzvkfGyhmO1b9TVpvHT6igKemUYxMdI_OECkoYn5F2uuG6TOZSKrM7A4ax6RZDF_ptFVLa-43c8eIqkU2m71WVLlwDBAszMDBpu0i0uAsLIYVlzE_rgtok30O98HM98" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از خفتگیری بیرحمانه از دختر دانشجو در خراسان شمالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/151037" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151036">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رویترز به نقل از منابع نظامی گزارش داد:
نیروهای وفادار به عربستان سعودی، مواضعی را در منطقه "ذو باب" که مشرف به تنگه باب‌المندب است، مورد حمله قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/151036" target="_blank">📅 11:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151035">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/042cda87ca.mp4?token=C2i9F4_fwdeZ6TbL4hQ3fDT4rjKCo18scNRDDn-4Ih7CxM6EabNa8Rf9J0VjTj19qL9Gig4tVepJB5nEmvZK4RY_ckoI1XKYqRKBoaCO-Ld-2zN8_HVQHQzRWwO9pH0DxEPH--QkmPOzwhw9dkaGzyr_9UpnS5kIIWUbkkqEqLbFu4Lk912fV930Apn7DQOB1e2Rj8TQTDn_j3qi4emOfTi7XeujAuAiEDVzKAyIM-p7Na1P_1CnIbifyScky4zAig_zfsf_5sWK0ouFmpDIQUbqIi4MjVdoq-IBFit8cUHW5cqrBIWoVO_2FEx00UCwueQSON4ruauyCT_75u-TBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/042cda87ca.mp4?token=C2i9F4_fwdeZ6TbL4hQ3fDT4rjKCo18scNRDDn-4Ih7CxM6EabNa8Rf9J0VjTj19qL9Gig4tVepJB5nEmvZK4RY_ckoI1XKYqRKBoaCO-Ld-2zN8_HVQHQzRWwO9pH0DxEPH--QkmPOzwhw9dkaGzyr_9UpnS5kIIWUbkkqEqLbFu4Lk912fV930Apn7DQOB1e2Rj8TQTDn_j3qi4emOfTi7XeujAuAiEDVzKAyIM-p7Na1P_1CnIbifyScky4zAig_zfsf_5sWK0ouFmpDIQUbqIi4MjVdoq-IBFit8cUHW5cqrBIWoVO_2FEx00UCwueQSON4ruauyCT_75u-TBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار عراقچی با وزیر خارجه ارمنستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151035" target="_blank">📅 11:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151034">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
شبکه ۱۳ تلویزیون عبری :کمک‌خلبان عمانی شرکت فلای‌دبی گفته است بررسی کردم کدام شرکت به تل‌آویو پرواز می‌کند، به همین دلیل فلای‌دبی را انتخاب کردم و پیش از پذیرفته شدن در این شرکت، برای این کار برنامه‌ریزی کرده بودم.
‏
🔴
️این کمک‌خلبان عمانی قصد داشته هواپیما را در فرودگاه بن‌گوریون سرنگون کند.
‏
🔴
️او قصد داشته هواپیما را به‌طور عادی به مرحله فرود نزدیک کند و در ثانیه‌های پایانی، زمانی که امکان رهگیری آن وجود نداشته باشد، آن را به ساختمان ترمینال بکوبد.
‏
🔴
گزارش منتشر شده حاکی از آن است که او به‌تنهایی اقدام کرده است
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/151034" target="_blank">📅 11:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151033">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYkA-e-Jrc8s1Zhy4zSM1EEQBneAm-s3peFd4mQbC0poaw1z4ts8hpiyrSKxzBBd9q0vIS_5p95BrmqtuGuJmTyiZyS881AJv6AAe_95iTYbwlWLSeDx2sL-E6Fu8m--uQN_bkAT8KJ-vYekOE5oz_0-rh7DjWX51nU-hK9ZA-VjiPIBPa_GmeC9TTNMrwVIBlCNq4qDbQ_NjXq50ArlxyCZ85yJAK_MyNxCJfrk_hz_NALo4orOCGl8VactJWUasf_A_g7A4IdDBrH8jUy1mReFNT2poRjUHp_YEmUMI5lDIb4Yp8j54AZQqAI0q9tK83p9gPVydnufG8FxxL7zkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش‌چشم: اتم‌ بزنن، اتم میزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151033" target="_blank">📅 10:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151032">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: یک گردشگر آمریکایی پس از ورود به کریا (Kirya)، مقر مرکزی ارتش اسرائیل در تل‌آویو، بازداشت شد.
🔴
بر اساس این گزارش، این فرد از محل عکاسی کرده و اعلام کرده که قصد دارد به این مقر نظامی حمله کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/151032" target="_blank">📅 10:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151031">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
ریزش انس جهانی طلا در بازگشایی مارکت
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151031" target="_blank">📅 10:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151030">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کیهان: پلیس در جمهوری اسلامی ایران جان‌نثار مردم و در غرب ابزار سرکوب مستضعفان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151030" target="_blank">📅 10:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151029">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
آقامیری: فناوری از کار انداختن استارلینک را در اختیار داریم
🔴
محمدامین آقامیری، دبیر شورای عالی فضای مجازی، مدعی شد ایران به فناوری‌هایی برای مختل یا از کار انداختن سرویس استارلینک دست یافته و این فناوری‌ها از نظر فنی «عملیاتی و آماده» هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/151029" target="_blank">📅 10:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151028">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
مسلمانان در انگلیس با برگزاری تجمعی خواستار حکومت اسلامی در این کشور شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/151028" target="_blank">📅 10:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151027">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
تسنیم: در یک حمله تروریستی به گشت انتظامی در بمپور؛ ۲ پلیس کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151027" target="_blank">📅 10:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151026">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bup4I-qcMKVxhzcyf1aPr_WKNsdb8eVrkk55xXjoXbY0XIEXyB5zTTJEvaMCaNP08HI7PcujdduSp_xejdVy3nGH8jZr1vHAm2mEc1Y01mfrUHHSIa4HLNovBxX_lfdFC1kDPo2lWQuG675pEc-LgVYHB8TrpH1iBxSrklk53IhMty7UyM0judjVQxCyosMcI8poT0TtKxNLLeRG2VTKmBnOT-fVJkX6SJ7dOsfCK3ujf9BmQ_6CETDgh_U4KhjrJKik0Nc1-g3BUyTATo5HAulf-fPUeoHdJXm9XAz8ZabxTGs5vcfsm_gjhXHlm4UjNNJQu45H_UBEFIfxLaIO4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعلیق پروازها در جده و ریاض
🔴
پس از برخی گمانه‌زنی‌های رسانه‌های عربی مبنی بر حملاتی از یمن به عربستان، عملیات پرواز در فرودگاه ریاض متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/151026" target="_blank">📅 10:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151025">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
یک مقام آمریکایی به نیویورک تایمز گفت که بیش از 200 تحلیلگر اطلاعاتی و نظامی در داخل مراکز فرماندهی در عربستان سعودی برای کمک به شناسایی اهداف در یمن کار می کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/151025" target="_blank">📅 09:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151024">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awQhULaDlTKmdPrL9daoRMB4yddF70Wyto-iokJTfx9Eze8PXNRIvh8y6PTgwWiCtlobkgG9-KvvaW6p_bjxMTQrBDPueDiDJTiiAgzU8ARn0s8bhg44iKPV0WLaBbGbtdWq1G4H_M98f60fTc-7ZSHjpZFQQrWykoi88ekvcvcVVfUqfEy1NKp7US5WiSvZGkcUM-G1yEuu-OpTUwuHxqKpkv-2v1SzOzKlGhGmxq_dsSC7NKer0dpZrkzft41X_nK7rGcHert4_BJJf-wJLlf2iiC1DsxOD_LeUQVApepTMGJZu6JFlnzvJJIVyb6tBvTb5NZoJTC7xCpRpQBR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای بریتانیایی تانکربندر (تامین‌کننده سوخت هوایی) امروز صبح در حال پرواز است و به سمت جنوب حرکت می‌کند تا از حملات عربستان سعودی به یمن پشتیبانی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/151024" target="_blank">📅 09:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151023">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد سامانه‌های پدافند هوایی 199 پهپاد اوکراینی را در طول شبانه‌روز بر فراز مناطق روسیه منهدم کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/151023" target="_blank">📅 09:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151022">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر اقتصاد: تورم کاهش پیدا خواهد کرد و وضعیت تولید و ارز خوب خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/151022" target="_blank">📅 09:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151021">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjIbaYPpwlDbviE-Z3BwrYm43H-qNK3FDKDk5HK5I0yTN0nVzNC6zVMF63UpwzhKYiVAk-mUWImtcIaLS3K5fQc-B3QrZEv3Kt-xLbcd2UAS-pfAjgr5RXsnqUTGimc8HE4-_dfn278WBQJS-eaXQTm80s-cJyfL_hv9HaxzaPgLjHbDTzkuBA6qikzjaSplBgWnPfV53YhA6P7MT_VfJo7EBDuxJUoYd435V0tLCAqH2sTYkxvKliOQXj8GERIkKtgZpG-iDXDYsNlDz4-jSdDg6PGhbRREYP0KiR4uWwxlu5qkK6rgltGTnv-ynDyq5BQmfJNduizynN7LheqsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال در فرودگاه بین المللی کویت همزمان با آتش سوزی در مخازن سوخت در شمال غرب کویت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/151021" target="_blank">📅 09:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151020">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5x8KQ6TTddzCPRlds2AYwyaF04SoWEwru8VoCQwvLeNGwXI6gTznUmW42omQ2zK15qyc2BKHrh87__JyHTSuczP738XTCJLfOL-7K1dmTQaQ3nf2pItvzSqmDChxrJbsw65byonm-BOG_J2HnGvcWRNEi6Rtthl5CmC6S0uwxrVby3T9dnNyDCsKz2PYRqACTxGEgO0RXzD5LlyWtyQ3tL2M7CANfWMnMG68pMhwgp2Tc7T6kKGVBvPCK9WzwRlAwPRCYpy9bbKp_JcKc5Xx220Re2FR7Mg53LloVMwoolYKRdzWkdMArz6PN9mu5nw5YcX4d8pD3FxdLtFbEUwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو فرانسه بخاطر اعتراضات دانش‌آموزی اینترنت رو قطع کردند، نت ملی هم ندارند، حالا سیستم بانکی هم قطع شده و مردم نمی‌تونند با کارت خرید کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/151020" target="_blank">📅 09:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151019">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیرکشاورزی: گرونی؟ نه؛ کالاهای اساسی نسبت به ماه پیش ارزون تر هم شدن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/151019" target="_blank">📅 09:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151018">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EacESCF2vAJ4rulJpVv94vYDPNhUJFb_gSlbiE9xBYe4GCm6fhC3MJpLfRZjSLeSv4Ez3sJLURyOic1iQdaHQw6cUwHzQ1SvJQeMDb_WwE-dyMDX4q3fHVXQNQn1xsvT3WBqiTWQ3hEFsMSIzczzKSFWSVtX5j4IxRgNJ91h6FXpJ2v4Z-ORcd1LFxulGrm5uJaaC1VGxeWoUEt9NVgLdVVZaDt__pQFJLC1xogWWFHjibsLRRBBs2MdbLNgZNi2yxwUEfck0DE6FOYdq09tHzHU121idyltW6X2-Z7MBfk1m6KPEZ4aXvO-fqzxuBo2jUzocJZNOROAb8zpLCFiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از آبان باران‌های شدید شروع میشود و قرار است هفته‌ها ادامه داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/151018" target="_blank">📅 08:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151017">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سی‌بی‌اس: بر اساس تحقیقات اولیه اسرائیل کمک‌خلبان هواپیمای فلای‌دبی احتمالاً به‌تنهایی اقدام کرده
🔴
الحمامی پیش از این برای مدتی در شرکت هواپیمایی عمان کار کرده که بازدید او از وب‌سایت‌های افراط‌گرایانه سبب انتقالش می شود
🔴
او همچنین در مقطعی ویدیویی از هواپیماهای شرکت هواپیمایی اسرائیلی در دبی منتشر کرده بود که در پایان آن، تصویری از ایمن الظواهری، رهبر شناخته‌شده القاعده نمایش داده می‌شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/151017" target="_blank">📅 08:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151016">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وال استریت ژورنال: توانایی ایران در هدف‌گیری کشتی‌ها در تنگه هرمز و اطراف آن افزایش یافته و خطر عبور از این تنگه را بالا برده است. یک مقام آمریکایی اعلام کرد دولت آمریکا پس از شلیک موشک‌های ایران به پایگاه‌های آمریکایی در اردن، از تهدید خود برای حمله به تاسیسات نفتی ایران عقب‌نشینی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/151016" target="_blank">📅 08:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151015">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6423daeae7.mp4?token=Bakyn6SKFlDUs3Axf44k7CJlT_95PX1nudazfec9frUxI9QWFaBnHpLrIkA1ihlHBUN7w-H0ZwtWmFrjpMtgUFWmbUI3_-OElcWoLhfYQ1T20FrK0_Ez8duEE45HyHzuyof-g2bkooQw3I8l2CfqTc0ZYZoGk1HE6NHtacqoNmrTdgU1DF2Thf42Yd02eQ-C3D6n9QZ4Zwj3hEaIw-2LjZS0DaZz4ddQ8N5G7_lrR5EIEky59_PObkztavGwayKFqAy3qErQgJLvOhyk8QsXHBFep3u8pySsBBgcMeRma2SUMbY9WmgZ2dzJtBv3pNjd06OVsk9qRfJRgdokK3BMaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6423daeae7.mp4?token=Bakyn6SKFlDUs3Axf44k7CJlT_95PX1nudazfec9frUxI9QWFaBnHpLrIkA1ihlHBUN7w-H0ZwtWmFrjpMtgUFWmbUI3_-OElcWoLhfYQ1T20FrK0_Ez8duEE45HyHzuyof-g2bkooQw3I8l2CfqTc0ZYZoGk1HE6NHtacqoNmrTdgU1DF2Thf42Yd02eQ-C3D6n9QZ4Zwj3hEaIw-2LjZS0DaZz4ddQ8N5G7_lrR5EIEky59_PObkztavGwayKFqAy3qErQgJLvOhyk8QsXHBFep3u8pySsBBgcMeRma2SUMbY9WmgZ2dzJtBv3pNjd06OVsk9qRfJRgdokK3BMaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین اعتراف سارق منزل سفیر فیلیپین: با حقوق ۱۲۰ میلیونی سرایدار خانه سفیر بودم
🔴
ساعتی که از منزل سفیر دزدیدم ۵ میلیارد قیمت داشت
🔴
در کمتر از یک شبانه روز دستگیر شدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/151015" target="_blank">📅 08:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151014">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر آموزش و پرورش:
حتی مدرسه یک نفره هم باید نماز جماعت داشته باشه؛ مهم‌ترین اولویت ما تو حوزه تربیتی توسعه فرهنگ اقامه نمازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/151014" target="_blank">📅 07:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151013">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
بر اساس تصاویر منتشرشده در شبکه‌های اجتماعی، کمبود گاز مایع در خاش واقع در سیستان و بلوچستان بار دیگر موجب تشکیل صف‌های طولانی مردم برای دریافت کپسول‌های گاز شده است. این وضعیت تامین یکی از نیازهای پایه و اساسی خانوارها در این منطقه را با چالش مواجه کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/151013" target="_blank">📅 07:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151012">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🟡
طلای ۱۸ عیار: 26,327,800  تومان
🔻
حباب طلا ۱۸ عیار: -1.89% ______________________
🟡
طلای دست دوم: 25,976,804  تومان
🟡
تتر: 268,950  تومان
🟡
یورو: 302,960  تومان
🟡
هر گرم نقره: 549,720  تومان
🟡
سکه امامی: 271,075,000  تومان
🟡
نیم سکه: 142,610,000  تومان
🟡
ربع سکه:…</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/151012" target="_blank">📅 01:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151011">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4pFsOi0-ffEENJJtsf9ZwvACeNbtHgE3fu0ceyNMCZ6JQSUNDJcuinalyJU-b_cuHq8dniPI68sB7YWis_oKal0VLQkPEFJIkFCoCAFHVVpex7WxNEHPAyCYc_2tG60UtiGfCRsecS9GZ6BI1aV9F4redpDvavm2QrlwYoLs-7WROyXbxlE1l1ItDOXoiz6w5EwgsEDm9kBshC6k6VTBTSkpiiROeUssV6OyURTYmT9zGxoBnA3wi_6oyni9moqegai7XZtUuemT0lcbkt-D-qz8JqBi8-17S-CCtVmBPHfCRSzZkTJjKKZoDSyT8nJPbvObroyB8BMu9A3O0XjOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بارون‌های انفجاری از آبان میاد
🔴
هواشناسی میگه بارون‌های این چند روز در مقایسه با چیزی که تو آبان میاد هیچی نیست. قراره از آبان بارون‌های انفجاری شروع بشه و هفته‌ها ادامه داشته باشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/151011" target="_blank">📅 01:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151010">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=a2YLqE0jVEQVpi5y8-esk9KgByqISHmJAOobxS2Cu1M8mv0jfqyXyowvbEIJt7GiB4KhLONPwwv1p8hPendjMa9i1iNaMqn_l2R3LiNZEm20aYu9sdf0yfMms3f-5TG9snDo7RF6Joo_jVqpCQDM5DOLXIPtSihzfg3WRKn7Te3R6jprxrA-mIqP5iwriv_ljkZHEOJZOu0CqJxsIfX53BETtqjIbWNZdsfa1eW0p1Nlokk01p3IQou4asPexbNMdYaVxcqXWfgP04e8PkLQCrAiMyFT69DlpuX8c2cu_dWJFqJW6pCUTRgIE06mi-tiimFRfkTDyiGEzpIN3Ga9Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=a2YLqE0jVEQVpi5y8-esk9KgByqISHmJAOobxS2Cu1M8mv0jfqyXyowvbEIJt7GiB4KhLONPwwv1p8hPendjMa9i1iNaMqn_l2R3LiNZEm20aYu9sdf0yfMms3f-5TG9snDo7RF6Joo_jVqpCQDM5DOLXIPtSihzfg3WRKn7Te3R6jprxrA-mIqP5iwriv_ljkZHEOJZOu0CqJxsIfX53BETtqjIbWNZdsfa1eW0p1Nlokk01p3IQou4asPexbNMdYaVxcqXWfgP04e8PkLQCrAiMyFT69DlpuX8c2cu_dWJFqJW6pCUTRgIE06mi-tiimFRfkTDyiGEzpIN3Ga9Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی: جنگی که توی راهه، آخرین جنگ ترامپ با جمهوری اسلامی خواهد بود!
🔴
اما به قدری این جنگ شدید و گسترده‌اس، که جنگ ۱۲ و ۴۰ روزه، پیشش یه شوخیه!
🔴
شدت بمبارون‌ها خیلی شدیدتر خواهد بود، کشورای بیشتری درگیر میشن و این نبرد آخره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/151010" target="_blank">📅 01:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151008">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSH8aGogPjkLQ5u93XthGHOm8g38RhS8Wl2j9UIKr5lmxlXX-FAcDougainAPGzdMBbQcV9KSiAZ_9M6V6xiu_KOVc2bW2S3xXgdApGDbW0CPJFdyxn1UUB2J4JMuVQoRcF4fBUiI-vMwCpYrTgjIOoYy-j_GRnTYr7eFQlgoZFhW8-q94coFoeHFluUDdk2iUT7MePAOGFA8s7JxsirsVpi53GKmg9DtQKAkJzzSYvW1YFWFxMcRbtquHBU8cw8MZevaLxpZQCsZrCT3ppNbT1FE8_ohNbyNHA8Q_Uw6jwyF3moJKWcUge8gxVn2uA8qdjf0nTR_1V02q31udK54A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار نزدیک به دولت ترامپ : پنتاگون در حال آماده‌سازی گزینه‌هایی برای حمله هسته‌ای به ایران است.
🔴
این را به خاطر بسپارید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/151008" target="_blank">📅 01:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151007">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0a3ccc7c.mp4?token=PozBk0YXnjGHz3t1dhp-rfRyCKR2AiGd-JlN0NeQ3VmoIyUkesFr1pHtWEvtitiGmX-iw5eXT5f2JkwWKEkJ411DLrhXgVVqZ40Id28afiyUgbfT0CdyDI_cWwhnFsWZrTVTwaHoA6ZGDxZMUmDX9remCZNH1qf0ecglw_moybg5kCvB4diAl4qruUZb_F5XlbWtyZYxy7iPAhZM0zdisy5980xaSRv4LoIj42sd2s94gzhyMpD80NOaGTne_Tlni5a2skjN7zYgXBMYj3aIg_-HNuPD8agph4yMXvdqSVFTKaPnBvJzRDqGHnekmqkNUHFB9VXN9kpOUCaWc1_o8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0a3ccc7c.mp4?token=PozBk0YXnjGHz3t1dhp-rfRyCKR2AiGd-JlN0NeQ3VmoIyUkesFr1pHtWEvtitiGmX-iw5eXT5f2JkwWKEkJ411DLrhXgVVqZ40Id28afiyUgbfT0CdyDI_cWwhnFsWZrTVTwaHoA6ZGDxZMUmDX9remCZNH1qf0ecglw_moybg5kCvB4diAl4qruUZb_F5XlbWtyZYxy7iPAhZM0zdisy5980xaSRv4LoIj42sd2s94gzhyMpD80NOaGTne_Tlni5a2skjN7zYgXBMYj3aIg_-HNuPD8agph4yMXvdqSVFTKaPnBvJzRDqGHnekmqkNUHFB9VXN9kpOUCaWc1_o8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: به کسانی که برای پرداخت هزینه بنزین، غذا و سوخت دیزل به سختی می‌افتند، چه می‌گویید؟
🔴
پرزیدنت ترامپ:
شما بازنده‌ها هستید. این بهترین اتفاقی است که می‌توانست بیفتد. اگر در این اقتصاد به مشکل برخورده‌اید، یعنی بازنده هستید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/151007" target="_blank">📅 00:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151006">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgQvW9rxXZizzXdnhEm2qD8L94Cpoe8AJI71sBD6WBEVEek86rg1ocxeaECvXPXvL-gE5U9LzjWxgdxj_BhjgHV1YLaNIXHYUDFgg-3QUDHcCSiC7PYc1hGOhqjuijSRHPLsYAC3RGu8FwGgkUg8jonbjntNiTUUDZqu-LN4j9ddNG06O8oF5XXYCOQpU3siXQx027_UsOp7lveesZb3mT2RjP_dRk8Dmg4_vavt-AZxwBASzXLEjkJ02VybpbIRlBDUDT5IaODERMsJPbWwACsfmnY8E1J_BV7WaiEKdrZDFhTD5FT5CL2CD2xTAkmNOiNywDg8OMgdwdgujNhUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این عکس رو ببینید!
🔴
در نگاه اول یک تندرو و سوپر انقلابی است اما درواقع وی مهدی نادری جهرمی، جاسوس ارشد موساد تو ایران بود!
🔴
این شخص فارغ التحصیل دانشگاه امام صادق و موسس اپ ۷۸۰ بوده!
🔴
خلاصه پایداریا و تندروها و این قماش کصخولا اکثرا فیلم بازی میکنن و درونشون یه چیز دیگس
🔴
این شخص الان تو سواحل تلاویو داره آب پرتغال میخوره و به ریش یه سریا میخنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/alonews/151006" target="_blank">📅 00:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151005">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f64fad2c13.mp4?token=AaqH7VtbJ7eaiyMku9ENRydDxbg0r13-6TxqAlFATUuj7ubCGA6znU9uT5uMv9qB3Hi2ZUel8-LrFmxJjHYGNba1ChUdgoPHioWjWHngm4nb6cKWhFJrrc2fBHAKHd3_rYNAT-aFRwxLyy-ZaDQLep0TMgGOUBd_Xh5zgGi79su00QlQLoK38lwrDrnjunTgooOv62pXl-UPR_i68ir-Smxy-UzaSngASUMzl7Fizux2G2UPUjffjhl5ekG6MX4_el69WhKyR91Hk8Yr__gvct4AlgTtSGEqVx2X_UgOSVtIjK-Ux7bTrgwVOhDAWdVViPxhMLG4Cn2zF4KQdgSa3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f64fad2c13.mp4?token=AaqH7VtbJ7eaiyMku9ENRydDxbg0r13-6TxqAlFATUuj7ubCGA6znU9uT5uMv9qB3Hi2ZUel8-LrFmxJjHYGNba1ChUdgoPHioWjWHngm4nb6cKWhFJrrc2fBHAKHd3_rYNAT-aFRwxLyy-ZaDQLep0TMgGOUBd_Xh5zgGi79su00QlQLoK38lwrDrnjunTgooOv62pXl-UPR_i68ir-Smxy-UzaSngASUMzl7Fizux2G2UPUjffjhl5ekG6MX4_el69WhKyR91Hk8Yr__gvct4AlgTtSGEqVx2X_UgOSVtIjK-Ux7bTrgwVOhDAWdVViPxhMLG4Cn2zF4KQdgSa3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
با همین افکار تخمی، لاکار رفتید
🔴
سردار فدوی: قیمت گازوئیل تو اروپا 2 یورو شده که یعنی 700هزار تومن
!
ما اینجا 10 هزار تومن پول بنزین میدیم که حتی یک دلار هم نمیشه و اصلا متوجه نمیشیم گازوئیل لیتری 2 یورویی یعنی چی
حتی با اینکه قیمت ما سه نرخی هست بازم کمتره به یه دلار هم نمیرسه
این شرایط قیمت ها بخاطر ابهت نیرو های نظامی جمهوری اسلامیه که بوجود اومده
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/alonews/151005" target="_blank">📅 00:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151004">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
آکسیوس: آمریکا باز هم درخواست عربستان برای شرکت در عملیات علیه یمن را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/151004" target="_blank">📅 00:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151003">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سردار فدوی: ایران و عمان بر تنگه هرمز حاکم هستند و قوانین تنگه هرمز را ما می نویسیم و در حال اجرا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/151003" target="_blank">📅 23:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151002">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وال استریت ژورنال: آمریکا تمامی بمب‌افکن‌های B-۱ خود را از پایگاه هوایی RAF Fairford در بریتانیا خارج کرده است؛ مقام‌های آمریکایی روز یکشنبه گفتند این تصمیم در پی نگرانی‌های امنیتی درباره طرح‌های احتمالی علیه این تأسیسات اتخاذ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/151002" target="_blank">📅 23:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151001">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
سنتکام گفته ایران باید تسلیم بشه یا جنگ سختی هم اقتصادی هم نظامی راه میندازیم!!
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/151001" target="_blank">📅 23:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151000">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سردار فدوی: در صورت حمله زمینی آمریکا ما هر نقطه‌ای که مربوط به آمریکایی‌هاست، پایگاه‌های آمریکایی‌ها، هر شناوری که مربوط به آمریکایی‌هاست را هدف قرار خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/alonews/151000" target="_blank">📅 23:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150999">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df3435529.mp4?token=ESHTdN1ITiYq6-198hz3ewU6YpCpU4ym1kLgMyKgD30pESmA9Jw01Co8_2MtKORJIxAV1MmzHoxLOJfPXIQIzEhDVufw4kkyudifapiaommH3pG0V1dN7Kw9ZHMYeJS7qi9uBiCxn0SVVGQ8Qeh3hUUnHpEbh4WRyZpY6fNttS_o9BL2QfJiwjIweu09M-rskR_EJbFnKk7ky_T2GdwI7AbHWSzRpk7S2cUEudalVNHt4ds0V8lzQWYOcYPmZvjqAilxvylm2rS6EIr6EJ1mpVa1A6GPk3PmOIb3I0UJXxhIOHDi32XeII-nudGJ8PzesKckU8IISbtDi-zPvjoFEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df3435529.mp4?token=ESHTdN1ITiYq6-198hz3ewU6YpCpU4ym1kLgMyKgD30pESmA9Jw01Co8_2MtKORJIxAV1MmzHoxLOJfPXIQIzEhDVufw4kkyudifapiaommH3pG0V1dN7Kw9ZHMYeJS7qi9uBiCxn0SVVGQ8Qeh3hUUnHpEbh4WRyZpY6fNttS_o9BL2QfJiwjIweu09M-rskR_EJbFnKk7ky_T2GdwI7AbHWSzRpk7S2cUEudalVNHt4ds0V8lzQWYOcYPmZvjqAilxvylm2rS6EIr6EJ1mpVa1A6GPk3PmOIb3I0UJXxhIOHDi32XeII-nudGJ8PzesKckU8IISbtDi-zPvjoFEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین یکتا در صداوسیما: ما یه جنتی داریم عمرش از خود اسرائیل بیشتره
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/150999" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150998">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
آمیت سگال، خبرنگار مشهور اسرائیلی: این هفته، خطرناک‌ترین هفته ۲۰۲۶ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/150998" target="_blank">📅 23:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150997">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUu6wTdWz6_B1V3cQKcl704cwo3Ri7YXQacFVR_dCYcMuGf87-zlqeguajjxyJnBG2XYIf3-Ebtk4sIhSdn3rm3U7jAvRKXgSz7wjVJtTKhJnyCOx1gSVE_pnd7pShDnTGEC-irSVIsVnfx6GxJkV_lKMU6sXdRdqJBziUI6smjlmeSeaT0jrB5MzJDJ-7hXKojMWKq_pfDSngspE3UfHPI7M7yCYgWTbbvhluYK6LCGUeFI2IH573aUsfYzrdhpxmbQ5hKb5TDnZLRCt2Mav94AiT92eLwYQF4fHt_tunEsGnlzpik_Vrxu8dBD3EaDGbJPahUkLpPzBOlf8n3e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
کوچک زاده: منم بکنید تو زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/150997" target="_blank">📅 23:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150996">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
گزارش از گشت جنگنده های ارتش در برفراز تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/150996" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150995">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpM8b1a-vNb4Wl31OjFNl6x7er_iLJkhtoYRIYfws7CFo4aHy1HIjGsRJulvRYp1LiFeEJQdIRpCQelKh5m3_18SBPDIdzlP25CFcc86lG-pGBuTuh413DLdTCF9I2YAc2i8WmSXtCu9nIncST21GhDKLVVYAfGggJ_kUYeOlmUEdFxqajUnFo4RuquJiGMazXEhlNRjvBTyKeMXu8bw420jbTQrS3UBp6NGLZsIDyUloQUaIYfj7hPuIV_iTX8GLrPjqMJ2j40Y5G2wK0ezawQB7mojioZfIWeujDMDGIL7trLUAVlqycQ9zbNH1TWvOLjP-c0dhtCHhKtXl22lZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات سنگین به مواضع حماس در نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/150995" target="_blank">📅 23:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150994">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزیر اقتصاد: مردم صبوری کنن، مشکل تورم بزودی حل میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/150994" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150993">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/674d1e998f.mp4?token=kkJTlj5EbkDkgqiYd6AcYO7FDfLWHkA2bJMQKSVCxb-E7YmrTrzv1xMxeDqjJKeMJLTcaMUkeMiQIgzH2BlHB5_-qTH2Ie4ztMrsQmWrvY2ZNrRCdsQNgsVMpoVRdhSzxT85MEcfd6P14jS09V_Pk4lD6bVWXBTbqHtdUYJD08oSF1DB4Nke4RINeZvjncsKWKX-PrQAlR7FY2PjgoPx5CJsWa6qZaW80qfu6njsZBcYqSrcpzjOIC0_OA3M2OY6UZHqtsYjd4oyT-1WKeo_YY5LMbZ3u7C6nYKm29XLqQ0NCnhoA-hKjMeMJxaWg7_26-KLCbmNuhbZ3vx-1gWNZB4tnvERw7dqZZ8_vJTPg6cZics9rdpsVf54etGeXOWDoDVhfrnTjGEqxsz3tFsU02ko8u_WFco5cFCGMJQsfQBJN74WwsKHGjQw4E4L-rbFAybvbah5wlmlk8tqlfCF9b4UW6mXXKI8OvX7M18V2TtP1poQTnR1maau3V5CkmtA55eGFAtkOK8zyto0BqL1xvDLt5lHXzjnLT73pXTynDlW8uvIZ0GWTUWhPSk9hO-nrlbtPua2hPGbUJq1lymn8z8mFDq6snsV1ur3ZQ1AoyTBXrQ41HuXhLoz32WIpYWm_6TuKmS5pvbx718NZ61ZWV8OerxkRncXo5p_bXqXsdY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/674d1e998f.mp4?token=kkJTlj5EbkDkgqiYd6AcYO7FDfLWHkA2bJMQKSVCxb-E7YmrTrzv1xMxeDqjJKeMJLTcaMUkeMiQIgzH2BlHB5_-qTH2Ie4ztMrsQmWrvY2ZNrRCdsQNgsVMpoVRdhSzxT85MEcfd6P14jS09V_Pk4lD6bVWXBTbqHtdUYJD08oSF1DB4Nke4RINeZvjncsKWKX-PrQAlR7FY2PjgoPx5CJsWa6qZaW80qfu6njsZBcYqSrcpzjOIC0_OA3M2OY6UZHqtsYjd4oyT-1WKeo_YY5LMbZ3u7C6nYKm29XLqQ0NCnhoA-hKjMeMJxaWg7_26-KLCbmNuhbZ3vx-1gWNZB4tnvERw7dqZZ8_vJTPg6cZics9rdpsVf54etGeXOWDoDVhfrnTjGEqxsz3tFsU02ko8u_WFco5cFCGMJQsfQBJN74WwsKHGjQw4E4L-rbFAybvbah5wlmlk8tqlfCF9b4UW6mXXKI8OvX7M18V2TtP1poQTnR1maau3V5CkmtA55eGFAtkOK8zyto0BqL1xvDLt5lHXzjnLT73pXTynDlW8uvIZ0GWTUWhPSk9hO-nrlbtPua2hPGbUJq1lymn8z8mFDq6snsV1ur3ZQ1AoyTBXrQ41HuXhLoz32WIpYWm_6TuKmS5pvbx718NZ61ZWV8OerxkRncXo5p_bXqXsdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه نجات یک خانم گرفتار در سیل ایذه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/150993" target="_blank">📅 23:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150992">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
شبکه 12 اسرائیل: خلبان عمانی اعتراف کرده میخواسته هواپیمای فلای دوبی رو ترمینال فرودگاه تلاویو بکوبه تا تعداد تلفات بیشتر بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/150992" target="_blank">📅 22:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150991">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDSkQAxbhTx0JcayHGcEFkbyvUdStIMOiHU4NCeeIreZigzTzdho5aiTDLMsAK9VApEVT2aKNjO8_BAgTYavnAQwnRDFgPFh3_vO7Rm-3jn6I5o-Im5Zu0CiKNzF8NuybyjXmUImgf16CSoQSGwcv8Fu6cWtPiPfty2cX-nGuKmbekBv30I67233J4FyaZl8efTvY4x-I6NF3yeasu1XagUbXVO8VdeLjtt8u8F43tEi3jxfp-bvBT8qYkA23vzfXOrUtSHTiQLG5IzyBkS9TPp_-HkBtcXYqnN_6Uc93N4gm_kRQUd0DOw-eiFJEOJjdeBcKSI89x0oEdsu9RU4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله به یک نفتکش در سواحل یمن
🔴
سازمان عملیات تجارت دریایی انگلیس خبر داد، گزارشی از یک حادثه در ۶۰ مایلی دریایی جنوب المخا در یمن دریافت کرده است.
🔴
به گفته این سازمان، یک نفت‌کش از وقوع چند انفجار در نزدیکی خود در جنوب المخا در یمن خبر داد، ولی خدمه در سلامت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/150991" target="_blank">📅 22:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150990">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzuVoHP6ex5v59A82x1nvOkv9Bi2dwOPuYGVqT4inV08SZH3hk2-8Cm4BpksgaKjZmeQ5bsX9F5WBwh8b7OJSKzk0673hlyfgMal8a1rngd8nREP83j99I97GFHy8A9gpHxOqw5oA5tAsQhX0n5vmeOk2j9O1XT4nJYAT_dX133jBoEXN3Lt47B7ZckajqJA1pkdPgOqd4rcPuwEGYJYwuTtEKrZ0eZomvAK_mHOHCgGVKSnfsU7FjtA7hP3WR4d6mNW12Jmgt6liM-fvx2R48eMt47-axqv3hD51809jsQpagBDp5tpNHmFM3V8yhlmX1VC9dQZ76xqQNtj3Hy5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ با انتشاری عکسی از خود در کنار رئیس‌جمهور چین نوشت:
ترامپ جوان‌تر به نظر می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/150990" target="_blank">📅 22:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150989">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: به نظر می‌رسد که همه طرف‌ها در حالت آماده‌باش کامل هستند و منتظر هرگونه تحول نظامی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/150989" target="_blank">📅 22:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150988">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🟡
طلای ۱۸ عیار: 26,327,800  تومان
🔻
حباب طلا ۱۸ عیار: -1.89% ______________________
🟡
طلای دست دوم: 25,976,804  تومان
🟡
تتر: 268,950  تومان
🟡
یورو: 302,960  تومان
🟡
هر گرم نقره: 549,720  تومان
🟡
سکه امامی: 271,075,000  تومان
🟡
نیم سکه: 142,610,000  تومان
🟡
ربع سکه:…</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/150988" target="_blank">📅 22:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150987">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
قتل همکلاسی بعد از زنگ آخر مدرسه
🔴
اختلاف دو نوجوان همکلاسی در سال ۱۴۰۲ پس از تعطیلی مدرسه به درگیری خونین با چاقو در پارکی نزدیک مدرسه منجر شد. آرین، نوجوان ۱۵ ساله، مدعی است سیاوش او را به بهانه پیدا کردن یک ویپ گمشده به پارک کشاند و از پشت با چاقو به او حمله کرد.
🔴
آرین می‌گوید: در این حادثه از ناحیه
است دچار آسیب عصبی و محدودیت حرکتی شده است. او همچنین گفته برای دفاع از خود یک ضربه به همکلاسی‌اش وارد کرده و بابت آن به پرداخت دیه محکوم شده است.
🔴
سیاوش در دادگاه وارد کردن ضربات چاقو را پذیرفت، اما اتهام شروع به قتل را رد کرد و گفت قصد کشتن همکلاسی‌اش را نداشته و تنها می‌خواسته از او «زهرچشم» بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/150987" target="_blank">📅 22:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150986">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد چهار نفت‌کش طی ۴۸ ساعت گذشته هدف حمله ایران قرار گرفته‌اند.
🔴
خدمه یکی از نفت‌کش‌ها که ۲ اکتبر هدف حمله قرار گرفت، ناچار به ترک کشتی شدند.
🔴
نفت‌کش دیگری که ۳ اکتبر مورد حمله قرار گرفت، برای مدتی کوتاه دچار رانش شد و سپس با کمک یدک‌کش به سمت فجیره در امارات حرکت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/150986" target="_blank">📅 21:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150985">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
خروج بمب‌افکن‌های راهبردی آمریکا از پایگاه فیرفورد انگلیس
🔴
۱۰ فروند از ۱۲ بمب‌افکن استراتژیک B-1B Lancer نیروی هوایی آمریکا که در پایگاه فیرفورد در انگلستان مستقر بودند، در حال خروج از این پایگاه و بازگشت به خاک آمریکا هستند.
🔴
انتظار می‌رود ۲ فروند باقی‌مانده نیز امروز خارج شوند، به این معنا که هیچ بمب‌افکن استراتژیکی در پایگاه فیرفورد حضور نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/150985" target="_blank">📅 21:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150984">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این پسره پشت پرده دلار رو لو داد
😐
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/150984" target="_blank">📅 21:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150983">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1433d0f2d8.mp4?token=Y-0-t-_Rao5xHrQMsYETwTxwrBzSwSVsShrUBfRwK4muwOIO9q_UdHG-HXGXXEQbpsb9RxkJH9zrM3DYGjUEo4mbUH_jrvngq4JcL71atkkdQ-r7xHOBAWCQHNNFpFdVU7J7dL5svjOVEzG2f9af4_dah0u4L-n4NxW0qRgizVxQ7QWuF69gnAJPA0q9QtyIhO2LGZu8eNLPUYIl0rvRs8OkOMymYThx_mwZuBqyULOHF5SanjJeu0rSiXUYQxnM4aGPlYffhFZWl5VmKJgGGmxzWKn8pi2kspHS04TgBtiDC0nsuQhQYXmVG2CQftnrXzyAzGZvogY6pE26Oe8cMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1433d0f2d8.mp4?token=Y-0-t-_Rao5xHrQMsYETwTxwrBzSwSVsShrUBfRwK4muwOIO9q_UdHG-HXGXXEQbpsb9RxkJH9zrM3DYGjUEo4mbUH_jrvngq4JcL71atkkdQ-r7xHOBAWCQHNNFpFdVU7J7dL5svjOVEzG2f9af4_dah0u4L-n4NxW0qRgizVxQ7QWuF69gnAJPA0q9QtyIhO2LGZu8eNLPUYIl0rvRs8OkOMymYThx_mwZuBqyULOHF5SanjJeu0rSiXUYQxnM4aGPlYffhFZWl5VmKJgGGmxzWKn8pi2kspHS04TgBtiDC0nsuQhQYXmVG2CQftnrXzyAzGZvogY6pE26Oe8cMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرتس، صدراعظم آلمان: اقتصاد روسیه نمی‌تواند این جنگ را به طور نامحدود ادامه دهد. ما می‌دانیم که اقتصاد روسیه از قبل به نقطه‌ی بحرانی خود رسیده است: تورم ۷ درصدی، نرخ بهره بانک مرکزی ۱۴ درصدی، کاهش درآمد حاصل از نفت و گاز، و کسری بودجه‌ی دولتی که به طور فزاینده‌ای در حال افزایش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/150983" target="_blank">📅 21:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150982">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy6b2X9PNopsbfxPquSzTqtaAT8g9zKpl7OqHRP0Z_VJiY6bYfZoer5bRjV1kUiINkzGKljmc1B3eab7Ow2D1XJGL174JbsrM2jYh551Tx5LhzICLRpdhJkyDhQZ6wjo2SCBmgyrY63Srsw45Iyu6xi-MJpcyNcl7fPxYhBm9IAZ0OkDZYkRhV-ztuxovwXX7KbHgQqrZjdG3Qs1ZlwTsDcZcwPWXA3AugGrkDOsKCjQF1kV68WZPVs8HBGr_vovqAXNnF4157YZL4s3q_EiOgw-McZj2KzKLX86OgFIZGX9XIv4ebBlYrdJaKtdO3sjcaD5A9m3WZ9ZS-L_cCN1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ تصویری از خود به همراه پنگوئن‌ها در گرینلند منتشر کرد.
🔴
پ.ن : پنگوئن‌ها در گرینلند زندگی نمی‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/150982" target="_blank">📅 21:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150981">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aaf4c3a90.mp4?token=vrz2vwfSoDR8rEs_GZl1au6hKQ5IdxZOARYAR0wxhPwR566kaQ8cnvz3bydJQQf0WMjRuLNysnSjLCBdtoQYSjGixKBCTm-o0iniG2vmpS1oma4_J5WKPuU4h_3WP7wZgcqAXsra6hxI1i9MW_VlmrCvKU53Y0vZ1DUHmTCWBkdfAwcO1s7d_XvYRqt1VwPZotzcUvP4i9XBtoE4dGLn5pPdM3QmS7LJ6HbPnlFg7-Y1D29g2FXDv9yged8q0L-NPrT19G8JNMuNtg9hnyFO9ii1hNO_zaRGSHbRTfjHGRCGxwZrYdcYGlQLTit8q6yx3P7HpwOcMN-l-A9gu67V3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aaf4c3a90.mp4?token=vrz2vwfSoDR8rEs_GZl1au6hKQ5IdxZOARYAR0wxhPwR566kaQ8cnvz3bydJQQf0WMjRuLNysnSjLCBdtoQYSjGixKBCTm-o0iniG2vmpS1oma4_J5WKPuU4h_3WP7wZgcqAXsra6hxI1i9MW_VlmrCvKU53Y0vZ1DUHmTCWBkdfAwcO1s7d_XvYRqt1VwPZotzcUvP4i9XBtoE4dGLn5pPdM3QmS7LJ6HbPnlFg7-Y1D29g2FXDv9yged8q0L-NPrT19G8JNMuNtg9hnyFO9ii1hNO_zaRGSHbRTfjHGRCGxwZrYdcYGlQLTit8q6yx3P7HpwOcMN-l-A9gu67V3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی ها داخل شهر تعز
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/150981" target="_blank">📅 21:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150980">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
اکسیوس به نقل از یک مقام آمریکایی:
سنتکام درباره آغاز حملات در یمن نگرانی‌های جدی داشت و این اقدام را عاملی برای منحرف شدن تمرکز آمریکا از ایران می‌دانست
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/150980" target="_blank">📅 21:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150979">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06a3608746.mp4?token=S5aVuRDC-LIavteuPngkiyBqmUndex93WfCLBGfVbOVlnZKPwpu5tsMPbukjdqptnZLkOnxXhEEQXvLe-RNelXZfvGoyOdqKY5qyynRGb-7sbrIPBcPdfY1SAIEvNCF-y6Kh2AF2XFvEWez9XQkCXk5yOdIa-2_J4wROa4E5utuP_-fvftckozoGnS2pMxi2wuQOBjtm5kg6GK5hs7jDh7piS7w01MqVba3kiNFSPoV1pw70DbXauvwGeI4HAPV4bVA5mn9b23EElAB7DmKet_ha49iS0SqVBsk5UKMjVmUQqhDsAp_jZ26PvcyODatICZBHiu0EXI0NUYkf_85l60BwDtT8Tk-ACvEiIqKJtiZY2WluGbRUHwaqiiHMr5NEJvJodf1lWzTsMLrFpLzEsprui0_8VhSPqCm5VxQjwLCiM_-BZ1oHtUduHLu1kg7mod78iIgjLh-9sTsFRMZwrh-GwZYl00WV5Wcd-NlNboASvJcPLkXPs7CAjOCE--7B9NNn3oobbrgwr4OJDER_9QXPt42cVlLfLUVQZ-q7fIVA1SvosAc1lhvgxHbHPM5WZiAGKqxdZR-CfDBGbf1lgLJ8ZoitnUdUR8DvtN0U9k_enrbixF_U6K1cupVsq8Cc-17ZOiUbtv7nNv8V64p4xJDGgP_6NfnfzI8jh23tDUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06a3608746.mp4?token=S5aVuRDC-LIavteuPngkiyBqmUndex93WfCLBGfVbOVlnZKPwpu5tsMPbukjdqptnZLkOnxXhEEQXvLe-RNelXZfvGoyOdqKY5qyynRGb-7sbrIPBcPdfY1SAIEvNCF-y6Kh2AF2XFvEWez9XQkCXk5yOdIa-2_J4wROa4E5utuP_-fvftckozoGnS2pMxi2wuQOBjtm5kg6GK5hs7jDh7piS7w01MqVba3kiNFSPoV1pw70DbXauvwGeI4HAPV4bVA5mn9b23EElAB7DmKet_ha49iS0SqVBsk5UKMjVmUQqhDsAp_jZ26PvcyODatICZBHiu0EXI0NUYkf_85l60BwDtT8Tk-ACvEiIqKJtiZY2WluGbRUHwaqiiHMr5NEJvJodf1lWzTsMLrFpLzEsprui0_8VhSPqCm5VxQjwLCiM_-BZ1oHtUduHLu1kg7mod78iIgjLh-9sTsFRMZwrh-GwZYl00WV5Wcd-NlNboASvJcPLkXPs7CAjOCE--7B9NNn3oobbrgwr4OJDER_9QXPt42cVlLfLUVQZ-q7fIVA1SvosAc1lhvgxHbHPM5WZiAGKqxdZR-CfDBGbf1lgLJ8ZoitnUdUR8DvtN0U9k_enrbixF_U6K1cupVsq8Cc-17ZOiUbtv7nNv8V64p4xJDGgP_6NfnfzI8jh23tDUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: در صورت حمله اتمی به تهران، سه‌میلیون نفر کشته خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/150979" target="_blank">📅 21:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150978">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
گزارش ها از انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/150978" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150977">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سناریوی هولناک در پرواز فلای‌دبی؛ نقشه برای کوبیدن هواپیما به تل‌آویو
🔴
رسانه‌های اسرائیلی گزارش داده‌اند کمک‌خلبان عمانی پرواز فلای‌دبی قصد داشته پس از از کار انداختن خلبان، مسیر عادی پرواز به تل‌آویو را ادامه دهد و در لحظات پایانی هواپیما را به یکی از ساختمان‌های شهر بکوبد؛ طرحی که به‌گونه‌ای برنامه‌ریزی شده بود تا جنگنده‌ها فرصت مداخله پیدا نکنند.
🔴
این کمک‌خلبان در میانه پرواز با تبر اضطراری به خلبان حمله کرد و هواپیما طی حدود ۳۰ ثانیه بیش از ۱۶ هزار پا سقوط کرد؛ اما مسافران وارد کابین شدند و او را مهار کردند. مقام‌های امارات این حادثه را «تلاش برای حمله تروریستی» توصیف کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/150977" target="_blank">📅 21:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150976">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
تسنیم: استان تعز یمن به کنترل انصارالله درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/150976" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150975">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPpfT_C2gj7h3HyqpeKKE81v4BG3KzQ3BirBjqOLCiS_xEJM9DAOkBCBEl-OMr_JPMyDe3KwUe-Fht95XfumMJCDroD6tFGYZbiBydxCo7jNRA7sujoHW0_a9yzkTOl1NJzVrqQA1f86oom7eHRWPg2lPzilw3cgSWcJ6gHfR_Nk0NpyEVNml4b4ZI3DucJzeOPrKxmd5TEfl9wgEmnbTNfVAeAe9Hdn_5w23qk4lMwcFDU8bMi80RsrZurok_a_xUqsrwH56yU2Ag9ThZnx8ipAgM84a7Grh8kewycI28wCXzyyMvg_TlMwJ4OeXcz_0CS6cccxEWkoP23rNfja1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازرگان، کارشناس تلوزیون: طبق محاسبات ما اگه آمریکا به تهران اتمی بزنه ۳میلیون نفر درجا بخار میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/150975" target="_blank">📅 20:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150974">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
آکسیوس به نقل از مقامات: با میانجی گری قطر گشایشی در مذاکرات ایجاد شده
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/150974" target="_blank">📅 20:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150973">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTAM23INIZ2QgJ06x_OeB0Lvx_51E0ikZXxCmoxZaGHBqBX724QLU3ZiF63c7QdG_5kkeN2PHHmjt6XVFkCM5u4I-iJ1uy5Xe_SNOS-T-AD0T6K1w5PJlFHdUDfD3PfTVT6MDNRYeAfqvF7VKbumezetUa8FVJZTH9_mf66TtpFf0qNJhENvGST9uX5EwEqYuSHP7M9ZxS4eR1yZzf89i_JDjE8bxnOzGQGY46g8XyfKxPhrcYfI6Nmj7T-aAPk9_aR44IznDLnXQ_6AqJv3UlPqfKcsF8eAw_1Fz4EjSlh_xGd_MgXYoB4X3lFVDJQpsPEPkO4gVjKnRfFWd4Qu4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۷ فروند هواپیمای تانکر آمریکایی در نزدیکی تنگه هرمز در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/150973" target="_blank">📅 20:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150972">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزیر نفت استعفا داد
🔴
بورد سرپرست وزارت نفت شد
🔴
«طباطبایی» معاون دفتر پزشکیان: با پذیرش استعفای محسن پاک نژاد طی حکمی از سوی دکتر پزشکیان رئیس جمهور، حمید بورد به عنوان سرپرست وزارت نفت منصوب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/150972" target="_blank">📅 20:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150971">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ایال زمیر: باید آماده یه جنگ غافلگیرکننده باشیم
🔴
رئیس ستاد ارتش اسرائیل می‌گه که باید خودمون رو به آمادگی کامل برسونیم چون ممکنه هر لحظه یه جنگ ناگهانی شروع بشه. این حرف‌ها در حالیه که تنش تو منطقه هر روز بیشتر می‌شه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/150971" target="_blank">📅 20:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150970">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XauByKVdNVQfYrLp4vSjNKva4GrUwvk7IMw1t2yjA59GgHIBveZMbZoQ6Alnh6NVjaTGcR9yrKtpvXphPj52JUI4uOWuRrXNt11phgW4l2b2JuRDq7zbOpk40kK22iFCJXdvDfnSs9CZQ4L_tbK2ccHIlnyAfzGu7irJPCzTMmFOqyri0ftkBoedP_Zyid-s01jrOrneXXHXmfKkUO4KvRosy9OUoGSvIO7gTjki5ebqfuWBp-RwuUV5QGj-9lw3zraBHVvzf7_60f39n1vdy1cuYZp3qOsO6V2ltHbtSft9QDCCKRGplWgMMPfdp4P-IvQiqO8k1YPgAmAMUTAwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاید باورتون نشه ولی نتانیاهو تو اسرائیل میانه رو حساب میشه و رقیب های انتخاباتی و قشر تندرو بهش میگن زیادی به فلسطین و ایران آسون میگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/150970" target="_blank">📅 20:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150969">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d8f4fd4a.mp4?token=Lxu9CX7bhPMINCTgXQVTY2NeeZEoGSqgRUI_uY50Ax1Jt2puxoFQ4VN9CjUipY84Y1dRQARqt9WqA6HQt34Q2rnxHSMF_kLP8bf10h9QNpQgvlxBjM1TyNuK5byeSv5noFqxayx9vlU8gAdMEaajJuC9svzh1CzKd3VUuXBxMB0_CWJmTfVjhfDHnbBF9joWMsD-Pz7jYWTQBlydq9W4sd2sRSLOgEhacwqWyHCHCkZFIkSZMH8nzQCaqqQD9OjewwCrl5jFUR4zdx1KN68ujIj3ncBhl4oVaWL8bkiIIX27UDsgC2DSvFb--TVQPyn9I0a4JBoXh-vfMwX2OGFKuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d8f4fd4a.mp4?token=Lxu9CX7bhPMINCTgXQVTY2NeeZEoGSqgRUI_uY50Ax1Jt2puxoFQ4VN9CjUipY84Y1dRQARqt9WqA6HQt34Q2rnxHSMF_kLP8bf10h9QNpQgvlxBjM1TyNuK5byeSv5noFqxayx9vlU8gAdMEaajJuC9svzh1CzKd3VUuXBxMB0_CWJmTfVjhfDHnbBF9joWMsD-Pz7jYWTQBlydq9W4sd2sRSLOgEhacwqWyHCHCkZFIkSZMH8nzQCaqqQD9OjewwCrl5jFUR4zdx1KN68ujIj3ncBhl4oVaWL8bkiIIX27UDsgC2DSvFb--TVQPyn9I0a4JBoXh-vfMwX2OGFKuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمار جدیدی از میزان تقاضای استارلینک در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/150969" target="_blank">📅 20:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150968">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbpJir4k2bKLLb_wQ6gi3bQXSVN89o1BGqwadFpH5uernY105w3CJZaf5XLuNx7czimfIU6VoUN2hGKtEoCKDK5M1FvzRGOxzFmOHqCTuorJuYerXq2Sk7hMFzRMeBXwmjUyGt7ehnMj0la56lcXOFl7HohGUxvAzwOcJojL7VGrkDVwuguH-Og4v_L8h0Q1mb9pmnTL1XE9_ZLe4A4ejGwhob3AJGPKFsRIP05icbPbvdxAGZP9shMiRpoCDjF0jHKODc2L_KvV42R4qR-jbugrxi-TFl_FW5zOaqNcB_8oTEak1yWZjNfo-LCAF5ElEUURefI3NuumxIDtdkSu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسپورت ایران در جایگاه ۹۷ رده بندی پاسپورت‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/150968" target="_blank">📅 20:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150967">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
پشت پرده ترسناک دلار
😳
‼️
خبری که بازار رو ترکونده
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/150967" target="_blank">📅 20:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150965">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7wmAdnYn2kMYaBEHMrAlkD6g1dZsIbp6HgLpAysqWfHXK4QeVHUnOumJLdOI_roRLDirDqvQ9ZRf-gb7GrC1ffYVlbh0BlrfzIBrT4te5m-TOKy99ajWf9aaYAMWYyb_9AxTrlEFZo4lfIQE2Dlr5SyCYA9IOU9tW47SB2-SzEgc9sZyEZW1FKRPalRhJFNaOg6vNutl0hQFLuR9cnj8YyGz47lvyrYeh_34JJarQWRBXOQNnenjEp1vBDFw_hGPq9AqEOmcqVmyOsjgZsOFZxG8t05tsIYsDYOMkN_TLnXeE3UIRMyJXQwSju0iO2k0pTOg09IMqfRQHL067JV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bo0e8wTaSxD2LmWAHwnqYX4IVL9SJz9e81Qx8F0NptSSBjQUBdfbRt3LbfUQhBjFoNA6_GGjomKOjCeOkabLn3mfWzFAzAvvEOtvaIG99m5y4E15JAvjYbYNvGlOGeZ-r5fEUQoOsaP_OhuMgcjQl7LcrSoowp5oSqOOleuk7Orqwm5LTvwaeMWo9jvl9Zzo-KlJHVD5heIroqZ2szqBSNkFAMZum8aNFOe_IX5du1pSSvnPF2LO_phsPQ3UZ6r2mhajAOhCEMAIaAiT4YlpxoTGIKxYUroiPwsdRa25z_p-qqnhFfO_bsGSNe87iX_vawv7LZcCSiPS7SDK1gxvzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نظر برخی دانشمندان فیزیک کوانتوم، تصمیماتی که الان میگیرید ممکنه روی گذشته شما تاثیر بزارند و اونو تغییر بدند.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/150965" target="_blank">📅 19:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150964">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
3000 سرباز آمریکایی در اسرائیل مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/150964" target="_blank">📅 19:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150963">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0340afb1.mp4?token=b6cS7V6Dfm_8plkvjC94Z7c98-7myeplefEJcBUqbabIO7cjvbtu3ryIEAdfzLrYWzcZBeZ1rTHgCQTXxLriEsFresiQsWXRTu0k_R3OG3Hdz9HCexQfQHY8p_e4QPSGSOnsXRxw7xAJ9DktL5S8b78tMqMV17nLhpvoccCyKRJoe1y61Ozfpuk3zIWJoClTx0aPZPXfcqAg83k-kxduAw2piAA4f8S7-cWTcSl_WxFiZ8PJakR3PKj4yKJ4fCveuwXZ2up57ADlCFfk0W-Yk3uVs1fqG--mf9Ytl6t_uv7xsILqoi7qLB-wO5nLcJqUcig5iV3Fuiz35nXPmAtxGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0340afb1.mp4?token=b6cS7V6Dfm_8plkvjC94Z7c98-7myeplefEJcBUqbabIO7cjvbtu3ryIEAdfzLrYWzcZBeZ1rTHgCQTXxLriEsFresiQsWXRTu0k_R3OG3Hdz9HCexQfQHY8p_e4QPSGSOnsXRxw7xAJ9DktL5S8b78tMqMV17nLhpvoccCyKRJoe1y61Ozfpuk3zIWJoClTx0aPZPXfcqAg83k-kxduAw2piAA4f8S7-cWTcSl_WxFiZ8PJakR3PKj4yKJ4fCveuwXZ2up57ADlCFfk0W-Yk3uVs1fqG--mf9Ytl6t_uv7xsILqoi7qLB-wO5nLcJqUcig5iV3Fuiz35nXPmAtxGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در یکی از تأسیسات آرامکو در عربستان رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/150963" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150962">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
اورشلیم پست:
جمهوری اسلامی کمک مالی به حماس را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/150962" target="_blank">📅 19:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150961">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری/سخنگوی وزارت خارجه:
تهران پیشنهاد مذاکره هسته‌ای واشینگتن را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/150961" target="_blank">📅 19:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150960">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
آکسیوس:
ارتش آمریکا درخواست عربستان سعودی برای بمباران حوثی های یمن را به دلیل تمرکز به روی ایران رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/150960" target="_blank">📅 18:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150959">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر انرژی آمریکا به سی‌بی‌اس: رئیس‌جمهور ترامپ به طور موازی به فشارهای دیپلماتیک و نظامی بر ایران ادامه می‌دهد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/150959" target="_blank">📅 18:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150958">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdpHikD2h7sHZ-Q97S3E7iG9A3asN79DzavLKQ6Yhzq2Bi7vCiqYnX3hk9akvsRecyeZRCNoelRBpBIpSZUjRpWcTdx9Y9Q2jPMF4Kb8E7ox54IjCuJHRDBIOjKd6x9csPK6x6ZsQwTCRWK4UnITreywqN3_cHCWvcq9difbCeckOARL-fw2_HJtr14xfzay8mWqG3oss1jk5y6Pir3YcTWMAnXx4sDLbJR4quGF-4Mw_wu0nGQaN6luXHDOWQeAN9VYyLD7UlEr-crq09Vv-D-M4tx-z3o4dUDemI104JMVQurMvO2bpofHunpDktFmMYOSgZSCakpyoJBTcFDN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از تهران که در رسانه‌های بین المللی منتشر شده تحت عنوان تحولات عظیم در ج.ا
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/150958" target="_blank">📅 18:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150957">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a09eee01.mp4?token=p_9nKredju3TjMfuDFhy8QhprFEoOGSYGBAwHjGcGASeD9tQZ-0hxYNkFd39kq8TwUMRXGf4uZZS7yodNLJ-DNdU3OLw6CU02cuLzdBtx7h6fazxxB_DgyRqAGYfYcZDcDHatL76_wUnJ6Rp5xfKHd--HiWPG3kgnOlI5KfnHwZ6tcwj6I59AB0sY_iZLRvWBvEBq0UjzwhqbG0CgKxDSyWKIUG8UIha3-rPqBG2znGRXuvXn0t8B_rlDRTKOlrwjQ9QObdUw5Xw8R-7E7-TosRM02tVKAdCGUqiseoGO7H8cfiFysqVIbA5hIdLx_eBkVGFHGnQ_-tdchf49CeRaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a09eee01.mp4?token=p_9nKredju3TjMfuDFhy8QhprFEoOGSYGBAwHjGcGASeD9tQZ-0hxYNkFd39kq8TwUMRXGf4uZZS7yodNLJ-DNdU3OLw6CU02cuLzdBtx7h6fazxxB_DgyRqAGYfYcZDcDHatL76_wUnJ6Rp5xfKHd--HiWPG3kgnOlI5KfnHwZ6tcwj6I59AB0sY_iZLRvWBvEBq0UjzwhqbG0CgKxDSyWKIUG8UIha3-rPqBG2znGRXuvXn0t8B_rlDRTKOlrwjQ9QObdUw5Xw8R-7E7-TosRM02tVKAdCGUqiseoGO7H8cfiFysqVIbA5hIdLx_eBkVGFHGnQ_-tdchf49CeRaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی یکی از شب نشینی‌ها، به یه دختر بچه گفتن بیا یه شعر حماسی‌ بخون تا علاقه‌ات به حکومت رو نشون بدی؛ اونم رفت و این شاهکار رو خوند:
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/150957" target="_blank">📅 18:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150956">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
بازار خودرو به شدت ملتهب و در حال رشده، کوییک به لحاظ قیمتی شده قیمت همین ۳ ماه پیش ۲۰۷ و ۲۰۷ داره میشه هم قیمت مزدا 3 های نیو قدیمی
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/150956" target="_blank">📅 18:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150955">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akVr3cI2Lc-y7wA0n2sexh0GdAnfLu1Gc0GFTmviDY0KIGO1CigzQP_fJLICHq1sQC5_XTUno4b9ZDNkIG5vWbnucPC-FLQX-HuU_A2bkoGp8wxWntRxLuYy8dAkdFTAp2TSUR-KWWsRPUc5bEu1xO2JDPw0unASR3-UOEY6i5JiCs1tZiGaUrJtOEFB5yWypvl3DoB2Fkj9oWwi4FrXKd4KsRugoCesCeLToxrzEY3VfoRZhYU8u3ZeJDNi7DsQ-x4Xj9mqTJ6SyIt5Pp7x1zLUwpUQ5RObJmN7PnA5ahV-cOyuBi5TjIg_onnEXBKvFPfz4zsg5GXtfbYJtPUT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی: آمریکایی‌ها میگن ایران ابرقدرت شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/150955" target="_blank">📅 18:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150954">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84aef80fb7.mp4?token=YD7zlKc5R3XGDUgaF6zVCm9njRmatJ395QfYwG5Ym7wpAEIdbbwSqmUkv5IyDwzSNJaQtB3MYSr6qTzlSvfK9RYIcnHddKrkQQAmBFdHXeWtLcfZs1Q_IfjMRJzHN2CuRrI62tK06f3pDbPcaFuV8FfEpMZiLIqT0CY95KnTyvD7tHpKnk9nxUgBQ1C6YGoVNwYfDPnjpqatR74rLKOaCzDN6pBAWRQcJp-dxlmkG5W9851hUxoJRphUzQL4j5Ar8Eks5pC0vq51R4Kl2cVSmkeexofGqi74jn9uYY3hk22XLCF0tAl1BDQ8hdD4ATgUNFfpE_Ve9i1iu_HW4PuF-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84aef80fb7.mp4?token=YD7zlKc5R3XGDUgaF6zVCm9njRmatJ395QfYwG5Ym7wpAEIdbbwSqmUkv5IyDwzSNJaQtB3MYSr6qTzlSvfK9RYIcnHddKrkQQAmBFdHXeWtLcfZs1Q_IfjMRJzHN2CuRrI62tK06f3pDbPcaFuV8FfEpMZiLIqT0CY95KnTyvD7tHpKnk9nxUgBQ1C6YGoVNwYfDPnjpqatR74rLKOaCzDN6pBAWRQcJp-dxlmkG5W9851hUxoJRphUzQL4j5Ar8Eks5pC0vq51R4Kl2cVSmkeexofGqi74jn9uYY3hk22XLCF0tAl1BDQ8hdD4ATgUNFfpE_Ve9i1iu_HW4PuF-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرار هیمتی از خبرنگاران
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/150954" target="_blank">📅 18:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150953">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
برآورد شبکه CBS: اگر انتخابات میان‌دوره‌ای همین امروز برگزار می‌شد، دموکرات‌ها با ۱۱ کرسی بیشتر، اکثریت را در مجلس نمایندگان می‌گرفتند
🔴
اکثر رأی‌دهندگان معتقدند جنگ ایران باعث افزایش قیمت بنزین شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/150953" target="_blank">📅 18:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150952">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
زلنسکی: آمریکا در تدارک برگزاری مذاکرات سه جانبه است
🔴
ولودیمیرزلنسکی، رئیس جمهور اوکراین گفت که آمریکا می‌خواهد تا پایان اکتبر مذاکرات سه‌جانبه‌ای با روسیه و اوکراین برگزار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/150952" target="_blank">📅 17:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150951">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت دفاع روسیه: دو کشتی باری حامل تجهیزات نظامی اوکراین را در نزدیکی بندر اودسا در دریای سیاه بمباران کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/150951" target="_blank">📅 17:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150950">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ارتش دولت یمن تحت حمایت عربستان سعودی عملیات نظامی گسترده ای را از سه جبهه به سمت صنعا، پایتخت حوثی های یمن آغاز کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/150950" target="_blank">📅 17:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150949">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFcdeeeGfqZc8qD_Bb5zMUImvf_S_p2RkZVIQUk2Hgw25DObrwi_fwDCCYxdauvLfPVfWTbSZk5ZfdENx6sbxibTW8mOeHQR1oxSmYeYJZq-4K6h78sX0KP0SdaAVsYW5QWEWjx-rQGwMNAJBSwOe7ER8Sw2_IUotbMlsNvcVlm3gkvmGRSu4nSi2_lCY6cA2h299186oQk18e66DWUOGv_qNPwHkCyfZbgkrRiQ02lYlOVeShnqPZpCvELE3hNfwb19gdD8kzm81str59-i4CyO2POztBtNYDlRoFpYAfhzhYuoOWrrdR7pEF7vJFM9fHC2EnEKHOClyihsx8CjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ایران انتقام خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/150949" target="_blank">📅 17:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150948">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/150948" target="_blank">📅 17:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150947">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ناو هواپیمابر جورج بوش پس از ۶ ماه حضور در خاورمیانه در تایلند پهلو گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/150947" target="_blank">📅 17:18 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
