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
<img src="https://cdn4.telesco.pe/file/akb16bUfntsjDmVPmgcI30b_Jm8uoGLOy1YlPID2IxoTtv3O1tTm0CP1fn6vf2kPpTPoFPbfVckWWubb_LAY89Ehf-2aAGE4gGbKkytFI9oWqAHO6ZEQTlC-qPMfuHV5CsgtyV7tRbaaTqdkvLeeyhYceWLfCxnfnAdX4kFHMvXWQt7f3jfeK6yNN2ldqWpwjXrGRbTPRjJaO9l483BH7Oa5eYSCyRbxUFXb0cqfVPUgdVeB2Fn_0tuP0C5bDZM7GuevWadoILMg-s-xsqASlYyTtZQQewqNhA1vBupQBFcshKNhIZoGIiOOJhr40UUIM124ECE8E1-YfDYHEMlwpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 276K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 17:41:59</div>
<hr>

<div class="tg-post" id="msg-12562">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ارتش اتاق جنگ داره بر‌میگرده
😈
💥</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/withyashar/12562" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12561">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیویورک پست:
ترامپ برای انجام سفری به کمپ دیوید است در حالی که تنش‌ها با ایران به دلیل حملات آمریکا افزایش یافته است
ترامپ چهارشنبه به طور نادر به کمپ دیوید سفر خواهد کرد تا جلسه کابینه‌ای برگزار کند، زیرا مذاکرات صلح با ایران به زمان حساس خود نزدیک می‌شود، روزنامه پست مطلع شده است.
محل برگزاری جلسه ممکن است به دلیل هوای نامساعد تغییر کند.
@withyashar</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/withyashar/12561" target="_blank">📅 17:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12560">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عارف: گام نخست دسترسی آزاد و ضابطه‌مند به فضای مجازی برداشته شد
@withyashar</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/withyashar/12560" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12559">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مالکی: در قطر توافق شد که نیمی از پول‌های بلوکه شده ایران پرداخت شود
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس:
سفر آقای قالیباف به قطر در راستای موضوعات مذاکره، مسایل دوجانبه و موضوعات بین‌المللی است و آخرین تحولات بین‌المللی آنجا بررسی خواهد شد.
از آنجا که قطر مسئولیتی درباره پرداخت بدهی‌های ایران به عهده گرفته است، یکی از موضوعات سفر آقای عراقچی و قالیباف، موضوع بدهی جمهوری اسلامی ایران است.
طبق یکی از بندهای توافق‌نامه، قرار شده است که نیمی از پول‌های بلوکه شده که در اختیار قطر است به جمهوری اسلامی ایران داده شود.
@withyashar</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/withyashar/12559" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12558">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0gVztoXjtINaSakehKkRnmCEcqXxEebmwlVzDdrBXGEDw9D_u7QIFgzPLUZqemrTA1-wrH6RPY4y6D7ZCwxlKUtvVN5YEN7g39r3TONEBq2q-7JijriGrBQvszMxnlmk9gFkuY1u48n59gxiL50iAaOjkAiJZezzbc4HG5eJV0RmfYzNNKmdGFCDzuzpj16g_egO9P-TVE9oe6mysVsCOABwMw91U_KUxnBKf5Fo592HHZnFJ_qRRwbtyc9Mq4lbYxKRq_s3Km4QktprBVjxxKIU3ThpPD_KFzW8xuOOTwKoYWiyo4kITk-yq5VDx2QD3u6TAdQBDICV1WsbID0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نت بلاکس، بعد از 88 روز و  2093ساعت خاموشی تمام عیار اینترنت، همکنون نزدیک به 35% اینترنت ایران وصل شده.
@withyashar</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/withyashar/12558" target="_blank">📅 16:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12557">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وال استریت ژورنال: قالیباف برای گفتگو درباره پایان جنگ برای دومین روز متوالی در قطر مانده
وال استریت ژورنال مدعی شد مقامات ایرانی و میانجی‌گران عرب گفتند: «محمدباقر قالیباف» برای دومین روز متوالی در قطر مانده است تا درباره توافق پایان جنگ گفتگو کند.
@withyashar</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/withyashar/12557" target="_blank">📅 16:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12556">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02157fdf30.mp4?token=g5OXcx9dhcgtc2XBvMEAkxasbLUkO8j6Vjjs7fVXbhxViH5E5RzlP5zoRzAsm04PjU4q5IjxG4QIYeV2R8E4cima8c-7eUYYwjIr9aRkRP8sDG7wNG_wyQ8QKBRMZXH3ysZCGfyVIlFk-BXOB-snIrZwML8kaVJoryR_HRVGuxT9wYTw90JjvsXzgJC7dLdlFz41jovGXeU3CFbG6QVl18O23I7wJp4epOPZIs6H0kq43ffM93ta7uScQpmpHm9uxfsE7bFIK1j9Ax25TDcQxZWmFWM6JLBdnFT0byLYhvnev5Kyfh4kCs_WmZbINeOrZpz-2hMMMQAYsrnvGNOo8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02157fdf30.mp4?token=g5OXcx9dhcgtc2XBvMEAkxasbLUkO8j6Vjjs7fVXbhxViH5E5RzlP5zoRzAsm04PjU4q5IjxG4QIYeV2R8E4cima8c-7eUYYwjIr9aRkRP8sDG7wNG_wyQ8QKBRMZXH3ysZCGfyVIlFk-BXOB-snIrZwML8kaVJoryR_HRVGuxT9wYTw90JjvsXzgJC7dLdlFz41jovGXeU3CFbG6QVl18O23I7wJp4epOPZIs6H0kq43ffM93ta7uScQpmpHm9uxfsE7bFIK1j9Ax25TDcQxZWmFWM6JLBdnFT0byLYhvnev5Kyfh4kCs_WmZbINeOrZpz-2hMMMQAYsrnvGNOo8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو ساعتی پیش تو مقر کریا با وزیر جنگ اسرائیل و رئیس ستاد ارتش جلسه امنیتی برگزار کرد
@withyashar</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/withyashar/12556" target="_blank">📅 16:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12555">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23fc7f9f78.mp4?token=uoY-nWy7bt_iQtVRVS6a5-CH12ei6Um3sWwkzon-NFFlkLj_T_oxdneai7dd2om5de6o4Fro5TrD0g3E32ueag3nAb2_rULvyMot6YWfYyMUQgcGxXpQgPcv0aw0e9gDMniXdLCWOfl6gpv_D1ItlN9HWc3iwSnGeNgFo4q7ooxYZZ2Zw3ED2ctnpoBzIb7V9AZtNzaf8HjEwheM8U7X2pseWry6wR7CZM82IetS-fysJAaZuyM_8QeD4LSFnBhzP9LPj-xlOMyC6TNlOeCj9B0XKarW-wNVAAATndGH0NP3jwvv77De3HJRfK18bL6MavbMxLTjKjuIegJyPQz0vJaqsjhR4et98NGJ1ME_O_H7pmROyd4FI8WA8JWx5Tj7nOKSXwJwKvtddKWxhuNV4T873jUp_w5atieJgvLwX9XyEJAoxWU5C76HlhiNDlRkyJNvgiPsZ9jzufDVfJKbbYfjecFkdltVMak_GxAwDmbwGGimGcwPsfDuJ59TbuMjeJEBucQ7McZUrRc_MOSxdsD0oJZShbW7zDAUbxoKQ_ahnZtmGbmVwnwFeZvbT8V0nZF2HVbYIFEGP53BeAIphdTqogZCBE0JOYauhilZsAFFX31EeQBCgGRHjFEVl6kmk7ARo-t5jGsex2Dn_2DVCvifPDs34gqFaTPF6JISN2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23fc7f9f78.mp4?token=uoY-nWy7bt_iQtVRVS6a5-CH12ei6Um3sWwkzon-NFFlkLj_T_oxdneai7dd2om5de6o4Fro5TrD0g3E32ueag3nAb2_rULvyMot6YWfYyMUQgcGxXpQgPcv0aw0e9gDMniXdLCWOfl6gpv_D1ItlN9HWc3iwSnGeNgFo4q7ooxYZZ2Zw3ED2ctnpoBzIb7V9AZtNzaf8HjEwheM8U7X2pseWry6wR7CZM82IetS-fysJAaZuyM_8QeD4LSFnBhzP9LPj-xlOMyC6TNlOeCj9B0XKarW-wNVAAATndGH0NP3jwvv77De3HJRfK18bL6MavbMxLTjKjuIegJyPQz0vJaqsjhR4et98NGJ1ME_O_H7pmROyd4FI8WA8JWx5Tj7nOKSXwJwKvtddKWxhuNV4T873jUp_w5atieJgvLwX9XyEJAoxWU5C76HlhiNDlRkyJNvgiPsZ9jzufDVfJKbbYfjecFkdltVMak_GxAwDmbwGGimGcwPsfDuJ59TbuMjeJEBucQ7McZUrRc_MOSxdsD0oJZShbW7zDAUbxoKQ_ahnZtmGbmVwnwFeZvbT8V0nZF2HVbYIFEGP53BeAIphdTqogZCBE0JOYauhilZsAFFX31EeQBCgGRHjFEVl6kmk7ARo-t5jGsex2Dn_2DVCvifPDs34gqFaTPF6JISN2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو استوری‌کرده بودم دیروز خیلی درخواست بالا بود که چنلم بزارم
❤️‍🩹
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/12555" target="_blank">📅 16:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12554">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/withyashar/12554" target="_blank">📅 16:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12553">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/withyashar/12553" target="_blank">📅 16:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12552" target="_blank">📅 16:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12551">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مملکت دیونه خونس یکی پاشو میزاره رو شلنگ بعد اونیکی میکشه …
خواهیم دید چه خواهد شد</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/withyashar/12551" target="_blank">📅 16:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12550">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اینترنت بین الملل روی مخابرات کامل باز شده
@withyashar</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/withyashar/12550" target="_blank">📅 15:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12549">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سایت دولتی سیتنا هم که ا‌ول خبر وصل شدن اینترنت رو پخش کرده بود فیلتر شد.
@withyashar</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/12549" target="_blank">📅 15:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12548">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">️ایسنا خبری که مربوط به متصل شدن اینترنت بود رو پاک کرد
@withyashar</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/12548" target="_blank">📅 15:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12547">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">موشتبی خامنه‌ای : اسرائیل 15 سال آینده رو نخواهد دید!
غدّه‌ی سرطانی اسرائیل به مراحل پایانی عمرش نزدیک شده و به فضل الهی و طبق آینده‌نگری 10 سال قبل پدرم، 25 سال بعد از اون تاریخ رو نخواهد دید، ان‌شاءالله.
@withyashar
😂</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/12547" target="_blank">📅 15:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12546">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وزارت خارجه در بیانیه ای گفت:
نقض آتش‌بس توسط آمریکا بی‌پاسخ نمی‌ماند.
@withyashar</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/withyashar/12546" target="_blank">📅 15:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12545">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زمان انتخاب.pdf</div>
  <div class="tg-doc-extra">822.7 KB</div>
