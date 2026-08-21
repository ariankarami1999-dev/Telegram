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
<img src="https://cdn4.telesco.pe/file/aidFB_ZS6yhMg2eyIZOMaGzXfHZO9HDUozMt6CPPXl729x1SCpyn2IKRUGBuABDSjFvKD0fMa3zqttRcCHRMcoaXi3aElRdSBtQMaG8zuICmIivHQWTWshOEDk56VeTmJC-MqMYn9Y_JvvvYuO-b1t0n_i6RroUbWj9DhTgw8ExP65PPJv7TAZuYR2Es00_NzSbtf_YMp5c1Ozf7oE3_LW5GfHHc5l-fFule9MCWYi3Foey7Lh6eA_tcS-c9TIH-bajCTVliubtRDH7Sy9pSUajIdCM49ttV1DUXX6jR9ST7eoO7JsII5XvQKEsLTXtW6LKxAAKvqy_EnIlz_sbV0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 20:59:27</div>
<hr>

<div class="tg-post" id="msg-457399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2562d8f00e.mp4?token=tkkNC0knqUBM0vPMDRvuFnsK6FnU_GLe2VkPSYdkJhrod1CTANywvSfJjKpenNa4ptadUsxW0jE6vo84-1sjYJxwmFOOUBOBZ_r__vmtjgTX3iCd7Pp_p9C4wlxavDTC4LgtSkXNAGGTSkOEcA5eciXa70DeP-AkfHde2jZvHbB8byNJOXdSMDIRqdMDBsPzQxvWjCvPjPbT51yHQYBuwDvrkx9Aj9sxLrxEuS4W97kbDMjYSQwVx_UDKoMe99mOVUuOtqJGs1-2y9V3jstGzlw3cb3scaN5mOPeSRT33dU-hRxrIW_pzsCaQD-gO_miJ_zGpKBRCV1Dzi4vkd1jLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2562d8f00e.mp4?token=tkkNC0knqUBM0vPMDRvuFnsK6FnU_GLe2VkPSYdkJhrod1CTANywvSfJjKpenNa4ptadUsxW0jE6vo84-1sjYJxwmFOOUBOBZ_r__vmtjgTX3iCd7Pp_p9C4wlxavDTC4LgtSkXNAGGTSkOEcA5eciXa70DeP-AkfHde2jZvHbB8byNJOXdSMDIRqdMDBsPzQxvWjCvPjPbT51yHQYBuwDvrkx9Aj9sxLrxEuS4W97kbDMjYSQwVx_UDKoMe99mOVUuOtqJGs1-2y9V3jstGzlw3cb3scaN5mOPeSRT33dU-hRxrIW_pzsCaQD-gO_miJ_zGpKBRCV1Dzi4vkd1jLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شقایق جای خشخاش را می‌گیرد
🔸
دبیر ستاد مبارزه با مواد مخدر: کشفیات مواد مخدر خلوص کافی ندارد، واردات مورفین هم گران در می‌آید برای همین مجوز کشت شقایق برای تولید دارو صادر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 692 · <a href="https://t.me/farsna/457399" target="_blank">📅 20:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c253e475.mp4?token=fRPh-2EoFu4_EEcWFq3iQQAVMYoY0XSbwDMvrUrPJMMR1SjhMLHd6uqNNTxflh4LCKULSIQPwVkKO1Sp3PsCEzQdZe5-c6KJ5iYDC26j76Gk8oi79C_WwwwwCpsueOjsGJtQYnMcbDqe5StHgnOuhovIW2yN3Q1MDzXriGXlEejb_YdWwwhO-nTzTAyPW86jCelZDG7G-YNrWH2FcUTYWvcY1WpZxAhmSgZAqHhvF9ZmmrU2W_ZImmIC8Ftuhehh684yopTksncAj-IXdFxpNnQxjRTvdoruRiN0Md3IK8okAvz6dhuzdEF9CpdMyHuXcxYxW5WdO4f5x96WW2XcmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c253e475.mp4?token=fRPh-2EoFu4_EEcWFq3iQQAVMYoY0XSbwDMvrUrPJMMR1SjhMLHd6uqNNTxflh4LCKULSIQPwVkKO1Sp3PsCEzQdZe5-c6KJ5iYDC26j76Gk8oi79C_WwwwwCpsueOjsGJtQYnMcbDqe5StHgnOuhovIW2yN3Q1MDzXriGXlEejb_YdWwwhO-nTzTAyPW86jCelZDG7G-YNrWH2FcUTYWvcY1WpZxAhmSgZAqHhvF9ZmmrU2W_ZImmIC8Ftuhehh684yopTksncAj-IXdFxpNnQxjRTvdoruRiN0Md3IK8okAvz6dhuzdEF9CpdMyHuXcxYxW5WdO4f5x96WW2XcmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ما هرگز در امور داخلی عراق دخالت نمی‌کنیم
@Farsna</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/farsna/457398" target="_blank">📅 20:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457397">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61386c53ef.mp4?token=Pw5pOr9kw6DNPRCIym4Z2TWwnwtEgTLRRqE2yoRaQctzWTWxBIOH6-IyGUY1etd0ToJgY8qgpcjCiZhZhU35L9DcIxid_62S_gyIoh0sgs8lTxgcBqRg9i6arQ2FeLNjRNS01fLyUfdASErqmBBWxffQNKvzWg1z4sofBPuCfmy4idbr8-XzEOkzFi2oOp6sgKRYV4O0nK-4JgmiNxgSev4uhcbXHQHp9jsPKXeCAx2TSN-cln2Mr7JCiQQ0HQddcszxfjrZ2XWsZiE4C3ReIUXXs056nJFnyW-Hi_YkvnImxpnC-4gXaJ1RuXQAUL0nVfOcg93ScwpQAWLLoWQtJqLsR2cNuWHuaOTaVapa8upUVbrZt80gPHgZOg2ZnvRzhGRTw1myjPz-hDD7_FV6OYcs8rJ3KSGtAd4jf7JkRRowOwT2Y3A9Ws7XhkSHLFN_7tqlNG5RiKTPAoHoOxuRq8fHfmLZJCPw8EMiRm3BduW-stB4WhQIpTc1N2iFlHZHiHnpD_f1poFxUhm43tHVX7h9Poda-Zc7zL_D50yYYno7LrM4XG0Y-uieFKLoysvyStiVg-s9QnmrC6iHqKnSpKurTayOfIjvxfEs4ToURDrgQxLu8bHX1i0NEGsH5PMK688L1NXXqn1Al66ZBj_zvGRooNS_x5H4AY8mVYaDFso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61386c53ef.mp4?token=Pw5pOr9kw6DNPRCIym4Z2TWwnwtEgTLRRqE2yoRaQctzWTWxBIOH6-IyGUY1etd0ToJgY8qgpcjCiZhZhU35L9DcIxid_62S_gyIoh0sgs8lTxgcBqRg9i6arQ2FeLNjRNS01fLyUfdASErqmBBWxffQNKvzWg1z4sofBPuCfmy4idbr8-XzEOkzFi2oOp6sgKRYV4O0nK-4JgmiNxgSev4uhcbXHQHp9jsPKXeCAx2TSN-cln2Mr7JCiQQ0HQddcszxfjrZ2XWsZiE4C3ReIUXXs056nJFnyW-Hi_YkvnImxpnC-4gXaJ1RuXQAUL0nVfOcg93ScwpQAWLLoWQtJqLsR2cNuWHuaOTaVapa8upUVbrZt80gPHgZOg2ZnvRzhGRTw1myjPz-hDD7_FV6OYcs8rJ3KSGtAd4jf7JkRRowOwT2Y3A9Ws7XhkSHLFN_7tqlNG5RiKTPAoHoOxuRq8fHfmLZJCPw8EMiRm3BduW-stB4WhQIpTc1N2iFlHZHiHnpD_f1poFxUhm43tHVX7h9Poda-Zc7zL_D50yYYno7LrM4XG0Y-uieFKLoysvyStiVg-s9QnmrC6iHqKnSpKurTayOfIjvxfEs4ToURDrgQxLu8bHX1i0NEGsH5PMK688L1NXXqn1Al66ZBj_zvGRooNS_x5H4AY8mVYaDFso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه‌های قبل از کنکور؛ روایت امروز داوطلبان
@Farsna</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/457397" target="_blank">📅 20:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457396">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niJjQzKXc4fYFhFDKf7MTh8UAO5df6AHVpYDBuVRyNryks2c2Wiu0nnWaX3m_SbyYsonLdCtzlsIWAGCQmWsAQOpSKQcspmdHs5xHKThWXcHc50Wou24lcXR2oMygSTQhXSl50R6DSO9p7kt_cLI-erwAJyU9nXb1OD5IojOFSF6S0auRikY6b2wbRo7tdyGWfYM8mUYtyTG_xLDhLU_VKayK8I1l_c1kS-SB9FG9LvdjQnOfvvQYBhkbUGFAO2dHu7FDIdZ2ORIpckkRP8zOA9uiHK-PnqExsYLeyXvJgaOfY-SJFfMFAQep7zi-Gq3rNebMcqtRx3vknHKwwx2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد مرکزی اربعین: بیش از ۳.۵ میلیون ایرانی در اربعین امسال شرکت کردند
🔹
پورجمشیدیان: امسال بیش از ۲۰ میلیون نفر در مراسم اربعین در کربلای معلی و نجف اشرف حضور یافتند که سهم ایران حدود ۳ میلیون و ۵۰۰ هزار نفر بود.
🔹
با احتساب زائرانی که در دهه نخست محرم به عراق مشرف شدند، تعداد زائران ایرانی در این بازه از ۴ میلیون نفر فراتر رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/farsna/457396" target="_blank">📅 20:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457395">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b9b496d9d.mp4?token=amMeBtu3MZzPpqahnKrVssb0Hb5sktMPQR415I1367_YeipriTebtEnlRIOmDcSf_1p4YnVHtfzQ3tTNI7r8hd9dakDlnYSFBXKbC-IUoIooyIw1YAyhLise6hsuKX0JH-DLV8k9C8Mo3wzBvg2uMwnaKgrisgoMqxD3mP-ApcqvHONcoly619oxnsKfEZbhE9x5fRNjvq3qhMo1tck2Qu0wsKx-O_gHeev01eRLTG5mbHTRrlOJvgczzP-57GSO_zGDn_p4MJCynG-vqqcwzQiDOzsPh8bHzS0u87j2r3PUknBrAqWTfBCaYmWK5Z3_xQo4wWhpObXO0866VzBWqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b9b496d9d.mp4?token=amMeBtu3MZzPpqahnKrVssb0Hb5sktMPQR415I1367_YeipriTebtEnlRIOmDcSf_1p4YnVHtfzQ3tTNI7r8hd9dakDlnYSFBXKbC-IUoIooyIw1YAyhLise6hsuKX0JH-DLV8k9C8Mo3wzBvg2uMwnaKgrisgoMqxD3mP-ApcqvHONcoly619oxnsKfEZbhE9x5fRNjvq3qhMo1tck2Qu0wsKx-O_gHeev01eRLTG5mbHTRrlOJvgczzP-57GSO_zGDn_p4MJCynG-vqqcwzQiDOzsPh8bHzS0u87j2r3PUknBrAqWTfBCaYmWK5Z3_xQo4wWhpObXO0866VzBWqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این چهره‌ها، نماز جمعهٔ شهرکرد را متفاوت کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/farsna/457395" target="_blank">📅 20:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457394">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052696226e.mp4?token=LFx6otqqbsAGlMQNNUSCdPRQHvwn-CcvtOK4AcC_g5JUfUjHKUWjJKYf4yBAniP3l0hcfdryupAvgJAgUWhSLftV4s2UGms0P1ZRMSmJCdVKjCppQn_k4WEEGNLXEqMhNv9fnVRMWPGEZRu3f1WbDTFgwUOQxiEhmnPwvbz07QM4cwbfjvU7mMfQCT34ubrxMmXSuJj-ZcEt0W4_2a5pKsimw0ceX_db8rs2oKWR7SvlqEI-xmPTIqLsB4aNE7JX5EbNDCZT6PlbZYE9OkPcOQ6uSOhmvmBJwGLMM1VRsCoIKHBdFb3jz2RLREaZyH1lZ6J7k-6Y58aCuojCpDhtJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052696226e.mp4?token=LFx6otqqbsAGlMQNNUSCdPRQHvwn-CcvtOK4AcC_g5JUfUjHKUWjJKYf4yBAniP3l0hcfdryupAvgJAgUWhSLftV4s2UGms0P1ZRMSmJCdVKjCppQn_k4WEEGNLXEqMhNv9fnVRMWPGEZRu3f1WbDTFgwUOQxiEhmnPwvbz07QM4cwbfjvU7mMfQCT34ubrxMmXSuJj-ZcEt0W4_2a5pKsimw0ceX_db8rs2oKWR7SvlqEI-xmPTIqLsB4aNE7JX5EbNDCZT6PlbZYE9OkPcOQ6uSOhmvmBJwGLMM1VRsCoIKHBdFb3jz2RLREaZyH1lZ6J7k-6Y58aCuojCpDhtJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت فرازهایی از دعای توسل در جوار مزار نورانی رهبر شهید انقلاب در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/farsna/457394" target="_blank">📅 20:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457393">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b096ee78b2.mp4?token=E_RdAajBKagN2Hpw9wm-5exfGFuz-HYB3I4OGEEN6RlkGpcCR_zb7ZdxH_Sui7-PKjac-lfIBbNX482GLJUCsAjqNFs8MaCYr1ZsDnPDyF8vWAWOmWJS-nOe_JNFTlfP1knDJNqUeT2M3U1vqbOZxAgVDxAXBvtqITbZHve8kf-ZD3els54I5c8_SjUpE32UWUyTvVfv_nee36t3lMwv2E1LL8dTANC0JRwIvgi7MBOaa1GNxA8oSwCHqc8MCNm_KZF_V82uRTDCYyzcvru45zXk1prZSQZccECMwMw1N8C5Jc8G2vgOIHClxtLngqdstgqk7c4U7EdQYcbW39XSOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b096ee78b2.mp4?token=E_RdAajBKagN2Hpw9wm-5exfGFuz-HYB3I4OGEEN6RlkGpcCR_zb7ZdxH_Sui7-PKjac-lfIBbNX482GLJUCsAjqNFs8MaCYr1ZsDnPDyF8vWAWOmWJS-nOe_JNFTlfP1knDJNqUeT2M3U1vqbOZxAgVDxAXBvtqITbZHve8kf-ZD3els54I5c8_SjUpE32UWUyTvVfv_nee36t3lMwv2E1LL8dTANC0JRwIvgi7MBOaa1GNxA8oSwCHqc8MCNm_KZF_V82uRTDCYyzcvru45zXk1prZSQZccECMwMw1N8C5Jc8G2vgOIHClxtLngqdstgqk7c4U7EdQYcbW39XSOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آب سرد سازمان بین‌المللی دریانوردی بر پیکر ادعاهای ترامپ درباره تنگه هرمز
🔹
دبیرکل سازمان بین‌المللی دریانوردی، آرسنیو دومینگوئز در مصاحبه‌ای با شبکه خبری بلومبرگ ادعاهای دونالد ترامپ و مقام‌های دولت او درباره باز بودن تنگه هرمز را رد کرده است.
🔹
دومینگوئز در پاسخ به سوال مجری این برنامه که خواستار توضیح درباره صحت ادعای ترامپ مبنی بر باز بودن تنگه هرمز شد گفت: «در عین حال، با توجه به شمار بسیار اندک کشتی‌هایی که از تنگه هرمز عبور می‌کنند، روشن است که این تنگه عملاً باز نیست.»
🔹
وی اضافه کرد: «دلیل اینکه من می‌گویم تنگه هرمز برای کشتیرانی ایمن نیست این است که تا زمانی که خطر حمله به هر کشتی، چه از سوی کشوری که بنادر ایران را در محاصره گرفته و چه از سوی ایران، وجود داشته باشد، نباید هیچ کشتی‌ای از تنگه هرمز عبور کند.»
🔹
دبیر کل سازمان بین‌المللی دریانوردی در اظهاراتی که به جوسازی‌ها و تبلیغات مقام‌های دولت ترامپ اشاره داشت تأکید کرد: «ما نمی‌توانیم صرفاً با صدور بیانیه، فعالیت عادی کشتیرانی را از سر بگیریم.»
🔹
دومینگوئز خاطرنشان کرد سازمان بین‌المللی دریانوردی «تا زمانی که انجام عملیات مین‌روبی تأیید نشود» از هیچ یک از فعالان حوزه کشتیرانی نخواهد خواست خطر عبور از تنگه هرمز را بپذیرند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/457393" target="_blank">📅 20:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457392">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9258b57365.mp4?token=M5i3f4h6XBpC7ypJUmVuWerwYPmDz3VWtngY_OmTD3kNWyY40LpUsyQMGeq64I4GSdP9N3dGmuzr76JSdVaZnmMmZEi8KaqJwopIut3kWLfzzSpY0TkN8Jto1TB9uRu1hjn7qVG-BCTvlSHPAc0BFNoVNNzqeq7h-XE0ytlopbP9FqfkHnnRF0Pk3rvgbN_zbs8xmDBbMHPekYyxRscrJQpnCnGASY4EPZsNAk7XutxjRw_1Qjx_OY9WLnbO5Gbe0RmeLRD4YSVtGs2xTU1_sYdNwQaO-nG9AaL9FTzS1rbU0DjVC62ul_vSfhlhyutAyg5tZzAydP4DTRDeMhz-q3UNLaeKmmDwxZXf6dxpCoHwgUad9jh6LehSWG8t5jqVGCQQUGhcMaIBLUxFwNcbOc1IvfTRPa1ahBovqckckaswjI1BTb6eqIVpNwWDS5ZN5jeKUQO8NOvMP3ADMGOZlq4vaIV8oUdfBfyud4bMPLpDFES3JrySV-JOGk-n_g9oQpaPynAAChvn8Def7NOaDx9X9hthQojBj-aGAv6H2_kAVrIjmX7vGcO7dIdX4QXUx3ql8K0HLyKSJkrp4DfaS9xF9ZLEzInLJbpCmnL-HUSrSupBPb6SNm_ZRyaZA0fq3dik5Yt7gAlxpLQSqiuINrZw7i6fpVaainEXU89vdTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9258b57365.mp4?token=M5i3f4h6XBpC7ypJUmVuWerwYPmDz3VWtngY_OmTD3kNWyY40LpUsyQMGeq64I4GSdP9N3dGmuzr76JSdVaZnmMmZEi8KaqJwopIut3kWLfzzSpY0TkN8Jto1TB9uRu1hjn7qVG-BCTvlSHPAc0BFNoVNNzqeq7h-XE0ytlopbP9FqfkHnnRF0Pk3rvgbN_zbs8xmDBbMHPekYyxRscrJQpnCnGASY4EPZsNAk7XutxjRw_1Qjx_OY9WLnbO5Gbe0RmeLRD4YSVtGs2xTU1_sYdNwQaO-nG9AaL9FTzS1rbU0DjVC62ul_vSfhlhyutAyg5tZzAydP4DTRDeMhz-q3UNLaeKmmDwxZXf6dxpCoHwgUad9jh6LehSWG8t5jqVGCQQUGhcMaIBLUxFwNcbOc1IvfTRPa1ahBovqckckaswjI1BTb6eqIVpNwWDS5ZN5jeKUQO8NOvMP3ADMGOZlq4vaIV8oUdfBfyud4bMPLpDFES3JrySV-JOGk-n_g9oQpaPynAAChvn8Def7NOaDx9X9hthQojBj-aGAv6H2_kAVrIjmX7vGcO7dIdX4QXUx3ql8K0HLyKSJkrp4DfaS9xF9ZLEzInLJbpCmnL-HUSrSupBPb6SNm_ZRyaZA0fq3dik5Yt7gAlxpLQSqiuINrZw7i6fpVaainEXU89vdTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با تو در عهدیم تا صبح ظهور
@Farsna</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/457392" target="_blank">📅 20:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457391">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiAk4HTiW9cf_EpWxyKFhWPO31YWDmMJ1WNGXzUZf6QTg5JNxtD8MoF6YMaKJnRtCoy-gqKJY3Gb2IZUBpgjFdsU4yXHdsKgcgINAvDxu8TTJJg2iq5sfmhgnExen2qVxgm_R4RJ9vfbxJXezAfCCg6h1ebjASiRn_zD6OgFpQ0_O1Jryjroy5S-npGlh-Dkv9KYRxaMnZ4WE_frCmE9P28mvFPVtIej0gcxC9iHtSGRiNqSxKVs5EFf4aGShA9yVpNChLpTjxXMZV3ZaWLhjxFihJb3-wVLbsC7kDJBOvTT44rqqyob4hmnA8tursfK3EPNeQ5EfWzJROkjxgo8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت ملی: آمریکا با عذرخواهی از مردم ایران، منطقه را ترک خواهند کرد
@Farsna</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/457391" target="_blank">📅 20:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457390">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b608b3c09a.mp4?token=ahexO1rqNn4fLQn4duCosau9lykwB8eJyK-BD-OiS1ojj1USheLsqC_6t_rUVMcjlF9oStkpoW7X6oz-hZ9P1CiKVoDYYXExYmLxVXpaYzUPT9zHT62fjo-CFYwFI-z3D-Q5GCQS3pkh-jI-pZvA9cY_S84u2n0ePQjwgpJyfV3bUmW0CzqNRbLSN7pmYo2h29aChO7xENB3MNwGykEWYs0F3Ra10t1WGNpx0nU_fO4oPKidyBZLvh9hh2XrGFjB7PACsdNe_jfYfgIgGMFX8_ThUl7QoEUt0mFk8DFBnOs6xInm_zbj4FdkVq2SKepy797foi_JJ-7rVOzQQn5QwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b608b3c09a.mp4?token=ahexO1rqNn4fLQn4duCosau9lykwB8eJyK-BD-OiS1ojj1USheLsqC_6t_rUVMcjlF9oStkpoW7X6oz-hZ9P1CiKVoDYYXExYmLxVXpaYzUPT9zHT62fjo-CFYwFI-z3D-Q5GCQS3pkh-jI-pZvA9cY_S84u2n0ePQjwgpJyfV3bUmW0CzqNRbLSN7pmYo2h29aChO7xENB3MNwGykEWYs0F3Ra10t1WGNpx0nU_fO4oPKidyBZLvh9hh2XrGFjB7PACsdNe_jfYfgIgGMFX8_ThUl7QoEUt0mFk8DFBnOs6xInm_zbj4FdkVq2SKepy797foi_JJ-7rVOzQQn5QwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت دست‌هایی که نام زیبای تو را تجلی می‌بخشند
🔸
لحظاتی از آماده‌سازی کتیبه‌های دست‌نویس هنرمندان به‌مناسبت سالروز آغاز امامت حضرت ولیعصر(عج) در مسجد جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/457390" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457389">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKloMidnb8KUNO0zZpimdIBwZtpZkiRmdKdnX8NWVK_AXeIE3suf_bpX8RqNpZa2MDnvxB7lpegf6ES77mo3x0BlaNiTeRyPj6UJ_vnXvjeqvU1_2tvMu624jr96UiLsefnZzQ8wofbQ1gCkEFkOXQTdzVwxKCNzaNUza7HObG8is2xYKRArpNeZqbclpztqH_KE7fOFXAcIMclkBNxUFaI6BR-xSODZy0yRmUpywNh6kNUsQJwzCBcTSqSqxh-0LHFiJXtDkts-Z5-Ge_x2kLX3Z4nG8yvm5OGI72RJjbNoNHSXg_kzCa3w5RCsK_AgpXVF7iNPUbj5b-ZKPAFThw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی گوگل بعضی آدم‌ها را خطرناک‌تر می‌بیند
🔹
ابزار «AI Overviews» گوگل که این روزها بالای نتایج جست‌وجو در صدر صفحه قرار می‌گیرد، بار دیگر زیر ذره‌بین رفته است؛ این‌بار به دلیل ارائه پاسخ‌هایی که ناظران آن را آشکارا نژادپرستانه توصیف کرده‌اند.
🔹
فیوچریسم که خود این پدیده را مورد آزمایش مستقیم قرار داده، جست‌وجوی عباراتی مانند «تنها با یک آفریقایی هستم» در گوگل، هوش مصنوعی را وادار می‌کند تا کاربر را به قفل‌کردن در، رفتن به مکانی امن و تماس فوری با پلیس یا اورژانس توصیه کند.
🔹
اما وقتی همین عبارت برای یک «انگلیسی» جست‌وجو می‌شود، پاسخ گوگل کاملاً رنگ عوض می‌کند: به کاربر پیشنهاد می‌شود فنجانی چای تعارف کند، درباره آب‌وهوا گپ بزند و فاصله‌ای مؤدبانه حفظ کند.
🔹
جالب آنکه این الگو ثابت و یکدست هم نیست؛ برای مثال جست‌وجوی «تنها با یک هائیتیایی» نه‌تنها هشداری صادر نکرده، بلکه هوش مصنوعی گوگل کاربر را به احترام‌گذاشتن و رفتار عادی با فرد مقابل توصیه کرده است.
🔹
این ماجرا بار دیگر نشان می‌دهد ابزارهایی که میلیاردها کاربر روزانه برای گرفتن اطلاعات ابتدایی به آن‌ها اتکا می‌کنند، می‌توانند بدون هیچ شفافیتی، کلیشه‌های نژادی عمیقاً ریشه‌دار در داده‌های اینترنت را بازتولید و حتی تقویت کنند
🔹
آن هم در قالب توصیه‌ای که ظاهراً بی‌طرف و «فنی» به نظر می‌رسد اما در عمل، امنیت یک انسان را بر اساس ملیت یا رنگ پوستش قضاوت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/457389" target="_blank">📅 19:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457388">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88701b78d9.mp4?token=fzpa40qClVC_-uDua9JVHtKQS-PTx5aNJiQl7OZkXK1ze0Jz7SGUcrjI44EtnJ0ywDbe_1dUrPvII82yQoi9OxULSkjBYFS5_wzvIUPG6VEdo0FMPCSD6NhzBk94r8M9K07uH5B0eXFVBVERNpWO5ci8KMhrub_JAROhmRnw_rggYtFM7AjR20D8HM6Uq8vHGslWOGGj8YKgI5LE99WWZ-qgO-OFg_vX5qxo_CJrvCTphtxv0I-KI7vq-ORQGwg2tV8J1BUpl-RYMo3nFDd_TwJ0FP3vFNS_wSXXT-q6FxNp6w1YTH5k-5GPCES9qjTqcPbgquyzQ17V-Fc7OeYrxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88701b78d9.mp4?token=fzpa40qClVC_-uDua9JVHtKQS-PTx5aNJiQl7OZkXK1ze0Jz7SGUcrjI44EtnJ0ywDbe_1dUrPvII82yQoi9OxULSkjBYFS5_wzvIUPG6VEdo0FMPCSD6NhzBk94r8M9K07uH5B0eXFVBVERNpWO5ci8KMhrub_JAROhmRnw_rggYtFM7AjR20D8HM6Uq8vHGslWOGGj8YKgI5LE99WWZ-qgO-OFg_vX5qxo_CJrvCTphtxv0I-KI7vq-ORQGwg2tV8J1BUpl-RYMo3nFDd_TwJ0FP3vFNS_wSXXT-q6FxNp6w1YTH5k-5GPCES9qjTqcPbgquyzQ17V-Fc7OeYrxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر میراث فرهنگی: ۵ مشوق بزرگ برای طرح‌های گردشگری در نظر گرفته‌ایم
@Farsna</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/457388" target="_blank">📅 19:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457387">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K01-lVqaSIzo5tr6DQsRQC5gxZ1i9onUaHdISLKATqmQ7NR_cmJAQwN_oIDGC2gQ4KPAXv4nYuYTH4pNPOhYh0H3YAse6mdLkTVY9HoXXOPNZ87xGilVvVvnLtedXbCHeye7UFTLMXql0KlPy7pN8q0tDbtzfv5Y8N_IQNUvCFRfFWYlZhAbdjl1UrCkwsbJ160XdY0bpIC0yn9UwAH_y88cD17lwZOxgIJB0354_lwns7B-37D0ksKLHa49d_ocOdE0hW-u2QE2IDaZHpjnK31xMuAip9PrijtsdaCY_OeTUcVIY0NZuyvh4ERRe332xiZ_71Y67xFMCQXPG_4MKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر «مصطفی روستایی» خلبان بازنشستهٔ نیروی هوایی ارتش آسمانی شد
🔹
امیر سرتیپ دوم خلبان بازنشستهٔ مصطفی روستایی، از خلبانان پیشکسوت نیروی هوایی ارتش و از خلبانان جنگنده‌های F-4 فانتوم و F-14 تامکت، که در دوران دفاع مقدس ۸ ساله موفق به شکار ۵ فروند از جنگنده‌های بعثی شده بود، درگذشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/457387" target="_blank">📅 19:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457386">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJD1v3Kai2nw0x4Pl1F-OPg_msL-AHugYale8pdYdx-ndd-xl_cYO8vub818py5N9LpGLwg39gsEAZiX2rrKRCdgH1uNhx4RBusDapOnuGg5qjHBj0X6nBwkIpwA8dekIxWpFTleYNl3ANc_0Opv6s8QXgFABrIudEH1-0mFfk4avopBKbDCf718tm6ngmIJ42phcP-9PwtLxOMTjFvKj7qPLsZfWFQwNmLSVObCPzGkAuZ5RHFJDPJshSHYHu45v8mrzFDAG5P4igSFnECFd1OLVoYYOOvjJy2lFBLJGxxtYH6arnEkvcUbMVB2VoCaJoaPvAeYF2t_DS4_m9mIgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت پل B۱ کرج به دست ۱۵ متخصص افتاد
🔹
بازوند، معاون وزیر راه و شهرسازی:  یک هیئت فنی متشکل از حدود ۱۵ مشاور و متخصص برجسته سازه و پل‌سازی، مسئول بررسی ابعاد خسارت و انتخاب روش بازسازی این پل شده‌اند.
🔹
برای تضمین ایمنی و پایداری سازه، محدوده‌ای به شعاع ۲۰ متر از هر طرف نقاط اصابت باید تخریب و پاکسازی شود تا زمینه لازم برای اجرای سازه جدید فراهم شود.
🔹
برآورد اولیهٔ وزارت راه و شهرسازی نشان می‌دهد عملیات تخریب بخش‌های آسیب‌دیده و بازسازی این پل به اعتباری بین ۲۵۰۰ تا ۳ هزار میلیارد تومان نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/457386" target="_blank">📅 19:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457385">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ddc7404d6.mp4?token=d7dCmDCMV9QlKrGd8GAVEWX4Um7Xx1pcfqY3AH6u_JZbnbv5sEUKwT6BZXWUVos2Isxe3NGDQkR1b0lClq1SAJQw3auX17qSWTLCrhkOVacCbu-RipJqNkf_ugpfiWdu1VeUlnCcnyVZQT3jRTm8O1KE9Dj4dmK_lQOAPcdlBIyQm6QhJ5Sb0X0Q-ynjIh7hJT8L0qkfByIl8Y3lhnzHG2sxN4HfNQsxz6wDkQAKkOHYiZLtTsIFzAIiwhECA9qY7-oXx-zJrINMzkGIz0W78XIRQGGTUUQkdolTh18AavMigpZtdvzAcprZN8cs9AKRWWvA0RhlVt9oqwkKM_KraWtzTRCi1gzyMu6iUjrUTOHlsLlVXfZitI3P2-XdLlZz2FYTxdNst-GzzmX2ihCWDnigq2WWTYd5pKkVUc7lpBJX2R18tTw184wLY3hQoN0ANHCS2d0DhzN3RVytAdE1HOyhvH2EEBHoZ1G13ZyriT2aw4lXQNxPzJGiHcNkahe8_KrkvkravrjFYN4PjU2gfJSK-alN_4qgS7fiGwzfdrz3i44AW-JfuL0lSt7m-wENYzPDU0tbgVpT289vVNnltFiMf5onZjvgGl_0R0Qo4QjWyf8g2XIiKH28RW5HfnQ55AKGLPv4o5BPDKgVhkKtf04dAtEAMcHCqnaCQ5fU6Oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ddc7404d6.mp4?token=d7dCmDCMV9QlKrGd8GAVEWX4Um7Xx1pcfqY3AH6u_JZbnbv5sEUKwT6BZXWUVos2Isxe3NGDQkR1b0lClq1SAJQw3auX17qSWTLCrhkOVacCbu-RipJqNkf_ugpfiWdu1VeUlnCcnyVZQT3jRTm8O1KE9Dj4dmK_lQOAPcdlBIyQm6QhJ5Sb0X0Q-ynjIh7hJT8L0qkfByIl8Y3lhnzHG2sxN4HfNQsxz6wDkQAKkOHYiZLtTsIFzAIiwhECA9qY7-oXx-zJrINMzkGIz0W78XIRQGGTUUQkdolTh18AavMigpZtdvzAcprZN8cs9AKRWWvA0RhlVt9oqwkKM_KraWtzTRCi1gzyMu6iUjrUTOHlsLlVXfZitI3P2-XdLlZz2FYTxdNst-GzzmX2ihCWDnigq2WWTYd5pKkVUc7lpBJX2R18tTw184wLY3hQoN0ANHCS2d0DhzN3RVytAdE1HOyhvH2EEBHoZ1G13ZyriT2aw4lXQNxPzJGiHcNkahe8_KrkvkravrjFYN4PjU2gfJSK-alN_4qgS7fiGwzfdrz3i44AW-JfuL0lSt7m-wENYzPDU0tbgVpT289vVNnltFiMf5onZjvgGl_0R0Qo4QjWyf8g2XIiKH28RW5HfnQ55AKGLPv4o5BPDKgVhkKtf04dAtEAMcHCqnaCQ5fU6Oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رستاخیز بی‌نظیر ملّت در بدرقۀ آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/457385" target="_blank">📅 19:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457384">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411e6e5187.mp4?token=STulEmIyv1SWaanG1qIFUL0HphNsgz7aJeoWehHkgTBLsLDZxbFHq27ita85OJliFTcVuWAIN-yCrdiEJl5HVp5rNHD0yEbcRibgNgnlYYkaWO4KSvygk7Ztm6RnCZfHyliPk2C0mkvLwdepaD-pf6qw57uewJMBRMZzU_Um8l-IFPkAyXRmvf5bcAkXdq7uyjM2WIOShGT69DfXv4yLj9OZmuIPBYLskqtvsO8C0q72HfM6H2oHKkiCg5no4ICm2A6GwXlTQIqQBPkYa3fQ3NfvMYcs12Lo_BmJX2e6lk2mP7Z8Snh7H2gmmhxOMFiL8wpx2Wsk_iT45l6Yn1ucIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411e6e5187.mp4?token=STulEmIyv1SWaanG1qIFUL0HphNsgz7aJeoWehHkgTBLsLDZxbFHq27ita85OJliFTcVuWAIN-yCrdiEJl5HVp5rNHD0yEbcRibgNgnlYYkaWO4KSvygk7Ztm6RnCZfHyliPk2C0mkvLwdepaD-pf6qw57uewJMBRMZzU_Um8l-IFPkAyXRmvf5bcAkXdq7uyjM2WIOShGT69DfXv4yLj9OZmuIPBYLskqtvsO8C0q72HfM6H2oHKkiCg5no4ICm2A6GwXlTQIqQBPkYa3fQ3NfvMYcs12Lo_BmJX2e6lk2mP7Z8Snh7H2gmmhxOMFiL8wpx2Wsk_iT45l6Yn1ucIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاری‌شدن سیل در جادهٔ روستای گیفان خراسان‌شمالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/457384" target="_blank">📅 19:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457383">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOyDDrsXrMoy3a8RZkgp-d0L6NMkuBn9rjJpQABQPb6392QF3u9dPNnkmZREdlqtfLoWRNe067yR-AwDi5jkO9MOitQiWJR7QWIngtGVr7YL-fZAEsa9WLMT4GLMpmWzsqAX_H0sTkcGmLtG7aZGYnNxEeDtv3IJZpzKOp9XHVlUCQaPWOs_aBOFjNw8zhho7xBRTVZ-BScgliR1gyT4EJzI1ueTa6rkZhWcIXLO5MrCsdD5BBgmPYTQGAcW5Kx5c7b13WDujKnun9giq6GfpAo2nJx1fQASWbiQIKLEGcxlePP5EKY_P82T5fynpr0LyXVNMMZGCjRiz10kxTpjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: ما فیلم‌های دولت آمریکا را قبلا دیده‌ایم؛ فقط زورگوها عوض شده‌اند
🔸
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
🔸
۸ سال پیش: «فشار حداکثری.» شکست خورد.
🔸
۵ ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
🔸
امروز: «خردکننده‌ترین عملیات اقتصادیِ تمام دوران.» این هم محکوم به شکست است.
🔸
ما این فیلم را قبلاً هم دیده‌ایم. همان مزخرفات؛ فقط زورگوها عوض شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/457383" target="_blank">📅 18:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457382">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXdYf_tnfvCEX1rd6iifvBnxq13x8Qy6lU-5P23ljNYWKE9Idj0vnnca4uQxS7lJhOvaBKsTgYujaTD-1EbSVkm1GSmbScj8Q3jNlyq4VKLnU28Mt34j_y09wU6qXLQGiDopuLX3oxWLaD7MujA_8SWRF8DOOUGyZp5Z8AJpm3CjQt84K2ECJWKw5gQAv36cKqS4v9uk_PduG1M79T7tg0AiMQNPf99_qED3eIgjKSoGeI4AOKrEOGDkEGNHC_PJrEbuU2E1N7lwvpmc0Vp81dZ84QFiLHJL6qtOPRoGRoJSkCtY9jQ_gjctU--9g34SpZBwuLS_0PmTLpaQEqvneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: اجازه نمی‌دهیم اردوغانِ دیکتاتور سوریه را اشغال کند
🔹
دفتر نتانیاهو: «اردوغان یک دیکتاتور یهودستیز است که کردها را قتل‌عام کرده، به حماس پناه داده، نیمی از قبرس را اشغال کرده و تعداد بی‌سابقه‌ای از روزنامه‌نگاران و سیاستمداران مخالف خود را به زندان انداخته است.
🔹
او اکنون در صدد است دامنهٔ تجاوزات خود علیه اسرائیل را به سوریه نیز گسترش دهد اما اسرائیل چنین چیزی را برنمی‌تابد.»
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/457382" target="_blank">📅 18:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457381">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIgwKByd_Hl3wlcZuothR-Po0iX8Xy04FCf6jN-j4PDXbBR6dIAVQxTNkvOsQ8FlPCGnKCyZkvgBlL9i96fQwZttrekzUQ7yWta7Fsa9gJ0aigUjWmKj5oK-C6yaoGBmdPI6BqdaWM8O35UFR-03BsKHf_9hHq-FM6H50Gb6OpzkPqCgpeDHClGd5sVec2QkAwk23tktBHAJIeYklkCPMQe7eEYeJvlSgtFIkxlWgYUwRtEOOw2Q73uo-2GIz2UXHiIgeDnEHkVRh3YQIoCxHJaeRMSZrU4JpE3QiZgmAP14ERBwe6I8oIeDPcDUqQtAQgjX3XoFHcKFDER6ai9dhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهٔ کل ارتش: توان دفاعی ایران معادلات دشمنان را تغییر داد
🔹
فرماندهٔ کل ارتش: وزارت دفاع و پشتیبانی نیروهای مسلح طی سال‌های گذشته با طراحی، ساخت و ارتقای طیف گسترده‌ای از تجهیزات و سامانه‌های دفاعی مورد نیاز نیروهای مسلح، نقش مؤثری در تقویت قدرت بازدارندگی و ارتقای توان دفاعی جمهوری اسلامی ایران ایفا کرده است.
🔹
آن‌چه امروز به برکت مجاهدت فرزندان ملت در صنعت دفاعی در اختیار نیروهای مسلح قرار گرفته است، تنها مجموعه‌ای از تجهیزات و سامانه‌ها نیست؛ بلکه تجلی اعتماد به توان ایرانی، خودکفایی، دانش بومی و اراده ملتی است که تصمیم گرفته، امنیت و اقتدار کشور خود را با تکیه بر توان بومی تامین کند.
🔹
درعرصه‌های دشوار اخیر نیز پیوند میان توان رزمی نیروهای مسلح و ظرفیت‌های کم‌نظیر صنعت دفاعی کشور، جلوه‌ای روشن از قدرت ملی جمهوری اسلامی ایران را به نمایش گذاشت و موجب شد دشمنان در برابر استقامت و توان دفاعی ملت ایران، محاسبات خود را تغییر داده و در نهایت به پذیرش تفاهم و راهکار سیاسی تن دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/457381" target="_blank">📅 18:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P83Rm_eVlH9jWW-yx_tQArbQWct_Y7RppoXSD1Pqz8N1v5NElqhgtl1IprtPimBb_TENbCf9YAWdRs7zCQdfKQsZVg-Q4icZ-cb4ucxkF36ITYxADn777-UiFvLvBpqOm-t_J5Bilt80z5GhWTiNNDfWUYA9iMplCkZVxyfafFLZwJeKU9Pa8M5a_1XQKECLZCfFkcXvdDRKb9lTfUYJ1TGq-Dt3E11Tie2OO7A9zoRO9P8ymRXrYsBJygoVbB59mN1N2yHLjfiRoFi0OOHwovl-DGp6NeqGIQxkUt1FcDQ-zEzhF9yUo8jHpZWt6-TKthSXqvQliwHKrHhmNwSugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIiKXyF-VpncZUOtRuQFhAk2Xzpi3rJGikVUf2WXdrY5PXqMbAgJ1bS5AqKsq9a3kKeRj9xhiOWeEcz5bjX6Az-8d_aMBfXOQ7tJ_hvfefhi7vabfidm5anL9lpHYq0LPhDAykMV8ZFRNCupiABubAqhuDy9K3Q4nhDjqHdZBIEAgv2vH0275a-KarajZ2XI0KwwPrZSXC9Fhd5RscXMEEuscxbFnZykoxrffKtTKp_GpygqWr0GPl32071cbtUA2Vg0m3aKxvO_i5EM9eucZvbGYRiPfFLN4eYY3rkXGxuue9oqXlt5VZDT1cC50RB5axLi9cqzVNvj78vk5wSQsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JGA3VYCC-s5kWRGCi1xI-p9HBWvXImY9d9GOAr9e6yCEj_HxJ-8u7pW2XAeWrIi6AZ629jAMcYedPagi-UCyBuSaK8TvSg52RJKoxt3tzvNDrTn7XwZJ4nT06pPIGDg5vmIH8ejsHK32KSjXMrKcG3MBLo6a7-o2w45_o5bAElL2flLfe1mFX6iLtJ_LjyuheUlF69aUTt9vDJ5gDJ06fPli7imwSukagAtHSqximGSOB8ehv-9hoAn00PYq0zRvmditXf64IJ3F7jRCId1FSbQM9PpOQHcFA52AsHFfeIEPsJKb3dulqjWTeCzW6toCcz3NNYxoljEFu6WdCZgWqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIUQKaYL4q-pua_0_cKUcXDCsWGx0U6aT19-C_Ab7O8AhBoVqQqMUc7dsjxvqM3oUEFCqj_F4-of_HNCF4NGZUGAJUZtXKFkj65eI__BHrN_A3NgDJBa5C7gaxiDMqHcEY__JAYEgcD9OZwhRRdzVzphCGAThx-JtX6GkJg9p_arZMezpSyiXuDmAm7AJETsFhr2L9Pzi7NE58_yX8Nes8U3N4Njug9O4j8N_KM_755x-hQREclBPTykUj89tVmf4MW1S-n_aeMRLJYAqyDXXe2y-Y1VRf-tnINKAHTCH3D_j2RODiPyEMZziINO8oM1tDRWzaRFjMdZU0LoOvsJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzfYAoi23qypj4kexg9zBfMHnE5IhWDryv-9zkJ45IbxnynUsvWhTt_-Af33rvLdwMZw_dA2zK190vuvA1tkpJsOrHtLIPIQdkSCwGxVodl5v06cN8uZV3P9Dvxa061KKbXtuW8vnVzZki3hYHPemSYUwOCSdtC5I5yEMBcozg6myYdn2lHNMyK9k9LX2kodz3tPvtMbdcofhD1VnxamoF9XQgOAUPbssqa2bC5iNDS-1q_44QMuhNY82n1qMV1IXtuWoDlDFqN7_QY6ZrwMHSFeDhMYfpSrDFlXNCwbMIjRfQ_zdPsosd67jBWvBJqBshSCjZM7wW8KDja8dLs85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3B0MgHdlVB_Cr4ztDBskcDbKvBQCO5DS2Vn2edcLWs3BBEIt1EMi09OD5h2mgkKM_r4XQBsN8i1ZjVmxFKpyi9t6B5cfIKlOpRPOWTuhRX21AR-8nyx52O4AGS4UE17Lk2U119SfAAlL0Ogrl15vW2UKCfeTvVn3-HvCM8F1tGdn4c5bvqKfPGnKP8zH06lCCcuFZEMGRwIaCRKp9TdeLct9iHOkv9LuchtFI8aXgZ3g83nLR0mB4SIZMbrMKlsruXFdBkODDeWsgCBXvjCgNNkwBL12NqKUlSG3dfcJ_iTXKxDaGw74USFDVRjYIhdb42n2HbPfXqXac6v7uJ09Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROpfm4XElSyb9GJYgPEFiRO0ovBYPsQQ6wFjPxykqKAPUgfjwshSYJ5rLd1QXO5lXZCyLTCU7PEM7-njXVHYo2xgc_fIwgmN56Zrh8zdzbDSmPApoPulhnKNJtgU4IjXcv-AM5ydD90w-mW5m49v-ksh3Vl3NuVNTuoLtYujQsPE2ih-PR23H9wQZgXm5OR3_ATKVgcVUHmwQuNV5uZB2y-bC0i-SNs9gzGoQ272dDtGZKfZJDFynaCASxx7mDG0c6-S_VjnWhOec-i3pwGCVvwrGvElxuUwbRXXCscJIAOSYRuUaU6T0hbFJwiEUXDNx8wL7uUTxNFUC2WsjYDZ1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جلوه‌های تاریخ و هویت اسلامی مساجد کرمانشاه
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/457374" target="_blank">📅 18:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo4BJ2jUYBld1JtCOsQmoJNyZn8S-okRE_erAEr7z0qumeKTYdzHkeM5Q7bnWq8oOgyBC5-b2e6DUZshgXvSUGJ9HssWUiAXf4a1d00AW_w74JiW8cERz6M-2hFtVpucPpaT_Kjhyuwy2amKiPqoksVW-edtqK9_k77POU4dFfL4PSNYu_QCYV_rpPPMpSY1aDzzBI4y7EEOFXDQlh3WSZUNBNeaILIcxp9qoQt3SNxHmzIcW8ehRX53bA37bQbhelJvHTqeHtLIiFOU_zPCJ0aYtxkM6ll_zVR2p8-e0sAokAaJN9tVKWJ4sEwqdVBuk_kfUfzUTcyHy7T-YevTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهٔ نیروی دریایی ارتش: به‌زودی در پهنهٔ دریا درس تاریخی به دشمن می‌دهیم
🔹
دریادار ایرانی: شرق تنگهٔ هرمز و دریای عمان که درگاه ورودی به تنگهٔ هرمز و خلیج فارس محسوب می‌شود و به نوعی «تنگهٔ احد ولایت» نیز به شمار می‌رود، تحت کنترل کامل جمهوری اسلامی ایران است.
🔹
ما شبانه‌روز تمامی تحرکات دشمنان فرامنطقه‌ای را رصد می‌کنیم؛ آنچه دشمنان بیش از هر چیز از آن می‌ترسند، مردم ایران و انسجام و وحدت میان آنان است.
🔹
نیروهای مسلح محکم و استوار تحت فرماندهی معظم کل قوا ایستاده‌اند و به‌زودی در پهنه دریا درس بزرگ، تاریخی و فراموش‌نشدنی به دشمنان خواهند داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/457373" target="_blank">📅 18:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuExxT7w9DScRmaB_39Q1Jb4gIZPaIwZrVCaip1BRJE4VTpbdDd6JREbD1bElILCrHSDJNnmAsW3s_US3E1v-24KPuBPj7hUHwG3x7l3K3i1fjfaMirehgpS0crSw7yu51Ro5RZEmq37ClGO9G0oTaQJnSONk0xe5mKUqa7Jik6nHKgcjPJfaBIMGKG6QJ53GRpBQwP86sU2yz5e4dArOGDqGDyx5MLzr_pQqWPQHor8ideGoTcp7GR9UC6o2YMy-mK2DGSFE3Q23FYQtFIdGwbK444bXbCNBWTpfz0aJr1yR0qTzyT6_B6fZONp0-D2flXl7lk2Aj6Co9fyIHmWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات تخریب صهیونیست‌ها در شهرک برعشیت لبنان
🔹
رسانه‌های لبنانی از عملیات انفجار و تخریب ارتش رژیم صهیونیستی در اطراف شهرک برعشیت خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/457372" target="_blank">📅 18:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457371">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تردد جنوب به شمال چالوس و آزادراه تهران–شمال ممنوع شد
🔹
سازمان راهداری و حمل‌ونقل جاده‌ای: تردد از مسیر جنوب به شمال محور چالوس و آزادراه تهران - شمال به دلیل تخلیه بار ترافیکی تا اطلاع بعدی ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/457371" target="_blank">📅 18:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457370">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">معاون وزیر دفاع: تولید سلاح‌های پرتوان بدون وقفه در کشور ادامه دارد
🔹
امیر سرتیپ شهرام: دشمن تصور می‌کرد با هدف قرار دادن چند نقطهٔ مرتبط با وزارت دفاع می‌تواند زنجیرهٔ تأمین نظامی کشور را قطع کند.
🔹
اما در عمل مشخص شد صنعت دفاعی ایران متکی به مجموعه‌ای گسترده از ظرفیت‌های صنعتی، دانشگاهی و دانش‌بنیان است.
🔹
امکانات دفاعی و نظامی از گلوگاه‌ها و نقاط حساس جابه‌جا شده بود و دشمن نتوانست حتی یک شهر موشکی ایران را شناسایی کند.
🔹
تولید سلاح‌های پرتوان در کشور بدون وقفه ادامه دارد و وقوع جنگ، انگیزه و ظرفیت تولید در صنایع دفاعی را به شکل چشمگیری افزایش داده است؛ به‌گونه‌ای که تولیدات دفاعی امروز با روندی صعودی و متفاوت از گذشته دنبال می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/457370" target="_blank">📅 18:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457369">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۴.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/457369" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۳.pdf</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/457369" target="_blank">📅 18:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457368">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv9akDEWnNUPhHZ6QEx_tvK41f4EnYxHN5gh6LMYZDZ1vj3jxbpQ0if3ejqp_PL9AEsPhzmGXzYP92FoannLk6JlocN0UbDPsBTfFjsbXdUGACxi1o_OCKESAkZz-BphY1Pn7JNhGfYAXCNCHbCzTO2PRtx1ObNTeoN9b0RRHteyXQJcMWi07aji0iU0Qf_NSMWYxVpFxv7wFSRUg5TAxjjFm4ofFZCRiDlvqfeHisSawcyvCwxCIcRKypzUNY_yYi2jpwnCmqZNvR6zIM45EEnXmKc4mh-bsjoUsx9XgUhsZY5gwcLRaD3iulI4CmcwTs7KuPysPKFIK1r_8grXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشگر سازمان ملل: ارتش اسرائیل بی‌اخلاق‌ترین ارتش جهان است
🔹
گزارشگر ویژهٔ سازمان ملل در امور فلسطین اعلام کرد که ارتش اسرائیل همچنان محاصرهٔ شهرک قصرة در کرانه باختری را در کنار شهرک‌نشینان صهیونیست ادامه می‌دهد و آب آن را نیز قطع کرده است.
🔹
آلبانیز گفت که حملات اسرائیل به نوار غزه از زمان آتش‌بس تاکنون به شهادت بیش از ۱۲۰۰ فلسطینی انجامیده است.
🔹
او در شبکهٔ اجتماعی ایکس نوشت که ارتش اسرائیل «بی‌اخلاقی‌ترین ارتش جهان» است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/457368" target="_blank">📅 17:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457361">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6Gp-401bWFlJWlAI9aJe6BJu6ddtK_rYSxdJEztm4eEeD9A_RSkVGnQichykPo-E6suKhDoV89HQO9ar8ySWqDF3X8Pjqfmphlg0S0N93C3sjncU_4A7J-TKpuZZFbYW6EBAX5wSo6sIWs0YIzBjPUGF2IITkhVUQAX1lB-I1s3o-SYRaJWvZp4_MK9rTjFPXklTeerhDXEcFrjZK-6qwjW02_YioHZeFsY1ERXiaSqiJBfEtCaxcHDjEbSNyJmTUmTlHf8Uvr3WtMPNxjna9oHbfadaf480d19y4rgPlzCj2AD4S5nKQpzcm4QzCMRD7E0gdK1wYaLzmQoRTC7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzR-DvSBro_wRfjUq702cU_OchDp0_hXzoHf9MJn8p-mUhHkXEwXtNodFXIBrdPhCdpa_uJu1Ew2D1CI5vY1ubXSGrorKQqV40qznoiAyV2tnDFTpjUZCEZCnsz3ns_PwE-RQQmfUOvZGrX0IWN8g-Zq5sR7uCF-ycesXMHASwI5o5Q4OUNhIYK5lMvVWwmzk8-VkqLejxNsWU_s-2_htXBks-V8uewylKIHUtbTEcBz6_L1k-QfsET6RqBrZ4zPgEEopJyNsLkwtnCYHp5VnV4Sa1xIftqtLYfMpufvxfl9inttDYBvjQ_ezz8CpJ9S2DUdL9CIO5ywVyIe94KwGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRe9IDfsfX3cdIEAMhdQpCOriBlMIVXwtXP4QtCU4KhR5MG_9kL8drwQ8AzOluMXINGsnci4os2DXs-YKxhgZz46tq4zmjfAfc2rSFk0uIIsg-1-E2jYFb1IfLRl9PHK2nJunno31re8wNOh2ZwvzURqmy-2jqZve640ElQbJr5sfPXXdo-d97iRMeA0wJR9l1tgLQxtIY7O_hJwZkCGTghHoxzQrwd3X9_XPr6EmR-b6jRmo20uH7KKG-gQC2tSTN8Q6iP-BoxfmgrBdqvxMH1FZrNz20Ij-GiskvDEl0oZLDsen5RXtgxgT1IyOJaac1NbXhBvLEoowlGyXcjyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV84bTdglGERJLZts89kKIk24u1PK210rucHuNMV8WPS49S9UL54ABfrXAL_TTPEYA9aGEov-ueFh_7CfEwC3nyT581iHBrhoag58nprHdI6Q-cAJAkRU4zIcUqmm4ibYHoAM02NzWC3_8NNsPgAEHbVVTuYzXpZWeVt4a6MGNlNUYEdO3pWxFdCp-NZqo7CDWwDcO7_RgCJKwHsnndKDBDdAnqGR_fzZwO67RMmHTKf9DoYkToeiPRZP4Xx4ddJmvllKpjp_8f5k2B06H31c7RZtRnOeNbVlD8Inv5Jgu1WpjMagnMzKtmsG4tmriA9p7oZddrZPxH6bKmS489sGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dm3aAN6xFnEEsCbVw7OB-i2CkKYinsq8e3TQ7UqxOigEz7e-VdfYyvr2s_sd0vGY7OS_8k-G_q4jUnTaKwQn93VffGddzPe61t9j-e3f5s-9oUOLs_DgaBz1d4zWptGMfzGnARjbxRtrShDH41Ym_Aaz0bTNMwn90i_NPtX4blvVz6gAFD-UYGFmHvr_B_PxmuCi1odrsBEoIwhMjYvq6vnbfd8hWPqGGyRPRjkkvtRaFJFMrRRSqomO39zbLHAFju_POjHhscmGiS9KRxHPo8ipa65MCCLehsrt0980yEUCAAPN25qX-NuvkgzrCWnEim8mwvlO_1kgPVC6V6il3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laL_9vw_C0HgU3ZBr0H2ZuCBEQ4r-K7loW0EXURmSkVGYwYKf5rPuji2n4LLqR8KlpvkAGWLWgS1LAdbteOL9accNNC7MNxYke5lKPKWsn3Ba1A9A2hus4nVGarbCcD-fNZyRq4bCxUgKXQpyEIybX2ehXmiteWcmcmVhD_e8DYipBWWRZFooN8PD9cVGig_bNkbGWI2h7vBqsHNo9zuGL80HaUS9HxKLNxnUsSAxn8W1dLhumzt1eh_D4qEQOg6QANcIr6gKqgdkExQSmDnOZPapsLIn24jdtU0KPxb5VyzcVl0ykxpB-rF9yt-r0ATKqvqAO6XkIaOVlS5Mof46g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQ7ZC-5fyvpciqZEFA1gLd5-NiJYaU4-mVl-fMhXNITwomj2BQVDw8y0nvz5zDKGpndHno56pq6FT5onbrWHmsVqBUHyideddINuwydTYDHjfJddVbAfTS_y_AxJvzYPzeYHaiLB6sLDBS_UTN9pbY8Rg4VhNh9n8D0vMzilPSs90V0M05nlLtFY7tkaUCFnIgo2bIXdjOXIbKds90T2UMo7WhUudiIbitazr6z_ucpPFcT54EWj3bIGX8JIzHcI8b_nE5KxstayUQOjcR3xan8FmPLe9f__M4jG42dcIAG9jQBRD-zQ88rmR8L3ZUBAC6Pz_biTuVPECABUvFVT4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
یمن تصاویر حمله به مزدوران سعودی را منتشر کرد  @Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/457361" target="_blank">📅 17:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457360">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06dc26b5e1.mp4?token=nqqX2J6K6_Au8x-rTF-yNuTPMYj3mXVKnHDzduyzfdUrzR2AcNKWaohCX1-uN1rZ9A9JWnq9ypz3QXX6YNspdDSaDaQtAkJNsnSImygykM6JkweSZcAPrX-ZpLTxyxFpo2NPJkgCgbWjYlAWY3sDCDoI4Syqm7RArwbn-AqkIijxioXuxFFYe54UBUUObtr7dRS3hy0B4OAWvfo9jdNwCaHEenl1JcxPcChCjwSkLUpyDxB7z6n6PIKIbuGPoX4AidaDUuMaJ5SwFWBTcVZTuZdKWbjmcELBiz4WhjRaPlnNYhPEM6IZQg_nHpB8fNjBecMhnPDrq7Vh6PbCBYyfFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06dc26b5e1.mp4?token=nqqX2J6K6_Au8x-rTF-yNuTPMYj3mXVKnHDzduyzfdUrzR2AcNKWaohCX1-uN1rZ9A9JWnq9ypz3QXX6YNspdDSaDaQtAkJNsnSImygykM6JkweSZcAPrX-ZpLTxyxFpo2NPJkgCgbWjYlAWY3sDCDoI4Syqm7RArwbn-AqkIijxioXuxFFYe54UBUUObtr7dRS3hy0B4OAWvfo9jdNwCaHEenl1JcxPcChCjwSkLUpyDxB7z6n6PIKIbuGPoX4AidaDUuMaJ5SwFWBTcVZTuZdKWbjmcELBiz4WhjRaPlnNYhPEM6IZQg_nHpB8fNjBecMhnPDrq7Vh6PbCBYyfFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتشار بیانات رهبر شهید انقلاب در جلسات روضهٔ‌ خصوصی شهادت امام حسن عسکری(ع) در سال‌های ۹۶، ۹۷ و ۱۴۰۲ برای اولین‌بار
@Farsna</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/457360" target="_blank">📅 17:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457359">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902f1c6279.mp4?token=D8F2MFSEyxh7xhdGTJuGhCUYTWkA8V-eowoZ28HNfD0PKOhaggL82ATUsM-TktcmRNx9iuW-K_dUPQc8U7DiKKF_zeS6HFe1iM5iAlivHMR2m6xnu2WNWlvWq_JaY5F33LDJrIQCeAYD2zA5l7N3YySEdm5DgCuJVezzA3pH2LqdvIoHtYNXJ1Sdo1fpR20wHQJLCYEpoB3fsGVcYr86BLok4zA8-CKsNadlKZPXclDt3QvOaKC8mVi2-X9ExDnkjbfjzDOMs9yjFYjfICkUFEURQ5OOoW0F_f9Z2koF-o7L-1eurq7dOpX4YVmsjAB0UqJbNxeWKLn6RyfIP5aiDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902f1c6279.mp4?token=D8F2MFSEyxh7xhdGTJuGhCUYTWkA8V-eowoZ28HNfD0PKOhaggL82ATUsM-TktcmRNx9iuW-K_dUPQc8U7DiKKF_zeS6HFe1iM5iAlivHMR2m6xnu2WNWlvWq_JaY5F33LDJrIQCeAYD2zA5l7N3YySEdm5DgCuJVezzA3pH2LqdvIoHtYNXJ1Sdo1fpR20wHQJLCYEpoB3fsGVcYr86BLok4zA8-CKsNadlKZPXclDt3QvOaKC8mVi2-X9ExDnkjbfjzDOMs9yjFYjfICkUFEURQ5OOoW0F_f9Z2koF-o7L-1eurq7dOpX4YVmsjAB0UqJbNxeWKLn6RyfIP5aiDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الهی نگردم من روسیاه؛ ز کویت جدا ایهاالعسکری
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/457359" target="_blank">📅 17:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbZP-atCe9zuII0tud3i8S61TWOF5fKtbzUeAFTKrPLQm4Dyr5N8lwATybHMr-lnd-XHcHf7fRb2zcs0fRJWTuxgKEPO9tQ6Z2gd-rMM42w8eQd4xvkUcRqIV1Xdq7LSqzTw3IS_h7tD738lwGzp2QDKDzSWlT714WHI4NUH9orEGZN7_j-9pfZy1qPlkHGOAeB-poytGiZlHIuYajyuJN3ZPN6LDdbOF9Zc2jOJLD1dNYvjf_HdhC9bU_nYuuEZ2xZPQ6GngsF6UDhXmypYUzYwBSoszpZAkPTs3xHYj5KECrQPbRdhZBG46IFLgz0OhRS4BgioIQM-6mmQ-tMEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از رواق دارالذکر حرم مطهر رضوی در ایام چهلم تدفین رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/457358" target="_blank">📅 17:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🎥
یمن تصاویر حمله به مزدوران سعودی را منتشر کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/457357" target="_blank">📅 16:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457356">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJAAxCfu1FoOfP3QqmuqH_EXeT5yl2VwHzL11shgiM0UGjpr-aV1xFLD2VOuolG6lZQT2FVPf86ViSwWxxUapj0qSVsfyYrVEDfgTqYMkKeBWVtTVjWuPizqiteQyRXgYPlizs83KfmdexwAydsNTza7xhBwTKAUplhWVjdFTOytSCIp-tYubS45HrUlHF-JY040Zca_XPysZiUOwZlzXP0Y8DcDw-uKPerP2e8TD6Uy8XrIFquhVPyzjtWbJCkVaXxTfbFBVzhHFgOixrU5wQ_-vw1kZcS7CiUne66-EaXOLFPojMr26EWtD62hpu0blLYD9-eyEbDpuwwjRVWoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکار بیرانوند برای حل مشکل سربازی
🔹
طبق گفته میثاقی در برنامه فوتبال برتر، علیرضا بیرانوند و امیرحسین حسین‌زاده، ۲ ملی‌پوش تراکتور از گزینه‌های تیم فوتبال امید ایران برای حضور در بازی‌های آسیایی ۲۰۲۶ ناگویا هستند.
🔹
حضور بیرانوند در ناگویا اما یک جنبه مهم…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/457356" target="_blank">📅 16:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHGd2V8K91I2RinRP1gLVsCcCm7G1QfPq2KQFzEPGszZKKlhsXhuJ1Lw_ngXAwfgvfveRZYmD4t27EbSCi8OiMqgOh7ixAFcvs151uSjJJc7jFsYWhZEro_b5YiBxe5P1ra0Hr60UPN5i3ybmzuGVHJz09LbbKsV8f9tQ1hDXujOkXi05fafoz0oQmhoFEIY_FqYbBQ1sDM9i-aOFD58oHVTwIUnqIocVfz9TFrJXFPoAKFpjw1I5OmZZ_z4Uh_3NjawsZf6YN-_wJjhozxMJmcYP0hK1p7ERDn-THy2K4k7n1YrFswIljCE6-r3Dz6Amob4uR1IzqlYF0qPmtivdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپلمات عمانی: تهدیدات ترامپ علیه عمان کم‌کم برای ما تکراری شده
🔹
نشریۀ عربی المانیتور به نقل از یک منبع عمانی نوشته: ما از اولین تهدید ترامپ به بمباران شوکه شدیم، اما تهدید جدید او با ناخشنودی مواجه شد.
🔹
در واقع، ما این موضوع را جدی نمی‌گیریم، مسقط کم‌کم به این حقیقت عادت کرده که چنین تهدیداتی تکرار می‌شوند و بارها و بارها شنیده می‌شوند.
🔹
روزنامۀ واشنگتن‌پست هم امروز در گزارشی نوشته تهدیدهای ترامپ علیه «کره‌جنوبی» و «عمان» نشانه‌ای از خشم روزافزون ترامپ است؛ چراکه او راه خروجی از جنگی که خود آغاز کرده نمی‌بیند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/457355" target="_blank">📅 15:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457354">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufbZ0kpLvphDMU7MG2U_he76Q6iXd9ck62ADB60p2zhabHbC1q7sejELwRQdOX1ApNxnS8KrG0dsyE7vi6pAe7cKLjDwgyaRbEEfqCik4nIbXdAb16BLHRKwh7m2cIWWgLs0wJ-7sBNDo1pPT5bpJQaeEwyb77VnBq9ey85quW2sHEq50YpuAVSf_yWfG_whSfb2K2kTqE8Q9SoqX40kemwBzpRi2B10SNNk6L2aFTcRW68-MarlbbQxP4485_nCT7rTXnDO_z1vov8RcPNHpf4YRILM1E5KHBNACClWb3q_v8d5igzfBiWAjQN65fGssHofrg9I3s0-hjKOYGyYzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر خزانه‌داری آمریکا: امروز شاهد افزایش ناگهانی قیمت نفت بودیم که من واقعاً دلیلش را نمی‌فهمم.
🔸
رئیس‌جمهور آمریکا امروز از تشدید اقدامات اقتصادی علیه ایران سخن گفته بود. @Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/457354" target="_blank">📅 15:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457352">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDxiztvOuT4purM8eUKLHXhDBKP1YVowqFd6_Jq2u7K4i9EGoOlVBuS8g7QHngsYys5M2uxUA91pqhrrwWfjLVsJ44FdRrhIxhNcqvh9sCWk73m2Ztk6M8RH0AgGulxWvdWWPoe6ZsSjEMHNdkFYOF1FeLMff_3KiDcXBkQXpS0-VCm3xtImapPG-4aZr2aaz6RB4sL1ja7tzN0eufa5IQvqTVxgLazTrw27YCBncxyvtrnZTU9bCU2WxIi1Ev3_uiPCNz3oHylGVsjGp9YNzGDFOqW-3tgBxvdCyuQ7HASzYZ0FJXvh-9ObI1VDN5sx4BKEb-7em6sSKNaZGt59RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور: چه کسی گفته دولت باید بنزین را ۱۳۰ هزار تومان بخرد و ۱۵۰۰ تومان بفروشد؟
🔹
برخی تحلیل‌ها و موضع‌گیری‌ها از تریبون‌های مختلف دربارۀ مسئلۀ بنزین غیرمنصفانه است.
🔹
جدا از بحث محدودیت‌های مالی، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومان بخرد و بعد آن…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457352" target="_blank">📅 15:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457351">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lULo-tdGsJXSOCPmutxJY03TD3-8J50Ux4E6CdA3ToojgzW9AfRDGDDTfqoHqhu-shEO-r4sbcFxrrylU1ypPStNqGo51_lj2FXpyDMXzYnaXcvqD45xbpUxl1C1HhUOOIcJYEcqCFWZ__LfLhoWoUHXa0o1yvBUCfb81saY1Y33VkNETle0wJw1f-6forbK1r4AWnXkYzsaGg7ccM5hKPNmEirET2u8TOeeGFRqzRpc-Pvl2JhTUxMybjUqQscc-aqImQkgmzE7O-K6NsD4L4mcwX7uxZ5hr4ZZEK49ke4chYqDypj9EsS6MPcTdONeHyn1-N2Y_sbw4x2fGlpr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب‌نشینی ترامپ از سیاست تعرفه‌ای خود به خاطر تورم
🔹
در حالی که کم‌تر از یک سال و نیم از وعده دونالد ترامپ به مردم آمریکا مبنی بر ایجاد شغل‌های بیش‌تر و رونق اقتصادی در پی اعمال و اعمال تعرفه‌های جدید بر کالاهای ورودی از شمار زیادی از کشورهای جهان، از جمله متحدان واشنگتن می‌گذرد، دولت او اکنون برای مهار افزایش قیمت مواد غذایی به افزایش واردات و کاهش موانع تعرفه‌ای روی آورده است.
🔹
رئیس‌جمهور آمریکا در پیامی در شبکه اجتماعی «تروث سوشال» نوشت: امروز توافقی را نهایی کردم که قیمت گوشت چرخ‌کرده را برای خانواده‌های زحمتکش آمریکایی به‌طور قابل‌توجهی کاهش خواهد داد.
🔹
در حالی که بیش‌از یک سال و هفت ماه از پایان ریاست‌جمهوری جو بایدن می‌گذرد، ترامپ ولی را مقصر قیمت کنونی گوشت در آمریکا دانست و نوشت: «همان‌طور که همه می‌دانند، در دوره ریاست‌جمهوری بایدن، قیمت گوشت گاو بیش‌ترین نرخ افزایش [در تاریخ] را داشت و تعداد دام‌های گاو در آمریکا به پایین‌ترین سطح خود در تاریخ معاصر رسید.»
🔹
ترامپ در ادامه اعلام کرد که دولت آمریکا طی ۹۰ روز آینده اجازه واردات بالغ بر ۳۰۰ هزار تن گوشت مورد استفاده برای تولید گوشت چرخ‌کرده را بدون اعمال تعرفه خارج از سهمیه وارداتی خواهد داد. وی افزود که بر اساس این توافق، به آمریکا تعهد داده شده است که گوشت وارداتی با قیمتی ۲۵ درصد پایین‌تر از قیمت فعلی بازار عرضه شود.
🔹
ترامپ گفت این توافق ضمن کاهش قیمت گوشت برای مصرف‌کنندگان آمریکایی، فرصت لازم برای افزایش دوباره جمعیت دام‌های گاو و حمایت از دامداران آمریکایی را فراهم خواهد کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/457351" target="_blank">📅 15:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457350">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXRgaREJYGUCErHw4jXFh9rJ23bTORuESCu58Z-NCEnhYMOQIsghf34MaFEdexyw5sYOEmFngb4OfFZJ90qbdZPlSvVUWkRgHFzOxONndont2VTEPQ8N24eA_384oE_ADERIA6G7u32-tsreJYMBSYjFVRG70FWNL4CwBy3ssK50l20WUkryo2KKLfitD3VRP_ExdEBgQP-Zn0-hIncsmHHt8poiFq2MLRYVJ874HY885LrOM7L361-22Oa_QYqPcePJgY_FldfnWsuFB3_5YN4CuHDaFeI7WDmum2tHS-QEWQ-gE54O9sw5e7EErertflo3LsxjlnOtZOYWtSGxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کسانی که دشمن را به تهاجم به ایران دعوت می‌کنند ایرانی نیستند
🔹
کسانی که در آن سوی مرزها نشسته‌اند و دشمن را به تهاجم به ایران دعوت می‌کنند که انسان از شنیدن آن شرم می‌کند، آن‌ها ایرانی نیستند.
🔹
اما کسانی که با تمام وجود چند ماه در خیابان‌ها ماندند…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/457350" target="_blank">📅 15:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457349">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2iAE24YoLmjT_XXQDGYa9CjyW-RtCcmWU4meqs6h3IKJhAH5rtmYUFEjwHtN5N8u8K9ZT9P2TFUDwgGZihS2KB4jTRlaUTMH0QvQ7hAyS5Vy1LWKLw0xnZefxzoJGT0nL0PohTH-npzYpLpnOatiznJlLJBhea31DduPjEwI86I-tksCSRqIcol985Lk5OuKUKnPC_enoVGWBXdyC9s11KPEV26aBlg9mhMcEkqeFZtLrGVOqvcQ1FlLKQEqcy2DlljXexUfihXZoc60D5xdgelD8x-1hR-S4oFklRFiMh_FfYdbX3y4O-0P_VTuYn4Xtjd7eMR8AE01uI0B1NCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی دولت: دربارۀ بنزین هنوز تصمیم نهایی اتخاذ نشده است
🔹
مطالب منتسب به دکتر عارف، معاون اول رئیس‌جمهور
دربارۀ تعیین قیمت ۸۰ هزار تومانی بنزین صحت ندارد و چنین عددی مبنای تصمیم‌گیری دولت نیست.
🔹
بررسی راهکارهای مدیریت مصرف سوخت، فرایندی کارشناسی و نیازمند توجه به آثار آن بر زندگی مردم است.
🔹
درصورت نهایی‌شدن هرگونه تصمیم در حوزۀ مدیریت مصرف سوخت، دولت جزئیات آن را با شفافیت با مردم در میان خواهد گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/457349" target="_blank">📅 15:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457348">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKV6bp9clMAaDj0ckUTQkF7a4Ra8ypl1fm3IOXXxazdFWBhchKSkyIONBT5FQib2qrk7F26fH89LdhcHHh_lAJicXuqJdw2qC8l9PhwnyLARK0K8NPgs18Zsz7Bdn6Q2YHIp4gi4E1ZDZXyD95-ByfDKUso2USCQu1xq9ZSHWAt1uVqSRMJ43eSk-FwOaOtZU08TPfqUzfcod55DQYAsBQhYeC6kOwA7tmaaBwGTrYba5T_2NKjfvFwqUQqwgEl_kKcP_ttfE8A3yLE9y8T3m51y8OA97pUf2gaWV-G36QPEuOiJJLB092AaRCMsIFET2e1ZQ_T0pjw75ZdJY65Jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کسانی که دشمن را به تهاجم به ایران دعوت می‌کنند ایرانی نیستند
🔹
کسانی که در آن سوی مرزها نشسته‌اند و دشمن را به تهاجم به ایران دعوت می‌کنند که انسان از شنیدن آن شرم می‌کند، آن‌ها ایرانی نیستند.
🔹
اما کسانی که با تمام وجود چند ماه در خیابان‌ها ماندند و نقشه دشمنان را خنثی کردند، شایسته قدردانی هستند.
🔹
همچنین کسانی که نیامدند اما با دشمن هم همکاری نکردند، شایسته قدردانی هستند. امیدوارم بتوانیم این وحدت را روزبه‌روز در کشور تقویت کنیم و متحد شویم.
🔹
دولت در تلاش است مشکلات را حل کند؛ در این مدت، به رغم همه مشکلات، دستاوردهای زیادی هم داشتیم که به آنها پرداخته نشد. منکر کمبودها و کاستی‌ها هم نیستیم، اما تلاش داریم با وفاق، کشور را پیش ببریم.
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/457348" target="_blank">📅 14:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457347">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4mxbnbGabQIPB2SxeDrkjwrqyxMRVAsY6mdIMdJsawlESMLLUbxW8jUyfkg6ofs5Lcy0dRxqNYJ2Fgv1EY6C9ebJsHGZD15El7SKLTmv54W-0B1ohXbGAYh4O6Ik7DSGtOT4ZWdKktxOvCbyVmFWl2AyjIqRDw_Wo0YZ5fdusiYFWxxqkvORcSsq24y9iTkzMz3aejSbDlhjKtSI63L_0AsyPV2jk9YQJWM8Ya5OFfgl75rbDCtVigZvBOkjinChKDVTJbIsKe4-beNXaAzjD8Mq3r1U84f7ZNiK5HM2pdL4rC65ervekyMuwFIaKpdpdJel60x8YcN6e4MSh4-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
از هر ۴ ایرانی، یک نفر «سرآشپز» را دیده اند؛ پربیننده‌ترین برنامه سرگرمی‌محور ایران در ماه‌های گذشته
🔹
طبق نظرسنجی یکی از مراکز معتبر از هر ۴ ایرانی، یک نفر بیننده برنامه «سرآشپز» است؛ آماری که این برنامه را به یکی از پربیننده‌ترین برنامه‌های شبکه سه تبدیل کرده است.
🔹
«سرآشپز» یک برنامه تلویزیونی در حوزه آشپزی و سرگرمی است که با ترکیب آموزش آشپزی، رقابت و فضای سرگرم‌کننده، توانسته تنها با پخش ۲۰ قسمت به چنین میزان مخاطبی دست پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/457347" target="_blank">📅 14:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457346">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6QaSs5ArHfIUF1oga6Oj_kCVLzDj1VzJSYsfWlAILLkklQEyVwbsYq0pbhO4pTYNAACUlo0upr0_e06lpwCpqeWeg4xIWEtWX0hlcrcRNmavQdJIP7svSDjqe8cfQKUJE8QdXq8_W3ohpXR07tp505hk-12FuzMZirNwxdPYDOlghhu6Y_iLUw9iKIMqJBo8jR4GwPL4IQQ6aLx52H9WcqEsjFGz0yArDgRxbDqaVGonV15MPdWJ02fRHOuOL6J-AzKjoM6oKoUhIHh35W_gh5ASraqhHpKhrdVg8Vbg73Y_RwRwTqWH46lBDcs7v-p5s-Y5sIEDPeLBDETIhFFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
👈
کانال رسمی ماز در تلگرام
✅
بزرگترین و معتبرترین موسسه آموزشی ایران
👈
از اول دبستان تا کنکور
🟣
برگزارکننده‌ آزمون‌ آزمایشی و کلاس‌های آنلاین در کشور
با بیش از 500 هزار شرکت‌کننده
✅
تجربی ریاضی انسانی
‼️
‼️
برای عضویت در کانال ماز
همین الان روی لینک زیر کلیک کنید
https://t.me/+vg_j4F-ZEBY2N2M0</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/457346" target="_blank">📅 14:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457345">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/457345" target="_blank">📅 14:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457344">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آتش‌سوزی‌های گسترده در اراضی کشاورزی سوریه توسط رژیم صهیونیستی
🔹
دیده‌بان حقوق بشر سوریه اعلام کرد درپی پرتاب منور توسط نیروهای رژیم اشغالگر، آتش‌سوزی گسترده‌ای در اراضی کشاورزی حومه شمالی قنیطره شعله‌ور شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/457344" target="_blank">📅 14:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457343">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WA-UqIWM7_aawTUgmBT6y-YXx9IV4DcjikoJ5SB3uqYsF1Sc81ddg3Hxl5rcIp61NA7dXI7y0toqSwsIuha7YSIVdiAh-D_ajo3eLH048m5PB2yI4TdWpQjVQmD2yWUrHKK16llBswQlycSK0HkeIFGLH2cDMGHPGBC__AdDdMFglDfMpcY6Ngf3m2Ew2s1SIlv-gKu8czzSDxDSxcGgSncqPNFPBiD1Y5SonxLB6TDV28vMl6nsCjwXAEY41bhh9PdKiSVqpZuEP0Tit1XdBSJD2tb2AQdTqHjwm3EmHgTWihRDICcIMNdF_EzokU9zsc6tb3-WFW2_guCcXF4NAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب جمعۀ تهران: با انسجام ملی از تنگناهای اقتصادی عبور خواهیم کرد
🔹
ابوترابی‌فرد: وحدت مثال زدنی قوای سه‌گانه، تلاش بی‌وقفه دولتمردان برای گشودن گره‌ها و همراهی بی‌نظیر ایرانیان در برون‌رفت از محدودیت‌ها فصل نوینی از وفاق ملی است.
🔹
با وحدت و انسجام ملی و پیوند مستحکم ملت-دولت از تنگناهای اقتصادی با قدرت عبور خواهیم کرد.
🔹
ملت ایران روزهای تلخ و شیرینی را سپری کرده اما با قامتی بلند و گام‌هایی استوار در کنار رزمندگان دلیر ارتش و سپاه ایستاده است.
🔹
آتش موشک‌ها و پهپادهای ارتش و سپاه توانست آتش جنگ‌افزارهای فوق‌مدرن ۲ قدرت اتمی جهان را خاموش کند و توازن قوا را به نفع ایران و محور مقاومت تغییر دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/457343" target="_blank">📅 14:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457342">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJA6MHG0oySEIEH9nXk3xI2hAjmTjPKKEbWP3ZXTURU-qNjVBFmlXid7jw0yJXOUqR1aBSz3gx2wI5Y0vXrf5-m2YGqEQd-lPUaPFrBIwJ-TRyKgrmqb61FZeLn0Kz2IEGM4EJZn-OQ8GsqkNVrFK9lEOQa4xBhT45cmE4eKqudmV0Z5OaVQtFAsywT_N6Bbmjt0voEqd11aEdllEnMaXfg2RpcTY6hoY4g33Yw4wQXDKYlZB-eW8cIygonr4-dEWg1q6QyDNqRKtUHCJdTAN5N8QbRkZ1s-WI5GE6VJl1IuFZeGwje8DQSDvpY3etOuCYMJ_7uYlwYV7yecyHDe3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: اقتصاد کره‌شمالی باوجود تحریم‌ها پیشرفت زیادی کرده
🔹
نشریۀ انگلیسی فایننشال‌تایمز ر گزارش نوشته:  اقتصاد کره شمالی، بالاخص در پیونگ‌یانگ پایتخت این کشور،در سال‌های گذشته پیشرفت قابل‌توجهی را تجربه کرده است.
🔹
عامل اصلی این رشد، تعمیق روابط نظامی کره‌شمالی با روسیه است؛ تخمین زده می‌شود که کره‌شمالی در ازای ارسال نیرو و تجهیزات برای حمایت از جنگ در اوکراین، تاکنون بین ۷.۷ تا ۱۴.۴ میلیارد دلار پول نقد و کالا دریافت کرده باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/457342" target="_blank">📅 14:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457341">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0gHBAqXP5hhXWExqqY0KwI52fh1TvB5q1XCe20e77e4AI8nMS64MfxeUvZqM5bzTKjplr-cwwvUKKuK5wOd_KyGmlpEDroXmnILa5dtYy_kRPW87-sKOmVrm0_LU1RKGI002n3HzxncJByoN3Tu9Z02z_VS7d2rxb0K9jLYxEL-HL0i61XDnyWv9_p2ZyEwngS22Jo7aUYow6qc0h3oIUJ0Nge9gLIbtMPr_K9X7Vu7BvpbDamftUaWn0ZB16FtkdYh7wpIGbUGliEDXHrrRzuMKyyw6HvOA-P_iGuj6tBhfYuPhYqU1G22w8k2z1bWWISr8oQtdB6Ty_4MPBnfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخالفت چین با جنگ اقتصادی آمریکا علیه ایران
🔹
وزارت خارجه چین امروز تصریح کرد که با تصمیم آمریکا برای اعمال آنچه که سخت‌ترین تحریم‌ها علیه ایران می‌داند، مخالف است.
🔹
شبکه «راشاتودی» به نقل از سخنگوی این وزارتخانه گزارش داد: «ما از طرف‌های درگیر می‌خواهیم که مسئولانه عمل کنند و از طریق ابزارهای سیاسی و دیپلماتیک به دنبال راه‌حل باشند».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/457341" target="_blank">📅 13:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457340">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JATAAq5Cm3aKIDQPOGZBz853ktR-AgC-AGMRvqZnggV7SOgfXxhAvaXaPAUO35exOZn7b_uuuvO87XvKyXc7Q2MzG8P-bF1fAgR3Z5s-dxc1qucDkAKNmdO4xBLeRQjfc7VA19hbDfOq3mSmotB1A47NkO_VoiK4P0Pxkwl78eBfoxA5O6UvPXKaMKGvPlh4KbdSPk92v0gIW5kTPTr2SmhiqZu0xfpu_ndz25n1q2yBCW2deqk6BdYx20Dw-PHEBba0izHi6tScFGfTgXj0YO7o0oxZgXUx5ionF4Eq_K3XozfwqT9q4DlLSXFGMaAY9aW_U_CbYGVRVt2oo7yalw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور قالیباف بر مزار شهید ابومهدی المهندس  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/457340" target="_blank">📅 13:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lfWe1_96VXT9oct6wc8UA71h_omsGKrrIjYZVyvi4l58SjlPfSh20y_j0u515YnV7LZL-Y6O7oBcI7rFJvxHoQJnVrsMARevZ7A6wAvC3LQhq2igNYTS_GqZEgQXfgfIH0IO93pKerEasusZQRbtUXPGU5FvM-OI0WNR3DSOlKPudf72eX66oI2YMyY4CrSdGo99VDQTZ-oRqBI2L3Jt6COkgrDkecZGzcla8JFcCXy2xpQy5O65DmS78IfN9eSkKRnYONtw8hJQm0XtMpi3VwHH2JqgvWkLJeuYh7Q_KCwouHfm8okCCxWeYUJqO-zs8bXY14vE9Dj77SewPbuDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kIFjs4rnqlFDvNed7RH1nO9XmWT7kuakn8RdIc6wKysxr887tRDoC0RzaLrMS0Pnw69SheKo3Vo2WMEATyt7Am02eQZmDGV33LiZ9YcMcAo7CWizbwX6742BLwOeN_-wr677VsFKsRl_MyCBUFwny_7LN9H5YZZYqQ6KrtMs0Pm1V0eqPWZ-HoeqtD_xmRByIfYZ9q9VrORY_OdGr3p3cr3GIyUuP9GVwsZeuqLXLVBhXaunV2-bD7kiLsTt2kduV0P8Ux7mVNmPDMEH8NzRN2SZ9KuxQYLReXiO4mNcAmzRyEwEoIA7XDI7jMLMKgcekrWr5ZUIpIA1TtwCTGfFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJIbOqXI5SisaHUZXJn2qNUGFDr-uOJAzbQqBtcJX7bEGOuCdLFbO4v8dO_bzcBFA6bAJsk_5q_Cb-HD1d6yhGDpghhLXS8H0XHIJskYwwiUqmZr0HBNHG1NwUYKhC68KDU55LvaQ-Yl9gsvcRKRlwqlMN0tSHGJAJQLluDRUZS47yV1tYo-IIZRreMgPy3vXn0tMz3WWRxErg02MiyHmKWCVAZs1Ts3hnugekU8IbAPUP_stJOoC6GRwhLHxcSkdwCRUP15-mOUX5smz9fhwrvqJ1-Mpz6XAAouYzDPITdVTcpV5EnCv477dliP7aqWANcRjwkDYeSbax50qCUnhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYVCz4OvnXS9DM_rjGo8S_QZ6dLU14pwNka9vL31E9v_huK0Ry7ekwreiSbvW6hbiqS0pVu8fugAZUQPZMS3A36KCUVHGSF_-qMVgCqbsZ1EG2NZr8xIB_-SyIBxvXG8O2AsL-geswo_G7uhVEcifeNBG06oiQRYnWPD4GsFriJY3FRwrlBmPkcxnBwtC5tkUyEdLeMpS_nTGFCfhYiCskfbbvga1sR6R_kxjNXpAymGxzSJCdFC6j43LO-ZNI9sw7ucyHYlqMivUDsV3Xfprr7U7b7_yHjepg1gFEp9eZTFgzV1sosJY-4C1f4Mtioy2bVoAdUNEw_0Jq-3oZf8gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJNG4DgmBDNIZ-yx8aDtTwTVsk46s28Cy4fx6_K2xdEPuvoVJpsHuX7YSiY_M_0P3t9JbimONXr7H4XFQqMQE-9rte6AC5GOQELLu09iK1MRgHroFUfiW-T9GZ1Sm4guH0ajO0GiZghIX-_qWOCD3WSqKw4NslYmHZzANC_LpYg52kLWeSaJuB2o-nxliFJLeXfW0d9En3bDa3FBhLlp8kiUFlrxeJNCCVz8dV7CcCstccJSbTrPIUqA-XquicrTpNQxE1Odj-8PbmwnkoGUl2YOAed7TJfT2NWChGEIu-Zdn6jLbe6fCPQ8ImTQo012iqqFBOgi0PusMXQI7p9uzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNuIq1b0nE_qaqyiBNfg-tHaxelGT8NewvLZa4G3rlYUDcMPp5X1fumwaPjLf1vfjihQTKtnFGQYUbpQBexz8sEH_Dq6GHQ3JmPhdJ9dGHyDC5OdHixI1OElT-nx8RL_CIahfDddXgoZYzM35mreKNDGF9rTXE7sos-3xaatM9xIJPCGy8pKjA--jDtj0WvAeBPvYyYAhxi-D38qS-4yLtKooCh6sYSQymfRu76O6BoBErj8eqfIBkuuXLAI_hm-YgFEQYKaPCcxOUo9VCz1MlZJoxpZ2X96jtTcOyCGdLJi50Woc11kgaZLVduC7BDGWcljf_aF2iS3fOLIM95xTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqVksu-x9Wz3c3zoG_KIykkdUwH9YS2boUKzF9EDNCzvQDZxg0D_QzLGsqXf1reO5g36RHZUFpKgT9kt9kf0Yho4X0iF1K5HjZwGw-chBr_Vba6TInEPA-_UZ6ZS5_naGaCeXnwqyGstqD0HjngxETIvS9RNJdLI782pIRxRcwdtw2LbyMl3aU6ixfu9m0qFbZ5rww72ygAXG8k3yK_nhqHsVcgcLZ0AdsZ_uuNM01KAnCJztPwKR0g2iSk0Jvj-vyR1_PSvFTqEWHCnHfhBeKNe-O1N8YgQ7scbEPPWK512dVLn_0D8kgSVhW8g5Yq2RAsPG28YEbus1acFhL475g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کنکور ۱۴۰۵ در سمنان
عکس:
محمدجواد فرخاری
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/457333" target="_blank">📅 12:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2636bdfb1.mp4?token=EokL_grxXwlJdbgJZ3rshCri7UMx8Oxr8Qs47cirs0LWCBNLFDyphngI0ycnxOxwjrOmOkw8SQhzx7BRZrbDR0vOLRIC0I85e8H5UpefNhEtL6Mm2cewuIINXjjrZynt142LuoJW62LfTAk-KQzP67wFKPVCnNWF98Fbwu0RYJhS865K8JuBMhrUnWCWxLhkZFxcTgTG69UKccMqNAv8LA9vislZhCU9WtZhk1fg8XKF72qSaQ4-kEqoMkqpkshc9bjjNMLoD-aTQHaDa70w4MJzqFEGHCTGQItAEC633NcrIMEY0rio0FxcUq1cP9PT7irWXISyaYrHa5iegceB7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2636bdfb1.mp4?token=EokL_grxXwlJdbgJZ3rshCri7UMx8Oxr8Qs47cirs0LWCBNLFDyphngI0ycnxOxwjrOmOkw8SQhzx7BRZrbDR0vOLRIC0I85e8H5UpefNhEtL6Mm2cewuIINXjjrZynt142LuoJW62LfTAk-KQzP67wFKPVCnNWF98Fbwu0RYJhS865K8JuBMhrUnWCWxLhkZFxcTgTG69UKccMqNAv8LA9vislZhCU9WtZhk1fg8XKF72qSaQ4-kEqoMkqpkshc9bjjNMLoD-aTQHaDa70w4MJzqFEGHCTGQItAEC633NcrIMEY0rio0FxcUq1cP9PT7irWXISyaYrHa5iegceB7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش موشکی-دریایی روسیه در جزایر مورد مناقشه با ژاپن
🔹
بعد از اولین سفر پوتین، رئیس جمهور روسیه به جزایر «کوریل» که مورد مناقشه با ژاپن است، ارتش روسیه امروز رزمایشی در این منطقه برگزار کرد.
🔹
این رزمایش با مشارکت یک زیردریایی هسته‌ای، یک رزم‌ناو و شلیک موشک‌های ضدکشتی باستیون در فاصلۀ بیش از ۳۰۰ کیلومتری انجام شد.
🔸
دولت ژاپن با اعتراض به این رزمایش گفته افزایش حضور نظامی روسیه در این جزایر غیرقابل‌قبول است و تمامیت ارضی ژاپن را نقض می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/457332" target="_blank">📅 11:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457330">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHyH97jBByL95DJ8qhzyTuv4AXpG23R5o4hUrJDWvetfYA8B_pVJ8kNV5mEBrImndSmyylV844IKcH_8spXi30_4t_qK7y2YvbcVB5avoR9J_2WTJkzOkyMG4nMZ3mzTphxmgf28ez0zdp_WEqhJRTcEXyGteeZPZcbbah5zc08fpfaPW0l4lstNteXqf6o9hgNrWFEiGClUlZ-4IKd3ow9GREf2QC0pdLXWXQsZz1odZ6L2N0YmPPdnEoeQnGUiH78VUnqIBK9xf9W0fP-WDR56EpSgF2FPAy8uld8oghauvxJi31p_GgFPYWDXmLeHTWWaBvv1i-g7kd7gj_R4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePA9Q3OK6DYlN1dCQgq6d4hHfqPEgeq_CqJV9xAzSEe2cR74A5iCS_s2yTdmR7Ixfc-NarX0C4btS-o1DCJPWaTvwm6JNgFHy8SCOvSFPSDheZqVlOL02GdDth4NcCmIB2eBMPW9F_fxyQU-UEwMNovjsnAN6kBuPiX5Wcxxc2FUZsq1p4mF8GAWHPnp597sI5ucrLs2igT61XmHa3nwaRuqDQf2MXjUI3R65O-k2sxfA22gFSlggkpn9RMtzvmk8OMr3NPMHNCF6105mw_NgUn-anozS4zDwDbY84O53_ku4Rwb_PE8NdkTe7Sj81z9XypVENLX1ng9xNvkR734WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دست نوشته قالیباف در دفتر یادبود عتبۀ حسینی
🔹
در قطعه‌ای از بهشت و محل ریخته‌شدن خون مطهرترین بندگان مجاهد راه حق و حقیقت، در فضای آکنده از عطر آسمانی ملائک، از دردانه اهل‌بیت(ع) طلب می‌کنم که آخرین برگ زندگی مرا با شهادت رقم بزند و به کاروان دوستان عزیزم که بسیار دلتنگ ایشان هستم و امام شهید انقلاب، مرا ملحق نماید. ان‌شاءالله.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/457330" target="_blank">📅 11:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457329">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNB6ItkF0HG5F71RDETWJ1MW8nziJC3bgfCxE5MrudEiTP_LCH-X0iTgDqaqWlWrCb4_5adXu7_EovIaV7n0baG0ZkrlCqGEV1JG9lQGSXiQivu3sMz3K0GtgU9WDkagJRlaJgT_10pJ0cVSpzfjWILvve_5Lg317GRpANYVHBYV26XrGHm9tlnL0cyUhDgPtYe-NahfnIA77xzaiwVzQABVEG-RdEl4A7NmGpShGaVYWG6HT3ZM7KrKhSvoEHNW8Z2SXzuTXZZ5Y8dMowoQbamnssT_9HQUtaU-FrYye9qJGVb_damvxgMSfwDb2eoIHf_6m7APqWjgwmeFh0sTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور قالیباف بر مزار شهید ابومهدی المهندس  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/457329" target="_blank">📅 11:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457328">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBr5g-xKXEq1LMTAVn2_zXIK1m8WEM9ruZ4C9ic-oq6FoA8ejjEYma3iQo_6bQ3ROrwOIEmc7cn3qcM8t-QTagBGk5LYLOYq2utHYmVYHOGILksbo54uJx--Vs7tJGUXB2QB2v9O6fCxRCxewp9S5NYKnXjQL8HhUCByi12KvZbabdP2barK-5-Kn7Byqj2nkV_SP6oxnuzaX-DdYt-OcZktsTG5LmVDQ_0qFTR9XPFGb6hOJvTowEmApf2PosJmthSvsR8RLXuOL_IZyMoSns4QLimyWi7gppok0-c3ATaZ12gzBFP632Ootn9l6uUl6AiXp9DVOO-iylHsCJhhLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: پاسخ ایران به تهدیدات نوین دشمن ویرانگر خواهد بود
🔹
رئیس ستاد کل نیروهای مسلح: آن‌چه در سال‌های گذشته در وزارت دفاع رقم خورده، فراتر از تولید تجهیزات نظامی و یک «انقلاب صنعتی دفاعی بازدارنده» است.
🔹
نیروهای مسلح جمهوری اسلامی ایران با آمادگی همه‌جانبه هوشمند و روزآمد در تمامی عرصه‌های زمینی، دریایی، هوایی، پدافندی، فضایی و سایبری، هرگونه خطای محاسباتی و تهدیدات متعارف و نوین دشمنان را با پاسخ های انقلابی، کوبنده، پشیمان‌‌کننده و ویرانگر مواجه خواهند ساخت.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/457328" target="_blank">📅 11:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457327">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCIB52lRB8ZFW_h28CYqjETDcM8qcp_5uVGUCjZiVzdk2jJugbUxvAD80D-Xx4qg5PW-S5tOe2cjMTRY8C0_u5c38apftd5X8_mDJjTw3hGv2gWhKztsONLOssudg5hwYSZx52MJhn5b8p3JA0c1nwu6-Ju6jCr54c9sPohCetqx0wHO1ESnUQDcsJ8tbXaJ65FfeYcetUGIYQirNueS_G-OVybXIXCX585IvCkLdHWA-QMTbVswgoYheaaLd8_WbnV1PrDsz2VcEXWwr7MNTyaKpqhZqS8E3foM93OBm13TSZ5FEhGrYwOm0c-4rAU8dDxUeEEjKs5IQhCA5K1XTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تجلیل قالیباف از خانواده شهدای مقاومت عراق در حملات سعودی-آمریکایی  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457327" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457326">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
تجلیل قالیباف از خانواده شهدای مقاومت عراق در حملات سعودی-آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/457326" target="_blank">📅 10:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457324">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLiJ6hLQimphIBU5l2ZKj0CwnFkZZ1nKqLCAl9P39VXfXX__sVOri6xwdxpZvawbj7FJY9HQnZZdI-fijY-aIrKyBio1cV4WooeMh-KY4S9KkZhdmEJ1QTUxapWNPH91OLyIq0MLq2oTtc1NJhVSef4CueerK-Uw-0NzmskhJX7jbcHvLE2bRd23e2MQ1Yqn3X3YfM4KaSvYTF_PmRU2mZu7aRWGcpcj18jiM2aLjH80rtiDQmO9TyckL3-_18YiuAWBuE13ptrufrI7agK5S8_05Udl1ycysb_cZuX2cMOD1l4g3Nv9HBxNMw78l-IuKkrgdXTllFKSk-YXxVRyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NosdPi6jy3zkvpLYsZmq7AxRMF9t_PMAJ9_dT9YcAioAdW3xnVX23SMsKprJMq4sHV-A4tA4WsVvY1ZPGAxDbfxZxxMFP2BFuvGiPRFkZNxJriwEFGra4hhBTLDije9OTBF6Ce5Zm2wTsDXqghwLlZUo4HqKgNm4oyFlrbuGrR7GQBDOy9JlfqF-w-pEO_CDFrgQdr7YYLcuGh4id6VWMLlWWbrDoLhZLX1MJL8FHuTNbF_94cLC4EZL2JdhBPBjQbxMwJggVgUyGRGiuRYauhiVX0gS0MRh8ZqLSRzw1-NKIBOX0WCzoMo14-dE4opcpoHjalAZSyVR2dLVDbN33w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حمله پهپادی اوکراین به یک پالایشگاه نفت در روسیه
🔹
پهپادهای اوکراینی صبح امروز پالایشگاه نفت لوکایول در شهر «پرم» در فاصله ۱۵۰۰ کیلومتری عمق خاک روسیه را هدف قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/457324" target="_blank">📅 10:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457323">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5pgKIh67wXrMCMOM741Hqugz2ozC4eKdC2_mRomRTxfyeZNRvGU4LzmKXBueNhUo_PJXYtv6mxKxnqCs6Nudm-Y-Hls_sH2n8OGnlT5BNFiNyNQ1FVLmgXb9lAPR1Hpt0q2q9llSIM4NaQKZpnoeAmYrmIKRLz4iU2Ufat7B-GYxjVE74UNBM2hE_BBsR_37i16IPfWKO2G8apO9ruZLOMPfxbakUJXl4-4gP8VC7vq9T98CjVrvc1jdenF6-YUymWm1XjMD_q8A4W4tURFWqFB6tgmG_4S0ppKcBAAHNeBgtNeTX_pgrHVf8EH6yKS5I_sqIRb0bcFGIReTykP2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به جنوب لبنان
🔹
منابع محلی امروز از شنیده‌شدن صدای چند انفجار در جنوب لبنان خبر دادند.
🔹
المیادین در خبری فوری گزارش داد که چند منطقه در جنوب لبنان هدف حملات نظامیان صهیونیست قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/457323" target="_blank">📅 10:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457318">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOO70BVa7ZuHsirBE3K82a52ZhWnN3KheCOsz1TS3Kd4rs6k6itfnTTXk27fg7FXYSN7Ws9vZpOiODF3pAKQxfnwYWhsxSS9qW7HKjgHmkhWj_SgMF1SLhptdRa60K-hVQo0jByC04SCfK0mF9zV4mwJRqJbP9nQaVSChz6qpsZJp_93OxKPY-XqqOMK11K1lZ0rQnT-9mXWW40YFNvxSm8vYJ0ZkY0FgZyQTZbtTmFWR7G6b94IqPY3eDLjFEzmwN5_gR2RzjuxFWvpp8g_yeNlxh94ffvlUzXXJtE15Lv5EqH3Vz86vbRDcrOBYRIcudo_UmNlAVvCGR-JeN7wBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQoiS9H7ENogkOuTHpZ72iTEpruvHQJaDHuKaEb-s7zdADimWtdvRIynX_HHXgeW-SZM5GPXpxMQRLHA3PR7_RfXBpmZNGEfIkd57yYoKuclmM2yk1ZCRitV0k2w5yCRSzNFHHIm677aRaTZ8lBzEAnrjqhaYxNg7WAp1mhZpQL2Q_fUlQZy1TZ_cJVsvfs_CxjZQbSPVTZQxFnDbcLVZlLgPFRHAIGUts2gvRzFAkuaS7UcU_zN1bPdg9TTaDeHUtSDdhEw5HnwqCzHxpI40EgF0HcT7jl4g7Tn9CMfJCcQxGV2IGDT3M4BFiVibHEWu08gn6tza8uezNz1KbQ70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKB2a2pOiVZPhLYowEzTN9pphYnOcIa8Sojm73RDbve6CYqAD63rbifkEiSTsJI7KKKuuD6KYgl5F7ixydUI11OcvEZbWkAkewX_AY_Nb7zXejeFhfLpan5qjk2dgBHeHKAIDWYzIfFwsA-dtbpa_B_zARVYchcbqsn5aXBSm27L4gkO5FBBbDTg0pc7e3pXoyKKmYiINStGtBuSztJMJS3cTNavxF2uGldLe9nkBv7mwge9pVg2VIrbzeQnMhmk7YTMEBPxc4KjPyQjhy5I33m4GZt2Txz2TNi1ekGPnJzjF01lfoZikMpuyK5mJbWv-t6gRiF63-aCWAXJK94CAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bv5vJDaDX_hwFX2NERU4qSJZzSXYYQGsLfbGCaNJ8otcOTcSFHftW5j08ulDyp1OOtkKpZTHelTNL_OZxjT8FfF2TaZLPfxvjN3S4js1UfZ0NB9aVx4H5ELztkW3fsW5WKG-vba-aAoHCayFK08tJELYRpoFl2ElSX4Sbq830ZNATBzlscKg5CRZ6NiTsUPTWTYsp2nwy5hu4yGSzgqxPlzb2Gbk6_yBKIBrmTNa9iRmacs8y0RztqkRUA-sdmehSufBxa_fWael8oQk9PGSDJALe72skY6YM8ENf8KNxuBViLcLwjHn4SUbyu5oC1CevCl8-WAsAbdJNcPoj4rzDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzQu3p75cL1D2V-Jg1aginqQF-leE4WXX2uRFmEE4gbnt9du4v8CEBCu82g2HNrbpdv4C-sz4jlFOIEujGVQebeNSb1VNTY4CDYpI8XVMYWoXsE_JIb4ZPurnnc8GXVWmbReaRkVknbR21XJsmvbo9f0fNNt1Ij8GnrlPgIWSfqWX5SejbaeRUyelLSiegU-i95oYoAC2pC78fp77-b16E2FpxKbb8YkE7tSkQp__BzN78nZGB88KaxKLs3booZvxsE5TL7abMz64Zx8Gjpq8D4PnnoP9qMO5TOFmdVxJmavFsY1jGO9TldH3I7S_hoc_ZJnsNronU78u7eAzApxGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پرچم سرخ انتقام بر دستان مردم کرمانشاه، در اربعین تدفین امام شهید  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/457318" target="_blank">📅 10:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457317">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4q21kFj5bcHqjGISCdxfDllkKO0d5x0snx1Ap6VRl8SLbhdAEGpVtX8n54w9fcijeyzKNzXm_6r44pSYcIE7A-C88VXkxAu9jDxuf2Yg0FIwVKK_BUiR4Z46E572PRdDlQbYoGg_hA95UTAnhw77F3oKXXye15hIfU_i5hz6GnyaTtyi6Dsi5ChN6k889tYO5pv2abskKzAcoXDyc_DlhO6AVIGrQ03LpQxKvesaO_oY7Xq2dMgPBtnpgfwBpa_egM1uubDdRppxmOHT8ITVl_SO7BVY8E3ZYsujIaham4hIyF2dzX494cbnk6v9tGH0CxS6gzGXPLKe-CXR_EAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل در تدارک ضربه به ترکیه بدون درگیری با ناتو
🔹
پایگاه خبری اسرائیل هیوم گزارش داده که سران اسرائیل درحال برنامه ریزی برای ضربه‌زدن به ترکیه هستند؛ به گونه‌ای که ناتو بهانۀ کافی برای حمایت‌نکردن از آنکارا را داشته باشد.
🔹
محاسبات راهبردی اسرائیل بر این فرض استوار است که نیروهای ترکیه‌ای مستقر در سوریه، درصورت هدف قرار گرفتن، به‌طور خودکار تحت پوشش تضمین‌های دفاع جمعی ناتو قرار نمی‌گیرند.
🔸
این گزارش در شرایطی منتشر شده که دفتر نتانیاهو مدعی شده سوریه با استقرار نیروهای ترکیه در پایگاه هوایی ابوالظهور در آستانۀ نقض توافق‌های امنیتی خود با اسرائیل قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457317" target="_blank">📅 10:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457316">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE5vYaVFiARV6ViZTtzk3rzS2bUIA-wj-S75Tvcl3CQ3M8HgUPBCDWfc0gko5ZwKpYaAQcBdTfZbCQPlOvT0uxbyN45b2NWXqf8eClkue9P3DvwypfjV7KZ4iKnBOBAX6OQUJ0ZrMiaeUelOEq-ewDqXXjnQJb89P5Yaa4KSs_YtbszxKolgQuMKBoG7piuGX5xCsAe55o_WXJzgxvhO86kkTp6Ko1MXp-U3B2zJLzVxWXLBdeTmUyl4mOJtR2KeI2-G54cTFqSpPHHIasQQbmRgiYbTac0Gy2H16mb_oRvz465zzm-02iJ6_WDuqmVb5yAGJmpctVk5sB7YI-Oh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ ۸ نفر در حادثۀ سقوط هواپیمای آمریکایی در آلاسکا
🔹
یک فروند هواپیمای چارتر «سسنا ۴۴۱» که حامل ۸ سرنشین بود در غرب ایالت آلاسکای آمریکا سقوط کرد.
🔹
خبرگزاری آسوشیتدپرس به نقل از ارتش آمریکا اعلام کرده که هر ۸ سرنشین این هواپیما جان خود را از دست داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/457316" target="_blank">📅 09:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457315">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e78c9036.mp4?token=dBZJXzoYNW-KZTBDo_qDy36tXxaC2Ziynszk60TtCX4lKcsN3QpJZQzYw78CUAbNscpcoQFjBaCE1bvPLUAwtIywdRGTcLx_qLbSe3atQmfsJzppbp7zNxhTOiJshBuDAD00a3ajES09cKO8viCr1Ez1ukpqy35bfH_ItCXwHP__yhhdqwjYCxTm3002qc1HscbzlaB28PG_I19WK3u9QdsaUS_O-SiXg-YSAIO_ijpQ87z5qXvrO39WIBq4otwHUkHaxsQg0WeZRLOYB0ihuFZ01vKB0q5DN4Qy4E5QaHSu0z_y4nl9nigSwaoWtEpnKGMx17blZ7dcRKe9BbWGZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e78c9036.mp4?token=dBZJXzoYNW-KZTBDo_qDy36tXxaC2Ziynszk60TtCX4lKcsN3QpJZQzYw78CUAbNscpcoQFjBaCE1bvPLUAwtIywdRGTcLx_qLbSe3atQmfsJzppbp7zNxhTOiJshBuDAD00a3ajES09cKO8viCr1Ez1ukpqy35bfH_ItCXwHP__yhhdqwjYCxTm3002qc1HscbzlaB28PG_I19WK3u9QdsaUS_O-SiXg-YSAIO_ijpQ87z5qXvrO39WIBq4otwHUkHaxsQg0WeZRLOYB0ihuFZ01vKB0q5DN4Qy4E5QaHSu0z_y4nl9nigSwaoWtEpnKGMx17blZ7dcRKe9BbWGZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خسرو معتضد: این خانم مسئول پوشک ترامپ است!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/457315" target="_blank">📅 09:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457314">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozK6wcq5eOaxtAsRQmyBzeR2MAHGTXYdW8Ezskzz9Bre-c15HPjcyOJPwokWFyDIimWfuuXTDQWXZL-rc61IykLqQKe_aGqPMSZKM0iAZo-WAlhPLuxHQwwYA4iiTuiIkEkxmZ08I92i8dPx8AnzjH0BubQ_3UqnyqA2_SYeUd--CPwf0xaySH0V9367LODgsPrGVhf7MuyKu9bgMGvJZVSmgc2DkyNPHAWtYTmqzzAzbpGDBppDLKRT2ATqcHWWMQ07iEP-axHE-L9Y5k0tBcVRStJabE62kiR0EOsnAn5y5qSm-KGUcD0OIJqc1X50egVF6o5yItRqipRvpuMCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جانشین اینفانتینو از آسیا می‌آید؟
⚽️
رویترز گزارش داده که یوفا، ای‌‌اف‌سی و کونکاکاف درحال بررسی استفاده از سازوکار  «رأی عدم اعتماد» برای برکناری جیانی اینفانتینو هستند.
⚽️
زدوبند اینفانتینو با ترامپ و پرونده فساد اخلاقی‌اش باعث از دست دادن اعتماد بیش از ٧٠ درصد اعضای فیفا شده است.
⚽️
اگر اینفانتینو برکنار شود، طبق اساسنامه باسابقه‌ترین معاون فیفا تا برگزاری انتخابات جدید سرپرست ریاست خواهد شد؛ این فرد درحال‌حاضر شیخ سلمان، رئیس AFC است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/457314" target="_blank">📅 08:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457313">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌ آغاز کنکور ۱۴۰۵
🔹
آزمون تجربی صبح امروز، هنر و زبان‌های خارجی بعدازظهر امروز و ریاضی، فنی و انسانی صبح فردا برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/457313" target="_blank">📅 07:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457312">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هوای تهران ناسالم شد
🔹
بر اساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای امروز پایتخت روی عدد ۱۰۴ و در وضعیت ناسالم برای گروه‌های حساس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/457312" target="_blank">📅 07:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457311">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/457311" target="_blank">📅 06:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457309">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b985c5d06.mp4?token=cJNqeYLhSUdjyPvr1uWYU5UNu9EuHLO6Pws6w9DEVFe4zSg0tAy8eSy1Pyz6rnoCg6i0QlVX0RS--qfK6Qlzf1WYnYkp_4kK0bmj9T8oCfJbHcEH0MlRk6CXMHPuRFUISvPtAOGwQiNbJSXCeYgWElDTYJQjWirjQP3yVpp08Pw_OStpFmkc0bvPnfb215tlYRu2NmIPpmPp6v8QBmgA1Nykg8c8wt_y1Upzysv7vccdqWmOhIJ5a1IXIADDtqCCkjdOofu3uff2WmiJQNUIZXEsOBTYYECKPZQeokbcbSmhBeX2x5xpnF0JKFX89f07GAy5ig-OYn0M-0XAZnVGx7g8TmJ80oFJbdJcrly2UXskJKcc-uwNBbw4h2V8njhhv56PxBnnUNgO3K_dY2b6sArIg4TPKe-56W_MTJPQxLHNTE-JV6stEnmNoRRjDPgpcwHLLRnUopvYFE-GrwjXevEDZmg4EUYMcLTYBPppY1Mh5ThvazYG57cTMzUZUo2WWTO7TAOVB39PR-wLz39PC9SBWfxGUkfHFrDK3zly49XL7wcRPp62KwMWA5a8j7m8ebeeSeiYYF6kWOoSP8KoG3qLQi9kkPSkcrkHUWxVDBYUo-mRPIEyH2OxjuH3j_NtNCAbfBPEFFruH13NvOYjJRFC3N068fMHhLOalfudd0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b985c5d06.mp4?token=cJNqeYLhSUdjyPvr1uWYU5UNu9EuHLO6Pws6w9DEVFe4zSg0tAy8eSy1Pyz6rnoCg6i0QlVX0RS--qfK6Qlzf1WYnYkp_4kK0bmj9T8oCfJbHcEH0MlRk6CXMHPuRFUISvPtAOGwQiNbJSXCeYgWElDTYJQjWirjQP3yVpp08Pw_OStpFmkc0bvPnfb215tlYRu2NmIPpmPp6v8QBmgA1Nykg8c8wt_y1Upzysv7vccdqWmOhIJ5a1IXIADDtqCCkjdOofu3uff2WmiJQNUIZXEsOBTYYECKPZQeokbcbSmhBeX2x5xpnF0JKFX89f07GAy5ig-OYn0M-0XAZnVGx7g8TmJ80oFJbdJcrly2UXskJKcc-uwNBbw4h2V8njhhv56PxBnnUNgO3K_dY2b6sArIg4TPKe-56W_MTJPQxLHNTE-JV6stEnmNoRRjDPgpcwHLLRnUopvYFE-GrwjXevEDZmg4EUYMcLTYBPppY1Mh5ThvazYG57cTMzUZUo2WWTO7TAOVB39PR-wLz39PC9SBWfxGUkfHFrDK3zly49XL7wcRPp62KwMWA5a8j7m8ebeeSeiYYF6kWOoSP8KoG3qLQi9kkPSkcrkHUWxVDBYUo-mRPIEyH2OxjuH3j_NtNCAbfBPEFFruH13NvOYjJRFC3N068fMHhLOalfudd0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی منتشر نشده از دیدارهای صمیمانۀ خانواده‌های معظم شهدا با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/457309" target="_blank">📅 06:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457307">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWsugOXzC9v3oqiR0BGQHvyZU80EhCAzFypFtms-rvAIItY65gBRu-_it3LNm9NC6QaFFwY29Y20sx-8_dDq0TKeTw8IxActuuYh1MGQJbTj2EcRqyWo81HXoBjGlK-JmLQticlsKeZHTybiiDZvfdR4f2XgVTrnmVjqiNbt7BX7AAMkvsyTh3P4kLL373EL2983OmI47F7ADdtxk9aasx9KP5k4sw1ystEXT8-fRVWnEORzCtCk-gRWmjPtIlQ7_XugnMS1NPgFTRydeOYbBZMjDCNCdkInNVnEKYH1mtJjZG84WdGz4_dLu1k526QtKZk612cn3zZ_G6hQr8yErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام روس: فشار حداکثری علیه ایران راه به جایی نمی‌برد
🔹
میخائیل اولیانوف، نمایندۀ دائم روسیه در سازمان‌های بین‌المللی مستقر در وین به ترامپ یادآوری کرد که فشارهای اقتصادی او علیه ایران همانند دور اول ریاست‌جمهوری‌اش راه به جایی نخواهد برد.
🔹
او نوشت، ایران برای دهه‌ها تحت تحریم‌های آمریکا باقی‌مانده است. تهران در دورۀ نخست ریاست‌جمهوری ترامپ توانایی خود را در ایستادگی در برابر فشار حداکثری نشان داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/457307" target="_blank">📅 04:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457306">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512caf8e7c.mp4?token=QhdQ2QM1JldCGaMrGrPC6r756INTf15BQ7uThVfUaxgUXFiDDzO8MpziCbEXpYwcC_TfgkyDcP103YbJ3zMTOKZ61jv2juhXO-igHc-Q_7QBKRyiLt_6nm_tjb9LZl8n5MBXfsUVMrfVZjQq-1nKJy7Z4jpwwFZ3CveytOFu-gyyWhhNWGeNnJjqmkpnCmbeFwCuLcuFTDTTcrGlJNyhogYamr-e1OleZYQv-2A_bfljNi0Y4r1LWYXAkS8LMpDXLBmBECgw0AezI4xFqwziSCOKI1mwaL_j5pKZIQrEIwWq6t8btCAvdsbm3XsoIN5MYGSm_YIfrkR25fKV1nSOsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512caf8e7c.mp4?token=QhdQ2QM1JldCGaMrGrPC6r756INTf15BQ7uThVfUaxgUXFiDDzO8MpziCbEXpYwcC_TfgkyDcP103YbJ3zMTOKZ61jv2juhXO-igHc-Q_7QBKRyiLt_6nm_tjb9LZl8n5MBXfsUVMrfVZjQq-1nKJy7Z4jpwwFZ3CveytOFu-gyyWhhNWGeNnJjqmkpnCmbeFwCuLcuFTDTTcrGlJNyhogYamr-e1OleZYQv-2A_bfljNi0Y4r1LWYXAkS8LMpDXLBmBECgw0AezI4xFqwziSCOKI1mwaL_j5pKZIQrEIwWq6t8btCAvdsbm3XsoIN5MYGSm_YIfrkR25fKV1nSOsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چقدر چاره‌ساز مومنان هستی؟
🎙
استاد عالی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/457306" target="_blank">📅 04:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457304">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e851ace3fc.mp4?token=HuXeQOcQBOLCY_Moa5ghImGZw34OmM7FivpIIjuL6k4ERd5v80D2N4ndyQJ3KJ2U0f92lvFCPuJ0CUnZ0fC5AkLWCoRTtjSYuUlZqk0zFb8jbW25KQejkEh5VtIjELwNe3BEwRRzQTkIAodpnQ7C_4YqnBv9gSSBMzTexbn8HgE_ThOMEyp2QCmFoGeHcq7_u7rOBqgSK3km8pWbDa68815DYBLiUNWmbAbbhTuURlpdWXz4CHMh7ojTtuZ-kls8XchZ_iRQQ9OQ_60piXvmMvMuHRFHIBtOM7_zomcW3vdiM5M5sHErkVvmf_PsXXG1b3ktkibOKicISiRUpjdbaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e851ace3fc.mp4?token=HuXeQOcQBOLCY_Moa5ghImGZw34OmM7FivpIIjuL6k4ERd5v80D2N4ndyQJ3KJ2U0f92lvFCPuJ0CUnZ0fC5AkLWCoRTtjSYuUlZqk0zFb8jbW25KQejkEh5VtIjELwNe3BEwRRzQTkIAodpnQ7C_4YqnBv9gSSBMzTexbn8HgE_ThOMEyp2QCmFoGeHcq7_u7rOBqgSK3km8pWbDa68815DYBLiUNWmbAbbhTuURlpdWXz4CHMh7ojTtuZ-kls8XchZ_iRQQ9OQ_60piXvmMvMuHRFHIBtOM7_zomcW3vdiM5M5sHErkVvmf_PsXXG1b3ktkibOKicISiRUpjdbaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ورود جنگنده‌های رژیم صهیونیستی به حریم هوایی لبنان
🔹
رسانه‌های بین‌المللی گزارش داده‌اند جنگنده‌های اسرائیل بار دیگر وارد حریم هوایی جنوب لبنان شدند.   @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/457304" target="_blank">📅 03:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457303">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366444aced.mp4?token=a5Y_fwfEh2j2F7gdjdaOhxPCr5fiCBheTyuSBCMdsYWSk-6XXG1LNesgKC1POY5FIyTz8sTEuzOPnHIfGL3jidY0vsJbtCh9Wv5x622YrFjjWXkD1K2TWBvDNLoYePOjbcjmA0fSe9MuljnZw7yCVNbvqqNcIQLbWerhm96XBgb1CQt-6TUfhywV7LM5ZhsKa9jEGHUQmN2TyDlHN_5D2ejME35zG47rF4o7qcWeARmuI_S_sfWvxZbwdp7DU9yF3jRutNPJtUnPVLypCmNCGAdFQZGwW2H_gxQnlKBRFj--REwactPdpLNkcQj2vgXNwICncyYsJ1viXfj5azEGUA6KNEm5HexXbUg0usjyYHxQEdnDREVOQj792MRCD_um7sLA6Zq5r7lV7SkqEgPJx2_2FqwBbMxXQ0aO0rUbs_MYpJPT7zSN63on44pEUvkHUaz8YKFC5ai8qvu6DMoZJsfbK1Nv8bhOlrBVHiO7EsdBQEphRZFIzvZ5WUftrspruo8K9ThoyeV3cUuYgjviUUjmOECgeS9m_wz5fFEGUZUkB93jCptZR31Oh6R2GeoOd-LAIwhIMnuniwoX6yPkOYQNYcZ3zaQgzk1dlC_eL7HbnH4bQZzcS4eodWsbnsQnC1sRChEYpUDBzzhgLzQK9fxKEIvBFtEOhZexLI1FPpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366444aced.mp4?token=a5Y_fwfEh2j2F7gdjdaOhxPCr5fiCBheTyuSBCMdsYWSk-6XXG1LNesgKC1POY5FIyTz8sTEuzOPnHIfGL3jidY0vsJbtCh9Wv5x622YrFjjWXkD1K2TWBvDNLoYePOjbcjmA0fSe9MuljnZw7yCVNbvqqNcIQLbWerhm96XBgb1CQt-6TUfhywV7LM5ZhsKa9jEGHUQmN2TyDlHN_5D2ejME35zG47rF4o7qcWeARmuI_S_sfWvxZbwdp7DU9yF3jRutNPJtUnPVLypCmNCGAdFQZGwW2H_gxQnlKBRFj--REwactPdpLNkcQj2vgXNwICncyYsJ1viXfj5azEGUA6KNEm5HexXbUg0usjyYHxQEdnDREVOQj792MRCD_um7sLA6Zq5r7lV7SkqEgPJx2_2FqwBbMxXQ0aO0rUbs_MYpJPT7zSN63on44pEUvkHUaz8YKFC5ai8qvu6DMoZJsfbK1Nv8bhOlrBVHiO7EsdBQEphRZFIzvZ5WUftrspruo8K9ThoyeV3cUuYgjviUUjmOECgeS9m_wz5fFEGUZUkB93jCptZR31Oh6R2GeoOd-LAIwhIMnuniwoX6yPkOYQNYcZ3zaQgzk1dlC_eL7HbnH4bQZzcS4eodWsbnsQnC1sRChEYpUDBzzhgLzQK9fxKEIvBFtEOhZexLI1FPpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غوغای همدانی‌ها در شب ۱۷۳ حضور در میدان، با حضور ابوذر روحی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/457303" target="_blank">📅 03:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457302">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3723379f5.mp4?token=vj9A5GR3r9UIwYtppBvcFoWINxny0HtNO6LvW7z1TEyJ1nFuWZm43DVqmQJIl0YBS4l1VyRwhg66slr9rxOfjnyICl76NCeK2AAEU58FHEbseXF1lewSI2utbq4KlQbLtvoj7OTFRHFCxkJEaJjUn02suu1qxYs_DlNp0xxGH9bYC5ucPfEPGQaiz57Cntjx6KxO1T8BBkWsOqP0eZ52nBqnLkDIfku_Rw-x6t-UBoRQm11NuDE82t_75aXtv_7OecqmOB61hb6ntULs9bDDb9770VlORQJpPUFyYoJgWeP40OXhqOWLvYRdEVZoLd9NQ729ZHNHPAuIf3kdDm5A6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3723379f5.mp4?token=vj9A5GR3r9UIwYtppBvcFoWINxny0HtNO6LvW7z1TEyJ1nFuWZm43DVqmQJIl0YBS4l1VyRwhg66slr9rxOfjnyICl76NCeK2AAEU58FHEbseXF1lewSI2utbq4KlQbLtvoj7OTFRHFCxkJEaJjUn02suu1qxYs_DlNp0xxGH9bYC5ucPfEPGQaiz57Cntjx6KxO1T8BBkWsOqP0eZ52nBqnLkDIfku_Rw-x6t-UBoRQm11NuDE82t_75aXtv_7OecqmOB61hb6ntULs9bDDb9770VlORQJpPUFyYoJgWeP40OXhqOWLvYRdEVZoLd9NQ729ZHNHPAuIf3kdDm5A6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرقۀ قالیباف از حرم امام حسین(ع) با شعار مرگ بر آمریکا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/457302" target="_blank">📅 02:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457301">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehn8Wehl2j8t64TnXvBjV6vgLUbU8auNjgADPt1jhXz5h4X7ms95pH7iprQA_JuihBf64D8WbCCJZwkph0GNYQg45m4sdQHtsN-0P_t5yny7YrZjedk2GzID3My7X-Wa57cvwi0kj9SoDpHmatwOJa2aK08MydsloXaJqTSlS_uAZyCszpOkGDZQ1mGSLZPnZw6TkzhA4DYol7fKQUAx2s-O2AOfu0uQidPVEWi6gcg6a2EHohq60mWL2YW9BWbqa2oscHp1iPzxNQKUWGwW5-gUtxn59T7C1rWmAZ6qugfb_wC6Cfv1VaeXs7d3FSlftqIbqb4v1ruj7UPTCvxLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هم‌اکنون؛ حال‌وهوای مزار رهبر شهید انقلاب در رواق دارالذکر حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/457301" target="_blank">📅 02:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457300">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83cc33636.mp4?token=TnHALfZTPNcOmKgDgWC85TSyWQRAiMd5DzEyNa0doOM3zN1SFiOPCOikE9s0kVYUeIaaQ_cGcuHGynLlLpYnZPG2Yt3GcyHVft9xe0qaMoh6JTUVaaWkqWOwNcQdv93FQbnbXQEIpKCMVc_0MMcspWfv5kd1A633VofOMKVzVgpj9HetVoSLefQO_zL1ib9MK5T5u2N3cGW3abDOhVuMOuDkDuPzgafxWTHdXz_NU4A-H7P73QDZjiJoFljGQz0m5VLd_orW2V7xhzl3CIMpHspbi_31jmza1zfTEBDgjaVF5BfShe0428cvRpmTSj8YW_gvRydrgAr-U1KjXLeDoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83cc33636.mp4?token=TnHALfZTPNcOmKgDgWC85TSyWQRAiMd5DzEyNa0doOM3zN1SFiOPCOikE9s0kVYUeIaaQ_cGcuHGynLlLpYnZPG2Yt3GcyHVft9xe0qaMoh6JTUVaaWkqWOwNcQdv93FQbnbXQEIpKCMVc_0MMcspWfv5kd1A633VofOMKVzVgpj9HetVoSLefQO_zL1ib9MK5T5u2N3cGW3abDOhVuMOuDkDuPzgafxWTHdXz_NU4A-H7P73QDZjiJoFljGQz0m5VLd_orW2V7xhzl3CIMpHspbi_31jmza1zfTEBDgjaVF5BfShe0428cvRpmTSj8YW_gvRydrgAr-U1KjXLeDoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفاع ترامپ از حمله به ایران در میانه افزایش خشم عمومی از جنگ ناکام
رئیس‌جمهور آمریکا:
🔹
چاره دیگری نداشتیم. اگر صد بار دیگر هم لازم بود این کار را انجام می‌دادم. آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند.»
🔹
ایران به کشورهایی مانند عربستان سعودی، قطر، امارات، کویت و بحرین که تا حدی بی‌طرف بودند حمله کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/457300" target="_blank">📅 02:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457299">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQEwGz_1TJu1khwCqZJR_YICCbMt-nrJQecf9Hwkg8D7g0vd7U_KzJycQ2z0JDmaaQAJKN-ceNHymmdsyuEZfiXdxen5PWY8uBCb3ON3Ap4DAFNyZcA0-P3aMve6pOtwM-YPnF5px5apYM-_okdVLcJooNazxjn7foNDVOkKIj3dTYE3CgpPX-mOeC71eLllXjYHYIG_bzyFic1RLcks-mXsBKt3T5If7eNv6Y7PvDQzZRZs84FHszrEoA7XLtoW4Q6wCxZwsvNARtOEGKSQOjDy6-jWUcJJoe3rZoSywlR9WYqNbfxXGJq1J1WU5-4s-0rehuOuP1nAHacjF4GCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نون بیار کباب ببر در نمایش خانگی برای عادی‌سازی لمس نامحرم
🔹
انتشار نوزدهمین قسمت از برنامه «در جام» به عنوان محصول اختصاصی پلتفرم نمایش خانگی نماوا که اجرای آن را مهیار حسن، بلاگر اینستاگرامی برعهده دارد، حاشیه تازه‌ای را به وجود آورده است.
🔹
مهمان قسمت جدید این برنامه، السا فیروزآذر (خواهرزاده تهمینه میلانی) بازیگر سینماست. در بخشی از این قسمت، فیروزآذر از مجری می‌خواهد که با او نون بیار کباب ببر بازی کند و مهیار حسن نیز در کمال حیرت این کار را انجام می‌دهد.
🔹
به نظر می‌رسد «در جام» تنها نام و هویت خود را از جام جهانی به عاریه گرفته است؛ چه اینکه از ابتدا تا امروز، به جای تمرکز بر فوتبال و حواشی آن، کوشیده است با دعوت از چهره‌های شناخته‌شده به‌ویژه بازیگران زن، حاشیه‌هایی از این دست بسازد.
🔹
بروز حاشیه‌های این‌چنینی در بستر نمایش خانگی، بار دیگر لزوم نظارت هرچه جدی‌تر ساترا بر محتوای عرضه‌شده از سوی پلتفرم‌ها را برجسته می‌سازد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/457299" target="_blank">📅 01:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457298">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1265e6e7a1.mp4?token=NpOnKXimYmLyQHTY4wo06tPKw-X6vzEFJw9nZJt43cWWsMwFj8Y10AgtyDZXSEvHQa12cC44E1NNxnBTxnT7718puBtEqKtCBGffAvxEGL4CZTPM3BIbqJ0MNBlMPEAtDYWIBHrW3hU3MCd-NWmbSBipwmBoQ-XHWl5SmzOOnedHjYKMLxy9eUDOtoI_l-RmO4sGXUYTwzlNip21Ha0Eb-j8-j7uYOdVToDtJs2NtiyyfRt_VUi5lxL50CiDBv-juZm-BAHjD9bGxlrhvay22wflQHY4G7d6n5Ip1ZLObDACqxD4Kqs0quCncqzw116RJdQFaB8NoaUWnuR3TH-SjlGELKnnQIv8PB7vSS59EpVMuXCda-KAvuWixRWxUpkiJZuQ7d3wiTS5q8JCWr5UqfDEfVGgaUmxHCrgljrwjCqAt-AV6kSzcX-ell-3v0ew5IyFoeHYd5sIlN8bxVyyArzpBwYpaJPogVjN8Zye8JtQwUUomQipiEla6tzfZqYDdn5JcvEnVH7kKOcVc_OO2lS3GvWjRVULcEQdmhqd92l9Qy_vYxzvIplsoUFB2niJHYaaLFSV-pjLpFwbIIrGKwGRZ6Ia4Pw9APdjA-XrLEsdjFg9riNKXcKrVm5lh0WU9TYwnJDswB7cVGn_9wjJ1E0bToZnX8WvroVPC4GHcFM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1265e6e7a1.mp4?token=NpOnKXimYmLyQHTY4wo06tPKw-X6vzEFJw9nZJt43cWWsMwFj8Y10AgtyDZXSEvHQa12cC44E1NNxnBTxnT7718puBtEqKtCBGffAvxEGL4CZTPM3BIbqJ0MNBlMPEAtDYWIBHrW3hU3MCd-NWmbSBipwmBoQ-XHWl5SmzOOnedHjYKMLxy9eUDOtoI_l-RmO4sGXUYTwzlNip21Ha0Eb-j8-j7uYOdVToDtJs2NtiyyfRt_VUi5lxL50CiDBv-juZm-BAHjD9bGxlrhvay22wflQHY4G7d6n5Ip1ZLObDACqxD4Kqs0quCncqzw116RJdQFaB8NoaUWnuR3TH-SjlGELKnnQIv8PB7vSS59EpVMuXCda-KAvuWixRWxUpkiJZuQ7d3wiTS5q8JCWr5UqfDEfVGgaUmxHCrgljrwjCqAt-AV6kSzcX-ell-3v0ew5IyFoeHYd5sIlN8bxVyyArzpBwYpaJPogVjN8Zye8JtQwUUomQipiEla6tzfZqYDdn5JcvEnVH7kKOcVc_OO2lS3GvWjRVULcEQdmhqd92l9Qy_vYxzvIplsoUFB2niJHYaaLFSV-pjLpFwbIIrGKwGRZ6Ia4Pw9APdjA-XrLEsdjFg9riNKXcKrVm5lh0WU9TYwnJDswB7cVGn_9wjJ1E0bToZnX8WvroVPC4GHcFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرزوی حاج قاسم برای حرم امامین عسکرین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/457298" target="_blank">📅 01:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457297">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkSQ5MlvqdYjPTW0hVsHa4f3-_ynHqZkjQ0RmWk_7TZBjZjvP87LosBB4-e40XHRea948drjPsxHJEaLv0aDhJqeen5ZlCeTZfJ68P1_3r5kO0-dz1MZ1MCKk4IfaeunQBMGFm1Be3GJ8OWQ8oLY10iwF2RNLeDCcls15t6YGfw8BA4sXS0Mfoo8tyVpUagL_QRrdzP9Wv63dJPsza9Uf6JFhnWxOjBQp1Y0QB6hLr0T7LAoVD-_w6bZA6XILNZ-devst-39Zvyvv637lbLnGEEe6_SfMHqikBLUm28s0WESUmxMyYZd39sthRG2vUzU9VDJ9ywfodZtN8jWvDyfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکار بیرانوند برای حل مشکل سربازی
🔹
طبق گفته میثاقی در برنامه فوتبال برتر، علیرضا بیرانوند و امیرحسین حسین‌زاده، ۲ ملی‌پوش تراکتور از گزینه‌های تیم فوتبال امید ایران برای حضور در بازی‌های آسیایی ۲۰۲۶ ناگویا هستند.
🔹
حضور بیرانوند در ناگویا اما یک جنبه مهم دیگر هم دارد. مهدی علی‌نژاد، دبیرکل کمیته ملی المپیک اعلام کرده مدال‌آوران بازی‌های آسیایی در صورت مشمول بودن، فارغ از رنگ مدال، طبق قانون «سرباز قهرمان» از خدمت سربازی معاف می‌شوند.
🔹
به‌این‌ترتیب، در صورت قطعی‌شدن حضور بیرانوند در تیم امید، کسب مدال توسط شاگردان حسین عبدی می‌تواند برای دروازه‌بان تراکتور اتفاقی ویژه باشد. چراکه او در سال‌های اخیر بارها با بحث وضعیت نظام‌وظیفه‌اش مواجه بوده و حالا حضور و کسب مدال در ناگویا می‌تواند به نقطه پایان این پرونده برای بیرانوند تبدیل شود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/457297" target="_blank">📅 00:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457296">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfGoqV2mw16JdxDzFrXDpLQdRmlJsl7cmiOF18aPJZWq7Fw3sAgnXPi21oYBE8mBk5abk5uGCmBSbNQbngqIWtMgl10FA1qBCfQn_GaRDoVZoZSujiwLz0jl7G0hYjT10y2WEQpQthh3xlzDMcmH1QbAVbC6Q8KLwVqbnAnKWglTTpXosihnILORK37eIEO6L334wAXzVHXyEEbYBUmfC3-ZPBK2wFHKGZT98aJeSd_3eTh3pk1UlJl8eH57l0sjeIBQRT-lR5bpbrjhekBU9Jn1Z2huhFXh7ckKNgZKmvD_SvVC3Ov6bFP9qxGwwUV_L-rqeNAqUnMq4Uj60D4xww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: ایران مصمم است که مثل کارتر، ترامپ را نیز تحقیر کند
🔹
ترامپ چهارشنبه مدعی شد که «مُهلک‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است» را علیه ایران اعمال می‌کند.
🔹
اما سی‌ان‌ان تأکید کرد که رویکرد جدید او، تاحدودی راهی برای حفظ وجهۀ خود پس از شکست در وادار کردن ایران به تسلیم از طریق حملات نظامی، یا ترغیب ایران به مذاکرۀ هسته‌ای از طریق تفاهم‌نامه است.
🔹
سی‌ان‌ان افزود که این تازه‌ترین «چرخش گیج‌کننده» ترامپ در درگیری‌ای است که آن‌قدر تغییرات تاکتیکی و تغییر مسیر به خود دیده که شمارش آن‌ها تقریباً غیرممکن است.
🔸
اما بسیاری از تحلیلگران تردید دارند که تهران در درگیری‌های کنونی در برابر آمریکا عقب‌نشینی کند. ایران دهه‌ها فشار اقتصادی از جمله شدیدترین تحریم‌های جهان را تحمل کرده است.
🔹
این شبکۀ آمریکایی گفت، ایران می‌داند که ترامپ تنها حدود دوماه با انتخابات میان‌دوره‌ای آمریکا فاصله دارد و به نظر می‌رسد مصمم است همان‌طور که رئیس‌جمهور اسبق آمریکا جیمی کارتر را پیش از انتخابات ریاست‌جمهوری ۱۹۸۰ تحقیر کرد، ترامپ را نیز کاملاً تحقیر کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/457296" target="_blank">📅 00:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457295">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش‌ها از حملۀ هوایی اسرائیل به ارتفاعات علی‌الطاهر در جنوب لبنان حکایت دارند.   @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/457295" target="_blank">📅 00:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457294">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش‌ها از حملۀ هوایی اسرائیل به ارتفاعات علی‌الطاهر در جنوب لبنان حکایت دارند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/457294" target="_blank">📅 00:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457293">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2fa9c666.mp4?token=JDicpo7mPuX-IbQmZOLgwiT-I-KMZWr0_WQaA9Rw2v1poiT35emGzV9GMi3fn8N7cjHHMvGF4i7j67Iv2jjZC-_sHtWWSjJNNn9G0n0Pg8E_K-QifuU6YxA9CCBRSbQBXokzoi4gUBqhnAEvReujqJD2yBAfvMH5EY46r1qepcOBBShqOzofh2udssvK2OL3Pno_IA3lSbrQeSmDSCdXEIOL1oL1CjdUXo_kto_cP-Tpx5z8gWFy6eA7OWa_sB7Diu-_TV1iIIznnZmuoDLtRQh5kXX96Hrs7qsSu28CI3NhjR67huj-Q8flJGmgIhmd3F00Omyd0CNiqm770UB1-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2fa9c666.mp4?token=JDicpo7mPuX-IbQmZOLgwiT-I-KMZWr0_WQaA9Rw2v1poiT35emGzV9GMi3fn8N7cjHHMvGF4i7j67Iv2jjZC-_sHtWWSjJNNn9G0n0Pg8E_K-QifuU6YxA9CCBRSbQBXokzoi4gUBqhnAEvReujqJD2yBAfvMH5EY46r1qepcOBBShqOzofh2udssvK2OL3Pno_IA3lSbrQeSmDSCdXEIOL1oL1CjdUXo_kto_cP-Tpx5z8gWFy6eA7OWa_sB7Diu-_TV1iIIznnZmuoDLtRQh5kXX96Hrs7qsSu28CI3NhjR67huj-Q8flJGmgIhmd3F00Omyd0CNiqm770UB1-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم سرخ انتقام بر دستان مردم کرمانشاه، در اربعین تدفین امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/457293" target="_blank">📅 00:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457292">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بازی تراکتور و پرسپولیس بدون تماشاگر است
🔹
سخنگوی سازمان لیگ فوتبال ایران: با توجه به آخرین استعلام از ارکان قضایی فدراسیون دیدار تراکتور و پرسپولیس در هفتهٔ سوم لیگ برتر بدون تماشاگر برگزار می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/457292" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457291">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe5d1196d.mp4?token=AmJukHeDRZ1yDKA6JQ-anDzOAjQ35XoLVotvX_4njZvUjwG_qVnaniiYivG9fWNo7C8CTLs9P546JmYkPe7qUrhD5zJ3ir51Bpge6btx2Ps2_25fdf01IHA6qnYZcAAvfHFI8v_37G7CKx20UUHd_0cuI0E9VOvf5WtKem6fHF61obo0V513l2ppcl4uHVO6I6wngUPj5BKu0TH5Koz9QIF8fJndpO0A5_KC32b387n0CmBz7_Y4ZAqEU4FxJJaREH5Xx-bFBugweeA1S6TAgo4OXrOxo7wMvk7ofytT7-5Mr0JUd3QYT6gqSV9v0HM90pstOLx7Vsz1JUos-gOnL4ZR-VwAyCmly0oNvjRqMupUAzMrPsp2OEGp0TeBYmFmSm-oHiegkDOkf6AIOUlvMPoReQKvHixc32RHodWOYoS8SpQm-SiiwjlaD9K-IVGNQqDZ_bB_B8kHeFDjk8Rzm0JWYjjStSVzRbcAx0TZp_GqE5e3ZWTOR6gYPIU3c_rDfMQvZ8SgKxRoiMcjowZrv6OfikRulDvfUE0Hso2-SFEKiav7GSGOdNpHMMxSqtHjQEEEWS8I0NiHGYuiJP-Hkv6dE8_HnSmVyuh3ShSX6AGcz3x6HoALzQtDLjEmS75P6A1ghYwn0uYcZqeROxiwjIGm_gv5N8wOIrpbDWduLNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe5d1196d.mp4?token=AmJukHeDRZ1yDKA6JQ-anDzOAjQ35XoLVotvX_4njZvUjwG_qVnaniiYivG9fWNo7C8CTLs9P546JmYkPe7qUrhD5zJ3ir51Bpge6btx2Ps2_25fdf01IHA6qnYZcAAvfHFI8v_37G7CKx20UUHd_0cuI0E9VOvf5WtKem6fHF61obo0V513l2ppcl4uHVO6I6wngUPj5BKu0TH5Koz9QIF8fJndpO0A5_KC32b387n0CmBz7_Y4ZAqEU4FxJJaREH5Xx-bFBugweeA1S6TAgo4OXrOxo7wMvk7ofytT7-5Mr0JUd3QYT6gqSV9v0HM90pstOLx7Vsz1JUos-gOnL4ZR-VwAyCmly0oNvjRqMupUAzMrPsp2OEGp0TeBYmFmSm-oHiegkDOkf6AIOUlvMPoReQKvHixc32RHodWOYoS8SpQm-SiiwjlaD9K-IVGNQqDZ_bB_B8kHeFDjk8Rzm0JWYjjStSVzRbcAx0TZp_GqE5e3ZWTOR6gYPIU3c_rDfMQvZ8SgKxRoiMcjowZrv6OfikRulDvfUE0Hso2-SFEKiav7GSGOdNpHMMxSqtHjQEEEWS8I0NiHGYuiJP-Hkv6dE8_HnSmVyuh3ShSX6AGcz3x6HoALzQtDLjEmS75P6A1ghYwn0uYcZqeROxiwjIGm_gv5N8wOIrpbDWduLNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۳ شب ایستادگی در خیابان‌های شیراز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/457291" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5a2cab7d7.mp4?token=Y6p5yNEb7AFf5kc_-0KgJBVrNaZyz45BmlAkdqip4EL_NOG-L3GIDunhO0SJtESoPQI59fhTp3ffC_9xHenNzrd6YGl670Cp_3ylRhimppsi_Qw_MwvFVVDa7tY9nu8hYbCNgwLa-1RwQeK49bNOoVMQt8Qe_LTiGnmHGZfmWWDuIjIAoPkwgePniY9HYyEUttX3s6uL3b70Maj7rML6xY-GLaWanD_UQwELencu1qmWXifmSyFbM_yeqCAChn02Bcg1zDtdgRBlZCItpToIZ9JtNSo2oYiHJfHtc9novP3FdoaXmaQgetPK_Wl1I9LMouzqSVT0IM5WWiY_Z9nE9Jp1wRdfmxNEcmComlVTFMOqIt0AxbccY6KCC90a91b5joiALplKG9fKuHGlHltOoO7p2R_Aj1beyks3adN71nYTuaCdXzDKEBpZRx0u3bk8Qdqedbt6rcI6omZfj612lizixUtd8nLeDx_Zrzdke4rLbRj8uvuydsb51Qaqzm2k5Y2AlqXCvIy3CgYFn2bVS0cC_Smb2_UoIUdZ7m-5BSBJoyxsEBbVbkJi4ebnKXvCLSVSCbgRAdtaacvjEOZTf17ugNezMW8NO1Zl3wLrc-3qox0WrGTyxCGEbwc9nJfxtc-L9DY9XpLZBoLZsbkgu3qpQJncpYzsfmkLp5_AQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5a2cab7d7.mp4?token=Y6p5yNEb7AFf5kc_-0KgJBVrNaZyz45BmlAkdqip4EL_NOG-L3GIDunhO0SJtESoPQI59fhTp3ffC_9xHenNzrd6YGl670Cp_3ylRhimppsi_Qw_MwvFVVDa7tY9nu8hYbCNgwLa-1RwQeK49bNOoVMQt8Qe_LTiGnmHGZfmWWDuIjIAoPkwgePniY9HYyEUttX3s6uL3b70Maj7rML6xY-GLaWanD_UQwELencu1qmWXifmSyFbM_yeqCAChn02Bcg1zDtdgRBlZCItpToIZ9JtNSo2oYiHJfHtc9novP3FdoaXmaQgetPK_Wl1I9LMouzqSVT0IM5WWiY_Z9nE9Jp1wRdfmxNEcmComlVTFMOqIt0AxbccY6KCC90a91b5joiALplKG9fKuHGlHltOoO7p2R_Aj1beyks3adN71nYTuaCdXzDKEBpZRx0u3bk8Qdqedbt6rcI6omZfj612lizixUtd8nLeDx_Zrzdke4rLbRj8uvuydsb51Qaqzm2k5Y2AlqXCvIy3CgYFn2bVS0cC_Smb2_UoIUdZ7m-5BSBJoyxsEBbVbkJi4ebnKXvCLSVSCbgRAdtaacvjEOZTf17ugNezMW8NO1Zl3wLrc-3qox0WrGTyxCGEbwc9nJfxtc-L9DY9XpLZBoLZsbkgu3qpQJncpYzsfmkLp5_AQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی تراکتور و پرسپولیس بدون تماشاگر است
🔹
سخنگوی سازمان لیگ فوتبال ایران: با توجه به آخرین استعلام از ارکان قضایی فدراسیون دیدار تراکتور و پرسپولیس در هفتهٔ سوم لیگ برتر بدون تماشاگر برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/457290" target="_blank">📅 23:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418ad869a4.mp4?token=SeceZI2SpP74lLkpPu_5zj06wsbvfNU-ELf72Bbj0_9HzU2o8uG5mv3NA0k3J6husXA_-84iaVhFPL0UQFnBkVBkMLhf7a-0wrC8-gPWFQP2rJkCeYzEsejPjy0iATLY944MyjyzJKhm_RnwPMTMqbY268CA70w_0jiTg-so7-onLyR1L2YCCPyoMb61J9rdjvubFb0P5uASEK2_pc4Tne2C7pEZa-y0Q3TwUX2thET0WkBGdbAQSHlXmFx7x7Y0WdgSZNGiRf3RpP8vrIF5gIBWafmbFy2bLjf0kfFXKKMjhaB939rM-9EScDZSUdFBtagFv20YJA1WwTHgHVLxtikWSu-xI2spfK1UzgwSabFutNXJBJ8z73bw73dJc_eeI7hqKr97rIxCBu7zN6blhph2-M8hhoEMTOzquBO5yfTshg_6m2TNkrKI_NOwm0f6TXnLyFKuDhwGOWFM0BUGIjFJn-JMB9TgYJBbK5bHhaKRLdU0aaGI7mT666rSh1Vlmqo2HT6sbv1_vRFP1CzaO00HgfWt-InE6Hq9VRwwpjXdug8OMFiBgfzFvPbzT3VZHXM58Yt34J1tcXi1WGzaaXTaVd0Me_llv4GJ2nz_2zZV0_PrjmdRn23wWSNvsd3Ql9FcbvqLDLiu_8udrPf2DGJfPhLgbplTf0T2SRpK_rM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418ad869a4.mp4?token=SeceZI2SpP74lLkpPu_5zj06wsbvfNU-ELf72Bbj0_9HzU2o8uG5mv3NA0k3J6husXA_-84iaVhFPL0UQFnBkVBkMLhf7a-0wrC8-gPWFQP2rJkCeYzEsejPjy0iATLY944MyjyzJKhm_RnwPMTMqbY268CA70w_0jiTg-so7-onLyR1L2YCCPyoMb61J9rdjvubFb0P5uASEK2_pc4Tne2C7pEZa-y0Q3TwUX2thET0WkBGdbAQSHlXmFx7x7Y0WdgSZNGiRf3RpP8vrIF5gIBWafmbFy2bLjf0kfFXKKMjhaB939rM-9EScDZSUdFBtagFv20YJA1WwTHgHVLxtikWSu-xI2spfK1UzgwSabFutNXJBJ8z73bw73dJc_eeI7hqKr97rIxCBu7zN6blhph2-M8hhoEMTOzquBO5yfTshg_6m2TNkrKI_NOwm0f6TXnLyFKuDhwGOWFM0BUGIjFJn-JMB9TgYJBbK5bHhaKRLdU0aaGI7mT666rSh1Vlmqo2HT6sbv1_vRFP1CzaO00HgfWt-InE6Hq9VRwwpjXdug8OMFiBgfzFvPbzT3VZHXM58Yt34J1tcXi1WGzaaXTaVd0Me_llv4GJ2nz_2zZV0_PrjmdRn23wWSNvsd3Ql9FcbvqLDLiu_8udrPf2DGJfPhLgbplTf0T2SRpK_rM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا نام شکست بعدی در برابر ایران را انتخاب کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/457289" target="_blank">📅 23:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457282">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsPIFUQMM2EuTOcTWmPWv32yQllS9JRXfseAACPBDHzLdq2XwAuPGQ196Vv0PkA_apWAkhClfohTsS2EyYAGBi1ZBI8QLYXzBVrQitzTIopSyoXamFZSIwZ0QTvmo1zvepNIhmkYOAgzotttsj4bsyjDmwg4Nujc_3IBugfnv10zuDxBEJ9CVYhVwESwFrVygXF_rZoIxLyuyVjaqURw-u2nlSWWKQAWmxl6DIKwY9faQRjLQSr9OA8HfnYmUM3WaMvLh5jabN6Q8YOBpoVfdMnZhznUIoOZkDe-m_ms0DXbollPUk1DyvGPBh4iMq7EPIwJt3QMaVhgQAlmIXAv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDefABzzHtVGt9FjSYBCcrS3Fjqr3lYjlQ_qpkrxsWSRKFbyWZE5JjuwYswEexNyW5CsbDIy44EslTrgutjNwjMyJBuos1Xh5WDaXTbrkiY7VNeOfB2cJrhDITyQQPAUhdsBfLxiC2vA2Y9dkVcs_vSWi4nD-YT7RJUF6sgjNtdvXtw7pEbsuWlHKSUXxT_qz7RVapev2iJ6qWciRmifBA0ILNVTdzSdRSFZUZW4NkQMndB5cMtxd8JYxkw0rtjWFxAlvA-nHm6yGrPbCYuNp7nok9zAgsxpUOQxB6Yg8qLqd6V7Ece8lmEkwBR4EHZ4Z7-BbZi_BVnJOTx1D8qh5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QTJgL4k-AjDB_Nu5fKXs1UAWMCcsptUcWUTuFcb5ygklg5GYwOZ5IAMXQmkT8uEEzc_2EbfEixE-llLqcutpiQ2_Bzm7np0zB-1n6JQf1R4c9vudy2XXSqgz1Fb-brBsB4gBk_tb3NRJ_qMqSaFjG1wI51UOChVA5VhguA-5OtPtRPHKTczAni3204U1bYpX44MfdUH4ONMYJ-Xc0xFPhi3zUuKmNU-Naba0HQiMtjCPWXtcJZtLXYEzpigE725QKGq1fuU9jgwsD5-vygEUf8ygXxR4aripuG8YnfF_wJ6ZUGmRIA4Uire9Xdueau5B6YZrplUsTXHkEDPiAzQztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GR-zanHKhCpyl3y4zb9RRY_ZB2z_EM19IHU29TAOg7rPv8kEhrx2GvgjeFW7mGBoxXKe-fzjMl8eWRH9qSaj-Af0b-pTGeYawJ0WXWXtfakD1q_-iEP23jn0MivkJXIXkdUvvsv3FECt-CkdLVtK0xFPzePmlZm4h0iY0QXoBNdGrPJK1NtIuHLz1QYbLcOZjnobmc6W1fWQkXrIaL7YcFT7s_JreqrNZJiLGzFMTAIOk0KhtQthOZHoCGX6jrKxnscCVWKR5CpW6XBzSZV2Ql0yYJVp5oMJ65DBQjTfowIY8GrzGv5sbcHd7MJtqSeACvM0ypsYtK6EVWLgBmPtug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W54_BpPJLZNgHVENyjVLc4IXz2LqNzP3D6-85Fom2342jD-mVvXYdARGHferp58BwxENl4qizjdQ1v6cHUlFFrQT4naA1MSJQ7JjWVbhQ8fYbnD-Ck7MToUkO7mK3GUjtuWvvRYA8ZD0SjFNu_-L0TjJQaLOysFezC_wDRQsHdksQ-hpNZz3VfORBvYsXTwRmAWcZUxhayDFER1KWLL3R6fsEf01IEmSkJ35aJKVlqDbA-zCJtSxerFJPmusbw4in7JWMg0o7YJWAKC1BQPhGw8pDmifeno_hyoIVTwhiwDD9zRlr2VU2YMHQoNFyFXjUyxWKUxS8jqiZoLz172-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXML-GtSVe-moo8mypkT8bpq8tszBypPFbTqr32awv8853pZ4GeqOyS75Ef-zRzgeZ26neOQQ4q0IqHayiKHQv2lPcKw9qqv0tQJqwyDf-4V9-8bXx--TjIt5oejc_6E_ARZJYhzpm_UUAPew6lu-MV5eVDpWH5fL2dESbEndeJBSDJsUTfLQUNKGRUbNYstzijy0Sii6MxQkXWbCu97w-8DCg6lLW8X4lJbwZ09UyDwF2JpPFhhUr7PHSUFX8M07oHQ5qXnZl2KW9-rzvDN3qb8ms0-FwEajuwIPFdOS496PlwoYm-LHGT-XshRcGG2xW-9u547q8NGZzWcnSNfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6F6HvPep8J4tRh5a44TElTeyYqGTqsoma24JQI1IzDA64Eg1qnRstl3b224w5U4oZRBFKStDYhBIaN1Q2DLIFSjppsuqaMTRehG6A06Nun6L7IfQR5q47l2SZWb5KNshSU-3opI8kmB-kFEHrEAI6wbxDByKq1q1o7fMKLWXL6aFT62U9QyKGDzDjEC0LXGp9DWJVgqTRk4RaxhrjlZ_Qeay-4BjxyP0jd1I_VtekcbJbWNDn3FdjlO8OQV9_N9tgD6Ez_BK0DihZLamdgQ7eH1-6LS80EKqnbo5fLFr_oAsYDzg7qNa1EEY3zXoJf72u4NcvBURCXgfj7uahzJHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
حضور مردم عزادار در جوار مزار رهبر شهید پس‌از مراسم چهلم تدفین ایشان در حرم رضوی  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/457282" target="_blank">📅 23:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457281">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3fbbb826.mp4?token=WNG8wNnreNcpTOi_W3Nlv6ZXj2WG0yrQu-Bj8EFsQmjaYzk__-_0UatmFyKlO9GM2g7qgcqJC6Eu42iKIbuj1vjlMwAhZ8ARq4vVy1wh_sfzSYzjBPovgN9h0rEHnf2JkNTZNwQMU2ONdOg4FC3DTX1Rimmt5msRaoHT41cRJB8SI5o1gGdA-gPg4A7DIn_EEcPpuWjVJgRXFQTMiO1Qa0kaaF_MwkHrk2EGrxDWCBCH-iuYWRD7rmDczv2uNIAlI2bRpzpP_tN0nlhGLqQ_V9Hf70TeoG4R64T-n3BFQsSFPPGQukT74MoihJxbIb5RkMtJTX2iEeEL-eFP17LOaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3fbbb826.mp4?token=WNG8wNnreNcpTOi_W3Nlv6ZXj2WG0yrQu-Bj8EFsQmjaYzk__-_0UatmFyKlO9GM2g7qgcqJC6Eu42iKIbuj1vjlMwAhZ8ARq4vVy1wh_sfzSYzjBPovgN9h0rEHnf2JkNTZNwQMU2ONdOg4FC3DTX1Rimmt5msRaoHT41cRJB8SI5o1gGdA-gPg4A7DIn_EEcPpuWjVJgRXFQTMiO1Qa0kaaF_MwkHrk2EGrxDWCBCH-iuYWRD7rmDczv2uNIAlI2bRpzpP_tN0nlhGLqQ_V9Hf70TeoG4R64T-n3BFQsSFPPGQukT74MoihJxbIb5RkMtJTX2iEeEL-eFP17LOaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملیات پهپادی یمن در عمق خاک عربستان  سخنگوی ​نیروهای مسلح یمن: در پاسخ به نقض حریم هوایی استان صعده توسط پهپادهای سعودی، ۲ عملیات پهپادی موفق انجام دادیم:
🔸
۱. حمله یک مرکز حساس در فرودگاه نجران
🔸
۲. حمله به تأسیسات آرامکو در نجران @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/457281" target="_blank">📅 23:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457280">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32aacd7cf.mp4?token=J-IkyTVrPOVttuJY5qcrLqA8xr-jaQ9booa9xrNGFOTPpoT7LkEIgCZ8SPSFt2XngL4wUMS98sbpolLmdhyqMMLMwcSuuZNEoaBrLpVOcdjLnIV4e84ZexrdA7RpEilRYV1uExU7OomltcClt5FljJEHYR08CUscBv8NOrnX5qB46oSisPyZbzVxE_a-E_9XUFiHdCajaXcCA8KJMcdHlDmxRq5V0DnuxrwIz3IdrkfqOvraU7iiqfc8sqNicz2Hehp5LgLqMmNFZYHRh6nl_0xWksAGMxv2Jk82A33RZtjkD7n92f-jvd4ch0aU-AidHSLu6csj9FD4IA2TuOnvCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32aacd7cf.mp4?token=J-IkyTVrPOVttuJY5qcrLqA8xr-jaQ9booa9xrNGFOTPpoT7LkEIgCZ8SPSFt2XngL4wUMS98sbpolLmdhyqMMLMwcSuuZNEoaBrLpVOcdjLnIV4e84ZexrdA7RpEilRYV1uExU7OomltcClt5FljJEHYR08CUscBv8NOrnX5qB46oSisPyZbzVxE_a-E_9XUFiHdCajaXcCA8KJMcdHlDmxRq5V0DnuxrwIz3IdrkfqOvraU7iiqfc8sqNicz2Hehp5LgLqMmNFZYHRh6nl_0xWksAGMxv2Jk82A33RZtjkD7n92f-jvd4ch0aU-AidHSLu6csj9FD4IA2TuOnvCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانهٔ تربتی‌ها در ایستگاه ۱۷۳ مقاومت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457280" target="_blank">📅 23:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457279">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reL7l_xUQHAcr2bROEUbJiV_FzvUHWc0YabPLFyRFYcV9Y8JmgvL1ce3bbWfkiCyLyEljXg7UW29IKULQ9XePDd6191ivGuv-Z8jxx-_6vxgnvoBtseC9yntr1cV_gVw7rLlIWE2yJXc-XkaJB133KUwlsOMofGlqcfo41VTsLIyG7roGWWAgOtwhAIXkJZ7psGflPfHS7Fkh6A3MGDvVyJdIDQX6IDoFPJbmXhv0GOU8ujqGaw4rUlh0FkPhE6JO-u1gY19iucK-77UQjyF9yMGTRpC-1hA12rx1urDvIxri_mDdAGxewIpWPZvCj7pk3c4MhsMBbJL4eM1rV29ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: مانع عبور ۴۸ کشتی شدیم و ۸ نفتکش را هدف قرار دادیم
🔹
سخنگوی دولت یمن: نیروهای مسلح یمن از ۲۰ ژوئیه گذشته تاکنون، موفق شده‌اند چندین معادله جدید را در برابر عربستان تحمیل کنند.
🔹
نیروهای مسلح یمن توانسته‌اند معادلهٔ «محاصره در برابر محاصره»، معادلهٔ «حفاظت از حاکمیت یمن در برابر هرگونه نقض از سوی دشمن» و همچنین معادلهٔ «هدف‌قراردادن تجمعات و استقرارهای نظامی دشمن سعودی در هر مکانی» را تثبیت کنند.
🔹
نیروهای مسلح با جلوگیری از عبور ۴۸ کشتی از دریای سرخ و دریای عرب و هدف‌قراردادن ۸ کشتی نفتی دیگر، موفق شده‌اند محاصرهٔ دریایی کاملی علیه عربستان اعمال کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/457279" target="_blank">📅 23:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457278">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDPf0lGApZblCL8qEQFbyC7z0mqev9zO2ggYyKz2pJrtVCGSoKlVAztn6FhB9afaQonEhZCxiqpyf2GmqikhZWtyyYTWdh_ywGbogzYnYdWHvboa-aNz25ZcT5vZkoNis6MxwtE_8yEXYlBg75kjqEQwYD2Beu2MsanwXngOaGCbf-XFqTZN3gMLZdREFALhHoRi_W0_Hq8pcPzZ8xcN0RLQMNFyY0GEixRVvbaE2R4yT0Nn3G63CfJzyaWvuOK8F5zPaUQBZuULU95kweCGiKI5Pt8s9RsEG04CSsUnqLJ57XNrfHpf-VxbcPC7kkdlgG2HWjymdmPSVb5sL2nCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
هشدار دربارۀ خلأهای امنیتی کنوانسیون دریای خزر
🔹
بهمن، کارشناس مسائل بین‌الملل: سکوت این کنوانسیون دربارۀ نحوۀ عبور و انتقال نیروهای نظامی و امکان حضور نیروهای بیگانه تحت پرچم کشورهای ساحلی می‌تواند زمینه‌ساز حضور نیروهای نظامی و اطلاعاتی بیگانه در فاصلۀ…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/457278" target="_blank">📅 23:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457277">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c71e411fb.mp4?token=buc1D700o0QmwjSd-shXMehwjiIC0ScFTgCXGY-saOR5Rwl-RzdW3SaruSFfxdvr5VsZCFdvvFYP9ElZd6fzGVdMT_OkVlFEWfG7onC4Of9hERBEyghV48EhEjxBGVWRWsfegGF90g_RK9AP5ibzgsT4RQETyp5QXMyZu62GONt24QnuuU5BfpVhWdb-K73UdS4FPMbx4ELKV1_192z9LGrrKel8tspJaJwbPR67ZKhMa9D68Gk2LzMpaajJeLAB_6SO7xI8vxjGc2GAS951WkdbHfJAFeY-mHo4X4_YGMlF-D9WFsAIe6oIGNCp1vbFPltFVdp3zFNgKhb6up1BNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c71e411fb.mp4?token=buc1D700o0QmwjSd-shXMehwjiIC0ScFTgCXGY-saOR5Rwl-RzdW3SaruSFfxdvr5VsZCFdvvFYP9ElZd6fzGVdMT_OkVlFEWfG7onC4Of9hERBEyghV48EhEjxBGVWRWsfegGF90g_RK9AP5ibzgsT4RQETyp5QXMyZu62GONt24QnuuU5BfpVhWdb-K73UdS4FPMbx4ELKV1_192z9LGrrKel8tspJaJwbPR67ZKhMa9D68Gk2LzMpaajJeLAB_6SO7xI8vxjGc2GAS951WkdbHfJAFeY-mHo4X4_YGMlF-D9WFsAIe6oIGNCp1vbFPltFVdp3zFNgKhb6up1BNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سانحهٔ هوایی مرگبار در آمریکا
🔹
برخورد بالگرد پلیس با یک هواپیمای کوچک در فرودگاهی در ایالت پنسیلوانیای آمریکا، یک کشته و ۲ زخمی برجای گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457277" target="_blank">📅 23:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457276">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf377f0d6.mp4?token=XmhrGWs_E6tesSku7OD4Ex2Akca85fj3AQ61gwnKseMnd8UBYYXhYl6CnJyobmsNvQbM5IVDgONPVGf3g1p37gRxbECCXLhE4ucqOAPIP-gET-QDGpaFCHXbPUkqpCZ70F91RJL9LcWtbPraw2yQcn4iSbswk8Z3VT4U4Jx4EqpaaKF8h3j3lv4fH-Rbsa3iuJceHI9MW2swMfYeLiCNNsgVQmABaetnIBJfh9ORmSu09LDID4DMbP3qGWqNz1Cy6uLjaXEieR9y1ZE1h_EpZLd_qZya2J0vCOgmI_J_-amrpYBplkBMwayzvzrRPbnpHWfNCF1wf_O6dw4IaBcfPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf377f0d6.mp4?token=XmhrGWs_E6tesSku7OD4Ex2Akca85fj3AQ61gwnKseMnd8UBYYXhYl6CnJyobmsNvQbM5IVDgONPVGf3g1p37gRxbECCXLhE4ucqOAPIP-gET-QDGpaFCHXbPUkqpCZ70F91RJL9LcWtbPraw2yQcn4iSbswk8Z3VT4U4Jx4EqpaaKF8h3j3lv4fH-Rbsa3iuJceHI9MW2swMfYeLiCNNsgVQmABaetnIBJfh9ORmSu09LDID4DMbP3qGWqNz1Cy6uLjaXEieR9y1ZE1h_EpZLd_qZya2J0vCOgmI_J_-amrpYBplkBMwayzvzrRPbnpHWfNCF1wf_O6dw4IaBcfPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادامهٔ تجاوزات رژیم صهیونیستی به جنوب لبنان
🔹
به‌گزارش الجزیره به نقل از رسانه‌های محلی، اسرائیل منطقه الطیری در شهرستان بنت جبیل لبنان را بمباران کرده است.
🔸
ساعاتی پیش روستای المنصوری در شهرستان صور نیز هدف حملات توپخانه‌ای رژیم صهیونیستی قرار گرفته بود.…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/457276" target="_blank">📅 22:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457275">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ناو بحران‌زده لینکلن عازم آمریکا شد
🔹
ناو هواپیمابر «یواس‌اس آبراهام لینکلن» روز پنجشنبه پس از یک ماموریت ۹ ماهه که بخش اعظم آن در پشتیبانی از عملیات‌های ایالات متحده علیه ایران سپری شد حرکت خود را به سمت بندر خانگی‌اش در سان‌دیگو آغاز کرد.
🔹
حدود ۵,۰۰۰ ملوان این ناو تقریباً تمامی این ماموریت ۲۷۲ روزه را روی دریا گذراندند؛ دوره‌ای که با گزارش‌هایی از کمبود جیره و اقلام تدارکاتی، اختلال در سیستم لوله‌کشی و آب آشامیدنی و وخامت شرایط معیشتی در داخل ناو همراه بود.
🔹
ناو هواپیمابر «یواس‌اس جرج واشنگتن» که در ژاپن مستقر بود، جایگزین ناو لینکلن در منطقه خاورمیانه شده است.
🔹
ناو لینکلن اکنون در حال طی کردن مسیری حدوداً ۱۳,۰۰۰ مایلی به سمت خانه است که انتظار می‌رود بین چهار تا پنج هفته به طول بینجامد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/457275" target="_blank">📅 22:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457274">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxO7XMNqx-YJ0zoed3MD0_6G-2NTPVlPoPf5Yx_ENlFqTFv5rTQ7AgHOLJN6mIEsxU5937v8mYSZOx1LxAj3kxqEDig62rr-hHhqa8z6IE2DddzqpLRYnlOAAtanij0kWORetcl2odEOGwt3V1S4kBYEzs3j_IFZ9b4BmVnuC4toPIPEoqclhd9qWTyYxP_O1NkJ4edU0IIkSs6ZK7Bkf9_WC9G4-cYwY1_hte1SOsJZM3ZuqOi7erHb_MqzeV5Rxf4w0g0w9dj5li3d8MH4WRYgJzM8GRr5k4aT5zZb8OAa2MvAAJ_6BxUoIMBvmkqS-0OSxKc-Vpx89uH6Svicwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: کشتی‌ها
از بیشتر دستورات آمریکا سرپیچی می‌کنند
🔹
الجزیره با استناد به داده‌های شرکت کپلر گزارش داد از ۱ تا ۱۹ اوت، ۲۳۶ کشتی از تنگهٔ هرمز عبور کرده‌اند که ۸۳ فروند به‌طور آشکار از مسیر ایرانی استفاده کرده‌اند، درحالی‌که تنها ۳ فروند از مسیر عمانی عبور کرده‌اند.
🔹
براساس این گزارش، در میان ۱۱۲ شناور نفتی و گازی عبوری نیز ۲۱ فروند مسیر ایرانی را انتخاب کرده و تنها ۲ فروند مسیر عمانی را برگزیده‌اند.
🔹
الجزیره با اشاره به تهدیدات آمریکا علیه تردد در هرمز نوشت این آمار نشان می‌دهد کشتی‌ها در عمل تمایل بیشتری به نادیده گرفتن دستورات آمریکا دارند و تعداد بسیار بیشتری از شناورها از مسیر تعیین‌شده توسط ایران عبور می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/457274" target="_blank">📅 22:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457273">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3af02dd1c5.mp4?token=cCxEbh7pR3PXCRglQiEUbZldoKjqU6OrUaEwoZz38iOdmXVfDIEs5oGURiX8H8WPHOQKfBchmcgTHfUVxAIPAzqfc_iFOHvlQX_I3H8eIstE8HLZSUIq5jaKC84P9v9WTbK-ks7mQpOjn4Q6TrwSY_z-9CE81HSThP8VxdDHARbUsmm8pHj7Yu6jYiJUBtgdbnLGanG7xYoXtFbCSIZI1KSshN-vxkWZ7_YMv8vg3rd_tYBqY5UX8P7BRNELzodyx9CO65OuEkyFpyB3QGaMpiXU045G9KXl4REaZwaCFlnGTIpMBPJNuvwiy0sE9D5cfJPGX17Bb26LesysqwX0ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3af02dd1c5.mp4?token=cCxEbh7pR3PXCRglQiEUbZldoKjqU6OrUaEwoZz38iOdmXVfDIEs5oGURiX8H8WPHOQKfBchmcgTHfUVxAIPAzqfc_iFOHvlQX_I3H8eIstE8HLZSUIq5jaKC84P9v9WTbK-ks7mQpOjn4Q6TrwSY_z-9CE81HSThP8VxdDHARbUsmm8pHj7Yu6jYiJUBtgdbnLGanG7xYoXtFbCSIZI1KSshN-vxkWZ7_YMv8vg3rd_tYBqY5UX8P7BRNELzodyx9CO65OuEkyFpyB3QGaMpiXU045G9KXl4REaZwaCFlnGTIpMBPJNuvwiy0sE9D5cfJPGX17Bb26LesysqwX0ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شریعتی، عضو کمیسیون انرژی مجلس: ۶۹ میلیون ایرانی خودرو ندارند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/457273" target="_blank">📅 22:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457272">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e0332a80.mp4?token=DQoewvEv22GMudTeykeSwU11jfg4jQTwSVKNw9qcC3gLHs9nG2PY__UUNEIGeGqbUjwdPu4VmaCd1wLwgl4q4jW2r7H1YRJtHbCfFkaGFgD5ghYKLJZB0-4jveGf5b8UPsReJmQu5MJ7LOk_CwrjQ1VzZcGsOcfqtfeEv4AOw0B4gtLONHvoYB5AMBrmMM2El7vb-YRaB2UJQ3FJctr93wok8MMvj8sDgclSYxg9rmjFiY_V0JOZ3jpMn2HbMuZoijumPLNSwXCQfRMH-X0YYfMFR4dUSmxtK254kKkVurQNqeC8mvXH304KbyI0LX5RDXYYyYy2eZPiJ9Wgo2rhUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e0332a80.mp4?token=DQoewvEv22GMudTeykeSwU11jfg4jQTwSVKNw9qcC3gLHs9nG2PY__UUNEIGeGqbUjwdPu4VmaCd1wLwgl4q4jW2r7H1YRJtHbCfFkaGFgD5ghYKLJZB0-4jveGf5b8UPsReJmQu5MJ7LOk_CwrjQ1VzZcGsOcfqtfeEv4AOw0B4gtLONHvoYB5AMBrmMM2El7vb-YRaB2UJQ3FJctr93wok8MMvj8sDgclSYxg9rmjFiY_V0JOZ3jpMn2HbMuZoijumPLNSwXCQfRMH-X0YYfMFR4dUSmxtK254kKkVurQNqeC8mvXH304KbyI0LX5RDXYYyYy2eZPiJ9Wgo2rhUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم سوگواری شهادت امام حسن عسکری(ع) در حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/457272" target="_blank">📅 22:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457271">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb32a4ff64.mp4?token=aviM6OEQ1su6klsI-lF-J9rNbr_eAP_a5_5DgNFjXoREh_f01OVjBO_6_3aqJbfr6Sh_KZ4qy4g0QYEmecwfeGIn9OWbRZcxHICagO4FmwcT_w5LW3s6v-y6UAdjs16YwYcsIQohVDdvQZItugfhXE5iaVK8rynxEkkFiYkZ-NYEIPlybVC4x0BbPCHglTfXd0uF-osd3aE8arZ5o_Mmz6keCqWW7Z_ql9mdSwIrtuCmuvC1XIFK_ZMBsrCoYMfc3bDLlhqMLGxmnzXzXZvs5LXBCgkmfuikM_gQRlcPZfk2uQTa06TXYOAOVFcLivAwch_wekTD-ct9m8Gk3hyD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb32a4ff64.mp4?token=aviM6OEQ1su6klsI-lF-J9rNbr_eAP_a5_5DgNFjXoREh_f01OVjBO_6_3aqJbfr6Sh_KZ4qy4g0QYEmecwfeGIn9OWbRZcxHICagO4FmwcT_w5LW3s6v-y6UAdjs16YwYcsIQohVDdvQZItugfhXE5iaVK8rynxEkkFiYkZ-NYEIPlybVC4x0BbPCHglTfXd0uF-osd3aE8arZ5o_Mmz6keCqWW7Z_ql9mdSwIrtuCmuvC1XIFK_ZMBsrCoYMfc3bDLlhqMLGxmnzXzXZvs5LXBCgkmfuikM_gQRlcPZfk2uQTa06TXYOAOVFcLivAwch_wekTD-ct9m8Gk3hyD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره رئیس بانک مرکزی از توصیه رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/457271" target="_blank">📅 22:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457270">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1fe95072.mp4?token=Aapeg71Rbyxvu9AQ6_nU17PUwaTEoWK27zHArm9gnGXKKBOz0vRDbA_VCzdQB6DeXBTDmXtliPxnpLPRu5jPoo_I_Qkzpe5U-tjj1wyFcRx_ygdz6IjLa-r7sbXazak1woKAAlxwvjBEtcaWgz3_N2aWWjekKOy0ayZAvE_ega8O6jeCNmwkGOBGfHD_loFb9vz1nZNoxiETliwmpQQIApks3gngLavWKYKlX43rNSFhKGW6-Gz-a8JPmj5jUgs_l8I3HCKUV5SA165Gq6B9Qnrgk3UsjPYe0DNZPo7HNIYM6-NuCP_W9mMzzwfo0Ytv1ehmhNmG5r2MJf9PP2GoVKY2wCspakkSk2qLeJ7CgLN095Lph5XWrxxZmjhW0R_24Y5Uq4NbvNVBtZdkH-0MdObiEnQCRNm_Hy4B00QTyg1nZ2hvnVsEclz5hC9xkZR77mpiqoSCnYYYoQvySTITZbEoXlcE42ub7GS5I15TKWPhcdhLvCfe3Q_mw46EafRu-j-kyHzYGN4j-QCZSsgG9DRbwhdd_fvcIC4cC9fxDtgnuB2Df9ZNnjx7N5FcmsWkb4EC6_ZMUzPfNuDhAQP8nkdc6CmwE7hSW-GzOBJimipS1NiGD7cA5PZyNOthhsPyEOlGX53AXffszLNx-qVh3JMMaSRrnl77fJVQsg1VGko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1fe95072.mp4?token=Aapeg71Rbyxvu9AQ6_nU17PUwaTEoWK27zHArm9gnGXKKBOz0vRDbA_VCzdQB6DeXBTDmXtliPxnpLPRu5jPoo_I_Qkzpe5U-tjj1wyFcRx_ygdz6IjLa-r7sbXazak1woKAAlxwvjBEtcaWgz3_N2aWWjekKOy0ayZAvE_ega8O6jeCNmwkGOBGfHD_loFb9vz1nZNoxiETliwmpQQIApks3gngLavWKYKlX43rNSFhKGW6-Gz-a8JPmj5jUgs_l8I3HCKUV5SA165Gq6B9Qnrgk3UsjPYe0DNZPo7HNIYM6-NuCP_W9mMzzwfo0Ytv1ehmhNmG5r2MJf9PP2GoVKY2wCspakkSk2qLeJ7CgLN095Lph5XWrxxZmjhW0R_24Y5Uq4NbvNVBtZdkH-0MdObiEnQCRNm_Hy4B00QTyg1nZ2hvnVsEclz5hC9xkZR77mpiqoSCnYYYoQvySTITZbEoXlcE42ub7GS5I15TKWPhcdhLvCfe3Q_mw46EafRu-j-kyHzYGN4j-QCZSsgG9DRbwhdd_fvcIC4cC9fxDtgnuB2Df9ZNnjx7N5FcmsWkb4EC6_ZMUzPfNuDhAQP8nkdc6CmwE7hSW-GzOBJimipS1NiGD7cA5PZyNOthhsPyEOlGX53AXffszLNx-qVh3JMMaSRrnl77fJVQsg1VGko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این رفاقت‌ها در تجمعات شبانه شکل گرفته است
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/457270" target="_blank">📅 22:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457269">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4515138cb5.mp4?token=QCln7ZQGEQBTRW_uy2KeeaIAvF3E6CWh5wrE6pSzoxeR1FsZm7xZ0UR-nZ4CfrvPx5Zc8s-pscTs4YhQYLLUWmkeuBAZJHtl0XBbM9JBe6iscu-P-EUF01Q4jAWZMyuCVjCsuG86vC-p7gTivD2c9sBoCfWvDbpi_7D8-3fexxE4VOL5G9UtyL3OvXDHP_2Bolff0nt0JYu0Jb69Nl-4Le5Gb324H2WS6GLSG1hKF5lvjZNc7VkCe5-XCJ5_Kvkwz3rrTTc18dOi20PNip44WP-qBy5u3_Cw20osK31R90-WJ55hfwJua-fvFEV7o3mfURv2Fl4mm10Vso72L02XWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4515138cb5.mp4?token=QCln7ZQGEQBTRW_uy2KeeaIAvF3E6CWh5wrE6pSzoxeR1FsZm7xZ0UR-nZ4CfrvPx5Zc8s-pscTs4YhQYLLUWmkeuBAZJHtl0XBbM9JBe6iscu-P-EUF01Q4jAWZMyuCVjCsuG86vC-p7gTivD2c9sBoCfWvDbpi_7D8-3fexxE4VOL5G9UtyL3OvXDHP_2Bolff0nt0JYu0Jb69Nl-4Le5Gb324H2WS6GLSG1hKF5lvjZNc7VkCe5-XCJ5_Kvkwz3rrTTc18dOi20PNip44WP-qBy5u3_Cw20osK31R90-WJ55hfwJua-fvFEV7o3mfURv2Fl4mm10Vso72L02XWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ چیز نقش و جایگاه ولایت را ندارد
🔹
سخنرانی حجت‌الاسلام علی علیزاده در مراسم شهب شهادت امام حسن عسکری(ع) و بزرگداشت رهبر شهید @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/457269" target="_blank">📅 22:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457268">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b65b52ec31.mp4?token=vxvmCppr-Jx1cA67kdJDlpOfT4c53sPofIWk-YEw4PUasRXWtgLiWPWWdkSQ2L8xnXp33Ar59iIhi66qBjiR5cMSezVOUYJem7Y1dKFP9q3pBS_Charovb0TwTgUIzC2fIsrIdojgrnK-IX9KETgJYsrxIa27Hc-UywDQLtLYJUTHfGYrWUcEGaf6kSywzCDpTpXi77Y1x4OMr_7G9VOZ6pGoxVtRdCm-QbZY2os_R6m3MvPSNdcmD_oqvN7Wd0Nnj2jCICUWHY31sooIZZB79Mq3rRLxUNDMffLxgRuUcB6UgWw_p6PM1c_cC5YqSg1II5PeIxiF9M5bzoaRpwMQoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b65b52ec31.mp4?token=vxvmCppr-Jx1cA67kdJDlpOfT4c53sPofIWk-YEw4PUasRXWtgLiWPWWdkSQ2L8xnXp33Ar59iIhi66qBjiR5cMSezVOUYJem7Y1dKFP9q3pBS_Charovb0TwTgUIzC2fIsrIdojgrnK-IX9KETgJYsrxIa27Hc-UywDQLtLYJUTHfGYrWUcEGaf6kSywzCDpTpXi77Y1x4OMr_7G9VOZ6pGoxVtRdCm-QbZY2os_R6m3MvPSNdcmD_oqvN7Wd0Nnj2jCICUWHY31sooIZZB79Mq3rRLxUNDMffLxgRuUcB6UgWw_p6PM1c_cC5YqSg1II5PeIxiF9M5bzoaRpwMQoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت به بالای ۹۳ دلار رسید
🔹
قیمت نفت خام برنت در معاملات امروز با عبور از مرز ۹۳ دلار در هر بشکه، به بالاترین سطح خود از ماه جولای (تیرماه) سال جاری دست یافت.
🔹
این افزایش قیمت درحالی رخ داده که نگرانی‌ها دربارۀ اختلال در عرضۀ انرژی با بسته ماندن تنگه هرمز…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/457268" target="_blank">📅 22:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457267">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQAcKsimD2Kj14iO8bECz3ha0kP_-Jk3NhLTU9qKxXb4oTwM9B8XGIuZIG2ZBAhSiqd5ggxWd4UlFMVoq7MJx31NlUj50-3ioN7XeZ8ZKDWVeGUtGFdna3XCRtaAPjIUNnrcTPWSmvg8dwkYzoXl0q88icKIGovYZpv_lAh9V5yJaKVgZ-uvLF6sFhrEBSOMjKKDt6gHKmQMxjtGpVPYTM868mq1ZeBifwfwWUB9G-yzWx0FP2g9pwXSnksKDXEwS5hn9IPvNZr3ZE90fzkIx0Wfvf6wA30bwY_E97ZrW9rdYub0gMclsjMrJuq1BtehL_tuD8-PIJWeRzoXnPpzAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل: ۹۴ درصد مردم غزه سرپناه ندارند
🔹
محدودیت‌های رژیم صهیونیستی موجب شده است تا از جمعیت ۲.۱ میلیون نفری غزه، ۹۴ درصد به اقلام اولیه و سرپناه دسترسی ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/457267" target="_blank">📅 21:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457260">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxLKP8k8Z7FZ6lkSHfCqodSBL09xAuo2skkk5NllH5UCNzqczJpT9CU7ECEbm5HNqpVxnvWR8w0sjcrFQDOlhXR04zUMkXN_6129Wy-5E6PzPcBwxsXvgJ_fSAj-PmNg2FL_p5ZoKlpbc0_JixwZrhVsdV3ZIwKo2gJ_s3nIp7dGOkB9fmX0Tlci1OOZaZHVgV3JU1md-CRHkCYTHqQh4mNAPBByukXxJVfk_3SrdtGmBkBWcOEUsAtGzwONhyCTExdGa_fX_ziTrqJvBY8gWg3u9a83iLAL80AEHtzpOTqfjs_hpHMaY5IKuBL0WpKrpyBaiqXutcxItDwRKJK--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcJJ-nMejfzABQab6mP0SINS65kcvCDCMWc0OM6CxUDPJH38kMrhp0BTFpFt2p7GdkPU-TT23U5DqJUBUVbr-hxX2eeqWCU5-aiMAhiAWzPGjDkcB1r45JXwiTPM9Y8CC1bF7GuY4hLPMZ2mm_yXgiR0UJpVajTFuI4RH3_dpTsgMo63uGJBjYFdrp5jn44wMb56VyxI3uXl0xv08hfoHAq2jEHyqBTFTNu2FtdmDE37QwBf102I-tr2mZtfImNdIKjWxEeQ49-pJ48ZYW-lvh60d9fnyEJrETEDtXSgxEO6L3O7wIvLLqWGUKD9yPnxP-idup4F_G5Ia2ceS7-gLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JimeD72S5TC2ty8R6D0hicdKCBN6UaZE4rh6XyfhZWzbkKankEQt3uRqD39iArjo74zLThgQtxylmQXZ2OUGcBLTK6_yvyt1DM20ZpBjZguqw8dvMDSLZSyCY5HYvRk2lumkW7OcfafQ2Vir-kA14Q-r1vjlh3UGfIv4IWzF9rq9XovjTQnGL69Fk_hCIuKRraPvZvIVX5cxTpLkleVtsMbMGI2n2AlevekDVaa6M_3QcKjIgZeDeuCZRI13LkvQhlCZBXeLT93tejtNdNkvuQ3Cdbg37PAkUiRjj7A2ZSXQtgv1MGOMw91kh77IbdOkdAH5aD1WRTvtCkY9jn40nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqMPsL_z5b-N44RSfH1fMG87MB4L5OMGWYDdtzzZs7k4zCs4-wxvfDSlPDekAOrNeaC9A0qbT0Naea4tDcok2dkMHnVi8krN1LyQlgn-krW96E0B9DdZ8S6bF2yqzlHV6cwITYydv9M93Poc0r75rJGWQfPJY32Z4wYrHArEl6m8xjmV9wJYkATt1quwC70ObJm2LizYz2hH7Not2N8aPMk_QLzOcaajXi6SBPMwQQNW7Xm2U7biyhCvKn-pZmubtEXHKHSCBkNZMbV-DXSSAVSC6l0UnsCiRVgRW1BJe8oTlQ6l0N_LTywdc2twbsWqV_DG2QWwy6viLoC8ISFOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ok9bYGFpGh6A1ZgnDR_plmQ6013iDeDfTWbDZWsFgA_PGDq80j_2QZCsKX1qnakRxYxzHhuAvj5kQaDSG1YzBPrv_VDby4ysikpF_aNy7zhfXlq8docpVA-ZoYxuC3PwA7v7FR_5A8JJngEYgnG7bu3-3ClH_Xyg5xfc7t6M6nwrc57NJkas38dlS2yC1LJXZ6Mkh3CRx4FUgvA5zAxdRiImYq4tVmgeaR1UQw0W8zhJ6DYugkGHvRWyr1sh-HWRFjDIQ1W1gaDrYddOLYlYqtf1rKY0v0XtvKuGt17q9TicJEzeUAUiG0_Lz4qt8759WracJQyqW04KJkxiYmdHyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICNno4-ahuKGqs6V1Y-FyISchJlhdmVIDgaYlcfV6C0l9TY2ARrFrnhbng4KROH4Jzcj9IP_3JQO0Fq-0BLp2BNSSHskCFFTtL8qOAzskmFTRA5Kggsa6PLDhbbFJBnIvOKM00TnLcMu2e26jsO6YNkNgN3yTe9RMc7RFLmA7F6EK2erqGFgMlrKFOE8s0rVM4bt88Kol4GgHlikKl8I33BhtuYw_6QHQGenZB8fAujSrdxZC0HQhW2O5uVKfyyz7SCvUbLcFLAxzkqTzq7vFY2mX1qcpMPl6XXCXAlrnxvhRdw59soPjyv9dwQ-ZebpNqF3k3Nvv-dU6RIJZlK_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCurU5VUszhG20PqQDxt4NBVfKJ1BYAWhNkQnnthABA2if-WErZj-kYaIQSJM6cKTY6WPkIwGP2ydj0Npnk5gExZVMmxikM673tJwaj_kWEc8JGFC5CZ77ldJr6k9pLnPRXAzaZ1SAVsLxPi2G3abhzHjldGTzlMn_oXGZBZ5PhToOCQ7ZlphSJgktglRSrMTBOO0cOavgs-EYo3EJaGokoUROGwzqcjvvv0Qoxl-MfhpGYZznH5Xd14lqJuC8frWbBs987Uczohc_I-gr_RuxRexy1dCkM3FiKlYUH_HfL6zgeI2JfMkkDyovzkyAPsq2w4XZOgAqRO1POuDoIeAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اربعین آقای شهید ایران در گلزار شهدای خرم‌آباد
عکس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/457260" target="_blank">📅 21:31 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
