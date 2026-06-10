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
<img src="https://cdn4.telesco.pe/file/S7F72QmCcMignJQwYJ957PtKh_B6xkSLNPTi-Xtw1sxwipbJDiawWGBOtKlnalxhjy-WbOgjouz1wX326XOknVklEk58MQA0CmmYz7XVfM0Hs3OSV3gk458Bh5olzdiwb3p71Hp61iwJxufpbM_gJ6e33-Bvh37hOawS4kcFRmajkPWRKjsRqDcZn7MmBE8dAIr-XyKm5YvKIjJUilx4UWrk3uYVPGFr546HVnd7n_yfuXi3VVxckwL-a53UqftUG_so_VqP0ZQN5EtLjLDMkLfjFPqT0t9K2dtrZknaC9qqlEBVSOyWvj4SJ_0pL2ic7bj0_VgFSKSB8Jz48wskqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 196K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 03:23:56</div>
<hr>

<div class="tg-post" id="msg-23159">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=TqB2oHR9AS-QUJproJsVwDB0r37pmCSQdGs9nLXm3HLo8zRGbAtgLyOQpd_SOO0IMLjW1d-a_-Uaki5fDi7W8qPsmPYcp2DD1BJQz67gm202qe80u0vaZGErRLtJouGTQiDGLUwR2Fz81u9zttfcZdheN_vnBu_YpWsyCyTY-Dw86Kal8fc3TAnhKWfwuQekr33EuCx4Fv8MIxI4B2Pbt4GeL6VHNE6aOpBFqAogtK_1Oi20f21TFtrtlO1G96VNEI293vELSUSpRv5y231LCUTWnCwtbAHuyVIKI5XvLyXqRYVGLt-9753CRtamz64q62MczQnjtwvUkVI1xfQJJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=TqB2oHR9AS-QUJproJsVwDB0r37pmCSQdGs9nLXm3HLo8zRGbAtgLyOQpd_SOO0IMLjW1d-a_-Uaki5fDi7W8qPsmPYcp2DD1BJQz67gm202qe80u0vaZGErRLtJouGTQiDGLUwR2Fz81u9zttfcZdheN_vnBu_YpWsyCyTY-Dw86Kal8fc3TAnhKWfwuQekr33EuCx4Fv8MIxI4B2Pbt4GeL6VHNE6aOpBFqAogtK_1Oi20f21TFtrtlO1G96VNEI293vELSUSpRv5y231LCUTWnCwtbAHuyVIKI5XvLyXqRYVGLt-9753CRtamz64q62MczQnjtwvUkVI1xfQJJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏐
برنامه کامل مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/persiana_Soccer/23159" target="_blank">📅 03:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23157">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1uhPTxIJPwTNXSTjWNLKv7M8XAcNKxMAzWwByMBmoXLq1uEqKC0s4i6AWodHNNfbhAYdyMRAAbUm3UHfUOLTHy7THvcIKJ6-tvgFr9kcvtIX_MGxlSNYRXVFnPdHg0exH7zwYRWT92RExvXRmjKDPswIdCXjCqknnLZ38zgvrjnhku8ksQeFuFJzIogixGSs12fnQLaFyD9ydwZ4bgjlEibdp_e7KPq4kFgNFJzvPYnMkfVx-oHyAIq1boqs9xli9lxBGW7WE7YI5psGRx5PKApkPpCfbyyWYv2tnfG18mTQ00XVtqyaBUvtBXIeUIkx_a7X6iSs67ij1cqS_K1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/23157" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23156">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgu-0i0HwcHnShBGk8o0SgOSl-kzkdDDhQkhVErQqObqVPPQiqvqs9ROzX7IzTUPxPbJVEi9rwEVeHqlaaUS5UEMtpYMj4G0zL9n9JT0SCCHNIP4zHeSf4RvskpscCczACYdoLn-UQTDtNWeCpgEKsDDcs5PvrrDYEodEZAu0r2HGn_HI_NTs1PAl8CYCcIkSUcQ8EI1z6goQ3wXw-kZ9qkOSwPdMeX6AOfkHtgwCaRHE3rmmUyOhMCy8dwD6JKiKumxjHB2t3CBpJyWTfL9rcruB8HF5jraoN8uMIiEfhj3mydMq6RYxsRVDVi94NxK6uhsuVjP_mqoRL0eeZgYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
برتری‌آرژانتین‌وپرتغال برابر ایسلند و نیجریه‌پیش‌ازشروع‌جام‌؛ انگلیس هم تاپایان نیمه اول با تک گل رایس از کاستاریکا پیش افتاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/23156" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23155">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3oHlPFNU0jhyoyxFY_Lb1V1gHpWiApA-0-bx_8XPCOjauQE49-ZvOE46rag6dHHIJwdeSYUiPuV5Isr4F-1ghrukMByxZynNxVl5_o82_RiKwfpF3v2s7pMsgUQG9eEVbuju-BeGYZa1f9MYcs5YYc27PskuPjS12NFPgOhCeRLaeDZ-z1Cazl6IvFVhCpJ676S6qyVt89gpccsp98FT2apqtFQr8W0WCGtIbb3JniHxBRc0zBh53IL8umcNCNhOW59ws9yqcjqTjojSZS2W7_k7x7Nqy7_zJlhYKwyCOB9U6xsNCgG_nIv6rfghWp9dpoSyZwckSErE8SAh65g1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
— سنتکام آغاز حملات علیه ایران را که از ۲۰ دقیقه پیش آغاز شده است، اعلام کرد.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/23155" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23154">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">▶️
هایلایتی‌ جدید و کامل از عملکرد نظمی‌ گریپشی فوق ستاره تیم‌ملی آلبانی که مدنظر سه باشگاه بزرگ پرسپولیس، استقلال و تراکتور قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/23154" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23153">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA9DAZidRSVSz4vYGL0qUWwVoQ7nD7G5ysmn7T6_rpGN2zlpmvqcIES8-fWUjKUC3Yfg1dfmturOp1uDn5Z6e0FUPax_E8BVJ4TXxoBM6FHudPlKlopbcDCzpOApMl9W6FjcWbv__xk6g7CCbFYDKP_UP9Y6XVDyiftvcKSldM9jno3UNF8vUPWXwx22mjwD7wRbTSojh4I5sDPHl3xi5HTOm1kUYX8ZxPvxtMu46u6Fy4a8ZJpzbHXRoLg7hv2np_xSJa4OqxQFLXRyBPPC0sy-pTubTQSTdmkDnpiH3knimHvLyeYn0AweKFbxOEz5NjEjFrkTtAzJw0asDrX1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/23153" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23152">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=BKnePIhP09urgLKuRajBepnoXmSPLpELWnz5FUT3hbK9EKGLr61VJXjanDKH-nsI4MesHvin8hFa183JUEVTTgpYJSHjMpGIzR3I1XyafNlc8VrHmtYSacmd_ID6W_8uFciH4BRdDzfM66LEl2F2fgAL5LBYGNS96XuAwWlzILl12zhHr8PD2ADE90WkM-fa4D4ntVBkiREEoksWbZDhKIwhwDwFcAkwHenHuYrw-y2gtJUhzR-IBqeyMnRiYpq923kwG46yPEzWP0kE8hSqqT3cQdPSuZyAibOuTtsfiJziZ_0lM-BF-BLdlODzR83L75TeoChmWApucOoMdGFqLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=BKnePIhP09urgLKuRajBepnoXmSPLpELWnz5FUT3hbK9EKGLr61VJXjanDKH-nsI4MesHvin8hFa183JUEVTTgpYJSHjMpGIzR3I1XyafNlc8VrHmtYSacmd_ID6W_8uFciH4BRdDzfM66LEl2F2fgAL5LBYGNS96XuAwWlzILl12zhHr8PD2ADE90WkM-fa4D4ntVBkiREEoksWbZDhKIwhwDwFcAkwHenHuYrw-y2gtJUhzR-IBqeyMnRiYpq923kwG46yPEzWP0kE8hSqqT3cQdPSuZyAibOuTtsfiJziZ_0lM-BF-BLdlODzR83L75TeoChmWApucOoMdGFqLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/23152" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23151">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz5JBdWJyWuLMeeuf643CLVSy7QJW2fsK4mm232zAKkWL_R0Y3NAryeOs68dyQZ0sfQ4YffXJdm29jBalwZhjKM63VW1UJ7Tc2umSkOmaDdjIOqw3NzOSMEB5na4Vs8cLipT0FGFQJFhAhbxrWgGi-qCh0sZJIcbHzKTzMtoxMzt4eyV0aadc9GXrktlVPsu8XDr4SzyGDi0UoiQnfBwlXb8JNadjMf1b6wtyT9DK3zgrLBwHElpwwskhXCpMa57TwzkJstQQi90vRiy_jzD6DdzWoFQ_odV-raG0ea5h3wwlKgqBhX2LgOtzlYH7AcxvhHwE4-bp0TVtNuIsLiD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea20
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/23151" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23150">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqve1OxPPhOtaXLZpqDckT92I-zgnAwIsFv2jVBWE7BF-tc1tLGq_T4mgEzww50UCtXpuCvKKCH2mr1p8VPyfRwbcMDIeTJ9EajI-2Ywl2nBBih7tlX0Bin-EMeS-YYSgeFT35xyebSBRt32qsecmIo9FXYEYWZlVXC5l3gGNSRQufF3pQFTpEteA7Mq1wisLkiTsjhZ3mJFULetrfXMOUQzvPvPbL8p9aglchXbZ0JPHmR0OrKQUQ1HcG0XhDeEBPx1uxgx8A_SbdhkQeX-HvJAWIPPTqp_J0fQrWKbfzDmVi9WXCs1twNPBpugjnIF_5dGqKkUfgvlvxgiUbcczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/23150" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23148">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxsxLPmbpPWlPAL-xJPVwqSnzhcc2FWfUX2iywuUcTLPCCtkwZpoRoE62QJi9dVe9KpmfUPgvAON4--Zv1gcV5HHG-FlLOxBBxFocqwib5bji0d1tPHWSFT-9hr8uJotZK_vZCDstlvMZTfjkO1R4mB2mpEetpzCI6dac8WWfWTCDHL-QUFvrxqJJi0CsHsUVwaSGwlOABoEuNuj5PQX1ljqOoFsJNWnqRfswsel7eqdgxYhMkYuIgxTIro6jDAnA4IKuoykCjyyW7hloiVN-NgDfYow0c8Z5N_OpHH2GfKvTBWIUTUHOS1RPovBZZU4I7VxjH_hhasD70vWdX3nPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/23148" target="_blank">📅 00:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23147">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=KN11WJhmwU1pbwPqVhSKtTvTj_jaO1Nd-D-zzsSSzg9fHX1rIAkPoUmn5i6zcT5NNhynQTkegypoOMm7RQsBIYjKeJRc6qPUxfFi2_qLpP-r95pu4H5q_ktONRrpQg7J7fWVDLqlPI02RlcWlw2-HRP2zg5DxhpTnARo9VjVncQH-VSD5Jvs3gk6b2s5CJHTrzRC4jpXU0r8jXGff5ErjFMQdD-5K0IhihON3cFNyDiCVduRFMP64xTcg6-_pf0hICz76zW9hEdYfvMxW3Ue2kpgUUVk3yg80gM4dqwcG9wBBYK-NcKHaQQ4aldaGdIQlYrOuzUyIepqUFKE-nZz7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=KN11WJhmwU1pbwPqVhSKtTvTj_jaO1Nd-D-zzsSSzg9fHX1rIAkPoUmn5i6zcT5NNhynQTkegypoOMm7RQsBIYjKeJRc6qPUxfFi2_qLpP-r95pu4H5q_ktONRrpQg7J7fWVDLqlPI02RlcWlw2-HRP2zg5DxhpTnARo9VjVncQH-VSD5Jvs3gk6b2s5CJHTrzRC4jpXU0r8jXGff5ErjFMQdD-5K0IhihON3cFNyDiCVduRFMP64xTcg6-_pf0hICz76zW9hEdYfvMxW3Ue2kpgUUVk3yg80gM4dqwcG9wBBYK-NcKHaQQ4aldaGdIQlYrOuzUyIepqUFKE-nZz7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
از پیت‌هگست وزیرجنگ‌آمریکا:
سنتکام امشب درگیره چون پرزیدنت ترامپ گفت ما امشب ایران را بسختی خواهیم زد و این کار را می‌کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/23147" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23146">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDGNjWOmDlIlRLpFG4bYaBtWODNtajbhPY8Dy3Ul9Os9NboJbRs4u09c4BoiSuo8gaUeTX2kPEpGEvUs5Zb27FM_IxxI0J_70PjIQQZ1x6ARqTNdZ5t7-NQhIWRce6NCoBszhHroOdcNymNxcJ370MQWhJvjdyoYWdYwMOo5GhpccQMKk6o9-Fydo4LFqwQ46l0ZGj7qG-ROY42E6sUaC2vqxfozfw0xpAcKitU_3apIBUgcnqak7qaqzPNmT4Vd3ttShMZbAho7ifthiMjVgXOkq7A15DfErWt9Yj2nhZQZ5EslH--g_z1hGwI3JIJl2hoRNlzVVENKi07iJp7NRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/23146" target="_blank">📅 00:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23145">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ah3vV5VEdZOfy7dWIX5LJ9bkivw-N6Uuq0vU3t2aUiPCAd5HeV8A8nlnoUhFFbD4pnm0xKRPbkqNyIuSrIaf9pdDOjaCpfGC8WJh37QWUawOfdf0LINDkfK932vIGnkSTjA_c0taKns5Vc_dipcCdnLP46fuJYkC0DhwjcmgMSpjE5onm0ewHIVzKFIB4WeSm5zJil4e_sp4U2VL6Sxs_wdc_kX5uq1IHvf0_l2AYPT6tgyT1Fukg7J58AA6MzDKUKlDxqjADwDofevoXr1XiiUvMhFMCnyFRmADUxOaw931GmLUmySaYCHUvdnQzvIHaRd4hcnCoq7HXUqBQPZb6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/23145" target="_blank">📅 23:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9VNgN-3F8BhGB6QbulZxPdQQuzyy0yXwc8Roc_TgHcy_om1xQHG2Xd8z9Kwher2utEUhNzb5vP21jovvIYuWBgwXt5CLDhF1YhPJc9ayf8berreAz8xiQRUsumaxv_76LghuCep4yJySKL69Al-Bda6lRfDPgc8EMbjwT4tGjQEw6gxNJQjH8ljen3Rp2FmPs1LTsH1od75FvUFyTuUnMEPSAIS8efYMJP1P3j6i12vztGH8kZA-n7yX_NVhibb3TXASTo6gxCVn1qdlFaKfkFjmadRM6F7YxhLfgCF0rt8hvo4V3-wnBS8xjYMd11rsbi_dQKzcfrKMpYdg8g5-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/23144" target="_blank">📅 23:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY1cT6C4TyFsfj-d0FHWp1hxvNOU0X2jp5-Gm9fd6-dODNj3zSzX02XHDAK_CKXCb3dgiJm_VK75F2dDHwHL8SHLTpMjUcPEGiqd7EyOgVcG5fXiU-Qvxxub_IisMji4lJcO8GTYeSYAyuw2oVAPHOdcZ_zAr35dodG5WMktjC9NV9JrPqYIbYSfSyEzpeSV2KbY0NmdPaGUpDHap3UkeYnK2giE5nXVg4uVSayGqDV8dYgdPI4esLDd2IEeGAB9V6EqFaIyo_qWjRp8SL4LCeYSN2v1qWNL7u2E7-06ZmCH1RsRUALtITesfpTlG1Egbz2_5YPRCstS2GP7_AmwEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23143" target="_blank">📅 23:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GInGKkenhZiV_NACMmmUJSLpbFQah-7hxLeA8ENiDhxV5qf3ZoIw_HXsk3GN4MBCUObISVZamxlNEZBexzYKtZ3jMFQ18d5ss5sH_T6HcfRMqpHt329e04jjh0eT6CUf7GISiZiFb5sjJ3fQ4f7WoK_jEjIrxoQ2gedr03VZ0dIK1xRFyYhXxZz7PdLpq07vnkOkmD0rXVuFfa2TkaKtVqWv-6R9YYol0_1Mab0b7-OI9SEozP5MJUNgj9rVtBiLbqvMDokRlP8sKuwnEtS_gw2VJDW1QKgudXsDesdqv3-dRY74rmnhSIZ2NQzgPgig4dFUv1I3cvDxalD_UdHi7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23142" target="_blank">📅 23:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy2yYeUWFrYFSLh4wQussG1jOmeqHR69evmfsgsNlwt0y1hVxR7LHFAdXLHqWKRsHMfjjin2IK3efeFdMuMvGY3k8uKI-3a02QdRNl15f3Gaer2Y7hqtvobBffy7JFE3bbkox1wo8ftoc64n5eD8yMOsf_7sFqBdX74Bk9YQtjO-cFcArnbmdRyDr5RWmZOUFZ6ndEFcSPXBlfFLB2kYpp45760WldebQXx5u5FoOZSvCMQ1ZmmhDkWC0XeznMhVSK8-0c6XbWh2QTBEP4S0IQmgmjAOd-rVATGDUBd0nQx6oyOYixbLfQEkkhc8wcU77U8GmFLqXj7eViHnTHr0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ متاسفانه اموال و حساب‌های بانکی و خط موبایل وریا غفوری توقیف و مصادره گردید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23141" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=dIgr-9L-T2m1TJjTXokXjetHb3WCgkmNlEPYRoqXke78eWMlTADWiFOZhmWpGY3TdREnnZ1k6ZLlDCsG-ZysKRsp-WPEQW6wZXEFIy5QALhtYW7BvImDZ4bwSrna0oQuAS8uJu525NHBmdA5Dk0JmjN-9eTtgvVhK5upsLfla6gy-tuaig7zRESx6lwVqZ1psrhLuRT3qT20txiNTOpj42BW6weOe_h5W0abr8jOx3UgoGQd5Y_1JC8AddpSd19fDg9l9F9U3JCUpb1pFCpMx926-sEq0EENbTlSM9SHoneG7ePDGQTiRXg6ZwX9AX3kqSEEB2SucF-S1iSqVVvcZxSzGqSBfEDU8Q3akQZWF1a42SlBzytLwOXoF4VRPCthSvgkFLBgPtytWR3a3luvUvkxS_D-uOwYDuO6CpaJPIY1J6w-aezAt9ayGHBvR1hUhkPS2FshRGRje5iQxlGQZrid0J0CIooum1e_I2VjDMYGe8mjvq7uPWGJdSO1THOsHDDB2J6XNg819UQnz05q82IOq7tTjUxKNjVbyJ7zcUBm0QYowAPyAXhw2U2C1Kkk996UB0Ud-w6eFOipYOYBsknC2qSoXymnlmobIM7D66i9XBZhmwi5UlMYkfdgZTKjgxuci9JYwoz2zeA3t8g3meWU0FpGbmzNyarGSmf_O4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=dIgr-9L-T2m1TJjTXokXjetHb3WCgkmNlEPYRoqXke78eWMlTADWiFOZhmWpGY3TdREnnZ1k6ZLlDCsG-ZysKRsp-WPEQW6wZXEFIy5QALhtYW7BvImDZ4bwSrna0oQuAS8uJu525NHBmdA5Dk0JmjN-9eTtgvVhK5upsLfla6gy-tuaig7zRESx6lwVqZ1psrhLuRT3qT20txiNTOpj42BW6weOe_h5W0abr8jOx3UgoGQd5Y_1JC8AddpSd19fDg9l9F9U3JCUpb1pFCpMx926-sEq0EENbTlSM9SHoneG7ePDGQTiRXg6ZwX9AX3kqSEEB2SucF-S1iSqVVvcZxSzGqSBfEDU8Q3akQZWF1a42SlBzytLwOXoF4VRPCthSvgkFLBgPtytWR3a3luvUvkxS_D-uOwYDuO6CpaJPIY1J6w-aezAt9ayGHBvR1hUhkPS2FshRGRje5iQxlGQZrid0J0CIooum1e_I2VjDMYGe8mjvq7uPWGJdSO1THOsHDDB2J6XNg819UQnz05q82IOq7tTjUxKNjVbyJ7zcUBm0QYowAPyAXhw2U2C1Kkk996UB0Ud-w6eFOipYOYBsknC2qSoXymnlmobIM7D66i9XBZhmwi5UlMYkfdgZTKjgxuci9JYwoz2zeA3t8g3meWU0FpGbmzNyarGSmf_O4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23140" target="_blank">📅 22:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23139">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba85793af.mp4?token=Nb7_Ac5DxUhf9EiCYZmPqOO96f2ap3rC4YtfOAlff5aLDYBQbCouhII5TlzbrSm1ku5EbvlZXRAdax0IrfN49wQXaRD-o8dPIJch7M512q0TqOkB1UELd2Wai7sZYicWsd2z40hD1iGpOkoFntQJUfNQ4nhWaEdW8CGTdk2gsznlsY4eeP3FyFe-OQAAdwgSBLodSrm2sEDs7KjHSY7XlOWJtzLkleIn-0IYDQE6PzM3VIIyQhCaevmCesWWgYW4hiAnEf03NuCS-mnDyWEQ7oT4NWTxQzK7wJEGH64Kd3P5NZylGc3OsSIeoPRV87Cg4sKqGJcCJhkIFZItCpj3RH7VI6wcgb3MnEwxoPAKTEed-HMz0p0yWXBPG73Fpuul9L3dZYjei9rbFvri_m_BH0dTZCKIA9HQqeYDqcEHwLKpCilPzVkBtkmG-ughANZ-DdZpvwrOSNQTAvWZJGHT100IjVBqt9DnCev5Ji_HkUJd9a-Ke2XLk6i-hla_khA1IkC7QGkgvGoGSomjYH0fqSGmkYV5tG53MeUQPcEkE82K96IZ94LzNQok5qe2KTk-idDx7L2rgdusYR1AWnA9tgMagln0f0I0C0o_LigTCvYRXnBxtlB0-oVv2cPHegElQhXcUOUgqal4yDXDb0op6m3TAnqOM-pEbbKC-rHO-II" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba85793af.mp4?token=Nb7_Ac5DxUhf9EiCYZmPqOO96f2ap3rC4YtfOAlff5aLDYBQbCouhII5TlzbrSm1ku5EbvlZXRAdax0IrfN49wQXaRD-o8dPIJch7M512q0TqOkB1UELd2Wai7sZYicWsd2z40hD1iGpOkoFntQJUfNQ4nhWaEdW8CGTdk2gsznlsY4eeP3FyFe-OQAAdwgSBLodSrm2sEDs7KjHSY7XlOWJtzLkleIn-0IYDQE6PzM3VIIyQhCaevmCesWWgYW4hiAnEf03NuCS-mnDyWEQ7oT4NWTxQzK7wJEGH64Kd3P5NZylGc3OsSIeoPRV87Cg4sKqGJcCJhkIFZItCpj3RH7VI6wcgb3MnEwxoPAKTEed-HMz0p0yWXBPG73Fpuul9L3dZYjei9rbFvri_m_BH0dTZCKIA9HQqeYDqcEHwLKpCilPzVkBtkmG-ughANZ-DdZpvwrOSNQTAvWZJGHT100IjVBqt9DnCev5Ji_HkUJd9a-Ke2XLk6i-hla_khA1IkC7QGkgvGoGSomjYH0fqSGmkYV5tG53MeUQPcEkE82K96IZ94LzNQok5qe2KTk-idDx7L2rgdusYR1AWnA9tgMagln0f0I0C0o_LigTCvYRXnBxtlB0-oVv2cPHegElQhXcUOUgqal4yDXDb0op6m3TAnqOM-pEbbKC-rHO-II" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23139" target="_blank">📅 22:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23138">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6TnQM1QusLFHt8f7ZC8kidELtG54WUxA6T1f919EKKvRY9SE85gk3bm5UtrdAFKy0OTDcHv4YqUEaYXhgvshYZjfZoDGqOcCMnT3KH4OI7dgrxuMr3Jl4Ftv3y_yFVOky_wpteKSo3izxBJhyf_Vtd1IwMOThioBKbjI2pi68J7TQV_5X6-LBddBfPtyy8xVJHWhvtsTWJOLmI0MPYygWmDv2pNTYyL_hEGh75kKfZzdtyA4GoxM1ZlSF9YbillgGwQzxkLTEwLYntrtQ0972j9ye1EsxjanMSwihfyuhZ_g6ArgJC_5AHMsE_sLS4AAAMkw5oIsy55KFh_k9YbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ دیگر مجری ویژه مسابقات جام جهانی شبکه TRT SPOR؛ از هرجانگاه‌میکنید بکنید فقط از صداوسیما باحضوراون‌دومجری عنتر نبینید. از شبکه های خارجی‌ببینید از هر نظر واقعا فوق العاده هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23138" target="_blank">📅 22:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23137">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ho8H080P0JIl7NIFTOtHW4rVtMunaq3Bt11CTYZL2zKRqbZ_ypalFNvCCYI2VuRcxphhYjKTAk_ZjJfiMrpxpTWGkPm08g4rTTkatQuYYkQZ1InkoKnl327dJaO473BiKlzShduQKZWOuHDv-YpdS7P88ny2i-dqAgnwdSqluWGb43CR7tXAa8PiOhGTyzXS0JwpWy7NkSv9WC0o6hckhJ_QWdR_VsVC0-EkbPheC7qpq81RxTu49Ln1HG4odFavs-CpFmGbCL_HElL-PMOQg904hlNLMivW07BdwJhnqT-gvT9UYQybdrEZ2umKwwtsy0bFPt92xFII305lxnbetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23137" target="_blank">📅 21:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23136">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmij3XhZs47TrPLIZco2LYSHr1xR4u5FSW-rS9Ng1iwuzmOwMAUPngkyesAcj8w4YtFqNw8DMs1LIgWTGPYVJ4cG3PxNpHfrVyVC2HhFig38TF3PfDuDkCBe_KA333yr1hyOyiZc1xwgU4duPk23-pIBsWhMMIlpeZdGjtZwU3BAXQHJqDfigMqVBra2PMNupzpHsgJ2jmWlQbaT0BVDWFzm0FBf0PRndvNiueFxWTMoyiXBBQpUzZa9WYxKSHkgDeE9jkKFPOBVhS6_sHsFszin5Bv0aFAUeSLxhprqYAedDpPLtPKPono8-W7J9SmnsL7f2Z6ydRsP7NWXhXy1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌اشتباه درطراحی نیست؛
پرچم لهستان روی پیراهن هائیتی؛درسال ۱۸۰۲ ناپلئون سربازان لهستانی رابرای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه‌ استقلال این کشور جنگیدند. پس‌از استقلال هائیتی در ۱۸۰۴ ژان ژاک‌دسالین به لهستانی‌ها تابعیت اعطا کرد. اکنون و بیش‌از ۲۰۰ سال بعد هائیتی با قرار دادن پرچم‌لهستان‌روی‌پیراهنش در جام جهانی ۲۰۲۶، یاد این دوستی تاریخی را زنده نگه می‌دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23136" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23135">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2aARVeflnpt7xD7_eqyeIIhqGuzlHZyDRLn2IoLLZPNrsuo5hXiils-qc80246qW-GhWpkv_Xjnc5LqfoojqzvFWZIi9MrQR_vziBOR8adaQflEtkLpq78gJXxCzdyoYgRk-2hZITDEi-NGJCbCmAHzRvwLIDPd4Q7LdJYHbp-z37r6FuXWrlrgXE4fwv3WW6lddqHJFpYSGmBUPvcpqU1JwWEiuQvfcFGdUqBe0DZe77l3QLUCD_5B_r5sXGkF5PKhjif3P7GirmYg0S5mITr6wSX-Ny99hVSAM4_Ewah9GV81IgNhVYDj2KJde-n7A6AFCYb8DO9jf2U6i6-ztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23135" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23134">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpISbseG6uwieGEmI0IAeRpdvCYL3mklmookJjqxw5jUtVZeQ0P0DMsh1gQyj-8-IDxzI3PHfVDvnimEfkORdxD2WBmovTYqBqPA6PDsTBsFhBNPZwhZtu49FlJkgyqv5SXemgPK1qxaHAWaThNwidsuJhCIkuLrCAkKcDYgmPEE7fB3BLRWTohkJM8D-lWxpyQIRoKk1y4naN94SSq5Qwqt4R8YfBbUBo6D1BDNqnyLXRZFjIdIfTySBNcZNqJLPVn3qL7zZb-8X2lqpeIm4O75FXYBPdHfldFiMdey7dZkz-1iKLPEfg-xF3pudQj3bbnJWhz1aZ1v7z_3QqFPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23134" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23133">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rE8V1hLB6-GC3piF2Rq9i9L2nCsZcTyMpMQJa3HYCpea5aMlNdz-8-03xiTtO_JyY4pjNEym5T7-k2gFywZBlXryqnNNO5VNNLDNRJqIy0uQMdMhSoJy-EklcjUa28AKnNWe-dZ2bZh-iRzcJf6Z_ZxdRCNN31uWVyoa7a0aFpZf9n73O_lCzeYkwHq-hf6JIzEEiu7-M4F586DWpEcF4gnUS5vHbZ16rrlWInTALdHHyFnzbnFBkt-ISjHNYEdv8UglfB4sQQGVbU5-QQcJvYS8fpE24FZIfnssBOhFj6XUz4iWjUWV5AUFob82hpxYFMyd4qixolIw9YLUC1V9XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23133" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23131">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keZqUI1Do89dJ_uJkfvBsPRWLY2qJArgivgt4SHSTai4S3b0-l64GtNVL9OG62usGe2YH7tcU7y9ghhD_i2GW9kpxO7zVdCgkAfxPAFIEvqf5ExgE1preRLNYIF4XTlNLLT107-jy6kUKF4JQhfIgjj_zuUmklqRGDEMirnKIwJB0Pcn1D2-CjG941S19cjsybAmT4Obqo49oddObIHL1Z-nuCZntZLKXE-gw86toL6zRugx1-SlalRlAHcOwaZClBN5Tae1QkpeL0h4nXYAt8hMD2Gdibq62j6E90aPjSocfxQRLb-HC74U7bobtwhzPzj2qhRLkirLvUZ_JuomSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-WrfYpMTcCOG9mIR-FfaXLWUkMP8dIfvl8IufvfIE8fQV81tExVosKcZCqUf2nRC0wVOs8-H_jNQS-GbNHpx1WXuj8j7PT8-hb7OXw5xXle8Kktph3ZnDY-FznKR6b4hMoffmQp8ijrfSqvISms2amezfe90cZM8jvL9BVqNSUX0KODLC1hywlflJB65aoS29B6W4l75_U0ztYaceTg0_FSoWFTx5u0ywZ5OoPflij_ruDjRCOGfU467FunbVLJmINPYtWAmpJIY54UlMAYs_VHQblKHP7tl7dKHddGYqi-OCASxW0PdrG3kHHckpBBd9Qd9fqLK_F-T2QM-IZrcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرخوش: تولد و بقای پنج توله یوزپلنگ در پناهگاه میاندشت‌. ‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت خراسان شمالی، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23131" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23130">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=U7IsHC_u1AsPEAHkQbhcITBl3qVDuYsP9RCPFSyMEoNPSPrWslA2hNPvGTbLvXEHMcha4nb-qGkD54CC05rDWkXa16Uhmawh1xxHEHdQV30i6mdxtapYSXaW7lIzai16kHMEo8ud9qfVqcFk8BHyz9o_uHDIHmrlS-G1u1rojaayBgjMVDZZIlz9CapUlkzUNAtf5jtsWNUrp5lam1u30bmV8MGzMK5i-AQJSPe6zYTFWgDWzSDVgzmOwzbWA2F1fzY-2a7q_RQeJIvn4DDTgTvv9L4_110fKz-l33ZzWnKYJ0JwWAYLsfRerWtv58oaz-itE4Q-2CB5woo9yRrUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=U7IsHC_u1AsPEAHkQbhcITBl3qVDuYsP9RCPFSyMEoNPSPrWslA2hNPvGTbLvXEHMcha4nb-qGkD54CC05rDWkXa16Uhmawh1xxHEHdQV30i6mdxtapYSXaW7lIzai16kHMEo8ud9qfVqcFk8BHyz9o_uHDIHmrlS-G1u1rojaayBgjMVDZZIlz9CapUlkzUNAtf5jtsWNUrp5lam1u30bmV8MGzMK5i-AQJSPe6zYTFWgDWzSDVgzmOwzbWA2F1fzY-2a7q_RQeJIvn4DDTgTvv9L4_110fKz-l33ZzWnKYJ0JwWAYLsfRerWtv58oaz-itE4Q-2CB5woo9yRrUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇷
حس و حالی که از آهنگ‌های تیم قلعه‌نویی و بازیکنان منتبخش و تیم ملی آرژانتین میگیرم:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23130" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23129">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJn8UyKIRy54n3hgY8coHmLVtW87xlqow3NzBkMijRUFtj6Dt3J69nbRa093IrtnLVz5QqLRscSD9C2x2FXbmkxJbiRtPoHaFaJpjEtIqeuQOG_9-2mBQGi1Vuh9TWktVCuOyZdrX9PPIUQBSPu3ItecdKkLL3bhEemFKpOVRVHWuUmg2NEuLxLOgxMOzPeATDWYFy2nwsMb5zhVGpshlUcijPTZwtjjctorAG1M9VcY-7gQL6T5v1sMkl5Myh3_7xpdoxCUzvWybHqGdd779TGR4ofdXQumzwuIK0Tjen6qrsjIUCu_O_gE0xjmWVMyDiGN-Fj6Gdn4ljvPAczqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg20
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23129" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23128">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ-ggHNAAC4zyuMPWAuDmJCJQFvj4FoT1Jdk7HDX70HBzqiLQbHmcF_-d95hR2hatOAu-KNbmCcBvui5IKHr3eR98afp1HerdQsP01xOjPSCib7hEJ850ky97KUifrxSEnhrDIyzDibIEeKpJSohZbxEPmTynLeBy5a9CY7UVRLEGnHGiACdB2BxhrDl5xdTqwbyljwWohMLSami26ZgqUREf_jN6Ql3Kr3dZryzyrZ-7BLbL67adhb2g2DslTK7NdBqg4yOxdoSTfpWn3VyrbHnBROc2ncfLE8K7kDDp0CJJHgIl4xVjieYfOyperQ8fEiWNGpm_xI6k0-GRpTTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23128" target="_blank">📅 19:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23127">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVbcQ0nGdBSbbuYJOSoVDr9TylwJy9Mw_w_3AwA_fXsgUnKvRsZZWKS4Lot7In4QmJwNYfMVMS_KNSNipPdYtWbXh-iMzrlcg6YUoWkEwYYcM-jSxA0unppqSF-ghIlXo7wpCZ-V9ysDGenrGv9zJexo1I7LErilgTwVNvtxdzPrHzhmxpJQma4gNhqHDxY6dONaT1JhLnLSM75bkchEN3lEDeLuq_yL_BhoIPTWheSMR3WtHSfgSTWpJAeIX9BWyOv8iLBfNSS4A9t_zbuZ0fOOEtqm2V9YImgvlc119ZjOKQs3QD_Utp69PrTOaiX_lOWIKc1HS-8Ry44mUhBLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23127" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23126">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-tc1fid7QZA7WNLJ0R3_MBBbaezM0ztCbAb10Nau7z5MVEFIKMftHOQHFkWGn6M89mMxvNspecMdBK6q_VFH4PYQoSY_UvKYwDyummRpcvlzAqYYVgT5W7vJ2-x_M8B4I0teWl4gvVMhxZZ7rHEuQzLMxJ3OL_2b3SPyO30yaiT8Z3_l3vEUS3Kiq9Ax21S6uUcRZ4xj7Pjl8j9s_4SopgRIU1_AaI8m8Mwsrb6lC7WLQqtIAFsklSUIB-tgg-dufWFICAZsu6MvJj6jbjpZhaSTved0NWVpH_c-BFPWGNxUpnxc5vt5pJs1Ap_jfwnSxX8VZHShTHv21qhhylAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23126" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23124">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOkixufHAi4gRsE9yokVrcxsDU_IM1V_gteRx8EZJxAL0S24z1u-DtW0WGxM8eJb9d4SzYk9q3aRQYJLoAIhyPCacpfSm2g1ryvZZWCS9uVK753LUHDuXCPvnh0CZlqJaPop3_nS0oo-Sz2quAD0I6JfhBQSYjQ2gfKK7zcIG7LAd4_dI28-mb_DskJ9hEEnLEzHBdXBe8P4Y7MouKuBrrBDhrP5RZwZ_fgwhDohAXVYRnfX3QH8MxTXNRwCelfYQbsrOVgvrOy4rik3FLOxPWyiB_hFFFWBxXbrDIlTmO4k-Hh9JUgBCWZ9_YvsBKkxzILHxk-JISNI1UX3tPGn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeqkWxonFAn5eypWDczGj3rcuElDpiV-3N56UIVKEppgWUGfHzlKDn-D1Ahqh7XdzPyJoUG_c_5j_-wpX5LVDDOoib7gxbjJ_BOk2gUGBkJiPVH3yVBYdFyipGfinVs7ZYif1OTkll5oCpQPWO8gXCchE5YLvVI10VmFn4gME6JXJjMiNPrBcWUCBK6V5MjvKneZGvNQANjHJsAueriYkqmrT5ym1_IZDlD29uUfpIVz4ktn_xDXRmMQn9vlCzBicyfgZMXmPTD-7aWRLWcTggXNTQEoB-hEzUM1suRRmfZ2jijQNK-LTqPzhYOSL5grdf20UGbH0pDzawHKQUIyIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23124" target="_blank">📅 16:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23123">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPvx_nKbp2P9Q9MGsJPV8hvjkvJ4Be-uiwSyApgpT4kI_EOlwKgwBPHgaAAQmkVqLYaoNGo6B_WNhV1VpWrtHdMhCSG51bIi0zHvXg2yDdCyHBNVGTMLDCMqMzvkMhWuP_hVSMo2RolvNCbEMN9qzNFm1FzTt9MO5DPcf1p1mV2a2xKaeYsG16xkCotvE9eooPH47NdPqRkTofOUb4tbYUK-YGtYHDHJ6ISL-7vbTY_xUCLhIHWHbcD14s1H0azs2qi4YvDWFKFByRjjXRL6XRLqiBIcc7VBYFG2qtnsSPeaqGG0xo5TgOwDknHprv3FtFdplkNtJi-aSU5MULA-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23123" target="_blank">📅 16:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23122">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میراث‌ترسناک‌ضدحمله‌های منچستر که بعد از یه توپ‌گیری آغاز میشه بامربیگری کریک پس از سال‌ها که توسط سر الکس فرگوسن اجرا میشد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23122" target="_blank">📅 16:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23120">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnZE6Qec2JeTp6BFB2Sh7vts2ctiTzuofh-K1Kkpb6rlBxoumPFdv5Tqb7SSFFurt_-wJBHar11k5bgSuG5XvrpJ4kyFOO2Kzo-RHImh6ZGTsD458uAceak3Xn72z57m2ZHKR3lJWWWZRtUdXqjfFUiWy-kt-BC4n1jYnxEFsb0pL95uR8WZJeNbua-4Q9HugdR1Opa7t9qZ6nBYS_v7aD9oikWWmRfVhLH_UnMNAkgfNYOgHWhGIZN4S0lvhz21DE2pf8aerzc59nf0WWs_tTYMa1IXnFYC-QkGu48E7r4esCmNvwzRtlwkMewMmn6NlFCM2obKunbyUf6Mf-hxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgEhGh4r8EQF82njjeWc_dTYSEBpr7QxfgpbI6vG6jiWCUkZ3SY2IkYvQobdoH0bSdNHF8ZSHYtV2XBX246HJfLGQgbS4TWopZVDIXlbkovSrjeZ5eq5SmALQbpX42EzNCXzDi68bLyAI-EduvDPgf7S5FzmTF5mhzSI3FJLfrfrBjGQOsv1cMeM5dnRlK1wibMaqMIjW4ES5M1tpQ_yjK3NngDqbuczDMX82iL9DoS176ovWZVSIb9FqT1nXdcdON1Qvg3cLLI9QvjA5BLQoqOq5fQCR0YvSpOHA6Of9DAYJflzDo6InX93v3sAXc5fCIYHuSNt2LLgw4anAzjc_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23120" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23119">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfN6yTPE5MWEgaj6Golc42wcTUk6w5Bcu759QnG8wdSwG0iQXUpGfgTU6bJmoR8YrVg2U-TxcP3W8nrwMAYEfAWBV0ugK7VZ6IflKvPn4odgkiAvvIq4eK0RVm-UuA9jdtZmoBugGJb00Hdu8_TTGcNMQn7JqpsAEIJu5GxCw4eDWlG68gKB-hcbplVgPvL5evbLBLN9_LSCSA1WJJ48D6TiersKrKqhXHaR9lMEpS_qu6Q8Leyrff8X8sjeTQqbZtNbvxYajFGYn2SvcpV0TmFjndJvWszUeo-WRjOeSV3_Gf17CSkLOyP9u_WAGH_vpDL0D8FSGEm5u1QZE4ikpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23119" target="_blank">📅 15:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23118">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C0uWg-WR75CbOEjoLnxSyj2oXkRoyyAk8f-xyYf4A24e9RTJ_W6GeQO-12UuK8HyRkypYVKUvyt49fEb3Hx5FxiO6gEd04xUDEd8hVHsgMfNmhy7p3RBARpVUoIGro-0z0NLLlZuvaHo2FOBjMrllcEETcY_pC8OQUtcl-jSMINcYU959nPHxXWxoOZ7q__BrrC4G8snAoZTLIWglKXcwLU2cYhkUnuscUOAMYmKnoRs1wPIqdvkPsYZdaYw9D-Omh74In0Zi_F_i3miynfFInmLWJxMF7fP4qXpwObXmeommqB2mwzvQfXXnsxVzzloKEfPzgKNyqHay-8vHgT_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
شهربرلین‌آلمان تازگی‌ها یه مکان برای شنا زده که خانوم‌ها در اون مکان حق پوشیدن سوتین ندارند! همونطوری که مردا سینه هاشون پیداست خانوما هم مجبورند بدون سوتین وارد اونجا بشن و شنا کنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23118" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23117">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nnv84wqOkAYFdNgOC2UQYf8u2ojnd4mPPbArxOK2LNf3fH6IRFacJg5k25JupKT80jt_DpfaZZPj3G9tgfUKasqAmodjUE90CHCEbERTTHzM8ISfjrPoORNDGgYvBMbZ8qbXbx08QN6GmSML-wDYSbsoeDHbwNk6H-ub6FO8MTt8L39b9-2_bbJeA24S5nND6k_XuH-cfjtEbcq_YeSBskTbAPPMCq6vdryHStnm_Tg8rXnGq--E5UcDvSlAZvo5SHFbcxeYWgxQFV4QYe2R9tSyTFbPuUMI7eXmLR3xt04nRoPaoSK2uMXldZMswDYpI21_fCcYid3MWrypcnr4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23117" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23116">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNm-vIRPEd_v-VSlZK9VV_iGmPsMnlfOOQwweF2XY9le79b4FbLiLC964c6P-fAxY8j0QrVBjnahaFi2ImQMQ_jtrpKftQ3jAVZANxvdKd51ocOYuZoZqhHL0-q-rmR7hnjuPbKulNv3dvcx7kY6pjRAlPOxCev_2eZfcQNHICPG9TZBLnI3PKc-SJdb9nTpSxKGPom1IlSKWQOO3RRliZzbKOn_1ZclcVj4spPme6Y8gtxGzvFzPJoV_2270DiPUAoT1s3zG7K_IH6Clr3rjpLSHX0x3OkoWiWQv3wic8eH6f-L75rWcJQ2yV6N-K0krsjiIVldf4Ph6pQUxLeA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23116" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng9ErlGwhxUjnhEJGw7IRwnF6Yx_FgiyiOfN48yspZGbiQnFUGzgT13qB5ejzoXoqDPumVMOW6nWQd5K55FuCxHsPq3YV4ZHgg3urNj5I3v69mA01DjLftD9wdJWsHx1qaW0ybRlpa-qwNjKWAtf0beDUt91t9ZIMHaTlW-hTMxUSXq0d_yFx39PMzuLBWs6hhELVwvMiHjZ-Neaok0OaGi9yEV8o1iU0RHrJxdsg3BPmjwHwV4G8b7buNK9qfT2kv1_p1-tczuTwPVmCDME8wOkRZbT71cPm4_8Izt-BgbE3xPMQFm8oAZCnFfLg5FLOs7TkBNmwnPd-kdbkjo5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23115" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/in3g-wWaOYS595IhF6zWPY0V8mL9tTEHC-0otl7cGMvgogOJtl2jfx5xLkeoERvl-0Xat3dEq0GHy5mnsAaZvZ1jEZ2DePsRwmnfJTQKqcCcnB99BU9LVqEISZlqSdmU2kMsvByZ-MYfsJ70H5QDVqumARGBSI8mx3Tvh7UKDUcbrDyWvqm-f_K5b_TaidHqCqP3MgtpYEXZumqBJkBLeBLZVtn7d9fSbiBAyJ6ZO1sOCUsTzeHOKvR7TUPvz2lTRQjcSB6c5wNmj4oRM5LReXjUl02ZouPZ9JikG_12K3XFG28N3Pj5LLclco2JWd_V3MRRTQo89hczP3zNJWVlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23114" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=M-pL1aTdLzdrdQYnj88RSvvu5Z2Bb6WvjMBq7nn1jZxLiNd_aTid1Zriq7BmkTKhKEh1kYGNKwVET15tYShB-Qwt5HwF3L5xG5AifR098TlG0-BhTPvS3pqoyR_f1-vh30o5sATEXFU--t3qXkssGSwp9T81x6DvvngJWJ-g39XK5EcLaj3kUL3JCn1EPsutnKsnZjFvBBNc-KSvu76pjaWlW_D2FNRVcYBjzQcu4MMGm1E_bNUhZTNqt0RCOMwwo0mu5Pndkm976Az4XzNhBmtVKwulVT6yTpUCAqDUqS6GXXpSQLB4opaKGA8zJbFCMHao4lE4wzjCGKr4QBAtraR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=M-pL1aTdLzdrdQYnj88RSvvu5Z2Bb6WvjMBq7nn1jZxLiNd_aTid1Zriq7BmkTKhKEh1kYGNKwVET15tYShB-Qwt5HwF3L5xG5AifR098TlG0-BhTPvS3pqoyR_f1-vh30o5sATEXFU--t3qXkssGSwp9T81x6DvvngJWJ-g39XK5EcLaj3kUL3JCn1EPsutnKsnZjFvBBNc-KSvu76pjaWlW_D2FNRVcYBjzQcu4MMGm1E_bNUhZTNqt0RCOMwwo0mu5Pndkm976Az4XzNhBmtVKwulVT6yTpUCAqDUqS6GXXpSQLB4opaKGA8zJbFCMHao4lE4wzjCGKr4QBAtraR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اسپید یوتیوبر معروف رفته‌سرتمرین تیم برزیل؛ بهش میگن شوت بزن اگ گلش نکردی باید شنا بری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23113" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL7gIrB1HW_ZJa6uG-xhMo2sIpSvXGLkWps46nav7Dj7NfHgCVZ8gCD3D0y388G1jP6HRJ_W_bEF_9ltkaizeHTC8z9VdtJEmDJKzIGbnecB2Lp0m7Qkr7wzAgnW8EOoAgExpYhdd14lgbWaC6mKoT16tqS3BqhyYaEy0ELNZhWQWWDHs_KLah7X7el-MMA6HxY947cqnePbM3VCdjcBfGoR88UFkhuetj6GYvDI3JqN6DFHmLUS4jC9klhkGO0XsBACHkV2dXvW4DJy5uaaYYuSgF8_2GlzxyT9mkwvUE0CYJtGXUxyOosUAeuGTi9uvN8AC8LZJQTFM8vxht590A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23112" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-ufAcFTi3va1UrGsCzqxsypvegTChOKlkiRTrgACwpPCHhrPM5Siq17onCo5_ET8_MjRUv-Kwpf4JwtlQM1gr4f8d4XUw-__65GNSx20mIPSzjVSIISDlz8C4rVjvQ2evkOusXQZRj1QqgghlUyn4pfJBrCXXFGGv4YSmTU3y_csjT5lDSpeMXzmRdtRqzJS--raeTx7r2jLLswOArmesJ_poftmQc4u7fzz0p8i_YqGCIosFfqnBdWlhLabQzZwIvDgntKl9o7VjklEdXU7BNGoI8nKHgcS2rWvogGZjbnR8l5cAzjRnxi-7vKM5ch4b9HgwjGmoNdGpIa766Rsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23111" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=ZUH2UjryszugON9o8XGiEMI3GT2tZKLFPvsYh-HPQgTSEFMrrocf_VsO3WWf5TE8GihYUX3HzqPC0RnBMhDUBqGYLAKqARWiy6Vx80-6tTKb6tGt7wFqhbRcO5ICKhUHK_rGMp7HJeC34ZgGgLYDMt4ilRl4yiCq-6vIkRsepXdXumNwSdnrCEcuM42bzka3x3n8b9v-az-USMvfhtHlVjOCuVIQHy9ZSwBkx49pFufsbYNsq_34B76TvGPKcCbBSbGJKv2KoUiv6pXrG9YDF6MbpC0KK9JWAHnyoBFj2xVVcAKXHFQw6OhUO2w5bX6pWu_8teNS8A1lJd3ouJ495Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=ZUH2UjryszugON9o8XGiEMI3GT2tZKLFPvsYh-HPQgTSEFMrrocf_VsO3WWf5TE8GihYUX3HzqPC0RnBMhDUBqGYLAKqARWiy6Vx80-6tTKb6tGt7wFqhbRcO5ICKhUHK_rGMp7HJeC34ZgGgLYDMt4ilRl4yiCq-6vIkRsepXdXumNwSdnrCEcuM42bzka3x3n8b9v-az-USMvfhtHlVjOCuVIQHy9ZSwBkx49pFufsbYNsq_34B76TvGPKcCbBSbGJKv2KoUiv6pXrG9YDF6MbpC0KK9JWAHnyoBFj2xVVcAKXHFQw6OhUO2w5bX6pWu_8teNS8A1lJd3ouJ495Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌قلعه‌نویی‌وقتی میبینه باید مقابل دوکو،دیبروین،صلاح و مرموش کلین‌شیت کنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23110" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW26N565nuDD3q_iU1CSGz5M5-CZliuqehhS6LzoiBMxCBcDu6U7lQsvO-khZE2bxjWiFjpjIYYLa7xmhj3EEl4f2AlhLFFSZHbEzMPWC1tG3q4ufN5J3bQMpQjM1IWQZ02VOQRZHIoKJdZPD99F2LgNiDZFRs69-gXh2Kmvw903_QNdci7Mk0WxmUVLZk5u8XSkW5NbdQdi6yEbp57tKfa5ofcqCXF0f6y3YSq3QTWP11k2bE_BP-jvO0O-1TOR6k9fj970Q0B2yx3zL2Blx-FvU4Rbq5QLcbRRpb-8Sf3iGTO7HMozrJxtuUFr_HuCmaSQPK5ZNxd74BxjPEFtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
دیمارتزیو: باشگاه رئال‌مادریدمذاکرات خود رابا باشگاه آرسنال برای‌جذب ریکاردو کالافیوری آغاز کرده. کالافیوری خودش برای عقد قرار دادی 5 ساله با کهکشانی ها با پرز به توافق نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23109" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23108">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSYly5KBF-C7Q54JZSeYSNh9bS42OIDtUteBObqLVcmPgHtWUAN2u161j_tlSBvviW44a0agB_nMZvVcbEfEyP31NhxDEzSvTod8e2AmhR4sPE_3pnPtmMMk4zYTcNhFWH3kO-epkkZ6UoW4ZP5sPF-Y849S4yoFoVBPRVXJ0IeMI1RHHhkEVFSS_8zyWPzLTNsHqNS-y9SOUUfc05fbCJlbdNHyeAEqDEqj94tWWY7hKHzC45tbS0aw6qlUg-Vrc4igRGbF_dKust-DvU-w3k_ZD_TA4byAS_gz-LxhV5lKtjCjGZbPy-EK6gLpq_5MQCc_CyotqJ925pfNc5K-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea20
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23108" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23106">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgElmggRNQ9sAApjsDbnRQ9TqoFIr0ECzcIYiqqqXrf5fgismtFt7ANswGR_WxPuU1TwvdC0QOvfS6ThfKqXR7LjrUkyMki_CwRpHY_D-BtIGlk0t6E0pga5n5GUwu4si9SMfvEjriM4LfryKrkq9wFgZ7py-yRypIVHQ4wMcG-YSfxU2CgUFJztzBmsU9Vikj0H9lYKks9mZicMZewUdvU8mODHXaq3H6GitcgrOM3dryaFEvJKuj93f5y8AIvkHmjZvDFviyw-eKzWwmBMXF23hrfPw5UOxDaPzEZJqkvMnxLyVnTYcrzfEA_WmZWEjdzBfHvTiaojGvarErg2lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23106" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23105">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfpcQEwJQrvtzxE6vt703Ph7EUm_Hz5l1RPAXkHKrtyyaNb0dVlCUHct1HJQA4jAeKkwQmrR_IhlXlFFT2VH_tTLG7RcXEKkLyWRCST-zhTrMAWibbU5KdmnKdCbVdKRpCliOcrl2OZnjZ5qgM-LsPoPHPEdVhmp6aqGNUImWv_vZBEDUW9rADyd_ZZedCY63REa9RepshwjjES4l8x80obit1i8vNoWovcFmXc3Qyeynq8L2tqS1C7_CasISBZwa0M_CBUmjVaBwK1POJBM5853xtvs-tqKjrDZIi3XEZTOnqmK707WUxat02lKZ1U--dghrniuXOcwhg4kwWg9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23105" target="_blank">📅 12:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLjv883tZDRjrLUMRBiWHm_4eW2pCpi2b2ZbYYf-UDIsNFG22kh0-rgn-3ylay2CJxabHFlkbTAOIafSl2FaSvF_9NLDo83F48tbwzWhpX65aoJFSRNHHQbN8pxdRSMZKsopJtZ-3r-xa39u35t8KSCXyUQLImCdrQ0PtXHtKVtzWBb9eizre-Mmrsb1oyslmUo2F3z9WDpFlxpyZ7j96ZH6KqjsC7xM6MoqAEIA6-rD5UxvUe6jKiW8sYtg-Y08T5r819xytyKUmZVWI3GyRWGAeJMEDKB4tgD6h57BwnC9X5f4z22COOemkpRRNh0Nk1u9HERUEsW04c-4jYhxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXiyWy0I4DjTn6-F2il36pqcQotTE5HwLj1R80tLH12v8aQlpvgyj6uud42RpS4A50mHOp_oWrA8ZoYrPlucagYn665RawlAky70MYRATHYenfdVmB0RwzcX56sbMTPXBIciI64K5NYbm0mcAoPsn0e__KTaRMyjVRCqvVuCquF1yzIq9kqyhU_vIvj_IIUV9pUKmzUPmWiQEAQx8Jz6n0H0e4ywpRane1PopemR4hSiOmhiMEDMAPc48IJ-OeFL-57UjS4J4IzmyXtIdwi9YoeTOPeAysAcmQGFXtUgCEk1pPjE_JtsPhoM-NLHBfBwB2fIxu8ibIn82HtMJkmG8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23103" target="_blank">📅 11:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDGY3uqTurmLlwmyi98-ed7Z_rwDj8n_cLcYolZ9se7MiQZlpw4TmSDKd5Sg21Iu_eURKa8Khb6BWagRX7U9XxKlty0QAGvjqZx8184PEJXZ6WwddTVKC5Z_TyeWWfu2NmmKoKxrLlOAJ5upi3greZlXGw3zKSRSpU-MJFcety0xmS5rFWi8GAqy1hBUmQsLKq5Y5I3O8v8B5Nvn8Atyx-9o7OgtuMoDfPk5HVM2iap7VEy7Z6Dfp8fMgkXKDNpX0-6HacPgaDEyKHfYNfD_1SjjBincIFOr1EZVu4h7p9N5O6rLPRXXAd7zx5abDDkU9-a7pATP-INbaHljN5H_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آب پاک ناصر الخلیفی مالک تیم پاری سن ژرمن روی‌دست‌مشتریان‌ویتینیا و ژائو نوس: این‌دو ستاره رو به هیچ باشگاهی با هیچ رقمی نخواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23102" target="_blank">📅 10:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23101">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hdee9dzAYqQstRToTQxik07JXMZEcmdWouIGLQFCK0m7YdH9AHoFzgRakQGCG6Sab31Zgf7QEcUnJYlcejrvhsuGqe_bwl1PN7AUQ2fRFYitBsPs51LJfbjIl7d6fWniFEgAQE0yzmvyBEu2ufRkH2jZKLo6RG1jeZHBeTykghFalsMi-xQB7n3Cf4WCuXhT9gsePDn2MyK4L8X9W2qsuAfrThYEGHSPYYqEy2N-JkIlZpLWdRd00N3-EPXh9yUZiu8uQ0UuFG16kvptkI3ZV-m_2ClPz8oWXWEZY4U8pwH5KIkwXdbTG8Ev_xpiMKu8o0ICQicdXwKXu5nX0gS_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل گرا مدافع‌تیم‌پرسپولیس با دریافت چهارمین کارت زرد خود، دیدار مقابل ذوب‌آهن را از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23101" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23100">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=l5v0u_4UpHPEmNFQtzZL9PTRn02D0K8pqo3Q86u_OfV5SO9e4sG7QaEiuUo-2Gftfp5xrk7FjD_tGlWeZaI8RS8zzsWbHJcBOjWCpphgji81BudKFp-sQN3muBSrS0KyJFplyhw6JLMA74ERG2ZXUdJ5Xv2cspHSFFy_gndCjeQxRz8-8EQcZmh-bGlPmufZ3lAQer4b8vKez_EVSTtxO9vuXDSBEZ2sADgauXT0MNehvLfwe3PIHlSEdDdQWfVoHHkmgXdFjt6yy5VE1sVQSP3FUydRogU5Lcfi76SDol4sRzAHcOU_qsYHxzWOxXw7WCumR3Ct6UN7ae_8U44Gcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=l5v0u_4UpHPEmNFQtzZL9PTRn02D0K8pqo3Q86u_OfV5SO9e4sG7QaEiuUo-2Gftfp5xrk7FjD_tGlWeZaI8RS8zzsWbHJcBOjWCpphgji81BudKFp-sQN3muBSrS0KyJFplyhw6JLMA74ERG2ZXUdJ5Xv2cspHSFFy_gndCjeQxRz8-8EQcZmh-bGlPmufZ3lAQer4b8vKez_EVSTtxO9vuXDSBEZ2sADgauXT0MNehvLfwe3PIHlSEdDdQWfVoHHkmgXdFjt6yy5VE1sVQSP3FUydRogU5Lcfi76SDol4sRzAHcOU_qsYHxzWOxXw7WCumR3Ct6UN7ae_8U44Gcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
درجام‌جهانی 2018، آلمان، مدافع عنوان قهرمانی داشت درآستانه حذف قرارمیگرفت و در حالی که 10 نفره بودن کروس دردقیقه 95 این شاهکارو خلق کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23100" target="_blank">📅 10:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23099">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇧🇷
👤
به‌مناسبت‌بازگشت نیمار به تیم ملی برزیل؛
ویدیویی ببینید از شاهکار‌های دیدنی او در سلسائو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23099" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23098">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2SV1ouv63MCUsuz3VEDwKNSQydOdtKuT5ltIn3n62NYBkyjK0lnrRtq5Xv3Cpd0xBzQBPhDn3MR1H65QIFKAouD9VaAN_GkVDuG327vx1CnHE8xorAbUkfIJFoD3F_-9K4rlBKVFDdwIuJtxk_1HP4uT81OyM8SwVwvMwWhkbmQQG_5XxZM9JH5x9ONdKwg-VaL01jAjb59rVmbLxe_mm6ZmEW4S2G9vf8gCTqutYkzmFTcN0WVJL0cTdqQB67Vc7HNyO0d4-vx_CSAKotNWL4z2DIgs6JSJdhYnK9c3hB9SIk56576FxEty7sFtawv3pKrf533KD2wT5HZxSxUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی جوایز تیم‌ های ملی در رقابت‌‌ های جام جهانی 2026؛ قهرمان 50 میلیون دلار میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23098" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23097">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_DYtXEy_XgwNfJzknfc2XoRx4nx_VcMHXJ2q5KaAuqAAQeqRsbuZnngcG7eHsdGZ4zNrZLw6gXpMdAl_dK8u-WfOXWYiOAsfL46bPbnP3ndFyNbV84jDWbJI_7pt36EFj0_HdOpjrKDBa2M4jVWP9iAjolPykvTLETOC0qUvpJGZ4Muten-3BS0XlEREstPGnAhVbirbCGokG9kHZ7xTm18dHB1UCmwTSHona0lV00_jdk3py0It4qB1XHi8yvHqL7KTWu2eaLfD30RrtzFWzysprsOalFT6PohtvxlZBD8CyELR_RHjCySf0OCYwi2tf2Rqo5ljdwKNew3wFgAGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان:
بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23097" target="_blank">📅 09:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23096">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=KTpT3VF1NLwAnj2Qqek9NmBdsQV_dYA1smfFEPjGxGNgGP0fEI3DwXpwx7257NoaXS15DTTksGWYn0mMkf4lPu6-WgizJVJi2tKpANexZL4jx8W-C1lvPusyqQrMWZwkFpAKAbo9HjNinjJ2B1xN2pkwZoIjC250uaIGu89D97sUks17YfoF3_cX8Re3nQPMH1M0mv5IwZD11vPBU6tg4OOCHovXkzHrE5b1qj1AcqMSCAsvJ3wPWrBfzdXWS4q9mr7Y5qTqcjl3g4Udo9I3oucsC6ccZBqfS3KHoUgv0B2r4Uljk_IJBc7Exh593tSev8dWrdF0rd7mahMyIBDEXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=KTpT3VF1NLwAnj2Qqek9NmBdsQV_dYA1smfFEPjGxGNgGP0fEI3DwXpwx7257NoaXS15DTTksGWYn0mMkf4lPu6-WgizJVJi2tKpANexZL4jx8W-C1lvPusyqQrMWZwkFpAKAbo9HjNinjJ2B1xN2pkwZoIjC250uaIGu89D97sUks17YfoF3_cX8Re3nQPMH1M0mv5IwZD11vPBU6tg4OOCHovXkzHrE5b1qj1AcqMSCAsvJ3wPWrBfzdXWS4q9mr7Y5qTqcjl3g4Udo9I3oucsC6ccZBqfS3KHoUgv0B2r4Uljk_IJBc7Exh593tSev8dWrdF0rd7mahMyIBDEXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23096" target="_blank">📅 09:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=X4RP_zO8aTeByTBUOf37ICzUwA7BVrp6EyfXJOLoEHld4nWiekkT6R-aNY0yk-iUYBmqREsRqdaCpAUGIdW80WPDFBVgdPw-XBcYTYEn-4FhZsHiEd4KHDhpswHJShZ0jJ_VO-MWZi6z8KU7eYSl6owWY-PchHZU-nf0bwSPe_noN2bHTZq9-Y5imbtFQooUSXmW3pk0diyWMvf4aSM-3k7fgkXWHn4GWXIHByfn6AQvVI6Pu2sDMRyEX2t02Ju6kAy9-Wvl3KWnoyJK6iyfqnMmPV9C3b2UDNcNAXj4FAqRSMLQ9_JWEJlRxssU7aooU_cQXy_ym5ORjoGmqBsIXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=X4RP_zO8aTeByTBUOf37ICzUwA7BVrp6EyfXJOLoEHld4nWiekkT6R-aNY0yk-iUYBmqREsRqdaCpAUGIdW80WPDFBVgdPw-XBcYTYEn-4FhZsHiEd4KHDhpswHJShZ0jJ_VO-MWZi6z8KU7eYSl6owWY-PchHZU-nf0bwSPe_noN2bHTZq9-Y5imbtFQooUSXmW3pk0diyWMvf4aSM-3k7fgkXWHn4GWXIHByfn6AQvVI6Pu2sDMRyEX2t02Ju6kAy9-Wvl3KWnoyJK6iyfqnMmPV9C3b2UDNcNAXj4FAqRSMLQ9_JWEJlRxssU7aooU_cQXy_ym5ORjoGmqBsIXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحنه‌ هایی دیگر از موزیک ویدئو شیدا مقصود لو همسر ایرانی خوزه مورایس برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23095" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PNhC1_p9CWurfE6Fu0AAqnEmBNOAB1tuIFm4BNu2w3mewblWpkeBY4GCBV5VZ_s1CvZCUqVHRK0Br8H6MCbD4msogSMy5mBKYHycRP1RRPD3VZBq4TAdwakHgfUzzbH4QNW08GZKDHPukfTfEK3bDeobh6bSsX4lMl4TdYRq_7NjwUcctfvdO2UzAuxN7dH7lFpUZfK5mOY8S-a9qAHzJZW272FtBt6nnZwSqVTlQYjk0UipT5fICe001Cj6qEIRmXP0yj9ZKMn3VsXb7_aOp4d2sQkRw00TLtJcyOvUjAQcsUI5hfbCXP22vmpMQp-smY7RW1fad9Dm-OrT-aGmbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJXBxdOj568ccGGtBHVFO_Hx0b_DdCXHXTT__teUfX-6Uhvz7B7GIthK7HKS3k0amZMPXgRF22JCRbSF8CqDLnRcy-wuiBDgrt2KdifHfMjxbSMPJhNt0Eplc5at1CdBDH64IcwwFw11ty6Kv6UBXHj3qfX7I3D2dHxJHgcOdjsb467hzwzESQo4XLFkQA6VZA1Rd6r116-xbrRa8Sf8Is9dWsdAFzbQOt8nzStiqNBmrENnwqGoBDrSlY-VbntO0RLg3clXdC2lIv68VjFneEcRhIfZKua02u8REA7JJOAkppRkSkHNy2g80fSMcb_aeTpi7cj9ismToRo8IeyD5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه تک دیدار دوستانه مهم روز گذشته + برنامه مهم ترین دیدار های دوستانه امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23092" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=lzCL2HSyHeLgbUV2oBbxfX3HkHHSOjxm1eoI6Xn0jP00W5G6VF6H4Ydlkez5Mac5OdicAwauz2XXYH6Onttsk8FEWm8hHdLZmMmWhQg6cSLgVWbGBcUxKZPjnaN-k6HulFuffdg0gcuxfL6R99gO0fWvrj69L13FjHp3v2IQo1Lz4wfjd4DjE0WUejmEcy4bSi23L7E7bQqXqajVBH-3K52gQQYFmhTsUilw3tpxsfYsX1viVK1M-AqGPxxcw_QwZuePG_6TQDO82r748TSA3mv0-t9Jo-P_ST8BSDjnxGSm-rhqoN7BmmcxV03-JI4CWyQpPl0VLuyVPruycF8HJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=lzCL2HSyHeLgbUV2oBbxfX3HkHHSOjxm1eoI6Xn0jP00W5G6VF6H4Ydlkez5Mac5OdicAwauz2XXYH6Onttsk8FEWm8hHdLZmMmWhQg6cSLgVWbGBcUxKZPjnaN-k6HulFuffdg0gcuxfL6R99gO0fWvrj69L13FjHp3v2IQo1Lz4wfjd4DjE0WUejmEcy4bSi23L7E7bQqXqajVBH-3K52gQQYFmhTsUilw3tpxsfYsX1viVK1M-AqGPxxcw_QwZuePG_6TQDO82r748TSA3mv0-t9Jo-P_ST8BSDjnxGSm-rhqoN7BmmcxV03-JI4CWyQpPl0VLuyVPruycF8HJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23091" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLN9giNZlPJ-7tTMKW6QPFiyZantgmxUmfxt76iHOWX5ZGJgx41S4AAIMRHbsZjTVj7aBpkoHFdP5R5eX2aTlG8g2skVs0fHksaGK04H_eP0K0QOnlzcg3m-Wmic_Xjm1Scvq9aLEZfe9ZHhuIH-7bI1HfN63tx55JBRrVKuykjEqmt0G1ZtWFW9GK6hMpVQd2f8S7l3AZOSC88cnc7uFsl_t4Fx06t6VWaoA3ztKY-BM-0grJGdrGMJDugFHBrMZvPJ1QaNmBR3pcDC0kl084SL0jVK8eVcjJiVBEuVxq2Ua3ybrcRzZngaFyL3YM79xctWBGpCxoY9HZMNIMz7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHttvgeVAx_XD4-fX_Zvgm2KydKfeWRu8sFYQ5NJ6ePSqogG5e-6O0OGSog5EuS1R8AoUzHRa11QcVL6_2aqEGyooXyQxPa3kPqgCFEDrfMhu965hUKBo9s-WxT4rgzS0y7Tnd9s8AIykxsHN6Jeuzjr_DtDzw6xU4lehrAmy3sC5GjFKkJAbyIj8Qe5r4Fy1xfzwsISJEe_yfmTDu7VrDfFqXRxNpKco2PV4r1sQjbTZh6NV53U-qWBzrD-aPIWf1D5yclEENtgu-OuMdIThDmS3V08gMFBan36LG9CCkJKBdTnp8PutGnKkx8B4pzDpcUszUQFdQ2eZywt8s01cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌باشگاه‌های‌برتر لیگ قهرمانان آسیا بر اساس آخرین امتیازات کسب شده در 10 سال اخیر + پر افتخار ترین‌ تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23089" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crrIqVjuiZ-fBQoWR5DcAqjuFPYwova6AEi6Wn3_ylVnTPZeCwyIp9erjhcnDAvTkCt_XGcWRcEWtmbEe7mjYin-gZYgVdRL4LDgPNoSHMdxv2_YpYxCeTs5Y4NS0ViscWNhvQNUxxqjaUyCMF3uOxGwUnFYOB55YYvCDl3wjjTYkNFrdptiWPYopPzZ-HS_5DL6EH2d3bXx3GdaFqSbW3T7QYhPgJX1t65bKPsfZBkjNztNBOPClqiuCbbYjHXeu8txJLhAdQuil8AMYkmD5Eqq9hJACoVbtcIrsZX_skcgW3fLUePCxvZPEzxlDnYwg76kLBs0Vvhga1FNxfMMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23088" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5366993444.mp4?token=VqWl0r3RopsSttb6jxGJQfBx52oFgokoepp0WIp2mx8_3b8w59es3EDaOGhG02EfQ-UlSpFTzwSiYyAxj-jZ17QaHBEY7iCafAW401whxpevBiTL7GXv0WmVv8we1NHY_dOmkRhvFlOy2IbN0dZzcYLCiLy0k3apZx9c9G3PrRT8kgT4a6opNCWaxqrTDCjecwxbu5bG0Az4VF2oXRBogielrym0znUe_iakmzj1Iy8aFmsFBFiiWtRP1TzI051vbSEB1yzPT-Q7ZhBYtJGdMyLw8NFFMIgzfaMlpyAuA4AZzv-QxmAmjC6P1H8GHRawyPPf28VUiLOvKxIFGk23iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5366993444.mp4?token=VqWl0r3RopsSttb6jxGJQfBx52oFgokoepp0WIp2mx8_3b8w59es3EDaOGhG02EfQ-UlSpFTzwSiYyAxj-jZ17QaHBEY7iCafAW401whxpevBiTL7GXv0WmVv8we1NHY_dOmkRhvFlOy2IbN0dZzcYLCiLy0k3apZx9c9G3PrRT8kgT4a6opNCWaxqrTDCjecwxbu5bG0Az4VF2oXRBogielrym0znUe_iakmzj1Iy8aFmsFBFiiWtRP1TzI051vbSEB1yzPT-Q7ZhBYtJGdMyLw8NFFMIgzfaMlpyAuA4AZzv-QxmAmjC6P1H8GHRawyPPf28VUiLOvKxIFGk23iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
جام‌جهانی‌داره شروع میشه اما همچنان با بزرگ‌ ترین غایب رقابت‌ ها؛ تیم‌ ایتالیا با شکست در مرحله پلی‌‌آف مقدماتی جام‌جهانی ۲۰۲۶، برای سومین دوره متوالی حذف شد و در این تورنمنت حضور نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23087" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRAkbwGBlbCvkMkjZUjY-XENbv_Xd4oQVapwQeBtOSGGcP2dBsvr7go5OkCOp97zHeiKc82ri2o6OZ8WlSWZCQaeCTd0eNwYDI6ZM2Ks1at4_xtB3hlf9FKuvwKxha49PkUU1C-YeXIqoi2pkaHZ3TvnEgAU2fGwZAjmvEmBq75lr6faHynQevTnxqq8xmzLP7AJFg6qpKJR-S0yads0E1dHjCFGwTXmjoByo_VjlQQvIq5iOd-xhIFcZFlEcmnlATZqeHWtXjIvtBi7sC7gDE7ZzzC5g8BGr7aMKOv3MPl4NcjEHq9Vk4-lZYdVtTudlTDvwrL-t8yjpHPfz2xJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصطفی پوردهقان، نماینده مجلس: بعد از رفع فیلتر شدن واتساپ و یوتیوب؛ ما سراغ سایر پلتفرم های فضای مجازی خواهیم رفت. رفع فیلتر شدن اینستاگرام و تلگرام نیز جز برنامه های مجلسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23085" target="_blank">📅 00:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXfnKSYb6TLa7G2VMWE_VePuSPe6kApI67-z2uIxCqsQFLlQGS6-uMIDMswjY6Nh_i-rSJ0Rs-ryvZLuYm20qLky4w5J26emytW9hUYjjk92hqdWe4Os3t-k1vrRLCO5WeSx4rQZK32SSv_yfkG4q0WlygMdhIXEHnes1oVsK8yxeCi7UmpkrFpXRbBIl-PsR-FEvoU3Y5h2qlSd6mVqUcTqtJxB66ZQ8qIH_ODBt3hHfl4iTE-zjMlXjZYCASA8h-giHJSvMTlbPIExcuatJ8LYj9aRHTpByuUDPI7kweL9rMMGauqwT9SQJWZo6E8YJ6Ecp6GZ7uWQr17tDbTBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
🤩
#تکمیلی؛ نشریه کوپه: پرونده پیوستن خولیان الوارز به رئال‌مادرید بعداز رد شدن آفر 150 میلیون‌یورویی کهکشانی‌ها توسط اتلتیکو بسته شد. حالا بارسا مصمم‌تر از همیشه به دنبال جذب آلوارزه. الوارز بارها به مدیران باشگاه اتلتیکو مادرید اعلام کرده علاقه‌ای به ماندن…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23084" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvkJzZaJZQ2iHToamiTGgGLINOHFoyp6rozPqJI1QRCgntG0KPdn2kLotgtuVL4u2GuaSW6-U3eg8s9EPssgH58DwA2hvUWBeEOZAH_I91Rq9y9Ny6xQKQkYqq9yBr3FZinjDJY9B6M_-DDH-N1fQxG5uQkzYeNW06g4j0Uy_qTgLfnJH7fC4claJTOoxCEeHugyzmeaV0fOcBZuOXxdBbw2OB010KzCVn_eCe6_hO9Alth13vh2yhPAJ6tjgKqvxREWB6x5ElCqSVhZ-_5Q_w8Nl7QS37WD-TfuhlCO1EBppHgSWE_2QwRpQnR5Lm_Vz8G3-NbbdrM20iwKX7e0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBd7-8k1VOw-yoCz8uPFt1JrpUsYlaWWMVDqXp80dGnE9gACVz8xGYmyBAu6RTLNVhGqVWkq8FVWHGssTzuSLCNgK16R-RBtg3WogtNMqhO_jUnOX891qg0oTVSArv3uBUH4dzM9koK3OoT41h6h8U-w66zpsyEfqhCtwI8R_ZMRMPFozuucKjAIie2thQPd1xx8D1-2di5_TZdjZFYz5VxAERvHtGlVbN5G0EePeboCed9NohWc_NNSEFUiGiG3s6x72uuC2Nyn4huVcRwvR4rX6QFXROxRNo9el_7-OeHtBKW0a4MU_a_Y4YsYb6rNwAjqAxm34zJctMhIC7EWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRkwafyJO_EGhosEDHwd8XWdEkZWNfFZc3MpQmumQaXJ5wfli1eIWxK1WO9o8aaxDcUhku8iVBLK-lAkZxN8KyvBptfpjbcPc1RtKohWU-cKY-x6iBvr7u0KjBbc9Tt14RJVZW33kXfvHNBvxpby2mAqmKllK34IbtPxOiVs8d__Khsz2inkc7A_Ksas_yHE8plADm3CAGb482RaLc9qXb5OJ2IBXtnJWDs26koIRvTUc-5S0bK0yrxdOc-LsSPYUNhRR2TXf4xK0Dn4_0kUyn5ApVCl3UMbxOn8k_JWPyWHCigDzechEaPKWLtDfHx2DdbJjK14VlfvkYi7nM0GDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7ePe9whqYoShbpB0G-eWd6dcpgCo6rY-QnOXaOlqV6vVaKqN8WRjJCb4jsbBl_OsfGHRaH9cOjykc0Hl9K3q5CZ2OIDrI2Xf25s0Rzp-Ja_ZGXYlUgDXR6nHpRyOMoGixIa6g1h0s9FyKela-MQSLayxinbVLWaYTCdblzhA1-_arzS7C_RFdW9iuYUQ0pjS72CsA-KGMo_YViLf-BdXF-YEHXbAqJYx4s0TBxYT6qDGdV7f4JZJxAoFJvBVouoLwddsp4PyWx-NGqWJNyYznGffq9-56ileSAQfDdN23zBl-FzEHPB9upZCPa0paJkFwuc3iEnKoAbIeQsc00DMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHZAaBU8GOgTnuv3jQ90Ddiku8lUfJNZlqUfNW5TR38kg9QGXZX1q3b-LIFJ_w8MPYvDnQo91gztO538oO5EZ12Hj8lJjB-ED__o_LhTS_fRbZfu8YoNls9Oh6bmbE-6GivoXH7FafVK4HAIZepSph_NhfpYYBMKk1snXzB7-DG_q9TAUZlVqe42xTLbubcJnYpqU20WOva9RbtPY6U_WgWdZUuuJwO3AQAVIubCh3gFenAob8ka-RQkqjBNRoUvbVYSUfjifgUC3em7VvTDUc02Che79TYXsCoddnARhvksiV3aokIMrhv4i2f5kNAxV5-Oi69WQGo4koc650dMQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
نادیا خمز دختر پاکو خمز اسپانیایی: علی رغم‌علاقه‌ام به تیم‌ملی‌اسپانیا؛ اما بخاطر اینکه کریس رونالدو رو به شدت دوست دارم امیدوارم پرتغال قهرمان جام جهانی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1MwaUGNtsqxXwPLgSWunjb_xQRbJJ5DBrRjtURwbzERiVRk1N2Z02gx3Mii_Mt7gXkERz963YFLIQTGx-dxJUpefWD-7K-KIpw-r_w4U0IQbHB9dczDy7vApWY40ukxZr8aqE5jmHxurDwzE3YvGriXPvWubgtjr46YXYDUut5DIuVCoUyOiwkJOQB2erT1JkRCRLcIl_QD2GX3zuZ-VDzzZeaXiybdAtDJ9Qgj3J8zLgwhH_nR_HO96xYaIPxyNJu6xEeUmpmcxyiwZPIlj4KZTudif4snGWi5gAaQnForuLXflwEWdjMC17IpUHn6eWh_bBx1--cz2Fh4Bj7l2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLrimvKG4VO33yAYmSEYCmmPmQFdYYEOYepS8Q1_gGqFcnLijgx5ofsoUFv0Os3mYgVmI1PRZSLyS10TdAs-frG_GET0bXovNGxGeDT6SwfENf4uzA3XUGf-m9PwAiWqfp15kUmeiWzL1D7CsRmF2Uj7MxaqOIWCMpUi-NOxv7w-yFXRYqnMCJt7qZ1IZcDnAgmucHF8fyXsMt8r0JGgMl-VD2MNuD1YE98sDqKrEsggWiMvp_5_1-lUUZNdyUDIOFRGw9wQw7s_lBxedgwmjT8bp4-MZo1NYvb-Wo9l36Kg2uel2RkXWbSLo3wisUGCdQDt0Q1mu92Mo8I64nWhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cg3Li9gWSc14WaKUS8mJvKiLuiZSGyXMcVVosxZT7s6XgL5paTJgnF0AW3PsvM647F2xvxhStt2FALkcP16jEDGG9aDhCCjTN0VYJ6urSRhRJFuWY8GAxv3rLOGjG48s_OYwr0pbGk8lrsmlUdXGdqDN7l674DKUyeG3vbCmMGleWA-ka9oTANOfjumS7N9-x0r5xmcBikOriN_CwWGQHY2ZHppWkaS85wBgiejdbuWnMUCzYZ374e8ANPnuBGzQiC-NYbGHOigTK-FUaB9zAKE6PWJBzd5JicmBIE0WcjtBXd0Lk6cTZ4dGxBY-5f7oED0gl0sMBjGd6hVkhoKwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jViM-pbeyDNY7eTvjJVsrjsjUiRrkN-nWiqAPY-wuHLJSz-8l2uWy0lHA2DMfkhEnTQNHOqCzY4uxJoHZjifNshywAU7MQ1zZVou-9jLe8RZMuIT3eWQbrsOQy9bgVYN1Cq8VDMjMIc6JNW4zLf9Ta1KPXPfasotph_9jl096FJgRk6jq-VEZUfQN_JfyL7FZzM0pKoeW_KLazftVhOqiD-ESJKhlvj6Td_7xS0rWSHEcKId7261fDPEE2ddwvAfwNHY_1-uU01dplbAFiOKajh8EVunjF4odqtvwS59oT_b3Thl7YUbMNtbgsSPX7g7IlAe8chN7CXRMpqJPFVdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKpn5aL8VYHpvwKZA06lfcAGpajTnQnsxsOoYItlyPHkN7ppmrgn6kwRzO5XawHlzITf895nvLSpeeWmtWfUM2TjAZP871vADGvhmVPpFTUtX2UbfBArdQNZqTZYCYORC4L_VRtxtYzbQ9dZ1rDC5O_eKsSB_CkjwfuXLOEHrf6iW0jNnoZK6xWzIbaNe-868KkZ6WCZ6xtlwmTFUFjgEhuuwRvB0eQUA2ZtOpyPfXSJrd4Zqi5Llrv-OyimlKzxEcrlfHw6gO7oetlJrM0Da61n4QBawLjfrr9M7Rgr6hJWnjfRBkQZn5eYf4M0WxcOm3DKnrtrknxvjcFtKebXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvVIXJb_ttESclCOeg_1C0KhWYECgwf7NetMmge1HJpagLSsVIDXOu9ARTZkUT0G72n3DC5Rbs1kZVwuIyfg1G2_jXyiX7vL54ll7ojyseQ-wob33y-ex482J29Yxb1g8Yz3_ueiZUvlUyChGpnEnH1FSBjcAbIt1iEEqFykvqt5CgFKjUNsUiVBhz3ie2YqcCY_dK6ilWv9nHa1nNeFtrItyM7U6kslFkgGyVWHW0cJ87rRfv_IUazkOOEdCaxgKSYsZNqtdROQngBKz-eHcGSkRc00NoEMjkrnJFGDltefJVUFqGGf-U-G9UJ0L-oqDmlzwgowbRJEi2i01MIWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=jcIeplh7PrEu7FZBhNdg4FS6v_y_BkkY7Nciyk1MZCbwqDqchFVGhlAFV9EEHn5nzyqg-KiYbEz3yF7yijcWcZWQn9QCeGn9zipwpkhSXSswGNxDnr33PBUvAG9CltxvL-8kHCN1XruzguAMV8ajlY1zO8C_5mApD1snucjShpJdZLYPVWBHMiBxCbwQ6Gn_A7cwRLpBeYfcG8FAb9kHgvKovV5oO-dAZhXuHQruirW8j1JsW-6mgQoJjqQwEL0KVFJ-erkjavoJXWZOUW4KpXtCh0supQB2Ec1ttrP2xTYWBsUI0Q8uExh_jQs2wYDZTE8GpGgFirRaxKtFGgQh6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=jcIeplh7PrEu7FZBhNdg4FS6v_y_BkkY7Nciyk1MZCbwqDqchFVGhlAFV9EEHn5nzyqg-KiYbEz3yF7yijcWcZWQn9QCeGn9zipwpkhSXSswGNxDnr33PBUvAG9CltxvL-8kHCN1XruzguAMV8ajlY1zO8C_5mApD1snucjShpJdZLYPVWBHMiBxCbwQ6Gn_A7cwRLpBeYfcG8FAb9kHgvKovV5oO-dAZhXuHQruirW8j1JsW-6mgQoJjqQwEL0KVFJ-erkjavoJXWZOUW4KpXtCh0supQB2Ec1ttrP2xTYWBsUI0Q8uExh_jQs2wYDZTE8GpGgFirRaxKtFGgQh6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سوپرگل استثنایی کریس رونالدو به الخلیج بعنوان بهترین‌گل‌این‌فصل لیگ‌عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTGiIQ9GfVqOEn3jvgM-anlcE96hLTDunM-E2TaWMb09tBsZ8jgghZmjDIQKIWyiivKfP2JqTvnZ8Cto-4B6_keWg-quEA3H9o94krcR3X7j6fyp3tnI30-kCbI_kgaXV2CWJtO-BfTjXBht6aEa4jVXgRnILn4V3njubTI8WJU-55Il4FFlGJoOFajcsxdVyMUzBNZ9fn8-MWzL5MfJ7_ViV8WWmYTkGluncNejiQ-ugCVb59WV5JbIlXFCAXK934B84KP7QizbvSDA8-JDQ4KHxPsC-5syqr4Ekco1xqK0RJWSAeReUaPU6Vq4kwD8Z8E7foWqKq1apuV4U-LFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=UJSuxxThkl2UZQfiiD02m7bO9z0EaAUmDZpI8sSsKbTb6Q-h7yu73GPz0HzLZq8hbDWZnJbum9DRd83rBINPg8s2-kU3I3itG_kHV4N2nQHWcsO_ZejLBXcv22SZvp9QJLLGLjmnx8yPSKddjQfNFkN56pwkBEYuRqBUGOEER7OilcYEjvfQva4XVVmcwW-jkWocyM9qrTfTXXbFmtNxCLxnQvtoPRcCgc6y7_2MDp_vVU1KB28HE2WIJnmtlzs4GDKK6yW_09CJk-PjBQnhc_jAlAYVSvALSJ7KlXivlFubjZSOWEN7IiMbYkJskiYA-kojOiT2jWINrzPZ5wQcoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=UJSuxxThkl2UZQfiiD02m7bO9z0EaAUmDZpI8sSsKbTb6Q-h7yu73GPz0HzLZq8hbDWZnJbum9DRd83rBINPg8s2-kU3I3itG_kHV4N2nQHWcsO_ZejLBXcv22SZvp9QJLLGLjmnx8yPSKddjQfNFkN56pwkBEYuRqBUGOEER7OilcYEjvfQva4XVVmcwW-jkWocyM9qrTfTXXbFmtNxCLxnQvtoPRcCgc6y7_2MDp_vVU1KB28HE2WIJnmtlzs4GDKK6yW_09CJk-PjBQnhc_jAlAYVSvALSJ7KlXivlFubjZSOWEN7IiMbYkJskiYA-kojOiT2jWINrzPZ5wQcoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPiKYhttDqe-DgUrmLEZfWceSIwBELepDIUMKYl_0rtd4s8EwlblP5lz1gRn6PfriVtHb2rMLokrHKSHeCjYZYKCvHvExmN6xibiqakniO7Uob54QNgN7C48d9ZmIK40kP4yJodlYiVVHMNftENXvGRQTLomU-qIre5YwZ5U9vI5XuLXE-e1PRD1BcPCq2o_D4kW1XsLjAAphSz_fvJnWGI9ynnEaa8YessmGn8Mm-jhukT53d_zgdbuiBPhk5GeE6pG77pNreUnwNxmN0M3gJxUuA_rDpU1T13ro5v4VgIvWcPHJ1W-l6NKANqI_pA-NAKJupohjhhhOlVArDEe5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2KBOzJ3kSNb2pMVi0kzLYe8SUMq32VYC5AMQMb2sdKG_Wx189TlYuVLU5x0_Dcr5fyIVr02OP319-7CRZYYITnxYGd7uV-MamWKwGsH7KRnwJVFDOiA_xv0TEB3MMJiwE6vyyfX0atb0Qsi7TGqBsqReD1bq28g2SHVbkVDh_SSWML2mXfEDuIcIQQ7teu0pQm_GkuUnV_58NcoSB5jzsfOey3yBQCuxUiE_zBLPinQx3OQuXuCwUKfEAlXpjIWq_p_-1fcxgw2a1J9tyVcHyGoqPApUdoDjOWt5cTkLaHva_VAnYj6gfGyPJAYOvuwPgkSseQbhQt4cMuRR0vMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzHf75zPBDjXap3rH-EtJOLibEHOKXnnZtfB5r9OO7mYUA3tjJf1cLGEGyitiC01ukGRud8-hFGZotsjSJNll6vhMxh6E4z_dqyQzwV0QNC8i4F4ldBXLK26meAOnleurfUZ8qvzR6cyD4pCRg0ODMwfASOo6AXFKGdKtesQg_p_G2w_17ELqYcfZeUQcWs2zl-glXstBuLqpRxQqlLi4LnKxACQ6vomZqtAlIjwZwkq7hcFiMrswYHV-gI5DDf2yWlrGPXBfMbOvdVa6EJ1Gq1fEA3g80lxmRSP0nJE-Qr22d9UXvG5ckhqSXxCbcyIKpf2ruS_rkp_SAnbU4PaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUMUvsF7pKua2SQMByS7BU3wjba2GVODzeZRmjhKnnTKNi-EcsgxKNHy8uW8gF2qoEEDvxwdngo6dSqqPOYA2A2uCPveV6ZJjjvyX19hA_g8xyHYJ-NU62tuhBzOVQhh3b7s1tJp4afVQW4XR7SUfGV--6Ez4LlUebTYZn41hi6xOZwdCFOQNXrdsO9c6IXS4FQnlNYcVCZpDQEvEVaYHO0qJN5WJ3nKnukMq1NC8Uohsvv820Js414lKdb1jYlnwivNyoJ7GWQSDa_M6WXQgArgAF3ZuuRNitXBukGwEb7qeCsggGc4uBeSNwLP8FZKM2wO8QDnLi_NrmLwgYtpqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1AAlInz9UMpJe4fIQTLrN6o-_sXKZJ1kufTe7Cv5fB0yR4zIW9kgFTNfevUBm77TlNYeeFHQDFmc4Qc-Pw9-4NU5H09-RSmPKMO9UjRZPCltRG5w8qhw1JTQ3oaU9Mbzj-wrWDrczHam4jbvvBj8n9WM_LtihWN1FDggYdHJmTPlwcRbayG0cgZKvvyzzPI4wR2gxdixBeATlKGVNupWOE1CnR9QU8v_J9zAehwh4bTf1Y_7LdiXVMDcxZuTuUwyCpZzB9ZoAED5mu_MRyshHsz8mEdNDh57_UtUe0VOgY5p-Za2upFx0V9PWZfTs3dRCJXW0eF-z98wOfME06obw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miJKaL-UjAYNbG2pF1tofhsGbDvd3owWu1ZkHjEPkdMZXA2EBVVPMg1LLYd3A4obYvMR6TjH73A1I251Nx5PK_mJb6d1-I87hd9T0pQ58WZ4-MtoSKDEkfcf44eACUqryyVJPINqZdUafxB-32MtCuXYlISgO_Njc0FSPWGcMgMfN9hMbKz1YPIUQoGTVwEmuYZIYNW77MS_-P7_2YKn33SATYdLI4PkTrM6vPqDhWqY_ro8ADotaB41hl2a9UswGfv8f_ZnzczMiC1s2WZSu6jv9uI59A-aSvyNqk5i7t6Q_Ir3Je7SRJA90M1tP6BCAU6ErymqN6MViBD-eVtRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=GkxUAFsXaSMEYfaRA5oEG4mjrMRVODUPUg5xGznMv2lzNzrvciOzUskoD5tjcNoEzDKntnv-fU88I5h-_pDg1J-NWfmT5CZi-yz0WxE4t5Kmykqx5gu1lbN-MMTPNvCSv9_STJstTKaWywNjfvfp0ENFxhsfticdag-sZIi85Rx-Q9WEtGogMmQ-HG1krXYHLeQxFtz2sLaeTYix0DOkXpcCRv4STrMcEtS5iG83Q1ZC_V4jqS21Ir224svW3K1fhrO4FDZtrghvIMO-9aSbT26UhREFSdS2WGPtb7D_1LpfvC7_XCY8JZksC9NT_rOdldd7AXMAOFu1rQ2db5lolA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=GkxUAFsXaSMEYfaRA5oEG4mjrMRVODUPUg5xGznMv2lzNzrvciOzUskoD5tjcNoEzDKntnv-fU88I5h-_pDg1J-NWfmT5CZi-yz0WxE4t5Kmykqx5gu1lbN-MMTPNvCSv9_STJstTKaWywNjfvfp0ENFxhsfticdag-sZIi85Rx-Q9WEtGogMmQ-HG1krXYHLeQxFtz2sLaeTYix0DOkXpcCRv4STrMcEtS5iG83Q1ZC_V4jqS21Ir224svW3K1fhrO4FDZtrghvIMO-9aSbT26UhREFSdS2WGPtb7D_1LpfvC7_XCY8JZksC9NT_rOdldd7AXMAOFu1rQ2db5lolA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSORRH1lyuCxwbzH2oHZBd7czMJJnjF47J7O3ii1pHZdWMJDQiIQecv9-ycZArvq3s2nCTXYb59vBV3n0H1fYYbFhz6a6mq7F2ySBFpreCYoiLu37AtxXfGW0qFUyXW9gFYZ8rzqlHoRjnTrS-T5aTbitgdAgrSX8U8HuXiIoVXzNdF3X6_GNIFH7srXey_Jqrpd-Yw0ICNUzCR68vrS-_ZCzQ8VcTqwm_PM71Uk-bewhNiNGrp1nZ-G0Uvr9nVeCBE5gpHGJeU2QrXut2L_KyaJV_sxpNBpw4rsDD9O0XHUCILyKQmedQVRhBCgHVgmoMT2LKROCXjP71cokjWcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UB3i-JIzZeyuWSnPbK-_kJbTh4wQo_tF0h0ncXTkOmQAy1h5KoB_lWPeEltKWjqP5OFBE-SdmG61xN03Z8NeISxIFKA2K7M9E48VQlcULXrJUjgwfdtG8eUTELS8oQE-MYvpLzJrh-EioFAKNa1MXyYX_9RBRoGbliLTfz1XPUK615FIdb5rvY0QBcibLiC9aBry3lRVQh6cFZwDASYgx2IL4kQ094YgWLRO9rqG2n3_jx5k27gjI7OJuEXaaCnw7XB90IdA0mggryAU3ca7338Rl949iozoMSgiYYKe81n-t9RyS7suWsdGkefx_GuxUvxe6PYvHIFHC39OcRkq_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6haE5Zve2Gr_bFAHHg82AkgbCO8db-hIvIwFrh-vFSIkAMh7eloyLS9mYzMrmKazZlrDwWHYhOtuHmU18VHrvAUn8LWVgvcaiKjUteJejiSNkKLtOem8ApvGfeaoXJIaRaa44lq3agJ7z1Q7CZpmt94-NcxpwGYto8FMZwP1nocgPZcD-WwupovW1pReqOSx30GbVcCCIQOln79iK8vAHLvLgKqgQ3by10JYbmBsrFAuNXX34DPV_30nM3EwOMAfoaKwRxcdgtP7p9xAsgLERn98-a-RzfGqUEaCbeeOyLu6gxaPR5Cn753kudogMpy2pWCSmb534F8J6GYAFghnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZF8hdpO6T-ZGFmQjXqfGnKseFL3_W8sYGTL3Ei83Yei-lexmLNjELQdrJxDmbjb5fLbQXRDDCXu4gbeaG5HQgu0ooXL0-E7LJ8LTBBEkm1n01VX_D6fvWt1JQnsDjKpH09V1410spwul41EIe6MFJj5mLZrdB3jcNW2DjA00foBjVgjAmJEFYJgAs7uVJZYrbkLGuCmb2GKpA9M7lhpuZkZHCKkoYgla2KvsPPq_fUuo1SmWLR0H7Scc3KIy-gx2MAnAG5iVWplJkLHMPPAM1n4Kpmp1oRLSJxRXzK7HCTswASegP4rWiBZ61wboacS6l9g2WGIazvlGmPmbcSFmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjmDJfDAmkOQsT4wi1QyEMxhAn8gYhKYXjKGH1f_fKKi06wmprH1oKoqZBzN8Fc92sLBIcY6V5LRMvvw-mQVs2HOnSAsN7ehNDEYF75lVAut-6IfJJ_t04zPNq0DDTp97tETdf5ye6d4rughXtIzak9K8p1dD4q-12MscRWtK-j4QxOb130XNI3sn-dU9_nQDXewVJy6PbWYwR0JFYkgzHpzGt8QczBdPfREsUmtTjgrwmaNk0UxgZdP7OGdEFcuHn5pTCjFUO_FkIHyo-mYK4W5cG46cR-ImsjLjWACBkiiJi4SoaPYHtZ67j1hROpl9kopYTFm0r_eICI6IAGhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er5zEZ9z9PJN_LbmNdJ8aGhmwG5091TXGb4_K8aqM6KwvmRwkvD4kMkKf8XwkUP18-69Q7Lg8RgFZwjQ0AyYrGU2mTtvFTPmQKLpn3wo6A1YhuDqR1UVEfTyxnOSOeaoUKFqdc8xAvNLGJqd1uoB5o0ImKlExpE3zICUj57IOXu_VSs2vkj6FlN4qjMUpVY19emNSl2RcIteykzkIAlVhZGJi4RnMIulczlaYq_n1r9yV9FUlSdUpfyFf61v2pVwj9ogEbJKh7jN4DLuQZabDnt2pKF4AXAXJwrJoXG6qmc7fGmQo1_ErRXXvHbaLcnacJUqBO9SEIkUG9dzsQwLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYnNMUv8A0iszMjQBI4E-mBWe5HvTQ8X7c9M5SztcCJyM0zW258Dkv77rcwvGoloPLapPh_dIVQFHOVBG3qPPor6mFINB7TFXMSG7f3Fwgwe4nQ5gP-Hvrp4LjbAM2svjvU3pVVkP3WkRfVK3y5p-Yc_MfSZLuCvp6wzEu8VCsbILdV-y8pPCpw_7KNQ3uVdwARw-vS8FY-7nXJ0TUEMKel71ss8cyFO9NC89hTGGi1cX-r6HikpUxEU_Phq7zALyUHFqpuVm-7f0HrHibSixg25IWeG5uqVVBLoEuFJwse4HzYDRV-6fbVe3OWKGP0K_tw1s-R01LYvyiG2TO1DEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=EGaYQlkn0TjVKeYhiDLSGluOXGUGTQqjmn7oIw7oPhjvzHD6IzJfBNma_Y5tYFcjc-01e2nK5kRpzPIutg650jWNI_Id8yEij53ouTvillGA04ww_96xRiwqnM0P215UQK7c4fVlteyA9wLZhPKR0eCajKgLtY18TbUSKP8kdH7M91AASBOMN3vHXzhrDn0aAmrGnI7KdG_KzDXlKRojkPcuTn0m6JD9SwP3kFf2YmLAG-fYSgR6u9I6E2gfmHS7Nf65cblGQOfCwInXWMiMVZTfVzEi6bhlly1hYUTL37vu6LT52I7qjI0Pi70DoPsZmm4zLKrm0T-GHNrGgL2cULkA2QCQjQ24g6kmiRl0M2hxODFdprqCLnSyW6Dfo8RAVGjOWd1g6kpVzd27H90xMpChcCW0PGeQ15icVwa_4swDq-6ORNi_oc1nbkFV5GqOC9k4dam3_8LLjABuOKEac5h0qvi4Tgo3WGMGmMiWzqtSuQQbN0gkvBFrO_iwTTdmN51HOvYkKapfaWd-u2TbPpdAb_HZEe3l7CFPCJgDKGAU6RghakX3kB5asI08bGUqzuAutmvyIHg2yfEfTY065xzTJu-NO2QTunxjpthCiC88nir0iqEyH6fCjNYjcGyLm1_ZMIyCWRBQn7z639dO65ThnNEBtyYvCgTAQN8OKrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=EGaYQlkn0TjVKeYhiDLSGluOXGUGTQqjmn7oIw7oPhjvzHD6IzJfBNma_Y5tYFcjc-01e2nK5kRpzPIutg650jWNI_Id8yEij53ouTvillGA04ww_96xRiwqnM0P215UQK7c4fVlteyA9wLZhPKR0eCajKgLtY18TbUSKP8kdH7M91AASBOMN3vHXzhrDn0aAmrGnI7KdG_KzDXlKRojkPcuTn0m6JD9SwP3kFf2YmLAG-fYSgR6u9I6E2gfmHS7Nf65cblGQOfCwInXWMiMVZTfVzEi6bhlly1hYUTL37vu6LT52I7qjI0Pi70DoPsZmm4zLKrm0T-GHNrGgL2cULkA2QCQjQ24g6kmiRl0M2hxODFdprqCLnSyW6Dfo8RAVGjOWd1g6kpVzd27H90xMpChcCW0PGeQ15icVwa_4swDq-6ORNi_oc1nbkFV5GqOC9k4dam3_8LLjABuOKEac5h0qvi4Tgo3WGMGmMiWzqtSuQQbN0gkvBFrO_iwTTdmN51HOvYkKapfaWd-u2TbPpdAb_HZEe3l7CFPCJgDKGAU6RghakX3kB5asI08bGUqzuAutmvyIHg2yfEfTY065xzTJu-NO2QTunxjpthCiC88nir0iqEyH6fCjNYjcGyLm1_ZMIyCWRBQn7z639dO65ThnNEBtyYvCgTAQN8OKrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOKG6bGVNnVtllbd9xodlQTC5OwpuX4SYDFewjFrpdhxcmf0z19VjmZRnTQJ5-1CYgvGvi0GEMY-DAPlSHtgVH_kb3bqerwUhlCfldaacLu8rRf4MbKsW4K3XOk5Z6ywZCsPz-fmx7yt6dLimITwk4JAvwR3cPKdiBcZO__UKWzj_n0B1i6m3nfoF_hwJoJMVrNVRbRKFWhx41Rg-P276Dj9Z-anEqfg1aV8XR5IwPvfPlmmIuBG_NXfTPvdsTWKZ7Vac-AZEznKLJ-QLqwM5Ld1xpO19AvfxKb2sHYIvRwuK1foTJmDf0WGfV7_cefYsAcKHknsRwEU2U3BGAiTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=fD5RTXT6TW1JyE-LhBJb9oHa4Ln_FqO0y6zzIDWhUCwYRDQqHAsPZzYesRpK4-sqh8vf-tnPOstCe3IIcqB9fVH9UhKnZkaO8MdEHQqSvdPtB0X9e44dglV4_VBZd5yXTAJsODO3OCGocwznW0X3G8Loe_D4qQ4p64bqBEAjSkozZDX2f8RixmoQxNpnNJcYNIkVLPmPSU1lg1okpXO8ygt61JF0n5xsMrHJ6mWTwT_NOEF14Awp1v9g31JXQeukeIJacU--I_sTXXlGHe84ynUAshDPQA5C0mDSRO6eFs_jZG65vWVZ_Q8Z7pkSugkrfwkyTR-9pbN3i9yT9Wm_oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=fD5RTXT6TW1JyE-LhBJb9oHa4Ln_FqO0y6zzIDWhUCwYRDQqHAsPZzYesRpK4-sqh8vf-tnPOstCe3IIcqB9fVH9UhKnZkaO8MdEHQqSvdPtB0X9e44dglV4_VBZd5yXTAJsODO3OCGocwznW0X3G8Loe_D4qQ4p64bqBEAjSkozZDX2f8RixmoQxNpnNJcYNIkVLPmPSU1lg1okpXO8ygt61JF0n5xsMrHJ6mWTwT_NOEF14Awp1v9g31JXQeukeIJacU--I_sTXXlGHe84ynUAshDPQA5C0mDSRO6eFs_jZG65vWVZ_Q8Z7pkSugkrfwkyTR-9pbN3i9yT9Wm_oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
تیم برزیل در جام جهانی ۲۰۲۶ با هدایت کارلو آنچلوتی و باترکیبی‌ازستارگان‌باسابقه و جوان، فقط با هدف پایان دادن به انتظار ۲۴ ساله برای ششمین قهرمانی‌جهان‌واردمسابقات شده. اندریک قبل از آغاز ماجراجویی‌هاش در اروپا، تمام دوران رشد و شهرت اولیه‌شو درکشور برزیل و بویژه در باشگاه پالمیراس سپری کرد. اون با درخشش در فوتبال برزیل به یک پدیده جهانی تبدیل شد. رسانه‌ها هم سر شوخی رو باهاش باز کردن و روز تولدش رو با پله که اونم ۲۱ جولای بود و ۱۷۳ سانت قد داشت مقایسه میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q03JTOF22tYyHlQPXB4jb-unuX-QXQtMhH34FdRih0FqE_h72Dy6IBgKjv0J3CvZoZSY3oKJGO9YqgLRqaIQIIeJqLyaR35XzLgZpeRTZ0hsI9b7bcN_louK7sD5R2d-AkUWREhXU5TryiHusy9GEtK6JhyZKk5qUeuBh4cUyC_8waMAKWQkFmr-XUhVgWTs5VBL2E8-7LuMfmLvxhz-1kTuGm1mqfjXudk4cGpJbqX4Fy8ONxqgSAOaiT5OTxM4VnYxgo3RbWQMPWseyJRLA5r1DyABHR-T8rd8xjV6z_OOci4kK4M0u62aVuEe9ipjPoa10NJ6vhJGvjA_Z7H-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmssmHLLPsQSwR7p8AEIZEviUBdWLebU2JArPCXRJ05dAua8MxGDRMivMZGrE95ZzJBXI1qPLBe9m6EBlZVMgl-0Xq2QbQCEdZz-Kwep6LSn0WJ7qwRkpvo6cA9hUlKnYs_SXEjLWSBU1KGuDpJjiQvOczOe7X9MKM_dAQOtkpeFi2_cOYkhpV_9ysRyp4dqz2shdSIBpK3tc0h7LFHTha5fvceZ6Xw1ON3VKuVyLEECJXrJMf-rOHhN_HRq6k8gL-wV5UCPe_8l9lVv3lMJ_9gVzr1ChzK0udtzwg2I0eQzP3qQ5p46NBujZO54kcR4DNtg3wcIe_FezlHpvLGfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwXEUjAz1brf7GUWZjz3T1skFhP2LA99CxpHhlBQx4efOM8D_VrcaAMyfIKQlwd9u-M17rDDxaHWUVgm-5cMeS7q36-NKcxrscZx_D6nliSYx707KfHs_8nb1zhbVoMdFcR2GzY5w6yCsovWELtD7pUL068st0NUINrnfoRxi4apAvNAjzjjgdfVv3bO4H6CmA5ux6Nfjx2gJFaqFToPWLDd_uBBY-3_7s7HmZE-0K_2_iJDdlZDa1CK4bn_oRvMb4d6mTOxDLWNExSVIwne2Kj_DaztpeUl-K-eC22KgzNG83oQ3k7YMKxIAJbp8DlKRgs_tVu0aLpBjtRYjSsmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZN3pK9nqWVzrupnp_t4GRrh6eFpH08o2jmvx6gwOkK7qWF1tRPzvKCFVUFY49Ow_-REQdW8BGTcrLbZrig62Myp-duJ2ZpHcYPWBTCDKz0WDcqh1CyFKU7gevGpJm39QHMtqKGJIG5TWt9CWBsIcvdkZ8qOhJ-Ol8kwdebpKozsZhR5sJQjRoqS4bAVKV_znEdO_jytBXbEi6HycrIpjTb5PLS4I4LYhoptkTOwROUPxww8y_kZoo0VMuw2hilzI4RRmGMkIpuSTP8YH3V6OnHaBx2B8fqv0DjFek8aroyIqTHcC4HZILpJQqWdb6glu7Z7Uwwe7v4QU7K_UjE6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=EOs7Rhy1qJLA-hZ14yNLZlualnI6qKstiR56NbRTA9mDjF81d0nqDOIa7MJZraH8d-yelfiFD1zmXAPWu7uRrPoY0MxiIXDQpRFIJ2oazdVIfHSAlyYHOT8649ht9EVTS2QRNIIK9V-YPWdpoziBctxkdCeAm4rQdWBB7xHJWRhuEXbLCDOF5-CodVx9cZasKDyYy8Uiq3aWkBF3sCNelu6BQsBJza7ASXmQNH_4P7S9lMJSy35tIXTNXmDfO-BFNjq_t6likLfc6LygeiJsSVhyVrBS0lH1W76a8aNE0fGR21BSZ4CjS80lHuzVhLnjUwYR0dydnECcUdldDdVNlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=EOs7Rhy1qJLA-hZ14yNLZlualnI6qKstiR56NbRTA9mDjF81d0nqDOIa7MJZraH8d-yelfiFD1zmXAPWu7uRrPoY0MxiIXDQpRFIJ2oazdVIfHSAlyYHOT8649ht9EVTS2QRNIIK9V-YPWdpoziBctxkdCeAm4rQdWBB7xHJWRhuEXbLCDOF5-CodVx9cZasKDyYy8Uiq3aWkBF3sCNelu6BQsBJza7ASXmQNH_4P7S9lMJSy35tIXTNXmDfO-BFNjq_t6likLfc6LygeiJsSVhyVrBS0lH1W76a8aNE0fGR21BSZ4CjS80lHuzVhLnjUwYR0dydnECcUdldDdVNlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWQ_S-lOP7RQCpxf6__D9t0aXf6fFwg1qnwGtn7BkJC-MgT0D467Nr_rYaajxTsu5ZwpHnbyK_55ob8xKUBwvVFF9WG9fmycxr6EX24SelKDpV8XCkoFSslRIKaFdH4XsEEg0uHOgd62PGHu7uofisaKu2IKfEv1HlYzwq8zPrU38bUlTC6YOnmDsmTvMSnrQ3ZtZupo-Z6rqhocJlAcQ-2jaEHJ34X5bKeDdVxHpJQsOIX_YrSWz2cKs-CI6ViSsjL__86qSr4q9mab1XjjVFWxwJ6l8_05wCieXmFm4Quax1A2KBHfN55lFTnRy8ee2JIa7tFHfqJO6acJhGnp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
