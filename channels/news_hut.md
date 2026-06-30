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
<img src="https://cdn4.telesco.pe/file/GqPjsC8fnTI1h9DSArFKyY88nYzUyyqvjWsQ9SxBq437Fzqp6aUmPkOzzCCvCjBeI9U-uXU46NGm5xnS74JDk9LkePyhw7gqtSqVaQUyilEEjGwGvnwlM76e6qplViV5nMBE-raX6lXOYOamZqtTgQbb90ofL95WAgHHk8SKvE0D-2VxYbHqWln6CXD-YFQl9kqn318MwjgNS-EqBsXp0PCivfHOEZF7Eay7rTI_77WzYe7_Z4r0oCop7Ewxw20CGSCH3GSUe0x4uXQts37EeIFxRWEc-HQcPgaK9I7K1hIcS5f_WczzseyajQklgbf5zvz1s9kjF3JwrlzTECDrXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 217K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 10:19:16</div>
<hr>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=jgR65WWOJ9qzeBC24slhDzfjZGIxliCAIqBVrYJWkvASLr49PxC5dqTkWlL2gq-92VnI96QdgcN4Jk4cP3ByW1SFCQP1-RT62MUGNhfdCZKtVdTUtuQERmimRaRkdG5bljiRTH-2B2BiIk1DllEYy2PDjLgQjdCac-xLLACB3a0ykT87aAZNsMYK2K17XmRC-D3wY84TiVOnjuA0BTrpijZzbz1na9laVGHO55OOYJS0a4H1SeRGYbwTp7Lg6MspQXHgcuOzF9gwkn-_BsP0gzHghjjouCiYLnDZ1cNy_khgjOhSSQzZhMAmXGCiPe91vtUsCelbIXfk144BhWQxzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=jgR65WWOJ9qzeBC24slhDzfjZGIxliCAIqBVrYJWkvASLr49PxC5dqTkWlL2gq-92VnI96QdgcN4Jk4cP3ByW1SFCQP1-RT62MUGNhfdCZKtVdTUtuQERmimRaRkdG5bljiRTH-2B2BiIk1DllEYy2PDjLgQjdCac-xLLACB3a0ykT87aAZNsMYK2K17XmRC-D3wY84TiVOnjuA0BTrpijZzbz1na9laVGHO55OOYJS0a4H1SeRGYbwTp7Lg6MspQXHgcuOzF9gwkn-_BsP0gzHghjjouCiYLnDZ1cNy_khgjOhSSQzZhMAmXGCiPe91vtUsCelbIXfk144BhWQxzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=mgr64ty_WDCOi_JpVQRdPorvKkS7AZtdHYB5p8UFhqM4p8HAaqcTwDrvqJXZdqFtKxsI-5TDgribocmM3J04cxtDgSFH3hTDAKFuMJ_o3uScNmrsMDEd64UDfi0hKBTBHjKb1O4_4nrcdaqNF94QqG21bGalb0sXhuwHrygbwj9Xu1DsmCYC1ydO0eg7Crn66lNvtmX3J45wm-pSyEzjn0HOJMZxm1_wFpGD6aPgTyU1AlKvYfOD8wpa37tX6jaMDqZpKlurFdswlVftljxAYJB2h3dbr72VHvpqtws-kheHi7rKj3jD8JqIMKDrFTAk--imKT73Ajhzd7Z2NPy6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=mgr64ty_WDCOi_JpVQRdPorvKkS7AZtdHYB5p8UFhqM4p8HAaqcTwDrvqJXZdqFtKxsI-5TDgribocmM3J04cxtDgSFH3hTDAKFuMJ_o3uScNmrsMDEd64UDfi0hKBTBHjKb1O4_4nrcdaqNF94QqG21bGalb0sXhuwHrygbwj9Xu1DsmCYC1ydO0eg7Crn66lNvtmX3J45wm-pSyEzjn0HOJMZxm1_wFpGD6aPgTyU1AlKvYfOD8wpa37tX6jaMDqZpKlurFdswlVftljxAYJB2h3dbr72VHvpqtws-kheHi7rKj3jD8JqIMKDrFTAk--imKT73Ajhzd7Z2NPy6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=rVpaYKRm49M60F6Q5ECyJQCkdX94tuVzJ89yPWEt1ieS8MrRnLrde-SuGogRdOELUa2cj3bHc4aEm6YO2V8pYhk_8cyASyTGwTqOrod-tYkbzXwi5p9zva4olIEAhfhYCeQVus9TrRTzpmOK2Q3frGcSyTgZbJ6315qdm2DBNIqIZ-SY6rmxlospZsZ4ITHycSuvYcoSLm9Bx63bEMz5dgNfgW_YfsLw472r4CCwu8STLDOPIF_-zifIv0aGhiov4LlU5z_J3VC9Hv2AYBsMfkJfYHIezjPYAzwBoDw7JbwyUYXQAkb7QetiuN3VU0jB-nhR8FRUu4rNQhpaTBi3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=rVpaYKRm49M60F6Q5ECyJQCkdX94tuVzJ89yPWEt1ieS8MrRnLrde-SuGogRdOELUa2cj3bHc4aEm6YO2V8pYhk_8cyASyTGwTqOrod-tYkbzXwi5p9zva4olIEAhfhYCeQVus9TrRTzpmOK2Q3frGcSyTgZbJ6315qdm2DBNIqIZ-SY6rmxlospZsZ4ITHycSuvYcoSLm9Bx63bEMz5dgNfgW_YfsLw472r4CCwu8STLDOPIF_-zifIv0aGhiov4LlU5z_J3VC9Hv2AYBsMfkJfYHIezjPYAzwBoDw7JbwyUYXQAkb7QetiuN3VU0jB-nhR8FRUu4rNQhpaTBi3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nwE5adGO0A2e4t-WOKYdZvMgzGnpuhb6JSU6yE6EbzMcOIbuiHDYbDh4P1HSmt-P_yabtcpdAvCvzf_AXUkF0hfXj3yI23mBCpoHkX3eOS-AG4TQELepD8DDOa8eGy27rX4wGWmuDfhVarp6ctp7_bbL6THhXZVUyqoMILakcBkRrC9qTgIOP_-7s66Y-GiyFmNXF9neHRNw9FrguFAYHxRPnDgJLFidVrFA8_RxOuHHVA_t41IKOY-wBDXRJLbKbOhfb34hZ_icHJQLq-0XsJhQ6HSr7ScC9ReOMMUVK3nxXplCUJzMZBvkBPulagKP4oJC2leA1-xy-9CeatnHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuPm5O56Hc8vFKDluvi7WZbpUa-HQsqw5K6C_hAH90F9XRGhBA-QSaDf0Q4H4mwnZMuHWAQRmF5ntuM_wD4Kc3UIfbuYzjvF4mSnYEF31gHmYNWb93gLB9RRDJi3-IWd3eOTqdKS0xGdY_DbGXpsMQqvg0Xidv20WkcPckBW_feplOrjbUrLK5zmlkFp3owXs3fkQqyo2fJBVkpFsNPjcIGLIWoqEAVf7sen7ExulsDnOvSA3FcFo5LTCCcbw64OEGb8IYV5Tcd8EoSiAc0uHfQe0AfrlDtA_Y66ghWNlo55RgM28lDv--5ccc2mvqvgIEQ6O_OF76EQGgYGHRNHUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1VvbRhQieyeylbv5sAEnvXBPih27tSE-OT3hZFZmfKSR3ZQ0GBdDBEa_ProVn2yPJuvuU6xRoY3j3YbVnQO-OlTdYTDVZY4DyQzK8ZOZDSG0Y6MjIiYkLakeeJ7E9_RMEWv8y9cc73me_BdhECmnZY-ue10qp0ZG-IxGGgGyVDjZyGqtnuxeqXW-SowGBquYH9gAEICMUgxfXeWTzSuQqOcDjUsgH1SAxWp77KFROsOLWCAqPY2LoBe35YwVoYCkd_OwLlR4GVDAPfnxqAPsfYQI-aletr0DSykihRxe0ctPToeU9vEBJTL28jPMmvChiWxbvGqEHBiDLS4VVqBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=YmYANDidpyWG7Ybuo9dO1W8mmaBojoO5jSnx5Cxlyvr-2kZefkygjMfJ6wgQrQX4wr18CKGEGLJc0ZtoRq_CoZhdO6TytkrwGSoHtOMoVsvsdWz_kIOomcY6kVIThDCAaLAiHnf8otrFo3U1RBweChf7aELN_FvbzoHl1QeLaUwLg6A60U4JOexF2h2SvsX-3Nmss3cq4QozTRIJPqFT7TN7nON675qqjDSlmCKikC36kqyivbxovWUnzyvtuFq4wBRcJRFjT5bEwKXZipFQj8vXnMmZZXbHbUqJ1lUFeCp4jxRxQC0okSDhaQonRYljNsq4v2LM62dCmMN-QQyIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=YmYANDidpyWG7Ybuo9dO1W8mmaBojoO5jSnx5Cxlyvr-2kZefkygjMfJ6wgQrQX4wr18CKGEGLJc0ZtoRq_CoZhdO6TytkrwGSoHtOMoVsvsdWz_kIOomcY6kVIThDCAaLAiHnf8otrFo3U1RBweChf7aELN_FvbzoHl1QeLaUwLg6A60U4JOexF2h2SvsX-3Nmss3cq4QozTRIJPqFT7TN7nON675qqjDSlmCKikC36kqyivbxovWUnzyvtuFq4wBRcJRFjT5bEwKXZipFQj8vXnMmZZXbHbUqJ1lUFeCp4jxRxQC0okSDhaQonRYljNsq4v2LM62dCmMN-QQyIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYG04gGyiWt-iW27UiwRwGZ8eXhndbw6-hGop29vfaQhl4hIT-FMTnC27_9ZQlsjeJGJtf9VXtHkWp5meHUp6uw8yuM2QZQ-j9dZKmKp0jdYLJ_Ymt_CqIGFXwMxjtVdJEqvdXhVFYbBVqbUmuyJ_WskIH05DHxYFiBAvXdcEjnOQ-yRZOiHVg5Ap1buIMTNF8YegOsoAnkIbK4oFatNbtB5JXTpNpPZAjy_KBrAxPk21tXTzgbWb3Te2pesqi5ctcu4PK0Pez07fpMBmZtYZnRkyoJ3Xs_H9fSa8O-ZXIQ4XuOOwQge6QIgldrtUrgpMOwCPJ6hpl2KwIzYL-pozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=ao3Q96S8gPg6ZLJqZrhvlMVBt8oWWFs9RkY017XfhAv5gzvo3ZLP18KrsQbI_LvI5VKi-WJi0Y8ZHoycjWYnZbLPB6ioMmSiiIBW45-uX68Z2s8-6fROqTV7eVOcxuV9wmXRuHZp9Xcn56p9ezdbIqURyJg9-Y5gIXkryJL1YMgqzcmHD82d_QoN1uzkQM8_y16751px-jU8WqmErKAlVSN8EFmK85lxhc8LJck41382o0buP5ok0SnMsfZFLC7PscpaDZEXDOpN7qHMZfA1LDfNIiUmFUj2AF2n5JHmNaPkhJYRJ-bETh0Uku3hk_yRQJPyvOzioT5_bjJzYl2rrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=ao3Q96S8gPg6ZLJqZrhvlMVBt8oWWFs9RkY017XfhAv5gzvo3ZLP18KrsQbI_LvI5VKi-WJi0Y8ZHoycjWYnZbLPB6ioMmSiiIBW45-uX68Z2s8-6fROqTV7eVOcxuV9wmXRuHZp9Xcn56p9ezdbIqURyJg9-Y5gIXkryJL1YMgqzcmHD82d_QoN1uzkQM8_y16751px-jU8WqmErKAlVSN8EFmK85lxhc8LJck41382o0buP5ok0SnMsfZFLC7PscpaDZEXDOpN7qHMZfA1LDfNIiUmFUj2AF2n5JHmNaPkhJYRJ-bETh0Uku3hk_yRQJPyvOzioT5_bjJzYl2rrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=JKzAjanDdNl2xJcvfvXyjFLMPYYukr9HY3FPW3eWiCEfiW8wmXORPAOm-sSn8QiKYSO8Z-S65RGagixxD8kdTwRBzfWdfrc6qEA28sh4IkA7jclpEUFzw8orCYW7_odXcrZzbNb6YAr7gBQSafxICeWJEs_eMRSv_pssDwZtDi-NkPB76EarRj7e7_1KGmzXXaz-zGkGNPbsVt0IWfHVRexOQnZM382tGelFwFoUIHToh-aflzVTxIhCr5dE1ehHQo3KJ8wXzLFe3eUjwSSWIFHiz_cO9OiOgMqMaCsEe8DxwhO-tIu1ahvEQdR2-vt7hQ9pZ9dohNuYFVjpQNKtSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=JKzAjanDdNl2xJcvfvXyjFLMPYYukr9HY3FPW3eWiCEfiW8wmXORPAOm-sSn8QiKYSO8Z-S65RGagixxD8kdTwRBzfWdfrc6qEA28sh4IkA7jclpEUFzw8orCYW7_odXcrZzbNb6YAr7gBQSafxICeWJEs_eMRSv_pssDwZtDi-NkPB76EarRj7e7_1KGmzXXaz-zGkGNPbsVt0IWfHVRexOQnZM382tGelFwFoUIHToh-aflzVTxIhCr5dE1ehHQo3KJ8wXzLFe3eUjwSSWIFHiz_cO9OiOgMqMaCsEe8DxwhO-tIu1ahvEQdR2-vt7hQ9pZ9dohNuYFVjpQNKtSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=WsSVg9SGkGh6OyCr3hlsChZ9wWfjJ_O30djDa0tFNXzt0P2dt3J1wRYAOuELt5TC55qtg_qxS7NEbeSl9JKn3jqJpoBRPnaH9bNiY6cYdUBtNTvTRNxdrlWIjF6vhimfAHtkbyyIuF7DiC8FzXa6bHaAKHPxb8aYFLPnyEUFWxDaSlukRsbxRRyzWRXrxtbka1LxAdhUM0G3XYIUPHbRezEUG1nxdUrFe7vM57Uso19cz6aK3kghHLj4kz15Ogk4KscPgX_rI1Ue8QcZxyfe-iOYpioqn0pmrRDn9W3hbIouOlG3piiXFJymzcSWDAQSMN8pUYk-T54FikFgnIhpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=WsSVg9SGkGh6OyCr3hlsChZ9wWfjJ_O30djDa0tFNXzt0P2dt3J1wRYAOuELt5TC55qtg_qxS7NEbeSl9JKn3jqJpoBRPnaH9bNiY6cYdUBtNTvTRNxdrlWIjF6vhimfAHtkbyyIuF7DiC8FzXa6bHaAKHPxb8aYFLPnyEUFWxDaSlukRsbxRRyzWRXrxtbka1LxAdhUM0G3XYIUPHbRezEUG1nxdUrFe7vM57Uso19cz6aK3kghHLj4kz15Ogk4KscPgX_rI1Ue8QcZxyfe-iOYpioqn0pmrRDn9W3hbIouOlG3piiXFJymzcSWDAQSMN8pUYk-T54FikFgnIhpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCite34rmVbWDL0teE1VDERgz6RvYHFaL5IZ_ZCZRDvrLc8PUlxQ3TnfWU85txWMquADBn-fil4vsPAmdef9fCGQ4OYOX4fqoi8JcKpnONihCj17jGAAh38cv6tuD-VgBoqA0S1B9EzfO_spbrCoPnqKjx4DFhPlZoqr9-w22QGQslRM9NRfVKBiZ5_3e0slCZ8RBi71KhKisot0yzFxDnvgB__cJgb7MQ-wbrLyOO6pPObm1qfUEHX2nV3sb70pTCscbZAVM5dp69_ABU5mWwO522_nb_mhzBpYCpyhn3z960KU8p9KQQ7ANxnvpSWLFLEdIOwIe8dc1LcGZczyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=W9K0aaYzXKkogDC09EjsQrHW--IFmjI_o48cJxhPaSd641tXIisW2oAvqK9TXl0Ue4aS7MScn-ZLeVpPVubM22a6jWmcGUZN143JyTNaipCwMjd5AyEwVFDA770k4P_t_pZR71FtWSxh_avclzi4r_b3lrJbIBZ6rw632lLN3ZsrvQ0LJPUPFUV0dFQP3QbHaCBgFMPjZLQN_SRhuHaXwq3Dm2Y8DQfTqFFjFSIpwUZLPmi_y24hsrHWLXbqLtTctZeH3MC2_uvX5lgZe4fCCpGCTLZ0xAYPPf07J_0apBjqrVNfo7rWyQcm4bKu27mjrmOMlQQifpvNDsWaBo4v8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=W9K0aaYzXKkogDC09EjsQrHW--IFmjI_o48cJxhPaSd641tXIisW2oAvqK9TXl0Ue4aS7MScn-ZLeVpPVubM22a6jWmcGUZN143JyTNaipCwMjd5AyEwVFDA770k4P_t_pZR71FtWSxh_avclzi4r_b3lrJbIBZ6rw632lLN3ZsrvQ0LJPUPFUV0dFQP3QbHaCBgFMPjZLQN_SRhuHaXwq3Dm2Y8DQfTqFFjFSIpwUZLPmi_y24hsrHWLXbqLtTctZeH3MC2_uvX5lgZe4fCCpGCTLZ0xAYPPf07J_0apBjqrVNfo7rWyQcm4bKu27mjrmOMlQQifpvNDsWaBo4v8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kC_qbp_ehhZLKouky5yBMjqgqFbbPuC9QpgUYObg-JPm3C-GNvdNtAWCLw7g6BavAdS58gs0ZTV9dKW3Y6viVzY_ncD_p8TkqrtTPwmXJEy3sBozLcDS7EmOJpukd083i94iHbJzTytA7OFHVPv6p6EDbFiRWGoBavDYsue6UqvG70tls0qHCKsiSQ-qBEWcGLRGvCe6KlNYZ5cTCDUXE011x_ZLsm4GZg9Uj90YSx554UV__5GrJxpLc5Jy7Hw0u9j49FRE8siBdGvssMTf1Ec8-tV74z0G0NS1QoG3q3-iRmDm_XQKruTrIzWBrf94fyUCa_HAi9fz_clbJCDI4EI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kC_qbp_ehhZLKouky5yBMjqgqFbbPuC9QpgUYObg-JPm3C-GNvdNtAWCLw7g6BavAdS58gs0ZTV9dKW3Y6viVzY_ncD_p8TkqrtTPwmXJEy3sBozLcDS7EmOJpukd083i94iHbJzTytA7OFHVPv6p6EDbFiRWGoBavDYsue6UqvG70tls0qHCKsiSQ-qBEWcGLRGvCe6KlNYZ5cTCDUXE011x_ZLsm4GZg9Uj90YSx554UV__5GrJxpLc5Jy7Hw0u9j49FRE8siBdGvssMTf1Ec8-tV74z0G0NS1QoG3q3-iRmDm_XQKruTrIzWBrf94fyUCa_HAi9fz_clbJCDI4EI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZQ1Eu_c7uc0qLfFMRBbg_5EnQUhrhw6-mQB_l0sK15qH0JL6lHrNRyxFmQvt_emo0xCYYusi2_fpbfg4CgJgXYfRVEN2siVv-C5AY3--xrRVvP_s6600S2jm2fe3zI54HseA-XDr-VcRySrRhPm4IaXZm5ryRsJwfxGu0qXLFWc2qKj_H6yRnX9RkASK3xDszs0mWoRtcqTcBGTizmlki6Tgm1fmGHKbYDrTeUPGPkrXFktyo-t-GrvyiLR4uTnnd582eYoni7OKwPqBQpcOFE5Kcj6wD5ORbhhnbdb23miYvCmn9M7YCwH_QvmKUAmnPuI3UX3_7aaBW08PlbXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=Pp5CvmChm2_VFJ5bi61zJSdsWFw_bFPJwiK8WO3inktA2wqBbQc6B8h5Im-KmCfkcjIGvbSEfBT-gr5s3UCLM8OUos5F52Q6sHOA-d2eERkbzBbkslekOqxnpssrioj1ygXKFc20rMvfVEyrbGkn0yDRjyhSEt2ifcJR3rny3JdU_zig-ZWAwRc8m4--sFtT-zKBBvo-wntYrK_c00spE7oE_pIPM2z6RLL-l0iBsOwhLy-_fqZ3bdL3b5WDNnVa6A6Uj0JCnsg_4dpei9CHW0zssFemDybPGG-3j4hR34_kAwuHKaDA4kn-Qb-T-i8lA3XO4Ibt8-IKUWG33R8NRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=Pp5CvmChm2_VFJ5bi61zJSdsWFw_bFPJwiK8WO3inktA2wqBbQc6B8h5Im-KmCfkcjIGvbSEfBT-gr5s3UCLM8OUos5F52Q6sHOA-d2eERkbzBbkslekOqxnpssrioj1ygXKFc20rMvfVEyrbGkn0yDRjyhSEt2ifcJR3rny3JdU_zig-ZWAwRc8m4--sFtT-zKBBvo-wntYrK_c00spE7oE_pIPM2z6RLL-l0iBsOwhLy-_fqZ3bdL3b5WDNnVa6A6Uj0JCnsg_4dpei9CHW0zssFemDybPGG-3j4hR34_kAwuHKaDA4kn-Qb-T-i8lA3XO4Ibt8-IKUWG33R8NRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjLzFP8l8iWktdUm6agNJq2XXnlImLHQSBtH_qdx5rzTt3adx-UvCv5LVWv7txKKL4uUM7Fn4ilLTEcyXtcIXa6DEvGrODsc2XbPu7h1DNVQvoh6gJ7zMVGHWpKx8GFSECXKvVn00-aHaAd5U2YzucYMusmCBI3GiuJX81aWGQNvPJZ_M7zKiKZ4e2gPbRbHdE7aCKnsY84dxkOIrjoshJQr9PmZU5Ov3b3Tfy-4nsBZLdvhsZrB8H-4XIzFJ9qZ_zhqiUMu9OGdlojMzxoK-cDuGapSHGuA_iDnolrDvQcveJvVX0xGk63u490wAhM5oMlleC2Jdxc2N4tHicReYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=MKfRdAATtAxAbviJq2AuJz017rcBzMOi7OvYILfDbYhqakBIhOwH4mu5GA_GTnEwqfJGph5H3xfd32pX5ZXvEVL3UEgjbBixT_6NeUnTYziRfTBtcZg3P-Y9RI0XpA86C4liNO_aU1W2ePUHaokiq74Pdcha67Jd7fi10WcdKLtIpbDb9g7_OOYcaP1c-wlmE78m7LYZQOOpumY6cBX73XOChzy3IRnlXNTCxHRGwyo_0VWU6lDJ9efN1bt4bg7MAMcBJ2OjhZE91d8THUahQg8xOBToFC8JNTV4wUUHYek1--c1XxAIW6QtsKprVX5G7VhTedq_HJ7ZyyasYHZpi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=MKfRdAATtAxAbviJq2AuJz017rcBzMOi7OvYILfDbYhqakBIhOwH4mu5GA_GTnEwqfJGph5H3xfd32pX5ZXvEVL3UEgjbBixT_6NeUnTYziRfTBtcZg3P-Y9RI0XpA86C4liNO_aU1W2ePUHaokiq74Pdcha67Jd7fi10WcdKLtIpbDb9g7_OOYcaP1c-wlmE78m7LYZQOOpumY6cBX73XOChzy3IRnlXNTCxHRGwyo_0VWU6lDJ9efN1bt4bg7MAMcBJ2OjhZE91d8THUahQg8xOBToFC8JNTV4wUUHYek1--c1XxAIW6QtsKprVX5G7VhTedq_HJ7ZyyasYHZpi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=N8__AAfptDf0R_H6cB-V94dQPW_oX0eAuU-vfU0rZWPF9goS0VzDzYzTIkbzeVBU-8gs-dVE4mb-5sUs4TLaVJ7l4Ltg8-uvURSyy0d058sPUS3ygSQLmmUHVf6uFkgdhqbJX5BvEF4PshL6DD88M91NnSiI4PcWICHr_jHKI8mlRGCRLMexiP2ROx6O-kQPX6MZg1bjcb9-PPL1h1elM0-EmeNqEojO47Y8G1T4YiY-2cHoII6b6CovZyFkDZ_Xk_MYY1ayXUwBoOP5xHxU-t6MTH6aMAvgA6ePBLB6fMljs9aDaLAD2kG8EOfHVPciuBT8phy9D4DKRfJyeKWqbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=N8__AAfptDf0R_H6cB-V94dQPW_oX0eAuU-vfU0rZWPF9goS0VzDzYzTIkbzeVBU-8gs-dVE4mb-5sUs4TLaVJ7l4Ltg8-uvURSyy0d058sPUS3ygSQLmmUHVf6uFkgdhqbJX5BvEF4PshL6DD88M91NnSiI4PcWICHr_jHKI8mlRGCRLMexiP2ROx6O-kQPX6MZg1bjcb9-PPL1h1elM0-EmeNqEojO47Y8G1T4YiY-2cHoII6b6CovZyFkDZ_Xk_MYY1ayXUwBoOP5xHxU-t6MTH6aMAvgA6ePBLB6fMljs9aDaLAD2kG8EOfHVPciuBT8phy9D4DKRfJyeKWqbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=NjMGQAlrSQl3PwvITGFISH6rw-Is8GrBKXpMagKStAEOukEzz9jFDyuRZpjkt8aIE7v1MwyrMUZ-UIb2zJJDzdug2vJFyKERWf9LSdu5s02T9Ze6HZgLP-t2Ny-i55Mw0BesbhwUh9OhSLOUfyowIh5uG7G_hZ1SUVXQR6eBZ5Rl8OtB_TkuingA72ZYG4xl7sDHQQ_DHaEVbtNAPdyHUVQCR7xSXlqgFmrmnrgNxR1fs7aXpG7aQL9LZVLE5c3AanwqqiiYnaIapdSWKneo-DdTIG-1jWn9fSiQ906t-uuLggqFeSuae1Sr0-vdlsRE0tiwHpAxmfDaIyCvgu2iUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=NjMGQAlrSQl3PwvITGFISH6rw-Is8GrBKXpMagKStAEOukEzz9jFDyuRZpjkt8aIE7v1MwyrMUZ-UIb2zJJDzdug2vJFyKERWf9LSdu5s02T9Ze6HZgLP-t2Ny-i55Mw0BesbhwUh9OhSLOUfyowIh5uG7G_hZ1SUVXQR6eBZ5Rl8OtB_TkuingA72ZYG4xl7sDHQQ_DHaEVbtNAPdyHUVQCR7xSXlqgFmrmnrgNxR1fs7aXpG7aQL9LZVLE5c3AanwqqiiYnaIapdSWKneo-DdTIG-1jWn9fSiQ906t-uuLggqFeSuae1Sr0-vdlsRE0tiwHpAxmfDaIyCvgu2iUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=QyFOzuT089Qkp7SjCb9X_kNjSiwLasSSHnGxPL795gPJQZ-wL0IQL7jvUxuReqeOqRtvphjpAVvboGNETAur5yoiISnq5zGWtjeirf5wyX6O4rafRzNitixJsxNFMTAT3ju1onHorS3tl3cyNjENNLj1blhCrNgO09RUxCEa6VFi1eSp6doMg28PPmcpK3BIYVRm0HDvXaaV7NAPrbQG-YYldyEIcCiP2ay96eaDeJZbWB8EfCsGmIsYXVw6ct3ita1V5CS7j2pq4feHawWNdYu_jdOCsWu9JjhprW_1BvIBemD7MLYeXEeQXQuU8wxD-Pt_1nJdfTNuQtyYe_INPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=QyFOzuT089Qkp7SjCb9X_kNjSiwLasSSHnGxPL795gPJQZ-wL0IQL7jvUxuReqeOqRtvphjpAVvboGNETAur5yoiISnq5zGWtjeirf5wyX6O4rafRzNitixJsxNFMTAT3ju1onHorS3tl3cyNjENNLj1blhCrNgO09RUxCEa6VFi1eSp6doMg28PPmcpK3BIYVRm0HDvXaaV7NAPrbQG-YYldyEIcCiP2ay96eaDeJZbWB8EfCsGmIsYXVw6ct3ita1V5CS7j2pq4feHawWNdYu_jdOCsWu9JjhprW_1BvIBemD7MLYeXEeQXQuU8wxD-Pt_1nJdfTNuQtyYe_INPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=vRyPnrAxxmAROtHSpvPiH7_u2aIKR3fiBcuJluQfhHAmxMcwEiTt9NR9uqCF79zNpfeFqhop8rlDDDhdcFp6szaoaxvExNGqbpgbWRd1amv-aBIdjVOYQNNO-6TqAUB10W1mQZRno52FQTxh21L3KJiTCVMxiMxb65dxj_Vp6-1Ancz130RFLJWj-ifF5dM0_0G49iM5jTjB0GqzB7D5_iEqxf99TOD_TDoK88oN6IXxbAKNCisN7JqLkYeHKHEQCBjiE24hEumMubm6Bp_g44yXlTAKLnOqutzD1ZxteFpYFnd4pxw1THExQX3-c7Iaisgas7hQwsPpa_3noeDARA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=vRyPnrAxxmAROtHSpvPiH7_u2aIKR3fiBcuJluQfhHAmxMcwEiTt9NR9uqCF79zNpfeFqhop8rlDDDhdcFp6szaoaxvExNGqbpgbWRd1amv-aBIdjVOYQNNO-6TqAUB10W1mQZRno52FQTxh21L3KJiTCVMxiMxb65dxj_Vp6-1Ancz130RFLJWj-ifF5dM0_0G49iM5jTjB0GqzB7D5_iEqxf99TOD_TDoK88oN6IXxbAKNCisN7JqLkYeHKHEQCBjiE24hEumMubm6Bp_g44yXlTAKLnOqutzD1ZxteFpYFnd4pxw1THExQX3-c7Iaisgas7hQwsPpa_3noeDARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=lwgWyGXs-gYjfFr2nguNgqKM7dXo_8V1U5Yl9BlzbLFlyZ1890foyrkeI1ZydyXOijR9l9LWk_Dr454TUJ5j7WqxHGfPfGkKFW4908oIVbwjMuOtDbkMKVVHppd8as0fXr5n-qxvGNBQmmOnFufz3-GwRYzwyfD26fEEywTjayynOqnNEwJ7N9zOQQerJwVieJQKMGoHM_2KCZmW-O9YU33kdAEKCh2q1oYzhk9s9oX05zps_QTgWSKwNXXYCdSLUc4fc5ZMwQ2riH1oTO_RLiHS0F1BCZbbKx_0NGguPdbbIpguMvFnfRgZKmWcM3pcxHhcjR3hsX1PvdhmIsYgow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=lwgWyGXs-gYjfFr2nguNgqKM7dXo_8V1U5Yl9BlzbLFlyZ1890foyrkeI1ZydyXOijR9l9LWk_Dr454TUJ5j7WqxHGfPfGkKFW4908oIVbwjMuOtDbkMKVVHppd8as0fXr5n-qxvGNBQmmOnFufz3-GwRYzwyfD26fEEywTjayynOqnNEwJ7N9zOQQerJwVieJQKMGoHM_2KCZmW-O9YU33kdAEKCh2q1oYzhk9s9oX05zps_QTgWSKwNXXYCdSLUc4fc5ZMwQ2riH1oTO_RLiHS0F1BCZbbKx_0NGguPdbbIpguMvFnfRgZKmWcM3pcxHhcjR3hsX1PvdhmIsYgow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=geNVAMzNknCM6xvsc3fNCd47pVSy7YAyG7tPv_UuZpJSrdEi1khjlerytGGz6b_G65FZSaf_rsENeludf01r5npF_fe9oBJXxqjditjPWFL9Bu-L25z2REha7F3sAZsYwP6I9Vpg8O_q0xn-MhU-4uJlXdGRYcgfSTxFtEhmtVwxdRnYCDPML-vSPlSbH9g1AokYB_HFErACpxJ4hjaV8GXmcbBpGAUZwm7MH4kuWUW9olM-Yr_w5DsfSnfOSclFw9iL1hS08aSrRXIk_rFltrmeZHKXhA__ZZwpQ-WLPYjkqsI0KxZ9ZLU9MchmR55BXiNFo1TZ8TMHuDAVhqduXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=geNVAMzNknCM6xvsc3fNCd47pVSy7YAyG7tPv_UuZpJSrdEi1khjlerytGGz6b_G65FZSaf_rsENeludf01r5npF_fe9oBJXxqjditjPWFL9Bu-L25z2REha7F3sAZsYwP6I9Vpg8O_q0xn-MhU-4uJlXdGRYcgfSTxFtEhmtVwxdRnYCDPML-vSPlSbH9g1AokYB_HFErACpxJ4hjaV8GXmcbBpGAUZwm7MH4kuWUW9olM-Yr_w5DsfSnfOSclFw9iL1hS08aSrRXIk_rFltrmeZHKXhA__ZZwpQ-WLPYjkqsI0KxZ9ZLU9MchmR55BXiNFo1TZ8TMHuDAVhqduXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUHXYf8HX-AFH4pGo-w12FEHjw9Wq930tMbMtkcleEWIe_pVjsaThAVRiDH18LWMUd5Ov_pCxl2j_JgGmAF2Dbo5bIkel9BVzys2xawmeuApp8e8Pzyw3XY0Lal2bFdkZCIEz14PF0G_BrGZqfgEEHNPqk5hlV6xJ526HCgy2MEasG0_KAKZB_-l5nZU2hx5pWvNbXtagYbabJ6ieS7I5YqdeIDJXXL6Lhy5iKg2MLMttKqNAu6BlD__4BXESPxBDZahmaqlhJjdm2MTubuDsMn_d3WG_oj6y4CykMATFHKXsINFKgdvs37Tm67PwbQo8tCkSL-1zhkfMJkbm6NmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9-9XvpiQLO5nTfRvLtN0jQAqKhRmBtbgCA60cmOFccrp0Y2kNqtRWolcaCRQPBvMHp5S2nMbo1Fe7oiBspbMDCEKAwYaSZ4OUJ8TI_BJwB_GaHDbyRWXw0tA1PRVa_ocfilGliQdeqbH4RjulQRqA7dni1HeRB_UjptleYRp_m0Q_WU85BdSDVkzVU_sB7kLNPttaoHrYWxFoIBQOKiDcyH7FTlqHhOczyNpzt-CqUYk3KfVdhwW-OTujWZiTrRyBqWaYv4I5uMIuj9O_Q6bGqYJMd-kfHs-JEdD3bTbaqecmwosnwT_WfIp9n2w1_X7CwID0fVXD5q-7qV6Klv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0jQQXo6y8AyLFVhEHM7n7wBhZMVVJo0IjahMQqKjCvlwV-8lrrKmYcLLlEfd-u3OboxdHuCm2nQDm3EFesahk7nGd8AyAEOjCVYvBazs4g8QP6FZeH0fmrxvcfsL4vkX4beUWdwLbIb6iM8XdORhu_cbsJnsqOOhb1rsv6Wxut1niqc-I5hRFua6IVsYnhA9nJWJjGeZIB0dkB5h74nhhCj58Q930LKmoNKmUiQIa3S48KSLnhTEJKFd4qeSg2Y-S3ElO_aodc3nJMDt505mYlXaIK8suVeSO2D56ubKxJFjDjAYomojmPYDlmpWEg6uSlwMepfIsfsOv_WUZ4ryA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=hjoRKSF0SNvP3_AMSFwp7jAJXM6PwvpsUZNeCx2Lxc2R0CSCYQxL0PX5PlvNY_B5rGrP3GTvP0Pt3f3xHa0ktggCKrwPOLj-YmyG0LIc6gyU8MRH22maDkNQW2M1HmCbDbGcYCLuSEs-vwJzyL4jiM9h-A_8CHc1dRgRav6Vz7XQnzeFzEXvZgYKojoaqL6Hpggg8J9rCnL_mLdt8UiGupU53PnyO1twGoLjYQcHl9oU0hAd_NLiPVAqnr0ibebL-4P4tfPrJ5k0a7h8i69N5S7S-xXV7z9KOp-aZPp2EJyP2_Tbq_dFM8jvII53tI-RIPoaDjb4LS4yhT9HDXr-qFN--6yjJf9CQOVS7JZN3h9zBAPBFaH6DXrWNNZogLzPEuTN3HvmspnotjTwqsvZrUbXV281ewDfhoS49rkvnSzQjGb1WLd2QH5hTLIG0rIgESykgYM_uIpdNlZfp1vS0ZRE5yx5Kko_aigyjFzRuWl5wqrP9BXnudBhOxUh-Kvr0QAg1U9ty5qOlyZg-CcrKLmsTILTZLxMnRFicB_803CCV2S1PR0v70IUfgGBXUTXPIMz9MukCQV76Gfvjo22aT_d5Dn37nzSDwgCjDypuPscE5FL8_nhIG7d8zgcmLQ-3d9IXX5caIdzC-JB-fIZ-9ZIIrIRUfaE4D--gDvBDAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=hjoRKSF0SNvP3_AMSFwp7jAJXM6PwvpsUZNeCx2Lxc2R0CSCYQxL0PX5PlvNY_B5rGrP3GTvP0Pt3f3xHa0ktggCKrwPOLj-YmyG0LIc6gyU8MRH22maDkNQW2M1HmCbDbGcYCLuSEs-vwJzyL4jiM9h-A_8CHc1dRgRav6Vz7XQnzeFzEXvZgYKojoaqL6Hpggg8J9rCnL_mLdt8UiGupU53PnyO1twGoLjYQcHl9oU0hAd_NLiPVAqnr0ibebL-4P4tfPrJ5k0a7h8i69N5S7S-xXV7z9KOp-aZPp2EJyP2_Tbq_dFM8jvII53tI-RIPoaDjb4LS4yhT9HDXr-qFN--6yjJf9CQOVS7JZN3h9zBAPBFaH6DXrWNNZogLzPEuTN3HvmspnotjTwqsvZrUbXV281ewDfhoS49rkvnSzQjGb1WLd2QH5hTLIG0rIgESykgYM_uIpdNlZfp1vS0ZRE5yx5Kko_aigyjFzRuWl5wqrP9BXnudBhOxUh-Kvr0QAg1U9ty5qOlyZg-CcrKLmsTILTZLxMnRFicB_803CCV2S1PR0v70IUfgGBXUTXPIMz9MukCQV76Gfvjo22aT_d5Dn37nzSDwgCjDypuPscE5FL8_nhIG7d8zgcmLQ-3d9IXX5caIdzC-JB-fIZ-9ZIIrIRUfaE4D--gDvBDAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwGOafrVwYf7fcZ0YGjGqcIX3c2G5AlvD-wCzTkq-YGO_w6vPAbTlthl0RTnh6yUxOvK0iYBOyZ5UJrkcsV93Yx5EKTGRCDK47n5H1_JKZo9Dpb5DvSXMAXI7pTjun63AYAO8QYMnGbp_spsLdKVXDjmbU0ZuBJ8S9mIriOVz-R42WJ8w61TCh_y-6vfeXLmdgwj8bYZDbZaNSC7iNw9Ya4gs79na0TkKJ7wi5xkqhFW3lv9kIU88YcoDVeTca86D0YlCGXGo_11ZQo2KqOeIu2jBigVakQyTxlGF7Cr5HLxeWc6kLvJlinYJbI4xoX8tYt_BvMbJ36UMi2YjYbRvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=Un_bu-RmaEm6-7rtP2Op6Cf9_7kNSUz-NaVH8KTGPbT48FK7Xzi_NVIGUhVbhrYYZ0kaOd0OcCuPguRbIskOZBT6lnkWwQjapn9Bto_IDF2XIdH7gaB_Y7hBNAQrcbvgYjX0Mls3UjNfzhpWylSKs9xuubCCBgcbybQJlw1WA4qVbFWE0fjZniLMhF-rcCvztabZwBqzOHGP31VUHzRmIJNhu8SKHSjzU-MYZ3xSjN8h1h7hTdStxY56gYNxOQJJIjqE6u12MXUfHHsIi_fLUNGNgDVTgQS7ZLXVup42zjdlzb7Wy03JF-1VMB_p2SxgrM3BLI_N1pN2vDPy_NkL0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=Un_bu-RmaEm6-7rtP2Op6Cf9_7kNSUz-NaVH8KTGPbT48FK7Xzi_NVIGUhVbhrYYZ0kaOd0OcCuPguRbIskOZBT6lnkWwQjapn9Bto_IDF2XIdH7gaB_Y7hBNAQrcbvgYjX0Mls3UjNfzhpWylSKs9xuubCCBgcbybQJlw1WA4qVbFWE0fjZniLMhF-rcCvztabZwBqzOHGP31VUHzRmIJNhu8SKHSjzU-MYZ3xSjN8h1h7hTdStxY56gYNxOQJJIjqE6u12MXUfHHsIi_fLUNGNgDVTgQS7ZLXVup42zjdlzb7Wy03JF-1VMB_p2SxgrM3BLI_N1pN2vDPy_NkL0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=irLnB0ur4O74fv_4unYHWNIGA-tbVOqkpn0SaWDKCcfljkMygm1Y8rNwUgLWoZekhZmOCaUTnIxyyKwzNP7DyeUmjeRbZTeROzzPgUbmhBj1skSxDhiL_0NbO2BpBYeAzEwVqjTcAJWdSI7HNPYOsJTpg-ySbrf3G5D5JDzX0mj9CJfFsjcR6oL0GZ2HK3NBym8RPpPSh0pKIn8pt2d5JZbLycKq3gVCSH9z4ZqU3O9nu3K14vMTiQWz0kDULacs0s4ReW9iGlp443NCEV5N4Yz_q7ZOuUpYXleXLlQkTAcCYndUlNLkEYZkkozuS3Oy-j4wrBlqO0kIy_uBE_JuYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=irLnB0ur4O74fv_4unYHWNIGA-tbVOqkpn0SaWDKCcfljkMygm1Y8rNwUgLWoZekhZmOCaUTnIxyyKwzNP7DyeUmjeRbZTeROzzPgUbmhBj1skSxDhiL_0NbO2BpBYeAzEwVqjTcAJWdSI7HNPYOsJTpg-ySbrf3G5D5JDzX0mj9CJfFsjcR6oL0GZ2HK3NBym8RPpPSh0pKIn8pt2d5JZbLycKq3gVCSH9z4ZqU3O9nu3K14vMTiQWz0kDULacs0s4ReW9iGlp443NCEV5N4Yz_q7ZOuUpYXleXLlQkTAcCYndUlNLkEYZkkozuS3Oy-j4wrBlqO0kIy_uBE_JuYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=WkQTSz_wLCZG7jXzmcQHn0K5GZnH41RXAw_tZlMO2LBsVYHtpCDBD9XwvQKweIM0Akn_HyrOMQIxlL9gUKYN7tmlDQ55Gb5K2fRZydYNOIJUqE99hGZphPFMEx5MHSPxZS1rj7AJ8rj3TLkLxgfgrgk5pR6Fzop9DZBeLcT1ql6viR6-LRzQx3WUUZ3F9QyDwD5px3hdp9hH9RueSzE-ezsUfUOPbUxlqzG8B-JrXO6AKu3jKFdhSLjqrvv-xBVDctRJ44X0FTryR3k3JzlQDwV1nQV6SlA786mX-ZnPZWuqvy1jaeGRUGXp3MLdDl9Q7VIu6nrlI3Vsm0PtyeXBpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=WkQTSz_wLCZG7jXzmcQHn0K5GZnH41RXAw_tZlMO2LBsVYHtpCDBD9XwvQKweIM0Akn_HyrOMQIxlL9gUKYN7tmlDQ55Gb5K2fRZydYNOIJUqE99hGZphPFMEx5MHSPxZS1rj7AJ8rj3TLkLxgfgrgk5pR6Fzop9DZBeLcT1ql6viR6-LRzQx3WUUZ3F9QyDwD5px3hdp9hH9RueSzE-ezsUfUOPbUxlqzG8B-JrXO6AKu3jKFdhSLjqrvv-xBVDctRJ44X0FTryR3k3JzlQDwV1nQV6SlA786mX-ZnPZWuqvy1jaeGRUGXp3MLdDl9Q7VIu6nrlI3Vsm0PtyeXBpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=Y4rB9RnO-s28A8cvMBM7QtDqIX6w_UqD8u2H9b3aQlfKjsph6ZKvSfnrUA6tYk1E9MqF9DFCOVjUosd-0igr1krj5gPRTCLZ3qt1AiLe81SpSs6VBk1pWeZtj5UTIN9W6BpJhFzK6ib_gWTeMfZcOnpXs7PKNUzAE7Hl7atICP0r8RdLZyu9-31pAZ0Ul8CelOhlMKro03vgbtaiV6n3VCD4SwPrXsRvIip_Yt7Cw5iyCeqpid7bAyCP968MTG9zVYefaDDgdsT1MXkSS3PjxIGsThmQVkUvzqH7ZC-rM0Op3KjNucmAqq6nANzv6hKkEAo2Ws5ahCvFEa6iqzUu0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=Y4rB9RnO-s28A8cvMBM7QtDqIX6w_UqD8u2H9b3aQlfKjsph6ZKvSfnrUA6tYk1E9MqF9DFCOVjUosd-0igr1krj5gPRTCLZ3qt1AiLe81SpSs6VBk1pWeZtj5UTIN9W6BpJhFzK6ib_gWTeMfZcOnpXs7PKNUzAE7Hl7atICP0r8RdLZyu9-31pAZ0Ul8CelOhlMKro03vgbtaiV6n3VCD4SwPrXsRvIip_Yt7Cw5iyCeqpid7bAyCP968MTG9zVYefaDDgdsT1MXkSS3PjxIGsThmQVkUvzqH7ZC-rM0Op3KjNucmAqq6nANzv6hKkEAo2Ws5ahCvFEa6iqzUu0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG8zkM7KoDGQPrp6im6M0Bp3ubh8XFn7orC23-HAQh_6em0DXV_NKzqOuprunbXoxCSfaPlgEE37mYytrgRt0h0lpIxUwLjRLe5BdH752Uwll7LWzh9bSAx8iqN3VSXk0iC_vBrrVrdjx76ZP411HrIN-TB8XDT-nUR5BY_YpidJaFt1jsmpSoUPaRGzGXzdBqmhiBsF1y6H2JE8KvE6UfUVz8UvehQOpHf10QXS24Vu5wIquAvDkqdDd2ASoMpqFSH74fGO6dH_sebIQ5mCnnjpmOl6kIc0hsA7VG4hMiHvQSz-ocAm631gXjF7DE4KQKHZWyXHJNRJe8iq-bUmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fk1S8cPtKWl7_ZW26oh7joyQNLphYb3W81JKu0TjIwDxuq90ecW4KKcpmFuOdtfjyfMblxWko2Ljl9MELwGuKoonESrrOHPT63NKWyQdrcQTcC3gk1xlLhKEJhylD3WfgwCAjoC3YRff41U-Gpf88VNedTlHQ0lcn6AiCXS45MTRtDf0lOZrondhcDb9HN_zOaQ5BG5vTY2O4Bv6jRBOL8DwkSEDG3DLVfw6kS53ex-Oax9uIImqh09zDHohqSH1WaUZqS5GVl8DqgrRoeF7d5p5qcdWYo516uguMmwm5Sr3uqI0_y0LeVEKxu77Q9iCp5uyHt7yj-nhb8-lg-8jOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=ZWHxKXsUzMEaVuQUj8gti0Um28ICE3hkHD_wBVH9MCRbkf8_YuWy_UBcBCsKzl9X_IdXmJsCyFlR8YGvFKWPEeXmJrJqU89t2D3P-3vQSkgfP9Cx_udBYPu4lPZ91c4QEgFIaGzQAtw1a-PGBWXkW5sNqS0mb69YMpuV-nRITfEBH6UfwW7v6TW6zh3T6ahVKMrhFz1viDI_RjpQnaxfkKH-7__WE8D0z3NUk7s3k6fKOzqe8mZEEYxRKQzHoPOw0o3oGEinIPW-WU-g12tqfAvWVYRNCn-finYBOpEWoXoa35rxB9dxQZs4ZimRMfetwNWKPbAlfV8Q7kdTHp9Sxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=ZWHxKXsUzMEaVuQUj8gti0Um28ICE3hkHD_wBVH9MCRbkf8_YuWy_UBcBCsKzl9X_IdXmJsCyFlR8YGvFKWPEeXmJrJqU89t2D3P-3vQSkgfP9Cx_udBYPu4lPZ91c4QEgFIaGzQAtw1a-PGBWXkW5sNqS0mb69YMpuV-nRITfEBH6UfwW7v6TW6zh3T6ahVKMrhFz1viDI_RjpQnaxfkKH-7__WE8D0z3NUk7s3k6fKOzqe8mZEEYxRKQzHoPOw0o3oGEinIPW-WU-g12tqfAvWVYRNCn-finYBOpEWoXoa35rxB9dxQZs4ZimRMfetwNWKPbAlfV8Q7kdTHp9Sxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=ha18tkmBHCIli6ZrDUY9OdlOVAoP7SezMpXeimZ5MSrh5PsJa8qx82VqY5FCM_CfA4Tf7wIjLxPLtoYbKpxssL8xK197ej0EcUQFbY7L447CQsfjV6mnSjbmojfeb5xNdcsY-rMj9fyZX4KU26ZuMpveMzwm4Bm2wIuK6FconZl3qu2qMJDQBV35RDufOgh0Ia1VmMnqYz0e-3fK15M6hFcAJmkjeOgCsI8qyQZdqciZupMiRqIH2sRb-mODQFHALOamTat9FpZ9czoAprY-Lg2Jpmr1Xbh47l5HdVG-MlCQ1lB0QUxmjcq1kfT3O3Tg0pQ6hFWFtxUT6xl19oyNtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=ha18tkmBHCIli6ZrDUY9OdlOVAoP7SezMpXeimZ5MSrh5PsJa8qx82VqY5FCM_CfA4Tf7wIjLxPLtoYbKpxssL8xK197ej0EcUQFbY7L447CQsfjV6mnSjbmojfeb5xNdcsY-rMj9fyZX4KU26ZuMpveMzwm4Bm2wIuK6FconZl3qu2qMJDQBV35RDufOgh0Ia1VmMnqYz0e-3fK15M6hFcAJmkjeOgCsI8qyQZdqciZupMiRqIH2sRb-mODQFHALOamTat9FpZ9czoAprY-Lg2Jpmr1Xbh47l5HdVG-MlCQ1lB0QUxmjcq1kfT3O3Tg0pQ6hFWFtxUT6xl19oyNtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giMKU2vdwS79zp1-an3gATnI5GeN_Uqddbym5OseYXiWN4DPtC1suXR7x1C9s6qTyoB0OrvXmO00JjvoJN9xustkaNgW5GlhJZuJLww87uTVzelnUqp99Mojt76ka1fSlS0xLA-DWSLbsUE147zyEFKmhj1rCTlC341ZvB_aqwaUP18yuX6A4PtcFb1HB54lQdPBwaZRrXOdQ7rffB1vQktn1zFXbHqpsInK4d0zv0r6VRBDrV_NCoPGkm7Efz-hzNKVw8TLD1yQE8sbTOvazq1e-5f5U81CC_4gpew2hyL46AJSnC8U2DMsHIZd36HFt98aGmiEAo_mjV8-apMwiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=Ok4Xr7mrdM0Blq_tnmBzbZ5he7z4Xfjirl0Af5WYdM7WYjYCQDNVQTb5_3XNl1EyVEMrHWEOy_odmnDMvpJ-e7ZfAvbV6xM4Cw05WhN2GuFUuBKVxDUOaQ7QPjwIxs6ywwta7jin7QfC7R9_l1OJBo9ThsdjVmxyJYm4jlYMG5p1Yal4k5FShuL_nciZBT5rVW7L9TqzaFyK7llXNZ9PSe9dynshbIIX_flxqSbjCXrcIwbYdfj_KzzNmp0ZWfXuXPFwFjOrkIC-pcIobI4J8hX6BGAGpnXrdpc2rOWYZ4OALia70GnQKlOPFqmGhXTwXe1GovYIqfHdyf1gYv7d4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=Ok4Xr7mrdM0Blq_tnmBzbZ5he7z4Xfjirl0Af5WYdM7WYjYCQDNVQTb5_3XNl1EyVEMrHWEOy_odmnDMvpJ-e7ZfAvbV6xM4Cw05WhN2GuFUuBKVxDUOaQ7QPjwIxs6ywwta7jin7QfC7R9_l1OJBo9ThsdjVmxyJYm4jlYMG5p1Yal4k5FShuL_nciZBT5rVW7L9TqzaFyK7llXNZ9PSe9dynshbIIX_flxqSbjCXrcIwbYdfj_KzzNmp0ZWfXuXPFwFjOrkIC-pcIobI4J8hX6BGAGpnXrdpc2rOWYZ4OALia70GnQKlOPFqmGhXTwXe1GovYIqfHdyf1gYv7d4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=ZIE5RIodiyp7g97DQMY-2L-byw7dKyTSrwbGuNffuzjxD_A35EZwr4tpBQSEWB-2U5R2d7BsUpfJsmg0cvrmS5ak6Wh8a2t7pVErucdooL9WP0N2SJ5VHVEMX0X2IQdJrYJzDTAIgwSMFGyCqeL-z2zGzFI3AffDPcNql8wLkIPsJ9tlv7n4KKhmLfy8h8cwXBeIQfLIHcfVomMdxC2Fq1iVxA945JKBjIicG3D0w5Fg1OzaX9PfEG3aAAWQ3s08kZO2UXtoFiF4QvdhJrlzzzNEMOshTMilKa_ini4RMUVZxC81zFCEDjSpAfjFHs7onPG45XWvw5FUsdiTDzXsNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=ZIE5RIodiyp7g97DQMY-2L-byw7dKyTSrwbGuNffuzjxD_A35EZwr4tpBQSEWB-2U5R2d7BsUpfJsmg0cvrmS5ak6Wh8a2t7pVErucdooL9WP0N2SJ5VHVEMX0X2IQdJrYJzDTAIgwSMFGyCqeL-z2zGzFI3AffDPcNql8wLkIPsJ9tlv7n4KKhmLfy8h8cwXBeIQfLIHcfVomMdxC2Fq1iVxA945JKBjIicG3D0w5Fg1OzaX9PfEG3aAAWQ3s08kZO2UXtoFiF4QvdhJrlzzzNEMOshTMilKa_ini4RMUVZxC81zFCEDjSpAfjFHs7onPG45XWvw5FUsdiTDzXsNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSVKjq3ADahE3-2Dw8Eqzik8oEQc0G50RnW4lHYrs-9iP4khpMVswd3ndPQcDuJX4FZQysSgxjYGu3DRtTdrJlwTxsanWuCLJB52xgijaVbg-YxDDOfKP5HT3VHUij6h3S5D-UjP8o_ifsxUZdcIBMJhCGizPg-Q7n5qpk56FDxwQWmoMI_H2Tcr4c4WEAsBrMBf1EXwJEl1s050eKjvGYj_8SSljetn8sthAb-WeQ4oyQu_xMVlcnZbIara5D-ZYAi3mUpW6rMnSC5SPxzg1otzwOmX1yOMEBqWiGMbhQm_4RgCBeVitK4a_NztTdDv0KPYMYjAo5KWDYgnF-B1xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gldWMwzuTwhZRLKUQDFTZnvuY4fOBv9B5QEWz3U7BhMWdh3MkmUwfhVthAQ_IA_0-0pI1oY59KrRHFeIed6I3y0R0supck-Qe9K8gci1co-16J-Q9yC1hyiTu7eilbELqcTX3DnabuxqL7yr_yUBRN1HFhBFTIRVqlNOi1nQ_aX9SLpwR_pgrwQs7velQWwCwN4H84CTw6uJcdo862PsBOkjmw99hu_WOlmACRhW98XJv2h_ZEDacHyDMYZCQwupcNPnfyh3kIObsCLyFs8JM9-5q2YlX9obxsGNdTJoIT7kYcAFQRqvqeysT_baLLWRhP8Vg96dbA3sPg-pK-2v6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RhFs2sP4GLJlrnkaMTXl5lFJ79o2Wcr9LGm6rR7KZWNxPoDFhlsS8BWbDYWsoo0GDJ7yUqgZ6W7XybJQYBqXJ8hLVqHWNmh6azAorou1dA3wW45B_2G1jDTYRezg4_zeQ6I3vg-nWchp74q2kmQJyunkkr6pEuGIlk20CCE_I8lXw99Axws0gLCHrT9Q34mA7mgmpP9GgsmNdhENGoJ_HOS8JcOzxShp5okKmogAPElRFmi7v5eeAKm79l5qkAKXwvJ_G9lzAXeIBrQp3AF6d7aCTJd_n5ZvNL9ld3huN4T-YIRV8A0lGPA1JW1vuX_q1eLvaSAOjTiUqs7aOLwiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=ZU6CUaDEguRt2pXkbCAOpKzjEgZchsqwvB84jWBR_0TEAt-W62hOF0DpMSlG-rfxx6jr2l8frMJjaVp4BS329v_Ng345WD9yjODi1aPPAV72LTOVAadXVs1Dmw385j9c4aFPo_PFmxrEiqj0VvzcUWn_9Sh6GYkavqRmn-NhKdoe9jG4-hUw9ZgxbVNiSmsE4bcaGB2yjj5cB9fL7ZAVejM7Rj5QBReqqnIERRreKgxSD3qR9Ppm9tBczmX6c_J4vg4BCQbKi-NwnloKlslgSvL_BaFc1ETHl6T0kSFAHtruphwUy9e9cWXqJxk50Ps-rSrrg1RilYUrQJcfDdFUYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=ZU6CUaDEguRt2pXkbCAOpKzjEgZchsqwvB84jWBR_0TEAt-W62hOF0DpMSlG-rfxx6jr2l8frMJjaVp4BS329v_Ng345WD9yjODi1aPPAV72LTOVAadXVs1Dmw385j9c4aFPo_PFmxrEiqj0VvzcUWn_9Sh6GYkavqRmn-NhKdoe9jG4-hUw9ZgxbVNiSmsE4bcaGB2yjj5cB9fL7ZAVejM7Rj5QBReqqnIERRreKgxSD3qR9Ppm9tBczmX6c_J4vg4BCQbKi-NwnloKlslgSvL_BaFc1ETHl6T0kSFAHtruphwUy9e9cWXqJxk50Ps-rSrrg1RilYUrQJcfDdFUYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwPBqGzDHY2JuMlOZX1NOpjuMJF0zraJIr8t1_ApdRkgtBw5F8opQiZVkgMeJG8nN5yKNPN1PD7ZbyYO1lyXJZl9bMt8_HIZ6lPin8gRIVcBRxFs_qwj6E6LG6fuoQ7uApKL2bwDkCRLut7SUIBLbbsDf0bWOd0d0bnfJgO3RtJxzGbUzew2JDgThPb7CfFt2pzFcS0_cvWvmdE3XDTp4uy4h3LhIAaAg-6r6AtQn99NaqSDLuV3Gf_ClCNm9_5Xb4b8P3HQKpaO1XC87uasR-ORcOr0pZnmVGDNhV8PIF-O2ZWJQzR_HDrio3q9mFNaz7r9qFpF4QDAlQDFWmNCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7PXvYKgbYdkoUmWSxVdeVNuPf6Tfthue2g7nsv5qvupo5DcFMg8VQx_rYQfbhHzPwu-5xLaQ85KoSpqCPWlHj6MVYvZe5fJY2FNleB6ybTPjZxUvtgIH56WErAHyBSYbUk6q_zckdJsGTDqyMPJtkn0mYc-p3Al9xYwiGDbqeS_YY4gG8aTsj493Kbyo3rHDCCotbgfzVaNxpM52JF5itu16c1PYGzCFnbZtAHmrBbtNT_UFqfJyA9-aFJlWqmdfLTZ_Tb0AH8fs6M8ueC3nbLs6E54inuqc7YGPE5MsjPka4XGE2-Iy8e6jVhjmkv3KI_S0JvkSodMy3tN8FidGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=R8zkhPeqDjPffI1ubJjpcilSkko18LiCdMvzC92UyOVwSl2fw4Ec98B7Lya709TfNYEyc0cxugKnE1lJ2G9b9HlpzJ3G35xmnHlhLtcGojE-o3o83K1OUKCyZDGPb_geefHtnujkksHT0sW40lAHvTdUnURnR8NJNbCm1BSN-vJzjYbuAUqUPoJbpr3wusVqgfY0xggZuaC_4kYhRmeKF31ALBt4l81_SbCtMG165JxICeSHxMcZnTyDK0-q2TwhhEaxtWq4pVEFHzZk5Ecglw_xCUBXAxnV73O4rAuXu3Q1EKvkq0ra6GII_Z9NucOhcwPyf9l5ZVhFWuK46bo-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=R8zkhPeqDjPffI1ubJjpcilSkko18LiCdMvzC92UyOVwSl2fw4Ec98B7Lya709TfNYEyc0cxugKnE1lJ2G9b9HlpzJ3G35xmnHlhLtcGojE-o3o83K1OUKCyZDGPb_geefHtnujkksHT0sW40lAHvTdUnURnR8NJNbCm1BSN-vJzjYbuAUqUPoJbpr3wusVqgfY0xggZuaC_4kYhRmeKF31ALBt4l81_SbCtMG165JxICeSHxMcZnTyDK0-q2TwhhEaxtWq4pVEFHzZk5Ecglw_xCUBXAxnV73O4rAuXu3Q1EKvkq0ra6GII_Z9NucOhcwPyf9l5ZVhFWuK46bo-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=T3BHb19aVMlad5__wBHSb1D01DXZHof_UDs0syEkG1rLxz6bW3cUK6MDf3D0ewJ6BMzpbtsRZhBB0QohyqzukkLkbomY4E0iG-hSlMXd78xj4P3FaCOWa-3sUfMqAs2OGjy-SeXyc7cvrzTfqJfRZeutiqc1Duf2hr_Mm7R1Wxya34oYtzMmBYb1j1ow54mXm3oBveD5EyPCte5tB9poHj4rgjofXU7gE3IZ_gSJiU2LF36772w_4dX9URaovcZyAM9deMpuERlguiIWRewRmKcUT5-4ikVMbi3I7oD9mmj-iRApJ_ECMT42IberxZhcPEU4WaQbW-xiEQcexJUbsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=T3BHb19aVMlad5__wBHSb1D01DXZHof_UDs0syEkG1rLxz6bW3cUK6MDf3D0ewJ6BMzpbtsRZhBB0QohyqzukkLkbomY4E0iG-hSlMXd78xj4P3FaCOWa-3sUfMqAs2OGjy-SeXyc7cvrzTfqJfRZeutiqc1Duf2hr_Mm7R1Wxya34oYtzMmBYb1j1ow54mXm3oBveD5EyPCte5tB9poHj4rgjofXU7gE3IZ_gSJiU2LF36772w_4dX9URaovcZyAM9deMpuERlguiIWRewRmKcUT5-4ikVMbi3I7oD9mmj-iRApJ_ECMT42IberxZhcPEU4WaQbW-xiEQcexJUbsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=Aju8GyrEkn4aCplq3JMpq5OneZ7wT_b_ZLbEqzThxaZBRVVNfpXPfqnomBmc6YAp3OCuBdsT9rf4-Vp6xnDtOIXa2xcDWveB3nCGfoxiikqpsJ4vh8cs-N-MKcJeVV2Yx0PVswle4TCBWv14UeZ0i3WvsFq8eVZQObofGp_GpFmmTchu0N2kScgxtxL49MmKPHze95hTgXM3M-KVYaXh78qEPZ22gp0BVBF-Egj4ZtHaX_We5meMqoib8UTJrSaPamFl5ElNf5UgVHg9zO220SmEW-dWhq9EyjjvudIEre9x05uR72MSxACJUMlqsGfTimGMndy24VAS4bcFeFRoTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=Aju8GyrEkn4aCplq3JMpq5OneZ7wT_b_ZLbEqzThxaZBRVVNfpXPfqnomBmc6YAp3OCuBdsT9rf4-Vp6xnDtOIXa2xcDWveB3nCGfoxiikqpsJ4vh8cs-N-MKcJeVV2Yx0PVswle4TCBWv14UeZ0i3WvsFq8eVZQObofGp_GpFmmTchu0N2kScgxtxL49MmKPHze95hTgXM3M-KVYaXh78qEPZ22gp0BVBF-Egj4ZtHaX_We5meMqoib8UTJrSaPamFl5ElNf5UgVHg9zO220SmEW-dWhq9EyjjvudIEre9x05uR72MSxACJUMlqsGfTimGMndy24VAS4bcFeFRoTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=eNhF7HZLzCoyhzAwSkUarplqFO3ad5Lle5MZLykr_ODDpKDdR7VaoGu9WbybPTLOMEsrtx1L8qbagdrS73OPySKJja2rAdWS-8XoXikyHrUNhmfAoH_JvQsX1_Mssl_q0X6EDNx3xUU6aNM7dwMCNnIMK5iRIqi32OC_4ubnlkRec9Jqf8_f4gKayXU1tpWiJE6SmPY_YmSstXQ5sBaaoMByRIBj7OqUBGSWX_jbqWkf6aJ_CcyY_Dd8u_5RuiF3hQb0jY_mDjXYoDpWDvCvBiVU7wk7bynB07OrhS0CYmJtJRaMRA4_f11-qpEmhR2JUF9YfEof6v68NCRS_pdSjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=eNhF7HZLzCoyhzAwSkUarplqFO3ad5Lle5MZLykr_ODDpKDdR7VaoGu9WbybPTLOMEsrtx1L8qbagdrS73OPySKJja2rAdWS-8XoXikyHrUNhmfAoH_JvQsX1_Mssl_q0X6EDNx3xUU6aNM7dwMCNnIMK5iRIqi32OC_4ubnlkRec9Jqf8_f4gKayXU1tpWiJE6SmPY_YmSstXQ5sBaaoMByRIBj7OqUBGSWX_jbqWkf6aJ_CcyY_Dd8u_5RuiF3hQb0jY_mDjXYoDpWDvCvBiVU7wk7bynB07OrhS0CYmJtJRaMRA4_f11-qpEmhR2JUF9YfEof6v68NCRS_pdSjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il48pm_6KC8Z7p3PW9YxWJJTuTj8Km6oAeJaFM9LwwKe4ogzKHr4q-JJq-LxFYRxbTzkdbi0IJXNGo2JAhvmMdtriWtuf6-ZD5xOXO2mfYNTM8slk6VDL8qF9vDis5stzMuvO6zPv8IeQ3WG1rtvn9G7a4jQMXr81BV3PKw2aaZC0MJ4T6g2yTMBVnMKf0h1ysvC3w8qDyZt8xX3D8JjlMXWejeTfYz5x0CQX7ExVoeUJMYjKxKHdOxXNLS2V_D7t4fVHj6avjM4vdYFN82XxYYeKXphHAHDVvoN9aoRb3h4c5MX7xzfvYKDcGOQ_gC2ZdRRD16dGkwTPxvOd_Vx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=t1IbHBsqod7_JTus4e49tirgJzTJ8q-rBBG1Uk2OFqNRrBtS9U3lbZWeVoUiUBEQ3pTWrSjGADBlv9rmg6WpAwOXS4P7aIo-YpqOZnIDlUBNXOziGc-EcaGgm3s1pp7_t3K25mrC9ubcWCAGxRzkh5EC4YOVlhbBfPGP1KlsSu2sAUnIIuuaX4STeIm24vPoahIFEYW8dgvilsj_RgpLL1FLSb-kDAMCsXAEHhxAJMeF5sSgArVwbjGIvqDK5Xq1L2xbWEAQfYultjfWZc55i8k1T0lc1m-uz6P2q6B6IsnDdCh39DQN61TCYufm9urVkU7GoZzreqU1NH22nbbxZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=t1IbHBsqod7_JTus4e49tirgJzTJ8q-rBBG1Uk2OFqNRrBtS9U3lbZWeVoUiUBEQ3pTWrSjGADBlv9rmg6WpAwOXS4P7aIo-YpqOZnIDlUBNXOziGc-EcaGgm3s1pp7_t3K25mrC9ubcWCAGxRzkh5EC4YOVlhbBfPGP1KlsSu2sAUnIIuuaX4STeIm24vPoahIFEYW8dgvilsj_RgpLL1FLSb-kDAMCsXAEHhxAJMeF5sSgArVwbjGIvqDK5Xq1L2xbWEAQfYultjfWZc55i8k1T0lc1m-uz6P2q6B6IsnDdCh39DQN61TCYufm9urVkU7GoZzreqU1NH22nbbxZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=uxPHvnBT2f-HMX1BCUu0GNxJI0Q2VSv8PU1Kp4sQfdH3p-JirytwzhHG7o4mO32z-98-01VA2xa96dW-cWdOYXPyxjs2RcjGopVwxt_zXcM4PUyVIFBEpaAJF_SwAFoPUgISWVFxRJ0GGGCH6JGQ01We0mQ4PNVu0os1qsyleadfzKvEUsv1mJPeEpag38CLMgZoHNcVg5-50-uCF50r16_IEvmJHxxuBtiyQ8yENukwieylrOJzs1Yq-h0s5K5DZ578yuSwKZEknGX0LG46p3MRYwnBTPCXSIK4haucjXd7128_uo5IRlwEr9bCMVLbkmDW2pj1BzfLmmLxiVzepw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=uxPHvnBT2f-HMX1BCUu0GNxJI0Q2VSv8PU1Kp4sQfdH3p-JirytwzhHG7o4mO32z-98-01VA2xa96dW-cWdOYXPyxjs2RcjGopVwxt_zXcM4PUyVIFBEpaAJF_SwAFoPUgISWVFxRJ0GGGCH6JGQ01We0mQ4PNVu0os1qsyleadfzKvEUsv1mJPeEpag38CLMgZoHNcVg5-50-uCF50r16_IEvmJHxxuBtiyQ8yENukwieylrOJzs1Yq-h0s5K5DZ578yuSwKZEknGX0LG46p3MRYwnBTPCXSIK4haucjXd7128_uo5IRlwEr9bCMVLbkmDW2pj1BzfLmmLxiVzepw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eckkDvl2hPGEb-1VnfhjqJcJ6pRBqJzVkcT4XfiaNL-5k7VuMMPn_6c9n5zgSg4T7y_is_oe36mp_d071-DiMlUi4w6QcwNyBZXQFWlZN3T6vGWEib1OK-xb-Fx6oKSfw3Oj3CM_DHQ_l-SWqvPr2UAAaQ7WpQlfVenZ8i43oPFraKH3EknRh8tYXecKrHQP6ublYVNnIPsy13nM1kottbIV_yx2TgOpr9KmJiA0DXHdXVeN1_qHwgGcMYoGqxMQUwZ3QGjinaSg3wrcQZrPM-OGOUMff0am_i1c0Ho217lqAvJRPkEyXn3hLwAjCu15Q-lsANcQ43FX7atm3VBIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtRsHRs1mVr_bdQLfCbwdf_WN7B-sVcgq1Yv5oejeowK_ZrbszRxHcSJQXVnpjIs1a_hLBMLL2sQqjPE3JItobGnKbWkBCI3JAVzhXZv2P2u79Lk-g217E_NI1nhjsSsQwNeR6UZR5ZEq9NNeTym74atl18BvHUyCxalfcpUt0GFzyFRAWXzIUn4iln0qC5et1bRf8vuaYHy6OvxiJfH218ZYCN10ucsBOioD0w4b2Rs7veTMN54Gwvo00NFyLqbCgwAHCiPS5jhI4oT0Tv49ub8QY9SWDKfqHax3fganp8h6LhFvCW_AuoJoOg4UooyFq5P1Uv8_X4IaVGV072OdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f51P9nvgCdJnkVmqS-iX9pRUnKlSWLzWxVwEuq0GiVdQKiksgOyeZt0RBuClSk6lvLSf0_h7KXxcVVJZYMws_AGgDwJnnbBaRv9uZKchynWGAd-CHFMFrLyCkNxSIOKCXHCaXNO6AfSkYwVESJs57ADGL68Eb307VNF5mzDw_IZi0F8Oq-zQJKBUgeA0kHfVPPmCYvPQHv6AqzPjPYyZ6AvhY0HWlhebqgLVb2PM-bCA3vgRXP_EY8wlzliUTk8Kxjs43EMR9W-V09O-HnjaBE3R3sWfswl_XXZXf7kdOg7XdTVHm3cIQSvLbKy0PpmhtgMTKBgDcX9fnIO77gS3JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=GzHfmDYxSiIz2dumQJPtN3abmAsrsfiChLk1hIkUavNlWLqOpPqXlV5MapOCFelF6Op9JRRbdW8I3iaqePfXS31YLlfi7QElHc4XjVXuFNpsCi8gIO08xNqT2-04Uy2kwArLgTP8KWIg_NnOS6mgx1tnuGANBikBH2dcRRdYoahK7cOG2pM4RMSJZRTsP2r1QucwA0OIMY3ASiWs_gnPQafclphXacIvkcWp8_KMRs_JbJM4SXT97UZivKPRoph2cLSocZt6xVIOssHPEtuTQCXBMPMI_YF9b07Jj6k2eDXE4Vvf73kfTTb4DtDLQuSqTuReYxvlFDqr9FZknEByGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=GzHfmDYxSiIz2dumQJPtN3abmAsrsfiChLk1hIkUavNlWLqOpPqXlV5MapOCFelF6Op9JRRbdW8I3iaqePfXS31YLlfi7QElHc4XjVXuFNpsCi8gIO08xNqT2-04Uy2kwArLgTP8KWIg_NnOS6mgx1tnuGANBikBH2dcRRdYoahK7cOG2pM4RMSJZRTsP2r1QucwA0OIMY3ASiWs_gnPQafclphXacIvkcWp8_KMRs_JbJM4SXT97UZivKPRoph2cLSocZt6xVIOssHPEtuTQCXBMPMI_YF9b07Jj6k2eDXE4Vvf73kfTTb4DtDLQuSqTuReYxvlFDqr9FZknEByGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0DCIB_9dcxCNQeVjt3xyQEq3FCYbW_wp5h07705VJNPLYvrBqif-SxvcfydJE6LbDDQuBgPPkdGFCa-O4uKmIWuCM592Gy_yLBcRiDVsawTH35XvmQqhsVhbuVHbE_ZascKCPnD25PM8E29V6Sm0ylUHUXisZbwLRogOwamlh0GQV0QbAdXGJA8IpVddR_TW7kOCpCSbwxcKJ6_mmehtbAhNF9rjnBZeaCgoYzmo1lSN8Cysw9DYIAKu7lcFnee20LB8uO2esN0BQwsz1IBJvu3t8Nm9uRCRYHU7YWw2YVhDbOGsG3V5R5jtloPdHVCivoR5yppCu7njXn01sNViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=DKKcsg1puNlPWa0IaDr9qC1nj8zvuTKUgMnlTzdWyBzC0HoLi27PmoQCA3L_m5ulVifyhzVuPiWo8800Gb2YainDyuekJiv8VIbl2SALfNrQo_rVzKrsznYIRe7kkSDTCpHAdD09Vy03XQbaGx8CbjbzZc_x5g1naYCJtSFAaVRbcsV5vPgJFJQNZUk01fSr9M2qUcVPQ_dZTPLqp-ZtoV4Uu4O-J9o8-QFMuAbB-9h4L441gTddE7NZiLXM6cGiqZLfC1WfjVSZUB4DLynvZZwdMrhepWK0uAHhN2JEmcrCKI3Q1-SIZzXIT_sGjTKkC_rcdfCjrmKluZBiP1H1Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=DKKcsg1puNlPWa0IaDr9qC1nj8zvuTKUgMnlTzdWyBzC0HoLi27PmoQCA3L_m5ulVifyhzVuPiWo8800Gb2YainDyuekJiv8VIbl2SALfNrQo_rVzKrsznYIRe7kkSDTCpHAdD09Vy03XQbaGx8CbjbzZc_x5g1naYCJtSFAaVRbcsV5vPgJFJQNZUk01fSr9M2qUcVPQ_dZTPLqp-ZtoV4Uu4O-J9o8-QFMuAbB-9h4L441gTddE7NZiLXM6cGiqZLfC1WfjVSZUB4DLynvZZwdMrhepWK0uAHhN2JEmcrCKI3Q1-SIZzXIT_sGjTKkC_rcdfCjrmKluZBiP1H1Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=OAQR54MzVuXZaabCIzI4kPZM_eowCIkLpm2p26Qie8NT0ExZURFqQdR3ZjbtUnQKXBe7lw-yojBGeQa5pSw8OdmbkcsdosucJChbgrdYiMiv2GuTp1YbZhWuqEm0W4lUowEpt1BTYNDXjuE0CcilMYgVsr8cAFPmhou9yZ-UZIRR40P__-UwsTQsflIdzeZnYGmA_SbN7qCxQ4-aLsxTidHLbtP0UbdqAqQQRVt5yT_GmNPweXUu6pGcsulQIOkL_EoVwS9g0p1Li_DnILtFJTa8_ZF7nvdlk7m0cDB90bTDm6bhj16-ga63_sThYytdWMCUGUc0ke8FcVHOqdf9QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=OAQR54MzVuXZaabCIzI4kPZM_eowCIkLpm2p26Qie8NT0ExZURFqQdR3ZjbtUnQKXBe7lw-yojBGeQa5pSw8OdmbkcsdosucJChbgrdYiMiv2GuTp1YbZhWuqEm0W4lUowEpt1BTYNDXjuE0CcilMYgVsr8cAFPmhou9yZ-UZIRR40P__-UwsTQsflIdzeZnYGmA_SbN7qCxQ4-aLsxTidHLbtP0UbdqAqQQRVt5yT_GmNPweXUu6pGcsulQIOkL_EoVwS9g0p1Li_DnILtFJTa8_ZF7nvdlk7m0cDB90bTDm6bhj16-ga63_sThYytdWMCUGUc0ke8FcVHOqdf9QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=f0tHJcPkFpjicojisoR4lzvWT3gYa0C3OfgHW2C3uwFqrKwJPXXT2LyhWpsVm7yVP_mry1RPbQKwutXn3AnpE5ujT6c4aWGY5_DwiiF5Ru7BWUEtbIyG8VsLPwwZQovXFDZMbyFXPTFW4Kaxlcojuy13Ne8rL_Whrp1KVno5c9-fZNGe6i9oRKadQWxXUoQnVZIGBVdGERANRxs7H6hb7Y38kC8N6nZ2HbaaIPvLaJHWEnQ9-xuOPk4WkIhWwOvZ24Bm98BYqSB_BrQ1ysmlc2kx0mxKDf2DRl52N8sKYj4-OU2azwh1sJRk8cdjXkZG5FcsB3kQQO6hBngswxlCsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=f0tHJcPkFpjicojisoR4lzvWT3gYa0C3OfgHW2C3uwFqrKwJPXXT2LyhWpsVm7yVP_mry1RPbQKwutXn3AnpE5ujT6c4aWGY5_DwiiF5Ru7BWUEtbIyG8VsLPwwZQovXFDZMbyFXPTFW4Kaxlcojuy13Ne8rL_Whrp1KVno5c9-fZNGe6i9oRKadQWxXUoQnVZIGBVdGERANRxs7H6hb7Y38kC8N6nZ2HbaaIPvLaJHWEnQ9-xuOPk4WkIhWwOvZ24Bm98BYqSB_BrQ1ysmlc2kx0mxKDf2DRl52N8sKYj4-OU2azwh1sJRk8cdjXkZG5FcsB3kQQO6hBngswxlCsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=erSJ_540ssSOI5MGUFSvulA2X3ALb2SnLQT39fLXWXxOuxjh01quQ5PDqJIaWHcb2PZ9XKtE6h37aEUB6cSJQZepLx-iwLno38l9cXnO73xBxFTdbGqzaLXR4Ghy5el4SPaJtkr9BX97jORDdzUGMl9r350B-TuaAkdwKKX6axxpAOgm-_OUsarQYqLTIlJuoFlVgJ_VYsWcjHoDQaqeqMkB1kuLCFkZ70wCKZ4cU0y8W9gd8zUIFp_4yZe5jxce5OgVbVQLVwenreoYqaRy0x3nD-pAhRSYk_iTSFU7pdyfFwCwY3ayrflvTWX-Z3stVmY4-46rJPN4IIiFEGmbAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=erSJ_540ssSOI5MGUFSvulA2X3ALb2SnLQT39fLXWXxOuxjh01quQ5PDqJIaWHcb2PZ9XKtE6h37aEUB6cSJQZepLx-iwLno38l9cXnO73xBxFTdbGqzaLXR4Ghy5el4SPaJtkr9BX97jORDdzUGMl9r350B-TuaAkdwKKX6axxpAOgm-_OUsarQYqLTIlJuoFlVgJ_VYsWcjHoDQaqeqMkB1kuLCFkZ70wCKZ4cU0y8W9gd8zUIFp_4yZe5jxce5OgVbVQLVwenreoYqaRy0x3nD-pAhRSYk_iTSFU7pdyfFwCwY3ayrflvTWX-Z3stVmY4-46rJPN4IIiFEGmbAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwahB2LDppf7cgUHNhSzkFcFrKLN2RSmd9Mccmd3rYWeyIOHhMGI91fVR3dYMGJzC7MINAODJs35Co-r3-SbUfaH7ao6jI7OG85NF9iRTW1PjXYr3N4iTeNkSOx0qUUKJQ7UBa8yDZ5hAkkKQ4HFXfOIgMey2aZ-bCFmlRI897en72eaQrPS3o6LoKRi2SnW_JjY6gKZqe3rR8FGJThLkRxmRA-OLUqsRgZLG-O8wkViOTVggWfn4wWISRRL6x7mbIiyH9-GMWlrzMnXa5IaT3yzilxzB2GrUD2DVkIrC9F6_WiFxWa-CfNBEF6ETEp6eQlPqXGsSu2nmyCWIyCPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKffwC_G3vY-P8HIXEeH2GM5_gFViGbWb1_3lvg9infOGUIW92un-JOPcWh82GOpCKX2nG3VIWfc5wqDVDVV2j6RE9Nl2VWRYMDyb41191ViGLc_ihyw10O7tIGFIkPJoxl_NnkaC7v4tnkFjGeCLeEuC9GFni1J-yHsFlq9N-KC7JaNZ6cDV0fwCEKlVgXMhOsdqEcHRaYYIx6yh_uQTN8EKDOYK-x0PTVUuLHeukVGXtUOfoK0h1DBMYinIefw9WBabP-0bWVBRE88kSJUYNAhQ7h4NACbqQE_K70EasIijx8VVPdVxHcuC8eKNvRhL142cjkfDxvTKmW5Xg4MZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=bnSkvUlsD_Eg64PPCXKnV2-yp-CsNQSC_lby4ITR0aYg_wpxIe5ZELGWnf6xdAErl_cEHfr-FeR6WY0zDUOijYSQtEHHKWDHdfULA_gDpSgHv7UnHzZXpY7YpR8gdkHFueiLwHmjxxC2UTg0E98HJtAjPBQM8_Kvqf_djmRXaNBcGHNGzZcOSIlKZkGJwZebLMhecS1IAX6Xoe3CbFNDMrmEN5X7JDVDBgHDO2KTZ7SF9J8fmShB_UTnk_8UZLIKDTQTRTil143UKc_jZu3aWnqQd8U8M4DCoIKVtmE1E_xPi9CRbdiuFuCw0M4Qj3X3tmHbD9isOrbtdiT12-qxmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=bnSkvUlsD_Eg64PPCXKnV2-yp-CsNQSC_lby4ITR0aYg_wpxIe5ZELGWnf6xdAErl_cEHfr-FeR6WY0zDUOijYSQtEHHKWDHdfULA_gDpSgHv7UnHzZXpY7YpR8gdkHFueiLwHmjxxC2UTg0E98HJtAjPBQM8_Kvqf_djmRXaNBcGHNGzZcOSIlKZkGJwZebLMhecS1IAX6Xoe3CbFNDMrmEN5X7JDVDBgHDO2KTZ7SF9J8fmShB_UTnk_8UZLIKDTQTRTil143UKc_jZu3aWnqQd8U8M4DCoIKVtmE1E_xPi9CRbdiuFuCw0M4Qj3X3tmHbD9isOrbtdiT12-qxmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
مجلس خبرگان بیانیه‌ای در حمایت از مجتبی خامنه‌ای صادر کرد:
🔴
1. مذاکره‌کننده‌ها باید حواسشون جمع باشه و تحت هیچ شرایطی از خطوط قرمز رهبر عبور نکنن.
🔴
2. تأکید میکنیم که انتقام خون رهبر گرفته بشه و ترامپ و نتانیاهو به مجازات برسن.
🔴
3. اگر طرف مقابل توافق رو نقض کرد، باید سریع جواب داده بشه؛ همچنین باز کردن تنگه هرمز در شرایط فعلی اشتباه راهبردیه.
🔴
4. موضوع برنامه هسته‌ای ایران اصلاً نباید وارد مذاکرات بشه.
🔴
5. کنترل تنگه هرمز، گرفتن غرامت جنگ، آزاد شدن پول‌های بلوکه‌شده، لغو کامل تحریم‌ها و خروج آمریکا از منطقه باید حتماً دنبال بشه.
🔴
6. مسئولان نباید حرفی بزنن که دشمن احساس کنه ایران ضعیف شده.
🔴
7. در نهایت، حرف آخر با رهبره و هیچ مسئولی نباید برخلاف نظر ایشون عمل کنه.
🔴
8. گفته شده دشمن فقط دنبال خریدن زمانه و احتمال حمله دوباره وجود داره؛ برای همین نباید مذاکرات طولانی بشه.
🔴
9. از مردم میخوایم حضورشون رو در صحنه حفظ کنن، اتحادشون رو به هم نزنن و به حرف‌های تفرقه‌انگیز توجه نکنن.
🔴
10.  کنار رهبر و مردم می‌مونیم و در صورت نیاز به وظیفه خودمون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=KEtSh0xPRwN8afAgSSjMahzSEthx4PU7QXqBiO6dj1HdrkFt3oi4pKCFZMeStDnV0F_Opa9WPdYrD2EFIa1kuKkdqc9Eyqbh6tXYG5pLPJ1Ci9b5vC_qakHwatQQUntM-k3FewPN5TQCfmclnHu-b-EmsIg0WL3HLQk7AcQENjZFRyffj71BT9BkNMuYjKn1Y0beHOcxqMTcaBBFzNz-gDdKZuGk_OepZAtRwjk6gfEZoei8vhDQCky8fYdryMB_gwxf0AzhZwqBMid0N5pzIeft8ouwKyKfst1HsRtlrsm99T4iCOx_P2lnM3l9rBfSAwen_tIF3WX2rYHwwJZfSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=KEtSh0xPRwN8afAgSSjMahzSEthx4PU7QXqBiO6dj1HdrkFt3oi4pKCFZMeStDnV0F_Opa9WPdYrD2EFIa1kuKkdqc9Eyqbh6tXYG5pLPJ1Ci9b5vC_qakHwatQQUntM-k3FewPN5TQCfmclnHu-b-EmsIg0WL3HLQk7AcQENjZFRyffj71BT9BkNMuYjKn1Y0beHOcxqMTcaBBFzNz-gDdKZuGk_OepZAtRwjk6gfEZoei8vhDQCky8fYdryMB_gwxf0AzhZwqBMid0N5pzIeft8ouwKyKfst1HsRtlrsm99T4iCOx_P2lnM3l9rBfSAwen_tIF3WX2rYHwwJZfSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سنتکام:
جت‌های جنگنده نیروی دریایی و هوایی ایالات متحده امشب به دنبال حمله پهپادی ایران به کشتی ام/تی کیکو، به ۱۰ هدف نظامی ایران در چندین مکان در داخل و نزدیکی تنگه هرمز حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران
:
فرزندان شجاع شما در نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی، در یک عملیات مشترک موشکی و پهپادی در ساعت ۰۲:۰۰ تا ۰۳:۰۰ بامداد، هشت هدف مهم آمریکایی از جمله پایگاه هوایی علی السالم در کویت و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین را هدف قرار دادند.
دشمن متجاوز که خیانت و نقض معاهدات بخشی از ذات اوست، بامداد امروز تحت عنوان مقابله با نیروی دریایی سپاه، پنج نقطه ساحلی در ایران را مورد حمله قرار داد.
بر اساس تفاهم‌نامه اسلام‌آباد درباره تنظیم تردد در تنگه هرمز با جمهوری اسلامی، از این پس با کشتی‌های متخلف با قدرت بیشتری برخورد خواهد شد و هرگونه تجاوز احتمالی دشمن به هر بهانه‌ای، حتی مشابه حملات دیشب به اهداف کم‌اهمیت، با پاسخی ویرانگر مواجه خواهد شد.
دشمن باید بداند که نقض آتش‌بس برخلاف بند ۱ تفاهم‌نامه اسلام‌آباد است و منجر به توقف کامل مذاکرات خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smXCW_gfWLLRJkZUkjjTRkb7XDSqmEO-CBMUgdTaQwotH1SsQGYD0Gydmf59GcEENz4N30R9qFHbUht7qfgxM5COUtdVGUvr9NHtL8HX1U_7A0iG_B56iH_SnTIcgmnJ9hGtKK-huVPa4yIcBlfG_LnlKIH-aKbb6n5ZXfKQ4ir75EPeAGNG6a4laqerQ16Tb5rEmAFqJVSfI8-4XPszK_whC2d9xtP3MTSjTMOqCvUrKXwxMFLQEMk-T1djMjhLVRYoCkHegxW36niZF43zhfCJIqWQQKE5E2dPvvBQYhpVMF_XUJf1W9U0c7nawoyHoyn4KjXtM-ISDKrMF_Rfhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=fJFcG_ZP0LoPeeJmNczJQ0AZQBlMTqkLoYodbnl9eq_1VQ86X73kXtjA8ILDZwUbzZ4gbjU2nRyl3Z0vnG-UFVgYx3dg4xflabPNbztL0P7iw5-LVG6yZQdULbJf8m8FHeb3iexrp2S2S7PIk6Kfmsouutot4n_cNotecUPMDE8RYZ8KePi1VrVfyu8g5C55E5pJ8GmnOz7-EVVchI1tTS6Ucfh2nMMYAT4soSRLKyA7TxmwJvmnqqqMMmm30uzKYdtYQu6tb_nbKJ80uWW6RT2iM21npV3VnEsMcJIIP3rJUdQ0Y5jDcBdy8FcnqoWMTIv3AxfMyh3suamsukbPoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=fJFcG_ZP0LoPeeJmNczJQ0AZQBlMTqkLoYodbnl9eq_1VQ86X73kXtjA8ILDZwUbzZ4gbjU2nRyl3Z0vnG-UFVgYx3dg4xflabPNbztL0P7iw5-LVG6yZQdULbJf8m8FHeb3iexrp2S2S7PIk6Kfmsouutot4n_cNotecUPMDE8RYZ8KePi1VrVfyu8g5C55E5pJ8GmnOz7-EVVchI1tTS6Ucfh2nMMYAT4soSRLKyA7TxmwJvmnqqqMMmm30uzKYdtYQu6tb_nbKJ80uWW6RT2iM21npV3VnEsMcJIIP3rJUdQ0Y5jDcBdy8FcnqoWMTIv3AxfMyh3suamsukbPoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من دور خونه بعد از گل سوم اتریش:
#haa4m
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=PerdbOmixV3jz3HNRR21a06eZqUdZaArvVDLn-WBKT1X64lopQPDKoFIzMg1qzsO2RbdRLVGbDYlyOd6a5y9-vvrtwsxBvx8eP4manLAYrguTNiqJUp1o_DpoI2SKC7JxxZIuJcUT_DdPqIcFjw2T83zP6si2N6anzReeSeREgqRfd3upyxS8Dr2pjt2DRTy8h8v2zW8Ffarye7JXGOTccI2XDUAAPgdVzoOKFYVsvtgg1TUvGDnR8FuiLx1XxKDOVAmxgyAoNDBup3tSJ0vM3ZGeI1gRcmsWbliBRZTBZWf_G-pWX0h5A_QCE9C_63t2iENKf-IzVxHYNKSavTCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=PerdbOmixV3jz3HNRR21a06eZqUdZaArvVDLn-WBKT1X64lopQPDKoFIzMg1qzsO2RbdRLVGbDYlyOd6a5y9-vvrtwsxBvx8eP4manLAYrguTNiqJUp1o_DpoI2SKC7JxxZIuJcUT_DdPqIcFjw2T83zP6si2N6anzReeSeREgqRfd3upyxS8Dr2pjt2DRTy8h8v2zW8Ffarye7JXGOTccI2XDUAAPgdVzoOKFYVsvtgg1TUvGDnR8FuiLx1XxKDOVAmxgyAoNDBup3tSJ0vM3ZGeI1gRcmsWbliBRZTBZWf_G-pWX0h5A_QCE9C_63t2iENKf-IzVxHYNKSavTCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا ابد موندگار شد این سکانس
😂
😂
😂
😂
😂
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=LRLR1SSMNW0bhciKVtqv8tSZUXT9SqEGmoq9j0MjWZBmto2E7SaKGCd9Z8P1ATeXHbm4zjFrkqGVmQz_rZwvLMD6QYxWAGsO7Vxk3uiDmntaWnDk0TBR3cAT5zcxqSpb6wIL-BGwB1Jhsr5keXdxOW-rJoo5wnKCpxndi0DjajmcspPPg9p61x4zGjtd1meEc2LhvvQVG4h52y5ljrjTXaJxQHj60Ua4MiGachRZtsi267gqHGGnlxG7nEWzBVK2ZbtTjr6xYEO2tfS1wvawedoQ46zZeA9ai8_nhsICVOQnlRztzB5RHj0V8cErQQ-fR7SK1ZlOvmkBmWD7rB2quQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=LRLR1SSMNW0bhciKVtqv8tSZUXT9SqEGmoq9j0MjWZBmto2E7SaKGCd9Z8P1ATeXHbm4zjFrkqGVmQz_rZwvLMD6QYxWAGsO7Vxk3uiDmntaWnDk0TBR3cAT5zcxqSpb6wIL-BGwB1Jhsr5keXdxOW-rJoo5wnKCpxndi0DjajmcspPPg9p61x4zGjtd1meEc2LhvvQVG4h52y5ljrjTXaJxQHj60Ua4MiGachRZtsi267gqHGGnlxG7nEWzBVK2ZbtTjr6xYEO2tfS1wvawedoQ46zZeA9ai8_nhsICVOQnlRztzB5RHj0V8cErQQ-fR7SK1ZlOvmkBmWD7rB2quQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLTO0yFR8ddYhfCdzh8oEGSc-MVrO5BIfpV2P5Y-hq3FZN0u2DPnQlOe6UbzJ0nbPc7Lfagle2Zo4MmHIP6tvojAw4ThYBuCDuT2XxJF_HXRP0j_J2u6WVO9Zqsh2g2t8Am0U8VrNP-xp6c2pOjuLfWF5aLzQR6oIvoHjtcxdSwFSL3WqDSYJef4v3s40DCz2VNfqsfE6u51tmsHLvwketb_nNZ0YEExqy3XN52wSy0drGGEHdxE6XXPbbHcD5g55CSI08RH_4p9RMxU1r6wPJUU2fa1GeSnhBRwUNafoCJtxPAzQnxw5dIZtqGKoltzd5WxalSKsl2fpcrjbs9k_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1w-K8530yF0BnazZkKq6WZPQOVr09FgTysQ83D_rLpwH_nn_0EDzt5hGcrTyQOH0lEGUb_0QhU9rqGhEg-GDuLhL04q2W2xepkkhB_t1LiHyu_A4f8-2fgrVdoi1QP65FBHj9oRTttQmlejJ7ZOlyJrLlM8c5uyUlMPk-6vt_q1uiwv2CVQ_r3X56PIyTb9RheM68cGIT-ALrYujv3-XlhzbZr-o18IBxSgakcHI2gyBGf04nOs2-dIT19j-mK22KZeB7ByjnXdxVsMkiELAhAeAFDDmnSLo3IUF5dCYcCCX0wTM8Fcdlvjp2zz2wB7O6T8pJuMySJPNmbrwTXSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای
😂
😂
😂
😂
یکک دقیقه مونده بود
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
اتریش
😂
😂
😂
😂
😂
دقیققققه ۹۴
😂
😂
😂
زدددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ot8DLUzfzmyGSLlsmbSyIzPVLvBm7cytovOBhhdBmbh6bKgfTLRSwvX_VMH18I92RoaKNp7dLEHnK2K0GWEPeuwY6JkqWGW0BtTo5Q3AUCFhYiTPaEUFmHteBVaovviFDXRgvnCUCcA9LK-TGdCLJuazi3m_05aIgyRFenvgBqiRV5K_ZlK51JkO4HwXOQ-X1foYWDez2XqaIvIDAiZs1sQU1jD4cc9rOUSR8TQmxU00c8JNDxP0B_ZiBPqloSldb2CFgBzK-HZjDwnIO7LwXYUlbAOhfX4BL6B2ofjP6PrNb-bS3eUVVlGJ7hN8jaeqhj48qn7Z8LbTcT5FFVOM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqT1-dc6ZqG7R4QbmtuaIMwJdrnw_RxJKO7aqQ4JgjNuwlUzObUPmBkW9FuaVeI_8Arkw1qQ14ou1vxzizavxUVaxWjWKfC7l959D78EQDn6L86Itl6j7rut37YBrjCUkN-ifi1SzF8xV6bgU7gd_z1DHUym8SkmAfWskLJtTJVqfCjlQSur_4e6JUeRmf967rPG990kdknzQUa0sDFd2u4_ITv4Fm7dSSBqu4V9Hen_OyZHavxTrI4ckEFgkCrr9eRMgr8MZN4m6TrGXrquKnjI9A1__VVw42p-8cZLToUNd3oac-xXOkUHKa60PNxYrsk2Q0RAO6VIMf_ZdSxmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=nDfl15dE5t7R9fxoX0WHnNJG5daCheRnK0oWM_mc_Nw-7Vr6LjbZHDMyF4n-W1-GRqvbGBBj4kgG_koyrtCq5lua7pATfdx_ipZTPBcjlncgpI54NN9PnW6dsMFNUTGOJz57Nv3DokOPYf8VtuW64guec2vjj4HhFOPPmRWoMITj-UqzVJef7HiE_qtZ1ZaL7ALdOsDdI4J5wxWj6xMDEBNnlVBqk6neFJcw3OsONvhPTnkS9txBWjUmouqJDMRDxfsc6TqB1TA0uMxN5D4s0SOzPqhVsKlaPIV6s6hmGuswdAwthNZbISQ3GAQWf5RglSIwGi-KJ__Y07MpOW85gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=nDfl15dE5t7R9fxoX0WHnNJG5daCheRnK0oWM_mc_Nw-7Vr6LjbZHDMyF4n-W1-GRqvbGBBj4kgG_koyrtCq5lua7pATfdx_ipZTPBcjlncgpI54NN9PnW6dsMFNUTGOJz57Nv3DokOPYf8VtuW64guec2vjj4HhFOPPmRWoMITj-UqzVJef7HiE_qtZ1ZaL7ALdOsDdI4J5wxWj6xMDEBNnlVBqk6neFJcw3OsONvhPTnkS9txBWjUmouqJDMRDxfsc6TqB1TA0uMxN5D4s0SOzPqhVsKlaPIV6s6hmGuswdAwthNZbISQ3GAQWf5RglSIwGi-KJ__Y07MpOW85gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ریدم تو هرچی الجزایریه، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIubvG3jw19W2HWjVshQMGvxKz_PsZc_o6a9k5gav4FSAkr2vGdvxuT8fOJ1AEC6txHZ_CbY7DzEyDlEYYkhw0U7w30M6sXSu8pGyoo8GDoSjd6NbSjBtitqrHGyGg1tYlzk03lWHrcV74NqXeG2Ia8p47UuQjLOivWW4GvhOJ5xIFB9_4rEc37BVF7BGQ7WbMIkst6KhONqOg8nBB_tIU6GFYs8TwEz-tfDgJ70xhq9BU1GmxPtcMNNn_rHIScDRWSil4sWWPrLpLRspRlkEjdeob8zENk3wjJqNjifWNcXSQ-5SCc9Q8pcSyzj8F6Gb9sCwYAHjqhcCANeBddaRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
