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
<img src="https://cdn4.telesco.pe/file/uyYRkaWMvZu9kuh9YKWQL5nHcb_Gx-4OVgOUQ4zAC0hKUVaIYCf5jyB20HKE06Fd_YX8_LHo_VWR2hLh4eC7OJV24LMZ5MLg42CwgotgtjyogtG5qXshHvE3k0Avj-NMNHf2KP8lRZhZ1fzpbBPzp5sOIj7zBq-1yjzycgcFCiee_EyHbIv9AELSDVVPcEDrV5LvLKbmkAvJb3Q3-oVJrkLd0D2lT9ryPRiGGXNYAP-jGbZ56JB20iEliCiUH0qrUumqmRHNs6VH6fXQaUcb8VACa8MD7sxYjsCQ_MuxEpkV-6FusoYv67uw4Xr9ftv1znVYa2Ou9XI-AXEGNqEUSA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 624K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 14:22:24</div>
<hr>

<div class="tg-post" id="msg-27576">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHSf3JyT6DtUz8mD2ZO-YIzJfzEZcFcuJAXf4JHA2PH9OmwUs675Kvdv866tgnpAbFGKl4cWtTBT_M4eW1-HEkCok4ZhReXG7c-5eJHkmmcwPn19al5U0lnyBtOt8kDxB08WcAZck82ve8NqhKfaisBPgfGhKDLEkSgr_5xOgTdXCqPDP6K7khIg4--s_7Oc4MqU7yILoZZ4VuLnrMU1kRCUJO7S_BCevQEab7rR9Ts3Vq33_N0RWsic_uo_YKj--ZF8RozQnKD6TdwnXDPydgmjjjYHVlqYEvi8ssNnlQLnCWA9V_P0A4d9LKS84_2yg4Y8IUTj6SdHUYWowq_J8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش روزبه سینکی به صحبت‌های شب گذشته رامین رضاییان روی آنتن زنده: به تخم مردم نیست‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/persiana_Soccer/27576" target="_blank">📅 14:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27575">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq66RhJ6MlS4R_xvhDe5cZJxdfS0303K10-jZAFilfwFz5s5QmXMADlRZFuDFU8GRbOuOS0Wm9e3u2ZYED9Af46WvkY9vYr8aLoa_960teu-gmIw9kRBWkdFLnzKi0-MtpKQkkw_PEIsQviTChHGrFxsgsOwoWgAHt6g1GGWpotNtx7bfk_vEYzjwYhOIIRbgxk_b0hHePHfWl3pZPsfZ2HEVp4cJvNmS0et_AkQotIqfFkwOfBWqlrV-FR4DbGPDw7aMhiDeAAYfTMRiMIUHs92OVban7cyRFTLjKfluEuMvC7jyNaMW1ikD-XwwPyHRNrgdJgePJaG2ASpEBD1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/27575" target="_blank">📅 13:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27574">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-8ZHFLj-rgmG0aeKQeCCVNPWCcQojDPR_4-Q8BzPa1VA51yB9PEcxlpGIhWnn45LfFCjZ-fePHDsQJrxQEUM0_iIzYC-88WVNLuZ-wIe1lxaesrFwqW17ZLbqjYReO73kfu77rnmdFTV6nChAK07QN8lnZcSuYE07pPH91vU2VMLB006PCq5G05p96lBcjUJBv59Z7yweECaY1NoBQKTd0P30Ub-VQ28TnZg6msnK8O3Lp9SmKm1dC52OGIbbHzDmgeITNjFGuVruxb4w3ScPgxr9itmARyGwNGlEH8fyG6zEUBwf7bS3N28jpTX9FgfHcCBh4OfzqAoEs38hnw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/27574" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27573">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOun21i5izNeYOcsPETbqO_yoR77jpMkj3OaVM40bAGc4qykw7YuLPJX9WbmbqJw-Cj-TRJaxECJafSKfNguit2zzkBVRClfJu1L-uTg33IxR8lbvAxcOe2wEESbguYjrF7zZ8-zfkMraktrqelUL_trm4Z9BCg-HHgayotFt_cpgAwAwy6hUxt7jitw4mg7LjlBNwjNf8K5Kq8jRLYRNYaiwmgFpZwNJ0m4KJkN3g6qZwB5Ck2SAxBAWiPYrjJJP7uq0mMG9f-7r0kh-FRP5Lp91dngd8z5AlR-qzci0L1MmHdoBgSgX6pNgxjzSCHkyUhXaBxApnZREAozJJu5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/27573" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27572">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/polUpzMrolXYH7EA75wLFNpqQbwEJWonTQ6yRTivPL3REK7vBlp2pMlzk_IX_IL2rOTCF5RjNCFeRV6oWTWHnWeFEoXSuVLb1p1Ag3v-jMCwOm9eVbIFKcSFVLcu1lkJQZmWv5gbFybPkbmF5vAHVoJcXdSl92P0SNDnH4CeFpAIlvdp-3w8a-AW78nBhicyoxpziRDWxHtHueJIZnz5ggsjxnlHD0Nea9Ez2cMViutpZ0vi1T-ZYSrx_pawcfrFUngAyFgAGUNCtucGEdioH04j1Yb-OKGLPqeEeDgaiw1guCzF4TzIBp6F_2parmUi-eeWqatOsCZiChHi9VIu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
بیمه ی
🤩
🤩
🤩
درصدی سوپرکاپ اروپا
برای اولین‌بار درایران
🎲
درصورت شارژ حساب و پیشبینی اشتباه‌بازی‌سوپرکاپ 2 برابر مبلغ شرط از وینرو فری بت هدیه بگیرید
‼️
⚽️
پاری سن ژرمن
🗼
✖️
⚽️
استون ویلا
⏰
امشب ساعت 22:30
🚨
ورزشگاه ردبول آرنا
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🤩
🤩
🤩
🤩
بونوس اولی
ن واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/27572" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27571">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV2fO4KiG_KIOfrMx5H43FyZcbsg50EKaO18ttsWLsJA2SgFjcL2_jof3GYci_S6_ixwV_6C9gPW592tGVwbckwcJv7YB_ap6guS7lW8HaTdc38xg5kqVGRrxrLnz2uZ4_nSq8H-X3N3I9YjwI0WHkcw0MT0v6baLO0A-C07vozQ5fh1hlSefFrh27PtFm4EDHL6HArFS3fp0Ayy7jlkqqkv9fLnbfc9goEL2zgzYWdgFF73gE3T4BI0BJdyWvDRTYscQK6A_L5D3UBvQ1r_I6ix7OFS04iLzxfVZAVQykiUtPHtKWmEQ-fmI2mUjsQLpsGAARaBq2GCZ1C1nhUIfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌سائوپائولو داشته‌ازکشور واسه‌بازی دوستانه خارج میشده که تو اتوبوس تیم 86 کیلو ماری‌جوانا پیدا میکنن؛ حالا سه نفر از اعضای تیم و چندین نفر از کارمندای باشگاه مظنون شدن و در حال بررسین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/27571" target="_blank">📅 13:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27569">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIiHqTncLMcVCYwxMl-j93H2FzLgHXt9HwjCEdCs_2cLvWaE7Y8WjBHUn3tp5UstsGGXLwdFNPOisB3ZohunAGN4EtAbM32ck19Mq0JXpiMlmXxJgY8NyzUpSsCEGjg3YldByJLBTkvdbrVZWCKlE3jrYBp8sNjOjBbOQtxCRnIlhPvlZ-X0TNylbWj17dIArYXrIfBvyaAHN_cJn3GdkNC6KjxoxcBmVHZljGihQm4r_tnLfxkaOJh4u_s3RxCbbPpYNILW318-usuorvMdk8KOKG9boHAbGZrZo74wtxxhm41HwZR8HfQ779usGRnzT1AEZuJcMMCI0dHsXsOkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو بمناسبت ازدواج رسمی‌اش با جورجینا یک قصر در عربستان به ارزش 22 میلیون یورو ناقابل به او هدیه داد و به نام خانومش زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/27569" target="_blank">📅 12:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27568">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
#فوری؛ بعداز حرفای‌دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌بازی…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/27568" target="_blank">📅 12:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27567">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn13Vx2Zbxx8q-6pA4iFgGq40Xywak8wO75r8sjjz4cY-zuEyS0s8xcjVcvkt1dXflFukOkKDhMLDuGAtxem1QWRWzT2rvgAMNcbXHkKOoBQj8-oDc5OZFkqeTTLmhVLMt8zjch2MfKQUMTaFrgCgT6s5ZyBqygrx4ToCjmEiIZZASNIK9q4-CCqvFxja2A1Syk0U-DkTnWC54ryQ98KwxiCQcfpM3phsB_XFyNx0Spj_-7i8QiAoWAztNP7UVA3pJBzrJWkiSomHbW4M4sDUj9k7j5vABTxkYBZYTpGQDgeA1eahhQFPh0p0BpgV46mv3N6JjpE88oGWxkW2WUfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
بااعلام سازمان لیگ؛ دیدار این هفته استقلال مقابل مس شهربابک در ورزشگاه شهر قدس با حضور هواداران تیم استقلال برگزار میشود. بعد از 229 روز بالاخره پای هواداران فوتبال به استادیوم باز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/27567" target="_blank">📅 11:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27566">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec3WuAPauD5BSa0TlBXLT_rleq_NQtUXWLozgkdB536Qni9dJ6LMJ2jiJVP2UbHl7BK-x5X-sRKLy64T7fgwzq7EqaOMq0DmtcY07yHaY0eRIIOndqRDIZ7U4W_zQNEY-bM4IscBpvHbKzYt1EhqQjJxcjdWZO5B19DZyHMnM5RJYAJYFqzZ1hw9ZlLubOVRBHZm_1BZAoXo1bk9Whti0WNIjKqrRyFmlP3XMDuj_jasyz4SvT-7NOUzwN8Ri9sU0ivx0xfML2iQFOyzMMxEBHXeM18qNPzPAwBLmkyfSDrlEXz9S1lw0Ko4jtpR3HXvFBYrHEFr-kshOKOg2GqDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/27566" target="_blank">📅 10:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27565">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7L5PV6ewBSgNb8JRsiO53Lh8C9QwRi603LriGUJ18R0MXMIJzm73tzhR8t4z1TLm5WLBT0LN-CQzv9YH5Z8eKA4hPEUG3vyLoGLfJYZvLbR4ayyoEeyN7a85-bCLNMykXnSGwurIPFiwZAROTaM5pYkBM5WiD1fn6hQ4_gISbvbrbMWKyHQ1dcvdbH4b3AX0XvwffwwJ6lHG06Cst72PacjHECEhB9E8Tv1KMLeWcX84D9Ebt9y6qdVRi4d9U0AvpylySVYXER90lhnNudg4HcSDrkM0y4Ofi9ZsbnIITUVUQMKtxQiNpQ4FngiRydtUnGUf_XprrsYWbl_UH_XcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/27565" target="_blank">📅 10:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27564">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAN6-7ViViUNG0DL8ud_FY4GhNzpshkX7mHZ-nOIiocmqBi7jn7_tj5WcTg9jr48VR-FZ3Z6L9JUghYkCZVcMMuFkfRX6EwP1rleDEckm_GMw_mwXi-MROYJeNjOOHzHZ4sEvikd8Hn163WN0o5crwYfkSG4Rmv_TIQkq_AWfqmiIyfE0_qdE6AnzfBCNHFQfuW20yxlawSMPERWT5eofHTDokmy039-Qv2nqWIeFaTlLDYr4LqQpUt-X8v9oEPJ8ITYweL6a_Fk9eyz6WSJeGFMru4bHSzTrM0-0LOV32mcwYaKi-ii50wiEtdH8eKP722x3hY6E0v84ReheEzSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/27564" target="_blank">📅 10:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27563">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZkL3H0Yk66PdNihoXSRfiql0xDAoaLDVS2BfXqkSfK0DMCYXgcwYo0obQUppejI6J-QEpZY0WK7R9BDCFS1MA6V4EaBFpwCBKRVV23LYaqbT-DyDaKUZwgPeNMTgp9RIlg_blbp8i77xiyItm0U8s-2XVoHmEw8FTNWzelnBPiTqsqQKwajqb7CRtCctCj-bn6zgp3dvUePpF7T6r-X1TDQHx9-S8LT6dQSbr835cuTjOxdpQJ8dGSxFfPpzk5_GMDGMMuOEQQxFn1buRwge-C6aq8iEMLzHI5PEwgkVt4sco2Ec2-8hO-QcAgXy7WHzwjdc9_fwMOxD9OTYT4lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
خبراومده‌که‌باشگاه پرسپولیس عملا قید جذب محمد قربانی رو به‌دلیل بالا بودن رقم رضایت نامه زده. در واقع باشگاه پرسپولیس با جذب لطیفی‌ فر و پورعلی عملا برنامه‌ای‌برای‌جذب قربانی نداشت و با تراکتوری‌ها نیز به‌توافق رسیده بود که ما محبی رو میگیریم قربانی هم…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/27563" target="_blank">📅 09:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27562">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofRPtuAG0dJ2mXea8OJmpjenqw9IpmBFFTg_vuv9R4iu0bIfmHk_k1v85nTR0r0PR35WN_e-z8DOxAawo7EO9sxadxwYUKSH7IfGqKtJ20IEg_1nM6nstLEJ_VBGM0NTu3yZZDNOIbO36J3LwEME54qSQsynunyG4RHJkPZr1HpPps0TJqsjHHjAoGVW3lrku2gvmrN7BvgFsTGHzUcgm639Ylit_8X0jPJuNaDtWfMqaQ_aqbwe8ALsHuHJGeBE75VLCuxF-hu8Z158xXdRgq89OSIY0ROM_5IeX7VFV0Tk3oYapCCtdgSJ2Q4Q3s384jZu74UA6ZmXemDV6hzQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27562" target="_blank">📅 01:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27561">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbVgnyGVe1jxYavEKUeiNQTGtgRuJsH3AWxeaDArRUIZqkec1sN2UzsYHLzGHbHc7FldtRqt0bkj5gkfQWUZo3ZdCZ-Za0ooEuQeIgCdcvixiWyPUy10eTBtLfvO-nhnDqxKJtQMBpFKbS9tJyN30ejkWnHj8PFtDZk5b9nOjsV3Rp2Ppkb5xOOP0yNI5Gr1HiPAkZBm0SYlZWIYanZtF1a5xi9IcelqjIZs2jCqdtyKpLJE-eR9PHRgL7Yg3rr-1Z7meGW965Dx7IEiHvRHp1hxsLPd4mbmBYbqf66EJlwounYQDFQYPUG2DlTCaDkwa2S22jnYX8QXe9TI7xGaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛
تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27561" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27560">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9XRHXE53NnmG1S9XK92xD1JOVTk2YWHyh3MqFdvY2NtO_ho5Vvi3ZU-ejDsWU13j0QhdW0wjZw6IXSwerP2JKnHg8dx4fo47NKjlgbZnlQiEdzWy3Zm8JYSst9zyda_IXjE6o_SIV8Deyxd4IHmrli3wZsSaZp3m0qM7Buey1t99ZnPSOASgBdPWUcy3_regaB_zExAwAAy0CTi7Oj9antWJZCw-3I_I1h-psOFJlqYO6s_eK1q1EMc655n1iL2fnEnSu1WfUQcOpPqyy6xaJqy0KPTZtYpflMaIkqMngBGsMvkDwwVCufp-Biy0TClkvFfKOEwpPpaikDBJA9ikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
کامبک‌المپیک لیون در بازی برگشت و برتری فنرباغچه با ‌گل تالیسکا در دور سوم پلی‌ اف UCL؛ کارتال و فنرباغچه عالی مینوازند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27560" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27559">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=YHL8QWijSaX2D5uIYMtKLc4RHsHVkKVrCplzxzyqEhQFs1zxA46Xeeq1auf9Lquq6eKHoXQ8NYHYWUhapleFrPIMMQMSeanD4GrUp4VzQkQx25eNh9I-4MhocFp644WMycL0XQtflKlJuA3dDJZI348d4-ecFpUfg1lb2G8yz_nAZKiAtEJjbdJdAkfc3OFzBFcE0KKnohpJfU0XVVUM7MMOXD4cGgWcGD3MGa49Wr2kC9ILPojGYMRSJptCfgyOHO84H34jaQw3BrSF_Y_IZ7a7i6eU1YOsexRhWBd-CA4Od5YbiNttC2SfmF4PuenxK8Ncgdy0NI7yzMEMRT_7vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=YHL8QWijSaX2D5uIYMtKLc4RHsHVkKVrCplzxzyqEhQFs1zxA46Xeeq1auf9Lquq6eKHoXQ8NYHYWUhapleFrPIMMQMSeanD4GrUp4VzQkQx25eNh9I-4MhocFp644WMycL0XQtflKlJuA3dDJZI348d4-ecFpUfg1lb2G8yz_nAZKiAtEJjbdJdAkfc3OFzBFcE0KKnohpJfU0XVVUM7MMOXD4cGgWcGD3MGa49Wr2kC9ILPojGYMRSJptCfgyOHO84H34jaQw3BrSF_Y_IZ7a7i6eU1YOsexRhWBd-CA4Od5YbiNttC2SfmF4PuenxK8Ncgdy0NI7yzMEMRT_7vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارما به‌روایت‌تصویر
؛ روایت تلخی مردی که به خاطر مسخره کردن پدرش نابینا شد. حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/27559" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27558">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=N5WvrAXeFC2TsLq_Yo-2lEkm4yjEjj-wnMW0amzXo6vZhQFLBJu06kDLFGMG8XsfDP4-iWT2kHF9lSZVhilijs_Cw06JENfrzaA-LKPBylW-F_vkW1mq9cugZ5N-G5gUau3vEm7QgPQu8TP1bayUuTS5fldb74s6ycgrOOw4Bkx4osfsCN1vvccuB3MppmiVwSoPHJw10NNdbobGUnoeF4Ia9Fy_uVOi-iOFl2U_WVozs6rgssFuegcgslLE-Ud99nDtcA7sSb5tNzJ9MV9gMBM-jTPhHhKr98za4TQUyfUmEmwXg_v5wpcbF0e8BEm0M3d19gmeNFwSlMG4qO1PUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=N5WvrAXeFC2TsLq_Yo-2lEkm4yjEjj-wnMW0amzXo6vZhQFLBJu06kDLFGMG8XsfDP4-iWT2kHF9lSZVhilijs_Cw06JENfrzaA-LKPBylW-F_vkW1mq9cugZ5N-G5gUau3vEm7QgPQu8TP1bayUuTS5fldb74s6ycgrOOw4Bkx4osfsCN1vvccuB3MppmiVwSoPHJw10NNdbobGUnoeF4Ia9Fy_uVOi-iOFl2U_WVozs6rgssFuegcgslLE-Ud99nDtcA7sSb5tNzJ9MV9gMBM-jTPhHhKr98za4TQUyfUmEmwXg_v5wpcbF0e8BEm0M3d19gmeNFwSlMG4qO1PUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکوردی‌فوق‌العاده‌برای CR7؛ پست اینستاگرامی رونالدو در فاصله سه ساعت از مرز 10 میلیون لایک گذاشت. فک کنم بعد از 24 ساعت عدد خفنی بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27558" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27556">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuE3ELj_i-FK16QcAqNud84zrIlJCXnV4JBeo5NohIz3ozW1AIzH9LvhVNMPcEi5HUFQPu70HPK6VPy8_2sAgaHfhx30kiHBJlra0yG1ujah9Q-t-_XWNlEURCNahxT1gvtsxoml7TKF1futkAsLtAsLjHYPgo6KznH5U7qmE5L92UpW_x2pHmkb31veu7aNKhrJ7rjmNSmYHDS15aL1Dqp8Gnx6cI2WPtOryLF1PMYfRGCoDrRdJBHAvkIGpsah70Q-cP5v6duYgJvG5QaY1o-xmQnJHAdUN0h8kYrRqpiuc18jZGXl7wtcAYKeuojNwFPjuuEUVLP3Xqn1a8rfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27556" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27555">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdQnsg-nraAx5n0o20o_l4loAG9fVpqwAkiuSjYVx95sdM4y3CFAeRJ-lCqKoFDtoGYE9J5lDcsQcZhAqtJoY5Mgnu7hhDFJq7SSdncdkrlWcLLegNqsCSoydWvRCHy9joHwHQz2s924hNpWr9N1o_kyrmGknNdBUUAIX0-MlE9sS1p3JIaK7asJWA1UpLMZpsCyKne6aNnScU_kC8S_jmF5SZugGc3Tch7AkZWKgdyCXHOlqXJT24FTr8TvOpZbmouj0DJnqWqbn9FlLk1hG6KJ80JZNOCtcXGfvSLSTYW5WL1UkAizjVFrqtkpkJq6CF7CGuXOCp4A-NxhT23QUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27555" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27554">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNW5oIcKsYbwEOQZqfJYJxrqf8eLU7DXhCQHOARlVQIO0UozW2XCwPsYa10pxRn72-NysQo-LkFAEb3ejQ7TP_z1gzw4Nzb19xsYyQ8hms4k9Bd4dQvFGp_fnU4fVF99eLHLkIzbIsbJW4cCXjjmEsq182YRjEwtBUlQ9pf3b5FIvGZOVWuaDpF7yoTEBkxxzowawUkyLqgoaaXY9wc7yHm3RGc_KkbXfqROSvKx3e0ecLjux_ERbkqvUgFEzgO2Te7HIhasbRwAQYBHz6QF29EE6uNzKGajRtt5cyBDadpB5ZLE3g5SKtgHZ7P8snya0FQ16hFmaX9_-Zu0SxXhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27554" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27553">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nto7IK_lgOhNJe2uc2mu5C4H3V5I9M7iqrx7A6utf78qA9QlfeYwf5nRujXMxWSiZOANQJjI4MtAe1hzEZ7TVZerw5DGzIj4Gu7GeZto6eMVAcHbu6Wq8FRNuh9rY4eRhcPJXjavD6gXTrxWseMm7gRPm5gB5uD-bPM_SiR3Qf_zYD6HEs8AmRk2BfzHcAtcNCZt0MNCe7hhdM39a4S-JhLPZfiIZh15NN9eCIVupsT-JPSYUBf1CtrpC1_KJEo1Bddns9-2ipjzHFVtdgn2acgpXJJo0gVp1g7Rv_X-URq6WHoniIH8g6mzPkIRoYvww87dF_Dx6rj7KWkQ-_-J8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو اسطوره‌پرتغالی‌جهان با انتشار این پست خبر از ازدواج رسمی‌اش با جورجینا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27553" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27552">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇹
🇧🇷
ویدیویی از عملکرد فوق العاده دیدنی و برگ ریزون رونالدینیو شاعرفوتبال‌جهان در فصل 2009
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27552" target="_blank">📅 23:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch3uTWBc0w-xy80GWTBNt8u_iNkooBUwCH17kNVKC2UF-AMMuPexXOqH21XOfDu_nfOpSfHrvpa9K11-OGXhsIOFOvqlOeneMtKgUb_bsuQhJ5QiG03pafEV7Hpq3aih98jWEy-gGwU78ljAzMU21UdQMCaudxZrFxRPfUKp50VYvZzqNd4pJGgJPxZGRWZHw-6Trg9CgCY-kbLzqWJ4WiZAWZmnU-BNVfwbmBXNP9Nr2njBS06Lk4ER0PpV17Q0M3Kqr2_J1WWMIXuoIg8gU99J7SWEZ_sFRaeL6WE56XF7MI0KeImPnrT2d7shcd2TBj5V87jInECvDOpkSY1YSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27551" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Z7j4FhQSFdJOXtXAWwjpviYQX1Bs_DsE3g30yu3nGUgZ9Z7025PAkkKmDTYJYrsX5DO7KjT_GnklK96kUqktkpmsC7jX2n9ASRQeTSpOAvl24hNN0cRcXE2mW83Gk8qRoyF7hKdWraM9_q2WpQOqOXRRBTEZGoOg5NoZ8W0tqCJ8hwUJOWKODIY4e-HkYRNkAHj5qW0OsjXLE74bHl1VCzKUvuwr2ZdkdREEpTdEq8qht_CdW4HgMrGwY0TZFydVjOLLvCc-mNxPSpaHqETR-S_QMiaiuOka_xYQXUDcacLT7ddWLuLB0Ad0l1NRzm-Yq5wTx2i6iP0hm_767evw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27550" target="_blank">📅 22:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v31WyMptgYfZRzIqhO_IB7L8Gyy7OFx1a8B8cA6VwTMIsHcC8CV_dkjBIqrRIE6usiSXls2y4GMfbJQ-34KP8QZ0cNeJqEnA8Ae59xdyUX1FmcmcxGMj_fs4RU4ezUJ5J0YbH6J10E9sUedYDJtfvrGFgljofK1R7UKtkgc9ne3aXQROH0p0SgRaAGa_GZYm6bNVVH1T-dWBZkTuxcfpfksdHvmhLXjQW4VNi949e39cPY08GOJ29AQdAhVYE6YKbc8sRnQ7QO-jpgviGDdygvRgb-lVzzQfawr-NvJA5Bt9HFUkEKyiY7Tmmj1HDH4VAaeZk6xeddyVjaV-U4cBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27549" target="_blank">📅 22:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWLZ8HV115EvUQp5SQDjjx-MGSekB5cCc3dhAmSrmiaC73RnQ5vfi-RKIQu6niN0lEwkN7UFoyuURuq7N9LuA3Dz5gagXWiGPbA47Dnt_8kK7dcLH2_Hn4TXpJzKO85f9RkPnpdbWQl6-rSnTRm2uo_GLv02XZNR0XpshzSUV50NoHDAfmpaHLyPj1ulux16c4mtIX5PWPTm3vqnOPpmK67_CxjLHHfYJY4OmZes4n2u0oNgfQ2dEWMW5qdL7NF_LXWGp-cy1LJLQc32VS0oyJAx8JsFZ7K9L51VFCZlFrXJXQdRg32P6NRD20V8ldplpt4EMKkPk2j1HwMtUrTfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام‌باشگاه‌پرسپولیس؛ سرژ اوریه مدافع‌راست ساحل‌عاجی بعداز توافق مالی با مدیران این باشگاه رسما از جمع سرخپوشان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27548" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgRm-lwBmranb387ZLOd-WL_0gIG1ZeqO8W-cFmi4D5XDYBtb3og1arQeAJ7GPeMJkrD2Wb_LJcbRVkH85V5BHW9cKCH_YDk8ZpQBfI-FAxZzS9RoDrTytA5eNTogsAvK5KhlDgGFf6SCcAEwfY071hQc9NGTDI4bu1Gz2yCz08TMXLukXFCAnmdWrQnbcNH2M7XVlSBF_jdcypWkVOgjz2r0m4TTnfQYor4nTkp6uqKUsb0-VChnvCnUHTvRL-L1QS8FOgOtCkmH20TQeljORcUEz9T1ZflkPdCpXbzGTERYcCj7yRpyl6YXoPCEhQTpaqqB59XbiqIF1sBUf4-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27547" target="_blank">📅 21:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEk8JkR0rTvTv5Kh6A_UruZNMFYgYTugf-hmP19LfDMECxyP668bP-sTjZscbaknTVaF9fDUb3skA3OSPzqky6B26eDYzSLbfLl1gNq4mc56EsKQeGimaLZVNeJzpH_QELYWUzRNT3RZ2pWmKPBW0UnL6fIgzdg_6qvPeeKfERTLc77aUv0ut24Uo5iwuPs0IZjAtbcjdMkjAB3yutKyBFMbyu_nN_Rs99SiecMBIoMy2ky7KROfwA26WF7-L6uAA9QbVs0N6AoJM-MlGQ_BHJ1bl0Y6WvxFGRSupehWdkTiuoDc5lokCwvdZRfA4KXfWgjp_pX6ZAcgAm3udF5Sow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27546" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4PE7r1WrwewpjwqZC6d0FLakOgYSWImANbpD0Pwna9eHHp6R76gmwVdpa3h0vVu5kgsXUIm5MCihUugaoyLjZ3OHhOCjrgeyKP0KCA83uqTd0D7jVLPfqkNTXAYpad67a23e4zyPws1YH0aWoA8VKCAFKLtwjvnW8wdTTAjI8_mCPfYtD5VIZ_7jf6QhlZ4DG1N7rkPdJz02ByFEoZ9RU0Kneq66YN6XBAq8ODIWGXsoKwRpccArZYs4-IYdGbdlxpeDYW6Q4LA63s1X0lGpZd9F7WWHPSWMcXfaL7th7XzEd-SyGxvZAH6YthlwsKyI0CUkiC-C-5AuwkhjrCN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزیکشنبه پیش رو یک جلسه مهم در ساختمان فدراسیون‌بین‌هیات‌رئیسه فدراسیون فوتبال برگزار خواهد شد و اعضای هیات رئیسه برای اهدای جام قهرمانی به استقلال رای گیری خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27545" target="_blank">📅 21:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIly9VknKn6pViGsUQbC-PlVOLo6vL1UltMpzX1ntZNmHf387SrgcBJdZzQNCp8CcSGVRSs0wHAv18IFDpxW9sWD9StDnhWsiYNTP6z5ucEv1jb5o3HeeOondMJgjTM9hOT1h82enQD27SAiDFnhF5BzRYelG8WUCnxLmlefODrkWUf4o_8i-goE_0d1jL6r1pE20tW0_HIgquFxydT8L-Dz-D8X6UyC10RZcgzSzLmMBB9A1BC-NJ7Ftrtq761GMOlluJ1D64jQoE8urx8p1d6yKzGte6ChA6OwMXwf6FLddIJN-gni4cxQmRSyfNhxxJTNC5QLMiaMayQ0S5MCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
بازگشت‌دوباره‌پُل‌پوگبا به‌فوتبال پس‌از ۲۶ ماه دوری! در شب شکست ۴-۱ موناکو مقابل رن، پل پوگبا از دقیقه ۸۵وارد زمین‌شد.  پل پوگبا بلافاصله بعداز سوت پایان مسابقه سجده شکر به‌جا آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27544" target="_blank">📅 21:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh8D2xOVAP7Or_u76l2FxY02OTlXgDAZP2jAo3XEOiDFfzfYC5d2zdJ-y4kbGCfEiliJXSsTkE2qBjYzXL7oS9hSpUY6js3gXbmrg1nTDWmOwudVo-f1zkLIU-Y59sAyTT94s0efak5UeY5SwJnQaeUAH_y4r79-EY5R87pRhgKco7MvReT2j98G-Q-JGwAEsTgS7p3EHSosMqA40Qud7M2S076I0oMTxgIpCOSfYAWzRWpgcn9pqHiMbsZTFQxc54vUhm9V8h8ZlGr05sKYgZTUqMXTVBMTfruf04rcWyequ6KgTo-g2EyhNd5ztdSHYcxjjc-n97lv5eNRLbuu7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مرتضی پورعلی‌گنجی مدافع 34 ساله سابق پرسپولیس با عقد قراردادی یک ساله به ارزش 600 هزار دلار به باشگاه پاختاکور ازبکستان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27543" target="_blank">📅 20:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27542">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
#تکمیلی؛ 7 گل فوق العاده تماشایی در مستطیل سبز روی ضربات‌کات‌دار و ماهرانه ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27542" target="_blank">📅 20:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqJepWBzbOfirBJZjZf7FcB9uOKdrbc2agOzzQzRz3QPC_epGlAtSRdITOiIxoBC7eIfWirkFhSs3bDlmqfNnGO_iIelxq1cSeOaq0mNuRrnL3TxDYGcN9I1upmLx46vLQYjZjSkGNc_BcJBE2JoADBpF-keDP4UaEXWsV7WjeB6yH97yn3tCMAUZILMy26Dc62Pz-B1Sco30_XafC85tzEz515t3TGbTY2SA31R4gQro84UoQfjabUba0CmRi3xKZ6ooLdYPLE-Nc9ZqTmSdPzBsa8AEUFgUX_Wfd_rn775hEz6sPIf9HblKiIOy01OqA7IhCt_kEXeBKFOzbT5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال تخفیف است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27541" target="_blank">📅 19:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27540">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-QZkilT6RQW_sWiL4RKZTLe2zsmWTcsB_bPodcUQall6Dkbsxm3QPwjq_DjVg_fRYTBoO_I3tgnRUig9hllr0xgSbJyiWRgVJndLeMegCINpK3rzrOWHF8P6FN_HmyqUQGR-lGPh041S-2VTRNBWSivJ7aZufsEOqwha4SzRaYC6xRHeoq4VmOOmI67kaQfLfDhjhN24nALz1vlb4Zopo2pOlt0OCorJ9nitCz_TNpl0FBh9jw2esQiEo0b0RQbvMddSHuDtwJ2lknOLABt6C1PN-jfjzjtQnKHFIE9LR2MVAZTs4bzSQIzStjzuH577oqlzSFZFP4OUGmJIG3LRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27540" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O57Aw0qXC6wxngR9FP779GuAtR5PXaO12aSdo1FIXSIqGlY3pkjwIoxomOn9x4TpycIDPRYcPBUVcF-55rroogJLgQ7Kvi4ZEPH4xXP6klXFGxMFeewkOntMl5OPtMPHASb8U4IP7zsio-P6nNhGWzngGmhYg4fMqJ7i0nGwUxcReVbaKUVWKmCp3aaBGhrHE1GIYh0kf21wm80XerXvsvwRrNsbGJIXLtEJjIxDSi43BizIK5s4F2HJukiLfDsxQAp17X6aHuM9m0sU0hvoMcS-BpTTEKLtMpvceDKUGPIO3EOY64CIzhBAUMap09m3apnwOj5svGK0GyGrFXhzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27539" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue7JlZe3d5lfkjtemBm5lzYnJcEsuM6pfgI3Ved-5UqpxpO69UAMga3o8TZ7Kn_Ldszrx2IFrbq8AHELUsju9w5rqD2_KfBZNIH7M0a5Ios6hishNi4WsALUdHtKMZ77EtewuAHupHQkfUonKiLQLLic_O2ZsmrkbrtVOStcaoSowxACjrmiqzN7OmU5Ej97C0CrVZCrhQmoTYBUOpnNZiDqnA-zSy3E_YBjlBqoEM1CI14XV2rsLvGudLtsWdlkNOvv56AT6oAfRMtoQ1wjIXgK9wsfwSqsZOdEYH7X8TLkh8STmEUIZm6cZ1wXOv0ONyv8WSTJaPy-olfHUbFLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
سه‌روزتاشروع‌لیگ‌برتر
؛نگاهی‌ به‌ ترکیب احتمالی چهار باشگاه بزرگ ایران در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27538" target="_blank">📅 19:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-FT3mgO4jYBaMJH9IgHpuxZvm5tYpBZElPGQfTOWvQNV8rhhSf599z1WwyIF1GnQ9bL7RqGoNYCbZcvSM7082yYev2hZlopoMqYfV2rF7bouR70SfplbHQYI8w_7Hq2g0J99FLZ5cJCP4nXi3w8DjaLgyCgzxWmmSA0mv-Pp2rBQYPSEywiolbr2f3ZMs2rSoc_noLyRQh_pnrGujVLEJiD5IVqj5jbnlLwgXf3_vMDwqwk-Nw80BN8GbThcYdEICZj1mrG7W2h8-0Og1MoL6cvVasfSHUEdF111FtcciwiRWyLm21ObNHK5mCIDq8BMDUWOfDTBYuRUTIM3GIzBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
آنتونیو گالیاردی مربی‌جوان‌ایتالیایی‌که چند هفته ای دستیار امیر قلعه نویی در تیم ایران بود به عنوان دستیار روبرتو مانچینی درتیم‌ملی‌ایتالیاانتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27537" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=cEv8_r8_zzNqrCJQ2OtY9yimc6OGmE9sH4ajsJr-mkl6fO8byHAMSGUBAvg5TPuNTChJJS9Pb_E_hZSJHOiCx8qBJ5M3jR7x1Pz8N44bJUVcbGP9Jl1x4HBtd3Ur_Aib9Z7ZLn5gp2ABsiL7IxgLXyqlrNTeUEPU-OXZ4FJhWwy7AfgeTEbza0GQTYEmvYAtTvAYcsVgFN2hTDJKvJqq9EaRIIDLonbmHthDynKZ2WMBXNVRXkXIIp5BEOYANkLG7epVgNLdw0nwy22BOsgUOkzGp5e4Oai0e6EeQWj4eb5uLXZfFsPpeAsojZe4wNqHJGLkHbfIdm2mxTZWD1l7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=cEv8_r8_zzNqrCJQ2OtY9yimc6OGmE9sH4ajsJr-mkl6fO8byHAMSGUBAvg5TPuNTChJJS9Pb_E_hZSJHOiCx8qBJ5M3jR7x1Pz8N44bJUVcbGP9Jl1x4HBtd3Ur_Aib9Z7ZLn5gp2ABsiL7IxgLXyqlrNTeUEPU-OXZ4FJhWwy7AfgeTEbza0GQTYEmvYAtTvAYcsVgFN2hTDJKvJqq9EaRIIDLonbmHthDynKZ2WMBXNVRXkXIIp5BEOYANkLG7epVgNLdw0nwy22BOsgUOkzGp5e4Oai0e6EeQWj4eb5uLXZfFsPpeAsojZe4wNqHJGLkHbfIdm2mxTZWD1l7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27536" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27534">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTm7pbjkAUvnOz-wr2Hwh4BMkhNGXD_uHdfVctDdvmGbaXWrgo1tnDH1YisV_e9aMLPaCvP2y3zYgg3-hUZXDiXdf5kczgL3ZHaSLWKeNPapHgAtF5ijztktx6wjTTuzzYv-o57Phrb1bQuKqEJvW1ul3QAKTLEKFxnKe-T4b5QgyT3fZdK5aQxhyoGplhchkwViTlU7g6w710BtzZg2zP7quG3r_piKj97LHC1K8mF0LRSbV9rLYPHSYRnVCyIzMGRrQhKu6nGzJI1Zbbty13NF6WA3VlUHTsDZL4fPdU0ye_8QI6QlGdq25e10e51l0MqtIfQ1HIt3shCoFYHPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27534" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27533">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYj-rne6dCfIxbn1wICvGFmfpE8s4LyIV4ApKFmroa2ScUTAcfxzVatK0vzxHYkdC0TsCv4u5diKpusIJ45_fzfpUxHZYB34qzk_nPLt2C4givGBh8m_cjWGfZjWuDIZoKLkxYzZv92OC2mlMMD5Hu6EqWKoFlAtATJ9V2nz8y-uqljboGFzKhDISUFubKtMrAXEYAXvlWeks71ohR5m-r_c6FPzGh-RgY2-SXoedoilMM9bK43YF47EN2g_nEJMlUNbEesnGJaJ1xGOCismAEmmCjc-EiFOaAb-0hWI7ubFwZYUL5ipcnIATVy9HnK2uaOPfPafEgigRaO1k-MT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27533" target="_blank">📅 18:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27532">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbSV7noVWtJbPo0llB9tYqspmu9OsUbYnAM0cTQ88gG-gU1n2ayowQXA7n0G4jpo5H7F54DIIObu-u2bWfZyHvhCiBFsRlo264S9OGrgMGEF8-_ALKHSozK03Ti3saurJR7yGTF83JgpRtbAHEGSrHPlXP5K6H_7lQBvUGqww-kCLpX1-qyl4CVaW6Gqd9cK0LZOOeHsc2G3se-K53fxrc0klTkeH4ge9EvCTdt3M0IsRoP8XBFm4ij7ZBnwemf-qFQ66tr2086sSNxa0jIJx7HURHrcO23qMyuGeAnoX2rRoc92ptQGIS1m7B90-lf95dwbSC9Gb4vSq0zgg-7v1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا:
به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش گفتم، ازدست‌دادن کسی که دوستش داری میتونه آدم رو کاملاً نابود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27532" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27531">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27531" target="_blank">📅 17:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27530">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxgrclhGdBeOgNiQHSJDXH1rz0ICV9hD31YIQDmhAINOMTSHQnqVsue_BLzLhSwvZltuItsOFFsl16XOv8PZUETk_csQY1WID5bskFuo05D05KQxJ4PmyyTSz5pkvGWk_0JrqYqakb7nx9CXIoUtZhjbayaCeIRDV_1tfhEVg-HBs6R66dC509C1QWfB84OO1Uqwgb27bItyzyTvPQiy8JQCsl-pV5MMlbPdHsSyW7J5bCIRWCBp68eIOdiC3rLKNVLV4M0_ypB3Wt1EUBh6wNr5gd7zztdlkYELv4Yckct0eBU3_4_l4GMawKdlDB6q94gD4HpbNqhm8gZ1WMyFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی برای عقد قراردادی یک ساله با سپاهان به‌توافق‌نهایی‌رسید و اگر اتفاق خاصی رخ ندهد فردا قراردادش رو باطلایی‌پوشان‌امضا خواهد شد. ارزش قرارداد واسعی در سپاهان 10 میلیارد تومان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27530" target="_blank">📅 17:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27529">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjlr5gLDh-hynvimK1_bTdgXZE8Q_XSVZn0fETrnyQtZ9Fvz9KT0Ql9wd3pbjfCcbnC6wKdcDSgG2DnJ7Oe9dPChK0xZsY8-_RXoSZS1kBuD9hwhqq9NAzo8H6GRnwYg2REBIjzvwylUIckGiiGB9jPLNlpkCaduEc_ZZRRKu0SMNZYtzw057hVs0kFuQGMkS78eu6-2Wjglq_1-PeCjBMZJ86-VBTZBa2rRKIxLXZ67DP9ABNY5Jxmf-klwYKVIZ1MAnV8pEvwe3ThZ5p5aB90AzviTbKdwpwGMnsbE4P3A-xrpzR4-VykPN_XIcaXimOAtAAqYJYgO7_QZg8afCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27529" target="_blank">📅 17:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB_GxGJOQ5b8LVuwO3LZpIxRKZCQkDwf1yTj0dHbgS-g7dmPyqN1wORrTtyOU7rBgeCviCbpIb3zepHkAGl6HVgkNsHTPz-dixAs-LxT3l4bcznMZZWTeeHUQxKIEm5j13LKLg7Aui409fOwZcKpcSZfIcBNwBkmJZKhkEqK46MpmAlud4ThIa3-2gRNPBNXokuaBbOkMuZrHWu17H_JsP5Zo1cl9ZhrBgyqSP-SF5PLNuvRmz0C0lkQx4GA0fntvUJ1i5VbnIRQL-atgsiYE4tx_l9ug91uLVNgE9Pi_Z4rEK3VZdiikXkZDCADq3mhpPzPoDztohLGWhDHUAToKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔵
بیانیه حسین زاده رییس هیات مدیره هلدینگ خلیج‌فارس خطاب‌به‌هوادران استقلال: استقلال تحت حمایت کامل مالی هلدینگ خلیج فارسه. در نیم فصل و با باز شدن پنجره قطعا تیم رو تقویت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/27528" target="_blank">📅 17:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27527">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQN7F2egIq8pxv5yI3MF_1LLhCjk1amUlO2kPznhCMar4Y-waxTnsJ3uZ6PeIe1AlbGa00Hc3oM7speMGDmsiHrgMIST8eBj2QL5ArY6XlwvBoQy-tOcm288fr2Ok5tX90hHo-j_D3sPV4x5tXKIxoRMR13cU1tWvfockTpAWUFtHxul-NUWLUgPxr-wIaxmfmpk0ceVW5_dtZTAZBBfzfYoNL4yu_U5U7-l4eKIHBkjK7NVElHhP5ymnPNKJakWqrK1Cck3PVDPZG6Abj1OkD9SHbRLlCHeYwhRZKGZ6Y3dN8qIqZHWvqjHPMZRJ9JGvg0fdYY6MRz5_jf6ewUHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌های انجام شده مشخص شد؛
باشگاه‌جنوا ایتالیا باارسال‌آفری 1.2 میلیون یورویی خواستار جذب آریا یوسفی ستاره 24 ساله سپاهان شده و این آفر روی میز مدیران این باشگاه است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27527" target="_blank">📅 17:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27526">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJ162zWHmCws4X0fr-lVe6d02LxyZmmgSWqmEW6LebB55EZXIVCiU-svBMofL0meXh6i6uml0K4uhGHeYcaa1OAEVsiG5Eq3y4smTyadUg1U5O5c2o0Mw0NOd8QtRlT5Q3GqTGcYmWcOZtr6023PJC5gy8t-0sMdIe2HB9p3APmszf2jXhOUsqVKMaoHM9W6EiEX_g-1LNGzXh_LpVlooEbUpggsjJoTI-VZZcov9vUPRKj6oBwwG2ommOxYOKagk8UsJ6TxQVhfAcocV1QEDCduz-CFR09AzH5K-0rmStkGLHgzggQQXzya2l1zP5xjazswdG7Tf43ypEY5WYXxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇪
#تکمیلی؛روملو لوکاکو مهاجم 33 ساله سابق منچستریونایتد و اینترمیلان با عقدقراردادی دو ساله‌ به‌ارزش‌هفت میلیون یورو به فنرباغچه ترکیه پیوست و شاگرد اسماعیل کارتال دراین تیم شد. کارتال دست گذاشته رو هر بازیکنی مدیریت فنرباغچه نه نگفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27526" target="_blank">📅 16:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27525">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=TYjw75qTVjt7aNm0YStvY1JhtM0vsLVOjDM3jRU-Z-uDLIkbnUbiAHycYyM22MrAfKZOOibN-xa7-njDSQs20_BOG9bwvQb9147E7PMtgMfxhpfJ1b-Fx0rk5A8PIws8wGOSPaxlKeeni3Icso-vBkOmmSV-g5_Sl1irp_r8zfz7YFSmHOMmdLSG9HnlAojgW-iiD8aOlGNch2Aa7zgWtvKbnmoGxj8DEAF2OUeMzzf5ziCwpkhywVkkDR_xW8cijHsYkCfbTCFRvJptrtro_Y1aY6UMhbnaE2qlS3uRng2Fb2mb3oxnHGThKQLYspLhfweoyU-8PRtapWLsVj4uVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=TYjw75qTVjt7aNm0YStvY1JhtM0vsLVOjDM3jRU-Z-uDLIkbnUbiAHycYyM22MrAfKZOOibN-xa7-njDSQs20_BOG9bwvQb9147E7PMtgMfxhpfJ1b-Fx0rk5A8PIws8wGOSPaxlKeeni3Icso-vBkOmmSV-g5_Sl1irp_r8zfz7YFSmHOMmdLSG9HnlAojgW-iiD8aOlGNch2Aa7zgWtvKbnmoGxj8DEAF2OUeMzzf5ziCwpkhywVkkDR_xW8cijHsYkCfbTCFRvJptrtro_Y1aY6UMhbnaE2qlS3uRng2Fb2mb3oxnHGThKQLYspLhfweoyU-8PRtapWLsVj4uVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دخترخانوم‌رضارشیدپور مجری‌سابق‌ برنامه حالا خورشید شبکه سه به این شکل که در ویدیو میبینید پدرش رو به مناسبت روز تولدش سورپرایز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27525" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27524">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI3bsig8E0MALG_XjM6QnKWPzvu-fKHm0xKVIe0GlB_sN9Wtj4BjPBC0HKFJEfHJf97olPsbgzl49-C2En9nKgyVOUIHyDg3v7ERqHCDz_1gPCg0Sly5cFGFk3swEJ8c0NoSRpsBh1_mM92mN1zCLi8cyugXMKrXXt-IhIzZA8npxp7U3NqpClhiCBMqIag52edk86N4jNYPjB67FOCcP017asMNMtAP98JAmc7GSZqBLOcdLuxhHvODMKx-_m6E1UdKu22dciFUteVXOD2ucD0AdsiDh7D5MVwjmp9wvnvw6oYJj7183qQDTh59r323y1YLYIlOxK_-dAJ5F0V54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27524" target="_blank">📅 15:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27523">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
بااختلاف‌بهترین‌ویدیووترولی‌که‌میتونیداز دعوای علی دایی و کاشانی تو برنامه نود ببینید؛ شاهکاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27523" target="_blank">📅 15:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27522">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe2RSHMUEhcQWnV5KJvFd4Fo_vCD1J9INnaNS3TVZfSljW46To3vzKJEbb0V-OfdPL_grRhlamYk8ilIVuPZZva0iWsUSDYlBkLSXQTg-7AGnUg1AbRoTHZNrHfmWzhb-Ai428Z1LS-jYl7XEV-IJo81srIRStw1EX2QAXqlN7EiZ3OHStmTuFLMQEkCqGHLGUkt6sUgpzxQwNCmpoqtmMNULRJFcZoAX5ZHpkhypvzX2d4p_n5YgGV6yHfCjhRLXLCZ8nXwRruh16-Hs0dc6R-Xi9Ip0KXnlbdjSCwRYkOdJ1lyQg37mrkN_Jq-3yd4V6IgF7eBPZp4ApOa3ov54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
وینیسیوس جونیور بعد از 9 فصل حضور در تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27522" target="_blank">📅 15:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27521">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGxkX1eS8hdaODiycLjt55KCE8oTusrbLxAUP4ubtOAENOl52qYlddw7N9FgUX1YA3A8ZFcQH0ExOmpJoqjFvt268seY7vTL7M-ksbT-ehscPJF-2YjjOPM-iaquM1zMsRKs9KwkiX4sBLd3emvwWL0Tmj9lqhuczlLvahDA4SgphlZTJLayxj3pd5E_3PtW-lYnlbZQaqSReakfoOsW2heusyg1r8wb1i8stQ4hk9WzK_jL6Mrc7548QfnUIMIwrkHtag9gKLL208rW8GduJiv3mr__Ld7b4Mv-UJJI4oiC3z4_OwQ0TIH3asVOUvMyCEIzcEouCIRmEQeHe_TWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27521" target="_blank">📅 14:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27520">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSVBZKKhSOOxjD8vUTqTQEcWEgpX-Fqhs2L3Dy1JSUnCbDCgDXqc88N_KFVLlU72-lG1jHJt5A2f0sGBRob3vPPZ1O4YFhay_7cKGAmqyajkWEejCU3CzXLf6gE0ufAHQrFSBMXP770t5pNs8usC178IKOrplcXjEQG8McMDb8hUqtlSsfCOGQ7Ln1ckPPqGUHXqXUBBVsnKFqN9xBCQT4LQn9gdY0DhYJP6zsSIWpogPBIRZ46biOtEeHbczyfTkMe9UXUiab6lrzzJTYFUSuzDvn8Qx250_Zm_dbjZTvh3EIXLWmWi7lfLVSc7XaWmDeRvU2nThfblqNuV3oGYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال تنها 10 روز فرصت داره تا طلب پنجاه هزار دلاری زیلیکیچ وینگر سابق خود که یک دقیقه هم برای آبی‌‌ها بازی نکرد و احمد شهریاری اون رو به استقلال اورد پرداخت‌کنه درغیر اینصورت آبی‌ها از چهار پنجره پیش‌رو نیز محروم خواهند کرد. پرونده های ساپینتو،…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27520" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27519">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=vHz8qWVHoAHwxpdLX90mA3gD2jBunji1FaPLzZ7RW2yNuz8opv5U9bnGmShluNAV6KBd7i09HIHZm8sJ_rZjwBA3F1oxqjweJRcce4qLyEwUJwrkrX7--pxn0A41tIfFQ_WKXD7d6WhcDOf8RhYFKiwA3NdP1CgbWvYmiFwIy38mjRl9z4I5cwXGQFvfBU-n4itza1iWqYYMFiF1G7vXJNpRUvBh6ZBxlaVNZOqYAZIOHOXLOUa2F4JSrJdRBC3V9lPcyAEi1XJ-AZAS11EQIs_uqLcTSh9cMhlqGkUT9-NWR3F-IlNDMiuX2EfqF23-st-kseka5YPV1MYODRJt-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=vHz8qWVHoAHwxpdLX90mA3gD2jBunji1FaPLzZ7RW2yNuz8opv5U9bnGmShluNAV6KBd7i09HIHZm8sJ_rZjwBA3F1oxqjweJRcce4qLyEwUJwrkrX7--pxn0A41tIfFQ_WKXD7d6WhcDOf8RhYFKiwA3NdP1CgbWvYmiFwIy38mjRl9z4I5cwXGQFvfBU-n4itza1iWqYYMFiF1G7vXJNpRUvBh6ZBxlaVNZOqYAZIOHOXLOUa2F4JSrJdRBC3V9lPcyAEi1XJ-AZAS11EQIs_uqLcTSh9cMhlqGkUT9-NWR3F-IlNDMiuX2EfqF23-st-kseka5YPV1MYODRJt-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇵🇹
ژوزه‌مورینیو سرمربی تیم رئال مادرید:
هر کاپیتانی نمیتونه‌رهبرتیم باشه. رهبر تیم رو نه میشه خرید نه میشه ساخت، اگه یکی از این بازیکنان توی تیمتون باشه، همیشه یه گام از حریف جلو ترید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27519" target="_blank">📅 14:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27518">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVmpH3DSJiSE2LNcEZooKIDaq4JvmifgIMxSdKyIKi8zBe2ke9Tm3zIiDX2RTPEIA02kvuSPesdLVhlhnIrIxtraBwT5Fc4d_fWKTsgw37ZBhUUanogeUVr3zTO2GChVQiO8gJwY9s37aHxQkt2Seq-e4LraZrxc0xedKTmlu6TDhHAx_aY6e4kdXgcaoZc3OkxyQVjI6IofMmZy1yGeo6YATiEytXHWGfSj7bJe0GSP3l2XEiwwEUwmMryTb3OGLzZWvyGWIGEnvwI_COTpst5ZVb8GfVsa_TmJJffDwIs2ttXXwu4shlVUXBc5sCVQJZ9O3r_ztBPs3uQPFgDuBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27518" target="_blank">📅 13:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27517">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERlwRJkjQJUdeVirmtj6RW5344ztPIZ5sZ5HZZe5TaK-Qa1E9utAtKoi935m6EwmBdX4rC3vikNmJtWS9awhE4nb3E9R0DKU7ANvzkvxcA-t7DAe6ihBHxxC6zfMMwPEWHan8mGXOtYe7G4p_a4unZwGPMsSIhd4taONDK64qyW9ViRmw3zl3cHXqTkCde7wpVYG_Kmc47_U0rpXznuP562AMdy8dyEa_cnlnHrM52383vIDnutLw8sTnWivDIzbrHvgiKEXPhgJop5GcL1z3lptR6A-RIiolr0_G8gum0wDyYJp4eQSlGnfarOuQ1dPs1tXX8zoppNndwFVlwumdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
مورد جالب دروازه‌بان سامورائی‌ها؛ سوزوکی دروازه‌بان تیم‌ملی‌ژاپن‌پدربزرگش نیجریه‌ایه، پدرش غناییه، مادرش کلمبیاییه، تو آمریکا متولد شده، تو پارمای ایتالیا بازی میکنه، تیم ملیش هم ژاپن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27517" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27516">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27516" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27515">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKnUk692Peod2QexTs_ZDD-Ey1OTOgvDKpS1wU-yt_jv0Td6K8LxBYJPzQDMYIEG2kteySOwK5kcdpJICIU60yXJyna-xuzADD5kfeeSb9TGVM-GUtREZfESTtEZikjCo3WHbMGrP_lLvXyQamWblI0K7V4LbPdbwi56uoiVybWYFHn2loeM65QrIoplZlLSMRPcbYKCy2fpjihXDT4RqWsXLVVQMFVoVKyQ84y9pFulPFILxEGkJCq5N0cfgb1qfO2ghuoa4AP7tXbMMDeX0kL0x6eiPCKJ1nF5C3adamUxYl6g6OpQncvYgJSvGZc6Vm10OEIZHQAa-lDagKdhcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🇧🇪
باشگاه‌‌فنرباغچه که سرمربی‌آن اسماعیل کارتال سرمربی‌سابق پرسپولیسه برای عقد قراردادی سه ساله با روملو لوکاکو به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27515" target="_blank">📅 12:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27514">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICOdDjeVc_2y02fFSHrKjPebDTX0jTiTWSljYLeNhLK4O1WDuQ1JzZQryPBgDkxcDoTWogah3bSOfps7eRbZxzEdN-vTc5xtm-D29XNhBpRofU4G5lSGsmKMnTDU8IKn0zp3k6HNkkF6Z0dVG4FS0-cbC0RhyG9zivqahExpyZyTeaoUXbk7BZgWB5XIGp0XSjs9x4ZvpfJs09UHVfksovV7WCS95VQxYA93LC7Bm8zob8r7UX8aMYyUSoLJubvaQ942IELVaHUP94Z-JSuBCpRfJnGrHUUNVmJybcSaL6KtcV2nGKMJIYhBmvTCnZ_lT7cPtlQb_c4gnpSHu82CCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27514" target="_blank">📅 12:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27513">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTd0OPBGxBUjlbBmP-CWyCcCwSA5MkulLPWuGALTmCuK0DV4nWM_y2YY3cg3Rh9tm4D1BlciJqfNYyOVOuhUerx6zH5ApUQzg2gdLiFcCpn_7ZQgRrHQTVjlT6hQuhvBcXob8lmeU3-qzZiwT-8jVtE9N4gCavYGl3DJzH8njrpdA7dgmQsw4IqhQ8Pz5j_I8UsNyfZ3RtMkk93XPTfcEqThWTT5WW-JpCf9Ammj_G0uOihdGhvGhFemHSepN1KHIkp9JPm2TwxFV4me2y5zIkH0s647_k4hwlfLWimhpZpXbrqNL-kXSbo61eVJGYuZ3C49HVIwKo9PdvvH7YXFcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
باشگاه المپیاکوس ظرف 48 ساعت آینده با مهدی‌طارمی و مدیربرنامه‌هاش جلسه‌ای مهم برگزار خواهد کرد تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27513" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27512">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAtBEm1NzdMdbbthYaBuTFUe8KKroqunHAPdNSCdWZbTPjEqT1bezS7CTkA_Hsk7QbH5cCfgpfYbqxxdSP31mHOXyy4yXfBifIUxGBR0-gZmIKgQMD3QULLWf5qifkjRAkXSyuVeXIcwmQGEJhsC4CQdPf5dPkMQdudCvRQc9aky1-eyr1IfWrsqJFZnrtNriP_Skn66Awe8fOb-bAAaRwuJLd-v0hOFVPW5-TcUeg4eziddIbHnApQmBw4z2iG18uNC-wn6m7tMNigxqlnC-W8WY44Y3PNYnwHAbAjzCORhLr69sddd22wHK86jSVoSRPGm5Y9mLVAwjr-xY5V2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
رامین رضاییان فوق‌ستاره‌فوتبال‌ایران امشب ابتدا به‌این‌شکل‌وارد برنامه فوتبال‌برتر شد که یکی از دکمه‌‌‌های پیراهن بازبود که با تذکر عجیب اتاق فرمان مجبور به‌بسته‌شدن دکمه پیراهن شد. داشتیم تحریک میشدیم که خیلی سریع دگمه لباس رامین رو بستن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27512" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27511">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=nXbZJl_5OfIhIuwkT9pOeGG6WNtTTJDOMzMO8AvggcNs51lP-zx-1vZ3Z7arCma80JmfQazruylzE6uKeCcXiQJZFIjNcVC48_t2K9_nkCG_nGR7EICk_gOTj1h9aoTxuzG9iiyPijH3lrVOOFuK0Csr0xtNlNiAjhvEhfA3zUX7f8bfIUEeaTP4xXurvB5U2GLeTLm_0mdJWkIdpsz6qixW0mSd4y2ouDeJeJENA2_TuCsiSrbuTrtak3Niie9r5JR_OAieqZJmQO-sUVvHjP6oyrwLrAskou76Og-DVIcE7xMrWqJ8lNn15l62yIxBtcT9eyh_Bo1dQqnQo44E51hOptm9221YUFT3_vscih_4dTLbpxuAx4qoPr9bz6Lqd4ZzQqVQcFPm_wumsritvJeP9YmSnjFbD7kOcS1ol_lGvOJDrz1IWH9_-D4m419np9_7qHrehx-lB4ahnZgOdZW8kxJbM-e856U8JFgRWwqOotjybS60NCEv0ayO5FffJkoUI3eQGoqXVwUxLwJrtJP_n21ZL8uQ3iKoeish996G58RzdaVP3Yft_7Ru7Kmn5pwRLmyjCqwkMS4GzbNUKdeqiBuPiUA_ZCWALAAuvzDuX0jXZUv3Y987YUoyrNVfFqnEouqnKLJz5KZV1jnkCNunKptvMapZZLouqxsHOvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=nXbZJl_5OfIhIuwkT9pOeGG6WNtTTJDOMzMO8AvggcNs51lP-zx-1vZ3Z7arCma80JmfQazruylzE6uKeCcXiQJZFIjNcVC48_t2K9_nkCG_nGR7EICk_gOTj1h9aoTxuzG9iiyPijH3lrVOOFuK0Csr0xtNlNiAjhvEhfA3zUX7f8bfIUEeaTP4xXurvB5U2GLeTLm_0mdJWkIdpsz6qixW0mSd4y2ouDeJeJENA2_TuCsiSrbuTrtak3Niie9r5JR_OAieqZJmQO-sUVvHjP6oyrwLrAskou76Og-DVIcE7xMrWqJ8lNn15l62yIxBtcT9eyh_Bo1dQqnQo44E51hOptm9221YUFT3_vscih_4dTLbpxuAx4qoPr9bz6Lqd4ZzQqVQcFPm_wumsritvJeP9YmSnjFbD7kOcS1ol_lGvOJDrz1IWH9_-D4m419np9_7qHrehx-lB4ahnZgOdZW8kxJbM-e856U8JFgRWwqOotjybS60NCEv0ayO5FffJkoUI3eQGoqXVwUxLwJrtJP_n21ZL8uQ3iKoeish996G58RzdaVP3Yft_7Ru7Kmn5pwRLmyjCqwkMS4GzbNUKdeqiBuPiUA_ZCWALAAuvzDuX0jXZUv3Y987YUoyrNVfFqnEouqnKLJz5KZV1jnkCNunKptvMapZZLouqxsHOvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
5 سال‌پیش درچنین‌روزی؛ لیونل مسی فوق ستاره آرژانتینی درانتقالی‌آزاد و با قراردادی دو ساله ازبارسلونا به پاریسن‌ژرمن پیوست. عملکرد لئو مسی درپاریسن‌ژرمن: 75 بازی، 32 گل‌زده و 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27511" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27509">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhWiSc0Wfo62h-gHJH0UCngyipeoCpCAlOTXqPFxIRgo_iztdMlQ8uU5qVxeE1mROfliV7UKQtbAdaH1aSxtcNCjdHiFFeXv0sufEpOYxR6qRFrUwF-vUsFgT3Pn2PGCjnaP9xVHWB3GYvt2Zx8iWvASmsQy1iZUTD_BiMvjfpNmoKoFcWbT9knnr_c6w9nWvs7cWYpsgJ6vN-emKtOZr1qJJEnT-IosurqI3U4Yl0SUhaRc1K1DWgWfVxS8ZsdEvD_CCcM3jjzfy6DSt60hxbHJ_G1ihrxrfcdODyXzm5LZQHdvNhvO3-36T6VwdAtG_E7bvJpfUEIxQzkzBlFsAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی تا روزچهارشنبه به‌باشگاه پرسپولیس فرصت داده تا رقم رضایت‌نامه دانیال ایری رو پرداخت کند. درصورتی‌ که ظرف این 48 ساعت مبلغ 120 میلیارد تومان به حساب‌باشگاه‌نساجی واریز نشود این انتقال منتفی خواهدشد و این‌جابجایی…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27509" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27508">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRDko6X1LfIgRG5mOKQR6TfUm8FOvuR4PJiuEZ5XOu2dt1HKiGLbx8FB9ThjXSJpKrS8H0t-HekBnyoRVxTDfm_-qswOxRSLrCCAsmigxSZWx_ttM5etNX9CwsBcZ0EBgYRLF_TrLhIuVk5bRVFVNq7v8uFDcmw867gl1gnVqcqYkFEHY6fEJIjs1S5z22Cf1i0Ky-2VbEeqtZ9c5e9qPV-iFUfn1QSg1QCDozKBPzPqRxvPN3R0riv4g9k2PhjYvvENTb-qv0dhjXgZKXUi-DnLHBoDFY4GDpdyA62JF5WpO-A91hBlgHvX713CsuIVLoLJLH4oQZ-PiTGtYt-Y3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مسئولان تیم نساجی: دلیل نهایی نشدن انتقال دانیال ایری به‌پرسپولیس‌کوتاهی مدیریت این باشگاه است. برای چندمین بار با ما تماس گرفتند و برای پرداخت رضایت‌نامه 120 میلیارد تومانی ایری اعلام امادگی کردند اما موقع پرداخت تعلل میکنند. بانک شهر و مدیریت‌باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27508" target="_blank">📅 10:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27507">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=fwcBWK1ECpvtvkiKlQr1JYOFJJMKtPokrQZUgyKOvik5tcSZErq0K3TDxEfqDBUlMDoBGmadrP_BN4_B6GueGxqYk8b5XHmSAyFbmsvAfi_IKROJ7-Y--3dAAesNeDUTl201mg8xM-c8EG5V-HyeDvOGASxvuEM0c0rBmMy-giiKqSHy9_waUrmR7b2JhPqrkOqey_ePjvPHPFewcg0dLV5yxdQj5iN8ouStLvdHyAcaBDt5JL9yyhOHyhJn_RPbXY0M8-6ioNIjzyQq336jBfUWxaGlvQewPB_s-5-V8KU9fzwzwKDv06HymZSU-HUiTpMjUUH_eMexFldt9a0bjIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=fwcBWK1ECpvtvkiKlQr1JYOFJJMKtPokrQZUgyKOvik5tcSZErq0K3TDxEfqDBUlMDoBGmadrP_BN4_B6GueGxqYk8b5XHmSAyFbmsvAfi_IKROJ7-Y--3dAAesNeDUTl201mg8xM-c8EG5V-HyeDvOGASxvuEM0c0rBmMy-giiKqSHy9_waUrmR7b2JhPqrkOqey_ePjvPHPFewcg0dLV5yxdQj5iN8ouStLvdHyAcaBDt5JL9yyhOHyhJn_RPbXY0M8-6ioNIjzyQq336jBfUWxaGlvQewPB_s-5-V8KU9fzwzwKDv06HymZSU-HUiTpMjUUH_eMexFldt9a0bjIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شماره تمام بازیکنان رئال مادرید در فصل جدید رقابت‌ها مشخص شد؛ دیومانده 25، اندریک 9.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27507" target="_blank">📅 10:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27506">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9xH2L42Xdw5Od7ivdPjYKFy5PzgOfaC6jv2V9z-Sq3Nuv7n2i8HwoAmxMgWyq0fZBQYOP08fUkVGM9_luB1fZeD4z_gM2l3CMnH0LEvUiGedFnKjftJhBoznlrzx7EVrg6O6KOkPMk7AYU7qHh5Yi16MkPsUfD-ewifMMWYoF0yHD2GcdHQLmsYS_8lp8C7j96n6eDmuU5l9ZpxuOlNNIoU2VvOBNpmk_Z-YL4s3jfzGm0QTawaLnwx9rQ3NxQVL9nT_6XrOIMHO63eatbwv8z0dflghX-y-BNoFo4iDz7coSzW8KE6mNz51BODdrZBwgGsHSyojXNLaB-06P144A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته اول لیگ:
موعود داور دیدار استقلال شد. بیژن هم قاضی دیدار پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27506" target="_blank">📅 09:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27505">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLlLMb1qWA9G_tka7x5W6lsEus1_vLa39JkxHxL0yXY7sR6Ra8o0QA2gUsgodkTMJvUPndi8Omr61iB4VdbByD2SrW1CHIsFFQeb6gKCvObQfxIgzsrcrs07ITozmYSqRLStO8HGOGCXHOsHW6V4u8DhyjbxWofA7vMmbIt1rMBuT0ynt0JXgnG_JJHxgjJ5FvifguPQCUHmQjrmSduHKqvRGngdDGRX40D30PWIx4lMWgw5cAbYq6YCB1mgxkxrm_Xm52cc9CbEzxChk_CJ4-VmgT0ItV-y-E9iyyMRz3J7o2vo3KO4-e9CrqXTiV1NA1ljuXQUmLbnnzWvTVHVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
مهدی طارمی بازهم‌ازلیست المپیاکوس یونان خط خورد تا در آستانه جدایی از این تیم قرار بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27505" target="_blank">📅 09:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27504">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=hjYLKquWiaBEt1CvF2ctNFAW32bb36mUleAxKR4FOoorvVnel0V01NEryltUR5fXM7_7evF8USjYkZK6tnezoB3L6jnzmLjWLV6iNLaDA5FkTRjvVeDVyxv4WkFqEY7vFAv0l0mBdsfH89IPlwLmfdVrzyG4t7Cfcvi6HHW19U2YkFtyHf0kr7vcMLyPu-waG5MQHZuEH9o5y7-qV1m6hqMx52a5tCdxrbc2KNdCppOoyP8ZlolW7ikjqmtLb89oePdY9kg4nEg_D4Mlag7hyESMBckgt-UroGI6dGgrJrQliYDOvNj_V0rx8rjjSyUEDkfgCHVprWHNjUTxclpXMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=hjYLKquWiaBEt1CvF2ctNFAW32bb36mUleAxKR4FOoorvVnel0V01NEryltUR5fXM7_7evF8USjYkZK6tnezoB3L6jnzmLjWLV6iNLaDA5FkTRjvVeDVyxv4WkFqEY7vFAv0l0mBdsfH89IPlwLmfdVrzyG4t7Cfcvi6HHW19U2YkFtyHf0kr7vcMLyPu-waG5MQHZuEH9o5y7-qV1m6hqMx52a5tCdxrbc2KNdCppOoyP8ZlolW7ikjqmtLb89oePdY9kg4nEg_D4Mlag7hyESMBckgt-UroGI6dGgrJrQliYDOvNj_V0rx8rjjSyUEDkfgCHVprWHNjUTxclpXMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسه‌درامدبرخی‌ازشغل‌هادرمملکت؛قلعه نویی یه‌زمانی حرف خوبی زد گفت 40 ساله هیچ عدالتی تو این مملکت نبوده از این به بعدم نخواهیم دید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27504" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27503">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJq_-xr9Z4C-HAdG1GHa6pBPvSGIqVt9L9hrlM1Mm6TTxMLT87BE6Ns1IiXXO5iIAbeRJF491zvSdbH39zpZlKNL_EM8iTkxXcYswekKHuuokqPXFTEx2HoTIkH_zLZu2Uc2Lj82uwEUkhxUe8jYRi7bZJEbAjXFLxAjL81-2GzrVTDGoz7MLdZZz_ekJWFgk-xZBx0Dv3yjPbpHmJij6ijxImoMdCygDHVIjtFhJCw0RqbfhU3GzUXLTEQ4h5Un7I84ItdfJOSJvi0-sXJT6qZA0LiJcyxRilKIvMcvT7bkUQ8LWLfr-oHms6L3UvL6Wc3Zyh0jjeKySMN8xo7e6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الکسیس سانچز ستاره شیلیایی سابق آرسنال و بارسلونا: من‌درجریان‌اعتراضات مردم ایران علیه حکومت کشورشون هستم. میخواهم به مردم ایران بگویم که جهان صدای شما رو شنیده است و قطعا پیروزی نهایی از آن مردم مظلوم ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27503" target="_blank">📅 02:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27502">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=lDiCVLBvBHG61Sa3FuNW_8jmQHqITxm6dgkfi30CRyT9jSzzYINbJhgSdRzonbIRIFWsPn5F6cH96KaGWhFXeMSFRFYzI2GB7iRK4Yi8EP0dvo9JABoY1gLBa_wWh_yoReDKa44ZEqrY6wJJsFLa8Tn-D9Q0FKJ0h7T7cnpF4tba2ZSaLLoL36zFUyM1EYJ7MOTYIZu0TJaqP0YcFjKNeLhjHxmHIYKDmuq2oPzZMXvrS6fUvXG0kgB6PTbn6bx2hjJI1hgc2LZVYgloFXGPmvymkjcZ1EKxD6n2wHfJis_ZlNsgb8E-XdU_P7JwQOx7mjAQPC_A8QgNA6vP_lo3lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=lDiCVLBvBHG61Sa3FuNW_8jmQHqITxm6dgkfi30CRyT9jSzzYINbJhgSdRzonbIRIFWsPn5F6cH96KaGWhFXeMSFRFYzI2GB7iRK4Yi8EP0dvo9JABoY1gLBa_wWh_yoReDKa44ZEqrY6wJJsFLa8Tn-D9Q0FKJ0h7T7cnpF4tba2ZSaLLoL36zFUyM1EYJ7MOTYIZu0TJaqP0YcFjKNeLhjHxmHIYKDmuq2oPzZMXvrS6fUvXG0kgB6PTbn6bx2hjJI1hgc2LZVYgloFXGPmvymkjcZ1EKxD6n2wHfJis_ZlNsgb8E-XdU_P7JwQOx7mjAQPC_A8QgNA6vP_lo3lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلندشدن رامین‌رضاییان‌از روی‌صندلی روی آنتن زنده: بخدا منم‌فقروبدبختی رو یه روزی کشیدم. الانم نه ساعت دستم کردم نه گردنبند گردنمه. همه لباسامم ایرانیه و معمولیه. از مسئولین میخوام هوای مردم رو داشته باشند که با این فوتبال "تیم ملی" آشتی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27502" target="_blank">📅 02:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27501">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDzmcYYTTRyMw_cTddMkcVhDiYRtVckl_tXpKeF6wT4naziY-8aWPUTY7WZ4JCyvzOz1e9avgydXc3_3uqT6Qbn9yAs-a9nMk1ub6TLNREfD54aylsp6sUbJ3pFdXM3H907iFsdECZy5H0KMxxliDLzrmI3MP6mF9PfyPXTxJzq0Y1nQOm3ebCseIYp8zX0Nd3ZaGRYVH6DhPFBuUo8Q6zGi_R0ddIq1nDHs4i_A1zPcFe6C2vdmWdECqy45K0AqTpzOGfmN-wkl6UYFhlAixAJgDG4k7hyH7SMExYbWt1Djc22sF6MDKJenjSP4LMQZPWtiI0TGPXfIgFem_QPzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
روزنامه AS: با صلاح دید ژوزه مورینیو اندریک مهاجم‌برزیلی رئال‌مادرید در این تیم موندنی شد و شماره9کهکشانی‌ها درفصل جدید برتن خواهد داشت. آلونسو بشدت علاقمند بود اندریک رو برای چلسی به خدمت بگیره که مورینیو مخالفت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27501" target="_blank">📅 02:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27500">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwoyJYyMtUhaOchhRIRibBg56e61GjfuHPYFyKljmXTABil9mmgoAVYVs5JbH2HXvpEzvFg4ztwHe0t1SRwFWZfgRrwUe-aqEAJzbOifBhjGvzybYk8nuQGsmTzUiEHhQtHDP3bBoux9iVgDxsTXIKdDhzHvcmL6mq0LY8vr1STUXFuoDztuk4V3UUUgGbndjCsadNFNQ2N3jE21C3I03PbqMDi7sqa2CNplh8eLTc0IivOwhTOb1leo0RBQhvAa63oZ_vkMS9q_gUNLYtcCuRO-cOXeWyjBDmL4dJbXkeWXkChL_SvtUjELFr2ftSavUTpv7bMb2ddVvrPJWwIYAD8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwoyJYyMtUhaOchhRIRibBg56e61GjfuHPYFyKljmXTABil9mmgoAVYVs5JbH2HXvpEzvFg4ztwHe0t1SRwFWZfgRrwUe-aqEAJzbOifBhjGvzybYk8nuQGsmTzUiEHhQtHDP3bBoux9iVgDxsTXIKdDhzHvcmL6mq0LY8vr1STUXFuoDztuk4V3UUUgGbndjCsadNFNQ2N3jE21C3I03PbqMDi7sqa2CNplh8eLTc0IivOwhTOb1leo0RBQhvAa63oZ_vkMS9q_gUNLYtcCuRO-cOXeWyjBDmL4dJbXkeWXkChL_SvtUjELFr2ftSavUTpv7bMb2ddVvrPJWwIYAD8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده: ما با پرواز زمینی اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27500" target="_blank">📅 01:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27498">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=kUb9Nrmf1qsh7jVfNYF6LY7TZ2asxORUZQhTQ6mqq9rlc2ieZAb2K7EtldMebZqyvySOh5pEEEGKHgJnQTThl-wC4RHR2AwDcAMMLHLRuuF8EQwF9lRxTiBxabUuscipfauO8tbaKe3r7ugTwV-Na-7XMFLGUo483vBHeqv7Lg6aBGemK18JwO5cxkMxVRE3nLv0R5zOTKl-s_aDA5se8NyHckz6iOmAL4Bx1P0L4rnnzuBB7e6qecL26PGy8QbIUpQGy2UzIvosDClK_4jr9DATNv4saPvaRYReDtcV4oUhIiK9GYqQ_u5_RkZD728u5VQ9RjBGKDpdipw9rWQkFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=kUb9Nrmf1qsh7jVfNYF6LY7TZ2asxORUZQhTQ6mqq9rlc2ieZAb2K7EtldMebZqyvySOh5pEEEGKHgJnQTThl-wC4RHR2AwDcAMMLHLRuuF8EQwF9lRxTiBxabUuscipfauO8tbaKe3r7ugTwV-Na-7XMFLGUo483vBHeqv7Lg6aBGemK18JwO5cxkMxVRE3nLv0R5zOTKl-s_aDA5se8NyHckz6iOmAL4Bx1P0L4rnnzuBB7e6qecL26PGy8QbIUpQGy2UzIvosDClK_4jr9DATNv4saPvaRYReDtcV4oUhIiK9GYqQ_u5_RkZD728u5VQ9RjBGKDpdipw9rWQkFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
با اعلام باشگاه آژاکس؛ مارک آندره‌ ترشتگن گلر 34 ساله بارسا با قراردادی قرضی یکساله به این تیم پیوست.ترشتگن‌اول ناراضی‌بود بعد راضیش کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27498" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27497">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6b775Z4-J-ZGAZfNxn22X1Zy4vqCNCAUyEObg-UPe-aD2NxlhCt0xXV5LhTdjrRqqyDnYoHotjBOh7-NYYdq2a5O80vzTxps6NDefROa-bn0zv0dAQuVyCPC6WJBR_qGVcw22guoaTZoejiZ5quAj-2UvhMkUhdvJgF7UbmMjIjTtCt8RBmL4jjdAiz3Sf27o3uutnk_YmuWnxQxH2RXTTNNmce3gc36aO9jGPCPnKpCn8A-eqyP44vDqc3pMnJRs2OMkvU83uHixpCQPZ_s6ZiO1pZeFVa59dkyxnFgo2TvHX8Fww6RDWvEnCPYGJAT-_qtrrrCfIm2SJDJfZkFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌ امروز؛
از بازی دوستانه یووه با پالرمو تا بازی پلی‌اف لیگ نخبگان و چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27497" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c2114992.mp4?token=kTpjryF28AxPwNS7tXF9PaSXTq8x1IzjXNLHAMohsFRuboBK0wFMBzlKZjBevGwSlnweyZaa94Pc93e9PTUgbttv5HFiiHDy3ppvjFoSfaNWcbQZ7HleXo4ljSJC2HXwyO-QKiOXxn3xc4mJj4pbMtuLwAXzU7SQCsImvMUL-oZ0-gmG4l0CqYxksm1bCablDCDfrbyyw1VsAkFINeOR7BvMCgeusx4y8zo2OqujXr9c9tT6MHsoDoFYewBT2PpeqfPkKpgnWmR15fsPaEh9n0NTuw1jIw6aU0OJLLHQjgRMLk5FeQByo0ADUtoaqS4IgwTrETX5LSTdm72qT2IJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c2114992.mp4?token=kTpjryF28AxPwNS7tXF9PaSXTq8x1IzjXNLHAMohsFRuboBK0wFMBzlKZjBevGwSlnweyZaa94Pc93e9PTUgbttv5HFiiHDy3ppvjFoSfaNWcbQZ7HleXo4ljSJC2HXwyO-QKiOXxn3xc4mJj4pbMtuLwAXzU7SQCsImvMUL-oZ0-gmG4l0CqYxksm1bCablDCDfrbyyw1VsAkFINeOR7BvMCgeusx4y8zo2OqujXr9c9tT6MHsoDoFYewBT2PpeqfPkKpgnWmR15fsPaEh9n0NTuw1jIw6aU0OJLLHQjgRMLk5FeQByo0ADUtoaqS4IgwTrETX5LSTdm72qT2IJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده:
ما با
پرواز زمینی
اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27495" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27493">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cylLfjw7y4mNf8Tpx9SE8TCr4hE9m17iOanXYI8QlXGHOciJSikcdpU--LVR38UBQICdhK8ZZhsfpmql02D8PWc5BrTcy7DPDDwo0xUoscxVoERNngXjXcmDjSADFAIFpfPi9yIo5Ve3J4plMDk2Q-BMPe4P9txMeAPDEZKeotVG3PnL3H1PTNY9KsWTDt0xChrbS6Jj8gq_M6VqkvjrtjKU6djsGvVluM1p0qdyVggoX8b8cltWE-nFYgv5bWBUKSvEhUQiRiBe-LyGX6n2UJiJO6VXI6qpNR3TF1bX-xRnYk18fdqZxapovjQEZsQhggY_vIrAyCGRHHLVkbaKuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رامین رضاییان: قرار شد ۵ تا ۱۰ میلیارد بند فسخ قرارداد من‌باشد امامدیران استقلال به جز علی تاجرنیا گفتندنیازی‌نیست و مبلغ روکردن ۱۰۰ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27493" target="_blank">📅 00:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27492">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ_FxBuxIdhItwqjVWCAMsUWX3ytUhy6Lq0tMiFzbMDV4-FfD7UShmI3KbKeCDOy5Sqxb3eY9D3eOKl23yKWli8zmJPhxkeazaYMcilysnTbgfOE5IF9k_FFm16Q-1z0x4Wedso0anYye12L2t7PILcnkSuJ-iw9w5skzW7UzOM5bCIuWukjgTC0VSRC_vHHfvwWwy0lUODcYJMqzme5_r-JCaWUHyhmGE0K9zxcnN93W-MjrlF_st6z8tNBwSOnbtz4MkvoZgZABHrriPbkE2o74wxBSwh7EFirVfNNbxldb8grtvXb3GsK7H37zFntib-FjfWhJ9hzeyAaUoG8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج‌رئیس‌فدراسیون‌فوتبال:درروزهای آینده جشن برترین‌های فصل گذشته لیگ برتر برگزار میشود و ممکنه جام‌قهرمانی‌لیگ‌برتر به باشگاه استقلال اهدا شود و این تیم رسما قهرمان لیگ معرفی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27492" target="_blank">📅 00:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27491">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK4EpTu9kWS7iIzjiXKuIyxsDfLGhEsvVg4nQevAAQq6yemsLnj3J9sS5sDUHkeFBxZNlO8heWLp9ZQIxZb83cTKqAZ_djc35LMl-nii51yihAFh6f1hP2MKJ6aUF7xNX3DPv-WtdBdwRgqv9Zgo2xCptvXL8U0xBpkWleSoU3VR6RbarSV-As8QW2fe5zrQMDL9gZbZBmiV79iFUFlUls-v1UQEf1BxEtCOmJIYIA1XVTixgqt6lpoPmmaIISLBwnql_OB0OKeGqxRFtW279ucaRtu0Cz5mXoeEp4KgHAUSjsdFCZHxPU2YxO5GvOkSmHCjzi7osU3bYeeUdbTKSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27491" target="_blank">📅 00:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27490">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBVvbiR7ML1j00UmZPdTjZKieDj4YuGOIt0jnAgdRMhNUWOeq3ZcOSglwdj64L5Hf4vMVJmka2gfeJaYGJM0iDGGY4oM1STkMzhtFuznDql5p1xnW6Jco1Z8OiZKPKpZob7TBlYvKPbOAgXHPaXA4M4NS0GuNQEA7dwucUHOJV-odvtnTVm9LgPlJLoHJUC3LhQ68jJzd1kMLCaG-L3WXMIDcO8thPA45k0BsKDHFjXHgv5h1qm_6hjN5aPJfT-urbFrMMlfvEWTR-oa7Eu-KOxuSKIM85M4mN0cW11kYoqPrlVGDrQlf-U2wn-PSRxnWihQ3QpisyGmvxXeHacDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27490" target="_blank">📅 23:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27489">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmcReIo9BgRaDndS77adxdVQ3thxm1wnVgY8gTi-2dlQzVMBgumSsrQeX4EAv4ZMEVh77E2TR40ltipXT9u0rNWkSS9w7fCJdYeA53vZEKgDhTyWSBZRc4ioKmAHx_GQh7Cna1TWKur2G1QXysx3-qfekb-J6rwI8tI_Tqfwr-5UKT-8QpjKJ8jdo8XmyYgL9LbWXtWXQBkLH7rK-hhYfgqLLsHzM61w1PHuFrQ54dNxSiE30rXkeND57-RDJ0GCJnz7oPZmsZPEf2bqCH5xBuHQDhtJUgBHbiECfAz3wW--zDtpQS0ppLVQRv4cKUlVGHL6e9nCpn8lHGyfFnLXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سعید مهری هافبک‌سابق‌استقلال و پرسپولیس با عقد قراردادی دو ساله به فجر پیوست. رقم قرارداد مهری برای دو فصل 30 میلیارد تومان ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27489" target="_blank">📅 23:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27488">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiD2IgwbtRZLiLJljKQrMCH33daTnV0kHqmUNRjIH0z6gdtltHzCnzt-3p6ggx3WFOSJ7tmgUGK-xrfFwTPKwlFhVlQmiLmcwZZggsqKNU4_dhLeHzkQH4gcFxKjSMqb5-3hZDUULGYbqIR_bEyJvFwQz-SUL174WCaax2Wur1M-cyMPrCGSc83HhjYR8hOgCREzhJkvwZTptL5lVlDxIecJbLDzxHmcWg9Y_lmWAaGYyyZe7X_C6Spg6XuKKOY1Z96PCcyCQM13DeHFG_tWGhRrn5adnTTN8vkzMYXsH4QZla4OlA6ZEBD0dRCKlNK2ARYSU0bBS65c-DcQhvGp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27488" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27487">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuQwvX251Plr7obCDi7EgCjhd0EUYKGdavXqDkTgVu6a5WEaPyugjlhgS7EvEkiFna9bg6Lo6E1E0gKmXp3CLb13mT2fnezcBw8RXiM94dBy6ihYDVg6f-h_jjy969cHmUw8_l1TrlcTWikrTR63Is56FyxfwoNLVd5JjQ4lKV9eJ9vR3eWBM4ItcDw7eL8hS61uQ3WPQFTBcf34dpGCwiDDrdKFTYAZZFCwMoa5EtkMVSTdWayS6p8Rd1kC5cj-RLpM79x8IuVRTmk_MbnwrRK7rf20lF1EJY2iRzgeSnJf8OcevenJIr3im0lueNyHII6ekYI0oFmdLH6l-XmPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27487" target="_blank">📅 23:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27486">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4X3MVecvYmIt6knYExqVOYGoK3lh1uajbuyjD0VMSkMVrLXGylGYrlabkia5QvNsFgNWxeuOx59anKsIc86h276dL84xfM2dw9NcbJHD0IzY3ItCPxbzEfm2Tgr8S9Sw5UCn0qRFrR4R1ou5mGz-SabWkGV3dL6l8lpMjVDfURlcIH8jJPdDSClCQZrHvvq4Z8eOgNLmccvAfk0nme9elxNzTvx7E6skwqKZbXwSjl1suWfimXjTRlDrp7EfUIjgWR6cNPNdG2QUhr-mYPQKUDqMqmrTMdXpIbWtvbbVGRPNrR435fXU_EpBF3VxcxLLGfHwUTIHh-ZcEm1DahsIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
ژابی آلونسو بعد از اینکه با جذب دنی ولبک و هندرسون تجربه تیمش روبالا برد حالا طبق ادعای اسکای‌اسپورت ازمدیران چلسی خواسته اندریک رو جذب کنن که پرز گفته فقط قرضی بهتون میدمش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27486" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27485">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTvtya-vZd0Nu6ygu0aIN7SnmBraoiQUaICor330p4Wg3ehKdtSMkXFURHf-Wj0XjFPMefmnNKsEdCXvTCFTVamloBmhdGjVgZvHoHjajDzyiCayeNA4zUr8kipCPiVIo-OnI_VG7bEKcF8edHSc9yHGmcjdAYz3NeDW2PpID9B3PeFVsULWysnFp4GYt_Un0JCGXOScboVG30Bp3vEsxk9xQZwv81BwOmFX0Qjz45auQwBeBw9y_yG2TbQfyiql9eYlnKlz-JAE_1EuJlXpuVqHUd46AKBA5j5i9Fr9xrLLCWLTz56uu5J2TkAAD6pxSkaCDtOGtgW2SHtOeaiTSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌سپاهان‌دقایقی پیش به‌این‌شکل‌از کیت‌های اول و دوم‌خود برای فصل جدید رونمایی کرد. باشگاه پرسپولیس و استقلال هم ظرف 48 ساعت آینده از کیت های جدیدشون رونمایی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27485" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nj43Uq6d25VMWwa7SnMSnRrVWMCaVEIWDFUpiH03NiGPS46ZYgNU85AcJ0nuy1nQBpeNynyE3MthjTwu0ujfb05WK0V0-mL6VPNuSXIvSErqoE9iwFVCcwnwXUU4VDdFzhKdE6eLJBV-9AjIEquZVsjL6m9TDgkrGLNYiAEaGMSmyZdctFcj1X1OxkRIrUwDqTRUvI4oj-BxrjdRan39CC4GeTgq2SrGFNf8QwIKv2NNt7U1nytcmwptcy6f_BvxS4ax9velrsT3lxEDOfJSd67BXcOv5euSOV3BlwLemZTlz9P-SIS7vGLzMBflWxzQceM3x6BVRcHK9Je1YANt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EE6gRDIQss5JL8w4bXNmYigEynVHG7t4xzmJiAxPzRIiJ0rghx_B0CSdd1sjNor8r3fPw30ElNkIesbs6L-wOZ1aAuBZKJ1hX8bkHTM_mBEDfHdA8a3VjgibrJxHyE-lk_CUUQYuTJYgWJJxUMOFRnX512U7L5ycp7IUNL0RuufCYoagCe5UrEn8klchnHE6V7oDyBH6NlSihG-9iz_jry5oATA3ONpo-BeFbrZ9eK1L-29ToFs1_xKcE0TxDJNX5oKV2Yt2AGoSFKz6tpWBFiX4lEAQTufpafsSrcxG6Bd9uU-MyfOvMrwVvvtrXDLqPy7WoSQO8eMQCB9WR761GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
پدرو پورو مدافع 26 ساله تیم ملی اسپانیا که بهترین مدافع راست جام جهانی شد اخیرا به این شکل از دوست دخترش خواستگاری کرد و پاسخ مثبت نیز از او گرفت. دوس دخترش سه سال از پدرو پورو اسپانیایی کوچیک تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27482" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4nfpzXcW3DKeA-p6sNIxgLuavg4k3f1m6Qh68HL53CTTuSG-hh5NePy5kHduzESHRBc0hehkVonGJt3p0Ln4M_f8JY4aU6XgjFhSfNdId128AoX0cbJ4u0t5NLEFzkO5Y9HRjr2Ro1jNKO6PK662tvYjfMn5xRzi7G8ZZbySMZkxuzFHmWF4uj-3IqmGC7H9kGb9hGF3Ei7xp6WRzhTzlqLHKjIdauroKfQJqAkMJ1thk4-qybBQufn3byyzQe9RbcFu_U06pek2Su8f9FA0OTGpYbIRjqYL4WVCmqFOYJVZQqJlGamILbM-7X_yaEEeN6eBXmi3y7afjFoPYgF5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27481" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAqm103n0n8dZE7RumaRBYPaR5DgpEYEqacw7wGSrjmDEJTTVWX1uWJtJQ8t7cAzHOJ-bv0qmJEv4v3vCKhX34LmPfh4vmHnci22lYiR9D49V17UlX5j7gS_GvvTHpe8Q3QLJ5RW3YS-KJk84momjlFku98JsdgwB7oVhtYTEO93gTwrmZYQIqKQw3hQhg_jP9EXrY2bHhHBtT4_iFAsqfmgq54ymCwLUDbN6TmRIHJthBYnXK9WJFYftOwdsNIl38wkwmLmiyWd7P_IL8B7zlkkLY9Pq8_KYgB8exW4nKEj9KCmBpq3U-VPeS3LcQM1dZ-PpH1HAumt9dEPYxuKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه استقلال؛ استعلام فیفادرخصوص‌قرارداد یاسر آسانی صادر شده و این بازیکن هیچ مشکلی برای همراهی آبی‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27480" target="_blank">📅 21:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYd4tFk0Lfr1PSolyskIwjnyS7GmPQQpugqb-UcWkZpybbatkEAJCvjoTNadMd9VaW64M2LixA28Zy4rrUdEjMPe_HVlIxmFYwvqM2Npz-rJT3aol7Ps3Onm0fVXwbk5zaPHJu1-M6oEPOlfP4w8HcV6AxZddb7PaDPbrCMKbPqX8-_Qd69XKwTUYwAuMRXaJSrQ2mh2S3iHiwys7EMnQWueU51sYZipB6X6ypsFpOnP1ckJP_4eqaipWdQ9Cs8btBi9UeyvJqep_h7lwCtT6A0DsL3ZMPpyY7Zh49xnklcbHinWCN3gZ6DrxASQ-uukMJiDTJFTq3sQdMfpXsFp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27479" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmNR0HjIwoYRDbGWSyPf7Wic5C-M50il2xvHd6iXCG3DCUoLeICsZ7fZpzXJonALqKOtORZGFcXCPJA2rV3MvKB882A9odv49apHXVLxvp3MwBUppQ98EHzjguj-Y6eG4oFpoTVhHd10w2NlZqYPCno4vCqj3_9pVVD-pAyn-iWoGYeWikK4uMnqmR_FIDDvgw4IUNYNywD80va4vSgOtRj4Qb2KxxhN5w4Zf99UnMfbX1cIO85ISiuAqzPCAbTTKYUeREgWuk0R891OroIWYtJ6VImzwaOCHgEsv6Eud0JNnVtK3j3VemJLV4cPxagaZEVa7czGAstxlNJVd_wNqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27478" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE6RNadsqs2IamzO5HlPWFkhvEp2Fn1-VjTn3tu2-2KYIZrTWSiCLb8lo6IykPsdCJj7SABpv-OwvqIm6heJXMnLC3iwuSjSCp_8HLy3hrvprXFDj0e6VSqlmEsCOlYnNZOUe8YUWqGp0ect4FpW4dzJqPt3YCetlDylXKGOckEHGlZnJLNN45QUAP4x-WVS5LePmsgyw6Yk7EyP1OvPe_XkMhqLZ_Kxcg3lOrHgjEqHdGmPedcW6fT1ZowFW2vJ5utoskvLzE6m-pcY8x7FwJlLe0dlaWYLKZpPca1IVPVw0SlyTwZykwFqSG8sRodMOAC4kGQ44vprAXdB2H4rOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از جوزپه رینا ستاره‌سابق دورتموند که رفت آرمینیابیله‌‌فیلد و ازباشگاه خواست که در طول فصل براش یه خونه خوشکل بسازن، این درخواست رو بیله‌ فیلد قبول کرد و چون رینا توضیح نداده بود که چه خونه‌ای‌میخواسته درپایان فصل باشگاه بهش گفت که خونه‌ت آمادست و با این شاهکار روبرو شد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27476" target="_blank">📅 20:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27474">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-OaGdUaJ4bew8a4FMUVoXv0pQCx58JKE_dAIPlsIZltbHm0QUlASK_xl2QwvAU2ldxt6m5iNdClUVNJXk5WQ7PGctZ2ASHIP5ubca_VXRfb65Dm1x_N8OnYwANiQGPFgB-J_fvTiORYrxJV5HQz_pmnBznfRyP2LipcXJ20RAvFG6XvJZ_AA7llux-dUah1_GWTdt1zcDLUgufh_cGiJVE9U3QCShSAbkNB7K-BSKYbgiIyVljwf2LGf6mhQt1BXo2_FXp8XNR-0CH1m-MbKHEK8rfhMjx0s4iBmKBTnfbJb3h1ZUQreKssIjHDgDzjs10Rl0QZDyEb_7xrBPWORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eiwWotVFLdLS9-z1mSIdva_enuxB4zPA-IyzaM3A_2VTdQOUaNazZ3yaaLzpjmJf1VS4T8GzHv6XLcVL2H73iIcNRfRrYLq1IPqHjULP9ZlCA0cKZ-v-xRpfiXTp2eAxmhAut8CVTzZebi7CuxMVuDdYWg1gbLs_oanb9M76i69k4q8xRky7uDQv_kBl4SqgA0OPU7CxAO3_kzHLrV_49wMzjyXi4fAH4pgZUntmDqyzhrjyiHj087l3q8R8wwc8-Lo--4jWvs6_StBTSUAWt1K-aUEhPKQTQ-37D5yset2yWRvzG9Gh8tspHTkmBSKx1ubB4yymKGQl9-gUujXXPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27474" target="_blank">📅 20:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27473">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1CQ-Or9ZkFtVZn5qmfvEKotjlq3lcdVgBjmaBpAlY_o3t7Xa7OORW4wU65homJLpBRTbfU0vIZkbOk5V7ZRINGpmNx8mP4TIime4adgpBvAFJx1knoe5txBsNitiOJvoI7RvXKbyBZLXGuruCGxvwnZSdj2xytrgeUVQOlgjevJprEz_ZzPg2dF9EPBUYLByFsTmxCKa1UT6AMYQUIP6YwXjNzyU-iNg-NnWKuMQ4HmIbvEQuT7-tR8sqnIArUg1g8HF0ovFRrqKIA3hq-2n0-B0ZsBaM6HBMr27Pp42MwPJsfsEHTI58XCQZfneG25b-MO7brTYF224G7csLWKAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27473" target="_blank">📅 19:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27472">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftkr-T1SG2GPWLOuo-KItrGK1Bf7MjHdTRD8dsrI56DqGlRC_OUQ_1hOal1IotIonyRYy8m81vtqP8Wlk_A1LrHmuQkImM6DeJS_PGyGA7exWh39aJiKxa_j76EoGORMLYd5Da7tn1B8XWOHCoXYdfO_rfWiC7QlMRJRSWG0UpsSBMEpgl3Y8QP7He8dKG0ot9tY_JsnNslB5TI2irxEt2cErVuf7u5k9O-KnZDczUTjiMjVSfTVgXX076LIQJnMWDHUpPYap--lFPwDkxPhNXqbvUGcrq2WKm3Fvs2boJoZpJa-2Zogyn00e5p9mEvbhObo0tJTtjdsSDBerTbYGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
ایفمارک و زهره هراتیان درحال‌برسی پرونده مصدومیت‌آلمدین‌زیلیکیچ‌بازیکن‌خارجی فصل‌گذشته استقلاله. درصورتی تاییدیه ایفمارک؛ سهمیه هشتم و سوخته استقلال تا پایان هفته احیا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27472" target="_blank">📅 19:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27471">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=SyH1JiXwbeIy4ugoTGUdSjQzK4_IiVV0FiSbDM8XqwDx7W5VKSWKvNvemQ1rZAA-IgIgqo1_Qk0GDYfbn6C4YKxox4XOFQSp9rqbXHkhrcsmbSKYvQGwVbJ1fmpT-QlPILiALyIb7BNKpHMtmTPSAt5RGAq4i1JHgO-Hc1uSqbiVHRExCBzi2580T5NEgvEwr8FL54cVKbnWElatv8T0gRLjgnO6QxLjiCZZ25hNQfFwU1T8GvVbFmP3vhBro_sihZGzxkEupxtOPXs6DAmH8XRMINQQEjn3RcxwwBAXfXfApS80UDFzkM3DR5XgOejQ0lJWtQtQbVojluwI3s0BDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=SyH1JiXwbeIy4ugoTGUdSjQzK4_IiVV0FiSbDM8XqwDx7W5VKSWKvNvemQ1rZAA-IgIgqo1_Qk0GDYfbn6C4YKxox4XOFQSp9rqbXHkhrcsmbSKYvQGwVbJ1fmpT-QlPILiALyIb7BNKpHMtmTPSAt5RGAq4i1JHgO-Hc1uSqbiVHRExCBzi2580T5NEgvEwr8FL54cVKbnWElatv8T0gRLjgnO6QxLjiCZZ25hNQfFwU1T8GvVbFmP3vhBro_sihZGzxkEupxtOPXs6DAmH8XRMINQQEjn3RcxwwBAXfXfApS80UDFzkM3DR5XgOejQ0lJWtQtQbVojluwI3s0BDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
عمق اسکواد رئال مادرید درفصل‌جدید رقابت‌ها؛ کنجکاوم‌ببینم‌مورینیو با این اسکواد جام میاره یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27471" target="_blank">📅 19:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27470">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=OYgh9Hyjzvulj9Ua-0Y11WlouaV-wlGobBtf2fGORAbsMHxdoyMULf9KZY9qP2zviK-8gDxmnJFFZ-_7vM_K3tRl9_am8fCdV9THQKZIkRSLs9SG0jvmX5qllf619A1EyLFikIv8_hSYqZSimYwvj1p5kJtan6dJ9ZeNtF6eSQ2qvp2Ko-NjGdNyRAWOA5wDKJfiLPTCjgX_fk1dd0fIm3ctSftRoPCyVT1bzankHtQGOyhf052U4xmO0Qs2sQjgcCTBIjO7AZDRne5w-H2IU9HJfVU2BofpPQuL1AybSZL0WihE3rJBMM5EoXy38AtnfPtdiCdgl4kakYvJIk3HsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=OYgh9Hyjzvulj9Ua-0Y11WlouaV-wlGobBtf2fGORAbsMHxdoyMULf9KZY9qP2zviK-8gDxmnJFFZ-_7vM_K3tRl9_am8fCdV9THQKZIkRSLs9SG0jvmX5qllf619A1EyLFikIv8_hSYqZSimYwvj1p5kJtan6dJ9ZeNtF6eSQ2qvp2Ko-NjGdNyRAWOA5wDKJfiLPTCjgX_fk1dd0fIm3ctSftRoPCyVT1bzankHtQGOyhf052U4xmO0Qs2sQjgcCTBIjO7AZDRne5w-H2IU9HJfVU2BofpPQuL1AybSZL0WihE3rJBMM5EoXy38AtnfPtdiCdgl4kakYvJIk3HsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیتر ورزش 3: کاپیتان‌تیم‌ملی به صدرنشین هلند پیوست. واقعیت: کلا یه‌هفته‌ از لیگ‌برتر هلند گذشته و جهانبخش رفته تیمی که پارسال سیزدهم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27470" target="_blank">📅 18:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27469">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkthvk5MqhYPPV3-skYPjJ0wJ9dvotu8Xa9GCAE7gkoio7FhbyJt6HOwg-9IUtXMlrUhL9sImHRPEM6BZyUJspJKyvDjFOqk8TQP4ri7fi_ZE9IjcY87ntPI9eQHso51E6euf19nMFDP9FKhi5uiuI6e1N7-YLiXqBSCyr0zUE1WC4jpW43DQAZKJmQhj_xVEz6ZhjMDl6kusrWgNaJ6aRCgLomM2AWctvb-8PzDzCwUCup4LS4H8FSwQirEJM7GmzHoGGJsTiy-tTJDx_urGux9BpMhpsQDJ7lLQTLaeWAI-a7npzfvNV7dKJuX-blTZeR1S4JkChO7xhWjeTXCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجتبی‌جباری اخیرا باقراردادی یکساله سرمربی تیم لیگ یکی شناور سازی قشم شده؛ و بعدش سریع مرتضی‌تبریزی، امین‌قاسمی‌نژاد و داریوش شجاعیان رو با خودش به این‌تیم برده؛ جالبه هر ۳ خرید روزی به عنوان بمب نقل و انتقالاتی به استقلال آمدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27469" target="_blank">📅 18:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27468">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBULD613cNHgJwLH-pgahtn4WXrbc5q3zB-ANCyinGNcHWt0co0OSReUN-bxdwxaN0cklLZ617hqbxOfvONOXwrAz-jDzqN8hYUj-j14PT6_DpWV9FDOcLZho5jXVHLMk3xKpHri01PYY3HUtXIqtGMNEWtQid1YZAMz3Ly7QfkHNB3Q9NKKSt0UOH3EgUKvwdyt8CHtOy7_PWr29_73DRQlBRVipdR9inxk_IJlZA4tFTG83JQmXODXm9AO-xDhwoM7eHksX_YazzZZVhjKO3A2st_UvvO8InjTNNWzhJXai9APc0ikoAVkrc46dzSZ3rS1NblBLLUlMbluyTzJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🤩
برترین عناوین تاریخ‌فوتبال‌جهان در تصاحب کریس رونالدو و لیونل مسی دو اسطوره تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27468" target="_blank">📅 18:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27467">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCtuzYSEgOY4lbFZqSYpH53ON252a_GiDgff5RYUcw9svn3L3i_PwyQX6JgBmIDvjOdlR4EmayRYqEcqhYQVxfqOJu3EHwa_qAwGlrG2TGYV6zrDFWUvKMVxuo6qhOL3pEp0MJom_xn0AdVTVPK-iGyMn9iHmA-uOZByQAqrANOpcrzb7gtGB--pWOQ8OdHNquJFbUxQZoSqEtZcu3A0Wi8g_Mkjz1_Rhc475Xal86Py7SdwBh8xeBvTNsAeCYnifRXeFNHYKJghtNVNpmD70Xcxr1hiZlyD0OAPms_UgXa-CENufpK4vRSIlBloLWmSmhD5dLmfzq36qWyERxqvkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27467" target="_blank">📅 17:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27466">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwBiA9uOb8ROyqwcMQYbQUjPlyPyNR2qgEub3ts9o6K4zHPfcaip2xHkTvKDjerROBQ7IyKeOos_WvmPOwUrMf9d5N_DUxdrsUEsQVUBpgBQIPu_8-fcTuoLE-qTQayBBJJOVYkugEwTG8QHvBwn362PGPX82sgKGTUGjDRmnUaJDInniT_9GJVP2wixzqtj0CKhIeGf9Tl-oBLFghyg8hKLmkof9FRo_H168tp-D4mR4vaNn_WU6KL5Ym1CHjvcxDl43y9vhrfARFy8hSv3dHwE0r2RERlpSia4EWt692XLcV2zbeMI4i21_O-A5SAvZDH6S2eqUcnq0nJthdpK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه‌دیدارهای هفته‌اول رقابت‌های فصل جدید لیگ برتر؛ تنها چهار روز تا آغاز دوره جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27466" target="_blank">📅 17:31 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
