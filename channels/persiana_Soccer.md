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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 16:17:19</div>
<hr>

<div class="tg-post" id="msg-27580">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEXCTJpPdlBLgKhY3vZ4OGK7KmrlHU1usLyUpK6jcDl8ZhfK7TKbcroBMCFV9LzM5Rb9prXbriV1EQbnPEEgqiTIPHl8gW8UpQLX9ZVy3SN2GuafEHMSTJAP7vjymLR45MSv4sfJEgqQYIhcN1jc7uQwgxqhtfjZZ-AQAs8m_hzDMEl2_Cim4wNCoNhyw_2pdJmFU7Lz158aLPs-6HTbslCTA_uPx0cAi0FeuQFxqSSsUE0Tl0Nrki3d4xuaVCM40XipweJF39uNHbIy65NWoZG1kuTTKR1ms0HB6VPjxTyz693kM7sVvKpXfMmaePkXiIrIhQU9jL-Q7ydb5-ZZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/27580" target="_blank">📅 15:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27579">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFICh4Ktln74Trnr7WFH_oK-mU5qGR2_oIJUEDF72wEHnyoT-BDuafXE41LPqUG1m4ioioDmX5zd9cen54KfTc3nAgN8RsumnykrPeeM3WzP3p4yGU3eVazIxAkRYMYMW43HCaUSJhV-uC7CruJnSO53ruj89J_EThvIsPEDxpQMeWp3RxzXcD283t7nVf004O2MDIpyre1qxlWzW51zoL2FG4poFzWf0pm92iHUr8GW9jENWwZoKYV_Ou6Aa880mS2lMckbDI7Vnw-69G1fYa0zbQwbkndkh_u87moSrPbB9NjPbAVfgF5lkauZT6-lWqN3bXxBUNFQihRDv_iFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
چنین‌روزی درسال2014
؛ تونی کروس اولین بازی رسمی خود را برای رئال مادرید انجام داد. او در این بازی، اولین جام خود را به دست آورد. این جام، سوپر جام اروپا بود که در برابر سویا به دست آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/27579" target="_blank">📅 15:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27578">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTLsc2LynphsAU1SDrXzIJvModL6VovRFxP_B8-83E7aP57luyDWQIyQjLVotPzDfFfFPnp7pnJ9eL9IFK1LNxS4Bv8wjnJ9bsu6hlfL5kXUkB7uQR3K5a-7_yxFudWE_uKRj6k0ppiEKhpTFb3W7Y6j9I8Eyk1wiO4LUsc6VWEm6g1TkO2nf9_tfkj70LYr8WDp37E--15K6M7ok3kQow086ks0DfobcGmZjfk1sGxYPL3RSOBC5avguendTFTupyIrxWdy3gHV_4wx3VZza8MXafOwT5JzJ9xoOYqC907qvYc9hUjcWDCpkxZu48CcV2R-Ki4BM6WVw9z97mA9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال طبق قرارداد بسته شده باید 200 هزار دلار برای فصل قبل و 400 هزار دلار برای پیش پرداختی فصل جدید به داکنز نازون پرداخت کنند. بنابر این نازون چه برای تیم استقلال بازی کند چه‌نکند باید این مبلغ به او پرداخت شود. اگر نشود‌ باکوچیک ترین شکایت داکنز…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/27578" target="_blank">📅 14:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27577">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjAqcDx0ENZ0nsn4JhHJBaDw9d4B8xvKAlEZqrKiW9aXcwMu0EXlQHUU6Fk8yeoqKntpsFSJz3s1NdhT9Zo85oOcbRgeDhGGMMlKCbIA2jN_vkWCN4VFjZFvA1S8ARRj63IdTa5iH2PbvBkGhfIeqq40vPv3U0DWK2M30eWG-ozeyMpkGfj1uP1oWDqc1bG0QXzcjtJmo0m7HTL_Fk0DiQlXaPUOWVHofa7IEf8X0U5hqbH2Yh5kXZIvSKKoBgtFthRUziVQqEozFaPiwunFX3iCutlJiN-8-SusceICBfjKlnHxhFPiudOhu6VbO62Ung7yNWZZlNRMHBih3yau_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/27577" target="_blank">📅 14:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27576">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHSf3JyT6DtUz8mD2ZO-YIzJfzEZcFcuJAXf4JHA2PH9OmwUs675Kvdv866tgnpAbFGKl4cWtTBT_M4eW1-HEkCok4ZhReXG7c-5eJHkmmcwPn19al5U0lnyBtOt8kDxB08WcAZck82ve8NqhKfaisBPgfGhKDLEkSgr_5xOgTdXCqPDP6K7khIg4--s_7Oc4MqU7yILoZZ4VuLnrMU1kRCUJO7S_BCevQEab7rR9Ts3Vq33_N0RWsic_uo_YKj--ZF8RozQnKD6TdwnXDPydgmjjjYHVlqYEvi8ssNnlQLnCWA9V_P0A4d9LKS84_2yg4Y8IUTj6SdHUYWowq_J8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش روزبه سینکی به صحبت‌های شب گذشته رامین رضاییان روی آنتن زنده: به تخم مردم نیست‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/27576" target="_blank">📅 14:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27575">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq66RhJ6MlS4R_xvhDe5cZJxdfS0303K10-jZAFilfwFz5s5QmXMADlRZFuDFU8GRbOuOS0Wm9e3u2ZYED9Af46WvkY9vYr8aLoa_960teu-gmIw9kRBWkdFLnzKi0-MtpKQkkw_PEIsQviTChHGrFxsgsOwoWgAHt6g1GGWpotNtx7bfk_vEYzjwYhOIIRbgxk_b0hHePHfWl3pZPsfZ2HEVp4cJvNmS0et_AkQotIqfFkwOfBWqlrV-FR4DbGPDw7aMhiDeAAYfTMRiMIUHs92OVban7cyRFTLjKfluEuMvC7jyNaMW1ikD-XwwPyHRNrgdJgePJaG2ASpEBD1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/27575" target="_blank">📅 13:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27574">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-8ZHFLj-rgmG0aeKQeCCVNPWCcQojDPR_4-Q8BzPa1VA51yB9PEcxlpGIhWnn45LfFCjZ-fePHDsQJrxQEUM0_iIzYC-88WVNLuZ-wIe1lxaesrFwqW17ZLbqjYReO73kfu77rnmdFTV6nChAK07QN8lnZcSuYE07pPH91vU2VMLB006PCq5G05p96lBcjUJBv59Z7yweECaY1NoBQKTd0P30Ub-VQ28TnZg6msnK8O3Lp9SmKm1dC52OGIbbHzDmgeITNjFGuVruxb4w3ScPgxr9itmARyGwNGlEH8fyG6zEUBwf7bS3N28jpTX9FgfHcCBh4OfzqAoEs38hnw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/27574" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27573">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOun21i5izNeYOcsPETbqO_yoR77jpMkj3OaVM40bAGc4qykw7YuLPJX9WbmbqJw-Cj-TRJaxECJafSKfNguit2zzkBVRClfJu1L-uTg33IxR8lbvAxcOe2wEESbguYjrF7zZ8-zfkMraktrqelUL_trm4Z9BCg-HHgayotFt_cpgAwAwy6hUxt7jitw4mg7LjlBNwjNf8K5Kq8jRLYRNYaiwmgFpZwNJ0m4KJkN3g6qZwB5Ck2SAxBAWiPYrjJJP7uq0mMG9f-7r0kh-FRP5Lp91dngd8z5AlR-qzci0L1MmHdoBgSgX6pNgxjzSCHkyUhXaBxApnZREAozJJu5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/27573" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27572">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/27572" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27571">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV2fO4KiG_KIOfrMx5H43FyZcbsg50EKaO18ttsWLsJA2SgFjcL2_jof3GYci_S6_ixwV_6C9gPW592tGVwbckwcJv7YB_ap6guS7lW8HaTdc38xg5kqVGRrxrLnz2uZ4_nSq8H-X3N3I9YjwI0WHkcw0MT0v6baLO0A-C07vozQ5fh1hlSefFrh27PtFm4EDHL6HArFS3fp0Ayy7jlkqqkv9fLnbfc9goEL2zgzYWdgFF73gE3T4BI0BJdyWvDRTYscQK6A_L5D3UBvQ1r_I6ix7OFS04iLzxfVZAVQykiUtPHtKWmEQ-fmI2mUjsQLpsGAARaBq2GCZ1C1nhUIfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌سائوپائولو داشته‌ازکشور واسه‌بازی دوستانه خارج میشده که تو اتوبوس تیم 86 کیلو ماری‌جوانا پیدا میکنن؛ حالا سه نفر از اعضای تیم و چندین نفر از کارمندای باشگاه مظنون شدن و در حال بررسین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/27571" target="_blank">📅 13:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27569">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIiHqTncLMcVCYwxMl-j93H2FzLgHXt9HwjCEdCs_2cLvWaE7Y8WjBHUn3tp5UstsGGXLwdFNPOisB3ZohunAGN4EtAbM32ck19Mq0JXpiMlmXxJgY8NyzUpSsCEGjg3YldByJLBTkvdbrVZWCKlE3jrYBp8sNjOjBbOQtxCRnIlhPvlZ-X0TNylbWj17dIArYXrIfBvyaAHN_cJn3GdkNC6KjxoxcBmVHZljGihQm4r_tnLfxkaOJh4u_s3RxCbbPpYNILW318-usuorvMdk8KOKG9boHAbGZrZo74wtxxhm41HwZR8HfQ779usGRnzT1AEZuJcMMCI0dHsXsOkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو بمناسبت ازدواج رسمی‌اش با جورجینا یک قصر در عربستان به ارزش 22 میلیون یورو ناقابل به او هدیه داد و به نام خانومش زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/27569" target="_blank">📅 12:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27568">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
#فوری؛ بعداز حرفای‌دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌بازی…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/27568" target="_blank">📅 12:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27567">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn13Vx2Zbxx8q-6pA4iFgGq40Xywak8wO75r8sjjz4cY-zuEyS0s8xcjVcvkt1dXflFukOkKDhMLDuGAtxem1QWRWzT2rvgAMNcbXHkKOoBQj8-oDc5OZFkqeTTLmhVLMt8zjch2MfKQUMTaFrgCgT6s5ZyBqygrx4ToCjmEiIZZASNIK9q4-CCqvFxja2A1Syk0U-DkTnWC54ryQ98KwxiCQcfpM3phsB_XFyNx0Spj_-7i8QiAoWAztNP7UVA3pJBzrJWkiSomHbW4M4sDUj9k7j5vABTxkYBZYTpGQDgeA1eahhQFPh0p0BpgV46mv3N6JjpE88oGWxkW2WUfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
بااعلام سازمان لیگ؛ دیدار این هفته استقلال مقابل مس شهربابک در ورزشگاه شهر قدس با حضور هواداران تیم استقلال برگزار میشود. بعد از 229 روز بالاخره پای هواداران فوتبال به استادیوم باز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/27567" target="_blank">📅 11:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27566">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec3WuAPauD5BSa0TlBXLT_rleq_NQtUXWLozgkdB536Qni9dJ6LMJ2jiJVP2UbHl7BK-x5X-sRKLy64T7fgwzq7EqaOMq0DmtcY07yHaY0eRIIOndqRDIZ7U4W_zQNEY-bM4IscBpvHbKzYt1EhqQjJxcjdWZO5B19DZyHMnM5RJYAJYFqzZ1hw9ZlLubOVRBHZm_1BZAoXo1bk9Whti0WNIjKqrRyFmlP3XMDuj_jasyz4SvT-7NOUzwN8Ri9sU0ivx0xfML2iQFOyzMMxEBHXeM18qNPzPAwBLmkyfSDrlEXz9S1lw0Ko4jtpR3HXvFBYrHEFr-kshOKOg2GqDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/27566" target="_blank">📅 10:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27565">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7L5PV6ewBSgNb8JRsiO53Lh8C9QwRi603LriGUJ18R0MXMIJzm73tzhR8t4z1TLm5WLBT0LN-CQzv9YH5Z8eKA4hPEUG3vyLoGLfJYZvLbR4ayyoEeyN7a85-bCLNMykXnSGwurIPFiwZAROTaM5pYkBM5WiD1fn6hQ4_gISbvbrbMWKyHQ1dcvdbH4b3AX0XvwffwwJ6lHG06Cst72PacjHECEhB9E8Tv1KMLeWcX84D9Ebt9y6qdVRi4d9U0AvpylySVYXER90lhnNudg4HcSDrkM0y4Ofi9ZsbnIITUVUQMKtxQiNpQ4FngiRydtUnGUf_XprrsYWbl_UH_XcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/27565" target="_blank">📅 10:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27564">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAN6-7ViViUNG0DL8ud_FY4GhNzpshkX7mHZ-nOIiocmqBi7jn7_tj5WcTg9jr48VR-FZ3Z6L9JUghYkCZVcMMuFkfRX6EwP1rleDEckm_GMw_mwXi-MROYJeNjOOHzHZ4sEvikd8Hn163WN0o5crwYfkSG4Rmv_TIQkq_AWfqmiIyfE0_qdE6AnzfBCNHFQfuW20yxlawSMPERWT5eofHTDokmy039-Qv2nqWIeFaTlLDYr4LqQpUt-X8v9oEPJ8ITYweL6a_Fk9eyz6WSJeGFMru4bHSzTrM0-0LOV32mcwYaKi-ii50wiEtdH8eKP722x3hY6E0v84ReheEzSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27564" target="_blank">📅 10:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27563">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZkL3H0Yk66PdNihoXSRfiql0xDAoaLDVS2BfXqkSfK0DMCYXgcwYo0obQUppejI6J-QEpZY0WK7R9BDCFS1MA6V4EaBFpwCBKRVV23LYaqbT-DyDaKUZwgPeNMTgp9RIlg_blbp8i77xiyItm0U8s-2XVoHmEw8FTNWzelnBPiTqsqQKwajqb7CRtCctCj-bn6zgp3dvUePpF7T6r-X1TDQHx9-S8LT6dQSbr835cuTjOxdpQJ8dGSxFfPpzk5_GMDGMMuOEQQxFn1buRwge-C6aq8iEMLzHI5PEwgkVt4sco2Ec2-8hO-QcAgXy7WHzwjdc9_fwMOxD9OTYT4lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
خبراومده‌که‌باشگاه پرسپولیس عملا قید جذب محمد قربانی رو به‌دلیل بالا بودن رقم رضایت نامه زده. در واقع باشگاه پرسپولیس با جذب لطیفی‌ فر و پورعلی عملا برنامه‌ای‌برای‌جذب قربانی نداشت و با تراکتوری‌ها نیز به‌توافق رسیده بود که ما محبی رو میگیریم قربانی هم…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/27563" target="_blank">📅 09:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27562">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofRPtuAG0dJ2mXea8OJmpjenqw9IpmBFFTg_vuv9R4iu0bIfmHk_k1v85nTR0r0PR35WN_e-z8DOxAawo7EO9sxadxwYUKSH7IfGqKtJ20IEg_1nM6nstLEJ_VBGM0NTu3yZZDNOIbO36J3LwEME54qSQsynunyG4RHJkPZr1HpPps0TJqsjHHjAoGVW3lrku2gvmrN7BvgFsTGHzUcgm639Ylit_8X0jPJuNaDtWfMqaQ_aqbwe8ALsHuHJGeBE75VLCuxF-hu8Z158xXdRgq89OSIY0ROM_5IeX7VFV0Tk3oYapCCtdgSJ2Q4Q3s384jZu74UA6ZmXemDV6hzQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27562" target="_blank">📅 01:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27561">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbVgnyGVe1jxYavEKUeiNQTGtgRuJsH3AWxeaDArRUIZqkec1sN2UzsYHLzGHbHc7FldtRqt0bkj5gkfQWUZo3ZdCZ-Za0ooEuQeIgCdcvixiWyPUy10eTBtLfvO-nhnDqxKJtQMBpFKbS9tJyN30ejkWnHj8PFtDZk5b9nOjsV3Rp2Ppkb5xOOP0yNI5Gr1HiPAkZBm0SYlZWIYanZtF1a5xi9IcelqjIZs2jCqdtyKpLJE-eR9PHRgL7Yg3rr-1Z7meGW965Dx7IEiHvRHp1hxsLPd4mbmBYbqf66EJlwounYQDFQYPUG2DlTCaDkwa2S22jnYX8QXe9TI7xGaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛
تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27561" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27560">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9XRHXE53NnmG1S9XK92xD1JOVTk2YWHyh3MqFdvY2NtO_ho5Vvi3ZU-ejDsWU13j0QhdW0wjZw6IXSwerP2JKnHg8dx4fo47NKjlgbZnlQiEdzWy3Zm8JYSst9zyda_IXjE6o_SIV8Deyxd4IHmrli3wZsSaZp3m0qM7Buey1t99ZnPSOASgBdPWUcy3_regaB_zExAwAAy0CTi7Oj9antWJZCw-3I_I1h-psOFJlqYO6s_eK1q1EMc655n1iL2fnEnSu1WfUQcOpPqyy6xaJqy0KPTZtYpflMaIkqMngBGsMvkDwwVCufp-Biy0TClkvFfKOEwpPpaikDBJA9ikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
کامبک‌المپیک لیون در بازی برگشت و برتری فنرباغچه با ‌گل تالیسکا در دور سوم پلی‌ اف UCL؛ کارتال و فنرباغچه عالی مینوازند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27560" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27559">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27559" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27558">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=h9tIRzitDGrz2lFkeREh8oOUGyweTlGUaAKXRo5o7hvbe0KWm6z7pLpXLfthcI9bvfpLlSzsFrve6UvfXaZbaXik0R3hZUNxPt55FTiJurnUyLc3MeK6ZhVjaOeerEQYoMCcxumZve5DUIUmjL7Cwb0PIk4VQS91jFm_NCS78_p08iTFXhgoOHyqDDVYrR7FLrm3g0JMHVkwN9ajo8aXbwKrak2ZTpaM2R8NCJ3ML8xe0RrmawQwWGY9iBI_KDUSx1BLEDibisfqJWxNhzUdHPrIeKjlhHDmFN0NyBNploBsIbU4rI45LBCdwDHnPo1ls8ljoSD_4afigS8o7DITqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=h9tIRzitDGrz2lFkeREh8oOUGyweTlGUaAKXRo5o7hvbe0KWm6z7pLpXLfthcI9bvfpLlSzsFrve6UvfXaZbaXik0R3hZUNxPt55FTiJurnUyLc3MeK6ZhVjaOeerEQYoMCcxumZve5DUIUmjL7Cwb0PIk4VQS91jFm_NCS78_p08iTFXhgoOHyqDDVYrR7FLrm3g0JMHVkwN9ajo8aXbwKrak2ZTpaM2R8NCJ3ML8xe0RrmawQwWGY9iBI_KDUSx1BLEDibisfqJWxNhzUdHPrIeKjlhHDmFN0NyBNploBsIbU4rI45LBCdwDHnPo1ls8ljoSD_4afigS8o7DITqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکوردی‌فوق‌العاده‌برای CR7؛ پست اینستاگرامی رونالدو در فاصله سه ساعت از مرز 10 میلیون لایک گذاشت. فک کنم بعد از 24 ساعت عدد خفنی بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27558" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27556">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2ygUyVQZF3FgIYGnkVG80U9s6lKvTzh_HLdgtNzG42m9NDX01Ef-gdnuF1FUZGirZfq6Yogfe65ekeJaTOvkAhBCi5Q6h9IQ6M_HANBnZXpiLMVSahLtP6evHzrzaoiSgp2pAGXBiUrNfBHNn300jBaa7gAHA3YQWn3CXP9VXFk0eVs0eV_aVO-nRgbx7X0IkE56ib_UJ0tLw-sShcjhiFmefg-0uJ2Kq-LRCBbNxHqVCUYM9Cfllt1K0HRWqAnIRPSEKfie9VlGTNYqehNpc8o-ylTbUItyfwgi481iLIpfTfAA37Oyi_FRJgdnHQUYh2VFTBL0fF0Ga6veTzgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27556" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27555">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvb9UT1lQMyn09YRq0M1j4RsFKnOhlbgp_DnHC2DU7jAruNHTy0n3Y9iPuoeaCJnJVCw8h8loMmN68ZJaeANRBpm8Ady1DIa9nTra4Wt279t1GbgngS8A0un2vAeQprLA_iiqGOSzillIwA_vQl9VAyBd0uCsAF-FyMwpmaPo60YAcasSZPLgsTO5-Kf05v_gX03eaQaLcaorDemakw5mkJ4Dnpvn7-ofq2amKNxh1GviRQaarYIdVdg5hTxS4gVyogKTFc5RVarIuZzXGolMqjWT06GG7SXQ2b6JmzIT5G-Eb2mvalbS08PXIfM9y5pRjzAoqG6fM2qR4EsL4RWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27555" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27554">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwfiW1BXj6bmuXxx3eDO_rjarY2df7Kb6-Yn1VqzflLXI5YnxBAbdWSVC_FwyZ4O4WK8fxszHLzIW6ZshMcs48tzQ12ZrRDDjGYRELhys4NNYcLSwlYPSm-GIRMJZnGmPnFIEizGhGpNwj-8cQCnLqM8CZ9b29UE6Gho8cLMzLkOyoLUOtUKNDK-LNIcGA-x_qZIsCVWFLiCNffBCKnPjUYZzWuPl54tqvp6Lg9d00sCgC3B5fCQ5IZz-wsi3y_tExTV2cf3q4xSiAqXDHwo0SsMyeW5U1VYSgCcIwwB5f5A2OFBMbJA8pthmM7mBUUKyIeqXZjFKq5BJ4Py6gHOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27554" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27553">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHacpfXZjxvw3KXg3s8qCWAsu2Pn6ObEnVcOd55gdbNUcjK4Q_fBHnqLtctPVdDQhblE2A48zzPvwRXcbs2vjx7QRVnJiLqg2lAQbDArudb4QncnVdyhH8WSJfPBX3641Roa-0djdB0HVrkHmCHU_I13c-wwVuHaPBiyqOmjGoV_QnAYD1-ohZHlfTkjr4YfkF-vX318L0cppDm1j7Tkyz9hKvjLaDxk1SQqWK05RMVG33h1kI_IT_LXeC9axMle0IS7dHx42MFjX_Wc9EA8c6UhXpUlDOGZUEl6JYFg5p_K7NGOkVUV5vT_06ou1Z7TPBTfOMuU35GlaL58H_ljWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو اسطوره‌پرتغالی‌جهان با انتشار این پست خبر از ازدواج رسمی‌اش با جورجینا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27553" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27552">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇹
🇧🇷
ویدیویی از عملکرد فوق العاده دیدنی و برگ ریزون رونالدینیو شاعرفوتبال‌جهان در فصل 2009
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27552" target="_blank">📅 23:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27551">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNU5WzP-4wjuZ_g-FzZ1OJLNxS6bhmoN9jWO47KCpTxy218jG1h80y36HRL1F49LxwvMKwclYX80mNhjpgJ2hdKqF5rKKRHiAWzVqD1q9p1irC3gnZFc4NVRY5GvBCCeAOrT6ewe75BQOAEwcn9RrC7P_h6w_r4PJDMtPKIvv7yLul69RvD3dcjYLDuc167CtfQqsyZDwqM0mFsCH2X-fD3emygBqGCUUXRKRMGBr7NBAwmpuRrsAxUz5tQDELiI-V6cf8d_Tt63w01J08GfAhD-Uzx4Zhkpqsdz6yjkCB9tfxxVGgoG8VSXaE5FRFVhdKuuL3yftTpr2HoyZjPQQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27551" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27550">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Z7j4FhQSFdJOXtXAWwjpviYQX1Bs_DsE3g30yu3nGUgZ9Z7025PAkkKmDTYJYrsX5DO7KjT_GnklK96kUqktkpmsC7jX2n9ASRQeTSpOAvl24hNN0cRcXE2mW83Gk8qRoyF7hKdWraM9_q2WpQOqOXRRBTEZGoOg5NoZ8W0tqCJ8hwUJOWKODIY4e-HkYRNkAHj5qW0OsjXLE74bHl1VCzKUvuwr2ZdkdREEpTdEq8qht_CdW4HgMrGwY0TZFydVjOLLvCc-mNxPSpaHqETR-S_QMiaiuOka_xYQXUDcacLT7ddWLuLB0Ad0l1NRzm-Yq5wTx2i6iP0hm_767evw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27550" target="_blank">📅 22:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27549">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcEmscVvT1URmQj-_kFXrG2SgoOju5rAiNeQqfXxxw99x-o61jQ-8760XvuDbJ7QcgBtrNR2Za1ZKQlMsGTKXHBhsDdiC5J_ZxPv_Y9PaIac42n7L7DJGGNrLRm_ZI9_wI7SMRJkveRlZYarbszKnFAYcptxKkTtOIWJI4IV0RcN5xTL06fj-6-QOy0cWx5a5HQzQiAyzn_07A3P0dKQzaS6ak6JwC8LKKluBV29_7xXAy5i_KxZxqijwE4rS_Z6loOtS-UpA3e82hDSm3ADbUXOqAWEpeOaVOTAwlDciFno63nfCG0_xvOJPJAYeozPKN3KiMP8wYncKI0rclr57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27549" target="_blank">📅 22:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27548">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-DXWlbO0FnW-igXjNcOZEfSRF5BOOq0qiQEuJuh5DA1ydZqloyHJ8Qbo77b9qMqTrni_HtauuTKU_YTYfGvafhl78v5jOdGiOIzSSgr4vp3vlsLWbgThUMEFYXIbo3TvvDfREwZ64M69SH3OdkfnNWoVYybfNnTnTaz97IT5P40GDCCDk85XDBqD2Adr125usKB6EqU1zvSCA4lw4shupfVsTdplolngMlnIOo_bd-1ududpt2QbzctGbp6q6_LKHpzfKmMH5HgK56SI5LAU0OTw2riTR14ay5IBFClLbqzPAcuwYUVhk8H7nZ8s3m3KreggqLVsKs2Vv2v1q9OAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام‌باشگاه‌پرسپولیس؛ سرژ اوریه مدافع‌راست ساحل‌عاجی بعداز توافق مالی با مدیران این باشگاه رسما از جمع سرخپوشان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27548" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27547">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkp6mk3g3tPp32ML454Vyy77jQKGLWjY3PZVBtN51R6DssEkF1NaP3c0tWYTFImIy0jxhMQkh_kG1P1elxTMIdgpbcUFocNmMp26p4XH2OwUKw84F69UEqQQwi8vayk2kIq3fNcvIIx1uIHdVd1QsWB6hTsShRz1c58uyusATnbGekLf6erWSgkryAkg_deI3ohjQ_Y3jsPATIbBzRLLbla51l24yNBKzxrg_Rrc0kjc-O31P6qtO7QdOKLvuesCWixAvc620-hbdGHPLTkrk8jkShkeSpUDw_lQGnrxk5RFcvKX0BNn1YfYkUf4hNDsntpesDRqBDS-lPYB_kKvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27547" target="_blank">📅 21:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27546">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuRpIKu_6UIKoag3G-QR1QGWP37O0giygHqv3R_duVHrG8JmJs4EfRdelODRp6EA4OqAIRxyDMYlzL2nq66-7CjC5BwIk4H5_MdqPNt0vH6AGkLcJOnohsGODbWXkFPb0AtC-JCqn7rve1xtTugWwfleTjHiiDu5viWwoIWdhS_qDeZWV8VH7b7XOtnyd0KQWhTd8nq4zjTVpJCbz4EBPoo-kDsMwzQtohjgWlmpiL1bsDBGhVo-vf2qCRVHs81ObXD_Ne7lIgEkw1L1_b67t2qp3FvvtfWuDC7r60_JtXqtRUwkJlaBS5BQr9yTVECmXZoWLxkot10Y8W0wCCay0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27546" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27545">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4PE7r1WrwewpjwqZC6d0FLakOgYSWImANbpD0Pwna9eHHp6R76gmwVdpa3h0vVu5kgsXUIm5MCihUugaoyLjZ3OHhOCjrgeyKP0KCA83uqTd0D7jVLPfqkNTXAYpad67a23e4zyPws1YH0aWoA8VKCAFKLtwjvnW8wdTTAjI8_mCPfYtD5VIZ_7jf6QhlZ4DG1N7rkPdJz02ByFEoZ9RU0Kneq66YN6XBAq8ODIWGXsoKwRpccArZYs4-IYdGbdlxpeDYW6Q4LA63s1X0lGpZd9F7WWHPSWMcXfaL7th7XzEd-SyGxvZAH6YthlwsKyI0CUkiC-C-5AuwkhjrCN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزیکشنبه پیش رو یک جلسه مهم در ساختمان فدراسیون‌بین‌هیات‌رئیسه فدراسیون فوتبال برگزار خواهد شد و اعضای هیات رئیسه برای اهدای جام قهرمانی به استقلال رای گیری خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27545" target="_blank">📅 21:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27544">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abN9qgCnJOH53CL1FJ_g5GPoK8Ztk7ibQsIv-nEbqG9SOSyoBatbQffmh8fBZ7BMFfFfmfepDrOkEsznmw-TtjF7JgaCaziuPudUqjSXyrh_Qvta3Uw_agXPn5pIuLGpnc1mSzOP3EK9eUwAn3xEJGUxp_udzYfN0fZLQ4yFU2QsDCcaDBJ6nimAFZbpUKElWmn4Rtz7TZLwDCNTRKMBHwSw4y6Roak85its1bQx1JeDIojQK6zayKvjpyHqz42BvcQcX6n-D46-alQN09NuJ2yhYimLkiLA28c3hWDqZHMWjY94DgSlXomDfNTkIDpmMNzvQ11JTkJashKPx8lfIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
بازگشت‌دوباره‌پُل‌پوگبا به‌فوتبال پس‌از ۲۶ ماه دوری! در شب شکست ۴-۱ موناکو مقابل رن، پل پوگبا از دقیقه ۸۵وارد زمین‌شد.  پل پوگبا بلافاصله بعداز سوت پایان مسابقه سجده شکر به‌جا آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27544" target="_blank">📅 21:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27543">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPa_XTqtL6ZRhnstlBbpDPZOgHLb7fPEUrD8M6VOideotvlUB2S6PGJFxfNtcNg_Ea1t1xoajMOaIycvSEuC4em7tGKfqXKdeyKPa4s1u74N67MhIs68aWTHhjzOZTEIr7rcmXQuPmqEy382G6EFFeOrzcpnBXKDTw2oQZOwcmyhsDeQxZwSyxgmb1PnLAb7HbbkP27IjhTvE-AghBnhOZ8FrxZUS1-NrYCuEspUSDW8pKoVHHhHowFrERdGO_6b4GTEQ8OG_hWmj8zxcAIPNS4oEBNFMSNNVpPQZsIvqQ8tcc2k3goxpSoP4CRYYkkICkA74WdypFb43iJS-Epk5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مرتضی پورعلی‌گنجی مدافع 34 ساله سابق پرسپولیس با عقد قراردادی یک ساله به ارزش 600 هزار دلار به باشگاه پاختاکور ازبکستان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27543" target="_blank">📅 20:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27542">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
#تکمیلی؛ 7 گل فوق العاده تماشایی در مستطیل سبز روی ضربات‌کات‌دار و ماهرانه ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27542" target="_blank">📅 20:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27541">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F55vrdRqtwwffX7OSGciZkxRFACZwamjw5jVfar7RA3VzZqHyqraLaXIj75rqzyJI-1F0Rg5BW04GO4rHoxz1HjgK8adUHBcBR9WXe6cUvvv9OIgcuEAdYFyMTo_7DECtTDIZiihNGzgUjR6mEV84o2nCB9yOWzpSm36kshIB359G-bkIMyQ1POHGSxOOxuNKXVUldglZthJEKpXfFWKXC5MtaN9krc4L-PMwTOtx-Aihdaf33XQee1d3Tpux9AgHDWd8CcYPXyu_xH50-tMkAcRaUD1Pp4fgY8_xX2Gor8l-vJW2OkRr9ukxiwGOhzdqeC9pxnWszEKNVpylBSkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال تخفیف است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27541" target="_blank">📅 19:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27540">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_yOqeH-WQ-55C2ZVYmsURYQf9i7HB6wvhj5H4q4sUiiLURdQUUdI0vhnV-f9NLHlvgeUT-Yl8g2mFoA74p7CpiplDnXZ2ZKw2isvKB9ZEFFDvVr7d-jXhSGsFC2AfvCAe3HkhSu2rmfzSUj7mCYK6onyHspMvDgblLs3S1NyBsCWAGdSGyxJ_4EaYmkM1hcKBDAIf0_Z6Ki3zHjFppqa9IdKOdmdaI8qZHZazNYlTOFlvxw0ePnt512z6VGsUlMGTyrmo-XofsbZEIBwgyA9qVeoDJx2UdAiEefR6VcGuZVFH1g-LycUzjOma42Bp0Do3sZeBC-YJWYbtAlCLL-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27540" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27539">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayLjOZjyAaHA9m-BAsSjqBtsB73ZR3PxEvEewXFA2DjHSHOFYGIFxBwh26Q8dFlbfn3gbpLLajiiGjeyFbjNE5b_MKsvwQ0sUBRvneXQGwUYy6KJ_pc_qDr01qLg4zdfS_qLzcxdvTXunLV-c07kj4OcyJuKqvM6VgklCPjfODdjZS0jgeGzHAn5maQ37cr3C_5EQZ-JXbeZTGSn0dhNoKxcSWuwUgUkm0rRf6G9cm01lReupBIBi_RxjhIFeJGhoS6qtr7BsSD0wZXBRbW-KP7V_kiH6wGkL1tq8v3-GW5QDzV9pBb4Z1wKVLr8_3BwaX1XNoS1vRRz_0_7EX5Wmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27539" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27538">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slWUkaCwbiMOIurHia4O9MJxS3-KU1TwFA6iomlg8IInLOpXQBVtr9napuNfqA0-SpIcCU-f7LLGMRHIY66r3b2P_jYuXl-uTERXySctw6DGZQjMt7FWGEkBwJRQ7m57E-07Y69JItsEoViLp2siUwgMfhxv4rcUdgHpn8hbhYcjESL1XZyXeSPbJBXH4TqyTE0Ru7jzVgB8cEAcUwxjbgItuX6rDjnRHXuEf_c5NTxC4sH4OiNft4U8xSV345XK03KvV9I8aCZemflarwyjK_WDysE0UnBKsoPGbnIWEkj7whvNcf5gP2GbSew-BhUK5UE3uhYBjOOvPRJRA9D-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
سه‌روزتاشروع‌لیگ‌برتر
؛نگاهی‌ به‌ ترکیب احتمالی چهار باشگاه بزرگ ایران در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27538" target="_blank">📅 19:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27537">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/be5Hsc0Shr6LsDkYDKZRb5sR-7xB2UDvknYUNRwppykXUCc9itfEqLDannkGt1w8K_6VN_g1TcfYZ3qnr2SvHxElfzh11oKb4lGMIkjva0x31X1k7WZ5MkvLUlqCtJPqwrX4wGCs5bYEXG3INBEt9zZchPBoRPqYu464q67cnf7cu1gzZT_BDST7zj9Bjmkb8EZhVTHEL8At42N9vbDNtdPQxfY0cxr_iPPG8ahcJTF5k5BBmBwuyYv7WEqhISQAM4rEhdufG4rUHGeVFsjVMG5XK9o9qCosELhV40Up4oUeuZn0TXGwneklbkBs-91OLwlsJSsEXFcDmklrLYCqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
آنتونیو گالیاردی مربی‌جوان‌ایتالیایی‌که چند هفته ای دستیار امیر قلعه نویی در تیم ایران بود به عنوان دستیار روبرتو مانچینی درتیم‌ملی‌ایتالیاانتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27537" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27536">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=soPKPp62F8bGRkA0kwfoq3rPLazjxGp810UjgCgAfRqjNJ9OPy_8vdFv-n4bl4M1mpB3YVnyf8EZeouIBhe4PRFOGRg7K4RYGp19vVi1OwDwEzr28dELgvvyP2USfWxSJbDj2nOgE7Idn6CTEOZsGlxuLGfsOJq3jUQ9-OD9qr0o_h1Bvxi1kdxDkTIlUUKsjpKPsrcfeMG8eB_Sl-tLy864H2fNbYbp7WxIZ8HD1Z1MDtfEuYs17arvrSIq4cbS2MXutfR5zZx8Etn0U6GiwzBhIyI7wJE2_f8XbOi3dU5Ac40tiM-RL6kZ7ZIKQpYnD2MaOVPxI_TJ8lOz4rXMpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=soPKPp62F8bGRkA0kwfoq3rPLazjxGp810UjgCgAfRqjNJ9OPy_8vdFv-n4bl4M1mpB3YVnyf8EZeouIBhe4PRFOGRg7K4RYGp19vVi1OwDwEzr28dELgvvyP2USfWxSJbDj2nOgE7Idn6CTEOZsGlxuLGfsOJq3jUQ9-OD9qr0o_h1Bvxi1kdxDkTIlUUKsjpKPsrcfeMG8eB_Sl-tLy864H2fNbYbp7WxIZ8HD1Z1MDtfEuYs17arvrSIq4cbS2MXutfR5zZx8Etn0U6GiwzBhIyI7wJE2_f8XbOi3dU5Ac40tiM-RL6kZ7ZIKQpYnD2MaOVPxI_TJ8lOz4rXMpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27536" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27534">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTm7pbjkAUvnOz-wr2Hwh4BMkhNGXD_uHdfVctDdvmGbaXWrgo1tnDH1YisV_e9aMLPaCvP2y3zYgg3-hUZXDiXdf5kczgL3ZHaSLWKeNPapHgAtF5ijztktx6wjTTuzzYv-o57Phrb1bQuKqEJvW1ul3QAKTLEKFxnKe-T4b5QgyT3fZdK5aQxhyoGplhchkwViTlU7g6w710BtzZg2zP7quG3r_piKj97LHC1K8mF0LRSbV9rLYPHSYRnVCyIzMGRrQhKu6nGzJI1Zbbty13NF6WA3VlUHTsDZL4fPdU0ye_8QI6QlGdq25e10e51l0MqtIfQ1HIt3shCoFYHPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27534" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27533">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfAIXmDItsnfFaTL6JiGd3AYSVdNICBOc18eu3EZG5mw0wftxhllCc7Qo6Lr9q-8p7HKcL4CamYskzRj6tdG6Jah4HmgBSfEwPPi7Am2Vc-EbPdv-6XYLJSmSIMm0Jt-oSCInCWQcICGnzV39QjWREJyLaTMVg8hyN3g11Cs6fxAUHuw6pgfX19J6in9MbXt8WnD2VJRbIdO323YpQ-EzE5GaU8MZSUkSCoCd6odAOh9dqUQV1Y6qrTMJI_k78EmGwbMZxQ4BZem1dGPcWtJ_JzXHNdYgS840ZQgcm9Zz5E_bzfP_Vsf75V6_m0Lo3maZHnwgw3gMzIvSDeYo5-cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27533" target="_blank">📅 18:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27532">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgZuShrs8Cmb__A6b71sijbCxXiXGRDmtBGfISXIi-HAUMI4LA9kvS0E25s2XAjU0sNycAr6nGW9V_cvpQNGU74lmhta22YUTonTzLWmRNZZ05kRDszZ_zur8_U8qlyOpztWiCYg_duL37zQ74m8TjiKZsOvcwLiT88q0l0EFloR3KHc1Pl5_oGpXSb9rp_e6NmSNSP1WpHU1DQbsWfvkDSqz1cW110mwII4S1dtyfhhwbq5YqYYMhcM1qwDTVeREU8OGooSZJWyyoF5RU3LCvqtBPNGZjlTmQcxFoZW06lg8r8nSSDZgawqCLemKLOErVwZ08yx7XNcYTy809LGug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا:
به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش گفتم، ازدست‌دادن کسی که دوستش داری میتونه آدم رو کاملاً نابود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27532" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27531">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27531" target="_blank">📅 17:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27530">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ9_MJKek0iQd1S3P_f7DnQ4Wqha4TK-luXiLgbvUHcx2SrUX1d2vm2fwoimYCGK2keD6rygMyg6o8XWXFWq2pRa2J73LqjjBb9tfq8CxK9GoaPzA61T8UXiDtC4VvdZSDxot9LZ58E-EoxjWjia8OJvJ0BpqOCmyXGp8tlEotNuVr60K3YQcWxtdL3he8tXVNCzXkwpSTGTN9TqpGepuDe8rzqbcMAnL2hq7DxgjNxpsnK_9pVeGYgNbjqGyXec0U9I-v6-YmT82QsigeKg-Cf1p33I18x-fCnRRZpwyTKXO3k_cXneft5nHaexYk79VOOa-SmrBBoCTykfqtjP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی برای عقد قراردادی یک ساله با سپاهان به‌توافق‌نهایی‌رسید و اگر اتفاق خاصی رخ ندهد فردا قراردادش رو باطلایی‌پوشان‌امضا خواهد شد. ارزش قرارداد واسعی در سپاهان 10 میلیارد تومان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27530" target="_blank">📅 17:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27529">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSokSsI8zv1_7eqV6SOuKj5U0-cpOZasU-jLy09ffSeJwVMXZMbd6Wye5Du0K93ze2RM24MKYePwGRETs4RXWDt7bYPU1oLFKN0rlChm7ARuRDv86CHDUUvhdj8ohaCVGdyXdC8qjpCsJJBWVssucjv0BJUygZ7mPID9Ba3ACrLUs5ZcDPQ60IlYa5R01ovQQ7WhLqpmeqgGqNYDMhkgbiYtqFe_fFRfjFJh6MaYor6zzRUiJRLALkwIZLtVz2boPD9qb8hwxmE7ZeORV69Z3kNKEJdOiZAQS0hk4WoFw6h6T_JRV2I4u9SsHEXu_2BT99vAzoZsXkzFZEmNSJZ56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27529" target="_blank">📅 17:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27528">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qlva9OA_pL0_v3m2AQygUyPSUGaCnLSOCKb9rQ6svEDQcOj3uaR1LNtaD-gvQanFcpVEPqcanaQx6kUaPWYpn9nMcpnjm7mZExE_hlQeAULGhWzJYdUBjwQdQmSpj615y5YuPrYXEMiLXVt7nOJnFsv_59Vq_E788JcVOXnVXLgT09ziL2ojLXcHKZD-ts9mI1P47zGU1aJj4gxa1iy9IAQ9MaoJFn6D3QIihMnGtERpop2ejdDsbCAUohx69uEL5nCBdZnsUSK9M9W705mtjQj0K-HvXf30o5aq5_Ra4YBUBwQ87gLwqf6_tseXjofCBESDz-DfyPLFNmZ2JbQ78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔵
بیانیه حسین زاده رییس هیات مدیره هلدینگ خلیج‌فارس خطاب‌به‌هوادران استقلال: استقلال تحت حمایت کامل مالی هلدینگ خلیج فارسه. در نیم فصل و با باز شدن پنجره قطعا تیم رو تقویت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27528" target="_blank">📅 17:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27527">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOCgm95zOg9bibkQp_3M-SwcmNNFBnCuZ73RHVTusT6BozYRDRIG73VDVTXHeu11jPghIioJ-whHJDHPkPbgv4fZhFxnvhqYhRlp51BVF8pS0xroh_lF93OZ_P3shepQHbfjRHEuEaxbnlJ3Ie0rg_FXSBOH2FNF90Gc285d_G4WvO7_d9uZH3ibFJ1JMPmaFB2fpl-wvnzFKWAvrKpLRmBajGm7n61dE_erLrJ9TJIgl4Urcxm5_hoYnbQ5HlgFn1fdzF4Bn1Dnc6MrPL5Ku4aRVT_T-pEm7WohMmDVZTtc8sAqUSjj3hNxNPO5-we8W0-ejADRzI63tm01OLphFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌های انجام شده مشخص شد؛
باشگاه‌جنوا ایتالیا باارسال‌آفری 1.2 میلیون یورویی خواستار جذب آریا یوسفی ستاره 24 ساله سپاهان شده و این آفر روی میز مدیران این باشگاه است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27527" target="_blank">📅 17:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27526">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fY7PL5J5aS7DrOG9KLioEvugw8k86CLg-eabQVM-8A9R7qZMX31-bkkFTZpWYtbXrP_FF0WaEIZGeSfYjwgkoBBRU7bIVMgaO7lcg17vH8la418-bTFCExdsyj4_tKUT72WZbmGtOrDkMyjgQXj6bKhyeA6kTDnT0o5eIvERuW7U6RzbDId8hBQmFr4JwtaxDaBRBMfFAvk36FLK4FYaQy_eYu0U2Vww5mV8FNIDsqAlzyhSdtcUmpiRloCSwc6XE-gncz1ADVLGhcp_1OzLm4VPPy3lz87xKb60T6Y2Re4aQgqozS5RzfICcONDJekjxHyD2elR7UHtSq1TtPBZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇪
#تکمیلی؛روملو لوکاکو مهاجم 33 ساله سابق منچستریونایتد و اینترمیلان با عقدقراردادی دو ساله‌ به‌ارزش‌هفت میلیون یورو به فنرباغچه ترکیه پیوست و شاگرد اسماعیل کارتال دراین تیم شد. کارتال دست گذاشته رو هر بازیکنی مدیریت فنرباغچه نه نگفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27526" target="_blank">📅 16:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27525">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=e8MSymoO4bajV7y1WkNDvqzDsIiSgIrWdCd4pbG5yjBh_CQkFtUHvcpeDhRa4N-YOkQNpyxeq9stHXYvXnVqUvX70uf660uH_CekWHDRISd78TB2MXAXVQJIlrY-M7oq9eeCCCNjn_iUIPHROD3O_eR_N8nTKIK2U10e0DrM47Yogda9gLlVUNxpu_EtS-yr84cxegA9Vs2xpg70B2ch4DOSH0GD1dD7J_b6cj6llUbr5g8Yl4D8qdp6ctEj2I38tpjRsN5KuU5v_5jX9KwnatPnCOmWqMoDrfr82LU5xkI1SplDmjQzkuACl6dloHtosYnuQMwQstnrOELKSPG95g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=e8MSymoO4bajV7y1WkNDvqzDsIiSgIrWdCd4pbG5yjBh_CQkFtUHvcpeDhRa4N-YOkQNpyxeq9stHXYvXnVqUvX70uf660uH_CekWHDRISd78TB2MXAXVQJIlrY-M7oq9eeCCCNjn_iUIPHROD3O_eR_N8nTKIK2U10e0DrM47Yogda9gLlVUNxpu_EtS-yr84cxegA9Vs2xpg70B2ch4DOSH0GD1dD7J_b6cj6llUbr5g8Yl4D8qdp6ctEj2I38tpjRsN5KuU5v_5jX9KwnatPnCOmWqMoDrfr82LU5xkI1SplDmjQzkuACl6dloHtosYnuQMwQstnrOELKSPG95g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دخترخانوم‌رضارشیدپور مجری‌سابق‌ برنامه حالا خورشید شبکه سه به این شکل که در ویدیو میبینید پدرش رو به مناسبت روز تولدش سورپرایز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27525" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27524">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAZjM89cA3qlYjcIqom_GDvnnrWWoBBngxz7qybnpwVM4DJiAZwD0Mt_3pFC6GMQlGypzsjDf1HAXUSkhPe6-wOFJgsHJWpp0QaABO1dFERr9C2X7RV6Y_j-BYnSJ9TH-slQd5XC7wdzMKF4PBQ0zEBLSkmhqYXUxHz5P4p3ZYJS7bodT_siqfff0OWfe_byX4p4YqCHiO1R4BYktTBpVvva2HKV-hoNjyPDXexxeqBDB0K13E4WGyBbt39a0yxjN0JY1uO59fzcJiTdF998XljfW2BdgWnSNRwpzZuTfZyQ0f3t9kb2l5ibbxz6Bpyqrv21Q4sMdMzO78bQXrybJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27524" target="_blank">📅 15:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27523">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
بااختلاف‌بهترین‌ویدیووترولی‌که‌میتونیداز دعوای علی دایی و کاشانی تو برنامه نود ببینید؛ شاهکاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27523" target="_blank">📅 15:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27522">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAiuj-GFUSQ4EY3GRMDCF0y8et4HHXBLwo65bp9FLQY5JuQK3ih1bppsKsfeq3_LqdlyF9zOtIpDnkITCM1AzDeSmKJrQ93dyIaXA5JpPT6NmrmitJE7jARdiTe7242LUZhvIr5QV_CNTiZCDJ_q5gKz3fMtfOB3B1AweCW9_r4LlkPurqdNosnmh69guosEXmWJjOwSjiFKR7FRR62MvLJCMHNJMMbbG1KE3AYTBVS6hzCoDcFn0X6KG5lkRaraREkeGaaSNoD1STSVF9RBS0WcjIZ20et-VlMXHU3TXUeLrUs8F25iP34wqhGJFdCR-Pw0nD7LGpTMYHJR1YzFKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
وینیسیوس جونیور بعد از 9 فصل حضور در تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27522" target="_blank">📅 15:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27521">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DO8e2-CRsJFehYjxPWNCAAluyEePtRj3goPWHSNO1OBRZXk-RU2UOHx6yK7k_8Fv1318PiOouIwCkLtYNoBYbAhJ88dNHeVxjfHWdbGEE0w9LoW0EZknujLzy53sQW5ZtMR3VIjfBcXrMMqddjvq6csGouPrnnhQ75H51ECHw1WKOn4jw8C3e0BK4azyIz96LDBkZ3vhAdKyFTO51p5GR9Anu2lAvY-Q9MrUeqFVtbcOI_vNMfaPJHFMJtezXPIFN521OdRLz1_1XrIZ3FGQAWltfxItnnYDY0i72rzKB1_1rL3xU7lZmwMUUGfAyuSQY7O2Ly2nrQSs-6LHxwaQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27521" target="_blank">📅 14:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27520">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ws9Rj5PJF4W26tFiiwOROZ39gy3xgASGemejCsw8KqtcOWTgSK49U1m_xLfF2ry2rDH7ZFZrdFTJZ5D86YuX_Gm6S4k2wYbt5dJWKmRHWy8Tpj_xvL1bf_Lc3rDUFLbco5PaC3GxyCZPxo7RCRlMjm5p9Fk6x7d3nJfg9tH5teuGAHhu31GFShAhUDM1PQxpvIhDTYCkk2TTUrKbuudBfGIchNyhaOcVnq1SBZceRYdfMoCwX6R7Sm5eY8zTgDrzgtwRXh_J6zU-WG6t0rDJ79lVyXXCC-4yCpmcgVUfMGFD7xc6GiEzj--EFDurvxowwQLFHyFH6TAtNyZozolQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال تنها 10 روز فرصت داره تا طلب پنجاه هزار دلاری زیلیکیچ وینگر سابق خود که یک دقیقه هم برای آبی‌‌ها بازی نکرد و احمد شهریاری اون رو به استقلال اورد پرداخت‌کنه درغیر اینصورت آبی‌ها از چهار پنجره پیش‌رو نیز محروم خواهند کرد. پرونده های ساپینتو،…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27520" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27519">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=GjwbYQizzQ0T1VKQ38C2sR8eV_yS3Brm5le-QJUVRwuqXOBsaz8zEPqF11kILF7Y_udzJxmKzLy2vICktxff4JOYb72P02vLzh0fp3XO6A3e1521kpgweNukpE40XzFWvJvejLbhL25_jvzQ7cZ8hIVmQIeKV24IEFYPb5Y-yd-CBQl_TlrRdPg-ngJrQcGdX9vl05XNj90Fau7fPR6YsdXNMGx03eJRq6gxSW0ohnV42RU7vMmlyDCTKuwsQruciYpzmVQ9PGjHNNXX9TSz7ue1KSvbJJV6BCyCuHOhsjbKZBRqHcMmdzjwYsBqEpaE1LjTR4EHwux8dsHYXe-cHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=GjwbYQizzQ0T1VKQ38C2sR8eV_yS3Brm5le-QJUVRwuqXOBsaz8zEPqF11kILF7Y_udzJxmKzLy2vICktxff4JOYb72P02vLzh0fp3XO6A3e1521kpgweNukpE40XzFWvJvejLbhL25_jvzQ7cZ8hIVmQIeKV24IEFYPb5Y-yd-CBQl_TlrRdPg-ngJrQcGdX9vl05XNj90Fau7fPR6YsdXNMGx03eJRq6gxSW0ohnV42RU7vMmlyDCTKuwsQruciYpzmVQ9PGjHNNXX9TSz7ue1KSvbJJV6BCyCuHOhsjbKZBRqHcMmdzjwYsBqEpaE1LjTR4EHwux8dsHYXe-cHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twO7coeGHeDRLGKnTw73j0Hb_aKlgdykTdDAW3BS0SchvtG6kVNeY68jsDpKenJ4xW_S8nniUsPOfBC_sDK1RYYa5T-e3S4TiucBpsD234TR8ITgvJcSTqg4nT518IviWM4J034SLTZPGDAF2cNVyIyJglQdYw7VaU6M6ui0KpeaUeIdU8yNgj2kAGw_oE-EV4CIs9UTurvmfuLPxNnuQwl8_qvO6ZUYZyWJiMz79AHfmK0Y3HeHTp1PRCNKWRTFxlmqL4v0miZRR8dJgK40nmsQcwv_xQkL_LVkCEjoCqxhr1RNa5KuJoyLoePiCaoKtxmVqjNf3eMvDM4Dd9difg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27518" target="_blank">📅 13:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27517">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPE8AdFP2dHg4eA0mAiBnq1E03bhk-wo4tkzVOuRXXvCW53x12M9ApJsFWyhwZx16pBmqNvDroTpUBqaUdihPffuLdcemA3IFSgS29DbGGbAuPeEelxCrUqMKqLaR2mmzZvaIcJIDGEg_AztlZ8mQ6mzhDQZhmEYdgo9okuXV-LQLHltYFWJtcSSaYX4xkzATbQrZcgeeWdljBSsWxl6vNSS4_NcBFhOZSR3A_EawfZ5HwSpQQih87NorEmRDYzVTzDBUjPz_WfACeLDRJ9YM6kLVs_tnwWYsJYb_u9Vu3w43QXGPQdS5tFlBibQ9JPAYbL90HEReqUoeZcaBVpn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
مورد جالب دروازه‌بان سامورائی‌ها؛ سوزوکی دروازه‌بان تیم‌ملی‌ژاپن‌پدربزرگش نیجریه‌ایه، پدرش غناییه، مادرش کلمبیاییه، تو آمریکا متولد شده، تو پارمای ایتالیا بازی میکنه، تیم ملیش هم ژاپن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27517" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27516">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27516" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27515">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eu0QZ7QZDCoqQY53HeCLqYcnsBMvjnW5jOWIKo1W-C_7lc1XrY9MIoOAUM7_TNhto5nqXUcz7KureqpWI4_yQt8ZYspbjsZnfeahzsHqENQWdprwxi7rf9wPgQJDYvJUPm7tDcLSt95rBBJr3to4kqekZzM5k_W25YzpFNCsPnnT4NhEZW7u5i_S6WGbGbI2GQ7GLzO4QnVg3fs0LK6RDp___VQTBl0GTMclM16S4ue1Cgd4YcvV9JzRBa7oh82uQuL6_17KWbfLPWi7587W1iyJxkx2II6w2wY8W6uww4PP6Mg4NIXwROqjvv8gGzij3sWn_pGMBqZqU3vQ5IZWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🇧🇪
باشگاه‌‌فنرباغچه که سرمربی‌آن اسماعیل کارتال سرمربی‌سابق پرسپولیسه برای عقد قراردادی سه ساله با روملو لوکاکو به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27515" target="_blank">📅 12:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGDSga2-IoTiv1MxIothrrhfmwo6ThDSXVM6alkpq5VBIz8c7mhkbJ5blj3n6yETyWChXaH3TOsS_DFlX4X2_k2tCQCeKI8o2UNjBIiKYTWTpd7q5mxCMVMzgK_jWzNdkLq5vvkxqzIXbcGJJFN16rZYvY6-VGwp1JMvf7iNVhWjcU-uwkePh42Zs_B2yy_5WOLVghTeaOuuZEC9owOYlsG69DZAZz_a2OHSmVbZjNK1TpvSsfq8Z3uy70xbnh16Ls3Sc0ibNMsli3jqeAkuzr8gNHP9H9X0d5uwvOy3L9cz2zZ0vnu6MvDFqhqbSneWXnRrKcASz32E7SBawjf2WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27514" target="_blank">📅 12:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27513">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwYetD5MlN_TlHntPXcu3M_ps2euprsagbTGkwAGT_nFVlF8mSodmsuILDZ9f6lUrnXXl4Vz1iG8A65d7Z4aiJanjGzZAHlTOU3u_wmeWUBJYrS7QcmSr3KNyfcuGFvpu4oihiODxiWTtDG6c3PXPTLmDuk_Rl6Atoe7bLhoqjdcmfV2p6jHOy7w7uo5Vmh70OzTSjPzQKHk68L8IpWvEAxYr6REKqh7YdMLF9BA9JGX3mc-UjN-sEHtI7vk3ldQUQlKLhttn6pkLqdvM6pZphjQ6BH4ns62zYNL0j2_LBVLMoEW272VRfT1dApEuNl_6TPuqVxZF_W-dymRSVuNUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
باشگاه المپیاکوس ظرف 48 ساعت آینده با مهدی‌طارمی و مدیربرنامه‌هاش جلسه‌ای مهم برگزار خواهد کرد تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27513" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27512">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdb0u7aqznUXetvl2IUa1nN5ry_8MNAkHvoiN_AjiSmMhCJcTfdueHrV-WXlCN29W3ZhVnRkUBpZ9x55KV7yYT4pqF6o0Zh4A2XzwL8EQHQKTDXgkF_QmHjJmz13y-P3kg8q7dLfEm5j37ZPXQuC3GH571pa5ws3J9rQQkgMyGE3qgu7_dPMJPHI-Qg_yu_DQrm8Kx-8nYHxcdVv8cfjg-88fVkoHwNM1YZHFYEA9Z7ByUTinCBq2PbzoWdMle5seqvCwRySqUNwFOUJHnu_5D6Wun0FOQq5I6IpNaE25eN1FrUG5041Mhj6sqdfC2j1Bc62r3eEXxMek_bZjIiCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
رامین رضاییان فوق‌ستاره‌فوتبال‌ایران امشب ابتدا به‌این‌شکل‌وارد برنامه فوتبال‌برتر شد که یکی از دکمه‌‌‌های پیراهن بازبود که با تذکر عجیب اتاق فرمان مجبور به‌بسته‌شدن دکمه پیراهن شد. داشتیم تحریک میشدیم که خیلی سریع دگمه لباس رامین رو بستن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27512" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27511">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=nXbZJl_5OfIhIuwkT9pOeGG6WNtTTJDOMzMO8AvggcNs51lP-zx-1vZ3Z7arCma80JmfQazruylzE6uKeCcXiQJZFIjNcVC48_t2K9_nkCG_nGR7EICk_gOTj1h9aoTxuzG9iiyPijH3lrVOOFuK0Csr0xtNlNiAjhvEhfA3zUX7f8bfIUEeaTP4xXurvB5U2GLeTLm_0mdJWkIdpsz6qixW0mSd4y2ouDeJeJENA2_TuCsiSrbuTrtak3Niie9r5JR_OAieqZJmQO-sUVvHjP6oyrwLrAskou76Og-DVIcE7xMrWqJ8lNn15l62yIxBtcT9eyh_Bo1dQqnQo44E53gwHrw04aPl43v2iGH7sshQXOJZUKy_PNGUq0-iCAMi7zFBO5xjUUs9IY-Yw1PMyLkP8dJAzo0q-OValKpKfVQy656hmRrH8WWjn5OKvkbTLkLyQLOG0qpKQEsPlhUAUwhTTShCUV-w1o6zYohvywi3v55isze8G-kdzvmbewuLhKS2v0CQNTOjDKieGvtJyxvc-Zm7PAewfV72HUaJk7PEfXG3tQ457rUWrMB1UqaN0LAH9UTuzqm8D3VTJnsdVbR6FeHUH0xH8vwlurll4sxa7lp5UWCyYqQWvngtOhp9EnSabssuKIKpe3IBRm8OXMUPpL-HsuuDi6teWlWjqPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=nXbZJl_5OfIhIuwkT9pOeGG6WNtTTJDOMzMO8AvggcNs51lP-zx-1vZ3Z7arCma80JmfQazruylzE6uKeCcXiQJZFIjNcVC48_t2K9_nkCG_nGR7EICk_gOTj1h9aoTxuzG9iiyPijH3lrVOOFuK0Csr0xtNlNiAjhvEhfA3zUX7f8bfIUEeaTP4xXurvB5U2GLeTLm_0mdJWkIdpsz6qixW0mSd4y2ouDeJeJENA2_TuCsiSrbuTrtak3Niie9r5JR_OAieqZJmQO-sUVvHjP6oyrwLrAskou76Og-DVIcE7xMrWqJ8lNn15l62yIxBtcT9eyh_Bo1dQqnQo44E53gwHrw04aPl43v2iGH7sshQXOJZUKy_PNGUq0-iCAMi7zFBO5xjUUs9IY-Yw1PMyLkP8dJAzo0q-OValKpKfVQy656hmRrH8WWjn5OKvkbTLkLyQLOG0qpKQEsPlhUAUwhTTShCUV-w1o6zYohvywi3v55isze8G-kdzvmbewuLhKS2v0CQNTOjDKieGvtJyxvc-Zm7PAewfV72HUaJk7PEfXG3tQ457rUWrMB1UqaN0LAH9UTuzqm8D3VTJnsdVbR6FeHUH0xH8vwlurll4sxa7lp5UWCyYqQWvngtOhp9EnSabssuKIKpe3IBRm8OXMUPpL-HsuuDi6teWlWjqPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
5 سال‌پیش درچنین‌روزی؛ لیونل مسی فوق ستاره آرژانتینی درانتقالی‌آزاد و با قراردادی دو ساله ازبارسلونا به پاریسن‌ژرمن پیوست. عملکرد لئو مسی درپاریسن‌ژرمن: 75 بازی، 32 گل‌زده و 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27511" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBX8I7zR9ISnrd8X02eGvaB8geIaPT0YpT5KZFPMJDokbjuNTe8Owgg_zOOksf8X_zaMYkyDjFjCsa-2AP0iumxd3gpxzF0KOrRs8qvaS2WxD7JGx77SGckn03FicnzD92o_vi_kmfpBVdhyjUPMiJWqXFpxYFVSX8aqjsBc13ARYfW2XfHLZoyDwDgLUGxdG6O6JXOGHlKvbCj5NVQcZQF4b6LSm5dE8nGXNmM8zMDFMCxvBlaRMB2TJUEKX3ARik71aWFcmMpTxcJl1Bd9xCvguLrowF-YtQwS47NelLUS5iBvTQ-pfzViz0gRd5t53mxx2bRNdpXBYKW2n_OG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی تا روزچهارشنبه به‌باشگاه پرسپولیس فرصت داده تا رقم رضایت‌نامه دانیال ایری رو پرداخت کند. درصورتی‌ که ظرف این 48 ساعت مبلغ 120 میلیارد تومان به حساب‌باشگاه‌نساجی واریز نشود این انتقال منتفی خواهدشد و این‌جابجایی…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27509" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRDko6X1LfIgRG5mOKQR6TfUm8FOvuR4PJiuEZ5XOu2dt1HKiGLbx8FB9ThjXSJpKrS8H0t-HekBnyoRVxTDfm_-qswOxRSLrCCAsmigxSZWx_ttM5etNX9CwsBcZ0EBgYRLF_TrLhIuVk5bRVFVNq7v8uFDcmw867gl1gnVqcqYkFEHY6fEJIjs1S5z22Cf1i0Ky-2VbEeqtZ9c5e9qPV-iFUfn1QSg1QCDozKBPzPqRxvPN3R0riv4g9k2PhjYvvENTb-qv0dhjXgZKXUi-DnLHBoDFY4GDpdyA62JF5WpO-A91hBlgHvX713CsuIVLoLJLH4oQZ-PiTGtYt-Y3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مسئولان تیم نساجی: دلیل نهایی نشدن انتقال دانیال ایری به‌پرسپولیس‌کوتاهی مدیریت این باشگاه است. برای چندمین بار با ما تماس گرفتند و برای پرداخت رضایت‌نامه 120 میلیارد تومانی ایری اعلام امادگی کردند اما موقع پرداخت تعلل میکنند. بانک شهر و مدیریت‌باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27508" target="_blank">📅 10:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=VKKWM24DllJp-WtCW37cTN1jlI_71IAGTPidLy17ZYLNEAR6Jsg3gOC5Ja3dE9UOXMzGIxoheHQBu96N5nI-04fKs5YH0wGBqtirpAY3AILhePysesc2L2gkRVtqgJgEgIJYJlv4gha-Sb8Cd3kZjUAGAuy9RO8TYucs1Oc05eddaoCiFNor43RoJmxS5REllJFgRaT3xT3InBsrMKZtmmw49SufcPL5sQtNs0kb1fSRHXR73t9cR_RNQz12BeVUYFKLfEJu43bA-rSYrimAg-LX3sD-WoRUZnbMMWlwdMuDjjxaEQHjcoG3PpS4UwHHB6xIjGciI5SKChPcaudEdoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=VKKWM24DllJp-WtCW37cTN1jlI_71IAGTPidLy17ZYLNEAR6Jsg3gOC5Ja3dE9UOXMzGIxoheHQBu96N5nI-04fKs5YH0wGBqtirpAY3AILhePysesc2L2gkRVtqgJgEgIJYJlv4gha-Sb8Cd3kZjUAGAuy9RO8TYucs1Oc05eddaoCiFNor43RoJmxS5REllJFgRaT3xT3InBsrMKZtmmw49SufcPL5sQtNs0kb1fSRHXR73t9cR_RNQz12BeVUYFKLfEJu43bA-rSYrimAg-LX3sD-WoRUZnbMMWlwdMuDjjxaEQHjcoG3PpS4UwHHB6xIjGciI5SKChPcaudEdoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شماره تمام بازیکنان رئال مادرید در فصل جدید رقابت‌ها مشخص شد؛ دیومانده 25، اندریک 9.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27507" target="_blank">📅 10:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZt_UjUg1e8KV17Lg-grM9baNPEktGVMARzG6JoflEzcFtWPzp5RqRm3VrMWu0Lz-h7oOne5XTctNDgXk3ndK0VBAuF0qRHn2vZyXp2q4dfZ7WS6ubSlZ5_xXSJ8SRu9RuGIHU3o17JLU0TT2xNH2X8U1u_m9nvx2PsKpOK8oazHCcJ8bY7sJa2_pykJmwBMCKeuIjQbS5GBhY6BuSJPI2t21uJZDj3AvXW4qBKsSkM3C5VkgH1zAfehqYscMuHJLOqpZzAzeSd15yTtUHcWplPKsrCV8hsdWAqIPiOO32N-FzGslHs0ulYQarjhXHk2Znv7GJ-8nL_BBjbeu3pFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته اول لیگ:
موعود داور دیدار استقلال شد. بیژن هم قاضی دیدار پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27506" target="_blank">📅 09:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqCOTkI1bn9ka08zSIwUR0W33eGrdMDmzaIfQFyLjj3t5_zE8Oq9l1QeXUtsQc2typI92fafRcSs-SVAhkcxzfhvzLBgRmCpi6XAteHxCWRPOPXgao7pBehPx3OsCGEjgCgZ8OIGFovd5DYMrNyd7BYgyF4az7QylJjTzd6A38aY6xLsK5_eG0Wh9tBzfTzZLtB2xCvMatoRG-J3LKLfQTOs1JGc4Z697jZpnaWPvaT09gA9jLbMJAMRgOloHXThxqTdEo0l3RTStIw6DXKGzMXxS_zfyzvMTeuS7lNwvmOCTpnPODQVoDbNnVQ9OlolgAc72fEnERk4itTPH8br7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
مهدی طارمی بازهم‌ازلیست المپیاکوس یونان خط خورد تا در آستانه جدایی از این تیم قرار بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27505" target="_blank">📅 09:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=kr9eNKbtbNJO_qV3urPyCOMPWx9mnqGKOkCMtgL4hrqWUXkrFxHVIjCoh4NiEjg-2i75dgGi5X4GmzCYKF1vZjrSXwW1c77IogVyLmorWieJPIk8BNiEJ0LouQN97MMTmBAl_uY8tp1WyqIE57iBYEfFuLyV1qc0uMDBuq9f3-Jn2SrcVHi0xe0Ql4hx0nTTW_GCLyGdnuD2KK816aQkALBekbqc6DQE5XRxxchLSrG_PMsG7vmZcpBXDgoBxeLSlURsWsczXBk7Cqy_20DPFnxOPqC53kTnbQ_s38DKW4mlVclwMJwu1jP-EM2AV3oEaxTCvnCy1nKU4ghf1x42Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=kr9eNKbtbNJO_qV3urPyCOMPWx9mnqGKOkCMtgL4hrqWUXkrFxHVIjCoh4NiEjg-2i75dgGi5X4GmzCYKF1vZjrSXwW1c77IogVyLmorWieJPIk8BNiEJ0LouQN97MMTmBAl_uY8tp1WyqIE57iBYEfFuLyV1qc0uMDBuq9f3-Jn2SrcVHi0xe0Ql4hx0nTTW_GCLyGdnuD2KK816aQkALBekbqc6DQE5XRxxchLSrG_PMsG7vmZcpBXDgoBxeLSlURsWsczXBk7Cqy_20DPFnxOPqC53kTnbQ_s38DKW4mlVclwMJwu1jP-EM2AV3oEaxTCvnCy1nKU4ghf1x42Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسه‌درامدبرخی‌ازشغل‌هادرمملکت؛قلعه نویی یه‌زمانی حرف خوبی زد گفت 40 ساله هیچ عدالتی تو این مملکت نبوده از این به بعدم نخواهیم دید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27504" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFEiyYIhHeGRcBnO_MX70Nv1Q9wqxZUY0zPQNXBfK4VWlf1BPjHczki56qjbUEEBaVgvXVQRAbWyDvO_FCBOlT8MnOY0gHClI2h4AhizIAa55lhEt8VwrIrPB4IVTZkzfc7VbM-N5JpfdDsI4yZwO0SkvUk3bB1kv_Eh3N3qUKSAIzRoNqQKJLbKAyG1-9M1PjM6Hb0QqzqQf8YhqVyDQx0vjuczlWc-9Hs3LUhJiGFGhoQr8n0-jSo6nOJolfkBql8UGeWtpe8gbWz73nEXG30mXwi5o0-u1M1dwpXQEADVWjibpwEiR9kvAJmshGFZyqHB3_RvIbOzpZC7Xs36KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الکسیس سانچز ستاره شیلیایی سابق آرسنال و بارسلونا: من‌درجریان‌اعتراضات مردم ایران علیه حکومت کشورشون هستم. میخواهم به مردم ایران بگویم که جهان صدای شما رو شنیده است و قطعا پیروزی نهایی از آن مردم مظلوم ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27503" target="_blank">📅 02:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=t6SHctP6Ik-Rmb2M28_Tl16TH8WopdA3ZF9gca2ppxIRCAnsvnloAzkkjfACYsj-g6h3qm3lap6KZVvfPpfobl41SvTNKR2Ig4VLY_IwmGjLo7Exe0xxcQko0Xq__lc9zWLaTDQGKZ-UTLQaYh01x6rn_M05vgnaguIQt6sWQolRH4nRK3rlvdYRQqy-eosx4DF9oMJFLhztJfZsHXRrnNKr7Ge_d5DZdER96qRuQnHcfovriwn22ouZIpXIagCTboJRwofUzSh5I-gCBtZ6ho_I6eRAmrBq7W71o6jKcTiPdReAXiwzQXX2PN4Wn3YFA6abGJhCYOfQI5IVapiBXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=t6SHctP6Ik-Rmb2M28_Tl16TH8WopdA3ZF9gca2ppxIRCAnsvnloAzkkjfACYsj-g6h3qm3lap6KZVvfPpfobl41SvTNKR2Ig4VLY_IwmGjLo7Exe0xxcQko0Xq__lc9zWLaTDQGKZ-UTLQaYh01x6rn_M05vgnaguIQt6sWQolRH4nRK3rlvdYRQqy-eosx4DF9oMJFLhztJfZsHXRrnNKr7Ge_d5DZdER96qRuQnHcfovriwn22ouZIpXIagCTboJRwofUzSh5I-gCBtZ6ho_I6eRAmrBq7W71o6jKcTiPdReAXiwzQXX2PN4Wn3YFA6abGJhCYOfQI5IVapiBXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلندشدن رامین‌رضاییان‌از روی‌صندلی روی آنتن زنده: بخدا منم‌فقروبدبختی رو یه روزی کشیدم. الانم نه ساعت دستم کردم نه گردنبند گردنمه. همه لباسامم ایرانیه و معمولیه. از مسئولین میخوام هوای مردم رو داشته باشند که با این فوتبال "تیم ملی" آشتی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27502" target="_blank">📅 02:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7ylYrCq0HoyrwGQyiGKURUfRvMPtp96YqC1V7qiDwaWY4S2QZPQCya7HNFQgUGKB9p5XNFzgSdab2ljjmk3mrPyzlJp3yI8QOqGTr2cX3e_0MQdC7-nIP6JbPkObc7Yxm5qEONaQGpC0VYhGO7F-4cCurBhKkTOdJkuV6iUBT4db3ioEj1Y7gENaxS8j3ocZQ36vvZsW9rRelA5_u6bHMBw3tEe6gZIUsMyL-MgmrbZEJEpJo7jYKCwHQtBhCyTA7VRyX0-5CNRNXeTnoOrrzkB3GtmEHb6ojzgzYKxapqrmRAzlwqdQl5wA8wPzQmTMLssMFl5PExD7P49r7nvDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
روزنامه AS: با صلاح دید ژوزه مورینیو اندریک مهاجم‌برزیلی رئال‌مادرید در این تیم موندنی شد و شماره9کهکشانی‌ها درفصل جدید برتن خواهد داشت. آلونسو بشدت علاقمند بود اندریک رو برای چلسی به خدمت بگیره که مورینیو مخالفت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27501" target="_blank">📅 02:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27500">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27500" target="_blank">📅 01:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27498">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=L8-J1yLm2ucBVrRtE7P-JXsLLqwzPCljIwlbg6wE0Q1IdnXjR8gKvQSZpJC2e-xkaUlO8fk83xVEH1Y1ou_fwJUgQb0gtgunVOp7f-91TdQLynuun77IZHJzYV5Uz1WXtbIjrFbAULOhhdn-9Jdwfv1ASQXuCSUQOPHOGQpVMTPokPBGukQnYVdtFZ4wyF9lAkSiANV_9Y1ZYfK3RmMW80XUCwlUczIw-BuxYXBXUfEyqhVehBGIxTlWPdj0EL2skCpUI5OcJhaeM7KdYJ7cU0DDt8jnevCrPk0kJ6ROpfGbxCZXj7wMxLruulNG94VmmXvFzLzc_phTy6LObgZvdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=L8-J1yLm2ucBVrRtE7P-JXsLLqwzPCljIwlbg6wE0Q1IdnXjR8gKvQSZpJC2e-xkaUlO8fk83xVEH1Y1ou_fwJUgQb0gtgunVOp7f-91TdQLynuun77IZHJzYV5Uz1WXtbIjrFbAULOhhdn-9Jdwfv1ASQXuCSUQOPHOGQpVMTPokPBGukQnYVdtFZ4wyF9lAkSiANV_9Y1ZYfK3RmMW80XUCwlUczIw-BuxYXBXUfEyqhVehBGIxTlWPdj0EL2skCpUI5OcJhaeM7KdYJ7cU0DDt8jnevCrPk0kJ6ROpfGbxCZXj7wMxLruulNG94VmmXvFzLzc_phTy6LObgZvdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
با اعلام باشگاه آژاکس؛ مارک آندره‌ ترشتگن گلر 34 ساله بارسا با قراردادی قرضی یکساله به این تیم پیوست.ترشتگن‌اول ناراضی‌بود بعد راضیش کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27498" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27497">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOBY6zZc-kWt45kgPiYZo0Vcu2flJIkUxzYECB9YBETrhpImxlr-PF1Og2nyu1qfj2iv1Pbovp29WNdKDD-zbh__wbIjhLNvMNrbyYmrpDHWtG_g2-fa5zlMMpfp38K78Ax60tRC3dye-xFj5UXoQFZf2kVbv_0g54F0ietPwVvPq0lcm1XlaZ50GdM5U0gxiSP9em8zzndTGUAVY4l-TxK9Y9tmjOmnUItL-_t8tclKQBWlFZITes26hlQPzNIfOAXGe7uAMuaziepMLCzxDo5TpGRnGHKBVAhHqUFdxTcosTa8liR5kFI_rxgsXUL4WxmTCN2BtU8Zh7auYL6q7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌ امروز؛
از بازی دوستانه یووه با پالرمو تا بازی پلی‌اف لیگ نخبگان و چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27497" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c2114992.mp4?token=u947T9sr0w0WY3BVS0VtaZr9pdEo_J6LiSSDi1onjzYsjH2HjkXNSwWJ_m5V0d0AfQwqwVrl4NwSr8ppYvbl2iEXwS7LMfb-eEg3bTfcwpESlpvGdG5yTwWV-szdrk4Xn8irchSVpkWZBGU5jUjhfxG2vDhxabT022co1WEBYI3FTKorbtmSFsYOxtoi2ajkpQveYr5jtvmDEN2lcbXOgNrtS58rclprOK6gGNONE24nLKs6KmueqKg62ZPd9zmT9kSAhhPGV5EzejNMpWAl2ia8n2e7EQsb3VVtzXvfg3STdvevLJmQGggw6rShT07pnbfre3qCYf6zRZrgjdLVfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c2114992.mp4?token=u947T9sr0w0WY3BVS0VtaZr9pdEo_J6LiSSDi1onjzYsjH2HjkXNSwWJ_m5V0d0AfQwqwVrl4NwSr8ppYvbl2iEXwS7LMfb-eEg3bTfcwpESlpvGdG5yTwWV-szdrk4Xn8irchSVpkWZBGU5jUjhfxG2vDhxabT022co1WEBYI3FTKorbtmSFsYOxtoi2ajkpQveYr5jtvmDEN2lcbXOgNrtS58rclprOK6gGNONE24nLKs6KmueqKg62ZPd9zmT9kSAhhPGV5EzejNMpWAl2ia8n2e7EQsb3VVtzXvfg3STdvevLJmQGggw6rShT07pnbfre3qCYf6zRZrgjdLVfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده:
ما با
پرواز زمینی
اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27495" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27493">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICHVuSIVIsEo5U5SdPlPwKHnVY4lG47sgRxodPsPWXwHMIz-nm-Iw4wHlhrhjyMRLoy3FswbQkPxO2q5Xr3f7ij5hZEY5jxv13JPJmn_Bl2hVHrfXeByJ1jxTuujtSJEKA5IRbbBEBdptpCPsbTWCKoiEQ-EViufc9vEoKbZ4j1wNXkp0akITW1GiqvXItAF54RRZLfVOy62t7JPPz2ZIxIy2yl9husEv8cy72bBpZPA3bKbQ7EiO0J9aCDtirX1PhrsGO4vp-9h-XOI1cCZj7zV5sUbRwMRL0zfxo3YhdQUoDeSs0jY7ZOj0X1v1cjU3WEOLq1D4TP3lWSlKM5PIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رامین رضاییان: قرار شد ۵ تا ۱۰ میلیارد بند فسخ قرارداد من‌باشد امامدیران استقلال به جز علی تاجرنیا گفتندنیازی‌نیست و مبلغ روکردن ۱۰۰ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27493" target="_blank">📅 00:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27492">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ_FxBuxIdhItwqjVWCAMsUWX3ytUhy6Lq0tMiFzbMDV4-FfD7UShmI3KbKeCDOy5Sqxb3eY9D3eOKl23yKWli8zmJPhxkeazaYMcilysnTbgfOE5IF9k_FFm16Q-1z0x4Wedso0anYye12L2t7PILcnkSuJ-iw9w5skzW7UzOM5bCIuWukjgTC0VSRC_vHHfvwWwy0lUODcYJMqzme5_r-JCaWUHyhmGE0K9zxcnN93W-MjrlF_st6z8tNBwSOnbtz4MkvoZgZABHrriPbkE2o74wxBSwh7EFirVfNNbxldb8grtvXb3GsK7H37zFntib-FjfWhJ9hzeyAaUoG8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج‌رئیس‌فدراسیون‌فوتبال:درروزهای آینده جشن برترین‌های فصل گذشته لیگ برتر برگزار میشود و ممکنه جام‌قهرمانی‌لیگ‌برتر به باشگاه استقلال اهدا شود و این تیم رسما قهرمان لیگ معرفی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27492" target="_blank">📅 00:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27491">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLtuKU_CVxrZwQEDiolMiiy5DVWEwRdhxOpiCQpYms7lyhJ7Jc9zYT7s6LO_twixXshDTI_LFzPj0pxPRDFP14lYBXGpH6wXhslrNbqnCmbqqOoOjNIM8DP0vySYYiy-LujTLWkMOe4VPFtO2ZeYe_TfMemGKJsPBhOOsk6f29Cswhc5CbcKfEphvEjHDkZM_mI3lsnbxsqYk2FSjaN5NloYQotGeYTWbiPUvtaPZvaQzYfClluzz3B4pmTQBfvAXxTxi8rh3-uDnopQj256NivTw_GoBocn05lruCHBgTuDJTVza_Pit6imnlyg-dr52V-Q0sK4jPBMgaxvYQMtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27491" target="_blank">📅 00:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27490">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byCF8KIh5R980DD5vYW1uuOM4TYf9pdcGynNWrq6VSyPdI1uGrybHEbbkvoLB0HKTdpTJOonlkJ8JjuBDB-kdbdflzNHgtEcHAn6MW5dYPsgYXJgr3fOwcKurZo1qFZUjtcphiBb_CQ0vLZPG8bz52u_VLyb01UZQsnyBAdYO336WtIGemvS4lINkdBMeYCBaoc2IQYSYzS_CISbGT3l6WjQeuUTa8K7_uMbicdLH2RW1a0GjSykFqAQTrRbgsppzHEsM16tgeOOd_Tcujpxv9YDdkp1dviidPFS0Vk3O8hqt2CUr0nV67O8oQyZmIAW0jifjzB6N8y6Hz5NNBVyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27490" target="_blank">📅 23:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27489">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQxvzQlZW9iSuHsEOc9jmME4tE6ylRVvv53D5puLFUnzWOzfVVMB2cTo_0A9md71N9mr2LfiXwo6x70l2RRI3yYZ5w5nrew8C7pVxywzUsQVL9CspQiZU6CavoYNd8sikYwkr5nqLrEzNRC-XJoVPHcUGiQpGUbzMA8-UagERjr5l2AgPkFgWm2GgnZfhXWooFW0NEJp_oI6dEMYe4S_PDWLwA08JKZgagqk7sGZvTYcxXcugE6BiVHLNnE_r5QzNykDw7W2CPqmdqrz_zJhVUG8Rps6L4cVfP0lePzx118ZtPaBF5BLvk9CjxcOMP7lRDleMwjS92J3q-dJTdsjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سعید مهری هافبک‌سابق‌استقلال و پرسپولیس با عقد قراردادی دو ساله به فجر پیوست. رقم قرارداد مهری برای دو فصل 30 میلیارد تومان ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27489" target="_blank">📅 23:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBNY3sP28u5Iseout1ilYLpPs-zgtLDaGDluvOAtrHY6LUTS1sEIX4k9cyBeQqavQ7y82oHrJa1hVOmHnIfs4TnhNqzirqkK9lPNHEI8BgMpQDJ0EKtuWwpI7kyuDuNNQ3pqRTatgoyiWbrsoHeM4a3_lTIUCUaTbeFvZkoD7lXUltJS5bhsuFm07F_oKw0tg2Iyscb89L-SWA0H-54vcCJopfLM1k7ZjDIFAp3OBDULaENfElwZngLahNoJRlLNi5tJnsdCrBq_lS-GLk8EEqQ-4HkO5EnrZZzys6mnahtvpNcNCmIiwOVF_zAUftFe5UV830jWM3i9_vPZ4eC3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27488" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27487">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb-RtoXcUdsaeonppjLm22rB0JOcku35bC-vFFrL6F5VBw10nZxPE4OOJ3m2flzbxWtBfJqk4qZRsDAW0sW8EizKO-xo540_egdoF_DCeUvjB08M_0s8_KV9Z-2fwTgDkyXtLgMnrSrhKiEh_mNFF1NRw9QPhPmFLiXNmjIxSZ4wat_OYxFy8eWOH744oAb5AthVIe5IFOGcPABS85k1wTr4nz14ZvqpgkkSYXKPZqXVR2y-hNgW5n_Sl3Jvu8HGrsSVElqOHbPgzul5RCgkDHTCA8G8Afrwgp02FTScnEsJcNrZuxumNP2Coz7bFN-Mw2HYJJ1O3AbiiYhn1NpF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27487" target="_blank">📅 23:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27486">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVU4GG2ReEt9MdoFYCZrgoDWx80-R9Vgv7B1JnvOIn17VgPZHQjqzqLU5cOSo457UskRXJu2TqanWAmNvSWauobdGzQtQT-buB6AEjs4uz_s_WbVVfaHEC7eCY-BP-LAQVPDLO0s1bpqY2AFAqmKcyJg-XAMIBHYiYSSXd1VaEcGSDvckMzxOPyRtB_lz-p02lVTBE7ENeCSUqPthteQFwGtc1G-sd08VJFS_bUdw0LdRJT2ZER9GKxee5-JT5bRJu_7kRzQW6trhDVulwFUysbEZeU2AxSFOaMaOCfSKzHb5xjBmcc928GP7uXiuPPUNVTyPob-FvSyIYOr990_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
ژابی آلونسو بعد از اینکه با جذب دنی ولبک و هندرسون تجربه تیمش روبالا برد حالا طبق ادعای اسکای‌اسپورت ازمدیران چلسی خواسته اندریک رو جذب کنن که پرز گفته فقط قرضی بهتون میدمش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27486" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27485">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPm3g_Y8LRCEC9--K2MhE39wqLomh-16LMnnStpU2LlAA2c8GxF2ZgMr4AtgacDO8hlVDT4JALKo4LBSfBfySx8uSkZ7wFnI4zdDxDQ6llubDG7pT4D6xwy30jre-KiuHKzewKKQPSpCs17VfhRAuLlrRAgssbq7piPKLC0fpF-U2pNuV4qfcjplT_719JvwlLUdKbQTltjjFdJw19kss3W7iveLwI9ZDYi56KgmKoOfEaYNj_fgvk07dhj1vhwYy5Z9lLvFzGx6IIi6BicMcCHTcZ_IAJysa5S4gfaNuEbVLHmup41swgfZXrbZcUg34DeNUYhxALCpAW--adcSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌سپاهان‌دقایقی پیش به‌این‌شکل‌از کیت‌های اول و دوم‌خود برای فصل جدید رونمایی کرد. باشگاه پرسپولیس و استقلال هم ظرف 48 ساعت آینده از کیت های جدیدشون رونمایی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27485" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27482">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5jVIyf0vm0tTzK95nhiT8ah0yQNvNBzeiJqeLy9qZbxsUv2yKemjG7x4NU3XugZ-gSX0a6dElW3kY1cNpIoV9hcKomKId80naYARlf2TcTkHCVgGbep0BhjTHVdS00XV-Tx6tBO-oHRejwOBYskPPNY-hB09chTzkF8nVmSinMdX1c3RIQFqy5NixKH9liRUsKmawzqYPXkeRyLTPP3wI7lOVwOBnwPIo2WT6MKaZVS9w0wpx2Pfsk2KBQ21MCah76ah-rBpoVODg8wBu8JOyXnxIc3fvxZgE4WUxGYm8KkwhJOKdw_aFA92UTueXEmY-f6AW4F3zEAxEQhIDw6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EE6gRDIQss5JL8w4bXNmYigEynVHG7t4xzmJiAxPzRIiJ0rghx_B0CSdd1sjNor8r3fPw30ElNkIesbs6L-wOZ1aAuBZKJ1hX8bkHTM_mBEDfHdA8a3VjgibrJxHyE-lk_CUUQYuTJYgWJJxUMOFRnX512U7L5ycp7IUNL0RuufCYoagCe5UrEn8klchnHE6V7oDyBH6NlSihG-9iz_jry5oATA3ONpo-BeFbrZ9eK1L-29ToFs1_xKcE0TxDJNX5oKV2Yt2AGoSFKz6tpWBFiX4lEAQTufpafsSrcxG6Bd9uU-MyfOvMrwVvvtrXDLqPy7WoSQO8eMQCB9WR761GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
پدرو پورو مدافع 26 ساله تیم ملی اسپانیا که بهترین مدافع راست جام جهانی شد اخیرا به این شکل از دوست دخترش خواستگاری کرد و پاسخ مثبت نیز از او گرفت. دوس دخترش سه سال از پدرو پورو اسپانیایی کوچیک تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27482" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27481">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2UONjUVw7gEIUtHy25ilbUmJGSu2VWyN4Ep4S6KNDfDKlJwBvzNnhDo7Vemung56lCvNA_LCMA4vjZvTNncQyMnxPxLCgR990h0bY9jpX_9QPEI9aAYudcrnhyWDxQZQ3D4-j8Kj-b_JYgUtSu8biEujWcjLEz4DHwo9kX5FAvfyBcpx4zA8B7rzt8WI8vjgj-Xjey-tfXhdj8LcS2uxnPirSMgO9fZ0yC4InpaVzmZwG__Z7RrEpp6thx29jWO7YR7B7umcnNAPqvPU6KLNFjqc0od8FtFkoaJ-jUaEWObunn4aKMZhbNupujO0d8G9S_YVVr3E3nCmflzeRFHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27481" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27480">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5VDYniJoD33jJPISJBJREKWt-3WLXuBnkJQoTXj0IEoVazBrN5tFOsxQ7BQcdRYAR_aqg3gmuCkSveS-nWnOzNYLXiRilGdVAbKKXGXZlYa5h3CI5cDOGEqageiDsbJISb82bn_F-go1V7MMroOd8DQBWCz0y9p379xx13YCH72xhko4q1YOiVQ6gOkaSVFBqvgL2HQDatkbbetifc9mMUbcOLBB6QOIbUyu55-NYXzIC2nE2uK2jvJcIbNLo_QX0Ym0SCWg49dby8lBRKQ-ujbY51x66JxCv5imzaVrSseslyILGNbIwtks_2_hwqYinJvfLvD93yFpf3vdhirIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه استقلال؛ استعلام فیفادرخصوص‌قرارداد یاسر آسانی صادر شده و این بازیکن هیچ مشکلی برای همراهی آبی‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27480" target="_blank">📅 21:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27479">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPtoRmJYET4DHKrNHFSey9GUi5l8NYw7lVP0P7Sga--1-Lre6pVTbHt08gb_l2vj_dlWjkXaXeYO_ijRw1nfRTyxgw8bJJE_1cQnNEEjuR8mQle7LNAT0i7SemliIYPKkOW039Q2MVfA9uOiDMrQrxCCd8o8FAHzb8Om3I2_TPyutIbQ2DBOw54az_3ackftetvoNbMGShNt1huZZuEynUB1tKNtLyCs3Wv6F3EScWNHftW0s9zF9LgLJx4cpqlXLPLwrJxNoHu0-eUNiTGapMblzVvkTb5mQD1Ko9DKpzDR6iHtWkLLs7ZBm-nEU8Fq9wELthowm7YLq_NqWUzLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27479" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27478">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBBxIDJgLiuwKTCoKAqr6qOnWzDHuaf2agKSfwQrK5FgpgYyGeCGZWLUGRp0vnC3e8fBLtwVwHHn2bei-m1N2im7_xDmnv6Vxgo7UJT3_Hq5COFhQGvQJc8nK-ZB1_inHDBAJK-z5eHhJw7_X05pb0UtzsHR2VwADwBD76wyVsgypwh3pmwsIgHt6qmf--b2fsvVQRdea_l4R9FtHe_-I7TGAokCoWR4x1G_9rkw9NXxkALBYBAtaEMwqvu3Uko84I_L9j1JYnKNm2iyrHf5209Rh9L132InlgkqQTIVihByumWnKsW7zTZPGrhFttVpj6PJTWlNoIjYhHRXrLcggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27478" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebZEEf5i_yqppDHQoM5XV9kFlZNLlGv4H57ANTJHLRgTcIju1KBhvAPdc-DImRAvq7ouBFHy48ticb2Dlc5sHD6HqIMgK5ciS2yEsugL21PSuDTIWqY3V9qUfct5FTRkbDOGv2Lc9RkX-mxQZ0yrGxgnPDaPxEEW8O5EDLXZt1R-LwIHXUssjUfh08bLDAyCfIQVtkYMy1ciGjNeJBy3xgpRFYEMF2VXs_CMSgwdQhhdFfoZfo08drzUrP9MT3ylVEsNmMvEB7zedZZwASvdCeUSkkId3BMObjYTTR7hiqAmIECQlx6blaKypOXLD_kQUFejZMwo_7obhRD7SeP4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از جوزپه رینا ستاره‌سابق دورتموند که رفت آرمینیابیله‌‌فیلد و ازباشگاه خواست که در طول فصل براش یه خونه خوشکل بسازن، این درخواست رو بیله‌ فیلد قبول کرد و چون رینا توضیح نداده بود که چه خونه‌ای‌میخواسته درپایان فصل باشگاه بهش گفت که خونه‌ت آمادست و با این شاهکار روبرو شد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27476" target="_blank">📅 20:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/luAjsKFmU4v2vPG-y4_XxEr_sofz2-5el92aDDTPb8gMLyykXIRE-be9PzPIJpzLmDH3enKyJkIKHW-pzhDWZyUToTZ5xXo8cObXrW1DyV4ogeEOrKNiHHesSlU5y-_0Q_mF2VfMsWqEKKCiS1uf83GpTOPxKp598f6WrFcg-QPM4uc0cuVgIufUtMPXeHltgolpKKLKR1CoBXT63kpQ0-xCjEp8tE_8hiKIg2ccgVcGOv98UCjmGZFtnomwS_ftFx7m4qivuMGEFcIDK2LHzdTNJTA56qfP0R8p25xm93J9oGv03KCkMpyy8A1EnIzJ1Lg2p9juZpnrpzUS_itXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTQY2sSbk6P2F7VKFkL0XOTB1Xv9T7Y5FMrraz5ogRKfObTnsmISzPxpHJ2TzPICyVW90B1ZNTNwjCRY4kcyDGxxRtl5Z3qFyxFyq66Ru1digLI1SpMhpKz1_3cBAtW9IOY-j7zomrrdsi5C1EMVemKiYS-6rRRhOAEPVSD0VXSjERNTFZusEkpv9ivw4isBzLcfBIaA_2W4ppXkw-wiaqI06a8HF-eviw1NcTBD9yv1YAvqHjhU-ULV6Fjl0dzoqRNEsjX8FF4w6fq07xqPDSE4EaRlejxr0ydZWusf1jxX_mV-dSWyi1Lps-gfYBlpqf43KsLpUhEe8tWODR2xzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27474" target="_blank">📅 20:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27473">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SEjLEGPB0CKl0NM8-xavWWYQ98kGSg1RJfEaWuS0ZZEBxayFqWGWnGSsVqrnFk47JE-gMXEl3eH3Q3WHD6GPVybGIGobaGfm202yHpdAfa_xZRCFXvYbWPnlWFQerT702MjvLoELD7alzgL39Pik65BR8veVoUixS18-_ExlFDTcpsffXeZL5AoZ0VU9gSm8Q5G9HCaw-Dux_2XQc9PH5r6f4IGqOkBpnh5S555MOyvnmsVPJu4OCLtqZVdqop2TslX4SZJdr74ut3iE3Zwxai9fp2M6fQSrjp_k9FcQV8ui9yHnlRXC6Go-LZaVo16bN2Nzz99Zsmpc0Rttz65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27473" target="_blank">📅 19:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27472">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzuQnT0rb3EbjQ4NyVJlPLaEMCKCtMwvPZSrv_3WKWNDu7_bNVctc9EAfPhtwhKKJ3fbqj59ZxD7GzOUnvdduyH6BbGJ432ycc6KvpaJTuZtA4xiVaHu323oQKW6kwj3DGd4kX36tSGwtU0q9SlFvSjMAv-6RL5W5GynGoIc_7PuPYq1FrLVhaM6kLQnlhHFkvsFHel0UFnzzt5N_t0ZNB1OEdnDOWE2ka3aZj6DPWOJIFSIPmEEX0usvm66Rorrn0oO9kKFQO-_KeaShpH4t8Nh97XFAc0hMCaFXgWuiONhF4ik7LnJ5nN7Miu39fMNLb1jHVmwmX1f57dWbWOCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
ایفمارک و زهره هراتیان درحال‌برسی پرونده مصدومیت‌آلمدین‌زیلیکیچ‌بازیکن‌خارجی فصل‌گذشته استقلاله. درصورتی تاییدیه ایفمارک؛ سهمیه هشتم و سوخته استقلال تا پایان هفته احیا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27472" target="_blank">📅 19:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27471">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=qwqoVEAMevqmh3YYdaKGFDeXOGou2esthIt1XkSrSjimraSdioXfdYpnaTr3x2v4_jt0LxFMhJj4BUFsvqHOpZlipAuxuDFDpSVr_Hw78Ip3t65kHW_XqgYZcOxJgsKXja7PH89iMVVcAwrHqyEBl1EWEtDAymNwKRaDMGvjoAMPB_Pga2VTriGQr-7MbN0-hSMmIhx023Oyi1A_wI-YpKS3uCHk5yK8np5iOsZ4BbRT0Sv2WJnaXjxu3nksvHImONU8bxq-DQbncuW-wg0_9SgK0mLqMmARR4iTF44R-zQApkkaZ7gS7u-ZfyyhSCihUPJE4KN2xPHlxNTcph8Mog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=qwqoVEAMevqmh3YYdaKGFDeXOGou2esthIt1XkSrSjimraSdioXfdYpnaTr3x2v4_jt0LxFMhJj4BUFsvqHOpZlipAuxuDFDpSVr_Hw78Ip3t65kHW_XqgYZcOxJgsKXja7PH89iMVVcAwrHqyEBl1EWEtDAymNwKRaDMGvjoAMPB_Pga2VTriGQr-7MbN0-hSMmIhx023Oyi1A_wI-YpKS3uCHk5yK8np5iOsZ4BbRT0Sv2WJnaXjxu3nksvHImONU8bxq-DQbncuW-wg0_9SgK0mLqMmARR4iTF44R-zQApkkaZ7gS7u-ZfyyhSCihUPJE4KN2xPHlxNTcph8Mog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
عمق اسکواد رئال مادرید درفصل‌جدید رقابت‌ها؛ کنجکاوم‌ببینم‌مورینیو با این اسکواد جام میاره یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27471" target="_blank">📅 19:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27470">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=CsG432w1I0mSmbm5PhNvLNHVSo8SqqMItaenMoaCP1QrPFTFzErQtO-7OAiVOCibwK2If2PIY8c6lMWQjp0TgXXOtrC7xKLUtEjStBT5cEv5U71riY2a9Cz8VdnLV5KHEHq_Lli2FHzAL7aS7tgD4KaIs4iq75YT9V1RGjjVDVjR6nOqitfKjhwtrX6BmcxFvg591RLzbfOPYCvPNRP1Za-0ujE_BnUFMlDUp5lztdg2Xx8uu5jV9Z4pQXA4Hdpx_CXgHFC0WxQ0NwhU3s90DssEgSxXn8IOo9mS6jnqJtz5xGJ2lKyxf-3_nMV-RlLaLlGE-V2DO9HJtpioohiXeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=CsG432w1I0mSmbm5PhNvLNHVSo8SqqMItaenMoaCP1QrPFTFzErQtO-7OAiVOCibwK2If2PIY8c6lMWQjp0TgXXOtrC7xKLUtEjStBT5cEv5U71riY2a9Cz8VdnLV5KHEHq_Lli2FHzAL7aS7tgD4KaIs4iq75YT9V1RGjjVDVjR6nOqitfKjhwtrX6BmcxFvg591RLzbfOPYCvPNRP1Za-0ujE_BnUFMlDUp5lztdg2Xx8uu5jV9Z4pQXA4Hdpx_CXgHFC0WxQ0NwhU3s90DssEgSxXn8IOo9mS6jnqJtz5xGJ2lKyxf-3_nMV-RlLaLlGE-V2DO9HJtpioohiXeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیتر ورزش 3: کاپیتان‌تیم‌ملی به صدرنشین هلند پیوست. واقعیت: کلا یه‌هفته‌ از لیگ‌برتر هلند گذشته و جهانبخش رفته تیمی که پارسال سیزدهم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27470" target="_blank">📅 18:58 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