</div>
<a href="https://t.me/withyashar/12545" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کتاب «زمان انتخاب» نوشته
شاهزاده رضا پهلوی
این کتاب مصاحبه ای است که میشل تبمن با رضا پهلوی انجام داده، گفت و گویی است متفاوت، بدون تعارف و رودربایستی، و آگاهی رسان! در گفت و گوی مورد بحث، رضا پهلوی با نهایت صراحت پرسش های مطرح شده، پاسخ های مفصل و قاطع ارائه داده و اصول برنامه مبارزاتی و معیارهای استراتژیک خود را در مورد نظام حاکم بر ایران، وضعیت اپوزیسیون و بسیاری از مسائل منطقه و جهان، ارائه نموده است
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/12545" target="_blank">📅 14:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12544">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">معاون وزیر ارتباطات: دقایقی دیگر اولین دسترسی ها به اینترنت بین الملل ایجاد می شود و رفته رفته مرم شاهد بازگشایی تدریجی اینترنت خواهند بود و تا ۲۴ ساعت دیگر همه مردم به اینترنت بین الملل متصل می شوند./خبر آنلاین  @withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/12544" target="_blank">📅 13:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12543">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ادعای آسوشیتدپرس:
ایالات متحده و ایران دیروز در مورد مسئله دارایی‌های بلوکه‌شده به تفاهم رسیدند.
میانجیگری قطر با موفقیت به تفاهم آمریکایی-ایرانی درباره «دارایی‌های بلوکه‌شده» منجر شد.
به احتمال زیاد ایالات متحده و ایران امروز توافقی را در مورد «دارایی‌های بلوکه‌شده» اعلام خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/12543" target="_blank">📅 13:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12542">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1InqK8dAmn2ngU02iDZHnB-24FNoFk5t5SJRHfgINxFY2FjyPxiADIJSwlEiJPDwcoyeZcqsh2FAnK_wW_1YX5r0fZLQK2NdUjU3mi4g4_4J5wxv0y6WCVqEBCWm22nqMPNz7m2ZPdIoSGTOD7_KoEICiMXdYYSaTtNXzInvDa74tZ4i7yuIk1GZndd3HavGE82TEBSejrC2JlFOs22iom85A_Q-sRU4HejXu4BgJMG6sJBmBpe2x4b3fHyspuIqW4nhHfAjp-gJkaRhsTcJbUFuB6Sp2M-tcmKeFxqpZQt7eXxAuLLr-fHj6UIZ199up3rTCE4zm8NXfQFZ2FN0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «رئیسِ معامله‌گرها، به ترامپ اعتماد کنید»
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/12542" target="_blank">📅 13:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12541">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L78DqBsIqsdMmpsrbG1Cl9wooINBdIc6VCQjKBoa1i8qo3QatrUm4-XFxdAtyG7OtrvauwSbt5WSUgKz0hGuZ0zevN4c_vTbD2qy_cEyXLfYhuvXxRMB1WoX8DN1B6KBjKgbSOnPzUpKd4YGC3Jn5SuPZV-tODRGzn4z1e43pilKZrmtqkaHamVhJ67x7u4OreeeRdbDt6buwydKMlingyFbio1Gp9Ul_I4TXoENCxhdT61I4uIZYpsqOvi9N4xXFGLGj9Yb6aL7uqbaIge1gwnjT7pPymHZhEjeGIzXTDKro1Nixdi4YHNSYnpbQTChXR8iSL1LGwP8R9QGUQTt7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : توافق اوباما با ایران , مقدار عظیمی پول فرستاد تا خیانتِ برنامهٔ هسته‌ای را تأمین مالی کند.
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/12541" target="_blank">📅 13:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12540">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">معاون وزیر ارتباطات: دقایقی دیگر اولین دسترسی ها به اینترنت بین الملل ایجاد می شود و رفته رفته مرم شاهد بازگشایی تدریجی اینترنت خواهند بود و تا ۲۴ ساعت دیگر همه مردم به اینترنت بین الملل متصل می شوند./خبر آنلاین
@withyashar</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/12540" target="_blank">📅 13:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12539">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خبر خوب</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/12539" target="_blank">📅 13:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12538">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/12538" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12537">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA.sh</strong></div>
<div class="tg-text">داداش انرژی که واسه انتقاد از ادمای بی لول میزاری به جاش بیرون یه قهوه بزن یه چرخی بزن هوایی عوض کن بعد بیا اخبارتو چک کن به زندگیم برس ما ایرانی جماعت کلا ادعای فهمیدنمون میشه و تو همه چی میخوایم نظر بدیم
بخدا اروپایی من ندیدم بگه همه چی میدونم یعنی تو ۹۰درصد مواقع بدونن هم میگن اطلاعی ندارم اما ما کلا همه چی بلدیم کوتاهم نمیایم
برای همینه یا تند میریم یا کلا یه جا بی حرکت می ایستیم این خصوصیت</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/12537" target="_blank">📅 13:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12536">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سپاه: حق پاسخ به حمله دیشب امریکایی رو برای خود محفوظ نگه میداریم
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/12536" target="_blank">📅 13:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12535">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">@withyashar
جنبش صهیونیسم</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/12535" target="_blank">📅 12:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12534">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منبعی آگاه به «اتاق جنگ با یاشار» گفت که در شروط توافق این مورد تأکیید شده که ترامپ باید ختنه کند.
🤣
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/12534" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12533">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">@withyashar
ماجرای ری اکشن</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/12533" target="_blank">📅 12:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12532">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/12532" target="_blank">📅 12:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12531">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فارس  :
امشب ساعت ۲۱؛ ملت ایران فریاد «الله‌اکبر» سر می‌دهند
@withyashar
ای کپی کارای کثیف پس ما هم با جواید شاه میشوریم میبریمش ! من قبلش‌اعلام مانور دادم
😐
😂</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/12531" target="_blank">📅 12:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12530">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اتاق جنگ با یاشار : از امشب ، برای فراخوان اینترنتی ( ارتباط باشاهزاده و شنیده شدن صدای ما ) در دوشنبه دیگه هر‌شب مانور میریم و تقسیم وظایف میکنیم !
💥</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/12530" target="_blank">📅 12:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12527">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کابینه امنیتی اسرائیل امروز تشکیل می‌شود
کانال ۱۳ رژیم اسرائیل گزارش داد که کابینه امنیتی رژیم اسرائیل عصر امروز در ساعت ۱۹:۰۰ به وقت محلی تشکیل می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/12527" target="_blank">📅 12:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12526">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک منبع آگاه اسرائیلی روز سه‌شنبه اعلام کرد که ارتش اسرائیل در روزهای آینده خود را برای گسترش عملیات‌ها و حملات هوایی در لبنان آماده می‌کند. سی‌ان‌ان : این منبع تأکید کرد تحرکات نظامی اسرائیلی قریب‌الوقوع «با هماهنگی ایالات متحده» انجام می‌شود. @withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/12526" target="_blank">📅 12:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">@withyashar این پست به درخواست شما منتشر میشود</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/12525" target="_blank">📅 12:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKaInMINb7nheFmkJtXoawXEkwvhJkqM0dDBFz8zfgUUtp-k5Dt361fet5X9_oJKifz-_UwmQiRLb_BvVDd_5uVvP_EI8mCErlozIzlKFExt_na2dFyuNcWrqcP0v5BAnujGafu1eI9-46AejiCpxjTx9YQvfRChsiezvLvQOgCpQmtgktEyZ5KutVoU2cPHmep7vvFlGpx3zJeuFLXXSeRnFKyG_sbC2PcwAr673lapzok3ZX6N06LHVVKb3LrTd-heJViMWw9Nb-uajahQw33UxSGaAnkdpXLe4mPeU7b81t92WthrUiPSh_B-HRHCYckx0Yny0097Jy7cSoIdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید علی کریمی
@withyashar
یاشار : کاری با انتقاد ندارم ولی ایشون باید راهشو از پشمک نادان جدا کنه…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/12524" target="_blank">📅 11:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12523">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر: اینکه گفتن قطر 12 میلیارد دلار از پول‌های بلوکه شده ایران رو قراره پرداخت کنه کاملا کذبه و از این خبرا نیست! @withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/12523" target="_blank">📅 11:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رئیس‌جمهور روسیه، ولادیمیر پوتین، قانونی را امضا کرد که اجازه می‌دهد از نیروهای نظامی برای حفاظت از شهروندان روسیه در خارج از کشور که توسط دادگاه‌های خارجی یا دادگاه‌های بین‌المللی دستگیر، بازداشت، زندانی یا تحت پیگرد قرار می‌گیرند، استفاده شود.
این قانون در مواردی اعمال می‌شود که دادگاه‌ها بدون مشارکت روسیه عمل می‌کنند و صلاحیت آن‌ها بر اساس معاهده بین‌المللی شامل روسیه یا قطعنامه شورای امنیت سازمان ملل نیست.
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/12522" target="_blank">📅 11:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دایرکت رو دیگه باز‌نمیکنم</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/12521" target="_blank">📅 11:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12520">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12520" target="_blank">📅 11:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12519">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYxGP3lEW6yZlCpfr3k83oZfb0iuStUj9KTmdxoG22jJZpAFcEepSYpOsrc8dRDuWvadcjmXSBci--EYPdKU2JeAMK2FV0YCVFqByjsVSkv4H3QIveOAyEPO8z5dcoW5G2zSlvWuGgha717zEyzwG6YpcNSatRpBt_eLs0PDt-0pstJ40Qz8zzyE0YhEYeEcaH4UHRakaH6Hr2v9VFxanbd4vRR-z916o3abjDhRLapfJpGvtrEL8Xf9chXDXhWfwFQ6N509XdwHxst2o_92nEmL5OrqDz1isTe5zJ4FQqAZ6NiqlHFGdefiS0mLli2bunPMhkuX10xggjlJzxSwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس آپدیت جدیدی از وضعیت اینترنت بین‌الملل ایران منتشر کرد
اینترنت ایران اکنون از ۱٪ وصل به ۳٪ افزایش پیدا کرده … داره یه چیزایی میشه…
@withyashar</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/12519" target="_blank">📅 11:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12517">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03565b856.mp4?token=HmOOUhQ8MiesTveIweb2GyEidXIWB8oLRGwz9FKj1oeH5yPdGuPs2QLTuPRBeq00MhDpPQpF8L1BX4K5EY2y-o5scDERE8ULGodh8olAFD1cQ1Zi-AaqCfkvvV5Nj9j_6uyjNnGGoJ7GBJvINy0Y4u-SkWSfufcoYGA63ZG6wQ0lWI9MkytPzHJl8WdvxlLpWkiqNRxC0kFCewIV150FPAepmzQzC3rsWIcusxHXrN38c_ZsQSIPAkaWWirywGHkDcDWnEogsVSLGwZOre1qaz9XvV6rsPKsLCkGC-Ba91U0KPA1AtAlBLP414qNZz7rhXX03kXkCvR6YzTgAQeAAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03565b856.mp4?token=HmOOUhQ8MiesTveIweb2GyEidXIWB8oLRGwz9FKj1oeH5yPdGuPs2QLTuPRBeq00MhDpPQpF8L1BX4K5EY2y-o5scDERE8ULGodh8olAFD1cQ1Zi-AaqCfkvvV5Nj9j_6uyjNnGGoJ7GBJvINy0Y4u-SkWSfufcoYGA63ZG6wQ0lWI9MkytPzHJl8WdvxlLpWkiqNRxC0kFCewIV150FPAepmzQzC3rsWIcusxHXrN38c_ZsQSIPAkaWWirywGHkDcDWnEogsVSLGwZOre1qaz9XvV6rsPKsLCkGC-Ba91U0KPA1AtAlBLP414qNZz7rhXX03kXkCvR6YzTgAQeAAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تجمعات بابل» اخطار ! دیدن این ویدیو ممکن است باعث بی اختیاری‌ادرار شود
⚠️
😂
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/12517" target="_blank">📅 10:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12516">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فاکس نیوز گزارش می‌دهد  بعید است حادثه دیشب تاثیر بالای  بر روی روند مذاکرات داشته باشد و در صورت نزدیک بودن توافقی هر دو طرف بر سر یک برخورد معامله را بر هم نمی‌زنند
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/12516" target="_blank">📅 10:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12515">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شبکه «سی‌ان‌ان»: برای نخستین باز از زمان آغاز جنگ ایران و آمریکا، یک نفت‌کش ژاپنی از تنگه هرمز عبور کرد.
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/12515" target="_blank">📅 10:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12514">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانال 12 اسراییل: مجتبی خامنه‌ای هنوز توافقات شکل‌گرفته را تایید نکرده
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/12514" target="_blank">📅 10:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12513">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZcKQ9jMwTafMx_JoU4ZNCszJuuBR0F9q-LUD7yMwIWR7mrySK32y-8zUKEUhQXXWoyY0KdwLm_Y88SBnUmVXVxu1VQ3inyq19R06c7hi1hPdGG_TxoaKEu66dRYTts_p2kWtdVgcHMYVd495_-xKjbDfeRjFej-GxAdk2_-4ycdi31idYnuuhTzGzmIE72D2Qyavt3zWAwLp_UUkrce-iUP8GUBtv5GxBnmVfIKasIOH69uPe0pvMq-3gkohT1R0FCQaObmEiBcBP2tV5nztsP4M_eT5QPdJiI-SX-8UeYsQinYyLu-5rdkHLe89BH4kr35FpClDbArgNFib2nwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه اینترنت پرو از سایت همراه اول حذف کردن
گویا این پروژه شکست خورده
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/12513" target="_blank">📅 09:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12512">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taBG1olcgUyipfhRdfYuvmtEEEbvq4dwH5gWxC8vhszj_qxg89heRewIiRHvfa4CG0JY-h_fzYmEcxrs72OszWbcZO-HLUzvMfsmq1FBW9pTVDgLJbkVvQ2ykL2-Vo3Wp1n5cLZOd6FGpHFJNSn5iTakVpgvccAb_JmRSx3-G22t6lgS8JaP5plzF_aFZQ8FuNdPjl3RF27h6NOG6TmXolqodIjx2QVkNPEB7QnVSJNK5UBtjE2NcZfARvMnY1dbiylRmBxKYxaLW0vwHXN9fS09WnHkdvTiEGk82raAWHIm9VSV1SSkKarUazrLFwpjTndju_T0CTLDOQLPLChvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بامداد امروز، یک هواپیما دولت حامل مقامات عالی‌رتبه به مسکو رفت!
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/12512" target="_blank">📅 09:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12511">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک منبع آگاه اسرائیلی روز سه‌شنبه اعلام کرد که ارتش اسرائیل در روزهای آینده خود را برای گسترش عملیات‌ها و حملات هوایی در لبنان آماده می‌کند.
سی‌ان‌ان : این منبع تأکید کرد تحرکات نظامی اسرائیلی قریب‌الوقوع «با هماهنگی ایالات متحده» انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/12511" target="_blank">📅 09:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12510">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q55ejvpshOonJ9yoOM4rs3NT6Uz6lcvcMIpZz8qbgYXIUL0pbcdOCnyS31mYwdKO6lCzxaa53vJ4_SBB6__cscwqwJUHcg8PqzgD-zRASsvUNzvYLXGeWFCGkhEgvUZQ-5dBOJNT71eSqZysT1NvNe4enVuhsEah7dJlcRT6ZpiTwhz0B19wIEyKRJclSpg_YqbTpWRnpWYvwVbo_HEGSsWY9JiwbmXWDJ0skNUJjy9__WZkdQFF97cw2a5PairvGbcSxDt8d4nqxIfrZMv6LNClsLCbBXBAudCOrjYkXWifpJ72h-nGO3QDDzxA7OEz4DbeVRwlWAPRX1PdBN3CMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ در تروث سوشال:
سیاست اوباما: بسته های پول میده
سیاست ترامپ : موشک میزنه
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/12510" target="_blank">📅 09:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12509">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رویترز
:
پاکستان بلافاصله پیشنهاد ترامپ مبنی بر اینکه توافق با ایران باید به عادی‌سازی روابط با اسرائیل گره بخورد را رد کرد و گفت که این دو موضوع «به هم مرتبط نیستند و نمی‌توان آن‌ها را به هم گره زد».
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/12509" target="_blank">📅 09:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12508">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
اینکه گفتن قطر 12 میلیارد دلار از پول‌های بلوکه شده ایران رو قراره پرداخت کنه کاملا کذبه و از این خبرا نیست!
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/12508" target="_blank">📅 02:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12507">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سخنگوی سنتکام به فاکس نیوز   :  نیرو های آمریکایی در جنوب ایران حملات دفاعی انجام دادند تا از نیرو های خود در برابر تهدیدات نیرو های ایرانی محافظت کنند. اهداف شامل سایت‌ های پرتاب موشک و قایق‌ های ایرانی بودند که در تلاش برای کاشت مین بودند فرماندهی مرکزی…</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/12507" target="_blank">📅 02:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12506">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سخنگوی سنتکام به فاکس نیوز   :
نیرو های آمریکایی در جنوب ایران حملات دفاعی انجام دادند تا از نیرو های خود در برابر تهدیدات نیرو های ایرانی محافظت کنند. اهداف شامل سایت‌ های پرتاب موشک و قایق‌ های ایرانی بودند که در تلاش برای کاشت مین بودند
فرماندهی مرکزی آمریکا همچنان از نیرو های خود دفاع میکند و در عین حال در طول آتش‌ بس جاری ، خویشتن‌ داری به خرج میدهد
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/12506" target="_blank">📅 02:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12505">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نفت ۹۷$
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/12505" target="_blank">📅 02:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12504">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری اتاق جنگ : کار کانفیگ فروشا بود نت وصل نشه
🤣
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/12504" target="_blank">📅 02:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12503">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارتباط زنده صدا و سیما همین الان</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/12503" target="_blank">📅 02:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12502">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2931acd1c0.mp4?token=vpybcXGMzEqOOIZZlyq0obPzo12-yqIl9X7zLoBXHvJezJEEzQjXZnuo-BaqiE4mOp3Yqe_9cBj_wb5y7KxYkN6kiDhmFudk7l91QPDwGqBlTWDFFqwbWLczgfOTXOaVBA_yMtxeYOKYORbvOjlnaki7zR8Rt5xkysLKK5ZFuW_ArqNWoa3Vr63Mz7PEMyQ6MluhYK0eSS1seeFqnUlp4Pk7cb_GoE4On9aCUAirT16WgAot89JWHmtYYYDDBtJ0vaGah4R2elIxTko-cFd-Q_rhZejD8rWGErDgIj51hlWqPh4rl--JN6kpT7K6eH-k-5ItBoTXyVCun5Hr13DGcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2931acd1c0.mp4?token=vpybcXGMzEqOOIZZlyq0obPzo12-yqIl9X7zLoBXHvJezJEEzQjXZnuo-BaqiE4mOp3Yqe_9cBj_wb5y7KxYkN6kiDhmFudk7l91QPDwGqBlTWDFFqwbWLczgfOTXOaVBA_yMtxeYOKYORbvOjlnaki7zR8Rt5xkysLKK5ZFuW_ArqNWoa3Vr63Mz7PEMyQ6MluhYK0eSS1seeFqnUlp4Pk7cb_GoE4On9aCUAirT16WgAot89JWHmtYYYDDBtJ0vaGah4R2elIxTko-cFd-Q_rhZejD8rWGErDgIj51hlWqPh4rl--JN6kpT7K6eH-k-5ItBoTXyVCun5Hr13DGcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/12502" target="_blank">📅 02:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12501">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال 14 اسرائیل: "سلام خامنه‌ای کوچیکه"
@withyashar
😈</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/12501" target="_blank">📅 02:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12500">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سناتور لیندزی گراهام: چه مسیحی انجیلی باشید و چه نباشید، اسرائیل برای آمریکا یک معامله بزرگ است.
اگر ارتش اسرائیل، موساد و شین بت فردا ناپدید شوند، ما کنترل منطقه را از دست خواهیم داد.
پولی که به اسرائیل می‌دهیم، چندین برابر آن را از نظر امنیتی پس می‌گیریم.
اگر اسرائیل می‌خواست همه فلسطینی‌ها را بکشد، می‌توانست. از سوی دیگر، حماس می‌خواهد همه اسرائیلی‌ها را بکشد، اما نمی‌تواند.
حزب‌الله اگر می‌توانست، همه اسرائیلی‌ها را می‌کشت. و هیچ‌کس در اسرائیل نمی‌خواهد همه مردم لبنان را بکشد
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/12500" target="_blank">📅 02:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12499">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شاهزاده رضا پهلوی:
«یکی از نماینده‌های پارلمان حتی بهم گفت فکر نمی‌کنه ایرانی‌ها آماده دموکراسی باشن.
ایرانی‌ها فقط آماده دموکراسی نیستن؛ ۴۰ هزار نفر جونشون رو برای رسیدن بهش دادن و من نمی‌ذارم این فداکاری بی‌نتیجه بمونه.
چه اروپا کنار ما بایسته چه نه، چه خبرنگارها کارشون رو درست انجام بدن چه نه، چه سیاستمدارها شجاعت اقدام داشته باشن چه نه، من برای مردمم و کشورم می‌جنگم.
حتی اگر مجبور باشیم تنهایی این مسیر رو بریم، می‌جنگیم تا ایران آزاد بشه.»
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/12499" target="_blank">📅 01:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12498">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارشها میگن که اپ های ، روبیکا و بله، سروس و بلو بانک از دسترس خارج شدند
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/12498" target="_blank">📅 01:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12497">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">باراک راوید
خبرنگار آکسیوس : چرا مهمه؟ آمریکا داره موضعش رو کمی نرم‌تر می‌کنه
- احتمالاً نسبت به قبل انعطاف بیشتری درباره اورانیوم غنی‌شده ایران نشون میده و حتی تا حدی به خواسته ایران نزدیک‌تر شده
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/12497" target="_blank">📅 01:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12496">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پست جدید ترامپ که به اسپانیایی واژه خداحافظ را نوشته که بسیار طعنه آمیز است و معنیه «بری دیگه برنگردی» را میدهد. @withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/12496" target="_blank">📅 01:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12495">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsNSEmmv4yXZODvANJZE1RmVRQU6HSwlULgPMqrMSMciD8EI8FESMuTm6Hh2z78IUabLTp6leqRxUxmh-tv9SyEmsQPpcfcNyTcB1bKrjBDKjpMo3blPcIZu96N0TIWJqhjyJycTW0G3Bc8gASY4aoVLphohRGPoWO439Ai89gqsXirLcRn_rJq7BioWzCGahZNNYlywH8bqNcuKAUtofxzi-XAcyTxXwNMce7CRv1QVI7HpNohyNn8VcYC5otKAu1sRXDFfkj6rXyTZvvdOQrShIRK1QD2g-8QPJ_2emK5US1YDQo_btAQlT72dcSnOzpaxUiskWJxZ6fWlFDPRgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر می رسد 2 آتش سوزی در جزیره خارک ایران رخ داده است.
جزیره خارک بندری برای صادرات 90 درصد فرآورده های نفتی ایران است.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/12495" target="_blank">📅 01:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12494">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12494" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12493">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/12493" target="_blank">📅 01:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12492">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12492" target="_blank">📅 01:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12491">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">صدا و سیما : حمله شب گذشته دشمن آمریکایی-اسرائیلی به شناورها در جنوب جزیره لارک  بر اساس اعلام منابع محلی شب گذشته جنگنده‌های آمریکایی-اسرائیلی چند شناور ایرانی را در جنوب جزیره لارک مورد هدف قرار دادند.   طبق اعلام منابع محلی چند تن از هموطنانمان در این حملات…</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/12491" target="_blank">📅 01:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12490">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivnIaqbKFM2KrBc93tiLErVq11OeKx6bMaTmz2Pf6wOZSeBIvsD3NarKmtfFMxmfpQJXGrYi7uWY37c6x90LmGbIiMk8ozRXvSLWGQNSU6zZ5knhaEXIP0m5RRsoxK8gWMhyTJQYYpR9Sq5GmBnpaJjd4I2Fcfg_kodJoY-wgfL-RBHKvL2RxeNms-ZNyyXwn1ybdng4v8T7D2slhmZxrM4aylxTG7qve_-5NNVo_MAhXhyGn9sLPu8nxErk6_OV4FwhFLJeUAPpaz__l5pSPlpvpsgfCdcbavG159zxC1cxeykr5py65Bdj9O-UJLWg2dmp5--GK42FoQCBIRtU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : اورانیوم غنی‌شده (غبار هسته‌ای!) یا باید فوراً به ایالات متحده تحویل داده شود تا به آمریکا منتقل و نابود گردد، یا ترجیحاً با همکاری و هماهنگی جمهوری اسلامی ایران، در همان محل ــ یا در مکان مورد توافق دیگری ــ از بین برده شود؛ آن هم در حالی که کمیسیون انرژی اتمی، یا نهاد معادل آن، بر این روند و این اقدام نظارت و شهادت داشته باشد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/12490" target="_blank">📅 01:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12489">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هر‌ چیزی لیاقت میخواد…</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/12489" target="_blank">📅 01:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12488">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12488" target="_blank">📅 01:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12487">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پدافند تهران گویا فعال شد !
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/12487" target="_blank">📅 01:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12486">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۴ نفر فوتی بردن بیمارستان شهید محمدی @withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/12486" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12485">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">صابرین نیوز : اسامی شهدای حمله سحرگاه شب گذشته ۴ خرداد در جنوب جزیره لارک
بر اساس اعلام منابع محلی نام سه تن از شهدای حمله دشمن متخاصم آمریکایی-اسرائیلی که تا این لحظه شناسایی شدند به شرح زیر است:
شهید عباس اسلامی
شهید قدرت زرنگاری
گشهید عبدالرضا گلزاری
گفتنی است تعداد شهدا هنوز مشخص نشده.
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/12485" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12484">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">صدا و سیما : حمله شب گذشته دشمن آمریکایی-اسرائیلی به شناورها در جنوب جزیره لارک  بر اساس اعلام منابع محلی شب گذشته جنگنده‌های آمریکایی-اسرائیلی چند شناور ایرانی را در جنوب جزیره لارک مورد هدف قرار دادند.   طبق اعلام منابع محلی چند تن از هموطنانمان در این حملات…</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/12484" target="_blank">📅 01:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12483">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صدا و سیما : حمله شب گذشته دشمن آمریکایی-اسرائیلی به شناورها در جنوب جزیره لارک
بر اساس اعلام منابع محلی شب گذشته جنگنده‌های آمریکایی-اسرائیلی چند شناور ایرانی را در جنوب جزیره لارک مورد هدف قرار دادند.
طبق اعلام منابع محلی چند تن از هموطنانمان در این حملات به شهادت رسیده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/12483" target="_blank">📅 01:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12482">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هاآرتص: جرقه زده شد
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/12482" target="_blank">📅 01:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12481">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش مشاهده  چند موشک ۳ پا در آسمان یزد
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/12481" target="_blank">📅 00:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12480">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">برابر گزارش‌ها، پرتاب  موشک از قم.
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/12480" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12479">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اتاق جنگ با شما : فکر کنم ترور بابل درست باشه بخشی از خیابونو دو طرفشو بسته بودن کلا نه اجازه ی ورود میدادن نه خروج
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/12479" target="_blank">📅 00:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12478">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">میدل ایست :  دو قایق تندرو نیروی دریایی سپاه در خلیج فارس هدف جنگنده‌های آمریکایی قرار گرفتن و چهار سرباز کشته شدن @withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/12478" target="_blank">📅 00:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12477">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">میدل ایست :  دو قایق تندرو نیروی دریایی سپاه در خلیج فارس هدف جنگنده‌های آمریکایی قرار گرفتن و چهار سرباز کشته شدن
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/12477" target="_blank">📅 00:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12476">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انقدر مسیج بی‌مورد ندید مگه به بچه آدم چند بار باید بگن !؟! دایرکت جای جوک و نظر شما نیست ! الان  زمانه  گزارش ها است فقط !</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/12476" target="_blank">📅 00:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12475">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترور هدفمند بابل (تایید نشده)
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/12475" target="_blank">📅 00:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12474">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تابناک :
باند پروازی فرودگاه بندرعباس مورد اصابت موشک قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/12474" target="_blank">📅 00:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12473">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">زدننننن</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/12473" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12472">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پدافند اصفهان فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/12472" target="_blank">📅 00:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12471">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبر ها حاکی از شنیده شدن صدای جنگنده در دزفول و بهبهان.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/12471" target="_blank">📅 00:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12470">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گویا اشتباه تایپی بوده مقتصات حمله رو بجا جنوب لبنان ، جنوب ایران نوشتن
😅
🤣
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/12470" target="_blank">📅 00:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12469">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiKpZau6XVLBgL74k_8-tcj9QCA0uy8j3qyraet-Q4p13lwVlWRhJFp_Oh1F1KimnW0Nb3V_S322wdl15yqaB67IKPyLuywX8ICxT9CHQU8Go8szIzAimPXsib_GR70ozrLtPTRk3HYYFuJW_LT48eAxE2q1Ugfe4lqGrwpDEivLMnVhFlJkqsyKjqLppw-yjUq32ChyTo7ao058v-aoQ3U3h5QagNV8QJGDeQMr75eO9bZgc4jz0J_OA4Uv9D1_Ec2BRQYM7hFapBaI3wezkvhwvdbPZNw4DUj-Gng9cCn_MPxuRQ0cSpfHruuc283o9LHzIWLcdHlqysd2kU7bUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین عکس‌ از بندرعباس ، سمت پایگاه هوایی
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/12469" target="_blank">📅 00:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12468">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌶️
🫑</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/12468" target="_blank">📅 00:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12467">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/12467" target="_blank">📅 00:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12466">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فارس: صداهای مشابهی در جزایر سیریک و جاسک شنیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/12466" target="_blank">📅 00:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12465">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مهر: دلیل انفجارها در بندرعباس مشخص نیست.
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/12465" target="_blank">📅 00:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12464">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نوتیف واریز پولای بلوکه شده بود
🤣
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/12464" target="_blank">📅 00:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12463">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تست توافقه چیزی نیست
😂
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/12463" target="_blank">📅 00:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12462">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی: بعید میدونم آمریکا با ایران توافق کنه و 5 بند ایران رو بپذیره؛ توافق ایران و آمریکا خیلی دور است.
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/12462" target="_blank">📅 23:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12461">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ممکنه مثل همیشه پدافند یا شلیک موشک هم باشه ! صبر میکنیم فیلمی عکسی خبری رسمی ‌بیاد</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/12461" target="_blank">📅 23:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12460">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش سه انفجار بندر عباس (تایید نشده )
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/12460" target="_blank">📅 23:42 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
