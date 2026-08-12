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
<img src="https://cdn5.telesco.pe/file/nEo9_qyHk4y-qkv4wdwRuZNyycILKwknw8fXXCAlnEROtOZNuwVSajMkaAF-9tRvZFfjB1MPVySuDtHW4vnw8Px9D0XpZHFfTEMdpJW1CUv0hDYjAXGqFk-19JvLL2nyRWsbqTSDfV7q_JZw_DhDXcaRMqs7Q57Q7FzYo-ZWT9CRP-3lz_fXT_tYcidu7WgygFzI_0xG9ISafolMsHW5a2eG-Jte8xLTQmTDi1VAUG-KdbmRhieQpmVWhwjOd6WnHFMEBdseRbwbMEEtSKMGr6vQgi272qIORfysR000zof2UCgW1lTS5PyT9OiEE2GV98K5bHaBJSlNzmtAr4sunA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 475K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 11:39:10</div>
<hr>

<div class="tg-post" id="msg-103431">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnD5J9DrIfQHc_IQBBVEemy9Q20_1G3kLBrfwHJTvPIN5rXlueuC6NwRe-gkyllgEngATTFlyYPlCodUPThlACcKecooadrH4pQfg6viErkO7m6AfgvOrd2UZUL9yFZ7OZMicBHu1BGOxX9E0F7qZMqAiNA8p_aCjzv0HFnSG2s6x7Mzcgew_xXorjHon81gUSCqXXDATKCtqS9YEQOptAQ_2IraBcR80RhHtxBfaNFrlB8Bq04tfQaQS-X-fp0UY9zP6FATN7xXi5tBqMo6R6LwTSDaawvcZBVIuJgPydT8U0E8AB2roCQpzVP8iR-2xvxJ7LtKiEUDDWGmViybrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
رونمایی‌رسمی از کیت‌اول قهرمان‌فوتبال آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/Futball180TV/103431" target="_blank">📅 11:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103430">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emL1tD9i5SDeaUv_6saGmTLoGWl3ZawLGtaIK1cE3br7HRxmmI0g86lFbF4UJK0525yVLm7jQi71yIC2UdrZW7-PyfrGAHN71W_v_f0KXEcrLCnQN4N1Oha5dFM8D5ohuSO1nFl1XUJ5hMy1D1yt-8pSCSR0QKlhYVJc2R5tRvPHlLEtFqB5J-fQ5feUjT5peTPmS_Xy5mNk4Gz8P9operWQCNIai6UPdLTtmRpCMQP9EXAPPT1GH0LK0WUaAY1gbEhkHICa7Vhqg6Z-PEsiAPK1JaAifU4meSa6AQ0Z758tyc48QoRCKKh-sSCnc-NsxiXRonCew4DDs0nGjjeK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
⚽️
#رسمیییییی
؛ باشگاه چلسی رسماً اعلام کرد که با پپ چاواریا از باشگاه رایو وایکانو به مبلغ 21 میلیون یورو (همراه با موارد اضافی) قرارداد امضا کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/103430" target="_blank">📅 11:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103429">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWjH9KVwxvPHl95F2DxT1iM8u6Q9EqvZpUgEyj879aoWJKzfiwb47gu_Fv0XmRZ08druEM0xTcTw_SPugeBmr2lezyJ7WfVERzdH53uRw4isVKolBcuDxWHm5lfttTJ1aRVCwiyeBFzfpDcaPr9HkXSvrybbYusptpAidVCEFCP67YiflZ4kfKWNcJPWL709XW2E_JxfAlP1IxbxuKuMkg1wU48O4EH74ohFRIwQI8QX0ahgGS198b6dcsk9o3D9LbZ6teR37XNThnBiObbGrhJZUgWQI-ok9XcPXDlXxDzbKrfEOa07326mV_MBQ4plmBQRjEckQrytRmuWOf-2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📰
فابریزیو رومانو:
🇪🇸
پیشنها دوم بارسلونا برای رودری به مبلغ ۶۰ میلیون ارسال شد
🚫
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سیتی ۸۰ میلیون یورو می‌خواد
💸
✅
انتظار میره روی مبلغی بین ۶۰ و ۸۰ میلیون توافق بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/103429" target="_blank">📅 11:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103428">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4QJ7iQZtXf2M7fdvAxt5Fa6bSobr_IL5vCNkA6eidhjPjHUNnXECrzHeYMTJyI7mjlT5nAABNOoc9gwDDa4D_p14w3NVJtjqJNEHYmIu7zLKFUTU7maeMBHnilz4-ViYti9LiNNqDsVzzuut0SyQWQaD1H6ZnMc8ItZTa0D7YA1Vus8ZCCmzDvfP8ZXU2SRo0oeF1j21GZXH0CSBOrfvvxeqCWDlru83dwJ5tEZhDLPujOaa6oJSsB8ZjKWvmUoWQ6AxTM5i7spYz26-TmVEi2CtlGEZSKAKxdQW5otsXpyom0Cj_7HBtmXm4VvIzw9Txu2D2LxCMXMLK0vTifqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی‌رسمی از کیت‌سوم و صورتی رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/103428" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103427">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103427" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/Futball180TV/103427" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103426">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zgisa4H-pIXJIjqElk7pIcqdLwO8bWJiS-RWEEVRF98n8I-8i29dTHDc8W0GwKNzZXHO6qCKXE4zxvK4PcBbxDJsMF1Ev3TVJ7y8Z14NZ_tqaHGJNTthROU-XlEPfmNpT89540abKJQ5LKuxIeCgT9ZBD3tGI_Vz4eY2H5JwanhWJUkUDdY9WicRPgKLqBJqtgRCI0n0nAIpBU256mIi_Wq7w1PRrJO9ZrkWJ_28JILP1Dim7mRVDFeQcXnkSk4tCK_Nnz5SMqjFgvT2j2QCAqvfsF_TDZ2GS4okjmwunvD6qgxX7YBCeC5DCm5oFPWCyJHZmMxvDhuAQQIf87lJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/Futball180TV/103426" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103425">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/870f9db185.mp4?token=pASKbcx1dQE0VjT1_kzbSiTkxVoMsgmf7ZlrCmrHl8z8JP_HtHsJSkU28Kh0_YL-n2U7VyP94djIjw5B53VYE11Nh71A1T_jEdnE7yeyilpeldgpVhr51UCiUAlJUY2lXuVzG2sWI-wb-kTwJXh_WbeqZhRtFHeNMUDwAAqhV4GsWDyQyl-XPxMbg64VxIkrDY_e812gitJsrj6VJZDCp7I3xfzo_KiO_sMiYKLhk1zY8SXCQOTqLrMBD4iHKGEdG9uf0VDStr8I7ER-uwDKwYqi5WCnzxTfONxA1KAd3O_SRpirQ6HMxetl2bC8NHrcj00vn0S4SVI6N7A43wwFU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/870f9db185.mp4?token=pASKbcx1dQE0VjT1_kzbSiTkxVoMsgmf7ZlrCmrHl8z8JP_HtHsJSkU28Kh0_YL-n2U7VyP94djIjw5B53VYE11Nh71A1T_jEdnE7yeyilpeldgpVhr51UCiUAlJUY2lXuVzG2sWI-wb-kTwJXh_WbeqZhRtFHeNMUDwAAqhV4GsWDyQyl-XPxMbg64VxIkrDY_e812gitJsrj6VJZDCp7I3xfzo_KiO_sMiYKLhk1zY8SXCQOTqLrMBD4iHKGEdG9uf0VDStr8I7ER-uwDKwYqi5WCnzxTfONxA1KAd3O_SRpirQ6HMxetl2bC8NHrcj00vn0S4SVI6N7A43wwFU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
😃
لو رفته از مراسم ازدواج رونالدو و جورجینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/103425" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103424">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6KuGbX2dg58CD8Ipk9p-54vV86QNv7cTg9mNNU4Fol9ctu9WQ9QiQF7lJi_my-aY9Pz_qIxXv4btlbYy7VFziGr-wiRarD-oXgAeK5kqH1BbGrH8-mLQoFV9SI1Vf5w6_wfTdQ_JIhnL-g7SbYOahIt0CbvYTh5RuqvQ6jIj1y2kL0F8SrfHIaGVIiTFFmAapdrS_1U_OKh6dicrEPKZy6_G7bRNquUi6bVkdem4YzbtrZFjR7ZWZcKc7bA3dxyJpes_MTO2L_E9Dsq3z-hsS_96HRWpXKcVLKtWHX-auP0KJn3kpLNPwWeudWqBu5WNVOxr82l7SRbENr6q01DmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مقایسه افتخارات یامال و امباپه در ۱۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/Futball180TV/103424" target="_blank">📅 10:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103423">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c644437b15.mp4?token=rvCOMk0ApYNDxSrSDgeep4sWmHzILYlFKz0wDPvmML5TqFhEyVWqGVU2tacNwOupPoXc31fhp94y4EbFeYNIYHPZ0R9El-JEXA2gXVLKt8IhwStaSJ1760PbCgSUBf6xLrqCwjtPCdebl3W1Tjm_LsPu4kqutGS3cXyZ3Fk_drYGHrnQFqEtnTz7wrg03dJzIgApBtf0fRWmTkJtIC-vGbK7hN0jiNs9YnlwVJgDvk985jSgTVBZ-n1-TGSZiAHZVRyZTbMaJ4hTGkcRR4J4htEp-Hy8sBImt2c-YjfTrS1uE2GaLpg4T0GMd6XzOGRuKB7zXrvHuG7XEzuERZ2HmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c644437b15.mp4?token=rvCOMk0ApYNDxSrSDgeep4sWmHzILYlFKz0wDPvmML5TqFhEyVWqGVU2tacNwOupPoXc31fhp94y4EbFeYNIYHPZ0R9El-JEXA2gXVLKt8IhwStaSJ1760PbCgSUBf6xLrqCwjtPCdebl3W1Tjm_LsPu4kqutGS3cXyZ3Fk_drYGHrnQFqEtnTz7wrg03dJzIgApBtf0fRWmTkJtIC-vGbK7hN0jiNs9YnlwVJgDvk985jSgTVBZ-n1-TGSZiAHZVRyZTbMaJ4hTGkcRR4J4htEp-Hy8sBImt2c-YjfTrS1uE2GaLpg4T0GMd6XzOGRuKB7zXrvHuG7XEzuERZ2HmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🇪🇸
اولین‌حضور پدری در تمرینات بارسلونا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/Futball180TV/103423" target="_blank">📅 10:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103422">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXsLdq_sQl543VNkkswSVmSttoPctI5VoGaTDH1TtCuK4yNP45Us2CpefVXGy8QUGraUqRqNaxzOKmSxfVR4ABfhW8YeT9E8_I7HUZDhbdfLD2vga_9C7nNTAtWY_Z8whBu9RyjvRfY5yCnZs8jgo7E6LiQU3yduU0Y0-XT4LqDE7lMKJHZUG0Kez4GzdNbHN9pObcg_RTUxThLgt4a3hLiDX_zCtplsJq1p35mtQ9w5kaVjyBS7JpXOIfRkoIYxTE9yM7dnOUWhm5TzzmaQaaoW_qGVsHs8InoiMLEBkrzdwhe4Y60_ua-MS6EhsVlOI2X8FCMlyndm9IkeewwGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
❌
جرارد رومرو: هانسی فلیک علاقه ای به اوسیمن ، ولاهوییچ یا لائوتارو نداره و فقط خولیان الوارز رو میخواد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/103422" target="_blank">📅 10:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103421">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDmTF2Ylssby6oGHC1tvu0fu2tvnnZAKlUSOT34jM7z14ifUcMleCC2hw9E0_4iC0KPDIoTX-LBGkKWr3Vkgo0aDY8JliyfQAC62A8rWBlzdNOfAnXb3paCr0xszHtPlnvbuUZgChJ0mUwT18kQPH5WFtHvdwQdM5rWTU2ujTNqJQ8m--5Ij6E5g-YW1TcNqB36jCxWelvF31dSx0mRe5MMj4lvwIjNz8F3ppR7D52B7mnFg27OvJQ2VTrXvZ--U2IP1CSqIQGkVI7cgxWhOZIhvqsCAxeo-C1TaTzR5DzUeV2FyEYjXkHvV1Y3bXPz0gngGL2r_14EkxmWA_3RL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
تمامی قهرمانان سوپرجام اروپا به بهانه بازی امشب تیم‌های پاری‌سن‌ژرمن و استون‌ویلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/Futball180TV/103421" target="_blank">📅 09:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103420">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzeUJrvKglNxgapOWdgjid9cfpv4SrPWhmFbk4Ne-pAmXmQ4QkOCcIZtZ_JbD4-dQ5w6z0EPuZ4I1PG-v3lekEdZQoVeFqcHmY4ScOIBN3G8sy6Z1kpEc55EBWBLpVz2oHVFiVZ29vRuAb9cg7_aydWt9gbAxTRkXdcyA74KsbpJXgdXtMPbvBZHFowcFRPndo3Pek8C9Nw0IgyFh2MEq-3BX25aUJS7vwmabfXmdXJHyHJqvXezleZ-lCPLAxhPp0NbYhf1Id-8-I7U21IlEOX_lBdYO130WGZTqssHkKcVRxsoTmS3oPmedn7GrGAjqkz3EY7yujpWDb8uA7pr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اولین باری که رونالدو و جورجینا این دو مرغ عشق باهم دیده شدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/103420" target="_blank">📅 09:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103419">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea09ff2dc9.mp4?token=XoiVLUR_x24YN1xJ6cAnlfS7ICsARafofGKnF3y4_HsvY6aARq-3hFP0ToJnA8U8kGgYN2YNesTl5Uw2-1qZN6AlJ5nZGHYRanrGXgGB_uMGIb0bvI2ectP9R1UqMR-3sHcyhRzV_41sJ3U0kiE8sir0wlNvyuy8W3QB_9OWB2fZwpDSYhES6t5J0CoRQjPCqFLl0hhfaHvnY5Mkih0WmeAjImH5YnaV0LiZeuixIvI3eSZCxzv6aepq0_zZz6QTe0D5qEt9Lorg7sEGsm9uqqNetD4GdrG7OCX48CvJFFW5yf4yz3BxIin-fqDuYL-ZmV66JtoYnpnMVI2JV0Tm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea09ff2dc9.mp4?token=XoiVLUR_x24YN1xJ6cAnlfS7ICsARafofGKnF3y4_HsvY6aARq-3hFP0ToJnA8U8kGgYN2YNesTl5Uw2-1qZN6AlJ5nZGHYRanrGXgGB_uMGIb0bvI2ectP9R1UqMR-3sHcyhRzV_41sJ3U0kiE8sir0wlNvyuy8W3QB_9OWB2fZwpDSYhES6t5J0CoRQjPCqFLl0hhfaHvnY5Mkih0WmeAjImH5YnaV0LiZeuixIvI3eSZCxzv6aepq0_zZz6QTe0D5qEt9Lorg7sEGsm9uqqNetD4GdrG7OCX48CvJFFW5yf4yz3BxIin-fqDuYL-ZmV66JtoYnpnMVI2JV0Tm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاوووو عاوووو رامین‌رضاییان چه کوفتیه دیگه قرمساق
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
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/103419" target="_blank">📅 09:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103418">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV2-tUhlP3KBMBlUKponF5tz04wXAqcXWCYsvSHAFToKL9q1ovgr2lTcplOhxe2co6W6om7aHML7NDEE2oiN3n9DAOxnZf57yAnFYJn8O-kp0hXyVDwGfM1ifCWYYFsddv_OTtgL3mOQeDiX90RZL6AlJXwO0PLI6V7yldHq5TjucynKaMbWjA8u-wghWU1pJ9XiSRT5_ZVkAptlYFTX8GGoA678nvRxPJzaHNR5Q50PFv1K_9Eb_wthYe0SWy5we7aVHf1RJqgJq65hTqNA_umeUdYFlaQYTHdyUlcGo9LCPam6c8m3N4mb2uCmqRTpmYUvxR55LAdR5p1zNq0WEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
رومانو: دوشان ولاهوویچ به بشیکتاش
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/103418" target="_blank">📅 09:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103417">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcd964c7b.mp4?token=GugJh0ANMqryhb08l7fTx3FGQ5ceMsZwJ24NRfFuw-GNeG-VzM5MqB--ey3MPTD4KWYDUkxDMx-UjbOcf06PDYFRk7evEoYMDULEYdk8thjPawOmK7ihL-k_QPMgYwUcXp_IdsuEmYegrY-noHDyTMPX5IrisbnNzX5eYigFk2rv6VTtWwyEm-6H9qUo1RDXcNptDxcxrGzjXv0aIEB2YlYlR5L8Dw6lH5YrhNfPoHPfKjaWgCfaXBdY81SrnNyWcEgmp0K4CTNPI3W4TWN1X2UmOizL69oh7PEkiBWo6Bny4Ea-M-3ZIwwXz-98FMZ8P_5hCbEXJfTKAcWrYUaBAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcd964c7b.mp4?token=GugJh0ANMqryhb08l7fTx3FGQ5ceMsZwJ24NRfFuw-GNeG-VzM5MqB--ey3MPTD4KWYDUkxDMx-UjbOcf06PDYFRk7evEoYMDULEYdk8thjPawOmK7ihL-k_QPMgYwUcXp_IdsuEmYegrY-noHDyTMPX5IrisbnNzX5eYigFk2rv6VTtWwyEm-6H9qUo1RDXcNptDxcxrGzjXv0aIEB2YlYlR5L8Dw6lH5YrhNfPoHPfKjaWgCfaXBdY81SrnNyWcEgmp0K4CTNPI3W4TWN1X2UmOizL69oh7PEkiBWo6Bny4Ea-M-3ZIwwXz-98FMZ8P_5hCbEXJfTKAcWrYUaBAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق و احترام لیونل‌مسی و پدر فقیدش
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/103417" target="_blank">📅 08:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103416">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22164b16b5.mp4?token=ANVK5zThBsj_LcJDUA35emlTB4Kpu60mb7r_k9pz-NwadKCaeRuWbrk7uF3lu_QbiGn-PxWqmbD4ZqeSkwRz2QuKUBPc-G598c017GATgqbyy0dmzyqe1Hxu2t3gxkSsGxDMBXIjgiVHStJsufMUiG304rhJwvynLwAhKQ8hHdYXdVISbXFt493q9JqR2Why8P3fvN-WFnBj01NRPGsZLNI1aK4I1ksPnUnD4mPYaVgnuZ8N1YX6P5x5MVFBY_6Bf0pepgf1_SxogIbfvN4s9xbuFl9ptGVd5f37wAzhcHH_VIfmEAcXgIYVVteUcIKAwL04Z95Ey_RC3rmQtSjxDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22164b16b5.mp4?token=ANVK5zThBsj_LcJDUA35emlTB4Kpu60mb7r_k9pz-NwadKCaeRuWbrk7uF3lu_QbiGn-PxWqmbD4ZqeSkwRz2QuKUBPc-G598c017GATgqbyy0dmzyqe1Hxu2t3gxkSsGxDMBXIjgiVHStJsufMUiG304rhJwvynLwAhKQ8hHdYXdVISbXFt493q9JqR2Why8P3fvN-WFnBj01NRPGsZLNI1aK4I1ksPnUnD4mPYaVgnuZ8N1YX6P5x5MVFBY_6Bf0pepgf1_SxogIbfvN4s9xbuFl9ptGVd5f37wAzhcHH_VIfmEAcXgIYVVteUcIKAwL04Z95Ey_RC3rmQtSjxDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
یه‌ویدیو کاملا کاربردی برای دوستانی که باشگاه میرن و میخوان بدونن هر حرکت برای تقویت کدوم ناحیه از بدنشون هست. حتما ببینید و برای دوستانتون بفرستید
❤️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103416" target="_blank">📅 01:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v12FmJUaR2HXGO2LGnvKPG4PV0ZfcUlnfEh4ywWL7mcneJ7g5aFRsjBuKDc-PfD5HEU7duSt-0CkvgrLQfK2buhYPoGzlIf3PN3v6Gz-gD75Br_to8F9ptcW4YBVzQJ6gWnccPdfJ3uethKWIJEe375xxePMT7DBhnBuC4pI_w95ysMKaCEb1lJuUmeWd85HBuerAOr6vHpW0iVXGVv2xo4xpVMDuG2a6gdXo3g0knHzk4Mxo_ep7JGfRm6pDG114U44T2_hH6lL8Gs9eQ90BgXzqR_LILwTxOZ0idf8VQjPCEPkaaetaas3wCbEQzC7zCucxBSFLNx89dK2IGBBqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
رومانو: HERE WE GO فران تورس بزودی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103415" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103414">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/038cd39016.mp4?token=rIvON15YNBCZ2at9CAmM63uiffkAS0dl7kGTSZzzSjbKMiCneLbsu_z_E_zXgeYcNuwshpcKaCuWYCZfdIZptCjQ7n3RExxoLbLf8D64IYzkB8yRvRlO4_XaFDuFfZ96lnj96q1vvtuJtrWGP4UWdbQ-_U8EXns_7CQVA6SHPG_UEwTJCNSv3MSsOzFXfoy7H6q3oWqpP9jHIk-1zCjE7Bzuk86D0ili7ttyjgEMt_gb3f0yz3mbe4p3S1t9JwnvOlR0-LoJFiEBcjOnuPUknY1gPmCwfL-rTYQas-GbWxkkvmuoimSJvsPDEOdEY2RjNRnZGBQILXeQi1EdzN1zyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/038cd39016.mp4?token=rIvON15YNBCZ2at9CAmM63uiffkAS0dl7kGTSZzzSjbKMiCneLbsu_z_E_zXgeYcNuwshpcKaCuWYCZfdIZptCjQ7n3RExxoLbLf8D64IYzkB8yRvRlO4_XaFDuFfZ96lnj96q1vvtuJtrWGP4UWdbQ-_U8EXns_7CQVA6SHPG_UEwTJCNSv3MSsOzFXfoy7H6q3oWqpP9jHIk-1zCjE7Bzuk86D0ili7ttyjgEMt_gb3f0yz3mbe4p3S1t9JwnvOlR0-LoJFiEBcjOnuPUknY1gPmCwfL-rTYQas-GbWxkkvmuoimSJvsPDEOdEY2RjNRnZGBQILXeQi1EdzN1zyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
😢
مسی وقتی می‌بینه رونالدو و جورجینا حداقل تا چهلم پدرش صبر نکردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103414" target="_blank">📅 01:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103413">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpXz6zPfOCBzvr4WyHUSG1hzUKs1T5dv3CkyjWJddcO4NCfuNGKWdvQafjyhAjSGW_UvLxcM-wpdVW6jf8ar3KsSg59tbWfZfwq2nLJxc31CvFl9-3b1VUQomBciwchVk-kQprTyIycelQx5GLcywPwyZ-5fiAHYM-lUVvNKbalHaRUkAwypRe5fryqQbcAm8BRIx8Lua3jG06qjGIKhlqp2JGHVKPwqdKNP7txZCMTcCWXFeyMNMfhfMGL9ZoyUSL13p6lYdTf-a5gEW2181pGnMkSKKta2Wp8m5EyBQnpUDqysz-b8anG2VbJ_7sri2PZ14-tcYt-Nwix0jVu--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری از رومانو: مذاکرات دو تیم استون‌ویلا و اتلتیکومادرید درباره متئو روجری در وضعیت پیشرفته قرار داره و بزودی توافق حاصل میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103413" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103412">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKrI26iejkKh2ZJ8QK-qpRuJep8n6mTYrIM9Ba1lp5_IRcLHK3Ea5DzCLqJviC6NfK0Q5ymo8luzMsngd2fLlTi50oZLMI4v8Tq_iAoobYeUIyM-HkqJVUdKKmESV-NAhlb-vlnBfVh5AwzG3kpJCYky1jDmNutzMXo_pBFZRWdwTPF3XNpqOt6QKtT3pH7l15Ex93G9e0LhCP0nieyJa8_jOxH38CqdzrygVaDaB8voOQnuemwJuAYWCzj7xrHbBjTgR6qPhJveoCSjadR1oduw0W9PrrtkD1L1N-gsS1GwGqtiK8YOKtlcitCFHD9_bX2Z4AAiaRjMUefe63kq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
از جرارد رومرو:
🤯
🤯
🔥
🔥
🔥
دکو مدیر ورزشی بارسا با وکیل لائوتارو مارتینز ملاقات کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103412" target="_blank">📅 00:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103411">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLuEJx8Qp37o39CquVsNqDLpdvA10u4KyBcnt0tvUVQCn6y1CJa8F7hDCcVtZLRmtD5z8s4yLNzGJzI7MejfuwqVMPFTjWygSMtRIL5KeimgMCHJxTn0oZHR656uCy9dZpfJuT4B3tr2uPlYKEqJmwOW1CD-kX5gDrzyrOQHarcFSKL1DwV_D3wLZyyueLEd4kfS6ubZxD5vqS03U6saCFgOCEAKKHjjU6M7XsYRSQ7Vi1K6aI99-KudsSs0CcUJ_W-Ex1qkjKKUOlJJYQppb5i6dP7TG5-KbAWzVtVyp4YI9RgFH28y028f5-ozLKpna7VT93PiedDWKgjuvBG4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇫🇷
#فوووووری
از اسپورت :
🔻
بارسا و‌پاریس برای فران‌تورس به توافق نهایی رسیدن. ۵۰ میلیون ثابت + ۵ میلیون یورو متغیرات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103411" target="_blank">📅 00:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103410">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObaWZ-ibng1FXVcZjOC5pmcMIW8Glh2pKummKVTiqhRDJnw0js40IDLe8qyYnIn19SLdyObl779PWgoQ3HfyL6-Qp9k4EkmVydP_3TjaFDi3cSH2OLt8x-tb-JP5N3fB2hXWw4XXsbOhSPyInON_ydkTuX4W2cd8a_aGItIL8-Dqkbs5fuYesKi72K3BmS2QgPyabBUdUE5UEXOFDqIJEUMaGXI9pkNB0mlLlRJB-PSE_mjiXCLZ90GrYviBm7Kinlqv0jOx8IUY3_cwseyHSInKEwmf7YHkmPW6z3An-GATUKUBx5hFif9ZZKod-nPcd6liQ8YWe96NPdewmwUSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇺🇸
#فوووووری
از نشریه The Athletic:
🔻
دونالد ترامپ بزودی شخصا با روسای جمهور کشورهای مختلف تماس خواهد گرفت تا صندلی ریاست فیفا را برای جیانی اینفانتینو تضمین کند. ترامپ بدلیل روابط صمیمی با رئیس فیفا به وی قول داده که تا زمان حضورش به عنوان ریاست جمهوری آمریکا هرگز اینفانتینو از فیفا برکنار نمی‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103410" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103409">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c334f75417.mp4?token=LnEFhI03PrtbaHUsiwqMoZRpxNrfvnkkuf6b_4NW2SGHm2jbIe80B-qG7mQ4HpllY5C_1KLQHVWuDXYGnR2ocRb8jkTQEqZbbjzNfV5duTRNRpWOwrNV9cLNPYzhpuqooE3YDRU7B1c0zYnGNb4lYd77eZT3wYi6SUKVYgpbCNNJUBOT6b2OLFrd6B2Wb-uW6V3Fsptj_BUxEnRChIm6GTp71_RsCVZpRYj7WS51tZRBzYlAn-fD3NFQthln-5NCT5OT-MrjkXZMv5_sU0zQG9BpF74AOCO8ADpKh8Fb6YSPMNt2abbLEySPJuAlWV02x3iRLxqkS0ZBOBlZd5obAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c334f75417.mp4?token=LnEFhI03PrtbaHUsiwqMoZRpxNrfvnkkuf6b_4NW2SGHm2jbIe80B-qG7mQ4HpllY5C_1KLQHVWuDXYGnR2ocRb8jkTQEqZbbjzNfV5duTRNRpWOwrNV9cLNPYzhpuqooE3YDRU7B1c0zYnGNb4lYd77eZT3wYi6SUKVYgpbCNNJUBOT6b2OLFrd6B2Wb-uW6V3Fsptj_BUxEnRChIm6GTp71_RsCVZpRYj7WS51tZRBzYlAn-fD3NFQthln-5NCT5OT-MrjkXZMv5_sU0zQG9BpF74AOCO8ADpKh8Fb6YSPMNt2abbLEySPJuAlWV02x3iRLxqkS0ZBOBlZd5obAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
✔️
ده روز تا آغاز لیگ برتر انگلستان باقی مانده است. پائولو دی‌کانیو، شماره ۱۰ وست‌هم و ستاره‌ای مشهور به خشونت، در سال ۲۰۰۱ جایزه بازی جوانمردانه فیفا را دریافت کرد؛ زیرا در بازی مقابل اورتون، به جای گلزنی از موقعیت حریف، دروازه‌بان آسیب‌دیده را کمک کرد. او ثابت کرد انسان‌ها سیاه و سفید نیستند.
همان‌طور که تالستوی در رستاخیز نوشت:
انسان‌ها مانند رودخانه‌ای هستند که آب درون همهٔ آن‌ها یکی است. هر رودخانه در جایی باریک و تنگ، در جایی تند و خروشان، در جایی گل‌آلود و در جایی زلال است. به همین سان، هر انسانی همهٔ قابلیت‌های انسانی را در خود دارد.
👍
دی‌کانیو با این کار نوع‌دوستی ثبت کرد، هرچند رفتارهای بعدی‌اش بسیاری را ناامید ساخت. اما هیچ وجودی بدون تضاد ممکن نیست. نفرت یک انتخاب است، اما باید فراموش نکنیم که جهان سراسر خاکستری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103409" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103408">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103408" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103407">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Hw09oktxPqdYK-WnLIR_VaG6pUxDPH7pe6b7A3Vm07NRzwP3_-ROUAp_3I_YeSM2SAC9QS2eLJLnUvATX0JcrtnZ-P4wiEzPT0lFizCkD7Vq-uS3MumiddvD6i7aQwD92PcVgtOYYNRnmow3YsajE3zc3vbh1DQ1hs9A7-BBH8RXhf5sGmOM3-5wysjyjeDMfe-SQKWl107r2q7eepj2MRyCJ7PxnyjReDF6kcoj4R_0NoaYfe31NhW3UJs-IEgsoYOPeT_IdWLWP9JMBi_RVwfhJO3vmmvCUD9E4wt1xOJfsig6ooyeQOCRLqyKypEQTAWLUoQkgJ7EXur3AK8_AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Hw09oktxPqdYK-WnLIR_VaG6pUxDPH7pe6b7A3Vm07NRzwP3_-ROUAp_3I_YeSM2SAC9QS2eLJLnUvATX0JcrtnZ-P4wiEzPT0lFizCkD7Vq-uS3MumiddvD6i7aQwD92PcVgtOYYNRnmow3YsajE3zc3vbh1DQ1hs9A7-BBH8RXhf5sGmOM3-5wysjyjeDMfe-SQKWl107r2q7eepj2MRyCJ7PxnyjReDF6kcoj4R_0NoaYfe31NhW3UJs-IEgsoYOPeT_IdWLWP9JMBi_RVwfhJO3vmmvCUD9E4wt1xOJfsig6ooyeQOCRLqyKypEQTAWLUoQkgJ7EXur3AK8_AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103407" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103406">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swUFrPWEox8Bai0gsxNeNMjqZbYT-PDsz46tZnFjx1GWMPJo1voBk01rH4i-BOPPZIZEtlT4Y9pEiQJxNeow87MgNpASaNaz1YgQvneQlWvbzXKlt7hzl0TGDul4ridmnlbakjyuFjLRnCKkjGRk_jsSHyte4ScYlNjD-BYhFEfTZoB2npoBGlWCnfXFL5yvQGYfh4P6muGOFdgY2V0n6NrRfMkQac04oXd3odCncwIjCFWCheICg1jLmEWKewxmCzopcBuhiVOXGDLzWFY8UnHk82nmuJrn0EOo9PiGpcFC6YxycV618WNE1E3n9sA3kIbELMc5CTbgse20R3wUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
کسری‌طاهری بازیکن نساجی با عقد قراردادی به تیم‌فوتبال سپاهان اصفهان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103406" target="_blank">📅 00:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103405">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkfCBra3R6l4GPKGYHh9X4MB5jzk8YscQnOnc2pvv8hPR0P32ygdqKbRZqggO_AN4LYt4Xt0jIiom8fA2y7XQwsh0hPWVOWyQEqmxXGZBGP5hIGb989zgrs5KJ3FIU-8gY1kuqtRrNI54XQPxLiioeU8LPM6fW1BhTO7R5JlzwxPrZL_mPvKG4GWyTTcT4IiC06_1VuulL-Sr_oL4lFFtoMN1bd6mF7YxhUtmMpDmFz_okcH4-dn4naASZW3E6S5iDGaNxn-eVzeyxfaQUjFGK9iRWKGEDxwlouaQmtJUV5XdccBSAKJRLaJLq05zGbHJQbUWsw7k280g2Zgq5fUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ستارگانی که ‌تو لیگ آمریکا و عربستان بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103405" target="_blank">📅 23:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103404">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnQqt0q6Odg7peH-GC9AV6Wju3O_iwFinQkxw1IT5f_uvCUqKNkQafMne_Lo7cWpfFHp4HCk9MiiTynyQwAeOq_vwIVAH3eMRawQSU_gC2L0MuS0Ab5GAcB6yN_O6CvD4TrmA2vC78HQM0eNuOZ-EbHR0Bp_SloCTACWPy-hXZJ9ozsBVBpDY3_4pDKnQSmWOHCpLdW4gd3fcwYuWmdFkElJ5NIqQC7P7dYw7cwz3K2O4ACoabor6fpsNTWzMGnRKCsWJCUwcAkUWPIpXXKcQ_e9g0RrwCSWt9Lag0mGyiE7z3ISic_m55DL6-Sg9Jdp2ZZXZpthKa1y0euLny6Tkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باشگاه کورنتیانس برزیل اعلام کرد که بخاطر مشکلات مالی توان تمدید قرارداد با دیپای‌ ستاره هلندی خودش رو نداره و این بازیکن پس از دو فصل از این تیم بالاجبار جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103404" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103403">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmTQXJhuWc9HYT5t5222jzqcEHm9i3cwa4Xt5LQV_4QbumKhN8D_W6RJ5dld2WuVN8t1Qr-cV1XMXPlNz3AotblWMyHOqk-6jNxmEwwA-Lpo4Wh_71JA6asKQVz97uT-YwWxek-a_4TD2-__v1Q0hYEDiUUJAY4cgx6O1dAgrkhyufAJk-bcKl98gyksHFK1LxXHD_IpSaWoi14Yg-cRo350xOEmN9dnthrz4mTXrdjBDpJGlXRQMrDSqJnotgZI_NrYB3DZh0WdYyvR_ngaXA7sz57Sti_95MP1UD9-HBdVa6cyJ15ftkMzL2dlrs5-WZU3aMBEZfv8eX5rWoPFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐐
🎙
مورینیو (در مستند جدیدش) درباره اسطوره لیونل مسی:
او یک کابوس همیشگی برایم بود.
☠️
☠️
☠️
ما چه کاری می‌توانستیم انجام دهیم تا جلوی او را بگیریم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103403" target="_blank">📅 23:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103402">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUo-T6O_HQfhtJUiUGeJh3ZDSIDt6_r51Pya6TZIYqI6fN-CL3ekyHBhyuxx-qXYIY3NboTcvi9rmhKVFyR0Inc8g8mN0GL6lI_YAnXRoXj8QewNZDB3Hwq6QZmVSB8WaYn2NktFcHYUOE6MznwdEeP24TSo-NotjdQjRZ_RUbP-BtcNZJpbUZnjbEn_2MqKzO6nenPsf7dXXEUaOU5SlVanYaPBp-B-up-PXUjmjN1Q-7R_hCLCjKfyNqFK7BXSuCtRlWk9MecwoThGZNe-Yijrq3oHeWOTrtlRZin3aBVO2rtv-RSLf6azqkV4NKr3jj-BDyB16UwKDmXZgxzU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رونالدو و جورجینا رسما زن و شوهر شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103402" target="_blank">📅 23:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103401">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu2fYgHoJqeSjP_S_Qn6CSlVoyZcJ-dZDNn_fZp-WC9zD6hxQXdwcDY9BtUycCV_pm4gnn1EzORmZqejHZuLyeZTXlRPtrlejFmwuX-S-3TjvEX_lmoUY6GxzOPotUH41_IpYog_1xTFPYpDzuTpkK1v5e_R03L7wCQiugL20I6RrasuM9wqModAt8_zack-uc3B6w8TXWwkUUJDHB_P8S5yP2Vu3NzLC6uT3oQx4mEt_2rUD__gCk4r2Gw6xPuZ0IZZa7NVoaA7vJDoVPPWmeiaSA-2WdIsuP9f5ED4qBwfrlLrLTMkbCjRKrD6f8ErAitNKPU5kBqPJw_NolhmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: چلسی برای فروش انزو فرناندز به سیتیزن‌ها رقم ۱۲۰ میلیون پوند میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103401" target="_blank">📅 21:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103400">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M93KxMN6wktTspCLvoJqivnl_F2kE1Xo2JnxLhs46fdLPtzJcEsJUm4Dp3KRm_nSJ7gJMmTmQEQhQ1dqdbULur67c-F0b65aIKuSWmThNdqOIHVoaIcxNuwvlUmW7g7qaH-dImLY3IYlQxAsUV2WsYCfzmkvIiOMUdjXQFaLE0ti0YMSqjT8ooeRA-KFeR-Q0D8PspWewHnEoH4LdDAsuFN9iHKBuEa7L_cZvVNqDlnBcZQPbY4-jpc-izbsqo8D0-1HNLJ0-VlUzFSgjOJyenG5yOuZ6Uz_oaHLjBJdjDTMi1hYsnqcKgajorrtWsvgi4RK_MAx7BkbCFOsVl8MKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
لیست ۱۶ تیم نهایی لیگ‌نخبگان آسیا؛ استقلال در سید اول و تراکتور در سید سوم قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103400" target="_blank">📅 21:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103399">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km_KLNVY6uWoCZW77W8-YLgjPdJq92HCD0fBhcthc95mR_p25ICoB2IzQ_5MNxJQCM_vavaIxqzaiGanBqUhaJvEu6G-IVagQCUOcawzhsHduxdF_NIh9h_YiXUCzpcB-nsaPdpoaXxLHegY7sJde5sAoe0LkLzNiZbmhqjSxsgPiusFMvXgJstEePoDrd5r28E1masnJMjC0Et4MBr8QnJLOSs948Y_rMsY6yb3PeH7NROyjwKFqB5HlhSGM-zw9Nmx-g0t1NcRMJDX1SRIJ0m_pqVH4mD9ZBlmwVXGd9Er0lMH7uzRXzGwAXQsDsEV4tpq8BOHsfZIGOl_h_jZKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فوووووری
از روزنامه اکیپ
:
🔻
باشگاه موناکو بدلیل مصدومیت پل پوگبا قصد دارد قرارداد خود با این بازیکن را فسخ کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103399" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103398">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGk8smYuwxx9WalP14XvxNjhPZ48EKOkyRqigVhi0GH1XwIf2LJNh5TP3FKsskqT-fbsCrmE-_K5IZdNAmju8Cb9bb8SohDfNeUxitadFpcKRovfAfJS1A06sAXWmtph7YkPfQKHSNbERRNL2OMlq-0xM8rjswYV6e7N4ozK6zFdzDP8wAI7H8OgZ4M6OmvBJjV_E3tuh1AvoUdLHWdlMH6fMhBqu3P3pg9xiCanuJkfRsKVvqBgISL-5EqQEqymO57VI31TzyhzMauhnnjbq7Ge3BZGxVFS2_y1M79KCSAZY8MJDbfliknvOMprrVdyK92NE928Uc_z1nc8livACA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ویتینیا:
توپ طلا باید به یکی از بازیکنان پاریس برسه و انتخاب من کوارتسخلیاست،‌اما نباید بازیکنانی مثل امباپه و هری کین رو ندید بگیریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103398" target="_blank">📅 20:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103397">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCakXsk0foBWH337nOJOwV_f1rGruBjA9AwkbKLk9ajrmkiGxS3cHR9clWXh70upn22qRb4uYZTCFHEB1KF9aHuliKZ33PCz1zftgIUP2nKL1YPi2cCI6G_mZK-0OOwpYI6oEZdijCjdhh6Gxv3fei7nbyK548S5ZMtLp3EvsimiZmz3oOYpwi8PIPq_50cbjOUpNkEHi4VteQlLyO9n46-RqdLu1zgvof7_J3MNkYwwJ5dbHX09O5FLoI7pUNhLnRwCIlQv4wMEPaPlsEsMaiQTnWt1pRQrhEEfOG5cIivcXuDG7BkJgisQlfy8NCpoP3K9Ay57PctcGlcsZFEgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
#فوووووری؛
🔺
هلدینگ‌خلیج‌فارس اعلام کرد که سهام باشگاه استقلال بزودی به چند شرکت یا شخص متمول هوادار آبی‌ها به فروش خواهد رسید. مذاکرات در این زمینه آغاز شده و بزودی نتیجه نهایی به مردم اطلاع‌رسانی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103397" target="_blank">📅 20:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103396">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nel3MqkXwPKRzybg8dLrTOwFPJ54x1lZq6W3fc3fhir2YoUaKEIxn5CKQaVdrs2LYtrIqNkvvafo_LRuNbbQwu71CocMGEbaXkRr6Le50fwSX0t5jnmE5CNkYmbLxs832FmewqyURQtuDwVyUGj2lC4tgYR84cRgeRrulCFc3iDsTOxLsCPQg1xdTZUXTRXcnUb0w5AaScHEjFt5H7lcktmm-4yO5gWlC6pbnuiSscd0jZrLr2IBiGDITIThf0z8JbuJRbGEypG9hWEn-aCyHyyr7aP1lMtMr_ZWuK8sx_HKKIIFoW6EB64sziwVG7zpvYFuD3PeeHPFXcJmEyQq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
باشگاه پاختاکور ازبکستان با برتری مقابل الحسین اردن راهی مرحله گروهی لیگ‌نخبگان آسیا شد. مرتضی پورعلی‌گنجی در این مسابقه برای پاختاکور حضور نداشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103396" target="_blank">📅 20:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103395">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG8Q1o3f5arS_SYSqpyMkwvtrR2dJZkuSX8FOPMpHzkrsygDOl8W5bP4qduAOoVvuC1y1QoDu4gPmTNpGcVq3krBMsTXiZbWVNOLkqQXX9cLGy2VUaZk7o3XqkFI56GNB7dJiigMz2NG36qAGJrt0eTNHXkH8BWa8bH8r2Qm8ijEmHZnD1b9z8FkohU-Sm9rwhziMaDmsxOqVoWLBAeL1v-lcenoZYvtYljPnLjsbZqYpC3XQOQO19o-DWiiLbIb2cmipa4Wrlhmge0ISgcFoZCtAB3P_3HKDT_-hevzUctPSQ2ZLh080AJc202QEqHBGqAoK4-NI3tWryOgVGnjQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبتای جالب مورینیو دربارهٔ کاسیاس در مستند جدیدش که از نتفلیکس پخش شده:
"اولین سه باری که با ایکر، کاپیتان تیم، صحبت کردم، اولین چیزی که بهم گفت این بود: «اومدم درخواست کنم به بازیکن‌های تیم ملی تعطیلات بیشتری بدید.»"
"دومین بار که باهام صحبت کرد ازم خواست تمرینات رو یک ساعت عقب بندازم، چون ساعتی که من می‌خواستم تمرین کنیم، توی مادرید ترافیک زیادی بود."
"سومین باری که با هم صحبت کردیم، بهم گفت: «ما نمی‌خوایم به هتل بریم. ترجیح می‌دیم روز بازی همدیگه رو ببینیم و مستقیم بریم ورزشگاه و بازی کنیم.»"
"خیلی زود متوجه شدم که حسابی لوس و نازپرورده شده بودن."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103395" target="_blank">📅 20:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3eRJM_8L1Rp88KxSXGcCSHlYr0I82zP3tC3VLlu3RuqXCTo0SnxmsN-DRADtjE3nm84cPUPWtnK4X-dQGoQaSDP_5L5zwBJAl80wRFWx6McyAq-kNMfJe-sxk8zN1hCBLbHFdoj5Hzzs982nCNxUUNECVKaSNy5mIXMwjFwYzqKVecn4Dw80_FRyFVYiJwCtrFODEQSBXLkWjZr-nNmx4ey1oV5bJw4-3i4HQr3Ou80Fm_bFrV2WaITnVBzY_VN_PEJnVj2L7qWRbtJcq7Kyk-BHl0-_hUoJUuwNlMeOIZhVagtp7P7IONuQ0ahFW8RYKKGudN5zI97ZcoPSGkIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار خط حمله اصلی رئال مادرید در فصل گذشته:
🔺
وینیسیوس جونیور: ۵۳ بازی، ۲۲ گل و ۱۴ پاس گل.
🔺
کیلیان امباپه: ۴۴ بازی، ۴۲ گل و ۷ پاس گل.
🔺
یان دیومانده: ۳۶ بازی، ۱۳ گل و ۱۰ پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103394" target="_blank">📅 20:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103392">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWWeHcx5Z1emST7Q_ekXW-sPzRBYAe0SZE7kEoddUfGPfmm8lrE61YRdzdztRpzfPuVwxZwpkXmYssKmABv37NoN8UkNHFwkmx_18ylu8UKjay04gCfjHe0Q91Gpsz6tsw-mh_XCPXTqqOc06_akVpFTH8iHcWQS1Jqa6VFGz8vEn5vLzs_kCzy4zuZcr4Ib7UhCeQrCmxlfYFvi1DGjfANCyqdqxa9mLNT0LqsYumIQyBx0MLkgvqmkdF9cMpIUOIFOLN5DCikd6fmNiI-WjwdVx8iKtD9ZR5towOnL1CoBZa5YRrg4IKF9Z68EgVEkRE8lpK6YL2o5yf6q0F3how.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Altdco4f-CMRuwwNZJqjYLFF8PLvw5pEa0pZFy0tTnfl4QR8g1f4njVXx-lETuMIKtv-NLUGwNJTHts1yXHHG5jzot8D0qZ9C8UFGu9WFdCVPzr8-glH2Tt5meH1Y6oCjfL-X9TS1F5pkoav0hOhGkIz-A5JI2LyH0DE7KsRC1hzlCu9Qy1LzRc-s4RWcNYIto1_yztfGCSdlflLbuGrC7zV6l0FJN7ZIXJX--rJqgnPy1DRtkBfynSoB5dKc0u-FlXl_4Sxgl2zRur4KXP46T5iVTBS8Q2k0ZqBHyAF1YuI13lvvw76GB_U5fJFmmIT_LKEvM9J1Z8O4mg82tKHEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👟
تبلیغ موزی پدری برای آدیداس
🍌
♥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103392" target="_blank">📅 19:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103391">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAUSIi7ExO8WjtAVNHj87VKQuXi_K0Id5bbtXgTjklS6YEtsojnJ5YjIIn2_QYL4uobGTcaY4TtIxRpNl7ZkT5bZ-KlU-ZFEE12yvRoJZkHqlDvuz7ThlgIrxSgJ9iAEJI60K2l4UmME3h5J0udGfTXwPV_egUZOoredOYvJVof4eOYozTgcmhsJvPPS-jEzefhi8HMU_gRU4kB1qWaxs1Bzf6zTgujjea5HixPnLlpnSkHNr5ObsbCcFnbzy5TVjroMy7uk24OaowVe9XJapN70UXUZV3RGeUUGO8PH9TptA2YIy_pscwiAyGfqRxFDYNXelc5QSQgOiDVHOq4dsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوست دختر جدید گارناچو؛ خارج از زمین فوتبال اوضاع واسه گارناچو خوب پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103391" target="_blank">📅 19:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103390">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2ed3bb71.mp4?token=dagLv0vFysDVopoO8N_6UmqtzzV8oNu5MVEBTQI4JhwIw5dTns_4qjz_M3yFnTQuuXf1kbESOXFU2H_0vdThqexG-T1VQZF_mdoAUzf9L3IXxd2t4957J1SbwWGfhAT1BfQoBuV8eb7wxPFcyO4C09M9KPx5IuHMCqBI4OJH7rKeDvguK_C5PQGiHMoNRTVTwMEohwMI5NGmMcl9Re3F3PRjJp2aoITTtcaB-9Kjg9s8PS5FS-_lQuHIPIKJapzzJ-xUwbJP8PPpg-ffkp0gHRde7C7VMyp8DwShNJp0fRLauuZGwXhMwnAtMj2tHoPU31nzwF3pByMscHxutn7GlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2ed3bb71.mp4?token=dagLv0vFysDVopoO8N_6UmqtzzV8oNu5MVEBTQI4JhwIw5dTns_4qjz_M3yFnTQuuXf1kbESOXFU2H_0vdThqexG-T1VQZF_mdoAUzf9L3IXxd2t4957J1SbwWGfhAT1BfQoBuV8eb7wxPFcyO4C09M9KPx5IuHMCqBI4OJH7rKeDvguK_C5PQGiHMoNRTVTwMEohwMI5NGmMcl9Re3F3PRjJp2aoITTtcaB-9Kjg9s8PS5FS-_lQuHIPIKJapzzJ-xUwbJP8PPpg-ffkp0gHRde7C7VMyp8DwShNJp0fRLauuZGwXhMwnAtMj2tHoPU31nzwF3pByMscHxutn7GlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
کالوین فیلیپس هافبک دفاعی سیتیزن‌ها با قرارداد قرضی یک ساله به شفیلدیونایتد پیوست
منچسترسیتی در سال 2022 برای جذب فیلیپس 50 میلیون یورو هزینه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103390" target="_blank">📅 19:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103389">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDJ4HeZas9X_hpxB1srDk4ULs9tDtB_7iWcT2WH6CbBGcvc6pIn4TAY1WuFCx174kFYuoKoLJ1jcA83rqNCfO1EyZorgyo1GXIeedb3b5K23FTi_idPrVqxk9bNaYaH4vgPxK3DHjYYu5mU9Hyel5r2Erfwlnmmj-ffssBSdonhuJWUblGqDpEYuPjbvk8ZAQuh7_3kB7ZI5ioUImN0Ow3WSpCGZrxKBxAJHIGlppgKgWkZTmFuppcGbQaZaKh1-2ONckl2oEJ2ra59g9M7ApNuYURWqqKYYx-kY7uI5xaBKTD-dbTorCJgOpt5KqwhP__87Jj1reI6YZSiNgkMtoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
خولیان آلوارز بعد از تمرین صبح، مجددا به مقر تمرینی اتلتیکو برگشت اما این بار به همراه ایجنتش!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103389" target="_blank">📅 19:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103388">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🇦🇷
خولیان آلوارز بعد از تمرین صبح، مجددا به مقر تمرینی اتلتیکو برگشت اما این بار به همراه ایجنتش
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103388" target="_blank">📅 19:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103386">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QPgocKbaaPKRiPdJxEt5-ajTTJg_Bi2pxiWL6McF9JvSMmQdPPS6zishgxFxyElwQwmzxw0vcGsygAc4SxlVB9M9iJOF7kh7B8k3UVcmER26iB029y6sKImOp-9KRm3yxKbMIFxOdtL_QjG_zPqnyXjuQhHeCdBCpGZWMbUt-XbRZrrlkjZRMZ5kLZs0V7KflqllMogZ3ILjdZpL5iMdYfSbrArDbUuBSxTvhpWzvUG49BO-fJ8yWkQPuOHOmxwKpZJbHpriwPJAvdPmNqramZnlm_xfzvT4KGgsacvTAkf6CpgPkNCS7ru0ld5zNagc9SYh__NHlgSvIzxO19OxOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vo3z5oAJNN0uNEkBE5cUtMWQIfPrxYufYq-eLOFyuGwWUxNU6NRnqUslTZKfKpqT9f5_1kuF5k7RpzikHsgYA-pIqJ8sG-m50rakTiEi3qOAg6omltBmqEJSxYNS2jE6pyS0tAZHqCbDkhaLBeo6EcWGd01STfyV5VQzCkyewqiUJ8PeL4VP-b2hAkeaasfINUt0PKYJD-BWnL1KoPE669El0K6RA0PO67L4we8yeEWEkEKzZMsMk8akLtBgcZgq5rgxxvcKTqlYziPLWTSy5ivt2jQucHbpsxGynoq2MgmBq_UUfITiYj78sY_Ldf2TEkvssJwOgLc89kJ8e1MdDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
امباپه و استر اکسپوزیتو در ایبیزا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103386" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103385">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHv_lr4slq08DHfDXneYCmpp_D11fESrzPsyUpHMyEP4E_FP0H0HD9pYQSpsRBZxLGwJZMY74wUVRfJZfTYNs5usd3K3lzzD-PZ2ByC5ABAgRtWzpMCPXrjMiVEDOiMYfnMO8hZUxMqdp6k4RkjEi8Se6EjisQ5UFfRfKoL8DKDKApQjrBFMF4ItWuMLNfhPMZiiljXoZm0I22ShqA5SLuHoIGPfWVR_YYJz-JATC2-Zl9me35AjHuj4ypIj9-vEAsmVvKnUcXDhuavZVSUppjT0_OEj1FfCLVy5dd-J4ZFRL9fuWHtLplWfUkf5nty7Zy8FO_k4PfVAvnOhQ1hjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
واکنش روزبه سینکی به صحبتای دیشب رضاییان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103385" target="_blank">📅 19:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103384">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5J1jyLvGciLTs1g5h3PLRoo579l42Meh5YOz55fPoI33aSYHG8dYBaEASX4pgXaaGeYOtAQHu40IKV7jrG_J_uHt-ARoBGkHIvJEMiM-2ih1y9YcRki558BAJZk3ulwK-dFSwzJd4mX-LAQB7m77nxS4atFIVfAErFC6YNGa5RZ3mYveQSxaf8tbnI-bkYbc-KWxxAJbCk8m5vUJkQYeiT-5-B3GDQT0DEjAJ3rRkLktijNF_4q8k2ogtd4_8EpHN5xHGMgR9H8d0nHcuLoQZt6Ks2dLXYBm3codj6cwtFsIsKdkDNOHokHmEVr0ZL1O4hu8wT8ezZ_nmixBU08OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🎙
ویتینیا درباره جایزه توپ طلا:
🔺
‏
"به نظر من، طبیعی است که یک بازیکن از پاریس، مانند کوارتسخلیا بعد از فصل درخشانی که در لیگ قهرمانان اروپا داشت، یا دمبله بعد از فصل فوق‌العاده‌اش، یا فابیان که همه جام‌ها را برده است، این جایزه را ببرد. به نظر من، رقابت بین این سه بازیکن خواهد بود و من به یک بازیکن از پاریس در توپ طلا رای خواهم داد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/103384" target="_blank">📅 19:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103383">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fe3eb369.mp4?token=eEVOHPjFgjtLbYoXvUkIK27Q2WzHCY72LgDTZ_e-InLiaB1TZsi8bVuoW0VyaPfykP_qTaezs0M8yBx4_2vyuY9CCykJmMU6hC-7W6nK4HhwkZPj9mSw59DvAhawhvzT0W9jxdweqQCY2pkNfQXneo7jUKL1RkFCCiJgGSeRx7ajB1xq7yim2lYYHH4N0Kcwe2uiWYTlr1JFomw8B7wDp-uY_tOkRHlXc4Y4CJB4UYa7tiXC4e1V5_rpRyOs6UKHO7EiYPrl7Vr9gD0-4VI22HpMdoxlH1M5DYLHxCvum1OtEuPK0MCW0qAuF7lR1l_7bJk3H-9ymrxY_X2oebwOY1jaOganfFnu4n5KKwe3aFyS-TS6xyi_BlrID-4zR-Oi6KRtSPwbmfVp4nJ16AsIi6HczZUgTXcPcZyOMQv8P9ndx0a8cC78VTWoy1oq42kTZmWGkDbUcuwNE21brIoNSbl8zlGwbyGzgySBgV2HKKQdtgsRG4qQKiFPQkk5O7ztnbIfediyaZNExoMAVkknavFkW6_KexIN6clJH-c8sYblEaXDU6XFipEl4KM0fhZnKe7tWYNW7I71SbTN72GBL0pRi6G_KGxC3TluSL307N-AHGyflT4tELKsay7Rv8pOlCkD06vdzqyx7Vc-0nChWlcF9nQqjErlJLNUZZxJ2Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fe3eb369.mp4?token=eEVOHPjFgjtLbYoXvUkIK27Q2WzHCY72LgDTZ_e-InLiaB1TZsi8bVuoW0VyaPfykP_qTaezs0M8yBx4_2vyuY9CCykJmMU6hC-7W6nK4HhwkZPj9mSw59DvAhawhvzT0W9jxdweqQCY2pkNfQXneo7jUKL1RkFCCiJgGSeRx7ajB1xq7yim2lYYHH4N0Kcwe2uiWYTlr1JFomw8B7wDp-uY_tOkRHlXc4Y4CJB4UYa7tiXC4e1V5_rpRyOs6UKHO7EiYPrl7Vr9gD0-4VI22HpMdoxlH1M5DYLHxCvum1OtEuPK0MCW0qAuF7lR1l_7bJk3H-9ymrxY_X2oebwOY1jaOganfFnu4n5KKwe3aFyS-TS6xyi_BlrID-4zR-Oi6KRtSPwbmfVp4nJ16AsIi6HczZUgTXcPcZyOMQv8P9ndx0a8cC78VTWoy1oq42kTZmWGkDbUcuwNE21brIoNSbl8zlGwbyGzgySBgV2HKKQdtgsRG4qQKiFPQkk5O7ztnbIfediyaZNExoMAVkknavFkW6_KexIN6clJH-c8sYblEaXDU6XFipEl4KM0fhZnKe7tWYNW7I71SbTN72GBL0pRi6G_KGxC3TluSL307N-AHGyflT4tELKsay7Rv8pOlCkD06vdzqyx7Vc-0nChWlcF9nQqjErlJLNUZZxJ2Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
رختکن جدید و سکسی استادیوم نیوکمپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103383" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103382">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbef9d0be.mp4?token=cS5A8t9jlzNZTkEML368b979g3C3xvrxB2iuCmJurrCE0XmGufQC77iPK2neFap64gyR9-y7eRPR1rJWlghuSwJigeUB5Xyl9GGk4uEolMPMie86VSqB2yeZxCaaqSDIrBu4ZRGi_dXWcEmMOk3PuRm0OOApE7agzF6jHT-i_tKTfepw4Hm1RD54-Zn2DW7lhTYLm7KZ1HDSZNZAyMtY6HvGZB3wFo1NCYLAxTaLPONINGb-t6XUYw8BplZY_6f_LO5YLw-NyzPDlUSVhtDrDS7T5mdky8SMdxL0zA6f_sb-hWOSJN7v9eXZQWomlKCt6t0V-DI-oinB1AacXK_JEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbef9d0be.mp4?token=cS5A8t9jlzNZTkEML368b979g3C3xvrxB2iuCmJurrCE0XmGufQC77iPK2neFap64gyR9-y7eRPR1rJWlghuSwJigeUB5Xyl9GGk4uEolMPMie86VSqB2yeZxCaaqSDIrBu4ZRGi_dXWcEmMOk3PuRm0OOApE7agzF6jHT-i_tKTfepw4Hm1RD54-Zn2DW7lhTYLm7KZ1HDSZNZAyMtY6HvGZB3wFo1NCYLAxTaLPONINGb-t6XUYw8BplZY_6f_LO5YLw-NyzPDlUSVhtDrDS7T5mdky8SMdxL0zA6f_sb-hWOSJN7v9eXZQWomlKCt6t0V-DI-oinB1AacXK_JEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی چه کوفتیه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103382" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103381">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/103381" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103380">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INCrd2X5HfUyCPY4Q_liLRA2694Hs1QRXG1tRBkb6cOFAOSFig9-r1S6EJ_iY7GshQlbLSIexTqJNGYYmA2lkAUquWSIhRKZ9-aU0hlyyquudiBuR2k3ZA1_IGUScrWRUEWCeB5Mbf6sp6uxMgOIiZs5IcxDBBS7FhWu_-3SYsb5t6yjGkX3vR1vASupfhGnGVbMvuVDCF2eAtwp-ApJXe2F7mX5lE-sn9gRGencHRbuSI0ywIL-EubqHGq3C_8a49T5lI3EJmpP2mGgGrWTYjOQe_qmSPPCIKx0M99pFeH6SNaVhfRYQ68CvtvEjp6jMBt9sYyhvzo42cacJ5YZ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103380" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103378">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npMqFp5W3FszO2reQNYEHyqbc2I4vQuXBrE6EVksCPDRNTqbGZW5zcJuC_CWMpjT3W_o7UwI8MMUKjHsr7ufBpJZC4x1wGUH4SOcvNVBlF0iFP5VETrtYt8knOaC6yrQ9bF8XVwL4NAIsFOH9ixsuN1HGtK8mIzRMOPHNijy3Y3TC4R-ylWVVo2iH0nC8_2JANyNLMhrkvb16NfZta020AqT6nceKnp_ER1aLrGYehvlhlR56VscDoAMv2z2aoqtDxGFlo8Czrr1UAEz54rJqwF4wi080MhS2ZW10LM39JyCvCtAebjhOAKGCu2-P2fI1-zLZTNXNQHzDqb29rtRrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میبینی رودیگر از امباپه و وینیسیوس دریبل نمیخوره ولی میزاره گولر بهش لایی بزنه.
⚽️
@Futball180TV
| بایرام حقگو</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103378" target="_blank">📅 18:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103377">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad153bb5d9.mp4?token=j1xagMPum2JE8D37HqOgA8glM2s62H0wYbOvQW11Dz1T2YBIZAF8j9cyhDOEWjBtBF9J5Is9C_rXxBOJlQghbBd9WrzELbKeHuJ74kD0g9suk0S6ACoCbVlIXGPnMSeKxWwzD1jX0Jh6CFra8E4lVWvEbxF_O1-dyIeOI42LcUDO4xwHXF0_rnpsmm4lSitFWdV-n7aJ5DRhoT2tp8jBY1sqLEOslSfrEJ2CHIVwiGguFaSxWpzwogIar__dUbpRDh-O95z8otWjMuIf9faAiL1oa4wsb4bIKTaREaE-eJlQ9tjiwznF4EYts1tXkYOFMEzQthLRX-yZTTwkdnBtfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad153bb5d9.mp4?token=j1xagMPum2JE8D37HqOgA8glM2s62H0wYbOvQW11Dz1T2YBIZAF8j9cyhDOEWjBtBF9J5Is9C_rXxBOJlQghbBd9WrzELbKeHuJ74kD0g9suk0S6ACoCbVlIXGPnMSeKxWwzD1jX0Jh6CFra8E4lVWvEbxF_O1-dyIeOI42LcUDO4xwHXF0_rnpsmm4lSitFWdV-n7aJ5DRhoT2tp8jBY1sqLEOslSfrEJ2CHIVwiGguFaSxWpzwogIar__dUbpRDh-O95z8otWjMuIf9faAiL1oa4wsb4bIKTaREaE-eJlQ9tjiwznF4EYts1tXkYOFMEzQthLRX-yZTTwkdnBtfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
محتواهای فاخر صداوسیما درباره فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103377" target="_blank">📅 18:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103376">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f850200c.mp4?token=iRPvE3oYAMt6CufrrLJtCUEIZETc2fKHVdYUKu3jnZ8ISZYJO_-QVHnLAs4Fgmrshs51wuvaLQnNZKc7VliLU2N6MyLlccDpQOWayAyDuofNpxkAKT76WprpVw0YTkz5sj42UOq613ISJLZhwoIkeJdowN8maWs5vikeY6sIahy0Z15YMuxPtZO6JsSJxoVbQBBkIokzsMAFp8jZs2LvRCoznfftPXyN9Qcw8JZQhJL3CmXeT-T4fssNXCnU5EdTjauP_e3moMRevBDXHItPMzgnzYRLOU1_bGhgVWxoJR1FbxtOSwRIGA1_qasq4L8jLt0MqxgMqeuud9-TR0j_ziq5yMzKpdiZOiW4dW8HYWkwBGVJdn60zEHD9nmdZ88JpNp-RUGNASMkPWbix5clsCczs7gREKy0tEABoUuoc-cvWXPFWsAYX2ASSkS8cX8g-SYpC9Ho4DmKMchX2vHcURvIKMO61QMLct_O5UpkIznRF0zqNIiwM1CvX8YMQdS-PO2sq1ynXEheJiZaNi0vFH05Cgyrclo6uzjndhHXxT1kWlM7eSI64P7csURydTk449GR2lobuY-zNNCbVHa-v7Q26OWHnWh4oV58TqJ41mcPNA1S1Wgy3BWlBWXGjpXr4P0soQJC3fMgOLxc5rMALhHgfQ9uM3xHoJrt1bOQWPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f850200c.mp4?token=iRPvE3oYAMt6CufrrLJtCUEIZETc2fKHVdYUKu3jnZ8ISZYJO_-QVHnLAs4Fgmrshs51wuvaLQnNZKc7VliLU2N6MyLlccDpQOWayAyDuofNpxkAKT76WprpVw0YTkz5sj42UOq613ISJLZhwoIkeJdowN8maWs5vikeY6sIahy0Z15YMuxPtZO6JsSJxoVbQBBkIokzsMAFp8jZs2LvRCoznfftPXyN9Qcw8JZQhJL3CmXeT-T4fssNXCnU5EdTjauP_e3moMRevBDXHItPMzgnzYRLOU1_bGhgVWxoJR1FbxtOSwRIGA1_qasq4L8jLt0MqxgMqeuud9-TR0j_ziq5yMzKpdiZOiW4dW8HYWkwBGVJdn60zEHD9nmdZ88JpNp-RUGNASMkPWbix5clsCczs7gREKy0tEABoUuoc-cvWXPFWsAYX2ASSkS8cX8g-SYpC9Ho4DmKMchX2vHcURvIKMO61QMLct_O5UpkIznRF0zqNIiwM1CvX8YMQdS-PO2sq1ynXEheJiZaNi0vFH05Cgyrclo6uzjndhHXxT1kWlM7eSI64P7csURydTk449GR2lobuY-zNNCbVHa-v7Q26OWHnWh4oV58TqJ41mcPNA1S1Wgy3BWlBWXGjpXr4P0soQJC3fMgOLxc5rMALhHgfQ9uM3xHoJrt1bOQWPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
مرتضی فنونی‌زاده رازی رو افشا کرد که امیر قلعه‌نویی در جلسه‌ای که با علی پروین برگزار و در تمرین پرسپولیس شرکت کرده بود، فقط یک امضا تا سرخپوش شدن فاصله داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103376" target="_blank">📅 17:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103373">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83944eb6b.mp4?token=TsTl3e1RZiUi0_mxyUUSBgVX-fdYWwdwF14lwXGR5EadxMDrlYItQeC7nmBE1nOOlsy6ZQeGOQSDdy-UIxToRny-U23wqsL_Ha6s7epMZ-XR0b_B5slz9QMFFm5AGtceQyj5_mQNs5AEdROrZ3uYbPaZgnKedeNZ7fnI8BqFii5xyB6yr3EfSbtrBvfX1kmevr2DXNsVsRFfrmTEUAXQ26TzRqJ3FCZvMEQsEukfY20NEhP7HmYHFdcLaFUdYYjp8NtUggVOaO0QgOcg7LKftrwQr-C0xdofitN4qn58BQUmtKsiVxnwlNy2kOATxurIuI97CbnKytNRQbbZiu1x_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83944eb6b.mp4?token=TsTl3e1RZiUi0_mxyUUSBgVX-fdYWwdwF14lwXGR5EadxMDrlYItQeC7nmBE1nOOlsy6ZQeGOQSDdy-UIxToRny-U23wqsL_Ha6s7epMZ-XR0b_B5slz9QMFFm5AGtceQyj5_mQNs5AEdROrZ3uYbPaZgnKedeNZ7fnI8BqFii5xyB6yr3EfSbtrBvfX1kmevr2DXNsVsRFfrmTEUAXQ26TzRqJ3FCZvMEQsEukfY20NEhP7HmYHFdcLaFUdYYjp8NtUggVOaO0QgOcg7LKftrwQr-C0xdofitN4qn58BQUmtKsiVxnwlNy2kOATxurIuI97CbnKytNRQbbZiu1x_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبر بسیار بباید پدر پیر فلک را
تا دگر‌ مادر گیتی چو تو فرزند بزاید...
نام و یاد استاد محمود فرشچیان گرامی‌باد
🖤
برشی از صحبت‌های استاد فرشچیان در دانشگاه هاروارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/103373" target="_blank">📅 17:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103372">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3dQfUlJHEex789HmABGXgmGMk7TSqTFmj7a2yGKzYqMt5Dl6_Jnl5Yv_kRaCifvM2_XvokOJ9ZG9aCW1_pLIAwkVnxjb-fDfx4NzB4VS_a-yMYcVlUYdOsST1i3e2u4tNDvdfNiA8GOquphXydRvqiSzwIGYHugLmuXCOXjUnfmlYRyLv0E8YKm1KSbaLuBjQzAAjzllPV9HVvMW_xB4SyNi-grAqkBkNhxtsqHzoMK64CQ5ngs2LhwBg2j9NAso39XhNei46I6C9biFnsUsuE_l0GjLD_zXzX3EKyPYabhFFU58lTZhyJB8_d0cpzHUrlz5VwpPfBAPCPQ2t2iOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
❌
بیانیه رسمی باشگاه بارسلونا: رونی بارداگجی رباط پاره کرد و به زودی جراحی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103372" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103371">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpq8MR-ZZntHQGFv8m9nMIyFGzzDf-Ozud3Gi2-qN9bwGwU39UTRtl2_i4VOI_D9saQzcanVJCOM4V8vSBzNrOnZEhcREtjAyB2gEMhbs9ZFg-_cPU3v5Qe5glg8tU1kczhZvLnbUcVLLwXLmH6vazU_cD_EK_YHeOcETcvJp57xC3CXutqLhyFtSN61BUiYwVerz2plu0fNkuuHg1Ud8gOqMN_kSB-vjGwzCtTt4-vHfKl1kzdFlUvOjuiozp4ZcGzocy2ScLYFzTtRu19czZva7dOGl4F0Ladtdy_FEC1e90Nzk0hF8vaVrRTm0p_-K0LyG-MWvP2lSxc-_VOOpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فنرباغچه همه استعدادای بگا رفته اروپا رو تو یه تیم جمع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103371" target="_blank">📅 17:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103370">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N56nUWWQMdCYsJ-oLmyRQBNMWi8f2U1VLA4GC2FXjXVyNsXuRlrNIXx_OnrxosC6YlJCZeQ27H60ZeVKtqvf9HE2tMq0K_uNgMB46ftIuQ3-qLf9zQjSWxPVaHNc0fCVl9YzAJxa3cbsxitfwcOjRk0xjJstrPEYAGplNAJJrnol8y2i8-AnMKbKssXt0yeSikGqlF3ePBC3cZ9mS_QCF8SZD3_RFfJOyHrst8KySf-GiyWMBfi7eHCsPulSXf8TE2KC6i0d5zemHq5gjZwNn7xgXujp1QvLZEKvQHR6avP13vXaep5D3zLkUkmDrnTsK2RF82_HtZvuRCDMB_PwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
لونین دروازه‌بان رئال مادرید بهمراه همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103370" target="_blank">📅 17:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103369">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fc92de2f.mp4?token=UolY6FxOkUG1ti7Yo1SNEdhzbIKrFxs5d8r5LmLQKCDmKO-a8z27mCdgp63tY0SgWzWrglyRsfd26b_wkZ5I8uQOCRrDFxoILm90w2Y6xfG25PfxsOo69aqBaB0wb4M72tqCkFkAFhjwQ0HLsaltOHCqcR3kInnI9t7L2a5K_42gMg9o2e808tHe7fA2JUWgwLODr5WWDQKzW-xeCZfB2nMf42OzPkdI-SW7yS3LmzgD-e-PnTGe4fS5v6mM6LME_ryhFcbNrHel9vDVLjoJwk0GR8s4miKNVfg_XqwqgYlNdJd5WSQ1a7lkKoit8404-xUpsIPc3XmWry5lxBQaip_d19rjU8iQOhDwkrmUACpSzHs3IyqXevAwyAgjOJ20YkXKIwXZPl5qi_jspie7zU6fmiK5Ln6s3qoX78WC_qm0CU92EYQXCu9x-vKkJSgZ-gVDKU_jDjOvy4PBI6dTp8sk4hnu9RMzeni8sQ11VJKsV6GolHe-W3g89A3HJsku6CYIiv2_-idxWmprnNhOMK8fU-Pt8IBlEWq6K24-jw59QTTUmHuMMgSxf9T8ZpG8dwGyqCMp0nP0m-9_6UOT5-glWq26mCARr1-F1JGeUzXm7cUFT5Hdv2dizRehpHg2WcjWHcoskRBL_5XEHdnQp_U0l4fis7mwWOEa35n3lO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fc92de2f.mp4?token=UolY6FxOkUG1ti7Yo1SNEdhzbIKrFxs5d8r5LmLQKCDmKO-a8z27mCdgp63tY0SgWzWrglyRsfd26b_wkZ5I8uQOCRrDFxoILm90w2Y6xfG25PfxsOo69aqBaB0wb4M72tqCkFkAFhjwQ0HLsaltOHCqcR3kInnI9t7L2a5K_42gMg9o2e808tHe7fA2JUWgwLODr5WWDQKzW-xeCZfB2nMf42OzPkdI-SW7yS3LmzgD-e-PnTGe4fS5v6mM6LME_ryhFcbNrHel9vDVLjoJwk0GR8s4miKNVfg_XqwqgYlNdJd5WSQ1a7lkKoit8404-xUpsIPc3XmWry5lxBQaip_d19rjU8iQOhDwkrmUACpSzHs3IyqXevAwyAgjOJ20YkXKIwXZPl5qi_jspie7zU6fmiK5Ln6s3qoX78WC_qm0CU92EYQXCu9x-vKkJSgZ-gVDKU_jDjOvy4PBI6dTp8sk4hnu9RMzeni8sQ11VJKsV6GolHe-W3g89A3HJsku6CYIiv2_-idxWmprnNhOMK8fU-Pt8IBlEWq6K24-jw59QTTUmHuMMgSxf9T8ZpG8dwGyqCMp0nP0m-9_6UOT5-glWq26mCARr1-F1JGeUzXm7cUFT5Hdv2dizRehpHg2WcjWHcoskRBL_5XEHdnQp_U0l4fis7mwWOEa35n3lO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
لوئیس سوارز ورژن ترسناک و جوان آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103369" target="_blank">📅 16:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103368">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1LqzIp8yQQk3lT68Hg7FFpLsiBivptoPdpbk-K5tyjcxzF9hrTawPCLjW3R_zXaC4WDXY2bLpQn6KYLbIjFFzY7MCQwO984w2JhY-PUpt6aXvSKEU-RVGEBSQuDUZbAQ32evFCrgmQLGRnF_XP9Cz8zZQiOKOSVfTrKGwVqfoCaxrVe9JVp6biONjSKquyUP0MFwbYvIXiFoX_PcxAklNHG0ZXUdvDcAjsbqJoLO5985LcipEM6O_Mc0-pydoNAyL2p-wt-uZnm_j8WbQp6pRQDjbLM4BiyCYnMSnZb6uHhuHdr62GXNieUD_m0_u7CLsAWyK6EUqO57x9h_LKSNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
رومانو؛ باشگاه بشیکتاش، پیشنهاد نهایی خود را به دوشان ولاهوویچ ارسال کرده است تا در ساعات آینده به توافق برسند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103368" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103367">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b011d4118.mp4?token=mc4uQxxZ5LUihh_88kEo9OKyb5q9sWhNtBSW0s36QdgroMU3pcgDY3Bz5amCTNR57lpBJt0IYq-9wi3KH10FGAfDY1LD5HSz0Ua_mM-ipC6QBrVPD6P73f9leHTuHUkm4A2ovMEqXxk3o0e1VdRYzGEWLeKVZ-NPRftZQFT0OcY-cBz10WhSU_Z6LFuhfd9i1EpB-5FFUJbp8sIwB_L3XbxDQ9P9BVglAkO-Bwz8r_CVmqY3UnWjysLpPNozhT4gSnNtE1AVZ-Qwf1S6bnJFXbfq00GeaEEEJJbBjXDBIDt6lQgBgaTqES-7ZViPvAuAOoO-bYnYiSGvowd4081mrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b011d4118.mp4?token=mc4uQxxZ5LUihh_88kEo9OKyb5q9sWhNtBSW0s36QdgroMU3pcgDY3Bz5amCTNR57lpBJt0IYq-9wi3KH10FGAfDY1LD5HSz0Ua_mM-ipC6QBrVPD6P73f9leHTuHUkm4A2ovMEqXxk3o0e1VdRYzGEWLeKVZ-NPRftZQFT0OcY-cBz10WhSU_Z6LFuhfd9i1EpB-5FFUJbp8sIwB_L3XbxDQ9P9BVglAkO-Bwz8r_CVmqY3UnWjysLpPNozhT4gSnNtE1AVZ-Qwf1S6bnJFXbfq00GeaEEEJJbBjXDBIDt6lQgBgaTqES-7ZViPvAuAOoO-bYnYiSGvowd4081mrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پشمام؛ روایت یه وکیل از جنجالی ترین پرونده خیانتی که داشته: زنی که از انگلیس پا میشه میاد ایران برای خیانت به شوهرش....
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103367" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103366">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8n3lG5Ig6FkRukI5ulva7XM2znIaXiYXihRo-VyeoO5BcuTlDFIFCAzNcOReY2332JKnqo1dtexgVykR00_bXReCYS2PazDdZD3azWPal14I9zriLEVf4qhOejLk4dKLU7BtUaWPf62xwwDRffFKb44OitsB9bJTKL3OiSN6aPhLRL1NHM1OpYcIMuuHQpiCbuGWk8OzNFUATaQbuuBuEUFv01NrujV1aMWvCGBxHbAuktvtfupBlW3iLI8vVOZFqho51pEr1FTUhl2sPgUmjGt8elyBRpt7ejz0synq_kaeQRX4RAE47eH031uL0dH9APDXgFGFcN9k3N1AxsZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
آلوارز در تمرینات اتلتیکو مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103366" target="_blank">📅 16:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103365">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzYwqtBEasj5oOLrFiGy8VZlqgiyGC0F5bEQunnO30Ao4mtdRBVEuDY0ihlJZN8SSPLjBDQAoSf5NO-HQrDPW-hIno8iUrLJ-t6Iyx4FYJjq8n1xLiqxXxyEEOGMPpww83GkXSEQx3GuD5vprGOZY8r7YffkbX5tGi2h2NBKdkte0_Nw-f3EEiPXA2UH6O0VFIA67bHqyDhUfD3s2eoXwPRhcewbbPBAOHJf0cIJ45k15pxljX3Xdf1BoR8GnX0LtzMHZTDhxB7Pf8V-Vd6_uboy6Onot7VwHbNJLm7XEbPJtPXJPrGtYkGoh6IE57Td0pGgNn-xIHGTmOlEF6ISKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
لیست نفرات رئال‌مادرید برای دیدار فردا مقابل دپورتیوو لاکرونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103365" target="_blank">📅 16:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103364">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2091ae4f3.mp4?token=dHBAiAxiwBXtzS0GXsd0MUNsxYtJa998oDSlypPQkx8LiEv0Pg2_slcY6o0t5Z0KfviqBr-FJrXyODoGGEJsStXDo-JNGwy4PTXlCfhRpUZekAzC3Y1pY7rVmD1aZLkk03JvPGp8BTEkX507L3CmL9HzZkFrtHzQqHD75GXcsbxgJSo9cvB5uHXnfYB-QXn3dUDL94To-Kc0FuJ4uKzS2oT37MKqbLjev2uriqg6GPQwrzZxap5lZLF7X863-LtratxdCFVCO-jtL87ynJkuDzFvdRzyBwT3RMBqH79uKHKq17RiS5-VLK01Ahr5zJIMep7vr8L_0waVE8ySf-dQLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2091ae4f3.mp4?token=dHBAiAxiwBXtzS0GXsd0MUNsxYtJa998oDSlypPQkx8LiEv0Pg2_slcY6o0t5Z0KfviqBr-FJrXyODoGGEJsStXDo-JNGwy4PTXlCfhRpUZekAzC3Y1pY7rVmD1aZLkk03JvPGp8BTEkX507L3CmL9HzZkFrtHzQqHD75GXcsbxgJSo9cvB5uHXnfYB-QXn3dUDL94To-Kc0FuJ4uKzS2oT37MKqbLjev2uriqg6GPQwrzZxap5lZLF7X863-LtratxdCFVCO-jtL87ynJkuDzFvdRzyBwT3RMBqH79uKHKq17RiS5-VLK01Ahr5zJIMep7vr8L_0waVE8ySf-dQLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
رفاقت ورزشکاران
💞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103364" target="_blank">📅 16:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103363">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5269SbXZlALRsP1ae4Z3XotWh8B0yzyTcMhklFqpagXcGNTALRrEd_oNif8aFNsUG8hSOwFmFFiqmjBDiVKXbOFBLEtJXzy9Fvz_bk2DJYJe7Li6ywVNlXZfRbYm0OGwvjewidCDaLX8RQCK8tM-u9wceTJ0daWqDK9emBNSwL1LGaiuWoMe6tdzQ1LNcbtNzrUlwieP-0pA5wV7xB30qvXkig3_QYVgbrj7-DY33Cg3JhLmP5f266bVC3YtER4HBKAorDJIP3OY7PNd5ZfR1l7nk16JGgmALh6tv168dASvX-2Cx7KGj5R5gb94QIkTkAy1EH5pnhQyc5amtjRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخترا: پسرا وفادار نیستن.
پسرا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103363" target="_blank">📅 15:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103362">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFpOVJGeqUzrMiauv70EY0zceCmlnCnvRZBM7Ea-aw_PupmWFdgPKRJVGJkf57c3mMwT2FfQ5ReuO_kj7xzth3LgDYMpXyuFBqjnf5LW561V8ZIPIAM0kKKi8T_80EHqRUfZgteTeY3lX1D_AvNM-DQDXG5BrXD2Ol05aCpIZAdafid0V3Bo2GW_6QbR2XWGvtI48XFoJUtSkfZ5xAxftuBQHZJPwdSonj81xipQft7uvatqTpgoq2g4R97c7GrCuwe9m-d9axqf7JiW28trCn9k0Qzrkp1gYiXZqIbfzBiuDUuq0Uey4sCoWZFFET8ePh7nCuWVe4VbqylDN1KloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✅
فابريزيو رومانو:
اینتری‌ها میخوان هر جور شده اسپنس رو به میلان ییارن. اون میخوان این انتقال رو با کمتر از 40 میلیون یورو نهایی کنن و مذاکرات بین دو باشگاه به زودی از سر گرفته خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103362" target="_blank">📅 15:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103361">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bea6d735e.mp4?token=AtgipyZsLLBvade8XUXh9uAnP_oDym_WJ58dnAGiBnpoLVzw0SiDBgL5HTYQ0G07OPOQjxNQEptqswzN-3s4J9RCXprJotwqarLhH5TUMNhISGgTiBwJciwJJ-ZXZvVNsK7ikuatfTBC82-AwEM7349I289IPQlBSAAQVodAFVK7r8tlEp3jjLqqXTUziCwWmA7e0y8dxP2Z6236Z5N8j1Y3EIqmOQaXrIxozw5qK894EyyHIdZckfFLv6beQmvLOS-ZCx7zOKlgcmbWp3aeo2NTGE8PdnseRY_WL7L01SBMbHSGuEHSTWSvs2zMY-Czzz321xvjQ2n0UvRjHNugszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bea6d735e.mp4?token=AtgipyZsLLBvade8XUXh9uAnP_oDym_WJ58dnAGiBnpoLVzw0SiDBgL5HTYQ0G07OPOQjxNQEptqswzN-3s4J9RCXprJotwqarLhH5TUMNhISGgTiBwJciwJJ-ZXZvVNsK7ikuatfTBC82-AwEM7349I289IPQlBSAAQVodAFVK7r8tlEp3jjLqqXTUziCwWmA7e0y8dxP2Z6236Z5N8j1Y3EIqmOQaXrIxozw5qK894EyyHIdZckfFLv6beQmvLOS-ZCx7zOKlgcmbWp3aeo2NTGE8PdnseRY_WL7L01SBMbHSGuEHSTWSvs2zMY-Czzz321xvjQ2n0UvRjHNugszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل و دستای پشت پرده فوتبال
😂
خنده بازار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103361" target="_blank">📅 15:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103360">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNOSUoqPoH9Ooy0mLNyGXJqQLZdGx_OqtpiDrSjkqyo2byvky8aeMWgl3iVdr8MADVeHSrPAOAGp6fw57YvcVg0AgtTh1St5iWUhxO9fWWvXzriLSt0GbEqAeMxZBfQs96BB9LXIxqT0w6PWcN70AuydmeEofJUyaQje0BoBtaaLyxsXMZJXivUbnM2P1GsXoikqxjETIQSjBBTBzmbhnQb4SYSwZ9AFngnmw9iyYUyrmHKIOi7RdUPpeKkWfOVLyFGJRXYWTJ_3IzVsrYUH_lAYNCzIHuioXugTG1rDCTH1PoDkMJXmRaxY4N6eWNTHUgE8LNjfi7ZvOm69sT5kDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو: فلیپس با قراردادی قرضی از منچستر سیتی به شفیلد یونایتد پیوست.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103360" target="_blank">📅 15:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103359">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyGg8sV_Oq4EQ-DT8RfVhZ4A4jGzMb5yESPChwSM7FfZA6BZWaqUnfVZarprrJp6wMYgGnP3Glw5RD8A5qB9kcz6XeJljYTXlLaOXPHn4bGkV-WT3LIFHBEE4hpwzf6N7W0nOrbvMO3e901IHBiebuv2YfHEcRdAi85redEpH1hlMz3iTXvip0MSTJUj91cPEMsv0zTeFaKHjCgRMZEVopPr0wU8z0DiI3ZPFHZlfE31wkHJZGOOwR0ntPrBch_CY-iT3pU09QLHkpOZleTlrXK85T2utHegkgJJxnQziNfo7jOwFLoVtSPjeg9HkoIomluPkaCaT937jQ_UN_GxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔹
خط دفاعی یوونتوس در فصل 2016/17 لیگ قهرمانان اروپا فقط 2 گل خورده بود تا اینکه در فینال به رئال مادرید رسید..
⚪️
اونا تو فینال 4 گل خوردن و جام رو تقدیم رونالدو کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103359" target="_blank">📅 15:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103358">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1146b9d2c3.mp4?token=ou8CwSpm05TVnyy3O73vuvTueJmDU9FOeYozkvVX_1KP-w2Omh3bQR6A20WhyoZNcGqONpAGMx3PUip_D9ZdQf7PjGNikey3-2eAJ_HJqTsrTa4YhZpMMabJ_vz4PwS5jOzA9npFHJAYHudaEMkgayg3s2kDM0wgWyQoC7kfxJirAsEwmMQJabFEzDjBa9Di2-vrfM9GJA-fvsR5mm4azzKfqR3g64AtNMXEgO-d4EV-NxBk3opBpiqOl6QmY0t_dnZPKSvDOK-C0F_M6AiTqaYsTxhW2zYrBOu3WFpcc2UEHwHXRcJwITHQeVnQbuAbenh7I4fFca_eLIf5DkR_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1146b9d2c3.mp4?token=ou8CwSpm05TVnyy3O73vuvTueJmDU9FOeYozkvVX_1KP-w2Omh3bQR6A20WhyoZNcGqONpAGMx3PUip_D9ZdQf7PjGNikey3-2eAJ_HJqTsrTa4YhZpMMabJ_vz4PwS5jOzA9npFHJAYHudaEMkgayg3s2kDM0wgWyQoC7kfxJirAsEwmMQJabFEzDjBa9Di2-vrfM9GJA-fvsR5mm4azzKfqR3g64AtNMXEgO-d4EV-NxBk3opBpiqOl6QmY0t_dnZPKSvDOK-C0F_M6AiTqaYsTxhW2zYrBOu3WFpcc2UEHwHXRcJwITHQeVnQbuAbenh7I4fFca_eLIf5DkR_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
تعریف و تمجید ستاره‌های سابق از لئو مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103358" target="_blank">📅 14:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103357">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4IJsALVNSCoDHm2mQ6gmmJPWge6byk8v5wAD9MJpO923cfX2pdW_O75Ip35ZfJw8FxSjQM_Z8MPG1pjXIFFPTytF5CFnj8lZDhzzVkucKz8r15O0lRWYVYMZsK6cxmVTt96-PEjzlWV2QUeazke2HFPGf_S-fWpEr4bPKN5P0uVIN8jFQt0s_lI2U2Vf0ZqxAd4JQEzj0q5HPKhzlVADuXB2IPDBFKQdiuV-fqfztuJZwMV8tarpuQPk3D1ommaS195gXOhMbcCkm_0aXmaOln847hjIp8xwRINLRZ_DGRq0Q9tJKEum7f43E4KsxjlhTORhquIjmvC3OTFbSr2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری از رومانو: دیگه مثل سابق قصد حضور فعال در اخبار نقل‌وانتقالات رو ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103357" target="_blank">📅 14:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103356">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/befb00f0c7.mp4?token=SYntFSyr_bows__st-cKR2XnMlJ2WLnSwkK7xx5aepkVtFGqGKR87pww6OjNP4w5rTc1AoiQwn1kbCP210YaanRHPoneHs5PZmBUDG93z3ugwikqhhYBqCt5fHM4e2I7YMTo6inRliqyG-J-YzfQaSfxeL0YYCjGVl3O2IBiS8P_6TCyjhFq4JilYFJEvuN6GMBH2H-NLFzxjRUhYz0pBdwJN_sBrWeW1L6r6I9Zf4edigEeNHoFYw68-5aClbLdHm1oBzpCvOPHnyU07GN6yeTL7rPkGOG_IBM58K_zs0uyRUH3d0dMi9wLrsaNnay6c89FEeT3ErngW3MOZiO9YTd3HhqyxwvDuOXxZRqqcBullNYrH2nvk-4korW_upEqTQsllPLn7pt5J3Y8D7mxENxw1J_0CIwvGakxy4zJm2n-NfQYBGI0-l6B3AxUGc4avTfEw1qSra8jSFc72SNCw5-NB4m0d-b6v7wPZR4quDhsFAidXPnzIuxbX-Njqdt96lkG40eWWQc73d38XAVjgKGcuUAq31wfxWdLPoPtuo34rM-5MgizHCIu0eVt2shu00Wc4cu5ZXn_whVxSXrUY61oo9e0C7CJXL4s2PMtK8JLcj3OxAanFWjFJCRO0I568jeff7BP_k4QhUa32S6iC3Qdz4JEjsW9FSAB6l729-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/befb00f0c7.mp4?token=SYntFSyr_bows__st-cKR2XnMlJ2WLnSwkK7xx5aepkVtFGqGKR87pww6OjNP4w5rTc1AoiQwn1kbCP210YaanRHPoneHs5PZmBUDG93z3ugwikqhhYBqCt5fHM4e2I7YMTo6inRliqyG-J-YzfQaSfxeL0YYCjGVl3O2IBiS8P_6TCyjhFq4JilYFJEvuN6GMBH2H-NLFzxjRUhYz0pBdwJN_sBrWeW1L6r6I9Zf4edigEeNHoFYw68-5aClbLdHm1oBzpCvOPHnyU07GN6yeTL7rPkGOG_IBM58K_zs0uyRUH3d0dMi9wLrsaNnay6c89FEeT3ErngW3MOZiO9YTd3HhqyxwvDuOXxZRqqcBullNYrH2nvk-4korW_upEqTQsllPLn7pt5J3Y8D7mxENxw1J_0CIwvGakxy4zJm2n-NfQYBGI0-l6B3AxUGc4avTfEw1qSra8jSFc72SNCw5-NB4m0d-b6v7wPZR4quDhsFAidXPnzIuxbX-Njqdt96lkG40eWWQc73d38XAVjgKGcuUAq31wfxWdLPoPtuo34rM-5MgizHCIu0eVt2shu00Wc4cu5ZXn_whVxSXrUY61oo9e0C7CJXL4s2PMtK8JLcj3OxAanFWjFJCRO0I568jeff7BP_k4QhUa32S6iC3Qdz4JEjsW9FSAB6l729-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
لحظه‌شماری بارسایی‌ها برای جذب رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103356" target="_blank">📅 14:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103355">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba0_AxcVu6FacogQauId2QLaISyOqNGiikxQ2nOR3Uje8IzmYZTBlkNwxYvG2yKbUx7yyKjHvCRvOgtoyxoRRUD5Hn3XiAJDiZRylv-uPu7RU7_eg44TpJVNIP_QkVLO_i1p7J5zGdeko6MWWkhHtjuG5iEevLe5STXEnbhaZvHJJfILHOygoU58NhkjccvJw18psGPnyGCirSmhr6X7yE71IxtHSM1vufJj15DKEVF7ztPHuTN4gQdkQSyJwXMJxtonG1QQ9bEyDoFx60QPDfrob6vCbDIXsSoVpf8BrznZl_HLTQnCimfbf-Vek5ezMRzllXtceD8vq-zGTNJf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
🔻
دو تیم ایتالیایی که برای آخرین بار قهرمان لیگ قهرمانان اروپا شده‌اند:
🔴
2007: میلان
🔵
2010: اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103355" target="_blank">📅 14:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103353">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری
از رومانو: دیگه مثل سابق قصد حضور فعال در اخبار نقل‌وانتقالات رو ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103353" target="_blank">📅 13:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103352">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri58jP4pQ_q_LhOTr489QmSg70LPl6orWJQ9Lrvg4t9u8O7vUMVjreyJEB8pVCvDp3d4m7CiyoZiQXHBDdfFwvTwnjeSemMB8MBigf4uy6RD-XRxZI_CvCEFq7dXKJVuy8NIhZ4GVnPBZ-xBau7zhkWg18hBA4ioUHmyxR-ksCGNtwXrGiJk7sAi-BSLlQnLvdHYkWnj-eTCnNY8FJs0g6Q5RAcsgekxXGe8olYiAs9Yw-HVeTHQId2ImlgqEVjsYZnK-v7YECIWHJvS8_8cYXg-Kx04DtdTz6sKwl4U7FG-bP7MAWcqfy4SQjPRSim-Sry6oHNqTAcG07t4DDMiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
😆
سال 2021 قبل از بازی منچستر یونایتد و لیورپول، لیورپولیا میدونستن که هوادارای یونایتد میخوان جلوی اتوبوس تیم رو که داشت به سمت اولدترافورد میرفت بگیرن و نذارن تیم به ورزشگاه برسه.
🔻
برای همین لیورپول یک اتوبوس خالی رو در مسیر هوادارای یونایتد فرستاد، در حالیکه بازیکنان و کادر فنی لیورپول به طور مخفیانه از یک مسیر دیگر به ورزشگاه رفتند.
🔻
نقشه‌شون دقیقاً همون‌طور که میخواستن پیش رفت و هوادارای یونایتد اتوبوس خالی رو متوقف کردن و حتی لاستیک‌هاش رو هم پنچر کردن، بدون اینکه اصلاً خبر داشته باشن اتوبوس واقعی لیورپول خیلی آروم و بی‌دردسر از یه مسیر دیگه به سمت اولدترافورد رفت. لیورپول تونست برای اولین بار بعد از هفت سال توی اولدترافورد یونایتد رو شکست بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103352" target="_blank">📅 13:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103351">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9708df2d85.mp4?token=EjI3sxxPFd8jJ5HqFvfYPpNPYtgHCzUqd8lQd7NxtCNvjFVzGt6WHLGRoZibyddrOuTT0s6u5N63UJwIKbiRKSRfLEDU8VYsgE5i91Oy3kXJMs23wL2XpdMPyCx2gd2ESKbFiU4Qxq7mxySenQ6lUj5qwqDgMuXTtzJEMYvtZhMJ7Abu37mE-echYYUPnaCpN1cfEh0eRYxagqCE0h4pPPzKgIWKEHKRkkNhBs2UG8Vh9ZXCTeRcwEgmT88imrBlCEbFedBECKWkHtw2PENGgBaGf4LfcGLkGJVv9_pwejncoin0GpvIlAL2fQ6LBczHt7uEZycj04EpvzQBwrjcEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9708df2d85.mp4?token=EjI3sxxPFd8jJ5HqFvfYPpNPYtgHCzUqd8lQd7NxtCNvjFVzGt6WHLGRoZibyddrOuTT0s6u5N63UJwIKbiRKSRfLEDU8VYsgE5i91Oy3kXJMs23wL2XpdMPyCx2gd2ESKbFiU4Qxq7mxySenQ6lUj5qwqDgMuXTtzJEMYvtZhMJ7Abu37mE-echYYUPnaCpN1cfEh0eRYxagqCE0h4pPPzKgIWKEHKRkkNhBs2UG8Vh9ZXCTeRcwEgmT88imrBlCEbFedBECKWkHtw2PENGgBaGf4LfcGLkGJVv9_pwejncoin0GpvIlAL2fQ6LBczHt7uEZycj04EpvzQBwrjcEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مقایسه مراسم معارفه در تبریز و ترکیه؛ فاصله جغرافیایی زیاد نیست اما فاصله سخت‌افزاری کیلومتر‌ها دیده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103351" target="_blank">📅 13:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103350">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFFPRaTjdMQbY5UkQTRPQ6fr36PQjyhdlQXGGsirPk16bR4GMp_XwX-NkM-acKiICzx5PkdqG3ZU7Mkni5hDjgftiLMiqe6jGXnTWXYPNBINsWa-KKjBftGeYhdeq7TpyIMQlbRZBCPrSEElbZczV8cWDoYuSmZeHCVp0qenAfxVmYbSev914bX8x60XdacTe7liTnR8TyG2HkP-BWSQvMM73xuEQMBmnmwxurKKRb7yfgJaDg5mvfXS10yphRC_SwBnYtbC7YyBeXSJkhTfsHl8-2zFne4pa0nC26EWCaeOl_onYruwY9ZuzlrUu7Zp0UptacBB5PYIUi7oYXim8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ ورود خولیان آلوارز با وکیلش به محل تمرینات اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103350" target="_blank">📅 13:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103349">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705d7fe27d.mp4?token=iz1qHBSpkys7MZLJ5haKRrlgv066cM-SpOXxVWLqPCa5WFpxoulxJ5QfT8BtLv-bKfIMJWkWuLTWpMRBm4HaIRivBHXH4kpbCTg4JN_0Eb8IR-DLBKRoynuzxKqiiV8pmMwVIplH9mE627YqxiyzcAeDf3MRoBN5XJCeHWeuaiTXlZqxePyQD7APQAKdp6UrBHZIC5iXAU6e2hvG_7IAlY-yqcdgElhG9n-_iuoXeKwXhE9RE3fzI1W8vDcO5KxWEFgCYBvN8-uhr6KZzEIc7zYJu-701reiBPPmrHuuVES8GNCX700FWH8WwooCz-VEjl7Im-zn3XktZEgzdK_-Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705d7fe27d.mp4?token=iz1qHBSpkys7MZLJ5haKRrlgv066cM-SpOXxVWLqPCa5WFpxoulxJ5QfT8BtLv-bKfIMJWkWuLTWpMRBm4HaIRivBHXH4kpbCTg4JN_0Eb8IR-DLBKRoynuzxKqiiV8pmMwVIplH9mE627YqxiyzcAeDf3MRoBN5XJCeHWeuaiTXlZqxePyQD7APQAKdp6UrBHZIC5iXAU6e2hvG_7IAlY-yqcdgElhG9n-_iuoXeKwXhE9RE3fzI1W8vDcO5KxWEFgCYBvN8-uhr6KZzEIc7zYJu-701reiBPPmrHuuVES8GNCX700FWH8WwooCz-VEjl7Im-zn3XktZEgzdK_-Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🚨
‼️
تاج: قلعه‌نویی اول با ما ۱۸ میلیارد تومان قرارداد بست بعد قراردادش به ۳۰ میلیارد تومان رسید. ۷۰ میلیارد هم برای جام جهانی به قلعه‌نویی پاداش پرداخت کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103349" target="_blank">📅 13:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103348">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🗞
رومانو؛ سوزوکی به پاری‌سن‌ژرمن   HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103348" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103347">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0zcoabj7j0QdRa_hpsoQoyuHY7fjryn6xOtP4jev-bncLFmacYKmbnvMHDpQQ8pmriUdPOWOwiIsZWE_h2GUG07clFTCcbC24IIGM90_eFDBzZcDyUXRVXIOn8ze5rF7ca5PlbGl-ryuwSYglLctSQnpKAlR96jn53WrwiEvwzFVJ3sUG6QWvxiiyji5riaBOErPofo20c8GqTKPWwtfuG-beznnGXuee2Iy1QK9HBvZ1XUf2HTZB-VxV6A25NMYgmLkY_bhFUfBRwLdoHVURRsqLMSUq31w6sV9OEgpEiuYhAyMAuvuVXBV8cHKtfu5-jPypdWmNWWc-b9Fa1yCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
✅
هاوکینز: باشگاه پاری‌سن‌ژرمن با مبلغ ۳۵ میلیون یورو موفق به جذب سوزوکی گلر تیم‌ملی ژاپن از باشگاه پارما شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103347" target="_blank">📅 12:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103346">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFQ3fZXNokVnpuL6qCWcjXwvz4PU5KXhPxlhY9ba4-NqmQ0IyTnQYLmwBqkVdNOXdz6E1GFI20uOxcvJH2GMJzZjIBmFbM5dWzd5JuS3oJwc0a_Po1hKqWRuoI9pFsw803tOTzt8a0Ab0Il_fOAKpen6FGBIMhX2lQZgmP5v86-aceQ-keAthSX72E7jVmnElZTadRBosEgmCWgoZMNfpfrhqwa12MZWXYlBVZIK9t_ocoRwWnGvnfHeTTG9ABoYZhLmjjhhccVgDFWkIX5j9Udy2BuQPqBJxcnBKnENPFHanqI53FA4ButU9BhXKENxMZSmiuTds8CjUiFjkYnraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
✅
هاوکینز: باشگاه پاری‌سن‌ژرمن با مبلغ ۳۵ میلیون یورو موفق به جذب سوزوکی گلر تیم‌ملی ژاپن از باشگاه پارما شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103346" target="_blank">📅 12:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103345">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از بن‌جیکوبز:
🔺
منچسترسیتی اگر بخواهد با انزو فرناندز قرارداد ببندد، باید رقمی بیش از ۱۳۰ میلیون یورو به چلسی پرداخت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103345" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103344">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9JChok4EHSjHpyMcfqgMqB_RD8CoRH3eJgWnuUsyCHZLNQ2nYKM756khCGEMod2ygdeIWyYt303Mh73oaLqzMMjm9LsZqeYpINacL7_1XZ5VdOLWgGynfyP5Mvrtbepdo8xg0a8PZFqAZOpisEmF0JCKfES7JUhLEdAn-iHf5PMOsDzUULABVZm_B_fUoJM0N6L75GiTX1piUKJkXFPA6cxCqFYoS8_C08po3Nc3R92LBUBmwValxXXX6g2oXfemFAwfCAr-aURVWSVjChq06b_xPhvM3TwrbBwDX7LeChbrNSXgeeeMKhAlUzZC8-ZzqZM5RNZ92-PUFQ7DgWPVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
استوری کنایه‌آمیز سیدحسین حسینی
که احتمالا مخاطبش رامین‌رضاییان هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103344" target="_blank">📅 12:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103342">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n3NqINWO1Dfmqvj8nImaqrrjBHpBdf9VdI6RRXH64H1_woy8KFQoxHQvW_ekyCum1HXjyMxAkazoOYRW8YD9vbBX9Y5WFPBAxHrjrfM_86GMt-Ilqt7QQvgBzyVidQ1cnrsYCGl_ghbQB5BiI0qzwMGqsxJLufF897TbkL-S8ygm8t-3SAClaI4LjFpIYBmQMTatjyK_nsjmZmdYUzsOUeHDwvNNd4wbg_FRGFiTLlElliGAiQGPkioniLMw6e3pvdvhq0zaj3NVu5Q6f9Vwe5MWosTKc-ZqfqLJRqH9lic39KOTfZYBHP9jXRqILEO3B-Uo7GgteWG5BUQsyOVTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRb7_bYoC2k59L-AcmfANtxQK-wFz5aqvoeXCXR0Y0KsLU_eVSFQ8NkZ26_r_ReLnZw1lAPc6bSwBUSzaLYRVLdD6pHZI1u31BH6VBUDcc4mYg2v9MH6q8cNgU31J2LAjgAvkw69tRIEd6JyHfjWRLyrTqStubGTJefPiUW7SG5lvVB-mQfew3NFGh4CfbgpMW_kRITCdL-Gy1ZiIdLH61wvM-gnTlU5bCGyCXpY6s9oY8kbMR48A0NEsJPJO912DGIjgB4ak0JpLLvAXES10A4BaKjY6rGvUJ1mNAEV-ZnjLKxfdUkXlBVuBrSZGKFIjn9NyMAEgEdE8RBL6W8-lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇫🇷
لیست پاری‌سن‌ژرمن برای دیدار سوپرکاپ اروپا فرداشب مقابل استون‌ویلا انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103342" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103341">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWF2B4DM5UcMCJ4f5U1o3bk5iI42o48qSV1-ekZ5G3EG0pw-LEfV-821302hvopqL6Gfiuv0BYyAjEiycCMgey6eUOboDg05QWyb_wRZh7mtmBNEc1WPZy9JNkEWkDU1uuRimA4Yn6Y3RUNPg9xWPn9HyNtt5enPoc72JJD7Q_azLDFN5qkrA40JTJ6dBAs5ls0u25C3OzsBuWcQ1yrgU5skhOioKo6rjtJIQAaPLoJ85ho7hLwIRD4xYVjAMyZmH-f_3c9GGncwmafagWyohht3Ol8eE9iqGGjzP6ONqRJvlX9TqQpHb2xStr9O2bqQrNSa8Oq2VaCYVFx_VTQ8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما اصن تیمو ببین..
بهترین بازیکنا رو تو هر پست داشتن ولی طرف اینقدر عقل نداشت که مسی رو هافبک بازی میداد. همه جوره این تیم تکمیل بود ولی فک کن قهرمانی لیگم حتی با درخشش فردی بازیکنا میگرفتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103341" target="_blank">📅 12:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103340">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVF8RmbPC04GR8w3TYfhsVSNPhdRnORkNZyU7B1tHDypnJHVtoeo9FU-8X5PAqK2E6kDMK_dTk1AblWdE4L6w_HbH1V_RmADubAMWjXg6FNDplypGjHR08pbMx1LWznsInkI0Cp3YK-oL-AvUlWF0TyOyG50WhB2WUsBD9xedVHv0cIQqi5jeMd8M2jek-ll-y1vTy69KaphSsF7K_70KBWm5k4veHbq_jdbiBnzOT9QZKVY_IStA8OzryB0tMQANTU-plJi9nVaQR7Ac_oamJ4ImPgYw8GTEa4YDLbZ8Y_oPZlHSZfe9cJxp3qrHp1o0FtT-GLQLmt4QmR88tDU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
روملو لوکاکو به فنرباغچه:
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103340" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103339">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHZAQQrVO2bxCkVxfdaSiTafobagav4B0i43PCR1ZH0J08LpPQyDtxVCZ59sEYIMA4svp9vttHxYAzVTj8k5UcSILoZ4MHn2Y5LX1sDretOvl_OgYHr8PtqURUAerS-LE1L2rhOoxXWwZCFVuz_q4OXSY4a_HftziTpsvHKFVC-NYWU5UVwOqg5eGoOK-fWGE6PvJHk65A2QLy_zWhfhxnCXrQ2L9F6whLqTPG9ErNsTGiCCukdRn4yACMwmYP1nUe6tB5y-07VZKG9On4Ph-nLc60_UHYHrWX-5xLpH1jmtnZPZthBZ64bcR6VkXZsn9ksp1vBp4Ky-YBGu6fdJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
مقایسه بازیکنان خط‌حمله وحشی بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103339" target="_blank">📅 12:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103338">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTzXJX0wJj7V7t2ZtCL1KMjlyuqr0NYqq7PAeSPPuVmhlht4gNTCb_5yNZjygqPlr5EwX2R-rCZ2UEMn0dVGo3_Hh2EwwiMjWFqssvvWzrcwCgUBqxu9hMlNgEWTwoOPSLnLQqKSjVNYBKiepQR1gjf8AqthKLK-AEnD9P2xSem-JBNP8wvhjmZFZI1QtfdgpitTdtj8i5PsE-9kuOfzWgv_NgxwOdg54YfJ3RpGRlXk9c2sOfI4GWRSra93B5l91EczBEjMJacRsn1NvZAbTqL5xSzE2wQJRtPH7Q6DHo5v8RlbgNVCwH1iRo1OxNOzEbakkOUP061YZINGnJik2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
پیراهن دوم و سکسی دورتمند برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103338" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103337">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmBXXbuTwfsjRC5Z2fsjVE1JpCAHDLtQJ3umVDNoOvtZjrEGhNp-K6JUiAG_t_9ilymGBwudbfH1vWuruQbNVRix2dhVZo6OXBF5yGjVPkbFt2RLDnx1gl50_el48_3wPMgN8nOpkTe4SdWlnsT1a3tpHcpLjXMLQDnn1nuwJ0kRlBnVn3-G4WYjrLDlsYWJH6d5OQT1f2mNUyd9XylKg43C-kOYOfSsBM0e0_dBz0CYITW0_aH7WQpd3wzyUiN0fjn2sqr-7bd8BxwdVOcNbf7e9wCJXAPOJVXYpUzRY7Z9HwgJcqbecSCrh_WL1FoIqVwMfqMYlcE63wwyozizPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری بامزه جواد کاظمیان
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103337" target="_blank">📅 11:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103336">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d8c12332.mp4?token=vplq5661cwP5gSBngVYDeY_A4i0-6y92Wc3IU_dO6mKsLWldMEGfW8dRjpfB0Eo0jitnjN-5-3iA-S8rKrY4h8loOWrqSVUfvr2JjYVH-MlzoXtSEdLmUHaigm_9eYJOPNa1xTvCsW9bwQl323IWpA1XsX5GsuzFz78Nth7HMDtsV1N7ejr64obGqreMmdgxeoofJ2Wa1Y36hmqx3Bq90XBx2ufKVBqnknvGjetuzfRm0tptlKTActOXb7oqFzr25F67wuRB9JhbgBwavJk0YrBFOArQ4T2nzEcAh5ht8LZGhSFMgmctjELoX2BW6Xsaidj7-7Vftyzi4YpkuazGOq_5Yob_QkIPo8TsOQ7WvxlrLD3TM5eMAHhEaVCYx4_rbpmfYjftwDOC_uJ2vFrdk1CJ8rzaaa9_LajgQzc6lkpFmLjf0wUDbzjNfzIl3KbvLb1B9C8nLWr1CJBahI_v7sWL-MGlcDKOtc8To16_InIGdZROCVdLj1AKMzpBB7vURyYf6Ym_kbHklEjcAXsw3H4ExR1R9jLKxY4THfRBp5FqZeiE7wsXmkSfYzEUyhwEYFYI-6sBQy-JmxmonioJzaWPKzrFg8A_B4on4pdOf-KTxiSU24UXKKftbChpnsD4KNr-TRwoC5PAGzkX4chGpKK9dJcBp_LFGRRlXaWETTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d8c12332.mp4?token=vplq5661cwP5gSBngVYDeY_A4i0-6y92Wc3IU_dO6mKsLWldMEGfW8dRjpfB0Eo0jitnjN-5-3iA-S8rKrY4h8loOWrqSVUfvr2JjYVH-MlzoXtSEdLmUHaigm_9eYJOPNa1xTvCsW9bwQl323IWpA1XsX5GsuzFz78Nth7HMDtsV1N7ejr64obGqreMmdgxeoofJ2Wa1Y36hmqx3Bq90XBx2ufKVBqnknvGjetuzfRm0tptlKTActOXb7oqFzr25F67wuRB9JhbgBwavJk0YrBFOArQ4T2nzEcAh5ht8LZGhSFMgmctjELoX2BW6Xsaidj7-7Vftyzi4YpkuazGOq_5Yob_QkIPo8TsOQ7WvxlrLD3TM5eMAHhEaVCYx4_rbpmfYjftwDOC_uJ2vFrdk1CJ8rzaaa9_LajgQzc6lkpFmLjf0wUDbzjNfzIl3KbvLb1B9C8nLWr1CJBahI_v7sWL-MGlcDKOtc8To16_InIGdZROCVdLj1AKMzpBB7vURyYf6Ym_kbHklEjcAXsw3H4ExR1R9jLKxY4THfRBp5FqZeiE7wsXmkSfYzEUyhwEYFYI-6sBQy-JmxmonioJzaWPKzrFg8A_B4on4pdOf-KTxiSU24UXKKftbChpnsD4KNr-TRwoC5PAGzkX4chGpKK9dJcBp_LFGRRlXaWETTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
برخی از جذاب‌ترین گل‌های آردا گولر ترکیه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103336" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103335">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
از اسپورت: سه باشگاه آرسنال، بایرن‌مونیخ و پاری‌سن‌ژرمن به جذب ژول‌کونده علاقه‌مند هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103335" target="_blank">📅 11:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103334">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dfe7c98c.mp4?token=Qkw7ghuN4q3KeL9vDDE6lEP_5rMbFpb0SQiOYLNxN-ckphXk1zc95ijwbqeAQQ9yGKxm9fjXqh_HUydsajBR4xMj-kEy8HwV2eqPYTmwegKkS967DcRiyZS5PePgJNo9ikEGjyDlxiRprrj2AaVdyG3F3Y5nYuY3lvmN0E5CuFn5bMuiLfKmaSXonqSrdd9dwjRkinAprPcv2BjjFvPsyw3yHlSk9JAwpndJLUkmV4gzrivOJ2oXt-tvF877O6ZxhshojKbiGWzkvuhKzHzchkyQZ64AhmyhSsd3koz9S5SI9HfdOonoZiYk_crsZgQUEv8x5m7CAcNploGvV0INKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dfe7c98c.mp4?token=Qkw7ghuN4q3KeL9vDDE6lEP_5rMbFpb0SQiOYLNxN-ckphXk1zc95ijwbqeAQQ9yGKxm9fjXqh_HUydsajBR4xMj-kEy8HwV2eqPYTmwegKkS967DcRiyZS5PePgJNo9ikEGjyDlxiRprrj2AaVdyG3F3Y5nYuY3lvmN0E5CuFn5bMuiLfKmaSXonqSrdd9dwjRkinAprPcv2BjjFvPsyw3yHlSk9JAwpndJLUkmV4gzrivOJ2oXt-tvF877O6ZxhshojKbiGWzkvuhKzHzchkyQZ64AhmyhSsd3koz9S5SI9HfdOonoZiYk_crsZgQUEv8x5m7CAcNploGvV0INKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ترشتگن در اولین بازی خودش برای آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103334" target="_blank">📅 11:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103333">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3329c503a4.mp4?token=rI55L0BpZ_oC6WHHRQZZMi5xrXVynK3noDnTvSjLSJ_bWzw1F3x4NpEkDZ77YOnId3ks30f3_LCXL70hdlNyaknfPwVOxVjBuOGXXlQbRGXE0rGK6mP62j3dBoPXVmb7Y3wCW0WY_BF92RpK5Lb_ZLCm4aP4sA67f2hXD0EX1ZDN2IBNysPMyrlemQj_h9hh1l18YxF3AzcU1MiggEMKcne6kr9_cVk0OWcyF1y_orlUfh0-8zFXb-FPzYj3ZTk-fIEDEiVmrPzwHx4cId1j_yO9mxK8UL7aVJeKpH67JMoGh_YNSZFBs0ZRJCvzyXXIGkp_WzlXQrwPYTyi2G0Muw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3329c503a4.mp4?token=rI55L0BpZ_oC6WHHRQZZMi5xrXVynK3noDnTvSjLSJ_bWzw1F3x4NpEkDZ77YOnId3ks30f3_LCXL70hdlNyaknfPwVOxVjBuOGXXlQbRGXE0rGK6mP62j3dBoPXVmb7Y3wCW0WY_BF92RpK5Lb_ZLCm4aP4sA67f2hXD0EX1ZDN2IBNysPMyrlemQj_h9hh1l18YxF3AzcU1MiggEMKcne6kr9_cVk0OWcyF1y_orlUfh0-8zFXb-FPzYj3ZTk-fIEDEiVmrPzwHx4cId1j_yO9mxK8UL7aVJeKpH67JMoGh_YNSZFBs0ZRJCvzyXXIGkp_WzlXQrwPYTyi2G0Muw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
لحظه انفجار در جایگاه CNG یکی از نقاط استان کرمانشاه که با کشته‌شدن یک نفر و زخمی شدن ۳ نفر همراه بوده!
❌
دیدن ویدیو مناسب برای همه افراد نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103333" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103332">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cdc7b28e6.mp4?token=QT-zNs1-3BkNt6maNAAki5je3nHKYJCh83G8HhnIHLctdmuZEtul6MomUIVNrZ4hE-_aiByzuoGK_BIpCFfRXqD_q9RPb0ki1q1SNyO6J4Utym8GCxgpY0VwKVFFt9VHei-YbLWarWYaofAM0FAl7eqNPYL8VN1qKf0XpNXXOS47VdgWJ85I88r8bD2zQY2A3OUF7boKZIAZ0cSW3rsB6lFet63QvNug_xFfX623sfZxwBwzsdjJ9pNcyGprwDMs8HL2tojvWUzT-ws3cPxwKBUcUNNYoUImjJ7UZGpcCpKOcHszf3RsH12KfRvx7Z4rWi2h6G9Tqppq98jtJ0MQww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cdc7b28e6.mp4?token=QT-zNs1-3BkNt6maNAAki5je3nHKYJCh83G8HhnIHLctdmuZEtul6MomUIVNrZ4hE-_aiByzuoGK_BIpCFfRXqD_q9RPb0ki1q1SNyO6J4Utym8GCxgpY0VwKVFFt9VHei-YbLWarWYaofAM0FAl7eqNPYL8VN1qKf0XpNXXOS47VdgWJ85I88r8bD2zQY2A3OUF7boKZIAZ0cSW3rsB6lFet63QvNug_xFfX623sfZxwBwzsdjJ9pNcyGprwDMs8HL2tojvWUzT-ws3cPxwKBUcUNNYoUImjJ7UZGpcCpKOcHszf3RsH12KfRvx7Z4rWi2h6G9Tqppq98jtJ0MQww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
❌
تصاویری از صحنهٔ گروگان‌گیری دقایقی پیش در خیابان ولیعصر تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103332" target="_blank">📅 10:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103331">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3e540db5.mp4?token=djozgmL92AAZLGrdZa01droZhk-wKrjgUM2M94Q1rN9I_LJ3CXZ43anAOu4pLYsSHUUOmbOKw0jCu1lB72uzsgvq5EdiGHdyDtxr_owbq8qCOpHrkT21S9mrEV0M1eOdPgZJ4NSafbptSOrxUcYocF_5NkuTSsLmkFRP4zQBzOLR6dHVd10M3KR-KDt63Lb-gP41fT5FAUSigNuDdQZLxKlmHun7PLCMj_SNNvNxjh8uszdcejlOFPji8eLKbMbc9L86YgJB7hg48DlOMoCf1fC7BwB6wZ6CafGf6Q9su1z09JdAqb1Z5JvZFO-gO_05LbotXsYm_QYhsYqbT9pomA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3e540db5.mp4?token=djozgmL92AAZLGrdZa01droZhk-wKrjgUM2M94Q1rN9I_LJ3CXZ43anAOu4pLYsSHUUOmbOKw0jCu1lB72uzsgvq5EdiGHdyDtxr_owbq8qCOpHrkT21S9mrEV0M1eOdPgZJ4NSafbptSOrxUcYocF_5NkuTSsLmkFRP4zQBzOLR6dHVd10M3KR-KDt63Lb-gP41fT5FAUSigNuDdQZLxKlmHun7PLCMj_SNNvNxjh8uszdcejlOFPji8eLKbMbc9L86YgJB7hg48DlOMoCf1fC7BwB6wZ6CafGf6Q9su1z09JdAqb1Z5JvZFO-gO_05LbotXsYm_QYhsYqbT9pomA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
چرا همسرت همیشه صورتشو میپوشونه؟
🎙
عثمان دمبله: همسر من یک زن بسیار مذهبیه، پوشوندن صورت تو اسلام اجباری نیست، اما اون واقعا بهش پایبنده گاهی بهش میگم که حداقل صورتتو تو جمع نشون بده، اما اون همیشه به من میگه: عثمان من میخوام فقط تو صورت من رو ببینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103331" target="_blank">📅 10:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103330">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0mNEZjvWq-9JlcwSMhgPX92YLhWbHmllH5mXl9QTpYx_DvfrITl61KIBiNtZ7IfAYQ6h6LUT3f792mfDC-iq6e9VD0kunYP10ji3fdD4E2dR9cAbDeJW0kSn9V2kPUftBOWD_Z6Q12v988MTflTHbXEbWQ6idBmEH58O2LASRimtCEEtiFBrDrS3J8E1C2ptnMOTEEzKPDUWqoktJLJJen5MQmwYRPKgDkpx7zaqB1bGjIrSUxa8UdO0gbU7fz4M93HHYssDCgihRLau8saxEjQS8kHAknUAsauXDxedmUkO9rigyQLBXVIHWHZVwksk8F7UcUFgQxPOUJCQtjT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
کوپه: ولاهوویچ می‌خواد به بارسلونا بیاد اما دکو و فلیک اعتقادی به او ندارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103330" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103329">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103329" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103329" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103328">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHIX9D8cwhup5VmBCau_6wKiuEQRK0XSvOC-bk0B6SsxyRjTwpFfsCnNkmiQiI9L76WjOqq9QhuCFBYh2jWZh77a1lSJEnFtrS72t-lK1dSpmch7BW_by6shf5BsZ_7AyAhN55n9UllRq5n0rrEWCBmg4NTLcU-1fPJ7EzKKPK9nm5y5CTqr45XbGYMxeoxMYszgjspmj9EZoTGK6J2KjkhVUo7ctwIUy5cbLux1IQAMeDy1-slXkTpPUGtu1LDGZdmfjCBzbmvx89kXhW6o5JClXwaoAdBWiqkhTOGO0DCqwa-Isj7yGUuqm14AJ1sEwqFwekCyP-roFPmjqjkvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
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
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103328" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103327">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYysDf40T64QIxtFonXO93nlIUWdQby0ncOxTm933OinuYmaAgRxIomXcMssUiu1d949HvDdo5o30PiGV_0qHh1mPHE5ELcxFEO9OZP8cz4r0fUpeCBiu5XOqFrhfXLANZxOTwIrRA8-yNqeLxvlIdsNMhqXpZJWpUgVjnFaLbnB2YkVfUt8C_GHx9KaldadB4_IbZG0_2mKeT7_yzn_zvVQEtWdZeAbxX-uMZVwLHKK4R8msHOQqLbD7_Fmix3uxr_-rSeua5Uuqfd03mNlfMv-7pgALdUqFuCRo_RVhR8059e-5wSQX_g0P9Ry8Un56OpJJ1ZXrneW8_RxsIPkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔺
دیاریو اسپورت:
بارسلونا اقدام برای جذب لائوتارو مارتینز رو تکذیب کرده و گفته در حال حاضر لائوتارو گزینه جایگزین خولیان آلوارز نیست و باشگاه اصلا روی جذب او کار نمیکنه و گزینه‌های دیگری مدنظر هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103327" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103326">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54347f49a9.mp4?token=Foa8ymJsMqKG_Qyhsy7zrP8-pfA-O9mOELSboDs32p3antx6gJPHIbDEZm2_Cky6WkOWlX7BcAkaVQE7xBLc1zwq0U3aKoHLTWeM4C6eN6hI_aZv2L95JyzveP_yzK02GKdFVyE7oEVx7E9hT78YHCWsUAlSiPMaIyO89SpoOkAEyo0Lzyscc3PlMPefIGhwxP3RDXE03lFoy4skaLip6TW783Aarry9OWHrMh91kwzckg4UUunU8YUvwXFjncDUSz2hV-5dkh1QreIKLs4Ak96gX34K9ra1uXA_Nm7cC36Hwd9kdk_obOkUE6tUmje-apHMyq3zaOkQEHCPq2KZZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54347f49a9.mp4?token=Foa8ymJsMqKG_Qyhsy7zrP8-pfA-O9mOELSboDs32p3antx6gJPHIbDEZm2_Cky6WkOWlX7BcAkaVQE7xBLc1zwq0U3aKoHLTWeM4C6eN6hI_aZv2L95JyzveP_yzK02GKdFVyE7oEVx7E9hT78YHCWsUAlSiPMaIyO89SpoOkAEyo0Lzyscc3PlMPefIGhwxP3RDXE03lFoy4skaLip6TW783Aarry9OWHrMh91kwzckg4UUunU8YUvwXFjncDUSz2hV-5dkh1QreIKLs4Ak96gX34K9ra1uXA_Nm7cC36Hwd9kdk_obOkUE6tUmje-apHMyq3zaOkQEHCPq2KZZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
😐
سقوط آزاد جرارد پیکه تو مراسم فوتبالی که دیشب دعوت شده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103326" target="_blank">📅 09:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103325">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3Jw4Et1EnC-a-FLbhC4mMepw8cRHYfTwH-Y84RO7glJPK8Ha2rHFWH55a2PQFDfro_Detv84lsM7C8GGJqOwA0uIv7w15nzYU0rXIMrw9R5Eox2VfhqaL1oAzx4nFdYIOn3xA2oHFfxGgCgpmYEyyjj9OzYOfR7NsSUzRUPlL2Fu4eRqRDxQadRBD1jHBKS1DuPgCTHkbWHeKxg3-jUokbGUUDzmAlkxdTdrgTQv6QhBFZgmNI-J0-Af0IRzHOlnFdEE9afh6H6E28xx6PNvl8tEW3OTDSC_lPxpgy3g4Kh5opPWRzsSQwfCBmlGi7xTyKTkaDclWX2clYhiS95SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
در ژانویه ۲۰۲۵، بالای لوگوی پاری‌سن‌ژرمن هیچ ستاره‌ای نبود... اما حالا دو ستاره روی لوگوی باشگاه دیده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103325" target="_blank">📅 09:19 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
