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
<img src="https://cdn5.telesco.pe/file/PWwb8sLpbgY0ZCNmZQLYm9Zam3CDDTGTgSh341yY00As8IFeXc6Yz9kjw5PFeDoH0cPDDlDtyh0ATYIOUffxHGM8t1B_6FtOKz1dyC7PT8JRLj6euAFG1xQVFpkM30LbnEdVI7VljHokLPFTyhQWMsZzL4z--roudc2rmR1jTVvzaJKc6HjbX_d3ePqCWvp36MaaCOmpBlk4qXzWXZhurtzXp_nfiP9xXfgSIF38tHfxV_jESyY-3PuSEPayEwAcTupwZBiw6z4rPuaH0qkwe9cM8SkxwXr2khVWdUNDBc0vnvP0shln7v-omG2DzjFs89dUres9r3_EiCpxqx7CMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 538K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 21:23:04</div>
<hr>

<div class="tg-post" id="msg-101701">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntcWXnJpKYRpwT4MkIr3gx40Nc0PFpZ6XPdvWQINqihnu3C2C5LT1BudJXvZb-l39Zwt0mdKcPaMN9Lyv5pE3YDTgPids2JKlJbN421LXMqXdUTHTnAAysZkaxUETAo8uX0bcC7eN44KveduoQsTFfS-mowwnm02RpOdfgCi5KQdRrhOvr4yBgjAv6H_c3iAqAeuvO4dsBqUg_ay59W7LrG0fz2yJ_btnCiIP-Gn7syBOzsA8oOSt_vO8dZqjdDlIsnMyCD-9ssSYWkd0DzkeUbz-9OuyBKNf2M90AhchSvdAdgjpx0j7rQb1BIaOHnUKT1bxEu8PuMTgwdRhyaQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا:
رئال مادرید شبیه یک تیم ملی بود؛ چون در هر پست، یکی از بهترین بازیکنان دنیا حضور داشت. هم‌تیمی بودن با کریستیانو رونالدو، بیل، بنزما، مودریچ، کاکا، کاسیاس، سرخیو راموس و په‌په واقعاً چیزی خاص و فراموش‌نشدنی بود. هیچ‌وقت کامل متوجه نشدم که برای بزرگ‌ترین باشگاه دنیا بازی میکنم، چون فقط داشتم از فوتبال لذت میبردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/Futball180TV/101701" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101700">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMKT1E0a0Y3Duj847s1aPi3yVZtsPKFyjw_yVL1aaX4MnqA9q5zXt74SZzOTc3WuUl2b-B43gWKsyl__wt6KTd7sQjg9IkLcQgaLVU99X7dUQF0SfNk_HSI84DEhd06LH3kD4Huz8sgHBwkRcTQRnrSCeYKZ6hfM_ZSVJfEQGT_deh-GRAc2h3EOwJA4-SC4Rw5PvPvdGBt4kSh2Hx4mv43u4VQ9SQiore4fovRHkZxbh5CSOzNlir3CZBKhUIdKSms7UxfgSYSsiYeFYFxV0HVAjLD2zTUKbXTNIkhHrV06I26pTwGeLVXENLHWLNLRZYrLW5mfCdAB5IHXmJBHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/101700" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHg0s6K5RNVaXy1dubBKUBWZ9ZAxPR1itUcDAiIDU-3ssCVsXz3OkFN_7WrpR-X0J-N4Fcp-hsnLbXmqKnPBYk9KBKLlO5uIuF8H2hem7RuttT-S4a9J59uEasvvLG1ZxUAdo1UYDXVjvxatEewOVLuQ5fCKuVzFLtiLZdBnbDm4_P_uemgNN1zi3p2ndqMmygVRk6X3TO0StiaVDAXiO4ntLB2VlviUr6nN3N_ThMlmorJ-2IIp_fXG7-NRPQic-pMpohX4wauN5i_qG99i-rnMeYL2ufzebXiuLNeLiIFa26V4qj4qeu9V_9fWGRx1hBKC5CbgiSbKQ_4pAKFRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
فدراسیون فوتبال نروژ قصد دارد بعد از دخالت دونالد ترامپ در ماجرای فولارین بالوگون، یک شکایت رسمی به فیفا ارائه کند. این فدراسیون نمی‌خواهد این دخالت بدون عواقب باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/101699" target="_blank">📅 21:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOKXcMKfvwLwTBMUtBUeFDXeDE4mv2gpJdqxr8-LfjsHJyKez9Czexmjcz56kUrVj0h9eloQYIkwruMUFVqtKd7Yc54yKYK63JC6qax0H6xiZKolErnlK2kDWE5q5EIxzJ3LNEXD-RBPqQep_D35Rsow2YRQZOpV2xGITl7jNmtxAKSS9zH5S68LjBWyoipLryKqxW0vL0hW6p_wqmBXyyX5Dt9VnYWCRHXerZ27HSVV1Q0cI518fyMdFkv4bUO1vOfR-cVaTcIhAP2MpZ_9A2qnHj-iadLisp9CkiDhUTA8UOLhIMEX7EbPcUh3fOSnglMup97pqgPD6MTv2xsX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آنجلوتی پیشنهاد فدراسیون فوتبال ایتالیا برای هدایت کشورش را رد کرده و گفته که میخواد در برزیل بمونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/101698" target="_blank">📅 20:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101697">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biZxtOpwShWOl0bjJESsqthGHCBBXp0FIYfX1wR7h-a4-rQo7_28eTTLKli0iovODyU0gSNlUCU7d5LCEN-PjyDfLkyUcLiHgEAH5KCI5Ekbnegq8Byfz8S5odYQOU_ZiX9gi7PJ6XJhHJcb6JynMtsuCTZNQ_Bm1IMjvNMHVqsh2Jwze8DmiLCA3tAGu-vlkSYIgq4sG27VhtQuhFj_n3GaZMjdb081SIqhhqrvjUYxhg934xm8xtrKNL07oJem2dsmp2tPseUbUXQRl8dAgC354QxV8IOb_T3jyU3LMrdY5P6EqczemUAPbGXIkruoaNj_6CmkisJ2UA290CYyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
لوئیس دلافوئنته بعد از قهرمانی اسپانیا در جام جهانی:
بعد از بازی، بازیکن‌هام به من گفتن: ما همه‌چی رو بردیم، در تمام رده‌ها. حالا دیگه چی مونده که ببریم؟
🚨
🔻
یادآوری:
این نسل از اسپانیا قهرمانی در یورو زیر ۱۷ سال، یورو زیر ۱۹ سال، جام ملت‌های اروپا، لیگ ملت‌ها و جام جهانی رو به دست آورده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/101697" target="_blank">📅 20:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3wd4s4nAsjhVFAS2JS3kQmHmFE_Rfgg-_egwbPKvr2Yvi1wPJTFdfAcVNanMGfPvDbcOUEd9Pv7yWW75cHuZ5-bu6qrvpnMbg7WUWbvv-v4caX8nJBTqiiGiAHEQV0rUk9awcjlSCMMaYPZVoTZ4xFTC6UtVoozOSGdnc9izFxlIEh91eG-mBuilCRTPHCNbj9qMnZKI4WJ8s1w7dKERX5X7FoNpQhxxgKHrEC52fg3h14nBZLwuiBhpJchzdAG8YBZl1a7ocCxno1g8VExFffLyfl4WIbB1a_mfln2A0Bc4EoYav-K6QaPXy-XGiCt0U9TfldhTY8z6NpzDrYB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار در کنار بتموبیل و هلیکوپتر و جتش :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/101696" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101695">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ9-tqjLnzraQWX6OTQM5d4b6uF0QiUyS22OitZ9sxK9M-LspbgN7X-hL7RIucv4xVzCs0N9HnjbzacC-jCj31mUSGIQ3HBXGCEFVxkgtRPjegttoL0Te7o3n96lIWgF9XEGwh25cXhA1LM6r_rXcZdHv31uww9Lmq2EiBmQBmJdCF3YX-wm4SpZ9q3saMXnLIIpKvkH7LYg9gTiBvbZZcpkhvKqSBzfCOgmPwUCkv1Isji213P_2JNmgG3j4LNTZwP9no7VGdNUcPKgsvKTh-k3utDIVEbNsHow5yu6AuQHL88PHkh7h-F5mw9gQgo_QV6PQhRZzyzjbrgXGO1c9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/101695" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM1UU5RzVARCgNQZDDirfmvhh-_DDfDnVPw7jIxvV9xmckFZ4NuVCUac_gkJT1qmShlADm7lAy3QF5tGmub9Ouw2Dcf9UUA_LF8YjBMQTySzv-SR1-U6l3gMB1ppVAJXJbS5inewWpMQ65ZwHEoEzTHIYdTZutH4iwvxiBHFUl2Zc2Xg_nf032ZvO9BnAEES4Wc74gWWH4Dhnje8fFTeoyCyi2-uTNu0eVkW6pcU8dvByajP_AaMjWoL9Sc8_2whjqi1L2-o7cfVkgdjAAwgk8v6p8OtED_NUulrl4DLHu_i9KaAYf9MgWrSJAaBbYoa2GdfQrCQBI8FOCAXbZASUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
سامی مقبل خبرنگار معتبر BBC:
🔻
باشگاه آرسنال قصد داره پیشنهادی به ارزش 70 میلیون پوند برای جذب برونو گیمارش به نیوکاسل ارائه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/101694" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101693">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=GhoGP0-Pz0VecKxZLQAWG8JZ9ynWtp0LOJamnOsHX1pgqfWLUlR0ZI-htl7t-DzusaU34bjSvdaPubKi4L3XF6BDQmAUnNRrPiBDpAPd3yS2ctueSZPYnIGV06lZElXdcDyw8SHWV8LOOeZmTxbHgKAP3A4EUKb0GxogT8XFA0ds9oUzpUqdEAbhHub6WsyzigJJXFjwhmNp7gfrOQJbk-__Fz8EIZ3PYoMDUQfynhVcTmJlKqthb6cRX4F7cyndXaYEEhvzyUmYfgv6iW0mEjy5N73vHwzUKX3as8JCikLgXP-PbHBnrZomVyx_zmln3wyzH7lNESrmMGFzdyGFGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=GhoGP0-Pz0VecKxZLQAWG8JZ9ynWtp0LOJamnOsHX1pgqfWLUlR0ZI-htl7t-DzusaU34bjSvdaPubKi4L3XF6BDQmAUnNRrPiBDpAPd3yS2ctueSZPYnIGV06lZElXdcDyw8SHWV8LOOeZmTxbHgKAP3A4EUKb0GxogT8XFA0ds9oUzpUqdEAbhHub6WsyzigJJXFjwhmNp7gfrOQJbk-__Fz8EIZ3PYoMDUQfynhVcTmJlKqthb6cRX4F7cyndXaYEEhvzyUmYfgv6iW0mEjy5N73vHwzUKX3as8JCikLgXP-PbHBnrZomVyx_zmln3wyzH7lNESrmMGFzdyGFGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اون دکتراهایی که دکتر علیرضا بیرانوند گرفته
😀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/101693" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZjI_PhXB5XGRM1Jzvly0fPLXD_qO2vFx5JtzscIAFmQwRuLD2BbgDSR-HTQe8jbe1py61UIon7c9PM_P-aV8i2ujJPyLAZ4kXRSHq1wFjSBOGVJN8SzG0Yq50B7UiqxjydMGugbXQsQCOQWVE-ebv6kbnnm4qSiAorE7hlmsXHsuWtrzzmXSoGu7aj2hkQAy4-Poyz0DdLQF5dfpCzM9y1InOlfxlpaMYz7uCgGeDdY1X80EIHHu257wpzqwJKEHiaxROksNEmTPfBZu2B2uPNPF0K337maTPOzlgUexXDXsnXb_418-3g4uAe0Ryv1piKEOYvDEnAS7fy97K_3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی که همه رئالیا رو برد به سال 2013 و اون کیت معروف..
⚪️
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/101692" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfHnv3Nucc2Cqtlwfx8AzOcGngqGBKqcdZCCqpNO4CsSl6DSu_VIhwW0sD9XvaKfGnpOkzIaumIjs5N_2PSATNht700eWyRDk0h-EVI6AQNUhzDPWnRF9clf22YJlv2povKLLINkxdxR1VlC8Epl3x7l44_Z8L-u_FQu5J11cGuvCR5FvXzspFGeqFsNz7AFLcuJ8WrmW6nlOqbZExE1ETbMMzEgPT16GeYS_WTLzU2vAbJvMQaYidOSBzfqy00o7_i09AbuSl1ZSwvRH334rtvZkEUq_78g8UUaHC4vzlWtSFvbXWJ7gPpvNsCC7M8ozUbPDNlIQMw3Mt_RQJ75rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو درباره پیوستن به اینتر میامی:
بی‌صبرانه منتظرم به لئو مسی کمک کنم؛ بازیکنی که یکی از بزرگ‌ترین بازیکنان تاریخ فوتبال است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/101691" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEGW7sU_G72g1rzeGwlEIfS1F4yH46mb9KsrFBlyN-Fi3-1DYQrAOEPA2LJ9AdGrGQmKN8AbhWvezkowNOVp2T__uVphVQKhJAt7c2fMe18RdpNGtiO_gRb4bWy8CJaeP-t4BRQlJ-35PHC4pHhHXLBSmIG6gMz8_8bA-3CkSJkraAKNCYL7GUCTbfi0djhBKSJdCd5WQoSgxTkOW1Q8vyfO6zWHLqf7VtSazWsVbs2SnwA7UAos1vxNkbRjULUCGh59r1WPkSCCms_tpxbA6akuE3eOEPaG0q3K6xeQwI5OQM4rljQJyVo7ERgNs447zHC_88Cx2AAHXGU0hI91iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
فوت‌مرتکاتو: پاتریک‌ویرا اسطوره فوتبال جهان بزودی سرمربی تیم‌ملی سنگال می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/101690" target="_blank">📅 20:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101689">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF2DKYPU7UOIVyKA9tmz801XxkXMG1NP1DXqOd3tr0JV5zFFdI56QCXb9z1Uys22lapQaCjHzXxRiUZ0KkNyGJgpowKc5J9aBg5vaxhZZ9I93s6t_k17vLfch2E2UuU9alGL0hobL1EK-GLcaMLJrOkbqjqQfqL6RGqZjz3Zjw0pBYtnnC_D1Ykiw39ajOa3XHnHcy79cr7GKSAGwqqRrA5Wcp5NsWEwJDpwMQoLxhqq6X26PeHLj5xhhFTG98CtV_V1WQpGA3hrAFizDugUI1Ww9UfwDVlYy8e-FbpahWO6x2ejvDb_pPkeAdNNCKBTXwy0Z8Oyz3NLNPtNJQDkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی
؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/Futball180TV/101689" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101688">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtyMv5uynneFzs5LBVDAMha3_03KeoP1kWgB-1bYkYayrk9t8mFEwTBJrcLqEk0yvGZVc4NkQUQFcHaq0WBGphVpTiJRQ_NzW12vEQ4KdhN3AiQHd_RkGyBq94rPfyitD0wYNxGy98dsZbz1_UwZs7AX_1R5cLgMs8OpUT3wQPMrkdsCgtdnHr3fpF6dfHZ3Y9HrS4ntcs6lqZ5-qRoLQtyAzGMUDhZRbXIj8qnenym1IrH3xUBdG3O0DAJXeC4ZuwWUfQhdP0lQXxKWJ4eieCnVzaeZPGpIaw_akjdpyqVlpCjj1RgafXiY4O-vRZV5Dg_s9MaR3Q4DR0gKpU7s-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله کارت زرد به من نشان داد. من مطمئنم که این فقط به این دلیل بود که مسی آنجا حضور داشت. ما 2 بر 0 جلو بودیم، بنابراین احساس می‌کردم که داور فکر می‌کرد:  بیایید کمی به مسی و آرژانتین کمک کنیم.'"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/101688" target="_blank">📅 19:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101687">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
فوووری و رسمی؛ تریلر FC 27 منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101687" target="_blank">📅 19:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101686">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVInxnkaj2L1xYQkevoVZcOhWIZzyT9FViRKK-NYtKoFOxgrfwJJxyKC7ZgJhRZiflWcUHHbIgMNFmYwBmo6uF78UVdiafYa4zXw0-cN4ZI7pE8ThrYpZbqyv0tKaIK8ccaRvxAjYZgK_zr6-X1EOzevoBYydVOfO3vf8RGppKuZ_AuEUXS8OwdG6bjj_j93DTPA3KKGS8ekT4BrVVMpLAYDdILwe-21ZtRnH3tNmU_IcRat31_dFB4_yFbvUqDYEP3ZkddGvBlOk0Mf0yDLIrDFxq5cHzIQ4YgiokSE_I9ZVnwumuOIpFCBNIzM3vGmSanep-fvmAIsYdVr7xVOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/101686" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101685">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBAdYAfTvDPpPSBVbe1x_7BBbmtjzHPkx26MtIPZMjD301yyJtls7mOk4uRGrDxUq3946Qj88jjyEz1AcQlvPU-utcSKFHGjCHuccvVvMCenXrWVCKnBKG8PiuDxUPQNFh9VzMfqcVUT98uPQmg2MoGnPPbAbWbhCZS7WyLST35lVLxORDYoGDgF0lb1bGC3kVVdfKzFrF4zQFg1LJFjGo0Q3ZgmDblqz5z_YrSO4qM3N4HxBToQVC-pmj0r3VPZtD55z0v9Tsr1d9KqMmhMlXOsn095X9DT30o_hS1L0reYeJIePS3pcjMbOfXtToAzlpkcJ1XomueFB2b1lBx90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/101685" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101684">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfvRiurjBmkmc_PgbBdICH33E7aBs8bjV7JyXbcf9fS88FIT2dUq2lBl1RcLFW81HLdliQWbyBJP8OkEzVrCLeNjyEv7ZId2W8_5mAEe90Q_OWw9BRDCCiaE-1-pD0e1bqjoGpJ5uBguYCIspmEMwkp_HBfNXtksYvfukcjA97s_52bVUSKqohZe1XbQ32WySyTKEuvXHzkbtJY14BfICMcBpZ3WgKHUVm9a9uu5JPquAl73fWSlWGcUjqgpLplH_fxRCGtrowOiEKJXo3BpdTi2GhZzGN22vD86b8QEpzjtofIUV1hSCeRb0ikRUvZdaUCl9dOc4BTzQeb8zZHZzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسمیرو رویاهای همتونو داره زندگی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/101684" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101683">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEiljS4vHyiit-kHamXfMhgjnaTCAatHey93LLepEHz1lHAFyf5b2VgQIBClCYWNQ_qX0EtglWaYkpBlj8_zFxxNn6fN6Nq59_gINMpj7jjxp8ubkbhThrW0zMH5CwOHi4OCJz4WBl890HhQoQqiNuZ-nMw7gPjoCK-vSZbbCoxYIGqxZbQHYTwAoK971haD2thQQimf4pj5k5F3erIJ1C8XzZfuwdwJrV3nDL3RNOaPALXWcgzgcE48BRs8url7i8kA3y_AYsUEh2kreRc1_dZTWTEVfGQTiS5fcMbbXIoCAh5bdHRAP97LZEOv-jFoir5zFp8F53tU84twC3RCmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمیییییی
: قرارداد لوکا مودریچ با میلان به مدت یک‌فصل دیگر تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/Futball180TV/101683" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101682">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf1Fos93-C8uyhHG5LdSPvMieoQbnXMPTGFQY7I3gImqqnbpT-kyF4xrN4dJwu9Hkrw9R2HRqracN746SkkGEjkgFdLcAGjUrTUN-oGKueit3bk7XjK3auT0DE94dO_ptRa3DxvF5EQu8z2pB1BTQs0tTg8R2vS5t2XMPi2uRks3en_EyU8fZBxnRE3gEdZhn9c6SwXfaQKaN90X72DZW8mqPuAG1XYgjPF_GuDuQi9MACtJ3MzwHg9ZPT0DBLle3iEgQQi4A6Cty6qCEYT2oHL-JB0OQIlo-wyLfNMTfsTOTczyIaaZzQYO_4UQrvcnn1Ja4wBG2ZtMAjesuVP3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/101682" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101681">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=YPOxpb9DuJPAqIDmwoZ6T8YmaGKHtEyoJtIaNRfi_9giFBH4ZMcY-k4UmXHxeHAiC0IgjqayWkplquux1mmHUDEiLpOCEZxW3bwc7ykYz0Z4dbumtsweKv9TvKgrU45ELOBhTZVRuCEGmnbhWAYTvioRLerX8mFKtBNQQdiEsbsWAHJKOldH77w6nCwqwpK_oHxCJT1hRlTaTtbHF_Zd_sLrOtKOhWQfBJH1q8G1mMX2v3OGvJQNjgwbzICRNoOIUNhdX3pjqthhOa_s1DQhwNAkUroNAUhvXt2gqHVdogqvxU2BSIulVrj2wdRwh3X9mzCK6_tfw7jc2sjhS4ndYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=YPOxpb9DuJPAqIDmwoZ6T8YmaGKHtEyoJtIaNRfi_9giFBH4ZMcY-k4UmXHxeHAiC0IgjqayWkplquux1mmHUDEiLpOCEZxW3bwc7ykYz0Z4dbumtsweKv9TvKgrU45ELOBhTZVRuCEGmnbhWAYTvioRLerX8mFKtBNQQdiEsbsWAHJKOldH77w6nCwqwpK_oHxCJT1hRlTaTtbHF_Zd_sLrOtKOhWQfBJH1q8G1mMX2v3OGvJQNjgwbzICRNoOIUNhdX3pjqthhOa_s1DQhwNAkUroNAUhvXt2gqHVdogqvxU2BSIulVrj2wdRwh3X9mzCK6_tfw7jc2sjhS4ndYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سوال: آیا مسی بهترین بازیکن تاریخ است؟
🇮🇱
نتانیاهو: باید بگویم، در کنار پله. اما در دوران ما و در دهه‌های اخیر قطعا مسی. او چند سال پیش به اسرائیل سفر کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/101681" target="_blank">📅 19:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101680">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
فوووری ترامپ: من در حال بررسی یک حمله گسترده هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام داده‌ایم. به تصمیم‌گیری نزدیک شده‌ام. ما برای انجام آن کاملاً آماده هستیم.
اگر از اسرائیل بخواهم، ظرف دو دقیقه به این عملیات ملحق خواهد شد. ایران به اندازه کافی احساس درد نکرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/101680" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101679">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=MxmhuXRZ3K4XVbM0H4DMA9WfE3vEXqVMn-OpaEBhUjTiZmVVYb5Y0cJRMP-7Ewwt9SbA7BZwjXWG7B5DPlxdL_4G0BOYQky8130Ig-FpQ16JLelsFJGXRROhlOXm97F5AO_QbgodcqgoWtgTIidhJSmi42BRJcIZJJ3iqqfUIJgZVvy8YIHZHUOvf8WfgMKM45tFa-nkYo9Wbj5xItulYLfPDIUe0qhS8pJz3mrtXsR68LsLewoKSYdtPFkx8n_P9XCj-AWexrGktWpi51bLr3rZer3KABcDg8SWIPD7PgoGDcrHRLEBOy5VHdQuAfNdeGezEWjgTNVQBPizKO3HTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=MxmhuXRZ3K4XVbM0H4DMA9WfE3vEXqVMn-OpaEBhUjTiZmVVYb5Y0cJRMP-7Ewwt9SbA7BZwjXWG7B5DPlxdL_4G0BOYQky8130Ig-FpQ16JLelsFJGXRROhlOXm97F5AO_QbgodcqgoWtgTIidhJSmi42BRJcIZJJ3iqqfUIJgZVvy8YIHZHUOvf8WfgMKM45tFa-nkYo9Wbj5xItulYLfPDIUe0qhS8pJz3mrtXsR68LsLewoKSYdtPFkx8n_P9XCj-AWexrGktWpi51bLr3rZer3KABcDg8SWIPD7PgoGDcrHRLEBOy5VHdQuAfNdeGezEWjgTNVQBPizKO3HTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تنها جمله درست گفته شده از صداوسیما در سال جاری خطاب به امیرحسین ثابتی: ‏مگه تنگه هرمز مال ننت بوده که بدیم بره:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/101679" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101677">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBvBU9UvZ53UrRA77PoQTnoi5VwF04uCG2BZoiKHpFAR-7Ry2byf3XWqJiUDVLKCOLTSzb5RAqdYI_QB0QcIi0ZU3VY9aRUdLK_J3Ebm4UBSY13tTHGp2PRlIxYf4uyTfn0PMan9mbiN5EW39vXUgDe6wSZuhtW8BiD3wIs7RDtAxX5tnXgPpxjiVJ6K7gBGCNfTyJyI1zixgTo8mqi-B7xQvDMu9ABT0-clUk73d2FNRzr5BUAmMMkbj62uf5dGgDXVEp3RCu1nVqbFCvjo2s1DEWjf2tOi6rd9tFEkg7O1Rc6y09YaTuFCIhzcpPjJ0_SMgh7EPd2BuA6G9A59XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4cstiVUr2mWlDfsIZ0LugzXVIRuxfvMof9lxiKDWqr9w2alY5OrwWF0l8sIFJfG1OAi2LCEwyw5V8GrqAmrTcZs2kE4fHd4WErYrHwjkAJjP0tEaJZ0VKrHbGx-w0iJmikqV0B4ydzbALpRU309kQwHCS4YNRHfZSpt3QAz5-Il1P1LmKRtqiOxq-Bnu03GlkhG13PK0J9GXRIWOfmzBer_C6swwcVsc_hRvv8rICJayuFKz0ZBSI56My8vk0fll9l51SXtI-EMyAOdhhyAehpM7OCoQwSIKBaqeNnUUMSmjMF--SEPOvxwH6L1hjlrwxyMK_Zd8LhHicOpSj8g7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تبلیغات جورجینا واسه برند خودش Mimoa
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/101677" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101676">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw8HNr0feMR04p14iPj-ew_zusvFoQq5MfRbzm_i5rDae5RI3NSSy41JfXOnEUy7jaKsmpqwJg-8kJTGgrH03zxn2I8R-DHgixrHsksvrQ7lMPSvuwu40-V-vIeCB2m3zbXVRheS068dQgKLXrFD_PpXkCML6HkJw82M3Epsd-lnxWuZ2y2PTfGF23Klt0PpqnTx1N_coNVonNlwUkTOacwf-JQyeQMj5Go18B1GGojeFU1lJe7eoNykv3QNNWu4RwDSWTYZR0lG45Ud3Fq_I19tfpD2FMgCe3xWznL1n5KxpTRDatU2EaiijIgORStluKvchKmqmelMeRf-Nwm3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
منتخب بازیکنان آزاد فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/101676" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101675">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d6746099.mp4?token=Hb8z6I2Qetg-zk_BpHXgRiltOzXNQcm70NEjaujLTD0U5LObyUHjdJx7i0qrN7ZPHdsncxPNj67e4kBSKP5x2NPdKhOaJkprAJ0NCfUvQkmWRm_TBeATq9OM3EZLBsfMO5njDwI-8XRKbnMauZd8HiZsH9CFk-ylVPnsG8sXwCKk5ZQJQWWx1Tj2f7f1MuNjSKpbWiWYeLd31VMnk71sTyaAXbDLSBVoNREsOp-uKna3jcyoA_9W0a2sAMevwE_UkpPRf4lvaHHlkqeCpFLcCp1-pj0_fh48PQNzUXz3maglZVdNDwql73NSXOR8dpbmnwlOlKkNGZudduRuO5AuYTkSzCkG6c4wlBtCa5LMNJIIlmbIYoK8ocAGUi9brWf9D5cCVQ2VqEx82FkgNiO7NgTP_BSUk4O4lq_3OhtxpEInNKg4So85tv8Oj8ifLtZizoLOfjhnrh1E8MBSK9JyuStbCn9Kl8o_vVzCJ3OrdbwkV-te9v6SBthJ3uTKwt-p8HemYrObffAMB3HOz6Y5x8yMZtYDXJXADcVOrkVLClwZTPo7DlUGUcFoG85NjN0_6NNxHv1Z7Pd4TKiJ4YQb-1lSxJl-1KZH6B_VUzS9rWk4R44xkFlc6FvyvSM9KPhSFLULs4cvjFF2wByJgbzhtH9SpMnfnxBsSEfFMy2zE08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d6746099.mp4?token=Hb8z6I2Qetg-zk_BpHXgRiltOzXNQcm70NEjaujLTD0U5LObyUHjdJx7i0qrN7ZPHdsncxPNj67e4kBSKP5x2NPdKhOaJkprAJ0NCfUvQkmWRm_TBeATq9OM3EZLBsfMO5njDwI-8XRKbnMauZd8HiZsH9CFk-ylVPnsG8sXwCKk5ZQJQWWx1Tj2f7f1MuNjSKpbWiWYeLd31VMnk71sTyaAXbDLSBVoNREsOp-uKna3jcyoA_9W0a2sAMevwE_UkpPRf4lvaHHlkqeCpFLcCp1-pj0_fh48PQNzUXz3maglZVdNDwql73NSXOR8dpbmnwlOlKkNGZudduRuO5AuYTkSzCkG6c4wlBtCa5LMNJIIlmbIYoK8ocAGUi9brWf9D5cCVQ2VqEx82FkgNiO7NgTP_BSUk4O4lq_3OhtxpEInNKg4So85tv8Oj8ifLtZizoLOfjhnrh1E8MBSK9JyuStbCn9Kl8o_vVzCJ3OrdbwkV-te9v6SBthJ3uTKwt-p8HemYrObffAMB3HOz6Y5x8yMZtYDXJXADcVOrkVLClwZTPo7DlUGUcFoG85NjN0_6NNxHv1Z7Pd4TKiJ4YQb-1lSxJl-1KZH6B_VUzS9rWk4R44xkFlc6FvyvSM9KPhSFLULs4cvjFF2wByJgbzhtH9SpMnfnxBsSEfFMy2zE08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ویرجیل فن‌دایک مقابل بازیکنان بزرگ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/101675" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101674">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=f2pCn4L9-tBkk7ONXAXARFiZ6oDL47w-18UWhBbK9zQ39Txc3r3pAV__WrjItu9PbhStZCGQbi3-fEOJAy6kuMPcFrFx12_cNnPJ3bBFlG1wsHA8pD3I2pSFZzoXuLs2_qvqm0gU5VrjvDnVOuHObeFJj8Pl02U1v8Q_IRdRmoEh3VFOZ92F0OIeF_p--QVu2OuPgW45jZzEJ2OE7XDk3bxvNUkTR_59379DUov34CM19xcj0i5K2nXdlzxt0zFU6arXyhavXI1ke8urwZG86M6qnaAJ-8N2KFVyFe7kdNe32IuVuxphnaFq15xjdNJPrN8jxipuNUX3_PkUL6fhTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=f2pCn4L9-tBkk7ONXAXARFiZ6oDL47w-18UWhBbK9zQ39Txc3r3pAV__WrjItu9PbhStZCGQbi3-fEOJAy6kuMPcFrFx12_cNnPJ3bBFlG1wsHA8pD3I2pSFZzoXuLs2_qvqm0gU5VrjvDnVOuHObeFJj8Pl02U1v8Q_IRdRmoEh3VFOZ92F0OIeF_p--QVu2OuPgW45jZzEJ2OE7XDk3bxvNUkTR_59379DUov34CM19xcj0i5K2nXdlzxt0zFU6arXyhavXI1ke8urwZG86M6qnaAJ-8N2KFVyFe7kdNe32IuVuxphnaFq15xjdNJPrN8jxipuNUX3_PkUL6fhTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
داستان دختربازی افشین قطبی
😂
😐
محمدرضا مامانی، بازیکن پرسپولیس در دهه ۸۰ با یه دختره دوست بوده، افشین قطبی خبر نداشته از رابطه‌شون، قطبی به دختره شماره میده، دختره به مامانی میگه، بعد نیکبخت کثافت‌کاری میکرده و چاق شده بوده میخواستن بهش گیر بدن، این با آتویی که از قطبی گرفته بوده گروکشی میکنه
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/101674" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101673">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RyfTUKBmqK8Clx2fQueQugKySoW2psDJLzxMpqtghUo1LJjMtU9fozwz9vuc1toC0UKE8m4TnQKAWSM8TsorOAU_IwtyR81CILb_YXOC9gvEtoQmNBiv0CSxvOKvMkpLSdeMSc_sSsX0D7jCmPAQXbHhHLI5mFzkrdn3DfZDsgY25mVJWPaUtypTgMpHKbRF3jDOJVvcULYg3xEyflyYw8NLrZVZrD8WMpyOTkJZpW7Oa1Bp5ozJqA6EimPGGLdw7meeCFatIL1vybP_Jx4DPe1Vyrmy8Kl7t_IusnrItT3EGPbdXDaahMkDYHVfteFB3RYfLviS1eOEhMsmT7B1yhTW4089XtxYVAxIB1B6Jz2hUdyRxPIwzECMw-RwjQfUJEUuNJ3aDtCq5w-Q1EFNPlrZP0O5i589WGBZakLp2IuS6c-5p_lzoRbbRmyj8fatxP5ne4xRKJAG1uMBCDRxrHik6LBOIkjLtLPpRQHzUWgfRils4pq0_4Tn8UkTqjibCs553PcpJGDeeeJscXHGkYyd1h0ykTcu3NXalfoGdMzJz2pgNhCZSTyV3eOEPqIWt_zr0pNU5fS77Qz3N_QBmoeqf21mcgIRBJkQkhIJsR8YCbOs-0nBe_RM5JoL1QT_0AnoT42uIYdhUTwCGOGmUJJu28kqjRxin9JvH3gTXlI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RyfTUKBmqK8Clx2fQueQugKySoW2psDJLzxMpqtghUo1LJjMtU9fozwz9vuc1toC0UKE8m4TnQKAWSM8TsorOAU_IwtyR81CILb_YXOC9gvEtoQmNBiv0CSxvOKvMkpLSdeMSc_sSsX0D7jCmPAQXbHhHLI5mFzkrdn3DfZDsgY25mVJWPaUtypTgMpHKbRF3jDOJVvcULYg3xEyflyYw8NLrZVZrD8WMpyOTkJZpW7Oa1Bp5ozJqA6EimPGGLdw7meeCFatIL1vybP_Jx4DPe1Vyrmy8Kl7t_IusnrItT3EGPbdXDaahMkDYHVfteFB3RYfLviS1eOEhMsmT7B1yhTW4089XtxYVAxIB1B6Jz2hUdyRxPIwzECMw-RwjQfUJEUuNJ3aDtCq5w-Q1EFNPlrZP0O5i589WGBZakLp2IuS6c-5p_lzoRbbRmyj8fatxP5ne4xRKJAG1uMBCDRxrHik6LBOIkjLtLPpRQHzUWgfRils4pq0_4Tn8UkTqjibCs553PcpJGDeeeJscXHGkYyd1h0ykTcu3NXalfoGdMzJz2pgNhCZSTyV3eOEPqIWt_zr0pNU5fS77Qz3N_QBmoeqf21mcgIRBJkQkhIJsR8YCbOs-0nBe_RM5JoL1QT_0AnoT42uIYdhUTwCGOGmUJJu28kqjRxin9JvH3gTXlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایت عادل فردوسی پور از الکس فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/101673" target="_blank">📅 18:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101672">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB70JOf1odqxzkYOu6FDTPTFHJbWe8mDCQ6pJkRrH6qdMKjF3vFJgzW14N8kMeIZpFw5YIWb8V3twGlrP2Kpg3xreOSqfP2CPECot1HelVNvWGiPb7dZ11VkYgcX3zOlcUTZ5GhXOzmi7w7ClOOADFwVsQXabcK_tMCropmI4pcvDgqZHy9EU4Lf0280AOuL87kjMx-UFj92i9y1RZPeCJNsMCXZ4rh4pTFP3XPUBX83DnsEBZPYv9kBwQVKWEOCKXd1V9uA2nIXqwsmdO2KlZhgPa5YaEgMEP6VNyEqS-PmpPg-2VSCjCvkw31hAjWGiFgapHoPaGpBunSe0r4P7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180
؛ باشگاه نساجی مازندران با ارائه پیشنهادی خواستار جذب محمد خلیفه به صورت قرضی به مدت نیم فصل از استقلال شد. این درخواست از سوی مجتبی‌حسینی به شهاب‌زندی مدیرعامل این تیم منتقل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101672" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101671">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815514f088.mp4?token=VXxUUX_kinZ2wdmNjcN694nTBiyonrspYBbogDFIjW-ShBZ9QzHM1q33nrak90xuLBxg39xiOY8wL39b4Vtx7wAO1R3jT6ye6KJ3zzgewmIok6KYWR-q_x6vRzGE4_m1g20SQn-ZSDhxhewkr-VtPBKFIZyVU9hbp8KIWIpZgQgl_0v_q3uV8liaiuiwckcKS3Sw3w0tJeH5YYYVp5HnYLwEgskwMj6qc0DJeAZ_QX_ljgZ1zCOAKbdv8T04A74X6NIMuAmhVg2nnETLhdj9vLjkuwdwtVRgn7ahtOZvIEr_YkdJELuhGT_ZQMoK8UXNuZIHjnHmPrtvPbM2kAcKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815514f088.mp4?token=VXxUUX_kinZ2wdmNjcN694nTBiyonrspYBbogDFIjW-ShBZ9QzHM1q33nrak90xuLBxg39xiOY8wL39b4Vtx7wAO1R3jT6ye6KJ3zzgewmIok6KYWR-q_x6vRzGE4_m1g20SQn-ZSDhxhewkr-VtPBKFIZyVU9hbp8KIWIpZgQgl_0v_q3uV8liaiuiwckcKS3Sw3w0tJeH5YYYVp5HnYLwEgskwMj6qc0DJeAZ_QX_ljgZ1zCOAKbdv8T04A74X6NIMuAmhVg2nnETLhdj9vLjkuwdwtVRgn7ahtOZvIEr_YkdJELuhGT_ZQMoK8UXNuZIHjnHmPrtvPbM2kAcKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مارک کوکوریا موهای بلندش را فقط به خاطر استایلش نگه نداشته است. پسر بزرگ او، «ماتئو»، مبتلا به اوتیسم است و در تشخیص چهره‌ها مشکل دارد. کوکوریا می‌گوید موهای بلندش کمک میکند پسرش هنگام تماشای مسابقه بتواند او را راحت‌تر بین ۲۲ بازیکن پیدا کند. به همین دلیل هم قصد ندارد موهایش را کوتاه کند؛ چون برای پسرش فقط یک مدل مو نیست، بلکه نشانه‌ای است که باعث می‌شود پدرش را گم نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/101671" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101668">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ST6eo3B34Xj0ZeqX6Z3tSRbqDchYBiINa-qHASR8aMpOltYsx-9OKR0nD0i2kvw8xmvieaOKmTLXwrfefmHgpdP85m5nFQE8VMeIQgXS1lZuVGbkCTBwSAS64Dgl0YQpVAfWoqN0eEA9xkdhO8B3G80dHz8BD5uVF6mp42QRRs3K_P7UvNVgqzeFaKr140cJI1lJBIg6CKs2Ul-_tYiteRUJ58QKcCsdo-Cdl8lcPS_ApmUJB_bex7T9F1Yrgxd29qYJ217O8hwzUd8O1CfoIoJQ4fDfmwm2EmDCHIad0GVJbf4so-1h4XUmXvEFWKuFFcJVcVSx27Gv1HMN7CA1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1vkkjs21BmP7MfMcuyhV9smh1ODH-wqkd1bziKOL0-Pp5ZP6xSvKdRdsc9Qcanv0joIyy3EIN8GYdaBLxhKKrJIaIcgRGQeAK1vHUPDuAiWfCbekfu08ZaHyy01sBs9DkCA-olyU9ymp_zo9nU2RvbvH-Q6sFbuDUsF7Op2xAbycf_NPvHLRi3I3yIUUT29ebq7b8bZLNczV2WAoYXlZXhX7VqmKttJJZVLnVOJvmUqcvqP_k5LOlQk4HeCJRTZo9s6cv41h2k7G1VajipBagkFPM_10SHzind16vwJOBLmeKA6aXm-ppG4g2vQdDNPYlrkWNAc9C7gnntr5uu4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRrsPW05O3pwcUa82LJIda_m4qdtmLo4Y-wSmfelMnxaMHDajlA35i_8drW5F5zE7LaBDUWtSMiirTHq0xyiJZ5T1Q31gvEs3m10CUE0ioEF1N977Or1FwqmCUO8hykF3vNr8tAfR0dBN6uxKhkke2PetmyziMefOLqW7RIKMPCtGipe6a-1zGfjtpyWbGZr86veFxRcTzhuyEQaeRzW3DEWXgKot2654zUED9KK2OAwPEyPz2XW0KzMeq1jSJEckzXus65btVowV2T-TQXHZUuQFpjWOO8H7hALMtBTne-iVI6tHe4Y9FnZDSUWc3Ms0_GVZbdyVPIOugKivXij7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رونمایی الهلال عربستان از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101668" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101667">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGaeFby7uG2mrVSxh2Vi9NGZf5NOb_CHsP23AMWJqsFpp0Bl6EAVKm1OXp9lnchcuLvm8-HQ33PZLS7Z832YC0liB8JYC3_dq2E2qLozbsSSAjmVhTue4zcsbRbynPsjjG4Wqel4CBxdDzt0gEXNddKSGbe-poL07Uw4d1YtBDdKCqUWoKBm5lh21KMv4r2sqwUfbNXQvUkuoAohf3VQ1_MYz66HfEbbhH09940tJMtoKKRx72sYuV-YL2e3qS94adKcYgdYKmB-NheoNwXG3Bzw_PWWY78O0iuK2fAQiJvUUwMiY1RRV5NJH24ftVFnCIWzL58eKJEzm7Bhk6S4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
جلد نهایی بازی FC27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/101667" target="_blank">📅 18:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101666">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=h31z2uhBPigjGoLQYEi9zAnAItFRDVlvPc03CsZlBM_Ux5MnRV0yBxYg7IfWnpTpTUGK2xUZl1tmjdrQsytYfkLfaX6U-BR0c_M_q4yo5Ye1zBs84yi5YwldDYtttpP2l5SiaMdALCQlwOjUMqXzRMiQ7SRrXcH_ZSs8l5CymW_Gw4xi2cnk_hzEVcK4XEGHL19Z3FJLeRznfA5jJaDg3l2JlDME2Q0bFIzT7j-6eJP_8qiJVHUX8Hbc8zW4X-ziI0tZFqOxbl9yJwUry0xsCPI8EwWJ56d2Tua_Xc19epYnqd1MjKZvj8oUJ2cJv7uKriY2Wo2NJVqzoRxNyGx4ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=h31z2uhBPigjGoLQYEi9zAnAItFRDVlvPc03CsZlBM_Ux5MnRV0yBxYg7IfWnpTpTUGK2xUZl1tmjdrQsytYfkLfaX6U-BR0c_M_q4yo5Ye1zBs84yi5YwldDYtttpP2l5SiaMdALCQlwOjUMqXzRMiQ7SRrXcH_ZSs8l5CymW_Gw4xi2cnk_hzEVcK4XEGHL19Z3FJLeRznfA5jJaDg3l2JlDME2Q0bFIzT7j-6eJP_8qiJVHUX8Hbc8zW4X-ziI0tZFqOxbl9yJwUry0xsCPI8EwWJ56d2Tua_Xc19epYnqd1MjKZvj8oUJ2cJv7uKriY2Wo2NJVqzoRxNyGx4ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔵
خاطره قایدی از اولین بازی در استقلال: جمله‌ای که بعد چند سال هنوز از ذهن قایدی پاک نشده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/101666" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101665">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=kJvFWe3mZCGG68cTqHQ2uFqZMqDQ37LZDHlek1YO5aqW2nrQdKW9Ww7_BpkQAJbJEJlE6Si2sp0ThWHFVSW20p8U3jNCofIR58XL9jX1ISgd_kAvIMpikuw8aUsE5WQnCFcrf9wxawysz5HSLC55q5qyP1VZO_VwP89vwRNfJSjbljm-wTJUpTi7EfdVhfS-Pb9-umSImbl2CUEBobmRgBF4maR5mM5AwsWNvPuAtFvj1WyIzKxC-4B0bnwiqYAR4PI-yfbHiBWF3mOYOLHE3Xa-llRHssXiymloOUv-gmT7rY3s_DSbNRU2iDEBWKT1KHZSXvJW3lm9BjcHAYpyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=kJvFWe3mZCGG68cTqHQ2uFqZMqDQ37LZDHlek1YO5aqW2nrQdKW9Ww7_BpkQAJbJEJlE6Si2sp0ThWHFVSW20p8U3jNCofIR58XL9jX1ISgd_kAvIMpikuw8aUsE5WQnCFcrf9wxawysz5HSLC55q5qyP1VZO_VwP89vwRNfJSjbljm-wTJUpTi7EfdVhfS-Pb9-umSImbl2CUEBobmRgBF4maR5mM5AwsWNvPuAtFvj1WyIzKxC-4B0bnwiqYAR4PI-yfbHiBWF3mOYOLHE3Xa-llRHssXiymloOUv-gmT7rY3s_DSbNRU2iDEBWKT1KHZSXvJW3lm9BjcHAYpyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های چندی‌پیش مهدی‌مهدوی‌کیا اسطوره فوتبال ایران درباره تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/101665" target="_blank">📅 17:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101664">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PB6aURjh67VKJhAhNBy9vyaTrFb3BVsUtIe9XkvHlJ1FyUvXKiR-s6qgBYIqRj9OUkl6JcTgd0vPtTYadAeuvKC4Akg-lNny8TiRMkkTOlWmKubcg3thbQdGCSiZrNCDNuiM5F1IgQM1IKe61rE2Hkbkh3I2lIkCw7M9U9X4QirgVQFyOTdl0yaWHyzxwiuomxtGvI29Ndyd_uITtmrsXU4daVd4Yz-3f_WuDlrZ2oDRToXzWudkZ0LaYMDDbKcM2XWEOKpgICko6Mj93D6mj2atqceE6L4gxSWsWxXJK8RSrGhLuNoRCVcq_itl56qHrdyamqq25IxufwSw-s8ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گارناچو رسماً به صورت قرضی با بند خرید اجباری به استون ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101664" target="_blank">📅 17:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101663">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUoWVDp1wJ2xdYE1idcnFrBSYzyEvdEL9EQu7JwCxwlyc93YpfbSRPtCFQZ70296OALQB2uBRAI0mDqsP0y-YG-2Gz9lLoKjHryfzLqhCp9RykDMNmt8cE9eLY_sCcdCl1g--XcBrMaVEI-cIk1OK0L4BNqDCx0U_ICMi3Wmo56XNuOPwgj6A1ciYD_eDQO6LjMFIiUjw3xPLaLwGMMaBNakmSMW8i5Rij8pGnh2d1jOOVgw4ARM1azTAruqp4qJzNPi38kscIA-2B0Bw1jXveEW99c8SNv2ZAFVO7678OnjH8tWri22CLFrN38O8t2mLKjwMOdpAHLRwhNvdR9mDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
آمار ۶ مهاجم برتر این‌فصل اروپا:
🇫🇷
دمبله ۲۶ گل‌ و ۱۴ پاس‌گل
🇩🇪
هری‌کین ۷۳ گل و ۸ پاس‌گل
🇪🇸
یامال ۲۵ گل‌ و ۲۰ پاس‌گل
🇩🇪
اولیسه ۲۷ گل‌ و ۳۴ پاس‌گل
🇪🇸
امباپه ۵۶ گل‌ و ۱۳ پاس‌گل ‌
🇫🇷
کوارتسخلیا ۲۳ گل‌و ۱۰پاس‌گل‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101663" target="_blank">📅 17:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101662">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=UrS997TzuZJOYvpAJypwo2CjCsqREHKG1OO6Ho-mJ6zlE-b8FykqPNlCqRGzJPC5F9zLYxzc3LlvbsbBtHJa1mi817NmFSHs9pjUFmhp3BshXaAoIr4SMZL00GC0DbmG-zeIubRHQZKm1wiFOEen1Z9EacZlE5DmSsj4-_2dAy-em0wW0pSbE_oOwLUISPXOSRwA7fl36XXf7LfZcP3dDubNXnQRqby_uaLuU69HQd5__cME94MSXtlvhSIv0KOLhdAoEw2n7ae2PO4nQrAdqQKWbSIelrysuY8ZvIV3ONiEzMaIwOdKdkcO7uT0zR5jYmrTo86Su0CEc21uvDvrVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=UrS997TzuZJOYvpAJypwo2CjCsqREHKG1OO6Ho-mJ6zlE-b8FykqPNlCqRGzJPC5F9zLYxzc3LlvbsbBtHJa1mi817NmFSHs9pjUFmhp3BshXaAoIr4SMZL00GC0DbmG-zeIubRHQZKm1wiFOEen1Z9EacZlE5DmSsj4-_2dAy-em0wW0pSbE_oOwLUISPXOSRwA7fl36XXf7LfZcP3dDubNXnQRqby_uaLuU69HQd5__cME94MSXtlvhSIv0KOLhdAoEw2n7ae2PO4nQrAdqQKWbSIelrysuY8ZvIV3ONiEzMaIwOdKdkcO7uT0zR5jYmrTo86Su0CEc21uvDvrVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمایت سید جلال و قیاسی از علی دایی و کنایه‌شان به بیرانوند: بعضی‌ها اصلا نمیدونن احترام چیه، هیچی دیگه سَر جاش نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/101662" target="_blank">📅 16:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101661">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=DSE3HdPOFMH0eypkvXK3igm_Wvs1UUa43lnv464WxEMPIsQaODGRxcrMKR2H27gEmQEiyPiQN_zZkwN2rYQleRWxWjU1a3dMI3mgrFy44itNXRjM_2IuNV7dDaX8EURXVH9im8yUnwLQACZ8Xd7hGUC9mTybEUtg5DuCGmHfGVeXyN3I1FRZxpahDl6KwOT3rMQzwoKjeuLNv2kK4ZSt6D2qRyX9lYVWHl1mOSdyCtk8_F7gqzzH_Cv95cBYvWwOWZt5YgT0zY_X72EVN5dEU-TWfYIEfyevX9WqoX381qjqNSOjseshBKWQCjbDY1i7m9FFna4gayYLM1Pq3GpNPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=DSE3HdPOFMH0eypkvXK3igm_Wvs1UUa43lnv464WxEMPIsQaODGRxcrMKR2H27gEmQEiyPiQN_zZkwN2rYQleRWxWjU1a3dMI3mgrFy44itNXRjM_2IuNV7dDaX8EURXVH9im8yUnwLQACZ8Xd7hGUC9mTybEUtg5DuCGmHfGVeXyN3I1FRZxpahDl6KwOT3rMQzwoKjeuLNv2kK4ZSt6D2qRyX9lYVWHl1mOSdyCtk8_F7gqzzH_Cv95cBYvWwOWZt5YgT0zY_X72EVN5dEU-TWfYIEfyevX9WqoX381qjqNSOjseshBKWQCjbDY1i7m9FFna4gayYLM1Pq3GpNPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⛔️
نگرش متفاوت دو سرمربی؛ یکی شکست را پذیرفته و با قبول واقعیت به فکر آینده‌ست؛ دیگری زمین و زمان را بابت عدم صعود از گروه در جام‌جهانی ۴٨ تیمی مقصر می‌داند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101661" target="_blank">📅 16:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101660">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=McoEZ5_BQRDembH1ZNyXeV5lEngGZp1x5N2B1-YYGYMudDA2qLjlEW28lnYFScAZ1DooPgcsb_nr2F22yDoYW3LqTmLTdFiCmpSbWCHxbSf0PAiAalVcsqj92FoNLOVZ-LRo6DOEpKq8co2FIloUqHA1Vj-viUQBpUVJWF3LEar3aMjPgH4uBTdBUx8vPddqpkz10U_rTlFCnQaPBMsSxCkK7CR8LCfnJOf_8RdHhECrCfL8lxtWnIqBHC3rtWneQOizXi-kCIr7e0HxH7Yxuuh3g1JYp0fCa7PoZN8oqrB39rrbTIqKTdAWuxoymmxz-T5ZfqtatYlibzznQjvzKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=McoEZ5_BQRDembH1ZNyXeV5lEngGZp1x5N2B1-YYGYMudDA2qLjlEW28lnYFScAZ1DooPgcsb_nr2F22yDoYW3LqTmLTdFiCmpSbWCHxbSf0PAiAalVcsqj92FoNLOVZ-LRo6DOEpKq8co2FIloUqHA1Vj-viUQBpUVJWF3LEar3aMjPgH4uBTdBUx8vPddqpkz10U_rTlFCnQaPBMsSxCkK7CR8LCfnJOf_8RdHhECrCfL8lxtWnIqBHC3rtWneQOizXi-kCIr7e0HxH7Yxuuh3g1JYp0fCa7PoZN8oqrB39rrbTIqKTdAWuxoymmxz-T5ZfqtatYlibzznQjvzKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مهدی‌قایدی: حسرت خیلی زیادی دارم که چرا بهم در جام‌جهانی بازی نرسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101660" target="_blank">📅 16:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101659">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101659" target="_blank">📅 15:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101658">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=pDg6-wT3h_hqXaXduX-EgTvruowFfNu7IJVbklCPhendsL4OktX6XRBIWscmXMvNP2o4eEk9Hvs21ST-lO-K2OLazh_viNnGPxZ2ZHmtd2QzYy1snKRoJVMw0k7OYNTXerQ8wuPQcwO_oncOJZ3stLlzfUU6_rlooSSpMjhsWGe12F72hD9XAUocgrmUbuDJvaUx0vBOchMfQPqCWqjALf-J6Y5mBYxUEPwfzTGVio7y4Hx78BWx9K3u49WbOAT1xdc3p0RzIyjiKGmWU0D-wb5sI-Z53kksZPU6_TJYqxKZERay3265Kxo2jQOsYcMKoovig7t63I3CB-Xf9tIwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=pDg6-wT3h_hqXaXduX-EgTvruowFfNu7IJVbklCPhendsL4OktX6XRBIWscmXMvNP2o4eEk9Hvs21ST-lO-K2OLazh_viNnGPxZ2ZHmtd2QzYy1snKRoJVMw0k7OYNTXerQ8wuPQcwO_oncOJZ3stLlzfUU6_rlooSSpMjhsWGe12F72hD9XAUocgrmUbuDJvaUx0vBOchMfQPqCWqjALf-J6Y5mBYxUEPwfzTGVio7y4Hx78BWx9K3u49WbOAT1xdc3p0RzIyjiKGmWU0D-wb5sI-Z53kksZPU6_TJYqxKZERay3265Kxo2jQOsYcMKoovig7t63I3CB-Xf9tIwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجراى مريم اميرجلالى و حميد لولايى در بين ٢ نيمه جام جهانی‌سمه خالص
🤣
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101658" target="_blank">📅 15:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101657">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔥
▶️
چند سوپرسیو دروازه‌بان در فصول‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101657" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101656">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❗️
علی‌قلی‌زاده: امیر‌ عابدزاده استعداد بی‌نظیری در نوشتن و رپ داره؛ از او خیلی چیزها یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101656" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101655">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEXta4jOvFS0jlo8G5qtenvAOSz1qbROLwkgaHVUi9u_Y5fnlOzhZt63E0x_MNUgxnaH1OI9HcYgS8k_rbYdQXapwCi1pPYzh0qqBnTxxanODtl6tl_Fc0GXuR97k4WOGF4MW_CHy2yT1ithKLnItzJLP5Nu5mpypUopM8E6NXoiB6-a6BKXJDphBwa1q1Q6qpua3zjEq0Jc22qeBSCVW3-bUyvtNAkDBwNj0VFHRluGR6OVoeBfKGxzT85zrfxhK-3BhRPQAotr2Cu80t0mc6-mvWiIQKq5z1TvP7ZZb23gAEytyUff0D8gs2NMBxmmOwav47yWZWPx6B3_8xqeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت گاوی زیر پست یامال
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101655" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101654">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ینی چه بلایی سر اون تیم پرانگیزه اومده بود؟! ببینید قبل از بازی با فرانسه همگی بمب انرژی و انگیزه بودن ولی تو فینال امسال انگار همگی از مراسم ختم اومده بودن.
بازیکنان تیم آرژانتین تو بازی انگلیس داشتن به معنای واقعی کلمه میجنگیدن و بعد از بازی مثل دیوونه ها جشن گرفتن اما یهو نمیدونم چی شده بود که اونا از لحظه شروع فینال هیچ تلاشی برای بردن نکردن!
بحث تئوری توطئه نیست و هیچ خدشه ای به قهرمانی شایسته اسپانیا وارد نمیکنم اما مطمئنم تو رختکن یه خبر بد یا یه اتفاق ناگوار برای آرژانتین افتاده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101654" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101653">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=GKgzqka4zAmt4kQ2f2VkNIg-uqpUvgWn_yyNWzzW1o0ngjz_yJRLXIPMEO9U2e5j_w75dFAVCfc5NaMaiEryeM25pT3jsGeYca3DQ5-tUjCdMlw-MLALC02ISWI9tHi0NyiGrIh9pLiVOjcvhwMrJKe_W9uO9vYN1LPDgP8NGft3QMqFEfwb0JScLM1xGCCalry-_BVZgMdJVXThTnbZZp2ybotQM2QLAzTBi3CBEQntju-b9f9NlJs6R5tNmJxJaK5WGygOgssVTzjf2w5lOyp8SBSoVanpk3vNQU60S-piqLWoYR18tNqn_QKptu3U8_1WJmLAsBR-uat3HgndLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=GKgzqka4zAmt4kQ2f2VkNIg-uqpUvgWn_yyNWzzW1o0ngjz_yJRLXIPMEO9U2e5j_w75dFAVCfc5NaMaiEryeM25pT3jsGeYca3DQ5-tUjCdMlw-MLALC02ISWI9tHi0NyiGrIh9pLiVOjcvhwMrJKe_W9uO9vYN1LPDgP8NGft3QMqFEfwb0JScLM1xGCCalry-_BVZgMdJVXThTnbZZp2ybotQM2QLAzTBi3CBEQntju-b9f9NlJs6R5tNmJxJaK5WGygOgssVTzjf2w5lOyp8SBSoVanpk3vNQU60S-piqLWoYR18tNqn_QKptu3U8_1WJmLAsBR-uat3HgndLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رضا جاودانی در جواب نگرانی عادل فردوسی‌پور، به جای فکر کردن به خودش، با آرامش گفت: «بذار بیکار بشم... مهم نیست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101653" target="_blank">📅 14:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101652">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=sICydQOO5cVaECNUgbqIj7ncQt7112iwEnVaJwEgV638kvPwf4sK3kpbrq-kohukodmjjTJHrOvQ3UJG1ZE-_ca8IsqoaScz-pNA56E2w1wZBl20E_-6J1wQ-unvv-JhBPYqYNw71JgZzYAXRGeBHrBvJrWkb_JS0cENCst-x0HkisT1hqJy4_3mmQfx_x-wxiYPpEIA_KGa3E8cL1iAOn5rE-GZCP0uasBHC8cxzLofA1K0ir4yXjfO_w9Axpj8hLA7LQQ3Toh3QfVB_9MCZRpDPvghCCS8EccY_K26tJNG_bQSMRwXNnIknoHqgG11JPaYPCRTzd11qp8A6K7cTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=sICydQOO5cVaECNUgbqIj7ncQt7112iwEnVaJwEgV638kvPwf4sK3kpbrq-kohukodmjjTJHrOvQ3UJG1ZE-_ca8IsqoaScz-pNA56E2w1wZBl20E_-6J1wQ-unvv-JhBPYqYNw71JgZzYAXRGeBHrBvJrWkb_JS0cENCst-x0HkisT1hqJy4_3mmQfx_x-wxiYPpEIA_KGa3E8cL1iAOn5rE-GZCP0uasBHC8cxzLofA1K0ir4yXjfO_w9Axpj8hLA7LQQ3Toh3QfVB_9MCZRpDPvghCCS8EccY_K26tJNG_bQSMRwXNnIknoHqgG11JPaYPCRTzd11qp8A6K7cTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
شیروانی، مافیا ایرانی فوتبال ایتالیا: به اینزاگی گفتم طارمی را جذب کن، اما طارمی در اینتر جواب نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101652" target="_blank">📅 14:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101651">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxg6-eUGn7x1rflQlMmMP5_EvvWdqBLfhpKpf91FB9bXzmJhR0O0ny8n6CfJYMdC4ejeazW5-d2srtAOqfCrYZGGYF2F19-ifY0VakzHuD5dIouCmuSY8SAAvnbmPpGD7qtOmkHM2Ck0fUJRrWP9gHehuoo0jg3htxLMAZeewPZEGAlWTKwqNyWw0RB-aP8xpwoxmqTOih4HgqsRMTlC8eeQQDMDkL1s-fz7-vjvDo_SyMqoerT05fJa49_YDJzkHZ_2b1VjunELmpOX_0-ZQsdPcqZxyXW2pTeHGn_M2AYkfB-BpT7_iea94BjgJSCn1pG23CvpqkI2GgtisRRVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101651" target="_blank">📅 14:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101650">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=RHLffNks4NSwJq8Uh08sLfREwTYdNZ9YL9rK7Yabqx26ns-4ENsnQXSdp9nmoGQYaouv7La-ywTmx-hXLtc9TLX2Lzick_7183tR5iavC3jQzCgQiW1sH4wQIp3396xKRWOgE6o53AL6ACUwHMmkA0--L6tP7XUZP5G0kzIkQKODNbUUyJS93IgFJvDFFY5Jwl1mt8AEM07GPSvRmBZ7qiVaq9vNdnRI-ETiQmoSD-Dc_8dAjT99gmQfCDisrUc7d6e9oczsnCArF8AztX9Q4M4Y2ZOVBzIh_YcUKHv4YzLUA8hA8l6oCaUW7T2Ygf3y-iik6b9SDiJqzDwQ0ScePw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=RHLffNks4NSwJq8Uh08sLfREwTYdNZ9YL9rK7Yabqx26ns-4ENsnQXSdp9nmoGQYaouv7La-ywTmx-hXLtc9TLX2Lzick_7183tR5iavC3jQzCgQiW1sH4wQIp3396xKRWOgE6o53AL6ACUwHMmkA0--L6tP7XUZP5G0kzIkQKODNbUUyJS93IgFJvDFFY5Jwl1mt8AEM07GPSvRmBZ7qiVaq9vNdnRI-ETiQmoSD-Dc_8dAjT99gmQfCDisrUc7d6e9oczsnCArF8AztX9Q4M4Y2ZOVBzIh_YcUKHv4YzLUA8hA8l6oCaUW7T2Ygf3y-iik6b9SDiJqzDwQ0ScePw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد شیروانی از اعضای ایرانی مافیای فوتبال ایتالیا: با دیگو مارادونا رفیق صمیمی بودم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101650" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101649">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upBZPL2xfmD_clXboUDnPXVc3cV_AlrezYImCHaPn7D6_Ck39dYHj7bgETF4e0Eijctsuv5nC6qQf5v0nyjVt91_ViKPQrdQv5MsX7ArZAt0ahPs7SfNqc61g4ydiyCMLyv5GyICeVX5wl7rKhtBha4NABZujQyI0zxkDqyRDxCVkpL32x4XrKDIlmPJQwOYij-3CiieyM4rtvSq9AMB476-m0xgQMo2eJzsE-uxT3wAuabRGF_T7erj-dTe-0DcBiTCzCMpcMY-tY4yXWf1H0Hi9DmWaWNQ3bJcLPsGH7U1Ahe5nIsqMFgjxmYL6dBoTERbhUF4c1dJCHP1uK8gpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
⚽️
#فوووووری
از مارکا: انریکه در روزهای اخیر با فران‌تورس تماس گرفته و پروژه آینده تیمش با حضور این بازیکن رو توضیح داده. قراره تورس نظر نهایی خودش رو بزودی اعلام کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101649" target="_blank">📅 13:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101648">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=oDVqJ3RRcte5oFMyzlb4BeTgbZLd1BQx9dB3t9YHOS-l2-7ssTp-72DxgMXpXyXHT5p-RubXsGo12PaxXwqC_ufAap9-OZ--_GsLaFNmEZ_pcCHI9lB4AHl9Tw8sLz0SQwYxhYbSkYy83t1iaiXfFeUSK3vNTXfR7QokvCR9DbD-CcMvxRKOHAntlTmWVT1KMrkHihoRL-mzni8hYqaqO-6FQa2q6Lj7D90R6pjHm8Bmr0GEVoGtx3Dac3oC0940l-_DFUIGXDgW7-WsnqugdOwulswahSZJNXp5v_TT_oRzeERqMQuOGNfUN9yTP8jXVUMZkIe4F7CpnQ5oAuVwPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=oDVqJ3RRcte5oFMyzlb4BeTgbZLd1BQx9dB3t9YHOS-l2-7ssTp-72DxgMXpXyXHT5p-RubXsGo12PaxXwqC_ufAap9-OZ--_GsLaFNmEZ_pcCHI9lB4AHl9Tw8sLz0SQwYxhYbSkYy83t1iaiXfFeUSK3vNTXfR7QokvCR9DbD-CcMvxRKOHAntlTmWVT1KMrkHihoRL-mzni8hYqaqO-6FQa2q6Lj7D90R6pjHm8Bmr0GEVoGtx3Dac3oC0940l-_DFUIGXDgW7-WsnqugdOwulswahSZJNXp5v_TT_oRzeERqMQuOGNfUN9yTP8jXVUMZkIe4F7CpnQ5oAuVwPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیدجلال‌حسینی: بدترین خاطره دوران فوتبالم بازی معروف با اولسان‌هیوندای کره‌جنوبی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101648" target="_blank">📅 13:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101647">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=CAtDMgG3bK66nW1k08a-C-NBFL2614JAk1MqQaDkzzRV-SDG0NEZypTrjb9imHaBRzAvm0ty3F4Fz79S6eSE3uXrCLlyKQiwFlg6xoDTLm-DBEkSezVExMquAAJTaf_shQI1yQLYNJnxDasf7pnELm_PJ1KmGjJL6NrymcENpEIzQTdoazFUcV3Zr1dxBSBFMF29SGx4WvnwVceAUttFOqfeXdHSVwjCcYI2QVgI7LyMFcmTcIzqy7kIaC6rlpvBNWMvO10jm0IPs2xAII8oB8Asv-OM7ujTeLPFX3jrE6KVB_TfdVdvKDUXL0P50Z1Oa5YIUzpYh0YWG9Ydo5zatQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=CAtDMgG3bK66nW1k08a-C-NBFL2614JAk1MqQaDkzzRV-SDG0NEZypTrjb9imHaBRzAvm0ty3F4Fz79S6eSE3uXrCLlyKQiwFlg6xoDTLm-DBEkSezVExMquAAJTaf_shQI1yQLYNJnxDasf7pnELm_PJ1KmGjJL6NrymcENpEIzQTdoazFUcV3Zr1dxBSBFMF29SGx4WvnwVceAUttFOqfeXdHSVwjCcYI2QVgI7LyMFcmTcIzqy7kIaC6rlpvBNWMvO10jm0IPs2xAII8oB8Asv-OM7ujTeLPFX3jrE6KVB_TfdVdvKDUXL0P50Z1Oa5YIUzpYh0YWG9Ydo5zatQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101647" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101646">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=U51ZKINFePFwrQVHwmsUxQAvYk2uTU1KiBPJxIjbS9ByDVRMvbATbTCLEbkY1FTp_rSxVM7IB2qgojkKgI5wK8tuAqQIGqSIqtv15F8K6ErW5tOwdAC2uJgbIjhql3FK6a5oyvELOp6OM76G4UpneNFufF39qrjbXJZ-fjSNTOxIKdnyJ-XsImV051cs2_aRNuXLzxLWJuzsKsNzwM7isWOHlCNGiCl_p5RSS9ZSx5p43QDvlOFzlz8g354hYhIMjw4Lpe2zFm3um-IU00NyDGU3fBKkyutN6ksA7clBYhkIFpSAZXSoom3fPqspOHKP5PkggB5tIsAp8zjVbVTQtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=U51ZKINFePFwrQVHwmsUxQAvYk2uTU1KiBPJxIjbS9ByDVRMvbATbTCLEbkY1FTp_rSxVM7IB2qgojkKgI5wK8tuAqQIGqSIqtv15F8K6ErW5tOwdAC2uJgbIjhql3FK6a5oyvELOp6OM76G4UpneNFufF39qrjbXJZ-fjSNTOxIKdnyJ-XsImV051cs2_aRNuXLzxLWJuzsKsNzwM7isWOHlCNGiCl_p5RSS9ZSx5p43QDvlOFzlz8g354hYhIMjw4Lpe2zFm3um-IU00NyDGU3fBKkyutN6ksA7clBYhkIFpSAZXSoom3fPqspOHKP5PkggB5tIsAp8zjVbVTQtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یادی‌کنیم از دوران درخشان سادیو‌مانه سنگالی در ایام حضورش در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101646" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101645">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz1CGS4okc5UYu7is-lnn4GcmYksVPLa1AnUWYouh542SlrNWXxdH02GZIV2b5341iZrruGn09kzJuWNZpuACFP5LC-9WIftezFZzy4G4cJVaWcyUmlc4NjOKPCzTGBsk2d-_lMgYUzOJcCnBS_L3a64DTeVBYe0YrvRpqYQR838wyCL4YiPUQzea2HzKFTxURAUAZkVoaszaoY5PimJbcNXc4cZLsm4TfMFKF63UGjYz7lNV7tr7Bv4BlrNKRrru2-jA5SsGNp85CgDMNFMR0A58qVM6sEemvxIJ94PxYIeJX6SitkuW9ItxE8f_PS-1NPaZVbCDtIUluIGD3Ug1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101645" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101644">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBtRQo9OEdYxmG1gDsfBVeiYKOBp7Neg1uvPNV5e4nQIO_pcMoWOVDdVPyhdt5VAqUdq5Xx2cP1LylpHgpUpjYd2SdEqg9gRw5orkgK1DPL5wdS-PQDT993CVlJwl3wiAw7THbZr4NLg-5cXpqcBXXs_Z2eOKJ3EvOgbpwGMVidgns3vgrH8L7ZAWtABaDsxJrlluSWgQg1Oc92E5TPzn-kuD7eSG50sRztUnjZQJ9LO3j9VBX5Ogp8QJ3eo0fs8cpwny6bA7QmUbY3s36rVIcnQMjcaFaP-I_kFdTPpiz9pROk3hcYwQrN140uwy4hbxyM2xn-_8mlzQDkG9B0Zvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101644" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101643">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXLyt0tUn4ZPLEQgm3llE6JYnGmYUla3mlwYB0PvCwqSiqTqZmoIRmg_1-2Lfxg9FkcjyGYfV1lOIguDDKX-LL5Sh-rkRvQDHpI4GPtHoqaTyPP906SlEO6ODosaq58qOBY60vYsarRE3YHTz59sw5RFu5C7ZSc8J2QXUEVw2j5eudaQRtvg-GLkJrAUPPNuUuYUavJWrFQXQm9HORf7XN9qm4n_gX3OZbNQ-N3XOFNiTDHrH9z0pFx3vw8qZw3BbG_2yl_G16IW6DKqh5jfP1psMOltbSvBFw0aDBgjvqKIFThtW87KLEeu56vWWKLIo-QQ7HVVLjD2NqdZFn62hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101643" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101642">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyKKgbv44bgwmvjAneB6_oUp2Rs2GWm2iesLwuWBdJgZcQL6PmQQxk9zgFbBDOsW6EB9bkRcDytS5iZwW61t9xOI-HO8y12QEeBhgZTnPg_z2UZmb6WL6TJ5dkwR2A2y1HrIh7LpEwMGeali0cv6MPiUy_coSnnh9hpX-UHXOaMWDybsz_thVHcaeUtJ2hQseSByRUIF4FSRmX7-7on-0VGvT9sQ2cx96zzbaLLVjmw8XH3ujAy_a4u_bjmoVRDS8LkFu3eb4HIXjFZ5mJVt-B5twb5qDBq5swO5LUez-RBdcJ6HwG9D9xhcMnLku_9ntKde_pXCoxFtlVtf34uWXBXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyKKgbv44bgwmvjAneB6_oUp2Rs2GWm2iesLwuWBdJgZcQL6PmQQxk9zgFbBDOsW6EB9bkRcDytS5iZwW61t9xOI-HO8y12QEeBhgZTnPg_z2UZmb6WL6TJ5dkwR2A2y1HrIh7LpEwMGeali0cv6MPiUy_coSnnh9hpX-UHXOaMWDybsz_thVHcaeUtJ2hQseSByRUIF4FSRmX7-7on-0VGvT9sQ2cx96zzbaLLVjmw8XH3ujAy_a4u_bjmoVRDS8LkFu3eb4HIXjFZ5mJVt-B5twb5qDBq5swO5LUez-RBdcJ6HwG9D9xhcMnLku_9ntKde_pXCoxFtlVtf34uWXBXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
هنر استپ‌ و گلزنی از برخی ستارگان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101642" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101641">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNx_OFNMZU8kMSl1Za8n4mCqcsb2k9pOXuRXUMXWFyWSiuYQbwDAsfzopaqxd6l48LbcJ8z13srDXVAmr2tbjSKh3616BjeGrfCP5ieHlONtkmOS9160mYZwMvvF4Z2oIfyB22bdcFcSOOeSj_hJ9AsTCWQgri8XdR_6gUvXUovVYlOCSlW907mXfUGFewKAZBvgrCkBcOr-pGPL0TUuQ69QSDGqmBdT4vywqrV4jfEEORMSFifvD9IbTI3BPPw6pYQ-HaW5_9jdUViCMGmyOvLoY9hjwp-OcD1XApBfmYaIqsZrKtnDb_EAHjpZTVcGZv60yM7ihFHem5uWqleU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
باشگاه بارسلونا در صورت عدم جذب آلوارز، داروین نونیز مهاجم الهلال را زیر نظر دارد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101641" target="_blank">📅 12:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101640">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOpv4Keaig7FyZf6KOhuQGFpVdxWBhxKWdbLsiOuNl-qylPE72iB7joryNsAK_ihGDYFziXydPzn3r0RBSDSAs1H4LYnA_i7TjD0jZZpWsW-gq5EKNiqS1vGh2srOpzTJ143KNOYHVQutkSzOv_Pzvzwin4rRUvzpPXKIiw1SItKSY7lRH8N8P4U7RUHA8wcg9slEjjbsRX70WtcW5SjzqkeCuI61cGQPDgHJZSCrqZOXbe0DSJLLqZrWWx9EqZBcCbqfHw0Zd-1NdEvkslu5qOdURgvoRZFYihCaEQ6shvMoaWH_wPnKLGACbMrbUViNbn6vas9zdU8JtzL70pclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101640" target="_blank">📅 12:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101639">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=MPSkptROD978aMcMc-uerBYUyYK8avo5vyIh3dWb4iRX079PV_hgBKDmnuxqOT_mvDmuncZDNDKYY8j9TTM05GuYOSfHGgBzpgaLPuAd0KHG9BfoqM5rGjgXrIiJcs0IZmgfGFHpIMzRt3o8Mw3HvLjXZzRgQQZc3JHz8lbOkrHlQ1LpTGcgb6Qn1TW8FoGBn38b9HwJgrs2IiCNqNXC-oNWSNudtMnZ6MfcGGjvpBIuVxUUewj5YKA5xQGzQLeMNnUjhzwvWco23QnyUfBERtHamnL1wDm16rKP-KpHo3aRL2duYrCM8lZMg5lfwIfoGEgRVuLfvS5F4B4cE4AKrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=MPSkptROD978aMcMc-uerBYUyYK8avo5vyIh3dWb4iRX079PV_hgBKDmnuxqOT_mvDmuncZDNDKYY8j9TTM05GuYOSfHGgBzpgaLPuAd0KHG9BfoqM5rGjgXrIiJcs0IZmgfGFHpIMzRt3o8Mw3HvLjXZzRgQQZc3JHz8lbOkrHlQ1LpTGcgb6Qn1TW8FoGBn38b9HwJgrs2IiCNqNXC-oNWSNudtMnZ6MfcGGjvpBIuVxUUewj5YKA5xQGzQLeMNnUjhzwvWco23QnyUfBERtHamnL1wDm16rKP-KpHo3aRL2duYrCM8lZMg5lfwIfoGEgRVuLfvS5F4B4cE4AKrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سید جلال حسینی: اشتباه کردم همه زندگیم رو برای فوتبال گذاشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101639" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101638">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcOeZRsfSPQ7CARpj5LT2ONZWjOceN3r4CoBpDYUJxcDXqTo07R_m1uH2NMl-RcmMTZqRTiZlHoMVMePERYDhssQUl-NLlsLvbx84PpNLputDIc1hOp8XC6PE_5_7TSMuuFDleWpOMwZrOcbXC0FEGoiXLENvUgo2JzL7BMN-dttGqsXr3nAnwgxTUxcodvuJQeopR577u9p-Um45hFggy3Gx4dP8HP1ik1J7jSKKPiPevEepFYyh6QhDTYdX4Qu2oGhg7P2jWnj5EqlsYEY0eclZ2VfX89_ZElF4vRW-_M4qRnqAYxgHsvgXgxaJm-sRSe-omQOgsrFA7nO1Gmamg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📰
بیلد‌آلمان: آرسنال حاضر است برای جذب دیامانده ستاره ساحل‌عاج مبلغ ۱۰۰ میلیون یورو پرداخت کند اما این بازیکن خواستار حضور در پاری‌سن‌ژرمن شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101638" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101637">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
▶️
عادل و جاودانی؛ دو مجری، دهه‌ها داستان!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101637" target="_blank">📅 12:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101636">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ5hUl9cjlapW0Tw33AvrPHk37Jg_b8f9OLqAMMxT_mcBOoTKlbwO3wHCmHOU5Qchc1Y6va1DOOp-FrFaO_XaIlDSGr4bBl3YM-3MjTzoEWiCw9L7HVXbFRvf5Ds8Ayj-scBMmEvRN7iHxyYceF3eTPN4XGd3XhX6nBtuT4hdoaOe3JaGVwb1K-rKmWrg_4VEVqeZKEZ-aKpbGu05HdBYpyLeTqNSAdeeA5BX_0MFW3iSq66Uq8hpSHh7i07FDzlZbAuhnlogpEfVLclxgCMOXaeaKtn2p0qCBik0ky-iMwilNy78ndtrlDyokeaXA-WSGt5Jrjj0Vdmh8yOVsjlWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه پس از تعطیلاتش باید به دنبال خانه جدیدی در مونیخ باشد. او از سپتامبر ۲۰۲۴ ویلای ژروم بواتنگ در گرونوالد را اجاره کرده. بواتنگ اکنون می‌خواهد ملک لوکس خود را بفروشد، بنابراین اولیسه باید تا پایان ماه اوت از آنجا نقل مکان کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101636" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101632">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXU7XGPmEMBMBXm1fAzEvXVFF0JKmJ4hI3xAGzgl-K0-R-XIGmzERDNBqK-zNJAWK1SA6gQuFdyjP5Tlxe19f6HTDRjgZnMzWmlQU-F0UrqXP3ozkiCir7Uo435U26NiVI1pIRSj0FpHwZQmXW0elgftOFdOpukw4DPxZkd2PytmcL6RuJpbvKT3TbDar-nwa0XpsT7tIcFGI9abwlutm6KlJA0xhU0angMsyFFPEyezDqhAMzyqokpwG01oGRrX0_6bkHSYGuw5dOnjVCiMqFEKywUJ6N6NbuviSki1r33QSwJf_iGKvwokTdoExYIUfG-Va_jubRy4clLmw3AaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTaGOLHjgXX_0lXCrlHCsf21ab_25NFWeo0ouSUP7C5Ip5kSwSAqlyBQnQXyheAHWbKziGO9dCMFCweQvQSA8rmsSeaYy6kOqyR6I8fZh9Bhq6S_GjtktbwfM5IURrR37wLZz0z_ORZunKXsKOsvck5aUYyMZ5UrZdcIdhYIoHm675jB9bpdSbh0GTJBbN2Ol95quT0-5w3Rz5LY9bo01brPQx3lPTMfK_nFfHH4Dsjb-zk9UjsmuVBMnD3_-9YlVv9hc_1utD5F9uhDwS-2l858hdJsymjCDqxqPSIh3dzqmB057IvhVW2Cx6uFpsdHdYAU5wCIPV17CpX30Q2k4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XawbEeUpB6OaMwBkZjkWJ0dsdKOXDjD7ML7ucd6W0l49aIP02ki8TaOx0Xq8OwdlPQVsD3xplvS91uIvzcOKsSXAOyenl2EXeuolBEnRT2Di8uM0ARv8lp28UtMzJViV3hWf4rcGFp1Y8rV4fi0U0lAEXakIsa7XGMVVyT3u8v-tWJAdgCSn3yx8_nKP2ci84rTYp6uqXZUuFzF6bJ3WH7mlkjn3B7WyOx_9yUFe_v4xj06G04-O2nE6qrvdUK-VX5vqSfdP3hy9HKJRrTYR16AE8rQUVLExAIU7GociyFCv2GW09fWJ5qJ6mENiNgok_-A_Rs6ZjLmulF6EQUc6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsfYidsXUEkrSZbvR168vULiVGb5ZH6wF_b-iIEpy-oxVuFe3s8w0cTTrVg3Nvda814thpvKe_twlPZ2Y0AFfbosIHeA-bHmoc4LEQsHeJLgfrPDt6XapAA5utgtdu0OHlkyW40oyn3gKWpU6WN9qbpaF4J4voaItV9GN0RpJlUZ63d0I3fOlPfSW00tNK-XMu1h5_hkE-1OFDoxqHv3z6ojvC-8yCQopo8WTlkhVFDTmpR-qQ6Qnwm-Hef9ssV8Cd2gEhP9Nc55Gpo67A4Z7ZbpPhdn57vgRYmB5FRo8xg_BhLdOz_3bNjeGmfYIA1rerHOGie2UXUIBPQwryNQqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101632" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101631">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKPHeGTzv3ZzfTqbXNLPaZnPFfsXsFPOR_Zio_pg6qGvev03JoVWFZ1Wzyg0rJwYitjq5IhKpYXXag-lbltrgsSfcwRIN9CjYu3s39WZSS-aZtfoJoYU1uSjGFoA0BLFxaxNQ8CQKzSlgYutQAWb9CrAK8I9u6xj7X5VzBCNTu6Cdn5P9MtI-LfK1u7IlPKbn84BFwpTz994jjALQm0oaITE5WR5-S4eJ1V1C8-ipHZMweHYJFTLFdkpyI9uxHVvE1-3oPMvPsZ4KcTPY5Fvqjnwk1SLuBAVw-XZTmflmV3JqtNNMJ6Pf1iLCtU9IxCSpS_3Pixad0lSaWb0rwnk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
هواداران آرژانتین بعد از شکست مقابل اسپانیا در فینال جام جهانی 2026، یک دادخواست برای تکرار بازی فینال راه‌اندازی کرده‌اند. تا امروز بیش از 61 هزار و 500 نفر این درخواست را امضا کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101631" target="_blank">📅 11:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101630">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-RKHHIMBlBXVGhSZKBOswV5o_LGUVNerR-A1TWdGMq5jU1Qx2nP7p_UATeLTF2vCoV9Vpc9_8JeraWzjUle1HVqA1l97ZcHR5rHumr0CAb6ZpyfUJLT047Ev8VS0nary3-sJwEd9tjSJSOpnalrBEafT6q7_ccHM5M0MK5W4lP51o_m04xTSLIACL21kR7leno3oVx5JXFtqre-sLETZcn2dEc7i0mSiposu9w25JGv1v1BqUlzghFgWwSb-n58uzH-_oSqxW7HTEWIqG_SNBdcaD309E8ecRDi5ucsR1ZPYX5K367xLBXvutUtgM1BjC4GwYqRfhtHOpVC-kQgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
❌
لاگاتزتا: پپ‌گواردیولا پیشنهاد تیم‌ملی ایتالیا برای نشستن روی نیمکت را رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101630" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101629">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=Rr5nCGZcT4kySnjbAIBYVbfezAgExRYmsVgRBfAa7HWoQHRcdmx8wDkt3QJPUc7trKlyXnfpQYLFIkffX8ARyWtDpzfsP1EC8I6wDd6Z7dnwve7__ztoMif7cTe1JtUe0xkM5RfNvEtJ1UHD_gRNtZzhUM5z1fxd_mXg9IsF5T2nOFRwhaWdeR3spGD7NE7LHTunci1oQ0JUcwwDhUBMaAmf0IF1hDx7NdDrSel3fGKKXDFC67XV0CCIp8RADPRkz_ldhlfceBE6b-k4Ubi_S3ddq9uZ3g6DCdk-lr-XXU7aSXLoBv7H3vwADJOTw-u2n7MQqyaabG0Uz95XXHMDmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=Rr5nCGZcT4kySnjbAIBYVbfezAgExRYmsVgRBfAa7HWoQHRcdmx8wDkt3QJPUc7trKlyXnfpQYLFIkffX8ARyWtDpzfsP1EC8I6wDd6Z7dnwve7__ztoMif7cTe1JtUe0xkM5RfNvEtJ1UHD_gRNtZzhUM5z1fxd_mXg9IsF5T2nOFRwhaWdeR3spGD7NE7LHTunci1oQ0JUcwwDhUBMaAmf0IF1hDx7NdDrSel3fGKKXDFC67XV0CCIp8RADPRkz_ldhlfceBE6b-k4Ubi_S3ddq9uZ3g6DCdk-lr-XXU7aSXLoBv7H3vwADJOTw-u2n7MQqyaabG0Uz95XXHMDmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📊
▶️
آنالیز‌بازی رودری ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101629" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101628">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-0oVj83IVVS1GFxDhIVBloB0eNC7cnavKXSrSsjzl-9o2cmqApJNoG6t_Uu3-1Dgq70LXgpHM-ROz6AGjcmFQstUYYoV8VswCdQqKo2BqzpuJ0mmzVQ_RuU29OY7s9Eyuv91Z4gkDgObJBiNcaO3JNFwfDz2m6i3klrurq4gfwpOwXIMQ14j-U3fMSHAj4l_ORuMcyjqFXXLCl-5TsXyH4KwWumR97Q9Ak6kRX4nfb4Ae6gsdQDQf0O4drzvVBoDMlCAaACIeosQJa5MRZgt5pFqtKJzGCX2bCWE1DBVa-jNvQdgfNDBNGo9SUb1ybvKKoM-6lYQIZ-RPS0t-BQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🇦🇷
اسکواد احتمالی آرژانتین در جام‌جهانی بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101628" target="_blank">📅 11:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101627">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzxccrTsYfICBp5Wdic6JfuACpp0ZlCtMJbfKNouPkr9wvYQfksJM39mWh17Gvf3j_ygD8pE0uC3CNXpgKeF2J5rzU41V5iUXUeLX1WXbDhHlowh3G0yTI24CPZXMhBxKIgIU8SrqS3cdhnxWKTgjR6h7_UuTKkClS9ixujwsyEpkCpsMqNsn1ol0pLprvX9PWehEPwJihib9SmtV08c6bU811FeZrHbI1cMs1pVcd_-PqUVZGq0p4wV8vgYRiq8z9sMKOk4bE951gUBI9-JiNTvCoHXVrxJz0OEkK_4yYpq5HQL6e7AEdGo_46FyXWWIxEbmVWttFPDsNqnhhEEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ نیمار بعد حذف برزیل از جام خیلی افسرده بنظر میرسه
- نیمار :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101627" target="_blank">📅 11:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101626">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MebeI-Dlg8dhaV-m4nBDus0Aj50EzhXXe0rHFfYneewvAvzCQu7Q0_WAOdAv_Tj7wKwxNHS2ndLx8DMWjuslc_0qxmwcS-swHbPHeHDzI9p_nncTfMLIMEYrrWKALyovGUljXJbyrWL_6WM5k2Ls2Q6S9KkcrWBhbgKmlI3kQ42HgaCYLJnrdPzr_9ppPH7oNsxeWgzUy7xFfr38cThZyfLUa2QSih9tA8vr1y1VUKZfAne_X3eMI2dS13Rusyw0r01PHwESbX-zuZ1jmFokRy6E3tDmFsm1d8wK5ncEOSGX8LX_9iTkK48Q3nyiendBnY5c4IsTHMdTqFU4fkUwmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101626" target="_blank">📅 11:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101625">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh3SsaAvJ8yNi2bojcU-wEOUcf1lwRFPRBrYvrDnmAdl4oWEePAmWvUkftk61rPny-44lgdKZa0_fDRlEP87M3ds4cHxqjjIyffqhRd_VQDuE67KC-tsXO5k4Aeu3iq9QnAPw9JAEut3f5MnMmRmu-5HWyoraWvFhJp-pKsV6GAja8EiTVRmR6bEcgHyxwg2A4UP6g9rRnuxN-kgyik3pqRROumiKCoaiGtOX-6v6au_LXUmnaOXp38F8R38m9vqjkebUrGpGHgmwqfYvCm1FQL3PJM_DlBWc1wVujbMN9CYCjCDCvRbpbPGUnK8vEG2PzudZA5DMqdbG8QoTgMZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لکیپ: انریکه و پاریس تا 2030 برای تمدید قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101625" target="_blank">📅 10:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101624">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=rBCFG9fDeJBBqd3K4fJCDONV8pz8FNhDzPzpA6vzYnOMtkPSkgwccHVnnhZuy_4YBdloCDTeEPGkzhab-7dw5pvHpNnPaRH6nwz_dIsfWvlEVAJuevgRv_eboSRZLLXB6Q67g_xYAUNSPbWfIseVp5u3r6jqt77OXIEMjBkzzNhnJ2ScS-ultS4k0mvpaAztsbrMu4JoajGs1QMPmAkdIiAums9n2kbZz_6UCQXOw3YjIBP5UE6tQfD9bpFpQGNK_TMyBU9R1us8IIqTD2ZU9VS7rKO_Aw8HhIpqaans2UOayBQ-7dtH_oaE_qByylWi3z8my91opsl56edNXWYmrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=rBCFG9fDeJBBqd3K4fJCDONV8pz8FNhDzPzpA6vzYnOMtkPSkgwccHVnnhZuy_4YBdloCDTeEPGkzhab-7dw5pvHpNnPaRH6nwz_dIsfWvlEVAJuevgRv_eboSRZLLXB6Q67g_xYAUNSPbWfIseVp5u3r6jqt77OXIEMjBkzzNhnJ2ScS-ultS4k0mvpaAztsbrMu4JoajGs1QMPmAkdIiAums9n2kbZz_6UCQXOw3YjIBP5UE6tQfD9bpFpQGNK_TMyBU9R1us8IIqTD2ZU9VS7rKO_Aw8HhIpqaans2UOayBQ-7dtH_oaE_qByylWi3z8my91opsl56edNXWYmrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سید جلال: حسین‌ماهینی واقعا بازیکن‌نفهمی بود. همیشه منو عصبی میکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101624" target="_blank">📅 10:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101623">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509c49999b.mp4?token=H629wZFrsiWU94T2yvku7SKNmiiV4VtNHLKnbPdytZBLMMvSeRsV3fiFqT6o6hLQnAl5eL5CT4P9qSCDdws97NNfCxZmw51WaPQYZxcstW83viL6LKeX98XnDcACYvDMFGT2hlcPb5ygWCrQX6-D6XrsdMO14eyZ95EBIvWCyrIjAGbRMWtpCiL938T04Odq0Y9j5WA0duJ6AqrqnHhOW4JiJyta8d0Ud9bcAi4RxfCuz0eV8h6LSmQwhrNpsFgbCE6ErV5mr2sZIVMqJSTTQ-l65qejChB_AHUF2CubPSlDGjJwORQOSeErf3aAjB4oH7Q4-6ryQ5oKngbqny7nm7BK8bSVg62dUDRktntbrZzonBr88jj7meZsxvPYqhfTUUaw2gzOoz0QB9CAGltcUvgzdeWheFN9r5lgjjLLdUIsFqUi85NVZok1Obf31lNzRzmyiqnAySVKcqj5TOcb_svNuTMJGrZG_iifnko3TWdEnayvkK-RuqsVtjDlCw_-y_ku4iyqZaFL8OY2XDlcSCuc-mB0_JkmxLjcgv3Y88gOroI9PVqyWaYAkQ-Dq3iMeuKz9uCpEICXkLqepYciPT24vunTbwqrHYrwEzohtpaK8auu2vSJla9LJxNmrQ0W3Q5FmNnMFztv7JrFU-tWzW6nYR82RagUXN6zFkO2pYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509c49999b.mp4?token=H629wZFrsiWU94T2yvku7SKNmiiV4VtNHLKnbPdytZBLMMvSeRsV3fiFqT6o6hLQnAl5eL5CT4P9qSCDdws97NNfCxZmw51WaPQYZxcstW83viL6LKeX98XnDcACYvDMFGT2hlcPb5ygWCrQX6-D6XrsdMO14eyZ95EBIvWCyrIjAGbRMWtpCiL938T04Odq0Y9j5WA0duJ6AqrqnHhOW4JiJyta8d0Ud9bcAi4RxfCuz0eV8h6LSmQwhrNpsFgbCE6ErV5mr2sZIVMqJSTTQ-l65qejChB_AHUF2CubPSlDGjJwORQOSeErf3aAjB4oH7Q4-6ryQ5oKngbqny7nm7BK8bSVg62dUDRktntbrZzonBr88jj7meZsxvPYqhfTUUaw2gzOoz0QB9CAGltcUvgzdeWheFN9r5lgjjLLdUIsFqUi85NVZok1Obf31lNzRzmyiqnAySVKcqj5TOcb_svNuTMJGrZG_iifnko3TWdEnayvkK-RuqsVtjDlCw_-y_ku4iyqZaFL8OY2XDlcSCuc-mB0_JkmxLjcgv3Y88gOroI9PVqyWaYAkQ-Dq3iMeuKz9uCpEICXkLqepYciPT24vunTbwqrHYrwEzohtpaK8auu2vSJla9LJxNmrQ0W3Q5FmNnMFztv7JrFU-tWzW6nYR82RagUXN6zFkO2pYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
به‌بهانه صحبت‌های اخیر قلعه‌نویی؛ یادی‌کنیم از روزی که مایلی‌کهن با شدیدترین الفاظ علیه سرمربی فعلی تیم‌منتخب ایران صحبت و افشاگری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101623" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101622">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=c6Yj2tGkqmYcibPgvWrt_TKNWnFcXX7iHbk_Fg-sX2Rd3qiryzpaY3pLCLe0nRb-9LNCI25V8O1mFUH79pZ9jNEqgFuFyRb49OHGOQJ-XDnkyykjcqNq_Lt8KHaEErHhiF3gFLw-7-t6e2Xq_RFdtcYHNXJbiEb4vmKYDSbb0jk31MsH1Bd4zY_lXSAqhHJoagiCys5Dcwihlmn-BMRYk6osWfyxiKXJdiMXRQpVAU_PIAsrM6XbtJQsc8ffWLDMW1QzpE6H2voHgJ2HFGBOxDn02bwSSQbdMqyTtFCa9l-jUZxTvLHvtqa79kommLx1SqkWF_jNpAOYbIKALKXBsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=c6Yj2tGkqmYcibPgvWrt_TKNWnFcXX7iHbk_Fg-sX2Rd3qiryzpaY3pLCLe0nRb-9LNCI25V8O1mFUH79pZ9jNEqgFuFyRb49OHGOQJ-XDnkyykjcqNq_Lt8KHaEErHhiF3gFLw-7-t6e2Xq_RFdtcYHNXJbiEb4vmKYDSbb0jk31MsH1Bd4zY_lXSAqhHJoagiCys5Dcwihlmn-BMRYk6osWfyxiKXJdiMXRQpVAU_PIAsrM6XbtJQsc8ffWLDMW1QzpE6H2voHgJ2HFGBOxDn02bwSSQbdMqyTtFCa9l-jUZxTvLHvtqa79kommLx1SqkWF_jNpAOYbIKALKXBsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
مهدی قایدی:
۲ سال دیگر قراردادم تمام میشود، اگر آن موقع استقلال من را خواست، برمی‌گردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101622" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101621">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=KZwBvAaROhLEye91UVGHo4qpbTbrzbtsoHSKnVyVqZXZSyCl4zFMDj5IJP5ZX_0DIoXMBcNw-XA3-CwNL_pLl2G4Q7nZwMOk5-ck5Ng63IeQEH0yvA2E2QaiOBgafNy6FvP8LZd7W-uS3bC89Stw1RGOvVlF7PjGy_XxH472H17tC29XAc0hSZ5ebfpjgGpoe2LGOW1Q13FuYpFddfiTutDysiiwSN3ayoOtLv43wKTApMfx3de4ryp3-RJ1pNEZNIU8Ll7txi37u12aZX_fJEoRM3RHB_U1F760fTcNp-zl3Q3oLRdqjFJkyaE_YrSk0UNk7x2wiOHMEqkkVM7AEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=KZwBvAaROhLEye91UVGHo4qpbTbrzbtsoHSKnVyVqZXZSyCl4zFMDj5IJP5ZX_0DIoXMBcNw-XA3-CwNL_pLl2G4Q7nZwMOk5-ck5Ng63IeQEH0yvA2E2QaiOBgafNy6FvP8LZd7W-uS3bC89Stw1RGOvVlF7PjGy_XxH472H17tC29XAc0hSZ5ebfpjgGpoe2LGOW1Q13FuYpFddfiTutDysiiwSN3ayoOtLv43wKTApMfx3de4ryp3-RJ1pNEZNIU8Ll7txi37u12aZX_fJEoRM3RHB_U1F760fTcNp-zl3Q3oLRdqjFJkyaE_YrSk0UNk7x2wiOHMEqkkVM7AEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
سیدجلال: بیرانوند رو مخ‌ترین همبازی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101621" target="_blank">📅 10:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101620">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8EXXE-56tk-8NkNNgTEaZsQJBb5ERIOXOyUc-byy_dQd6s0Of_XxguSHUCZtVhGmsEbRUhTVhOL9SiWZKJgUL55W_Dc8lOOWSxfyG8lGLpHRCCf95f7Q5DThTJqwVimKjwMMukCXmwtut8MXJwGIYpWgQ4Xrh-X9DM3Wf-YXdi0q8ynmidYDO70z_eYvsqpB3wzif4cT1geEkCx3LoSSelGyVxNPWiYae_DaPSsra3qGJ_a9OoYNyRlQgUp7fw1lb9cgYBjJtmmNWTKByEMcrXa3qw6roFv7tSCCbQKE_Tojljzh9XFIXxDFyZ5EBROLUuzxrsLgYNiIgsBbhAwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استوری رسول خادم برای عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101620" target="_blank">📅 09:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101619">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=RTK_qTUOyrhmzOtL0c8gsJSR-ZTnmdYnwXuoZnrnkZZ21PKpVOcTOlzQ9TTyM3DNy-QGQweWROz-KiM9Lu57XUspzsPqg8GKtCzJiXdVaO0Ob9ymGxHdbmPIa9uYOAro-GHxVnh3oxt3tNZk_8SJ7xsyGeQcIf6U7CH9z9Sknb6UCYwQGt-xtLJsXH9C_pr2XQlwbdnXBsABC6TOQFkOJHBRlA4lV_J-2PmqmLVc_YgdUipW3v8sOOqKDE0wNxR_6BoINFFiMtNYbw8wQ89a3SrFbjMVuyszTr-v4f11biZn5n5N8zqlWkK0ePcrGkpP9ahtRZNGB_IX2JmTN7hqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=RTK_qTUOyrhmzOtL0c8gsJSR-ZTnmdYnwXuoZnrnkZZ21PKpVOcTOlzQ9TTyM3DNy-QGQweWROz-KiM9Lu57XUspzsPqg8GKtCzJiXdVaO0Ob9ymGxHdbmPIa9uYOAro-GHxVnh3oxt3tNZk_8SJ7xsyGeQcIf6U7CH9z9Sknb6UCYwQGt-xtLJsXH9C_pr2XQlwbdnXBsABC6TOQFkOJHBRlA4lV_J-2PmqmLVc_YgdUipW3v8sOOqKDE0wNxR_6BoINFFiMtNYbw8wQ89a3SrFbjMVuyszTr-v4f11biZn5n5N8zqlWkK0ePcrGkpP9ahtRZNGB_IX2JmTN7hqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
صحبت‌های جالب علی‌قلی‌زاده بازیکن تیم‌ملی درباره همسرش که فوتبالیست هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101619" target="_blank">📅 09:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101618">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=aYFKfm1fq_bPqTeA-90qCAESLT34oKkvrr6S1TV4kVrip2cYWgzrDyM6vQA0A_2G_-CzItVp6m1WIanTmRSHk7q1wJJ4cNvq0xTGXg9qI9svFI_79O_kmaKrGSdIGkJEbc1Hw18aEde6mC52q9ISTl5L5hmoax--h0x0q7Xitz7AVFXUfY5_tAWCc3DQSN6hST9dB5Ol-L-ktAdik1fPOFDlKuGRC1yVN2p0RxmMPA6O5opdaS90tHk9J99mGSr5CSnvxlxkK_Dr9nTKZ9kp3aKPI2Aeu98_W4rUkaerltNSCUcQdgefTxW0FmHF8PsBpZRS4CuZiSu0F82SkZiTXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=aYFKfm1fq_bPqTeA-90qCAESLT34oKkvrr6S1TV4kVrip2cYWgzrDyM6vQA0A_2G_-CzItVp6m1WIanTmRSHk7q1wJJ4cNvq0xTGXg9qI9svFI_79O_kmaKrGSdIGkJEbc1Hw18aEde6mC52q9ISTl5L5hmoax--h0x0q7Xitz7AVFXUfY5_tAWCc3DQSN6hST9dB5Ol-L-ktAdik1fPOFDlKuGRC1yVN2p0RxmMPA6O5opdaS90tHk9J99mGSr5CSnvxlxkK_Dr9nTKZ9kp3aKPI2Aeu98_W4rUkaerltNSCUcQdgefTxW0FmHF8PsBpZRS4CuZiSu0F82SkZiTXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
سیدجلال‌حسینی اسطوره پرسپولیس: رپر مورد علاقم تتلو هست. بعضی وقتا هم شایع!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/101618" target="_blank">📅 09:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101617">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB-QISmOrLDzef-GI8cDYRsMD_v9dffwMLGH2rfmp2-Dp2tKwaO1f8433Y27fF6XZupPyQJ-IdpKrDxmrlC3i-dYG_2BrOAaBjUc6BcOhK-aJlh6nKiXhlwYYf19cpV29tkliyzRZmXHKYuZDAhazRz02kbF861nwKG9LZp8h8QnKhvepjQWbryuOQtL-u7HEGfaDmWcme1VtKLhZ8U51lx74LxksAfAaN1BgjFF2cBlGEQ5EhNsvnNOcLEqrviTtEsP2O3BxqW8AN-O_0Vua9vJ_-BMd4GW8D9zBiRrzYbCdp4asI2HvjjdDGHaLCF11fGJc9Fr14AhFLji2Bq_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔵
⚪️
منچستر سیتی احتمالا مبلغ زیادی رو برای انتقال رودری به رئال‌مادرید درخواست خواهد کرد. حتی اگر فلورنتینو پِرز موافقت کند، باید دید که آیا این انتقال از نظر مالی برای رئال مادرید امکان‌پذیر است یا خیر.
🔹
🔺
رودری هنوز قراردادش را با منچسترسیتی تمدید نکرده است، زیرا منتظر پیشنهادی از رئال مادرید است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/101617" target="_blank">📅 04:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101616">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=XTqUTryKfecN_Xrqb9ugO-goyYxq1lmFg8rFoBJeHBNSFTpnxgTn-7TEIsXftrEZUeHemgXEkByN2I0CJEnMNnR98hqrVPUy6zmuU2jLCtyjrU21yo9IpRtK02McsLtfIO1Qk7sfuUTkrIt-CRS6NJyG39SPJ_tUnIRtM__uieVuwz0VPnL4blTT3-GzDcyi1KbeGiGnfpC8yCgbKJ8nTFPxDzt03VavnKVb3lD2NcM0eIMPYDBrwsXDV_1i2ZyrnDWpv91Bi5Jk2Htv8H4N18PeHZcgNJGSR60r4CdRwCWG88ZDBlj0iWXD9Drv1Q_sniD9TzFZtFN905h8GYokOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=XTqUTryKfecN_Xrqb9ugO-goyYxq1lmFg8rFoBJeHBNSFTpnxgTn-7TEIsXftrEZUeHemgXEkByN2I0CJEnMNnR98hqrVPUy6zmuU2jLCtyjrU21yo9IpRtK02McsLtfIO1Qk7sfuUTkrIt-CRS6NJyG39SPJ_tUnIRtM__uieVuwz0VPnL4blTT3-GzDcyi1KbeGiGnfpC8yCgbKJ8nTFPxDzt03VavnKVb3lD2NcM0eIMPYDBrwsXDV_1i2ZyrnDWpv91Bi5Jk2Htv8H4N18PeHZcgNJGSR60r4CdRwCWG88ZDBlj0iWXD9Drv1Q_sniD9TzFZtFN905h8GYokOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
⚽️
خاطره مهدی قایدی: بیرانوند خیلی خسیسه. یه روز زنگ زد بستنی آوردن خوردیم و خودش رفت، گفتیم چرا حساب نمیکنی گفت فقط دعوت کردم نگفتم حساب میکنم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/101616" target="_blank">📅 02:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101615">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvFCxoncbZv5TwbZyAcm2YX9wzBuNWQxoCLAwcZ7FQaE_mTo4qwZC4iEi7zBsAa_UfQpRzqIn3gZYW__BAmP2G7TUjMNoEPal7EycdeUsixjmGCWncYEIGmGVUuL-e63lKDJ1gfCK-9pcHABg_LVLw8b6CgTi_KlCwdex0_xe3GToh3Va_KsA9IVYA6hYCO-Qqy8YGs6KgcltfKWziOWltyhTH-e7jXHW22T_1Ei5FYfQotEVUNwqWXOmEbqNBlBK2UBBuAJpWUPOcNfMqzYk9UI01iA7KNc5-RdXMInKfkKFDfhzBy4_Tng0prLkTsHdG2iYbbsMEGPsFrXNnGkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/101615" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101614">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMSQ0jK23r0PNINXkzfCl9s4qTqwMXqVnrCWyTq8-Fi1LaRRwHHMSj9Z8B4rDKw9vVOJ6vF5MZvHb14Q3EVL2qLTgax_AB0saTp1LsYWC7obeAG_1m7JanDMDJL1es76Qm5lHK7WgcGLeRzlhbD1jbmIFjnpI5dAAW-Jk_38iiiesKUVHxZ0R7MDb_UYLpQFuO-aSkkzoSG3XPS9xfhZB-Gou15Q9jTyerhgCuFp2m5y8OOJyXfW-MIiV-olGSfShvsOfTGIP6ErkPQoVwd_9D3B7R3AccBh5n6wJqK4oiigPFG8tVKbZDF8aTY9xj-Hzx4wVkcOIcWuFJh0nGl_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/101614" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101613">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMpnhlwIr8DC6uvSyBwrdUY6UmZKDz0nTVFcCtbbORXeitpMm6MAWQEz8N7mFBUYghuUn1ICaq2aeI1AfDZ0tvdjgXvQ3L3lfIHRitgHxsmYn8cuLvxIWkgy2Sza-84AwojC-OicnOdwZKW9_KeQDrRjiK9hmnlP2TdbFDXW4gTvZvm37ksJNrP5OMOGkq_vijblGzmR33ZvnnE0iSJGnwbE1GPGIQVq6rXNiNVi9PuwLcW-HIxA9mnKNUE8VF6XEuY-PL-fFTR1BC7HIPgSWnOUESrSfcopcpM1ebKWUx8eBWPL8Svc85IhpZLv0hoqx8v6UKA9GCfqR-MaFqJn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام از تبلیغات تو جام جهانی 22 میلیون دلار درامد داشت و شکیرا 17.5 میلیون دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/101613" target="_blank">📅 01:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101612">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTVa3UHwL8goqhFb4_uDuiTtdf_GnbQs9bY2qyGB0QTU3AxEV-REmiq-6QtLbmJAucxmJhPZngD19-dlB3l74rbNsTLTmtHcFWO-HzAqAo_d9AA8_cF-GwpR1-8gDC0VapJLmK7RdlhHpV010rDuarzUA1O7Nm9RE2alTzQphvTDmw6GJ_jJj1IIU9Y_nDhPPC9NwrtFKX36P4wInKiZNnQ-OpL8ew2AL9Qljx7BWy3wg0AvHM9TF_zqyIVc5UoJroVDO2KZveUFFuc3GDKNDp9GKURNa6xS_j0hk2F-o0VIpBB9nEez8uoHIPD6bed92fYEn9MbqWB_VLPdpss3zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط 3 بازیکن فعال حال حاضر فوتبال این افتخارات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/101612" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101611">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBq5-EUJJdlutrQNPycFxqAp5kvtmK4zgmrZ2Y4hYB6js8sFPclMWkNzJqWqMu8i4BC9-2uTMPldLcj-pW93riU8pnF6qSWZwh9MmW8_u22bo4bj3vSaKcHI2IqyYKT4A6xGVlZNl5rDolzmW3OXvq6QkokJ0w9u2JB6nq0t09gdMCHvUJ3i215lEHjkxcY_Ee1TSEgM_sJPQBskm0OP0e4IPp5UsQo5tFkDfmn92J0Xrkij3PLW36lTWj9_yIxnQlYsogPftkQICWIjZPb0J-osNbEowemkGuDtZ6M88km9bikp5qxsBfPbpgUpurs7-Uwt7HfwA2m79oIJuxQ5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/101611" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101610">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HzZIvqYpRRHj9p2LJlnhzPidO9HyXiVccnWy9mIjzTqId9PKvmxyYQlWNTazCYkaj1gJhgF2NmmCf8NalD3rRYvXgM6fXJLZ2YFc7Z5OCvGgQZi9L4A1Of0oBb0elUFqwII8eB__UMkRXIyZskNcSIOgMYFZZUiOimNrGOfoleX2-WrFtfBYCByRg0-HKbc-Cw8xTup4W-e9AjZqb77KaVsj9FwUT9JIBp4UshFbxfXrXA1wwE4azlqxH8T3F3oWyCbjY8-fJmJ7BHLzOXS7bxk7MOFfSu0fZFQ7F0a95EBX5W8rhTKUT2B6LFmUUFwBNEZ7hhA4HEtUBy7ZXLFlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101610" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز: رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/101609" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3J02B1HwghCIXBe3ShcMtlBTfsgOXh4_GjGXpGNYYMJ0HAh9NOYZHfjI1oPGTofKsEPspBl5wwrqvXm6sULyk9GnKCdjsczmwEMslm1D6O5mesFSG2h6Kt7p1ajOMnRhT0IyPM7v05TOT9cw_wYXfvreiCtXTdhl2fbDUxj_XaPh-HNFiDUuQspqLjmhlBvH0h4xpygQC270hVAHmPekHJSCFJjKMPujBIrbqfRENafjvKzmu2NmZlyVKd9ieVD_R2jrS-IYxBk7IR2sHa6sq8FIvCod2WW6Vjyld-_ZG4ZEKf4pZREDuSk6gxLeME133Xbar-mH-LlFkbkQpq9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
والنتین بارکو با قراردادی به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/101608" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101607">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
▶️
👤
حمایت‌جمعی از مردم فارسی زبان آفریقایی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/101607" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/101606" target="_blank">📅 00:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UDsaJWTOZcXCfW8oM-t7VjH1PfLKmQ8hgObbHvrjAra9SH_LG8Zd7GPjPAe12lyvcRMlOneu4KEgrj3gb6jzIBD-f4w0SK_RRClnhWsw5a1dLZs50LroxvqxZfSIyoWMURVgCXtpmA0IETkgh1w-yLpyu-2inp5P-jur6xzCwXGxMO7ha160rXAzX8BGzoD6iBmsLH124n-NSWrEtXRbFqUDdmPXHM65afHBlckazuIrLz_0Cg7GvLXAsFfzcmrAcI-LGM0L08BcTjFfjQRrKl2UHFYNMGDguxABQVCO-OqLZUzArS35GUo7UeuHuR3aN11hEGnPzHZIKmS1WBPPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/101605" target="_blank">📅 00:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsroBfNjruv-Hs7nKeVOZ1mUcppUw9ZShbdpy2PFQDCkGfwajzSn4sVhaujNlvwltd9_kdtlF8PQJCU3GyiD4pWCe9Pun-ZRda73ENYAc7RdQPniz2WzpwsfFb5z6tu3kpG03-zXhU8g6ZNskbzZ8lJYUTSTdChnHQgDhWFfYaDUXDihXw89jkBlbIbCbtcmVjFMOpmYVPXANzJUNAMCoTRetn2eopwJ9kXBPh2FT7yDb2HH8M-KWkD520EyrCFvd1xdyRrua7IDQgq_SHxmcui676R7cFvrUO_Wq17Rtu_5g5LqpyAQiOcf4IK-c_5Pov38kMT44myR_eDlqfczXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
ده‌مسابقه برتر جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/101604" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/psuuooIEz7ozYTdBxJhywa61TqSdtNgj9KXjRv97EHLT_r-nzX26NQ_s43okUcY1fCkz-aDHmSB-ePXvMmRi5AobIutCphiBsZ3IW2QMhFOhTLY-xhojmdFYTP1PIqubwgzoP8-trvNJwC3ISqueLtWDUWdLGIccEVf18EM0rR266JRaGQJYiskShj9G4kPJNEhY7YS8k5b9SE_x3tMuXTcqebqHt6vvulN824zJ3TQK4zS3cYUl_0XVaHERSY_r_R_FUlhaLpIdt1vq-XmQowNlLUP0prZ7rQz3qPFo6wtLRHUrYcIv7ucJTYZz4hY4Ck3yACPgXSoeeagH8AecQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بیانیه آرسنال: ویلیام‌سالیبا به دلیل آسیب‌دیدگی در ناحیه کمر برای مدت طولانی قادر به بازی نخواهد بود، اما تحت درمان قرار خواهد گرفت و جراحی برای او ضروری نیست. او فیزیوتراپی خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/101603" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101602">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACH7sP4RIMTO5Huj8dt84VGKHZdhWcTW0osDiwruvCqhUC_ddYnVvq9RLL-WdCtLe2p1-pMWlS6MuhFGWA77aNrajDZYjZKkK8d6nQn34MF_hhhsYMWqDTfr0_6DfX-fGWl-Ctx8biB0H_kC7BFXpkGoLkFLBuRHa6osNP2Euun3dF7H0lgmJNARLUDGl_rDT6l12yD-o3n2B24yv6y4AnUIHosi_iCwUj5PSFF4UTX47XnsLRTkirDDKUCfM8bOVqy7PH7MEF2ULW7WpIguUaAdHz5VvVzZWpixr3tx_S_zyIna2hWgl4dDpBrOYcOJ-jp5nFeEZYILIBWz131Qzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توصیه‌مهم صداوسیما به مردم ایران؛ فقط کاش تجهیزات هم تحویل مردم بدن تا خوب بزنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/101602" target="_blank">📅 23:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101601">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ck1CRx0SBPVkwPPI07t4HhCdVUX4xqnos9aSTNSLQr98AIRx1t5UR8W3YAgHlriKvPl4KPxkAj5Boh6VvzasecWQdOaIU3fpBEkBaox3ZBPvf3ZoEynTISKDbWATa_fwnpt0cyTNRtI7R7f5nwvyUHqYN-T3IMDrshyf_XbDwOqU1uV-eJ6unJwhKEruJNYekAjYyemnk-djsCorKV81Ed7qyFlZ9n-pF4A41Y4wy1do69T7WZ-2Bm_s5L0K8nYMWyqdPPg1sHibtY2Y9BzQDvJkn6zrEbhUP3gvCJkbwgM58daA5u_AG_w2On6JpeGwPzPywSIGUPavo0Wy0OMMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔝
ستاره‌های حاضر در لیگ MLS آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/101601" target="_blank">📅 23:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101600">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtVfynLHV1DqfegdVBosjTZNPUlYdF_RpHffyp-oYoC_5EFHwsonk3y2SbSKUsHc6DW9bSH2akzJYlTmwL0LgjZRQ4ca6a0Bb9u9bIMI4ExB96DPJlKX-EEsXbq0nNCnIyOIn3LWdTmqUcnurZ65TzqsaodI0CR5UAup3NYxWdA-rxYLFbAY86mEUwk9wEk2aRK7dvWPd3agIBx8kqmNrtxQm53aGTqnkDAs2Fdm2RmhYjqx8jJCu1LOYD1BDs7kSCc4Q9xlKUrs4x59jRMWGMyMvD4DL-BPizRT7EPbu7zv1TYCrwnoO0DcjiDpcPhRm8RIga68M7Z3aFxNAaRH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز:
رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/101600" target="_blank">📅 22:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1nb6ZpQ8GwgTcFJZ2L9mPxzVSdhYNJHAmfDiGTPA4FpZ4GXSh109Pwy5P2bEYPlcSaLIo8Edyf1Mfy3S5z49UYFZl8qx_ZVrYUMcv9msr8E6cPzKrAv6ywHKRb0GGAyrmweKzeUxM-UuOPezeBjLNs8TV-fW4CMt3x5CIcUkHTUJky-S9MpityXEOfoLx0IwF2I0AAkOgk_DmGeURLjA3evgr6-O5qPfRMinRJEXxLDxN6_7rpMmI5fumb5bJlYdVGmiFyyZ-cYXZY0YkPcVQUCcptn0v37MZnCrQicrb7QGzE6jIyv7VXVucRCFeWYXDuXNK2Zj5HUM7GceW8JCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از بیلد آلمان: کیلیان امباپه به فلورنتینو پرز اطلاع داده که موفق شده مایکل اولیسه را برای پیوستن به رئال مادرید متقاعد کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/101599" target="_blank">📅 22:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101598">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrIOe3xiog0jZYI8Jc5xpXjHtHnMF8ZcUN_wH1_nv8ovbvfPyow8Ijv9J_Kd9vK8rUa04KjO0sXE7XnfK-1PL-wd_fi8RQ-I_K-aNCwHGLYJ0IKU-xgzDyyhtDo2fAyQI9XMWZNHDCuoxlxvb1xxyhaXByF5UO5Y_sjVp7g6ouJXBbJ9qtXv1jJneWVVh2G1AZAlhlTm0vFGnwtRZ1g8YULzhPObp3aYDdtEr28ZPfFSb8Y9CxTR3_oYaN_WY58G2htvIMzAYHW7NbhH46wHz12Pdy_zVbZFCJTjWuI4ZRwzi9gXekTYaJStSwo_pZJAavYmSJyJgD4kPFGAVIpQaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکلی که وینیسیوس این روزا باهاش سروکله میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/101598" target="_blank">📅 22:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNwlGdJB-qmbnvmMqzlaBMehxjAP-QZJ4dojVHIGmiKcKYTi4oQaFXSjFf6xQync2BfcwVCvE9BEB3koraLqyU8qopro3hzCiUtTo9BLQHQYDzuy3cUWcaJj54ybRhfQnY2Ubh-dElVJI6XWCmo0xcmPnDco2itBWAn2Ey6LfUWp6RGaHoQfnir4511UwiRzg39N5Bm8zRS2ww0ScSG2OGm145foFa6dSmnCIPDx3gExKPvJW5a1HW3kc15dix9l9JLyv_CaE_DyOPt7FHbzh7MpSba_oX5pRnrtCzkCfWMWifzzRKXxkxidhLUGaXThs9dINHW2b9R6KKxRiM3e-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فابیو کاناوارو:
اگر من بعد از قهرمانی در جام جهانی و کسب عنوان قهرمانی لیگ، توپ طلا را بردم، چرا پائو کوبارسی نتونه این کار رو انجام بده؟ به نظر من، کوبارسی فصل و جام جهانی حتی بهتری نسبت به چیزی که من در سال ۲۰۰۶ داشتم، پشت سر گذاشته. فکر میکنم او بیش از هر کسی شایسته بردن توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101597" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101596">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuMd1yNs0px7FwxNWNwtmIoyqYoX10dsiyZr_Iis-KcV0ByapBZ_RrD5s9yg6A7QqB2HMki205qRK9si0LxSnSSNJELSgNKwHhJUEkPTFPBcFyJ1SIofG2q8QZBooIy3FUdft4oS1wwAkM4dkQ0kzmNu7kkdTrAAJz_TuTYcMR7btQWVYK8d191R4YjPuy035Rt-aovM1Ei32FlsDDZ3B1b38bVNCT1CswRmiTJmgYijqZhXbdzPGJyO9HnDUXIFGu133qsIqmebL8dIwd1iOw2lsBEFP0Tpb_yX2jWoShRbnU9GHxXwr8V4TVy-NQ9dB-exLsZphvRhnFazYrCuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🗞
رومانو: سامرویل ستاره وستهم با مبلغ ۵۵ میلیون یورو راهی الهلال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/101596" target="_blank">📅 21:56 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
