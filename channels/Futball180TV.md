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
<img src="https://cdn5.telesco.pe/file/lO_TI58Ueh6tuC794hPzoJmJuV6wfbk3rQ3fzxlBWu7pZrVLA4VSRqyJFQKd5dUjonz5kSR7la1hItT7T3U3D7jW-FVfAy2WVKh05qhTj7VLMwHjLOrbRMNOvQMug2t53bzMwg0CsVMGyweMhNlvfvPzkEawGs-azcwZks6QAr-EusXUgJ7EizoNInmkZjyOaCEiaaadE7ScI50bd9Vdl5pr8bdd2zexxRx1Ucw__rgXOj0UHdC-FBgahek8QaCDUQEPtPbqNw4_zkYmY6a4x3PvSnZH-Nqe3mJFBNehoJ7aAz60bA_hAap5gFYd6ZdQho7L1qi-XjgNmg7RluU4pA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 165K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-90798">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRqXOj3W1gYKxlJXr7BxJrtupdNDZnEtgypWaqq6nMQYfKZiPcXICQIhYKkHIEG1ao2uShopIBRIp5VZW0Pr6YAvO8J_IjWGnlr4kmxEEwnfNNhS_EZQ1F6Ra-aVzKTze3MOKGyMOY_r95HyDlvd2-g3Pkfay7--d7bHtIgOE3xpQj3gSCGROaIZZMa89pUsiFmiLVE3nTCB22vgxT0CKhXtvxoPGDrByak0XWm5rxDHwRSTScURdktNtSyd4WiDjdCpaKmyOeyXVS7pkDAv4waNkpWBU8tCOH0dWnZA6C0WYxjIRYG58dEKBWnpevHcXsaBldTrkv-kcG4cFyqfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: افتخار دیدار با آیت‌الله خامنه‌ای را نداشته‌ام. به نظر می‌رسد که ما با آیت‌الله رابطه خوبی داریم و دوست دارم او را ملاقات کنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/Futball180TV/90798" target="_blank">📅 15:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90797">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=cIoMrO7oUw5HLe0dH5EA0Yjn3CA1YbPO6zta6yfox9pXoD2E3dI83EgeQcHS6tEy6Cm934LBo-HQ3ccPT2ajRqa29yDAC-4YwVYuxhz3E2puvKXkU-u6I6QVEYMhsWMVa1isQ6Xbu0S6bDwTwhZOQn09wwhYE8slNC7BnQmL7ItHMwSzSrNu4Ys-K4ZUQ1NmirTcdFPLgMEx-BnKUgG9raN_3uVi3XYb5_mYeuucdBjhwYQvo48mcJ2bIt287Nr1ajTtb664LomonXjLWvSwqI-5l7TAoUiFt3j4SLq9dWFg_-JjR3gEu5O-bk1BAID5NB6Y0EaPwExBnHbi3TWLQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=cIoMrO7oUw5HLe0dH5EA0Yjn3CA1YbPO6zta6yfox9pXoD2E3dI83EgeQcHS6tEy6Cm934LBo-HQ3ccPT2ajRqa29yDAC-4YwVYuxhz3E2puvKXkU-u6I6QVEYMhsWMVa1isQ6Xbu0S6bDwTwhZOQn09wwhYE8slNC7BnQmL7ItHMwSzSrNu4Ys-K4ZUQ1NmirTcdFPLgMEx-BnKUgG9raN_3uVi3XYb5_mYeuucdBjhwYQvo48mcJ2bIt287Nr1ajTtb664LomonXjLWvSwqI-5l7TAoUiFt3j4SLq9dWFg_-JjR3gEu5O-bk1BAID5NB6Y0EaPwExBnHbi3TWLQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردها اینجوری بعد باخت خنده و بعد برد گریه میکنن..
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/Futball180TV/90797" target="_blank">📅 15:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90796">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7TgapUx_VyFyPk6QUZWZSJ_Z_yuaaUY7Tksegndhpl4WnPzwmSuPljedGYnRU0V_nXFoMpIgYQzvjxIIzWq8MlteP9ibJ9pyJ_GdqQZXTHH9pY95oq-UHMimTE2CLApxfyYB82jfIWS13b62cV1M6uiDZcHHsN38qvmDsY69BOvB3NeUVpSccMpzikHIeMdedBZu5UDEsXobLhL3xO09btfc-fYkdPS_E_OwtExFzXPZs9dNm5ACtK6h6eHyRH_hrUUlaRP-sDdX4MJBIRxgcjZMIF3iSHwAeTUQi8kv0YBd6rPeQnpySN26bOKBSSRX5gMikyxBNo-orz4ZNQsqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🏆
سامورایی‌های شگفتی‌ساز که طی چند سال اخیر حداقل یکبار تیم‌های مطرح دنیا رو شکست دادن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/Futball180TV/90796" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90795">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
انریکه ریکلمه کاندید ریاست رئال: امشب اعلام خواهم کرد که یک ستاره جهانی درجه یک را جذب کرده‌ایم. من به طور رسمی یک سند قانونی الزام‌آور امضا خواهم کرد که تضمین می‌کند قرارداد با او را نهایی خواهم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/90795" target="_blank">📅 14:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90794">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=lJtME-WJOZmoNBdb_I-165Sxi1P9zKAEuHNTvnJ-675WX3EvwFqJXrxcZ72xDuUTG2ekrn1iMVZSryfImsTgTq_VdBEcF2FxMUNTjNDXOAkFp4K9p-ExfAsQ6xPrAZgIOF2ZXGIBTyCBr-p__920szK7DKsAc6NJiulQn6CSArfbOWNXVTj-1Dfl37Au9JKd93BBbQLWoGZHimyKPrs5Ee25zCfjO9l7jc58zH7rTBcPYMIpCHajTMKFc0LETyBQTTSNKFHQjDjQFE0E1fZc3Z9dSvbG5XO16zckqW8FRJ13QJ5HF3R98TRQUj5Hq7b4avGrfvHUrpMrL1EaVQKsqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=lJtME-WJOZmoNBdb_I-165Sxi1P9zKAEuHNTvnJ-675WX3EvwFqJXrxcZ72xDuUTG2ekrn1iMVZSryfImsTgTq_VdBEcF2FxMUNTjNDXOAkFp4K9p-ExfAsQ6xPrAZgIOF2ZXGIBTyCBr-p__920szK7DKsAc6NJiulQn6CSArfbOWNXVTj-1Dfl37Au9JKd93BBbQLWoGZHimyKPrs5Ee25zCfjO9l7jc58zH7rTBcPYMIpCHajTMKFc0LETyBQTTSNKFHQjDjQFE0E1fZc3Z9dSvbG5XO16zckqW8FRJ13QJ5HF3R98TRQUj5Hq7b4avGrfvHUrpMrL1EaVQKsqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی که از هم‌باشگاهی هم شانس نیاوردی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/90794" target="_blank">📅 14:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90793">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476676c77a.mp4?token=YjK-PJdUzWS5hA5KOUlAJO02V3Os2UcCuOV7IaOygYXq56WlPbRNnIuSSZQVpadgK6dxk6YNOG33Lvti3sQHN4ywt-aRCKi6PD2NdmpK_AS_RqahfoPDeQk_U3VVsurNwhbvd3XMZZQe9-HX2Zwmn-PvFzbk_RijFph2DsBxbGuLwMeSRyeGw8ymmxpMunPsf-Q_KYRuQS8MLq5qGo8Ary4LMH0AyFdE89Zf6FqreUOeWvVcqMaByTVNapr4cp3O7qKINymq6tjcITSB44sUS8z7-viBhUD0B7v8-dLf-nJ9yNBoS9L5bIODYr9KeXP3jyTSeeKSVo_nr-U5oijOVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476676c77a.mp4?token=YjK-PJdUzWS5hA5KOUlAJO02V3Os2UcCuOV7IaOygYXq56WlPbRNnIuSSZQVpadgK6dxk6YNOG33Lvti3sQHN4ywt-aRCKi6PD2NdmpK_AS_RqahfoPDeQk_U3VVsurNwhbvd3XMZZQe9-HX2Zwmn-PvFzbk_RijFph2DsBxbGuLwMeSRyeGw8ymmxpMunPsf-Q_KYRuQS8MLq5qGo8Ary4LMH0AyFdE89Zf6FqreUOeWvVcqMaByTVNapr4cp3O7qKINymq6tjcITSB44sUS8z7-viBhUD0B7v8-dLf-nJ9yNBoS9L5bIODYr9KeXP3jyTSeeKSVo_nr-U5oijOVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
🔥
Colombia
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/90793" target="_blank">📅 14:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90792">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: احتمال داره بزودی با آیت‌الله دیدار و ملاقات داشته باشم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/Futball180TV/90792" target="_blank">📅 14:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90791">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9285a340b.mp4?token=Ve6Sa_x9WaomcgH5R493ZNLBtcYJrAZTf-G1gfDzFcRbNQROl_dSSUR4K7jwSbmqBXLgr6qGUEqzokVEBBX-ewuY2xEAX2wtGp0ImUy-57HVYt8EZ9e6FC-qFZ5UGOAV3dWzuhIG6sxZ1iYJ0oS8HZClMXcOQ6hLb00kL2Uzd15-rYqxkvAahIYLsEoEHOqN5tZo3_jUCOIhFeMbaAUHnjJQF19xn0JzN0-OOI0nGI60BestBiA9KzcTuy41TtLTP8-Jw3LGdPcD967UbVpNgsrw1JEcLXQxAF1isDzAqWufEltFnMPv3cOA6oEtwpCAV2JQ9__-sTg6aBPaw8Ti8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9285a340b.mp4?token=Ve6Sa_x9WaomcgH5R493ZNLBtcYJrAZTf-G1gfDzFcRbNQROl_dSSUR4K7jwSbmqBXLgr6qGUEqzokVEBBX-ewuY2xEAX2wtGp0ImUy-57HVYt8EZ9e6FC-qFZ5UGOAV3dWzuhIG6sxZ1iYJ0oS8HZClMXcOQ6hLb00kL2Uzd15-rYqxkvAahIYLsEoEHOqN5tZo3_jUCOIhFeMbaAUHnjJQF19xn0JzN0-OOI0nGI60BestBiA9KzcTuy41TtLTP8-Jw3LGdPcD967UbVpNgsrw1JEcLXQxAF1isDzAqWufEltFnMPv3cOA6oEtwpCAV2JQ9__-sTg6aBPaw8Ti8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات تابستونی دوستان در بلاد کفر
🚬
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/Futball180TV/90791" target="_blank">📅 13:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90790">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: احتمال داره بزودی با آیت‌الله دیدار و ملاقات داشته باشم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/Futball180TV/90790" target="_blank">📅 13:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90789">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw0-W0gFB517NmzdvWH6BZ7aQucY3wd0al4HApoc1o8fqkDQCS7Aui8Voa5DvEsLFlxQLmeKbNlSmlWqBKn4efrRKTo2dcgZCNM-FIuiwZfTLHGt9eFTCvhr2gFqMBnt_QJjpyD8MlMQju0V54QNJTU7zqrx9Nkheu047jHjj1JDFdpgb59Q889lrW9359T9QivCxjimHBZTFSTJ6ZrTBWsPThoh53Qf4yYHqNOVXDaDMtX83n2zhcG8fXrkCpP3_tTUxKnWUMPG4KZ14L7dozZiMPUQk0oWZikLTDAhP4bc_rDLRPqtjkloq9KHYRFPyxuX-HC10-uv2WrCowt6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ یونایتد، psg، آرسنال و لیورپول بدنبال جذب ماتئوس فرناندز ستاره وستهام. تیم لندنی خواستار دریافت ۸۰ میلیون یورو برای فروش این بازیکن شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/Futball180TV/90789" target="_blank">📅 13:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90788">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJR3U-nZDqyzNTtgUoTAcX8CHV1wSZqRdnq9WtPqy-XsmG5en4GBIP4n1AgqQiD2admcsOK9sxc9gVt8EZ3rZCZz8WA-_g8WQG3_HGDZh5FCRX3aj_BE2YQ3glSrZ1pL1wmUt17iLUru8kZUy9OkaU_I_E_RNfNty2Wb9L5DEl6gMapTUvGpqgUsu3VEeAIosutZXITVUCL-Srba5mQiaa4qmlOGQVmA6ZNvMok1StcREv3wegwIsezVJwR6pBPw__PTzyK_UcB2qejFbf7NB3AcGuodJR4qZvA2UnHa8igikAsfPx5k658kX_z5p4XGYhORDnqq97s8UZYIKFfnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
منچستر سیتی در صدر تیم‌های با بیشترین تعداد بازیکن در جام جهانی
2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/Futball180TV/90788" target="_blank">📅 13:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90787">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXYHH09m69B0U4eNDf6zFwxTuRauI3gcktBytaP9yuOIm06JPBCokTNZRWewwkInS2N3ZHrxWHUt_TPEMQXff6YlfcDI5wtkjpvvdytD0hEX-2bncsrBv5k6-UBUd4MjsHbJqO3KUTuwTr5zECmeX2ysoVWgQZ7OJJYX4WDmG3ozO0yAoO7YxjK46Xfdxw8qBJh9UhKm0JuQlP6aXwguphUrVsHRJknduTEkxGkazqIzwDXVRKQCyF789e4n9CDq_-jbW3gdUNULZCCQFka4IEfZeM0EDuItG_jcuyEUgbCymGtw9Q9GjqD2TV_dqJ6-aEcF3WaVeUCS2aSyU9jfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام جهانی واقعا برامون غم انگیزه..
پایان نسلی پر از اسطوره و پر از خاطره
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/Futball180TV/90787" target="_blank">📅 13:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90786">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری؛ ژوزه مورینیو خواستار عقد قرارداد با گواردیول شده‌است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/Futball180TV/90786" target="_blank">📅 13:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90785">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCxTc2NgsQxiHipLFJSi4wC4AAXXNYpRYhLft84TnFWTUyv4D1Y5kuSelh8z94b-KGVerWAAyaSNclV02mm5AiHor4kx4MkVQLpTzFS2Tp_QC3LecSJQ8NTpYgIR7bous7ivAjAO5Wic_Xoo-D8Pg8MOjeDbRxQ5gaWLD3gEGG_oRZ3T5hufbdRaiCnuLG2WyOY9ROPpI-g7GLN5HcZcUFj7oWsI4Ym1aWKiDGG5a7RIG0220HH7gb5hFECqoexuEzI0gQyMZM1jfY9SjSl-Kqz0ohyIGN5NPG8BWARMClUNbsqdUj75RLdOkxP2SEShQMALgz9lX5atGAXzYyCVUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری
؛ ژوزه مورینیو خواستار عقد قرارداد با گواردیول شده‌است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/Futball180TV/90785" target="_blank">📅 13:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90784">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJKfRcEmP7pXbpDFOsTZ3ykXzkGRTyemWM_mdcm7X7l7wKDtrAjo0ERMYPtte5ln77dHJOz86miNkrtH1bhAJ9F0l4B2F8ScHOaeZF1BG2dAUqCSUjGknXPoT3ygH3a-mmUXj_kEq2bHHVtqDba9yJGpCp5YQsd1p1txlxKmtajjymWZ1n3IGL1ea0GImKGhsg7lyoxRfCdmvSJ4A7PmZbzTjRFLgNMM0cv1bvY_oA9e1wvczk_M75l1UFNO0Wk9R1cGoLYFn6_pvdLcDvppjfVNXCaPGuzSHc8yaKj85VvJIus8vP2bLnveP2wloM--UGJuQ8AbDBq0oBwwLCLv7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستام وقتی میخوان تولدمو تبریک بگن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/Futball180TV/90784" target="_blank">📅 12:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90783">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8caed85c.mp4?token=N4K6vOba3Ytfn_zf-Ow5hiZUZCxnOU5CNLypSM5HFOmpwKaBKcQ0b5KJHCihwzZ9pbAKB0VNS5UroUqtVDGkH4m8DqnyQqWhAMlqNF4n5gPZQKhVdObacysiEE_KC8eIuxrHNaCdAh7IJFgP4VjV_0-vJaVS90WdgiRLB-kSKtmz1gCM88T3FOGyTzzMQG5GBzGfI7iIZOQQKKrTezqeX4DHYV5wLSfZu3pndY8bExmvkVLFvgs2PKyi5DL_bLbuxqhS7mkIzERYMNsz6OsXhKKkc1T9mZOeJUKQk_qk31m5hJHJVCsHq1Y86MRconL02SJofrhJxmAoFqn7nkCqOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8caed85c.mp4?token=N4K6vOba3Ytfn_zf-Ow5hiZUZCxnOU5CNLypSM5HFOmpwKaBKcQ0b5KJHCihwzZ9pbAKB0VNS5UroUqtVDGkH4m8DqnyQqWhAMlqNF4n5gPZQKhVdObacysiEE_KC8eIuxrHNaCdAh7IJFgP4VjV_0-vJaVS90WdgiRLB-kSKtmz1gCM88T3FOGyTzzMQG5GBzGfI7iIZOQQKKrTezqeX4DHYV5wLSfZu3pndY8bExmvkVLFvgs2PKyi5DL_bLbuxqhS7mkIzERYMNsz6OsXhKKkc1T9mZOeJUKQk_qk31m5hJHJVCsHq1Y86MRconL02SJofrhJxmAoFqn7nkCqOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇫🇷
تنها تیم‌ملی که تیم‌ملی نیست:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/90783" target="_blank">📅 12:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90782">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQv9fX946hV1niYRCW9eAXYRfUEAHEZoAeaGpAZz0kX4ec3cigPdw4zQzoM3SyujqyVbyOyntYTfvyzYOM3ORkaod3b1PsOhc7H6Z0sfbWVcDkPWRSTm5HUnzX8-L6_8D4AofvilRJ5k7nh4kDRUXJdUFa-XcdottoxXKhYPbJcRWJH_4NQYcfoCIcZzXIE7TT_5mloQK9X_3Ftafn35JuVFE7ljtaY6H6_sRbLcxkxPs-Q-Qcy0Ynm1YF3-TjwUQedARIHS_y4wadLCmXFnRpukXix-2qjyNpkzw6gNHGZgoSs0HhXxMYtnQtiusSunh_qSbwzE6viGKCHoRMaDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پیراهن اول رئال مادرید برای فصل 27_2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/Futball180TV/90782" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90781">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c9a85cfef.mp4?token=Zh6UdityDVCyyTBYzc5yv0IyBtnXHD4_HN1FenXrsVC5c4cvVLXSsPbFksCFUpBK0vUqx6Cjsx728TXz66jETdkmfkTauiROn0JAMVGjU7HORLfb6hbVTOixwnVqGuKMS8JhLWsdIv2x-s3ThdISyDnLU8TCG0kl9JauUIWYvz1yXiZt_NsAH6nUk3GXIx7PubVsSEinkzhsdKDLyaTVK5ka_hK80AKSmUjH8iE6dYanX91DAqtGCyGdlGUTYqubqs-ltYHHLNxAPm6GX8Kl33LMUSM6_bGl7q8jUen8fwVqUNoPLF-g1YVORzOOdzOu3aMpR8jLolcMFBYl9i7rwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c9a85cfef.mp4?token=Zh6UdityDVCyyTBYzc5yv0IyBtnXHD4_HN1FenXrsVC5c4cvVLXSsPbFksCFUpBK0vUqx6Cjsx728TXz66jETdkmfkTauiROn0JAMVGjU7HORLfb6hbVTOixwnVqGuKMS8JhLWsdIv2x-s3ThdISyDnLU8TCG0kl9JauUIWYvz1yXiZt_NsAH6nUk3GXIx7PubVsSEinkzhsdKDLyaTVK5ka_hK80AKSmUjH8iE6dYanX91DAqtGCyGdlGUTYqubqs-ltYHHLNxAPm6GX8Kl33LMUSM6_bGl7q8jUen8fwVqUNoPLF-g1YVORzOOdzOu3aMpR8jLolcMFBYl9i7rwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇹🇳
این دختره که می‌بینید از بیکاری زده به سرش و رو قهرمانی ترکیه با شانس یک درصد، تو جام‌جهانی بیش از ۵ هزار دلار شرط بسته
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/Futball180TV/90781" target="_blank">📅 12:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90780">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0dddef5c.mp4?token=OTXcSxrbF1jTpCnU2pJpM1S2U2Kn1ASttmv_0XFWmTuYecEqlX8NCPuhaj-X69n2InfkOeadAQRrPIde6bQ-uHyjrEqjgH93pSO1wB67h44aBuFnZleWohtz4TFy1RVm6z5GFjFhDddW8ZqTzwWEmy5He5t-1As424Z9mJkANtbx_gzJYUWpXG_tMfgA9Q5Wj322vz1iHHKn0dqNxGXrRdi_ZFYPVkKCg5rGQqHCCgXi-PVg3e1ImesCQSZtF4y15aWQGHbGx4tRxsnbdDJ-36r0N9CM7wrSYINWOE6z6sUvdRPtcdFnrG9wp1FuQyYWFi1QpitIeW7Am4pwXCG5Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0dddef5c.mp4?token=OTXcSxrbF1jTpCnU2pJpM1S2U2Kn1ASttmv_0XFWmTuYecEqlX8NCPuhaj-X69n2InfkOeadAQRrPIde6bQ-uHyjrEqjgH93pSO1wB67h44aBuFnZleWohtz4TFy1RVm6z5GFjFhDddW8ZqTzwWEmy5He5t-1As424Z9mJkANtbx_gzJYUWpXG_tMfgA9Q5Wj322vz1iHHKn0dqNxGXrRdi_ZFYPVkKCg5rGQqHCCgXi-PVg3e1ImesCQSZtF4y15aWQGHbGx4tRxsnbdDJ-36r0N9CM7wrSYINWOE6z6sUvdRPtcdFnrG9wp1FuQyYWFi1QpitIeW7Am4pwXCG5Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بسوزه پدر هوش‌مصنوعی که مردمو از راه به در کرده
😊
🎧
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/Futball180TV/90780" target="_blank">📅 11:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90779">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1b77wF4xLFLxk5RYjV4OoJxSIAo6JTaHib7jf_3hZLcvXFAuh3fQf259CB2G6r0O6YxH5UbBTmzlKqMVfUipgQJ_0a2Dmhlnu_2QkCnvM9gMSQTU1efQV2HDSv4kamZ2fvZycM8UaWWNCzxp-Reg_z60P8qcEnYzi-VWRtHTpPNknjcE0HoJWo5DBtr1FqFT08DCpRpOau6JLyrs4MkKZcl7SPdbhSshiVLSr-MKTyZ94WPgcJy2JTPUvHqSL1GUPnu_ijeOrlnJkgCNErEbvsje6Cmsbq53RtNoBL_PHDdm1GP2UMUm9DhTcx82TWA5o7tIG5dm_oIw48dD1LlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
توپ‌های مختلف ادوار جام‌جهانی؛ پیشرفت تکنولوژی قشنگ حس میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/90779" target="_blank">📅 11:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90778">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d071cdfe94.mp4?token=Jq9eOuA8sqmZa1AkLjQaAdlu96T5T86ir2WOr7QEppTJc0DxNNXIkF6vz49ELLgmggXpyyH1isSQkax1C8OBw-5MGYBdoFXqx6uGQ_8Eb-hW1J_R75jWkDGujr6BVZoHm_A731i1TwMf-lVs0ipgdAScesTtS5Ggbd9e05T3SXH22HbWe24vBMu_CzLOYhAvdaKGkQGmm1jQIXsizCHCMJ0wDgqs5xSj32kd6_RVailXbNMBdTQNcxJnYod07aIpNXPoMu1cR28qZ5nTPCM0X97J_p0CimU_EGq00m7jKbIQzyKhOIVJyDK9aYUR0R70TkrZEEDkhOjWY36qNP8aODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d071cdfe94.mp4?token=Jq9eOuA8sqmZa1AkLjQaAdlu96T5T86ir2WOr7QEppTJc0DxNNXIkF6vz49ELLgmggXpyyH1isSQkax1C8OBw-5MGYBdoFXqx6uGQ_8Eb-hW1J_R75jWkDGujr6BVZoHm_A731i1TwMf-lVs0ipgdAScesTtS5Ggbd9e05T3SXH22HbWe24vBMu_CzLOYhAvdaKGkQGmm1jQIXsizCHCMJ0wDgqs5xSj32kd6_RVailXbNMBdTQNcxJnYod07aIpNXPoMu1cR28qZ5nTPCM0X97J_p0CimU_EGq00m7jKbIQzyKhOIVJyDK9aYUR0R70TkrZEEDkhOjWY36qNP8aODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
▶️
تکنولوژی فوق‌پیشرفته توپ مسابقات WC که دیدنش خالی از لطف نیست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/90778" target="_blank">📅 11:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90777">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omTSh1xX5eiYTYMsJQET0THh2CD_uny7BaFTqPuQUPjg4ouAXtO1ylwdMLRjz2t7GvIuyv1rWeyfJ_do8O-SidIyqiIvcegrwPlSL_BpJTYE8I60fLhdJXb-rG6rfAGaMsIFjRQdPru9vi3FHjUc_bS8kQNI-MzrcSI_24BrzyYoMc0Ow5EbkB5qoH3FiRo5oiSDaw6QFmzOWjNzK-hkOeCkqVB7FdGOjyzEtDCUDxPB9CA9G_n0LyifJhQs6jCNsjWggSa9gaX_JJG7NRCpGQNwIxthBz6ULuwY5P_5E-m48cEq09ICAq9N_7HmpgRBW8q169WiuTGMfLOmRm2o9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
اطلاعاتی مختصر درباره ورزشگاه‌های WC
😃
نیویورک/نیوجرسی (MetLife Stadium) – بزرگ‌ترین ورزشگاه آمریکایی میزبان و محل برگزاری فینال جام جهانی ۲۰۲۶.
😀
مکزیکو سیتی (Estadio Azteca) – ورزشگاهی تاریخی که فینال‌های ۱۹۷۰ و ۱۹۸۶ را میزبانی کرده و میزبان بازی افتتاحیه خواهد بود.
😆
دالاس (AT&T Stadium) – یکی از بزرگ‌ترین ورزشگاه‌های مسابقات با سقف بازشو و صفحه نمایش عظیم.
😀
لس آنجلس (SoFi Stadium) – جدیدترین ورزشگاه جام جهانی و یکی از پیشرفته‌ترین ورزشگاه‌های جهان.
😄
سان فرانسیسکو (Levi's Stadium) – ورزشگاهی مدرن در سانتا کلارا که میزبان چندین بازی مهم است.
😃
هیوستون (NRG Stadium) – ورزشگاهی کاملاً سرپوشیده و یکی از برجسته‌ترین ورزشگاه‌های تگزاس.
😁
کانزاس سیتی (Arrowhead Stadium) – مشهور به جو پرشور هواداران و رکوردهای تشویق قوی.
😄
آتلانتا (Mercedes-Benz Stadium) – با طراحی منحصر به فرد و سقف متحرک، میزبان نیمه نهایی خواهد بود.
😃
فیلادلفیا (Lincoln Financial Field) – ورزشگاهی مدرن با جو پرشور و موقعیت برجسته
😏
😃
سیاتل (Lumen Field) – یکی از بهترین ورزشگاه‌های آمریکا از نظر حضور تماشاگران و چشم‌انداز شهر.
💥
ورزشگاه‌های شماره ۱۱ تا ۱۶ عبارتند از: میامی، بوستون، مونتری، ونکوور، گوادالاخارا و تورنتو که همه میزبان بازی‌های مرحله گروهی و حذفی در جام جهانی ۲۰۲۶ خواهند بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/90777" target="_blank">📅 10:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90776">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMjiGIagjBav3j54BznIQxGQ4FdCfMJye7TZ9Ebg2tqLyn8aZLPiIuJNsDQXZVg9Z2mp7pzSnWMTh7eBxqPlhmfP3fRRgHobjZMoBJGloDnSwOz7DwZ-mYr7RmPwY0mY8Q5oz0QlRYoOWJvLukEkyN37Bb3_dG5hqCvd37mJbs8yB3NqmPVDZCS4IcPuTYbNO0WCl6Ie3j0qM-JRTqF5Wz7H0BcNWzqrXV0xRoqaMkEUcUFlsD5hc8-lAUhVyxXpE8aPjdFkbA6Tw0v2i4XgRT5CzEnR1WhPY_bNS7kn1QsB0kygVPh5ePpaO8B8HVfzT8BIaV3tUooi3YdYAHgDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرز : فردا از اولین خرید رونمایی می‌کنم و همینطور این هفته از مربی جدید رونمایی میکنم، این تابستون حداقل ۵ خرید داریم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/90776" target="_blank">📅 10:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90775">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f607323bfa.mp4?token=bvbAU5BpEqzytHSOy5NYEr4eRnyt1brUKF1MbLqDA17RVoXHYlHRyGSTC2lIERSpYU2AW0l31sFJNkWVQRFxTZzh0BCl5f2VCHLB8bNDt_l8kyCJeTsa79XtJ8eo_5LjoWfg4u3eI5R7RKYXuOPrpXog4HhPJHjg6eynqoobMaKqEpQ8kX2Flv7VOZyyyA_d1ca6APbnjpK7n3dOBUPoFiEbQ8aF_K-BVNg-rz3omLwxTGBz1T9sSR4epVAzNjcJsxgWz0qoP10beDKfZaQYm-WkF1iK7IAn87mQ7AH8sloqI0_jY0H50TJhjiXmdKNofJuaaOvTuT_jgW4tzJPBxQrGT_Rv4KlTv7xe-Qn8nPp1jvv02O5xDo4OJLXFVFMLa7OJ3StDCXbAghV3zZx9Vl7eZQv__66wWZxLumixOQYxG6DL8vi_149fgD9jfrVIPeFNrKE4Bzz2Hov7aKi3GwAvQ0JuOeQRZ-o3eY9eaQPHUl1GAt5CgwmAewoy44I0JLd6W7YDQzS9S3QlBt778THYOqO29pCxBplIq82bAUZGv71bEGhrjAhhLsWrDO6Eh9jh87b43uAbVFkhy1vDEEIWuM6tvWwoKTt8A2Qwz1lqn76EN6aG7r1U50QLAqQ3I7g2lCr9MAeRqXCgLMkas14kQgcF6LDkX5DieGBPMdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f607323bfa.mp4?token=bvbAU5BpEqzytHSOy5NYEr4eRnyt1brUKF1MbLqDA17RVoXHYlHRyGSTC2lIERSpYU2AW0l31sFJNkWVQRFxTZzh0BCl5f2VCHLB8bNDt_l8kyCJeTsa79XtJ8eo_5LjoWfg4u3eI5R7RKYXuOPrpXog4HhPJHjg6eynqoobMaKqEpQ8kX2Flv7VOZyyyA_d1ca6APbnjpK7n3dOBUPoFiEbQ8aF_K-BVNg-rz3omLwxTGBz1T9sSR4epVAzNjcJsxgWz0qoP10beDKfZaQYm-WkF1iK7IAn87mQ7AH8sloqI0_jY0H50TJhjiXmdKNofJuaaOvTuT_jgW4tzJPBxQrGT_Rv4KlTv7xe-Qn8nPp1jvv02O5xDo4OJLXFVFMLa7OJ3StDCXbAghV3zZx9Vl7eZQv__66wWZxLumixOQYxG6DL8vi_149fgD9jfrVIPeFNrKE4Bzz2Hov7aKi3GwAvQ0JuOeQRZ-o3eY9eaQPHUl1GAt5CgwmAewoy44I0JLd6W7YDQzS9S3QlBt778THYOqO29pCxBplIq82bAUZGv71bEGhrjAhhLsWrDO6Eh9jh87b43uAbVFkhy1vDEEIWuM6tvWwoKTt8A2Qwz1lqn76EN6aG7r1U50QLAqQ3I7g2lCr9MAeRqXCgLMkas14kQgcF6LDkX5DieGBPMdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
مکزیک، یکی از میزبانان جام‌جهانی هم حسابی با این طرفداراش خاطرخواه داره
😂
😊
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/90775" target="_blank">📅 10:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90774">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c4dc141e.mp4?token=aLonVO0KnS7__4Ish_sVEn5N2i5HeiIeemfhWy4QyLDG3h4lfK6MytChr1aPK_7wnUQDcJO9_EpHIO2eq3l0JIlzk2QHbWBvVQzJWjFT_agFmKLYwK8bM84wZJbG-0hQwJxFDUHi8I_HANhT8onC3XIs9M1lgtx0_zIyaNGSWpLp3s0WfwjPXFZHx8sW_swx5sytMe-3ugwDg6eosWUCqydbzWtAqt6YztfrEDsbcBVprDI3AZOUFgIj9dIynibP3SGFcsZ6iguJusgICLP2dEe8aGupziuKHBlHwmjG6FlvYgeSXTD779LAShGPTrgHApoOY21ADJ0MsvlrOtrUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c4dc141e.mp4?token=aLonVO0KnS7__4Ish_sVEn5N2i5HeiIeemfhWy4QyLDG3h4lfK6MytChr1aPK_7wnUQDcJO9_EpHIO2eq3l0JIlzk2QHbWBvVQzJWjFT_agFmKLYwK8bM84wZJbG-0hQwJxFDUHi8I_HANhT8onC3XIs9M1lgtx0_zIyaNGSWpLp3s0WfwjPXFZHx8sW_swx5sytMe-3ugwDg6eosWUCqydbzWtAqt6YztfrEDsbcBVprDI3AZOUFgIj9dIynibP3SGFcsZ6iguJusgICLP2dEe8aGupziuKHBlHwmjG6FlvYgeSXTD779LAShGPTrgHApoOY21ADJ0MsvlrOtrUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بهترین‌گل‌های جام‌جهانی قبلی رو ببینیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/90774" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90773">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ae696fa.mp4?token=sSBoWciywKFyIGxSVtdD-qK0H1VvXSmL104TeDrAc4s-QkTVQP-oaBbWGTT6t3k7RFP7-upxD4sc8U_JqR0qirphWvRpIV3IanWtI9MG4U_y_bHJLIQVStt9c02v-SoFUjyOrPIA1cRzYhT_Se_t5ntWFD_BxWUkn507-hceIBRZDjSfupvUaKcU6Ck8dIelElECrO8NOIOACj-2-nnBcXi3T_3cDQ7Vax3kdcNUQw4kiONYoERsbNMThBFuUO6eUd0I64AUfih_wUUVweObZ1NHu636-n7xWllE_LrqdUHarEyxAq-wQTsDAFmBAQu2XM9H1RXcootViUmTcmlR3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ae696fa.mp4?token=sSBoWciywKFyIGxSVtdD-qK0H1VvXSmL104TeDrAc4s-QkTVQP-oaBbWGTT6t3k7RFP7-upxD4sc8U_JqR0qirphWvRpIV3IanWtI9MG4U_y_bHJLIQVStt9c02v-SoFUjyOrPIA1cRzYhT_Se_t5ntWFD_BxWUkn507-hceIBRZDjSfupvUaKcU6Ck8dIelElECrO8NOIOACj-2-nnBcXi3T_3cDQ7Vax3kdcNUQw4kiONYoERsbNMThBFuUO6eUd0I64AUfih_wUUVweObZ1NHu636-n7xWllE_LrqdUHarEyxAq-wQTsDAFmBAQu2XM9H1RXcootViUmTcmlR3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پنج سیو برتر فصل پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/Futball180TV/90773" target="_blank">📅 09:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90772">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfmIZPSCP78KW-igMSvZLuJ50PFchymgyTz3sVLe4wMRoOKkQGTh77WkZ_EHiM4Pa7SJGaet7J69IitByhopZnIHFLaDT_BaPSe1OX4TNh56_jyT8US3KTTwZCiYLhZEpcnYpWuVFN_8jU5Ag_bv4G9JTWOmxbMTv6F2dgKnfF0litkDEqSYVMp_0scmbYaiNL_MLa0GGQo_nmQJViGmlYREHl-mUAOqRU-1BB80ncnYKvv5XFdFqhqzjtdtJJJoDZ9LJ3Cx4vKBhNTFVOk2D28tTDwpjNQie0F_2YYWadOJYT_Alr5IZTN5GyCe2uJjSwZPQLS-2c2liOHUd80n_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🏆
۱۷ روز هیجان‌انگیز و متوالی که هرشب تا صبح فوتبال در پیش داریم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/90772" target="_blank">📅 09:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90771">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLwcfl-bl3xAbkolsPYoGcMRf4JHegS9zabFdk9hEaoeKZumbC5XxEduXO4vNuNOyq2BCY_x9-H905CL7_abIgPgXG7idFsrNFVDqFovkinlOKT6yFIGmJTr46sN5AqvJajNJuMGue0tL-MEHIRaqcVBC03969y0WLLiUAqc9540c4Tk0nWIQopsKJSC6OhTjwJgZR-irWDMY_NcPZc6gPHqM32C9O79Zv-nEaX5_WgEa4uWuypy7cdWnyr6J_rTVKoH8JxUzdZJSfiDJOvZq3JpYsSPklmxcOy4ic5shuGAfQGdEydBKu5mcHaDYtdt3szTiPcWhUZ8Te3Pu9rLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ اینتر بدنبال جذب دنی کارواخال برای جانشینی دامفریز
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/90771" target="_blank">📅 09:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90770">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ولش تهش هرچی شد، جام‌جهانی رو با اینهمه دلبرررررر از دست ندیددددددد
😍
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90770" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90769">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b603dc908.mp4?token=f8wCEVOFj5FVvZw6Gea3XpjGtCO8su1NxLqvHT89VQD4vx2l1uYt0eAB5qYqZt35IQUae9yTuslsas_jn0-kr1Amc0AyaLoX7KXadLQv6izvAillz3AIDLFZb8aRSF6EI0R4cv0U2pXbfJtHNjrEsc6KzKwvUeI-ld7AvIaQJDFNg9dMzQVJe29Ok1pxHneL9wQyk4Alo-D6ChzGjzfELm4jr9kgbEofit_zsq0CQvdz_O6pMHvLc0i8FFAqCpJaeqIIBSRN4a_hENlHLCfL6V7S4nnX4gBiFccZizG_iAVk1BoFV00krbh3OBlP0QcmkVREg4Fr-0hUTWKLC70Z1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b603dc908.mp4?token=f8wCEVOFj5FVvZw6Gea3XpjGtCO8su1NxLqvHT89VQD4vx2l1uYt0eAB5qYqZt35IQUae9yTuslsas_jn0-kr1Amc0AyaLoX7KXadLQv6izvAillz3AIDLFZb8aRSF6EI0R4cv0U2pXbfJtHNjrEsc6KzKwvUeI-ld7AvIaQJDFNg9dMzQVJe29Ok1pxHneL9wQyk4Alo-D6ChzGjzfELm4jr9kgbEofit_zsq0CQvdz_O6pMHvLc0i8FFAqCpJaeqIIBSRN4a_hENlHLCfL6V7S4nnX4gBiFccZizG_iAVk1BoFV00krbh3OBlP0QcmkVREg4Fr-0hUTWKLC70Z1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولش تهش هرچی شد، جام‌جهانی رو با اینهمه دلبرررررر از دست ندیددددددد
😍
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90769" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90768">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=I9aTDNniuudwos9-__QgmwX89oVzaFWsII8zCFs94EJPHiHIXKbMpl4RA4eoqUqaHAhzIt1zqpXRUW4iwe2gMQMv0bT5qS1yvhv8uSbctoFjacQpyMmx3_6D1a-ydIrREXa39ubAGHCsyPwilfLK1z5Khdrl0GqqPkpLhx86WAEwQqphY-tPmHXczPhv5XnCjlsvz0w-HRlnu7DGWvWawpYA6lDqjaETxF0xzmZD1PeGdnqNaBSR9gTqzp6KXisLoNl7huu56LwqNH1mC5qDKuGh6YjepcLkwe03yvb_7r7OsSeQNte8v3ZLXnlGsq0HJoRYKQJAEAfptseZEj_qWUkIkBw3wlp1Vgew7dfa_Q0YlRejKhXgQNkVa8SVcJJaslXDJpwdXgflmHktE8M7GJ9xI_VlkVOG2LZNYnqLi6AWwDvuAz1vOIl4HuF2PcU7_XJp8C-s2FWqHDlEKZbe7R_415CauRHZBcrPLKmPRzfKPrl8XsuuSkuDWRSPmW8Rj0cz0jhPb67yu4Tbts_5LhvJ8MbN6YXdIDDQOIiqN3vOm-KbTXGhCAzHLkc8gde8BlDaFYfru7j1lUFeA4m_nRw7OALdWkxcvN3rBsHDTomHNqu12FhUhVouvezJOW8y0a8La2zyhFHU7OY7fn7g0SyedPvaRTCNBpWKrsV2HfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=I9aTDNniuudwos9-__QgmwX89oVzaFWsII8zCFs94EJPHiHIXKbMpl4RA4eoqUqaHAhzIt1zqpXRUW4iwe2gMQMv0bT5qS1yvhv8uSbctoFjacQpyMmx3_6D1a-ydIrREXa39ubAGHCsyPwilfLK1z5Khdrl0GqqPkpLhx86WAEwQqphY-tPmHXczPhv5XnCjlsvz0w-HRlnu7DGWvWawpYA6lDqjaETxF0xzmZD1PeGdnqNaBSR9gTqzp6KXisLoNl7huu56LwqNH1mC5qDKuGh6YjepcLkwe03yvb_7r7OsSeQNte8v3ZLXnlGsq0HJoRYKQJAEAfptseZEj_qWUkIkBw3wlp1Vgew7dfa_Q0YlRejKhXgQNkVa8SVcJJaslXDJpwdXgflmHktE8M7GJ9xI_VlkVOG2LZNYnqLi6AWwDvuAz1vOIl4HuF2PcU7_XJp8C-s2FWqHDlEKZbe7R_415CauRHZBcrPLKmPRzfKPrl8XsuuSkuDWRSPmW8Rj0cz0jhPb67yu4Tbts_5LhvJ8MbN6YXdIDDQOIiqN3vOm-KbTXGhCAzHLkc8gde8BlDaFYfru7j1lUFeA4m_nRw7OALdWkxcvN3rBsHDTomHNqu12FhUhVouvezJOW8y0a8La2zyhFHU7OY7fn7g0SyedPvaRTCNBpWKrsV2HfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اساتید یه چنتا موشک سمت بحرین و کویت ول دادن. ایشالا که دم جام‌جهانی خیره
😐</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90768" target="_blank">📅 02:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90767">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این وسط که احتمالا خیلیا خوابیدن، دوباره خاورمیانه قهرمان درگیر آتیش بازی شده
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90767" target="_blank">📅 02:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90766">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این وسط که احتمالا خیلیا خوابیدن، دوباره خاورمیانه قهرمان درگیر آتیش بازی شده
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90766" target="_blank">📅 02:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90765">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💠
سلام دوستان ! اسم من مبیناس صاحب کانال مبینابت
✅
👌
💠
اعضای کانالم روزانه 3-4 میلیون کسب درآمد میکنن
🤑
💠
میپرسی چجوری ؟ داخل کانالم عضو شید و شروع کنید
🔥
https://t.me/+vt7V5iY0jVhkNWU8
‼️
اگر سنگین شرطبندی میکنی عضو شو آمارش فوق العادس
🤑
🤑
👇
https://t.me/…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90765" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90764">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5fnwrz3wUBgzY05tdeKtP3td7IjfeJo3Ing5P2oljDH-Bx_xhjGhC5tSExWxHG-dB-E5A4O9Mebe7QCEeYS3ja0gB4DzgncfTI80K5EFnFWVbj6JGmFOWkZxuFnFHHKJ-xsvVQN1LPYQfsf7_rcefssnq9PJuygDuu190bbqoH0HCo6tm0KP-xft-QEVKBQ0YH4xslZ5XE8Fso78yYHxjjc6YDD3p6PjLLpyWR-bYuMXhgZK10MElSoma0OTDQxHjfit_PjGz2JtW7PsRObxKyT0pathrYXzLXQiUsmHyvle-RMoaQVIaT8TbY887u3z1CSNN2yjXRzxBHKKTsBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
سلام دوستان ! اسم من مبیناس صاحب کانال مبینابت
✅
👌
💠
اعضای کانالم روزانه
3-4 میلیون
کسب درآمد میکنن
🤑
💠
میپرسی چجوری ؟ داخل
کانالم عضو
شید
و شروع کنید
🔥
https://t.me/+vt7V5iY0jVhkNWU8
‼️
اگر سنگین شرطبندی میکنی عضو شو آمارش فوق العادس
🤑
🤑
👇
https://t.me/+vt7V5iY0jVhkNWU8</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90764" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90763">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz0cQQWVgDcnUdGXaqyEQuWIN1XykEQS0YGeie5fBqZpaz85cZJrFEj4VFVkkMSjUfTwLkn2m11Xb4TbYzZJG1y2tcSBXsBqFoSVvjomPOjAFRoz6bcR6W2ywLhzSx_bVFi396IAqTOUW5vav7tzoq8HqsLoSU9aOLoHk8KVf6t9iVuRLORxVf4g_ITaMO-cOaO_bW3K-v_eWU0OxkVPCQcFQF5YBLil22tkqj6X2UmY-GkEd_qKgg_s_4d0Q1KZU3aCofEg77lJOV6m1_4DUto-nCmb9GarXl-4HvsfNDu0ZDPTf-y2EpvUPr6j8XpuLyMWwzlnqIierqHc1BexyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مودریچ، رونالدو، مسی و اوچوا از جام‌جهانی 2006 تا الان حضور دارن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90763" target="_blank">📅 00:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90762">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAIdhjAae3deoYmn-RQwkIeTPWPMr5TYg3yMNdu-NPOJnHXTYTSUXh_CbDbF0BU-b4KR6cujIk2jHsAwfKNQjhbZj_lQe3RNmKhHekW4KsU_OWGlUcL14JqXH1lyHdkXGUzjlJZvcNwoUwv3JG3UI5ObPyWdQRl5brvMbJxmYVhz338QY_UJvR8PErzG3TmfpaqEXSPDHoZWMdAabkYaWWh44ZEyt6Lt_fARFcpJM2DjRaD5PupCsR9gUceW_SeDheNaENK4ul1sCy8cJd9-Lba_IRfpTYIqObsXa-VxAM8salO9umxVh94SJEiFi1pg5Pm5KxEkHW-wg-w45UbkcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوووریییی رومانو؛
دنزل دامفریز به رئال؛ 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90762" target="_blank">📅 00:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90761">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/JAlUkNOCj4MslBdOIRrKJxY03X_a4zF-Rt1U2hRCGKmbOsHh930v8QgHPzrnRXU7y1cyM2JCAUwjlhzn49Xvo4D1Y51-VK8MbB4r3iUdUduIGDOfsDHj4uuvMw0jtArQjMI1cvWoGd9IFYR9B_lHGiZQaLgJDcK4ZZHZRFhlLOTlZkFnEFOSeDCZEKh6O-_zvajVeoLMJs7YK-zdWkoW_cadGFbfdWq7CAjvaS8UFxG3CyjGL5n3Wp_XZIGd_heKgtYRyxEM2S6jWW8tSVuErj4GW1Q5achCcaXTsGpqWhRWUEnljBkQBhNabmLMyBQ9DpZW2tBI513WpNjCWZOJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولدت مبارک کون عزیز
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90761" target="_blank">📅 00:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90760">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN_6vSg25X9Vg0UAfa6-gHMyJnEf2dPk-8rGijaTEYjqqX2ox4W8Ki6XZoHFE6_TpNFNhM7rulihOFiPMu2sxX3iYqIoKAAiEwqB7TklT4S5GvQCl8DyMGICu4DxfNAOSKLV6wSTBTbwhAzF61UiqLaTIWcSSshSHR29HuF5Dslslw5HRMSX8YxRzBr5B2G3Ntk_ISLWiPvcGPDdMUHhbs22Km-1YlgsYSfIlX0rO8FKL5bPVsR3d6VFzMpGy4fKjUko4YygltzEuLEZYSPbAReioG7VurjMU2EVE3Jqvj9n-gcqCUXTF1t1BX3OhmzxWJutDU_ekl_VMINSTS1PAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎇
جشن‌تولد رضا شکاری با حضور همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90760" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90758">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90758" target="_blank">📅 23:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90757">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg5gF73dehruNrJJpoVd14dGQwhA1ItTEyHvc8TzoDOSbo64xmTMSb7kMiTNBj-hSL-aIqbksDutMRR-mh5j5gIeiH2MrMVC_j-M4ATiE5dKclhEXvl3KthChGK3I0SOHeBF7gsgEaMB6l2yh0JTW80D2GjLI_35wBdI8IeGJIV_ox_wungiI0Uwuv0XGShTv1nlXFFQsNvxdlUpwlaAtHKzrmJlQbAVWHEJVFJmTENooF_xFBrTp8MWXaxACLcdWmXwqnPLaXw_TRblnnezSpqSm2MjSbI_oI3CLg7UNnZv1OVQ-lJLcZXcLhh6dQ8GnXOx3uIPhJTgPirUUL5BNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین روش‌های سوپر اپلیکیشن روبیکا برای جذب مخاطب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90757" target="_blank">📅 23:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90756">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7127e40488.mp4?token=Gn83hnBPFVL1DwOabnFgsQUAsJaXGx99fFUvzZD_e24533lZRVviEUlxPr6oZFOQm1aKFQfQ0ySqwKwJC9FVUQwqaZABCE2QWCI1mWujVrlUEP-6pM28gXLYdpBtxOnFbcXVmrpa4VjrYrEhAiTHIPNcX1QlpIhhZtFY0FzY1VCEVWz38Lz7RQz5hjNxRlJq0hgXY1c2J5CKstldyodIYJn74t3-c75bz8Zwq_H5SUlKHHt_fg99MiqtA7fKee2vT6R8Ucx_JYImgpUzz3SumwT0FShNhUOqc7vcgNWVf4MEuCsIkUI4_fC9SXMxScz44UoOr2_MysVkG6mx76BYuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7127e40488.mp4?token=Gn83hnBPFVL1DwOabnFgsQUAsJaXGx99fFUvzZD_e24533lZRVviEUlxPr6oZFOQm1aKFQfQ0ySqwKwJC9FVUQwqaZABCE2QWCI1mWujVrlUEP-6pM28gXLYdpBtxOnFbcXVmrpa4VjrYrEhAiTHIPNcX1QlpIhhZtFY0FzY1VCEVWz38Lz7RQz5hjNxRlJq0hgXY1c2J5CKstldyodIYJn74t3-c75bz8Zwq_H5SUlKHHt_fg99MiqtA7fKee2vT6R8Ucx_JYImgpUzz3SumwT0FShNhUOqc7vcgNWVf4MEuCsIkUI4_fC9SXMxScz44UoOr2_MysVkG6mx76BYuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کفاشیان : آبشو دادیم آقای میثاقی بخوره
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90756" target="_blank">📅 23:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90755">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7fd2c5dbc.mp4?token=FU6IGL9gOX3Zump_HgU8YC65odvlHv0F4Sc_3QlaELxm9D48EJf4WPs_tGwlvhUq-Z_OUSHw3HkIV_ebb3go-yCtCxEk1Ut1Jzg_mX3qc6fKZdKfmyyIi7VMNzq9OAtX4fJUdFZt1WqXKM_TgpWDOxTspi1S-6qPS4xegb-Eb16FlbaI6sGUH0h6cNOaIZclCbGQZ6xOJLX-7Mz2WnDAQ39nimbQFr5bWdc_fKR6oi6BCngIl_qENaEjJKFy2WpUrnid5tTs0YPwrNQvMqAH1iAfNnNjUeWlqQAIpWs9zV--F2xN9gU-sb45qXkEkdB-lcUy0_zUmpYEvutpyRIU-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7fd2c5dbc.mp4?token=FU6IGL9gOX3Zump_HgU8YC65odvlHv0F4Sc_3QlaELxm9D48EJf4WPs_tGwlvhUq-Z_OUSHw3HkIV_ebb3go-yCtCxEk1Ut1Jzg_mX3qc6fKZdKfmyyIi7VMNzq9OAtX4fJUdFZt1WqXKM_TgpWDOxTspi1S-6qPS4xegb-Eb16FlbaI6sGUH0h6cNOaIZclCbGQZ6xOJLX-7Mz2WnDAQ39nimbQFr5bWdc_fKR6oi6BCngIl_qENaEjJKFy2WpUrnid5tTs0YPwrNQvMqAH1iAfNnNjUeWlqQAIpWs9zV--F2xN9gU-sb45qXkEkdB-lcUy0_zUmpYEvutpyRIU-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این شکل شیک و مجلسی تیم ملی ترکیه بدرقه شد
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90755" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90754">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftbcCXKPHaJz-rfHdlZohSsDteG28DO2jKppL8km5Oc7zxeKZnEJEeF2aFlZBAWVswENft3dbg3iwZht6FG04OMjjbAjaxEYguajd77EvOuMtV3AsTGE92SKz_XI0jYM7BAFvog9QDOtllHt0C3nT3IhFw2LjPoPqM4OtT2G3WSXTVUrXEyeuARQfCK5Mz3Ub103G4zrBDD2_P8mGT4N7pVV_Qm1HZYRfE20Ei28s5NV-OhIbWL8CPi2T_sWYivCqOeIHx5Crps2MGlRXLsBNvAnYSRz6PS64ik0eSbQk5msOje67hpmJ7OoqGC9cnuro2bMcuaQaXIjQP_5znnBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هلند
🇳🇱
-
🇩🇿
الجزایر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه دکویپ
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
هلند در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
الجزایر در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر هلند
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر الجزایر
۲.۷
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه : هلند - ضریب :
۱.۳۸
🧠
نه گفتن بخش مهمی از استراتژی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90754" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90753">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lkv_s0Zp1MksPky237xZ4NlDAtJn-uMxcaz0dPg1oEQlYGUKx7pa1X_mBD1FRThGfwjjmh-PrWOgXN4U-ByBs7TyLrkwfdAV-PcK4Em2tpJskh2wabm9k_mwPMHv6yXrQoJsEFIf-pfiNXJ2GZPnB3masAoXClu7Cg2UJbmOQ6UqWSVt2HZ1fJLUjnM9PXJAV4OdhikPs1uq05npYMX_-iDubdHgfCJXH6-jDvpN8Pic6IgRL75wFZI82BvgUMyfBY1NkzBCpCAUkeSFl83-kl93mqCX5q9lq5OQgJUSGnljXC3qeb4GQYASrfq-aT2KkIsmjEje3VLaCk8CE6kk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اون ایونت‌هاس که ناهار میری اوین.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90753" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90751">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/px5-tbljZa5_ZW5HRmr_DLDGjJlxWVMIqkYcXQvkhzE_wjJSEwNNTkMQdAhIz6e6syQorg_uztq6cSpkYYmbEeIiAMZDWe2igFjWQQw0ZA61QIPjzx1iqI8vZ82asSulFSIAh9B_FHcIs2ZwI2u78H64ggZKS3cUqZZIkZfOW_Xu7S42XYqxWVoEK0F_NUaRbrQ6iSNre5ydkSz4PHPCW-D-JoXiGXoKzyv2uLOc8SKZf5dUII6_RNxuB6t2GrSPLkYifvBH5b9F9RhfVcfjKVEa4s0TCFFnNsNELZKRE5YLEPcVIhOGZd1p3uX-1A9mVnC1p2vyZkDGsFxyc_YzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریکلمه بدون اینکه خندش بگیره:
میخوام بارسلونا رو در دسته دوم ببینم، خیلی خوشحال میشم حتی اگه کاملاً ناپدید بشن
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90751" target="_blank">📅 22:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90750">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNw6Eh0cmg8sCwDWj4Sm0hwK-8n5Q7yn92dG-RDBDHZu5oVyOt7zAHsFx6sEnmiBaqY1yhkDV6S41n0NTT-gLBaUzCcoz_qap6Fm-uYtYQg5tQPtn5yqTXmS9g4MJKXVv0d443pbIb7bIPIiwqGtI3FJCdZJ4lPn7JUq1ye4FT-BJJSCT-LhM0i03xJ7p8njRNdb7CK39ztEWarAwGJ-Bn1Or1LH5uR_LY9NiCR9fVhG9z91n4mPs9dWAM2w4L_ILcC1d5SGjWWJGqgR2W0j3h9l4Q8HCSfJZbqq__RaMbgrhiK0kg2e1-YTLYFXhku_Lx60CrnwNLfmSV2xOOlnuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنسو فاطمه دید تو فوتبال گوهی نمیشه زد تو کار خوانندگی
پست گذاشته ۲ هفته ی دیگه آهنگ میده بیرون
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90750" target="_blank">📅 22:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90748">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0HtvihKurXSFboDLSBNnbNJ7Su1lvgGoUCWmfq3CWVcbySb4hSYxY2RCP7sf8kXCdcsm1GAB0fOX3sCpqDDnTW08wtOwBBpEiNm8liU3gSgSH3kIRoEepT9MrdatnxT2dgJDOgfwwISzwCy_sb3_ScYOGIgcOhCMtikodj2A0mun4Ml1Dsx-QVDMniU6ZvI4xR9iqNldLoQLlw9XijXiVSzZ-ln714aRDRuvFI6V3l3ljTP6jP5gxzIPlw8Vpm3v6maPlaFq1fq3mprQ0gc5l1P9g4HkBR-SI6MrX4saJlO4YR3zeBv4upLJ8qXmZ8Nk_zQHq42cSDf_9jB5W-uaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید جدی برای یاران نیوکاسل
بلژیک با برتری ۲ بر صفر در یک بازی دوستانه مقابل کرواسی آماده جام جهانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90748" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90747">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromernesto SUPP</strong></div>
<div class="tg-text">🚨
فروش اشتراک V2Ray
✅
سازگار با تمام اپراتورها
✅
لینک ساب اختصاصی
✅
سرعت بالا و پایداری واقعی
💵
تعرفه‌ها 10 گیگ — 200 تومان 20 گیگ — 400 تومان 30 گیگ — 600 تومان 40 گیگ — 800 تومان 50 گیگ — 1.000 تومان
❗️
پشتیبانی ۲۴ ساعته  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90747" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90746">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UH6AbnmsA8wxIJsnbPjuat34uMhUbu_7HsdYrkA7O_tHpyqkhyT1h1p_gggi8X_k01H0KkAjGy-UGCuy1g65irVicAF8GnhEtwhfCrZwIHc1p1ndLE8ZljD2zCAM6pNziCpRj4UFDwPG5YEFqLV-Hyr99RXzGs6tTbW65wUVrawstAVBLc_MUe9IUNcBRFGfeYhBguZmM35al7tZ1usa891pAQjwbRNievT6Og-2aKIHuq1RqxyWvdne2TEBKhLrrO9l7KehMZEHtiBzYIdu29hOJyBkZ8zEDVUaQa68K_QjpMeFMX4ZQFNmKx2X5AQ5UdZLVc1j3lrfkfxA8gihJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش اشتراک V2Ray
✅
سازگار با تمام اپراتورها
✅
لینک ساب اختصاصی
✅
سرعت بالا و پایداری واقعی
💵
تعرفه‌ها
10 گیگ — 200 تومان
20 گیگ — 400 تومان
30 گیگ — 600 تومان
40 گیگ — 800 تومان
50 گیگ — 1.000 تومان
❗️
پشتیبانی ۲۴ ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90746" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WSsckRNzKCwWlruubwZevY7-WpE5jmu7cg_-doeWac5obrwwOkFQlU32regKgckX0MzebeX-czHKK_CO_DecB96k_cuyWMVdfNKOxO5VE_eBCdsLK-JnGsFoSbGH7QFKp1BzdyV9hrXWQl-EBPLG2vzoSbhdil6oN4uOjmc-Cxgg5IVwk7vm9o5KEx7_pbAatzEHVeuQkpf7Wf-S8wbmefX_Rv2zy5GCcp2VZor04wtzDE0FVcWflDc7HqpqkmkQuWDD-sPH4MWazSggptoXmahzvFqFD71yjOBA-GxpMJ2llASnar0qeRzJa-nT0h8zH2nhMuVNd1hnaXFqLT8RRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vb67CeP-6q1Rp0wsbKzKvdMyUmjsXNhamrRBWEIFW-gnVSLG2kv-ouFq05kGvhD5HDEePejTkzbWMYJ3sgctKU01vFrNzc6xK8aj234YViGRJTDwJ88KOzd1zQQl22gGr44g4DDFO15FMjAbpbYyQ3ROEFUVcD8x3Q6I3bKRgA1CcE0cjCuwyi99IXiq9IsuLmaXMgEd28ghNrucr4HMQXzAIwkUOhPwAXIYgs70tA7gWOGls-nKEDQAE4lE-33cGsEK80yWJqdnd4Vq-QULxMukYU7j7tvhyr-vKh70sqEkikt-FeT-Pp4Ogsy0_OR1dyxUmuuHAwc3IcVuZgWs4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیه اینجوری تیم ملی ترکیه رو به جام جهانی بدرقه کرد
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90741" target="_blank">📅 21:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf8MpFw35m29eKjiSTABnAEa2i41LrF4KJ2fUNlW4zgVI-VjiqcEa6jFNl0V8zSyE2Db2I7ZwC1ydOGqbpd1CejUKBEmgnYs-ZaWKfn4JbFBveTejrm_OeeciSCinvmORZ_OtxDF-MUT2KECRQCHA2zFT3dCvCpSIuPZ3AFXb4Md9dpK4BvGP3Pd-Jkkv9gjfz6jIpC7KPcU11JksWh7u3tAxFr-7QO306oYTTiBkjda78dWN_O8hLUQzqfhwo1Z7yX0gaFT3o5q1zXiKHqf2cB3xN9IziY0buvEO8e--YXkbuKb7a87KDsAJSSDZfBmN3tDuogxlQd0XpkE7rkJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
شماره پیراهن بازیکنای انگلیس تو جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90740" target="_blank">📅 21:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=gSY7s8t3iOO-0H8eknyO773OD9yHt6fgtTI5l6QEBAp4SeISsin0gdRf9pWkLNzY4m1mnPJUMOoJWf4L20OS_E8TF6lcCN6MArPUX7vjagsGvyMcBk1woJoUyIn-hF2wUFOh1rdiOnuvpU6doRfhBAMcBzEkEmFd8Zl8Yx0IEXDVoG1Iv6sGiB5Z6jMkZZf_tiqRG2Uh2awxiJ4UZtop1fhoNWvJLBmpR2w0AvmuqAJl7Sw0q-cLglOg25iCx5Db8XVM-lfOE4CNKgOriQRgFTfbiaV4kqONh6yP_bCIEPvX5IkVpXp1HpN-gxXKxMAN9V9yq-VUB0Jvj6HcnPZqEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=gSY7s8t3iOO-0H8eknyO773OD9yHt6fgtTI5l6QEBAp4SeISsin0gdRf9pWkLNzY4m1mnPJUMOoJWf4L20OS_E8TF6lcCN6MArPUX7vjagsGvyMcBk1woJoUyIn-hF2wUFOh1rdiOnuvpU6doRfhBAMcBzEkEmFd8Zl8Yx0IEXDVoG1Iv6sGiB5Z6jMkZZf_tiqRG2Uh2awxiJ4UZtop1fhoNWvJLBmpR2w0AvmuqAJl7Sw0q-cLglOg25iCx5Db8XVM-lfOE4CNKgOriQRgFTfbiaV4kqONh6yP_bCIEPvX5IkVpXp1HpN-gxXKxMAN9V9yq-VUB0Jvj6HcnPZqEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هواداران عراق در انتظار جام‌جهانی؛ واقعا الله‌اکبر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90739" target="_blank">📅 21:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYbdvhEf-n2_zDASXHpKgw694ZJN__K5a-Oz85KQYq256NZlQUA9Mzz9DKmK0kUkzDQYGusrQbJt2is_iKJdPAcNooqxOvIXtVwqLTa7yPrHE7AE9fWVp3bCk6G2To-uJ03PRntUKL_BA6rhL-nFnF0mVvHMBho0-sysvsAnjllDP7Pphf4PhuK1ocKlZ_UUkd-0AQtNMnWf7X_SHxMnlANK6QhBgqxeb_1CKo-s8u1Dvoc9SoTySHFukVeqkxwNZ_VFxiQ3ddonkBRsLcXVpGSbYA3DkVsNiyNHndYdF0-vhEkyYaBcMyCAI0WUKEumJq0pAxnWyKeBxnh3EnadFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مقایسه ویو موزیک ویدئو شکیرا و اسپید برای جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90738" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90734">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrYtM_kem1fkPTJ6y3NSredS2Ch8ZNzARZC9l0O622CQnfv9aHCS-hekNSAeSmXkimhVzX5Zsv3P1H-447I5yUWhpY9MuAN-J62pF6ybbIFY6P0qM9EVWDvvkdHIQyB4Wgt37UwF-GsjgVdR5opgLQ5A3Laq_P5J-giW11rhxfCDC1PqIwphuy_RetIs96Avb1APmekQQXVhjY6ETOLajSAOSDKHGRzQW9ndE5mVITkf35UsVxwQodhnoZvNJCdTYGlxC6sOj61hRk6xQDtV1n9tqU31xvPiOxqlg0_rT2FsaWI7-10OG2pey9hZh1v9f2xSqTsHGnotW6-gnkBMRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbUmGYTp5ja7wDFwNv9bZwWziPbioSkCyvf-V3U1V-VgrXdH0-M0sx7SQO91kJUHtG3CXEmBieZwSZSxlfBq1P4c4_g5MvjZB02O_hRuznwEMQzkTRlrwW7ARmHYgXGBsp0QrEAhjtRe6rvW9vDQ5HKf-14lxaXdQLTArUnuGt95z_tm4VF_TR1pAhVIXhN5vQN03ANoN2qGfb80e1iU9uZKJwQgkPjOSfVNiSXHuEJiv4OS7WQ20QpA3B7k4Fgk51JG6Uz3wvXB68FAaxnOMU8e-rnubk2jACHPnW3uI_n7xma1Yct3Qk5Wr1YWi-w-7dog0Ra36ZxUUOq-zULTnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG7KFSvVSnHU-6qDd5UVvnw1DP7uizh-8AxC9ZhjfVdh1CNot3BK_EEhhYZ25_l47lwFCOwYMdZ2H3sdSVUjEKgkU380nesKi0LJlkizdHaJ9Xfw4dhK2usuTjxBbfZhdYnspa0PsmbHxbxdvMA-IC1YW73rnavI9U9ljq-EWD8Z6ZZWnanm-SdMTFpsMwBfRgO0p_T5yrdBPsfqIdCbrVz1SWKIYc5qp8meW70Gdvobne-ZHJONhDCpiZ7YB6eaCaXdaW7doHoh3D-xpLegXVu5tiCNE4IDCRxQFRtlEpW1foEExmSWWWkMkXXwKqj6F-zClVsXeyrEMUF00ZxLOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🙂
بلاگر خلاق برزیلی حوصلش سررفته اومده خودشو لخت کرده که عکس بازیکنان مهم جام‌جهانی رو چسبونده به بدنش. طارمی رو زده رو باسنش. وینیسیوس هم خودتون ببینید
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90734" target="_blank">📅 20:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇹
#فووووووری؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90733" target="_blank">📅 20:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLVWLYIetfwYI092DDqfG6i8ut25E9PWFFXT_WR9M0yenCnjh-2HXwhrDG9UxRe9Ger1Mo-OxESV3zlW-thpz27KXWAjhgDJubHO8BrduLVKjaD6mb5gl6utylq6QiItqp3Gfki51WLbTwBcznNe3kG1lPDmuqlo85ekt-HCiGEtU7yf7Ee-J55U1elM4-Pl9_f6AI3nvCBPxUYg0aytG2j7GcvHMHShk1hceERg41zwodUPxXwnN8-in5sd8hnnXAcB2U2G-cyDB6mu38N4dnENFeE7lfnZHCG-lPii9aKg23i5hvncVOHa9Tn7sQIMb4rjX7m-q4ECissqAZ3RaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90732" target="_blank">📅 19:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0JA15ElhKZ1s_Wm5P0lJJDfmnDqacUKlodgGmp_otE35E8CTLCSeX1Ps2yAwDpRQ_FQFNc346C4BthPIbg2ZViip8I3gSGeho230jmNH4KZjQsDzVTn0hpBkDJNhFdZ-M-NGzjs2RUXtKjnyCT7CYCRvTJepAJyCg5bpIfaDo57LR5wiSn5_Yk6qk4z3MpXwaa6UzAHt9QiOYGblfAwjAO6RihOR4DWgfRF0V_P3WXDiot18nP2-CRdLmVCHd8eJ1oJwRsTcJLVqXRBzbEBLVbdsTFNbVzM0M-L28oaq8Fhju2vICDhbHIejXeGi7c_D5ZkcH6o9N1jL8RxpvS9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🤩
تبلیغ جدید نایکی با رونالدو و لبران‌جیمز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90731" target="_blank">📅 19:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uss695t3o14PJkdn0ss-Xv8Tx1wQ5EybX70IvSDb73cpSRv4lnASaWRHkqDVM6Cw2rNg5RzXS6exqyAB6OXEN0ycYsAZ07g0gbOM8pYe266Iaks1UKHH6sDaF8s8R_CVv3ymlJuxSPsXcR5zr7OLSu0MhFU8htf7lbNKkOcTQgBDMi4BEc2HurmzgjUyW6cUCjDEyONXHhvM-bedqSz6ETi4kacKExbvB8s4ikHhRRvFtBOZrOcBv9bS2VAgQShtteqpm_Ss1O4bEn6FWm1mOUWFzYPDRnCWFFmzgbwkVfulO1MvUcEgepGY9HAhanIrrkTK-xqbVJWv1nBJhVR7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
دوس‌پسر گلشیفته فراهانی امروز به تمرینات فرانسه سر زده و با امباپه و رفقاش صحبت کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90730" target="_blank">📅 19:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7ExQutBAaQBuJbDUi6KouIjXJGTtHqJszqKKuTCh6HGLA2V7H1jFIiMm9MKoSoeKsSRj6AurRlRX52EKL-IJjpr_TWPhFc6ZLlQm2XRb0geoSGVbmwelh89SC4ld2wYePSLlVw-4fJnGdZctQtUwk4_zhzq1RHSqgJf2Q5GWcFe49t6ACGHcWOPBH4Jr0EXjA5ILwwCYtmb3AZGSqGhBOYfFR1Hd5gpf8nxhhVzEBnPIovTYv1U5PftmkcGaS1f66nEqpqglOTjgnTO_JjEeAbwDZzlxWD3qjTI1Zriviie92v77qyGPnrtHm7sKKJk5fHofHFkgCXZGJWL4KMdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ گستون آیدول ( معتبر در آرژانتین ):
‼️
من دوباره تأکید می‌کنم، موندن خولیان آلوارز در اتلتیکو مادرید برای فصل بعد خیلی خیلی سخته، در حدی که تقریباً غیرممکنه.
🇪🇸
پیشنهاد بارسلونا جدیه؛ ۱۰۰ میلیون یورو کامل و نقدی، بدون هیچ بازیکن معاوضه‌ای، ولی اتلتیکو این پیشنهاد رو رد کرده.
🇪🇸
الان اتلتیکو در ظاهر خیلی محکم و قاطع رفتار می‌کنه و از طریق شبکه‌های اجتماعی و پیام‌هایی که به رسانه‌ها میده، می‌خواد نشون بده که اصلاً قصد فروش آلوارز رو نداره و موضعش رو تغییر نمی‌ده.
❌
اما واقعیت اینه که نزدیکان باشگاه خوب می‌دونن نگه داشتن آلوارز برای فصل بعد خیلی سخت خواهد بود. برای همین انتظار میره مذاکرات طولانی و پیچیده‌ای بین اتلتیکو و بارسلونا شکل بگیره، و حتی شاید پاری‌سن‌ژرمن هم وارد رقابت بشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90729" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90728" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90728" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90727">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGvYkndpwpdWv8v2OD24eRqX0F2jR4hFbH9URoi5wC9WzTZK3PZ7EGEqB-hyYWxyrFFzaEB2MdlAbClukUZ0g5tugzqTueqmb15JszC6vEbvt-IUGtjWv82hQE40BwJfezj6UPG6DSnka95wXctFGGLZk_HqB9NNShG7W2pzlDkfQjF55qwy0SS9bcRsCGfzRCzDI9iFJEUIqMcjl_3P8ple1p_G2u4LxgZrEKiq2GI7x6zrwTPW6Fp8apDR7kRGdUzedLOpIR48_aPYILk2b3GyvOHdTzTsNPO2vDzI673MiEAopoWF-u4T0aZK-2o-zGRt0GU-Bv8R0B72TfR_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90727" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90725">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aC_T98uoXJx4HWGyXR_cw8IH0oHv6YZzunG5Ox_aOPXR1p1Xz_it2xAJfaXYEoFA_4bnKHyU7hAJn14MH52j6DsYhISUENACxxoSbvPFstTA9MeXc4jjP8TvCL5QyzyCka6W0iIeAbZl56Nuq4dNBXjZ7DtkUGyz4mvval6WRpETva8IqowBPSOONDAHp8BF4QxLWFu4LtoTcTlrEA9xxJaGnaVW7gH2_ZlKEqscVOQS3YDJrXlrgmCLCdpmERTtwFIDMhyEThPTHoP0hH2RLshI8il8uUT-VwmyxsQ0JzYwo-D6X0rGx8YPkdkwcifcORcjysuAzSG-kflKK36Z_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووری
؛ توافق اولیه رئال‌مادرید با دامفریس حاصل شده. کهکشانی‌ها میخوان تا قبل آغاز جام‌جهانی این معامله رو انجام بدن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90725" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90724">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj5Wx9_1QfpaYvHhK_P23dmXXLBqoq7QambF_Vh5WnS-62llObmWyN4h1fIKg_ov9ygIlkI20gsrcpa_NAT_KoElUVQhifoBuOeGfVeww-LLI-hGx9jgPjiAGD48r7mpd7_h0W_Y3IvesBp9Cx8MDjeamHImqY8oTEnE3WoRn6KCF2GM-uDuYpwaNcQTOTPlaaCq9JdIJtsvw4FqqutLmUBfCkdEy8bo-wC1bvvurcFt3sDW6cjn4G4eTT0fG7yQ8qGNDgCviDADDNdeArc4M8qbP57D03g6gAKoCbDaBMYRcgCzzMGnOF3YwTOsI2475zX4WW2mzU9Xp-12Ao5wpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ادن هازارد برگر فروشی خودشو تو بلژیک افتتاح کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90724" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90723">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تاج: 100 هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90723" target="_blank">📅 18:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90722">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b72747be.mp4?token=N6fhnq5BsGXkDNmqPp2qaOTcgUE_7jf2gNkcqT7aMt28Yt1CWrrdZzkif1ZnTaUtpfwIk2lmX0G_JdpWC1EZUEBpkPKaiWvLzQvkS5ESU6kh46qujxzs1QLTUVXLsA_sIuweErF8OqY731UPgGUN8edNk20kXv5WtiHkXDp9XFykjYxbXcYKtjaiBZpcIZVfoD9t7XCZBMINcuIN-xRxxlTf8pDXwQbffGpiskEZZbYyeeaJSenldObqo1lczkI8ah8r4XCA5TGd-3UcFcXHSpDdElQqayqcj1kFzvmVPeNx76PjVU60JSC51Mv7H8fOBPvM210TEkesKcM2UOHcH6mr6gwidVz6D4ctLotYnd-sv-AorI58-0JUd7Hacal1oaZi_Nq0GVUs8WMbKZRARVnwXKlRhkM7QFseabDz5fk3w0wQ96abcjuM3hUMmLp4NiShr0q522oa2hmdjg76k4vYeHaPWffuS0_kdsAuOvPlcq93V-y1EX7ZG0sYYDSnjjyavZ1TEPGn5nMLN3k9JCHdacOKeyOqhfcT8twitn4Fogd_ckFg0U4Cg9aL-50f0FDPdCyXNLeMLn-3mDxBXSp-48JC6AAQtGem8JBZbbFY8QTLd08xvWI_ToY5EHV-Ez1EKBOC5hXSyaFMsK78Pc-64l84pVH452ruFi8bL1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b72747be.mp4?token=N6fhnq5BsGXkDNmqPp2qaOTcgUE_7jf2gNkcqT7aMt28Yt1CWrrdZzkif1ZnTaUtpfwIk2lmX0G_JdpWC1EZUEBpkPKaiWvLzQvkS5ESU6kh46qujxzs1QLTUVXLsA_sIuweErF8OqY731UPgGUN8edNk20kXv5WtiHkXDp9XFykjYxbXcYKtjaiBZpcIZVfoD9t7XCZBMINcuIN-xRxxlTf8pDXwQbffGpiskEZZbYyeeaJSenldObqo1lczkI8ah8r4XCA5TGd-3UcFcXHSpDdElQqayqcj1kFzvmVPeNx76PjVU60JSC51Mv7H8fOBPvM210TEkesKcM2UOHcH6mr6gwidVz6D4ctLotYnd-sv-AorI58-0JUd7Hacal1oaZi_Nq0GVUs8WMbKZRARVnwXKlRhkM7QFseabDz5fk3w0wQ96abcjuM3hUMmLp4NiShr0q522oa2hmdjg76k4vYeHaPWffuS0_kdsAuOvPlcq93V-y1EX7ZG0sYYDSnjjyavZ1TEPGn5nMLN3k9JCHdacOKeyOqhfcT8twitn4Fogd_ckFg0U4Cg9aL-50f0FDPdCyXNLeMLn-3mDxBXSp-48JC6AAQtGem8JBZbbFY8QTLd08xvWI_ToY5EHV-Ez1EKBOC5hXSyaFMsK78Pc-64l84pVH452ruFi8bL1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🇮🇷
بازم ویدیو ایرانی‌ها برای تیم اردشیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90722" target="_blank">📅 18:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90721">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_3ar9BjIyODtQ6PsFrqLeHVes1BK5RqvH_4ndrWhGb1IKwAVolBzBN7k-lIJLIb360mL52Mf2_YsGiUl7T4a-aB5xJZ4Vu9BbJwx1rtZOlgqu9tKUmj1SQwbB5ujedAWjfFM7RgHnZpCeKhT5SLdTaTQWjVJvWsj64yc4Hs8J6YDdlsHuPyBHCq7MPac0Bs3mcq4QM5XJ-NzUa2bdPJHYEO5cVT9EvPt1uwCE_bgUkJ32ipEKoFYCks-Vc8g7ZB3_bwUbl95OtM7fCrNgnI0pkfbO3tAa0jSa7S6UvtgkJrtwHd8c9zFIXEtrEuX7wBjr8VQDlaxdAXm7Rll9FOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
ترکیب امروز بلژیک مقابل کرواسی؛ خلاصه که اردشیر از الان باید حسابی چربش کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90721" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90720">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyPo3_GTRFKf0sUBOuPLnIS-MHmhcFs4aYYThLqCP9y1xDeHomrp5Nf7aqeM7CwduHgfhXcviKF1vGKKAwIMf0vUgkpxMldDFC5ysSu-DdiaHkEqywjFIOwZdrbyKPxH62eHR1oBguVYEK1n5XCb_NM4DdbljtHUiObgNsqXmfwvsalRe8T25BrY-cU26s7ZFUu5eYmToN776bKITDcz0qzBdXTa9_J--AB3MI6Cep01EBa2EUUxv9tRqSBt-dmrRTjXSVFQz7UHXOPdytCnHZGwKdp2m0rvbuHF5mKZuJF6ObyYwF1wsmmn2xO5grpdPIfePhmcxzXtaOEpv8arEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه هایی با بیشترین نماینده در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90720" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA34c33KHBBuWBG3WhazwX5LKQwkJdVT6pUiqK-TIyIlXDJvem3sKZVkD6kxoiiKxzgKDTHe-Z3QPd6R3JJMwqkZjQPDJd0gni0QUIz2pyAm4g7k9mAfhHZppFLmcScxqG1epaPCD5QHpWdfr0DAwj5PfBtoND6UAr9zim3mIRRWFJwI-vchI5_NJiUO2tHtp2cTGUoTJQ6KRa7OXK0KHBgLGKwLN0QnkwjdCzsA9e9uJ38z2S3D78a6I-4ABB94DSOunAPjf7JjjyVM0II9lOj7AW4qmJc49bImLFeI5xVfz01hG4Z1nQHRGoaUjvXEpvQCf4BfmRF9nkXXstUEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
اسکالونی سرمربی آرژانتین: مدعی اصلی جام؟ بنظرم اسپانیا قهرمان رقابت‌ها میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90719" target="_blank">📅 18:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYl4b2isCMlCjYrrVB2rhIlOE04-YaSvj-6I41OWjZYoF1jwGxMBEcajm4sapnY5rVEUsTKJJjNYR5HxHyYI9lPA5aWfFovhBzES4yLqsAtHgYLuNoJo8IBl13zSrtAqyaIsWIKO7lA-fRPADWmG6pj627PuDn5kWg-5ljvvi2Dus-b9BEgRNCEd49pX2PV5Apcd09Yq_Xqll_DhlHJfIlCXVZGsffrvdN_mi_V5Hod6BucSOd_qiSMagZxFHI7UQWSg_tEFnEUsT5J9PXIakWauNM6wjlS8VjjLD5HpbMyDDWHBVFNkQf0U0rmUeQ5-MXQzUzuYnwbHTMJZjEN7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👟
هری‌کین درباره تصاحب دوباره کفش‌طلا
: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90718" target="_blank">📅 17:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47c5a1723.mp4?token=b8AtqyPYf9Weg2WX85R0IXJXJtWFtCtrtIzDDwQKXTn0HVTFdFJM3oknI239njL6kBgrywburF8i7CERuOqupQnObd9wwvUUPgAoNTl11nXo8-UxGj39V34f2kn6GZeE5BpKqqGAUvkDJ9MSxeyoKj09B-v6xKl_ZTK5ZC6ePzY8R5z_7lpwqq2d1FeTf-m-3rxG1ciuHbl0nZGtDD412aaisvyQnFlfcpXwQdEyR6dM2GtanDROqyZV_U8FpPNKXBhbaeY-UbVQ6nh4vYwERXO-cB0keNfnJKV69UFwppuW-v5zN57qUx9C9ZudKVIVP6t0QxamamljwvtdIDfJHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47c5a1723.mp4?token=b8AtqyPYf9Weg2WX85R0IXJXJtWFtCtrtIzDDwQKXTn0HVTFdFJM3oknI239njL6kBgrywburF8i7CERuOqupQnObd9wwvUUPgAoNTl11nXo8-UxGj39V34f2kn6GZeE5BpKqqGAUvkDJ9MSxeyoKj09B-v6xKl_ZTK5ZC6ePzY8R5z_7lpwqq2d1FeTf-m-3rxG1ciuHbl0nZGtDD412aaisvyQnFlfcpXwQdEyR6dM2GtanDROqyZV_U8FpPNKXBhbaeY-UbVQ6nh4vYwERXO-cB0keNfnJKV69UFwppuW-v5zN57qUx9C9ZudKVIVP6t0QxamamljwvtdIDfJHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو غمگین و تاسف‌بار از یک گیمر ایرانی...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90717" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">علی تاجرنیا ظرف ۳ روز آینده مطالبات آسانی رو پرداخت خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90716" target="_blank">📅 17:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laihPTqq5tO_7rQ3f-3AoHBRYcpzRUPuN60L8DXapxTNREnegNlU8ZJIzardghU0tz_wwhnzuyKJ4MBHLc9GqKYKq6_8HYLlqD6a-wfE75ljG_LktNLXnX_QeO9omjnWtugD1bZ_d6LD42X0vsDq8aYJmxqrYCYGF8NSEJX5FVEgM-u1vYCbQwZpKQBJUhyCztSexL0zfio3JiiKoyWxAF06TvGWt1rku20XT91VcDiXjPZrhNXysaWqVG-K3Of-KSddv5w_Lwmxqo5Zp0h5tWkptNDavdawOCoUkF5NIYNcAvmeAfaUxVxrTZ9aAJ7FAfSoTFCBmUng7uCf4Uyn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
املیانو مارتینز : اگه قهرمان جام جهانی شیم از فوتبال خداحافظی میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90715" target="_blank">📅 17:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeI1JARuzhQ3-2PDfVYHnVGSCMl2dlyHozUsVfDaPSP0Xvt4s5xqHDAQYUBVRG1MrqihPE8PzMsHl_-V06azZtPnHiFhy90btOCSeUvPt52el-EvMpHyU5ZkXUUf6TYsrZ7N5ZgdiOro7cH0m3oROsm26rzYRzQXRVESKZVFIsFsEM-WKpXFY0KaqFQY4M7BIoGj7SCfOIiCMdQ8M3-ytz95QKGHx4_atjqnekWZF4huFF6Cd6tkY5gd3ABeKXQcRhmVol883BxDJApauP6QtyQYiVN7OmtKF7r32nNEyQzzJqjLk7VBaC5ukx5WZCHS5twQkkKc5X3GxImh7Co-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#غیررسمی #فووووووری ابراهیم‌کوناته مدافع لیورپول با عقد قراردادی ۴ ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90714" target="_blank">📅 17:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=kWErxnWkLRwoyAQsNb5YRYvwferkqwj5qG9Hl-MBZJfKm5MCjgq31-yZfGMQktzkmCsu8mDYaKanioCgZlI8iy2rqF2sAlHV7WvnutPbJbij1Q7CXw3p944LTPFt-WYbWsEO4OO3LpEZXrUKg05yk114CqIpL3Wi6oBYH7R6suiJQ9qKfzMnULJefrttwoUZpFjICLg_I_58qwzmrEUJRmBw3tI8vGG_0zVaaiFORlwpqov8xaOCbM9itDp3ogMyUsPObfYfpTo2nN06rLg-7zYXgvuw96Jf8w3P48yW0KyilCG-AwC3iLxyJNvwRXBJmru-fhhnNGX45DmlBqmLww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=kWErxnWkLRwoyAQsNb5YRYvwferkqwj5qG9Hl-MBZJfKm5MCjgq31-yZfGMQktzkmCsu8mDYaKanioCgZlI8iy2rqF2sAlHV7WvnutPbJbij1Q7CXw3p944LTPFt-WYbWsEO4OO3LpEZXrUKg05yk114CqIpL3Wi6oBYH7R6suiJQ9qKfzMnULJefrttwoUZpFjICLg_I_58qwzmrEUJRmBw3tI8vGG_0zVaaiFORlwpqov8xaOCbM9itDp3ogMyUsPObfYfpTo2nN06rLg-7zYXgvuw96Jf8w3P48yW0KyilCG-AwC3iLxyJNvwRXBJmru-fhhnNGX45DmlBqmLww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
یه رسانه فرانسوی با انتشار این ویدیو از فرصت سوزی‌های بارکولا نوشته که این بازیکن جقی رو باید رد کنیم و یکی مثل آلوارز رو بیاریم!!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90713" target="_blank">📅 17:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90712">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLlo-2W7zMLzzAZaVGCTCM-5TO0yA-pIeLCBjzUwNi4PLX-201D_JNqnqNG_eycgUTJDzDgm7LTWQxAFdZES0jZ6bbKs_M26YkqfB2d0tAXkoxQe6JBq3KHgys4LCYItzZuXvdjtqawMaVRtX8-hPBS7I9rzBkH0t1W7rqUoyNa5ziWmOveDjjQG_pkCgLswFCbg5iuC--4iFwGM5RKM0SaQLZEigF0Qj_7kuLkjTi9I3LNkIBd4MM1D-OnsuFklHJB_zz_1UcTQVydQtR38h9achwGleCHjbmJds6me-GOLdD6EIpb4f1k2206NvYa7Iat_UNaI9WJVhFT5BeSEUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
شماره پیراهن پرتغالی‌ها برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90712" target="_blank">📅 17:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90711">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqPW5DPLqcEdlsKsp0DEc-2a2OdcNUxlOW3Oo4EcISbhQfqcqdOQgWxu1tgsZp0EbXCUJjF9AfU1Ih_EKhbjo-fDois6Xtoc4Lx8UYnmC9v-qLONaxlEeSKJ4wm4MWpVMmToYRvI5-GeouqkIi7OarJWot_XtdwnXGuFXFAH4ji2WZL54jndp3xAF4v90wWlN8slHhNF-Euwd0qehxr-qi2_qHakBQAYeruJ9KpoxXnGW8Zfyam8J6JIcngyfFOLu9_8vxa8gvOZAk3nSmvhmN_inZ-aAg3x0TgjCLbZx5W2MsR5cKuiVHVmcJigWSgfrQNVkNaIdsYS7zFIdjhi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نظر روبرتو کارلوس از بین نیمار و وینیسیوس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90711" target="_blank">📅 16:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90710">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805387d840.mp4?token=jL-G4bHJaFFWNCLdJgUA1JVCK-igTTjb1MDh_7ShTpqbgR0zC22MiRnPt2PrAi8ftiHm6ZmdetlNGc8TMUSGR6n0QmnAy5mnDV77YKHrf5ad629TUDu0eVExf8dmjFPWukhjvzHhOXRLnlDPqsg08Id80yhMKe4LRdS6TVeV3e4XgGyHaV0lDHVNvyHeLU-V5UzH3jvFzwBTKiVcWeYQpk4Ks9NeaXGtFo3l522quL8Ibs5aKGLv_633WzUJhAXwoVuoFBp8X2lq1-1_qUKh5AwvJMyjaQgUpw528svexsGvVZlvtfWMbvf9tqC-AUn2851vc_tTTq8mGFASb1drrxqGGLfUE6NG6ZzR24eWCkubKEH_nwVWXT8yruy52VNQau0CeN-gsjg8w0EM1w2TcLY68LjgMg2LoHdSfuyQlsTikA4fLh43mB4rtTiTXhCXM391Gz_mX0GC06-ZGxu0D66u5ZEMnB4Wt6jfmMtiDicUKeiPZrOoLbUSOc3t51a5HMfyZWsIV92SsFJDgquIWJCkQIEAzoQu3KmoFTuCfueyDaRo_4odNar1wFY7-K2DeGUQ7Sf5aerrE7gsO0M4SEcE58B-BFrvrwJ1UtMRwyVk2D-6jaWuwYWhxYGVu522FMt3JtSWE0TN9eHgel1xmsMlp5_hsobgIE13LVMx0TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805387d840.mp4?token=jL-G4bHJaFFWNCLdJgUA1JVCK-igTTjb1MDh_7ShTpqbgR0zC22MiRnPt2PrAi8ftiHm6ZmdetlNGc8TMUSGR6n0QmnAy5mnDV77YKHrf5ad629TUDu0eVExf8dmjFPWukhjvzHhOXRLnlDPqsg08Id80yhMKe4LRdS6TVeV3e4XgGyHaV0lDHVNvyHeLU-V5UzH3jvFzwBTKiVcWeYQpk4Ks9NeaXGtFo3l522quL8Ibs5aKGLv_633WzUJhAXwoVuoFBp8X2lq1-1_qUKh5AwvJMyjaQgUpw528svexsGvVZlvtfWMbvf9tqC-AUn2851vc_tTTq8mGFASb1drrxqGGLfUE6NG6ZzR24eWCkubKEH_nwVWXT8yruy52VNQau0CeN-gsjg8w0EM1w2TcLY68LjgMg2LoHdSfuyQlsTikA4fLh43mB4rtTiTXhCXM391Gz_mX0GC06-ZGxu0D66u5ZEMnB4Wt6jfmMtiDicUKeiPZrOoLbUSOc3t51a5HMfyZWsIV92SsFJDgquIWJCkQIEAzoQu3KmoFTuCfueyDaRo_4odNar1wFY7-K2DeGUQ7Sf5aerrE7gsO0M4SEcE58B-BFrvrwJ1UtMRwyVk2D-6jaWuwYWhxYGVu522FMt3JtSWE0TN9eHgel1xmsMlp5_hsobgIE13LVMx0TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تبلیغ جدید مک‌دونالد برای جام جهانی با حضور رونالدینیو، یامال، هنری، بکام و سون
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90710" target="_blank">📅 16:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7hk6PelD0V7nlnvfdFg0g3A1gqxTNcuc_PmslCuTPEX-FDXaezx9EawCpIhrtJHUGCM0CgQzEBfazlIliaGUX2bE6xP9a3ec84M-bh-1xISvNVAjWEAmb5z7OAda1xxeZYS3-OkOowg-NejXCri16-vA0HShpX4JJATjLGlusmTdP_7wdc6M7h2r_EzMZMAysx2siBr_BUmqnn68VABKs56CTSJV7jGItl2Bal6R_2DgQV9afDIqPb1SCYv_UfzjFEH6HOneVFEIbNSeJ546eFdUabyQLTcdN2MJ5WPPXJm5vaKXBQRuqh0p_W0EXMrqbErGugLFhsrM120pvnrqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#نقل‌وانتقالات
|بایرن‌مونیخ بدنبال جذب اسماعیل سیباری ستاره فصل آیندهوون هلند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90709" target="_blank">📅 16:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90708">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py9wQOnPfaepSxCDBxquVwzdmCftT9xpqTWFS0RTsBc7Zeq62c7bJcfFt9_bWEYScDB5unPWx5I-ooceQs92cDPHUOZrMZtQb-awfQ0vd1zZShoaDZEZeNmIUFJph8QipyQAGE3Ki876rFQaNG8QJ6LxZBfxLbeSd2KX3KEaq4VVspBm3A-wW2yBPCyf5oMgz7xGPbxLtJWyUmW-zxa6udBsRYS_9sEENAa6c-D2jcIWbIA1MK7piPEO241KR9mvYnCz1A3PHG77XChTKDwWB8iQWAWO52LjHMF6wJuG5DboOwGnLmB3ub2WYPQwn8NnW2NvTz1SWbQRSz1MaHFwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#غیررسمی
#فووووووری
ابراهیم‌کوناته مدافع لیورپول با عقد قراردادی ۴ ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90708" target="_blank">📅 16:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90707">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRQD7Mntw-ltsI7Fjgyo7Br_tbGvnjVmPTx3gWyvDCYzl0u28DWwsy3OZMTAPmxoxv6YGItpusimNWT6c1x37xHuxxnkIPPQcU1Og1-5cLyXAjbSm6Rir9MHRZxm7uHdcYINqJGvX74-XJPZOeK3c6OLUQT2r9pRRUeYUbrlH_eiQQ3xrlpkEceu99v4x8lWG1Hk9RSjprT2zqT7Cf-OJ3f4IkeK6U0rgyynY1JqgRPKW0wnN6jULaJDUThhaQumrnpRwy2oZwFj8GLZRtRE-q7KmbDt1cG2xeeVljC6jkNDnA4Z5w61rAR7MGZWLzqTRiONtMk6kh4KGz4e6p7bvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منتخب فصل لیگ‌برتر انگلیس با رای مردم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90707" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieSujuBYD__y5HT9iCijKREfyPv4s49E-8XRPK5VkkW2SF7_91deYM0IfvLrjC_FMTOwI9RRmUifr8on4276lQZG85kR83KRBX8WBhBFW5An39yDbpyZbVpkc14LNWE42Rg9dHl6IJLfpw-feS8v-uVIopmTdejwU0pbh_OzHfGBP-csDqjF71Oltm9P6XO9EwiH-Bzq6bxh2Fx95MySPpCQdoALzM995ulDKNq4Ec1cqHJMRs4LfkGums8GhBmElUhYDVzwMBXkG-4EVuXZ8poR_kWsdEj3bk77jStQZaew-1WDKc0z01WKqUjR_7b5UJyFh_G2-OeF7s4dlvLx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
عمر مرموش ستاره سیتی هم رفت قاطی مرغا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90706" target="_blank">📅 16:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90705">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dliRa2xwYglF4IUHgO7EcLkgnUmqEoU97pQrzN4h137HyAJ4gl6hw_VI1OAehnF7As_wHcldBImjQ8sTqEQ0oyYn6sp-zJO6GJxJOdbWo-UtXGCkC0UwL2ytCbxKoMQLqi4ghJgndJTlyiIWfpmg9oQdWlFXbB3FJO9wkcEpXDcmYx8iUCwA7jnK1FAnoqFYm-paUEaWWq4TINv3RqjK9H9X9OxNpRv64MwiAjyLijZEBXHUbKGZoKesoXpvoYLltNqiOAUZq0U1aj8-0ScMDxhjpTIwkiC-jOX0w9KG7_u5cthWPzu_KtDMzLkq4hlUYu0yTWBIcml1WLO44AjIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوار جام‌جهانی با کسب نمره ۹ در سال ۱۹۸۶، رکورددار تاریخ شده و‌ تا امروز هیچ بازیکنی نتونسته در یک دوره از مسابقات چنین نمره‌ای رو به دست بیاره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90705" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90704" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/90703" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i76SEv-Rm-50GvnVReEQIyFuLcOLB8voJb8I6ukZHqY0mksSvsMP1KsNWuhR_2WIcbj7etgJr7HV0HpfoMYOLZEg-XmMtke0JzhNbpSnWIFODtlMAFSjSc5K03esQAchi4xB8x5pmeXb--qP_ctvaaS7322f8YqLacUjYYC4mUGg6M5P8cDgP6kf19MzvBXwhPtqux54CPTvKAPii50culH0MyBVSbJCJPvGJGN0B55fIoli4VFqpyMPdqkeEer56HaPT_EwyDbRzo_EkeUI4ZaqmDSaHG938B8ubTCvU4T2uHO_d52tF-Pslu1Z0T41HjnLqCFTyn3hy1RuahvU4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👀
اتاق شخصی لیونل‌مسی در کمپ آرژانتین؛ مسی خواسته بدون هم‌اتاقی در این رقابت‌ها باشه و از دی‌پائول جدا شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90702" target="_blank">📅 15:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b52d4c89.mp4?token=s4yUdRwdkdIh6P4k3Lqcvvq-a9nsD0pwYuT3vyDyxJ9QtfWGotjpp4AQG_-1L2j52W5KIjtWAUJKhIFDU630vieLWr8rb1Fo940KF1VH0LsGhM15sKy4ZRzBBSaTgzPhg3tbEmbgZeWnC6YaBQi4b-8wZHuJRiI22RKVBsaN10u-LoWqeP8dtmb3FF7Gsl0f9kStZa06Emc4VbPXVtGgl7Nt2Q6XzwpwISJC25lxpATjCSJSfeTlxpv0KSU7eEKm1tAwxfKR9X6TnkxgiaTVrWnnjKTjsz4gLNTTvAOmmz5FCbePsYiP0ZI0o-ddys9n40BzJ0p_o1L8zpx9v-Jzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b52d4c89.mp4?token=s4yUdRwdkdIh6P4k3Lqcvvq-a9nsD0pwYuT3vyDyxJ9QtfWGotjpp4AQG_-1L2j52W5KIjtWAUJKhIFDU630vieLWr8rb1Fo940KF1VH0LsGhM15sKy4ZRzBBSaTgzPhg3tbEmbgZeWnC6YaBQi4b-8wZHuJRiI22RKVBsaN10u-LoWqeP8dtmb3FF7Gsl0f9kStZa06Emc4VbPXVtGgl7Nt2Q6XzwpwISJC25lxpATjCSJSfeTlxpv0KSU7eEKm1tAwxfKR9X6TnkxgiaTVrWnnjKTjsz4gLNTTvAOmmz5FCbePsYiP0ZI0o-ddys9n40BzJ0p_o1L8zpx9v-Jzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇿
🇨🇦
درگیری دیشب بازیکنان ازبکستان با بازیکن کانادا بخاطر تکل خشن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90701" target="_blank">📅 15:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwWdm-NX-bkzON2La6WzRFfE4TlLh4VVFGv8hS5cpeaQEDH_6hICMvA4FrFO9m1S-RSvmb_RkIx2gW5J6rjzdgO-MD81AN5rZQFLdKSWDsHv_Ar8hZxqPdwzspdmF0LxY6wFOWXI926kj95zwhzgC5Iq9EmqWRAGJqrRMMiA27v0gBAZ_yMiGm_GHsy-dbo0BGB4ZKxkdHTD-0jO_VMPyNXYZ25GKkNrpnxW4OqrCTZtlBgUqCazSXL8wxKC7lF7bbOBv20VprICk09GUcuBOxjOF6kp15OEBXBGLqvbaBvsUo4zVJguvhYUmTtSRiaC9ZJ0oyNWnFrI6VeX8HLDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
یادی‌کنیم از سال ۲۰۲۰ و شاهکار پدری در سن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90700" target="_blank">📅 14:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cab41e786.mp4?token=gShQgGS1PjgVn8MXhXIpiVtvfUjpl6oQfvIf9uvsps_UGVE9SXHW1mnJeB8kbebjV7wMaXvXUWUpSzPIKruf8VzbUUYeKMhv20ebzfDvhhWTYrkBVoGsrzqNpnpYbDGy0y9BeOecH8cktk9HFNl48eHFMYFscqqG0VDUf0Vgqf_K9lu3BHnscQexwHW0vI_z2myL8Ys4klKr8KIH9Bc1V9Cackrr4Fi0OxXlhRhC7Ns72e9C_5Yf7ujdXScS1KKx9-Rx6UEGcTnTOQHnXxaqqFtnetOYyxmO9ZaRUxky-sbo9-sUThYZvwm2ibaCC8agm1OXgCMqAef4E4xfxDk5-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cab41e786.mp4?token=gShQgGS1PjgVn8MXhXIpiVtvfUjpl6oQfvIf9uvsps_UGVE9SXHW1mnJeB8kbebjV7wMaXvXUWUpSzPIKruf8VzbUUYeKMhv20ebzfDvhhWTYrkBVoGsrzqNpnpYbDGy0y9BeOecH8cktk9HFNl48eHFMYFscqqG0VDUf0Vgqf_K9lu3BHnscQexwHW0vI_z2myL8Ys4klKr8KIH9Bc1V9Cackrr4Fi0OxXlhRhC7Ns72e9C_5Yf7ujdXScS1KKx9-Rx6UEGcTnTOQHnXxaqqFtnetOYyxmO9ZaRUxky-sbo9-sUThYZvwm2ibaCC8agm1OXgCMqAef4E4xfxDk5-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از روزگاری که مجریان و مهمانان ویژه برنامه جام‌جهانی صداوسیما برا خودشون یه پا جذابیت خاصی داشتن و کلی مخاطب این برنامه‌رو می‌دید...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90699" target="_blank">📅 14:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMkeEWc5rCKwYZKUZEz4vY9_O2W8d3qSk_Qt9qvc64NOGaqScsotFaZbDpZxY52cdamaYLlZwsHHNhiI6UTvmBQqG4QyzvjTgGBVeu3TC9V1N1RuoiA13vuqnIqkCWLC4E96m_8rDt2_Vb0DUEp4XPyglNXQ25m4ZhOLjhE5azqMWaiJZBzgOVwEU3Pv_-r2WJduT1DLWJMalLKWX62Fym1dgliOpGorGwgZwL4sllA5ir4gqGQpkxRGqUFnxd86btFpughgFd-K4HkCT9GTXFkCGhele1DOGHAMcBgXb8pPoi9UzrlEKTWQpBVRwsj25Gd2jKwzmjHAS06z_IttLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🔄
برترین پاسورهای تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90698" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90697" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛑
تنها سایت روسی فعال در ایران که درگاه ریالی امن داره
💎
شارژ دو برابر با کد هدیه
IRANBET
برای بونوس ۲۰۰٪ این کدهدیه رو وارد کنید
آدرس سایت فقط با فیلتر شکن روی سرور کشور های آسیایی
👇🏻
derbybet.org</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90697" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCtXsABtdoq_ADXnXT9obfKUr4qU6wemRMdig8t8Asn7cpkKmf8WX2fZtuXfMC2n_ZVn-ulmrv6O1s4popuzYWo9htQyPRZ3RHI-fqUbDzJ7pc97bpjjVzMQaybBcLrAooV9eEB2Xk7f0yav6-cSmoQw3KhpcI6S2oWq0xHUeC9Eqzm-cP710TY8RyNtFl9Oz_6wBxcvM-02ZuvsKVwNPwGZV3vR7XNfUXDMY_2VNB9QWa5nfbFd9cFpU_PGOj3LTVczo794HZYG-jLutF47ADZ2mhDViRox-ARE5SFWZRRtNqwmndTTteMOf2A0X0o8dQ2Gc1BUYpq93NJgayUfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
Derby Bet – تجربه شرط‌بندی در سطح جهانی
━━━━━━━━━━━━━━━
🏆
دارای لایسنس رسمی CURACAO
💳
شارژ حساب با ووچر، رمزارز و درگاه بانکی مستقیم
💸
تسویه‌حساب سریع، امن و تضمین‌شده
🔖
آموزش گام‌به‌گام برای شارژ و برداشت
💎
شارژ دو برابر با کد هدیه
IRANBET
🎁
100%بونوس هدیه واریز اول(
شرایط
)
🎁
100% بونوس هدیه هر شنبه (
شرایط
)
💈
آدرس ورود به سایت
⚠️
💈
دانلود اپلیکیشن دربی بت
📲
💈
اموزش شارژ با کد ووچر
👉
💈
اموزش شارژ با کارت بانکی
👉
━━━━━━━━━━━━━━━
همین حالا ثبت‌نام کنید و تجربه‌ای سطح‌بالا و ایمن از شرط‌بندی داشته باشید.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90696" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90694">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwBSbBfALbBdPhSMAUU63JC6bW_A6LpkVDDwmszQjp-FvQF8lidHxzxUleKoqm4QeaF7YTWfJK6wGf7c59kHsKVPm7X-BEytFpPz7B7q9BoMLpyIqx7hEbK4WIyGcRiZ_amDxP1_DLeVqxR-phqCDmg5t5ygUi5KMt5dUHJpgjOmHkG93cHrnSHCDDjyurOQRZUNWyRcArz5uP8wxb11UNiCFmo8-Bz5yQJXa2boDKSPBqD2xGTeYf_NOjgfKRG4mqGSnMRS8846QvmVPRhoF3Ol-2RfKbKxlBpU6dqMH554jntdn6fXUXT4OJ7RMWM5sRlH3M3onEbpqZDU-fpJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
مکان کمپ ۴۸ تیم جام‌جهانی در یک‌نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90694" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90693">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری؛ کارلوس مونفریت خبرنگار مطرح اسپانیایی مدعی مذاکرات بارسلونا با اینتر برای جذب دامفریز شد. ظاهرا فلیک نام کونده رو در لیست خروج قرار داده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90693" target="_blank">📅 13:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90692">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUe0wujROI_x-VvDLLFzhE7FsnjR3qaAAjFC0MdDdm87BwfWwxTO-quwbaBcjdX5Dz-vCm_0xnOnxVU_DV-RpozJX5vsPuhTMskGo-lepHCbVv0pDn8Pv668l3O4ysqIqXYrnuE8n_bzdRoVJfMDXRSuKWFYcEHYYbWwFqNR-MzKkA5clSFNYhm3_jwNg58ugpIFMwe8v-osqdmGPn1MgiK7I3qiy9t8QUASx8v_MGDWb1uWe4VDLg-mZK5U5VItf_tU4ENsfqp5xQHkoGRR_L6tA83rdH07J3rRN_qeZOU2-n5wwfct4U--KrBXezOnI1dNB2trccJrHnWPMlX-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
با اعلام رومانو، بارسلونا با پیشی گرفتن از رقبا حالا در آستانه عقد قرارداد با برناردو سیلوا قرار داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90692" target="_blank">📅 13:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90691">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mo1Hu1SDOYBo3T2WR8DuAUTVIGGFKO35IRd8RtA-62uwmb23eJSVvtpAxOkYCFuhLEfyR9yQKSOE9k0bZ1bPd93_Evwjx8dhyvEGU7Q-G5AGZshCboNWa6bTiWNk39_d_aUmTc0W-7hBIdix-TJ-ymkYpxR3hHejKGEcIvrTHWJbgw1gazAofQS9KGgR50tflc2AXdMhNWO2XOfl3Q84MQ1gKgc_UA5QHIl1Wtv1QyntmJ9HIaEE4OI4gWteNHlPKtmKe3qJUTXA9l-pXgOSsw1CvUzd7t4irECZydD9rO-MB03D_BIvJf1BYeKHOeQaYT605iUSTnrBZAwZFqJkJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
مقایسه آمار این‌فصل مثلث هجومی psg و آمار لیونل‌مسی در سال ۲۰۱۴/۱۵
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90691" target="_blank">📅 13:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90690">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWFp3JUARCzoaZU6cxBiCNvKO_bgU3l9c1frA25Lil6ARLxiDkqHlxNejU8ZbVJGXX19_upu12nwRmCJOZ1nqNmoIqyFCiJ0UXFnexEa085DhPUwzxo9CxmGNXXI2lg3D-W8-zp2_haDPgjIUSJfwwbslB3vs_NEjmRkatkNJ3_m8Q3mwMpUe5pcVujJM19b8wgwsgmaMHuEnfSY3dZZZez5EEeUg54GDbQfKhEkn-1ufEDQt1MRsGmqypCyS-RsNcVEqq8TFEgr3LsogcufjdRTtSeLr_It3qulq_XJb2Pv9MMnom5ACwPxH-f4fqpu8Td9lcwZ96nHWZhawFEYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇧🇷
نیمار و مامی در حاشیه تمرینات برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90690" target="_blank">📅 13:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90689">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90689" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyP-ZWNOIgtmYaRFyiv-CWTCmh6OyzZoOHA5pMXGqkCyoU_mPgBBMIGUl3Xhf30z9c0lDpTLCeR6qVa0kMAMTjI3Hs-o25y7osTlw0YwR57kqGrMp03N3on4Jxm_qmg_stTocB9FXAAiIBrITT6A8rN8Kd2i7BSrilt_bdjcyVXc5keoRTWP6X7-eTgdOFFcgYaTVurYTA57_tTBrqS0DIbKya_0AxHk-tKDK02poTNsSHWQdv5I-qwW5sdT3bdaJd99AaFn3fIh8JG7ofpZB3Rl0d8n5ibwKQdP3xM51SvM9Vb5yV6dmXB1bieEQ0hPMrKUQIltaj5-_qSLsb7WLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90688" target="_blank">📅 12:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4tbyZZcFGxZI8V-hB3hbrCzGW_ynHVQlNC7Ye-g_y_wvl78G8zEVS4tfJT5QKiJgtHtj1AABk0q1VdojMSP2-vUg21RY4YSEW1uaFf0yzcSFob2w3YKBbgP4MZ2h_f7fUHYI5BXJxgMQU3hqBvFGC7MMCxlHok6MpLQoibWvi3PMECPsO7GV0JQ31GWXoWckCZsyTIPQ9rR2TggoEBZd-mj-mwt6_pTeT-FU8dANVLbE681XUrQLSQ4KV1tddfH0coO7FCGk3IpVEUIbFII4kupH5t43aWkmMvx1xYPen4iEoux98gmkBKkrjxS5uZxtYwQDm2HZOv4QDz4hLVrVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇹🇷
لیست‌نهایی ترکیه برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90687" target="_blank">📅 12:49 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
