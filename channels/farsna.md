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
<img src="https://cdn4.telesco.pe/file/BmCTUcrabdTrpcjKLd0_GrR-Y2ZaWa7NbIXqmXOKND7PTUYW5VVZj_w2fOkGmzFf3v9x78k4QFLdk6xQUf_jUcG0xPqqrH3eHFGhnQCvlR3L2k21QxCQ6rca5-9xBrx-EGMa-GE6uIirPwBGu39ieFmn0PLupRSM7pbxNU3AMlcaJYjF4jfUUzni-lukD5w4HRS0gl-LzRGPMJaJzg1QrknzCgjLkI2oERLxGQphOXp8rYOTbnaiPNKqrhfCdNTdByxP9SvFzj0SGKcj4dOxRWJ4zVlq8L5IkCjSERi0NA25avgrrnqyBA-jNH9c5xvsAXR8lfIIdQfF-wc3tUIvdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 00:11:03</div>
<hr>

<div class="tg-post" id="msg-448477">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxDoG_w7mNmWiTQXziENZ-eJpExUVwPVGLT_a1NinM3WT5sU41i19pIySOHDJqGQs3958J1cY88qt9laEZx2_vXyIwGO0UigjTzT6pkA3J5t54U-4iaUAQ8RRE9zkwwAXUl8YqJoqVRTjv8E4qBk5WrRaWmIxSM_K8X7JMGgDceGFGGC57qclBkg0akOdWIZ72X6svXX81LxqMY7SFTKwm2VPuuVrKdKjYSREMHy_jTAwqpRAec0GJDOfvtbuV6W8pxD41eSOl-CAI1vGGKQ-YO9mzqytVBN54nD37_qqy3YxCRAJItJq5os1bIAx4aV68pdYtdZPLxBWGbxS-_LlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قدردانی سردار قاآنی از ملت شریف عراق در پی تشییع باشکوه رهبر شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/farsna/448477" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
رویترز: قیمت نفت خام برنت با ۵.۲ درصد افزایش، به ۷۸.۰۲ دلار در هر بشکه رسید.
@Farsna</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/448476" target="_blank">📅 00:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌
🔴
صدای انفجار در چابهار و کنارک هم شنیده شد
🔹
دقایقی پیش مردم در چابهار و کنارک هم صدای چندین انفجار شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست. @Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/448475" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448474">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad76bbcd64.mp4?token=sxKncaH60yl7XRhAcxV56Vjm6cxYJ69BraDOeyRr1w5CHD2L0n03ATqE_9Nq6GoB2hYw07OuW2zrVrFYoHO9tZLIykXr1gq4OyeITw7aTzUgOa4PWKE-hj-Ya5gG1I_Pr7kp_CBLY8BQoLUEz1QLhVyJPtAYgCGY_QZcamQetvIkA6hib-jqyT6hiR6nfl23TN85l1j5kPML4NS_KFkqLyu5WESu0uVNLqFnVsAx7-p-hvu3DIuvggzELVWS9jE7_IM_coOSfMAW8EARojZ_boWWO5A4eClxKZjZog2jOlfCxdFV0zBmvZDoK98f7bvncHigbs69E3QoSKyDZ5i-hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad76bbcd64.mp4?token=sxKncaH60yl7XRhAcxV56Vjm6cxYJ69BraDOeyRr1w5CHD2L0n03ATqE_9Nq6GoB2hYw07OuW2zrVrFYoHO9tZLIykXr1gq4OyeITw7aTzUgOa4PWKE-hj-Ya5gG1I_Pr7kp_CBLY8BQoLUEz1QLhVyJPtAYgCGY_QZcamQetvIkA6hib-jqyT6hiR6nfl23TN85l1j5kPML4NS_KFkqLyu5WESu0uVNLqFnVsAx7-p-hvu3DIuvggzELVWS9jE7_IM_coOSfMAW8EARojZ_boWWO5A4eClxKZjZog2jOlfCxdFV0zBmvZDoK98f7bvncHigbs69E3QoSKyDZ5i-hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امضای مردم پای طومار «ترامپ را بکشید
»
@Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/448474" target="_blank">📅 00:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQgzW7SpyW-Wd6BwwUSX6jhimyKb9ShpyIpnOKa2SjBxdgneQlkQ-EMasQ9nIPNo91ImjXBk-I4OWfX5CIQWZJQvXPvFX-cEeRifSb7JgbIX9Sd-AeyppXS2aKhGfkKPLejeGSNxS_e4BXwkwi-mkbEH71s7iUqN17d7vMlMb5LFSJL7GrtxAjEFd0CJ6MDwkh1gZOsQeRj9mz1O17EXO-EKxNur9jdmtDWIqzvqo5j1hJnDCpAqvKrQ3TK9wd_piRzUNk_LiYEEyJ-Z46gjimIMynaHQ7i1PrTDlE2M4UfeUFcX6dswbtHbvHI_Y4rIdec1hoLtL86gekOzMRoK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| پنجشنبه ۱۸ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/448473" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9198ef1eb4.mp4?token=HpfAyVcff3AWk7hCsu92Ww6NnEkyH4Lsh4gDVGPp6PjHxE3RbG-mOOnfL1bYbFCkivf6xjj7pGoCtTxbWcR0DI3BUxT1PkXJzRsm3WQc1VFQUkXDGEmCfqU3mmtFvSqmqyYIToSxgOyUnxTaWHBvfHSfQqRa79jq9kr8e5Mo0JyyKo9tcMDbwhIFSL_t-ybJAh0BLBifSQKc5YNf5nySzmlK_pla2Xg8NZ-d8qffn0WZ6o7cDMqj5JUBspPQdj4ii67o6pY7BRpsUHdZ56seIq0JAq3OEHEpVYMvKy7_UEVWb3y0VmY8N_l26WxvIzyjKOAHo9Y-UXtaWjmLp3f8Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9198ef1eb4.mp4?token=HpfAyVcff3AWk7hCsu92Ww6NnEkyH4Lsh4gDVGPp6PjHxE3RbG-mOOnfL1bYbFCkivf6xjj7pGoCtTxbWcR0DI3BUxT1PkXJzRsm3WQc1VFQUkXDGEmCfqU3mmtFvSqmqyYIToSxgOyUnxTaWHBvfHSfQqRa79jq9kr8e5Mo0JyyKo9tcMDbwhIFSL_t-ybJAh0BLBifSQKc5YNf5nySzmlK_pla2Xg8NZ-d8qffn0WZ6o7cDMqj5JUBspPQdj4ii67o6pY7BRpsUHdZ56seIq0JAq3OEHEpVYMvKy7_UEVWb3y0VmY8N_l26WxvIzyjKOAHo9Y-UXtaWjmLp3f8Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب در مسیر حرم اباعبدالله(ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/448472" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448471">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayRaA-RCWYaCbhdhiuDmq13YKnyeeJkR8GrRvBEplTaPx023_cUd8zmcAddKJCHhktSvkG-aw3CEJ4mPLNF7dy3Bn0nHZxDKU010ChfiZjEd7CsLgL2cV99dOLV-5yzbag9d1TJ88DWKOzYf4uhW-dyyTe6UnW8CgDn4D_wpjTI0iGEfPol2c_3k7xJURcfJEu-SXuRFKerFQ5DV6fHMpcs4aTwtAtWxaZRhJttLh5Mrfp3fP4fXQQhgmHj9OaUV-BMR6BP-__VjliLO8rSFXbTiYFMURvDDd1jmnOKa2NYqPaqd6zE6QPLs7feWQdas7QRLgn4Tp6vbVreH2T_V2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آمریکا نقض دوباره آتش‌بس با حمله به ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که در واکنش به حملات ادعایی ایران به کشتی‌های تجاری در تنگ هرمز، حملات تجاوزکارانه‌ای را به چند نقطه در جنوب ایران انجام داده است. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448471" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در جنوب کشور
🔹
حوالی ساعت ۱۱:۱۵ صدای چند انفجار در بندرعباس و سیریک به گوش رسیده است.
🔹
همچنین صدای برخی انفجارها از سمت دریا در محدوده ساحل غربی سیریک به گوش رسیده است.
🔸
شب گذشته هم نیروهای تروریست ارتش آمریکایی به چندین نقطه…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448470" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2186adbf.mp4?token=XF-AwmLUwk65EV135XkIsdOuH23r3nElPDo891Sb_pBwY4TYLtofKGxRZiureJX7R4TG-eIvzRqlXJ8TXPrSkPaPhhYYIdfbZ3oFD6KZjv9hRGTcom6LOg43J8E3ugTDu9AT3bxUOKbwAgjtRamM5oYtL1ujCVhpDLMEEAZQVlX0A9xvf06GLKKM79Za9FJFqRTTzMAUqNvwmY51eoMRjkaOrkzHGqPfNRG0trV7ObRQ6wJSteBMw_49Mcm-wPBKOPo6TAb2JnqxteKyVUQWGiJNWIesr0qs0ZHv3gOeQhmiJDTSLFpkeuRO3CrZizMZ-omIy2IOJt6iYMzIOODuZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2186adbf.mp4?token=XF-AwmLUwk65EV135XkIsdOuH23r3nElPDo891Sb_pBwY4TYLtofKGxRZiureJX7R4TG-eIvzRqlXJ8TXPrSkPaPhhYYIdfbZ3oFD6KZjv9hRGTcom6LOg43J8E3ugTDu9AT3bxUOKbwAgjtRamM5oYtL1ujCVhpDLMEEAZQVlX0A9xvf06GLKKM79Za9FJFqRTTzMAUqNvwmY51eoMRjkaOrkzHGqPfNRG0trV7ObRQ6wJSteBMw_49Mcm-wPBKOPo6TAb2JnqxteKyVUQWGiJNWIesr0qs0ZHv3gOeQhmiJDTSLFpkeuRO3CrZizMZ-omIy2IOJt6iYMzIOODuZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تراکم جمعیت در اطراف خودروی حامل پیکر رهبر شهید در نزدیکی حرم امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448469" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448468">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در جنوب کشور
🔹
حوالی ساعت ۱۱:۱۵ صدای چند انفجار در بندرعباس و سیریک به گوش رسیده است.
🔹
همچنین صدای برخی انفجارها از سمت دریا در محدوده ساحل غربی سیریک به گوش رسیده است.
🔸
شب گذشته هم نیروهای تروریست ارتش آمریکایی به چندین نقطه…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448468" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448467">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تغییر ساعت مراسم تشییع رهبر شهید در مشهد
🔹
ستاد تشییع رهبر شهید: با توجه به استقبال کم‌نظیر مردم عراق از پیکر مطهر امام شهید، ورود پیکرهای مطهر به مشهد مقدس با تأخیر همراه شده و از همین رو مراسم فردا در ساعت ۱۴ برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448467" target="_blank">📅 23:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448466">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در جنوب کشور
🔹
حوالی ساعت ۱۱:۱۵ صدای چند انفجار در بندرعباس و سیریک به گوش رسیده است.
🔹
همچنین صدای برخی انفجارها از سمت دریا در محدوده ساحل غربی سیریک به گوش رسیده است.
🔸
شب گذشته هم نیروهای تروریست ارتش آمریکایی به چندین نقطه در استان‌های جنوبی حمله کردند که با پاسخ نیروهای مسلح ایران مواجه شدند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448466" target="_blank">📅 23:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448465">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee8e83406.mp4?token=ko3e1AjAQszDUrF-vOOfuUksyDXhqZeu4a2EdqE4DBxOzbvk4dasAkaRWBWn32Q4YR0aZ0rTaBbALHl-LPt0Bn6m1ZhIWaoaw8VCg4-1SxvDmmVf0lYG_PmNIMNNASnoVtKk3fGA4CtgOCqSUKdSn2KtVWONax_UdJp5jRhraPGqNDpNSeLaQG0aVHypkD1OjyHg3lpCZjfivWic-FpjBFCtfU26LrlVxDBU7sz442nXz-dw_rhs0HuqDUm0G72HlGJGgJ4kv9FdQsm9MtavKaqdMKgF14JpGpbQFypkcIcU6tlr-imGf_eBxodqSyixN17xt_84BiC9Nrn9LGj3aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee8e83406.mp4?token=ko3e1AjAQszDUrF-vOOfuUksyDXhqZeu4a2EdqE4DBxOzbvk4dasAkaRWBWn32Q4YR0aZ0rTaBbALHl-LPt0Bn6m1ZhIWaoaw8VCg4-1SxvDmmVf0lYG_PmNIMNNASnoVtKk3fGA4CtgOCqSUKdSn2KtVWONax_UdJp5jRhraPGqNDpNSeLaQG0aVHypkD1OjyHg3lpCZjfivWic-FpjBFCtfU26LrlVxDBU7sz442nXz-dw_rhs0HuqDUm0G72HlGJGgJ4kv9FdQsm9MtavKaqdMKgF14JpGpbQFypkcIcU6tlr-imGf_eBxodqSyixN17xt_84BiC9Nrn9LGj3aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از حرکت پیکر مطهر رهبر شهید به سمت حرم امام حسین(ع) در میان انبوه جمعیت
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448465" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de0aadf74.mp4?token=NjF1OHBiQosc8wLxH0GKSSVxioXCgdKfSjOyAhVViHRNGArSsVr1hBHqU_dR04xM4tVlcNOLbwEG2pC7r4ZHd1GUgIcs0VPPpCC98gD8fJyFcRTHk_x5ldmg0fq9feQA_q1lLbFjY-sT2ih9RK991KZ0fDrg4uEHcitqB-KQu0wGeroBESBAvGZ2PXTpLsMUBQkBAK95PX1AHG7RFbwG25KevmharbbyAyF869BNDUb1Ko71d4glAu-TXlXH3g1dyafxgUqSEUgDgT6viVDUl8d-UrcJKM-7ht22lyuE8hQDaFhAH_TRDkSCxyNJkcNF8yl5BXEPsOK8WHEszVrImw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de0aadf74.mp4?token=NjF1OHBiQosc8wLxH0GKSSVxioXCgdKfSjOyAhVViHRNGArSsVr1hBHqU_dR04xM4tVlcNOLbwEG2pC7r4ZHd1GUgIcs0VPPpCC98gD8fJyFcRTHk_x5ldmg0fq9feQA_q1lLbFjY-sT2ih9RK991KZ0fDrg4uEHcitqB-KQu0wGeroBESBAvGZ2PXTpLsMUBQkBAK95PX1AHG7RFbwG25KevmharbbyAyF869BNDUb1Ko71d4glAu-TXlXH3g1dyafxgUqSEUgDgT6viVDUl8d-UrcJKM-7ht22lyuE8hQDaFhAH_TRDkSCxyNJkcNF8yl5BXEPsOK8WHEszVrImw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر رهبر معظم انقلاب بر فراز دستان مردم عراق در استقبال از پیکر امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448464" target="_blank">📅 23:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiQweoxCSBEWOOLqlj7yHuHomIxFcseUsE_5eaKXhmYFrHok78mrimRIzRH4E7emLoSlrrYsOgUVTUFhXvLulnL7vsiXfoT5_cglnFmzx97P4Q8b3Z-lQPI6p34qtYqWbn6dDKzkHMiiVYMbwgm09XF7WTWyrZt0OAsq_Tzfi5QZU_ggYheH4E5tBOoIi8LiWm12O4Y5l3Yb-qzBrx7P6lidufAr8FmKQ-5IBBeg1sy_suXktUSIg0UfPS3s8juLvZo03egW-0uLUIzeH_KsXs0t3dmF2yUkddx8uUA5x1oaXIlSAB5kLkYHJKshSDNFgXN4EW-51NbunkkypV5JbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله: تشییع امام شهید آیت‌الله خامنه‌ای قیامی الهی است
🔹
شیخ نعیم قاسم: ما امروز به مناسبت تشییع پیکر امام مستضعفین گرد هم آمده‌ایم؛ باید برای خدا برخاست که این تشییع، خود یک قیام، یک حرکت و یک انقلاب است.
🔹
امام خامنه‌ای یگانه عصر خود و رهبری استثنایی در دوران معاصر بود که نظیرش در تاریخ کم‌مانند است، ایشان ولی‌امرِ امت و نایب امام غائبِ معصوم، امام مهدی (عج) و بنیان‌گذارِ پایه و اساس تمدن اسلامی معاصر بوده است.
🔹
امام خامنه‌ای مرشد، حامی و مربی بود؛ رهبری که در دریای جمعیت، مردم را به سوی رهایی از بت‌های مادی‌گرایی هدایت می‌کرد.
🔹
ایشان سیاستمداری کارکشته بود که ابعاد امور را در سطح جهان درک می‌کرد؛ او مردی بود که با شجاعت، عزم، عزت، اعتماد به نفس و توکل بر خداوند متعال، استوار ایستاد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448463" target="_blank">📅 23:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448462">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi72nmew1ZUN0ZgkmHAljN8AJ2Vmq4Qh4z2s65jF0lbOnsQ0ibFhYgU4b_nS_lmWYE1to602SHow5VJvvzSn1NKxnXWllB55A69JQsbC69Y2kGS2s01Z0NcCuUlWH0JeTCytrG5ay2slAcpeouyxvFilqCGSeQplT3DCv6qSuBmyTTbqCgIYXkL5r-ckyddYn9CfZ6pW_fgqz2CG3XoLN0UiYiGLI97lzoqcojs1DztVmyGtNDvgVsWWHh-IKu8SaD1PHeDDsqoqEVs-Wi8rpxfx-SZqtG3-KqQwVgF2Gd85afqCApOaPvRbrAGqJzfg3uIpU0y6EtxI6hklPIqpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
زائر اِرباً اِرباًی امام حسین(ع)
🔹
دست‌نوشته زائر عراقی برای رهبر شهید: از فضیلت کسی که پیاده به زیارت امام حسین(ع) می‌آید شنیده‌ایم؛ پس حالا فضیلت کسی که اِرباً اِرباً به زیارت او می‌آید چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/448462" target="_blank">📅 23:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448461">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
فریاد خون‌خواهی بروجردی‌ها در ۱۳۰ اجتماع مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/448461" target="_blank">📅 23:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448460">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d4f9ee59.mp4?token=cvh3eK-b5nczfk-nrO3rKVn0bNBOEPNjTO6Xlu3uFYsixM_J3ae7Gec5jVrEsqvGAVRXMPGZ1bXKEE54jGqO7LqG47GBBS94PWV5waJz1oJ5ymcDu9CK2ZpB96aqiPZVEX3QI4Q_0qnXhBxRSDvjtvjT6XGqMw7gldh94tWVARQr12D7GjXJAuEM-TNhn8glbH2sne13TKU-qJmP9lfqDbhtbtmApEp1BFb8Z9B2P9n4tS0GV8jGlVd_TaLNWFHy_kp_3ud7KnXz415fY41C5uFz1P1Xf9r4J9_y0-Gt2fOQUWoEiWaCJAfxvCxET0EZXNGd2HE0yhZxh6___hIUew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d4f9ee59.mp4?token=cvh3eK-b5nczfk-nrO3rKVn0bNBOEPNjTO6Xlu3uFYsixM_J3ae7Gec5jVrEsqvGAVRXMPGZ1bXKEE54jGqO7LqG47GBBS94PWV5waJz1oJ5ymcDu9CK2ZpB96aqiPZVEX3QI4Q_0qnXhBxRSDvjtvjT6XGqMw7gldh94tWVARQr12D7GjXJAuEM-TNhn8glbH2sne13TKU-qJmP9lfqDbhtbtmApEp1BFb8Z9B2P9n4tS0GV8jGlVd_TaLNWFHy_kp_3ud7KnXz415fY41C5uFz1P1Xf9r4J9_y0-Gt2fOQUWoEiWaCJAfxvCxET0EZXNGd2HE0yhZxh6___hIUew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب به عمود ۱۳۲۵ رسید
🔹
کمتر از ۱۳۰ عمود دیگر تا رسیدن پیکر رهبر شهید انقلاب به پایان مسیر مشایه و قرارگرفتن پیکر پاک ایشان در برابر گنبد و بارگاه حضرت ابالفضل العباس(ع) فاصله وجود دارد. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448460" target="_blank">📅 23:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jzd5Ru9G5aLnOblS5nGm4Qv2DJrFZbVxJSP8LDwapNQqc1Rzp_y7KFLkx0W6Ene20nTa1vBRE3Vt2rbEQK1jLkHzNVi2jXhKXLMA7W6TvcLbqmVIxLrodwaFILXbpsg3IHJ4YtvqsD0V_IFvkbl2u9alXl6wHC6UWfjATJbsBvVO_q2DL2_vAt67NFYtwPxmb2EKIGF0yXbwfN8GrspZBePqbKHnuO71ZCH_q-jJNswMoM1ASpmYFgRMJsEdiu0wjehT_oTbBnaAWc6f6qHWDaIKaLF5OhVrrr9RnRt9Htdi_nIudZfxo2han_WoGl-9tz65l2md-uOY3rR8VZptyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLNxoxiqWZIlAP0epC5inoOPwVmm-JWYoqI_Ti1wNEbnVWhwRyjOkr9f9uFeIcTc8IUBuOIGFc_bzUR14oFdJdp1fXZ27q2u9m8XP5sr64sYkXg-ccZ1k7NGQf1YkeQ1SdBxKt4Lfm7w1Ep9G6yX4gQBan00iSpnwEP9HF2p0a_KISkOWAvRSgjzmhSPhFN7EOuGZTtNc_5BDMfA1DBZb_Nxv_cD1zX2OHd7StjpXyPrmD0ZtTv_VctuRIkkcWaEIZBq1RnNTIEIoSG3WXAZW1Mgkzdn-jxaIHlbAIItXe17vxasbNl3ub19Kbac2OkJkUS_Wa6rRs_oKrhYjv3ztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdEjnRjQWQjSEoS65jhW768fl4_6Yd-6sbOiDSiIzEzdkujvDRCCOZLnrMpQFeCO40-VX__unoMUot-rpr3cd_WQFvaiWMdQw6o1vOQ0VXmUKO3s9sPlbFnPWG5rtT4p0Xh9uaxYtgJpTPCLZB77E9HDVvmHI9EATmiRZhCQQiXTXCS3XFciXMDQOyaJ3Als-2sDzpaZsXiPRbYFqhzFJUq9RRzl666813XMDDtxgCrjfb_45DJ0gCa8yEBjkmExE7i5-U9pf4i3QCX43C9f1zCYL403YuBiXYCPa26bkJDitmkgORcDgqgBDdNwtM0NObV3hhnF26NUwkjwkVHX3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZUDghAmfsEI7FOE3rcFnLI5A6S-eh93J3Y9DXTAPsg7cCAsxAxaVPfK7_Fn3jkGvJsrUdmRtOIQooyWIVkL7Zrva-5pOfAxL09pbmfwX9nW00KSw54MVIeyXhqrGSRYyIMg0E6q2Y2KfQ6jhFtSTWudqFP6s9vnaQVlLB6lafko7i2Hh8mugcjpqipDvtEFr2QmPY-A6hJW7D7D8FYbfXnJzQxoNImzDFr09AVSDMGUP_w_zkHXtAOXzFbi4SsRxF46ni1EBZdTVlmOg8H7BnOgGoct9h_QUG6QPPA2O_2YYrTlphuwLO8tHfL1osuR3pdpomO2yAV_EDg1NtbZKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از تشییع رهبر شهید انقلاب در کربلای معلی
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/448456" target="_blank">📅 23:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008000a807.mp4?token=fWRy8Oo0A78YBPEI9zxK91UqK-eXY0Socw4ECfM-rvb6bDkLOEQ8-dRdTd4zkVU5AM-UrGhPvF_Vf0FZ_RuMVLylHdcyG6-nbGJxm-xSE5yrIvCzGP3Z4_uLAQLErwGv1VzJE9tHKHoVBb-PIqmBDrzHWXjLM160QjqlOTJsE6IuY_IvBzW4eUk5mhLB9E3Km-yVWVSMCf5wj2h4-8_ZxBcPKcMVWWsqC4n4HErLbhnAUGbNpgDk7sKC6MLX_y8RMZsxv23nK-FqvVDg_tGiegwDriIp6tS_95iN-mqj6NpwvYwG1enJYtvTMOt84DLpYfJShwrRBkpVUGL6eBjbYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008000a807.mp4?token=fWRy8Oo0A78YBPEI9zxK91UqK-eXY0Socw4ECfM-rvb6bDkLOEQ8-dRdTd4zkVU5AM-UrGhPvF_Vf0FZ_RuMVLylHdcyG6-nbGJxm-xSE5yrIvCzGP3Z4_uLAQLErwGv1VzJE9tHKHoVBb-PIqmBDrzHWXjLM160QjqlOTJsE6IuY_IvBzW4eUk5mhLB9E3Km-yVWVSMCf5wj2h4-8_ZxBcPKcMVWWsqC4n4HErLbhnAUGbNpgDk7sKC6MLX_y8RMZsxv23nK-FqvVDg_tGiegwDriIp6tS_95iN-mqj6NpwvYwG1enJYtvTMOt84DLpYfJShwrRBkpVUGL6eBjbYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم خونخواهی ۱۳۰ شب در گرگان برافراشته است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/448455" target="_blank">📅 23:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448454">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12a187cbb.mp4?token=KBvNSCKeT6LoRng3LQW9nHxgIAVoP6rt2h5XINuTMxIXUzlREWNbMmuJ12KH1ueFV9hnkUTzTCkdzeaaSE0RIyK2itjgQY_bX4nkjuQOKcCPUrV-aWYPBzJmqHDyyCA9LefGfAFPw6J0EneiqFfQxUC_f0J1oYsa-ewTFcmzqJfh447VG7jPuG2_P21ZfnZxkvAxD3HuDRch2gT_-uAr3bf0FC6KFZ5MzLGzkpkxWB1li2yGCJuvolpBBXlRtPBfv98jeu1Pvp24gossMHcJubAs57mzZJmwuyRhAUsLL98W7lIIlYsZOqSIWbZ8dW1jAS_gSywunVssj5by9Jvkyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12a187cbb.mp4?token=KBvNSCKeT6LoRng3LQW9nHxgIAVoP6rt2h5XINuTMxIXUzlREWNbMmuJ12KH1ueFV9hnkUTzTCkdzeaaSE0RIyK2itjgQY_bX4nkjuQOKcCPUrV-aWYPBzJmqHDyyCA9LefGfAFPw6J0EneiqFfQxUC_f0J1oYsa-ewTFcmzqJfh447VG7jPuG2_P21ZfnZxkvAxD3HuDRch2gT_-uAr3bf0FC6KFZ5MzLGzkpkxWB1li2yGCJuvolpBBXlRtPBfv98jeu1Pvp24gossMHcJubAs57mzZJmwuyRhAUsLL98W7lIIlYsZOqSIWbZ8dW1jAS_gSywunVssj5by9Jvkyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ از ایستادگی مردم ایران به جنون رسیده است
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/448454" target="_blank">📅 23:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448453">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2607292543.mp4?token=ckYWgMe4tO0wz41yX-lRfWj__5rrJXAInp_nD9bXXafU63PSyU8gXMD2xVZZW2I4FCdRt7OBFlAEhN9woweAT2rMeL3DjrA34uf5bToto-PtGTyfnQSyW13L21ynjPPwt1syW3UMvLh5JRR8VlCcGBcWHTSz4qCCSkua7-87juzYPRFEdvzTtdoYhFncNm9nOAr8SYfHMz7YTBlK84fyavwdYOCwmnpSQd-UhQgsf2JeWgiBF9ubBteyUqq3iu-APxKzJVPxDDgu8SdyA7nyQiVd1rZMA5_3ZKrL9OZawcoXqtUf1ohv9HwiQszpvlvhKkC7BOlo2sQNOMt6vhVumnVxceMraAUE1X8FKvK957Q0HtGvlO5_og-QaegpxwvOhCdgH7eDOBU_Kzvi7vg8CCqzoHlPG5w1g4qxCqGwYio9S0HKeGBdnJq-43mziMJz4jXOZ7o4Ps1RwCstO8wv76V4ogFXhkGNP-rzlEiAvwgyHm-QoZfwGzQMgJndPnKfm6oIadQa2nA6b6z-ATy0VXXbkKGD2_3-1Em73FHBhzok0g5PqYJULgbjhg8pjLDl-8p48skA0mdlR3zb4gpldrLZVa0x3iEhQ7iNNNRk6PmQOjmmqJZoJsO_lNEU5lcPrSrOeqtu3KeSSZEVegqjVgEjxV-QaJbppPufwoxtOK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2607292543.mp4?token=ckYWgMe4tO0wz41yX-lRfWj__5rrJXAInp_nD9bXXafU63PSyU8gXMD2xVZZW2I4FCdRt7OBFlAEhN9woweAT2rMeL3DjrA34uf5bToto-PtGTyfnQSyW13L21ynjPPwt1syW3UMvLh5JRR8VlCcGBcWHTSz4qCCSkua7-87juzYPRFEdvzTtdoYhFncNm9nOAr8SYfHMz7YTBlK84fyavwdYOCwmnpSQd-UhQgsf2JeWgiBF9ubBteyUqq3iu-APxKzJVPxDDgu8SdyA7nyQiVd1rZMA5_3ZKrL9OZawcoXqtUf1ohv9HwiQszpvlvhKkC7BOlo2sQNOMt6vhVumnVxceMraAUE1X8FKvK957Q0HtGvlO5_og-QaegpxwvOhCdgH7eDOBU_Kzvi7vg8CCqzoHlPG5w1g4qxCqGwYio9S0HKeGBdnJq-43mziMJz4jXOZ7o4Ps1RwCstO8wv76V4ogFXhkGNP-rzlEiAvwgyHm-QoZfwGzQMgJndPnKfm6oIadQa2nA6b6z-ATy0VXXbkKGD2_3-1Em73FHBhzok0g5PqYJULgbjhg8pjLDl-8p48skA0mdlR3zb4gpldrLZVa0x3iEhQ7iNNNRk6PmQOjmmqJZoJsO_lNEU5lcPrSrOeqtu3KeSSZEVegqjVgEjxV-QaJbppPufwoxtOK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم عراق پیکر رهبر شهید را گلباران کردند
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/448453" target="_blank">📅 22:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448452">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7afb780c08.mp4?token=H6DDGuGflWfxDaKre8c1vEE_kk4bfHrXX6Pji1z2MPgodvQ6eJypJdpddAEkWtI1P38fGIl_szfni0cz7JjqWRTeYu4hlBmLXck9tWUod21_ghbwrtjrHA9avZX_dhAl6rQsdolJmAj9jokc2lPHYQxnD7evx00TwRW-sgKcVGWbxyFe9zr8P1jCpZUV9veFsJ58xLD_0m72LbPK5u2gkGovJoU0CYVB1-WlMXqOzAPthm0eUPJhy7rzFaT2I0bmfR_9LzwdwKV0ZItbXO5y5m2HP2xXm_jHdG2XxSzzMby6abHGejuWzcvjs9i51VkP1XHBCViOmQq-BJSeWfbZfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7afb780c08.mp4?token=H6DDGuGflWfxDaKre8c1vEE_kk4bfHrXX6Pji1z2MPgodvQ6eJypJdpddAEkWtI1P38fGIl_szfni0cz7JjqWRTeYu4hlBmLXck9tWUod21_ghbwrtjrHA9avZX_dhAl6rQsdolJmAj9jokc2lPHYQxnD7evx00TwRW-sgKcVGWbxyFe9zr8P1jCpZUV9veFsJ58xLD_0m72LbPK5u2gkGovJoU0CYVB1-WlMXqOzAPthm0eUPJhy7rzFaT2I0bmfR_9LzwdwKV0ZItbXO5y5m2HP2xXm_jHdG2XxSzzMby6abHGejuWzcvjs9i51VkP1XHBCViOmQq-BJSeWfbZfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشق و علاقۀ عجیب جوان سرباز به رهبر شهید: ساعت‌ها کنار جاده ایستاده‌ام تا شاید حداقل ماشین حمل پیکر رهبر شهید را ببینم!
🔹
تابه‌حال نتوانستم ایشان را ببینم.
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/448452" target="_blank">📅 22:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448451">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کربلا پنج‌شنبه تعطیل شد
🔸
کربلا به دلیل ادامهٔ حضور جمعیت‌های میلیونی برای شرکت در مراسم استقبال و تشییع پیکر رهبر شهید، فعالیت اداری در این استان را برای فردا تعطیل اعلام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/448451" target="_blank">📅 22:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448450">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/468085ec2d.mp4?token=e7FiObVHAnK8lbze4YTEv3Af52hcoNlJwoRqmyCiVJGDWxRyO5arD9clpI0ajAJ4UZO5xAXpsnjZeBylOsXZBHJVIqIch8cfB6QE1_q4b-NYFoG63QeKF2dmvDQh0pa2rFN6jQoBqWg6oS1xr3yl7nsA8fOPeFzzLe5ESi9zV3Tgd2me0QRsEb6k1ipG7cHOYVnz64I3PJz7-_fSupo3uiTaXPDZ2mnB2YQP8-XTCmdG6_wg8Uny7pvaT8y56ivc2wl0ttAwWU2mNBVM0fCYRe8QjTOby-u7M8oY7f0246mGf8kFPsZfN9O3wSuQzc7phSS4nvFU94cKjWJxzzVPrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/468085ec2d.mp4?token=e7FiObVHAnK8lbze4YTEv3Af52hcoNlJwoRqmyCiVJGDWxRyO5arD9clpI0ajAJ4UZO5xAXpsnjZeBylOsXZBHJVIqIch8cfB6QE1_q4b-NYFoG63QeKF2dmvDQh0pa2rFN6jQoBqWg6oS1xr3yl7nsA8fOPeFzzLe5ESi9zV3Tgd2me0QRsEb6k1ipG7cHOYVnz64I3PJz7-_fSupo3uiTaXPDZ2mnB2YQP8-XTCmdG6_wg8Uny7pvaT8y56ivc2wl0ttAwWU2mNBVM0fCYRe8QjTOby-u7M8oY7f0246mGf8kFPsZfN9O3wSuQzc7phSS4nvFU94cKjWJxzzVPrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌چه در تشییع رهبر شهید رخ داد، در قاب رسانه‌های ضدایرانی جا نشد
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/448450" target="_blank">📅 22:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448449">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20b5cebaef.mp4?token=pIkvDlNw5TEKs80yWoa6sEc98OYuhnTGbVPWxWABmxo97ZaOmf4dWFvT0EBMqYcWt5fMrFXMi98SHd14lD_bAjQi4bc03SQ0WTYjZcFdqzO4bWqQbAFS9O3zahGdPWL8dywrv-w9w-Wm-FqaVmLos2SBppbtlAYCnzQ95jsF7Ej3z90jNQMrA6haNzNDGdufCYWtZSOq3HnG09KUg1Hjmkqcls_WB6JlWYjUhqONh9gLYwTGLNTAVvMatniv_M8ihPwSnv-eRdw5TNPk_6aWceI4zHsKWU73EWdm8yzXF8AFDUkJ5wRHTMJnOi3o4VzGDTpLlXkUHJ5pI4yB9r8yhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20b5cebaef.mp4?token=pIkvDlNw5TEKs80yWoa6sEc98OYuhnTGbVPWxWABmxo97ZaOmf4dWFvT0EBMqYcWt5fMrFXMi98SHd14lD_bAjQi4bc03SQ0WTYjZcFdqzO4bWqQbAFS9O3zahGdPWL8dywrv-w9w-Wm-FqaVmLos2SBppbtlAYCnzQ95jsF7Ej3z90jNQMrA6haNzNDGdufCYWtZSOq3HnG09KUg1Hjmkqcls_WB6JlWYjUhqONh9gLYwTGLNTAVvMatniv_M8ihPwSnv-eRdw5TNPk_6aWceI4zHsKWU73EWdm8yzXF8AFDUkJ5wRHTMJnOi3o4VzGDTpLlXkUHJ5pI4yB9r8yhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درسی که شب گذشته به آمریکای کودک‌کش دادیم
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/448449" target="_blank">📅 22:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448448">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5m2xwtPtyQDTD0zl6z7Mb8m3h3iDLBNjrfK8qBKje8LqGd8dhlaveHOMSF19eDnJmICo67vhAgFVO6pvfmWVo5coWtqReLkaOyZIYS0kfzIdIkTNDlEN_fTp8CE9NNxWR2dKQIwd2N4dfr6aAxLgqbo4tj6EB5QTA58kqv6MSdjqdFqztepJZgcQ9240-sbNX62-0dd_Lrbd-4vhSzSI9ydgSSgZM94esQvN9eLWQUiVuXfevdkKWtPuresuwnEnJ6Zy-ZxRKedi7CQuz6j7SNzoz2WoXvfj8oMSc-1vRx15fmbDyAyllG9jQKJBrNrVv7lLQ0uBZI3LBbEUzCZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دستخط عاشقانهٔ رهبر شهید انقلاب در وصف امام حسین (ع
)
بسم الله الرّحمن الرّحیم
این حسین کیست که عالم همه دیوانه‌ى اوست‌
این چه شمعی است که جانها همه پروانه‌ى اوست‌
🔹
اى شعلۀ فروزان، اى فروغ تابان، اى گرمابخش دل‌هاى خلایق!
تو کیستى با این شکوه و جلال، با این شیرینى و دلنشینى، با این هیبت و اقتدار، با این‌همه لشکر دل‌به‌همراه، با غلغله‌ى فرشتگان که در کنار موکب تو با آدمیان رقابت میکنند؟ تو کیستى اى نور خدا، اى نداى حقیقت، اى فرقان، و اى سفینةالنجاة؟ چه کرده‌‌اى در راه خدایت که پاداش آن خدائى‌شدنِ هر آن چیزى است که به تو نسبت میرساند؟
🔹
بنفسى انت، بروحى انت، بِمُهجَةِ قلبى انت، و سلام الله علیکَ یومَ وُلِدتَ و یوم اُستُشهِدتَ مظلوماً و یوم تُبعَثُ فاخِراً و مَفخَراً.
۹۳/۲/۲۹
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448448" target="_blank">📅 22:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448447">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a329c47e75.mp4?token=tzCp2nGsWTNADhy-HKfc90BIw5fpTv70zyBQ2eOeiGKjwG7SWRfgiGi0YP8881CWtZW_LGKa89sg-9UBbjZtwfsZWnhCKeQn4YCEKP4hz1sN36O5__eSgSI4giB-5VuckuIVSRqtfilqnSq5Efd7kJdGKOqYfg9k5dQP7w-Ka4u5lWT_G0U88r2i-hsCKUkzvVIM3DA4l4IIfag_V70-tXER78k22FlFWM8gDPnp1bbDSRL-qi8Qky4dhYx7f1xc2rP5ZqJUD7LKykNkyBvKHLQdTm3rk52dnbkpgfQp7-imZIGOwI4k086piz34rxzmVZ-U-dWF69eyuhUMiDvs0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a329c47e75.mp4?token=tzCp2nGsWTNADhy-HKfc90BIw5fpTv70zyBQ2eOeiGKjwG7SWRfgiGi0YP8881CWtZW_LGKa89sg-9UBbjZtwfsZWnhCKeQn4YCEKP4hz1sN36O5__eSgSI4giB-5VuckuIVSRqtfilqnSq5Efd7kJdGKOqYfg9k5dQP7w-Ka4u5lWT_G0U88r2i-hsCKUkzvVIM3DA4l4IIfag_V70-tXER78k22FlFWM8gDPnp1bbDSRL-qi8Qky4dhYx7f1xc2rP5ZqJUD7LKykNkyBvKHLQdTm3rk52dnbkpgfQp7-imZIGOwI4k086piz34rxzmVZ-U-dWF69eyuhUMiDvs0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کربلا صحنۀ وداع عاشقان با رهبر شهید شیعیان جهان شد
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/448447" target="_blank">📅 22:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448446">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_UyClSnFG2bTBZ16p-RErsX8FuNHCzPbc4YlyAwGM23CYQb-E07WQO3po2Vdjt-u5s5G2rzv5ksW00WqhtziLiyrcHmqRIKgoEADZ_tMhfhWhveJkX71T08EO92y_TiT8ysA7IFOToZAvBdM78Y285BVivghTeR_C5ugY0O43570uHU0OAgzNwbA3CtiRodempO_Mpub3NVWpnfVnPpBO9NkaHYQ7gIVwUOmZdKTUuWdC6qbFV5nY-06WHrqA6it4IMcHbM0l8KjY576YoUaacaNP15PD5vIc3EkkMLxGVFRKc4b5zEHoEE6rlJfVhT_V2VCBozeTfeETNv1GE7jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شریعتمداری: فاصلهٔ ایران با سلاح هسته‌ای، اراده است نه فناوری
🔹
مدیرمسئول روزنامۀ کیهان در پاسخ به سوالی دربارۀ توصیه عده‌ای پیرامون تغییر دکترین هسته‌ای ایران، به فارس گفت: جمهوری اسلامی از دانش و توان فنی ساخت سلاح هسته‌ای برخوردار است و فاصله ایران با تولید…</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/448446" target="_blank">📅 22:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448445">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11ab5a8965.mp4?token=bVwgq6SB4heT-MFy7uCIv3HJ4lTFHVFdd5ElDJhoP0UVDPkj66ymJrp7RiVF6wFEFyRUVP_TiDSTm88wJyT3ba8B9xAz--CkEZd1-G1BQVtWONDenFftOwdudSYlgW0TJVisEL6MytJNINMmBEv6T2ue-c1ejxUOehyf7JQr9rjYwpr_RQrgLWtXz6bJ1ewdzia-a2DkoQKU7p2RFPtgH_Yc2qyRjL7Afu33AQSstZil6S8Bk16zg4fJ5FsS8GDyvSEAwU2N48DzpRROm0TRNIk_lyt4rhsNNdsDZKo5uqgTKv0UehXapLPo0oabfMC2-xwkq0eN7qAgeYiCgqvdPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11ab5a8965.mp4?token=bVwgq6SB4heT-MFy7uCIv3HJ4lTFHVFdd5ElDJhoP0UVDPkj66ymJrp7RiVF6wFEFyRUVP_TiDSTm88wJyT3ba8B9xAz--CkEZd1-G1BQVtWONDenFftOwdudSYlgW0TJVisEL6MytJNINMmBEv6T2ue-c1ejxUOehyf7JQr9rjYwpr_RQrgLWtXz6bJ1ewdzia-a2DkoQKU7p2RFPtgH_Yc2qyRjL7Afu33AQSstZil6S8Bk16zg4fJ5FsS8GDyvSEAwU2N48DzpRROm0TRNIk_lyt4rhsNNdsDZKo5uqgTKv0UehXapLPo0oabfMC2-xwkq0eN7qAgeYiCgqvdPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرزوی ۳ ماه پیش از شهادت رهبر شهید انقلاب اسلامی که اکنون برآورده شد...
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/448445" target="_blank">📅 22:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448444">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4066b49a.mp4?token=pfSWkWsQaTx7POFC9C3gXjJhOaIZWNG-Ph13TaBsR3Zz9l0-r2kGqi-B6pSXVy3drnEYTKOc7Hy42dw7GschioDdhux_4pMeFuvQiJHHxK7DWdncYqn3Wv_e8zWNrWJzfieS1JEo0bHPCwzkMvpVOc7CTVeCQtrapogEoPAMXa42ILMyCygotFHYjIZ6RSjEmlpehHK9jLD1C4J6tzPHhlYMPffTCHgtnAFFj6stiG0kpMjT-o5OdBz0Bm0EhO2LCkrjViWpwvc4hCWsC7p7m7naKxs3RO4Ib-8F6VVY6pPJKIzRbh8tvBtq6kjfH2MA-P1jHYAgxUta7HCaSA0lY6kDFj8ZPPjGgHO0ZfTuoBPEdRmpV-9H97ix2aKtKzEW3kJuK6n55iXnneWM6Yp3s6ulTCrWNqqVwFjcRFdrHv1WgrfTVoJE7ASUntMgsaJjucdZAWd24LP8hNxaqkQEHsA0_zH5TKNrg6AXIel4agWNHpuR2vVfJ3kQT7W437-B-mRxCw_5DTm19hnHUklr3u03hhMdnhIs7MLrmI6NXsfYIb7pG4pp2Iav85oP2LDB2NGD6lTMapZnVxZ1UQthQotCqXuyQoor_zQpeCRL5CM2ZBezyElMWlMq6SmkTNlPkuDQb9i7Ea_A9V78x2t1gRCc_NY4eca3-hgnfolUo38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4066b49a.mp4?token=pfSWkWsQaTx7POFC9C3gXjJhOaIZWNG-Ph13TaBsR3Zz9l0-r2kGqi-B6pSXVy3drnEYTKOc7Hy42dw7GschioDdhux_4pMeFuvQiJHHxK7DWdncYqn3Wv_e8zWNrWJzfieS1JEo0bHPCwzkMvpVOc7CTVeCQtrapogEoPAMXa42ILMyCygotFHYjIZ6RSjEmlpehHK9jLD1C4J6tzPHhlYMPffTCHgtnAFFj6stiG0kpMjT-o5OdBz0Bm0EhO2LCkrjViWpwvc4hCWsC7p7m7naKxs3RO4Ib-8F6VVY6pPJKIzRbh8tvBtq6kjfH2MA-P1jHYAgxUta7HCaSA0lY6kDFj8ZPPjGgHO0ZfTuoBPEdRmpV-9H97ix2aKtKzEW3kJuK6n55iXnneWM6Yp3s6ulTCrWNqqVwFjcRFdrHv1WgrfTVoJE7ASUntMgsaJjucdZAWd24LP8hNxaqkQEHsA0_zH5TKNrg6AXIel4agWNHpuR2vVfJ3kQT7W437-B-mRxCw_5DTm19hnHUklr3u03hhMdnhIs7MLrmI6NXsfYIb7pG4pp2Iav85oP2LDB2NGD6lTMapZnVxZ1UQthQotCqXuyQoor_zQpeCRL5CM2ZBezyElMWlMq6SmkTNlPkuDQb9i7Ea_A9V78x2t1gRCc_NY4eca3-hgnfolUo38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از مراسم حزب‌الله برای رهبر شهید انقلاب در ضاحیه بیروت
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/448444" target="_blank">📅 22:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448442">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275f82336c.mp4?token=bHg0LeXs_venXaWk_MmXCqJlqsHSu6yKRZFF0sjgUJEFQz50pwi8MoDU8maGU6t1WtRvm9q8AJTWXrzldZVVI3tAkpqzQWoMtReRmwsAZVVdtmpgNjbHdr_iTctXF6XFJu34dmHLRN7uCEhUcCqh5Hwv0vw6CLj0Dj-9tcQEGW6udEmeu-9ixdctRh5QfTf7KQr7HFLEJoJZqHvZ8Wo8HALoeT2PPdqBNNsDi1K0rWA8CYCWVtt_zdohiTYbg7Qjs7APQ9A6x2pAtQhoUF186SShrOUNS6FkceT4VSAVWCdFqJa2beU3nEhjIIpGjcjALM54rdkME5xJzn12xnOBiD20jsRAfgzMAy3KVSJFJw1IeBCNa0Z3JcAyP2jiDf1qqh7poA4zzxzFqezKWePJKgxxBMHT0x4hMosfpZiz7AVdGl68gOgDsuTbpeQF1W0k7FA9IV6YRATz733g-4fTVewAAuwOCLGeA2l__StcXfqYxig-72QhqP5ILsQBx3-724ZPwj9m9tRho16kPM47PSR9Ykfe3MacxYLSK05X5fSvaY4FICz_B0IfiHuIMOeMXraU-kcGVyiQB2PDBNq7Gpc7bL1f0jTaPmyCiR7bBMY4b6BY6Prc5o-8o2kuyxc8AFydZ7C2ojq_O_7lmhhMh_37ri3OYtGHaCrw3RGe8YY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275f82336c.mp4?token=bHg0LeXs_venXaWk_MmXCqJlqsHSu6yKRZFF0sjgUJEFQz50pwi8MoDU8maGU6t1WtRvm9q8AJTWXrzldZVVI3tAkpqzQWoMtReRmwsAZVVdtmpgNjbHdr_iTctXF6XFJu34dmHLRN7uCEhUcCqh5Hwv0vw6CLj0Dj-9tcQEGW6udEmeu-9ixdctRh5QfTf7KQr7HFLEJoJZqHvZ8Wo8HALoeT2PPdqBNNsDi1K0rWA8CYCWVtt_zdohiTYbg7Qjs7APQ9A6x2pAtQhoUF186SShrOUNS6FkceT4VSAVWCdFqJa2beU3nEhjIIpGjcjALM54rdkME5xJzn12xnOBiD20jsRAfgzMAy3KVSJFJw1IeBCNa0Z3JcAyP2jiDf1qqh7poA4zzxzFqezKWePJKgxxBMHT0x4hMosfpZiz7AVdGl68gOgDsuTbpeQF1W0k7FA9IV6YRATz733g-4fTVewAAuwOCLGeA2l__StcXfqYxig-72QhqP5ILsQBx3-724ZPwj9m9tRho16kPM47PSR9Ykfe3MacxYLSK05X5fSvaY4FICz_B0IfiHuIMOeMXraU-kcGVyiQB2PDBNq7Gpc7bL1f0jTaPmyCiR7bBMY4b6BY6Prc5o-8o2kuyxc8AFydZ7C2ojq_O_7lmhhMh_37ri3OYtGHaCrw3RGe8YY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از خانهٔ سادهٔ رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448442" target="_blank">📅 22:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448441">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95cccf4d4.mp4?token=E87BxDnaBQyWPZr7--dF-n7O_npO1pUUi0gZgKqCjVEYNgMvd6UfPgVHRulrV-ub0nAhjuZd6cys35U6NlwDTJPtomrFjf8fsFeIqHhOoB_rzYfHG84OQh-jsRpFiy6gJzIQTK9NWt5t5duvDDIPzyh6wqE84CGL3TR2xyOsSCJK_IP9IEYNhW07Mnl1H0CFRiNkoqxSv9NvtMvcwYdNDoDtGohfQ2kXsqJEOiWH4gXLjDYA1zKFu6KxA2NclS-GaxUUcI5bXuD7gqSiwMtJBQILl_5fmUjdTetyzI6m0P0F0w9JaIHDkkRfw8myl5QaNnGk6I3lybthYOGp10iP7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95cccf4d4.mp4?token=E87BxDnaBQyWPZr7--dF-n7O_npO1pUUi0gZgKqCjVEYNgMvd6UfPgVHRulrV-ub0nAhjuZd6cys35U6NlwDTJPtomrFjf8fsFeIqHhOoB_rzYfHG84OQh-jsRpFiy6gJzIQTK9NWt5t5duvDDIPzyh6wqE84CGL3TR2xyOsSCJK_IP9IEYNhW07Mnl1H0CFRiNkoqxSv9NvtMvcwYdNDoDtGohfQ2kXsqJEOiWH4gXLjDYA1zKFu6KxA2NclS-GaxUUcI5bXuD7gqSiwMtJBQILl_5fmUjdTetyzI6m0P0F0w9JaIHDkkRfw8myl5QaNnGk6I3lybthYOGp10iP7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب به عمود ۱۳۲۵ رسید
🔹
کمتر از ۱۳۰ عمود دیگر تا رسیدن پیکر رهبر شهید انقلاب به پایان مسیر مشایه و قرارگرفتن پیکر پاک ایشان در برابر گنبد و بارگاه حضرت ابالفضل العباس(ع) فاصله وجود دارد. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448441" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef4bfc690.mp4?token=KItDmkavIBQ9_rggoh6TEoDU__BzbfmuKLCceHL5DRTvNiY7wGMQM6Y18Guu5AL7Dt0BAuWRvmwzXgJjQhJFAajb48qXYgcSb6KMno7Z9NslCIzFvgCjtmuJ5ywM9h5yePcN-0_iI5rrIui0qf08deFf5mfWTChqTPVFU1ifSSNbDPPyN0hef0DLTY32ZY6wiE0I2T3DccT-gNJCzYWfpjy2TZXqhDrmafnT7v66XyddyZRa7Vousf8HSADbDO80DDPBdGE4x-av-9iyQ4wHnItlu9Mefu9y3R3kLmIzzV1P4nwQUMP1hoUO_ZB9DIsBVCaGJ2Kgj2fWNrDFFIPkgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef4bfc690.mp4?token=KItDmkavIBQ9_rggoh6TEoDU__BzbfmuKLCceHL5DRTvNiY7wGMQM6Y18Guu5AL7Dt0BAuWRvmwzXgJjQhJFAajb48qXYgcSb6KMno7Z9NslCIzFvgCjtmuJ5ywM9h5yePcN-0_iI5rrIui0qf08deFf5mfWTChqTPVFU1ifSSNbDPPyN0hef0DLTY32ZY6wiE0I2T3DccT-gNJCzYWfpjy2TZXqhDrmafnT7v66XyddyZRa7Vousf8HSADbDO80DDPBdGE4x-av-9iyQ4wHnItlu9Mefu9y3R3kLmIzzV1P4nwQUMP1hoUO_ZB9DIsBVCaGJ2Kgj2fWNrDFFIPkgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسیدم کربلا! الحمدلله...
🔹
صحنه‌هایی از ورود خودروی حامل پیکر مطهر رهبر شهید انقلاب به شهر مقدس کربلا. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448440" target="_blank">📅 22:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448438">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940d9f12d4.mp4?token=urnVpgxOV9ga_4D8YeLK_WTlLkqUzKB-wZvrotFZn-j-7t0MxOSoyT63L_CUvDMyBN9nWV3UvRuXDLdUbKRYi9Ak_F0-yZG9DCnO1biswpcUq60-SC71rNFdk6Q7nEc11ve4p0vZaz6NnTbx7vqXWt7qL7J1TbW1nVTfhKfbRb9RAbhGkY_1ul-qzhRQ4zJxM-fc-jxXYhoGPdJm1CZuzaJ3vuHClcTwjBI1l5FGZsWFXeUkX17uBRZiD59VCbr-iy_3YuKHpBiQCYZoLBkvXTSTOX4JgUVJXfNjmt91blkLBrIa5RRO-F7mEiFwURhjFNRCeyJZv4aKjuNm9-7poQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940d9f12d4.mp4?token=urnVpgxOV9ga_4D8YeLK_WTlLkqUzKB-wZvrotFZn-j-7t0MxOSoyT63L_CUvDMyBN9nWV3UvRuXDLdUbKRYi9Ak_F0-yZG9DCnO1biswpcUq60-SC71rNFdk6Q7nEc11ve4p0vZaz6NnTbx7vqXWt7qL7J1TbW1nVTfhKfbRb9RAbhGkY_1ul-qzhRQ4zJxM-fc-jxXYhoGPdJm1CZuzaJ3vuHClcTwjBI1l5FGZsWFXeUkX17uBRZiD59VCbr-iy_3YuKHpBiQCYZoLBkvXTSTOX4JgUVJXfNjmt91blkLBrIa5RRO-F7mEiFwURhjFNRCeyJZv4aKjuNm9-7poQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجلاس ناتو در سایهٔ اعتراضات مردمی هم‌زمان با حضور ترامپ به کار خود پایان داد
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/448438" target="_blank">📅 22:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448437">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46922cfadb.mp4?token=A0WCwrMyZmB_IP5igdY3qDv61X7nXXnu3f6mG1voMagj1zySprlITj1n5iTM0EwrNLl5__zBo8PtYRO9IyfxTlKEnP7JfH0Yw8ltsaexekllxyi23EtLYUg3Afihq6VGV64ylAntla3geRCdT81DSkgsboUNpkPGnjvgIaDBFhj61z7tslEewuyfaJXC6NKtrkthPXwtTNZKyUJFJN50XfOi4La7XVhyvZ9Vu0QYLWaSW8QOBjp3vyf-7IJxqy_l3lC36E0KHrLCSc413aKx7ze6aHhY528zmB9O9D5zHS_Qw2DnZ0AXJHSAyoczVEPPWglsnmFosey926_zxDQ31g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46922cfadb.mp4?token=A0WCwrMyZmB_IP5igdY3qDv61X7nXXnu3f6mG1voMagj1zySprlITj1n5iTM0EwrNLl5__zBo8PtYRO9IyfxTlKEnP7JfH0Yw8ltsaexekllxyi23EtLYUg3Afihq6VGV64ylAntla3geRCdT81DSkgsboUNpkPGnjvgIaDBFhj61z7tslEewuyfaJXC6NKtrkthPXwtTNZKyUJFJN50XfOi4La7XVhyvZ9Vu0QYLWaSW8QOBjp3vyf-7IJxqy_l3lC36E0KHrLCSc413aKx7ze6aHhY528zmB9O9D5zHS_Qw2DnZ0AXJHSAyoczVEPPWglsnmFosey926_zxDQ31g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع رهبر شهید، نگاه رسانه‌های جهان را خیره کرد
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448437" target="_blank">📅 21:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448436">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1d1b87ab.mp4?token=dSZoDUEG7lGiSOjqiU7fHvXnHOqCRVT7tpLVD6iKcKxHDr5VJp7waiJoJYr1ctNDvNtZBaCyG1twJsNqzH-0hFxg6GYoHY3Zoy5CE0JDJi8xxmuw6ZyuFGK31j6iMJY99Nts1_oAGtC_w6hULhnigs2SPgQ2WJ3sRhGJgdFa0Dy7mWd11z2f1j7udpU3gG0GO2g3dakE4BT74cp6BYuNA2CdYiV_jIxsvngfl6z9BH_l9iF6p7dZGv8H8Qg6S5NAGfjqftLsA-bjbEyoZJowefZEPacUQbaKzoydXfeudvn9rfXh_-n8jNdPhZ_ZEr9CsuRcm50SK-0beXtbbwB3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1d1b87ab.mp4?token=dSZoDUEG7lGiSOjqiU7fHvXnHOqCRVT7tpLVD6iKcKxHDr5VJp7waiJoJYr1ctNDvNtZBaCyG1twJsNqzH-0hFxg6GYoHY3Zoy5CE0JDJi8xxmuw6ZyuFGK31j6iMJY99Nts1_oAGtC_w6hULhnigs2SPgQ2WJ3sRhGJgdFa0Dy7mWd11z2f1j7udpU3gG0GO2g3dakE4BT74cp6BYuNA2CdYiV_jIxsvngfl6z9BH_l9iF6p7dZGv8H8Qg6S5NAGfjqftLsA-bjbEyoZJowefZEPacUQbaKzoydXfeudvn9rfXh_-n8jNdPhZ_ZEr9CsuRcm50SK-0beXtbbwB3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انبوه مردم مشهد از حالا به استقبال مراسم تشییع فردا در حرم رضوی می‌روند
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448436" target="_blank">📅 21:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448435">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr4Y7iTJV2meQB2uZKgnRo_YVgGPtAYD62pFDEGxtF54_q3UlWuKBwefuxCMDDYKUePx3SfcADEuEADftg4_Te4R6TfEP2A-tPAV5VlKA8Gdao-d7lMGwib0_ax-dJPQUuw1ulo3sXzVIzRhMgH8NXwdOkdhJJrvdUvOYeG_se-Fj2Sgk2kTja85vJyUKaw_Aie5uoew9XexBiU6d3dHoUPCX4dFquFlZuJQNuEge5sENCGPUrY0BjjZ-bLlCfCVi8QsasS8osez7zFd0l4thO1GQ_gjkeEn9njErEKP7mX3UEc_RmALU_1qNn_-c49zzXyQ9Gc-g9pwVMNT1wo8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رسیدم کربلا! الحمدلله...
🔹
صحنه‌هایی از ورود خودروی حامل پیکر مطهر رهبر شهید انقلاب به شهر مقدس کربلا. @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448435" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448433">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e769369d0e.mp4?token=vvv0IklxKPmjbyzl5Z8FmXdIx_zeauRPDPCfyIcwnpvEVqq_Db71gMLULv7ALcaajO_om9SZM09aPiyQ3N3tLImSp6cctK2RjFqU-o9Qfwu-TxyJnn7QpqOzWkRYrL-nNx_Xsr5DPwJ7M_sJ53buXa6MZuLzDQYwLph-d3fbWNeTTvhSQnLuFK50d1SsjEzAoYr1zcnPR16y2Bo8ukuMWljExvrAw64MBz9_RNgO86KnIDUr-rDRvwPxvGpekozxaAJoxjE6RPt7g7wnKITa3aFAz9GrCVLW69KtznfY7UgQBLYC0UmfoAIUfQzuspjYrsD8APCOCPRnpkKovedybjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e769369d0e.mp4?token=vvv0IklxKPmjbyzl5Z8FmXdIx_zeauRPDPCfyIcwnpvEVqq_Db71gMLULv7ALcaajO_om9SZM09aPiyQ3N3tLImSp6cctK2RjFqU-o9Qfwu-TxyJnn7QpqOzWkRYrL-nNx_Xsr5DPwJ7M_sJ53buXa6MZuLzDQYwLph-d3fbWNeTTvhSQnLuFK50d1SsjEzAoYr1zcnPR16y2Bo8ukuMWljExvrAw64MBz9_RNgO86KnIDUr-rDRvwPxvGpekozxaAJoxjE6RPt7g7wnKITa3aFAz9GrCVLW69KtznfY7UgQBLYC0UmfoAIUfQzuspjYrsD8APCOCPRnpkKovedybjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بار دیگر خادم حضرت خورشید به‌حرم امام رضا(ع) باز می‌گردد
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448433" target="_blank">📅 21:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448432">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7649652333.mp4?token=H3vSkaIsAEqyc_ehlQ8ulR-IsHA0Lw0g3REWBoETQ3HrgYFSly0pe8eDqa59htgWEafSVqIQdby5Zq9JWEU9udI2KzKwpxURolwSh93nkyk29NTUpm773vh7X9eqcR0fsHL8xffWSHVNmbima_jk0U7iD4P4ZnITXxktBEsWy9RI16uhhbcD0LR86HbmvgEK23v42hkIyr5D55WHNIYkVC0IGkVrYVVrj4YX9ZuTP7GBQF1QhiCsurS6PEHIiEhX9F6dmMHAUMsiiRO1ZReTqf96p-oBXWg4pHNGfdTBsNhCqC4NJb0qOoiNDPrMrGocthl0PIjgnUM_UAhbCcLkBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7649652333.mp4?token=H3vSkaIsAEqyc_ehlQ8ulR-IsHA0Lw0g3REWBoETQ3HrgYFSly0pe8eDqa59htgWEafSVqIQdby5Zq9JWEU9udI2KzKwpxURolwSh93nkyk29NTUpm773vh7X9eqcR0fsHL8xffWSHVNmbima_jk0U7iD4P4ZnITXxktBEsWy9RI16uhhbcD0LR86HbmvgEK23v42hkIyr5D55WHNIYkVC0IGkVrYVVrj4YX9ZuTP7GBQF1QhiCsurS6PEHIiEhX9F6dmMHAUMsiiRO1ZReTqf96p-oBXWg4pHNGfdTBsNhCqC4NJb0qOoiNDPrMrGocthl0PIjgnUM_UAhbCcLkBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اَلسَّلامُ عَلَیْکَ یا اَباعَبْدِاللهِ وَعَلَی الْاَرْواحِ الَّتی حَلَّتْ بِفِنائِکَ
🔹
پیکر رهبر شهید گلگون‌کفن به کربلای اربابش رسید. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/448432" target="_blank">📅 21:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448431">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4dd4f34e.mp4?token=rjFxqYvcQppQ7E8PcSUVrwSyv8t_ce974RaULAZ2UrATbo-ZwNdPws3GB5ZcvW0ol_FKIoTYzJBX8RaQztRbM8EwK_ZR4WEQgeXD4eiyM_3_AftLZ9dJ4bZ7D00kSzVgdcCd1w7fjaw60nSngkTxEquMCVZBjCv4CWJDtvM2CeGXG1awZacsFzgX88B9yaWzr9Z9e9N7NmnGaOGi7R-X3eiIA6LZ2xr7QLcl2E_XdsS6_R6BZ9r0w9Rw8fksl3wMIEUbSNIhrUBlrqn7jzqxPQ9hmpRAGfRUGvqNBjgTWhMXVeRExM01iMLKvpSyge0zv9qOKnBsCMxsVI2VblHSag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4dd4f34e.mp4?token=rjFxqYvcQppQ7E8PcSUVrwSyv8t_ce974RaULAZ2UrATbo-ZwNdPws3GB5ZcvW0ol_FKIoTYzJBX8RaQztRbM8EwK_ZR4WEQgeXD4eiyM_3_AftLZ9dJ4bZ7D00kSzVgdcCd1w7fjaw60nSngkTxEquMCVZBjCv4CWJDtvM2CeGXG1awZacsFzgX88B9yaWzr9Z9e9N7NmnGaOGi7R-X3eiIA6LZ2xr7QLcl2E_XdsS6_R6BZ9r0w9Rw8fksl3wMIEUbSNIhrUBlrqn7jzqxPQ9hmpRAGfRUGvqNBjgTWhMXVeRExM01iMLKvpSyge0zv9qOKnBsCMxsVI2VblHSag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از ساعت ۲۲ امشب، محدودیت‌های تردد در خیابان‌های اطراف حرم مطهر رضوی اعمال می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/448431" target="_blank">📅 21:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448430">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad13f17f9.mp4?token=p_h3Zou-ebJrP-LlW2aq5od8HqGTgDBY2E4nFr0TZ278HuXBtZhVPIceNOaavwjrWAGSQn-BgWFeE2EnjkGTCiFKV3AYfVtIPGXl-bgHv5UgmmdT8ISx_ViGwMv8RQXxN30TkXggmQzBDQeRrK3k45sxZ6MJjoWH-NW0QunLfoUAxlml1EzT-pJ41EyTE-Q4sWKTitaltOzlgg8MKKNnSCRTABgEjp9RsVHUnqTkkYE4ZWo_ZRAsU7iwcAQnfFr5K_IgmZpo_4MlVKzDuvw-FheFYZ_g5re--pITQFajXD--FPC886BnD6gNKTgGTb6IC9-OUOARfaZbMeZsn9MevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad13f17f9.mp4?token=p_h3Zou-ebJrP-LlW2aq5od8HqGTgDBY2E4nFr0TZ278HuXBtZhVPIceNOaavwjrWAGSQn-BgWFeE2EnjkGTCiFKV3AYfVtIPGXl-bgHv5UgmmdT8ISx_ViGwMv8RQXxN30TkXggmQzBDQeRrK3k45sxZ6MJjoWH-NW0QunLfoUAxlml1EzT-pJ41EyTE-Q4sWKTitaltOzlgg8MKKNnSCRTABgEjp9RsVHUnqTkkYE4ZWo_ZRAsU7iwcAQnfFr5K_IgmZpo_4MlVKzDuvw-FheFYZ_g5re--pITQFajXD--FPC886BnD6gNKTgGTb6IC9-OUOARfaZbMeZsn9MevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانشین رئیس پلیس راهور: محورهای ورودی به شهر مشهد با ترافیک سنگین مواجه است و پیش‌بینی می‌شود تا ساعاتی دیگر بر حجم ترافیک افزوده شود
🔹
برای هر خودرویی که وارد شهر مشهد شود، پیامکی حاوی آدرس پارکینگ تعیین‌شده ارسال خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448430" target="_blank">📅 21:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448429">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvIcrNcbv-MRtcYC4qIFOEiYQjNCiUIWtXeZxG8Vq9zHuMlN30G8rZIBD-zf0Cc1ZBZ_ttqjKIj49EgdPu98xFKm5P8FDQXhcGUOQKApW5iqwIQm-hdE5E1sHQK_8QFNZtiCEnKgRQKUtF8Ze2fhQMvcQeA5sfx3B51QJ9sPDzzwn575s-9qT-19Hy7dNECWJH4YyqWqIIQeeJOwat0ewKpfUOlEdTz0P9IetC6ehMKrsyObzt5_ftbfwXm0DQk_ZvnG2cM-kY8N79E8XSOdWn82h27iCoAH6_yO42h-qIHsp-dAfo3qMu6jpVgti43AHoeojk4KZpRNBuf_rklvkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دبیرکل گردان‌های سیدالشهدای عراق  در حرم مطهر حسینی در انتظار پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448429" target="_blank">📅 21:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448428">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d868a35f7.mp4?token=UmTtRqyzU2dhrjP3sDUCI4xCyecBxfwCrimdGUtc15-6_H4Be895rfYhiyB_BDpvM1y_79AvinhYbuXZh4u5aSZ5PPEiAyoYaYdNQhRlxhJa9tFu9GpiNn50Mc4pOgqL0oLt84-caSrvqPog152U-qalJBpiEUid7yXsBz4pDwlBVPcAk75wnpW78yzUKoGE8AB4Sqk7Qz-8UvfkoW4nTLP0xsxoeo-wvdZQnD7vvX9kWKEQPNNDl3lr_1wrr27-Jyr-SluF1PbsjyGAP21zNA-17v7xoeAhOkOnAuU1-j-U31MjGgGI25fQNIRxpo95JfmHtgzaZVQ3QR-XTsVY-4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d868a35f7.mp4?token=UmTtRqyzU2dhrjP3sDUCI4xCyecBxfwCrimdGUtc15-6_H4Be895rfYhiyB_BDpvM1y_79AvinhYbuXZh4u5aSZ5PPEiAyoYaYdNQhRlxhJa9tFu9GpiNn50Mc4pOgqL0oLt84-caSrvqPog152U-qalJBpiEUid7yXsBz4pDwlBVPcAk75wnpW78yzUKoGE8AB4Sqk7Qz-8UvfkoW4nTLP0xsxoeo-wvdZQnD7vvX9kWKEQPNNDl3lr_1wrr27-Jyr-SluF1PbsjyGAP21zNA-17v7xoeAhOkOnAuU1-j-U31MjGgGI25fQNIRxpo95JfmHtgzaZVQ3QR-XTsVY-4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اَلسَّلامُ عَلَیْکَ یا اَباعَبْدِاللهِ وَعَلَی الْاَرْواحِ الَّتی حَلَّتْ بِفِنائِکَ
🔹
پیکر رهبر شهید گلگون‌کفن به کربلای اربابش رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448428" target="_blank">📅 21:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448427">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbf4c36af.mp4?token=QXkx-NG5pe9pCCokckf4J3B26Mh3oXOpqhBtH7ekovPlxePxcIV-WIr3h8KpLkXitFTeQD13eGM6xsO5SDNv29mn1v0vcjRdxHPUzt_JcwVI-k5ofhi41BSNZyiaUdpTsWI3vKetb1Wp9janylbFioxtxGgp-Dm0GVU-Gg4_gqJZKUrOMdbWFQfoPkG_D7FtnJFqxPHrE_Fd4qS6B361Fsfk2iSREO-dg1w45h7wbPPbC5Lv8zvs1K0qhzTsCkx6hHjRa78Zasr7TpYcaum4RL8Q9gMmFrI5xaF43tbcTT_C57M254pauJiMzH4ND6UIx8wYsOvLwDAc6-hhSoEN0gngLE0ufAqpmCld-Z0mPVwqpGYQPDPNq66dW5p5ZQtYiuFQI0kbM4eRwXZSVtPHOAMaQ-hN22WNpAUTCA3X1f2CNFsk8ml6MOzvjGC2i4VB6I-U81nzr7kcWAcsh1otA8vUiAq2U1W0uoYd2oCKPPhXYFT7jo3M_ZWj1MD7Xx08Dj1ypWwow2cG2javI2IAFANuRuwAysfxCelr-k2cAn5I7EAKWppmOL7-NSmrPaNJcBun73ONvP0mCyPP-0-IW_7C3SIRcYva37LeC4iZmc640j7Sq72lql8mcNy4YZcKpCzWtNhtMFmUEp_sSD7kAZhFKFfNnOWlJyelMIqFbps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbf4c36af.mp4?token=QXkx-NG5pe9pCCokckf4J3B26Mh3oXOpqhBtH7ekovPlxePxcIV-WIr3h8KpLkXitFTeQD13eGM6xsO5SDNv29mn1v0vcjRdxHPUzt_JcwVI-k5ofhi41BSNZyiaUdpTsWI3vKetb1Wp9janylbFioxtxGgp-Dm0GVU-Gg4_gqJZKUrOMdbWFQfoPkG_D7FtnJFqxPHrE_Fd4qS6B361Fsfk2iSREO-dg1w45h7wbPPbC5Lv8zvs1K0qhzTsCkx6hHjRa78Zasr7TpYcaum4RL8Q9gMmFrI5xaF43tbcTT_C57M254pauJiMzH4ND6UIx8wYsOvLwDAc6-hhSoEN0gngLE0ufAqpmCld-Z0mPVwqpGYQPDPNq66dW5p5ZQtYiuFQI0kbM4eRwXZSVtPHOAMaQ-hN22WNpAUTCA3X1f2CNFsk8ml6MOzvjGC2i4VB6I-U81nzr7kcWAcsh1otA8vUiAq2U1W0uoYd2oCKPPhXYFT7jo3M_ZWj1MD7Xx08Dj1ypWwow2cG2javI2IAFANuRuwAysfxCelr-k2cAn5I7EAKWppmOL7-NSmrPaNJcBun73ONvP0mCyPP-0-IW_7C3SIRcYva37LeC4iZmc640j7Sq72lql8mcNy4YZcKpCzWtNhtMFmUEp_sSD7kAZhFKFfNnOWlJyelMIqFbps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیام ملت عراق در بدرقهٔ امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448427" target="_blank">📅 21:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448426">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c627a93b.mp4?token=dMPoa_9k_ntnJdoW-UuWWuP9PwTQg_Mb4nT0uddbmUbPxLAL0hxCUV6jWQ0fawDxpIttnTxOgsXTej0ezp3eND7GJ1ldv3ShyMK9SowzpseEq61e6tnowFfhLLdN_WiY7_zwm0kx92zJHhJXN794TvRGXSfwOJy9OTl5ckw904znkuf6TooERpb2qyJXFztzAVXAZ_0l683RIyKv1Tls0dRAzuBi7KeX-Tuabpx2r8YRO9AoxVrQ29rf8h1FC7wBrf1juT3DYR2NPxpugztPJYp_8QnlG7j4QUNJ_LRi_vgZ6MSxxBZtqs2TRBmIebH0bShnKKnUAJ3Q2tVEo_eONw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c627a93b.mp4?token=dMPoa_9k_ntnJdoW-UuWWuP9PwTQg_Mb4nT0uddbmUbPxLAL0hxCUV6jWQ0fawDxpIttnTxOgsXTej0ezp3eND7GJ1ldv3ShyMK9SowzpseEq61e6tnowFfhLLdN_WiY7_zwm0kx92zJHhJXN794TvRGXSfwOJy9OTl5ckw904znkuf6TooERpb2qyJXFztzAVXAZ_0l683RIyKv1Tls0dRAzuBi7KeX-Tuabpx2r8YRO9AoxVrQ29rf8h1FC7wBrf1juT3DYR2NPxpugztPJYp_8QnlG7j4QUNJ_LRi_vgZ6MSxxBZtqs2TRBmIebH0bShnKKnUAJ3Q2tVEo_eONw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید تنها ۲ کیلومتر تا بین‌الحرمین فاصله دارد
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448426" target="_blank">📅 21:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448425">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d210620e72.mp4?token=he8LUTNhyOrnzQFWnaoCK6LENMQ5mV7dtBQBberMlS-q-lQwZs33eWaARTU0t22oZswJ6T7qVU5JIQ323u2xyfYj5xEqegrLmfBjuMYBGTQR-hJ20DB1zORO1yVV93NL7VK0QjYaerkmY0Cn9MSdFLY6b8x7Cid3mxzsCNiXHkhpEprRRDqyeFrqqg5h7YFUyuarnwOoNmxPruDe69juWjoz8oGXWsRTagODjiSNy_5lx5_vy5Tr0SrS3IioCI_YHfF41sfcZmxfbITj0EehkPxFv34rfuf9q8NcipSeJqOarIUyVDcSXwUW_9ACmwYotiDDneTWP-jsq4ciGem-vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d210620e72.mp4?token=he8LUTNhyOrnzQFWnaoCK6LENMQ5mV7dtBQBberMlS-q-lQwZs33eWaARTU0t22oZswJ6T7qVU5JIQ323u2xyfYj5xEqegrLmfBjuMYBGTQR-hJ20DB1zORO1yVV93NL7VK0QjYaerkmY0Cn9MSdFLY6b8x7Cid3mxzsCNiXHkhpEprRRDqyeFrqqg5h7YFUyuarnwOoNmxPruDe69juWjoz8oGXWsRTagODjiSNy_5lx5_vy5Tr0SrS3IioCI_YHfF41sfcZmxfbITj0EehkPxFv34rfuf9q8NcipSeJqOarIUyVDcSXwUW_9ACmwYotiDDneTWP-jsq4ciGem-vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجف دریا شد؛ عاشقان رهبر شهید موج زدند
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/448425" target="_blank">📅 21:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448423">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیکر پاک رهبر شهید انقلاب به عمود ۱۲۷۹ رسید
🔹
مسیر نجف به کربلا ۱۴۵۲ عمود دارد. @FarsNewsInt</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448423" target="_blank">📅 20:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448421">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLIKouxfJVzFmOhCiBKnjr7UB-hrfuCCHPmPBd7dOMxajTvfFPP_mz2LZtLNhrxfHnXNsTAZic7S41ZZuL7CS_apg2npcAgF40a8miQk9fkHWQUQUef39l-vrUGmn1bQo3AXF2CmfZ014u1WRl0FGQHcgryd-cnEY9yeun17E0A0NFMZsO-uvJupQaNVQe74QpwEkI9lxZ9mzHJu25IF1R3uScCDAvNpkejgXKIIb1GNyjJsy6xDlKzUr2vv8laUxvxzAH9zITVCXrIE7GRE2GBSw3bCGWhqk-zrUJ-eCCgKNDmRYxpEEXnlYRV1rTaohWm4x5PW7adlYZ1UY1Ixiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: ما بی‌ادبی ترامپ را در عمل پاسخ می‌دهیم
🔹
خطاب قرار دادن ملت متمدن و شجاع ایران با زبان تحقیرآمیز، از عظمت آن نمی‌کاهد.
🔹
ایرانیان به‌خاطر تمدن، فرهنگ و ارزش‌های اخلاقی قوی خود شناخته شده‌اند.
🔹
ما ابتذال را با ابتذال پاسخ نمی‌دهیم، بلکه با عمل پاسخ می‌دهیم: بی‌باکانه و با شجاعت فراوان.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448421" target="_blank">📅 20:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448420">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFzKbLwiW8RoehnAgoB2OTmgcAFZo617WDVULFXh2f31d9IF86A2Dj3HElxdtm9tobIZIEdnj47JP6lpJarJ5pExVmmDBs3AHg2s_GNn6X3NFZsERKzaHzpj3q481cnidAV04CGod7rc9aao9uzG1mzYsFUjSJggDtpLH-Jx-Xahrn2f3htfglJ7WF89QKON4AB8KMciSIRcjw8Dy66IRDAhNs4YHIRi47ilqIRVbs1cLBDuou9lXUCNincy0c1Qx01ZEsP4k9H0N9owKf6wAmiDoY6gULlZBcwq7gCGeujeijFBgH_Y16ZVLif58fLYFvQVO8XMChBqR8iuyrA8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور سردار قاآنی در نماز مغرب و عشای حرم امام حسین(ع
)
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448420" target="_blank">📅 20:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448419">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12cc54c351.mp4?token=qIawvgN92wlzmRJ1zlQ0dqCesEndvEQMJxapbZBPewaj20k9Vhbtz53mqmFg6lGPM0n79G-5VI1-IXqOXF0IycuPsYFm05HU9swN39rZn7AVvrSK1abL5LtwkS61h8VsGx_Yw_Naq7-XU5fNoRoxZQJvyWFK6am1cbLM_ewrbZW_32P07Ze7P4PG9YzFLdac8dSA_-kPoIgfjtQJWISs9QHgguZ_OXREWT9VxbYkyb3YXTspz04jWXrJpGWqF14-eLwYgPpfzT0pvFJRdARfInbwStpAJE5FYv_FcRgpj8ULdlecJG70O7O81siAFwNQiytgUmUmINCruNSa0akHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12cc54c351.mp4?token=qIawvgN92wlzmRJ1zlQ0dqCesEndvEQMJxapbZBPewaj20k9Vhbtz53mqmFg6lGPM0n79G-5VI1-IXqOXF0IycuPsYFm05HU9swN39rZn7AVvrSK1abL5LtwkS61h8VsGx_Yw_Naq7-XU5fNoRoxZQJvyWFK6am1cbLM_ewrbZW_32P07Ze7P4PG9YzFLdac8dSA_-kPoIgfjtQJWISs9QHgguZ_OXREWT9VxbYkyb3YXTspz04jWXrJpGWqF14-eLwYgPpfzT0pvFJRdARfInbwStpAJE5FYv_FcRgpj8ULdlecJG70O7O81siAFwNQiytgUmUmINCruNSa0akHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: من هدف شماره یک ایران هستم.  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448419" target="_blank">📅 20:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448418">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb3c01c6a7.mp4?token=EDl3Emxpj682fKQhxnCcvsnjfUhdj8slGljJwr8mx_V7ds-SAF7LIRsdi9O69HbWi0Z5-VpAUVS7IATurBVzroNQEeQZDW1fIEbRXhUrbz_0tqQRERZ3x1gj0qADDe9_VDQFpWQ4ZTau0SvCOx19q_Z0CEEPlvHhfkWS7xt6_k2Jg0G0t_9u_6Fm7cq2NYmB5BQWeSls9ClJzayYIGgS6RZjD4-wwH_naRDq4hR6H3h1lCWWjScrsPcEY577JEQU10RgBev3u6IUuYKzYbIX41U635GZrs8Yne9VUzrD7Gmb5QgoFy_m7z4HZNkF6Lfoe6gN1MdgbG3KMiAotwGjxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb3c01c6a7.mp4?token=EDl3Emxpj682fKQhxnCcvsnjfUhdj8slGljJwr8mx_V7ds-SAF7LIRsdi9O69HbWi0Z5-VpAUVS7IATurBVzroNQEeQZDW1fIEbRXhUrbz_0tqQRERZ3x1gj0qADDe9_VDQFpWQ4ZTau0SvCOx19q_Z0CEEPlvHhfkWS7xt6_k2Jg0G0t_9u_6Fm7cq2NYmB5BQWeSls9ClJzayYIGgS6RZjD4-wwH_naRDq4hR6H3h1lCWWjScrsPcEY577JEQU10RgBev3u6IUuYKzYbIX41U635GZrs8Yne9VUzrD7Gmb5QgoFy_m7z4HZNkF6Lfoe6gN1MdgbG3KMiAotwGjxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۴۸ ساعت گذشته در تنگه چه خبر بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448418" target="_blank">📅 20:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448417">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ae0700d.mp4?token=YdDvF3rgColjB3uKOR8uOEXiGmozNIAh7MuhkBACt9zEUK6zgQNUw9mBbYzqWiXgiqy9v0bh89-Rplo1O0f9Qu4kn31loKYTNipB6kZElcF--0uH_36JO4MFgL44Rn7kPqfgTzu_fGFoE0vD4rp21BVtSYm35DMOmnd9VmizSvs1dbq3HANLpm5SVik7nFGHAGT4Z1P3n9knkzSOJlhZc8bq-XFqMESQ0AbJmfPox5gg5TJ8y3VXkJ6BLDRafsBlPLjr3fKvXjyoiWLqOq1VJqhHuBmuWpPQPY5e_hwYrit3PJJ_Y-k_l38ZsGHf_w3rFfQbAz0dZcqytiAR4kY9QoFyAlCax2KnvtGxcik0Ii2qC19uWm5Pf_KdLl-Q1SYSRYoYq259SioIP1P91zyxdXCpHvi24izNiZYw8dYr5w6KlUpjCHcjcgN_40j_7_Fr59rL4OZ3x8pvPCmIfj3cPkpjlQO5nlyckNQicKJqkNN9cpoYCyt2WJop7UVdl2t4fdvUwS4Lhf1D36i3T7zQiLn612tijMYtckiS08q2P9ymEf9CuepRobgJOxIW1ZNXuPA9nsTZ_WzR5Oz9WRV0ohiCSqb1z9Mv9OrlbO07mdnx74H-dNVbXWjUAbir0YZ16qyCJwHTDm1zrzqTaKcFpUcYnoi3Kq4tbAUeplj-1zU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ae0700d.mp4?token=YdDvF3rgColjB3uKOR8uOEXiGmozNIAh7MuhkBACt9zEUK6zgQNUw9mBbYzqWiXgiqy9v0bh89-Rplo1O0f9Qu4kn31loKYTNipB6kZElcF--0uH_36JO4MFgL44Rn7kPqfgTzu_fGFoE0vD4rp21BVtSYm35DMOmnd9VmizSvs1dbq3HANLpm5SVik7nFGHAGT4Z1P3n9knkzSOJlhZc8bq-XFqMESQ0AbJmfPox5gg5TJ8y3VXkJ6BLDRafsBlPLjr3fKvXjyoiWLqOq1VJqhHuBmuWpPQPY5e_hwYrit3PJJ_Y-k_l38ZsGHf_w3rFfQbAz0dZcqytiAR4kY9QoFyAlCax2KnvtGxcik0Ii2qC19uWm5Pf_KdLl-Q1SYSRYoYq259SioIP1P91zyxdXCpHvi24izNiZYw8dYr5w6KlUpjCHcjcgN_40j_7_Fr59rL4OZ3x8pvPCmIfj3cPkpjlQO5nlyckNQicKJqkNN9cpoYCyt2WJop7UVdl2t4fdvUwS4Lhf1D36i3T7zQiLn612tijMYtckiS08q2P9ymEf9CuepRobgJOxIW1ZNXuPA9nsTZ_WzR5Oz9WRV0ohiCSqb1z9Mv9OrlbO07mdnx74H-dNVbXWjUAbir0YZ16qyCJwHTDm1zrzqTaKcFpUcYnoi3Kq4tbAUeplj-1zU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای اربعینی امروز نجف
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448417" target="_blank">📅 20:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448415">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXYy3WE5i_P7rlc06O5QgHajNsRfbYg4jcjQPHCMMVDLQGumgfObccecqrgUrW945qR7VbwUrKxCfjLsHIE18C8dwUR3C3YSY6aqN-oJ85jGqAZd_uZr_oIxQoDv0DXE2yWhjZh3-7J7G-Egtm9SLDoS1JnEKsm-DNE86S4wJhfFLXs6C-CTNWSaUqwY-O2HFZlbCRhIWCkiNBQ1F0xyHag_ueXaTibCYXEmFVEVFK4cz7nTL8B7zFag9Zcg9R1ptQcdPEKwS-x0k6-TzdJ2wQ0L310ocdui-zn05gBEZIunTMdbGbQSkJDwZAml-NmX9UQVbt15qGuq3OmrIew9-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی کمیسیون امنیت ملی مجلس: حملۀ مجدد آمریکا با تغییر دکترین هسته‌ای پاسخ داده می‌شود
🔹
در رویارویی آینده، دشمن با تهاجمی همه‌جانبه و غافلگیرانه از سوی جمهوری اسلامی ایران مواجه خواهد شد.
🔹
گزینه‌های زیادی در اختیار داریم که حتی در جنگ ۴۰ روزه نیز از…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448415" target="_blank">📅 20:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448414">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43d50ac539.mp4?token=pxzWeSH3dpeAQzbweno0irhNhFbFw4eC4ym6jh0wdm9MTzi3584NxQo7P6zB3qT6JSUM6Ybdu_PK1TcJ9y9dNVzEv3ZEYxKF1oSYasfOXeDk8wfJ-JDN9qQprMJhP-7P-MZvrQlE1loGebSisZgBhsgaq3WVxikgKMu-sYMb907e_zniY6rejw7BwMoozR1vmEpFAzx_YhAUekxZfQ65mWDcBHswvPOPAOMJjXgGUHcbJGiS4raIbZcwpMSInK1Sv4rjWiSienok6r0A1DohNDZQ8SN4aVUcYE794M0qy243zsvMMEohCavd49do0Fzl6nhwyvxMViLJT9bSfhZ1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43d50ac539.mp4?token=pxzWeSH3dpeAQzbweno0irhNhFbFw4eC4ym6jh0wdm9MTzi3584NxQo7P6zB3qT6JSUM6Ybdu_PK1TcJ9y9dNVzEv3ZEYxKF1oSYasfOXeDk8wfJ-JDN9qQprMJhP-7P-MZvrQlE1loGebSisZgBhsgaq3WVxikgKMu-sYMb907e_zniY6rejw7BwMoozR1vmEpFAzx_YhAUekxZfQ65mWDcBHswvPOPAOMJjXgGUHcbJGiS4raIbZcwpMSInK1Sv4rjWiSienok6r0A1DohNDZQ8SN4aVUcYE794M0qy243zsvMMEohCavd49do0Fzl6nhwyvxMViLJT9bSfhZ1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمود کریمی دوان‌دوان درپی ماشین تشییع پیکر رهبر در عراق
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448414" target="_blank">📅 20:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448413">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
منبع آگاه به پرس‌تی‌وی: در صورت تجاوز مجدد، تنگه هرمز کاملاً بسته می‌شود و ایران  ۲ برابر تجاوزات دشمن را هدف قرار خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448413" target="_blank">📅 20:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448412">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d591c088b.mp4?token=pjc45IZL9oUBIH9fXQiOzpMTz911Mvj0rqxbv8_USnObOqirD_PGhcW9zOP-QElg5xJ0Bv87ZdbTaZs0ZIj7eEskduw1kIVsnBV7OIvXYv5yPAMq5sf6YEjsrOyB4m-zUEIY72OiDA5E7j9TRHCqwIeImDgiH3zl3ZG77pE5gM7pUq8tPgjdGOxqpvhRSMVC2AnaNc1_p9MZUyfby9Dx71WBV9OSmTx_cgqcxJStbjS9m1A8HzV9tzuaRvaJf87VwbBssUKVYi2qxlyt-w68QvyvgRk2RStAJQqpV7YpcxgWpYzDZSVc2NOeTYHj1h9rooze_W35ZwU3WHsfa6_6Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d591c088b.mp4?token=pjc45IZL9oUBIH9fXQiOzpMTz911Mvj0rqxbv8_USnObOqirD_PGhcW9zOP-QElg5xJ0Bv87ZdbTaZs0ZIj7eEskduw1kIVsnBV7OIvXYv5yPAMq5sf6YEjsrOyB4m-zUEIY72OiDA5E7j9TRHCqwIeImDgiH3zl3ZG77pE5gM7pUq8tPgjdGOxqpvhRSMVC2AnaNc1_p9MZUyfby9Dx71WBV9OSmTx_cgqcxJStbjS9m1A8HzV9tzuaRvaJf87VwbBssUKVYi2qxlyt-w68QvyvgRk2RStAJQqpV7YpcxgWpYzDZSVc2NOeTYHj1h9rooze_W35ZwU3WHsfa6_6Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غروب دلگیر کربلا در روز تشییع رهبر شیعیان جهان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448412" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448411">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
ترامپ: من هدف شماره یک ایران هستم.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448411" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448410">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-CAfkfgYU7FuSysYKOjrqusjrbyh3m-4b4WzM8P-BaFU6abvCex0V6c1WTHLw1d7Pv_O4FLdDS0CsM1Ncye1ueMvUPx1hpqP9cSdBrPHEyy28tgDfLe0L6ZtrP686xvypXQNEF7itrupeomU760sCEPgh1YHwnFbg61n3TM5LZpML0KCioN7ji3R08rzD_CZp74_sR_4j7ilC-k6YGHZVoW6HPEW0asYflaOdJKPQihUrMovK3zhf1swJ2c-_-bfEsMtgivTed-7Lrd1-2pRuR1Bp1ZaxwC3VDh7LEM9Fy1RWLdB6sA-x8VIHJu4WLxWMCN0CGNUxfaj-RywVvG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر پاک رهبر شهید انقلاب به عمود ۱۲۷۹ رسید
🔹
مسیر نجف به کربلا ۱۴۵۲ عمود دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448410" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448409">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc350b6bdd.mp4?token=SzCIrPacYY7zSBRycRzME_5ggq4KJhQqRW8C780KoCAHKcth06nY_rj75mb9TIj_PIXd33zgEKj5sM3I52QhoBe_v5KJS-QPFISRDQmMWHbBfFFH4ACmJVZcY5H8_OFg_XIYTn55SaXjVgQtvlG2vIuHb0UWtTsYGZ_RbbqA9i2fsx6-g6j2Eer-0rj9wszeLuWGEtZJyvQQSz7U52T4mi_QAw6n_-i9EwevVdaxeMQ98kchK9U2XZWqS8l2t-ScRyWEP1Y90eOyNxfP0ZVnmfysxZJuqBOCFV-MeUkv0u5Ykiyda2Ij2mssF8J-4gKAU0ViBUoOvAcdBZZjU9ouVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc350b6bdd.mp4?token=SzCIrPacYY7zSBRycRzME_5ggq4KJhQqRW8C780KoCAHKcth06nY_rj75mb9TIj_PIXd33zgEKj5sM3I52QhoBe_v5KJS-QPFISRDQmMWHbBfFFH4ACmJVZcY5H8_OFg_XIYTn55SaXjVgQtvlG2vIuHb0UWtTsYGZ_RbbqA9i2fsx6-g6j2Eer-0rj9wszeLuWGEtZJyvQQSz7U52T4mi_QAw6n_-i9EwevVdaxeMQ98kchK9U2XZWqS8l2t-ScRyWEP1Y90eOyNxfP0ZVnmfysxZJuqBOCFV-MeUkv0u5Ykiyda2Ij2mssF8J-4gKAU0ViBUoOvAcdBZZjU9ouVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار خطاب به ترامپ: جنگ ایران برای شما به یک بن‌بست استراتژیک تبدیل شده. چرا نمی‌توانید به این جنگ پایان دهید؟
🔹
ترامپ: جنگ ایران یک موفقیت نظامی فوق‌العاده بوده است. ما ایران را خلع سلاح هسته‌ای کرده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448409" target="_blank">📅 20:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448408">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a11ad69b.mp4?token=G33G3wlMH8iWUcozDG_7k053Dq1aR1-ptWB-kpq5EopYqNNmrpuR3g64TlUjHITSeiYJtQNuQ1EQLuVjzGLuH0i6W72Z71XgZeIVNf5fIN69mT8--EL8V89eK42UaibpCPZM82cHqIlWTSpmYzQvtqy1YlIlV4CkBpa9sAbrSpfrNnynwCcmufPli1zYHUnfDu25ZalFGuz8ajqhkten5cC5b65KRXycNHAOKCcb8ySgACciWyUWNs8Zfq3C4OGG7fmP91mFLHrV166GU7efRoJtyle6RtDH2SsL-0taPZYWJ19ijiUZnzHVoc5pK7mavUVXBFiMdOiLu-tNbxrrgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a11ad69b.mp4?token=G33G3wlMH8iWUcozDG_7k053Dq1aR1-ptWB-kpq5EopYqNNmrpuR3g64TlUjHITSeiYJtQNuQ1EQLuVjzGLuH0i6W72Z71XgZeIVNf5fIN69mT8--EL8V89eK42UaibpCPZM82cHqIlWTSpmYzQvtqy1YlIlV4CkBpa9sAbrSpfrNnynwCcmufPli1zYHUnfDu25ZalFGuz8ajqhkten5cC5b65KRXycNHAOKCcb8ySgACciWyUWNs8Zfq3C4OGG7fmP91mFLHrV166GU7efRoJtyle6RtDH2SsL-0taPZYWJ19ijiUZnzHVoc5pK7mavUVXBFiMdOiLu-tNbxrrgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: وقتی جنگ شروع شد تورم ایران ۵ یا ۶ درصد بود اما الان تورم آن‌ها به ۳۵۰ درصد رسیده است.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448408" target="_blank">📅 20:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448407">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5254493837.mp4?token=Hl7r3_XC6mjxWf7DNOlZ10CCJ2z9UXKSCjlSC-64OTeroUEc_dBqAi1xPbERcG6EqRdJPtJi1RaQ0fou81sHrx4HCNVLk2PfuOAN_mJtsCIQkSL0IDT3PbsOBV8PRRHeI_PjLzURfpsOF647sIodhgcjNgfbwFT9rLfTyLKk8e4NE1nQ7NqRSlNPmHZyUtDlRGjb7ffDOcWstv6Nze_PM0NiZUTRovfGSMY6mO8QjIjwmOyKaX3xWYXZTvQRV6RTqAGmP8o1MLhibn14wxzNaAe6d_sdSq9HFtw2f8bSQ-nSByGBm1Gbn3oYMdmq2bmH0aVyzofcjtkQd1LcUT3GHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5254493837.mp4?token=Hl7r3_XC6mjxWf7DNOlZ10CCJ2z9UXKSCjlSC-64OTeroUEc_dBqAi1xPbERcG6EqRdJPtJi1RaQ0fou81sHrx4HCNVLk2PfuOAN_mJtsCIQkSL0IDT3PbsOBV8PRRHeI_PjLzURfpsOF647sIodhgcjNgfbwFT9rLfTyLKk8e4NE1nQ7NqRSlNPmHZyUtDlRGjb7ffDOcWstv6Nze_PM0NiZUTRovfGSMY6mO8QjIjwmOyKaX3xWYXZTvQRV6RTqAGmP8o1MLhibn14wxzNaAe6d_sdSq9HFtw2f8bSQ-nSByGBm1Gbn3oYMdmq2bmH0aVyzofcjtkQd1LcUT3GHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: احتمالاً محاصرهٔ ایران را هم برقرار کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448407" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448404">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۸۸.pdf</div>
  <div class="tg-doc-extra">4 MB</div>
</div>
<a href="https://t.me/farsna/448404" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448404" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448403">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368b999813.mp4?token=kjFpsscl7grUMMJT_y67Y_sdsLZvIThrxzvVL58dS4p63DCymJhOFaBmNNBrtVXosQ5BbvXyXllUaEUlYMWnvo2ttKCIroWcq9DnyTQSQyY3eorM_2Vz4-w6rFnux9_TFBsaGepR84Nrz5f0SZnxh3y7a_vknnQg9Rq0fUEn1JVEKOL2keOzxYZJfX20BxWf-docgUgBugXYNGclUVJSfXN3t41d4jiaimRoo25zpsLCG0xoy7SHqF0qYwJpMzEB2GbH5BGb193fmuZaGDgbkqKapVyobHhqYIpcSu3K75Iv9WJyHzIAZq7bIpAyDpKh5PCFDjiaHpcXWYSvhtFPBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368b999813.mp4?token=kjFpsscl7grUMMJT_y67Y_sdsLZvIThrxzvVL58dS4p63DCymJhOFaBmNNBrtVXosQ5BbvXyXllUaEUlYMWnvo2ttKCIroWcq9DnyTQSQyY3eorM_2Vz4-w6rFnux9_TFBsaGepR84Nrz5f0SZnxh3y7a_vknnQg9Rq0fUEn1JVEKOL2keOzxYZJfX20BxWf-docgUgBugXYNGclUVJSfXN3t41d4jiaimRoo25zpsLCG0xoy7SHqF0qYwJpMzEB2GbH5BGb193fmuZaGDgbkqKapVyobHhqYIpcSu3K75Iv9WJyHzIAZq7bIpAyDpKh5PCFDjiaHpcXWYSvhtFPBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشهد، لحظه‌به‌لحظه به بدرقهٔ آقای شهید نزدیک‌تر می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448403" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448402">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c89662c3.mp4?token=QsmOYvv5xbAdBpcxe1BlIfKYbp6lcrVmPzF29ACMox5se701qhJsQ9FGb86ObgJs7CzbrXLsIa7ZnXDdJpVo9gTSWrK2PDikt-m3VbhLMrUteYIPb8FQyxcLMvnH8Dlh09_KPe-QEUmlTqQdbSmKg39d7fcFLg0n7KReN7QhK8aN-4zm6_LKOh1D7FdcY4ImM4_RIaTYLkvXtXxVstKFmB9ms_fCtnskOQTM0szgDNz2ylbbR6nLxW-qyXmrgl0xQ38Wo50GKmD0GdoxMtxcIhI_rIuva8I12ST1Nk6bLfqv9wg9uO8wlNQCAwMnoZ-h8PMbLWkPfdCZxVJeSEaTyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c89662c3.mp4?token=QsmOYvv5xbAdBpcxe1BlIfKYbp6lcrVmPzF29ACMox5se701qhJsQ9FGb86ObgJs7CzbrXLsIa7ZnXDdJpVo9gTSWrK2PDikt-m3VbhLMrUteYIPb8FQyxcLMvnH8Dlh09_KPe-QEUmlTqQdbSmKg39d7fcFLg0n7KReN7QhK8aN-4zm6_LKOh1D7FdcY4ImM4_RIaTYLkvXtXxVstKFmB9ms_fCtnskOQTM0szgDNz2ylbbR6nLxW-qyXmrgl0xQ38Wo50GKmD0GdoxMtxcIhI_rIuva8I12ST1Nk6bLfqv9wg9uO8wlNQCAwMnoZ-h8PMbLWkPfdCZxVJeSEaTyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم سیدالشهدا(ع) مهیای استقبال از رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448402" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448401">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxSS2AH1YM-ryIgwAlNFeWfuy1vExdqI8g4c7mjIi0XZ-lAT-8a8sjIA2jmFFQDHp5A2NeB2wlzE4cmZ43wvZBxlCtdWEBzFAv0jeN1Kds7zrcOYl8SYnP4-aIXYxzGZWUfng4n7QbkXANhc-DYygNi6UsKHJZm2_OYxlskIWajKtNMggh1NhgrMisevJdqvSpNascM-N_kBveAp-8ygXHWNz3T8kOCLOTZP2rls79jtKIRcoqMFMP9l6-_u1DTMJ6TDYxHz5k89j8P7WgBhC54Lr2PU0c7pCFJs1KSgx9c0Wn43dNx5sBkoGrHiepHcdcYFLzCU3VI414-pFx2A7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل‌گهر از حضور در لیگ قهرمانان آسیا انصراف داد
🔹
باشگاه گل‌گهر سیرجان با ارسال نامه‌ای به فدراسیون انصراف خود را از لیگ‌قهرمانان آسیا اعلام کرد تا بدین ترتیب چادرملو نماینده ایران در لیگ سطح ۲ آسیا باشد.
🔹
در نامۀ مدیرعامل گل‌گهر آمده: این تصمیم واکنشی به فرآیندی است که طی آن ابهاماتی پیرامون حقوق این باشگاه شکل گرفت که امروز حتی اعاده احتمالی سهمیه نیز نمی‌تواند آن را جبران کند.
@Sportfars</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448401" target="_blank">📅 19:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448400">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ceb8ef0ea.mp4?token=K31TNoJ0AQ7i8OYuPICTHDDJa-Z498ezxT5Nh7-hRozPLn4w7s_t14cMmdWlAA-6tIX8MG9-ct4UmZZIlYqo1HBcXcRLKTbGrCA7g_2pR5QarzdOLIErn5AaVTroYkBYUnOc-DoXXqZAWc03d3X6hs12LUQ3xXLr_QaxKKc-TDA5ejseUrZCzJJmCZBxVut5fVlZqEu5ffVdz3HqYEVhH8i8bWT-J5vOl09gwnSckRWZmABVFkeQEs-79ynYxiDST4fyY6Afs58FKcjGudX8_31sAZ8vfLHQCnaE9yYk0uv4-m0VVGNpAGyDi0k61sSUmpHHE4KBvZQ1n2cECnABfLzpOFnTA3XgWo1Tl6Vf3ommKepYsxIy3riBEchGLRSw7D34rJ_VM6HxpaVuLZlKCgCWkMc6a9u0QjhgjeOjrS0qfoWcKUQOJJrbMEVJ54DwHXrJbnXrqSgvIa_zLuN5vpNXK07SPbwA_scwQ6aCUJ5i9M3oEjIxIkH-eE1edOU-f1hjRgI0fXLwRABft1az2G_0dHro6oQo3Kr68LBdRuaNeLcDavy7GI-wH7VA7ze0SVnEIG8v8bsHZj71JfFaZLj9dBuRkxdSw2NE0H_1NIOekBf4BlL8K40a0s7aN1BGhie_qrckWCxKrSWXh7c56BeWwPSe8NPA4iS-ylx7PSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ceb8ef0ea.mp4?token=K31TNoJ0AQ7i8OYuPICTHDDJa-Z498ezxT5Nh7-hRozPLn4w7s_t14cMmdWlAA-6tIX8MG9-ct4UmZZIlYqo1HBcXcRLKTbGrCA7g_2pR5QarzdOLIErn5AaVTroYkBYUnOc-DoXXqZAWc03d3X6hs12LUQ3xXLr_QaxKKc-TDA5ejseUrZCzJJmCZBxVut5fVlZqEu5ffVdz3HqYEVhH8i8bWT-J5vOl09gwnSckRWZmABVFkeQEs-79ynYxiDST4fyY6Afs58FKcjGudX8_31sAZ8vfLHQCnaE9yYk0uv4-m0VVGNpAGyDi0k61sSUmpHHE4KBvZQ1n2cECnABfLzpOFnTA3XgWo1Tl6Vf3ommKepYsxIy3riBEchGLRSw7D34rJ_VM6HxpaVuLZlKCgCWkMc6a9u0QjhgjeOjrS0qfoWcKUQOJJrbMEVJ54DwHXrJbnXrqSgvIa_zLuN5vpNXK07SPbwA_scwQ6aCUJ5i9M3oEjIxIkH-eE1edOU-f1hjRgI0fXLwRABft1az2G_0dHro6oQo3Kr68LBdRuaNeLcDavy7GI-wH7VA7ze0SVnEIG8v8bsHZj71JfFaZLj9dBuRkxdSw2NE0H_1NIOekBf4BlL8K40a0s7aN1BGhie_qrckWCxKrSWXh7c56BeWwPSe8NPA4iS-ylx7PSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحدت شیعه و سنی در مسیر عشق به رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448400" target="_blank">📅 19:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448399">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/846e3e4aaa.mp4?token=thviacvo3wtE4Kt9NFFUwWWa73d57Njc8wZcy58MmLmrIhlk4gkWxWX1LGhBJ6fHKXw-AOtISniStNabai9VgdFPxf5Y0VizZrNDwHZIQnuA1JNNrYC04LKDm75XvCIKvP8a_XMN-D2RFq4HeSzG3oyAqQ9gfS7tQvha2LpkeryM52iXRABf_arwZjAumZyYbfrjy_vdZqiB1jJncb5JOUxcnyZNpGuvq8B4lEaOJrvQzMPKcmibxnCyzDOBQCBCv-7EPJeUNsCaewGGpm-nCfq_N0E1_bKbRXomqcJp2F41KZxSyICdF-3z35J1EBN6LWsg8qUUXsH8LDVvr9Qe9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/846e3e4aaa.mp4?token=thviacvo3wtE4Kt9NFFUwWWa73d57Njc8wZcy58MmLmrIhlk4gkWxWX1LGhBJ6fHKXw-AOtISniStNabai9VgdFPxf5Y0VizZrNDwHZIQnuA1JNNrYC04LKDm75XvCIKvP8a_XMN-D2RFq4HeSzG3oyAqQ9gfS7tQvha2LpkeryM52iXRABf_arwZjAumZyYbfrjy_vdZqiB1jJncb5JOUxcnyZNpGuvq8B4lEaOJrvQzMPKcmibxnCyzDOBQCBCv-7EPJeUNsCaewGGpm-nCfq_N0E1_bKbRXomqcJp2F41KZxSyICdF-3z35J1EBN6LWsg8qUUXsH8LDVvr9Qe9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشایر کربلا: خون‌خواهی رهبر شهید را فراموش نمی‌کنیم و آمریکا را رها نخواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448399" target="_blank">📅 19:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448398">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a747ffd1.mp4?token=XYCae7Os-ebJLL6-u-87Y6CYFrlhV4mNGMXVPb88kVdAqf3Bv08KSsXfH7jt_Sv_TB5WOeXGTOTZXKTyxQnghpVBysrLpz1l2OECstQngOztGOkFGUFta_yKUwsTt2ChJoIcnGIQoAWpU2y-Yx4vQAb8QskYRp7BulD7oMwj5Hunz3loW56rvcnHHOLdmAvKU8ZBDc40tU7YDgZwyW5fmkjNgGQcrM6FnXvB1R65QxcbUwGL4R68fM6shefeGGZe58VoKFv-XdNO51hxOehk102C34CxidQkZq_KoMe19H43O3vKlaf7_tNtdWtNsIq3cidlalH2gOYjyJRzNqiPmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a747ffd1.mp4?token=XYCae7Os-ebJLL6-u-87Y6CYFrlhV4mNGMXVPb88kVdAqf3Bv08KSsXfH7jt_Sv_TB5WOeXGTOTZXKTyxQnghpVBysrLpz1l2OECstQngOztGOkFGUFta_yKUwsTt2ChJoIcnGIQoAWpU2y-Yx4vQAb8QskYRp7BulD7oMwj5Hunz3loW56rvcnHHOLdmAvKU8ZBDc40tU7YDgZwyW5fmkjNgGQcrM6FnXvB1R65QxcbUwGL4R68fM6shefeGGZe58VoKFv-XdNO51hxOehk102C34CxidQkZq_KoMe19H43O3vKlaf7_tNtdWtNsIq3cidlalH2gOYjyJRzNqiPmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر چین در ایران: همکاری‌های ما با ایران تحت تاثیر طرف ثالث قرار نمی‌گیرد
🔹
چین به‌عنوان شریک جامع راهبردی ایران کماکان از ایران حمایت می‌کند تا از حاکمیت و امنیت و کرامت ملی خود دفاع کند. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448398" target="_blank">📅 19:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448396">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c54bed844.mp4?token=KeTtv3yXE_Ry46z5lldbVN7LPawkKP_wLKuejTi_xKTGxSSdl4AjTxLcgEh7fsYdZrt37WtJbxPEI6SXVCA0ACuJSNcEyupgdeWOb77XKeap5llE03RTrU20ivvv6k7WLDBYoVP-8iu8pbY_NFOifQJiqMIu03C-_1DIl9QvqpWfVopshBNcvNBxyvzsWhRZmeFKkKZB2W03I59CBfcWH7yHQmY6-eym-1z_Rn0qm1V1POY0yv5Okbh6xSAWS22SGjWTEb7GDjINvyJZtqKZ-9LtSVQVYi6kLcfO_I9kkx3-G10Oxwxo3QnNmANQ_3Z6S15uL6heO4BhBC4pMJu3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c54bed844.mp4?token=KeTtv3yXE_Ry46z5lldbVN7LPawkKP_wLKuejTi_xKTGxSSdl4AjTxLcgEh7fsYdZrt37WtJbxPEI6SXVCA0ACuJSNcEyupgdeWOb77XKeap5llE03RTrU20ivvv6k7WLDBYoVP-8iu8pbY_NFOifQJiqMIu03C-_1DIl9QvqpWfVopshBNcvNBxyvzsWhRZmeFKkKZB2W03I59CBfcWH7yHQmY6-eym-1z_Rn0qm1V1POY0yv5Okbh6xSAWS22SGjWTEb7GDjINvyJZtqKZ-9LtSVQVYi6kLcfO_I9kkx3-G10Oxwxo3QnNmANQ_3Z6S15uL6heO4BhBC4pMJu3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش زلنسکی به اینکه ترامپ او را «رئیس‌جمهور پوتین» خطاب کرد
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448396" target="_blank">📅 19:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6553b9097e.mp4?token=tiC87oBpUp-ToNieKIOTIHNXZfSyGdfvyjcGkxzk4ajbKFJgR6DW-igaEeYcx-6zT0p-hudXzSakCqtCHt4mrozn87Dgotf7yjYa190npe5sDqEFNYO0iokU-vgbOJgQ_l8Vq-S-lv1WrgGHkF1SVnlyrToeh3TO_rqj_VkQpEvtQskeTbl3XJ5w5xygf2rWfywpBre6KWcyY5MO8zBf35oxULVUZSmr2G31yCEEfxq_9p5pnV6x3SQ2SmofqOdoeNo952x9sl1Mznosd5FHGeThnB9_yfkqp_jaeHZB6V9hULNpSMyXs2hwMx04EkvBw_08U4tFSwWdPPgx9OpNHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6553b9097e.mp4?token=tiC87oBpUp-ToNieKIOTIHNXZfSyGdfvyjcGkxzk4ajbKFJgR6DW-igaEeYcx-6zT0p-hudXzSakCqtCHt4mrozn87Dgotf7yjYa190npe5sDqEFNYO0iokU-vgbOJgQ_l8Vq-S-lv1WrgGHkF1SVnlyrToeh3TO_rqj_VkQpEvtQskeTbl3XJ5w5xygf2rWfywpBre6KWcyY5MO8zBf35oxULVUZSmr2G31yCEEfxq_9p5pnV6x3SQ2SmofqOdoeNo952x9sl1Mznosd5FHGeThnB9_yfkqp_jaeHZB6V9hULNpSMyXs2hwMx04EkvBw_08U4tFSwWdPPgx9OpNHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: پیکر مطهر رهبر شهید نزدیک بین‌الحرمین است و به‌زودی وارد این مکان مقدس می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448395" target="_blank">📅 19:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f255e148.mp4?token=hP8igXXZAhPm-ADwKLsWsk0Meda9DQrM5Meg2ET0aHyWlx0m7CdaCW3pG-j4N_kmcObHjN3cy7Ozly28s7p_KNrmjm43kx3218aJrR5slMpvwpkFbm0BbK2xaHxwi-Hjit2KZzWvhAJ8jFwsPIxdp9VWUGZcO63ms8YpIU7M_mqyr7HGrq4s5N2Gmd54h2ntApatm6fLPSD22Wa7ge45Z0ySY7Etj0TcPsSygITnHuu8xEIZLS0XKSWhBK4qDAEgxmRayeNuyf7_I1r1CFHh4cBagNIG92foxhCv4oCg9isI8w86sPJHJ6Nz6wQQNYxNbbYeLEnVdmgQYlb4fpv_PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f255e148.mp4?token=hP8igXXZAhPm-ADwKLsWsk0Meda9DQrM5Meg2ET0aHyWlx0m7CdaCW3pG-j4N_kmcObHjN3cy7Ozly28s7p_KNrmjm43kx3218aJrR5slMpvwpkFbm0BbK2xaHxwi-Hjit2KZzWvhAJ8jFwsPIxdp9VWUGZcO63ms8YpIU7M_mqyr7HGrq4s5N2Gmd54h2ntApatm6fLPSD22Wa7ge45Z0ySY7Etj0TcPsSygITnHuu8xEIZLS0XKSWhBK4qDAEgxmRayeNuyf7_I1r1CFHh4cBagNIG92foxhCv4oCg9isI8w86sPJHJ6Nz6wQQNYxNbbYeLEnVdmgQYlb4fpv_PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر اختصاصی شبکه افق از حرکت سخت خودرو حامل قائد شهید امت در عمود ۴۶۱ به‌خاطر ازدحام جمعیت عشایر عراقی  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448394" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448393">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e7bfb4ad5.mp4?token=c0Z6W9_NjL-mk566pGiQjH5s1e7PQt7hsngSXfmM3NJ_l2n4btZt1CJgyAFIkLD-Y5TmKo4jmIcZVKNAzMk936TvOxDNqXABijXyDK_6lmp8FrRmKSR-SAQA5bL7XcfnJh6SRNzplpZ-lqoj5I0LVtZZlKRAEZIOICf76nyFF5znGizmMwuiFOS-TRYOhlO2TzW0GlOHeQr32lY_JGE5BYOomepm6-5LeNb9TdWP7BA2jPiq8I9USl_JbhLT6AOH1kI22PLRyUSX2WXPiyzNc56ajV3LfZR5y2Gke0NPB-9F5cvTDslaZAhLGIEam8pEEsYjV60DWb4TudV9bfHzeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e7bfb4ad5.mp4?token=c0Z6W9_NjL-mk566pGiQjH5s1e7PQt7hsngSXfmM3NJ_l2n4btZt1CJgyAFIkLD-Y5TmKo4jmIcZVKNAzMk936TvOxDNqXABijXyDK_6lmp8FrRmKSR-SAQA5bL7XcfnJh6SRNzplpZ-lqoj5I0LVtZZlKRAEZIOICf76nyFF5znGizmMwuiFOS-TRYOhlO2TzW0GlOHeQr32lY_JGE5BYOomepm6-5LeNb9TdWP7BA2jPiq8I9USl_JbhLT6AOH1kI22PLRyUSX2WXPiyzNc56ajV3LfZR5y2Gke0NPB-9F5cvTDslaZAhLGIEam8pEEsYjV60DWb4TudV9bfHzeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر اختصاصی شبکه افق از حضور پرتعداد عشایر عراقی در مسیر مشایه، حرکت خودرو حامل پیکر رهبر شهید را متوقف کرده است  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448393" target="_blank">📅 19:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24537cb428.mp4?token=dye-wjF2CZzaVWHuevq_i2Hr2luouYXBj0RhIAKHAjQ81qEAjGjb_6rX7zPdfnClUluEVFVKbOmdxXRdssMo2QwWLxdc_OKNtTkKHYFn-VLo1U2ltFfgIel0ZrYlDHCaFfbIzlAJIIYX6po1lrGAU3hcpHVxSAxxbO4yxYrNj78ehThREVG7s4tP6ilnyHSBS_V3HWaU_LMZgqzh1PT3mqCTlBuqxoIcDFmLVKdwVD1t-3QN5iQ0J47_2BJgE4mycQ3a_7WDTZwNGxslqKKJb9fQeDprXkoM--HZrOQhE-1z0rNAJMzVVIuSZIbxKyQN0DhJkE2_e_GTbdpR261Irw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24537cb428.mp4?token=dye-wjF2CZzaVWHuevq_i2Hr2luouYXBj0RhIAKHAjQ81qEAjGjb_6rX7zPdfnClUluEVFVKbOmdxXRdssMo2QwWLxdc_OKNtTkKHYFn-VLo1U2ltFfgIel0ZrYlDHCaFfbIzlAJIIYX6po1lrGAU3hcpHVxSAxxbO4yxYrNj78ehThREVG7s4tP6ilnyHSBS_V3HWaU_LMZgqzh1PT3mqCTlBuqxoIcDFmLVKdwVD1t-3QN5iQ0J47_2BJgE4mycQ3a_7WDTZwNGxslqKKJb9fQeDprXkoM--HZrOQhE-1z0rNAJMzVVIuSZIbxKyQN0DhJkE2_e_GTbdpR261Irw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر اختصاصی شبکه افق از حضور پرتعداد عشایر عراقی در مسیر مشایه، حرکت خودرو حامل پیکر رهبر شهید را متوقف کرده است
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448392" target="_blank">📅 19:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448391">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c194d5bb86.mp4?token=aB_pLM6sQ5Cxjkny7ErWiieukRkDMBo7z4KXSce01trlmBUuhS3A-0EnGcig6DO3SWARooYyI0WnpTUx8bTDuGsSHSqTnbKUx5l1obSUx9c6eUTHwgo3e2Iyle9JzMyRmHRI8F-ChT2cSGHowwHVPzNdbOVAeI32kTtZSf1jF2KStDSn7p8A7gG2U-qroJvOD_s1eJyEUFuP3xsotBEeD4DX9_kbsQIFbqkGnNd2peIJNaTN7njgH4zzZ7GvpiUhx_RwWZxNV8RSwjkj-bw8d6XcIei2pgFMmJ72adb2pwMXgAe9HXOXCf73RB6TaZkfe7eFjGGdZP0dEBxOj7GGRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c194d5bb86.mp4?token=aB_pLM6sQ5Cxjkny7ErWiieukRkDMBo7z4KXSce01trlmBUuhS3A-0EnGcig6DO3SWARooYyI0WnpTUx8bTDuGsSHSqTnbKUx5l1obSUx9c6eUTHwgo3e2Iyle9JzMyRmHRI8F-ChT2cSGHowwHVPzNdbOVAeI32kTtZSf1jF2KStDSn7p8A7gG2U-qroJvOD_s1eJyEUFuP3xsotBEeD4DX9_kbsQIFbqkGnNd2peIJNaTN7njgH4zzZ7GvpiUhx_RwWZxNV8RSwjkj-bw8d6XcIei2pgFMmJ72adb2pwMXgAe9HXOXCf73RB6TaZkfe7eFjGGdZP0dEBxOj7GGRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مرجع تقلید شیعیان کربلا در مراسم تشییع پیکر رهبر شهید انقلاب
🔹
حضرت آیت‌الله سید تقی المدرسی، از مراجع تقلید شیعیان در کربلا به حرم امام حسین برای حضور در مراسم تشییع پیکر رهبر شهید انقلاب رفتند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448391" target="_blank">📅 19:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448390">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BewOJpupXww7mOsXYggmWOaeNlm2-mFBVG25RG79d4ikEgHYuQUgfbOCTcGXfEm32BCQ0Hl-ZNdCWF_Ez2zW0_tBmIw3mB_PKXiJCd6RVUQjXjuJDubA2_hIBCT0yyaoFPLpjM6aZH0cP1SZEQd-EftD_9mcVK0sXXT2h7t0C46U6Ng3Fcs02vB88cywrefDNiyBwEbzCoIDX4CRyV8SHuK8lJbYv2nfqcx9-04vf5l5tedXaxIbuznzA1O3ropQ4B17FKf7DigXckV-qhG4mD1ZrcatTxO5PbOiXjREhYUvdd09NU0cu0RnT8ZDdgRJQ6o1wC92xiGIz3no6QliMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸ قهرمان ارتش به شهادت رسیدند
🔹
روابط عمومی ارتش: به دنبال تجاوز جنایتکارانه ارتش تروریستی آمریکا به مناطقی از جنوب ایران اسلامی در بامداد امروز، ۸ نفر از دلاورمردان  نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در بندرعباس و بوشهر، حین دفاع از میهن اسلامی، بر اثر اصابت پرتابه‌های دشمن به شهادت رسیدند.
🔹
سروان علی معینی از پایگاه شهید یاسینی بوشهر، ستوانیکم علی مهدی‌زاده، ستوانسوم حامددورای، استواردوم امیرحسین قاسمی، استواردوم علیرضا زارعی ثانی و استواردوم علیرضا بالیده از پایگاه شهید عبدالکریمی بندرعباس و ناواستواردوم شهاب امیدی بزی و ناوی محمدجواد روانفر از منطقه یکم نیروی دریایی ارتش، در این حملات، به مقام شامخ شهادت نائل آمدند.
🔹
ارتش جمهوری اسلامی ایران با تاکید بر ایستادگی تا آخرین نفس مقابل دشمنان، اعلام کرد که انتقام خون شهدای میهن اسلامی را از دشمنان این آب و خاک، خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448390" target="_blank">📅 19:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448389">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
سخنگوی کمیسیون امنیت ملی مجلس: حملۀ مجدد آمریکا با تغییر دکترین هسته‌ای پاسخ داده می‌شود
🔹
در رویارویی آینده، دشمن با تهاجمی همه‌جانبه و غافلگیرانه از سوی جمهوری اسلامی ایران مواجه خواهد شد.
🔹
گزینه‌های زیادی در اختیار داریم که حتی در جنگ ۴۰ روزه نیز از آن‌ها استفاده نکردیم.
🔹
گزینه‌هایی مانند خروج از NPT، تغییر دکترین هسته‌ای و بستن تنگۀ باب‌المندب در کنار تنگۀ هرمز قابل بررسی خواهد بود.
🔹
طرح خروج از NPT نیز در مجلس آمادۀ بررسی است و اگر ایران با تهدید موجودیتی روبه‌رو شود، تغییر دکترین هسته‌ای نیز می‌تواند در دستورکار قرار گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448389" target="_blank">📅 19:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448388">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e89016597b.mp4?token=YIUBcd_Vif87mpB751uyqNXUm-rzw9xUYcXjpJlmROyatGCR70YIBTi_4TUjVRSglSjUH1oKWgr8nD0_cIiocAMR85GUS00e476b-R-zrBoaSUfklfKq7TUY45tuPpPdOAsuLDwKO-47k5QA78m1LtcrR37x5U4jNZ9RH8QKa6F9yKdarbDUySh_JvBgkan1mwKInkJIi3JutQTPSQ-xPqg3aKUqRewFpW3xZUJORGDZrzT2X_jEaLEM_3QirOnXSxwfM6_5zWGniumr9PUeFU3Uaj4UsfQzYsVMQHMyR43OH30fQshYacO0q06uLwMIid2jf5I4Fop0TMLVKsSINA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e89016597b.mp4?token=YIUBcd_Vif87mpB751uyqNXUm-rzw9xUYcXjpJlmROyatGCR70YIBTi_4TUjVRSglSjUH1oKWgr8nD0_cIiocAMR85GUS00e476b-R-zrBoaSUfklfKq7TUY45tuPpPdOAsuLDwKO-47k5QA78m1LtcrR37x5U4jNZ9RH8QKa6F9yKdarbDUySh_JvBgkan1mwKInkJIi3JutQTPSQ-xPqg3aKUqRewFpW3xZUJORGDZrzT2X_jEaLEM_3QirOnXSxwfM6_5zWGniumr9PUeFU3Uaj4UsfQzYsVMQHMyR43OH30fQshYacO0q06uLwMIid2jf5I4Fop0TMLVKsSINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر چین در ایران: همکاری‌های ما با ایران تحت تاثیر طرف ثالث قرار نمی‌گیرد
🔹
چین به‌عنوان شریک جامع راهبردی ایران کماکان از ایران حمایت می‌کند تا از حاکمیت و امنیت و کرامت ملی خود دفاع کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448388" target="_blank">📅 18:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448387">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895864774a.mp4?token=Vygv7_marGdPqLKidP6fx_A10wfRMYsB8x4WnrGoazaNjjqhTrMocYKO1DtBxpVTx0hDmswIjpxZugxKy807xHVECETc4pGFrEZRHleqMkUW9FXjCHdhMQdKqJbhXwTA8oaDVdEPpdHm9ULedneycYl-8l4Z_FlYrw3Xa8icpOPBZ9DbsF7sPr_TCb8vXIiQPOBXKRRkL-ougS-aMbDZuFMRYgYNpReTusIyqhWFIvtyVdz1BXNpYuFKgEwjPQxtAYQ2PgkCr_YrV-l3XKPrKXDq8J1AKnJrhc8InqzV9pJ6aznFWEb_wiesvVUkZq3aX3r69ab7Xi7PWub8E-zKCUU2ixVFHnvlFuDd6QlnAv19gt-8JiyRpoV_iSrH1nOsxUJCU9d7b7thAu7sJcfNwLntKduyBcOQOXxP7MvDp0YcNCOFrw6WUOxZ0hUkJvG3O7tzy3Gkei-klYpzNTn_0eEyY_jxCvWhAg5qLcGi_YrTkpTrkPk4XYv3ybIGXQtitzkgPi064uOjoVSrgnYu7bITqQwpzv2mbagfYQY50YCzoedFoPXdBCgpo9dGqk8i5Xt9OfjrweAsZOnELmuYacSaG9lgncqwza_kzuJRfL8M7mg4gMlg1bRdO52mZzCjbvJx82WW0dX501wd6XjAhwGd6GvC-bJ2hxxozOFcW4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895864774a.mp4?token=Vygv7_marGdPqLKidP6fx_A10wfRMYsB8x4WnrGoazaNjjqhTrMocYKO1DtBxpVTx0hDmswIjpxZugxKy807xHVECETc4pGFrEZRHleqMkUW9FXjCHdhMQdKqJbhXwTA8oaDVdEPpdHm9ULedneycYl-8l4Z_FlYrw3Xa8icpOPBZ9DbsF7sPr_TCb8vXIiQPOBXKRRkL-ougS-aMbDZuFMRYgYNpReTusIyqhWFIvtyVdz1BXNpYuFKgEwjPQxtAYQ2PgkCr_YrV-l3XKPrKXDq8J1AKnJrhc8InqzV9pJ6aznFWEb_wiesvVUkZq3aX3r69ab7Xi7PWub8E-zKCUU2ixVFHnvlFuDd6QlnAv19gt-8JiyRpoV_iSrH1nOsxUJCU9d7b7thAu7sJcfNwLntKduyBcOQOXxP7MvDp0YcNCOFrw6WUOxZ0hUkJvG3O7tzy3Gkei-klYpzNTn_0eEyY_jxCvWhAg5qLcGi_YrTkpTrkPk4XYv3ybIGXQtitzkgPi064uOjoVSrgnYu7bITqQwpzv2mbagfYQY50YCzoedFoPXdBCgpo9dGqk8i5Xt9OfjrweAsZOnELmuYacSaG9lgncqwza_kzuJRfL8M7mg4gMlg1bRdO52mZzCjbvJx82WW0dX501wd6XjAhwGd6GvC-bJ2hxxozOFcW4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فدای جان پاکی که جان‌فدای ما شد...
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448387" target="_blank">📅 18:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448386">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0kTC_mvBt2b8gPOQ0eu1Sx5FbvGbZkOWQx01xtm3yUEkPwnDVVfgV4Ksh0I1ZGagryo9T_AtUqwBr0GToTh6WEtLDuQwF0T7rVCOUy6qfi_LtXqTVWs2Ieh7e0RtWWxxtLqd_Pfvc30bw6CoGUkHYGV9hsjkOf0ZEwoowctdxgdGgnRQuktyGfSsn2YQjOFM4xLEe-IzIpmLo746A9BRWuFtwiggijHLzsbcHqy1Yt4tq06_J9mQoEc5D6tTg07ecy6wIua-kAmJ6UywCh_WfF5DRagL9Ctbo3LaZpRQRMt43kZHq65Hf5XwsoIPs4pBd_6NiSwrbJB98P-rFjeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
فرزند ارشد رهبر شهید انقلاب به همراه ۲ فرزند آیت‌الله‌سیستانی در انتظار پیکر امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448386" target="_blank">📅 18:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448385">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b179b4651.mp4?token=hYzC6Pd6PM2bTykyIW9Z67vJRwqg2EyPMjlg91L6XgVYdvYAeFqYs4G6Ip4nPcWHdRsXEECHdsCLNWArVmsD1IcIG84Rkn1bE1PkSTTlotQW8HJ2S4h4M85n5m43alHJQ9m_ncfamwzl77ZtKEpVDPZxf9AUgMErmEvNS65STXu8w7dtb_moTnUmqOwfr9ZDC7CMWleePqsX-7xucY3XdiGMuwHcH_cbNP49s_khn78WGNvk9Gd0Ywxv4lbwbuPfgU_yUVsOiNkg1_qWKD0Y9NaXzGanQ680HzCPa_JGmitAnx43O_27p0rrt76JZh0VB_E4QSgrMbcEJrciIJpx3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b179b4651.mp4?token=hYzC6Pd6PM2bTykyIW9Z67vJRwqg2EyPMjlg91L6XgVYdvYAeFqYs4G6Ip4nPcWHdRsXEECHdsCLNWArVmsD1IcIG84Rkn1bE1PkSTTlotQW8HJ2S4h4M85n5m43alHJQ9m_ncfamwzl77ZtKEpVDPZxf9AUgMErmEvNS65STXu8w7dtb_moTnUmqOwfr9ZDC7CMWleePqsX-7xucY3XdiGMuwHcH_cbNP49s_khn78WGNvk9Gd0Ywxv4lbwbuPfgU_yUVsOiNkg1_qWKD0Y9NaXzGanQ680HzCPa_JGmitAnx43O_27p0rrt76JZh0VB_E4QSgrMbcEJrciIJpx3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیارتی که سال‌ها در دل بود، به وصال رسید
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448385" target="_blank">📅 18:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448384">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6318b53b.mp4?token=huRSY54pzBgrtaOlGZ9AVhK2vOZ5wyD3Unf95FgN1JZYS0_Pa677W8R8s4b8i5CmfcFfvN_VbeIbjlizGHjme9Y8gztEfSNGUjLiwqrpf_aHET3626gkj73ClzrvfuCPhXAGo0iKEiZ7NIdehq3t0rdWw1MZGI9J7j7IZigX8YFXWQt6jc0pp4NtsTMh55ty4a2F6Yu9Vgr6sjN61xkbHUriYanqaXklYAzu7eB4-GjQJwPGQ92uHuf-kCDGbt8cQc3NpbIMbURvrQgkfvVpjLcU8f6MoENLNXw19aMrhhI4Z-5SX7dV_c_CdX_DHwH3E4cWH_0KBMxPp55gOIp-OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6318b53b.mp4?token=huRSY54pzBgrtaOlGZ9AVhK2vOZ5wyD3Unf95FgN1JZYS0_Pa677W8R8s4b8i5CmfcFfvN_VbeIbjlizGHjme9Y8gztEfSNGUjLiwqrpf_aHET3626gkj73ClzrvfuCPhXAGo0iKEiZ7NIdehq3t0rdWw1MZGI9J7j7IZigX8YFXWQt6jc0pp4NtsTMh55ty4a2F6Yu9Vgr6sjN61xkbHUriYanqaXklYAzu7eB4-GjQJwPGQ92uHuf-kCDGbt8cQc3NpbIMbURvrQgkfvVpjLcU8f6MoENLNXw19aMrhhI4Z-5SX7dV_c_CdX_DHwH3E4cWH_0KBMxPp55gOIp-OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال جوانان عراقی از پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448384" target="_blank">📅 18:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448382">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca2b8c1e5.mp4?token=loXb2sh6XmoI8PBNP0kHXgfOVduxzUDd5RE583dRcESg0Q772ky9TxKnwxl-EKfvXaJLSRYXbyJZEohhmwgqntZ0MYVenwYDB7bGjAeI4zBFTTsbx0gMDPhtQuyJfzfjkmnkqLfXDzrBNQ5FXydhB1weIdL9WEkd7UlkCE9_xWv6emocdBXxCBCX9GrHKXiXmyARx0q5IEwfgCsKZlRWNNfJgFlM4AEFrAJ-LHk-iU-glNzpGYWwvFEQYPJwxAGehFZYEV4VTBNu6ezr8evDON3-4xNq_rFqZDhgs_wH2xbJ60lIwcPMC0MRkktds7M3Z1V5GGxqpbNnnUyBYMWFwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca2b8c1e5.mp4?token=loXb2sh6XmoI8PBNP0kHXgfOVduxzUDd5RE583dRcESg0Q772ky9TxKnwxl-EKfvXaJLSRYXbyJZEohhmwgqntZ0MYVenwYDB7bGjAeI4zBFTTsbx0gMDPhtQuyJfzfjkmnkqLfXDzrBNQ5FXydhB1weIdL9WEkd7UlkCE9_xWv6emocdBXxCBCX9GrHKXiXmyARx0q5IEwfgCsKZlRWNNfJgFlM4AEFrAJ-LHk-iU-glNzpGYWwvFEQYPJwxAGehFZYEV4VTBNu6ezr8evDON3-4xNq_rFqZDhgs_wH2xbJ60lIwcPMC0MRkktds7M3Z1V5GGxqpbNnnUyBYMWFwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشایر عراق در حال تشییع پیکر رهبر شهید امت در عمود ۶۰۰ طریق نجف به کربلا
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448382" target="_blank">📅 18:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448381">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7a09d41ff.mp4?token=VZXHTL7dCx6iiO6Ap19F0rcaU3LAjP25zKZpSph1m84GpONS6GOWkpJ9goBx11HlEvSZx4G4T7aZh6KiW6T6tXZK60Xyj6TVIERxyo58AQ7n0i3wlWgMQpZj8WSYvL7KO8eQZsQ9NkFgE4MkE8STgaz-JfgezSJOnigmBKmztGT2EiTLv6KGMP53BQoo1VAvp8wI1lKF88EgIM_3Pa9A5ouI_tVcbFJrZrQ6luBhVdm9yNetvHP8krocojOzwKjMqqzw8L8FHioEp1jAMk1QGtbhGPBMJ9ewq0TOnK4eAaBWSIHRpDlHtXwbmqIWnJS26FOOVUYZX4OUgFA85SmteQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7a09d41ff.mp4?token=VZXHTL7dCx6iiO6Ap19F0rcaU3LAjP25zKZpSph1m84GpONS6GOWkpJ9goBx11HlEvSZx4G4T7aZh6KiW6T6tXZK60Xyj6TVIERxyo58AQ7n0i3wlWgMQpZj8WSYvL7KO8eQZsQ9NkFgE4MkE8STgaz-JfgezSJOnigmBKmztGT2EiTLv6KGMP53BQoo1VAvp8wI1lKF88EgIM_3Pa9A5ouI_tVcbFJrZrQ6luBhVdm9yNetvHP8krocojOzwKjMqqzw8L8FHioEp1jAMk1QGtbhGPBMJ9ewq0TOnK4eAaBWSIHRpDlHtXwbmqIWnJS26FOOVUYZX4OUgFA85SmteQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قطره‌ای از اقیانوس حضور مردم تهران در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448381" target="_blank">📅 18:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448380">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc90bc8181.mp4?token=esb06ZRENcIl_EXtBz2M79UPwMWw_AGujZUIFMX0wLuhQfNEPmIPio_-9ZpL7BQcCDiCBNMDZHOkKF7au5xJvqX6MwJR-wzGc82o9ZR61kOnps9q50WyrXRQqaroqH-9GtkorQM2tnACzgOHbUazf_DlaFnLZHfl7-g4pxquOnGJ6bLHWGyY6urpwEKr7ZwQP6OQBVUWh51C1vYkZbNp0OX3QrMko6yvBKAG3YLF4rF-GgEj0VSGCAWyDuY626SkMVw1oSScr7mf6x9nnmk8SxO4xuyizsv2RlVUpJRrMwhdJYubiesNtlRuJH0CHSwy3W0F1_nVcFOXP59qrLH9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc90bc8181.mp4?token=esb06ZRENcIl_EXtBz2M79UPwMWw_AGujZUIFMX0wLuhQfNEPmIPio_-9ZpL7BQcCDiCBNMDZHOkKF7au5xJvqX6MwJR-wzGc82o9ZR61kOnps9q50WyrXRQqaroqH-9GtkorQM2tnACzgOHbUazf_DlaFnLZHfl7-g4pxquOnGJ6bLHWGyY6urpwEKr7ZwQP6OQBVUWh51C1vYkZbNp0OX3QrMko6yvBKAG3YLF4rF-GgEj0VSGCAWyDuY626SkMVw1oSScr7mf6x9nnmk8SxO4xuyizsv2RlVUpJRrMwhdJYubiesNtlRuJH0CHSwy3W0F1_nVcFOXP59qrLH9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقای شهید در مسیر پیاده‌روی اربعین
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448380" target="_blank">📅 18:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448379">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFGhniPfqmcGUFEz6V5uh0wVkMX_r3NMelbVXEVDHe9Gl6uuD3hNKjTRYZMHdHIaSr0Y-f3xF__giAMeRVp5K0V2MK9aCBHdcpjcCVqOmfmwzHi6FQcL8lPfqaHGxqhrfe29IYL4cXWUkawCysKvHQbGbZID7iOVhb7zMbkAl1WrJKemroSRCznjUVr15HYy920JTqGCHHEiyb3cLcsc2TOaWSXen9qeUa7CGFbb_f_CKunEbWEPTCcRaeKax7bMHJT3bC2I3YfQOrtQgJGnaeyQqWXrqj3mveLNiSJ9yb4Nb-tPGNcKWQPc17oaD8hm74CWnEKZQQQjn0pBNsgOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سقوط مشکوک هواپیمای پاکستانی در دریای عمان
🔹
ادارۀ فرودگاه‌های پاکستان از سقوط یک هواپیمای باری با ۵ سرنشین در دریای عمان خبر داد.
🔹
طبق این گزارش، این هواپیما ساعت ۲۱:۱۸ به وقت اقیانوس آرام از شارجه به کراچی در حرکت بود، که مشکل سیستم ناوبری را گزارش کرد…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448379" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448378">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnG5Y4ONa-4j6IB1mOYJJi_DKc0lzwdvwvnkpOt5BHS1uhFlxTJllIi5goDTrRBdtBaxUyuVFplsrPOS_LqHy90V1vmmwGidz3IftKj5HXOQxwfRCfdLynMBRI3Q6W5nfbZZ_sOmxu8FeiEFwYYOOtRAdrzYOvP4-F9QMxSGGl00ozd0JbOyXNikOlcfNg_xyVFcooIN2-YDQlIXHOUd-R2jKWfnUigGQ2c3dEPCAyhT60Ra595_NWaoMHdqYHBUvcXVp1u1BnkSIGSZoauRQUsh5rSDntgSfBpL7ph-h5xjEriMCrOdf-7NksomzgG9A7yZ_RKv3rbjFFlPvZOPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه شماره ۳ آستان قدس برای مراسم تشییع رهبر شهید انقلاب در حرم رضوی
🔹
آستان قدس رضوی به منظور میزبانی شایسته از زائران شرکت کننده در مراسم تشییع و خاکسپاری رهبر شهید انقلاب اسلامی و دیگر شهدای گران‌قدر از خانواده معظم ایشان، مجموعه‌ای از خدمات ویژه را…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448378" target="_blank">📅 18:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448377">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43d505f40d.mp4?token=bzLhW62gQvfU1XQd0nEUU9DjNsWOyqeZ2_d8TORHQmIJwMRGUIpTMj_BiboHJZX4gh38VDRE3pxfE0i4eg9Bz2Re3seMhbZqt1L3LT966o3YjMbR5TcrN_MJ5uEFAcnIqE3k8yPpETU15QHhflW_HSun7NJR3K3rLzi7Xp_p00Qy2w5jcBicJrKC7Aifr5HJ0lJZp8esePIKJgWjdqDZLjwTB2Z75poCVI6N3Lza1Db9ZdabOLcB4jrQeWi_tHuPqD6a-4RfkzmbUvrFhbew6SDHxffsi9LrGSPgWOiWlg-E3DzBtg8uXNaB6QqT0rOZplLu2MM-JPUXk5N-xu0-nHs5bSUPNfuiDAdlKaQZD1Bb9gYucBVgP-bj-7e1Ii95bX6a8eZc7RtBLLvHjD_xeYtMUpHspHLxQKB-3ci6FKJpvJaYoDpuMz0PLQZgmyEOOJGqP5pmVBZFeNV9EO9jXL34ja1qgQT4klSRS-Hx_GHlDKa1klJ1HmfpavSx5e7foVGSSF7jX3mg0bezycqS6op4-qOdgBcJZTc_u-TYEJsk3ilQ-1O4_orYFGfP2wigHZ7nZVIL0sjMMtIdg3vvbYZnBGTO2aTz5dyR1bQ_A9UfQaWfzrSsO_8tw3q02Kc9HU8G1BNUHqggC6Zs-MyJ1t69x-uNiG12wpj2k7JXxHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43d505f40d.mp4?token=bzLhW62gQvfU1XQd0nEUU9DjNsWOyqeZ2_d8TORHQmIJwMRGUIpTMj_BiboHJZX4gh38VDRE3pxfE0i4eg9Bz2Re3seMhbZqt1L3LT966o3YjMbR5TcrN_MJ5uEFAcnIqE3k8yPpETU15QHhflW_HSun7NJR3K3rLzi7Xp_p00Qy2w5jcBicJrKC7Aifr5HJ0lJZp8esePIKJgWjdqDZLjwTB2Z75poCVI6N3Lza1Db9ZdabOLcB4jrQeWi_tHuPqD6a-4RfkzmbUvrFhbew6SDHxffsi9LrGSPgWOiWlg-E3DzBtg8uXNaB6QqT0rOZplLu2MM-JPUXk5N-xu0-nHs5bSUPNfuiDAdlKaQZD1Bb9gYucBVgP-bj-7e1Ii95bX6a8eZc7RtBLLvHjD_xeYtMUpHspHLxQKB-3ci6FKJpvJaYoDpuMz0PLQZgmyEOOJGqP5pmVBZFeNV9EO9jXL34ja1qgQT4klSRS-Hx_GHlDKa1klJ1HmfpavSx5e7foVGSSF7jX3mg0bezycqS6op4-qOdgBcJZTc_u-TYEJsk3ilQ-1O4_orYFGfP2wigHZ7nZVIL0sjMMtIdg3vvbYZnBGTO2aTz5dyR1bQ_A9UfQaWfzrSsO_8tw3q02Kc9HU8G1BNUHqggC6Zs-MyJ1t69x-uNiG12wpj2k7JXxHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم عراق مقابل ماشین حمل پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448377" target="_blank">📅 18:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448376">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4855ecd8.mp4?token=DuTWZlpYfYFNnZ_Naj4vgoG-vL1aXO6BSTBUXPKhYS-Yffz8bMPDHGCV8P8ntHjcP46wx9a9hAhrbDC2gf9VjKhGQgTXl2FFFODbJAChchSwgHY6UrnnTdbOsR9bJAKph-qAtsDib1I3_AbONUy8e-o8R5VnNJi5yX_VBUDvYLoj3j3cp_bHDv9duItjSaUdSobx8GITVDcay-HVOBvXc3V9RJg3w84QA429sGEzUMz_tMh2di6q9dqwz6lWn0j0JC7lnqacGlrTv501pNENrxO664d6_d4MKUTNk4RIilF2IkKwamdetm6LhG2s4zKFsgkF7YfU7EwR1dJ47xSKow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4855ecd8.mp4?token=DuTWZlpYfYFNnZ_Naj4vgoG-vL1aXO6BSTBUXPKhYS-Yffz8bMPDHGCV8P8ntHjcP46wx9a9hAhrbDC2gf9VjKhGQgTXl2FFFODbJAChchSwgHY6UrnnTdbOsR9bJAKph-qAtsDib1I3_AbONUy8e-o8R5VnNJi5yX_VBUDvYLoj3j3cp_bHDv9duItjSaUdSobx8GITVDcay-HVOBvXc3V9RJg3w84QA429sGEzUMz_tMh2di6q9dqwz6lWn0j0JC7lnqacGlrTv501pNENrxO664d6_d4MKUTNk4RIilF2IkKwamdetm6LhG2s4zKFsgkF7YfU7EwR1dJ47xSKow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای انتقام، ‌قدرت تو را می‌خواهیم یا مولا؛ خون در برابر خون
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448376" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448375">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d6b642ee.mp4?token=gerGHxoENnv6pN1WsvI54MKrB6-T0YFK5Em7ZgE1XjDj0A1vVL1Z_CYf0lokkxlO_Z5K92CIXt0sG7Srsrx3tXbdsSwcvp6MHFwEba5qpt-FtcBg9iEEBx_1wPvFIGUvkJsOBjpZAbZ0BNRgALAnmc9V4tMFOyotuUGBvKNQb6VAuAUdHj53JKdlbdw23vVL860nCueGSgNJsFbntC08o3hLVc8Dz1EN3ULuXj4Rtzy7L0OLS5W2I3m6dzaGHC2AD7B9AEJxZGQGbYO8RAk-BWhzo9TdDkt-QSr1OsYSOxZTL9Uwz3Y54umb0FHJOgqpDkg98YaQ6tDYVR4qHGZYMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d6b642ee.mp4?token=gerGHxoENnv6pN1WsvI54MKrB6-T0YFK5Em7ZgE1XjDj0A1vVL1Z_CYf0lokkxlO_Z5K92CIXt0sG7Srsrx3tXbdsSwcvp6MHFwEba5qpt-FtcBg9iEEBx_1wPvFIGUvkJsOBjpZAbZ0BNRgALAnmc9V4tMFOyotuUGBvKNQb6VAuAUdHj53JKdlbdw23vVL860nCueGSgNJsFbntC08o3hLVc8Dz1EN3ULuXj4Rtzy7L0OLS5W2I3m6dzaGHC2AD7B9AEJxZGQGbYO8RAk-BWhzo9TdDkt-QSr1OsYSOxZTL9Uwz3Y54umb0FHJOgqpDkg98YaQ6tDYVR4qHGZYMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار عراقی‌ها: یاحسین(ع) پسرت سر خم نکرد
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/448375" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448374">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8152564799.mp4?token=Vxffk6CsTsI9AB01vPFgLOtp8m-2z8N6VXcXRJE_frLfE0-rH_WaEyG-MHOa1-153Rw1ZGyC1ul36xDePGCabjRs8OXKxXzZLiljwots3xkWl1iXgPBUOWPXeUXV236qawEZzz3mdx5nWWOnkgU8vVNfMN4exVDUAJZtCEVGG_Eu_0uTvkU6hx4SfjgT9E8nryqsz6BrWPvfzqvBJbuWjwopMGLNBzpu7YNs3Mv23w14HbxcDyQsOjUiFVE-cc-U4aRIKjrpI4BC94jxR8tgojKXd5YEXiFYc6hC3TUo6KLwaUISa7e_KHQ3zdB6CI3sxxIRzKsSp0a3lwkS5rjzxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8152564799.mp4?token=Vxffk6CsTsI9AB01vPFgLOtp8m-2z8N6VXcXRJE_frLfE0-rH_WaEyG-MHOa1-153Rw1ZGyC1ul36xDePGCabjRs8OXKxXzZLiljwots3xkWl1iXgPBUOWPXeUXV236qawEZzz3mdx5nWWOnkgU8vVNfMN4exVDUAJZtCEVGG_Eu_0uTvkU6hx4SfjgT9E8nryqsz6BrWPvfzqvBJbuWjwopMGLNBzpu7YNs3Mv23w14HbxcDyQsOjUiFVE-cc-U4aRIKjrpI4BC94jxR8tgojKXd5YEXiFYc6hC3TUo6KLwaUISa7e_KHQ3zdB6CI3sxxIRzKsSp0a3lwkS5rjzxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
و خداوند دعایت را اجابت کرد
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/448374" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448373">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864d75da4.mp4?token=nkY-wKSQ--aSLUPNEODx6YFy-BXFL3xW-YcCVlgJcgxlbXgqG7bCgJEZcPyknqOQr3ewV1Hykt7BqypcEniUSNsPei-gO30zdMad_3dPbdwurMSWlAuLHQCqBgTTM2S_n2oLtol-qWCCbiMh7MOW2Nv6gAeSfasFxrPOcYgo_CU_hiIjYsB7U-it16LU5uQfGCgEAjc0KOJIf3yr7qFVjWxBvHHn1k5mDLK6bvuPJp2A5sRSoe4UfUufVSYzOwIrjuqZaJfaJqZ323UvOBcwTBPvhwxNe9tif0cT_PFSTrEoDap8AhyttAdGDSqTZbpPKL4lTzh8XR4yx0VT6wop7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864d75da4.mp4?token=nkY-wKSQ--aSLUPNEODx6YFy-BXFL3xW-YcCVlgJcgxlbXgqG7bCgJEZcPyknqOQr3ewV1Hykt7BqypcEniUSNsPei-gO30zdMad_3dPbdwurMSWlAuLHQCqBgTTM2S_n2oLtol-qWCCbiMh7MOW2Nv6gAeSfasFxrPOcYgo_CU_hiIjYsB7U-it16LU5uQfGCgEAjc0KOJIf3yr7qFVjWxBvHHn1k5mDLK6bvuPJp2A5sRSoe4UfUufVSYzOwIrjuqZaJfaJqZ323UvOBcwTBPvhwxNe9tif0cT_PFSTrEoDap8AhyttAdGDSqTZbpPKL4lTzh8XR4yx0VT6wop7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بین‌الحرمین قبل رسیدن پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/448373" target="_blank">📅 18:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448372">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npNkNmtZxueIx3eo3W0ARnH62B4zdjAgH3n-UIl0ewBn3ZaTnbR3jlokbzYHInaylJhPLpkSSsGYFvsn5g-F44CmdcP6ShnPtoHHITPntQRQZS7NmuuKEQ6HR7pGwpbR-LUJedDwEPvjHKEvXdH-XZZhNt6UXD6Uri7hvQWc4NGvjXRb5bMo3xKsAhJfRr_E7_TzhIq7U7YXSTHViz3UB3yP0ktLuzxYQY1ht-SV4AvA19aXTqSW8UftV9zSG56mMgbKUprxFZjUpre9bTa9FWjAhjot1Cim1e5aJ8sqTKtayBu_oif0Sq2s7_PYPp85HREqDjGhU7HtPcQjN_yJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر رهبر شیعیان جهان در دست نظامیان عراقی‌
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/448372" target="_blank">📅 18:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448371">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-text">🎥
حال و هوای عراقی‌ها وقتی متوجه می‌شوند آقا ۷۰ سال کربلا نرفته بود
@Fars_plus</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/448371" target="_blank">📅 17:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448370">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=iqWZ1ICNX1MqBs1Nif1CzfWaHl7da85U-RXo713yc5gW1KZvtRyd819cjVu_m34grzfroyVTlzpvDXbt1Jp3RNBPW-wGLaIXM42IAaTmfJJxRmlvcEI_d48qDDrfCVud5jnWHfpB-vrAB3HgXm-3do5y6URCWUjd0ZRqSlxlSouEa-HX6ifjJ9zReHXOm9fnTlCzSWaKURdK-qHJGmknv6MY3i9inwDXxc8_wi29-qUas4R1LI2s6NRmRJxM_UuK-_F5ihMRiuHutaZJ7uRCYGSDAiSNOPOb-y447u5_kD42d-H8TUnw_rw4YmJvBPaH8iGXokRDZqDofUCZNORL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=iqWZ1ICNX1MqBs1Nif1CzfWaHl7da85U-RXo713yc5gW1KZvtRyd819cjVu_m34grzfroyVTlzpvDXbt1Jp3RNBPW-wGLaIXM42IAaTmfJJxRmlvcEI_d48qDDrfCVud5jnWHfpB-vrAB3HgXm-3do5y6URCWUjd0ZRqSlxlSouEa-HX6ifjJ9zReHXOm9fnTlCzSWaKURdK-qHJGmknv6MY3i9inwDXxc8_wi29-qUas4R1LI2s6NRmRJxM_UuK-_F5ihMRiuHutaZJ7uRCYGSDAiSNOPOb-y447u5_kD42d-H8TUnw_rw4YmJvBPaH8iGXokRDZqDofUCZNORL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر شهید لاریجانی در دست عراقی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/448370" target="_blank">📅 17:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448368">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58433e38f.mp4?token=TdJVJMuFGswhh0z7Hzyv7Z1uG6P1zzsRkRUfAzvd3kerGsx-MpN_-bmvcCLGpDX0rGMH263lKdlSigpxgJy1VTnRDrChv-VjwA1-amTzDlUY_4bC6PczLLuXrsqJwKD_9Hxm5867CeFd1TtjhoSAAlh1aHVOA4_Y10DaOwBeAc8lyCGiObXtKa1W-gteJ26dDhJHZq7vsUuA18gzEVSd8c0EdKb1Sva2qnM1F6B7qEShfGJdoyoCZvYAhhcn3Ak8LxljLl2-74IJwcwj9rRtlNBKjwDsvjWTOBL_MdFJzssZH-oFZ_ks1vreqRYWSPeglyOtK1JNDCexBQCBJgGiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58433e38f.mp4?token=TdJVJMuFGswhh0z7Hzyv7Z1uG6P1zzsRkRUfAzvd3kerGsx-MpN_-bmvcCLGpDX0rGMH263lKdlSigpxgJy1VTnRDrChv-VjwA1-amTzDlUY_4bC6PczLLuXrsqJwKD_9Hxm5867CeFd1TtjhoSAAlh1aHVOA4_Y10DaOwBeAc8lyCGiObXtKa1W-gteJ26dDhJHZq7vsUuA18gzEVSd8c0EdKb1Sva2qnM1F6B7qEShfGJdoyoCZvYAhhcn3Ak8LxljLl2-74IJwcwj9rRtlNBKjwDsvjWTOBL_MdFJzssZH-oFZ_ks1vreqRYWSPeglyOtK1JNDCexBQCBJgGiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احترام نظامی پلیس عراق به ماشین حمل پیکر رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448368" target="_blank">📅 17:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448367">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=XXo-_8iKqfC9nkhxxqae2mYJLN2ghlcG44X1iagm1xlvU0llarlB9LGF719hB_g826rShamErXG88wZpJ_LtCQ3eN-g_Lz6jFwIgo-3esTeASjc9mqwnl8dw2J-IIYkrJgEfHFGW-hC6P6YfuWFwoEOpG30qFJJyrdwUsZ9NAyyKMUj8nX5VvFM5EptGg1ayx7H2DRS59GNMO9GJrkkkeOoqe0AFlALH-47lb5QlBeBFJD8ycaBFGmlTBUihQqV2Va3NGRGDuBqzY2Jq5eCKimbST57h8-orb9NjiRzO0R2Ue45_oOP-sIuHR6cwgROGr6Rok-OEbANM8CENZZmEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=XXo-_8iKqfC9nkhxxqae2mYJLN2ghlcG44X1iagm1xlvU0llarlB9LGF719hB_g826rShamErXG88wZpJ_LtCQ3eN-g_Lz6jFwIgo-3esTeASjc9mqwnl8dw2J-IIYkrJgEfHFGW-hC6P6YfuWFwoEOpG30qFJJyrdwUsZ9NAyyKMUj8nX5VvFM5EptGg1ayx7H2DRS59GNMO9GJrkkkeOoqe0AFlALH-47lb5QlBeBFJD8ycaBFGmlTBUihQqV2Va3NGRGDuBqzY2Jq5eCKimbST57h8-orb9NjiRzO0R2Ue45_oOP-sIuHR6cwgROGr6Rok-OEbANM8CENZZmEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برافراشته‌شدن پرچم «یا لثارات الخامنه‌ای» در خیابان حرم امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448367" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448366">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc919fb2a.mp4?token=sz56g_7Vouc59BPZatNslg3c6tEBdGYpcWsw8G8ulZz5ip4IzIdIkEqH8eQXgNnfHjlPlhkmr24O4bI8f73SXHXlAn35p1zeKPSLLqGnH0VKE3M1sdxnAMU3j_0IoJaPUy2UXNa6zb0Q-qVG6WceQkSv0UQptPACTf3Q7XWKKhZTFVr6d7LdboBOO8X6AkmO6FeURD6fcIp2jeWajRKxYlnBRPg_hlCFkVMKX4SD1R6pFNZ67WDRH75wjAfXOUGG-EnAo0VzshnSm6wnGESr8qAYtZMV5Pq2_XFXeLDBC0H4nvV0lsOMLw7yQwAvTgYs2Bb51MeODmKu5mwfQXCpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc919fb2a.mp4?token=sz56g_7Vouc59BPZatNslg3c6tEBdGYpcWsw8G8ulZz5ip4IzIdIkEqH8eQXgNnfHjlPlhkmr24O4bI8f73SXHXlAn35p1zeKPSLLqGnH0VKE3M1sdxnAMU3j_0IoJaPUy2UXNa6zb0Q-qVG6WceQkSv0UQptPACTf3Q7XWKKhZTFVr6d7LdboBOO8X6AkmO6FeURD6fcIp2jeWajRKxYlnBRPg_hlCFkVMKX4SD1R6pFNZ67WDRH75wjAfXOUGG-EnAo0VzshnSm6wnGESr8qAYtZMV5Pq2_XFXeLDBC0H4nvV0lsOMLw7yQwAvTgYs2Bb51MeODmKu5mwfQXCpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمعیت حاضر در بین‌الحرمین در آستانه مراسم تشییع پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448366" target="_blank">📅 17:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448365">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e9748c01.mp4?token=IAtAVznRfMzO5WOZKDlsmGqXDtUVBe2Sdk73PxIsh0EZZ7RPLH5jFEzabDe9q2By9AwSJDCHnawh_HoWGBNr0zL4phOCokERj3-wcWSejZHSE7B7dbLfxJ63bUl-9JZzzRu6aHTu5WMMg1slECcYb4Um3ZktdNreXHsVzTVdf4EiRXo036jyVeH3jmoWu_2g6_wJSUrUPGEFhgvjNdydSiyCPmkJNAntv51zkhWMU8WIfdWARVMrz1dLzfk2M-1oKhiWclfagi88wToEStlTN-gX7DEFM06Hirk5TrbNaqA5UhuxE84Z7aKNITeZWc7TISrXxEcQHmj7zwbS_EqZLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e9748c01.mp4?token=IAtAVznRfMzO5WOZKDlsmGqXDtUVBe2Sdk73PxIsh0EZZ7RPLH5jFEzabDe9q2By9AwSJDCHnawh_HoWGBNr0zL4phOCokERj3-wcWSejZHSE7B7dbLfxJ63bUl-9JZzzRu6aHTu5WMMg1slECcYb4Um3ZktdNreXHsVzTVdf4EiRXo036jyVeH3jmoWu_2g6_wJSUrUPGEFhgvjNdydSiyCPmkJNAntv51zkhWMU8WIfdWARVMrz1dLzfk2M-1oKhiWclfagi88wToEStlTN-gX7DEFM06Hirk5TrbNaqA5UhuxE84Z7aKNITeZWc7TISrXxEcQHmj7zwbS_EqZLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیون و زاری زنان عراقی برای زهرای ۱۴ ماهه شهید جنایت ترامپ قاتل؛ هنگامی که پیکر او وارد حرم سیدالشهدا(ع) می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/448365" target="_blank">📅 17:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448364">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVJ-cuoTMwdahAfZm3snku6mP7ahj4l4CvsbAuCSS8eI0zRG3_Wt7DICVria7ItEANY66aSR_7p1FY39IaVRY4upsBhqISWgnU0bvLNOjU7z8bYdkQfrbaZ_xXin3PA1MfPv4UxFdcGZhcsd9tpb-OCdeqRa2D-T6alK-NMjYHdTZRtWnSAFDibMmvAoicTiRWCx9OQ1SgHxsUcPMmgLKO4g14xlpChredQg5qIEKrE-92Mt9ICku1ARbYJrgLDBb5OKZKFHG9PSJYZkUJFRlANOQJIGY_uvre1N9AGNYQuW6zCPb_0IFddeCLEAmDsL51odpNGSTXDUckqBjl9rcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس یادگاری با تصویر حضرت آقا در بین‌الحرمین
🔹
هر جا عکسی از حضرت آقا می‌بینند، جلو می‌آیند. با احترام، با لبخند و گاهی با چشمانی خیس می‌گویند: ممكن الصورة؟
🔹
در تمام سال‌هایی که خدمت به مردم، فرصت زیارت را از او گرفت. بارها آرزو کرده بود به زیارت برسد، اما نشد تا رسید به امشب، به سلام و وداعی با شکوه در میان مردم عراق...
🔗
حال‌وهوای عجیب مردم کربلا در وداع با رهبر انقلاب را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448364" target="_blank">📅 17:45 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
