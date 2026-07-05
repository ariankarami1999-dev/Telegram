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
<img src="https://cdn5.telesco.pe/file/fSsmYNny0YvDsYuPTvA9evFABbDAKoMe0NNYiteGpzD4vzJ2WtJZHB2ijmL0rsudSE8z7bdM865l7teX2WoYorq3mo5zhOFYQu_D3gh4rD3yL5n4nmuW3CCHsLYZiCyddUC4GvExwwI1fmRVxXCPg6pw6xh5f7xOVc_iwmyAs3ZGtqPyWDdGYG021WH7Wqj4uzqAB43CFtvLYN5vN3slkyscJrBMChMGAI-krAD3Wjqn4Itvyh42WT2QKya7w1QozpKZGEZozHzRfZEGv8LJg_KqUJRdDvnFvfiLOHvv6zJw-loQCqMMD6Kv_UnWQ2GjxwnAWkPS3ibE1un0i1wenQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 633K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 21:30:48</div>
<hr>

<div class="tg-post" id="msg-98343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys_Hc91sYFkFgLLGN1IhyREqBgZ0TYgJ0xRGoHIL93VONCUDcxuUPXkQNxUJNYsNcYS1n3tikOwJ5LjYeN0wGlaV5yPff82PiAAtPG9CYcIqMBkvttshTuVNM2mEE_ID-bMG3J0ZFZocQwZ9wtHLPHgC75UNrUOm2Rgpt2Ff877-JmQnZXT74ul7C7KzA0EdobT9GFLxmMne0V9s0WvPo_exGrG7gxhglbuH4m5zttTWAfDn5b4NR2suBq5ykLG9AqZLFUERqE7_kUpJb-SekHbuUizspAqKxCeLiFGM3gqVAWECdbAQCpUvSiY713A1W_wDzzfICNQuLkhTFPUXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔻
رونالدو: من زمانی از فوتبال خداحافظی میکنم که خودم دلم بخواد نه زمانی که رسانه ها دلشون بخواد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/98343" target="_blank">📅 21:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98342">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhJ7N0qa7YpP9-5DUmL1ItoJHVJHxPgjBIPPFFK5LrWN6L7cqheN8jlH8HdSfPupoKAvzGKNCZxr6q0_pzTuyPR1tXNlwYzi7HwvLjQPalJTUhMpvBIULXcmBqI969V1CMNRY36Lmd-MCn-Na-OTWmSey1VU2NLoR0GXuRd3_Nf0tI9J-BAOEP82iA4Az3llALuVliaQOU_QNpp3oJX66UP5tycKuQ_iNM7wUilDJH3qARyWbt1szbxjfXboMnsOrjVZncCJwjDbxMREIMT_iLvfRtWIOnu4b6dqaVf3O_-icOho0oUvx3qyoeOC2NAea7hngt-EawjLAHblxJgOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
نخست‌وزیر کشور کیپ ورد پیشنهاد داده است که روز سوم جولای (روز مسابقه آرژانتین و کیپ ورد) به عنوان تعطیل رسمی اعلام شود و این روز به نام "روز کوسه آبی" نام‌گذاری شود، به مناسبت عملکرد تیم کشورش در برابر آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/Futball180TV/98342" target="_blank">📅 21:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98341">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ha7dRAk-2VvXO3g-hudbpFuvuhwBwwRw_oF9VvFOJT47UXSmfJBDd9ab1QS5u28LObf9FVNTQc4fYS2ZGPFPn1Gf1oIo1jWORw2dLm9EGPV-VkQb3SwBbkF5kzO7eMJivAkEAlzeWmmgM5r3GmfCB88rE1fvus_JMjsfRDhcmYka5jtdCleYb2Ku_4-PA3o_xv6nN0jgKP7F488dg4VaPFnlDSjIGuSuNr_OhNEd_VYMFpe5Ov0TjIwjF8IpH1IWLn5xAoeRmqkQEMAffNmI7kdCHQBSggvcAg2TJdrPXx425MOTpaUX9zrxu-v_q2gYZjN_ly89BEpzN1UD3W8ZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
احتمالا عمو ترامپ بازم دست به کار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/98341" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98340">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFjGqv5j0qBl6M_N8uQQdyxCHtuB4VSexsjxFlrVa0__-RihiZqdp-gRn2FpJ2KCCykWGetBag8Elqp4flmKXCYzNFYbjDZMlYfqcOT_7AVZ1XGPcYktnSmFElHzUDVfPz2KXFlzpqmg-aumKCLWktT7QDEdvUuCHVdk045iAZ2JFWuzg8eJVSf1Z-Knizi6NW2_Mz4RaPqebvA4OchHkiX0MY_puOU8qGa9gQ_njly0aQN9aHFiI4gQhE0k2fsSuhf_S4xpIJmofipukgI_2AuhN7OilwhqmbAR89WRdhpbe99uDCwmsIXh881KuQ8_BUZf_kmEx5-viArLacg-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
انریکه:
بهترین تصمیم زندگیم قبول کردن پیشنهاد پاریس بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/98340" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98339">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/Futball180TV/98339" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98338">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p0amoO0AIe-_QzSwGZvjF4l2r9DteHpIL4xI2wynms1BZ7ugpASDs5Aic99b15geXEzgrD7Ee4wbYG7dfgz464FnKHyid5TJC0UapVP7O4C3PSKzVem-sB81v9Mlme3c3_eJXjY2hS7DQqaA-7oTF3YC2m8YCLKIrORdQ_bXhElr_wWxyyWYz36-1WijjV9nSnUTm6fy9OOXuVj9lBuT2Il2TWaySeec9GDyGR2wQgguW7qQc6jFuqN2XBLuEoJb6NX_Bu2Dnohf2F8o4boO5Oya3YotRj8gNOi5l63anCkZw2go6Q15PQpiqXVau3yxTvQDzFqkGVmEHRVD4jQ-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/98338" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98337">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b463de3d6.mp4?token=Ine9SPejCNsV9hR7RjC4tTQTtpTcy85JoGBuQhqgYBLsYfmpt7BiGjWD6_UgvvAG08rzrUVEHk2euWKix-dQF9B9iPyaOj7fW9CrZVzaFbBLtl4-Ty6jYWvLeN_UXIwO3ewcKFMQApnFcIBKfkbvTniZn-ncoqYah6UcXyfJoSzTelCjdi70ZfITdKct4hCPWAtqHt3ErfDWC3q0z50zQr2VvfCHKqOr42LrcwetH-yyDyFVKsPIMVABelOeSkGH5hDHyKLAjvJQHHX77qDuSIxHb7HFDDGgGXHBWvtF96Z1cCni_cjtvymd4WKoq6XvLaoXwM-dqzEgl4MLrznEbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b463de3d6.mp4?token=Ine9SPejCNsV9hR7RjC4tTQTtpTcy85JoGBuQhqgYBLsYfmpt7BiGjWD6_UgvvAG08rzrUVEHk2euWKix-dQF9B9iPyaOj7fW9CrZVzaFbBLtl4-Ty6jYWvLeN_UXIwO3ewcKFMQApnFcIBKfkbvTniZn-ncoqYah6UcXyfJoSzTelCjdi70ZfITdKct4hCPWAtqHt3ErfDWC3q0z50zQr2VvfCHKqOr42LrcwetH-yyDyFVKsPIMVABelOeSkGH5hDHyKLAjvJQHHX77qDuSIxHb7HFDDGgGXHBWvtF96Z1cCni_cjtvymd4WKoq6XvLaoXwM-dqzEgl4MLrznEbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
سلفی ماموران امنیتی فرودگاه آمریکا در بدو ورود کریس‌رونالدو پیش از بازی با اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98337" target="_blank">📅 20:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98336">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
رونالدو در کنفرانس مطبوعاتی قبل از بازی اسپانیا و پرتغال حاضر خواهد شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/98336" target="_blank">📅 20:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98335">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaaGVHvQzkjHQiHGtQ06VqtCtijvka3Kv6DQerB9rrWpGYEIDKq0hEoEJGs-iZZ8YNbkaRSAkzfQHXPMhY3Lm_SjaaTUoECQ-P92ld8eUj34dI-SozWAe3p79ufUOiJQXb93bCk183tma0GVRA5kwZyi80Z_2eyHhoeqMA1y4lgU9IvTlMc0drLve7BD1rPqs2KpoPS1IgDU8z3AyO1bgyLC13a65Lal49YqyFP7ZO9I-2ew5006RLAsrAdVjMBCcU1gBUZOvny_BEOadc2F2E8amg10Eh6pRmabCv2DmuPayMZ29w3A5jRlAPbr0Cw-ARTFSRGL81zE2Hvo0lE13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری و #رسمی |
🇺🇸
❌
با اعلام رسمی فیفا؛ کارت قرمز بالوگون بازیکن آمریکا در بازی مقابل بوسنی لغو شد و او در بازی با بلژیک به میدان خواهد رفت
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98335" target="_blank">📅 20:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98334">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW04WFGxa6IDwBTU4ghaBDLiJaq29PUHBZxM2oz7dF9txgacRI32NJueNFcsyGRB92_vNsmCc3pBR0pagTK-jJqZI1p6yb5cxUJuPJT41E1okfSw1UTmlu0Qgqw1IqrFcdmZ3P1NWiR51ar6r_3M5mbiC-r-73VeRAfXPyclBqgSKvyfSmNY2pdGwzcYYsNKqKvOW6l1z71uNMPXW9rJ181FJRKDIi8o_g0po-x2fy1bUIViVm8o-loIo4MJiw7IE1kjwGRzWJgCiVdRaDMIjyRIVBNkz-idXN8ETIs1O-XIY8G2Vn1yr7Ips2BxvaW9WV5Hwaefcdq_QIN4wCa89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
و
#رسمی
|
🇺🇸
❌
با اعلام رسمی فیفا؛ کارت قرمز بالوگون بازیکن آمریکا در بازی مقابل بوسنی لغو شد و او در بازی با بلژیک به میدان خواهد رفت
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/98334" target="_blank">📅 20:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98333">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBl0vKiDG8PrQho9fyzQxUhWdYQVq4685yWP8GocJgtRFMBzvK8BEXrm5SbS1aYH1tNjx5STw7WO3udYjMO7fyEDCpyELHr8cSQKaogMZmkw640XwjRjH8o3TbtcpDTYm1XibhSPvMjbfuptcXwJERpSdAj6M-bpKCI75JnHu9KvypXuJS68RvkjRuA_hoL4F6P1oikNxwBKqbcWvEtQyD_h0QTCCYrCTA-uDqCx7LxPgTmjNN3biV_GJYePNQRLosxTWcg3K3zk9m1RrL9mcRP6FXpo2n9diVzgFzE7XcUhpN-_zfivBAXCvaAj_sEImTXPqwkt0JgkMbatKOBTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
برزیل تا حالا با ۹۱ تیم ملی مختلف بازی کرده، اما تنها تیمی که هیچ‌وقت نتونسته شکستش بده نروژ بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/98333" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98332">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🤩
#تکمیلی؛ مهدی‌تارتار برای تقویت کادرفنی خود بزودی یک‌مربی اروپایی را به باشگاه پرسپولیس معرفی خواهد کرد. شنیده می‌شود یکی از این گزینه‌های تابعیت اسپانیایی دارد و در چند تیم مطرح لالیگایی عضویت داشته است
🔴
همچنین تا این لحظه کریم‌باقری نیز در کادرفنی تارتار…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/98332" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98331">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGhkJuJWyKmHVKCuxIKNUV6FtkU7aYdbEvceqoUXq4_yW6wUKyb9uac3DKqeGAkV2oqwEJzczpBZuKOLCQTatSfD6MD5GK5JDZN9h1XvjvqzckTR22dExqCnPOyBIumDGFKbVI41tAWGfr0Glb5sl56fRS-MgUrgQVwVhDU9JBPXEHVlRh_i8OVLGPDpurTz0cKwayY4jSYqXpq8KtSU1RIDseoeuB9-MjCX-Gf7m9VPog9RcsRtLLSP8QWHuIhEuzOYjOPsmxzg-1aAZIex_qX8nXrixICeK82ACE7UmX6liHBo43PhzjFYYF52jBC-k-rIDhWZ9pMfq_Vui9X9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
برزیل تا حالا با ۹۱ تیم ملی مختلف بازی کرده، اما تنها تیمی که هیچ‌وقت نتونسته شکستش بده نروژ بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98331" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98330">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHZtblVgry6yC_PW-MIdaZeW3q86k1TdIWAlmLE4cXLvKmlWqKepDYel44amg_7ctXXT-CIAQR_wXvhZtdUB70PZKFZag2U0M189inQEZU5xnT2nrfqk1doEUXttbB1C8nOCqtP65N6Woeo5Iwam--C-q9C2FugfU5fZMbkRAsDZTMJ0RD5x63bVV5wbLmHpGxV42WZjLO1_iEpVnl8VlszyHtUzg6HlJS3-s2MG7jSj3OXg2-IJKFJgF2CO3aJjWEjUUR1eIqR14YVP6UWSIBBJ3YZMeGl-v_sub3GPlmonLqjcO4oZQgWOsL2Z1llUXlV5WACh-12XETj0s4nmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب مشترک بازیکنان انگلیس و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/98330" target="_blank">📅 19:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_PQ1S-zSxqrVpzyvo4NwIohrRid_LkYhMOyXNgNZ9MTbZZPHsiA68sbmlw32pdVT23fTisYJD14Jbg4H_hSshLnrCqs2jW8Qm_oC2o8PoR0NqTGCVoSj5zHDXUhlALkxUTnF1sQ6GUhXKf3jWL4EA4QwpQjQ7U1nTeBQF6QMheAbgLC3wC9JsY4AoBm8IGMSwVlAzNGAx79L4YFBFS0PONaSAXaExTtprc1YSuQRxtgWllqma0Sp-QxS91zLWA209TE_RPODcH3HaNnIuHPCGAhAsXs4y4iCAvll0eUMoNY1k2O9PnBvHQ9EThAkNbL2VsRcrq3hSFgdvhd-0XeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇲🇽
عملکرد تیم‌ملی مکزیک در استادیوم آزتکا
🏟️
• [89] بازی.
✅
• [70] برد.
❌
• [2] باخت.
🤝
• [17] مساوی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/98329" target="_blank">📅 19:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jy-TtPi1EX9TRBjoSbel_WDQ7H79XCr9yNBAW893ztSYzqESeZynbNOW7nPVZihwRAoxdD62wI19xnKKLKOKomg2w_DG-IXNDJ5CFLdNtcC1KFeCZ_3CXYpZHXeij57nw9j37kouB6-Thu5rcWwBzl-UwsHIMDTRlIFRV97SHawtfOt9-cMVgqKhRLr3zc9sRA9LHWOLWo2yTb7xKdpYH0PemTPT8vKd4fZRxi83xVNj-mdyqMRGw3p9sfM5yFNlmcDcx_GhaPRPT_vKdP_j-YjnsPM1QQmHi390_B-kPAV5dKAv7XZb5qqzv4YKCaOLU3DzUozkOSmE7b6Q0i-yuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
⚪️
#اختصاصی_فوتبال‌180 #فوری؛ حداقل دو بازیکن گل‌گهر سیرجان در فصل‌گذشته بزودی با پرسپولیس قرارداد امضا خواهند کرد. یکی از این بازیکنان مهدی تیکدری است که قرار است جانشین دنیل گرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98328" target="_blank">📅 19:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7mhbs-fkHeVcmYC8teJL1xRuxbEQCWGrMzzUuX5GrOHsH8Wnc1TXp3nRpu8SuS3SxkR3a16PnirqKwligl-WUGvkpJHO7VODggIoX7F1WWXRnAHNGBltVLsj3JfIiP79qgedocwYbqw5ussfUCnGT1v2laYL3FogW116j36TMVjvbu__ucCLI3tblisa-Wz8lBFF1TFFU1Mc7NM8xTqqQqoAFf-WszJC2dsMyPhpAs_i-8Xgtv7vVzIGo92te3ujxg-U58uwLi_xdjstQEOSjCs-VpO23Z9IeDs108hc6yHVE91-3yzW8zo7FRd82CmbJzW9mCCrKebvsGnezdbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇺
🇩🇪
یک شهروند آلمانی پیامی برای لوکاس هرینگتون بازیکن استرالیا فرستاد، پس از اینکه او یک ضربه پنالتی را در مقابل مصر از دست داد:
‏"آقای لوکاس هرینگتون، اگر روزی این پیام را خواندید: یک قهرمان لیگ قهرمانان اروپا، به نام لئون گورتزکا، 31 ساله، که برای بایرن مونیخ بازی می‌کند (تیمی که 6 بار قهرمان لیگ قهرمانان شده) و برای تیم ملی آلمان که 4 بار قهرمان جام جهانی شده، بازی می‌کند... هرگز جرأت نکرد که در زمانی که کشورش به آن نیاز داشت، یک ضربه پنالتی را مقابل پاراگوئه بزند و شما این کار را در سن 18 سالگی انجام دادید. شما بسیار شجاع هستید و در چشمان ما قهرمانید."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/98327" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98326">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR_tWOCzSVaGBav7-QdxxSoWZWsp10pi7KrH521nezScAGJ_WgloFSLQAnIk3IJTZ0VXa3NNEk2FSrC7MwfATIm7cfqJv1rHR2BoxHKW7_u8Dgm1fmTabvyWVZ7zMqk7t0vD1qrEpA9wYQJ78Mk4qrqZTdecTGvvHmqKBN8BD9Nwfy-iPA41WJ1T0Swba219n9g1ZIPMd1TjQYLQ6AWwtJJEKHr2e2-l1yKK6428GHTUYmAdf62ro87_hs2lVbnCjWLnpK5nYP6GKSR41cFomaxR544Ft-wdVITzFGUGbJKaKvJXFUHBVHT5YjYrC6N-5UTOu8FM_-eeGowXkXGFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرانس فوتبال اعلام کرد که کسب توپ طلا بدون حضور در یک باشگاه اروپایی امکان پذیر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98326" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a3889ca0.mp4?token=EvBbiiaSCCc1E9XskB3zEgGKf6_UznW3jYBYpab8jeidO_mVYZegPpQP-CSVgouXue1ycD2LA6CBiXg3aHjwEHtq3lHatHXSs46qp8fPudMe5VBpKWHGY0RKIStOcG17boYLVLQYyo9JfU1ATMYEKzzn1pceHpZD1kN70z2bHDopnHWBHZcxITdZFenFr_TtwMk2wX8aNFD-MmQo1Yr0-x-ccpSe9n649ioQDRLOaqgY0Y8mF_vfTidrEF03b35ab6jJyH3Nwee6HDotdKNJX14_DBXdAh2RA9aZDkN_7a0bat294ILRFbiUR2KBXdLJXcdcAr_m4QE43YpstLMoXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a3889ca0.mp4?token=EvBbiiaSCCc1E9XskB3zEgGKf6_UznW3jYBYpab8jeidO_mVYZegPpQP-CSVgouXue1ycD2LA6CBiXg3aHjwEHtq3lHatHXSs46qp8fPudMe5VBpKWHGY0RKIStOcG17boYLVLQYyo9JfU1ATMYEKzzn1pceHpZD1kN70z2bHDopnHWBHZcxITdZFenFr_TtwMk2wX8aNFD-MmQo1Yr0-x-ccpSe9n649ioQDRLOaqgY0Y8mF_vfTidrEF03b35ab6jJyH3Nwee6HDotdKNJX14_DBXdAh2RA9aZDkN_7a0bat294ILRFbiUR2KBXdLJXcdcAr_m4QE43YpstLMoXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو آخرین تمرین انگلیس مقابل مکزیک، رشفورد لاشی برای کونسا شرف و آبرو نذاشت
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98325" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6563ff0794.mp4?token=u7CL4zMYdcx8Ng7v9VrMwDZTBSHeBDp3BYaxCl0HsU7c4NUOz92o7pAmZjSPtZ_nnsqjlQ2LRi1jVyGPFSMJ37MsNJy7kNXch98X2fK8XS0bhgmkXWyRDrE35P6R_JP04du91DMZwTiQqYwocbld9YyJF64J0OhrTqh0afoqW5sNrS-9iarzuJieI7eNqLQ7qIczvrw0szqAPQp8E-OjGxn41MuIk1O2T9pzRZJ8ycuHrRR85oDVbptyTUeEXSN6sJ4XRm7in6mHOBcSRLpIjlWqvzy8nbTjESdKrt-Ws0YHTxWIbHFoawsqEKhMLEV4fpnnrqCU_Mc60c6axJXMkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6563ff0794.mp4?token=u7CL4zMYdcx8Ng7v9VrMwDZTBSHeBDp3BYaxCl0HsU7c4NUOz92o7pAmZjSPtZ_nnsqjlQ2LRi1jVyGPFSMJ37MsNJy7kNXch98X2fK8XS0bhgmkXWyRDrE35P6R_JP04du91DMZwTiQqYwocbld9YyJF64J0OhrTqh0afoqW5sNrS-9iarzuJieI7eNqLQ7qIczvrw0szqAPQp8E-OjGxn41MuIk1O2T9pzRZJ8ycuHrRR85oDVbptyTUeEXSN6sJ4XRm7in6mHOBcSRLpIjlWqvzy8nbTjESdKrt-Ws0YHTxWIbHFoawsqEKhMLEV4fpnnrqCU_Mc60c6axJXMkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
مکزیکی ها 80 هزار پرچم تو ورزشگاه آزتکا قرار دادن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/98324" target="_blank">📅 19:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkHE0xR5nq8M058P5v25yVi7cM3j51E-vnR3drr7m50V1LirpK7kBSaKM1umyBhk8-hEmlhw9GGF1hPdsV-qu9jhlGtQmbZQXX2iZb2OTliXS7kojWHclvuIlSC082isX-XaGsZZ3HfPBi4a_-k8yC2xe5GiUszQIhPNoGhqwb1s8ms6r-3bz3du-ZyWjRjCoJHQUwzWoif5obucyeraTAgHEW3Jz2SuACQwFHN9FZZ8uM5TdrWrT2sHvupDDx_DTs8kqg21xe06HLEsoQdDO8uRXveXMhSEi48Cgs8-Wbbrr8FOkCwVTOAeC-Bglb96FVEQ_8wgIFisZQypYbcJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇳🇴
ترکیب منتخب و مشترک بازیکنان برزیل و نروژ در آستانه بازی حساس و تماشایی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98323" target="_blank">📅 18:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EucQ3z1OcsL8A6E2oKyG5eaYiJPvpVNJbP3XLzLoPW7dZ_sWyuFbIhQfkYdjYRyR6Bqx-8FaEuXE4mP12cxo73r9CRxQdsXQat2hzGra92eVAuGm9FK30IRatYGVxfTlwLWcp1EOWRR7ftBHONOef5TVRmvjho62F7iZdCqhDULeun0CPkSSfKM4z-4FrR449N_dQryh-J9DI6tVkvaxpuYJsWnXi_dbfstRaOD69pPX_-PX9qLDIqCKxUnwm4zhgNiEBRJGnvk1028I34pxNsunfwkYEYlNxJ7sAnytzrFJCq9cmnFTE3x1TCav7l9x__m1xl57fqx2jK5djMcNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
بیشترین تعداد بازیکنان از کدام لیگ‌ها در مرحله یک‌هشتم نهایی جام جهانی 2026 حضور دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/98322" target="_blank">📅 18:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jovvk8XhU6dlGWYjPhaQBky0_hFjdYSaOjOFHBsjt__RQu5ZqeNHJbAXvM7p1yZGuyqDo92WLG6WZiCGKI4OQun2hsVhjm4_lTUlZF22LC8bTLh7NnprhuXR0m3NEcSG0GExEyDdQUvcIf3OAX17fN1PQzMe8ROfAX6SnJPpe3wz39neG2kNuyhswtSgDFrBOFS7OD-73-Ivb9XB87bQnsAAaKdaq3sG1IGxkLwJoHdCB2mH1k8XEdnPFsd223I_AsiM4mNPugiJPJwTNv-VR91V6We1eoFLxo_JcsqTqF7j_lziF2HYAaCD-g869B6xe74MANUAaJAhErAdIrA-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه الاهلی عربستان در آستانه جذب فرانسیسکو ترینکائو به عنوان جانشین ریاض محرز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/98321" target="_blank">📅 18:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eab4140fd.mp4?token=P_nVDjiMyFh72ychm7aHgpN_0UEmH-Erbk1JpVyFLmQ0pCqrCpl4YmNjKsg-7dh9A0iJPOX1TCke9zygxFos5RkIVn-yFZcdNn0eBKRgBCfLAzqiEIPi9N7NYiDmc1FrKX880BljxA3qp6hb8-mVn7fdh09tywvDG_UbD-HbPgT997tV_inBNCtAdsfdcWqBano1twBqM65oD6FBKurbH-fMW4zzH3gspgqjfRYuxwXOsZhPo_3CvMzJFrEAghZJu6RQbje7lVBg3UMbpQSouUzifRj1gVN-Y3PUTY9cHXUV3lybiyHxfyHI5wuyECIMY5dqDJioRWTpnaGJgVR9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eab4140fd.mp4?token=P_nVDjiMyFh72ychm7aHgpN_0UEmH-Erbk1JpVyFLmQ0pCqrCpl4YmNjKsg-7dh9A0iJPOX1TCke9zygxFos5RkIVn-yFZcdNn0eBKRgBCfLAzqiEIPi9N7NYiDmc1FrKX880BljxA3qp6hb8-mVn7fdh09tywvDG_UbD-HbPgT997tV_inBNCtAdsfdcWqBano1twBqM65oD6FBKurbH-fMW4zzH3gspgqjfRYuxwXOsZhPo_3CvMzJFrEAghZJu6RQbje7lVBg3UMbpQSouUzifRj1gVN-Y3PUTY9cHXUV3lybiyHxfyHI5wuyECIMY5dqDJioRWTpnaGJgVR9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آماده شدن استادیوم محل برگزاری دیدار حساس و دیدنی مکزیک و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98320" target="_blank">📅 18:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98319">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2674c1bb.mp4?token=CNw7eoPo4qRxQAouWR0a-Om6tJ5LphkkrQooguYFGMyp0eORHZAnBBG8wJy_c1CZwx9-AFZCpI_VVdkShpNkLUKdNVSiTQLjoUZxHDGCyMvtSUR0q1WH7tTjy_4vF1OJ-Gf0xFTe5NKJ1qnwRzLUyWHpBSFEe7i36tSjEUqssqxLKNqGXP5oKqriMDXspfQc3aa_ZrczSmj6x0D5_ngfqwgfqAxt9-qCL3yu1_v1656pZkcf5PZkWuYdx8LYq0BMaaFgKa8kFoXlLORAVXo3kgsiP8FwG1Yo7EhngAx1ZHOmLBsIwrbllwq9e7bS-2geosdDOUzGy9FZ7cinR6pymjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2674c1bb.mp4?token=CNw7eoPo4qRxQAouWR0a-Om6tJ5LphkkrQooguYFGMyp0eORHZAnBBG8wJy_c1CZwx9-AFZCpI_VVdkShpNkLUKdNVSiTQLjoUZxHDGCyMvtSUR0q1WH7tTjy_4vF1OJ-Gf0xFTe5NKJ1qnwRzLUyWHpBSFEe7i36tSjEUqssqxLKNqGXP5oKqriMDXspfQc3aa_ZrczSmj6x0D5_ngfqwgfqAxt9-qCL3yu1_v1656pZkcf5PZkWuYdx8LYq0BMaaFgKa8kFoXlLORAVXo3kgsiP8FwG1Yo7EhngAx1ZHOmLBsIwrbllwq9e7bS-2geosdDOUzGy9FZ7cinR6pymjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
🇧🇷
هوادار برزیلی و آرژانتینی کف مکزیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/98319" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98318">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
بازی چرک و کثیف فوق‌العاده زشت پاراگوئه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98318" target="_blank">📅 17:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98317">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
👤
⚪️
#اختصاصی_فوتبال‌180؛ در صورت حضور مهدی تاتار در باشگاه پرسپولیس، جواد نکونام به احتمال بسیار زیاد جانشین وی در باشگاه گل‌گهر برای فصل‌بعد خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98317" target="_blank">📅 17:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98316">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD2smHWO8AKjH2V4M7NKFOquvojr6_lV1H-V-zvEX0u58GpNRmbGHMz3JRtEVpOoQRnIR928z2Wy_ZUAp3uGaRJ5vn7ZjuaH9qRuKmMob18ALjvJRoc4l1kEBIZAeJWzf8j_k1pgOsFeRaXupBMaOZRpvgx61f0wtuniNU7Je1RXURKMpEdMPgOkoT-4_V-40yC6C2VXQWhs1RUZmSJUNgw1-ILVXlwczaU_w2wUbd3Z5QgMFvy7mU6YoPOJlEy8XmH9QssfscVt8m6YQVsxZDrBNmGRtS9Zf0vMSRzoYq1IXMtCK2ywLxoYqNJ00FqPax9IlTJuCGVCRpGyK1y0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
💥
گلر کیپ‌ورد و یکی از هواداراش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98316" target="_blank">📅 17:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcqEzPzJTxW3MCkvJVgb3LELmLm0nWXHmeu4u0CNgb5RPXZ5yZF7ZKzC1OLyBuzAmWtGJVPguLG2J2WOX8pkw4TyLSdIHnqhxClyMMWGLc9_0zlgFypZXhPOhVCTGzmvHv98CoYZpbZAcXYpiQ4EcO-qNjS4MVZDa-jxizaomoqepJXEd2d8TUqGFWMf5AdClBeELX9KqstRLOrBqJSGr9F3V0VgfCtDMVxXJlyK6pJpvqh8mTyS89rbTbAtog391ahUvDEOGsqSNcJ6y4Pv66KmQhQ_kg0oJLI-jOv6CyQQ1Jyvf13aoq0SAavY9XQDg1Mqye-c6zDo3s6tnRr5Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
دختر اینفانتینو رئیس فیفا دیشب حین بازی مراکش و کانادا با کیت مراکش رویت شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98315" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f320acc5d.mp4?token=KMO-BS8AU38sHv39yxtPla1RqYQrtiPhbb7lrXyeFh8-PfMoVYSBms2lqsKmLp_N8utp372D2bJ21TQ5uATMG9UqNEUCzAAG4mSFhZm7RQyb0d3yIyddGoE9aaaUV96XggIyD5Zgnlo5G9gKkI63YAMmk4DCN1tppsd2ph3_NLvuNzZF36F1NhaZVJfd7_o30Tf2AsZPdUFKrQJ7gL3jxMV653L_B3ymmuFFNRgKc9gCOthxCKxtUhBMXYhpxHtpfrhWw8wKwk6-ud95ZYOV9ZNGJQsvov8cHLmXT-8OKhL5nIRgcHwu91ipmR6tEpf7s-QPmqPwHBjA0PWPe_NnWx72ay3RO98nqGZN2Cyqxr8s0liUSrLiv9e-GLExuSFCox51uREmIB3nblDHLZE5FL5idV5KBGVIZprCaYC_uaBpuetY5yBTPKBmOYQUsN1tRWJwlrdZ8kmke6xo-hMcZIhsGf5fHMdmjP_o9QnwtOQM7VkqkGxRo_7wLv5djledsLZygx4txj8CUrRtB9yHHDzQh8Y1kX5WSNABWkvZ5uOihldiNKMepL9VkVATQRdEWMLFHtRQD_7VHnerp5u_cf9_1uPPNTbFGg143BJuUDRJgtUMKukk5A5pNXcCG_FaQBiENBhFGjPWpzJ22mJha0c0dMk4Yx3gXbWI1H57vbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f320acc5d.mp4?token=KMO-BS8AU38sHv39yxtPla1RqYQrtiPhbb7lrXyeFh8-PfMoVYSBms2lqsKmLp_N8utp372D2bJ21TQ5uATMG9UqNEUCzAAG4mSFhZm7RQyb0d3yIyddGoE9aaaUV96XggIyD5Zgnlo5G9gKkI63YAMmk4DCN1tppsd2ph3_NLvuNzZF36F1NhaZVJfd7_o30Tf2AsZPdUFKrQJ7gL3jxMV653L_B3ymmuFFNRgKc9gCOthxCKxtUhBMXYhpxHtpfrhWw8wKwk6-ud95ZYOV9ZNGJQsvov8cHLmXT-8OKhL5nIRgcHwu91ipmR6tEpf7s-QPmqPwHBjA0PWPe_NnWx72ay3RO98nqGZN2Cyqxr8s0liUSrLiv9e-GLExuSFCox51uREmIB3nblDHLZE5FL5idV5KBGVIZprCaYC_uaBpuetY5yBTPKBmOYQUsN1tRWJwlrdZ8kmke6xo-hMcZIhsGf5fHMdmjP_o9QnwtOQM7VkqkGxRo_7wLv5djledsLZygx4txj8CUrRtB9yHHDzQh8Y1kX5WSNABWkvZ5uOihldiNKMepL9VkVATQRdEWMLFHtRQD_7VHnerp5u_cf9_1uPPNTbFGg143BJuUDRJgtUMKukk5A5pNXcCG_FaQBiENBhFGjPWpzJ22mJha0c0dMk4Yx3gXbWI1H57vbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇻
بازیکنان کیپ ورد در بازگشت به کشورشان مانند قهرمانان مورد استقبال قرار گرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98314" target="_blank">📅 17:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9605fe2f1d.mp4?token=H7nXAoXOzyKzbFVTmZYWqhdia_v5NmSe6N4KZ4vmZVn95mdygUD1hMe61vvscVjwAi1RfqebE5PMlCwH4n0y7FcU3mnEZnquer1a6H4aG3xBkdaFEFDGFaRxizWrUAOmjhLgCVzMdW1BnW32mPpbyEBvwfumMPXK8dhpUKtgOnHjWvwoDZF_nk5LZQR24gwsow8FahpEsCtgdhC60L0JCxRQipOM_fXrLkihyuvuJ-vd032fzI9rQEGpkqBZZntvkKb8VG8OkYjZjP-fGeOrci-qNnBqSVU8taBDYxZjIi81TlTE5j2PciMkMsIR7XqALxj42J6Qck7eFmSiUWKZcgRNev1gq4CAiScj67kpn3sbjN8FNfOVS57R7KAFfIZU0DLVCvrXd48TtXsLzQpVeOUAZ48AMuyjGyoZfIIw7VkDfE0sbI0nhnDqpVaBn-x1GCvfMXak_nlTcbTfmLhn3NKUEr0cbCX2A3eIENmuPZ1pTIiG46vXWGzh7F4i5r-cjxXdHli2mxRUuE3ewJjlXG4J1Wre2NpYU7pARY3_7fsa-uGFSVORZIvwuVo3QYv7Ew2Svyi6cY8rgDTzXhncXgQeqMf1zBWSaahkvBVhm5g7m9epk7Jq3muZ3oSWEduM227NDmAe1OUYDEW0xFMbwEV46RlegM3608ah6uW8VCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9605fe2f1d.mp4?token=H7nXAoXOzyKzbFVTmZYWqhdia_v5NmSe6N4KZ4vmZVn95mdygUD1hMe61vvscVjwAi1RfqebE5PMlCwH4n0y7FcU3mnEZnquer1a6H4aG3xBkdaFEFDGFaRxizWrUAOmjhLgCVzMdW1BnW32mPpbyEBvwfumMPXK8dhpUKtgOnHjWvwoDZF_nk5LZQR24gwsow8FahpEsCtgdhC60L0JCxRQipOM_fXrLkihyuvuJ-vd032fzI9rQEGpkqBZZntvkKb8VG8OkYjZjP-fGeOrci-qNnBqSVU8taBDYxZjIi81TlTE5j2PciMkMsIR7XqALxj42J6Qck7eFmSiUWKZcgRNev1gq4CAiScj67kpn3sbjN8FNfOVS57R7KAFfIZU0DLVCvrXd48TtXsLzQpVeOUAZ48AMuyjGyoZfIIw7VkDfE0sbI0nhnDqpVaBn-x1GCvfMXak_nlTcbTfmLhn3NKUEr0cbCX2A3eIENmuPZ1pTIiG46vXWGzh7F4i5r-cjxXdHli2mxRUuE3ewJjlXG4J1Wre2NpYU7pARY3_7fsa-uGFSVORZIvwuVo3QYv7Ew2Svyi6cY8rgDTzXhncXgQeqMf1zBWSaahkvBVhm5g7m9epk7Jq3muZ3oSWEduM227NDmAe1OUYDEW0xFMbwEV46RlegM3608ah6uW8VCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
هواداران مراکش پس از بازی با کانادا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98313" target="_blank">📅 17:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqN-NiPDiz5v4olc0DtaoSr5cLjkMgQl4yacAVAj47EZltHOmOnxku3nq_C596-JzYVCuTOz8iQXVU67ydAI9mXJsDNXfDfLradCdZJ91iYxmu3-537N4t2AuWY13Xzxr9_fRalXvl5-pG9pXQoZzhQlUztsXqqSEGK65hCWo8-iiwjLyrxf4Laqqv_tcK6jDLfgH99ME7g6Wg2XPSxi_EW21wIYn_hwxeFTs5D5lnBlu3fO6mRo-s-bRv2VnN00GFU83UmikELjnzGnLORl-ZfGTaQUdm8fWvOXM4ipW0ZEAqQ9uFec3JJzIU8pZvWB160IfSn6WZRmkFSh0xr6HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
💥
دشان، اولین مربی در تاریخ جام جهانی شد که 10 بازی حذفی را برده است:
— در سال 2014:
✅
مقابل نیجریه (مرحله یک‌هشتم نهایی)
— در سال 2018:
✅
مقابل آرژانتین (مرحله یک‌هشتم نهایی)
✅
مقابل اروگوئه (مرحله یک‌چهارم نهایی)
✅
مقابل بلژیک (مرحله نیمه‌نهایی)
✅
مقابل کرواسی (فینال)
— در سال 2022:
✅
مقابل لهستان (مرحله یک‌هشتم نهایی)
✅
مقابل انگلیس (مرحله یک‌چهارم نهایی)
✅
مقابل مراکش (مرحله نیمه‌نهایی)
— در سال 2026:
✅
مقابل سوئد (مرحله یک‌شانزدهم‌نهایی)
✅
مقابل پاراگوئه (مرحله یک‌هشتم نهایی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98312" target="_blank">📅 16:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔥
🔥
🔥
▶️
🏆
برزیل
🇧🇷
🆚
🇳🇴
نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98311" target="_blank">📅 16:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6IpgpBlEmUda0DhgZiKFGzH4_CEBqrW2q9sYNuCm_mHpGg183cIaSbgv1y8iZYAgfJCEewnroVhtPbVTqKkk9mVFyVALzSJkKfZkf9JOFYFbSf6ODCwsufa3-SDUCOXDuLW91PxaIkwqAS1HhQVUiAJd03Y-1lczg8d7INb9V-pAvnHDxbNTRLI03UFd-4N6rCIzVmTjtK4jxPrDE7RVwdFFtVc8E3PlWZaSYSkxF8QQsenXh86X1OCSGLdOFiGavkq1zN8AllmLIiVNp1Qivr3lelgiSPMJPJjzWEdc0DkI6GD_70ATwJRcTAYXoViGBX-EpGua2TkY_Uh4cCb1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
📱
بیشترین فالوور از بین دروازه‌بان فوتبال؛ گلر استثنایی کیپ‌ورد صدرنشین شد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98310" target="_blank">📅 16:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98309">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyh8UmyoFTiOMZDcMEpE3TXxLfgrkSlH3r-lpXrVBSutja2A28Bga-xwY_AxKsXCyXDJ4qsO99r12ER4TkSpEE_uUmTH6bPDTLT5_Q_97VewGM1ooRkoP_zC6XnYJpgRyRQLeLkZiL5X1pVl3-RB9pQBHKOgki7eQR93d-HnFim5fPSPGz61waBwQfb4500MfRyCQaLpFPyDWH5pkfjR9oHhDEa728pE4VPe217Np0-3WpHTOn6gAn1CJNYqTO-aPqdgQRlGjtvzQQaZqsbHX6BQZpAQ4qUPZg44GuoC_FvgMYAk3s10i4zFQ1yWn-FlUmeTCuVf7NH6mJLtW32mDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🏆
صفحه رسمی مجله فرانس فوتبال
:
امکان برنده شدن جایزه توپ طلایی بدون بازی در یک باشگاه اروپایی وجود دارد.
👀
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98309" target="_blank">📅 16:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98308">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
انتقادات شدید مجتبی پوربخش از رویکرد عجیب صداوسیما پس از حذف ایران از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98308" target="_blank">📅 16:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98307">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuA_4gqxMSs-pzxNn584Kryil4aNBRlnPpMDczuxmXVyfsNNP3YF0SuGZxNGZEehvNk7UhqDnQyEzDgUTbk9eSws-l1rRDLpsmOMNBK9GpTP0e77Q3SiqshfxY8lJdp84EZnoK0hoZTVDyToo_L0UYVh85Wz1SXJnlpAVom-jnp-wgy4v1nIDU8k1fgzaC13MURm1_WAg1DL5Sh_ut4iI-C20CBTQ34YO9g-BNtDKTZAWvUJjU0YHu0EQmxNwQh7sMpSlVQKoM2TJqBIvMERYr5QiadJbKnfrkl5CzaDolCf9UorzRt7NmBAAEWXQFLcizBUCMoPc7LK8QX2iMjXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98307" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98306">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98306" target="_blank">📅 15:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98305">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98305" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98304">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaXN0KR8xhTxhz2GTBQYQKGIFYKFouASZiydjQFQ1EK723h2kPY_3GRoqH-7N-QG5DuNEwgVwlxnqo2FxdroBWOxDNLOi_bjezE8enB4yxmoRHoUXJg09a28jYvwZRMqZBRddCReuOctCloC-1y8iT7sDT3R25THmFfqVbW_o_wOOUalVree-jAScaRMzAmBF085wXBwARaMxt2jitc9c7Tz4ACQU4o-zcA4aMmPOV9v24qEAQCOJKTkjp_4XbrSmyZMzxNhYfdLTxHGTQk8wTX3WG9U3kHtK6JPd6Xl2vnHEg0YkoTRUlBOtYG4mvMiNFO2-9mRcESmarx-DLU3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
یکی از دستیاران مهدی‌تارتار در گفت‌وگویی کوتاه با رسانه فوتبال180 اعلام کرد که مذاکرات پرسپولیس با این سرمربی درحال انجام است و پس از توافق نهایی با گل‌گهر و در صورت رخ ندادن اتفاقات عجیب از سوی بانک شهر، این سرمربی به آرزوی دیرینه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98304" target="_blank">📅 15:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98303">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8c9137cf.mp4?token=aJJrWX9vOXcvDmXoB2YVJXYC3iIuKb0pgPZg_JLnAqjrTefYhNEBPOpVXEPlAHsS0CemAf6zLlTdk_CHR4vgTVYQ9W0MT4VKB7S4J8K8JKdA1w3yOVbqcp-UCZvTXX_UDAb16mhICSG098nSfYo32gFQ2h7L9ULx5hzSFjj0vUjzDXAllNui2J9wKO-RIBT_10KcT-3IfvR9F1HeDaNVgVDykIj_yTOg3ppE-qkr31hOuqmbEgktE8nn2NOj-9W59ph_m92KsCWLmlA5gIMbD5kINl3oJ9iW3uwrfCh8rzbV_oWP88eYWsOx-23XfR5UeQvCTBGBRwzWmutVMTDBPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8c9137cf.mp4?token=aJJrWX9vOXcvDmXoB2YVJXYC3iIuKb0pgPZg_JLnAqjrTefYhNEBPOpVXEPlAHsS0CemAf6zLlTdk_CHR4vgTVYQ9W0MT4VKB7S4J8K8JKdA1w3yOVbqcp-UCZvTXX_UDAb16mhICSG098nSfYo32gFQ2h7L9ULx5hzSFjj0vUjzDXAllNui2J9wKO-RIBT_10KcT-3IfvR9F1HeDaNVgVDykIj_yTOg3ppE-qkr31hOuqmbEgktE8nn2NOj-9W59ph_m92KsCWLmlA5gIMbD5kINl3oJ9iW3uwrfCh8rzbV_oWP88eYWsOx-23XfR5UeQvCTBGBRwzWmutVMTDBPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
هرچی از این سیو بگم کم گفتم. گلر تو ۴۰ سالگی اینجوری جلو مسی غافلگیر نشد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98303" target="_blank">📅 15:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98302">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek4y4_dUdF0nXxBKmDg6YkDXROBBs3OnlLOL-4LeUYqoMKiwn2m4DzctPj3KgMdYcrEZTaJ1g8WDM-DqlZIGbLa1lwUMNJmCZM5XpfMudLfyMq-VVn9MMNQVWIX8yh4nCQ4nWylgUcyBRNn6tE8wqFYydLTtdhl6Jkqn8C-itHNmUxarS1B2JcIxwkIwUaqEHZWdWXD2RgkQbMon11Y4pY9qxmBBBsugqK172jFssRoXn6q-zHkGEHkrFsQSngzMEm6U7t5XN2YLBZWdQfPnN8JxDXRUtd6Haep-53W3-uR9hbeuqNBL_4xrb9EBCCczeQim8SKDYy-1RYAZAPJotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورلاندو خیل 3 سال پیش تو دسته 2 پاراگوئه بازی میکرد و با درامد فوتبال از پس هزینه های خانوادش بر نمیوند
حالا بعد 3 سال اون دروازه بان اصلی پاراگوئه شد و مقابل فرانسه و ستاره هاش فقط از روی نقطه پنالتی دروازه‌اش باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98302" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98301">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98301" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98300">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98300" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98299">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743a223544.mp4?token=Jy6oeDml0ZLuMFKBtT-XxdjtCzlbRObgSVIblaZCbtkrPthJZH8aA2d51lQ55Z6A7n3ybB3quQvq6KC85aj8TXpJNkpYzlvPjfK5YJhbqNt-wvBxOJpQNm7crlF-KDULzf8MF_XcLBQ-Cry9095uieU_8bsl5DAbq9qZ1m7vJ-DsyJySS8BMHMsjFD96KlXxGA9ZBSWr16IjOUhp3twyJk3sN_rOuBbxz4fs55sEIIvgcD9Eb0-noQ6wSWrfAwnRkBPNjQt0qdKrXiVN7GPoT425AySV6_qcMi0GEERXE7kI2gRm2lXGaaniDtz5qtlv6eP6394mAuofcwOY1qC4PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743a223544.mp4?token=Jy6oeDml0ZLuMFKBtT-XxdjtCzlbRObgSVIblaZCbtkrPthJZH8aA2d51lQ55Z6A7n3ybB3quQvq6KC85aj8TXpJNkpYzlvPjfK5YJhbqNt-wvBxOJpQNm7crlF-KDULzf8MF_XcLBQ-Cry9095uieU_8bsl5DAbq9qZ1m7vJ-DsyJySS8BMHMsjFD96KlXxGA9ZBSWr16IjOUhp3twyJk3sN_rOuBbxz4fs55sEIIvgcD9Eb0-noQ6wSWrfAwnRkBPNjQt0qdKrXiVN7GPoT425AySV6_qcMi0GEERXE7kI2gRm2lXGaaniDtz5qtlv6eP6394mAuofcwOY1qC4PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تشویق کیپ‌وردی‌ها توسط هواداران آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98299" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98298">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d4df0d8d.mp4?token=dJ-wUf9a_Sw06UvxyZoRZBH9TNqcXwjsz3yRVgVGjL6M9MrLVmoSZQNaUzFmUNkb1xv0iRLHrvoCezLZK8P4za1QCPWxZXgdQcFcXar6FOXLSArH-frrEeOwxyhl6-_e5VyVtDXVLA_M14D-k7Cyozfui6rH08Ln7Bu3G9M_n31OmdA-oWUZypB9OAUaUILD0TrK0ilS5HD6Geq7IM32ghWvrjMzZAVA7gdg6GnsBs6Zg_nUDisDZZHamCqBdCRPOVpLubuFbLpweVBkCLUZ_Gpoed4EfG9gRWm3YykX811G-6KOxEnAZo9e0euxQOBewm-0Mr9X98j2okZV88CQ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d4df0d8d.mp4?token=dJ-wUf9a_Sw06UvxyZoRZBH9TNqcXwjsz3yRVgVGjL6M9MrLVmoSZQNaUzFmUNkb1xv0iRLHrvoCezLZK8P4za1QCPWxZXgdQcFcXar6FOXLSArH-frrEeOwxyhl6-_e5VyVtDXVLA_M14D-k7Cyozfui6rH08Ln7Bu3G9M_n31OmdA-oWUZypB9OAUaUILD0TrK0ilS5HD6Geq7IM32ghWvrjMzZAVA7gdg6GnsBs6Zg_nUDisDZZHamCqBdCRPOVpLubuFbLpweVBkCLUZ_Gpoed4EfG9gRWm3YykX811G-6KOxEnAZo9e0euxQOBewm-0Mr9X98j2okZV88CQ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
خسرو حیدری: یه بار تو تمرین تیم‌ملی سر توپ زدم کی‌روش نزدیک بود کونم بذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98298" target="_blank">📅 14:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98297">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH_iMm_2je2gvNdcxuAMJFMq03UNbRuzNHYmxdQxN3xtXPOUjtM1XjGEUMmh6JYLwOMIA6YWdopN_l4R4ATp3wHu21VIw6ZnIqFVWkPWRgCLFNCEI4BkL1MXmzZT0YOMjTtxKf-ZKLSbEHzfOSVBMyRUwz-jUogXsTGeKmKHsWfWtdYQFlX4QPZJSFIaQoOSjWGOy8RFM04QSsDmqE-3QgQrcnOQvEKZ6dUjrpQqkH4JtgZZx1JOpvHjrvuGB5ikMoALBQGvXR4C44zHnhbzJrw7K7pgOI94CAN5WShU7YvvusOHjo3aDYpAhsWEYdrYFMXRGwjUFHNL925d5FuLJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
محمود خردبین اسطوره پرسپولیس و دخترش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98297" target="_blank">📅 14:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98296">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj67DE_06XHTjDitDTe_2iaEQDxnJKfCXn3RXAF7Citg-r-czqoiWeb3lEYUH_0ZhIDkQwMB-EeBqDuBf9MIPPhjSukQDiVNSeoo7tkm0yEx-HZakoFdnJ5IPll-RXgzPetjJ7HhzFqJrkd0aqRPl5ScYQrrw4g-WzyLpq6yjEi1LX76I8oZ2EkeIsySSWPqmcI15DZsQ0tMR4OvQ0JbBD8G1cbxkfhSh7XnslrGSPGsJCSHPubyXPPzOIdpwXMVioCvWh-KprbItMKmFuTgjs2hVDVUR94o20A86wAVfIToMDXjUlm-yUofCtTj9KlKw1OUuLYlDHO5LvEd302sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
پیشرفت چشمگیر مراکش طی ۱۶ سال اخیر...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98296" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98295">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYEMmqfSHvCfEqSXkEuCpf04m-ZiM11aywuh1QYNskCOxw848X3qRzUiM2b_5SVG6vFIiiLjKF4i7UpVEX30AsD9Ccqr2My_7jQMfYsybOI5JVk92ReKmUm_tD4dSUbJc3U0im_5rlsICb0W1FOZiwhfpjb_4owSBck0It2jrm0ZI_raKzLo99yTXXiSsS7vaIugUflRcYAe-F_Ay8Z1NJ_w4-ju42ik0Ahm4K9m9S-tCDta0EBb8sYvfPpcxsozBGv-g-Nnd5g_TcahzpGshN2c-yuwnZG0bSooRdBYCS5KDKe2n29MCcFxon1vd7sL5P1boZKHqvfKYz-8DaqXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گریه‌های علیرضا دبیر در مراسم علی خامنه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98295" target="_blank">📅 14:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98294">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqWP_FYf3MAJVSzpaTwskltNVFU0PytGzXGDrnq6XzXTr2icrLn6cc-2enUDWJndpEc_8pL7S6_4SiZkIobLoFGQ54fJHhvThe3k7YtbH4tuMOCwblhsMcUuQzLdqAnmBRRB5On9QGibB5eJ9CNdTJ-SyO6S1ufukH6b1GTbVme-VK8QHOxwP0WZ6d0340xvmqeuNG_lns2SbW7Q_XSR09RSnDh9gkZLxwwBRoE0nTqsQPsnDvAbvVpkH46tLY_FKaR19oGXO8i9416mN40p1jf2OC-HYswu0JVw2VR9qVv0IOsPwDiratOQuQHEpKB3joLzBAt-kL1FG39t8MuJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#رسمیییییی
؛ دومفریس مدافع تیم‌ملی هلند با عقد قراردادی به رئال‌مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98294" target="_blank">📅 13:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98293">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde65c4bdf.mp4?token=DvY_1OV_ulaSPfjkSzuBQn2cc42CHGyIIuzXyW5uihFl4llunMBmtxGeMiODA-fVW2Uumre7TIE_QYohfKPXbYERx1FwCc274dhQI3TJPpY-WybOYSXvZPQntvQMtOovuMszrFKdLFEDgKwc3jwZey4ECKYMHy6MqwDMViaBeaISJykTYyQGbs8XHAcMl9h0ERvKqq_9V3buhiggvXoXjHj2qgdRIM8FXLgLVuKWqCTF6w1L4wOsn2I2H1P-LB0DU-ZbPqd9gqgKSI60zzm0Jn0khki5r1cdrDN3WqCdOJGO_S0aizkdbPsQ21a2lram1L_OGHGNrjX0uGKwYosTeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde65c4bdf.mp4?token=DvY_1OV_ulaSPfjkSzuBQn2cc42CHGyIIuzXyW5uihFl4llunMBmtxGeMiODA-fVW2Uumre7TIE_QYohfKPXbYERx1FwCc274dhQI3TJPpY-WybOYSXvZPQntvQMtOovuMszrFKdLFEDgKwc3jwZey4ECKYMHy6MqwDMViaBeaISJykTYyQGbs8XHAcMl9h0ERvKqq_9V3buhiggvXoXjHj2qgdRIM8FXLgLVuKWqCTF6w1L4wOsn2I2H1P-LB0DU-ZbPqd9gqgKSI60zzm0Jn0khki5r1cdrDN3WqCdOJGO_S0aizkdbPsQ21a2lram1L_OGHGNrjX0uGKwYosTeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماجرای درگیری معروف علی فتح‌الله‌زاده و مجتبی جباری را یکبار از زبان خود فتح‌الله‌زاده بشنویم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98293" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98292">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP5MOl29kAnpu1nvU9Lgqa7iXwDMgEawYVEXuTSJ2IL46-gT41rSTIJFE9mNMgf7o_4J5iNQvKuwu0k4fpQsIVgnZx14ONaXXnw45O5eBVXYeey73106AkMTN30HI3jj90jVpFCyj0BpShKjtt1xNblecCnjJpbRhQg60Gp5fwiGleCbpGIiDUuXTq7YitjwiQX8FPiIBx8DalBBOH9oB8RlM2WC9twXNQyp_c5cmsxA9mcy_FxJoeOfRkcYJ1qhmmcOR3HnFviONseN0_7Hib-_g7r6m2aLeBs2AziJMUGRLjaJ8oBkFLkxBUNdFp0ItMnOFemrRMNUT2n11MeWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
کلوپ به عنوان سرمربی جدید تیم ملی آلمان انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98292" target="_blank">📅 13:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98291">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63e17f963.mp4?token=U4B7T-9-RaQDrwVtLCd4fzHsh5TS48mARH31SXRB6kRpGcEGpKSyIpW8Me5dz7qAGoyCEsVXgfhhx9Z-IFkJ2vKHNi5zv1GuZi0k60AOx0686_G0Pch7M6vM2KRyeFHYB_gBWxsSTEdHhShtnPypekT1tlUQYtpOGqWiNW7jDlOSRHqshj5AZgPvkblbjHnx-iENapl80fjaCGgGPZ55URaCfqzEF-0LrsZT1iLUCsK8FweziaXYAneSBArUFeIMe68PCJ3frZEWMt9hiWLEIa7jKF_nJvUAlhScigOMjpeGFGtl_taivoO5sVN_1Xdq9MbSTkgjotsaRxbAox8RHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63e17f963.mp4?token=U4B7T-9-RaQDrwVtLCd4fzHsh5TS48mARH31SXRB6kRpGcEGpKSyIpW8Me5dz7qAGoyCEsVXgfhhx9Z-IFkJ2vKHNi5zv1GuZi0k60AOx0686_G0Pch7M6vM2KRyeFHYB_gBWxsSTEdHhShtnPypekT1tlUQYtpOGqWiNW7jDlOSRHqshj5AZgPvkblbjHnx-iENapl80fjaCGgGPZ55URaCfqzEF-0LrsZT1iLUCsK8FweziaXYAneSBArUFeIMe68PCJ3frZEWMt9hiWLEIa7jKF_nJvUAlhScigOMjpeGFGtl_taivoO5sVN_1Xdq9MbSTkgjotsaRxbAox8RHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم از حماسه تاریخی محمد مایلی‌کهن در گفتگو با عادل فردوسی‌پور
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98291" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98290">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4ade1cc7.mp4?token=jteLqQgyGPiXw5U7_8vfakquLMZYIx86CKAhv5YcIQMe4FgukMhMMwn1ErP9pnUvK_tpJDzEBb4zXrCcr2MsZulfwpjR-MMNeGqVBnERy0ZDE2WmEIGTxFFcu8c_PCSwA9yqwImGeixWTGRmEYJkCtForSeaQLG-dAtpvGO3yYYYp1M4aEzeEjTcigGeulKzVBf_CxOdUj3ozWQpMlOnpmB4J1vJ1GZaf7EpKg9sosrJVQEpyZczk-oYDGaUHn4h3rszOGDiuezLYYVE8ul5W8ECVqJ6fYbQ-Ir7qaRWHdo_W1RIxMD7u-y9FR0k92IC_DJ9BTdRAIeOuGpdYTNdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4ade1cc7.mp4?token=jteLqQgyGPiXw5U7_8vfakquLMZYIx86CKAhv5YcIQMe4FgukMhMMwn1ErP9pnUvK_tpJDzEBb4zXrCcr2MsZulfwpjR-MMNeGqVBnERy0ZDE2WmEIGTxFFcu8c_PCSwA9yqwImGeixWTGRmEYJkCtForSeaQLG-dAtpvGO3yYYYp1M4aEzeEjTcigGeulKzVBf_CxOdUj3ozWQpMlOnpmB4J1vJ1GZaf7EpKg9sosrJVQEpyZczk-oYDGaUHn4h3rszOGDiuezLYYVE8ul5W8ECVqJ6fYbQ-Ir7qaRWHdo_W1RIxMD7u-y9FR0k92IC_DJ9BTdRAIeOuGpdYTNdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادار کیپ‌ورد: «ووزینیا شوهر آینده‌مه»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98290" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98289">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0306de1296.mp4?token=SFpcA5gy7gFoyc7JUddCtiBIwN5bQq3K3DCsjDUXbZGu3iDa-GEd4qcaGtSoCa_ILepqswClcRO46LhuQ7XEgg7v3kKqKpzSWvNM2-oslomSRq8eNT8AoBJQZWMIE4n5jLkt1PsA7CgNdKdzrHO39C5idMag6xbgI10chUMTXNhS9uoNF3DhxRgNBDdq5O4YYMDiU1bhna18-A6WfmkeTnbCdFFo73bR5qXMFOzNKiJ4dYTvczGeKYfLaKZ6YsF0hYjnZNCNx1r12-mW9GhFOUH12mNNi6Uk01tZngVSITM1i8POuEmL9S0KIuAk7NvyIl6WXfj_5xMbGc3gT_dGug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0306de1296.mp4?token=SFpcA5gy7gFoyc7JUddCtiBIwN5bQq3K3DCsjDUXbZGu3iDa-GEd4qcaGtSoCa_ILepqswClcRO46LhuQ7XEgg7v3kKqKpzSWvNM2-oslomSRq8eNT8AoBJQZWMIE4n5jLkt1PsA7CgNdKdzrHO39C5idMag6xbgI10chUMTXNhS9uoNF3DhxRgNBDdq5O4YYMDiU1bhna18-A6WfmkeTnbCdFFo73bR5qXMFOzNKiJ4dYTvczGeKYfLaKZ6YsF0hYjnZNCNx1r12-mW9GhFOUH12mNNi6Uk01tZngVSITM1i8POuEmL9S0KIuAk7NvyIl6WXfj_5xMbGc3gT_dGug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇨🇻
نام ووزینیا تا ابد در تاریخ جام جهانی خواهد درخشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98289" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98288">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شادی فوق‌العاده سمی هوادار کلمبیا بعد بازی با غنا
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98288" target="_blank">📅 12:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98287">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98287" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98286">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cI8ni6GQ3Qm1j2oVa8vrdR0JpFhtVg4yv2PM3Q4WH5zTYfzrVmdPvSjbwSi5e5o0JgFeor2W1rdDbLJ7rTV91onSMkFfoNscklBC6pQI3PNz3-uESdiWrPUSNgZqC0EW7NrbAlF57_BDeSIelMuGaC4zqJe1aL-4RY3nSdJsjQD6RHKXh1GLHTrNhKuqioraq2jPgYeCkS1NnGdmsZprx0weYvVzJ_RA3_yHQtLu5GltUmksKbIOCPA1057YRt29-5zYi_t7HMGdAtWOWQktojAzUJwTrF5Vo0_gsYbc1K57_8M97Ik1auV9GpIXyTNGf5XcnLC5c4dl5Zb1BXQKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇵🇹
🇪🇸
گاوی‌قبل از بازی با پرتغال:
برخلاف اخبار و شایعات، بنظرم بازیکنان پرتغال با احترام فراوانی با کریس‌رونالدو برخورد می‌کنند. اینکه می‌گویند رونالدو در رختکن محبوبیت ندارد اصلا درست نیست. همواره واقعیت‌های یک‌تیم در رسانه‌ها بازتاب داده نمی‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98286" target="_blank">📅 11:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98285">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=AVo7HaQzSv6Xgc-twizTpu2MwxnL2PvxhPwq6ISYmXB0K-yXRmi2hlZMGlaLiBv1jA3owNucY-6Q_9uX7sJVl_yq2EPv5iyP3DMxfJ-z7tKxSkbniPMo6m6Ug9yZrlG-UZvGCvZAohS4rXtC9dbeF0Fj5ZZr2lhyyavNERngME7jRK3fzdIFI67GwPcunehj6UfPRzxnCjfVxW3Re2dSn56iDxMkaRuimMUqGS4RKPvb3c2g0NYwEL-D6hQ8KuTbd08PPAehJs2EUBXJ7spzTB8NNvIWSmHo2LUbgNFBybMKkEKMLFeBpn84QJDyHJIP8I1Or09nugM9pymW1gh6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=AVo7HaQzSv6Xgc-twizTpu2MwxnL2PvxhPwq6ISYmXB0K-yXRmi2hlZMGlaLiBv1jA3owNucY-6Q_9uX7sJVl_yq2EPv5iyP3DMxfJ-z7tKxSkbniPMo6m6Ug9yZrlG-UZvGCvZAohS4rXtC9dbeF0Fj5ZZr2lhyyavNERngME7jRK3fzdIFI67GwPcunehj6UfPRzxnCjfVxW3Re2dSn56iDxMkaRuimMUqGS4RKPvb3c2g0NYwEL-D6hQ8KuTbd08PPAehJs2EUBXJ7spzTB8NNvIWSmHo2LUbgNFBybMKkEKMLFeBpn84QJDyHJIP8I1Or09nugM9pymW1gh6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇬🇭
جادوگر غنایی در بازی با کلمبیا!
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/98285" target="_blank">📅 11:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98284">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GffH_tjK31GGdCRUXpjb9g76eGU0VmzSsUprV2ENK0jkhDVBNwjVWcSm94RsjDFETRmoE_dSwn-8vqViUQ29fRqoxb5Wfot6Xh6jFfX_JLV8zcLBbnB7AAxJ0FqJslLWOhdmzWoa2QQbvMn8skP_u3osWErE_BGt4NoXk2eeZdNv1z1KuhjJUfHjlSTz7OHbbMBxk3ZmDCv0Z2p1eMqKh9li0F0SM1cCHLtIAddVHVMogiysDgx78FmX-vA7ZRsqi8vQ8cMkemwo7KfSQB6tSdoPWL_N4IzLpTRpuIMET08hw-PQDgI569oT9Q_dQXuklYPbdms5vad-3K3QZJHSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇫🇷
دیدیه‌دشان
:
من خیلی حال میکنم وقتی مردم به امباپه میگن دیکتاتور. دیکتاتور همیشه کلمه منفی نیست و وقتی راجب امباپه اینجوری صحبت میشه، ذوق میکنم و بهش افتخار میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98284" target="_blank">📅 11:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98283">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=QpqbcB_wlj7nNHxXVv-xTN3E0WgT4ymOQ88FjLHxdhvkBLqEhfO36Fo_JBtBqOr-9ueUQiqgUPJUOLnqHX_arCqXeLAZngnreKnM7RgwRKc06E4kRihTnCo9iIBT2BAy4z9PTwjPK7Uy7SwI1pWruAdb9wRyABit1LA9y4X36w5M97USt9_BN2J0cEFOKZWQ0_Pka5Qgmp1PD8IgbSDHKZci6tFiulmPVyagqd7IHPSLAiHJXwhJ5uaHI2kiTI8P8OwyFGPrHGmCYphg48WZj9uaAnPtpZ9qLzuCjyJA-tHMT5rjOJVQOXJrlTf5XJdUS8RctAxpHZo5oTMkDbqKyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=QpqbcB_wlj7nNHxXVv-xTN3E0WgT4ymOQ88FjLHxdhvkBLqEhfO36Fo_JBtBqOr-9ueUQiqgUPJUOLnqHX_arCqXeLAZngnreKnM7RgwRKc06E4kRihTnCo9iIBT2BAy4z9PTwjPK7Uy7SwI1pWruAdb9wRyABit1LA9y4X36w5M97USt9_BN2J0cEFOKZWQ0_Pka5Qgmp1PD8IgbSDHKZci6tFiulmPVyagqd7IHPSLAiHJXwhJ5uaHI2kiTI8P8OwyFGPrHGmCYphg48WZj9uaAnPtpZ9qLzuCjyJA-tHMT5rjOJVQOXJrlTf5XJdUS8RctAxpHZo5oTMkDbqKyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژوزه مورینیو: بعضی از بازیا دقیقه ۱۰ تلویزیون رو خاموش میکنم  و در این مرحله از زندگیم تا ساعت ۳ نصف شب بیدار نمیمونم که بازیای بدرد نخور رو ببینم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98283" target="_blank">📅 11:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98282">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXm-_g46rvEisb2Hi4vFXN5i6ZUR5DvZDDN8hEBiOrZdcl42rmXLyJ7xuGTvAEK3KU--OBQkPhNxnVgrUtqvRMJbMk-7QqWv4ov7TFQ3woEve7oVpeiDpEIyvQZtHxnZ-TinH2613tdFk1B5M3yDT1pv3mzFiR-RZKehUvjFCatblW1B6F6e5r55cR4tBk5Tw525fW8UVWkn9s-fesZHJYIiZb-C3ZGvTwnWyFwo-mV0ZtVBPey2oA34Yg0CkGaFlbBxoTXMUClOq4JfRgnlTSR-y-EWaYJwPheAnksTbsbwiHWmOrw-T2Pxjh2Mki8rxgarct8le6BVTU00Q46Zcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
📊
گلر کیپ‌ورد در جام‌جهانی از حیث دریبل موفق از رونالدو کاپیتان پرتغال پیش است!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98282" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98281">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=t4TDau2IHwMqtQO4Wn3IicB65TQ_vGwee8Y8u-i3mWROD6v4UOXpfsudb61RTgxjVeV1gexRCOZNXvO7_n2KA1kXNnDw2Kgx8aIVathBuZVew20YsoS7paIJ1HfMpxyThqjF4Q4gfzpuzlKNZwSNG1KM5MmGT0Z5yP7M2JrArQDAvIKHjDizRFzo_UWMPQiKXFu430RdpKUCsm96FEpy9RcZYcYCXeAq75rcQnEizw-B2GeKgHhZU6OoAv1XtboJFJMzWQQhrVCuNQX0USnr6T3oj8WLOxfvzQ2ITT-nrDKJ5Pl0T_YZfeubv0-eASBHJsoaZuhopzVxixzP_-pgiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=t4TDau2IHwMqtQO4Wn3IicB65TQ_vGwee8Y8u-i3mWROD6v4UOXpfsudb61RTgxjVeV1gexRCOZNXvO7_n2KA1kXNnDw2Kgx8aIVathBuZVew20YsoS7paIJ1HfMpxyThqjF4Q4gfzpuzlKNZwSNG1KM5MmGT0Z5yP7M2JrArQDAvIKHjDizRFzo_UWMPQiKXFu430RdpKUCsm96FEpy9RcZYcYCXeAq75rcQnEizw-B2GeKgHhZU6OoAv1XtboJFJMzWQQhrVCuNQX0USnr6T3oj8WLOxfvzQ2ITT-nrDKJ5Pl0T_YZfeubv0-eASBHJsoaZuhopzVxixzP_-pgiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
خاطره مهرداد صدیقیان از تماشای بازی لیورپول و چلسی در استادیوم استانبول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98281" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98280">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=cU_P9OJs7bpjmmm3Y52iJ3yac4JWYvXnU9y07byFI_0cQCPjMirUQXyDHlqVZRj6UapgLCOQotNq1TAS9X1hZ0Nkmloy08L3GaiXnVRAWgg3NNS_swFDbvfPQQ85TR5GWqmtVSydZEHO3GaA064d59Wcktjd7sFO-yJM5e3WvzjL20qAEvSu72BUYuyfz9lcIdr_SrzS3Rs7Jybby_PQw-5RyQBUeG7Xi_bjjiry5OxcpUgLm8wsBWyI_dNvlGz4g5Lomvt2tqoXblytlmyDowMPGqwvKt6q1h9Ue0DyS51ih3lWdDfbMMSvL2fTLRH6XFm57jy-4TLPUjz6Dmlq-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=cU_P9OJs7bpjmmm3Y52iJ3yac4JWYvXnU9y07byFI_0cQCPjMirUQXyDHlqVZRj6UapgLCOQotNq1TAS9X1hZ0Nkmloy08L3GaiXnVRAWgg3NNS_swFDbvfPQQ85TR5GWqmtVSydZEHO3GaA064d59Wcktjd7sFO-yJM5e3WvzjL20qAEvSu72BUYuyfz9lcIdr_SrzS3Rs7Jybby_PQw-5RyQBUeG7Xi_bjjiry5OxcpUgLm8wsBWyI_dNvlGz4g5Lomvt2tqoXblytlmyDowMPGqwvKt6q1h9Ue0DyS51ih3lWdDfbMMSvL2fTLRH6XFm57jy-4TLPUjz6Dmlq-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
گارد ملی مکزیک درحال تامین امنیت هتل محل استقرار بازیکنان انگلیس پیش از بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98280" target="_blank">📅 10:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98279">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522d669236.mp4?token=idGI7xtsXpFUQiKbm2qEix0eZGDSZz_muguU4TWL6yzh0vLGzAsqihy1M_MbT26zn41gyI_tEp4xEhSydfI8Mrq60O9ipBuaysTg1vza9_p-jClXuAkxGUKqtHXut2qkfEIzx0bOcU0YF3XmKcjkRxFyAtSvQTUNwJB9eBa_kJlDVYaRiCXSrfbYAhsStTQBmAiZkktH_uM0L19TqmUiS3DYwBvUtuTqZE_oWLtELH6QaqKgfxAKSPlhkq8c8mnpIiUmT7cFZ0Fp-kkMR0qEmmA_KrMdGm45nGJ3bwS-bVaEV06ntoC27WfJtNIEY_zNFigERZyLNNLXbJa6j3ZKE3h--S4aR_xlDRqHZbf0HzGxhR71eF16TncUhiGBx7hhM-LjiZsJQlpDU4HHGAxyDAy_tTOoSeS_2EHl-T-_H4M-x5wrWEkV9Xpb9iVjtHu84IkJGaDjjQnMcjggatEB3-pTJc-TrJ7bhQUY5jz8OEgjtXLiO7Ppql_oZjIzGDVcmPF4_RrCb9fd5ZBN-vf0-F1xx8IGgLJ0ekCvWBTeHEh_c-NWwTnP66un7kydlmlYBNDxcnkKlB6Kf5PNgSlExm946hX25Zw1v8kcbhcKMFwvoLBpiE3uHj8Z9Yml6flDjY23jgmtBR6d21QIABdIa0FYN_K0g55Qe92JblgPpb0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522d669236.mp4?token=idGI7xtsXpFUQiKbm2qEix0eZGDSZz_muguU4TWL6yzh0vLGzAsqihy1M_MbT26zn41gyI_tEp4xEhSydfI8Mrq60O9ipBuaysTg1vza9_p-jClXuAkxGUKqtHXut2qkfEIzx0bOcU0YF3XmKcjkRxFyAtSvQTUNwJB9eBa_kJlDVYaRiCXSrfbYAhsStTQBmAiZkktH_uM0L19TqmUiS3DYwBvUtuTqZE_oWLtELH6QaqKgfxAKSPlhkq8c8mnpIiUmT7cFZ0Fp-kkMR0qEmmA_KrMdGm45nGJ3bwS-bVaEV06ntoC27WfJtNIEY_zNFigERZyLNNLXbJa6j3ZKE3h--S4aR_xlDRqHZbf0HzGxhR71eF16TncUhiGBx7hhM-LjiZsJQlpDU4HHGAxyDAy_tTOoSeS_2EHl-T-_H4M-x5wrWEkV9Xpb9iVjtHu84IkJGaDjjQnMcjggatEB3-pTJc-TrJ7bhQUY5jz8OEgjtXLiO7Ppql_oZjIzGDVcmPF4_RrCb9fd5ZBN-vf0-F1xx8IGgLJ0ekCvWBTeHEh_c-NWwTnP66un7kydlmlYBNDxcnkKlB6Kf5PNgSlExm946hX25Zw1v8kcbhcKMFwvoLBpiE3uHj8Z9Yml6flDjY23jgmtBR6d21QIABdIa0FYN_K0g55Qe92JblgPpb0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
غیرضروری‌ترین بحث تاریخ:
خداداد: گزارشتو بکن
خیابانی: توام فوتبالتو بازی کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98279" target="_blank">📅 09:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98278">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=FtoN6ERsoHBlZWdBDcmQSbr-ZpwJ9S9apQoAQ_QaBbqgKjth-m2iRw7N2Pb5FkyK-0OFYQk1eIM8lheXjMA2fQLdTO_7TGGJC1gpQXgHRohsC-S0XkCEcPUFLhoEb8dswcLzyJOmNi1NvNf5bts0kvCWaatOxtyBGMbyPJIgMvam4dhBqzAD8RXoyVJo2GcpS3H469QMDmKpgcDk3xHVa9nMmNMXDsvWk_PcYV485uZJf1zzrH2Q0qXvgwW-h0QXkv-4p_Jq4Qb9epJhhzJb8RW7M_JTglezlX125fogEIAvC7DZPP2Wp2g2hSjo7Pnlu57GtJEyVBG483Y3eOSDgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=FtoN6ERsoHBlZWdBDcmQSbr-ZpwJ9S9apQoAQ_QaBbqgKjth-m2iRw7N2Pb5FkyK-0OFYQk1eIM8lheXjMA2fQLdTO_7TGGJC1gpQXgHRohsC-S0XkCEcPUFLhoEb8dswcLzyJOmNi1NvNf5bts0kvCWaatOxtyBGMbyPJIgMvam4dhBqzAD8RXoyVJo2GcpS3H469QMDmKpgcDk3xHVa9nMmNMXDsvWk_PcYV485uZJf1zzrH2Q0qXvgwW-h0QXkv-4p_Jq4Qb9epJhhzJb8RW7M_JTglezlX125fogEIAvC7DZPP2Wp2g2hSjo7Pnlu57GtJEyVBG483Y3eOSDgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه فوق جنجالی از بی‌توجهی کیلیان امباپه به گلر پاراگوئه در پایان بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98278" target="_blank">📅 09:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98277">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
بازی چرک و کثیف فوق‌العاده زشت پاراگوئه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/98277" target="_blank">📅 09:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98276">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897a264b10.mp4?token=CI7D2GEbIDxzuUo5D-B3c6KKnaDML0FzrNRCYXqU9VPgxRBkDeYkpCz0Vqfj0bR93pZZNF22aA1bS2ZAfYwB4iSz7SreoTrCzuvXYD35DFIglsyUQ-QM6CvOrkl3PjhYfaIytBY8Bix7H0o5g9PuraqA7_eKBke1IriKxZtiEXqzxEM8D04Vs9befDObpbdLlbcYAmZnfD9h8zcaM2pgn6A3-vhIStIqcnO1HUEAS0dUCa1lopdux4BC2ky5hM5FxznyugroovaLzpFYTiamOMM1tZvRcHPP_VRpCvgwcHeJ5vx6j-IVU2VLyLnLfYEoJNVpEnD0m10Zfs5BdKqwvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897a264b10.mp4?token=CI7D2GEbIDxzuUo5D-B3c6KKnaDML0FzrNRCYXqU9VPgxRBkDeYkpCz0Vqfj0bR93pZZNF22aA1bS2ZAfYwB4iSz7SreoTrCzuvXYD35DFIglsyUQ-QM6CvOrkl3PjhYfaIytBY8Bix7H0o5g9PuraqA7_eKBke1IriKxZtiEXqzxEM8D04Vs9befDObpbdLlbcYAmZnfD9h8zcaM2pgn6A3-vhIStIqcnO1HUEAS0dUCa1lopdux4BC2ky5hM5FxznyugroovaLzpFYTiamOMM1tZvRcHPP_VRpCvgwcHeJ5vx6j-IVU2VLyLnLfYEoJNVpEnD0m10Zfs5BdKqwvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
در پایانِ مسابقه، امباپه بسیار شاد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98276" target="_blank">📅 09:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98275">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=BoYZZJ15UA0m8iKYRl-O_00VO7kx2W16Y4OGT4iLEdHkoeBAwepJzvmR8lh-XKN7Gbly-dt4dIIHoVFLwr_f6n_6ufC_Sx5O53bA0oaPPQeIqjGFq1INhciFL98qdRJzIVzCLEnOVhVmqjUbNo1r1CHeuf-UDBAMi0D6AwUz9Qb_VmMTCoYHkjGp6577OPNyoMrF2fzfuIou_YHmLAh2XuG1UkoySaccsPKkrvB5naPKnlRkfGKrxh9LVROoJUNHiORJMu9cRsR-lS17WT_WOhL1UTusAc3RSrp0J35wt0sbCUP62suxF4VCzltS2n7jMYSxkSDpIh8j8wFVqleSpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=BoYZZJ15UA0m8iKYRl-O_00VO7kx2W16Y4OGT4iLEdHkoeBAwepJzvmR8lh-XKN7Gbly-dt4dIIHoVFLwr_f6n_6ufC_Sx5O53bA0oaPPQeIqjGFq1INhciFL98qdRJzIVzCLEnOVhVmqjUbNo1r1CHeuf-UDBAMi0D6AwUz9Qb_VmMTCoYHkjGp6577OPNyoMrF2fzfuIou_YHmLAh2XuG1UkoySaccsPKkrvB5naPKnlRkfGKrxh9LVROoJUNHiORJMu9cRsR-lS17WT_WOhL1UTusAc3RSrp0J35wt0sbCUP62suxF4VCzltS2n7jMYSxkSDpIh8j8wFVqleSpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها استفاده من از خونه خالی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98275" target="_blank">📅 06:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98273">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRJP4typm_1uwmNtH7JekRrhF4p3Y7QJV8ysfT-LXaxlVH_1_DteXx3bTrvk6CcnHQpeG6IKYoE8kIGwA_wt3_ZTLTev8iM3G9BQ35xCNgzN4Ytxlg1ot4wzqAFUZ0tKrp9J6BbtaMKk2lefeNatISNRuhtLfVx4MOKUdCuHHUxpOde7sInWHohAw_Q_H4a6kJ2NipvHQEAwar1NiLYP-pufbyDdIPMGImLFEkbroVXivYg2xfHQjtWXuHnT6dse3rbLgHm_vJckVblXJJO3QAPML_7jl5vUTRrj3k-vBJnHLLTVdV4zd2i4x21alb4Cb6vuhUO9FGHSyaamZWcL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIyj7Qz4NjufUceK7U8RGSC2rfaKgOwJrRWx6guUL9C55s4NYKze8gXyAxsnCNdYaIZnW7QQs3P56nSuPTCnUJlHdGhohFXXTxB90zdR5W2TkDVHcDU548nQfeKR0exPYEALYPFT2rqwPhJqOcCfVkt30_yBK3qfyplhn9AbMWYsXBR9ZoCu3JMGTyyZ09UT0WweujdvL5rlw9Q8aIdFH2ChvL1o5_RXUlGBniAWKzTpaSbxNKKpqcJsi4UyDgvkRwm52VpNmTcboQJ32TIh4-TsPfo3ZY3nk3pZ-Xr056pzv36i9ul9ackT90AJH_5YpguAALDi-8-cI4oagLmPlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/98273" target="_blank">📅 05:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98272">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=CfB_HYZAN0Pom41sZjs0tcp_jjytkh6-DcI_bIGmBxRDLEZcV1r3wSSX1zddXvC5O_hx2O8u6WcdGakdArtHZs85wxviImloz9xSs9m5jKT_TzyA75qIzm84KEfA4cc_6tBihubXOPPaEyw8A0O3Gz6nihdUUoAMtn5SgT2Jzbu1_FTxAjiFJj-OFdkLHp4-AkEi60hfCwpRz4bX2HGRZgcob3fdgniNjeK8ZZAsildcIe4r22UO66e3CSfRgYV15fc-zyam-MckFaWy5VFobs5pXOGrRExFsHdoQo9p1NR1ETxEtbszjGmrgnjeYV9M_M8mYKduXz08E33PombIxWcUfsmJ5iS-BNoV3M6JMnPO9A0YHq9Xg5GsAEG-TzObbt45E6VUDtVZ_x2higa1uwf2s6u4d5-_1MjRm55nWYaiPSvzjxk2_GeW-mo2b_xOY7nL8L_K2YdBDzFzO7On7uyT3PDZ1o9tyQuzhhESuYGE7TUbXcPx2lPH0SZK0HCxSrDkCW_85GtdKjvfRZgu56cUP-du9GtFyEb5gRV1mgM-hW982qUIEr3B2HNOFVC4S3UWFvKSBawXMyu7Ul9MfzPU-KwyvFK2g8JTROqvY-zIyxPmVRAVE_YFjoJSownJarI8na_dhhxuhOLxguLRwFKi2P3maVTAOOvJApddL1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=CfB_HYZAN0Pom41sZjs0tcp_jjytkh6-DcI_bIGmBxRDLEZcV1r3wSSX1zddXvC5O_hx2O8u6WcdGakdArtHZs85wxviImloz9xSs9m5jKT_TzyA75qIzm84KEfA4cc_6tBihubXOPPaEyw8A0O3Gz6nihdUUoAMtn5SgT2Jzbu1_FTxAjiFJj-OFdkLHp4-AkEi60hfCwpRz4bX2HGRZgcob3fdgniNjeK8ZZAsildcIe4r22UO66e3CSfRgYV15fc-zyam-MckFaWy5VFobs5pXOGrRExFsHdoQo9p1NR1ETxEtbszjGmrgnjeYV9M_M8mYKduXz08E33PombIxWcUfsmJ5iS-BNoV3M6JMnPO9A0YHq9Xg5GsAEG-TzObbt45E6VUDtVZ_x2higa1uwf2s6u4d5-_1MjRm55nWYaiPSvzjxk2_GeW-mo2b_xOY7nL8L_K2YdBDzFzO7On7uyT3PDZ1o9tyQuzhhESuYGE7TUbXcPx2lPH0SZK0HCxSrDkCW_85GtdKjvfRZgu56cUP-du9GtFyEb5gRV1mgM-hW982qUIEr3B2HNOFVC4S3UWFvKSBawXMyu7Ul9MfzPU-KwyvFK2g8JTROqvY-zIyxPmVRAVE_YFjoJSownJarI8na_dhhxuhOLxguLRwFKi2P3maVTAOOvJApddL1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/98272" target="_blank">📅 04:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98271">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKbxub2hcx6YHW-TK-np0T2IIdq3dUb0AGCzRWuGHsdXB9OMJs-pYl5ubYtmtto8v2Ysz0OEd-o_H2cxpovfJcLfKpM36y2sdLmE8kVObddq28HkMW6163_CjfFbdk_yZxlTu-O_dzxbNn1yGQFhiqbnB2j-upE2ycOXr_4YHvOetLQGD-BMXVBOwmcTAxAFe2Zt3LtT4mGHYnObc94bcUFP_DRC7qVc6CKF8PmC3teiB-apP7RVrjOHuZqEO9cAXTpyqdORNam0vxLQE7zwQe0DqCAOVPz4WLoeKfIPZlNl35dYHk_xRVE35hwJ9ugYxwpjQ2up7BjnhndlLliLFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔺
از سال 2018، کیلیان امباپه با 11 گل بیشتر از تیم‌های زیر در مرحله حذفی جام‌جهانی گلزنی کرده است:
🇧🇷
برزیل (10 گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس (10 گل)
🇵🇹
پرتغال (9 گل)
🇪🇸
اسپانیا (4 گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/98271" target="_blank">📅 04:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98270">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEeWlGlTv40Q7aDq49P8Js5lZM4mf4xhov8624opwWJf_gO8bta0P1LgAVb4ooJVV24LFGovkwWgYQd3GIBpj2shnYZWGGXOC1WD6AeHIThQppAKuGSzsRQPpvQzDp-7NypS1qG08_acGx0yCs1ILbVU6De7F6eug66F9basd7RLY_A2sYVJMiDDhIdUy0UMjxcD1uS3ESekP1D4K1DbsagHhEnq9C_0jlao7daqi2yTe5mKWwHWvV18sx2tqWQf_msyANS-IukWQsGDz0hRcsFU7pjyg_txPG-gFmc5PP708ERifg6lOS-PcYuE1Ve4LpUlwbz1wE7cY6p37DwFOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان: اگه من امشب بازی می‌کردم، ۴-۵ تا کارت قرمز می‌گرفتم. فرانسه خیلی خونسرد بود، آروم موندن و حتی بهشون لبخند زدن. بهترین واکنش همینه که وارد بازی روانی اونا نشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/98270" target="_blank">📅 03:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98269">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=PP-mA5IXqoTzm9sPbzhNd37llt2MYzcCRB09HCJy1z_iiHk8RsY1F32xYqr-OQyYGTXwUQ4h4Pk-bYLeh8C3FUEACzWi678epfDgiV1HbtQdT1wQynIt_2-I0bPP9YNejtZmKzabz1iHCXJ271RSkKtdACXOlL9VhlKC1PjpYTD8kxzSm-VYQnMOsySehOUuEnF7jOfAJzdwn2btXmQCsKyl5t4DC694D3XwlnWqzjpaq3Hx1FPhvkCaCxiVUTO-SBinka-_usUbph9fe_vitKDGdYpUHxD1cSVh4PfSJmI_ICFotNr-ABliCb_ZgH6v35zxrgvwnUwtO_IMQKI1kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=PP-mA5IXqoTzm9sPbzhNd37llt2MYzcCRB09HCJy1z_iiHk8RsY1F32xYqr-OQyYGTXwUQ4h4Pk-bYLeh8C3FUEACzWi678epfDgiV1HbtQdT1wQynIt_2-I0bPP9YNejtZmKzabz1iHCXJ271RSkKtdACXOlL9VhlKC1PjpYTD8kxzSm-VYQnMOsySehOUuEnF7jOfAJzdwn2btXmQCsKyl5t4DC694D3XwlnWqzjpaq3Hx1FPhvkCaCxiVUTO-SBinka-_usUbph9fe_vitKDGdYpUHxD1cSVh4PfSJmI_ICFotNr-ABliCb_ZgH6v35zxrgvwnUwtO_IMQKI1kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ ترین صحنه بازی همینجا بود
😂
😂
بازیکنای پاراگوئه با تنه زدن و فحش دادن همه کاری کردن تا امباپه رو فشاری کنن ولی دیکتاتور با خنده‌هاش بازیکنای پاراگوئه‌ رو حسابی فشاری کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/98269" target="_blank">📅 03:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98268">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPdajWgWt0RXu_C_kiRxn0V7fj_cQdnt4RPkTogfqdTg9qQcM0PkNAg1htE-v3NdHs9YXg5FEALlJriFwyNrtsGq5wvaSDMlHsqGluV4O-dx-qWX0TKMxydyfKh4QHBmX1BY7ZH3QNIE_Jtay7jvzeEijG8TQb8jqg9sqVZk3wKH8uBHBwsjaeTsA3PlJlozyl3RlWGoMeKv-NiV_L8HVaRBu0xR7Ia5ktCts3O4KPnqyrDu-Cg0qC01L-gcE_a_vLQCJ_xg8ft9qjv5Off4yQ_GX45_1JlwxP304xP7RGGMG4zVaj_A-kN6MNPSFJHblo1-y9Vl-ExgJrdCMuy0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار :" کیلیان امباپه گفت اگه لازم باشه دستامونو کثیف میکنیم. نظر تو چیه؟"
رایان چرکی :" دستامونو کثیف میکنیم؟ ما لازم باشه تو خود گوه شیرجه میزنیم"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/98268" target="_blank">📅 03:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98267">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUj5g7T8uyehuXalMbH5yJokrvkbreP1OPn__K2-e209kJjEirIpBF7R-lNftq0Lp62b2XrgTXOr3D-ejJJcTQjceH78bD7gfqt7IRZPU2xtmI-z3FMgSR-_5f3N2Zmwy6QcPXkvpvp2b_pRQMeyTRQn8cS8YaktFDHamurEhA-D1U-rgg6inoFBwjLrGsfHmXl2-9DhL6G7gj3JwXY7O9Pv53puNLuZsmjFdpNZURz4pEDPpPTQoRIaZgHmLnv3lCQaQV59AwlRLRIaUUZq3Orh93OYO9GxNGnyZAv9MKcmINVanNcUeggl0U8fzaqB9Viy706EhDwDY4NYwazTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه : ماهم بلدیم مث خودشون کثیف بازی کنیم. ما نشون دادیم تیمی نیستیم که فقط برای هجومی بازی کردن به زمین بیایم.
🔺
اونا فک کردن ما میایم با لباس مهمونی بازی کنیم اما ما هم بلدیم کثیف بازی کنیم. حتی تو کثیف بازی کردنم ما بهتریم. فک کردن میتونن مارو غافلگیر کنن ولی ما غافلگیرشون کردیم.
🔺
اگه اونا بهمون بگن برو به جهنم ماهم به اونا میگیم برو به جهنم. اونا نمیخواستن فوتبال بازی کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98267" target="_blank">📅 03:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98266">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYjY6rBAWbE1sXKwGegvt8UMAqlCTjFXFUPNMQNjtkRf9rbmUjbMWOKGffccOSIspJuwVjXD-rKhjATYmS2_9U57yVAJQWMfHy2zUKybcx2-qa3hE8RsBASONbWSJHcvBWZ9kwEX7ygd-Rjn8u5nMuI2zV2tQXtK429prESnCdvuMpEmrE8eo1c31PxuOdSMU2ZbpApIK51ondhL0d06wsZKFzsRJUkb8w0jHv3a8ks4YBpubrKkzYEivjVvdta3jvkwg9RCrhJRNuz_f3Bea-Jgkraw1Tb2Fzlmds628DraqGk4tSlnNj-BSyx0bF12Xw1NYWW4IWrTdbxRs7qnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه تحقیقی هم در مورد این آقای تانتاشف باید بکنن تو این بازی. هیچکدوم از کرم‌ریختنای پاراگوئه‌ای‌ها رو ندید
😂
چندتا خطای خطرناک ازشون نگرفت و در عین ناباوری یه دونه کارت نداد بهشون و سه تا کارت داد به فرانسه. خیلی عجیب قضاوت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98266" target="_blank">📅 02:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98265">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOLM_3SJrbrWSorjaoHvtepwwK8aj_WSuC8azq07KdJ334Xx8VOjHliXFF9dnZt3vgt9NJvebx3ewqtXh6Jc5u9ztWSrFUdNFlEOFt8Q-jFjQ6dtLZ6MlyFu8bRqo7ojr7E076PwjbL9F_sEBkdeHRVjSGSv1Yn75VoN0jB0KRcJkXPf_I5DxLbh8nM8GBvyijbI07ljuzqb9Ae8-Rov_gXWxDhYu9u0fpzswnjP9Bzq9wthE048XD2cnHdT2VEHR2qblJ0zVRyWrv0XqM2oskkQ0ZJcPYrcHzQvkyfa4-q5ocurOfLcCz0y1MFnXX7tCEFGqCTUfbJDg-qgdGBwyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه خطاب به یه بازیکن پاراگوئه تو بازی امشب: مادرت خرابه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98265" target="_blank">📅 02:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98264">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxo0hdy6WsXvO1VVplDklfahVGKrqP7PtYczVXnwr5Sz_uciHOWx-nwEjuLA12M_o-9i3Zo5CTK5JoXuu7jvhhjdb_N3G5tTcDt-Qya3J3szjQTDcHLazRKXk_z3YmD92Z0FAklWfdiX8PYiZejiXDN52IBbFPHjymjvItZFfwjs-7KvYMd_PDWApe8C2sE58xM-OS_rhUsyoLfuQ2gIReRfk6PbYhqCEWRpIsoT7_qHHF_WrBWzYrOwAkiXdx8S8oDkMFrA7eucFwGwa2gmIeKgm34PIOW42FZ_SLUiyWDEUtHjxo6horNS20GbWgBTpQe-u8fce-RXLpJT69HlPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
|| عملکرد پشم‌ریزون کیلیان امباپه در جام جهانی:
🏟️
19 بازی
⚽️
19 گل
🪄
4 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/98264" target="_blank">📅 02:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98263">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T64XsusbgTIk5NAx5ab2kCwVhw1zAUMVFL-i16hsJD6EoEF-exekccQ2lpecgDWnDvELA-sMnEF2xCjOHK-Jpu6esyxgILNCukgONJCMtzscFGmrx89ebZqUi6d6gEk-dQeyn_R-uoKTn0tSUlIBO8WHTrBghro3xBjAwmVQfuVtQB1LKDjJzFObQZ_bWRTkp_xxpbPCL-vgtWd4Gcx7-ZsxCU9RJe2ra16ezWFvGhR2DqAstwVZdlK5Wi9KmhXRd9b7vcl0fdZv8eUbafc1zLA1pekjqYPzX9jBNr56klmyt0gd9dWpLeYPMDhUhU5t71AMDxf4612H9fDyWV_N1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏
🇫🇷
|
کیلیان امباپه به همراه مسی، رکورددار بیشترین مشارکت در گلزنی در مرحله حذفی جام جهانی شد.
🤩
لیونل مسی - 12 مشارکت در گلزنی
‏
🇫🇷
کیلیان امباپه - 12 مشارکت در کلزنی
🇧🇷
پله - 11 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98263" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98262">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNcMa2N0N4hP1bV9I_Id4T2wvwKDhicRGaU5C5cWFeAHDzrXi5OdcUYvsgTgjJZlZlzVUlGW1Q5ia3SWRcn2hGU6frmQ4v8Sv6UM3GTlGMQqG-0l4TD8t5Pt12Z3jcgyebvIKc-mKcWzXXdg1FqJEA-z9ICCU9Di4qdgFn3VBpZy7N6ZGLYIj6ujmGX46cjkoAWJSrqYlmcxzYI7BRXUSUQN9pfw1qi_oPsXfP8XM8rAwDyRd7KX2lLKf5bFLmBsgCiPCFxdT8SCV86sPSDnpdjaY0jmji_NeFDuYDdxgTLB8qd_3jk5Fr_nRg6DvJx4dS6gMIT9C6PKZ4JpPED5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورلاندو خیل، گلر پاراگوئه با ثبت 4 سیو مقابل فرانسه به عنوان بهترین بازیکن زمین انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98262" target="_blank">📅 02:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98261">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD9KJUOv6LZ-ZOJwxQxj2xYATem1p7Fk1bhiEw0SFvE9kE0Mp0wqr9D1tt-tLwpFrZtCNQJY2zylxxFcwHUvrc_R-V9Wz6poU3EOeaprhB95pt37V4QjnLPvN4Ji7BDeX9fQDr51hYMleWP_abI250AvZ957YDQKQc-dxC-C0NvdP0ZjSXXhPlkbSKiD8JqUsZnkdSRLSiCEvOj31xIw2592CZ6I4hEGw9z32JkQs8uO0VSXZWtbwPq3gbfuzQL5sgwYPFi1aBDRlc1hmZewyN5U1oh7knVeYUiZN0ECqIS8xoQSs9kwcOb3ip5DDOwMtYIvjl-QkVHau1v4dI6SjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر پاراگوئه اومد به امباپه دست بده امباپه دست نداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98261" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98260">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98260" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98259">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ViJFfdt-a42sIXY47kxFYdIsJ-Ng5JyiKriqsL_gRk1QOFlpc7sgJ-_TVi8xW9COq9YTIkBvYfJNL90bAHOvkQ4NyQyXdAh82FRScotFcHUNMn_Pgp8yNmLIgQRoPzW0YidWa06vnuiu9Hf9pz5XmOU-OQ7xZMDSvg8bivWZ9AidcffXcDKxFzcziMKYgx5QkVGXy9iDOZEvVnOdoYRHaPIkg5RwP3o0KzdfFP3vcn9CbHkU5YS1AaCLn3Z6sGnrKFF3OltJFTHVRh4ECzGAaodR4szXyzlHxt_2ScXda01hb-cuUEEvKDQWgFT9Nj0d_RxkfZaqYG_yFr2Sma0qRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/98259" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98257">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHOBrJK8cefqKVqxqIjYzhZ6YsvLPwDXxRQNC3aNFtd3dKz3FVeuApAnqA1WvIiqSkT1DkSdTWOLMORtFIAfDDFNnKiJOArXWuHkPP1Z_GF59iMt3UdrtMSOHIK-Uw1zybetxwH8IUVylL_tXX2IcY9fapfChO0f7AQzzQaB6iAwouRRJpmXSVGO1-W0vHPwoNOBNG6kkba9TnUQn2rcOvyLD12ltyNO-4FGsl1iBwqTeql6LkTROULaOMohwkWBx-dx30ZRxRaYsdGBOsHobM2WiTof6T3t1Si6LlyFTEAwdNzmf4eN0FGXtDfev2XK82d77r5IpQWv1uTOBWFUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQnY8t2APpUc5ICoZwvJuMCyPmWtnVzll1oRMkdgBYK9228VksljvnEPfNYw9t3yu2sW8Ez4oDLsQkbb96yBWgS3CrdmTzQ4g-i0sQwstPmvgY7EZXAIwT-5WPpIcKQDo3pk188s9k_Yz4KRaX74E6Y8gE76ECFF1uEZuqaihoGIF-BKY1PlTQu9pS_5QJ43rDMd_TC5vO26dSOWXobuvU_73i2qwNdy-bCbBq_EWJd478BiCpw8SMmefvP_tgCRhwg1cu2s5RA5s33kIYoP9GwSCsBOVcfXFlal3iGRYjMNuZU66HDOsqYv94eBwpaMZksp0yaL1zrXIQV9KB3QKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت رایان چرکی بعد بازی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98257" target="_blank">📅 02:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98256">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMjE8nHwmjkidSnhrbO67uiE1UhSVckANOi4mP35XZO5ZmMKUaH2p7n_4G4Zzpv6qpV6YZy9B4SHjGdlOqA60-IRhDlNmSXH1ALH7Bo4iAs9mSXGeDL0sFpVxSqsLp18BascwjdhXHnFdSpjXzT7E2yHvEykRS9d22i33_CLRWJ5OicGB-H9mKelXgQQQnnGXvrHAZNd4zajP7iKmrCwvpmvHO8KTjYxTRrweLRnKk7pCyZB0D4nCjJ3Bve-y6K0qK4OxAxACN3hwr2BECzcoDb4DEEvG-XzigMi13I3wMSWq9F1mQuA0DDO6XYUHD0ds_gsR0Lopz_6E4CVWMxdPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98256" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98255">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkqZdL3WzWJaGq1cqbh-yEJP9E-CsA_jCOuH75A4O-nV_sz3Kwa5RSuhdG7An7fCTmSp7OV2y2-l9HKfasdwE5N-GDVo1BcwhrPwX9-xfc8KJkPoen6hhTINntywoD2uMJTTcCjMneieIGD1b6ekLWLq3qmIknDxNR-Al-GB4QswCzSwCfCV8xHbIYZER_WBQnDwsR6LYp_HDDQR2f1ATGis0yzLVZsThF4VKXyEPwbJdYAKVsklLSoPaM8ma0Ck-9Q-vbzM9vqmBoAVqEFTOoOWRyd6Gklrny8YSCuDevHFAHMqGXeMBbripnkyXzquihhMoxQbVWUeXaMjWlpohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇫🇷
فرانسه - مراکش
🇲🇦
📆
پنجشنبه 18 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98255" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98254">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGeB3AjBUcnGGGyOCfZxfUxr5mWKLNT3m3lDZnoF7KVueIKwXJj-jwx94Zc3tIcm4MLNA-FQXY1-kAcgo0xAmFC-1IFtfiE6YMARiaN4N2zK9-2ehLyAWOmlmtIa8FSiMea-ObKnjqFwAKSlxZLkOL94FdJ4VSuCu8JAqj0ijYDROKVt-8jCV-zMV7t4CnuIDiE7wSmrAlfEXEPFUv1JHXypsFnWGSriRGi1qj-kN3ewN-D59cxGfNavUyYmQ9jx_7nbOGVt0C304OkMXhp4dh1kqFxO4jC92DPpD0elFQ1Ng255rOz-izZMLmDXY1h-1H0c_7CKuvnMo6T1Oqx1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود دشوار خروس‌ها با تک گل دیکتاتور
🇫🇷
فرانسه
1️⃣
-
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98254" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aByWZM8I7-EEg6Wf3E0A_pjkPMp9E06LXTJaY1XeIRjIIJqkW6FSYKTqRSwHqPmlJBPuSxIk0grNIowBEHykHkB-ikyBZFC_HbUDwLODL9lrHaIS5gFnC_6qE7id4BHbifsqZXP1IbjEQd73x5J08SoaZyGX9aI31RWlcJ-wifdrM3ivWahOXJQuo7Uo7F1YNYinkNMxHOpFn4-6xR3ptkyXMLtnX57fUbYQoysCRK2Anosyt-PxUWJ_rPQSuEd0ZxXCpTpLUTwDMk62qd1GmgaM5M_JH4yJ8RvH3GA6i3Xyv2c9BQiXAlRuAfeASYIZLQsiwWT8GyLdTH02g6t9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98253" target="_blank">📅 02:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98252" target="_blank">📅 02:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=CWPgM7teMNRKqlusB9GdSqQAI5kas5ToFPFEUaKT4gbITm7K1pYrOyS75WSvpc_82ZpUhfVKtJhB8rrh9hpr3Xmws_Yac-0KNH1h7KUII8ZSUiWDF9aOyGuErd3xvcUuOmDmvF-jpPul_2W9NqjhDnd-40yMstnHyrvxMtNIeHMQzJ0r7LG9xk_ygNwrK-p6kzjJJ-x1athshCAmrytlwxdLn8yUTE8PBwxMTceCan7Z-emFB12aHJTyTNKNi6WzNSivbUxI1WeyvGecuqujRclr1P5R3XmfSe8s0SXAfwLYsKJ5uAAsh7ZBETwFAUPA-OgvuMFVDCFiBedzIjwSHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=CWPgM7teMNRKqlusB9GdSqQAI5kas5ToFPFEUaKT4gbITm7K1pYrOyS75WSvpc_82ZpUhfVKtJhB8rrh9hpr3Xmws_Yac-0KNH1h7KUII8ZSUiWDF9aOyGuErd3xvcUuOmDmvF-jpPul_2W9NqjhDnd-40yMstnHyrvxMtNIeHMQzJ0r7LG9xk_ygNwrK-p6kzjJJ-x1athshCAmrytlwxdLn8yUTE8PBwxMTceCan7Z-emFB12aHJTyTNKNi6WzNSivbUxI1WeyvGecuqujRclr1P5R3XmfSe8s0SXAfwLYsKJ5uAAsh7ZBETwFAUPA-OgvuMFVDCFiBedzIjwSHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
تشکر خبرنگار آرژانتینی از لیونل مسی: "تو پناهگاه و دلیل شادی میلیون‌ها بچه بودی؛ از همون روزی که به دنیا اومدن، تا اون پیرمردی که داره از این دنیا میره.
🔺
بگذریم... این دستبند رو آوردم تا تو تمام کارها و مسیر زندگیت حافظ و نگهدارت باشه. برای خودت و خانواده‌ت آرزوی سلامتی فراوان دارم و از طرف همه مردم آرژانتین ازت ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98251" target="_blank">📅 02:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98250">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اوه اوه ده دقیقه وقت اضافه گرفت‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98250" target="_blank">📅 02:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98249">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry9R99YKaBASO8C-xq0ygpz6siyC8OwcacLBLrZ6zjJpPBvxj0HsKa4V5IMqjxUHGGY_11qvjyMRi9d17evnmJV_qfo1P00ZLyaCKAnSg_Zaug49hL3mKOgHkK85Wavn26cZOeWf7iiBhg7W1Kifh4v5hpn12gU-Yr8ZFqyns-7YbdADbGXXyLE6aQ_VGE6LBeInP6_jmSs7-mMi6tJcTjlznpEyMqSp30luOUEUcviqu-XV7K_YklS5QRxc7kgxAofstC1hftTczFrkIiTSzC_Vu1yZ3QtWh1D0gIdNLonC9gqpUmWOIGkNV7eFHPLF-YiHq_NoPaeF3GBdiQ9fEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه به آمار 19 گل زده تو جام‌جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98249" target="_blank">📅 02:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98248">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=nhMrNB_ZmPhLSXuP0W9VySt5Zd57BJKtTy97WkqzwyuV8JHoFeVBKt1__0YC31XidmbhZOECy6m8bCK74Ylflt4BFYYeMkOshjOOQ4bcAikt_aoT8nqdvr-Z55qr6aJvW1u73FQfwoGMsaibj8h-jWY5QT47oB17aGv6IKBShGaj9O_NgXwColqbJC52l_dLue8446wphhk2mTbmKvznqDumgtzaBCS10bttyj77w23-im47_lDslam9IfU511oVglfLbBv3lpIF675Vmp1uJprtkvEY6ixUTRGAV4CSohaPwD41QhuUEcDcid2-5uNhncq3QczyzSspdYYqwKpZAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=nhMrNB_ZmPhLSXuP0W9VySt5Zd57BJKtTy97WkqzwyuV8JHoFeVBKt1__0YC31XidmbhZOECy6m8bCK74Ylflt4BFYYeMkOshjOOQ4bcAikt_aoT8nqdvr-Z55qr6aJvW1u73FQfwoGMsaibj8h-jWY5QT47oB17aGv6IKBShGaj9O_NgXwColqbJC52l_dLue8446wphhk2mTbmKvznqDumgtzaBCS10bttyj77w23-im47_lDslam9IfU511oVglfLbBv3lpIF675Vmp1uJprtkvEY6ixUTRGAV4CSohaPwD41QhuUEcDcid2-5uNhncq3QczyzSspdYYqwKpZAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول فرانسه به پاراگوئه توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98248" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98247">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98247" target="_blank">📅 02:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98246">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98246" target="_blank">📅 02:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98245">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">صحنه مشکوک به پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98245" target="_blank">📅 02:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98244">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پشمام چی گرفت گلر پاراگوئه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/98244" target="_blank">📅 01:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98243">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇫🇷
🏆
🇵🇾
بریم سراغ نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/98243" target="_blank">📅 01:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qpknWsxaNCUkNr4qrFWAT7Be6x2S9w67wynVxD71GcVaa9T2l7ekWDjGsHLy5-fsEASVJxWKKFwW37mlqDCtJtYUFlR-yH8TU9JyFyy08pvfYqKZN5JcjWh8-yHPymN0gvuEgZKlzsuDJZvHGp_82fojT2y-YDJ1_YF2d8sQL7S7h34SHWv3RPqAS6M6ED39kj5FmzCXlCgdgRetYTmg2N0NjyR4y1dfjoPDim8e3djAtgJZBCxRNpmr2foVjS2QIzkB5FCpCV4tsKyhy3rb2n4qwqM8mn5pcvnripTmgjNvWDYE9G2UbJIx8RUtw9tO5qwV-tjw_KD8hhrkpENvqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tLuVjtUcUuz8Qvv_-NraGgGT2nbAytBAGJkp-M3FHIudsCL8eLItACjdFrB3rpG_oqnIskZHNNSP6ShSIOOQXnNPTe2Hsz_WMdrV0sqvm5CNkxMNGhY0h1NVGblSEQCXxX5Y3kKtHQ9_TYlqEXEM2j5rjzGFo4-rmhrTu5VmN6FvFE-404tLeDSPcSio7-yr771OohBz_mj_WMh9_qzEH9dGkl1KMtG_Ij3yLbjmce3EoaOvGCAeCxSBA_9xz7t_H8yXgQwfpRoSLFf49erNVjSCHmVJby-XvkQzL2tJGGznLBbjyZxizjSwYHVo252XjoIyLB40kTjWFWuiiyVpDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
مراسم سالگرد استقلال کشور آمریکا که در بازی امشب پاراگوئه و فرانسه برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/98241" target="_blank">📅 01:30 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
