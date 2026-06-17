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
<img src="https://cdn1.telesco.pe/file/nrETitJLZEgUH69I102eOBwA2PI60sSS4HsjJsoVvci7U6cOP6Po3BKDdtr7TeAgDP9VwK8tJa3qH3riCVMQNpW6YlGVKqwVzQUoPbxZGxDcmKmLsdpgDD2UEKXSbW0ILeQKhVQ_T5Q3cGPRXA-inz7kS4O9fKrhf_ZP0iN1jdiUIvPYfXvG9Q-t3t9VC9EO36DLcy1CLa_puzLGfuPAH7vTNYyZAmhOoz63yeqXOkqArja5qVfhDxgKrmzdRcSr14_zeaOB007ghgjw3MAHFrfkt_2Um26RI1plmkIOv-UdZO7b2F7o1C9oeaf-WLI7_dG-Ka_5kRjbYOmk5opcew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 161K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3922">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I4r4NcuaVXKU4Y6qVVgfw4LNVfRSYC_pcpdrTwmZs_7N5Xm5YiGippaK01xf4mA09YbH4rTTsNFelpqqG1EGi2h36re6UwS3MMeX4m2NzS4SVwKpoTRCDeVPyT9RILn6EUE7JI7w0LVL1VbR8zQpkZJowgLDv4QV3cI5vT1J8ZYwXPcjUC89oBwetTzk7GtihJh49-STiaBosYBlCqYKyBebB88hnyWzNIk1JJuwWa0kunc1_YCfQ94VZf9x4yyXboMEBMOn4WAhKrS6pe_vg3Co-dRag5u3O3ZDW5HZDbwTkAaDefd3x8BaLd29P8iONLlFI9dGboPzcpenYA21Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iKCFp6eYX78R0S-Y5MGSWlbpcJTPZLInNTFkh1iTq2RiaV_fxxd6z33Eoul3ruHZ4gS2dK1EGEpR9orqL9iKbKidE3YeqcrWCzDIMT-MbhIWExiR1IHLmxrn0ml3eQ4Lg8lmoCPLydUr3OM_A5s7GMQ9C90FX2qk7YJ2OhKd6e0a9fKGVCDN-fAXSIHC_FRa8lnMb0afeZNxpf2bLhtH3xttdAo19n_R0ijPen5EjPAdmCDzdbwoqQUb8cXUx_vQvuoD3xVfINP7-ZXAzC43sOQ7s6bmPZduSc0rNRVY3ESfDhHHlpre7W2zyzkJ64xIATv0hyKbGztAcLwcmlgrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kFOb4pWxllivaG9JFY6lOdn6Tz27p6gpyryCZA1oU-ziPMOs2aZ0D8WnwMvzf2rQ8FjnVL7oKutkjRddzHcORnL62DcUBBIhD37dgwA8hLnbKrpXfGWxI2ROU5Jma6J54rxiuAnF-UjqFi5Pp0jBSxZjHusLyZgkN6py5dnLpnkm17HakcQnz9BzfNFbpkVT3Ts_Vy3QOGiVRzkzx4r523vqkbDSFY9IohXKaunn7eEQA_joQc7b5QYWOrZN0H8uprFVFkKXwjt0R5M-HLmt61culAzNiTXA2WeeVm9l16fb9O6avSdEdR0iBR5GtA6FJSuZ0tiiUCVeZc6J4TlQ1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره قابلیت ضبط صفحه نمایش به همراه دوربین سلفی، به اندروید 17 اضافه شد و دیگه نیازی نیست این کارو با نرم‌افزارهای مجزا یا تیک‌تاک و... انجام بدیم. کلی قابلیت باحال هم برای گوشی‌های تاشو اضافه شده؛ از جمله foldable gaming(که توی تصویر دوم می‌بینید) و ارتقای مولتی تسکینگ
اطلاعات کامل تغییرات:
https://blog.google/products-and-platforms/platforms/android/android-17-features/</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qMVVwbmuANrItHo13t1aaj5f1kuKZkOq6Rnq6smhpU8DQHoBZ-1ChFGHqGijuQGiSHsxwU0lAtwBtNrLYegS4Xuw_f9B8GCexhLAegKXrasg8KH3ctOtKC25VIipPdzfkNfiR4CXcKPI2RVibpweWg0fT6flg2EjqU-cLw0QCCwHmH1Lbs4VjxvRMd7z0mxQXY0oLaebin6Ng5qZbwkvfpqPMnbtDtSN3PPwtaK7S0mYSql7L7MV-dBFa1XEqGvufUgvoHf7LE-WLbydw3Tsglm6ChIJ04_Awa2HucnHI0rj-hMNiIcwf7QbnsV-MmjMpLh48br016v4--RCjYkFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MprQEItDlfQrrwrJsFQND8zzZc9mRFWkInxee03ArgGXaqupwZ9F7_FEjhE6XrGIMfeUYzayTDlZgxDD9o4tmvCuj6P3_jLkoAY_hUxKeRDKyBOQJnq_B1zmyAUytSzIeKTggb-ltW2DUlN_Sf1F50fi0j7LksEbxrO8Gvg9QSt8iO6v7b0q0fhsLlRWQuqAPmfeEJ6I3quBoIwHGTb-UkV9UeIrGq8T2QEme52Kpp3Ucq4AQZvI820CxCovpOCzpW6TylSCYNw17JWjoH_MfVaLotJJpRZst61qrORMLEm37t4jCEJ5bZ6-KNiDggIYwUi46UClhGWSXrbgdICUrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l8dnrY7J8g5JnmGPLOK9uSH8siXfZFa4kak9llyPtwrhCjDHIfFOi3K5yPdDLq6Ahq5Jv9RtbdVxaKJW8ZEX065aKkr-I0xBSt5QLSUX0ktY4TJyweNqYf1r2oamDjJZjHPMyWGsa3cOh0ft3HYaIMwzR4xgsX12u410PCLb9gBfRnVQ44kKh7yIy5mDVLvirq0OSmdGtJLUQhRjzpUHfk87kJ8_0DZlvxYK-ULYmX6R-ZDq4DtHr6aowS-qG2QDn9CV73bsM-GeAn7M8tOeiEBPfRI_3nyjSm8PyEa91OZQ6oQPEfdWgCg8fkN5PUSFNuyQfX4E37g7cHamCQZ0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXLH3Y-q3kf4Cdc1Rd-GItBOPC5dbw6zey8M3TF9WPD37UkqaY299yEkB2EeArF-otMh-NNU5SnGzNkOKWlcALry_9Cr-KoMuThmspUo860EWPMk_0sL4rec2PjRW68cIHWYPc8VOhsMJxfXR3neazCCzO7ZUkmVIjiUCAFalM9KpdAgFZh5EEvE3J3Nrh4lwOS6rfHgw9LzzQ0yA4eO5gjIWz5nW9fo7qi7pDK2mjoSSrtslu_FhS69C6G6i3aprc6AvZhy4knw9UC7876UOw8P8TugzlAnj00-9l-sYJfrUgsQ7SUQ5TnlvAh16WF0-dzzwAhVcQGhGf5o6Ht8YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3910">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3910" target="_blank">📅 00:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا من داخل این پست میخوام توضیح بدم این بکاپ ها و این ip به چه درد میخوره؟
ببینید قبلا یعنی تا چند روز پیش شما تو ایرانسل اسکن میزدید واسه ip اینا ۱۰۰ تا میداد برای مثال ولی الان هر  چی میزنید ۵ تا به زور بهتون میده و ip اصلی که
188.114.97.6
میشد که ملت روش وصل بودن رو بستن
❗️
یعنی ip ها کلا رفت تو دیوار کاملا خاکستری شد
اینجا (patterniha) بهش اشاره کرد:
https://t.me/patt_channel_x/68
بعد حالا همه ip ها واسه همه جواب نمیده باید ببرید پشت gpt با یه سری ip محدود برای sni spoof استفاده کنید.
جدا از اون میتونید تست کنید این لیست ip ها رو که واسه شما وایت باشن و مستقیم بتونید داخل پنل های bpb و نهان و... استفاده کنید
🫰
ip:
103.160.204.34
185.193.30.94
45.8.211.57
199.181.197.1
159.112.235.52
170.114.45.239
104.17.21.111
104.24.200.94
188.114.97.6
آموزش ساخت پنل bpb
آموزش sni spoof
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AhF6hPTrsTwsX8IOZFP6-AVz3hKmIWV2h7EMvhdaWIC4FYAnrciUYUZl-cdTaX0OddWoOAwcOm9vrqquwTDUG4Ag2Wan9dTomIqpTJRMTJ1gvOK1WK0NBMfvcVpn_pEJ4rMvXmROlSfGvyKts4fgTe3DZPkyinJB3IuzSZY7HBNgEX_eHT-dMuJwG8U4A7AIIZDi-5suXZqQtaAnqjXQsPG37Ne-zRzn22uxWUzp_M-8zIZH8joGYjU5MvePsjcKrBZx4Tpy0ii5ZzCrc5g7oszUrF1pivtFUw75hlJhS_w2Kf9HluLW6rnwHzrrXRuI9hSQKL9V0wqapuNPbN-u-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3905">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی نهان:
https://github.com/itsyebekhe/nahan
لینک اسکنر:
https://github.com/MatinSenPai/SenPaiScanner
لینک ربات ProxyIP یـ‌بـ‌خـ:
t.me/nahanproxyipbot
لینک ویدئوی اندروید:
https://youtu.be/2otJfXgNWCM
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل نهان
2- اتصال به ربات تلگرام و api کلودفلر
3- ساخت کاربر و مدیریتشون
4- رفع مشکل وارد نشدن ساب در  V2rayNG و ارور 1031 و 1101
5- اسکن آیپی تمیز با اسکنر SenPaiScanner
6- پیدا کردن و تنظیم ProxyIP بر اساس کشور یا بر اساس سرعت اتصال(توی ویدئو نشون دادم چقدر سرعتم بالا رفت برای دانلود)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از
YeBeKHe
عزیز
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(نسخه باکیفیت‌تر)
💰
دونیت</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3903">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی نسخه اولیه WhiteDNS BPB
نسخه اولیه اپلیکیشن WhiteDNS BPB منتشر شد.
این برنامه برای کسانی ساخته شده که می‌خواهند پنل BPB خودشان را راحت‌تر روی Cloudflare راه‌اندازی و مدیریت کنند، بدون اینکه لازم باشد همه مراحل را دستی و پیچیده انجام بدهند.
با این اپ می‌توانید:
✅
به حساب Cloudflare خود وصل شوید
✅
پنل BPB جدید بسازید
✅
پنل‌های ساخته‌شده را داخل خود اپ ببینید و مدیریت کنید
✅
پنل BPB را با مرورگر داخلی اپ باز کنید
✅
لینک‌های سابسکریپشن مختلف پنل را ببینید
✅
سابسکریپشن‌ها را کپی یا مستقیم وارد بخش VPN کنید
✅
کانفیگ‌ها را تست کنید
✅
از داخل اپ به VPN وصل شوید
✅
لاگ‌ها و وضعیت اتصال را بررسی کنید
در این نسخه تلاش شده همه چیز ساده و مرحله‌به‌مرحله باشد؛ از اتصال Cloudflare گرفته تا ساخت پنل، گرفتن سابسکریپشن و اتصال VPN.
اپلیکیشن هنوز در نسخه اولیه است، پس ممکن است در بعضی دستگاه‌ها یا شرایط خاص نیاز به بهبود داشته باشد. اگر مشکلی دیدید یا پیشنهادی داشتید، خوشحال می‌شویم گزارش کنید تا نسخه‌های بعدی بهتر و کامل‌تر شوند.
WhiteDNS BPB v1.0.0
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3897">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lY8jfYAqqpyhp9Uov7yTK6rejyp_aEbBjiIUWJ-_ImBXHtSYIpS8kYXrYOCJ36jQnaWXDRDc7pv95yjA_6h4QOeASC649tJWF1JMkcdBz0_a16qtIPNbQi1io7rGghDnlMVjzPRWzNeoQ9S6GnpiDc6V3iWCKw6uWpghge4qbHxGHPhKkphhnuZglb1OWWQxITB66bTEF3DvoRY-gVHyd7_wMr-CKyTn4-ee4jzxuBGXDsRTIbEEMO1cVtdharY0DcBX0c92B3cEqvVzNir9DWRdi1MgaqP-5N6MS8PvGhnTxb6KjBILRBfeRH4dqNb8WqeJHgaJmemY5wMUOK6xZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xg0KdZVlcUORRiDZnnJsfCt388xXdXrKTpgOKOHzWdyUWjpb6cDOOd2PRvWwhJAgbcy1gGRWXlKYsj9t5m9Yz5UwOXIowWU82SeXQgMnmTORmsLWfLuviEcE_LE6QeCPZ0DhOb2usaLA_zGYAPeAV93r5bU3qrUXwBZ7kM5T1nWujviV00TReOlrjWXqG481GjJlTC0avgrC3E-XAFT6HvtAaPT4DQOQ5yGGmy7XLDnVGyTYNletPdywDKp4xXx_AddR0fV9lIEmvZh9kYaqh1aaq38aaYVtlXLjavSFluALXmMxHbMqUWDx56gPn3v2a-of9-X_j7jfNonqac9_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pvesIPxY5SEvkeNtFYEAdwT_zgMUN9aEOr1zJR-vBsbZRG3gf4T1Lrn3p7tjUJIRwL0JwXk1rZgPbdzR5A6X8fsSLeiqpqpjYyh7WTryDk1sX7Y5cpyEc6dJ2ft2WsK87CKZj-zuIAFBU-JYI0WIwm_0lA7JA7cto1eqsIXskZbWwfmtHiRJ69oHydwn6l8ECVBsfNs5OkIwGTJwL2uqbo8BF45MCK2kIyNhIdZPR7hbDHj_qfbUaMurLiW-Hstlr6oZOqs194MmlVf0WCpFTWSv85Bsv-q-HEcG7iU9A7_fysUsPaCQXgaowo3q8YwFDDng0_Z-Z-XGCnQceBftWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد میگن چرا کامنت‌ها رو جواب نمیدی
چون 90 درصدشون جواب توی ویدئو هست، اما ویدئو رو کامل ندیدن
✉️
مثلا اینا کامنت‌های ویدئو BPB هست</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bDPOthIQwoOWGIglyfkIuJ1XWqX1V_CPoGwJV8HLN5urAo_OvCGO_q7hqKZ9YZFdmBorpMXU5txNeI0andfRlblG7SD7jurDbyAIJJPcr8kNfewxbWUue9Y814z8TPL5c2W4QELsm-C5cSMq8qMCpS-QCzPknIp37WqQX8WxO24kGzdNIpiqzPCwd-pA4EGFpdSKFjmGeB1JK8_kNm1xydwvmc6azjekpIeg8X34brxu_ElO8GEGPOcA_4CWtm-zxp_xLHv07G5OFBPiWNOEC0D0Pb7GE1c7RNpsrgozjOLJdqQ3vpTdWMg63EaN96-vmgyC7GBCzICkkqJWqFKRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LlBkRcV9mF-ZQMCVBPRGxXeMSppPnm8yejN0T39eH2FbSofovGHTIk-Q-LkmEJbl1FXK3l1sOv-y75bSV_xF7kgunBzRePTHrrxbyStaXEhK5zfHSeATrTA256HSpHPyraL-HfTESbNOXtRXyCjhLnNaAa46r6AH0MScWDaNvAxGsmBc9I4hRDHETeTjBlUNoLiccTpgCQXL8iyRGLTvoZ06chJpT9uEeWpTqrgETWPmEJ8EjNYWLPGu9g4A8bVMAjyyZNc_CA8dN_mtBr3qIctoxBOemE4Bm5U2yl9D942HvLG0vxJITjU4EMoTxs8p3MFthHUTackGV9v3pQXZ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M0PLacTM2BzjVv7PFRhRby9VKK29B88aZyldE5LXQwpdetn_gDQUAyHei9sVnSZBfBOLkpr-Wez5lfH1yjOZqeMVkwA42U4czex9KzWCHe1HX7-fVnTAHjJhuPLnVpE-sfU0eM_H-XBCd2La3ue7DS2Ov2XSMzwt3xRVsibOY7pvSSQJGqfKpBDUfZ7mbon5S1ul-vm2QWu4AJRxORAM5GorB3haH5IBkLIo7SuStKsJVg2RzV93i439kl6IPVTbGZXK32Rio1jo_wjH7E8gJJG6F3oCmq1QmQYR7Q-cIcKTq0PVCbw0IMKgZSP7rSiwLmAI-hwlyx_uvJVXby264g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W81LmqfhWXiM53EEFjyGoiqNN5fdSgtyYCToA9W25Tl-66869DcO9Xm9oPFf1HTpHGvuNL7rjiukVGVhO2lTBaKcP9086lfhulYcnfd-8M1-lDCXP1nhbXAzEx0KCQXeyFmLeKivB-7vjLih-EdVNRKgJ-9mwFL48K_D2qhSH4lpZObo0A1aPvYF5DyztdqjxwGk496Es36VqVaYNB_NiiNq4ygBL-XUDSJ6pyQ2UTbx8dmz3odpMysax4lxuzDB6kYVcYimP6mP6ANTymebKCaazALMZYK5l2KbITftH-hIPnjpsCyRXruTuTemu9rzNOoZM25GqDL3zmpnvLIqXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/krZVQyRB7wl83qV9jQ20sUGmGayz7T_lp9hgu75HLP4eIITx9deLpi3oZZeccadtfZlMz_QSeyVxTUWO8kumWmTP2maFq5O-P5liAjoHOatU6Iy6ZbU-dIibSxjr3A7a3LzN668pfrzDlhVfUb-IEWpcohzVcr6PEMBj5xRc3BXxhQNuElrIdQtqhmNcQMTEYnPcWwSaeA1GuxLcifRlof8ySlnr0mU4tUCoc09l6gggiDBbz0bUsFpE_Ju4MDgFS2ObSIOdxRZUBe2NEsZmZYZyo4502AQ2SqWGdRnfgCjlETmk7StK-VL0ipZWF_c91N7RBNLuxl_8Zim4J-PvZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iXc3Dg4AmUGWvNznKfTKV3ZJumIQKWifJeSTz4HmAJ54mg24FfwO7LA2TXyaQrWO0uiEK9YvV1bVCCKojcP7GvK7P9S-YWIDZDHxGNDh2vkBwQZozzuctjP2t7yAtpQ-14gRPLkckMUAairGwrZJaKvKpKuiF9WQfqtlMg6OBaQmoHIjZc_7pZLExj7UTXBiaoiUVdaSzI3OzuSbvbuagP_J2ZsfnL295RaANpbE6pZoHMeLyXaCpxT3sRTgUCX1PkDFmtcYStpI1u5Xw-vs-R0xVhMrQYsgN0LQRcoW6AtMvm_fwiAEgE0QQD_Y1l4O3SwKcWW-5VIFzCgsdhHzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LdgoyUFxGuYG6yMdOhnfBZEf-iH-j_1hXKmDm0TsNJWlAfDQUoFzGivkX1D0zGNTn4IfnqEt9zhdTahOVmIZSCRGWCnY9YmvagGOZyFlGl3Y-fszWu2WQ1K3gN2sYnQBkACtCtYr_reD_3RWsAQ7WoVL8odGdOtdyN6GmyYD7_NPJocU-dwBc_EBVXQCeZ2vSjdoKi31Xh5IrHBLCrEnuYEtfs_sHL-1-jGtLlAq2eOGVGr4wJGhghrO-cVCwdkzIsxLl-yftpGc4CPEkNhvAhigyW9pIXlD917v9dqS7389RtjYJPfKkaB9zzQD-_oglw_VLvZbrMisKuUUQgkTgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SalAnj3DweaFgK8g6eKP3H4JSdDYha8aCtsolkljEjitB7POXRW6ruKTkXrFE9Cz6rsDaIVAGK4oweIpTewuVhBR2ay-IbkzTq34ZEynYT07ZLPPMzt8GJ71rlWPsVLhjw-fCQgJzj2bzvOGCRHHzWsBPq_XI-36RTFfE8WIOkIgGusFsrsX2tTfHILzHvVdt6sLHUY2O80-9bQ4TSvPSxnCNVLFgTmhReZ_EXtlPoVJyCWcqcz0Nzn-xC1YAwbDBXgWk2vPpcAtBVL_4TMxkBKc4qDiHvhR75TDBck7r9gH711EeDTSc2npOECcDFTytygsNI3PpZfPILxcYQalhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PozVQskPdu8Q0ZV950hqt3vAWfZrlbLCffuMhymEBu6CZa1fhI-fgPTPUxhViZz6k_fAUsdvJqZvavmJfgUvqQmn8_dH6y3RoDfHfnRC2bm_3S5YTuwfLznbgVdlUURmssQjDq0YAm2Pc_ty_xi3sAIGydZbM7GvfXTVNvLXmbsgWxoX7JtTdTQhvmBsUQBY3afKdRLImGTG-vMkfHu_w5qbCuzoaMnlQtSBmCCWwINYCoGAfuqyvJ3VIXUI3sdCG5Mv41FgrhK1REZcevF01GgNW3zJxlVbGFLtvJWxaLMK01c9oh33PJA3nC30KT9Ey5K-7prxwd4UkZFsptJy8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پروژه‌ی جالب دیدم به اسم SurfSense، که بهش می‌گن جایگزین اوپن سورس NotebookLM
📞
اگه از NotebookLM میاید، باید بگم که SurfSense همون کارو می‌کنه؛ صرفا با کنترل کامل دست خودتون. خلاصه بخوام بگم، یه agent تحقیقاتی اوپن‌سورس و با تمرکز روی حریم خصوصیه که شبیه به کار NotebookLM رو انجام میده.
👍
مزایا نسبت به NotebookLM:
• اتصال به ۲۵+ منبع: گوگل درایو، Notion، Slack، YouTube، GitHub و افزونه‌ی مرورگر برای ذخیره‌ی هر صفحه‌ای (حتی پشت لاگین)
• آزادی انتخاب مدل: ۱۰۰+ مدل از طریق LiteLLM، یا اجرای کاملاً لوکال با Ollama و vLLM
• بدون محدودیت داده: هیچ سقفی روی تعداد منبع و نوت‌بوک نیست، و دیتا روی سرور(یا سیستم) خودت می‌مونه
• جستجوی بهتر: RAG دومرحله‌ای در برابر سرچ تک‌مرحله‌ای NotebookLM
• قابلیت‌های تیمی جالب: به شما رول‌های Owner/Admin/Editor/Viewer میده + چت و کامنت و...
• تولید پادکستا بدون محدودیته
😭
معایب:
• نصبش هلو برو توی گلو نیست واقعا. رو اعصابه — باید با dependency، API key و فایل‌های Env کلنجار برید
• هنوز کاملاً production-ready نیست و در حال توسعه‌ی فعاله
• باید خودت میزبانی و نگهداری کنی؛ طبیعتا که راحتی NotebookLM رو نداره
#️⃣
جمع‌بندی:
صادقانه بگم، NotebookLM همچنان ساده‌تر و آماده‌تره ولی کاملاً بسته‌ست. SurfSense سخت‌تر راه میفته ولی دیتا و انتخاب مدل کاملاً دست خودته. اگه با self-hosting و سرور هم بخواید پیش برید، به درد بخورترینه.
🔗
ریپوی اصلی:
github.com/MODSetter/SurfSense
آدرس خود وبسایتش برای دانلود مستقیم نرم‌افزار:
https://www.surfsense.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vUTtc1DHrhqTfyyPPMX7f_dVUYQVZJif3L1_b2lb2SOCss-NJV8FIQnyXxUSG0hxWzU_MpFAF1jq5fnz258h3puWdVYa9i7Ug-_45v9Cm5Ek4fkcwYcK5vnUqvDXGs2nZpYrD15FHARVNrbXdaSsUiuGdwaYkCquyEXIrQ5t_FY3r41JvWAVTb8Pa1r6ILhnQnGOWrTgE0PR6BiFAdjvtttLgiUgKzrDT3j_bexWkPky7e5SOUEVnCC24jb1KsLf_1vQb1PESbvV4sypbUO3OICSSKtkzeWBzBeH-kxAsTGwkpXjKVDB2jLpBggTuKyA5k6kwaw9kqPeDQ2sMeXnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZRc6vGGOAIMD6mtEZ5i2E88QTOm_Whn_3MAFsdwk4LLwsbp12qfaJ5dB53kf39BV-4WD8apFr56KlTRoBlsSJlrQGtU89uM_ADpJfyrPKCSCgkZbUnuDhwtk8dQp-1xOz6jWh4M6gXKBlOuAktbBs4NIWhO3DAhOZ-MpYH4AKZ3FZzjZOKFlDFCqXuHHk59U2yB7kLJhXKtij0cOyMK7XJ5Gw2NcsAb76b3Po_-IWd3eAlhBiPh80wcTDvNEMGbrKxsCRMC_TQJIoF_Vnchw1ybRgDUxRMBUeSERxoPDFdjyc9ygGfj2n_2Ctu5_DAxW4eZ9ZywBhw8WrCNW_Monw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3876">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید اپ WhiteDNS VPN آماده شده.
در این نسخه
• سرعت اتصال بهتر شده
• مشکل داغ شدن گوشی رفع شده
• اپ همانقدر ساده مانده و فقط شما باید دکمه اتصال رو بزنید
متاسفانه باید نسخه قدیم رو پاک کنید و این ورژن رو از اول نصب کنید. این مشکل از ورژن بعدی نخواهد بود.
ممنون
🔥
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/3876" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3875">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/anhYmAnNjsEVblrcj9H_msz5CpVwsJZzOBIMck-FU3_wuu9nz1uFvOu0_yWLS9iFE7IVOGkyld2N_n-k2lCIU8U2rrkw28u2p3KwBfUV4IcmYQnax5kQeYUMHI3OBAB2vnkc0V7S5MeocXv-RXhx10z2W1QuxSt0PX71oWTDRI0tpSW1LTu5kzIJtNSzRV1phO6VERtxItifRBRkonXuPO0MJTGltBH1tX4zTHKsPQt0GHbYjfHmyCHklEZrQ_Jl7GoSAUL2olhV9bv7z_9G4MB_zgocFGPpGd8KpBg-2JSmLHijyi11v5zpOsQMmHh8pnUm20lRWbYysnfopDkIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو نمی‌کردم یه روزی قالب وردپرس رو هم بگن بیاید اقساطی بخرید</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CvWUab2-RBG8kitfR8jj8HqE0BRRNhEy62UH0XuAsYPHa_4UlDQfVwUuyjhnZ0oJSXgV8JS22hWk9DAUUgTb4fQlo6M8V0YErV4YTiHCHBq36Rwtg21a8El4JhgL59kgrNV3RVEe1sB34DRYHV7bE7hyM3fua266Uxg2OuU_WawlI9u0E3lmnC9NvMdXwg67_Pxrh6r2U05tQ6I22-RbbPCpSwAl_4CsJmX0yvBnJNjzsVgzkaV_hQnWT5E7nsADtI1FlNyD7UGh2zPTPMLHJljNtYVUXOAwZHiNVjazAHqKiJjIbbaTf70oayAL9fdE2BjNdG9DJPmLA_KD_-fO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a-wKN1VWGyOmtCweuPenKYUAvbE0bRCyKX8WoTOJB9Pzx4_T8Uo-s5oB4vIbLIy-suPJXCBT9cvTXdqiChoV7j7ciI2tOnJ7GnGb4vkzXvUhDvHgmXxAtJbEpkHUsD51Or8eNVDQl26_lt8UfkhYis21uBLHtGoFYD4i1LETPPqc1H9t84HSmOUi_YzdjCY3NTrkSCr3Mv0BWrTb1sneeRqll-8Vte7VS94xc5G65SGKPKqA065XibqkcJQFb1L6l-Ul6yVa8taAlUqxZy4hqMOPEKfdXRl5b3ZWIPZYBM74sMKj1KGJ0YioRQHzwRwhyx91E-YYur77jDHAcGCsOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dfRA7Nc2hO_HrJzHYx1bGhCqzt1_LvMja-XtsdQeoqOeQfDIzfoP97L4dZnMLFnfIByzdkuH5djGuwMSD7YZ7tekLoiz94SW17dysWZJ7tLidG2l83en6uc6C4x7AYqJ2xiTY4Y0sFtVVL8K0SsGc_UDwAYbDRq60JFICobGhGTmTnSIV3AFC6FLldGySMzwM2NNV1OTX6DOt6U1wBsAgVkfATXwXuS7F100NKt-fHzXpwxyhWx9EFIbUX8h0c9qX5rn857KiahMiO7zM71cOdnBY_0dpIVH0b3D6rV1uwi9B4fIxCJHtpYNp0rH0OHPDpNP2S3_-KybEbGnD3Ncow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/3871" target="_blank">📅 10:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3870">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3869">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/3869" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3868">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3868" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3867">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏
بدافزارهایی که با ترساندن هوش مصنوعی پنهان می‌مانند!
تصور کنید یک سارق بعد از دزدی، یادداشتی آنقدر وحشتناک جلوی در خانه بگذارد که مامور پلیس بعد از خواندنش، با خود بگوید «بیخیال…» و اصلاً بازرسی را ادامه ندهد! پژوهشگران متوجه شده‌اند در موج تازه‌ای از حملات نرم‌افزاری، هکرها از ترفندی مشابه برای فریب دادن هوش مصنوعی استفاده می‌کنند؛ آن‌ها بدافزارهایی می‌سازند که بخشی از متن‌شان طوری نوشته شده که هوش مصنوعی از بررسی هرچه بیشتر صرف نظر می‌کند!
ابزارهای هوش مصنوعی کنونی، ترمزهایی از پیش تعریف‌شده دارند. برای مثال اگر از آن‌ها راجع به نحوه‌ی ساخت «بدافزار»، «تسلیحات شیمیایی» یا «تسلیحات اتمی» سوال کنید، فوراً ترمزشان کشیده می‌شود و از پاسخ دادن طفره می‌روند. حالا هکرها متوجه شده‌اند که با افزودن این نوع از متون ممنوعه به بدافزارها یا نرم‌افزارهای معتبری که آلوده شده‌اند، می‌توان فرایند بررسی امنیتی کدها از سوی هوش مصنوعی را هم مختل کرد.
به زبان ساده، مهاجم سعی دارد کاری کند که ابزار امنیتی وقتی به بدافزار می‌رسد، به‌جای بررسی دقیق کدها با خود بگوید: «من اصلاً اجازه ندارم این را تحلیل کنم» و از آن رد شود.
﻿
این نوع حمله نشانه‌ای است از ورود به مرحله تازه‌ای در امنیت سایبری؛ مهاجمان دیگر فقط انسان‌ها را فریب نمی‌دهند، بلکه رفتار هوش مصنوعی هم هدف قرار می‌گیرد و ترفندها در گذر زمان فقط پیچیده‌تر و خلاقانه‌تر خواهند شد.
✍️
NooshDaroo</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmF6wZkvCSXCy9xzq__X7yTPj7Oc3cL0WjMyW7jKpldFHT8kKkIAtUhHXFbOw6uLa_3hRxjYIkKUd79PeR1gOCWOlmgGRkjRuLWDsC1wYo_aQuDnbDxRqAGASYempc8_touJHMoANISSEfaybeu0dGQc8Vayu5tASzSyPUxeqVMUjnhAdj_3fxnptNJdkQmueRuDPA6JPNGLhKrC4cuGm8SYkQ2QEfJT56c7g4Z8R6ZCfbDIKeLcv8f2Kr6J9QeRx2YfaAuuGaQHiERi12uwZ_FT_uPxTX8XdK_Uvx7EsMhbkZlGRP0TeTN86i4qRs6roU_GcCN3sSkRGVwI7vIDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید دفید قراره قابلیت چت با رمزنگاری e2e داشته باشه؛
باهاش میشه ارتباط امن با خارج و داخل ایران داشت.
کل این قابلیت با ریزالور ها کار‌ میکنه تا توی فیلترینگ و قطعی شدید هم وصل بمونه.
طبق تست های من یک‌ سرور متوسط با ۸ گیگ رم و ۴ کور سی‌پی‌یو میتونه تا ۵ هزار کاربر انلاین رو هندل کنه!
اینجوری کار میکنه که هر کاربر یک اکانت رندم واسش ساخته میشه که توی سرور های مختلف ادرس اکانتش ثابت هست؛
ادرس اکانت شامل ۲۰ حرف انگلیسیه که هرکی این رو داشه باشه میتونه بهتون پیام بده.
(سیستم اکانتینگش تقریبا شکل شبکه اتریوم هست، یعنی‌یک seed دارید که با اون یک اکانت ساخته میشه)
کلاینت هر ۱۵ ثانیه به سرور هایی که بهش وصل هست درخواست میده و پیام های جدید رو میگیره و تقریبا برای ارسال یک پیام چند کلمه ای باید حدود ۴‌ کوئری دی ان اس کوچیک‌به سرور بفرسته!
واسه اینکه به سرور ها فشار نیاد محدودیت های سختگیرانه گذاشتم، ولی همه این محدودیت ها توی سرور قابل تنظیم هست و اگر سرور شخصی راه بندازید میتونید محدودیت هارو کمتر کنید.
https://x.com/i/status/2065531715041239193</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Opvq4Ndm-WXNyKQoAjEr0xPWfqxtL_o1eg4mQHlFV7tPe1aSze4R6XDPEH7NZm7WXKmNChqLxc0CCNAR-L5RXzWfIyfo17zNEOS6Dn_iYRfmo52SreNBq8JcKhTzkikQWU0uC_3OD0F94fxL3n52N54FyTE3-5PwCHdak4VcLiZ5Xr_TX2YOt_OqqBsQMiEO7CoyPttBpYdCgJKy9CRbFPoAdCQlojsb2U_Xt3O5LGheROcYYUrV_YcnuRRf8WTPOzu_PMVZIlEiPQPCJWvEttiQKHqdwBO_3sft8KuKBl90wOAl-afAQnF-szNMmp6ikRHU-GewUpjVa8CuCb31UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a8o_9hrCHxpSv_DDtiuoLNr7aLPAvnoeZUr_lw0RdSBHDujXUfhcwKXI7BUInrzGYmRK6zEWGiAGCPfEwXMO8OsT2Urcg_zo4fYYhWRsutukxjQs99NMy4peLDRvigIiORiDQOIkbKS5L7qYObKTLeWCV37CEWoKFohoL-lphLKp6r6_uwNfnSTWVVj0Q0KM_aax6DprFGnJUdP6ZZlE5bWaTznoJNWmFpvwcfL8PFPS1e_CHv1Zi8gNzg62Reb4Jz075AtWYXMYTC-KGBanNQs3ktykAtgcAHVSI7AGZQlmScVHdVAaGzm9ARjgEVu4owTGc4TslyDpJZOCI-XX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qdETRsnwGemsQGCjgESbS9l9r-VvQTlJT79-3rPkvN-k7XGsDD3CboY6n8yhep8N9oD5P7dfeOLFa6ovNA5mpCjM523hfhN8p6YtGE6fWjFbdKrguFD_Sboji2qEjNbgYs-_i5-kx6ngpfcU6kvIHvUUSB025lugLmX1lHSH_NqEKH6qF80nZ5j5Yyf0u6zb4AfYmSdXrDUK78vAzJc-qkGF3E1KS0phUYDyuh40xd0LdVYmcaRZzO5210NWYB3JZvzoB9YTCCc-rrPDSXdH_AU72dw-mZ855et-KNz9KDI84FBsXAK_PopsMAun7VkNFz10xxrZOHGHw99p9cyqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mHfDXMk4IKpiVYH08V3lfY-WXi4waMlupevTYGXAO7FTXgAlNfnFasLlJFJrbHG8YMXPPnAOOYEPlYt-Zo0A1OeWlkdF5Y1FE_ezK3dZyfH9_xURSP6rTslQYzywy7YYoFHOP8CixY2auIJStP7_w5VCeiHbbevik62uEyt3nGF7rZDPCNZxjFXGdnrI3lMLnt0awuQHhkEHrmac1WnkkGf6M_OWAAgMQbZXJK8NbNHkXhCqkZ6bcrXHxw5QrgLlghx3rzxGXNeqlI0IrIGQejXOQih626XKRTdPJHd-uin1UOk5NSCqh24JKlRnlzExSlSERuw9ocKUQyI-LTa6uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن 0.7.1 از SenPaiScanner منتشر شد
✉️
😏
پروتکل‌های جدید
: پشتیبانی از
Shadowsocks
و
VMess
اضافه شد — هر دو از فاز ۱ اسکن تا فاز ۲ xray کاملا کار می‌کنن.
🧮
خروجی چندفرمتی
: با زدن
e
بعد از فاز ۲ می‌تونید نتایج رو به سه فرمت صادر کنید:
1- لیست Subscription
2- Sing-Box JSON
3- Clash YAML
🔥
تنظیمات سرعت
: فیلتر حداقل سرعت، تست سرعت آپلود، آدرس سرعت‌سنج دلخواه، و سایز sample قابل تنظیم.
🤖
ذخیره تنظیمات
: تنظیمات اسکن ذخیره می‌شن و گزینه «retry last scan» هم اضافه شد.
📚
پشتیبانی از CIDR
: حالا می‌تونید توی
ips.txt
، مستقیم رنج‌های
/13
و... بنویسید.
📱
اولین نسخه پیش‌نمایش
اپ اندروید
با Kotlin و Jetpack Compose اضافه شد. معماری MVVM، تم‌بندی کامل، و ساخت خودکار APK از طریق CI/CD(هرچند CI/CD باید روش کار بشه هنوز).
لینک دانلود آخرین نسخه:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.7.1</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3853">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هم پشتیبانی از Trojan و Vmess و Shadowsocks اضافه شده
هم تشخیص ISP
هم تست آپلود و شخصی‌سازی تست دانلود
هم WebSocket(که بهتره On بذارید)
هم هسته رو به کلی بازنویسی کردم
و این به کوشش دوستان عزیز برنامه‌نویس دیگه هم بودش که اسمشون توی Release note میاد و contributer پروژه هستن. من شاید 20 درصد از این 10 هزار خط کد که اضافه شد توی این ورژن رو نوشته بودم</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/3853" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3851">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yi3IthhxtRU9VhYkDXZt6YifaGJ6K12Vdrz6ZM0DQjKcV7hRZir5dxEAQpMzNJN6txFm7hviAjVmCwD7T-w82gvoVmeGaqYOnNFpX9EF7WGy_yZZk07Vxqn8VpWy6X_EmPsneQG9PXy1nJ9L4n5HJJXuO5nB_6NIE4aZ2i7qru8W776LFuHpwuhAJ1yFUGtQWc1LOlmCSPRq85sVv2AgyxE7V2aPVhhK3OGEE586xmQesKW0Oqz6dlRF25ok-JdUpZrEEGdkAEPDpqKfhs_xDLeTrYTpa6_UIg-w2ONCwMvNi6ABm4E2Lt-Bp1tDCD3D1iZlpZ3Twwz3bxc7SHKAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mJ7S3ZzNvjFXEzDrfBzsGOT-Dk5m8XPUdRqbC5GQJhWk1yp-0plIBjqtkJ8gmSFu9yCmYRG-7m4LaE5nWtwGCD94ZrWgwjYDXwIjPkL6wDZi5kFeNUIWOv32wRlImFd74tvIzSPEpWWuznTk1PemI4gro8a39G36Bm5Z3N2mnq7Y94CGJ3uzANahRhQTbxuZsKxVs-0kC7FDQ-vC7lnsfyN28lCd0GNUHAWMNTDmt09aBGy4NRcWvukDeUgLuNwpj0q5sY0TEXIrORs6-ssjqX_5PSN3EfNvAigfaRP0nYQQ_bVXD5tvhlH6twnCBBiUx_DYZd5fxOnER2cXUbQpPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvGb33qDX6UQqLhcvbXBPsT4LogH5_b_VOHFpgHkN1t1aBWpWX3RDSYOdyH2t_pbkSKZ3vMEHEVMvisYffa7DOLdYUE2tNwT7meuhB2mu7D-F0SHyRC7s09vy8e9VDoeApUSNHCwlhzvEBjpKGzOL6jwTV7Zc5XJsgyMAwhUs0APEvsaK8Mn_CqHZoSJlR6M_p5X9oMceTMHouh0o_vkmHAmZySir1eXp7JdReaJ8_HN0Bi_b0VrIGaPGfSiHssVP57ZPGVBN_CZpQwAolDy6aF_GD3hBcmB3lZD4T00x0Kr-HXWf0bWt-kkjjEVO8plQGDeWYQelVBnspNhIM-weA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/3850" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/3849" target="_blank">📅 11:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3848">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aANoDoUBlOSTMwwiEjEASUKtYwsAjplLs37TJCPBE0de8NZzN6EDnGSG66WnrDtUxkzS_OL7AYZc_yh2IdfREQn82md6sFr_ll_jo28Gv0_Ed12hO9b70aQhVK0swZZVlcI8LuP68MWUCKm00P69IxAQQ43B7tdisSYOamQq2OA_z2IHmdcIYwBA2GDKDuGjdvb7xMJD0wnBd8cIyc5nwhUESP_bjaczS97Yor6cYedDJPAVz4GwhnkBQYD0Ek7ZzVamU7DUVQLN3OZ_Wi33qX0PfcdSYrGQo7dLZYPRibrh2jD3M3_zXq95R8xysFFgwQHbDreFic3Xw83DBJBYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان خوب، لطف کرد و هسته‌ی اندروید و تمام چیزی که برای ورژن اندروید نیاز داریم اد کرده، صرفا منتظرم که خود اسکنر عملکردش به بهترین سطح برسه، اون موقع نسخه‌ی اندروید هم بیلد میگیرم</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/3848" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نکته‌ی خنده‌دار اینجاست که دولت آمریکا دستور داده دسترسی به این مدل‌ها برای هر فرد غیرآمریکایی (foreign national) — حتی داخل آمریکا و حتی کارکنان غیرآمریکایی آنتروپیک — مسدود بشه!!  آنتروپیک اعلام کرده که چک کردن ملیت کاربران به صورت عملی ممکن نیست، بنابراین…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/3847" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3846">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/3846" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3845">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/3845" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3838">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">32 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خب، دوستای من هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3838" target="_blank">📅 11:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3837">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خب، دوستای من
هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c2M-QNnMoWPgaBkCyNNXDKFuML6awTk90WgpBgcMklHMD4KnqGbaLinJRahw-S_4gVEqSGjqtZz0orLQV8DpP6mlI_DuOO53DGOmya5DOEFG6XhC82KKE03mLqO_yHWx-WVWIR7IggcZodTzIfNUe0k7M7A6qFIhABTRs3BHiGXHaMU59RwEwlJ0Jv1pEYm7lKGwz-qXbDfWPfREjhSZSsdR5N_p3DVueOX4lObYmWW0e9XOwXSgHfpKEFkZQREGtMCCcsJ7XnFOTc9CsTwJVplFgn2D0TL4wTQVAexuBaCW18zw5fRMgN8Md5-wbDinCQ84sZSH9_xfDZLCm_9MsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZ1SLFxgxQFFIdTU2l3tNUwjw0j7fyNvd27snRqofXL1KMV2jD9B2eqyvMBMFpWjAZm72RSk_EFFzpJppiLJRM_ALkBnXCny1878dhODZ5Y9QYMCH_8LWozKieelohS81R8H5xuxwE93NwBmTRvx_Jz5zSNNn9ohPvYCyTfYMBZBlhehmzZO2sc-2YJlLIe9eL00lsTycsLZMGRkmX6a-CmadB8dR_c_F4CfWroOeE5An7EDHt_Y4D-idWw4X0IfbmjtTuye7eVle34r8an7pifguiWfTz0NfHLH5VE4ye9YTPQmRSDM8kpOZoT-Sd_hDNIJ7ibqj10HBiNLqGLwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3835" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3834">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3834" target="_blank">📅 09:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3833">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l0fHyT9NcHerNmT8EEEXL8AQvhMLO2vG2QNe_lRm4aste5IHTaaxeS8HbjoFuE7Y_exslmJ5_oweO2oQQnvumI1jv4cLi3WcZYJXcjsbGJihr9W1qVlbQfFuGyoZrtB1aWxeAeZHIg2yoX56XWcdt9-tXy1XT_PUR3Si3M5ekLJj5TJEx94jUZgiEIjUKfZprh6hTnAE9nfGxWCrfwt1pXFcEMBT4_3Q53qDVxb3ikEsvy3mIamMNI4HtE-SWieESQ2cS7ezeH3sVioOIZ-BFj6-m33vM2tSPdr-Uy0OurL1MNyT-WjsrHAy7xX6sTi7Q7HaytPwbUfTC3pRAy-THA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3833" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v9O3ztuDeicbSRHPEi_obhnmVjTia4_eZweqwUrDEQit-3PLzvtCwjIuA1tQaW3V_TuIzKxE5xkZJOyWIhhsg-IoNfz4sLYejfNTjYSWrgDlhxWl4FLNUr8KoBRNKcNS04mcQ0aQ3gdL4WpWjZPVaTSlwEs_6gUzbzEFr6lBd5I1P1ChwYKTZj5o154TIBYpjtAavz_WTx1uGfLuFNms1Twc55Ht3MON-0-EgwsZcbEuu6HyiHNs0eOH81TrVv4fkxn0BBiv_UgM0VnXwQaKGrq3iZX6QopSTbRudWZawSRw6fiijWTHvjBAUQE1t6033OHEUgPT_kZIe_i964itUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3830">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">من شرایط ضبط نداشتم دوستان. یه مشکلی هم برای لپ تاپم پیش اومده که باید بدم تعمیر و ممکنه کلا مادربوردش بسوزه اگه روشن کنم ترجیح میدم ریسک نکنم چون دیگه پول ندارم بخرم
😂
تعمیر شد، آموزش‌هایی که قول داده بودم رو ضبط می‌کنم</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/3830" target="_blank">📅 01:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3829">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWireguard Configᵛᵖⁿ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=RJXwCzoxJmr7jDtNE6zQvfgWrtimbzCDsyBnLoqHUtBiOfY4_9tn8RbhgUHf2_Sc7nMSonN34_F-2Ux1w2pfVU2fwrQsSV7JNqluGPbUGyZrgrr_EvYXlUxqyFWOzYJaNukXcAaDKAm96tu5PV6pzjWYZinFExlNQAiWLHRbq2xCcejrLFkjmPZloEGmFvX-PWCiFrYmLM9b62uxosENsmjduKj72l7uwLmxChl6PX_47enXYJdP-_ZhWiKBeA6EqH_ZA7ec8RT4ba8uXF5lJmN9yP5IBruw63LDVNLOynYd7CyOrt4shyCQCaAc3rIlK3nGkBxLIGar7wFts2g7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=RJXwCzoxJmr7jDtNE6zQvfgWrtimbzCDsyBnLoqHUtBiOfY4_9tn8RbhgUHf2_Sc7nMSonN34_F-2Ux1w2pfVU2fwrQsSV7JNqluGPbUGyZrgrr_EvYXlUxqyFWOzYJaNukXcAaDKAm96tu5PV6pzjWYZinFExlNQAiWLHRbq2xCcejrLFkjmPZloEGmFvX-PWCiFrYmLM9b62uxosENsmjduKj72l7uwLmxChl6PX_47enXYJdP-_ZhWiKBeA6EqH_ZA7ec8RT4ba8uXF5lJmN9yP5IBruw63LDVNLOynYd7CyOrt4shyCQCaAc3rIlK3nGkBxLIGar7wFts2g7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سا
خت کانفیگ Amnezia VPN
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
🟡
فعلا روی ایرانسل
💯
جوابه(همراه اول ،مخابرات،سامانعلی)
📍
ای پی جدید هم اضافه می‌کنم
https://darknessshade.github.io/Amnezia-VPN-Config/
@ConfigWireguard</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3829" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3828">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کلا فکر کنم ساعت از ۱۲ میگذره دکمه‌ی بمبارونشون روی سیریک گیر می‌کنه</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3828" target="_blank">📅 00:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3827">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tjxCE0LOXg40nzCPiyixP_gYMljKxIrNtBJJQZVm81-DFZ8lvAkpg2mTAfVQiIik_6qIH3W526fIWbqOB8MzVoVa2-Wwyg8fSZiGQU_zpOldr35CfW5hmP4O8sR8IpOJzyuYMXtVohlw598tU4QIFQ2KKWZGIUvJSQHLHNMO3cipyAi8Ik1V3EwXB8A1fl86KNbX0HHz6k66cwd3Jl0o4PQpu_0sXCSTEKA7acCY0DQETi3SulZpctvOmY7_TaGw5Jae5pkqHWqKuyKm42uSDNK9Omq8D8ahI_9aUONm8seIMspJOZipJ4HmLk8Jnv1mP6as0rhbkBRSgkLfS_orzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3827" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3825">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اگر مشکل باز نشدن توییتر با پنل BPB دارید، همونطور که توی
ویدئوی تنظیماتش
یاد دادم، NAT64 یا ProxyIP ست کنید. اگر باز هم نشد، صرفا کانفیگتون رو عوض کنید با چندتا کانفیگ تست کنید، درست میشه.
proxy chain هم صد درصد درستش می‌کنه.</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3825" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3824">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j_fh6SrJhjEnDCIy6bXo09Jdfsc6tJPHJa861ertu4mpB9WuPklVrY-mbNTJGtN2rLRP1DllSOZpheGA47tQpn4s9BdCPVY8Mo73MKAUHYxe8iIHPzUh7vl6alhnnse0DbFdbcgeyBXCigFpB7n7dnca8muNC-9G3UeiGTj9VnU15lOjD9A99k3gieYWiCb7BfHvnMHWFZCSCK6PP6U9cEutxN5Q3XCNHzZnVr3oUDIRw-4isqvGRCLmwa_xj7qUYnxUgfXsQjDIuPrqLGhDnT5SNq40DtWBSg8ZbTbHHsqOpOWXN2y319-CWWOfL7OCiCdvTvw2fqmV_tP5lzgoFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد
توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش
فورک OpenCode
هست!).
خلاصه‌ی ماجرا: تیم MiMo شیائومی به‌تازگی، دو روز پیش (۱۰ ژوئن ۲۰۲۶) نسخه‌ی
v0.1.0
از یه
AI coding agent اوپن‌سورس
با لایسنس MIT منتشر کرده که توی ترمینال کار می‌کنه و برای پروژه‌های پیچیده و
long-horizon
(بیش از ۲۰۰ مرحله) ساخته شده. این ابزار فقط کد نمی‌نویسه؛ می‌تونه دستور اجرا کنه، با Git کار کنه و در طول جلسات مختلف، درک عمیقی از پروژه‌ت رو حفظ کنه.
از اون‌جا که نسخه v0.1.0 هست، طبیعتاً یه پروژه‌ی اولیه و اکتشافیه — ولی معماری‌ش جدی و قابل‌بررسیه.
ویژگی‌های جذابش:
۱. حافظه ماندگار (Persistent Memory):
برخلاف ابزارهای فعلی که فقط به context window مدل تکیه می‌کنن، اینجا یه subagent جداگانه (به اسم checkpoint-writer) توی پس‌زمینه کار می‌کنه و تصمیم‌ها و پیشرفت رو لحظه‌به‌لحظه ثبت می‌کنه. حافظه روی
SQLite FTS5
(جست‌وجوی full-text) ذخیره می‌شه و توی فایل‌هایی مثل
MEMORY.md
،
checkpoint.md
و
tasks/<id>/progress.md
نگه‌داری می‌شه. وقتی context پر می‌شه، خودش از روی آخرین checkpoint بازسازیش می‌کنه؛ یعنی دیگه نیازی نیست پروژه رو از اول یاد بگیره.
۲. ویژگی Dream و Distill (خودتکاملی):
دستور
/dream
به راحتی جلسات اخیر رو اسکن می‌کنه، دانش مهم رو به حافظه پروژه منتقل می‌کنه و موارد قدیمی رو حذف می‌کنه. دستور
/distill
هم کارهای تکراری رو پیدا می‌کنه و تبدیلشون می‌کنه به skill یا command قابل‌استفاده مجدد. هر چی بیشتر کار کنی، بهتر «پروژه‌ی شما رو می‌شناسه».
۳. قابلیت Max Mode (آزمایشی):
چند راه‌حل موازی تولید می‌کنه (best-of-N) و با یه مدل داور بهترین رو انتخاب می‌کنه. که با
experimental.maxMode
توی فایل کانفیگ می‌تونید فعالش کنید.
۴. قابلیت Goal Mode:
با دستور
/goal
یه شرط توقف تعیین می‌کنی؛ وقتی agent می‌خواد متوقف بشه، یه
مدل داور مستقل
چک می‌کنه که واقعاً شرط برآورده شده یا نه — در نتیجه جلوی توقف زودهنگام و خوش‌بینانه رو می‌گیره.
۵. ویژگی Compose Mode:
با زدن کلید Tab فعال می‌شه و یه workflow ساختاریافته برای توسعه مبتنی بر spec ارائه می‌ده — با skillهای داخلی برای planning، اجرا، code review، TDD، دیباگ و merge. کل چرخه از spec تا کد نهایی.
۶. ورودی صوتی، Git و Multimodal:
ورودی صوتی real-time با
/voice
(بر پایه MiMo ASR و TenVAD، مخصوص کاربران لاگین‌شده)؛ مستقیم با Git پروژه‌ت کار می‌کنه و multimodal هم هست.
۷. سازگار با Claude Code:
authentication، skillها، MCP serverها و دستورهای قبلی رو توی یه مرحله import می‌کنه از پروژه‌ای که داشتید با Claude می‌زدید.
۸. انعطاف‌پذیری مدل:
MiMo Auto به‌صورت
رایگان(1 میلیون توکن اگز اشتباه نکنم) برای مدت محدود
و بدون کانفیگ در دسترسه، ولی خودش هم از هر API سازگار با OpenAI و prov/erهایی مثل Anthropic، DeepSeek، Kimi و GLM هم پشتیبانی می‌کنه — یعنی vendor lock-in نداریم.
نتیجه؟
طبق ادعای شیائومی، توی بنچمارک‌های SWE-Bench Pro و Terminal Bench 2 (به‌ترتیب ۶۲٪ و ۷۳٪)، با همون مدل پایه حدوداً
۵ درصد
از Claude Code جلوتره(که هنوز بعید میدونم. به چینی‌ها اعتماد ندارم). اما می‌گن تفاوت واقعی‌ش جایی خودش رو نشون می‌ده که کار طولانی و چندمرحله‌ای باشه — نه «له کردن»، ولی برتری معناداری توی long-horizon.
نحوه استفاده (خیلی ساده):
۱. نصب یک‌خطی (Mac/Linux):
curl -fsSL https://mimo.xiaomi.com/install | bash
(بهترین تجربه با iTerm یا ترمینال VSCode)
ویندوز:
npm install -g @mimo-ai/cli
۲. اولین اجرا:
خودش راهنمایی می‌کنه — MiMo Auto (رایگان) رو انتخاب می‌کنیم، با حساب شیائومی لاگین می‌کنیم، از Claude Code Import می‌کنیم تنظیمات و... رو، یا خودمون می‌سازیم.
۳.
می‌ریم تو پروژه و کار رو بهش می‌سپریم (با زدن Tab بین agentهای build / plan / compose سوییچ می‌کنیم).
لینک‌ها:
- گیت‌هاب:
github.com/XiaomiMiMo/MiMo-Code
- سایت:
mimo.xiaomi.com/en/mimocode
- بلاگ فنی (درباره long-horizon):
mimo.xiaomi.com/en/blog/mimo-code-long-horizon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3824" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3819">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JcRV7mjAsAAYW6YpGcfrRGR-n0pPV1Kg3N55lZdjwpcWZKwbxpzKadMvjz1It-MGNwAw21NcDz6Yoko4BE4JQ3h94QX-b7sbHbMO8iU9h5mDb_YBN4jFiQTdOo65mFeekdu1PxZtwb2gI0g_lYJ4QO6N42LXQVufhb9Z8a-Dh1Vt0uTC7GalT6DI_bv0hBrrwnjxGjMDwiCh3oIfRxwg3JqTmb10KMsXKJvP1NtxTFYvsA34PDk3lAcbCuB41lNRZJcw8i6iZnwFkMHgSmjBFhf20tMzRIANKWtEx1c2tfF93l0W0JYPLNxQkZsRLE_keXDmHWO1167fI8y2MfngTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از ChatGPT بپرسید که
یه عدد بین ۱ تا ۱۰۰ انتخاب کن
بهتون به احتمال زیاد میگه 73! علتش رو هم از خودش پرسیدم:
وقتی کسی می‌گوید «یه عدد بین ۱ تا ۱۰۰ انتخاب کن»، من واقعاً عدد تصادفی تولید نمی‌کنم؛ بیشتر یک عدد دلخواه را انتخاب می‌کنم. بعضی عددها مثل ۷۳، ۳۷، ۴۲ یا ۶۹ به خاطر الگوهای آماری و داده‌های آموزشی بیشتر از بقیه به ذهن مدل می‌آیند.
جالب اینجاست که در آزمایش‌ها، وقتی از انسان‌ها می‌خواهند یک عدد «تصادفی» بین ۱ تا ۱۰۰ بگویند، عدد ۳۷ بیش از حد انتظار انتخاب می‌شود. مغز آدم‌ها از اعداد خیلی گرد (مثل ۵۰) فرار می‌کند و به سمت اعدادی می‌رود که «تصادفی‌تر به نظر می‌رسند». من هم تا حدی همین سوگیری را دارم.
پس اگر چند نفر قبلاً همین سؤال را پرسیده باشند، کاملاً ممکن است من دوباره ۷۳ را گفته باشم
امروز توی توییتر اینو دیده بودم و واسم جالب بود علتش</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/3819" target="_blank">📅 15:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3818">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jifILi0Wccwz9c5mUuP-sziDX-quPsV3Tn4WV8vxkHnscYt33lBKUATP9isYTEKg4s27csWBOAVAAwij-PnZ2gDbS1MRcX2SRJdNpy3DgzVWAJ9M9kyDZ4hFxGwVHP0KEmlJI_s3nFtW37LFqXG450qWDRI7Nu_73KQMNrh7HA3LYPSv5F4xD7UKcH0waK7a52f7YRI7NSV9RTl8IyGu7dDVCCYFP8kvkAAfIBW-WHAe62vy43U4rWDVbL711Zb9850QzJ_kY3Db-7EgzHz5zRC00VtE8uLtf-4O4LhhJF7YrfwHjrZd5cNb5UR8DXndjpCkr9rDjjGPxKx0QWqMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار باحال آنلاین پیدا کردم: یه عکس می‌دی بهش، بهت گرادینت میده با کلی تنظیمات.
برای وقتایی که دنبال یه بک‌گراند یا پلت رنگی هماهنگ با یه تصویری، عالیه.
تو مرورگر کار می‌کنه و رایگانه
👇
photogradient.com
‎
✍️
Reza</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/3818" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3817">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
ابزاری که امروز معرفی میکنم...
داخل این سایت میتونید تمام ip های مربوط و بنا بر نت خودتون چه برای ورکر و کلودفلر یا شیر و خورشید اسکن کنید
❗️
ویژگی ها:
💡
اسکن راحت و سریع و دقیق
رابطه کاربری خوب برا همه سیستم ها
داشتن ip بیشتر cdn ها
لینک سایت:
✅
https://cdn-scanner-pro.vercel.app/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/3817" target="_blank">📅 12:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3816">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2658a29175.mp4?token=v0NwkSDfjVtXMciUTGntZGa8NyAgFG3SKqCvNOXsrIbAvxTa-z-ynfSpLXZ6ssZMF3Tg5_EXubqhTexur6Kj3HBYMSRc7lOCkVO8Ga-k7N4YCNCmhUZf5VfJ97-OrYleCXQtc2VYlTR6N6VUg_7Rw-taqf4J69iO8gq7Ajq5aJ3ejpcxQy_wRxj7fWJhadlVARxV_-BmXqm-FZQ3DQ6Z59VHl8OFyN75dGl5Ba8tm5-gZ47CEAhKKPmVtqCYeAz8HxHdrrVCD0IIyLDkv5RNdVj5uJ70L9JQtERtq_0UdBnu-03UEtDuxT7QQKxIPbt_4HaIwbujFGp9UyloJm2_Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2658a29175.mp4?token=v0NwkSDfjVtXMciUTGntZGa8NyAgFG3SKqCvNOXsrIbAvxTa-z-ynfSpLXZ6ssZMF3Tg5_EXubqhTexur6Kj3HBYMSRc7lOCkVO8Ga-k7N4YCNCmhUZf5VfJ97-OrYleCXQtc2VYlTR6N6VUg_7Rw-taqf4J69iO8gq7Ajq5aJ3ejpcxQy_wRxj7fWJhadlVARxV_-BmXqm-FZQ3DQ6Z59VHl8OFyN75dGl5Ba8tm5-gZ47CEAhKKPmVtqCYeAz8HxHdrrVCD0IIyLDkv5RNdVj5uJ70L9JQtERtq_0UdBnu-03UEtDuxT7QQKxIPbt_4HaIwbujFGp9UyloJm2_Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیگما یه اکستنشن کروم منتشر کرده(فعلا برای کاربرای پلن پرو) که با رفتن توی اکثر وبسایت‌ها، می‌تونید با یه کلیک، تمام اون صفحه‌ی وبسایت رو به شکل فایل قابل ادیت فیگما دریافت کنید.
برام جالبه که سر بحث کپی‌رایت و اینا کسی بهش چیزی نگفته هنوز
😁
اما خب گویا هنوز با چنگ و دندون قصد دارن نگه دارن اکوسیستم فیگما رو بعد از اون سقوط سنگین سر Claude Design
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3816" target="_blank">📅 11:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3815">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!  همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.  بعد…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3815" target="_blank">📅 10:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3814">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fPl7zecCCO6j94moqj3BcE0N_4hPhUo7cOHOsWm-Tho1BdVM7Du6YeWFjaZDdB1PPBWBv6V4Xh5jU7zWG1H2bsLYEllrpFWKqSKpi7spaw3qOCdUY5gShdgGnU6dW4x0XBE8M6-qVzQJcAz7cTLtbqnBaYdspRzOvhI3igQAMy0RpmtuN7-w87Bboa-3wOYjqUgX8frtV7F6O_49wtovNuPnimtFDqlJixMqAdlhwW1hFoC2yqaf4cfQ_MkZ6Fw6_6_Pnp2--KPnSJ7mnf6AXTLYjmUQhH_MH5nRMCy8EWeQbTpkl3siEbyqOWwZTbyap4MexUDLoFSu_VJhNXLeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!
همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.
بعد از چند دور summarize کردن، نهایتا بخشی از دیتای مهم از بین میره و تسک به صورت کامل انجام نمیشه! پس اومدیم یک سری تکنیک پیاده کردیم مثل تقسیم کار بین sub-agentها تا از پر شدن سریع کانتکس اصلی جلوگیری کنیم.
بعد این ایده مطرح شد که بیایم هدف نهایی (PRD) رو تعریف کنیم و اون رو به تعداد زیادی sub-task تقسیم کنیم، بعد مدل رو در یک loop بندازیم که با هر بار اجرا، یک context و یک prompt جدید داشته باشه و بعد از هر iteration چک کنیم که تسک به صورت کامل انجام شده، و در غیر اینصورت چرخه رو دوباره تکرار کنیم!
در واقع به جای اینکه برای اتمام تسک به مدل اعتماد کنیم، ما در یک لایه بالاتر این رو validate میکنیم و اجینتِ تنبل رو harness می‌کنیم :))
✍️
Amir</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3814" target="_blank">📅 09:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3813">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VoZZbEVFMk8DQsdiCF1jnxYWzLMJE1lnOOagO-3AHHz4XBN5TH_tBOHpnHQi5o4j3Vr5UPYhCl9gMWDgppGh3N5bibcJyQWRGRsYwxQjIg3pVMJ8RsvODgqnsK3d1ZEUqABWFNdT6MGuFBWSp07ckwDQQHSQxtYukGlE2ygdiUSR13Tb48jFaFScnqGQt_fS199lGoSaBsGdkeqTi6qJA2gQ-JW63JgW8wdg5fNgOtL9Zr1WmlWV-AGtL-UIf7UDBSKaWt34zaMKfridthRInzChfHJ_xUWFqAgX3pAP01FZTCV1QMfLnQXXnu3DWBGe7In8IVhsh6qUMVHqSAPkzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله شما می‌تونید دامنه و سرور خارج رو از سایت‌های ایرانی هم بخرید، اما چندتا نکته وجود داره:
۱- احراز هویت سایت‌های ایرانی کلا جالب نیست و خب این ریسک رو باید در نظر داشته باشید
۲- توی شرایط قطعی، فروش دامنه و سرور همه‌ی این سایت‌ها میره روی هوا
۳- شاید عجیب باشه شما اگر از سایت‌هایی مثل netlen و با کریپتو خرید کنی دامین+سرور رو، شاید ۸۰۰ هزار تومن(با کارمزد و همه‌چیش) پات بیفته. اما همین دوتا رو از سایت ایرانی بخری زیر 1 تومن نیست</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/3813" target="_blank">📅 07:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3811">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نکات استفاده</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3811" target="_blank">📅 01:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3809">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FXRmHGMpcfsPcX_eWJnm-TpQvM1CJn9l9XdVQQ3lg2L2tCU_oAtGT1TAT_GwTVtreY6n3lXkntmOtiUF0I0KTINkb8yCTer7tKik8XlAv85TYbTgzYIih25O7Y8SONOqLJZAc-yUSLt0o5PMV6mKosnQzYBvoTWuret1cuI7sQDoOcm8jeRvfLjMbjlsGBhzFkxReQkFp-S3h4nwESyIsHgtCTHWUMhl0EB-AHWUOzXkTna7SSez9eRbVVutWMbIXqRbmIpeOXT35LTP9qCamCNEfGn-MSZJuPgkPbfY2fPYaTJb5-_ts5eVGpH--oq0C4bUuRAx9GxnCpFCrnuPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran  * دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)  ///  * حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)  * کافی است لینک subscription را وارد…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3809" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3808">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3808" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3807">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XRehAUFOXRHAtNONN5jMG9bHT-ohyk0UtVDG4Z5s0RAdU9cQOulL59Y3E9l2LUwiSjt8jOif8b4OX2zUcx0kBPeUo_AsPQNsq-aYkM7PzeawUhYfGFE6Um-leUJZKqynQsVlEmdUVdHbdXC1ubxsBTic2ItaZS8AoBu8CC1JiMW6iujcKdZ-p98ERsU65Hne396ROPN4xDv5j0rKPTKFdRl7_bl399FQZ8duYgC2EVhHQo4sDieALjw6pP7YODg7kVIWfKMKXpvQfSLQDBJd-nchB5Riq-YzdzrvKAhjGMOqcHySkXrlaBWI5-2lB4YWKMBDQhw1WWvEEqWxaw8c2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از http://Netlen.com.tr بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰ باز هم خود دانید</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3807" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3806">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">درود به همه رفقا
🍷
اگر از پنل bpb و... استفاده میکنید میخواید ip ثابت باشه ولی جز لوکیشن آلمان
🇩🇪
میتونید از ابزار زیر استفاده کنید برای ip های مختلف برای مثال:
میتونید از ip چین استفاده کنید برای دور زدن تبلیغات یا از ip آمریکا برای بیشتر هوش مصنوعی ها خلاصه این ابزار مشابه واسه خود bpb برای ثابت کردن ip هست ولی با لوکیشن بیشتر
❗️
لینک پروژه:
✅
https://smart-ip-scanner.10-354.workers.dev/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3806" target="_blank">📅 22:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3805">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید  محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان»…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3805" target="_blank">📅 22:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3804">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WYp4An1ryXSHD_PBHoeQlFZ5OwW7guYOVQ7vFyMg1QGTnixf46jrqNDSqJ3AOnJ29-Aum63Wp2Lda3KpvelTOlGoI9TwDwLGThOnK1nMREpJIBccvw3T7K-hHX8QmDTwnethGfEpX3d_ClVzVKxIH5Xlt8Rq2LLPnz0Lb0YESPpSPqIYpk6f-Rfr-gWw-l2r8eB0Qk8ciYfRAsTJft-XxXk61ANEGC1Y9KvKMZRwuFhKmCV6jVsAfR2Pq0gA_0Vc5q6L4MhR4rHkAiMZ7ybYCji8eipCm0sBKKt70tb34y8RowvfNtH92g92PaxUv4AqtO-rNgppAfKKx79Pa91AtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید
محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان» (X-VPN) است که برای نصب بدافزاری به نام STX RAT روی سیستم قربانیان استفاده شده است. این بدافزار می‌تواند رمزهای ذخیره‌شده، نشست‌های فعال و اطلاعات سیستم را سرقت کند و به مهاجم امکان اجرای دستور از راه دور بدهد.
در این حمله سرویس ایکس وی‌پی‌ان هک نشده و کانال‌های رسمی دانلود این برنامه سالم هستند. خطر اصلی متوجه کاربرانی است که نسخه آلوده را از منابع غیررسمی (در این مورد، یک مخزن ناشناس در سرویس Bitbucket) دانلود کرده‌اند. در پاسخ به این تهدید، ایکس وی‌پی‌ان به‌سرعت آپدیت نسخه ۷۷.۵.۳ ویندوز را با کنترل‌های سخت‌گیرانه‌تر منتشر کرد.
➕
نوشدارو پلاس: این هشدار مشخصاً به نسخه ویندوز X-VPN مربوط است، آن هم زمانی که کاربر نسخه جعلی و دست‌کاری‌شده را از منابع غیررسمی دانلود کرده باشد. طبق اعلام X-VPN، نسخه‌های رسمی دریافت‌شده از وب‌سایت X-VPN یا Microsoft Store تحت تأثیر این سناریو نیستند.
▪️
روش زیرکانه هکرها برای اجرای حمله
این کمپین ابتدا با نسخه‌های جعلی برنامه‌هایی مانند «بایننس» (Binance)، «بای‌بیت» (Bybit)، متاتریدر ۵ (MetaTrader 5) و کیف پول اکسودوس (Exodus)، معامله‌گران را هدف قرار داد. آن‌ها حتی به سراغ پلتفرم بازی استیم نیز رفتند و در نهایت تمرکز خود را روی کاربرانی گذاشتند که از ابزار تغییر آی‌پی ایکس وی‌پی‌ان برای حفظ حریم خصوصی بهره می‌برند.
💡
نکته: بد نیست بدانید شرکت Kaspersky (کسپرسکی) پیش‌تر متوجه شده بود که همین بدافزار با نفوذ به سایت CPUID، بیش از ۱۵۰ قربانی را در صنایع و کشورهای مختلف آلوده کرده بود.
بر اساس یافته‌های شرکت سایدرز، مهاجمان در فایل نصبی اپ‌های معتبر یک فایل مخرب به نام CRYPTBASE.dll جاسازی می‌کنند؛ تکنیکی که به آن «بارگذاری جانبی» (DLL Sideloading) می‌گویند.
به دلیل ساختار سیستم‌عامل ویندوز، فرایند نصب برنامه در ظاهر کاملاً عادی پیش می‌رود، اما فایل پنهان‌شده، بدافزار را مستقیماً به حافظه دستگاه تزریق می‌کند تا آنتی‌ویروس‌ها متوجه ردپای آن نشوند. پس از فعال‌سازی، بدافزار می‌تواند ارتباطات خود را در قالب ترافیک عادی و قفل‌گذاری‌شده وب پنهان سازد.
▪️
چطور قربانی برنامه‌های جعلی نشویم؟
دفاع در برابر این نوع حملات بسیار ساده است و نیازی به دانش فنی ندارد:
• دانلود از منابع رسمی: برنامه‌ها را فقط از وب‌سایت اصلی شرکت یا فروشگاه‌های رسمی دانلود کنید. این هشدار برای ما کاربران ایرانی که اغلب ناچار به دانلود از منابع واسطه هستیم، اهمیتی دوچندان دارد.
• تایپ مستقیم آدرس: برای جلوگیری از ورود به سایت‌های مشابه و جعلی، آدرس را مستقیم تایپ کنید و روی تبلیغات کلیک نکنید.
• استفاده از نرم‌افزارهای امنیتی: داشتن یک آنتی‌ویروس قدرتمند و به‌روز در کنار رعایت اصول دانلود امن، لایه محافظتی محکمی ایجاد می‌کند.
اگر گمان می‌کنید نسخه جعلی را نصب کرده‌اید، فرض را بر لو رفتن اطلاعاتتان بگذارید. فوراً رمزهای عبور خود را از یک دستگاه امن تغییر دهید، از حساب‌ها خارج شده و احراز هویت دومرحله‌ای را فعال کنید.
✍️
یونس مرادی(نوشدارو)</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3804" target="_blank">📅 21:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3803">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cLBmXp2-jCnOA7UPlVA-ouMdRAG_lWF6bA7yZsqp92rH7nC4FXRgioa4f4jCK815PZP7l4RuB664feV8UGNfsWvBTpBah7PrRxPUCVsiilOMUXCu-rwIHnWozwfF1XiSRzCPHSsYxoCyo03zeXIxHr_MYrEUuv4rg7prf1pICwE0-1wjFc2AwwG2k0LQ9HxUoaCr7Ch-Wu3iB9IauAdZz3gEL9NNE-J_drwhZ9TvMDDLxO0AJO9y_zI9ylMYHzv8E5_stYc6EjIQhCyYQIHUHn5jTowe9FK3mG_3dghUlmAxel0WN0OqUqdb8OF6omIu1DxiooAA8gWfMiTZ8KZjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یه نکته‌ی جالب از کنفرانس WWDC اپل!
توی ویدیو هر بار که کلمه سیری گفته می‌شد فرکانس‌های ۳، ۴، ۵ و ۶ کیلوهرتز صدا رو کات می‌کردن. چرا؟
برای اینکه وقتی دارید ویدیو رو می‌بینید، سیری توی دیوایس‌های اطراف شما بی‌دلیل بیدار نشه.
✍️
Behrad Javed
منبع</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3803" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3802">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اگر از
http://Netlen.com.tr
بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار
یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰
باز هم خود دانید</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3802" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3801">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ببینید واقعا درک می‌کنم که ۶ دلار هزینه سرور و دامنه براتون زیاده، اما اگر سه چهار نفر با هم بگیرید بهتون فشار نمیاد. همه هم می‌تونید استفاده کنید
برای من سود و ضرری نداره صرفا می‌خوام بدونید که با نفری ۱۵۰-۲۰۰ میتونید راهش بندازید</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3801" target="_blank">📅 19:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3800">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-poll">
<h4>📊 میتونم بپرسم چرا هنوز راه ننداختین؟</h4>
<ul>
<li>✓ هزینش زیاد بود واسم</li>
<li>✓ آموزش پیچیده بود واسم</li>
<li>✓ حوصله‌ام نشد و بعد از قطعی مغزم نیاز به استراحت داشت</li>
</ul>
</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3800" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3799">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3799" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3798">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:  1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3798" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3797">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3797" target="_blank">📅 17:14 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
