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
<img src="https://cdn4.telesco.pe/file/hqN87zEFu03QJ5rnfrJdOOX7D-ZabTKlfLlAZb-SCgBCpGgejOUWrb5jYD0uUbcEm_VMfkyz6uCAFdSWq8kipZ8oWWXz4Faky4pJ-LeWKPDFkztigVbCjEU6krbVPPyjJgJ07nvzZdRLz3lVEyvQJAseVk1SH2h1sJSYuONlz4W8Z771hp5YpQP_XKpwHfMJOU_-cOXtHwnmx03CgrHAV602ZGbSF1jqSccbPbFimzRnri6qsa6WB9IXeb3LQV6JiY4YV_Ohw2BRaJIN82H_QaXPRar3Abvzp6PwRckIf_QuGOwk9dXMi-z2GJS30bW87thNnid76LdytIwGU76mGg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 14:30:57</div>
<hr>

<div class="tg-post" id="msg-83303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ درباره حمله به خط لوله نفتی عربستان:
ایران به احتمال زیاد مسئول این حمله است!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/funhiphop/83303" target="_blank">📅 13:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83302">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efdf4abb9.mp4?token=DhDawXX9mew_YcwzWc2fK0zXkNsoU8hSdBl6KkTRBUIMxt5rbc64SfZ5V9QwTOcF3Lci-wxw98voH0CPz6MGaa6BXQR8u8OiXJHT2uhG1nzGwouCoitU4By3M4qo2MW3CHrP44GZN-Dax0i6rwxmzNWPqrO9mOSv0yBCvKJ_ZEaerSmxM25ytbb6LY3tLR1aOrxL4YGUq3PgdhNL8DrKl2c2TWvatORCSCp1DC0AkkpV8mDvPRsefN9SphN-EOKyxgtIBXjyx7THTL6GAxiyfEeePsLm547OYH6R38EfuoxIpH-A-7SKHis2L06mbL0mjvLo3q6tlEKIC5e3HYelQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efdf4abb9.mp4?token=DhDawXX9mew_YcwzWc2fK0zXkNsoU8hSdBl6KkTRBUIMxt5rbc64SfZ5V9QwTOcF3Lci-wxw98voH0CPz6MGaa6BXQR8u8OiXJHT2uhG1nzGwouCoitU4By3M4qo2MW3CHrP44GZN-Dax0i6rwxmzNWPqrO9mOSv0yBCvKJ_ZEaerSmxM25ytbb6LY3tLR1aOrxL4YGUq3PgdhNL8DrKl2c2TWvatORCSCp1DC0AkkpV8mDvPRsefN9SphN-EOKyxgtIBXjyx7THTL6GAxiyfEeePsLm547OYH6R38EfuoxIpH-A-7SKHis2L06mbL0mjvLo3q6tlEKIC5e3HYelQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی این چه اکسپلوریه من دارم آخه
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/funhiphop/83302" target="_blank">📅 12:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83300">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اگه رپ آمریکا به کیرتون هست، باید بگم که Lil Durk تبرئه شده و قراره آزاد شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/funhiphop/83300" target="_blank">📅 11:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83299">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یه گزارشگر تو شهر وان ترکیه تو یه گزارش خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده جواب هاشون رو ببینید  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/funhiphop/83299" target="_blank">📅 11:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83298">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e472b3e6.mp4?token=RQg0tGUAakwH00rzjZhe-tPmqEomB0w31ZTwWxQO79xbRiCoudDU0Oj84LYd5xGOfbK9Tob6keVqvNCUVeaU1L_PuzSSBnR4kND2zMkp9stwm1y8GnHtg7fP7ljcIbP3Ul-jw-n3ehGHw8aU-kcIdBXVGrlk6XCkX1eazcoJ3AnXhRcqkG2cnQnxADl11FUk_K0uAVtluFqaAZTRZUzH_of6v-jugmy0tYI4Wzxq8QpIh6HvY0r9SN623An7jxuS9c4HxAQLYgMx2gJKvgULeNVEn-wB2GV6CwH2BbI7fruV4oFJ1MIcUwpve3PhZN_3VaS4bcKUpXVlAokX6ID9LFDu02eYw1dOJ-VNNOfP4qBk4546phzUNYqejHSwbdnbpv3Q0NswWDIjvWwZQvD-fq1Lp2sAiRVq2fE8Ly9inJkYymD3cg1t-jRNGVeA7ktlgHAtc6_Zo1S8DZTEC02QPTp5ZR921WtYbTf7JGHKc0T6k4Tl7cpp6MIH9wFEU6BRzLI61X1opmP4KDGfvL_61c-lXodpZcg7u0FpFqQqHelno6WIhu_-f0utwK5_ax0Iqk8eUqTwFlcJ6LWVnniBPWKGzXhKqc9-3VqqJH6DLx-cwV80v_nprqKZG-_Y4ngvecaOmRwXSLFD8ggZoMm1LiZmsRqjKmBaC2RodUxoY2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e472b3e6.mp4?token=RQg0tGUAakwH00rzjZhe-tPmqEomB0w31ZTwWxQO79xbRiCoudDU0Oj84LYd5xGOfbK9Tob6keVqvNCUVeaU1L_PuzSSBnR4kND2zMkp9stwm1y8GnHtg7fP7ljcIbP3Ul-jw-n3ehGHw8aU-kcIdBXVGrlk6XCkX1eazcoJ3AnXhRcqkG2cnQnxADl11FUk_K0uAVtluFqaAZTRZUzH_of6v-jugmy0tYI4Wzxq8QpIh6HvY0r9SN623An7jxuS9c4HxAQLYgMx2gJKvgULeNVEn-wB2GV6CwH2BbI7fruV4oFJ1MIcUwpve3PhZN_3VaS4bcKUpXVlAokX6ID9LFDu02eYw1dOJ-VNNOfP4qBk4546phzUNYqejHSwbdnbpv3Q0NswWDIjvWwZQvD-fq1Lp2sAiRVq2fE8Ly9inJkYymD3cg1t-jRNGVeA7ktlgHAtc6_Zo1S8DZTEC02QPTp5ZR921WtYbTf7JGHKc0T6k4Tl7cpp6MIH9wFEU6BRzLI61X1opmP4KDGfvL_61c-lXodpZcg7u0FpFqQqHelno6WIhu_-f0utwK5_ax0Iqk8eUqTwFlcJ6LWVnniBPWKGzXhKqc9-3VqqJH6DLx-cwV80v_nprqKZG-_Y4ngvecaOmRwXSLFD8ggZoMm1LiZmsRqjKmBaC2RodUxoY2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه گزارشگر تو شهر وان ترکیه تو یه گزارش خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده
جواب هاشون رو ببینید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/funhiphop/83298" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83297">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6LarM4cb4PIYlvXM_QnIGvDG9jIH6bpw1SG49aLTM72nM009QSxGvJKWmhVpRBP_o2ChXILWHtE5W-KaMiBPYPmWe8fKMuOIIQ8tgE_DpG-BC4n7GQBCxftcTYCiaRGOiOPl6odGfLW9srbbEj2xz5px7yuwd8eXAyhoj735mPuZ2GEgd3ek1t5wjFzDRCvBgqU3dnaXZYGQDS6WqMQ3fiUQ1VDU_nf3JtpP84DU90JDl5eV0V2jd8CGcDiC4LsvFf1_n6pbG0MJjyEXboQq_IPUzn85cE190tBM3cmCadnye6TOJklArfowQ3zOyP6GnApnJRed0IjUkkalZTIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
شارژ کن، هدیه بگیر! بونوس فوق‌العاده ۴درصد
⭐️
💰
۴٪ بونوس نقدی روی تمام شارژهای حساب دلاری!
💰
🚀
می‌خواهی با سرمایه بیشتری وارد بازی شوی و شانس برد خود را چند برابر کنی؟
🚀
از همین حالا، با هر بار شارژ حساب کاربری‌ات، ۴ درصد بونوس نقدی هدیه بگیر! این یعنی پول بیشتر برای شرط‌بندی، هیجان بالاتر و شانس بیشتر برای پیروزی در بازی‌ها و پیش‌بینی‌ها.
🎯
💥
چرا این بونوس را نباید از دست بدهی؟
✅
اعمال خودکار روی تمامی واریزی‌ها و شارژها
✅
سرمایه بیشتر برای ثبت فرم‌ها و بازی‌های کازینو
✅
فرصتی بی‌نظیر برای چند برابر کردن سود
🃏
همین حالا حسابت را شارژ کن، بونوس‌ات را بگیر و شانس خود را امتحان کن!
🌹
کازینو رامسر جایی که هیجان بازی هیچ‌وقت متوقف نمی‌شود...
🅰
r21
🔗
ورود به سایت و شارژ حساب:
⚡️
لینک ورود بدون فیلتر شکن به کازینو رامسر
💻
@C_ramsar</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/83297" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83296">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">همینجوری پیش بره ایران میشه نیرو نیابتی یمن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/funhiphop/83296" target="_blank">📅 11:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83295">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">صبح بخیر
مرز شلمچه بین ایران و عراق توسط عراق بسته شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/83295" target="_blank">📅 10:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83294">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شلتون ست اولو که باخت اومدم ۶ بزنم رو بردش، اشتباهی زدم رو تیافو</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/83294" target="_blank">📅 05:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83293">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GL6qi7zo1J0Dxyy6Ye2iU3vHnXViyBAZll4PAJgyAaRv54AKbCYUp6i1n1RhvU590vBbfgQRlgAfeUkz5ZAkQhqoc1Ck2tOJD5KEzjL-qNhsiVaQYZqMP5C-1RrOpRL0oGRunk3clY_yK9JDADEZOliFQwBnR4rl_vrOIPnALz1yqc9wDtM9xoyGY4q30Pm5ru_wegsSW2NJfBFUwamMVlF6FmmFMH18JQpr6LjJV4nsP-oFiVoIQk1VKNJDL0T80UsJUfoYuApM1gZgUUz8UBPcF9qejfmjG7jltDPq3lCM_Y1jAvjZA3usuGHH79sbq1ylbZBvL0A6HF3Iha4nCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلکسیون نمایش زوال عقل با هوش مصنوعی توسط جهان پهلوان کامل شد.
❤️‍🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83293" target="_blank">📅 02:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83292">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckjr0VEY7S6sNTJT1Sh3e09BhdIQSDGssqLlIv-KLNsDWXkv5u2q8yEFHB1GIM2uqbeT78uHljGiZ4e2hwRqXz0gUQwlHB0p6HRLsRnkwePOAWPvzIMZw8i6psaKy-QL45JSQukORnlhph0-3Olg_1ij6qgAn4BgbQJkkYzp4pRKTP-Z8gOVc82rsOAszBdStKBq8RnZWjKY_jFtubUDMJCF8LqQAEDpiO4XDyHZFTGYs-DWX3s23kTnywvy5f6f5UcvqUYnmjxZQ3dxNOVXcMJvzwG5SeDSr_pH9WpiyWok08sUkRtbpGCMaAsKZjDC0kD9xnmSC53xO34P4Xt0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرومزاده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83292" target="_blank">📅 00:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83291">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcjjZ-1S37OhXbKK3Rxw0ghJScrMxw-DM3-eL58m1i1q2KAFSqxT5dJq_a8eOoyKmiyyEFMKjjhAmV_JdqYtM6gGR2gCGgLxxpeQke_kT2nMdwTH9gJThZXeq8m5IgmpZsnLgz-z-LAZF8St_nuVT6LPlfKKaHB_XH5DQBYYR7mHbkcYoh_KmmoWCQkpNRdmY05itPQJ9JAuMJQIhIypcmaQ4SZ0DHSLx8tB4TWxC4OYXYcwCtDh6B7YBcO6XeeuewFTiUsFjMy2CI7tgt3_A8x-6h7tqRMpRQ3pP4UbgHtb4kg9asNpgQMFodveWcquhiYmESbbM7CYmfYtlGMsBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پسر تو کون نرو هه با این دختر اسکیت سواره رل زده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83291" target="_blank">📅 00:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83287">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شرکت آنتروپیک، سازنده‌ی کلاد اومده یه گزارش مفصل از عملکرد و تهدیدات و اقدامات هوش مصنوعی کلاد منتشر کرده که توش یه بخش راجع‌به حکومت حاکم بر ایران خیلی جالبه؛
این شرکت ادعا کرده که این حکومت با کمک مستقیم نهادهای چینی، به استفاده گسترده از این هوش مصنوعی برای رصد و شناسایی مخالفانش در فضای مجازی پرداخته و تعداد زیادی از مخالفانش در داخل و خارج از ایران رو دقیقا با همین روش طبقه‌بندی و شناسایی کرده.
همچنین این شرکت ادعا کرده که این حکومت، از طریق همین هوش مصنوعی، برای طراحی طرح‌ها، سایت‌ها و بدافزارهایی که تهدید یا استخراج اطلاعات و به دام انداختن مخالفانش رو در پی دارن، تلاش‌های زیادی کرده.
ادعای دیگر این شرکت این است که این حکومت، با استفاده از این هوش مصنوعی صفحات مجازی غیرواقعی زیادی ایجاد کرده و از این طریق پروپاگاندای عظیمی را برای خود رقم زده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83287" target="_blank">📅 23:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83286">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">زندگیتونو بزارید رو برد کارن خوسانوف</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83286" target="_blank">📅 22:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83285">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1473c0f40f.mp4?token=STOAfo2ZtSpiCMG3sKgdCdkPpFMd5ESNvau3Go8upzF_SnaTckuBbDpFP1StRHI3tutpXtjKA8RQ6RmLMEr8wqCryn37hEU6gYuNbS98mvAAfKZiJqEuEIjhDpxUNtN1P3Anf8d3yMuFc0q7MN_2XTZXTv-vjY8IosrmwaVc961mPAKlG90xodKCQzz3wZItmxW4ow4veJLmC3qFMdrphCW_7xRDUd1foZYAGYp-P7BpRNNPa2070QAH48VUsHwGjw7lHY7zIHtcC4s6RlKuVJtw8GkeIcIEbrhwtfjUZ85rexLOoPqHKc71V6H3brvSEFGEqjBglL_WcTC4yuQCRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1473c0f40f.mp4?token=STOAfo2ZtSpiCMG3sKgdCdkPpFMd5ESNvau3Go8upzF_SnaTckuBbDpFP1StRHI3tutpXtjKA8RQ6RmLMEr8wqCryn37hEU6gYuNbS98mvAAfKZiJqEuEIjhDpxUNtN1P3Anf8d3yMuFc0q7MN_2XTZXTv-vjY8IosrmwaVc961mPAKlG90xodKCQzz3wZItmxW4ow4veJLmC3qFMdrphCW_7xRDUd1foZYAGYp-P7BpRNNPa2070QAH48VUsHwGjw7lHY7zIHtcC4s6RlKuVJtw8GkeIcIEbrhwtfjUZ85rexLOoPqHKc71V6H3brvSEFGEqjBglL_WcTC4yuQCRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید سروش هیچکس.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83285" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83284">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8742f867a0.mp4?token=PiVUQG3Qx7I06t81sJYpuYPUvCWXGjk6IrY6iRGjNIdiMaUCmqEI5gRX6QXtf59cDssZCAZg4co7pLWvPZnq9JJH7FeaRc9bvz2TFKXOC5AYZtZhyaRyR5jnB3DWd1dX3aWu7vgPe6ki9tFHQHaU1PpPWtoboz22SVAjQk_wZQxmyrpRvFXWhhs7sv3LocXEDJ86b1QzT8ipM3hggF4oschh35PugOdR0GJiImvHV1x7xFsRhxWvT4nzk_2wI9aIOgb3lPwH9BeEtTJMols-Fpxe9sV8uq1lqUl83VNLw4VpMiakwPjkNfjr6rKeOjtNbSy4EgLKRdjANieuhxkkcZg5p89QD9xkGt64WKYgZ-ns4mycq39uWwOcJSSt_W1-jJeZXLlE_m9Fz96KJ9ROmuNpNeJ_sfvirD9Z2KTOuPq9nxIHQc515t6TG_QqFTVfsBN6YqoIVCX74hCJxTUugJUDOj19sFwQmGmQdGrRRb1KqFw6Pq-M6VpKvST-Y1g3cUZNfLL7WL2GuTNxDLLZG6AWWyEzybuF1qZN6rLKePznpZs3zcmc3ywGH_s0HTpJkBVi80vsCLKjUrK2gUbDAXmn4gKfCaEWia_edvYutoHYLVA1JsOQeDu-FII_hs95oFugwrYTk3YJeIQU8zanL9wqNZ2QmRAuemVoeWRN0hE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8742f867a0.mp4?token=PiVUQG3Qx7I06t81sJYpuYPUvCWXGjk6IrY6iRGjNIdiMaUCmqEI5gRX6QXtf59cDssZCAZg4co7pLWvPZnq9JJH7FeaRc9bvz2TFKXOC5AYZtZhyaRyR5jnB3DWd1dX3aWu7vgPe6ki9tFHQHaU1PpPWtoboz22SVAjQk_wZQxmyrpRvFXWhhs7sv3LocXEDJ86b1QzT8ipM3hggF4oschh35PugOdR0GJiImvHV1x7xFsRhxWvT4nzk_2wI9aIOgb3lPwH9BeEtTJMols-Fpxe9sV8uq1lqUl83VNLw4VpMiakwPjkNfjr6rKeOjtNbSy4EgLKRdjANieuhxkkcZg5p89QD9xkGt64WKYgZ-ns4mycq39uWwOcJSSt_W1-jJeZXLlE_m9Fz96KJ9ROmuNpNeJ_sfvirD9Z2KTOuPq9nxIHQc515t6TG_QqFTVfsBN6YqoIVCX74hCJxTUugJUDOj19sFwQmGmQdGrRRb1KqFw6Pq-M6VpKvST-Y1g3cUZNfLL7WL2GuTNxDLLZG6AWWyEzybuF1qZN6rLKePznpZs3zcmc3ywGH_s0HTpJkBVi80vsCLKjUrK2gUbDAXmn4gKfCaEWia_edvYutoHYLVA1JsOQeDu-FII_hs95oFugwrYTk3YJeIQU8zanL9wqNZ2QmRAuemVoeWRN0hE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید سروش هیچکس.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83284" target="_blank">📅 22:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83283">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69a6fe9b0.mp4?token=YtxyK5Xgflb_rYdOwLtUjHpfy1CdXdqxCgMz8eRoyNIm7oLHX-oiNJj9fREF3_QiQ0iHXpdkfA3oXOuyJFvPqgH7FXnlzGe-E95eZOP2m-EGvJGrX5b3D1ksZaAjyQljs_q-H_9yovnSxVhbyEzE4rNeq1clCidaM0tTvSc_xpDQvp2MVDKYqbqHBccj9m5TwXOhDRTsi4XMbiKwLzH3nWLUHEjooXJRABLRAX1VXgGONSYljOVQnyUBcoEp3Dba-J02OH_xpRiG2fyOsT7v5QhpLkZ77s6ORZ7ARAVPb2cgyMsRy3VjvabcHrshTVSdk6b63i-9FSaqLTWQmc-Z3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69a6fe9b0.mp4?token=YtxyK5Xgflb_rYdOwLtUjHpfy1CdXdqxCgMz8eRoyNIm7oLHX-oiNJj9fREF3_QiQ0iHXpdkfA3oXOuyJFvPqgH7FXnlzGe-E95eZOP2m-EGvJGrX5b3D1ksZaAjyQljs_q-H_9yovnSxVhbyEzE4rNeq1clCidaM0tTvSc_xpDQvp2MVDKYqbqHBccj9m5TwXOhDRTsi4XMbiKwLzH3nWLUHEjooXJRABLRAX1VXgGONSYljOVQnyUBcoEp3Dba-J02OH_xpRiG2fyOsT7v5QhpLkZ77s6ORZ7ARAVPb2cgyMsRy3VjvabcHrshTVSdk6b63i-9FSaqLTWQmc-Z3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان: هانی رامبد رو من گنده کردم، قبل من هیچکس نمیشناختش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83283" target="_blank">📅 21:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83282">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شاهین نجفی عجب موزیک ویدیو خفنی ریلیز کرده
🔥
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83282" target="_blank">📅 21:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83281">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8Zrty-P4Xu2EdQ1ntZBh_UxWEKkS2KvqhSV_LCe6xGbrTWxR5QWhHKkQMDO89wMMQ4yl3KO6Hvz3EhXpo-HADL0eyGzeMK4cGUdKR5CMIS0Kmscy5Sw059jCq5UIIOSA_cyh7TeyWmqpmF2TBNx8oZXKdTEhIFuMFW2teas_AKQFqh69I1iN9eqy0PR3G5OTb-LQ5_8u60ULyYM02p-rkhJ2ZDMhTFzAg99b22h8vwhaDDIvyn2NMAw0XgoeR0q6uAwyp-BW8OrtnW9bjRSsfUreoSDhR411qRTa2A8yBgDHQa3w3qU1bLItyWTuL7ejMlzCHP-hrB6jKNoxDH4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین نجفی عجب موزیک ویدیو خفنی ریلیز کرده
🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83281" target="_blank">📅 21:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83280">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جدی این وضعیت دیگه داره تکراری و حوصله سربر می‌شه، به نظرتون سیزن بعد از کی شروع میشه یکم پشت کامیونای سازمان ملل بدویم یه ذره هیجان زندگی بالا بره؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83280" target="_blank">📅 20:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83279">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سعی کنید تو این دوره زمونه درامد دلاری داشته باشید
من خودم درامدم دلاریه، دلاری بت میزنم و میبازم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83279" target="_blank">📅 19:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83278">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه سریالی هم هست Special Lioness یجوری توش ایرانو گنده کردن منم کم کم داره باورم میشه ایران ابرقدرته.
- مثلا ایرانیا رفتن افسر ارشد اطلاعاتی CIA رو تو خاک خود آمریکا دزدیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83278" target="_blank">📅 19:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83277">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a6977e47.mp4?token=bDck3Dmk5Ar6mxKlSxCj7K0uNCqOkzxuYgR2dmJIVTdgg9yMAg-LLXMvVVUltI83Teaf7m81yt6YXt4JkH5zs3E8sBklkjspHbovO7dDWmPqcvJas-wbRDeLZ4umBrhNfkO3gySvPgEQyQshh_SWZTtmjV-7AE7qg4dxzM51OujZtBoFU3utfCGr5H3B0zAs9jqSzAu4-7w7AjTKSTIpR7tIoPGm1BoI-ksynf9Bjj1F7jYkdawuFi7cAjN9IIlh3qVywMpwye9_FC4TuSQxjBiXH7hAmJhQj0pwxduFBv_n-iZlvKjC3mu4tcjTnJF-SFIy6RGHkBTxZmkPN0YXYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a6977e47.mp4?token=bDck3Dmk5Ar6mxKlSxCj7K0uNCqOkzxuYgR2dmJIVTdgg9yMAg-LLXMvVVUltI83Teaf7m81yt6YXt4JkH5zs3E8sBklkjspHbovO7dDWmPqcvJas-wbRDeLZ4umBrhNfkO3gySvPgEQyQshh_SWZTtmjV-7AE7qg4dxzM51OujZtBoFU3utfCGr5H3B0zAs9jqSzAu4-7w7AjTKSTIpR7tIoPGm1BoI-ksynf9Bjj1F7jYkdawuFi7cAjN9IIlh3qVywMpwye9_FC4TuSQxjBiXH7hAmJhQj0pwxduFBv_n-iZlvKjC3mu4tcjTnJF-SFIy6RGHkBTxZmkPN0YXYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق تجربه شخصی ۹۰ درصد فیلم هایی که تو اینستاگرام معرفی میکنن کصشره و بعد دیدنشون پشیمون میشید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83277" target="_blank">📅 19:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83276">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_1eLnDfOn42wbptqrnO5eDNd_LXfSw8bYNi-jf4UammOHI68IeS1v0i4Vi0AWUI6w9Ul486nJj_ey83azSenpzOoYFo7pOddSskh5EZokIYQdvCviI91F6T_FbBKPHfGbhUD2waxvFe8JfFltm2jHufN8eZihCDdunBCtP2Dlg0e52tx1qArNqvQzL4YT1CN6ZOHxlroWi3QzkrBKSf5rGbPalDbayYrZbdE62pweEfUuo6-QgRbuBCPf4d0vLglu1MfPEOs_EAvqV9ZfE18laXnk-UfjF4uTJKMXjJEmcJ_IXGjWK9H3zUXrRqivev9wX7vlz1KPfhyAKpR6H5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی هفته چهارم سری آ ایتالیا
🇮🇹
⚽️
تا دوشنبه بیست‌وسوم شهریور ماه، با ثبت حداقل ۶ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته چهارم سری آ ایتالیا، در صورت ناموفق شدن نتیجه پیش‌بینی، بتفوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/SEA4
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g20
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83276" target="_blank">📅 19:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83275">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhXQQ8kmvqFtzHcIdepl4sngOjAwA0ivfnO2jxX7JNzH90PRVmDPbhFT9mDYks7V1NUUq3hDJx4wo9BwC7Krc4CazVaVQH4eaCBdZ5tVdMB428EeLqHf--1W5UOSXETroN84lLrbRThHQZmcGZo-Xbl4fIDB5zhfYSEosOl_WG6DFp0aHcajCPP0s2ZViklihlWMCRBmA0HtlIvnNIKnZktjPS_RPsGBdk4J7zchRJE-609otn3Jn5-Tmd2r7XGbS_JTzucsBNEOawO2G86ibRMG4ttlJswwbK-8ZwBsBLN5QLkNPlR3hIWmRGZbvink-gvf-b84XwNmzaWEOO3jVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیکس چند هفته از تمام دنیا جلوایم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83275" target="_blank">📅 18:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83274">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edd900df7.mp4?token=D2MDG-v5bho6XWuzy-G7sHJkbqNFHU-vGpupDCAdOubh4211s3VyxthfU4XYbzE0he5MrIyTTL8v5KyCYaglePRmtS0fgVPLhsCwsYiW7aRfLhRJY-kVnt6nHtPv2eaybo57B0j89oRkPNe23JaS1rM5bHXvM5xsLXel5BWswO-l3epP3CTbbP-x362RPWV4pJcak-w765HbGgCOOZ245rgf_TDs6To2cPAZOBwWygagvhhKeKp7mUYFBCbf8T_AywEEBPnHGaJE7XLCE0l3b7FYoBjItD6_z-XrPUIugO8hi1IJtWY9MRwvRSt19uu7Iy3XJubP8jZHTRZU-kQdTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edd900df7.mp4?token=D2MDG-v5bho6XWuzy-G7sHJkbqNFHU-vGpupDCAdOubh4211s3VyxthfU4XYbzE0he5MrIyTTL8v5KyCYaglePRmtS0fgVPLhsCwsYiW7aRfLhRJY-kVnt6nHtPv2eaybo57B0j89oRkPNe23JaS1rM5bHXvM5xsLXel5BWswO-l3epP3CTbbP-x362RPWV4pJcak-w765HbGgCOOZ245rgf_TDs6To2cPAZOBwWygagvhhKeKp7mUYFBCbf8T_AywEEBPnHGaJE7XLCE0l3b7FYoBjItD6_z-XrPUIugO8hi1IJtWY9MRwvRSt19uu7Iy3XJubP8jZHTRZU-kQdTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی این بچه چه گناهی داشت که پوتک باباشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83274" target="_blank">📅 17:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83273">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ و‌ آمریکاییا بفهمن با ۱۱ سپتامبر همچین شوخیایی میکنیم همین امشب با اتم ایرانو نابود میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83273" target="_blank">📅 17:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83272">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تصویری از فاجعه ۱۱ سپتامبر:
🛬
🏢
🏢
🏢
🏢
🏢
🏢
🛫
🏢
🏢
🏢
🏢
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83272" target="_blank">📅 17:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83271">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان رئالی شما برا اولیسه بمالید مالک بایرن نمیگه اینا خوب مالیدن پس اولیسه رو بدیم بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83271" target="_blank">📅 16:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83270">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دلار ۲۳۵
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83270" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83269">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83269" target="_blank">📅 15:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83267">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQ7UiFh36MVV9udLs2W_cFYgWo2cutNU6CbkH4jG_DngYx1azMhauHl0l9Vsrt-hd7XUvnRqysUbHUfBL2s0ISYMTuigBFzmrOsuprlTCECryuzPdtNB72lv_cm6SfLA6PZ99YOzdwp39rHch1XSmaUU4aW0vJhiQRdgC45vkFJWkVBJa2P22dJhK0Sa6DEzEE0qwYwUf38ZHAa_7NYmV7zoMmqGBhUz9fGIDmZfM82TIg9K5tvjqezYbkAbsYSNng5XLjXJeRq9hua9Qs18Yo7I3ps1vUULEp5wzcHTDpCSoRr-5j4hYBL0hn-RygKtSCmU7lg485aExIg36xVSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rblCe3wowVCjZaaM7ez_7JmqWqb56kxB6Eyc53SHmOlVpEu8MF-TIfojtmF68OB_i-zlzYbZ7CS38ZiExwbBK6-Lh9-o5XQR8PMS4Z1p9qCD9cCX378T49GOtQ-SdDpQ-wd3ogrzCeeT-nKJjY9azSH_XiLKGl3smhGTk1z8nVb0eE-aArT0tY3t1meI4sY4lHKHUfMW_w8nDpy8jczhRXC_YqNOJuqJBASTpBvewqay-vcmEEXglfzaGE3RXKWMIdYN4rBxnuwwYtEGXeNaIsYIHa6SiVG7xiDDAnKgIWaFMXIB2Ltkd8BKP3wBn7_ACZFFbdeHclc9YBtSK-w90g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همدردی مردم ایران با مردم آمریکا همزمان با حمله تروریستی القاعده به آمریکا 20 شهریور 1380
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83267" target="_blank">📅 14:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83266">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=BYEXM8zsK_BgVJ-XvnN1hxT6ZBHJQGrXPYlZ6bw50qqBgIwokmzjwQeZRw5V6KfZ2T6lF5C6FKELfFhnV-2qWofI6j2FuWE02yn-ehOhyWCv6Gqqpf5RSvVEV9vJZX3usYoNjJIJn5bkVbv2ZTGvAknE9OH9XfvUyxDgVAuaFKEPzqHdZjyFcFfJ55dhm2NxM9r2W8ObcE8069EKMzx7N0TXSplysoRDoq523ApFOmKF5_H82JvbTG01GLszxHcJnyyqjcX-ZgzG46zFsVbn_Tngs3MkFsuDqsz9syA6KMFYt1D5UG2b5z7tb_fYesQWORshRgllI9FzIGA7YDrijA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=BYEXM8zsK_BgVJ-XvnN1hxT6ZBHJQGrXPYlZ6bw50qqBgIwokmzjwQeZRw5V6KfZ2T6lF5C6FKELfFhnV-2qWofI6j2FuWE02yn-ehOhyWCv6Gqqpf5RSvVEV9vJZX3usYoNjJIJn5bkVbv2ZTGvAknE9OH9XfvUyxDgVAuaFKEPzqHdZjyFcFfJ55dhm2NxM9r2W8ObcE8069EKMzx7N0TXSplysoRDoq523ApFOmKF5_H82JvbTG01GLszxHcJnyyqjcX-ZgzG46zFsVbn_Tngs3MkFsuDqsz9syA6KMFYt1D5UG2b5z7tb_fYesQWORshRgllI9FzIGA7YDrijA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت ۱۰۶دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83266" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83265">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دیشب نه در آمریکا، بلکه در یک کافه در قم از آیفون ۱۸ رونمایی شده، تو این ایونت همه حضور داشتن الا خود آیفون ۱۸</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83265" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83264">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8758825884.mp4?token=mEVXGjiFvR74O7wfgTp2ou5-KSduVW13fEKktYTaoF0vFKhPlEKRj8SHJV5Upst1kIMrAhJMiUOb42WzY_wGgQSbBQSws3JoKsoVfCunRbYGGFOvq-B5IBqU5vRhHilFUykj0QYvrdZNc9m7KcxDrFot8_y5zIzv7rFrh0aBSQHYzZTvR5ESu1iWSRoxR8AVwizkEuI5hZzDFY7NsM75FOqn1uCKadhmIUuxLERgQK1YgVWHzFyLL9MfdjZJdb7XXtfu1tyfPrqyAfj_6gqJRYIBSnvI68d04xw7rrSEtRKj5HoRgZyke_asuFk9dv0rQO3kFWOzIHphjwJvg-cK6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8758825884.mp4?token=mEVXGjiFvR74O7wfgTp2ou5-KSduVW13fEKktYTaoF0vFKhPlEKRj8SHJV5Upst1kIMrAhJMiUOb42WzY_wGgQSbBQSws3JoKsoVfCunRbYGGFOvq-B5IBqU5vRhHilFUykj0QYvrdZNc9m7KcxDrFot8_y5zIzv7rFrh0aBSQHYzZTvR5ESu1iWSRoxR8AVwizkEuI5hZzDFY7NsM75FOqn1uCKadhmIUuxLERgQK1YgVWHzFyLL9MfdjZJdb7XXtfu1tyfPrqyAfj_6gqJRYIBSnvI68d04xw7rrSEtRKj5HoRgZyke_asuFk9dv0rQO3kFWOzIHphjwJvg-cK6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو منهدم کردن تونل های در علی‌الطاهر که اسرائیل منتشر کرده
انفجار این تونل باعث شده یک زلزله ۴‌.۱ ریشتری بیاد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83264" target="_blank">📅 11:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83263">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=JqxqFsctHCDxmm56FMDohxNHyR050mcaP74Udys-yXEbWF2I2LEljmBi1gcPmPLl03xRABr1Wa8-GknbzAWde0Z_yiRnJJN9glSSRl6Wd6wJjEW6r1RdBRWmpwwPyIBSBT6c4YQ5c68inKO2iSGuFY0xAUKmCMFbl-Wpmy0Re5eYd9ZrVY3S3w8YKasHquA_qNXMXB9dMb8Ecmu4jsrxNsyME0dxhzLwZw4gZfLJL_27FnHCRCbSBpdr_yLvxRYZFPUAskSnPCZlvOntOOH2g8BTbDb93CA5Rt3WJTeN7pd1AG73zNjihm1bYjQSQa21ojRNrhH5OKrlDo5iL1bi_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=JqxqFsctHCDxmm56FMDohxNHyR050mcaP74Udys-yXEbWF2I2LEljmBi1gcPmPLl03xRABr1Wa8-GknbzAWde0Z_yiRnJJN9glSSRl6Wd6wJjEW6r1RdBRWmpwwPyIBSBT6c4YQ5c68inKO2iSGuFY0xAUKmCMFbl-Wpmy0Re5eYd9ZrVY3S3w8YKasHquA_qNXMXB9dMb8Ecmu4jsrxNsyME0dxhzLwZw4gZfLJL_27FnHCRCbSBpdr_yLvxRYZFPUAskSnPCZlvOntOOH2g8BTbDb93CA5Rt3WJTeN7pd1AG73zNjihm1bYjQSQa21ojRNrhH5OKrlDo5iL1bi_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی پایدار کی منحل میشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83263" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83262">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83262" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83261">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t38zEsk3KZ3_HNzRgVIZawRJXHRZQJYzH_nloCCWwqj8cbzlxs_7-IBY7RVjMaIrNaLBi0FOG9HJ29RE25eMt2A6IuBmSryLvnhAYSBorwFXaiuz5dgR2-bSGexF41zZQ5x3QVG7T-CAqwHLuBDUYXHQba2kHER-0e-wmTehVs3xjpLUJmIQD-XNfjKey3wvnGtGJTd109uMEGlM4DG99gIVQ5tlODznaHZdZjFtTL-f-bClDPilcRDQ6U99cJToh8xcseI0GzZTNJBhpLyURMtbgaQeNlmh2ibFGKZIhcR4qFzlpPlvfH6FgLAI4rCxfgxIIj0UpHa4PsHfD4eJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r20
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83261" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83260">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">امروز سالگرد حادثه ۱۱ سپتامبره، یه دژاوومون نشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83260" target="_blank">📅 09:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83259">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83259" target="_blank">📅 02:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83258">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNcfAmhQg5njQR-sacFGQ7AJ8B2cffVVE4QsVXJlVh_pKXtp08ly3YG1qLG_Xe1PgP2utX5-HzfpCY7oJOwwtpnqIVlfzzNG9TdX-MgKCgb7x6672xcmfOMhw4wf_yMwTOt7hjgDbwUI4X61SkoXbuq1RJfcP7VI0REbPXh7pF2YSPV9TNM-Mh1k4l8S4Xw3SIOyyp7UOSCDv5NydWv_mkyZVsrwCXOnolYMNS8lf1OewFPtw2vjw3ICA5KkU-egqTVcejqUiS1PPzrnLWYkgJzJvofFWaWTUbQ2rG9h8WTGA-cdA6lsEKcQskyFSrFLyjzbkT6ZZolM17J-m9NOhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا اعلام کرد به دو نفتکش در ۷ کیلومتری عمان حمله شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83258" target="_blank">📅 00:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83257">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شاهین نجفی الان برا زید جدیدش آهنگ عاشقانه هاشو میفرسته میگه لیلی بهونه بود اینارو برا تو خوندم، درحالی که اون موقع این اصلا بدنیا نیومده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83257" target="_blank">📅 23:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83256">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2d11d68qK8YJVexKbiFvGgm067IQhgeX-k1c2YwwlFiKlBKDssg6_jFgYqJf_l-CzoLQ5lplIioFzWDNhBiKNuMDXfVgjH0ZwbZ_GmBzFXUfd-f7-SMpWXXLSm4enwjtpmxeAQpHjbjDhJn3hRORAgE6-uuulkBSdvK4RNhbzJg4ohxQraMpVeeCUWKUNcuUkUsyUj17gzEmp57hmIhA326B8k8NoJgggRuhvRd1VZT7Z4dphxYY4WkU6CT4e0lSUqYUL6DtpKGih2ripi8ocx-_P158rArzCvWCrlR_CBprGFpFYXJ8S73ep0wPEH2Z1lGJtvr4rKPGwhIgis3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا یه باند میپیچه دور دستاش، با اون ۶۶ میلیون تهش اونو بدن بهتون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83256" target="_blank">📅 22:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83255">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=QJ5vu1DZei9vy575bLu4txe1mF6-ZDhbL9ib4cQwxdVW32eVwKTYdSICkKwgLMjZvH4DJQv-Em4GRVW5zeAkmWMRJNrXOYMYMIUisG2hW4daiX-P4WAFhu3AnpsHSmikyHS8Lug1Ypof75DBMdocXvdvY19_kvJMXlHAbcsNZUjObgsd3cGXJLKeMqm2ZFmnXZ2s4ltquTj5kNwJ_oQAjoiJnm_CeYaKf-bL5DQcKleSP8Pu2Y3NQmRRh3WLKc11rF3AUJnoJIXNHyDWUzS1Bvn4QwHmch4ndhcDVXsmrYPy-m9s64pz1vKzSY_qqoZmolXXdk-1YVchP5t-_eTp2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=QJ5vu1DZei9vy575bLu4txe1mF6-ZDhbL9ib4cQwxdVW32eVwKTYdSICkKwgLMjZvH4DJQv-Em4GRVW5zeAkmWMRJNrXOYMYMIUisG2hW4daiX-P4WAFhu3AnpsHSmikyHS8Lug1Ypof75DBMdocXvdvY19_kvJMXlHAbcsNZUjObgsd3cGXJLKeMqm2ZFmnXZ2s4ltquTj5kNwJ_oQAjoiJnm_CeYaKf-bL5DQcKleSP8Pu2Y3NQmRRh3WLKc11rF3AUJnoJIXNHyDWUzS1Bvn4QwHmch4ndhcDVXsmrYPy-m9s64pz1vKzSY_qqoZmolXXdk-1YVchP5t-_eTp2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو انهدام پایگاه عماد ۴ حزب الله در تپه علی الطاهر توسط ارتش اسرائیل
پایگاه عماد ۴ بزرگ ترین پایگاه گروه حزب الله بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83255" target="_blank">📅 22:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83254">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83254" target="_blank">📅 22:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83253">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=r8RRPncaWXPkfHi-eQWPs1qSl1YHX4pbRolPO74YPMUZ1vS8T9JFi0GIhOtVgQxGDhjF9kYL_wRLacUh5oDFps4rWilM3gB9yvsETy7AjeCItOGrSHorVo-hSH7lgzyl4C_HaxCsWVJ4xUnQnnNMqthYZIVKEGiNwqJ624asSb8X9-ZpyIMeo7DB672zrLvR5HxwhOf-TFoveRPj9VbWh-hpdTpaoPFk9NWuwAt-HUgErR75vr1D48vhfMQSN_sWLBFruMmkdLa7OTy9mafDlWMTk2-WVB7XJEo9o-HJFloENKYqZVMPJ2nZNUZWS_GPpgKYHU_9iNM_uXkfNUdiSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=r8RRPncaWXPkfHi-eQWPs1qSl1YHX4pbRolPO74YPMUZ1vS8T9JFi0GIhOtVgQxGDhjF9kYL_wRLacUh5oDFps4rWilM3gB9yvsETy7AjeCItOGrSHorVo-hSH7lgzyl4C_HaxCsWVJ4xUnQnnNMqthYZIVKEGiNwqJ624asSb8X9-ZpyIMeo7DB672zrLvR5HxwhOf-TFoveRPj9VbWh-hpdTpaoPFk9NWuwAt-HUgErR75vr1D48vhfMQSN_sWLBFruMmkdLa7OTy9mafDlWMTk2-WVB7XJEo9o-HJFloENKYqZVMPJ2nZNUZWS_GPpgKYHU_9iNM_uXkfNUdiSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83253" target="_blank">📅 21:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83252">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLCMJ5cGh3sCoJLwPz8VKN_u4m9O31OJDTcn2538AuDtekF68YLcjaTUYQIQ_Lsbnjb7Y4qfTuFusodCvnxO7dicSGL0YFVDCrDPpgO50KWZPTN3ay27R-jmwNrAmcXenFma-AnUFjxAwD7YJXHfFVtT_Kqmye2Ognw5yI24GmGouV59URqSCt5l57L-bkmnIfHa52RogQyCszC7NjbxjSj3p8gMgSh1F_fFelLICh7racYaL_rUOVOaySUtnEnidR3VkYsDM7cwvbi9FywTYseL1amZRZ0AOur7T1jikKWhk7u6ldkShlT2L0VZaLNpWGDYEo0GRGaUm0edKqxlCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا این کصخل که اشتباه جمع و تفریق کرده ولی جدای این ۲۶ تا میمونه، یه تورکم بوده گیشنیزارو خورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83252" target="_blank">📅 21:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83251">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4r3YMaqJpG2Tu9LjTTtdFxTY07TrFeNcBWD9nZ0YCdLlDPa_TS6-FSHV9HjOWhdpU77R0d5tgWQZDibG-CRluS1KnSmnvDNgYOos51eoNpQj1kW_BqCvE73aRxNbAZNSX7IsPjqcoQmyBGpkGUhKxGS7eKAwv7lOor8VxIWoqRDKPO_Bi8O8zIoHnlawvnG1aLUR_bLbJvCU-tFOpw4878zoXLrVLhdg0h4gHQ1YJpQtVC-83uKx_28CIdhru19yUpVUvUaq7z9MhHOhV83J4da48EQH6yd0URWx7vgfDEGHvHAJSei2NhMk5BBYh-HwM8-KhLoqcROKJj2cOwS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا مهراد هیدن که با اعضای گروهش فرق داره و بحثش جداست اومده ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83251" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83249">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hv_iBz-UU2JI5L7i5kIPnZ7v8Yp2FE-5EQGcmfDn9YzZkNUA1nKfusGpHcTXteK0jrDT3ESi4I-_1JjWujDEpqvqab7Y6Fy1XnYB2zMc7dKyld1-1Q-uEd58m_Px-7u3xe6nnUGKO0IX33NvVjcW7KM7yV6CBjOS3Jy-QjSrewc48fEOezsUs_uV1HH4CnlxiBRDqiSCqnutHBOrgs8S2fh6UJBfSk-JzKabxbpE_NI3xRR0zHEtZbRE3jvuQ19FEAjcpJo3dzaX7GL_710g4ybHPOyNpOL_Fedilr2CDXqUic7OoCvQ8IWw_Zlnx835uWA6-vFJ-okldKAZEyCLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPuTcFtE2FxadY6M_i42-2ZD7BuxBwmgM18ny-ODrT4ZFSBzV-2zPZFkEk5ZMjSGz_p9bylg6BuCF2Fuatt5XVTqRZMWqRh_aE4WTFMow_lEyglwbudH5KZ20GsYdU3qmkixs2A1b0metD6wNGqYvbthtKfFzhKYBCgWSK0j_RMCPaxnxMSa6iFG906tYYWpoe5QZLza5X0K7XTktwAaj1kfT9rx1JAHqh5mEdkO9AZw_DFjvUxyoqLwn2_3ve-Wt-lWkGhD2YZG6iNG0Q4oXxThX1uMWjfgN-IlpJLF7LnfV4zUFGPVD2wzKcVdhuAOvHaOLJ___f2nwzHK8z_hEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آدیداس با انیمیشن ماشین ها همکاری کرده و کفش با طرح مک کویین و ماتر داده بیرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83249" target="_blank">📅 19:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83248">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHHrlo5u96V5oFqmkFHJK3PQ6ZW-X0O2fNeoZJMicyLVddX5jeRIEV7hRyd57J0tRqHm9FaP4yDICv66D1Ur4emdTiqePdbobqH0bWtDmC5P_t7bBwz4o0m3GSHMNJk78TOAhEiFEQjfVNGNqXdzgz-LyNDn8hXsKZALWa5To1GL66e_mjpSiZamJh9OeQECagjJj4HfDJ4PhSDgHICMmwFB6ZZ7QXqqv_kVnvM659o-nfUBDeVaBClcplJ1iYkPm6RmybVdJ929-Zn2SswT82hm8YsR8ruKSX8GEV8Ftsq6dlsiMBfPy8DNDBkmOoJ-Z0I4TwaHq-iSouBJEtHuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم دیگه بگذره عکس کیر مهدیارم لیک میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83248" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqGtMw1BAUAbz_aPk0m3isS9utk7ad0QPCvNue9JR2qGnhPB9xZcjnaI_1Xd9XVbT7BCbKDynH5Kdb5__Aun7Hcp5EJTgGh-NoUGa-2z9bQmqkH32G-_ecXJQeNLT1bD12m24wL1fSvS6hpjFGfrhlvbHWTSJwCTET-pkTN8kIWzSataEkRJPMPOsAoYLRJzC5Jxy-WtnErGbOvF7R-fSGXj09ajmHMml01Lwx4tuazEL3qZd7dL63_eQajWk5ZUYxtG1se4fCgXQQ3c4vO6H1wNeszwj_Y1WWMZOf_YmtkhOVGMDJhHSOKsUB1E-VCQ8NugFXj-5dcOy1sbe2HWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین مهاجم نوکای تاریخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83246" target="_blank">📅 17:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خلوت کنید آقای خمسه اومده</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83245" target="_blank">📅 17:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TturWT44KvwDYI7n7iK6ZX8FXOQxPH7L5mqJ0C6CEwyNGmv0jFvDClfGzixnCAYgL2gLGRlwt-7fHGuv44YYK0Ue3KVka8TIyj1KcPzecVg_gD1ZfMzdpnn5ugzTjU9UOD7cYmUK_6XYoCnpyFy8jOOxR3iS8vP4iQQ54j4NlBYQPlZDPynUcQ1gK_QTkMrH2H2k_RNkwB-9CWAyUEkzqAPI--7lqXuXNhkwxKFZyvebBcGOJrwtBr2tG878aM2dJsxiDekYiyeeuOXL_LoFLx1F3ztRAHhbcwohUB8tR09IpHrmCiaepMxbn94YD0lRf0a6UlmDsRCZCTuOCCyW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب رپفارسی اینه که کسی که به داداش حسین تی ام میشناسنش به سجاد شاهی میگه فید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83244" target="_blank">📅 16:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83240">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=J1kmQGGj1ItVUwkuBzYLg3d-PSetNE322xdN-6Wzwb-4fu0cvBlHViDU-3SH1ruScX_cZTik38qrC993z1mbx7gyVH7A5G7D2DSVOpDeN-dWVsalU1fXBVoFpkEfCxkDRzb48EszgvvNBZrMnsHeXUdOkGTjrtwbQ1ryjkliT7kvbmHo5iDOZ6dM29V95lHg8Tph7kNedf8lcQ26ett2ktgbF2wmnAOyAnLdB_M59caVReJk7mPK2OtQ2Cx_2GLJW4BnyaOSiH1L3jfo30QSzJOo_o4jd1waSAZ33gPdiF1O77qghQq5FfRYjxBh0fcexNuUWFaIMu20MEjSpmi8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=J1kmQGGj1ItVUwkuBzYLg3d-PSetNE322xdN-6Wzwb-4fu0cvBlHViDU-3SH1ruScX_cZTik38qrC993z1mbx7gyVH7A5G7D2DSVOpDeN-dWVsalU1fXBVoFpkEfCxkDRzb48EszgvvNBZrMnsHeXUdOkGTjrtwbQ1ryjkliT7kvbmHo5iDOZ6dM29V95lHg8Tph7kNedf8lcQ26ett2ktgbF2wmnAOyAnLdB_M59caVReJk7mPK2OtQ2Cx_2GLJW4BnyaOSiH1L3jfo30QSzJOo_o4jd1waSAZ33gPdiF1O77qghQq5FfRYjxBh0fcexNuUWFaIMu20MEjSpmi8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: پاکستان و ترکیه تصمیم گرفتند نیروهای خود را به یمن نفرستند</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83240" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83239">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ولی خب طبیعتاً هیچوقت کسی که برا پول میجنگه نمیتونه حریف کسی برا اعتقاد میجنگه بشه، اسرائیلم سر همین جلو اینا دووم اورده و خیلیاشونو نابود کرده، چون اونام اعتقاد خودشونو دارن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83239" target="_blank">📅 14:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83238">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مگه نمیگقتید حوثی ها دارن بگا میرن</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83238" target="_blank">📅 14:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83237">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انصار الله و حوثی های یمن به نیروهای تحت حمایت عربستان و امارات کیر زدن و درحال پیشروی ان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83237" target="_blank">📅 14:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83236">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKNbil3PGjOWyHSl6oRXeh_vOEC2AviJoak1nzNaj1hpOX4m8nKandGMJ0qlWDSAw41GLQ0bWRZF4IBkfzkrc20SLuVylneIC2N7oCQ5wtYUmZYtzCQuTN3Tpi8_HMI8ZuwoQwAWfpH5x-hNYHOdU5S7VdcBDzNWGbo_j93vOMBfW74eFBiVrQ-GKCQVVi-ut9xKY_Nq8wTaIqLSnzYy1lhrhQFHdOXmS0k8X2Rz1X1d6PMr9wh3lVYgs6sNBidrr-Gcv-tndtKf1fOVaXA2qu6i9zUV2WjbqVwpMGK5PQZve-X0cUYd2reBAXe1yI09rLWaKUKgad5-gh_O3Xd0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم نظرم عوض شد ولی همچنان لیلی بهتره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83236" target="_blank">📅 14:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83234">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scB8nR93xXpDiMgIRkTO_XMBLUlv7NkEsQO731mhGY9fl6ed34F2uzdhoocxfVO3D38R3c-Khn-trKidRt2JZmlgE2mJhUAfekXgStnKfGS_EYN7tCPalBQx9Ro9g5hPficyQEjGADxtDpQk_M6KtgUuuLz5pRv9caF6PxM4c1ebQasG7bnurD18uuxdqGXz6iQKAcqCLV1LXM4RMcPvzmljCYLIl0lW93erh4fB_1ebEyp310RzJfB7-wMkotarU8ZRcAx38jQNbtB22Lcw8Zwo2QCh_f0_VHkxRk08Zl1QmnfPOEiFmrAFeIUCjy9T4zipEIhVqLf9Qjfbnh4_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-zcTagtiyxfUsIeTDC6dFK6xHsLLFHEGS0nTQGXs6B2t4hsHzcSzWtla1Y3tuCjeumCVpmZokmsPnFhKPPaJ83dUlFAiZpXjIlGYR2vuC-0044BaozoWdulNyyaxraLCAXOrSxS99Sl9szX7O-L4xjGvVhTnZckz7e2F-8ETEm9bWuQD6k2MzbsGm2PMTG6HhQMQ0Iy-h7WAwDTorK6-KMiQyY2BVdT6LrXi1_U9ue76fp5r7EPQFCzXszf2i5XC7KZhXkwk7Jc2j2vcIbXsfvkXyh56CgMphGH7FxoNNI8Wqeyao-C4whxO1JkBP_OKG1gabOC6kd_EqNT1PU86Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لیلی بازرگان بدون دست و پا اینو میزنه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83234" target="_blank">📅 14:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83233">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الان لیلی بازرگان میاد توییت میزنه این کار شاهین نجفی رو به شاهزاده اطلاع دادم و منتظرم باهاش برخورد کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83233" target="_blank">📅 13:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83232">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83232" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83228">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jkzQozmj6gYWPFTVarbCj5rX9asELJs54pw0eL04bbXJPFjHYKRCcxFpXLlUz75W5F2OIGo70qlP_oxcH2ozdSuz3Psarrc5i9Z6FslrAjTSQDFvb1g7CJKPKj0iyBblGytb7gq3T_lRIszJIbfJEwt2Pb_bvXdOARpAm3Te1w3BGLoMhtEhxbSMt1GDmDLz9JokFy6kyhXDIR1fCjrZ3Ovf7Jj0pfqE1-INIplPO92f91kA0mmiLKY-T-MDn-IY2Wb5Wrx-g-wVW4rF2TcYjhJDbDNaICzGD55WM-p6xbFY7tnvs6YWb6k9jOSn3SUkl97QbkTSasXAFjz8lkR-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dx-vrPX5CHsj_AFVvdyWNYqELI5bgWyRTrPKjORp2z0iQ7qS4v1sJkauPonLh8SpZ0NoO8YybQrk798JHl2izqyQTqgObKLAWnBq1VcKuNkb4QiTzfIG4_FAAZCM6ZvCufRioF2u2Lt5kOvblpsfdqGEoSIvBtje-jXrrWWypDC8SpQ2uhQkUrRQCowZcLizMJx6qK5JDbYt2-JAIA4JQgF0C-TivxMiyMTPrI54A6f6jgprg9giudlsDGjbn6mMKfOipgGl11o57HqLrCg7v6IQuUDiZBLnC2HRbz04SYEziP63nwRRrxItpCeipGTzOV3O3T2uTyJve8xfCirW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxaGxLera3LzKTiKdVPlBYW9XmlV39JWro_AmRXWQD3Hhop-UHiig5mrfX8VRmzXFUphB4nV5jdEuZ68eUCIhocTBB1vuKPrDjJRhErNKMjlXfholGj076TXdgEtpfTmlSeXxbnLJzsriKsKQ9E4B8ehAWCjgem0SJL8iZZvxh_Mw1_sd0MEgAmbeVqJ2DTHRTWOvaelBwTamhDpPwhDH0tMGi7aFB9gzGhyBDggrvRUWjrlIA1wBpwIIAEMfrWpPPlhWa8pXZxYOxj0er1j8Ngf5pthuk4FG7M9dJLqRwq2NOoSp8ZJevYCqYE0O5sbMuAnPLMjx8MsUm6NVhbuxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTTgDP3165P62jFdPzwTQD8Ti-lpd0uKIhGpFRBR71D5ufYHAJ9jKWG5ezL50_UplwjRd1Uo4dcPPyzZYgdq9Xi3cP_GZyTKY9ORBeScuJh67BDD8ayn5ld3KA0IuTLmSKGXOhy4CRlvRDfNOGYeh24wFUnhmPrp4rpuGKKWynULis0pmt3pcIeauXKEgsT9t46YUzbhfAT0-h9TfgsH_AZ3pM9JK5RPsGXSZ8FB9NqQjMg-Z8xlxiO_DdWVdAxJ_CAd7QtGbwVHv5rwjKHpwjMTc2tzaiGjnzJVl0tcfC2UjsRJJR-Elhrt-umrrTUQ2C3dJs52dZwCSBKxRlVN0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83228" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83227">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83227" target="_blank">📅 13:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83226">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83226" target="_blank">📅 12:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83225">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الان دیگه هرکی عقل داره از قبل داشته</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83225" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83224">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNqUU1PL3MA_VO6cEbQPRfbbl2VP_B24zU4fEPqSZ7v4BlvCMpicFLIFuxtpbOpA4UEVPfmHH3Rkz4RpWih9sBvNIzp3S2aUpDVDx4S03R4zutm-3wjtxdg4VlEQOvE6nWQky0FjjWsQmez4hdC6l4mSh-qN9rVSerGV_qwmf2-EOF3A0LgewsSIzTn3SW7G_WuI13L1uIHSWXcz9vjR0n5yW7_8XjLS9vBzS33Bzm1YsBGjSl9qKWcMFHtE1wVg20Iubo1AXyZya5hgmxfa_jrRAFEqxX_RSpJTJMEPDFQoGugWAgRBuHetopFX1G74VSrDVtfKCuw4gAz5R0X80A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعید جوانمرد، افسر معترض ارتش، به ۸ سال حبس محکوم شد
جوانمرد، اهل الشتر در استان لرستان، پس از حضور در اعتراضات سراسری ۱۴۰۱ از ارتش اخراج شد و در پرونده‌ای مرتبط با فعالیت‌ها و مواضعش به سه سال زندان محکوم شد.
بر اساس این گزارش، جوانمرد که در مرخصی زندان به سر می‌برد، ۱۹ دی ۱۴۰۴ در منزلش بازداشت شد و در پرونده‌ای جدید با اتهام‌های «همکاری با دول متخاصم»، «اخلال در نظم» و «اقدام علیه امنیت ملی» به پنج سال  دیگر حبس محکوم شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83224" target="_blank">📅 11:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83223">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7-_nhOupBxjCSoLk4zZSrffaaNrJLZil8vT-BrbNojAwu1ag9kypkcWeYnbyV4sjBtMcnBfVk9mlcdJv2kE34kmrg-bw10r8bCjGhLofMDMioSBRV2JHq4T4_nRwobhEzc_cwrG7n1vCyG15p4TBgwoSsAGjvZzunBmy7xOMrrfQIZ4COoaSC82ucKPcfniEL-k4y3n7Fe0eC08BcVB6AcAYur1vAxivCqXKqJIgzgDzZVbAYilnkgsKncPPknevXYYCpPklZVlhsbRfEOgSvoIXrHMFpa-jGpwhy2yf_-c0huNcJylSjFGV_BeXR1FohTW74mbDfwmsMTpXih_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا به خدا این کار همه جای دنیا رای خریدن حساب میشه، این آمریکا دیگه زیادی دموکراسی داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83223" target="_blank">📅 10:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83221">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ:
ما شاهد فعالیت‌های مشکوک در کوه کلنگ هستیم، به آنها هشدار می‌دهم دست بردارند وگرنه مجبور به اقدام خواهیم شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83221" target="_blank">📅 10:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83220">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFSv5u-SELviOfZkY1RKHLDa8t6szleR2apgT7cazT3G7UzLu1wNRN2zCG_GWDfhc6tHKE-ChuNuR8LfIYpwaGGNcXQkvzIQUwSn4n8Uc5xrJjB_iuP30jpzdj7581cPreaaQphOQ1Y1TjXN14QAr5iRpPIcKiDg90aXCK2Mvf-ynevYJN0j4GkN5W5I6byx9CzRhgEFB9B-MGRqQq-KZOMKkC6sTBn561XFfOp5YkyqEurzOkYLCGbTbmx2Q5cnE_aQQ71kGWUCo9jK2GrRaK20PQDMcndCNyAJ1ne7BOAp7bNthrjY_ho7ZexjZHGbBYlMAQ1XR8tZURVVtjb5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون متن ریز اون وسط رو من اضافه نکردم، خود عقب مونده‌ش فکر کرده خیلی خنده داره.
ولی به هرحال اینچیزا مهم نیست که، دوباره صبح زیباتون بخیر
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83220" target="_blank">📅 10:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83219">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=nwTf11o99qNNrdWWuL4I6lQoh_l5wK2c23xCF97ZZG-523qfYoNgPeKUGVdLybVlMluNyALxXXt9yonxlfEnMkhAOj4WeTn4kiQshwn8EsBNqYwez4BBLhisgiBJjaFir74U4vyrGLs3wRb3plmCjvv2aP-RrKVqJD3iHWrktla0yKZVM7xp9tnEqHmb7oVYZkuVBBfaV4-zrXat_rA7rV5wHH0EKJmG4NRipDK9TJ2RJEEFGkCa75Il1sYxJp6R913DHvOHuRfIM9XsN40AVZHRSfkTuOB84X4_aieip4WsSBRKYF0JX4Xtv_T6A42aUUFrBm7Sx5QV0WEwUcTChg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=nwTf11o99qNNrdWWuL4I6lQoh_l5wK2c23xCF97ZZG-523qfYoNgPeKUGVdLybVlMluNyALxXXt9yonxlfEnMkhAOj4WeTn4kiQshwn8EsBNqYwez4BBLhisgiBJjaFir74U4vyrGLs3wRb3plmCjvv2aP-RrKVqJD3iHWrktla0yKZVM7xp9tnEqHmb7oVYZkuVBBfaV4-zrXat_rA7rV5wHH0EKJmG4NRipDK9TJ2RJEEFGkCa75Il1sYxJp6R913DHvOHuRfIM9XsN40AVZHRSfkTuOB84X4_aieip4WsSBRKYF0JX4Xtv_T6A42aUUFrBm7Sx5QV0WEwUcTChg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا اعلام کرده فیلم سینمایی نجات خلبان آمریکایی در خاک ایران هم دستور ساختشو صادر کردن و بزودی وارد پرده سینما میشه.
بزودی مردم آمریکا تو سینما:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83219" target="_blank">📅 09:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83218">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=d35-JZIy26EyXZ1Rw7Q-__ox3G1igNBZLF675afZg5YVA2Z7POzoBsVKNFjzmrm0geSH9U3cjCGmvANf5dIp5pifCfTy-5Hv0Pwqf1COPeD28Hwr7HqUNbOY5vq48cZjgF4eAEUJ0ZZQJ_nBmgVXvyXtcFx08s7hYSYkAc6r55YbPAl2Ha1xKJaDNE0AobXIL-YfTMYwEbIVAIQCNEYFzpTe8hNTQN0NuywydylhEuE4ECP74N7H1teUqTBPsR6rOC_Z6R009vK7HIN5lIybScVWSJA0MbJiyIu3KsN-5BPVYr_JufhpQnLOfbPxyT1er7Tcmld7iBgHNs4wuuvG3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=d35-JZIy26EyXZ1Rw7Q-__ox3G1igNBZLF675afZg5YVA2Z7POzoBsVKNFjzmrm0geSH9U3cjCGmvANf5dIp5pifCfTy-5Hv0Pwqf1COPeD28Hwr7HqUNbOY5vq48cZjgF4eAEUJ0ZZQJ_nBmgVXvyXtcFx08s7hYSYkAc6r55YbPAl2Ha1xKJaDNE0AobXIL-YfTMYwEbIVAIQCNEYFzpTe8hNTQN0NuywydylhEuE4ECP74N7H1teUqTBPsR6rOC_Z6R009vK7HIN5lIybScVWSJA0MbJiyIu3KsN-5BPVYr_JufhpQnLOfbPxyT1er7Tcmld7iBgHNs4wuuvG3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون با تیک‌تاک فارسی بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83218" target="_blank">📅 08:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83217">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قرمه سبزی جا افتاده از نظر پسرا و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83217" target="_blank">📅 02:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83216">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">۸ ماه گذشت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83216" target="_blank">📅 00:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hL55kbXN3sSODgovDQEg7_kF8p6h5i_E4z0YlMm4l1ftIK3MSy-ESrXyFPjfeviTjpOQ0AVsEJqE1S0xcN39ko07LFZd4XWfsjhUvQ772cWi0d3XW0csBsSXw4BcODV2gaorJ8SatS9x4v37VCOxACX9ViwS-HKKzlZWR9WcegcIUxuuGM9JAPt_QNt-ca4B8o8XJGekh8Nk_qY5GaktYgW3wwCG0wLos5hYRl_mCZ3_Le00ItsRpDpqpIoE_mkRIynOrUIijnIRFktRhr6poBoH9MH48WVxRRSsUrPpZNmIqhtsO66GLI0I2_wAvNCOznhQLNdq3manwsFa0mUwiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GpueeCNY0CBY0Z4sNOUEZ0YqaultdkKv006gAwOLwY6N5cw5fiyo42tImW3eSrjlU_rVr1ue9D3dCx39vWKhmrVmAt46Pu41Sxf2UoMQFIM9dHgGZSgtB6YWsAF5lj3ufM0nmc8OmCurZvonjqdIQ9ewRsJYBF-k9lNyQ2gSwfa7N_NO1-l8ULsHVa-qXRVS8ybdw5LE_4zh6ls1G-0_v1fdMXviyylqwiYrQaUGopc18Kx7nLiVfg3svSRC6X0wfMb93NNCHIVdeQP31sbGgaQKHcUKby1AGzYaDoR7Sla_VidZJDVLaaZul0ulx37eexUJf0kI_183ZFiXSjIBbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت بت زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83214" target="_blank">📅 22:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQarMlS1i_Dhiaz0QW0dJ8TdXa5BgoyGsmm5fbBPBdadUeSgGNwtfUFY8BHRXWx2DAfhQ7DjZLh56AWFHK5H9w0dlaPwR3Sv9Cype5e0ndk1WAUtHll_SPlMd-dXu7183WOtCmAfe_BUl89di_9UDVml-pauHNFLHfNkHJYFVrqSLQ4Bve-aUAsbpjkq3gBhwbpBjqVmvSUP2Dkbz89KUTK8kis7g-FkA0fQfYKnH_Agl2FMSU0ADDQwSD_i13V6kEfpnsdRo1HwBEztbg6P39zFwwdXPKhJFDKY1YpTBJmvPbKPdp5YXzzPCLsjHSaBkHShaA2rQ9VMw1gMB4TSAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احساس میکنم بارسا منظوری داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83213" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr1ji5inhjCRaX3AkOQ2ZbwC1rixbFxXcGu97lcECIj1jgs6x1zAnJQn0wQl9SuW9hCnm8H2gPIv9o9Vex77OKDO-ftlxhKTFPVJW_5gCCHXkZ0xDECmQf5IakjO1_tOxC2ZVEOsxtVVFhtTBW786G3RHhAL25OmXhu2Qos4i_HS4BuuA3a8ojJos8UwB40gPG10pJSQdjIbpHIWpuZpBzffAbYzy8iQF7kOCWdCJpcGZNAv3Ac-kZZ8bCioJgU1Kj519Hut6gP81t2RJ9r2jmba8gT1qAdkmuQWmIQ78h2eaCrz-SRGrLzfntw6F1j_mujTYQdRq8BXm3KhJ5K0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظ
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83212" target="_blank">📅 20:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83211">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کریم سوسکه چی موشکی ول داد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83211" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83210">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">میثاقی وقتی خداداد تو پخش زنده از کلمه های "کصخل و کصکش" استفاده میکرد میخندید، الان اومده میگه کار خداداد زشت بود نباید فحش میداد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83210" target="_blank">📅 19:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83209">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=NM8b0eRwUn_brzlJxcwZ3vzESjzwq7mzHB3DTrmjZzlJzs_zHUthhUMsGuyIXSBgoxeDN7y_6cvCaK1aU_zQ4xrABP4md64b1xK3w481YAkSW61bBOg2YVhRi0au1wxJ9lnlIHb318I31q6hx-wI_MlFjzArg-j-rNW7wbAwehg03FgYcBlFfH1nJVUXr-MAfMIUwuSg0h44iirGTF7j_2FbCEPl65kweLVI2Cjc3fopGrnheXdKlUuGHGBtO-5ZChnGeAoOz65QYmH7bQ_SgCf6TLmbgeQpEKdnxFAK9S7KxBp66J8NJrBsTlVlEZy6NTri3UJCNR_tKWBA6RTl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=NM8b0eRwUn_brzlJxcwZ3vzESjzwq7mzHB3DTrmjZzlJzs_zHUthhUMsGuyIXSBgoxeDN7y_6cvCaK1aU_zQ4xrABP4md64b1xK3w481YAkSW61bBOg2YVhRi0au1wxJ9lnlIHb318I31q6hx-wI_MlFjzArg-j-rNW7wbAwehg03FgYcBlFfH1nJVUXr-MAfMIUwuSg0h44iirGTF7j_2FbCEPl65kweLVI2Cjc3fopGrnheXdKlUuGHGBtO-5ZChnGeAoOz65QYmH7bQ_SgCf6TLmbgeQpEKdnxFAK9S7KxBp66J8NJrBsTlVlEZy6NTri3UJCNR_tKWBA6RTl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ سیدنی سوئینی برا یه سایت شرط‌بندی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83209" target="_blank">📅 19:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83208">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=O8caA0eWpYBb_jLE_4L-R71jm4fvtyPa_D-IfJcuTwXAgct4iYsERjpx68JX6GsD5sU_PgTI1aGgCS3Rv4Gp-MvQRRgc-0Ofon0K7AZjtL3Z1DizRcY77ld5cUWWkzFbGvXcqc_eiTI9EUzBpqoHkRBaYccqPrxHilRYUkw8qvq7jBk6yTC2flshkTSrwU-Rg_jLZmDJnojfuDSaz-of7Z8o5uibla15VOLwb6zI26zRVvwJJerE4q2h_WWwfvRfx2AD5mWM4cmNSwB1t_NXUp0fP8kzgkKGyhvWlFXC1x4eLziRdP1W0Zh27JkWH6ve3MWrTJvgVTt9G2h6gyyVYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=O8caA0eWpYBb_jLE_4L-R71jm4fvtyPa_D-IfJcuTwXAgct4iYsERjpx68JX6GsD5sU_PgTI1aGgCS3Rv4Gp-MvQRRgc-0Ofon0K7AZjtL3Z1DizRcY77ld5cUWWkzFbGvXcqc_eiTI9EUzBpqoHkRBaYccqPrxHilRYUkw8qvq7jBk6yTC2flshkTSrwU-Rg_jLZmDJnojfuDSaz-of7Z8o5uibla15VOLwb6zI26zRVvwJJerE4q2h_WWwfvRfx2AD5mWM4cmNSwB1t_NXUp0fP8kzgkKGyhvWlFXC1x4eLziRdP1W0Zh27JkWH6ve3MWrTJvgVTt9G2h6gyyVYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83208" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83206">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgpXQSL2dX38DX9C9gTyg2-8kjBcHv2all3dideyxKis7anwMxNMmLIJDHWIpGiUPFxJQu96BWosX0DnPjIF8lCaBm5Ma5NF6qiK2uSjU--ns3NcMJoiHRYJ4Oldx_g_BvLMspapq4QWQdT9Vj1pQEfqQsd9nMZLxqFQMbxWLYHF8sl3qEBGTDpKiAUgZ2ba0bzaG0g1TMDtvaNtmF7sZYpbyAjWu8uzo2jV3jMdwqifXgBQXmVWFoqqOoeI_i6vGSMTV9IESPdIxKPzkVIXpf-MBCUb7PQphKIOgsUMFpZCahm6eNUTtGpc72DTyYU0a3ienRFUStNzv22alv6UlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت هرگونه تحقیق، بنده‌ی حقیر به هیچ عنوان هیچگونه ارتباطی با عوامل این کانال و به خصوص این محتوا نداشته و ندارم و به صورت اجباری و تصادفی و به دلیل کمبود محتوا، در این کانال ادمین شده و دست به انتشار غیرعمدی و ناگهانی این توییت زده‌ام.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83206" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83205">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مثکه پاکستان میخواد پیمان مکه رو فعال کنه و حوثیا رو بزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83205" target="_blank">📅 18:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83204">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_Nhhc9mLm5Ln51f-IsItENjiJUONH7rae_grOxENRRK2SVWaYMBKMwboLw6443FJdFflSnBszv_tZOkyJRnkRRIbs6UZ9f5iGX_pmxSR6o8EkwTG6dcLhepjAuIpNNX31alMiWuS54TnvNh37XkAr5ba1Gx3phHNwI6HhmtYxHLbpSdzZZtWMH5zKgEM0t9Ni3AV3fyA6OHM3wFWv7Trvy8hh7JN4N5mvG0pQuz1XvH2K-5JUwPqs3-oIseNnmJizrfz1mMhG-vP0x7xzHBxie2RKEd5cD8NsrzFAYbENBSJDzNHs8fSJEoVo_CImfk7CYNObXx5EF2O6SVEhckkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به این حرکتا، همینکه تاحالا اتم نخوردیم یعنی هر جور حساب کنی خیلی تو سودیم پسر.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83204" target="_blank">📅 17:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83203">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565302292d.mp4?token=iBI_KOk1yNSodOTA64Ve7M0d_G3pTaEiBKLoPxhN66IEAEToFAsoHizLMlIir18KFDJ6IgwnSdpRO-WGel_Cud7YZuazhSTvJsGYlaLUu_nY2M2voCnypiCCCwm7xp1G_4fJTkAfRrAXmFh6HWkbwu2EBaloAAF0sCFfhGShTM1vc7cqM12apA45wfkdNxd_vsuEWXtD1wKI1XbM4mJRQS2NT8GCzC_SPpXx1Qf2RoJuXfIjKBpMZkEU1OgcOsmJf2xjFaJ13z3nsd12ItxCisM1YxRXrQk6uMV5sHCIdA_b-KF6msDtzjQc0-7YCwDkiFTupXVemDNFr4aIeDoU3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565302292d.mp4?token=iBI_KOk1yNSodOTA64Ve7M0d_G3pTaEiBKLoPxhN66IEAEToFAsoHizLMlIir18KFDJ6IgwnSdpRO-WGel_Cud7YZuazhSTvJsGYlaLUu_nY2M2voCnypiCCCwm7xp1G_4fJTkAfRrAXmFh6HWkbwu2EBaloAAF0sCFfhGShTM1vc7cqM12apA45wfkdNxd_vsuEWXtD1wKI1XbM4mJRQS2NT8GCzC_SPpXx1Qf2RoJuXfIjKBpMZkEU1OgcOsmJf2xjFaJ13z3nsd12ItxCisM1YxRXrQk6uMV5sHCIdA_b-KF6msDtzjQc0-7YCwDkiFTupXVemDNFr4aIeDoU3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فان‌هیپ‌هاپ در گذر زمان:
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83203" target="_blank">📅 17:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83202">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ارم نیوز: آمریکا در حال بررسی حضور تفنگداران دریایی خود در برخی جزایر خالی از سکنه ایران در اطراف تنگه هرمز است
در صورت اجرای این طرح، جنگنده‌های اف‌ـ۳۵بی مستقر در ناو تریپولی وظیفه پشتیبانی هوایی از تفنگداران را بر عهده خواهند داشت.
هدف این طرح، ایجاد نقاط دیده‌بانی و پایگاه‌های لجستیکی برای نظارت بر تنگه و حفاظت از کشتی‌های تجاری عنوان شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83202" target="_blank">📅 17:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83201">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=GvzGteh7A34vrioavGBgif09syBADH3e5hN6f1HLrgXDgL6vbTjJk5uN-SQ-Jc6jSTVoKzY-gDp5wcDaEXYmFcPYgNafY7b7i7t9Jl1PpwlpdA8fTli6N4ngpQcHix8MOALUqrKgOpfdYE_2nKjUGsmzo0YWyjcA5dSYDWSgALyScL4HVMSLeIHOjEP0Unq44fsKgre7JcYhzqsgLs7lAwe6MoVw3-zRUzSz8-LKJsKnZPetiDLN_okFN355kQjq17ueQS3MqWktJUaml99i6NUbWAKsY4M8lM8AhAQymZRPKZgMO3kzg1acbdkc9cxCmB9lGdZQN4bwBq_yMmTYbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=GvzGteh7A34vrioavGBgif09syBADH3e5hN6f1HLrgXDgL6vbTjJk5uN-SQ-Jc6jSTVoKzY-gDp5wcDaEXYmFcPYgNafY7b7i7t9Jl1PpwlpdA8fTli6N4ngpQcHix8MOALUqrKgOpfdYE_2nKjUGsmzo0YWyjcA5dSYDWSgALyScL4HVMSLeIHOjEP0Unq44fsKgre7JcYhzqsgLs7lAwe6MoVw3-zRUzSz8-LKJsKnZPetiDLN_okFN355kQjq17ueQS3MqWktJUaml99i6NUbWAKsY4M8lM8AhAQymZRPKZgMO3kzg1acbdkc9cxCmB9lGdZQN4bwBq_yMmTYbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ویدیو دیگه از عملکرد قوی سامانه پدافندی پاتریوت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83201" target="_blank">📅 17:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83200">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBUzsSzoq89YZYSwulV68RBZ9eZSGizzE5Cb55erTUakv41XuvZfCClMwTGSpp5bJLeJ_fWaPc7J0PHciBbAKCqoAmRzV_JwkkHTstbGDAp4esjy2Sff2XFZPq9OfgcFsIc7wN5up_IYL4-CBE0MP5aSw5L89ACqnV_8j2aeuXllhnVLF2oOl5GWAFgRcD03k5-dA2Qi_b1YcYFTL2WyKR6Tk-bIhP-4dZ9-Oy2MjMA6N2HelXYYtFpRzOQswBAIiFJBlHdrpnlMCc08ADnGeF3kTqh0uJ5wMHyd6xO8EStj1h-LcgJ9Ui5mQPsuaKHD3A_lhISkMFsNkTmUT1r6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد محجوب ۲۵ مهر ماه قراره با لویی سادرلند فایت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83200" target="_blank">📅 16:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83199">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83199" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83197">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuvGsJu4gCWNVXbJ6dSBZbAt1eKm5OlW05DdG4OyggeKMcF1wLIJn_Y7mpz4ZtMS5NSmGWJLQoCtExXu0gQCpo34JSg9oCy4xS1Vf_qWwFtn40-CfCheVZ-ibWQb5Gsb9XYMh4-DorGtFaMWsyAZmhTdQVQCsh5QjCV8UJyDyz0RA9Vv5FuRqauUGjSZcz03PqvfkKXAjrXU1wenHn_LNH4O9FEMvUwfU_c_0h1I_wftluQJFTWU_nehup64IV_izKbfSexnpIbFa26iuB7C4blYzpvbKPYmJs4COh_cjgwNv6GmLCb5pJHbBMOYg7neoVCXSmmICXejaNcESz58LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83197" target="_blank">📅 16:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83196">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZYqOHlMIthDIjalRXNl2tsqCsswAQAFTlziCDoVoAWZHwP7b8kntOmGuQj3AOAQHjtCuypF9r6EgSiOo8PXI1_T4cNiKBPXK-mmFI4hzsMgpvies_Kczh-kRdfzviAKauhaWWQYpcvtHUAfija3Ki9jrJwo97tcKMnt2IZwkcNwFXAH0moehxo3sfd1MU9EsbAMqadvIF2_QthWB4Yunr07RPzPC6Kv85VgIL8LT4KC_zIfy5KMfuHioVnVHUNUO4BC7nVSEC6aCjiPxVN7Ygnuh2nUsK9HFXiXsmFikU3QSTADwGXwxqdeHS88iawf4KpvqZvNHCVJN_BhfyDf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83196" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83195">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbMrDE2EWO-zAaEns0uIoKTjAhXhyefk9v3u0MIPdMgxzjdoUo46az9hSoOIbK4MsdFxeBQhO29IVgWFY-WN6aZd3drqxdj6njZxZk2EjLAo5vHcQvYZjboc9krq_VJdn_f5hasSvIzmTL9vNIz4nQXR-Vfgb3ZU2A3I4gHDTi5oqoV8W-8T9cJ7ZAZpwgTwxwvW5b7bG0z_YbOoKfeWNR3ZMreklTRg2zDI_99n-3nQJq6G9odZuztPmRm05ZkG3_lDnWz96qZmJdzGqel5N-i_mjDbQTsvmhBKlfEPqExH_gButVloafTQCNk4ZZdgAvZ-YEVLFdS74O3FtwmkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رنگ های احتمالی آیفون ۱۸ که میتونید با حقوق ۳ روزتون بخرید اگه قاچاقچی اعضای بدن باشید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83195" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83194">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw7oY8un3epromK9iEAZ5uXuQolNgSTDwkaIqj94hxVhHQnCRaVEfvq3p2rq5wfjymPJE6Npc8CYiRtaVzYqBf2LjLP6s-WzzbjErtHVv3SNte6UFjh2jR930EM3B2pIG8h-0RlVxuYYLXPd9_LtFSijLY0l9FK9L_E5yYGcAtSMz0boDGLQlGqxVhC25bbv_RSE4bylZHuerP_wS7K_E3-kASZukK4Wvh8FgVdbZ7pm5cMk6wjI6gbRs4DzL2lzSOTPGldP-6Y8_OLJG0rD_GvgSWGrpDR85x5YS4l_T5eEb4wqpNU8RCykH8J_FpzwqqIVZ14sxBBFqFQ0Y0l-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی وقتی دلار ی میلیارد و هفتصد و بیست میلیون تومن بود.
(اینو چند سال بعد بخونید)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83194" target="_blank">📅 15:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83193">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=N8eRedh2ne1Z8kBj7GT-mIhDIuzCN9JLsMHMQACIgO2aQ7cv1x8ikMFtaaxuvQ55n2NjzPfL32uqY3KgpQlTJIQACwxecyB8pOZrUeajl9bwb58XqAP1PvhpOcG6lwP6w9QGgYs3XWLPD24iZi__QBQNtN3juqQ-eD0t5o_5qYQZ5Wl77LLJtqksYu6haCE12iq4lziwtodjT81J4h4vuWnEbZysZuAPYBhkGGpjPpliW_1xqUXOJKdLrUpS5VAaVE_SxY5qswRwlNm4JbdnUe1euw1VsRbpnc_PqNWwqiUa41IjM_cuJTpfLgVrvL47lFaEMbZlkanI_iQ1Icvb0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=N8eRedh2ne1Z8kBj7GT-mIhDIuzCN9JLsMHMQACIgO2aQ7cv1x8ikMFtaaxuvQ55n2NjzPfL32uqY3KgpQlTJIQACwxecyB8pOZrUeajl9bwb58XqAP1PvhpOcG6lwP6w9QGgYs3XWLPD24iZi__QBQNtN3juqQ-eD0t5o_5qYQZ5Wl77LLJtqksYu6haCE12iq4lziwtodjT81J4h4vuWnEbZysZuAPYBhkGGpjPpliW_1xqUXOJKdLrUpS5VAaVE_SxY5qswRwlNm4JbdnUe1euw1VsRbpnc_PqNWwqiUa41IjM_cuJTpfLgVrvL47lFaEMbZlkanI_iQ1Icvb0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دانشگاه سمنان درمورد اتفاقات چند روز پیش و تعرض به یه دختر ایرانی توسط دانشجویان عراقی:
از همه دانشجویان عراقی‌ای که هیچ کار بدی نکرده بودن و یه دروغ بزرگ براشون بافتن عذر می‌خوام که چند تا دانشجو ایرانی که حالت طبیعی نداشتن سمت خوابگاهشون هجوم بردن، ما دستگیرشون کردیم و کاری کردیم که اعتراف کنن به کار بدی که کردن شما خیالتون راحت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83193" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83192">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ما تو خیابون کسی با استایل دهه هشتاد میلادی ببینیم مسخره اش میکنیم، بعد شما میرید عکساتونو میدید هوش مصنوعی اون شکلی بکنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83192" target="_blank">📅 14:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83191">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کیا مثل من نمی‌تونن تا شب صبر کنن تا مشخصات و قیمت گوشی آینده‌شون رو ببینن و پیش خرید کنن.
😍
بیاید بهتون قیمت و مشخصات احتمالی رو بدم تا از همین الان آماده باشید.
😉
این رو برای سیسی‌های ارزون هم که دنبال آیفون ۱۸ معمولی هستن بگم که آیفون ۱۸ عادی فعلا تا بهمن…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83191" target="_blank">📅 14:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83190">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYGCw_Uky2S5qW93wLhNuXPi3KI5P75DGA9kvozpkCVkMoQXQNN2FqkAcVusrRLD9xF-_iRUhZHOROShrt9-2IL4549z0pvGhJRD4vEJnRguh9ZfJIKhQFgRx3ZRpHLc3JlEZTV4M4R6nAFoLWZ7NAG9EdlIUpe18EqmIB7rlt3g9H_7ylm3qRBnRakbm_TE4Jb43gjJHoLDdJlj5qa2K_b6noCNO_ccurksguycYgtHuNhtuk-dO_loZfhla7JvRoYZOGRgijf9i9k_C7dcv-Hepk8kgjRK5l3g6Zk7TPMkVy4wCTciabjzc1EkvJQMJmERJh5BDO2fDyuI0QABZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگرای ایرانی آماده باشید که عقب نمونید امشب از آیفون ۱۸ رونمایی میشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83190" target="_blank">📅 13:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83189">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حاجی من از آیفون ۱۳ به بعد دیگه باورم نشد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83189" target="_blank">📅 12:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83188">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دلار ۲۳۱
درهم ۶۳
طلا گرمی ۲۴
خدایی این وضعیت برای کشوری که میانگین آیکیو جهانیش تو رتبه چهارمه اصلا قابل قبول نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83188" target="_blank">📅 12:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83187">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">روبیو وزیر امورخارجه آمریکا:
از این پس هربار ایران تلاش کند به ناوگان امریکایی آسیب برساند چه موفق باشد چه ناموفق، تعدادی از ناوگان نفتکش‌های خود را از دست می‌دهد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83187" target="_blank">📅 11:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83186">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=KCAi_46L51MQ3qSd1tkQdRkxEDehes6Ba7wFFmJGnr74w8dom-URjnRGxOYsUXztmZX5NfuK1DURID-f1zSZdEbcM5dsuG0NkjZEcEQk_U5skQTobPr3wr7LxRqERKEzpSM88gNJo5SvvoupfD4qhXqqug8tdt5qIr43PtbFSVAH4HE8dnkCrgsaJ633PgY_9QfBZfU7ptKAle0bFFCi4Oz9eYUgAdX0ihDx_-Ck-ydYLGIQxDOGzkjo5lHyiFjM8hIzH2viRW3n4NdPeDPPOShZfA_IjpIDMMS5lLTqq8aWtMT5K1vDJt33EGXbK1ziWTnE7EfTfehLpcxfgbiTZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=KCAi_46L51MQ3qSd1tkQdRkxEDehes6Ba7wFFmJGnr74w8dom-URjnRGxOYsUXztmZX5NfuK1DURID-f1zSZdEbcM5dsuG0NkjZEcEQk_U5skQTobPr3wr7LxRqERKEzpSM88gNJo5SvvoupfD4qhXqqug8tdt5qIr43PtbFSVAH4HE8dnkCrgsaJ633PgY_9QfBZfU7ptKAle0bFFCi4Oz9eYUgAdX0ihDx_-Ck-ydYLGIQxDOGzkjo5lHyiFjM8hIzH2viRW3n4NdPeDPPOShZfA_IjpIDMMS5lLTqq8aWtMT5K1vDJt33EGXbK1ziWTnE7EfTfehLpcxfgbiTZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83186" target="_blank">📅 11:28 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
