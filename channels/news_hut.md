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
<img src="https://cdn4.telesco.pe/file/OVmEd3_krpBPPz52Ay3BjEMPIvFNtYYtnEpNUqj6H57cVFgOOz0x4A8_tqojEk8LTGIHXG2izU4hwnWMol42fHmDR9dhpweat4v7SVjlMPTHApmIeCAjydF9WHhAILcdGIFEkeXWWve_RsGzKSBbk5bwWEfHsNRYKWZeWbRtQsrRQUgIEYTVrYiMPBgNbwJSLhfsgRE9GgyprpygdV1kDsR_b7cpGNMlHI83VsndwE98JyTnN9mT9zqwAx_DGg7CDJ_6hhBFLTU9wYRTe8Zv794p-wzY3-UbDK2POAK5SwnXaOKIo4szAubNb2j_eXUDE0dSkGktcuKq0Txd28iAmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 226K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 06:16:46</div>
<hr>

<div class="tg-post" id="msg-65807">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">در ۶۰ روز اخیر این سنگین ترین حمله‌ی موشکی سپاه پاسداران به کشور های منطقه بود
حالا باید از ترامپ پرسید، کدام نیروی هوایی و کدام موشک ها از بین رفته؟!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/news_hut/65807" target="_blank">📅 05:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65806">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onPHHRcDK63kmCQhYhUi2u98uLAC0S3cTuhJUA9cJYGA3Ogra5XLrxgg8ZVMc96BZXTnkL5QfND4cIoRA2wATGRxQUeC1rVrSGgjCm084DtbNC7V2UacKCU1pQHOilYK6oYvoUxfb_-eVsyFb1VbWMIriFWSg1yzRoVYzoFrCewW90nK8xjR57gMO393iDogKojcJgWAXk-mAntY7lfb2ux6beFJ_vJZ--_Y4f_39cYzL9pUtAVV2L4Sg5dcbC44bPf6pSesiWf_KuvEekEiajVZAIneNJJLtpRoAH0f8swehNpBkRNpsYrttxltYC3EvwpnqwCzhAG_d4WngZXjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کردستان
@News_Hut</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/news_hut/65806" target="_blank">📅 05:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65805">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7vOk8vnUfrJ5pHtU3etysgAMwNphcYcza-L_BNHx8S7mMlRrqgDuMY2gS5c1q0fRj7bukJvTfxwnGioanKWK3rj4ZLr4QpCGlJQcj0wIw4qjyvTZG0uPR4-8x-rE433Jx_mpHVesGGcu018hTlQOPUCjIPvyq2YFvmexESYRYbbmB3LbN4gmJawwu4wi-SI7L7B4gbl3zNDhYBy_qaK86tPIQdBVcUVkGOzTyAZsHgjwZ_m_wNpz-vX3xq4BNDIuMyy19jFg2fMlg4mTyUnijkIWAGlpXZMlEuFiU7B6jKFdqRs2sROlCGOag5PQzN4v-U1cM6agbb4EqzJTjDOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارومیه
@News_Hut</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/news_hut/65805" target="_blank">📅 05:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65804">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-uMOjukqTJVbc_QqDQXxRKaeLh7eMJUqisjEIGgsVw7r_EmxHDXG1Uup7ljqobFvyRBrIML3moGEPNjQzos4bFSnWh6cB6sYNTh-apeyiOx83OTpa_-ZfjcnJEqkrbweNiywT2VkRmjyXSytD94R4XaSnLKizS8wTPCdgulULokN8Uqn8jCdTjuMDI6GWA9sUcXRKdZnVt2RLRicUGo6Gb8jj85JWcBGvI4oVsInSQFnWoXVO6jWgFZt5yqzK3WpXpDghT6qraamRGkCBYBAfI2WYaICqPJ6ii8XKYfJPd7NeRcXAZ0lYwpnWwePHjBsVB35un6174TpxaKXe2liw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/news_hut/65804" target="_blank">📅 05:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxniB7i6yFlgzx1XA0qhZKwQkKgKqHU8FstOZ751UCcik5u_eDvEpmiyDIoTfkjVXcf89g4voyboX0jsoDc-CT5zRNMtujCudkTgmiDgQa_DkoR_mEFJXvp8OxjkhL70sfKTbm5DM0S2RU1m7jekHTGy_cf6Jqi6yXOh_5OpmxxSuQrgKCX-s3JbiIAVQ7u3cft6wDYEVrmprCS1V8FpTny1qxIxOhLhAUEPu0-h9ONwOMN7ygIIiOy0Dom7KCxAQQv_BsoDKM3h7G26zeJk1VQRh1p3_u_J0JyKO4t8-LCKMvtBqy7vtrx9qPc0D68tN62j2s6d1m3yYyPVvHPdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زنجان
@News_Hut</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/news_hut/65803" target="_blank">📅 05:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l94mlJdY-mFeO5yTZVLWNGNeJeTaDCrPG4zpWCYprPtKYwpWKJi-NK6n-bQAOtgwl72DEfKo_tyNtxSuzYrrl0HKNlVNAMgdF4vQMyie7KEl4wQV7tyTy4i34wctkhHQRNnddzt-cqf1Z6QW9f8dvEbzmz_IQFxT_oSW0UcrJhFiK6XMNkXARrYNVuWnJYsaK2RavIpIjrWZr8HJ5eVtoqdOrlNoIfFNJF9mtJDhNjJ2lAhkJjhny5XPEVvfdqo5bJ5TqaPacR0XTEHGgmuDKy-bNzyykzW-Iz8YukpcsNh9TXCDqffyJPdeFUbAPeOdNs2IVeKVDUBI6s-LKg5WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون خرم آباد
@News_Hut</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/news_hut/65802" target="_blank">📅 05:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین سپاه آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/news_hut/65801" target="_blank">📅 05:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔥
فیلترشکن پرسرعت و رایگان اسگارد
• نسخه 3.0
متصل با همه اپراتورها
✅
کاملا رایگان
✅
بدون قطعی
✅
بدون محدودیت حجمی
دانلود مستقیم از فروشگاه گوگل پلی
👇🏼
https://play.google.com/store/apps/details?id=com.vpn.esgard</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/news_hut/65800" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/news_hut/65799" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AokuZn9_taA0JlVZcwlkncQ-px2-FoNs2yEdEDVRyU1bVr5s7dRD-oVpLd99TbZSWMiFRoaZXtQyyBlXW-5gniItR_BugbaZEE56jm5Chx9OmdeVE9mvBcwYrb1ctxXtxP7p0R5X708-0lq003u4Qk_8EVQFVd6h-wcyIeMoc7Oc2INsCgH-GcFkMa_U6rtrzGTw475wVNrcOhG_GjO39gl4w3IGdMSHAFSU2Cqtfq_Fd65340C-jBoR-CdnPP0VuFF0FLamxqEArssHJg1dOffRlW__BJnDiSrsYSp45wf2xgLht5qBJtGKkFaThU3KJr9VRiqB7VzvgQWW3P0LfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/news_hut/65798" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65797">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
ترامپ:
اگر ایران توافقنامه رو امضا نکنه، فرداشب به بمباران آنها برمیگردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/news_hut/65797" target="_blank">📅 02:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65796">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
ترامپ:
مستقیما با مقامات ایرانی صحبت کردم
«بمباران به زودی متوقف خواهد شد»
@News_Hut</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/news_hut/65796" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
قرارگاه مرکزی حضرت خاتم‌الانبیا:
نیروهای مسلح جمهوری اسلامی ایران به هرگونه تجاوز و شرارت ارتش متجاوز و تروریست آمریکا در منطقه، پاسخ کوبنده و قاطع می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/65794" target="_blank">📅 02:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpxQWFoILnO90EdQ5GuJKiGHrCGH--hpKSBzwtIxfYO6BjjyqxHNdhndyDt8Br4irUDHgTIHAYj5vnk8ZMNKn9vUPlnaMST8C_laVx6xmFpl7kr9qivRHv2pZ-bo0ohqONDgAYN6Eg6J2jr0G7caPEI2xudme-29sj5c1PFHBebBOFbVimljflJPfJ_uzkLw1vKCrzHmHZEHhFzuxuLVFfT1U0bS9ZR7CSBKoqv-pCyGnkg82dmvRs_2HwxKBAViEiJxoCzAOjBOTV2BHT27eve4Yd9A4SgtgkP5XN6Q9BZZ7tO4HqI2dN93IMRynMQdhdUNRSVlMdTBcDsrhwL13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مارک لوین :
دور دوم حملات به ایران همین حالا در حال انجام است. من کاملاً موافق آن هستم.
من درک نمی‌کنم چرا حملات ۴۸ ساعت پیش اسرائیل، که در پاسخ به شلیک ۱۱ موشک بالستیک به کشورش بود، این‌همه انتقاد به همراه داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/65793" target="_blank">📅 02:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65792">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هاازانفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/65792" target="_blank">📅 02:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اگه لازم باشه آخوند حتی تا دوسال دیگه هم مذاکرات رو طول می‌ده، ترامپِ جاکش تنها راهش اینه یه لشکر ۱۵۰ هزار نفری آماده کنی و تو تاریخ جاودانه شی
🌂
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/65790" target="_blank">📅 02:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
نیروی دریایی سپاه:
دو کشتی که قصد عبور از تنگه هرمز رو داشتن هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/65789" target="_blank">📅 02:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65787">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
بزودی  @News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/65787" target="_blank">📅 02:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65786">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1713aa9451.mp4?token=BjrCWt7Z3s3L2dXr5GhHVXBM1mrLnoWcLa0EXHGPzsmDPzq7f1u9poDEM9FcuLZgyGb2qtD3PBCmkwVPw0YLOuYBddjuPfS5RAGQEs7ERNX2UjN1evWAIzyCVm2fEfF7NBJfRFs_votB8EWphjlujiuzw6vcnjxFf7kod8pFgaIFhy42iyRV_6lesy3qwd_GzleOsub04TqkfGI1QVhUxC_hcp3KvccYWUFMmneow3Q1w7A6t4PLXUMn7eN5blfcpCdTo1licy3IVx-PIShJjDoorR_GXPaOkQHniLBboj9KANh5DOq2wQZWNh1bFkAxySCFVl5Cw9ZfCv5D8Vaivw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1713aa9451.mp4?token=BjrCWt7Z3s3L2dXr5GhHVXBM1mrLnoWcLa0EXHGPzsmDPzq7f1u9poDEM9FcuLZgyGb2qtD3PBCmkwVPw0YLOuYBddjuPfS5RAGQEs7ERNX2UjN1evWAIzyCVm2fEfF7NBJfRFs_votB8EWphjlujiuzw6vcnjxFf7kod8pFgaIFhy42iyRV_6lesy3qwd_GzleOsub04TqkfGI1QVhUxC_hcp3KvccYWUFMmneow3Q1w7A6t4PLXUMn7eN5blfcpCdTo1licy3IVx-PIShJjDoorR_GXPaOkQHniLBboj9KANh5DOq2wQZWNh1bFkAxySCFVl5Cw9ZfCv5D8Vaivw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزودی
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/65786" target="_blank">📅 02:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65785">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تا الان ترامپ هیچ اظهار نظری نداشته و حرف هایی که بهش نسبت داده می‌شن فیکن
#hjAly‌</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/65785" target="_blank">📅 02:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65784">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
شبکه ۱۵ اسرائیل :
موج اول حملات به ایران به پایان رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/65784" target="_blank">📅 02:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
صداوسیما به‌نقل از روابط‌عمومی سپاه:
گفته یه جنگنده F16دشمن رو زدیم
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/65783" target="_blank">📅 02:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65782">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کصننه هرکی نیروگاه بزنه
#hjAly‌</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65782" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65781">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
#فورییی
؛فاکس نیوز:
اهداف بعدی نیروگاه های برق ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/65781" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسرائیل هیچ نقشی تو حملات امشب نداشته
#hjAly‌</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/65780" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65779" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWgI8HsaOMs9e0MeQt2BOK4NK-F-MM_OX9f7lJj1FMyX7W2cyXsr7juXxxxIYQxzTMRS9C_wpT-XCgnWrZO0QfjI-UVmcWzmmkwBxAbYRlO0dVdAcdqH8uTF3A3cuIpr188Z3dDsX1vNLNcdq3AQBs-4KlhY9wYQZZt4mA41y5gF-Mxml8v6Kf6UyKPr4cROZUtJGJJSLYe7J87oUVpR5gypSyEYiOuAnHuV_m_ctnbSz2LR8aSfBZxZJ_kefuDhijaeXXFnXuhUDhiOUSiY5cUWGE_rSG2JPrjF9GFaxiWbRwfkNSxeatYdCU9WVi84_ZXB32oLBzblFwT2qugabA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یدیعوت آحارونوت مدعی است که یک کشتی جنگی آمریکا در تنگه هرمز هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/65778" target="_blank">📅 01:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTnZiFbmMP6i4MeJTSkvl-DlepY9z6Ifou_ZqavCIwdRJz7g2hR44u1vOBf6cX4ISpx2TkAGhFaFOZzh6ULzNgW_icD79juoMOKsSE6koyy20Y-WmbuKMxxQoiHKSwW8GDIxSGPjUNMHswgTs23eFPfeeUCeihmJgTlkQRKbKFX2iWHTj7CG5Q48umek4pgGvNkW540I_fBZJPmSpVKNgeVbqVoObjbYr3ePxdxkzMsyTecbdFJpQOjMS5gFDfjkg42qQQn81v7t4_EoPgxqusiNN679HjoON8VNMtC34HOu9pvCpuwC0xGaaT8TMMjQ1gZ4H8hmyYW2jPyeE1a7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خبرنگار المیادین از درگیری و تبادل آتش در تنگه هرمز خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/65777" target="_blank">📅 01:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65775">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2C-4gOBRu15OzSP8yYzUHvWCU2Z9jLZ9xW2U_4F9QAovQ9mwSsLQHATN9cIvFCIqKV_FpiBzSj8cVrV3rnYZ3Xqnjv7iT5ASHaz8RoqHPx_S93lq9EBVbcA82fw3hqzf0_jjInK7gs3fuDnG-XcOLCT158i1qBS2aicdO11J3zjKSV6MF4gmgIoTGkHCmX3rayn9eAL-WQl200dMBCKRkTl_pa23OcnItQrxn1gn_RzKtER0SORNApT9A2LDBD2ntjG1U2n4U2k0cffk1TjOCuNMwAJzRrp1OZI5S2ZLsZjETSOdGcVaFcUCFo5Sz6s_4G5PuzHb7qc7KMuAwE87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzvRyReV-YrqdcQle90sxmWkXmHSTwC3193pxRZqqb2VXiDrYVzdqc_pCobrgQTHtHkzh7HUD03p7M1gYZroPUi87sSRsl0CrCzpEq9Pi13-V1u7Q9WqYfyAEAMbMZ8zTpu1j5wNonzirh3-uc1JgVebZsDmVAPTPDSWeBPwQAWjUgXUveogDU2-6krKnfacDooaj5TxtCq-EaroKmSu975besElU6r7IUifDNDcyTBh_mKNeSZ_7zlAP6C8yTukwYuYm_556aa61jTfSsHauI3DQ-kqDFVcLq2qVxaxyOtZHyvzXgj2jLdJxuzJETs79YRT5zrlWUY9z8mPZPz8-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
دو فروند هواپیمای سوخت‌رسان هوایی KC-135R «استراتوتانکر» در حال انجام مانورهای سوخت‌رسانی در جنوب استان هرمزگان، غرب تنگه هرمز هستند. این استراتوتانکرها از پایگاه هوایی پرنس سلطان در عربستان سعودی برخاسته‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65775" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65774">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB_eT11ZU8C5Q6cZgXZ1Oc_Gc9xDFqyyPxvQ4YvzUgGJE2lVJeEF8rGIrscDRfCClASPtF6iN_qUdX_nUCrfcCHxFCKkRjQ79PSbk8O4qyVJ9fkFEco-bM7IH4F6YciQ5Fg4ULszv6cGPuas7YEGqOiWmupJ0Bzg9QM1fCs5luHkZy2RiEsVWcd9lRnNNBe9hdb6jCnxSluUZJAAuZ05FuEXyQD_NP_MwR2R9J78nqqVnEt0qN_kM6_FUeZ18mSpj7VnyQfHQ0wUQEYL8QllYyMooy9ZQyyQQhRaPZ25legM_sReH11EqigaOQbejpgtH14fxhoTjlNHzpfM7Hko8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دود انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/65774" target="_blank">📅 01:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65773">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=GTTBUrz8S-i3V82lYRZXlz1rOEVbe_QZki2bOSLA-vHQ7_7bYRARVgNCs2MB8kCP8pNhSWJGwtnN_KB_XE8C_4sgtZ6Yf59a0fhCWMji_Vo_VjnVadQ8aWrRQknpZBio7R0WTqqwTjuBhQpqqH40ZdYBcjMe5x2CZX9Yj9L8ifJnunoMO87k3xIbbhjarOClqUFkf_imLOrJsvCGB61nMY_1JJX8qqUVp6XQdZ7FAiyKoWVb0b6XYETkKID9Z7N7wReRJh9KsgKywuNgKwCu_I18F5scKTl3hrWH_4RE2vcbmlCqD_4DVQgQUIdqo60nRQsceMO5ez7MmfXBL5tRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=GTTBUrz8S-i3V82lYRZXlz1rOEVbe_QZki2bOSLA-vHQ7_7bYRARVgNCs2MB8kCP8pNhSWJGwtnN_KB_XE8C_4sgtZ6Yf59a0fhCWMji_Vo_VjnVadQ8aWrRQknpZBio7R0WTqqwTjuBhQpqqH40ZdYBcjMe5x2CZX9Yj9L8ifJnunoMO87k3xIbbhjarOClqUFkf_imLOrJsvCGB61nMY_1JJX8qqUVp6XQdZ7FAiyKoWVb0b6XYETkKID9Z7N7wReRJh9KsgKywuNgKwCu_I18F5scKTl3hrWH_4RE2vcbmlCqD_4DVQgQUIdqo60nRQsceMO5ez7MmfXBL5tRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/65773" target="_blank">📅 01:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65772">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
وقوع انفجار ها در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65772" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJajVGqy7l5dvNdmn2Ycj9quzexE-feSRYZ6eiBu-YkmsDx5WZRMKbkkT5zPWQM531hbsFnh7K5Jfz0BJqqydtSZog607iDgjko0GhuaWX4tof6hMBJSBkyKsNy1MVO94brMfSVuqPj-7aZC9izlBY7XRqYbJlRVmcsOrrCO9EFmh5vXnhXxTnpbcpid49VSlbtZ9liSa52vVeQjonsYCqMP6kP0700SnzAAKMeTYNlLtZwtZ0havVGxBFARhdlHfR6BbxU2xXgxCgfP6xxiORZOr8UCF0jw_p-Oo2ru-fu_Ba8tmjMvKuR1MJe5vNMY2sOPMnmnGR8Vs2EvfV_sSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توئیت جدید سید مجید موسوی
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/65771" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65770">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
گروه هکری حنظله وابسته به سپاه:
آغاز پاسخ ترکیبی، قاطع و ویرانگر اتاق عملیات مشترک فرماندهی سایبری حنظله و سپاه پاسداران به دشمن تا دقایقی دیگر رقم خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/65770" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
حمله آمریکا به پایگاه شکاری بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65769" target="_blank">📅 01:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HD8vZMxvSps466z0pcnd2pQtrBoIRkAnSUkysz5NlWy5LG47KNn0YtQQC6hc41nrsDalIoKi_3aWuxbLXY3r3432PlhmDQrfr_mIHRmEPM0er1CXvNOYtfW4L-AxmtUSCkwNy43BqapnISvqpuD48u6FJtp4z7lp0eZed4XhOVGKO9dvsOpCfqaM0AwACVkzQxkc3jS-gAOHIWRt8KTSlhYig_9Ox4j2pisyDV2jKl9yjsL8zrjSh4qlUvlzhPYDECKdbUI8SpGFebYFkJ2Ov68YgWHXzAGR2ODA7S4eUhHTEXOAifURGBMt4buRn4RXEX8QLIRedTjvGuf66IPk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا قدرتنمایی کردن برگردین حمله کنسله
😖
#haa4m</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65768" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65767">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری مهر گزارش داده که میان نیروهای جمهوری اسلامی و ایالات متحده در دریا درگیری هایی رخ داده
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65767" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65766">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHhoI3ABU6r-euvhU1UOLTooDAlJ39l9ireTxjJtyFN7jDf0zRryAukb6JbmtubyUGc7hunnhwExiKthYbvjGZC3h7LLJofnN8Ip7Je8R591--nGgfmVdsm1easYJTVoVP02YRlGCIGZZVu6OSwJ_w9_ZIQCNYOIRqYOB8kMA23_mitImcSrp7--cHMXlyi5_FeUyypmTysiqX9AXxSi7Edp3vWJBP9hObVmPqVQnE78Y-PQALgEHZ15MgOxiesz6JRc6FCUocttkpc-yI51SXpw3mzvrsd8Q0vIM_qO8no5ONTJ-B9Q0IxSYE432-dUZp5Q-jcaG7hwzYqrQ7Cmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مرد باید با موج انفجار کوبیده شه به در و دیوار، نگرانی چیه آخه
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65766" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65765">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
گزارش ها از حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65765" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65764">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
منابع داخلی:
تا دقایقی دیگر پیام سخنگوی قرارگاه مرکزی خاتم الانبیاء در پی جنایت آمریکا و نقص آتش بس
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65764" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65763">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
وال‌استریت ژورنال به نقل از پنتاگون:
این حملات نوعی اقدام از جنس «دیپلماسی اجباری» است که هدف اون وادار کردن جمهوری اسلامی به ارائه امتیازاتی در میز مذاکره‌ست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65763" target="_blank">📅 01:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65762">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
فاکس نیوز:
موج‌های دیگه‌ای از حملات در راهه و درگیری فعلاً ادامه داره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65762" target="_blank">📅 01:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65761">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یه انفجار شدید تو بندرعباس همین الان رخ داده #hjAly‌</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65761" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65760">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه انفجار شدید تو بندرعباس همین الان رخ داده
#hjAly‌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65760" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65759">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65759" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65757">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3VLTyCu1y5DJpANhkEo51BL_AsRsFqdNPvYWXhu06RhI-fU7RLEguDtysHLFCkHdCu5CWgEzpDpIaZJ3Ql9X0xosLbOL1O-mpX5cZyCacKo-01-iNs_hWJCVrHiDW-cOzrql53q9u1xwnxrMjzpcwXtpJzLBOIvCAhArecBriNm90IEDh_gR_8tf3SPilzmZdjv9yk5yTgv0PKwC6-qQX_Dvr-DH-br1jfgLFKFadJZ735lbg85M38ZyY7EeSJ2S61tvobVlL2mvhpBkCl3Qz0-z30ZuQosQuk4jy1ejEv-KCVVlUULOTjkDlJFcFB1nBrEVUHx5QfzIOhq1FmK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا وقتی یه ترور کله‌گنده تو کار نباشه واکنش سپاه شدید نیست، مثلا دیشب یه پهپاد فرستادن بحرین گفتن خب بسه دیگه #hjAly‌</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65757" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
هم اکنون یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه بمباران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65756" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
اون طرف اسرائیل هم حملاتش رو به حزب‌الله شروع کرده
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65755" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
حملات مجدد به میناب
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65754" target="_blank">📅 01:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تا وقتی یه ترور کله‌گنده تو کار نباشه واکنش سپاه شدید نیست، مثلا دیشب یه پهپاد فرستادن بحرین گفتن خب بسه دیگه
#hjAly‌</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65753" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
مقام آمریکایی:
این دور حملات اهداف نزدیک تنگه هرمز هستش ولی گسترده میشه در ساعات آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65752" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65751" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65750">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی غیر رسمی از وقوع انفجار در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65750" target="_blank">📅 01:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65749">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
#فورییی؛ سنتکام:   نیروهای فرماندهی مرکزی آمریکا امروز از ساعت 5:15 عصر به وقت شرق آمریکا، به دستور فرمانده کل قوا، چندین حمله دفاعی دیگر علیه اهداف مختلف در ایران را آغاز کردند. این حملات در واکنش به اقدامات تهاجمیِ بی‌دلیل و ادامه‌دار ایران انجام شده…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65749" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65748">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از شنیده شدن صدای انفجار در اطراف قشم
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65748" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65747">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5U1Rp2v5_A57NoTF_bVA7LVDTzWZrGBHTudNoWU3Zi2c43aU76cQ2nktGzVGNMKzKfUvJvnBZicS_UKAZDg9aBZcHvg4j1p9t3YZZjh5I8XMdS5FSHJw_uaDOsVDtf3pbDk70xAkF59iGRyedtda_VrTCQwweQAugjDBgqLumAxOY3aY8SJoRcF82W6_-vMbTKjdUxJgwAEmG8pwoSEfVI4NBbKORt1q957eNG9H47KiNTpc9d9gNFlIpJNWqsndoBA3IXOBNzNXKt8aNhdbVk7jxr5wZ-bpIuA5h_0yXcxyd5JZv6Dk8uKuXg1JzJFY-KEUf9pgI5GNiVn_rnuOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورییی
؛ سنتکام:
نیروهای فرماندهی مرکزی آمریکا امروز از ساعت 5:15 عصر به وقت شرق آمریکا، به دستور فرمانده کل قوا، چندین حمله دفاعی دیگر علیه اهداف مختلف در ایران را آغاز کردند. این حملات در واکنش به اقدامات تهاجمیِ بی‌دلیل و ادامه‌دار ایران انجام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65747" target="_blank">📅 01:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65746">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
مجدد، انفجار های شدید در بندر عباس  @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65746" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
مجدد، انفجار های شدید در بندر عباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65745" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
انفجار ها در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65744" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر از فعال شدن پدافند عسلویه
خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65743" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی تایید نشده از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65742" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
تا اینجا تمرکز حملات به خط ساحلی جنوب کشور مربوط بوده
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65741" target="_blank">📅 01:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در میناب
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65740" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ رسانه آی ۲۴ اسرائیل:
شروع شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65739" target="_blank">📅 00:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در میناب
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65738" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65737" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری ایران اینترنشنال :    جنگ شروع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65736" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65733">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
فعال شدن پدافند در غرب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65733" target="_blank">📅 00:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65732">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پاسخ به حملات آمریکا دیگه فقط جنگ منطقه‌ای نیست اهداف فرا منطقه‌ای رو هدف قرار میدیم  @News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65732" target="_blank">📅 00:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65731">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پاسخ به حملات آمریکا دیگه فقط جنگ منطقه‌ای نیست اهداف فرا منطقه‌ای رو هدف قرار میدیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65731" target="_blank">📅 00:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65730">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
سفارت ایالات متحده در بغداد: از عراق خارج شوید
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65730" target="_blank">📅 00:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65729">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: هم اینک صداهایی از دور در کیش شنیده می شود که منشا آن مشخص نیست  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65729" target="_blank">📅 00:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65728">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: هم اینک صداهایی از دور در کیش شنیده می شود که منشا آن مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65728" target="_blank">📅 00:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65727">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65727" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65726">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
فوری از پیت هگست، وزیر جنگ آمریکا:   سنتکام امشب حسابی سرش شلوغ میشه؛ چون ترامپ گفته قراره ضربه محکمی به ایران  بزنیم، و دقیقاً همین کار رو هم می‌کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65726" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65725">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuwZETNtFFZTqow_eg4Y4u92bkTw6TBehtm8sbcji5XXoeg6-BiVjqnwQhKFoN-tghqgMlEnlYfJNiRkuXHdRzLh9uu_T2ht3rxf0GFVrExQlaJn8TtbDoQ2YtgWAIkMDqjIBvRQ8AgDC7vgntG-xA6GbgoplqozdVsQGZ32LuHnjwCBwJNaY6f0uIC1gQnk2H1PdgQLtRojJMlOmIptysRGIYbjab6syl-MUxupxP765tvSrZxRCgqffaqvpulV1KHUjRS5SIGLrT763VaO-kkNS8HFvA0aCQuEbWFazlOwwU3zIGyfp3d3Ox9kr6fLgikdMnDXs62GTqvKts_bwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یجور مذاکره کردم که تو آتش بسم هرشب جنگه
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65725" target="_blank">📅 00:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65724">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=Dw5pF1YqJ8vngPYKG-IzHVojiJUQxnSELq8DhkLQsltUYSdem5lqTJkisbranauTxc4nFBbKMgSjGV-6egZfr9K7P3ei1I1-xAPt01NUCFFNiXddr6FnS-E067BU9soBgExPIMSoibOuy0F5ur8kYMy2gLtgkdLpWEWYqCgkQgAicZphQC4gmG52GZuQy9CK_TEjKKfXXJNy5OPNHgIOHj33R-K-X6FGuU3ZPQlhmEcawjB0x5iF_a0JMHnUAiIxZsdBnnS1YH_G9hLk8wpLS_9pNTAKgMVhRcUev9PBsVEwwt6LhZ_qtwfqJIQh49JvAmB8fbrfFsnrvScdtwvKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=Dw5pF1YqJ8vngPYKG-IzHVojiJUQxnSELq8DhkLQsltUYSdem5lqTJkisbranauTxc4nFBbKMgSjGV-6egZfr9K7P3ei1I1-xAPt01NUCFFNiXddr6FnS-E067BU9soBgExPIMSoibOuy0F5ur8kYMy2gLtgkdLpWEWYqCgkQgAicZphQC4gmG52GZuQy9CK_TEjKKfXXJNy5OPNHgIOHj33R-K-X6FGuU3ZPQlhmEcawjB0x5iF_a0JMHnUAiIxZsdBnnS1YH_G9hLk8wpLS_9pNTAKgMVhRcUev9PBsVEwwt6LhZ_qtwfqJIQh49JvAmB8fbrfFsnrvScdtwvKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فوری از پیت هگست، وزیر جنگ آمریکا:   سنتکام امشب حسابی سرش شلوغ میشه؛ چون ترامپ گفته قراره ضربه محکمی به ایران  بزنیم، و دقیقاً همین کار رو هم می‌کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65724" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431e022a4d.mp4?token=RLVur8brdnVnVODPoW7BmT7fDG6a_R1S95nG6wsS64o_erkqsgOaibgUoE9SWX1ZWping5AnyKWzt7ZrghHegdVHLy66LNxtMl2HaJ_ormwc4vHSvTWKkWXbOys_Rv0JVw_Zus4HKpy_IhyV3Tf8uwAdfXI7t_p2Xbb_DNf3eJxyJfOI-q7tRKlIqv7RJLt5oniMv7U22d_0Kvi4KH_XA0_kU2MXKqaJxNLCn6b6gDOYtzYToPKraYDOrdMv2zqA3fR-Be8W4r7piQJmU02y9yHH3gVisaqxaKrTOcW-7VtUQ9Pg7Yj8xTbxNjknqgW3qFvzeMhCzZcya1QO0Syutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431e022a4d.mp4?token=RLVur8brdnVnVODPoW7BmT7fDG6a_R1S95nG6wsS64o_erkqsgOaibgUoE9SWX1ZWping5AnyKWzt7ZrghHegdVHLy66LNxtMl2HaJ_ormwc4vHSvTWKkWXbOys_Rv0JVw_Zus4HKpy_IhyV3Tf8uwAdfXI7t_p2Xbb_DNf3eJxyJfOI-q7tRKlIqv7RJLt5oniMv7U22d_0Kvi4KH_XA0_kU2MXKqaJxNLCn6b6gDOYtzYToPKraYDOrdMv2zqA3fR-Be8W4r7piQJmU02y9yHH3gVisaqxaKrTOcW-7VtUQ9Pg7Yj8xTbxNjknqgW3qFvzeMhCzZcya1QO0Syutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فوری از پیت هگست، وزیر جنگ آمریکا:
سنتکام امشب حسابی سرش شلوغ میشه؛ چون ترامپ گفته قراره ضربه محکمی به ایران  بزنیم، و دقیقاً همین کار رو هم می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65723" target="_blank">📅 00:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
ترامپ ساعتی پیش با تیم اصلی امنیت ملی‌ش در اتاق وضعیت کاخ سفید جلسه گذاشته
جی‌دی ونس، مارکو روبیو، رئیس «سیا» جان رتکلیف، رئیس ستاد مشترک ژنرال «دن کین» و استیو ویتکاف در جلسه بودن.
موضوع: ایران
@News_hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65722" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه دوش نگیریم؟
#hjAly‌</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65721" target="_blank">📅 00:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65720">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پیت هگست: بمب‌ها رو تق تق تق روی تاسیسات کلیدی ایران خواهیم انداخت!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65720" target="_blank">📅 00:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bnz-8GmQuDiZ5KsK_w29ncGXoE0JN1r51Lo5emsYDBFtYBvPrbeFJoqktrRRMvGEmtkdZRVZtF0KE1rFD5gSRpfWEJIXG5LT727boIQxotorhFLtqiGJSo8Mc3GfjwuYo-Hroe0AuOwpEvABrNrny9Dh-aidKxOjbvqsdVhuexERxhbZbDvqPmWoztnwjM8rvd1k47pdDATHjuCXS2Ci-YO42qC6HZy8BKAto-kshG20aHgdu2eu5UPnwXRa_tbk-3XLEIN0OBEj5t40NalbMKtnWYnGDm_ZfoLiYExpyy_ouAsCN9ZqvWpI8KwqueSOn4O3fzqh7MsF3ymK9X1DtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری؛پیت هگست:   ایالات متحده تأسیسات اصلی در ایران را بمباران خواهد کرد. حملاتی که امشب رخ خواهد داد، شدید و آشکار خواهند بود. @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65719" target="_blank">📅 00:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛پیت هگست:
ایالات متحده تأسیسات اصلی در ایران را بمباران خواهد کرد. حملاتی که امشب رخ خواهد داد، شدید و آشکار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65718" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65717">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
پیت هگست وزیر جنگ آمریکا:
همانطور که رئیس‌جمهور ترامپ امروز گفت، آنها معامله نخواهند کرد، پس ما به شدت به آنها ضربه خواهیم زد. سنتکام این کار را بسیار خوب انجام می‌دهد، بهتر از هر کس دیگری در جهان.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65717" target="_blank">📅 00:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨️
#فوری
؛ترامپ :
به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65716" target="_blank">📅 00:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
نورالدین الدغیر خبرنگار الجزیره در تهران: واسطه قطری تهران را ترک کرد
به گفته ایران، سند توافق برای حل برخی اختلافات که هنوز به دلیل تغییرات آمریکا پابرجا هستند، نیاز به کار دارد.
منابعی در تهران می‌گویند هرگونه حمله به ایران به معنای پایان اجرای آتش‌بس است.
واسطه‌ها در حال حرکت برای جلوگیری از هر درگیری جدیدی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65715" target="_blank">📅 23:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
باراک راوید خبرنگار آکسیوس:
ممکن است مذاکرات در چند ساعت آینده کاملا فروبپاشد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65714" target="_blank">📅 23:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
آکسیوس:
عباس عراقچی، وزیر امور خارجه ایران، به میانجیگران و ایالات متحده گفته است که برای دریافت پاسخ به چهار یا پنج روز زمان نیاز دارد.
این ماجرا به یک بازی انتظار دیپلماتیک تقریباً دو هفته‌ای تبدیل شد که در طی آن، ترامپ به طور فزاینده‌ای از پوشش منفی و حتی تمسخرآمیز رسانه‌ها در مورد وعده‌های محقق نشده‌اش در مورد توافق، و همچنین انتقاد تندروها مبنی بر اینکه او در قبال ایران نرمش نشان می‌دهد، ناامید می‌شد.
بدتر از همه اینکه، ایرانی‌ها در ملاء عام و خصوصی می‌گفتند که انتظار دارند برخی از دارایی‌های مسدود شده‌شان از قبل آزاد شود، علیرغم اصرار ترامپ مبنی بر اینکه این امر تنها پس از انجام برخی تعهدات صورت خواهد گرفت.
این مقام آمریکایی گفت که ترامپ از این اظهارات ناامید شده و موضع او تغییر نکرده است، اما خاطرنشان کرد که ایرانی‌ها می‌توانند با شروع به برآورده کردن خواسته‌های هسته‌ای ترامپ، میلیاردها دلار از دارایی‌های مسدود شده خود را آزاد کنند
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65713" target="_blank">📅 22:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65712">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
آکسیوس: جمهوری اسلامی امروز به هیئت میانجی‌قطری اعلام کرده که حاضر به برگزاری نشست سه ‌جانبه با قطر و آمریکا نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65712" target="_blank">📅 22:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65711">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
خبرنگار الجزیره: حمله هوایی اسرائیل به حومه شهرک زلایا در غرب دره بقاع در شرق لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65711" target="_blank">📅 22:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65710">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVnwbz3JQ3PnCncMAaJgX_fZpTAVgwXe7e7Ft9UeHzGcX7Ae9EluwccGNVQcT5_VWC71CVjv-oRenXzlgLhb28FX49PXGLzpw-sac_MxMsQbAM2bsp-S40gOzBQ2JywNjCE07svYGHkeUWmbyJV8gERCPTrnae-otsuY7k1moDi54zNjysN85t3oZxit5_xG1klopHXuwX7DcLPfAtgVLWQIPqI-v2sSY5WEDnBojiCpNr5b2gb3SE3nch3WabDErULP1ujxKhiL3QMzm541Zw1QaLAIwl8EEZdzo8gXGKm88SAPmpRykG15zW8T8YOjic4ZllY1PzKB2ifu9KSCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابراهیم عزیزی رئیس کمیسیون امنیت مجلس:
ما از جنگیدن با بازندگان نمی‌ترسیم.
تعداد تلفات آمریکایی‌ها بسیار بیشتر از آن چیزی است که ترامپ تأیید می‌کند و افزایش خواهد یافت.
این بار، جنگ محدود به منطقه نخواهد بود.
خواهیم دید چه اتفاقی می‌افتد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65710" target="_blank">📅 21:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65709">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_A8IwkdDYpJkZwakK7aAorFqOUcXhkIX2YGbH4KDA8Y_bVOFnqR6GkErkUmi8Vzdm7K5YXIu_XMoSIDt48HvyM3_GU05CYromp4eH-C19oXnQA6BNcTNIXMhBy4LyprBaOUjRm4BfyTc_pTgX5LGnROEToh8ExgMZNPL3qc5Srnb1EfGKhlm7cziq1p2aCv1k5iPTQe0vNJ3kgMuKLVk95ko00ORQ6g8_KzBiYJpR8umiUoTblqeWEdKmF15VtYnZiZeSc-epgLFv7KM3ZVZPDlw-URgl7A7cYrflG0qvqezhzll415dIjOWb6VZayAkTor3kI05z6q1TK6i9gx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
آقا بووووو میااد
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65709" target="_blank">📅 21:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65708">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
‼️
جواد خیابانی از اساطیر فراموش نشدنی صداوسیما میلی، اعلام بازنشستگی از این سازمان کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65708" target="_blank">📅 21:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65707">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JeJtSeVhzXdD9rJeId7yEI34HT4nkmzgFDKVrPv4LcUTIoQsTbMjlN8F3LlqKVX332tMb8bRjhpelsGY7l4RkbBdZ4TdecRwZ8aURxt7eVGQDfdo_qhBZm9jlF7DXi6gUrDhg0oiYeo9GF1pPcCFqR-62ZWnIuh6WdouSWo-KDDn5be96iIYF-DKVhSoAL_Snx7rSPbczX4gN47T3NXm5qQ8xUUS_s5TUb7WjXXSX2Wz7ygJ2rsSdfyWunA8HWGt0tkE6NX3PcCK-Aer5wcBCJm70gDApT-zItFSEUqUDKcTyUxDhIV6UdZ3Pf9izH5QJuoScltySv8_s9yFJ-KPHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پست ترامپ:
ماه گذشته، من به ارتش بزرگ ایالات متحده دستور دادم مأموریتی محرمانه برای حمایت از نفتکش‌ها و دیگر کشتی‌های تجاری در عبور از تنگه هرمز اجرا کند. امروز خوشحالم اعلام کنم که این تلاش باعث شده بیش از ۱۰۰ میلیون بشکه نفت از تنگه عبور کند و وارد بازار آزاد شود. بیش از ۲۰۰ کشتی تجاری نیز با ایمنی از تنگه عبور کرده‌اند.
این تلاش به‌شدت موفقیت‌آمیز به این دلیل است که ایالات متحده آمریکا تنگه هرمز را کنترل می‌کند — نه ایران. ارتش آن‌ها شکست خورده و اقتصادشان از دست رفته است. کار ایران تمام است
!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65707" target="_blank">📅 21:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65706">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یک فروند بمب افکن B-52 بر فراز آسمون عربستان داره کص‌چرخ می‌زنه! #hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65706" target="_blank">📅 21:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65705">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک فروند بمب افکن B-52 بر فراز آسمون عربستان داره کص‌چرخ می‌زنه!
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65705" target="_blank">📅 21:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65704">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
ایران ما، امروز بیش از هر زمان دیگری، به اتحاد نیروهای ملی خود نیاز دارد. با یا بدون حمایت خارجی، سرنوشت ایران در دستان خود ماست.
ما قوی‌تر از این رژیم فرسوده و ناتوان هستیم. ما مصمم‌تر و استوارتر از حامیان اجیر شده‌ایم که برای نمایش‌های تبلیغاتی به خیابان‌ها فرستاده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65704" target="_blank">📅 21:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65703">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
⭕️
⭕️
رسانه‌های اسرائیل: ارتش این کشور درحال تدارک آغاز فاز دو عملیات مشترک غرش شیران با حضور مستقیم ایالات متحده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65703" target="_blank">📅 21:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65702">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62accbae38.mp4?token=hSHhhZDfzryubIIzidid18OGIMqyJ3ELEPBHHySjH50Ar3kYNDN2H_Nw4pQl3QigrKsA7n20I3_ZCcrhJRz52nCklomMF7DMysTvazKw11el25Uqt9OmKon5fGx-vHxCnIL_FBugoY1Mr-rZA6fvOFk5Kq8UZNlbi5iJRuObY9Z--Kx4_pFbYFcFMhCnHT3m66DvFaUfU6apWWuacOpEOhHnNmKEOfKyFNyuOtbbULelJSRkAGVM-7zzYvsSGPNYfIcdPyKhA4UxLVgLiQCGbwAxlDzniLJZK4NG7TS481qE2eFEUDu039LbciRa2XwSX8GhqZiLmRwm8-H5HX_3OY2suJPlbEOqhVV9-vHDw2Xc5wYR-HQonb0myILZhLuclO1zQyLJFfMXHMYt291J9uhjQpfXpfzQz9gKQOw_wJVD79uwFV0m1ijhiaAc1bQbD-So23C1ozVZNlABgU6ChN1gjYcY1lBonnJ0uSXUq8aJRW60IP90ddeT20j3i8-7tdcsZCc-QdkvsOykWv7HeyMTq17dC5hpTBOxV7FzWaGzIn695wc8-M-LhG5nAEwz07NQYpfVSeb6Vtc-HEv1YjxZJIncESzDTj7zKXCvhtQwJpPSeAlL2_iMhDZEUQ2pYP-sTDBsga9C8Mj6qFfDvmfQ9--LEcFQ48ajcFOff-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62accbae38.mp4?token=hSHhhZDfzryubIIzidid18OGIMqyJ3ELEPBHHySjH50Ar3kYNDN2H_Nw4pQl3QigrKsA7n20I3_ZCcrhJRz52nCklomMF7DMysTvazKw11el25Uqt9OmKon5fGx-vHxCnIL_FBugoY1Mr-rZA6fvOFk5Kq8UZNlbi5iJRuObY9Z--Kx4_pFbYFcFMhCnHT3m66DvFaUfU6apWWuacOpEOhHnNmKEOfKyFNyuOtbbULelJSRkAGVM-7zzYvsSGPNYfIcdPyKhA4UxLVgLiQCGbwAxlDzniLJZK4NG7TS481qE2eFEUDu039LbciRa2XwSX8GhqZiLmRwm8-H5HX_3OY2suJPlbEOqhVV9-vHDw2Xc5wYR-HQonb0myILZhLuclO1zQyLJFfMXHMYt291J9uhjQpfXpfzQz9gKQOw_wJVD79uwFV0m1ijhiaAc1bQbD-So23C1ozVZNlABgU6ChN1gjYcY1lBonnJ0uSXUq8aJRW60IP90ddeT20j3i8-7tdcsZCc-QdkvsOykWv7HeyMTq17dC5hpTBOxV7FzWaGzIn695wc8-M-LhG5nAEwz07NQYpfVSeb6Vtc-HEv1YjxZJIncESzDTj7zKXCvhtQwJpPSeAlL2_iMhDZEUQ2pYP-sTDBsga9C8Mj6qFfDvmfQ9--LEcFQ48ajcFOff-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
♨️
شبکه i24News :
انتظار می‌رود ایالات متحده در ساعات آینده حملاتی را علیه طیف گسترده‌ تری از اهداف ایرانی انجام دهد که دامنه آن از حملات شب گذشته فراتر خواهد رفت
هدف از این حملات ارسال پیامی به تهران برای ارائه پاسخ فوری در مورد توافق پیشنهادی روی میز است و به معنای بازگشت به یک جنگ تمام‌ عیار نیست
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65702" target="_blank">📅 21:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65701">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c979a7db.mp4?token=ZKjEPfWTV8gplY9Gfv7Eh3oYkPAovAAi_gqKvo2ELLV0BmmGanEnd451m0yZb3viBK5zKb6JaSEilJPn5yecLmMb-TKTBvny-YEzsouI8aD1b6KRmhaYw72Ws_R-JaeDxDwHtoYQN1-lSLH2S_ghl2sL5W-JTAtAcbgK2wa_Sq3fPXSCXkvvXGLiU4larDX-OKsbB5TgS8vwfXIszsBC24cNkQh0csPw3Mw_CpxbTW-Gm_5k5E_DD2z4Q934T-Eia8ZNTvntn3Da8fAzYNdVNQ2eE2opeisFCjqI628hrVwSFnG9QvmI-4srsVAMKemMI3PySzXHaItEtmMlqdVAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c979a7db.mp4?token=ZKjEPfWTV8gplY9Gfv7Eh3oYkPAovAAi_gqKvo2ELLV0BmmGanEnd451m0yZb3viBK5zKb6JaSEilJPn5yecLmMb-TKTBvny-YEzsouI8aD1b6KRmhaYw72Ws_R-JaeDxDwHtoYQN1-lSLH2S_ghl2sL5W-JTAtAcbgK2wa_Sq3fPXSCXkvvXGLiU4larDX-OKsbB5TgS8vwfXIszsBC24cNkQh0csPw3Mw_CpxbTW-Gm_5k5E_DD2z4Q934T-Eia8ZNTvntn3Da8fAzYNdVNQ2eE2opeisFCjqI628hrVwSFnG9QvmI-4srsVAMKemMI3PySzXHaItEtmMlqdVAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام ویدیو ای از هدف قرار گرفتن یک نفتکش مرتبط با ایران منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65701" target="_blank">📅 20:51 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
